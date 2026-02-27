#!/usr/bin/env python3
"""Complete lesson data for G12L1-L01 through G12L1-L10 (Grade 12 Level 1: Science, Society & You)"""

L01 = {
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
    "images": {
        "cover": ("G12L1-L01-cover.png", "A photorealistic close-up of a diverse 17-18 year old student looking at an optical illusion display in a modern science classroom, with visual distortion effects suggesting perception vs reality, dramatic lighting"),
        "landscape": ("G12L1-L01-landscape.png", "A diverse group of 17-18 year old students in a modern psychology classroom examining optical illusions and brain models on their desks, engaged discussion, natural lighting through large windows"),
        "modeling": ("G12L1-L01-modeling.png", "A diverse group of 17-18 year old students working on laptops building computational models of cognitive bias, modern classroom with brain diagrams and decision flowcharts on the walls"),
        "discussion": ("G12L1-L01-discussion.png", "A teacher leading a discussion with diverse 17-18 year old students about cognitive bias, a brain scan image and bias flowchart displayed on a smartboard, students actively debating"),
        "stem": ("G12L1-L01-stem.png", "Diverse 17-18 year old students designing bias-aware decision tools on whiteboards with flowcharts, decision trees, and human factors diagrams")
    },
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
    "slides_guide": [
        {
            "num": "Slide 1",
            "title": "Cover",
            "visual": "Title slide with compelling image related to Why Does Your Brain Lie to You?",
            "say": "Today we're investigating something that affects every single one of you. Modeling Cognitive Bias.",
            "do": "Show cover image. Ask: What do you already know about this topic? Quick share-out.",
            "time": "2 min"
        },
        {
            "num": "Slide 2",
            "title": "Learning Objectives",
            "visual": "Learning goals and vocabulary terms",
            "say": "Here's what you'll be able to do by the end of today's lesson.",
            "do": "Have students read objectives aloud. Pre-teach vocabulary with quick visual aids.",
            "time": "3 min"
        },
        {
            "num": "Slide 3",
            "title": "Big Question",
            "visual": "Provocative question related to Why Does Your Brain Lie to You?",
            "say": "This is our driving question. By the end of class, you'll be able to answer it with evidence from your model.",
            "do": "Quick-write: Students write their initial hypothesis. Save to compare later.",
            "time": "3 min"
        },
        {
            "num": "Slide 4",
            "title": "LEVER Framework",
            "visual": "LEVER steps overview",
            "say": "We're going to build a computational model to investigate this system. Here are our five steps.",
            "do": "Preview each LEVER step. Emphasize that modeling reveals hidden patterns.",
            "time": "2 min"
        },
        {
            "num": "Slide 5",
            "title": "Activity 1: Components",
            "visual": "Component cards for sorting",
            "say": "What are the key parts of this system? Which ones come from outside, and which respond inside?",
            "do": "Guide sorting of external vs. internal components. Use think-pair-share for reasoning.",
            "time": "8 min"
        },
        {
            "num": "Slide 6",
            "title": "Activity 2: Connections",
            "visual": "Relationship arrows between components",
            "say": "When Prior Experience is very strong and Sensory Input is weak, what happens to Bias Strength?",
            "do": "Students draw arrows showing +/- relationships. Discuss feedback loops if present.",
            "time": "8 min"
        },
        {
            "num": "Slide 7",
            "title": "Activity 3: Simulation",
            "visual": "Simulation results graphs",
            "say": "Now let's test our model. Run each scenario and record what happens.",
            "do": "Students run all scenarios, record predictions vs. observations. Discuss surprises.",
            "time": "10 min"
        },
        {
            "num": "Slide 8",
            "title": "Discoveries",
            "visual": "Key findings summary",
            "say": "So what did our model reveal? Your brain lies because it's optimized for speed, not accuracy....",
            "do": "Class discussion of discoveries. Compare initial hypotheses to model evidence.",
            "time": "5 min"
        },
        {
            "num": "Slide 9",
            "title": "STEM Challenge",
            "visual": "Engineering challenge: Design a Bias-Aware Decision Tool",
            "say": "Now apply what you've learned. Design a decision-support tool that helps doctors maintain diagnostic accuracy....",
            "do": "Groups design solutions using model data. Present and evaluate designs.",
            "time": "12 min"
        }
    ],
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
    ]
}

L02 = {
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
    "images": {
        "cover": ("G12L1-L02-cover.png", "A photorealistic image of a diverse 17-18 year old student struggling to stay awake in an early morning classroom, head propped on hand, other students similarly drowsy, blue-tinted early morning light through windows"),
        "landscape": ("G12L1-L02-landscape.png", "A diverse group of 17-18 year old students in a modern biology classroom examining brain models and circadian rhythm diagrams, some students looking tired while engaged in discussion"),
        "modeling": ("G12L1-L02-modeling.png", "A diverse group of 17-18 year old students working on laptops building computational models of sleep cycles, modern classroom with sleep stage diagrams and circadian charts on walls"),
        "discussion": ("G12L1-L02-discussion.png", "A teacher leading discussion with diverse 17-18 year old students about sleep science, a melatonin cycle graph and brain diagram on smartboard, students actively participating"),
        "stem": ("G12L1-L02-stem.png", "Diverse 17-18 year old students designing school schedule proposals on whiteboards with circadian rhythm charts, clock diagrams, and data tables")
    },
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
    "slides_guide": [
        {
            "num": "Slide 1",
            "title": "Cover",
            "visual": "Title slide with compelling image related to The Science of Sleep",
            "say": "Today we're investigating something that affects every single one of you. Modeling Circadian Rhythms and Sleep Architecture.",
            "do": "Show cover image. Ask: What do you already know about this topic? Quick share-out.",
            "time": "2 min"
        },
        {
            "num": "Slide 2",
            "title": "Learning Objectives",
            "visual": "Learning goals and vocabulary terms",
            "say": "Here's what you'll be able to do by the end of today's lesson.",
            "do": "Have students read objectives aloud. Pre-teach vocabulary with quick visual aids.",
            "time": "3 min"
        },
        {
            "num": "Slide 3",
            "title": "Big Question",
            "visual": "Provocative question related to The Science of Sleep",
            "say": "This is our driving question. By the end of class, you'll be able to answer it with evidence from your model.",
            "do": "Quick-write: Students write their initial hypothesis. Save to compare later.",
            "time": "3 min"
        },
        {
            "num": "Slide 4",
            "title": "LEVER Framework",
            "visual": "LEVER steps overview",
            "say": "We're going to build a computational model to investigate this system. Here are our five steps.",
            "do": "Preview each LEVER step. Emphasize that modeling reveals hidden patterns.",
            "time": "2 min"
        },
        {
            "num": "Slide 5",
            "title": "Activity 1: Components",
            "visual": "Component cards for sorting",
            "say": "What are the key parts of this system? Which ones come from outside, and which respond inside?",
            "do": "Guide sorting of external vs. internal components. Use think-pair-share for reasoning.",
            "time": "8 min"
        },
        {
            "num": "Slide 6",
            "title": "Activity 2: Connections",
            "visual": "Relationship arrows between components",
            "say": "During puberty, melatonin doesn't rise until 11 PM. School starts at 7:30 AM. What happens?",
            "do": "Students draw arrows showing +/- relationships. Discuss feedback loops if present.",
            "time": "8 min"
        },
        {
            "num": "Slide 7",
            "title": "Activity 3: Simulation",
            "visual": "Simulation results graphs",
            "say": "Now let's test our model. Run each scenario and record what happens.",
            "do": "Students run all scenarios, record predictions vs. observations. Discuss surprises.",
            "time": "10 min"
        },
        {
            "num": "Slide 8",
            "title": "Discoveries",
            "visual": "Key findings summary",
            "say": "So what did our model reveal? Teens can't wake up because their brains are wired to sleep later during puberty....",
            "do": "Class discussion of discoveries. Compare initial hypotheses to model evidence.",
            "time": "5 min"
        },
        {
            "num": "Slide 9",
            "title": "STEM Challenge",
            "visual": "Engineering challenge: Design an Evidence-Based School Schedule",
            "say": "Now apply what you've learned. Design an optimal school schedule maximizing cognitive performance....",
            "do": "Groups design solutions using model data. Present and evaluate designs.",
            "time": "12 min"
        }
    ],
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
    ]
}

L03 = {
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
    "images": {
        "cover": ("G12L1-L03-cover.png", "A photorealistic image of water flowing from a kitchen faucet into a glass, with a subtle split showing clean water on one side and discolored water on the other, dramatic lighting emphasizing the contrast"),
        "landscape": ("G12L1-L03-landscape.png", "A diverse group of 17-18 year old students in a modern chemistry lab testing water samples with pH meters and testing kits, colorful chemical indicators visible, engaged and focused"),
        "modeling": ("G12L1-L03-modeling.png", "A diverse group of 17-18 year old students working on laptops building computational models of water distribution systems, modern classroom with water cycle diagrams and pipe infrastructure maps"),
        "discussion": ("G12L1-L03-discussion.png", "A teacher leading discussion with diverse 17-18 year old students about water contamination, a water distribution system diagram on smartboard showing treatment plant to homes"),
        "stem": ("G12L1-L03-stem.png", "Diverse 17-18 year old students designing water monitoring systems on whiteboards with sensor placement maps, alert flowcharts, and water chemistry data")
    },
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
    "slides_guide": [
        {
            "num": "Slide 1",
            "title": "Cover",
            "visual": "Title slide with compelling image related to Is Your Tap Water Safe?",
            "say": "Today we're investigating something that affects every single one of you. Modeling Water Contamination and Public Health.",
            "do": "Show cover image. Ask: What do you already know about this topic? Quick share-out.",
            "time": "2 min"
        },
        {
            "num": "Slide 2",
            "title": "Learning Objectives",
            "visual": "Learning goals and vocabulary terms",
            "say": "Here's what you'll be able to do by the end of today's lesson.",
            "do": "Have students read objectives aloud. Pre-teach vocabulary with quick visual aids.",
            "time": "3 min"
        },
        {
            "num": "Slide 3",
            "title": "Big Question",
            "visual": "Provocative question related to Is Your Tap Water Safe?",
            "say": "This is our driving question. By the end of class, you'll be able to answer it with evidence from your model.",
            "do": "Quick-write: Students write their initial hypothesis. Save to compare later.",
            "time": "3 min"
        },
        {
            "num": "Slide 4",
            "title": "LEVER Framework",
            "visual": "LEVER steps overview",
            "say": "We're going to build a computational model to investigate this system. Here are our five steps.",
            "do": "Preview each LEVER step. Emphasize that modeling reveals hidden patterns.",
            "time": "2 min"
        },
        {
            "num": "Slide 5",
            "title": "Activity 1: Components",
            "visual": "Component cards for sorting",
            "say": "What are the key parts of this system? Which ones come from outside, and which respond inside?",
            "do": "Guide sorting of external vs. internal components. Use think-pair-share for reasoning.",
            "time": "8 min"
        },
        {
            "num": "Slide 6",
            "title": "Activity 2: Connections",
            "visual": "Relationship arrows between components",
            "say": "In Flint, switching water sources increased corrosion. Why didn't treatment prevent the crisis?",
            "do": "Students draw arrows showing +/- relationships. Discuss feedback loops if present.",
            "time": "8 min"
        },
        {
            "num": "Slide 7",
            "title": "Activity 3: Simulation",
            "visual": "Simulation results graphs",
            "say": "Now let's test our model. Run each scenario and record what happens.",
            "do": "Students run all scenarios, record predictions vs. observations. Discuss surprises.",
            "time": "10 min"
        },
        {
            "num": "Slide 8",
            "title": "Discoveries",
            "visual": "Key findings summary",
            "say": "So what did our model reveal? Your tap water depends on source protection, treatment, and distribution all working together....",
            "do": "Class discussion of discoveries. Compare initial hypotheses to model evidence.",
            "time": "5 min"
        },
        {
            "num": "Slide 9",
            "title": "STEM Challenge",
            "visual": "Engineering challenge: Design a Community Water Monitoring System",
            "say": "Now apply what you've learned. Design a low-cost monitoring system for early contamination detection....",
            "do": "Groups design solutions using model data. Present and evaluate designs.",
            "time": "12 min"
        }
    ],
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
    ]
}

L04 = {
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
    "images": {
        "cover": ("G12L1-L04-cover.png", "A photorealistic split image showing ultra-processed snack foods (bright packaging, artificial colors) on one side and whole foods (fresh fruits, vegetables, grains) on the other, dramatic contrast lighting"),
        "landscape": ("G12L1-L04-landscape.png", "A diverse group of 17-18 year old students in a modern food science lab examining nutrition labels and food samples, microscopes and chemical testing equipment visible"),
        "modeling": ("G12L1-L04-modeling.png", "A diverse group of 17-18 year old students working on laptops building computational models of metabolic pathways, modern classroom with food system diagrams and NOVA classification posters"),
        "discussion": ("G12L1-L04-discussion.png", "A teacher leading discussion with diverse 17-18 year old students about food processing, a comparison of ingredient lists on smartboard, students examining packaged food labels"),
        "stem": ("G12L1-L04-stem.png", "Diverse 17-18 year old students designing healthy school lunch menus on whiteboards with nutrition data, cost calculations, and meal planning templates")
    },
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
    "slides_guide": [
        {
            "num": "Slide 1",
            "title": "Cover",
            "visual": "Title slide with compelling image related to The Ultra-Processed Food Problem",
            "say": "Today we're investigating something that affects every single one of you. Modeling Food Chemistry and Metabolic Health.",
            "do": "Show cover image. Ask: What do you already know about this topic? Quick share-out.",
            "time": "2 min"
        },
        {
            "num": "Slide 2",
            "title": "Learning Objectives",
            "visual": "Learning goals and vocabulary terms",
            "say": "Here's what you'll be able to do by the end of today's lesson.",
            "do": "Have students read objectives aloud. Pre-teach vocabulary with quick visual aids.",
            "time": "3 min"
        },
        {
            "num": "Slide 3",
            "title": "Big Question",
            "visual": "Provocative question related to The Ultra-Processed Food Problem",
            "say": "This is our driving question. By the end of class, you'll be able to answer it with evidence from your model.",
            "do": "Quick-write: Students write their initial hypothesis. Save to compare later.",
            "time": "3 min"
        },
        {
            "num": "Slide 4",
            "title": "LEVER Framework",
            "visual": "LEVER steps overview",
            "say": "We're going to build a computational model to investigate this system. Here are our five steps.",
            "do": "Preview each LEVER step. Emphasize that modeling reveals hidden patterns.",
            "time": "2 min"
        },
        {
            "num": "Slide 5",
            "title": "Activity 1: Components",
            "visual": "Component cards for sorting",
            "say": "What are the key parts of this system? Which ones come from outside, and which respond inside?",
            "do": "Guide sorting of external vs. internal components. Use think-pair-share for reasoning.",
            "time": "8 min"
        },
        {
            "num": "Slide 6",
            "title": "Activity 2: Connections",
            "visual": "Relationship arrows between components",
            "say": "NIH study: same calories, same nutrients, but 500 MORE calories consumed from ultra-processed meals. Why?",
            "do": "Students draw arrows showing +/- relationships. Discuss feedback loops if present.",
            "time": "8 min"
        },
        {
            "num": "Slide 7",
            "title": "Activity 3: Simulation",
            "visual": "Simulation results graphs",
            "say": "Now let's test our model. Run each scenario and record what happens.",
            "do": "Students run all scenarios, record predictions vs. observations. Discuss surprises.",
            "time": "10 min"
        },
        {
            "num": "Slide 8",
            "title": "Discoveries",
            "visual": "Key findings summary",
            "say": "So what did our model reveal? Ultra-processed foods bypass your body's natural fullness systems....",
            "do": "Class discussion of discoveries. Compare initial hypotheses to model evidence.",
            "time": "5 min"
        },
        {
            "num": "Slide 9",
            "title": "STEM Challenge",
            "visual": "Engineering challenge: Design a School Lunch That Beats Ultra-Processing",
            "say": "Now apply what you've learned. Design meals as satisfying as processed ones using whole foods within budget....",
            "do": "Groups design solutions using model data. Present and evaluate designs.",
            "time": "12 min"
        }
    ],
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
    ]
}

L05 = {
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
    "images": {
        "cover": ("G12L1-L05-cover.png", "A photorealistic image of a brain model with glowing neural pathways highlighted in the reward circuit, dopamine pathway illuminated in bright color against dark background, scientific and dramatic"),
        "landscape": ("G12L1-L05-landscape.png", "A diverse group of 17-18 year old students in a modern neuroscience classroom examining brain models and neural pathway diagrams, engaged in serious scientific discussion"),
        "modeling": ("G12L1-L05-modeling.png", "A diverse group of 17-18 year old students working on laptops building computational models of neurotransmitter systems, modern classroom with brain reward circuit posters and genetics diagrams"),
        "discussion": ("G12L1-L05-discussion.png", "A teacher leading discussion with diverse 17-18 year old students about addiction neuroscience, a dopamine pathway diagram and risk factor chart on smartboard, respectful and scientific tone"),
        "stem": ("G12L1-L05-stem.png", "Diverse 17-18 year old students designing prevention program materials on whiteboards with neuroscience diagrams, protective factor lists, and program evaluation metrics")
    },
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
    "slides_guide": [
        {
            "num": "Slide 1",
            "title": "Cover",
            "visual": "Title slide with compelling image related to Why Some People Get Addicted",
            "say": "Today we're investigating something that affects every single one of you. Modeling Neurotransmitter Systems and Addiction.",
            "do": "Show cover image. Ask: What do you already know about this topic? Quick share-out.",
            "time": "2 min"
        },
        {
            "num": "Slide 2",
            "title": "Learning Objectives",
            "visual": "Learning goals and vocabulary terms",
            "say": "Here's what you'll be able to do by the end of today's lesson.",
            "do": "Have students read objectives aloud. Pre-teach vocabulary with quick visual aids.",
            "time": "3 min"
        },
        {
            "num": "Slide 3",
            "title": "Big Question",
            "visual": "Provocative question related to Why Some People Get Addicted",
            "say": "This is our driving question. By the end of class, you'll be able to answer it with evidence from your model.",
            "do": "Quick-write: Students write their initial hypothesis. Save to compare later.",
            "time": "3 min"
        },
        {
            "num": "Slide 4",
            "title": "LEVER Framework",
            "visual": "LEVER steps overview",
            "say": "We're going to build a computational model to investigate this system. Here are our five steps.",
            "do": "Preview each LEVER step. Emphasize that modeling reveals hidden patterns.",
            "time": "2 min"
        },
        {
            "num": "Slide 5",
            "title": "Activity 1: Components",
            "visual": "Component cards for sorting",
            "say": "What are the key parts of this system? Which ones come from outside, and which respond inside?",
            "do": "Guide sorting of external vs. internal components. Use think-pair-share for reasoning.",
            "time": "8 min"
        },
        {
            "num": "Slide 6",
            "title": "Activity 2: Connections",
            "visual": "Relationship arrows between components",
            "say": "Same drug, different people — why does one person walk away while another can't stop?",
            "do": "Students draw arrows showing +/- relationships. Discuss feedback loops if present.",
            "time": "8 min"
        },
        {
            "num": "Slide 7",
            "title": "Activity 3: Simulation",
            "visual": "Simulation results graphs",
            "say": "Now let's test our model. Run each scenario and record what happens.",
            "do": "Students run all scenarios, record predictions vs. observations. Discuss surprises.",
            "time": "10 min"
        },
        {
            "num": "Slide 8",
            "title": "Discoveries",
            "visual": "Key findings summary",
            "say": "So what did our model reveal? The difference is biology: genetics, brain development, and dopamine system dynamics....",
            "do": "Class discussion of discoveries. Compare initial hypotheses to model evidence.",
            "time": "5 min"
        },
        {
            "num": "Slide 9",
            "title": "STEM Challenge",
            "visual": "Engineering challenge: Design an Evidence-Based Prevention Program",
            "say": "Now apply what you've learned. Design a neuroscience-based prevention program replacing 'Just Say No' with real science....",
            "do": "Groups design solutions using model data. Present and evaluate designs.",
            "time": "12 min"
        }
    ],
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
    ]
}

L06 = {
    "id": "G12L1-L06",
    "title": "Why Is Antibiotic Resistance Getting Worse?",
    "subtitle": "Modeling Natural Selection, Mutation, and the Evolution of Resistant Bacteria",
    "ngss": "HS-LS4-2",
    "ngss_desc": "Construct an explanation based on evidence that the process of evolution primarily results from four factors: (1) the potential for a species to increase in number, (2) the heritable genetic variation of individuals in a species due to mutation and sexual reproduction, (3) competition for limited resources, and (4) the proliferation of those organisms that are better able to survive and reproduce in the environment.",
    "big_question": "Every year, 1.27 million people die worldwide from antibiotic-resistant infections — more than HIV/AIDS or malaria. If antibiotics are one of humanity\'s greatest inventions, how are microscopic bacteria outsmarting our best medicines, and are we heading toward a post-antibiotic apocalypse?",
    "objectives": [
        "Model how random mutations, selective pressure from antibiotics, bacterial reproduction rate, and gene transfer interact to drive the evolution of resistance",
        "Explain why incomplete antibiotic courses and agricultural overuse accelerate resistance evolution",
        "Predict how different antibiotic usage patterns affect the speed and extent of resistance development",
        "Analyze why antibiotic resistance is an evolutionary arms race that humans are currently losing"
    ],
    "vocabulary": [
        ("Antibiotic Resistance", "The ability of bacteria to survive and reproduce in the presence of an antibiotic that previously killed them — arising from random mutations that are naturally selected when antibiotics create selective pressure"),
        ("Selective Pressure", "An environmental factor that favors individuals with certain heritable traits over others — antibiotics create intense selective pressure by killing susceptible bacteria and leaving resistant mutants to reproduce without competition"),
        ("Horizontal Gene Transfer", "The process by which bacteria share genetic material, including resistance genes, directly between cells through conjugation, transformation, or transduction — allowing resistance to spread between species without reproduction"),
        ("Superbug", "A bacterial strain that has evolved resistance to multiple classes of antibiotics — such as MRSA, CRE, and XDR-TB — making infections extremely difficult or impossible to treat with existing drugs")
    ],
    "components": [
        ("Antibiotic Exposure", "The concentration, duration, and frequency of antibiotic use in a bacterial population — the primary selective pressure that drives resistance evolution by killing susceptible bacteria and favoring resistant mutants", True),
        ("Bacterial Population Diversity", "The natural genetic variation present in a bacterial colony due to random mutations — larger and more diverse populations have a higher probability of containing pre-existing resistance mutations", True),
        ("Mutation Rate", "The frequency at which random genetic changes occur during bacterial DNA replication — bacteria reproduce every 20-30 minutes, generating millions of mutations daily across a population", False),
        ("Resistance Gene Frequency", "The proportion of bacteria in the population carrying one or more resistance genes — increases rapidly under antibiotic selective pressure as susceptible bacteria die and resistant ones multiply", False),
        ("Treatment Effectiveness", "How well an antibiotic kills or inhibits the target bacterial population — decreases as Resistance Gene Frequency increases, eventually reaching zero when the population is fully resistant", False)
    ],
    "think_about_it": "A patient starts a 10-day antibiotic course but stops after 5 days because they feel better. At that point, the weakest bacteria are dead but the most resistant ones are still alive. What does your model predict about Resistance Gene Frequency in the surviving population?",
    "scenarios": [
        ("Full Treatment Course", "Set Antibiotic Exposure to the correct dose for the full prescribed duration — observe how Resistance Gene Frequency changes when nearly all bacteria are eliminated before resistant mutants can multiply"),
        ("Incomplete Course", "Set Antibiotic Exposure to stop at 50% of the prescribed duration — observe how surviving bacteria with partial resistance multiply without competition and increase Resistance Gene Frequency"),
        ("Agricultural Overuse", "Set Antibiotic Exposure to low, constant sub-therapeutic levels across a massive bacterial population — observe how this creates ideal conditions for gradual resistance evolution")
    ],
    "sim_scenarios": [
        ("Complete Treatment", "Antibiotic Exposure: Full dose, 10 days | Population Diversity: Moderate | Mutation Rate: Normal", "When antibiotics are taken correctly for the full duration, what happens to Resistance Gene Frequency over time?"),
        ("Stopped Early", "Antibiotic Exposure: Full dose, 5 days then stopped | Population Diversity: Moderate | Mutation Rate: Normal", "What happens to the bacterial population when treatment stops before all bacteria are killed?"),
        ("Farm Antibiotics", "Antibiotic Exposure: Low constant dose | Population Diversity: High | Mutation Rate: Normal", "How does constant low-level antibiotic exposure in livestock create resistant bacteria?")
    ],
    "discoveries": [
        "Incomplete antibiotic courses are one of the most powerful drivers of resistance — they kill weak bacteria and leave the most resistant ones to reproduce without competition",
        "Resistance evolution follows predictable natural selection: random mutation provides variation, antibiotics provide selective pressure, and differential survival increases resistance gene frequency",
        "Horizontal gene transfer allows resistance to jump between bacterial species, meaning resistance that evolves in harmless soil bacteria can transfer to deadly pathogens",
        "Sub-therapeutic antibiotic use in agriculture exposes trillions of bacteria to low-level selective pressure — the perfect training ground for resistance evolution on a massive scale"
    ],
    "answer": "Antibiotic resistance is getting worse because we are accelerating bacterial evolution through misuse. Antibiotics create intense selective pressure — every time bacteria are exposed, the susceptible ones die and any resistant mutants survive to reproduce without competition. Incomplete treatment courses are especially dangerous because they kill weak bacteria while leaving partially resistant ones alive to evolve further. Agricultural overuse exposes trillions of bacteria to constant low-level antibiotics, creating a massive evolutionary laboratory for resistance. Horizontal gene transfer allows resistance genes to spread between species, compounding the problem. We are heading toward a post-antibiotic era unless we dramatically change how we use these drugs — the bacteria are not outsmarting us; we are training them to defeat our own medicines.",
    "stem_title": "Design an Antibiotic Stewardship Campaign",
    "stem_mission": "Design an evidence-based public awareness and behavior change campaign that reduces antibiotic misuse in your community by targeting the specific behaviors that drive resistance evolution.",
    "stem_scenario": "Your county health department has documented a 40% increase in antibiotic-resistant infections over the past decade. Data shows the top three drivers are: patients demanding antibiotics for viral infections, patients not completing prescribed courses, and agricultural antibiotic overuse. Your team must design a multi-pronged campaign that changes these behaviors using evolutionary biology evidence.",
    "stem_questions": [
        "Which of the three misuse behaviors does your model show drives resistance fastest, and why?",
        "How can you explain natural selection to the general public without using jargon?",
        "What does your model predict about resistance trends if current misuse patterns continue for 20 more years?"
    ],
    "stem_design_qs": [
        "What specific behaviors does your campaign target and what evidence-based strategies do you use to change them?",
        "How does your campaign communicate evolutionary biology concepts in ways non-scientists can understand and act on?",
        "What model evidence supports your claim that these interventions will slow resistance evolution?",
        "How would you measure whether your campaign actually reduces antibiotic misuse and resistance rates?"
    ],
    "career": "Epidemiologists and antimicrobial resistance researchers track the spread of resistant infections and develop containment strategies, earning $60,000-$120,000/year. Infectious disease physicians specialize in treating resistant infections and designing antibiotic stewardship programs, earning $200,000-$350,000/year. Pharmaceutical microbiologists developing new antibiotics earn $75,000-$140,000/year.",
    "images": {
        "cover": ("G12L1-L06-cover.png", "A photorealistic close-up of diverse 17-18 year old students in a modern microbiology lab examining bacterial culture plates under dramatic lighting, with petri dishes showing zones of inhibition on the lab bench"),
        "landscape": ("G12L1-L06-landscape.png", "A diverse group of 17-18 year old students in a modern biology classroom examining diagrams of bacterial resistance mechanisms on a large smartboard, with microscopes and culture plates on lab tables"),
        "modeling": ("G12L1-L06-modeling.png", "Diverse 17-18 year old students working on laptops building computational models of bacterial population dynamics, classroom walls showing evolution and natural selection diagrams"),
        "discussion": ("G12L1-L06-discussion.png", "A teacher leading an animated discussion with diverse 17-18 year old students about antibiotic resistance, a graph showing rising resistance rates displayed on the smartboard"),
        "stem": ("G12L1-L06-stem.png", "Diverse 17-18 year old students designing public health campaign materials on whiteboards and laptops, with infographics about antibiotic stewardship visible")
    },
    "pre_assessment": [
        "Have you or someone you know ever stopped taking antibiotics early because you felt better? What do you think happens to the bacteria that survive?",
        "Why do you think antibiotics don\'t work against viruses like the common cold or flu?",
        "What does the term \'superbug\' mean to you, and why do you think they\'re becoming more common?",
        "Do you think bacteria \'learn\' to resist antibiotics, or is something else happening? Explain your thinking."
    ],
    "extend_components": [
        ("Horizontal Gene Transfer Rate", "The frequency at which bacteria exchange resistance genes through conjugation, transformation, and transduction — allows resistance to spread between unrelated species without reproduction"),
        ("Immune System Response", "The host\'s innate and adaptive immune defenses working alongside antibiotics — when immunity is compromised, even low levels of resistant bacteria can cause life-threatening infections"),
        ("Biofilm Formation", "Bacterial communities encased in a protective matrix that reduces antibiotic penetration by up to 1000x — bacteria in biofilms require much higher antibiotic concentrations to kill, promoting resistance development")
    ],
    "reflections": [
        "How does your model demonstrate that antibiotic resistance is an example of evolution by natural selection happening in real time?",
        "Why is stopping antibiotics early one of the most dangerous things a patient can do, according to your model?",
        "If bacteria evolve resistance to every antibiotic we create, is developing new antibiotics a long-term solution? What does your model suggest?",
        "How does agricultural antibiotic use connect to human health, even if people never directly consume those antibiotics?",
        "What are the ethical implications of wealthy countries having access to last-resort antibiotics while developing nations do not?"
    ],
    "dimensions": [
        ("Science Practice", "Constructing Explanations", "Students construct evidence-based explanations for how the four factors of evolution — population growth potential, heritable variation, competition, and differential survival — drive antibiotic resistance."),
        ("Disciplinary Core Idea", "LS4.B Natural Selection", "Natural selection acts on heritable variation in bacterial populations: antibiotic exposure selects for resistance mutations, and surviving bacteria reproduce to increase resistance gene frequency in subsequent generations."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify causal relationships between antibiotic usage patterns and the rate of resistance evolution, predicting how changes in human behavior affect bacterial population dynamics.")
    ],
    "cast_items": [
        "Construct an explanation for how natural selection drives antibiotic resistance using evidence from the model",
        "Predict how different antibiotic usage patterns affect resistance gene frequency over multiple bacterial generations",
        "Explain why horizontal gene transfer makes antibiotic resistance a community-level threat rather than an individual patient problem"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A patient takes antibiotics for 5 of the prescribed 10 days and feels better. Based on the natural selection model, what is the most likely composition of the remaining bacterial population and why does this matter?"),
        ("Constructed Response:", "Using your model, explain why giving low doses of antibiotics to healthy livestock to promote growth is considered one of the greatest threats to human health. Reference at least three model components and the mechanism of natural selection.")
    ],
    "background_intro": "Antibiotics transformed medicine after Alexander Fleming\'s discovery of penicillin in 1928, turning previously fatal infections into treatable conditions. But bacteria have been evolving resistance mechanisms for billions of years — antibiotic resistance genes have been found in 30,000-year-old permafrost bacteria. What\'s changed is the speed of evolution: human antibiotic use has created unprecedented selective pressure that accelerates resistance development from millennia to mere years.",
    "background_sections": [
        ("The Mechanics of Resistance", "Bacteria develop resistance through several mechanisms: enzymatic degradation (producing enzymes like beta-lactamase that break down antibiotics), target modification (altering the cellular structure an antibiotic targets), efflux pumps (actively pumping antibiotics out of the cell), and reduced permeability (changing membrane proteins to prevent antibiotic entry). These mechanisms arise from random mutations during DNA replication and are passed to daughter cells during binary fission."),
        ("The Role of Horizontal Gene Transfer", "Unlike humans, bacteria can share genetic material between unrelated species through three mechanisms: conjugation (direct cell-to-cell transfer via pili), transformation (uptake of free DNA from dead bacteria), and transduction (transfer via bacteriophage viruses). This means a resistance gene that evolves in a harmless soil bacterium can transfer to a deadly pathogen. Plasmids — small circular DNA molecules — often carry multiple resistance genes simultaneously, creating multi-drug resistance in a single transfer event."),
        ("Agricultural Antibiotics: The Hidden Driver", "Approximately 73% of all antibiotics sold globally are used in livestock — not to treat sick animals, but as growth promoters at sub-therapeutic doses. This practice exposes trillions of bacteria to constant low-level selective pressure, the perfect conditions for gradual resistance evolution. Resistant bacteria then spread to humans through direct contact, food supply, water runoff, and airborne transmission. The WHO has called for a complete ban on growth-promotion antibiotics, but economic interests have slowed policy changes."),
        ("The Post-Antibiotic Threat", "The WHO has warned that without urgent action, we face a post-antibiotic era where common infections and minor injuries can once again kill. The development pipeline for new antibiotics is nearly empty because pharmaceutical companies find it unprofitable — a new antibiotic takes 10-15 years and $1 billion to develop but can become obsolete in 2-3 years. Currently, 700,000 people die annually from resistant infections, projected to reach 10 million by 2050 — surpassing cancer as a cause of death.")
    ],
    "lever_L": "Students identify antibiotic exposure, bacterial population diversity, mutation rate, resistance gene frequency, and treatment effectiveness as the key components of the antibiotic resistance system.",
    "lever_E": "Students determine that antibiotic exposure creates selective pressure favoring resistant mutations, that incomplete courses and low doses accelerate resistance, and that treatment effectiveness decreases as resistance gene frequency rises.",
    "lever_V": "Students build a computational model showing how antibiotic usage patterns interact with bacterial reproduction and mutation to drive the evolution of resistance over multiple generations.",
    "lever_Ev": "Students run full treatment, incomplete course, and agricultural overuse scenarios to test predictions about which behaviors drive resistance evolution fastest.",
    "lever_R": "Students add horizontal gene transfer, immune response, or biofilm formation to explore how real-world complexity affects resistance dynamics and treatment outcomes.",
    "slides_guide": [
        {
            "num": "Slide 1",
            "title": "Cover",
            "visual": "Title slide with compelling image related to Why Is Antibiotic Resistance Getting Worse?",
            "say": "Every year, 1.27 million people die from infections that antibiotics can no longer treat. Today we investigate why.",
            "do": "Show cover image. Ask: Has anyone ever stopped taking antibiotics early? Why?",
            "time": "2 min"
        },
        {
            "num": "Slide 2",
            "title": "Learning Objectives",
            "visual": "Learning goals and vocabulary terms",
            "say": "Here\'s what you\'ll be able to do by the end of today\'s lesson — model how bacteria evolve resistance in real time.",
            "do": "Have students read objectives aloud. Pre-teach vocabulary with visual aids showing bacterial structures.",
            "time": "3 min"
        },
        {
            "num": "Slide 3",
            "title": "Big Question",
            "visual": "Provocative question with image of resistant bacteria vs. antibiotics",
            "say": "Are we heading toward a world where a simple cut could kill you because no antibiotic works? Let\'s find out.",
            "do": "Quick-write: Students write their initial hypothesis about why resistance is increasing. Save to compare later.",
            "time": "3 min"
        },
        {
            "num": "Slide 4",
            "title": "LEVER Framework",
            "visual": "LEVER steps overview",
            "say": "We\'re going to model evolution by natural selection — happening right now, in real time, inside your body.",
            "do": "Preview each LEVER step. Emphasize that this is evolution you can observe in days, not millions of years.",
            "time": "2 min"
        },
        {
            "num": "Slide 5",
            "title": "Activity 1: Components",
            "visual": "Component cards for sorting — antibiotic exposure, population diversity, mutation rate, resistance frequency, treatment effectiveness",
            "say": "What are the key parts of this evolutionary system? Which inputs come from outside the bacteria?",
            "do": "Guide sorting of external vs. internal components. Use think-pair-share for reasoning about which factors bacteria control vs. which humans control.",
            "time": "8 min"
        },
        {
            "num": "Slide 6",
            "title": "Activity 2: Connections",
            "visual": "Relationship arrows between components",
            "say": "When Antibiotic Exposure increases but the course is incomplete, what happens to the surviving population\'s Resistance Gene Frequency?",
            "do": "Students draw arrows showing +/- relationships. Discuss the feedback loop: more resistance leads to less effective treatment leads to more antibiotic use.",
            "time": "8 min"
        },
        {
            "num": "Slide 7",
            "title": "Activity 3: Simulation",
            "visual": "Simulation results showing bacterial population changes over time",
            "say": "Now let\'s test our model. Run each scenario — full course, incomplete course, and farm antibiotics — and record what happens.",
            "do": "Students run all scenarios, record predictions vs. observations. Discuss why incomplete courses are so dangerous.",
            "time": "10 min"
        },
        {
            "num": "Slide 8",
            "title": "Discoveries",
            "visual": "Key findings summary with resistance evolution timeline",
            "say": "Our model reveals that WE are the selective pressure. Every time we misuse antibiotics, we train bacteria to defeat them.",
            "do": "Class discussion of discoveries. Compare initial hypotheses to model evidence. Emphasize this is evolution by natural selection in action.",
            "time": "5 min"
        },
        {
            "num": "Slide 9",
            "title": "STEM Challenge",
            "visual": "Engineering challenge: Design an Antibiotic Stewardship Campaign",
            "say": "Now apply what you\'ve learned. Your county needs a campaign that changes the specific behaviors driving resistance.",
            "do": "Groups design evidence-based campaigns targeting the three main drivers. Present and evaluate using model data.",
            "time": "12 min"
        }
    ],
    "sort_reasoning": "Antibiotic Exposure and Bacterial Population Diversity are external components because they represent inputs that exist before the evolutionary process begins — one is determined by human medical/agricultural practices and the other by the natural variation in bacterial colonies. Mutation Rate, Resistance Gene Frequency, and Treatment Effectiveness are internal because they are properties that emerge from how the bacterial population responds to selective pressure over generations.",
    "relationships": [
        ("Antibiotic Exposure to Resistance Gene Frequency", "POSITIVE (+)", "Antibiotic exposure creates selective pressure that kills susceptible bacteria and allows resistant mutants to survive and reproduce, increasing the proportion of resistance genes in the population."),
        ("Bacterial Population Diversity to Mutation Rate", "POSITIVE (+)", "More diverse populations have greater genetic variation, increasing the probability that resistance-conferring mutations already exist or will arise through recombination."),
        ("Mutation Rate to Resistance Gene Frequency", "POSITIVE (+)", "Higher mutation rates increase the probability of resistance mutations arising in each generation, providing more raw material for natural selection to act upon."),
        ("Resistance Gene Frequency to Treatment Effectiveness", "NEGATIVE (-)", "As the proportion of resistant bacteria increases, the antibiotic kills fewer and fewer organisms, reducing treatment effectiveness until it reaches zero for fully resistant populations.")
    ],
    "sim_answers": [
        ("Full Treatment Course", "With complete antibiotic exposure at proper dosage, the model shows that nearly all bacteria — including partially resistant ones — are eliminated before they can reproduce. Resistance Gene Frequency stays low because the few surviving highly resistant mutants face competition from the recovering microbiome and immune system. This demonstrates why completing the full course is critical."),
        ("Incomplete Course", "When treatment stops at 50%, the model shows a dramatic spike in Resistance Gene Frequency. The weakest bacteria are dead, but partially resistant ones survive without competition. They reproduce rapidly, and within a few generations, the population is dominated by resistant organisms. The next time this person needs antibiotics, the same drug may not work."),
        ("Agricultural Overuse", "Constant low-level exposure creates the most dangerous scenario in the model: gentle but persistent selective pressure across a massive population. Resistance Gene Frequency climbs steadily because sub-therapeutic doses kill only the most susceptible bacteria while leaving billions of partially resistant ones to gradually evolve stronger resistance over time.")
    ],
    "reflection_exemplars": [
        ("Is developing new antibiotics enough to solve the resistance crisis?", "Our model shows that developing new antibiotics alone is a losing strategy — it\'s an arms race where bacteria evolve faster than we can develop new drugs. A new antibiotic takes 10-15 years to develop, but resistance can emerge in 2-3 years. The model demonstrates that reducing selective pressure (through better stewardship, completing courses, and eliminating agricultural overuse) is more effective than simply adding new weapons. We need both, but prevention of resistance must be the priority."),
        ("Why does agricultural antibiotic use affect human health?", "The model reveals that sub-therapeutic doses in agriculture create a massive evolutionary laboratory — trillions of bacteria under constant gentle selective pressure. Horizontal gene transfer means resistance genes that evolve in animal gut bacteria can transfer to human pathogens through the food chain, water runoff, and environmental contact. The agricultural setting amplifies the total pool of resistance genes in the environment, which inevitably flows into human medicine.")
    ],
    "stem_intro": "Present the challenge: Your county health department has documented a 40% increase in antibiotic-resistant infections. Your team must design a multi-pronged campaign targeting the three main drivers of resistance: patients demanding antibiotics for viral infections, patients not completing courses, and agricultural overuse. Use your model data to prioritize which behaviors to target first.",
    "stem_concepts": [
        ("Antibiotic Stewardship", "A coordinated program to improve and measure the appropriate use of antibiotics — including selecting the right drug, correct dose, and proper duration. Hospital stewardship programs have reduced resistant infections by 20-30% where implemented."),
        ("One Health Approach", "A framework that recognizes that human health, animal health, and environmental health are interconnected. Antibiotic resistance in livestock directly affects human medicine, so solutions must address all three domains simultaneously."),
        ("Surveillance and Tracking", "Systematic monitoring of resistance patterns across regions and populations to detect emerging threats early. The CDC\'s Antibiotic Resistance Threats Report tracks the most dangerous resistant organisms and guides intervention priorities.")
    ],
    "stem_eval": [
        ("Expert (4)", "Campaign targets all three drivers with specific evidence-based interventions, communicates evolution clearly to non-scientists, uses model data to justify priorities, and includes measurable outcomes"),
        ("Proficient (3)", "Campaign addresses major drivers with reasonable interventions and some reference to evolutionary model evidence"),
        ("Developing (2)", "Campaign identifies some drivers but interventions are vague or not grounded in evolutionary biology evidence"),
        ("Beginning (1)", "Campaign is incomplete, scientifically inaccurate, or does not connect antibiotic misuse to evolutionary mechanisms")
    ],
    "support": [
        "Provide a visual timeline showing how a bacterial population changes during complete vs. incomplete antibiotic treatment",
        "Use a color-coded population diagram: green = susceptible, yellow = partially resistant, red = fully resistant, showing selection in action",
        "Sentence frames: \'When antibiotic exposure ___, the resistant bacteria survive because ___, which causes Resistance Gene Frequency to ___\'"
    ],
    "extensions": [
        "Research the discovery pipeline for new antibiotics — why have pharmaceutical companies largely abandoned antibiotic development, and what economic solutions have been proposed?",
        "Investigate phage therapy as an alternative to antibiotics — how does using viruses that specifically infect bacteria potentially avoid the resistance problem?",
        "Analyze the case of colistin resistance (the MCR-1 gene) — how did resistance to humanity\'s last-resort antibiotic emerge in Chinese pig farms and spread globally within years?"
    ],
    "cross_curr": [
        ("Math", "Calculate bacterial population growth using exponential functions: if one resistant bacterium divides every 20 minutes, how many resistant bacteria exist after 24 hours? Graph resistance gene frequency as a function of antibiotic selection pressure."),
        ("ELA", "Write a persuasive letter to a state legislator arguing for legislation to ban sub-therapeutic antibiotics in livestock, using evolutionary biology evidence from your model to support your position"),
        ("History", "Research the history of antibiotic development from Fleming\'s penicillin to modern last-resort drugs. Create a timeline showing when each major antibiotic was introduced and when resistance was first detected — what pattern emerges?")
    ],
    "misconceptions": [
        ("Bacteria become resistant by adapting to antibiotics like building immunity", "Bacteria don\'t \'learn\' or \'adapt\' to antibiotics the way humans build immunity to diseases. Resistance arises from random mutations that happen to provide a survival advantage when antibiotics are present. Natural selection favors these pre-existing mutants — the antibiotic doesn\'t cause the mutation, it selects for it. This is a critical distinction between Lamarckian (acquired traits) and Darwinian (natural selection) evolution.", "Demonstrate with a thought experiment: If you painted a room with poison paint, the surviving cockroaches wouldn\'t be ones that \'learned\' to resist poison — they\'d be ones that happened to already have genetic resistance. The paint selected for resistance that already existed."),
        ("Antibiotic resistance only affects people who take antibiotics", "Resistant bacteria spread between people, animals, and environments regardless of individual antibiotic use. A person who has never taken an antibiotic can be infected by MRSA from a gym locker room, resistant E. coli from contaminated food, or resistant tuberculosis from a cough. Resistance is a community-level threat driven by total population antibiotic use, not an individual consequence.", "Ask: If your neighbor\'s overuse of antibiotics creates resistant bacteria that spread to you, is antibiotic misuse a personal choice or a public health issue? Compare to secondhand smoke."),
        ("We can always develop new antibiotics to stay ahead of resistance", "The antibiotic development pipeline is nearly empty. Only 12 new antibiotics have been approved since 2017, and most are modifications of existing classes rather than truly novel mechanisms. Development takes 10-15 years and costs over $1 billion, but a new antibiotic generates less revenue than drugs for chronic conditions because it\'s used short-term and doctors are told to use it sparingly. Meanwhile, bacteria can evolve resistance in 2-3 years. We cannot innovate our way out of this crisis without also reducing misuse.", "Compare the development timeline (10-15 years per new drug) with the resistance timeline (2-3 years). Draw a graph showing both trends — where do the lines cross? This visual makes the math of the problem unmistakable.")
    ]
}

L07 = {
    "id": "G12L1-L07",
    "title": "Can We Edit the Human Genome?",
    "subtitle": "Modeling CRISPR Gene Editing, Inheritance, and the Ethics of Genetic Engineering",
    "ngss": "HS-LS3-1",
    "ngss_desc": "Ask questions to clarify relationships about the role of DNA and chromosomes in coding the instructions for characteristic traits passed from parents to offspring.",
    "big_question": "CRISPR technology lets scientists edit DNA like a word processor edits text — cutting out disease-causing genes and replacing them with healthy versions. If we can cure genetic diseases before birth, should we? And where is the line between healing and designing \'perfect\' humans?",
    "objectives": [
        "Model how CRISPR-Cas9 uses guide RNA to locate, cut, and replace specific DNA sequences in the genome",
        "Explain how edited genes are inherited and how germline vs. somatic editing differ in their generational impact",
        "Predict the biological outcomes of gene editing for single-gene disorders vs. complex polygenic traits",
        "Analyze the ethical tensions between curing genetic disease and enabling genetic enhancement or eugenics"
    ],
    "vocabulary": [
        ("CRISPR-Cas9", "A gene-editing tool adapted from bacterial immune systems that uses a guide RNA to direct the Cas9 protein to a specific DNA sequence, where it cuts both strands — allowing scientists to delete, replace, or insert genetic material with unprecedented precision"),
        ("Guide RNA", "A short RNA molecule engineered to match a specific DNA target sequence — it directs the Cas9 protein to the exact location in the genome where the edit should occur, providing the specificity that makes CRISPR revolutionary"),
        ("Germline Editing", "Genetic modifications made to sperm, eggs, or embryos that are inherited by all future generations — the most powerful and most controversial application of CRISPR because changes are permanent and affect people who cannot consent"),
        ("Off-Target Effects", "Unintended cuts or edits at DNA locations similar but not identical to the target sequence — the primary safety concern with CRISPR, as even small unintended changes could activate cancer genes or disrupt essential functions")
    ],
    "components": [
        ("Guide RNA Specificity", "How precisely the guide RNA matches the intended DNA target — higher specificity means fewer off-target effects, but perfect specificity is difficult to achieve because the human genome contains many similar sequences", True),
        ("Target Gene Location", "The specific position in the genome where the edit is intended — some locations are easier to access and edit than others, and the surrounding DNA context affects both editing efficiency and off-target risk", True),
        ("Editing Efficiency", "The percentage of cells in which the CRISPR system successfully makes the intended edit — varies from 10-90% depending on guide RNA design, delivery method, and target accessibility", False),
        ("Off-Target Mutation Rate", "The frequency of unintended edits at non-target locations in the genome — even rates as low as 0.1% are concerning because off-target cuts in tumor suppressor genes could cause cancer", False),
        ("Therapeutic Outcome", "The overall health benefit or harm resulting from the gene edit — determined by the balance between successful on-target editing and harmful off-target effects across all edited cells", False)
    ],
    "think_about_it": "A scientist designs a guide RNA to fix a mutation causing sickle cell disease. The guide RNA has 99.5% specificity — sounds nearly perfect. But the human genome has 3.2 billion base pairs. What does your model predict about Off-Target Mutation Rate across the entire genome?",
    "scenarios": [
        ("High-Specificity Single Gene Edit", "Set Guide RNA Specificity to maximum with a well-characterized Target Gene Location — observe high Editing Efficiency, low Off-Target Mutation Rate, and strong Therapeutic Outcome"),
        ("Low-Specificity Editing", "Reduce Guide RNA Specificity to moderate levels — observe how Off-Target Mutation Rate increases and Therapeutic Outcome becomes uncertain as unintended edits accumulate"),
        ("Complex Polygenic Trait", "Attempt to edit multiple genes simultaneously for a trait controlled by many genes — observe how Editing Efficiency drops and Off-Target Mutation Rate multiplies with each additional target")
    ],
    "sim_scenarios": [
        ("Sickle Cell Cure", "Guide RNA Specificity: High | Target: Single gene (HBB) | Delivery: Somatic cells", "When CRISPR targets a single well-known gene with high specificity, what does the model predict for Therapeutic Outcome?"),
        ("Multiple Gene Edit", "Guide RNA Specificity: Moderate | Target: 5 genes simultaneously | Delivery: Somatic cells", "What happens to Off-Target Mutation Rate when you try to edit multiple genes at once?"),
        ("Germline Enhancement", "Guide RNA Specificity: High | Target: Multiple trait genes | Delivery: Embryo (germline)", "What are the risks when gene edits in an embryo will be inherited by all future descendants?")
    ],
    "discoveries": [
        "CRISPR is highly effective for single-gene disorders like sickle cell disease where one specific mutation can be precisely targeted with well-designed guide RNA",
        "Off-target effects are the critical safety limitation — even with 99.9% specificity, the sheer size of the genome means unintended cuts are statistically inevitable across millions of cells",
        "Editing multiple genes simultaneously for complex traits multiplies both the difficulty and the risk — each additional target increases the probability of harmful off-target effects",
        "Germline editing raises unique concerns because edits are permanent and heritable — mistakes cannot be undone and will propagate through all future generations of that lineage"
    ],
    "answer": "Yes, we can edit the human genome — and we already have. In 2023, the FDA approved the first CRISPR-based therapy for sickle cell disease, marking a new era in medicine. CRISPR-Cas9 works by using a guide RNA to direct a molecular scissors (Cas9) to a precise location in the DNA, where it cuts and allows the cell\'s repair machinery to fix or replace the gene. For single-gene diseases, this is revolutionary. But the technology has real limitations: off-target effects can cause unintended mutations, editing multiple genes is exponentially more complex, and germline edits affect future generations who cannot consent. The line between healing and enhancement is the great ethical challenge of our generation.",
    "stem_title": "Design a Gene Therapy Ethics Framework",
    "stem_mission": "Design a comprehensive ethical framework that a hospital genetics board could use to evaluate whether a proposed CRISPR gene-editing treatment should be approved, considering both scientific evidence and societal implications.",
    "stem_scenario": "A genetics company has developed a CRISPR treatment that could eliminate the gene for Huntington\'s disease in embryos — a fatal neurodegenerative disorder with no cure. But the same technology could potentially be used to select for traits like height, intelligence, or eye color. Your hospital\'s ethics board needs a decision framework that distinguishes between therapeutic and enhancement uses of gene editing.",
    "stem_questions": [
        "What scientific criteria from your model should determine whether a gene edit is safe enough to approve?",
        "Where should the ethical line be drawn between treating disease and enhancing traits, and who decides?",
        "What does your model reveal about the technical limitations that should constrain what gene edits are attempted?"
    ],
    "stem_design_qs": [
        "What specific criteria does your framework use to evaluate whether an edit is \'therapeutic\' vs. \'enhancement\'?",
        "How does your framework account for the scientific uncertainty of off-target effects when making approval decisions?",
        "What safeguards does your framework include for germline edits that will affect future generations?",
        "How does your framework address equity — preventing a future where gene editing creates biological inequality between rich and poor?"
    ],
    "career": "Genetic counselors help families understand genetic testing results and make informed decisions about treatments including gene therapy, earning $80,000-$110,000/year. Bioethicists specializing in genetic technology work at hospitals, universities, and policy organizations, earning $60,000-$130,000/year. CRISPR researchers in biotechnology companies earn $90,000-$180,000/year.",
    "images": {
        "cover": ("G12L1-L07-cover.png", "A photorealistic image of diverse 17-18 year old students in a modern genetics lab examining DNA models and CRISPR diagrams on a holographic display, dramatic lighting emphasizing the futuristic technology"),
        "landscape": ("G12L1-L07-landscape.png", "A diverse group of 17-18 year old students in a modern biology classroom with DNA double helix models on desks, a large smartboard showing CRISPR mechanism diagrams, natural light"),
        "modeling": ("G12L1-L07-modeling.png", "Diverse 17-18 year old students working on laptops building computational models of gene editing efficiency, classroom walls showing genetics and CRISPR infographics"),
        "discussion": ("G12L1-L07-discussion.png", "A teacher facilitating a Socratic seminar with diverse 17-18 year old students debating gene editing ethics, students showing passionate engagement, ethics guidelines visible on a poster"),
        "stem": ("G12L1-L07-stem.png", "Diverse 17-18 year old students collaborating around a table with documents, creating an ethics framework flowchart on a large whiteboard, modern classroom setting")
    },
    "pre_assessment": [
        "What do you already know about CRISPR or gene editing? Where did you learn about it?",
        "If scientists could edit a gene to prevent a fatal disease in an unborn child, do you think they should? Why or why not?",
        "What\'s the difference between curing a disease and enhancing a trait? Is the line always clear?",
        "Who should decide what gene edits are allowed — scientists, governments, parents, or society as a whole?"
    ],
    "extend_components": [
        ("Delivery Method Efficiency", "How effectively the CRISPR components are delivered into target cells — viral vectors, lipid nanoparticles, and electroporation each have different efficiency rates and tissue specificity that affect overall therapeutic outcome"),
        ("Mosaicism Risk", "The probability that only some cells in an organism are successfully edited while others retain the original gene — creates organisms with mixed genetic populations, reducing therapeutic effectiveness"),
        ("Epigenetic Disruption", "The risk that DNA cuts or insertions alter the epigenetic marks (methylation, histone modification) near the target site, changing gene expression patterns in ways that may not be apparent for years")
    ],
    "reflections": [
        "How does your model help explain why CRISPR works well for single-gene diseases but struggles with complex traits like intelligence or height?",
        "What does the Off-Target Mutation Rate reveal about why we should be cautious even when editing seems highly precise?",
        "Should germline editing be banned, regulated, or left to individual families? What evidence from your model informs your position?",
        "If gene editing becomes affordable, how might it affect social inequality? What if only wealthy families can access genetic enhancements?",
        "How does the precautionary principle apply to a technology that could cure devastating diseases but also enable genetic discrimination?"
    ],
    "dimensions": [
        ("Science Practice", "Asking Questions and Defining Problems", "Students ask clarifying questions about the relationships between DNA structure, gene function, and how CRISPR-mediated changes to DNA sequences affect protein production and trait expression."),
        ("Disciplinary Core Idea", "LS3.A Inheritance of Traits", "DNA sequences code for proteins that determine traits; CRISPR allows modification of these sequences, and whether changes are in somatic or germline cells determines whether modifications are inherited by offspring."),
        ("Crosscutting Concept", "Structure and Function", "Students connect the molecular structure of DNA, guide RNA, and Cas9 protein to the function of precise gene editing, understanding how structural specificity determines functional accuracy.")
    ],
    "cast_items": [
        "Model how CRISPR-Cas9 uses guide RNA specificity to target and edit specific DNA sequences with varying degrees of accuracy",
        "Predict therapeutic outcomes based on the interaction of editing efficiency and off-target mutation rate for different types of genetic modifications",
        "Explain why germline edits have different ethical and biological implications than somatic cell edits"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A CRISPR guide RNA with 99.8% specificity is used to edit embryonic cells. Given that the human genome contains 3.2 billion base pairs, approximately how many potential off-target sites could be affected, and why does this matter for germline editing?"),
        ("Constructed Response:", "Using your model, compare the predicted Therapeutic Outcome for editing a single gene causing cystic fibrosis versus editing the 20+ genes associated with height. Explain why the model predicts dramatically different outcomes and what this reveals about the limits of gene editing for complex traits.")
    ],
    "background_intro": "CRISPR-Cas9 is arguably the most revolutionary biological technology since the discovery of DNA\'s structure. Adapted from a natural immune system that bacteria use to defend against viruses, CRISPR allows scientists to edit any organism\'s DNA with a precision that was unimaginable a decade ago. The technology is transforming medicine, agriculture, and our fundamental understanding of genetics — while raising ethical questions that humanity has never faced before.",
    "background_sections": [
        ("How CRISPR Works", "The CRISPR-Cas9 system has two key components: a guide RNA (gRNA) that is designed to match a specific 20-nucleotide DNA target sequence, and the Cas9 protein that acts as molecular scissors. The gRNA leads Cas9 to the correct location in the genome, where Cas9 cuts both strands of the DNA double helix. The cell\'s natural repair mechanisms then fix the break — either by joining the cut ends (often disabling the gene) or by using a provided DNA template to insert a new sequence. This allows scientists to delete harmful mutations, correct disease-causing variants, or insert entirely new genetic sequences."),
        ("Current Medical Applications", "CRISPR has already produced FDA-approved therapies. Casgevy (2023) treats sickle cell disease and transfusion-dependent beta-thalassemia by editing patients\' own blood stem cells to reactivate fetal hemoglobin production. Clinical trials are underway for CRISPR treatments of cancer (editing immune cells to better attack tumors), hereditary blindness (Leber congenital amaurosis), HIV (disabling the CCR5 receptor), and dozens of other genetic conditions. Most current applications use somatic cell editing — modifying the patient\'s cells without affecting their children."),
        ("The Germline Editing Controversy", "In 2018, Chinese scientist He Jiankui shocked the world by announcing he had used CRISPR to edit human embryos — twin girls born with modified CCR5 genes intended to confer HIV resistance. The scientific community condemned the experiment as premature, poorly designed, and ethically unjustifiable. The girls may face unknown health consequences from off-target effects. The incident crystallized the debate: germline edits are permanent, heritable, and affect individuals who cannot consent. Most countries have banned germline editing, but enforcement is inconsistent."),
        ("The Enhancement vs. Therapy Debate", "The most contentious ethical frontier is the line between therapy (fixing a disease-causing gene) and enhancement (improving a normal trait). Curing Huntington\'s disease seems clearly therapeutic. But what about editing genes associated with higher intelligence, greater muscle mass, or longer lifespan? Most traits are polygenic — influenced by dozens or hundreds of genes interacting with environment — making enhancement both technically difficult and ethically fraught. Critics warn of a new eugenics where wealthy families purchase genetic advantages, creating biological inequality between economic classes.")
    ],
    "lever_L": "Students identify guide RNA specificity, target gene location, editing efficiency, off-target mutation rate, and therapeutic outcome as the key components of the CRISPR gene-editing system.",
    "lever_E": "Students determine that guide RNA specificity is the primary determinant of editing accuracy, that off-target effects increase with lower specificity and multiple targets, and that therapeutic outcome depends on the balance of on-target success and off-target harm.",
    "lever_V": "Students build a computational model showing how guide RNA design, target complexity, and cellular repair mechanisms interact to determine the safety and effectiveness of gene edits.",
    "lever_Ev": "Students run single-gene, multi-gene, and germline editing scenarios to test predictions about when CRISPR is safe and effective versus when risks outweigh benefits.",
    "lever_R": "Students add delivery method efficiency, mosaicism risk, or epigenetic disruption to explore how real-world biological complexity affects gene-editing outcomes beyond the simplified model.",
    "slides_guide": [
        {
            "num": "Slide 1",
            "title": "Cover",
            "visual": "Title slide with compelling image related to Can We Edit the Human Genome?",
            "say": "What if you could rewrite the code of life itself? Today we investigate the most powerful biological technology ever created.",
            "do": "Show cover image. Ask: What have you heard about CRISPR or gene editing? Quick share-out.",
            "time": "2 min"
        },
        {
            "num": "Slide 2",
            "title": "Learning Objectives",
            "visual": "Learning goals and vocabulary terms with DNA/CRISPR visuals",
            "say": "Here\'s what you\'ll be able to do by the end of today — model how CRISPR edits DNA and evaluate when it should be used.",
            "do": "Have students read objectives aloud. Pre-teach vocabulary with molecular animation or diagram of CRISPR mechanism.",
            "time": "3 min"
        },
        {
            "num": "Slide 3",
            "title": "Big Question",
            "visual": "Provocative question with split image: disease cure vs. designer baby",
            "say": "CRISPR can cure sickle cell disease AND theoretically enhance intelligence. Should we use it for both? Neither? Where\'s the line?",
            "do": "Quick-write: Students write their initial position on where the line should be drawn. Save to revisit after modeling.",
            "time": "3 min"
        },
        {
            "num": "Slide 4",
            "title": "LEVER Framework",
            "visual": "LEVER steps overview",
            "say": "We\'re going to model the actual molecular mechanism of CRISPR to understand both its power and its limitations.",
            "do": "Preview each LEVER step. Emphasize that understanding the biology is essential for informed ethical reasoning.",
            "time": "2 min"
        },
        {
            "num": "Slide 5",
            "title": "Activity 1: Components",
            "visual": "Component cards — guide RNA specificity, target gene location, editing efficiency, off-target rate, therapeutic outcome",
            "say": "What are the key parts of this gene-editing system? What inputs do scientists control, and what emerges from the biology?",
            "do": "Guide sorting of external vs. internal components. Discuss: What can scientists design, and what does biology determine?",
            "time": "8 min"
        },
        {
            "num": "Slide 6",
            "title": "Activity 2: Connections",
            "visual": "Relationship arrows between CRISPR components",
            "say": "If Guide RNA Specificity decreases even slightly, what happens to Off-Target Mutation Rate across 3.2 billion base pairs?",
            "do": "Students draw arrows showing +/- relationships. Discuss why the genome\'s massive size amplifies even tiny error rates.",
            "time": "8 min"
        },
        {
            "num": "Slide 7",
            "title": "Activity 3: Simulation",
            "visual": "Simulation results comparing single-gene vs. multi-gene editing outcomes",
            "say": "Run each scenario. Compare what happens when you edit one gene precisely vs. multiple genes simultaneously.",
            "do": "Students run all scenarios, record predictions vs. observations. Discuss why complex traits are so much harder to edit safely.",
            "time": "10 min"
        },
        {
            "num": "Slide 8",
            "title": "Discoveries",
            "visual": "Key findings summary — what CRISPR can and cannot safely do",
            "say": "Our model reveals both the extraordinary promise and the real limitations of gene editing technology.",
            "do": "Class discussion of discoveries. Revisit initial positions — has the model evidence changed anyone\'s thinking about where the line should be?",
            "time": "5 min"
        },
        {
            "num": "Slide 9",
            "title": "STEM Challenge",
            "visual": "Engineering challenge: Design a Gene Therapy Ethics Framework",
            "say": "Now apply both the science AND the ethics. Your hospital needs a framework for deciding which gene edits to approve.",
            "do": "Groups design ethics frameworks using model data to set scientific criteria. Present and debate frameworks.",
            "time": "12 min"
        }
    ],
    "sort_reasoning": "Guide RNA Specificity and Target Gene Location are external components because they represent inputs that scientists design and select before the editing process begins — the guide RNA is engineered in the lab and the target is chosen based on the disease. Editing Efficiency, Off-Target Mutation Rate, and Therapeutic Outcome are internal because they emerge from the biological interactions between the CRISPR system and the cell\'s DNA and repair machinery.",
    "relationships": [
        ("Guide RNA Specificity to Editing Efficiency", "POSITIVE (+)", "Higher guide RNA specificity means the CRISPR system binds more reliably to the intended target, increasing the percentage of cells where the correct edit is made."),
        ("Guide RNA Specificity to Off-Target Mutation Rate", "NEGATIVE (-)", "Higher specificity reduces the chance of the guide RNA binding to similar but incorrect DNA sequences elsewhere in the genome, decreasing off-target mutations."),
        ("Off-Target Mutation Rate to Therapeutic Outcome", "NEGATIVE (-)", "More off-target mutations increase the risk of harmful unintended effects — including potential activation of oncogenes — which decreases overall therapeutic benefit."),
        ("Editing Efficiency to Therapeutic Outcome", "POSITIVE (+)", "Higher editing efficiency means more cells carry the corrected gene, producing more functional protein and greater therapeutic benefit for the patient.")
    ],
    "sim_answers": [
        ("High-Specificity Single Gene Edit", "With maximum Guide RNA Specificity targeting a well-characterized gene like HBB (sickle cell), the model shows high Editing Efficiency (70-90%), very low Off-Target Mutation Rate, and strong Therapeutic Outcome. This represents the best-case scenario for CRISPR and mirrors the success of approved sickle cell therapies."),
        ("Complex Polygenic Trait", "When attempting to edit 5+ genes simultaneously, the model shows dramatically different results. Each additional guide RNA introduces its own off-target risk, and the cumulative Off-Target Mutation Rate multiplies. Editing Efficiency for all targets simultaneously drops below 10%, and Therapeutic Outcome becomes unpredictable. This is why \'designer babies\' for complex traits remain science fiction, not science.")
    ],
    "reflection_exemplars": [
        ("Should germline editing ever be allowed?", "This requires balancing immense potential benefit against irreversible risk. Our model shows that for severe single-gene diseases like Huntington\'s — which is fatal, has no cure, and is caused by one well-characterized mutation — the Therapeutic Outcome of germline editing could be transformative: an entire lineage freed from the disease. But the model also shows that Off-Target Mutation Rate, however small, creates risks that would propagate through all future generations. The precautionary principle suggests extreme caution, but an absolute ban condemns families to preventable suffering. A regulated, transparent system with extensive safety testing may be the most ethical path."),
        ("Could gene editing create a genetic class system?", "If gene editing becomes commercially available, our model suggests that the most effective edits — those with high Guide RNA Specificity and proven safety — will initially be extremely expensive. Wealthy families could access genetic enhancements (disease resistance, cognitive advantages) that poor families cannot. Over generations, this could create biological inequality reinforcing economic inequality. The model\'s technical data shows that safe, effective editing is possible for single-gene traits, making this scenario plausible. Equitable access policies would need to be established before the technology becomes widespread.")
    ],
    "stem_intro": "Present the challenge: A genetics company has applied to your hospital to begin offering CRISPR editing for Huntington\'s disease in embryos. The same technology could be used for trait selection. Your ethics board must develop a decision framework that approves beneficial applications while preventing misuse — and your criteria must be grounded in both scientific evidence and ethical principles.",
    "stem_concepts": [
        ("Informed Consent in Genetics", "A foundational bioethics principle requiring that patients fully understand the risks, benefits, and alternatives before agreeing to treatment. Germline editing complicates consent because the edited individual (future child) cannot participate in the decision, and effects extend to all their descendants."),
        ("Genetic Determinism vs. Gene-Environment Interaction", "The misconception that genes alone determine traits. In reality, most traits result from complex interactions between multiple genes and environmental factors. This means editing \'intelligence genes\' would have unpredictable outcomes because the same genetic variant may produce different effects in different environments."),
        ("Precautionary Principle", "When an action raises threats of harm, precautionary measures should be taken even if some cause-and-effect relationships are not fully established scientifically. Applied to gene editing, this means the burden of proof for safety should be on those proposing edits, especially for irreversible germline changes.")
    ],
    "stem_eval": [
        ("Expert (4)", "Framework establishes clear scientific safety criteria grounded in model data, distinguishes therapy from enhancement with specific definitions, addresses germline vs. somatic editing differently, and includes equity provisions"),
        ("Proficient (3)", "Framework has reasonable criteria for evaluating safety and distinguishing therapy from enhancement with some model evidence"),
        ("Developing (2)", "Framework identifies some ethical concerns but criteria are vague or not connected to scientific evidence from the model"),
        ("Beginning (1)", "Framework is incomplete, lacks scientific grounding, or does not address the therapy-enhancement distinction")
    ],
    "support": [
        "Provide a simplified diagram of the CRISPR mechanism: Guide RNA finds target -> Cas9 cuts DNA -> Cell repairs -> Gene is edited",
        "Use a risk-benefit matrix: rows for different types of edits (single gene disease, polygenic trait, enhancement), columns for safety, effectiveness, ethics",
        "Sentence frames: \'When Guide RNA Specificity is ___, Off-Target Mutation Rate is ___ because the genome contains ___\'"
    ],
    "extensions": [
        "Research the He Jiankui case (2018 CRISPR babies in China) — what went wrong scientifically and ethically, and what has changed in gene-editing governance since?",
        "Investigate base editing and prime editing — newer CRISPR technologies that may reduce off-target effects. How do they differ from traditional Cas9 cutting?",
        "Analyze the movie Gattaca (1997) through the lens of your CRISPR model — which aspects of the film\'s genetic future are scientifically plausible and which are fiction?"
    ],
    "cross_curr": [
        ("Math", "Calculate the probability of at least one off-target edit given a per-site error rate of 0.001% across 3.2 billion base pairs. Use complementary probability: P(at least one) = 1 - P(none). What does the result reveal about genome-wide safety?"),
        ("ELA", "Write a Socratic dialogue between two scientists debating whether germline editing should be permitted for fatal genetic diseases, using evidence from your CRISPR model to support both positions"),
        ("History", "Research the history of eugenics in the United States (1900s-1970s) — forced sterilization programs, immigration restrictions, and the science that was used to justify them. How should this history inform modern gene-editing policy?")
    ],
    "misconceptions": [
        ("CRISPR can edit any trait we want with perfect precision", "While CRISPR is remarkably precise compared to previous gene-editing tools, it is not perfect. Off-target effects occur because the guide RNA can bind to similar DNA sequences elsewhere in the genome. More importantly, most human traits (intelligence, height, personality) are influenced by hundreds of genes interacting with environment, making them far beyond current editing capabilities. CRISPR works best for single-gene disorders with well-characterized mutations.", "Ask students: How many genes affect your height? (Answer: over 700 identified so far.) Now imagine trying to edit all 700 with some off-target risk at each one — the math makes it clear why \'designer babies\' are science fiction."),
        ("Gene editing is the same as GMOs in food", "While both involve modifying DNA, the techniques, organisms, and ethical stakes are fundamentally different. Agricultural GMOs typically insert genes from other species into plants for pest resistance or nutrition (like Bt corn or Golden Rice). Human gene editing with CRISPR corrects or modifies existing human genes. The ethical considerations — informed consent, heritability, equity, human dignity — are unique to human germline editing and don\'t apply to crop modification.", "Create a Venn diagram: What do GMO crops and human gene editing share? Where do they differ? Focus on the ethical dimensions that are unique to editing humans."),
        ("If a gene edit cures a disease, there are no downsides", "The model clearly shows that every gene edit carries some off-target risk. Additionally, some disease-causing genes confer benefits in other contexts — the sickle cell gene provides malaria resistance, and some cancer-risk genes enhance immune function. Editing these genes may cure one condition while creating vulnerability to another. The concept of pleiotropy (one gene affecting multiple traits) means the full consequences of any edit may not be apparent for years or generations.", "Discuss the sickle cell example: The HBB mutation causes sickle cell disease when you have two copies, but carrying one copy protects against malaria. If we edit out sickle cell, what happens to malaria resistance in regions where it\'s needed?")
    ]
}

L08 = {
    "id": "G12L1-L08",
    "title": "Why Does Stress Make You Sick?",
    "subtitle": "Modeling Stress Hormones, Immune Suppression, and the Mind-Body Connection",
    "ngss": "HS-LS1-3",
    "ngss_desc": "Plan and conduct an investigation to provide evidence that feedback mechanisms maintain homeostasis.",
    "big_question": "Your body has an immune system powerful enough to kill cancer cells and fight off deadly pathogens. So why does being stressed about a test, a breakup, or family problems make you more likely to catch a cold, break out in acne, and take longer to heal from injuries?",
    "objectives": [
        "Model how the hypothalamic-pituitary-adrenal (HPA) axis activates cortisol release and how chronic activation suppresses immune function",
        "Explain why the stress response evolved as a survival mechanism but becomes destructive when chronically activated",
        "Predict how different stress patterns (acute vs. chronic) produce different immune outcomes",
        "Analyze how understanding the stress-immune connection can inform practical health strategies for students"
    ],
    "vocabulary": [
        ("Cortisol", "A glucocorticoid hormone released by the adrenal glands in response to stress signals from the brain — acutely it mobilizes energy and enhances focus, but chronic elevation suppresses immune cell production, increases inflammation, and damages the hippocampus"),
        ("HPA Axis", "The hypothalamic-pituitary-adrenal axis — a neuroendocrine feedback loop where the hypothalamus signals the pituitary gland to release ACTH, which triggers cortisol release from the adrenal glands, with cortisol feeding back to shut down the loop when stress resolves"),
        ("Immune Suppression", "The reduction in immune system function caused by chronic cortisol exposure — cortisol reduces the production and activity of lymphocytes (T-cells, B-cells, natural killer cells), making the body more vulnerable to infections and slower to heal"),
        ("Allostatic Load", "The cumulative physiological wear and tear on the body from chronic stress activation — measured by biomarkers including cortisol levels, blood pressure, inflammatory markers, and metabolic indicators, representing the long-term cost of constant stress response activation")
    ],
    "components": [
        ("Stress Exposure", "The intensity, duration, and frequency of psychological or physical stressors — can range from acute (a single exam) to chronic (ongoing family conflict, poverty, or discrimination), with very different biological effects", True),
        ("Social Support", "The availability and quality of supportive relationships that buffer the stress response — strong social connections reduce HPA axis activation and cortisol release, while social isolation amplifies stress effects", True),
        ("Cortisol Level", "The concentration of cortisol in the bloodstream at any given time — rises sharply during acute stress to mobilize energy, but should return to baseline when stress resolves; chronic elevation indicates a dysregulated HPA axis", False),
        ("Immune Function", "The overall capacity of the immune system to detect and destroy pathogens, infected cells, and cancer cells — measured by lymphocyte count, antibody production, and natural killer cell activity, all of which decrease under chronic cortisol exposure", False),
        ("Health Outcome", "The observable health effects resulting from the balance between stress exposure, cortisol regulation, and immune function — ranges from optimal health with acute-only stress to frequent illness, slow healing, and chronic inflammation under persistent stress", False)
    ],
    "think_about_it": "During finals week, stress is high and sleep is low. Your model shows Cortisol Level spiking. But after finals, the stress is gone — yet many students get sick DURING the break. What does your model predict about the lag between cortisol exposure and immune recovery?",
    "scenarios": [
        ("Acute Stress Response", "Set Stress Exposure to high but brief (single event) with moderate Social Support — observe how Cortisol Level spikes then returns to baseline, with Immune Function temporarily suppressed but quickly recovering"),
        ("Chronic Stress Without Support", "Set Stress Exposure to moderate but continuous with low Social Support — observe how Cortisol Level remains elevated, Immune Function progressively declines, and Health Outcome deteriorates over weeks"),
        ("Chronic Stress With Strong Support", "Set Stress Exposure to moderate continuous with high Social Support — observe how Social Support buffers the cortisol response and partially protects Immune Function despite ongoing stress")
    ],
    "sim_scenarios": [
        ("Fight or Flight", "Stress Exposure: High, single event | Social Support: Moderate | Duration: 1 hour", "When you face a brief intense stressor (like a presentation), what does the model predict for Cortisol Level and Immune Function over the next 24 hours?"),
        ("Finals Week", "Stress Exposure: Moderate-high, continuous | Social Support: Low (isolated studying) | Duration: 2 weeks", "What happens to Immune Function after two weeks of sustained stress with little social connection?"),
        ("Supported Through Crisis", "Stress Exposure: High, continuous | Social Support: High (strong friend/family network) | Duration: 2 weeks", "How does strong social support change the trajectory of cortisol and immune function during a stressful period?")
    ],
    "discoveries": [
        "Acute stress actually enhances immune function briefly — cortisol mobilizes immune cells for potential injury, which is why the fight-or-flight response is adaptive for short-term survival",
        "Chronic stress is immunosuppressive because sustained cortisol exposure reduces lymphocyte production, impairs antibody response, and increases systemic inflammation — the opposite of the acute response",
        "Social support is not just emotional comfort — it measurably reduces HPA axis activation and cortisol release, creating a biological buffer that partially protects immune function during chronic stress",
        "There is a lag between stress cessation and immune recovery — this explains why people often get sick right after a stressful period ends, when cortisol drops but immune function hasn\'t yet restored"
    ],
    "answer": "Stress makes you sick because of a tragic mismatch between evolution and modern life. Your stress response system — the HPA axis — evolved to handle short-term physical threats: a predator, a rival, a storm. Cortisol surges to mobilize energy, sharpen focus, and temporarily boost immune readiness. The system works brilliantly for 20-minute emergencies. But modern stress is chronic — school pressure, social media, family conflict, financial worry — and the HPA axis never shuts off. Sustained cortisol exposure suppresses the very immune cells (T-cells, B-cells, NK cells) that protect you from infection and cancer. Your body is literally choosing to fight the perceived threat at the expense of fighting actual pathogens. Social support is the most powerful natural buffer — it physically reduces cortisol output and partially protects immune function even during chronic stress.",
    "stem_title": "Design a School Stress Reduction Program",
    "stem_mission": "Using your model data on the biological mechanisms of stress-immune suppression, design an evidence-based stress reduction program for your school that targets the specific biological pathways through which chronic stress damages health.",
    "stem_scenario": "Your school\'s health data shows that 68% of seniors report chronic stress, absences spike during exam periods, and students who report low social support have 3x more sick days. The administration wants a science-based program — not generic wellness posters — that addresses the biological mechanisms your model revealed. The program must be practical, evidence-based, and measurable.",
    "stem_questions": [
        "Which biological pathway does your model identify as the most important target for stress intervention?",
        "How can your program increase Social Support as a cortisol buffer, based on what your model shows about its protective effects?",
        "What does your model predict about the health impact of reducing chronic stress exposure by even 20%?"
    ],
    "stem_design_qs": [
        "What specific stress-reduction interventions does your program include and which biological mechanism does each one target?",
        "How does your program address the social support component that your model shows is critical for cortisol buffering?",
        "What model evidence supports your claim that these interventions will measurably improve student health?",
        "How would you measure whether your program actually reduces cortisol levels and improves immune function outcomes?"
    ],
    "career": "Psychoneuroimmunologists study the interactions between psychological processes, the nervous system, and the immune system, earning $70,000-$140,000/year in research positions. Health psychologists apply stress-health research in clinical settings, earning $75,000-$120,000/year. Public health specialists designing workplace and school wellness programs earn $55,000-$100,000/year.",
    "images": {
        "cover": ("G12L1-L08-cover.png", "A photorealistic image of a diverse 17-18 year old student looking stressed while studying late at night, surrounded by textbooks and a laptop, with a visual overlay suggesting biological stress markers, dramatic moody lighting"),
        "landscape": ("G12L1-L08-landscape.png", "A diverse group of 17-18 year old students in a modern health science classroom examining HPA axis diagrams and immune system models on a smartboard, some students looking engaged in animated discussion"),
        "modeling": ("G12L1-L08-modeling.png", "Diverse 17-18 year old students working on laptops building computational models of cortisol-immune interactions, classroom walls showing endocrine system and immune cell diagrams"),
        "discussion": ("G12L1-L08-discussion.png", "A teacher leading a discussion with diverse 17-18 year old students about stress and health, a diagram of the HPA axis feedback loop on the smartboard, students sharing personal observations"),
        "stem": ("G12L1-L08-stem.png", "Diverse 17-18 year old students collaboratively designing a school wellness program on whiteboards, with health data charts and stress intervention flowcharts visible")
    },
    "pre_assessment": [
        "Have you ever gotten sick right after a really stressful period (like after finals or a big event)? Why do you think that happens?",
        "What do you think the connection is between your mental state and your physical health? Can thoughts really affect your body?",
        "What does \'stress\' actually mean biologically? What\'s happening inside your body when you feel stressed?",
        "Do you think having close friends and family actually affects your physical health, or is that just a feel-good idea?"
    ],
    "extend_components": [
        ("Sleep Quality", "The duration and architecture of sleep — chronic stress disrupts sleep, and sleep deprivation independently elevates cortisol and suppresses immune function, creating a vicious cycle that compounds stress-immune damage"),
        ("Inflammatory Response", "The body\'s generalized immune activation that increases under chronic stress — cortisol paradoxically increases systemic inflammation even while suppressing specific immune defenses, contributing to autoimmune conditions and cardiovascular disease"),
        ("Coping Strategy Effectiveness", "The degree to which an individual\'s stress management techniques actually reduce HPA axis activation — evidence-based strategies (exercise, mindfulness, social connection) produce measurable cortisol reduction, while maladaptive coping (substance use, avoidance) can worsen the stress response")
    ],
    "reflections": [
        "How does your model explain the paradox that stress evolved as a survival mechanism but now causes disease?",
        "Why does chronic stress suppress the immune system while acute stress briefly enhances it? What does this reveal about evolutionary design?",
        "Your model shows that social support physically reduces cortisol. What are the implications for people who are socially isolated — and for how we design schools and communities?",
        "How might understanding the stress-immune connection change the way you manage your own health during stressful periods?",
        "What are the equity implications of stress-immune research, given that poverty, discrimination, and adverse childhood experiences create chronic stress in specific populations?"
    ],
    "dimensions": [
        ("Science Practice", "Planning and Carrying Out Investigations", "Students plan investigations to provide evidence that the HPA axis feedback mechanism maintains cortisol homeostasis during acute stress but fails during chronic activation, leading to immune suppression."),
        ("Disciplinary Core Idea", "LS1.A Structure and Function", "The HPA axis is a homeostatic feedback mechanism that maintains cortisol balance: the hypothalamus detects stress, signals the pituitary, which triggers adrenal cortisol release, which feeds back to suppress further activation — a loop that breaks down under chronic stress."),
        ("Crosscutting Concept", "Stability and Change", "Students analyze how the stress response system maintains stability (homeostasis) during normal conditions but shifts to a disease-promoting state when chronic stress overwhelms the feedback mechanisms designed for short-term activation.")
    ],
    "cast_items": [
        "Provide evidence that the HPA axis is a feedback mechanism that maintains cortisol homeostasis under normal conditions but fails under chronic stress",
        "Predict how different stress patterns (acute vs. chronic) and social support levels affect immune function and health outcomes",
        "Explain why the stress response is adaptive for short-term survival but maladaptive when chronically activated in modern environments"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student experiences two weeks of chronic stress during finals with minimal sleep and social isolation. Based on the stress-immune model, which of the following best predicts their health outcome during winter break and why?"),
        ("Constructed Response:", "Using your model, explain the biological mechanism by which strong social support protects immune function during chronic stress. Reference the HPA axis feedback loop, cortisol levels, and at least two specific immune components that are affected.")
    ],
    "background_intro": "The field of psychoneuroimmunology — the study of how psychological states affect the nervous and immune systems — has revolutionized our understanding of the mind-body connection. Far from being separate systems, the brain, endocrine system, and immune system are in constant bidirectional communication. Stress hormones directly regulate immune cell production and activity, meaning that your psychological state literally determines how well your body can fight infection and disease.",
    "background_sections": [
        ("The HPA Axis: Your Stress Command Center", "When the brain perceives a threat, the hypothalamus releases corticotropin-releasing hormone (CRH), which signals the anterior pituitary to release adrenocorticotropic hormone (ACTH) into the bloodstream. ACTH travels to the adrenal glands atop the kidneys, triggering cortisol release. This cascade takes about 20 minutes from threat perception to peak cortisol. Critically, cortisol feeds back to the hypothalamus and pituitary to suppress further CRH and ACTH release — a negative feedback loop that shuts down the stress response once the threat passes. Under chronic stress, this feedback mechanism becomes desensitized, and cortisol remains elevated."),
        ("How Cortisol Suppresses Immunity", "Cortisol suppresses the immune system through multiple mechanisms: it reduces the production of lymphocytes (T-cells, B-cells) in the thymus and bone marrow, inhibits cytokine signaling between immune cells, reduces the activity of natural killer cells that patrol for cancer and virus-infected cells, and shifts immune response from anti-viral (Th1) to anti-bacterial (Th2), leaving the body more vulnerable to viruses. Acutely, this makes evolutionary sense — during a fight, the body redirects resources from long-term immune surveillance to immediate survival. Chronically, it\'s catastrophic."),
        ("The Social Buffer Effect", "Research by Sheldon Cohen, Janice Kiecolt-Glaser, and others has demonstrated that social support physically reduces HPA axis activation. Studies show that people with strong social networks produce less cortisol in response to the same stressor, recover cortisol baseline faster after stress, have higher natural killer cell activity, produce stronger antibody responses to vaccines, and heal from wounds 40% faster. The mechanism appears to involve oxytocin release during positive social interactions, which directly inhibits HPA axis activation."),
        ("Allostatic Load and Health Disparities", "Bruce McEwen\'s concept of allostatic load describes the cumulative biological cost of chronic stress. Populations experiencing poverty, discrimination, adverse childhood experiences, and environmental hazards carry disproportionate allostatic load — measurable in higher cortisol, elevated inflammatory markers, accelerated telomere shortening, and premature aging of the immune system. This provides a biological mechanism for observed health disparities: chronic social stress produces chronic immune suppression, which produces higher rates of infection, autoimmune disease, cancer, and cardiovascular disease in specific communities.")
    ],
    "lever_L": "Students identify stress exposure, social support, cortisol level, immune function, and health outcome as the key components of the stress-immune system.",
    "lever_E": "Students determine that chronic stress elevates cortisol which suppresses immune function, that social support buffers cortisol response, and that the pattern of stress (acute vs. chronic) determines whether immune effects are adaptive or destructive.",
    "lever_V": "Students build a computational model showing how the HPA axis feedback loop responds to different stress patterns and how social support modifies cortisol output and downstream immune function.",
    "lever_Ev": "Students run acute stress, chronic stress without support, and chronic stress with support scenarios to test predictions about how stress patterns and social connections affect immune function and health outcomes.",
    "lever_R": "Students add sleep quality, inflammatory response, or coping strategy effectiveness to explore how additional factors interact with the basic stress-immune model.",
    "slides_guide": [
        {
            "num": "Slide 1",
            "title": "Cover",
            "visual": "Title slide with compelling image related to Why Does Stress Make You Sick?",
            "say": "Ever get sick right after finals? That\'s not coincidence — it\'s biology. Today we investigate the science behind it.",
            "do": "Show cover image. Ask: How many of you have gotten sick after a stressful period? Quick show of hands.",
            "time": "2 min"
        },
        {
            "num": "Slide 2",
            "title": "Learning Objectives",
            "visual": "Learning goals and vocabulary terms with HPA axis diagram",
            "say": "Here\'s what you\'ll understand by the end of today — the actual biological mechanism connecting your thoughts to your immune system.",
            "do": "Have students read objectives aloud. Pre-teach vocabulary with endocrine system diagram showing the HPA axis pathway.",
            "time": "3 min"
        },
        {
            "num": "Slide 3",
            "title": "Big Question",
            "visual": "Provocative question with image showing stressed student and immune cell imagery",
            "say": "Your immune system can kill cancer cells. So why can worrying about a test make you catch a cold?",
            "do": "Quick-write: Students hypothesize a biological mechanism connecting stress and illness. Save to compare with model evidence.",
            "time": "3 min"
        },
        {
            "num": "Slide 4",
            "title": "LEVER Framework",
            "visual": "LEVER steps overview",
            "say": "We\'re going to model the hidden conversation between your brain, your hormones, and your immune system.",
            "do": "Preview each LEVER step. Emphasize that this model connects psychology to biology through measurable hormones.",
            "time": "2 min"
        },
        {
            "num": "Slide 5",
            "title": "Activity 1: Components",
            "visual": "Component cards — stress exposure, social support, cortisol level, immune function, health outcome",
            "say": "What are the key parts of this stress-immune system? Which inputs come from your environment, and which emerge inside your body?",
            "do": "Guide sorting of external vs. internal components. Discuss why social support is an external input that modifies internal biology.",
            "time": "8 min"
        },
        {
            "num": "Slide 6",
            "title": "Activity 2: Connections",
            "visual": "Relationship arrows between stress-immune components",
            "say": "When Stress Exposure is chronic and Social Support is low, what happens to Cortisol Level? And what does sustained cortisol do to Immune Function?",
            "do": "Students draw arrows showing +/- relationships. Discuss the HPA feedback loop and why chronic stress breaks it.",
            "time": "8 min"
        },
        {
            "num": "Slide 7",
            "title": "Activity 3: Simulation",
            "visual": "Simulation results comparing acute vs. chronic stress immune effects",
            "say": "Run each scenario. Notice the dramatic difference between brief stress and sustained stress on your immune system.",
            "do": "Students run all scenarios, record predictions vs. observations. Discuss the social support buffer effect.",
            "time": "10 min"
        },
        {
            "num": "Slide 8",
            "title": "Discoveries",
            "visual": "Key findings summary — stress-immune connection mechanisms",
            "say": "Your model reveals that chronic stress literally turns down your immune system — and social connection literally turns it back up.",
            "do": "Class discussion of discoveries. Compare initial hypotheses to model evidence. Emphasize the evolutionary mismatch.",
            "time": "5 min"
        },
        {
            "num": "Slide 9",
            "title": "STEM Challenge",
            "visual": "Engineering challenge: Design a School Stress Reduction Program",
            "say": "Now design a program that targets the specific biological pathways your model revealed. No generic wellness posters.",
            "do": "Groups design evidence-based programs targeting HPA axis regulation and social support. Present with model data justification.",
            "time": "12 min"
        }
    ],
    "sort_reasoning": "Stress Exposure and Social Support are external components because they represent environmental inputs that exist before the biological stress response activates — one is the stressor itself and the other is the social environment that modifies the response. Cortisol Level, Immune Function, and Health Outcome are internal because they emerge from the body\'s neuroendocrine and immune processing of those external inputs through the HPA axis feedback system.",
    "relationships": [
        ("Stress Exposure to Cortisol Level", "POSITIVE (+)", "Greater stress exposure activates the HPA axis more intensely and for longer durations, increasing cortisol production and bloodstream concentration."),
        ("Social Support to Cortisol Level", "NEGATIVE (-)", "Stronger social support reduces HPA axis activation through oxytocin-mediated pathways, lowering cortisol output even when stress exposure remains constant."),
        ("Cortisol Level to Immune Function", "NEGATIVE (-)", "Elevated cortisol suppresses lymphocyte production, reduces natural killer cell activity, and impairs antibody response, progressively weakening immune defenses."),
        ("Immune Function to Health Outcome", "POSITIVE (+)", "Higher immune function means greater capacity to fight infections, detect abnormal cells, and heal injuries, directly improving overall health outcomes.")
    ],
    "sim_answers": [
        ("Acute Stress Response", "With high but brief Stress Exposure and moderate Social Support, the model shows a sharp Cortisol spike that returns to baseline within hours. Immune Function dips temporarily but recovers fully. Health Outcome remains positive because the system worked as designed — a short mobilization followed by recovery. This is the stress response doing its evolutionary job."),
        ("Chronic Stress Without Support", "With continuous moderate Stress Exposure and low Social Support, the model shows Cortisol Level remaining elevated for weeks. The HPA feedback loop becomes desensitized and fails to shut down. Immune Function progressively declines as lymphocyte production drops and natural killer cell activity decreases. Health Outcome deteriorates with increased susceptibility to infection, slower wound healing, and rising inflammation. This is the most dangerous pattern — and the most common in modern life.")
    ],
    "reflection_exemplars": [
        ("Why is chronic stress more dangerous than acute stress?", "Our model clearly shows the difference: acute stress produces a cortisol spike that enhances immune readiness briefly and resolves quickly — exactly what evolution designed. Chronic stress keeps cortisol elevated indefinitely because the HPA feedback loop becomes desensitized and fails to shut down the response. This sustained cortisol exposure progressively destroys immune function: T-cells decline, natural killer cells become less active, and antibody production drops. The system evolved for 20-minute emergencies but modern life creates 20-week (or 20-year) chronic activation. The immune system pays the price."),
        ("How does social support physically protect health?", "This isn\'t just psychology — our model shows a measurable biological mechanism. Social support reduces HPA axis activation through oxytocin release during positive social interactions. Oxytocin directly inhibits CRH release from the hypothalamus, which means less ACTH, less cortisol, and less immune suppression. Research shows this is dose-dependent: people with stronger social networks produce measurably less cortisol in response to identical stressors, have higher NK cell counts, and produce stronger vaccine antibody responses. Social connection is literally medicine — it modifies the same biological pathway that chronic stress damages.")
    ],
    "stem_intro": "Present the challenge: Your school\'s health data shows alarming connections between student stress levels and illness rates. The administration wants a science-based stress reduction program — not generic motivational posters, but interventions that target the specific HPA axis and immune pathways your model revealed. Use your model data to identify the highest-leverage intervention points and design a program with measurable health outcomes.",
    "stem_concepts": [
        ("Mind-Body Medicine", "A medical approach that recognizes the bidirectional communication between psychological states and physiological processes. Evidence-based mind-body interventions include mindfulness meditation (shown to reduce cortisol by 25%), yoga (reduces inflammatory markers), and cognitive behavioral therapy (normalizes HPA axis function)."),
        ("Biofeedback", "A technique that uses real-time monitoring of physiological processes (heart rate variability, skin conductance, cortisol levels) to teach people to consciously modify their stress response. Studies show biofeedback can reduce HPA axis reactivity with consistent practice."),
        ("Universal vs. Targeted Prevention", "In public health, universal programs serve everyone (like school-wide mindfulness), while targeted programs focus on high-risk individuals (like students with chronic stressors). Effective stress programs use both tiers because different populations have different allostatic loads and different biological needs.")
    ],
    "stem_eval": [
        ("Expert (4)", "Program targets specific biological mechanisms (HPA axis, cortisol, immune pathways) with evidence-based interventions, includes social support building as a core component, uses model data to justify design, and has measurable health outcomes"),
        ("Proficient (3)", "Program addresses stress-immune biology with reasonable interventions and some reference to model evidence and measurable outcomes"),
        ("Developing (2)", "Program identifies stress as a health concern but interventions are generic or not connected to the specific biological mechanisms from the model"),
        ("Beginning (1)", "Program is incomplete, not grounded in stress-immune biology, or relies on unscientific approaches")
    ],
    "support": [
        "Provide a labeled diagram of the HPA axis feedback loop: Hypothalamus -> CRH -> Pituitary -> ACTH -> Adrenals -> Cortisol -> (feedback to hypothalamus)",
        "Use a traffic light analogy: Green = acute stress (helpful), Yellow = moderate stress (manageable), Red = chronic stress (immune damage) — what determines which zone you\'re in?",
        "Sentence frames: \'When Stress Exposure is ___ and Social Support is ___, the model predicts Cortisol Level will ___ because the HPA axis ___\'"
    ],
    "extensions": [
        "Research telomere shortening as a biomarker of chronic stress — how does Elizabeth Blackburn\'s Nobel Prize-winning research show that stress literally ages your cells faster?",
        "Investigate how adverse childhood experiences (ACEs) reprogram the HPA axis during development — why are the stress-immune effects of childhood trauma measurable decades later?",
        "Design an experiment to measure cortisol levels in your classmates during exam week vs. a normal week using salivary cortisol test strips — what does your model predict the results will show?"
    ],
    "cross_curr": [
        ("Math", "Graph cortisol levels over 24 hours for acute stress (single spike and recovery) vs. chronic stress (sustained elevation). Calculate the area under the curve for each — how does total cortisol exposure compare, and what does this imply for cumulative immune damage?"),
        ("ELA", "Write a research-based essay arguing that later school start times, reduced homework loads, or increased recess time would improve student health based on the biological mechanisms of stress-immune suppression"),
        ("Sociology", "Research how allostatic load — the biological cost of chronic stress — contributes to health disparities in communities experiencing poverty, discrimination, and environmental injustice. How does the stress-immune model explain patterns in population health data?")
    ],
    "misconceptions": [
        ("Stress is all in your head — it can\'t really make you physically sick", "Stress is a full-body physiological event, not just a mental state. The HPA axis converts psychological perception of threat into measurable hormonal changes (cortisol, adrenaline) that directly affect immune cell production, inflammatory pathways, cardiovascular function, and wound healing. Brain scans, blood tests, and immune assays all show physical changes during stress. The mind-body connection is not metaphorical — it operates through specific, measurable neuroendocrine pathways.", "Show data: surgical wounds heal 40% slower in chronically stressed patients. Vaccine antibody responses are 50% weaker in stressed caregivers. These are physical measurements, not opinions."),
        ("Some stress is good for you, so all stress management is unnecessary", "The model clearly distinguishes between acute and chronic stress. Acute stress IS beneficial — it enhances alertness, mobilizes energy, and briefly boosts immune readiness. This is the \'good stress\' (eustress) people reference. But chronic stress — where cortisol remains elevated for days, weeks, or months — is unambiguously harmful. The issue isn\'t eliminating all stress but preventing the chronic activation that damages the HPA feedback loop and suppresses immunity.", "Demonstrate with the model: Run the acute scenario (positive outcome) then the chronic scenario (negative outcome). Same system, different patterns — the difference is duration, not existence of stress."),
        ("Relaxation techniques are too simple to affect real biology", "Evidence-based stress reduction techniques produce measurable biological changes. Mindfulness meditation reduces cortisol by 25% and increases natural killer cell activity. Regular exercise normalizes HPA axis sensitivity and reduces inflammatory markers. Deep breathing activates the parasympathetic nervous system, directly counteracting the sympathetic stress response. These aren\'t placebo effects — they are physiological modifications of the same neuroendocrine pathways your model shows driving immune suppression.", "Compare: A prescription medication that reduced cortisol by 25% would be considered highly effective. Mindfulness meditation achieves the same result through a different mechanism — activating the parasympathetic nervous system. Both modify the same biology; only the delivery method differs.")
    ]
}

L09 = {
    "id": "G12L1-L09",
    "title": "Is Social Media Rewiring Your Brain?",
    "subtitle": "Modeling Dopamine Pathways, Attention Regulation, and Digital Addiction Mechanisms",
    "ngss": "HS-LS1-2",
    "ngss_desc": "Develop and use a model to illustrate the hierarchical organization of interacting systems that provide specific functions within multicellular organisms.",
    "big_question": "You check your phone 96 times a day — once every 10 minutes. Instagram, TikTok, and Snapchat were designed by neuroscientists to be as addictive as possible. Is social media physically changing the structure and function of your brain, and if so, can you get it back?",
    "objectives": [
        "Model how variable-ratio reinforcement schedules in social media trigger dopamine release patterns that hijack the brain\'s reward circuitry",
        "Explain how chronic social media use alters prefrontal cortex function, attention span, and the brain\'s baseline dopamine sensitivity",
        "Predict how different usage patterns (passive scrolling vs. active creation vs. digital detox) produce different neurological outcomes",
        "Analyze whether social media platforms should be regulated based on neuroscience evidence of addictive design"
    ],
    "vocabulary": [
        ("Variable-Ratio Reinforcement", "A reward schedule where the payoff comes after an unpredictable number of actions — the most addictive pattern known to behavioral neuroscience, used in slot machines and social media feeds where you never know when the next like, comment, or viral post will appear"),
        ("Dopamine Baseline", "The brain\'s resting level of dopamine activity that determines normal mood, motivation, and pleasure capacity — chronic overstimulation from social media can lower this baseline, making non-digital activities feel boring and unrewarding by comparison"),
        ("Attention Fragmentation", "The progressive shortening of sustained attention capacity caused by rapid-switching between stimuli — social media trains the brain to expect new content every few seconds, making it increasingly difficult to maintain focus on longer tasks like reading or studying"),
        ("Neuroplasticity", "The brain\'s ability to physically reorganize neural pathways based on repeated experience — social media use literally strengthens the neural circuits associated with checking, scrolling, and seeking social validation while weakening circuits for sustained attention and deep thinking")
    ],
    "components": [
        ("Social Media Exposure", "The total time, frequency, and type of social media use — includes passive scrolling (consuming content), active posting (creating content), and social comparison (evaluating self against others), each with different neurological effects", True),
        ("Notification Frequency", "The rate at which push notifications, alerts, and badges interrupt ongoing activity — each notification triggers a micro-dopamine hit and trains the brain to expect and crave interruptions, designed by platforms to maximize engagement", True),
        ("Dopamine Sensitivity", "The brain\'s responsiveness to dopamine signals in the reward circuit — decreases with chronic overstimulation as receptors downregulate, requiring increasingly intense stimuli to achieve the same pleasure response", False),
        ("Attention Capacity", "The brain\'s ability to sustain focus on a single task without switching — measured by duration of sustained attention, resistance to distraction, and depth of cognitive processing, all of which decrease with heavy social media use", False),
        ("Cognitive Well-Being", "The overall health of higher-order brain functions including working memory, impulse control, emotional regulation, and self-directed attention — reflects the cumulative impact of social media on prefrontal cortex function and dopamine system integrity", False)
    ],
    "think_about_it": "TikTok serves you a new video every 15-60 seconds, each one optimized by AI to maximize your dopamine response. After two hours of this, you try to read a textbook chapter. What does your model predict about Attention Capacity, and why does the textbook feel unbearable?",
    "scenarios": [
        ("Heavy Passive Scrolling", "Set Social Media Exposure to high passive scrolling with maximum Notification Frequency — observe how Dopamine Sensitivity drops, Attention Capacity shrinks, and Cognitive Well-Being deteriorates over time"),
        ("Active and Intentional Use", "Set Social Media Exposure to moderate with active creation (posting original content) and low Notification Frequency — observe how intentional use produces different dopamine patterns and partially preserves Attention Capacity"),
        ("Digital Detox", "Reduce Social Media Exposure to zero for 7 days with zero Notification Frequency — observe how Dopamine Sensitivity gradually recovers and Attention Capacity begins to restore, though not immediately")
    ],
    "sim_scenarios": [
        ("Doom Scrolling", "Social Media Exposure: 4+ hours passive scrolling | Notification Frequency: Maximum | Duration: 30 days", "After a month of heavy passive scrolling with constant notifications, what does the model predict for Dopamine Sensitivity and Attention Capacity?"),
        ("Mindful Usage", "Social Media Exposure: 1 hour active/creative | Notification Frequency: Off | Duration: 30 days", "How does intentional, time-limited, notification-free social media use compare to passive scrolling in its effects on the brain?"),
        ("Recovery Period", "Social Media Exposure: Zero | Notification Frequency: Zero | Duration: 14 days after heavy use", "How quickly do Dopamine Sensitivity and Attention Capacity recover after a two-week digital detox? Does the brain fully reset?")
    ],
    "discoveries": [
        "Social media platforms use variable-ratio reinforcement — the same mechanism that makes slot machines addictive — to create unpredictable reward patterns that maximize dopamine release and compulsive checking behavior",
        "Chronic heavy use lowers dopamine baseline sensitivity through receptor downregulation, making non-digital activities (reading, conversation, nature) feel increasingly boring and unrewarding",
        "Attention fragmentation is a neuroplastic change — the brain physically strengthens rapid-switching circuits and weakens sustained-attention circuits, measurably reducing the ability to focus on tasks longer than a few minutes",
        "Recovery is possible but not instant — dopamine sensitivity and attention capacity can partially restore during digital detox, but full recovery requires weeks to months depending on the duration and intensity of prior use"
    ],
    "answer": "Yes, social media is physically rewiring your brain — and the science is increasingly clear about how. Social media platforms exploit variable-ratio reinforcement schedules (the same mechanism behind slot machine addiction) to trigger unpredictable dopamine surges that train your brain to compulsively check for new content. Chronic use downregulates dopamine receptors, lowering your baseline sensitivity so that normal activities feel increasingly unsatisfying. Meanwhile, the constant stream of 15-60 second content fragments trains your attention circuits to expect rapid novelty, physically weakening the neural pathways for sustained focus through neuroplasticity. The good news: the brain can recover. Digital detox studies show measurable improvement in attention span and dopamine sensitivity within 2-4 weeks. But the platforms are designed by neuroscientists to prevent exactly this recovery — every notification pulls you back.",
    "stem_title": "Design a Digital Wellness App",
    "stem_mission": "Design a smartphone application that helps teens monitor and manage their social media use by providing real-time feedback on neurological effects, using the same behavioral neuroscience principles that make social media addictive — but in reverse, to build healthier digital habits.",
    "stem_scenario": "A tech company wants to create a counter-product: an app that uses behavioral neuroscience to help people break unhealthy social media habits. The app must be based on the same dopamine and reinforcement science that makes platforms addictive, but designed to promote digital wellness. The challenge: the app itself must avoid becoming another addictive screen experience.",
    "stem_questions": [
        "What specific dopamine and reinforcement mechanisms does your model identify as the targets for intervention?",
        "How can you use variable-ratio reinforcement FOR good — rewarding healthy behaviors instead of compulsive checking?",
        "What does your model predict about the minimum digital detox duration needed for measurable dopamine sensitivity recovery?"
    ],
    "stem_design_qs": [
        "What specific behavioral neuroscience principles does your app use to counteract addictive social media design?",
        "How does your app provide feedback without becoming another source of compulsive checking and dopamine-seeking?",
        "What model evidence supports your claim that your app\'s intervention strategy will improve attention capacity and dopamine sensitivity?",
        "How would you measure whether your app actually reduces problematic social media use and improves cognitive well-being?"
    ],
    "career": "Behavioral neuroscientists study how digital technology affects brain function and development, earning $70,000-$140,000/year in research positions. UX ethics designers ensure technology products don\'t exploit psychological vulnerabilities, earning $90,000-$160,000/year. Digital wellness consultants help organizations develop healthy technology policies, earning $65,000-$120,000/year.",
    "images": {
        "cover": ("G12L1-L09-cover.png", "A photorealistic image of a diverse 17-18 year old student illuminated by the blue glow of a smartphone screen in a dimly lit room, with faint neural pathway graphics overlaid suggesting brain rewiring, cinematic lighting"),
        "landscape": ("G12L1-L09-landscape.png", "A diverse group of 17-18 year old students in a modern neuroscience classroom examining brain imaging displays showing dopamine pathways, smartphones on desks, engaged in lively debate"),
        "modeling": ("G12L1-L09-modeling.png", "Diverse 17-18 year old students working on laptops building computational models of dopamine and attention, classroom walls showing reward pathway diagrams and attention research posters"),
        "discussion": ("G12L1-L09-discussion.png", "A teacher leading a discussion with diverse 17-18 year old students about social media and the brain, a comparison of brain scans during scrolling vs. reading displayed on the smartboard"),
        "stem": ("G12L1-L09-stem.png", "Diverse 17-18 year old students designing a digital wellness app interface on whiteboards and tablets, with behavioral science flowcharts and wireframes visible")
    },
    "pre_assessment": [
        "How many times do you estimate you check your phone each day? Do you think the actual number is higher or lower than your estimate?",
        "Have you noticed any changes in your ability to focus on reading or homework over the past few years? What do you think caused those changes?",
        "Why do you think scrolling through TikTok or Instagram feels so satisfying in the moment but often leaves you feeling worse afterward?",
        "Do you think social media companies have a responsibility to make their products less addictive? Why or why not?"
    ],
    "extend_components": [
        ("Social Comparison Intensity", "The degree to which social media use triggers upward social comparison — comparing yourself to curated highlight reels of others\' lives, which activates stress pathways and reduces self-esteem independently of the dopamine and attention effects"),
        ("Sleep Disruption", "The impact of evening screen use on melatonin production and sleep architecture — blue light suppresses melatonin, social media content increases arousal, and poor sleep independently impairs dopamine system recovery and attention restoration"),
        ("FOMO Activation", "Fear of missing out — a psychological driver that keeps users checking social media even when they want to stop, operating through anxiety pathways that are separate from but synergistic with the dopamine reward system")
    ],
    "reflections": [
        "How does your model explain why TikTok and Instagram feel more compelling than reading a book, even when you know the book is more valuable?",
        "What does dopamine receptor downregulation mean for your ability to enjoy non-digital activities like conversation, nature, or hobbies?",
        "Your model shows that notification frequency is a powerful driver of compulsive checking. What would happen if you turned off ALL notifications for a week?",
        "Should social media platforms be required to disclose the psychological manipulation techniques they use, similar to nutrition labels on food?",
        "If social media is rewiring teenage brains during critical development periods, is this a personal responsibility issue or a public health issue?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop computational models to illustrate how hierarchically organized neural systems — from individual dopamine neurons to reward circuits to prefrontal cortex regulation — are disrupted by social media\'s designed reinforcement patterns."),
        ("Disciplinary Core Idea", "LS1.A Structure and Function", "The brain\'s reward circuitry (ventral tegmental area, nucleus accumbens, prefrontal cortex) provides specific motivational and attention-regulation functions that are altered by chronic social media stimulation patterns, affecting the hierarchical organization of cognitive control."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify causal mechanisms linking specific social media design features (variable-ratio reinforcement, notification systems) to measurable changes in dopamine sensitivity and attention capacity through neuroplastic reorganization.")
    ],
    "cast_items": [
        "Model how variable-ratio reinforcement in social media platforms triggers dopamine release patterns that lead to receptor downregulation and compulsive use",
        "Predict how different social media usage patterns (passive scrolling vs. active creation vs. detox) produce different neurological outcomes for attention and reward sensitivity",
        "Explain how neuroplasticity enables both the damage from chronic heavy use and the recovery during digital detox"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student spends 4 hours daily on TikTok for 3 months, then tries to study for the SAT. Based on the social media-brain model, which neurological changes best explain why sustained focus on test preparation feels nearly impossible?"),
        ("Constructed Response:", "Using your model, compare the predicted neurological effects of 3 hours of passive Instagram scrolling per day versus 3 hours of active content creation (making art, writing, filming). Explain why the same total screen time produces different effects on Dopamine Sensitivity and Attention Capacity.")
    ],
    "background_intro": "Silicon Valley\'s most profitable products are designed using the same behavioral neuroscience that makes slot machines addictive. Former tech insiders — including Facebook\'s founding president Sean Parker, Google\'s former design ethicist Tristan Harris, and the creators of the iPhone\'s infinite scroll — have publicly warned that social media platforms are engineered to exploit dopamine-driven feedback loops in the human brain. The question is no longer whether social media affects the brain, but how much damage is being done and whether it\'s reversible.",
    "background_sections": [
        ("The Neuroscience of the Scroll", "Social media platforms use variable-ratio reinforcement — delivering rewards (likes, comments, interesting content) at unpredictable intervals. This is the most addictive reinforcement schedule known to behavioral science, identical to the mechanism that makes slot machines the most profitable form of gambling. Each scroll is a pull of the lever: sometimes you get nothing interesting, sometimes you get a dopamine-triggering post. The unpredictability is the key — the brain releases more dopamine in anticipation of an uncertain reward than in response to a guaranteed one. This is why you can\'t stop scrolling even when most content is boring."),
        ("Dopamine Downregulation and Anhedonia", "When the brain is chronically flooded with dopamine from social media stimulation, it protects itself by reducing dopamine receptor density — the same downregulation mechanism seen in substance addiction. The result is a lowered dopamine baseline: the brain\'s resting state of pleasure and motivation drops below normal. Activities that once felt rewarding — reading, face-to-face conversation, walking in nature — no longer produce enough dopamine to feel satisfying. Stanford psychiatrist Anna Lembke calls this \'dopamine deficit state\' — a mild but pervasive anhedonia (inability to feel pleasure) that drives the user back to the screen for relief."),
        ("Attention Fragmentation and Neuroplasticity", "The average TikTok video is 15-60 seconds. Instagram Reels, YouTube Shorts, and Twitter/X are all converging toward shorter content because engagement data shows users prefer rapid novelty. This preference isn\'t innate — it\'s trained. Neuroplasticity means the brain strengthens whatever neural circuits are used most frequently. Hours of daily rapid-content-switching strengthens circuits for quick task-switching while weakening circuits for sustained attention. Research by Gloria Mark at UC Irvine shows average attention span on a single screen has decreased from 2.5 minutes in 2004 to 47 seconds in 2023 — and heavy social media users show the shortest spans."),
        ("The Adolescent Vulnerability Window", "The adolescent brain is uniquely vulnerable because the prefrontal cortex — responsible for impulse control, long-term planning, and self-regulation — doesn\'t fully mature until age 25. Meanwhile, the reward circuitry (nucleus accumbens) is fully active and hypersensitive during adolescence. This creates a developmental mismatch: teens have a fully operational gas pedal (reward-seeking) with an underdeveloped brake (impulse control). Social media exploits this window — which is why teen usage rates, addiction indicators, and mental health impacts consistently exceed those of adults exposed to identical platforms.")
    ],
    "lever_L": "Students identify social media exposure, notification frequency, dopamine sensitivity, attention capacity, and cognitive well-being as the key components of the social media-brain system.",
    "lever_E": "Students determine that variable-ratio reinforcement and notification interruptions drive dopamine dysregulation, that chronic exposure reduces dopamine sensitivity and attention capacity through neuroplasticity, and that usage pattern (passive vs. active) affects outcomes differently.",
    "lever_V": "Students build a computational model showing how social media design features interact with the brain\'s dopamine and attention systems to produce measurable changes in cognitive function over time.",
    "lever_Ev": "Students run heavy passive use, mindful active use, and digital detox scenarios to test predictions about how different usage patterns affect dopamine sensitivity, attention capacity, and cognitive well-being.",
    "lever_R": "Students add social comparison intensity, sleep disruption, or FOMO activation to explore how additional psychological mechanisms interact with the core dopamine and attention model.",
    "slides_guide": [
        {
            "num": "Slide 1",
            "title": "Cover",
            "visual": "Title slide with compelling image related to Is Social Media Rewiring Your Brain?",
            "say": "You check your phone 96 times a day. That\'s not a personal choice — it\'s a design specification. Today we investigate why.",
            "do": "Show cover image. Ask: Estimate your daily screen time. Then check your phone\'s actual report. Surprised?",
            "time": "2 min"
        },
        {
            "num": "Slide 2",
            "title": "Learning Objectives",
            "visual": "Learning goals and vocabulary terms with dopamine pathway diagram",
            "say": "Here\'s what you\'ll understand by the end — the neuroscience behind why you can\'t put your phone down.",
            "do": "Have students read objectives aloud. Pre-teach vocabulary with reward circuit diagram showing dopamine pathways.",
            "time": "3 min"
        },
        {
            "num": "Slide 3",
            "title": "Big Question",
            "visual": "Provocative question with split image: phone-addicted teen vs. engaged student",
            "say": "Social media was designed by neuroscientists to be as addictive as possible. Is it physically changing your brain?",
            "do": "Quick-write: Students write honestly about their own social media habits and any effects they\'ve noticed. Save to revisit.",
            "time": "3 min"
        },
        {
            "num": "Slide 4",
            "title": "LEVER Framework",
            "visual": "LEVER steps overview",
            "say": "We\'re going to model how the same dopamine system targeted by addictive substances is being targeted by your phone.",
            "do": "Preview each LEVER step. Emphasize that this is personal — the model describes what\'s happening in THEIR brains right now.",
            "time": "2 min"
        },
        {
            "num": "Slide 5",
            "title": "Activity 1: Components",
            "visual": "Component cards — social media exposure, notification frequency, dopamine sensitivity, attention capacity, cognitive well-being",
            "say": "What are the key parts of this system? What do the platforms control, and what happens inside your brain?",
            "do": "Guide sorting of external vs. internal components. Discuss: What\'s designed by the platform vs. what\'s your brain\'s response?",
            "time": "8 min"
        },
        {
            "num": "Slide 6",
            "title": "Activity 2: Connections",
            "visual": "Relationship arrows between social media and brain components",
            "say": "After 3 hours of TikTok, you try to read a textbook. What does your model predict about Attention Capacity? Why does reading feel impossible?",
            "do": "Students draw arrows showing +/- relationships. Discuss the dopamine downregulation cycle and attention fragmentation.",
            "time": "8 min"
        },
        {
            "num": "Slide 7",
            "title": "Activity 3: Simulation",
            "visual": "Simulation results comparing usage patterns over 30 days",
            "say": "Run each scenario. Compare heavy passive scrolling, mindful active use, and digital detox. The differences are dramatic.",
            "do": "Students run all scenarios, record predictions vs. observations. Discuss what recovery actually looks like neurologically.",
            "time": "10 min"
        },
        {
            "num": "Slide 8",
            "title": "Discoveries",
            "visual": "Key findings summary — social media\'s neurological impact",
            "say": "The science is clear: social media exploits your dopamine system by design, and your brain physically changes in response. But recovery IS possible.",
            "do": "Class discussion of discoveries. Revisit initial reflections — has the model changed how you think about your own usage?",
            "time": "5 min"
        },
        {
            "num": "Slide 9",
            "title": "STEM Challenge",
            "visual": "Engineering challenge: Design a Digital Wellness App",
            "say": "Now use the same neuroscience that makes social media addictive — but in reverse. Design an app that builds healthy digital habits.",
            "do": "Groups design wellness apps using behavioral neuroscience principles from the model. Present and evaluate designs.",
            "time": "12 min"
        }
    ],
    "sort_reasoning": "Social Media Exposure and Notification Frequency are external components because they represent designed inputs from technology platforms that exist before any neurological response begins — the platforms control how content is delivered and how often users are interrupted. Dopamine Sensitivity, Attention Capacity, and Cognitive Well-Being are internal because they emerge from the brain\'s neuroplastic response to those external stimulation patterns over time.",
    "relationships": [
        ("Social Media Exposure to Dopamine Sensitivity", "NEGATIVE (-)", "Chronic high social media exposure floods the reward circuit with dopamine, triggering receptor downregulation that lowers baseline dopamine sensitivity over time."),
        ("Notification Frequency to Attention Capacity", "NEGATIVE (-)", "Frequent notifications train the brain to expect and seek constant interruptions, weakening the neural circuits for sustained attention through neuroplastic reorganization."),
        ("Dopamine Sensitivity to Cognitive Well-Being", "POSITIVE (+)", "Higher dopamine sensitivity means normal activities produce adequate pleasure and motivation, supporting healthy mood, engagement, and executive function."),
        ("Attention Capacity to Cognitive Well-Being", "POSITIVE (+)", "Greater attention capacity supports deeper learning, better emotional regulation, and more effective problem-solving — all core components of cognitive well-being.")
    ],
    "sim_answers": [
        ("Heavy Passive Scrolling", "With 4+ hours of daily passive scrolling and maximum notifications, the model shows progressive decline across all internal components. Dopamine Sensitivity drops as receptors downregulate from chronic overstimulation. Attention Capacity shrinks as rapid-switching circuits strengthen and sustained-attention circuits weaken. Cognitive Well-Being deteriorates as the combined effects impair mood, motivation, and academic performance. After 30 days, the model shows significant measurable changes — consistent with real-world research findings."),
        ("Digital Detox", "After 14 days of zero social media and zero notifications, the model shows gradual but incomplete recovery. Dopamine Sensitivity begins to restore as receptors upregulate in the absence of overstimulation — the first few days are the hardest as the brain experiences dopamine deficit. Attention Capacity improves more slowly because neuroplastic changes require sustained practice of focused activities. The model predicts meaningful improvement by day 14 but not full recovery — consistent with research showing 4-6 weeks for substantial restoration.")
    ],
    "reflection_exemplars": [
        ("Is social media addiction a real addiction?", "Our model reveals striking parallels between social media and substance addiction. Both exploit dopamine pathways: substances flood the system chemically while social media floods it through variable-ratio reinforcement. Both cause receptor downregulation, lowering baseline dopamine sensitivity. Both create compulsive behavior despite negative consequences — people continue scrolling even when they know it\'s making them unhappy. The main difference is degree: substances produce much larger dopamine surges (200-1000% vs. 50-100% for social media), making physical dependence more severe. But the neurological mechanism is fundamentally the same, and the behavioral pattern of compulsive use despite harm meets clinical definitions of addiction."),
        ("Should social media platforms be regulated like addictive substances?", "The model provides evidence that social media exploits the same dopamine pathways as addictive substances, using behavioral design techniques specifically engineered to maximize compulsive engagement. Variable-ratio reinforcement, infinite scroll, autoplay, and notification systems are not accidental — they were designed by behavioral scientists to exploit known neurological vulnerabilities. The adolescent brain is particularly vulnerable because the prefrontal cortex (impulse control) is still developing. This parallels the argument for tobacco regulation: a product designed to be addictive, marketed to vulnerable populations, with documented health harms. Whether regulation is the right policy response involves values, but the scientific case for harm is strong.")
    ],
    "stem_intro": "Present the challenge: A tech company wants to create an app that uses behavioral neuroscience to help people break unhealthy social media habits. Your team must design this app using the same dopamine and reinforcement principles that make platforms addictive — but in reverse. The critical constraint: your app must avoid becoming another source of addictive screen behavior.",
    "stem_concepts": [
        ("Persuasive Design Ethics", "The practice of using psychological principles to influence user behavior through technology design. When used to maximize engagement regardless of user well-being, it\'s manipulation. When used to help users achieve their own goals (like reducing screen time), it\'s ethical persuasion. The line depends on whose interests are served."),
        ("Habit Reversal Training", "A behavioral therapy technique that replaces unwanted habitual behaviors with healthier alternatives. For social media: identifying triggers (boredom, FOMO), awareness of the automatic response (reaching for phone), and substituting a competing response (calling a friend, taking a walk, reading)."),
        ("Dopamine Scheduling", "The practice of intentionally structuring activities to maintain healthy dopamine levels without overstimulation. Includes alternating high-stimulation and low-stimulation activities, scheduling social media windows rather than constant access, and building tolerance for boredom as a path to dopamine system recovery.")
    ],
    "stem_eval": [
        ("Expert (4)", "App design uses specific behavioral neuroscience principles from the model, targets dopamine and attention mechanisms directly, avoids becoming addictive itself, includes measurable outcomes, and addresses the adolescent vulnerability window"),
        ("Proficient (3)", "App addresses dopamine and attention concerns with reasonable neuroscience-based features and some built-in measurement"),
        ("Developing (2)", "App has wellness features but they are generic or not grounded in the specific neurological mechanisms from the model"),
        ("Beginning (1)", "App is incomplete, lacks neuroscience grounding, or risks becoming another addictive screen experience")
    ],
    "support": [
        "Provide a comparison diagram: Slot Machine (pull lever -> random reward -> dopamine -> pull again) vs. Social Media (scroll -> random interesting post -> dopamine -> scroll again)",
        "Use a dopamine timeline graphic showing baseline sensitivity over 30 days of heavy use vs. 14 days of detox recovery",
        "Sentence frames: \'When Social Media Exposure is ___ and Notification Frequency is ___, Dopamine Sensitivity ___ because the brain\'s reward circuit ___\'"
    ],
    "extensions": [
        "Watch and analyze \'The Social Dilemma\' documentary — which claims are supported by the neuroscience in your model, and which are exaggerated or unsupported?",
        "Research the proposed Kids Online Safety Act (KOSA) — does the neuroscience evidence from your model support or undermine the argument for legislative regulation of social media for minors?",
        "Design and conduct a self-experiment: track your screen time, attention span (using a sustained attention test app), and mood for one week of normal use and one week of reduced use. Compare results to your model\'s predictions."
    ],
    "cross_curr": [
        ("Math", "Calculate the cumulative dopamine overstimulation from social media: if each notification produces a 50% dopamine surge lasting 30 seconds, and you receive 80 notifications per day, what is the total \'dopamine exposure\' over a month? Compare to baseline levels and discuss receptor downregulation thresholds."),
        ("ELA", "Write an argumentative essay taking a position on whether social media companies should be legally liable for designing addictive products that harm adolescent brain development, using neuroscience evidence from your model"),
        ("Economics", "Analyze the attention economy: social media platforms sell your attention to advertisers. Calculate the revenue per user-hour for major platforms. How does this business model create incentives to maximize addictive design rather than user well-being?")
    ],
    "misconceptions": [
        ("Social media is just a tool — it\'s how you use it that matters", "While usage patterns do affect outcomes (passive scrolling is worse than active creation), the platforms themselves are engineered to exploit neurological vulnerabilities. Variable-ratio reinforcement, infinite scroll, autoplay, algorithmic content curation, and notification systems are deliberate design choices made by behavioral scientists to maximize time-on-platform. Saying social media is \'just a tool\' ignores that the tool was specifically designed to be addictive. A hammer is just a tool. A slot machine is a tool designed to exploit dopamine pathways — and so is social media.", "Compare: A knife is a neutral tool. A slot machine is a tool designed to exploit your brain. Which one is social media more like? Have students identify the specific design features in their favorite apps that map to behavioral addiction mechanisms."),
        ("I can stop anytime I want — I\'m not addicted", "The model shows that dopamine downregulation happens gradually and below conscious awareness. Most people don\'t recognize their baseline has shifted until they try to stop — and experience the restlessness, boredom, and irritability of dopamine deficit. Research shows that 50% of teens describe themselves as \'addicted\' to their phones, and most who attempt digital detox fail within the first 72 hours. The hallmark of addiction is continued use despite negative consequences and difficulty stopping despite wanting to.", "Challenge students: Put your phone in a locked drawer for 24 hours (including sleeping hours). Journal how you feel at 1 hour, 4 hours, 8 hours, and 24 hours. If you can\'t do it, or if you feel significant distress, what does that reveal?"),
        ("Attention spans aren\'t really getting shorter — that\'s just older people complaining", "Measurable data contradicts this. Gloria Mark\'s research at UC Irvine tracked attention span on screens from 2004-2023, showing a decline from 2.5 minutes to 47 seconds. Standardized cognitive testing shows declining sustained attention scores in heavy social media users. Brain imaging studies show reduced gray matter volume in the prefrontal cortex of heavy users — the same region that controls sustained attention. This isn\'t generational bias — it\'s neuroscience measured with fMRI machines and standardized tests.", "Show the data: Gloria Mark\'s graph of declining screen attention spans from 2004-2023. Ask students to honestly self-report how long they can read a textbook without checking their phone. Compare their answers to the research data.")
    ]
}

L10 = {
    "id": "G12L1-L10",
    "title": "How Can One Mutation Change Everything?",
    "subtitle": "Modeling Gene Mutations, Protein Structure, and Phenotypic Variation",
    "ngss": "HS-LS3-2",
    "ngss_desc": "Make and defend a claim based on evidence that inheritable genetic variations may result from (1) new genetic combinations through meiosis, (2) viable errors occurring during replication, and (3) mutations caused by environmental factors.",
    "big_question": "A single change in one letter of your DNA — out of 3.2 billion — can cause sickle cell disease, give you red hair, protect you from HIV, or increase your cancer risk. How can one tiny mutation in a gene have such massive effects on an organism, and why do some mutations help while others harm?",
    "objectives": [
        "Model how point mutations, insertions, and deletions alter DNA sequences and produce changed proteins with different structures and functions",
        "Explain why the phenotypic impact of a mutation depends on its location in the gene, the type of change, and the protein\'s functional tolerance for variation",
        "Predict whether a given mutation will be harmful, neutral, or beneficial based on its effect on protein structure and function",
        "Analyze why genetic variation from mutations is the raw material for evolution and why most mutations are neutral rather than harmful"
    ],
    "vocabulary": [
        ("Point Mutation", "A change in a single nucleotide base in the DNA sequence — can be silent (no effect on protein), missense (changes one amino acid), or nonsense (creates a premature stop codon), with vastly different phenotypic consequences depending on location and type"),
        ("Frameshift Mutation", "An insertion or deletion of nucleotides that is not a multiple of three, shifting the entire reading frame of the genetic code downstream — typically devastating because every amino acid after the mutation is wrong, usually producing a nonfunctional protein"),
        ("Phenotypic Variation", "Observable differences in traits among individuals caused by underlying genetic differences — the visible expression of genotypic variation, ranging from trivial (hair color) to life-threatening (sickle cell disease) depending on which protein is affected"),
        ("Protein Folding", "The process by which a linear amino acid chain folds into a specific three-dimensional structure that determines its function — even a single amino acid change can destabilize folding, creating a misfolded protein that cannot perform its biological role")
    ],
    "components": [
        ("Mutation Type", "The category of genetic change — point mutations (substitutions), insertions, and deletions each alter the DNA sequence differently, with frameshift mutations generally being more disruptive than single-base substitutions", True),
        ("Gene Location", "Where in the genome the mutation occurs — mutations in coding regions affect protein sequence directly, mutations in regulatory regions affect gene expression levels, and mutations in non-coding regions are usually silent", True),
        ("Protein Structure Change", "The degree to which the mutation alters the three-dimensional folding and shape of the encoded protein — ranges from no change (silent mutation) to complete misfolding (frameshift or critical-site missense mutation)", False),
        ("Protein Function", "How well the mutated protein performs its biological role — directly determined by structural change; a slightly altered structure may retain partial function, while a severely misfolded protein is typically nonfunctional or toxic", False),
        ("Phenotypic Impact", "The observable effect of the mutation on the organism\'s traits, health, or fitness — determined by how much protein function changes and how critical that protein is to the organism\'s survival and reproduction", False)
    ],
    "think_about_it": "Sickle cell disease is caused by a single point mutation: one A changed to a T in the hemoglobin gene, replacing glutamic acid with valine. This changes ONE amino acid out of 147 in the protein. How does your model explain why such a tiny change has such a massive Phenotypic Impact?",
    "scenarios": [
        ("Silent Mutation", "Set Mutation Type to point mutation (synonymous substitution) in a coding region — observe how the redundancy of the genetic code means no amino acid change, no protein change, and no phenotypic effect"),
        ("Missense Mutation in Critical Site", "Set Mutation Type to point mutation (missense) at an active site of an essential protein — observe how a single amino acid change disrupts Protein Structure, destroys Protein Function, and produces severe Phenotypic Impact"),
        ("Frameshift in Early Gene", "Set Mutation Type to single-base insertion early in a gene\'s coding sequence — observe how the reading frame shift changes every downstream amino acid, producing a completely nonfunctional protein")
    ],
    "sim_scenarios": [
        ("Silent Change", "Mutation Type: Point (synonymous) | Gene Location: Coding region, non-critical site | Protein: Hemoglobin", "When a mutation changes the DNA but NOT the amino acid (due to genetic code redundancy), what happens to Phenotypic Impact?"),
        ("Sickle Cell Mutation", "Mutation Type: Point (missense, E6V) | Gene Location: HBB gene, position 6 | Protein: Hemoglobin beta chain", "The sickle cell mutation changes just one amino acid. Why does the model predict such severe Phenotypic Impact from this tiny change?"),
        ("Frameshift Disaster", "Mutation Type: Single base insertion | Gene Location: Early in CFTR gene coding region | Protein: CFTR chloride channel", "What happens when a frameshift mutation near the beginning of a gene scrambles the entire downstream protein sequence?")
    ],
    "discoveries": [
        "The genetic code\'s redundancy provides a buffer: about 25% of all possible point mutations are silent because multiple codons code for the same amino acid, producing no phenotypic effect whatsoever",
        "Location matters enormously — the same type of mutation (missense) can be harmless in one part of a protein and fatal in another, depending on whether the changed amino acid is at a structurally or functionally critical site",
        "Frameshift mutations are almost always devastating because they change every amino acid downstream of the insertion or deletion, producing a completely different and usually nonfunctional protein",
        "Most mutations are neutral or slightly harmful — beneficial mutations are rare but provide the raw genetic variation that natural selection acts upon to drive evolution"
    ],
    "answer": "One mutation can change everything because proteins are molecular machines whose function depends entirely on their precise three-dimensional structure — and structure is determined by amino acid sequence, which is determined by DNA sequence. A single nucleotide change can alter one amino acid, which can destabilize the entire protein\'s folding, which can destroy its function, which can cause disease or death. The sickle cell mutation changes just one amino acid (glutamic acid to valine) in hemoglobin, but this causes hemoglobin molecules to polymerize into rigid fibers that distort red blood cells into sickle shapes, blocking blood flow and causing organ damage. However, most mutations are not this dramatic — the genetic code\'s redundancy means many mutations are silent, and many amino acid changes occur at positions that tolerate variation. Whether a mutation helps, harms, or does nothing depends on what protein it affects, where in that protein the change occurs, and what function that protein serves in the organism.",
    "stem_title": "Design a Genetic Screening Decision Tool",
    "stem_mission": "Design a decision-support tool that helps genetic counselors explain to patients what their specific gene mutations mean — distinguishing between harmful, neutral, and potentially beneficial variants using the protein structure-function model.",
    "stem_scenario": "A genetics clinic receives hundreds of patient genome sequences each week, each containing thousands of mutations compared to the reference genome. Most mutations are harmless, but a few may cause disease. Genetic counselors need a tool that uses the principles from your model — mutation type, gene location, protein structure change, and functional impact — to rapidly classify mutations and explain results to patients in understandable terms.",
    "stem_questions": [
        "What criteria from your model best predict whether a specific mutation will be harmful, neutral, or beneficial?",
        "How can you communicate the uncertainty of mutation classification to patients without causing unnecessary panic?",
        "What does your model reveal about why the same mutation can have different severity in different individuals?"
    ],
    "stem_design_qs": [
        "What specific model-based criteria does your tool use to classify mutations as harmful, neutral, or potentially beneficial?",
        "How does your tool communicate complex genetic information to patients without scientific training?",
        "What model evidence supports your classification criteria, and how does your tool handle uncertain or ambiguous mutations?",
        "How does your tool account for the fact that phenotypic impact can vary between individuals carrying the same mutation?"
    ],
    "career": "Genetic counselors help patients understand genetic test results and make health decisions, earning $80,000-$110,000/year. Bioinformaticians who analyze genome sequences and classify mutation variants earn $75,000-$140,000/year. Structural biologists studying protein folding and mutation effects work in pharmaceutical and biotech companies, earning $80,000-$160,000/year.",
    "images": {
        "cover": ("G12L1-L10-cover.png", "A photorealistic close-up of diverse 17-18 year old students in a modern genetics lab examining 3D protein structure models on a large display, with DNA sequence data visible on screens, dramatic lighting"),
        "landscape": ("G12L1-L10-landscape.png", "A diverse group of 17-18 year old students in a modern biology classroom with protein folding models on desks and a smartboard showing DNA mutation comparisons, engaged in collaborative analysis"),
        "modeling": ("G12L1-L10-modeling.png", "Diverse 17-18 year old students working on laptops building computational models of mutation effects on protein structure, classroom walls showing the genetic code table and protein folding diagrams"),
        "discussion": ("G12L1-L10-discussion.png", "A teacher leading a discussion with diverse 17-18 year old students about genetic mutations and their effects, normal vs. sickle cell hemoglobin comparison displayed on the smartboard"),
        "stem": ("G12L1-L10-stem.png", "Diverse 17-18 year old students designing a genetic screening decision tool on whiteboards and laptops, with mutation classification flowcharts and patient communication materials visible")
    },
    "pre_assessment": [
        "What is a mutation? Is it always a bad thing? Explain your thinking with any examples you know.",
        "How do you think a change in DNA can affect the way your body looks or functions?",
        "If every human has millions of mutations compared to each other, why aren\'t we all sick? What does that suggest about most mutations?",
        "Have you heard of sickle cell disease or cystic fibrosis? What do you know about what causes them at the genetic level?"
    ],
    "extend_components": [
        ("Epigenetic Modification", "Chemical changes to DNA or histone proteins that alter gene expression without changing the DNA sequence — can amplify or suppress the phenotypic impact of a mutation by changing how much of the mutated protein is actually produced"),
        ("Genetic Background", "The combined effect of all other genes in an individual\'s genome — modifier genes can enhance or suppress the phenotypic impact of a specific mutation, explaining why the same mutation causes severe disease in one person and mild symptoms in another"),
        ("Environmental Interaction", "External factors like diet, temperature, UV exposure, and chemical exposure that interact with genotype to determine phenotype — some mutations are only harmful under specific environmental conditions, revealing gene-environment interactions")
    ],
    "reflections": [
        "How does your model explain why a single amino acid change can sometimes cause fatal disease and sometimes have no effect at all?",
        "Why is the redundancy of the genetic code (multiple codons for the same amino acid) an important buffer against mutation damage?",
        "Your model shows that frameshift mutations are almost always devastating. Why is the reading frame so important for protein function?",
        "If most mutations are neutral, why do people associate the word \'mutation\' with disease and danger? How does your model challenge that assumption?",
        "How does genetic variation from mutations connect to evolution by natural selection? Why are mutations essential for adaptation?"
    ],
    "dimensions": [
        ("Science Practice", "Engaging in Argument from Evidence", "Students make and defend claims about whether specific mutations will be harmful, neutral, or beneficial, using evidence from their model about mutation type, protein structure change, and functional impact."),
        ("Disciplinary Core Idea", "LS3.B Variation of Traits", "Genetic variations result from mutations during DNA replication and from environmental mutagens; these variations alter protein structure and function, producing phenotypic variation that ranges from undetectable to lethal depending on the protein and position affected."),
        ("Crosscutting Concept", "Structure and Function", "Students connect DNA sequence structure to protein three-dimensional structure to biological function, understanding how a change at one structural level cascades through to produce observable phenotypic effects.")
    ],
    "cast_items": [
        "Make and defend a claim about whether a described mutation will be harmful, neutral, or beneficial based on its predicted effect on protein structure and function",
        "Predict the phenotypic impact of different mutation types (silent, missense, nonsense, frameshift) based on their location in the gene and effect on the encoded protein",
        "Explain why genetic variation from mutations is the essential raw material for evolution by natural selection"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A point mutation changes codon 6 of the hemoglobin beta gene from GAG (glutamic acid) to GTG (valine). Based on the mutation-protein-phenotype model, why does this single amino acid change at this specific location cause the severe symptoms of sickle cell disease?"),
        ("Constructed Response:", "Using your model, explain why a frameshift mutation caused by a single base insertion at position 10 of a 500-amino-acid protein is likely to be more damaging than a missense mutation at position 450 of the same protein. Reference Protein Structure Change, Protein Function, and Phenotypic Impact in your answer.")
    ],
    "background_intro": "Every time a cell divides, its entire genome — 3.2 billion base pairs — must be copied. DNA polymerase is remarkably accurate, making only about 1 error per billion base pairs copied. But with 37 trillion cells in the human body dividing regularly, mutations are inevitable. Most are repaired by proofreading enzymes, but some persist. Understanding how these changes in DNA sequence translate to changes in protein structure, function, and ultimately observable traits is fundamental to genetics, medicine, and evolution.",
    "background_sections": [
        ("From DNA to Protein: The Central Dogma", "The flow of genetic information follows the central dogma: DNA is transcribed into mRNA, which is translated into protein by ribosomes reading three-nucleotide codons. Each codon specifies one of 20 amino acids (or a stop signal). The amino acid sequence determines how the protein folds into its three-dimensional structure, and this structure determines the protein\'s function. A mutation in DNA changes the mRNA, which can change the amino acid sequence, which can change protein folding, which can change function. This cascade — sequence to structure to function — is why a single DNA change can have system-wide effects."),
        ("Types of Mutations and Their Effects", "Point mutations (single nucleotide changes) come in three categories: silent/synonymous (no amino acid change due to genetic code redundancy — about 25% of all possible point mutations), missense (different amino acid — effects range from undetectable to fatal depending on location), and nonsense (premature stop codon — usually produces a truncated, nonfunctional protein). Insertions and deletions that aren\'t multiples of three cause frameshift mutations that scramble the entire downstream reading frame. Large-scale mutations include chromosomal duplications, deletions, inversions, and translocations that affect thousands of genes simultaneously."),
        ("Why Location Determines Impact", "Not all positions in a protein are equally important. Active sites (where enzymes catalyze reactions), binding sites (where proteins interact with other molecules), and structural core residues (that maintain three-dimensional shape) are highly sensitive to amino acid changes — mutations at these sites often destroy function. Surface residues and flexible loop regions are more tolerant of substitution. Similarly, mutations in regulatory regions (promoters, enhancers) can change when, where, and how much protein is produced without changing the protein itself — sometimes with dramatic phenotypic effects like cancer when tumor suppressors are silenced."),
        ("Mutations as Raw Material for Evolution", "While most attention focuses on harmful mutations, the majority of mutations are neutral — they occur in non-coding DNA, produce silent changes, or affect tolerant positions in proteins. These neutral mutations accumulate over generations and serve as the raw material for evolution. Occasionally, a mutation produces a protein variant that works better in a specific environment — like the hemoglobin S variant that protects against malaria in heterozygous carriers. Natural selection acts on this variation: beneficial mutations increase in frequency, harmful ones are removed, and neutral ones drift randomly. Without mutations, there would be no genetic variation and no evolution.")
    ],
    "lever_L": "Students identify mutation type, gene location, protein structure change, protein function, and phenotypic impact as the key components of the mutation-to-phenotype system.",
    "lever_E": "Students determine that mutation type and gene location together determine the degree of protein structure change, that structural change directly affects protein function, and that the criticality of the affected protein determines phenotypic impact.",
    "lever_V": "Students build a computational model showing how different mutations at different gene locations cascade through protein structure and function to produce varying degrees of phenotypic impact.",
    "lever_Ev": "Students run silent mutation, critical missense, and frameshift scenarios to test predictions about which combinations of mutation type and location produce harmful, neutral, or beneficial phenotypic outcomes.",
    "lever_R": "Students add epigenetic modification, genetic background, or environmental interaction to explore why the same mutation can produce different phenotypes in different individuals or conditions.",
    "slides_guide": [
        {
            "num": "Slide 1",
            "title": "Cover",
            "visual": "Title slide with compelling image related to How Can One Mutation Change Everything?",
            "say": "One letter changed out of 3.2 billion. That\'s all it takes to cause sickle cell disease — or to protect against HIV. Today we model why.",
            "do": "Show cover image. Ask: What comes to mind when you hear the word \'mutation\'? Quick share-out — note how many responses are negative.",
            "time": "2 min"
        },
        {
            "num": "Slide 2",
            "title": "Learning Objectives",
            "visual": "Learning goals and vocabulary terms with genetic code chart",
            "say": "Here\'s what you\'ll understand by the end — how to predict whether a mutation will help, harm, or do nothing at all.",
            "do": "Have students read objectives aloud. Pre-teach vocabulary with visual showing DNA to protein pathway and mutation types.",
            "time": "3 min"
        },
        {
            "num": "Slide 3",
            "title": "Big Question",
            "visual": "Provocative question with image showing normal vs. sickle cell red blood cells",
            "say": "One amino acid. Out of 147. Changes a round, flexible red blood cell into a rigid sickle that blocks blood vessels. How?",
            "do": "Quick-write: Students hypothesize how a single DNA change could have system-wide effects. Save to compare with model evidence.",
            "time": "3 min"
        },
        {
            "num": "Slide 4",
            "title": "LEVER Framework",
            "visual": "LEVER steps overview",
            "say": "We\'re going to model the cascade from DNA change to protein change to whole-organism effect — one of biology\'s most important chains of causation.",
            "do": "Preview each LEVER step. Emphasize that this model connects molecular biology to observable traits.",
            "time": "2 min"
        },
        {
            "num": "Slide 5",
            "title": "Activity 1: Components",
            "visual": "Component cards — mutation type, gene location, protein structure change, protein function, phenotypic impact",
            "say": "What are the key parts of this system? What determines the input, and what emerges from the biology?",
            "do": "Guide sorting of external vs. internal components. Discuss: Scientists control where to look, but biology determines the outcome.",
            "time": "8 min"
        },
        {
            "num": "Slide 6",
            "title": "Activity 2: Connections",
            "visual": "Relationship arrows between mutation-protein-phenotype components",
            "say": "A missense mutation at an enzyme\'s active site vs. at a surface loop — same mutation type, dramatically different Phenotypic Impact. Why?",
            "do": "Students draw arrows showing +/- relationships. Discuss why location in the protein matters as much as the type of mutation.",
            "time": "8 min"
        },
        {
            "num": "Slide 7",
            "title": "Activity 3: Simulation",
            "visual": "Simulation results comparing silent, missense, and frameshift mutations",
            "say": "Run each scenario. The silent mutation, the sickle cell missense, and the frameshift. Watch how the cascade plays out differently each time.",
            "do": "Students run all scenarios, record predictions vs. observations. Discuss why most mutations are actually neutral.",
            "time": "10 min"
        },
        {
            "num": "Slide 8",
            "title": "Discoveries",
            "visual": "Key findings summary — the mutation spectrum from neutral to devastating",
            "say": "Most mutations are nothing. Some are everything. Your model reveals what determines which is which.",
            "do": "Class discussion of discoveries. Challenge the \'mutations are bad\' assumption — most are neutral, and some are essential for evolution.",
            "time": "5 min"
        },
        {
            "num": "Slide 9",
            "title": "STEM Challenge",
            "visual": "Engineering challenge: Design a Genetic Screening Decision Tool",
            "say": "Now apply your model. A genetics clinic needs to classify thousands of mutations quickly. Your tool must predict which ones matter.",
            "do": "Groups design classification tools using model criteria. Present and evaluate using real mutation examples.",
            "time": "12 min"
        }
    ],
    "sort_reasoning": "Mutation Type and Gene Location are external components because they represent the specific characteristics of the genetic change — what kind of mutation occurred and where in the genome it happened — which are determined before the biological consequences play out. Protein Structure Change, Protein Function, and Phenotypic Impact are internal because they emerge from how the cell processes the mutated DNA through transcription, translation, and protein folding into observable biological effects.",
    "relationships": [
        ("Mutation Type to Protein Structure Change", "POSITIVE (+)", "More disruptive mutation types (frameshift > nonsense > missense > silent) cause greater changes to the protein\'s amino acid sequence, producing larger structural disruptions."),
        ("Gene Location to Protein Structure Change", "POSITIVE (+)", "Mutations at functionally critical gene locations (active sites, structural cores) produce greater protein structure changes than mutations at tolerant positions (surface loops, non-coding regions)."),
        ("Protein Structure Change to Protein Function", "NEGATIVE (-)", "Greater structural changes disrupt the protein\'s three-dimensional shape, reducing or destroying its ability to perform its biological role."),
        ("Protein Function to Phenotypic Impact", "NEGATIVE (-)", "Reduced protein function affects the biological processes that protein supports; the more critical the protein and the greater the functional loss, the more severe the observable phenotypic effect.")
    ],
    "sim_answers": [
        ("Silent Mutation", "With a synonymous point mutation in a coding region, the genetic code\'s redundancy means the same amino acid is produced despite the DNA change. Protein Structure Change is zero, Protein Function is unchanged, and Phenotypic Impact is nil. This demonstrates why about 25% of all possible point mutations are invisible to natural selection — they literally do not change the protein. This is a major source of neutral genetic variation used for population genetics studies."),
        ("Missense Mutation in Critical Site", "The sickle cell mutation (E6V in hemoglobin) changes a single charged amino acid (glutamic acid) to a hydrophobic one (valine) at position 6 of the beta chain. The model shows moderate Protein Structure Change — the overall fold is mostly preserved, but the surface chemistry changes dramatically. This creates a hydrophobic patch that causes hemoglobin molecules to polymerize into rigid fibers under low oxygen conditions. Protein Function is severely compromised, and Phenotypic Impact is devastating: sickle-shaped red blood cells, vaso-occlusive crises, organ damage. The model illustrates how one amino acid at a critical position can cascade to system-wide effects."),
        ("Frameshift in Early Gene", "A single base insertion early in the coding sequence shifts the entire reading frame, producing a completely different amino acid sequence for the remainder of the protein. The model shows maximum Protein Structure Change — the protein cannot fold correctly because virtually every amino acid after the insertion is wrong. Protein Function drops to zero, and Phenotypic Impact depends on the protein\'s importance: for essential proteins like CFTR (cystic fibrosis), the result is severe disease.")
    ],
    "reflection_exemplars": [
        ("Why are most mutations neutral rather than harmful?", "Our model reveals three key reasons. First, genetic code redundancy: about 25% of point mutations are silent because multiple codons specify the same amino acid — the DNA changes but the protein doesn\'t. Second, most of the human genome (over 98%) is non-coding, so random mutations are far more likely to land in regions that don\'t encode proteins. Third, even within proteins, many amino acid positions are tolerant of substitution — surface residues and flexible loops can often accommodate different amino acids without significant structural or functional change. The model shows that devastating mutations like sickle cell are actually the exception, not the rule. This is important because it means genetic variation — the raw material for evolution — can accumulate without killing the organism."),
        ("How does the sickle cell mutation illustrate gene-environment interaction?", "The sickle cell mutation (E6V) is a perfect case study in context-dependent phenotypic impact. In homozygous individuals (two copies), it causes severe sickle cell disease. But in heterozygous carriers (one copy), the model shows a different outcome: enough normal hemoglobin is produced to prevent sickling under most conditions, while the sickle hemoglobin makes red blood cells inhospitable to the malaria parasite. In malaria-endemic regions, carriers have a survival advantage over both non-carriers (who die of malaria) and homozygous individuals (who die of sickle cell). This is heterozygote advantage — a mutation that is simultaneously harmful, neutral, and beneficial depending on genetic dosage and environmental context.")
    ],
    "stem_intro": "Present the challenge: A genetics clinic processes hundreds of patient genomes each week, each containing thousands of variants compared to the reference genome. Your team must design a decision-support tool that uses the principles from your mutation-protein-phenotype model to help genetic counselors rapidly classify mutations as harmful, neutral, or potentially beneficial, and communicate these classifications to patients clearly.",
    "stem_concepts": [
        ("Variant Classification", "The American College of Medical Genetics (ACMG) classifies genetic variants into five categories: pathogenic, likely pathogenic, variant of uncertain significance (VUS), likely benign, and benign. This classification uses evidence about mutation type, location, protein effect, population frequency, and clinical data — directly paralleling your model\'s components."),
        ("Genetic Counseling Communication", "Translating complex genetic information into language that patients can understand and act upon. Key challenges include explaining probabilistic risk (a mutation increases risk by X%, not guarantees disease), conveying uncertainty (VUS classifications), and avoiding unnecessary anxiety while ensuring informed decision-making."),
        ("Personalized Medicine", "Using individual genetic information to guide medical decisions — including drug selection, dosing, screening schedules, and preventive interventions. Understanding mutation impact on protein function is the foundation of pharmacogenomics and precision medicine.")
    ],
    "stem_eval": [
        ("Expert (4)", "Tool uses specific model-based criteria (mutation type, location, protein structure change, functional impact) to classify variants, communicates uncertainty clearly, includes patient-friendly explanations, and accounts for variable penetrance"),
        ("Proficient (3)", "Tool has reasonable classification criteria based on model principles and includes some patient communication guidance"),
        ("Developing (2)", "Tool identifies some classification criteria but logic is incomplete or patient communication is overly technical"),
        ("Beginning (1)", "Tool is incomplete, uses oversimplified binary classification, or does not connect to the mutation-protein-phenotype model")
    ],
    "support": [
        "Provide a visual cascade diagram: DNA Change -> mRNA Change -> Amino Acid Change -> Protein Folding Change -> Function Change -> Trait Change, with branching paths for silent vs. missense vs. frameshift",
        "Use a color-coded genetic code table where students can look up whether a specific nucleotide change is silent, missense, or nonsense",
        "Sentence frames: \'This mutation is predicted to be ___ because the ___ change at ___ position in the protein will ___ protein folding, which will ___ function\'"
    ],
    "extensions": [
        "Research the CCR5-delta32 mutation that provides resistance to HIV infection — how does a loss-of-function mutation in a surface receptor become beneficial, and what does this reveal about the context-dependency of mutation effects?",
        "Investigate how cancer arises from accumulated mutations in proto-oncogenes and tumor suppressor genes — use your model to explain why cancer is a disease of multiple mutations rather than a single genetic change",
        "Use protein structure databases (like RCSB PDB) to visualize the actual 3D structure of normal hemoglobin vs. the sickle cell variant — how does one amino acid change alter the protein\'s surface chemistry and cause polymerization?"
    ],
    "cross_curr": [
        ("Math", "Calculate the probability of a specific point mutation occurring in the hemoglobin gene given the human mutation rate (1.1 x 10^-8 per base per generation), the gene length (1,600 base pairs), and the global birth rate. How many babies per year are expected to carry a new HBB mutation?"),
        ("ELA", "Write a patient-friendly explanation of a genetic test result that shows a \'variant of uncertain significance\' in a cancer-risk gene, balancing scientific accuracy with compassion and avoiding unnecessary alarm"),
        ("History", "Research how the geographic distribution of the sickle cell allele maps onto historical malaria-endemic regions. How does this pattern provide evidence for natural selection and the heterozygote advantage hypothesis?")
    ],
    "misconceptions": [
        ("All mutations are harmful", "The vast majority of mutations are neutral — they either occur in non-coding DNA, produce silent changes due to genetic code redundancy, or affect tolerant positions in proteins. Of the mutations that do affect protein function, many cause only minor changes that the organism can compensate for. Truly harmful mutations are a small minority, and beneficial mutations (though rare) are the essential raw material for evolution. Without mutations, there would be no genetic variation and no adaptive evolution.", "Ask: If mutations were always harmful, how would species ever adapt to changing environments? Evolution requires genetic variation, and mutations are the ultimate source. Have students estimate what fraction of their own ~100 new mutations are in coding regions (answer: about 1-2)."),
        ("A single mutation directly causes a single trait change", "The relationship between genotype and phenotype is rarely one-to-one. Most traits are polygenic (influenced by many genes), and most genes are pleiotropic (affecting multiple traits). The sickle cell mutation affects hemoglobin but the downstream consequences include blood flow, oxygen delivery, organ function, malaria resistance, and bone development. Environmental factors, epigenetic modifications, and other genes all modify how a mutation expresses as a phenotype. The model simplifies this to make the mechanism clear, but reality involves multiple interacting layers.", "Use the sickle cell example: One mutation in one gene produces effects on blood cells, blood vessels, spleen, kidneys, lungs, bones, and malaria susceptibility. Draw a map of all these downstream effects from one amino acid change. Is this really a \'single trait change\'?"),
        ("Mutations are random, so they can\'t produce organized adaptation", "Mutations ARE random with respect to whether they\'ll be helpful — the cell doesn\'t \'know\' what mutations would be beneficial. But natural selection is decidedly non-random. Selection consistently preserves beneficial mutations and removes harmful ones over generations. The combination of random mutation + non-random selection is what produces organized adaptation. Our model shows that even though most mutations are neutral or harmful, the rare beneficial ones — like CCR5-delta32 for HIV resistance or hemoglobin S for malaria resistance — can sweep through populations when they provide a survival advantage.", "Analogy: Imagine typing random letters on a keyboard (mutations). Most produce gibberish. But if a spell-checker deletes everything except real words (natural selection), eventually meaningful text emerges. The randomness of input doesn\'t prevent organized output when there\'s a selection filter.")
    ]
}

ALL_LESSONS = [L01, L02, L03, L04, L05, L06, L07, L08, L09, L10]
