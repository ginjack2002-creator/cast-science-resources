#!/usr/bin/env python3
"""Complete lesson data for G10L2-L01 through G10L2-L10 (Grade 10 Level 2: Systems Under Pressure)"""

L01 = {
    "id": "G10L2-L01",
    "title": "Why Is Lithium the New Gold?",
    "subtitle": "Modeling the Resource Economics of the Electric Vehicle Revolution",
    "ngss": "HS-ESS3-1, HS-PS1-3",
    "ngss_desc": "Construct an explanation based on evidence for how the availability of natural resources, occurrence of natural hazards, and changes in climate have influenced human activity. Plan and conduct an investigation to gather evidence to compare the structure of substances at the bulk scale to infer the structure of atoms and molecules.",
    "big_question": "Why has a soft, silvery metal that most people have never heard of become the most fought-over resource on the planet?",
    "objectives": [
        "Model how lithium demand, mining capacity, and recycling interact to determine global supply stability",
        "Analyze the feedback loops connecting EV adoption rates to lithium market prices and environmental consequences",
        "Predict how changes in battery technology and recycling infrastructure could shift the lithium supply crisis",
        "Evaluate the trade-offs between accelerating the green energy transition and the environmental cost of lithium extraction"
    ],
    "vocabulary": [
        ("Critical Mineral", "A natural resource that is essential for modern technology and economic security but faces significant supply chain risks due to geological scarcity, geopolitical concentration, or extraction difficulty"),
        ("Brine Extraction", "The primary method of lithium mining, which pumps underground saltwater into massive evaporation ponds where solar energy concentrates lithium over 12-18 months — consuming enormous quantities of water in arid regions"),
        ("Circular Economy", "An economic model that designs waste out of the system by reusing, repairing, and recycling materials instead of the traditional extract-use-dispose linear model"),
        ("Supply Chain Bottleneck", "A point in a production system where demand exceeds the capacity to supply, creating shortages, price spikes, and cascading delays throughout the entire manufacturing chain")
    ],
    "components": [
        ("Lithium Demand", "The total global demand for lithium driven by EV batteries, grid storage, consumer electronics, and industrial applications — growing at 25-35% annually", False),
        ("Mining Rate", "The volume of lithium extracted from brine pools and hard-rock mines globally per year, constrained by geological deposits, water availability, and permitting timelines", False),
        ("Environmental Damage", "The cumulative ecological harm caused by lithium extraction including aquifer depletion, toxic waste generation, habitat destruction, and indigenous community displacement", False),
        ("Battery Performance", "The energy density, charge speed, lifespan, and cost per kilowatt-hour of lithium-ion batteries, which determines how much lithium each vehicle requires", False),
        ("Recycling Rate", "The percentage of lithium from end-of-life batteries that is successfully recovered and returned to the supply chain through hydrometallurgical or pyrometallurgical processes", True),
        ("Market Price", "The spot price of battery-grade lithium carbonate or hydroxide on global commodity markets, driven by the balance between supply and demand", False),
        ("EV Adoption", "The rate at which consumers and fleet operators purchase electric vehicles instead of internal combustion engine vehicles, driven by policy, price, and infrastructure", True)
    ],
    "think_about_it": "When EV Adoption surges, Lithium Demand spikes — but Mining Rate cannot increase quickly because new mines take 7-10 years to develop. What happens to Market Price? And when Market Price rises, does it accelerate or slow Recycling Rate investment? Where are the feedback loops?",
    "scenarios": [
        ("Steady Growth", "Set EV Adoption to moderate growth with current Mining Rate — observe how supply and demand balance over a decade"),
        ("EV Boom Without Recycling", "Set EV Adoption to rapid growth with Recycling Rate near zero — observe the supply crisis and environmental consequences"),
        ("Circular Economy Transition", "Set Recycling Rate to 90% and moderate EV Adoption — observe how recycled lithium changes the supply dynamics")
    ],
    "sim_scenarios": [
        ("Steady Growth", "Moderate EV adoption, current mining capacity", "What do you predict will happen to Market Price if EV Adoption grows steadily but Mining Rate stays flat?"),
        ("EV Boom, No Recycling", "Rapid EV adoption, zero recycling", "What do you predict happens to Environmental Damage when all lithium comes from new mining operations?"),
        ("Circular Economy", "High recycling, moderate adoption", "Do you predict that high Recycling Rate can significantly reduce the need for new Mining Rate?")
    ],
    "discoveries": [
        "Lithium supply cannot keep pace with projected EV demand because new mines take 7-10 years to develop while demand is growing 25-35% annually",
        "The environmental cost of lithium extraction creates a painful paradox — the green energy transition requires mining practices that damage ecosystems and water supplies",
        "High Market Price triggers both increased mining investment AND increased recycling investment, but on very different timescales — recycling infrastructure can scale faster",
        "A circular economy approach combining improved Battery Performance (less lithium per vehicle) and high Recycling Rate is the only path that resolves the supply-demand-environment trilemma"
    ],
    "answer": "Lithium has become the new gold because it is irreplaceable in the batteries powering the electric vehicle revolution, yet global supply chains are dangerously strained. Demand is growing at 25-35% annually while new mines take a decade to develop. The extraction process consumes massive amounts of water in some of the world's driest regions. Market prices have swung wildly — lithium carbonate went from $6,000/ton to $80,000/ton and back in just two years. The only sustainable path forward combines three strategies: improving battery chemistry to use less lithium per vehicle, scaling recycling infrastructure to recover lithium from end-of-life batteries, and developing mining practices that minimize environmental destruction.",
    "stem_title": "Design a Lithium Supply Chain Resilience Plan",
    "stem_mission": "Design a 20-year lithium supply strategy for an EV manufacturer that balances cost, environmental responsibility, and supply security.",
    "stem_scenario": "A major electric vehicle company projects it will need 10x its current lithium supply within eight years. Current suppliers cannot guarantee delivery. Your team has been hired to design a comprehensive supply strategy that ensures the company can meet production targets without contributing to environmental disaster.",
    "stem_questions": [
        "How would you balance sourcing from new mines versus investing in recycling facilities?",
        "What contingency plans would you build for lithium price volatility?",
        "How would you address the environmental and social justice concerns of lithium mining communities?"
    ],
    "stem_design_qs": [
        "What mix of lithium sources — brine, hard-rock, recycled, and next-generation — would you recommend?",
        "How would you structure long-term supply contracts to hedge against price swings?",
        "What role should battery chemistry research play in reducing lithium dependence?",
        "How would you communicate your environmental strategy to consumers and investors?"
    ],
    "career": "Supply Chain Engineers and Resource Economists analyze global material flows, predict shortages, and design resilient procurement strategies. They work for automotive companies, mining firms, government agencies, and consulting firms, earning $75,000–$150,000/year. Battery Materials Scientists developing next-generation chemistries earn $90,000–$160,000/year.",
    "images": {
        "cover": ("G10L2-L01-cover.png", "A photorealistic, cinematic image of a massive lithium evaporation pond in a stark desert landscape with turquoise-blue brine pools stretching to the horizon, an electric vehicle charging station in the foreground creating a visual juxtaposition between clean energy and raw extraction, dramatic golden-hour lighting"),
        "landscape": ("G10L2-L01-landscape.png", "A diverse group of 15-16 year old students in a modern chemistry lab examining lithium mineral samples and battery components, periodic table prominently displayed, engaged expressions and collaborative atmosphere, natural classroom lighting"),
        "modeling": ("G10L2-L01-modeling.png", "A diverse group of 15-16 year old students working on laptops building computational models of lithium supply chains, screens showing supply-demand graphs and global mining maps, modern classroom setting"),
        "discussion": ("G10L2-L01-discussion.png", "A teacher leading an animated discussion with diverse 15-16 year old students about resource economics, a world map showing lithium deposits and EV adoption rates displayed on a smartboard, students actively debating"),
        "stem": ("G10L2-L01-stem.png", "Diverse 15-16 year old students presenting supply chain strategy proposals with charts and infographics on large displays, professional presentation atmosphere with modern technology")
    },
    "pre_assessment": [
        "What do you know about where the materials in your phone battery come from?",
        "Why do you think electric vehicle prices have been so volatile in recent years?",
        "Draw a diagram showing how you think lithium gets from the ground into a car battery.",
        "What trade-offs might exist between fighting climate change and mining for battery materials?"
    ],
    "extend_components": [
        ("Geopolitical Risk", "The concentration of lithium reserves in a few countries (Australia, Chile, Argentina, China) creates supply vulnerability to political instability, trade disputes, and export restrictions"),
        ("Alternative Chemistry", "Research into sodium-ion, solid-state, and lithium-sulfur batteries that could reduce or eliminate lithium dependence in future battery generations"),
        ("Water Scarcity Index", "The ratio of lithium extraction water consumption to available freshwater in mining regions, which determines whether extraction is sustainable or destroys local water supplies")
    ],
    "reflections": [
        "How does your model reveal the tension between the urgency of climate action and the reality of resource extraction timelines?",
        "What feedback loops in your model create the most instability in lithium markets?",
        "How would your model's predictions change if a breakthrough in sodium-ion batteries eliminated lithium demand for EVs?",
        "What does your model suggest about the difference between a linear economy and a circular economy for critical minerals?",
        "What ethical considerations does your model raise about who bears the environmental cost of the green energy transition?"
    ],
    "dimensions": [
        ("Science Practice", "Constructing Explanations and Designing Solutions", "Students construct evidence-based explanations of lithium supply dynamics and design resource management strategies informed by computational model data."),
        ("Disciplinary Core Idea", "ESS3.A Natural Resources / PS1.A Structure and Properties of Matter", "The availability of lithium as a natural resource is constrained by geological distribution, extraction technology, and the atomic-level properties that make it uniquely suited for batteries."),
        ("Crosscutting Concept", "Cause and Effect / Systems and System Models", "Students trace causal chains from EV policy decisions through resource extraction to environmental consequences, modeling the lithium economy as an interconnected system with feedback loops.")
    ],
    "cast_items": [
        "Model the feedback loops connecting EV adoption, lithium demand, mining capacity, and environmental impact",
        "Analyze how recycling infrastructure and battery technology improvements can shift supply-demand dynamics",
        "Evaluate the trade-offs between accelerating green energy adoption and sustainable resource extraction"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Global EV sales triple over five years while lithium mining capacity increases by only 40%. Based on your model, which outcome is MOST likely?"),
        ("Constructed Response:", "Using your model, explain why simply opening more lithium mines is not a sustainable long-term solution to the supply crisis. Reference at least three model components and their interactions in your explanation.")
    ],
    "background_intro": "Lithium — element number 3, the lightest metal on the periodic table — has become the most strategically important mineral of the 21st century. Every electric vehicle battery, grid-scale energy storage system, and smartphone depends on it. As the world races to decarbonize transportation, the demand for lithium is skyrocketing while supply chains buckle under the pressure.",
    "background_sections": [
        ("Why Lithium? The Atomic Advantage", "Lithium's dominance in batteries comes from its atomic properties: it has the highest electrochemical potential of any element, the lowest atomic mass of any metal, and a small ionic radius that allows lithium ions to move quickly through electrode materials. These properties produce batteries with unmatched energy density — storing more energy per kilogram than any competing chemistry. A single EV battery contains 8-12 kg of lithium, and global EV sales are projected to reach 40 million per year by 2030."),
        ("The Extraction Problem", "About 60% of the world's lithium comes from brine deposits in the 'Lithium Triangle' of Chile, Argentina, and Bolivia. Brine extraction pumps underground saltwater into massive evaporation ponds where the sun concentrates lithium over 12-18 months. This process consumes approximately 2.2 million liters of water per ton of lithium — in some of the driest places on Earth. In Chile's Atacama Desert, lithium mining consumes 65% of the region's water, devastating indigenous farming communities and fragile ecosystems. Hard-rock mining in Australia is faster but generates significant toxic waste."),
        ("The Price Rollercoaster", "Lithium markets are extraordinarily volatile because supply is inelastic — new mines take 7-10 years from discovery to production. When Tesla and other manufacturers announced massive EV expansion plans, lithium carbonate prices surged from $6,000/ton in early 2021 to $80,000/ton in late 2022. When demand growth briefly paused, prices crashed back to $12,000/ton by 2024. This volatility makes long-term planning nearly impossible for both miners and manufacturers."),
        ("The Recycling Imperative", "Currently, less than 5% of lithium-ion batteries are recycled. Most end up in landfills, leaching toxic materials into soil and groundwater. But recycled lithium requires 90% less water and produces 75% less CO2 than newly mined lithium. Companies like Redwood Materials and Li-Cycle are building facilities that can recover 95% of lithium from spent batteries. The challenge is building recycling capacity fast enough — the first massive wave of EV batteries will reach end-of-life around 2030-2035.")
    ],
    "lever_L": "Students identify seven components of the lithium economy system: Lithium Demand, Mining Rate, Environmental Damage, Battery Performance, Recycling Rate, Market Price, and EV Adoption — distinguishing external drivers from internal system responses.",
    "lever_E": "Students determine that EV Adoption drives Lithium Demand, which outpaces Mining Rate, causing Market Price spikes. Mining Rate increases Environmental Damage. High Market Price incentivizes Recycling Rate investment. Better Battery Performance reduces Lithium Demand per vehicle.",
    "lever_V": "Students build a computational model showing the interconnected feedback loops of the lithium supply chain, visualizing how shocks propagate through the system.",
    "lever_Ev": "Students run steady growth, EV boom without recycling, and circular economy scenarios to identify which strategies resolve the supply-demand-environment trilemma.",
    "lever_R": "Students add Geopolitical Risk, Alternative Chemistry, or Water Scarcity Index to explore more realistic supply chain dynamics and vulnerability analysis.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic juxtaposition of lithium mine and electric vehicle", "say": "This metal costs more than some people's rent per gram. It powers every EV, every phone, every laptop. And we're running out of easy ways to get it.", "do": "Show lithium price chart from 2020-2025. Let the volatility speak for itself. Ask: What could cause a price to swing this wildly?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary terms", "say": "Today you're modeling one of the most important supply chain crises of your generation — the race for lithium.", "do": "Have students read objectives. Pre-teach 'critical mineral' and 'circular economy.' Quick-write: Name three things that use lithium batteries.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why is lithium the new gold?", "say": "Gold is valuable because it's rare and beautiful. Lithium is valuable because without it, the entire green energy transition stops. Which matters more?", "do": "Poll: How many devices with lithium batteries are in this room right now? Count them. Multiply by the lithium content.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're building a model of an entire global supply chain — from mines in Chile to car dealerships in America.", "do": "Preview each LEVER step. Emphasize that this is a system with feedback loops, not a simple supply-demand line.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Seven component cards for lithium economy model", "say": "Seven moving parts in this system. Some you can control with policy, some respond to the market. Which is which?", "do": "Guide sorting of external vs. internal components. Discuss why Recycling Rate and EV Adoption are external (policy-driven) while others respond to system dynamics.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between all seven components", "say": "When EV sales double, what chain reaction ripples through the entire lithium economy? Trace it.", "do": "Help students map feedback loops. Identify the key tension: EV Adoption drives demand but Mining Rate can't keep up. Find the stabilizing role of Recycling Rate.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and simulation results for three scenarios", "say": "Let's crash-test the lithium economy. What happens if everyone buys an EV but nobody recycles the batteries?", "do": "Students predict outcomes first, then run all three scenarios. Compare the circular economy scenario to the boom-without-recycling scenario.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model exploration", "say": "The green energy transition has a dirty secret — and your model just exposed it. But it also found the solution.", "do": "Lead discussion on the paradox of mining for sustainability. Connect to real-world lithium recycling companies and policy proposals.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Lithium supply chain resilience plan design challenge", "say": "An EV company just hired your team. You have 20 years and a billion-dollar budget. Design a lithium strategy that doesn't destroy the planet.", "do": "Groups design comprehensive supply strategies balancing cost, environment, and security. Present to class as board proposals.", "time": "12 min"}
    ],
    "sort_reasoning": "Recycling Rate and EV Adoption are external components because they are primarily driven by policy decisions, government mandates, consumer behavior, and investment choices that exist outside the natural lithium market system. Lithium Demand, Mining Rate, Environmental Damage, Battery Performance, and Market Price are internal because they respond to and are shaped by the interactions within the supply chain system itself.",
    "relationships": [
        ("EV Adoption to Lithium Demand", "POSITIVE (+)", "Higher EV Adoption directly increases Lithium Demand because each electric vehicle requires 8-12 kg of lithium for its battery pack. As more consumers switch from gasoline to electric, total lithium consumption scales proportionally."),
        ("Lithium Demand to Market Price", "POSITIVE (+)", "When Lithium Demand exceeds Mining Rate capacity, Market Price rises sharply due to competition for scarce supply. Because lithium supply is inelastic in the short term, even modest demand increases can cause dramatic price spikes."),
        ("Mining Rate to Environmental Damage", "POSITIVE (+)", "Higher Mining Rate directly increases Environmental Damage through greater water consumption in brine extraction, more toxic waste from hard-rock processing, expanded habitat destruction, and increased displacement of indigenous communities near mining sites.")
    ],
    "sim_answers": [
        ("Steady Growth Scenario", "With moderate EV Adoption growth and current Mining Rate, Lithium Demand gradually outpaces supply over the decade. Market Price increases steadily, making EVs more expensive and slightly slowing adoption — a weak negative feedback loop. Environmental Damage accumulates as mines expand. Without significant Recycling Rate improvement, the system reaches a supply crisis around year 7-8."),
        ("Circular Economy Scenario", "With Recycling Rate at 90% and moderate EV Adoption, the system transforms dramatically. Recycled lithium supplements mined lithium, reducing pressure on Mining Rate and slowing Environmental Damage accumulation. Market Price stabilizes because recycled material acts as a price ceiling. The system reaches a sustainable equilibrium where most lithium circulates in a closed loop.")
    ],
    "reflection_exemplars": [
        ("What is the lithium paradox?", "The model reveals a fundamental tension: solving climate change through EVs requires massive lithium extraction that damages ecosystems and water supplies. Fighting one environmental crisis creates another. The paradox is that the 'green' transition depends on environmentally destructive mining. The model shows this isn't unsolvable — high recycling rates and improved battery chemistry can break the paradox — but only if we invest in circular economy infrastructure before the first wave of EV batteries reaches end-of-life."),
        ("Why can't we just mine more lithium?", "The model demonstrates that Mining Rate is constrained by geological reality and development timelines. New mines take 7-10 years from discovery to production. Even if we started today, supply cannot match projected demand growth of 25-35% annually. Furthermore, every increase in Mining Rate directly increases Environmental Damage. The model shows that mining alone cannot solve the supply crisis — it must be combined with recycling and battery chemistry improvements to create a sustainable system.")
    ],
    "stem_intro": "Present the challenge: A major EV manufacturer needs 10x its current lithium supply within eight years. Your team will design a comprehensive 20-year supply strategy that balances cost, environmental responsibility, and supply security — using your model data to justify every decision.",
    "stem_concepts": [
        ("Supply Chain Resilience", "Robust supply chains diversify sources, maintain buffer stocks, and build redundancy. For lithium, this means not depending on a single country, single extraction method, or single battery chemistry. Resilience requires investing in alternatives before a crisis forces you to."),
        ("Life Cycle Analysis", "Evaluating the total environmental impact of a product from raw material extraction through manufacturing, use, and end-of-life. For lithium batteries, this reveals that mining and processing account for 30-50% of the total carbon footprint."),
        ("Circular Economy Design", "Designing products for disassembly and material recovery from the start. Battery packs designed for recycling can recover 95% of lithium, cobalt, and nickel — turning waste streams into supply streams.")
    ],
    "stem_eval": [
        ("Expert (4)", "Strategy integrates multiple lithium sources, includes recycling infrastructure timeline, hedges against price volatility, addresses environmental justice concerns, and uses model data to justify all projections"),
        ("Proficient (3)", "Strategy addresses supply diversification and recycling with reasonable timelines and uses some model evidence"),
        ("Developing (2)", "Strategy mentions multiple supply approaches but lacks detailed timeline, cost analysis, or model-based justification"),
        ("Beginning (1)", "Strategy is incomplete or relies on a single supply approach without considering system-level interactions")
    ],
    "support": [
        "Provide a simplified global map showing lithium deposits, mining operations, and EV manufacturing centers",
        "Use a timeline graphic showing the 7-10 year mine development cycle alongside the 2-3 year recycling facility development cycle",
        "Sentence frames: 'When EV Adoption increases, the demand for lithium __, which causes Market Price to __ because __'"
    ],
    "extensions": [
        "Research the Lithium Triangle (Chile, Argentina, Bolivia) and analyze how indigenous communities are affected by lithium extraction in the Atacama Desert",
        "Investigate sodium-ion battery technology and model how its commercialization would change global lithium demand projections",
        "Compare the environmental footprint of lithium mining to oil extraction and analyze which causes more damage per unit of transportation energy"
    ],
    "cross_curr": [
        ("Math", "Calculate the total lithium demand for projected global EV sales through 2040 and compare it to known reserves and current recycling capacity"),
        ("ELA", "Write a policy brief recommending lithium supply chain regulations, using model data as evidence for proposed mandates"),
        ("Social Studies", "Research the geopolitical implications of lithium concentration in a few countries and compare to historical resource conflicts over oil")
    ],
    "misconceptions": [
        ("Electric vehicles are completely green", "While EVs produce zero tailpipe emissions, their environmental impact depends heavily on how battery materials are sourced. Lithium mining consumes millions of liters of water in arid regions, generates toxic waste, and displaces communities. The full life cycle analysis shows EVs are still significantly cleaner than gasoline cars, but they are not zero-impact.", "Compare: Calculate the total CO2 and water footprint of manufacturing an EV battery versus the lifetime emissions of a gasoline car. EVs win, but the margin depends on mining practices."),
        ("We'll run out of lithium soon", "Global lithium reserves are actually substantial — an estimated 98 million tons. The problem isn't total supply but extraction rate. Current mining capacity cannot scale fast enough to meet projected demand. It's a flow problem, not a stock problem. New deposits are still being discovered, and ocean water contains 230 billion tons of lithium — the challenge is extracting it economically.", "Analogy: Imagine a water tank with a million gallons but only a garden hose to drain it. You don't have a water shortage — you have a flow rate shortage."),
        ("Recycling batteries is too expensive to be practical", "Early lithium-ion recycling was indeed uneconomical when lithium was cheap. But with prices now 5-10x higher than a decade ago and improving recycling technology, recovered lithium is increasingly cost-competitive with mined lithium. Recycling also avoids the 7-10 year development timeline of new mines and produces 75% less CO2 than primary extraction.", "Show the cost curves: Plot lithium mining cost vs. recycling cost over the past decade. The crossover point where recycling becomes cheaper has already been reached for many operations.")
    ]
}

L02 = {
    "id": "G10L2-L02",
    "title": "How Do Stars Forge Every Atom in Your Body?",
    "subtitle": "Modeling Stellar Nucleosynthesis and the Origin of the Elements",
    "ngss": "HS-ESS1-3, HS-PS1-5",
    "ngss_desc": "Communicate scientific ideas about the way stars, over their life cycle, produce elements. Use mathematical representations to support the claim that atoms, and therefore mass, are conserved during a chemical reaction.",
    "big_question": "Every atom in your body was forged inside a star that exploded before our Sun was born — how did stars create the entire periodic table?",
    "objectives": [
        "Model how stellar core temperature and gravitational pressure drive nuclear fusion through successive element-building stages",
        "Explain why stars produce elements in a specific sequence determined by nuclear binding energy",
        "Predict how a star's mass determines which elements it can produce and how it ultimately dies",
        "Analyze how the balance between gravitational pressure and radiation output determines a star's stability and lifecycle"
    ],
    "vocabulary": [
        ("Nucleosynthesis", "The process by which new atomic nuclei are created from pre-existing protons and neutrons — primarily occurring in stellar cores where temperatures exceed 10 million Kelvin"),
        ("Fusion", "A nuclear reaction in which lighter atomic nuclei combine to form a heavier nucleus, releasing enormous energy because the product has less mass than the sum of its parts — powering all main-sequence stars"),
        ("Binding Energy", "The energy required to disassemble a nucleus into its component protons and neutrons — iron-56 has the highest binding energy per nucleon, making it the endpoint of energy-releasing fusion"),
        ("Supernova", "The catastrophic explosion of a massive star when its core can no longer support itself against gravitational collapse, dispersing heavy elements into space and triggering the formation of new star systems")
    ],
    "components": [
        ("Stellar Core Temperature", "The temperature at the center of the star, which must reach specific thresholds to ignite each successive stage of nuclear fusion — from 10 million K for hydrogen to 3 billion K for silicon", False),
        ("Hydrogen Fusion Rate", "The rate at which hydrogen nuclei fuse into helium in the star's core, which determines the star's luminosity, lifespan, and the pace of chemical evolution", False),
        ("Helium Accumulation", "The buildup of helium ash in the stellar core from hydrogen fusion, which eventually triggers helium fusion when core temperature and pressure reach the ignition threshold", False),
        ("Gravitational Pressure", "The inward-directed force from the star's enormous mass compressing the core — the fundamental driver that heats the core and initiates each new fusion stage", True),
        ("Radiation Output", "The outward-directed energy pressure from nuclear fusion reactions that pushes against gravitational collapse, maintaining the star's structural stability", False),
        ("Element Production", "The sequential creation of progressively heavier elements through fusion — from helium through carbon, oxygen, neon, silicon, and ultimately iron in the most massive stars", False),
        ("Star Lifecycle Stage", "The current evolutionary phase of the star — main sequence, red giant, supergiant, or end state (white dwarf, neutron star, or black hole) — determined by fuel availability and mass", False)
    ],
    "think_about_it": "Gravitational Pressure constantly tries to crush the star while Radiation Output from fusion pushes outward. What happens when the core runs out of hydrogen? When helium runs out? When the star reaches iron — an element that absorbs energy instead of releasing it during fusion?",
    "scenarios": [
        ("Sun-Like Star Lifecycle", "Set Gravitational Pressure to moderate (1 solar mass) — observe the star's progression through hydrogen fusion, helium fusion, and its end as a white dwarf"),
        ("Massive Star to Supernova", "Set Gravitational Pressure to high (20 solar masses) — observe rapid progression through all fusion stages ending in iron core collapse and supernova"),
        ("Red Dwarf Longevity", "Set Gravitational Pressure to low (0.3 solar masses) — observe extremely slow Hydrogen Fusion Rate and trillion-year lifespan")
    ],
    "sim_scenarios": [
        ("Sun-Like Star", "Moderate mass, standard fusion", "What do you predict happens to Stellar Core Temperature when the hydrogen fuel is exhausted?"),
        ("Massive Star", "High mass, rapid burning", "What do you predict happens when Element Production reaches iron and fusion can no longer release energy?"),
        ("Red Dwarf", "Low mass, slow burning", "How does low Gravitational Pressure affect the star's Hydrogen Fusion Rate and total lifespan?")
    ],
    "discoveries": [
        "Stars are element factories — the balance between Gravitational Pressure and Radiation Output creates the conditions for nuclear fusion to forge progressively heavier elements",
        "Each fusion stage requires higher temperatures and produces heavier elements, but releases less energy — creating an inevitable countdown to fuel exhaustion",
        "Iron is the endpoint of energy-releasing fusion because its nucleus has the highest binding energy per nucleon — fusing iron absorbs energy instead of releasing it, triggering core collapse",
        "The elements in your body required at least two generations of stars — hydrogen and helium from the Big Bang, carbon and oxygen from medium stars, and iron and heavier elements from supernovae"
    ],
    "answer": "Every atom heavier than hydrogen and helium was forged inside a star through nucleosynthesis. Stars fuse hydrogen into helium for most of their lives, but when hydrogen runs out, gravitational pressure compresses the core until it's hot enough to fuse helium into carbon and oxygen. In massive stars, this process repeats — carbon fuses to neon, neon to oxygen, oxygen to silicon, silicon to iron. Iron is the dead end: fusing it absorbs energy instead of releasing it. When a massive star builds an iron core, it collapses in seconds and explodes as a supernova, scattering every element it created into space. Those elements became the gas cloud that formed our solar system — including every atom in your body.",
    "stem_title": "Design a Stellar Evolution Visualization Tool",
    "stem_mission": "Design an interactive visualization that shows how stars of different masses produce different elements and how those elements end up in planets and living organisms.",
    "stem_scenario": "A science museum is creating a new exhibit on the origin of elements. They need an interactive display that lets visitors select a star mass and watch the entire lifecycle unfold — from birth through element production to death. Your team has been hired to design this visualization using your model data.",
    "stem_questions": [
        "How will you visually represent the different timescales of each fusion stage?",
        "What interactive controls will visitors use to explore different star masses?",
        "How will you connect the abstract physics to the tangible reality that these elements are in visitors' bodies?"
    ],
    "stem_design_qs": [
        "What visual metaphor will make nuclear fusion intuitive for a general audience?",
        "How will you show the onion-layer structure of a massive star's core?",
        "What data from your simulations will drive the visualization's behavior?",
        "How will you handle the dramatic difference in timescales — billions of years of hydrogen burning versus seconds of core collapse?"
    ],
    "career": "Astrophysicists study the physical processes governing stars, galaxies, and the universe. They work at universities, NASA, national observatories, and research institutions, earning $70,000–$150,000/year. Nuclear Physicists who study fusion reactions earn $80,000–$170,000/year.",
    "images": {
        "cover": ("G10L2-L02-cover.png", "A photorealistic, cinematic image of a massive star in its final stages showing the onion-layer internal structure with different fusion zones glowing in distinct colors from hydrogen on the outside to iron at the core, set against a deep space background with nebula remnants"),
        "landscape": ("G10L2-L02-landscape.png", "A diverse group of 15-16 year old students in a modern physics lab examining spectroscopy equipment and stellar classification charts, fascinated expressions as they analyze light spectra, natural classroom lighting"),
        "modeling": ("G10L2-L02-modeling.png", "A diverse group of 15-16 year old students working on laptops building computational models of stellar evolution, screens showing temperature-luminosity diagrams and fusion chain graphics, modern classroom with space imagery"),
        "discussion": ("G10L2-L02-discussion.png", "A teacher leading an animated discussion with diverse 15-16 year old students about stellar nucleosynthesis, a Hertzsprung-Russell diagram and periodic table displayed on a smartboard, students raising hands enthusiastically"),
        "stem": ("G10L2-L02-stem.png", "Diverse 15-16 year old students designing interactive museum exhibit mockups for stellar evolution, prototypes with colorful diagrams and digital displays on their tables, creative collaborative atmosphere")
    },
    "pre_assessment": [
        "Where do you think the atoms in your body originally came from?",
        "What do you know about how stars produce energy?",
        "Draw a diagram showing what you think happens inside a star during its lifetime.",
        "Why do you think there are so many different elements on the periodic table instead of just one or two?"
    ],
    "extend_components": [
        ("Stellar Mass", "The total mass of the star, which is the master variable determining core temperature, fusion rate, element production capacity, lifespan, and ultimate fate"),
        ("Neutrino Emission", "The flood of nearly massless particles produced during fusion and especially during core collapse, which carry away energy and signal the star's internal state"),
        ("Metallicity", "The proportion of elements heavier than helium in the star's composition, inherited from previous stellar generations and affecting opacity, fusion rates, and stellar structure")
    ],
    "reflections": [
        "How does your model demonstrate that a star's mass determines its entire life story — from birth to death?",
        "Why is iron the 'dead end' of stellar fusion, and what does this mean for how elements heavier than iron are created?",
        "What does your model reveal about the timescales involved — why does hydrogen burning last billions of years while silicon burning lasts only days?",
        "How does the concept of hydrostatic equilibrium (gravitational pressure vs. radiation output) explain both stellar stability and stellar death?",
        "What are the limitations of modeling stellar evolution with only seven components when real stars involve magnetohydrodynamics, rotation, and mass loss?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model of stellar nucleosynthesis that connects nuclear physics to stellar evolution and element production across cosmic timescales."),
        ("Disciplinary Core Idea", "ESS1.A The Universe and Its Stars / PS1.C Nuclear Processes", "Stars produce elements through nuclear fusion in their cores, with the specific elements produced determined by stellar mass and lifecycle stage."),
        ("Crosscutting Concept", "Energy and Matter: Flows, Cycles, and Conservation", "Students trace matter transformation from primordial hydrogen through stellar nucleosynthesis to the heavy elements found in planets and living organisms.")
    ],
    "cast_items": [
        "Model how gravitational pressure and radiation output interact to drive nuclear fusion through successive element-building stages",
        "Explain why stellar mass determines element production capacity and ultimate stellar fate",
        "Trace the cosmic journey of elements from stellar cores to the atoms in the human body"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A star 25 times the mass of our Sun has built up an iron core after fusing successively heavier elements. What happens next, according to your model?"),
        ("Constructed Response:", "Using your model, explain why the calcium in your bones and the iron in your blood required different types of stars to produce. Reference the role of Gravitational Pressure and Stellar Core Temperature in your explanation.")
    ],
    "background_intro": "You are literally made of stardust — and that is not a metaphor. The calcium in your bones was forged in a supergiant star. The iron in your blood was the last element produced before a star collapsed and exploded. The oxygen you're breathing right now was fused from carbon in a stellar core at 600 million degrees. Understanding stellar nucleosynthesis is understanding the origin of everything.",
    "background_sections": [
        ("The Cosmic Origin of Elements", "After the Big Bang, the universe contained only hydrogen (~75%), helium (~25%), and trace amounts of lithium. Every other element on the periodic table was created later inside stars. This process — stellar nucleosynthesis — occurs when gravitational compression heats stellar cores to temperatures where atomic nuclei can overcome their electromagnetic repulsion and fuse. The energy released by fusion is what makes stars shine."),
        ("The Fusion Sequence", "Stars fuse elements in a specific order dictated by the energy required to overcome nuclear repulsion. Hydrogen fuses to helium at 10 million K (our Sun does this). Helium fuses to carbon at 100 million K. Carbon to neon at 600 million K. Neon to oxygen at 1.2 billion K. Oxygen to silicon at 1.5 billion K. Silicon to iron at 2.7 billion K. Each stage requires higher temperatures and produces less energy — a star that burns hydrogen for 10 million years may burn silicon for only one day."),
        ("The Iron Catastrophe", "Iron-56 has the highest binding energy per nucleon of any element. This means fusing iron into heavier elements does not release energy — it requires energy input. When a massive star accumulates an iron core of about 1.4 solar masses (the Chandrasekhar limit), fusion stops. In less than a second, the core collapses from the size of Earth to a sphere 20 km across. The resulting shockwave — a supernova — is briefly brighter than an entire galaxy and creates all elements heavier than iron through rapid neutron capture (the r-process)."),
        ("From Stardust to You", "The elements scattered by supernovae mix with interstellar gas and eventually collapse into new star systems — complete with planets. Our solar system formed 4.6 billion years ago from a cloud enriched by multiple generations of stellar deaths. The Earth's composition reflects this cosmic heritage: an iron core, a silicate mantle, a nitrogen-oxygen atmosphere, and carbon-based life. Every atom in your body has been inside at least one star, and the heaviest atoms required the most violent events in the universe to create.")
    ],
    "lever_L": "Students identify seven components of stellar nucleosynthesis: Stellar Core Temperature, Hydrogen Fusion Rate, Helium Accumulation, Gravitational Pressure, Radiation Output, Element Production, and Star Lifecycle Stage — with Gravitational Pressure as the external driver.",
    "lever_E": "Students determine that Gravitational Pressure drives Stellar Core Temperature, which enables Hydrogen Fusion Rate. Fusion produces Radiation Output (opposing gravity) and Helium Accumulation (fuel for the next stage). Element Production advances as each fuel is exhausted.",
    "lever_V": "Students build a computational model showing the balance between gravitational collapse and radiation pressure, and how fuel exhaustion drives transitions between lifecycle stages.",
    "lever_Ev": "Students run sun-like, massive star, and red dwarf scenarios to compare element production capacity, lifecycle duration, and end states across different stellar masses.",
    "lever_R": "Students add Stellar Mass, Neutrino Emission, or Metallicity to explore how initial conditions and energy loss mechanisms affect stellar evolution pathways.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic stellar interior cross-section", "say": "Hold up your hand. The iron in your blood was forged in a star that exploded before our Sun existed. The calcium in your bones came from a different star. You are made of dead stars.", "do": "Let the statement land. Show the periodic table with elements color-coded by their stellar origin. Give students 30 seconds to process.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary terms", "say": "Today you're modeling the most powerful factories in the universe — stellar cores where atoms are literally built from scratch.", "do": "Have students read objectives. Pre-teach 'nucleosynthesis' and 'binding energy.' Quick-write: What do you think powers a star?", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How do stars forge every atom in your body?", "say": "The Big Bang made hydrogen and helium. That's it. So where did the other 90+ elements come from?", "do": "Students examine a periodic table and identify which elements are in the human body. Challenge: Where did each one originate?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're going to model the entire life of a star — from its birth burning hydrogen to its death creating the heaviest elements.", "do": "Preview each LEVER step. Emphasize that stellar mass is the master variable that determines everything.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Seven component cards for stellar nucleosynthesis model", "say": "A star is a battleground between two forces: gravity trying to crush it and radiation trying to blow it apart. Everything else follows from that battle.", "do": "Guide component sorting. Discuss why Gravitational Pressure is external (set by the star's mass at birth) while other components respond to it.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between stellar components", "say": "When hydrogen runs out, what happens to the balance between gravity and radiation? That moment determines everything.", "do": "Help students trace the feedback loop: gravity compresses, temperature rises, fusion ignites, radiation pushes back. Identify what breaks this balance.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and simulation results for three star masses", "say": "Let's watch three different stars live and die. A star like our Sun. A monster 20 times larger. And a tiny red dwarf.", "do": "Students predict element production and lifespan for each mass. Run simulations. Compare the dramatically different outcomes.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings about stellar element production", "say": "Your body is a periodic table of stellar debris. Different elements required different stars, different temperatures, and different deaths.", "do": "Create a class 'element origin map' connecting body elements to their stellar sources. Discuss why supernovae are essential for life.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Museum exhibit visualization design challenge", "say": "A science museum wants visitors to truly understand that they are made of stars. Design the exhibit that makes it real.", "do": "Groups design interactive stellar evolution visualizations. Must show mass-dependent outcomes and connect to human body composition.", "time": "12 min"}
    ],
    "sort_reasoning": "Gravitational Pressure is the external component because it is determined by the star's total mass, which is set at the star's formation and acts as the primary driver of all internal processes. Stellar Core Temperature, Hydrogen Fusion Rate, Helium Accumulation, Radiation Output, Element Production, and Star Lifecycle Stage are all internal components because they respond to and are determined by the gravitational compression and the chain of nuclear fusion reactions it drives.",
    "relationships": [
        ("Gravitational Pressure to Stellar Core Temperature", "POSITIVE (+)", "Greater Gravitational Pressure compresses the core more intensely, converting gravitational potential energy to thermal energy and raising core temperature to the thresholds required for each successive fusion stage."),
        ("Stellar Core Temperature to Hydrogen Fusion Rate", "POSITIVE (+)", "Higher core temperature dramatically increases the rate of hydrogen fusion because nuclear fusion probability depends exponentially on temperature — even small temperature increases produce large increases in reaction rates through quantum tunneling."),
        ("Hydrogen Fusion Rate to Radiation Output", "POSITIVE (+)", "Faster hydrogen fusion releases more energy per second as gamma rays and neutrinos, increasing the outward Radiation Output that supports the star against gravitational collapse.")
    ],
    "sim_answers": [
        ("Sun-Like Star Scenario", "With moderate Gravitational Pressure, Stellar Core Temperature reaches 15 million K — sufficient for hydrogen fusion but not much beyond helium. Hydrogen Fusion Rate is steady for approximately 10 billion years. When hydrogen is exhausted, Helium Accumulation triggers helium fusion at 100 million K, producing carbon and oxygen. The star swells into a red giant, then sheds its outer layers as a planetary nebula, leaving a white dwarf. Element Production stops at carbon and oxygen."),
        ("Massive Star Scenario", "With high Gravitational Pressure (20 solar masses), Stellar Core Temperature rapidly climbs through all fusion thresholds. The star races through hydrogen fusion in just 10 million years, then progresses through helium, carbon, neon, oxygen, and silicon fusion in progressively shorter intervals. Element Production reaches iron in the final days. When the iron core exceeds the Chandrasekhar limit, Radiation Output drops to zero, gravitational collapse occurs in milliseconds, and the supernova explosion creates all elements heavier than iron.")
    ],
    "reflection_exemplars": [
        ("Why is iron the dead end of fusion?", "Iron-56 has the highest binding energy per nucleon on the binding energy curve. All elements lighter than iron release energy when they fuse because the products are more tightly bound. All elements heavier than iron require energy input to fuse because the products are less tightly bound. When a massive star builds an iron core, fusion can no longer generate the Radiation Output needed to support the star against Gravitational Pressure. The balance breaks, and the star collapses in less than a second."),
        ("Why do different elements require different stars?", "The model shows that Stellar Core Temperature must reach specific thresholds for each fusion stage, and only stars with sufficient Gravitational Pressure can achieve these temperatures. Our Sun can only reach ~100 million K — enough for hydrogen and helium fusion, producing carbon and oxygen. A 20-solar-mass star reaches 3 billion K, producing everything up to iron. Elements heavier than iron require the extreme conditions of a supernova explosion. This is why your body's composition required multiple generations of stars with different masses.")
    ],
    "stem_intro": "Present the challenge: A science museum needs an interactive exhibit that shows visitors how stellar nucleosynthesis created every element in their bodies. Your team will design a visualization that makes abstract nuclear physics tangible and connects the cosmic scale to the personal scale.",
    "stem_concepts": [
        ("Hertzsprung-Russell Diagram", "A plot of stellar luminosity versus surface temperature that reveals the life tracks of stars. Main sequence stars fuse hydrogen; red giants have exhausted core hydrogen; supergiants are approaching their final fusion stages. The diagram is astrophysics' most powerful classification tool."),
        ("Nuclear Binding Energy Curve", "A graph of binding energy per nucleon versus atomic mass number that explains why fusion releases energy for light elements and fission releases energy for heavy elements. Iron sits at the peak — the most stable nucleus and the endpoint of energy-releasing fusion."),
        ("Cosmic Elemental Abundances", "The relative amounts of each element in the universe follow a predictable pattern determined by nucleosynthesis processes: hydrogen and helium dominate, with peaks at carbon, oxygen, and iron reflecting the most energetically favorable fusion products.")
    ],
    "stem_eval": [
        ("Expert (4)", "Visualization accurately represents mass-dependent stellar evolution, shows all fusion stages with correct timescales, connects element production to human body composition, and provides intuitive interactive controls"),
        ("Proficient (3)", "Visualization shows stellar lifecycle stages and element production with reasonable accuracy and some interactive elements"),
        ("Developing (2)", "Visualization includes some stellar evolution concepts but timescales or element production sequences contain inaccuracies"),
        ("Beginning (1)", "Visualization is incomplete or contains fundamental misconceptions about stellar physics")
    ],
    "support": [
        "Provide a simplified binding energy curve showing why iron is the fusion endpoint",
        "Use a layered diagram (like an onion) to show the different fusion shells in a massive star's core",
        "Sentence frames: 'When Gravitational Pressure increases, Stellar Core Temperature __, which causes __ to fuse into __ because __'"
    ],
    "extensions": [
        "Research the r-process and s-process of neutron capture that create elements heavier than iron, and explain why gold requires a neutron star merger",
        "Investigate the solar neutrino problem and how its resolution confirmed our model of stellar fusion",
        "Compare Population III stars (the first stars, made only of hydrogen and helium) to modern stars and explain how metallicity affects stellar evolution"
    ],
    "cross_curr": [
        ("Math", "Use the mass-luminosity relation (L proportional to M^3.5) to calculate how stellar mass affects luminosity and lifespan, and graph the results"),
        ("ELA", "Write a creative narrative from the perspective of a carbon atom, tracing its journey from stellar core to human cell over billions of years"),
        ("History", "Research the history of spectroscopy and how Cecilia Payne-Gaposchkin's discovery that stars are mostly hydrogen revolutionized astronomy")
    ],
    "misconceptions": [
        ("Stars burn like fires", "Stars do not undergo chemical combustion (burning). They produce energy through nuclear fusion — combining atomic nuclei at temperatures of millions of degrees. Chemical burning involves electron interactions and produces thousands of degrees; nuclear fusion involves nuclear forces and produces millions to billions of degrees. The energy output per kilogram of fuel is roughly 10 million times greater for fusion than for combustion.", "Calculate: How long would the Sun last if it were actually burning hydrogen as a chemical fuel? (Answer: about 10,000 years, not 10 billion.)"),
        ("The Sun will explode as a supernova", "Only stars roughly 8 or more times the mass of the Sun have enough gravitational pressure to progress through all fusion stages to iron core collapse. Our Sun will exhaust its hydrogen, swell into a red giant, fuse helium into carbon and oxygen, then gently shed its outer layers as a planetary nebula — leaving behind a white dwarf the size of Earth. No explosion, no supernova.", "Show the Hertzsprung-Russell diagram and trace the evolutionary paths of different-mass stars. Our Sun's path leads to the white dwarf graveyard, not the supernova explosion."),
        ("Heavy elements are made during normal stellar fusion", "Normal stellar fusion can only produce elements up to iron (atomic number 26). All elements heavier than iron — including copper, silver, gold, uranium — require the extreme neutron flux of a supernova explosion or neutron star merger. These events produce enormous numbers of free neutrons that are rapidly captured by nuclei, building up to the heaviest elements in seconds.", "Challenge: Gold (atomic number 79) exists on Earth. No star can fuse elements past iron. So where did the gold come from? (Answer: A neutron star merger or supernova that occurred before our solar system formed.)")
    ]
}

L03 = {
    "id": "G10L2-L03",
    "title": "The Carbon Bomb: Why Thawing Permafrost Terrifies Scientists",
    "subtitle": "Modeling Arctic Feedback Loops and Climate Tipping Points",
    "ngss": "HS-ESS2-6, HS-LS2-3",
    "ngss_desc": "Develop a quantitative model to describe the cycling of carbon among the hydrosphere, atmosphere, geosphere, and biosphere. Construct and revise an explanation based on evidence for the cycling of matter and flow of energy in aerobic and anaerobic conditions.",
    "big_question": "There is twice as much carbon frozen in permafrost as exists in the entire atmosphere — what happens when it thaws?",
    "objectives": [
        "Model how rising permafrost temperatures trigger a cascade of methane release, microbial decomposition, and atmospheric carbon amplification",
        "Analyze the feedback loop where thawing permafrost releases greenhouse gases that cause more warming that thaws more permafrost",
        "Predict the conditions under which the permafrost carbon feedback becomes a self-sustaining process beyond human control",
        "Evaluate how ocean absorption and vegetation growth act as partial carbon sinks that slow but cannot stop the feedback amplification"
    ],
    "vocabulary": [
        ("Permafrost", "Ground that remains frozen for at least two consecutive years — covering 25% of the Northern Hemisphere's land surface and storing an estimated 1,500 billion tons of organic carbon from thousands of years of accumulated dead plant and animal material"),
        ("Positive Feedback Loop", "A self-amplifying cycle where the output of a process reinforces its own input — in this case, warming thaws permafrost, releasing greenhouse gases that cause more warming, which thaws more permafrost"),
        ("Methane Clathrate", "Methane gas trapped in ice-like crystal structures within frozen ground and ocean sediments — methane is 80 times more potent than CO2 as a greenhouse gas over a 20-year period"),
        ("Tipping Point", "A critical threshold beyond which a system shifts rapidly and irreversibly to a new state — for permafrost, the point at which carbon release becomes self-sustaining even if human emissions stop completely")
    ],
    "components": [
        ("Permafrost Temperature", "The temperature of permanently frozen ground, which is warming at twice the rate of the global average — thawing begins when ground temperature exceeds 0 degrees Celsius", False),
        ("Methane Release Rate", "The volume of methane escaping from thawing permafrost through thermokarst lakes, wetlands, and subsea sediments — methane is 80x more potent than CO2 over 20 years", False),
        ("Microbial Decomposition", "The activity of soil microorganisms that awaken from dormancy when permafrost thaws, consuming ancient organic carbon and producing CO2 and methane as metabolic byproducts", False),
        ("Atmospheric CO2", "The total concentration of carbon dioxide in the Earth's atmosphere, currently at 420+ ppm — driven by both human emissions and natural sources including permafrost thaw", True),
        ("Ocean Absorption", "The rate at which oceans absorb CO2 from the atmosphere through dissolution and biological uptake — currently absorbing about 25% of human emissions but capacity is declining", False),
        ("Vegetation Growth", "The expansion of plant life into newly thawed Arctic regions, which absorbs some CO2 through photosynthesis but cannot offset the massive carbon release from decomposing permafrost", False),
        ("Feedback Amplification", "The net acceleration of warming caused by permafrost carbon release reinforcing the original warming signal — the key metric that determines whether the system passes the tipping point", False)
    ],
    "think_about_it": "Atmospheric CO2 raises global temperature, which increases Permafrost Temperature, which releases methane and CO2 from Microbial Decomposition — which raises Atmospheric CO2 further. Ocean Absorption and Vegetation Growth slow this cycle but cannot stop it. At what point does Feedback Amplification become self-sustaining?",
    "scenarios": [
        ("Current Trajectory", "Set Atmospheric CO2 at current levels with continued growth — observe Permafrost Temperature rise and the feedback cascade over 50 years"),
        ("Aggressive Emissions Cuts", "Reduce Atmospheric CO2 growth rate to near zero — observe whether the permafrost feedback has already passed the tipping point"),
        ("Methane Burst Event", "Simulate a rapid Methane Release Rate spike from thermokarst lake collapse — observe how a sudden pulse propagates through the feedback system")
    ],
    "sim_scenarios": [
        ("Current Trajectory", "Rising atmospheric CO2, continued warming", "What do you predict happens to Feedback Amplification over the next 50 years if emissions continue at current rates?"),
        ("Aggressive Cuts", "Near-zero emissions growth", "Do you predict that stopping human emissions will also stop the permafrost feedback — or has it already become self-sustaining?"),
        ("Methane Burst", "Sudden large-scale methane release", "What do you predict happens to Atmospheric CO2 and Permafrost Temperature after a sudden methane burst from thermokarst collapse?")
    ],
    "discoveries": [
        "The permafrost carbon feedback is a positive feedback loop — thawing releases greenhouse gases that cause more warming that causes more thawing, creating a self-amplifying cycle",
        "Ocean Absorption and Vegetation Growth provide negative feedback that slows the cycle, but the carbon being released from permafrost vastly exceeds what these sinks can absorb",
        "The system has a tipping point beyond which the feedback becomes self-sustaining — meaning permafrost carbon release would continue even if all human emissions stopped immediately",
        "The 1,500 billion tons of carbon in permafrost is a legacy of tens of thousands of years of organic accumulation — its release over decades rather than millennia would overwhelm Earth's carbon cycle"
    ],
    "answer": "Permafrost contains approximately 1,500 billion tons of carbon — nearly twice the amount currently in the entire atmosphere. As Arctic temperatures rise at twice the global average, this ancient frozen ground is thawing. When permafrost thaws, dormant microorganisms reawaken and begin decomposing thousands of years of accumulated organic material, releasing CO2 and methane into the atmosphere. This creates a terrifying positive feedback loop: more greenhouse gases cause more warming, which thaws more permafrost, which releases more greenhouse gases. Scientists are terrified because this feedback may have a tipping point beyond which it becomes self-sustaining — a 'carbon bomb' that would continue detonating even if humanity eliminated all its own emissions overnight.",
    "stem_title": "Design an Arctic Permafrost Monitoring Network",
    "stem_mission": "Design a monitoring system that tracks permafrost thaw rates across the Arctic and provides early warning when the carbon feedback approaches tipping point conditions.",
    "stem_scenario": "The International Arctic Research Council needs a comprehensive monitoring network to detect whether permafrost carbon release is approaching the self-sustaining tipping point. Your team has been hired to design the sensor network, data analysis system, and warning threshold criteria.",
    "stem_questions": [
        "What measurements would provide the earliest warning that the feedback loop is accelerating?",
        "How would you distinguish between seasonal permafrost thaw and irreversible deep thaw?",
        "What geographic coverage would your monitoring network need to provide representative Arctic-wide data?"
    ],
    "stem_design_qs": [
        "What types of sensors would you deploy — ground temperature, methane flux, soil moisture, satellite thermal imaging?",
        "How would you power and maintain monitoring stations in extremely remote Arctic locations?",
        "What data analysis algorithms would detect the transition from linear thaw to exponential feedback?",
        "How would you communicate tipping point warnings to policymakers in time for action?"
    ],
    "career": "Climate Scientists study Earth's climate systems including feedback loops, tipping points, and carbon cycles. They work at NOAA, NASA, universities, and international research organizations, earning $70,000–$140,000/year. Permafrost Researchers who specialize in Arctic carbon dynamics earn $65,000–$130,000/year.",
    "images": {
        "cover": ("G10L2-L03-cover.png", "A photorealistic, cinematic aerial image of thawing permafrost in the Arctic tundra showing thermokarst lakes forming as ground collapses, methane bubbles visible in turquoise water, the crumbling permafrost edge exposing layers of ancient frozen soil, dramatic Arctic lighting with low sun angle"),
        "landscape": ("G10L2-L03-landscape.png", "A diverse group of 15-16 year old students in a modern earth science lab examining permafrost core samples and studying climate data on monitors, Arctic landscape images on the walls, engaged and concerned expressions, natural classroom lighting"),
        "modeling": ("G10L2-L03-modeling.png", "A diverse group of 15-16 year old students working on laptops building computational models of Arctic carbon feedback loops, screens showing temperature curves and methane flux graphs, modern classroom with climate data displays"),
        "discussion": ("G10L2-L03-discussion.png", "A teacher leading an intense discussion with diverse 15-16 year old students about climate feedback loops, a diagram of the permafrost carbon cycle displayed on a smartboard with positive and negative feedback arrows, students deeply engaged"),
        "stem": ("G10L2-L03-stem.png", "Diverse 15-16 year old students designing Arctic monitoring network proposals with maps and sensor diagrams on large displays, collaborative atmosphere with technical drawings and data visualizations")
    },
    "pre_assessment": [
        "What do you think permafrost is and why might scientists be worried about it thawing?",
        "What do you know about feedback loops — can you think of an example where a process speeds itself up?",
        "Draw a diagram showing how you think carbon moves between the ground, the atmosphere, and the ocean.",
        "What is a tipping point and why might one exist in the climate system?"
    ],
    "extend_components": [
        ("Thermokarst Formation", "The collapse of ground surface as ice-rich permafrost thaws, creating lakes and wetlands that accelerate further thawing and become concentrated methane emission sources"),
        ("Subsea Permafrost", "Frozen ground beneath the Arctic Ocean floor that formed during ice ages when sea levels were lower — now warming from both above (warmer ocean) and below (geothermal heat), potentially releasing enormous methane stores"),
        ("Albedo Change", "The shift in surface reflectivity as white snow and ice are replaced by dark water and vegetation in thawing regions, causing the surface to absorb more solar energy and accelerating local warming")
    ],
    "reflections": [
        "How does your model demonstrate the difference between a positive feedback loop and a negative feedback loop in the climate system?",
        "Why can't Ocean Absorption and Vegetation Growth fully compensate for the carbon released from thawing permafrost?",
        "What does your model suggest about whether the permafrost tipping point has already been passed or can still be avoided?",
        "How does the timescale mismatch — carbon accumulated over tens of thousands of years being released over decades — create the crisis?",
        "What are the limitations of modeling a global climate feedback with only seven components when the real system involves ocean circulation, cloud dynamics, and ice sheet behavior?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a quantitative computational model of the permafrost carbon feedback loop, testing scenarios to identify tipping point conditions."),
        ("Disciplinary Core Idea", "ESS2.D Weather and Climate / LS2.B Cycles of Matter and Energy Transfer", "Carbon cycles between the atmosphere, geosphere, and biosphere through processes including decomposition, absorption, and photosynthesis, with feedback loops that can amplify or dampen changes."),
        ("Crosscutting Concept", "Stability and Change", "Students model how a stable system (frozen permafrost storing carbon for millennia) can be pushed past a tipping point into a new, self-reinforcing state of change.")
    ],
    "cast_items": [
        "Model the positive feedback loop between permafrost thawing, greenhouse gas release, and atmospheric warming",
        "Analyze how carbon sinks (ocean absorption, vegetation growth) interact with carbon sources (microbial decomposition, methane release) to determine net feedback",
        "Predict tipping point conditions using computational model evidence"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Arctic temperatures have risen 3 degrees Celsius above pre-industrial levels. Based on your model, which feedback component would show the most dramatic change first?"),
        ("Constructed Response:", "Using your model, explain why the permafrost carbon feedback is described as a 'carbon bomb' and why scientists fear it could make climate change irreversible even if all human emissions stopped. Reference at least three model components.")
    ],
    "background_intro": "Beneath the frozen ground of Siberia, Alaska, and northern Canada lies a carbon time bomb that dwarfs all human emissions combined. Permafrost — ground frozen continuously for at least two years, some of it for hundreds of thousands of years — stores approximately 1,500 billion tons of organic carbon. That's nearly twice the carbon in the entire atmosphere. As the Arctic warms at twice the global rate, this ancient carbon is beginning to thaw.",
    "background_sections": [
        ("What Is Permafrost?", "Permafrost is ground that remains at or below 0 degrees Celsius for at least two consecutive years. It covers approximately 25% of the Northern Hemisphere's land surface — an area larger than all of North and South America combined. Some permafrost in Siberia has been frozen for 700,000 years. During all that time, dead plants and animals accumulated in the frozen soil without decomposing, creating an enormous reservoir of organic carbon trapped in a natural freezer."),
        ("The Thaw Cascade", "When permafrost thaws, several interconnected processes begin simultaneously. Soil microorganisms that have been dormant for millennia reactivate and begin decomposing the ancient organic material, producing CO2 in aerobic (oxygen-rich) conditions and methane in anaerobic (oxygen-poor) conditions. Methane is 80 times more potent than CO2 as a greenhouse gas over 20 years. The ground physically collapses as ice lenses melt, creating thermokarst lakes that accelerate further thawing. These lakes become concentrated sources of methane that bubbles visibly to the surface."),
        ("The Feedback Loop That Terrifies Scientists", "The permafrost carbon feedback is a textbook positive feedback loop. Human emissions warm the atmosphere. The warmer atmosphere thaws permafrost. Thawed permafrost releases CO2 and methane. These additional greenhouse gases warm the atmosphere further. The warmer atmosphere thaws more permafrost. Each cycle amplifies the last. Current estimates suggest this feedback could add 0.3 degrees Celsius of additional warming by 2100 under high-emission scenarios — on top of the warming from human emissions. The critical question is whether this feedback has a tipping point beyond which it becomes self-sustaining."),
        ("Can Anything Stop It?", "Two natural processes partially counteract the permafrost feedback. Oceans absorb about 25% of atmospheric CO2 through dissolution and biological uptake (phytoplankton). Vegetation expansion into newly thawed Arctic regions absorbs some carbon through photosynthesis — shrubs and trees are moving northward as conditions warm. However, studies consistently show that these sinks cannot match the rate of carbon release from thawing permafrost. The carbon was accumulated over tens of thousands of years but is being released over decades — an asymmetry that overwhelms the planet's absorption capacity.")
    ],
    "lever_L": "Students identify seven components of the permafrost carbon system: Permafrost Temperature, Methane Release Rate, Microbial Decomposition, Atmospheric CO2, Ocean Absorption, Vegetation Growth, and Feedback Amplification — with Atmospheric CO2 as the external driver.",
    "lever_E": "Students determine that Atmospheric CO2 raises global temperature, increasing Permafrost Temperature. Thawing activates Microbial Decomposition and Methane Release Rate, which increase Atmospheric CO2 further. Ocean Absorption and Vegetation Growth provide partial offsetting, but Feedback Amplification tracks the net acceleration.",
    "lever_V": "Students build a computational model showing the positive feedback loop and the partial negative feedback from carbon sinks, tracking whether the net effect pushes toward a tipping point.",
    "lever_Ev": "Students run current trajectory, aggressive emissions cuts, and methane burst scenarios to determine whether the tipping point can be avoided and what happens if it is crossed.",
    "lever_R": "Students add Thermokarst Formation, Subsea Permafrost, or Albedo Change to explore additional feedback mechanisms and their contribution to tipping point dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic Arctic thawing landscape", "say": "There's a bomb buried under the Arctic. Not a weapon — something far more dangerous. 1,500 billion tons of carbon frozen in the ground, and the fuse is already lit.", "do": "Show a satellite time-lapse of Arctic ice retreat over 30 years. Then reveal the permafrost carbon number. Let the scale register.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary terms", "say": "Today you're modeling the feedback loop that keeps climate scientists awake at night — the one that could make climate change unstoppable.", "do": "Have students read objectives. Pre-teach 'positive feedback loop' and 'tipping point.' Quick-write: What's the difference between a feedback that stabilizes and one that amplifies?", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "What happens when 1,500 billion tons of frozen carbon thaws?", "say": "Twice the carbon in the entire atmosphere is frozen under your feet if you're standing in Siberia. What happens when that freezer stops working?", "do": "Visual comparison: Stack representing atmospheric carbon next to stack representing permafrost carbon. Which is bigger? Students react.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're going to model a system with a terrifying property — it can reach a point where it keeps going even if we try to stop it.", "do": "Preview each LEVER step. Emphasize that this model contains both positive (amplifying) and negative (dampening) feedback loops.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Seven component cards for permafrost feedback model", "say": "Seven components, two types of feedback, and one critical question: can we stop it?", "do": "Guide component sorting. Discuss why Atmospheric CO2 is external (driven by human emissions policy) while the Arctic system responds internally.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Feedback loop diagram with positive and negative arrows", "say": "Trace the loop: CO2 warms the air, air thaws the ground, ground releases more CO2. Now find what slows it down — and ask if it's enough.", "do": "Help students map both the positive feedback (warming-thawing-release) and the negative feedback (ocean absorption, vegetation growth). Calculate the net effect.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and simulation results for three scenarios", "say": "Three futures: business as usual, aggressive cuts, and a methane burst. Only one of them has a chance of avoiding the tipping point.", "do": "Students predict outcomes first. Run all three scenarios. Identify the tipping point threshold in each. Discuss which scenario is most realistic.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model exploration", "say": "Your model just showed why this is called a carbon bomb. Once the feedback becomes self-sustaining, it doesn't matter what humans do.", "do": "Lead discussion connecting model findings to current Arctic observations. Show real methane bubble data from Siberian lakes.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Arctic monitoring network design challenge", "say": "Scientists need to know exactly when the tipping point is approaching. Design the warning system.", "do": "Groups design Arctic monitoring networks. Must specify sensors, locations, power sources, data analysis methods, and warning thresholds.", "time": "12 min"}
    ],
    "sort_reasoning": "Atmospheric CO2 is the external component because it is primarily driven by human emissions decisions — fossil fuel combustion, deforestation, and industrial activity — that exist outside the Arctic permafrost system. Permafrost Temperature, Methane Release Rate, Microbial Decomposition, Ocean Absorption, Vegetation Growth, and Feedback Amplification are internal because they respond to atmospheric conditions and to each other through the natural carbon cycle feedback mechanisms.",
    "relationships": [
        ("Atmospheric CO2 to Permafrost Temperature", "POSITIVE (+)", "Higher Atmospheric CO2 strengthens the greenhouse effect, raising global and especially Arctic temperatures (Arctic amplification causes 2-3x faster warming at poles), which increases Permafrost Temperature toward the thawing threshold."),
        ("Permafrost Temperature to Microbial Decomposition", "POSITIVE (+)", "As Permafrost Temperature rises above 0 degrees Celsius, previously frozen organic material becomes available to soil microorganisms. Higher temperatures accelerate microbial metabolic rates, increasing decomposition of ancient carbon stores."),
        ("Microbial Decomposition to Atmospheric CO2", "POSITIVE (+)", "Active Microbial Decomposition converts ancient organic carbon into CO2 (in aerobic conditions) and methane (in anaerobic conditions), both of which enter the atmosphere and increase greenhouse gas concentrations — completing the positive feedback loop.")
    ],
    "sim_answers": [
        ("Current Trajectory Scenario", "With Atmospheric CO2 continuing to rise, Permafrost Temperature crosses the thawing threshold across increasingly large Arctic areas. Microbial Decomposition activates and Methane Release Rate accelerates. Ocean Absorption and Vegetation Growth provide some offset but cannot match the release rate. Feedback Amplification steadily increases, suggesting the system approaches tipping point conditions within 30-50 years. The positive feedback begins generating measurable additional warming."),
        ("Aggressive Emissions Cuts Scenario", "Even with near-zero human emissions growth, Permafrost Temperature continues to rise for decades due to thermal inertia in the climate system. Microbial Decomposition and Methane Release Rate still increase, but more slowly. The critical finding is whether Feedback Amplification remains below the self-sustaining threshold — the model suggests aggressive cuts may keep the system below the tipping point, but the margin is dangerously narrow.")
    ],
    "reflection_exemplars": [
        ("Why is this called a positive feedback if it is bad?", "In systems science, 'positive feedback' does not mean good — it means self-amplifying. The permafrost carbon feedback is positive because the output (greenhouse gases from thawing) reinforces the input (atmospheric warming that causes thawing). Each cycle amplifies the last. This is contrasted with negative feedback, which is self-correcting — like a thermostat that turns off heating when the room gets warm enough. The permafrost system has no thermostat. Once started, the warming-thawing-release cycle accelerates until the carbon reservoir is depleted."),
        ("Can we stop the feedback once it starts?", "The model shows that the answer depends on timing. If Atmospheric CO2 is stabilized before Feedback Amplification crosses the self-sustaining threshold, the permafrost carbon release slows and eventually stops as temperatures stabilize. But if the tipping point is crossed, the feedback generates enough warming to sustain itself — permafrost continues thawing and releasing carbon even without additional human emissions. The model demonstrates that every year of delay in emissions reduction moves the system closer to this irreversible threshold.")
    ],
    "stem_intro": "Present the challenge: The International Arctic Research Council needs a monitoring network to detect whether permafrost carbon release is approaching the self-sustaining tipping point. Your team will design the sensor network, data analysis system, and warning criteria that could give humanity advance notice of an irreversible climate shift.",
    "stem_concepts": [
        ("Remote Sensing Technologies", "Satellite-based thermal imaging, microwave sensors, and interferometric radar can detect permafrost temperature changes, ground subsidence from thermokarst formation, and methane plumes over vast Arctic areas that are impossible to monitor with ground stations alone."),
        ("Methane Flux Measurement", "Eddy covariance towers measure real-time methane emissions from permafrost landscapes by tracking the vertical movement of air parcels. Combined with chamber measurements and isotopic analysis, these tools can quantify carbon release and identify whether it originates from ancient permafrost or modern biological activity."),
        ("Tipping Point Detection", "Mathematical early-warning signals of approaching tipping points include increasing variance in system measurements, slower recovery from perturbations, and increasing autocorrelation in time series data. These statistical signatures can detect approaching tipping points before the transition occurs.")
    ],
    "stem_eval": [
        ("Expert (4)", "Monitoring design integrates satellite remote sensing with ground stations, uses multiple measurement types, includes tipping point detection algorithms, and provides a clear communication protocol for warning policymakers"),
        ("Proficient (3)", "Monitoring design includes appropriate sensor types and locations with reasonable coverage and some tipping point criteria"),
        ("Developing (2)", "Monitoring design includes some sensors but lacks geographic coverage, measurement diversity, or clear warning thresholds"),
        ("Beginning (1)", "Monitoring design is incomplete or does not connect measurements to tipping point detection")
    ],
    "support": [
        "Provide a map of the Arctic showing permafrost extent, temperature zones, and known thermokarst lake locations",
        "Use a diagram showing the positive feedback loop with numbered steps so students can trace the cycle",
        "Sentence frames: 'When Permafrost Temperature exceeds 0 degrees C, Microbial Decomposition __, which releases __ into the atmosphere, causing __ to increase further because __'"
    ],
    "extensions": [
        "Research the Siberian crater explosions caused by methane blowouts from thawing permafrost and analyze the implications for Arctic infrastructure",
        "Investigate how the Paleocene-Eocene Thermal Maximum (56 million years ago) was driven by a similar carbon feedback — and what it tells us about our future",
        "Model how subsea permafrost thawing on the Arctic Ocean floor could release methane clathrates and compare this to terrestrial permafrost carbon release"
    ],
    "cross_curr": [
        ("Math", "Calculate the total warming potential of 1,500 billion tons of carbon released as a mix of CO2 and methane over 50 years, and compare to current annual human emissions"),
        ("ELA", "Write a science journalism article explaining the permafrost carbon feedback to a general audience, making the science accessible without sacrificing accuracy"),
        ("Social Studies", "Research how indigenous Arctic communities are already experiencing permafrost thaw and analyze the environmental justice dimensions of who causes versus who suffers from climate change")
    ],
    "misconceptions": [
        ("Permafrost is just frozen dirt", "Permafrost is frozen ground that contains enormous amounts of organic carbon — dead plants and animals accumulated over tens of thousands of years. In some locations, permafrost is 30-50% organic material by weight. When it thaws, this material becomes available for microbial decomposition, releasing greenhouse gases. It is not just dirt — it is the largest terrestrial carbon reservoir on Earth.", "Compare the carbon content: 1,500 billion tons in permafrost versus 850 billion tons in the entire atmosphere. Permafrost is essentially a giant carbon freezer, and the power is being turned off."),
        ("Planting trees can offset permafrost emissions", "While Vegetation Growth does absorb some CO2, the rate of carbon release from thawing permafrost vastly exceeds what new Arctic vegetation can absorb. Trees grow slowly in Arctic conditions and cover only a fraction of the thawing area. Furthermore, dark trees absorb more solar radiation than white snow (albedo effect), potentially causing additional local warming. The math simply doesn't work — you cannot plant enough trees to offset 1,500 billion tons.", "Calculate: A single tree absorbs about 22 kg of CO2 per year. How many trees would you need to offset even 1% of the permafrost carbon reservoir? (Answer: approximately 680 billion trees per year — more than 80 trees for every person on Earth.)"),
        ("The Arctic has always been frozen so it will stay frozen", "The Arctic has not always been frozen. During the Eocene epoch (50 million years ago), the Arctic was ice-free with palm trees and crocodiles near the North Pole. Permafrost formed during ice ages and has persisted through warmer interglacial periods — but it has never experienced the rate of warming occurring today. Current warming is happening 10-100 times faster than natural cycles, giving permafrost no time to gradually adjust.", "Show the temperature record: Plot Arctic temperature over the past 100,000 years alongside the current warming spike. The rate of change is unprecedented.")
    ]
}

L04 = {
    "id": "G10L2-L04",
    "title": "Can We Engineer the Amazon Back to Life?",
    "subtitle": "Modeling Rainforest Restoration and Ecological Tipping Points",
    "ngss": "HS-LS2-7, HS-ESS2-7",
    "ngss_desc": "Design, evaluate, and refine a solution for reducing the impacts of human activities on the environment and biodiversity. Construct an argument based on evidence about the simultaneous coevolution of Earth's systems and life on Earth.",
    "big_question": "The Amazon rainforest is approaching a tipping point where it could transform from the world's largest carbon sink into a carbon source — can engineering and restoration reverse the damage?",
    "objectives": [
        "Model how deforestation rate, reforestation effort, and soil recovery interact to determine whether the Amazon can be restored",
        "Analyze the critical tipping point threshold where the rainforest can no longer sustain its own water cycle",
        "Predict the timeline and conditions required for meaningful biodiversity return and carbon sequestration recovery",
        "Evaluate the feasibility of engineering the Amazon back to ecological health using computational model evidence"
    ],
    "vocabulary": [
        ("Tipping Point Threshold", "The critical level of deforestation (estimated at 20-25% of total Amazon area) beyond which the rainforest cannot generate enough moisture to sustain itself, triggering irreversible conversion to savanna"),
        ("Ecological Succession", "The sequential process by which plant and animal communities recolonize a disturbed area, progressing from pioneer species through intermediate stages to mature forest over decades to centuries"),
        ("Carbon Sequestration", "The process by which growing forests absorb CO2 from the atmosphere and store it in biomass and soil — the Amazon currently sequesters approximately 2 billion tons of CO2 per year"),
        ("Hydrological Cycle", "The Amazon generates 50% of its own rainfall through evapotranspiration — trees release water vapor that forms clouds and falls as rain downwind, creating a self-sustaining moisture recycling system")
    ],
    "components": [
        ("Deforestation Rate", "The annual area of Amazon rainforest cleared for cattle ranching, soybean farming, logging, and mining — currently approximately 10,000 square kilometers per year", True),
        ("Reforestation Effort", "The scale of active tree-planting programs and natural regeneration assistance in degraded Amazon areas, measured in square kilometers restored per year", True),
        ("Soil Nutrient Recovery", "The gradual restoration of mycorrhizal fungal networks, organic matter, and nutrient cycling capacity in degraded soils — a process that takes 15-50 years after replanting", False),
        ("Water Cycle Restoration", "The recovery of evapotranspiration capacity and rainfall recycling as reforested areas mature and begin pumping moisture back into the atmosphere", False),
        ("Biodiversity Return", "The recolonization of restored areas by native plant and animal species, progressing from generalist pioneers to specialist forest-interior species over decades", False),
        ("Carbon Sequestration", "The net rate of atmospheric CO2 absorption by growing forest biomass minus emissions from continued deforestation and decomposition of cleared areas", False),
        ("Tipping Point Threshold", "The proximity of the current forest state to the critical deforestation level (~20-25%) beyond which the self-sustaining water cycle collapses and the remaining forest dries out and dies", False)
    ],
    "think_about_it": "If Deforestation Rate exceeds Reforestation Effort, the Tipping Point Threshold approaches. But Reforestation Effort depends on Soil Nutrient Recovery, which takes decades. Meanwhile, Water Cycle Restoration requires large areas of mature forest. Is there enough time to restore the Amazon before the tipping point is crossed?",
    "scenarios": [
        ("Deforestation Continues", "Maintain current Deforestation Rate with minimal Reforestation Effort — observe the approach to the tipping point"),
        ("Aggressive Restoration", "Stop Deforestation Rate and maximize Reforestation Effort — observe recovery timelines for soil, water cycle, and biodiversity"),
        ("Partial Intervention", "Reduce Deforestation Rate by half and moderate Reforestation Effort — observe whether this is sufficient to avoid the tipping point")
    ],
    "sim_scenarios": [
        ("Continued Deforestation", "Current deforestation rate, minimal restoration", "What do you predict happens to the Tipping Point Threshold if current deforestation continues for another 20 years?"),
        ("Aggressive Restoration", "Zero deforestation, maximum replanting", "How long do you predict it takes for Soil Nutrient Recovery and Water Cycle Restoration to reach functional levels after replanting?"),
        ("Partial Intervention", "Halved deforestation, moderate restoration", "Do you predict that halfway measures are enough to keep the Amazon from crossing the tipping point?")
    ],
    "discoveries": [
        "The Amazon's tipping point is dangerously close — approximately 17% of the original forest has already been cleared, with the threshold estimated at 20-25%",
        "Reforestation is not simply planting trees — Soil Nutrient Recovery takes 15-50 years and determines whether planted trees can actually survive and establish a self-sustaining ecosystem",
        "The water cycle is the critical feedback: the Amazon generates 50% of its own rainfall through evapotranspiration, so losing too much forest starves the remaining forest of water",
        "Full ecosystem recovery including Biodiversity Return of specialist species requires 100-200+ years — there is no quick fix for complex tropical forest ecosystems"
    ],
    "answer": "Engineering the Amazon back to life is theoretically possible but faces extraordinary challenges of time and scale. The rainforest is approaching a tipping point (~20-25% deforestation) where it can no longer generate enough rainfall to sustain itself. Currently at ~17% cleared, every year of continued deforestation narrows the window. Restoration requires stopping deforestation immediately AND actively replanting degraded areas — but success depends on soil recovery (15-50 years), water cycle restoration (requires large contiguous reforested areas), and biodiversity return (100-200+ years for specialist species). The model reveals a painful truth: even under the most optimistic restoration scenarios, the Amazon cannot return to its original state within any human lifetime. But the alternative — doing nothing and crossing the tipping point — would convert the world's largest rainforest into degraded savanna, releasing hundreds of billions of tons of carbon and extinguishing millions of species.",
    "stem_title": "Design an Amazon Restoration Master Plan",
    "stem_mission": "Design a 50-year restoration plan for a 10,000 square kilometer degraded Amazon region, specifying planting strategies, soil recovery techniques, and monitoring milestones.",
    "stem_scenario": "The Brazilian government has committed to restoring 10,000 square kilometers of degraded Amazon land and hired your team to design the master plan. You must balance speed (preventing tipping point crossing) with ecological integrity (ensuring the restored forest is self-sustaining, not just a tree plantation).",
    "stem_questions": [
        "How would you prioritize which areas to restore first — proximity to intact forest, soil quality, or water cycle importance?",
        "What species would you plant in the first phase versus the fifth phase of restoration?",
        "How would you monitor whether the restored areas are developing self-sustaining ecological function?"
    ],
    "stem_design_qs": [
        "What planting density, species mix, and spatial arrangement would maximize early soil recovery?",
        "How would you use corridors to connect restored patches with intact forest for wildlife colonization?",
        "What role would local and indigenous communities play in long-term forest stewardship?",
        "What metrics would you use to determine success at 5, 10, 25, and 50 year milestones?"
    ],
    "career": "Restoration Ecologists design and implement ecosystem recovery projects for degraded landscapes. They work for conservation organizations, government agencies, and consulting firms, earning $55,000–$110,000/year. Tropical Ecologists studying Amazon dynamics earn $60,000–$130,000/year.",
    "images": {
        "cover": ("G10L2-L04-cover.png", "A photorealistic, cinematic split image showing half dense Amazon rainforest canopy teeming with life and half barren deforested land with burned stumps and exposed red soil, dramatic lighting emphasizing the contrast between life and destruction"),
        "landscape": ("G10L2-L04-landscape.png", "A diverse group of 15-16 year old students in a modern biology lab examining tropical soil samples and rainforest ecosystem models, large map of the Amazon basin on the wall, engaged and collaborative expressions, natural classroom lighting"),
        "modeling": ("G10L2-L04-modeling.png", "A diverse group of 15-16 year old students working on laptops building computational models of forest restoration dynamics, screens showing deforestation maps and recovery timelines, modern classroom with tropical ecology posters"),
        "discussion": ("G10L2-L04-discussion.png", "A teacher leading an animated discussion with diverse 15-16 year old students about ecological tipping points, a diagram showing the Amazon moisture recycling system displayed on a smartboard, students actively participating"),
        "stem": ("G10L2-L04-stem.png", "Diverse 15-16 year old students designing Amazon restoration master plans with maps, timelines, and species lists on large displays, collaborative atmosphere with ecological planning materials visible")
    },
    "pre_assessment": [
        "What do you think happens to the land, soil, and climate after a rainforest is cut down?",
        "Why might it be harder to regrow a rainforest than to plant a new forest in a temperate region?",
        "Draw a diagram showing how you think a rainforest creates its own weather system.",
        "What do you think a 'tipping point' means for an ecosystem like the Amazon?"
    ],
    "extend_components": [
        ("Fire Vulnerability", "The susceptibility of degraded and edge-of-forest areas to fire during dry seasons, which can destroy restoration progress and accelerate tipping point approach"),
        ("Indigenous Land Management", "The conservation effectiveness of indigenous-managed territories, which show 50% lower deforestation rates than other areas due to traditional ecological knowledge and stewardship"),
        ("Economic Pressure", "The market forces driving deforestation — cattle ranching, soy farming, illegal logging, and gold mining — which must be addressed for any restoration plan to succeed long-term")
    ],
    "reflections": [
        "How does your model demonstrate that the Amazon's water cycle is a self-sustaining feedback loop — and why its disruption is so dangerous?",
        "What does your model reveal about the timescale mismatch between the speed of destruction and the pace of restoration?",
        "Why is the tipping point concept so critical for policy decisions about the Amazon?",
        "How does Biodiversity Return differ from simply replanting trees, and why does this distinction matter for ecosystem function?",
        "What are the limitations of modeling complex tropical ecology with only seven components when real rainforests contain millions of interacting species?"
    ],
    "dimensions": [
        ("Science Practice", "Designing Solutions", "Students design evidence-based restoration plans using computational model data to optimize species selection, spatial arrangement, and timeline milestones."),
        ("Disciplinary Core Idea", "LS2.C Ecosystem Dynamics, Functioning, and Resilience / ESS2.A Earth Materials and Systems", "Ecosystems maintain function through interconnected biotic and abiotic processes; disruption of key components can trigger cascading failure and regime shifts."),
        ("Crosscutting Concept", "Stability and Change", "Students model how the Amazon ecosystem maintains stability through self-reinforcing feedback loops and identify the threshold conditions where stability is lost.")
    ],
    "cast_items": [
        "Model the feedback loops connecting deforestation, water cycle disruption, and tipping point dynamics",
        "Analyze the timescales of soil recovery, water cycle restoration, and biodiversity return in degraded tropical ecosystems",
        "Design restoration strategies optimized for avoiding the tipping point while maximizing long-term ecological recovery"
    ],
    "cast_questions": [
        ("Multiple Choice:", "The Amazon has lost 17% of its original forest cover. Based on your model, what is the most urgent action to prevent crossing the estimated 20-25% tipping point?"),
        ("Constructed Response:", "Using your model, explain why simply replanting trees in deforested areas is not sufficient to restore the Amazon's ecological function. Reference Soil Nutrient Recovery, Water Cycle Restoration, and Biodiversity Return in your explanation.")
    ],
    "background_intro": "The Amazon rainforest — 5.5 million square kilometers spanning nine countries — is the most biodiverse ecosystem on Earth, home to 10% of all known species, storing 150-200 billion tons of carbon, and generating half of its own rainfall. It is also approaching a catastrophic tipping point that could transform it from the world's greatest carbon sink into a massive carbon source.",
    "background_sections": [
        ("The Amazon's Self-Sustaining Water Cycle", "Unlike most forests, the Amazon creates its own weather. Trees pump water from the soil through their roots and release it as water vapor through their leaves — a process called evapotranspiration. A single large Amazon tree can release 1,000 liters of water per day. This moisture forms clouds that travel westward, generating rainfall that sustains the forest downwind. Approximately 50% of the Amazon's rainfall is recycled moisture from the forest itself. This means the forest needs itself to survive — remove enough trees and the remaining forest doesn't get enough rain to sustain itself."),
        ("The Tipping Point", "Scientists estimate the Amazon's tipping point lies at 20-25% total deforestation — the level at which the forest can no longer generate sufficient rainfall to sustain itself. As of 2024, approximately 17% of the original Amazon has been cleared. At current deforestation rates of 10,000 square kilometers per year, the tipping point could be reached within 15-25 years. Once crossed, models predict a cascade: reduced rainfall causes tree death, which reduces evapotranspiration, which further reduces rainfall, converting most of the eastern and southern Amazon to degraded savanna within decades."),
        ("The Challenge of Restoration", "Replanting trees is necessary but woefully insufficient for restoring a tropical rainforest. The Amazon's biodiversity includes over 80,000 plant species with intricate ecological relationships — mycorrhizal fungal networks that connect tree roots, specific pollinators for each plant species, seed dispersers that distribute species across the landscape. Soil in deforested areas loses its organic layer, fungal networks, and nutrient cycling capacity within years. Rebuilding these foundations takes 15-50 years under optimal conditions. Full canopy forest with specialist interior species requires 100-200+ years."),
        ("Success Stories and Lessons", "Despite the daunting challenges, some restoration projects show promise. Costa Rica reversed decades of deforestation, going from 21% to 60% forest cover in 30 years through payments for ecosystem services. Atlantic Forest restoration in Brazil has replanted millions of hectares using natural regeneration assisted by seed dispersal. Key lessons: restoration near intact forest succeeds faster (seed sources and wildlife corridors), mixed species plantings outperform monocultures, and involving local and indigenous communities is essential for long-term success.")
    ],
    "lever_L": "Students identify seven components of the Amazon restoration system: Deforestation Rate, Reforestation Effort, Soil Nutrient Recovery, Water Cycle Restoration, Biodiversity Return, Carbon Sequestration, and Tipping Point Threshold — with Deforestation Rate and Reforestation Effort as external drivers.",
    "lever_E": "Students determine that Deforestation Rate pushes the system toward the tipping point while Reforestation Effort pulls it back. Recovery depends on Soil Nutrient Recovery enabling Water Cycle Restoration, which enables Biodiversity Return, which enables full Carbon Sequestration. The timescales are decades to centuries.",
    "lever_V": "Students build a computational model showing the race between deforestation and restoration, with the tipping point as the critical threshold that determines the Amazon's fate.",
    "lever_Ev": "Students run continued deforestation, aggressive restoration, and partial intervention scenarios to determine which strategies can prevent tipping point crossing and what recovery timelines look like.",
    "lever_R": "Students add Fire Vulnerability, Indigenous Land Management, or Economic Pressure to explore how additional factors affect restoration feasibility and tipping point dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic forest-to-destruction split image", "say": "The Amazon generates half of its own rain. It is the only forest on Earth that literally creates the weather it needs to survive. And we are cutting it down.", "do": "Show satellite comparison of Amazon deforestation over 20 years. Ask: What happens when a forest that makes its own rain loses too many trees to make rain?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary terms", "say": "Today you're going to determine whether the Amazon can be saved — or whether we're already too late.", "do": "Have students read objectives. Pre-teach 'tipping point threshold' and 'ecological succession.' Quick-write: How long do you think it takes to regrow a rainforest?", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Can we engineer the Amazon back to life?", "say": "17% gone. Tipping point at 20-25%. That's a margin of 3-8%. At current rates, we have 15-25 years. Can we fix this?", "do": "Students calculate: At 10,000 sq km per year of deforestation, how many years until 20%? Until 25%? Discuss the urgency.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're racing the clock. Build the model that tells us whether restoration can outpace destruction.", "do": "Preview each LEVER step. Emphasize that this is about timescales — destruction is fast, recovery is slow.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Seven component cards for Amazon restoration model", "say": "Two things we control directly: how fast we cut and how fast we plant. Everything else the ecosystem has to do on its own.", "do": "Guide sorting. Discuss why Deforestation Rate and Reforestation Effort are external (policy-driven) while ecological recovery processes are internal.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between restoration components", "say": "You can plant a million trees tomorrow. But can those trees survive in depleted soil? Can they restart the rain cycle? How long does each step take?", "do": "Help students trace the recovery cascade. Identify the bottleneck: Soil Nutrient Recovery is the rate-limiting step for everything downstream.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and simulation results", "say": "Let's test three futures for the Amazon. Which one saves it? Which one loses it forever?", "do": "Students predict outcomes first, then run all three scenarios. Focus on the tipping point threshold in each. Discuss the 'partial intervention' scenario — is halfway enough?", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model exploration", "say": "The model reveals an uncomfortable truth: even aggressive restoration takes decades to centuries. But the alternative is losing the Amazon entirely.", "do": "Lead discussion on the timescale mismatch. Compare destruction speed (years) to recovery speed (decades-centuries). Discuss what 'success' looks like at different timescales.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Amazon restoration master plan design challenge", "say": "Brazil just gave your team 10,000 square kilometers and 50 years. Design the plan that brings the Amazon back to life.", "do": "Groups design comprehensive restoration plans including species selection, phasing, monitoring milestones, and community engagement. Present as professional proposals.", "time": "12 min"}
    ],
    "sort_reasoning": "Deforestation Rate and Reforestation Effort are external components because they are directly controlled by human decisions — government policy, economic incentives, law enforcement, and conservation investments. Soil Nutrient Recovery, Water Cycle Restoration, Biodiversity Return, Carbon Sequestration, and Tipping Point Threshold are internal because they are ecological processes that respond to the balance between destruction and restoration according to natural timescales and biological dynamics.",
    "relationships": [
        ("Deforestation Rate to Tipping Point Threshold", "POSITIVE (+)", "Higher Deforestation Rate directly pushes the system closer to the critical threshold by removing the trees that generate rainfall and maintain the self-sustaining water cycle. Each hectare cleared reduces the forest's ability to sustain itself."),
        ("Reforestation Effort to Soil Nutrient Recovery", "POSITIVE (+)", "Greater Reforestation Effort — planting native species in degraded areas — initiates the slow process of rebuilding soil organic matter, mycorrhizal networks, and nutrient cycling capacity that were destroyed by deforestation."),
        ("Water Cycle Restoration to Biodiversity Return", "POSITIVE (+)", "As the water cycle recovers through increased evapotranspiration from maturing reforested areas, consistent rainfall supports the return of moisture-dependent species and enables ecological succession toward complex forest community structure.")
    ],
    "sim_answers": [
        ("Continued Deforestation Scenario", "With current Deforestation Rate and minimal Reforestation Effort, the Tipping Point Threshold is approached within 15-25 years. As the threshold nears, Water Cycle Restoration stalls because remaining forest fragments cannot generate sufficient rainfall. Biodiversity Return and Carbon Sequestration decline as the system degrades. If the tipping point is crossed, the model predicts cascading forest dieback converting the eastern and southern Amazon to savanna."),
        ("Aggressive Restoration Scenario", "With zero deforestation and maximum Reforestation Effort, the system stabilizes — but recovery is painfully slow. Soil Nutrient Recovery shows meaningful improvement after 15-20 years. Water Cycle Restoration begins to register after 20-30 years as restored areas reach sufficient maturity for significant evapotranspiration. Full Biodiversity Return requires 100-200+ years. Carbon Sequestration gradually increases as biomass accumulates. The tipping point recedes but the Amazon does not return to its original state within any human lifetime.")
    ],
    "reflection_exemplars": [
        ("Why can't we just plant trees and fix the Amazon?", "The model demonstrates that tree planting is a necessary first step but is limited by Soil Nutrient Recovery — the slowest component in the system. Deforested Amazon soil loses its mycorrhizal fungal networks, organic matter, and nutrient cycling capacity. Without these soil foundations, planted trees grow slowly, many die, and the ecosystem cannot progress through ecological succession. Furthermore, isolated tree plantations cannot restart the water cycle — Water Cycle Restoration requires large, contiguous areas of mature forest generating enough evapotranspiration to produce rainfall. Restoration is not a planting problem; it's an ecosystem rebuilding problem."),
        ("Is there still time to save the Amazon?", "The model suggests the answer is yes — barely. At 17% deforested with a tipping point at 20-25%, there is a 3-8% margin. But this margin is shrinking by approximately 0.2% per year at current deforestation rates. The model shows that aggressive action — stopping deforestation completely and initiating large-scale restoration — could stabilize the system. Partial measures (halving deforestation) may not be enough because the self-reinforcing nature of the water cycle means even small additional losses have disproportionate effects near the threshold. The window for action is open but closing rapidly.")
    ],
    "stem_intro": "Present the challenge: Brazil has committed to restoring 10,000 square kilometers of degraded Amazon land. Your team will design the 50-year master plan, specifying what to plant, when, where, and how to monitor progress — with the scientific understanding that this is not just gardening but ecosystem engineering.",
    "stem_concepts": [
        ("Nucleation Planting", "Instead of planting trees uniformly across degraded land, nucleation planting creates dense clusters ('islands') of native species that attract seed dispersers and naturally expand. This mimics natural regeneration patterns and is more cost-effective than full-coverage planting."),
        ("Assisted Natural Regeneration", "In areas near intact forest, removing barriers to natural seed dispersal (such as invasive grasses) and protecting young seedlings can be more effective than active planting. The intact forest provides seeds, mycorrhizal inoculants, and wildlife corridors."),
        ("Ecological Monitoring Indicators", "Successful restoration is measured not just by tree count but by functional indicators: canopy closure, soil organic matter, fungal network development, bird and insect species diversity, and water cycling capacity. These indicators reveal whether the restoration is building a self-sustaining ecosystem or just a tree plantation.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan uses phased approach with species appropriate for each succession stage, includes soil recovery strategy, connects patches to intact forest, specifies monitoring milestones, involves local communities, and uses model data to justify timelines"),
        ("Proficient (3)", "Plan includes reasonable species selection, spatial arrangement, and monitoring with some model-based justification"),
        ("Developing (2)", "Plan addresses planting but lacks phasing, soil recovery strategy, or connection to model evidence"),
        ("Beginning (1)", "Plan is incomplete or treats restoration as simple tree planting without considering ecological succession")
    ],
    "support": [
        "Provide a map of Amazon deforestation showing the 'arc of deforestation' and proximity of degraded areas to intact forest",
        "Use a timeline graphic showing the stages of ecological succession: pioneer species (0-5 years), early successional (5-20 years), mid-successional (20-50 years), mature forest (50-200+ years)",
        "Sentence frames: 'When Reforestation Effort increases, Soil Nutrient Recovery begins to __ because __, which eventually enables __ to improve'"
    ],
    "extensions": [
        "Research how the Amazon's 'flying rivers' — atmospheric moisture corridors generated by forest evapotranspiration — supply rainfall to South American agriculture thousands of kilometers away",
        "Investigate the role of Brazil's indigenous territories as 'walls of forest' that resist deforestation and analyze the legal and political threats these territories face",
        "Compare the Amazon's tipping point dynamics to the Sahel region of Africa, where deforestation triggered desertification that has proven extremely difficult to reverse"
    ],
    "cross_curr": [
        ("Math", "Calculate the area of forest needed to generate sufficient evapotranspiration to sustain regional rainfall, using data on tree water release rates and regional precipitation requirements"),
        ("ELA", "Research and debate the tension between Brazilian economic development (cattle, soy, mining) and Amazon conservation, presenting evidence-based arguments for both sides"),
        ("Social Studies", "Investigate how Payment for Ecosystem Services programs in Costa Rica incentivized reforestation and analyze whether similar approaches could work in Brazil")
    ],
    "misconceptions": [
        ("Planting any trees counts as restoration", "Ecologically meaningful restoration requires planting native species in appropriate combinations that can support the full web of ecological interactions. Monoculture plantations of eucalyptus or pine do not restore rainforest function — they lack biodiversity, do not support native wildlife, deplete soil differently, and do not generate the same evapotranspiration patterns. True restoration mimics natural forest composition.", "Compare: A monoculture pine plantation has 1 tree species and supports ~20 bird species. A restored Amazon plot with 100 native tree species can support 400+ bird species. Numbers matter."),
        ("Forests regrow quickly if you leave them alone", "While natural regeneration does occur in small clearings near intact forest, large-scale deforested areas face multiple barriers: depleted soils, invasive grasses that prevent tree seedling establishment, absence of seed dispersers, and altered microclimate (too hot and dry for forest species). In heavily degraded areas, active restoration is essential — natural regeneration alone could take 500+ years or may never occur.", "Show time-lapse comparisons: A naturally regenerating plot near intact forest vs. a large deforested area far from forest. After 20 years, the difference is stark."),
        ("The Amazon is too big to lose", "The Amazon's size creates the illusion of invulnerability, but the tipping point model shows that the forest's survival depends on a self-sustaining feedback loop (evapotranspiration-rainfall) that has a critical threshold. Once 20-25% is cleared, the remaining 75-80% may not receive enough self-generated rainfall to survive. Size provides no protection against a system-level collapse.", "Analogy: A large building seems indestructible until you remove enough support columns. The Amazon's 'support columns' are the trees that generate its rainfall. Remove 20-25% of them and the entire structure becomes unstable.")
    ]
}

L05 = {
    "id": "G10L2-L05",
    "title": "Why Did Dinosaurs Rule and Then Vanish?",
    "subtitle": "Modeling Extinction Dynamics and the Fragility of Dominant Species",
    "ngss": "HS-LS4-1, HS-LS4-4",
    "ngss_desc": "Communicate scientific information that common ancestry and biological evolution are supported by multiple lines of empirical evidence. Construct an explanation based on evidence for how natural selection leads to adaptation of populations.",
    "big_question": "Dinosaurs dominated Earth for 165 million years — then vanished almost overnight. What determines whether a species survives or goes extinct when the environment changes catastrophically?",
    "objectives": [
        "Model how species diversity, environmental change rate, and adaptation speed interact to determine extinction outcomes",
        "Analyze why dominant species can be more vulnerable to extinction than generalist species when conditions change rapidly",
        "Predict the conditions under which populations can recover from mass extinction events versus those that lead to permanent loss",
        "Evaluate how niche competition and survival advantages shift when environmental conditions change faster than species can adapt"
    ],
    "vocabulary": [
        ("Mass Extinction", "An event in which a significant proportion of Earth's species — typically more than 75% — go extinct within a geologically brief period, usually caused by catastrophic environmental change that exceeds the adaptive capacity of most organisms"),
        ("Adaptive Radiation", "The rapid evolutionary diversification of a single ancestral lineage into many new species, each adapted to a different ecological niche — typically occurring after a mass extinction creates vacant niches"),
        ("Niche Competition", "The struggle between species that occupy similar ecological roles for the same limited resources — food, habitat, mates — which intensifies when environments shrink or resources become scarce"),
        ("Selection Pressure", "An environmental factor that affects which individuals in a population survive and reproduce, driving the direction and speed of evolutionary change — more intense pressure drives faster adaptation or extinction")
    ],
    "components": [
        ("Species Diversity", "The total number and variety of species in an ecosystem, including genetic diversity within species — higher diversity provides more evolutionary 'options' for survival during environmental change", False),
        ("Environmental Change Rate", "The speed at which conditions shift — temperature, atmospheric composition, food availability, habitat — which determines whether organisms can adapt, migrate, or go extinct", True),
        ("Adaptation Speed", "The rate at which populations can evolve traits that match new environmental conditions, limited by generation time, genetic variation, and the intensity of selection pressure", False),
        ("Extinction Pressure", "The cumulative stress on populations from environmental change, habitat loss, food web disruption, and competition — when this exceeds a species' tolerance, extinction occurs", False),
        ("Niche Competition", "The intensity of competitive interactions between species for limited resources, which increases when environmental change reduces available habitat and food sources", False),
        ("Survival Advantage", "The traits that provide a fitness benefit in the changed environment — small body size, generalist diet, burrowing ability, or rapid reproduction — which differ from advantages in the pre-extinction environment", False),
        ("Population Recovery", "The ability of surviving species to expand their populations and diversify into empty niches after the extinction event passes, beginning the process of adaptive radiation", False)
    ],
    "think_about_it": "When Environmental Change Rate is extremely fast (asteroid impact), Adaptation Speed cannot keep up — Extinction Pressure overwhelms Species Diversity. But some organisms survive. What Survival Advantages allowed mammals, birds, and crocodilians to survive while dinosaurs perished?",
    "scenarios": [
        ("Gradual Climate Change", "Set Environmental Change Rate to slow — observe how Adaptation Speed and Niche Competition shift Species Diversity over millions of years"),
        ("Asteroid Impact", "Set Environmental Change Rate to maximum (sudden catastrophic change) — observe the mass extinction cascade and which traits provide Survival Advantage"),
        ("Post-Extinction Recovery", "After the mass extinction event, observe how Population Recovery and adaptive radiation refill empty ecological niches over millions of years")
    ],
    "sim_scenarios": [
        ("Gradual Change", "Slow environmental shift over millions of years", "What do you predict happens to Species Diversity when Environmental Change Rate is slow enough for Adaptation Speed to keep pace?"),
        ("Asteroid Impact", "Sudden catastrophic environmental change", "What do you predict determines which species survive when Environmental Change Rate vastly exceeds Adaptation Speed?"),
        ("Post-Extinction", "Recovery after mass extinction", "How do you predict Population Recovery will proceed — which types of organisms will diversify first?")
    ],
    "discoveries": [
        "Mass extinction is not about which species are the most powerful but which are best suited to survive catastrophic conditions — size and dominance become liabilities when food webs collapse",
        "Adaptation Speed has a biological limit determined by generation time and genetic variation — when Environmental Change Rate exceeds this limit, extinction is inevitable regardless of fitness",
        "Survival Advantage shifts dramatically during mass extinction events — traits like small body size, generalist diet, and ability to enter torpor become critical, reversing the normal competitive hierarchy",
        "Population Recovery after mass extinction follows a predictable pattern: opportunistic generalists colonize first, followed by gradual specialization and adaptive radiation over millions of years"
    ],
    "answer": "Dinosaurs didn't vanish because they were poorly designed — they were among the most successful organisms in Earth's history, dominating for 165 million years. They vanished because the Chicxulub asteroid impact changed the environment faster than any organism could adapt. The impact triggered nuclear winter conditions: dust and sulfur blocked sunlight, photosynthesis collapsed, food webs disintegrated from the bottom up, and global temperatures dropped 10-15 degrees Celsius in months. Large-bodied animals that needed enormous food supplies couldn't survive on the meager resources available. Small mammals, birds (which are actually surviving dinosaurs), crocodilians, and insects survived because of smaller body size, lower metabolic demands, ability to burrow or enter torpor, and generalist diets. The lesson is universal: dominance provides no protection when the environment changes faster than evolution can respond.",
    "stem_title": "Design a Biodiversity Resilience Index",
    "stem_mission": "Design a scoring system that evaluates how vulnerable or resilient different species are to rapid environmental change, based on their biological traits and ecological relationships.",
    "stem_scenario": "Conservation biologists need a tool that predicts which modern species are most vulnerable to rapid environmental change (climate change, habitat destruction, pollution). Your team has been hired to design a Biodiversity Resilience Index that scores species based on the same survival factors your model identified.",
    "stem_questions": [
        "What biological traits should your index score — body size, diet breadth, reproductive rate, habitat specificity?",
        "How would you weight the different factors based on what your model revealed about extinction dynamics?",
        "How could your index be used to prioritize conservation efforts for the most vulnerable species?"
    ],
    "stem_design_qs": [
        "What data would you need to calculate a resilience score for any given species?",
        "How would you account for species that are specialists versus generalists?",
        "What threshold score would indicate a species is at high extinction risk?",
        "How would your index handle interconnected species — if a keystone species scores low, how does that affect dependent species?"
    ],
    "career": "Paleobiologists study ancient life through fossils to understand evolution, extinction, and the history of biodiversity. They work at museums, universities, and research institutions, earning $55,000–$120,000/year. Conservation Biologists who apply extinction science to modern species protection earn $50,000–$110,000/year.",
    "images": {
        "cover": ("G10L2-L05-cover.png", "A photorealistic, cinematic image of a dramatic prehistoric scene showing a massive asteroid streaking across the sky above a landscape where dinosaurs look upward, fiery impact glow on the horizon, combining scientific accuracy with dramatic cinematic lighting"),
        "landscape": ("G10L2-L05-landscape.png", "A diverse group of 15-16 year old students in a modern paleontology lab examining fossil specimens and casts, geological timeline charts on the walls, magnifying glasses and digital microscopes on tables, engaged expressions, natural lighting"),
        "modeling": ("G10L2-L05-modeling.png", "A diverse group of 15-16 year old students working on laptops building computational models of extinction dynamics, screens showing species diversity curves and environmental change graphs, modern classroom with evolution posters"),
        "discussion": ("G10L2-L05-discussion.png", "A teacher leading an animated discussion with diverse 15-16 year old students about mass extinction patterns, a geological timeline showing the five major extinctions displayed on a smartboard, students actively debating"),
        "stem": ("G10L2-L05-stem.png", "Diverse 15-16 year old students designing biodiversity resilience index scoring systems with species data cards and ranking charts on large displays, collaborative atmosphere with biological specimens visible")
    },
    "pre_assessment": [
        "What do you think caused the extinction of the dinosaurs — and why didn't ALL life go extinct?",
        "Why might being the biggest and strongest animal actually be a disadvantage during a catastrophe?",
        "Draw a diagram showing what you think happens to an ecosystem when its dominant species suddenly disappears.",
        "What traits do you think helped some species survive the asteroid impact that killed the dinosaurs?"
    ],
    "extend_components": [
        ("Food Web Complexity", "The number and strength of feeding relationships in an ecosystem, which determines how disruption of one species cascades through the entire community"),
        ("Genetic Diversity", "The range of genetic variation within a species' population, which determines the raw material available for natural selection and the potential for rapid adaptation"),
        ("Geographic Range", "The total area occupied by a species, which affects vulnerability — widespread species are less likely to be completely eliminated by a localized catastrophe")
    ],
    "reflections": [
        "How does your model explain why 165 million years of evolutionary success provided no protection against the asteroid impact?",
        "What does your model reveal about the relationship between Adaptation Speed and Environmental Change Rate — why is there a critical threshold?",
        "Why did small body size become a Survival Advantage during the mass extinction when large body size was advantageous before it?",
        "How does your model's Population Recovery phase relate to the concept of adaptive radiation?",
        "What parallels does your model suggest between the Cretaceous mass extinction and the current biodiversity crisis driven by human activity?"
    ],
    "dimensions": [
        ("Science Practice", "Constructing Explanations", "Students construct evidence-based explanations of mass extinction dynamics by analyzing the interactions between environmental change rate, adaptation speed, and survival traits in their computational model."),
        ("Disciplinary Core Idea", "LS4.A Evidence of Common Ancestry / LS4.C Adaptation", "Multiple lines of fossil evidence document mass extinction events and subsequent adaptive radiation; natural selection drives adaptation but cannot operate faster than the rate of environmental change."),
        ("Crosscutting Concept", "Cause and Effect", "Students trace the causal chain from catastrophic environmental change through food web collapse, competitive hierarchy reversal, and selective survival to post-extinction recovery and adaptive radiation.")
    ],
    "cast_items": [
        "Model how the rate of environmental change relative to adaptation speed determines extinction versus survival outcomes",
        "Analyze why dominant species can be more vulnerable than generalist species during mass extinction events",
        "Predict post-extinction recovery patterns using computational model evidence"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A mass extinction event rapidly eliminates 75% of species. Based on your model, which type of organism is most likely to survive?"),
        ("Constructed Response:", "Using your model, explain why dinosaurs — the most successful land animals in Earth's history — went extinct while small mammals survived. Reference Environmental Change Rate, Adaptation Speed, and Survival Advantage in your answer.")
    ],
    "background_intro": "Dinosaurs were not failures. They were the most successful terrestrial vertebrates in Earth's history, dominating every continent for 165 million years — 800 times longer than modern humans have existed. Their extinction was not a result of evolutionary inferiority but of environmental change so sudden and severe that adaptation was physically impossible.",
    "background_sections": [
        ("The Chicxulub Impact", "Sixty-six million years ago, a 10-kilometer asteroid struck what is now the Yucatan Peninsula at 70,000 km/h. The impact released energy equivalent to 10 billion nuclear weapons. Within hours, the entire hemisphere was subjected to superheated debris raining from the sky, igniting global wildfires. Within weeks, sulfur aerosols and dust blocked 90% of sunlight. Within months, photosynthesis largely ceased, collapsing food webs from the bottom up. Global temperatures dropped 10-15 degrees Celsius. This 'impact winter' lasted 3-10 years."),
        ("Why Size Killed the Dinosaurs", "Large body size was the dinosaurs' greatest advantage — and their fatal vulnerability. Large animals require enormous caloric intake. A Tyrannosaurus rex needed an estimated 40,000-60,000 calories per day. When photosynthesis collapsed and food webs disintegrated, large animals simply could not find enough food to sustain their metabolism. Small mammals could survive on insects, seeds, and detritus. Small body size also meant shorter generation times, lower caloric needs, ability to burrow for shelter, and capacity to enter torpor (a hibernation-like state) during resource scarcity."),
        ("The Survivors", "The organisms that survived the K-Pg extinction share revealing traits. Mammals (small, burrowing, insectivorous), birds (small-bodied descendants of theropod dinosaurs), crocodilians (aquatic, able to survive long periods without food), turtles (protected by shells, slow metabolism), frogs (small, aquatic, can estivate), and insects (short generation times, diverse diets, small body size). The pattern is clear: generalist diet, small body size, low metabolic demands, ability to shelter or go dormant, and short generation times were the winning combination."),
        ("Recovery and Adaptive Radiation", "After the extinction pressure lifted, the surviving lineages underwent explosive adaptive radiation — rapid evolutionary diversification into empty ecological niches. Mammals evolved from small, mouse-like creatures into every modern form: whales, bats, elephants, primates. Birds diversified from small, ground-dwelling survivors into 10,000+ species occupying every habitat from ocean to mountaintop. This recovery took millions of years — the first large mammals didn't appear until 10 million years after the impact. Evolution rebuilds, but never quickly.")
    ],
    "lever_L": "Students identify seven components of the extinction dynamics system: Species Diversity, Environmental Change Rate, Adaptation Speed, Extinction Pressure, Niche Competition, Survival Advantage, and Population Recovery — with Environmental Change Rate as the external driver.",
    "lever_E": "Students determine that Environmental Change Rate drives Extinction Pressure, which overwhelms Adaptation Speed when change is too rapid. Niche Competition intensifies as resources shrink. Survival Advantage shifts from traits favoring dominance to traits favoring resilience. Population Recovery begins when conditions stabilize.",
    "lever_V": "Students build a computational model showing how the rate of environmental change relative to adaptation speed determines whether species survive or go extinct.",
    "lever_Ev": "Students run gradual change, asteroid impact, and post-extinction recovery scenarios to compare outcomes and identify which biological traits provide survival advantage in each context.",
    "lever_R": "Students add Food Web Complexity, Genetic Diversity, or Geographic Range to explore additional factors that determine species vulnerability and resilience during mass extinction events.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic asteroid impact scene", "say": "For 165 million years, dinosaurs ruled every continent on Earth. Then, in a single bad day, it was over. What determines who lives and who dies when the world changes overnight?", "do": "Show the scale: dinosaurs ruled for 165 million years; modern humans have existed for 200,000. Ask: What can a 165-million-year winning streak not protect you from?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary terms", "say": "Today you're modeling the most dramatic event in the history of life — and asking a question that matters for the future: what determines survival?", "do": "Have students read objectives. Pre-teach 'mass extinction' and 'adaptive radiation.' Quick-write: List three traits you think would help a species survive a catastrophe.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why did dinosaurs rule and then vanish?", "say": "Being big, powerful, and dominant for 165 million years wasn't enough. What went wrong — and what does it teach us about survival?", "do": "Think-pair-share: Students brainstorm why being the top predator might become a disadvantage. Share and discuss.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're going to model what happens when the environment changes faster than evolution can respond. Spoiler: it's not pretty.", "do": "Preview each LEVER step. Emphasize the critical variable: the ratio of environmental change rate to adaptation speed.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Seven component cards for extinction dynamics model", "say": "Seven factors determine whether a species makes it through a mass extinction. Only one is external — the thing that changed. Everything else is how life responds.", "do": "Guide component sorting. Discuss why Environmental Change Rate is external (the asteroid) while all biological responses are internal.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between extinction components", "say": "When the asteroid hits and food webs collapse, trace what happens to every component. Where does the chain of death begin — and where does survival emerge?", "do": "Help students map the cascade from environmental change through extinction pressure, niche competition collapse, and survival advantage reversal.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and simulation results", "say": "Three scenarios: slow change, catastrophic change, and the aftermath. Watch how completely different the survival rules become when the change rate shifts.", "do": "Students predict outcomes first. Run all three scenarios. Compare which traits win in gradual vs. catastrophic change. Discuss the post-extinction recovery pattern.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model exploration", "say": "The biggest, strongest, most dominant animals died. The small, flexible, generalist survivors inherited the Earth. What does that tell us about our own species?", "do": "Lead discussion connecting extinction dynamics to modern biodiversity crisis. Are humans acting as the asteroid for current species?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Biodiversity resilience index design challenge", "say": "Conservation biologists need to know which species are most at risk RIGHT NOW. Design the scoring system that identifies them before it's too late.", "do": "Groups design resilience indices using model insights. Score real modern species and predict which are most vulnerable. Present and defend rankings.", "time": "12 min"}
    ],
    "sort_reasoning": "Environmental Change Rate is the external component because it represents the catastrophic event (asteroid impact, volcanic eruption, or climate shift) that acts upon the biological system from outside. Species Diversity, Adaptation Speed, Extinction Pressure, Niche Competition, Survival Advantage, and Population Recovery are internal because they are biological and ecological responses determined by the inherent properties of organisms and ecosystems interacting with the changed environment.",
    "relationships": [
        ("Environmental Change Rate to Extinction Pressure", "POSITIVE (+)", "Faster Environmental Change Rate increases Extinction Pressure because organisms have less time to adapt, migrate, or find alternative resources. When change outpaces the biological capacity to respond, populations decline toward extinction."),
        ("Extinction Pressure to Species Diversity", "NEGATIVE (-)", "Higher Extinction Pressure directly reduces Species Diversity as populations that cannot survive the changed conditions decline and disappear. The most specialized species — those tightly adapted to pre-change conditions — are eliminated first."),
        ("Species Diversity to Population Recovery", "POSITIVE (+)", "Greater remaining Species Diversity after the extinction event provides more genetic and ecological raw material for Population Recovery. Surviving lineages with diverse traits and wide ecological tolerances can radiate into empty niches more rapidly.")
    ],
    "sim_answers": [
        ("Gradual Change Scenario", "With slow Environmental Change Rate, Adaptation Speed can track the environmental shift. Species Diversity changes gradually as some species adapt and others are outcompeted, but mass extinction does not occur. Niche Competition adjusts incrementally. The system reaches a new equilibrium without catastrophic loss."),
        ("Asteroid Impact Scenario", "With maximum Environmental Change Rate, the system experiences catastrophic failure. Extinction Pressure overwhelms Adaptation Speed within months — far too fast for evolutionary response. Species Diversity plummets as food webs collapse from the bottom up. Niche Competition becomes irrelevant because resources disappear entirely. Survival Advantage shifts radically from large-dominant to small-generalist traits. Only species pre-adapted to low-resource conditions survive. Population Recovery begins only after environmental conditions stabilize, progressing from opportunistic generalists to specialized forms over millions of years.")
    ],
    "reflection_exemplars": [
        ("Why is being dominant a vulnerability?", "The model shows that dominant species achieve their position through specialization — T. rex was perfectly adapted to being a top predator in a specific food web. But specialization means dependence on specific conditions. When those conditions change catastrophically, the very traits that created dominance (large body size requiring massive food intake, position atop a specific food chain) become fatal liabilities. Generalist species that can eat many things, survive in many conditions, and have low metabolic demands are inherently more resilient to unpredictable change. Dominance is optimization for current conditions; resilience is tolerance of any conditions."),
        ("What parallels exist with the modern extinction crisis?", "The model reveals that the current biodiversity crisis shares a key feature with past mass extinctions: Environmental Change Rate is exceeding Adaptation Speed for many species. Human activity is changing climate, destroying habitat, and altering ecosystems at rates comparable to geological catastrophes. The model predicts that specialist species with small geographic ranges, specific habitat requirements, and slow reproduction rates are most vulnerable — and this matches real-world data. Species like polar bears, coral reef organisms, and tropical forest specialists are declining fastest. The question is whether humans can reduce the Environmental Change Rate before crossing the threshold for a sixth mass extinction.")
    ],
    "stem_intro": "Present the challenge: Conservation biologists need a tool that predicts which modern species are most vulnerable to rapid environmental change — before those species go extinct. Your team will design a Biodiversity Resilience Index using the survival factors identified by your extinction dynamics model.",
    "stem_concepts": [
        ("Extinction Risk Assessment", "The IUCN Red List evaluates species based on population size, rate of decline, geographic range, and habitat fragmentation. Your resilience index would complement this by predicting vulnerability to future rapid change based on biological traits rather than current population status."),
        ("Trait-Based Vulnerability", "Species with specific combinations of traits are more vulnerable to rapid change: specialist diet, large body size, slow reproduction rate, small geographic range, and narrow temperature tolerance. Each of these traits was a disadvantage during past mass extinctions and predicts vulnerability to current environmental changes."),
        ("Functional Redundancy", "Ecosystems with multiple species performing similar ecological functions are more resilient because the loss of one species can be compensated by others. Ecosystems with low functional redundancy are vulnerable to cascading collapse if a key species is lost.")
    ],
    "stem_eval": [
        ("Expert (4)", "Index incorporates multiple biological traits, weights factors based on model evidence, accounts for ecological interdependencies, has been tested on real species data, and includes clear vulnerability thresholds"),
        ("Proficient (3)", "Index scores species on relevant biological traits with reasonable weighting and some connection to model findings"),
        ("Developing (2)", "Index includes some relevant traits but weighting is arbitrary or not connected to extinction dynamics model"),
        ("Beginning (1)", "Index is incomplete or does not connect species traits to survival factors identified by the model")
    ],
    "support": [
        "Provide species profile cards with key trait data (body size, diet breadth, geographic range, reproductive rate) for students to score",
        "Use a visual comparison chart showing pre-extinction dominant species versus surviving species to identify key survival traits",
        "Sentence frames: 'When Environmental Change Rate exceeds Adaptation Speed, species with __ are more vulnerable because __, while species with __ survive because __'"
    ],
    "extensions": [
        "Research the 'Big Five' mass extinctions and compare the Environmental Change Rate and survival patterns in each — are the same traits always advantageous?",
        "Investigate the concept of 'extinction debt' — species that are functionally extinct but haven't died yet because their decline is slow — and model how this affects biodiversity projections",
        "Compare the K-Pg mass extinction to the current 'Sixth Extinction' being driven by human activity and calculate whether the current species loss rate qualifies as a mass extinction event"
    ],
    "cross_curr": [
        ("Math", "Calculate extinction rates during the K-Pg event (75% species loss in ~100,000 years) and compare to current rates of species loss to determine whether we are experiencing a sixth mass extinction"),
        ("ELA", "Write a narrative from the perspective of a paleontologist discovering the K-Pg boundary layer and the iridium anomaly, connecting evidence to the asteroid impact hypothesis"),
        ("Social Studies", "Research and debate whether humans have a moral obligation to prevent species extinction, considering both ecological and economic arguments")
    ],
    "misconceptions": [
        ("Dinosaurs went extinct because they were inferior", "Dinosaurs were extraordinarily successful organisms that dominated Earth for 165 million years — far longer than mammals have been dominant. They didn't go extinct because of evolutionary inferiority but because a 10-kilometer asteroid changed the environment faster than any organism could adapt. The same event would extinguish most modern species if it happened today.", "Perspective check: Humans have existed for 200,000 years. Dinosaurs existed for 165 million years. Who is the more 'successful' group by any objective measure of evolutionary longevity?"),
        ("Evolution can save a species from any threat", "Natural selection can only operate as fast as organisms can reproduce and transmit genetic changes to offspring. When environmental change occurs in months (asteroid impact) but adaptation requires thousands to millions of generations, evolution is powerless. There is a fundamental speed limit to adaptive evolution set by generation time, population size, and the magnitude of change required.", "Math it out: If a large dinosaur has a generation time of 20 years and needs 1,000 generations to adapt to new conditions, adaptation requires 20,000 years. The post-impact winter lasted 3-10 years. Evolution lost that race before it started."),
        ("All dinosaurs went extinct", "Birds ARE dinosaurs — specifically, they are the surviving lineage of theropod dinosaurs. Modern birds descended from small, feathered dinosaurs that survived the K-Pg extinction. With over 10,000 species, dinosaurs are actually among the most diverse vertebrate groups alive today. When you see a pigeon, you are seeing a dinosaur.", "Show the cladogram: trace the evolutionary lineage from theropod dinosaurs through Archaeopteryx to modern birds. The 'birds are dinosaurs' statement isn't a metaphor — it's phylogenetic fact.")
    ]
}

L06 = {
    "id": "G10L2-L06",
    "title": "How Does 5G Actually Work?",
    "subtitle": "Modeling Electromagnetic Wave Behavior in Wireless Communication Networks",
    "ngss": "HS-PS4-2, HS-PS4-3",
    "ngss_desc": "Evaluate questions about the advantages of using digital transmission and storage of information. Evaluate the claims, evidence, and reasoning behind the idea that electromagnetic radiation can be described either by a wave model or a particle model.",
    "big_question": "Why does 5G promise lightning-fast internet but struggle to work through walls — and what trade-offs did engineers have to make?",
    "objectives": [
        "Model how signal frequency, wave penetration, and tower density interact to determine wireless network performance",
        "Analyze the fundamental trade-off between data transfer rate and signal penetration in electromagnetic wave communication",
        "Predict how interference, absorption, and network capacity change as frequency increases from 4G to 5G ranges",
        "Evaluate the engineering compromises required to build a high-speed, wide-coverage wireless network"
    ],
    "vocabulary": [
        ("Millimeter Wave", "Electromagnetic waves with frequencies between 30 GHz and 300 GHz, corresponding to wavelengths of 1-10 millimeters — 5G uses these frequencies for their enormous data capacity but they are easily blocked by buildings, trees, and even rain"),
        ("Signal Attenuation", "The reduction in electromagnetic signal strength as it travels through space, caused by distance (inverse square law), absorption by materials, atmospheric scattering, and interference from other signals"),
        ("MIMO Antenna Array", "Multiple-Input Multiple-Output technology that uses dozens or hundreds of small antennas to simultaneously transmit and receive multiple data streams, dramatically increasing network capacity and reliability"),
        ("Beamforming", "A signal processing technique that focuses electromagnetic energy into narrow, directed beams aimed at specific users rather than broadcasting in all directions, improving signal strength and reducing interference")
    ],
    "components": [
        ("Signal Frequency", "The frequency of electromagnetic waves used for data transmission — higher frequencies (millimeter wave) carry more data but are absorbed more easily by obstacles and atmosphere", True),
        ("Wave Penetration", "The ability of electromagnetic waves to pass through solid materials like walls, glass, and vegetation — inversely related to frequency, with higher frequencies being blocked more easily", False),
        ("Data Transfer Rate", "The volume of digital information that can be transmitted per second, measured in megabits or gigabits per second — directly proportional to bandwidth, which increases with signal frequency", False),
        ("Tower Density", "The number of cell towers or small cells per square kilometer needed to maintain coverage — must increase dramatically as frequency increases because each tower covers a smaller area", True),
        ("Interference Level", "The degree to which signals from neighboring towers, devices, and environmental reflections degrade signal quality, requiring error correction and reducing effective throughput", False),
        ("Energy Absorption", "The rate at which electromagnetic energy is absorbed by atmospheric gases, water vapor, building materials, vegetation, and human tissue as signals propagate from tower to device", False),
        ("Network Capacity", "The total volume of data that can be simultaneously served to all users in a coverage area, determined by the interaction of frequency, tower density, MIMO technology, and interference management", False)
    ],
    "think_about_it": "When Signal Frequency increases to millimeter wave ranges, Data Transfer Rate skyrockets — but Wave Penetration collapses and Energy Absorption increases. Tower Density must increase enormously to compensate. How do engineers balance this fundamental trade-off between speed and coverage?",
    "scenarios": [
        ("4G Standard", "Set Signal Frequency to 700 MHz (4G range) — observe the balance of Data Transfer Rate, Wave Penetration, and Tower Density requirements"),
        ("5G Millimeter Wave", "Set Signal Frequency to 28 GHz (5G mmWave) — observe the dramatic shift in all components"),
        ("5G Mid-Band Compromise", "Set Signal Frequency to 3.5 GHz (5G mid-band) — observe how the compromise between speed and coverage works")
    ],
    "sim_scenarios": [
        ("4G Standard", "Low frequency, wide coverage", "What do you predict happens to Wave Penetration and Tower Density when operating at 700 MHz?"),
        ("5G Millimeter Wave", "High frequency, narrow coverage", "What do you predict happens to Data Transfer Rate and Wave Penetration when frequency jumps to 28 GHz?"),
        ("5G Mid-Band", "Medium frequency, balanced approach", "Do you predict the mid-band compromise provides enough speed improvement while maintaining reasonable coverage?")
    ],
    "discoveries": [
        "There is a fundamental physics trade-off in wireless communication: higher frequencies carry more data but penetrate materials less effectively and are absorbed more by the atmosphere",
        "5G millimeter wave delivers extraordinary data rates (10+ Gbps) but requires a massive increase in Tower Density because each cell covers only 200-300 meters versus 2-5 kilometers for 4G",
        "Interference Level increases with Tower Density, requiring sophisticated beamforming and MIMO technology to direct signals precisely and manage overlapping coverage",
        "The 'best' 5G solution is actually a layered network using multiple frequency bands — low-band for wide coverage, mid-band for urban areas, and millimeter wave for dense hotspots"
    ],
    "answer": "5G works by transmitting data on higher electromagnetic frequencies than 4G — up to 28-39 GHz (millimeter wave) compared to 4G's 700 MHz to 2.5 GHz. Higher frequencies carry vastly more data because bandwidth is proportional to frequency. But physics creates an inescapable trade-off: as frequency increases, electromagnetic waves are increasingly blocked by walls, trees, glass, rain, and even human bodies. A 28 GHz signal loses 98% of its energy passing through a single brick wall. This means 5G millimeter wave requires a cell tower (or small cell) every 200-300 meters instead of every 2-5 kilometers. The engineering solution is a layered network: low-band 5G for wide coverage, mid-band for cities, and millimeter wave for stadiums, airports, and dense urban areas where demand is highest.",
    "stem_title": "Design a Campus 5G Network",
    "stem_mission": "Design the placement and frequency strategy for a 5G network covering a school campus, optimizing for both coverage and capacity while managing interference.",
    "stem_scenario": "Your school district is deploying a 5G network across campus to support 2,000 simultaneous device connections for digital learning. The network must work inside classrooms, in outdoor spaces, and in the auditorium during events. Your team has been hired to design the antenna placement and frequency strategy.",
    "stem_questions": [
        "Which areas of campus need millimeter wave coverage (high density) versus mid-band coverage (general use)?",
        "How will you ensure signal penetrates into classrooms through walls and windows?",
        "What happens to your network during a school assembly when 2,000 devices are in one room?"
    ],
    "stem_design_qs": [
        "Where would you place small cells for millimeter wave coverage and macro cells for wide coverage?",
        "How would you use beamforming to direct signals to classroom areas without creating dead zones?",
        "What frequency mix would balance speed, coverage, and cost for the campus budget?",
        "How would you test your network design before installation using your model data?"
    ],
    "career": "RF Engineers (Radio Frequency Engineers) design wireless communication systems, optimizing antenna placement, frequency selection, and interference management. They work for telecom companies, tech firms, and government agencies, earning $80,000–$150,000/year. Network Architects who design large-scale wireless infrastructure earn $100,000–$180,000/year.",
    "images": {
        "cover": ("G10L2-L06-cover.png", "A photorealistic, cinematic image of a modern cityscape with visible electromagnetic wave patterns emanating from small cell towers on building tops and light poles, showing how waves interact with buildings and obstacles, futuristic visualization with blue and purple wave graphics overlaid on realistic urban architecture"),
        "landscape": ("G10L2-L06-landscape.png", "A diverse group of 15-16 year old students in a modern physics lab experimenting with radio frequency equipment and signal strength meters, wave diagrams on the whiteboard, engaged expressions as they measure signals, natural classroom lighting"),
        "modeling": ("G10L2-L06-modeling.png", "A diverse group of 15-16 year old students working on laptops building computational models of wireless network coverage, screens showing signal propagation maps and frequency-penetration graphs, modern classroom with electromagnetic spectrum posters"),
        "discussion": ("G10L2-L06-discussion.png", "A teacher leading an animated discussion with diverse 15-16 year old students about electromagnetic wave behavior, a diagram comparing low-frequency and high-frequency signal propagation displayed on a smartboard, students raising hands"),
        "stem": ("G10L2-L06-stem.png", "Diverse 15-16 year old students designing campus network layout plans with building maps and antenna placement diagrams on large displays, collaborative atmosphere with RF equipment and signal testing tools visible")
    },
    "pre_assessment": [
        "What do you think makes 5G different from 4G — and why is it faster?",
        "Why do you think your phone signal gets worse inside certain buildings?",
        "Draw a diagram showing how you think a signal travels from a cell tower to your phone.",
        "What trade-offs do you think engineers have to make when designing a wireless network?"
    ],
    "extend_components": [
        ("Beamforming Precision", "The ability of MIMO antenna arrays to focus electromagnetic energy into narrow beams directed at specific users, improving signal-to-noise ratio and allowing multiple users to share the same frequency without interference"),
        ("Weather Impact", "The effect of rain, snow, humidity, and atmospheric conditions on signal propagation — millimeter waves are particularly susceptible to rain fade, where water droplets absorb and scatter the signal"),
        ("Latency", "The time delay between transmitting and receiving a signal, measured in milliseconds — 5G promises 1ms latency versus 30-50ms for 4G, enabling real-time applications like autonomous vehicles and remote surgery")
    ],
    "reflections": [
        "How does your model demonstrate the fundamental trade-off between data speed and signal penetration in electromagnetic communication?",
        "Why does increasing Signal Frequency require such a dramatic increase in Tower Density — what does this reveal about wave physics?",
        "What does your model suggest about why 5G networks use multiple frequency bands instead of one?",
        "How does Interference Level change as Tower Density increases, and what engineering solutions address this challenge?",
        "What are the limitations of modeling wireless network behavior with only seven components when real networks involve terrain, weather, and thousands of simultaneous users?"
    ],
    "dimensions": [
        ("Science Practice", "Evaluating Claims and Evidence", "Students evaluate claims about 5G performance by building computational models that reveal the physics-based trade-offs between frequency, penetration, and coverage."),
        ("Disciplinary Core Idea", "PS4.A Wave Properties / PS4.C Information Technologies and Instrumentation", "Electromagnetic waves transport energy and information; wave frequency determines both data capacity and interaction with matter, creating fundamental engineering trade-offs."),
        ("Crosscutting Concept", "Structure and Function", "Students analyze how the physical structure of electromagnetic waves (frequency, wavelength) determines their functional properties (data capacity, penetration, absorption) and constrains network design.")
    ],
    "cast_items": [
        "Model how electromagnetic wave frequency determines the trade-off between data transfer rate and signal penetration",
        "Analyze the engineering compromises in 5G network design between coverage area, capacity, and infrastructure cost",
        "Evaluate claims about 5G performance using computational model evidence"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A 5G tower using 28 GHz millimeter wave covers approximately 200 meters, while a 4G tower at 700 MHz covers 5 kilometers. Based on your model, how many 5G small cells would be needed to replace one 4G tower's coverage area?"),
        ("Constructed Response:", "Using your model, explain why 5G promises much faster speeds than 4G but requires dramatically more cell towers. Reference the relationship between Signal Frequency, Wave Penetration, Data Transfer Rate, and Tower Density in your explanation.")
    ],
    "background_intro": "Every time you stream a video, send a text, or scroll social media, you're using electromagnetic waves traveling at the speed of light between your device and a cell tower. The evolution from 4G to 5G represents a fundamental shift in which electromagnetic frequencies we use — and understanding why higher frequencies mean faster speeds but shorter range reveals the core physics of wireless communication.",
    "background_sections": [
        ("The Electromagnetic Spectrum and Data", "All wireless communication uses electromagnetic waves — the same fundamental phenomenon as visible light, radio waves, and X-rays, differing only in frequency. Data is encoded by modulating the wave's amplitude, frequency, or phase. The amount of data a wave can carry is directly proportional to its bandwidth (the range of frequencies used). Higher carrier frequencies allow wider bandwidths. A 28 GHz millimeter wave channel can be 400 MHz wide (carrying 10+ Gbps), while a 700 MHz 4G channel is typically 20 MHz wide (carrying 100 Mbps). This is why 5G is faster — it uses higher frequencies with wider channels."),
        ("The Penetration Problem", "Electromagnetic waves interact with matter in frequency-dependent ways. Low-frequency waves (700 MHz, wavelength ~43 cm) can diffract around obstacles and penetrate building materials with moderate loss. High-frequency millimeter waves (28 GHz, wavelength ~1 cm) are absorbed and reflected by most solid materials. A 28 GHz signal loses approximately 40 dB passing through a concrete wall — that's 99.99% energy loss. Even glass windows, tree foliage, and rain attenuate millimeter waves significantly. This is a consequence of the wave's wavelength being similar in size to common obstacles, maximizing interaction."),
        ("Small Cells and Densification", "Because millimeter wave signals cover only 200-300 meters (versus 2-5 km for 4G), 5G requires network densification — deploying many small cell antennas on light poles, building facades, and utility poles rather than relying on a few large towers. A single city block might need 4-6 small cells for millimeter wave coverage. This creates challenges: more antennas mean more interference between cells, more power consumption, more installation costs, and more community resistance to antenna proliferation."),
        ("The Layered Solution", "Real 5G networks don't use one frequency — they layer three bands. Low-band (600-900 MHz) provides wide coverage similar to 4G with modest speed improvements. Mid-band (2.5-6 GHz) offers a balance of coverage and speed for urban areas — this is where most users experience 5G. Millimeter wave (24-100 GHz) provides extreme speed in dense locations like stadiums, airports, and downtown areas. Your phone automatically switches between bands based on availability. This layered approach is an engineering compromise that maximizes the strengths of each frequency range.")
    ],
    "lever_L": "Students identify seven components of the 5G network system: Signal Frequency, Wave Penetration, Data Transfer Rate, Tower Density, Interference Level, Energy Absorption, and Network Capacity — with Signal Frequency and Tower Density as external engineering choices.",
    "lever_E": "Students determine that increasing Signal Frequency dramatically increases Data Transfer Rate but decreases Wave Penetration and increases Energy Absorption. This forces higher Tower Density, which increases Interference Level. Net Network Capacity depends on balancing all these trade-offs.",
    "lever_V": "Students build a computational model showing how frequency selection cascades through all network parameters, revealing the fundamental physics trade-off in wireless communication.",
    "lever_Ev": "Students run 4G standard, 5G millimeter wave, and 5G mid-band scenarios to compare data speed, coverage area, and infrastructure requirements for each frequency strategy.",
    "lever_R": "Students add Beamforming Precision, Weather Impact, or Latency to explore how advanced antenna technology and environmental conditions affect network performance.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with futuristic 5G cityscape visualization", "say": "5G promises to download a movie in three seconds. But walk behind a wall and the signal vanishes. Why? The answer is pure physics.", "do": "Demo: If possible, compare signal strength between 4G and 5G in the classroom using a signal strength app. If not, show a signal propagation comparison video.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary terms", "say": "Today you're learning the physics behind every text, every stream, every download — and why engineers had to make painful trade-offs to give you faster internet.", "do": "Have students read objectives. Pre-teach 'millimeter wave' and 'signal attenuation.' Quick-write: Why do you think 5G is faster than 4G?", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why does 5G struggle to work through walls?", "say": "You'd think faster internet is just about better technology. But it's actually about physics — and physics doesn't negotiate.", "do": "Students guess: What happens when you double the frequency of a wave? What happens to its ability to go through walls? Collect hypotheses.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're going to model the electromagnetic physics behind wireless networks — and discover why engineers have to compromise between speed and coverage.", "do": "Preview each LEVER step. Emphasize that this is about the physics of electromagnetic waves interacting with matter.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Seven component cards for wireless network model", "say": "Two things the engineers choose: what frequency to broadcast on and how many towers to build. Physics determines the rest.", "do": "Guide component sorting. Discuss why Signal Frequency and Tower Density are external (engineering choices) while Wave Penetration and Energy Absorption are governed by physics.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between network components", "say": "When you crank up the frequency for more speed, what chain reaction ripples through every other component of the network?", "do": "Help students trace the trade-off cascade: higher frequency means more data but less penetration, requiring more towers, creating more interference. Find the balance points.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and simulation results for three frequency bands", "say": "Let's compare 4G, 5G mid-band, and 5G millimeter wave. Same city, same users, completely different physics.", "do": "Students predict outcomes for each frequency band. Run simulations. Compare tower counts, coverage gaps, and data speeds side by side.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model exploration", "say": "Now you know why there's no perfect wireless solution — only trade-offs. The real genius of 5G is using ALL the frequencies and switching between them.", "do": "Lead discussion on the layered network approach. Connect model findings to students' real experience with cell signal variability.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Campus 5G network design challenge", "say": "Your school just got funding for a 5G network. Design it. Where do the antennas go? What frequencies do you use? And what happens during the school assembly?", "do": "Groups design campus networks using model data. Must specify antenna locations, frequency bands, and capacity for high-density events. Present as engineering proposals.", "time": "12 min"}
    ],
    "sort_reasoning": "Signal Frequency and Tower Density are external components because they represent deliberate engineering decisions made by network designers — choosing which electromagnetic frequencies to use and how many cell towers to deploy. Wave Penetration, Data Transfer Rate, Interference Level, Energy Absorption, and Network Capacity are internal because they are physical consequences determined by the laws of electromagnetic wave propagation interacting with the chosen frequency and infrastructure density.",
    "relationships": [
        ("Signal Frequency to Data Transfer Rate", "POSITIVE (+)", "Higher Signal Frequency allows wider bandwidth channels, which can carry proportionally more data per second. Doubling the frequency roughly doubles the available bandwidth and data capacity."),
        ("Signal Frequency to Wave Penetration", "NEGATIVE (-)", "Higher Signal Frequency produces shorter wavelengths that interact more strongly with building materials, vegetation, and atmospheric particles. Millimeter waves at 28 GHz lose 99.99% of energy through a concrete wall, while 700 MHz signals pass with moderate attenuation."),
        ("Tower Density to Interference Level", "POSITIVE (+)", "Higher Tower Density means more overlapping signals in the same geographic area. Without sophisticated interference management (beamforming, MIMO), signals from adjacent cells degrade each other, reducing effective Data Transfer Rate and Network Capacity.")
    ],
    "sim_answers": [
        ("4G Standard Scenario", "At 700 MHz, Wave Penetration is high — signals easily pass through walls and travel 2-5 km from towers. Tower Density can be low, keeping infrastructure costs manageable. But Data Transfer Rate is limited by the narrow bandwidth available at low frequencies — typically 50-100 Mbps peak. Network Capacity is adequate for current demand but insufficient for future bandwidth-intensive applications."),
        ("5G Millimeter Wave Scenario", "At 28 GHz, Data Transfer Rate skyrockets to 10+ Gbps — fast enough to download a full movie in seconds. But Wave Penetration collapses: signals cannot pass through walls, are blocked by trees, and are attenuated by rain. Each cell covers only 200-300 meters, requiring enormous Tower Density. Interference Level becomes a major challenge requiring advanced beamforming. Network Capacity is extraordinary within coverage areas but coverage gaps are pervasive.")
    ],
    "reflection_exemplars": [
        ("Why can't engineers just use the highest frequency?", "The model reveals a fundamental physics constraint: electromagnetic wave penetration decreases as frequency increases. This isn't an engineering limitation that can be overcome with better technology — it's a property of how electromagnetic waves interact with matter at the atomic level. Higher-frequency waves have shorter wavelengths that match the size of common obstacles (walls, rain drops, leaves), maximizing absorption and scattering. Engineers must work within these physics constraints, which is why the solution is a layered network using multiple frequencies rather than one 'best' frequency."),
        ("How does the 5G trade-off relate to the electromagnetic spectrum?", "The model demonstrates a universal principle: every region of the electromagnetic spectrum has trade-offs. Radio waves penetrate walls but carry little data. Microwaves carry more data but are partially blocked. Millimeter waves carry enormous data but are blocked by almost everything. X-rays penetrate everything but are too energetic for communication. This trade-off is fundamental to wave physics — there is no frequency that combines high data capacity with high penetration. The engineering challenge is designing systems that navigate this constraint.")
    ],
    "stem_intro": "Present the challenge: Your school is deploying a 5G network for 2,000 students. Design the antenna placement and frequency strategy that provides coverage in classrooms, outdoor spaces, and the auditorium — using your model data to justify every engineering decision.",
    "stem_concepts": [
        ("Coverage Mapping", "Network engineers create coverage maps showing signal strength at every point in the target area, accounting for building materials, terrain, and antenna characteristics. Dead zones — areas with insufficient signal — must be identified and addressed with additional antennas or frequency adjustments."),
        ("Capacity Planning", "Networks must handle peak demand, not just average demand. A school assembly with 2,000 devices in one room requires vastly more capacity than normal distributed usage. Capacity planning uses traffic models to predict demand patterns and ensure the network can handle worst-case scenarios."),
        ("Cost-Benefit Analysis", "Every additional antenna improves coverage but increases cost. Engineers must optimize the trade-off between network performance and budget. Millimeter wave small cells cost $10,000-$30,000 each including installation, so placement must be strategic, not blanket coverage.")
    ],
    "stem_eval": [
        ("Expert (4)", "Network design uses multiple frequency bands strategically, includes coverage maps with dead zone analysis, accounts for peak capacity scenarios, optimizes antenna placement using model data, and includes cost estimate"),
        ("Proficient (3)", "Network design includes reasonable antenna placement and frequency selection with some model-based justification for coverage decisions"),
        ("Developing (2)", "Network design includes antenna placement but lacks frequency strategy, coverage analysis, or capacity planning"),
        ("Beginning (1)", "Network design is incomplete or does not connect antenna placement to electromagnetic wave physics")
    ],
    "support": [
        "Provide a simplified campus map showing building outlines, wall materials, and key gathering areas for students to plan antenna placement",
        "Use a frequency-penetration chart showing signal loss through common materials (drywall, concrete, glass, vegetation) at different frequencies",
        "Sentence frames: 'At __ GHz, the signal can/cannot penetrate __ because __, so we need to place antennas at __ to ensure coverage'"
    ],
    "extensions": [
        "Research how 5G millimeter wave technology is being used in fixed wireless access to provide home internet without cable, and model whether this could replace fiber optic connections",
        "Investigate the physics of beamforming — how antenna arrays create focused beams — and explain why this technology is essential for making millimeter wave 5G practical",
        "Compare the electromagnetic frequency allocations used by different countries for 5G and analyze why spectrum policy is a matter of national economic competition"
    ],
    "cross_curr": [
        ("Math", "Calculate the number of small cells needed to provide millimeter wave coverage to a 10 square kilometer urban area, accounting for 200-meter cell radius and 15% overlap for handoff zones"),
        ("ELA", "Evaluate competing claims about 5G health effects by analyzing the scientific evidence, electromagnetic energy levels, and the difference between ionizing and non-ionizing radiation"),
        ("Social Studies", "Research the digital divide — how unequal access to high-speed internet affects educational and economic opportunity — and analyze whether 5G will narrow or widen this gap")
    ],
    "misconceptions": [
        ("5G is dangerous to human health", "5G uses non-ionizing electromagnetic radiation — the same fundamental type as FM radio, Wi-Fi, and visible light. Non-ionizing radiation does not have enough energy per photon to break chemical bonds or damage DNA. The frequencies used by 5G (up to 39 GHz) are far below the ionizing threshold (approximately 3,000,000 GHz for UV light). Decades of research have found no confirmed health effects from non-ionizing radiation at the power levels used by cell networks.", "Calculate: Compare the photon energy of a 28 GHz 5G signal to a 500,000 GHz visible light photon. Visible light is 18,000 times more energetic per photon — and we evolved under constant visible light exposure."),
        ("5G is just faster 4G", "5G is not simply 4G with higher speeds — it represents a fundamental architectural change in wireless networks. 5G introduces network slicing (dedicating virtual network segments to different applications), massive MIMO (hundreds of antennas per tower), edge computing (processing data near the user rather than in distant data centers), and ultra-low latency (1ms vs 30-50ms). These capabilities enable entirely new applications like autonomous vehicles, remote surgery, and industrial automation that were impossible on 4G.", "Analogy: 4G is like a highway — it can carry more or fewer cars. 5G is like redesigning the entire transportation system with highways, railways, bike lanes, and air taxis, each optimized for different needs."),
        ("Higher frequency always means better performance", "The model demonstrates that higher frequency increases data rate but simultaneously decreases coverage area, increases infrastructure costs, and introduces vulnerability to weather and obstacles. There is no universally 'better' frequency — each range offers different trade-offs. The optimal frequency depends on the specific use case: low-band for rural coverage, mid-band for suburban areas, and millimeter wave for dense urban hotspots.", "Test it: Ask students whether they'd rather have extremely fast internet that works only outdoors within 200 meters of a tower, or moderately fast internet that works everywhere including inside buildings. Neither answer is 'wrong' — it depends on the use case.")
    ]
}

L07 = {
    "id": "G10L2-L07",
    "title": "Why Does a Glow Stick Stop Glowing?",
    "subtitle": "Modeling Chemical Kinetics and Energy Transformation in Chemiluminescence",
    "ngss": "HS-PS1-4, HS-PS1-6",
    "ngss_desc": "Develop a model to illustrate that the release or absorption of energy from a chemical reaction system depends upon the changes in total bond energy. Refine the design of a chemical system by specifying a change in conditions that would produce increased amounts of a product at equilibrium.",
    "big_question": "Why does a glow stick glow brighter when you heat it up, dimmer when you cool it — and why does it eventually stop glowing entirely?",
    "objectives": [
        "Model how chemical concentration, temperature, and reaction rate interact to determine the intensity and duration of chemiluminescent light output",
        "Analyze why temperature accelerates reaction rate while simultaneously shortening the total glow duration",
        "Predict the conditions that maximize total light output versus peak brightness versus glow duration",
        "Evaluate the relationship between energy dissipation and product buildup in determining when a chemical reaction stops"
    ],
    "vocabulary": [
        ("Chemiluminescence", "The emission of light as a product of a chemical reaction without requiring heat input — energy stored in chemical bonds is converted directly to photons when specific molecules undergo reaction"),
        ("Activation Energy", "The minimum energy that reacting molecules must possess for a chemical reaction to occur — temperature increases the fraction of molecules that exceed this threshold, accelerating the reaction"),
        ("Reaction Kinetics", "The study of how fast chemical reactions occur and what factors affect the rate — including concentration of reactants, temperature, catalysts, and surface area"),
        ("Chemical Equilibrium", "The state in which the forward and reverse reactions occur at equal rates, resulting in no net change in concentrations — in a glow stick, equilibrium is approached as reactants are consumed and products accumulate")
    ],
    "components": [
        ("Chemical Concentration", "The amount of unreacted chemical reagents remaining in the glow stick — primarily diphenyl oxalate and hydrogen peroxide — which decreases as the reaction proceeds", False),
        ("Temperature", "The thermal energy of the chemical system, which determines the kinetic energy of molecules and the fraction that exceeds the activation energy threshold for reaction", True),
        ("Reaction Rate", "The speed at which reactant molecules collide with sufficient energy and proper orientation to undergo the chemiluminescent reaction, measured in moles converted per second", False),
        ("Fluorescent Dye Activation", "The rate at which high-energy intermediate molecules transfer energy to fluorescent dye molecules, exciting their electrons to higher energy states from which they emit visible light photons", False),
        ("Light Output", "The intensity of visible light emitted by the glow stick, measured in lumens — directly proportional to the rate of fluorescent dye activation events", False),
        ("Energy Dissipation", "The loss of chemical energy as heat rather than light during side reactions and molecular collisions, representing inefficiency in the energy conversion process", False),
        ("Product Buildup", "The accumulation of reaction products (phenol and CO2) which dilute the remaining reactants and shift the system toward chemical equilibrium, progressively slowing the reaction", False)
    ],
    "think_about_it": "When Temperature increases, Reaction Rate increases dramatically — producing brighter Light Output. But faster Reaction Rate also means Chemical Concentration decreases faster. The glow stick runs out of fuel sooner. Is there an optimal temperature that maximizes the TOTAL light produced rather than just peak brightness?",
    "scenarios": [
        ("Room Temperature", "Set Temperature to 25 degrees Celsius — observe the standard glow duration and intensity over time"),
        ("Hot Water Bath", "Set Temperature to 60 degrees Celsius — observe the dramatic increase in brightness followed by rapid fading"),
        ("Freezer Storage", "Set Temperature to -10 degrees Celsius — observe the dim but extremely long-lasting glow")
    ],
    "sim_scenarios": [
        ("Room Temperature", "Standard conditions, 25 degrees C", "What do you predict happens to Light Output over the full lifespan of a glow stick at room temperature?"),
        ("Hot Water Bath", "Elevated temperature, 60 degrees C", "What do you predict happens to peak Light Output and total glow duration when temperature is doubled?"),
        ("Freezer Storage", "Low temperature, -10 degrees C", "Do you predict that a cold glow stick produces the same total light as a warm one — just more slowly?")
    ],
    "discoveries": [
        "Temperature is the master controller of reaction rate — doubling the temperature approximately doubles the rate because more molecules exceed the activation energy threshold",
        "There is a fundamental trade-off between brightness and duration: heating a glow stick makes it brighter but shorter-lived because the same chemical fuel is consumed faster",
        "Product Buildup creates a negative feedback loop — as products accumulate, they dilute the reactants and slow the reaction, causing the gradual dimming observed in all glow sticks",
        "Total light output is roughly constant regardless of temperature — a hot glow stick and a cold glow stick convert approximately the same total chemical energy to light, just at different rates"
    ],
    "answer": "A glow stick glows because of chemiluminescence — a chemical reaction that converts bond energy directly into light. When you snap a glow stick, you break an internal glass vial that mixes hydrogen peroxide with diphenyl oxalate. The reaction produces a high-energy intermediate that transfers energy to fluorescent dye molecules, which emit visible light. The glow stick stops glowing because the reactants are consumed — Chemical Concentration drops to near zero and Product Buildup shifts the system toward equilibrium. Temperature controls HOW the reaction proceeds: heating makes molecules move faster, increasing collision rates and producing brighter light — but it also exhausts the reactants faster. Cooling slows everything down, producing dimmer light that lasts much longer. The total light energy is approximately the same either way because it's determined by the amount of chemical fuel, not the rate of consumption.",
    "stem_title": "Design an Optimized Emergency Light Stick",
    "stem_mission": "Design a chemiluminescent light source optimized for a specific emergency scenario — maximizing either brightness, duration, or total visibility based on mission requirements.",
    "stem_scenario": "A search-and-rescue equipment company needs light sticks for three different scenarios: maritime distress signals (maximum brightness for 30 minutes), camping emergency lighting (moderate brightness for 12+ hours), and underwater cave markers (dim but visible for 48+ hours). Your team must design the chemical formulation and temperature management strategy for each.",
    "stem_questions": [
        "How would you adjust chemical concentration and temperature to optimize for brightness versus duration?",
        "What role does the choice of fluorescent dye play in the color and efficiency of light output?",
        "How would you design a light stick that changes color to indicate when chemical concentration is running low?"
    ],
    "stem_design_qs": [
        "What reactant concentrations would you use for the 30-minute versus 48-hour light stick?",
        "How could you incorporate a thermal management system to control glow rate in field conditions?",
        "What packaging modifications would help maintain optimal temperature in maritime versus cave environments?",
        "How would you test and validate your designs using model predictions before manufacturing prototypes?"
    ],
    "career": "Chemical Engineers design chemical processes and products for manufacturing, including specialty chemicals, materials, and consumer products. They work in industries from pharmaceuticals to energy, earning $75,000–$140,000/year. Photochemists who study light-producing chemical reactions earn $65,000–$130,000/year.",
    "images": {
        "cover": ("G10L2-L07-cover.png", "A photorealistic, cinematic close-up image of multiple glow sticks in different colors (green, blue, pink, yellow) illuminating a dark environment, showing the chemical glow in vivid detail with light reflecting off surrounding surfaces, dramatic low-light photography with sharp focus on the luminous tubes"),
        "landscape": ("G10L2-L07-landscape.png", "A diverse group of 15-16 year old students in a dimly lit chemistry lab conducting glow stick experiments in beakers of hot and cold water, the colorful glow illuminating their fascinated faces, lab equipment visible, dramatic lighting from the chemiluminescent reactions"),
        "modeling": ("G10L2-L07-modeling.png", "A diverse group of 15-16 year old students working on laptops building computational models of chemical kinetics, screens showing reaction rate curves and concentration graphs, modern chemistry classroom with molecular model kits and periodic table"),
        "discussion": ("G10L2-L07-discussion.png", "A teacher leading an animated discussion with diverse 15-16 year old students about energy transformation in chemical reactions, an energy diagram showing activation energy and bond energy changes displayed on a smartboard, students actively engaged"),
        "stem": ("G10L2-L07-stem.png", "Diverse 15-16 year old students designing emergency light stick prototypes with chemical formulation charts and optimization graphs on their tables, collaborative atmosphere with chemistry lab equipment and glow stick samples visible")
    },
    "pre_assessment": [
        "What do you think makes a glow stick glow — and why does it eventually stop?",
        "Why does putting a glow stick in hot water make it glow brighter? What happens when you put it in the freezer?",
        "Draw a diagram showing what you think is happening at the molecular level inside a glowing glow stick.",
        "What is the relationship between temperature and chemical reaction speed?"
    ],
    "extend_components": [
        ("Catalyst Presence", "A substance that lowers the activation energy of the reaction without being consumed, allowing the reaction to proceed faster at any given temperature — some glow stick formulations include catalysts to enhance initial brightness"),
        ("Dye Quantum Yield", "The efficiency of the fluorescent dye in converting chemical excitation energy into visible light photons versus heat — higher quantum yield means more light per unit of chemical reaction"),
        ("Solvent Viscosity", "The resistance of the liquid medium to molecular movement, which affects how quickly reactant molecules can diffuse and collide — lower viscosity at higher temperatures contributes to faster reaction rates")
    ],
    "reflections": [
        "How does your model demonstrate the relationship between activation energy and temperature in determining reaction rate?",
        "Why is the trade-off between brightness and duration a fundamental constraint rather than an engineering limitation that could be overcome?",
        "What does your model predict about total light output at different temperatures — does a hot glow stick produce more total light than a cold one?",
        "How does Product Buildup create a negative feedback loop that gradually extinguishes the glow stick?",
        "What are the limitations of modeling chemiluminescence with only seven components when real glow stick chemistry involves dozens of intermediate reactions?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model of chemiluminescent reaction kinetics to predict how temperature and concentration changes affect light output intensity and duration."),
        ("Disciplinary Core Idea", "PS1.B Chemical Reactions / PS1.A Structure and Properties of Matter", "Chemical reactions involve the breaking and forming of bonds with associated energy changes; the rate of reactions depends on temperature, concentration, and molecular properties."),
        ("Crosscutting Concept", "Energy and Matter: Flows, Cycles, and Conservation", "Students trace energy transformation from chemical bond energy through molecular excitation to visible light emission, accounting for energy conservation and dissipation as heat.")
    ],
    "cast_items": [
        "Model how temperature and chemical concentration interact to determine chemiluminescent reaction rate and light output",
        "Analyze the trade-off between peak brightness and total glow duration as a function of temperature",
        "Predict the time course of chemical concentration, reaction rate, and light output over a glow stick's lifespan"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student places identical glow sticks in hot water (60 degrees C) and cold water (5 degrees C). After 30 minutes, which glow stick has produced more total light?"),
        ("Constructed Response:", "Using your model, explain why a glow stick placed in boiling water produces an intense burst of light that fades quickly, while one in the freezer produces a dim glow that lasts for days. Reference Chemical Concentration, Reaction Rate, and Product Buildup in your answer.")
    ],
    "background_intro": "A glow stick is a chemistry lesson in a plastic tube. When you snap it, you initiate a precisely engineered chemiluminescent reaction that converts chemical bond energy directly into visible light — no battery, no filament, no electricity. Understanding why it glows, why it stops, and why temperature matters reveals fundamental principles of chemical kinetics, energy transformation, and molecular dynamics.",
    "background_sections": [
        ("The Chemistry Inside", "A glow stick contains two separated chemicals: a solution of diphenyl oxalate (the energy source) and a fluorescent dye in the outer tube, and a glass vial of hydrogen peroxide (the oxidizer) in the center. When you snap the stick, the glass vial breaks and the chemicals mix. Hydrogen peroxide oxidizes diphenyl oxalate to produce phenol, CO2, and a high-energy intermediate called 1,2-dioxetanedione. This intermediate decomposes and transfers its energy to the fluorescent dye, which emits a photon of visible light as it returns to its ground state. The color depends on the dye: green (9,10-bis(phenylethynyl)anthracene), blue (9,10-diphenylanthracene), red (rhodamine B)."),
        ("Temperature and Reaction Rate", "The Arrhenius equation describes how temperature affects reaction rate: k = Ae^(-Ea/RT), where k is the rate constant, Ea is activation energy, R is the gas constant, and T is temperature in Kelvin. For most reactions, a 10 degree Celsius increase approximately doubles the reaction rate. This is because higher temperature means molecules move faster, collide more frequently, and a larger fraction exceeds the activation energy threshold. For a glow stick, this means doubling the temperature roughly doubles the light intensity — but also halves the duration."),
        ("The Brightness-Duration Trade-Off", "A glow stick contains a fixed amount of chemical reactant — its 'fuel.' The total light energy it can produce is determined by this fuel amount, not by how fast it's consumed. Heating accelerates the reaction, consuming fuel faster and producing brighter light for a shorter time. Cooling slows the reaction, consuming fuel more slowly and producing dimmer light for a longer time. The total integrated light output is approximately the same. This is a direct consequence of conservation of energy — the chemical energy in the bonds is converted to light energy regardless of the rate."),
        ("Product Buildup and Reaction Slowdown", "As the reaction proceeds, reactant concentration decreases and product concentration increases. According to the law of mass action, reaction rate is proportional to reactant concentration. As diphenyl oxalate and hydrogen peroxide are consumed, fewer reactant molecules are available to collide and react. Simultaneously, the accumulating products (phenol and CO2) dilute the remaining reactants. This creates a characteristic exponential decay in light output — bright at first, then progressively dimmer. The glow stick doesn't stop abruptly; it fades because the reaction asymptotically approaches completion.")
    ],
    "lever_L": "Students identify seven components of the chemiluminescent system: Chemical Concentration, Temperature, Reaction Rate, Fluorescent Dye Activation, Light Output, Energy Dissipation, and Product Buildup — with Temperature as the external variable.",
    "lever_E": "Students determine that Temperature drives Reaction Rate (Arrhenius relationship), which determines both Fluorescent Dye Activation (producing Light Output) and the rate of Chemical Concentration decline. Product Buildup slows the reaction as it progresses. Energy Dissipation represents losses.",
    "lever_V": "Students build a computational model showing how temperature controls the rate of chemiluminescent light production and the trade-off between intensity and duration.",
    "lever_Ev": "Students run room temperature, hot water bath, and freezer scenarios to compare brightness curves, duration, and total light output, confirming the brightness-duration trade-off.",
    "lever_R": "Students add Catalyst Presence, Dye Quantum Yield, or Solvent Viscosity to explore how chemical formulation choices affect glow stick performance optimization.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic glow stick image in darkness", "say": "Snap. Shake. Glow. No batteries, no electricity, no heat — just chemistry turning bond energy into light. But why does it stop? And why does heating it make it brighter but shorter?", "do": "If possible, snap a glow stick in class. Place pieces in hot water and ice water. Observe in real time. If not possible, show a time-lapse video of the experiment.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary terms", "say": "Today you're modeling one of the coolest chemical reactions you can hold in your hand — and discovering the fundamental rules that control ALL chemical reactions.", "do": "Have students read objectives. Pre-teach 'chemiluminescence' and 'activation energy.' Quick-write: Why do you think hot glow sticks are brighter?", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why does a glow stick stop glowing?", "say": "A glow stick starts bright and fades to nothing. Is it running out of energy? Running out of chemicals? Both? And why does temperature change the whole story?", "do": "Students hypothesize: What's happening inside the glow stick over time? Draw their mental model. Share and compare.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're going to model a chemical reaction from start to finish — tracking every molecule, every photon, every degree of temperature.", "do": "Preview each LEVER step. Emphasize that this model connects molecular-level chemistry to observable macroscopic behavior.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Seven component cards for chemiluminescence model", "say": "One thing you control: temperature. The chemistry handles the rest. But how you set that one variable changes everything.", "do": "Guide component sorting. Discuss why Temperature is external (you control it with hot/cold water) while all chemical processes are internal responses.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between chemical components", "say": "When temperature goes up, reaction rate goes up. But so does chemical consumption. Trace the consequences all the way to the last photon.", "do": "Help students map the cascade: Temperature drives Reaction Rate, which drives both Light Output and Chemical Concentration depletion. Product Buildup slows everything down.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and simulation results for three temperatures", "say": "Three glow sticks, three temperatures. Which one is brightest? Which lasts longest? And here's the real question: which produces the most total light?", "do": "Students predict brightness curves for all three temperatures before running simulations. Compare total light output (area under the curve) across scenarios.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings about energy conservation and kinetics", "say": "Conservation of energy just showed up in a glow stick. The total light is the same regardless of temperature — you're just choosing how to spend your chemical budget.", "do": "Lead discussion connecting glow stick behavior to conservation of energy. Discuss the Arrhenius equation in accessible terms.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Emergency light stick optimization design challenge", "say": "Search and rescue teams need three different glow sticks: a flare, a lantern, and a trail marker. Same chemistry, different specs. Design all three.", "do": "Groups optimize light stick formulations for three different emergency scenarios. Must specify concentration, temperature management, and expected performance. Present designs.", "time": "12 min"}
    ],
    "sort_reasoning": "Temperature is the external component because it is an environmental condition that can be controlled independently of the chemical reaction — by placing the glow stick in hot water, ice water, or ambient conditions. Chemical Concentration, Reaction Rate, Fluorescent Dye Activation, Light Output, Energy Dissipation, and Product Buildup are internal because they are determined by the chemistry of the reaction responding to the temperature condition and to each other through kinetic and thermodynamic relationships.",
    "relationships": [
        ("Temperature to Reaction Rate", "POSITIVE (+)", "Higher Temperature increases the kinetic energy of molecules, causing more frequent and more energetic collisions. According to the Arrhenius equation, a 10 degree Celsius increase roughly doubles the fraction of molecules exceeding activation energy, approximately doubling the Reaction Rate."),
        ("Reaction Rate to Chemical Concentration", "NEGATIVE (-)", "A faster Reaction Rate consumes reactant molecules more rapidly, decreasing Chemical Concentration. This is a direct mass balance relationship — every reaction event converts one set of reactant molecules into products, reducing the pool of available reactants."),
        ("Product Buildup to Reaction Rate", "NEGATIVE (-)", "As Product Buildup increases, the concentration of products rises relative to reactants. This dilutes the remaining reactants and shifts the system toward equilibrium, progressively slowing the net forward Reaction Rate according to the law of mass action.")
    ],
    "sim_answers": [
        ("Room Temperature Scenario", "At 25 degrees Celsius, the glow stick produces moderate Light Output that gradually fades over 6-12 hours. Reaction Rate is steady but not intense. Chemical Concentration decreases approximately exponentially. Product Buildup gradually slows the reaction. The characteristic glow curve shows a relatively flat plateau that slowly declines."),
        ("Hot Water Bath Scenario", "At 60 degrees Celsius, Reaction Rate approximately quadruples compared to room temperature (Arrhenius effect of ~35 degree increase). Light Output is dramatically brighter — perhaps 4x peak intensity. But Chemical Concentration plummets rapidly, Product Buildup accelerates, and the glow stick is essentially exhausted in 1-2 hours instead of 6-12. The brightness curve shows a sharp peak followed by rapid decay. Total integrated light output is approximately the same as room temperature — the chemical energy is conserved.")
    ],
    "reflection_exemplars": [
        ("Why is total light approximately the same at any temperature?", "This is a direct consequence of conservation of energy. A glow stick contains a fixed amount of chemical energy stored in the bonds of its reactants. When the reaction occurs, this energy is converted to light (and some heat through Energy Dissipation). Temperature doesn't change how much energy is stored — it changes how fast the energy is released. A hot glow stick releases its chemical energy quickly (bright, short-lived). A cold glow stick releases it slowly (dim, long-lasting). But the total energy converted to light is approximately the same because the same amount of chemical fuel is consumed either way."),
        ("Why does the glow fade rather than stop suddenly?", "The model shows that Product Buildup creates a negative feedback loop. As the reaction proceeds, reactant Chemical Concentration decreases while product concentration increases. Since Reaction Rate is proportional to reactant concentration (law of mass action), the rate continuously slows as reactants are consumed. This produces an exponential decay curve — bright at first when reactant concentration is highest, then progressively dimmer as the reaction asymptotically approaches completion. The glow stick never truly 'stops' — it just becomes too dim to see.")
    ],
    "stem_intro": "Present the challenge: A search-and-rescue equipment company needs chemiluminescent light sources optimized for three different emergency scenarios. Your team will design formulations for a bright signal flare (30 min), a moderate camp light (12+ hours), and a dim trail marker (48+ hours) — all using the same fundamental chemistry.",
    "stem_concepts": [
        ("Reaction Rate Optimization", "Chemical engineers control reaction rate through reactant concentration, temperature, catalyst selection, and solvent properties. For glow sticks, the primary controls are the concentration of diphenyl oxalate and hydrogen peroxide and the ambient temperature."),
        ("Quantum Yield Engineering", "Different fluorescent dyes convert chemical energy to light with different efficiencies. A dye with 90% quantum yield converts nearly all excitation energy to light; a dye with 30% quantum yield wastes 70% as heat. Choosing the right dye is critical for maximizing light output per gram of reactant."),
        ("Thermal Management", "In field conditions, temperature cannot always be controlled. Emergency light sticks might be used in Arctic cold (-40 degrees C) or desert heat (50 degrees C). Chemical formulations can be adjusted — higher concentrations and lower activation energies for cold environments, slower-reacting formulations for hot environments.")
    ],
    "stem_eval": [
        ("Expert (4)", "Designs specify reactant concentrations, temperature management strategies, and expected performance curves for all three scenarios, with model data supporting optimization choices and clear energy conservation reasoning"),
        ("Proficient (3)", "Designs address concentration and temperature trade-offs for each scenario with reasonable performance predictions"),
        ("Developing (2)", "Designs mention different formulations but lack specific concentration or temperature parameters or model-based justification"),
        ("Beginning (1)", "Designs are incomplete or do not connect chemical formulation choices to brightness/duration outcomes")
    ],
    "support": [
        "Provide a reaction rate vs. temperature graph template showing the Arrhenius relationship for students to reference",
        "Use a glow intensity vs. time graph template where students can sketch predicted curves for hot, cold, and room temperature glow sticks before running simulations",
        "Sentence frames: 'When Temperature increases from __ to __, Reaction Rate __ because __, which causes Light Output to __ but Duration to __ because __'"
    ],
    "extensions": [
        "Research bioluminescence — the biological version of chemiluminescence used by fireflies, deep-sea organisms, and some fungi — and compare the chemical mechanisms to synthetic glow sticks",
        "Investigate the Arrhenius equation quantitatively and calculate exactly how much temperature change is needed to double the reaction rate for a glow stick's specific activation energy",
        "Design a chemiluminescent reaction that changes color over time by incorporating multiple fluorescent dyes that are activated at different stages of the reaction"
    ],
    "cross_curr": [
        ("Math", "Use the Arrhenius equation to calculate reaction rate constants at three different temperatures and predict the glow duration for each, then compare predictions to experimental data"),
        ("ELA", "Write a technical product specification for an emergency light stick, including chemical formulation, performance parameters, safety data, and storage requirements"),
        ("Art", "Design packaging and marketing materials for a line of chemiluminescent products, accurately communicating the science of how they work while appealing to consumers")
    ],
    "misconceptions": [
        ("Glow sticks use electricity or radioactivity", "Glow sticks produce light entirely through chemical energy — no batteries, electricity, or radioactive materials are involved. The light comes from fluorescent dye molecules that are excited by energy from a chemical reaction (oxidation of diphenyl oxalate by hydrogen peroxide). This is chemiluminescence — the direct conversion of chemical bond energy to visible light photons.", "Compare energy sources: A flashlight converts electrical energy to light. A candle converts combustion energy to light. A glow stick converts oxidation energy to light. Different inputs, same output — photons."),
        ("Heating a glow stick gives it more energy", "Heating a glow stick does not add energy to the chemical reaction — it increases the RATE at which existing chemical energy is released. The total chemical energy is determined by the amount of reactant, not the temperature. A hot glow stick converts its chemical fuel to light faster, producing brighter but shorter-lived light. A cold one converts the same fuel slower. Conservation of energy means the total light output is approximately the same.", "Analogy: Heating a glow stick is like opening the faucet wider on a water tank. The water flows out faster, but the tank is the same size. You get more water per minute but run out sooner. Total water is the same."),
        ("When the glow stick stops glowing, the chemicals are gone", "The chemicals are not gone — they have been transformed. The reactants (diphenyl oxalate and hydrogen peroxide) have been converted to products (phenol and CO2). The atoms are still there; they are just arranged in different molecules that store less energy. This is conservation of mass in action. The glow stops because the products don't have the high-energy bonds needed to excite the fluorescent dye.", "Connect to conservation laws: Weigh a glow stick before and after use. The mass is the same (assuming CO2 stays dissolved). The atoms haven't disappeared — they've just rearranged into lower-energy configurations.")
    ]
}

L08 = {
    "id": "G10L2-L08",
    "title": "The Nitrogen Crisis: Why Fertilizer Is Destroying Our Rivers",
    "subtitle": "Modeling Nutrient Pollution and Aquatic Ecosystem Collapse",
    "ngss": "HS-LS2-4, HS-ESS2-2",
    "ngss_desc": "Use mathematical representations to support claims for the cycling of matter and flow of energy among organisms in an ecosystem. Analyze geoscience data to make the claim that one change to Earth's surface can create feedbacks that cause changes to other Earth's systems.",
    "big_question": "How does nitrogen fertilizer — designed to help plants grow — end up creating massive dead zones in oceans thousands of miles from the nearest farm?",
    "objectives": [
        "Model how fertilizer application cascades through nitrogen runoff, algal blooms, and oxygen depletion to cause aquatic ecosystem collapse",
        "Analyze the feedback loops connecting agricultural practices, water quality, and marine biodiversity",
        "Predict the conditions under which nutrient pollution crosses thresholds that trigger dead zone formation",
        "Evaluate the trade-offs between agricultural productivity, water quality, and the economic costs of water treatment and fishery collapse"
    ],
    "vocabulary": [
        ("Eutrophication", "The process by which excess nutrients — primarily nitrogen and phosphorus — cause explosive algal growth in water bodies, leading to oxygen depletion and ecosystem collapse when the algae die and decompose"),
        ("Hypoxia", "Dissolved oxygen levels below 2 mg/L — insufficient to support most marine life — caused by bacterial decomposition of massive algal blooms consuming all available oxygen in the water"),
        ("Dead Zone", "An area of ocean or lake where dissolved oxygen is so low that most marine organisms cannot survive — the Gulf of Mexico dead zone covers up to 22,000 square kilometers annually"),
        ("Nonpoint Source Pollution", "Pollution that comes from many diffuse sources across a landscape rather than a single pipe or factory — agricultural runoff is the largest nonpoint source of nitrogen pollution globally")
    ],
    "components": [
        ("Fertilizer Application", "The amount of synthetic nitrogen fertilizer applied to agricultural fields per hectare per year — globally approximately 120 million tons of nitrogen are applied annually", True),
        ("Nitrogen Runoff", "The fraction of applied fertilizer that washes off fields during rainfall and irrigation, entering streams and rivers as dissolved nitrate — typically 20-40% of applied nitrogen is lost to runoff", False),
        ("Algal Bloom Growth", "The explosive proliferation of algae and cyanobacteria in nitrogen-enriched water bodies, which can double their biomass every 1-3 days under ideal nutrient and light conditions", False),
        ("Oxygen Depletion", "The consumption of dissolved oxygen by bacteria decomposing dead algal biomass, creating hypoxic conditions that suffocate fish, shellfish, and other aquatic organisms", False),
        ("Fish Kill Rate", "The mortality rate of fish and other aquatic organisms in hypoxic zones, which can be sudden and massive — a single dead zone event can kill millions of organisms in days", False),
        ("Soil Depletion", "The progressive loss of natural soil nitrogen and organic matter caused by intensive monoculture farming, which increases dependence on synthetic fertilizer in a self-reinforcing cycle", False),
        ("Water Treatment Cost", "The economic burden of removing nitrogen from drinking water sources, treating algal toxins, and managing fishery losses — estimated at billions of dollars annually in the United States alone", False)
    ],
    "think_about_it": "When Fertilizer Application is high, some nitrogen feeds crops but the rest runs off into waterways. Nitrogen Runoff triggers Algal Bloom Growth, which leads to Oxygen Depletion and Fish Kill Rate. Meanwhile, Soil Depletion from intensive farming demands MORE fertilizer. Where is the vicious cycle, and where could you break it?",
    "scenarios": [
        ("Conventional Farming", "Set Fertilizer Application to current industrial levels — observe the cascade from field to dead zone"),
        ("Precision Agriculture", "Reduce Fertilizer Application to match actual crop needs — observe the impact on Nitrogen Runoff and downstream effects"),
        ("Soil Regeneration", "Invest in reducing Soil Depletion through cover crops and composting — observe how healthier soil reduces fertilizer dependence")
    ],
    "sim_scenarios": [
        ("Conventional Farming", "High fertilizer, intensive monoculture", "What do you predict happens to Algal Bloom Growth when conventional farming practices continue for 20 years?"),
        ("Precision Agriculture", "Optimized fertilizer matched to crop needs", "Do you predict that precision application can significantly reduce Nitrogen Runoff while maintaining crop yields?"),
        ("Soil Regeneration", "Cover crops, composting, reduced synthetic input", "What do you predict happens to Fertilizer Application needs when Soil Depletion is reversed through regenerative practices?")
    ],
    "discoveries": [
        "Only 30-50% of applied nitrogen fertilizer is actually absorbed by crops — the rest enters waterways as Nitrogen Runoff, making agriculture the largest source of nutrient pollution globally",
        "There is a threshold effect: moderate nitrogen loading allows rivers and oceans to process the excess, but above a critical concentration, Algal Bloom Growth overwhelms the system and dead zones form",
        "Soil Depletion creates a vicious cycle — degraded soil holds less nitrogen, requiring more fertilizer, which degrades soil further while increasing runoff",
        "The economic costs of nutrient pollution (water treatment, fishery losses, tourism damage) often exceed the economic gains from the excess fertilizer that caused the pollution"
    ],
    "answer": "Nitrogen fertilizer reaches the ocean through a cascade that begins on farms and ends in dead zones thousands of miles away. Farmers apply approximately 120 million tons of synthetic nitrogen to crops annually, but only 30-50% is absorbed by plants. The rest washes into streams during rain events (Nitrogen Runoff), flows through river systems (the Mississippi River carries 1.7 million tons of nitrogen to the Gulf of Mexico each year), and feeds explosive Algal Bloom Growth in coastal waters. When these massive algal blooms die, bacteria decompose them and consume all the dissolved oxygen, creating hypoxic dead zones where fish, shrimp, and crabs suffocate. The Gulf of Mexico dead zone — up to 22,000 square kilometers — is directly caused by Midwestern agricultural runoff flowing down the Mississippi. The tragedy is that this destruction is entirely preventable through precision fertilizer application, cover cropping, and buffer strips that filter runoff before it reaches waterways.",
    "stem_title": "Design a Watershed Nutrient Management Plan",
    "stem_mission": "Design a comprehensive nutrient management strategy for a 5,000-hectare agricultural watershed that maintains crop yields while reducing nitrogen runoff to safe ecological levels.",
    "stem_scenario": "A farming community downstream from a dead zone event has been ordered by the EPA to reduce nitrogen runoff by 40% within five years or face mandatory fertilizer restrictions. Your team has been hired to design a plan that achieves this reduction while keeping farmers economically viable.",
    "stem_questions": [
        "What combination of farming practices could reduce runoff by 40% without devastating crop yields?",
        "How would you use buffer zones, cover crops, and precision agriculture together?",
        "What monitoring system would verify that the plan is working before the five-year deadline?"
    ],
    "stem_design_qs": [
        "What is the maximum fertilizer application rate that maintains yield while meeting the 40% runoff reduction target?",
        "Where would you place riparian buffer strips and constructed wetlands to intercept runoff most effectively?",
        "How would you incentivize farmers to adopt regenerative practices — subsidies, technical assistance, or market premiums?",
        "What data would you collect to demonstrate compliance and measure ecological recovery downstream?"
    ],
    "career": "Environmental Scientists study how human activities affect water quality, soil health, and ecosystems. They work for the EPA, state agencies, consulting firms, and agricultural organizations, earning $55,000–$110,000/year. Agricultural Engineers who design sustainable farming systems earn $65,000–$120,000/year.",
    "images": {
        "cover": ("G10L2-L08-cover.png", "A photorealistic, cinematic aerial image of a vivid green algal bloom covering a lake or river surface, with clear water visible at the edges for contrast, agricultural fields visible in the background connected to the water by drainage channels, dramatic overhead lighting emphasizing the unnatural green color"),
        "landscape": ("G10L2-L08-landscape.png", "A diverse group of 15-16 year old students in a modern environmental science lab testing water quality samples for nitrogen content, test tubes with different colored reagents, water quality charts on the walls, engaged expressions, natural classroom lighting"),
        "modeling": ("G10L2-L08-modeling.png", "A diverse group of 15-16 year old students working on laptops building computational models of nutrient cycling in watersheds, screens showing nitrogen flow diagrams and dissolved oxygen graphs, modern classroom with ecology posters"),
        "discussion": ("G10L2-L08-discussion.png", "A teacher leading an animated discussion with diverse 15-16 year old students about agricultural pollution, a diagram of the nitrogen cycle from farm field to ocean dead zone displayed on a smartboard, students actively engaged"),
        "stem": ("G10L2-L08-stem.png", "Diverse 15-16 year old students designing watershed management plans with topographic maps and agricultural data charts on large displays, collaborative atmosphere with soil and water samples visible")
    },
    "pre_assessment": [
        "What do you think happens to the fertilizer farmers put on their fields when it rains?",
        "Why might too many nutrients in a lake or river be a bad thing — don't nutrients help things grow?",
        "Draw a diagram showing how you think nitrogen moves from a farm field to the ocean.",
        "What is a 'dead zone' in the ocean and what do you think causes it?"
    ],
    "extend_components": [
        ("Wetland Filtration", "The natural capacity of wetlands to absorb and denitrify excess nitrogen before it reaches rivers and oceans — 90% of US wetlands have been destroyed, eliminating this natural buffer"),
        ("Atmospheric Deposition", "Nitrogen oxides from fossil fuel combustion that deposit onto land and water surfaces through rain, adding to nutrient loading independent of agricultural sources"),
        ("Phosphorus Loading", "The companion nutrient that often limits algal growth in freshwater systems — reducing phosphorus may be more effective than reducing nitrogen for preventing freshwater eutrophication")
    ],
    "reflections": [
        "How does your model demonstrate the concept of nonpoint source pollution — why is agricultural runoff harder to control than factory discharge?",
        "What threshold effects did you observe in your model — at what point does nitrogen loading overwhelm the waterway's capacity to process it?",
        "How does Soil Depletion create a vicious cycle that increases both fertilizer dependence and nitrogen pollution over time?",
        "What does your model suggest about the economic cost-benefit of preventing pollution at the source versus treating it downstream?",
        "What are the limitations of modeling a continental-scale nutrient cascade with only seven components when real watersheds involve thousands of farms, tributaries, and microhabitats?"
    ],
    "dimensions": [
        ("Science Practice", "Using Mathematical Representations", "Students use mathematical relationships to model nitrogen flow from agricultural application through runoff, biological amplification, and oxygen depletion to predict dead zone formation."),
        ("Disciplinary Core Idea", "LS2.B Cycles of Matter and Energy Transfer / ESS2.A Earth Materials and Systems", "Matter cycles between the living and nonliving components of ecosystems; human activities can disrupt nutrient cycles with cascading effects on Earth's systems."),
        ("Crosscutting Concept", "Cause and Effect", "Students trace the causal chain from individual farm fertilizer decisions through watershed-scale nutrient transport to continental-scale dead zone formation, identifying leverage points for intervention.")
    ],
    "cast_items": [
        "Model the cascade from agricultural fertilizer application through nitrogen runoff, algal bloom growth, and oxygen depletion to dead zone formation",
        "Analyze threshold effects where nutrient loading overwhelms natural processing capacity and triggers ecosystem collapse",
        "Design intervention strategies that reduce nitrogen pollution while maintaining agricultural productivity"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A farmer applies 200 kg of nitrogen fertilizer per hectare. Based on your model, approximately how much of that nitrogen will eventually reach the nearest river as runoff?"),
        ("Constructed Response:", "Using your model, explain the complete causal chain from a farmer applying fertilizer in Iowa to a dead zone forming in the Gulf of Mexico 1,500 miles downstream. Reference Nitrogen Runoff, Algal Bloom Growth, and Oxygen Depletion in your explanation.")
    ],
    "background_intro": "The invention of synthetic nitrogen fertilizer in 1913 (the Haber-Bosch process) is arguably the most impactful chemical innovation in human history — it enabled the feeding of billions of people who would otherwise have starved. But it also created a nitrogen pollution crisis that is destroying aquatic ecosystems worldwide. Understanding this trade-off is one of the defining challenges of the 21st century.",
    "background_sections": [
        ("The Haber-Bosch Revolution", "Before 1913, all nitrogen for agriculture came from natural sources — manure, crop rotation with legumes, and guano. The Haber-Bosch process converts atmospheric nitrogen gas (N2) into ammonia (NH3) using high temperature and pressure, making unlimited synthetic fertilizer possible. Today, approximately 50% of the nitrogen atoms in your body were fixed by the Haber-Bosch process. It has enabled the global population to grow from 1.7 billion to 8 billion. But it has also doubled the amount of reactive nitrogen cycling through Earth's ecosystems."),
        ("The Runoff Cascade", "When nitrogen fertilizer is applied to fields, crops absorb only 30-50% under best management practices. The rest has three fates: it volatilizes into the atmosphere as ammonia or nitrous oxide (a potent greenhouse gas), it leaches into groundwater contaminating drinking water supplies, or it washes off the soil surface during rainfall as dissolved nitrate. This runoff enters streams, flows through river systems, and accumulates in lakes and coastal waters. The Mississippi River basin drains 41% of the continental United States — every farm in this vast watershed contributes to the nutrient load that eventually reaches the Gulf of Mexico."),
        ("Eutrophication and Dead Zones", "When excess nitrogen reaches a water body, it fertilizes algae just as it fertilizes crops. Algal populations explode, doubling every 1-3 days and forming massive blooms that can cover hundreds of square kilometers. When these algae die, bacteria decompose the biomass and consume dissolved oxygen in the process. When oxygen drops below 2 mg/L (hypoxia), fish flee if they can and suffocate if they cannot. The resulting dead zone is a biological desert. The Gulf of Mexico dead zone averages 14,000 square kilometers annually — larger than Connecticut. There are now over 500 dead zones worldwide, up from 49 in the 1960s."),
        ("Solutions and Trade-offs", "Solving the nitrogen crisis requires balancing food production with environmental protection. Precision agriculture uses GPS-guided equipment and soil sensors to apply exactly the nitrogen each section of field needs — reducing application by 15-30% without yield loss. Cover crops prevent bare soil from eroding and capture residual nitrogen between growing seasons. Riparian buffer strips (vegetated zones along waterways) intercept and filter runoff before it reaches streams. Constructed wetlands can denitrify water through bacterial processes. The technology exists — the challenge is implementation at scale across millions of farms.")
    ],
    "lever_L": "Students identify seven components of the nitrogen pollution system: Fertilizer Application, Nitrogen Runoff, Algal Bloom Growth, Oxygen Depletion, Fish Kill Rate, Soil Depletion, and Water Treatment Cost — with Fertilizer Application as the external driver.",
    "lever_E": "Students determine that Fertilizer Application drives Nitrogen Runoff (20-40% loss), which triggers Algal Bloom Growth. Dead algae cause Oxygen Depletion, leading to Fish Kill Rate. Soil Depletion increases fertilizer dependence. Water Treatment Cost rises with pollution severity.",
    "lever_V": "Students build a computational model showing the cascade from farm field to dead zone and the economic feedback through Water Treatment Cost.",
    "lever_Ev": "Students run conventional farming, precision agriculture, and soil regeneration scenarios to compare environmental and economic outcomes and identify the most effective intervention points.",
    "lever_R": "Students add Wetland Filtration, Atmospheric Deposition, or Phosphorus Loading to explore how natural buffers and additional nutrient sources affect dead zone dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic algal bloom aerial image", "say": "That bright green water isn't paint. It's trillions of algae, fed by fertilizer from farms a thousand miles away. And underneath that green surface, everything is dying.", "do": "Show satellite images of the Gulf of Mexico dead zone and compare to a map of the Mississippi River watershed. Ask: How does fertilizer from Iowa end up killing fish in Louisiana?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary terms", "say": "Today you're modeling how a farmer's perfectly reasonable decision to fertilize crops creates an environmental disaster 1,500 miles downstream.", "do": "Have students read objectives. Pre-teach 'eutrophication' and 'hypoxia.' Quick-write: What do you think happens to fertilizer when it rains?", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How does fertilizer destroy our rivers?", "say": "Fertilizer helps plants grow. More plants, more food, more life. So why does fertilizer in water kill everything?", "do": "Students brainstorm: When is 'more nutrients' actually harmful? Can you think of other examples where too much of a good thing becomes destructive?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're tracing a nitrogen atom from a fertilizer bag in Iowa to a dead fish in the Gulf of Mexico. The journey will change how you think about agriculture.", "do": "Preview each LEVER step. Emphasize that this model connects individual farm decisions to continental-scale environmental consequences.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Seven component cards for nitrogen pollution model", "say": "One decision: how much fertilizer to apply. The consequences cascade through seven components across 1,500 miles.", "do": "Guide component sorting. Discuss why Fertilizer Application is external (farmer's decision) while all downstream effects are internal ecological and economic responses.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between nitrogen pollution components", "say": "Follow the nitrogen. Field to stream. Stream to river. River to gulf. Algae to dead zone. Dead zone to fish kills. Fish kills to economic collapse. It's all connected.", "do": "Help students trace the complete cascade. Identify the Soil Depletion vicious cycle. Calculate how much nitrogen reaches the ocean from a single farm.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and simulation results for three farming strategies", "say": "Three approaches to farming, three very different outcomes for the Gulf of Mexico. Let's find out which one actually works.", "do": "Students predict dead zone size for each scenario. Run simulations. Compare environmental AND economic outcomes — including Water Treatment Cost.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model exploration", "say": "The Haber-Bosch process feeds half the world. It also created 500 dead zones. Can we keep the food and fix the water?", "do": "Lead discussion on the food-environment trade-off. Connect to the real Gulf of Mexico dead zone data. Discuss solutions that are available but not widely adopted.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Watershed nutrient management plan design challenge", "say": "The EPA says your community must cut nitrogen runoff by 40% in five years or face mandatory restrictions. Design the plan that saves both the farms and the fish.", "do": "Groups design comprehensive watershed management plans. Must balance agricultural productivity with environmental targets. Present as proposals to a simulated EPA panel.", "time": "12 min"}
    ],
    "sort_reasoning": "Fertilizer Application is the external component because it is a deliberate agricultural decision made by farmers based on crop needs, cost, and management practices — it is the controllable input to the system. Nitrogen Runoff, Algal Bloom Growth, Oxygen Depletion, Fish Kill Rate, Soil Depletion, and Water Treatment Cost are internal because they are ecological and economic consequences that cascade from the fertilizer application through natural biogeochemical and economic processes.",
    "relationships": [
        ("Fertilizer Application to Nitrogen Runoff", "POSITIVE (+)", "Higher Fertilizer Application increases the amount of excess nitrogen available on field surfaces. During rainfall events, a greater fraction of this nitrogen dissolves and washes into waterways as nitrate runoff — typically 20-40% of applied nitrogen is lost."),
        ("Nitrogen Runoff to Algal Bloom Growth", "POSITIVE (+)", "Higher Nitrogen Runoff delivers more dissolved nutrients to lakes and coastal waters. Since nitrogen is often the limiting nutrient in marine systems, increased supply removes the growth constraint on algae, triggering explosive population blooms."),
        ("Algal Bloom Growth to Oxygen Depletion", "POSITIVE (+)", "Larger Algal Bloom Growth produces more biomass that eventually dies and sinks. Bacterial decomposition of this massive organic load consumes dissolved oxygen at rates that exceed atmospheric replenishment, driving dissolved oxygen to hypoxic levels.")
    ],
    "sim_answers": [
        ("Conventional Farming Scenario", "With high Fertilizer Application, Nitrogen Runoff carries substantial nutrient loads into waterways. Algal Bloom Growth responds dramatically — bloom extent and intensity increase each year as cumulative nutrient loading enriches sediments. Oxygen Depletion creates expanding hypoxic zones. Fish Kill Rate peaks during late summer when water is warmest and algal die-offs are largest. Soil Depletion gradually increases, demanding more fertilizer and worsening the cycle. Water Treatment Cost rises as drinking water sources become contaminated."),
        ("Precision Agriculture Scenario", "With Fertilizer Application optimized to match actual crop uptake, Nitrogen Runoff decreases by 20-35%. This reduction propagates through the cascade: Algal Bloom Growth moderates, Oxygen Depletion stays above critical thresholds in most areas, and Fish Kill Rate drops significantly. The key finding is that relatively modest reductions in over-fertilization produce disproportionately large improvements downstream because the system has threshold behavior — staying below the eutrophication trigger prevents the entire cascade.")
    ],
    "reflection_exemplars": [
        ("Why does Soil Depletion create a vicious cycle?", "Healthy soil contains organic matter and microbial communities that naturally cycle nitrogen, reducing the need for synthetic fertilizer. But intensive monoculture farming depletes soil organic matter, destroys soil structure, and kills beneficial microorganisms. Depleted soil holds less nitrogen, so more leaches away as runoff. Farmers compensate by applying more synthetic fertilizer, which further degrades soil biology. The cycle escalates: worse soil requires more fertilizer, which makes soil worse, which requires even more fertilizer. Breaking this cycle requires investing in soil health through cover crops, compost, and crop rotation — practices that rebuild soil's natural nitrogen-cycling capacity."),
        ("Why are dead zones getting worse despite awareness?", "The model shows that the nitrogen pollution problem has structural features that resist easy solutions. The pollution is nonpoint source — it comes from millions of individual farms, not one factory. There is a time lag: nitrogen applied to fields this year may not reach the coast for months or years, so cause and effect are geographically and temporally separated. Economic incentives favor over-fertilization because the marginal cost of extra fertilizer is small compared to the risk of yield loss. And the environmental costs (dead zones, water treatment) are borne by downstream communities, not the farmers who cause the pollution — a classic economic externality.")
    ],
    "stem_intro": "Present the challenge: A farming community facing EPA nitrogen reduction mandates needs a comprehensive plan that cuts runoff by 40% without bankrupting farmers. Your team will design the watershed management strategy using model data to justify every intervention and predict outcomes.",
    "stem_concepts": [
        ("Precision Nutrient Management", "GPS-guided variable-rate application technology can apply different fertilizer amounts to different parts of a field based on soil tests and yield maps. This reduces over-application in areas that don't need it while maintaining yields where soil is deficient — typically reducing total nitrogen use by 15-30%."),
        ("Buffer Infrastructure", "Riparian buffer strips (vegetated zones along waterways) can intercept 50-90% of nitrogen in surface runoff. Constructed wetlands use denitrifying bacteria to convert dissolved nitrate to harmless nitrogen gas. Strategic placement of these natural filters at critical runoff pathways maximizes nutrient removal per dollar invested."),
        ("Economic Incentive Design", "Environmental compliance can be achieved through regulation (mandates and fines) or incentives (payments for nutrient reduction, certification premiums for sustainable practices). The most effective programs combine both — setting clear targets while providing financial support for the transition to better practices.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan combines precision agriculture, buffer infrastructure, and soil regeneration practices with specific acreage targets, timeline milestones, monitoring protocols, economic analysis, and model-based justification for projected 40% reduction"),
        ("Proficient (3)", "Plan includes multiple intervention strategies with reasonable coverage and some model-based evidence for effectiveness"),
        ("Developing (2)", "Plan addresses some intervention strategies but lacks quantitative targets, monitoring plan, or clear connection to model evidence"),
        ("Beginning (1)", "Plan is incomplete or proposes interventions without connecting them to the nitrogen cascade model")
    ],
    "support": [
        "Provide a watershed map showing farm locations, waterways, and areas where buffer strips would be most effective",
        "Use a nitrogen budget template: 'Applied: __ kg/ha. Crop uptake: __ kg/ha. Runoff: __ kg/ha. Residual: __ kg/ha'",
        "Sentence frames: 'When Fertilizer Application is reduced by __%, Nitrogen Runoff decreases by approximately __% because __, which reduces Algal Bloom Growth by __ because __'"
    ],
    "extensions": [
        "Research the Chesapeake Bay nutrient restoration program — one of the most ambitious watershed management efforts in the world — and analyze what has worked and what has not",
        "Investigate how harmful algal blooms (HABs) produce toxins like microcystin that contaminate drinking water, and model the public health consequences of eutrophication",
        "Compare the nitrogen pollution crisis to the phosphorus-driven eutrophication of Lake Erie in the 1960s-70s and analyze what policy interventions successfully restored the lake"
    ],
    "cross_curr": [
        ("Math", "Calculate the total nitrogen load delivered to the Gulf of Mexico from a 1,000-hectare farm applying 150 kg N/ha with 35% runoff loss, and determine how many farms would need to adopt precision agriculture to reduce the dead zone by 30%"),
        ("ELA", "Write a persuasive letter to a member of Congress arguing for or against mandatory nitrogen application limits on farms, using model data and economic analysis as evidence"),
        ("Social Studies", "Research the environmental justice dimensions of agricultural pollution — who lives near concentrated animal feeding operations and who drinks contaminated well water — and analyze how nutrient pollution disproportionately affects marginalized communities")
    ],
    "misconceptions": [
        ("Fertilizer is artificial and therefore harmful", "Synthetic nitrogen fertilizer is chemically identical to nitrogen from natural sources — plants cannot distinguish between a nitrate ion from a compost pile and one from a fertilizer bag. The problem is not the chemistry but the quantity. Natural nitrogen cycling adds about 140 million tons of reactive nitrogen to ecosystems annually; the Haber-Bosch process adds another 120 million tons. We have doubled the nitrogen cycle, overwhelming ecosystems' capacity to process it.", "Clarify: The nitrogen atom doesn't know where it came from. A compost-derived nitrate molecule is identical to a synthetic one. The issue is that we've added 120 million tons MORE than natural systems evolved to handle."),
        ("Dead zones are permanent", "Most dead zones are seasonal — they form in late summer when warm water holds less oxygen and algal die-offs are largest, then dissipate in fall and winter when cooler temperatures and storms mix oxygen back into the water. This means the damage is potentially reversible if nutrient loading is reduced. The Black Sea dead zone — once the largest in the world — largely disappeared after the collapse of Soviet agriculture reduced fertilizer use. Recovery is possible, but it requires sustained reduction in nutrient inputs.", "Hope note: Show the Black Sea recovery data. When Soviet fertilizer subsidies ended in 1991, fertilizer use dropped 50% and the dead zone shrank dramatically within a decade. The ecosystem can recover — if we let it."),
        ("Organic farming solves the nitrogen problem", "Organic farming reduces synthetic fertilizer use but does not eliminate nitrogen runoff. Organic nitrogen sources (manure, compost, cover crop residues) can still wash into waterways if applied in excess or during rain events. In some cases, manure over-application on organic farms creates worse runoff than well-managed conventional fields. The solution is not the nitrogen source but the nitrogen balance — applying only what crops can absorb, regardless of whether the source is synthetic or organic.", "Compare: Test nitrogen runoff from an over-manured organic field versus a precision-managed conventional field. The conventional field may actually produce less runoff because precision technology matches application to uptake more accurately.")
    ]
}

L09 = {
    "id": "G10L2-L09",
    "title": "How Do Doctors See Inside You Without Cutting You Open?",
    "subtitle": "Modeling MRI Physics and Medical Imaging Technology",
    "ngss": "HS-PS2-4, HS-PS4-4",
    "ngss_desc": "Use mathematical representations of Newton's law of gravitation and Coulomb's law to describe and predict the gravitational and electrostatic forces between objects. Evaluate the validity and reliability of claims in published materials of the effects that different frequencies of electromagnetic radiation have when absorbed by matter.",
    "big_question": "How can a machine create detailed images of your brain, muscles, and organs using nothing but a magnetic field and radio waves — without a single X-ray or incision?",
    "objectives": [
        "Model how magnetic field strength, radio frequency pulses, and tissue properties interact to produce diagnostic-quality medical images",
        "Analyze why MRI provides superior tissue contrast compared to X-rays and CT scans for certain medical conditions",
        "Predict how changes in magnetic field strength and coil temperature affect image resolution and diagnostic accuracy",
        "Evaluate the trade-offs between image quality, patient safety, scan time, and energy consumption in MRI system design"
    ],
    "vocabulary": [
        ("Nuclear Magnetic Resonance", "The physical phenomenon where atomic nuclei with odd numbers of protons or neutrons absorb and re-emit radiofrequency energy when placed in a magnetic field — the principle underlying MRI technology"),
        ("Magnetic Field Strength", "The intensity of the magnetic field generated by the MRI scanner, measured in Tesla — clinical MRI machines typically operate at 1.5 to 3 Tesla, which is 30,000 to 60,000 times Earth's magnetic field"),
        ("Relaxation Time", "The time it takes for hydrogen nuclei to return to their equilibrium alignment after being excited by a radiofrequency pulse — different tissues have different relaxation times, creating the contrast that makes MRI images useful"),
        ("Superconducting Coil", "An electromagnet made of special alloys (niobium-titanium) cooled to near absolute zero (-269 degrees Celsius) with liquid helium, which carries electrical current with zero resistance to generate the powerful, stable magnetic field required for MRI")
    ],
    "components": [
        ("Magnetic Field Strength", "The intensity of the static magnetic field in Tesla, which aligns hydrogen nuclei in the patient's body and determines the signal-to-noise ratio of the resulting images", True),
        ("Coil Temperature", "The temperature of the superconducting magnet coils, which must remain below the critical temperature (-269 degrees Celsius for NbTi) to maintain zero electrical resistance and stable magnetic field", True),
        ("Image Resolution", "The spatial detail visible in the MRI image, measured in millimeters — determined by magnetic field strength, gradient coil precision, and signal-to-noise ratio", False),
        ("Tissue Contrast", "The ability to visually distinguish different tissue types in the image based on their different relaxation times — the primary advantage of MRI over other imaging modalities", False),
        ("Patient Safety", "The level of risk to the patient during scanning, affected by magnetic field interactions with implants, specific absorption rate (SAR) of radiofrequency energy, and acoustic noise from gradient switching", False),
        ("Energy Consumption", "The total electrical power required to operate the MRI system, including maintaining cryogenic cooling for superconducting coils, powering gradient amplifiers, and running computing systems", False),
        ("Diagnostic Accuracy", "The probability that the MRI image provides sufficient information for a correct medical diagnosis, determined by the combination of Image Resolution, Tissue Contrast, and the radiologist's expertise", False)
    ],
    "think_about_it": "Higher Magnetic Field Strength improves Image Resolution and Tissue Contrast, increasing Diagnostic Accuracy. But it also increases Energy Consumption, requires colder Coil Temperature, and creates greater Patient Safety risks for people with metallic implants. Where is the optimal balance?",
    "scenarios": [
        ("Standard 1.5T Clinical MRI", "Set Magnetic Field Strength to 1.5 Tesla — observe the baseline performance for resolution, contrast, safety, and energy"),
        ("High-Field 3T Research MRI", "Set Magnetic Field Strength to 3 Tesla — observe the improvements in image quality and the increases in energy and safety considerations"),
        ("Coil Warming Emergency", "Simulate Coil Temperature rising above the superconducting critical point — observe the cascade failure of the entire system")
    ],
    "sim_scenarios": [
        ("Standard 1.5T", "Clinical standard field strength", "What do you predict is the relationship between Magnetic Field Strength and Image Resolution at 1.5 Tesla?"),
        ("High-Field 3T", "Double the standard field strength", "What do you predict happens to Tissue Contrast and Patient Safety when Magnetic Field Strength doubles from 1.5T to 3T?"),
        ("Coil Failure", "Superconducting coil warms above critical temperature", "What do you predict happens to the entire MRI system if the liquid helium cooling fails and Coil Temperature rises?")
    ],
    "discoveries": [
        "MRI creates images using only magnetic fields and radio waves — no ionizing radiation is involved, making it fundamentally safer than X-rays or CT scans for repeated imaging",
        "Image Resolution and Tissue Contrast both improve with higher Magnetic Field Strength, but the relationship is not linear — doubling field strength from 1.5T to 3T roughly doubles signal-to-noise ratio",
        "The superconducting coil is the most critical and fragile component — if Coil Temperature rises above the critical threshold, the magnet 'quenches,' explosively boiling the liquid helium and destroying the magnetic field",
        "The trade-off between image quality and patient safety means that the most powerful MRI machines are not always the best choice — 1.5T is sufficient for most diagnoses and presents fewer safety challenges"
    ],
    "answer": "MRI works by exploiting the magnetic properties of hydrogen atoms — which are abundant in every tissue of the body because we are mostly water. The scanner generates a powerful magnetic field (1.5-3 Tesla) that aligns hydrogen nuclei. Short bursts of radiofrequency energy are then applied, knocking the nuclei out of alignment. As they return to equilibrium, they emit radiofrequency signals that are detected by receiver coils. Different tissues (fat, muscle, cerebrospinal fluid, tumor) have different relaxation times, producing different signal intensities that create contrast in the final image. A computer processes millions of these signals to construct detailed cross-sectional images. No X-rays, no radiation, no incision — just magnets, radio waves, and the hydrogen atoms already inside you.",
    "stem_title": "Design a Next-Generation Portable MRI System",
    "stem_mission": "Design a compact, lower-cost MRI system that could be deployed in rural clinics, ambulances, or developing countries where traditional MRI is unavailable.",
    "stem_scenario": "A medical technology startup wants to bring MRI capabilities to the 70% of the world's population that currently has no access to MRI imaging. Your team has been hired to design a portable MRI system that sacrifices some image quality for dramatic reductions in cost, size, and power requirements.",
    "stem_questions": [
        "What Magnetic Field Strength would you use for a portable system — and what diagnostic capabilities would you sacrifice?",
        "Could you eliminate the superconducting coils (and liquid helium cooling) by using permanent magnets, and what would that trade away?",
        "What is the minimum Image Resolution needed to diagnose the most common conditions in underserved areas (stroke, fractures, tumors)?"
    ],
    "stem_design_qs": [
        "What type of magnet technology would you use — superconducting, permanent, or resistive electromagnets?",
        "How would you power the system in locations without reliable electricity?",
        "What imaging protocols would you prioritize for the most impactful diagnoses in resource-limited settings?",
        "How would you address patient safety with a system that might be operated by non-specialist technicians?"
    ],
    "career": "MRI Physicists design and optimize MRI scanning protocols and develop new imaging techniques. They work in hospitals, research universities, and medical device companies, earning $90,000–$180,000/year. Biomedical Engineers who design medical imaging equipment earn $75,000–$150,000/year.",
    "images": {
        "cover": ("G10L2-L09-cover.png", "A photorealistic, cinematic image of a modern MRI machine in a clinical setting with a patient entering the scanner bore, the machine's sleek white design illuminated by ambient blue clinical lighting, showing the impressive scale of the technology"),
        "landscape": ("G10L2-L09-landscape.png", "A diverse group of 15-16 year old students in a modern physics lab examining MRI brain scan images and magnetic field demonstrations with iron filings, fascinated expressions as they learn about medical imaging, natural classroom lighting"),
        "modeling": ("G10L2-L09-modeling.png", "A diverse group of 15-16 year old students working on laptops building computational models of MRI signal physics, screens showing magnetic field diagrams and tissue contrast simulations, modern classroom with medical imaging posters"),
        "discussion": ("G10L2-L09-discussion.png", "A teacher leading an animated discussion with diverse 15-16 year old students about how MRI creates images, a diagram showing nuclear magnetic resonance and tissue relaxation times displayed on a smartboard, students actively engaged"),
        "stem": ("G10L2-L09-stem.png", "Diverse 15-16 year old students designing portable MRI system concepts with engineering diagrams and component specifications on large displays, collaborative atmosphere with magnetic demonstrations and MRI scan prints visible")
    },
    "pre_assessment": [
        "What do you know about how MRI machines create images of the inside of the body?",
        "Why might a doctor choose MRI over an X-ray for certain types of injuries or conditions?",
        "Draw a diagram showing what you think happens inside an MRI machine when it scans a patient.",
        "What role do magnets play in medical imaging — how could a magnet help see inside a person?"
    ],
    "extend_components": [
        ("Gradient Coil Precision", "The accuracy of the additional magnetic field gradients that encode spatial location in the MRI signal — more precise gradients produce higher resolution images but generate louder noise and more heat"),
        ("Scan Duration", "The total time required to acquire sufficient data for a diagnostic-quality image — longer scans produce better images but increase patient discomfort, motion artifacts, and system operating costs"),
        ("RF Pulse Sequence Design", "The specific pattern and timing of radiofrequency pulses used to generate tissue-specific contrast — different sequences (T1-weighted, T2-weighted, FLAIR) highlight different tissue properties for different diagnostic purposes")
    ],
    "reflections": [
        "How does your model demonstrate why MRI is preferred over CT scans for soft tissue imaging despite being more expensive and slower?",
        "What does the coil failure scenario reveal about the engineering fragility of the superconducting magnet system?",
        "Why is there an optimal Magnetic Field Strength rather than simply using the strongest possible magnet?",
        "How does your model help explain the extreme cost of MRI machines ($1-3 million) and MRI scans ($500-$5,000)?",
        "What are the limitations of modeling MRI physics with only seven components when real MRI involves quantum spin physics, Fourier transforms, and complex pulse sequence programming?"
    ],
    "dimensions": [
        ("Science Practice", "Evaluating Claims", "Students evaluate claims about medical imaging technologies by modeling the physics-based trade-offs between field strength, image quality, safety, and cost."),
        ("Disciplinary Core Idea", "PS2.B Types of Interactions / PS4.B Electromagnetic Radiation", "Magnetic fields exert forces on aligned nuclear magnetic moments; radiofrequency electromagnetic radiation can be absorbed and re-emitted by atomic nuclei, with tissue-dependent properties that enable medical imaging."),
        ("Crosscutting Concept", "Structure and Function", "Students analyze how the physical structure of MRI components (superconducting coils, gradient coils, RF transmitters) determines the functional capability of the imaging system.")
    ],
    "cast_items": [
        "Model how magnetic field strength and tissue relaxation properties interact to produce diagnostic medical images",
        "Analyze the trade-offs between image quality, patient safety, and system cost in MRI technology",
        "Evaluate why MRI uses non-ionizing radiation and how this affects its safety profile compared to X-ray and CT imaging"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A hospital is choosing between a 1.5T MRI and a 3T MRI. Based on your model, which factor would most improve by upgrading to 3T?"),
        ("Constructed Response:", "Using your model, explain how MRI creates images of soft tissues without using X-rays or any ionizing radiation. Reference Magnetic Field Strength, Tissue Contrast, and the role of hydrogen nuclei in your explanation.")
    ],
    "background_intro": "Magnetic Resonance Imaging is one of the most remarkable achievements of applied physics — it turns the quantum mechanical properties of hydrogen atoms into detailed images of the human body's interior. Without a single X-ray photon or surgical incision, MRI can distinguish between healthy and diseased tissue, map brain activity, visualize blood flow, and detect tumors as small as a few millimeters.",
    "background_sections": [
        ("The Physics of Nuclear Magnetic Resonance", "Every hydrogen atom has a nucleus (single proton) that acts as a tiny magnetic dipole — a miniature bar magnet. Normally, these nuclear magnets point in random directions, canceling out. But when placed in a strong external magnetic field, the protons align either parallel or antiparallel to the field, with a slight majority parallel (lower energy state). This creates a net magnetization that can be manipulated with radio waves. When a radiofrequency pulse at the precise resonance frequency (the Larmor frequency, proportional to field strength) is applied, it flips the aligned protons to the higher energy state. When the pulse stops, the protons relax back to equilibrium, emitting radiofrequency signals as they do. These signals are the raw data of MRI."),
        ("How Contrast Works", "The key to MRI's diagnostic power is that different tissues have different relaxation times. T1 relaxation (spin-lattice) measures how quickly protons return to alignment with the main field. T2 relaxation (spin-spin) measures how quickly the precessing protons fall out of phase with each other. Fat has short T1 (recovers quickly, appears bright on T1-weighted images). Cerebrospinal fluid has long T1 and long T2 (appears dark on T1, bright on T2). Tumors often have different relaxation times from surrounding healthy tissue, making them visible. By adjusting the timing of RF pulses (the pulse sequence), radiologists can create images that highlight specific tissue properties."),
        ("The Superconducting Magnet", "Creating a stable, powerful, and homogeneous magnetic field requires a superconducting electromagnet. Miles of niobium-titanium wire are wound into coils and cooled to 4.2 Kelvin (-269 degrees Celsius) using liquid helium. At this temperature, the wire's electrical resistance drops to exactly zero, allowing thousands of amperes to flow without energy loss. Once energized, the current circulates indefinitely — many MRI magnets have been running continuously for years without being re-energized. But the system is fragile: if any section of the coil warms above the critical temperature, resistance appears, generating heat that boils the helium explosively in a 'quench' — a dramatic and expensive failure."),
        ("Safety and Limitations", "MRI is generally very safe because it uses non-ionizing radiation (radio waves, not X-rays). However, the powerful magnetic field creates unique hazards. Ferromagnetic objects (iron, steel) become high-velocity projectiles when brought near the scanner — MRI-related accidents from chairs, oxygen tanks, and tools being pulled into the bore have caused injuries and deaths. Patients with certain metallic implants (pacemakers, cochlear implants, shrapnel) cannot safely enter the magnetic field. The strong radiofrequency pulses deposit energy in tissue (measured as Specific Absorption Rate, SAR), which can cause heating. The loud noise from gradient coil switching (up to 130 dB) requires hearing protection.")
    ],
    "lever_L": "Students identify seven components of the MRI system: Magnetic Field Strength, Coil Temperature, Image Resolution, Tissue Contrast, Patient Safety, Energy Consumption, and Diagnostic Accuracy — with Magnetic Field Strength and Coil Temperature as external engineering parameters.",
    "lever_E": "Students determine that Magnetic Field Strength drives Image Resolution and Tissue Contrast (both improving signal-to-noise ratio), which together determine Diagnostic Accuracy. Higher field strength increases Energy Consumption and creates greater Patient Safety concerns. Coil Temperature must stay below the superconducting critical point.",
    "lever_V": "Students build a computational model showing how field strength affects all downstream parameters and the trade-offs between image quality, safety, and cost.",
    "lever_Ev": "Students run 1.5T standard, 3T high-field, and coil failure scenarios to compare image quality, safety profiles, and the consequences of system failure.",
    "lever_R": "Students add Gradient Coil Precision, Scan Duration, or RF Pulse Sequence Design to explore how additional engineering parameters affect MRI performance optimization.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic MRI scanner image", "say": "This machine can see inside your skull without touching you. No X-rays. No cutting. Just magnets and radio waves. How is that even possible?", "do": "Show a stunning MRI brain scan image. Ask: How can a magnet create a picture of something it can't touch? Collect initial hypotheses.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary terms", "say": "Today you're modeling one of the most sophisticated machines in modern medicine — and the physics that makes it work is something you already know: electromagnetism.", "do": "Have students read objectives. Pre-teach 'nuclear magnetic resonance' and 'relaxation time.' Quick-write: What do you think happens to atoms in a magnetic field?", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How do doctors see inside you without cutting you open?", "say": "Your body is 60% water. Water is H2O. Those hydrogen atoms are about to become the most important atoms in medicine.", "do": "Students estimate: How many hydrogen atoms are in your body? (Answer: approximately 4 x 10^27.) Ask: What if you could make every single one of them send you a signal?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're going to model how magnets, cold, and radio waves combine to create the most detailed images of the human body ever possible.", "do": "Preview each LEVER step. Emphasize that MRI connects quantum physics (nuclear spin) to clinical medicine (diagnosis).", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Seven component cards for MRI system model", "say": "Two things engineers control: how strong to make the magnet and how cold to keep it. The physics and the patient determine everything else.", "do": "Guide component sorting. Discuss why Magnetic Field Strength and Coil Temperature are external (engineering choices) while image quality and safety are internal responses.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between MRI system components", "say": "Stronger magnet means better images. But it also means more energy, more danger, and one malfunction away from a catastrophic quench.", "do": "Help students map the trade-offs: field strength improves image quality but increases energy, cost, and safety concerns. Trace the coil temperature failure cascade.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and simulation results for three scenarios", "say": "Let's compare a standard hospital MRI, a research powerhouse, and what happens when the cooling fails spectacularly.", "do": "Students predict outcomes for each scenario. Run simulations. The quench scenario is particularly dramatic — discuss what happens physically.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from MRI system model", "say": "You just modeled a $2 million machine that uses the coldest temperature in the hospital to detect the warmest thing in medicine: living tissue.", "do": "Lead discussion connecting model findings to real MRI capabilities and limitations. Show clinical MRI images comparing healthy and diseased tissue.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Portable MRI design challenge", "say": "70% of the world has no access to MRI. Design the machine that changes that — even if it means sacrificing the Rolls Royce version for something that actually reaches people.", "do": "Groups design portable MRI concepts. Must specify magnet type, field strength, target diagnoses, power requirements, and cost estimate. Present as startup pitches.", "time": "12 min"}
    ],
    "sort_reasoning": "Magnetic Field Strength and Coil Temperature are external components because they are engineering parameters that can be specified and controlled during system design and operation. Magnetic Field Strength is chosen based on the desired image quality, and Coil Temperature is maintained by the cryogenic cooling system. Image Resolution, Tissue Contrast, Patient Safety, Energy Consumption, and Diagnostic Accuracy are internal because they are determined by the physics of nuclear magnetic resonance responding to the field strength and operational conditions.",
    "relationships": [
        ("Magnetic Field Strength to Image Resolution", "POSITIVE (+)", "Higher Magnetic Field Strength increases the signal-to-noise ratio of the detected radiofrequency emissions from hydrogen nuclei. More signal relative to noise allows finer spatial detail to be resolved, improving Image Resolution approximately proportionally to field strength."),
        ("Magnetic Field Strength to Tissue Contrast", "POSITIVE (+)", "Higher Magnetic Field Strength increases the difference in signal intensity between different tissue types because the Boltzmann distribution creates a larger population difference between aligned and anti-aligned spin states, enhancing the contrast-generating relaxation time differences."),
        ("Image Resolution to Diagnostic Accuracy", "POSITIVE (+)", "Higher Image Resolution allows radiologists to detect smaller abnormalities and distinguish fine structural details, directly improving the probability of correct diagnosis. A 1mm resolution MRI can detect tumors invisible on a 3mm resolution scan.")
    ],
    "sim_answers": [
        ("Standard 1.5T Scenario", "At 1.5 Tesla, the MRI produces clinical-quality images with adequate Image Resolution (approximately 1mm) and good Tissue Contrast for most diagnostic purposes. Patient Safety is well-managed at this field strength with standard screening protocols. Energy Consumption is substantial but manageable for hospital infrastructure. Diagnostic Accuracy is sufficient for the vast majority of clinical indications — this is why 1.5T remains the global clinical workhorse."),
        ("Coil Failure Scenario", "When Coil Temperature rises above the superconducting critical point (9.2K for NbTi), electrical resistance suddenly appears. The enormous current (hundreds of amperes) generates intense heat, which boils the liquid helium explosively. The magnetic field collapses in seconds as the quench propagates through all coils. The scanner becomes non-functional, requiring weeks of repair, re-cooling, and re-energization. In worst cases, the explosive helium boil-off can displace oxygen from the scanner room, creating an asphyxiation hazard.")
    ],
    "reflection_exemplars": [
        ("Why is MRI safer than CT but more expensive?", "MRI uses non-ionizing radiation (radiofrequency waves) while CT uses ionizing X-rays that can damage DNA and increase cancer risk. This makes MRI inherently safer for repeated imaging and for vulnerable populations like children and pregnant women. However, MRI's safety comes at an engineering cost: generating the powerful magnetic field requires superconducting coils cooled to near absolute zero with liquid helium, which is expensive to install, maintain, and operate. A CT scanner costs $500K-$1M; an MRI costs $1-3M. CT scan costs $200-$1,000; MRI scan costs $500-$5,000."),
        ("Why is there an optimal field strength?", "The model shows that increasing Magnetic Field Strength improves Image Resolution and Tissue Contrast, but with diminishing returns at higher strengths. Meanwhile, Patient Safety concerns increase because stronger fields create greater forces on metallic implants, higher RF energy deposition (SAR), and louder noise. Energy Consumption scales with field strength as well. For most clinical diagnoses, 1.5T provides sufficient quality at manageable cost and safety. 3T is used when higher resolution is needed (neuroimaging, research). 7T and above are research-only because Patient Safety challenges become severe.")
    ],
    "stem_intro": "Present the challenge: A medical startup wants to bring MRI to the 70% of the world without access. Your team will design a portable MRI system that dramatically reduces cost, size, and power requirements — accepting some image quality trade-offs to make the technology accessible to billions of people.",
    "stem_concepts": [
        ("Permanent Magnet MRI", "Instead of superconducting coils requiring liquid helium, portable MRI systems can use permanent magnets made of rare-earth materials (neodymium). These generate weaker fields (0.05-0.5T) but require no cooling, no electricity for the magnet, and weigh hundreds of kilograms instead of tons. The trade-off is lower Image Resolution and longer scan times."),
        ("Point-of-Care Diagnostics", "In resource-limited settings, the diagnostic question is often simpler: Is there a stroke? Is this bone fractured? Is there a brain tumor? These binary diagnostic decisions may not require 1mm resolution — a portable 0.05T system that can answer these questions could save more lives than a 3T research scanner that serves only wealthy hospitals."),
        ("AI-Enhanced Imaging", "Machine learning algorithms can significantly improve the quality of images from low-field MRI systems by reducing noise, enhancing contrast, and compensating for resolution limitations. This allows portable MRI to approach diagnostic accuracy of higher-field systems for specific clinical questions.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design specifies magnet type, field strength, target diagnostic applications, power and cooling requirements, estimated cost, AI enhancement strategy, and addresses patient safety — with model data justifying all trade-off decisions"),
        ("Proficient (3)", "Design addresses magnet technology and target applications with reasonable specifications and some model-based justification"),
        ("Developing (2)", "Design includes some specifications but lacks clear trade-off analysis or connection to model evidence"),
        ("Beginning (1)", "Design is incomplete or does not address the fundamental physics constraints of portable MRI")
    ],
    "support": [
        "Provide a comparison chart showing field strength, image resolution, cost, weight, and power requirements for 3T, 1.5T, 0.5T, and 0.05T MRI systems",
        "Use a diagram showing the basic MRI signal chain: magnetic field alignment, RF pulse excitation, relaxation signal emission, and image reconstruction",
        "Sentence frames: 'When Magnetic Field Strength is reduced from __ to __, Image Resolution decreases by approximately __ because __, but the system becomes portable because __'"
    ],
    "extensions": [
        "Research the Hyperfine Research portable MRI system (0.064T, $50,000) and analyze how it achieves diagnostic utility at a fraction of the cost and field strength of traditional systems",
        "Investigate functional MRI (fMRI) and how it detects brain activity by measuring blood oxygen level changes — model how this extends MRI from structural to functional imaging",
        "Compare the physics of MRI, CT, PET, and ultrasound imaging and create a decision guide for when each modality is most appropriate"
    ],
    "cross_curr": [
        ("Math", "Calculate the Larmor frequency for hydrogen protons at 1.5T and 3T (gyromagnetic ratio = 42.576 MHz/T) and explain why different field strengths require different RF frequencies"),
        ("ELA", "Write a patient information sheet that explains MRI in accessible language, addressing common fears (claustrophobia, loud noise, magnetic safety) while accurately conveying the science"),
        ("Social Studies", "Research global access to medical imaging technology and analyze how the distribution of MRI machines correlates with national wealth, healthcare spending, and health outcomes")
    ],
    "misconceptions": [
        ("MRI uses radiation like X-rays", "MRI uses radiofrequency electromagnetic radiation, which is non-ionizing — the same fundamental type as FM radio signals and Wi-Fi, just at specific frequencies that resonate with hydrogen nuclei. Unlike X-rays and CT scans, MRI does not use ionizing radiation that can damage DNA. This is why MRI is preferred for repeated imaging and for patients where radiation exposure is a concern (children, pregnant women).", "Compare photon energies: An X-ray photon carries enough energy to ionize atoms and break DNA bonds. An MRI radiofrequency photon has about 100 million times LESS energy per photon — far too low to cause any ionization damage."),
        ("Stronger magnets are always better for MRI", "While higher field strength improves signal-to-noise ratio and image resolution, it also increases safety risks (stronger forces on metallic objects, higher SAR), cost, energy consumption, and technical complexity. For most clinical diagnoses, 1.5T provides sufficient image quality. The trend toward higher fields (3T, 7T) is driven by research applications that need extremely fine detail, not by clinical necessity.", "Real-world context: Most hospitals worldwide use 1.5T MRI and achieve excellent diagnostic outcomes. A 3T scanner costs 50-100% more to purchase and operate but provides only marginal improvement for the majority of clinical scans."),
        ("MRI is perfectly safe for everyone", "While MRI does not use ionizing radiation, it is not risk-free. The powerful magnetic field can turn ferromagnetic objects into dangerous projectiles, cause implanted devices (pacemakers, neurostimulators) to malfunction, and move metallic foreign bodies within the body. The RF pulses deposit thermal energy in tissue, which can be problematic at high field strengths. The gradient coil switching produces noise levels up to 130 dB — loud enough to cause hearing damage without ear protection.", "Safety perspective: More people have been injured by MRI accidents involving metallic objects being pulled into the scanner than by any radiation effect from MRI — because the radiation risk is essentially zero but the magnetic projectile risk is real and immediate.")
    ]
}

L10 = {
    "id": "G10L2-L10",
    "title": "Why Do Animals Migrate Thousands of Miles?",
    "subtitle": "Modeling the Costs and Benefits of Long-Distance Animal Migration",
    "ngss": "HS-LS2-8, HS-LS4-6",
    "ngss_desc": "Evaluate evidence for the role of group behavior on individual and species' chances of survival and reproduction. Create or revise a simulation to test a solution to mitigate adverse impacts of human activity on biodiversity.",
    "big_question": "Why would an animal risk a journey of thousands of miles through storms, predators, and starvation — and how do millions of them navigate with pinpoint accuracy?",
    "objectives": [
        "Model how navigation accuracy, energy reserves, and environmental triggers interact to determine migration success or failure",
        "Analyze the cost-benefit calculation that makes migration an evolutionary winning strategy despite enormous individual risk",
        "Predict how climate change, habitat loss, and human infrastructure are disrupting ancient migration routes",
        "Evaluate how group behavior and collective navigation improve individual survival probability during migration"
    ],
    "vocabulary": [
        ("Magnetoreception", "The biological ability to detect Earth's magnetic field for navigation, found in birds, sea turtles, salmon, and other migratory species — likely using magnetite crystals or cryptochrome proteins in the retina"),
        ("Stopover Ecology", "The study of critical rest and refueling locations along migration routes where animals replenish energy reserves — loss of these sites can cause population-level collapse even if breeding and wintering grounds are intact"),
        ("Phenological Mismatch", "A disruption in the timing alignment between seasonal events — when migratory animals arrive at breeding grounds but the food resources they depend on have already peaked due to climate-shifted timing"),
        ("Zugunruhe", "Migratory restlessness — the innate behavioral drive triggered by changing day length and internal biological clocks that compels migratory animals to begin their journey at the genetically programmed time")
    ],
    "components": [
        ("Navigation Accuracy", "The precision with which migrating animals follow their genetically encoded or learned route, using a combination of magnetic field detection, celestial cues, landmarks, and olfactory signals", False),
        ("Energy Reserves", "The total caloric reserves (primarily fat stores) available for the migration journey, which must be sufficient to fuel continuous flight, swimming, or walking for days to weeks between refueling stops", False),
        ("Climate Trigger", "The environmental signal — primarily day length (photoperiod) and temperature — that initiates migratory restlessness and determines the timing of departure and arrival", True),
        ("Predator Avoidance", "The ability of migrating animals to detect and evade predators during the journey, which is enhanced by group behavior but compromised by exhaustion and unfamiliar territory", False),
        ("Group Size", "The number of individuals migrating together, which affects navigation accuracy through collective intelligence, predator dilution, energy efficiency through drafting, and social information sharing", False),
        ("Food Availability", "The abundance of food resources at stopover sites and the final destination, which must align temporally with the species' arrival — increasingly disrupted by climate change", True),
        ("Reproductive Success", "The ultimate evolutionary payoff of migration — the number of offspring successfully produced at the destination, which must exceed the mortality cost of the journey for migration to be evolutionarily stable", False)
    ],
    "think_about_it": "Migration is an enormous gamble: Energy Reserves must last the journey, Navigation Accuracy must hold through storms and unfamiliar terrain, and Food Availability at the destination must be sufficient. Climate change is shifting the Climate Trigger timing while independently shifting Food Availability timing. What happens when these two clocks go out of sync?",
    "scenarios": [
        ("Optimal Migration", "Set all components to favorable conditions — observe how successful migration maximizes Reproductive Success"),
        ("Climate Mismatch", "Shift Food Availability timing earlier while keeping Climate Trigger unchanged — observe the phenological mismatch effect"),
        ("Habitat Fragmentation", "Reduce Food Availability at key stopover sites — observe how losing refueling stations collapses the entire migration")
    ],
    "sim_scenarios": [
        ("Optimal Conditions", "Aligned timing, abundant stopovers, large groups", "What do you predict happens to Reproductive Success when all migration components are functioning optimally?"),
        ("Climate Mismatch", "Food peaks earlier than arrival time", "What do you predict happens when migratory birds arrive at breeding grounds two weeks after the insect population has already peaked?"),
        ("Stopover Loss", "Critical refueling sites destroyed", "Do you predict that animals can complete migration if one major stopover site along the route is lost to development?")
    ],
    "discoveries": [
        "Migration persists because the Reproductive Success at distant destinations exceeds the mortality cost of the journey — it's an evolutionary cost-benefit calculation that has been refined over millions of years",
        "Group Size provides compound benefits: collective navigation averaging (the 'many wrongs' principle), predator dilution, aerodynamic drafting, and social information about food and danger",
        "Phenological mismatch from climate change is the most insidious threat to migration because it disrupts the timing coordination that migration depends on — animals arrive on schedule but food does not",
        "Stopover sites are the 'gas stations' of migration — losing even a single critical stopover can cause population collapse across the entire route, making habitat at rest stops as important as habitat at destinations"
    ],
    "answer": "Animals migrate thousands of miles because the evolutionary payoff — access to abundant food, optimal breeding conditions, and seasonal resources — exceeds the enormous cost of the journey. Arctic terns fly 71,000 km annually because the polar summers provide 24-hour daylight and explosive insect production for chick-rearing. Wildebeest cross crocodile-infested rivers because the Serengeti grasslands cycle between regions. Monarch butterflies fly 4,000 km because Mexican mountain forests provide the exact microclimate for winter survival. Navigation uses a remarkable toolkit: Earth's magnetic field detected by magnetite crystals, star patterns for celestial navigation, the Sun's position corrected by an internal clock, learned landmarks, and even olfactory maps. The journey succeeds because millions of years of natural selection have optimized every component — energy storage, navigation precision, timing, and group behavior. But this finely tuned system is now threatened by climate change shifting the timing of food resources while migration triggers remain fixed, and by habitat loss destroying the critical stopover sites that migrants depend on for refueling.",
    "stem_title": "Design a Migration Corridor Conservation Plan",
    "stem_mission": "Design a conservation strategy that protects a complete migration corridor — including breeding grounds, stopover sites, and wintering habitat — for a threatened migratory species.",
    "stem_scenario": "A conservation organization has identified that a migratory shorebird population has declined 70% in 20 years. Analysis shows the decline is caused by loss of three critical stopover sites along their 10,000 km migration route. Your team has been hired to design a corridor conservation plan that protects the most critical habitats across multiple countries.",
    "stem_questions": [
        "How would you identify which stopover sites are most critical to protect first?",
        "How would you coordinate conservation across the multiple countries the migration route crosses?",
        "What monitoring systems would tell you whether your conservation plan is working?"
    ],
    "stem_design_qs": [
        "What criteria would you use to prioritize habitat protection — stopover site quality, threatened species density, feasibility of protection, or cost?",
        "How would you design protected areas that are resilient to climate change shifting the migration timing?",
        "What economic incentives could encourage local communities along the route to protect migration habitat?",
        "How would you use satellite tracking and population data to measure conservation outcomes?"
    ],
    "career": "Migration Ecologists study the movement patterns, physiology, and conservation needs of migratory animals. They work for wildlife agencies, conservation organizations, and universities, earning $55,000–$120,000/year. Wildlife Corridor Planners who design connected habitat networks earn $60,000–$110,000/year.",
    "images": {
        "cover": ("G10L2-L10-cover.png", "A photorealistic, cinematic image of a massive flock of migratory birds in V-formation against a dramatic sunset sky, hundreds of birds stretching across the frame with golden and orange light filtering through their wings, conveying the epic scale of long-distance migration"),
        "landscape": ("G10L2-L10-landscape.png", "A diverse group of 15-16 year old students in a modern biology lab examining migration route maps and bird specimens, binoculars and field guides on tables, world map showing migration corridors on the wall, engaged and curious expressions, natural classroom lighting"),
        "modeling": ("G10L2-L10-modeling.png", "A diverse group of 15-16 year old students working on laptops building computational models of migration dynamics, screens showing route maps and energy budget graphs, modern classroom with wildlife posters and globe"),
        "discussion": ("G10L2-L10-discussion.png", "A teacher leading an animated discussion with diverse 15-16 year old students about animal migration, a world map showing major flyways and migration routes displayed on a smartboard, students raising hands enthusiastically"),
        "stem": ("G10L2-L10-stem.png", "Diverse 15-16 year old students designing migration corridor conservation plans with maps showing protected areas and habitat connectivity on large displays, collaborative atmosphere with satellite imagery and wildlife data visible")
    },
    "pre_assessment": [
        "Why do you think animals like birds, whales, and butterflies migrate thousands of miles instead of staying in one place?",
        "How do you think animals navigate across oceans and continents without maps or GPS?",
        "Draw a diagram showing what you think a migratory bird needs to survive a 5,000-mile journey.",
        "What threats do you think migratory animals face today that they didn't face 100 years ago?"
    ],
    "extend_components": [
        ("Light Pollution", "Artificial light from cities that disorients nocturnal migrating birds, causing them to circle illuminated buildings until exhaustion — an estimated 1 billion birds die annually from building collisions during migration in the US alone"),
        ("Wind Pattern Shifts", "Changes in prevailing wind patterns due to climate change that alter the energy cost of migration — tailwinds become headwinds, increasing the fat reserves needed and the risk of exhaustion during ocean crossings"),
        ("Genetic Program Fidelity", "The accuracy of the inherited genetic instructions that encode migration direction, distance, and timing — which can only evolve over many generations and cannot adapt to rapid environmental changes within a few decades")
    ],
    "reflections": [
        "How does your model demonstrate that migration is an evolutionary cost-benefit calculation rather than a simple instinct?",
        "What does your model reveal about why phenological mismatch is a more serious threat than direct habitat loss for some migratory species?",
        "How does Group Size improve individual survival — what mechanisms make collective migration safer than solo migration?",
        "Why are stopover sites the 'weakest links' in the migration system, according to your model?",
        "What are the limitations of modeling migration with only seven components when real migration involves weather unpredictability, individual learning, and complex social dynamics?"
    ],
    "dimensions": [
        ("Science Practice", "Constructing Explanations and Designing Solutions", "Students construct evidence-based explanations of why migration evolved and design conservation solutions to protect migration corridors from climate change and habitat loss."),
        ("Disciplinary Core Idea", "LS2.D Social Interactions and Group Behavior / LS4.C Adaptation", "Group behaviors such as collective migration enhance individual survival and reproductive success; natural selection has shaped migration as an adaptive response to seasonal resource variation."),
        ("Crosscutting Concept", "Cause and Effect", "Students trace the causal chains from environmental triggers through physiological responses and behavioral decisions to population-level outcomes, identifying how disruption at any link can collapse the entire migration system.")
    ],
    "cast_items": [
        "Model how environmental triggers, energy management, navigation, and group behavior interact to determine migration success",
        "Analyze how climate change creates phenological mismatches that undermine the evolutionary benefits of migration",
        "Design conservation strategies that protect complete migration corridors including critical stopover habitats"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Climate change causes spring insect emergence to occur two weeks earlier at a bird's breeding ground, but the bird's migration departure is triggered by day length, which has not changed. Based on your model, what is the most likely consequence?"),
        ("Constructed Response:", "Using your model, explain why the destruction of a single stopover wetland in Delaware could contribute to the decline of a shorebird species that breeds in the Arctic and winters in South America. Reference Energy Reserves, Food Availability, and Reproductive Success in your explanation.")
    ],
    "background_intro": "Every year, billions of animals undertake journeys that would be extraordinary even with modern technology. Arctic terns fly from pole to pole — 71,000 kilometers annually. Bar-tailed godwits fly 11,000 km non-stop across the Pacific Ocean without resting. Monarch butterflies navigate 4,000 km to a specific mountain forest in Mexico that no individual butterfly has ever visited before. Migration is one of evolution's most remarkable achievements — and one of its most fragile.",
    "background_sections": [
        ("Why Migrate? The Cost-Benefit Equation", "Migration is extraordinarily dangerous — an estimated 50-80% of some migratory bird species die during migration each year. So why do it? Because the reproductive payoff exceeds the survival cost. High-latitude breeding grounds offer longer daylight hours for foraging, explosive seasonal food production (insect hatches, plant blooming), fewer parasites and diseases, and less competition. A bird that migrates to the Arctic and raises a clutch of 6 chicks — even if 50% die on the return migration — still produces more surviving offspring than a sedentary relative in the tropics that raises 2 chicks. Natural selection favors the strategy with the highest net reproductive output, even if individual risk is extreme."),
        ("Navigation: A Biological GPS", "Migratory animals use a multi-modal navigation system of astonishing sophistication. The magnetic compass uses magnetite crystals or cryptochrome proteins to detect Earth's magnetic field direction and intensity. The celestial compass uses the sun's position (time-compensated by an internal circadian clock) during the day and star patterns at night. The olfactory map uses chemical gradients in air or water (salmon use this to find their natal stream). Landmarks and memory allow experienced migrants to recognize landscape features. The 'many wrongs' principle explains collective navigation: individual birds make small navigation errors in random directions, but averaging across a flock cancels errors and produces a more accurate group trajectory than any individual could achieve alone."),
        ("The Phenological Mismatch Crisis", "Migration timing evolved to synchronize with seasonal food availability. Arctic-breeding birds arrive when insect populations explode. Whales arrive when krill blooms occur. This synchronization developed over millions of years of coevolution. Climate change is disrupting this synchronization because different components of the system respond to different cues. Plants and insects respond to temperature — which is shifting earlier. But many migratory animals respond to day length (photoperiod) — which does not change with climate. The result is phenological mismatch: birds arrive on their genetically programmed schedule only to find that the food peak occurred two weeks ago. Populations that depend on this timing are declining rapidly."),
        ("Stopover Ecology: The Critical Link", "A migratory shorebird flying from Argentina to the Arctic cannot carry enough fat to make the trip in one flight. It must stop at specific locations to rest and refuel — often for just 2-3 weeks, doubling its body weight before continuing. Delaware Bay, for example, hosts 1 million shorebirds each May that depend on horseshoe crab eggs to fuel the final leg to the Arctic. If Delaware Bay is degraded, the entire flyway population collapses — even though breeding and wintering habitats are intact. The chain is only as strong as its weakest link, and stopover sites are increasingly threatened by coastal development, pollution, and climate change.")
    ],
    "lever_L": "Students identify seven components of the migration system: Navigation Accuracy, Energy Reserves, Climate Trigger, Predator Avoidance, Group Size, Food Availability, and Reproductive Success — with Climate Trigger and Food Availability as external environmental conditions.",
    "lever_E": "Students determine that Climate Trigger initiates migration timing, but Food Availability at the destination determines whether arriving migrants can successfully breed. Energy Reserves must be sufficient for the journey, Navigation Accuracy determines route efficiency, and Group Size affects both navigation and predator survival. Reproductive Success is the ultimate outcome.",
    "lever_V": "Students build a computational model showing how the timing and spatial requirements of migration must align for populations to sustain themselves across generations.",
    "lever_Ev": "Students run optimal migration, climate mismatch, and habitat fragmentation scenarios to determine which disruptions are most damaging to population viability.",
    "lever_R": "Students add Light Pollution, Wind Pattern Shifts, or Genetic Program Fidelity to explore how additional human-caused and evolutionary factors affect migration success.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic migratory bird flock image", "say": "A bird the size of your fist just flew 11,000 kilometers non-stop across the Pacific Ocean. No food. No rest. No GPS. How?", "do": "Show the bar-tailed godwit non-stop Pacific crossing data on a map. Let the distance sink in. Ask: Could any human-built drone do this?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary terms", "say": "Today you're modeling one of nature's most extreme behaviors — and asking why natural selection would favor such a dangerous strategy.", "do": "Have students read objectives. Pre-teach 'magnetoreception' and 'phenological mismatch.' Quick-write: Why would an animal choose the most dangerous possible way to live?", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why do animals migrate thousands of miles?", "say": "Migration kills 50-80% of some species every year. By any common-sense measure, it seems insane. But evolution doesn't do insane — it does math. What's the equation?", "do": "Students calculate: If migration kills 60% of birds but survivors produce 6 chicks, while staying put kills 10% but produces only 2 chicks — which strategy wins? (Migration: 0.4 x 6 = 2.4 offspring vs. Sedentary: 0.9 x 2 = 1.8 offspring.)", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're modeling the most dangerous commute in the natural world — and figuring out how climate change is about to break it.", "do": "Preview each LEVER step. Emphasize that migration is a cost-benefit optimization refined by millions of years of evolution.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Seven component cards for migration model", "say": "Seven factors determine whether a migration succeeds or fails. Two come from the environment. The rest come from the animal and its flock.", "do": "Guide component sorting. Discuss why Climate Trigger and Food Availability are external (environmental conditions) while biological capabilities are internal responses shaped by evolution.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between migration components", "say": "The migration system is a precision machine with zero margin for error. Change one thing — timing, fuel, route, food — and the whole system can collapse.", "do": "Help students map the connections. Identify why Energy Reserves at stopover sites are the bottleneck and how Group Size improves multiple components simultaneously.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and simulation results", "say": "Three scenarios: perfect migration, climate mismatch, and lost stopovers. Your model will show which one is most devastating.", "do": "Students predict outcomes. Run all three scenarios. The phenological mismatch scenario often surprises students — it's more damaging than they expect because it undermines Reproductive Success, not just survival.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from migration model", "say": "Migration is not about strength or speed — it's about timing, fuel, and precision. And we're disrupting all three simultaneously.", "do": "Lead discussion connecting model findings to real species declines. Show satellite tracking data of actual migratory routes. Discuss which species are most vulnerable.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Migration corridor conservation plan design", "say": "A shorebird population has crashed 70%. The stopovers are gone. Design the conservation plan that saves them — across international borders.", "do": "Groups design corridor conservation plans specifying which habitats to protect, how to coordinate across countries, and how to monitor success. Present as proposals to a simulated conservation board.", "time": "12 min"}
    ],
    "sort_reasoning": "Climate Trigger and Food Availability are external components because they are environmental conditions outside the control of the migrating animals. Climate Trigger (photoperiod, temperature) is determined by Earth's orbital mechanics and atmospheric conditions. Food Availability depends on ecosystem productivity at destinations and stopovers, influenced by climate, land use, and ecological interactions. Navigation Accuracy, Energy Reserves, Predator Avoidance, Group Size, and Reproductive Success are internal because they are biological traits and outcomes shaped by evolution and determined by the organism's physiology and behavior.",
    "relationships": [
        ("Climate Trigger to Energy Reserves", "POSITIVE (+)", "Appropriate Climate Trigger timing initiates migratory preparation, including hyperphagia (excessive eating) that builds fat reserves for the journey. Birds can double their body weight in 2-3 weeks of pre-migration feeding, converting food to the high-energy fat stores needed for sustained flight."),
        ("Energy Reserves to Navigation Accuracy", "POSITIVE (+)", "Adequate Energy Reserves allow migrants to fly at optimal altitudes and speeds for navigation rather than being forced into energy-saving behaviors that compromise route accuracy. Well-fueled birds can maintain precise compass headings; exhausted birds make more navigation errors and may be forced to land in suboptimal locations."),
        ("Food Availability to Reproductive Success", "POSITIVE (+)", "Higher Food Availability at breeding grounds directly increases Reproductive Success by providing the caloric resources needed for egg production, nestling growth, and adult survival during the breeding season. When food peaks align with arrival timing, clutch sizes are larger and chick survival rates are higher.")
    ],
    "sim_answers": [
        ("Optimal Migration Scenario", "With all components at favorable levels, migration proceeds smoothly. Climate Trigger initiates departure at the correct time. Energy Reserves are built up at productive stopovers. Navigation Accuracy guides the flock along an efficient route. Group Size provides protection and collective navigation. Food Availability at the destination peaks at arrival time. Reproductive Success is high — the evolutionary cost-benefit calculation favors migration. Population is stable or growing."),
        ("Climate Mismatch Scenario", "When Food Availability timing shifts earlier due to warming but Climate Trigger (photoperiod) remains unchanged, migrants arrive to find the food peak has already passed. Chick provisioning rates drop because parents must forage harder for declining food resources. Nestling growth slows, fledging weight decreases, and first-year survival drops. Reproductive Success declines below the threshold needed to offset migration mortality. Over successive generations, the population spirals downward even though habitat appears intact — the problem is invisible because it's a timing mismatch, not a physical destruction.")
    ],
    "reflection_exemplars": [
        ("Why is phenological mismatch so devastating?", "The model reveals that phenological mismatch attacks Reproductive Success — the evolutionary reason migration exists. Unlike habitat loss (which reduces where animals can go) or predation (which reduces how many survive the journey), mismatch undermines why they migrate at all. If arriving migrants can no longer access the seasonal resource bonanza that makes the dangerous journey worthwhile, the cost-benefit equation flips — migration becomes a net evolutionary loss. The insidious part is that nothing visible has changed. The habitat looks fine. The stopovers are intact. The route is clear. But the timing clock is broken, and that clock took millions of years to calibrate."),
        ("Why are stopover sites as important as destination habitat?", "The model shows that Energy Reserves are the critical bottleneck during migration. Most migratory species cannot carry enough fat to fly their entire route non-stop — they must refuel at specific stopover locations. If a stopover is degraded or destroyed, migrants cannot replenish Energy Reserves for the next leg. Even animals with perfect Navigation Accuracy and optimal Climate Trigger timing will fail if they arrive at a stopover and find no food. A migratory route is like a chain of fuel stations across a desert — remove one station and the journey becomes impossible even though all others are intact.")
    ],
    "stem_intro": "Present the challenge: A migratory shorebird has declined 70% in 20 years because three critical stopover wetlands along its 10,000 km route have been degraded by coastal development. Your team will design a corridor conservation plan that identifies, protects, and monitors the most important habitats across multiple countries.",
    "stem_concepts": [
        ("Flyway Conservation", "Migration corridors (flyways) cross international boundaries, requiring cooperation between multiple countries. The East Asian-Australasian Flyway, for example, spans 22 countries from Arctic Russia to New Zealand. Effective conservation requires international treaties, coordinated habitat protection, and shared monitoring data."),
        ("Critical Habitat Identification", "Satellite tracking reveals exactly which stopover sites individual birds use, how long they stay, and how much weight they gain. Combining tracking data with habitat surveys identifies sites where protection would have the greatest impact on population survival."),
        ("Citizen Science Monitoring", "Programs like eBird and the Christmas Bird Count enlist millions of volunteer observers to track bird populations and migration timing across entire continents. This crowdsourced data provides the large-scale monitoring that professional scientists alone could never achieve.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan identifies priority habitats using satellite tracking and population data, proposes international coordination mechanisms, includes monitoring protocols with measurable outcomes, addresses climate adaptation, and uses model evidence to justify priorities"),
        ("Proficient (3)", "Plan identifies important habitats and proposes protection measures with some monitoring and model-based justification"),
        ("Developing (2)", "Plan addresses some habitats but lacks prioritization criteria, monitoring plan, or international coordination strategy"),
        ("Beginning (1)", "Plan is incomplete or protects only one location without considering the full corridor")
    ],
    "support": [
        "Provide a flyway map showing the migration route, stopover sites, breeding grounds, and wintering grounds with threat assessments at each location",
        "Use an energy budget diagram showing how much fat a shorebird burns per 1,000 km and how much it needs to gain at each stopover",
        "Sentence frames: 'When Food Availability at the __ stopover site declines, migrants arrive at the next leg with __ Energy Reserves, which means __ because __'"
    ],
    "extensions": [
        "Research the decline of the red knot shorebird and its dependence on horseshoe crab eggs in Delaware Bay — model how overharvesting of horseshoe crabs caused a population crash 5,000 km away in the Arctic",
        "Investigate how monarch butterfly migration is a multi-generational relay — no individual completes the round trip — and analyze how this unique system is threatened by milkweed loss and climate change",
        "Compare the navigation systems of different migratory species (birds using magnetic fields, sea turtles using ocean currents, salmon using olfaction) and evaluate which are most vulnerable to human disruption"
    ],
    "cross_curr": [
        ("Math", "Calculate the energy budget for a 10,000 km migration: fat calories stored, calories burned per km, minimum stopover duration needed to refuel, and the margin of error if one stopover is degraded"),
        ("ELA", "Write a science narrative following a single bird's migration journey from South America to the Arctic, incorporating the scientific concepts of navigation, energy management, and climate timing"),
        ("Social Studies", "Research the Migratory Bird Treaty Act and international flyway agreements, analyzing how international cooperation has succeeded and failed in protecting migratory species")
    ],
    "misconceptions": [
        ("Animals migrate to escape cold weather", "While temperature plays a role, migration is primarily driven by food availability, not cold avoidance. Many migratory birds can physiologically tolerate cold temperatures — they leave because food resources (insects, nectar, small mammals) disappear in winter, not because it's too cold. This is why some species migrate to tropical regions that are actually warmer than necessary for survival — they're following the food, not the thermostat.", "Evidence: Some bird species that eat seeds (which remain available in winter) do NOT migrate, while insect-eating species from the same habitat DO migrate. If it were about cold, all species would leave."),
        ("Migration routes are learned from parents", "While some species (geese, cranes) learn routes by following experienced adults, many migrants are entirely self-navigating on their first trip. Juvenile cuckoos, raised by foster parents of a different species, migrate to Africa alone — having never seen the route and without any adult cuckoo to follow. Their navigation is genetically encoded: the direction, distance, and timing are inherited, not learned.", "Stunning example: Hand-raised starlings displaced 600 km from their capture site navigate to the correct wintering ground — not the original capture site and not where they were released — proving that migration direction is innate, not learned."),
        ("Human activity doesn't affect migration much", "Human activity is the primary threat to migratory species worldwide. Light pollution kills an estimated 1 billion birds annually in the US alone by disorienting nocturnal migrants. Wind turbines and communication towers kill hundreds of millions more. Coastal development destroys critical stopover wetlands. Climate change disrupts timing synchronization. Agricultural conversion eliminates grassland and forest habitat along routes. Migratory species are declining 2-3 times faster than sedentary species precisely because they depend on a chain of habitats across thousands of miles — and humans are degrading links across the entire chain.", "Statistic: In North America, migratory bird populations have declined by 3 billion individuals (29%) since 1970. That's nearly one in three migratory birds gone in 50 years.")
    ]
}

ALL_LESSONS = [L01, L02, L03, L04, L05, L06, L07, L08, L09, L10]
