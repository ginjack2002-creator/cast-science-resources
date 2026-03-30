#!/usr/bin/env python3
"""Multiple choice pre/post assessment questions for Grade 12 Level 1 ModelIt! Lessons"""

# =============================================================================
# L01 — Why Does Your Brain Lie to You? (HS-LS1-2)
# =============================================================================
L01_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A student is convinced she saw a dog run across the street, but security footage shows it was a plastic bag blown by wind. Which explanation best accounts for this perceptual error?",
            "choices": {
                "A": "The brain uses prior experience to fill in ambiguous sensory data, sometimes generating false perceptions",
                "B": "The student's eyes were not functioning correctly at the time of the observation",
                "C": "The brain randomly generates images that have no connection to sensory input",
                "D": "Perceptual errors only occur in people with below-average intelligence"
            },
            "correct": "A",
            "feedback_correct": "Correct. The brain relies on prior experience and heuristics to interpret ambiguous sensory input, which can produce systematic perceptual errors even in healthy individuals.",
            "feedback_incorrect": "Incorrect. Perceptual errors are a normal feature of neural processing. When sensory input is ambiguous, the brain uses prior experience to 'fill in' what it expects to see, sometimes generating false perceptions."
        },
        {
            "question": "Two scientists analyze the same climate dataset and reach opposite conclusions. Which concept from neuroscience most directly explains this phenomenon?",
            "choices": {
                "A": "One scientist must have made a mathematical error in the analysis",
                "B": "Confirmation bias causes each scientist to selectively attend to data supporting their pre-existing beliefs",
                "C": "Scientific data is always ambiguous and can never support any conclusion",
                "D": "Scientists with more education are always more accurate in their interpretations"
            },
            "correct": "B",
            "feedback_correct": "Correct. Confirmation bias causes people to search for, interpret, and remember information that confirms their pre-existing beliefs while ignoring contradictory evidence.",
            "feedback_incorrect": "Incorrect. Confirmation bias is a well-documented cognitive bias where prior beliefs shape how new evidence is interpreted, causing two people to draw different conclusions from identical data."
        },
        {
            "question": "What is a heuristic in the context of cognitive science?",
            "choices": {
                "A": "A type of brain damage that impairs decision-making ability",
                "B": "A mental shortcut the brain uses for quick decisions that is efficient but prone to systematic errors",
                "C": "A conscious, deliberate strategy for solving complex problems step by step",
                "D": "A rare cognitive ability found only in experts with years of training"
            },
            "correct": "B",
            "feedback_correct": "Correct. Heuristics are mental shortcuts that allow the brain to make rapid decisions without analyzing all available data. They work well most of the time but produce predictable errors in specific situations.",
            "feedback_incorrect": "Incorrect. Heuristics are mental shortcuts used by everyone's brain to make fast decisions. They are efficient most of the time but produce systematic, predictable errors called cognitive biases."
        },
        {
            "question": "A student claims that highly intelligent people are less susceptible to cognitive biases. Based on neuroscience research, which response is most accurate?",
            "choices": {
                "A": "This is correct; intelligence fully protects against cognitive biases",
                "B": "Intelligence has no relationship to cognitive processing at all",
                "C": "Expertise can actually increase certain biases because strong prior knowledge shapes interpretation of ambiguous information",
                "D": "Only people with cognitive disabilities experience biases"
            },
            "correct": "C",
            "feedback_correct": "Correct. Research shows that expertise can increase confirmation bias because experts have stronger prior beliefs that more powerfully shape how they interpret new, ambiguous evidence.",
            "feedback_incorrect": "Incorrect. Cognitive biases are features of neural processing in all brains. Experts can actually be more biased in their area of expertise because their strong prior knowledge more powerfully filters new information."
        },
        {
            "question": "When would a person's cognitive biases be MOST likely to influence their decision-making?",
            "choices": {
                "A": "When they are well-rested, have clear data, and no prior expectations",
                "B": "When sensory input is clear and unambiguous with low cognitive load",
                "C": "When they are stressed, fatigued, and processing ambiguous information with strong prior beliefs",
                "D": "When they are making decisions in their area of least experience"
            },
            "correct": "C",
            "feedback_correct": "Correct. Biases are strongest when cognitive load is high (stress, fatigue), sensory input is ambiguous, and prior experience is strong, because the brain relies more heavily on shortcuts under these conditions.",
            "feedback_incorrect": "Incorrect. Cognitive biases are amplified by high cognitive load (stress/fatigue), ambiguous information, and strong prior beliefs. Under these conditions, the brain shifts from careful analysis to quick heuristic shortcuts."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the cognitive bias model, what happens to Decision Accuracy when Sensory Input is weak and Prior Experience is very strong?",
            "choices": {
                "A": "Decision Accuracy increases because strong prior experience compensates for weak sensory data",
                "B": "Decision Accuracy decreases because the brain fills in gaps with expectations rather than evidence, increasing Bias Strength",
                "C": "Decision Accuracy remains unchanged because Sensory Input and Prior Experience are independent variables",
                "D": "Decision Accuracy improves only if Cognitive Load is also high"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that when sensory input is ambiguous and prior experience is strong, the brain fills in gaps with what it expects to see, dramatically increasing Bias Strength and reducing Decision Accuracy.",
            "feedback_incorrect": "Incorrect. The model demonstrates that weak sensory input combined with strong prior experience increases Bias Strength because the brain relies on expectations rather than evidence, which decreases Decision Accuracy."
        },
        {
            "question": "A hospital finds that diagnostic errors increase during long shifts. Based on the cognitive bias model, which mechanism best explains this pattern?",
            "choices": {
                "A": "Doctors become physically unable to see symptoms after working many hours",
                "B": "Increased Cognitive Load from fatigue causes the brain to rely more heavily on heuristic shortcuts, amplifying anchoring and confirmation biases",
                "C": "Patients who arrive during long shifts tend to have more unusual conditions",
                "D": "Diagnostic protocols are only designed to work during short shifts"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that high Cognitive Load (from fatigue, stress, multitasking) forces the brain to shift from careful, analytical processing to faster heuristic shortcuts, amplifying all biases including anchoring and confirmation bias.",
            "feedback_incorrect": "Incorrect. The model predicts that increased Cognitive Load from fatigue amplifies Bias Strength because the brain shifts from analytical processing to heuristic shortcuts when overwhelmed, increasing the influence of anchoring and confirmation biases."
        },
        {
            "question": "A student adds Metacognition as a component to the cognitive bias model. Based on the model's predictions, how would Metacognition interact with Bias Strength?",
            "choices": {
                "A": "Metacognition would completely eliminate all cognitive biases",
                "B": "Metacognition would act as a moderating variable that reduces but never eliminates the impact of biases on decisions",
                "C": "Metacognition would increase Bias Strength by making people more aware of their beliefs",
                "D": "Metacognition would only affect Decision Accuracy if Cognitive Load is zero"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model predicts that metacognition (awareness of one's own thinking) acts as a moderating variable that can reduce but never fully eliminate bias, since biases are built into the brain's fundamental processing architecture.",
            "feedback_incorrect": "Incorrect. Metacognition moderates Bias Strength by enabling people to recognize when shortcuts might lead to errors, but it cannot eliminate biases entirely because they are fundamental features of neural processing, not optional settings."
        },
        {
            "question": "Which scenario from the cognitive bias model would produce the HIGHEST Decision Accuracy?",
            "choices": {
                "A": "High Sensory Input clarity, low Prior Experience, low Cognitive Load",
                "B": "Low Sensory Input clarity, high Prior Experience, high Cognitive Load",
                "C": "Medium Sensory Input clarity, maximum Prior Experience, low Cognitive Load",
                "D": "Low Sensory Input clarity, low Prior Experience, high Cognitive Load"
            },
            "correct": "A",
            "feedback_correct": "Correct. The model predicts highest Decision Accuracy when sensory data is clear (reducing reliance on expectations), prior beliefs are weak (reducing confirmation bias), and cognitive load is low (allowing analytical rather than heuristic processing).",
            "feedback_incorrect": "Incorrect. Decision Accuracy is maximized when sensory input is strong and unambiguous, prior experience is low (reducing bias from preconceptions), and cognitive load is low (allowing the brain to process information analytically rather than through shortcuts)."
        },
        {
            "question": "The model shows that cognitive biases are 'features' of neural processing rather than 'flaws.' Which evidence from the model best supports this claim?",
            "choices": {
                "A": "Biases only appear in people with brain injuries, suggesting they are abnormal",
                "B": "Heuristic shortcuts produce correct decisions approximately 95% of the time, failing only in specific predictable situations involving ambiguous input or high cognitive load",
                "C": "Biases are randomly distributed and unpredictable, suggesting they serve no function",
                "D": "Biases disappear entirely when a person is aware of them"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that heuristics evolved because they produce fast, accurate-enough decisions the vast majority of the time. They only fail systematically in specific conditions (ambiguous input, high load, strong priors), indicating they are adaptive features optimized for speed over perfect accuracy.",
            "feedback_incorrect": "Incorrect. The model shows biases are features because the underlying heuristics produce good decisions most of the time. Evolution optimized the brain for speed, not perfect accuracy, so these shortcuts work well in typical conditions but fail predictably when evidence is ambiguous or cognitive load is high."
        }
    ]
}

# =============================================================================
# L02 — The Science of Sleep: Why Teens Can't Wake Up (HS-LS1-3)
# =============================================================================
L02_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A 16-year-old naturally falls asleep at 11:30 PM and wakes at 8:30 AM on weekends, but must wake at 6:30 AM on school days. What biological factor most likely explains this pattern?",
            "choices": {
                "A": "Teenagers are lazier than adults and choose to sleep later",
                "B": "The adolescent circadian clock shifts approximately 2 hours later during puberty, delaying natural sleep onset",
                "C": "Teenagers have a different type of sleep that requires more hours",
                "D": "Weekend sleep patterns are abnormal and school-day patterns represent the body's true rhythm"
            },
            "correct": "B",
            "feedback_correct": "Correct. During puberty, the suprachiasmatic nucleus shifts the circadian clock approximately 2 hours later, causing melatonin to rise around 11 PM instead of 9 PM. This is a biological change, not a behavioral choice.",
            "feedback_incorrect": "Incorrect. Adolescent circadian rhythms shift 1-2 hours later during puberty due to changes in the suprachiasmatic nucleus. Melatonin onset occurs later, making early wake times fight fundamental biology."
        },
        {
            "question": "What role does melatonin play in the sleep-wake cycle?",
            "choices": {
                "A": "It provides energy to the brain during sleep so memories can be consolidated",
                "B": "It is a hormone released in response to darkness that signals the body to prepare for sleep",
                "C": "It is a neurotransmitter that keeps the brain active during REM sleep",
                "D": "It is produced by the eyes to protect them from damage during sleep"
            },
            "correct": "B",
            "feedback_correct": "Correct. Melatonin is produced by the pineal gland in response to darkness, signaling the body to prepare for sleep. Production begins about 2 hours before natural sleep onset and is suppressed by blue light.",
            "feedback_incorrect": "Incorrect. Melatonin is a hormone produced by the pineal gland when darkness is detected. It signals the body to prepare for sleep and is suppressed by blue light exposure from screens."
        },
        {
            "question": "A student uses their phone in bed for 2 hours before trying to sleep. Which physiological effect is most likely to occur?",
            "choices": {
                "A": "The phone's warmth increases body temperature, making sleep impossible",
                "B": "Blue light from the screen suppresses melatonin production, delaying sleep onset by 30-90 minutes",
                "C": "The phone emits sound waves that interfere with brain wave patterns",
                "D": "Phone use has no measurable effect on sleep biology"
            },
            "correct": "B",
            "feedback_correct": "Correct. Blue-wavelength light from screens directly suppresses melatonin production in the pineal gland, delaying sleep onset by 30-90 minutes even when the person feels tired.",
            "feedback_incorrect": "Incorrect. Blue light from screens suppresses the pineal gland's melatonin production, the hormone that signals the body to prepare for sleep. This delays sleep onset by 30-90 minutes."
        },
        {
            "question": "Sleep pressure refers to which biological phenomenon?",
            "choices": {
                "A": "The social pressure teenagers feel to stay up late with friends",
                "B": "The physical compression of brain tissue during sleep",
                "C": "The accumulating drive to sleep caused by the buildup of adenosine in the brain during waking hours",
                "D": "The pressure from parents and schools to maintain regular sleep schedules"
            },
            "correct": "C",
            "feedback_correct": "Correct. Sleep pressure results from adenosine accumulation during waking hours. The longer you are awake, the stronger the drive to sleep. Caffeine works by temporarily blocking adenosine receptors.",
            "feedback_incorrect": "Incorrect. Sleep pressure is a biological drive caused by adenosine buildup in the brain during waking hours. It increases the longer you stay awake and is cleared during sleep, especially deep sleep."
        },
        {
            "question": "Why might getting 6 hours of sleep from 2 AM to 8 AM produce different cognitive outcomes than 6 hours from 10 PM to 4 AM, even though total hours are identical?",
            "choices": {
                "A": "Sleep quality is identical regardless of timing; only total hours matter",
                "B": "The brain only needs sleep between midnight and 6 AM",
                "C": "Cognitive performance depends on alignment between sleep timing and the circadian rhythm, not just total sleep hours",
                "D": "Earlier sleep is always better because the body produces more growth hormone before midnight"
            },
            "correct": "C",
            "feedback_correct": "Correct. Sleep architecture and restorative quality depend on alignment with the circadian rhythm. The same total hours produce different outcomes depending on when they occur relative to the body's biological clock.",
            "feedback_incorrect": "Incorrect. It is not just total hours but WHEN those hours occur that matters. Sleep timing must align with the circadian rhythm for optimal cognitive performance and restorative sleep architecture."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "Based on the sleep model, what cascade of effects does the model predict when a teenager experiences 5 consecutive school nights with a 6:30 AM wake time and an 11 PM circadian sleep onset?",
            "choices": {
                "A": "The circadian clock will quickly adjust to the earlier schedule within 2-3 days",
                "B": "Sleep debt accumulates each night, progressively impairing cognitive performance, with weekend recovery only partially restoring function",
                "C": "Sleep pressure will decrease each night as the body adapts to less sleep",
                "D": "Melatonin production will shift earlier to compensate for the alarm time"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that sleep debt is cumulative. Each night of insufficient sleep compounds cognitive impairment, and weekend catch-up sleep only partially restores function because circadian misalignment cannot be fully corrected by sleeping in.",
            "feedback_incorrect": "Incorrect. The model predicts that sleep debt accumulates over the school week because the adolescent circadian clock cannot simply adjust to early wake times. Each night of lost sleep compounds cognitive impairment, and weekend recovery is only partial."
        },
        {
            "question": "The model includes five components: Light Exposure, Circadian Phase, Melatonin Level, Sleep Pressure, and Cognitive Performance. If a student eliminates screen use after 8 PM, which component is FIRST directly affected, and what is the downstream cascade?",
            "choices": {
                "A": "Sleep Pressure decreases first, then Cognitive Performance improves",
                "B": "Light Exposure decreases, allowing Melatonin Level to rise on schedule, improving sleep onset timing and Cognitive Performance",
                "C": "Circadian Phase shifts immediately, resolving all downstream effects",
                "D": "Cognitive Performance improves first, which then reduces the need for sleep"
            },
            "correct": "B",
            "feedback_correct": "Correct. Reducing evening light exposure is the first direct change, which allows melatonin production to begin on its natural schedule, improving sleep onset timing and downstream cognitive performance.",
            "feedback_incorrect": "Incorrect. The model shows that Light Exposure is the input variable most directly changed. Reducing blue light allows Melatonin Level to rise on schedule, which improves sleep onset timing and the downstream cascade to Cognitive Performance."
        },
        {
            "question": "The American Academy of Pediatrics recommends high school start times no earlier than 8:30 AM. Based on the sleep model, which evidence most strongly supports this recommendation?",
            "choices": {
                "A": "Students prefer sleeping later because they stay up playing video games",
                "B": "The adolescent circadian phase shift delays melatonin onset to approximately 11 PM, and 8:30 AM start times allow sufficient sleep aligned with the biological clock to maintain cognitive performance",
                "C": "Earlier start times only affect students who do not drink coffee in the morning",
                "D": "The recommendation is based on teacher preferences, not student biology"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model provides biological evidence: adolescent melatonin onset occurs around 11 PM, natural wake time is 8-9 AM, and cognitive performance depends on sleep timing alignment with the circadian rhythm. A 8:30 AM start accommodates this biology.",
            "feedback_incorrect": "Incorrect. The recommendation is grounded in circadian biology. The adolescent circadian shift delays melatonin onset to ~11 PM, making the natural wake time 8-9 AM. Starting school at 8:30 AM allows sleep timing to align with the biological clock."
        },
        {
            "question": "A student adds Caffeine Level as a new component to the model. Based on caffeine's mechanism of action, how would this component interact with Sleep Pressure?",
            "choices": {
                "A": "Caffeine eliminates Sleep Pressure by breaking down adenosine in the brain",
                "B": "Caffeine blocks adenosine receptors, masking Sleep Pressure without actually reducing it, with a half-life of 5-6 hours",
                "C": "Caffeine increases melatonin production, which indirectly reduces Sleep Pressure",
                "D": "Caffeine has no interaction with Sleep Pressure because they operate in different brain regions"
            },
            "correct": "B",
            "feedback_correct": "Correct. Caffeine blocks adenosine receptors, which masks the sensation of sleep pressure without clearing the accumulated adenosine. When caffeine wears off (half-life 5-6 hours), the masked sleep pressure hits at full force.",
            "feedback_incorrect": "Incorrect. Caffeine does not reduce Sleep Pressure. It blocks adenosine receptors, hiding the sleep signal. The adenosine continues accumulating, and when caffeine's effects wear off (half-life 5-6 hours), the full sleep pressure returns."
        },
        {
            "question": "Schools that shifted to later start times reported improved grades, attendance, and mental health. Which component interaction in the sleep model best explains ALL three improvements simultaneously?",
            "choices": {
                "A": "Later start times reduce homework load, which reduces stress",
                "B": "Aligning wake times with the circadian phase allows adequate sleep, which improves Cognitive Performance, a variable that affects learning (grades), alertness (attendance), and emotional regulation (mental health)",
                "C": "Later start times mean students skip breakfast less often, improving nutrition",
                "D": "Students are simply happier about sleeping later, which creates a placebo effect"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that Cognitive Performance is downstream of circadian-aligned sleep. When sleep timing matches the biological clock, cognitive function improves across multiple domains: memory consolidation (grades), alertness (attendance), and emotional regulation (mental health).",
            "feedback_incorrect": "Incorrect. The model predicts that aligning sleep with the circadian rhythm improves the umbrella variable of Cognitive Performance, which encompasses memory consolidation (grades), daytime alertness (attendance), and emotional regulation (mental health)."
        }
    ]
}

# =============================================================================
# L03 — Is Your Tap Water Safe? (HS-PS1-2, HS-ESS3-4)
# =============================================================================
L03_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "The EPA action level for lead in drinking water is 15 parts per billion (ppb). What does this measurement represent?",
            "choices": {
                "A": "The temperature at which lead dissolves in water",
                "B": "A concentration of contamination so small that specialized instruments are needed to detect it",
                "C": "The percentage of water molecules that contain lead atoms",
                "D": "The number of lead pipes in a city's water distribution system"
            },
            "correct": "B",
            "feedback_correct": "Correct. Parts per billion is an extremely small concentration measurement. At 15 ppb, there are only 15 lead molecules for every billion water molecules, yet even this tiny amount can cause harm, especially to children.",
            "feedback_incorrect": "Incorrect. Parts per billion (ppb) measures contamination concentration. At 15 ppb, there are 15 units of lead per billion units of water. No level of lead is considered safe for children."
        },
        {
            "question": "What is the primary function of corrosion control in municipal water treatment?",
            "choices": {
                "A": "To remove bacteria and viruses from the water supply",
                "B": "To add fluoride to water for dental health",
                "C": "To create a protective coating inside water pipes that prevents lead and copper from leaching into drinking water",
                "D": "To adjust the color and taste of water to make it more appealing"
            },
            "correct": "C",
            "feedback_correct": "Correct. Corrosion control chemicals create a protective mineral coating inside pipes that prevents metals from dissolving into the water. The failure of this treatment triggered the Flint, Michigan water crisis.",
            "feedback_incorrect": "Incorrect. Corrosion control adds chemicals that form a protective coating on the inner surfaces of pipes, preventing lead and copper from leaching into drinking water. Its failure was central to the Flint crisis."
        },
        {
            "question": "In the Flint, Michigan water crisis, what was the initial cause that triggered the contamination cascade?",
            "choices": {
                "A": "A natural disaster destroyed the water treatment plant",
                "B": "The city switched to a new water source with different chemistry and failed to adjust corrosion control treatment",
                "C": "Residents deliberately contaminated their own water supply",
                "D": "The EPA raised the acceptable lead limit, making previously safe water unsafe"
            },
            "correct": "B",
            "feedback_correct": "Correct. Flint switched from Detroit's treated Lake Huron water to the Flint River to save money. The new water had different chemistry (higher chloride) that corroded the protective coating in lead pipes, releasing lead into the drinking water.",
            "feedback_incorrect": "Incorrect. The crisis began when Flint switched water sources to save money. The new source water had different chemistry that was more corrosive, and without adjusting corrosion control treatment, the protective coatings in lead pipes dissolved."
        },
        {
            "question": "Why is tap water safety described as a 'system property' rather than determined by any single factor?",
            "choices": {
                "A": "Because water safety is subjective and depends on individual taste preferences",
                "B": "Because tap water quality depends on the interconnected functioning of source protection, treatment, and distribution infrastructure",
                "C": "Because different government agencies each test for different contaminants",
                "D": "Because water safety varies by the time of day it is tested"
            },
            "correct": "B",
            "feedback_correct": "Correct. Tap water safety is an emergent property of an interconnected system. Even if the treatment plant produces perfectly clean water, aging pipes in the distribution system can introduce contaminants before it reaches your tap.",
            "feedback_incorrect": "Incorrect. Water safety emerges from the interaction of source water quality, treatment effectiveness, and distribution infrastructure integrity. A failure in any component can compromise the entire system."
        },
        {
            "question": "The EPA estimates that 6-10 million American homes receive water through lead service lines. Why does this represent an ongoing public health concern?",
            "choices": {
                "A": "Lead pipes are structurally weaker and prone to bursting during cold weather",
                "B": "Lead pipes can leach lead into drinking water, especially when protective coatings fail or water chemistry changes",
                "C": "Lead pipes reduce water flow, causing water shortages in those homes",
                "D": "Lead pipes are only found in commercial buildings, not residential homes"
            },
            "correct": "B",
            "feedback_correct": "Correct. Lead service lines are a latent hazard. While corrosion control can keep lead levels low, any change in water chemistry, treatment failure, or coating deterioration can cause lead to leach into drinking water at dangerous levels.",
            "feedback_incorrect": "Incorrect. Lead pipes remain a public health concern because they can release lead into drinking water whenever protective coatings break down due to water chemistry changes, treatment failures, or aging infrastructure."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the water safety model, a city has excellent Source Water Quality and high Treatment Effectiveness, but its Pipe Infrastructure is 80+ years old with lead service lines. What does the model predict about Tap Water Safety?",
            "choices": {
                "A": "Tap Water Safety will be high because good source and treatment compensate for old pipes",
                "B": "Tap Water Safety is compromised because aging infrastructure can introduce contaminants after water leaves the treatment plant, regardless of upstream quality",
                "C": "Tap Water Safety depends only on Treatment Effectiveness, so pipe age is irrelevant",
                "D": "Tap Water Safety will be low only if the water temperature exceeds 70 degrees"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that aging infrastructure is a ticking time bomb. Even with excellent source water and treatment, deteriorating lead pipes can leach contaminants into water after it leaves the plant, making Tap Water Safety a system property.",
            "feedback_incorrect": "Incorrect. The model predicts that pipe infrastructure age independently threatens Tap Water Safety. Water that is perfectly clean leaving the treatment plant can become contaminated as it travels through aging lead pipes."
        },
        {
            "question": "Using the model, which sequence correctly describes the Flint water crisis as a cascading system failure?",
            "choices": {
                "A": "Pipe Infrastructure failed first, then Treatment Effectiveness dropped, then Source Water Quality declined",
                "B": "Source Water Quality changed (more corrosive chemistry) -> Treatment Effectiveness was not adjusted (no corrosion control) -> Corrosion Rate spiked -> Tap Water Safety collapsed",
                "C": "Testing Frequency was reduced first, causing all other components to fail simultaneously",
                "D": "Tap Water Safety declined first, which caused Source Water Quality to deteriorate"
            },
            "correct": "B",
            "feedback_correct": "Correct. The Flint crisis was a cascading failure: the new water source had different chemistry, treatment was not adjusted for the new chemistry, corrosion rates spiked in unprotected lead pipes, and lead leached into drinking water.",
            "feedback_incorrect": "Incorrect. The model shows the cascade: Source Water Quality changed when Flint switched rivers, Treatment Effectiveness was not recalibrated, Corrosion Rate increased dramatically in the aging lead pipes, and Tap Water Safety collapsed."
        },
        {
            "question": "A student extends the model by adding Community Socioeconomic Status as a component. Based on environmental justice research, how would this component most likely interact with the other variables?",
            "choices": {
                "A": "Socioeconomic status has no connection to water infrastructure quality",
                "B": "Lower-income communities tend to have older infrastructure, less political power to demand repairs, and fewer resources for alternatives, increasing vulnerability to contamination",
                "C": "Wealthier communities always have worse water because they use more water",
                "D": "Socioeconomic status only affects Source Water Quality, not distribution infrastructure"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model extension reveals that lower-income communities face compounding vulnerabilities: older pipes, less political influence for infrastructure investment, and fewer resources for bottled water when contamination occurs.",
            "feedback_incorrect": "Incorrect. Environmental justice research shows that socioeconomic status correlates with infrastructure age, political power to demand repairs, and access to alternatives, making lower-income communities disproportionately vulnerable to water contamination."
        },
        {
            "question": "Why is replacing lead pipes considered a more permanent solution than adjusting water chemistry, according to the water safety model?",
            "choices": {
                "A": "Replacing pipes is cheaper than maintaining corrosion control chemicals",
                "B": "Chemical treatment eliminates the source of contamination, while pipe replacement only addresses symptoms",
                "C": "Removing lead pipes eliminates the contamination source entirely, while chemical treatment must be continuously maintained and can fail if water chemistry changes again",
                "D": "New pipes never corrode, making them maintenance-free forever"
            },
            "correct": "C",
            "feedback_correct": "Correct. The model shows that corrosion control is a continuous treatment that can fail if conditions change, while removing lead pipes permanently eliminates the source of lead contamination from the system.",
            "feedback_incorrect": "Incorrect. The model demonstrates that chemical corrosion control requires continuous maintenance and is vulnerable to changes in water chemistry. Replacing lead pipes permanently removes the contamination source, making the system inherently safer."
        },
        {
            "question": "Based on the systems model of water safety, which intervention strategy would be MOST effective at preventing a crisis similar to Flint?",
            "choices": {
                "A": "Testing water quality only at the treatment plant exit",
                "B": "Replacing all lead pipes with modern materials and increasing testing frequency at multiple points throughout the distribution system",
                "C": "Only increasing the amount of disinfectant added during treatment",
                "D": "Relying solely on residents to report discolored water"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that addressing both infrastructure (replacing lead pipes) and monitoring (testing at multiple distribution points) creates redundant protections that can detect problems before they reach crisis levels.",
            "feedback_incorrect": "Incorrect. The systems model shows that effective prevention requires addressing multiple components: replacing the source of contamination (lead pipes) AND monitoring water quality throughout the distribution system, not just at the plant exit."
        }
    ]
}

# =============================================================================
# L04 — The Ultra-Processed Food Problem (HS-LS1-7)
# =============================================================================
L04_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "In a landmark NIH clinical trial, participants eating ultra-processed meals consumed 500 more calories per day than those eating unprocessed meals, despite both groups having unlimited food access. Which factor best explains this difference?",
            "choices": {
                "A": "Ultra-processed foods contain more total calories per gram than whole foods",
                "B": "Ultra-processed foods bypass normal satiety signaling, causing people to eat faster and consume more before feeling full",
                "C": "Participants eating whole foods were more motivated to lose weight",
                "D": "Ultra-processed foods are more nutritious, so the body craves less of them"
            },
            "correct": "B",
            "feedback_correct": "Correct. Ultra-processed foods are consumed 20-30% faster and produce weaker fullness signals than whole foods. The body cannot regulate intake effectively when satiety mechanisms are disrupted by food engineering.",
            "feedback_incorrect": "Incorrect. The key mechanism is disrupted satiety signaling. Ultra-processed foods are eaten faster and produce weaker fullness signals, so people consume significantly more calories before feeling satisfied."
        },
        {
            "question": "What distinguishes an ultra-processed food from a processed food?",
            "choices": {
                "A": "Ultra-processed foods have fewer ingredients than processed foods",
                "B": "Ultra-processed foods are industrially manufactured products containing ingredients not found in home kitchens, such as emulsifiers, flavor enhancers, and hydrogenated oils",
                "C": "Any food that has been cooked is considered ultra-processed",
                "D": "Ultra-processed foods are always more expensive than whole foods"
            },
            "correct": "B",
            "feedback_correct": "Correct. Ultra-processed foods are defined by the NOVA classification as industrial formulations made mostly from substances derived from foods, with additives not found in home kitchens, designed for hyper-palatability, shelf life, and profit.",
            "feedback_incorrect": "Incorrect. Ultra-processed foods contain industrial ingredients like emulsifiers, flavor enhancers, and hydrogenated oils that are not used in home cooking. They are engineered for maximum palatability, not nutrition."
        },
        {
            "question": "What is metabolic syndrome?",
            "choices": {
                "A": "A single disease caused by eating too much sugar",
                "B": "A cluster of conditions including high blood sugar, excess abdominal fat, high blood pressure, and abnormal cholesterol that together increase heart disease and diabetes risk",
                "C": "A genetic disorder that prevents the body from digesting food",
                "D": "A temporary condition that resolves when a person exercises more"
            },
            "correct": "B",
            "feedback_correct": "Correct. Metabolic syndrome is a cluster of interconnected conditions that dramatically increase the risk of heart disease, stroke, and type 2 diabetes. Ultra-processed diets are strongly associated with its development.",
            "feedback_incorrect": "Incorrect. Metabolic syndrome is not a single disease but a cluster of co-occurring conditions (high blood sugar, abdominal fat, high blood pressure, abnormal cholesterol) that together multiply the risk of cardiovascular disease and diabetes."
        },
        {
            "question": "Why is blaming obesity on 'lack of willpower' scientifically inaccurate based on food science research?",
            "choices": {
                "A": "Because obesity is entirely genetic and food choice plays no role",
                "B": "Because ultra-processed foods are engineered to override biological satiety signals, making overconsumption a physiological response rather than a character flaw",
                "C": "Because all people have exactly the same willpower regardless of circumstances",
                "D": "Because only extremely rare medical conditions cause obesity"
            },
            "correct": "B",
            "feedback_correct": "Correct. Ultra-processed foods disrupt the hormonal signals (leptin, ghrelin) that regulate hunger and fullness. The overconsumption is driven by food engineering that bypasses biological controls, not by individual willpower failure.",
            "feedback_incorrect": "Incorrect. Research shows that ultra-processed foods override the body's natural satiety signaling systems. People overconsume because the food is engineered to bypass fullness signals, not because they lack self-control."
        },
        {
            "question": "How does the gut microbiome relate to ultra-processed food consumption?",
            "choices": {
                "A": "Ultra-processed foods increase gut microbiome diversity, which improves health",
                "B": "The gut microbiome is not affected by diet in any measurable way",
                "C": "Ultra-processed food consumption significantly decreases gut microbiome diversity, which correlates with metabolic dysfunction and impaired immune function",
                "D": "The gut microbiome only affects digestion and has no connection to overall health"
            },
            "correct": "C",
            "feedback_correct": "Correct. Research shows that ultra-processed diets dramatically reduce the diversity of gut bacteria, which correlates with metabolic problems, weakened immune function, and even mood disturbances.",
            "feedback_incorrect": "Incorrect. Ultra-processed foods decrease gut microbiome diversity. The gut microbiome influences metabolism, immune function, and even mood, so reduced diversity from ultra-processed diets has far-reaching health consequences."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The food model shows that Processing Level predicts health outcomes better than individual nutrient content. Two meals have identical calories, protein, fat, carbohydrates, and fiber. One is ultra-processed, one is whole food. Which model mechanism explains why health outcomes differ?",
            "choices": {
                "A": "The whole food meal has more vitamins, which is the only relevant nutritional difference",
                "B": "The ultra-processed meal disrupts satiety signaling and is consumed faster, leading to weaker fullness responses and greater caloric overconsumption despite identical nutrient profiles",
                "C": "The meals would produce identical health outcomes since the macronutrient profiles match",
                "D": "The whole food meal causes faster digestion, which alone accounts for the difference"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that processing level affects the food matrix itself, not just nutrient content. Ultra-processed foods are consumed 20-30% faster and produce weaker satiety responses, causing overconsumption regardless of macronutrient matching.",
            "feedback_incorrect": "Incorrect. The model reveals that it is the processing that matters, not just the nutrients. Ultra-processed foods are eaten faster and disrupt satiety signaling, causing the body to overconsume even when the nutritional profile appears identical."
        },
        {
            "question": "According to the model, when a person shifts from an 80% ultra-processed diet to 50% whole foods, what pattern of Metabolic Health recovery does the model predict?",
            "choices": {
                "A": "No improvement until the diet is 100% whole foods",
                "B": "Measurable improvements in blood sugar, inflammation, and gut microbiome diversity within 2-4 weeks, with continued improvement over time",
                "C": "Immediate full recovery of all metabolic markers within 48 hours",
                "D": "Metabolic damage from ultra-processed foods is permanent and irreversible"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that metabolic damage is partially reversible. Shifting to more whole foods shows measurable improvements in blood sugar, inflammation markers, and gut microbiome diversity within 2-4 weeks.",
            "feedback_incorrect": "Incorrect. The model demonstrates that metabolic damage from ultra-processed diets is partially reversible. Measurable improvements appear within 2-4 weeks of dietary change, with continued improvement over longer periods."
        },
        {
            "question": "The model includes Satiety Response as a component. What causal mechanism links ultra-processing to weakened satiety?",
            "choices": {
                "A": "Ultra-processed foods contain fewer calories, so the body signals for more food",
                "B": "Ultra-processed foods are consumed 20-30% faster than whole foods, not allowing time for gut hormones to signal fullness to the brain before excess calories are consumed",
                "C": "Ultra-processed foods strengthen satiety signals, which causes people to eat less",
                "D": "Satiety is entirely determined by stomach volume, not food processing level"
            },
            "correct": "B",
            "feedback_correct": "Correct. The eating speed mechanism is critical. Ultra-processed foods are consumed faster because of their texture and palatability engineering. The gut hormones that signal fullness need 15-20 minutes to activate, but the food is already consumed.",
            "feedback_incorrect": "Incorrect. Ultra-processed foods are eaten 20-30% faster due to engineered texture and palatability. The gut hormones (leptin, GLP-1) that signal fullness need time to reach the brain, but the rapid consumption means excess calories are consumed before the signal arrives."
        },
        {
            "question": "A student adds Food Marketing Exposure as a component to the model. Children and teens see an average of 13 food ads per day, overwhelmingly for ultra-processed products. How does this component interact with Caloric Overconsumption?",
            "choices": {
                "A": "Marketing has no measurable effect on food choices or consumption patterns",
                "B": "Marketing only affects adults, not children or teenagers",
                "C": "Marketing exposure increases preference for and consumption of ultra-processed foods, amplifying the satiety disruption pathway and increasing Caloric Overconsumption",
                "D": "Marketing decreases consumption by making people more aware of what they are eating"
            },
            "correct": "C",
            "feedback_correct": "Correct. Food marketing increases both preference for and availability-seeking of ultra-processed products, driving more frequent consumption of foods that disrupt satiety signaling and amplifying the overconsumption pathway in the model.",
            "feedback_incorrect": "Incorrect. Research shows that food marketing exposure increases preference for ultra-processed foods, leading to more frequent consumption of products that disrupt satiety signaling, which amplifies the Caloric Overconsumption pathway."
        },
        {
            "question": "Based on the model, which intervention would be MOST effective at reducing population-level metabolic disease from ultra-processed food consumption?",
            "choices": {
                "A": "Teaching individuals to count calories more carefully",
                "B": "Reducing the Processing Level of available food through policy changes that make whole foods more affordable and accessible while regulating ultra-processing practices",
                "C": "Recommending that people exercise more to burn off extra calories from ultra-processed foods",
                "D": "Removing all fat content from ultra-processed foods"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that Processing Level is the root driver of metabolic dysfunction. Addressing the upstream cause (reducing processing) through food policy is more effective than downstream interventions like calorie counting or exercise.",
            "feedback_incorrect": "Incorrect. The model identifies Processing Level as the upstream driver. Individual-level interventions like calorie counting address symptoms, not causes. Systemic changes to food availability, affordability, and processing practices address the root mechanism."
        }
    ]
}

# =============================================================================
# L05 — Why Some People Get Addicted and Others Don't (HS-LS1-2, HS-LS3-1)
# =============================================================================
L05_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Research shows that genetic factors account for 40-60% of addiction vulnerability. What does this statistic mean in practical terms?",
            "choices": {
                "A": "People with addiction genes will always become addicted regardless of circumstances",
                "B": "Inherited variations in brain chemistry create significantly different baseline vulnerabilities, but genes are not destiny",
                "C": "Genetics play no meaningful role in addiction because environment is all that matters",
                "D": "Exactly 50% of all people will become addicted to any substance they try"
            },
            "correct": "B",
            "feedback_correct": "Correct. Genetic predisposition means inherited variations in dopamine receptors, metabolism enzymes, and stress response create different vulnerability levels. Genes load the dice but do not determine the outcome.",
            "feedback_incorrect": "Incorrect. The 40-60% figure means genetics significantly influence risk through variations in brain chemistry, but they do not determine outcomes. Environmental factors, age of exposure, and stress also play critical roles."
        },
        {
            "question": "What role does dopamine play in the brain's reward system and how do addictive substances exploit it?",
            "choices": {
                "A": "Dopamine is a pain-blocking chemical; drugs work by eliminating pain signals",
                "B": "Dopamine signals reward and motivation; addictive substances flood the system with 2-10 times more dopamine than natural rewards, rewiring motivation circuits",
                "C": "Dopamine is only released during sleep; drugs interfere with sleep patterns",
                "D": "Dopamine destroys brain cells, which is why drugs are harmful"
            },
            "correct": "B",
            "feedback_correct": "Correct. Dopamine signals reward and motivation through the mesolimbic pathway. Addictive substances produce dopamine surges far beyond natural rewards, gradually rewiring the brain to prioritize the substance above all else.",
            "feedback_incorrect": "Incorrect. Dopamine is a neurotransmitter that signals reward and motivation. Natural rewards produce 150-200% baseline dopamine, while drugs produce 200-1000%, overwhelming the system and physically rewiring motivation circuits."
        },
        {
            "question": "Why does the age of first substance exposure significantly affect addiction risk?",
            "choices": {
                "A": "Younger people have stronger immune systems that metabolize drugs faster",
                "B": "The prefrontal cortex, responsible for impulse control, is not fully developed until age 25, making adolescent brains more vulnerable to reward circuit hijacking",
                "C": "Younger people are more likely to use substances in social settings, which is the only risk factor",
                "D": "Age of exposure has no significant effect on addiction outcomes"
            },
            "correct": "B",
            "feedback_correct": "Correct. The prefrontal cortex (impulse control, long-term planning) is still developing during adolescence. Substance exposure during this critical period can permanently alter reward circuitry development.",
            "feedback_incorrect": "Incorrect. Adolescent brains are more vulnerable because the prefrontal cortex, which provides impulse control and long-term planning, is not fully mature until age 25. Substance exposure during brain development creates higher addiction risk."
        },
        {
            "question": "What is tolerance in the context of addiction neuroscience?",
            "choices": {
                "A": "The social acceptance of drug use in a community",
                "B": "The brain's adaptation to repeated substance exposure by reducing dopamine receptor density, requiring increasing doses for the same effect",
                "C": "The body's ability to completely eliminate a drug from the bloodstream",
                "D": "A personality trait that determines whether someone will try drugs"
            },
            "correct": "B",
            "feedback_correct": "Correct. Tolerance occurs when the brain reduces dopamine receptor density in response to repeated substance-induced flooding. This means higher doses are needed for the same effect, and natural rewards become less satisfying.",
            "feedback_incorrect": "Incorrect. Tolerance is a neurobiological adaptation where the brain reduces dopamine receptor density to cope with repeated substance-induced flooding. This requires escalating doses and is a hallmark of addiction progression."
        },
        {
            "question": "Which statement best reflects the current scientific understanding of addiction?",
            "choices": {
                "A": "Addiction is purely a moral failure that can be overcome through willpower alone",
                "B": "Addiction is a chronic brain disease involving hijacked reward circuitry that overrides rational decision-making",
                "C": "Addiction only affects people who choose to use drugs recreationally",
                "D": "Addiction is completely determined by genetics with no environmental component"
            },
            "correct": "B",
            "feedback_correct": "Correct. Modern neuroscience classifies addiction as a chronic brain disease. Substances physically rewire the brain's reward and motivation circuits, creating compulsions that override the prefrontal cortex's decision-making abilities.",
            "feedback_incorrect": "Incorrect. Neuroscience has established that addiction is a brain disease, not a moral failing. Addictive substances physically alter the brain's reward circuitry, creating compulsions that override rational decision-making capacity."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the addiction model, Individual A has high Genetic Vulnerability and first Substance Exposure at age 14. Individual B has low Genetic Vulnerability and first exposure at age 25. What does the model predict about their relative Addiction Severity trajectories?",
            "choices": {
                "A": "Both individuals will have identical trajectories because the substance is the same",
                "B": "Individual A will show amplified Dopamine Surge, faster Receptor Downregulation, and higher Addiction Severity because high genetic vulnerability combined with adolescent brain development creates compounding risk",
                "C": "Individual B will develop greater Addiction Severity because adult brains are more susceptible to addiction",
                "D": "Neither individual will develop addiction because genetics alone do not determine outcomes"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model predicts compounding risk for Individual A: high genetic vulnerability means stronger initial dopamine response, and adolescent brain exposure means the still-developing prefrontal cortex cannot effectively moderate compulsive behavior.",
            "feedback_incorrect": "Incorrect. The model shows that Individual A faces compounding risk. High genetic vulnerability amplifies the dopamine surge, and adolescent exposure occurs during a critical window when the prefrontal cortex cannot yet effectively override reward-seeking behavior."
        },
        {
            "question": "The model shows that chronic stress multiplies addiction vulnerability rather than simply adding to it. Which mechanism best explains this multiplicative interaction?",
            "choices": {
                "A": "Stress causes people to spend more time around drugs, increasing exposure probability",
                "B": "Chronic stress hormones sensitize the dopamine system (making it hyperresponsive to substances) while simultaneously impairing the prefrontal cortex's ability to override compulsions",
                "C": "Stress only affects addiction in people who already have high genetic vulnerability",
                "D": "Stress increases tolerance, which paradoxically protects against addiction"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows a dual mechanism: stress hormones sensitize the reward system (amplifying dopamine response to substances) AND impair prefrontal cortex function (weakening impulse control). These effects multiply, not add.",
            "feedback_incorrect": "Incorrect. Chronic stress is multiplicative because it simultaneously sensitizes the dopamine system to substances AND impairs the prefrontal cortex's ability to override compulsions. This dual mechanism compounds vulnerability beyond simple addition."
        },
        {
            "question": "Based on the model, why have fear-based prevention programs like 'Just Say No' consistently failed to reduce substance use initiation?",
            "choices": {
                "A": "They are too expensive to implement effectively",
                "B": "They target conscious choice (prefrontal cortex) but addiction operates through subcortical reward circuits that bypass rational decision-making, and fear can actually increase curiosity",
                "C": "They only work for adults, not teenagers",
                "D": "They are too successful, leading schools to become overconfident and reduce other prevention efforts"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that addiction hijacks subcortical reward circuits that operate below conscious decision-making. Fear-based programs address the wrong neural system and research shows they can paradoxically increase curiosity about substances.",
            "feedback_incorrect": "Incorrect. The model reveals that addiction operates through reward circuits that bypass rational decision-making. Programs that rely on fear and conscious choice-making target the wrong part of the brain. Research also shows fear can increase curiosity."
        },
        {
            "question": "A student adds Epigenetic Modification as a component to the model. How does epigenetics expand understanding of addiction beyond simple genetic inheritance?",
            "choices": {
                "A": "Epigenetics replaces genetics entirely as the cause of addiction",
                "B": "Epigenetic changes from stress or substance exposure can activate or silence addiction-related genes without altering DNA sequence, potentially affecting future generations",
                "C": "Epigenetics only affects hair color and eye color, not brain function",
                "D": "Epigenetic modifications are identical to mutations and are always harmful"
            },
            "correct": "B",
            "feedback_correct": "Correct. Epigenetic modifications change gene expression without altering DNA sequence. Environmental factors like chronic stress or substance exposure can activate addiction-related genes, and some of these changes may be inherited across generations.",
            "feedback_incorrect": "Incorrect. Epigenetics adds a layer of complexity: environmental factors (stress, substance exposure) can change gene expression without altering DNA, potentially activating or silencing addiction-related genes across generations."
        },
        {
            "question": "The model predicts that understanding addiction as a brain disease should fundamentally change societal responses. Which policy change is most directly supported by the model's evidence?",
            "choices": {
                "A": "Increasing criminal penalties for substance use to deter people through fear",
                "B": "Replacing punitive approaches with evidence-based treatment that targets the neurobiological mechanisms of reward circuit hijacking and receptor downregulation",
                "C": "Eliminating all prevention programs since addiction is purely biological",
                "D": "Making all substances legal since prohibition does not address brain chemistry"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that addiction involves physical brain changes (receptor downregulation, reward circuit rewiring) that require medical/therapeutic intervention, not punishment. Treatment must target the biological mechanisms the model reveals.",
            "feedback_incorrect": "Incorrect. The model demonstrates that addiction involves physical brain changes that cannot be addressed through punishment. Evidence-based treatment targeting the neurobiological mechanisms (dopamine system, receptor downregulation) is the approach supported by the science."
        }
    ]
}

# =============================================================================
# L06 — Why Is Antibiotic Resistance Getting Worse? (HS-LS4-2)
# =============================================================================
L06_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A patient takes antibiotics for 5 of a prescribed 10-day course because they feel better. What is the most likely outcome for the surviving bacterial population?",
            "choices": {
                "A": "All bacteria are eliminated because the patient felt better, indicating the infection is cured",
                "B": "The weakest bacteria are killed but the most resistant ones survive and multiply without competition, increasing resistance gene frequency",
                "C": "The surviving bacteria become weaker because they were partially exposed to the antibiotic",
                "D": "The bacteria develop immunity to the antibiotic through a conscious adaptation process"
            },
            "correct": "B",
            "feedback_correct": "Correct. Stopping antibiotics early kills susceptible bacteria but leaves resistant mutants alive to reproduce without competition. This is natural selection in action, increasing resistance gene frequency in the surviving population.",
            "feedback_incorrect": "Incorrect. Incomplete courses create strong selective pressure: the weakest bacteria die first, leaving the most resistant ones to multiply without competition from susceptible bacteria, dramatically increasing resistance gene frequency."
        },
        {
            "question": "Antibiotic resistance is an example of which fundamental biological process?",
            "choices": {
                "A": "Cellular respiration in bacterial cells",
                "B": "Evolution by natural selection, where antibiotics create selective pressure that favors bacteria with resistance mutations",
                "C": "Photosynthesis that allows bacteria to produce their own energy",
                "D": "Bacteria deliberately learning to resist chemicals through memory"
            },
            "correct": "B",
            "feedback_correct": "Correct. Antibiotic resistance is natural selection in real time: random mutations provide variation, antibiotics create selective pressure, susceptible bacteria die, and resistant mutants survive and reproduce.",
            "feedback_incorrect": "Incorrect. Antibiotic resistance is evolution by natural selection. Bacteria do not 'learn' to resist. Random mutations provide genetic variation, antibiotics create selective pressure, and bacteria with resistance mutations survive and reproduce."
        },
        {
            "question": "What is horizontal gene transfer and why does it make antibiotic resistance particularly dangerous?",
            "choices": {
                "A": "It is the process by which bacteria reproduce, creating identical copies of themselves",
                "B": "It is the process by which bacteria share genetic material, including resistance genes, directly between cells, allowing resistance to spread between species",
                "C": "It is the process by which viruses transfer genes to bacteria during infection",
                "D": "It is a laboratory technique used to create genetically modified bacteria"
            },
            "correct": "B",
            "feedback_correct": "Correct. Horizontal gene transfer (conjugation, transformation, transduction) allows bacteria to share resistance genes directly between cells, even between different species. This means resistance that evolves in one species can transfer to deadly pathogens.",
            "feedback_incorrect": "Incorrect. Horizontal gene transfer allows bacteria to share genetic material, including resistance genes, between unrelated cells and species. This means resistance genes can jump from harmless environmental bacteria to dangerous pathogens."
        },
        {
            "question": "Why is sub-therapeutic antibiotic use in livestock considered one of the greatest threats to human health?",
            "choices": {
                "A": "Antibiotics make the meat taste different and cause allergic reactions in consumers",
                "B": "Constant low-level exposure creates ideal conditions for gradual resistance evolution in trillions of bacteria across massive populations",
                "C": "Livestock antibiotics are chemically different from human antibiotics and cannot affect human health",
                "D": "Agricultural antibiotic use has decreased over the past 50 years and is no longer a concern"
            },
            "correct": "B",
            "feedback_correct": "Correct. Sub-therapeutic doses in livestock expose trillions of bacteria to constant low-level selective pressure. This is the perfect evolutionary training ground for resistance, and resistant bacteria can transfer to humans through food, water, and the environment.",
            "feedback_incorrect": "Incorrect. Agricultural antibiotic use exposes massive bacterial populations to constant sub-therapeutic levels, creating an enormous evolutionary laboratory for resistance development that can then transfer to human pathogens."
        },
        {
            "question": "What defines a 'superbug' and why are these organisms an urgent medical concern?",
            "choices": {
                "A": "Any bacterium that causes infection in hospitalized patients",
                "B": "A bacterial strain that has evolved resistance to multiple classes of antibiotics, making infections extremely difficult or impossible to treat",
                "C": "A genetically modified bacterium created in laboratories for research purposes",
                "D": "A large bacterium that can be seen without a microscope"
            },
            "correct": "B",
            "feedback_correct": "Correct. Superbugs like MRSA, CRE, and XDR-TB have evolved resistance to multiple antibiotic classes. When no antibiotics work, infections that were once easily treatable become life-threatening.",
            "feedback_incorrect": "Incorrect. Superbugs are bacterial strains resistant to multiple antibiotic classes. Examples include MRSA, CRE, and XDR-TB. They represent the endpoint of resistance evolution where our medicines are no longer effective."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the resistance model, a patient completes the full 10-day antibiotic course at the correct dose. What does the model predict about Resistance Gene Frequency compared to an incomplete course?",
            "choices": {
                "A": "Resistance Gene Frequency will be identical regardless of course completion",
                "B": "Full course completion eliminates nearly all bacteria before resistant mutants can establish, keeping Resistance Gene Frequency low, while incomplete courses allow resistant survivors to multiply",
                "C": "Full course completion increases Resistance Gene Frequency because longer exposure means more mutations",
                "D": "Course duration does not affect bacterial population dynamics"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that completing the full course eliminates bacteria before resistant variants can establish a population. Stopping early removes the competition for resistant bacteria, allowing them to multiply and dominate.",
            "feedback_incorrect": "Incorrect. The model predicts that full treatment eliminates the vast majority of bacteria, including most with partial resistance, before they can multiply. Incomplete courses leave the most resistant bacteria alive with no competition."
        },
        {
            "question": "The model includes Mutation Rate as a component. Bacteria reproduce every 20-30 minutes, generating millions of mutations daily. Why does this reproductive speed make resistance evolution practically inevitable?",
            "choices": {
                "A": "Fast reproduction means each individual bacterium becomes resistant more quickly",
                "B": "Rapid reproduction generates enormous genetic variation in very short time frames, making it statistically likely that pre-existing resistance mutations will be present before antibiotic exposure even begins",
                "C": "Reproduction speed has no relationship to the probability of beneficial mutations",
                "D": "Bacteria only mutate when exposed to antibiotics, so reproduction speed is irrelevant"
            },
            "correct": "B",
            "feedback_correct": "Correct. With reproduction every 20-30 minutes, a single bacterium can produce billions of offspring in hours. With random mutations occurring at each division, the probability of pre-existing resistance mutations in any large population approaches certainty.",
            "feedback_incorrect": "Incorrect. Rapid reproduction creates massive genetic variation. Mutations are random and occur during every replication. With millions of divisions per day, the probability of resistance mutations existing BEFORE antibiotic exposure is very high in large populations."
        },
        {
            "question": "Based on the model, which of the three main misuse behaviors (incomplete courses, prescribing for viral infections, agricultural overuse) drives resistance evolution FASTEST, and why?",
            "choices": {
                "A": "Prescribing for viral infections, because viruses and bacteria share resistance genes",
                "B": "Agricultural overuse, because it exposes trillions of bacteria to constant sub-therapeutic selective pressure across massive populations, maximizing the probability and speed of resistance evolution",
                "C": "Incomplete courses, because they are the only behavior that actually affects bacteria",
                "D": "All three behaviors have exactly identical effects on resistance evolution rates"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model predicts that agricultural overuse is the most dangerous because it combines the largest bacterial population sizes with constant sub-therapeutic selective pressure across continuous time periods, creating optimal conditions for resistance evolution.",
            "feedback_incorrect": "Incorrect. The model shows agricultural overuse is most dangerous because it exposes the largest bacterial populations to continuous selective pressure at sub-therapeutic levels, providing ideal conditions for gradual resistance evolution on a massive scale."
        },
        {
            "question": "Horizontal gene transfer allows resistance genes to move between bacterial species. How does including this mechanism in the model change predictions about the spread of resistance?",
            "choices": {
                "A": "It has no effect because resistance genes can only be passed from parent to offspring",
                "B": "It transforms resistance from an individual-patient problem to a community-level threat, because resistance evolving in harmless environmental bacteria can transfer to deadly human pathogens",
                "C": "It slows resistance spread because gene transfer between species is always unsuccessful",
                "D": "It only matters in laboratory settings, not in natural environments"
            },
            "correct": "B",
            "feedback_correct": "Correct. Horizontal gene transfer means resistance is not contained within a single species. Genes can jump from harmless soil bacteria to dangerous pathogens, making resistance a population-level and community-level threat.",
            "feedback_incorrect": "Incorrect. Horizontal gene transfer means resistance genes can jump between species through conjugation, transformation, and transduction. This transforms resistance from an individual infection problem into a community-wide and even global threat."
        },
        {
            "question": "The model demonstrates that antibiotic resistance follows all four factors of evolution by natural selection. Which correctly matches each factor to the resistance scenario?",
            "choices": {
                "A": "1) Bacteria multiply rapidly, 2) Random mutations create variation, 3) Antibiotics create competition for survival, 4) Resistant bacteria survive and reproduce preferentially",
                "B": "1) Bacteria choose to become resistant, 2) Resistance is learned behavior, 3) All bacteria respond identically, 4) Antibiotics cause mutations",
                "C": "1) Bacteria reproduce slowly, 2) All bacteria are genetically identical, 3) Resources are unlimited, 4) Survival is random",
                "D": "1) Bacteria evolve intentionally, 2) Mutations are directed toward resistance, 3) Only strong antibiotics create selection, 4) Resistance disappears when antibiotics are removed"
            },
            "correct": "A",
            "feedback_correct": "Correct. This correctly maps the four factors: (1) population growth potential (rapid reproduction), (2) heritable variation (random mutations), (3) competition for limited resources (antibiotic selective pressure), and (4) differential survival (resistant bacteria proliferate).",
            "feedback_incorrect": "Incorrect. The four factors of natural selection in resistance are: (1) bacteria can increase rapidly in number, (2) heritable genetic variation exists from random mutations, (3) antibiotics create selective pressure/competition, (4) resistant organisms survive and reproduce preferentially."
        }
    ]
}

# =============================================================================
# L07 — Can We Edit the Human Genome? (HS-LS3-1)
# =============================================================================
L07_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is the function of the guide RNA in the CRISPR-Cas9 system?",
            "choices": {
                "A": "It provides energy for the Cas9 protein to cut DNA",
                "B": "It is a short RNA molecule engineered to match a specific DNA target, directing Cas9 to the exact genome location for editing",
                "C": "It repairs the DNA after Cas9 makes a cut",
                "D": "It protects the rest of the genome from being edited accidentally"
            },
            "correct": "B",
            "feedback_correct": "Correct. The guide RNA provides the specificity of CRISPR. It is designed to complement a specific DNA sequence, directing the Cas9 protein to the precise location where the edit should occur.",
            "feedback_incorrect": "Incorrect. Guide RNA acts as the targeting system. It is engineered to match a specific DNA sequence, guiding the Cas9 cutting protein to the exact location in the genome where the edit is intended."
        },
        {
            "question": "What is the critical difference between germline editing and somatic cell editing?",
            "choices": {
                "A": "Germline editing is less accurate than somatic editing",
                "B": "Somatic editing affects only the treated individual, while germline editing modifies sperm, eggs, or embryos and is inherited by all future generations",
                "C": "Germline editing only works in plants, not humans",
                "D": "Somatic editing changes DNA permanently while germline editing is temporary"
            },
            "correct": "B",
            "feedback_correct": "Correct. Germline edits are made in reproductive cells or embryos, meaning the changes are inherited by all descendants. Somatic edits affect only the treated individual's body cells and are not passed to offspring.",
            "feedback_incorrect": "Incorrect. The key difference is heritability. Germline edits (in sperm, eggs, embryos) are passed to all future generations, while somatic edits affect only the treated individual and are not inherited."
        },
        {
            "question": "What are off-target effects in the context of CRISPR gene editing?",
            "choices": {
                "A": "Intended edits that work better than expected",
                "B": "Unintended cuts or edits at DNA locations similar but not identical to the target sequence, potentially causing harmful mutations",
                "C": "The side effects of the drugs used alongside CRISPR treatment",
                "D": "Changes in gene expression that occur naturally without any editing"
            },
            "correct": "B",
            "feedback_correct": "Correct. Off-target effects occur when the guide RNA binds to DNA sequences similar to the intended target, directing Cas9 to make cuts at unintended locations. Even rare off-target cuts could activate cancer genes.",
            "feedback_incorrect": "Incorrect. Off-target effects are unintended edits at genome locations that are similar to the target sequence. They are the primary safety concern because unplanned cuts could disrupt essential genes or activate cancer-causing mutations."
        },
        {
            "question": "In 2023, the FDA approved the first CRISPR-based therapy. What disease does it treat?",
            "choices": {
                "A": "Type 2 diabetes",
                "B": "Sickle cell disease",
                "C": "Alzheimer's disease",
                "D": "Common cold"
            },
            "correct": "B",
            "feedback_correct": "Correct. The FDA approved CRISPR-based therapy for sickle cell disease in 2023, marking a milestone. Sickle cell is an ideal CRISPR target because it is caused by a single, well-characterized gene mutation.",
            "feedback_incorrect": "Incorrect. The first FDA-approved CRISPR therapy treats sickle cell disease. This single-gene disorder is ideal for CRISPR because the mutation is well-characterized and can be precisely targeted."
        },
        {
            "question": "Why is editing complex traits like intelligence or height fundamentally more difficult than editing single-gene disorders?",
            "choices": {
                "A": "Complex traits are not influenced by genes at all, only by environment",
                "B": "Complex traits are controlled by many genes (polygenic), and editing multiple genes simultaneously multiplies both difficulty and the risk of off-target effects",
                "C": "CRISPR can only work on genes located on chromosome 1",
                "D": "Complex traits are determined by a single gene that is too large to edit"
            },
            "correct": "B",
            "feedback_correct": "Correct. Complex traits like height involve 20+ genes. Each additional gene target multiplies editing complexity and off-target risk. The model shows dramatically different outcomes for single-gene vs. polygenic editing.",
            "feedback_incorrect": "Incorrect. Complex traits are polygenic (controlled by many genes). Each additional CRISPR target increases the probability of off-target effects multiplicatively, making multi-gene editing far riskier and less predictable than single-gene editing."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A scientist designs a guide RNA with 99.5% specificity to edit embryonic cells. The human genome has 3.2 billion base pairs. What does the model predict about off-target effects?",
            "choices": {
                "A": "99.5% specificity means virtually zero off-target effects",
                "B": "With 3.2 billion base pairs, even 0.5% non-specificity means up to 16 million potential off-target binding sites, creating significant risk especially in germline editing where errors are inherited",
                "C": "Off-target effects only occur when specificity is below 50%",
                "D": "The number of base pairs does not affect off-target calculations"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that 'nearly perfect' specificity is misleading when applied to a 3.2 billion base pair genome. Even 0.5% non-specificity creates millions of potential off-target sites, which is especially dangerous in germline editing.",
            "feedback_incorrect": "Incorrect. The genome's enormous size means even tiny percentages of non-specificity translate to millions of potential off-target sites. For germline editing, where mistakes are inherited by all future generations, this risk is particularly serious."
        },
        {
            "question": "The model predicts high Therapeutic Outcome for single-gene disorders like sickle cell disease. Which combination of model components explains this prediction?",
            "choices": {
                "A": "Low Guide RNA Specificity and high Off-Target Mutation Rate produce good outcomes for simple diseases",
                "B": "High Guide RNA Specificity targeting a single well-characterized gene location produces high Editing Efficiency with low Off-Target Mutation Rate, yielding strong Therapeutic Outcome",
                "C": "Therapeutic Outcome is independent of Guide RNA Specificity and depends only on the disease type",
                "D": "Single-gene disorders are easier because they do not require any DNA cutting"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that single-gene disorders are ideal CRISPR targets because: (1) guide RNA can be highly specific to one known target, (2) only one gene needs editing, keeping off-target risk low, and (3) editing efficiency is maximized with a single, well-characterized target.",
            "feedback_incorrect": "Incorrect. The model predicts success for single-gene disorders because high guide RNA specificity can be achieved for one well-known target, editing efficiency is high with a single target, and off-target risk stays low without multiplying across many targets."
        },
        {
            "question": "A student models the scenario of editing 5 genes simultaneously for a complex trait. How does the model predict Off-Target Mutation Rate will change compared to single-gene editing?",
            "choices": {
                "A": "Off-Target Mutation Rate decreases because multiple guide RNAs provide cross-checking accuracy",
                "B": "Off-Target Mutation Rate increases multiplicatively because each additional guide RNA introduces its own set of potential off-target binding sites across the genome",
                "C": "Off-Target Mutation Rate stays constant regardless of how many genes are targeted",
                "D": "Off-Target Mutation Rate doubles with each additional gene, following a linear pattern"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that each additional guide RNA introduces its own set of off-target risks, and these risks multiply rather than simply adding together, making multi-gene editing exponentially more dangerous.",
            "feedback_incorrect": "Incorrect. Each additional guide RNA in multi-gene editing introduces independent off-target risks that compound multiplicatively. Five simultaneous targets create far more than five times the risk of a single target."
        },
        {
            "question": "The model distinguishes between 'therapeutic' and 'enhancement' uses of gene editing. Which ethical criterion from the model best separates these categories?",
            "choices": {
                "A": "Cost of the procedure determines whether it is therapeutic or enhancement",
                "B": "Therapeutic editing corrects a known disease-causing mutation to restore normal function, while enhancement alters genes to exceed typical human variation for traits like height or intelligence",
                "C": "Any gene edit performed on an adult is therapeutic while any edit on an embryo is enhancement",
                "D": "The distinction is purely subjective with no scientific basis"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model supports a science-based distinction: therapeutic editing targets known pathogenic variants to restore normal protein function, while enhancement seeks to modify traits within or beyond normal human variation, which involves polygenic complexity and greater uncertainty.",
            "feedback_incorrect": "Incorrect. The scientific distinction is clear: therapeutic editing corrects known disease-causing mutations to restore normal function (supported by the model's single-gene success data), while enhancement targets traits within normal variation (which the model shows involves polygenic complexity and higher risk)."
        },
        {
            "question": "Based on the model's predictions about germline editing, which concern is MOST scientifically justified?",
            "choices": {
                "A": "Germline editing is too expensive to ever become widely available",
                "B": "Germline edits are permanent and heritable, meaning off-target errors cannot be undone and will propagate through all future generations of that lineage without the consent of those affected",
                "C": "Germline editing only works in non-human organisms",
                "D": "Germline editing always produces beneficial mutations in subsequent generations"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model's most powerful insight about germline editing is irreversibility: any off-target error is not just permanent in the individual but inherited by ALL descendants, affecting people who never consented to the modification.",
            "feedback_incorrect": "Incorrect. The model shows that germline editing's greatest risk is permanence and heritability. Unlike somatic edits (limited to one person), germline errors propagate through every subsequent generation, affecting individuals who could not consent."
        }
    ]
}

# =============================================================================
# L08 — Why Does Stress Make You Sick? (HS-LS1-3)
# =============================================================================
L08_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Many students report getting sick during winter break immediately after finals. Which physiological mechanism best explains this pattern?",
            "choices": {
                "A": "Cold weather during winter break causes more infections",
                "B": "Chronic stress suppresses immune function through sustained cortisol, and there is a lag between stress cessation and immune recovery, leaving a vulnerability window",
                "C": "Students are exposed to more germs at home than at school",
                "D": "Relaxation directly weakens the immune system"
            },
            "correct": "B",
            "feedback_correct": "Correct. During chronic stress, sustained cortisol suppresses immune cell production. When stress ends, cortisol drops but immune function doesn't recover immediately, creating a window of vulnerability when infections can take hold.",
            "feedback_incorrect": "Incorrect. The post-stress illness pattern occurs because chronic cortisol exposure suppresses immune function, and when stress ends, there is a lag before the immune system recovers. During this vulnerability window, infections can establish."
        },
        {
            "question": "What is the HPA axis and what role does it play in the stress response?",
            "choices": {
                "A": "A bone structure in the spine that causes back pain during stress",
                "B": "A neuroendocrine feedback loop where the hypothalamus signals the pituitary, which triggers cortisol release from the adrenal glands",
                "C": "A part of the digestive system that produces stomach acid during stress",
                "D": "A brain region responsible for generating fear responses to visual stimuli"
            },
            "correct": "B",
            "feedback_correct": "Correct. The HPA (hypothalamic-pituitary-adrenal) axis is a three-step feedback loop: hypothalamus detects stress, signals pituitary to release ACTH, which triggers adrenal cortisol release. Cortisol then feeds back to shut down the loop.",
            "feedback_incorrect": "Incorrect. The HPA axis is a neuroendocrine feedback loop: the hypothalamus signals the pituitary gland (via CRH), the pituitary releases ACTH, and the adrenal glands release cortisol. Cortisol feeds back to suppress further activation."
        },
        {
            "question": "How does cortisol affect the immune system differently during acute versus chronic stress?",
            "choices": {
                "A": "Cortisol has no effect on the immune system regardless of stress duration",
                "B": "Acute cortisol briefly enhances immune readiness for potential injury, while chronic cortisol suppresses lymphocyte production and antibody response",
                "C": "Both acute and chronic cortisol always suppress the immune system equally",
                "D": "Cortisol only affects the immune system in people with pre-existing autoimmune conditions"
            },
            "correct": "B",
            "feedback_correct": "Correct. This paradox is key: acute stress briefly mobilizes immune cells (adaptive for fight-or-flight), but chronic stress suppresses immune function by reducing T-cell, B-cell, and natural killer cell production and activity.",
            "feedback_incorrect": "Incorrect. Acute and chronic stress produce opposite immune effects. Acute cortisol briefly enhances immune readiness (adaptive for survival), while chronic cortisol suppresses lymphocyte production and increases vulnerability to infection."
        },
        {
            "question": "What is allostatic load?",
            "choices": {
                "A": "The weight of stress-related muscle tension in the body",
                "B": "The cumulative physiological wear and tear on the body from chronic stress response activation",
                "C": "The maximum amount of stress a person can handle before passing out",
                "D": "A measurement of how many stressful events a person has experienced in their lifetime"
            },
            "correct": "B",
            "feedback_correct": "Correct. Allostatic load represents the cumulative biological cost of chronic stress. It is measured through biomarkers including cortisol levels, blood pressure, inflammatory markers, and metabolic indicators.",
            "feedback_incorrect": "Incorrect. Allostatic load is the cumulative physiological damage from chronic stress activation. It is measured through biological markers (cortisol, blood pressure, inflammation, metabolic indicators) that reveal the long-term cost of sustained stress."
        },
        {
            "question": "Research shows that strong social support measurably reduces cortisol output during stressful periods. What does this suggest about the relationship between social connection and physical health?",
            "choices": {
                "A": "Social support is purely psychological comfort with no biological effects",
                "B": "Social support physically reduces HPA axis activation and cortisol release, providing a biological buffer that partially protects immune function during chronic stress",
                "C": "Social support only helps if the supportive person is a medical professional",
                "D": "Social connection increases cortisol because being around people is inherently stressful"
            },
            "correct": "B",
            "feedback_correct": "Correct. Social support is not just emotional comfort. Research shows it measurably reduces HPA axis activation, resulting in lower cortisol levels and partially preserved immune function during stressful periods.",
            "feedback_incorrect": "Incorrect. Social support has measurable biological effects: it reduces HPA axis activation and cortisol output, which partially protects immune function during chronic stress. This is a physiological mechanism, not just psychological comfort."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The stress-immune model includes five components: Stress Exposure, Social Support, Cortisol Level, Immune Function, and Health Outcome. In the 'Chronic Stress Without Support' scenario, which cascade does the model predict?",
            "choices": {
                "A": "Cortisol drops, Immune Function rises, Health Outcome improves",
                "B": "Continuous Stress Exposure with low Social Support keeps Cortisol Level chronically elevated, progressively declining Immune Function, and deteriorating Health Outcome over weeks",
                "C": "Social Support has no effect on the cascade because stress is too intense",
                "D": "Immune Function adapts to high cortisol and returns to normal within 48 hours"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model predicts a progressive decline: without social buffering, continuous stress maintains elevated cortisol, which progressively suppresses lymphocyte production, reducing immune capacity and worsening health outcomes over time.",
            "feedback_incorrect": "Incorrect. Without social support buffering, the model shows: sustained stress keeps cortisol elevated, chronic cortisol progressively suppresses immune cell production and function, and health outcomes deteriorate as the body becomes increasingly vulnerable."
        },
        {
            "question": "The model shows that Social Support buffers cortisol response. Comparing the 'Chronic Stress Without Support' and 'Chronic Stress With Strong Support' scenarios with identical stress levels, what key difference does the model predict?",
            "choices": {
                "A": "Social Support eliminates cortisol entirely, producing perfect health even under chronic stress",
                "B": "Strong Social Support reduces HPA axis activation, resulting in lower Cortisol Levels and partially preserved Immune Function, leading to measurably better Health Outcomes despite identical stress exposure",
                "C": "Social Support only affects perceived stress, not actual cortisol or immune markers",
                "D": "Both scenarios produce identical biological outcomes because the stressor is the same"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that social support physically reduces cortisol output (not just perceived stress), partially protecting immune function. The same chronic stressor produces measurably different biological outcomes depending on social support.",
            "feedback_incorrect": "Incorrect. The model demonstrates that social support is a biological modifier, not just emotional comfort. It reduces HPA axis activation and cortisol levels, partially preserving immune function and improving health outcomes even with identical stress exposure."
        },
        {
            "question": "The stress response evolved as a survival mechanism for short-term threats but becomes destructive when chronically activated. Which model evidence best explains this evolutionary mismatch?",
            "choices": {
                "A": "The stress response does not actually help with survival in any scenario",
                "B": "Acute cortisol mobilizes energy and briefly enhances immune readiness (adaptive for a 20-minute predator encounter), but the same mechanisms destroy immune function when activated continuously by modern chronic stressors the system was never designed to handle",
                "C": "Evolution has already corrected this mismatch in modern humans",
                "D": "Chronic stress only became possible after the invention of antibiotics"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows the mismatch: the HPA axis evolved for brief physical threats where cortisol's effects (energy mobilization, temporary immune boost) are adaptive. Modern chronic psychological stressors keep the system activated far beyond its design parameters.",
            "feedback_incorrect": "Incorrect. The model reveals an evolutionary mismatch: the stress response is optimized for brief, intense physical threats. Modern stressors (school pressure, social media, financial worry) are chronic and psychological, keeping the system activated far beyond what evolution designed."
        },
        {
            "question": "A student adds Sleep Quality as a component to the stress-immune model. Based on the known interactions, how does chronic stress-disrupted sleep create a compounding effect?",
            "choices": {
                "A": "Sleep disruption has no measurable effect on cortisol or immune function",
                "B": "Chronic stress disrupts sleep, and sleep deprivation independently elevates cortisol and suppresses immune function, creating a vicious cycle that compounds stress-immune damage beyond what either factor causes alone",
                "C": "Better sleep during chronic stress would completely eliminate all immune suppression",
                "D": "Sleep only affects physical recovery, not immune function or hormone levels"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model with added Sleep Quality shows a vicious cycle: stress disrupts sleep, poor sleep independently raises cortisol and suppresses immunity, which worsens stress response, which further disrupts sleep. The combined effect is greater than either alone.",
            "feedback_incorrect": "Incorrect. Adding Sleep Quality reveals a compounding cycle: chronic stress disrupts sleep architecture, and sleep deprivation independently elevates cortisol and suppresses immune function, amplifying the original stress-immune damage in a feedback loop."
        },
        {
            "question": "Based on the model, which school stress reduction intervention targets the MOST biologically impactful pathway?",
            "choices": {
                "A": "Posting motivational posters in hallways to improve student attitudes",
                "B": "Creating structured peer support programs that increase Social Support, which the model shows directly reduces HPA axis activation and cortisol output, providing measurable immune protection",
                "C": "Eliminating all homework to completely remove stress from students' lives",
                "D": "Teaching students to ignore stress signals because acknowledging them makes them worse"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model identifies Social Support as the most powerful modifiable variable. Structured peer support programs target the biological mechanism the model shows is most protective: reduced HPA axis activation and lower cortisol output.",
            "feedback_incorrect": "Incorrect. The model shows Social Support directly reduces cortisol output through reduced HPA axis activation. This is the most biologically impactful modifiable variable, making structured peer support programs the most evidence-based intervention."
        }
    ]
}

# =============================================================================
# L09 — Is Social Media Rewiring Your Brain? (HS-LS1-2)
# =============================================================================
L09_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Social media platforms use variable-ratio reinforcement schedules in their design. Which comparison best illustrates why this pattern is so addictive?",
            "choices": {
                "A": "It is like getting paid the same amount every hour at a job",
                "B": "It is the same mechanism that makes slot machines addictive: unpredictable rewards after an uncertain number of actions create the most compulsive behavior patterns",
                "C": "It is like earning a fixed grade on every assignment",
                "D": "It is similar to watching a movie with a predictable plot"
            },
            "correct": "B",
            "feedback_correct": "Correct. Variable-ratio reinforcement is the most addictive reward schedule known to behavioral neuroscience. The unpredictability of when the next reward (like, comment, viral post) will arrive creates compulsive checking behavior.",
            "feedback_incorrect": "Incorrect. Variable-ratio reinforcement, where rewards come after an unpredictable number of actions, is the same mechanism used in slot machines. It creates the most compulsive behavior because you never know when the next reward is coming."
        },
        {
            "question": "What is dopamine baseline and how does chronic social media use affect it?",
            "choices": {
                "A": "Dopamine baseline is the brain's resting mood level; social media has no effect on it",
                "B": "Dopamine baseline is the brain's resting dopamine activity; chronic overstimulation from social media can lower it, making non-digital activities feel boring and unrewarding",
                "C": "Dopamine baseline increases with social media use, making everything more enjoyable",
                "D": "Dopamine baseline is determined entirely by genetics and cannot change"
            },
            "correct": "B",
            "feedback_correct": "Correct. The dopamine baseline determines normal mood, motivation, and pleasure capacity. Chronic social media overstimulation lowers this baseline through receptor downregulation, making non-digital experiences feel less rewarding.",
            "feedback_incorrect": "Incorrect. Chronic social media use can lower the dopamine baseline through receptor downregulation. When baseline dopamine activity drops, non-digital activities like reading, conversation, and hobbies feel increasingly boring by comparison."
        },
        {
            "question": "What is attention fragmentation, and how does social media contribute to it?",
            "choices": {
                "A": "A medical condition unrelated to technology use",
                "B": "The progressive shortening of sustained attention capacity caused by the brain adapting to expect new content every few seconds through neuroplastic changes",
                "C": "The ability to focus on multiple social media platforms simultaneously, which improves multitasking",
                "D": "A temporary condition that resolves as soon as a person puts down their phone"
            },
            "correct": "B",
            "feedback_correct": "Correct. Attention fragmentation is a neuroplastic change where the brain physically strengthens rapid-switching circuits and weakens sustained-attention circuits. Social media trains the brain to expect new stimuli every few seconds.",
            "feedback_incorrect": "Incorrect. Attention fragmentation is a measurable neuroplastic change. Social media trains the brain to expect new content every few seconds, physically strengthening rapid-switching circuits while weakening the ability to sustain focus on longer tasks."
        },
        {
            "question": "TikTok serves videos every 15-60 seconds, each optimized by AI to maximize dopamine response. After two hours, a student tries to read a textbook. Why does the textbook feel unbearable?",
            "choices": {
                "A": "The textbook contains more difficult vocabulary than TikTok videos",
                "B": "Two hours of rapid dopamine hits from short-form content temporarily elevates the brain's reward threshold, making the slower, lower-stimulation experience of reading feel unsatisfying by comparison",
                "C": "The student is simply not interested in the subject of the textbook",
                "D": "Reading requires different eye muscles than watching videos, causing physical fatigue"
            },
            "correct": "B",
            "feedback_correct": "Correct. Rapid-fire short-form content creates a temporarily elevated dopamine threshold. The textbook's slower, lower-stimulation experience cannot compete, making it feel unsatisfying and requiring more effort to sustain attention.",
            "feedback_incorrect": "Incorrect. Two hours of rapid dopamine hits raises the brain's reward threshold. The textbook delivers stimulation below this elevated threshold, making it feel boring and effortful. The brain has been temporarily trained to expect constant novelty."
        },
        {
            "question": "Can the brain recover from the neurological effects of heavy social media use?",
            "choices": {
                "A": "No, all changes to brain structure from social media are permanent and irreversible",
                "B": "Yes, digital detox studies show measurable improvement in dopamine sensitivity and attention span within 2-4 weeks, though full recovery depends on duration and intensity of prior use",
                "C": "Recovery happens instantly as soon as a person deletes their social media accounts",
                "D": "Only children's brains can recover; adult brains are permanently changed"
            },
            "correct": "B",
            "feedback_correct": "Correct. Neuroplasticity works in both directions. Digital detox research shows measurable recovery of dopamine sensitivity and attention capacity within 2-4 weeks, though complete recovery may take longer depending on the extent of prior use.",
            "feedback_incorrect": "Incorrect. The brain's neuroplasticity enables recovery. Digital detox studies demonstrate measurable improvements in attention and dopamine sensitivity within 2-4 weeks, though full restoration depends on the duration and intensity of prior heavy use."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model includes Social Media Exposure, Notification Frequency, Dopamine Sensitivity, Attention Capacity, and Cognitive Well-Being. After 30 days of 4+ hours of passive scrolling with maximum notifications, what does the model predict?",
            "choices": {
                "A": "Dopamine Sensitivity increases and Attention Capacity improves because the brain is getting more practice",
                "B": "Dopamine Sensitivity decreases through receptor downregulation, Attention Capacity shrinks due to neuroplastic strengthening of rapid-switching circuits, and Cognitive Well-Being deteriorates",
                "C": "Only Attention Capacity changes; Dopamine Sensitivity is unaffected by passive scrolling",
                "D": "All components return to baseline within 24 hours of stopping"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model predicts a three-part decline: receptor downregulation lowers Dopamine Sensitivity, neuroplastic changes shorten Attention Capacity, and both effects compound to reduce Cognitive Well-Being (working memory, impulse control, emotional regulation).",
            "feedback_incorrect": "Incorrect. The model shows heavy passive use drives three interconnected declines: dopamine receptor downregulation reduces reward sensitivity, neuroplastic adaptation weakens sustained attention circuits, and both compound to impair overall cognitive well-being."
        },
        {
            "question": "The model compares passive scrolling versus active content creation with equal total screen time. Why does the model predict different neurological outcomes for these two usage patterns?",
            "choices": {
                "A": "Active creation uses different apps, which have different screen resolutions",
                "B": "Passive scrolling delivers rapid, variable-ratio dopamine hits that drive receptor downregulation, while active creation engages sustained attention, goal-directed behavior, and prefrontal cortex function, producing a different dopamine release pattern",
                "C": "The outcomes are identical because total screen time is the only variable that matters",
                "D": "Active creation is more addictive than passive scrolling because it involves more effort"
            },
            "correct": "B",
            "feedback_correct": "Correct. The type of engagement matters as much as duration. Passive scrolling triggers rapid variable-ratio dopamine hits, while active creation engages different neural circuits (sustained attention, prefrontal planning) with more natural dopamine patterns.",
            "feedback_incorrect": "Incorrect. The model shows that dopamine release patterns differ by usage type. Passive scrolling provides rapid, unpredictable rewards that downregulate receptors, while active creation engages sustained attention and goal-directed processing with healthier dopamine dynamics."
        },
        {
            "question": "The model predicts that a 14-day digital detox shows partial recovery. Why does the model predict that full recovery requires weeks to months rather than days?",
            "choices": {
                "A": "Social media toxins must be physically eliminated from the bloodstream, which takes months",
                "B": "Neuroplastic changes (strengthened rapid-switching circuits, weakened sustained-attention circuits, downregulated dopamine receptors) are structural brain adaptations that require time to reverse through new neuroplastic rewiring",
                "C": "Recovery takes months because the brain must generate entirely new neurons to replace damaged ones",
                "D": "Recovery is actually instant; the model's prediction of weeks to months is incorrect"
            },
            "correct": "B",
            "feedback_correct": "Correct. The changes from heavy social media use are neuroplastic (structural). Reversing them requires the brain to strengthen sustained-attention circuits and upregulate dopamine receptors through new neuroplastic changes, which is a gradual process.",
            "feedback_incorrect": "Incorrect. Recovery takes time because the changes are neuroplastic (structural adaptations in neural circuits). Rebuilding sustained-attention pathways and upregulating dopamine receptors requires time for new structural changes, just as the original damage developed gradually."
        },
        {
            "question": "A student adds FOMO Activation as a component to the model. How does FOMO interact with the existing dopamine-based mechanisms to keep users engaged?",
            "choices": {
                "A": "FOMO is identical to dopamine reward and operates through the same pathway",
                "B": "FOMO operates through anxiety pathways separate from but synergistic with the dopamine reward system, creating a dual-drive mechanism where users check both to seek rewards AND to avoid the anxiety of missing out",
                "C": "FOMO has no biological basis and is purely a marketing concept",
                "D": "FOMO only affects users under 13 years old"
            },
            "correct": "B",
            "feedback_correct": "Correct. FOMO adds an anxiety-based drive that operates through different neural pathways than dopamine reward. Together, they create a dual mechanism: users check for rewards (dopamine) AND to relieve anxiety about missing out (FOMO), making disengagement doubly difficult.",
            "feedback_incorrect": "Incorrect. FOMO operates through anxiety pathways that are separate from but synergistic with the dopamine reward system. This dual-drive mechanism means users are pulled to check by both reward-seeking AND anxiety-avoidance, compounding the addictive pull."
        },
        {
            "question": "Based on the model's evidence about variable-ratio reinforcement and neuroplasticity, which regulatory approach is MOST directly supported by the neuroscience?",
            "choices": {
                "A": "Banning all social media for people under 25",
                "B": "Requiring platforms to disclose the specific psychological manipulation techniques they use (like variable-ratio reinforcement) and mandating design changes that reduce addictive features, similar to how nutrition labels disclose food ingredients",
                "C": "Making social media use a mandatory part of school curriculum to build tolerance",
                "D": "Regulation is unnecessary because individuals can simply choose to use less social media"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that platforms deliberately exploit known addictive mechanisms. Transparency requirements and design regulations address the root cause (engineered addiction) rather than placing the full burden on individuals whose brains are being manipulated.",
            "feedback_incorrect": "Incorrect. The model demonstrates that platforms use deliberate psychological manipulation (variable-ratio reinforcement, notification systems). Requiring disclosure and design changes addresses the engineered addictiveness at its source, rather than asking individuals to resist neuroscientific manipulation alone."
        }
    ]
}

# =============================================================================
# L10 — How Can One Mutation Change Everything? (HS-LS3-2)
# =============================================================================
L10_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "The human genome contains 3.2 billion base pairs. Every human carries millions of mutations compared to each other. Why are most people not seriously ill from these mutations?",
            "choices": {
                "A": "Modern medicine corrects most mutations before they cause problems",
                "B": "Most mutations are neutral because of genetic code redundancy, non-coding DNA locations, and many amino acid positions tolerating substitution without affecting protein function",
                "C": "Humans have evolved to be immune to all mutations",
                "D": "Mutations only occur in non-essential parts of the body like hair and nails"
            },
            "correct": "B",
            "feedback_correct": "Correct. Three factors protect against most mutations: (1) genetic code redundancy means ~25% of point mutations are silent, (2) over 98% of DNA is non-coding, and (3) many protein positions tolerate amino acid changes without functional impact.",
            "feedback_incorrect": "Incorrect. Most mutations are neutral due to built-in buffers: genetic code redundancy (multiple codons for the same amino acid), the vast amount of non-coding DNA, and many protein positions that can tolerate amino acid substitutions."
        },
        {
            "question": "What is a point mutation?",
            "choices": {
                "A": "A mutation that occurs at the pointed end of a chromosome",
                "B": "A change in a single nucleotide base that can be silent, missense, or nonsense depending on its effect on the amino acid sequence",
                "C": "Any mutation that causes a disease",
                "D": "A mutation that only occurs during embryonic development"
            },
            "correct": "B",
            "feedback_correct": "Correct. A point mutation is a single nucleotide change. It can be silent (no amino acid change), missense (one amino acid changed), or nonsense (premature stop codon), with vastly different phenotypic consequences.",
            "feedback_incorrect": "Incorrect. A point mutation changes one nucleotide. Its effect depends on whether it is silent (no change to amino acid), missense (one amino acid substitution), or nonsense (creates a stop codon). Location and type determine impact."
        },
        {
            "question": "Why are frameshift mutations typically more damaging than point mutations?",
            "choices": {
                "A": "Frameshift mutations are louder and more easily detected by the cell's repair systems",
                "B": "An insertion or deletion that is not a multiple of three shifts the entire reading frame, changing every amino acid downstream and usually producing a completely nonfunctional protein",
                "C": "Frameshift mutations only occur in genes that control essential functions",
                "D": "Frameshift mutations are less damaging because they only affect one amino acid"
            },
            "correct": "B",
            "feedback_correct": "Correct. Frameshift mutations shift the reading frame of all downstream codons, producing a completely different amino acid sequence from the point of mutation onward. This typically results in a nonfunctional protein.",
            "feedback_incorrect": "Incorrect. Frameshift mutations are devastating because they shift the reading frame, causing every codon after the mutation to be read differently. This changes every downstream amino acid, typically producing a completely nonfunctional protein."
        },
        {
            "question": "Sickle cell disease is caused by a single amino acid change in hemoglobin (glutamic acid to valine at position 6). How can such a small change cause such severe disease?",
            "choices": {
                "A": "Position 6 is at the very end of the protein, so any change there is always fatal",
                "B": "The amino acid change alters the surface chemistry of hemoglobin, causing molecules to polymerize into rigid fibers that distort red blood cells, blocking blood flow",
                "C": "The mutation causes the body to stop producing hemoglobin entirely",
                "D": "Valine is toxic to red blood cells regardless of its location in any protein"
            },
            "correct": "B",
            "feedback_correct": "Correct. The glutamic acid to valine change replaces a charged, hydrophilic amino acid with a hydrophobic one, creating a sticky patch on hemoglobin's surface. Under low oxygen, hemoglobin molecules polymerize into fibers, distorting red blood cells into sickle shapes.",
            "feedback_incorrect": "Incorrect. The E6V mutation changes a charged amino acid to a hydrophobic one, creating a sticky patch on hemoglobin. Under low oxygen conditions, these sticky patches cause hemoglobin molecules to polymerize into rigid fibers that distort red blood cells."
        },
        {
            "question": "Why is protein folding critical for understanding mutation effects?",
            "choices": {
                "A": "Protein folding is decorative and does not affect protein function",
                "B": "Proteins are molecular machines whose function depends on their precise three-dimensional structure, which is determined by amino acid sequence, so even single amino acid changes can destabilize folding and destroy function",
                "C": "Only unfolded proteins are functional in cells",
                "D": "Protein folding only matters for structural proteins like collagen, not enzymes"
            },
            "correct": "B",
            "feedback_correct": "Correct. Protein function depends entirely on three-dimensional structure, which depends on amino acid sequence, which depends on DNA sequence. A single mutation can alter an amino acid, destabilize folding, and destroy function.",
            "feedback_incorrect": "Incorrect. The cascade is DNA sequence -> amino acid sequence -> protein folding -> protein function. Proteins are molecular machines that only work in their correct 3D shape. Even one amino acid change at a critical position can destabilize this folding."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The mutation model predicts that a synonymous (silent) point mutation in a coding region will produce zero Phenotypic Impact. Which mechanism explains this prediction?",
            "choices": {
                "A": "Silent mutations are repaired by DNA polymerase before they can have any effect",
                "B": "The genetic code's redundancy means multiple codons specify the same amino acid, so the DNA changes but the protein sequence and structure remain identical",
                "C": "Silent mutations only occur in non-essential genes",
                "D": "All point mutations are silent and never cause phenotypic changes"
            },
            "correct": "B",
            "feedback_correct": "Correct. The genetic code has 64 codons for only 20 amino acids. This redundancy means about 25% of point mutations change the DNA but not the amino acid, producing identical protein with zero phenotypic effect.",
            "feedback_incorrect": "Incorrect. Genetic code redundancy is the mechanism: 64 codons code for only 20 amino acids. A synonymous mutation changes the DNA codon but produces the same amino acid, so protein structure, function, and phenotype are all unchanged."
        },
        {
            "question": "Using the model, compare a missense mutation at position 6 of a 147-amino-acid protein versus the same type of mutation at position 140. Why might the model predict dramatically different Phenotypic Impact?",
            "choices": {
                "A": "The model predicts identical impact because both are missense mutations in the same protein",
                "B": "Phenotypic Impact depends on whether the affected position is structurally or functionally critical; position 6 in hemoglobin affects surface chemistry critical for preventing polymerization, while position 140 may be in a region tolerant of substitution",
                "C": "Later positions in a protein are always more important than earlier ones",
                "D": "Only mutations in the first 10 amino acids of any protein can cause disease"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that location within the protein matters as much as mutation type. The same type of mutation at a critical functional site versus a tolerant surface region produces vastly different structural changes and phenotypic outcomes.",
            "feedback_incorrect": "Incorrect. The model predicts that Phenotypic Impact depends on the functional importance of the affected amino acid position. Some positions are critical for protein structure/function, while others tolerate substitutions with minimal effect."
        },
        {
            "question": "The model compares a frameshift mutation (single base insertion at position 10) versus a missense mutation at position 450 of a 500-amino-acid protein. Why does the model predict the frameshift is more damaging?",
            "choices": {
                "A": "Insertions are always more damaging than substitutions regardless of location",
                "B": "The early frameshift changes the reading frame for 490 downstream amino acids (98% of the protein), producing a completely nonfunctional protein, while the missense at position 450 changes only one amino acid near the protein's end",
                "C": "Position 10 is always more important than position 450 in every protein",
                "D": "The model predicts the missense mutation is actually more damaging because it occurs later in the gene"
            },
            "correct": "B",
            "feedback_correct": "Correct. The early frameshift scrambles nearly the entire protein (490 of 500 amino acids), guaranteeing complete loss of structure and function. The late missense changes only one amino acid, and its impact depends on that position's functional importance.",
            "feedback_incorrect": "Incorrect. An early frameshift shifts the reading frame for virtually the entire protein, producing a completely different and nonfunctional amino acid sequence. A late missense changes only one amino acid near the end, which may or may not be at a critical site."
        },
        {
            "question": "The sickle cell mutation provides heterozygote advantage in malaria-endemic regions. How does the model explain why the same mutation can be simultaneously harmful, neutral, and beneficial?",
            "choices": {
                "A": "The mutation changes effect based on the weather and climate conditions",
                "B": "In homozygotes (two copies), severe sickling causes disease; in heterozygotes (one copy), enough normal hemoglobin prevents disease while sickle hemoglobin makes red blood cells inhospitable to the malaria parasite, creating a context-dependent phenotype",
                "C": "The model cannot account for a mutation being both harmful and beneficial",
                "D": "The mutation is beneficial in all people regardless of genotype or environment"
            },
            "correct": "B",
            "feedback_correct": "Correct. Gene dosage and environmental context determine phenotype. Homozygotes (HbSS) have severe disease. Heterozygotes (HbAS) produce enough normal hemoglobin to avoid sickling while gaining malaria resistance. This is heterozygote advantage.",
            "feedback_incorrect": "Incorrect. The model shows that phenotypic impact depends on dosage and environment. Two copies cause disease, one copy provides malaria protection with minimal sickling. The same mutation is harmful, neutral, or beneficial depending on genotype and geographic context."
        },
        {
            "question": "Based on the model, most mutations are neutral rather than harmful. Why is this fact essential for understanding evolution by natural selection?",
            "choices": {
                "A": "Neutral mutations have no relevance to evolution because natural selection only acts on harmful mutations",
                "B": "Neutral mutations allow genetic variation to accumulate in populations without killing organisms, providing the raw material that natural selection can act upon when environmental conditions change",
                "C": "If all mutations were neutral, evolution could not occur",
                "D": "Neutral mutations are actively selected for by natural selection because they are always beneficial"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that neutral mutations are the primary source of standing genetic variation. This accumulated variation provides the raw material for natural selection to act upon when environmental conditions change, enabling adaptation.",
            "feedback_incorrect": "Incorrect. Neutral mutations are essential for evolution because they allow genetic variation to build up in populations without causing disease. This reservoir of variation becomes the raw material that natural selection can act upon when environmental pressures change."
        }
    ]
}

# =============================================================================
# Master Dictionary — ALL QUESTIONS
# =============================================================================
ALL_QUESTIONS = {
    "G12L1-L01": L01_QUESTIONS,
    "G12L1-L02": L02_QUESTIONS,
    "G12L1-L03": L03_QUESTIONS,
    "G12L1-L04": L04_QUESTIONS,
    "G12L1-L05": L05_QUESTIONS,
    "G12L1-L06": L06_QUESTIONS,
    "G12L1-L07": L07_QUESTIONS,
    "G12L1-L08": L08_QUESTIONS,
    "G12L1-L09": L09_QUESTIONS,
    "G12L1-L10": L10_QUESTIONS,
}
