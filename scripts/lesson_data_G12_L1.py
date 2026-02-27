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

ALL_LESSONS = [L01, L02, L03, L04, L05]
