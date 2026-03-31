#!/usr/bin/env python3
"""Complete lesson data for G07L2-L01 through G07L2-L07 (Grade 7 Level 2 ModelIt! Lessons)"""

L01 = {
    "id": "G07L2-L01",
    "title": "The Invisible War: How Your Immune System Fights Back",
    "subtitle": "Your Body's Army Against Invaders",
    "ngss": "MS-LS1-3, MS-LS1-8",
    "ngss_desc": "Use argument supported by evidence for how the body is a system of interacting subsystems composed of groups of cells. Gather and synthesize information that sensory receptors respond to stimuli by sending messages to the brain for immediate behavior or storage as memories.",
    "big_question": "How does your body know the difference between you and an invader, and how does it fight back?",
    "objectives": [
        "Model how the immune system detects and responds to pathogen invasions",
        "Explain how vaccines train the immune system to produce antibodies before infection",
        "Predict infection severity based on pathogen load and immune system preparedness",
        "Describe how white blood cells and antibodies work together as interacting subsystems"
    ],
    "vocabulary": [
        ("Pathogen", "A microorganism such as a bacterium or virus that can cause disease when it enters the body"),
        ("Antibody", "A Y-shaped protein produced by white blood cells that specifically targets and neutralizes a particular pathogen"),
        ("Vaccine", "A weakened or inactive form of a pathogen that trains the immune system to recognize and fight the real pathogen"),
        ("White Blood Cell", "A type of blood cell that defends the body against infection by identifying, attacking, and destroying pathogens")
    ],
    "components": [
        ("Pathogen Load", "Amount of bacteria or virus entering the body at one time", True),
        ("Vaccine Status", "Whether the immune system has been previously trained to recognize this pathogen", True),
        ("White Blood Cell Response", "How quickly and strongly immune cells activate to fight the invasion", False),
        ("Antibody Production", "The rate at which targeted pathogen-fighting proteins are created", False),
        ("Infection Severity", "How sick the person gets based on pathogen spread vs. immune response", False)
    ],
    "think_about_it": "When a vaccinated person encounters a high pathogen load, what happens to antibody production compared to an unvaccinated person? How does this affect infection severity?",
    "scenarios": [
        ("Unvaccinated Exposure", "Set Pathogen Load to high and Vaccine Status to off and observe Infection Severity"),
        ("Vaccinated Exposure", "Set Pathogen Load to high and Vaccine Status to on and observe the difference"),
        ("Low Exposure", "Set Pathogen Load to low with no vaccine and observe whether the body can handle it")
    ],
    "sim_scenarios": [
        ("Unvaccinated + High Pathogen", "High pathogen load, no prior vaccination", "What do you predict happens to Infection Severity when the body has never seen this pathogen before?"),
        ("Vaccinated + High Pathogen", "High pathogen load, immune system pre-trained", "What do you predict happens differently when the immune system already knows how to make antibodies?"),
        ("Low Pathogen + No Vaccine", "Small pathogen exposure, no vaccine", "Can the body fight off a small invasion on its own? What do you predict?")
    ],
    "discoveries": [
        "The immune system has two lines of defense: fast general response (white blood cells) and slow targeted response (antibodies)",
        "Vaccines work by giving the immune system a head start, so antibody production begins immediately upon infection",
        "Higher pathogen loads overwhelm the immune system faster, making the white blood cell response critical in the first hours",
        "The immune system remembers past infections, which is why you rarely get the same illness twice"
    ],
    "answer": "Your body fights back using a two-part system. White blood cells respond immediately to any invader, while antibodies are custom-built weapons that target specific pathogens. Vaccines pre-train your immune system so antibody production starts immediately instead of taking days, which is why vaccinated people get less sick or don't get sick at all!",
    "stem_title": "Design a Public Health Campaign",
    "stem_mission": "Create an evidence-based public health campaign explaining how the immune system works and why vaccination matters, using data from your simulation model.",
    "stem_scenario": "A local health department needs help explaining to the community how vaccines work. Your team has been asked to create educational materials that use real scientific models to show the difference between vaccinated and unvaccinated immune responses.",
    "stem_questions": [
        "How can you use your model data to show the difference vaccines make?",
        "What visual representations best explain antibody production to non-scientists?",
        "How do you address common misconceptions about the immune system in your campaign?"
    ],
    "stem_design_qs": [
        "What format will your campaign use (poster, video, infographic, presentation)?",
        "How will you represent the invisible processes of the immune system visually?",
        "What model data will you include as evidence for vaccine effectiveness?",
        "How will you make complex immunology accessible to a general audience?"
    ],
    "career": "Immunologists study the immune system and develop treatments for diseases, allergies, and autoimmune disorders. They work at research hospitals, pharmaceutical companies, and the CDC, earning $75,000-$150,000/year.",
    "images": {
        "cover": ("cover-immune-war.png", "A dramatic 3D visualization of white blood cells and antibodies attacking virus particles inside the human body, glowing blue and purple immune cells surrounding red virus particles, cinematic medical illustration"),
        "landscape": ("landscape-immune.png", "A group of 7th grade students in a modern science lab using microscopes to examine blood cell slides, a White female student and an Asian male student examining slides together while a Black male student records observations, bright modern lab"),
        "modeling": ("modeling-immune.png", "A diverse group of 7th grade students working on laptops building a digital immune system model, a Latino male student pointing at the screen explaining to classmates, classroom with anatomy posters on walls"),
        "discussion": ("discussion-immune.png", "A teacher pointing at a large diagram of the immune response on a smartboard while 7th grade students raise hands, an Asian female student and a White male student actively participating, bright modern classroom"),
        "stem": ("stem-immune-campaign.png", "7th grade students creating a public health campaign poster about vaccination, a Black female student leading the design while a Latino female student and White male student contribute ideas, collaborative group work")
    },
    "pre_assessment": [
        "What do you think happens inside your body when you get sick?",
        "Why do you think some people get sicker than others from the same illness?",
        "Draw what you think a white blood cell does when a virus enters your body.",
        "How do you think vaccines help prevent disease?"
    ],
    "extend_components": [
        ("Memory Cell Formation", "Long-lived immune cells that remember specific pathogens and activate faster during re-infection"),
        ("Fever Response", "The body raising its temperature to slow pathogen reproduction and speed up immune cell activity"),
        ("Inflammatory Response", "Increased blood flow and swelling at the infection site that brings more immune cells to the area")
    ],
    "reflections": [
        "Why does it take several days to recover from a new illness but your body fights it faster the second time?",
        "How does your model show that vaccines don't prevent exposure but do prevent severe illness?",
        "What would happen in your model if white blood cells couldn't communicate with antibody-producing cells?",
        "Why is herd immunity important for people who can't be vaccinated?",
        "How is the immune system an example of interacting subsystems within the body?"
    ],
    "dimensions": [
        ("Science Practice", "Engaging in Argument from Evidence", "Students use model evidence to argue how the body's immune subsystems interact to fight pathogens."),
        ("Disciplinary Core Idea", "LS1.A Structure and Function", "The body is a system of interacting subsystems composed of groups of cells that work together to fight infection and maintain health."),
        ("Crosscutting Concept", "Systems and System Models", "Students model the immune system as interacting subsystems where white blood cells, antibodies, and memory cells work together.")
    ],
    "cast_items": [
        "Use evidence to argue how the immune system functions as interacting subsystems",
        "Explain how vaccines alter the immune response timeline and severity",
        "Model the relationship between pathogen load, immune response, and infection outcome"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A vaccinated person and an unvaccinated person are both exposed to the same virus. The vaccinated person shows mild symptoms while the unvaccinated person becomes severely ill. Which best explains this difference?"),
        ("Constructed Response:", "Using your immune system model, explain how white blood cells and antibodies work together as interacting subsystems to fight a pathogen. Include how vaccination changes this interaction.")
    ],
    "background_intro": "Your body is constantly under attack from pathogens, bacteria, viruses, and other microorganisms that can cause disease. The immune system is a complex network of cells, tissues, and organs that work together to defend the body, acting as interacting subsystems within the larger body system.",
    "background_sections": [
        ("First Line of Defense", "The body's first defenses are physical barriers: skin blocks most pathogens, mucus traps them in the nose and throat, and stomach acid destroys many that are swallowed. These are non-specific defenses that work against all types of invaders."),
        ("White Blood Cell Response", "When pathogens breach physical barriers, white blood cells are the first immune cells to respond. Neutrophils arrive within hours, engulfing and destroying invaders. Macrophages follow, cleaning up debris and presenting pathogen fragments to other immune cells to trigger a targeted response."),
        ("Antibody Production", "B-cells produce antibodies: Y-shaped proteins that lock onto specific pathogen molecules called antigens. Each antibody is custom-made for one pathogen type. The first time the body encounters a pathogen, antibody production takes 7-10 days. This delay is why new infections make you sick."),
        ("Immune Memory and Vaccines", "After fighting an infection, the immune system creates memory cells that remember the pathogen's identity. If the same pathogen returns, antibody production begins within hours instead of days. Vaccines exploit this by introducing harmless versions of pathogens to trigger memory cell formation without causing disease.")
    ],
    "lever_L": "Students identify pathogen load, vaccine status, white blood cell response, antibody production, and infection severity as key components of the immune system.",
    "lever_E": "Students determine that pathogen load drives infection severity positively while vaccine status and immune responses reduce it through negative relationships.",
    "lever_V": "Students build a model showing how the immune system's interacting subsystems respond to pathogen invasion with and without prior vaccination.",
    "lever_Ev": "Students run vaccinated, unvaccinated, and low-exposure scenarios to compare immune response timelines and infection outcomes.",
    "lever_R": "Students add memory cell formation or fever response to explore how the immune system adapts and strengthens over time.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic immune cell imagery", "say": "Right now, inside your body, there's a war happening. And you're winning.", "do": "Show a dramatic visualization of immune cells attacking pathogens.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're building a model of the most sophisticated defense system on Earth: YOUR immune system.", "do": "Have students read objectives. Pre-teach 'pathogen' and 'antibody.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How does your body fight back?", "say": "You've been sick before. But how does your body know something doesn't belong? And how does it fight back?", "do": "Quick poll: Who has been sick in the last year? What happened? How did you recover?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model the immune system as a set of interacting parts that work together.", "do": "Preview each LEVER step. Emphasize the idea of SUBSYSTEMS working together.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for immune system model", "say": "What are the key players in this invisible war? What can we control vs. what responds automatically?", "do": "Guide sorting of external vs. internal components. Discuss why vaccine status is an input.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "When pathogen load goes up, what happens to white blood cell response? And how does that affect how sick you get?", "do": "Help students identify positive and negative relationships. Trace the cascade.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's infect a vaccinated person and an unvaccinated person with the same virus. What happens?", "do": "Students predict first, then run simulations. Compare the graphs side by side.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "So why do vaccinated people get less sick? What did our model reveal about the TIMING of antibody production?", "do": "Lead discussion about immune memory. Connect to real-world vaccination data.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Public health campaign design", "say": "You now understand the science. Can you explain it to someone who doesn't?", "do": "Groups design public health campaigns using model evidence.", "time": "12 min"}
    ],
    "sort_reasoning": "Pathogen Load and Vaccine Status are external because they are inputs the student controls: how much pathogen enters the body and whether the immune system was pre-trained. White Blood Cell Response, Antibody Production, and Infection Severity are internal because they change automatically based on those inputs.",
    "relationships": [
        ("Pathogen Load to Infection Severity", "POSITIVE (+)", "More pathogens entering the body means the infection can spread faster and cause more damage before the immune system catches up."),
        ("Vaccine Status to Antibody Production", "POSITIVE (+)", "When the immune system has been vaccinated, it already has memory cells ready to produce antibodies immediately upon infection."),
        ("White Blood Cell Response to Infection Severity", "NEGATIVE (-)", "A stronger white blood cell response destroys more pathogens early, reducing how severe the infection becomes."),
        ("Antibody Production to Infection Severity", "NEGATIVE (-)", "Antibodies specifically target and neutralize pathogens, directly reducing infection severity."),
        ("Pathogen Load to White Blood Cell Response", "POSITIVE (+)", "More pathogens trigger a larger immune response as the body detects the growing threat.")
    ],
    "sim_answers": [
        ("Unvaccinated + High Pathogen Scenario", "With high Pathogen Load and no Vaccine Status, White Blood Cell Response activates but antibody production is slow (7-10 day delay). Infection Severity rises rapidly because the immune system is fighting blind, without pre-made antibodies. The person gets very sick before the body catches up."),
        ("Vaccinated + High Pathogen Scenario", "With the same high Pathogen Load but Vaccine Status on, Antibody Production begins almost immediately thanks to memory cells. White Blood Cell Response still activates, but antibodies neutralize pathogens so quickly that Infection Severity stays low. The person experiences mild or no symptoms.")
    ],
    "reflection_exemplars": [
        ("Why does the body fight faster the second time?", "The first time the body encounters a pathogen, it takes 7-10 days to identify the invader, design antibodies, and mass-produce them. But after the infection clears, the immune system creates memory cells that store the antibody blueprint. The second time that pathogen appears, memory cells recognize it instantly and begin producing antibodies within hours, not days."),
        ("How is the immune system an example of interacting subsystems?", "The immune system works because multiple subsystems communicate and cooperate. White blood cells detect and present pathogen information to B-cells. B-cells then produce targeted antibodies. Memory cells store the information long-term. No single part can fight infection alone. They are interacting subsystems within the larger body system, each with a specific role.")
    ],
    "stem_intro": "A local health department needs help explaining how vaccines work to the community. Your team will create educational materials that use real scientific model data to show the difference between vaccinated and unvaccinated immune responses.",
    "stem_concepts": [
        ("Innate vs. Adaptive Immunity", "Innate immunity is the body's immediate, non-specific response (white blood cells, inflammation). Adaptive immunity is the slow but targeted response (antibodies, memory cells). Vaccines enhance adaptive immunity."),
        ("Herd Immunity", "When enough people in a population are immune to a disease (through vaccination or prior infection), the pathogen can't spread easily, protecting even those who aren't immune."),
        ("Immune System Memory", "Memory B-cells and T-cells can survive for decades, maintaining the ability to produce antibodies against pathogens the body fought years ago. This is why some vaccines provide lifelong protection.")
    ],
    "stem_eval": [
        ("Expert (4)", "Campaign accurately explains immune system subsystems, uses model data to show vaccinated vs. unvaccinated responses, and addresses common misconceptions with evidence"),
        ("Proficient (3)", "Campaign explains how vaccines work and includes model evidence comparing immune responses"),
        ("Developing (2)", "Campaign mentions vaccines but doesn't clearly connect to the immune system model or use data"),
        ("Beginning (1)", "Campaign is incomplete or contains scientific inaccuracies about how the immune system works")
    ],
    "support": [
        "Provide a simplified diagram of the immune response timeline for reference",
        "Use colored beads to physically model pathogens (red), white blood cells (white), and antibodies (yellow)",
        "Sentence frames: 'When pathogen load increases, __ happens because __'"
    ],
    "extensions": [
        "Research how autoimmune diseases occur when the immune system attacks the body's own cells",
        "Investigate how HIV specifically targets white blood cells and why this makes it so dangerous",
        "Add fever response as a component and model how raising body temperature helps fight infection"
    ],
    "cross_curr": [
        ("Math", "Graph antibody production rates over time for vaccinated vs. unvaccinated individuals and calculate the difference"),
        ("ELA", "Write a persuasive essay using model evidence to explain how vaccines work to a skeptical audience"),
        ("Social Studies", "Research the history of vaccination from Edward Jenner's smallpox vaccine to modern mRNA technology")
    ],
    "misconceptions": [
        ("Vaccines give you the disease", "Vaccines contain weakened, inactivated, or partial versions of pathogens that CANNOT cause the full disease. Some people feel mild side effects (sore arm, low fever) because the immune system is RESPONDING to the vaccine and building defenses, not because they're sick.", "Analogy: A fire drill doesn't burn down the school. It trains you to respond. Vaccines are fire drills for your immune system."),
        ("Antibiotics kill viruses", "Antibiotics only work against bacteria by disrupting their cell walls or reproduction. Viruses are not cells, so antibiotics have no effect on them. That's why doctors don't prescribe antibiotics for the flu or common cold.", "Ask: Can you use a key designed for one lock to open a completely different lock? Antibiotics are keys that only fit bacterial locks."),
        ("If you're healthy, you don't need vaccines", "Even healthy people can get severely ill from certain diseases. Vaccines also protect vulnerable people around you (babies, elderly, immunocompromised) through herd immunity. Your vaccination protects your community, not just you.", "Show how one unvaccinated person in a group can spread disease to those who can't be vaccinated.")
    ]
}

L02 = {
    "id": "G07L2-L02",
    "title": "DNA Decoded: Why You Are (Mostly) Unique",
    "subtitle": "The Blueprint of Life and What Makes You, You",
    "ngss": "MS-LS3-1, MS-LS3-2",
    "ngss_desc": "Develop and use a model to describe why structural changes to genes (mutations) located on chromosomes may affect proteins and may result in harmful, beneficial, or neutral effects to the structure and function of the organism. Develop and use a model to describe why asexual reproduction results in offspring with identical genetic information and sexual reproduction results in offspring with genetic variation.",
    "big_question": "If you share 99.9% of your DNA with every other human, what makes you unique?",
    "objectives": [
        "Model how parent gene variation produces diverse offspring through sexual reproduction",
        "Explain how environmental conditions influence which genes are expressed",
        "Predict how trait variation affects survival advantage in different environments",
        "Describe the difference between genetic variation from sexual reproduction and identical copies from asexual reproduction"
    ],
    "vocabulary": [
        ("Gene Expression", "The process by which information from a gene is used to create a functional protein or trait in an organism"),
        ("Genetic Variation", "Differences in DNA sequences between individuals that lead to diversity in traits within a population"),
        ("Mutation", "A permanent change in the DNA sequence that may alter the protein a gene produces, potentially changing a trait"),
        ("Allele", "Different versions of the same gene that can produce different traits, like brown eyes vs. blue eyes")
    ],
    "components": [
        ("Parent Gene Variation", "The diversity of alleles and genetic material contributed by both parents", True),
        ("Environmental Conditions", "External factors like nutrition, climate, and lifestyle that affect gene expression", True),
        ("Gene Expression Level", "Which genes are actively being turned on or off in the organism's cells", False),
        ("Trait Variation in Offspring", "The visible and functional differences between siblings and within populations", False),
        ("Survival Advantage", "Whether an organism's particular combination of traits helps it survive in its current environment", False)
    ],
    "think_about_it": "If two siblings share the same parents, why don't they look identical? What role do environmental conditions play in making siblings different even beyond their genetic differences?",
    "scenarios": [
        ("High Genetic Diversity", "Set Parent Gene Variation to high and observe Trait Variation in Offspring"),
        ("Environmental Shift", "Keep genes constant but change Environmental Conditions and observe which traits become advantageous"),
        ("Low Variation Risk", "Set Parent Gene Variation to low (like asexual reproduction) and test against environmental change")
    ],
    "sim_scenarios": [
        ("High Parent Variation", "Diverse parent genes, stable environment", "What do you predict happens to Trait Variation in Offspring when parents have very different genetic backgrounds?"),
        ("Environment Changes", "Same genes, shifting environmental conditions", "What do you predict happens to Survival Advantage when the environment changes but genes stay the same?"),
        ("Low Variation (Asexual-like)", "Minimal parent variation, changing environment", "What do you predict happens to a population with almost no genetic variation when the environment changes?")
    ],
    "discoveries": [
        "Sexual reproduction creates unique combinations of parent genes, which is why siblings look different despite sharing parents",
        "Environmental conditions can turn genes on or off, meaning identical DNA can produce different traits in different environments",
        "Populations with more genetic variation are better equipped to survive environmental changes",
        "Asexual reproduction creates identical copies, which is efficient but dangerous if the environment changes"
    ],
    "answer": "Even though you share 99.9% of your DNA with every other human, the 0.1% that differs contains millions of genetic variations. Sexual reproduction shuffles parent genes into unique combinations. Then environmental conditions influence which genes are expressed. You are unique because of BOTH the genetic hand you were dealt AND the environment you grew up in!",
    "stem_title": "Design a Genetic Diversity Exhibit",
    "stem_mission": "Create an interactive exhibit demonstrating why genetic diversity is essential for species survival, using evidence from your simulation model.",
    "stem_scenario": "A science museum is opening a new genetics wing and needs an interactive exhibit that shows visitors why genetic diversity matters. Your team will design the exhibit using data from your model showing how variation affects survival.",
    "stem_questions": [
        "How can you visually demonstrate the difference between high and low genetic variation?",
        "What does your model data show about the survival risks of low genetic diversity?",
        "How can your exhibit make complex genetics concepts accessible to museum visitors?"
    ],
    "stem_design_qs": [
        "What interactive elements will help visitors understand gene expression?",
        "How will you show that environment influences which traits are advantageous?",
        "What model data will you display to prove genetic diversity matters?",
        "How will you represent the difference between sexual and asexual reproduction?"
    ],
    "career": "Genetic Counselors help individuals and families understand genetic conditions, inheritance patterns, and testing options. They work in hospitals, clinics, and research labs, earning $80,000-$120,000/year.",
    "images": {
        "cover": ("cover-dna-decoded.png", "A dramatic 3D visualization of a DNA double helix unraveling with colorful base pairs glowing, transitioning into diverse human silhouettes, deep blue and purple tones, cinematic science illustration"),
        "landscape": ("landscape-dna.png", "A group of 7th grade students in a genetics lab comparing trait surveys on clipboards, a White male student and a Black female student comparing eye color data while an Asian female student records results, modern science lab"),
        "modeling": ("modeling-dna.png", "A diverse group of 7th grade students building a digital genetics model on laptops, a Latino female student explaining DNA concepts to classmates, classroom with genetics and DNA posters on walls"),
        "discussion": ("discussion-dna.png", "A teacher using a 3D DNA model while leading discussion with 7th grade students, a White female student and an Asian male student examining the model closely, bright modern classroom"),
        "stem": ("stem-genetics-exhibit.png", "7th grade students designing an interactive genetics exhibit with colorful diagrams, a Black male student leading the design while a Latino male student and White female student contribute, collaborative teamwork")
    },
    "pre_assessment": [
        "Why do you think you look similar to your parents but not identical to either one?",
        "What do you know about DNA and what it does in your body?",
        "Draw what you think happens when traits from two parents combine in their offspring.",
        "Why do you think identical twins look the same but siblings do not?"
    ],
    "extend_components": [
        ("Mutation Rate", "The frequency at which random changes occur in DNA during cell division, creating new variations"),
        ("Epigenetic Factors", "Chemical modifications that change gene activity without altering the DNA sequence itself"),
        ("Sexual Selection", "When organisms choose mates based on certain traits, influencing which genes pass to the next generation")
    ],
    "reflections": [
        "Why is genetic variation important for a species' long-term survival?",
        "How does your model show the difference between sexual and asexual reproduction outcomes?",
        "What would happen to a population if all individuals had identical DNA and the environment suddenly changed?",
        "How do environmental conditions affect gene expression even when DNA stays the same?",
        "Why might a trait that is harmful in one environment be beneficial in another?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop and use a model to describe how genetic variation arises through sexual reproduction and how mutations affect organisms."),
        ("Disciplinary Core Idea", "LS3.A Inheritance of Traits / LS3.B Variation of Traits", "Genes are located on chromosomes. Variations of inherited traits can be explained by sexual reproduction and mutations."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify how parent gene variation and environmental conditions cause differences in trait expression and survival outcomes.")
    ],
    "cast_items": [
        "Model how sexual reproduction produces genetic variation in offspring",
        "Explain how mutations can result in harmful, beneficial, or neutral effects",
        "Describe the relationship between genetic variation and survival advantage"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A farmer plants a field with genetically identical crop plants. A new fungal disease arrives. What is the most likely outcome and why?"),
        ("Constructed Response:", "Using your genetics model, explain why sexual reproduction produces offspring with more genetic variation than asexual reproduction. Include how this variation affects a population's ability to survive environmental changes.")
    ],
    "background_intro": "DNA is the molecule that carries the instructions for building and maintaining every living organism. Understanding how genes are inherited, expressed, and varied is fundamental to explaining why organisms look and function the way they do.",
    "background_sections": [
        ("DNA and Genes", "DNA (deoxyribonucleic acid) is a double-helix molecule containing the instructions for building proteins. Genes are specific segments of DNA that code for particular traits. Humans have approximately 20,000 genes spread across 23 pairs of chromosomes."),
        ("Sexual vs. Asexual Reproduction", "In sexual reproduction, offspring receive half their DNA from each parent through meiosis, creating unique combinations every time. In asexual reproduction, a single parent produces genetically identical offspring. Sexual reproduction is slower but creates diversity; asexual is faster but creates clones."),
        ("Gene Expression and Environment", "Not all genes are active at all times. Environmental factors like nutrition, temperature, stress, and sunlight can turn genes on or off through a process called epigenetics. This means identical DNA can produce different results in different environments, which is why identical twins raised apart may develop differently."),
        ("Mutations: The Source of New Variation", "Mutations are permanent changes in DNA that occur during cell division. Most mutations are neutral (no effect), some are harmful (cause disease), and rarely, some are beneficial (improve survival). Over generations, beneficial mutations can spread through a population through natural selection.")
    ],
    "lever_L": "Students identify parent gene variation, environmental conditions, gene expression level, trait variation, and survival advantage as components of the genetic system.",
    "lever_E": "Students determine that parent gene variation drives trait diversity, while environmental conditions influence which traits are expressed and which provide survival advantages.",
    "lever_V": "Students build a model showing how genetic and environmental inputs interact to produce diverse organisms with varying survival prospects.",
    "lever_Ev": "Students run high variation, environmental shift, and low variation scenarios to observe how genetic diversity affects population resilience.",
    "lever_R": "Students add mutation rate or epigenetic factors to explore how new genetic variation arises and how gene expression can change without DNA changes.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with DNA helix imagery", "say": "You share 99.9% of your DNA with every person in this room. So what makes you, YOU?", "do": "Show a side-by-side of diverse students. Ask: What makes each person unique?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're decoding the blueprint of life to understand why you are mostly unique.", "do": "Have students read objectives. Pre-teach 'gene expression' and 'allele.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "What makes you unique if DNA is 99.9% the same?", "say": "That 0.1% difference? It contains MILLIONS of variations. Let's explore what they do.", "do": "Show a class trait survey (eye color, hair type, etc.). Discuss visible variation.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll build a model that shows how genes and environment interact to create YOU.", "do": "Preview LEVER steps. Connect to prior knowledge about inherited traits.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for genetics model", "say": "What inputs determine your traits? What can nature control vs. what responds automatically?", "do": "Guide sorting. Discuss why parent genes and environment are external inputs.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "When parent gene variation is high, what happens to offspring diversity? And how does environment change the picture?", "do": "Help students trace relationships. Discuss positive and negative connections.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's compare a population with high genetic diversity to one with almost none. What happens when the environment shifts?", "do": "Students predict first, then run simulations. Compare survival outcomes.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "Why is genetic diversity a species' insurance policy? What did our model reveal?", "do": "Lead discussion about diversity and survival. Connect to real examples.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Genetics exhibit design", "say": "You're now museum designers. Build an exhibit that shows why genetic diversity is essential.", "do": "Groups design interactive exhibits using model data.", "time": "12 min"}
    ],
    "sort_reasoning": "Parent Gene Variation and Environmental Conditions are external because they are inputs that determine what genetic material is available and what conditions organisms face. Gene Expression Level, Trait Variation in Offspring, and Survival Advantage are internal because they respond automatically to those genetic and environmental inputs.",
    "relationships": [
        ("Parent Gene Variation to Trait Variation in Offspring", "POSITIVE (+)", "When parents have more diverse alleles, their offspring have a wider range of possible trait combinations, increasing diversity in the population."),
        ("Environmental Conditions to Gene Expression Level", "POSITIVE/NEGATIVE (+/-)", "Environmental factors can turn genes on or off. Favorable conditions may activate growth genes while harsh conditions may activate stress-response genes."),
        ("Gene Expression Level to Trait Variation in Offspring", "POSITIVE (+)", "When more genes are actively expressed, there are more visible and functional trait differences among offspring."),
        ("Trait Variation in Offspring to Survival Advantage", "POSITIVE/NEGATIVE (+/-)", "Whether trait variation helps or hurts depends on the environment. In a changing environment, more variation means a better chance that some individuals have the right traits."),
        ("Environmental Conditions to Survival Advantage", "POSITIVE (+)", "Favorable environmental conditions improve survival for all organisms, regardless of their specific traits.")
    ],
    "sim_answers": [
        ("High Variation Scenario", "When Parent Gene Variation is high, Trait Variation in Offspring increases significantly. Gene Expression Level varies across individuals. When Environmental Conditions change, some offspring have traits that match the new conditions, giving them higher Survival Advantage. The population adapts and persists."),
        ("Low Variation (Asexual-like) Scenario", "When Parent Gene Variation is minimal, all offspring have nearly identical traits. Gene Expression Level is uniform. When Environmental Conditions shift, ALL individuals are equally vulnerable. Survival Advantage drops across the entire population because there's no diversity to select from. This is the danger of asexual reproduction in changing environments.")
    ],
    "reflection_exemplars": [
        ("Why don't siblings look identical?", "During sexual reproduction, each parent contributes a random half of their chromosomes through meiosis. The random assortment means each sibling gets a different combination of alleles. Additionally, crossing over during meiosis shuffles genes even further. With millions of possible combinations, the chance of two siblings being genetically identical (unless they're identical twins) is essentially zero."),
        ("Why might a harmful trait be beneficial in another environment?", "Sickle cell trait is harmful in its full form, causing sickle cell disease. But carrying just one copy of the sickle cell allele provides resistance to malaria. In regions where malaria is common, this 'harmful' gene actually provides a survival advantage. Whether a trait is helpful or harmful depends entirely on the environmental context.")
    ],
    "stem_intro": "A science museum is creating a new genetics wing and needs your team to design an interactive exhibit showing why genetic diversity matters for species survival. Use your simulation data to create evidence-based displays.",
    "stem_concepts": [
        ("Genetic Bottleneck", "When a population's size is drastically reduced (disease, natural disaster), genetic diversity drops dramatically. The surviving population may lack the variation needed to adapt to future challenges. Cheetahs experienced this and now have dangerously low genetic diversity."),
        ("Epigenetics", "Environmental factors can modify how genes are read without changing the DNA itself. These modifications can sometimes be passed to offspring, meaning a parent's environment can affect their children's gene expression."),
        ("CRISPR and Gene Editing", "Modern technology allows scientists to precisely edit DNA sequences. This raises important questions about modifying organisms, treating genetic diseases, and the ethics of changing the genetic code.")
    ],
    "stem_eval": [
        ("Expert (4)", "Exhibit accurately demonstrates sexual vs. asexual reproduction, uses model data to show survival outcomes, and includes interactive elements explaining gene expression and environmental influence"),
        ("Proficient (3)", "Exhibit shows how genetic variation affects survival and includes model data comparing different scenarios"),
        ("Developing (2)", "Exhibit mentions genetics but doesn't clearly connect genetic diversity to survival using model evidence"),
        ("Beginning (1)", "Exhibit is incomplete or contains misconceptions about how genetic variation works")
    ],
    "support": [
        "Provide trait cards showing different allele combinations for students to physically sort and combine",
        "Use coin flips to simulate random allele selection during reproduction",
        "Sentence frames: 'When parent gene variation is high, offspring are __ because __'"
    ],
    "extensions": [
        "Research the cheetah genetic bottleneck and explain why their lack of diversity threatens survival",
        "Investigate how identical twins raised in different environments develop differently (nature vs. nurture)",
        "Model how CRISPR gene editing could add new variations to a population and discuss the ethics"
    ],
    "cross_curr": [
        ("Math", "Calculate the probability of inheriting specific trait combinations using Punnett squares with two traits"),
        ("ELA", "Read and discuss a case study about genetic diversity in endangered species conservation"),
        ("Social Studies", "Research the ethical debates around genetic testing, gene editing, and genetic privacy")
    ],
    "misconceptions": [
        ("Traits are only from one parent", "Every trait is influenced by genes from BOTH parents. You receive one allele from your mother and one from your father for each gene. Which allele is expressed depends on dominance patterns and sometimes both alleles contribute (codominance).", "Use a color mixing analogy: Red paint from one parent + blue paint from the other = purple (blending). Or sometimes one color dominates."),
        ("DNA determines everything", "While DNA provides the blueprint, environmental conditions strongly influence which genes are expressed and how. Nutrition, stress, exercise, and exposure to chemicals can all change gene expression without changing the DNA itself. You are not ONLY your genes.", "Ask: If you planted identical seeds in rich soil vs. sandy soil, would the plants be identical? Same DNA, different environments, different outcomes."),
        ("Mutations are always bad", "Most mutations are neutral and have no effect. Some are harmful, causing diseases. But some mutations are beneficial, providing new traits that help organisms survive. All genetic diversity ultimately comes from mutations. Without them, evolution couldn't occur.", "Example: A mutation that causes darker fur might be bad in a snowy environment but great in a forest. Context matters.")
    ]
}

L03 = {
    "id": "G07L2-L03",
    "title": "Ocean Currents and Climate: The Conveyor Belt",
    "subtitle": "The Hidden Rivers That Control Our Weather",
    "ngss": "MS-ESS2-6, MS-ESS3-5",
    "ngss_desc": "Develop and use a model to describe how unequal heating and rotation of the Earth cause patterns of atmospheric and oceanic circulation that determine regional climates. Ask questions to clarify evidence of the factors that have caused the rise in global temperatures over the past century.",
    "big_question": "How do invisible rivers in the ocean control the weather thousands of miles away?",
    "objectives": [
        "Model how temperature differences between the equator and poles drive ocean circulation",
        "Explain how wind patterns and ocean currents work together to distribute heat globally",
        "Predict how disruptions to ocean currents could affect regional climate stability",
        "Describe why Europe is warmer than expected for its latitude due to ocean heat transport"
    ],
    "vocabulary": [
        ("Thermohaline Circulation", "The global ocean current system driven by differences in water temperature and salinity, often called the Great Ocean Conveyor Belt"),
        ("Heat Distribution", "The process by which thermal energy is spread from warmer regions to cooler regions through fluid movement"),
        ("Ocean Current", "A continuous, directed movement of ocean water generated by wind, temperature, salinity, and Earth's rotation"),
        ("Regional Climate", "The average weather conditions in a specific geographic area over long periods, influenced by nearby ocean currents")
    ],
    "components": [
        ("Temperature Difference (Equator vs Poles)", "The heat gradient between tropical and polar regions that drives circulation", True),
        ("Wind Patterns", "Surface winds that push ocean water and create surface currents", True),
        ("Ocean Current Speed", "How fast water circulates through the global conveyor belt system", False),
        ("Heat Distribution", "How evenly thermal energy is spread across the planet by ocean circulation", False),
        ("Regional Climate Stability", "How predictable and moderate weather patterns are in coastal areas", False)
    ],
    "think_about_it": "If ocean currents suddenly slowed down dramatically, what would happen to heat distribution between the equator and the poles? How would this affect weather in Europe?",
    "scenarios": [
        ("Normal Circulation", "Set Temperature Difference to moderate and Wind Patterns to normal and observe climate stability"),
        ("Enhanced Gradient", "Lock Temperature Difference to maximum and observe how current speed and heat distribution respond"),
        ("Disrupted Currents", "Reduce Temperature Difference (simulating ice melt) and observe what happens to regional climates")
    ],
    "sim_scenarios": [
        ("Normal Circulation", "Moderate temperature gradient, normal wind patterns", "What do you predict Heat Distribution looks like when currents are flowing normally?"),
        ("Enhanced Temperature Gradient", "Maximum difference between equator and poles", "What do you predict happens to Ocean Current Speed when the temperature difference increases?"),
        ("Ice Melt Disruption", "Reduced temperature gradient from polar ice melt", "What do you predict happens to Regional Climate Stability if ocean currents slow down significantly?")
    ],
    "discoveries": [
        "Ocean currents act as a global conveyor belt, carrying warm water toward the poles and cold water back toward the equator",
        "Wind patterns drive surface currents while temperature and salinity differences drive deep-water currents",
        "Europe is warmer than expected for its latitude because the Gulf Stream carries tropical heat northward",
        "If global warming disrupts the temperature gradient by melting polar ice, ocean currents could weaken, paradoxically making some regions colder"
    ],
    "answer": "Ocean currents are like invisible rivers flowing through the sea, driven by temperature differences and wind. The Great Ocean Conveyor Belt carries warm tropical water toward the poles and brings cold polar water back. This heat distribution is why Europe has mild winters and why disrupting these currents could cause dramatic climate shifts thousands of miles from where the disruption occurs!",
    "stem_title": "Design a Climate Impact Map",
    "stem_mission": "Create a visual map showing how ocean current disruption would affect climate in different regions around the world, using evidence from your simulation model.",
    "stem_scenario": "NOAA scientists are studying what would happen if the Atlantic Meridional Overturning Circulation (AMOC) weakened by 50%. They need your team to create a visual impact map showing which regions would be affected and how.",
    "stem_questions": [
        "Which regions depend most on ocean currents for their climate?",
        "How does your model data predict the cascade effects of current disruption?",
        "What evidence supports the claim that ocean currents affect weather thousands of miles away?"
    ],
    "stem_design_qs": [
        "How will you represent ocean current flow on your map?",
        "What color coding will show temperature changes in different regions?",
        "How will you visualize the before and after of current disruption?",
        "What model evidence will you cite to support your impact predictions?"
    ],
    "career": "Physical Oceanographers study ocean currents, waves, and water properties to understand how oceans affect climate and weather. They work for NOAA, universities, and environmental research institutes, earning $70,000-$130,000/year.",
    "images": {
        "cover": ("cover-ocean-currents.png", "A dramatic aerial view of ocean currents visualized as glowing blue and red streams flowing across a dark ocean, warm red currents moving north and cold blue currents moving south, cinematic satellite perspective"),
        "landscape": ("landscape-ocean.png", "A group of 7th grade students on a field trip at a coastal research station observing ocean monitoring equipment, an Asian male student and a White female student reading instruments while a Latino male student takes notes, sunny coastal setting"),
        "modeling": ("modeling-ocean.png", "A diverse group of 7th grade students working on laptops building a digital ocean circulation model, a Black female student and a White male student collaborating, classroom with ocean maps and current diagrams on walls"),
        "discussion": ("discussion-ocean.png", "A teacher using a globe and colored arrows to show ocean current patterns while 7th grade students ask questions, a Latino female student and an Asian female student pointing at the Gulf Stream, bright modern classroom"),
        "stem": ("stem-climate-map.png", "7th grade students creating a large climate impact map on poster board, a White male student drawing current patterns while a Black male student and Asian female student add temperature data, collaborative group work")
    },
    "pre_assessment": [
        "Do you think the ocean moves? If so, what makes it move?",
        "Why do you think some coastal cities have mild winters while inland cities at the same latitude have harsh ones?",
        "Draw what you think happens to warm water from the equator as it moves toward the poles.",
        "How do you think the ocean affects weather on land?"
    ],
    "extend_components": [
        ("Salinity Levels", "The salt concentration in ocean water, which affects water density and drives deep-water currents"),
        ("Coriolis Effect", "The deflection of moving water and air caused by Earth's rotation, which curves ocean currents"),
        ("Sea Surface Temperature", "The temperature of the ocean's surface layer, which affects evaporation and storm formation")
    ],
    "reflections": [
        "Why is England warmer than Labrador, Canada, even though they are at the same latitude?",
        "How does your model show that ocean currents are driven by temperature differences rather than just wind?",
        "What would happen to global climate if the Great Ocean Conveyor Belt completely stopped?",
        "How is the ocean current system an example of Earth's systems interacting with each other?",
        "Why could global warming paradoxically make some parts of Europe colder?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop and use a model to describe how unequal heating creates patterns of oceanic circulation that determine regional climates."),
        ("Disciplinary Core Idea", "ESS2.C The Roles of Water in Earth's Surface Processes / ESS3.D Global Climate Change", "Water's movements are driven by energy from the Sun and gravity, creating patterns that distribute heat and affect global climate."),
        ("Crosscutting Concept", "Energy and Matter", "Students trace the flow of thermal energy through the ocean current system, showing how energy transfer from equator to poles drives global climate patterns.")
    ],
    "cast_items": [
        "Model how temperature differences drive ocean circulation patterns",
        "Explain the relationship between ocean currents and regional climate stability",
        "Predict effects of ocean current disruption on global climate patterns"
    ],
    "cast_questions": [
        ("Multiple Choice:", "London, England, and Goose Bay, Canada, are at nearly the same latitude. Yet London's average winter temperature is about 10 degrees Celsius warmer. Which factor best explains this difference?"),
        ("Constructed Response:", "Using your ocean circulation model, explain how temperature differences between the equator and poles drive ocean currents and why disrupting these currents could change climate in regions far from where the disruption occurs.")
    ],
    "background_intro": "The ocean covers 71% of Earth's surface and plays a critical role in regulating global climate. Ocean currents act as a massive heat transport system, moving thermal energy from tropical regions toward the poles and influencing weather patterns across entire continents.",
    "background_sections": [
        ("The Great Ocean Conveyor Belt", "The thermohaline circulation is a global system of deep-water currents driven by differences in temperature and salinity. Warm, salty surface water flows poleward (like the Gulf Stream), cools, becomes denser, and sinks to the ocean floor. This cold, dense water then flows back toward the equator along the ocean bottom, creating a continuous loop that takes about 1,000 years to complete."),
        ("Surface Currents and Wind", "Surface currents are driven by wind patterns and the Coriolis Effect (Earth's rotation deflecting moving water). Trade winds push water westward near the equator, while prevailing westerlies push it eastward at mid-latitudes. These create circular current patterns called gyres that transport heat across ocean basins."),
        ("Ocean Currents and Climate", "The Gulf Stream carries an enormous amount of heat from the tropical Atlantic to northwestern Europe. Without it, England would have winters similar to Labrador, Canada. Coastal cities near warm currents have milder climates, while those near cold currents (like San Francisco's fog from the California Current) have cooler summers."),
        ("Climate Change and Current Disruption", "As global temperatures rise, polar ice melts and adds fresh water to the ocean. This reduces salinity, which could weaken the thermohaline circulation. Scientists monitoring the Atlantic Meridional Overturning Circulation (AMOC) have found it has slowed by about 15% since the mid-20th century, raising concerns about future climate disruption.")
    ],
    "lever_L": "Students identify temperature difference, wind patterns, ocean current speed, heat distribution, and regional climate stability as components of the ocean circulation system.",
    "lever_E": "Students determine that temperature differences drive current speed, which controls heat distribution, which in turn affects climate stability through cascading relationships.",
    "lever_V": "Students build a model showing how ocean circulation distributes thermal energy globally and stabilizes regional climates.",
    "lever_Ev": "Students run normal circulation, enhanced gradient, and disrupted current scenarios to compare climate outcomes across regions.",
    "lever_R": "Students add salinity levels or Coriolis Effect to explore how additional factors influence ocean current behavior.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with ocean current visualization", "say": "There are rivers in the ocean. You can't see them, but they control your weather.", "do": "Show a NASA animation of ocean current patterns if available.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're modeling the planet's hidden heating system: ocean currents.", "do": "Have students read objectives. Pre-teach 'thermohaline circulation.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How do invisible ocean rivers control weather?", "say": "London and northern Canada are at the same latitude. But London's winters are 10 degrees warmer. How?", "do": "Show a map comparing London and Goose Bay. Discuss latitude vs. climate.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll build a model of the ocean's heat delivery system.", "do": "Preview LEVER steps. Connect to what they know about hot and cold water.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for ocean circulation model", "say": "What drives ocean currents? What can we control in our model vs. what responds?", "do": "Guide sorting. Discuss why temperature difference and wind are external inputs.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "When the temperature difference between equator and poles gets bigger, what happens to current speed? And how does that affect climate?", "do": "Help students trace the cascade from temperature to currents to climate.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's see what happens when ocean currents are flowing normally vs. when they slow down.", "do": "Students predict first, then run simulations. Compare normal vs. disrupted scenarios.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "So WHY is Europe warmer than it should be? And what happens if we break the conveyor belt?", "do": "Lead discussion about Gulf Stream. Show AMOC slowdown data.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Climate impact map project", "say": "You're climate scientists now. Map what happens if ocean currents weaken by 50%.", "do": "Groups create impact maps using model evidence.", "time": "12 min"}
    ],
    "sort_reasoning": "Temperature Difference and Wind Patterns are external because they are the driving forces that students control in the model: the heat gradient between equator and poles and the wind pushing surface water. Ocean Current Speed, Heat Distribution, and Regional Climate Stability are internal because they respond automatically to changes in those driving forces.",
    "relationships": [
        ("Temperature Difference to Ocean Current Speed", "POSITIVE (+)", "A larger temperature gradient between the equator and poles creates a stronger density difference in ocean water, driving faster circulation through the conveyor belt."),
        ("Wind Patterns to Ocean Current Speed", "POSITIVE (+)", "Stronger surface winds push more water, increasing the speed of surface currents and contributing to overall ocean circulation."),
        ("Ocean Current Speed to Heat Distribution", "POSITIVE (+)", "Faster ocean currents transport more thermal energy from the tropics to the poles, creating more even heat distribution across the planet."),
        ("Heat Distribution to Regional Climate Stability", "POSITIVE (+)", "When heat is distributed more evenly, coastal regions experience more moderate temperatures and more predictable weather patterns."),
        ("Heat Distribution to Temperature Difference", "NEGATIVE (-)", "As currents distribute heat from equator to poles, they reduce the very temperature difference that drives them. This creates a self-regulating system.")
    ],
    "sim_answers": [
        ("Normal Circulation Scenario", "With moderate Temperature Difference and normal Wind Patterns, Ocean Current Speed is steady. Heat Distribution is even, carrying tropical warmth to higher latitudes. Regional Climate Stability is high, with coastal areas experiencing moderate temperatures. This is the current state of Earth's ocean system."),
        ("Disrupted Current Scenario", "When Temperature Difference is reduced (simulating ice melt diluting cold polar water), Ocean Current Speed drops. Heat Distribution becomes uneven, with tropical regions retaining heat while polar-adjacent regions lose their warm current input. Regional Climate Stability drops, and places like Western Europe could experience dramatically colder winters.")
    ],
    "reflection_exemplars": [
        ("Why is England warmer than Canada at the same latitude?", "The Gulf Stream is a powerful warm ocean current that carries tropical heat from the Caribbean across the Atlantic to northwestern Europe. This current delivers enormous amounts of thermal energy, warming the air above it and giving England much milder winters than Goose Bay, Canada, which sits at the same latitude but doesn't receive this ocean heat delivery."),
        ("Why could global warming make Europe colder?", "This seems contradictory but makes sense through the model. Global warming melts Arctic ice, adding fresh water that reduces ocean salinity. Less salty water is less dense, so it doesn't sink as effectively at the poles. This weakens the thermohaline circulation (conveyor belt), reducing the Gulf Stream's warm water delivery to Europe. So even as the globe warms overall, Europe could lose its warm current and experience much colder winters.")
    ],
    "stem_intro": "NOAA scientists are studying what would happen if the Atlantic Meridional Overturning Circulation weakened significantly. Your team will create a visual impact map showing which regions would be affected and how, based on your simulation model data.",
    "stem_concepts": [
        ("Gulf Stream Heat Transport", "The Gulf Stream moves about 30 million cubic meters of water per second and transports heat equivalent to about 1 petawatt (1 million gigawatts). This is 100 times the global electricity consumption. It is the reason Western Europe has a habitable climate."),
        ("AMOC Slowdown", "The Atlantic Meridional Overturning Circulation has weakened by approximately 15% since the mid-20th century. Some climate models predict it could weaken by 50% or more by 2100, which would dramatically alter European climate, Atlantic storm patterns, and global rainfall distribution."),
        ("Feedback Mechanisms", "The ocean-atmosphere system contains both positive and negative feedback loops. Warming reduces ice, which reduces the temperature gradient, which slows currents, which changes heat distribution. Understanding these feedbacks is essential for predicting future climate.")
    ],
    "stem_eval": [
        ("Expert (4)", "Impact map accurately shows current flow patterns, identifies vulnerable regions, uses model data for before/after comparison, and explains the cascade of effects with evidence"),
        ("Proficient (3)", "Map shows ocean current effects on climate and includes model evidence for how disruption changes regional temperatures"),
        ("Developing (2)", "Map shows ocean currents but doesn't clearly connect disruption to specific climate impacts using model data"),
        ("Beginning (1)", "Map is incomplete or doesn't accurately represent how ocean currents affect regional climate")
    ],
    "support": [
        "Provide a world map with major ocean currents pre-drawn for students to reference",
        "Use warm and cold colored water in a clear container to demonstrate density-driven circulation",
        "Sentence frames: 'When ocean current speed decreases, heat distribution __ because __, which causes regional climate to __'"
    ],
    "extensions": [
        "Research the AMOC slowdown and compare scientific predictions to your model's predictions",
        "Investigate El Nino and La Nina to see how Pacific current changes affect global weather",
        "Add salinity as a component and model how ice melt affects the thermohaline circulation"
    ],
    "cross_curr": [
        ("Math", "Calculate the heat energy transported by the Gulf Stream using flow rate and temperature data"),
        ("ELA", "Write a news article explaining how ocean current changes could affect your region's weather"),
        ("Social Studies", "Research how historic climate changes driven by ocean current shifts affected human civilizations")
    ],
    "misconceptions": [
        ("The ocean is still water", "The ocean is constantly in motion. Surface currents driven by wind can move water at speeds up to 5 mph, while deep-water thermohaline currents move more slowly but continuously. The Great Ocean Conveyor Belt circulates water through the entire global ocean over about 1,000 years.", "Demonstrate with food coloring in water: add a drop and watch it slowly spread and circulate. The ocean works the same way, just on a massive scale."),
        ("Ocean currents only affect coastal areas", "Ocean currents affect climate far inland by warming or cooling the air that blows over them. The Gulf Stream warms air masses that then blow across all of Western Europe, affecting temperatures hundreds of miles from the coast. Ocean currents also drive evaporation that creates rain patterns over entire continents.", "Ask: When you heat soup on the stove, does only the surface get warm? No, heat convection distributes warmth throughout. Ocean currents work similarly for the planet."),
        ("Climate and weather are the same", "Weather is what happens today or this week (sunny, rainy, cold snap). Climate is the average pattern over 30+ years. Ocean currents affect CLIMATE by consistently delivering heat to certain regions. A single cold day doesn't change the climate, but a persistent change in ocean currents would.", "Analogy: Your mood changes day to day (weather), but your personality is consistent over years (climate).")
    ]
}

L04 = {
    "id": "G07L2-L04",
    "title": "Newton's Laws: Why Things Move the Way They Do",
    "subtitle": "The Three Rules That Govern Every Motion in the Universe",
    "ngss": "MS-PS2-1, MS-PS2-2",
    "ngss_desc": "Apply Newton's Third Law to design a solution to a problem involving the motion of two colliding objects. Plan an investigation to provide evidence that the change in an object's motion depends on the sum of the forces acting on the object and the mass of the object.",
    "big_question": "Why does a bowling ball keep rolling while a tennis ball stops quickly, and why does pushing a shopping cart feel different when it's full vs. empty?",
    "objectives": [
        "Model how applied force, mass, and friction interact to determine an object's acceleration",
        "Explain why heavier objects require more force to achieve the same acceleration as lighter ones",
        "Predict how net force determines whether an object speeds up, slows down, or stays at rest",
        "Design investigations demonstrating that F = ma through controlled variable experiments"
    ],
    "vocabulary": [
        ("Net Force", "The total force acting on an object after all individual forces are added together, accounting for direction"),
        ("Acceleration", "The rate at which an object's speed or direction changes over time, measured in meters per second squared"),
        ("Friction", "A force that opposes motion between two surfaces in contact, converting kinetic energy to heat"),
        ("Inertia", "An object's resistance to changes in its motion, directly related to its mass")
    ],
    "components": [
        ("Applied Force", "The push or pull exerted on the object by an external source", True),
        ("Object Mass", "How much matter the object contains, determining its resistance to acceleration", True),
        ("Acceleration", "How quickly the object's speed changes in response to net force", False),
        ("Friction Force", "The resistance force from the surface that opposes the object's motion", False),
        ("Net Force", "The total unbalanced force remaining after friction is subtracted from applied force", False)
    ],
    "think_about_it": "If you push a heavy box with a certain force and friction removes some of that force, what determines how fast the box accelerates? What happens if you double the mass but keep the same push?",
    "scenarios": [
        ("Light Object + Big Push", "Set Applied Force to high and Object Mass to low and observe Acceleration"),
        ("Heavy Object + Same Push", "Keep Applied Force the same but increase Object Mass and compare Acceleration"),
        ("Adding Friction", "Set moderate force and mass, then increase friction and observe how Net Force and Acceleration change")
    ],
    "sim_scenarios": [
        ("Light + Strong Force", "High applied force, low mass, moderate friction", "What do you predict the Acceleration will be when you push a light object hard?"),
        ("Heavy + Same Force", "Same applied force, much higher mass, same friction", "What do you predict happens to Acceleration when you push a heavy object with the same force?"),
        ("High Friction", "Moderate force, moderate mass, high friction", "What do you predict happens to Net Force and Acceleration when friction is very high?")
    ],
    "discoveries": [
        "Acceleration depends on BOTH force AND mass: more force means more acceleration, but more mass means less acceleration (F = ma)",
        "Friction always opposes motion, reducing net force and therefore reducing acceleration",
        "Net force is what determines motion: an object only accelerates when forces are UNBALANCED",
        "A heavier object has more inertia, meaning it resists changes in motion more than a lighter object"
    ],
    "answer": "A bowling ball keeps rolling because its greater mass gives it more inertia, and a smooth lane has low friction. A tennis ball stops quickly because it's light (low inertia) and grass creates high friction. Pushing a full cart is harder because F = ma: the same force applied to more mass produces less acceleration. Newton's second law explains every motion you've ever seen!",
    "stem_title": "Design a Vehicle Safety Test",
    "stem_mission": "Design and conduct a vehicle safety test demonstrating how mass, force, and friction affect collision outcomes, applying Newton's Laws to real-world engineering.",
    "stem_scenario": "An automotive safety company needs to test how different vehicle masses and speeds affect collision impacts. Your team will design a scaled-down crash test using toy cars, ramps, and barriers to demonstrate Newton's Laws in action.",
    "stem_questions": [
        "How does doubling the mass of a vehicle change the force of impact in a collision?",
        "What role does friction play in stopping distance and collision severity?",
        "How can your model data inform real vehicle safety features?"
    ],
    "stem_design_qs": [
        "What variables will you test in your crash test (mass, speed, surface type)?",
        "How will you measure the force of impact in your scaled model?",
        "What safety features could reduce impact force based on Newton's Laws?",
        "How will you record and present your data as evidence?"
    ],
    "career": "Mechanical Engineers apply Newton's Laws to design machines, vehicles, and structures. They analyze forces, motion, and materials to create safe, efficient products, earning $75,000-$130,000/year.",
    "images": {
        "cover": ("cover-newtons-laws.png", "A dramatic freeze-frame action shot of a bowling ball mid-collision with pins, showing motion blur and force vectors, dynamic lighting against a dark background, cinematic sports physics"),
        "landscape": ("landscape-newton.png", "A group of 7th grade students in a physics lab conducting force experiments with spring scales and toy cars on tracks, a White male student and a Latino female student measuring force while a Black female student records data, bright modern lab"),
        "modeling": ("modeling-newton.png", "A diverse group of 7th grade students working on laptops building a digital force and motion model, an Asian male student explaining F=ma to classmates, classroom with Newton's Laws posters on walls"),
        "discussion": ("discussion-newton.png", "A teacher demonstrating forces using a cart and weights on a track while 7th grade students observe and predict, a Latino male student and a White female student making predictions, bright modern classroom"),
        "stem": ("stem-crash-test.png", "7th grade students conducting a crash test with toy cars and ramps, an Asian female student launching a car while a Black male student and White male student measure impact distance, hands-on engineering activity")
    },
    "pre_assessment": [
        "Why is it harder to push a full shopping cart than an empty one?",
        "What makes a moving ball eventually stop on a flat surface?",
        "Draw what you think happens to the speed of an object when you push it harder.",
        "If you push two objects with the same force, which moves faster: the heavy one or the light one? Why?"
    ],
    "extend_components": [
        ("Air Resistance", "The drag force exerted by air on a moving object, increasing with speed and surface area"),
        ("Gravitational Force", "The downward pull of gravity on all objects with mass, equal to mass times gravitational acceleration"),
        ("Momentum", "The quantity of motion an object has, calculated as mass times velocity, which is conserved in collisions")
    ],
    "reflections": [
        "How does your model demonstrate that F = ma? What evidence from the simulation proves this relationship?",
        "Why does a hockey puck slide so much farther on ice than a ball rolls on grass?",
        "What would motion look like in a world with zero friction?",
        "How do Newton's Laws explain why seatbelts save lives in car crashes?",
        "If two objects of different masses fall from the same height, why do they hit the ground at the same time (ignoring air resistance)?"
    ],
    "dimensions": [
        ("Science Practice", "Planning and Carrying Out Investigations", "Students plan investigations to provide evidence that an object's change in motion depends on the sum of forces and the mass of the object."),
        ("Disciplinary Core Idea", "PS2.A Forces and Motion", "The motion of an object is determined by the sum of the forces acting on it. If the total force is not zero, the object will change speed and/or direction."),
        ("Crosscutting Concept", "Stability and Change", "Students analyze how the balance of forces determines whether an object maintains its current motion or changes speed and direction.")
    ],
    "cast_items": [
        "Apply Newton's Second Law to predict motion outcomes given force and mass values",
        "Plan investigations that control variables to demonstrate force-mass-acceleration relationships",
        "Explain how friction affects net force and real-world motion"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Two identical forces are applied to two different objects. Object A has a mass of 2 kg and Object B has a mass of 8 kg. Which statement correctly compares their accelerations and why?"),
        ("Constructed Response:", "Using your force and motion model, explain why a loaded truck takes longer to stop than an empty car traveling at the same speed. Reference net force, mass, and friction in your explanation.")
    ],
    "background_intro": "Newton's Laws of Motion are the foundation of classical mechanics, explaining why objects move the way they do. From a rolling ball to a launching rocket, these three laws govern every motion in the universe at everyday speeds.",
    "background_sections": [
        ("Newton's First Law: Inertia", "An object at rest stays at rest, and an object in motion stays in motion at constant velocity, unless acted upon by an unbalanced force. This property of matter is called inertia. Mass is the measure of inertia: more mass means more resistance to changes in motion. A bowling ball has more inertia than a tennis ball."),
        ("Newton's Second Law: F = ma", "The acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass. Doubling the force doubles the acceleration. Doubling the mass halves the acceleration. This simple equation (F = ma) predicts the motion of everything from atoms to planets."),
        ("Newton's Third Law: Action-Reaction", "For every action force, there is an equal and opposite reaction force. When you push on a wall, the wall pushes back on you with equal force. When a rocket expels gas downward, the gas pushes the rocket upward. These paired forces act on DIFFERENT objects."),
        ("Friction: The Hidden Force", "Friction is a force that opposes the relative motion of two surfaces in contact. It converts kinetic energy to thermal energy (heat). Without friction, you couldn't walk, drive, or pick up objects. The amount of friction depends on the surfaces involved and the normal force pushing them together.")
    ],
    "lever_L": "Students identify applied force, object mass, acceleration, friction force, and net force as components of the motion system.",
    "lever_E": "Students determine that applied force increases net force (and thus acceleration) while friction and mass oppose it, creating a balance that determines motion.",
    "lever_V": "Students build a model showing how F = ma governs motion, with friction as a real-world complication that reduces net force.",
    "lever_Ev": "Students run light object, heavy object, and high friction scenarios to verify the F = ma relationship through different variable combinations.",
    "lever_R": "Students add air resistance or momentum to explore how additional forces affect motion in more realistic scenarios.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic motion imagery", "say": "Every time you throw a ball, ride a bike, or sit in a chair, you're experiencing Newton's Laws.", "do": "Drop a heavy and light object simultaneously. Ask: Which hits first?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're discovering the three rules that explain every motion in the universe.", "do": "Have students read objectives. Pre-teach 'net force' and 'acceleration.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why does a full cart push harder?", "say": "Push an empty cart. Easy. Now load it up. Much harder. Same push, different result. Why?", "do": "Demonstrate with classroom objects of different masses. Discuss observations.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll build a model that shows how force, mass, and friction determine ALL motion.", "do": "Preview LEVER steps. Connect to everyday motion experiences.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for motion model", "say": "What determines how fast something accelerates? What can we control vs. what responds?", "do": "Guide sorting. Discuss why applied force and mass are the inputs.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "When applied force goes up, what happens to net force and acceleration? But what does friction do?", "do": "Help students identify positive and negative relationships. Introduce F = ma.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's push a light object and a heavy object with the same force. Who predicts what happens?", "do": "Students predict first, then run all three scenarios. Graph and compare.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "So F = ma isn't just a formula. It EXPLAINS why pushing a full cart is harder. What else does it explain?", "do": "Lead discussion connecting model to real-world examples: cars, rockets, sports.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Vehicle crash test design", "say": "You're safety engineers now. Design a crash test that proves Newton's Laws save lives.", "do": "Groups design and conduct scaled crash tests with toy cars.", "time": "12 min"}
    ],
    "sort_reasoning": "Applied Force and Object Mass are external because they are inputs the student directly controls in the model: how hard you push and how heavy the object is. Acceleration, Friction Force, and Net Force are internal because they are determined automatically by the relationship between the inputs and the physical laws governing motion.",
    "relationships": [
        ("Applied Force to Net Force", "POSITIVE (+)", "Increasing the applied force directly increases the net force available to accelerate the object, assuming friction stays constant."),
        ("Friction Force to Net Force", "NEGATIVE (-)", "Friction opposes motion and subtracts from the applied force. Higher friction means less net force is available to accelerate the object."),
        ("Net Force to Acceleration", "POSITIVE (+)", "Newton's Second Law: acceleration is directly proportional to net force. More net force produces more acceleration (F = ma)."),
        ("Object Mass to Acceleration", "NEGATIVE (-)", "Newton's Second Law: acceleration is inversely proportional to mass. More mass means less acceleration for the same net force (a = F/m)."),
        ("Acceleration to Friction Force", "POSITIVE (+)", "As an object moves faster (higher acceleration leads to higher velocity), friction force increases because there is more relative motion between surfaces.")
    ],
    "sim_answers": [
        ("Light Object + Strong Force Scenario", "With high Applied Force and low Object Mass, Net Force is large (after subtracting moderate Friction). Acceleration is high because the same net force acts on a small mass. The light object speeds up rapidly, demonstrating F = ma with a small 'm'."),
        ("Heavy Object + Same Force Scenario", "With the SAME Applied Force but much higher Object Mass, Acceleration drops dramatically. Net Force is similar (same friction), but dividing by a larger mass (a = F/m) produces much less acceleration. This directly demonstrates why pushing a heavy object feels harder.")
    ],
    "reflection_exemplars": [
        ("Why does a hockey puck slide farther on ice?", "Friction is the key difference. Ice provides very low friction, so the puck loses very little kinetic energy as it slides. The net force opposing its motion is tiny, so it decelerates slowly. On grass, friction is much higher, so more of the ball's kinetic energy is converted to heat, and it decelerates rapidly. Newton's First Law says an object stays in motion unless an unbalanced force acts on it. Less friction means less unbalanced force means more sustained motion."),
        ("How do seatbelts save lives using Newton's Laws?", "Newton's First Law explains why passengers keep moving forward when a car stops suddenly. Your body has inertia and wants to continue at the car's speed. Without a seatbelt, you'd hit the dashboard or windshield at that speed. A seatbelt applies a stopping force over a longer time (Newton's Second Law), reducing the acceleration (deceleration) your body experiences. The force is spread across your chest and hips rather than concentrated on one point of impact.")
    ],
    "stem_intro": "An automotive safety company needs to test how mass, speed, and friction affect collision outcomes. Your team will design a scaled-down crash test using toy cars, ramps, and barriers to demonstrate Newton's Laws in action and propose safety improvements.",
    "stem_concepts": [
        ("Impulse and Impact", "Force multiplied by the time it acts equals impulse. In a crash, the same impulse can be delivered as a large force over a short time (rigid impact) or a smaller force over a longer time (crumple zone). Safety engineering extends impact time to reduce peak force."),
        ("Stopping Distance", "Stopping distance depends on speed squared divided by friction force and mass. Doubling speed quadruples stopping distance. This is why speed limits exist near schools and in residential areas."),
        ("Crumple Zones and Airbags", "Modern vehicles use crumple zones (front sections that collapse gradually) and airbags (cushions that extend impact time) to reduce the force experienced by passengers during collisions. Both apply Newton's Second Law to protect lives.")
    ],
    "stem_eval": [
        ("Expert (4)", "Crash test demonstrates clear F=ma relationships, tests multiple variables systematically, proposes evidence-based safety improvements, and accurately applies all three of Newton's Laws"),
        ("Proficient (3)", "Crash test shows how mass and force affect collision outcomes and references Newton's Laws"),
        ("Developing (2)", "Crash test measures some collision outcomes but doesn't clearly connect to Newton's Laws"),
        ("Beginning (1)", "Crash test is incomplete or doesn't demonstrate an understanding of force, mass, and acceleration relationships")
    ],
    "support": [
        "Provide spring scales for measuring force and toy cars of different masses for hands-on experimentation",
        "Use a ramp with a consistent slope as a controlled method for applying the same force to different masses",
        "Sentence frames: 'When I doubled the mass, the acceleration __ because F = ma tells us __'"
    ],
    "extensions": [
        "Calculate the force of impact for a car crash at different speeds using F = ma and stopping distance data",
        "Research how rocket propulsion works using Newton's Third Law and calculate thrust-to-weight ratios",
        "Add air resistance to the model and explore how it affects objects of different shapes"
    ],
    "cross_curr": [
        ("Math", "Use F = ma to calculate acceleration for different force and mass combinations, graphing the inverse relationship between mass and acceleration"),
        ("ELA", "Write a technical report explaining your crash test results using Newton's Laws, with data tables and graphs"),
        ("Physical Education", "Analyze the physics of a sport (football tackle, baseball pitch, soccer kick) using force, mass, and acceleration")
    ],
    "misconceptions": [
        ("Heavier objects fall faster", "In the absence of air resistance, ALL objects fall at the same rate regardless of mass. Galileo demonstrated this over 400 years ago. Air resistance affects light, large-surface-area objects more, which is why a feather falls slowly. In a vacuum, a feather and a bowling ball hit the ground at the same time.", "Show the NASA video of an astronaut dropping a hammer and feather on the Moon (no air). They hit at the same time."),
        ("An object needs constant force to keep moving", "Newton's First Law says an object in motion stays in motion WITHOUT any force, unless something (like friction) acts on it. On Earth, friction always acts, so we think things 'naturally' stop. But in space, objects drift forever without any force at all.", "Slide a book across a smooth table vs. a rough carpet. The book doesn't stop because it 'ran out of force.' It stops because friction is a force acting on it."),
        ("Action-reaction forces cancel out", "Newton's Third Law forces act on DIFFERENT objects, so they never cancel. When you push a wall, you push the wall forward and the wall pushes you backward. These forces are equal and opposite but act on different objects. Forces only cancel when they act on the SAME object.", "Push against a partner's hands. You both feel the force. If the forces cancelled, neither of you would feel anything.")
    ]
}

L05 = {
    "id": "G07L2-L05",
    "title": "Evolution in Action: How Species Change Over Time",
    "subtitle": "Why Biodiversity Is Nature's Insurance Policy",
    "ngss": "MS-LS4-1, MS-LS4-4",
    "ngss_desc": "Analyze and interpret data for patterns in the fossil record that document the existence, diversity, extinction, and change of life forms throughout the history of life on Earth. Construct an explanation based on evidence that describes how genetic variations of traits in a population increase some individuals' probability of surviving and reproducing in a specific environment.",
    "big_question": "How can a population of identical-looking organisms become two completely different species over time?",
    "objectives": [
        "Model how environmental change creates selection pressure that favors certain traits",
        "Explain why larger populations with more genetic variation adapt faster than small, uniform ones",
        "Predict extinction risk based on population size, genetic variation, and rate of environmental change",
        "Construct explanations for how natural selection drives adaptation over many generations"
    ],
    "vocabulary": [
        ("Natural Selection", "The process by which organisms with traits better suited to their environment survive and reproduce at higher rates, passing those traits to offspring"),
        ("Selection Pressure", "Any environmental factor that causes individuals with certain traits to survive and reproduce better than others"),
        ("Adaptation", "A trait that increases an organism's fitness in its specific environment, developed through natural selection over many generations"),
        ("Genetic Variation", "The range of different alleles and traits present within a population, providing the raw material for natural selection")
    ],
    "components": [
        ("Environmental Change Rate", "How quickly the habitat is changing in temperature, food availability, or other conditions", True),
        ("Population Size", "The total number of individuals in the population", True),
        ("Genetic Variation", "The diversity of traits and alleles present within the population", False),
        ("Selection Pressure", "How strongly the current environment favors certain traits over others", False),
        ("Adaptation Rate", "How quickly favorable traits spread through the population via reproduction", False)
    ],
    "think_about_it": "If a small population with low genetic variation faces rapid environmental change, what happens to its adaptation rate? Compare this to a large population with high variation. Why is biodiversity called 'nature's insurance policy'?",
    "scenarios": [
        ("Rapid Change + Small Population", "Set Environmental Change Rate to high and Population Size to low and observe Adaptation Rate"),
        ("Rapid Change + Large Population", "Keep Environmental Change Rate high but increase Population Size and compare outcomes"),
        ("Gradual Change", "Set Environmental Change Rate to low and observe how populations adapt over longer time periods")
    ],
    "sim_scenarios": [
        ("Rapid Change + Small Population", "Fast environmental shift, few individuals", "What do you predict happens to a small population's survival when the environment changes quickly?"),
        ("Rapid Change + Large Population", "Same fast change, many individuals", "What do you predict is different about a large population's response to the same rapid change?"),
        ("Gradual Change", "Slow environmental shift over many generations", "What do you predict happens to Adaptation Rate when the environment changes slowly enough for selection to keep up?")
    ],
    "discoveries": [
        "Natural selection can only work if there is genetic variation in the population. Without variation, there's nothing to select from",
        "Large populations have more genetic variation, giving them more options for adaptation when environments change",
        "When environmental change is faster than adaptation can keep up, extinction becomes likely, especially for small populations",
        "Adaptation rate increases when selection pressure is strong AND the population has sufficient genetic variation to respond"
    ],
    "answer": "Species change over time through natural selection. When the environment changes, individuals with traits better suited to the new conditions survive and reproduce more, passing those advantageous traits to their offspring. Over many generations, the population shifts. Large, genetically diverse populations adapt faster because they have more trait options to select from. This is why biodiversity is nature's insurance policy: the more variation in a population, the better its chances of surviving whatever the environment throws at it!",
    "stem_title": "Design a Conservation Strategy",
    "stem_mission": "Create an evidence-based conservation strategy for an endangered species, using your evolution model to explain why genetic diversity is critical for the species' survival.",
    "stem_scenario": "A wildlife conservation organization has asked your team to develop a rescue plan for an endangered species with a shrinking population. Using your model data, you need to explain why the population is at risk and propose strategies to increase their chances of survival.",
    "stem_questions": [
        "Why is a small, genetically uniform population at higher risk of extinction?",
        "What does your model data show about the relationship between population size and adaptation rate?",
        "How can conservation strategies increase genetic variation in threatened populations?"
    ],
    "stem_design_qs": [
        "Which endangered species will you focus on and what environmental pressures does it face?",
        "How will you use model evidence to justify your conservation recommendations?",
        "What specific strategies will increase population size and genetic diversity?",
        "How will you measure whether your conservation strategy is working?"
    ],
    "career": "Conservation Biologists study ecosystems and develop strategies to protect endangered species and habitats. They work for wildlife agencies, national parks, and environmental nonprofits, earning $55,000-$95,000/year.",
    "images": {
        "cover": ("cover-evolution-action.png", "A dramatic split image showing a group of identical organisms on one side gradually transitioning to diverse adapted forms on the other side, showing speciation over time, natural history illustration style"),
        "landscape": ("landscape-evolution.png", "A group of 7th grade students on a field trip in a natural history museum examining fossil displays, a Latino male student and a White female student reading fossil labels while an Asian male student sketches in a notebook, museum lighting"),
        "modeling": ("modeling-evolution.png", "A diverse group of 7th grade students working on laptops building an evolution simulation model, a Black female student pointing at population graphs while a White male student adjusts parameters, classroom with evolution and biodiversity posters"),
        "discussion": ("discussion-evolution.png", "A teacher showing images of Darwin's finches on a smartboard while leading discussion with 7th grade students, a White female student and a Latino male student debating adaptation examples, bright modern classroom"),
        "stem": ("stem-conservation.png", "7th grade students creating a conservation strategy poster with population data graphs, an Asian female student presenting data while a Black male student and Latino female student add habitat information, collaborative group work")
    },
    "pre_assessment": [
        "What do you think happens to a population of animals when their habitat suddenly changes?",
        "Why do you think there are so many different species of the same type of animal (like hundreds of beetle species)?",
        "Draw what you think happens to a population over many generations if only the fastest individuals survive.",
        "Why do you think some species go extinct while others survive the same environmental change?"
    ],
    "extend_components": [
        ("Geographic Isolation", "When a physical barrier separates a population into groups that can no longer interbreed, leading to independent evolution"),
        ("Mutation Rate", "The frequency of new genetic changes arising during reproduction, providing fresh raw material for natural selection"),
        ("Competition Intensity", "The degree to which organisms compete for limited resources, influencing which traits provide advantages")
    ],
    "reflections": [
        "Why can't individual organisms evolve? Why does evolution only happen at the population level?",
        "How does your model show that genetic variation is the raw material for natural selection?",
        "What would happen in your model if the environment changed so fast that no individuals had suitable traits?",
        "How does the fossil record provide evidence that species have changed over millions of years?",
        "Why is maintaining biodiversity important for the future of life on Earth?"
    ],
    "dimensions": [
        ("Science Practice", "Constructing Explanations", "Students construct explanations based on model evidence for how genetic variation and environmental change drive natural selection and adaptation."),
        ("Disciplinary Core Idea", "LS4.B Natural Selection / LS4.C Adaptation", "Natural selection leads to the predominance of certain traits in a population and the suppression of others based on environmental fitness."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify how environmental changes cause selection pressures that result in shifts in population trait frequencies over generations.")
    ],
    "cast_items": [
        "Analyze patterns in the fossil record showing species change over time",
        "Construct explanations for how genetic variation affects a population's probability of surviving environmental change",
        "Predict extinction risk based on population size, variation, and environmental change rate"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Two populations of the same species live in different environments. Population A is large with high genetic variation. Population B is small with low genetic variation. A disease outbreak affects both. Which population is more likely to survive and why?"),
        ("Constructed Response:", "Using evidence from your evolution model, explain how natural selection can lead to a population of organisms becoming better adapted to their environment over many generations. Include the roles of genetic variation, selection pressure, and reproduction in your explanation.")
    ],
    "background_intro": "Evolution by natural selection is the central organizing principle of biology. It explains how the incredible diversity of life on Earth arose from common ancestors over billions of years, driven by genetic variation, environmental change, and the differential survival and reproduction of organisms.",
    "background_sections": [
        ("Natural Selection Basics", "Charles Darwin proposed that organisms with traits better suited to their environment are more likely to survive and reproduce. Over many generations, favorable traits become more common in the population. This process requires three conditions: variation (differences exist), heritability (differences can be passed to offspring), and differential survival (some differences affect survival)."),
        ("The Role of Genetic Variation", "Natural selection can only act on traits that already exist in a population. Genetic variation comes from mutations, sexual reproduction (recombination), and gene flow between populations. Without variation, a population is like having only one answer to every question: if the question changes, you're stuck."),
        ("Adaptation and Speciation", "When populations of the same species are separated and face different environmental pressures, they accumulate different adaptations. Over thousands or millions of years, they may become so different that they can no longer interbreed: a new species has formed. Darwin's finches on the Galapagos Islands are a famous example."),
        ("Extinction and the Fossil Record", "The fossil record shows that over 99% of all species that ever lived are now extinct. Mass extinctions (like the one that killed the dinosaurs 66 million years ago) have periodically wiped out large portions of life, but surviving species diversified to fill empty ecological niches, leading to new waves of biodiversity.")
    ],
    "lever_L": "Students identify environmental change rate, population size, genetic variation, selection pressure, and adaptation rate as components of the evolutionary system.",
    "lever_E": "Students determine that environmental change drives selection pressure, population size determines genetic variation, and variation enables adaptation through interconnected relationships.",
    "lever_V": "Students build a model showing how population characteristics and environmental factors interact to determine whether a species adapts or goes extinct.",
    "lever_Ev": "Students run rapid change, large population, and gradual change scenarios to observe how population size and variation affect survival outcomes.",
    "lever_R": "Students add geographic isolation or mutation rate to explore how new species form and how fresh variation enters populations.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with evolution imagery", "say": "99% of all species that ever lived are extinct. The survivors had something the others didn't.", "do": "Show images of extinct and surviving species. Ask: What made the difference?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're modeling the most powerful force in biology: natural selection in action.", "do": "Have students read objectives. Pre-teach 'natural selection' and 'selection pressure.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How do species change over time?", "say": "How can one population split into two completely different species? It happens all the time.", "do": "Show Darwin's finch beak diversity. Discuss: same ancestor, different beaks. Why?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll build a model that shows evolution happening in real time.", "do": "Preview LEVER steps. Connect to prior knowledge about traits and inheritance.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for evolution model", "say": "What factors determine whether a species survives or goes extinct?", "do": "Guide sorting. Discuss why environment and population size are external inputs.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "When the environment changes fast, what happens to selection pressure? And how does population size affect adaptation?", "do": "Help students trace the cascade. Emphasize that variation is the key.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's compare: a small population vs. a large one, both facing the same environmental change. Who survives?", "do": "Students predict first, then run simulations. Discuss why size matters.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "Why is biodiversity nature's insurance policy? What did our model prove about variation and survival?", "do": "Lead discussion connecting model results to real endangered species.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Conservation strategy design", "say": "You're conservation biologists now. Design a rescue plan for an endangered species.", "do": "Groups develop conservation strategies using model evidence.", "time": "12 min"}
    ],
    "sort_reasoning": "Environmental Change Rate and Population Size are external because they are the driving conditions that students control in the model. Genetic Variation, Selection Pressure, and Adaptation Rate are internal because they respond to changes in those external inputs through natural processes that students observe.",
    "relationships": [
        ("Environmental Change Rate to Selection Pressure", "POSITIVE (+)", "Faster environmental change creates stronger selection pressure because the gap between current traits and optimal traits for the new environment widens."),
        ("Population Size to Genetic Variation", "POSITIVE (+)", "Larger populations contain more individuals, which means more genetic diversity through random mutations and recombination. More individuals = more trait options."),
        ("Genetic Variation to Adaptation Rate", "POSITIVE (+)", "Populations with more genetic variation have a wider range of traits to select from. When the environment changes, there's a higher probability that some individuals already have beneficial traits."),
        ("Selection Pressure to Adaptation Rate", "POSITIVE (+)", "Stronger selection pressure means a bigger survival advantage for individuals with favorable traits, causing those traits to spread faster through the population."),
        ("Adaptation Rate to Population Size", "POSITIVE (+)", "When a population adapts successfully, more individuals survive and reproduce, increasing population size. This creates a positive feedback loop with genetic variation.")
    ],
    "sim_answers": [
        ("Rapid Change + Small Population Scenario", "With high Environmental Change Rate and low Population Size, Selection Pressure is strong but Genetic Variation is low. The population has few trait options to select from, so Adaptation Rate is very slow. Many individuals die before adaptation can occur. The population shrinks further, reducing variation even more. This death spiral is why small, isolated populations face the highest extinction risk."),
        ("Rapid Change + Large Population Scenario", "With the same high Environmental Change Rate but a large Population Size, Genetic Variation is high. Even though Selection Pressure is equally strong, there are many trait options available. Some individuals already possess traits suited to the new conditions. Adaptation Rate is much faster because natural selection has raw material to work with. The population survives and may even grow as adapted individuals reproduce.")
    ],
    "reflection_exemplars": [
        ("Why can't individual organisms evolve?", "Evolution is a population-level process. An individual organism's DNA doesn't change during its lifetime (aside from mutations in body cells that aren't passed on). Evolution happens when the FREQUENCY of traits in a population changes over generations. Natural selection acts on individuals (some survive, some don't), but evolution is the result observed in the population over time."),
        ("Why is maintaining biodiversity important?", "Biodiversity is essentially a population's toolkit for survival. The more diverse the traits in an ecosystem, the more likely some organisms can handle whatever changes come. If a disease kills all organisms of one type, others fill the gap. If the climate shifts, some species are already adapted. Losing biodiversity is like throwing away tools from your toolbox: you might not need them today, but you will eventually.")
    ],
    "stem_intro": "A wildlife conservation organization needs your team to develop a rescue plan for an endangered species with a shrinking population. Use your model data to explain why the species is at risk and propose evidence-based strategies to improve its chances of survival.",
    "stem_concepts": [
        ("Minimum Viable Population", "The smallest population size at which a species can survive long-term without losing genetic diversity. Below this threshold, inbreeding reduces variation and health, creating a genetic death spiral. For many species, this number is several hundred to several thousand individuals."),
        ("Captive Breeding Programs", "Zoos and conservation centers maintain breeding populations of endangered species, carefully managing genetics to maximize diversity. Some species, like the California condor, have been saved from extinction through these programs."),
        ("Habitat Corridors", "Connected pathways between isolated habitat fragments that allow populations to exchange individuals and genes. Without corridors, populations become genetically isolated and lose variation over time.")
    ],
    "stem_eval": [
        ("Expert (4)", "Conservation strategy identifies specific threats, uses model data to explain extinction risk, proposes multiple evidence-based interventions, and includes genetic diversity management"),
        ("Proficient (3)", "Strategy explains why the species is at risk using model evidence and proposes at least two conservation interventions"),
        ("Developing (2)", "Strategy mentions population decline but doesn't clearly connect to genetic variation or use model evidence"),
        ("Beginning (1)", "Strategy is incomplete or doesn't demonstrate understanding of how population size and variation affect survival")
    ],
    "support": [
        "Provide trait cards that students can physically sort to simulate natural selection choosing from a pool of variation",
        "Use M&M color sorting: remove all of one color and show how population composition changes, simulating selection",
        "Sentence frames: 'When population size decreases, genetic variation __ because __, making adaptation __'"
    ],
    "extensions": [
        "Research the California condor recovery program and explain how captive breeding preserved genetic diversity",
        "Model how geographic isolation leads to speciation using the Galapagos finches as a case study",
        "Investigate antibiotic-resistant bacteria as a modern example of rapid evolution in action"
    ],
    "cross_curr": [
        ("Math", "Calculate how trait frequencies change over 10 generations under different selection pressures using a simulation spreadsheet"),
        ("ELA", "Write a persuasive conservation proposal for an endangered species, using model evidence to support each recommendation"),
        ("Social Studies", "Research how human activities (deforestation, pollution, urbanization) have accelerated extinction rates compared to natural background rates")
    ],
    "misconceptions": [
        ("Organisms evolve on purpose", "Evolution has no direction or goal. Organisms don't 'decide' to evolve or 'try' to develop new traits. Natural selection acts on RANDOM variation that already exists. Beneficial traits spread because their carriers survive more, not because organisms intended to change.", "Analogy: Shuffling a deck of cards doesn't aim for any particular order. But if you could only keep cards above 5, the deck would 'evolve' toward high cards. No intention required."),
        ("Evolution means improvement", "Evolution doesn't produce 'better' organisms in any absolute sense. It produces organisms better suited to their CURRENT environment. If the environment changes, previously beneficial traits might become harmful. Adaptations are context-dependent, not universally 'better.'", "Ask: Is thick fur 'better'? It is in the Arctic. It's terrible in the desert. Better is always relative to the environment."),
        ("Evolution is too slow to observe", "We can observe evolution happening in real time in organisms with short generation times. Bacteria evolving antibiotic resistance happens within days. Peppered moths changed color within decades during the Industrial Revolution. Evolution is happening right now, everywhere.", "Show examples: antibiotic-resistant bacteria, pesticide-resistant insects, dog breeds created by artificial selection in just a few hundred years.")
    ]
}

L06 = {
    "id": "G07L2-L06",
    "title": "Electromagnetic Spectrum: Beyond Visible Light",
    "subtitle": "The Invisible Waves That Run Your World",
    "ngss": "MS-PS4-2, MS-PS4-3",
    "ngss_desc": "Develop and use a model to describe that waves are reflected, absorbed, or transmitted through various materials. Integrate qualitative scientific and technical information to support the claim that digitized signals are a more reliable way to encode and transmit information than analog signals.",
    "big_question": "If visible light is just a tiny sliver of the electromagnetic spectrum, what else is out there that we can't see?",
    "objectives": [
        "Model the relationship between wave frequency, energy, and penetration depth across the electromagnetic spectrum",
        "Explain why different types of electromagnetic waves are used for different purposes based on their properties",
        "Predict how waves interact with different materials based on frequency and energy",
        "Describe how digital signals use electromagnetic waves to transmit information reliably"
    ],
    "vocabulary": [
        ("Electromagnetic Spectrum", "The complete range of electromagnetic waves organized by frequency, from low-energy radio waves to high-energy gamma rays"),
        ("Frequency", "The number of wave cycles that pass a point per second, measured in Hertz, directly related to the energy carried by the wave"),
        ("Wavelength", "The distance between consecutive wave peaks, inversely related to frequency: higher frequency means shorter wavelength"),
        ("Penetration Depth", "How far an electromagnetic wave can pass through a given material before being absorbed or reflected")
    ],
    "components": [
        ("Wave Frequency", "How fast the electromagnetic wave oscillates, determining its position on the spectrum", True),
        ("Wave Amplitude", "How strong or tall the wave is, related to the intensity of the signal", True),
        ("Wave Energy", "The amount of energy carried by the wave, determined by frequency and amplitude", False),
        ("Penetration Depth", "How far the wave passes through different types of matter", False),
        ("Detection Sensitivity", "Whether human senses or specific instruments can detect the wave", False)
    ],
    "think_about_it": "X-rays pass through your skin but are stopped by your bones, while radio waves pass through walls but can't penetrate metal. What property of these waves determines what they can and can't pass through?",
    "scenarios": [
        ("Radio Waves", "Set Wave Frequency to very low and observe Penetration Depth and Detection Sensitivity"),
        ("Visible Light", "Set Wave Frequency to the visible range and observe how detection changes"),
        ("X-rays", "Set Wave Frequency to very high and observe Wave Energy and Penetration Depth")
    ],
    "sim_scenarios": [
        ("Radio Frequency", "Very low frequency, moderate amplitude", "What do you predict about the energy and penetration depth of radio waves? Can your eyes detect them?"),
        ("Visible Light", "Mid-range frequency, moderate amplitude", "What is special about visible light's frequency range in terms of detection? Why can your eyes detect this range?"),
        ("X-ray Frequency", "Very high frequency, moderate amplitude", "What do you predict about X-ray energy? Why can X-rays pass through flesh but not bone?")
    ],
    "discoveries": [
        "Higher frequency electromagnetic waves carry more energy, which is why X-rays and gamma rays are dangerous while radio waves are harmless",
        "Visible light is just a tiny sliver of the electromagnetic spectrum that human eyes evolved to detect",
        "Different materials absorb, reflect, or transmit electromagnetic waves differently depending on the wave's frequency",
        "Digital signals encode information as discrete pulses of electromagnetic waves, making them more resistant to noise than analog signals"
    ],
    "answer": "Visible light is just one small part of a vast electromagnetic spectrum. Below visible light, there are infrared, microwaves, and radio waves with longer wavelengths and less energy. Above it, there are ultraviolet, X-rays, and gamma rays with shorter wavelengths and more energy. We use different parts of the spectrum for different purposes because each type of wave interacts with matter differently. Radio waves pass through walls (great for communication), X-rays pass through flesh but not bone (great for medicine), and visible light bounces off objects (great for seeing)!",
    "stem_title": "Design an EM Spectrum Technology Showcase",
    "stem_mission": "Create a showcase demonstrating how different parts of the electromagnetic spectrum are used in everyday technology, with evidence from your wave model explaining why each application works.",
    "stem_scenario": "A tech company wants to create an educational display showing customers how electromagnetic waves power their everyday devices: from WiFi to medical imaging to TV remotes. Your team will design the display using wave science to explain each technology.",
    "stem_questions": [
        "Why are different frequencies used for different technologies?",
        "How does your model explain why we use radio waves for communication but X-rays for medical imaging?",
        "What determines whether a wave can pass through a particular material?"
    ],
    "stem_design_qs": [
        "Which technologies will you feature and what EM spectrum region does each use?",
        "How will you visually represent the spectrum and each technology's place on it?",
        "What model data will you include to explain why each application uses its specific frequency?",
        "How will you explain digital vs. analog signal transmission to a non-technical audience?"
    ],
    "career": "Telecommunications Engineers design and maintain systems that transmit information using electromagnetic waves, including cell networks, satellite communications, and fiber optics, earning $80,000-$140,000/year.",
    "images": {
        "cover": ("cover-em-spectrum.png", "A dramatic visualization of the electromagnetic spectrum showing colorful waves transitioning from long red radio waves through visible light to short purple gamma rays, with real-world applications illustrated at each range, dark background with glowing waves"),
        "landscape": ("landscape-em.png", "A group of 7th grade students using prisms and diffraction gratings to split white light into its component colors in a darkened lab, a Black female student and a White male student observing the rainbow spectrum while a Latino male student records observations, dramatic light effects"),
        "modeling": ("modeling-em.png", "A diverse group of 7th grade students working on laptops building a digital wave model, an Asian female student adjusting frequency parameters while a White female student compares wave properties, classroom with electromagnetic spectrum poster on wall"),
        "discussion": ("discussion-em.png", "A teacher using a UV light and fluorescent materials to demonstrate invisible light while 7th grade students react with excitement, a Latino female student and a Black male student holding UV-reactive objects, bright modern classroom"),
        "stem": ("stem-em-showcase.png", "7th grade students building a technology showcase with labeled examples of EM spectrum applications, a White male student placing a model satellite while an Asian male student and Black female student label spectrum regions, collaborative group work")
    },
    "pre_assessment": [
        "What is light? Is it a particle, a wave, or something else?",
        "Can you name any types of waves or radiation besides visible light?",
        "Draw what you think happens when light hits a glass window vs. a brick wall.",
        "How do you think your phone receives text messages without a wire connecting it?"
    ],
    "extend_components": [
        ("Material Density", "How tightly packed the atoms are in the material the wave encounters, affecting absorption and transmission"),
        ("Signal Noise", "Random interference that degrades the quality of transmitted information, affecting both analog and digital signals"),
        ("Absorption Rate", "How much of the wave's energy is converted to heat or other forms when passing through a material")
    ],
    "reflections": [
        "Why is visible light the only part of the spectrum your eyes can detect? What evolutionary advantage might this provide?",
        "How does your model explain why sunscreen protects against UV radiation but not visible light?",
        "Why are digital signals more reliable than analog signals for transmitting information?",
        "What would the world look like if your eyes could see infrared or ultraviolet instead of visible light?",
        "How does the relationship between frequency and energy explain why gamma rays are dangerous but radio waves are not?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop and use a model to describe how electromagnetic waves of different frequencies interact with various materials differently."),
        ("Disciplinary Core Idea", "PS4.B Electromagnetic Radiation / PS4.C Information Technologies and Instrumentation", "Electromagnetic waves can be described by frequency and wavelength, and when they interact with matter, they may be absorbed, reflected, or transmitted."),
        ("Crosscutting Concept", "Structure and Function", "Students analyze how the structure of electromagnetic waves (frequency, wavelength, amplitude) determines their function and applications in technology.")
    ],
    "cast_items": [
        "Model how wave frequency determines energy and interaction with materials",
        "Explain why different EM spectrum regions are used for different technological applications",
        "Compare digital and analog signal transmission reliability"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A hospital uses X-rays to see inside a patient's body. Why do X-rays pass through soft tissue but are blocked by bones?"),
        ("Constructed Response:", "Using your electromagnetic spectrum model, explain why radio waves are used for WiFi communication while visible light is used for fiber optic cables. Include how frequency, energy, and material interaction determine each wave's best application.")
    ],
    "background_intro": "The electromagnetic spectrum encompasses all types of electromagnetic radiation, from the longest radio waves to the shortest gamma rays. Every part of the spectrum has unique properties that make it useful for specific applications in science, medicine, communication, and technology.",
    "background_sections": [
        ("The Electromagnetic Spectrum", "All electromagnetic waves travel at the speed of light (300,000 km/s) but differ in frequency and wavelength. From lowest to highest frequency: radio waves, microwaves, infrared, visible light, ultraviolet, X-rays, and gamma rays. The speed equation (speed = frequency x wavelength) means higher frequency waves have shorter wavelengths."),
        ("Wave-Matter Interactions", "When electromagnetic waves encounter matter, three things can happen: reflection (wave bounces off), absorption (wave's energy is converted to heat), or transmission (wave passes through). Which interaction occurs depends on the wave's frequency and the material's properties. X-rays pass through soft tissue (transmission) but are absorbed by dense bone."),
        ("Visible Light: Our Window to the World", "Human eyes detect electromagnetic waves between approximately 380 nm (violet) and 700 nm (red) wavelength. This tiny sliver of the spectrum is visible light. Our eyes evolved to detect this range because it matches the peak output of our Sun and passes through Earth's atmosphere. Other organisms detect different ranges: pit vipers see infrared, and bees see ultraviolet."),
        ("Digital vs. Analog Signals", "Analog signals vary continuously, like a smooth wave. Digital signals encode information as discrete pulses (1s and 0s). Digital signals are more reliable because any noise or distortion is easy to filter out: a pulse is either there or not. Analog signals degrade with distance because noise accumulates. This is why modern communication has shifted almost entirely to digital.")
    ],
    "lever_L": "Students identify wave frequency, wave amplitude, wave energy, penetration depth, and detection sensitivity as components of the electromagnetic wave system.",
    "lever_E": "Students determine that frequency drives energy, which drives penetration depth, while the combination of frequency and amplitude determines whether waves can be detected by specific sensors.",
    "lever_V": "Students build a model showing how electromagnetic wave properties determine their interaction with matter and their usefulness for specific applications.",
    "lever_Ev": "Students run radio wave, visible light, and X-ray scenarios to observe how frequency changes energy, penetration, and detection across the spectrum.",
    "lever_R": "Students add material density or signal noise to explore how wave-matter interactions and signal quality change across different conditions.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with EM spectrum visualization", "say": "Right now, invisible waves are passing through your body, through the walls, through everything. You just can't see them.", "do": "Turn on a radio. Ask: How does sound get from a radio station to this speaker without wires?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're exploring the invisible waves that run your entire world.", "do": "Have students read objectives. Pre-teach 'frequency' and 'wavelength.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "What can't we see?", "say": "Visible light is less than 1% of all electromagnetic waves. What's in the other 99%?", "do": "Show a full EM spectrum diagram. Point out how tiny the visible range is.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll build a model that lets us explore waves we can never see with our eyes.", "do": "Preview LEVER steps. Connect to everyday technologies that use invisible waves.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for wave model", "say": "What properties determine how a wave behaves? Which can we control?", "do": "Guide sorting. Discuss why frequency and amplitude are inputs we adjust.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "When frequency goes up, what happens to energy? And how does that change what the wave can pass through?", "do": "Help students trace frequency to energy to penetration. Discuss the pattern.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's explore three regions of the spectrum: radio, visible, and X-ray. What's different about each?", "do": "Students predict first, then run simulations across the spectrum.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "So why do we use radio waves for WiFi but X-rays for medicine? The model tells us exactly why.", "do": "Lead discussion connecting wave properties to real-world applications.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "EM technology showcase", "say": "You're tech educators now. Show people how invisible waves power their daily life.", "do": "Groups create technology showcases with spectrum labels and explanations.", "time": "12 min"}
    ],
    "sort_reasoning": "Wave Frequency and Wave Amplitude are external because they are properties the student directly controls in the model: how fast the wave oscillates and how strong the signal is. Wave Energy, Penetration Depth, and Detection Sensitivity are internal because they are determined by the frequency and amplitude inputs through physical laws.",
    "relationships": [
        ("Wave Frequency to Wave Energy", "POSITIVE (+)", "Higher frequency electromagnetic waves carry more energy per photon. This is why gamma rays (extremely high frequency) are dangerous while radio waves (extremely low frequency) are harmless."),
        ("Wave Amplitude to Wave Energy", "POSITIVE (+)", "Larger amplitude means a more intense wave carrying more total energy, regardless of frequency. A bright light has more amplitude than a dim light of the same color."),
        ("Wave Energy to Penetration Depth", "POSITIVE (+)", "Higher energy waves can penetrate deeper into materials. X-rays have enough energy to pass through soft tissue, while radio waves pass through walls. Very low energy waves may be stopped by thin barriers."),
        ("Wave Frequency to Detection Sensitivity", "POSITIVE/NEGATIVE (+/-)", "Human eyes detect only the visible frequency range. Below (infrared) and above (ultraviolet) this range, waves are invisible to us. Different instruments detect different frequency ranges."),
        ("Wave Amplitude to Detection Sensitivity", "POSITIVE (+)", "Stronger amplitude waves are easier to detect. A louder radio signal is clearer than a weak one. A brighter light is easier to see than a dim one.")
    ],
    "sim_answers": [
        ("Radio Wave Scenario", "At very low Wave Frequency, Wave Energy is low. Penetration Depth is moderate: radio waves pass through walls, clothing, and bodies easily because they lack the energy to interact strongly with these materials. Detection Sensitivity for human senses is zero, as eyes cannot detect radio frequencies. Special antennas are needed."),
        ("X-ray Scenario", "At very high Wave Frequency, Wave Energy is high. Penetration Depth varies by material: X-rays pass through soft tissue (low density) but are absorbed by bone and metal (high density). This differential penetration is what creates X-ray images. Detection Sensitivity again requires instruments, as X-rays are invisible to the human eye, but their effects on photographic film reveal the image.")
    ],
    "reflection_exemplars": [
        ("Why can our eyes only see visible light?", "Our eyes evolved to detect the range of electromagnetic frequencies that (1) are most abundantly produced by our Sun and (2) pass through Earth's atmosphere to reach the surface. It would be wasteful to develop receptors for frequencies that never reach us. The visible range happens to be the 'window' in Earth's atmosphere where electromagnetic radiation passes through most efficiently."),
        ("Why are digital signals more reliable?", "Analog signals degrade continuously as they travel. Any noise (electromagnetic interference, electrical fluctuations) permanently distorts the signal. Digital signals encode information as 1s and 0s: discrete on/off pulses. Even if noise slightly distorts a pulse, the receiver can still tell if it was meant to be a 1 or 0. Digital signals can also be perfectly regenerated (copied) without losing quality, while analog copies always degrade.")
    ],
    "stem_intro": "A tech company wants to create an educational display showing how electromagnetic waves power everyday devices. Your team will design the display, using wave science from your model to explain why each technology uses its specific part of the spectrum.",
    "stem_concepts": [
        ("Antenna Design", "Radio antennas are designed to match the wavelength of the signal they receive. A FM radio antenna is about 1.5 meters long because FM radio wavelengths are about 3 meters. Cell phone antennas are tiny because cell signals have much shorter wavelengths."),
        ("Medical Imaging", "Different medical imaging technologies use different parts of the EM spectrum. X-rays show bone structure. MRI uses radio waves and magnetic fields to image soft tissue. CT scans use X-rays from multiple angles to create 3D images. Each leverages specific wave-matter interactions."),
        ("Fiber Optics", "Fiber optic cables transmit information as pulses of visible or near-infrared light through glass fibers. Light bounces off the walls of the fiber (total internal reflection) and can travel thousands of miles. Fiber optics carry data faster than radio waves because visible light has a much higher frequency, allowing more data per second.")
    ],
    "stem_eval": [
        ("Expert (4)", "Showcase accurately maps technologies to spectrum regions, explains WHY each frequency is used with model evidence, and includes digital vs. analog signal comparison"),
        ("Proficient (3)", "Showcase identifies correct spectrum regions for technologies and explains wave property differences"),
        ("Developing (2)", "Showcase lists technologies but doesn't clearly connect them to wave properties or model data"),
        ("Beginning (1)", "Showcase is incomplete or incorrectly places technologies on the electromagnetic spectrum")
    ],
    "support": [
        "Provide a large printed electromagnetic spectrum with common technologies labeled at each region",
        "Use a prism to physically demonstrate that white light contains multiple frequencies (colors)",
        "Sentence frames: 'This technology uses __ waves because their frequency is __ enough to __'"
    ],
    "extensions": [
        "Research how infrared cameras work and why they're used for night vision and thermal imaging",
        "Investigate the ozone layer and explain how it protects life by absorbing UV radiation",
        "Compare the data capacity of radio waves vs. visible light in fiber optics and calculate the difference"
    ],
    "cross_curr": [
        ("Math", "Calculate wavelength from frequency using the wave equation (speed = frequency x wavelength) for different EM regions"),
        ("ELA", "Write a technical explanation of how WiFi works, from router to device, explaining each step in terms of electromagnetic waves"),
        ("Art", "Create an infographic showing the electromagnetic spectrum with real-world applications illustrated at each frequency range")
    ],
    "misconceptions": [
        ("Light and radio waves are completely different things", "Light and radio waves are both electromagnetic waves. They differ only in frequency and wavelength. All electromagnetic waves travel at the same speed (speed of light) and are produced by the same fundamental mechanism: accelerating electric charges.", "Show the EM spectrum as a continuous range. Visible light is just one section. Radio, X-rays, and gamma rays are all the same TYPE of wave at different frequencies."),
        ("Higher frequency waves are always dangerous", "Whether an electromagnetic wave is dangerous depends on its energy AND intensity. A single X-ray photon has more energy than a radio photon, but a very weak X-ray beam is less dangerous than an extremely intense radio beam. Medical X-rays use very low intensity for very short exposure, making them safe.", "Analogy: A single drop of hot water won't hurt you (high energy, low amount). A bathtub of warm water could cause problems if you stayed too long (lower energy, huge amount)."),
        ("Walls block all electromagnetic waves", "Different materials block different frequencies. Walls block visible light but radio waves pass right through (that's how WiFi works). Metal blocks radio waves (that's why you lose signal in elevators). Glass transmits visible light but blocks UV. No single material blocks ALL electromagnetic waves.", "Turn on WiFi in a room with closed doors and walls. It still works because radio waves pass through. But visible light from the hallway is blocked by the same walls.")
    ]
}

L07 = {
    "id": "G07L2-L07",
    "title": "Rock Cycle Deep Dive: From Magma to Mountain",
    "subtitle": "How Earth Recycles Itself Over Millions of Years",
    "ngss": "MS-ESS2-1, MS-ESS1-4",
    "ngss_desc": "Develop a model to describe the cycling of Earth's materials and the flow of energy that drives this process. Construct a scientific explanation based on evidence from rock strata for how the geologic time scale is used to organize Earth's 4.6-billion-year-old history.",
    "big_question": "If Earth is 4.6 billion years old, why aren't all rocks ancient? How does Earth constantly create, destroy, and recreate rocks?",
    "objectives": [
        "Model how heat, pressure, and weathering drive the continuous transformation of rock types",
        "Explain how the three rock types (igneous, sedimentary, metamorphic) are connected through the rock cycle",
        "Predict which rock type dominates under different geological conditions",
        "Describe how rock strata and the rock cycle help scientists organize Earth's geologic history"
    ],
    "vocabulary": [
        ("Igneous Rock", "Rock formed from the cooling and solidification of magma or lava, either below or above Earth's surface"),
        ("Sedimentary Rock", "Rock formed from compressed and cemented layers of sediment, often containing fossils"),
        ("Metamorphic Rock", "Rock that has been transformed by extreme heat and pressure without melting, changing its mineral structure"),
        ("Weathering", "The breaking down of rocks by physical, chemical, or biological processes at Earth's surface")
    ],
    "components": [
        ("Heat & Pressure (Depth)", "The intensity of thermal and compressive conditions deep underground", True),
        ("Weathering Rate", "How rapidly rocks are broken down by physical, chemical, and biological processes at the surface", True),
        ("Igneous Rock Formation", "The rate at which magma cools and solidifies into new igneous rock", False),
        ("Sedimentary Layers", "The accumulation of eroded rock fragments that compact into sedimentary rock over time", False),
        ("Metamorphic Transformation", "The rate at which existing rocks are changed by heat and pressure into metamorphic rock", False)
    ],
    "think_about_it": "If weathering breaks down rocks at the surface and heat/pressure transform rocks deep underground, what prevents Earth from running out of any one rock type? How does the cycle keep all three types in existence?",
    "scenarios": [
        ("Deep Underground", "Set Heat & Pressure to high and Weathering Rate to low and observe which rock types form"),
        ("Surface Erosion", "Set Weathering Rate to high and Heat & Pressure to low and observe sedimentary layer buildup"),
        ("Balanced Cycle", "Set both inputs to moderate and observe how all three rock types are maintained simultaneously")
    ],
    "sim_scenarios": [
        ("High Heat & Pressure", "Intense conditions deep underground, minimal surface erosion", "What do you predict happens to Metamorphic Transformation and Igneous Rock Formation when conditions are extremely hot and pressurized?"),
        ("High Weathering", "Rapid surface erosion, minimal underground heat", "What do you predict happens to Sedimentary Layers when weathering breaks down surface rocks rapidly?"),
        ("Balanced Conditions", "Moderate heat/pressure AND moderate weathering", "What do you predict the balance between all three rock types looks like when both processes are active?")
    ],
    "discoveries": [
        "The rock cycle has no beginning or end: any rock type can become any other rock type given the right conditions",
        "Heat and pressure deep underground create igneous and metamorphic rocks, while weathering at the surface creates sedimentary rocks",
        "The rock cycle is driven by Earth's internal heat (radioactive decay and leftover formation heat) and external energy (the Sun, which drives weathering)",
        "Sedimentary rock layers contain fossils and provide a timeline of Earth's history, which is how scientists organize the geologic time scale"
    ],
    "answer": "Earth constantly recycles its rocks through the rock cycle. Surface rocks are broken down by weathering into sediment, which gets buried and compressed into sedimentary rock. If buried deep enough, heat and pressure transform it into metamorphic rock. If it melts completely, the magma cools into igneous rock. And any of these rocks can be uplifted to the surface and weathered again. Earth has been recycling its materials for 4.6 billion years, which is why not all rocks are ancient. The planet is constantly destroying and recreating itself!",
    "stem_title": "Build a Geologic History Timeline",
    "stem_mission": "Create a geologic history timeline showing how the rock cycle has shaped Earth's surface over billions of years, using rock strata evidence and your simulation model data.",
    "stem_scenario": "A geology museum is developing a new exhibit on Earth's 4.6-billion-year history. They need your team to create a visual timeline showing how the rock cycle has continuously reshaped the planet, using rock strata as evidence for major geologic events.",
    "stem_questions": [
        "How do rock layers tell the story of Earth's past?",
        "What does your model reveal about which conditions produce which rock types?",
        "How can you represent 4.6 billion years of rock cycling in an engaging exhibit?"
    ],
    "stem_design_qs": [
        "What major geologic events will you include in your timeline?",
        "How will you show the relationship between the rock cycle and the geologic time scale?",
        "What model data will you use to explain how different conditions create different rocks?",
        "How will you make 4.6 billion years of history accessible and engaging for museum visitors?"
    ],
    "career": "Geologists study Earth's materials, processes, and history. They work in natural resource exploration, environmental consulting, hazard assessment, and academic research, earning $65,000-$120,000/year.",
    "images": {
        "cover": ("cover-rock-cycle.png", "A dramatic cross-section of Earth showing the rock cycle in action, with magma rising from below, metamorphic zones of intense pressure, sedimentary layers on the surface, and weathering creating sediment, cinematic geological illustration"),
        "landscape": ("landscape-rocks.png", "A group of 7th grade students on a geology field trip examining exposed rock layers in a canyon wall, a White female student and a Black male student using hand lenses to examine rock samples while a Latino female student sketches the rock layers, sunny outdoor setting"),
        "modeling": ("modeling-rocks.png", "A diverse group of 7th grade students working on laptops building a digital rock cycle model, an Asian male student and a White male student comparing rock formation data on screens, classroom with rock samples and geological maps on display"),
        "discussion": ("discussion-rocks.png", "A teacher holding rock samples (granite, sandstone, marble) while leading discussion with 7th grade students, a Black female student examining a metamorphic rock while a Latino male student and Asian female student compare samples, bright modern classroom"),
        "stem": ("stem-geology-timeline.png", "7th grade students creating a large geologic timeline poster with rock samples attached, a White male student labeling eras while a Black female student and Asian male student arrange rock type examples along the timeline, collaborative group work")
    },
    "pre_assessment": [
        "Where do you think rocks come from? Are they all the same?",
        "What do you think happens to a rock if it gets buried really deep underground for millions of years?",
        "Draw what you think happens when a volcano erupts and lava flows onto the surface.",
        "How do you think scientists figure out which rocks are older and which are younger?"
    ],
    "extend_components": [
        ("Tectonic Plate Movement", "The motion of Earth's crustal plates that subducts rock into the mantle and uplifts it to the surface"),
        ("Erosion Transport Distance", "How far weathered sediment travels from its source before being deposited and compacted"),
        ("Fossil Preservation", "The likelihood that organisms become fossilized during sedimentary rock formation, dependent on burial speed and conditions")
    ],
    "reflections": [
        "Why is the rock cycle called a 'cycle' rather than a 'chain'? How does your model demonstrate this?",
        "How does the rock cycle explain why we find marine fossils on mountain tops?",
        "What would happen to the rock cycle if Earth's internal heat completely died out?",
        "Why are sedimentary rocks the most important for understanding Earth's biological history?",
        "How does your model show that the rock cycle is driven by BOTH internal and external energy sources?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model to describe the cycling of Earth's materials through igneous, sedimentary, and metamorphic rock formation."),
        ("Disciplinary Core Idea", "ESS2.A Earth's Materials and Systems / ESS1.C The History of Planet Earth", "All Earth processes are the result of energy flowing and matter cycling. Rock strata provide evidence for the geologic time scale."),
        ("Crosscutting Concept", "Energy and Matter", "Students trace the flow of energy (internal heat, solar) that drives matter cycling through the rock cycle, showing how energy inputs determine which transformations occur.")
    ],
    "cast_items": [
        "Model how energy flow drives the cycling of Earth's materials through three rock types",
        "Explain how heat, pressure, and weathering transform rocks from one type to another",
        "Use rock strata evidence to describe how the geologic time scale organizes Earth's history"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A geologist finds a rock that was once sandstone (sedimentary) but now has a crystalline structure with folded layers. Which process most likely caused this transformation and what type of rock is it now?"),
        ("Constructed Response:", "Using your rock cycle model, explain how a single piece of granite (igneous rock) could eventually become sandstone (sedimentary rock) and then marble (metamorphic rock). Describe the specific processes and conditions required at each step.")
    ],
    "background_intro": "The rock cycle is Earth's grand recycling system. Over billions of years, the planet has continuously created, destroyed, and recreated rocks through processes driven by internal heat and external energy from the Sun. Understanding the rock cycle explains how Earth's surface has changed over its 4.6-billion-year history.",
    "background_sections": [
        ("Three Rock Types", "Igneous rocks form when magma (underground) or lava (surface) cools and solidifies. Granite forms slowly underground (large crystals); basalt forms quickly on the surface (small crystals). Sedimentary rocks form when weathered fragments are deposited, compacted, and cemented. Sandstone, limestone, and shale are common examples. Metamorphic rocks form when existing rocks are transformed by intense heat and pressure without melting. Marble comes from limestone; slate comes from shale."),
        ("The Cycling Process", "The rock cycle has no starting point. Igneous rock at the surface weathers into sediment, which becomes sedimentary rock. If buried deep, sedimentary rock becomes metamorphic. If heated further, it melts into magma, which cools into new igneous rock. But shortcuts exist: igneous rock can become metamorphic directly, or metamorphic rock can weather directly into sediment."),
        ("Energy Driving the Cycle", "Two energy sources power the rock cycle. Earth's internal heat (from radioactive decay and residual formation heat) drives melting, metamorphism, and plate tectonics. The Sun's energy drives weathering and erosion by powering wind, water cycles, and temperature changes. Without both energy sources, the rock cycle would stop."),
        ("Rock Strata and Geologic Time", "Sedimentary rock layers (strata) are deposited in sequence, with older layers on the bottom and younger layers on top (Law of Superposition). Fossils in these layers record the history of life. By studying rock strata, scientists have organized Earth's 4.6-billion-year history into eons, eras, periods, and epochs, creating the geologic time scale.")
    ],
    "lever_L": "Students identify heat and pressure, weathering rate, igneous rock formation, sedimentary layers, and metamorphic transformation as components of the rock cycle system.",
    "lever_E": "Students determine that heat/pressure drives metamorphic and igneous formation while weathering drives sedimentary formation, with the cycle connecting all three types.",
    "lever_V": "Students build a model showing how the rock cycle continuously transforms Earth's materials based on conditions at different depths.",
    "lever_Ev": "Students run deep underground, surface erosion, and balanced scenarios to observe how different conditions favor different rock types.",
    "lever_R": "Students add tectonic plate movement or fossil preservation to explore how plate tectonics connects the deep and surface rock processes.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic rock cycle cross-section", "say": "Pick up any rock. It might be older than the dinosaurs. Or it might have been magma last year. How can you tell?", "do": "Pass around three rock samples (granite, sandstone, marble). Ask: What's different about these?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're diving deep into how Earth recycles itself over billions of years.", "do": "Have students read objectives. Pre-teach 'igneous,' 'sedimentary,' and 'metamorphic.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why aren't all rocks ancient?", "say": "Earth is 4.6 billion years old. But some rocks formed last week from volcanic eruptions. How is the planet constantly making new rocks?", "do": "Show before/after images of volcanic eruptions creating new land. Discuss.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll build a model of Earth's rock recycling system.", "do": "Preview LEVER steps. Show rock cycle diagram for reference.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for rock cycle model", "say": "What forces shape rocks? What can we control in our model vs. what responds?", "do": "Guide sorting. Discuss why heat/pressure and weathering are external driving forces.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "When heat and pressure increase, which rock types form? When weathering increases, what builds up?", "do": "Help students trace connections. Emphasize that the cycle has NO starting point.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's crank up the heat underground and see what happens. Then let's crank up weathering on the surface.", "do": "Students predict first, then run all three scenarios. Compare which rock types dominate.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "So WHY is the rock cycle a cycle and not a chain? What did our model prove about Earth's recycling?", "do": "Lead discussion about how the cycle maintains all three rock types. Connect to geologic time.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Geologic timeline project", "say": "You're geologists now. Tell the story of 4.6 billion years using rocks as your evidence.", "do": "Groups create geologic timelines with rock type examples at key events.", "time": "12 min"}
    ],
    "sort_reasoning": "Heat & Pressure and Weathering Rate are external because they are the driving forces that students control in the model: the intensity of underground conditions and the rate of surface erosion. Igneous Rock Formation, Sedimentary Layers, and Metamorphic Transformation are internal because they are the resulting rock-forming processes that respond to those driving forces.",
    "relationships": [
        ("Heat & Pressure to Metamorphic Transformation", "POSITIVE (+)", "Greater heat and pressure deep underground cause more rock to undergo metamorphic transformation, changing its mineral structure without melting it."),
        ("Heat & Pressure to Igneous Rock Formation", "POSITIVE (+)", "Extreme heat melts rock into magma. When magma cools (either underground or at the surface), it solidifies into igneous rock."),
        ("Weathering Rate to Sedimentary Layers", "POSITIVE (+)", "Faster weathering breaks down more surface rock into sediment. This sediment is transported, deposited, and compressed into sedimentary rock layers."),
        ("Sedimentary Layers to Metamorphic Transformation", "POSITIVE (+)", "As sedimentary layers accumulate, the weight of upper layers creates pressure on deeper layers. If buried deep enough, this pressure (combined with heat) triggers metamorphic transformation."),
        ("Weathering Rate to Igneous Rock Formation", "NEGATIVE (-)", "High weathering erodes and breaks down exposed igneous rock at the surface, reducing the amount of intact igneous rock and converting it to sediment.")
    ],
    "sim_answers": [
        ("Deep Underground Scenario", "With high Heat & Pressure and low Weathering Rate, Metamorphic Transformation and Igneous Rock Formation dominate. Rocks deep underground are being transformed by heat and pressure into metamorphic rock, and the most extreme conditions melt rock into magma that cools into igneous rock. Sedimentary Layers form slowly because weathering at the surface is minimal."),
        ("Surface Erosion Scenario", "With high Weathering Rate and low Heat & Pressure, Sedimentary Layers build up rapidly. Surface rocks (of all types) are broken down and compressed into sedimentary deposits. Metamorphic Transformation and Igneous Rock Formation are minimal because underground conditions are not intense enough to transform or melt rock.")
    ],
    "reflection_exemplars": [
        ("Why is it a cycle and not a chain?", "A chain has a beginning and an end, but the rock cycle has neither. Any rock type can become any other rock type: granite (igneous) can weather into sandstone (sedimentary), which can be buried and pressed into slate (metamorphic), which can melt and cool into new igneous rock. But granite can also go directly to metamorphic, or metamorphic can weather directly to sedimentary. There are many paths, and the cycle never stops as long as Earth has internal heat and external energy."),
        ("What if Earth's internal heat died out?", "If Earth's core cooled completely, the rock cycle would become a half-cycle. Without internal heat, there would be no melting (no new igneous rock), no plate tectonics (no subduction or uplift), and no metamorphism (no heat/pressure). Only weathering and sedimentary rock formation would continue, driven by solar energy. Eventually, all rocks would be broken down into sediment. Mars is an example: its core cooled, and its geological recycling essentially stopped billions of years ago.")
    ],
    "stem_intro": "A geology museum needs a new exhibit showing how the rock cycle has shaped Earth's surface over 4.6 billion years. Your team will create a visual timeline connecting major geologic events to the rock cycle, using your simulation data to explain which conditions produced which rock types.",
    "stem_concepts": [
        ("Law of Superposition", "In undisturbed rock strata, the oldest layers are on the bottom and the youngest are on top. This principle allows geologists to determine the relative age of rock layers and the fossils they contain, forming the basis of the geologic time scale."),
        ("Plate Tectonics and the Rock Cycle", "Tectonic plate movement drives much of the rock cycle. Subduction zones push rock into the mantle (where it metamorphoses or melts), while volcanic activity brings new igneous rock to the surface. Mountain building uplifts deep rocks to the surface where weathering begins."),
        ("Index Fossils", "Certain fossils are found only in rocks of a specific age range. These index fossils help geologists correlate rock layers across different locations and determine their age. For example, trilobites indicate Paleozoic era rocks (541-252 million years ago).")
    ],
    "stem_eval": [
        ("Expert (4)", "Timeline accurately represents major geologic events, connects rock types to specific conditions using model data, includes rock strata evidence, and explains the continuous cycling of Earth's materials"),
        ("Proficient (3)", "Timeline shows major events and connects the rock cycle to geologic history with model evidence"),
        ("Developing (2)", "Timeline lists some events but doesn't clearly connect them to the rock cycle or use model data"),
        ("Beginning (1)", "Timeline is incomplete or shows misconceptions about how rock types form and transform")
    ],
    "support": [
        "Provide rock samples of all three types (granite, sandstone, marble) for students to examine and compare",
        "Use a simplified geologic time scale poster with major events pre-labeled for reference",
        "Sentence frames: 'When heat and pressure increase, __ forms because __, which means the rock has been __'"
    ],
    "extensions": [
        "Research how geologists use radiometric dating to determine the absolute age of igneous and metamorphic rocks",
        "Investigate how metamorphic grade (low to high) tells scientists about the intensity of conditions the rock experienced",
        "Model how the rock cycle interacts with the water cycle and carbon cycle as interconnected Earth systems"
    ],
    "cross_curr": [
        ("Math", "Create a proportional timeline of Earth's 4.6-billion-year history and calculate what percentage of that time has had multicellular life"),
        ("ELA", "Write a narrative from the perspective of a single atom as it journeys through the rock cycle over billions of years"),
        ("Social Studies", "Research how ancient civilizations used different rock types for building and tools, connecting to their local geology")
    ],
    "misconceptions": [
        ("Rocks don't change", "Rocks are constantly changing, just very slowly from a human perspective. Over millions of years, mountains erode to plains, seafloors become mountaintops, and solid rock melts to magma and solidifies again. The rock cycle transforms rocks continuously.", "Show time-lapse erosion footage. Ask: What would this rock look like in 10,000 years? 10 million years?"),
        ("The rock cycle goes in one direction", "The rock cycle has NO fixed direction. Any rock type can become any other type. Igneous can become sedimentary OR metamorphic. Sedimentary can become metamorphic OR melt to become igneous. The path depends entirely on the conditions the rock encounters.", "Draw the rock cycle as a triangle with arrows going in EVERY direction between all three types. There's no 'start' or 'end.'"),
        ("Fossils are only found in very old rocks", "Fossils are found in sedimentary rocks of ALL ages, from billions of years old to very recent. Fossils are forming right now as organisms die and are buried in sediment. What changes over time is the TYPE of organisms preserved: ancient rocks contain simple organisms, while recent rocks contain more complex life.", "Show a recent shell being buried in beach sand. This is the beginning of fossilization. Now show an ancient trilobite fossil. Same process, different time.")
    ]
}
