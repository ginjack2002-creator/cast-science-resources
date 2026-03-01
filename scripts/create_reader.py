#!/usr/bin/env python3
"""
CAST Science Differentiated Readers Generator
Creates 4-level interactive notebook inserts (cut-and-paste PDFs)
for composition notebooks.

Pipeline: PARSE → CONTENT (Gemini 3.1 Pro) → IMAGES (Imagen 4) → RENDER (WeasyPrint) → VERIFY

Usage:
    python create_reader.py --lesson G05-L01          # Single lesson
    python create_reader.py --all                      # All Grade 5
    python create_reader.py --lesson G05-L01 --skip-images  # Skip image gen
    python create_reader.py --lesson G05-L01 --skip-content # Use cached content
"""

import os
import sys
import json
import time
import base64
import argparse
import requests
from pathlib import Path

# Add scripts dir to path for imports
SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

# Load env
import dotenv
dotenv.load_dotenv(Path.home() / '.env')

GOOGLE_API_KEY = os.environ.get('GOOGLE_AI_STUDIO_API_KEY', '')
OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY', '')

# Directories
BASE_DIR = SCRIPT_DIR.parent
TEMPLATE_DIR = BASE_DIR / 'templates' / 'reader'
OUTPUT_BASE = BASE_DIR / 'readers' / 'grade-05'

# Reading levels config
LEVELS = {
    'advanced': {
        'label': 'Advanced',
        'css_key': 'advanced',
        'word_count': (350, 400),
        'sentence_style': 'compound-complex sentences, domain vocabulary used freely',
        'scaffolding': 'Go Deeper extension question only, no margin notes or sentence starters',
    },
    'grade': {
        'label': 'Grade Level',
        'css_key': 'grade',
        'word_count': (280, 320),
        'sentence_style': 'mix of simple and compound sentences, key terms bolded with inline definitions',
        'scaffolding': '2 Think About It margin prompts, key terms bolded',
    },
    'below': {
        'label': 'Below Level',
        'css_key': 'below',
        'word_count': (200, 250),
        'sentence_style': 'simple sentences (10-15 words average), numbered sequences',
        'scaffolding': 'Margin definitions, sentence starters, Check prompts every paragraph',
    },
    'esl': {
        'label': 'ESL-Assisted',
        'css_key': 'esl',
        'word_count': (180, 220),
        'sentence_style': 'short simple sentences (8-12 words), present tense, active voice',
        'scaffolding': 'Word bank header, labeled diagram, bilingual cognate sidebar, bullet key points, sentence frames everywhere',
    },
}

# Cost tracking
total_content_cost = 0.0
total_image_cost = 0.0


# ==============================================================
# PHASE 1: PARSE — Load lesson data + reader hooks
# ==============================================================

def load_lesson_data(lesson_id):
    """Load lesson data from the appropriate data file."""
    lesson_num = int(lesson_id.split('-L')[1])

    if lesson_num == 1:
        return get_L01_data()
    else:
        import lesson_data_L02_L10 as ld
        # ALL_LESSONS is a list; get the right dict by variable name
        var_name = f"L{lesson_num:02d}"
        if hasattr(ld, var_name):
            return getattr(ld, var_name)
        print(f"[ERROR] Lesson {var_name} not found in lesson_data_L02_L10")
        sys.exit(1)


def get_L01_data():
    """Return G05-L01 lesson data (inline since it was the exemplar)."""
    return {
        "id": "G05-L01",
        "title": "When Trees Become Matches",
        "subtitle": "California's Burning Season and the Earth Systems That Fuel It",
        "ngss": "5-ESS2-1",
        "ngss_desc": "Develop a model using an example to describe ways the geosphere, biosphere, hydrosphere, and/or atmosphere interact.",
        "big_question": "Why does California burn every single year?",
        "objectives": [
            "Model how lack of rainfall affects vegetation",
            "Trace cause-and-effect relationships between drought and fire conditions",
            "Explain how Earth systems (atmosphere, biosphere, hydrosphere) interact",
            "Predict what happens when one part of the system changes"
        ],
        "vocabulary": [
            ("Geosphere", "The solid Earth—rocks, mountains, soil, and landforms"),
            ("Biosphere", "All living things on Earth—plants, animals, fungi, bacteria"),
            ("Hydrosphere", "All water on Earth—oceans, rivers, groundwater, ice"),
            ("Atmosphere", "The blanket of gases surrounding Earth—our air")
        ],
        "components": [
            ("Rainfall", "Precipitation from atmosphere", True),
            ("Wind", "Air movement that spreads flames", True),
            ("Dry Vegetation", "Plants and trees that become fuel", False),
            ("Fire Spread", "How fast and far fire moves", False)
        ],
        "relationships": [
            ("Rainfall to Dry Vegetation", "NEGATIVE (-)", "More rain means less dry vegetation."),
            ("Dry Vegetation to Fire Spread", "POSITIVE (+)", "More dry vegetation means fire spreads faster."),
            ("Wind to Fire Spread", "POSITIVE (+)", "More wind pushes fire farther and faster.")
        ],
        "extend_components": [
            ("Temperature", "Hot days dry out plants faster"),
            ("Humidity", "Dry air pulls moisture from living plants"),
            ("Human Activity", "Campfires, power lines, and construction can spark fires")
        ],
        "career": "Wildland Firefighters and Fire Scientists protect communities and study fire behavior. They earn $40,000-$90,000/year.",
        "discoveries": [
            "Rainfall and dry vegetation have an inverse relationship",
            "Wind makes fire spread dramatically faster",
            "When multiple factors combine, fire behavior becomes extreme",
            "Earth systems are interconnected—changes in one affect all others"
        ],
        "reflections": [
            "How do Earth's atmosphere and biosphere interact during fire season?",
            "What role does the hydrosphere play in preventing wildfires?",
            "Why are some years worse for fires than others?",
            "How do firefighters use their understanding of systems to fight fires?",
            "What could humans do to reduce wildfire risk?"
        ],
        "background_intro": "California wildfires are driven by the interaction of multiple Earth systems. The atmosphere controls wind and rainfall. The biosphere provides fuel in the form of vegetation. The hydrosphere determines moisture levels.",
        "background_sections": [
            ("The Fire Triangle", "Fire needs three things: fuel (dry vegetation), oxygen (wind provides fresh air), and heat (temperature or an ignition source). Remove any one and fire cannot exist."),
            ("California's Fire Season", "California's Mediterranean climate creates a natural fire cycle: wet winters grow vegetation, hot dry summers cure it into fuel. Santa Ana winds in fall provide the final ingredient."),
            ("Earth System Interactions", "Wildfires show how Earth's systems interact. The atmosphere (weather), biosphere (vegetation), hydrosphere (drought), and geosphere (terrain) all play roles."),
            ("Human Factors", "90% of California wildfires are human-caused. Power lines, campfires, and equipment can ignite fires during high-risk conditions.")
        ],
        "misconceptions": [
            ("Wildfires are always bad", "Fire is a natural part of many ecosystems. Some plants need fire to reproduce. The problem is when fires burn where people live.", "Ask: Why do some pine cones only open in extreme heat?"),
            ("Climate and weather are the same thing", "Weather is daily conditions; climate is the long-term pattern. California's climate creates fire conditions, but weather determines when fires start.", "Compare today's weather to California's overall climate pattern."),
            ("Firefighters just spray water on fires", "Modern firefighting uses science—weather models, fuel moisture data, and terrain analysis—to predict fire behavior and plan strategy.", "Research how fire behavior analysts work.")
        ]
    }


def load_reader_hooks(lesson_id):
    """Load reader hooks for the lesson."""
    from reader_hooks_G05 import READER_HOOKS
    if lesson_id not in READER_HOOKS:
        print(f"[ERROR] No reader hooks for {lesson_id}")
        sys.exit(1)
    return READER_HOOKS[lesson_id]


def parse_lesson(lesson_id):
    """Combine lesson data with reader hooks into unified config."""
    data = load_lesson_data(lesson_id)
    hooks = load_reader_hooks(lesson_id)

    # Parse components into structured format
    components = []
    for c in data['components']:
        components.append({
            'name': c[0],
            'description': c[1],
            'is_external': c[2]
        })

    # Parse relationships
    relationships = []
    for r in data['relationships']:
        parts = r[0].split(' to ')
        sign = '+' if 'POSITIVE' in r[1] else '-'
        relationships.append({
            'from_comp': parts[0].strip(),
            'to_comp': parts[1].strip() if len(parts) > 1 else '',
            'sign': sign,
            'reason': r[2]
        })

    # Parse vocabulary
    vocabulary = []
    for v in data['vocabulary']:
        vocabulary.append({
            'term': v[0],
            'definition': v[1]
        })

    # Parse extend components from hooks
    extend_components = []
    for ec in hooks['extend_components']:
        extend_components.append({
            'name': ec[0],
            'why': ec[1]
        })

    return {
        'lesson_id': lesson_id,
        'grade': '5th Grade',
        'title': data['title'],
        'subtitle': data['subtitle'],
        'ngss': data['ngss'],
        'big_question': data['big_question'],
        'objectives': data['objectives'],
        'vocabulary': vocabulary,
        'components': components,
        'relationships': relationships,
        'extend_components': extend_components,
        'discoveries': data['discoveries'],
        'reflections': data['reflections'],
        'background_intro': data['background_intro'],
        'background_sections': data['background_sections'],
        'scientist': hooks['scientist'],
        'additional_career': hooks['additional_career'],
        'spotlight': hooks['spotlight'],
        'data': hooks['data'],
        'existing_career': data['career'],
    }


# ==============================================================
# PHASE 2: CONTENT — Generate 4-level text via Gemini 3.1 Pro
# ==============================================================

def call_gemini(prompt, temperature=0.7):
    """Call Google AI Studio Gemini 3.1 Pro API."""
    global total_content_cost
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
            # Track approximate cost
            usage = data.get('usageMetadata', {})
            input_tokens = usage.get('promptTokenCount', 0)
            output_tokens = usage.get('candidatesTokenCount', 0)
            cost = (input_tokens * 1.25 / 1_000_000) + (output_tokens * 10 / 1_000_000)
            total_content_cost += cost
            print(f"    [Gemini] {input_tokens} in / {output_tokens} out (${cost:.4f})")
            return text
        else:
            print(f"    [ERROR] Gemini {r.status_code}: {r.text[:300]}")
            return None
    except Exception as e:
        print(f"    [ERROR] Gemini exception: {e}")
        return None


def generate_content_for_level(config, level_key):
    """Generate reader content for a specific reading level."""
    level = LEVELS[level_key]
    sci = config['scientist']

    # Build the generation prompt
    prompt = f"""You are an expert science curriculum writer creating a differentiated reader for 5th grade students.

LESSON: {config['title']} ({config['lesson_id']})
NGSS: {config['ngss']}
BIG QUESTION: {config['big_question']}
READING LEVEL: {level['label']}

SCIENTIST CHARACTER:
- Name: {sci['name']}
- Title: {sci['title']}
- Workplace: {sci['workplace']}
- What they model: {sci['what_they_model']}

SYSTEM COMPONENTS (from the lesson model):
{json.dumps([{'name': c['name'], 'description': c['description'], 'type': 'External' if c['is_external'] else 'Internal'} for c in config['components']], indent=2)}

RELATIONSHIPS:
{json.dumps([{'from': r['from_comp'], 'to': r['to_comp'], 'sign': r['sign'], 'reason': r['reason']} for r in config['relationships']], indent=2)}

VOCABULARY:
{json.dumps(config['vocabulary'], indent=2)}

BACKGROUND:
{config['background_intro']}

EXTEND COMPONENTS (for "What Else?" section):
{json.dumps(config['extend_components'], indent=2)}

WRITING GUIDELINES:
- Word count: {level['word_count'][0]}-{level['word_count'][1]} words for the main story
- Sentence style: {level['sentence_style']}
- Scaffolding: {level['scaffolding']}
- Frame the story from {sci['name']}'s perspective as a {sci['title']}
- This is NOT a textbook — it's a discussion fuel piece
- Suggest new components students could add to their models
- Career-framed, workforce-realistic, forward-looking
- Age-appropriate for 10-11 year olds
- No divisive politics, nothing shocking/gross
- Use the scientist as a relatable character

CONTENT RULES:
- Do NOT repeat exact content from the lesson slides/activities
- Focus on what the scientist DOES, THINKS, and MODELS daily
- Naturally introduce system components as tools the scientist uses
- Hint at additional components not in the basic model

OUTPUT FORMAT (JSON):
{{
    "story": {{
        "title": "story title incorporating scientist and their work",
        "text": "the full story text (HTML allowed: <strong> for bold terms, <br> for breaks)",
        "think_abouts": ["prompt 1", "prompt 2"] or [] for advanced,
        "go_deeper": "extension question" or null for non-advanced,
        "margin_defs": [{{"term": "word", "definition": "simple def"}}] for below level, else [],
        "check_prompts": ["check question 1"] for below level, else [],
        "word_bank": ["word1", "word2"] for ESL, else [],
        "cognate_sidebar": [{{"english": "word", "spanish": "cognado"}}] for ESL, else []
    }},
    "vocabulary": [
        {{
            "term": "term",
            "definition": "level-appropriate definition",
            "use_sentence": "example sentence using the term",
            "phonetic": "pronunciation guide" or null,
            "cognate": "Spanish cognate" or null
        }}
    ],
    "discussion_cards": [
        {{
            "prompt": "open-ended discussion question",
            "frame": "sentence starter for below/ESL" or null
        }}
    ],
    "organizer": {{
        "title": "Graphic Organizer Title",
        "type": "cause-effect" or "t-chart",
        "boxes": [{{"label": "Cause", "content": "pre-filled or empty"}}] for cause-effect,
        "left_header": "header" for t-chart,
        "right_header": "header" for t-chart,
        "left_items": ["item1", "", ""] for t-chart,
        "right_items": ["item1", "", ""] for t-chart
    }},
    "reflection_frames": {{
        "knew": "Before reading, I already knew that ___" or null,
        "learned": "From the story, I learned that ___" or null,
        "wonder": "Now I wonder ___" or null
    }}
}}

Generate the complete content now. Return ONLY valid JSON."""

    print(f"  Generating {level['label']} content...")
    raw = call_gemini(prompt, temperature=0.7)
    if not raw:
        return None

    try:
        content = json.loads(raw)
        return content
    except json.JSONDecodeError as e:
        # Try to extract JSON from response
        try:
            start = raw.index('{')
            end = raw.rindex('}') + 1
            content = json.loads(raw[start:end])
            return content
        except:
            print(f"    [ERROR] Could not parse JSON: {e}")
            print(f"    Raw response: {raw[:500]}")
            return None


def generate_all_content(config, output_dir, skip_content=False):
    """Generate content for all 4 levels, with caching."""
    content_dir = output_dir / 'content'
    content_dir.mkdir(parents=True, exist_ok=True)

    all_content = {}

    for level_key in LEVELS:
        cache_file = content_dir / f'content-{level_key}.json'

        if skip_content and cache_file.exists():
            print(f"  [CACHE] Loading {level_key} from cache")
            with open(cache_file, 'r', encoding='utf-8') as f:
                all_content[level_key] = json.load(f)
            continue

        content = generate_content_for_level(config, level_key)
        if content:
            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump(content, f, indent=2, ensure_ascii=False)
            all_content[level_key] = content
            print(f"    [OK] {level_key} cached")
        else:
            print(f"    [FAIL] {level_key} content generation failed")

        # Rate limiting between API calls
        time.sleep(3)

    return all_content


# ==============================================================
# PHASE 3: IMAGES — Generate via OpenRouter (Gemini Flash Image)
# ==============================================================

def generate_image(scene, filename, images_dir):
    """Generate a single image via OpenRouter NanoBanana."""
    global total_image_cost
    filepath = images_dir / filename

    if filepath.exists():
        print(f"    [SKIP] {filename} already exists")
        return str(filepath)

    prompt = f"""Create a photorealistic, cinematic, ultra-crisp image of {scene} featuring a diverse, multicultural group with Black people centered (a mix of skin tones and ethnicities represented), age-accurate for 10-11 years old (no one looks like an adult if they're a kid).

Style: modern education / future-ready / "middle school coolness"—confident, aspirational, realistic.

Composition: clean framing, strong focal subject, natural body proportions, believable clothing textures, realistic hair detail (coils, curls, locs, braids), subtle emotion and authentic interaction.

Camera/lighting: soft natural window light + gentle fill, shallow depth of field, 35mm/50mm look, high dynamic range, sharp eyes, realistic skin texture.

Quality: high-resolution, crisp edges, minimal noise, professional editorial photo. HIGH CONTRAST suitable for grayscale printing.

If tech overlays appear: keep them subtle, readable, and physically plausible (not cluttered), with realistic reflections and occlusion."""

    print(f"    Generating: {filename}...")
    try:
        r = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json"},
            json={
                "model": "google/gemini-2.5-flash-image",
                "messages": [{"role": "user", "content": prompt}],
                "modalities": ["image", "text"]
            },
            timeout=180
        )
        if r.status_code == 200:
            data = r.json()
            imgs = data.get("choices", [{}])[0].get("message", {}).get("images", [])
            if imgs:
                img = imgs[0]
                url = img.get("image_url", {}).get("url", "") if isinstance(img, dict) else ""
                if url.startswith("data:image"):
                    images_dir.mkdir(parents=True, exist_ok=True)
                    with open(filepath, "wb") as f:
                        f.write(base64.b64decode(url.split(",")[1]))
                    cost = data.get("usage", {}).get("cost", 0)
                    total_image_cost += cost
                    print(f"    [OK] {filename} (${cost:.4f})")
                    return str(filepath)
            print(f"    [!] No image in response for {filename}")
            return None
        else:
            print(f"    [X] {r.status_code}: {r.text[:200]}")
            return None
    except Exception as e:
        print(f"    [X] {e}")
        return None


def generate_all_images(config, images_dir, skip_images=False):
    """Generate 4 images per reader (shared across all levels)."""
    if skip_images:
        print("  [SKIP] Image generation skipped")
        # Return existing images if any
        images = {}
        for key in ['cover-hero', 'story-inline', 'spotlight', 'career-card']:
            fp = images_dir / f'{key}.png'
            if fp.exists():
                images[key.replace('-', '_')] = str(fp)
        return images

    print(f"\n  Generating images for {config['lesson_id']}...")
    sci = config['scientist']
    images = {}

    # 1. Cover hero — scientist/career in action
    images['cover'] = generate_image(
        f"a {sci['title']} ({sci['name']}'s role) at work in {sci['workplace']}, "
        f"analyzing data on monitors showing {config['title'].lower()} models, "
        f"professional Black woman scientist in modern lab/field setting, "
        f"with 5th grade students visiting and watching in awe",
        "cover-hero.png", images_dir
    )
    time.sleep(3)

    # 2. Story inline — science narrative visual
    images['story_inline'] = generate_image(
        f"a dramatic but educational visualization related to {config['title']}: "
        f"{config['subtitle']}, showing the science concept in action, "
        f"high contrast for grayscale printing, documentary style",
        "story-inline.png", images_dir
    )
    time.sleep(3)

    # 3. Spotlight — real-world case study
    images['spotlight'] = generate_image(
        f"a photorealistic scene related to: {config['spotlight']['title']}, "
        f"educational documentary style, high contrast, dramatic but appropriate "
        f"for 10-11 year old students",
        "spotlight.png", images_dir
    )
    time.sleep(3)

    # 4. Career card — professionals
    images['career'] = generate_image(
        f"a split image: on the left a {sci['title']} at work in {sci['workplace']}, "
        f"on the right a {config['additional_career']['name']} at their workplace, "
        f"both looking professional and confident, diverse representation, "
        f"clean portrait style with workplace context visible",
        "career-card.png", images_dir
    )

    return images


# ==============================================================
# PHASE 4: RENDER — Jinja2 HTML → Playwright (Chromium) → PDF
# ==============================================================

def render_pdf(config, content, images, level_key, output_dir):
    """Render a single-level PDF using Jinja2 + Playwright Chromium."""
    from jinja2 import Environment, FileSystemLoader
    from playwright.sync_api import sync_playwright

    level = LEVELS[level_key]
    print(f"  Rendering {level['label']} PDF...")

    # Set up Jinja2
    env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))
    template = env.get_template('reader.html')

    # CSS base URL (absolute file:// path for Playwright)
    css_dir = TEMPLATE_DIR / 'css'
    css_base_url = f'file:///{css_dir.resolve().as_posix()}'

    # Merge content into template context
    ctx = {
        'lesson_id': config['lesson_id'],
        'grade': config['grade'],
        'lesson_title': config['title'],
        'lesson_subtitle': config['subtitle'],
        'level_label': level['label'],
        'level_key': level['css_key'],
        'css_base_url': css_base_url,
        'scientist': config['scientist'],
        'additional_career': config['additional_career'],
        'spotlight': config['spotlight'],
        'data': config['data'],
        'components': config['components'],
        'relationships': config['relationships'],
        'extend_components': config['extend_components'],
        'images': images,

        # From generated content
        'vocabulary': content.get('vocabulary', []),
        'story': content.get('story', {}),
        'discussion_cards': content.get('discussion_cards', []),
        'organizer': content.get('organizer', {}),
        'reflection_frames': content.get('reflection_frames', {}),
    }

    # Render HTML
    html_str = template.render(**ctx)

    # Save HTML temp file (Playwright needs file:// URL for CSS to load)
    html_file = output_dir / f"_temp_{level_key}.html"
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_str)

    # Render PDF via Playwright Chromium
    output_file = output_dir / f"{config['lesson_id']}-Reader-{level['label'].replace(' ', '')}.pdf"
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f'file:///{html_file.resolve().as_posix()}')
        page.pdf(
            path=str(output_file),
            format='Letter',
            margin={'top': '0.35in', 'bottom': '0.35in', 'left': '0.4in', 'right': '0.4in'},
            print_background=True
        )
        browser.close()

    # Cleanup temp HTML
    html_file.unlink(missing_ok=True)

    # Verify
    size_kb = output_file.stat().st_size / 1024
    print(f"    [OK] {output_file.name} ({size_kb:.0f} KB)")
    return str(output_file)


# ==============================================================
# PHASE 5: VERIFY — Check output quality
# ==============================================================

def verify_outputs(lesson_id, output_dir):
    """Verify generated PDFs and report stats."""
    pdfs = list(output_dir.glob('*.pdf'))
    images = list((output_dir / 'images').glob('*.png')) if (output_dir / 'images').exists() else []
    content_files = list((output_dir / 'content').glob('*.json')) if (output_dir / 'content').exists() else []

    print(f"\n{'='*60}")
    print(f"VERIFICATION: {lesson_id}")
    print(f"{'='*60}")
    print(f"  PDFs generated: {len(pdfs)}/4")
    for p in sorted(pdfs):
        size_kb = p.stat().st_size / 1024
        print(f"    {p.name}: {size_kb:.0f} KB")
    print(f"  Images generated: {len(images)}/4")
    for img in sorted(images):
        size_kb = img.stat().st_size / 1024
        print(f"    {img.name}: {size_kb:.0f} KB")
    print(f"  Content cached: {len(content_files)}/4")

    ok = len(pdfs) == 4
    if ok:
        print(f"\n  [PASS] All 4 levels generated successfully!")
    else:
        print(f"\n  [FAIL] Missing {4 - len(pdfs)} PDF(s)")
    return ok


# ==============================================================
# MAIN PIPELINE
# ==============================================================

def generate_reader(lesson_id, skip_images=False, skip_content=False):
    """Full pipeline for one lesson."""
    print(f"\n{'='*60}")
    print(f"GENERATING READER: {lesson_id}")
    print(f"{'='*60}")

    # Output directory
    output_dir = OUTPUT_BASE / lesson_id
    output_dir.mkdir(parents=True, exist_ok=True)
    images_dir = output_dir / 'images'
    images_dir.mkdir(parents=True, exist_ok=True)

    # Phase 1: Parse
    print("\n[PHASE 1] Parsing lesson data + hooks...")
    config = parse_lesson(lesson_id)
    print(f"  Title: {config['title']}")
    print(f"  Scientist: {config['scientist']['name']}, {config['scientist']['title']}")
    print(f"  Spotlight: {config['spotlight']['title']}")

    # Phase 2: Content
    print("\n[PHASE 2] Generating leveled content...")
    all_content = generate_all_content(config, output_dir, skip_content)
    if len(all_content) < 4:
        print(f"  [WARNING] Only {len(all_content)}/4 content levels generated")

    # Phase 3: Images
    print("\n[PHASE 3] Generating images...")
    images = generate_all_images(config, images_dir, skip_images)

    # Phase 4: Render
    print("\n[PHASE 4] Rendering PDFs...")
    for level_key in LEVELS:
        if level_key in all_content:
            try:
                render_pdf(config, all_content[level_key], images, level_key, output_dir)
            except Exception as e:
                print(f"    [ERROR] {level_key}: {e}")
                import traceback
                traceback.print_exc()

    # Phase 5: Verify
    ok = verify_outputs(lesson_id, output_dir)

    return ok


def main():
    parser = argparse.ArgumentParser(description='CAST Science Differentiated Readers Generator')
    parser.add_argument('--lesson', type=str, help='Lesson ID (e.g., G05-L01)')
    parser.add_argument('--all', action='store_true', help='Generate all Grade 5 readers')
    parser.add_argument('--skip-images', action='store_true', help='Skip image generation')
    parser.add_argument('--skip-content', action='store_true', help='Use cached content (skip LLM)')
    args = parser.parse_args()

    if not args.lesson and not args.all:
        parser.print_help()
        sys.exit(1)

    OUTPUT_BASE.mkdir(parents=True, exist_ok=True)

    if args.all:
        lessons = [f"G05-L{i:02d}" for i in range(1, 11)]
    else:
        lessons = [args.lesson]

    results = {}
    for lesson_id in lessons:
        ok = generate_reader(lesson_id, args.skip_images, args.skip_content)
        results[lesson_id] = ok

    # Summary
    print(f"\n{'='*60}")
    print("GENERATION SUMMARY")
    print(f"{'='*60}")
    passed = sum(1 for v in results.values() if v)
    for lid, ok in results.items():
        print(f"  {'PASS' if ok else 'FAIL'} {lid}")
    print(f"\n  Total: {passed}/{len(results)} passed")
    print(f"  Content API cost: ${total_content_cost:.4f}")
    print(f"  Image API cost: ${total_image_cost:.4f}")
    print(f"  Total cost: ${total_content_cost + total_image_cost:.4f}")


if __name__ == '__main__':
    main()
