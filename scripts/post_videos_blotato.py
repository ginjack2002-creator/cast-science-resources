#!/usr/bin/env python3
"""
Upload educational videos to YouTube and promote on social media via Blotato API.

Workflow:
1. Create GitHub release on remotion-studio repo → public download URLs
2. Upload each video to YouTube via Blotato (ModelIt! in Action channel)
3. Post promotional content to Facebook, Instagram, LinkedIn, X, TikTok

Usage:
    python post_videos_blotato.py --youtube           # Upload all to YouTube
    python post_videos_blotato.py --promote           # Post promos to social media
    python post_videos_blotato.py --all               # YouTube + social media
    python post_videos_blotato.py --dry-run --all     # Preview everything
    python post_videos_blotato.py --release-only      # Just create GitHub release
"""

import os, sys, json, time, argparse, subprocess, requests
from pathlib import Path
from datetime import datetime, timedelta, timezone

import dotenv
dotenv.load_dotenv(Path.home() / '.env')

BLOTATO_API_KEY = os.environ.get('BLOTATO_API_KEY', '')
BLOTATO_BASE = "https://backend.blotato.com/v2"
HEADERS = {
    "blotato-api-key": BLOTATO_API_KEY,
    "Content-Type": "application/json"
}

# Connected Blotato accounts
ACCOUNTS = {
    "youtube":   "28826",
    "facebook":  "16257",
    "instagram": "25818",
    "linkedin":  "10375",
    "twitter":   "10836",
    "tiktok":    "30219",
}

FB_PAGE_ID = "748341445039609"
MODELIT_URL = "https://modelit.io"
GITHUB_REPO = "alexandriasworld1234-source/remotion-studio"
RELEASE_TAG = "v1.0-cast-videos"

VIDEOS_DIR = Path.home() / "remotion-studio" / "out"

# ─── Video Catalog ────────────────────────────────────────────────────────────

VIDEOS = {
    # ═══ Grade 5 Lessons ═══
    "G05-L01-wildfires.mp4": {
        "title": "When Trees Become Matches — Wildfire Systems",
        "grade": "Grade 5", "lesson": "L01",
        "ngss": "5-ESS2-1",
        "topic": "Wildfires and Earth System Interactions",
        "vocab": ["Rainfall", "Dry Vegetation", "Fire Spread", "Wind"],
        "desc": "Students model why California wildfires happen by building a cause-and-effect model of drought, dry vegetation, and fire spread. Discover how Earth's atmosphere, biosphere, and hydrosphere interact to create wildfire conditions.",
        "hook": "Why does California keep catching fire?",
        "careers": ["Fire Behavior Analyst", "Wildland Firefighter", "Climate Scientist"],
    },
    "G05-L02-natures-recycling.mp4": {
        "title": "Nature's Recycling System — Decomposition",
        "grade": "Grade 5", "lesson": "L02",
        "ngss": "5-LS2-1",
        "topic": "Decomposition and Matter Cycling",
        "vocab": ["Decomposer", "Nutrient", "Organic Matter", "Matter Cycle"],
        "desc": "Students model how decomposers recycle dead matter into nutrients. Why doesn't Earth fill up with dead stuff? Explore how soil moisture and organic matter drive decomposer activity.",
        "hook": "Why doesn't Earth fill up with dead stuff?",
        "careers": ["Soil Scientist", "Bioremediation Engineer"],
    },
    "G05-L03-powered-by-sun.mp4": {
        "title": "Powered by the Sun — Energy Transfer",
        "grade": "Grade 5", "lesson": "L03",
        "ngss": "5-PS3-1",
        "topic": "Energy Transfer Through Photosynthesis",
        "vocab": ["Photosynthesis", "Producer", "Consumer", "Energy Transfer"],
        "desc": "Students trace energy from the sun through plants to animals. Model how sunlight intensity and temperature affect photosynthesis rate. All food energy originates from the sun.",
        "hook": "How does sunlight become your lunch?",
        "careers": ["Botanist", "Agricultural Scientist"],
    },
    "G05-L04-earths-hidden-water.mp4": {
        "title": "Earth's Hidden Water — Freshwater Systems",
        "grade": "Grade 5", "lesson": "L04",
        "ngss": "5-ESS2-2",
        "topic": "Freshwater Distribution and the Water Cycle",
        "vocab": ["Precipitation", "Evaporation", "Freshwater", "Reservoir"],
        "desc": "Students model how precipitation and temperature control freshwater availability. Less than 1% of Earth's water is accessible — discover the balance between precipitation and evaporation.",
        "hook": "If Earth is 70% water, why do we run out?",
        "careers": ["Hydrologist", "Water Resource Engineer"],
    },
    "G05-L05-disappearing-act.mp4": {
        "title": "The Disappearing Act — Conservation of Matter",
        "grade": "Grade 5", "lesson": "L05",
        "ngss": "5-PS1-2",
        "topic": "Conservation of Matter During State Changes",
        "vocab": ["Conservation", "State of Matter", "Physical Change", "Mass"],
        "desc": "Students model how mass stays constant when matter changes form. Prove that ice and liquid water share the same mass. Conservation of matter applies to all changes.",
        "hook": "Where does water go when it 'disappears'?",
        "careers": ["Chemical Engineer", "Materials Scientist"],
    },
    "G05-L06-tree-mass.mp4": {
        "title": "Where Does a Tree's Mass Come From?",
        "grade": "Grade 5", "lesson": "L06",
        "ngss": "5-LS1-1",
        "topic": "Plant Growth from CO2 via Photosynthesis",
        "vocab": ["Photosynthesis", "CO2", "Biomass", "Glucose"],
        "desc": "Students model how trees get most of their mass from carbon dioxide in the air — not from soil. Trace how CO2 and sunlight build tree biomass through photosynthesis.",
        "hook": "A tree weighs tons — where does all that mass come from?",
        "careers": ["Forest Ecologist", "Carbon Cycle Researcher"],
    },
    "G05-L07-mushroom-network.mp4": {
        "title": "The Mushroom Network Under Your Feet",
        "grade": "Grade 5", "lesson": "L07",
        "ngss": "5-LS2-1",
        "topic": "Mycorrhizal Networks and Forest Connectivity",
        "vocab": ["Mycorrhizal", "Mutualism", "Hyphae", "Nutrient"],
        "desc": "Students model the Wood Wide Web — underground fungal networks that allow trees to share nutrients and warnings. Discover how drought collapses the network and isolates trees.",
        "hook": "Trees talk to each other underground?",
        "careers": ["Mycologist", "Forest Ecologist"],
    },
    "G05-L08-soap-destroys-viruses.mp4": {
        "title": "How Soap Actually Destroys Viruses",
        "grade": "Grade 5", "lesson": "L08",
        "ngss": "5-PS1-4",
        "topic": "Soap Chemistry and Virus Membrane Disruption",
        "vocab": ["Lipid", "Membrane", "Amphiphilic", "Pathogen"],
        "desc": "Students model how soap destroys viruses at the molecular level by breaking apart lipid membranes. Why 20 seconds of soap and water is so effective against pathogens.",
        "hook": "How does soap actually kill viruses?",
        "careers": ["Virologist", "Public Health Scientist"],
    },
    "G05-L09-whose-air.mp4": {
        "title": "Whose Air Is This? — Air Quality & Justice",
        "grade": "Grade 5", "lesson": "L09",
        "ngss": "5-ESS3-1",
        "topic": "Air Quality, Pollution, and Environmental Justice",
        "vocab": ["Air Quality Index", "Particulate Matter", "Respiratory", "Environmental Justice"],
        "desc": "Students model how vehicle traffic and wind patterns determine air pollution and respiratory health impact. Discover why communities near freeways face disproportionate health burdens.",
        "hook": "Is the air you breathe the same as everyone else's?",
        "careers": ["Environmental Engineer", "Air Quality Scientist"],
    },
    "G05-L10-old-starlight.mp4": {
        "title": "The Light You're Seeing Is Already Old",
        "grade": "Grade 5", "lesson": "L10",
        "ngss": "5-ESS1-1",
        "topic": "Star Brightness, Distance, and Light Travel Time",
        "vocab": ["Light Year", "Luminosity", "Apparent Brightness", "Inverse Square Law"],
        "desc": "Students model how distance and luminosity determine a star's apparent brightness. The sun looks brightest because it's closest. Looking at distant stars means looking into the past.",
        "hook": "When you look at stars, you're literally looking back in time.",
        "careers": ["Astrophysicist", "Optical Engineer"],
    },

    # ═══ Grade 8 Lessons ═══
    "G08-L01-superbugs.mp4": {
        "title": "Superbugs: Evolution You Can See",
        "grade": "Grade 8", "lesson": "L01",
        "ngss": "MS-LS4-4, MS-LS4-6",
        "topic": "Antibiotic Resistance and Natural Selection",
        "vocab": ["Antibiotic Resistance", "Natural Selection", "Mutation", "Selective Pressure"],
        "desc": "Students model how antibiotic use selects for resistant bacteria, creating superbugs that are impossible to kill. Evaluate real-world strategies for slowing antibiotic resistance.",
        "hook": "What if medicine stops working?",
        "careers": ["Epidemiologist", "Microbiologist"],
    },
    "G08-L02-reef-bleaching.mp4": {
        "title": "The Reef Is Bleaching — Ocean Ecosystems",
        "grade": "Grade 8", "lesson": "L02",
        "ngss": "MS-LS2-1, MS-LS2-4",
        "topic": "Coral Bleaching and Ecosystem Collapse",
        "vocab": ["Coral Bleaching", "Symbiosis", "Ecosystem Services", "Trophic Cascade"],
        "desc": "Students model why coral reefs turn white and die. Trace how rising sea temperatures disrupt coral-algae symbiosis, causing cascading ecosystem collapse.",
        "hook": "Half the world's coral reefs are already dead. Why?",
        "careers": ["Marine Biologist", "Coral Restoration Scientist"],
    },
    "G08-L03-phones-dirty-secret.mp4": {
        "title": "Your Phone's Dirty Secret — E-Waste",
        "grade": "Grade 8", "lesson": "L03",
        "ngss": "MS-ESS3-3, MS-ESS3-4",
        "topic": "Electronics Lifecycle and E-Waste",
        "vocab": ["Rare Earth Minerals", "E-Waste", "Resource Extraction", "Lifecycle Analysis"],
        "desc": "Students model the true environmental cost of smartphones — from rare earth mining to e-waste. Discover how consumer demand drives environmental destruction.",
        "hook": "Your phone has a dirty secret.",
        "careers": ["Environmental Engineer", "Materials Scientist"],
    },
    "G08-L04-hurricanes.mp4": {
        "title": "Why Hurricanes Are Getting Angrier",
        "grade": "Grade 8", "lesson": "L04",
        "ngss": "MS-ESS2-5, MS-ESS2-6",
        "topic": "Hurricane Intensification and Ocean Temperature",
        "vocab": ["Sea Surface Temperature", "Rapid Intensification", "Storm Surge", "Convection"],
        "desc": "Students model why hurricanes are getting stronger. Warmer ocean temperatures fuel more powerful storms — just a few degrees can turn a Cat 1 into a Cat 5.",
        "hook": "Hurricanes are getting stronger. The ocean knows why.",
        "careers": ["Meteorologist", "Climate Scientist"],
    },
    "G08-L05-roller-coaster.mp4": {
        "title": "The Roller Coaster Equation — Energy",
        "grade": "Grade 8", "lesson": "L05",
        "ngss": "MS-PS3-1, MS-PS3-2",
        "topic": "Kinetic and Potential Energy Transformation",
        "vocab": ["Kinetic Energy", "Potential Energy", "Energy Conservation", "Energy Transformation"],
        "desc": "Students model how roller coasters convert height into speed without an engine. Discover the energy seesaw between potential and kinetic energy — total energy is always conserved.",
        "hook": "No engine. No fuel. How does a roller coaster work?",
        "careers": ["Mechanical Engineer", "Roller Coaster Designer"],
    },
    "G08-L06-concussion.mp4": {
        "title": "The Concussion Problem — Collision Physics",
        "grade": "Grade 8", "lesson": "L06",
        "ngss": "MS-PS2-1, MS-PS2-2",
        "topic": "Newton's Laws, Collision Forces, and Sports Safety",
        "vocab": ["Newton's Third Law", "Impulse", "Concussion", "Deceleration"],
        "desc": "Students model why football players still get concussions even with helmets. Use Newton's Laws to understand collision physics — doubling speed quadruples collision energy.",
        "hook": "Why can't helmets stop concussions?",
        "careers": ["Biomedical Engineer", "Biomechanist"],
    },
    "G08-L07-lebron-atp.mp4": {
        "title": "How LeBron Turns Food Into Dunks",
        "grade": "Grade 8", "lesson": "L07",
        "ngss": "MS-LS1-5, MS-LS1-7",
        "topic": "Cellular Respiration and Athletic Performance",
        "vocab": ["Cellular Respiration", "ATP", "Glucose", "Metabolism"],
        "desc": "Students model how food converts into athletic performance through cellular respiration. Trace glucose and oxygen to ATP energy production — why athletes need both fuel and oxygen.",
        "hook": "How does a cheeseburger become a slam dunk?",
        "careers": ["Sports Nutritionist", "Exercise Physiologist"],
    },
    "G08-L08-genetics.mp4": {
        "title": "Why Do You Look Like That? — Genetics",
        "grade": "Grade 8", "lesson": "L08",
        "ngss": "MS-LS3-1, MS-LS3-2",
        "topic": "Inheritance, Alleles, and Genetic Variation",
        "vocab": ["Allele", "Dominant", "Recessive", "Genotype vs. Phenotype"],
        "desc": "Students model why they look similar to parents but not identical. Explore how dominant and recessive alleles produce traits — discover the 3:1 ratio and the genetic lottery.",
        "hook": "You have your mom's eyes. But why not everything else?",
        "careers": ["Genetic Counselor", "Forensic Geneticist"],
    },
    "G08-L09-sound-waves.mp4": {
        "title": "Your Music Is a Wave — Sound Science",
        "grade": "Grade 8", "lesson": "L09",
        "ngss": "MS-PS4-1, MS-PS4-2",
        "topic": "Wave Properties: Amplitude, Frequency, Energy",
        "vocab": ["Amplitude", "Frequency", "Wavelength", "Medium"],
        "desc": "Students model how waves carry music from speakers to ears. Amplitude = loudness, frequency = pitch, and doubling amplitude quadruples energy. All waves follow the same rules.",
        "hook": "Your favorite song is literally just vibrating air.",
        "careers": ["Acoustical Engineer", "Audio Engineer"],
    },
    "G08-L10-hand-warmers.mp4": {
        "title": "Hand Warmers and Hidden Reactions",
        "grade": "Grade 8", "lesson": "L10",
        "ngss": "MS-PS1-4, MS-PS1-5",
        "topic": "Exothermic/Endothermic Reactions and Conservation of Mass",
        "vocab": ["Chemical Reaction", "Exothermic", "Endothermic", "Conservation of Mass"],
        "desc": "Students model how hand warmers create heat without fire through exothermic iron oxidation. Atoms rearrange but total mass is conserved — connecting energy release to conservation of matter.",
        "hook": "No battery. No fire. How does a hand warmer get hot?",
        "careers": ["Chemical Engineer", "Materials Scientist"],
    },

    # ═══ Concept Explainers (Grades 4-8) ═══
    "concept-systems-48.mp4": {
        "title": "What Is a System? — Science Explainer",
        "grade": "Grades 4-8", "lesson": "Concept",
        "ngss": "NGSS CCC: Systems and System Models",
        "topic": "Introduction to Systems Thinking in Science",
        "vocab": ["System", "Component", "Interaction", "Emergent Behavior"],
        "desc": "What is a system? Everything around you — from your body to the weather — is made of parts that interact. Learn how scientists use systems thinking to understand the world and make predictions.",
        "hook": "Everything around you is a system. Once you see it, you can't unsee it.",
        "careers": ["Systems Engineer", "Data Scientist"],
    },
    "concept-modeling-48.mp4": {
        "title": "What Is Modeling? — Science Explainer",
        "grade": "Grades 4-8", "lesson": "Concept",
        "ngss": "NGSS Practice 2: Developing and Using Models",
        "topic": "Scientific Modeling and Simulation",
        "vocab": ["Model", "Variable", "Prediction", "Simulation"],
        "desc": "Scientists don't just memorize facts — they build models to test ideas. Learn how modeling helps us predict the future, test solutions, and understand complex systems without breaking anything.",
        "hook": "Scientists don't guess — they model.",
        "careers": ["Computational Scientist", "Architect"],
    },
    "concept-boolean-48.mp4": {
        "title": "What Is Boolean Logic? — Science Explainer",
        "grade": "Grades 4-8", "lesson": "Concept",
        "ngss": "NGSS Practice 5: Using Mathematics and Computational Thinking",
        "topic": "Boolean Logic and Decision-Making in Science",
        "vocab": ["Boolean", "True/False", "AND/OR", "Conditional"],
        "desc": "Every computer, every video game, and every scientific model runs on Boolean logic — true or false, yes or no. Learn how this simple idea powers everything from Google searches to climate models.",
        "hook": "True or false? That simple question runs the entire digital world.",
        "careers": ["Software Engineer", "AI Researcher"],
    },
    "concept-simulation-48.mp4": {
        "title": "What Is a Simulation? — Science Explainer",
        "grade": "Grades 4-8", "lesson": "Concept",
        "ngss": "NGSS Practice 2, Practice 5: Computational Thinking",
        "topic": "Computer Simulations in Science",
        "vocab": ["Simulation", "Variable", "Iteration", "Prediction"],
        "desc": "What if you could test ideas without consequences? Simulations let scientists crash cars, spread diseases, and build cities — all on a computer. Learn how running models forward in time reveals the future.",
        "hook": "What if you could test any idea — without consequences?",
        "careers": ["Simulation Engineer", "City Planner"],
    },

    # ═══ Concept Explainers (Grades K-3) ═══
    "concept-systems-k3.mp4": {
        "title": "What Is a System? — For Young Scientists",
        "grade": "Grades K-3", "lesson": "Concept",
        "ngss": "NGSS CCC: Systems and System Models",
        "topic": "Introduction to Systems for Young Learners",
        "vocab": ["System", "Parts", "Connected", "Together"],
        "desc": "A system is a group of parts that work together! Your body, your classroom, even a fish tank — they're all systems. Learn to spot systems everywhere and think like a scientist.",
        "hook": "A fish tank. A family. A rainstorm. What do they all have in common?",
        "careers": ["Scientist", "Engineer"],
    },
    "concept-modeling-k3.mp4": {
        "title": "What Is Modeling? — For Young Scientists",
        "grade": "Grades K-3", "lesson": "Concept",
        "ngss": "NGSS Practice 2: Developing and Using Models",
        "topic": "Introduction to Models for Young Learners",
        "vocab": ["Model", "Represent", "Test", "Predict"],
        "desc": "A model is like a mini version of the real thing! Scientists build models to test their ideas and predict what will happen. You can be a model-builder too!",
        "hook": "Scientists build mini worlds to test big ideas.",
        "careers": ["Scientist", "Designer"],
    },
    "concept-boolean-k3.mp4": {
        "title": "What Is Boolean Logic? — For Young Scientists",
        "grade": "Grades K-3", "lesson": "Concept",
        "ngss": "NGSS Practice 5: Using Mathematics and Computational Thinking",
        "topic": "True/False Thinking for Young Learners",
        "vocab": ["True", "False", "Rule", "Decision"],
        "desc": "Is it raining? Yes or no! Boolean logic is how computers think — using true and false to make decisions. Learn how yes/no questions power everything from traffic lights to video games.",
        "hook": "Yes or no. True or false. That's how computers think!",
        "careers": ["Computer Scientist", "Game Designer"],
    },
    "concept-simulation-k3.mp4": {
        "title": "What Is a Simulation? — For Young Scientists",
        "grade": "Grades K-3", "lesson": "Concept",
        "ngss": "NGSS Practice 2, Practice 5",
        "topic": "Introduction to Simulations for Young Learners",
        "vocab": ["Simulation", "Try", "Predict", "Discover"],
        "desc": "What if you could try something over and over without breaking anything? A simulation lets you test ideas on a computer — grow a garden, build a bridge, or predict the weather!",
        "hook": "What if you could test anything — without breaking it?",
        "careers": ["Scientist", "Engineer"],
    },
}


def get_release_url(filename):
    """Get the GitHub release download URL for a video file."""
    return f"https://github.com/{GITHUB_REPO}/releases/download/{RELEASE_TAG}/{filename}"


def build_youtube_description(v):
    """Build SEO-optimized YouTube description."""
    vocab_tags = " | ".join(v["vocab"])
    careers_text = ", ".join(v.get("careers", []))

    return f"""{v['hook']}

{v['desc']}

This is a FREE lesson video from the "Everything is a System!" curriculum — a phenomenon-driven, NGSS-aligned science series powered by ModelIt, an interactive systems modeling platform for K-12 students.

LESSON DETAILS
{v['grade']} | {v['topic']}
NGSS Standard: {v['ngss']}
Key Vocabulary: {vocab_tags}
STEM Careers: {careers_text}

CALIFORNIA CAST-ALIGNED
This lesson is part of the California CAST (Computer Assisted Science Teaching) aligned curriculum. Full lesson materials — including student presentations, activity packs, and teacher guides — available mid-March 2026.

BUILD YOUR OWN MODEL
Try ModelIt FREE: {MODELIT_URL}
Students build, simulate, and analyze scientific models using real cause-and-effect relationships. Drag-and-drop interface, real-time simulation, and NGSS-aligned curriculum.

CONNECT WITH US
Website: {MODELIT_URL}
Instagram: @dr.martinedtech
TikTok: @modeliteducation
X/Twitter: @ModelitEduc

#NGSS #ScienceEducation #ModelIt #SystemsThinking #STEMEducation #{v['grade'].replace(' ', '')} #PhenomenonDriven #NextGenerationScienceStandards #CASCTAligned #InteractiveScience #K12Science #ScienceSimulation"""


def build_social_caption(v, platform):
    """Build platform-appropriate social media caption."""
    base = f"""{v['hook']}

NEW lesson video: "{v['title']}"
{v['grade']} | {v['ngss']}

Students build interactive models to discover real science. No memorizing — just investigating.

California CAST-aligned lessons available mid-March 2026.
Try ModelIt FREE: {MODELIT_URL}

#NGSS #ScienceEducation #ModelIt #SystemsThinking #STEM #{v['grade'].replace(' ', '')}"""

    if platform == "twitter":
        # 280 char limit — shortened version
        return f"""{v['hook']}

NEW: "{v['title']}" — {v['grade']} | {v['ngss']}

Students build models to discover real science. CAST-aligned lessons coming mid-March 2026.

Try ModelIt FREE: {MODELIT_URL}

#NGSS #ModelIt #STEM #ScienceEd"""

    return base


def create_github_release(dry_run=False):
    """Create GitHub release and upload video files."""
    print("\n=== Creating GitHub Release ===")

    # Check if release exists
    result = subprocess.run(
        ["gh", "release", "view", RELEASE_TAG, "--repo", GITHUB_REPO],
        capture_output=True, text=True
    )

    if result.returncode == 0:
        print(f"  Release {RELEASE_TAG} already exists")
        return True

    if dry_run:
        print(f"  [DRY-RUN] Would create release: {RELEASE_TAG}")
        return True

    # Create release
    print(f"  Creating release: {RELEASE_TAG}")
    result = subprocess.run([
        "gh", "release", "create", RELEASE_TAG,
        "--repo", GITHUB_REPO,
        "--title", "CAST Science Educational Videos v1.0",
        "--notes", "Complete set of \"Everything is a System!\" educational videos.\n\n"
                   "- 10 Grade 5 lesson videos\n"
                   "- 10 Grade 8 lesson videos\n"
                   "- 8 Concept Explainer videos (K-3 and 4-8)\n\n"
                   "NGSS-aligned, California CAST-aligned, powered by ModelIt.\n"
                   f"Learn more: {MODELIT_URL}"
    ], capture_output=True, text=True)

    if result.returncode != 0:
        print(f"  [ERROR] Failed to create release: {result.stderr}")
        return False

    print(f"  Release created!")
    return True


def upload_release_assets(dry_run=False):
    """Upload video files to GitHub release."""
    print("\n=== Uploading Videos to GitHub Release ===")

    for i, filename in enumerate(VIDEOS.keys()):
        filepath = VIDEOS_DIR / filename
        if not filepath.exists():
            print(f"  [{i+1}/{len(VIDEOS)}] [SKIP] {filename} — not found")
            continue

        size_mb = filepath.stat().st_size / (1024 * 1024)

        if dry_run:
            print(f"  [{i+1}/{len(VIDEOS)}] [DRY-RUN] Would upload: {filename} ({size_mb:.0f} MB)")
            continue

        # Check if already uploaded
        result = subprocess.run(
            ["gh", "release", "view", RELEASE_TAG, "--repo", GITHUB_REPO, "--json", "assets",
             "-q", f'.assets[] | select(.name == "{filename}") | .name'],
            capture_output=True, text=True
        )
        if filename in result.stdout:
            print(f"  [{i+1}/{len(VIDEOS)}] [EXISTS] {filename}")
            continue

        print(f"  [{i+1}/{len(VIDEOS)}] Uploading: {filename} ({size_mb:.0f} MB)...")
        result = subprocess.run([
            "gh", "release", "upload", RELEASE_TAG,
            str(filepath),
            "--repo", GITHUB_REPO,
            "--clobber"
        ], capture_output=True, text=True, timeout=600)

        if result.returncode == 0:
            print(f"    [OK]")
        else:
            print(f"    [ERROR] {result.stderr[:200]}")

        time.sleep(0.5)


def post_to_youtube(dry_run=False):
    """Upload all videos to YouTube via Blotato."""
    print("\n=== Posting Videos to YouTube ===")
    print(f"  Channel: ModelIt! in Action (account {ACCOUNTS['youtube']})")

    success = 0
    failed = 0

    for i, (filename, v) in enumerate(VIDEOS.items()):
        video_url = get_release_url(filename)
        yt_title = f"{v['title']} | {v['grade']} Science | {v['ngss']}"
        yt_desc = build_youtube_description(v)

        # YouTube title max 100 chars
        if len(yt_title) > 100:
            yt_title = f"{v['title']} | {v['grade']} | {v['ngss']}"
        if len(yt_title) > 100:
            yt_title = v['title'][:100]

        if dry_run:
            print(f"\n  [{i+1}/{len(VIDEOS)}] [DRY-RUN] {yt_title}")
            print(f"    URL: {video_url}")
            print(f"    Desc: {yt_desc[:120]}...")
            continue

        print(f"\n  [{i+1}/{len(VIDEOS)}] Posting: {yt_title}")

        payload = {
            "post": {
                "accountId": ACCOUNTS["youtube"],
                "content": {
                    "text": yt_desc,
                    "mediaUrls": [video_url],
                    "platform": "youtube"
                },
                "target": {
                    "targetType": "youtube",
                    "title": yt_title,
                    "privacyStatus": "public",
                    "shouldNotifySubscribers": True
                }
            }
        }

        try:
            resp = requests.post(f"{BLOTATO_BASE}/posts", headers=HEADERS, json=payload, timeout=60)
            if resp.status_code in (200, 201):
                data = resp.json()
                submission_id = data.get("postSubmissionId", "unknown")
                print(f"    [SUBMITTED] ID: {submission_id}")
                success += 1
            else:
                print(f"    [ERROR] {resp.status_code}: {resp.text[:200]}")
                failed += 1
        except Exception as e:
            print(f"    [ERROR] {e}")
            failed += 1

        # Rate limit: 30/min — be safe with 2s between posts
        time.sleep(2)

    print(f"\n  YouTube Results: {success} submitted, {failed} failed")
    return success, failed


def post_social_promo(dry_run=False):
    """Post promotional content to Facebook, Instagram, LinkedIn, X, TikTok."""
    print("\n=== Posting Social Media Promotions ===")

    # Group videos by grade for summary posts
    grades = {}
    for filename, v in VIDEOS.items():
        grade = v["grade"]
        grades.setdefault(grade, []).append((filename, v))

    platforms = [
        ("facebook",  ACCOUNTS["facebook"],  {"targetType": "facebook", "pageId": FB_PAGE_ID}),
        ("linkedin",  ACCOUNTS["linkedin"],  {"targetType": "linkedin"}),
        ("instagram", ACCOUNTS["instagram"], {"targetType": "instagram"}),
        ("twitter",   ACCOUNTS["twitter"],   {"targetType": "twitter"}),
        ("tiktok",    ACCOUNTS["tiktok"],    {"targetType": "tiktok", "privacyLevel": "PUBLIC_TO_EVERYONE",
                                               "disabledComments": False, "disabledDuet": False,
                                               "disabledStitch": False, "isBrandedContent": False,
                                               "isYourBrand": False, "isAiGenerated": True}),
    ]

    # Post a series announcement per grade
    for grade_name, lessons in grades.items():
        lesson_list = "\n".join([f"  {v['title']}" for _, v in lessons])
        ngss_list = ", ".join(sorted(set(v["ngss"] for _, v in lessons)))

        announcement = f"""NEW VIDEO SERIES: "Everything is a System!" — {grade_name}

{len(lessons)} NGSS-aligned lesson videos just dropped on the ModelIt! in Action YouTube channel.

{lesson_list}

Standards: {ngss_list}
California CAST-aligned curriculum available mid-March 2026.

Students don't memorize science — they MODEL it. Build, simulate, and discover with ModelIt.

Try it FREE: {MODELIT_URL}

#NGSS #ScienceEducation #ModelIt #SystemsThinking #STEM #{grade_name.replace(' ', '').replace('-', '')} #PhenomenonDriven #CASCTAligned"""

        for platform, account_id, target in platforms:
            caption = announcement
            if platform == "twitter":
                # Shorten for 280 char limit
                caption = f"""NEW: "Everything is a System!" — {grade_name}

{len(lessons)} NGSS-aligned lesson videos are LIVE on YouTube!

Students build models to discover real science. CAST-aligned curriculum coming mid-March 2026.

{MODELIT_URL}

#NGSS #ModelIt #STEM #ScienceEd"""

            if platform == "instagram":
                # Instagram needs media — use first video as cover
                first_video_url = get_release_url(lessons[0][0])
                media_urls = [first_video_url]
            else:
                media_urls = []

            if dry_run:
                print(f"  [DRY-RUN] {platform} — {grade_name} announcement ({len(caption)} chars)")
                continue

            print(f"  Posting to {platform}: {grade_name} announcement...")

            payload = {
                "post": {
                    "accountId": account_id,
                    "content": {
                        "text": caption,
                        "mediaUrls": media_urls,
                        "platform": platform
                    },
                    "target": target
                }
            }

            try:
                resp = requests.post(f"{BLOTATO_BASE}/posts", headers=HEADERS, json=payload, timeout=60)
                if resp.status_code in (200, 201):
                    print(f"    [OK] {resp.json().get('postSubmissionId', '')}")
                else:
                    print(f"    [ERROR] {resp.status_code}: {resp.text[:200]}")
            except Exception as e:
                print(f"    [ERROR] {e}")

            time.sleep(2)


def main():
    parser = argparse.ArgumentParser(description="Post CAST Science videos via Blotato API")
    parser.add_argument('--youtube', action='store_true', help='Upload videos to YouTube')
    parser.add_argument('--promote', action='store_true', help='Post promos to social media')
    parser.add_argument('--all', action='store_true', help='YouTube + social media')
    parser.add_argument('--release-only', action='store_true', help='Just create GitHub release')
    parser.add_argument('--dry-run', action='store_true', help='Preview without posting')
    args = parser.parse_args()

    if not any([args.youtube, args.promote, args.all, args.release_only]):
        parser.print_help()
        sys.exit(1)

    if not BLOTATO_API_KEY:
        print("[ERROR] BLOTATO_API_KEY not set in ~/.env")
        sys.exit(1)

    do_youtube = args.youtube or args.all
    do_promote = args.promote or args.all

    # Step 1: Create GitHub release (needed for public video URLs)
    if not create_github_release(dry_run=args.dry_run):
        print("[ERROR] Failed to create release")
        sys.exit(1)

    # Step 2: Upload videos to release
    upload_release_assets(dry_run=args.dry_run)

    if args.release_only:
        print("\n=== Release created. Done. ===")
        return

    # Step 3: Post to YouTube
    if do_youtube:
        post_to_youtube(dry_run=args.dry_run)

    # Step 4: Social media promotion
    if do_promote:
        post_social_promo(dry_run=args.dry_run)

    print(f"\n{'='*50}")
    print("COMPLETE")
    print(f"{'='*50}")


if __name__ == '__main__':
    main()
