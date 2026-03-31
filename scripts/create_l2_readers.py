#!/usr/bin/env python3
"""
Generate Differentiated Readers for L2 Lessons (Grades 4-8)
===========================================================
Creates 4-level reading passages (Advanced, Grade, Below, ESL)
for all 35 Level 2 lessons using Gemini API for content generation.

Outputs JSON content files that can be rendered to HTML/PDF.

Usage:
    python create_l2_readers.py --grade 04_L2 --all
    python create_l2_readers.py --grade 06_L2 --lesson 1
    python create_l2_readers.py --all
"""

import os, sys, json, time, argparse, importlib.util, requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path.home() / '.env')

GOOGLE_API_KEY = os.environ.get('GOOGLE_AI_STUDIO_API_KEY', '')
SCRIPTS_DIR = Path(__file__).parent
BASE_DIR = SCRIPTS_DIR.parent

# Reading levels
LEVELS = {
    'advanced': {
        'label': 'Advanced',
        'word_count': (350, 400),
        'sentence_style': 'compound-complex sentences, domain vocabulary used freely',
        'scaffolding': 'Go Deeper extension question only',
    },
    'grade': {
        'label': 'Grade Level',
        'word_count': (280, 320),
        'sentence_style': 'mix of simple and compound sentences, key terms bolded with inline definitions',
        'scaffolding': '2 Think About It margin prompts, key terms bolded',
    },
    'below': {
        'label': 'Below Level',
        'word_count': (200, 250),
        'sentence_style': 'simple sentences (10-15 words average), numbered sequences',
        'scaffolding': 'Margin definitions, sentence starters, Check prompts every paragraph',
    },
    'esl': {
        'label': 'ESL-Assisted',
        'word_count': (180, 220),
        'sentence_style': 'short simple sentences (8-12 words), present tense, active voice',
        'scaffolding': 'Word bank header, labeled diagram, bilingual cognate sidebar, sentence frames',
    },
}

# Grade age mapping
GRADE_AGES = {
    "04": "9-10 year olds (4th grade)",
    "05": "10-11 year olds (5th grade)",
    "06": "11-12 year olds (6th grade)",
    "07": "12-13 year olds (7th grade)",
    "08": "13-14 year olds (8th grade)",
}

total_cost = 0.0


def load_lesson_data(grade, lesson_num):
    """Load lesson data from the appropriate L2 data file."""
    grade_num = grade.split("_")[0]
    data_file = SCRIPTS_DIR / f"lesson_data_G{grade_num}_L2.py"

    if not data_file.exists():
        print(f"ERROR: {data_file} not found")
        return None

    spec = importlib.util.spec_from_file_location("ld", str(data_file))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    key = f"L{lesson_num:02d}"
    if hasattr(mod, key):
        return getattr(mod, key)
    return None


def load_reader_hooks(lesson_id):
    """Load reader hooks for an L2 lesson."""
    hooks_file = SCRIPTS_DIR / "reader_hooks_L2.py"
    if not hooks_file.exists():
        return None

    spec = importlib.util.spec_from_file_location("hooks", str(hooks_file))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    hooks = getattr(mod, "READER_HOOKS_L2", {})
    return hooks.get(lesson_id)


def call_gemini(prompt, temperature=0.7):
    """Call Gemini API for content generation."""
    global total_cost
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-pro:generateContent?key={GOOGLE_API_KEY}"

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": 8192,
            "responseMimeType": "application/json"
        }
    }

    try:
        r = requests.post(url, json=payload, timeout=120)
        if r.status_code == 200:
            data = r.json()
            text = data['candidates'][0]['content']['parts'][0]['text']
            usage = data.get('usageMetadata', {})
            cost = (usage.get('promptTokenCount', 0) * 1.25 / 1_000_000) + \
                   (usage.get('candidatesTokenCount', 0) * 10 / 1_000_000)
            total_cost += cost
            return text
        else:
            print(f"    [ERROR] Gemini {r.status_code}: {r.text[:200]}")
            return None
    except Exception as e:
        print(f"    [ERROR] {e}")
        return None


def generate_reader_content(data, hooks, level_key, grade_num):
    """Generate reader content for a specific reading level."""
    level = LEVELS[level_key]
    age_desc = GRADE_AGES.get(grade_num, "students")

    # Build scientist info
    sci = hooks.get("scientist", {}) if hooks else {}
    sci_name = sci.get("name", "Dr. Sarah Chen")
    sci_title = sci.get("title", "Research Scientist")
    sci_workplace = sci.get("workplace", "National Science Lab")
    sci_models = sci.get("what_they_model", "complex systems")

    # Extend components
    extend = hooks.get("extend_components", []) if hooks else []
    extend_text = "\n".join([f"- {e[0]}: {e[1]}" for e in extend]) if extend else "None specified"

    # Build component info
    comp_info = json.dumps([{
        'name': c[0], 'description': c[1],
        'type': 'External' if c[2] else 'Internal'
    } for c in data.get('components', [])], indent=2)

    rel_info = json.dumps([{
        'connection': r[0], 'type': r[1], 'reason': r[2]
    } for r in data.get('relationships', [])], indent=2)

    vocab_info = json.dumps([{
        'term': v[0], 'definition': v[1]
    } for v in data.get('vocabulary', [])], indent=2)

    prompt = f"""You are an expert science curriculum writer creating a differentiated reader for {age_desc}.

LESSON: {data['title']} ({data['id']})
NGSS: {data.get('ngss', '')}
BIG QUESTION: {data.get('big_question', '')}
READING LEVEL: {level['label']}

SCIENTIST CHARACTER:
- Name: {sci_name}
- Title: {sci_title}
- Workplace: {sci_workplace}
- What they model: {sci_models}

SYSTEM COMPONENTS:
{comp_info}

RELATIONSHIPS:
{rel_info}

VOCABULARY:
{vocab_info}

BACKGROUND:
{data.get('background_intro', '')}

EXTEND COMPONENTS:
{extend_text}

WRITING GUIDELINES:
- Word count: {level['word_count'][0]}-{level['word_count'][1]} words for the main story
- Sentence style: {level['sentence_style']}
- Scaffolding: {level['scaffolding']}
- Frame the story from {sci_name}'s perspective as a {sci_title}
- This is NOT a textbook — it's discussion fuel
- Career-framed, workforce-realistic, forward-looking
- Age-appropriate for {age_desc}
- No divisive politics, nothing shocking

OUTPUT FORMAT (JSON):
{{
    "story": {{
        "title": "story title incorporating scientist and their work",
        "text": "the full story text (HTML: <strong> for bold terms, <br> for breaks)",
        "think_abouts": ["prompt 1", "prompt 2"],
        "go_deeper": "extension question" or null,
        "margin_defs": [{{"term": "word", "definition": "simple def"}}],
        "check_prompts": ["check question"],
        "word_bank": ["word1", "word2"],
        "cognate_sidebar": [{{"english": "word", "spanish": "cognado"}}]
    }},
    "vocabulary": [
        {{
            "term": "term",
            "definition": "level-appropriate definition",
            "use_sentence": "example sentence",
            "phonetic": "pronunciation" or null,
            "cognate": "Spanish cognate" or null
        }}
    ],
    "discussion_cards": [
        {{
            "prompt": "open-ended discussion question",
            "frame": "sentence starter" or null
        }}
    ],
    "reflection_frames": {{
        "knew": "Before reading, I already knew that ___",
        "learned": "From the story, I learned that ___",
        "wonder": "Now I wonder ___"
    }}
}}

Generate complete content. Return ONLY valid JSON."""

    raw = call_gemini(prompt, temperature=0.7)
    if not raw:
        return None

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        try:
            start = raw.index('{')
            end = raw.rindex('}') + 1
            return json.loads(raw[start:end])
        except:
            print(f"    [ERROR] Could not parse JSON")
            return None


def generate_readers_for_lesson(grade, lesson_num):
    """Generate all 4 reading levels for one lesson."""
    grade_num = grade.split("_")[0]
    data = load_lesson_data(grade, lesson_num)
    if not data:
        print(f"  SKIP: No data for lesson {lesson_num}")
        return

    lesson_id = data["id"]
    hooks = load_reader_hooks(lesson_id)

    # Output directory
    output_dir = BASE_DIR / "materials" / f"grade-{grade_num}" / "level-2" / f"G{grade_num}L2-L{lesson_num:02d}" / "readers"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n  {lesson_id}: {data['title']}")

    for level_key in LEVELS:
        cache_file = output_dir / f"content-{level_key}.json"

        if cache_file.exists():
            print(f"    [CACHE] {level_key} already exists")
            continue

        print(f"    Generating {LEVELS[level_key]['label']}...")
        content = generate_reader_content(data, hooks, level_key, grade_num)

        if content:
            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump(content, f, indent=2, ensure_ascii=False)
            print(f"    [OK] {level_key} saved")
        else:
            print(f"    [FAIL] {level_key}")

        time.sleep(3)  # Rate limit


def main():
    parser = argparse.ArgumentParser(description="Generate L2 Differentiated Readers")
    parser.add_argument("--grade", help="Grade (e.g., 04_L2, 06_L2)")
    parser.add_argument("--lesson", type=int, help="Lesson number")
    parser.add_argument("--all", action="store_true", help="All L2 lessons")

    args = parser.parse_args()

    if args.all and not args.grade:
        # All grades
        grades = ["04_L2", "05_L2", "06_L2", "07_L2", "08_L2"]
        for g in grades:
            print(f"\n{'='*60}")
            print(f"Grade {g}")
            print(f"{'='*60}")
            for i in range(1, 8):
                generate_readers_for_lesson(g, i)
    elif args.grade and args.all:
        for i in range(1, 8):
            generate_readers_for_lesson(args.grade, i)
    elif args.grade and args.lesson:
        generate_readers_for_lesson(args.grade, args.lesson)
    else:
        print("Usage: python create_l2_readers.py --grade 06_L2 --all")
        print("       python create_l2_readers.py --all")
        sys.exit(1)

    print(f"\nTotal Gemini API cost: ${total_cost:.4f}")
    print("Done!")


if __name__ == "__main__":
    main()
