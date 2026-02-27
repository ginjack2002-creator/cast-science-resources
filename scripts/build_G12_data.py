#!/usr/bin/env python3
"""
Grade 12 Lesson Data Generator
Generates lesson_data_G12_L1.py, lesson_data_G12_L2.py, lesson_data_G12_L3.py
Run: python build_G12_data.py
"""
import os, textwrap

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
AGE = "17-18 years old"

def img(lid, scene_cover, scene_land, scene_model, scene_disc, scene_stem):
    """Generate image dict with diversity-centered prompts"""
    return {
        "cover": (f"{lid}-cover.png", scene_cover),
        "landscape": (f"{lid}-landscape.png", scene_land),
        "modeling": (f"{lid}-modeling.png", scene_model),
        "discussion": (f"{lid}-discussion.png", scene_disc),
        "stem": (f"{lid}-stem.png", scene_stem),
    }

def slides(title, sub, comps, think, scenarios, discoveries, answer, stem_title, stem_mission, stem_scenario, stem_qs, career):
    """Generate 9-slide facilitation guide"""
    return [
        {"num":"Slide 1","title":"Cover","visual":f"Title slide with compelling image related to {title}",
         "say":f"Today we're investigating something that affects every single one of you. {sub}.",
         "do":f"Show cover image. Ask: What do you already know about this topic? Quick share-out.","time":"2 min"},
        {"num":"Slide 2","title":"Learning Objectives","visual":"Learning goals and vocabulary terms",
         "say":"Here's what you'll be able to do by the end of today's lesson.",
         "do":"Have students read objectives aloud. Pre-teach vocabulary with quick visual aids.","time":"3 min"},
        {"num":"Slide 3","title":"Big Question","visual":f"Provocative question related to {title}",
         "say":"This is our driving question. By the end of class, you'll be able to answer it with evidence from your model.",
         "do":"Quick-write: Students write their initial hypothesis. Save to compare later.","time":"3 min"},
        {"num":"Slide 4","title":"LEVER Framework","visual":"LEVER steps overview",
         "say":"We're going to build a computational model to investigate this system. Here are our five steps.",
         "do":"Preview each LEVER step. Emphasize that modeling reveals hidden patterns.","time":"2 min"},
        {"num":"Slide 5","title":"Activity 1: Components","visual":"Component cards for sorting",
         "say":f"What are the key parts of this system? Which ones come from outside, and which respond inside?",
         "do":"Guide sorting of external vs. internal components. Use think-pair-share for reasoning.","time":"8 min"},
        {"num":"Slide 6","title":"Activity 2: Connections","visual":"Relationship arrows between components",
         "say":f"{think}",
         "do":"Students draw arrows showing +/- relationships. Discuss feedback loops if present.","time":"8 min"},
        {"num":"Slide 7","title":"Activity 3: Simulation","visual":"Simulation results graphs",
         "say":"Now let's test our model. Run each scenario and record what happens.",
         "do":"Students run all scenarios, record predictions vs. observations. Discuss surprises.","time":"10 min"},
        {"num":"Slide 8","title":"Discoveries","visual":"Key findings summary",
         "say":f"So what did our model reveal? {answer[:100]}...",
         "do":"Class discussion of discoveries. Compare initial hypotheses to model evidence.","time":"5 min"},
        {"num":"Slide 9","title":"STEM Challenge","visual":f"Engineering challenge: {stem_title}",
         "say":f"Now apply what you've learned. {stem_mission[:100]}...",
         "do":"Groups design solutions using model data. Present and evaluate designs.","time":"12 min"},
    ]

def write_lesson_file(filepath, docstring, lessons):
    """Write a complete lesson data Python file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f'#!/usr/bin/env python3\n"""{docstring}"""\n\n')
        for i, lesson in enumerate(lessons, 1):
            f.write(f"L{i:02d} = ")
            write_dict(f, lesson, indent=0)
            f.write("\n\n")
        names = ", ".join(f"L{i:02d}" for i in range(1, len(lessons)+1))
        f.write(f"ALL_LESSONS = [{names}]\n")
    print(f"[OK] Written: {filepath} ({len(lessons)} lessons)")

def write_dict(f, d, indent=0):
    """Write a Python dict with proper formatting"""
    pad = "    " * indent
    f.write("{\n")
    items = list(d.items())
    for idx, (k, v) in enumerate(items):
        f.write(f'{pad}    "{k}": ')
        write_value(f, v, indent + 1)
        if idx < len(items) - 1:
            f.write(",")
        f.write("\n")
    f.write(f"{pad}}}")

def write_value(f, v, indent):
    """Write a Python value with proper formatting"""
    pad = "    " * indent
    if isinstance(v, str):
        # Escape quotes and backslashes
        escaped = v.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
        f.write(f'"{escaped}"')
    elif isinstance(v, bool):
        f.write("True" if v else "False")
    elif isinstance(v, (int, float)):
        f.write(str(v))
    elif isinstance(v, tuple):
        f.write("(")
        for i, item in enumerate(v):
            write_value(f, item, indent)
            if i < len(v) - 1:
                f.write(", ")
        f.write(")")
    elif isinstance(v, list):
        if not v:
            f.write("[]")
        elif all(isinstance(x, str) for x in v) and len(v) <= 5 and all(len(x) < 80 for x in v):
            f.write("[\n")
            for i, item in enumerate(v):
                f.write(f'{pad}    ')
                write_value(f, item, indent + 1)
                if i < len(v) - 1:
                    f.write(",")
                f.write("\n")
            f.write(f"{pad}]")
        else:
            f.write("[\n")
            for i, item in enumerate(v):
                f.write(f'{pad}    ')
                write_value(f, item, indent + 1)
                if i < len(v) - 1:
                    f.write(",")
                f.write("\n")
            f.write(f"{pad}]")
    elif isinstance(v, dict):
        write_dict(f, v, indent)
    else:
        f.write(repr(v))


# ============================================================
# LEVEL 1: Science, Society & You (4-5 components each)
# ============================================================

def build_L1():
    lessons = []

    # L01: Why Does Your Brain Lie to You?
    lessons.append({
        "id": "G12L1-L01",
        "title": "Why Does Your Brain Lie to You?",
        "subtitle": "Modeling Cognitive Bias, Perception, and Decision-Making in the Brain",
        "ngss": "HS-LS1-2",
        "ngss_desc": "Develop and use a model to illustrate the hierarchical organization of interacting systems that provide specific functions within multicellular organisms.",
        "big_question": "If your brain is the most powerful computer on Earth, why does it constantly trick you into seeing things that aren't there and believing things that aren't true?",
        "objectives": [
            "Model how sensory input, prior experience, and cognitive shortcuts interact to produce perceptual errors",
            "Explain why cognitive biases are features of neural processing, not flaws in intelligence",
            "Predict when confirmation bias will cause someone to misinterpret new evidence",
            "Analyze how understanding your own biases can improve decision-making in science and daily life"
        ],
        "vocabulary": [
            ("Cognitive Bias", "A systematic pattern of deviation from rationality in judgment — the brain's shortcut that works most of the time but produces predictable errors in specific situations"),
            ("Confirmation Bias", "The tendency to search for, interpret, and remember information that confirms pre-existing beliefs while ignoring contradictory evidence — one of the most powerful biases in science and politics"),
            ("Heuristic", "A mental shortcut the brain uses to make quick decisions without analyzing all available data — efficient but prone to systematic errors in complex or unfamiliar situations"),
            ("Neuroplasticity", "The brain's ability to reorganize neural pathways based on experience — the mechanism that creates both expertise and deeply ingrained biases over time")
        ],
        "components": [
            ("Sensory Input", "Raw data from eyes, ears, and other senses entering the brain — the starting information that gets filtered and interpreted before you become conscious of it", True),
            ("Prior Experience", "Accumulated memories and learned patterns stored in neural networks — the brain's reference library that shapes how new information is interpreted", True),
            ("Cognitive Load", "The amount of mental processing required by the current task — when cognitive load is high, the brain relies more heavily on shortcuts and biases", False),
            ("Bias Strength", "How strongly a cognitive bias influences the final perception or decision — increases when the brain is stressed, tired, or processing ambiguous information", False),
            ("Decision Accuracy", "How closely the brain's output matches objective reality — decreases as bias strength increases and as sensory input becomes more ambiguous", False)
        ],
        "think_about_it": "When Prior Experience is very strong and Sensory Input is weak or ambiguous, what happens to Bias Strength? Why might an expert sometimes be MORE biased than a beginner?",
        "scenarios": [
            ("Clear Evidence Scenario", "Set Sensory Input to high clarity with low Prior Experience — observe how Decision Accuracy responds when the brain has strong data and few preconceptions"),
            ("Confirmation Bias Scenario", "Set Prior Experience to maximum with moderate Sensory Input — observe how strong prior beliefs increase Bias Strength even with decent evidence"),
            ("Cognitive Overload Scenario", "Increase Cognitive Load to maximum — observe how stress and multitasking amplify Bias Strength and reduce Decision Accuracy across the board")
        ],
        "sim_scenarios": [
            ("Clear Evidence", "Sensory Input: High | Prior Experience: Low | Cognitive Load: Low", "When the brain receives clear data with few preconceptions and low stress, what do you predict happens to Decision Accuracy?"),
            ("Strong Priors", "Sensory Input: Medium | Prior Experience: Maximum | Cognitive Load: Low", "What happens when someone has very strong prior beliefs and receives ambiguous new information?"),
            ("Overloaded Brain", "Sensory Input: Low | Prior Experience: High | Cognitive Load: Maximum", "When someone is stressed, tired, and processing weak information with strong biases, what happens?")
        ],
        "discoveries": [
            "Cognitive biases are strongest when sensory input is ambiguous and prior experience is strong — the brain fills in gaps with what it expects to see",
            "High cognitive load amplifies ALL biases because the brain shifts from careful analysis to quick shortcuts when overwhelmed",
            "Decision accuracy drops most dramatically when strong prior experience meets ambiguous evidence — expertise can actually increase bias in uncertain situations",
            "Awareness of bias doesn't eliminate it but can reduce its impact — the model shows that metacognition acts as a moderating variable on bias strength"
        ],
        "answer": "Your brain lies to you because it's optimized for speed, not accuracy. Evolution designed neural processing to make fast-enough decisions using shortcuts called heuristics. These shortcuts work brilliantly 95% of the time but produce systematic errors — cognitive biases — in specific situations: when evidence is ambiguous, when you're stressed or tired, or when you have strong prior beliefs. Confirmation bias, the most dangerous for scientific thinking, causes your brain to literally filter incoming sensory data to match what you already believe. Your brain isn't broken — it's doing exactly what evolution designed it to do. Understanding this is the first step to thinking more clearly.",
        "stem_title": "Design a Bias-Aware Decision Tool",
        "stem_mission": "Design a decision-making tool or protocol that helps people recognize and counteract cognitive biases when making important choices about health, finances, or education.",
        "stem_scenario": "A hospital has noticed that doctors' diagnostic accuracy drops significantly during long shifts. Research shows cognitive biases like anchoring (fixating on the first diagnosis) and confirmation bias (only looking for evidence that supports the initial guess) are major contributors. Your team must design a decision-support tool that helps doctors maintain diagnostic accuracy even when cognitive load is high.",
        "stem_questions": [
            "Which cognitive biases are most dangerous in medical decision-making and when do they activate?",
            "How can a tool force the brain to consider alternative explanations instead of anchoring on the first one?",
            "What does your model suggest about the relationship between cognitive load and bias strength?"
        ],
        "stem_design_qs": [
            "What specific bias-interruption mechanisms does your tool include and how does each one work?",
            "How does your design account for the fact that doctors under high cognitive load resist complex protocols?",
            "What evidence from your model supports your design choices?",
            "How would you test whether your tool actually reduces diagnostic errors?"
        ],
        "career": "Cognitive scientists and behavioral researchers study how the brain processes information and makes decisions. They work in healthcare, tech companies, government policy, and academia, earning $65,000-$130,000/year. UX researchers who apply cognitive science to product design earn $80,000-$150,000/year.",
        "images": img("G12L1-L01",
            "A photorealistic close-up of a diverse 17-18 year old student looking at an optical illusion display in a modern science classroom, with visual distortion effects suggesting perception vs reality, dramatic lighting",
            "A diverse group of 17-18 year old students in a modern psychology classroom examining optical illusions and brain models on their desks, engaged discussion, natural lighting through large windows",
            "A diverse group of 17-18 year old students working on laptops building computational models of cognitive bias, modern classroom with brain diagrams and decision flowcharts on the walls",
            "A teacher leading a discussion with diverse 17-18 year old students about cognitive bias, a brain scan image and bias flowchart displayed on a smartboard, students actively debating",
            "Diverse 17-18 year old students designing bias-aware decision tools on whiteboards with flowcharts, decision trees, and human factors diagrams"
        ),
        "pre_assessment": [
            "Have you ever been completely sure you saw or heard something that turned out to be different from what actually happened? Describe what occurred.",
            "Why do you think two people can look at the same evidence and reach completely opposite conclusions?",
            "What do you think a 'cognitive bias' is, and can you name any examples?",
            "Do you think smarter people are less biased? Explain your reasoning."
        ],
        "extend_components": [
            ("Emotional State", "The current emotional condition of the decision-maker — fear, anger, and excitement each amplify different biases and override rational processing in predictable ways"),
            ("Social Pressure", "Influence from peers, authority figures, or group consensus — conformity bias can override personal judgment even when the individual knows the group is wrong"),
            ("Metacognition", "Awareness of one's own thinking processes — acts as a moderating variable that can reduce but never eliminate the impact of cognitive biases on decisions")
        ],
        "reflections": [
            "How does your model explain why two scientists can look at the same data and reach different conclusions?",
            "Why does increasing cognitive load make biases stronger, and what does this imply for important decisions made under stress?",
            "If cognitive biases are built into how the brain works, can we ever truly eliminate them? What does your model suggest?",
            "How might understanding cognitive bias change the way you evaluate news, social media, or advertising?",
            "What are the limitations of a five-component model for something as complex as human decision-making?"
        ],
        "dimensions": [
            ("Science Practice", "Developing and Using Models", "Students develop computational models to predict how cognitive biases affect decision accuracy based on sensory input clarity, prior experience strength, and cognitive load."),
            ("Disciplinary Core Idea", "LS1.A Structure and Function", "The nervous system processes sensory information through hierarchical neural networks that use shortcuts (heuristics) to manage the enormous volume of incoming data, producing systematic biases."),
            ("Crosscutting Concept", "Cause and Effect", "Students identify causal mechanisms linking sensory ambiguity, prior experience, and cognitive load to predictable increases in bias strength and decreases in decision accuracy.")
        ],
        "cast_items": [
            "Model how neural information processing produces systematic cognitive biases under specific conditions",
            "Predict decision accuracy based on the interaction of sensory input quality, prior experience, and cognitive load",
            "Explain why cognitive biases are adaptive features of brain organization rather than random errors"
        ],
        "cast_questions": [
            ("Multiple Choice:", "A student with strong prior beliefs about climate change reads an ambiguous news article about temperature data. Based on the cognitive bias model, what is the most likely outcome and why?"),
            ("Constructed Response:", "Using your model, explain why a tired doctor at the end of a 16-hour shift is more likely to misdiagnose a patient than the same doctor at the start of the shift. Reference at least three components from your model.")
        ],
        "background_intro": "Every second, your brain processes approximately 11 million bits of sensory information, but your conscious mind can only handle about 50 bits per second. To bridge this enormous gap, the brain uses mental shortcuts called heuristics — fast, efficient rules of thumb that produce good-enough answers most of the time. But these same shortcuts create systematic errors called cognitive biases that affect every human being, regardless of intelligence or education.",
        "background_sections": [
            ("The Neuroscience of Heuristics", "Daniel Kahneman's Nobel Prize-winning research identified two systems of thinking: System 1 (fast, automatic, intuitive) and System 2 (slow, deliberate, analytical). System 1 handles 95% of daily decisions using heuristics, while System 2 activates for complex problems. Cognitive biases arise when System 1 processes situations that actually require System 2 analysis — the brain takes a shortcut when it should slow down."),
            ("Confirmation Bias in Science", "Confirmation bias is particularly dangerous in scientific thinking because it causes researchers to unconsciously design experiments that confirm their hypotheses, selectively notice supporting evidence, and discount contradictory results. Studies show that even peer review is affected — reviewers rate papers more favorably when conclusions align with their existing beliefs. This is why double-blind studies and pre-registered hypotheses are critical safeguards."),
            ("The Adaptive Value of Bias", "Cognitive biases aren't bugs — they're features. In evolutionary terms, the cost of a false positive (seeing a predator that isn't there) is much lower than a false negative (missing a real predator). The brain evolved to be paranoid, pattern-seeking, and quick rather than accurate. In modern environments, these same adaptations cause us to see patterns in random data, jump to conclusions, and resist changing our minds even when evidence demands it."),
            ("Cognitive Load and Decision Quality", "Research consistently shows that decision quality degrades under high cognitive load. When working memory is taxed — by stress, fatigue, multitasking, or information overload — the brain shifts almost entirely to System 1 processing. This means more reliance on heuristics, stronger biases, and worse decisions. This has critical implications for high-stakes environments like hospitals, courtrooms, and air traffic control.")
        ],
        "lever_L": "Students identify sensory input, prior experience, cognitive load, bias strength, and decision accuracy as the key components of the cognitive bias system.",
        "lever_E": "Students determine that sensory ambiguity and strong prior experience increase bias strength, that cognitive load amplifies all biases, and that bias strength inversely affects decision accuracy.",
        "lever_V": "Students build a computational model showing how the interaction of input clarity, experience, and cognitive load determines the strength of cognitive biases and the accuracy of decisions.",
        "lever_Ev": "Students run clear evidence, confirmation bias, and cognitive overload scenarios to test predictions about when and why the brain produces systematic errors.",
        "lever_R": "Students add emotional state, social pressure, or metacognition to explore how real-world factors modify the basic bias model and test bias-reduction strategies.",
        "slides_guide": slides("Why Does Your Brain Lie to You?", "Modeling Cognitive Bias",
            [c[0] for c in [("Sensory Input",), ("Prior Experience",), ("Cognitive Load",), ("Bias Strength",), ("Decision Accuracy",)]],
            "When Prior Experience is very strong and Sensory Input is weak, what happens to Bias Strength?",
            [("Clear Evidence",), ("Confirmation Bias",), ("Cognitive Overload",)],
            ["Biases are strongest with ambiguous input + strong priors", "Cognitive load amplifies ALL biases"],
            "Your brain lies because it's optimized for speed, not accuracy.",
            "Design a Bias-Aware Decision Tool",
            "Design a decision-support tool that helps doctors maintain diagnostic accuracy.",
            "A hospital has noticed diagnostic accuracy drops during long shifts.",
            ["Which biases are most dangerous?", "How can a tool force alternative thinking?"],
            "Cognitive scientists study how the brain processes information, earning $65,000-$130,000/year."),
        "sort_reasoning": "Sensory Input and Prior Experience are external components because they represent inputs that exist before the cognitive process begins — one comes from the environment and the other from stored memory. Cognitive Load, Bias Strength, and Decision Accuracy are internal because they are emergent properties of the brain's processing that result from how external inputs interact within the neural system.",
        "relationships": [
            ("Sensory Input to Bias Strength", "NEGATIVE (-)", "When sensory input is clear and unambiguous, the brain has less need for shortcuts, so bias strength decreases. When input is weak or ambiguous, the brain fills gaps with assumptions, increasing bias."),
            ("Prior Experience to Bias Strength", "POSITIVE (+)", "Stronger prior experience creates stronger expectations, which increase bias strength. The brain interprets new information through the lens of what it already believes."),
            ("Cognitive Load to Bias Strength", "POSITIVE (+)", "Higher cognitive load forces the brain to rely more on quick heuristics rather than careful analysis, amplifying all cognitive biases."),
            ("Bias Strength to Decision Accuracy", "NEGATIVE (-)", "As bias strength increases, the gap between perception and reality widens, directly reducing decision accuracy.")
        ],
        "sim_answers": [
            ("Clear Evidence Scenario", "With high Sensory Input, low Prior Experience, and low Cognitive Load, the model shows minimal Bias Strength and high Decision Accuracy. The brain has strong data, few preconceptions to distort it, and plenty of processing capacity — ideal conditions for accurate perception and judgment."),
            ("Cognitive Overload Scenario", "With maximum Cognitive Load, even moderate Sensory Input and Prior Experience produce dramatically increased Bias Strength and decreased Decision Accuracy. The overloaded brain shifts entirely to heuristic processing, amplifying every bias. This explains why critical errors increase during high-stress, high-workload situations.")
        ],
        "reflection_exemplars": [
            ("Can smart people be more biased than average?", "Yes, and our model explains why. Intelligence increases Prior Experience and the sophistication of pattern-matching, but it doesn't reduce the fundamental heuristic processing that produces bias. In fact, research shows that more intelligent people are better at constructing convincing rationalizations for their biased conclusions — they use their cognitive abilities to defend their biases rather than question them. The model shows that Prior Experience strength is a stronger driver of bias than any other variable."),
            ("How does this apply to scientific thinking?", "Science is specifically designed to counteract cognitive biases. Double-blind experiments prevent confirmation bias, peer review provides external checks, and replication requirements catch false positives. Our model shows that the most dangerous condition for bias is strong prior experience + ambiguous data + high cognitive load — exactly the situation a researcher faces when they've spent years on a hypothesis and encounter unclear results. The scientific method doesn't eliminate bias; it creates institutional safeguards against it.")
        ],
        "stem_intro": "Present the challenge: A hospital needs your team to design a decision-support tool that helps doctors recognize and counteract cognitive biases during long shifts. Use your model data to identify the most dangerous bias conditions and design interventions that reduce diagnostic errors.",
        "stem_concepts": [
            ("Anchoring Bias in Medicine", "Doctors tend to fixate on the first diagnosis they consider, then unconsciously seek confirming evidence. Studies show that initial diagnostic impressions are correct only 70-80% of the time, but doctors often fail to generate alternative diagnoses once anchored."),
            ("Debiasing Techniques", "Research-backed strategies for reducing bias include: forcing consideration of alternatives (What else could this be?), using structured checklists, taking cognitive breaks, and seeking outside perspectives. No technique eliminates bias completely, but combinations can significantly reduce errors."),
            ("Human Factors Engineering", "The design of tools and environments to work with human cognitive limitations rather than against them. In healthcare, this includes standardized handoff protocols, decision-support algorithms, and fatigue management systems.")
        ],
        "stem_eval": [
            ("Expert (4)", "Design identifies specific biases, includes evidence-based debiasing mechanisms, accounts for cognitive load constraints, and cites model data to justify design choices"),
            ("Proficient (3)", "Design addresses major biases with reasonable interventions and some reference to model evidence"),
            ("Developing (2)", "Design identifies some biases but interventions are vague or not connected to model data"),
            ("Beginning (1)", "Design is incomplete or does not connect cognitive bias concepts to the decision tool")
        ],
        "support": [
            "Provide a reference chart of common cognitive biases with everyday examples students can relate to",
            "Use a simplified flowchart showing: Input -> Brain Processing -> Output, with bias as a filter in the middle",
            "Sentence frames: 'When ___ increases, bias strength ___ because the brain ___'"
        ],
        "extensions": [
            "Research how artificial intelligence systems can develop their own form of bias through training data and compare AI bias to human cognitive bias",
            "Investigate how cognitive biases affect jury decision-making in criminal trials and what safeguards exist",
            "Design an experiment to measure confirmation bias in your classmates using ambiguous images or news headlines"
        ],
        "cross_curr": [
            ("Math", "Calculate the probability of diagnostic error as a function of bias strength using a simple Bayesian model — how does prior probability affect the interpretation of test results?"),
            ("ELA", "Analyze how political advertisements and news media exploit cognitive biases like anchoring, framing, and confirmation bias to influence public opinion"),
            ("Psychology", "Research Kahneman and Tversky's prospect theory and explain how loss aversion — a cognitive bias — affects economic decision-making at personal and national scales")
        ],
        "misconceptions": [
            ("Smart people don't have cognitive biases", "Intelligence does not protect against cognitive biases and may actually make some biases worse. Research shows that higher-IQ individuals are better at rationalizing biased conclusions, not at avoiding them. Cognitive biases are features of neural architecture shared by all human brains, not deficits of intelligence.", "Show optical illusions that fool everyone regardless of intelligence. Ask: If your visual system can be tricked, why would your reasoning system be immune?"),
            ("If you know about a bias, you can just choose not to be biased", "Awareness of bias is necessary but not sufficient to eliminate it. Studies show that simply telling people about biases has minimal effect on their actual decision-making. Biases operate below conscious awareness in System 1 processing. Effective debiasing requires structural interventions — checklists, alternative generation, external review — not just willpower.", "Demonstrate: Tell students about the anchoring bias, then immediately give them an anchoring task. Most will still be anchored despite knowing about the bias."),
            ("Cognitive biases are always bad", "Cognitive biases are the result of heuristics that work correctly the vast majority of the time. Pattern recognition, quick threat detection, and social conformity all serve critical survival functions. Biases only become problematic in specific situations — when evidence is ambiguous, stakes are high, or the environment differs from what the brain evolved for. The goal isn't to eliminate biases but to recognize when they're likely to mislead.", "Discuss: In what situations is quick, biased thinking actually better than slow, careful analysis? (Answer: immediate physical danger, social situations requiring fast response, routine decisions)")
        ],
    })

    # L02: The Science of Sleep
    lessons.append({
        "id": "G12L1-L02",
        "title": "The Science of Sleep: Why Teens Can't Wake Up",
        "subtitle": "Modeling Circadian Rhythms, Melatonin, and Sleep Architecture",
        "ngss": "HS-LS1-3",
        "ngss_desc": "Plan and conduct an investigation to provide evidence that feedback mechanisms maintain homeostasis.",
        "big_question": "If sleep is so important for health and learning, why did evolution wire teenage brains to stay up late and wake up late — and why does society force you to fight your own biology every school morning?",
        "objectives": [
            "Model how the circadian clock, melatonin production, light exposure, and sleep pressure interact to regulate sleep timing",
            "Explain why adolescent circadian rhythms shift later and how this conflicts with school schedules",
            "Predict how screen time, caffeine, and schedule changes affect sleep quality and cognitive performance",
            "Analyze the evidence for later school start times as a public health intervention"
        ],
        "vocabulary": [
            ("Circadian Rhythm", "A roughly 24-hour internal biological clock regulated by the suprachiasmatic nucleus (SCN) in the hypothalamus — controls sleep-wake cycles, hormone release, body temperature, and dozens of physiological processes"),
            ("Melatonin", "A hormone produced by the pineal gland in response to darkness that signals the body to prepare for sleep — production begins about 2 hours before natural sleep onset and is suppressed by blue light exposure"),
            ("Sleep Pressure", "The accumulating drive to sleep caused by the buildup of adenosine in the brain during waking hours — the longer you're awake, the stronger the pressure to sleep, and caffeine works by blocking adenosine receptors"),
            ("Sleep Architecture", "The structured pattern of sleep stages throughout the night — cycling between light sleep, deep sleep, and REM sleep approximately every 90 minutes, with deep sleep concentrated early and REM later")
        ],
        "components": [
            ("Light Exposure", "The amount and timing of light entering the eyes, particularly blue-wavelength light from screens and artificial sources — the primary external signal that sets the circadian clock", True),
            ("Circadian Phase", "The current position in the 24-hour biological cycle, controlled by the SCN — determines when the body naturally wants to sleep and wake, and shifts about 2 hours later during adolescence", False),
            ("Melatonin Level", "The concentration of melatonin in the bloodstream — rises in darkness to promote sleep and drops with light exposure to promote wakefulness", False),
            ("Sleep Pressure", "The accumulated adenosine in the brain that creates the drive to sleep — builds during waking hours and clears during sleep, especially deep sleep", False),
            ("Cognitive Performance", "The brain's ability to learn, remember, focus, and make decisions — directly dependent on adequate sleep quality and timing alignment with the circadian rhythm", False)
        ],
        "think_about_it": "During puberty, the circadian clock shifts about 2 hours later — melatonin doesn't rise until around 11 PM instead of 9 PM. But school still starts at 7:30 AM. What does your model predict about Cognitive Performance for a typical teenager?",
        "scenarios": [
            ("Natural Schedule", "Set Light Exposure to natural daylight patterns with no screens after sunset — observe how Circadian Phase, Melatonin Level, and Sleep Pressure align for optimal sleep"),
            ("Screen Time Before Bed", "Add 2 hours of blue light exposure from screens before bed — observe how this delays Melatonin Level rise and shifts Circadian Phase later"),
            ("Early School Start", "Force wake time to 6:30 AM with adolescent circadian phase — observe the impact on Sleep Pressure clearance and Cognitive Performance throughout the day")
        ],
        "sim_scenarios": [
            ("Natural Rhythm", "Light: Natural daylight | No screens after 8 PM | Wake: Natural", "What do you predict happens to Cognitive Performance when sleep timing matches the circadian rhythm?"),
            ("Blue Light Disruption", "Light: 2 hours screen time before bed | Wake: 6:30 AM", "How does blue light from phones and laptops affect Melatonin Level and subsequent sleep quality?"),
            ("Sleep Debt Accumulation", "Light: Screens until midnight | Wake: 6:30 AM | Repeat 5 days", "What happens to Cognitive Performance after five days of circadian misalignment?")
        ],
        "discoveries": [
            "The adolescent circadian shift is a biological reality — melatonin onset occurs 1-2 hours later in teens, making early wake times fight fundamental biology",
            "Blue light from screens at night directly suppresses melatonin production, delaying sleep onset by 30-90 minutes even when the person feels tired",
            "Sleep debt is cumulative — each night of insufficient sleep compounds cognitive impairment, and weekend catch-up only partially restores function",
            "Cognitive performance is best when sleep timing aligns with circadian phase — it's not just total hours but WHEN those hours occur that matters"
        ],
        "answer": "Teens can't wake up because their brains are biologically wired to sleep later. During puberty, the circadian clock shifts approximately 2 hours later, so melatonin doesn't rise until around 11 PM and the body naturally wants to wake around 8-9 AM. This isn't laziness — it's neurobiology. When school forces a 6:30 AM wake time, teens accumulate chronic sleep debt that impairs memory consolidation, emotional regulation, and academic performance. The science is overwhelming: the American Academy of Pediatrics recommends school start no earlier than 8:30 AM, and schools that have shifted later show improved grades, attendance, and mental health.",
        "stem_title": "Design an Evidence-Based School Schedule",
        "stem_mission": "Using your model data, design an optimal school schedule for your district that maximizes student cognitive performance while addressing practical constraints like transportation, athletics, and parent work schedules.",
        "stem_scenario": "Your school district is considering shifting high school start times from 7:30 AM to 8:45 AM based on sleep science. However, parents are concerned about after-school activities, bus scheduling, and supervision. The school board wants your team to present a data-driven proposal that addresses both the science and the logistics.",
        "stem_questions": [
            "What does your model predict about cognitive performance at 7:30 AM vs. 8:45 AM for a typical teen circadian phase?",
            "How could you redesign the school day to accommodate later start times without cutting instructional time?",
            "What evidence would you present to parents who believe early start times build character and discipline?"
        ],
        "stem_design_qs": [
            "What specific start and end times does your schedule propose and what is the scientific basis?",
            "How does your design address transportation, athletics, and parent work schedule constraints?",
            "What model evidence supports your claim that the new schedule will improve academic outcomes?",
            "How would you measure the effectiveness of your proposed schedule changes?"
        ],
        "career": "Sleep scientists and chronobiologists research circadian rhythms and sleep disorders, working in hospitals, research universities, and pharmaceutical companies, earning $70,000-$140,000/year. Public health policy analysts who translate sleep research into school policy recommendations earn $55,000-$95,000/year.",
        "images": img("G12L1-L02",
            "A photorealistic image of a diverse 17-18 year old student struggling to stay awake in an early morning classroom, head propped on hand, other students similarly drowsy, blue-tinted early morning light through windows",
            "A diverse group of 17-18 year old students in a modern biology classroom examining brain models and circadian rhythm diagrams, some students looking tired while engaged in discussion",
            "A diverse group of 17-18 year old students working on laptops building computational models of sleep cycles, modern classroom with sleep stage diagrams and circadian charts on walls",
            "A teacher leading discussion with diverse 17-18 year old students about sleep science, a melatonin cycle graph and brain diagram on smartboard, students actively participating",
            "Diverse 17-18 year old students designing school schedule proposals on whiteboards with circadian rhythm charts, clock diagrams, and data tables"
        ),
        "pre_assessment": [
            "What time do you naturally fall asleep and wake up on weekends when you have no alarm? How different is this from school days?",
            "Why do you think teenagers tend to stay up later than younger children or adults?",
            "What do you think happens in your brain while you sleep — is it just resting or doing something active?",
            "Do you think getting 6 hours of sleep from midnight to 6 AM is the same as 6 hours from 10 PM to 4 AM? Why or why not?"
        ],
        "extend_components": [
            ("Caffeine Level", "The concentration of caffeine in the bloodstream — blocks adenosine receptors to mask sleep pressure without actually reducing it, with a half-life of 5-6 hours"),
            ("REM Sleep Proportion", "The percentage of total sleep spent in REM stages — critical for memory consolidation and emotional processing, concentrated in the last 2-3 hours of sleep and disproportionately lost with early wake times"),
            ("Cortisol Cycle", "The daily rhythm of the stress hormone cortisol — normally peaks at wake time and drops at night, but becomes dysregulated with chronic sleep deprivation, contributing to anxiety and depression")
        ],
        "reflections": [
            "How does your model explain why you might feel exhausted on a school morning but wide awake at midnight?",
            "Why is it not possible to simply 'train yourself' to be a morning person during adolescence?",
            "What does the model predict about the effectiveness of catching up on sleep during weekends?",
            "If a school district showed you data proving that later start times improve grades, attendance, and mental health, what argument could someone make against the change?",
            "What are the limitations of modeling sleep with only five components?"
        ],
        "dimensions": [
            ("Science Practice", "Developing and Using Models", "Students develop computational models to predict how light exposure, circadian phase, and sleep pressure interact to determine sleep quality and cognitive performance."),
            ("Disciplinary Core Idea", "LS1.A Structure and Function", "Feedback mechanisms including the circadian clock and sleep homeostasis maintain the body's sleep-wake cycle, and disruptions to these mechanisms impair cognitive and physiological function."),
            ("Crosscutting Concept", "Stability and Change", "Students analyze how the circadian system maintains stable sleep-wake cycles through feedback mechanisms and how external disruptions (light, schedules) shift the system away from equilibrium.")
        ],
        "cast_items": [
            "Model how circadian rhythms and sleep homeostasis interact to regulate sleep timing and quality",
            "Predict the effect of light exposure changes on melatonin production and sleep onset",
            "Explain why adolescent circadian phase shifts create a biological conflict with early school schedules"
        ],
        "cast_questions": [
            ("Multiple Choice:", "A student uses their phone in bed until 11:30 PM and must wake at 6:30 AM for school. Based on the sleep model, which component is most directly disrupted first, and what cascade of effects follows?"),
            ("Constructed Response:", "Using your model, explain why the American Academy of Pediatrics recommends high school start times no earlier than 8:30 AM. Reference the circadian phase shift during adolescence and its effects on at least three components.")
        ],
        "background_intro": "Sleep is not a passive state — it's an active, highly structured process essential for memory consolidation, emotional regulation, immune function, and physical growth. During adolescence, a biological shift in the circadian clock creates a perfect storm: the brain wants to sleep later, but society demands earlier wake times, resulting in chronic sleep deprivation that affects millions of students.",
        "background_sections": [
            ("The Two-Process Model of Sleep", "Sleep is regulated by two independent systems: Process C (circadian rhythm) and Process S (sleep homeostasis). Process C is controlled by the suprachiasmatic nucleus, a cluster of ~20,000 neurons in the hypothalamus that tracks the 24-hour day using light as the primary cue. Process S is driven by the accumulation of adenosine in the brain during waking hours. When both systems align — high sleep pressure meeting circadian sleep phase — you fall asleep quickly and sleep well."),
            ("The Adolescent Circadian Shift", "During puberty, the circadian clock shifts approximately 1-3 hours later due to changes in melatonin secretion timing and sensitivity to light. This is not a choice or a habit — it's a fundamental change in brain biology. Melatonin onset, which occurs around 8-9 PM in pre-pubescent children, shifts to 10-11 PM in adolescents. This means a teenager physically cannot fall asleep as early as a child or adult, even with perfect sleep hygiene."),
            ("Blue Light and Melatonin Suppression", "The photoreceptors responsible for setting the circadian clock are particularly sensitive to blue-wavelength light (460-480nm). Electronic screens emit significant blue light, and exposure within 2 hours of bedtime has been shown to suppress melatonin production by up to 50%, delay sleep onset by 30-90 minutes, and reduce REM sleep. For adolescents with already-delayed circadian phases, screen time before bed compounds the biological shift with a behavioral one."),
            ("Sleep Deprivation and Academic Performance", "The CDC reports that 73% of high school students get less than the recommended 8-10 hours of sleep. Research shows that each hour of sleep lost below optimal is associated with a 0.07 GPA decrease, increased absenteeism, and higher rates of anxiety and depression. Schools that have adopted later start times (8:30 AM or later) report 4-5% increases in standardized test scores, reduced car accidents among teen drivers, and improved mental health outcomes.")
        ],
        "lever_L": "Students identify light exposure, circadian phase, melatonin level, sleep pressure, and cognitive performance as the key components of the teen sleep system.",
        "lever_E": "Students determine that light exposure sets circadian phase, darkness triggers melatonin, waking hours build sleep pressure, and alignment of these factors determines cognitive performance.",
        "lever_V": "Students build a computational model showing how the circadian system, melatonin, and sleep pressure interact to determine when teens naturally sleep and how well they function.",
        "lever_Ev": "Students run natural schedule, blue light disruption, and early school start scenarios to test predictions about teen sleep biology versus societal demands.",
        "lever_R": "Students add caffeine, REM proportion, or cortisol to explore how common teen behaviors and stress interact with the basic sleep system.",
        "slides_guide": slides("The Science of Sleep", "Modeling Circadian Rhythms and Sleep Architecture",
            [("Light Exposure",), ("Circadian Phase",), ("Melatonin Level",), ("Sleep Pressure",), ("Cognitive Performance",)],
            "During puberty, melatonin doesn't rise until 11 PM. School starts at 7:30 AM. What happens?",
            [("Natural Schedule",), ("Screen Time",), ("Early School Start",)],
            ["Adolescent circadian shift is biological reality", "Blue light delays melatonin 30-90 min"],
            "Teens can't wake up because their brains are wired to sleep later during puberty.",
            "Design an Evidence-Based School Schedule",
            "Design an optimal school schedule maximizing cognitive performance.",
            "District considering shifting start times from 7:30 to 8:45 AM.",
            ["What does model predict about 7:30 vs 8:45 AM?", "How to redesign school day?"],
            "Sleep scientists earn $70,000-$140,000/year."),
        "sort_reasoning": "Light Exposure is external because it comes from the environment and can be controlled by behavior choices. Circadian Phase, Melatonin Level, Sleep Pressure, and Cognitive Performance are internal because they are physiological processes that respond to external inputs and interact within the body's regulatory systems.",
        "relationships": [
            ("Light Exposure to Circadian Phase", "DETERMINES", "Light, especially blue wavelength, is the primary signal that sets the timing of the circadian clock. Morning light advances the clock (earlier sleep); evening light delays it (later sleep)."),
            ("Circadian Phase to Melatonin Level", "DETERMINES", "The circadian clock triggers melatonin production as the sleep phase approaches. In teens, this trigger occurs about 2 hours later than in adults."),
            ("Melatonin Level to Sleep Pressure", "POSITIVE (+)", "Rising melatonin reinforces the biological drive to sleep, working with accumulated adenosine to promote sleep onset."),
            ("Sleep Pressure to Cognitive Performance", "NEGATIVE (-)", "Unresolved sleep pressure from insufficient or poorly timed sleep directly impairs memory, attention, and executive function.")
        ],
        "sim_answers": [
            ("Natural Schedule Scenario", "With natural light patterns and no screen interference, Circadian Phase aligns with a ~11 PM sleep onset for teens. Melatonin rises appropriately, sleep pressure clears during a full night's sleep, and Cognitive Performance is at baseline optimal levels. This represents the biological ideal that most teens rarely experience."),
            ("Early School Start Scenario", "Forcing a 6:30 AM wake time against a teen circadian phase that promotes sleep until 8-9 AM cuts 1.5-2.5 hours from the sleep period. Sleep Pressure doesn't fully clear, REM-rich late sleep is lost, and Cognitive Performance drops significantly — especially for tasks requiring memory consolidation and emotional regulation. After five days of this pattern, cumulative sleep debt creates performance equivalent to staying awake for 24 hours straight.")
        ],
        "reflection_exemplars": [
            ("Why can't teens just go to bed earlier?", "Our model shows that the circadian clock physically controls when melatonin is produced. During adolescence, the clock shifts 1-3 hours later, meaning melatonin doesn't rise until 10-11 PM regardless of when the teen gets in bed. Lying in bed without melatonin doesn't produce quality sleep — it produces frustration and anxiety that can worsen insomnia. This is biology, not behavior. Telling a teen to fall asleep at 9 PM is like telling an adult to fall asleep at 6 PM — the brain simply isn't ready."),
            ("What's the strongest evidence for later start times?", "The model shows that when wake time aligns with circadian phase, all downstream components improve — sleep pressure clears completely, REM sleep is preserved, and cognitive performance reaches optimal levels. Real-world data confirms this: when the Seattle School District shifted start times from 7:50 to 8:45 AM, students gained an average of 34 minutes of sleep per night, grades improved, and chronic tardiness decreased by 50%. The biological model and the epidemiological data tell the same story.")
        ],
        "stem_intro": "Present the challenge: Your school district is debating whether to shift high school start times later. The school board wants evidence-based proposals that address both the science and the practical logistics. Use your model data to design a schedule and present your case.",
        "stem_concepts": [
            ("Chronotype Variation", "Not all teens have identical circadian phases. Chronotype — whether someone is naturally an early bird or night owl — is largely genetic and varies by up to 3 hours across the population. Any school schedule must accommodate this biological diversity."),
            ("Social Jet Lag", "The difference between a person's biological sleep schedule and their social obligations. For teens with late chronotypes forced into early school schedules, social jet lag can exceed 3 hours — equivalent to flying from New York to Los Angeles every Monday morning."),
            ("Policy Implementation Science", "The gap between knowing what works and implementing it. Even when evidence strongly supports later start times, implementation requires addressing transportation logistics, teacher contracts, community athletics, and parent work schedules.")
        ],
        "stem_eval": [
            ("Expert (4)", "Proposal specifies exact times with circadian science justification, addresses all logistics, presents model evidence, and includes an evaluation plan to measure outcomes"),
            ("Proficient (3)", "Proposal has reasonable times with science basis and addresses most practical constraints"),
            ("Developing (2)", "Proposal suggests later times but lacks detailed logistics or strong model evidence"),
            ("Beginning (1)", "Proposal is incomplete or not connected to circadian science evidence")
        ],
        "support": [
            "Provide a visual timeline showing melatonin levels across 24 hours for teens vs. adults",
            "Use a simplified diagram: Light -> Clock -> Melatonin -> Sleep -> Performance",
            "Sentence frames: 'When light exposure ___ in the evening, melatonin production ___ because ___'"
        ],
        "extensions": [
            "Research shift work disorder and model how rotating work schedules disrupt the circadian system — what does this predict about health outcomes for night-shift workers?",
            "Investigate the relationship between screen time, blue light filtering apps, and melatonin suppression — do blue light glasses actually work?",
            "Analyze sleep data from your own phone or fitness tracker and compare your actual sleep patterns to what the circadian model predicts for your age"
        ],
        "cross_curr": [
            ("Math", "Calculate cumulative sleep debt over a school week if a teen's circadian phase calls for 11 PM-8 AM sleep but school requires a 6:30 AM wake. Graph the relationship between sleep debt and cognitive performance decline."),
            ("ELA", "Write a persuasive letter to your school board arguing for later start times, using scientific evidence from your model and published research to support your case"),
            ("Health/PE", "Research the connection between sleep deprivation and athletic performance — how does insufficient sleep affect reaction time, injury risk, and muscle recovery in teen athletes?")
        ],
        "misconceptions": [
            ("Teenagers who stay up late are just being lazy or irresponsible", "The adolescent circadian shift is a well-documented biological phenomenon driven by changes in melatonin secretion timing during puberty. Telling a teenager to go to bed at 9 PM is biologically equivalent to telling an adult to fall asleep at 6 PM — the brain's clock simply isn't ready. This shift reverses in the early twenties.", "Show the melatonin curves for children, teens, and adults side by side. The biological reality is unmistakable."),
            ("You can train yourself to need less sleep", "Sleep need is biologically determined and not reducible through practice. Studies of people who claim to thrive on 4-5 hours of sleep show measurable cognitive impairment they've simply adapted to not noticing. The rare genetic variant (DEC2 mutation) that allows short sleep affects less than 1% of the population.", "Compare this to breathing — you can hold your breath longer with practice, but you can't train yourself to need less oxygen."),
            ("Catching up on sleep on weekends fixes everything", "Weekend sleep recovery partially repays sleep debt but doesn't restore all lost function. The irregular schedule creates 'social jet lag' that further disrupts the circadian clock. Research shows that chronic sleep restriction followed by recovery sleep does not fully restore cognitive performance, attention, or metabolic health.", "Run the model: After 5 days of debt, how much weekend sleep is needed to return to baseline? The answer is more than 2 weekend mornings can provide.")
        ],
    })

    # L03: Is Your Tap Water Safe?
    lessons.append({
        "id": "G12L1-L03",
        "title": "Is Your Tap Water Safe?",
        "subtitle": "Modeling Water Contamination Pathways and Public Health Systems",
        "ngss": "HS-PS1-2, HS-ESS3-4",
        "ngss_desc": "Construct and revise an explanation for the outcome of a simple chemical reaction based on the outermost electron states of atoms. Evaluate or refine a technological solution that reduces impacts of human activities on natural systems.",
        "big_question": "The water coming out of your faucet traveled through miles of pipes before reaching your glass — how do we know what's in it, and what happens when the system fails?",
        "objectives": [
            "Model how water source quality, treatment processes, distribution infrastructure, and testing frequency interact to determine tap water safety",
            "Explain how lead contamination occurs through pipe corrosion and why it disproportionately affects older neighborhoods",
            "Predict how changes in water chemistry, aging infrastructure, or reduced testing could create a contamination crisis",
            "Analyze the Flint water crisis as a systems failure and identify which components failed"
        ],
        "vocabulary": [
            ("Parts Per Billion (ppb)", "A measurement of contamination concentration — the EPA action level for lead in drinking water is 15 ppb, but no level of lead exposure is considered safe for children"),
            ("Corrosion Control", "Chemical treatment that creates a protective coating inside water pipes to prevent lead and copper from leaching into drinking water — the failure of this treatment triggered the Flint crisis"),
            ("Water Treatment", "The multi-step process of making raw water safe for drinking — typically includes coagulation, sedimentation, filtration, and disinfection, removing 99.9% of pathogens"),
            ("Distribution System", "The network of pipes, storage tanks, and pumping stations that deliver treated water from the treatment plant to your tap — aging infrastructure is the weakest link in water safety")
        ],
        "components": [
            ("Source Water Quality", "The chemical and biological quality of raw water from rivers, lakes, or aquifers before treatment — affected by agricultural runoff, industrial discharge, and natural mineral content", True),
            ("Treatment Effectiveness", "How well the water treatment plant removes contaminants through filtration, disinfection, and chemical treatment — determines the quality of water entering the distribution system", False),
            ("Pipe Infrastructure Age", "The age and material of pipes in the distribution system — older cities have lead service lines installed before 1986 that can leach lead when protective coatings fail", True),
            ("Corrosion Rate", "The speed at which pipe materials dissolve into the water — increases when water chemistry changes (pH, chloride levels) and protective coatings break down", False),
            ("Tap Water Safety", "The final quality of water at the consumer's faucet — determined by the cumulative effects of source quality, treatment, and distribution system integrity", False)
        ],
        "think_about_it": "In Flint, Michigan, the city switched water sources to save money. The new source water had different chemistry that increased Corrosion Rate. What does your model predict happened to Tap Water Safety, and why didn't Treatment Effectiveness prevent the crisis?",
        "scenarios": [
            ("Healthy System", "Set Source Water Quality to good, Treatment Effectiveness to high, and Pipe Infrastructure to modern — observe baseline Tap Water Safety"),
            ("Flint Crisis Simulation", "Switch Source Water Quality to corrosive chemistry with aging lead pipes and no corrosion control — observe how Corrosion Rate spikes and Tap Water Safety collapses"),
            ("Infrastructure Neglect", "Keep Source Water and Treatment good but age Pipe Infrastructure to 80+ years — observe how infrastructure decay alone can compromise safety")
        ],
        "sim_scenarios": [
            ("Healthy System", "Source: Clean | Treatment: Full | Pipes: Modern copper/PVC", "When all system components are functioning well, what level of Tap Water Safety do you predict?"),
            ("Flint Scenario", "Source: Corrosive river water | Treatment: No corrosion control | Pipes: 1920s lead", "What happens when corrosive water meets unprotected lead pipes?"),
            ("Aging Infrastructure", "Source: Clean | Treatment: Full | Pipes: 80+ year old lead/iron", "Can aging pipes alone compromise water safety even with good treatment?")
        ],
        "discoveries": [
            "Water safety is a SYSTEM property — no single component guarantees safe water; the system depends on source quality AND treatment AND distribution integrity working together",
            "Corrosion control is the critical link — when water chemistry changes without adjusting corrosion treatment, protective pipe coatings dissolve and heavy metals leach into drinking water",
            "Aging infrastructure is a ticking time bomb — even with excellent source water and treatment, deteriorating pipes can introduce contaminants after the water leaves the plant",
            "The Flint crisis was a cascading system failure — changing the source without adjusting treatment for the new water chemistry triggered pipe corrosion that poisoned an entire city"
        ],
        "answer": "Your tap water's safety depends on an interconnected system of source protection, treatment, and distribution. When any component fails, contamination can reach your glass. The Flint crisis demonstrated that changing water sources without adjusting corrosion control treatment caused lead pipes to corrode, releasing dangerous lead levels into drinking water. The scary truth: many American cities have similar aging lead infrastructure, and the EPA estimates that 6-10 million homes still receive water through lead service lines. Water safety isn't just chemistry — it's infrastructure, policy, and investment.",
        "stem_title": "Design a Community Water Monitoring System",
        "stem_mission": "Design a low-cost, community-based water quality monitoring system that can detect contamination before it reaches dangerous levels and alert residents in real-time.",
        "stem_scenario": "After the Flint crisis, a neighboring city wants to prevent a similar disaster. They have aging infrastructure, limited budget for pipe replacement, and want residents to be empowered with water quality data. Your team must design a monitoring system that provides early warning of contamination events.",
        "stem_questions": [
            "What contaminants should your system test for and at what frequency?",
            "Where in the distribution system should sensors be placed for maximum early detection?",
            "How can your system make data accessible to residents who may not trust government agencies?"
        ],
        "stem_design_qs": [
            "What specific sensors and testing methods does your system use and what is the scientific basis for each?",
            "How does your monitoring network coverage relate to the distribution system architecture?",
            "What alert thresholds trigger action and how were they determined from model data?",
            "How would your system have detected the Flint crisis earlier than the actual timeline?"
        ],
        "career": "Environmental engineers design water treatment systems and monitor water quality, earning $65,000-$110,000/year. Water quality scientists test drinking water for contaminants at utilities and government agencies, earning $50,000-$85,000/year. Environmental justice advocates work to ensure equitable access to clean water, earning $45,000-$80,000/year.",
        "images": img("G12L1-L03",
            "A photorealistic image of water flowing from a kitchen faucet into a glass, with a subtle split showing clean water on one side and discolored water on the other, dramatic lighting emphasizing the contrast",
            "A diverse group of 17-18 year old students in a modern chemistry lab testing water samples with pH meters and testing kits, colorful chemical indicators visible, engaged and focused",
            "A diverse group of 17-18 year old students working on laptops building computational models of water distribution systems, modern classroom with water cycle diagrams and pipe infrastructure maps",
            "A teacher leading discussion with diverse 17-18 year old students about water contamination, a water distribution system diagram on smartboard showing treatment plant to homes",
            "Diverse 17-18 year old students designing water monitoring systems on whiteboards with sensor placement maps, alert flowcharts, and water chemistry data"
        ),
        "pre_assessment": [
            "Where does the water in your tap come from, and what happens to it before it reaches your glass?",
            "Have you ever heard of a city having contaminated drinking water? What do you know about what happened?",
            "What do you think is in your tap water right now besides H2O?",
            "Who is responsible for making sure your drinking water is safe?"
        ],
        "extend_components": [
            ("Testing Frequency", "How often water quality is measured at various points in the distribution system — less frequent testing means contamination can go undetected for weeks or months"),
            ("Community Socioeconomic Status", "The economic resources of the community served — lower-income communities often have older infrastructure, less political power to demand repairs, and fewer resources for bottled water alternatives"),
            ("Regulatory Enforcement", "The strength and consistency of government oversight — weak enforcement allows utilities to delay maintenance, skip tests, or manipulate results")
        ],
        "reflections": [
            "How does your model explain why the Flint water crisis was a systems failure rather than a single-point failure?",
            "Why might lower-income communities be more vulnerable to water contamination than wealthier ones?",
            "What does your model suggest about the relationship between infrastructure investment and public health?",
            "If you could add one component to your model to make it more accurate, what would it be and why?",
            "How does the concept of 'parts per billion' change the way you think about contamination?"
        ],
        "dimensions": [
            ("Science Practice", "Developing and Using Models", "Students develop computational models to predict how source water quality, treatment, infrastructure age, and corrosion interact to determine tap water safety."),
            ("Disciplinary Core Idea", "PS1.A Structure and Properties of Matter / ESS3.C Human Impacts on Earth Systems", "Water chemistry (pH, dissolved minerals, chloride) determines corrosion rates in pipe materials. Human infrastructure decisions directly affect water quality at the tap."),
            ("Crosscutting Concept", "Systems and System Models", "Students analyze water safety as an emergent property of an interconnected system where failure in any component can cascade through the entire system.")
        ],
        "cast_items": [
            "Model how water chemistry changes interact with pipe infrastructure to affect contamination levels",
            "Predict tap water safety outcomes based on source quality, treatment effectiveness, and infrastructure condition",
            "Explain how the Flint crisis resulted from cascading failures across multiple system components"
        ],
        "cast_questions": [
            ("Multiple Choice:", "A city switches from a lake water source to a river water source with higher chloride content. The treatment plant does not adjust corrosion control chemicals. What does the model predict will happen to lead levels at the tap and why?"),
            ("Constructed Response:", "Using your model, explain why replacing lead pipes is a more permanent solution to lead contamination than adjusting water chemistry. Reference the relationships between at least three components.")
        ],
        "background_intro": "Every day, 300 million Americans turn on their taps and trust that the water is safe. Most of the time, it is — the United States has one of the safest public water supplies in the world. But the infrastructure that delivers that water is aging, with some pipes dating back over a century, and the consequences of system failure can be catastrophic.",
        "background_sections": [
            ("How Water Treatment Works", "Modern water treatment is a multi-barrier approach: coagulation removes large particles, sedimentation allows solids to settle, filtration through sand and activated carbon removes smaller contaminants, and disinfection (chlorine or UV) kills pathogens. This process removes 99.9% of harmful organisms. However, treatment at the plant doesn't prevent contamination that occurs AFTER water enters the distribution system."),
            ("The Lead Pipe Problem", "Before 1986, lead was commonly used in water service lines, solder, and fixtures. The EPA estimates 6-10 million lead service lines remain in use across the US. Lead doesn't typically leach into water when pipes develop a protective mineral coating (called a scale). However, if water chemistry changes — becoming more acidic or containing more chloride — this protective coating dissolves, releasing lead directly into drinking water."),
            ("The Flint Water Crisis", "In April 2014, Flint, Michigan switched its water source from Lake Huron to the Flint River to save $5 million over two years. The river water was more corrosive, but the city failed to add corrosion control chemicals (orthophosphate). Within months, the protective scale inside Flint's lead pipes dissolved, and lead levels at some taps exceeded 13,000 ppb — nearly 900 times the EPA action level. An estimated 6,000-12,000 children were exposed to elevated lead, causing irreversible neurological damage."),
            ("Environmental Justice and Water Access", "Water contamination disproportionately affects communities of color and low-income communities. EPA data shows that drinking water violations are 40% more likely in communities with higher poverty rates. These communities often have the oldest infrastructure, least political influence, and fewest resources for alternatives. The Flint crisis highlighted how water safety is not just a technical issue but an issue of equity and justice.")
        ],
        "lever_L": "Students identify source water quality, treatment effectiveness, pipe infrastructure age, corrosion rate, and tap water safety as the key components of the drinking water system.",
        "lever_E": "Students determine that source chemistry and pipe age drive corrosion rate, treatment mitigates source contamination, and the interaction of all factors determines final tap water safety.",
        "lever_V": "Students build a computational model showing how the water delivery system functions as an interconnected chain where failure at any point can compromise safety at the tap.",
        "lever_Ev": "Students run healthy system, Flint crisis, and infrastructure neglect scenarios to identify which failures are most dangerous and why cascading failures are hardest to prevent.",
        "lever_R": "Students add testing frequency, community socioeconomic status, or regulatory enforcement to explore how policy and social factors interact with the physical system.",
        "slides_guide": slides("Is Your Tap Water Safe?", "Modeling Water Contamination and Public Health",
            [("Source Water Quality",), ("Treatment Effectiveness",), ("Pipe Infrastructure Age",), ("Corrosion Rate",), ("Tap Water Safety",)],
            "In Flint, switching water sources increased corrosion. Why didn't treatment prevent the crisis?",
            [("Healthy System",), ("Flint Crisis",), ("Infrastructure Neglect",)],
            ["Water safety is a SYSTEM property", "Corrosion control is the critical link"],
            "Your tap water depends on source protection, treatment, and distribution all working together.",
            "Design a Community Water Monitoring System",
            "Design a low-cost monitoring system for early contamination detection.",
            "City wants to prevent a Flint-style crisis with limited budget.",
            ["What contaminants to test for?", "Where to place sensors?"],
            "Environmental engineers earn $65,000-$110,000/year."),
        "sort_reasoning": "Source Water Quality and Pipe Infrastructure Age are external because they represent pre-existing conditions that the water treatment system must respond to — the quality of raw water and the state of pipes exist before treatment begins. Treatment Effectiveness, Corrosion Rate, and Tap Water Safety are internal because they are outcomes of how the system processes and delivers water.",
        "relationships": [
            ("Source Water Quality to Treatment Effectiveness", "POSITIVE (+)", "Better source water quality makes treatment more effective because the plant has fewer contaminants to remove, staying within its design capacity."),
            ("Source Water Quality to Corrosion Rate", "NEGATIVE (-)", "Better source water quality (proper pH, low chloride) reduces pipe corrosion. Corrosive source water attacks pipe materials and dissolves protective coatings."),
            ("Pipe Infrastructure Age to Corrosion Rate", "POSITIVE (+)", "Older pipes with thinner protective coatings or deteriorating materials corrode faster, especially when exposed to changes in water chemistry."),
            ("Corrosion Rate to Tap Water Safety", "NEGATIVE (-)", "Higher corrosion releases more heavy metals (lead, copper) into the water between the treatment plant and the tap, directly reducing safety.")
        ],
        "sim_answers": [
            ("Healthy System Scenario", "With good Source Water Quality, high Treatment Effectiveness, and modern pipes, Corrosion Rate stays minimal and Tap Water Safety remains high. The system works as designed — each component reinforces the others. This is the baseline that 85% of Americans experience daily."),
            ("Flint Crisis Scenario", "Switching to corrosive source water without adjusting treatment causes Corrosion Rate to spike dramatically. The aging lead pipes, which depended on a protective coating maintained by the previous water chemistry, begin dissolving lead directly into the water. Tap Water Safety collapses within weeks. The model shows this was entirely predictable — the corrosion science was well-understood; the failure was in not applying it.")
        ],
        "reflection_exemplars": [
            ("Why is water safety a systems problem?", "Our model shows that Tap Water Safety is not determined by any single component but by the interaction of all five. Good source water can be ruined by aging pipes. Excellent treatment is useless if corrosion adds lead after the water leaves the plant. Modern pipes can't compensate for contaminated source water. Each component depends on the others — and a change in any one can cascade through the system. Flint proved that even a wealthy nation can poison a city when the system fails at multiple points simultaneously."),
            ("What does this teach about infrastructure and equity?", "The model reveals that Pipe Infrastructure Age is a critical vulnerability. Communities with the oldest infrastructure — typically lower-income communities and communities of color that received less investment over decades — face the highest risk. Our model shows that even with good source water and treatment, 80+ year old lead pipes create unacceptable Corrosion Rates. Water safety is ultimately an investment question: who gets new pipes and who doesn't? The science is clear; the policy choices determine who bears the risk.")
        ],
        "stem_intro": "Present the challenge: A city with aging infrastructure wants to prevent a Flint-style crisis. Your team must design a community-based water monitoring system that provides early warning of contamination and empowers residents with real-time data.",
        "stem_concepts": [
            ("Electrochemical Corrosion", "Lead pipes corrode through electrochemical reactions where the lead metal oxidizes and dissolves into the water. The rate depends on water pH, dissolved oxygen, chloride concentration, and temperature. Orthophosphate treatment creates a protective phosphate-lead mineral coating that prevents direct contact between water and pipe metal."),
            ("Sensor Networks", "Modern water quality monitoring uses networks of sensors measuring pH, turbidity, chlorine residual, conductivity, and specific metal concentrations at multiple points in the distribution system. Real-time data enables rapid response to contamination events."),
            ("Environmental Justice Frameworks", "Environmental justice principles require that no community bears a disproportionate share of environmental risks. Water monitoring systems must prioritize the most vulnerable communities — those with the oldest infrastructure, lowest incomes, and highest exposure risks.")
        ],
        "stem_eval": [
            ("Expert (4)", "Design specifies sensor types, placement strategy, alert thresholds with scientific justification, addresses equity and accessibility, and demonstrates how it would have caught the Flint crisis"),
            ("Proficient (3)", "Design includes reasonable monitoring approach with some scientific basis and addresses community communication"),
            ("Developing (2)", "Design identifies monitoring needs but lacks technical specificity or community engagement strategy"),
            ("Beginning (1)", "Design is incomplete or not connected to water chemistry and contamination science")
        ],
        "support": [
            "Provide a simplified diagram of a water treatment and distribution system showing where contamination can enter",
            "Use a visual: Source -> Treatment Plant -> Pipes -> Your Tap, with risk points highlighted",
            "Sentence frames: 'When ___ changes, corrosion rate ___ because ___'"
        ],
        "extensions": [
            "Research PFAS (forever chemicals) contamination and model how these persistent chemicals move through the water system differently than lead",
            "Investigate the cost-benefit analysis of replacing all lead service lines in a city versus maintaining corrosion control — which is more cost-effective over 50 years?",
            "Map the water infrastructure age in your own community and identify which neighborhoods are most at risk"
        ],
        "cross_curr": [
            ("Math", "Calculate the lead concentration in ppb if 0.5 mg of lead dissolves from a pipe into 1,000 gallons of water flowing through it daily. At what flow rate does concentration exceed the EPA action level of 15 ppb?"),
            ("ELA", "Read excerpts from 'The Poisoned City' by Anna Clark and write an analysis connecting the book's narrative of institutional failure to the systems model you built"),
            ("Social Studies", "Research the history of environmental regulation in the US — from the Clean Water Act (1972) to the Lead and Copper Rule (1991). How has policy evolved in response to water crises?")
        ],
        "misconceptions": [
            ("If water is clear, it's safe to drink", "Many dangerous contaminants are invisible, odorless, and tasteless. Lead, PFAS, arsenic, and many bacteria cannot be detected by human senses. Clear water can contain lead at 100x the safe level without any visible sign. This is why regular testing at the tap — not just at the treatment plant — is essential.", "Demonstration: Show two glasses of water — one pure, one with dissolved lead at 50 ppb. Ask: Can you tell which is contaminated? (Answer: No. That's the problem.)"),
            ("The government tests water so it must be safe", "While utilities are required to test water, testing has significant gaps. The EPA's Lead and Copper Rule only requires testing at a sample of homes, and utilities have historically selected homes less likely to show problems. Flint's water tested 'safe' for over a year because of sampling manipulation. Testing frequency, sample site selection, and reporting transparency all matter.", "Show Flint's official test results vs. independent testing by Virginia Tech — same water, dramatically different conclusions based on where and how samples were collected."),
            ("Bottled water is always safer than tap water", "Bottled water is regulated by the FDA with less stringent standards than the EPA applies to tap water. Studies have found that 25% of bottled water is simply repackaged tap water, and some brands have tested positive for microplastics and contaminants. Tap water in most US cities is tested hundreds of times per month, while bottled water may be tested only weekly.", "Compare testing frequency: Your city's tap water is likely tested 100+ times/month. Bottled water brands may test once per week. Which has more oversight?")
        ],
    })

    # L04: The Ultra-Processed Food Problem
    lessons.append({
        "id": "G12L1-L04",
        "title": "The Ultra-Processed Food Problem",
        "subtitle": "Modeling Food Chemistry, Metabolic Pathways, and Nutritional Systems",
        "ngss": "HS-LS1-7",
        "ngss_desc": "Use a model to illustrate that cellular respiration is a chemical process whereby the bonds of food molecules and oxygen molecules are broken and the bonds in new compounds are formed, resulting in a net transfer of energy.",
        "big_question": "Why do foods engineered to be irresistible in your mouth end up being catastrophic for your body — and how did we build a food system where the cheapest calories are the most dangerous?",
        "objectives": [
            "Model how food processing level, sugar and additive content, metabolic response, and gut microbiome interact to affect long-term health",
            "Explain why ultra-processed foods trigger overconsumption through disrupted satiety signaling",
            "Predict how different dietary patterns affect metabolic health markers over time",
            "Analyze why ultra-processed foods are disproportionately marketed to and consumed by lower-income communities"
        ],
        "vocabulary": [
            ("Ultra-Processed Food", "Industrially manufactured food products containing ingredients not found in home kitchens — emulsifiers, flavor enhancers, hydrogenated oils, and high-fructose corn syrup — engineered for maximum palatability, shelf life, and profit"),
            ("Metabolic Syndrome", "A cluster of conditions — high blood sugar, excess abdominal fat, high blood pressure, abnormal cholesterol — that together dramatically increase the risk of heart disease, stroke, and type 2 diabetes"),
            ("Satiety Signaling", "The body's system for telling the brain when to stop eating — involves hormones like leptin and ghrelin that regulate hunger and fullness, disrupted by ultra-processed foods that bypass these signals"),
            ("Gut Microbiome", "The community of trillions of bacteria in the digestive tract that influence metabolism, immune function, and even mood — diversity decreases significantly with ultra-processed food consumption")
        ],
        "components": [
            ("Processing Level", "The degree of industrial processing applied to food — from unprocessed (whole apple) to ultra-processed (fruit-flavored gummy snack with 30 ingredients)", True),
            ("Sugar and Additive Load", "The concentration of added sugars, emulsifiers, preservatives, and artificial flavors in food — increases dramatically with processing level and disrupts normal metabolic responses", False),
            ("Satiety Response", "How effectively the body signals fullness after eating — ultra-processed foods are eaten 20-30% faster and produce weaker fullness signals than whole foods with the same calories", False),
            ("Metabolic Health", "The overall functioning of the body's energy regulation systems — blood sugar control, insulin sensitivity, inflammation levels, and fat storage patterns", False),
            ("Caloric Overconsumption", "The amount of excess calories consumed beyond what the body needs — driven by weak satiety signals and the engineered hyper-palatability of ultra-processed foods", False)
        ],
        "think_about_it": "In a NIH clinical trial, people eating ultra-processed meals consumed 500 more calories per day than people eating unprocessed meals — even though both groups had unlimited food. If Processing Level is the only variable changed, why does Caloric Overconsumption increase so dramatically?",
        "scenarios": [
            ("Whole Foods Diet", "Set Processing Level to minimal (whole foods) — observe how Satiety Response stays strong, Caloric Overconsumption stays low, and Metabolic Health remains high"),
            ("Ultra-Processed Diet", "Set Processing Level to maximum — observe how Sugar/Additive Load rises, Satiety Response weakens, and Caloric Overconsumption increases"),
            ("Mixed Diet Transition", "Shift from ultra-processed to 50% whole foods — observe how quickly Metabolic Health begins to recover")
        ],
        "sim_scenarios": [
            ("Whole Foods", "Processing: Minimal | All meals from whole ingredients", "What do you predict happens to Metabolic Health when the body receives food with intact fiber, nutrients, and no additives?"),
            ("Ultra-Processed", "Processing: Maximum | 80% ultra-processed calories", "What happens to satiety signals when food is engineered to be consumed quickly and in large quantities?"),
            ("Diet Shift", "Processing: Transition from 80% UPF to 50% whole foods over 4 weeks", "How quickly do you predict Metabolic Health markers begin to improve?")
        ],
        "discoveries": [
            "Ultra-processed foods override normal satiety signaling, causing people to eat 500+ extra calories per day without feeling more full — it's not about willpower, it's about food engineering",
            "The speed of eating matters: ultra-processed foods are consumed 20-30% faster, which doesn't allow time for gut hormones to signal fullness to the brain",
            "Metabolic damage from ultra-processed diets is partially reversible — shifting to whole foods shows measurable improvements in blood sugar, inflammation, and gut microbiome diversity within 2-4 weeks",
            "Food processing level predicts health outcomes better than individual nutrients — it's not just about sugar or fat content but about the entire matrix of processing that disrupts metabolic regulation"
        ],
        "answer": "Ultra-processed foods are catastrophic for health because they're engineered to bypass your body's natural satiety systems. The combination of refined ingredients, added sugars, and chemical additives creates foods that are eaten faster, produce weaker fullness signals, and trigger stronger reward responses than whole foods. A landmark NIH study showed that people eating ultra-processed meals consumed 500 more calories per day compared to unprocessed meals — with both diets matched for calories, sugar, fat, and fiber available. The body simply cannot regulate intake of foods that evolution never encountered. The crisis is magnified by economics: ultra-processed foods are the cheapest available calories, making the communities with the least money most vulnerable to diet-related disease.",
        "stem_title": "Design a School Lunch That Beats Ultra-Processing",
        "stem_mission": "Design a school lunch program that provides meals as satisfying and convenient as ultra-processed options but using minimally processed, whole-food ingredients — within the current per-meal budget.",
        "stem_scenario": "Your school district spends $1.50 per student per meal on ingredients, and 75% of current menu items are ultra-processed. The district wants to reduce ultra-processing to 25% while maintaining cost, student acceptance, and nutrition standards. Your team must design a week of lunch menus with a cost analysis.",
        "stem_questions": [
            "What makes ultra-processed school lunches so cheap and how can whole-food alternatives compete on cost?",
            "How can you make whole-food meals as appealing and convenient as processed ones for teen students?",
            "What does your model predict about student metabolic health and focus if the school shifts to whole-food lunches?"
        ],
        "stem_design_qs": [
            "What specific meals comprise your weekly menu and what is the NOVA processing classification of each component?",
            "How does your total per-student cost compare to the current budget, and what trade-offs did you make?",
            "What evidence from your model supports the claim that your menu will improve student health outcomes?",
            "How would you measure student acceptance and health impacts of your new menu?"
        ],
        "career": "Food scientists study the chemistry of food processing and develop healthier alternatives, earning $60,000-$100,000/year. Registered dietitians design nutrition programs for schools, hospitals, and communities, earning $55,000-$85,000/year. Public health nutritionists research diet-disease relationships at $65,000-$110,000/year.",
        "images": img("G12L1-L04",
            "A photorealistic split image showing ultra-processed snack foods (bright packaging, artificial colors) on one side and whole foods (fresh fruits, vegetables, grains) on the other, dramatic contrast lighting",
            "A diverse group of 17-18 year old students in a modern food science lab examining nutrition labels and food samples, microscopes and chemical testing equipment visible",
            "A diverse group of 17-18 year old students working on laptops building computational models of metabolic pathways, modern classroom with food system diagrams and NOVA classification posters",
            "A teacher leading discussion with diverse 17-18 year old students about food processing, a comparison of ingredient lists on smartboard, students examining packaged food labels",
            "Diverse 17-18 year old students designing healthy school lunch menus on whiteboards with nutrition data, cost calculations, and meal planning templates"
        ),
        "pre_assessment": [
            "What did you eat for your last meal? Try to list every ingredient you can think of.",
            "What do you think the difference is between 'processed' and 'ultra-processed' food?",
            "Why do you think some foods are very easy to overeat while others fill you up quickly?",
            "Do you think the cost of food affects what people eat? How?"
        ],
        "extend_components": [
            ("Gut Microbiome Diversity", "The variety of bacterial species in the digestive tract — decreases with ultra-processed food consumption and correlates with metabolic health, immune function, and even mental health"),
            ("Food Marketing Exposure", "The amount and type of food advertising a person encounters — children and teens see an average of 13 food ads per day, overwhelmingly for ultra-processed products"),
            ("Socioeconomic Access", "The availability and affordability of whole foods in a person's neighborhood — food deserts with limited fresh food access correlate strongly with higher ultra-processed food consumption")
        ],
        "reflections": [
            "How does your model explain why calorie counting alone doesn't capture the health impact of different diets?",
            "Why is it misleading to blame obesity on 'lack of willpower' based on what you've learned about satiety signaling?",
            "What does the model suggest about the responsibility of food companies versus individual choice?",
            "How might understanding food processing change the way you read nutrition labels?",
            "What are the ethical implications of engineering foods to bypass biological satiety signals?"
        ],
        "dimensions": [
            ("Science Practice", "Developing and Using Models", "Students develop computational models to predict how food processing level affects metabolic responses, satiety signaling, and long-term health outcomes."),
            ("Disciplinary Core Idea", "LS1.C Organization for Matter and Energy Flow in Organisms", "Cellular respiration converts food molecules into energy, but the body's metabolic response differs dramatically based on food processing level, affecting how efficiently energy is regulated."),
            ("Crosscutting Concept", "Cause and Effect", "Students identify causal mechanisms linking ultra-processing to disrupted satiety, metabolic dysfunction, and caloric overconsumption through specific biochemical pathways.")
        ],
        "cast_items": [
            "Model how food processing level affects metabolic responses and satiety signaling",
            "Predict health outcomes based on the proportion of ultra-processed versus whole foods in a diet",
            "Explain why food processing level predicts health outcomes better than individual nutrient content"
        ],
        "cast_questions": [
            ("Multiple Choice:", "Two meals contain identical calories, protein, fat, carbohydrates, sugar, and fiber. One is made from whole foods, the other from ultra-processed ingredients. The model predicts that the ultra-processed meal will result in greater caloric overconsumption. What mechanism best explains this?"),
            ("Constructed Response:", "Using your model, explain why replacing a school's ultra-processed lunch menu with whole-food alternatives could improve student academic performance. Connect food processing to at least three components in your model.")
        ],
        "background_intro": "In the last 50 years, ultra-processed foods have gone from a small fraction of the American diet to over 60% of total calories consumed. This industrial transformation of food has coincided with unprecedented rates of obesity, type 2 diabetes, and metabolic disease. The science is now clear: it's not just what nutrients are in our food that matters, but how that food is processed.",
        "background_sections": [
            ("The NOVA Classification System", "Developed by researchers at the University of Sao Paulo, the NOVA system classifies foods into four groups: unprocessed or minimally processed (fruits, vegetables, meat, eggs), processed culinary ingredients (oil, butter, sugar, salt), processed foods (canned vegetables, cheese, fresh bread), and ultra-processed foods (soft drinks, packaged snacks, instant noodles, chicken nuggets). Ultra-processed foods are defined by the presence of industrial ingredients and additives not used in home cooking."),
            ("The NIH Ultra-Processing Study", "In 2019, a landmark randomized controlled trial at the National Institutes of Health provided the first direct evidence that ultra-processing itself — not just nutrient content — drives overconsumption. Twenty adults lived in a research facility for four weeks, eating either ultra-processed or unprocessed meals for two weeks each. Diets were matched for calories, sugar, fat, fiber, and macronutrients. On the ultra-processed diet, participants ate 500 more calories per day and gained an average of 2 pounds in two weeks. On unprocessed food, they lost 2 pounds."),
            ("How Ultra-Processing Disrupts Satiety", "Ultra-processed foods undermine satiety through multiple mechanisms: they are softer and require less chewing (increasing eating speed 20-30%), they have higher caloric density per bite, their refined ingredients are absorbed faster (causing rapid blood sugar spikes and crashes), and their additives may directly alter gut hormone signaling. The brain's appetite regulation system evolved for whole foods that required significant chewing and digestion time — ultra-processed foods bypass these ancient controls."),
            ("The Economics of Ultra-Processing", "Ultra-processed foods are cheap because they use low-cost industrial ingredients (corn syrup, hydrogenated oils, starches) that have long shelf lives and require minimal preparation. Whole foods are more expensive, perishable, and require cooking skills and time. This creates a nutrition inequality where the cheapest available calories are the most metabolically harmful. In the US, households spending less than $4 per person per day on food get over 80% of their calories from ultra-processed sources.")
        ],
        "lever_L": "Students identify processing level, sugar/additive load, satiety response, metabolic health, and caloric overconsumption as the key components of the food-health system.",
        "lever_E": "Students determine that processing level drives additive load, additives weaken satiety, weak satiety causes overconsumption, and overconsumption degrades metabolic health in a reinforcing cycle.",
        "lever_V": "Students build a computational model showing how food processing creates a cascade from engineered palatability to metabolic dysfunction.",
        "lever_Ev": "Students run whole food, ultra-processed, and transition scenarios to quantify how processing level affects health outcomes independent of nutrient content.",
        "lever_R": "Students add gut microbiome, food marketing, or socioeconomic access to explore how systemic factors amplify or mitigate the effects of ultra-processing.",
        "slides_guide": slides("The Ultra-Processed Food Problem", "Modeling Food Chemistry and Metabolic Health",
            [("Processing Level",), ("Sugar/Additive Load",), ("Satiety Response",), ("Metabolic Health",), ("Caloric Overconsumption",)],
            "NIH study: same calories, same nutrients, but 500 MORE calories consumed from ultra-processed meals. Why?",
            [("Whole Foods",), ("Ultra-Processed",), ("Diet Transition",)],
            ["Ultra-processing overrides satiety signals", "Eating speed matters as much as content"],
            "Ultra-processed foods bypass your body's natural fullness systems.",
            "Design a School Lunch That Beats Ultra-Processing",
            "Design meals as satisfying as processed ones using whole foods within budget.",
            "District spends $1.50/student and wants to cut ultra-processing from 75% to 25%.",
            ["How can whole-food meals compete on cost?", "What does model predict about health?"],
            "Food scientists earn $60,000-$100,000/year."),
        "sort_reasoning": "Processing Level is external because it represents the manufacturing decisions made before food reaches the consumer — it's an input the eater encounters but doesn't control at the point of consumption. Sugar/Additive Load, Satiety Response, Metabolic Health, and Caloric Overconsumption are internal because they are physiological and behavioral responses that occur within the body after food is consumed.",
        "relationships": [
            ("Processing Level to Sugar and Additive Load", "POSITIVE (+)", "Higher processing adds more industrial ingredients — sugars, emulsifiers, flavors, and preservatives that don't exist in whole foods."),
            ("Sugar and Additive Load to Satiety Response", "NEGATIVE (-)", "Higher additive loads disrupt gut hormone signaling, accelerate eating speed, and reduce the body's ability to detect fullness."),
            ("Satiety Response to Caloric Overconsumption", "NEGATIVE (-)", "Weaker satiety signals mean the brain doesn't receive the 'stop eating' message, leading to consumption of 20-30% more calories."),
            ("Caloric Overconsumption to Metabolic Health", "NEGATIVE (-)", "Chronic excess calorie intake, especially from refined sources, drives insulin resistance, inflammation, and fat accumulation — the hallmarks of metabolic syndrome.")
        ],
        "sim_answers": [
            ("Whole Foods Scenario", "With minimal Processing Level, Sugar/Additive Load stays low, Satiety Response functions normally, and Caloric Overconsumption doesn't occur. Metabolic Health remains at baseline. The body's evolved regulation systems work correctly when given the types of food they evolved to handle — whole foods with intact fiber, complex structures, and natural nutrient ratios."),
            ("Ultra-Processed Scenario", "Maximum Processing Level drives Sugar/Additive Load high, which collapses Satiety Response. With weakened fullness signals, Caloric Overconsumption increases by approximately 500 calories per day. Over time, this chronic surplus degrades Metabolic Health through insulin resistance, chronic inflammation, and disrupted gut microbiome. The model reveals a self-reinforcing cycle: metabolic dysfunction further impairs satiety signaling, creating a feedback loop.")
        ],
        "reflection_exemplars": [
            ("Why isn't this just about calories?", "Our model shows that Processing Level affects health through mechanisms independent of calorie content. The NIH study controlled for calories, macros, sugar, fat, and fiber — yet ultra-processed meals still caused 500 more calories of intake. The processing itself alters Satiety Response by changing food texture (faster eating), absorption speed (blood sugar spikes), and gut hormone signaling (disrupted leptin and ghrelin). Two meals with identical nutrition panels can have completely different metabolic effects based on processing. This is why 'a calorie is a calorie' is scientifically misleading."),
            ("Is this a personal choice or a systemic issue?", "The model suggests it's both, but the system is rigged. Processing Level is marked as 'external' because individuals encounter it as a given — but it's determined by food companies, agricultural subsidies, and economic structures. When ultra-processed food is 3x cheaper than whole food, and marketing targets the youngest and poorest consumers, calling obesity a 'personal choice' ignores the system that shapes those choices. Our model shows that changing the input (Processing Level) at the systemic level would be far more effective than asking individuals to resist foods engineered to be irresistible.")
        ],
        "stem_intro": "Present the challenge: Your school district wants to reduce ultra-processed food in school lunches while maintaining cost, convenience, and student acceptance. Use your model data to design a week of menus that prove whole-food meals can compete.",
        "stem_concepts": [
            ("Food Matrix Effect", "The physical structure of food affects how nutrients are absorbed. Whole foods have intact cellular structures that slow digestion and absorption, while ultra-processing destroys these structures, causing rapid nutrient release that overwhelms metabolic regulation systems."),
            ("Bliss Point Engineering", "Food companies optimize the combination of sugar, salt, and fat to hit the 'bliss point' — the precise ratio that maximizes pleasure and consumption. This engineering creates foods that are supernormally stimulating, far beyond anything that exists in nature."),
            ("Food System Economics", "The US agricultural subsidy system primarily supports corn, soy, wheat, and dairy — the raw materials of ultra-processed food. Fruits and vegetables receive less than 1% of farm subsidies. This policy structure makes unhealthy ingredients artificially cheap.")
        ],
        "stem_eval": [
            ("Expert (4)", "Menu provides a complete week with NOVA classifications, per-meal cost analysis, nutritional adequacy, student appeal strategy, and model-based health outcome predictions"),
            ("Proficient (3)", "Menu includes several days with reasonable cost analysis and connection to processing science"),
            ("Developing (2)", "Menu attempts whole-food alternatives but lacks cost analysis or scientific justification"),
            ("Beginning (1)", "Menu is incomplete or doesn't demonstrate understanding of processing levels and health impacts")
        ],
        "support": [
            "Provide a visual NOVA classification chart with examples students recognize (brand name vs. whole food equivalents)",
            "Use a simplified pathway: Processing -> Speed of Eating -> Fullness Signal -> How Much You Eat -> Health",
            "Sentence frames: 'Ultra-processed foods disrupt satiety because ___, which causes ___, leading to ___'"
        ],
        "extensions": [
            "Design and conduct a mini-experiment: compare how long it takes to eat 500 calories of ultra-processed snacks versus 500 calories of whole foods and measure subjective fullness",
            "Research the food industry's response to ultra-processing research — how do companies frame the debate and what counter-arguments do they use?",
            "Investigate the NOVA classification of your own diet for one day and calculate the percentage of calories from each processing level"
        ],
        "cross_curr": [
            ("Math", "Calculate the cost per calorie of 10 common ultra-processed foods versus 10 whole-food equivalents. Graph the relationship between processing level and cost per calorie."),
            ("ELA", "Write an investigative journalism piece exploring why the cheapest foods in your school cafeteria are the most processed, connecting food science to economic policy"),
            ("Economics", "Analyze how US agricultural subsidies shape the relative prices of ultra-processed versus whole foods and propose a subsidy reform that would incentivize healthier food production")
        ],
        "misconceptions": [
            ("Processed food is fine as long as you watch calories", "The NIH study demonstrated that processing level affects health independently of calorie content. Participants given unlimited access to either diet consumed 500 more calories daily from ultra-processed food — the processing disrupted satiety signals that normally regulate intake. Calorie labels don't capture how processing changes the body's metabolic response to food.", "Compare two 300-calorie meals: a bowl of oatmeal with berries vs. a processed cereal bar. Ask: Will the body respond the same way to both? (No — the oatmeal will produce stronger satiety and slower blood sugar response despite similar calories.)"),
            ("If the FDA allows it, it must be safe", "FDA approval means a food additive is Generally Recognized as Safe (GRAS) in isolation, not that a diet dominated by ultra-processed foods is safe. Many additives are tested individually but consumed in combinations never studied. The health effects of ultra-processing emerge from the total dietary pattern, not from any single ingredient.", "Analogy: Each car on the road is individually tested for safety, but traffic jams and accidents emerge from the system of many cars interacting — you can't assess highway safety by testing one car."),
            ("Organic ultra-processed food is healthy", "Organic ultra-processed food (organic chips, organic soda, organic candy) is still ultra-processed. The NOVA classification is about the degree of industrial processing, not about whether ingredients are organic. An organic cookie can have the same metabolic impact as a conventional one — the processing is what matters, not the farming method.", "Show examples: Organic soda vs. conventional soda — same sugar content, same metabolic impact. An organic apple vs. organic apple fruit leather — very different processing levels despite both being 'organic.'")
        ],
    })

    # L05: Why Some People Get Addicted
    lessons.append({
        "id": "G12L1-L05",
        "title": "Why Some People Get Addicted and Others Don't",
        "subtitle": "Modeling Neurotransmitter Systems, Genetic Vulnerability, and Addiction Pathways",
        "ngss": "HS-LS1-2, HS-LS3-1",
        "ngss_desc": "Develop and use a model to illustrate the hierarchical organization of interacting systems that provide specific functions within multicellular organisms. Ask questions to clarify relationships about the role of DNA and chromosomes in coding the instructions for characteristic traits passed from parents to offspring.",
        "big_question": "Two people try the same substance — one walks away and never thinks about it again, while the other develops a devastating addiction. If the drug is the same, what's different about the people?",
        "objectives": [
            "Model how genetic predisposition, dopamine system sensitivity, substance exposure, and environmental stress interact to determine addiction vulnerability",
            "Explain why addiction is a brain disease involving hijacked reward circuitry, not a moral failure or lack of willpower",
            "Predict which combinations of risk factors create the highest addiction vulnerability",
            "Analyze why understanding addiction biology should change how society treats substance use disorders"
        ],
        "vocabulary": [
            ("Dopamine", "A neurotransmitter that signals reward and motivation in the brain's mesolimbic pathway — addictive substances flood the system with 2-10x more dopamine than natural rewards, gradually rewiring the brain to prioritize the substance above all else"),
            ("Genetic Predisposition", "Inherited variations in genes that affect dopamine receptor density, metabolism enzymes, and stress response — accounting for 40-60% of addiction vulnerability, not a destiny but a loaded dice"),
            ("Tolerance", "The brain's adaptation to repeated substance exposure by reducing dopamine receptor density — requiring increasing doses to achieve the same effect, a hallmark of addiction progression"),
            ("Neuroplasticity", "The brain's ability to physically rewire neural connections in response to experience — in addiction, this rewiring shifts motivation circuits from natural rewards to substance-seeking, creating powerful compulsions")
        ],
        "components": [
            ("Genetic Vulnerability", "Inherited variations in dopamine receptor genes (DRD2), metabolism enzymes (ALDH2, CYP2A6), and stress-response systems that create a biological baseline of addiction risk — varies significantly across individuals", True),
            ("Substance Exposure", "The type, amount, and age of first exposure to addictive substances — earlier exposure during brain development creates higher risk because adolescent reward circuits are still forming", True),
            ("Dopamine Surge", "The magnitude of dopamine release triggered by a substance — natural rewards produce 150-200% baseline, while drugs produce 200-1000%, overwhelming normal reward calibration", False),
            ("Receptor Downregulation", "The brain's response to repeated dopamine flooding — reducing receptor density to restore balance, but this makes natural rewards feel less satisfying and drives escalating use", False),
            ("Addiction Severity", "The degree to which substance-seeking behavior dominates decision-making — from casual use through dependence to compulsive use despite severe consequences", False)
        ],
        "think_about_it": "A person with high Genetic Vulnerability who experiences their first Substance Exposure at age 14 versus age 25 — what does your model predict about their relative Addiction Severity? Why does the age of exposure matter so much?",
        "scenarios": [
            ("Low Risk Profile", "Set Genetic Vulnerability to low with adult-age first exposure — observe moderate Dopamine Surge, minimal Receptor Downregulation, and low Addiction Severity"),
            ("High Risk Profile", "Set Genetic Vulnerability to high with adolescent exposure — observe amplified Dopamine Surge, rapid Receptor Downregulation, and escalating Addiction Severity"),
            ("Environmental Stress Amplifier", "Add chronic stress to a moderate risk profile — observe how stress hormones amplify Dopamine Surge response and accelerate Receptor Downregulation")
        ],
        "sim_scenarios": [
            ("Low Risk", "Genetic Vulnerability: Low | First Exposure: Age 25 | Stress: Low", "With low genetic risk and adult-age first exposure, what does the model predict about addiction progression?"),
            ("High Risk", "Genetic Vulnerability: High | First Exposure: Age 14 | Stress: Moderate", "How does high genetic vulnerability combined with adolescent exposure change the trajectory?"),
            ("Stress Amplification", "Genetic Vulnerability: Moderate | First Exposure: Age 17 | Stress: Chronic high", "How does chronic stress change addiction vulnerability for someone with moderate genetic risk?")
        ],
        "discoveries": [
            "Addiction vulnerability is primarily biological — genetic factors account for 40-60% of risk, and adolescent brain development creates a critical window of heightened vulnerability",
            "Addictive substances hijack the brain's reward system by producing dopamine surges far beyond what natural rewards can generate, physically rewiring motivation circuits",
            "Tolerance and receptor downregulation create a vicious cycle: the brain reduces sensitivity to cope with flooding, making normal pleasures feel flat and driving escalating use",
            "Environmental factors like chronic stress don't just add to biological risk — they multiply it by sensitizing the dopamine system and reducing the prefrontal cortex's ability to override compulsions"
        ],
        "answer": "The reason one person becomes addicted and another doesn't comes down to biology meeting environment. Genetic variations in dopamine receptors, metabolism enzymes, and stress response systems create dramatically different baseline vulnerabilities — some people's brains are wired to respond much more intensely to substances. When exposure occurs during adolescence (when the prefrontal cortex isn't fully developed), the risk multiplies further. Chronic stress amplifies vulnerability by sensitizing the reward system. Addiction isn't a choice or a character flaw — it's a brain disease where hijacked reward circuitry overrides rational decision-making. Understanding this biology is the key to compassionate, effective treatment.",
        "stem_title": "Design an Evidence-Based Prevention Program",
        "stem_mission": "Design a science-based addiction prevention program for high school students that uses neuroscience evidence rather than fear tactics, addressing both biological risk factors and environmental protective factors.",
        "stem_scenario": "Your school district is replacing its outdated 'Just Say No' program with an evidence-based approach. Research shows that fear-based programs are ineffective and can actually increase curiosity. The district wants a program that teaches students the neuroscience of addiction, helps them assess their own risk factors, and builds evidence-based protective skills.",
        "stem_questions": [
            "Why have fear-based prevention programs consistently failed, and what does neuroscience suggest instead?",
            "How can teaching the biology of addiction reduce stigma while also motivating prevention?",
            "What protective factors does your model identify that could be strengthened through a school program?"
        ],
        "stem_design_qs": [
            "What neuroscience concepts does your program teach and how are they presented to be engaging without being preachy?",
            "How does your program address genetic vulnerability without causing anxiety in students who may have family history?",
            "What specific protective skills does your program build and what evidence supports their effectiveness?",
            "How would you evaluate whether your program actually reduces substance use initiation?"
        ],
        "career": "Neuroscientists studying addiction research how drugs change brain structure and function, earning $70,000-$130,000/year. Addiction counselors help people recover using evidence-based therapies, earning $40,000-$65,000/year. Pharmacologists develop medications to treat addiction by targeting specific receptor systems, earning $80,000-$150,000/year.",
        "images": img("G12L1-L05",
            "A photorealistic image of a brain model with glowing neural pathways highlighted in the reward circuit, dopamine pathway illuminated in bright color against dark background, scientific and dramatic",
            "A diverse group of 17-18 year old students in a modern neuroscience classroom examining brain models and neural pathway diagrams, engaged in serious scientific discussion",
            "A diverse group of 17-18 year old students working on laptops building computational models of neurotransmitter systems, modern classroom with brain reward circuit posters and genetics diagrams",
            "A teacher leading discussion with diverse 17-18 year old students about addiction neuroscience, a dopamine pathway diagram and risk factor chart on smartboard, respectful and scientific tone",
            "Diverse 17-18 year old students designing prevention program materials on whiteboards with neuroscience diagrams, protective factor lists, and program evaluation metrics"
        ),
        "pre_assessment": [
            "Why do you think some people become addicted to substances while others who try the same thing don't?",
            "Do you think addiction is a choice, a disease, or something else? Explain your reasoning.",
            "What do you know about how drugs affect the brain? Be as specific as you can.",
            "What do you think is more effective for preventing addiction: scaring people or educating them? Why?"
        ],
        "extend_components": [
            ("Prefrontal Cortex Development", "The brain region responsible for impulse control and long-term planning — not fully mature until age 25, explaining why adolescent substance use carries higher addiction risk than adult use"),
            ("Social Environment", "Peer influence, family support, community connectedness, and access to substances — can either amplify or buffer biological vulnerability depending on quality"),
            ("Epigenetic Modification", "Changes in gene expression caused by environmental factors without altering DNA sequence — stress and substance exposure can activate or silence addiction-related genes, potentially across generations")
        ],
        "reflections": [
            "How does understanding the neuroscience of addiction change the way you think about people struggling with substance use disorders?",
            "Why does the age of first substance exposure matter so much according to your model?",
            "If genetic vulnerability accounts for 40-60% of addiction risk, what does that mean for prevention strategies?",
            "How should the criminal justice system treat addiction differently if it's a brain disease rather than a moral choice?",
            "What are the ethical implications of genetic testing for addiction vulnerability?"
        ],
        "dimensions": [
            ("Science Practice", "Developing and Using Models", "Students develop computational models to predict addiction vulnerability based on the interaction of genetic predisposition, substance exposure timing, dopamine system dynamics, and environmental stress."),
            ("Disciplinary Core Idea", "LS1.A Structure and Function / LS3.A Inheritance of Traits", "Neural systems that process reward are organized hierarchically, and genetic variations in these systems are inherited and contribute to differential addiction vulnerability."),
            ("Crosscutting Concept", "Cause and Effect", "Students identify causal chains from genetic vulnerability and substance exposure through dopamine surge and receptor downregulation to addiction severity, recognizing that multiple factors interact nonlinearly.")
        ],
        "cast_items": [
            "Model how genetic and environmental factors interact to determine addiction vulnerability",
            "Predict addiction risk profiles based on the combination of genetic vulnerability, age of exposure, and stress levels",
            "Explain why addiction involves physical changes to brain reward circuitry that override voluntary decision-making"
        ],
        "cast_questions": [
            ("Multiple Choice:", "Two individuals are exposed to the same addictive substance at the same age. Individual A has high genetic vulnerability and low stress. Individual B has low genetic vulnerability and high chronic stress. Which individual does the model predict will develop greater Addiction Severity, and what is the primary mechanism?"),
            ("Constructed Response:", "Using your model, explain why adolescent substance exposure carries higher addiction risk than adult exposure. Reference brain development, dopamine system sensitivity, and at least two other components.")
        ],
        "background_intro": "Addiction affects over 20 million Americans and kills more than 100,000 annually from overdoses alone. Despite decades of moral stigma and punitive approaches, addiction rates continue to rise. The neuroscience revolution of the past 30 years has fundamentally changed our understanding: addiction is a chronic brain disease involving the hijacking of natural reward circuits, not a failure of character or willpower.",
        "background_sections": [
            ("The Brain's Reward Circuit", "The mesolimbic dopamine pathway runs from the ventral tegmental area (VTA) to the nucleus accumbens, with connections to the prefrontal cortex. This circuit evolved to reinforce survival behaviors — eating, social bonding, reproduction — by producing pleasurable dopamine signals. Addictive substances hijack this system by triggering dopamine releases 2-10x larger than natural rewards. Cocaine blocks dopamine reuptake, opioids trigger release in the VTA, and nicotine activates receptors throughout the circuit. The brain cannot distinguish drug-induced pleasure from survival-critical reward."),
            ("Genetic Factors in Addiction", "Twin studies consistently show 40-60% heritability for addiction vulnerability. Specific genes have been identified: variations in DRD2 (dopamine receptor density), ALDH2 (alcohol metabolism), CYP2A6 (nicotine metabolism), and OPRM1 (opioid receptor sensitivity) all affect individual risk. Importantly, no single 'addiction gene' exists — vulnerability emerges from the interaction of hundreds of genetic variants with environmental factors. Having genetic risk doesn't guarantee addiction, and lacking it doesn't guarantee safety."),
            ("The Adolescent Brain and Vulnerability", "The prefrontal cortex — responsible for impulse control, risk assessment, and long-term planning — is the last brain region to fully develop, not completing myelination until approximately age 25. During adolescence, the reward system is fully active but the brake system is still under construction. This developmental imbalance explains why teens are more sensitive to substances' rewarding effects and less able to override compulsions. Substance exposure during this window can permanently alter brain development."),
            ("The Cycle of Tolerance and Dependence", "When repeatedly flooded with dopamine, the brain adapts through neuroplasticity: it reduces dopamine receptor density (downregulation) to restore homeostatic balance. This creates tolerance — needing more substance for the same effect. But downregulation also means natural rewards (food, friendships, achievements) produce less pleasure than before. The person now feels flat and unmotivated without the substance. This neurobiological trap — where the brain has physically adapted to require the substance for normal functioning — is the mechanism of dependence.")
        ],
        "lever_L": "Students identify genetic vulnerability, substance exposure, dopamine surge, receptor downregulation, and addiction severity as the key components of the addiction system.",
        "lever_E": "Students determine that genetics set baseline vulnerability, exposure triggers dopamine surges proportional to vulnerability, repeated surges cause receptor downregulation, and downregulation drives escalating use and addiction severity.",
        "lever_V": "Students build a computational model showing how biological predisposition and environmental exposure interact through dopamine system dynamics to produce the spectrum from casual use to severe addiction.",
        "lever_Ev": "Students run low-risk, high-risk, and stress-amplified scenarios to compare how different combinations of factors produce dramatically different outcomes from the same initial exposure.",
        "lever_R": "Students add prefrontal cortex development, social environment, or epigenetics to explore how additional biological and social factors modify addiction trajectories.",
        "slides_guide": slides("Why Some People Get Addicted", "Modeling Neurotransmitter Systems and Addiction",
            [("Genetic Vulnerability",), ("Substance Exposure",), ("Dopamine Surge",), ("Receptor Downregulation",), ("Addiction Severity",)],
            "Same drug, different people — why does one person walk away while another can't stop?",
            [("Low Risk",), ("High Risk",), ("Stress Amplifier",)],
            ["Genetics account for 40-60% of vulnerability", "Adolescent brains are uniquely susceptible"],
            "The difference is biology: genetics, brain development, and dopamine system dynamics.",
            "Design an Evidence-Based Prevention Program",
            "Design a neuroscience-based prevention program replacing 'Just Say No' with real science.",
            "District replacing outdated fear-based program with evidence-based approach.",
            ["Why do fear-based programs fail?", "What protective factors can be strengthened?"],
            "Neuroscientists studying addiction earn $70,000-$130,000/year."),
        "sort_reasoning": "Genetic Vulnerability and Substance Exposure are external because they represent pre-existing biological inheritance and environmental encounters that the brain's reward system must respond to. Dopamine Surge, Receptor Downregulation, and Addiction Severity are internal because they are neurobiological processes that emerge from how the brain's reward circuitry responds to the interaction of genetic programming and substance exposure.",
        "relationships": [
            ("Genetic Vulnerability to Dopamine Surge", "POSITIVE (+)", "Higher genetic vulnerability (more reward-sensitive dopamine systems) produces larger dopamine surges from substance exposure — the same drug produces a bigger hit in a genetically vulnerable brain."),
            ("Substance Exposure to Dopamine Surge", "POSITIVE (+)", "Greater exposure (higher dose, more frequent use, earlier age) produces larger and more frequent dopamine surges that overwhelm the brain's regulatory capacity."),
            ("Dopamine Surge to Receptor Downregulation", "POSITIVE (+)", "Repeated large dopamine surges trigger the brain's homeostatic response — reducing receptor density to cope with the flooding, which creates tolerance."),
            ("Receptor Downregulation to Addiction Severity", "POSITIVE (+)", "As receptors downregulate, natural rewards become less satisfying and more substance is needed for normal functioning, driving compulsive use and escalating addiction severity.")
        ],
        "sim_answers": [
            ("Low Risk Scenario", "With low Genetic Vulnerability, adult-age first exposure, and low stress, the model shows moderate Dopamine Surge, slow and limited Receptor Downregulation, and low Addiction Severity. The brain responds to the substance but doesn't develop the extreme sensitization and tolerance that drive addiction. This person can typically walk away from the experience."),
            ("High Risk Scenario", "With high Genetic Vulnerability and adolescent exposure, Dopamine Surge is dramatically amplified — the same substance produces a much more intense reward signal. This triggers rapid Receptor Downregulation, quickly creating tolerance and a need for escalating doses. Combined with an immature prefrontal cortex that can't override compulsions, Addiction Severity escalates rapidly. The model shows how biology meets brain development to create maximum vulnerability.")
        ],
        "reflection_exemplars": [
            ("Is addiction a choice?", "Our model shows that the initial decision to try a substance involves choice, but addiction itself is a brain disease that progressively destroys the capacity for choice. As Receptor Downregulation advances, the prefrontal cortex — the seat of decision-making — becomes less able to override the reward circuit's demands. It's like choosing to walk into quicksand: the first step is voluntary, but once you're sinking, willpower alone can't pull you out. The model demonstrates that once neuroplasticity has physically rewired motivation circuits, the brain is literally a different organ than it was before exposure."),
            ("Should this change how we treat addiction?", "Absolutely. If addiction is a brain disease driven by genetics, brain development, and neuroplasticity rather than moral failure, then punishment is the wrong response — just as you wouldn't jail someone for having diabetes. The model shows that effective intervention must target the biological mechanisms: medications that normalize dopamine signaling, therapies that strengthen prefrontal cortex function, and environmental changes that reduce stress amplification. The evidence overwhelmingly supports medical treatment over incarceration, yet the US still criminalizes addiction. This is a policy informed by stigma, not science.")
        ],
        "stem_intro": "Present the challenge: Your school district is replacing its outdated drug prevention program with an evidence-based approach. The new program must teach addiction neuroscience, help students understand risk factors without causing panic, and build genuine protective skills backed by research.",
        "stem_concepts": [
            ("Harm Reduction", "A public health approach that aims to minimize the negative health consequences of substance use rather than demanding abstinence as the only acceptable outcome. Strategies include naloxone distribution, safe consumption sites, and needle exchange programs — all of which have strong evidence for reducing deaths."),
            ("Protective Factors", "Evidence-based factors that reduce addiction risk: strong family bonds, school engagement, positive peer groups, stress management skills, and delayed age of first use. Each of these can be strengthened through targeted programs."),
            ("Motivational Interviewing", "A counseling technique that helps people explore and resolve ambivalence about behavior change without judgment or confrontation. Research shows it's significantly more effective than lectures, fear tactics, or confrontational interventions.")
        ],
        "stem_eval": [
            ("Expert (4)", "Program teaches accurate neuroscience accessibly, addresses genetic risk sensitively, builds specific evidence-based protective skills, and includes measurable outcome evaluation"),
            ("Proficient (3)", "Program includes neuroscience education and some protective skill-building with general evaluation plan"),
            ("Developing (2)", "Program has some science content but relies partly on fear-based messaging or lacks evaluation"),
            ("Beginning (1)", "Program is incomplete, scientifically inaccurate, or primarily fear-based")
        ],
        "support": [
            "Provide a simplified diagram of the dopamine reward pathway with labeled components",
            "Use a risk factor spectrum visual: Low Risk <---> High Risk, with genetic and environmental factors positioned along it",
            "Sentence frames: 'When ___ is high and ___ is also high, the model predicts ___ because ___'"
        ],
        "extensions": [
            "Research how pharmaceutical companies contributed to the opioid crisis by marketing addictive painkillers as non-addictive — what does the neuroscience model reveal about these claims?",
            "Investigate the neuroscience of behavioral addictions (gaming, social media, gambling) — do they hijack the same dopamine pathways as substance addiction?",
            "Analyze the effectiveness of Portugal's 2001 drug decriminalization policy using addiction neuroscience — why did treating addiction as a health issue reduce drug deaths by 80%?"
        ],
        "cross_curr": [
            ("Math", "Graph dopamine release levels for natural rewards (100-200% baseline) versus various substances (cocaine: 400%, methamphetamine: 1000%). Calculate the fold-difference and explain why receptor downregulation is inevitable at those levels."),
            ("ELA", "Write a narrative piece from the perspective of the brain's reward circuit during the progression from first exposure to full addiction, using accurate neuroscience but accessible storytelling"),
            ("Social Studies", "Research the history of drug policy in the US from the War on Drugs to current reform movements. How has the science of addiction been used — or ignored — in shaping policy?")
        ],
        "misconceptions": [
            ("Addiction is a moral failing or lack of willpower", "Addiction involves physical changes to brain structure and function — dopamine receptor density decreases, prefrontal cortex activity diminishes, and motivation circuits are rewired. These are measurable neurological changes visible on brain scans, not character flaws. Asking an addicted person to 'just stop' is like asking someone with a broken leg to 'just walk.' The brain is the organ of decision-making, and addiction damages this organ.", "Show fMRI images comparing reward circuit activation in healthy brains vs. brains with addiction — the physical differences are unmistakable."),
            ("Addiction only affects people who use hard drugs", "Addiction can develop from any substance that hijacks the dopamine reward system, including alcohol, nicotine, prescription painkillers, and caffeine. Alcohol addiction affects 14.5 million Americans — more than all illegal drugs combined. Nicotine is one of the most addictive substances known, with 60% of people who try a cigarette becoming daily smokers.", "Ask: What's more addictive — heroin or nicotine? (Research shows nicotine produces dependence in a higher percentage of users, though heroin's consequences are more immediately severe.)"),
            ("If it's genetic, there's nothing you can do about it", "Genetic vulnerability is not destiny — it's risk probability. Having addiction-related gene variants means your dopamine system is more sensitive, but environmental factors are equally important. The model shows that even high genetic vulnerability requires substance exposure to activate. Delaying first exposure past age 25, reducing chronic stress, building social connections, and understanding your own risk profile all significantly reduce the likelihood of addiction developing.", "Analogy: Having a genetic predisposition to addiction is like having dry kindling — it increases fire risk, but without a spark (exposure), there's no fire. And with fire prevention measures (protective factors), even dry kindling can be safe.")
        ],
    })

    # L06: Your Carbon Shadow
    lessons.append({
        "id": "G12L1-L06", "title": "Your Carbon Shadow", "subtitle": "Modeling Personal Carbon Footprints, Energy Sources, and Climate Impact",
        "ngss": "HS-ESS3-4, HS-PS3-3", "ngss_desc": "Evaluate or refine a technological solution that reduces impacts of human activities on natural systems. Design, build, and refine a device that works within given constraints to convert one form of energy into another form of energy.",
        "big_question": "Every time you charge your phone, eat a burger, or ride in a car, you leave an invisible trail of carbon emissions — how big is YOUR carbon shadow, and which of your daily choices actually matter the most?",
        "objectives": ["Model how transportation, diet, housing energy, and consumer purchases contribute to an individual's total carbon footprint", "Explain why some daily choices produce 10-100x more emissions than others", "Predict how specific lifestyle changes would reduce personal carbon emissions and rank them by impact", "Analyze why individual action alone cannot solve climate change without systemic policy changes"],
        "vocabulary": [("Carbon Footprint", "The total greenhouse gas emissions caused directly and indirectly by an individual, measured in tons of CO2 equivalent per year — the average American produces about 16 tons, compared to a global average of 4 tons"), ("Lifecycle Emissions", "The total carbon emitted across a product's entire life — from raw material extraction through manufacturing, transportation, use, and disposal — often revealing hidden emissions consumers don't see"), ("Carbon Intensity", "The amount of CO2 emitted per unit of energy produced — varies dramatically by source: coal emits ~1000g CO2/kWh, natural gas ~450g, solar ~40g, wind ~10g"), ("Rebound Effect", "When efficiency improvements lead to increased consumption that partially or fully offsets the savings — for example, buying a fuel-efficient car but driving more because it's cheaper per mile")],
        "components": [("Transportation Mode", "How a person travels — driving alone produces ~404g CO2/mile, public transit ~89g/mile, cycling ~0g — transportation is typically the largest single source of personal emissions", True), ("Diet Type", "The carbon intensity of food choices — beef produces 27kg CO2 per kg of food, chicken 6.9kg, vegetables 2kg — diet accounts for 10-30% of a person's carbon footprint depending on meat consumption", True), ("Housing Energy Source", "The fuel mix powering a home — coal-heavy grids produce 5-10x more emissions per kWh than renewable grids, making location one of the biggest determinants of housing carbon impact", True), ("Annual CO2 Output", "The total greenhouse gas emissions produced by an individual's lifestyle choices in one year, measured in metric tons of CO2 equivalent", False), ("Climate Impact Score", "A normalized measure of how an individual's emissions compare to sustainable levels — scientists estimate 2.5 tons CO2/year per person is the maximum for limiting warming to 1.5C", False)],
        "think_about_it": "The average American produces 16 tons of CO2 per year. The sustainable target is 2.5 tons. If you changed Transportation Mode to cycling, Diet Type to plant-based, and Housing Energy to 100% renewable — would you hit the target? What's still missing?",
        "scenarios": [("Average American", "Set all inputs to US average values — observe total Annual CO2 Output and how it compares to the 2.5-ton target"), ("Maximum Reduction", "Set Transportation to cycling/transit, Diet to plant-based, Housing to renewable — observe how much individual choices can reduce emissions"), ("Systemic vs Individual", "Compare: one person going zero-carbon vs. policy that reduces everyone's transportation emissions by 30%")],
        "sim_scenarios": [("US Average", "Transport: Car commute | Diet: Standard American | Energy: National grid average", "How far above the sustainable 2.5-ton target is the average American lifestyle?"), ("Personal Maximum", "Transport: Bike/transit | Diet: Plant-based | Energy: 100% renewable", "If you maximize every personal choice, can you reach the 2.5-ton sustainable target?"), ("Policy Comparison", "One person at zero vs. 10% reduction for 1 million people", "Which produces a larger total emission reduction — one person's heroic effort or a small policy change affecting millions?")],
        "discoveries": ["Transportation and diet are the two largest personal emission sources — together they typically account for 60-70% of an individual carbon footprint", "The gap between the average American footprint (16 tons) and the sustainable target (2.5 tons) is so large that individual behavior changes alone cannot close it without systemic changes to energy infrastructure", "Where you live matters enormously — the same lifestyle in a coal-powered state produces 2-3x more emissions than in a renewable-energy state, highlighting the importance of grid decarbonization", "The rebound effect means efficiency gains are often partially consumed by increased usage — making systemic policy changes more reliable than voluntary behavior change for achieving emission targets"],
        "answer": "Your carbon shadow is larger than you think — the average American produces 16 tons of CO2 annually, over 6x the sustainable target. Transportation (driving) and diet (meat) are the biggest personal levers, but even maximizing every individual choice can only reduce emissions by about 50-60%. The remaining gap requires systemic changes: decarbonizing the electrical grid, redesigning cities for transit, and transforming industrial agriculture. Individual action matters for building political will and normalizing sustainable behavior, but the math is clear — personal virtue alone cannot solve a systemic problem.",
        "stem_title": "Design a Carbon Reduction Plan for Your School",
        "stem_mission": "Conduct a carbon audit of your school and design a reduction plan that achieves a 50% emission cut within 5 years using both behavioral and infrastructure changes.",
        "stem_scenario": "Your school emits an estimated 500 tons of CO2 annually from building energy, student/staff transportation, food service, and waste. The principal wants a science-based plan to cut emissions by 50% in 5 years. Your team must identify the largest sources, propose specific interventions, calculate expected reductions, and present a cost-benefit analysis.",
        "stem_questions": ["What are your school's three largest sources of carbon emissions?", "Which interventions offer the biggest reduction per dollar invested?", "How do you balance infrastructure changes (expensive but lasting) with behavior changes (cheap but unreliable)?"],
        "stem_design_qs": ["What specific emission sources did your audit identify and what is each source's contribution?", "What interventions does your plan propose and what is the projected CO2 reduction for each?", "What is the total cost of your plan and what is the cost per ton of CO2 avoided?", "How would you verify that your plan is actually achieving its emission reduction targets?"],
        "career": "Climate scientists model global carbon cycles and project future warming scenarios, earning $70,000-$120,000/year. Sustainability consultants help organizations reduce their carbon footprints, earning $60,000-$110,000/year. Energy policy analysts design carbon reduction regulations, earning $65,000-$100,000/year.",
        "images": img("G12L1-L06", "A photorealistic aerial view of a city with visible carbon emission sources highlighted — car exhaust, industrial smokestacks, building HVAC — dramatic environmental photography style", "A diverse group of 17-18 year old students in a modern environmental science classroom using carbon footprint calculators on laptops, globe and climate data posters visible", "A diverse group of 17-18 year old students building computational models of carbon emissions on laptops, modern classroom with energy source comparison charts and CO2 graphs", "A teacher leading discussion with diverse 17-18 year old students about carbon footprints, a pie chart of emission sources on smartboard, students analyzing their own data", "Diverse 17-18 year old students designing school carbon reduction plans on whiteboards with energy audits, intervention timelines, and cost-benefit tables"),
        "pre_assessment": ["What activities in your daily life do you think produce the most carbon emissions?", "How many tons of CO2 do you think the average American produces per year? Take your best guess.", "Do you think individual actions like recycling can significantly reduce climate change? Why or why not?", "What's the difference between using less energy and using cleaner energy?"],
        "extend_components": [("Consumption Emissions", "The carbon embedded in products purchased — a new smartphone has approximately 70kg of lifecycle CO2, a pair of jeans ~33kg — consumer purchasing is a major hidden emission source"), ("Policy Environment", "Government regulations affecting emissions — carbon taxes, fuel economy standards, renewable energy mandates — that shape the carbon intensity of choices available to individuals"), ("Carbon Offset Quality", "The effectiveness of purchased carbon offsets — ranging from high-quality reforestation to questionable credits that don't actually remove carbon — a controversial tool for emission reduction")],
        "reflections": ["Why can't individual behavior changes alone close the gap between 16 tons and 2.5 tons per person?", "How does the rebound effect undermine efficiency-based approaches to emission reduction?", "Is it fair to focus on individual carbon footprints when 100 companies produce 71% of global emissions?", "What does your model suggest about the relative importance of personal action versus systemic policy change?", "How should we think about carbon equity — should everyone have the same emission budget regardless of where they live?"],
        "dimensions": [("Science Practice", "Developing and Using Models", "Students develop computational models to quantify how transportation, diet, and energy choices contribute to personal carbon emissions and compare individual versus systemic reduction strategies."), ("Disciplinary Core Idea", "ESS3.C Human Impacts on Earth Systems / PS3.D Energy in Chemical Processes", "Human activities release greenhouse gases through combustion and industrial processes. Different energy conversion pathways have dramatically different carbon intensities."), ("Crosscutting Concept", "Scale, Proportion, and Quantity", "Students use quantitative analysis to compare the scale of individual emission reductions versus systemic policy changes, recognizing that proportion matters when evaluating solutions.")],
        "cast_items": ["Model how personal choices in transportation, diet, and energy contribute to total carbon footprint", "Predict emission reductions from specific lifestyle changes and rank interventions by impact", "Evaluate the relative effectiveness of individual behavior change versus systemic policy intervention"],
        "cast_questions": [("Multiple Choice:", "A student switches from driving to cycling (saving 3 tons CO2/year) and adopts a plant-based diet (saving 1.5 tons/year). Their footprint drops from 16 to 11.5 tons. What does the model suggest is needed to reach the 2.5-ton sustainable target?"), ("Constructed Response:", "Using your model, explain why a carbon tax that reduces everyone's transportation emissions by 20% produces more total emission reduction than even 1 million individuals voluntarily going car-free.")],
        "background_intro": "The concept of a personal carbon footprint was actually popularized by BP (British Petroleum) in a 2004 ad campaign designed to shift climate responsibility from fossil fuel companies to individual consumers. Despite this cynical origin, understanding your carbon footprint is genuinely useful — not because individual action alone can solve climate change, but because it reveals which systemic changes would have the biggest impact.",
        "background_sections": [("Measuring Carbon Footprints", "A carbon footprint measures total greenhouse gas emissions in CO2 equivalents (CO2e), which accounts for the different warming potentials of gases like methane (28x CO2) and nitrous oxide (265x CO2). The average American produces about 16 tons CO2e/year — roughly 4x the global average and 6x the level scientists say is sustainable for limiting warming to 1.5°C."), ("The Big Three: Transport, Food, Housing", "For most Americans, three categories dominate: transportation (~29% of US emissions), food (~10-30% individual), and housing energy (~20%). Within these, specific choices vary enormously: driving alone vs. transit is a 4x difference; beef vs. plants is a 10-20x difference; coal electricity vs. renewable is a 50-100x difference per kWh."), ("The Rebound Effect", "When people save money through efficiency, they often spend the savings on other carbon-intensive activities. A person who buys a fuel-efficient car may drive more because fuel costs less per mile. A person who saves money on LED lighting may spend the savings on a flight. This rebound effect can offset 10-30% of efficiency gains and is a key reason why purely voluntary measures underperform policy mandates."), ("Individual Action vs. Systemic Change", "Analysis by Project Drawdown shows that the highest-impact climate solutions are systemic: reducing food waste, shifting to plant-rich diets at scale, deploying renewable energy, and improving building efficiency — all requiring policy support. The 'personal responsibility' framing, while motivating, obscures the reality that 71% of global emissions come from just 100 companies. Individual action builds political will; policy action changes the system.")],
        "lever_L": "Students identify transportation mode, diet type, housing energy source, annual CO2 output, and climate impact score as the key components of the personal carbon system.",
        "lever_E": "Students determine that each lifestyle choice contributes to total emissions, that some choices have 10-100x more impact than others, and that the gap between actual and sustainable emissions reveals the need for systemic change.",
        "lever_V": "Students build a computational model quantifying how daily choices aggregate into annual emissions and compare personal maximum reduction to sustainable targets.",
        "lever_Ev": "Students run average American, maximum reduction, and policy comparison scenarios to discover that individual optimization alone cannot reach sustainable emission levels.",
        "lever_R": "Students add consumption emissions, policy environment, or carbon offsets to explore how the full scope of personal and systemic factors determines climate impact.",
        "slides_guide": slides("Your Carbon Shadow", "Modeling Personal Carbon Footprints", [("Transportation Mode",), ("Diet Type",), ("Housing Energy Source",), ("Annual CO2 Output",), ("Climate Impact Score",)], "Average American: 16 tons. Sustainable target: 2.5 tons. Can you close that gap with personal choices alone?", [("Average American",), ("Maximum Reduction",), ("Systemic vs Individual",)], ["Transport and diet account for 60-70% of personal emissions", "Individual action alone cannot close the gap to 2.5 tons"], "Your shadow is bigger than you think — and closing the gap requires both personal and systemic change.", "Design a Carbon Reduction Plan for Your School", "Conduct a carbon audit and design a 50% reduction plan.", "School emits 500 tons/year. Principal wants 50% cut in 5 years.", ["What are the biggest emission sources?", "Which interventions give best ROI?"], "Climate scientists earn $70,000-$120,000/year."),
        "sort_reasoning": "Transportation Mode, Diet Type, and Housing Energy Source are external because they represent lifestyle choices and infrastructure conditions that exist as inputs to the carbon calculation. Annual CO2 Output and Climate Impact Score are internal because they are calculated outcomes of how these inputs combine.",
        "relationships": [("Transportation Mode to Annual CO2 Output", "POSITIVE (+)", "Higher-emission transportation (solo driving) directly increases annual CO2. This is typically the largest single personal emission source."), ("Diet Type to Annual CO2 Output", "POSITIVE (+)", "More carbon-intensive diets (high meat consumption) increase annual emissions. Beef produces 10-20x more CO2 per calorie than plant foods."), ("Housing Energy Source to Annual CO2 Output", "POSITIVE (+)", "Carbon-intensive energy sources (coal, natural gas) increase household emissions. The same electricity use can produce 50-100x more CO2 on a coal grid vs. renewable."), ("Annual CO2 Output to Climate Impact Score", "POSITIVE (+)", "Higher annual emissions push further from the 2.5-ton sustainable target, increasing climate impact. The relationship is proportional but the scale reveals how far most Americans are from sustainability.")],
        "sim_answers": [("Average American Scenario", "With typical US driving, standard American diet, and national grid average electricity, Annual CO2 Output reaches approximately 16 tons — over 6x the 2.5-ton sustainable target. Transportation contributes the largest share (~5-6 tons), followed by housing energy (~3-4 tons) and food (~2-3 tons), with remaining emissions from goods and services."), ("Maximum Reduction Scenario", "Switching to cycling/transit, plant-based diet, and 100% renewable energy reduces Annual CO2 to approximately 6-8 tons — a dramatic 50-60% reduction. However, this still exceeds the 2.5-ton target because embedded emissions in products, services, infrastructure, and government spending contribute carbon that individuals cannot eliminate through personal choices alone.")],
        "reflection_exemplars": [("Can personal action solve climate change?", "Our model shows that maximizing every personal choice — cycling everywhere, eating plant-based, using 100% renewable energy — reduces emissions from 16 to about 6-8 tons, still 2-3x above the sustainable target. The remaining gap is embedded in systems individuals don't control: industrial supply chains, government operations, infrastructure construction. Personal action matters for two reasons: it reduces your contribution AND it builds political will for systemic change. But the math is clear — personal virtue without policy is necessary but insufficient."), ("Why does the rebound effect matter?", "The rebound effect reveals a fundamental limitation of efficiency-based approaches. When a family saves $1,000/year from a fuel-efficient car, they typically spend that money on other carbon-intensive activities — a vacation flight, more online shopping, eating out more. The model shows that only about 70-90% of expected savings actually materialize after rebound is accounted for. This is why economists favor carbon pricing over voluntary efficiency — a carbon tax makes ALL carbon-intensive activities more expensive, eliminating the rebound.")],
        "stem_intro": "Present the challenge: Your school principal wants a science-based plan to cut the school's carbon emissions by 50% in 5 years. Your team must audit current emissions, identify high-impact interventions, and present a costed plan with projected outcomes.",
        "stem_concepts": [("Carbon Auditing", "Systematic measurement of all emission sources within a defined boundary. For a school, this includes building energy (electricity and heating), transportation (buses, student/staff cars), food service, waste, and procurement. Each source is converted to CO2e using standard emission factors."), ("Marginal Abatement Cost", "The cost of reducing one additional ton of CO2 emissions. Some interventions (LED lighting, thermostat optimization) have negative marginal cost — they save money while reducing emissions. Others (solar panels, EV buses) have positive costs but long-term paybacks."), ("Scope 1, 2, and 3 Emissions", "Scope 1: direct emissions from sources you own (school buses, boilers). Scope 2: indirect emissions from purchased electricity. Scope 3: all other indirect emissions (student commuting, food supply chains, purchased goods). Most organizations only measure Scopes 1-2; Scope 3 often represents 70%+ of total emissions.")],
        "stem_eval": [("Expert (4)", "Plan includes comprehensive audit, prioritized interventions with cost-per-ton analysis, timeline, and monitoring strategy, with model evidence supporting projected reductions"), ("Proficient (3)", "Plan identifies major sources and proposes reasonable interventions with some cost analysis"), ("Developing (2)", "Plan identifies some emission sources but interventions lack quantification or cost analysis"), ("Beginning (1)", "Plan is incomplete or not connected to emission data and carbon science")],
        "support": ["Provide a reference chart showing CO2 emissions per activity (driving per mile, electricity per kWh, food per kg)", "Use a simple pie chart template for students to fill in their own emission breakdown", "Sentence frames: 'Switching from ___ to ___ would reduce my emissions by approximately ___ tons because ___'"],
        "extensions": ["Calculate the carbon footprint of your family's last vacation including flights, hotels, food, and activities — then research how much it would cost to offset those emissions and whether the offsets are credible", "Research carbon capture and storage (CCS) technology — is it a viable alternative to emission reduction or a dangerous distraction?", "Compare the carbon footprints of 10 countries and analyze how GDP, energy mix, and lifestyle differences explain the variation"],
        "cross_curr": [("Math", "Calculate the total US emission reduction if 50% of Americans switched from driving to public transit for their commute. Compare this to the reduction from one coal plant closing. Which is larger?"), ("ELA", "Analyze BP's 2004 carbon footprint campaign and write a rhetorical analysis of how corporations use individual responsibility framing to deflect systemic criticism"), ("Economics", "Research carbon pricing mechanisms (carbon tax vs. cap-and-trade) and model how a $50/ton carbon price would change the relative costs of different energy sources and transportation modes")],
        "misconceptions": [("Recycling is one of the most important things I can do for climate", "While recycling is good practice, its carbon impact is tiny compared to transportation, diet, and energy choices. Recycling all your household waste saves approximately 0.2 tons CO2/year. Switching from car to transit saves ~2.5 tons. Going plant-based saves ~1.5 tons. Recycling is visible and feels good, but the model shows it ranks near the bottom of carbon-reduction strategies.", "Rank activities by CO2 impact: students are usually surprised that recycling saves less than 2% of what driving changes save."), ("Electric cars are zero-emission", "Electric vehicles produce zero tailpipe emissions but are not zero-emission. Their carbon footprint depends entirely on the electricity source. An EV charged from a coal-heavy grid may produce nearly as much lifecycle CO2 as an efficient gas car. On a renewable grid, EVs produce 70-90% less CO2 than gas cars. The car itself also embodies significant manufacturing emissions, especially the battery.", "Calculate: An EV using 30 kWh/100 miles on a coal grid (1000g CO2/kWh) vs. a renewable grid (40g CO2/kWh). The difference is 25x — same car, different grid."), ("My individual actions don't matter because I'm just one person", "This framing creates a collective action paradox: if everyone thinks their individual actions don't matter, nobody acts and nothing changes. The model shows that individual action has two effects: direct emission reduction (small per person but significant in aggregate) and political signaling (demonstrating demand for sustainable options). The 71% statistic about 100 companies is misleading — those companies produce fossil fuels that individuals and businesses consume. Supply and demand are connected.", "Counter-question: If everyone stopped buying gasoline tomorrow, would those 100 companies still produce 71% of emissions? Individual action shapes the system that produces emissions.")],
    })

    # L07: Electric vs. Gas: The Full Lifecycle
    lessons.append({
        "id": "G12L1-L07", "title": "Electric vs. Gas: The Full Lifecycle", "subtitle": "Modeling Energy Conversion, Lifecycle Emissions, and Transportation Trade-offs",
        "ngss": "HS-PS3-3, HS-ETS1-3", "ngss_desc": "Design, build, and refine a device that works within given constraints to convert one form of energy into another form of energy. Evaluate a solution to a complex real-world problem based on prioritized criteria and trade-offs.",
        "big_question": "Everyone says electric cars will save the planet — but when you count the mining, manufacturing, charging, and disposal, are they really cleaner than gas cars, and does the answer depend on where you live?",
        "objectives": ["Model how manufacturing emissions, energy source for charging, driving efficiency, and battery lifecycle interact to determine total vehicle carbon footprint", "Explain why the same electric car can be clean or dirty depending on the electrical grid it charges from", "Predict the break-even point where an EV's total lifecycle emissions become lower than a gas car's", "Analyze why lifecycle thinking reveals trade-offs that simple 'zero emissions' labels hide"],
        "vocabulary": [("Lifecycle Assessment", "A comprehensive analysis of environmental impacts across a product's entire life — from raw material extraction through manufacturing, use, and end-of-life disposal — revealing hidden costs that point-of-use measurements miss"), ("Grid Carbon Intensity", "The CO2 emitted per kilowatt-hour of electricity from a regional power grid — ranges from ~900g CO2/kWh for coal-dominant grids to ~20g for nearly all-renewable grids, determining whether charging an EV is clean or dirty"), ("Embodied Carbon", "The total CO2 emitted during manufacturing before a product is ever used — an EV battery embodies 8-16 tons of CO2 from mining, refining, and manufacturing, creating a 'carbon debt' that must be repaid through cleaner driving"), ("Well-to-Wheel Efficiency", "The total energy efficiency from original energy source to wheels on the road — EVs convert 77-82% of electrical energy to motion vs. gas cars converting only 12-30% of fuel energy, but the comparison depends on how the electricity was generated")],
        "components": [("Manufacturing Carbon Debt", "The embodied CO2 from vehicle production — EV manufacturing produces 30-50% more emissions than gas car manufacturing due to battery production, creating an initial carbon deficit that EVs must overcome through cleaner operation", True), ("Grid Carbon Intensity", "The CO2 per kWh of the electricity used to charge the EV — the single most important variable determining whether an EV is cleaner than a gas car over its lifetime", True), ("Driving Efficiency", "How effectively the vehicle converts stored energy to motion — EVs are 3-4x more efficient than gas engines, meaning even with some carbon in the grid, they often produce fewer emissions per mile", False), ("Cumulative Operating Emissions", "Total CO2 emitted during the vehicle's operational life from fuel or electricity — accumulates with every mile driven and determines when the EV overcomes its manufacturing carbon debt", False), ("Total Lifecycle Emissions", "The sum of manufacturing, operating, and end-of-life emissions over the vehicle's complete life — the only honest comparison between EVs and gas cars", False)],
        "think_about_it": "An EV starts life with a bigger Manufacturing Carbon Debt than a gas car. But its Driving Efficiency is 3-4x better. How many miles does it take before the EV's total Lifecycle Emissions drop below the gas car's? Does Grid Carbon Intensity change this answer?",
        "scenarios": [("Clean Grid EV", "Set Grid Carbon Intensity to renewable-dominant (~50g/kWh) — observe how quickly the EV overcomes its manufacturing debt and its total lifecycle advantage"), ("Coal Grid EV", "Set Grid Carbon Intensity to coal-dominant (~800g/kWh) — observe how the carbon advantage shrinks and the break-even point extends dramatically"), ("Gas Car Baseline", "Run a modern efficient gas car for comparison — observe how its lower manufacturing emissions but higher operating emissions create a different trajectory")],
        "sim_scenarios": [("Clean Grid", "EV on renewable grid (50g CO2/kWh) vs. gas car (25 mpg)", "On a clean grid, how quickly does the EV overcome its manufacturing carbon debt?"), ("Dirty Grid", "EV on coal grid (800g CO2/kWh) vs. gas car (25 mpg)", "On a coal-heavy grid, does the EV still win on lifecycle emissions? At what mileage?"), ("Grid Transition", "EV starting on 600g grid that drops to 200g over 10 years", "How does a cleaning grid change the EV's lifecycle advantage over time?")],
        "discoveries": ["EVs start with a larger manufacturing carbon debt (30-50% more) but overcome it through vastly superior driving efficiency — the crossover typically occurs at 15,000-40,000 miles depending on the grid", "Grid carbon intensity is THE determining variable — the same EV can produce 70% fewer lifecycle emissions on a clean grid or nearly match a gas car on a coal grid", "Over a 150,000-mile lifetime, an EV on a clean grid produces about 50-70% fewer total lifecycle emissions than a comparable gas car, even accounting for battery manufacturing", "The grid is getting cleaner every year, which means EVs purchased today will become even cleaner over their lifetime as the grid decarbonizes — a benefit gas cars can never achieve"],
        "answer": "Electric cars are cleaner than gas cars in almost every scenario, but HOW much cleaner depends enormously on where you charge them. An EV on a clean grid produces 50-70% fewer lifecycle emissions than a gas car. An EV on a coal-heavy grid may only be 10-20% cleaner. The key insight is that EVs start with a manufacturing carbon debt from battery production but overcome it through 3-4x better driving efficiency. The break-even point ranges from 15,000 miles (clean grid) to 80,000+ miles (dirty grid). And here's the crucial point: the grid is getting cleaner every year, so every EV on the road today will become cleaner over its lifetime. Gas cars are locked into fossil fuel forever.",
        "stem_title": "Design the Optimal Vehicle Fleet for Your City",
        "stem_mission": "Using lifecycle analysis, design an optimal vehicle fleet transition plan for your city's 500 government vehicles, maximizing emission reduction within a 10-year budget.",
        "stem_scenario": "Your city government operates 500 vehicles (sedans, trucks, buses) and wants to transition to the lowest-emission fleet possible over 10 years. EVs cost more upfront but save on fuel and maintenance. The city's grid is currently 60% gas / 30% renewable / 10% coal, projected to reach 70% renewable by 2035.",
        "stem_questions": ["Which vehicle types should be replaced first for maximum emission reduction?", "How does the grid's projected decarbonization affect the lifecycle comparison over 10 years?", "What's the optimal replacement schedule that maximizes emission savings within budget constraints?"],
        "stem_design_qs": ["What is your fleet composition recommendation and what lifecycle analysis supports each choice?", "How does your plan account for the grid getting cleaner during the fleet transition period?", "What is the total projected emission reduction and cost over 10 years compared to keeping the gas fleet?", "What data would you monitor to verify your plan is achieving projected benefits?"],
        "career": "Automotive engineers design vehicle powertrains and optimize energy efficiency, earning $70,000-$120,000/year. Lifecycle assessment analysts evaluate the environmental impact of products from cradle to grave, earning $60,000-$100,000/year. Clean transportation policy analysts design vehicle emission standards and incentive programs, earning $65,000-$105,000/year.",
        "images": img("G12L1-L07", "A photorealistic split image of an electric car charging station on one side and a gas station on the other, both modern and sleek, environmental comparison aesthetic", "A diverse group of 17-18 year old students in a modern physics lab examining electric motor and internal combustion engine models side by side, measurement tools visible", "A diverse group of 17-18 year old students building lifecycle assessment models on laptops, modern classroom with energy conversion diagrams and emission comparison charts", "A teacher leading discussion with diverse 17-18 year old students about vehicle emissions, a lifecycle comparison graph on smartboard showing manufacturing vs operating emissions", "Diverse 17-18 year old students designing fleet transition plans on whiteboards with vehicle replacement timelines, cost tables, and emission reduction projections"),
        "pre_assessment": ["Do you think electric cars are better for the environment than gas cars? Why or why not?", "What do you think happens before an electric car reaches the dealership — what's the environmental cost of making it?", "If you charge an electric car using electricity from a coal power plant, is that car really 'zero emissions'?", "What do you think 'lifecycle emissions' means and why might it matter?"],
        "extend_components": [("Battery Recycling Rate", "The percentage of EV battery materials recovered and reused at end of life — currently only 5% of lithium-ion batteries are recycled, but this rate is expected to rise significantly with new regulations and technology"), ("Mining Impact", "The environmental and social costs of extracting lithium, cobalt, nickel, and rare earths for EV batteries — concentrated in specific regions with varying environmental and labor standards"), ("Fuel Infrastructure Carbon", "The emissions from extracting, refining, and transporting gasoline — adding approximately 20-30% to the carbon footprint beyond what comes out of the tailpipe")],
        "reflections": ["Why is 'zero emissions' a misleading label for electric vehicles?", "How does the grid carbon intensity in your state affect whether buying an EV makes environmental sense?", "What does the break-even analysis reveal about the importance of keeping vehicles longer rather than replacing them frequently?", "How should lifecycle analysis change the way we evaluate 'green' products in general?", "What are the ethical considerations of mining battery minerals in developing countries to make 'clean' cars for wealthy nations?"],
        "dimensions": [("Science Practice", "Developing and Using Models", "Students develop lifecycle models comparing electric and gas vehicle emissions across manufacturing, operation, and disposal phases."), ("Disciplinary Core Idea", "PS3.D Energy in Chemical Processes and Everyday Life / ETS1.B Developing Possible Solutions", "Energy conversion efficiency differs fundamentally between electric motors and internal combustion engines. Evaluating solutions requires analyzing trade-offs across the complete system lifecycle."), ("Crosscutting Concept", "Energy and Matter", "Students trace energy and carbon flows through the complete vehicle lifecycle, from mining raw materials through manufacturing, operation, and disposal, analyzing where emissions occur and how they can be reduced.")],
        "cast_items": ["Model how manufacturing emissions, grid carbon intensity, and driving efficiency determine total vehicle lifecycle emissions", "Predict the break-even mileage where an EV becomes cleaner than a gas car for different grid scenarios", "Evaluate the trade-offs between upfront manufacturing impact and long-term operational benefits in vehicle technology choices"],
        "cast_questions": [("Multiple Choice:", "An EV has 12 tons of manufacturing emissions compared to 8 tons for a gas car. The EV produces 50g CO2/mile on a clean grid, while the gas car produces 350g CO2/mile. At approximately how many miles does the EV's total lifecycle emissions become lower than the gas car's?"), ("Constructed Response:", "Using your model, explain why the environmental benefit of electric vehicles depends more on the electrical grid than on the vehicle itself. Compare the lifecycle emissions of the same EV charged on a coal-dominant grid versus a renewable grid.")],
        "background_intro": "The electric vehicle revolution is reshaping transportation, but the debate over whether EVs are truly 'green' often generates more heat than light. The answer lies in lifecycle analysis — a comprehensive accounting of every gram of CO2 from mine to junkyard — that reveals a nuanced truth far more interesting than the simple 'gas bad, electric good' narrative.",
        "background_sections": [("The Manufacturing Carbon Debt", "Producing an EV creates approximately 30-50% more manufacturing emissions than a comparable gas car, primarily due to the battery. A 75 kWh lithium-ion battery pack embodies 8-16 tons of CO2 from mining lithium and cobalt, refining materials, and manufacturing cells. This creates a 'carbon debt' — the EV starts its life with a larger environmental footprint that it must overcome through cleaner operation."), ("Grid Carbon Intensity: The Critical Variable", "The carbon intensity of electricity varies enormously by region. In France (nuclear-dominant), the grid produces ~60g CO2/kWh. In the US Midwest (coal-heavy), it can exceed 800g. Norway (hydro-dominant) is ~20g. An EV charged from the Norwegian grid produces over 95% less operating emissions than a gas car. The same EV on a coal grid might only be 20% cleaner. This single variable — where you charge — matters more than any vehicle specification."), ("Energy Conversion Efficiency", "Electric motors convert 77-82% of electrical energy to wheel motion. Internal combustion engines convert only 12-30% of fuel energy to motion — the rest is lost as heat. This fundamental physics advantage means EVs use far less total energy per mile, even when accounting for generation and transmission losses. It's why EVs are almost always cleaner on a lifecycle basis, except on the most carbon-intensive grids."), ("The Improving Equation", "Unlike gas cars (which are locked into fossil fuel), EVs get cleaner as the grid decarbonizes. An EV purchased today on a 500g/kWh grid will charge from a projected 300g/kWh grid in 2030 and potentially 100g/kWh by 2040 — becoming dramatically cleaner over its lifetime without any modification. This 'automatic improvement' is a unique advantage of electrification that no fossil fuel vehicle can replicate.")],
        "lever_L": "Students identify manufacturing carbon debt, grid carbon intensity, driving efficiency, cumulative operating emissions, and total lifecycle emissions as the key components of the vehicle comparison system.",
        "lever_E": "Students determine that manufacturing creates an initial carbon debt for EVs, grid intensity and efficiency determine operating emission rates, and the crossover point depends on how quickly cleaner operation overcomes the manufacturing deficit.",
        "lever_V": "Students build a computational model comparing EV and gas car lifecycle emissions across different grid scenarios and mileage milestones.",
        "lever_Ev": "Students run clean grid, dirty grid, and transitioning grid scenarios to discover how dramatically location and time affect the lifecycle comparison.",
        "lever_R": "Students add battery recycling, mining impact, or fuel infrastructure carbon to explore how expanding the system boundary changes the comparison.",
        "slides_guide": slides("Electric vs. Gas", "Modeling Lifecycle Emissions and Transportation Trade-offs", [("Manufacturing Carbon Debt",), ("Grid Carbon Intensity",), ("Driving Efficiency",), ("Cumulative Operating Emissions",), ("Total Lifecycle Emissions",)], "An EV starts dirtier but drives cleaner. How many miles until it wins? Does your grid change the answer?", [("Clean Grid EV",), ("Coal Grid EV",), ("Gas Baseline",)], ["Grid carbon intensity is THE determining variable", "EVs get cleaner as the grid improves"], "EVs are cleaner in almost every scenario — HOW much depends on where you charge.", "Design an Optimal Vehicle Fleet", "Design a 10-year fleet transition plan for 500 city vehicles.", "City fleet of 500 vehicles, grid projected 70% renewable by 2035.", ["Which vehicles to replace first?", "How does grid improvement affect the plan?"], "Automotive engineers earn $70,000-$120,000/year."),
        "sort_reasoning": "Manufacturing Carbon Debt and Grid Carbon Intensity are external because they represent fixed conditions the vehicle operates within — manufacturing is completed before the car is driven, and the grid's carbon intensity is determined by the regional energy infrastructure. Driving Efficiency, Cumulative Operating Emissions, and Total Lifecycle Emissions are internal because they emerge from how the vehicle converts and uses energy during its operational life.",
        "relationships": [("Manufacturing Carbon Debt to Total Lifecycle Emissions", "POSITIVE (+)", "Higher manufacturing emissions increase total lifecycle emissions — EVs start with a larger debt that must be overcome through cleaner operation."), ("Grid Carbon Intensity to Cumulative Operating Emissions", "POSITIVE (+)", "Higher grid carbon intensity means each kWh of charging produces more CO2, directly increasing operating emissions for EVs."), ("Driving Efficiency to Cumulative Operating Emissions", "NEGATIVE (-)", "Higher driving efficiency means less energy consumed per mile, reducing cumulative operating emissions regardless of energy source."), ("Cumulative Operating Emissions to Total Lifecycle Emissions", "POSITIVE (+)", "Operating emissions accumulate over the vehicle's lifetime and combine with manufacturing emissions to determine total lifecycle impact.")],
        "sim_answers": [("Clean Grid Scenario", "On a clean grid (50g CO2/kWh), the EV's operating emissions are approximately 15-20g CO2/mile compared to the gas car's 350-400g/mile. Despite the EV's higher manufacturing carbon debt (~12 tons vs ~8 tons), the EV breaks even at approximately 15,000-20,000 miles and then accumulates a growing lifecycle advantage. Over 150,000 miles, the EV produces approximately 50-70% fewer total lifecycle emissions."), ("Coal Grid Scenario", "On a coal-dominant grid (800g CO2/kWh), the EV's operating emissions rise to approximately 240-280g CO2/mile — still lower than the gas car's 350-400g/mile due to superior motor efficiency, but the advantage is much smaller. The break-even point extends to 60,000-80,000 miles, and the total lifecycle advantage shrinks to 10-20%. This shows why grid decarbonization is even more important than vehicle electrification.")],
        "reflection_exemplars": [("Why does location matter so much for EV environmental impact?", "Our model reveals that Grid Carbon Intensity is the dominant variable in determining whether an EV is dramatically cleaner or only marginally cleaner than a gas car. The same EV can produce 50-70% fewer lifecycle emissions on a clean grid or only 10-20% fewer on a coal grid. This means that the most effective climate policy isn't just subsidizing EVs — it's simultaneously decarbonizing the grid. An EV on a dirty grid is still slightly better, but an EV on a clean grid is transformatively better. The car is the same; the system it operates in determines its impact."), ("How should we think about lifecycle analysis for other products?", "The EV lifecycle analysis teaches a general principle: you can't evaluate a product's environmental impact by looking at just one phase. If we only measured tailpipe emissions, EVs appear 'zero emission' — hiding the manufacturing carbon debt. If we only measured manufacturing, gas cars appear cleaner — hiding the operating emissions. Lifecycle thinking reveals the FULL truth. This same principle applies to everything: solar panels (manufacturing emissions vs. clean generation), reusable bags (higher manufacturing vs. many uses), and buildings (construction carbon vs. operational efficiency).")],
        "stem_intro": "Present the challenge: Your city wants to transition its government fleet of 500 vehicles from gas to electric over 10 years. Use lifecycle analysis to design the optimal replacement strategy, considering vehicle types, grid trajectory, budget constraints, and maximizing total emission reduction.",
        "stem_concepts": [("Total Cost of Ownership", "The complete cost of a vehicle over its lifetime including purchase price, fuel, maintenance, insurance, and resale value. EVs typically cost more upfront but have lower fuel and maintenance costs, often reaching cost parity with gas cars within 3-5 years of ownership."), ("Fleet Electrification Sequencing", "Not all vehicles should be electrified at the same time. High-mileage vehicles (patrol cars, delivery vans) produce more operating emissions and benefit most from electrification. Low-mileage vehicles benefit less because they take longer to overcome the manufacturing carbon debt."), ("Grid Decarbonization Trajectory", "The projected path of grid carbon intensity over time. As more renewable energy comes online, the grid gets cleaner each year. This means EVs purchased later will charge from cleaner electricity, and EVs purchased now will benefit from grid improvements during their lifetime.")],
        "stem_eval": [("Expert (4)", "Plan includes lifecycle analysis by vehicle type, sequencing strategy based on mileage, grid trajectory projections, comprehensive cost-benefit analysis, and monitoring framework"), ("Proficient (3)", "Plan identifies appropriate vehicles for early replacement with reasonable cost and emission projections"), ("Developing (2)", "Plan suggests EV transition but lacks vehicle-specific analysis or grid trajectory consideration"), ("Beginning (1)", "Plan is incomplete or treats all EVs as equally beneficial regardless of use case and grid conditions")],
        "support": ["Provide a reference table showing manufacturing and per-mile emissions for gas cars, EVs on clean grids, and EVs on dirty grids", "Use a visual graph showing how EV and gas car cumulative emissions diverge over miles driven", "Sentence frames: 'The EV breaks even at ___ miles because ___, which means ___'"],
        "extensions": ["Research hydrogen fuel cell vehicles and compare their lifecycle emissions to both EVs and gas cars — is hydrogen a viable alternative or a distraction?", "Investigate the environmental and social impacts of cobalt mining in the Democratic Republic of Congo and analyze how battery chemistry innovations could reduce these impacts", "Calculate the lifecycle emissions of a self-driving electric rideshare vehicle that operates 100,000 miles/year vs. a personal EV driven 12,000 miles/year — which produces fewer emissions per passenger-mile?"],
        "cross_curr": [("Math", "Calculate the break-even mileage for an EV with 12 tons manufacturing emissions and 50g CO2/mile vs. a gas car with 8 tons manufacturing and 350g CO2/mile. Then recalculate for a dirty grid where the EV produces 250g CO2/mile."), ("ELA", "Write a fact-check article evaluating the claim that 'electric cars are worse for the environment than gas cars' — use lifecycle data to assess this claim's accuracy and explain what context it gets wrong"), ("Economics", "Analyze how government EV subsidies, gas taxes, and carbon pricing affect the economics of EV adoption and model what policy combination would achieve the fastest fleet transition")],
        "misconceptions": [("Electric cars are zero emission", "EVs produce zero TAILPIPE emissions, but the electricity they consume, the manufacturing of their batteries, and their eventual disposal all involve carbon emissions. Lifecycle analysis shows EVs produce 50-70% fewer total emissions than gas cars on clean grids, but they are not zero. The label 'zero emission vehicle' is technically about local air pollution, not total carbon impact.", "Show the lifecycle emission timeline graph: EVs start higher (manufacturing) but their line flattens (efficient driving) while gas cars keep climbing steeply (burning fuel every mile)."), ("The battery is so polluting that EVs never make up for it", "This claim cherry-picks the manufacturing phase while ignoring the operational advantage. Yes, battery production creates 8-16 tons of CO2. But gas cars emit 350-400g CO2 per mile EVERY mile driven. At 15,000 miles/year, a gas car adds 5-6 tons annually. The EV overcomes its manufacturing deficit in 1-3 years on a clean grid. Over a 150,000-mile lifetime, the total lifecycle advantage is enormous.", "Do the math together: 8 extra tons of manufacturing vs. 300g/mile savings × 150,000 miles = 45 tons saved. Net benefit: 37 tons less CO2."), ("We should wait for better EVs instead of buying now", "Waiting for 'better' technology is a common argument that ignores the cost of continuing to drive gas cars while waiting. Each year an EV ISN'T on the road, a gas car is emitting 5-6 tons of CO2. A slightly less efficient EV purchased today will produce far fewer lifetime emissions than a slightly more efficient one purchased in 5 years — because 5 years of gas driving cannot be un-emitted. The grid is also getting cleaner, so today's EV will benefit from grid improvements automatically.", "Calculate: 5 years of waiting × 5 tons/year gas emissions = 25 tons of CO2 that can never be recovered. No future efficiency improvement can offset those sunk emissions.")],
    })

    # L08: How Vaccines Train Your Immune Army
    lessons.append({
        "id": "G12L1-L08", "title": "How Vaccines Train Your Immune Army", "subtitle": "Modeling Immune Response, Antibody Production, and Herd Immunity Thresholds",
        "ngss": "HS-LS1-4", "ngss_desc": "Use a model to illustrate the role of cellular division (mitosis) and differentiation in producing and maintaining complex organisms.",
        "big_question": "How can injecting a weakened or dead pathogen teach your immune system to defeat a disease it has never encountered — and why does YOUR vaccination protect people who CAN'T be vaccinated?",
        "objectives": ["Model how antigen exposure, B-cell activation, antibody production, and memory cell formation interact to create lasting immunity", "Explain why vaccines produce protection without causing disease and how different vaccine types achieve this", "Predict herd immunity thresholds for diseases with different transmission rates", "Analyze why individual vaccination decisions affect community-level disease protection"],
        "vocabulary": [("Antigen", "A molecular marker on the surface of a pathogen that the immune system recognizes as foreign — vaccines present antigens without the dangerous pathogen, training the immune system to recognize the real threat"), ("Antibody", "Y-shaped proteins produced by B-cells that bind specifically to antigens, neutralizing pathogens — each antibody is custom-built to match one specific antigen, like a key fitting one lock"), ("Memory Cell", "Long-lived immune cells that 'remember' a pathogen's antigens for years or decades — when the real pathogen appears, memory cells trigger a rapid, powerful immune response that defeats the infection before symptoms develop"), ("Herd Immunity Threshold", "The percentage of a population that must be immune to prevent sustained disease transmission — for measles (R0=15), approximately 94% must be immune; for COVID-19 (R0=2-3), approximately 60-70%")],
        "components": [("Antigen Exposure", "The introduction of pathogen antigens to the immune system via vaccination — can be weakened live virus, inactivated virus, protein subunit, or mRNA instructions for making the antigen", True), ("B-Cell Activation", "The immune response triggered when B-cells recognize the vaccine antigen — activated B-cells multiply rapidly and differentiate into antibody-producing plasma cells", False), ("Antibody Production", "The output of antibodies specifically targeted to the vaccine antigen — peaks 2-4 weeks after vaccination and provides active protection against the pathogen", False), ("Memory Cell Formation", "The creation of long-lived B and T memory cells that persist after antibody levels decline — the key to lasting immunity that can rapidly reactivate if the real pathogen is encountered", False), ("Community Protection", "The level of disease protection across the population — when enough individuals are immune, transmission chains break and even unvaccinated people are protected by the 'herd'", False)],
        "think_about_it": "If a disease has an R0 of 15 (each infected person infects 15 others on average), your model must achieve a Community Protection threshold of 93-94% immunity to stop transmission. What happens if vaccination rates drop to 85%?",
        "scenarios": [("Successful Vaccination", "Set Antigen Exposure to standard vaccine dose — trace the pathway from B-Cell Activation through Antibody Production to Memory Cell Formation"), ("Community Threshold", "Set vaccination rate at 95% with R0=15 (measles) — observe Community Protection above the herd immunity threshold"), ("Threshold Collapse", "Drop vaccination rate to 85% with R0=15 — observe how falling below the herd threshold allows outbreak transmission")],
        "sim_scenarios": [("Individual Response", "Antigen: Standard vaccine dose | Healthy immune system", "What is the timeline from vaccination to full protection, and what happens at each stage?"), ("Above Threshold", "Vaccination rate: 95% | Disease R0: 15 (measles)", "When 95% are immune and the threshold is 94%, what level of Community Protection exists?"), ("Below Threshold", "Vaccination rate: 85% | Disease R0: 15 (measles)", "What happens to outbreak potential when vaccination drops just 10% below the herd immunity threshold?")],
        "discoveries": ["Vaccines train the immune system by presenting antigens without disease — the immune response is real but the danger is removed, creating genuine protective immunity", "Memory cells are the key to lasting protection — even when antibody levels decline over months or years, memory cells can reactivate within hours when the real pathogen appears", "Herd immunity thresholds are mathematical, not arbitrary — for R0=15, exactly 1-(1/15) = 93.3% must be immune; dropping even slightly below this threshold allows exponential outbreak growth", "Individual vaccination decisions are inherently community decisions — your immunity protects immunocompromised people, infants, and others who cannot be vaccinated"],
        "answer": "Vaccines work by presenting your immune system with pathogen antigens in a safe form — teaching your B-cells to recognize the threat without the danger of actual infection. The activated B-cells produce antibodies for immediate protection and memory cells for decades-long immunity. When enough people are vaccinated, herd immunity creates a shield around those who can't be vaccinated. The math is precise: for highly contagious diseases like measles (R0=15), 93-94% must be immune. When communities drop below this threshold — as happened in multiple measles outbreaks since 2015 — the disease roars back with mathematical certainty. Your vaccination isn't just about you; it's about the immunocompromised child who depends on YOUR immunity for protection.",
        "stem_title": "Design a Vaccination Campaign for a Disease Outbreak",
        "stem_mission": "Design a targeted vaccination campaign to achieve herd immunity in a community experiencing a disease outbreak, addressing both the science of immunity and the challenge of vaccine hesitancy.",
        "stem_scenario": "A measles outbreak has struck a community where vaccination rates have dropped to 82%. Three schools have confirmed cases and the disease is spreading. Your team must design a campaign to rapidly increase vaccination rates above the 94% herd immunity threshold while addressing parents' concerns with scientific evidence.",
        "stem_questions": ["What vaccination rate must be achieved to stop the outbreak, and how is this calculated from R0?", "Which populations should be prioritized for vaccination and why?", "How can you address vaccine hesitancy using immunology science rather than just public pressure?"],
        "stem_design_qs": ["What is your target vaccination rate and what epidemiological evidence supports this specific threshold?", "What communication strategy does your campaign use to explain vaccine science to hesitant parents?", "How does your plan prioritize limited vaccine doses during the early response phase?", "What monitoring metrics would you track to determine if your campaign is working?"],
        "career": "Immunologists study how the immune system fights disease and develop new vaccines, earning $75,000-$140,000/year. Epidemiologists track disease outbreaks and design public health interventions, earning $60,000-$110,000/year. Public health communicators translate complex vaccine science for public audiences, earning $50,000-$85,000/year.",
        "images": img("G12L1-L08", "A photorealistic microscopic view of antibodies (Y-shaped proteins) binding to virus particles, colorful scientific visualization with dramatic depth of field", "A diverse group of 17-18 year old students in a modern biology classroom examining immune system models and vaccine diagrams, microscopes visible, engaged learning atmosphere", "A diverse group of 17-18 year old students building computational models of immune response on laptops, modern classroom with immunology posters and herd immunity threshold diagrams", "A teacher leading discussion with diverse 17-18 year old students about vaccines and herd immunity, an antibody-antigen binding diagram on smartboard, scientific atmosphere", "Diverse 17-18 year old students designing vaccination campaign materials on whiteboards with epidemiological data, community maps, and communication strategies"),
        "pre_assessment": ["How do you think vaccines work — what do they actually do inside your body?", "Why do some vaccines require multiple doses or boosters while others last a lifetime?", "What do you think 'herd immunity' means and why does it matter?", "If a disease is very contagious, does that change how many people need to be vaccinated?"],
        "extend_components": [("Vaccine Type", "The specific technology used to present antigens — live attenuated, inactivated, subunit, mRNA, or viral vector — each has different immune response profiles, storage requirements, and side effect profiles"), ("Waning Immunity", "The gradual decline in antibody levels and memory cell responsiveness over time — explains why some vaccines need boosters and why immunity from natural infection can also fade"), ("Mutation Rate", "How quickly the pathogen evolves new antigen variants — high mutation rates (influenza, HIV) can outpace immune memory, requiring annual reformulation or making vaccines less effective")],
        "reflections": ["How does the mathematical relationship between R0 and herd immunity threshold explain why measles outbreaks occur when vaccination rates drop even slightly?", "Why is it accurate to say that getting vaccinated is both an individual health decision and a community protection decision?", "How does your model explain why some people who are vaccinated can still get sick, and why this doesn't mean the vaccine 'doesn't work'?", "What does the model reveal about the vulnerability of people who cannot be vaccinated (infants, immunocompromised)?", "How should vaccine policy balance individual freedom with community protection?"],
        "dimensions": [("Science Practice", "Developing and Using Models", "Students develop computational models of immune response to vaccination, tracing the pathway from antigen exposure through memory cell formation and predicting community-level protection thresholds."), ("Disciplinary Core Idea", "LS1.B Growth and Development of Organisms", "Cellular division and differentiation of B-cells into plasma cells and memory cells is the mechanism by which vaccines produce lasting immunity without causing disease."), ("Crosscutting Concept", "Cause and Effect", "Students trace the causal chain from antigen exposure through immune activation to community protection, identifying how individual-level biology produces population-level disease prevention.")],
        "cast_items": ["Model how vaccine antigens trigger B-cell activation, antibody production, and memory cell formation", "Predict herd immunity thresholds based on disease transmission rates (R0 values)", "Explain why individual vaccination decisions affect community-level disease protection"],
        "cast_questions": [("Multiple Choice:", "A new disease has an R0 of 5, meaning each infected person spreads it to 5 others on average. Using the herd immunity formula (1 - 1/R0), what percentage of the population must be immune to achieve herd immunity?"), ("Constructed Response:", "Using your model, explain why a community with 90% measles vaccination rate experienced an outbreak while a community with 95% vaccination rate did not. Reference the herd immunity threshold and R0 in your answer.")],
        "background_intro": "Vaccines are arguably the most successful medical intervention in human history, preventing an estimated 154 million deaths over the past 50 years. Yet the science behind how they work — training the adaptive immune system to recognize threats it's never faced — is remarkably elegant and often misunderstood.",
        "background_sections": [("How the Adaptive Immune System Learns", "Unlike the innate immune system (which provides general defenses), the adaptive immune system creates targeted responses to specific pathogens. When a B-cell encounters an antigen matching its receptor, it activates, multiplies, and differentiates. Some daughter cells become plasma cells that mass-produce antibodies. Others become memory cells that persist for years or decades. This antigen-specific learning is the foundation of vaccine science."), ("Vaccine Technologies", "Different vaccines present antigens in different ways. Live attenuated vaccines (MMR, chickenpox) use weakened viruses that replicate but don't cause disease. Inactivated vaccines (flu shots, polio) use killed pathogens. Subunit vaccines (hepatitis B, HPV) use only specific proteins. mRNA vaccines (COVID-19) give cells instructions to make the antigen temporarily. All approaches trigger the same adaptive immune response but differ in strength, duration, and side effects."), ("The Mathematics of Herd Immunity", "Herd immunity is a mathematical property of disease transmission. For a disease with basic reproduction number R0, the herd immunity threshold = 1 - (1/R0). For measles (R0 ~15), this equals 93.3%. For COVID-19 (R0 ~2-3), approximately 50-67%. Below the threshold, each infected person infects more than one other on average, and the disease spreads exponentially. Above the threshold, transmission chains die out. This is why even small drops in vaccination rates can trigger devastating outbreaks."), ("Vaccine Hesitancy: A Public Health Crisis", "The WHO named vaccine hesitancy one of the top 10 threats to global health. Misinformation — including the thoroughly debunked claim linking vaccines to autism (based on a fraudulent 1998 study) — has eroded confidence. In 2019, the US experienced 1,282 measles cases, the highest count in 27 years, primarily in under-vaccinated communities. Understanding the immunology — not just the policy arguments — is essential for science-literate citizens navigating this debate.")],
        "lever_L": "Students identify antigen exposure, B-cell activation, antibody production, memory cell formation, and community protection as the key components of the vaccine-immunity system.",
        "lever_E": "Students determine that antigen exposure triggers B-cell activation, activated B-cells produce antibodies and memory cells, and sufficient individual immunity aggregates to community protection above the herd threshold.",
        "lever_V": "Students build a computational model tracing the immune response from vaccination through community-level disease protection.",
        "lever_Ev": "Students run individual response, above-threshold, and below-threshold scenarios to discover how vaccination rates determine outbreak potential.",
        "lever_R": "Students add vaccine type, waning immunity, or mutation rate to explore how real-world complications affect the basic immunity model.",
        "slides_guide": slides("How Vaccines Train Your Immune Army", "Modeling Immune Response and Herd Immunity", [("Antigen Exposure",), ("B-Cell Activation",), ("Antibody Production",), ("Memory Cell Formation",), ("Community Protection",)], "If measles needs 94% immunity and vaccination drops to 85%, what does the math predict?", [("Individual Response",), ("Above Threshold",), ("Below Threshold",)], ["Memory cells provide decades of protection from a single vaccine", "Herd immunity thresholds are mathematical, not arbitrary"], "Vaccines train your immune system to defeat threats it's never seen — and your immunity protects others.", "Design a Vaccination Campaign", "Design a campaign to achieve herd immunity during a measles outbreak.", "Community at 82% vaccination with active measles spread.", ["What rate stops the outbreak?", "How to address hesitancy with science?"], "Immunologists earn $75,000-$140,000/year."),
        "sort_reasoning": "Antigen Exposure is external because it represents the vaccination event — an input administered from outside the body. B-Cell Activation, Antibody Production, Memory Cell Formation, and Community Protection are internal because they are biological and epidemiological responses that emerge from the immune system processing the antigen.",
        "relationships": [("Antigen Exposure to B-Cell Activation", "POSITIVE (+)", "Vaccine antigens bind to B-cell receptors, triggering activation, proliferation, and differentiation into antibody-producing plasma cells and long-lived memory cells."), ("B-Cell Activation to Antibody Production", "POSITIVE (+)", "Activated B-cells differentiate into plasma cells that mass-produce antigen-specific antibodies, peaking 2-4 weeks after vaccination."), ("B-Cell Activation to Memory Cell Formation", "POSITIVE (+)", "A subset of activated B-cells differentiate into memory cells that persist for years or decades, providing rapid recall immunity if the pathogen is encountered."), ("Memory Cell Formation to Community Protection", "POSITIVE (+)", "When enough individuals have memory cells (achieving vaccination rates above the herd immunity threshold), transmission chains break and even unvaccinated individuals are protected.")],
        "sim_answers": [("Above Threshold Scenario", "With 95% vaccination rate against a disease with R0=15 (herd threshold 93.3%), Community Protection is robust. Each infected person encounters mostly immune individuals, infecting fewer than 1 new person on average. Transmission chains quickly die out, and even unvaccinated individuals are protected because the virus can't find enough susceptible hosts to sustain spread."), ("Below Threshold Scenario", "Dropping to 85% vaccination (below the 93.3% threshold), each infected person can now find enough susceptible individuals to infect more than 1 new person. Transmission becomes self-sustaining and grows exponentially. The 15% unvaccinated population provides enough fuel for a full-scale outbreak. The model shows the transition is sharp — the difference between 95% and 85% is the difference between containment and epidemic.")],
        "reflection_exemplars": [("Why is herd immunity a mathematical threshold, not a gradient?", "The transition from disease containment to outbreak is governed by a mathematical tipping point: when the effective reproduction number (Re) crosses 1.0. Above the herd immunity threshold, each case produces less than 1 new case and the disease dies out. Below it, each case produces more than 1 new case and the disease grows exponentially. There's no 'partial herd immunity' — you're either above the threshold (protected) or below it (vulnerable). This is why even small drops in vaccination rates can trigger explosive outbreaks."), ("How should science inform vaccine policy?", "Our model reveals that vaccination is inherently a community decision because individual immunity contributes to population-level protection. People who cannot be vaccinated — infants, immunocompromised patients, organ transplant recipients — depend on others' immunity for survival. The model shows that when vaccination rates drop below the herd threshold, these vulnerable individuals bear the highest risk of severe disease. Science can't dictate policy, but it clearly demonstrates that individual vaccine decisions have measurable consequences for community health and that the herd immunity threshold is not negotiable biology.")],
        "stem_intro": "Present the challenge: A measles outbreak has hit a community with 82% vaccination rate — well below the 94% herd immunity threshold. Your team must design a rapid vaccination campaign that achieves herd immunity while addressing vaccine hesitancy with scientific evidence, not just pressure.",
        "stem_concepts": [("Ring Vaccination", "A targeted strategy where everyone in contact with or living near a confirmed case is vaccinated immediately, creating a ring of immunity that stops transmission from spreading outward. Highly effective for diseases with identifiable contact chains."), ("Vaccine Confidence Communication", "Research shows that the most effective approach to vaccine hesitancy is NOT debunking myths (which can backfire by reinforcing them) but rather explaining how vaccines work using clear, visual immunology. Teaching the science of memory cells and herd immunity is more persuasive than arguing about safety statistics."), ("Epidemiological Surveillance", "Real-time tracking of cases, contacts, and vaccination status to identify outbreak clusters and direct resources. Modern surveillance uses genomic sequencing to trace transmission chains and predict where outbreaks will spread next.")],
        "stem_eval": [("Expert (4)", "Campaign calculates precise herd immunity target, uses ring vaccination and targeted outreach, addresses hesitancy with immunology education, and includes surveillance monitoring plan"), ("Proficient (3)", "Campaign has reasonable vaccination targets and includes some community engagement strategy"), ("Developing (2)", "Campaign identifies need for higher vaccination but lacks specific strategies or scientific communication approach"), ("Beginning (1)", "Campaign is incomplete or relies primarily on mandates without scientific education component")],
        "support": ["Provide a visual diagram of the immune response pathway: Antigen -> B-Cell -> Antibodies + Memory Cells -> Protection", "Use a herd immunity threshold calculator where students plug in R0 values and see the required vaccination rate", "Sentence frames: 'When vaccination rates drop below ___%, the model predicts ___ because each infected person now infects more than ___'"],
        "extensions": ["Research how mRNA vaccine technology works at the molecular level and explain why it represents a paradigm shift in vaccine development", "Investigate the mathematical modeling that epidemiologists used to predict COVID-19 spread and evaluate how accurate those models were", "Analyze the ethics of vaccine mandates: when (if ever) should the government require vaccination, and what does the science of herd immunity contribute to this debate?"],
        "cross_curr": [("Math", "Calculate the herd immunity threshold for diseases with R0 values of 2, 5, 10, and 15. Graph the relationship between R0 and required vaccination rate. What pattern do you observe?"), ("ELA", "Write a science communication piece explaining how vaccines work to an audience of concerned parents, using the immune response model and avoiding condescension"), ("History", "Research the eradication of smallpox — the only human disease ever eliminated by vaccination — and analyze what made the global campaign successful and what lessons apply to current vaccination challenges")],
        "misconceptions": [("Vaccines give you a mild version of the disease", "Most modern vaccines do NOT contain the disease-causing pathogen in any active form. Inactivated vaccines use killed virus, subunit vaccines use only protein fragments, and mRNA vaccines contain no virus at all — just temporary instructions for making one antigen protein. Side effects like soreness and mild fever are signs of immune activation, not disease. You're feeling your immune system learning, not getting sick.", "Analogy: A fire drill isn't a fire. It prepares you for the real thing without any actual danger. Vaccines are immune system fire drills."), ("Natural immunity is always better than vaccine immunity", "While natural infection sometimes produces stronger immunity, it comes at the cost of actually having the disease — which can cause severe complications, hospitalization, or death. Measles infection causes encephalitis in 1 in 1,000 cases. The measles vaccine provides 97% protection with minimal risk. The model shows that both natural and vaccine immunity produce memory cells; the difference is that vaccines achieve this without the disease.", "Ask: Would you rather learn to swim by being thrown in the ocean during a storm (natural infection) or by taking lessons in a pool (vaccination)? Both teach you to swim, but one might kill you."), ("If most people are vaccinated, I don't need to be", "This is a free-rider problem that only works if everyone else doesn't think the same way. If enough people opt out, the community drops below the herd immunity threshold and EVERYONE becomes vulnerable — including those who thought they were protected by others' immunity. The model shows this is a sharp threshold: 95% vaccination = containment; 85% = outbreak. Your individual decision to skip vaccination increases outbreak risk for the entire community.", "Run the model: Show what happens when 5%, then 10%, then 15% of people adopt the free-rider strategy. The collapse of herd immunity is dramatic and rapid.")],
    })

    return lessons


# ============================================================
# Build and write files
# ============================================================

if __name__ == "__main__":
    print("Grade 12 Lesson Data Generator")
    print("=" * 50)

    # Build Level 1 (start with first 2, more to come)
    L1 = build_L1()
    print(f"Level 1: {len(L1)} lessons built")

    # Write Level 1
    fp1 = os.path.join(SCRIPT_DIR, "lesson_data_G12_L1.py")
    write_lesson_file(fp1, "Complete lesson data for G12L1-L01 through G12L1-L10 (Grade 12 Level 1: Science, Society & You)", L1)

    print("\nDone! Files generated.")
    print("NOTE: Run build_G12_data_L03_L10.py to add remaining L1 lessons")
    print("NOTE: Run build_G12_data_L2.py and build_G12_data_L3.py for Levels 2 and 3")
