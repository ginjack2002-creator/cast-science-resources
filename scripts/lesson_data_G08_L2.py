#!/usr/bin/env python3
"""Complete lesson data for G08L2-L01 through G08L2-L07 (Grade 8 Level 2 ModelIt! Lessons)"""

L01 = {
    "id": "G08L2-L01",
    "title": "Survival of the Fittest: Can You Outrun Natural Selection?",
    "subtitle": "How Environmental Pressure and Genetic Diversity Shape Who Survives",
    "ngss": "MS-LS4-4, MS-LS4-6",
    "ngss_desc": "Construct an explanation based on evidence that describes how genetic variations of traits in a population increase some individuals' probability of surviving and reproducing in a specific environment. Use mathematical representations to support explanations of how natural selection may lead to increases and decreases of specific traits in populations over time.",
    "big_question": "Can a population survive when the environment changes faster than it can adapt?",
    "objectives": [
        "Explain how environmental pressure selects for certain traits over others",
        "Model how population diversity affects a species' ability to survive change",
        "Use mathematical representations to track trait frequency changes across generations",
        "Predict outcomes for populations with high vs. low genetic diversity under stress"
    ],
    "vocabulary": [
        ("Environmental Pressure", "Any factor in the environment that affects which organisms survive and reproduce"),
        ("Population Diversity", "The range of different traits and genetic variations within a group of organisms"),
        ("Favorable Trait Frequency", "The percentage of a population that carries a trait suited to the current environment"),
        ("Natural Selection", "The process by which organisms with traits better suited to their environment survive and reproduce more"),
        ("Fitness", "An organism's ability to survive and reproduce in its specific environment")
    ],
    "components": [
        ("Environmental Pressure", "Intensity of drought, predators, or disease affecting the population", True),
        ("Population Diversity", "Range of trait variations present in the population", True),
        ("Favorable Trait Frequency", "Percentage of the population carrying advantageous traits", False),
        ("Survival Rate", "Percentage of individuals that survive each generation", False),
        ("Reproduction Rate", "Number of offspring produced per surviving individual", False)
    ],
    "think_about_it": "When environmental pressure increases dramatically, what happens to a population with very little genetic diversity compared to one with a wide range of traits?",
    "scenarios": [
        ("Stable Environment", "Set Environmental Pressure and Population Diversity to moderate levels"),
        ("Sudden Drought", "Lock Environmental Pressure to 90% with low Population Diversity (20%)"),
        ("Diverse Population Under Stress", "Lock Environmental Pressure to 90% with high Population Diversity (80%)")
    ],
    "sim_scenarios": [
        ("Stable Environment", "Moderate pressure, moderate diversity", "What do you predict will happen to Survival Rate over 20 generations?"),
        ("Low Diversity Crisis", "High Environmental Pressure, low Population Diversity", "What do you predict will happen to Favorable Trait Frequency?"),
        ("High Diversity Advantage", "High Environmental Pressure, high Population Diversity", "How does this compare to the low diversity scenario?")
    ],
    "discoveries": [
        "Populations with greater genetic diversity have more 'options' for natural selection to work with",
        "Environmental pressure doesn't create new traits — it selects for traits that already exist",
        "Low-diversity populations can crash rapidly under strong environmental pressure",
        "Natural selection is NOT random — it predictably favors traits that match the environment",
        "Reproduction rate amplifies the effect of selection by spreading favorable traits faster"
    ],
    "answer": "Natural selection acts on existing genetic variation. When environmental pressure increases, populations with high diversity have a better chance of containing individuals with favorable traits. Those individuals survive and reproduce, shifting the population's trait frequency over generations. Low-diversity populations may lack the right traits entirely and face extinction!",
    "stem_title": "Design a Species Conservation Strategy",
    "stem_mission": "Design an evidence-based conservation plan for an endangered species facing rapid environmental change, using your model data to justify every recommendation.",
    "stem_scenario": "A population of desert tortoises is declining as temperatures rise and drought intensifies. Wildlife biologists need your team to propose a conservation strategy that maximizes the species' chances of long-term survival.",
    "stem_questions": [
        "What role does genetic diversity play in the species' ability to adapt?",
        "How can conservationists maintain or increase population diversity?",
        "At what point does a population become too small to recover?"
    ],
    "stem_design_qs": [
        "What specific actions will increase genetic diversity in the population?",
        "How will you reduce environmental pressure on the species?",
        "What monitoring system will track trait frequency changes over time?",
        "How will you measure whether your strategy is working?"
    ],
    "career": "Conservation Biologists and Wildlife Geneticists study how genetic diversity affects species survival and design strategies to protect endangered populations. They earn $55,000-$95,000/year.",
    "images": {
        "cover": ("cover-natural-selection.png", "A photorealistic dramatic scene of a diverse group of animals in a challenging desert landscape, some thriving and some struggling, golden hour lighting with dust in the air, cinematic quality"),
        "landscape": ("landscape-natural-selection.png", "A photorealistic image of a White male 8th grade student (age 13-14) leading a group of diverse classmates examining animal skull specimens and fossils in a modern science lab, wearing casual clothes like hoodies and jeans, natural window light, engaged expressions"),
        "modeling": ("modeling-natural-selection.png", "A photorealistic image of an Asian female 8th grade student (age 13-14) pointing at a laptop screen while building a population model, diverse classmates gathered around, modern classroom with evolution and biodiversity posters, natural lighting"),
        "discussion": ("discussion-natural-selection.png", "A photorealistic image of a Black male 8th grade student (age 13-14) presenting data about trait frequencies to engaged classmates, teacher nodding approvingly, modern classroom with natural light and science displays"),
        "stem": ("stem-natural-selection.png", "A photorealistic image of a Latino female 8th grade student (age 13-14) leading her team in presenting a species conservation poster with graphs and data, diverse teammates contributing, modern classroom setting")
    },
    "pre_assessment": [
        "What does 'survival of the fittest' mean to you?",
        "Why do you think some species go extinct while others survive environmental changes?",
        "What is genetic diversity, and why might it matter for a population?",
        "Draw what you think happens to a population when its environment suddenly changes."
    ],
    "extend_components": [
        ("Migration Rate", "New individuals joining the population bring different genetic traits"),
        ("Mutation Rate", "Random DNA changes introduce new traits over generations"),
        ("Predator Efficiency", "How effectively predators target specific traits in the prey population")
    ],
    "reflections": [
        "Why is genetic diversity sometimes called an 'insurance policy' for a species?",
        "How does natural selection differ from random chance? Use evidence from your model.",
        "Why might a population that survived one environmental change still be vulnerable to the next?",
        "How does the concept of favorable trait frequency help explain why some endangered species recover while others don't?",
        "What would happen if humans artificially reduced the genetic diversity of a crop species?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model to demonstrate how natural selection changes trait frequencies in a population over multiple generations."),
        ("Disciplinary Core Idea", "LS4.B Natural Selection", "Natural selection leads to the predominance of certain traits in a population and the suppression of others based on environmental conditions."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify that environmental pressure CAUSES differential survival, which leads to the EFFECT of changed trait frequencies across generations.")
    ],
    "cast_items": [
        "Construct an explanation for how genetic variations affect survival probability",
        "Use mathematical representations to describe trait frequency changes over time",
        "Support claims about natural selection with evidence from population data"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A population of lizards lives in a region where temperatures are rising. Only 15% of the population carries a heat-tolerance gene. After 10 generations of intense heat, 80% of survivors carry the gene. Which best explains this shift?"),
        ("Constructed Response:", "Using evidence from your model, explain why a population with high genetic diversity is more likely to survive a sudden environmental change than a population with low diversity. Reference specific components and relationships from your simulation.")
    ],
    "background_intro": "Natural selection is one of the key mechanisms of evolution, first described by Charles Darwin and Alfred Russel Wallace. It explains how populations change over time as environmental pressures favor certain inherited traits over others. Understanding natural selection is critical for conservation biology, agriculture, and medicine.",
    "background_sections": [
        ("The Three Requirements for Natural Selection", "Natural selection requires three conditions: variation (individuals differ in their traits), heritability (traits are passed from parents to offspring), and differential survival (some traits provide better chances of surviving and reproducing in the current environment). When all three are present, populations evolve."),
        ("Genetic Diversity as a Survival Tool", "A population's genetic diversity is its toolkit for facing change. Large, diverse populations contain many trait variations, increasing the odds that some individuals will have traits suited to new conditions. Small, inbred populations with low diversity are vulnerable because they may lack the genetic 'raw material' for adaptation."),
        ("Mathematical Patterns of Selection", "Trait frequency changes follow predictable mathematical patterns. Under strong selection pressure, favorable trait frequency increases rapidly in early generations, then slows as it approaches fixation (100%). The Hardy-Weinberg principle describes the mathematical conditions under which trait frequencies remain stable — no selection, no mutation, no migration, large population, random mating."),
        ("Real-World Examples", "The peppered moth in industrial England evolved from mostly light-colored to mostly dark-colored in just decades as pollution darkened tree bark. Darwin's finches on the Galapagos Islands show beak size shifts in response to drought years. Antibiotic-resistant bacteria demonstrate natural selection happening in days rather than years.")
    ],
    "lever_L": "Students identify environmental pressure, population diversity, favorable trait frequency, survival rate, and reproduction rate as system components.",
    "lever_E": "Students determine that environmental pressure negatively affects survival rate, population diversity positively affects favorable trait frequency, and favorable traits positively affect survival, which drives reproduction.",
    "lever_V": "Students build the natural selection model showing how environmental pressure and genetic diversity interact to drive population change.",
    "lever_Ev": "Students compare low-diversity vs. high-diversity populations under identical environmental stress and analyze the mathematical difference in outcomes.",
    "lever_R": "Students add migration rate or mutation rate to explore how new genetic variation enters a population.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Dramatic natural selection imagery", "say": "If a deadly drought hit tomorrow, would every animal in the herd survive? Why not?", "do": "Show images of diverse animal populations. Build suspense about who survives and why.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we model one of biology's most powerful ideas — natural selection in action.", "do": "Have students read objectives. Pre-teach 'trait frequency' vs. 'genetic diversity.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Can you outrun natural selection?", "say": "Can a species survive when the environment changes faster than it can adapt?", "do": "Think-pair-share: What traits might help an animal survive a drought?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll use the LEVER framework to build and test a model of natural selection.", "do": "Briefly preview each LEVER step.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Natural selection system components", "say": "What are the key parts of this system? Which ones can we control vs. which respond?", "do": "Guide sorting of external vs. internal components. Emphasize that diversity is the raw material.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "Here's the key: pressure doesn't CREATE favorable traits — it REVEALS which ones matter.", "do": "Map positive and negative relationships. Focus on the feedback loop from reproduction back to trait frequency.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and scenario results", "say": "Let's test: will a diverse population survive what wipes out a uniform one?", "do": "Students predict before running. Compare low vs. high diversity under identical pressure.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from the model", "say": "What did the data reveal about diversity and survival? Were you surprised?", "do": "Whole-class discussion. Connect to real examples like cheetah genetic bottleneck.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Conservation strategy design", "say": "You're conservation biologists. A species is declining — what's your evidence-based rescue plan?", "do": "Distribute materials. Circulate and probe for model evidence in proposals.", "time": "12 min"}
    ],
    "sort_reasoning": "Environmental Pressure and Population Diversity are external because they represent conditions imposed on or brought into the population from outside — the environment creates pressure, and diversity is a pre-existing condition of the gene pool. Favorable Trait Frequency, Survival Rate, and Reproduction Rate are internal because they change as direct consequences of the interaction between pressure and diversity.",
    "relationships": [
        ("Environmental Pressure to Survival Rate", "NEGATIVE (-)", "Harsher environmental conditions reduce the overall percentage of individuals that survive each generation."),
        ("Population Diversity to Favorable Trait Frequency", "POSITIVE (+)", "Greater genetic diversity means a higher chance that some individuals carry traits suited to the current environment."),
        ("Favorable Trait Frequency to Survival Rate", "POSITIVE (+)", "When more individuals carry advantageous traits, a greater percentage survives environmental challenges."),
        ("Survival Rate to Reproduction Rate", "POSITIVE (+)", "More survivors means more individuals reproduce and pass on their traits to the next generation."),
        ("Reproduction Rate to Favorable Trait Frequency", "POSITIVE (+)", "Surviving individuals with favorable traits reproduce, increasing the frequency of those traits in the next generation — this is natural selection in action.")
    ],
    "sim_answers": [
        ("Low Diversity Crisis", "When Environmental Pressure is set to 90% and Population Diversity is only 20%, Favorable Trait Frequency starts very low — there simply aren't enough individuals with the right traits. Survival Rate crashes within a few generations, and Reproduction Rate follows. The population spirals toward extinction because natural selection has too little variation to work with."),
        ("High Diversity Advantage", "When Environmental Pressure is the same 90% but Population Diversity is 80%, Favorable Trait Frequency starts much higher. Survival Rate dips initially but stabilizes as favorable traits spread. Within 10-15 generations, the population has adapted — Favorable Trait Frequency climbs toward 70-80%. This demonstrates why biodiversity is critical for long-term survival.")
    ],
    "reflection_exemplars": [
        ("Why is genetic diversity an insurance policy?", "Just like financial insurance protects against unexpected events, genetic diversity protects a species against unpredictable environmental changes. A diverse population is more likely to contain individuals with traits that happen to be useful when conditions change. Without that diversity, a single disease or climate shift could eliminate everyone because they all share the same vulnerability."),
        ("How does natural selection differ from random chance?", "Random chance determines which mutations arise and what environmental changes occur. But natural selection is NOT random — it systematically favors individuals whose traits best match the current environment. In our model, we can predict that higher Environmental Pressure will consistently reduce Survival Rate and that populations with more diversity will fare better. These outcomes are directional and predictable, not random.")
    ],
    "stem_intro": "Present a scenario: Desert tortoise populations have declined 90% in some areas due to rising temperatures and prolonged drought. Genetic analysis shows remaining populations have dangerously low diversity. Your team must design a rescue strategy.",
    "stem_concepts": [
        ("Genetic Rescue", "Introducing individuals from genetically distinct populations to increase diversity and adaptive potential."),
        ("Minimum Viable Population", "The smallest population size that can sustain itself over the long term — typically 500-5,000 individuals depending on the species."),
        ("Assisted Migration", "Moving individuals to new habitats where environmental conditions better match their traits.")
    ],
    "stem_eval": [
        ("Expert (4)", "Strategy uses model evidence to address both diversity and pressure, includes monitoring plan with measurable goals"),
        ("Proficient (3)", "Strategy references model data and includes at least two evidence-based conservation actions"),
        ("Developing (2)", "Strategy mentions diversity or pressure but lacks specific model evidence"),
        ("Beginning (1)", "Strategy doesn't connect to natural selection concepts or model findings")
    ],
    "support": [
        "Provide trait cards that students can physically sort to simulate selection",
        "Use color-coded population diagrams showing trait frequency shifts across generations",
        "Sentence frames: 'When environmental pressure increases, survival rate __ because __'"
    ],
    "extensions": [
        "Research the cheetah genetic bottleneck and calculate how low diversity nearly caused extinction",
        "Add a migration component to the model and test how gene flow from another population affects outcomes",
        "Debate: Should we use genetic engineering to increase diversity in endangered species?"
    ],
    "cross_curr": [
        ("Math", "Calculate trait frequency percentages across generations and graph the rate of change using exponential models"),
        ("ELA", "Write a scientific argument explaining why genetic diversity matters for species survival, using model evidence"),
        ("Social Studies", "Research how human activities such as habitat fragmentation reduce genetic diversity in wildlife populations")
    ],
    "misconceptions": [
        ("Survival of the fittest means the strongest survive", "Fitness in biology means reproductive success in a specific environment, not physical strength. A small, camouflaged lizard may be 'fitter' than a large, conspicuous one if predators are the main pressure.", "Ask: Would the strongest animal survive a disease outbreak? What trait would actually help?"),
        ("Animals choose to adapt or evolve on purpose", "Individual organisms cannot choose to evolve. Natural selection acts on variation that already exists in the population. Giraffes didn't 'decide' to grow longer necks — individuals with slightly longer necks survived better and reproduced more.", "Run the model: Can the population 'choose' which traits to have? What determines which traits spread?"),
        ("Evolution always makes species better", "Natural selection optimizes for the CURRENT environment. If conditions change again, previously favorable traits may become harmful. Evolution doesn't have a direction or goal — it responds to present conditions only.", "Change the environmental pressure in the model mid-simulation. Watch how previously favorable traits can become disadvantageous.")
    ]
}

L02 = {
    "id": "G08L2-L02",
    "title": "Trophic Cascades: When Predators Disappear",
    "subtitle": "How Removing One Species Can Collapse an Entire Ecosystem",
    "ngss": "MS-LS2-1, MS-LS2-4",
    "ngss_desc": "Analyze and interpret data to provide evidence for the effects of resource availability on organisms and populations of organisms in an ecosystem. Construct an argument supported by empirical evidence that changes to physical or biological components of an ecosystem affect populations.",
    "big_question": "What happens to an entire ecosystem when the top predator vanishes?",
    "objectives": [
        "Explain how apex predators regulate ecosystem balance through top-down control",
        "Model the cascade of effects when a predator is removed from a food web",
        "Predict how vegetation loss leads to erosion and ecosystem collapse",
        "Evaluate real-world evidence from the Yellowstone wolf reintroduction"
    ],
    "vocabulary": [
        ("Trophic Cascade", "A chain of ecological effects triggered by adding or removing a top predator"),
        ("Apex Predator", "The top predator in a food chain with no natural predators of its own"),
        ("Overgrazing", "When herbivore populations grow unchecked and destroy vegetation faster than it can regrow"),
        ("Ecosystem Stability", "The ability of an ecosystem to maintain its structure and function over time"),
        ("Top-Down Control", "When predators regulate the populations below them in the food web")
    ],
    "components": [
        ("Apex Predator Population", "Number of top predators such as wolves or sharks in the ecosystem", True),
        ("Herbivore Population", "Number of prey species like deer or elk", False),
        ("Vegetation Health", "Plant coverage, growth rate, and root strength", False),
        ("Erosion Rate", "Rate of soil loss from bare, unprotected ground", False),
        ("Ecosystem Stability", "Overall health and balance of the entire ecosystem", False)
    ],
    "think_about_it": "If all wolves were removed from Yellowstone National Park, what do you think would happen to the elk population? And what would happen after that?",
    "scenarios": [
        ("Balanced Ecosystem", "Set Apex Predator Population to a moderate, natural level"),
        ("Predator Removal", "Lock Apex Predator Population to 0% and observe the cascade"),
        ("Predator Reintroduction", "Restore Apex Predator Population to 50% after removal")
    ],
    "sim_scenarios": [
        ("Balanced Ecosystem", "Natural predator-prey balance", "What do you predict will happen to Vegetation Health over time?"),
        ("Predator Removal", "Set Apex Predator Population to 0%", "What do you predict will happen to Herbivore Population, then Vegetation, then Erosion?"),
        ("Predator Reintroduction", "Restore predators to 50% after removal", "How long does it take for the cascade to reverse?")
    ],
    "discoveries": [
        "Removing apex predators causes herbivore populations to explode without natural checks",
        "Unchecked herbivores overgraze vegetation, leaving soil bare and vulnerable",
        "Vegetation loss triggers erosion that damages the entire ecosystem — even rivers and streams",
        "Restoring predators can reverse the cascade, but recovery takes years or decades",
        "Wolves in Yellowstone literally changed the course of rivers by allowing vegetation to regrow on banks"
    ],
    "answer": "When apex predators disappear, herbivores multiply unchecked and overgraze vegetation. Without plant roots to hold soil, erosion accelerates and destroys habitat for all species. The entire ecosystem cascades toward collapse — all from removing one species at the top!",
    "stem_title": "Design a Wildlife Management Plan",
    "stem_mission": "Design an evidence-based wildlife management plan for a national park experiencing ecosystem decline due to predator loss.",
    "stem_scenario": "A state park has removed wolves 20 years ago due to rancher complaints. Now the park is experiencing severe erosion, declining bird populations, and degraded streams. Your team must propose a recovery plan using model evidence.",
    "stem_questions": [
        "What evidence from your model supports predator reintroduction?",
        "How will you address concerns from nearby ranchers about livestock safety?",
        "What timeline does your model suggest for ecosystem recovery?"
    ],
    "stem_design_qs": [
        "How many predators should be reintroduced and on what schedule?",
        "What monitoring systems will track herbivore populations and vegetation recovery?",
        "How will you manage conflicts between wildlife and local communities?",
        "What milestones will indicate your plan is working?"
    ],
    "career": "Wildlife Ecologists and Conservation Managers study predator-prey dynamics and design management strategies for national parks and wildlife reserves. They earn $55,000-$95,000/year.",
    "images": {
        "cover": ("cover-trophic-cascades.png", "A photorealistic dramatic landscape showing a healthy green forest on one side transitioning to an overgrazed barren landscape on the other, with a wolf silhouette overlooking the healthy side, cinematic lighting"),
        "landscape": ("landscape-trophic-cascades.png", "A photorealistic image of an Asian male 8th grade student (age 13-14) examining a food web poster with diverse classmates in a modern science lab, wearing jeans and a hoodie, natural window light, enthusiastic expressions"),
        "modeling": ("modeling-trophic-cascades.png", "A photorealistic image of a Black female 8th grade student (age 13-14) leading a group working on laptops to build an ecosystem model, diverse classmates collaborating, modern classroom with ecology posters"),
        "discussion": ("discussion-trophic-cascades.png", "A photorealistic image of a White female 8th grade student (age 13-14) raising her hand to contribute to a class discussion about wolf reintroduction, diverse classmates engaged, teacher facilitating, bright classroom"),
        "stem": ("stem-trophic-cascades.png", "A photorealistic image of a Latino male 8th grade student (age 13-14) presenting a wildlife management poster with ecosystem data to classmates, diverse team supporting, modern classroom setting")
    },
    "pre_assessment": [
        "What is an apex predator and can you name some examples?",
        "What do you think would happen if all predators in an area disappeared?",
        "How are different species in an ecosystem connected to each other?",
        "Draw a simple food web and predict what happens when you remove the top predator."
    ],
    "extend_components": [
        ("Scavenger Population", "Animals like ravens and beetles that feed on predator kills"),
        ("Stream Health", "Water quality and bank stability affected by vegetation"),
        ("Bird Diversity", "Number of bird species, which depends on habitat variety from vegetation")
    ],
    "reflections": [
        "Why is it surprising that wolves can affect the course of rivers?",
        "How does the Yellowstone wolf story challenge the idea that predators are just 'dangerous animals'?",
        "Why did the ecosystem NOT recover on its own after 70 years without wolves?",
        "What does the trophic cascade model reveal about the idea that 'everything is connected' in nature?",
        "Should humans actively manage wildlife populations, or should we let nature find its own balance?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students build a computational model showing how changes to one trophic level cascade through the entire ecosystem."),
        ("Disciplinary Core Idea", "LS2.C Ecosystem Dynamics, Functioning, and Resilience", "Ecosystems are dynamic; changes to physical or biological components can cascade through the entire system."),
        ("Crosscutting Concept", "Cause and Effect", "Students trace the causal chain from predator removal through herbivore explosion, vegetation loss, erosion, and ecosystem instability.")
    ],
    "cast_items": [
        "Analyze data showing how removal of one species affects others in the food web",
        "Construct arguments supported by evidence about ecosystem disruption",
        "Use models to predict cascading effects of changes to biological components"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Wolves are removed from a forest ecosystem. Over the next 10 years, streambank erosion increases by 300%. Which chain of events best explains this?"),
        ("Constructed Response:", "Using evidence from your model, construct an argument explaining why removing apex predators from an ecosystem can cause damage to components that seem completely unrelated to predators, such as soil and rivers.")
    ],
    "background_intro": "Trophic cascades are among the most dramatic demonstrations of ecological interconnection. The removal or addition of a single species at the top of a food web can trigger a chain of effects that transforms entire landscapes — even reshaping rivers and coastlines.",
    "background_sections": [
        ("What Is a Trophic Cascade?", "A trophic cascade occurs when changes at one level of a food web ripple through other levels. Top-down cascades happen when predator changes affect everything below them. Bottom-up cascades happen when changes to producers (plants) affect everything above. The most dramatic examples involve top-down cascades triggered by predator removal or reintroduction."),
        ("The Yellowstone Wolf Story", "Wolves were eliminated from Yellowstone National Park by 1926. Without predators, elk populations exploded and overgrazed willows, aspens, and cottonwoods — especially along riverbanks. Without root systems to stabilize banks, rivers widened and became shallower. When 41 wolves were reintroduced in 1995-96, elk behavior changed immediately. Elk avoided lingering near rivers (the 'landscape of fear'), vegetation regrew, banks stabilized, and rivers literally changed course. Beaver, songbirds, and fish populations recovered."),
        ("The Ecology of Fear", "Predators affect prey not just by killing them but by changing their behavior. The 'landscape of fear' describes how prey avoid areas where predators hunt, allowing vegetation to recover in those zones. This behavioral effect can be as powerful as direct predation in shaping ecosystems."),
        ("Marine Trophic Cascades", "Similar cascades occur in the ocean. When sea otters were hunted to near-extinction, sea urchin populations exploded and devoured kelp forests. Without kelp, entire coastal ecosystems collapsed. Restoring otter populations allowed kelp forests to recover, bringing back fish, invertebrates, and seabirds.")
    ],
    "lever_L": "Students identify apex predator population, herbivore population, vegetation health, erosion rate, and ecosystem stability as system components.",
    "lever_E": "Students determine that predators negatively affect herbivores, herbivores negatively affect vegetation, vegetation negatively affects erosion, and both vegetation and erosion affect ecosystem stability.",
    "lever_V": "Students build the trophic cascade model showing how predator removal triggers a chain reaction through the entire ecosystem.",
    "lever_Ev": "Students compare balanced, predator-removed, and predator-reintroduced scenarios to measure the cascade effect and recovery time.",
    "lever_R": "Students add stream health or bird diversity components to extend the cascade model further.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Healthy vs. degraded landscape split", "say": "Same place, 20 years apart. What could possibly cause this much damage?", "do": "Show Yellowstone before/after wolf removal photos. Let students react.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we model how removing ONE species can collapse an entire ecosystem.", "do": "Pre-teach 'trophic cascade' with a domino metaphor.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "What happens when predators disappear?", "say": "You might think removing a dangerous predator makes things better. Think again.", "do": "Quick poll: Who thinks removing wolves would help or hurt Yellowstone?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll build a model to trace the chain reaction from predators to rivers.", "do": "Preview the surprising connection between wolves and rivers.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Ecosystem components", "say": "What are the key parts of this ecosystem? Can you guess which ones wolves affect?", "do": "Guide sorting. Build anticipation for indirect effects.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Cascade relationship chain", "say": "Watch how each connection creates a domino effect through the whole system.", "do": "Map the chain step by step. Emphasize that wolves connect to rivers through FOUR links.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Predator removal and reintroduction", "say": "Let's remove the wolves and watch. Then let's bring them back.", "do": "Students predict each stage. Run removal, then reintroduction. Compare timelines.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key cascade findings", "say": "Wolves changed the course of rivers. Let that sink in.", "do": "Show the 'How Wolves Change Rivers' video summary. Discuss ecosystem interconnection.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Wildlife management plan", "say": "A park is in trouble. You're the ecologists hired to fix it. What does your model tell you?", "do": "Teams design management plans using model evidence. Present and defend.", "time": "12 min"}
    ],
    "sort_reasoning": "Apex Predator Population is external because it represents an input that humans or natural events can control or change (hunting, reintroduction programs). Herbivore Population, Vegetation Health, Erosion Rate, and Ecosystem Stability are all internal because they respond to and change as a result of predator levels and each other.",
    "relationships": [
        ("Apex Predator Population to Herbivore Population", "NEGATIVE (-)", "More predators kill more herbivores, keeping their numbers in check. Fewer predators allow herbivore populations to explode."),
        ("Herbivore Population to Vegetation Health", "NEGATIVE (-)", "More herbivores consume more plants, leading to overgrazing and vegetation decline."),
        ("Vegetation Health to Erosion Rate", "NEGATIVE (-)", "Healthy vegetation holds soil in place with root systems. Less vegetation means more bare soil exposed to wind and water erosion."),
        ("Vegetation Health to Ecosystem Stability", "POSITIVE (+)", "Healthy vegetation supports habitat, food, and shelter for diverse species, increasing overall ecosystem stability."),
        ("Erosion Rate to Ecosystem Stability", "NEGATIVE (-)", "High erosion degrades habitat, silts waterways, and destroys the foundation that the ecosystem depends on.")
    ],
    "sim_answers": [
        ("Predator Removal", "When Apex Predator Population drops to 0%, Herbivore Population surges rapidly within 5-10 generations. Vegetation Health crashes as overgrazing intensifies. Erosion Rate spikes as bare soil is exposed. Ecosystem Stability plummets as the cascade of destruction reaches every level. The model shows how one removal triggers a chain reaction through four connected components."),
        ("Predator Reintroduction", "When Apex Predators are restored to 50%, Herbivore Population begins declining. Vegetation Health starts recovering, but slowly — plants take time to regrow. Erosion Rate gradually decreases as roots re-establish. Ecosystem Stability begins climbing but takes significantly longer to recover than it took to collapse. This asymmetry shows why prevention is easier than restoration.")
    ],
    "reflection_exemplars": [
        ("Why can wolves affect rivers?", "Wolves don't touch rivers directly. But by reducing elk numbers and changing elk behavior (the 'landscape of fear'), wolves allow willows and other plants to regrow along riverbanks. Those root systems stabilize the soil, narrow river channels, and create deeper pools. The cascade crosses four trophic levels: predator → herbivore → vegetation → geomorphology. This is the power of indirect ecological effects."),
        ("Why didn't the ecosystem recover on its own?", "Without predators, the system reached a new stable state — one with too many herbivores, little vegetation, and high erosion. This degraded state was self-reinforcing: bare soil couldn't support new plant growth, which kept herbivores concentrated on remaining patches, preventing recovery. The system needed an external intervention (wolf reintroduction) to break the cycle.")
    ],
    "stem_intro": "Present a case study: A state park removed wolves 20 years ago after rancher complaints. Now the park reports 40% vegetation loss, stream widening, declining bird species, and severe erosion. The park board has asked your team for an evidence-based recovery plan.",
    "stem_concepts": [
        ("Predator Reintroduction", "Carefully managed return of apex predators to restore top-down ecosystem regulation."),
        ("Landscape of Fear", "The behavioral effect where prey avoid certain areas due to predator presence, allowing vegetation recovery."),
        ("Ecosystem Services Valuation", "Calculating the economic value of services provided by healthy ecosystems — water filtration, erosion control, tourism revenue.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan uses model evidence to justify predator reintroduction, addresses stakeholder concerns, and includes a monitoring timeline with measurable recovery milestones"),
        ("Proficient (3)", "Plan references model data and proposes specific reintroduction strategy with monitoring"),
        ("Developing (2)", "Plan mentions predator-prey relationships but lacks specific model evidence or stakeholder consideration"),
        ("Beginning (1)", "Plan doesn't connect to trophic cascade concepts or model findings")
    ],
    "support": [
        "Provide a visual food web poster showing Yellowstone species at each trophic level",
        "Use domino demonstrations to physically model cascade effects",
        "Sentence frames: 'When apex predators are removed, herbivore populations __ because __'"
    ],
    "extensions": [
        "Research the sea otter-urchin-kelp cascade and compare it to the Yellowstone wolf story",
        "Add stream health and bird diversity components to extend the cascade model",
        "Calculate the economic value of ecosystem services restored by wolf reintroduction"
    ],
    "cross_curr": [
        ("Math", "Graph population changes at each trophic level over time and calculate the rate of cascade propagation"),
        ("ELA", "Write a persuasive essay arguing for or against predator reintroduction using model evidence"),
        ("Social Studies", "Research the political and social conflicts surrounding wolf reintroduction in the American West")
    ],
    "misconceptions": [
        ("Predators are bad for ecosystems", "Apex predators are essential regulators. Without them, herbivore populations grow unchecked and damage the very habitat that supports all species. Predators maintain balance through top-down control.", "Show the Yellowstone data: More wolves = healthier ecosystem. Ask students what their model predicts when predators are removed."),
        ("Removing one species only affects that species", "Ecosystems are interconnected networks. Removing one species — especially a keystone species like an apex predator — triggers cascading effects through multiple trophic levels that can transform entire landscapes.", "In the model, remove predators and count how many OTHER components change. The cascade affects everything."),
        ("Ecosystems always recover naturally", "Degraded ecosystems can become trapped in unhealthy stable states. Without intervention, overgrazing prevents vegetation recovery, which prevents erosion reduction, which prevents ecosystem recovery. Sometimes the system needs an external push to restart.", "Ask: If the model has been running for 50 generations without predators, does vegetation recover on its own?")
    ]
}

L03 = {
    "id": "G08L2-L03",
    "title": "Why Baking Soda Explodes: Reaction Rates and Energy",
    "subtitle": "How Reactant Amount and Surface Area Control Chemical Reactions",
    "ngss": "MS-PS1-2, MS-PS1-5",
    "ngss_desc": "Analyze and interpret data on the properties of substances before and after the substances interact to determine if a chemical reaction has occurred. Develop and use a model to describe how the total number of atoms does not change in a chemical reaction and thus mass is conserved.",
    "big_question": "Why does baking soda and vinegar explode, and where does the mass go?",
    "objectives": [
        "Explain how reactant amount and surface area affect the rate of a chemical reaction",
        "Model the relationship between reaction rate, gas production, and mass conservation",
        "Demonstrate that total system mass is conserved even when gas is produced",
        "Predict how changing reaction conditions affects the speed and intensity of a reaction"
    ],
    "vocabulary": [
        ("Reaction Rate", "How fast reactants convert into products in a chemical reaction"),
        ("Surface Area", "The amount of exposed surface where reactants can make contact"),
        ("Conservation of Mass", "The principle that total mass in a closed system stays the same before and after a reaction"),
        ("Gas Production", "The formation of gaseous products such as carbon dioxide during a chemical reaction"),
        ("Reactant", "A starting substance that is consumed during a chemical reaction")
    ],
    "components": [
        ("Reactant Amount", "How much baking soda and vinegar are combined", True),
        ("Surface Area", "Whether the baking soda is fine powder or large chunks", True),
        ("Reaction Rate", "Speed at which the chemical reaction proceeds", False),
        ("Gas Production (CO2)", "Amount of carbon dioxide bubbles produced", False),
        ("Total System Mass", "Combined mass of all reactants and products — always conserved", False)
    ],
    "think_about_it": "If you put baking soda and vinegar in a sealed bag and weigh it before and after the reaction, will the mass change? What if the bag is open?",
    "scenarios": [
        ("Standard Reaction", "Set Reactant Amount to moderate and Surface Area to medium"),
        ("Maximum Explosion", "Lock Reactant Amount to 100% with fine powder (Surface Area 100%)"),
        ("Slow Fizz", "Set Reactant Amount to 30% with large chunks (Surface Area 20%)")
    ],
    "sim_scenarios": [
        ("Standard Reaction", "Moderate amounts, medium surface area", "What do you predict will happen to Gas Production over time?"),
        ("Maximum Explosion", "Maximum reactant, maximum surface area", "What do you predict will happen to Reaction Rate and Gas Production?"),
        ("Slow Fizz", "Low reactant, low surface area", "How does this compare to the maximum explosion scenario?")
    ],
    "discoveries": [
        "More reactant produces more product, but at the same rate per unit of reactant",
        "Increasing surface area dramatically speeds up the reaction — powder reacts faster than chunks",
        "Total System Mass stays constant in a sealed system, even though gas is produced",
        "When the container is open, mass appears to decrease because gas escapes — but the gas still has mass",
        "Reactants are consumed as products form — the lines on the graph are inverse mirrors"
    ],
    "answer": "Baking soda and vinegar react to produce carbon dioxide gas, water, and sodium acetate. More reactant and more surface area mean faster, more intense reactions. The 'explosion' is CO2 gas escaping rapidly. In a sealed system, total mass never changes because atoms are rearranged, not created or destroyed!",
    "stem_title": "Design the Ultimate Reaction Container",
    "stem_mission": "Design an experiment to prove that mass is conserved in a chemical reaction, even when gas is produced, by engineering a container that captures all products.",
    "stem_scenario": "Your science team has been challenged to prove conservation of mass to skeptical classmates who believe that mass 'disappears' when a reaction produces gas. Design a sealed reaction system and present your evidence.",
    "stem_questions": [
        "How can you contain all products, including gas, to measure total mass?",
        "What variables will you control to ensure a fair test?",
        "How will you explain the apparent mass loss in an open system?"
    ],
    "stem_design_qs": [
        "What container design will seal the reaction while allowing you to weigh it?",
        "How will you measure mass before and after with precision?",
        "What safety considerations are needed when gas pressure builds?",
        "How will you present your data to convince skeptics?"
    ],
    "career": "Chemical Engineers and Materials Scientists design chemical processes and reactions for industry, from pharmaceuticals to food production to energy. They earn $75,000-$130,000/year.",
    "images": {
        "cover": ("cover-baking-soda.png", "A photorealistic dramatic close-up of a baking soda and vinegar reaction erupting with foamy bubbles overflowing from a flask, laboratory setting with precise scientific equipment, high-speed photography style"),
        "landscape": ("landscape-baking-soda.png", "A photorealistic image of a Latino female 8th grade student (age 13-14) wearing safety goggles and pouring vinegar into a flask of baking soda while diverse classmates watch eagerly in a science lab, natural lighting"),
        "modeling": ("modeling-baking-soda.png", "A photorealistic image of a White male 8th grade student (age 13-14) at a laptop building a chemical reaction rate model, diverse classmates collaborating around the table, modern classroom with chemistry posters"),
        "discussion": ("discussion-baking-soda.png", "A photorealistic image of an Asian female 8th grade student (age 13-14) explaining conservation of mass using a whiteboard diagram to engaged diverse classmates, teacher observing, bright modern classroom"),
        "stem": ("stem-baking-soda.png", "A photorealistic image of a Black male 8th grade student (age 13-14) presenting an experiment design poster showing sealed vs. open reaction containers, diverse team supporting, modern classroom")
    },
    "pre_assessment": [
        "What happens when you mix baking soda and vinegar?",
        "Where do the bubbles come from in a chemical reaction?",
        "If a reaction produces gas, does the total mass increase, decrease, or stay the same?",
        "Draw what you think happens to the atoms in baking soda and vinegar during the reaction."
    ],
    "extend_components": [
        ("Temperature", "Higher temperatures increase molecular motion and speed up reactions"),
        ("Catalyst Presence", "Substances that speed up reactions without being consumed"),
        ("pH Level", "Acidity of the vinegar affects how vigorously the reaction proceeds")
    ],
    "reflections": [
        "Why does increasing surface area speed up a reaction even though the total amount of reactant is the same?",
        "If mass is truly conserved, why does a fizzing open container weigh less after the reaction?",
        "How does the baking soda reaction demonstrate that atoms are rearranged, not destroyed?",
        "Why is it important for scientists to work with sealed systems when studying conservation of mass?",
        "How could understanding reaction rates help in real-world applications like manufacturing or cooking?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model showing how reactant amount and surface area control reaction rate and demonstrate conservation of mass."),
        ("Disciplinary Core Idea", "PS1.B Chemical Reactions", "The total number of atoms does not change during a chemical reaction; atoms rearrange to form new substances while conserving mass."),
        ("Crosscutting Concept", "Energy and Matter", "Students track matter through a chemical reaction, demonstrating that atoms are conserved even as they form new arrangements and new substances.")
    ],
    "cast_items": [
        "Analyze data to determine if a chemical reaction has occurred based on property changes",
        "Develop a model showing that mass is conserved during chemical reactions",
        "Use evidence to explain how reaction conditions affect reaction rates"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student seals baking soda and vinegar in a plastic bag, weighs it, lets the reaction occur, and weighs it again. The mass stays the same. Then the student opens the bag and weighs it. The mass decreases. Which best explains this?"),
        ("Constructed Response:", "Using evidence from your model, explain how both reactant amount and surface area affect reaction rate. Include a description of what happens to total system mass during the reaction and why.")
    ],
    "background_intro": "Chemical reactions involve the rearrangement of atoms from reactant molecules into product molecules. Understanding what controls reaction rate and how mass is conserved is fundamental to chemistry, engineering, and everyday life — from cooking to manufacturing to medicine.",
    "background_sections": [
        ("The Baking Soda-Vinegar Reaction", "When sodium bicarbonate (baking soda, NaHCO3) reacts with acetic acid (vinegar, CH3COOH), three products form: sodium acetate (NaCH3COO), water (H2O), and carbon dioxide gas (CO2). The fizzing and bubbling is CO2 escaping. Every atom from the reactants ends up in the products — nothing is created or destroyed."),
        ("Reaction Rate Factors", "Reaction rate depends on how often reactant particles collide with enough energy to react. Surface area increases the number of exposed particles available for collision. More reactant means more particles overall. Higher temperature increases particle speed and collision frequency. Catalysts lower the energy barrier for successful collisions."),
        ("Conservation of Mass", "Antoine Lavoisier established the law of conservation of mass in the 1780s. In any chemical reaction, the total mass of reactants equals the total mass of products. When reactions seem to lose mass (like burning wood), the 'missing' mass has become gases that escaped into the atmosphere. In sealed systems, mass remains constant."),
        ("Surface Area and Particle Size", "Grinding a solid into powder dramatically increases its surface area. A 1 cm cube has 6 cm² of surface area, but crushing it into powder can produce hundreds of cm² of surface area from the same volume. This is why powdered sugar dissolves faster than sugar cubes, and why grain dust in silos can explode — maximized surface area means maximized reaction rate.")
    ],
    "lever_L": "Students identify reactant amount, surface area, reaction rate, gas production, and total system mass as system components.",
    "lever_E": "Students determine that reactant amount and surface area both positively affect reaction rate, which drives gas production, while total system mass remains constant.",
    "lever_V": "Students build the chemical reaction model showing how inputs control rate and outputs while mass is conserved.",
    "lever_Ev": "Students compare maximum explosion vs. slow fizz scenarios and verify that total system mass is identical in both cases.",
    "lever_R": "Students add temperature or catalyst components to explore additional factors affecting reaction rate.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Dramatic reaction eruption", "say": "Baking soda and vinegar — you've done it since kindergarten. But do you know WHY it explodes?", "do": "Quick demonstration: baking soda + vinegar in a flask. Build curiosity.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we go deeper — modeling the science behind every fizzy reaction.", "do": "Have students read objectives. Pre-teach 'conservation of mass.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Where does the mass go?", "say": "If gas escapes during a reaction, is mass really conserved? Let's find out.", "do": "Weigh a sealed bag before and after the reaction. Reveal the answer later.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model what controls how fast and how violently this reaction happens.", "do": "Preview the connection between surface area and explosion intensity.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Reaction system components", "say": "What are the key parts of this chemical system? What can we change?", "do": "Guide sorting. Discuss why surface area matters even when the amount is the same.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Reaction rate relationships", "say": "More surface area means more collisions between reactant particles — faster reaction!", "do": "Map relationships. Use collision analogy (dodgeball with more players).", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Explosion vs. slow fizz", "say": "Let's compare: powder explodes while chunks barely fizz. But is the total mass different?", "do": "Students predict, then run. Focus on the Total System Mass line staying flat.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Conservation of mass proof", "say": "The gas has mass! When you seal the system, nothing is lost. Atoms rearrange, not disappear.", "do": "Return to the sealed bag demonstration. Weigh it again. Mass unchanged!", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Reaction container design", "say": "Prove to the skeptics: mass is conserved. Design an experiment that shows it.", "do": "Teams design sealed reaction experiments. Present evidence.", "time": "12 min"}
    ],
    "sort_reasoning": "Reactant Amount and Surface Area are external because they are inputs the experimenter directly controls before the reaction begins. Reaction Rate, Gas Production, and Total System Mass are internal because they are outcomes determined by the external inputs and the laws of chemistry.",
    "relationships": [
        ("Reactant Amount to Reaction Rate", "POSITIVE (+)", "More reactant means more particles available to collide and react, increasing the overall rate of the reaction."),
        ("Surface Area to Reaction Rate", "POSITIVE (+)", "Greater surface area exposes more reactant particles for contact, dramatically increasing collision frequency and reaction speed."),
        ("Reaction Rate to Gas Production", "POSITIVE (+)", "A faster reaction produces carbon dioxide gas more quickly, creating more vigorous bubbling and fizzing."),
        ("Reaction Rate to Reactant Amount", "NEGATIVE (-)", "As the reaction proceeds, reactants are consumed and converted into products, decreasing the amount of reactant remaining."),
        ("Total System Mass remains CONSTANT", "NEUTRAL (=)", "In a sealed system, the total mass of all reactants equals the total mass of all products. Atoms are rearranged, not created or destroyed.")
    ],
    "sim_answers": [
        ("Maximum Explosion", "When Reactant Amount is at 100% and Surface Area is at 100% (fine powder), Reaction Rate spikes immediately to maximum. Gas Production surges — the reaction is fast and intense. But the reactants are consumed quickly, so the reaction also ends sooner. Total System Mass stays perfectly flat throughout."),
        ("Slow Fizz", "When Reactant Amount is at 30% and Surface Area is at 20% (large chunks), Reaction Rate is much slower. Gas Production is gradual — a gentle fizz instead of an explosion. The reaction takes longer to complete because fewer particle surfaces are exposed. Total System Mass is again perfectly constant — proving conservation of mass regardless of reaction speed.")
    ],
    "reflection_exemplars": [
        ("Why does surface area matter if the amount is the same?", "Imagine a cube of ice vs. crushed ice in a glass of water. The crushed ice melts faster because more surface is in contact with the water. Similarly, powdered baking soda has vastly more surface area exposed to vinegar than a single chunk of the same mass. More contact points means more simultaneous reactions, which means a faster overall rate."),
        ("Why does an open container weigh less after the reaction?", "The carbon dioxide gas produced during the reaction has mass — it's made of carbon and oxygen atoms from the reactants. In an open container, this gas floats away into the air, carrying its mass with it. The atoms aren't destroyed — they're just no longer on the scale. In a sealed container, the gas stays inside, and the total mass on the scale doesn't change.")
    ],
    "stem_intro": "Challenge the class: Most people think mass disappears during chemical reactions. Your job is to prove them wrong. Design an experiment using baking soda and vinegar in sealed vs. open containers to demonstrate conservation of mass.",
    "stem_concepts": [
        ("Sealed System vs. Open System", "A sealed system prevents matter from entering or leaving, making it possible to verify conservation of mass. Open systems allow gases to escape, creating the illusion of mass loss."),
        ("Precision Measurement", "Using digital balances with 0.01g precision to detect or rule out mass changes during reactions."),
        ("Controlled Variables", "Keeping temperature, amounts, and container type constant while changing only the variable being tested.")
    ],
    "stem_eval": [
        ("Expert (4)", "Experiment design uses sealed and open systems, precise measurements, controlled variables, and clearly explains apparent vs. real mass changes"),
        ("Proficient (3)", "Experiment demonstrates conservation with sealed system and references model data"),
        ("Developing (2)", "Experiment involves the reaction but lacks systematic control or clear mass measurements"),
        ("Beginning (1)", "Experiment doesn't clearly test conservation of mass or connect to model concepts")
    ],
    "support": [
        "Provide a visual showing atoms before and after the reaction (same atoms, new arrangement)",
        "Use sealed plastic bags for hands-on mass conservation demonstrations",
        "Sentence frames: 'When surface area increases, reaction rate __ because __'"
    ],
    "extensions": [
        "Test how temperature affects reaction rate by running the reaction in cold vs. warm vinegar",
        "Calculate the theoretical mass of CO2 produced from a known amount of baking soda",
        "Research how surface area affects reaction rates in real-world applications like catalytic converters"
    ],
    "cross_curr": [
        ("Math", "Calculate the surface area of a cube vs. the same volume crushed into smaller cubes, and graph how surface area relates to reaction rate"),
        ("ELA", "Write a lab report explaining the experiment that proves conservation of mass, using scientific reasoning and model evidence"),
        ("Social Studies", "Research how Antoine Lavoisier's discovery of conservation of mass revolutionized chemistry and ended the phlogiston theory")
    ],
    "misconceptions": [
        ("Gas produced means mass is lost", "The gas (CO2) has mass just like any other substance. In an open container, the gas escapes and takes its mass with it — but the atoms still exist. In a sealed container, total mass stays exactly the same.", "Weigh a sealed bag before and after the reaction. The scale doesn't change. Then open the bag and weigh again — now it's lighter because gas escaped."),
        ("Chemical reactions create new atoms", "Chemical reactions REARRANGE existing atoms into new combinations. No atoms are created or destroyed. The same carbon, hydrogen, oxygen, and sodium atoms from the reactants end up in the products — just in different molecular arrangements.", "Count the atoms on both sides of the balanced equation: NaHCO3 + CH3COOH → NaCH3COO + H2O + CO2. Same atoms, different arrangement."),
        ("Faster reactions produce more product", "Faster reactions produce the SAME amount of product — just more quickly. The total product depends on the amount of reactant, not the speed of the reaction. A powder explosion and a chunk fizz produce the same total CO2 from the same mass of baking soda.", "Compare the final values in the maximum explosion and slow fizz scenarios — the endpoints are the same, only the speed differs.")
    ]
}

L04 = {
    "id": "G08L2-L04",
    "title": "Climate Feedback Loops: Why Small Changes Get Big",
    "subtitle": "How CO2, Temperature, Ice, and Reflectivity Create a Runaway System",
    "ngss": "MS-ESS2-6, MS-ESS3-5",
    "ngss_desc": "Develop and use a model to describe how unequal heating and rotation of the Earth cause patterns of atmospheric and oceanic circulation that determine regional climates. Ask questions to clarify evidence of the factors that have caused the rise in global temperatures over the past century.",
    "big_question": "Why do small increases in CO2 lead to such large changes in global temperature?",
    "objectives": [
        "Explain how CO2 emissions drive the greenhouse effect and global warming",
        "Model the positive feedback loop between temperature, ice cover, and albedo",
        "Predict how feedback loops amplify small changes into large climate shifts",
        "Evaluate evidence for why climate scientists are concerned about tipping points"
    ],
    "vocabulary": [
        ("Feedback Loop", "A cycle where the output of a system feeds back to become an input, amplifying or dampening the original change"),
        ("Albedo", "The reflectivity of a surface — how much incoming sunlight is bounced back to space"),
        ("Greenhouse Effect", "When atmospheric gases trap heat that would otherwise escape to space, warming the planet"),
        ("Tipping Point", "A threshold beyond which a system shifts rapidly to a new state and may not easily return"),
        ("Positive Feedback", "A feedback loop where the output amplifies the original change, creating a snowball effect")
    ],
    "components": [
        ("CO2 Emissions Rate", "Amount of carbon dioxide released from human activities like burning fossil fuels", True),
        ("Atmospheric CO2 Level", "Concentration of greenhouse gases in the atmosphere", False),
        ("Global Temperature", "Earth's average surface temperature", False),
        ("Ice Cover", "Extent of ice at the Arctic, Antarctic, and glaciers worldwide", False),
        ("Albedo (Reflectivity)", "How much incoming sunlight Earth's surface reflects back to space", False)
    ],
    "think_about_it": "When ice melts and reveals dark ocean or land underneath, what happens to the amount of sunlight absorbed vs. reflected? How does that affect temperature?",
    "scenarios": [
        ("Pre-Industrial Baseline", "Set CO2 Emissions Rate to 10% — natural background levels"),
        ("Current Emissions", "Set CO2 Emissions Rate to 60% — approximate current human output"),
        ("Runaway Feedback", "Lock CO2 Emissions Rate to 90% and observe the feedback loop over 50 years")
    ],
    "sim_scenarios": [
        ("Pre-Industrial Baseline", "Low CO2 emissions, natural levels", "What do you predict will happen to Ice Cover and Global Temperature?"),
        ("Current Emissions", "Modern emission levels", "What do you predict will happen to Albedo as ice melts?"),
        ("Runaway Feedback", "Very high emissions sustained for 50 years", "What do you predict happens when the feedback loop accelerates?")
    ],
    "discoveries": [
        "CO2 traps heat through the greenhouse effect, raising global temperatures",
        "Higher temperatures melt ice, which reduces albedo (reflectivity)",
        "Lower albedo means more sunlight absorbed instead of reflected, causing MORE warming",
        "This creates a positive feedback loop: warming → ice melt → lower albedo → more warming → more ice melt",
        "Feedback loops explain why small CO2 increases can trigger disproportionately large temperature changes"
    ],
    "answer": "CO2 emissions increase atmospheric greenhouse gas levels, trapping heat and raising temperatures. Warming melts ice, exposing dark surfaces that absorb more sunlight instead of reflecting it (lower albedo). This causes more warming, which melts more ice, creating a positive feedback loop that amplifies small changes into major climate shifts!",
    "stem_title": "Design a Climate Action Plan",
    "stem_mission": "Design an evidence-based climate action plan for your city that targets the feedback loop at its most effective intervention point, using data from your model.",
    "stem_scenario": "Your city council has asked your team to propose a climate action plan. They want to know: where in the CO2-temperature-ice feedback loop can we intervene most effectively, and what measurable goals should we set?",
    "stem_questions": [
        "At which point in the feedback loop is intervention most effective?",
        "What CO2 reduction level is needed to stabilize the feedback?",
        "How do you address the time delay between action and result?"
    ],
    "stem_design_qs": [
        "What specific emission reductions will your plan target?",
        "How will you address the feedback loop's self-reinforcing nature?",
        "What timeline does your model suggest for achieving stabilization?",
        "How will you measure progress and communicate results to the public?"
    ],
    "career": "Climate Scientists and Atmospheric Researchers study feedback loops in Earth's climate system and develop models to predict future changes. They earn $70,000-$120,000/year and work at universities, government agencies, and research institutions.",
    "images": {
        "cover": ("cover-climate-feedback.png", "A photorealistic dramatic aerial view of a glacier calving into the ocean with meltwater streams, showing the contrast between brilliant white ice and dark blue water, cinematic lighting, environmental photography"),
        "landscape": ("landscape-climate-feedback.png", "A photorealistic image of a Black female 8th grade student (age 13-14) analyzing climate data graphs on a screen with diverse classmates in a modern science classroom, wearing casual clothes, natural window lighting"),
        "modeling": ("modeling-climate-feedback.png", "A photorealistic image of an Asian male 8th grade student (age 13-14) drawing a feedback loop diagram on a whiteboard while diverse classmates work on laptops building a climate model, modern classroom with Earth science posters"),
        "discussion": ("discussion-climate-feedback.png", "A photorealistic image of a White female 8th grade student (age 13-14) pointing at a projected graph showing ice cover decline while leading a discussion with diverse engaged classmates, bright modern classroom"),
        "stem": ("stem-climate-feedback.png", "A photorealistic image of a Latino male 8th grade student (age 13-14) presenting a climate action plan poster with graphs and data to city council members (adults), diverse team behind him, professional setting")
    },
    "pre_assessment": [
        "What is the greenhouse effect, and how does it relate to global warming?",
        "What do you think happens when Arctic ice melts?",
        "Have you heard of a 'feedback loop'? What do you think it means?",
        "Draw a diagram showing how you think CO2 in the atmosphere affects Earth's temperature."
    ],
    "extend_components": [
        ("Permafrost Thaw", "Frozen ground that releases methane — an even stronger greenhouse gas — when it melts"),
        ("Ocean Heat Absorption", "Oceans absorb heat, slowing atmospheric warming but causing marine impacts"),
        ("Cloud Cover Changes", "Warming changes cloud patterns, which can either reflect or trap more heat")
    ],
    "reflections": [
        "Why is the ice-albedo feedback loop called a 'positive' feedback even though the effects are negative?",
        "How does the concept of a tipping point make climate change different from gradual temperature change?",
        "Why is it harder to reverse a feedback loop than to stop it before it starts?",
        "What does your model reveal about the difference between 'linear thinking' and 'systems thinking'?",
        "How might understanding feedback loops change the way governments approach climate policy?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model demonstrating how feedback loops in Earth's climate system amplify initial changes."),
        ("Disciplinary Core Idea", "ESS3.D Global Climate Change", "Human activities are major factors in global warming. Rising temperatures create feedback loops that can accelerate change beyond initial causes."),
        ("Crosscutting Concept", "Stability and Change", "Students analyze how feedback loops can push a system past a stability threshold (tipping point) into a fundamentally different state.")
    ],
    "cast_items": [
        "Develop a model showing how feedback loops amplify climate changes",
        "Ask questions to clarify evidence about factors driving global temperature rise",
        "Analyze data showing relationships between CO2, temperature, and ice cover"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Arctic ice cover has decreased by 40% since 1980. A student claims this creates a feedback loop that causes more warming. Which chain of events supports this claim?"),
        ("Constructed Response:", "Using evidence from your model, explain why a small increase in CO2 emissions can lead to a disproportionately large increase in global temperature. Include the role of albedo and the feedback loop in your explanation.")
    ],
    "background_intro": "Earth's climate is regulated by complex feedback loops that can either stabilize or destabilize the system. Understanding these feedback mechanisms is essential for predicting how human-caused CO2 emissions will affect global climate in the coming decades.",
    "background_sections": [
        ("The Greenhouse Effect", "Earth's atmosphere contains gases (CO2, methane, water vapor) that trap outgoing infrared radiation. This greenhouse effect keeps Earth approximately 33°C warmer than it would be without an atmosphere. Human activities have increased atmospheric CO2 from 280 ppm (pre-industrial) to over 420 ppm today — a 50% increase."),
        ("The Ice-Albedo Feedback", "Ice and snow reflect 80-90% of incoming sunlight (high albedo). Open ocean and dark land absorb 90-94% of sunlight (low albedo). As warming melts ice, the exposed dark surface absorbs more heat, causing more warming, which melts more ice. This is the ice-albedo positive feedback loop — the most significant amplifying feedback in Earth's climate system."),
        ("Climate Tipping Points", "Scientists have identified several potential tipping points: complete Arctic summer ice loss, Greenland ice sheet collapse, permafrost thaw releasing stored methane, Amazon rainforest dieback, and Atlantic circulation shutdown. Once crossed, these tipping points may be irreversible on human timescales. Current estimates suggest some tipping points could be crossed between 1.5°C and 2°C of warming above pre-industrial levels."),
        ("The Carbon Budget", "Scientists estimate humanity can emit approximately 400 billion more tons of CO2 while maintaining a 50% chance of staying below 1.5°C of warming. At current emission rates (approximately 40 billion tons per year), this budget will be exhausted within a decade. The feedback loops in the climate system mean that every fraction of a degree matters.")
    ],
    "lever_L": "Students identify CO2 emissions rate, atmospheric CO2 level, global temperature, ice cover, and albedo as system components.",
    "lever_E": "Students determine that emissions drive CO2 levels, CO2 drives temperature, temperature reduces ice, ice affects albedo, and albedo feeds back to temperature — creating a loop.",
    "lever_V": "Students build the climate feedback model showing how a linear cause-effect chain becomes a self-reinforcing loop.",
    "lever_Ev": "Students compare pre-industrial, current, and runaway scenarios to see how the feedback loop amplifies with higher emissions.",
    "lever_R": "Students add permafrost thaw or ocean heat absorption to model additional feedback mechanisms.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Dramatic glacier calving imagery", "say": "This glacier is 10,000 years old. It's disappearing in decades. Why?", "do": "Show time-lapse video of glacier retreat. Let the visual create urgency.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we model why Earth's climate has a hidden 'accelerator pedal' built in.", "do": "Pre-teach 'feedback loop' with an audio feedback analogy (microphone near speaker).", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why do small changes get big?", "say": "A little CO2 shouldn't cause this much change. So why does it?", "do": "Think-pair-share: What's the difference between a gradual change and a snowball effect?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll build a model that shows how Earth's climate amplifies small changes.", "do": "Preview the concept of feedback loops — this is the first loop model in the curriculum.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Climate system components", "say": "What are the key parts of the climate feedback system?", "do": "Guide sorting. Emphasize that most components are INTERNAL — only emissions are truly external.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Feedback loop arrows", "say": "Watch: the last arrow connects BACK to the beginning. That's what makes it a loop.", "do": "Draw the loop step by step. The moment students see the loop close is the 'aha' moment.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Emissions scenarios with feedback", "say": "At low emissions, the loop barely runs. At high emissions, watch what happens.", "do": "Students predict, then run all three scenarios. Focus on the acceleration in the runaway scenario.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Tipping point evidence", "say": "This is why scientists talk about tipping points. Small changes can become unstoppable.", "do": "Connect to real Arctic ice data. Discuss what 'irreversible' means.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Climate action plan", "say": "Your city council wants a plan. Where in the loop do you intervene? Show your evidence.", "do": "Teams design action plans targeting specific loop components. Present with data.", "time": "12 min"}
    ],
    "sort_reasoning": "CO2 Emissions Rate is external because it represents human activities that input carbon into the atmosphere from outside the climate system. Atmospheric CO2 Level, Global Temperature, Ice Cover, and Albedo are all internal because they respond to each other in a self-reinforcing feedback loop — each one is both a cause and an effect within the system.",
    "relationships": [
        ("CO2 Emissions Rate to Atmospheric CO2 Level", "POSITIVE (+)", "More fossil fuel burning releases more CO2 into the atmosphere, increasing the concentration of greenhouse gases."),
        ("Atmospheric CO2 Level to Global Temperature", "POSITIVE (+)", "Higher CO2 concentrations trap more outgoing heat through the greenhouse effect, raising Earth's average temperature."),
        ("Global Temperature to Ice Cover", "NEGATIVE (-)", "Higher temperatures melt ice sheets, glaciers, and sea ice, reducing the total area of frozen surfaces on Earth."),
        ("Ice Cover to Albedo", "POSITIVE (+)", "More ice means more reflective surface area to bounce sunlight back to space. Less ice means lower reflectivity."),
        ("Albedo to Global Temperature", "NEGATIVE (-)", "Higher albedo reflects more sunlight, cooling Earth. Lower albedo absorbs more sunlight, warming Earth. This is where the FEEDBACK LOOP closes — lower albedo causes more warming, which melts more ice, which lowers albedo further.")
    ],
    "sim_answers": [
        ("Current Emissions", "At 60% emissions, Atmospheric CO2 rises steadily. Global Temperature increases gradually, causing Ice Cover to decline. As Ice Cover drops, Albedo decreases, which adds ADDITIONAL warming on top of the greenhouse effect. The feedback loop is active but manageable — the system is warming faster than CO2 alone would predict."),
        ("Runaway Feedback", "At 90% emissions sustained for 50 years, the feedback loop accelerates dramatically. Temperature rises quickly → ice melts rapidly → albedo plummets → absorbed sunlight adds massive additional warming → even more ice melts. The graph shows exponential acceleration rather than linear increase. This is the tipping point scenario — the system 'runs away' from human control.")
    ],
    "reflection_exemplars": [
        ("Why is positive feedback called positive if it's bad?", "In systems science, 'positive' doesn't mean 'good.' It means the feedback AMPLIFIES the original change — pushes it further in the same direction. A positive feedback loop that increases warming makes warming worse. A negative feedback loop would dampen the change and bring the system back toward balance. The terminology describes the direction of amplification, not whether the outcome is desirable."),
        ("Why is prevention easier than reversal?", "Once the ice-albedo feedback loop is running at full strength, reducing emissions alone may not be enough to stop it. Even if we cut CO2, the reduced ice cover continues absorbing extra heat, maintaining warming. The system has memory — the dark surface stays dark until new ice forms, which requires temperatures below freezing for extended periods. Preventing ice loss is far easier than re-freezing the Arctic.")
    ],
    "stem_intro": "Present real data: Arctic ice has decreased 40% since 1980, CO2 has increased 50% since pre-industrial times, and global temperature has risen 1.2°C. Your city council wants a plan that targets the most effective intervention point in the feedback loop.",
    "stem_concepts": [
        ("Carbon Capture", "Technologies that remove CO2 from the atmosphere to reduce greenhouse gas concentrations."),
        ("Albedo Enhancement", "Strategies like painting roofs white or restoring ice to increase reflectivity and counteract warming."),
        ("Emissions Reduction", "Transitioning from fossil fuels to renewable energy to reduce the CO2 input that drives the entire feedback loop.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan targets specific components of the feedback loop, uses model evidence to justify intervention points, includes timeline and measurable goals"),
        ("Proficient (3)", "Plan addresses emissions reduction with reference to the feedback loop and model data"),
        ("Developing (2)", "Plan mentions climate action but doesn't specifically target the feedback mechanism"),
        ("Beginning (1)", "Plan doesn't connect to the feedback loop or model findings")
    ],
    "support": [
        "Provide a color-coded diagram showing the feedback loop with arrows",
        "Use ice cubes on white vs. dark surfaces to demonstrate albedo differences",
        "Sentence frames: 'When ice cover decreases, albedo __ because __, which causes temperature to __'"
    ],
    "extensions": [
        "Research permafrost methane release and add it as a second feedback loop to the model",
        "Graph real Arctic ice extent data from 1980-present and identify acceleration patterns",
        "Debate: Is it more effective to cut emissions or develop carbon capture technology?"
    ],
    "cross_curr": [
        ("Math", "Calculate the percentage of additional solar energy absorbed when ice cover drops from 80% to 40%, using albedo values for ice (0.85) and ocean (0.06)"),
        ("ELA", "Write an explanatory article for a local newspaper describing how feedback loops make climate change accelerate beyond simple CO2 effects"),
        ("Social Studies", "Research how different countries contribute to and are affected by climate change, and analyze climate justice implications")
    ],
    "misconceptions": [
        ("Climate change is just gradual warming", "Feedback loops mean climate change is NOT gradual — it can accelerate. The ice-albedo feedback creates a snowball effect where warming causes changes that cause MORE warming. The relationship between CO2 and temperature is not a straight line but a curve that steepens over time.", "Run the model at constant emissions and watch the temperature graph. It curves upward, not in a straight line, because of the feedback loop."),
        ("Melting ice is the only problem", "Ice loss matters not primarily because of the ice itself, but because of what it reveals. Dark ocean and land absorb vastly more sunlight than ice, creating additional warming. The loss of reflective surface is a planetary thermostat being broken.", "Compare the model with and without the albedo feedback. Without albedo, temperature rises slowly from CO2 alone. With albedo feedback, it accelerates dramatically."),
        ("We can just stop emissions and everything will be fine", "Even if emissions stopped today, the feedback loops already in motion would continue for decades. Reduced ice cover continues absorbing extra heat. Warming oceans continue releasing stored heat. The climate system has inertia — like a freight train, it doesn't stop the moment you release the brake.", "In the model, cut emissions to 0% after running at high levels. Observe how long the system takes to stabilize. The delay is the inertia.")
    ]
}

L05 = {
    "id": "G08L2-L05",
    "title": "Potential to Kinetic: The Energy Transformation Chain",
    "subtitle": "How Height, Mass, and Friction Determine Where Energy Goes",
    "ngss": "MS-PS3-1, MS-PS3-5",
    "ngss_desc": "Construct and interpret graphical displays of data to describe the relationships of kinetic energy to the mass of an object and to the speed of an object. Construct, use, and present arguments to support the claim that when the kinetic energy of an object changes, energy is transferred to or from the object.",
    "big_question": "Where does the energy go when a roller coaster slows down at the bottom of a hill?",
    "objectives": [
        "Explain how potential energy converts to kinetic energy as an object falls",
        "Model how mass and height determine the amount of potential energy stored",
        "Demonstrate that total energy is conserved even when friction generates heat",
        "Predict how friction changes the distribution of energy in a system"
    ],
    "vocabulary": [
        ("Potential Energy", "Energy stored in an object due to its position or height — the higher it is, the more energy is stored"),
        ("Kinetic Energy", "Energy of motion — a moving object has kinetic energy based on its mass and speed"),
        ("Thermal Energy", "Heat energy generated by friction when surfaces rub together"),
        ("Conservation of Energy", "The principle that energy cannot be created or destroyed, only transformed from one form to another"),
        ("Energy Transformation", "The conversion of energy from one form to another, such as potential to kinetic")
    ],
    "components": [
        ("Height", "Starting elevation of the object above the ground", True),
        ("Mass", "Weight of the object", True),
        ("Potential Energy", "Energy stored due to position — increases with height and mass", False),
        ("Kinetic Energy", "Energy of motion — increases as the object falls and speeds up", False),
        ("Thermal Energy (Friction)", "Heat generated by friction between the object and surfaces", False)
    ],
    "think_about_it": "If you drop a heavy ball and a light ball from the same height, which hits the ground with more energy? And if there's friction on the ramp, where does the 'lost' speed go?",
    "scenarios": [
        ("Ideal Drop", "Set Height to 80%, Mass to 50%, observe PE to KE conversion"),
        ("Heavy vs. Light", "Compare Mass at 90% vs. Mass at 20% from the same Height"),
        ("Friction World", "Add increasing friction and observe Thermal Energy absorb Kinetic Energy")
    ],
    "sim_scenarios": [
        ("Ideal Drop", "High height, moderate mass, no friction", "What do you predict will happen to PE and KE as the object falls?"),
        ("Heavy vs. Light", "Same height, different masses", "What do you predict about the KE of the heavier vs. lighter object?"),
        ("High Friction", "Same starting conditions plus heavy friction", "What do you predict will happen to the Thermal Energy line?")
    ],
    "discoveries": [
        "As an object falls, its potential energy decreases while kinetic energy increases — energy transforms, not disappears",
        "Heavier objects store more potential energy at the same height and therefore have more kinetic energy at the bottom",
        "Friction converts kinetic energy into thermal energy (heat), slowing the object down",
        "Total energy (PE + KE + Thermal) remains CONSTANT — conservation of energy is always obeyed",
        "In a frictionless world, PE at the top would exactly equal KE at the bottom"
    ],
    "answer": "Energy is never lost — it transforms. At the top of a hill, an object has maximum potential energy. As it descends, PE converts to KE (speed). Friction converts some KE into thermal energy (heat). At any point, PE + KE + Thermal Energy always equals the starting energy. The roller coaster 'slows down' because energy has transformed into heat, not because it disappeared!",
    "stem_title": "Design an Energy-Efficient Ramp System",
    "stem_mission": "Design a ramp system that maximizes the kinetic energy delivered to a target at the bottom, minimizing energy loss to friction, using evidence from your model.",
    "stem_scenario": "An engineering firm needs to design a delivery system that uses gravity to move packages from a high warehouse shelf to a packing station below. Your team must design the most energy-efficient ramp, maximizing speed at the bottom.",
    "stem_questions": [
        "What height and angle maximize kinetic energy at the bottom?",
        "How does surface material affect energy lost to friction?",
        "What is the trade-off between ramp length and friction losses?"
    ],
    "stem_design_qs": [
        "What ramp material minimizes friction while maintaining safety?",
        "How steep should the ramp be for maximum efficiency?",
        "What mass range can your system handle effectively?",
        "How will you measure the kinetic energy at the bottom to prove efficiency?"
    ],
    "career": "Mechanical Engineers and Energy Systems Designers create machines and systems that efficiently convert and transfer energy. They earn $70,000-$120,000/year and work across industries from transportation to manufacturing.",
    "images": {
        "cover": ("cover-energy-transformation.png", "A photorealistic dramatic image of a roller coaster at the peak of its highest hill with a city skyline in the background, golden hour lighting, emphasizing the height and potential energy of the moment"),
        "landscape": ("landscape-energy-transformation.png", "A photorealistic image of a White female 8th grade student (age 13-14) releasing a ball down a ramp while diverse classmates measure speed with sensors in a modern physics lab, wearing casual clothes, natural lighting"),
        "modeling": ("modeling-energy-transformation.png", "A photorealistic image of a Latino male 8th grade student (age 13-14) at a laptop graphing energy transformation data, diverse classmates collaborating, modern classroom with physics and energy posters"),
        "discussion": ("discussion-energy-transformation.png", "A photorealistic image of an Asian female 8th grade student (age 13-14) pointing at a projected energy bar graph explaining PE to KE conversion, diverse engaged classmates, bright modern classroom"),
        "stem": ("stem-energy-transformation.png", "A photorealistic image of a Black male 8th grade student (age 13-14) demonstrating a ramp design to classmates with measuring tools and data displays, diverse team supporting, modern classroom")
    },
    "pre_assessment": [
        "What is potential energy and what is kinetic energy?",
        "Where does a roller coaster have the most energy — at the top or bottom of a hill?",
        "What happens to a ball's speed when it rolls down a ramp? Where does the speed come from?",
        "Draw an energy diagram for a ball rolling down a ramp, showing PE and KE at the top, middle, and bottom."
    ],
    "extend_components": [
        ("Air Resistance", "Drag force that opposes motion and converts kinetic energy to thermal energy"),
        ("Elastic Energy", "Energy stored in compressed or stretched materials like springs"),
        ("Sound Energy", "Energy converted to vibrations in the air when objects collide or scrape surfaces")
    ],
    "reflections": [
        "Why can't a roller coaster's second hill be taller than its first?",
        "If energy is conserved, why do machines always seem to 'waste' energy?",
        "How does the model prove that friction doesn't destroy energy but transforms it?",
        "Why does a heavier object rolling down a ramp have more kinetic energy but not necessarily more speed?",
        "Where does the thermal energy from friction go after it's generated? Does it disappear?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students build a model showing energy transformations between potential, kinetic, and thermal forms while demonstrating conservation."),
        ("Disciplinary Core Idea", "PS3.B Conservation of Energy", "Energy is transferred between objects or converted between forms, but the total energy in a closed system is conserved."),
        ("Crosscutting Concept", "Energy and Matter", "Students track energy through transformations, demonstrating that energy is conserved in quantity even as it changes form.")
    ],
    "cast_items": [
        "Construct graphical displays showing the relationship between KE and mass or speed",
        "Present arguments that energy is transferred when an object's kinetic energy changes",
        "Use models to demonstrate conservation of energy across multiple transformations"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A 2 kg ball is released from a height of 10 meters on a frictionless ramp. At the bottom, its kinetic energy is 196 J. If the same ball is released on a ramp with friction, at the bottom its kinetic energy is 150 J. What happened to the other 46 J?"),
        ("Constructed Response:", "Using evidence from your model, explain why a heavier object released from the same height as a lighter object reaches the bottom with more kinetic energy. Include the role of potential energy and conservation of energy in your explanation.")
    ],
    "background_intro": "Energy transformation is one of the most fundamental concepts in physics. Every motion, every machine, every living process involves energy changing from one form to another. Understanding these transformations and the law of conservation of energy is essential for engineering, technology, and understanding the natural world.",
    "background_sections": [
        ("Potential and Kinetic Energy", "Gravitational potential energy depends on two factors: mass and height (PE = mgh, where m is mass, g is gravitational acceleration at 9.8 m/s², and h is height). Kinetic energy depends on mass and speed (KE = ½mv²). As an object falls, height decreases (PE drops) while speed increases (KE rises). The conversion is continuous and predictable."),
        ("The Conservation Law", "The law of conservation of energy states that energy cannot be created or destroyed — only transformed. In a closed system, total energy remains constant. This law was established through the work of James Joule, Hermann von Helmholtz, and Julius Robert von Mayer in the 1840s. It is one of the most fundamental laws of physics and has never been violated."),
        ("Friction and Thermal Energy", "Friction is not an energy-destroyer but an energy-transformer. When surfaces rub together, kinetic energy converts to thermal energy (heat) at the molecular level. The 'lost' energy is actually in the form of faster-vibrating molecules at the contact surfaces. This is why rubbing your hands together makes them warm. In engineering, friction is managed, not eliminated."),
        ("Real-World Energy Chains", "A car engine converts chemical energy (gasoline) to thermal energy (combustion) to kinetic energy (motion) — with inevitable losses to heat and sound at each step. A hydroelectric dam converts gravitational PE (water at height) to KE (falling water) to electrical energy (generator). Every energy system is a chain of transformations governed by conservation.")
    ],
    "lever_L": "Students identify height, mass, potential energy, kinetic energy, and thermal energy as system components.",
    "lever_E": "Students determine that height and mass both positively affect potential energy, PE converts to KE as objects fall, and friction converts KE to thermal energy.",
    "lever_V": "Students build the energy transformation model showing PE → KE → Thermal while total energy remains constant.",
    "lever_Ev": "Students compare ideal (frictionless) vs. friction scenarios and verify that PE + KE + Thermal always equals the starting energy.",
    "lever_R": "Students add air resistance or elastic energy components to model more complex energy chains.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Roller coaster at peak height", "say": "Right now, this roller coaster has more energy than at any other point on the ride. How?", "do": "Show a roller coaster photo. Ask: Where is the energy stored?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we track energy as it transforms from stored to moving to heat.", "do": "Pre-teach 'potential' (stored, waiting) vs. 'kinetic' (moving, active).", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Where does the energy go?", "say": "If a ball slows down at the bottom of a ramp, where did the energy go? It can't just vanish.", "do": "Quick demo: roll a ball on a smooth surface vs. carpet. Where did the speed go?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll build a model to track every joule of energy from start to finish.", "do": "Preview that total energy will NEVER change — only its form.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Energy system components", "say": "Height and mass are our inputs. PE, KE, and thermal energy are the outputs.", "do": "Sort components. Discuss why height and mass are external (we set them).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Energy transformation arrows", "say": "Energy flows: PE becomes KE, KE becomes thermal. But the total never changes.", "do": "Map relationships. Draw the transformation chain. Highlight the conservation rule.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Energy bar graphs over time", "say": "Watch the bars trade places: PE shrinks, KE grows. Add friction — thermal appears.", "do": "Students predict bar graph changes. Run ideal vs. friction scenarios. Verify total stays constant.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Conservation of energy proof", "say": "Energy is the ultimate shape-shifter. It changes form but never amount.", "do": "Sum PE + KE + Thermal at multiple time points. They always equal the starting PE.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Efficient ramp design", "say": "Engineers fight friction every day. Design a ramp that delivers maximum KE to the bottom.", "do": "Teams design, test with model, and present. Compare efficiency ratings.", "time": "12 min"}
    ],
    "sort_reasoning": "Height and Mass are external because they are initial conditions set by the experimenter before the object begins moving. Potential Energy, Kinetic Energy, and Thermal Energy are internal because they change as a result of the object's motion and interactions — they are determined by the external inputs and the physics of energy transformation.",
    "relationships": [
        ("Height to Potential Energy", "POSITIVE (+)", "Greater height means more gravitational potential energy stored in the object (PE = mgh)."),
        ("Mass to Potential Energy", "POSITIVE (+)", "Greater mass means more gravitational potential energy at the same height (PE = mgh)."),
        ("Potential Energy to Kinetic Energy", "POSITIVE (+)", "As the object descends, stored potential energy transforms into kinetic energy of motion."),
        ("Kinetic Energy to Thermal Energy", "POSITIVE (+)", "Friction between the moving object and surfaces converts some kinetic energy into heat."),
        ("Thermal Energy to Kinetic Energy", "NEGATIVE (-)", "Energy lost to friction as heat reduces the kinetic energy available for motion — the object slows down.")
    ],
    "sim_answers": [
        ("Heavy vs. Light", "The heavier object (Mass at 90%) starts with much more Potential Energy at the same height than the lighter object (Mass at 20%). As both fall, the heavier one converts more PE to KE, arriving at the bottom with substantially more kinetic energy. Both obey conservation — total energy matches starting PE — but the heavier object simply started with more."),
        ("High Friction", "With heavy friction, the Thermal Energy line rises significantly as the object descends. The Kinetic Energy line is lower than in the ideal scenario because energy has been diverted to heat. But PE + KE + Thermal at any point STILL equals the starting PE. Conservation of energy is proven: no energy was lost, it just changed form.")
    ],
    "reflection_exemplars": [
        ("Why can't the second hill be taller?", "A roller coaster's first hill sets the total energy budget for the entire ride (PE at the top). Every subsequent hill must be shorter because some energy has been converted to thermal energy by friction and air resistance along the way. There isn't enough energy left to reach the original height. This is why the first hill is always the tallest."),
        ("If energy is conserved, why do machines waste energy?", "Machines don't violate conservation — they obey it perfectly. What we call 'wasted' energy is thermal energy generated by friction, sound, and vibration. A car engine converts about 25% of gasoline's chemical energy to motion and 75% to heat. The energy isn't lost — it's transformed into forms we can't easily use. Engineers work to minimize these 'unwanted' transformations.")
    ],
    "stem_intro": "Present the challenge: An engineering firm needs a gravity-powered delivery system. Packages must slide from a 3-meter-high shelf to a packing station at ground level with maximum speed. Your team designs the most energy-efficient ramp.",
    "stem_concepts": [
        ("Friction Coefficient", "A number that describes how 'grippy' two surfaces are — lower coefficient means less friction and less energy lost to heat."),
        ("Energy Efficiency", "The percentage of input energy that is converted to useful output energy. A 90% efficient system loses only 10% to heat."),
        ("Regenerative Systems", "Designs that capture 'wasted' energy (like heat) and convert it back to useful forms — used in hybrid car braking systems.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design minimizes friction through specific material choices, uses model evidence to calculate efficiency, and includes energy budget analysis"),
        ("Proficient (3)", "Design addresses friction reduction with reference to model data and includes efficiency measurement"),
        ("Developing (2)", "Design mentions reducing friction but lacks specific model evidence or efficiency calculations"),
        ("Beginning (1)", "Design doesn't connect to energy transformation concepts or model findings")
    ],
    "support": [
        "Provide energy bar graph templates for students to fill in at top, middle, and bottom positions",
        "Use physical ramp demonstrations with different surface materials to show friction effects",
        "Sentence frames: 'When height increases, potential energy __ because __'"
    ],
    "extensions": [
        "Calculate the exact PE, KE, and thermal energy values using PE = mgh and KE = ½mv² formulas",
        "Add air resistance to the model and test how aerodynamic shapes reduce drag losses",
        "Research regenerative braking in electric vehicles and explain how it recovers kinetic energy"
    ],
    "cross_curr": [
        ("Math", "Use PE = mgh and KE = ½mv² to calculate energy values and verify conservation at multiple points on a ramp"),
        ("ELA", "Write an explanation of energy conservation for a younger student using everyday examples like roller coasters and bicycles"),
        ("Social Studies", "Research how energy transformation efficiency affects technology development and economic decisions in different industries")
    ],
    "misconceptions": [
        ("Energy is used up or consumed", "Energy is NEVER used up — it transforms. When a ball 'loses' speed to friction, that kinetic energy becomes thermal energy in the surface. The total energy hasn't changed; it's just in a less useful form.", "Run the model and add PE + KE + Thermal at any point. It always equals the starting PE. Nothing was consumed."),
        ("Heavier objects fall faster", "In a vacuum (no air resistance), all objects fall at the same rate regardless of mass. Heavier objects have more PE and more KE, but they also need more force to accelerate. The effects cancel out. Mass affects energy, not fall rate.", "In the model, compare the KE of heavy vs. light objects. More KE, yes — but plot speed vs. time and they match (without friction)."),
        ("Friction destroys energy", "Friction transforms kinetic energy into thermal energy — it doesn't destroy it. The heat generated is real energy that warms the surfaces. In the model, adding friction reduces KE but adds exactly that much thermal energy. The total stays constant.", "Feel the ramp surface after a ball rolls down it repeatedly. It's slightly warmer — that's where the 'lost' kinetic energy went.")
    ]
}

L06 = {
    "id": "G08L2-L06",
    "title": "Genetic Mutations: When DNA Makes a Typo",
    "subtitle": "How UV Radiation and Cell Division Create Errors That Change Organisms",
    "ngss": "MS-LS3-1, MS-LS3-2",
    "ngss_desc": "Develop and use a model to describe why structural changes to genes (mutations) located on chromosomes may affect proteins and may result in harmful, beneficial, or neutral effects to the structure and function of the organism. Develop and use a model to describe why asexual reproduction results in offspring with identical genetic information and sexual reproduction results in offspring with genetic variation.",
    "big_question": "What happens when DNA copies itself and makes a mistake?",
    "objectives": [
        "Explain how UV radiation and cell division rate affect mutation frequency",
        "Model the relationship between mutations, protein function, and organism fitness",
        "Predict whether mutations are likely to be harmful, beneficial, or neutral",
        "Evaluate evidence for why mutations are the raw material for evolution"
    ],
    "vocabulary": [
        ("Mutation", "A change in the DNA sequence that alters the genetic instructions for building proteins"),
        ("Mutagen", "Any environmental factor, such as UV radiation or chemicals, that increases mutation frequency"),
        ("Protein Function", "The specific job a protein performs in the body, determined by its shape, which is determined by its gene"),
        ("Organism Fitness", "An organism's overall ability to survive and reproduce in its environment"),
        ("Gene Expression", "The process by which the information in a gene is used to produce a functional protein")
    ],
    "components": [
        ("UV Radiation Exposure", "Intensity of ultraviolet light hitting cells, which damages DNA", True),
        ("Cell Division Rate", "How frequently cells divide and copy their DNA", True),
        ("Mutation Frequency", "How often DNA copying errors occur per generation", False),
        ("Protein Function Change", "Whether mutations alter the shape and function of proteins", False),
        ("Organism Fitness", "Overall survival and reproduction ability of the organism", False)
    ],
    "think_about_it": "Every time a cell divides, it copies 3 billion letters of DNA. If UV radiation damages some of those letters, what happens to the proteins they code for?",
    "scenarios": [
        ("Normal Conditions", "Set UV Radiation and Cell Division Rate to moderate levels"),
        ("High UV Exposure", "Lock UV Radiation to 90% — simulating heavy sun exposure without protection"),
        ("Rapid Growth", "Set Cell Division Rate to 90% with moderate UV — simulating fast-growing tissue")
    ],
    "sim_scenarios": [
        ("Normal Conditions", "Moderate UV, moderate cell division", "What do you predict will happen to Mutation Frequency and Organism Fitness?"),
        ("High UV Exposure", "UV Radiation at 90%", "What do you predict will happen to Protein Function Change and Organism Fitness?"),
        ("Rapid Division", "Cell Division at 90%, moderate UV", "How does faster division affect Mutation Frequency compared to high UV?")
    ],
    "discoveries": [
        "UV radiation damages DNA by causing chemical changes to nucleotide bases",
        "Faster cell division means more DNA copying events, which means more chances for errors",
        "Most mutations are neutral — they don't significantly change protein function",
        "Harmful mutations are more common than beneficial ones, but rare beneficial mutations drive evolution",
        "Mutation frequency increases with BOTH UV exposure and cell division rate — the risks are additive"
    ],
    "answer": "DNA copying is remarkably accurate, but not perfect. UV radiation damages DNA bases, and every cell division is another chance for a copying error. These mutations change the instructions for building proteins, which can alter their function. Most mutations are neutral, some are harmful (like those causing cancer), and rarely, some are beneficial — providing the raw material for evolution!",
    "stem_title": "Design a Skin Cancer Prevention Campaign",
    "stem_mission": "Design an evidence-based public health campaign about UV exposure and skin cancer risk, using your model data to create clear, compelling messaging.",
    "stem_scenario": "A dermatology clinic has hired your team to create a skin cancer prevention campaign for teenagers. Your messaging must be based on scientific evidence from your mutation model, not scare tactics.",
    "stem_questions": [
        "What level of UV exposure significantly increases mutation frequency?",
        "Why are rapidly dividing cells (like skin cells) at higher risk?",
        "How can your model evidence make the campaign more convincing to teens?"
    ],
    "stem_design_qs": [
        "What key facts from your model will anchor the campaign messaging?",
        "How will you communicate risk without using scare tactics?",
        "What specific protective behaviors will your campaign recommend?",
        "How will you measure whether the campaign changes behavior?"
    ],
    "career": "Genetic Counselors and Molecular Biologists study how mutations affect health and disease, helping families understand genetic risks and developing new therapies. They earn $65,000-$110,000/year.",
    "images": {
        "cover": ("cover-genetic-mutations.png", "A photorealistic dramatic visualization of a DNA double helix with a glowing error section highlighted in red, molecular biology laboratory background with blue lighting, scientific and cinematic"),
        "landscape": ("landscape-genetic-mutations.png", "A photorealistic image of an Asian male 8th grade student (age 13-14) examining a DNA model kit with diverse classmates in a modern biology lab, wearing casual clothes, natural window light, focused expressions"),
        "modeling": ("modeling-genetic-mutations.png", "A photorealistic image of a Black female 8th grade student (age 13-14) at a laptop building a mutation frequency model, diverse classmates discussing results around the table, modern classroom with genetics posters"),
        "discussion": ("discussion-genetic-mutations.png", "A photorealistic image of a Latino male 8th grade student (age 13-14) asking a question about mutation types while classmates listen, teacher pointing to a projected protein diagram, bright modern classroom"),
        "stem": ("stem-genetic-mutations.png", "A photorealistic image of a White female 8th grade student (age 13-14) presenting a skin cancer prevention campaign poster with infographics and model data, diverse team supporting, modern classroom")
    },
    "pre_assessment": [
        "What is a mutation, and what causes one?",
        "Do you think most mutations are harmful, helpful, or have no effect? Why?",
        "How might UV light from the sun affect your DNA?",
        "Draw what you think happens to a protein when the gene coding for it has a mutation."
    ],
    "extend_components": [
        ("DNA Repair Mechanisms", "Cellular enzymes that detect and fix DNA damage before it becomes a permanent mutation"),
        ("Chemical Mutagen Exposure", "Chemicals in smoke, food, or the environment that damage DNA"),
        ("Cancer Risk", "The probability of uncontrolled cell growth caused by accumulated mutations in growth-control genes")
    ],
    "reflections": [
        "Why are most mutations neutral rather than harmful or beneficial?",
        "How does the model explain why skin cancer risk increases with sun exposure?",
        "If mutations are mostly harmful, why are they also considered the 'raw material for evolution'?",
        "Why might rapidly dividing cells (like skin, gut lining, and blood cells) have higher cancer risk?",
        "How does understanding mutation help explain why sunscreen is important, based on the model?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model showing how environmental and cellular factors affect mutation frequency and its consequences for organisms."),
        ("Disciplinary Core Idea", "LS3.A Inheritance of Traits", "Genes are located on chromosomes and can be altered by mutations, which may change the proteins they produce and affect organism traits."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify UV radiation and cell division rate as CAUSES of mutations, and protein function changes as EFFECTS that determine organism fitness.")
    ],
    "cast_items": [
        "Develop a model describing how structural changes to genes may affect protein function",
        "Use evidence to explain how mutations can be harmful, beneficial, or neutral",
        "Connect genetic variation from mutations to the mechanism of natural selection"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A mutation changes one amino acid in a protein. The organism shows no change in appearance or survival. Which type of mutation is this most likely to be?"),
        ("Constructed Response:", "Using evidence from your model, explain how UV radiation exposure and cell division rate both contribute to increased mutation frequency. Describe how these mutations can lead to changes in protein function and organism fitness.")
    ],
    "background_intro": "DNA is the instruction manual for building every protein in your body. When DNA is copied during cell division, errors can occur. Environmental factors like UV radiation increase these errors. Understanding mutations is essential for genetics, medicine, cancer research, and evolutionary biology.",
    "background_sections": [
        ("How Mutations Happen", "DNA replication is remarkably accurate — DNA polymerase makes approximately 1 error per billion base pairs copied. However, with 3 billion base pairs per cell and millions of cell divisions per day, errors accumulate. UV radiation causes thymine dimers (chemical bonds between adjacent bases) that can lead to incorrect bases being inserted during replication. Chemical mutagens, radiation, and viral infections also increase mutation rates."),
        ("Types of Mutations", "Point mutations change a single base pair. Insertions add extra bases. Deletions remove bases. Frameshift mutations (insertions or deletions) are often the most damaging because they shift the reading frame, changing every amino acid downstream. Chromosomal mutations involve large segments of DNA being duplicated, deleted, inverted, or translocated."),
        ("Effects on Proteins", "Since the DNA sequence determines the amino acid sequence of a protein, mutations can change the protein's shape and function. Silent mutations don't change the amino acid (due to redundancy in the genetic code). Missense mutations change one amino acid. Nonsense mutations create a premature stop signal, truncating the protein. About 70% of point mutations are neutral, 29% are harmful, and less than 1% are beneficial."),
        ("Mutations and Cancer", "Cancer occurs when mutations accumulate in genes that control cell growth (oncogenes and tumor suppressor genes). A single mutation usually isn't enough — cancer typically requires 5-10 mutations in critical genes over a lifetime. This is why cancer risk increases with age (more time for mutations to accumulate) and with UV exposure, smoking, or chemical exposure (more mutations per year).")
    ],
    "lever_L": "Students identify UV radiation exposure, cell division rate, mutation frequency, protein function change, and organism fitness as system components.",
    "lever_E": "Students determine that UV radiation and cell division rate both increase mutation frequency, mutations can change protein function, and protein changes affect organism fitness positively or negatively.",
    "lever_V": "Students build the mutation model showing how environmental and cellular inputs drive genetic changes that affect organisms.",
    "lever_Ev": "Students compare normal conditions, high UV, and rapid division scenarios to see how different factors affect mutation frequency and fitness.",
    "lever_R": "Students add DNA repair mechanisms or cancer risk to explore how organisms defend against and are harmed by mutations.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "DNA helix with error", "say": "Your body copies 3 billion letters of DNA every time a cell divides. What if it makes a typo?", "do": "Analogy: Copy a paragraph by hand 1,000 times. How many errors would you make?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we model what happens when DNA makes mistakes — and why it matters.", "do": "Pre-teach 'mutation' vs. 'mutagen' (the cause vs. the result).", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "When DNA makes a typo", "say": "Most mutations do nothing. Some cause disease. And rarely, some give an advantage. Let's model it.", "do": "Quick write: What do you think causes mutations? List everything you know.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll build a model connecting UV light and cell division to mutations to fitness.", "do": "Preview the chain from external inputs to organism-level effects.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Mutation system components", "say": "What causes mutations? What do mutations affect? Let's sort our components.", "do": "Guide sorting. Discuss why UV and cell division are external inputs.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Mutation pathway arrows", "say": "Both UV and fast division increase mutations. But the effects on fitness can go either way.", "do": "Map relationships. Discuss the +/- nature of protein function changes (can help OR hurt).", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "UV exposure and division rate scenarios", "say": "Let's crank up the UV and watch what happens. Then crank up division rate.", "do": "Students predict, then run. Compare how each input drives mutation frequency differently.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Mutation spectrum findings", "say": "Most mutations are duds. A few are dangerous. And very rarely, one helps. That's evolution's fuel.", "do": "Connect to cancer risk data. Discuss why sunscreen matters at the molecular level.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Prevention campaign design", "say": "Design a campaign that uses science — not scare tactics — to protect teens from UV damage.", "do": "Teams create evidence-based campaigns. Present and evaluate messaging effectiveness.", "time": "12 min"}
    ],
    "sort_reasoning": "UV Radiation Exposure and Cell Division Rate are external because they are inputs from outside the cell's genetic system — UV comes from the environment and cell division rate is set by growth signals. Mutation Frequency, Protein Function Change, and Organism Fitness are internal because they are consequences that result from DNA damage and copying errors.",
    "relationships": [
        ("UV Radiation Exposure to Mutation Frequency", "POSITIVE (+)", "More UV radiation causes more DNA damage (thymine dimers and base modifications), increasing the rate at which mutations occur during DNA replication."),
        ("Cell Division Rate to Mutation Frequency", "POSITIVE (+)", "Faster cell division means more DNA copying events, and each copy is another opportunity for errors. More copies = more mistakes."),
        ("Mutation Frequency to Protein Function Change", "POSITIVE (+)", "More mutations mean more chances that a gene's code is altered, producing a protein with a different shape and potentially different function."),
        ("Protein Function Change to Organism Fitness", "POSITIVE/NEGATIVE (+/-)", "Changed proteins can be harmful (disrupting vital functions), neutral (no significant effect), or rarely beneficial (providing new capabilities). The net effect depends on which proteins are affected and how."),
        ("Organism Fitness to Cell Division Rate", "POSITIVE (+)", "Healthier organisms with higher fitness maintain normal growth patterns and cell division. Reduced fitness can alter growth rates and tissue maintenance.")
    ],
    "sim_answers": [
        ("High UV Exposure", "When UV Radiation is locked at 90%, Mutation Frequency rises dramatically. Protein Function Change increases as more genes are affected. Organism Fitness gradually declines because harmful mutations outnumber beneficial ones — most protein changes disrupt normal function. This models why chronic sun exposure increases cancer risk over time."),
        ("Rapid Division", "When Cell Division Rate is set to 90% with moderate UV, Mutation Frequency also rises significantly because each division is an opportunity for copying errors. The effect is similar to high UV but through a different mechanism — more copying events rather than more DNA damage. This explains why rapidly dividing tissues like skin and gut lining are more prone to cancer.")
    ],
    "reflection_exemplars": [
        ("Why are most mutations neutral?", "The genetic code has built-in redundancy — multiple three-letter codons can code for the same amino acid. So many point mutations change the DNA sequence without changing the protein. Additionally, many mutations occur in non-coding regions of DNA that don't directly affect protein production. Only mutations that change a protein's critical active site or folding pattern tend to have noticeable effects."),
        ("How are mutations both dangerous and essential?", "Most individual mutations are neutral or harmful, which is why organisms have DNA repair mechanisms. But across an entire population over many generations, the rare beneficial mutation provides a new trait that natural selection can act on. Without mutations, there would be no genetic variation, and without variation, there would be no evolution. Mutations are evolution's raw material — dangerous to individuals but essential for species adaptation.")
    ],
    "stem_intro": "Present the challenge: A dermatology clinic wants to reach teenagers with a skin cancer prevention message. Teens often ignore warnings about sun exposure. Your campaign must use your mutation model data to create compelling, evidence-based messaging that resonates with a teen audience.",
    "stem_concepts": [
        ("SPF and UV Blocking", "Sunscreen SPF rating indicates how much UV radiation is blocked. SPF 30 blocks about 97% of UV-B rays. Higher SPF blocks slightly more."),
        ("DNA Repair Enzymes", "Cells have repair mechanisms (like photolyase and nucleotide excision repair) that fix UV-damaged DNA, but these systems can be overwhelmed by excessive exposure."),
        ("Cumulative Damage", "UV damage accumulates over a lifetime. Childhood sunburns significantly increase adult cancer risk because the mutations persist in skin cells.")
    ],
    "stem_eval": [
        ("Expert (4)", "Campaign uses specific model data, explains the mutation-cancer pathway clearly, includes actionable recommendations, and is designed to engage teens"),
        ("Proficient (3)", "Campaign references model evidence and includes at least two science-based prevention strategies"),
        ("Developing (2)", "Campaign mentions UV and skin cancer but lacks specific model data or clear scientific explanation"),
        ("Beginning (1)", "Campaign doesn't connect to mutation science or model findings")
    ],
    "support": [
        "Provide a visual DNA sequence showing before/after mutation with resulting protein change",
        "Use letter-substitution exercises to simulate mutation effects on a sentence",
        "Sentence frames: 'When UV radiation increases, mutation frequency __ because __'"
    ],
    "extensions": [
        "Research CRISPR gene editing and explain how scientists can now intentionally create specific mutations",
        "Add DNA repair mechanisms as a component and test how they buffer against mutation effects",
        "Compare mutation rates in organisms with very different lifespans and cell division rates"
    ],
    "cross_curr": [
        ("Math", "Calculate the probability of a specific mutation occurring given a known error rate per base pair and number of cell divisions"),
        ("ELA", "Write a scientific explanation of how a single mutation can lead to cancer, using evidence from the model and background reading"),
        ("Social Studies", "Research how different countries approach sun protection education and compare skin cancer rates across populations")
    ],
    "misconceptions": [
        ("Mutations are always harmful", "Most mutations are neutral — they don't change protein function due to genetic code redundancy. Only mutations that alter critical protein regions tend to be harmful. And rarely, mutations provide beneficial new functions that drive evolution.", "In the model, observe that Protein Function Change includes both positive and negative outcomes. Most of the time, fitness barely changes."),
        ("UV radiation causes mutations instantly", "UV radiation damages DNA by creating chemical modifications like thymine dimers. These become mutations only when the cell divides and copies the damaged DNA incorrectly. The damage is immediate, but the mutation happens during the next cell division.", "In the model, increase UV but set Cell Division to 0%. Mutations don't occur because the damaged DNA hasn't been copied yet."),
        ("You can feel mutations happening", "Mutations are molecular-level events — you cannot feel a single base pair change. Even mutations that cause disease often take years or decades to produce symptoms. Cancer from UV exposure typically develops 20-30 years after the initial DNA damage.", "Discuss: If you can't feel it, how do scientists detect mutations? (Gene sequencing, protein analysis, phenotype observation.)")
    ]
}

L07 = {
    "id": "G08L2-L07",
    "title": "Wave Properties: Amplitude, Frequency, and Speed",
    "subtitle": "How Energy and Medium Shape Every Wave in the Universe",
    "ngss": "MS-PS4-1, MS-PS4-2",
    "ngss_desc": "Use mathematical representations to describe a simple model for waves that includes how the amplitude of a wave is related to the energy in a wave. Develop and use a model to describe that waves are reflected, absorbed, or transmitted through various materials.",
    "big_question": "Why does a whisper sound different from a shout, and why does sound travel faster underwater?",
    "objectives": [
        "Explain how wave source energy affects amplitude and frequency",
        "Model the relationship between frequency and wavelength (inverse relationship)",
        "Predict how different media affect wave speed while preserving frequency",
        "Demonstrate the universal wave equation: speed = frequency x wavelength"
    ],
    "vocabulary": [
        ("Amplitude", "The height of a wave from its resting position — larger amplitude means more energy"),
        ("Frequency", "The number of wave cycles per second, measured in Hertz (Hz)"),
        ("Wavelength", "The distance between two consecutive wave peaks or troughs"),
        ("Wave Speed", "How fast a wave moves through a medium — determined by the medium's properties"),
        ("Medium", "The material a wave travels through, such as air, water, or solid metal")
    ],
    "components": [
        ("Wave Source Energy", "The amount of power or force creating the wave", True),
        ("Medium Type", "The material the wave travels through — air, water, or solid", True),
        ("Amplitude", "Wave height, representing energy — bigger waves carry more energy", False),
        ("Frequency", "How many wave cycles pass per second — determines pitch for sound, color for light", False),
        ("Wavelength", "Distance between wave peaks — inversely related to frequency", False)
    ],
    "think_about_it": "If you shout instead of whisper, which wave property changes — amplitude, frequency, or both? And when sound enters water from air, which properties change and which stay the same?",
    "scenarios": [
        ("Quiet Sound in Air", "Set Wave Source Energy to 20%, Medium Type to Air"),
        ("Loud Sound in Air", "Set Wave Source Energy to 90%, Medium Type to Air"),
        ("Sound Moving from Air to Water", "Keep Wave Source Energy steady, change Medium Type from Air to Water")
    ],
    "sim_scenarios": [
        ("Quiet vs. Loud", "Low energy vs. high energy in air", "What do you predict will happen to Amplitude and Frequency?"),
        ("Air to Water", "Same source energy, switch medium from air to water", "What do you predict will happen to Wave Speed and Wavelength?"),
        ("High Frequency", "High source energy in different media", "How does the inverse relationship between Frequency and Wavelength appear in the data?")
    ],
    "discoveries": [
        "More source energy increases amplitude (louder/brighter) and can increase frequency (higher pitch)",
        "Frequency and wavelength have an inverse relationship — higher frequency means shorter wavelength",
        "When a wave enters a new medium, its speed changes but its frequency stays the same",
        "The wavelength adjusts to match the new speed while maintaining the original frequency",
        "The wave equation v = f x lambda (speed = frequency x wavelength) holds true in every medium"
    ],
    "answer": "A whisper has small amplitude (low energy) while a shout has large amplitude (high energy) — both can have the same frequency (pitch). Sound travels faster in water because water molecules are closer together and transmit vibrations more efficiently. When a wave enters a denser medium, speed increases but frequency stays the same — wavelength stretches to compensate. This relationship (speed = frequency x wavelength) is universal for all waves!",
    "stem_title": "Design a Sonar Detection System",
    "stem_mission": "Design a sonar system that uses wave properties to detect underwater objects at different depths, using your model data to select the optimal frequency and energy settings.",
    "stem_scenario": "A marine research team needs a sonar system for their submarine. They need to detect objects at various depths in the ocean. Your team must determine the best wave frequency, amplitude, and medium considerations for their detection system.",
    "stem_questions": [
        "What frequency gives the best resolution for detecting small objects?",
        "How does water depth affect the wave properties you need?",
        "What is the trade-off between high-frequency (detail) and low-frequency (range) sonar?"
    ],
    "stem_design_qs": [
        "What wave frequency will your system use and why?",
        "How will amplitude affect detection range?",
        "How will you account for wave speed changes in different water temperatures?",
        "How will you calculate the distance to a detected object using wave speed and return time?"
    ],
    "career": "Acoustical Engineers and Wave Physicists design systems that use wave properties for applications ranging from medical ultrasound to earthquake detection to concert hall design. They earn $70,000-$120,000/year.",
    "images": {
        "cover": ("cover-wave-properties.png", "A photorealistic dramatic visualization of ocean waves in cross-section showing amplitude, wavelength, and frequency labels, with sunlight refracting through the water, cinematic scientific illustration style"),
        "landscape": ("landscape-wave-properties.png", "A photorealistic image of a White male 8th grade student (age 13-14) using a wave generator machine on a ripple tank while diverse classmates observe wave patterns, modern physics lab, natural lighting"),
        "modeling": ("modeling-wave-properties.png", "A photorealistic image of a Latino female 8th grade student (age 13-14) at a laptop graphing wave properties while diverse classmates compare frequency and wavelength data, modern classroom with wave and sound posters"),
        "discussion": ("discussion-wave-properties.png", "A photorealistic image of a Black male 8th grade student (age 13-14) drawing wave diagrams on a whiteboard showing amplitude and wavelength, diverse engaged classmates, teacher facilitating, bright classroom"),
        "stem": ("stem-wave-properties.png", "A photorealistic image of an Asian female 8th grade student (age 13-14) presenting a sonar system design poster with wave property calculations, diverse team supporting, modern classroom setting")
    },
    "pre_assessment": [
        "What is a wave, and can you name different types of waves?",
        "What is the difference between a loud sound and a quiet sound at the wave level?",
        "Does sound travel faster in air or water? Why do you think so?",
        "Draw a wave and label any properties you know (amplitude, wavelength, frequency)."
    ],
    "extend_components": [
        ("Energy Carried", "The total energy transported by the wave, related to both amplitude and frequency"),
        ("Reflection Percentage", "How much of the wave bounces back when it hits a boundary between media"),
        ("Absorption Rate", "How much wave energy is converted to heat as it passes through a medium")
    ],
    "reflections": [
        "Why does sound seem different underwater compared to in air?",
        "How does the inverse relationship between frequency and wavelength help explain why radio waves are long but gamma rays are short?",
        "Why does frequency stay the same when a wave enters a new medium, but speed and wavelength change?",
        "How does amplitude relate to the energy of a wave? What real-world evidence supports this?",
        "How could understanding wave properties help in designing earthquake-resistant buildings?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model relating wave source energy and medium type to amplitude, frequency, wavelength, and wave speed."),
        ("Disciplinary Core Idea", "PS4.A Wave Properties", "A simple wave has a repeating pattern with a specific wavelength, frequency, and amplitude. The relationship between these properties is described by the wave equation."),
        ("Crosscutting Concept", "Patterns", "Students identify the mathematical pattern of the inverse relationship between frequency and wavelength, and the consistent pattern of speed = frequency x wavelength across all media.")
    ],
    "cast_items": [
        "Use mathematical representations to describe wave amplitude and energy relationships",
        "Develop a model showing how waves interact with different materials",
        "Apply the wave equation to predict changes in wavelength when waves enter new media"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A sound wave with a frequency of 440 Hz travels through air at 343 m/s. When the same sound enters water, its speed increases to 1,480 m/s. What happens to the frequency and wavelength of the wave?"),
        ("Constructed Response:", "Using evidence from your model, explain the relationship between amplitude, frequency, and wavelength. Include how changing the wave source energy affects these properties and what happens when a wave moves from one medium to another.")
    ],
    "background_intro": "Waves are one of the fundamental ways energy travels through the universe. Sound, light, ocean waves, earthquakes, and radio signals are all waves. Understanding wave properties — amplitude, frequency, wavelength, and speed — reveals the mathematical relationships that govern all wave behavior.",
    "background_sections": [
        ("Wave Anatomy", "Every wave has four measurable properties: amplitude (height from rest position), wavelength (distance between peaks), frequency (cycles per second, measured in Hz), and speed (distance traveled per second). Amplitude determines how much energy the wave carries. Frequency determines the wave's character — pitch for sound, color for light. Wavelength and frequency are inversely related."),
        ("The Universal Wave Equation", "The relationship v = f x lambda (speed = frequency x wavelength) is universal — it applies to all waves in all media. If you know any two of these three quantities, you can calculate the third. This equation is one of the most powerful and widely used relationships in all of physics."),
        ("Waves and Media", "Wave speed depends on the medium. Sound travels at 343 m/s in air, 1,480 m/s in water, and 5,960 m/s in steel. When a wave enters a new medium, its speed changes but its frequency stays the same (because the source is still vibrating at the same rate). Wavelength must adjust to maintain the equation v = f x lambda. Faster speed with same frequency means longer wavelength."),
        ("Energy and Amplitude", "A wave's energy is proportional to the square of its amplitude. Doubling the amplitude quadruples the energy. This is why a small increase in earthquake magnitude (which relates to wave amplitude) represents a massive increase in energy. The Richter scale is logarithmic — each whole number increase represents about 31.6 times more energy.")
    ],
    "lever_L": "Students identify wave source energy, medium type, amplitude, frequency, and wavelength as system components.",
    "lever_E": "Students determine that source energy positively affects amplitude and frequency, medium type affects wave speed, and frequency and wavelength have an inverse relationship.",
    "lever_V": "Students build the wave property model showing how inputs affect wave characteristics and demonstrating the wave equation.",
    "lever_Ev": "Students compare quiet vs. loud waves and waves in different media to verify the wave equation holds in all scenarios.",
    "lever_R": "Students add energy carried or reflection percentage to model more complex wave interactions.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Wave cross-section visualization", "say": "Every sound you hear, every color you see, every earthquake — they're all waves. Let's decode them.", "do": "Play a low-pitch and high-pitch tone. Ask: What's different about these two sounds?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we model the math behind every wave in the universe.", "do": "Pre-teach amplitude (height), frequency (speed of vibration), wavelength (distance between peaks).", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why whispers and shouts sound different", "say": "Why does a whisper feel different from a shout? And why does sound change underwater?", "do": "Quick demo: speak normally, then whisper, then shout. What changed physically?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model how energy and medium shape wave behavior.", "do": "Preview the universal wave equation as the 'punchline' of the lesson.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Wave system components", "say": "What can we control? Energy and medium. What responds? Amplitude, frequency, wavelength.", "do": "Sort components. Introduce the idea that some properties are mathematically linked.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Wave property relationships", "say": "Here's the key: frequency and wavelength are inversely related. When one goes up, the other goes down.", "do": "Map relationships. Highlight the inverse connection — this is the most important pattern.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Wave property graphs in different media", "say": "Watch what happens when we change the medium. Speed changes, frequency stays. What adjusts?", "do": "Students predict before running. Focus on wavelength adjusting to maintain v = f x lambda.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Wave equation proof", "say": "Speed equals frequency times wavelength. This works for sound, light, ocean waves — everything.", "do": "Calculate v = f x lambda using the simulation data. Verify it works in every scenario.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Sonar system design", "say": "Design a sonar system for a submarine. What frequency and energy do you need? The math will tell you.", "do": "Teams design sonar specifications using wave equation calculations. Present and defend.", "time": "12 min"}
    ],
    "sort_reasoning": "Wave Source Energy and Medium Type are external because they are inputs that the experimenter or environment controls — how much energy drives the wave and what material it travels through. Amplitude, Frequency, and Wavelength are internal because they are wave properties that result from and respond to those external inputs.",
    "relationships": [
        ("Wave Source Energy to Amplitude", "POSITIVE (+)", "More energy from the source creates larger wave amplitude — louder sounds, brighter light, taller ocean waves."),
        ("Wave Source Energy to Frequency", "POSITIVE (+)", "More energy can drive higher-frequency oscillations — though frequency is primarily set by the source mechanism."),
        ("Medium Type to Wave Speed", "POSITIVE/NEGATIVE (+/-)", "Denser media generally increase wave speed for mechanical waves (sound in water is faster than in air) because particles are closer together and transmit vibrations more efficiently."),
        ("Frequency to Wavelength", "NEGATIVE (-)", "Frequency and wavelength are inversely related. Higher frequency waves have shorter wavelengths. This is the core mathematical relationship: if v is constant, then lambda = v/f."),
        ("Amplitude to Energy Carried", "POSITIVE (+)", "Larger amplitude waves carry more energy. Energy is proportional to the square of amplitude — doubling amplitude quadruples the energy carried.")
    ],
    "sim_answers": [
        ("Quiet vs. Loud", "When Wave Source Energy increases from 20% to 90%, Amplitude increases dramatically — the waves are taller and carry much more energy. Frequency can also increase, meaning the wave oscillates faster. Wavelength decreases to maintain the wave equation (speed = frequency x wavelength). The key takeaway: louder/brighter means more amplitude and energy."),
        ("Air to Water", "When Medium Type switches from Air to Water with the same source, Wave Speed increases significantly (from 343 m/s to 1,480 m/s for sound). Frequency stays the SAME because the source is still vibrating at the same rate. To maintain v = f x lambda, Wavelength must increase proportionally. The wave stretches out — same frequency, faster speed, longer wavelength.")
    ],
    "reflection_exemplars": [
        ("Why does frequency stay the same in a new medium?", "Frequency is determined by the SOURCE, not the medium. If a tuning fork vibrates at 440 Hz, it pushes air molecules 440 times per second. When those vibrations reach water, the water molecules also vibrate 440 times per second — they're being driven by the same source. What changes is how FAST those vibrations travel through the medium and how far apart the peaks are (wavelength). The source sets the frequency; the medium sets the speed; wavelength adjusts."),
        ("How does amplitude relate to energy with real-world evidence?", "A gentle ocean wave barely moves a surfboard, but a tsunami (enormous amplitude) can destroy entire cities. Both are water waves with similar wavelengths and frequencies, but the tsunami's amplitude is orders of magnitude larger, meaning it carries vastly more energy. In earthquakes, a magnitude 7 quake releases about 31.6 times more energy than a magnitude 6 — because the relationship between amplitude and energy is exponential, not linear.")
    ],
    "stem_intro": "Present the scenario: A marine research submarine needs sonar to map the ocean floor and detect underwater objects. Different depths and water conditions require different sonar settings. Your team must determine the optimal wave properties for the detection system.",
    "stem_concepts": [
        ("Sonar Resolution", "Higher-frequency sonar detects smaller objects with more detail, but high-frequency waves are absorbed more quickly and have shorter range."),
        ("Echo Timing", "Distance to an object equals (wave speed x round-trip time) / 2. Knowing wave speed in the medium is essential for accurate distance calculation."),
        ("Frequency-Range Trade-off", "Low-frequency sonar travels farther but provides less detail. High-frequency sonar provides fine detail but is absorbed quickly. The choice depends on whether you need range or resolution.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design uses the wave equation to calculate specific frequency and wavelength values, addresses the frequency-range trade-off, and includes distance calculations"),
        ("Proficient (3)", "Design selects appropriate frequency based on model data and explains the medium's effect on wave speed"),
        ("Developing (2)", "Design mentions sonar properties but doesn't apply the wave equation or model evidence"),
        ("Beginning (1)", "Design doesn't connect to wave property concepts or model findings")
    ],
    "support": [
        "Provide slinky or rope demonstrations to physically show amplitude, frequency, and wavelength",
        "Use graphing paper templates for students to draw waves with labeled properties",
        "Sentence frames: 'When wave source energy increases, amplitude __ because __'"
    ],
    "extensions": [
        "Calculate the wavelength of different musical notes using v = f x lambda and the speed of sound in air",
        "Add reflection and absorption components to model how sonar and ultrasound work",
        "Research how earthquake P-waves and S-waves differ in speed, medium requirements, and what they reveal about Earth's interior"
    ],
    "cross_curr": [
        ("Math", "Use the wave equation v = f x lambda to calculate unknown values in problems involving sound waves in different media"),
        ("ELA", "Write a technical explanation of how sonar works for a general audience, using wave property concepts and the wave equation"),
        ("Social Studies", "Research how understanding wave properties led to technologies like radio, ultrasound, and earthquake early warning systems, and their societal impact")
    ],
    "misconceptions": [
        ("Louder sounds have higher frequency", "Loudness and pitch are independent properties. Loudness relates to AMPLITUDE (wave height), while pitch relates to FREQUENCY (vibrations per second). You can whisper a high note or shout a low note — amplitude and frequency are separate.", "In the model, increase only amplitude while keeping frequency constant. The wave gets taller but doesn't oscillate faster. Loudness changed, pitch didn't."),
        ("Sound travels at the same speed everywhere", "Sound speed depends entirely on the medium. In air, sound travels at about 343 m/s. In water, it's 1,480 m/s. In steel, 5,960 m/s. The density and elasticity of the medium determine how fast vibrations propagate.", "In the model, switch Medium Type while keeping source energy constant. Wave Speed changes dramatically while Frequency stays the same."),
        ("Waves carry matter from one place to another", "Waves carry ENERGY, not matter. The particles in the medium oscillate back and forth but stay in place — they don't travel with the wave. A cork floating on ocean waves bobs up and down but doesn't move toward shore. The wave pattern moves, not the water.", "Watch a wave in a slinky — the coils move back and forth, but they return to their starting position. The PULSE moves down the slinky; the COILS stay put.")
    ]
}

L08 = {
    "id": "G08L2-L08",
    "title": "Why Is Gold So Different from Iron?",
    "subtitle": "How Atomic Structure Determines the Properties of Every Material",
    "ngss": "MS-PS1-1, MS-PS1-3",
    "ngss_desc": "Develop models to describe the atomic composition of simple molecules and extended structures. Gather and make sense of information to describe that synthetic materials come from natural resources and impact society.",
    "big_question": "Why do two elements made of the same basic particles — protons, neutrons, and electrons — behave so differently?",
    "objectives": [
        "Explain how atomic number determines an element's identity and position on the periodic table",
        "Model how electron configuration affects an element's reactivity and bonding behavior",
        "Predict material properties like conductivity and reactivity based on atomic structure",
        "Compare how differences at the atomic level produce dramatically different macroscopic properties"
    ],
    "vocabulary": [
        ("Atomic Number", "The number of protons in an atom's nucleus, which defines the element and its place on the periodic table"),
        ("Electron Configuration", "The arrangement of electrons in energy levels (shells) around the nucleus, which determines how an element bonds"),
        ("Reactivity", "How readily an element undergoes chemical reactions — determined by how easily it gains, loses, or shares electrons"),
        ("Conductivity", "The ability of a material to transmit electrical current or heat, related to how freely electrons move"),
        ("Material Properties", "Observable characteristics of a substance — such as color, hardness, melting point, and luster — that result from its atomic structure")
    ],
    "components": [
        ("Atomic Number", "The number of protons defining the element — sets identity and electron count", True),
        ("Electron Configuration", "How electrons are arranged in energy levels — determines bonding and reactivity", True),
        ("Reactivity", "How readily the element undergoes chemical reactions with other substances", False),
        ("Conductivity", "How well the element transmits electricity and heat", False),
        ("Material Properties", "Observable traits like color, luster, hardness, and melting point", False)
    ],
    "think_about_it": "Gold has 79 protons and iron has 26. Both are metals, both conduct electricity, but gold barely reacts with anything while iron rusts easily. What about their electron arrangement explains this?",
    "scenarios": [
        ("Compare Gold and Iron", "Set Atomic Number to 79 (gold) vs. 26 (iron) and observe differences in Reactivity and Conductivity"),
        ("Highly Reactive Metal", "Set Electron Configuration to 1 outer electron (like sodium) and observe high Reactivity"),
        ("Noble Gas Stability", "Set Electron Configuration to a full outer shell (like neon) and observe near-zero Reactivity")
    ],
    "sim_scenarios": [
        ("Gold vs. Iron", "Atomic Number 79 vs. 26", "What do you predict will happen to Reactivity for each element?"),
        ("Alkali Metal", "1 outer electron configuration", "What do you predict will happen to Reactivity and Conductivity?"),
        ("Full Outer Shell", "Complete electron shell configuration", "What do you predict will happen to Reactivity?")
    ],
    "discoveries": [
        "Atomic number determines the element's identity — change the proton count and you change the element entirely",
        "Electron configuration, especially the outermost shell, determines how an element bonds and reacts",
        "Elements with nearly full or nearly empty outer shells are the most reactive",
        "Elements with full outer shells (noble gases) are extremely stable and barely react",
        "Conductivity depends on how freely outer electrons can move — metals with loosely held electrons conduct well"
    ],
    "answer": "Gold and iron are so different because their electron configurations produce different reactivities and material properties. Iron has electrons that readily interact with oxygen and water, causing rust. Gold's electrons are held in a configuration that resists chemical reactions — its outer electrons are tightly bound due to relativistic effects from its large nucleus. Both conduct electricity because they are metals with mobile outer electrons, but their chemical behavior is worlds apart because of how those electrons are arranged.",
    "stem_title": "Design a Material Selection Guide",
    "stem_mission": "Design an evidence-based guide that recommends the best element or alloy for specific engineering applications, using your model data on atomic properties to justify each recommendation.",
    "stem_scenario": "An engineering company needs to select materials for three products: electrical wiring, a corrosion-resistant ship hull, and a lightweight aircraft frame. Your team must recommend materials based on conductivity, reactivity, and material properties.",
    "stem_questions": [
        "Why is copper used for wiring instead of gold, even though gold conducts well?",
        "What atomic properties make a material resistant to corrosion?",
        "How do you balance conductivity, weight, and cost when selecting materials?"
    ],
    "stem_design_qs": [
        "What specific atomic properties does each application require?",
        "How does reactivity affect the long-term durability of each material?",
        "What trade-offs exist between conductivity, cost, and corrosion resistance?",
        "How will you use model evidence to justify each material recommendation?"
    ],
    "career": "Materials Scientists and Metallurgical Engineers study how atomic structure determines material properties and design new materials for technology, medicine, and construction. They earn $75,000-$130,000/year.",
    "images": {
        "cover": ("cover-gold-vs-iron.png", "A photorealistic dramatic split image showing a gleaming gold bar on one side and a rusty iron chain on the other, with atomic structure diagrams subtly overlaid, cinematic lighting"),
        "landscape": ("landscape-gold-vs-iron.png", "A photorealistic image of a Black female 8th grade student (age 13-14) examining metal samples with a conductivity tester while diverse classmates record data, modern chemistry lab, natural lighting"),
        "modeling": ("modeling-gold-vs-iron.png", "A photorealistic image of an Asian male 8th grade student (age 13-14) at a laptop comparing periodic table data for gold and iron, diverse classmates collaborating, modern classroom with periodic table poster"),
        "discussion": ("discussion-gold-vs-iron.png", "A photorealistic image of a Latino male 8th grade student (age 13-14) pointing at electron configuration diagrams on a whiteboard explaining reactivity differences, diverse engaged classmates, bright modern classroom"),
        "stem": ("stem-gold-vs-iron.png", "A photorealistic image of a White female 8th grade student (age 13-14) presenting a material selection poster with property comparisons, diverse team supporting, modern classroom setting")
    },
    "pre_assessment": [
        "What makes one element different from another at the atomic level?",
        "Why do some metals rust easily while others stay shiny for centuries?",
        "What is an electron, and how might its position in an atom affect the atom's behavior?",
        "Draw a simple atom and label the protons, neutrons, and electrons. How might adding more protons change the element?"
    ],
    "extend_components": [
        ("Melting Point", "The temperature at which a solid becomes a liquid — related to the strength of bonds between atoms"),
        ("Electronegativity", "How strongly an atom attracts electrons in a chemical bond — affects bonding type and reactivity"),
        ("Density", "Mass per unit volume — heavier atoms and tighter packing increase density")
    ],
    "reflections": [
        "Why is gold so valued throughout human history — is it just appearance, or do its atomic properties play a role?",
        "How does the periodic table organize elements by atomic structure, and what patterns emerge?",
        "Why are noble gases so unreactive while alkali metals are so reactive?",
        "How does understanding electron configuration help engineers choose materials for specific jobs?",
        "If you could design a new element with custom properties, what electron configuration would you choose and why?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model relating atomic number and electron configuration to macroscopic material properties like reactivity and conductivity."),
        ("Disciplinary Core Idea", "PS1.A Structure and Properties of Matter", "Each pure substance has characteristic physical and chemical properties that can be used to identify it. Substances are made from different types of atoms, which combine in various ways."),
        ("Crosscutting Concept", "Structure and Function", "Students connect the invisible structure of atoms (electron configuration) to the visible function and behavior of materials (conductivity, reactivity, material properties).")
    ],
    "cast_items": [
        "Develop models describing atomic composition and how it relates to material properties",
        "Gather and interpret information about how atomic structure determines element behavior",
        "Use evidence from the periodic table to predict properties of unfamiliar elements"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Element X has 11 protons and 1 electron in its outermost shell. Element Y has 18 protons and a completely full outermost shell. Which element is more likely to react violently with water, and why?"),
        ("Constructed Response:", "Using evidence from your model, explain why gold (atomic number 79) resists corrosion while iron (atomic number 26) rusts easily. Include the role of electron configuration in your explanation.")
    ],
    "background_intro": "The periodic table organizes all known elements by their atomic structure, revealing patterns in properties that scientists have used for over 150 years. Understanding why gold resists corrosion while iron rusts, or why copper conducts electricity better than wood, requires looking at the atomic level — specifically at how electrons are arranged.",
    "background_sections": [
        ("Atomic Number and Identity", "Every element is defined by its atomic number — the number of protons in its nucleus. Hydrogen has 1, carbon has 6, iron has 26, gold has 79. Change the proton count and you change the element entirely. The atomic number also determines how many electrons surround the nucleus in a neutral atom, which in turn determines all chemical behavior."),
        ("Electron Configuration and Reactivity", "Electrons occupy energy levels (shells) around the nucleus. The outermost shell determines reactivity. Atoms 'want' full outer shells — those with nearly empty outer shells (alkali metals like sodium) easily lose electrons, while those with nearly full shells (halogens like chlorine) easily gain electrons. Both are highly reactive. Noble gases already have full shells and barely react at all."),
        ("Why Gold Resists Corrosion", "Gold is special among metals. Its large nucleus (79 protons) creates such a strong pull that inner electrons move at a significant fraction of the speed of light, causing relativistic effects that contract the inner shells and alter the outer electron energies. This makes gold's outer electrons unusually stable and resistant to chemical reactions — which is why gold jewelry from ancient Egypt still gleams today."),
        ("Conductivity and Electron Mobility", "Metals conduct electricity because their outer electrons are loosely held and can flow freely through the material like a 'sea of electrons.' Silver is the best conductor, followed by copper, then gold. The arrangement and binding energy of outer electrons determine how freely they move. Non-metals hold their electrons tightly, making them poor conductors (insulators).")
    ],
    "lever_L": "Students identify atomic number, electron configuration, reactivity, conductivity, and material properties as system components.",
    "lever_E": "Students determine that atomic number sets identity, electron configuration drives reactivity and conductivity, and these atomic-level factors produce observable material properties.",
    "lever_V": "Students build the atomic property model showing how atomic number and electron configuration determine reactivity, conductivity, and material properties.",
    "lever_Ev": "Students compare elements with different atomic numbers and electron configurations to verify that outer-shell electrons predict reactivity and conductivity patterns.",
    "lever_R": "Students add melting point, electronegativity, or density to model more complex property relationships.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Gold bar vs. rusty iron", "say": "One of these has been treasured for 5,000 years. The other crumbles in the rain. Both are metals. Why?", "do": "Show gold and iron side by side. Ask: What makes them so different?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we go inside the atom to discover why elements behave so differently.", "do": "Pre-teach atomic number (identity), electron configuration (behavior), reactivity (chemical willingness).", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Gold vs. iron atomic diagrams", "say": "Both are made of protons, neutrons, and electrons. Same ingredients, wildly different results. Why?", "do": "Show atomic diagrams. Count the protons. Ask: Does more protons always mean more reactive?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model how atomic structure creates the material properties we observe.", "do": "Preview that electron arrangement is the key to everything.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Atomic structure components", "say": "Atomic number and electron configuration are our inputs. Reactivity, conductivity, and material properties are our outputs.", "do": "Sort components. Discuss why atomic number and electron config are external (they define the element).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Property relationship arrows", "say": "Electron configuration drives everything — reactivity, conductivity, and the properties we can see and touch.", "do": "Map relationships. Highlight that outer-shell electrons are the most important factor.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Element comparison data", "say": "Compare gold, iron, sodium, and neon. Watch how electron configuration predicts their behavior.", "do": "Students predict properties before running. Compare reactive vs. stable elements.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Periodic table patterns", "say": "The periodic table isn't random — it's organized by electron configuration, and properties follow predictable patterns.", "do": "Identify groups: alkali metals (reactive), noble gases (stable), transition metals (variable).", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Material selection engineering", "say": "Engineers choose materials based on atomic properties. Your turn — recommend the best material for each job.", "do": "Teams analyze applications, select materials using model evidence, and present recommendations.", "time": "12 min"}
    ],
    "sort_reasoning": "Atomic Number and Electron Configuration are external because they are inherent properties of the element that define its identity — they are the inputs that cannot change without changing the element itself. Reactivity, Conductivity, and Material Properties are internal because they are outcomes determined by those atomic-level inputs.",
    "relationships": [
        ("Atomic Number to Electron Configuration", "POSITIVE (+)", "More protons means more electrons in a neutral atom, filling additional energy levels and creating more complex configurations."),
        ("Electron Configuration to Reactivity", "POSITIVE/NEGATIVE (+/-)", "Elements with nearly empty or nearly full outer shells are highly reactive. Elements with full outer shells have near-zero reactivity. The relationship depends on how close the outer shell is to being full or empty."),
        ("Electron Configuration to Conductivity", "POSITIVE (+)", "Elements with loosely held outer electrons (metals) allow electron flow, creating high conductivity. Tightly held electrons (non-metals) resist flow."),
        ("Reactivity to Material Properties", "POSITIVE (+)", "High reactivity leads to observable properties like tarnishing, corrosion, or vigorous reactions with water and acids."),
        ("Conductivity to Material Properties", "POSITIVE (+)", "High conductivity correlates with metallic luster, malleability, and the ability to transmit heat — all observable material properties.")
    ],
    "sim_answers": [
        ("Gold vs. Iron", "Gold (atomic number 79) shows very low Reactivity due to its uniquely stable electron configuration — relativistic effects from its large nucleus make outer electrons resistant to bonding. Iron (atomic number 26) shows moderate-to-high Reactivity because its outer electrons readily interact with oxygen and water. Both show high Conductivity as metals, but their chemical stability is dramatically different."),
        ("Full Outer Shell", "With a complete outer electron shell (like neon or argon), Reactivity drops to near zero. The element has no 'need' to gain, lose, or share electrons because its configuration is already stable. This is why noble gases are called 'noble' — they don't easily combine with other elements. The model shows that electron satisfaction determines chemical behavior.")
    ],
    "reflection_exemplars": [
        ("Why is gold so valued throughout human history?", "Gold's value comes directly from its atomic properties. Its electron configuration makes it extremely resistant to corrosion — it doesn't rust, tarnish, or degrade over millennia. It's also beautiful (its color comes from relativistic electron effects absorbing blue light), malleable (easy to shape into jewelry and coins), and rare. Ancient cultures discovered through experience what atomic physics now explains: gold is one of the most chemically stable elements on Earth."),
        ("Why are noble gases so unreactive?", "Noble gases have completely full outer electron shells. Chemical reactions involve gaining, losing, or sharing electrons to achieve a full outer shell. Since noble gases already have this stable configuration, they have no driving force to react. It's like trying to fill a cup that's already full — there's no reason for the process to occur. This makes noble gases useful in situations where you need an inert (non-reactive) atmosphere, like protecting welds or filling lightbulbs.")
    ],
    "stem_intro": "Present the challenge: An engineering company is selecting materials for three products — electrical wiring, a ship hull that resists saltwater corrosion, and a lightweight aircraft frame. Your team must analyze atomic properties to recommend the best material for each application.",
    "stem_concepts": [
        ("Alloys", "Mixtures of two or more metals designed to combine desirable properties — steel is iron plus carbon for strength, stainless steel adds chromium for corrosion resistance."),
        ("Corrosion Resistance", "The ability of a material to withstand chemical attack from its environment. Low reactivity and protective oxide layers both contribute to corrosion resistance."),
        ("Cost-Performance Trade-off", "Gold conducts well and resists corrosion but is expensive and heavy. Copper conducts nearly as well at a fraction of the cost. Engineers balance performance with practical constraints.")
    ],
    "stem_eval": [
        ("Expert (4)", "Recommendations use specific atomic property data from the model, address trade-offs between properties, and include cost-performance analysis"),
        ("Proficient (3)", "Recommendations reference electron configuration and reactivity data with clear connections to application requirements"),
        ("Developing (2)", "Recommendations mention material properties but lack connection to atomic-level model evidence"),
        ("Beginning (1)", "Recommendations don't connect to atomic structure concepts or model findings")
    ],
    "support": [
        "Provide periodic table reference sheets with electron configuration diagrams for key elements",
        "Use physical metal samples (copper, aluminum, iron, zinc) for students to test conductivity and observe properties",
        "Sentence frames: 'Gold resists corrosion because its electron configuration __'"
    ],
    "extensions": [
        "Research why relativistic effects in gold's electrons cause its distinctive color and chemical stability",
        "Add electronegativity to the model and explore how it predicts bonding type (ionic vs. covalent)",
        "Design a new alloy by combining elements with complementary properties and predict its behavior using model evidence"
    ],
    "cross_curr": [
        ("Math", "Calculate the number of electrons in each shell for elements up to atomic number 36 using the 2n² rule and connect to periodic table periods"),
        ("ELA", "Write a persuasive argument for why a specific material should be used in a real-world engineering application, citing atomic property evidence"),
        ("Social Studies", "Research how the discovery of bronze (copper-tin alloy) and steel (iron-carbon alloy) transformed human civilizations and economies")
    ],
    "misconceptions": [
        ("All metals behave the same way", "Metals vary enormously in reactivity, conductivity, hardness, and other properties based on their atomic structure. Sodium explodes in water while gold sits in seawater for centuries unchanged. Mercury is a liquid at room temperature while tungsten doesn't melt until 3,422°C. Electron configuration explains these differences.", "In the model, compare sodium (1 outer electron), iron (variable outer electrons), and gold (stable outer electrons). Their Reactivity values are dramatically different despite all being metals."),
        ("Bigger atoms are always more reactive", "Reactivity depends on electron configuration, not size. Neon (10 protons) is completely unreactive because its outer shell is full, while sodium (11 protons, just one more) is explosively reactive because it has a single lonely outer electron. Size alone tells you nothing about reactivity.", "In the model, compare neon (full shell) and sodium (1 outer electron). Despite being neighbors on the periodic table and similar in size, their Reactivity is opposite."),
        ("Electrons orbit like planets around the sun", "Electrons don't travel in neat circular orbits. They exist in probability clouds (orbitals) — regions where they are likely to be found. The 'shell' model is a useful simplification for understanding energy levels and reactivity, but real electron behavior is described by quantum mechanics.", "The model uses energy levels (shells) as a simplification. Discuss that real atoms are more complex but the shell model accurately predicts reactivity patterns.")
    ]
}

L09 = {
    "id": "G08L2-L09",
    "title": "How Does a Cut Heal Itself?",
    "subtitle": "How Your Body Orchestrates Cell Division to Repair Damaged Tissue",
    "ngss": "MS-LS1-4, MS-LS1-2",
    "ngss_desc": "Use argument based on empirical evidence and scientific reasoning to support an explanation for how characteristic animal behaviors and specialized plant structures affect the probability of successful reproduction of animals and plants respectively. Develop and use a model to describe the function of a cell as a whole and ways the parts of cells contribute to the function.",
    "big_question": "How does your body know when you're injured, and how does it rebuild damaged tissue cell by cell?",
    "objectives": [
        "Explain how wound severity and blood supply affect the healing process",
        "Model the relationship between cell division rate and new tissue formation",
        "Predict how different wound conditions affect healing progress over time",
        "Evaluate evidence for why some wounds heal faster than others"
    ],
    "vocabulary": [
        ("Wound Severity", "The depth and extent of tissue damage — deeper wounds destroy more cells and take longer to heal"),
        ("Blood Supply", "The flow of blood to the wound area, delivering oxygen, nutrients, and immune cells needed for repair"),
        ("Cell Division Rate", "How quickly cells near the wound are dividing (mitosis) to produce new cells for repair"),
        ("New Tissue Formation", "The growth of replacement skin, blood vessels, and connective tissue to close and repair the wound"),
        ("Healing Progress", "The overall advancement of wound repair from initial injury to complete tissue restoration")
    ],
    "components": [
        ("Wound Severity", "The depth and area of tissue damage — sets the scale of repair needed", True),
        ("Blood Supply", "Blood flow to the wound area delivering oxygen, nutrients, and immune cells", True),
        ("Cell Division Rate", "How rapidly cells undergo mitosis to produce replacement cells", False),
        ("New Tissue Formation", "Growth of new skin, blood vessels, and connective tissue at the wound site", False),
        ("Healing Progress", "Overall wound closure and tissue restoration over time", False)
    ],
    "think_about_it": "A paper cut heals in a few days, but a deep gash might take weeks. Both involve the same process — cell division. What factors determine how fast your body can rebuild?",
    "scenarios": [
        ("Minor Cut", "Set Wound Severity to 20% and Blood Supply to 70% — a small, well-supplied wound"),
        ("Deep Wound", "Set Wound Severity to 90% and Blood Supply to 70% — a serious injury with normal blood flow"),
        ("Poor Circulation", "Set Wound Severity to 50% and Blood Supply to 20% — a moderate wound with limited blood flow")
    ],
    "sim_scenarios": [
        ("Minor vs. Deep", "Low severity vs. high severity with normal blood supply", "What do you predict will happen to Healing Progress over 14 days?"),
        ("Good vs. Poor Blood Supply", "Same wound severity with high vs. low blood supply", "What do you predict will happen to Cell Division Rate?"),
        ("Worst Case", "High severity with low blood supply", "What do you predict will happen to New Tissue Formation?")
    ],
    "discoveries": [
        "Wound severity determines the scale of repair needed — more damaged tissue requires more cell divisions to replace",
        "Blood supply is critical because dividing cells need oxygen and nutrients delivered by blood to fuel mitosis",
        "Cell division rate increases near the wound edge as the body signals cells to multiply faster",
        "New tissue formation follows cell division — first new cells are produced, then they organize into functional tissue",
        "Healing progress depends on both factors: severe wounds with good blood supply heal faster than moderate wounds with poor circulation"
    ],
    "answer": "Your body heals a cut through a carefully coordinated process. When tissue is damaged, chemical signals trigger nearby cells to increase their division rate (mitosis). Blood supply delivers the oxygen and nutrients these rapidly dividing cells need. New cells gradually fill the wound, forming new tissue. Wound severity sets the scale of the job, and blood supply determines how fast the workers can work. This is why diabetic patients (who often have poor circulation) heal slowly, and why keeping a wound clean and well-supplied with blood is essential for recovery.",
    "stem_title": "Design a Wound Treatment Protocol",
    "stem_mission": "Design an evidence-based wound treatment plan that optimizes healing conditions, using your model data to justify why each treatment step accelerates tissue repair.",
    "stem_scenario": "A school nurse needs a science-based protocol for treating different types of student injuries — from minor scrapes to deeper cuts. Your team must create treatment guidelines that maximize healing speed based on the biological factors in your model.",
    "stem_questions": [
        "How does keeping a wound moist vs. dry affect cell division rate?",
        "Why does elevating an injury help with healing?",
        "What role does nutrition play in providing fuel for cell division?"
    ],
    "stem_design_qs": [
        "What specific conditions optimize cell division rate at the wound site?",
        "How will your protocol address blood supply to the wound?",
        "What steps prevent infection, which would divert resources from healing?",
        "How will you use model evidence to explain each treatment recommendation?"
    ],
    "career": "Biomedical Researchers and Wound Care Specialists study how the body repairs itself and develop treatments that accelerate healing. They work in hospitals, research labs, and pharmaceutical companies, earning $65,000-$120,000/year.",
    "images": {
        "cover": ("cover-wound-healing.png", "A photorealistic dramatic microscopic view of skin tissue healing, showing layers of new cells forming over a wound, with cellular detail visible, cinematic scientific visualization"),
        "landscape": ("landscape-wound-healing.png", "A photorealistic image of a Latino male 8th grade student (age 13-14) examining cell division slides under a microscope while diverse classmates record observations, modern biology lab, natural lighting"),
        "modeling": ("modeling-wound-healing.png", "A photorealistic image of a Black female 8th grade student (age 13-14) at a laptop graphing healing rate data over time, diverse classmates collaborating, modern classroom with biology and cell division posters"),
        "discussion": ("discussion-wound-healing.png", "A photorealistic image of a White male 8th grade student (age 13-14) pointing at a diagram of wound healing stages on a whiteboard, diverse engaged classmates, teacher facilitating, bright modern classroom"),
        "stem": ("stem-wound-healing.png", "A photorealistic image of an Asian female 8th grade student (age 13-14) presenting a wound treatment protocol poster with healing data charts, diverse team supporting, modern classroom setting")
    },
    "pre_assessment": [
        "What happens when you get a cut? Describe what you think is happening inside your body.",
        "Why do some cuts heal faster than others?",
        "What is cell division, and why might it be important for healing?",
        "Draw a simple diagram showing what you think happens to the cells around a wound over time."
    ],
    "extend_components": [
        ("Immune Response", "White blood cells that fight infection at the wound site — infection diverts resources from repair"),
        ("Scar Tissue Formation", "Collagen-rich tissue that forms when wounds are too large for perfect regeneration"),
        ("Growth Factor Signaling", "Chemical signals released by damaged cells that trigger nearby cells to divide faster")
    ],
    "reflections": [
        "Why do wounds on the tongue or inside the mouth heal faster than wounds on the skin?",
        "How does the body 'know' when to stop dividing cells once a wound is healed?",
        "Why do older people generally heal more slowly than younger people?",
        "How does understanding wound healing connect to understanding cancer (uncontrolled cell division)?",
        "What would happen if cell division at a wound site never stopped?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model showing how wound severity and blood supply affect cell division rate, new tissue formation, and overall healing progress."),
        ("Disciplinary Core Idea", "LS1.B Growth and Development of Organisms", "Animals engage in characteristic behaviors and have specialized body structures that increase the probability of successful reproduction and survival, including wound repair through cell division."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify causal relationships between wound severity, blood supply, cell division rate, and healing outcomes — understanding that multiple causes interact to produce observed effects.")
    ],
    "cast_items": [
        "Use models to describe how cells contribute to the function of tissue repair",
        "Support explanations with empirical evidence about how cell division drives wound healing",
        "Develop arguments about why different wound conditions lead to different healing outcomes"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Patient A has a moderate cut on their well-supplied forearm. Patient B has the same cut on their lower leg, where circulation is reduced due to diabetes. After 10 days, which patient will show more healing progress, and what is the primary reason?"),
        ("Constructed Response:", "Using evidence from your model, explain why a deep wound with good blood supply might heal faster than a shallow wound with poor blood supply. Include the roles of cell division rate and new tissue formation in your explanation.")
    ],
    "background_intro": "The human body is a remarkable self-repairing system. Every cut, scrape, and bruise triggers a precisely orchestrated cascade of cellular events that rebuild damaged tissue. Understanding how wounds heal reveals fundamental principles of cell biology — particularly cell division (mitosis) and how the body regulates growth.",
    "background_sections": [
        ("The Four Phases of Wound Healing", "Healing occurs in four overlapping phases: (1) Hemostasis — blood clotting stops the bleeding within minutes. (2) Inflammation — immune cells flood the area to fight infection and clear debris (hours to days). (3) Proliferation — cells divide rapidly to rebuild tissue, forming new skin, blood vessels, and connective tissue (days to weeks). (4) Remodeling — new tissue is reorganized and strengthened (weeks to months or years)."),
        ("Cell Division: The Engine of Repair", "Mitosis is the process by which one cell divides into two identical daughter cells. At a wound site, cells at the edge receive chemical signals (growth factors) that trigger them to divide much faster than normal. These new cells migrate into the wound, gradually filling the gap. The rate of cell division depends heavily on blood supply — dividing cells consume enormous amounts of oxygen and nutrients."),
        ("Blood Supply: The Lifeline", "Blood delivers everything healing cells need: oxygen for cellular respiration (energy production), glucose and amino acids for building new cellular structures, growth factors that signal cells to divide, and white blood cells that fight infection. Areas with rich blood supply (face, tongue, scalp) heal remarkably fast. Areas with poor circulation (lower legs, feet) heal slowly — this is why diabetic foot wounds are a serious medical concern."),
        ("Why Some Wounds Scar", "Small wounds can regenerate tissue that is virtually identical to the original. Large or deep wounds cannot wait for perfect regeneration — they fill the gap quickly with collagen-rich scar tissue. Scars are functional but lack the full complexity of original tissue (no hair follicles, sweat glands, or normal pigmentation). The body prioritizes speed of closure over perfection of repair.")
    ],
    "lever_L": "Students identify wound severity, blood supply, cell division rate, new tissue formation, and healing progress as system components.",
    "lever_E": "Students determine that wound severity sets the repair scale, blood supply fuels cell division, and cell division produces new tissue that drives healing progress.",
    "lever_V": "Students build the wound healing model showing how inputs (severity and blood supply) affect the cascade of cell division, tissue formation, and healing.",
    "lever_Ev": "Students compare scenarios with different severity and blood supply levels to verify that blood supply is the rate-limiting factor for healing speed.",
    "lever_R": "Students add immune response, scar tissue formation, or growth factor signaling to model more complex healing dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Microscopic wound healing", "say": "Every time you get a cut, billions of cells launch a repair mission. How does your body rebuild itself?", "do": "Show microscopic wound healing image. Ask: What do you think happens in the first hour after a cut?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we model how your body heals wounds through cell division.", "do": "Pre-teach wound severity (how bad), blood supply (delivery system), cell division (copying cells).", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Paper cut vs. deep wound", "say": "A paper cut heals in days. A deep gash takes weeks. Same process, different timelines. Why?", "do": "Ask students to share experiences with cuts healing. What did they notice?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model the biological assembly line that rebuilds your tissue after injury.", "do": "Preview that healing is a cascade: severity sets the job, blood supply fuels the workers.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Healing system components", "say": "Wound severity and blood supply are our inputs. Cell division, tissue formation, and healing progress are outputs.", "do": "Sort components. Discuss why severity and blood supply are external (set by the injury and body).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Healing cascade arrows", "say": "Blood supply fuels cell division. Cell division produces new tissue. New tissue drives healing progress.", "do": "Map the cascade. Highlight that blood supply is the rate-limiting factor.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Healing progress graphs", "say": "Compare a minor cut with good blood supply vs. a deep wound with poor circulation. What happens?", "do": "Students predict healing curves. Run scenarios. Identify the critical role of blood supply.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Healing factors summary", "say": "Your body is an incredible self-repair system — but it needs fuel, time, and the right conditions.", "do": "Summarize key findings. Connect to real medical practice (wound care, diabetes management).", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Wound treatment protocol", "say": "You're the school nurse's science advisor. Design a treatment protocol backed by cell biology evidence.", "do": "Teams create evidence-based protocols. Present and defend with model data.", "time": "12 min"}
    ],
    "sort_reasoning": "Wound Severity and Blood Supply are external because they are conditions set by the injury and the body's circulatory system — they are inputs the healing process must work with. Cell Division Rate, New Tissue Formation, and Healing Progress are internal because they are biological responses that result from and are regulated by those external conditions.",
    "relationships": [
        ("Wound Severity to Cell Division Rate", "POSITIVE (+)", "More severe wounds trigger stronger chemical signals (growth factors) that increase the rate of cell division at the wound edge."),
        ("Wound Severity to Healing Progress", "NEGATIVE (-)", "Greater wound severity means more tissue to replace, requiring more time to achieve complete healing — deeper wounds heal more slowly."),
        ("Blood Supply to Cell Division Rate", "POSITIVE (+)", "Greater blood flow delivers more oxygen and nutrients to dividing cells, enabling faster mitosis and cell production."),
        ("Cell Division Rate to New Tissue Formation", "POSITIVE (+)", "Faster cell division produces more new cells per day, accelerating the formation of replacement tissue."),
        ("New Tissue Formation to Healing Progress", "POSITIVE (+)", "More new tissue filling the wound means greater healing progress — the wound closes and functional tissue is restored.")
    ],
    "sim_answers": [
        ("Minor vs. Deep", "The minor cut (20% severity) shows rapid Healing Progress, reaching near-complete healing within 5-7 days because fewer cells need replacement. The deep wound (90% severity) shows much slower progress — Cell Division Rate is high (strong growth factor signals), but the sheer volume of tissue to replace means full healing takes 3-4 weeks even with good blood supply."),
        ("Good vs. Poor Blood Supply", "With the same wound severity, good blood supply (70%) produces a significantly higher Cell Division Rate than poor blood supply (20%). Cells with adequate oxygen and nutrients divide rapidly, while oxygen-starved cells divide slowly. The poorly supplied wound shows much slower New Tissue Formation and delayed Healing Progress — this models why diabetic patients with poor circulation face chronic wound healing problems.")
    ],
    "reflection_exemplars": [
        ("Why do mouth wounds heal faster?", "The mouth has one of the richest blood supplies in the body — dense networks of blood vessels deliver abundant oxygen, nutrients, and growth factors to injured tissue. Additionally, saliva contains growth factors and antimicrobial compounds that support healing. In the model, this is equivalent to setting Blood Supply to near-maximum. High blood supply drives high Cell Division Rate, which accelerates New Tissue Formation and Healing Progress. The mouth's biological environment is optimized for rapid repair."),
        ("Connection between healing and cancer", "Normal wound healing involves controlled cell division — cells divide rapidly to fill the wound, then STOP when the tissue is repaired. Cancer occurs when this stop signal fails and cells continue dividing uncontrollably. In the model, imagine Cell Division Rate staying at maximum even after Healing Progress reaches 100%. The excess cells form a tumor. Understanding wound healing helps scientists understand cancer because both involve the same cellular machinery — mitosis — but cancer has lost the regulatory 'brakes.'")
    ],
    "stem_intro": "Present the scenario: The school nurse wants science-based treatment guidelines for different student injuries. Your team must create a protocol that optimizes healing conditions based on the biological factors in your wound healing model.",
    "stem_concepts": [
        ("Moist Wound Healing", "Research shows wounds heal up to 50% faster in a moist environment. Dry wounds form scabs that cells must dissolve before migrating — moist wounds allow cells to move freely and divide efficiently."),
        ("Infection and Healing", "Bacterial infection diverts immune cells and blood supply away from tissue repair toward fighting invaders. Keeping wounds clean is essential because infection dramatically slows cell division dedicated to healing."),
        ("Nutrition and Cell Division", "Cell division requires raw materials — proteins (amino acids), vitamins (especially C and A), and minerals (zinc). Malnourished patients heal significantly slower because their cells lack the building blocks for new tissue.")
    ],
    "stem_eval": [
        ("Expert (4)", "Protocol addresses all model factors (severity assessment, blood supply optimization, cell division support), includes evidence-based reasoning, and considers infection prevention"),
        ("Proficient (3)", "Protocol references blood supply and cell division rate with connections to treatment steps and model evidence"),
        ("Developing (2)", "Protocol mentions wound care steps but lacks biological reasoning from the model"),
        ("Beginning (1)", "Protocol doesn't connect to cell division or wound healing model concepts")
    ],
    "support": [
        "Provide wound healing timeline diagrams showing the four phases for reference",
        "Use time-lapse videos of wound healing under microscope to visualize cell division and tissue formation",
        "Sentence frames: 'Blood supply affects healing because dividing cells need __ to __'"
    ],
    "extensions": [
        "Research how growth factors are used in medical treatments to accelerate wound healing in burn patients",
        "Add immune response to the model and explore how infection delays healing by competing for blood supply",
        "Compare regeneration in humans (limited) vs. organisms like salamanders and starfish (extensive) — what makes them different?"
    ],
    "cross_curr": [
        ("Math", "Calculate healing rates (percentage of wound closed per day) for different scenarios and create graphs comparing healing curves"),
        ("ELA", "Write a patient education guide explaining the science of wound healing in accessible language for a hospital waiting room"),
        ("Social Studies", "Research how access to medical care and nutrition affects wound healing outcomes across different communities and socioeconomic groups")
    ],
    "misconceptions": [
        ("Scabs are the healing", "Scabs are blood clots that protect the wound, not the actual repair process. Real healing happens UNDERNEATH the scab as cells divide and form new tissue. In fact, keeping wounds moist (without a dry scab) often leads to faster healing because cells can migrate and divide more easily without having to dissolve dried material.", "In the model, healing progress tracks new tissue formation, not scab formation. The scab is a temporary protective barrier, not the repair itself."),
        ("Wounds heal from the outside in", "Wounds actually heal from the edges inward and from the bottom up. Cells at the wound margin divide and migrate across the wound surface, while new blood vessels and connective tissue build up from below. This is why deep wounds take longer — there's more vertical depth to fill.", "In the model, New Tissue Formation builds gradually from the wound edges. Increasing wound severity (depth) dramatically increases the time needed because cells must fill a larger three-dimensional space."),
        ("Your body just 'knows' when to heal", "Healing is triggered by specific chemical signals, not some mysterious awareness. When cells are damaged, they release growth factors and cytokines that signal neighboring cells to begin dividing. White blood cells arrive and release additional signals. This chemical cascade is automatic and measurable — it's biochemistry, not magic.", "In the model, Cell Division Rate increases in response to Wound Severity because damage triggers growth factor signals. The model shows the cause-and-effect chain: damage → signals → cell division → new tissue → healing.")
    ]
}

L10 = {
    "id": "G08L2-L10",
    "title": "Why Is Groundwater Disappearing?",
    "subtitle": "How Human Activity and Natural Cycles Determine the Future of Underground Water",
    "ngss": "MS-ESS3-1, MS-ESS2-4",
    "ngss_desc": "Construct a scientific explanation based on evidence for how the uneven distributions of Earth's mineral, energy, and groundwater resources are the result of past and current geoscience processes. Develop a model to describe the cycling of water through Earth's systems driven by energy from the sun and the force of gravity.",
    "big_question": "Why are aquifers that took thousands of years to fill being drained in just decades?",
    "objectives": [
        "Explain how agricultural irrigation and rainfall recharge affect aquifer levels",
        "Model the relationship between water extraction and long-term aquifer sustainability",
        "Predict how land subsidence occurs when underground water is removed",
        "Evaluate evidence for why groundwater depletion threatens long-term water security"
    ],
    "vocabulary": [
        ("Agricultural Irrigation", "The use of groundwater to water crops — the largest consumer of groundwater worldwide"),
        ("Rainfall Recharge", "The natural process by which rainwater seeps through soil and rock to replenish underground aquifers"),
        ("Aquifer Level", "The height of the water table in an underground aquifer — drops when extraction exceeds recharge"),
        ("Land Subsidence", "The sinking or settling of the ground surface caused by the removal of underground water, oil, or minerals"),
        ("Long-term Water Security", "The ability of a region to meet its water needs sustainably over decades and generations")
    ],
    "components": [
        ("Agricultural Irrigation", "Volume of groundwater pumped for farming — the primary demand on aquifers", True),
        ("Rainfall Recharge", "Amount of precipitation that percolates down to replenish the aquifer", True),
        ("Aquifer Level", "Current water table height — decreases when pumping exceeds natural recharge", False),
        ("Land Subsidence", "Ground surface sinking as empty underground spaces compact under pressure", False),
        ("Long-term Water Security", "Projected ability to meet future water needs based on current extraction rates", False)
    ],
    "think_about_it": "The Ogallala Aquifer under the Great Plains took millions of years to fill. Farmers have been pumping it for about 70 years, and some areas have already lost over 50% of their water. What happens when the pumping rate exceeds the refill rate?",
    "scenarios": [
        ("Balanced Water Budget", "Set Agricultural Irrigation and Rainfall Recharge to equal levels — sustainable pumping"),
        ("Over-Extraction", "Set Agricultural Irrigation to 90% and Rainfall Recharge to 30% — pumping far exceeds recharge"),
        ("Drought Conditions", "Set Agricultural Irrigation to 60% and Rainfall Recharge to 10% — high demand with minimal rain")
    ],
    "sim_scenarios": [
        ("Balanced vs. Over-Extraction", "Equal pumping and recharge vs. heavy pumping with low recharge", "What do you predict will happen to Aquifer Level over 20 years?"),
        ("Drought Impact", "Moderate irrigation with very low rainfall recharge", "What do you predict will happen to Land Subsidence?"),
        ("Long-term Projection", "Heavy irrigation sustained for 50 years", "What do you predict will happen to Long-term Water Security?")
    ],
    "discoveries": [
        "When extraction exceeds recharge, aquifer levels decline steadily — this is called groundwater mining",
        "Rainfall recharge is extremely slow — water may take decades or centuries to percolate down to deep aquifers",
        "As aquifer levels drop, the empty pore spaces in rock and sediment compact under the weight of overlying land, causing permanent land subsidence",
        "Land subsidence is irreversible — once the ground sinks, the aquifer can never hold as much water again even if refilled",
        "Long-term water security requires that extraction rates stay at or below natural recharge rates"
    ],
    "answer": "Groundwater is disappearing because humans are pumping water out of aquifers far faster than nature can replace it. Agricultural irrigation is the biggest consumer, and rainfall recharge is a slow process that can take years to centuries. When aquifer levels drop, the rock and soil above compact and the land surface sinks (subsidence) — permanently reducing the aquifer's storage capacity. This creates a dangerous feedback loop: less storage, less water security, more vulnerability to drought. Without reducing extraction or finding alternative water sources, many of the world's major aquifers face depletion within our lifetimes.",
    "stem_title": "Design a Sustainable Water Management Plan",
    "stem_mission": "Design an evidence-based water management plan for a farming community that balances agricultural needs with long-term aquifer sustainability, using your model data to justify every recommendation.",
    "stem_scenario": "A farming community in the Central Valley of California depends on groundwater for 80% of its irrigation. The aquifer level has dropped 60 feet in the last 30 years, and land subsidence has damaged roads and canals. Your team must create a plan that sustains both farming and the aquifer.",
    "stem_questions": [
        "How much can irrigation be reduced before crop yields are significantly affected?",
        "What alternative water sources could supplement groundwater?",
        "How can recharge be increased through managed aquifer replenishment?"
    ],
    "stem_design_qs": [
        "What specific irrigation reduction targets does your model evidence support?",
        "How will you balance short-term farming needs with long-term water security?",
        "What infrastructure changes could increase rainfall recharge rates?",
        "How will you monitor aquifer levels and land subsidence to measure your plan's effectiveness?"
    ],
    "career": "Hydrogeologists and Water Resource Engineers study groundwater systems and design sustainable water management strategies for communities, agriculture, and industry. They earn $65,000-$115,000/year.",
    "images": {
        "cover": ("cover-groundwater-disappearing.png", "A photorealistic dramatic cross-section of land showing an underground aquifer with the water level dropping, dried wells on the surface, cracked earth around them, farms in the background, cinematic environmental visualization"),
        "landscape": ("landscape-groundwater-disappearing.png", "A photorealistic image of a White male 8th grade student (age 13-14) examining a groundwater model with layers of soil and rock in a clear tank, diverse classmates measuring water levels, modern earth science lab, natural lighting"),
        "modeling": ("modeling-groundwater-disappearing.png", "A photorealistic image of a Black male 8th grade student (age 13-14) at a laptop graphing aquifer depletion data over decades, diverse classmates collaborating, modern classroom with water cycle and geology posters"),
        "discussion": ("discussion-groundwater-disappearing.png", "A photorealistic image of a Latino female 8th grade student (age 13-14) pointing at a cross-section diagram of aquifer depletion and land subsidence on a whiteboard, diverse engaged classmates, teacher facilitating, bright modern classroom"),
        "stem": ("stem-groundwater-disappearing.png", "A photorealistic image of an Asian male 8th grade student (age 13-14) presenting a water management plan poster with aquifer sustainability data, diverse team supporting, modern classroom setting")
    },
    "pre_assessment": [
        "Where does the water come from when you turn on a tap? Trace it as far back as you can.",
        "What is an aquifer, and how does water get underground?",
        "Why might pumping too much water from underground be a problem?",
        "Draw a simple diagram showing how rain becomes groundwater and how wells pump it back up."
    ],
    "extend_components": [
        ("Urban Water Demand", "Water consumed by cities and towns for drinking, sanitation, and industry — competing with agricultural use"),
        ("Aquifer Recharge Rate", "The speed at which water naturally percolates down to the aquifer — varies by soil type and geology"),
        ("Contamination Risk", "The chance that pollutants enter the aquifer as water levels drop and flow patterns change")
    ],
    "reflections": [
        "Why is groundwater depletion considered a 'slow-motion crisis' that many people don't notice until it's too late?",
        "How does land subsidence create a feedback loop that makes the problem worse?",
        "What responsibilities do current generations have to preserve groundwater for future generations?",
        "How does climate change affect the balance between rainfall recharge and irrigation demand?",
        "Why is it harder to manage groundwater than surface water like rivers and lakes?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model showing how agricultural extraction and natural recharge interact to determine aquifer levels, land subsidence, and long-term water security."),
        ("Disciplinary Core Idea", "ESS3.A Natural Resources", "Humans depend on Earth's land, ocean, atmosphere, and biosphere for many different resources, including groundwater. The distribution and sustainability of these resources is determined by geoscience processes."),
        ("Crosscutting Concept", "Stability and Change", "Students analyze how groundwater systems can remain stable (when recharge equals extraction) or change dramatically (when extraction exceeds recharge), and identify the tipping points where change becomes irreversible.")
    ],
    "cast_items": [
        "Construct scientific explanations for how geoscience processes affect groundwater distribution",
        "Develop models showing the cycling of water through Earth's systems including underground aquifers",
        "Use evidence to argue for sustainable groundwater management practices"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A farming region pumps 500 million gallons per year from its aquifer. Rainfall recharges the aquifer at 200 million gallons per year. At this rate, which of the following will occur, and why?"),
        ("Constructed Response:", "Using evidence from your model, explain why land subsidence is considered irreversible and how it creates a feedback loop that worsens groundwater depletion. Include the relationship between aquifer level and storage capacity in your explanation.")
    ],
    "background_intro": "Groundwater — water stored in underground rock formations called aquifers — supplies drinking water for nearly half the world's population and irrigates much of the world's farmland. Yet this invisible resource is being depleted at alarming rates, creating a slow-motion crisis that threatens food production and water security worldwide.",
    "background_sections": [
        ("What Is an Aquifer?", "An aquifer is an underground layer of permeable rock, sand, or gravel that holds and transmits water. Water fills the tiny spaces (pores) between rock particles, like water in a sponge. Major aquifers can be enormous — the Ogallala Aquifer underlies 174,000 square miles across eight US states. Some aquifers were filled millions of years ago and receive very little new water today (fossil aquifers)."),
        ("The Recharge Problem", "Rainfall recharge is the process by which surface water percolates through soil and rock to reach an aquifer. This process is slow — water may take years to decades to travel from the surface to a deep aquifer. In arid regions, very little rain reaches the aquifer because most evaporates or is consumed by plants. When pumping exceeds recharge, the aquifer is essentially being mined like a non-renewable resource."),
        ("Land Subsidence: The Irreversible Consequence", "When water is pumped from an aquifer, the pore spaces that held the water can collapse and compact under the weight of overlying land. This causes the ground surface to sink — a process called subsidence. In California's Central Valley, some areas have sunk over 28 feet since the 1920s. Critically, compacted rock cannot re-expand — even if the aquifer is refilled, it can never hold as much water as before. Subsidence is permanent."),
        ("The Global Groundwater Crisis", "The world's largest aquifers are being depleted. The Ogallala Aquifer (US Great Plains) has lost an average of 15 feet of water since 1950, with some areas losing over 150 feet. India's aquifers support 60% of irrigated agriculture but are declining rapidly. The North China Plain aquifer drops 3 feet per year. NASA's GRACE satellites measure groundwater from space and show that 21 of Earth's 37 major aquifers are being drained faster than they're refilled.")
    ],
    "lever_L": "Students identify agricultural irrigation, rainfall recharge, aquifer level, land subsidence, and long-term water security as system components.",
    "lever_E": "Students determine that irrigation depletes aquifer levels while rainfall recharges them, dropping aquifer levels cause land subsidence, and the balance determines long-term water security.",
    "lever_V": "Students build the groundwater model showing how extraction and recharge rates determine aquifer sustainability and the cascading effects of depletion.",
    "lever_Ev": "Students compare balanced vs. over-extraction scenarios to verify that sustainable pumping requires extraction at or below recharge rates, and observe irreversible subsidence effects.",
    "lever_R": "Students add urban water demand, contamination risk, or variable recharge rates to model more complex groundwater dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Aquifer cross-section depleting", "say": "Beneath your feet right now, there might be an ocean of water. And it's disappearing.", "do": "Show aquifer cross-section. Ask: Where does well water actually come from?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we model why underground water that took millennia to accumulate is vanishing in decades.", "do": "Pre-teach aquifer (underground reservoir), recharge (natural refilling), subsidence (ground sinking).", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Ogallala Aquifer depletion map", "say": "The Ogallala Aquifer feeds America's breadbasket. Some areas have lost half their water in 70 years. Why?", "do": "Show before/after aquifer level maps. Ask: What happens when you drain a sponge faster than it can soak up water?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model the balance between what goes in (rain) and what comes out (pumping).", "do": "Preview that this is fundamentally a balance problem — input vs. output over time.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Groundwater system components", "say": "Irrigation and rainfall are our inputs. Aquifer level, subsidence, and water security are the outputs.", "do": "Sort components. Discuss why irrigation and rainfall are external (human choice and weather).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Groundwater relationship arrows", "say": "Pumping drains the aquifer. Rain refills it. When the aquifer drops, the ground sinks — permanently.", "do": "Map relationships. Highlight the irreversibility of subsidence — this is the critical insight.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Aquifer depletion projections", "say": "Compare sustainable pumping vs. over-extraction over 50 years. The difference is dramatic.", "do": "Students predict before running. Focus on the long-term divergence and the subsidence feedback loop.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Groundwater crisis data", "say": "This isn't a future problem — it's happening now. Twenty-one of Earth's major aquifers are being drained.", "do": "Show NASA GRACE satellite data. Connect to local water sources and regional agriculture.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Water management plan", "say": "A farming community needs your help. Design a plan that saves both the farms and the aquifer.", "do": "Teams create management plans using model evidence. Present trade-offs and justify recommendations.", "time": "12 min"}
    ],
    "sort_reasoning": "Agricultural Irrigation and Rainfall Recharge are external because they represent the demand and supply inputs to the groundwater system — human pumping decisions and weather patterns that the aquifer itself cannot control. Aquifer Level, Land Subsidence, and Long-term Water Security are internal because they are outcomes that respond to and are determined by the balance between those external inputs.",
    "relationships": [
        ("Agricultural Irrigation to Aquifer Level", "NEGATIVE (-)", "More pumping for irrigation removes water from the aquifer, lowering the water table."),
        ("Rainfall Recharge to Aquifer Level", "POSITIVE (+)", "More rainfall percolation adds water to the aquifer, raising or stabilizing the water table."),
        ("Aquifer Level to Land Subsidence", "NEGATIVE (-)", "Lower aquifer levels cause underground pore spaces to collapse, increasing land subsidence at the surface."),
        ("Land Subsidence to Aquifer Level", "NEGATIVE (-)", "Subsidence permanently compacts aquifer rock, reducing its storage capacity — even if water is added, the aquifer holds less than before."),
        ("Aquifer Level to Long-term Water Security", "POSITIVE (+)", "Higher aquifer levels mean more water available for future use, increasing long-term water security for the region.")
    ],
    "sim_answers": [
        ("Balanced vs. Over-Extraction", "When irrigation equals recharge, Aquifer Level remains stable over 20 years — this is sustainable pumping. When irrigation is set to 90% and recharge to 30%, the aquifer loses water every year. After 20 years, the Aquifer Level has dropped dramatically, Land Subsidence has increased, and Long-term Water Security has plummeted. The gap between extraction and recharge compounds over time."),
        ("Drought Impact", "With moderate irrigation (60%) but very low rainfall recharge (10%), the aquifer depletes rapidly despite not being heavily pumped. This shows that recharge is equally important as extraction in the water budget. Land Subsidence increases as the aquifer drops, and once the ground has sunk, the aquifer permanently loses storage capacity — creating a feedback loop that accelerates the crisis even if rain returns.")
    ],
    "reflection_exemplars": [
        ("Why is groundwater depletion a 'slow-motion crisis'?", "Unlike a river running dry or a reservoir emptying — which are visible events people notice immediately — aquifer depletion happens underground, invisible to daily observation. Farmers pump water and crops grow normally for decades while the aquifer quietly drops. By the time wells start going dry or the ground visibly sinks, enormous damage has already been done. The model shows that over-extraction appears harmless in any single year but compounds catastrophically over decades. It's a classic 'boiling frog' problem — gradual change is harder to perceive than sudden change."),
        ("How does subsidence create a feedback loop?", "When aquifer levels drop, pore spaces in the rock collapse and the ground sinks. This is irreversible — the compacted rock cannot re-expand. The permanently reduced pore space means the aquifer can now hold LESS water than before, even if fully recharged. So the maximum possible aquifer level decreases, which further reduces Long-term Water Security. In the model, this appears as a negative feedback from Land Subsidence back to Aquifer Level — each cycle of depletion and subsidence reduces the aquifer's total capacity, making recovery harder and the next drought more dangerous.")
    ],
    "stem_intro": "Present the scenario: A farming community in California's Central Valley depends on groundwater for most of its irrigation. The aquifer has dropped 60 feet in 30 years, roads are cracking from subsidence, and the state is requiring a sustainability plan. Your team must design a plan that keeps farms productive while restoring the aquifer.",
    "stem_concepts": [
        ("Managed Aquifer Recharge", "Intentionally directing surface water (from rivers, canals, or treated wastewater) into basins where it percolates down to recharge aquifers. This can supplement natural rainfall recharge."),
        ("Deficit Irrigation", "Applying less water than crops ideally need during drought-tolerant growth stages. Many crops can produce 80-90% of normal yield with 60-70% of normal water — a significant savings."),
        ("Water Banking", "Storing excess surface water underground during wet years for extraction during dry years. The aquifer acts as a natural reservoir, reducing evaporation losses compared to surface reservoirs.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan uses model evidence to set specific extraction targets, addresses the subsidence feedback loop, includes recharge strategies, and balances agricultural and sustainability goals"),
        ("Proficient (3)", "Plan references aquifer depletion data and proposes extraction limits with recharge strategies"),
        ("Developing (2)", "Plan mentions reducing water use but lacks model evidence or specific sustainability targets"),
        ("Beginning (1)", "Plan doesn't connect to groundwater system concepts or model findings")
    ],
    "support": [
        "Provide groundwater budget worksheets where students calculate extraction vs. recharge rates",
        "Use sponge-and-water demonstrations to model aquifer storage and compaction",
        "Sentence frames: 'When irrigation exceeds recharge, the aquifer __ because __'"
    ],
    "extensions": [
        "Research the Ogallala Aquifer and calculate how many years of water remain at current extraction rates",
        "Add urban water demand and contamination risk to the model to explore competing pressures on groundwater",
        "Design a managed aquifer recharge system for a local watershed and estimate how much additional recharge it could provide"
    ],
    "cross_curr": [
        ("Math", "Calculate aquifer depletion rates using extraction and recharge data, and project how many years until the aquifer reaches critical levels"),
        ("ELA", "Write a persuasive letter to a state water board arguing for groundwater conservation policies, using model evidence and real-world data"),
        ("Social Studies", "Research how groundwater depletion affects different communities unequally — who loses access to water first, and what are the social justice implications?")
    ],
    "misconceptions": [
        ("Groundwater is an underground lake or river", "Groundwater doesn't exist in open underground caverns (except in rare karst geology). It fills tiny pore spaces between rock and sediment particles, like water in a sponge. An aquifer is rock or sediment whose pores are saturated with water — it looks like wet sand, not an underground pool.", "The model treats the aquifer as a storage volume that fills and drains. Use a sponge demonstration: water is held in the tiny spaces, not in a hollow chamber."),
        ("Rain immediately refills the aquifer", "Rainfall recharge is extremely slow. Water must percolate through soil, clay layers, and rock — a journey that can take months, years, or even centuries to reach deep aquifers. Most rainfall evaporates, runs off into rivers, or is absorbed by plant roots long before reaching the aquifer.", "In the model, even setting Rainfall Recharge to high values doesn't instantly restore Aquifer Level. The slow percolation rate means replenishment always lags behind extraction."),
        ("We can always drill deeper to find more water", "Drilling deeper wells is a temporary solution that accelerates the problem. Deeper pumping lowers the water table faster, increases energy costs, and can access lower-quality water. It also increases subsidence by pulling water from deeper rock that is even more prone to compaction. Eventually, there is no deeper water to reach.", "In the model, increasing Agricultural Irrigation (analogous to drilling deeper) temporarily maintains supply but accelerates Aquifer Level decline, increases Land Subsidence, and reduces Long-term Water Security faster.")
    ]
}
