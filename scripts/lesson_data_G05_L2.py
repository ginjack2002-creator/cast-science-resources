#!/usr/bin/env python3
"""Complete lesson data for Grade 5 Level 2 (G05L2-L01 through G05L2-L10)"""

L01 = {
    "id": "G05L2-L01",
    "title": "The Carbon Cycle: Where Does Your Breath Go?",
    "subtitle": "How Carbon Travels Between Air, Plants, Soil, and Back Again",
    "ngss": "5-LS1-1, 5-LS2-1",
    "ngss_desc": "Develop a model to describe the movement of matter among plants, animals, decomposers, and the environment. Support an argument that plants get the materials they need for growth chiefly from air and water.",
    "big_question": "Where does the carbon in your breath go, and how does it come back?",
    "objectives": [
        "Trace carbon as it moves between the atmosphere, plants, soil, and back",
        "Model how CO2 levels and sunlight affect photosynthesis rate",
        "Explain the role of decomposition in releasing stored carbon",
        "Predict what happens to atmospheric CO2 when photosynthesis stops"
    ],
    "vocabulary": [
        ("Carbon Dioxide (CO2)", "A gas in the atmosphere that plants absorb and animals exhale"),
        ("Photosynthesis", "The process plants use to convert CO2 and sunlight into food"),
        ("Decomposition", "The breakdown of dead organisms by bacteria and fungi"),
        ("Carbon Cycle", "The continuous movement of carbon through living and nonliving systems")
    ],
    "components": [
        ("CO2 in Atmosphere", "The amount of carbon dioxide gas in the air", True),
        ("Sunlight Intensity", "The amount of solar energy reaching plants", True),
        ("Photosynthesis Rate", "How fast plants absorb CO2 and convert it to sugar", False),
        ("Decomposition Rate", "How fast dead organisms are broken down, releasing carbon", False),
        ("Soil Carbon Storage", "The amount of carbon locked in the ground from dead plants", False)
    ],
    "think_about_it": "When there is more CO2 in the atmosphere, what do you think happens to the rate of photosynthesis?",
    "scenarios": [
        ("Normal Carbon Cycle", "Set CO2 and Sunlight to moderate levels and observe the cycle"),
        ("Sunlight Shutdown", "Lock Sunlight Intensity to 0% and watch what happens to CO2"),
        ("High CO2 World", "Set CO2 in Atmosphere to 90% and observe how plants respond")
    ],
    "sim_scenarios": [
        ("Normal Carbon Cycle", "Moderate CO2 and sunlight levels", "What do you predict will happen to Soil Carbon Storage over time?"),
        ("Sunlight Shutdown", "Lock Sunlight Intensity to 0%", "What do you predict will happen to CO2 in Atmosphere when plants can't photosynthesize?"),
        ("High CO2 World", "Set CO2 to 90%", "What do you predict will happen to Photosynthesis Rate?")
    ],
    "discoveries": [
        "Carbon moves in a CYCLE, not a one-way path — it loops between air, plants, soil, and back",
        "Photosynthesis removes CO2 from the atmosphere, acting like a natural filter",
        "Decomposition releases stored carbon back into the atmosphere as CO2",
        "When sunlight disappears, photosynthesis stops and CO2 builds up in the air"
    ],
    "answer": "The carbon in your breath is absorbed by plants during photosynthesis, stored in their bodies, and released back into the air when dead plants decompose. It is an endless cycle!",
    "stem_title": "Design a Carbon-Capturing Schoolyard",
    "stem_mission": "Design a schoolyard landscape that maximizes carbon capture from the atmosphere.",
    "stem_scenario": "Your school district wants to reduce its carbon footprint. They've asked your class to redesign the schoolyard to absorb as much CO2 as possible.",
    "stem_questions": [
        "Which types of plants absorb the most CO2?",
        "How does soil health affect carbon storage?",
        "What happens to captured carbon when leaves fall and decompose?"
    ],
    "stem_design_qs": [
        "What mix of trees, shrubs, and ground cover will you plant?",
        "How will you maximize sunlight exposure for your plants?",
        "How will you manage fallen leaves and organic matter?",
        "How will you measure whether your design is actually capturing carbon?"
    ],
    "career": "Climate Scientists and Carbon Analysts study how carbon moves through Earth's systems and develop strategies to reduce CO2 in the atmosphere. They earn $70,000-$120,000/year.",
    "images": {
        "cover": ("cover-carbon-cycle.png", "A photorealistic, cinematic image of a lush green forest with visible CO2 molecules floating in the air, sunlight streaming through tree canopy, showing the invisible exchange of carbon between trees and atmosphere, ultra-crisp detail"),
        "landscape": ("landscape-carbon-cycle.png", "A photorealistic image of a White female student (age 10-11) leading a group of diverse 5th graders including Asian, Black, and Latino classmates through a forest trail, pointing at decomposing leaves on the ground, wearing modern hoodies and sneakers, natural window light filtering through trees"),
        "modeling": ("modeling-carbon-cycle.png", "A photorealistic image of a Latino male student (age 10-11) at a laptop showing a carbon cycle diagram, with Asian female, Black male, and White female classmates collaborating around the screen, modern classroom with science posters, natural light"),
        "discussion": ("discussion-carbon-cycle.png", "A photorealistic image of a Black female teacher leading a discussion about the carbon cycle with engaged 5th graders including White, Asian, Latino, and Black students raising hands, classroom whiteboard showing CO2 arrows, warm lighting"),
        "stem": ("stem-carbon-cycle.png", "A photorealistic image of an Asian male student (age 10-11) presenting a schoolyard design poster while White, Black, and Latino classmates examine plant samples, outdoor school garden setting, bright natural daylight")
    },
    "pre_assessment": [
        "When you breathe out, where does that air go? What happens to it?",
        "Do plants breathe? If so, what do they breathe in and out?",
        "Draw arrows showing how carbon might move between a tree, the air, and the soil.",
        "What do you think happens to a fallen leaf over time?"
    ],
    "extend_components": [
        ("Ocean Absorption", "Oceans absorb CO2 from the atmosphere"),
        ("Fossil Fuel Burning", "Humans release stored carbon by burning coal and oil"),
        ("Animal Respiration", "Animals breathe out CO2 from digesting food")
    ],
    "reflections": [
        "Why is the carbon cycle called a cycle and not a chain?",
        "What would happen to CO2 levels if all decomposition suddenly stopped?",
        "How are forests sometimes called 'the lungs of the Earth'?",
        "If you could add one more component to this model, what would it be and why?",
        "How does understanding the carbon cycle help us think about climate change?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model showing how carbon cycles between atmosphere, plants, soil, and back."),
        ("Disciplinary Core Idea", "LS2.B Cycles of Matter and Energy Transfer", "Matter cycles between living and nonliving parts of an ecosystem through processes like photosynthesis and decomposition."),
        ("Crosscutting Concept", "Systems and System Models", "Students model the carbon cycle as a system with feedback loops where outputs become inputs.")
    ],
    "cast_items": [
        "Trace the path of a carbon atom from the atmosphere through a plant and back",
        "Explain how photosynthesis and decomposition are connected in the carbon cycle",
        "Predict how changes in one part of the carbon cycle affect the rest"
    ],
    "cast_questions": [
        ("Multiple Choice:", "If all sunlight were blocked for a month, what would happen to CO2 levels in the atmosphere?"),
        ("Constructed Response:", "Explain how a carbon atom in the air you breathe out could end up in a tree, then in the soil, and then back in the air again.")
    ],
    "background_intro": "The carbon cycle is one of Earth's most important biogeochemical cycles. Carbon atoms move continuously between the atmosphere, living organisms, soil, and oceans in a complex loop that supports all life.",
    "background_sections": [
        ("Carbon in the Atmosphere", "Carbon dioxide makes up about 0.04% of Earth's atmosphere, but this small amount has an enormous effect on climate. Plants absorb CO2 during photosynthesis, and organisms release it during respiration and decomposition."),
        ("Photosynthesis as Carbon Capture", "During photosynthesis, plants use sunlight energy to combine CO2 from the air with water to create glucose (sugar). This effectively pulls carbon out of the atmosphere and stores it in plant tissue."),
        ("Decomposition Completes the Cycle", "When plants and animals die, decomposers (bacteria, fungi, worms) break down their bodies. This process releases the stored carbon back into the atmosphere as CO2, completing the cycle."),
        ("Soil as Carbon Storage", "Soil holds more carbon than the atmosphere and all plants combined. Organic matter in soil — decomposed leaves, roots, and organisms — acts as a long-term carbon bank that can store carbon for centuries.")
    ],
    "lever_L": "Students identify CO2 in Atmosphere, Sunlight Intensity, Photosynthesis Rate, Decomposition Rate, and Soil Carbon Storage as the five system components.",
    "lever_E": "Students determine that CO2 and Sunlight positively affect Photosynthesis, that Photosynthesis negatively affects CO2 (removes it), and that Decomposition positively affects CO2 (releases it).",
    "lever_V": "Students build the carbon cycle model showing feedback loops where photosynthesis removes CO2 and decomposition adds it back.",
    "lever_Ev": "Students run the Sunlight Shutdown scenario and observe CO2 building up when photosynthesis stops, then test the High CO2 scenario to see plants respond by photosynthesizing faster.",
    "lever_R": "Students add Ocean Absorption or Fossil Fuel Burning to explore how humans and oceans affect the carbon cycle.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Forest with CO2 molecules floating between trees and sky", "say": "Every breath you take is part of a giant cycle. Where does it go?", "do": "Have students breathe out onto their hands and ask: Where does that CO2 go?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary list", "say": "Today we trace carbon through the entire cycle.", "do": "Have students read objectives aloud and circle unfamiliar words.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Where does the carbon in your breath go?", "say": "This is the mystery we will solve with our model.", "do": "Quick-write: students write their best guess in 30 seconds.", "time": "2 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We will use all five LEVER steps to build and test our carbon cycle model.", "do": "Briefly review each step with the class.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Five component cards with descriptions", "say": "Our model has five parts. Two are external — we control them. Three are internal — they respond.", "do": "Students sort component cards into external and internal categories.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows with +/- signs", "say": "Notice that photosynthesis has a NEGATIVE effect on CO2 — it removes carbon from the air. This creates a feedback loop.", "do": "Guide students to draw all five relationship arrows in ModelIt.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph showing CO2, Photosynthesis, Decomposition over time", "say": "What happens when we take away sunlight? Let's test it.", "do": "Students run Sunlight Shutdown scenario and record observations.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings about the carbon cycle", "say": "Carbon moves in a loop, not a straight line. That's what makes it a cycle.", "do": "Class discussion: How is this different from an energy chain?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Schoolyard carbon capture design", "say": "Now use what you learned to design a carbon-capturing schoolyard.", "do": "Distribute design materials, circulate to assist groups.", "time": "10 min"}
    ],
    "sort_reasoning": "CO2 in Atmosphere and Sunlight Intensity are external because they represent environmental conditions that students can adjust. Photosynthesis Rate, Decomposition Rate, and Soil Carbon Storage are internal because they respond to and are determined by the external conditions.",
    "relationships": [
        ("CO2 in Atmosphere to Photosynthesis Rate", "POSITIVE (+)", "More CO2 gives plants more raw material for photosynthesis."),
        ("Sunlight Intensity to Photosynthesis Rate", "POSITIVE (+)", "More sunlight provides more energy for plants to photosynthesize."),
        ("Photosynthesis Rate to CO2 in Atmosphere", "NEGATIVE (-)", "Faster photosynthesis removes more CO2 from the air."),
        ("Decomposition Rate to CO2 in Atmosphere", "POSITIVE (+)", "Faster decomposition releases more stored carbon back as CO2."),
        ("Photosynthesis Rate to Soil Carbon Storage", "POSITIVE (+)", "More photosynthesis creates more plant matter that eventually stores carbon in soil.")
    ],
    "sim_answers": [
        ("Sunlight Shutdown", "When sunlight drops to 0%, photosynthesis stops completely. CO2 in Atmosphere rises steadily because decomposition continues releasing carbon but nothing is removing it. Soil Carbon Storage gradually depletes as decomposers use up stored organic matter."),
        ("High CO2 World", "When CO2 is set to 90%, photosynthesis rate increases because plants have abundant raw material. This creates a negative feedback — faster photosynthesis pulls CO2 back down. Soil Carbon Storage increases as more plant matter is produced.")
    ],
    "reflection_exemplars": [
        ("Why is the carbon cycle a cycle?", "Carbon atoms are not created or destroyed — they move continuously between the atmosphere, plants, soil, and back. Photosynthesis pulls carbon from the air into plants, and decomposition releases it back. The same carbon atoms cycle over and over."),
        ("How does this model help us think about climate change?", "If humans add extra CO2 by burning fossil fuels faster than photosynthesis and ocean absorption can remove it, CO2 accumulates in the atmosphere. The model shows that the cycle can be overwhelmed if inputs exceed outputs.")
    ],
    "stem_intro": "Present the challenge by discussing school carbon footprints. Connect to the model: every tree and plant in the schoolyard is a carbon capture machine.",
    "stem_concepts": [
        ("Tree Species Matter", "Fast-growing trees like poplars capture carbon quickly, while oaks store carbon for centuries."),
        ("Soil Health", "Healthy soil with active decomposers stores more carbon long-term than bare ground."),
        ("Ground Cover", "Grass and ground plants prevent carbon from escaping compacted, bare soil.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design includes diverse plants, soil management, and measurement plan; explains connection to carbon cycle model"),
        ("Proficient (3)", "Design addresses 2 of 3 factors (plant choice, soil, measurement) with scientific reasoning"),
        ("Developing (2)", "Design addresses 1 factor; limited connection to carbon cycle model"),
        ("Beginning (1)", "Design lacks scientific reasoning or does not address how plants capture carbon")
    ],
    "support": [
        "Provide a visual diagram of the carbon cycle with labeled arrows",
        "Use sentence frames: 'When CO2 goes up, photosynthesis goes __ because...'",
        "Pair students for model building so stronger modelers can guide peers"
    ],
    "extensions": [
        "Research how much carbon a single tree captures per year",
        "Add ocean absorption as a component and explore how oceans affect CO2",
        "Compare carbon cycles in forests, grasslands, and deserts"
    ],
    "cross_curr": [
        ("Math", "Calculate how many trees would be needed to offset the school's annual CO2 emissions"),
        ("ELA", "Write a narrative following a single carbon atom through three full cycles"),
        ("Social Studies", "Research how deforestation in the Amazon affects the global carbon cycle")
    ],
    "misconceptions": [
        ("Plants get carbon from soil", "Plants get carbon from CO2 in the AIR through photosynthesis, not from the soil. Soil provides minerals and water.", "Ask: If plants got carbon from soil, why do they have leaves reaching toward sunlight?"),
        ("Carbon is only in living things", "Carbon exists in the atmosphere (CO2), in oceans (dissolved CO2), in rocks (limestone), and in fossil fuels. Living things are just one stop on the cycle.", "Show students a piece of chalk (calcium carbonate) and explain it contains carbon."),
        ("Decomposition is bad", "Decomposition is essential for the carbon cycle. Without it, dead matter would pile up and nutrients would never return to the soil for new plants.", "Ask: What would happen to a forest if nothing ever decomposed?")
    ]
}

L02 = {
    "id": "G05L2-L02",
    "title": "Solar vs. Fossil: The Energy Showdown",
    "subtitle": "Which Power Source Wins — and What's the Tradeoff?",
    "ngss": "5-PS3-1, 5-ESS3-1",
    "ngss_desc": "Use models to describe that energy in animals' food was once energy from the sun. Obtain and combine information about ways individual communities use science ideas to protect the Earth's resources and environment.",
    "big_question": "Can solar energy replace fossil fuels, or do we need both?",
    "objectives": [
        "Compare how solar panels and fossil fuels produce electricity",
        "Model how sunlight hours and fossil fuel burn rate affect energy output and emissions",
        "Explain the relationship between CO2 emissions and air quality",
        "Evaluate the tradeoffs between solar and fossil fuel energy sources"
    ],
    "vocabulary": [
        ("Solar Energy", "Electricity generated from sunlight using solar panels"),
        ("Fossil Fuel", "Coal, oil, or natural gas formed from ancient organisms"),
        ("CO2 Emissions", "Carbon dioxide gas released into the air by burning fuels"),
        ("Air Quality Index", "A measurement of how clean or polluted the air is")
    ],
    "components": [
        ("Sunlight Hours", "The number of hours of direct sunlight per day", True),
        ("Fossil Fuel Burn Rate", "How much coal, oil, or gas is burned for energy", True),
        ("Solar Energy Output", "Electricity generated from solar panels", False),
        ("CO2 Emissions", "Greenhouse gases released into the atmosphere", False),
        ("Air Quality Index", "How clean and breathable the air is", False)
    ],
    "think_about_it": "If we increase the amount of fossil fuel being burned, what do you think happens to the air quality in a city?",
    "scenarios": [
        ("Mixed Energy", "Set both Sunlight Hours and Fossil Fuel Burn Rate to 50%"),
        ("All Solar", "Set Fossil Fuel Burn Rate to 0% and Sunlight Hours to 80%"),
        ("Cloudy Day Crisis", "Lock Sunlight Hours to 10% with Fossil Fuel at 0%")
    ],
    "sim_scenarios": [
        ("Mixed Energy", "Both sources at 50%", "What do you predict will happen to CO2 Emissions and Air Quality?"),
        ("All Solar", "Fossil Fuel at 0%, Sunlight at 80%", "What do you predict will happen to CO2 Emissions?"),
        ("Cloudy Day Crisis", "Sunlight at 10%, Fossil Fuel at 0%", "What happens to total energy output?")
    ],
    "discoveries": [
        "Solar energy produces NO CO2 emissions — it is completely clean",
        "Fossil fuels produce reliable energy but release CO2 that harms air quality",
        "Solar energy depends on sunlight — cloudy days and nighttime are a problem",
        "Replacing fossil fuels with solar improves air quality but requires backup for low-sun periods"
    ],
    "answer": "Solar energy is cleaner but depends on sunlight. Fossil fuels are reliable but pollute the air. The best solution may be a smart combination — using solar when possible and reducing fossil fuels over time.",
    "stem_title": "Design a Clean Energy Plan for Your Town",
    "stem_mission": "Design an energy plan that keeps the lights on while minimizing air pollution.",
    "stem_scenario": "Your town currently runs on 100% fossil fuels. The mayor has asked your team to create a plan that reduces CO2 emissions by at least 50% without causing blackouts.",
    "stem_questions": [
        "How many hours of sunlight does your region get per day on average?",
        "What happens to solar output on cloudy days and at night?",
        "How can you store solar energy for when the sun isn't shining?"
    ],
    "stem_design_qs": [
        "What percentage of energy will come from solar vs. fossil fuels?",
        "How will you handle energy needs at night or during storms?",
        "Where will you place solar panels for maximum sunlight?",
        "How will you measure whether your plan actually reduces emissions?"
    ],
    "career": "Renewable Energy Engineers design and install solar, wind, and other clean energy systems. They help communities transition away from fossil fuels. They earn $75,000-$130,000/year.",
    "images": {
        "cover": ("cover-energy-showdown.png", "A photorealistic, cinematic split image showing a gleaming solar panel farm on one side and a coal power plant with smokestacks on the other, dramatic sky, ultra-crisp detail, strong contrast between clean and polluted"),
        "landscape": ("landscape-energy-showdown.png", "A photorealistic image of a Black male student (age 10-11) leading a group of diverse 5th graders including White, Asian, and Latina classmates examining a solar panel on the school roof, wearing hoodies and jeans, bright sunlight, confident expressions"),
        "modeling": ("modeling-energy-showdown.png", "A photorealistic image of a White female student (age 10-11) at a laptop building an energy model, with Black male, Asian female, and Latino male classmates pointing at the screen, modern classroom with recycling posters, natural light"),
        "discussion": ("discussion-energy-showdown.png", "A photorealistic image of a Latino male teacher leading a class debate about energy sources with animated 5th graders including White, Asian, Black, and Latina students, some holding pro-solar and pro-fossil signs, classroom setting"),
        "stem": ("stem-energy-showdown.png", "A photorealistic image of an Asian female student (age 10-11) presenting a clean energy plan poster while Black, White, and Latino classmates evaluate it, school multipurpose room, professional science fair atmosphere")
    },
    "pre_assessment": [
        "Where does electricity come from when you flip a light switch?",
        "What do you think happens when coal is burned at a power plant?",
        "Have you seen solar panels in your neighborhood? What do they do?",
        "Why do some people want to use solar energy instead of burning coal or gas?"
    ],
    "extend_components": [
        ("Wind Energy", "Electricity generated from wind turbines as another clean source"),
        ("Energy Storage", "Batteries that save solar energy for nighttime use"),
        ("Electricity Demand", "How much energy the community needs at any given time")
    ],
    "reflections": [
        "Why can't we just switch to 100% solar energy overnight?",
        "What would happen to air quality in cities if all cars and power plants switched to solar?",
        "How is your town's energy mix similar to or different from the model you built?",
        "What surprised you most about the relationship between fossil fuels and air quality?",
        "If you were the mayor, what would your energy plan look like?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model comparing solar and fossil fuel energy systems and their environmental impacts."),
        ("Disciplinary Core Idea", "ESS3.C Human Impacts on Earth Systems", "Students model how energy choices affect atmospheric CO2 and air quality."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify causal relationships between energy source choices and environmental outcomes.")
    ],
    "cast_items": [
        "Compare the environmental impacts of solar and fossil fuel energy",
        "Explain how CO2 emissions from fossil fuels affect air quality",
        "Evaluate tradeoffs between reliability and environmental impact of energy sources"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A city switches from coal power plants to solar panels. Which of the following will most likely decrease?"),
        ("Constructed Response:", "Explain why a town cannot rely on solar energy alone and describe one solution to this problem.")
    ],
    "background_intro": "Humans need energy to power homes, schools, and transportation. The two main sources — fossil fuels and solar energy — have very different impacts on the environment.",
    "background_sections": [
        ("How Fossil Fuels Work", "Coal, oil, and natural gas are burned to heat water into steam, which spins turbines to generate electricity. This process releases CO2 and other pollutants into the atmosphere."),
        ("How Solar Panels Work", "Solar panels contain cells that convert sunlight directly into electricity. No burning is involved, so no CO2 is released during operation."),
        ("The Air Quality Connection", "CO2 and particulate matter from burning fossil fuels reduce air quality. Poor air quality causes respiratory problems, especially for children and elderly populations."),
        ("The Reliability Tradeoff", "Fossil fuels can generate power 24/7, rain or shine. Solar panels only produce energy during daylight hours and are affected by clouds, seasons, and latitude.")
    ],
    "lever_L": "Students identify Sunlight Hours, Fossil Fuel Burn Rate, Solar Energy Output, CO2 Emissions, and Air Quality Index as the five system components.",
    "lever_E": "Students determine that Sunlight drives Solar Output (+), Fossil Fuels drive CO2 Emissions (+), CO2 reduces Air Quality (-), and Solar Output reduces the need for fossil fuels, thereby reducing emissions (-).",
    "lever_V": "Students build the energy comparison model showing how two energy sources produce different environmental outcomes.",
    "lever_Ev": "Students run All Solar and Cloudy Day scenarios to discover the strengths and weaknesses of each energy source.",
    "lever_R": "Students add Energy Storage (batteries) or Wind Energy to explore how the system can be improved.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Split image: solar farm vs coal plant", "say": "Two ways to make electricity. One is clean. One is not. Which should we choose?", "do": "Show split image and ask students to identify what they see on each side.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we model the energy showdown between solar and fossil fuels.", "do": "Students read objectives and predict which energy source is better.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Can solar replace fossil fuels?", "say": "This is not a simple yes or no. Our model will reveal the tradeoffs.", "do": "Quick poll: Who thinks solar can replace fossil fuels completely?", "time": "2 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We will build a model that compares both energy sources side by side.", "do": "Preview how the model will have two inputs and three outputs.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Five component cards", "say": "Our model has two external inputs: Sunlight Hours and Fossil Fuel Burn Rate. The three internal components respond to these inputs.", "do": "Students sort components and discuss which are controllable.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows with +/- signs", "say": "Notice that solar energy has an INDIRECT negative effect on emissions — by replacing fossil fuels.", "do": "Guide students through drawing all relationship arrows.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graphs comparing scenarios", "say": "Let's test what happens when we go all solar — and then when clouds roll in.", "do": "Students run All Solar and Cloudy Day scenarios and compare results.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings about energy tradeoffs", "say": "Solar is cleaner, but fossil fuels are more reliable. That's the tradeoff.", "do": "Class discussion: What's the best mix?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Clean energy plan for your town", "say": "Now design an energy plan that cuts emissions by 50% without blackouts.", "do": "Groups create plans; circulate to challenge assumptions.", "time": "10 min"}
    ],
    "sort_reasoning": "Sunlight Hours and Fossil Fuel Burn Rate are external because they represent controllable inputs — how much sunlight is available and how much fossil fuel is burned. Solar Energy Output, CO2 Emissions, and Air Quality Index are internal because they change in response to the external inputs.",
    "relationships": [
        ("Sunlight Hours to Solar Energy Output", "POSITIVE (+)", "More hours of sunlight means more electricity generated from solar panels."),
        ("Fossil Fuel Burn Rate to CO2 Emissions", "POSITIVE (+)", "Burning more fossil fuel releases more CO2 into the atmosphere."),
        ("CO2 Emissions to Air Quality Index", "NEGATIVE (-)", "More CO2 and pollutants in the air means worse air quality."),
        ("Solar Energy Output to CO2 Emissions", "NEGATIVE (-)", "When solar provides more energy, less fossil fuel is needed, reducing emissions.")
    ],
    "sim_answers": [
        ("All Solar Scenario", "When Fossil Fuel Burn Rate drops to 0% and Sunlight is at 80%, CO2 Emissions drop to near zero and Air Quality improves dramatically. Solar Energy Output is high and stable."),
        ("Cloudy Day Crisis", "When Sunlight drops to 10% and Fossil Fuel is at 0%, Solar Energy Output crashes. There is very little energy being produced. This reveals the reliability weakness of solar-only systems — we need storage or backup.")
    ],
    "reflection_exemplars": [
        ("Why can't we switch to 100% solar overnight?", "Solar only works during daylight and depends on weather. Without massive battery storage, nights and cloudy days would cause blackouts. The transition requires time to build storage infrastructure and backup systems."),
        ("What would happen to city air quality?", "If all power plants and vehicles switched to solar/electric, CO2 emissions would drop dramatically. Cities would have much cleaner air, reducing asthma and respiratory illness, especially in communities near current power plants.")
    ],
    "stem_intro": "Present the challenge by discussing local air quality. Ask: Has anyone noticed smog or pollution? Connect to the model: every power plant choice affects the air we breathe.",
    "stem_concepts": [
        ("Solar Capacity", "Solar panels produce about 4-6 hours of peak energy per day in most US locations."),
        ("Battery Storage", "Batteries can store solar energy for nighttime, but they are expensive and have limited capacity."),
        ("Energy Mix", "Most clean energy plans use a combination of solar, wind, and reduced fossil fuels rather than one source alone.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan includes specific solar/fossil percentages, addresses nighttime needs, and connects reasoning to model data"),
        ("Proficient (3)", "Plan addresses energy mix and one limitation with scientific reasoning"),
        ("Developing (2)", "Plan mentions solar and fossil but lacks specific percentages or reasoning"),
        ("Beginning (1)", "Plan does not address tradeoffs or connect to model findings")
    ],
    "support": [
        "Provide a T-chart comparing solar and fossil fuel advantages/disadvantages",
        "Use sentence frames: 'When fossil fuel burn rate increases, CO2 emissions __ because...'",
        "Show real-time air quality maps so students can see local conditions"
    ],
    "extensions": [
        "Research how much of your state's energy comes from solar vs fossil fuels",
        "Add wind energy as a third component and explore the expanded model",
        "Calculate how many solar panels your school would need to go off-grid"
    ],
    "cross_curr": [
        ("Math", "Calculate CO2 emissions saved by replacing 50% of fossil fuel use with solar"),
        ("ELA", "Write a persuasive letter to the mayor recommending an energy plan"),
        ("Social Studies", "Research which countries lead the world in solar energy adoption and why")
    ],
    "misconceptions": [
        ("Solar panels work at night", "Solar panels require sunlight to generate electricity. At night, stored energy from batteries or other sources must be used.", "Ask: What powers your house at 2 AM if you only have solar panels?"),
        ("Fossil fuels are not related to air quality", "Burning fossil fuels releases CO2, sulfur dioxide, and particulate matter directly into the air, reducing air quality.", "Show before/after photos of cities that reduced fossil fuel use."),
        ("One energy source is always better", "Both solar and fossil fuels have advantages and disadvantages. The best solution depends on location, climate, technology, and community needs.", "Challenge students: Name one advantage of fossil fuels that solar does not have.")
    ]
}

L03 = {
    "id": "G05L2-L03",
    "title": "The Water Crisis: Who Gets the Water?",
    "subtitle": "When Rain Runs Out and People Keep Moving In",
    "ngss": "5-ESS2-2, 5-ESS3-1",
    "ngss_desc": "Describe and graph the amounts and percentages of water and fresh water in various reservoirs to provide evidence about the distribution of water on Earth. Obtain and combine information about ways individual communities use science ideas to protect the Earth's resources and environment.",
    "big_question": "What happens when a growing community runs out of water?",
    "objectives": [
        "Model how rainfall and population size affect groundwater and water availability",
        "Explain the relationship between water usage rate and groundwater depletion",
        "Predict what happens during a drought when population continues to grow",
        "Evaluate solutions for managing limited water resources"
    ],
    "vocabulary": [
        ("Groundwater", "Water stored underground in soil and rock layers called aquifers"),
        ("Aquifer", "An underground layer of rock or sediment that holds water"),
        ("Water Usage Rate", "How fast a community uses its available water supply"),
        ("Water Availability", "Whether there is enough clean water for everyone in a community")
    ],
    "components": [
        ("Rainfall Amount", "How much precipitation falls in the region", True),
        ("Population Size", "The number of people living in the community", True),
        ("Groundwater Level", "The amount of water stored underground in aquifers", False),
        ("Water Usage Rate", "How fast the community consumes available water", False),
        ("Water Availability", "Whether there is enough water to meet everyone's needs", False)
    ],
    "think_about_it": "If a town's population doubles but rainfall stays the same, what happens to the amount of water available for each person?",
    "scenarios": [
        ("Normal Conditions", "Set Rainfall and Population to moderate levels"),
        ("Drought + Growth", "Lock Rainfall to 20% and set Population to 80%"),
        ("Conservation Success", "Moderate Rainfall, high Population, but reduced Usage Rate")
    ],
    "sim_scenarios": [
        ("Normal Conditions", "Moderate rainfall and population", "What do you predict will happen to Groundwater Level?"),
        ("Drought + Growth", "Rainfall at 20%, Population at 80%", "What do you predict will happen to Water Availability?"),
        ("Recovery", "Restore rainfall to 60% while keeping population high", "How quickly does the system recover?")
    ],
    "discoveries": [
        "Groundwater refills slowly from rainfall but depletes quickly with high usage",
        "A growing population increases water demand even when rainfall stays the same",
        "Droughts are most dangerous in areas with large, growing populations",
        "Water availability depends on the BALANCE between rainfall input and usage output"
    ],
    "answer": "When a growing community faces drought, groundwater is depleted faster than rain can refill it. Water availability drops, creating a crisis. The solution requires either increasing supply (more rain, desalination) or decreasing demand (conservation).",
    "stem_title": "Design a Water Conservation Plan",
    "stem_mission": "Design a plan that keeps a growing town from running out of water during a drought.",
    "stem_scenario": "The town of Dry Creek has doubled in population over 10 years, but rainfall has decreased by 30%. The mayor has asked your team to create a water conservation plan.",
    "stem_questions": [
        "How much water does one person use per day on average?",
        "What are the biggest uses of water in a town (homes, farms, industry)?",
        "How can you reduce usage without hurting people's daily lives?"
    ],
    "stem_design_qs": [
        "What water conservation rules will you put in place?",
        "How will you capture and store rainwater when it does rain?",
        "Can you recycle greywater (used sink/shower water) for irrigation?",
        "How will you measure whether your plan is working?"
    ],
    "career": "Hydrologists and Water Resource Engineers study how water moves through the environment and design systems to ensure communities have enough clean water. They earn $70,000-$110,000/year.",
    "images": {
        "cover": ("cover-water-crisis.png", "A photorealistic, cinematic split image showing a lush green reservoir on one side and a dry, cracked lakebed on the other, dramatic sky with gathering clouds, ultra-crisp detail"),
        "landscape": ("landscape-water-crisis.png", "A photorealistic image of a Latino female student (age 10-11) leading diverse 5th graders including White, Asian, and Black classmates collecting water samples from a school rain garden, wearing jeans and sneakers, overcast sky, focused expressions"),
        "modeling": ("modeling-water-crisis.png", "A photorealistic image of an Asian male student (age 10-11) at a laptop building a water systems model, with White female, Black male, and Latina classmates pointing at graphs on screen, modern classroom, natural light"),
        "discussion": ("discussion-water-crisis.png", "A photorealistic image of a White female teacher at a whiteboard drawing a water cycle diagram while diverse 5th graders including Black, Asian, Latino, and White students ask questions, warm classroom light"),
        "stem": ("stem-water-crisis.png", "A photorealistic image of a Black female student (age 10-11) presenting a water conservation poster while White, Asian, and Latino classmates examine water filtration models, school science fair setting")
    },
    "pre_assessment": [
        "Where does the water in your faucet come from before it reaches your house?",
        "What do you think happens underground when it rains?",
        "If a town grows from 1,000 people to 10,000 people, what happens to water supply?",
        "What does the word 'drought' mean, and have you ever experienced one?"
    ],
    "extend_components": [
        ("Desalination", "Converting ocean water to fresh water using technology"),
        ("Agricultural Irrigation", "Water used to grow crops, often the largest water consumer"),
        ("Water Recycling", "Treating and reusing wastewater for non-drinking purposes")
    ],
    "reflections": [
        "Why are some communities more vulnerable to water crises than others?",
        "What surprised you about how quickly groundwater can be depleted?",
        "How does the water crisis model connect to what you know about the water cycle?",
        "If you could add one component to this model to make it more realistic, what would it be?",
        "What responsibility do individuals have to conserve water?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model showing how rainfall, population, and usage interact to determine water availability."),
        ("Disciplinary Core Idea", "ESS2.C The Roles of Water in Earth's Surface Processes", "Students model how water is distributed and how human activity affects its availability."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify how population growth and reduced rainfall cause water crises.")
    ],
    "cast_items": [
        "Explain how groundwater levels are affected by both rainfall and population",
        "Predict the outcome of a drought in a growing community",
        "Propose a solution that balances water supply and demand"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A town's population triples while rainfall stays the same. What is the most likely result?"),
        ("Constructed Response:", "Explain how a drought and population growth together create a water crisis, using evidence from your model.")
    ],
    "background_intro": "Fresh water makes up less than 3% of all water on Earth, and most of it is frozen in glaciers and ice caps. The tiny fraction that is accessible as groundwater and surface water must support all human communities, agriculture, and ecosystems.",
    "background_sections": [
        ("Groundwater and Aquifers", "Groundwater is water that has seeped through soil and rock into underground layers called aquifers. These aquifers are recharged by rainfall, but the refilling process takes years or decades."),
        ("Growing Demand", "As populations grow, water demand increases for drinking, cooking, bathing, farming, and industry. Many aquifers are being pumped faster than rainfall can refill them."),
        ("Drought Amplifies the Problem", "During drought, rainfall drops while demand stays the same or increases. This double pressure — less input, same output — can rapidly deplete groundwater reserves."),
        ("Real-World Water Crises", "Cities like Cape Town, South Africa nearly ran out of water in 2018. Flint, Michigan had contaminated water. California regularly faces drought restrictions. Water crises are a global issue affecting billions.")
    ],
    "lever_L": "Students identify Rainfall Amount, Population Size, Groundwater Level, Water Usage Rate, and Water Availability as the five system components.",
    "lever_E": "Students determine that Rainfall refills Groundwater (+), Population increases Usage (+), Usage depletes Groundwater (-), Groundwater supports Availability (+), and Population strains Availability (-).",
    "lever_V": "Students build the water crisis model showing competing inputs and outputs that determine whether a community has enough water.",
    "lever_Ev": "Students run the Drought + Growth scenario and observe groundwater crashing and water availability dropping to crisis levels.",
    "lever_R": "Students add Desalination, Water Recycling, or Agricultural Irrigation to explore how technology and behavior can change outcomes.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Split image: full reservoir vs dry cracked lakebed", "say": "What happens when the water runs out? Today we model a water crisis.", "do": "Show before/after photos of a real reservoir during drought.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we explore how rainfall, population, and water usage interact.", "do": "Students read objectives and share what they know about droughts.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "What happens when a growing community runs out of water?", "say": "This is happening right now in communities around the world.", "do": "Quick discussion: Has anyone experienced water restrictions?", "time": "2 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "Our model will have two inputs competing against each other.", "do": "Preview how rainfall adds water while population removes it.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Five component cards", "say": "Rainfall adds water to the system. Population takes it away. What happens in between?", "do": "Students sort components and predict which are external vs internal.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows with +/- signs", "say": "Notice that Population has BOTH a positive and negative effect — it increases usage but decreases availability.", "do": "Guide students through all five relationships.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graphs showing drought + growth scenario", "say": "What happens when rain drops and population rises? Let's watch the crisis unfold.", "do": "Students run Drought + Growth scenario and record observations.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings about water systems", "say": "Water availability is a balance — when inputs fall below outputs, crisis follows.", "do": "Class discussion: What solutions exist?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Water conservation plan design", "say": "Design a plan to keep Dry Creek from running out of water.", "do": "Groups create plans, present to class for feedback.", "time": "10 min"}
    ],
    "sort_reasoning": "Rainfall Amount and Population Size are external because they represent environmental and demographic conditions that students can adjust. Groundwater Level, Water Usage Rate, and Water Availability are internal because they respond to and are determined by the balance between rainfall input and population demand.",
    "relationships": [
        ("Rainfall Amount to Groundwater Level", "POSITIVE (+)", "More rainfall seeps into the ground and refills underground aquifers."),
        ("Population Size to Water Usage Rate", "POSITIVE (+)", "More people means more water is used for drinking, bathing, and farming."),
        ("Water Usage Rate to Groundwater Level", "NEGATIVE (-)", "Pumping water out of the ground faster depletes aquifer levels."),
        ("Groundwater Level to Water Availability", "POSITIVE (+)", "Higher groundwater levels mean more water is available for the community."),
        ("Population Size to Water Availability", "NEGATIVE (-)", "More people competing for the same water supply reduces availability per person.")
    ],
    "sim_answers": [
        ("Drought + Growth Scenario", "When Rainfall drops to 20% and Population is at 80%, Groundwater Level falls rapidly because usage far exceeds refill. Water Usage Rate stays high due to large population. Water Availability crashes as aquifers are depleted."),
        ("Recovery Scenario", "When rainfall returns to 60%, groundwater begins to refill, but recovery is slow because the large population continues to draw water at a high rate. Full recovery takes much longer than the depletion did.")
    ],
    "reflection_exemplars": [
        ("Why are some communities more vulnerable?", "Communities in dry climates with large or rapidly growing populations are most vulnerable because they start with less rainfall input. If they also rely on a single aquifer, they have no backup when that aquifer depletes."),
        ("What responsibility do individuals have?", "Every person's daily water use contributes to the total demand. Shorter showers, fixing leaks, and drought-resistant landscaping reduce individual demand, which collectively helps the whole community.")
    ],
    "stem_intro": "Present the Dry Creek scenario by showing real drought photos. Connect to the model: the town is using water faster than rain can replace it.",
    "stem_concepts": [
        ("Per Capita Water Use", "The average American uses about 80-100 gallons of water per day for drinking, bathing, cooking, and landscaping."),
        ("Rainwater Harvesting", "Collecting and storing rainwater from rooftops can supplement groundwater supply during dry periods."),
        ("Greywater Recycling", "Used water from sinks and showers can be treated and reused for irrigation, reducing demand on fresh water supplies.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan includes specific conservation measures, quantifies water savings, and connects reasoning to model data"),
        ("Proficient (3)", "Plan includes 2-3 conservation measures with scientific reasoning"),
        ("Developing (2)", "Plan mentions conservation but lacks specific measures or quantities"),
        ("Beginning (1)", "Plan does not address the relationship between supply and demand")
    ],
    "support": [
        "Provide a labeled diagram showing how rainfall becomes groundwater",
        "Use sentence frames: 'When population increases, water availability __ because...'",
        "Show a simple bar graph comparing daily water use for different activities"
    ],
    "extensions": [
        "Research your town's water source and find out if it is sustainable",
        "Add agricultural irrigation as a component and explore its effect on groundwater",
        "Compare water crises in different parts of the world using data"
    ],
    "cross_curr": [
        ("Math", "Calculate how many gallons of water your school uses per day and how much could be saved"),
        ("ELA", "Write a news article reporting on the Dry Creek water crisis and proposed solutions"),
        ("Social Studies", "Research the history of water rights in the western United States")
    ],
    "misconceptions": [
        ("There is plenty of water because Earth is 70% water", "97% of Earth's water is saltwater. Only 3% is fresh, and most of that is frozen. Less than 1% is accessible groundwater and surface water.", "Ask: If you had 100 cups of water representing all of Earth's water, how many would you be able to drink?"),
        ("Rain always refills groundwater", "Rain refills aquifers, but the process takes years. If water is pumped out faster than rain can replace it, the aquifer depletes — just like withdrawing money faster than deposits.", "Show an animation of aquifer depletion over time."),
        ("Water crises only happen in deserts", "Water crises can happen anywhere that demand exceeds supply. Even rainy regions can experience water shortages if population growth outpaces infrastructure.", "Discuss the Flint, Michigan water crisis as an example.")
    ]
}

L04 = {
    "id": "G05L2-L04",
    "title": "Phase Changes: When Matter Transforms",
    "subtitle": "Same Stuff, Different State — and Nothing Is Lost",
    "ngss": "5-PS1-2, 5-PS1-4",
    "ngss_desc": "Measure and graph quantities to provide evidence that regardless of the type of change that occurs when heating, cooling, or mixing substances, the total weight of matter is conserved. Conduct an investigation to determine whether the mixing of two or more substances results in new substances.",
    "big_question": "When ice melts and water boils, does any matter disappear?",
    "objectives": [
        "Model how temperature and pressure affect the state of matter",
        "Demonstrate that total mass is conserved during phase changes",
        "Explain why matter changes states when energy is added or removed",
        "Predict what happens to solid, liquid, and gas amounts when conditions change"
    ],
    "vocabulary": [
        ("Phase Change", "A physical change where matter switches between solid, liquid, and gas"),
        ("Conservation of Matter", "The principle that matter is neither created nor destroyed"),
        ("Melting Point", "The temperature at which a solid becomes a liquid"),
        ("Evaporation", "The process of a liquid turning into a gas")
    ],
    "components": [
        ("Temperature", "The amount of heat energy applied to the substance", True),
        ("Pressure", "The atmospheric pressure pushing on the substance", True),
        ("Solid Amount", "The mass of the substance in solid form", False),
        ("Liquid Amount", "The mass of the substance in liquid form", False),
        ("Gas Amount", "The mass of the substance in gas form", False)
    ],
    "think_about_it": "When you heat an ice cube and it melts into water, does the water weigh more, less, or the same as the ice?",
    "scenarios": [
        ("Heating from Frozen", "Start with Temperature at 0% (frozen solid) and slowly increase"),
        ("Boiling Point", "Set Temperature to 90% and observe what happens to Liquid Amount"),
        ("Pressure Squeeze", "Set Pressure to 90% and observe the effect on Gas Amount")
    ],
    "sim_scenarios": [
        ("Heating from Frozen", "Temperature starts at 0%, increase gradually", "What do you predict will happen to Solid Amount and Liquid Amount?"),
        ("Boiling Point", "Temperature set to 90%", "What do you predict will happen to the amount of gas?"),
        ("Pressure Squeeze", "Pressure increased to 90%", "What do you predict will happen to Gas Amount?")
    ],
    "discoveries": [
        "When temperature rises, solids melt into liquids and liquids evaporate into gases",
        "The TOTAL amount of matter stays the same — it just changes form",
        "High pressure can push gas molecules back into liquid form",
        "Solid + Liquid + Gas always equals the same total — matter is CONSERVED"
    ],
    "answer": "When ice melts and water boils, NO matter disappears. The same atoms just spread out (as gas) or pack together (as solid). The total mass never changes. Matter is conserved during every phase change.",
    "stem_title": "Design a Phase Change Challenge",
    "stem_mission": "Design an experiment that proves matter is conserved during a phase change.",
    "stem_scenario": "A younger student says 'water disappears when it boils.' Your team needs to design an experiment that PROVES the water didn't disappear — it just changed form.",
    "stem_questions": [
        "How can you measure the mass of water before and after boiling?",
        "Where does the water go when it seems to disappear?",
        "How could you capture the steam and prove it is still water?"
    ],
    "stem_design_qs": [
        "What materials will you need for your experiment?",
        "How will you measure mass before and after the phase change?",
        "How will you capture the gas to prove it is still the same substance?",
        "What data will you collect to prove conservation of matter?"
    ],
    "career": "Materials Scientists study how substances behave under different temperatures and pressures. They design new materials for everything from phone screens to spacecraft heat shields. They earn $80,000-$130,000/year.",
    "images": {
        "cover": ("cover-phase-changes.png", "A photorealistic, cinematic image showing three states of water side by side — a glistening ice cube, a splash of liquid water, and swirling steam — all against a dark background, ultra-crisp detail, dramatic lighting"),
        "landscape": ("landscape-phase-changes.png", "A photorealistic image of a White male student (age 10-11) leading a group of diverse 5th graders including Black, Asian, and Latina classmates observing a beaker of water beginning to boil on a hot plate, science lab setting, safety goggles on, focused expressions"),
        "modeling": ("modeling-phase-changes.png", "A photorealistic image of a Black female student (age 10-11) at a laptop building a phase change model, with White male, Asian female, and Latino male classmates watching the simulation graphs, modern classroom, natural light"),
        "discussion": ("discussion-phase-changes.png", "A photorealistic image of an Asian male teacher drawing a diagram of solid, liquid, and gas molecules on a whiteboard while diverse 5th graders including White, Black, Latino, and Asian students follow along, classroom with science equipment"),
        "stem": ("stem-phase-changes.png", "A photorealistic image of a Latino male student (age 10-11) carefully weighing a beaker on a digital scale while Black, White, and Asian classmates record data on clipboards, school science lab, bright overhead lighting")
    },
    "pre_assessment": [
        "What happens to ice when you leave it on a counter? Where does it go?",
        "When you boil water and see steam, did the water disappear? Explain your thinking.",
        "Draw what you think molecules look like in ice, liquid water, and steam.",
        "If you weigh a glass of water, then freeze it, will it weigh the same?"
    ],
    "extend_components": [
        ("Melting Point Threshold", "The specific temperature where solid becomes liquid"),
        ("Boiling Point Threshold", "The specific temperature where liquid becomes gas"),
        ("Particle Speed", "How fast molecules move, which increases with temperature")
    ],
    "reflections": [
        "Why does conservation of matter matter for science?",
        "If you could see individual water molecules, what would you see happening during melting?",
        "Why does high pressure turn gas back into liquid?",
        "How is this model similar to what happens in the real water cycle?",
        "What evidence would convince a skeptic that matter is not destroyed during boiling?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model showing how temperature and pressure affect the distribution of matter across three states."),
        ("Disciplinary Core Idea", "PS1.A Structure and Properties of Matter", "Students model how matter changes state while total mass is conserved."),
        ("Crosscutting Concept", "Scale, Proportion, and Quantity", "Students observe that the total quantity of matter remains constant across phase changes.")
    ],
    "cast_items": [
        "Explain how temperature causes phase changes",
        "Demonstrate that total mass is conserved during a phase change",
        "Predict the effect of pressure on gas molecules"
    ],
    "cast_questions": [
        ("Multiple Choice:", "You weigh a sealed container of water, then boil it. The container now holds steam. How does the weight compare to before boiling?"),
        ("Constructed Response:", "Explain what happens to water molecules as ice is heated to steam, and how you know that no matter is lost during this process.")
    ],
    "background_intro": "Matter exists in three common states — solid, liquid, and gas. Phase changes occur when energy is added or removed, but the total amount of matter always stays the same. This is the law of conservation of matter.",
    "background_sections": [
        ("Molecular Motion", "In solids, molecules vibrate in fixed positions. In liquids, they slide past each other. In gases, they fly freely in all directions. Adding heat energy makes molecules move faster, causing phase changes."),
        ("Conservation of Mass", "Antoine Lavoisier proved in the 1770s that matter is conserved in all changes. When water boils, it seems to disappear, but the same mass of water now exists as invisible steam."),
        ("Pressure Effects", "Pressure affects phase changes. High pressure pushes gas molecules closer together, turning them back into liquids. This is how refrigerators and air conditioners work."),
        ("Phase Change Diagrams", "Scientists use phase diagrams to show the temperatures and pressures where each state exists. Water's unique properties — like expanding when it freezes — make it essential for life.")
    ],
    "lever_L": "Students identify Temperature, Pressure, Solid Amount, Liquid Amount, and Gas Amount as the five system components.",
    "lever_E": "Students determine that Temperature reduces Solid Amount (-) and increases Gas Amount (+), while Pressure reduces Gas Amount (-) by compressing gas back to liquid.",
    "lever_V": "Students build the phase change model showing how matter transfers between three states while total mass remains constant.",
    "lever_Ev": "Students run the Heating from Frozen scenario and observe Solid decreasing as Liquid and Gas increase, confirming conservation of matter.",
    "lever_R": "Students add Melting Point Threshold or Particle Speed to explore more precise phase change behavior.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Ice, liquid water, and steam side by side", "say": "Same stuff. Three forms. Does anything disappear when it changes?", "do": "Hold up an ice cube and ask: Where will this water be in an hour?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we prove that matter is NEVER lost — it just changes form.", "do": "Students read objectives and predict: Does boiled water weigh less?", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "When ice melts and water boils, does any matter disappear?", "say": "Most people think water disappears when it boils. Let's test that.", "do": "Quick vote: Does water weigh less after boiling? Tally predictions.", "time": "2 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "Our model tracks matter in three states at once.", "do": "Preview how the three internal components always add up to the same total.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Five component cards", "say": "Temperature and Pressure are external — we control them. The three states respond.", "do": "Students sort components and discuss which ones they can control in real life.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows with +/- signs", "say": "Watch for the key pattern: what one state loses, another gains.", "do": "Guide students through the relationships, emphasizing conservation.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graphs showing phase transitions", "say": "Slowly increase temperature and watch what happens to each state.", "do": "Students run Heating from Frozen scenario and track all three amounts.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings: conservation of matter", "say": "The total never changed. Matter does not disappear — it transforms.", "do": "Have students add all three amounts at each time step to verify total is constant.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Phase change experiment design", "say": "Now prove it with a real experiment. Design a test that shows boiled water does not disappear.", "do": "Groups design experiments; discuss how to capture steam.", "time": "10 min"}
    ],
    "sort_reasoning": "Temperature and Pressure are external because they represent environmental conditions that students can adjust. Solid Amount, Liquid Amount, and Gas Amount are internal because they change in response to temperature and pressure conditions, and they must always add up to the same total mass.",
    "relationships": [
        ("Temperature to Solid Amount", "NEGATIVE (-)", "Increasing temperature causes solids to melt, reducing the amount of solid."),
        ("Temperature to Gas Amount", "POSITIVE (+)", "Increasing temperature causes liquids to evaporate, increasing the amount of gas."),
        ("Pressure to Gas Amount", "NEGATIVE (-)", "Increasing pressure compresses gas molecules back toward liquid form."),
        ("Temperature to Liquid Amount", "POSITIVE/NEGATIVE (+/-)", "Moderate heat melts ice into liquid (+), but high heat evaporates liquid into gas (-). Liquid amount first rises, then falls.")
    ],
    "sim_answers": [
        ("Heating from Frozen", "As temperature increases from 0%, Solid Amount decreases while Liquid Amount increases (melting). At higher temperatures, Liquid Amount starts to decrease as Gas Amount increases (evaporation). At all points, Solid + Liquid + Gas = same total."),
        ("Pressure Squeeze", "When Pressure is set to 90%, Gas Amount decreases as molecules are compressed closer together. This pushes gas back toward liquid form. Total mass remains unchanged.")
    ],
    "reflection_exemplars": [
        ("Why does conservation of matter matter for science?", "If matter could disappear, we could not predict how systems behave. Conservation of matter means we can always track where matter goes — it just changes form. This is a foundational principle of all chemistry and biology."),
        ("What evidence would convince a skeptic?", "Weigh a sealed container of water, boil it, and weigh again. The mass will be identical. The water is now steam inside the container, but no matter was lost. You can also cool the container to condense the steam back to water.")
    ],
    "stem_intro": "Present the challenge by asking: 'A second grader says water disappears when you boil it. How would you prove them wrong?' Connect to the model: our model shows matter is conserved.",
    "stem_concepts": [
        ("Closed Systems", "In a sealed container, all matter stays inside regardless of phase changes. Mass before = mass after."),
        ("Measuring Conservation", "Use a digital scale to measure mass before and after a phase change to prove nothing is lost."),
        ("Capturing Gas", "Steam can be captured using a sealed flask or condensed back to liquid with a cold surface.")
    ],
    "stem_eval": [
        ("Expert (4)", "Experiment clearly tests conservation with measurements before and after; captures gas phase; connects to model"),
        ("Proficient (3)", "Experiment measures mass but may not fully capture gas phase; sound reasoning"),
        ("Developing (2)", "Experiment idea present but lacks measurement plan or gas capture method"),
        ("Beginning (1)", "Experiment does not test conservation of matter or lacks scientific reasoning")
    ],
    "support": [
        "Provide a visual showing molecule arrangement in solid, liquid, and gas",
        "Use sentence frames: 'When temperature increases, the solid amount __ because...'",
        "Demonstrate with ice cubes in a sealed bag — weigh before and after melting"
    ],
    "extensions": [
        "Research sublimation (solid directly to gas) and add it to the model",
        "Investigate why water is unusual — it expands when it freezes",
        "Explore how pressure cookers use high pressure to change boiling point"
    ],
    "cross_curr": [
        ("Math", "Graph the mass of solid, liquid, and gas over time as temperature increases, verifying the total stays constant"),
        ("ELA", "Write a persuasive essay arguing that steam is still water, using evidence from the model"),
        ("Social Studies", "Research how understanding phase changes led to inventions like the steam engine and refrigeration")
    ],
    "misconceptions": [
        ("Water disappears when it boils", "Water does not disappear — it becomes water vapor (steam), an invisible gas. The same mass of water still exists, just in a different state.", "Boil water in a sealed container and weigh it before and after. The mass is identical."),
        ("Ice weighs less than water", "The same mass of water weighs the same whether it is ice, liquid, or steam. Ice floats because it is less DENSE (takes up more space), not because it weighs less.", "Weigh ice in a sealed bag, let it melt, and weigh again — same mass."),
        ("Gas has no mass", "Gas absolutely has mass. A balloon inflated with air weighs more than an empty balloon. Gas molecules are just spread far apart.", "Weigh an empty balloon, inflate it, and weigh again to show gas has mass.")
    ]
}

L05 = {
    "id": "G05L2-L05",
    "title": "The Food Web Puzzle",
    "subtitle": "Remove One Piece and Watch Everything Change",
    "ngss": "5-LS2-1",
    "ngss_desc": "Develop a model to describe the movement of matter among plants, animals, decomposers, and the environment.",
    "big_question": "What happens to an entire ecosystem when one species disappears?",
    "objectives": [
        "Model the relationships between producers, consumers, and decomposers in a food web",
        "Explain how energy and matter flow through trophic levels",
        "Predict the cascading effects of removing a species from the food web",
        "Demonstrate how decomposers complete the nutrient cycle"
    ],
    "vocabulary": [
        ("Producer", "An organism that makes its own food from sunlight, like plants and algae"),
        ("Primary Consumer", "An herbivore that eats producers directly"),
        ("Secondary Consumer", "A predator that eats primary consumers"),
        ("Trophic Cascade", "A chain reaction through a food web when one species is removed or changed")
    ],
    "components": [
        ("Producer Population", "The number of plants and algae in the ecosystem", True),
        ("Primary Consumer Population", "The number of herbivores eating the producers", False),
        ("Secondary Consumer Population", "The number of predators eating the herbivores", False),
        ("Decomposer Activity", "The rate at which dead organisms are broken down", False),
        ("Available Nutrients", "Minerals and nutrients in the soil for producers to use", False)
    ],
    "think_about_it": "If all the wolves disappeared from Yellowstone, what would happen to the deer? And then what would happen to the plants?",
    "scenarios": [
        ("Balanced Ecosystem", "Set Producer Population to a moderate level and observe all trophic levels"),
        ("Remove Predators", "Set Secondary Consumer Population to 0% and watch the cascade"),
        ("Remove Producers", "Lock Producer Population to 0% and observe the total collapse")
    ],
    "sim_scenarios": [
        ("Balanced Ecosystem", "Normal producer population", "What do you predict will happen to all five components?"),
        ("Remove Predators", "Secondary Consumers set to 0%", "What do you predict will happen to Primary Consumers and then Producers?"),
        ("Remove Producers", "Producers locked at 0%", "What do you predict will happen to the entire food web?")
    ],
    "discoveries": [
        "Every species in a food web is connected — removing one causes a cascade of changes",
        "Without predators, herbivores overpopulate and can destroy producers through overgrazing",
        "Without producers, the entire food web collapses because there is no energy entering the system",
        "Decomposers close the loop by recycling dead matter back into nutrients for producers"
    ],
    "answer": "When one species disappears, the effects ripple through the entire food web. Removing predators causes herbivore overpopulation and plant destruction. Removing producers causes total ecosystem collapse. Decomposers recycle matter so the cycle can continue.",
    "stem_title": "Restore the Broken Ecosystem",
    "stem_mission": "Design a plan to restore a damaged ecosystem where a key species has been lost.",
    "stem_scenario": "A lake ecosystem has lost its top predator (bass) due to pollution. Minnows (primary consumers) have exploded in population and are eating all the algae. Your team must restore balance.",
    "stem_questions": [
        "What was the role of bass in the original food web?",
        "Why did minnow population explode when bass were removed?",
        "What happens to the lake when algae are completely consumed?"
    ],
    "stem_design_qs": [
        "How will you reintroduce or replace the missing predator?",
        "How long will it take for the ecosystem to rebalance?",
        "What indicators will tell you the ecosystem is recovering?",
        "What other species might be affected by your restoration plan?"
    ],
    "career": "Wildlife Ecologists and Conservation Biologists study food webs and ecosystem health to protect endangered species and restore damaged habitats. They earn $65,000-$100,000/year.",
    "images": {
        "cover": ("cover-food-web.png", "A photorealistic, cinematic image of a vibrant forest ecosystem showing a hawk perched on a branch above a rabbit in a meadow surrounded by green plants, with mushrooms decomposing a fallen log nearby, ultra-crisp detail, golden hour lighting"),
        "landscape": ("landscape-food-web.png", "A photorealistic image of an Asian female student (age 10-11) leading diverse 5th graders including White, Black, and Latino classmates examining a pond ecosystem with a magnifying glass, students wearing hoodies and sneakers, natural outdoor light"),
        "modeling": ("modeling-food-web.png", "A photorealistic image of a White male student (age 10-11) at a laptop building a food web model, with Black female, Asian male, and Latina classmates discussing relationships on screen, modern classroom with animal posters"),
        "discussion": ("discussion-food-web.png", "A photorealistic image of a Black male teacher pointing at a food web diagram on a smartboard while diverse 5th graders including White, Asian, Latino, and Black students raise hands eagerly, colorful classroom"),
        "stem": ("stem-food-web.png", "A photorealistic image of a Latina female student (age 10-11) presenting an ecosystem restoration plan while White, Black, and Asian classmates examine model organisms, school science room setting")
    },
    "pre_assessment": [
        "Draw a food chain with at least three organisms. Which one is the producer?",
        "What do you think would happen if all the plants in an ecosystem died?",
        "If wolves were removed from a forest, what would happen to the deer population?",
        "What happens to a dead leaf on the forest floor over time?"
    ],
    "extend_components": [
        ("Sunlight Energy", "The energy source that drives all producer growth"),
        ("Tertiary Consumer", "A top predator like an eagle or shark"),
        ("Invasive Species", "A non-native organism that disrupts the food web")
    ],
    "reflections": [
        "Why do ecologists say 'everything is connected' in an ecosystem?",
        "What surprised you about removing predators from the system?",
        "How do decomposers prevent dead matter from piling up?",
        "What would happen if you added an invasive species to this model?",
        "How does understanding food webs help us protect endangered species?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model showing matter cycling through multiple trophic levels in a food web."),
        ("Disciplinary Core Idea", "LS2.A Interdependent Relationships in Ecosystems", "Students model how organisms depend on each other for matter and energy."),
        ("Crosscutting Concept", "Systems and System Models", "Students model the food web as an interconnected system where changes cascade through all levels.")
    ],
    "cast_items": [
        "Describe the flow of matter through a food web from producers to decomposers",
        "Predict the cascading effects of removing a species from the food web",
        "Explain how decomposers return nutrients to producers"
    ],
    "cast_questions": [
        ("Multiple Choice:", "In a grassland, wolves eat rabbits and rabbits eat grass. If wolves are removed, what happens first?"),
        ("Constructed Response:", "Explain how removing one species from a food web can cause a trophic cascade, using evidence from your model simulation.")
    ],
    "background_intro": "A food web shows the complex feeding relationships in an ecosystem. Unlike a simple food chain, a food web reveals how organisms are interconnected — and how removing one piece can cause a cascade of effects.",
    "background_sections": [
        ("Producers: The Foundation", "Plants and algae are producers that capture sunlight energy through photosynthesis. They form the base of every food web and provide energy for all consumers above."),
        ("Consumers: Energy Transfers", "Primary consumers (herbivores) eat producers. Secondary consumers (predators) eat herbivores. At each level, about 90% of energy is lost as heat, which is why predators are always rarer than prey."),
        ("Trophic Cascades", "When a species is removed, effects cascade through the web. The reintroduction of wolves to Yellowstone in 1995 is a famous example — wolves reduced elk overpopulation, allowing trees and rivers to recover."),
        ("Decomposers Close the Loop", "Bacteria, fungi, and invertebrates break down dead organisms, releasing nutrients back into the soil. Without decomposers, nutrients would be locked in dead matter and producers would starve.")
    ],
    "lever_L": "Students identify Producer Population, Primary Consumer Population, Secondary Consumer Population, Decomposer Activity, and Available Nutrients as the five system components.",
    "lever_E": "Students determine that Producers feed Primary Consumers (+), Primary Consumers feed Secondary Consumers (+), Secondary Consumers reduce Primary Consumers (-), Decomposers release Nutrients (+), and Nutrients support Producers (+).",
    "lever_V": "Students build the food web model showing circular matter flow from producers through consumers to decomposers and back to nutrients for producers.",
    "lever_Ev": "Students run the Remove Predators scenario and observe herbivore explosion followed by producer decline, then run Remove Producers to see total collapse.",
    "lever_R": "Students add Sunlight Energy, Invasive Species, or a Tertiary Consumer to make the model more complex and realistic.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Forest food web: hawk, rabbit, plants, mushrooms", "say": "What happens when you remove one puzzle piece from nature?", "do": "Ask: If all rabbits disappeared, what would happen? What about all plants?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we build a food web and test what happens when species disappear.", "do": "Students read objectives and identify vocabulary they already know.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "What happens when one species disappears?", "say": "This is called a trophic cascade, and it has happened in real life.", "do": "Share the Yellowstone wolves example briefly.", "time": "2 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "Our model has a CIRCULAR flow — nutrients come back around to the beginning.", "do": "Preview how decomposers feed nutrients back to producers.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Five component cards for food web", "say": "Producer Population is our only external component. Everything else responds to it.", "do": "Students sort components into external and internal, discussing why.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows forming a cycle", "say": "Notice the circle: producers feed consumers, dead consumers feed decomposers, decomposers feed nutrients back to producers.", "do": "Students draw all five relationship arrows.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graphs showing trophic cascade", "say": "What happens when we remove all predators? Let's watch.", "do": "Students run Remove Predators and Remove Producers scenarios.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings about food web interconnection", "say": "Everything is connected. Remove one piece and the whole system shifts.", "do": "Class discussion: Which removal caused the biggest surprise?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Ecosystem restoration plan", "say": "A lake lost its top predator. Your job: restore the balance.", "do": "Groups design restoration plans; present to class.", "time": "10 min"}
    ],
    "sort_reasoning": "Producer Population is external because it represents the base energy input that students can adjust. Primary Consumer Population, Secondary Consumer Population, Decomposer Activity, and Available Nutrients are internal because they respond to producer levels and to each other in a cascading system.",
    "relationships": [
        ("Producer Population to Primary Consumer Population", "POSITIVE (+)", "More plants provide more food for herbivores, supporting larger populations."),
        ("Primary Consumer Population to Secondary Consumer Population", "POSITIVE (+)", "More herbivores provide more food for predators."),
        ("Secondary Consumer Population to Primary Consumer Population", "NEGATIVE (-)", "More predators eat more herbivores, reducing their population."),
        ("Decomposer Activity to Available Nutrients", "POSITIVE (+)", "More decomposition releases more nutrients into the soil."),
        ("Available Nutrients to Producer Population", "POSITIVE (+)", "More soil nutrients help producers grow, supporting larger plant populations.")
    ],
    "sim_answers": [
        ("Remove Predators", "When Secondary Consumers drop to 0%, Primary Consumers (herbivores) explode in population because nothing is eating them. They rapidly consume Producers, causing Producer Population to crash. As Producers decline, herbivores eventually starve. The entire food web destabilizes."),
        ("Remove Producers", "When Producers drop to 0%, Primary Consumers starve first, then Secondary Consumers starve. Decomposer Activity continues briefly on dead organisms but eventually stops. Available Nutrients accumulate but have no producers to use them. Total ecosystem collapse.")
    ],
    "reflection_exemplars": [
        ("What surprised you about removing predators?", "I expected removing predators to help herbivores, but it actually destroyed the whole ecosystem. Without predators controlling herbivore numbers, herbivores overate the plants. When plants were gone, herbivores starved too. Predators actually PROTECT the ecosystem."),
        ("How do decomposers prevent dead matter from piling up?", "Decomposers break down dead plants and animals into simple nutrients. Without them, dead matter would accumulate and nutrients would be locked away. Decomposers recycle matter so producers can use it again — they complete the cycle.")
    ],
    "stem_intro": "Present the lake scenario: Bass were killed by pollution. Now minnows are eating all the algae. The lake is out of balance. Connect to the model: removing a component causes cascade effects.",
    "stem_concepts": [
        ("Trophic Cascade in Action", "Removing a top predator allows prey to overpopulate, which can devastate the next level down."),
        ("Species Reintroduction", "Reintroducing a missing species can restore balance, as seen with wolves in Yellowstone."),
        ("Indicator Species", "Certain organisms (like algae levels or fish diversity) indicate whether an ecosystem is healthy or damaged.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan addresses predator reintroduction, timeline, indicators, and connects reasoning to food web model"),
        ("Proficient (3)", "Plan addresses reintroduction and one monitoring strategy with reasoning"),
        ("Developing (2)", "Plan mentions restoration but lacks detail on monitoring or reasoning"),
        ("Beginning (1)", "Plan does not connect to food web dynamics or lacks scientific reasoning")
    ],
    "support": [
        "Provide a visual food web diagram with arrows showing energy flow",
        "Use sentence frames: 'When producer population decreases, primary consumers __ because...'",
        "Use physical cards with organisms that students can arrange and rearrange"
    ],
    "extensions": [
        "Research the Yellowstone wolf reintroduction and its cascading effects",
        "Add an invasive species component and explore how it disrupts the food web",
        "Compare food web complexity in different biomes (rainforest vs desert)"
    ],
    "cross_curr": [
        ("Math", "Graph population changes across three trophic levels over time"),
        ("ELA", "Write a proposal for an ecosystem restoration project using model evidence"),
        ("Social Studies", "Research how human activities (hunting, deforestation) have disrupted real food webs")
    ],
    "misconceptions": [
        ("Food chains are straight lines", "Real ecosystems are food WEBS with many interconnected chains. An animal may eat multiple food sources and be eaten by multiple predators.", "Draw a food web for your backyard — most organisms connect to more than one other species."),
        ("Removing predators helps prey animals", "In the short term, prey populations increase. But without predators controlling their numbers, prey overpopulate, destroy their food source, and eventually crash.", "The Yellowstone example: removing wolves led to elk destroying riverbanks and forests."),
        ("Decomposers are not important", "Without decomposers, dead matter would pile up and nutrients would never return to the soil. Producers would run out of nutrients and the entire food web would collapse.", "Place a leaf in a sealed jar with soil vs without soil. The one with soil decomposers breaks down.")
    ]
}

L06 = {
    "id": "G05L2-L06",
    "title": "Earth Systems Collide: Volcanoes, Climate, and Life",
    "subtitle": "How a Volcanic Eruption Can Change the Whole Planet",
    "ngss": "5-ESS2-1",
    "ngss_desc": "Develop a model using an example to describe ways the geosphere, biosphere, hydrosphere, and/or atmosphere interact.",
    "big_question": "How can a volcano on one continent change the climate on another?",
    "objectives": [
        "Model how volcanic eruptions release CO2 into the atmosphere",
        "Explain how increased atmospheric CO2 raises global temperature",
        "Demonstrate how vegetation and ocean absorption create negative feedback loops",
        "Predict what happens to global temperature when volcanic activity increases"
    ],
    "vocabulary": [
        ("Geosphere", "The solid Earth, including rocks, mountains, and the mantle"),
        ("Atmosphere", "The layer of gases surrounding Earth"),
        ("Negative Feedback", "A response that counteracts a change, pushing a system back toward balance"),
        ("Greenhouse Gas", "A gas like CO2 that traps heat in the atmosphere")
    ],
    "components": [
        ("Volcanic Activity", "The frequency and intensity of volcanic eruptions", True),
        ("Atmospheric CO2", "The amount of carbon dioxide gas in Earth's atmosphere", False),
        ("Global Temperature", "Earth's average surface temperature", False),
        ("Ocean Absorption", "The amount of CO2 absorbed by the world's oceans", False),
        ("Vegetation Growth", "The amount of plant growth responding to temperature and CO2", False)
    ],
    "think_about_it": "When a volcano erupts and releases CO2, what do you think happens to Earth's temperature over time?",
    "scenarios": [
        ("Normal Earth", "Set Volcanic Activity to a low level and observe stability"),
        ("Massive Eruption", "Set Volcanic Activity to 90% and watch the cascade"),
        ("Self-Regulation", "Set Volcanic Activity to 60% and observe how vegetation and oceans respond")
    ],
    "sim_scenarios": [
        ("Normal Earth", "Low volcanic activity", "What do you predict will happen to Global Temperature?"),
        ("Massive Eruption", "Volcanic Activity at 90%", "What do you predict will happen to Atmospheric CO2 and then Global Temperature?"),
        ("Self-Regulation", "Volcanic Activity at 60%", "Will vegetation and ocean absorption bring the system back to balance?")
    ],
    "discoveries": [
        "Volcanic eruptions add CO2 to the atmosphere, which raises global temperature",
        "Warmer temperatures and more CO2 cause plants to grow faster, absorbing some CO2 (negative feedback)",
        "Oceans also absorb CO2, helping to regulate the atmosphere (another negative feedback)",
        "Earth has natural self-regulation systems, but they can be overwhelmed by extreme events"
    ],
    "answer": "A volcanic eruption releases CO2 into the atmosphere, raising global temperature. But Earth fights back — plants grow faster and absorb more CO2, and oceans soak up CO2 too. These negative feedback loops help stabilize the climate, but extreme eruptions can overwhelm them temporarily.",
    "stem_title": "Design an Early Warning Climate System",
    "stem_mission": "Design a monitoring system that could detect and predict climate changes after a major volcanic eruption.",
    "stem_scenario": "A supervolcano like Yellowstone could erupt in the future. Your team needs to design a global monitoring system that tracks CO2, temperature, ocean chemistry, and vegetation changes to predict the climate impact.",
    "stem_questions": [
        "What measurements would tell you the climate is changing after an eruption?",
        "How quickly does CO2 from a volcano spread around the globe?",
        "How long does it take for vegetation and oceans to absorb the extra CO2?"
    ],
    "stem_design_qs": [
        "What sensors will your system include and where will they be placed?",
        "How will you measure atmospheric CO2, temperature, ocean absorption, and vegetation?",
        "How will you display the data so leaders can make decisions quickly?",
        "What thresholds will trigger warnings?"
    ],
    "career": "Volcanologists and Climate Modelers study how volcanic eruptions affect Earth's climate. They use computer models similar to what you built today to predict future climate changes. They earn $70,000-$120,000/year.",
    "images": {
        "cover": ("cover-earth-systems.png", "A photorealistic, cinematic image of a volcanic eruption with a massive ash plume rising into the atmosphere, lush green vegetation in the foreground, and ocean visible in the background, showing the connection between geosphere, atmosphere, biosphere, and hydrosphere, ultra-crisp detail"),
        "landscape": ("landscape-earth-systems.png", "A photorealistic image of a Black female student (age 10-11) leading diverse 5th graders including White, Asian, and Latino classmates examining volcanic rock samples at a geology table, wearing modern hoodies and sneakers, well-lit classroom, engaged expressions"),
        "modeling": ("modeling-earth-systems.png", "A photorealistic image of a Latino male student (age 10-11) at a laptop building an Earth systems model, with White female, Asian male, and Black female classmates pointing at CO2 and temperature graphs on screen, modern classroom"),
        "discussion": ("discussion-earth-systems.png", "A photorealistic image of a White male teacher pointing at a diagram showing Earth's four spheres interacting while diverse 5th graders including Asian, Black, Latino, and White students take notes, classroom with globe and rock samples"),
        "stem": ("stem-earth-systems.png", "A photorealistic image of an Asian female student (age 10-11) presenting a climate monitoring system poster while Black, White, and Latino classmates ask questions, school science exhibition setting")
    },
    "pre_assessment": [
        "What gases come out of a volcano when it erupts?",
        "Do you think a volcano in one country can affect the weather in another country? Why or why not?",
        "What are Earth's four major systems (spheres)? Name as many as you can.",
        "What do you think 'negative feedback' means in science?"
    ],
    "extend_components": [
        ("Volcanic Ash", "Ash particles that block sunlight, temporarily cooling the planet"),
        ("Ice Cap Melting", "Glaciers that melt as global temperature rises"),
        ("Human CO2 Emissions", "Carbon dioxide added by humans burning fossil fuels")
    ],
    "reflections": [
        "How does Earth regulate its own temperature naturally?",
        "What surprised you about how vegetation responds to increased CO2?",
        "How is the volcanic CO2 cycle similar to or different from human CO2 emissions?",
        "If Earth's self-regulation systems can handle volcanoes, can they handle human emissions too?",
        "Why is it important to study how Earth's systems interact?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model showing interactions between the geosphere, atmosphere, biosphere, and hydrosphere."),
        ("Disciplinary Core Idea", "ESS2.A Earth Materials and Systems", "Students model how volcanic activity affects atmospheric CO2 and global temperature."),
        ("Crosscutting Concept", "Systems and System Models", "Students model Earth as a system with feedback loops that promote stability.")
    ],
    "cast_items": [
        "Describe how volcanic eruptions affect atmospheric CO2 and global temperature",
        "Explain how vegetation and ocean absorption create negative feedback loops",
        "Predict how Earth's systems respond to a major volcanic eruption"
    ],
    "cast_questions": [
        ("Multiple Choice:", "After a massive volcanic eruption, atmospheric CO2 rises sharply. Which of the following is a negative feedback that helps reduce CO2?"),
        ("Constructed Response:", "Explain how a volcanic eruption in Asia could affect the climate in North America, using evidence from your model.")
    ],
    "background_intro": "Earth is a system of interacting spheres — the geosphere (rock), atmosphere (air), hydrosphere (water), and biosphere (life). Volcanic eruptions are a dramatic example of how one sphere's activity can ripple through all the others.",
    "background_sections": [
        ("Volcanoes and CO2", "When volcanoes erupt, they release large amounts of CO2 and other gases into the atmosphere. Over geologic time, volcanic CO2 has been a major driver of climate change."),
        ("The Greenhouse Effect", "CO2 is a greenhouse gas that traps heat in the atmosphere. More CO2 means more heat is retained, raising global temperatures. This is the greenhouse effect."),
        ("Negative Feedback: Vegetation", "When CO2 and temperature rise, plants grow faster because they have more CO2 for photosynthesis. This increased growth absorbs some of the extra CO2, partially counteracting the warming."),
        ("Negative Feedback: Ocean Absorption", "Oceans absorb about 30% of atmospheric CO2. As CO2 levels rise, oceans absorb more. However, this also makes oceans more acidic, which harms marine life.")
    ],
    "lever_L": "Students identify Volcanic Activity, Atmospheric CO2, Global Temperature, Ocean Absorption, and Vegetation Growth as the five system components.",
    "lever_E": "Students determine that Volcanic Activity increases CO2 (+), CO2 increases Temperature (+), Temperature increases Vegetation (+), Vegetation decreases CO2 (-), and Ocean Absorption decreases CO2 (-).",
    "lever_V": "Students build the Earth systems model showing how volcanic CO2 drives warming while vegetation and oceans create negative feedback loops.",
    "lever_Ev": "Students run the Massive Eruption scenario and observe CO2 and temperature spiking, then the Self-Regulation scenario to see feedback loops in action.",
    "lever_R": "Students add Volcanic Ash (cooling effect), Ice Cap Melting, or Human CO2 Emissions to explore more complex Earth system interactions.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Volcanic eruption with vegetation and ocean visible", "say": "A volcano erupts in Asia. Could it change the weather in your town?", "do": "Show eruption image and ask: What comes out of a volcano besides lava?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we model how Earth's four spheres interact during a volcanic eruption.", "do": "Students list the four spheres: geosphere, atmosphere, biosphere, hydrosphere.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How can a volcano on one continent change the climate on another?", "say": "Volcanoes don't just affect the nearby area. Their impact is GLOBAL.", "do": "Quick pair-share: How could volcanic gas travel around the world?", "time": "2 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "Our model includes a new concept: negative feedback loops.", "do": "Define negative feedback and preview how it appears in the model.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Five component cards", "say": "Volcanic Activity is our only external input. Everything else responds in a chain.", "do": "Students sort components and predict which sphere each belongs to.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows with feedback loops highlighted", "say": "Look at the arrows from Vegetation and Ocean back to CO2. Those are negative feedback loops — Earth fighting back.", "do": "Students draw all five relationships and identify the two feedback loops.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graphs showing CO2, temperature, and feedback responses", "say": "Massive eruption! Watch CO2 and temperature spike — then watch Earth respond.", "do": "Students run Massive Eruption and Self-Regulation scenarios.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings about Earth's self-regulation", "say": "Earth has built-in stabilizers. But can they handle everything we throw at them?", "do": "Class discussion: How is volcanic CO2 different from human CO2 emissions?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Climate monitoring system design", "say": "If Yellowstone erupted, how would we track the climate changes?", "do": "Groups design monitoring systems; present to class.", "time": "10 min"}
    ],
    "sort_reasoning": "Volcanic Activity is external because it represents a geosphere input that students can adjust. Atmospheric CO2, Global Temperature, Ocean Absorption, and Vegetation Growth are internal because they respond to volcanic input and to each other through feedback loops.",
    "relationships": [
        ("Volcanic Activity to Atmospheric CO2", "POSITIVE (+)", "Volcanic eruptions release large amounts of CO2 into the atmosphere."),
        ("Atmospheric CO2 to Global Temperature", "POSITIVE (+)", "More CO2 traps more heat, increasing Earth's average temperature."),
        ("Global Temperature to Vegetation Growth", "POSITIVE (+)", "Warmer temperatures and more CO2 stimulate plant growth (to a point)."),
        ("Vegetation Growth to Atmospheric CO2", "NEGATIVE (-)", "More vegetation absorbs more CO2 through photosynthesis, reducing atmospheric levels."),
        ("Ocean Absorption to Atmospheric CO2", "NEGATIVE (-)", "Oceans absorb CO2 from the atmosphere, reducing atmospheric levels.")
    ],
    "sim_answers": [
        ("Massive Eruption", "When Volcanic Activity is set to 90%, Atmospheric CO2 spikes dramatically. Global Temperature rises in response. Vegetation Growth and Ocean Absorption increase, trying to counteract the CO2 rise, but they cannot fully compensate for the extreme input."),
        ("Self-Regulation", "At 60% Volcanic Activity, CO2 and Temperature rise moderately. Vegetation and Ocean Absorption increase enough to partially offset the CO2 input. The system reaches a new, higher equilibrium rather than spiraling out of control. This demonstrates Earth's negative feedback in action.")
    ],
    "reflection_exemplars": [
        ("How does Earth regulate its own temperature?", "Earth has negative feedback loops. When CO2 rises, plants grow faster and absorb more CO2. Oceans also absorb more CO2. These processes counteract the warming, pushing the system back toward balance — though not always perfectly."),
        ("Can Earth's systems handle human emissions?", "Earth's natural feedback loops developed over millions of years to handle volcanic CO2. Human emissions have risen far faster than volcanic emissions ever did. The feedback loops help, but they cannot keep pace with the rate of human CO2 addition.")
    ],
    "stem_intro": "Present the Yellowstone supervolcano scenario. It last erupted 640,000 years ago. If it erupted today, how would we track and predict the climate impact? Connect to the model: our monitoring system needs to track all five components.",
    "stem_concepts": [
        ("CO2 Monitoring", "The Mauna Loa Observatory in Hawaii has measured atmospheric CO2 continuously since 1958, showing steady increases."),
        ("Satellite Temperature Tracking", "NASA satellites measure global temperature from space, providing data for climate models."),
        ("Ocean Chemistry Sensors", "Buoys and underwater sensors track ocean CO2 absorption and acidity worldwide.")
    ],
    "stem_eval": [
        ("Expert (4)", "System monitors all key variables (CO2, temperature, ocean, vegetation), includes thresholds, and connects to model"),
        ("Proficient (3)", "System monitors 3-4 variables with warning thresholds"),
        ("Developing (2)", "System monitors 1-2 variables without clear thresholds"),
        ("Beginning (1)", "System lacks clear variables to monitor or connection to Earth systems model")
    ],
    "support": [
        "Provide a labeled diagram of Earth's four spheres with arrows showing interactions",
        "Use sentence frames: 'When volcanic activity increases, atmospheric CO2 __ because...'",
        "Use color-coded arrows: red for positive relationships, blue for negative feedback"
    ],
    "extensions": [
        "Research the 1815 eruption of Mount Tambora and its 'Year Without a Summer' effect",
        "Add Human CO2 Emissions as a component and compare to volcanic emissions",
        "Investigate ocean acidification as a consequence of CO2 absorption"
    ],
    "cross_curr": [
        ("Math", "Graph the relationship between CO2 concentration and temperature using real climate data"),
        ("ELA", "Write a news report about a fictional supervolcano eruption and its predicted global effects"),
        ("Social Studies", "Research how the eruption of Mount Pinatubo in 1991 affected global weather patterns")
    ],
    "misconceptions": [
        ("Volcanoes only affect the area nearby", "Volcanic gases and ash can circle the entire globe within weeks. Major eruptions have changed global temperatures for years.", "Show maps of how ash from Mount Pinatubo spread across the entire planet."),
        ("Earth's temperature is always the same", "Earth's temperature has changed dramatically over geologic time, driven by volcanic activity, solar changes, and CO2 levels.", "Show a graph of Earth's temperature over the last million years."),
        ("Plants can solve climate change on their own", "While plants absorb CO2, there are limits. Deforestation is removing plants, and human CO2 emissions are far greater than what current vegetation can absorb.", "Calculate: How many new trees would we need to plant to absorb one year of human CO2 emissions?")
    ]
}

L07 = {
    "id": "G05L2-L07",
    "title": "Starlight and Distance: Mapping the Universe",
    "subtitle": "Why the Brightest Star You See Might Not Be the Closest",
    "ngss": "5-ESS1-1",
    "ngss_desc": "Support an argument that differences in the apparent brightness of the sun compared to other stars is due to their relative distances from Earth.",
    "big_question": "How do we know how far away stars are if we can't travel to them?",
    "objectives": [
        "Model how a star's actual brightness and distance affect its apparent brightness",
        "Explain why a dim-looking star might actually be brighter than a bright-looking star",
        "Demonstrate the relationship between distance and light travel time",
        "Predict how distance affects our ability to observe detail in distant objects"
    ],
    "vocabulary": [
        ("Apparent Brightness", "How bright a star LOOKS from Earth, which depends on distance"),
        ("Actual Brightness", "How much light a star truly produces, also called luminosity"),
        ("Light-Year", "The distance light travels in one year — about 6 trillion miles"),
        ("Observable Detail", "How much information we can see about a distant object")
    ],
    "components": [
        ("Star Actual Brightness", "How much light the star truly produces (luminosity)", True),
        ("Distance from Earth", "How far away the star is, measured in light-years", True),
        ("Apparent Brightness", "How bright the star appears to someone looking from Earth", False),
        ("Light Travel Time", "How long the star's light takes to reach Earth", False),
        ("Observable Detail", "How much detail we can see about the star from Earth", False)
    ],
    "think_about_it": "A flashlight looks very bright up close but dim from far away. Does the flashlight get weaker, or does something else change?",
    "scenarios": [
        ("Nearby Star", "Set Star Actual Brightness to 50% and Distance to 10%"),
        ("Distant Giant", "Set Star Actual Brightness to 100% and Distance to 90%"),
        ("The Trick Question", "Set Star Actual Brightness to 30% and Distance to 5% vs Brightness 90% and Distance 80%")
    ],
    "sim_scenarios": [
        ("Nearby Star", "Moderate brightness, very close", "What do you predict for Apparent Brightness?"),
        ("Distant Giant", "Maximum brightness, very far away", "What do you predict for Apparent Brightness compared to the nearby star?"),
        ("Side-by-Side", "Dim close star vs bright distant star", "Which one looks brighter from Earth?")
    ],
    "discoveries": [
        "A star's apparent brightness depends on BOTH its actual brightness AND its distance from Earth",
        "A dim-looking star might actually be the brightest star in the galaxy — just very far away",
        "The farther a star is, the longer its light takes to reach us — we see it as it was in the past",
        "Distance reduces both apparent brightness and observable detail"
    ],
    "answer": "We figure out how far stars are by comparing how bright they LOOK (apparent brightness) with how bright they actually ARE (actual brightness). If a star is very bright but looks dim, it must be very far away. Distance is the key that makes bright things look dim.",
    "stem_title": "Design a Star Distance Calculator",
    "stem_mission": "Design a method to determine how far away an unknown star is using only its apparent and actual brightness.",
    "stem_scenario": "NASA has discovered a new star. They know its actual brightness from its color and size, and they can measure its apparent brightness from Earth. Your team must design a method to calculate its distance.",
    "stem_questions": [
        "If you know how bright a star really is and how bright it looks, what can you figure out?",
        "How does distance affect apparent brightness? Is there a pattern?",
        "Why do astronomers need to know star distances?"
    ],
    "stem_design_qs": [
        "What measurements will you need (actual brightness, apparent brightness)?",
        "What is the relationship between distance and apparent brightness?",
        "How will you present your method so other scientists can use it?",
        "How accurate do you think your method is? What could cause errors?"
    ],
    "career": "Astrophysicists and Stellar Astronomers study stars to understand the universe. They use the exact relationship you modeled today — comparing actual and apparent brightness — to map the cosmos. They earn $80,000-$150,000/year.",
    "images": {
        "cover": ("cover-starlight-distance.png", "A photorealistic, cinematic image of a stunning night sky filled with stars of varying brightness, with a telescope silhouetted in the foreground, showing the Milky Way band, ultra-crisp detail, deep blues and golds"),
        "landscape": ("landscape-starlight-distance.png", "A photorealistic image of a White female student (age 10-11) looking through a telescope while diverse 5th graders including Black, Asian, and Latino classmates wait their turn excitedly, school rooftop or outdoor observation area, twilight sky"),
        "modeling": ("modeling-starlight-distance.png", "A photorealistic image of a Black male student (age 10-11) at a laptop building a star brightness model, with White female, Asian male, and Latina classmates comparing model predictions to a star chart, modern classroom, natural light"),
        "discussion": ("discussion-starlight-distance.png", "A photorealistic image of a Latina female teacher using a flashlight at different distances to demonstrate apparent brightness while diverse 5th graders including White, Black, and Asian students observe, dimmed classroom"),
        "stem": ("stem-starlight-distance.png", "A photorealistic image of an Asian male student (age 10-11) presenting a star distance calculator poster while White, Black, and Latina classmates examine a star chart, school library or science room, warm lighting")
    },
    "pre_assessment": [
        "Look at the stars tonight (or imagine them). Are the brightest ones the closest? How do you know?",
        "If you hold a flashlight close to your face and then far away, what changes? Does the flashlight change?",
        "How do you think scientists figure out how far away a star is?",
        "What is a light-year? Take your best guess."
    ],
    "extend_components": [
        ("Telescope Power", "A stronger telescope can resolve more detail at greater distances"),
        ("Star Color", "A star's color tells us its temperature and actual brightness"),
        ("Atmospheric Interference", "Earth's atmosphere blurs starlight, reducing observable detail")
    ],
    "reflections": [
        "Why is it misleading to say 'that star is the brightest in the sky'?",
        "When you look at a star 100 light-years away, what are you actually seeing?",
        "How did this model change your understanding of what you see in the night sky?",
        "Why is it important for astronomers to know actual brightness, not just apparent brightness?",
        "What limitations does this model have? What would make it more realistic?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model showing how distance and actual brightness determine what we observe from Earth."),
        ("Disciplinary Core Idea", "ESS1.A The Universe and Its Stars", "Students model the relationship between distance and apparent brightness to explain star observations."),
        ("Crosscutting Concept", "Scale, Proportion, and Quantity", "Students explore how vast distances affect our perception of star brightness.")
    ],
    "cast_items": [
        "Explain why apparent brightness is different from actual brightness",
        "Use the model to predict a star's relative distance based on apparent and actual brightness",
        "Describe how light travel time connects to our view of the past"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Star A looks brighter than Star B in the night sky. Which statement MUST be true?"),
        ("Constructed Response:", "Two stars have the same actual brightness, but Star X looks much brighter than Star Y. Explain what this tells us about their distances from Earth, using evidence from your model.")
    ],
    "background_intro": "When you look at the night sky, the stars appear to have different brightnesses. But apparent brightness is deceiving — it depends on both how much light a star produces AND how far away it is. Understanding this relationship is key to mapping the universe.",
    "background_sections": [
        ("Apparent vs. Actual Brightness", "A star's apparent brightness is how bright it looks from Earth. Its actual brightness (luminosity) is how much light it truly produces. A very bright star that is far away can look dimmer than a less bright star that is close."),
        ("The Inverse Square Law", "Light spreads out as it travels. At twice the distance, light covers four times the area, so it appears one-quarter as bright. This is the inverse square law, and it is why distance has such a dramatic effect."),
        ("Light Travel Time", "Light travels at 186,000 miles per second. Even at this speed, light from the nearest star (Proxima Centauri) takes 4.24 years to reach us. We see that star as it was over four years ago."),
        ("Measuring Star Distances", "Astronomers use several methods to measure distances. For nearby stars, they use parallax (the apparent shift of a star as Earth orbits the sun). For distant stars, they compare actual and apparent brightness — the same principle in your model.")
    ],
    "lever_L": "Students identify Star Actual Brightness, Distance from Earth, Apparent Brightness, Light Travel Time, and Observable Detail as the five system components.",
    "lever_E": "Students determine that Actual Brightness increases Apparent Brightness (+), Distance decreases Apparent Brightness (-), Distance increases Light Travel Time (+), Actual Brightness increases Observable Detail (+), and Distance decreases Observable Detail (-).",
    "lever_V": "Students build the starlight model showing how the same star looks different depending on its distance from Earth.",
    "lever_Ev": "Students run the Distant Giant scenario and discover that the brightest star in the galaxy can look dim from Earth, then run the Trick Question to compare two stars side by side.",
    "lever_R": "Students add Telescope Power or Atmospheric Interference to explore how technology and conditions affect observation.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Stunning night sky with stars of varying brightness", "say": "The brightest star you see tonight might not be the closest. How is that possible?", "do": "Show a night sky image and ask: Which star do you think is closest?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we discover why appearance can be deceiving when it comes to stars.", "do": "Students read objectives and share what they think 'apparent' means.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How do we know how far away stars are?", "say": "We can't fly to a star. We can't stretch a tape measure. So how do scientists figure it out?", "do": "Partner discussion: brainstorm ideas for measuring star distances.", "time": "2 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "Our model has TWO external inputs that compete with each other.", "do": "Preview: actual brightness helps us see, but distance takes it away.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Five component cards", "say": "Star Actual Brightness and Distance from Earth are external — we can set them. The other three respond.", "do": "Students sort components and predict relationships before building.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows with +/- signs", "say": "Notice that Distance has all NEGATIVE effects on what we can observe. That's the challenge of astronomy.", "do": "Students draw all five relationship arrows in ModelIt.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graphs comparing nearby star vs distant giant", "say": "Which star looks brighter — the close dim one or the far bright one? Let's test it.", "do": "Students run all three scenarios and record predictions vs results.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings about starlight and distance", "say": "You can't trust your eyes alone. Distance is the hidden variable.", "do": "Class discussion: Why is this important for mapping the universe?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Star distance calculator design", "say": "NASA needs your help. Design a method to calculate star distances.", "do": "Groups create calculator methods; test with sample data.", "time": "10 min"}
    ],
    "sort_reasoning": "Star Actual Brightness and Distance from Earth are external because they represent inherent star properties and positions that students can adjust. Apparent Brightness, Light Travel Time, and Observable Detail are internal because they are determined by the combination of actual brightness and distance.",
    "relationships": [
        ("Star Actual Brightness to Apparent Brightness", "POSITIVE (+)", "A star that produces more light will appear brighter from Earth."),
        ("Distance from Earth to Apparent Brightness", "NEGATIVE (-)", "The farther a star is, the dimmer it appears because light spreads out over distance."),
        ("Distance from Earth to Light Travel Time", "POSITIVE (+)", "The farther a star is, the longer its light takes to reach Earth."),
        ("Star Actual Brightness to Observable Detail", "POSITIVE (+)", "Brighter stars provide more light, allowing us to observe more detail."),
        ("Distance from Earth to Observable Detail", "NEGATIVE (-)", "Greater distance reduces the amount of detail we can resolve, even with telescopes.")
    ],
    "sim_answers": [
        ("Distant Giant", "Even with Star Actual Brightness at 100%, the 90% distance makes Apparent Brightness moderate or low. Light Travel Time is very long, meaning we see the star as it was long ago. Observable Detail is low despite the star being incredibly bright."),
        ("The Trick Question", "The dim close star (30% brightness, 5% distance) appears BRIGHTER than the bright distant star (90% brightness, 80% distance). This proves that distance is often more important than actual brightness for what we see from Earth.")
    ],
    "reflection_exemplars": [
        ("Why is it misleading to say a star is the brightest?", "We should specify whether we mean apparent or actual brightness. Sirius is the brightest star in our sky (apparent), but it is not actually the most luminous star — it just happens to be relatively close at 8.6 light-years away."),
        ("When you look at a star 100 light-years away, what do you see?", "You are seeing the star as it was 100 years ago, because that is how long its light took to reach you. If that star exploded 50 years ago, you would not know for another 50 years. We see the past when we look at stars.")
    ],
    "stem_intro": "Present the NASA scenario: A new star has been discovered. We know its color tells us its actual brightness. We can measure how bright it looks from Earth. How do we calculate the distance? Connect to the model.",
    "stem_concepts": [
        ("Standard Candles", "Certain types of stars always have the same actual brightness. By measuring their apparent brightness, astronomers can calculate their distance."),
        ("The Inverse Square Law", "Light intensity decreases with the square of the distance. At twice the distance, a star appears 1/4 as bright."),
        ("Parallax", "For nearby stars, astronomers measure the tiny apparent shift as Earth orbits the sun. Larger shift = closer star.")
    ],
    "stem_eval": [
        ("Expert (4)", "Method uses brightness comparison correctly, shows mathematical reasoning, and identifies sources of error"),
        ("Proficient (3)", "Method uses brightness comparison with reasonable logic and one consideration of accuracy"),
        ("Developing (2)", "Method mentions brightness but lacks clear mathematical or logical steps"),
        ("Beginning (1)", "Method does not use the relationship between actual and apparent brightness")
    ],
    "support": [
        "Use a flashlight at different distances to physically demonstrate apparent brightness changes",
        "Use sentence frames: 'When distance increases, apparent brightness __ because...'",
        "Provide a pre-made data table for recording simulation observations"
    ],
    "extensions": [
        "Research the 20 brightest stars in the sky and compare their actual brightness vs distance",
        "Add Telescope Power as a component and explore how technology helps overcome distance",
        "Calculate how long it would take to travel to the nearest star at different speeds"
    ],
    "cross_curr": [
        ("Math", "Use the inverse square law to calculate apparent brightness at different distances"),
        ("ELA", "Write a science fiction story where a character travels to a star they always thought was dim but is actually incredibly bright"),
        ("Social Studies", "Research how ancient civilizations used star brightness for navigation")
    ],
    "misconceptions": [
        ("The brightest-looking stars are the closest", "Many of the brightest stars in the sky are not the closest. Sirius looks brightest because it is relatively close AND luminous, but Rigel is much farther and still very bright because of its enormous actual brightness.", "Compare Sirius (8.6 light-years, moderate luminosity) with Rigel (860 light-years, extreme luminosity)."),
        ("Stars are all the same brightness", "Stars vary enormously in actual brightness. Some produce millions of times more light than the Sun, while others produce only a fraction.", "Show a comparison chart of star luminosities."),
        ("We see stars as they are right now", "We see stars as they were when their light left them. A star 50 light-years away is seen as it was 50 years ago. The farther the star, the further back in time we are looking.", "Ask: If the Sun went dark right now, how long before we would notice? (8 minutes)")
    ]
}

L08 = {
    "id": "G05L2-L08",
    "title": "Why Does Ice Cream Melt Faster on a Hot Day?",
    "subtitle": "How Heat Energy Transfers from the Environment to Frozen Treats",
    "ngss": "5-PS1-1, 5-PS1-3",
    "ngss_desc": "Develop a model to describe that matter is made of particles too small to be seen. Make observations and measurements to identify materials based on their properties, including thermal conductivity and insulation.",
    "big_question": "Why does ice cream melt faster on a hot day than on a cool day?",
    "objectives": [
        "Model how air temperature and insulation affect the rate of heat transfer",
        "Explain how heat energy moves from warmer surroundings to colder objects",
        "Predict how changing container insulation affects melting speed",
        "Connect particle motion to temperature and state changes"
    ],
    "vocabulary": [
        ("Heat Transfer", "The movement of thermal energy from a warmer object to a cooler object"),
        ("Insulation", "A material that slows down heat transfer"),
        ("Melting", "The change from solid to liquid caused by absorbing heat energy"),
        ("Thermal Energy", "The total energy of moving particles in a substance")
    ],
    "components": [
        ("Air Temperature", "The temperature of the surrounding environment", True),
        ("Container Insulation", "How well the container blocks heat from reaching the ice cream", True),
        ("Heat Transfer Rate", "How quickly thermal energy moves from the air to the ice cream", False),
        ("Melting Speed", "How fast the ice cream changes from solid to liquid", False),
        ("Ice Cream State", "The current condition of the ice cream — fully frozen, slushy, or melted", False)
    ],
    "think_about_it": "If you put one scoop of ice cream on a plate and another in a thermos, which one melts first? Why?",
    "scenarios": [
        ("Hot Summer Day", "Set Air Temperature to 90% and Container Insulation to 10%"),
        ("Insulated Container", "Set Air Temperature to 90% and Container Insulation to 90%"),
        ("Cool Day, No Insulation", "Set Air Temperature to 30% and Container Insulation to 10%")
    ],
    "sim_scenarios": [
        ("Hot Summer Day", "High air temperature, low insulation", "What do you predict will happen to Melting Speed?"),
        ("Insulated Container", "High air temperature, high insulation", "What do you predict will happen to Heat Transfer Rate compared to the hot day scenario?"),
        ("Cool Day, No Insulation", "Low air temperature, no insulation", "What do you predict will happen to Ice Cream State over time?")
    ],
    "discoveries": [
        "Heat always flows from warmer surroundings to cooler objects — never the other way",
        "Higher air temperature means a greater difference in thermal energy, so heat transfers faster",
        "Insulation slows heat transfer by blocking thermal energy from reaching the ice cream",
        "Melting speed depends on BOTH air temperature and insulation working together"
    ],
    "answer": "Ice cream melts faster on a hot day because the greater difference between the air temperature and the ice cream temperature causes heat energy to transfer more quickly. The heat flows from the warm air into the cold ice cream, raising its temperature until it changes from solid to liquid.",
    "stem_title": "Design the Ultimate Ice Cream Keeper",
    "stem_mission": "Design an insulated container that keeps ice cream frozen the longest on a hot day.",
    "stem_scenario": "Your school's summer fair is outdoors in 95-degree heat. The ice cream stand needs a way to keep scoops frozen for at least 30 minutes without electricity. Your team must design and test an insulated container.",
    "stem_questions": [
        "Which materials are the best insulators and why?",
        "How does the thickness of insulation affect heat transfer rate?",
        "What role does the container's color play in absorbing or reflecting heat?"
    ],
    "stem_design_qs": [
        "What insulating materials will you use (foam, fabric, foil, air gaps)?",
        "How will you minimize the opening where heat can enter?",
        "How will you test whether your design actually slows melting?",
        "How will you measure melting speed to compare designs?"
    ],
    "career": "Materials Scientists and Thermal Engineers design insulation for everything from food containers to spacecraft. They use the same heat transfer principles you modeled today. They earn $75,000-$130,000/year.",
    "images": {
        "cover": ("cover-ice-cream-melting.png", "A photorealistic, cinematic image of a scoop of ice cream melting on a cone in bright summer sunlight, with visible heat waves and dripping liquid, vibrant colors, ultra-crisp detail"),
        "landscape": ("landscape-ice-cream-melting.png", "A photorealistic image of a Latino male student (age 10-11) holding an ice cream cone outdoors on a hot day while diverse 5th graders including Black, Asian, and White classmates observe the melting with clipboards, modern casual clothing, bright natural sunlight"),
        "modeling": ("modeling-ice-cream-melting.png", "A photorealistic image of a Black female student (age 10-11) at a laptop building a heat transfer model, with White male, Asian female, and Latino classmates comparing results, modern classroom with science posters, natural light"),
        "discussion": ("discussion-ice-cream-melting.png", "A photorealistic image of a White male teacher demonstrating insulation materials while diverse 5th graders including Black, Latino, and Asian students examine different containers, classroom with thermal experiment setup, warm lighting"),
        "stem": ("stem-ice-cream-melting.png", "A photorealistic image of an Asian female student (age 10-11) presenting an insulated container design while Black, White, and Latino classmates test their own prototypes, school makerspace setting, bright natural light")
    },
    "pre_assessment": [
        "Why does ice cream melt? What causes it to change from solid to liquid?",
        "If you hold an ice cube in your hand, your hand feels cold. Is cold moving to your hand, or is something else happening?",
        "Draw what you think is happening to the ice cream particles as it melts.",
        "What could you do to keep ice cream frozen longer without a freezer?"
    ],
    "extend_components": [
        ("Ice Cream Volume", "Larger scoops take longer to melt because there is more frozen material to warm up"),
        ("Wind Speed", "Moving air carries heat to the ice cream faster than still air"),
        ("Direct Sunlight", "Sunlight adds radiant heat energy directly to the ice cream surface")
    ],
    "reflections": [
        "Why does heat always flow from hot to cold and never the other way?",
        "How is a thermos like a winter coat? What do they have in common?",
        "What surprised you most about how insulation affected melting speed?",
        "If you could add one more component to this model, what would it be and why?",
        "How does understanding heat transfer help engineers design better products?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model showing how air temperature and insulation control heat transfer and melting."),
        ("Disciplinary Core Idea", "PS1.A Structure and Properties of Matter", "Students model how thermal energy transfer causes changes in the state of matter from solid to liquid."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify causal relationships between temperature difference, insulation, and melting speed.")
    ],
    "cast_items": [
        "Explain how heat energy moves from the air to the ice cream",
        "Predict how insulation affects the rate of melting",
        "Describe the relationship between air temperature and heat transfer rate"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Two identical ice cream scoops are placed outside on a 95°F day. One is in a foam container and one is on a plate. Which melts first and why?"),
        ("Constructed Response:", "Explain why ice cream melts faster on a hot day than on a cool day using the concepts of heat transfer and thermal energy from your model.")
    ],
    "background_intro": "Heat transfer is one of the most fundamental concepts in physical science. Thermal energy always moves from warmer objects to cooler objects until they reach the same temperature — a state called thermal equilibrium. Ice cream melting is a perfect everyday example of this principle.",
    "background_sections": [
        ("What Is Heat Transfer?", "Heat transfer is the movement of thermal energy from a warmer substance to a cooler substance. This happens through three mechanisms: conduction (direct contact), convection (moving fluids), and radiation (electromagnetic waves). Ice cream melting involves all three."),
        ("Temperature Difference Drives the Rate", "The greater the temperature difference between two objects, the faster heat transfers. On a 95°F day, heat rushes into 25°F ice cream much faster than on a 65°F day because the temperature gap is much larger."),
        ("Insulation Slows Heat Transfer", "Insulating materials like foam, wool, and trapped air have low thermal conductivity — they resist the flow of heat. A thermos uses vacuum-sealed walls and reflective linings to minimize all three types of heat transfer."),
        ("State Change Requires Energy", "Melting is a phase change that requires energy called the heat of fusion. The ice cream must absorb enough thermal energy to break the bonds holding its particles in a solid structure before it can become liquid.")
    ],
    "lever_L": "Students identify Air Temperature, Container Insulation, Heat Transfer Rate, Melting Speed, and Ice Cream State as the five system components.",
    "lever_E": "Students determine that Air Temperature increases Heat Transfer Rate (+), Container Insulation decreases Heat Transfer Rate (-), Heat Transfer Rate increases Melting Speed (+), and Melting Speed changes Ice Cream State from frozen to melted (+).",
    "lever_V": "Students build the heat transfer model showing how external conditions (temperature and insulation) control internal responses (heat flow, melting, state change).",
    "lever_Ev": "Students run the Insulated Container scenario and observe that high insulation dramatically slows melting even on a hot day, then compare with the Cool Day scenario to see the effect of temperature alone.",
    "lever_R": "Students add Wind Speed or Direct Sunlight to explore additional factors that affect heat transfer rate.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Ice cream melting in summer sunlight", "say": "You know it happens — your ice cream melts faster on a hot day. But WHY?", "do": "Ask students to share their worst ice cream melting story.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary list", "say": "Today we model the invisible flow of heat energy.", "do": "Students read objectives and discuss what 'thermal energy' might mean.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why does ice cream melt faster on a hot day?", "say": "Everyone knows it happens, but can you explain the science behind it?", "do": "Quick-write: students write their best explanation in 30 seconds.", "time": "2 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We will model heat transfer as a system with inputs we control and outputs we observe.", "do": "Preview the five components students will work with.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Five component cards with descriptions", "say": "Air Temperature and Container Insulation are external — we set them. The other three respond.", "do": "Students sort component cards into external and internal categories.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows with +/- signs", "say": "Notice insulation has a NEGATIVE effect — it works AGAINST heat transfer. That is what makes it useful.", "do": "Guide students to draw all four relationship arrows in ModelIt.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graphs comparing melting under different conditions", "say": "Let's race: hot day vs insulated container. Which ice cream survives longer?", "do": "Students run all three scenarios and record observations.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings about heat transfer and melting", "say": "Heat always flows from hot to cold. Insulation is just a speed bump for that flow.", "do": "Class discussion: What real-world products use this principle?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Insulated container design challenge", "say": "Now design the ultimate ice cream keeper for the school fair.", "do": "Distribute materials; groups design, build, and test prototypes.", "time": "10 min"}
    ],
    "sort_reasoning": "Air Temperature and Container Insulation are external because they represent environmental conditions and design choices that students can adjust. Heat Transfer Rate, Melting Speed, and Ice Cream State are internal because they are determined by and respond to the external conditions.",
    "relationships": [
        ("Air Temperature to Heat Transfer Rate", "POSITIVE (+)", "Higher air temperature creates a larger temperature difference, driving faster heat transfer."),
        ("Container Insulation to Heat Transfer Rate", "NEGATIVE (-)", "Better insulation blocks heat from reaching the ice cream, slowing the transfer rate."),
        ("Heat Transfer Rate to Melting Speed", "POSITIVE (+)", "Faster heat transfer delivers more thermal energy to the ice cream, speeding up melting."),
        ("Melting Speed to Ice Cream State", "POSITIVE (+)", "Faster melting causes the ice cream to transition from frozen to slushy to liquid more quickly.")
    ],
    "sim_answers": [
        ("Insulated Container", "Even with Air Temperature at 90%, high insulation (90%) dramatically reduces Heat Transfer Rate. Melting Speed is much slower than the hot day scenario. The ice cream stays frozen much longer because insulation blocks most of the incoming heat energy."),
        ("Cool Day, No Insulation", "With Air Temperature at only 30%, Heat Transfer Rate is low because the temperature difference is small. Melting Speed is slow even without insulation. This shows that temperature difference is the primary driver of heat transfer.")
    ],
    "reflection_exemplars": [
        ("Why does heat always flow from hot to cold?", "Heat is the movement of thermal energy, and particles in warmer objects vibrate faster than particles in cooler objects. When they interact, the fast particles transfer energy to the slow ones until they balance out. Energy naturally spreads from concentrated areas to less concentrated areas."),
        ("How is a thermos like a winter coat?", "Both work by trapping air, which is a poor conductor of heat. A winter coat traps air between fibers to slow heat from leaving your body. A thermos traps air (or vacuum) between walls to slow heat from entering the cold contents. Both are barriers to heat transfer, not heat generators.")
    ],
    "stem_intro": "Present the summer fair challenge. Connect to the model: every design decision either increases or decreases heat transfer rate. The winning design minimizes heat flow from the hot air to the ice cream.",
    "stem_concepts": [
        ("Thermal Conductivity", "Different materials transfer heat at different rates. Metal conducts heat quickly (bad for insulation), while foam and air conduct heat slowly (good for insulation)."),
        ("Reflective Surfaces", "Shiny materials like aluminum foil reflect radiant heat away, adding another layer of protection against thermal energy transfer."),
        ("Air Gaps", "Trapped air is one of the best insulators because air molecules are spread far apart and transfer energy slowly.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design uses multiple insulation strategies, explains heat transfer principles, and includes a measurement plan to test effectiveness"),
        ("Proficient (3)", "Design uses at least two insulation methods with scientific reasoning connected to the model"),
        ("Developing (2)", "Design addresses insulation but lacks detail on why chosen materials work"),
        ("Beginning (1)", "Design does not connect material choices to heat transfer principles")
    ],
    "support": [
        "Provide physical materials (foam cups, foil, fabric) so students can feel the temperature difference",
        "Use sentence frames: 'When air temperature increases, heat transfer rate __ because...'",
        "Offer a pre-made observation table for recording melting times across scenarios"
    ],
    "extensions": [
        "Test real insulating materials by timing how long an ice cube lasts in each container",
        "Add Wind Speed as a component and explore how convection affects melting rate",
        "Research how vacuum insulation in thermoses works and connect it to the model"
    ],
    "cross_curr": [
        ("Math", "Graph melting speed vs. air temperature and find the relationship pattern"),
        ("ELA", "Write a persuasive product description for your insulated container design"),
        ("Social Studies", "Research how ancient civilizations stored ice and kept food cold before refrigeration")
    ],
    "misconceptions": [
        ("Cold flows into the ice cream", "Cold is not a substance that flows. Heat (thermal energy) flows FROM the warm air INTO the cold ice cream. The ice cream warms up; the air does not send 'cold' anywhere.", "Hold an ice cube: your hand feels cold, but heat is leaving your hand and entering the ice."),
        ("Insulation adds cold to keep things frozen", "Insulation does not generate cold. It simply slows down heat transfer. A thermos keeps things cold by preventing warm air from reaching the contents, not by adding cold.", "A thermos also keeps hot soup hot — it blocks heat transfer in both directions."),
        ("All materials transfer heat at the same rate", "Different materials have very different thermal conductivities. Metal transfers heat rapidly while foam transfers it slowly. That is why a metal spoon in soup gets hot but a wooden spoon does not.", "Touch a metal desk and a book — the metal feels cooler because it conducts heat away from your hand faster.")
    ]
}

L09 = {
    "id": "G05L2-L09",
    "title": "Can a River Change Direction?",
    "subtitle": "How Flowing Water Reshapes the Land Over Time",
    "ngss": "5-ESS2-1, 5-ESS2-2",
    "ngss_desc": "Develop a model using an example to describe ways the geosphere, hydrosphere, atmosphere, and biosphere interact. Describe and graph the amounts and percentages of water and fresh water in various reservoirs to provide evidence about the distribution of water on Earth.",
    "big_question": "Can a river actually change the direction it flows? What forces make that happen?",
    "objectives": [
        "Model how water flow speed and soil softness affect erosion and sediment transport",
        "Explain how erosion on one bank and deposition on another changes a river's path",
        "Predict how changes in water flow speed affect channel shape over time",
        "Connect river processes to real-world landform changes"
    ],
    "vocabulary": [
        ("Erosion", "The wearing away of rock and soil by water, wind, or ice"),
        ("Sediment", "Small pieces of rock and soil carried by flowing water"),
        ("Deposition", "When flowing water slows down and drops the sediment it was carrying"),
        ("Channel", "The path or bed through which a river flows")
    ],
    "components": [
        ("Water Flow Speed", "How fast the water moves through the river channel", True),
        ("Soil Softness", "How easily the riverbank material can be worn away by water", True),
        ("Erosion Rate", "How quickly the river wears away soil and rock from its banks", False),
        ("Sediment Transport", "How much loose material the river carries as it flows", False),
        ("Channel Shape Change", "How much the river's path shifts over time due to erosion and deposition", False)
    ],
    "think_about_it": "If you run water from a hose over a pile of sand, what happens to the sand? What if you turn the water up higher?",
    "scenarios": [
        ("Fast River, Soft Soil", "Set Water Flow Speed to 90% and Soil Softness to 90%"),
        ("Slow River, Soft Soil", "Set Water Flow Speed to 20% and Soil Softness to 90%"),
        ("Fast River, Hard Rock", "Set Water Flow Speed to 90% and Soil Softness to 10%")
    ],
    "sim_scenarios": [
        ("Fast River, Soft Soil", "Maximum flow speed, very soft soil", "What do you predict will happen to Erosion Rate and Channel Shape Change?"),
        ("Slow River, Soft Soil", "Low flow speed, very soft soil", "What do you predict will happen compared to the fast river scenario?"),
        ("Fast River, Hard Rock", "Maximum flow speed, very hard rock", "What do you predict will happen to Erosion Rate even with fast water?")
    ],
    "discoveries": [
        "Rivers CAN change direction over time through erosion on the outside of bends and deposition on the inside",
        "Faster water erodes more material and carries more sediment, reshaping the channel quickly",
        "Soft soil erodes much faster than hard rock, so rivers change course more easily in soft ground",
        "Channel shape change is a SLOW process — it happens over years, decades, and centuries, not overnight"
    ],
    "answer": "Yes, a river can change direction! Fast-moving water erodes soft soil on the outside of bends, while slower water on the inside deposits sediment. Over time, this makes bends grow larger and the river shifts its path. In very soft soil with fast water, rivers can change course dramatically.",
    "stem_title": "Design a Riverbank Protection Plan",
    "stem_mission": "Design a plan to protect a community's riverbank from erosion without harming the river ecosystem.",
    "stem_scenario": "A riverside community is losing land to erosion. Every year, the river eats away more of the bank, threatening homes and roads. Your team must design a protection plan that slows erosion while keeping the river healthy for fish and wildlife.",
    "stem_questions": [
        "What methods can slow erosion without blocking the river entirely?",
        "How do plants help prevent riverbank erosion?",
        "What happens downstream if you armor one section of riverbank?"
    ],
    "stem_design_qs": [
        "What materials or natural features will you use to slow erosion?",
        "How will you protect the bank without speeding up erosion elsewhere?",
        "How will you ensure fish and wildlife can still use the river?",
        "How will you measure whether your protection plan is working over time?"
    ],
    "career": "Fluvial Geomorphologists and River Engineers study how rivers shape the land and design solutions to protect communities from erosion and flooding. They earn $65,000-$120,000/year.",
    "images": {
        "cover": ("cover-river-direction.png", "A photorealistic, cinematic aerial image of a winding river with dramatic meanders cutting through a green valley, showing visible erosion on outer banks and sediment deposits on inner banks, golden hour lighting, ultra-crisp detail"),
        "landscape": ("landscape-river-direction.png", "A photorealistic image of a Black female student (age 10-11) leading diverse 5th graders including White, Asian, and Latino classmates along a stream bank, pointing at erosion marks in the soil, wearing modern hoodies and sneakers, bright natural light"),
        "modeling": ("modeling-river-direction.png", "A photorealistic image of a White male student (age 10-11) at a laptop building a river erosion model, with Black female, Asian male, and Latina classmates comparing simulation results, modern classroom, natural light"),
        "discussion": ("discussion-river-direction.png", "A photorealistic image of an Asian female teacher using a stream table demonstration while diverse 5th graders including Black, White, and Latino students observe water cutting through sand, classroom science lab, warm lighting"),
        "stem": ("stem-river-direction.png", "A photorealistic image of a Latino female student (age 10-11) presenting a riverbank protection poster while White, Black, and Asian classmates examine model riverbanks, school science room, bright natural light")
    },
    "pre_assessment": [
        "Have you ever seen a place where water wore away the ground? What did it look like?",
        "Do you think rivers have always been in the same place? Why or why not?",
        "Draw what you think happens to a riverbank when water flows past it very quickly.",
        "What do you think 'erosion' means? Where have you seen it happen?"
    ],
    "extend_components": [
        ("Vegetation Cover", "Plant roots hold soil together, reducing erosion even when water flows fast"),
        ("Rainfall Intensity", "Heavy rain adds more water to the river, increasing flow speed and erosion"),
        ("River Slope", "Steeper river channels cause water to flow faster, increasing erosive power")
    ],
    "reflections": [
        "Why do rivers have curves instead of flowing in straight lines?",
        "How is a river like a living thing that changes and grows over time?",
        "What surprised you most about how quickly soft soil erodes?",
        "If you could add one more component to this model, what would it be and why?",
        "How does understanding erosion help communities plan where to build?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model showing how water flow and soil properties control erosion, sediment transport, and channel change."),
        ("Disciplinary Core Idea", "ESS2.A Earth Materials and Systems", "Students model how water interacts with earth materials to reshape landforms through erosion and deposition."),
        ("Crosscutting Concept", "Stability and Change", "Students explore how river systems appear stable but are constantly changing through slow erosion processes.")
    ],
    "cast_items": [
        "Explain how water flow speed affects erosion rate",
        "Predict how a river's path will change based on soil type and water speed",
        "Describe the relationship between erosion and deposition in shaping river channels"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A river flows through an area where one bank is soft clay and the other is solid rock. Over time, which direction will the river shift and why?"),
        ("Constructed Response:", "Explain how a river can change direction over time using the concepts of erosion, sediment transport, and deposition from your model.")
    ],
    "background_intro": "Rivers are powerful agents of change on Earth's surface. Over time, flowing water reshapes the land by eroding material from some areas and depositing it in others. This constant process of erosion and deposition is how rivers carve valleys, create floodplains, and even change their own course.",
    "background_sections": [
        ("Erosion: Water's Sculpting Tool", "Erosion occurs when flowing water has enough energy to dislodge and carry away soil and rock particles. Faster water has more erosive power. On the outside of a river bend, water flows fastest and cuts into the bank."),
        ("Sediment Transport", "Once material is eroded, the river carries it as sediment. Faster water can carry larger and heavier particles. When water slows down — on the inside of a bend or where the river widens — it drops its sediment load in a process called deposition."),
        ("How Rivers Change Course", "Rivers develop curves called meanders because erosion on the outside of bends and deposition on the inside cause bends to grow larger over time. Eventually, a meander can loop so far that the river cuts a new, shorter path, leaving an oxbow lake behind."),
        ("Factors That Control Erosion", "The rate of erosion depends on water speed, soil or rock type, vegetation cover, and slope. Soft soils like clay and sand erode quickly, while hard rock like granite resists erosion for thousands of years.")
    ],
    "lever_L": "Students identify Water Flow Speed, Soil Softness, Erosion Rate, Sediment Transport, and Channel Shape Change as the five system components.",
    "lever_E": "Students determine that Water Flow Speed increases Erosion Rate (+), Soil Softness increases Erosion Rate (+), Erosion Rate increases Sediment Transport (+), Sediment Transport increases Channel Shape Change (+), and Water Flow Speed increases Sediment Transport (+).",
    "lever_V": "Students build the river erosion model showing how external conditions (water speed and soil type) drive internal responses (erosion, transport, channel change).",
    "lever_Ev": "Students run the Fast River, Hard Rock scenario and discover that even fast water erodes slowly through hard rock, then compare with soft soil scenarios to see the dramatic difference.",
    "lever_R": "Students add Vegetation Cover or Rainfall Intensity to explore how plants and weather affect river erosion.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Aerial view of a winding river with dramatic meanders", "say": "Can a river actually change direction? The answer might surprise you.", "do": "Show satellite images of meandering rivers and ask: Has this river always looked like this?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary list", "say": "Today we model how water reshapes the very ground it flows over.", "do": "Students read objectives and share what they think 'erosion' means.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Can a river change direction?", "say": "Rivers seem permanent, but they are constantly moving. How?", "do": "Partner discussion: Have you ever seen evidence of erosion?", "time": "2 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "Our model shows how TWO external factors combine to reshape a river over time.", "do": "Preview: water speed and soil type work together.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Five component cards with descriptions", "say": "Water Flow Speed and Soil Softness are external — we control them. Erosion, sediment, and channel change respond.", "do": "Students sort component cards into external and internal categories.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows with +/- signs", "say": "Notice that ALL relationships here are positive. More speed means more erosion, more erosion means more transport, and more transport means more channel change.", "do": "Guide students to draw all five relationship arrows in ModelIt.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graphs comparing erosion under different conditions", "say": "Fast water in soft soil vs fast water in hard rock — what is the difference? Let's test it.", "do": "Students run all three scenarios and record observations.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings about river erosion and change", "say": "Rivers are not permanent. They are constantly reshaping themselves and the land around them.", "do": "Class discussion: What does this mean for communities near rivers?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Riverbank protection plan", "say": "A community needs your help to save their riverbank. Design a protection plan.", "do": "Groups brainstorm, design, and present their protection strategies.", "time": "10 min"}
    ],
    "sort_reasoning": "Water Flow Speed and Soil Softness are external because they represent environmental conditions that students can adjust. Erosion Rate, Sediment Transport, and Channel Shape Change are internal because they are determined by and respond to the combination of water flow and soil properties.",
    "relationships": [
        ("Water Flow Speed to Erosion Rate", "POSITIVE (+)", "Faster water has more energy to dislodge and carry away soil and rock particles."),
        ("Soil Softness to Erosion Rate", "POSITIVE (+)", "Softer soil is easier for water to break apart and carry away."),
        ("Erosion Rate to Sediment Transport", "POSITIVE (+)", "More erosion produces more loose material for the river to carry."),
        ("Water Flow Speed to Sediment Transport", "POSITIVE (+)", "Faster water can carry more and larger sediment particles."),
        ("Sediment Transport to Channel Shape Change", "POSITIVE (+)", "More sediment being moved and deposited causes greater changes in the river's path and shape.")
    ],
    "sim_answers": [
        ("Fast River, Hard Rock", "Even with Water Flow Speed at 90%, the hard rock (Soil Softness at 10%) keeps Erosion Rate low. Sediment Transport is minimal and Channel Shape Change is very slow. This shows why some rivers have carved the same rocky canyon for millions of years."),
        ("Slow River, Soft Soil", "With Water Flow Speed at only 20%, Erosion Rate is moderate despite soft soil because the water lacks energy. Sediment Transport is low and Channel Shape Change is slow. Water speed matters as much as soil type.")
    ],
    "reflection_exemplars": [
        ("Why do rivers have curves?", "Rivers develop curves because any slight bend causes water to flow faster on the outside and slower on the inside. The fast water erodes the outer bank while the slow water deposits sediment on the inner bank. This makes the bend grow larger, creating meandering curves over time."),
        ("How does understanding erosion help communities?", "Communities near rivers need to know where erosion is likely to occur so they can avoid building in those areas. Understanding that soft soil erodes faster helps planners predict which banks are at risk. Engineers can design protection like riprap or vegetation buffers based on erosion models.")
    ],
    "stem_intro": "Present the community crisis: a riverside neighborhood is losing land to erosion. Show before and after images of riverbank erosion. Connect to the model: every protection strategy works by changing erosion rate, sediment transport, or both.",
    "stem_concepts": [
        ("Riprap and Armor", "Large rocks placed along the bank absorb water energy and resist erosion, essentially making the soil 'harder' in model terms."),
        ("Vegetation Buffers", "Deep-rooted plants hold soil in place and slow water near the bank, reducing both erosion rate and sediment transport."),
        ("Engineered Channels", "Structures like wing dams and deflectors redirect water flow away from vulnerable banks, reducing the flow speed hitting the bank.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan uses multiple strategies, explains erosion science, considers downstream effects, and includes monitoring plan"),
        ("Proficient (3)", "Plan uses at least two strategies with scientific reasoning and one consideration of environmental impact"),
        ("Developing (2)", "Plan addresses erosion but lacks detail on why strategies work or environmental considerations"),
        ("Beginning (1)", "Plan does not connect strategies to erosion science from the model")
    ],
    "support": [
        "Use a stream table or sand tray to physically demonstrate erosion and deposition",
        "Use sentence frames: 'When water flow speed increases, erosion rate __ because...'",
        "Provide before/after satellite images of real river changes for comparison"
    ],
    "extensions": [
        "Research the Mississippi River's historical course changes using old maps",
        "Add Vegetation Cover as a component and explore how plants protect riverbanks",
        "Build a stream table model and test how different bank materials resist erosion"
    ],
    "cross_curr": [
        ("Math", "Calculate how many cubic meters of soil a river removes per year at different erosion rates"),
        ("ELA", "Write a news article about a community dealing with river erosion threatening their neighborhood"),
        ("Social Studies", "Research how the changing course of the Mississippi River has affected cities and state borders")
    ],
    "misconceptions": [
        ("Rivers have always been where they are now", "Rivers constantly change course through erosion and deposition. The Mississippi River has shifted hundreds of miles over thousands of years. Even small streams shift noticeably over decades.", "Compare old maps of a river with current satellite images to see the changes."),
        ("Erosion only happens during floods", "Erosion happens every day as water flows past riverbanks. Floods accelerate erosion dramatically, but normal flow constantly wears away soft material. It is a slow, continuous process.", "Show time-lapse images of riverbank erosion over months or years."),
        ("Rocks and soil are permanent", "Rocks and soil seem permanent because erosion is usually too slow to watch. But given enough time, water can carve through solid rock — that is how the Grand Canyon formed over millions of years.", "The Grand Canyon is a mile deep, carved entirely by the Colorado River.")
    ]
}

L10 = {
    "id": "G05L2-L10",
    "title": "Why Do Some Things Dissolve and Others Don't?",
    "subtitle": "How Water Temperature and Motion Affect Dissolving Speed",
    "ngss": "5-PS1-1, 5-PS1-4",
    "ngss_desc": "Develop a model to describe that matter is made of particles too small to be seen. Conduct an investigation to determine whether the mixing of two or more substances results in new substances.",
    "big_question": "Why do some things dissolve in water quickly while others take forever or don't dissolve at all?",
    "objectives": [
        "Model how water temperature and stirring speed affect dissolving rate",
        "Explain how particle contact rate determines how quickly a substance dissolves",
        "Predict how changing temperature or stirring speed affects solution concentration",
        "Connect particle-level interactions to observable dissolving behavior"
    ],
    "vocabulary": [
        ("Dissolving", "The process of a solid breaking apart and mixing evenly into a liquid"),
        ("Solution", "A mixture where one substance is completely dissolved in another"),
        ("Concentration", "How much dissolved substance is in a given amount of liquid"),
        ("Particles", "The tiny pieces that make up all matter, too small to see")
    ],
    "components": [
        ("Water Temperature", "The temperature of the water used as the solvent", True),
        ("Stirring Speed", "How fast the water is being stirred or agitated", True),
        ("Particle Contact Rate", "How often water particles bump into and interact with the solid particles", False),
        ("Dissolving Speed", "How quickly the solid breaks apart and mixes into the water", False),
        ("Solution Concentration", "How much of the solid has dissolved into the water", False)
    ],
    "think_about_it": "If you put sugar in cold water and sugar in hot water, which one dissolves first? Why do you think that happens?",
    "scenarios": [
        ("Hot Water, Fast Stirring", "Set Water Temperature to 90% and Stirring Speed to 90%"),
        ("Cold Water, No Stirring", "Set Water Temperature to 10% and Stirring Speed to 0%"),
        ("Hot Water, No Stirring", "Set Water Temperature to 90% and Stirring Speed to 0%")
    ],
    "sim_scenarios": [
        ("Hot Water, Fast Stirring", "High temperature, fast stirring", "What do you predict will happen to Dissolving Speed?"),
        ("Cold Water, No Stirring", "Low temperature, no stirring", "What do you predict will happen to Dissolving Speed compared to the hot stirred scenario?"),
        ("Hot Water, No Stirring", "High temperature, no stirring", "What do you predict — does temperature or stirring matter more?")
    ],
    "discoveries": [
        "Hot water dissolves substances faster because its particles move faster and collide with the solid more often",
        "Stirring increases dissolving speed by bringing fresh water particles into contact with the solid surface",
        "BOTH temperature and stirring increase particle contact rate, which is the key to dissolving speed",
        "Solution concentration builds over time as more and more of the solid dissolves into the water"
    ],
    "answer": "Some things dissolve faster because of particle contact rate — how often water particles bump into the solid. Hot water has faster-moving particles that collide more often, and stirring brings fresh water to the solid surface constantly. Both increase the rate at which the solid breaks apart and mixes into the water.",
    "stem_title": "Design the Fastest Dissolving Method",
    "stem_mission": "Design and test the fastest method to completely dissolve a sugar cube in water.",
    "stem_scenario": "A drink company needs to dissolve flavor packets as fast as possible in their factory. They can adjust water temperature, stirring method, and other factors. Your team must find the fastest dissolving method and explain the science behind it.",
    "stem_questions": [
        "Does crushing the sugar cube before dissolving it help? Why or why not?",
        "Is there a maximum amount of sugar that water can dissolve? What happens then?",
        "How would you measure dissolving speed accurately?"
    ],
    "stem_design_qs": [
        "What water temperature will you use and why?",
        "What stirring method will you use (spoon, shaking, blending)?",
        "Will you change the shape or size of the sugar cube? Why?",
        "How will you measure the exact time it takes to fully dissolve?"
    ],
    "career": "Food Scientists and Chemical Engineers design processes for mixing, dissolving, and creating solutions at industrial scale. They use the same principles you modeled today to make medicines, beverages, and materials. They earn $70,000-$125,000/year.",
    "images": {
        "cover": ("cover-dissolving.png", "A photorealistic, cinematic close-up image of a sugar cube dissolving in a clear glass of water, with visible swirls and wisps of dissolved sugar spreading through the water, backlit with warm light, ultra-crisp detail"),
        "landscape": ("landscape-dissolving.png", "A photorealistic image of an Asian female student (age 10-11) stirring a beaker of colored water while diverse 5th graders including Black, White, and Latino classmates observe and take notes, modern science classroom, natural light"),
        "modeling": ("modeling-dissolving.png", "A photorealistic image of a Latino male student (age 10-11) at a laptop building a dissolving model, with White female, Black male, and Asian classmates comparing their simulation predictions, modern classroom, warm lighting"),
        "discussion": ("discussion-dissolving.png", "A photorealistic image of a Black male teacher holding up two beakers — one with clear water and one with a dissolved solution — while diverse 5th graders including White, Asian, and Latina students discuss observations, classroom lab setting"),
        "stem": ("stem-dissolving.png", "A photorealistic image of a White female student (age 10-11) timing a dissolving experiment with a stopwatch while Black, Asian, and Latino classmates test different water temperatures, school science lab, bright natural light")
    },
    "pre_assessment": [
        "What does it mean when something 'dissolves'? Where does the solid go?",
        "If you stir sugar into water, is the sugar still there? How do you know?",
        "Draw what you think is happening to the sugar particles when sugar dissolves in water.",
        "What could you do to make something dissolve faster?"
    ],
    "extend_components": [
        ("Particle Size", "Smaller pieces have more surface area exposed to water, dissolving faster"),
        ("Solvent Amount", "More water can dissolve more substance before reaching saturation"),
        ("Substance Type", "Different substances have different solubilities — salt dissolves but sand does not")
    ],
    "reflections": [
        "When sugar dissolves, does it disappear? How do you know it is still there?",
        "Why does stirring help even if the water temperature stays the same?",
        "What surprised you most about how temperature affected dissolving speed?",
        "If you could add one more component to this model, what would it be and why?",
        "How does understanding dissolving help in cooking, medicine, or manufacturing?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model showing how temperature and stirring affect particle interactions and dissolving."),
        ("Disciplinary Core Idea", "PS1.A Structure and Properties of Matter", "Students model how particle-level interactions explain observable dissolving behavior and solution formation."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify causal relationships between temperature, stirring, particle contact, and dissolving speed.")
    ],
    "cast_items": [
        "Explain how water temperature affects dissolving speed at the particle level",
        "Predict how stirring changes the rate of dissolving",
        "Describe why some conditions produce faster dissolving than others"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student puts identical sugar cubes in two cups of water. Cup A is hot and stirred. Cup B is cold and not stirred. Which sugar cube dissolves first and what is the MAIN reason?"),
        ("Constructed Response:", "Explain why hot, stirred water dissolves sugar faster than cold, still water. Use the concept of particle contact rate from your model in your explanation.")
    ],
    "background_intro": "Dissolving is a physical process where a solid breaks apart into particles so small they spread evenly throughout a liquid, forming a solution. Understanding what controls dissolving speed requires thinking about what happens at the particle level — even though we cannot see individual particles.",
    "background_sections": [
        ("What Happens When Something Dissolves?", "When a solid dissolves, its particles separate from each other and mix evenly among the liquid particles. The solid does not disappear — its particles are still there, just spread out. You can prove this by evaporating the water and finding the solid left behind."),
        ("Temperature and Particle Motion", "In warmer water, particles move faster. These fast-moving water particles collide with the solid surface more often and with more energy, breaking apart the solid particles more quickly. This is why hot water dissolves most substances faster than cold water."),
        ("Stirring and Fresh Contact", "When water is still, dissolved particles accumulate near the solid surface, creating a 'barrier' of already-saturated water. Stirring moves this saturated water away and brings fresh water into contact with the solid, maintaining a high rate of dissolving."),
        ("Saturation: The Dissolving Limit", "Every liquid can only dissolve a certain amount of a substance at a given temperature. When no more can dissolve, the solution is saturated. Warming the water usually increases how much can dissolve, which is why more sugar dissolves in hot tea than iced tea.")
    ],
    "lever_L": "Students identify Water Temperature, Stirring Speed, Particle Contact Rate, Dissolving Speed, and Solution Concentration as the five system components.",
    "lever_E": "Students determine that Water Temperature increases Particle Contact Rate (+), Stirring Speed increases Particle Contact Rate (+), Particle Contact Rate increases Dissolving Speed (+), and Dissolving Speed increases Solution Concentration (+).",
    "lever_V": "Students build the dissolving model showing how external conditions (temperature and stirring) drive particle-level interactions that produce observable dissolving behavior.",
    "lever_Ev": "Students run the Hot Water, No Stirring scenario and compare with the full hot-stirred scenario to isolate the effect of stirring alone, then test cold-no-stirring to see both factors removed.",
    "lever_R": "Students add Particle Size or Substance Type to explore how physical properties of the solid affect dissolving.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Sugar cube dissolving in a glass of water with visible swirls", "say": "You have done this a hundred times — stirred sugar into a drink. But do you know WHY it dissolves?", "do": "Drop a sugar cube into a glass of water in front of the class. Ask: What is happening?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary list", "say": "Today we model the invisible particle collisions that make dissolving happen.", "do": "Students read objectives and discuss: Where does the sugar GO?", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why do some things dissolve faster than others?", "say": "Sugar dissolves. Sand does not. Hot water works faster than cold. Let's figure out why.", "do": "Quick-write: List three things you could do to make sugar dissolve faster.", "time": "2 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "Our model has two external factors that BOTH affect the same internal process — particle contact rate.", "do": "Preview: temperature and stirring both increase particle collisions.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Five component cards with descriptions", "say": "Water Temperature and Stirring Speed are external — we control them. The other three respond.", "do": "Students sort component cards into external and internal categories.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows with +/- signs", "say": "Notice that BOTH external components feed into Particle Contact Rate — it is the bottleneck of the system.", "do": "Guide students to draw all four relationship arrows in ModelIt.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graphs comparing dissolving under different conditions", "say": "Hot and stirred vs cold and still — how big is the difference? Let's race them.", "do": "Students run all three scenarios and record observations.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings about dissolving and particle interactions", "say": "Everything comes down to particle contact. More collisions, faster dissolving.", "do": "Class discussion: Where do you see dissolving in everyday life?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Dissolving speed competition setup", "say": "Design the fastest method to dissolve a sugar cube. Time it. Beat the other teams.", "do": "Groups design methods, test with real materials, and record times.", "time": "10 min"}
    ],
    "sort_reasoning": "Water Temperature and Stirring Speed are external because they represent conditions that students can directly adjust. Particle Contact Rate, Dissolving Speed, and Solution Concentration are internal because they are determined by and respond to the combination of temperature and stirring conditions.",
    "relationships": [
        ("Water Temperature to Particle Contact Rate", "POSITIVE (+)", "Warmer water particles move faster, colliding with the solid surface more frequently."),
        ("Stirring Speed to Particle Contact Rate", "POSITIVE (+)", "Stirring brings fresh water particles into contact with the solid, increasing collision frequency."),
        ("Particle Contact Rate to Dissolving Speed", "POSITIVE (+)", "More frequent particle collisions break apart the solid faster."),
        ("Dissolving Speed to Solution Concentration", "POSITIVE (+)", "Faster dissolving increases the amount of dissolved substance in the water over time.")
    ],
    "sim_answers": [
        ("Cold Water, No Stirring", "With Water Temperature at 10% and Stirring Speed at 0%, Particle Contact Rate is very low. Dissolving Speed is extremely slow. Solution Concentration builds very slowly. The sugar cube sits in the water barely dissolving because particles move slowly and no fresh water reaches the surface."),
        ("Hot Water, No Stirring", "With Water Temperature at 90% but no stirring, Particle Contact Rate is moderate — higher than cold water but lower than the hot-stirred scenario. Dissolving Speed is faster than cold water but noticeably slower than when stirring is added. This isolates the effect of temperature alone.")
    ],
    "reflection_exemplars": [
        ("When sugar dissolves, does it disappear?", "No, the sugar is still there — its particles are just spread out evenly among the water particles. You can prove this because the water tastes sweet, and if you evaporate the water, the sugar remains behind. Dissolving is a physical change, not a chemical one."),
        ("Why does stirring help even at the same temperature?", "When water is still, the water right next to the sugar cube becomes saturated — full of dissolved sugar. Stirring sweeps this saturated water away and replaces it with fresh water that can dissolve more sugar. It is like clearing a path so new water particles can reach the solid surface.")
    ],
    "stem_intro": "Present the drink company challenge. Connect to the model: every factory decision (water temperature, mixing speed, particle size) maps to a component in the model. Faster dissolving means faster production.",
    "stem_concepts": [
        ("Surface Area", "Crushing a sugar cube into powder creates much more surface area for water particles to contact. More surface area means more simultaneous particle collisions, dramatically increasing dissolving speed."),
        ("Saturation Point", "At a given temperature, water can only dissolve a fixed amount of substance. Hot water usually has a higher saturation point, which is why more sugar dissolves in hot tea."),
        ("Industrial Mixing", "Factories use high-speed mixers, heated water, and pre-ground materials to maximize dissolving speed. The same principles from your model operate at industrial scale.")
    ],
    "stem_eval": [
        ("Expert (4)", "Method optimizes multiple factors (temperature, stirring, particle size), explains particle-level reasoning, and includes accurate timing data"),
        ("Proficient (3)", "Method optimizes at least two factors with scientific reasoning connected to the model"),
        ("Developing (2)", "Method addresses one or two factors but lacks particle-level explanation"),
        ("Beginning (1)", "Method does not connect choices to dissolving science from the model")
    ],
    "support": [
        "Provide sugar cubes, warm and cold water, and spoons for hands-on testing alongside the model",
        "Use sentence frames: 'When water temperature increases, particle contact rate __ because...'",
        "Offer a pre-made data table for recording dissolving times under different conditions"
    ],
    "extensions": [
        "Test dissolving speed of different substances (salt, baking soda, sand) and explain the differences",
        "Add Particle Size as a component by crushing sugar cubes and comparing dissolving times",
        "Research how pharmaceutical companies design medicines that dissolve at specific rates in the body"
    ],
    "cross_curr": [
        ("Math", "Graph dissolving time vs. water temperature and find the relationship pattern"),
        ("ELA", "Write a lab report explaining your dissolving experiment with claims, evidence, and reasoning"),
        ("Social Studies", "Research how water purification uses dissolving and filtering to make water safe")
    ],
    "misconceptions": [
        ("Dissolved substances disappear", "When a solid dissolves, it does not vanish. Its particles separate and mix evenly with the water particles. The dissolved substance is still there — the water tastes sweet, weighs more, and the solid reappears if you evaporate the water.", "Dissolve salt in water, then evaporate. The salt crystals reappear, proving they were always there."),
        ("Stirring creates heat that dissolves things", "Stirring does not significantly heat the water. It works by moving fresh, unsaturated water to the solid surface. The mechanical motion replaces the saturated layer near the solid with water that can still dissolve more material.", "Stir cold water — it stays cold, but dissolving speeds up because fresh water reaches the solid."),
        ("Everything dissolves if you stir long enough", "Some substances simply do not dissolve in water regardless of temperature or stirring. Sand, plastic, and oil do not dissolve because their particles are not attracted to water particles. Solubility is a property of the substance itself.", "Compare sugar (dissolves) with sand (does not dissolve) under identical conditions.")
    ]
}
