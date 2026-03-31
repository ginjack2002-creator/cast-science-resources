#!/usr/bin/env python3
"""Complete lesson data for G06L2-L01 through G06L2-L07 (Grade 6 Level 2 ModelIt! Lessons)"""

L01 = {
    "id": "G06L2-L01",
    "title": "Who Eats Who? Energy Flow Through Food Webs",
    "subtitle": "Tracing Energy from Sunlight to Top Predators",
    "ngss": "MS-LS2-3, MS-LS2-4",
    "ngss_desc": "Develop a model to describe the cycling of matter and flow of energy among living and nonliving parts of an ecosystem. Construct an argument supported by empirical evidence that changes to physical or biological components of an ecosystem affect populations.",
    "big_question": "If the Sun provides enough energy to power all life on Earth, why are there so few top predators?",
    "objectives": [
        "Trace the flow of energy from the Sun through producers, primary consumers, and secondary consumers",
        "Model how energy is lost at each trophic level through metabolism and heat",
        "Explain the 10% energy transfer rule and its consequences for food web structure",
        "Predict how removing or adding organisms at one trophic level cascades through the entire web",
        "Analyze how decomposers recycle matter back to producers"
    ],
    "vocabulary": [
        ("Trophic Level", "A position in a food chain or food web that describes how many energy transfers separate an organism from the Sun"),
        ("Biomass", "The total mass of living organisms in a given area or trophic level, representing stored chemical energy"),
        ("Energy Pyramid", "A diagram showing the decrease in available energy at each trophic level, typically losing 90% at each step"),
        ("Decomposer", "An organism that breaks down dead organic matter and returns nutrients to the soil for producers to use"),
        ("Trophic Cascade", "A chain reaction through a food web when a change at one level ripples up or down to affect other levels")
    ],
    "components": [
        ("Solar Energy Input", "The amount of sunlight reaching the ecosystem, which producers capture through photosynthesis", True),
        ("Producer Biomass", "The total mass of plants and algae in the ecosystem that convert solar energy to chemical energy", False),
        ("Primary Consumer Biomass", "The total mass of herbivores that eat producers and transfer energy to the next level", False),
        ("Secondary Consumer Biomass", "The total mass of predators that eat herbivores, representing the third trophic level", False),
        ("Available Energy at Each Level", "The energy remaining after metabolic losses at each trophic level, following the 10% rule", False),
        ("Decomposer Return Rate", "The speed at which decomposers break down dead organisms and recycle nutrients back to producers", False)
    ],
    "think_about_it": "When solar energy input increases, what happens to producer biomass? If secondary consumers are removed, what happens to primary consumers and then to producers?",
    "scenarios": [
        ("Balanced Ecosystem", "Set Solar Energy Input to moderate and observe energy flow through all trophic levels"),
        ("Solar Shutdown", "Lock Solar Energy Input to 10% and observe the cascade through the food web"),
        ("Predator Removal", "Remove secondary consumers and observe what happens to primary consumers and producers")
    ],
    "sim_scenarios": [
        ("Balanced Ecosystem", "Moderate solar energy, all trophic levels present", "What do you predict will happen to Available Energy as you move from producers to secondary consumers?"),
        ("Solar Shutdown", "Lock Solar Energy to 10%", "What do you predict will happen to Secondary Consumer Biomass when producers receive very little sunlight?"),
        ("Predator Removal", "Remove secondary consumers", "What do you predict will happen to Producer Biomass if all predators are removed?")
    ],
    "discoveries": [
        "Only about 10% of energy transfers from one trophic level to the next. 90% is lost as heat from metabolism",
        "Removing top predators causes primary consumers to explode in population, which overgrazes producers",
        "Decomposers are essential because they recycle nutrients that producers need to capture new solar energy",
        "The energy pyramid explains why there are more plants than herbivores and more herbivores than predators",
        "Ecosystems depend on a constant input of solar energy because energy flows through but does not cycle"
    ],
    "answer": "There are so few top predators because energy is lost at every step of the food web. Only 10% of the energy at one level makes it to the next. So if producers capture 10,000 units of solar energy, herbivores get only 1,000, and predators get just 100. There simply is not enough energy at the top to support many large predators!",
    "stem_title": "Design a Balanced Ecosystem",
    "stem_mission": "Design a self-sustaining ecosystem for a sealed terrarium that maintains energy flow and nutrient cycling for at least 6 months.",
    "stem_scenario": "A space agency is designing sealed life-support ecosystems for a Mars colony. Your ecology team must design a small-scale model ecosystem that demonstrates balanced energy flow and nutrient recycling without any outside inputs except light.",
    "stem_questions": [
        "How many producers do you need to support one secondary consumer? Use the 10% rule to calculate.",
        "What role do decomposers play in keeping your sealed ecosystem running?",
        "What happens to your ecosystem if one trophic level is over- or under-represented?"
    ],
    "stem_design_qs": [
        "What species will represent each trophic level in your terrarium?",
        "How will you ensure enough producer biomass to support the consumers you include?",
        "What decomposers will you add and why are they critical for a sealed system?",
        "How will you monitor the health of your ecosystem over time?"
    ],
    "career": "Ecologists and Conservation Biologists study how energy and nutrients flow through ecosystems to protect biodiversity and design wildlife management plans. They earn $55,000-$110,000/year.",
    "images": {
        "cover": ("cover-food-web.png", "A stunning photorealistic aerial view of a diverse savanna ecosystem with visible food web connections: grasses, zebras, lions, and vultures, golden hour lighting with dramatic shadows"),
        "landscape": ("landscape-food-web.png", "A diverse group of 6th grade students in a modern science lab examining a terrarium ecosystem, one Asian student pointing at organisms while a White student takes notes, natural light"),
        "modeling": ("modeling-food-web.png", "A group of 6th grade students building a food web model on laptops, a Black student leading the discussion while a Latino student points at the screen, modern classroom with ecology posters"),
        "discussion": ("discussion-food-web.png", "A teacher leading an animated discussion about food webs with 6th grade students, pointing at an energy pyramid on a smartboard, Latino and White students with hands raised"),
        "stem": ("stem-terrarium.png", "6th grade students designing sealed terrariums at lab tables, an Asian student carefully placing plants while a Black student records observations, collaborative STEM project")
    },
    "pre_assessment": [
        "What do you think happens to energy when a rabbit eats grass?",
        "Why do you think there are more mice than hawks in most ecosystems?",
        "Draw a simple food chain with at least 3 organisms. Where does the energy come from?",
        "If all the wolves disappeared from Yellowstone, what do you think would happen?"
    ],
    "extend_components": [
        ("Tertiary Consumer Biomass", "Top predators like eagles or sharks that eat secondary consumers, receiving only 0.1% of original solar energy"),
        ("Nutrient Concentration", "The amount of recycled minerals and nitrogen available in the soil for plant uptake"),
        ("Competition Intensity", "How strongly organisms at the same trophic level compete for limited resources")
    ],
    "reflections": [
        "Why can't a food web support an infinite number of trophic levels?",
        "How is energy flow different from nutrient cycling in an ecosystem?",
        "What would happen to an ecosystem if all decomposers suddenly disappeared?",
        "Why does removing a top predator sometimes HELP producers more than removing herbivores?",
        "How does the 10% rule connect to the shape of an energy pyramid?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how solar energy flows through trophic levels with 90% loss at each transfer, and how decomposers recycle matter."),
        ("Disciplinary Core Idea", "LS2.B Cycles of Matter and Energy Transfer in Ecosystems", "Food webs are models that demonstrate how matter and energy are transferred between producers, consumers, and decomposers as the three groups interact within an ecosystem."),
        ("Crosscutting Concept", "Energy and Matter: Flows, Cycles, and Conservation", "Students trace energy flow (one-way, from Sun through organisms as heat) and matter cycling (nutrients recycled by decomposers) through the ecosystem.")
    ],
    "cast_items": [
        "Trace energy flow from sunlight through multiple trophic levels in a food web",
        "Explain why energy decreases at each trophic level using the 10% rule",
        "Predict the effects of removing a species from a food web on other populations"
    ],
    "cast_questions": [
        ("Multiple Choice:", "In a grassland ecosystem, producers capture 20,000 kJ of solar energy. Based on the 10% energy transfer rule, approximately how much energy is available to secondary consumers?"),
        ("Constructed Response:", "Wolves were reintroduced to Yellowstone National Park in 1995. Using your understanding of trophic cascades and energy flow, explain how adding wolves affected the elk population, the vegetation, and even the rivers.")
    ],
    "background_intro": "Food webs are the interconnected feeding relationships that link every organism in an ecosystem. Understanding energy flow through these webs reveals why ecosystems are structured the way they are and why every species matters.",
    "background_sections": [
        ("Energy Flow Is One-Way", "Unlike nutrients, energy does not cycle through ecosystems. Solar energy enters through photosynthesis, flows through consumers, and exits as heat. Every metabolic process (breathing, moving, growing) converts usable chemical energy into heat that radiates away. This one-way flow means ecosystems require constant solar input to function."),
        ("The 10% Rule", "On average, only about 10% of the energy at one trophic level is stored as biomass at the next level. The other 90% is used for metabolic processes and lost as heat. This is why a field of grass can support fewer rabbits, which support even fewer foxes. It takes roughly 10,000 kg of grass to produce 1,000 kg of rabbits to produce 100 kg of foxes."),
        ("Trophic Cascades", "When a predator population changes, it cascades through the food web. In Yellowstone, removing wolves led to an elk population explosion, which overgrazed willows and aspens along riverbanks, which caused riverbank erosion. Reintroducing wolves in 1995 reversed this cascade, allowing vegetation to recover and even changing how rivers flowed."),
        ("Decomposers Close the Loop", "While energy flows one-way, matter cycles. Decomposers (bacteria, fungi, worms) break down dead organisms and waste, releasing nutrients like nitrogen and phosphorus back into the soil. Producers absorb these nutrients to grow, starting the cycle again. Without decomposers, nutrients would be locked in dead matter and ecosystems would collapse.")
    ],
    "lever_L": "Students identify solar energy input, producer biomass, primary consumer biomass, secondary consumer biomass, available energy, and decomposer return rate as the key components of the food web energy system.",
    "lever_E": "Students determine that solar energy positively drives producer biomass, each trophic level positively feeds the next but with 90% energy loss, and decomposers positively recycle nutrients back to producers.",
    "lever_V": "Students build a model showing energy flow from sunlight through three trophic levels with metabolic losses and nutrient recycling by decomposers.",
    "lever_Ev": "Students run solar shutdown and predator removal scenarios to observe bottom-up and top-down cascade effects on the entire food web.",
    "lever_R": "Students add tertiary consumers or competition intensity to explore more complex food web dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with savanna food web imagery", "say": "Lions are the kings of the jungle, but there are only about 20,000 wild lions left. There are 7 billion chickens. Why?", "do": "Show comparison images of lion vs. chicken populations. Let students wonder about the numbers.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're going to discover the hidden math that controls every ecosystem on Earth.", "do": "Have students read objectives aloud. Pre-teach 'trophic level' and 'biomass.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why so few top predators?", "say": "The Sun blasts Earth with enough energy to power everything. So why can't ecosystems support more predators?", "do": "Think-pair-share: Why are there more plants than animals in every ecosystem?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll build a model to trace every unit of energy from sunlight to the top predator.", "do": "Preview LEVER steps. Explain that this model has 6 components and more complex relationships.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for food web model", "say": "Where does the energy start? What organisms capture it? Where does it go next?", "do": "Guide sorting. Explain why Solar Energy Input is external (comes from outside the ecosystem).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between trophic levels", "say": "Here is the big surprise: 90% of energy is LOST at every step. Only 10% moves up.", "do": "Use a hands-on demo: start with 100 candies (energy). Pass 10 to herbivores, then 1 to predators. Where did the other 89 go?", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's cut the sunlight and watch the whole web collapse from the bottom up!", "do": "Have students predict first. Run solar shutdown then predator removal. Compare cascade directions.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "Now you know the real reason there are so few eagles, sharks, and lions. It is all about energy math.", "do": "Connect the 10% rule to the energy pyramid shape. Discuss Yellowstone wolves as a real example.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Sealed terrarium design", "say": "Can you design a sealed ecosystem that runs on nothing but light? That is what Mars colonists will need.", "do": "Distribute materials. Groups design terrariums with the right ratio of producers to consumers.", "time": "12 min"}
    ],
    "sort_reasoning": "Solar Energy Input is external because it comes from outside the ecosystem entirely. Producer Biomass, Primary Consumer Biomass, Secondary Consumer Biomass, Available Energy at Each Level, and Decomposer Return Rate are all internal because they are properties of the ecosystem that respond to solar input and to each other through feeding relationships.",
    "relationships": [
        ("Solar Energy Input to Producer Biomass", "POSITIVE (+)", "More sunlight allows producers to photosynthesize more, building more biomass. Without sunlight, producers cannot make food and the entire web starves."),
        ("Producer Biomass to Primary Consumer Biomass", "POSITIVE (+)", "More plant biomass supports more herbivores. But only about 10% of the energy in producers transfers to primary consumers; 90% is lost as heat."),
        ("Primary Consumer Biomass to Secondary Consumer Biomass", "POSITIVE (+)", "More herbivore biomass supports more predators. Again, only 10% of herbivore energy reaches predators. This is why predators are rare."),
        ("Each Trophic Level to Available Energy", "NEGATIVE (-)", "At each level, organisms use 90% of consumed energy for metabolism (breathing, moving, body heat). Only 10% is stored as biomass available to the next level."),
        ("Decomposer Return Rate to Producer Biomass", "POSITIVE (+)", "Faster decomposition releases nutrients back into the soil sooner, allowing producers to grow more. Decomposers close the matter cycle.")
    ],
    "sim_answers": [
        ("Solar Shutdown Scenario", "When Solar Energy Input is locked at 10%, Producer Biomass drops sharply because plants cannot photosynthesize enough. Primary Consumer Biomass then crashes because there is not enough food. Secondary Consumer Biomass collapses last. The model shows a bottom-up cascade: energy starvation propagates upward through the web."),
        ("Predator Removal Scenario", "When secondary consumers are removed, Primary Consumer Biomass surges because nothing is eating the herbivores. This exploding herbivore population then overgrazes producers, causing Producer Biomass to crash. The model shows a top-down cascade: removing predators destabilizes the entire web from the top.")
    ],
    "reflection_exemplars": [
        ("Why can't a food web have infinite trophic levels?", "Each trophic level only retains 10% of the energy from the level below. After 4-5 levels, there simply is not enough energy left to support another population of organisms. If producers capture 10,000 kJ, the fourth level gets only 10 kJ. That is not enough to sustain any population. Energy loss sets a hard limit on food chain length."),
        ("What happens if decomposers disappear?", "Without decomposers, dead organisms would pile up and nutrients would be locked in dead matter forever. Producers would run out of soil nutrients, unable to grow. Without producers, the entire food web collapses. Decomposers are not just cleaners; they are the recyclers that keep the nutrient cycle running. Energy flows, but matter must cycle.")
    ],
    "stem_intro": "Present the challenge: A space agency is designing sealed life-support ecosystems for a Mars colony. Your team must design a small terrarium that maintains energy flow and nutrient recycling with only light as an external input.",
    "stem_concepts": [
        ("Ecological Stoichiometry", "The balance of chemical elements like carbon, nitrogen, and phosphorus in an ecosystem. Every organism needs specific ratios, and imbalances cause population crashes."),
        ("Carrying Capacity", "The maximum population an ecosystem can support based on available energy and resources. Exceeding carrying capacity leads to die-offs and ecosystem collapse."),
        ("Bioaccumulation", "The process where toxins concentrate as they move up the food web. Top predators accumulate the most because they eat contaminated prey over a lifetime.")
    ],
    "stem_eval": [
        ("Expert (4)", "Terrarium design uses the 10% rule to calculate correct ratios, includes decomposers, explains energy flow and nutrient cycling, and predicts potential failures"),
        ("Proficient (3)", "Design includes all trophic levels and decomposers with explanation of energy flow"),
        ("Developing (2)", "Design includes producers and consumers but lacks decomposers or energy calculations"),
        ("Beginning (1)", "Design is incomplete or does not demonstrate understanding of energy flow through food webs")
    ],
    "support": [
        "Provide a pre-drawn energy pyramid template with percentage labels at each level",
        "Use the candy demonstration: start with 100, pass 10, then 1 to physically show the 10% rule",
        "Sentence frames: 'When producer biomass decreases, primary consumer biomass __ because __'"
    ],
    "extensions": [
        "Research the Yellowstone wolf reintroduction and create a trophic cascade diagram showing all affected species",
        "Calculate how many kilograms of plankton it takes to produce 1 kg of tuna using the 10% rule across 4 trophic levels",
        "Investigate how mercury bioaccumulates through aquatic food webs and why top predator fish have the highest levels"
    ],
    "cross_curr": [
        ("Math", "Calculate energy available at each trophic level using the 10% rule and create a bar graph of the energy pyramid"),
        ("ELA", "Write a persuasive argument for protecting apex predators using evidence from trophic cascade research"),
        ("Social Studies", "Research how the collapse of cod fisheries in the North Atlantic affected both ecosystems and human communities")
    ],
    "misconceptions": [
        ("Energy recycles through ecosystems like nutrients do", "Energy does NOT cycle. It flows one way: in from the Sun, through organisms, and out as heat. Every metabolic process converts usable energy into heat that radiates into space. That is why ecosystems need constant sunlight. Nutrients cycle, but energy flows.", "Draw two diagrams side by side: nutrient cycle (circle with arrows) vs. energy flow (straight arrow from Sun to heat)."),
        ("Removing predators helps prey populations", "In the short term, prey populations increase. But without predators, herbivores overpopulate and overgraze, destroying the producer base. Then herbivores starve in a crash. Predators actually stabilize prey populations at a healthy, sustainable level.", "Show data from Yellowstone: elk populations surged after wolf removal but caused massive vegetation damage."),
        ("Decomposers are not important to the food web", "Decomposers are arguably the most critical organisms in any ecosystem. Without them, nutrients would be permanently locked in dead matter and producers would starve. They do not just clean up; they recycle the raw materials that keep the entire ecosystem running.", "Seal a terrarium with and without decomposers. The one without will fail as nutrients become unavailable.")
    ]
}

L02 = {
    "id": "G06L2-L02",
    "title": "Why Does Your Coffee Get Cold?",
    "subtitle": "The Hidden Math of Thermal Energy Transfer",
    "ngss": "MS-PS3-3, MS-PS3-4",
    "ngss_desc": "Apply scientific principles to design, construct, and test a device that either minimizes or maximizes thermal energy transfer. Plan an investigation to determine the relationships among the energy transferred, the type of matter, the mass, and the change in the average kinetic energy of the particles as measured by the temperature of the sample.",
    "big_question": "Why does hot coffee cool down fast at first but then seem to slow down, and why does it never get colder than the room?",
    "objectives": [
        "Explain how the temperature difference between an object and its surroundings drives thermal energy transfer",
        "Model how transfer rate changes as the temperature gap shrinks over time",
        "Describe how thermal equilibrium is reached through exponential decay of temperature difference",
        "Predict how changing room temperature affects the cooling curve of a hot object",
        "Connect the model to real-world engineering applications like insulation and climate control"
    ],
    "vocabulary": [
        ("Thermal Equilibrium", "The state reached when two objects are at the same temperature and net heat transfer stops between them"),
        ("Temperature Difference", "The gap between an object's temperature and the surrounding environment, which drives the rate of heat flow"),
        ("Transfer Rate", "The speed at which thermal energy moves from a hot object to its cooler surroundings, measured in joules per second"),
        ("Exponential Decay", "A pattern where something decreases quickly at first, then slows down as it approaches a limit, like a cooling curve"),
        ("Newton's Law of Cooling", "The principle that the rate of heat loss is proportional to the temperature difference between an object and its environment")
    ],
    "components": [
        ("Hot Object Temperature", "The starting temperature of the hot object, which decreases over time as heat transfers out", True),
        ("Room Temperature", "The ambient temperature of the surrounding environment, which the object cannot cool below", True),
        ("Temperature Difference", "The gap between the hot object and the room, which drives the rate of heat transfer", False),
        ("Transfer Rate", "The speed of heat flow from the object to the surroundings, directly proportional to the temperature difference", False),
        ("Object Temperature Over Time", "The changing temperature of the object as it cools toward room temperature following an exponential decay curve", False)
    ],
    "think_about_it": "When the temperature difference is large, the transfer rate is fast. As the object cools, the difference shrinks. What happens to the transfer rate? Will the object ever get colder than the room?",
    "scenarios": [
        ("Hot Coffee in Cold Room", "Set Hot Object Temperature to 90 degrees C and Room Temperature to 20 degrees C and observe the cooling curve"),
        ("Hot Coffee in Warm Room", "Set Hot Object Temperature to 90 degrees C and Room Temperature to 35 degrees C and compare cooling speed"),
        ("Lukewarm Water in Cold Room", "Set Hot Object Temperature to 40 degrees C and Room Temperature to 20 degrees C and observe the flatter curve")
    ],
    "sim_scenarios": [
        ("Hot Coffee in Cold Room", "90 degrees C object, 20 degrees C room", "What do you predict the cooling curve will look like? Will it be a straight line or a curve?"),
        ("Hot Coffee in Warm Room", "90 degrees C object, 35 degrees C room", "How will the cooling curve differ from the cold room scenario? Will it take longer or shorter to stop cooling?"),
        ("Lukewarm Water", "40 degrees C object, 20 degrees C room", "What do you predict happens to the transfer rate when the temperature difference is only 20 degrees instead of 70?")
    ],
    "discoveries": [
        "Heat transfer rate is proportional to the temperature difference. Bigger gap means faster transfer",
        "The cooling curve is NOT a straight line. It is an exponential decay curve that flattens as the object approaches room temperature",
        "A hot object in a warmer room cools more slowly because the temperature difference driving the transfer is smaller",
        "The object can never cool below room temperature because at equilibrium, the temperature difference is zero and transfer stops",
        "This same pattern appears everywhere: cooling drinks, warming cold objects, climate systems, and even electric circuits"
    ],
    "answer": "Coffee cools fast at first because the temperature difference between the hot coffee and the cool room is large, driving rapid heat transfer. As the coffee cools and the gap shrinks, the transfer rate slows down. The coffee approaches room temperature but never goes below it because at equilibrium, the temperature difference is zero and there is no force driving further transfer. This exponential decay pattern is one of the most common patterns in all of physics.",
    "stem_title": "Design a Temperature Control System",
    "stem_mission": "Design a passive cooling or warming system that maintains a beverage within a target temperature range for the longest time possible.",
    "stem_scenario": "A hospital needs to keep medications at exactly 37 degrees C during transport. Your biomedical engineering team must design a passive thermal system (no electricity) that maintains temperature within 2 degrees of the target for at least 4 hours.",
    "stem_questions": [
        "Based on your model, what is the most important factor controlling how fast temperature changes?",
        "How could you slow down the transfer rate to keep your beverage at the target temperature longer?",
        "Why does insulation work better when the temperature difference is large?"
    ],
    "stem_design_qs": [
        "What insulation materials will you use to slow thermal energy transfer?",
        "How will you pre-condition your container (pre-heat or pre-cool) to start near the target?",
        "What is the optimal starting temperature for your beverage to stay in range the longest?",
        "How will you test your system and measure its performance over time?"
    ],
    "career": "Thermal Engineers design heating, cooling, and insulation systems for buildings, vehicles, spacecraft, and medical devices. They apply Newton's Law of Cooling daily. They earn $65,000-$125,000/year.",
    "images": {
        "cover": ("cover-cooling.png", "A photorealistic thermal imaging photograph of a steaming coffee mug showing heat gradients from deep red at the liquid to blue at the surrounding air, dramatic scientific visualization on dark background"),
        "landscape": ("landscape-cooling.png", "A diverse group of 6th grade students conducting a cooling experiment with thermometers in cups of water at different temperatures, a White student reading the thermometer while a Black student records data, bright science lab"),
        "modeling": ("modeling-cooling.png", "6th grade students working on laptops building a thermal energy model, a Latino student pointing at an exponential decay graph on screen while an Asian student adjusts parameters, modern classroom"),
        "discussion": ("discussion-cooling.png", "A teacher drawing a cooling curve on a whiteboard while 6th grade students compare their predictions, diverse students with notebooks open, engaged classroom discussion"),
        "stem": ("stem-thermal-system.png", "6th grade students testing insulated containers with digital thermometers, comparing different materials like foam and foil, a Black student leading the data collection while a White student records results")
    },
    "pre_assessment": [
        "If you pour hot water and cold water into the same cup, what temperature do you think it becomes? Why?",
        "Does a hot drink cool at the same speed the entire time, or does it change? Explain your thinking.",
        "Why do you think soup cools down faster on a cold winter day than on a warm summer day?",
        "Draw a graph of what you think happens to the temperature of hot coffee over time."
    ],
    "extend_components": [
        ("Insulation Level", "How well the container prevents heat from escaping, slowing the transfer rate"),
        ("Object Mass", "Larger masses store more thermal energy and take longer to change temperature"),
        ("Material Conductivity", "How easily the container material conducts heat, affecting transfer rate")
    ],
    "reflections": [
        "Why does the cooling curve flatten out instead of continuing straight down?",
        "Could a hot object ever cool below room temperature without a refrigerator? Why or why not?",
        "If you double the temperature difference, does the cooling rate double? What does your model show?",
        "How is the cooling of coffee similar to the way a phone battery drains?",
        "Why do thermos bottles work so well based on what you learned about transfer rate and temperature difference?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model demonstrating how temperature difference drives transfer rate and produces exponential decay cooling curves."),
        ("Disciplinary Core Idea", "PS3.A Definitions of Energy / PS3.B Conservation of Energy", "Temperature is a measure of the average kinetic energy of particles. Thermal energy transfers from regions of higher temperature to regions of lower temperature until equilibrium is reached."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify that the temperature difference CAUSES the heat transfer, and as the effect (cooling) reduces the cause (temperature difference), the rate of change slows. This is a self-limiting system.")
    ],
    "cast_items": [
        "Explain how temperature difference drives the rate of thermal energy transfer",
        "Describe why cooling curves are exponential rather than linear",
        "Predict how changing the room temperature affects the final equilibrium temperature"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student heats two identical cups of water to 80 degrees C. Cup A is placed in a 10 degrees C room and Cup B is placed in a 30 degrees C room. After 10 minutes, which cup has lost more thermal energy, and why?"),
        ("Constructed Response:", "Using Newton's Law of Cooling, explain why a cup of coffee left on a counter cools rapidly in the first 5 minutes but barely changes temperature in the last 5 minutes before reaching room temperature. Include a sketch of the cooling curve.")
    ],
    "background_intro": "The cooling of a hot object is one of the most fundamental and observable physics phenomena. Newton's Law of Cooling describes the exponential decay pattern, and this same mathematical pattern appears in radioactive decay, capacitor discharge, population decline, and countless other systems.",
    "background_sections": [
        ("Newton's Law of Cooling", "Isaac Newton discovered that the rate of heat loss from an object is proportional to the temperature difference between the object and its surroundings. This means that a 90-degree C object in a 20-degree C room loses heat much faster than a 40-degree C object in the same room. The bigger the gap, the faster the flow."),
        ("Exponential Decay", "The cooling curve follows an exponential decay pattern. Temperature drops rapidly at first (when the gap is large), then progressively slows as the gap shrinks. Mathematically, the temperature approaches room temperature but never quite reaches it (in theory). In practice, the difference becomes so small that it is undetectable."),
        ("Thermal Equilibrium", "When two objects reach the same temperature, they are in thermal equilibrium. Net heat transfer is zero because there is no temperature difference to drive it. This is the Second Law of Thermodynamics in action: energy naturally disperses from concentrated (hot) to diffuse (spread out), never the reverse without external energy."),
        ("Real-World Applications", "This principle governs building insulation (slowing heat transfer through walls), cooking (heat must transfer from the oven to the center of food), climate science (Earth radiates heat to space based on temperature difference), and medicine (hypothermia treatment, fever management). Engineers use these principles daily.")
    ],
    "lever_L": "Students identify hot object temperature, room temperature, temperature difference, transfer rate, and object temperature over time as the key components of the thermal system.",
    "lever_E": "Students determine that temperature difference positively drives transfer rate, transfer rate negatively affects object temperature, and as the object cools, temperature difference shrinks, creating a self-slowing system.",
    "lever_V": "Students build a model showing how the interplay between temperature difference and transfer rate produces the characteristic exponential decay cooling curve.",
    "lever_Ev": "Students run hot-in-cold-room vs. hot-in-warm-room scenarios and compare cooling curves to observe how room temperature affects the equilibrium point and cooling speed.",
    "lever_R": "Students add insulation level or object mass to explore how additional variables modify the cooling curve shape.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with thermal imaging of hot coffee", "say": "You make the perfect cup of coffee. You take one phone call. It is cold. Where did all that heat go?", "do": "If possible, bring a hot cup of water and a thermometer. Show the temperature dropping in real time.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are going to discover the hidden math behind every cooling curve in the universe.", "do": "Have students read objectives. Pre-teach 'thermal equilibrium' and 'exponential decay.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why does cooling slow down?", "say": "Your coffee cools fast at first, then slows to a crawl. That is NOT random. There is an elegant law behind it.", "do": "Have students sketch their prediction of a cooling curve. Collect and display several predictions.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We will build a model to discover Newton's Law of Cooling through simulation.", "do": "Preview the 5 components. Emphasize that this model has a self-limiting feedback mechanism.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for thermal model", "say": "What controls how fast heat transfers? The temperature of the object? The room? Both?", "do": "Guide sorting. Discuss why both temperatures are external inputs the student controls.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows with feedback", "say": "Here is the key insight: as the object cools, the temperature difference SHRINKS, which slows the transfer rate. The system slows itself down.", "do": "Draw the feedback loop on the board. Show how the output (cooling) reduces the input (temperature difference).", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions vs. actual cooling curves", "say": "Let's compare coffee in a cold room versus coffee in a warm room. Which cools faster?", "do": "Students predict curves first. Run both scenarios. Overlay the curves to compare.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings and exponential decay pattern", "say": "This exponential decay pattern is everywhere. Cooling coffee, draining batteries, radioactive decay. Same math, different systems.", "do": "Show examples of exponential decay in other domains. Discuss thermal equilibrium.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Temperature control system design", "say": "Now you are biomedical engineers. Design a system that keeps medicine at body temperature for 4 hours.", "do": "Distribute materials and constraints. Groups design, test, and measure passive thermal systems.", "time": "12 min"}
    ],
    "sort_reasoning": "Hot Object Temperature and Room Temperature are external because they are the initial conditions the student sets. Temperature Difference, Transfer Rate, and Object Temperature Over Time are internal because they are calculated by the system based on the two external inputs and the relationships between components.",
    "relationships": [
        ("Hot Object Temperature to Temperature Difference", "POSITIVE (+)", "A hotter starting object creates a larger temperature gap with the room, which drives faster initial heat transfer."),
        ("Room Temperature to Temperature Difference", "NEGATIVE (-)", "A warmer room means a smaller gap between the object and its surroundings, reducing the driving force for heat transfer."),
        ("Temperature Difference to Transfer Rate", "POSITIVE (+)", "The larger the temperature gap, the faster heat flows. This is Newton's Law of Cooling: transfer rate is proportional to temperature difference."),
        ("Transfer Rate to Object Temperature Over Time", "NEGATIVE (-)", "A faster transfer rate causes the object to cool more quickly. As the object cools, temperature difference shrinks, which slows the transfer rate. This creates the exponential decay curve.")
    ],
    "sim_answers": [
        ("Hot Coffee in Cold Room", "The 90-degree C coffee in a 20-degree C room cools rapidly in the first 5-10 minutes because the 70-degree temperature difference drives fast transfer. As the coffee approaches room temperature, the curve flattens dramatically. The coffee reaches about 25 degrees C after a long time, approaching but never quite reaching the 20-degree C room temperature."),
        ("Hot Coffee in Warm Room", "The same 90-degree C coffee in a 35-degree C room cools more slowly throughout because the maximum temperature difference is only 55 degrees (vs. 70 in the cold room). It also reaches equilibrium at a higher temperature (35 degrees C vs. 20 degrees C). The curve shape is the same exponential decay but shallower and shifted upward.")
    ],
    "reflection_exemplars": [
        ("Why does the cooling curve flatten?", "The curve flattens because the CAUSE of cooling (temperature difference) shrinks as the EFFECT of cooling (lower temperature) happens. When the coffee is 90 degrees C in a 20-degree C room, the 70-degree gap drives very fast transfer. By the time the coffee is 25 degrees C, the gap is only 5 degrees, driving very slow transfer. The system is self-limiting because the output (cooling) reduces the input (temperature difference)."),
        ("Can an object cool below room temperature?", "No, because at room temperature, the temperature difference is zero. With zero temperature difference, the transfer rate is zero. There is no driving force to push heat out of the object. To cool below room temperature, you would need to actively remove heat (like a refrigerator), which requires energy input. This is a consequence of the Second Law of Thermodynamics.")
    ],
    "stem_intro": "Present the challenge: A hospital needs to transport temperature-sensitive medications at exactly 37 degrees C. Your biomedical engineering team must design a passive thermal system that maintains temperature within 2 degrees for 4 hours using only insulation and thermal mass.",
    "stem_concepts": [
        ("Thermal Mass", "Materials that absorb and store large amounts of thermal energy, releasing it slowly. Water and stone have high thermal mass. This can buffer temperature changes."),
        ("Phase Change Materials", "Substances engineered to melt or freeze at specific temperatures, absorbing or releasing heat during the phase change to maintain constant temperature."),
        ("R-Value and U-Value", "Engineering measures of insulation effectiveness. R-value measures resistance to heat flow (higher is better insulation). U-value measures heat transfer rate (lower is better insulation).")
    ],
    "stem_eval": [
        ("Expert (4)", "Design uses model evidence to calculate required insulation, addresses thermal mass, includes testing data, and explains the physics of temperature maintenance"),
        ("Proficient (3)", "Design includes insulation strategy with model evidence and testing plan"),
        ("Developing (2)", "Design mentions insulation but does not connect to Newton's Law of Cooling or temperature difference"),
        ("Beginning (1)", "Design is incomplete or does not demonstrate understanding of thermal energy transfer")
    ],
    "support": [
        "Provide a pre-drawn exponential decay curve template with labels for students to annotate",
        "Use two cups of water (hot and lukewarm) and thermometers to physically observe different cooling rates",
        "Sentence frames: 'When the temperature difference decreases, the transfer rate __ because __'"
    ],
    "extensions": [
        "Graph actual cooling data from a real experiment and compare the curve shape to the model predictions",
        "Research how spacecraft manage extreme temperature differences between sun-facing and shadow-facing sides",
        "Investigate phase-change materials used in building construction to maintain comfortable indoor temperatures"
    ],
    "cross_curr": [
        ("Math", "Plot cooling data on a graph and identify the exponential decay pattern. Calculate the rate of temperature change at different time intervals."),
        ("ELA", "Write a technical report explaining Newton's Law of Cooling to a younger student, using everyday analogies and a hand-drawn cooling curve"),
        ("Social Studies", "Research how ancient civilizations managed temperature without electricity (Roman hypocaust heating, Persian wind catchers, ice houses)")
    ],
    "misconceptions": [
        ("Objects cool at a constant rate", "Cooling is NOT linear. Objects cool fast at first (large temperature gap drives fast transfer) and slow down as they approach room temperature. The curve is exponential, not a straight line. This is a fundamental pattern in physics.", "Measure a hot cup every 2 minutes and plot the data. Students see the curve flatten in real time."),
        ("Cold flows into hot objects", "There is no such thing as 'cold' flowing. Only thermal energy (heat) moves, and it always moves from hot to cold. When your coffee cools, heat is leaving. When your hands feel cold touching metal, your body heat is flowing INTO the metal, not cold flowing out.", "Ask: Is a coat warm? Put a thermometer in a coat by itself. The temperature does not rise. The coat just slows YOUR heat from leaving."),
        ("Room temperature is a property of the object", "Room temperature is the temperature of the environment, not the object. The object approaches room temperature through heat transfer. Different rooms have different temperatures. The same coffee would reach different final temperatures in different rooms.", "Move the same hot cup between a cold room and a warm room. The equilibrium temperature changes because the environment changed.")
    ]
}

L03 = {
    "id": "G06L2-L03",
    "title": "Plate Tectonics: Predicting Where Earth Will Crack Next",
    "subtitle": "Using Models to Forecast Earthquakes and Volcanic Activity",
    "ngss": "MS-ESS2-2, MS-ESS2-3",
    "ngss_desc": "Construct an explanation based on evidence for how geoscience processes have changed Earth's surface at varying time and spatial scales. Analyze and interpret data on the distribution of fossils and rocks, continental shapes, and seafloor structures to provide evidence of the past plate motions.",
    "big_question": "If we know where tectonic plates meet, why can't we predict exactly when the next big earthquake will hit?",
    "objectives": [
        "Explain how mantle convection drives tectonic plate movement at measurable rates",
        "Model how different plate boundary types produce different geological hazards",
        "Analyze the relationship between tectonic stress buildup and earthquake frequency",
        "Predict volcanic activity based on plate boundary type and mantle convection speed",
        "Describe how negative feedback between earthquakes and stress creates cyclical patterns"
    ],
    "vocabulary": [
        ("Mantle Convection", "Circular currents of hot rock rising and cool rock sinking in Earth's mantle that drag tectonic plates along"),
        ("Tectonic Stress", "The pressure that builds at plate boundaries as plates push against, pull apart from, or slide past each other"),
        ("Convergent Boundary", "A plate boundary where two plates collide, creating mountains, deep trenches, and subduction zones with volcanoes"),
        ("Divergent Boundary", "A plate boundary where two plates move apart, creating rifts, mid-ocean ridges, and new oceanic crust"),
        ("Transform Boundary", "A plate boundary where two plates slide horizontally past each other, creating earthquake faults like the San Andreas")
    ],
    "components": [
        ("Mantle Convection Speed", "How fast hot rock circulates in the mantle, driving plate movement above", True),
        ("Plate Boundary Type", "Whether plates are colliding (convergent), separating (divergent), or sliding (transform)", True),
        ("Tectonic Stress", "The pressure accumulating at the boundary as plates interact, storing potential energy", False),
        ("Earthquake Frequency", "How often seismic events occur at the boundary, related to stress release patterns", False),
        ("Volcanic Activity", "The likelihood and intensity of volcanic eruptions, dependent on boundary type and magma availability", False)
    ],
    "think_about_it": "When mantle convection speed increases, what happens to tectonic stress? After a large earthquake releases stress, what happens to earthquake frequency? Why do some boundaries have volcanoes and others do not?",
    "scenarios": [
        ("Fast Convergent", "Set Mantle Convection Speed high and Plate Boundary Type to convergent to observe both earthquakes and volcanoes"),
        ("Slow Transform", "Set Mantle Convection Speed low and Plate Boundary Type to transform to see earthquake-only behavior"),
        ("Stress Cycle", "Watch tectonic stress build and release in cycles as earthquakes periodically reduce accumulated stress")
    ],
    "sim_scenarios": [
        ("Fast Convergent", "High convection, convergent boundary", "What do you predict will happen to both earthquake frequency and volcanic activity at a fast convergent boundary?"),
        ("Slow Transform", "Low convection, transform boundary", "What do you predict happens to volcanic activity at a transform boundary? Will there be volcanoes?"),
        ("Stress Cycle", "Moderate convection, observe over time", "What pattern do you predict in the tectonic stress graph? Will it be steady or will it go up and down?")
    ],
    "discoveries": [
        "Faster mantle convection increases tectonic stress at boundaries, leading to more frequent geological events",
        "Convergent boundaries produce BOTH earthquakes and volcanoes because subducting plates melt and create magma",
        "Transform boundaries produce earthquakes but almost NO volcanoes because plates slide horizontally without subduction",
        "Earthquakes release accumulated stress, creating a negative feedback cycle: stress builds, quake releases, stress rebuilds",
        "The stress-release cycle explains why earthquake patterns are somewhat cyclical but never perfectly predictable"
    ],
    "answer": "We know WHERE earthquakes will happen (at plate boundaries) but not WHEN because of the complex stress-release cycle. Stress builds gradually as plates push against each other, but release is sudden and unpredictable. The exact moment when accumulated stress overcomes friction depends on countless microscopic variables in the rock. We can predict the pattern but not the precise timing, just as we know a stretched rubber band will snap but not exactly when.",
    "stem_title": "Design an Earthquake Early Warning System",
    "stem_mission": "Design a community early warning and response system for a city located near two different types of plate boundaries.",
    "stem_scenario": "A coastal city sits near both a convergent boundary (offshore subduction zone) and a transform fault. The city council needs your team to design warning systems, building codes, and emergency procedures based on your model predictions of earthquake and volcanic risks.",
    "stem_questions": [
        "Based on your model, which boundary poses a greater earthquake risk and which poses a volcanic risk?",
        "How would you prioritize building design for earthquake resistance vs. volcanic preparedness?",
        "How should evacuation routes differ for earthquake vs. tsunami vs. volcanic threats?"
    ],
    "stem_design_qs": [
        "What sensor systems will detect early seismic activity and how much warning time can they provide?",
        "How will your building codes differ for areas near the transform fault vs. near the subduction zone?",
        "What emergency communication systems will reach all residents quickly?",
        "How will you design infrastructure (bridges, hospitals, schools) to withstand the hazards your model predicts?"
    ],
    "career": "Seismologists use network sensor data and computational models to study earthquake patterns and improve prediction methods. Volcanologists monitor active volcanoes to forecast eruptions and protect communities. They earn $65,000-$130,000/year.",
    "images": {
        "cover": ("cover-tectonics-L2.png", "A dramatic photorealistic satellite view of Earth showing tectonic plate boundaries glowing with seismic activity markers, convergent boundaries in red and divergent in blue, cinematic Earth science visualization"),
        "landscape": ("landscape-tectonics-L2.png", "6th grade students examining a globe and a plate boundary map, a Latino student pointing at the Ring of Fire while a White student marks earthquake locations, bright modern science classroom"),
        "modeling": ("modeling-tectonics-L2.png", "A diverse group of 6th grade students building a plate tectonics model on laptops, an Asian student adjusting convection speed while a Black student records predictions, classroom with Earth science displays"),
        "discussion": ("discussion-tectonics-L2.png", "A teacher comparing convergent and transform boundary diagrams on a smartboard, 6th grade students debating which boundary type is more dangerous, diverse and engaged classroom"),
        "stem": ("stem-warning-system.png", "6th grade students designing earthquake warning system prototypes using craft materials and maps, a White student drawing evacuation routes while a Latino student builds a model seismometer, collaborative STEM work")
    },
    "pre_assessment": [
        "Why do you think earthquakes happen more in California than in Florida?",
        "Do earthquakes and volcanoes always happen together? Why or why not?",
        "If you could measure the stress building in the ground, could you predict an earthquake? Why might it be hard?",
        "Draw what you think happens underground when two tectonic plates push into each other."
    ],
    "extend_components": [
        ("Plate Thickness", "Thicker continental plates resist subduction while thinner oceanic plates dive underneath, affecting boundary behavior"),
        ("Magma Viscosity", "Thicker magma creates explosive volcanoes while thinner magma creates gentle flows, depending on silica content"),
        ("Fault Depth", "Shallow earthquakes are more destructive at the surface than deep earthquakes of the same magnitude")
    ],
    "reflections": [
        "Why do convergent boundaries have volcanoes but transform boundaries do not?",
        "If earthquakes release stress, why do more earthquakes keep happening at the same location?",
        "How is the stress-release cycle at plate boundaries similar to stretching a rubber band?",
        "Why is predicting WHEN an earthquake will happen so much harder than predicting WHERE?",
        "How does your model help explain why the Ring of Fire has 75% of the world's volcanoes?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how mantle convection, boundary type, and tectonic stress interact to produce patterns of earthquakes and volcanic activity."),
        ("Disciplinary Core Idea", "ESS2.B Plate Tectonics and Large-Scale System Interactions", "Tectonic plates are the top parts of giant convection cells that bring hot material up from Earth's interior and send cooled material back down. Plate interactions cause earthquakes, volcanic activity, and mountain building."),
        ("Crosscutting Concept", "Stability and Change", "Students explore how plate boundaries appear stable over human timescales but are zones of constant stress accumulation and sudden release, creating cyclical patterns of geological activity.")
    ],
    "cast_items": [
        "Compare the geological hazards produced by convergent, divergent, and transform boundaries",
        "Explain how the negative feedback between tectonic stress and earthquake release creates cyclical patterns",
        "Use plate tectonic theory to predict where future geological activity is most likely"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Scientists observe that a transform fault has been quiet for 150 years while a similar fault nearby has frequent small earthquakes. Based on tectonic stress models, which fault poses a greater risk of a large earthquake, and why?"),
        ("Constructed Response:", "Using your plate tectonics model, explain why Japan experiences both earthquakes AND volcanic eruptions while the San Andreas Fault area in California has earthquakes but very few volcanoes. Reference boundary types in your explanation.")
    ],
    "background_intro": "Plate tectonics is the unifying theory of geology, explaining earthquakes, volcanoes, mountain building, and even the distribution of fossils. By modeling the stress dynamics at different boundary types, students can predict real-world geological patterns.",
    "background_sections": [
        ("Mantle Convection Drives Everything", "Earth's interior is incredibly hot (over 5,000 degrees C at the core). This heat creates convection currents in the mantle: hot rock rises, spreads laterally, cools, and sinks. These currents drag tectonic plates along at rates of 2-15 cm per year. Though slow by human standards, these movements reshape continents over millions of years."),
        ("Three Boundary Types, Three Hazard Profiles", "Convergent boundaries (plates collide) create mountains and subduction zones where one plate dives under another, melting and fueling volcanoes. Divergent boundaries (plates separate) create mid-ocean ridges and rift valleys. Transform boundaries (plates slide past) create earthquake faults. Each type produces a distinct combination of hazards."),
        ("The Stress-Release Cycle", "At plate boundaries, friction locks plates together while convection keeps pushing. Stress accumulates over years or decades. When stress exceeds the frictional strength of the rock, it fails suddenly, releasing energy as an earthquake. After the quake, stress drops and begins rebuilding. This creates a cyclical pattern that is predictable in average frequency but unpredictable in exact timing."),
        ("Prediction vs. Forecasting", "Scientists cannot predict the exact date, time, and location of an earthquake. But they CAN forecast probabilities: the USGS estimates a 72% chance of a magnitude 6.7+ earthquake in the San Francisco Bay Area before 2043. This is based on historical patterns, stress measurements, and understanding of the recurrence intervals at specific faults.")
    ],
    "lever_L": "Students identify mantle convection speed and plate boundary type as external inputs, and tectonic stress, earthquake frequency, and volcanic activity as internal responses of the system.",
    "lever_E": "Students determine that mantle convection positively drives tectonic stress, stress positively drives earthquake frequency, but earthquakes negatively feed back to reduce stress (negative feedback). Boundary type determines whether volcanic activity occurs.",
    "lever_V": "Students build a model showing how convection drives stress accumulation, which is periodically released by earthquakes, creating cyclical patterns. Different boundary types produce different hazard combinations.",
    "lever_Ev": "Students run fast convergent vs. slow transform scenarios to compare hazard profiles and observe the stress-release cycle in the simulation graphs.",
    "lever_R": "Students add plate thickness or magma viscosity to explore why some convergent boundaries produce explosive volcanoes while others produce gentle eruptions.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with plate boundary imagery from space", "say": "Right now, the ground under you is moving. You cannot feel it, but the forces building beneath your feet could release in seconds.", "do": "Show a global earthquake map with the Ring of Fire highlighted. Let students notice the pattern.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are going beyond plate tectonics to model the STRESS system that controls when and where Earth cracks.", "do": "Have students read objectives. Pre-teach 'tectonic stress' and 'convergent/divergent/transform.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why can't we predict the exact moment?", "say": "We know California will have a big earthquake. We know the fault that will do it. So why can't we say when?", "do": "Think-pair-share: What makes earthquake timing so hard to predict?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "Our model has a hidden feedback loop: earthquakes release stress, which REDUCES earthquake frequency. Until stress builds again.", "do": "Preview the negative feedback concept. Draw the cycle on the board.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for tectonics model", "say": "What drives the system? What responds? Notice we have TWO external inputs this time: speed AND boundary type.", "do": "Guide sorting. Explain why boundary type is external (it is a geological given, not something the system changes).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows with negative feedback loop", "say": "The critical relationship: earthquakes RELEASE stress. So more earthquakes at a boundary temporarily REDUCE the stress driving them.", "do": "Demonstrate with a spring: compress (stress builds), release (earthquake), spring returns to normal (stress resets).", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions vs. results for different boundary types", "say": "Let's compare a fast convergent boundary to a slow transform boundary. Which is more dangerous?", "do": "Students predict first. Run both scenarios. Compare earthquake frequency AND volcanic activity side by side.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "Now you understand why we can forecast earthquake ZONES but not exact timing. The cycle is real but the timing is chaotic.", "do": "Show USGS earthquake probability forecasts. Discuss how models inform preparedness even without exact prediction.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Earthquake warning system design", "say": "Your city sits near TWO fault types. Design a warning system that handles both earthquake and volcanic threats.", "do": "Distribute maps and materials. Groups design integrated warning systems using model evidence.", "time": "12 min"}
    ],
    "sort_reasoning": "Mantle Convection Speed is external because it is driven by Earth's internal heat, a force outside the plate boundary system. Plate Boundary Type is external because it is a geological configuration that the model does not change. Tectonic Stress, Earthquake Frequency, and Volcanic Activity are internal because they are properties of the boundary system that respond to convection and boundary type.",
    "relationships": [
        ("Mantle Convection Speed to Tectonic Stress", "POSITIVE (+)", "Faster mantle convection pushes plates harder, accumulating more stress at boundaries where plates interact. More convection energy means more force building up."),
        ("Tectonic Stress to Earthquake Frequency", "POSITIVE (+)", "Higher accumulated stress means more stored energy that must be released. This increases both the likelihood and frequency of seismic events at the boundary."),
        ("Plate Boundary Type to Volcanic Activity", "POSITIVE/NEGATIVE (+/-)", "Convergent boundaries produce volcanoes because subducting plates melt and create magma. Transform boundaries produce almost no volcanic activity because plates slide horizontally without subduction. Boundary type determines the volcanic hazard profile."),
        ("Earthquake Frequency to Tectonic Stress", "NEGATIVE (-)", "Earthquakes release accumulated stress, temporarily reducing the pressure at the boundary. This creates a negative feedback cycle: stress builds, earthquake releases, stress drops, then rebuilds over time."),
        ("Mantle Convection Speed to Volcanic Activity", "POSITIVE (+)", "Faster convection brings more heat to the surface, increasing magma production and volcanic activity at convergent and divergent boundaries.")
    ],
    "sim_answers": [
        ("Fast Convergent Scenario", "With high Mantle Convection Speed and a convergent boundary, both Earthquake Frequency and Volcanic Activity are high. The model shows tectonic stress building rapidly, triggering frequent earthquakes that periodically reduce stress. Volcanic Activity remains elevated because subduction continually creates new magma. This matches the real Ring of Fire profile."),
        ("Slow Transform Scenario", "With low Mantle Convection Speed and a transform boundary, Earthquake Frequency is moderate and Volcanic Activity is near zero. Stress builds more slowly but still accumulates. The model shows longer intervals between earthquakes but they still occur. The absence of volcanoes confirms that transform boundaries lack the subduction process needed for magma creation.")
    ],
    "reflection_exemplars": [
        ("Why do convergent boundaries have volcanoes but transform ones do not?", "At convergent boundaries, one plate dives under the other (subduction). The subducting plate descends into the hot mantle, where heat and pressure cause it to partially melt, creating magma. This magma rises through the overlying plate and erupts as volcanoes. At transform boundaries, plates slide PAST each other horizontally. Neither plate goes down into the mantle, so no melting occurs and no magma is produced. No magma means no volcanoes."),
        ("Why is earthquake timing unpredictable?", "While we know stress accumulates and must be released, the exact moment of failure depends on microscopic conditions in the rock: tiny fractures, water content, mineral composition, and temperature variations along the fault. It is like knowing a fraying rope will break but not which fiber fails first. The system is deterministic in principle but chaotic in practice. We can predict averages and probabilities, but not precise moments.")
    ],
    "stem_intro": "Present the challenge: A coastal city is located near an offshore subduction zone (convergent boundary) and an inland transform fault. The city council needs integrated warning and preparedness systems for both earthquake and volcanic/tsunami threats.",
    "stem_concepts": [
        ("Seismic Monitoring Networks", "Arrays of seismometers that detect P-waves (fast, less destructive) before S-waves (slow, destructive) arrive. This gives seconds to minutes of warning time for nearby earthquakes."),
        ("Earthquake Recurrence Intervals", "The average time between major earthquakes on a specific fault, based on historical records and geological evidence. Used to estimate future earthquake probabilities."),
        ("Tsunami Warning Systems", "Ocean buoys and coastal sensors that detect tsunami waves generated by undersea earthquakes at convergent boundaries, providing minutes to hours of warning for distant coastlines.")
    ],
    "stem_eval": [
        ("Expert (4)", "Warning system addresses both boundary types with specific hazard responses, uses model evidence for risk assessment, includes building codes and evacuation plans for each hazard type"),
        ("Proficient (3)", "System addresses earthquake and volcanic risks with model-based rationale and at least one emergency procedure"),
        ("Developing (2)", "System mentions hazards but does not differentiate between boundary types or connect to model evidence"),
        ("Beginning (1)", "System is incomplete or does not demonstrate understanding of plate tectonic hazards")
    ],
    "support": [
        "Provide a labeled diagram showing the three boundary types with their associated hazards side by side",
        "Use a stress ball or spring to physically demonstrate the stress-accumulation-and-release cycle",
        "Sentence frames: 'At a convergent boundary, volcanic activity is __ because __'"
    ],
    "extensions": [
        "Research the 2011 Tohoku earthquake and tsunami in Japan and explain it using your model of convergent boundary dynamics",
        "Compare the earthquake histories of the San Andreas Fault (transform) and the Cascadia Subduction Zone (convergent) in western North America",
        "Investigate how earthquake early warning systems like ShakeAlert work and calculate how much warning time they provide"
    ],
    "cross_curr": [
        ("Math", "Calculate the recurrence interval for a fault given a list of historical earthquake dates, then predict the probability of a quake in the next 30 years"),
        ("ELA", "Write an emergency preparedness guide for a family living near a plate boundary, explaining the science behind the hazards in accessible language"),
        ("Social Studies", "Research how earthquake-prone cities like Tokyo, San Francisco, and Mexico City have adapted their building codes, infrastructure, and emergency systems")
    ],
    "misconceptions": [
        ("Earthquakes are random events", "Earthquakes are NOT random. They occur at plate boundaries in patterns governed by stress accumulation and release. While we cannot predict exact timing, the locations and average frequencies are well understood and follow the physics of plate tectonics.", "Show a map of global earthquake locations overlaid on plate boundaries. The correlation is nearly perfect."),
        ("All plate boundaries are the same", "Each boundary type produces distinctly different hazards. Convergent boundaries create mountains, volcanoes, and deep earthquakes. Divergent boundaries create rift valleys and mid-ocean ridges. Transform boundaries create horizontal earthquake faults. Knowing the boundary type tells you WHAT to prepare for.", "Compare the hazards of San Andreas (transform, earthquakes only) vs. Mount St. Helens (convergent, eruptions and earthquakes)."),
        ("After a big earthquake, the area is safe for a long time", "While stress is temporarily reduced after a large earthquake, aftershocks can occur for weeks or months as the surrounding rock adjusts to the stress change. Additionally, releasing stress on one part of a fault can actually INCREASE stress on adjacent sections, potentially triggering earthquakes nearby.", "Show data from aftershock sequences following major earthquakes to demonstrate the cluster pattern.")
    ]
}

L04 = {
    "id": "G06L2-L04",
    "title": "Inside the Cell: The Factory That Runs Your Body",
    "subtitle": "How Mitochondria Power Every Move You Make",
    "ngss": "MS-LS1-1, MS-LS1-2",
    "ngss_desc": "Conduct an investigation to provide evidence that living things are made of cells; either one cell or many different numbers and types of cells. Develop and use a model to describe the function of a cell as a whole and ways the parts of cells contribute to the function.",
    "big_question": "Why do you need to eat food AND breathe oxygen just to stay alive, and what happens inside your cells that makes both essential?",
    "objectives": [
        "Model how nutrients and oxygen fuel mitochondria to produce ATP energy for the cell",
        "Explain the relationship between mitochondria activity, cell growth rate, and waste production",
        "Describe how waste buildup from cellular respiration limits cell growth and function",
        "Predict what happens to a cell when nutrient or oxygen supply is cut off",
        "Connect cellular respiration to the whole-body need for food and breathing"
    ],
    "vocabulary": [
        ("Mitochondria", "The organelles known as the cell's power plants that convert glucose and oxygen into ATP energy through cellular respiration"),
        ("ATP", "Adenosine triphosphate, the energy currency of the cell that powers all cellular activities from growth to movement"),
        ("Cellular Respiration", "The chemical process in mitochondria that combines glucose and oxygen to produce ATP energy, carbon dioxide, and water"),
        ("Metabolic Waste", "Byproducts of cellular processes, including carbon dioxide and other compounds that must be removed to prevent toxic buildup"),
        ("Cell Growth Rate", "How fast a cell divides and increases in size, directly dependent on available ATP energy from mitochondria")
    ],
    "components": [
        ("Nutrient Input", "The amount of glucose and other food molecules available to the cell for energy production", True),
        ("Oxygen Availability", "The concentration of oxygen reaching the cell, essential for efficient ATP production in mitochondria", True),
        ("Mitochondria Activity", "The rate at which mitochondria convert glucose and oxygen into ATP energy through cellular respiration", False),
        ("Cell Growth Rate", "How fast the cell can divide, build proteins, and maintain its structures, powered entirely by ATP", False),
        ("Waste Production", "The amount of carbon dioxide and metabolic waste produced as byproducts of cellular respiration", False)
    ],
    "think_about_it": "When nutrient input and oxygen availability both increase, what happens to mitochondria activity? If waste production increases, what happens to cell growth rate? Why do you breathe faster when you exercise?",
    "scenarios": [
        ("Healthy Cell", "Set Nutrient Input and Oxygen Availability to moderate-high levels and observe balanced cell function"),
        ("Oxygen Deprivation", "Lock Oxygen Availability to 10% while keeping nutrients normal and observe the shutdown cascade"),
        ("Nutrient Starvation", "Lock Nutrient Input to 10% while keeping oxygen normal and compare to the oxygen scenario")
    ],
    "sim_scenarios": [
        ("Healthy Cell", "Moderate-high nutrients and oxygen", "What do you predict will happen to cell growth rate when the cell has plenty of both inputs?"),
        ("Oxygen Deprivation", "Lock Oxygen to 10%, nutrients normal", "What do you predict happens to ATP production when the cell cannot get oxygen?"),
        ("Nutrient Starvation", "Lock Nutrients to 10%, oxygen normal", "How do you predict nutrient starvation differs from oxygen deprivation in its effect on the cell?")
    ],
    "discoveries": [
        "Mitochondria need BOTH glucose AND oxygen to produce ATP. Removing either one shuts down energy production",
        "Cell growth rate is directly proportional to ATP production. No energy means no growth, no repair, no division",
        "Waste production (CO2) increases with mitochondria activity. More energy production means more waste that must be removed",
        "Waste buildup is toxic. If the cell cannot remove waste fast enough, it poisons the cell and slows growth",
        "This is why you breathe faster during exercise: your muscle cells need more oxygen for ATP and must expel more CO2 waste"
    ],
    "answer": "You need food because glucose is the fuel your mitochondria burn. You need oxygen because it is the other reactant in cellular respiration. Inside every cell, mitochondria combine glucose and oxygen to produce ATP, the energy molecule that powers EVERYTHING your cells do. The byproducts are carbon dioxide (which you exhale) and water. Without either input, ATP production stops and cells cannot grow, repair, or even maintain themselves. That is why you die without food or air.",
    "stem_title": "Design a Cell Survival System",
    "stem_mission": "Design an emergency life-support system that keeps cells alive by maintaining optimal nutrient and oxygen delivery while removing waste products.",
    "stem_scenario": "A biotech company is designing an artificial organ support system for patients whose organs cannot supply cells with nutrients and oxygen efficiently. Your biomedical team must design a system that maintains cellular respiration in isolated tissue samples for 48 hours.",
    "stem_questions": [
        "Based on your model, what are the minimum levels of nutrients and oxygen needed to keep cells alive?",
        "What happens if your system delivers nutrients but fails to remove waste?",
        "How will you monitor cell health to know if your system is working?"
    ],
    "stem_design_qs": [
        "How will your system deliver nutrients and oxygen continuously to every cell in the tissue?",
        "What waste removal mechanism will prevent toxic buildup of CO2 and metabolic waste?",
        "How will you adjust delivery rates based on the tissue's metabolic demand?",
        "What sensors will monitor ATP production, waste levels, and cell health indicators?"
    ],
    "career": "Cell Biologists and Biomedical Engineers study how cells function at the molecular level and design medical devices, artificial organs, and drug delivery systems. They earn $60,000-$130,000/year.",
    "images": {
        "cover": ("cover-cell-factory.png", "A stunning photorealistic 3D rendering of the interior of a human cell showing glowing mitochondria producing energy, detailed organelles visible in cross-section, dramatic bioluminescent lighting on dark background"),
        "landscape": ("landscape-cell-factory.png", "6th grade students looking through microscopes at cell slides in a modern science lab, a Black student adjusting the focus while an Asian student draws observations, natural light from windows"),
        "modeling": ("modeling-cell-factory.png", "A diverse group of 6th grade students building a cell model on laptops, a White student pointing at mitochondria on screen while a Latino student compares nutrient input settings, modern classroom"),
        "discussion": ("discussion-cell-factory.png", "A teacher using a large cell diagram on a smartboard to explain cellular respiration, 6th grade students connecting the diagram to breathing and eating, engaged diverse classroom"),
        "stem": ("stem-cell-support.png", "6th grade students designing cell support system prototypes with tubing and containers, an Asian student assembling the delivery system while a Black student tests oxygen flow, hands-on STEM lab")
    },
    "pre_assessment": [
        "Why do you think you need to eat food every day? What does food actually do inside your body?",
        "Why do you need to breathe? What happens to the air once it enters your lungs?",
        "What do you think provides energy to your cells? Where does that energy come from?",
        "Draw what you think the inside of a cell looks like and label anything you know."
    ],
    "extend_components": [
        ("ATP Concentration", "The amount of energy currency available for cellular processes at any given moment"),
        ("Temperature", "Higher temperatures speed up chemical reactions in mitochondria, but extreme heat denatures enzymes"),
        ("Cell Membrane Permeability", "How easily nutrients and waste pass through the cell membrane, affecting supply and removal rates")
    ],
    "reflections": [
        "Why do you breathe faster when you exercise? Connect this to what is happening inside your muscle cells.",
        "What would happen to a cell if it had plenty of food but no oxygen?",
        "How is a cell like a factory? What are the raw materials, the product, and the waste?",
        "Why do some cells (like muscle cells) have MORE mitochondria than others?",
        "How does the waste produced by your cells eventually leave your body?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how nutrient input, oxygen availability, mitochondria activity, cell growth, and waste production are interconnected in a functioning cell."),
        ("Disciplinary Core Idea", "LS1.A Structure and Function", "Within cells, special structures are responsible for particular functions, and the cell membrane forms the boundary that controls what enters and leaves the cell."),
        ("Crosscutting Concept", "Energy and Matter: Flows, Cycles, and Conservation", "Students trace matter (glucose + oxygen in, CO2 + water out) and energy (chemical energy transformed to ATP then to heat) through the cellular respiration process.")
    ],
    "cast_items": [
        "Explain how mitochondria convert nutrient input and oxygen into usable energy for the cell",
        "Describe the relationship between cellular respiration and whole-body functions like breathing and eating",
        "Predict how removing one input (nutrients or oxygen) affects cell function"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A scientist observes that cells placed in a sealed container with glucose but no oxygen stop growing within hours. Which best explains why the cells stopped growing?"),
        ("Constructed Response:", "Using your cell model, explain why a person who is choking needs help within minutes while a person without food can survive for weeks. Reference mitochondria, ATP, and the role of oxygen vs. nutrients in cellular respiration.")
    ],
    "background_intro": "Every second, your cells are running a chemical factory inside their mitochondria. Cellular respiration is the process that converts the food you eat and the air you breathe into the energy that powers every heartbeat, every thought, and every movement.",
    "background_sections": [
        ("The Cellular Respiration Equation", "Glucose (C6H12O6) + Oxygen (6O2) yields Carbon Dioxide (6CO2) + Water (6H2O) + ATP Energy. This equation summarizes the most important chemical reaction in your body. Every molecule of glucose combined with oxygen produces approximately 36-38 molecules of ATP, plus waste products that your body exhales and excretes."),
        ("Mitochondria: The Powerhouses", "Mitochondria are double-membraned organelles with their own DNA (evidence they were once independent bacteria). A typical human cell contains 1,000-2,000 mitochondria, but high-energy cells like heart muscle cells can have 5,000+. They are constantly producing ATP through a complex series of chemical reactions on their inner membrane."),
        ("Why Two Inputs Are Required", "Glucose provides the carbon atoms and chemical energy. Oxygen serves as the final electron acceptor in the electron transport chain. Without oxygen, the respiration process backs up after glycolysis, producing only 2 ATP per glucose instead of 36-38. This is why oxygen deprivation kills faster than nutrient deprivation: the energy output drops by 95%."),
        ("Waste Must Be Removed", "Carbon dioxide is the primary waste product of cellular respiration. It dissolves in blood, travels to the lungs, and is exhaled. If CO2 builds up in cells, it lowers pH (increases acidity), which denatures enzymes and disrupts cell function. Your breathing rate automatically adjusts to match CO2 production, which is why you breathe harder during exercise.")
    ],
    "lever_L": "Students identify nutrient input and oxygen availability as the two external inputs, and mitochondria activity, cell growth rate, and waste production as the internal responses of the cellular system.",
    "lever_E": "Students determine that both nutrient input and oxygen positively drive mitochondria activity, mitochondria activity positively drives both cell growth rate and waste production, and waste production negatively affects cell growth rate.",
    "lever_V": "Students build a model showing how two inputs (food and oxygen) fuel the mitochondrial engine, producing both useful energy (ATP for growth) and harmful waste (CO2) that must be removed.",
    "lever_Ev": "Students run oxygen deprivation and nutrient starvation scenarios to compare how the cell responds differently to each type of input loss.",
    "lever_R": "Students add ATP concentration or temperature to explore how energy availability and reaction speed affect cell function.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with glowing mitochondria imagery", "say": "Right now, inside every one of your 37 trillion cells, tiny power plants are burning fuel and producing energy. Without them, you would be dead in minutes.", "do": "Show a 3D animation or image of mitochondria producing ATP. Build awe about cellular machinery.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are going to explore the factory inside every cell that keeps you alive.", "do": "Have students read objectives. Pre-teach 'mitochondria,' 'ATP,' and 'cellular respiration.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why food AND oxygen?", "say": "You eat food for energy. You breathe for oxygen. But what happens when they meet inside your cells?", "do": "Think-pair-share: Why do you think you need BOTH food and air? Would one work without the other?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "Our model has two external inputs feeding one central engine. Both are required.", "do": "Preview the two-input structure. Explain that removing either one crashes the system.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for cell model", "say": "What does a cell need to come in from outside? What processes happen inside?", "do": "Guide sorting. Emphasize that nutrients and oxygen are EXTERNAL (come from outside the cell).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows showing inputs to mitochondria to outputs", "say": "Mitochondria take in glucose and oxygen and produce ATP energy AND waste. More activity means more of BOTH.", "do": "Draw the cellular respiration equation. Connect each part to a model component.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions for healthy cell vs. deprived scenarios", "say": "What happens if we cut off the oxygen? What about cutting off food? Are the results the same?", "do": "Students predict before running. Compare oxygen deprivation (rapid crash) vs. nutrient starvation (slower decline).", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings connecting cell to whole body", "say": "Now you know WHY you breathe. Every breath delivers oxygen to your mitochondria. Every meal delivers glucose. You are fueling 37 trillion tiny engines.", "do": "Connect the cell model to whole-body systems: lungs deliver O2, digestive system delivers glucose, blood transports both.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Cell support system design", "say": "You are biomedical engineers. Can you keep isolated cells alive for 48 hours?", "do": "Distribute materials and constraints. Groups design nutrient delivery and waste removal systems.", "time": "12 min"}
    ],
    "sort_reasoning": "Nutrient Input and Oxygen Availability are external because they must be supplied from outside the cell, through the bloodstream and cell membrane. Mitochondria Activity, Cell Growth Rate, and Waste Production are internal because they are processes and outputs within the cell that respond to the external inputs.",
    "relationships": [
        ("Nutrient Input to Mitochondria Activity", "POSITIVE (+)", "More glucose available means more fuel for cellular respiration. Mitochondria can produce more ATP when glucose supply is abundant."),
        ("Oxygen Availability to Mitochondria Activity", "POSITIVE (+)", "More oxygen allows the electron transport chain to run efficiently, producing 36-38 ATP per glucose. Without oxygen, only 2 ATP are produced."),
        ("Mitochondria Activity to Cell Growth Rate", "POSITIVE (+)", "More ATP production means more energy available for cell division, protein synthesis, and structure maintenance. Energy is the limiting factor for growth."),
        ("Mitochondria Activity to Waste Production", "POSITIVE (+)", "More cellular respiration produces more CO2 and metabolic waste as byproducts. Higher activity means higher waste output."),
        ("Waste Production to Cell Growth Rate", "NEGATIVE (-)", "Excess waste (especially CO2) lowers cell pH and damages enzymes. If waste removal cannot keep up with production, toxic buildup slows growth and can kill the cell.")
    ],
    "sim_answers": [
        ("Oxygen Deprivation Scenario", "When Oxygen Availability is locked at 10%, Mitochondria Activity drops dramatically because the electron transport chain cannot function. ATP production falls by approximately 95%. Cell Growth Rate crashes rapidly and Waste Production initially drops but the cell begins producing lactic acid as a less efficient alternative. The cell begins dying within minutes. This is why choking is a medical emergency."),
        ("Nutrient Starvation Scenario", "When Nutrient Input is locked at 10%, Mitochondria Activity decreases because there is less glucose fuel to burn. The decline is more gradual than oxygen deprivation because cells have some stored glycogen and can break down fats and proteins for fuel. Cell Growth Rate slows and the cell enters a conservation mode. This is why you can survive weeks without food but only minutes without air.")
    ],
    "reflection_exemplars": [
        ("Why do you breathe faster during exercise?", "During exercise, your muscle cells need more ATP to power contractions. More ATP means mitochondria must work harder, consuming more oxygen and glucose and producing more CO2 waste. Your breathing rate increases to deliver more oxygen to cells AND to expel the extra CO2. Your heart rate also increases to transport these materials faster through your blood. The whole-body response is driven by cellular-level demand."),
        ("Why do muscle cells have more mitochondria?", "Muscle cells require enormous amounts of ATP for contraction. A resting muscle cell might need 100 ATP molecules per second, but a working muscle cell needs thousands per second. More mitochondria means more factories producing ATP simultaneously. Heart muscle cells have the most mitochondria of any cell type because the heart never rests. It is a direct relationship: higher energy demand means more power plants needed.")
    ],
    "stem_intro": "Present the challenge: A biotech company needs to keep isolated tissue samples alive outside the body for 48 hours during transport. Your team must design a support system that delivers nutrients and oxygen while removing waste, mimicking what the bloodstream normally does.",
    "stem_concepts": [
        ("Perfusion", "The delivery of blood or nutrient fluid through tissue to supply cells with oxygen and glucose. Artificial perfusion systems mimic what the heart and blood vessels do naturally."),
        ("Gas Exchange", "The process of delivering oxygen and removing carbon dioxide, normally handled by the lungs. In a support system, this can be done by bubbling oxygen through the nutrient solution."),
        ("Bioreactor Design", "An engineered system that supports biological processes by controlling temperature, pH, nutrient supply, oxygen levels, and waste removal to keep cells alive and functioning.")
    ],
    "stem_eval": [
        ("Expert (4)", "System delivers both nutrients and oxygen, removes waste, includes monitoring sensors, and connects design choices to model evidence about cellular respiration"),
        ("Proficient (3)", "System addresses nutrient and oxygen delivery with waste removal plan and model evidence"),
        ("Developing (2)", "System delivers nutrients but does not adequately address oxygen supply or waste removal"),
        ("Beginning (1)", "System is incomplete or does not demonstrate understanding of cellular respiration requirements")
    ],
    "support": [
        "Provide a simplified cellular respiration diagram showing glucose + oxygen entering mitochondria and ATP + CO2 exiting",
        "Use a bicycle pump analogy: air (oxygen) and fuel (food) go in, energy (pedaling) and exhaust (CO2) come out",
        "Sentence frames: 'When oxygen availability decreases, mitochondria activity __ because __'"
    ],
    "extensions": [
        "Research why mitochondria have their own DNA and what this tells us about cell evolution (endosymbiosis theory)",
        "Investigate mitochondrial diseases and explain symptoms using your model of cellular energy production",
        "Compare aerobic respiration (with oxygen, 36 ATP) to anaerobic respiration (without oxygen, 2 ATP) and explain why muscles burn during intense exercise"
    ],
    "cross_curr": [
        ("Math", "Calculate the ATP production efficiency difference between aerobic (36 ATP/glucose) and anaerobic (2 ATP/glucose) respiration as a percentage"),
        ("ELA", "Write a day-in-the-life narrative from the perspective of a mitochondrion inside a marathon runner's muscle cell"),
        ("Health/PE", "Explain why warm-up exercises help athletic performance by connecting to oxygen delivery and mitochondria activity")
    ],
    "misconceptions": [
        ("Energy comes from food directly", "Food does not power your cells directly. The chemical energy in glucose must be converted to ATP by mitochondria before cells can use it. It is like how you cannot put crude oil directly in a car engine; it must be refined into gasoline first. Mitochondria are your cellular refineries.", "Analogy: food is crude oil, mitochondria are refineries, ATP is gasoline, cell activities are the car engine."),
        ("You breathe in oxygen and breathe out the same air minus oxygen", "The air you exhale contains carbon dioxide that was NOT in the air you inhaled. The carbon atoms come from glucose (food). During cellular respiration, carbon from food combines with oxygen to form CO2. You are literally breathing out atoms that were in your breakfast.", "Weigh students before and after exercise. The tiny weight loss is CO2 from food being exhaled."),
        ("Cells use energy, so energy disappears", "Energy is never created or destroyed (First Law of Thermodynamics). The chemical energy in glucose is converted to ATP energy in mitochondria. When ATP is used for cell work, that energy becomes heat. Your body temperature (37 degrees C) is maintained by the heat produced by trillions of mitochondria. Energy transforms but never disappears.", "Feel your own skin. That warmth IS the heat from your mitochondria working. You are warm because of cellular respiration.")
    ]
}

L05 = {
    "id": "G06L2-L05",
    "title": "Atoms Rearrange: Modeling Chemical Reactions",
    "subtitle": "Conservation of Mass in Action",
    "ngss": "MS-PS1-2, MS-PS1-5",
    "ngss_desc": "Analyze and interpret data on the properties of substances before and after the substances interact to determine if a chemical reaction has occurred. Develop and use a model to describe how the total number of atoms does not change in a chemical reaction and thus mass is conserved.",
    "big_question": "If atoms are never created or destroyed in a chemical reaction, why do some reactions seem to make things disappear?",
    "objectives": [
        "Model how reactant concentration and temperature affect the rate of a chemical reaction",
        "Demonstrate conservation of mass by tracking total mass as reactants convert to products",
        "Explain why reactants decrease and products increase as mirror images of each other",
        "Predict how changing temperature or concentration affects the speed of product formation",
        "Connect the conservation of mass model to real-world chemical reactions like rusting and combustion"
    ],
    "vocabulary": [
        ("Reactant", "A starting substance that enters a chemical reaction and is transformed into products through atomic rearrangement"),
        ("Product", "A new substance formed by a chemical reaction when atoms from reactants rearrange into different molecular configurations"),
        ("Conservation of Mass", "The law that states the total mass of reactants must equal the total mass of products because atoms are neither created nor destroyed"),
        ("Reaction Rate", "The speed at which reactants are converted into products, affected by temperature, concentration, and surface area"),
        ("Chemical Equation", "A symbolic representation of a chemical reaction showing reactant and product formulas with balanced atom counts")
    ],
    "components": [
        ("Reactant Concentration", "The amount of starting materials available for the reaction, which decreases as the reaction proceeds", True),
        ("Temperature", "The thermal energy applied to the reaction system, which affects how fast molecules collide and react", True),
        ("Reaction Rate", "How fast reactants are being converted into products, proportional to both concentration and temperature", False),
        ("Product Formation", "The amount of new substance being created as atoms rearrange from reactant molecules to product molecules", False),
        ("Total Mass", "The combined mass of all reactants and products in the system, which remains constant throughout the reaction", False)
    ],
    "think_about_it": "When reactant concentration increases, what happens to reaction rate? As the reaction proceeds and reactants are used up, what happens to the reaction rate? Why does total mass never change?",
    "scenarios": [
        ("Fast Reaction", "Set Reactant Concentration and Temperature both to high and observe rapid product formation"),
        ("Slow Reaction", "Set Temperature to low while keeping Reactant Concentration high and compare rates"),
        ("Running Out", "Start with high reactants and observe how reaction rate slows as reactants are consumed")
    ],
    "sim_scenarios": [
        ("Fast Reaction", "High concentration, high temperature", "What do you predict will happen to the Reactant Concentration line as Product Formation rises?"),
        ("Slow Reaction", "High concentration, low temperature", "How will the reaction graph differ from the fast reaction scenario? Will the same amount of product eventually form?"),
        ("Running Out", "High start, observe decline over time", "What do you predict happens to the reaction rate as reactants get used up? Does it stay constant?")
    ],
    "discoveries": [
        "Reactant and product lines are INVERSE: as one goes down, the other goes up by exactly the same amount",
        "Total Mass stays perfectly flat throughout the reaction, proving conservation of mass",
        "Higher temperature increases reaction rate because molecules collide more frequently and with more energy",
        "As reactants are consumed, the reaction rate SLOWS because there are fewer molecules available to collide",
        "Atoms are not created or destroyed. They just rearrange from one molecular configuration to another"
    ],
    "answer": "Things seem to disappear in reactions because the products are sometimes invisible. When wood burns, the solid wood seems to vanish, but it has actually combined with oxygen to form carbon dioxide gas and water vapor. The atoms did not disappear; they rearranged into gases that float away. If you could capture and weigh ALL the products (including gases), the total mass would exactly equal the original wood plus the oxygen consumed.",
    "stem_title": "Design a Conservation of Mass Experiment",
    "stem_mission": "Design and execute a sealed-system experiment that proves conservation of mass during a chemical reaction.",
    "stem_scenario": "A science magazine is challenging student teams to prove conservation of mass using everyday chemical reactions. Your team must design an experiment where you can measure the total mass before and after a reaction in a sealed system, proving that mass is conserved even when gases are produced.",
    "stem_questions": [
        "Why must the system be sealed to prove conservation of mass? What happens if it is open?",
        "What chemical reaction will you use and what evidence shows a reaction occurred?",
        "How precisely do you need to measure mass to detect any difference?"
    ],
    "stem_design_qs": [
        "What chemical reaction will you use (baking soda + vinegar, steel wool rusting, etc.)?",
        "How will you seal the system so no gases escape?",
        "How will you measure mass accurately before and after the reaction?",
        "What evidence will show that a chemical reaction actually occurred (not just mixing)?"
    ],
    "career": "Chemical Engineers design and optimize chemical reactions for manufacturing everything from medicines to fuels to plastics. They apply conservation of mass to scale reactions from lab to industrial size. They earn $75,000-$140,000/year.",
    "images": {
        "cover": ("cover-chemical-reactions.png", "A photorealistic close-up of a dramatic chemical reaction in a beaker with colorful precipitates forming, dry ice fog, and vibrant liquid layers, laboratory setting with scientific precision"),
        "landscape": ("landscape-chemical-reactions.png", "6th grade students wearing safety goggles conducting a chemistry experiment, a White student carefully measuring baking soda while a Black student records observations, bright modern science lab"),
        "modeling": ("modeling-chemical-reactions.png", "A diverse group of 6th grade students building a chemical reaction model on laptops, a Latino student highlighting the total mass line while an Asian student compares reactant and product curves, modern classroom"),
        "discussion": ("discussion-chemical-reactions.png", "A teacher holding a sealed flask before and after a reaction, demonstrating conservation of mass on a balance scale to engaged 6th grade students, diverse classroom with chemistry equipment"),
        "stem": ("stem-sealed-reaction.png", "6th grade students designing sealed-system experiments with plastic bags, bottles, and digital scales, a Black student sealing a reaction vessel while a White student reads the scale, collaborative lab work")
    },
    "pre_assessment": [
        "When you burn a piece of paper, it seems to disappear. Where do you think the material goes?",
        "If you mix baking soda and vinegar in a sealed bag, do you think the bag will weigh more, less, or the same after the reaction?",
        "What do you think atoms do during a chemical reaction? Do they change into different atoms?",
        "Draw what you think happens to atoms when wood burns."
    ],
    "extend_components": [
        ("Surface Area", "Crushed or powdered reactants react faster because more molecules are exposed for collisions"),
        ("Catalyst Presence", "A substance that speeds up a reaction without being consumed, lowering the energy needed to start the reaction"),
        ("Equilibrium Point", "The state where forward and reverse reactions occur at equal rates, and concentrations stop changing")
    ],
    "reflections": [
        "Why do reactant and product lines on the graph look like mirror images of each other?",
        "If mass is conserved, why does a log seem lighter after it burns?",
        "Why does the reaction rate slow down even when temperature stays the same?",
        "How is conservation of mass related to the idea that atoms are never created or destroyed?",
        "How could you prove that a burned match has the same total mass as before, including all products?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how reactant concentration and temperature affect reaction rate and product formation while total mass remains conserved."),
        ("Disciplinary Core Idea", "PS1.B Chemical Reactions", "Substances react chemically in characteristic ways. In a chemical process, the atoms that make up the original substances are regrouped into different molecules, and these new substances have different properties from those of the reactants."),
        ("Crosscutting Concept", "Energy and Matter: Flows, Cycles, and Conservation", "Students demonstrate that matter is conserved during chemical reactions. The total number of atoms of each element is the same before and after the reaction, even though atoms rearrange.")
    ],
    "cast_items": [
        "Demonstrate that total mass is conserved before and after a chemical reaction",
        "Explain how atoms rearrange during a chemical reaction without being created or destroyed",
        "Predict how changing temperature or concentration affects reaction rate"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student mixes 50 grams of baking soda with 100 grams of vinegar in an open beaker. After the reaction stops, the beaker and contents weigh 140 grams. What best explains the missing 10 grams?"),
        ("Constructed Response:", "A student claims that burning a log destroys matter because the ashes weigh less than the original log. Using the law of conservation of mass and your model of chemical reactions, explain why this claim is incorrect. Include what happens to the atoms in the log.")
    ],
    "background_intro": "Conservation of mass is one of the most fundamental laws in all of science. Antoine Lavoisier established it in the 1770s, earning him the title 'Father of Modern Chemistry.' Every chemical reaction in the universe obeys this law without exception.",
    "background_sections": [
        ("Lavoisier's Discovery", "Before Lavoisier, scientists believed that burning destroyed matter. Lavoisier designed careful experiments with sealed containers and precise measurements, proving that the total mass before and after a reaction is identical. He showed that burning requires oxygen from the air and produces gases. No mass is lost; it just changes form."),
        ("Atoms Rearrange, Not Transform", "In a chemical reaction, atoms do not change identity. A carbon atom stays a carbon atom. An oxygen atom stays an oxygen atom. What changes is how atoms are connected to each other. In burning wood, carbon atoms bonded to hydrogen and oxygen in cellulose molecules break apart and rebond with oxygen from the air to form CO2 and H2O. Same atoms, new arrangement."),
        ("Why Reactions Seem to Destroy Matter", "Reactions appear to destroy matter because products are often gases that disperse into the air. Burning wood produces CO2 and water vapor that float away, leaving only ash (minerals that did not combust). In an open system, the gases escape and the remaining solid weighs less. In a sealed system, all products stay, and the mass is identical."),
        ("Reaction Rate Factors", "Temperature increases reaction rate because molecules move faster and collide more often with more energy. Higher concentration increases rate because more molecules are packed together, increasing collision frequency. Surface area matters because reactions happen at surfaces where molecules can contact each other. Catalysts lower the energy barrier for reactions without being consumed.")
    ],
    "lever_L": "Students identify reactant concentration and temperature as external inputs, and reaction rate, product formation, and total mass as internal properties of the reaction system.",
    "lever_E": "Students determine that both reactant concentration and temperature positively drive reaction rate, reaction rate positively drives product formation, and reaction rate negatively affects reactant concentration (reactants get used up). Total mass remains constant.",
    "lever_V": "Students build a model showing reactant and product lines as inverse curves with a flat total mass line, demonstrating conservation of mass.",
    "lever_Ev": "Students run fast vs. slow reaction scenarios and observe that while the RATE changes, the total mass is always conserved, and the same final amounts of products form.",
    "lever_R": "Students add surface area or catalyst presence to explore additional factors that affect reaction rate without changing total mass.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic chemical reaction imagery", "say": "When you burn a match, the wood seems to vanish. But here is a mind-bending fact: NOT ONE ATOM was destroyed. So where did it all go?", "do": "Light a match (or show video). Ask students: Where did the wood go? Capture responses.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are going to prove that matter is NEVER created or destroyed. Atoms just rearrange.", "do": "Have students read objectives. Pre-teach 'reactant,' 'product,' and 'conservation of mass.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Where does matter go in reactions?", "say": "A 10-pound log burns down to a few ounces of ash. Where did the other 9+ pounds go?", "do": "Think-pair-share: Does burning destroy matter? Students write predictions before discussion.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "Our model will show two lines that are perfect mirror images, and one line that NEVER moves. That flat line is the key.", "do": "Preview the 5 components. Tease that one variable (total mass) will stay perfectly constant.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for reaction model", "say": "What can we control in a chemical reaction? What responds? What stays the same no matter what?", "do": "Guide sorting. Emphasize that Total Mass is internal but CONSTANT. This is the conservation law.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows showing inverse reactant/product curves", "say": "As reactants go DOWN, products go UP by the exact same amount. They are perfect inverses. This is conservation.", "do": "Use physical model: start with 20 red blocks (reactants), convert to blue blocks (products) one at a time. Count total at each step.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions vs. actual reaction curves", "say": "Let's run a fast reaction and a slow reaction. The rates change, but watch that total mass line.", "do": "Students predict graphs first. Run fast and slow scenarios. Overlay graphs. Point to the flat mass line.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings and conservation law", "say": "Lavoisier proved this 250 years ago and it has NEVER been violated. Every reaction in the universe conserves mass.", "do": "Connect to the burning log question. Explain that gases (CO2, H2O vapor) carry the missing mass away.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Sealed-system experiment design", "say": "Prove it yourself. Design an experiment that captures ALL products and shows mass is conserved.", "do": "Distribute materials (bags, bottles, scales). Groups design, execute, and measure sealed reactions.", "time": "12 min"}
    ],
    "sort_reasoning": "Reactant Concentration and Temperature are external because the student controls these as initial conditions and adjustments. Reaction Rate, Product Formation, and Total Mass are internal because they are calculated by the system. Total Mass is unique because it stays constant regardless of what the student changes.",
    "relationships": [
        ("Reactant Concentration to Reaction Rate", "POSITIVE (+)", "More reactant molecules means more collisions per second, driving a faster reaction rate. As reactants are consumed, the rate naturally slows."),
        ("Temperature to Reaction Rate", "POSITIVE (+)", "Higher temperature makes molecules move faster, collide more often, and collide with more energy. This speeds up the reaction rate significantly."),
        ("Reaction Rate to Product Formation", "POSITIVE (+)", "A faster reaction rate means products are being created more quickly. The product line rises faster when reaction rate is high."),
        ("Reaction Rate to Reactant Concentration", "NEGATIVE (-)", "As the reaction proceeds, it consumes reactants. Higher reaction rate means reactants are consumed faster, causing concentration to drop. This creates a self-slowing effect."),
        ("Total Mass: CONSTANT", "CONSERVATION", "Total Mass never changes because atoms are neither created nor destroyed. As reactant mass decreases, product mass increases by exactly the same amount. The sum is always constant.")
    ],
    "sim_answers": [
        ("Fast Reaction Scenario", "With high Reactant Concentration and high Temperature, the reaction proceeds quickly. The Reactant line drops steeply while the Product line rises steeply. They are mirror images. The reaction rate starts high but slows as reactants are consumed. Critically, the Total Mass line remains perfectly flat at 100%. This proves conservation of mass even during a fast reaction."),
        ("Running Out Scenario", "Starting with high reactants, the reaction rate begins fast because many molecules are available to collide. As reactants are consumed, fewer molecules remain, so collisions become rarer and the rate slows. Eventually the reaction stops when all reactants are converted to products. The graph shows a curve that flattens, not a straight line. This is the same self-slowing pattern seen in cooling curves.")
    ],
    "reflection_exemplars": [
        ("Why does a burned log seem lighter?", "The log is made of carbon, hydrogen, and oxygen atoms in cellulose molecules. When burned, these atoms combine with oxygen from the air to form CO2 gas and water vapor. These gases float away into the atmosphere. The ash that remains is only the mineral atoms that did not combust. If you could capture and weigh ALL the CO2 and H2O produced, plus the ash, the total would equal the original log weight plus the oxygen consumed. Mass is conserved; it just changed form and location."),
        ("Why does reaction rate slow as reactants decrease?", "Reaction rate depends on how often molecules collide. With many reactant molecules, collisions are frequent and the reaction is fast. As molecules are converted to products, fewer reactant molecules remain in the solution. Fewer molecules means fewer collisions per second, which means a slower reaction. It is like a room full of people bumping into each other. Remove half the people and collisions happen less often.")
    ],
    "stem_intro": "Present the challenge: Design and execute a sealed-system experiment that proves conservation of mass. Use a chemical reaction that produces visible evidence of change (gas production, color change, precipitate) while keeping all products contained for measurement.",
    "stem_concepts": [
        ("Closed vs. Open Systems", "A closed system does not allow matter to enter or leave. Conservation of mass is easiest to demonstrate in closed systems where gases cannot escape. Open system reactions lose gaseous products to the air."),
        ("Precision Measurement", "Proving conservation requires precise mass measurements. A difference of even 0.1 grams could be due to gas escape, not mass destruction. Analytical balances measure to 0.001 grams for this reason."),
        ("Evidence of Chemical Change", "Signs that a chemical reaction occurred include: gas production (bubbles), color change, temperature change, precipitate formation, and new odor. These distinguish chemical reactions from physical mixing.")
    ],
    "stem_eval": [
        ("Expert (4)", "Experiment uses sealed system, measures mass precisely before and after, demonstrates conservation, shows evidence of chemical change, and explains results using atomic rearrangement"),
        ("Proficient (3)", "Sealed system experiment with mass measurements and evidence of chemical change"),
        ("Developing (2)", "Experiment shows a chemical reaction but does not adequately seal the system or measure mass precisely"),
        ("Beginning (1)", "Experiment is incomplete or does not demonstrate understanding of conservation of mass")
    ],
    "support": [
        "Provide a labeled diagram of atoms rearranging in a simple reaction (like 2H2 + O2 -> 2H2O) with atom counts before and after",
        "Use physical blocks or beads to represent atoms: rearrange them into new 'molecules' and count that the total never changes",
        "Sentence frames: 'When reactant concentration decreases, the reaction rate __ because __'"
    ],
    "extensions": [
        "Research nuclear reactions where mass IS converted to energy (E=mc2) and explain why conservation of mass does not fully apply",
        "Design an experiment to measure the mass of CO2 produced when baking soda reacts with vinegar",
        "Investigate how industrial chemical plants use conservation of mass to calculate how much raw material they need for a given amount of product"
    ],
    "cross_curr": [
        ("Math", "Balance simple chemical equations by counting atoms on each side, proving conservation of mass algebraically"),
        ("ELA", "Write an argument essay: Does burning destroy matter? Use evidence from your experiment and model to support your claim"),
        ("History", "Research Antoine Lavoisier's life and experiments that overturned the phlogiston theory and established conservation of mass")
    ],
    "misconceptions": [
        ("Burning destroys matter", "Burning is a chemical reaction between fuel and oxygen that produces new substances (CO2, H2O) as gases. These gases float away, making it LOOK like matter disappeared. In a sealed container, the mass before and after burning is identical. Not one atom is destroyed.", "Burn steel wool in a sealed flask on a balance. The mass does not change even though the steel wool looks destroyed."),
        ("Heavier products mean mass was created", "When iron rusts, it gains mass because it combines with oxygen from the air. The oxygen atoms were already there in the atmosphere. No mass was created; it was transferred from the air to the iron. The total mass of the system (iron + air) stays the same.", "Weigh a sealed container with iron and moist air. After rusting, the container weighs the same. The iron gained what the air lost."),
        ("Chemical reactions create new atoms", "Atoms are NEVER created or destroyed in chemical reactions. Only nuclear reactions (fusion, fission) change atom identities. In chemistry, atoms simply rearrange their connections. Carbon stays carbon. Oxygen stays oxygen. The only thing that changes is which atoms are bonded to which.", "Count the atoms in the equation for burning methane: CH4 + 2O2 -> CO2 + 2H2O. Same atoms on both sides, just rearranged.")
    ]
}

L06 = {
    "id": "G06L2-L06",
    "title": "The Invisible Plant Factory: Photosynthesis Deeper",
    "subtitle": "How Plants Build Themselves from Thin Air and Sunlight",
    "ngss": "MS-LS1-6, MS-LS1-7",
    "ngss_desc": "Construct a scientific explanation based on evidence for the role of photosynthesis in the cycling of matter and flow of energy into and out of organisms. Develop a model to describe how food is rearranged through chemical reactions forming new molecules that support growth and/or release energy as this matter moves through an organism.",
    "big_question": "A giant redwood tree weighs over 2 million pounds, but it started as a tiny seed. Where did all that mass actually come from?",
    "objectives": [
        "Model how light intensity, CO2 concentration, and water availability all contribute to photosynthesis",
        "Explain how glucose production from photosynthesis drives both oxygen release and plant biomass growth",
        "Demonstrate that the mass of a plant comes primarily from carbon dioxide in the air, not from soil",
        "Predict how removing any one input (light, CO2, or water) stops the entire photosynthesis process",
        "Connect photosynthesis to the global carbon cycle and atmospheric oxygen maintenance"
    ],
    "vocabulary": [
        ("Photosynthesis", "The chemical process in which plants use light energy to convert carbon dioxide and water into glucose and oxygen"),
        ("Glucose", "A simple sugar (C6H12O6) produced by photosynthesis that serves as the primary energy storage and building block molecule for plants"),
        ("Chloroplast", "The organelle in plant cells that contains chlorophyll and performs photosynthesis, capturing light energy"),
        ("Carbon Fixation", "The process of converting inorganic carbon dioxide gas into organic carbon molecules like glucose, adding mass to the plant"),
        ("Limiting Factor", "The resource in shortest supply that constrains the rate of photosynthesis, regardless of how abundant other resources are")
    ],
    "components": [
        ("Light Intensity", "The amount of sunlight energy reaching the leaf, which powers the photosynthesis reaction", True),
        ("CO2 Concentration", "The amount of carbon dioxide available in the air around the leaf for carbon fixation", True),
        ("Water Availability", "The amount of water reaching the leaf through roots and stem, providing hydrogen atoms and electrons", True),
        ("Glucose Production", "The rate at which the plant produces sugar from CO2, water, and light energy through photosynthesis", False),
        ("Oxygen Released", "The amount of O2 produced as a byproduct of splitting water molecules during photosynthesis", False),
        ("Plant Biomass Growth", "The increase in plant mass as glucose is used to build cellulose, proteins, and other structural molecules", False)
    ],
    "think_about_it": "If you increase light intensity but keep CO2 very low, what happens to glucose production? Why does the plant need ALL THREE inputs and not just one or two?",
    "scenarios": [
        ("Full Sun", "Set all three inputs (Light, CO2, Water) to maximum and observe peak photosynthesis"),
        ("Darkness", "Lock Light Intensity to 0% and observe what happens even with abundant CO2 and water"),
        ("Drought", "Lock Water Availability to 10% with normal light and CO2 to observe the limiting factor effect")
    ],
    "sim_scenarios": [
        ("Full Sun", "All inputs maximized", "What do you predict will happen to Glucose Production and Oxygen Released at maximum inputs?"),
        ("Darkness", "Lock Light to 0%, other inputs normal", "What do you predict happens to the entire photosynthesis system without light?"),
        ("Drought", "Lock Water to 10%, other inputs normal", "Even with plenty of light and CO2, what happens during drought? Which input is the limiting factor?")
    ],
    "discoveries": [
        "Photosynthesis requires ALL THREE inputs: light, CO2, and water. Removing any one of them stops the entire process",
        "Glucose production is limited by whichever input is in shortest supply (the limiting factor), not by the most abundant one",
        "Most of a plant's mass comes from carbon dioxide gas in the air, NOT from soil. Trees are made of air!",
        "Oxygen is a BYPRODUCT, not the purpose of photosynthesis. Plants make oxygen because they must split water molecules",
        "The photosynthesis equation (6CO2 + 6H2O + light -> C6H12O6 + 6O2) shows matter conservation: same atoms in and out"
    ],
    "answer": "A 2-million-pound redwood got almost all its mass from CARBON DIOXIDE in the air! Through photosynthesis, the tree combines CO2 from the atmosphere with water from the soil, using sunlight as energy. The carbon atoms from CO2 become the carbon backbone of glucose, which is then used to build cellulose, lignin, and every other molecule in the tree. A tree is literally built from air and water, powered by sunlight. The soil provides only minerals, which make up less than 5% of the tree's mass.",
    "stem_title": "Design a Plant Growth Optimization Chamber",
    "stem_mission": "Design a growth chamber that maximizes photosynthesis and plant biomass production by optimizing light, CO2, and water delivery.",
    "stem_scenario": "A vertical farming company wants to grow food in urban buildings without natural sunlight. Your agricultural engineering team must design a growth chamber that delivers optimal light, CO2, and water to maximize plant production efficiency.",
    "stem_questions": [
        "Based on your model, which input is most likely to be the limiting factor in an indoor growing system?",
        "How will you ensure all three inputs are optimized, not just one?",
        "How will you measure whether your optimization actually increases plant growth?"
    ],
    "stem_design_qs": [
        "What type of artificial light will you use and how many hours per day will it run?",
        "How will you supplement CO2 levels above normal atmospheric concentration?",
        "What watering system will deliver water efficiently without waterlogging the roots?",
        "How will you measure biomass growth over time to evaluate your chamber's effectiveness?"
    ],
    "career": "Plant Biologists and Agricultural Engineers study photosynthesis and design systems to optimize crop production, including vertical farms, greenhouses, and space agriculture. They earn $55,000-$120,000/year.",
    "images": {
        "cover": ("cover-photosynthesis.png", "A photorealistic macro photograph of a vibrant green leaf with visible cellular structure backlit by golden sunlight, water droplets on the surface catching light like jewels, dramatic botanical photography"),
        "landscape": ("landscape-photosynthesis.png", "6th grade students examining plants under grow lights in a classroom, a Latino student measuring leaf growth while a White student adjusts the light height, bright and green indoor garden setting"),
        "modeling": ("modeling-photosynthesis.png", "A diverse group of 6th grade students building a photosynthesis model on laptops, a Black student toggling light intensity while an Asian student observes the glucose production graph, modern classroom with plants on windowsill"),
        "discussion": ("discussion-photosynthesis.png", "A teacher explaining the photosynthesis equation on a whiteboard while 6th grade students connect it to their model components, diverse students with plant specimens on their desks"),
        "stem": ("stem-growth-chamber.png", "6th grade students building small plant growth chambers with LED lights and clear containers, a White student wiring lights while a Latino student plants seedlings, hands-on engineering project")
    },
    "pre_assessment": [
        "Where do you think plants get the material to grow? Is it from the soil, the air, water, or sunlight?",
        "If you put a plant in a dark closet with plenty of water and soil, what would happen and why?",
        "Where does the oxygen you breathe come from? How is it made?",
        "A tree can weigh thousands of pounds but grows from a tiny seed. Where does all that weight come from?"
    ],
    "extend_components": [
        ("Temperature", "Photosynthesis enzymes work fastest at optimal temperatures. Too cold or too hot slows or stops the process"),
        ("Chlorophyll Concentration", "More chlorophyll means more light can be captured. Pale or yellowing leaves photosynthesize less"),
        ("Stomata Openness", "Pores on leaves that open to let CO2 in but also let water vapor out, creating a tradeoff between photosynthesis and water conservation")
    ],
    "reflections": [
        "Why is it surprising that most of a tree's mass comes from air rather than soil?",
        "If you increase light but not CO2, why does photosynthesis eventually plateau?",
        "How is photosynthesis the reverse of cellular respiration? What do they share?",
        "Why do plants produce oxygen even though they do not need it?",
        "How does understanding limiting factors help farmers grow more food?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model with three external inputs showing how light, CO2, and water interact to produce glucose, oxygen, and plant growth."),
        ("Disciplinary Core Idea", "LS1.C Organization for Matter and Energy Flow in Organisms", "Plants use the energy from light to make sugars from carbon dioxide and water through photosynthesis. This produces food that can be used immediately or stored for later use."),
        ("Crosscutting Concept", "Energy and Matter: Flows, Cycles, and Conservation", "Students trace the flow of matter (carbon from CO2 becomes glucose becomes plant mass) and energy (light energy becomes chemical energy in glucose) through photosynthesis.")
    ],
    "cast_items": [
        "Explain how photosynthesis converts light energy and inorganic molecules into organic glucose",
        "Describe where the mass of a growing plant actually comes from using the photosynthesis equation",
        "Predict how changing one input (light, CO2, or water) affects the entire photosynthesis system"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A scientist grows two identical plants in sealed containers. Plant A receives normal light, CO2, and water. Plant B receives normal light and water but the CO2 has been removed from the air. After 4 weeks, which result would you most likely observe?"),
        ("Constructed Response:", "A student claims that plants get their food from the soil through their roots. Using your photosynthesis model and the famous Jan van Helmont willow tree experiment, explain why this claim is mostly incorrect. Where does the mass of a plant actually come from?")
    ],
    "background_intro": "Photosynthesis is the foundation of almost all life on Earth. This single chemical process captures solar energy, removes CO2 from the atmosphere, produces the oxygen we breathe, and creates the food that feeds nearly every food web. Understanding it deeply reveals the elegant chemistry that powers our planet.",
    "background_sections": [
        ("The Photosynthesis Equation", "6CO2 + 6H2O + light energy yields C6H12O6 + 6O2. Six molecules of carbon dioxide combine with six molecules of water, using light energy, to produce one molecule of glucose and six molecules of oxygen. Every atom on the left appears on the right. Mass is conserved. Energy is transformed from light to chemical energy stored in glucose bonds."),
        ("Where Plant Mass Really Comes From", "In 1648, Jan van Helmont grew a willow tree for 5 years. The tree gained 164 pounds, but the soil lost only 2 ounces. He concluded the mass came from water, but we now know most plant mass comes from CO2 in the air. Carbon atoms from atmospheric CO2 are fixed into glucose, then assembled into cellulose, lignin, and other structural molecules. A tree is literally made of air."),
        ("Three Inputs, One Limiting Factor", "Photosynthesis requires light, CO2, and water simultaneously. The rate is limited by whichever input is in shortest supply. In a bright greenhouse with plenty of water, CO2 concentration is often the limiting factor. In a desert with abundant light and CO2, water is the limiting factor. Commercial greenhouses supplement CO2 to levels 2-3 times atmospheric concentration to overcome this limitation."),
        ("Photosynthesis and Cellular Respiration Are Opposites", "Photosynthesis builds glucose from CO2 and H2O using light energy. Cellular respiration breaks glucose down into CO2 and H2O, releasing the stored energy as ATP. They are essentially the same reaction running in opposite directions. Plants perform BOTH processes: photosynthesis during the day and cellular respiration 24 hours a day.")
    ],
    "lever_L": "Students identify light intensity, CO2 concentration, and water availability as the three external inputs, and glucose production, oxygen released, and plant biomass growth as the internal responses.",
    "lever_E": "Students determine that all three inputs positively drive glucose production, glucose production positively drives both oxygen release and plant biomass growth, and the overall rate is limited by whichever input is lowest.",
    "lever_V": "Students build a model with three independent inputs converging on one central process (photosynthesis), demonstrating that ALL inputs are required and the limiting factor controls the rate.",
    "lever_Ev": "Students run full sun, darkness, and drought scenarios to observe how removing different inputs affects the system differently, and discover the concept of limiting factors.",
    "lever_R": "Students add temperature or stomata openness to explore the tradeoff between CO2 uptake and water loss that plants face in hot, dry environments.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with backlit leaf imagery", "say": "This leaf is a solar-powered factory that builds itself from thin air. Literally. And it has been doing this for 3 billion years.", "do": "Hold up a leaf. Tell students it is a factory that takes invisible gas and turns it into solid wood. Challenge them to figure out how.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are going to discover that trees are made of AIR, and prove it with a model.", "do": "Have students read objectives. Pre-teach 'glucose,' 'carbon fixation,' and 'limiting factor.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Where does 2 million pounds come from?", "say": "A redwood weighs 2 million pounds. It started as a seed smaller than your fingernail. Where did all that mass come from?", "do": "Poll the class: soil, water, air, or sunlight? Most will say soil. They will be surprised.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "Our model has THREE external inputs. This is the most complex model we have built. All three must be present for the system to work.", "do": "Preview the three-input structure. Tease that removing ANY one input crashes everything.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for photosynthesis model", "say": "What does a plant need from outside? What does it produce inside? Notice we have SIX components.", "do": "Guide sorting. Discuss why all three inputs are external (supplied by the environment, not made by the plant).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows from three inputs to glucose to outputs", "say": "Light, CO2, and water all converge on one process. Glucose is the product, and from glucose comes oxygen and growth.", "do": "Write the photosynthesis equation. Match each part to a model component. Count atoms on both sides.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions for full sun vs. darkness vs. drought", "say": "Let's turn off the lights and watch the factory shut down. Then let's create a drought. Which kills the plant faster?", "do": "Students predict before running. Compare darkness (immediate stop) to drought (gradual decline). Discuss limiting factors.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings including the air-to-tree revelation", "say": "A tree is made of air. The carbon in CO2 becomes the carbon in wood. You are breathing tree-building material right now.", "do": "Share van Helmont's willow experiment. Connect CO2 to plant carbon to cellulose to wood. Mind-blowing for students.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Plant growth chamber design", "say": "Design a factory that makes food from air, water, and light. It is called a greenhouse. Make it the best one possible.", "do": "Distribute materials. Groups design growth chambers optimizing all three inputs.", "time": "12 min"}
    ],
    "sort_reasoning": "Light Intensity, CO2 Concentration, and Water Availability are all external because they are supplied by the environment outside the plant and are controlled by the student. Glucose Production, Oxygen Released, and Plant Biomass Growth are internal because they are outputs and processes within the plant that respond to the three external inputs.",
    "relationships": [
        ("Light Intensity to Glucose Production", "POSITIVE (+)", "More light energy powers more photosynthesis reactions, producing more glucose. Without light, the light-dependent reactions cannot split water or generate the energy carriers needed for carbon fixation."),
        ("CO2 Concentration to Glucose Production", "POSITIVE (+)", "More CO2 provides more carbon atoms for fixation into glucose. Carbon from CO2 becomes the carbon backbone of every glucose molecule. Higher CO2 means faster fixation."),
        ("Water Availability to Glucose Production", "POSITIVE (+)", "Water provides hydrogen atoms and electrons for the light reactions. Without water, the plant cannot split H2O molecules, and the entire process stops."),
        ("Glucose Production to Oxygen Released", "POSITIVE (+)", "Oxygen is a byproduct of splitting water molecules during photosynthesis. More photosynthesis means more water split and more O2 released."),
        ("Glucose Production to Plant Biomass Growth", "POSITIVE (+)", "Glucose is used to build cellulose, lignin, proteins, and all other structural molecules. More glucose production means more building material for growth.")
    ],
    "sim_answers": [
        ("Darkness Scenario", "When Light Intensity is locked at 0%, Glucose Production drops to zero immediately because the light-dependent reactions cannot function. Oxygen Released also drops to zero because no water molecules are being split. Plant Biomass Growth stops and eventually becomes negative as the plant uses stored glucose for cellular respiration. The plant is burning its reserves."),
        ("Drought Scenario", "When Water Availability is locked at 10%, Glucose Production drops significantly because water is a direct reactant in photosynthesis AND because plants close their stomata to conserve water, which also blocks CO2 entry. This demonstrates the limiting factor concept: even with abundant light and CO2, the shortage of water constrains the entire process.")
    ],
    "reflection_exemplars": [
        ("Why does most plant mass come from air, not soil?", "The photosynthesis equation shows that glucose (C6H12O6) is made from CO2 and H2O. The carbon and oxygen atoms come from CO2 gas in the air. The hydrogen comes from water. Soil provides only mineral nutrients (nitrogen, phosphorus, potassium, etc.) which make up less than 5% of plant mass. Van Helmont proved this in 1648: his willow gained 164 pounds while the soil barely changed. The mass came from the air and water."),
        ("Why does photosynthesis plateau when one input is maxed?", "Photosynthesis requires all three inputs simultaneously. If light is maxed but CO2 is low, the light reactions produce energy carriers faster than the Calvin cycle can use them (because CO2 is the limiting factor). Increasing light further gives no benefit because the bottleneck is CO2, not light. The rate is always limited by whichever input is in shortest supply, regardless of how abundant the others are.")
    ],
    "stem_intro": "Present the challenge: A vertical farming company wants to grow food indoors in urban buildings. Your team must design a growth chamber that maximizes photosynthesis by optimizing light, CO2, and water delivery to produce the most plant biomass per square meter.",
    "stem_concepts": [
        ("Photosynthetically Active Radiation (PAR)", "The wavelengths of light (400-700 nm) that plants can actually use for photosynthesis. Red and blue light are most effective, which is why grow lights often appear purple."),
        ("CO2 Enrichment", "Commercial greenhouses supplement CO2 to 800-1200 ppm (vs. atmospheric 420 ppm) to increase photosynthesis rates by 20-40%. This is a direct application of the limiting factor concept."),
        ("Hydroponics", "Growing plants in nutrient-rich water solutions without soil. Since soil provides only minerals (not mass), hydroponics proves that plants can grow without soil as long as light, CO2, water, and minerals are provided.")
    ],
    "stem_eval": [
        ("Expert (4)", "Growth chamber optimizes all three inputs with model evidence, includes measurement plan, explains limiting factor management, and connects to real vertical farming technology"),
        ("Proficient (3)", "Design addresses all three inputs with model-based rationale and measurement plan"),
        ("Developing (2)", "Design addresses light but neglects CO2 or water optimization"),
        ("Beginning (1)", "Design is incomplete or does not demonstrate understanding of photosynthesis inputs")
    ],
    "support": [
        "Provide a labeled photosynthesis diagram showing inputs (light, CO2, H2O) entering the chloroplast and outputs (glucose, O2) exiting",
        "Use a simple analogy: photosynthesis is a recipe that needs three ingredients. Missing ANY one means no cake (glucose).",
        "Sentence frames: 'When CO2 concentration decreases, glucose production __ because __'"
    ],
    "extensions": [
        "Research the van Helmont willow experiment and explain what he got right and what he missed about where plant mass comes from",
        "Investigate how rising atmospheric CO2 affects photosynthesis rates and whether this is good or bad for plant growth",
        "Compare C3, C4, and CAM photosynthesis adaptations and explain how plants in different climates have evolved different strategies"
    ],
    "cross_curr": [
        ("Math", "Calculate the mass of CO2 a tree must absorb to produce 100 kg of wood, given that wood is approximately 50% carbon by mass"),
        ("ELA", "Write a myth-busting article titled 'Trees Are Made of Air' that explains photosynthesis to a general audience using evidence and analogies"),
        ("Social Studies", "Research how deforestation affects atmospheric CO2 levels and connect to climate change, using photosynthesis chemistry to explain the mechanism")
    ],
    "misconceptions": [
        ("Plants get their food from the soil", "Plants get only water and minerals from the soil. Their actual food (glucose) is made through photosynthesis from CO2 in the air and water, using light energy. Soil nutrients make up less than 5% of plant mass. Van Helmont proved this in 1648.", "Grow plants in hydroponic solution (no soil at all). They grow normally because soil is not the source of food or mass."),
        ("Plants breathe in CO2 and breathe out O2 (like reverse animals)", "Plants perform BOTH photosynthesis and cellular respiration. During the day, photosynthesis is faster, so they appear to absorb CO2 and release O2. At night (no light), they only do cellular respiration, absorbing O2 and releasing CO2. Plants are not reverse animals; they do both processes.", "Measure O2 levels near plants in light vs. dark. In darkness, O2 drops because plants are only doing respiration."),
        ("Sunlight is the plant's food", "Sunlight is ENERGY, not food. Light provides the energy to drive the chemical reaction that makes food (glucose). It is like saying electricity is your food because it powers your stove. The food is the glucose molecule, and light is the energy that assembles it from CO2 and water.", "Analogy: light is the electricity that powers the factory. CO2 and water are the raw materials. Glucose is the product (food).")
    ]
}

L07 = {
    "id": "G06L2-L07",
    "title": "Engineering a Solution: The Design Process",
    "subtitle": "Modeling How Iteration Turns Failure into Innovation",
    "ngss": "MS-ETS1-1, MS-ETS1-2",
    "ngss_desc": "Define the criteria and constraints of a design problem with sufficient precision to ensure a successful solution, taking into account relevant scientific principles and potential impacts on people and the natural environment. Evaluate competing design solutions using a systematic process to determine how well they meet the criteria and constraints of the problem.",
    "big_question": "Why do the best engineering solutions almost never work on the first try, and how does failure actually make designs better?",
    "objectives": [
        "Model how problem complexity, research depth, design quality, prototype performance, and iteration count interact in the engineering design process",
        "Explain the positive feedback loop between testing prototypes and improving design quality",
        "Predict how increasing research depth improves first-attempt design quality for complex problems",
        "Demonstrate that iteration (test-improve cycles) is the single most powerful variable for improving outcomes",
        "Connect the engineering design process model to real-world innovation stories"
    ],
    "vocabulary": [
        ("Criteria", "The specific requirements that a successful engineering solution must meet, defining what 'success' looks like"),
        ("Constraints", "The limitations on an engineering solution, such as budget, materials, time, safety, and environmental impact"),
        ("Prototype", "A preliminary model or version of a design used for testing and evaluation before final production"),
        ("Iteration", "The process of testing a design, identifying problems, making improvements, and testing again in repeated cycles"),
        ("Trade-off", "A compromise where improving one aspect of a design requires sacrificing another, requiring engineering judgment")
    ],
    "components": [
        ("Problem Complexity", "How difficult the engineering challenge is, determined by the number of criteria, constraints, and competing requirements", True),
        ("Research Depth", "How much background investigation is done before designing, including studying existing solutions and relevant science", True),
        ("Design Quality", "How well the proposed solution addresses the problem criteria and constraints on paper before building", False),
        ("Prototype Performance", "How well the first physical build actually works when tested against the criteria", False),
        ("Iteration Count", "The number of test-improve cycles completed, where each cycle identifies problems and implements solutions", False)
    ],
    "think_about_it": "When problem complexity increases, what happens to first-attempt design quality? After testing a prototype and finding problems, what happens to design quality in the next iteration? Why does more research before designing lead to better first attempts?",
    "scenarios": [
        ("No Research Rush", "Set Problem Complexity high and Research Depth to 0% to observe the failure of jumping straight to building"),
        ("Research First", "Set Problem Complexity high and Research Depth to 90% to see how preparation improves outcomes"),
        ("Iterate to Excellence", "Start with moderate research and observe how each iteration improves prototype performance")
    ],
    "sim_scenarios": [
        ("No Research Rush", "High complexity, no research", "What do you predict will happen to Design Quality when you jump into a hard problem without researching first?"),
        ("Research First", "High complexity, deep research", "How much better do you predict the first prototype will perform with thorough research?"),
        ("Iterate to Excellence", "Moderate research, observe iterations", "What do you predict happens to Prototype Performance with each iteration? Does improvement ever stop?")
    ],
    "discoveries": [
        "Harder problems produce worse first designs, but research can partially offset complexity",
        "Research depth has a strong positive effect on initial design quality because understanding the problem is half the solution",
        "Iteration is the most powerful improvement tool. Each test-improve cycle catches problems the previous one missed",
        "The feedback loop between prototype testing and design quality is POSITIVE: testing informs better designs, which produce better prototypes, which reveal subtler problems",
        "Even expert engineers rarely succeed on the first try. Iteration is not failure; it IS the engineering process"
    ],
    "answer": "Engineering solutions rarely work the first time because real-world problems are complex with many interacting constraints. Every test reveals unexpected problems that no amount of planning could predict. But here is the beautiful part: each failure teaches you something specific that makes the next version better. The feedback loop between testing and redesign is the engine of innovation. Thomas Edison tested thousands of materials for the light bulb filament. SpaceX crashed rockets before landing them. Iteration is not the opposite of success; it is the path TO success.",
    "stem_title": "The Iterative Design Challenge",
    "stem_mission": "Design, test, and iterate on a solution to a real engineering problem, documenting how each iteration improves performance.",
    "stem_scenario": "Your engineering firm has been hired to design a device that protects a raw egg from a 3-meter drop using only limited materials. You have three test rounds. After each test, you must analyze what failed, redesign, and test again. The team with the most improvement across iterations wins.",
    "stem_questions": [
        "How did your prototype performance change from iteration 1 to iteration 3?",
        "What specific information from testing led to your design improvements?",
        "Would more research before your first design have prevented any of the failures you experienced?"
    ],
    "stem_design_qs": [
        "What are the criteria (must protect the egg) and constraints (limited materials, 3-meter drop height)?",
        "What scientific principles (force distribution, energy absorption, deceleration) will guide your design?",
        "How will you document what you learn from each test to inform the next iteration?",
        "What trade-offs are you making in your design (weight vs. protection, simplicity vs. effectiveness)?"
    ],
    "career": "Engineering Design Specialists and Product Developers use iterative prototyping and testing to create everything from medical devices to consumer electronics to spacecraft. They earn $65,000-$130,000/year.",
    "images": {
        "cover": ("cover-engineering.png", "A photorealistic image of engineering iteration showing three versions of a prototype on a workbench, progressing from rough sketch to refined model, engineering tools and notebooks visible, warm workshop lighting"),
        "landscape": ("landscape-engineering.png", "6th grade students in a maker space testing prototypes, a Black student dropping a test device while an Asian student records results with a tablet, bright modern STEM lab with tools and materials"),
        "modeling": ("modeling-engineering.png", "A diverse group of 6th grade students building an engineering design process model on laptops, a White student pointing at the iteration feedback loop while a Latino student compares scenarios, modern classroom"),
        "discussion": ("discussion-engineering.png", "A teacher showing photos of SpaceX rocket iterations from crashes to successful landings, 6th grade students amazed at the progression, diverse engaged classroom with engineering posters"),
        "stem": ("stem-egg-drop.png", "6th grade students testing egg drop devices from a ladder, one Asian student carefully lowering a prototype while a Black student checks the egg below, excited collaborative atmosphere in a gym or outdoor area")
    },
    "pre_assessment": [
        "Have you ever built something that did not work the first time? What did you do next?",
        "Why do you think engineers test their designs before producing the final product?",
        "Is failure a bad thing in engineering? Why or why not?",
        "Draw the steps you think engineers follow when designing a new product."
    ],
    "extend_components": [
        ("Budget Constraint", "Money available for materials and testing. Lower budget limits options and forces creative trade-offs"),
        ("Team Collaboration", "How effectively team members share ideas, divide tasks, and integrate feedback. Better collaboration improves outcomes"),
        ("Time Pressure", "Deadline constraints that limit how many iterations are possible. More time allows more improvement cycles")
    ],
    "reflections": [
        "Why is a tested-and-improved second design usually better than even a carefully planned first design?",
        "How does the feedback loop between testing and redesign create a cycle of improvement?",
        "What would happen if an engineer built their first design and shipped it without testing?",
        "How is the engineering design process similar to how scientists do experiments?",
        "Why does more research before designing lead to a better FIRST prototype?"
    ],
    "dimensions": [
        ("Science Practice", "Designing Solutions", "Students model the engineering design process showing how problem complexity, research, design quality, prototype performance, and iteration interact as a system."),
        ("Disciplinary Core Idea", "ETS1.A Defining and Delimiting Engineering Problems", "The more precisely a problem is defined in terms of criteria and constraints, the more likely it is that the designed solution will be successful. Specifications and constraints help ensure that a solution addresses the intended problem."),
        ("Crosscutting Concept", "Influence of Engineering, Technology, and Science on Society", "Students explore how the iterative design process has produced innovations that improve human life, and how engineering solutions must consider societal impact and environmental constraints.")
    ],
    "cast_items": [
        "Define criteria and constraints for an engineering problem with sufficient precision for a successful solution",
        "Explain how iterative testing and redesign improves engineering solutions",
        "Evaluate competing design solutions using systematic comparison against criteria"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Two engineering teams are given the same problem. Team A spends 80% of their time researching and 20% building one prototype. Team B spends 20% researching and 80% building and testing three prototypes. Based on the engineering design process model, which team is more likely to produce a better solution, and why?"),
        ("Constructed Response:", "Using your engineering design process model, explain why SpaceX's approach of rapidly testing, failing, and iterating on rocket designs led to reusable rockets, while other companies that spent years perfecting designs on paper before testing fell behind. Reference the feedback loop between prototype performance and design quality.")
    ],
    "background_intro": "The engineering design process is not a simple linear path from problem to solution. It is a dynamic, iterative cycle where testing, failure, and redesign are the most important steps. Understanding this process reveals why innovation is messy, why failure is valuable, and why the best solutions come from persistent iteration.",
    "background_sections": [
        ("Define, Research, Design, Test, Iterate", "The engineering design process has five major stages: defining the problem (criteria and constraints), researching existing solutions and relevant science, designing a potential solution, building and testing a prototype, and iterating (using test results to improve the design). The process is cyclical, not linear: each test sends you back to redesign with new knowledge."),
        ("Why First Designs Fail", "Real-world problems involve countless interacting variables. No amount of planning can predict every behavior of a physical system. Wind load, material fatigue, user behavior, manufacturing tolerances, and environmental conditions all create surprises. The ONLY way to discover these problems is to test. Every failure reveals information that was impossible to obtain otherwise."),
        ("The Power of Iteration", "Research on engineering outcomes consistently shows that iterative designs outperform single-attempt designs. SpaceX crashed multiple rockets before achieving controlled landings. The Wright Brothers tested over 200 wing shapes in a wind tunnel. Apple creates dozens of prototypes for each product. The feedback loop (test, learn, redesign, retest) is the engine of engineering innovation."),
        ("Criteria, Constraints, and Trade-offs", "Every engineering problem has criteria (what the solution MUST do) and constraints (limitations like budget, materials, time, safety, and environmental impact). Solutions must satisfy criteria while respecting constraints, which often requires trade-offs. Making a bridge stronger might require more material (cost) or more weight. Engineering judgment is about making the best trade-offs.")
    ],
    "lever_L": "Students identify problem complexity and research depth as the two external inputs, and design quality, prototype performance, and iteration count as the internal responses of the engineering design system.",
    "lever_E": "Students determine that problem complexity negatively affects initial design quality, research depth positively affects design quality, design quality positively affects prototype performance, and iteration count positively improves prototype performance through a feedback loop.",
    "lever_V": "Students build a model showing how research reduces the negative impact of complexity, and how the iteration feedback loop (test, learn, redesign) progressively improves performance.",
    "lever_Ev": "Students run no-research-rush vs. research-first scenarios, then observe how adding iterations dramatically improves outcomes even with lower initial quality.",
    "lever_R": "Students add budget constraint or time pressure to explore how real-world limitations affect the engineering process and force trade-offs.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with iteration imagery from rough to refined", "say": "SpaceX crashed SIX rockets before they landed one. Was that failure? Or was that the process working exactly as designed?", "do": "Show a rapid montage of SpaceX rocket crashes followed by the first successful landing. Let students react.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are going to model the engineering design process itself and discover why failure is the most important step.", "do": "Have students read objectives. Pre-teach 'criteria,' 'constraints,' and 'iteration.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why don't great designs work the first time?", "say": "Every product you own went through dozens of failures before it worked. Why can't smart engineers get it right the first time?", "do": "Think-pair-share: Have you ever built something that did not work the first time? What did you do?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "Our model has a FEEDBACK LOOP. Testing tells you what is wrong, which makes the next design better, which reveals new problems to fix.", "do": "Draw the feedback loop on the board. This is different from the one-way models we have built before.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for engineering model", "say": "What can we control? What responds? And where is the feedback loop hidden?", "do": "Guide sorting. Discuss why problem complexity is external (given) and research depth is external (chosen by the engineer).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows with feedback loop highlighted", "say": "Here is the most important arrow in the entire model: prototype testing feeds BACK to design quality. This loop is what makes engineering work.", "do": "Trace the feedback loop: design -> prototype -> test results -> better design -> better prototype. Each cycle improves.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions for no-research vs. research-first vs. iterative", "say": "Let's race: a team that does no research vs. a team that researches first vs. a team that iterates three times. Who wins?", "do": "Students predict outcomes. Run all three scenarios. The iterative team wins even with less initial research.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings about iteration power", "say": "Iteration beats everything. You can overcome a bad start by testing and improving. But you cannot overcome skipping the testing loop.", "do": "Connect to real examples: Wright Brothers, SpaceX, Apple, medical devices. Every great innovation went through painful iteration.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Egg drop iterative challenge", "say": "Three drops. Three chances. After each drop, you analyze, redesign, and try again. The team that improves the MOST wins.", "do": "Set up the egg drop challenge with clear criteria and material constraints. Emphasize documentation of changes between iterations.", "time": "12 min"}
    ],
    "sort_reasoning": "Problem Complexity is external because it is a given characteristic of the challenge that the engineer cannot change. Research Depth is external because it is a conscious choice the engineer makes before designing. Design Quality, Prototype Performance, and Iteration Count are internal because they are properties of the design process that respond to the external inputs and to each other through the feedback loop.",
    "relationships": [
        ("Problem Complexity to Design Quality", "NEGATIVE (-)", "More complex problems have more interacting constraints, making it harder to produce a good first design. Complexity increases the chance of unexpected problems."),
        ("Research Depth to Design Quality", "POSITIVE (+)", "More research means better understanding of the problem, existing solutions, and relevant science. This leads to better-informed designs that address more criteria from the start."),
        ("Design Quality to Prototype Performance", "POSITIVE (+)", "A better design on paper translates to a better-performing prototype. Good planning reduces (but never eliminates) unexpected failures during testing."),
        ("Iteration Count to Prototype Performance", "POSITIVE (+)", "Each test-improve cycle catches problems and implements solutions. More iterations mean more opportunities to identify and fix issues, progressively improving performance."),
        ("Prototype Performance to Design Quality", "POSITIVE (+) FEEDBACK LOOP", "Testing reveals problems that were invisible on paper. This information directly improves the next design iteration. The loop creates progressive improvement with each cycle.")
    ],
    "sim_answers": [
        ("No Research Rush Scenario", "With high Problem Complexity and zero Research Depth, Design Quality starts extremely low. The first Prototype Performance is poor because the design missed key constraints. Even with iteration, improvement is slow because the team lacks fundamental understanding. The model shows that skipping research wastes iterations on problems that research could have prevented."),
        ("Research First vs. Iterate to Excellence", "The research-first team starts with higher initial Design Quality and better first-prototype performance. But the iterating team, even starting with moderate research, eventually catches up and surpasses because each test-improve cycle provides information that research alone cannot. The optimal strategy is both: research first, THEN iterate. Research gives a better starting point, and iteration refines from there.")
    ],
    "reflection_exemplars": [
        ("Why is a tested second design better than a planned first design?", "Planning is limited by what you can predict. Testing reveals what actually happens, which always includes surprises. Real materials behave differently than expectations. Users interact with designs in unexpected ways. Environmental conditions create unforeseen stresses. The only way to discover these realities is to test. The second design incorporates REAL DATA from testing, not just predictions. That is why it is almost always better."),
        ("How is the engineering feedback loop like the scientific method?", "Both are iterative cycles where testing provides information that improves the next attempt. Scientists form hypotheses, test them with experiments, analyze results, and refine hypotheses. Engineers design solutions, test prototypes, analyze performance, and refine designs. In both cases, the testing step provides information that was impossible to obtain any other way, and each cycle brings you closer to truth (science) or to an effective solution (engineering).")
    ],
    "stem_intro": "Present the challenge: Design a device that protects a raw egg during a 3-meter drop using limited materials. You have THREE test opportunities. After each test, analyze what failed, redesign, and test again. Document your changes. The team with the greatest improvement across iterations (not just the best final result) wins.",
    "stem_concepts": [
        ("Force Distribution", "Spreading the impact force over a larger area or longer time reduces the peak force on the egg. Crumple zones in cars use this principle."),
        ("Energy Absorption", "Materials that deform on impact (foam, crumpled paper, bubble wrap) absorb kinetic energy before it reaches the egg, converting it to heat and deformation."),
        ("Deceleration Distance", "The longer the stopping distance, the lower the deceleration force. This is why airbags inflate (increasing stopping distance) and why landing on a thick cushion is safer than landing on concrete.")
    ],
    "stem_eval": [
        ("Expert (4)", "Three clear iterations with documented analysis between each, measurable improvement from test 1 to test 3, scientific reasoning for each design change, and connection to model evidence"),
        ("Proficient (3)", "Three iterations with documented changes and clear improvement from first to final design"),
        ("Developing (2)", "Multiple attempts but limited documentation of what was learned between iterations"),
        ("Beginning (1)", "Single design attempt without meaningful iteration or analysis of failures")
    ],
    "support": [
        "Provide a structured iteration log template: 'What happened? What failed? Why? What will you change?'",
        "Demonstrate the first iteration yourself, deliberately making mistakes and modeling how to learn from them",
        "Sentence frames: 'When problem complexity increases, design quality __ because __'"
    ],
    "extensions": [
        "Research the design history of a product you use daily (smartphone, bicycle, running shoe) and document how many iterations it went through",
        "Interview a local engineer or maker about their iterative process and how they handle failure in their work",
        "Design a comparison experiment: give one group unlimited research time but one prototype attempt vs. another group minimal research but three prototype attempts. Compare outcomes."
    ],
    "cross_curr": [
        ("Math", "Graph prototype performance vs. iteration count and identify whether improvement follows a linear, logarithmic, or diminishing returns pattern"),
        ("ELA", "Write a failure resume for a famous engineer or inventor, documenting all the failed attempts that led to their eventual success"),
        ("Social Studies", "Research how engineering solutions must balance technical performance with social, environmental, and ethical constraints. Use a real example like dam construction or urban highway design.")
    ],
    "misconceptions": [
        ("Good engineers get it right the first time", "The best engineers expect failure on the first attempt. They design EXPERIMENTS, not final products, in early iterations. NASA, SpaceX, Apple, and every major engineering organization budgets for multiple prototypes. Getting it right the first time is not a sign of good engineering; it usually means the problem was too simple.", "Show the number of prototypes for products students know: iPhone (dozens), SpaceX Starship (6+ full-scale test flights), Wright Flyer (hundreds of wing shapes tested)."),
        ("Failure means the design is bad", "In engineering, failure is DATA. Every failure tells you specifically what does not work and why. A prototype that survives a test without revealing any problems is actually LESS useful than one that fails, because the failure provides actionable information for improvement. The only real failure is not learning from the test.", "Reframe classroom language: 'What did you learn from this test?' instead of 'Did it work?'"),
        ("More research always beats more testing", "Research provides theoretical understanding, but testing provides real-world data that research cannot. The ideal approach combines both: research to build a strong foundation, then iterate to refine. Research alone misses problems that only emerge in physical testing. Testing alone wastes time on problems research could have prevented.", "Compare two strategies in the model: maximum research with one test vs. moderate research with three tests. The combination wins.")
    ]
}

L08 = {
    "id": "G06L2-L08",
    "title": "Why Does It Feel Colder When It's Windy?",
    "subtitle": "Modeling Wind Chill and Convective Heat Loss",
    "ngss": "MS-PS1-4, MS-PS3-4",
    "ngss_desc": "Develop a model that predicts and describes changes in particle motion, temperature, and state of a pure substance when thermal energy is added or removed. Plan an investigation to determine the relationships among the energy transferred, the type of matter, the mass, and the change in the average kinetic energy of the particles as measured by the temperature of the sample.",
    "big_question": "If the air temperature is the same on a calm day and a windy day, why does the windy day feel so much colder?",
    "objectives": [
        "Explain how wind increases the rate of convective heat loss from the skin",
        "Model the relationship between wind speed, air temperature, and perceived cold",
        "Distinguish between actual air temperature and the wind chill effect on the human body",
        "Predict how changes in wind speed affect skin temperature at different air temperatures",
        "Analyze why wind chill is a measure of heat loss rate rather than actual temperature"
    ],
    "vocabulary": [
        ("Convection", "The transfer of thermal energy through the movement of a fluid (liquid or gas), carrying heat away from or toward a surface"),
        ("Wind Chill", "A measure of how cold it feels to the human body when wind speed is factored in with actual air temperature"),
        ("Thermal Boundary Layer", "A thin layer of warm air that forms against the skin and acts as insulation, which wind disrupts"),
        ("Convective Heat Loss", "The process by which moving air carries thermal energy away from a warm surface, cooling it faster than still air"),
        ("Perceived Temperature", "The temperature the body feels based on the combined effects of actual air temperature and wind speed on heat loss rate")
    ],
    "components": [
        ("Wind Speed", "The velocity of moving air in the environment, which strips away the insulating boundary layer near the skin", True),
        ("Air Temperature", "The actual measured temperature of the surrounding air, independent of wind conditions", True),
        ("Convective Heat Loss", "The rate at which thermal energy is carried away from the skin by moving air currents", False),
        ("Skin Temperature", "The surface temperature of the skin, which drops as heat is lost to the environment faster than the body replaces it", False),
        ("Perceived Cold", "How cold the body feels based on the combined effect of air temperature and wind-driven heat loss", False)
    ],
    "think_about_it": "When wind speed increases, what happens to convective heat loss? If air temperature drops but wind speed is zero, how does perceived cold compare to a warmer day with high wind?",
    "scenarios": [
        ("Calm Cold Day", "Set Wind Speed to 0 and Air Temperature to low, then observe skin temperature and perceived cold"),
        ("Windy Cold Day", "Set Wind Speed to high with the same low Air Temperature and compare the results"),
        ("Wind Chill Danger", "Lock Air Temperature at moderate cold and gradually increase Wind Speed to observe when perceived cold becomes dangerous")
    ],
    "sim_scenarios": [
        ("Calm Cold Day", "Wind Speed at 0, Air Temperature at 30°F", "What do you predict will happen to Perceived Cold when there is no wind but the air is cold?"),
        ("Windy Cold Day", "Wind Speed at 30 mph, Air Temperature at 30°F", "What do you predict will happen to Skin Temperature when you add strong wind to the same cold air?"),
        ("Wind Chill Danger", "Lock Air Temperature at 40°F, increase Wind Speed from 0 to 60 mph", "What do you predict will happen to Perceived Cold as wind speed keeps increasing at the same temperature?")
    ],
    "discoveries": [
        "Wind does not change the actual air temperature but dramatically increases the rate of heat loss from the skin",
        "The thermal boundary layer acts as a thin blanket of warm air against the skin that wind strips away",
        "Wind chill is not a real temperature but a measure of how fast the body loses heat",
        "At higher wind speeds, the additional cooling effect diminishes because the boundary layer is already fully disrupted",
        "Wet skin loses heat even faster in wind because evaporation adds another cooling mechanism on top of convection"
    ],
    "answer": "It feels colder when it is windy because wind strips away the thin layer of warm air that your body naturally creates around your skin. This thermal boundary layer acts like insulation. Without wind, that warm air stays close and slows heat loss. But when wind blows, it constantly replaces that warm air with cold air, so your skin loses heat much faster. The air temperature has not changed, but the rate at which your body loses heat has increased dramatically.",
    "stem_title": "Design a Wind Chill Shield",
    "stem_mission": "Design a wearable face shield that minimizes convective heat loss while still allowing the wearer to breathe and see clearly.",
    "stem_scenario": "A winter sports equipment company needs a new face protection system for skiers and snowboarders who experience extreme wind chill at high speeds. Your engineering team must design a prototype that reduces wind chill effects on exposed skin by at least 50% without fogging up or restricting breathing.",
    "stem_questions": [
        "How does your shield design maintain the thermal boundary layer against the skin?",
        "What materials best block wind while allowing moisture from breathing to escape?",
        "How will you test whether your shield actually reduces the rate of heat loss?"
    ],
    "stem_design_qs": [
        "What shape will best deflect wind while allowing comfortable breathing?",
        "What materials will provide wind blocking without trapping moisture?",
        "How will you measure the temperature difference between shielded and unshielded skin?",
        "How will you test your prototype at different simulated wind speeds?"
    ],
    "career": "Meteorologists and Atmospheric Scientists study weather patterns including wind chill to issue safety warnings that protect millions of people. They earn $55,000-$105,000/year.",
    "images": {
        "cover": ("cover-wind-chill.png", "A photorealistic image of wind blowing across a snowy landscape with visible wind streaks and frost crystals, dramatic winter lighting with blue and white tones"),
        "landscape": ("landscape-wind-chill.png", "A diverse group of 6th grade students in a science lab using a small fan and thermometers to test heat loss, a Latino student holding a thermometer near the fan while a Black student records data, bright modern lab"),
        "modeling": ("modeling-wind-chill.png", "6th grade students building a wind chill model on laptops, an Asian student pointing at the component relationships while a White student adjusts wind speed values, modern classroom with weather posters"),
        "discussion": ("discussion-wind-chill.png", "A teacher explaining thermal boundary layers to 6th grade students using a diagram on a smartboard, Black and Latino students with hands raised, engaged discussion about why wind makes it feel colder"),
        "stem": ("stem-wind-shield.png", "6th grade students testing face shield prototypes with a desk fan and temperature sensors, a White student wearing a prototype while an Asian student reads the thermometer, collaborative STEM lab")
    },
    "pre_assessment": [
        "Have you ever noticed that a windy day feels much colder than a calm day at the same temperature? Why do you think that happens?",
        "When you blow on hot soup, why does it cool down faster?",
        "Does wind actually change the temperature of the air? Why or why not?",
        "Draw what you think happens to the air around your skin on a windy day versus a calm day."
    ],
    "extend_components": [
        ("Humidity Level", "The amount of moisture in the air. Higher humidity can increase heat loss through evaporative cooling, especially on windy days"),
        ("Clothing Insulation", "How effectively clothing traps warm air near the body and blocks wind from stripping the thermal boundary layer"),
        ("Physical Activity", "The rate at which the body generates internal heat through metabolism and muscle movement, counteracting heat loss")
    ],
    "reflections": [
        "Why does the wind chill index warn about frostbite danger even when the actual temperature is above freezing?",
        "How is the thermal boundary layer similar to wearing a thin invisible jacket?",
        "Why does wind chill have a diminishing effect at very high wind speeds?",
        "How could understanding convective heat loss help you dress more effectively for winter?",
        "Why is wind chill only relevant to warm-blooded organisms and not to objects like cars or rocks?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how wind speed and air temperature interact to drive convective heat loss, skin temperature changes, and perceived cold."),
        ("Disciplinary Core Idea", "PS3.A Definitions of Energy / PS3.B Conservation of Energy and Energy Transfer", "Energy is transferred from warmer to cooler objects or regions by conduction, convection, and radiation. Wind increases convective transfer rate, removing thermal energy from the skin faster."),
        ("Crosscutting Concept", "Cause and Effect", "Students investigate the causal mechanisms by which wind speed increases heat loss rate, identifying that the disruption of the thermal boundary layer is the key mechanism linking wind to perceived cold.")
    ],
    "cast_items": [
        "Explain how thermal energy is transferred from the body to the environment through convection",
        "Model the relationship between wind speed and rate of heat loss from a warm surface",
        "Predict wind chill effects given specific air temperature and wind speed conditions"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Two students stand outside on a 35°F day. Student A is in a sheltered area with no wind. Student B is on a hilltop with 25 mph wind. Based on the wind chill model, which student will experience a lower skin temperature, and what is the primary mechanism causing the difference?"),
        ("Constructed Response:", "Using your wind chill model, explain why a marathon runner who finishes a race on a cold, windy day is at risk of hypothermia even though they were warm during the race. Reference convective heat loss, the thermal boundary layer, and how physical activity and wind speed interact in the system.")
    ],
    "background_intro": "Wind chill is one of the most commonly experienced but least understood weather phenomena. Understanding the physics behind why wind makes cold feel colder reveals fundamental principles of thermal energy transfer and how the human body interacts with its environment.",
    "background_sections": [
        ("The Thermal Boundary Layer", "The human body constantly radiates heat, warming a thin layer of air directly against the skin. This thermal boundary layer acts as natural insulation, typically only a few millimeters thick. In still air, this layer remains intact and slows further heat loss. When wind blows, it strips this warm air away and replaces it with cold air, forcing the body to warm a new layer that is immediately stripped away again."),
        ("Convection: The Mechanism of Wind Chill", "Convection is the transfer of thermal energy by the physical movement of a fluid. In wind chill, the fluid is air. Faster-moving air increases the rate of convective heat transfer because it replaces the warmed boundary layer more rapidly. This is the same principle that makes a convection oven cook faster than a conventional oven and why blowing on hot food cools it down."),
        ("Wind Chill Is Not Real Temperature", "Wind chill is a calculated index that represents how fast exposed skin loses heat, not an actual air temperature. A wind chill of 0°F on a 20°F day with 25 mph wind means your skin loses heat at the same rate it would on a calm 0°F day. Objects that do not generate their own heat (like a car or a rock) will never cool below the actual air temperature regardless of wind."),
        ("Diminishing Returns at High Speed", "The relationship between wind speed and wind chill is not linear. The first 10 mph of wind has a much greater cooling effect than going from 40 to 50 mph. This is because the thermal boundary layer is mostly disrupted at moderate wind speeds, so additional wind speed has less remaining insulation to remove.")
    ],
    "lever_L": "Students identify wind speed and air temperature as the two external components, and convective heat loss, skin temperature, and perceived cold as the three internal responses of the wind chill system.",
    "lever_E": "Students determine that wind speed positively increases convective heat loss, air temperature negatively affects convective heat loss (colder air means more loss), convective heat loss negatively affects skin temperature, and lower skin temperature positively increases perceived cold.",
    "lever_V": "Students build a model showing how wind disrupts the thermal boundary layer to increase heat loss, connecting wind speed and air temperature to the chain of convective heat loss, skin temperature drop, and perceived cold.",
    "lever_Ev": "Students run calm vs. windy scenarios at the same temperature, then compare moderate wind at different temperatures to discover that wind amplifies cold but does not create it.",
    "lever_R": "Students add humidity level or clothing insulation to explore how additional factors modify the wind chill effect and protection strategies.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic wind and winter imagery", "say": "It is 35 degrees outside. On Monday with no wind, you are comfortable in a jacket. On Tuesday with 30 mph wind, you are shivering and your face hurts. Same temperature. What changed?", "do": "Show weather reports from two days with same temperature but different wind. Let students compare.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are modeling why wind makes cold feel colder, and it is NOT because wind is cold. The answer is about how fast your body loses heat.", "do": "Have students read objectives. Pre-teach 'convection' and 'thermal boundary layer.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why does it feel colder when it is windy?", "say": "A thermometer reads the same temperature whether wind is blowing or not. So if the air is the same temperature, why does your body disagree?", "do": "Think-pair-share: When have you experienced wind chill? What did it feel like compared to a calm day?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We are going to model the invisible layer of warm air your body creates around itself and what wind does to that layer.", "do": "Draw a person with a thin warm air layer. Show arrows of wind stripping it away.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for wind chill model", "say": "Which components are external inputs we cannot control, and which respond inside the system?", "do": "Guide sorting. Wind speed and air temperature are external. Convective heat loss, skin temperature, and perceived cold are internal responses.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between wind chill components", "say": "Wind speed does not change the air temperature. It changes how fast your body loses heat. That is the key connection.", "do": "Trace the chain: wind speed increases convective heat loss, which decreases skin temperature, which increases perceived cold.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions for calm vs. windy at same temperature", "say": "Let's test it. Same air temperature, different wind speeds. Watch what happens to skin temperature.", "do": "Students predict then run calm, moderate wind, and high wind scenarios. Compare perceived cold values.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings about wind chill and convective heat loss", "say": "Wind does not make the air colder. It makes YOU colder by stripping away your body's natural warm air insulation.", "do": "Connect to real life: blowing on soup, car windshield defrost, why mittens work better than gloves.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Wind chill shield design challenge", "say": "Design a face shield that keeps the thermal boundary layer intact against wind while still letting you breathe and see.", "do": "Provide materials (fabric swatches, foam, plastic sheets). Test with a fan and thermometer. Measure temperature behind the shield.", "time": "12 min"}
    ],
    "sort_reasoning": "Wind Speed is external because it is an environmental condition that the system cannot control. Air Temperature is external because it is determined by weather conditions outside the system. Convective Heat Loss is internal because it is a process rate driven by both external inputs. Skin Temperature is internal because it responds to the balance between body heat production and convective heat loss. Perceived Cold is internal because it is the body's response to the combined effects of the external conditions acting through the heat loss mechanism.",
    "relationships": [
        ("Wind Speed to Convective Heat Loss", "POSITIVE (+)", "Higher wind speed strips the thermal boundary layer faster, replacing warm air with cold air more rapidly and increasing the rate of heat transfer away from the skin."),
        ("Air Temperature to Convective Heat Loss", "NEGATIVE (-)", "Lower air temperature increases the temperature difference between skin and air, driving faster heat transfer. Warmer air reduces the gradient and slows heat loss."),
        ("Convective Heat Loss to Skin Temperature", "NEGATIVE (-)", "Greater convective heat loss removes thermal energy from the skin faster than the body can replace it, causing skin temperature to drop."),
        ("Skin Temperature to Perceived Cold", "NEGATIVE (-)", "Lower skin temperature triggers more cold receptors in the skin, increasing the sensation of cold that the brain perceives."),
        ("Wind Speed to Skin Temperature (indirect)", "NEGATIVE (-)", "This indirect path shows how wind speed ultimately drives down skin temperature through the convective heat loss mechanism, even though wind does not change air temperature.")
    ],
    "sim_answers": [
        ("Calm Cold Day vs. Windy Cold Day", "At the same air temperature, the calm day shows moderate convective heat loss because the thermal boundary layer remains mostly intact. Skin temperature drops slowly. On the windy day, convective heat loss spikes because wind constantly strips the boundary layer. Skin temperature drops much faster and reaches a lower value. Perceived cold is significantly higher on the windy day even though the thermometer reads the same."),
        ("Wind Chill Danger Scenario", "As wind speed increases from 0 to 60 mph at a constant 40°F, perceived cold increases rapidly at first (0-20 mph) then more gradually (40-60 mph). This diminishing return pattern shows that the thermal boundary layer is mostly disrupted at moderate wind speeds. The model demonstrates why wind chill warnings focus on the combination of cold AND wind rather than either alone.")
    ],
    "reflection_exemplars": [
        ("Why is wind chill only relevant to warm-blooded organisms?", "Wind chill measures the rate of heat loss from a warm surface to cold moving air. Warm-blooded organisms generate their own internal heat and maintain a temperature above their environment, creating the thermal boundary layer that wind disrupts. A rock or car at ambient temperature has no boundary layer to strip because it is already the same temperature as the air. Wind cannot cool an object below the actual air temperature, only speed up the cooling to that temperature."),
        ("How is the thermal boundary layer like wearing an invisible jacket?", "The thermal boundary layer is a thin layer of air warmed by body heat that stays against the skin in calm conditions. Like a jacket, it creates insulation between the warm body and the cold environment. Wind strips this layer away, just like removing a jacket exposes you to the cold. The difference is that the boundary layer constantly reforms (the body keeps warming the air) but wind keeps stripping it. It is like having your jacket repeatedly pulled off and put back on.")
    ],
    "stem_intro": "Present the challenge: Design a wearable face shield for extreme wind chill conditions that reduces heat loss by at least 50% while maintaining visibility and breathability. Test your prototype using a fan, warm water bottle (simulating a face), and thermometer to measure temperature behind your shield versus unshielded.",
    "stem_concepts": [
        ("Convective Heat Transfer", "Moving air carries heat away from warm surfaces. Faster air movement means faster heat loss. Your shield must slow or redirect airflow near the face."),
        ("Thermal Insulation", "Materials that trap still air (fleece, foam, layered fabric) reduce convective heat loss by maintaining the boundary layer even in wind."),
        ("Breathability vs. Wind Blocking", "A perfect wind block also blocks breathing air. The design challenge is allowing air exchange for breathing while minimizing convective heat loss from exposed skin.")
    ],
    "stem_eval": [
        ("Expert (4)", "Shield reduces measured heat loss by 50%+ with clear data, allows comfortable breathing and visibility, design choices connected to convection principles with model evidence"),
        ("Proficient (3)", "Shield measurably reduces heat loss with data, reasonably comfortable, and design choices explained with thermal concepts"),
        ("Developing (2)", "Shield provides some wind protection but limited data collection or unclear connection to convection principles"),
        ("Beginning (1)", "Minimal design effort with no measurable data or connection to thermal energy transfer concepts")
    ],
    "support": [
        "Provide a diagram of the thermal boundary layer for students to reference during model building",
        "Use a hair dryer on low and a thermometer to physically demonstrate how wind cools a warm surface",
        "Sentence frames: 'When wind speed increases, convective heat loss __ because __'"
    ],
    "extensions": [
        "Research how Arctic animals (polar bears, penguins, musk oxen) have evolved physical adaptations to minimize wind chill effects",
        "Calculate the wind chill index for different temperature and wind speed combinations using the NWS formula and graph the results",
        "Investigate why humidity makes cold feel even colder and add a moisture component to your model"
    ],
    "cross_curr": [
        ("Math", "Use the NWS wind chill formula to calculate perceived temperatures at various wind speeds and graph the nonlinear relationship"),
        ("ELA", "Write a survival guide explaining wind chill to hikers, using scientific vocabulary while keeping it accessible to a general audience"),
        ("Social Studies", "Research how indigenous Arctic peoples designed clothing and shelter systems that minimize convective heat loss and compare to modern winter gear")
    ],
    "misconceptions": [
        ("Wind makes the air colder", "Wind does not change air temperature. A thermometer reads the same whether wind is blowing or not. Wind increases the rate at which warm objects lose heat to the air by disrupting the insulating boundary layer. The air is the same temperature; your body just loses heat to it faster.", "Place a thermometer in front of a fan and show that the reading does not change. Then hold a warm water bottle and show the temperature drops faster with the fan on."),
        ("Wind chill temperature is a real temperature", "Wind chill is an index that describes heat loss rate, not an actual temperature. It tells you how fast exposed skin would lose heat compared to a calm day. A wind chill of -10°F does not mean anything outside will cool to -10°F. Only objects that generate their own heat (humans, animals) are affected by wind chill.", "Compare a person and a metal pole outside on a windy cold day. The person feels much colder with wind; the pole reaches air temperature and stops regardless of wind."),
        ("More wind always means proportionally more cold", "The relationship between wind speed and cooling is nonlinear with diminishing returns. The first 10 mph of wind has a much greater effect than going from 40 to 50 mph because the boundary layer is already mostly disrupted at moderate speeds. The model shows this curve clearly.", "Run the simulation and graph perceived cold vs. wind speed. Students see the curve flatten at high speeds, demonstrating diminishing returns.")
    ]
}

L09 = {
    "id": "G06L2-L09",
    "title": "Why Can't Two Plants Share the Same Sunlight?",
    "subtitle": "Modeling Competition for Limited Resources in Ecosystems",
    "ngss": "MS-LS2-1, MS-LS2-2",
    "ngss_desc": "Analyze and interpret data to provide evidence for the effects of resource availability on organisms and populations of organisms in an ecosystem. Construct an explanation that predicts patterns of interactions among organisms across multiple ecosystems.",
    "big_question": "If there is plenty of sunlight hitting a forest, why can't all plants grow equally tall and healthy?",
    "objectives": [
        "Model how two plants compete for limited sunlight and soil nutrients",
        "Explain how resource availability determines which organisms thrive and which decline",
        "Predict the outcome of competition when one plant species has an advantage in resource capture",
        "Analyze how resource depletion creates feedback loops that intensify competition over time",
        "Connect interspecific competition to patterns of biodiversity and species distribution"
    ],
    "vocabulary": [
        ("Interspecific Competition", "Competition between two different species for the same limited resource such as light, water, or nutrients"),
        ("Resource Partitioning", "When competing species evolve to use slightly different resources or the same resource at different times to reduce competition"),
        ("Competitive Exclusion", "The principle that two species competing for the exact same resource cannot coexist indefinitely; one will outcompete the other"),
        ("Limiting Factor", "A resource that is in shortest supply relative to demand, which restricts the growth of a population"),
        ("Carrying Capacity", "The maximum population size an environment can sustain indefinitely given the available resources")
    ],
    "components": [
        ("Sunlight Available", "The total amount of light energy reaching the ecosystem, which both plants need for photosynthesis", True),
        ("Soil Nutrients", "The minerals and nitrogen in the soil that both plants require for growth but exist in limited quantities", True),
        ("Plant A Growth", "The rate at which Plant A increases in biomass by capturing sunlight and absorbing soil nutrients", False),
        ("Plant B Growth", "The rate at which Plant B increases in biomass by capturing sunlight and absorbing soil nutrients", False),
        ("Resource Depletion", "The rate at which available sunlight and soil nutrients are consumed as both plants grow and compete", False)
    ],
    "think_about_it": "When Plant A grows taller and captures more sunlight, what happens to the sunlight available for Plant B? If soil nutrients are depleted faster, how does that affect both plants differently?",
    "scenarios": [
        ("Equal Start", "Set both plants to equal starting size with moderate sunlight and nutrients, then observe who wins over time"),
        ("One Plant Advantage", "Give Plant A a height advantage and observe how initial advantage compounds through resource competition"),
        ("Nutrient Crash", "Lock Soil Nutrients to low levels and observe how scarcity intensifies competition between the plants")
    ],
    "sim_scenarios": [
        ("Equal Start", "Both plants at equal size, moderate resources", "What do you predict will happen to Plant A Growth and Plant B Growth when they start with equal access to resources?"),
        ("One Plant Advantage", "Plant A starts taller, same soil nutrients", "What do you predict will happen to Plant B Growth when Plant A can reach more sunlight from the start?"),
        ("Nutrient Crash", "Lock Soil Nutrients to low", "What do you predict will happen to Resource Depletion when nutrients are scarce and both plants are trying to grow?")
    ],
    "discoveries": [
        "Even small initial advantages in resource capture can compound over time, leading to one species dominating",
        "Competition for light is often asymmetric because taller plants shade shorter ones but not vice versa",
        "Resource depletion creates a feedback loop where growth reduces available resources, which limits further growth",
        "Two species can coexist if they partition resources (different root depths, different light needs, different growing seasons)",
        "The competitive exclusion principle means identical niches cannot support two species long-term"
    ],
    "answer": "Two plants cannot truly share the same sunlight because light is a directional resource. The taller plant intercepts sunlight first, casting shade on the shorter plant below. As Plant A grows taller, it captures more light and more nutrients, which fuels more growth, which captures even more resources. This positive feedback loop means that even a tiny initial advantage compounds over time. The shorter plant gets less and less of both sunlight and nutrients until it cannot sustain itself. This is competitive exclusion in action.",
    "stem_title": "Design a Coexistence Garden",
    "stem_mission": "Design a small garden where two competing plant species can coexist by using resource partitioning strategies.",
    "stem_scenario": "A community garden has limited space and wants to maximize biodiversity by growing two plant species in the same bed. Your ecology team must design a planting arrangement that allows both species to thrive by minimizing direct competition for sunlight and nutrients.",
    "stem_questions": [
        "How can you arrange plants so they do not directly compete for the same sunlight?",
        "What characteristics of each plant species would allow them to partition soil nutrients?",
        "How will you measure whether both species are truly coexisting versus one slowly outcompeting the other?"
    ],
    "stem_design_qs": [
        "What two plant species will you choose and what are their light and nutrient requirements?",
        "How will planting arrangement (spacing, height tiers, orientation) reduce light competition?",
        "What soil amendments or root zone strategies will help both plants access nutrients?",
        "How will you monitor the health and growth of both species over several weeks?"
    ],
    "career": "Ecologists and Conservation Biologists study species interactions including competition to protect biodiversity and manage ecosystems. They earn $55,000-$110,000/year.",
    "images": {
        "cover": ("cover-plant-competition.png", "A photorealistic image of two plant species growing close together in a forest, one tall and receiving full sunlight while the other is shaded below, dappled forest light with green tones"),
        "landscape": ("landscape-plant-competition.png", "A diverse group of 6th grade students examining two potted plants growing at different heights under a grow light, a Black student measuring plant height while a White student records data, bright science lab"),
        "modeling": ("modeling-plant-competition.png", "6th grade students building a plant competition model on laptops, a Latino student adjusting resource values while an Asian student compares growth curves on screen, modern classroom with ecology posters"),
        "discussion": ("discussion-plant-competition.png", "A teacher showing photos of forest canopy layers to 6th grade students on a smartboard, explaining how tall trees shade understory plants, diverse students with hands raised in discussion"),
        "stem": ("stem-coexistence-garden.png", "6th grade students designing a companion planting arrangement at lab tables with plant pots and soil, a White student sketching the layout while a Black student organizes seed packets, collaborative STEM lab")
    },
    "pre_assessment": [
        "If you plant two different types of plants very close together, what do you think will happen over time?",
        "Why do you think some plants grow tall while others stay close to the ground?",
        "What resources do plants need to survive and where do those resources come from?",
        "Draw what you think happens to sunlight as it passes through a forest with tall and short plants."
    ],
    "extend_components": [
        ("Water Availability", "The amount of water in the soil, which both plants need and which can become a limiting factor in dry conditions"),
        ("Root Depth Difference", "How deeply each plant's roots extend into the soil. Different root depths can allow plants to access different nutrient zones"),
        ("Allelopathy", "Chemical compounds released by some plants that inhibit the growth of nearby competitors, a form of chemical competition")
    ],
    "reflections": [
        "Why does even a small head start in height give one plant a compounding advantage over the other?",
        "How is competition between plants different from competition between animals?",
        "What would happen in your model if both plants were identical in every way?",
        "How does resource partitioning allow species that would otherwise compete to coexist?",
        "Why does competitive exclusion not eliminate all biodiversity in natural ecosystems?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how two plant species compete for limited sunlight and soil nutrients, with resource depletion creating feedback that determines which species thrives."),
        ("Disciplinary Core Idea", "LS2.A Interdependent Relationships in Ecosystems", "Organisms and populations of organisms are dependent on their environmental interactions both with other living things and with nonliving factors. Competition for resources influences organism growth, survival, and reproduction."),
        ("Crosscutting Concept", "Cause and Effect", "Students investigate how asymmetric resource capture causes one species to dominate another, identifying the feedback mechanisms that amplify small initial advantages into large competitive outcomes.")
    ],
    "cast_items": [
        "Explain how competition for limited resources affects the growth and survival of organisms",
        "Model the relationship between resource availability and population growth for competing species",
        "Predict outcomes of interspecific competition based on resource capture advantages"
    ],
    "cast_questions": [
        ("Multiple Choice:", "In a field, Species A grows 2 cm taller per week than Species B. After 8 weeks, Species A is significantly taller and Species B is wilting. Based on the competition model, what is the most likely cause of Species B's decline?"),
        ("Constructed Response:", "Using your competition model, explain why invasive plant species often outcompete native plants when introduced to a new ecosystem. Reference sunlight capture, soil nutrient depletion, and the feedback loop between growth and resource availability.")
    ],
    "background_intro": "Competition is one of the fundamental forces shaping ecosystems. When two organisms need the same limited resource, the outcome of their competition determines which species thrive, which decline, and how communities are structured. Understanding competition reveals why ecosystems look the way they do.",
    "background_sections": [
        ("Competition for Light Is Asymmetric", "Unlike nutrients or water, light comes from above. This means competition for light is inherently asymmetric: a taller plant shades a shorter one, but the shorter plant cannot shade the taller one. This asymmetry means that any height advantage compounds over time. The taller plant gets more light, grows more, gets even taller, and shades the shorter plant even more. This positive feedback loop is why forests have distinct canopy layers."),
        ("The Competitive Exclusion Principle", "Ecologist G.F. Gause demonstrated in 1934 that two species competing for the exact same resource in the exact same way cannot coexist indefinitely. One will always eventually outcompete the other. This is why no two species occupy exactly the same ecological niche. When species do coexist, they have evolved to partition resources: different root depths, different light requirements, different growing seasons."),
        ("Resource Depletion Feedback", "As competing organisms consume resources, those resources become scarcer. Scarcity intensifies competition because organisms must work harder (grow taller, extend roots deeper) to access what remains. This creates a feedback loop: growth depletes resources, scarcity intensifies competition, competition favors the stronger competitor, and the weaker competitor declines further. This feedback is why competition often leads to clear winners and losers."),
        ("Coexistence Through Niche Partitioning", "Despite the competitive exclusion principle, ecosystems are full of biodiversity. Species coexist by partitioning resources: different depths in the soil, different heights in the canopy, different times of day for activity, or different types of nutrients. Some plants are shade-tolerant, thriving in the understory with less light. Others are sun-loving and dominate the canopy. This diversity of strategies allows many species to share an ecosystem.")
    ],
    "lever_L": "Students identify sunlight available and soil nutrients as the two external components, and Plant A growth, Plant B growth, and resource depletion as the three internal responses of the competition system.",
    "lever_E": "Students determine that sunlight positively drives both plant growth rates, soil nutrients positively drive both plant growth rates, both growth rates positively increase resource depletion, and resource depletion negatively reduces available sunlight and nutrients in a feedback loop.",
    "lever_V": "Students build a model showing how two plants draw from shared resource pools, with growth creating resource depletion that feeds back to limit both plants, especially the weaker competitor.",
    "lever_Ev": "Students run equal-start and one-plant-advantage scenarios to observe how small initial differences amplify through the competition feedback loop.",
    "lever_R": "Students add water availability or root depth difference to explore how resource partitioning changes competition outcomes.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with forest canopy and understory contrast", "say": "There is enough sunlight hitting this forest to power a small city. So why are the plants on the forest floor so small and struggling?", "do": "Show a photo of a dense forest canopy with dim understory. Let students observe the light difference.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are modeling what happens when two plants fight for the same sunlight and nutrients. Spoiler: it is not a fair fight.", "do": "Have students read objectives. Pre-teach 'interspecific competition' and 'competitive exclusion.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why can't two plants share the same sunlight?", "say": "If I put two plants side by side with the same soil and light, will they both grow equally? What if one starts just a little taller?", "do": "Think-pair-share: What do you think will happen to two identical plants growing next to each other?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "Our model has a hidden feedback loop. When one plant grows, it takes resources from the other, which makes the first plant grow even more.", "do": "Sketch the feedback loop: growth captures resources, which starves the competitor, which frees more resources for the winner.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for competition model", "say": "Sunlight and soil nutrients are given by the environment. But plant growth and resource depletion are driven by the competition itself.", "do": "Guide sorting. Discuss why both plants draw from the same resource pools.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows showing competition dynamics", "say": "Here is the critical connection: Plant A's growth DEPLETES resources, which REDUCES Plant B's growth. And Plant B's growth does the same to Plant A.", "do": "Trace the competition loop. Both plants feed resource depletion, which hurts both, but hurts the weaker one more.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions for equal start vs. one plant advantage", "say": "What if Plant A starts just 1 centimeter taller? Does that tiny advantage matter? Let's find out.", "do": "Students predict outcomes. Run equal start and slight advantage scenarios. Watch how small differences amplify.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings about competition and resource depletion", "say": "Even a tiny advantage compounds over time because the winner captures more resources, grows more, and captures even more. It is a snowball effect.", "do": "Connect to real examples: invasive species, forest succession, why weeding a garden helps your plants.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Coexistence garden design challenge", "say": "Can you outsmart competitive exclusion? Design a garden where two competing species BOTH thrive.", "do": "Provide plant data cards with light and nutrient needs. Students design planting arrangements that partition resources.", "time": "12 min"}
    ],
    "sort_reasoning": "Sunlight Available is external because it is determined by the environment (time of day, season, weather) and is not controlled by the plants. Soil Nutrients is external because it represents the existing mineral content of the soil before the plants begin competing. Plant A Growth and Plant B Growth are internal because they are responses driven by the available resources and competition dynamics. Resource Depletion is internal because it is a consequence of both plants consuming shared resources and creates the feedback that intensifies competition.",
    "relationships": [
        ("Sunlight Available to Plant A Growth", "POSITIVE (+)", "More available sunlight provides more energy for photosynthesis, allowing Plant A to produce more biomass and grow taller."),
        ("Sunlight Available to Plant B Growth", "POSITIVE (+)", "More available sunlight provides more energy for Plant B's photosynthesis, but this is reduced if Plant A shades Plant B."),
        ("Soil Nutrients to Plant A Growth", "POSITIVE (+)", "More soil nutrients provide the minerals needed for cell growth and reproduction, supporting Plant A's biomass increase."),
        ("Soil Nutrients to Plant B Growth", "POSITIVE (+)", "More soil nutrients support Plant B's growth, but competition with Plant A for the same nutrient pool limits availability."),
        ("Plant A Growth to Resource Depletion", "POSITIVE (+)", "As Plant A grows, it consumes more sunlight (through shading) and more soil nutrients (through root absorption), increasing the rate of resource depletion."),
        ("Plant B Growth to Resource Depletion", "POSITIVE (+)", "As Plant B grows, it also consumes sunlight and nutrients, contributing to overall resource depletion in the shared environment."),
        ("Resource Depletion to Plant A Growth", "NEGATIVE (-)", "As resources are depleted, there is less sunlight and fewer nutrients available for Plant A, slowing its growth rate."),
        ("Resource Depletion to Plant B Growth", "NEGATIVE (-)", "Resource depletion reduces available sunlight and nutrients for Plant B. Because Plant A may already be capturing more, Plant B is disproportionately affected.")
    ],
    "sim_answers": [
        ("Equal Start Scenario", "When both plants start equal, the model shows an unstable equilibrium. Both plants grow and deplete resources at similar rates initially. But any tiny random variation breaks the symmetry. Once one plant gains even a slight advantage, the feedback loop amplifies it. The winner grows faster, depletes more resources, and the loser declines. This demonstrates competitive exclusion: identical niches cannot support two equal competitors long-term."),
        ("One Plant Advantage Scenario", "With Plant A starting taller, it immediately captures more sunlight and drives faster growth. Plant B receives less light from the start and grows slower. As Plant A grows more, it shades Plant B further and depletes soil nutrients faster. Plant B's growth rate drops toward zero while Plant A continues to dominate. The model clearly shows how small initial advantages compound through the resource depletion feedback loop.")
    ],
    "reflection_exemplars": [
        ("Why does a small head start give a compounding advantage?", "A slightly taller plant captures slightly more sunlight, which produces slightly more growth, which makes it slightly taller still. Each cycle through the feedback loop amplifies the advantage. Meanwhile, the shorter plant gets progressively less light and fewer nutrients because the taller plant is consuming them. The advantage does not just maintain itself; it accelerates. This is why early establishment is so important in plant ecology and why invasive species that arrive first often dominate."),
        ("Why does competitive exclusion not eliminate all biodiversity?", "Competitive exclusion says two species with identical niches cannot coexist, but ecosystems have enormous biodiversity because no two species occupy truly identical niches. Species partition resources: different root depths access different soil layers, shade-tolerant species thrive under canopies that sun-loving species need, some plants grow in spring while others grow in summer. This niche partitioning means species avoid direct competition for the exact same resource, allowing coexistence.")
    ],
    "stem_intro": "Present the challenge: Design a garden planting arrangement where two competing plant species can both thrive in the same space. Use provided plant data cards (light needs, root depth, nutrient requirements) to select species and arrange them so they partition resources rather than directly compete. Monitor growth of both species over 3 weeks.",
    "stem_concepts": [
        ("Resource Partitioning", "Species that use different parts of the same resource (different soil depths, different light levels) can coexist because they are not directly competing."),
        ("Companion Planting", "Some plant combinations benefit each other. Tall sun-loving plants can shade heat-sensitive plants below. Deep-rooted plants access nutrients that shallow-rooted plants cannot reach."),
        ("Carrying Capacity", "Every environment has a maximum amount of life it can support based on available resources. Exceeding carrying capacity leads to resource depletion and population decline.")
    ],
    "stem_eval": [
        ("Expert (4)", "Both species show healthy growth over 3 weeks with clear data, planting arrangement explicitly designed for resource partitioning, and design choices connected to competition model evidence"),
        ("Proficient (3)", "Both species survive with growth data collected, planting arrangement shows resource partitioning strategy, and connection to competition concepts explained"),
        ("Developing (2)", "Plants are arranged with some strategy but limited data on growth outcomes or unclear connection to competition principles"),
        ("Beginning (1)", "Random planting arrangement with no resource partitioning strategy or data collection")
    ],
    "support": [
        "Provide plant data cards with specific light, water, and nutrient requirements for different species",
        "Use a lamp and two plants at different heights to physically demonstrate light competition in the classroom",
        "Sentence frames: 'When Plant A grows taller, Plant B's growth __ because __'"
    ],
    "extensions": [
        "Research a real example of competitive exclusion (red and gray squirrels in the UK, Gause's paramecium experiments) and explain the outcome using your competition model",
        "Design an experiment to test whether root competition or light competition has a greater effect on plant growth",
        "Investigate how invasive plant species like kudzu or purple loosestrife outcompete native plants and connect to your model's feedback loops"
    ],
    "cross_curr": [
        ("Math", "Graph the growth curves of both plants over time and calculate the rate at which the gap between them widens, identifying exponential growth patterns"),
        ("ELA", "Write a narrative from the perspective of Plant B as it slowly loses the competition for light, incorporating scientific vocabulary about resource limitation"),
        ("Social Studies", "Research how competition for agricultural land and water resources has shaped human settlement patterns and conflicts throughout history")
    ],
    "misconceptions": [
        ("Plants cooperate and share resources", "While some mutualistic relationships exist (mycorrhizal networks), plants in close proximity generally compete intensely for light, water, and nutrients. They do not share resources voluntarily. Even trees connected by fungal networks are engaged in complex competitive and cooperative dynamics, not simple sharing.", "Set up two plants under one lamp and observe over two weeks. The taller or faster-growing plant will shade the other, demonstrating competition rather than sharing."),
        ("Competition only matters when resources are scarce", "Competition occurs whenever organisms use the same resource, even if that resource seems abundant. Two plants can compete for sunlight even on a bright day because one shades the other. Competition shapes growth patterns long before resources become critically scarce.", "Use the model to show that even with high sunlight available, Plant A's shading of Plant B reduces Plant B's growth rate."),
        ("The bigger plant always wins", "While size is a major advantage, other factors matter. A smaller plant with deeper roots might access nutrients the taller plant cannot reach. A shade-tolerant species might thrive in the understory. The 'winner' depends on which resources are most limiting and how each species accesses them.", "Introduce the root depth component and show a scenario where the shorter plant with deeper roots outcompetes the taller plant when soil nutrients become the limiting factor.")
    ]
}

L10 = {
    "id": "G06L2-L10",
    "title": "Why Do Some Countries Run Out of Water?",
    "subtitle": "Modeling Water Stress from Rainfall, Population, and Consumption",
    "ngss": "MS-ESS3-1, MS-ESS3-4",
    "ngss_desc": "Construct a scientific explanation based on evidence for how the uneven distributions of Earth's mineral, energy, and groundwater resources are the result of past and current geoscience processes. Construct an argument supported by evidence for how increases in human population and per-capita consumption of natural resources impact Earth's systems.",
    "big_question": "If Earth has the same amount of water it has always had, why are some countries running out?",
    "objectives": [
        "Model how rainfall patterns and population density interact to create water stress",
        "Explain the relationship between aquifer recharge rates and water demand",
        "Predict which conditions lead to sustainable water use versus water crisis",
        "Analyze how the Water Stress Index reflects the balance between supply and demand",
        "Evaluate how human population growth and consumption patterns affect groundwater systems"
    ],
    "vocabulary": [
        ("Aquifer", "An underground layer of rock or sediment that holds groundwater, recharged by rainfall seeping through soil over months to thousands of years"),
        ("Water Stress", "A condition where water demand in a region approaches or exceeds the available supply, measured as the ratio of withdrawal to availability"),
        ("Recharge Rate", "The speed at which an aquifer is replenished by rainfall infiltration, which is often much slower than the rate of human extraction"),
        ("Per-Capita Consumption", "The average amount of water used by each person in a population, which varies greatly between countries and lifestyles"),
        ("Water Stress Index", "A numerical measure of how close a region is to using all its renewable water supply, with higher values indicating greater risk of shortage")
    ],
    "components": [
        ("Rainfall Pattern", "The amount, timing, and distribution of precipitation that provides the primary input of freshwater to a region", True),
        ("Population Density", "The number of people per unit area, which drives total water demand through domestic, agricultural, and industrial use", True),
        ("Aquifer Recharge", "The rate at which groundwater supplies are naturally replenished by rainfall infiltration through soil and rock", False),
        ("Water Demand", "The total amount of water withdrawn for human use including drinking, agriculture, industry, and sanitation", False),
        ("Water Stress Index", "A measure of the gap between available water supply and human water demand, indicating sustainability or crisis", False)
    ],
    "think_about_it": "When rainfall decreases, what happens to aquifer recharge? If population density increases while rainfall stays the same, what happens to the Water Stress Index?",
    "scenarios": [
        ("Sustainable Balance", "Set moderate rainfall and low population density, then observe aquifer recharge and water stress"),
        ("Growing Demand", "Keep rainfall constant but gradually increase population density to observe when water stress becomes critical"),
        ("Drought Crisis", "Lock rainfall to very low levels with moderate population and observe the growing gap between recharge and demand")
    ],
    "sim_scenarios": [
        ("Sustainable Balance", "Moderate rainfall, low population density", "What do you predict will happen to the Water Stress Index when rainfall is sufficient and population is low?"),
        ("Growing Demand", "Constant rainfall, population increasing", "What do you predict will happen to Aquifer Recharge compared to Water Demand as population grows?"),
        ("Drought Crisis", "Very low rainfall, moderate population", "What do you predict will happen to the Water Stress Index when drought reduces rainfall but water demand stays the same?")
    ],
    "discoveries": [
        "Water stress is not about total water on Earth but about the balance between local supply and local demand",
        "Aquifer recharge can take years to centuries, while human extraction can drain aquifers in decades",
        "Population growth increases water demand even when per-capita consumption stays constant",
        "Rainfall patterns are uneven across the globe, creating natural water-rich and water-poor regions",
        "The Water Stress Index can tip from sustainable to crisis when either supply drops or demand rises past a threshold"
    ],
    "answer": "Countries run out of water not because Earth's total water supply is shrinking but because the balance between local water supply and local demand becomes unsustainable. Rainfall patterns are geographically uneven, so some regions receive far less freshwater than others. When population density grows in these regions, water demand rises while aquifer recharge stays limited by rainfall. Humans can extract water from aquifers much faster than rain can replenish them. The result is a growing gap between supply and demand: the Water Stress Index rises until the region faces a water crisis.",
    "stem_title": "Design a Water Management Plan",
    "stem_mission": "Design a sustainable water management plan for a fictional growing city that prevents water stress from exceeding critical levels over the next 50 years.",
    "stem_scenario": "A rapidly growing city in a semi-arid region currently has moderate water stress. Population projections show the city will triple in size over the next 50 years while climate models predict a 15% decrease in annual rainfall. Your environmental engineering team must design a comprehensive water management strategy that keeps the Water Stress Index below crisis level.",
    "stem_questions": [
        "How will you reduce water demand without limiting population growth?",
        "What strategies can increase aquifer recharge even with less rainfall?",
        "How will you balance agricultural, industrial, and domestic water needs?"
    ],
    "stem_design_qs": [
        "What conservation measures will reduce per-capita water consumption?",
        "What infrastructure (rainwater harvesting, wastewater recycling, desalination) will supplement natural supply?",
        "How will you prioritize water allocation between agriculture, industry, and households?",
        "How will you monitor the Water Stress Index over time and trigger emergency measures if needed?"
    ],
    "career": "Hydrologists and Water Resource Engineers study water systems and design sustainable management plans to ensure communities have clean water. They earn $60,000-$115,000/year.",
    "images": {
        "cover": ("cover-water-stress.png", "A photorealistic aerial view of a landscape split between a lush green irrigated area and a dry cracked earth region, showing the contrast between water availability and scarcity, dramatic lighting"),
        "landscape": ("landscape-water-stress.png", "A diverse group of 6th grade students examining a watershed model on a table, a Black student pouring water over the model while a Latino student measures runoff with a graduated cylinder, bright science lab"),
        "modeling": ("modeling-water-stress.png", "6th grade students building a water stress model on laptops, an Asian student adjusting rainfall values while a White student watches the Water Stress Index change on screen, modern classroom with water cycle posters"),
        "discussion": ("discussion-water-stress.png", "A teacher showing a world map of water stress levels on a smartboard to 6th grade students, pointing to high-stress regions while diverse students compare their own city's water use, engaged classroom"),
        "stem": ("stem-water-plan.png", "6th grade students collaborating on water management plans at lab tables with maps and calculators, a Latino student presenting their plan while a Black student points to projected population data, collaborative STEM lab")
    },
    "pre_assessment": [
        "Where does the water that comes out of your tap originally come from?",
        "Why do you think some places in the world do not have enough clean water?",
        "If Earth is 70% covered in water, why would any country run out of water?",
        "Draw what you think happens to rainwater after it hits the ground."
    ],
    "extend_components": [
        ("Climate Change Effect", "Long-term shifts in rainfall patterns and temperature that can permanently reduce water supply in some regions and increase it in others"),
        ("Agricultural Water Use", "Water consumed by farming, which typically accounts for 70% of all freshwater withdrawal globally and is often the largest demand on aquifers"),
        ("Water Recycling Rate", "The percentage of used water that is treated and returned to the supply system, which can significantly reduce net demand on freshwater sources")
    ],
    "reflections": [
        "Why is water stress a local problem even though Earth has a global water cycle?",
        "How is the time mismatch between aquifer recharge and human extraction the root of water crises?",
        "What would happen to your model if a country doubled its population but also cut per-capita consumption in half?",
        "Why might two countries with the same rainfall have very different Water Stress Indexes?",
        "How does your model show that water stress is about balance, not just about supply?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how rainfall patterns and population density interact through aquifer recharge and water demand to produce a Water Stress Index indicating sustainability or crisis."),
        ("Disciplinary Core Idea", "ESS3.A Natural Resources / ESS3.C Human Impacts on Earth Systems", "Humans depend on Earth's land, ocean, atmosphere, and biosphere for freshwater resources. Increases in human population and per-capita consumption of natural resources impact Earth's groundwater systems."),
        ("Crosscutting Concept", "Stability and Change", "Students investigate how the balance between water supply and demand can shift from stable sustainability to unstable crisis through changes in rainfall, population, or consumption patterns.")
    ],
    "cast_items": [
        "Explain how uneven distribution of freshwater resources creates water-rich and water-poor regions",
        "Model the relationship between human population growth and groundwater depletion",
        "Predict water stress outcomes based on changes in rainfall patterns and population density"
    ],
    "cast_questions": [
        ("Multiple Choice:", "City A and City B both receive 500 mm of annual rainfall. City A has 100,000 residents and City B has 1,000,000 residents. Based on the water stress model, which city is more likely to face a water crisis, and what is the primary factor causing the difference?"),
        ("Constructed Response:", "Using your water stress model, explain why Cape Town, South Africa nearly ran out of water in 2018 even though it receives moderate annual rainfall. Reference rainfall patterns, population growth, aquifer recharge rates, and the Water Stress Index in your explanation.")
    ],
    "background_intro": "Water is the most essential resource for human civilization, yet billions of people face water scarcity. Understanding why requires modeling the complex balance between natural water supply and human water demand, a balance that is shifting in dangerous directions around the world.",
    "background_sections": [
        ("Uneven Distribution of Freshwater", "Only about 2.5% of Earth's water is freshwater, and most of that is locked in ice caps and glaciers. The freshwater available for human use (rivers, lakes, accessible groundwater) is unevenly distributed by geography and climate. Some regions receive heavy rainfall while others are arid. This natural inequality means water stress is fundamentally a geographic problem, not a global shortage."),
        ("Aquifers: Underground Water Banks", "Aquifers are layers of permeable rock or sediment that store groundwater. They are recharged when rainfall filters through the soil, a process that can take months to thousands of years depending on the aquifer depth and geology. Humans extract water from aquifers using wells and pumps. When extraction exceeds recharge (overdraft), the aquifer level drops, wells go dry, and land can permanently compact (subsidence), destroying storage capacity forever."),
        ("Population Growth and Water Demand", "Global water demand has increased six-fold over the past century, driven primarily by population growth, agricultural expansion, and industrial development. Agriculture alone accounts for roughly 70% of freshwater withdrawal. As populations grow in water-stressed regions, the gap between demand and supply widens. Per-capita consumption also matters: an average American uses about 300 liters per day, while a person in sub-Saharan Africa may use only 20 liters."),
        ("Tipping Points and Water Crisis", "Water systems can shift from stressed to crisis rapidly. Cape Town nearly reached 'Day Zero' in 2018, when taps would be shut off. The Aral Sea, once the world's fourth-largest lake, has nearly disappeared due to irrigation diversion. The Ogallala Aquifer in the US Great Plains is being depleted 3-10 times faster than it recharges. These examples show that water systems have tipping points beyond which recovery becomes extremely difficult or impossible.")
    ],
    "lever_L": "Students identify rainfall pattern and population density as the two external components, and aquifer recharge, water demand, and Water Stress Index as the three internal responses of the water stress system.",
    "lever_E": "Students determine that rainfall positively drives aquifer recharge, population density positively drives water demand, aquifer recharge negatively reduces water stress (more recharge means less stress), and water demand positively increases the Water Stress Index.",
    "lever_V": "Students build a model showing how rainfall feeds aquifer recharge while population drives demand, with the Water Stress Index reflecting the balance between supply and demand.",
    "lever_Ev": "Students run sustainable balance, growing demand, and drought crisis scenarios to observe how the Water Stress Index responds to changes in either supply or demand.",
    "lever_R": "Students add climate change effects or agricultural water use to explore how additional factors compound water stress beyond basic supply and demand.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with contrast between green and arid landscape", "say": "Earth has 326 million trillion gallons of water. That is a 326 followed by 18 zeros. So how is it possible that Cape Town almost turned off all its taps in 2018?", "do": "Show a photo of Cape Town's empty reservoirs during the crisis. Let students react to the contrast between Earth's total water and a city's shortage.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are modeling why some countries face water crises while others have plenty. The answer is about balance, not total supply.", "do": "Have students read objectives. Pre-teach 'aquifer,' 'recharge rate,' and 'Water Stress Index.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why do some countries run out of water?", "say": "If the water cycle recycles all water and Earth never loses water, how can any place run out?", "do": "Think-pair-share: Where does your tap water come from? What would happen if no rain fell for a year?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "Water stress is about the BALANCE between how fast nature refills the supply and how fast humans drain it. Our model captures this balance.", "do": "Draw a simple balance scale: rainfall and recharge on one side, population and demand on the other. Water Stress Index is the needle.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for water stress model", "say": "Rainfall and population are givens that we cannot control in the model. But recharge, demand, and the stress index respond to those inputs.", "do": "Guide sorting. Discuss why rainfall pattern is external (weather) and population density is external (demographics).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between water stress components", "say": "Here is the critical insight: aquifer recharge is SLOW, measured in months to centuries. Water demand is FAST, measured in daily consumption. That time mismatch is what creates water stress.", "do": "Trace both paths: rainfall to recharge to supply, and population to demand. Show how the stress index compares the two.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions for sustainable vs. growing demand vs. drought", "say": "What happens when a city triples in size but the rain stays the same? Let's model it.", "do": "Students predict outcomes. Run all three scenarios. Watch the Water Stress Index cross from green to yellow to red.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings about water stress balance", "say": "Countries do not run out of water because Earth is drying up. They run out because they are using it faster than nature can replace it, and that is a choice we can change.", "do": "Show real-world examples: Ogallala Aquifer depletion, Aral Sea disappearance, Singapore's water recycling success.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Water management plan challenge", "say": "Your city is tripling in size and rainfall is dropping. Design a 50-year water plan that keeps the stress index below crisis.", "do": "Provide city data sheets with population projections and rainfall forecasts. Teams design management plans balancing conservation, infrastructure, and allocation.", "time": "12 min"}
    ],
    "sort_reasoning": "Rainfall Pattern is external because it is determined by geographic location and climate, not by human activity within the system. Population Density is external because it is driven by demographic trends that are inputs to the water system rather than outputs. Aquifer Recharge is internal because its rate responds to rainfall patterns and soil conditions. Water Demand is internal because it is generated by the population's consumption patterns within the system. Water Stress Index is internal because it is a calculated measure of the balance between the supply (recharge) and demand sides of the system.",
    "relationships": [
        ("Rainfall Pattern to Aquifer Recharge", "POSITIVE (+)", "More rainfall provides more water that can infiltrate through soil and rock to replenish groundwater stores. Less rainfall means slower recharge."),
        ("Population Density to Water Demand", "POSITIVE (+)", "More people in an area means more total water consumption for drinking, cooking, sanitation, agriculture, and industry, increasing overall demand."),
        ("Aquifer Recharge to Water Stress Index", "NEGATIVE (-)", "Higher aquifer recharge means more water is being replenished, which reduces the gap between supply and demand and lowers the Water Stress Index."),
        ("Water Demand to Water Stress Index", "POSITIVE (+)", "Higher water demand increases the gap between what humans need and what the environment can supply, raising the Water Stress Index toward crisis levels."),
        ("Rainfall Pattern to Water Stress Index (indirect)", "NEGATIVE (-)", "This indirect path shows how rainfall ultimately reduces water stress by feeding aquifer recharge, which increases available supply relative to demand.")
    ],
    "sim_answers": [
        ("Sustainable Balance vs. Growing Demand", "With moderate rainfall and low population, aquifer recharge keeps pace with water demand and the Water Stress Index remains low (green zone). As population triples while rainfall stays constant, water demand climbs steeply but aquifer recharge remains unchanged. The Water Stress Index crosses from sustainable to stressed to critical. The model reveals that the crisis is not caused by less water but by more demand on the same supply."),
        ("Drought Crisis Scenario", "When rainfall drops to very low levels, aquifer recharge slows dramatically. Even with moderate population, water demand now far exceeds the rate of replenishment. The Water Stress Index rises rapidly into crisis territory. The model shows that both supply reduction (drought) and demand increase (population) push toward the same crisis, and when both occur simultaneously, the effect is compounded.")
    ],
    "reflection_exemplars": [
        ("Why is water stress a local problem if Earth has a global water cycle?", "The water cycle moves water globally through evaporation, precipitation, and runoff, but it deposits water unevenly. Some regions get heavy rainfall while others are arid. Water stress occurs when local demand exceeds local supply. A region cannot easily use water that is falling thousands of miles away. It takes massive infrastructure (dams, pipelines, desalination) to move water from where it is to where it is needed. Until then, water stress is fundamentally a local mismatch between where rain falls and where people live."),
        ("What would happen if a country doubled population but halved per-capita consumption?", "Total water demand would stay roughly the same (2x people times 0.5x consumption per person = 1x total demand). The Water Stress Index would remain unchanged because the supply-demand balance would not shift. This shows that per-capita consumption is just as important as population size. It also reveals a policy lever: reducing consumption per person can offset population growth. This is exactly what Singapore and Israel have done through aggressive conservation and water recycling.")
    ],
    "stem_intro": "Present the challenge: A semi-arid city currently has a Water Stress Index of 0.6 (moderate stress). Population will triple in 50 years and rainfall is projected to decrease 15%. Design a comprehensive water management plan that keeps the Water Stress Index below 0.8 (crisis threshold) for the entire 50-year period. Your plan must address conservation, infrastructure, and allocation priorities.",
    "stem_concepts": [
        ("Water Conservation", "Reducing per-capita water consumption through efficient fixtures, landscaping changes, pricing signals, and public education. Conservation is the cheapest way to reduce water stress."),
        ("Water Recycling and Desalination", "Treating wastewater for reuse and converting seawater to freshwater. These technologies increase the effective water supply but require energy and infrastructure investment."),
        ("Aquifer Management", "Protecting recharge zones, limiting extraction rates, and using managed aquifer recharge (deliberately infiltrating treated water into aquifers) to maintain long-term groundwater supply.")
    ],
    "stem_eval": [
        ("Expert (4)", "Comprehensive 50-year plan addresses conservation, infrastructure, and allocation with quantitative targets, keeps Water Stress Index below threshold with evidence, and connects strategies to model components"),
        ("Proficient (3)", "Multi-strategy plan addresses at least two areas (conservation, infrastructure, allocation) with clear connection to water stress model"),
        ("Developing (2)", "Plan includes some strategies but lacks quantitative targets or clear connection to how they reduce the Water Stress Index"),
        ("Beginning (1)", "Minimal plan with single strategy and no connection to the water stress model or quantitative reasoning")
    ],
    "support": [
        "Provide a world map showing water stress levels so students can identify real-world examples",
        "Use a simple bucket with a small hole (recharge) and a cup for scooping (demand) to physically model the supply-demand balance",
        "Sentence frames: 'When population density increases, water demand __ because __'"
    ],
    "extensions": [
        "Research a real water crisis (Cape Town Day Zero, Flint Michigan, Aral Sea shrinkage) and explain it using your water stress model components",
        "Calculate your household's daily water consumption and compare it to the global average. How would your water stress model change if everyone consumed at your household's rate?",
        "Investigate how Israel became a world leader in water management despite being in one of the driest regions on Earth, and identify which model components they changed"
    ],
    "cross_curr": [
        ("Math", "Calculate the Water Stress Index for different cities using real rainfall and population data. Graph how the index changes as population grows at 3% per year"),
        ("ELA", "Write a persuasive letter to a city council explaining why the current water usage rate is unsustainable and proposing three evidence-based solutions from your model"),
        ("Social Studies", "Research how competition for water resources has contributed to conflicts between nations (Egypt-Ethiopia Nile dispute, India-Pakistan Indus Treaty) and connect to your water stress model")
    ],
    "misconceptions": [
        ("Earth is running out of water", "Earth has the same amount of water it has always had. Water is not created or destroyed in the water cycle, only moved and transformed. The problem is distribution: freshwater is unevenly distributed, and humans are consuming it faster than nature replenishes it in certain locations. It is a local balance problem, not a global shortage.", "Show the water cycle diagram and emphasize that water is recycled. Then show the water stress world map to show the problem is WHERE water is, not HOW MUCH exists."),
        ("Rainfall alone determines water stress", "Rainfall is only the supply side of the equation. Water stress depends on the BALANCE between supply and demand. A region with low rainfall but also low population may have no water stress, while a region with moderate rainfall but massive population can be in crisis. Both supply and demand must be modeled together.", "Compare two scenarios in the model: low rainfall with low population (low stress) vs. moderate rainfall with high population (high stress). Students see that demand matters as much as supply."),
        ("Groundwater is unlimited because it refills from rain", "While aquifers do recharge from rainfall, the process can take years to thousands of years depending on depth and geology. Humans can extract water from an aquifer with a pump in minutes. This time mismatch means that aquifers can be depleted far faster than they recharge, effectively mining fossil water that took millennia to accumulate.", "Show the Ogallala Aquifer data: recharged over thousands of years, being depleted in decades. Have students calculate how long the aquifer would last at current extraction rates versus recharge rates.")
    ]
}
