#!/usr/bin/env python3
"""Multiple choice post-assessment questions for Grade 5 Level 2 ModelIt! Lessons (G05L2-L01 through G05L2-L07)"""

L01_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "In the carbon cycle model, what happens when Sunlight Intensity is locked at 0%?",
            "choices": {
                "A": "Photosynthesis Rate increases because plants use stored energy",
                "B": "CO2 in Atmosphere decreases because decomposition slows down",
                "C": "CO2 in Atmosphere rises because photosynthesis stops but decomposition continues releasing CO2",
                "D": "Soil Carbon Storage increases because plants grow underground"
            },
            "correct": "C",
            "feedback_correct": "Correct! Without sunlight, photosynthesis cannot occur, so no CO2 is being removed from the atmosphere. Meanwhile, decomposition continues releasing stored carbon as CO2, causing atmospheric levels to rise.",
            "feedback_incorrect": "Remember the Sunlight Shutdown scenario. Photosynthesis requires sunlight to pull CO2 from the air. Without sunlight, photosynthesis stops, but decomposers keep breaking down dead matter and releasing CO2. The result is a buildup of CO2 in the atmosphere."
        },
        {
            "question": "What type of relationship exists between Photosynthesis Rate and CO2 in Atmosphere?",
            "choices": {
                "A": "Positive: more photosynthesis adds more CO2 to the air",
                "B": "Negative: more photosynthesis removes CO2 from the air",
                "C": "No relationship: photosynthesis does not affect CO2",
                "D": "Positive: photosynthesis and CO2 always increase together"
            },
            "correct": "B",
            "feedback_correct": "That's right! Photosynthesis absorbs CO2 from the atmosphere and converts it into sugar. Faster photosynthesis means more CO2 is removed. This is a negative relationship.",
            "feedback_incorrect": "Think about what photosynthesis does. Plants take in CO2 and use it to make food. So when photosynthesis speeds up, it pulls more CO2 out of the air, reducing the amount in the atmosphere. That makes it a negative (-) relationship."
        },
        {
            "question": "In the model, when CO2 in Atmosphere is set to 90%, what happens to Photosynthesis Rate and why?",
            "choices": {
                "A": "Photosynthesis Rate drops because too much CO2 poisons plants",
                "B": "Photosynthesis Rate increases because plants have more CO2 raw material to use",
                "C": "Photosynthesis Rate stays the same because plants only need sunlight",
                "D": "Photosynthesis Rate drops to zero because CO2 blocks sunlight"
            },
            "correct": "B",
            "feedback_correct": "Correct! CO2 is a raw material for photosynthesis. When more CO2 is available, plants can photosynthesize faster. This is a positive relationship between CO2 and Photosynthesis Rate, and it creates a negative feedback loop that pulls CO2 back down.",
            "feedback_incorrect": "CO2 is one of the ingredients plants need for photosynthesis. More CO2 gives plants more raw material, so photosynthesis speeds up. This is actually a self-correcting feedback loop: high CO2 drives faster photosynthesis, which pulls CO2 back down."
        },
        {
            "question": "Why is the carbon cycle called a 'cycle' and not a 'chain'?",
            "choices": {
                "A": "Because carbon is destroyed at the end of the process",
                "B": "Because carbon moves in only one direction, from air to soil",
                "C": "Because carbon atoms loop continuously between the atmosphere, plants, soil, and back again",
                "D": "Because the cycle only happens once per year"
            },
            "correct": "C",
            "feedback_correct": "Exactly! Carbon is never created or destroyed. It moves from the atmosphere into plants through photosynthesis, into the soil when organisms die, and back to the atmosphere through decomposition. The same carbon atoms cycle over and over.",
            "feedback_incorrect": "A chain has a beginning and end. A cycle loops back to the start. Carbon atoms move from the air into plants (photosynthesis), from dead plants into the soil, and from the soil back into the air (decomposition). This loop repeats endlessly."
        },
        {
            "question": "A scientist notices that a forest has very little dead organic matter on the ground despite many trees dropping leaves. What does this tell you about the carbon cycle in this forest?",
            "choices": {
                "A": "The trees have stopped producing leaves",
                "B": "Decomposition Rate is very high, breaking down dead matter quickly and releasing carbon back to the atmosphere",
                "C": "The wind blows all the leaves to another forest",
                "D": "Soil Carbon Storage has reached zero and can't hold any more"
            },
            "correct": "B",
            "feedback_correct": "That's right! If trees are dropping leaves but the ground is clear, decomposers must be working very quickly. Warm, moist conditions speed up decomposition, breaking down dead matter and releasing stored carbon as CO2 back into the atmosphere.",
            "feedback_incorrect": "Think about the model. If leaves are falling but not accumulating, something must be breaking them down. Decomposers (bacteria, fungi, worms) are processing the dead matter rapidly, which means the Decomposition Rate is high, and stored carbon is being released back into the atmosphere."
        }
    ]
}

L02_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "In the energy model, what happens to CO2 Emissions when Fossil Fuel Burn Rate is set to 0% and Sunlight Hours are at 80%?",
            "choices": {
                "A": "CO2 Emissions increase because solar panels release CO2",
                "B": "CO2 Emissions stay the same because energy is still being produced",
                "C": "CO2 Emissions drop to near zero because solar energy produces no CO2",
                "D": "CO2 Emissions increase because more energy is needed from backup sources"
            },
            "correct": "C",
            "feedback_correct": "Correct! Solar panels convert sunlight directly into electricity without burning anything. No burning means no CO2 emissions. When fossil fuel use drops to zero, emissions drop to near zero.",
            "feedback_incorrect": "Remember the All Solar scenario. Solar panels generate electricity from sunlight without combustion. Unlike fossil fuels, they release no CO2 during operation. With fossil fuels at 0%, there is nothing producing CO2 emissions."
        },
        {
            "question": "What is the main tradeoff between solar energy and fossil fuel energy revealed by the model?",
            "choices": {
                "A": "Solar energy is more expensive but produces more CO2",
                "B": "Fossil fuels are cleaner but less reliable",
                "C": "Solar energy is clean but depends on sunlight; fossil fuels are reliable but produce CO2 that harms air quality",
                "D": "There is no tradeoff; solar energy is better in every way"
            },
            "correct": "C",
            "feedback_correct": "That's right! The model shows that solar energy produces zero emissions but only works when the sun is shining. Fossil fuels work anytime but release CO2 that reduces air quality. This is the core tradeoff.",
            "feedback_incorrect": "The Cloudy Day Crisis scenario revealed solar energy's weakness: it depends on sunlight. The All Solar scenario showed its strength: zero emissions. Fossil fuels have the opposite pattern: reliable 24/7 but produce CO2 that worsens air quality."
        },
        {
            "question": "What type of relationship exists between Fossil Fuel Burn Rate and Air Quality Index?",
            "choices": {
                "A": "Positive: more fossil fuels improve air quality",
                "B": "No relationship: fossil fuels don't affect air",
                "C": "Negative: burning more fossil fuels releases CO2 and pollutants that reduce air quality",
                "D": "Positive: burning fuels cleans the air by consuming oxygen"
            },
            "correct": "C",
            "feedback_correct": "Correct! Burning fossil fuels releases CO2 and particulate matter into the atmosphere. More burning means more pollution, which lowers the Air Quality Index. This is an indirect negative relationship through CO2 Emissions.",
            "feedback_incorrect": "Trace the chain in the model: Fossil Fuel Burn Rate increases CO2 Emissions (+), and CO2 Emissions decrease Air Quality (-). So more fossil fuel burning leads to worse air quality. The overall effect is negative."
        },
        {
            "question": "During the Cloudy Day Crisis scenario (Sunlight at 10%, Fossil Fuel at 0%), what problem does the model reveal?",
            "choices": {
                "A": "CO2 Emissions spike because clouds trap greenhouse gases",
                "B": "Solar Energy Output crashes and very little total energy is produced",
                "C": "Air Quality drops because clouds contain pollution",
                "D": "Temperature rises because clouds trap heat"
            },
            "correct": "B",
            "feedback_correct": "Correct! With very little sunlight and no fossil fuels, almost no electricity is generated. This reveals the reliability problem of solar-only energy: the community would face blackouts on cloudy days or at night without backup or storage.",
            "feedback_incorrect": "In this scenario, solar panels have almost no sunlight to work with, and fossil fuels are turned off. The result is very low energy output. This shows why a community cannot rely on solar energy alone without energy storage or backup sources."
        },
        {
            "question": "A city switches from 100% fossil fuels to 50% solar and 50% fossil fuels. Based on the model, what would you predict?",
            "choices": {
                "A": "CO2 Emissions would stay the same because total energy hasn't changed",
                "B": "Air Quality would get worse because solar panels create pollution",
                "C": "CO2 Emissions would decrease by about half, and Air Quality would improve",
                "D": "Energy output would double because two sources are better than one"
            },
            "correct": "C",
            "feedback_correct": "That's right! Cutting fossil fuel use in half means roughly half the CO2 emissions. Less CO2 means better air quality. The solar energy fills in the gap without adding any emissions.",
            "feedback_incorrect": "In the model, CO2 Emissions come from fossil fuels only. If you cut fossil fuel use by 50% and replace it with solar (which produces zero CO2), emissions drop by about half. Less CO2 in the air means the Air Quality Index improves."
        }
    ]
}

L03_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "In the water crisis model, what happens during the Drought + Growth scenario (Rainfall at 20%, Population at 80%)?",
            "choices": {
                "A": "Groundwater Level stays stable because the aquifer is deep",
                "B": "Groundwater Level drops rapidly because water usage far exceeds rainfall refill",
                "C": "Water Availability increases because people conserve during droughts",
                "D": "Population decreases automatically to match the water supply"
            },
            "correct": "B",
            "feedback_correct": "Correct! With low rainfall, very little water is being added to the aquifer. But a large population keeps pulling water out at a high rate. Usage far exceeds refill, so groundwater drops rapidly and water availability crashes.",
            "feedback_incorrect": "Remember the simulation: low rainfall means the aquifer gets very little new water. A large population means heavy demand continues. When output exceeds input, groundwater depletes rapidly and water availability plummets."
        },
        {
            "question": "What type of relationship exists between Population Size and Water Availability?",
            "choices": {
                "A": "Positive: more people means more water is available",
                "B": "No relationship: population does not affect water",
                "C": "Negative: more people competing for the same supply reduces water availability per person",
                "D": "Positive: more people build more wells, increasing supply"
            },
            "correct": "C",
            "feedback_correct": "That's right! When more people compete for the same water supply, each person gets less. Population growth strains the system unless rainfall also increases. This is a negative relationship.",
            "feedback_incorrect": "Think about it: if you have 100 gallons of water and 10 people, each gets 10 gallons. If the population grows to 100 people with the same 100 gallons, each only gets 1 gallon. More people sharing the same supply means less for everyone."
        },
        {
            "question": "Why does groundwater recovery take much longer than groundwater depletion?",
            "choices": {
                "A": "Because water evaporates before it can reach the aquifer",
                "B": "Because rainfall seeps into aquifers slowly over time, while pumping can drain them quickly",
                "C": "Because aquifers are destroyed when they run dry and cannot refill",
                "D": "Because rain only falls during summer months"
            },
            "correct": "B",
            "feedback_correct": "Correct! Rainwater must slowly filter through soil and rock to reach underground aquifers, a process that takes years. But pumps can extract water much faster than this natural refill rate. That is why depletion is fast but recovery is slow.",
            "feedback_incorrect": "In the Recovery scenario from the simulation, even when rainfall returned to 60%, groundwater took a long time to rebuild. That is because rain seeps underground slowly through soil and rock layers, while pumps can extract water at a much faster rate."
        },
        {
            "question": "A town's population triples while rainfall stays the same. Based on the model, what is the most likely result?",
            "choices": {
                "A": "Nothing changes because rain provides unlimited water",
                "B": "Water Usage Rate triples, groundwater depletes, and water availability drops sharply",
                "C": "The aquifer automatically expands to meet the demand",
                "D": "Rainfall increases to match the population"
            },
            "correct": "B",
            "feedback_correct": "Exactly! Population has a positive relationship with Water Usage Rate: more people use more water. But Rainfall has not changed, so the aquifer is losing water faster than it gains. Groundwater drops and water availability falls.",
            "feedback_incorrect": "In the model, Population Size drives Water Usage Rate up (positive relationship). If rainfall stays the same, the aquifer receives the same input but has triple the demand. This imbalance depletes groundwater and reduces water availability."
        },
        {
            "question": "Which solution would the model predict is most effective for a town facing both drought and population growth?",
            "choices": {
                "A": "Building more wells to pump water faster",
                "B": "Waiting for the drought to end naturally",
                "C": "Reducing water usage through conservation while exploring new supply sources like water recycling",
                "D": "Moving the town to a location with more rain"
            },
            "correct": "C",
            "feedback_correct": "Correct! The model shows that water availability depends on the balance between input and output. Conservation reduces demand (output), while water recycling increases effective supply (input). Attacking both sides of the balance is the most effective strategy.",
            "feedback_incorrect": "The model shows water availability is a balance between supply and demand. Pumping more wells just drains the aquifer faster. The most effective approach addresses both sides: reduce demand through conservation AND increase supply through recycling or alternative sources."
        }
    ]
}

L04_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "In the phase change model, what happens when Temperature increases from 0% to 100%?",
            "choices": {
                "A": "Solid Amount increases because heat makes molecules pack tighter",
                "B": "Solid Amount decreases, then Liquid Amount increases, then Gas Amount increases as matter changes state",
                "C": "All three amounts increase because heat creates new matter",
                "D": "Nothing changes because temperature does not affect the state of matter"
            },
            "correct": "B",
            "feedback_correct": "Correct! As temperature rises, solid melts into liquid (Solid decreases, Liquid increases). At higher temperatures, liquid evaporates into gas (Liquid decreases, Gas increases). The matter transforms from one state to the next.",
            "feedback_incorrect": "Remember the Heating from Frozen scenario. As you increase temperature, ice melts into water (solid goes down, liquid goes up). Continue heating, and water evaporates into steam (liquid goes down, gas goes up). Each state transitions to the next."
        },
        {
            "question": "What is the most important pattern the model reveals about total mass during phase changes?",
            "choices": {
                "A": "Total mass decreases because gas weighs less than liquid",
                "B": "Total mass increases because heat adds weight to molecules",
                "C": "Solid Amount + Liquid Amount + Gas Amount always equals the same total, proving matter is conserved",
                "D": "Total mass changes unpredictably depending on pressure"
            },
            "correct": "C",
            "feedback_correct": "Exactly! At every point in the simulation, the three amounts always add up to the same total. Matter is not created or destroyed during phase changes. It just moves from one state to another. This is the law of conservation of matter.",
            "feedback_incorrect": "Look at the data from the simulation. Add Solid + Liquid + Gas at any time step. The total is always the same number. No matter appears or disappears. It simply changes form. This proves the law of conservation of matter."
        },
        {
            "question": "What type of relationship exists between Temperature and Gas Amount?",
            "choices": {
                "A": "Negative: higher temperature reduces gas",
                "B": "Positive: higher temperature increases gas as liquid evaporates into vapor",
                "C": "No relationship: temperature only affects solids",
                "D": "Negative: heat pushes gas molecules back into liquid"
            },
            "correct": "B",
            "feedback_correct": "Correct! Higher temperatures give molecules more energy, causing them to break free from liquid form and become gas. More heat means more evaporation, which means more gas. This is a positive relationship.",
            "feedback_incorrect": "Think about what happens when you boil water. Adding heat (increasing temperature) causes liquid water to turn into steam (gas). The more heat you add, the more gas is produced. Temperature and Gas Amount have a positive (+) relationship."
        },
        {
            "question": "You weigh a sealed container of water, then boil it so all the water becomes steam. How does the weight compare?",
            "choices": {
                "A": "It weighs less because steam is lighter than water",
                "B": "It weighs more because heat added energy and weight",
                "C": "It weighs exactly the same because the same matter is inside, just in gas form",
                "D": "It weighs zero because gas has no mass"
            },
            "correct": "C",
            "feedback_correct": "That's right! The sealed container holds the same molecules of water whether they are liquid or steam. No matter entered or left. The mass is identical because matter is conserved during phase changes.",
            "feedback_incorrect": "In a sealed container, no matter can enter or leave. The same water molecules are inside, whether they are liquid or steam. Gas absolutely has mass. Since no matter was added or removed, the weight stays exactly the same."
        },
        {
            "question": "In the model, what happens when Pressure is set to 90%?",
            "choices": {
                "A": "Gas Amount increases because pressure pushes molecules apart",
                "B": "Gas Amount decreases because high pressure compresses gas molecules back toward liquid form",
                "C": "Solid Amount decreases because pressure melts ice",
                "D": "Nothing happens because pressure does not affect states of matter"
            },
            "correct": "B",
            "feedback_correct": "Correct! High pressure squeezes gas molecules closer together, pushing them back into liquid form. This is a negative relationship between Pressure and Gas Amount. Refrigerators and air conditioners use this principle.",
            "feedback_incorrect": "Remember the Pressure Squeeze scenario. When pressure increases, gas molecules are forced closer together, which can convert them back to liquid. This is why Pressure has a negative (-) relationship with Gas Amount. Total mass stays the same."
        }
    ]
}

L05_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "In the food web model, what happens when Secondary Consumers (predators) are removed from the system?",
            "choices": {
                "A": "Primary Consumers decrease because they have no food source",
                "B": "Primary Consumers explode in population, overeat the Producers, and then Producers crash",
                "C": "Producers increase because predators were eating them",
                "D": "Nothing changes because predators are not important to the food web"
            },
            "correct": "B",
            "feedback_correct": "Correct! Without predators controlling their numbers, herbivores (Primary Consumers) overpopulate. They consume Producers faster than plants can regrow, causing a Producer crash. This chain reaction is called a trophic cascade.",
            "feedback_incorrect": "Remember the Remove Predators scenario. Predators keep herbivore populations in check. Without them, herbivores multiply unchecked, eat all the plants, and then starve when plants are gone. This domino effect is called a trophic cascade."
        },
        {
            "question": "What happens in the model when Producer Population is locked at 0%?",
            "choices": {
                "A": "Primary Consumers switch to eating decomposers",
                "B": "Secondary Consumers increase because there is less competition",
                "C": "The entire food web collapses because no energy enters the system",
                "D": "Decomposer Activity increases to replace the producers"
            },
            "correct": "C",
            "feedback_correct": "Exactly! Producers are the foundation of the food web. They capture sunlight energy and make it available to all other organisms. Without producers, primary consumers starve, then secondary consumers starve, and the entire ecosystem collapses.",
            "feedback_incorrect": "Producers (plants) are the only organisms that convert sunlight into food energy. They are the base of the entire food web. Without them, herbivores have no food, predators have no prey, and the whole system falls apart."
        },
        {
            "question": "What role do decomposers play in completing the food web cycle?",
            "choices": {
                "A": "They eat producers and compete with primary consumers",
                "B": "They break down dead organisms and release nutrients back into the soil for producers to use",
                "C": "They create new energy from sunlight like producers do",
                "D": "They have no connection to the rest of the food web"
            },
            "correct": "B",
            "feedback_correct": "That's right! Decomposers break down dead plants and animals, releasing nutrients into the soil. Producers then absorb those nutrients to grow. This closes the loop, making the food web a true cycle rather than a dead end.",
            "feedback_incorrect": "In the model, Decomposer Activity has a positive relationship with Available Nutrients, and Available Nutrients has a positive relationship with Producer Population. Decomposers recycle dead matter back into nutrients that producers need to grow."
        },
        {
            "question": "In a grassland, wolves eat rabbits and rabbits eat grass. If wolves are removed, what happens first?",
            "choices": {
                "A": "Grass grows faster because wolves were eating it",
                "B": "Rabbit population increases rapidly because nothing is eating them",
                "C": "Rabbit population decreases because wolves protected them",
                "D": "Nothing changes because wolves only eat other predators"
            },
            "correct": "B",
            "feedback_correct": "Correct! Wolves are the secondary consumers that control rabbit (primary consumer) populations. Removing wolves means rabbits face no predation, so their population explodes. Eventually, the overabundant rabbits would overgraze the grass.",
            "feedback_incorrect": "Wolves eat rabbits, keeping their population in check. When wolves are removed, rabbits no longer have a predator. Without that control, rabbit numbers grow rapidly. This is the first step in a trophic cascade."
        },
        {
            "question": "Why do ecologists say 'everything is connected' in an ecosystem?",
            "choices": {
                "A": "Because all organisms live in the same area",
                "B": "Because changing one species population causes cascading effects on every other species through the food web",
                "C": "Because all animals eat the same food",
                "D": "Because all species were created at the same time"
            },
            "correct": "B",
            "feedback_correct": "Exactly! The model demonstrates that removing or changing one component affects every other component through their relationships. Producers support consumers, consumers control each other, and decomposers recycle nutrients for producers. Every connection matters.",
            "feedback_incorrect": "The simulation showed that removing just one species (predators or producers) caused changes that rippled through the entire food web. Each organism is connected to others through feeding relationships, and changing one population shifts all the others."
        }
    ]
}

L06_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "In the Earth systems model, what happens when Volcanic Activity is set to 90%?",
            "choices": {
                "A": "Global Temperature drops because volcanic ash blocks sunlight",
                "B": "Atmospheric CO2 spikes, which causes Global Temperature to rise",
                "C": "Ocean Absorption stops because volcanoes heat the water",
                "D": "Vegetation Growth drops to zero because lava destroys all plants"
            },
            "correct": "B",
            "feedback_correct": "Correct! Volcanic eruptions release massive amounts of CO2 into the atmosphere. CO2 is a greenhouse gas that traps heat, so more CO2 leads to higher global temperatures. The model shows this positive chain: Volcanic Activity increases CO2, and CO2 increases Temperature.",
            "feedback_incorrect": "In the Massive Eruption scenario, volcanoes release large amounts of CO2 into the atmosphere. CO2 traps heat (the greenhouse effect), which raises global temperature. Follow the chain: Volcanic Activity (+) CO2 (+) Temperature."
        },
        {
            "question": "What is a 'negative feedback loop' in the Earth systems model?",
            "choices": {
                "A": "A loop where one change causes more of the same change in an endless spiral",
                "B": "A response that counteracts a change, pushing the system back toward balance",
                "C": "A negative outcome that harms the environment permanently",
                "D": "A loop that only occurs during volcanic eruptions"
            },
            "correct": "B",
            "feedback_correct": "That's right! A negative feedback loop works against a change. When CO2 rises, vegetation grows faster and absorbs more CO2, partially reducing the increase. The response pushes back against the original change, helping stabilize the system.",
            "feedback_incorrect": "In the model, when CO2 rises, two things push back: vegetation grows faster and absorbs CO2 (reducing it), and oceans absorb more CO2 (also reducing it). These responses counteract the original increase. That is negative feedback: the system fights back toward balance."
        },
        {
            "question": "How does Vegetation Growth create a negative feedback loop with Atmospheric CO2?",
            "choices": {
                "A": "More vegetation releases more CO2 through photosynthesis",
                "B": "When CO2 rises, plants grow faster and absorb more CO2 through photosynthesis, pulling CO2 back down",
                "C": "Vegetation blocks volcanic eruptions from releasing CO2",
                "D": "Plants die when CO2 increases, which removes plant matter from the system"
            },
            "correct": "B",
            "feedback_correct": "Correct! Rising CO2 stimulates plant growth because CO2 is a raw material for photosynthesis. As plants grow faster, they absorb more CO2, reducing atmospheric levels. This loop counteracts the original CO2 increase, which is why it is called negative feedback.",
            "feedback_incorrect": "Follow the loop: CO2 rises, which provides more raw material for photosynthesis. Plants grow faster, absorbing more CO2. This reduces atmospheric CO2, counteracting the original increase. The system partially corrects itself through this negative feedback."
        },
        {
            "question": "In the Self-Regulation scenario (Volcanic Activity at 60%), what does the model demonstrate about Earth's climate?",
            "choices": {
                "A": "Earth's temperature spirals out of control with any volcanic activity",
                "B": "Vegetation and ocean absorption fully cancel out all volcanic CO2",
                "C": "The system reaches a new, higher equilibrium because feedback loops partially counteract the CO2 input",
                "D": "Earth's temperature is completely unaffected by volcanic eruptions"
            },
            "correct": "C",
            "feedback_correct": "Exactly! At moderate volcanic activity, CO2 and temperature rise, but vegetation and ocean absorption increase enough to partially offset the input. The system stabilizes at a new, slightly higher level rather than spiraling out of control. This shows Earth's self-regulating ability.",
            "feedback_incorrect": "The Self-Regulation scenario showed that feedback loops (vegetation and ocean absorption) cannot fully cancel out volcanic CO2, but they significantly slow and limit the increase. The system finds a new balance point. This is how Earth has regulated its climate for millions of years."
        },
        {
            "question": "How can a volcanic eruption in Asia affect the climate in North America?",
            "choices": {
                "A": "It cannot; volcanic effects stay in the local area only",
                "B": "Volcanic gases and CO2 spread through the atmosphere globally, affecting temperature and weather patterns worldwide",
                "C": "The eruption sends lava across the ocean to other continents",
                "D": "Ash falls only on nearby countries and does not travel far"
            },
            "correct": "B",
            "feedback_correct": "Correct! Volcanic gases and CO2 enter the atmosphere and can circle the entire globe within weeks. The greenhouse effect from added CO2 warms the whole planet, not just the area near the volcano. This is how Earth's spheres interact globally.",
            "feedback_incorrect": "The atmosphere does not have walls between continents. CO2 and volcanic gases mix throughout the global atmosphere. Increased atmospheric CO2 traps heat everywhere, raising global temperatures. The eruption of Mount Pinatubo in 1991 affected global weather for years."
        }
    ]
}

L07_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "In the starlight model, a star with high Actual Brightness is placed at 90% Distance from Earth. What does the model predict for Apparent Brightness?",
            "choices": {
                "A": "Apparent Brightness is very high because the star is very bright",
                "B": "Apparent Brightness is low because distance greatly reduces how bright the star looks from Earth",
                "C": "Apparent Brightness equals Actual Brightness because distance does not matter",
                "D": "Apparent Brightness is zero because distant stars are invisible"
            },
            "correct": "B",
            "feedback_correct": "Correct! Even a very bright star looks dim when it is extremely far away. Distance has a powerful negative effect on apparent brightness. The model shows that what we see (apparent brightness) depends on both luminosity and distance.",
            "feedback_incorrect": "Remember the Distant Giant scenario. A star can produce enormous amounts of light, but if it is very far away, that light spreads out and weakens before reaching us. Distance has a strong negative relationship with Apparent Brightness."
        },
        {
            "question": "Star A has low Actual Brightness but is very close to Earth. Star B has very high Actual Brightness but is very far away. Which star looks brighter from Earth?",
            "choices": {
                "A": "Star B always looks brighter because it produces more light",
                "B": "They always look the same because brightness and distance cancel out",
                "C": "Star A could look brighter than Star B because proximity can outweigh luminosity",
                "D": "Neither star is visible from Earth"
            },
            "correct": "C",
            "feedback_correct": "That's right! This is the key insight from the model. A close, dim star can appear brighter than a distant, powerful star. Our sun is much less luminous than many stars but appears brightest because it is closest. Apparent brightness depends on both factors.",
            "feedback_incorrect": "The Side-by-Side scenario demonstrated this. A nearby dim star can outshine a distant giant because closeness amplifies apparent brightness while distance diminishes it. Our own sun is a perfect example: it is a medium-brightness star that looks brightest because it is closest."
        },
        {
            "question": "What type of relationship exists between Distance from Earth and Apparent Brightness?",
            "choices": {
                "A": "Positive: farther stars look brighter",
                "B": "No relationship: distance does not affect how bright stars appear",
                "C": "Negative: greater distance means the star looks dimmer from Earth",
                "D": "Positive: distance magnifies starlight like a lens"
            },
            "correct": "C",
            "feedback_correct": "Correct! As distance increases, apparent brightness decreases. Light spreads out in all directions as it travels, so the farther away a star is, the less light reaches our eyes. This is a negative (-) relationship.",
            "feedback_incorrect": "Think about the flashlight analogy. A flashlight looks very bright up close but dim from far away. The flashlight did not change; the distance changed how bright it appears. Greater distance means lower apparent brightness. This is a negative relationship."
        },
        {
            "question": "The sun appears brighter than Betelgeuse from Earth, even though Betelgeuse is about 100,000 times more luminous. What does the model tell us about why?",
            "choices": {
                "A": "Betelgeuse's light is blocked by dust clouds",
                "B": "The sun is 93 million miles away while Betelgeuse is about 700 light-years away, and distance dramatically reduces apparent brightness",
                "C": "The sun is actually more powerful than Betelgeuse",
                "D": "Betelgeuse is not a real star"
            },
            "correct": "B",
            "feedback_correct": "Exactly! Even though Betelgeuse produces vastly more light, it is enormously farther away. The sun's proximity more than compensates for its lower luminosity. Distance is such a powerful factor that it can make a dim star outshine a giant.",
            "feedback_incorrect": "Apparent brightness depends on both actual brightness AND distance. Betelgeuse is 100,000 times more luminous, but it is also roughly 700 light-years away compared to the sun's 93 million miles. At that distance, even enormous luminosity appears dim."
        },
        {
            "question": "When we look at a star that is 500 light-years away, what are we actually seeing?",
            "choices": {
                "A": "The star as it is right now, in real time",
                "B": "The star as it was 500 years ago, because its light took 500 years to reach us",
                "C": "A prediction of what the star will look like in 500 years",
                "D": "An illusion because stars are too far away to see"
            },
            "correct": "B",
            "feedback_correct": "Correct! Light travels at a finite speed. A star 500 light-years away means its light took 500 years to reach Earth. We are seeing that star as it existed 500 years in the past. The farther away a star is, the further back in time we are looking.",
            "feedback_incorrect": "Light does not arrive instantly. A light-year is the distance light travels in one year. If a star is 500 light-years away, its light took 500 years to reach us. We are looking 500 years into the past. This is why the model includes Light Travel Time as a component."
        }
    ]
}

# Aggregate all questions
ALL_QUESTIONS = {
    "G05L2-L01": L01_QUESTIONS,
    "G05L2-L02": L02_QUESTIONS,
    "G05L2-L03": L03_QUESTIONS,
    "G05L2-L04": L04_QUESTIONS,
    "G05L2-L05": L05_QUESTIONS,
    "G05L2-L06": L06_QUESTIONS,
    "G05L2-L07": L07_QUESTIONS,
}

if __name__ == "__main__":
    total_q = 0
    for lesson_id, questions in ALL_QUESTIONS.items():
        post_count = len(questions["mc_post_assessment"])
        total_q += post_count
        print(f"  {lesson_id}: {post_count} post-assessment questions")
    print(f"\n  Total: {total_q} questions across {len(ALL_QUESTIONS)} lessons")
