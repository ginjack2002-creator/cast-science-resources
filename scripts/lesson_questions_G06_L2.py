#!/usr/bin/env python3
"""Multiple choice post-assessment questions for Grade 6 Level 2 ModelIt! Lessons"""

L01_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "In a grassland food web, producers capture 10,000 kJ of solar energy. Using the 10% energy transfer rule, how much energy is available to secondary consumers?",
            "choices": {
                "A": "5,000 kJ because half the energy transfers to each level",
                "B": "1,000 kJ because only 10% reaches secondary consumers",
                "C": "100 kJ because only 10% transfers at each step, and secondary consumers are two steps above producers",
                "D": "10 kJ because energy is divided equally among all four trophic levels"
            },
            "correct": "C",
            "feedback_correct": "Correct! Producers capture 10,000 kJ. Primary consumers get 10% of that (1,000 kJ). Secondary consumers get 10% of the primary consumers' energy (100 kJ). Each trophic level retains only 10% of the energy from the level below.",
            "feedback_incorrect": "Not quite. The 10% rule means each trophic level passes only 10% of its energy to the next. Producers (10,000 kJ) pass 1,000 kJ to primary consumers, who pass 100 kJ to secondary consumers. Two transfers at 10% each means secondary consumers get 1% of the original energy."
        },
        {
            "question": "In the food web model, what happens when secondary consumers are removed from the ecosystem?",
            "choices": {
                "A": "Primary consumer biomass decreases because they lose their food source",
                "B": "Primary consumer biomass increases because nothing is eating them, which then causes producer biomass to crash from overgrazing",
                "C": "Producer biomass increases because more sunlight reaches the ground",
                "D": "Nothing changes because secondary consumers do not affect lower trophic levels"
            },
            "correct": "B",
            "feedback_correct": "Correct! This is a top-down trophic cascade. Without predators, herbivore populations explode. The unchecked herbivores then overgraze the producers, causing producer biomass to crash. Removing predators destabilizes the entire web.",
            "feedback_incorrect": "Not quite. When predators are removed, herbivores are no longer being eaten, so their population surges. These extra herbivores consume far more plants than the ecosystem can sustain, causing producer biomass to crash. This is called a top-down trophic cascade."
        },
        {
            "question": "Which statement best explains why energy flows through an ecosystem but does not cycle?",
            "choices": {
                "A": "Predators at the top of the food web absorb all the energy so none is left to cycle",
                "B": "Energy is converted to heat at every trophic level through metabolism, and heat radiates away and cannot be recaptured by organisms",
                "C": "Plants can only capture energy once, so it cannot be reused",
                "D": "Decomposers destroy the remaining energy when they break down dead organisms"
            },
            "correct": "B",
            "feedback_correct": "Correct! At every trophic level, organisms use energy for metabolism (breathing, moving, maintaining body heat), and that energy is released as heat. Heat energy disperses into the environment and cannot be recaptured by living organisms, so new solar energy must constantly enter the system.",
            "feedback_incorrect": "Not quite. Energy does not cycle because every organism converts usable chemical energy into heat through metabolic processes. This heat radiates away and is no longer available to power life. That is why ecosystems need a constant input of new solar energy through producers."
        },
        {
            "question": "A marine biologist notices that removing sea otters from a kelp forest causes the kelp to disappear. Which explanation is supported by the food web model?",
            "choices": {
                "A": "Sea otters were protecting the kelp from storms",
                "B": "Without otters eating sea urchins, urchin populations exploded and devoured the kelp",
                "C": "Sea otters were fertilizing the kelp with their waste",
                "D": "The kelp died because it needed the shade from sea otter fur"
            },
            "correct": "B",
            "feedback_correct": "Correct! This is a real trophic cascade. Sea otters are secondary consumers that eat sea urchins (primary consumers). Without otters controlling urchin populations, urchins multiply and overgraze the kelp (producers), destroying the entire kelp forest ecosystem.",
            "feedback_incorrect": "Not quite. This is a classic trophic cascade. Sea otters eat sea urchins, keeping urchin numbers low. Without otters, urchin populations explode and consume all the kelp. The food web model predicts this: removing a predator causes herbivore populations to surge and producers to decline."
        },
        {
            "question": "Why are decomposers essential to ecosystem survival even though they are not part of the energy pyramid?",
            "choices": {
                "A": "Decomposers create new energy from dead organisms",
                "B": "Decomposers recycle nutrients locked in dead matter back into the soil so producers can use them to grow",
                "C": "Decomposers eat predators and keep the food web balanced",
                "D": "Decomposers convert heat energy back into chemical energy for producers"
            },
            "correct": "B",
            "feedback_correct": "Correct! While energy flows one way and cannot be recycled, matter CAN cycle. Decomposers break down dead organisms and return essential nutrients (nitrogen, phosphorus, minerals) to the soil. Without decomposers, these nutrients would be permanently locked in dead matter and producers would run out of raw materials.",
            "feedback_incorrect": "Not quite. Decomposers do not create energy or recycle energy. Their critical role is recycling MATTER. They break down dead organisms and waste, releasing nutrients like nitrogen and phosphorus back into the soil. Producers need these nutrients to grow. Without decomposers, the matter cycle would stop and ecosystems would collapse."
        }
    ]
}

L02_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "A cup of hot chocolate at 85 degrees C is placed in a 20 degrees C room. After 10 minutes, the temperature is 50 degrees C. After 20 more minutes, the temperature is 28 degrees C. What explains this pattern?",
            "choices": {
                "A": "The drink cooled at a constant rate of about 2 degrees per minute",
                "B": "The drink cooled faster at first because the large temperature difference drove rapid heat transfer, then slowed as the gap shrank",
                "C": "The room temperature increased, slowing the cooling",
                "D": "The cup absorbed heat from the room after 10 minutes"
            },
            "correct": "B",
            "feedback_correct": "Correct! This is Newton's Law of Cooling in action. The initial 65-degree gap drove fast cooling (35 degrees in 10 minutes). As the gap shrank to 30 degrees, the transfer rate slowed (only 22 degrees in 20 minutes). The driving force for heat transfer weakens as the temperatures converge.",
            "feedback_incorrect": "Not quite. The cooling was NOT constant. It was fast at first (35 degrees lost in 10 minutes) and slower later (22 degrees lost in 20 minutes). This exponential decay happens because the rate of heat transfer is proportional to the temperature difference. As the gap between object and room shrinks, the transfer slows down."
        },
        {
            "question": "In the thermal energy model, why can the hot object never cool below room temperature?",
            "choices": {
                "A": "The container insulates the object and prevents further cooling",
                "B": "At room temperature, the temperature difference is zero, so there is no driving force for further heat transfer",
                "C": "The object generates its own heat to maintain room temperature",
                "D": "Cold air rises away from the object, stopping the cooling process"
            },
            "correct": "B",
            "feedback_correct": "Correct! Heat transfer requires a temperature difference to drive it. When the object reaches room temperature, the difference is zero and the transfer rate drops to zero. With no driving force, no more heat can flow. This is thermal equilibrium.",
            "feedback_incorrect": "Not quite. The key principle is that temperature difference drives heat transfer. When the object equals the room temperature, the temperature difference is zero. Zero difference means zero transfer rate. There is simply no force pushing heat in any direction. To cool below room temperature would require active refrigeration."
        },
        {
            "question": "Two identical cups of 90 degrees C water are placed in different rooms. Cup A is in a 10 degrees C room and Cup B is in a 30 degrees C room. After 15 minutes, which statement is true?",
            "choices": {
                "A": "Both cups lost the same amount of heat because they started at the same temperature",
                "B": "Cup A lost more heat because the larger temperature difference drove faster transfer",
                "C": "Cup B lost more heat because the warmer room contains more thermal energy",
                "D": "Neither cup lost heat because 15 minutes is too short for significant cooling"
            },
            "correct": "B",
            "feedback_correct": "Correct! Cup A has a temperature difference of 80 degrees (90 minus 10) while Cup B has only 60 degrees (90 minus 30). The larger difference drives faster heat transfer, so Cup A cools more quickly and loses more thermal energy in the same time period.",
            "feedback_incorrect": "Not quite. The rate of heat transfer depends on the temperature difference, not just the starting temperature. Cup A has an 80-degree gap with its room, while Cup B has only a 60-degree gap. Since a larger gap drives faster transfer, Cup A loses heat more rapidly."
        },
        {
            "question": "Which graph shape correctly represents how a hot object's temperature changes over time as it cools toward room temperature?",
            "choices": {
                "A": "A straight line dropping at a constant rate to room temperature",
                "B": "A curve that drops steeply at first, then gradually flattens as it approaches room temperature",
                "C": "A curve that drops slowly at first, then accelerates as it approaches room temperature",
                "D": "A zigzag line that goes up and down randomly"
            },
            "correct": "B",
            "feedback_correct": "Correct! The cooling curve is an exponential decay. It drops steeply when the temperature difference is large (driving fast transfer), then flattens as the difference shrinks and transfer slows. The curve approaches but never quite reaches room temperature.",
            "feedback_incorrect": "Not quite. Cooling does not happen at a constant rate. The curve starts steep (fast cooling when the gap is large) and gradually flattens (slow cooling as the gap shrinks). This exponential decay shape is one of the most common patterns in physics."
        },
        {
            "question": "A thermos keeps coffee hot for hours while a metal cup lets coffee cool in minutes. Based on the thermal energy model, what does the thermos change?",
            "choices": {
                "A": "The thermos raises the room temperature around the coffee",
                "B": "The thermos eliminates the temperature difference between the coffee and the room",
                "C": "The thermos slows the transfer rate by reducing how quickly heat can flow through the container walls",
                "D": "The thermos creates new heat energy to replace what is lost"
            },
            "correct": "C",
            "feedback_correct": "Correct! A thermos does not change the temperature difference or create heat. It adds insulation that dramatically slows the RATE at which heat transfers through the walls. The same driving force (temperature difference) is present, but the transfer rate is reduced by the insulating layers.",
            "feedback_incorrect": "Not quite. The temperature difference is the same whether coffee is in a thermos or a metal cup. What changes is the transfer rate. The thermos uses insulation (vacuum, reflective layers) to slow how fast heat can flow from the hot coffee to the cooler surroundings, keeping the coffee hot much longer."
        }
    ]
}

L03_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "Why do convergent plate boundaries produce volcanoes but transform boundaries do not?",
            "choices": {
                "A": "Transform boundaries are not hot enough to melt rock",
                "B": "At convergent boundaries, one plate subducts into the mantle and melts, creating magma that rises as volcanoes. Transform boundaries have no subduction.",
                "C": "Volcanoes only form near oceans, and transform boundaries are always inland",
                "D": "Transform boundaries move too slowly to generate enough heat for volcanoes"
            },
            "correct": "B",
            "feedback_correct": "Correct! At convergent boundaries, one plate dives beneath the other (subduction) into the hot mantle, where it partially melts. This magma rises through the overlying plate and erupts as volcanoes. At transform boundaries, plates slide horizontally past each other with no subduction, so no melting occurs and no magma is produced.",
            "feedback_incorrect": "Not quite. The key difference is subduction. At convergent boundaries, one plate plunges into the mantle and melts, producing magma that feeds volcanoes. At transform boundaries, plates slide sideways past each other without either plate going down into the mantle. No subduction means no melting and no volcanoes."
        },
        {
            "question": "In the plate tectonics model, tectonic stress builds and then drops repeatedly. What creates this cyclical pattern?",
            "choices": {
                "A": "The Sun's gravity periodically pulls on the plates, releasing stress",
                "B": "Mantle convection speeds up and slows down on a regular schedule",
                "C": "Earthquakes release accumulated stress (negative feedback), then convection rebuilds the stress, creating a repeating cycle",
                "D": "Volcanic eruptions reset the stress to zero every few years"
            },
            "correct": "C",
            "feedback_correct": "Correct! This is a negative feedback cycle. Mantle convection continuously pushes plates, building stress at boundaries. When stress exceeds the friction holding plates together, an earthquake releases that stored energy. Stress drops, then gradually rebuilds as convection continues pushing. This creates the cyclical build-release pattern.",
            "feedback_incorrect": "Not quite. The cycle works through negative feedback. Convection pushes plates together, building stress. When stress overcomes friction, an earthquake releases the energy and stress drops. Then convection begins rebuilding stress again. This repeating pattern of accumulation and release is why earthquakes recur at the same locations."
        },
        {
            "question": "A region on a plate boundary has not experienced an earthquake in 200 years, while a nearby boundary has frequent small earthquakes. Which region poses a greater risk of a large earthquake?",
            "choices": {
                "A": "The region with frequent earthquakes, because it is clearly more active",
                "B": "Neither region, because earthquakes are completely random",
                "C": "The quiet region, because 200 years of stress accumulation without release means enormous energy is stored",
                "D": "Both regions have exactly equal risk at all times"
            },
            "correct": "C",
            "feedback_correct": "Correct! The quiet region has been accumulating stress for 200 years without release. The model shows that longer periods without earthquakes mean more stored energy, which means a potentially larger earthquake when the fault finally slips. The region with frequent small quakes is regularly releasing small amounts of stress.",
            "feedback_incorrect": "Not quite. The tectonic stress model shows that stress builds continuously at plate boundaries. A 200-year quiet period means enormous stress has accumulated without release. When the fault finally fails, all that stored energy releases at once as a potentially devastating earthquake. Frequent small quakes actually reduce risk by releasing stress incrementally."
        },
        {
            "question": "How does increasing mantle convection speed affect geological activity at a plate boundary?",
            "choices": {
                "A": "Faster convection has no effect on surface activity because the mantle is too deep",
                "B": "Faster convection cools the plates, reducing both earthquakes and volcanoes",
                "C": "Faster convection pushes plates harder, building stress faster and increasing earthquake frequency and volcanic activity",
                "D": "Faster convection only affects divergent boundaries, not convergent or transform ones"
            },
            "correct": "C",
            "feedback_correct": "Correct! Faster mantle convection drives plates together (or apart, or past each other) with more force. This builds tectonic stress more rapidly, leading to more frequent earthquakes. At convergent boundaries, faster convection also increases heat delivery and magma production, intensifying volcanic activity.",
            "feedback_incorrect": "Not quite. Mantle convection is the engine driving all plate movement. Faster convection means plates are pushed with more force, which builds stress at boundaries more quickly. More stress accumulation leads to more frequent earthquakes. At convergent boundaries, faster convection also increases magma production and volcanic activity."
        },
        {
            "question": "Scientists know California will have a major earthquake, but they cannot predict the exact date. What does the plate tectonics model reveal about why precise timing is impossible?",
            "choices": {
                "A": "Scientists do not have enough instruments to measure plate movement",
                "B": "The exact moment when accumulated stress overcomes rock friction depends on countless microscopic variables that are impossible to measure",
                "C": "Earthquakes happen randomly and follow no patterns at all",
                "D": "Plate tectonics theory is still unproven and may be wrong about California"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model shows that the stress-release pattern is predictable on average, but the exact moment of failure depends on microscopic conditions in the rock: tiny fractures, water content, mineral composition, and temperature variations. It is like knowing a fraying rope will break but not being able to predict which fiber fails first.",
            "feedback_incorrect": "Not quite. Earthquakes are NOT random. They follow predictable patterns at known plate boundaries. The challenge is that while we can predict WHERE and approximately how OFTEN, the precise timing depends on microscopic conditions in the rock that are impossible to measure. The system is deterministic in principle but chaotic in practice."
        }
    ]
}

L04_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "In the cell model, what happens when oxygen availability is locked at 10% while nutrients remain normal?",
            "choices": {
                "A": "The cell functions normally because nutrients alone provide enough energy",
                "B": "Mitochondria activity drops dramatically because oxygen is required for efficient ATP production, causing cell growth to crash",
                "C": "The cell switches to using a different organelle for energy production",
                "D": "Waste production increases because the cell works harder without oxygen"
            },
            "correct": "B",
            "feedback_correct": "Correct! Mitochondria need BOTH glucose and oxygen for cellular respiration. Without oxygen, the electron transport chain cannot function, and ATP production drops by approximately 95%. With almost no energy, the cell cannot grow, repair, or maintain itself. This is why oxygen deprivation kills cells within minutes.",
            "feedback_incorrect": "Not quite. Mitochondria require both glucose AND oxygen to produce ATP efficiently. Without oxygen, ATP production falls by about 95% because the electron transport chain shuts down. The cell rapidly loses energy for growth and maintenance. This is why choking is a medical emergency."
        },
        {
            "question": "Why does waste production increase when mitochondria activity increases?",
            "choices": {
                "A": "Mitochondria malfunction at high activity levels and produce extra waste",
                "B": "Carbon dioxide and water are natural byproducts of cellular respiration, so more respiration produces more waste",
                "C": "High mitochondria activity causes the cell membrane to leak, letting waste in from outside",
                "D": "Waste production is random and not related to mitochondria activity"
            },
            "correct": "B",
            "feedback_correct": "Correct! Cellular respiration converts glucose and oxygen into ATP, carbon dioxide, and water. CO2 is an unavoidable byproduct. More mitochondria activity means more glucose is being burned, which produces more CO2 waste. This is a positive relationship built into the chemistry of respiration.",
            "feedback_incorrect": "Not quite. The chemical equation for cellular respiration shows that CO2 and water are inherent products: glucose + oxygen yields ATP + CO2 + water. More active mitochondria are running more of these reactions, so more CO2 waste is produced. It is not a malfunction; it is fundamental chemistry."
        },
        {
            "question": "A student observes that oxygen deprivation kills cells in minutes, but nutrient starvation takes days or weeks. What does the cell model reveal about this difference?",
            "choices": {
                "A": "Cells do not actually need nutrients, only oxygen",
                "B": "Oxygen is used faster than nutrients because cells breathe more than they eat",
                "C": "Without oxygen, ATP production drops by 95% immediately. Without nutrients, cells can slowly burn stored reserves like glycogen and fat, declining more gradually.",
                "D": "The difference is due to temperature, not the inputs themselves"
            },
            "correct": "C",
            "feedback_correct": "Correct! Oxygen deprivation is immediately catastrophic because the electron transport chain cannot function, cutting ATP output by 95%. Nutrient deprivation is more gradual because cells have stored energy reserves (glycogen, fat) they can break down for glucose. The decline is real but slower because reserves buy time.",
            "feedback_incorrect": "Not quite. The critical difference is in backup options. Without oxygen, there is no alternative for efficient ATP production, so energy output crashes immediately. Without nutrients, cells can burn stored glycogen and fat reserves, which sustains them for a while. Eventually reserves run out, but the decline is gradual rather than sudden."
        },
        {
            "question": "How does the cell model explain why you breathe faster during exercise?",
            "choices": {
                "A": "Exercise heats up your lungs, making them expand and contract faster",
                "B": "Muscle cells need more ATP during exercise, so mitochondria work harder, consuming more oxygen and producing more CO2 that must be exhaled",
                "C": "Your brain signals faster breathing to cool your body down",
                "D": "Exercise creates new mitochondria that require extra oxygen"
            },
            "correct": "B",
            "feedback_correct": "Correct! During exercise, muscle cells demand more ATP for contraction. Mitochondria must work harder, consuming more oxygen and producing more CO2 waste. Your breathing rate increases to deliver more oxygen to the cells AND to expel the extra CO2. The whole-body response is driven by cellular-level demand.",
            "feedback_incorrect": "Not quite. The connection is direct: exercising muscles need more ATP, so mitochondria increase their activity. More active mitochondria consume more oxygen (so you need to breathe in more) and produce more CO2 waste (so you need to breathe out more). Your faster breathing is a whole-body response to a cellular-level demand."
        },
        {
            "question": "Which relationship in the cell model creates a potential problem for cell health?",
            "choices": {
                "A": "Nutrient input positively affecting mitochondria activity",
                "B": "Oxygen availability positively affecting mitochondria activity",
                "C": "Waste production negatively affecting cell growth rate, because more energy production also creates more toxic byproducts",
                "D": "Mitochondria activity positively affecting cell growth rate"
            },
            "correct": "C",
            "feedback_correct": "Correct! There is a built-in tension in the system: higher mitochondria activity produces more ATP for growth (positive) but also more CO2 waste (positive). That waste negatively affects cell growth by lowering pH and damaging enzymes. Cells must remove waste fast enough to prevent this toxic buildup from canceling out the benefits of energy production.",
            "feedback_incorrect": "Not quite. The problematic relationship is between waste production and cell growth. More mitochondria activity produces more energy (good) but also more CO2 waste (bad). If waste removal cannot keep pace, the toxic buildup actually slows cell growth. The cell must balance energy production with waste management."
        }
    ]
}

L05_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "In the chemical reaction model, what happens to the Total Mass line when reactants convert to products?",
            "choices": {
                "A": "Total Mass decreases because some matter is destroyed in the reaction",
                "B": "Total Mass increases because new atoms are created during the reaction",
                "C": "Total Mass stays perfectly flat because atoms are neither created nor destroyed, they just rearrange",
                "D": "Total Mass fluctuates up and down as the reaction proceeds"
            },
            "correct": "C",
            "feedback_correct": "Correct! Conservation of mass means the total mass never changes during a chemical reaction. As reactant mass decreases, product mass increases by exactly the same amount. The total is always constant because atoms are rearranging, not appearing or disappearing.",
            "feedback_incorrect": "Not quite. The law of conservation of mass states that atoms are neither created nor destroyed in chemical reactions. As reactants are converted to products, the total count of every type of atom remains the same. The total mass line stays perfectly flat, proving that matter is conserved."
        },
        {
            "question": "A student burns a 200-gram log in an open fire and the remaining ash weighs only 15 grams. Does this violate conservation of mass?",
            "choices": {
                "A": "Yes, 185 grams of matter were destroyed by the fire",
                "B": "No, the missing 185 grams escaped as carbon dioxide gas and water vapor into the atmosphere",
                "C": "Yes, fire converts matter into pure energy",
                "D": "No, the missing mass was absorbed by the surrounding air"
            },
            "correct": "B",
            "feedback_correct": "Correct! Burning is a chemical reaction between the log's carbon and hydrogen atoms with oxygen from the air. The products are CO2 gas and water vapor, which float away into the atmosphere. The ash is only the minerals that did not combust. If you could capture and weigh all the gases, the total mass would equal the original log plus the oxygen consumed.",
            "feedback_incorrect": "Not quite. Conservation of mass is never violated. When wood burns, the carbon and hydrogen atoms combine with oxygen to form CO2 and water vapor, which are invisible gases that escape into the air. The 'missing' mass is not destroyed. It changed form from solid wood to invisible gases. In a sealed container, the mass before and after would be identical."
        },
        {
            "question": "Why does the reaction rate slow down as a chemical reaction proceeds, even if the temperature stays constant?",
            "choices": {
                "A": "The products interfere with the reaction and block it from continuing",
                "B": "The container walls absorb energy from the reaction",
                "C": "As reactant molecules are consumed, fewer molecules remain to collide, so collisions become less frequent",
                "D": "Chemical reactions naturally lose energy over time"
            },
            "correct": "C",
            "feedback_correct": "Correct! Reaction rate depends on how often reactant molecules collide. As reactants are consumed and converted to products, fewer reactant molecules remain in the system. Fewer molecules means fewer collisions per second, which slows the reaction. This is a self-slowing system, similar to how cooling curves flatten.",
            "feedback_incorrect": "Not quite. The reaction rate depends on collision frequency between reactant molecules. Early in the reaction, many reactant molecules are present and collisions are frequent. As the reaction converts reactants to products, fewer reactant molecules remain, so collisions become rarer and the rate slows. It is the same self-slowing pattern seen in cooling curves."
        },
        {
            "question": "How does increasing temperature affect a chemical reaction?",
            "choices": {
                "A": "Higher temperature creates new atoms that speed up the reaction",
                "B": "Higher temperature makes molecules move faster, collide more often, and collide with more energy, increasing the reaction rate",
                "C": "Higher temperature has no effect on reaction rate, only on the amount of product formed",
                "D": "Higher temperature destroys some reactant molecules, slowing the reaction"
            },
            "correct": "B",
            "feedback_correct": "Correct! Temperature is a measure of molecular motion. Higher temperature means molecules move faster, which increases both the frequency and the energy of collisions. More frequent, more energetic collisions mean more successful reactions per second, increasing the reaction rate.",
            "feedback_incorrect": "Not quite. Temperature directly affects how fast molecules move. Faster-moving molecules collide more often and with greater energy. Both of these effects increase the reaction rate. This is why food cooks faster at higher temperatures and why refrigeration slows food spoilage (a chemical reaction)."
        },
        {
            "question": "In the model, reactant concentration and product formation are described as 'mirror images' of each other. What does this mean and why does it happen?",
            "choices": {
                "A": "Reactants and products are always at the same concentration",
                "B": "As reactant concentration decreases by a certain amount, product formation increases by exactly the same amount, because atoms are rearranging rather than being created or destroyed",
                "C": "The two graphs look the same but are measured at different times",
                "D": "Products break down into reactants at the same rate they are formed"
            },
            "correct": "B",
            "feedback_correct": "Correct! Since atoms are neither created nor destroyed, every gram of reactant that disappears reappears as a gram of product. The reactant line goes down while the product line goes up by the same amount. They are perfect inverses because conservation of mass guarantees that what is lost from one side is gained by the other.",
            "feedback_incorrect": "Not quite. The mirror image pattern is a direct consequence of conservation of mass. Atoms from reactant molecules rearrange into product molecules. Every unit of mass that leaves the reactant pool enters the product pool. So if reactants decrease by 30 grams, products must increase by exactly 30 grams. The two lines are mathematically linked by conservation."
        }
    ]
}

L06_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "A giant redwood tree weighs over 2 million pounds. Where did most of that mass come from?",
            "choices": {
                "A": "Minerals and nutrients absorbed from the soil through the roots",
                "B": "Water absorbed from the ground",
                "C": "Carbon dioxide gas from the atmosphere, converted to glucose and then to wood through photosynthesis",
                "D": "Sunlight energy that was converted into solid matter"
            },
            "correct": "C",
            "feedback_correct": "Correct! Through photosynthesis, plants take carbon atoms from CO2 in the air and fix them into glucose molecules. That glucose is then assembled into cellulose, lignin, and other structural molecules that make up wood. A tree is literally built from air. Soil minerals make up less than 5% of tree mass.",
            "feedback_incorrect": "Not quite. Most people assume trees grow from soil, but soil provides only minerals (less than 5% of mass). The carbon that makes up wood comes from CO2 in the air. During photosynthesis, carbon from atmospheric CO2 is fixed into glucose, which is then used to build the solid structures of the tree. Trees are made of air."
        },
        {
            "question": "In the photosynthesis model, what happens when light is abundant and water is plentiful but CO2 is very low?",
            "choices": {
                "A": "Glucose production runs at maximum because two out of three inputs are high",
                "B": "Glucose production is severely limited because CO2 is the limiting factor, regardless of how much light and water are available",
                "C": "The plant switches to using nitrogen from the air instead of CO2",
                "D": "The extra light compensates for the lack of CO2"
            },
            "correct": "B",
            "feedback_correct": "Correct! This demonstrates the limiting factor concept. Photosynthesis requires ALL three inputs simultaneously. The rate is controlled by whichever input is in shortest supply. With low CO2, there are not enough carbon atoms to fix into glucose, so production is limited regardless of how much light and water are available.",
            "feedback_incorrect": "Not quite. Photosynthesis cannot run faster than its weakest input allows. Even with abundant light and water, low CO2 means few carbon atoms are available for glucose production. The CO2 becomes the bottleneck, or limiting factor, that constrains the entire process. No single input can compensate for another."
        },
        {
            "question": "Why is oxygen described as a 'byproduct' of photosynthesis rather than its main purpose?",
            "choices": {
                "A": "Plants do not actually produce oxygen",
                "B": "Plants produce oxygen to help animals breathe, which is the main purpose",
                "C": "Oxygen is released when water molecules are split to provide hydrogen and electrons for glucose production. The plant needs the hydrogen, not the oxygen.",
                "D": "Oxygen is just leftover sunlight energy that the plant cannot use"
            },
            "correct": "C",
            "feedback_correct": "Correct! During the light reactions of photosynthesis, water molecules (H2O) are split to harvest hydrogen atoms and electrons needed to build glucose. The oxygen atoms left over are released as O2 gas. The plant does not make oxygen on purpose. It is a leftover from splitting water for its useful parts.",
            "feedback_incorrect": "Not quite. The purpose of photosynthesis is to produce glucose for energy and growth. To do this, plants must split water molecules to get hydrogen atoms and electrons. The oxygen from water is the leftover that the plant does not need, so it is released as a byproduct. Oxygen production is a side effect, not the goal."
        },
        {
            "question": "How are photosynthesis and cellular respiration related?",
            "choices": {
                "A": "They are the same process happening in different organelles",
                "B": "They are essentially opposite reactions: photosynthesis builds glucose from CO2 and water using light energy, while cellular respiration breaks glucose down into CO2 and water to release energy",
                "C": "Photosynthesis only occurs in plants and cellular respiration only occurs in animals",
                "D": "They have no relationship because they occur in different types of cells"
            },
            "correct": "B",
            "feedback_correct": "Correct! Photosynthesis and cellular respiration are reverse processes. Photosynthesis: CO2 + H2O + light energy yields glucose + O2. Cellular respiration: glucose + O2 yields CO2 + H2O + ATP energy. The products of one are the reactants of the other. Plants actually perform BOTH processes.",
            "feedback_incorrect": "Not quite. These two processes are mirror images of each other. Photosynthesis uses light energy to build glucose from CO2 and water, releasing oxygen. Cellular respiration does the reverse, breaking glucose down with oxygen to release energy as ATP, producing CO2 and water. Plants do both processes, not just photosynthesis."
        },
        {
            "question": "A scientist grows two identical plants in sealed containers. Plant A has normal light, CO2, and water. Plant B has normal light and water but the CO2 has been removed. After four weeks, what would the model predict?",
            "choices": {
                "A": "Both plants grow equally because light provides all the energy needed",
                "B": "Plant B grows slightly less because it can use water as an alternative carbon source",
                "C": "Plant B barely grows because without CO2, it cannot perform photosynthesis or produce glucose for building new tissue",
                "D": "Plant B grows more because removing CO2 forces the plant to use more efficient processes"
            },
            "correct": "C",
            "feedback_correct": "Correct! CO2 provides the carbon atoms that plants fix into glucose and then into all structural molecules. Without CO2, photosynthesis cannot produce glucose. Without glucose, the plant has no building material for growth and no energy source. Plant B would barely grow and would slowly consume its stored reserves.",
            "feedback_incorrect": "Not quite. CO2 is one of the three essential inputs for photosynthesis. Without it, the plant cannot fix carbon into glucose. Without glucose, there is no building material for new cells and no energy source. The plant would survive briefly by burning stored reserves but could not grow. This proves that plant mass comes from atmospheric carbon."
        }
    ]
}

L07_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "In the engineering design model, what happens when a team jumps into building a prototype for a complex problem without doing any research first?",
            "choices": {
                "A": "The prototype works well because hands-on building is more effective than research",
                "B": "Design quality is low because the team does not understand the problem well enough, leading to poor prototype performance",
                "C": "Research is unnecessary because testing will reveal everything they need to know",
                "D": "The prototype performs the same regardless of research depth"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model shows that research depth has a strong positive effect on initial design quality. Without understanding the problem, existing solutions, and relevant science, the first design addresses the wrong issues or misses key constraints. This leads to a poor-performing prototype that wastes the first iteration.",
            "feedback_incorrect": "Not quite. The model demonstrates that skipping research leads to low design quality because the team does not understand what they are solving. Understanding the problem, constraints, and relevant science before designing produces a much better first attempt. Research does not replace testing, but it makes testing more productive."
        },
        {
            "question": "Why is iteration the single most powerful variable for improving engineering outcomes?",
            "choices": {
                "A": "Iteration allows engineers to start over from scratch with each attempt",
                "B": "Each test-improve cycle reveals problems that planning alone cannot predict, and fixing those problems creates a positive feedback loop of improvement",
                "C": "Iteration is just repeating the same design until it works by luck",
                "D": "More iterations mean more materials are used, which always produces better results"
            },
            "correct": "B",
            "feedback_correct": "Correct! Real-world testing reveals unexpected problems that no amount of planning could anticipate. Each iteration identifies specific failures, which inform targeted improvements. This creates a positive feedback loop: testing reveals problems, redesign fixes them, the next test reveals subtler problems, and so on. Each cycle produces a measurably better design.",
            "feedback_incorrect": "Not quite. Iteration is not random repetition. It is a structured cycle of testing, identifying specific failures, redesigning to fix those failures, and testing again. Each cycle makes the design better because real-world testing reveals problems that theory alone cannot predict. The positive feedback loop between testing and improvement is the engine of engineering innovation."
        },
        {
            "question": "The model shows a positive feedback loop between prototype testing and design quality. What does this mean?",
            "choices": {
                "A": "Positive feedback means the design gets worse with each test",
                "B": "Testing a prototype provides specific information about what works and what fails, which directly improves the next design, which produces an even better prototype",
                "C": "Positive feedback means the engineer feels more confident after each test",
                "D": "The prototype automatically improves itself without human intervention"
            },
            "correct": "B",
            "feedback_correct": "Correct! In this positive feedback loop, testing reveals real performance data and failure points. This information improves the next design iteration. The improved design produces a better prototype, which reveals subtler (previously hidden) problems when tested. Each cycle drives improvement because real data continuously feeds back into the design process.",
            "feedback_incorrect": "Not quite. A positive feedback loop in this context means that the output of one step amplifies the next. Testing produces performance data that improves design quality. Better design produces better prototypes. Better prototypes reveal more nuanced problems when tested. Each cycle feeds forward, creating continuous improvement. This is why iteration beats perfecting a design on paper."
        },
        {
            "question": "Two teams tackle the same engineering problem. Team A researches thoroughly and builds one prototype. Team B does minimal research but builds and tests three prototypes. Based on the model, which team likely produces a better solution?",
            "choices": {
                "A": "Team A, because research always produces better results than testing",
                "B": "Team B, because three iterations of testing and improvement typically outperform one well-researched attempt that has not been tested against reality",
                "C": "Both teams produce identical results because the problem is the same",
                "D": "Neither team can succeed without combining research and iteration"
            },
            "correct": "B",
            "feedback_correct": "Correct! While research improves the first design, the model shows that iteration is the most powerful improvement variable. Three test-improve cycles reveal real-world problems that research alone cannot predict. Team B's iterative approach, even with less research, produces more total improvement through the feedback loop between testing and redesign.",
            "feedback_incorrect": "Not quite. The model reveals that while research improves initial design quality, iteration is the strongest driver of final prototype performance. Three cycles of real-world testing reveal problems that no amount of planning can anticipate. Each test-improve cycle makes the design measurably better. The ideal approach combines research with iteration, but forced to choose, iteration wins."
        },
        {
            "question": "How does increasing problem complexity affect the engineering design process?",
            "choices": {
                "A": "More complex problems require fewer iterations because engineers work harder",
                "B": "More complex problems produce worse first designs because more constraints and criteria interact in unpredictable ways, making research and iteration even more important",
                "C": "Problem complexity has no effect because all engineering follows the same steps",
                "D": "More complex problems are easier because they have more possible solutions"
            },
            "correct": "B",
            "feedback_correct": "Correct! Higher problem complexity means more criteria, more constraints, and more interactions between them. This makes it harder to design a good solution on the first try because there are more ways things can go wrong. The model shows that both research (to understand the complexity) and iteration (to discover unexpected interactions) become more critical as complexity increases.",
            "feedback_incorrect": "Not quite. Complex problems have many interacting criteria and constraints, which makes first attempts less likely to succeed. With more variables, there are more unexpected interactions and failure modes. The model shows that complex problems benefit most from thorough research (to understand the system) and multiple iterations (to discover and fix problems that emerge only during testing)."
        }
    ]
}

# ─── Master dictionary ───────────────────────────────────────────────────────

ALL_QUESTIONS = {
    "G06L2-L01": L01_QUESTIONS,
    "G06L2-L02": L02_QUESTIONS,
    "G06L2-L03": L03_QUESTIONS,
    "G06L2-L04": L04_QUESTIONS,
    "G06L2-L05": L05_QUESTIONS,
    "G06L2-L06": L06_QUESTIONS,
    "G06L2-L07": L07_QUESTIONS,
}
