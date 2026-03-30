#!/usr/bin/env python3
"""Multiple choice pre/post assessment questions for Grade 6 ModelIt! Lessons"""

L01_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is the basic building block of all living things?",
            "choices": {
                "A": "Atoms",
                "B": "Cells",
                "C": "Molecules",
                "D": "Organs"
            },
            "correct": "B",
            "feedback_correct": "Correct! Cells are the smallest unit of life. Every living organism is made of one or more cells.",
            "feedback_incorrect": "Not quite. While atoms and molecules are important, the cell is the basic unit of life. All living things are made of cells."
        },
        {
            "question": "Why do scientists need microscopes to study most cells?",
            "choices": {
                "A": "Cells move too fast to see",
                "B": "Cells are transparent and invisible",
                "C": "Cells are too small to see with the naked eye",
                "D": "Cells only exist inside bones where we can't look"
            },
            "correct": "C",
            "feedback_correct": "Correct! Most cells are far too small to see without magnification. Human cells are typically 10-100 micrometers wide.",
            "feedback_incorrect": "Not quite. The main reason we need microscopes is that cells are extremely small, usually between 10 and 100 micrometers, which is far below what our eyes can detect."
        },
        {
            "question": "Which of these is a living thing made of only ONE cell?",
            "choices": {
                "A": "A dog",
                "B": "A tree",
                "C": "A bacterium",
                "D": "A mushroom"
            },
            "correct": "C",
            "feedback_correct": "Correct! Bacteria are single-celled organisms. Each bacterium is one complete living cell that carries out all life functions.",
            "feedback_incorrect": "Not quite. Dogs, trees, and mushrooms are all made of many cells. Bacteria are single-celled organisms, meaning one cell does everything needed to survive."
        },
        {
            "question": "What do you think cells need to stay alive?",
            "choices": {
                "A": "Only water",
                "B": "Only sunlight",
                "C": "Nutrients, oxygen, and waste removal",
                "D": "Nothing — cells are self-sufficient"
            },
            "correct": "C",
            "feedback_correct": "Correct! Cells need nutrients for energy, oxygen for cellular respiration, and they must remove waste to survive.",
            "feedback_incorrect": "Not quite. Like all living things, cells need multiple resources: nutrients for energy, oxygen for respiration, and a way to get rid of waste products."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "Why can't a single cell grow to be as large as a basketball?",
            "choices": {
                "A": "Cells are programmed to stay small by their DNA",
                "B": "As a cell grows, its volume increases faster than its surface area, so it can't exchange materials efficiently",
                "C": "Gravity would crush a cell that large",
                "D": "There aren't enough organelles to fill a cell that big"
            },
            "correct": "B",
            "feedback_correct": "Correct! The surface-area-to-volume ratio is the key constraint. A larger cell would have too much interior for its membrane to supply with nutrients and remove waste from.",
            "feedback_incorrect": "Not quite. The real reason is the surface-area-to-volume ratio. As a cell grows, its interior (volume) increases faster than its membrane (surface area), so the membrane can't keep up with exchanging nutrients and waste."
        },
        {
            "question": "In the cell model, what happens when Nutrient Supply is locked at 10%?",
            "choices": {
                "A": "Cell Size increases because the cell stores energy",
                "B": "Waste Buildup decreases because the cell uses less",
                "C": "Cell Size decreases and Waste Buildup increases as the cell loses function",
                "D": "Nothing changes because cells can survive without nutrients"
            },
            "correct": "C",
            "feedback_correct": "Correct! Without adequate nutrients, cells shrink because they can't maintain their structures, and waste builds up because the cell can't power its cleanup systems.",
            "feedback_incorrect": "Not quite. When nutrient supply drops to 10%, cells shrink because they lack energy to maintain their structures. Waste also builds up because the cell can't power its waste removal systems."
        },
        {
            "question": "Which statement best describes the relationship between Oxygen Level and Waste Buildup in the cell model?",
            "choices": {
                "A": "Positive relationship — more oxygen means more waste",
                "B": "Negative relationship — more oxygen helps break down waste, so waste decreases",
                "C": "No relationship — oxygen and waste are independent",
                "D": "Oxygen creates waste as a byproduct of respiration"
            },
            "correct": "B",
            "feedback_correct": "Correct! Higher oxygen levels allow cellular respiration to work efficiently, which helps break down and remove waste. Low oxygen causes waste to accumulate.",
            "feedback_incorrect": "Not quite. Oxygen and Waste Buildup have a negative relationship. More oxygen allows efficient cellular respiration, which helps cells break down waste. When oxygen drops, waste accumulates."
        },
        {
            "question": "A scientist observes that cells in a tissue sample are shrinking and accumulating waste. Which combination of conditions most likely explains this?",
            "choices": {
                "A": "High nutrient supply and high oxygen",
                "B": "Low nutrient supply and low oxygen",
                "C": "High nutrient supply and low oxygen",
                "D": "Low nutrient supply and high oxygen"
            },
            "correct": "B",
            "feedback_correct": "Correct! Both low nutrients (causing shrinkage) and low oxygen (causing waste buildup) together would produce these symptoms. This is what happens when blood flow to a tissue is restricted.",
            "feedback_incorrect": "Not quite. Shrinking cells indicate low nutrient supply, and waste accumulation indicates low oxygen. Both conditions together, such as restricted blood flow, would cause these observations."
        }
    ]
}

L02_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is the outermost layer of the Earth called?",
            "choices": {
                "A": "Mantle",
                "B": "Core",
                "C": "Crust",
                "D": "Magma"
            },
            "correct": "C",
            "feedback_correct": "Correct! The crust is the thin, solid outermost layer of Earth where we live. It sits on top of the mantle.",
            "feedback_incorrect": "Not quite. The outermost layer of the Earth is the crust. The mantle is below the crust, and the core is at Earth's center."
        },
        {
            "question": "Why do you think earthquakes happen in certain places more than others?",
            "choices": {
                "A": "Earthquakes happen randomly all over the planet",
                "B": "Earthquakes only happen near oceans",
                "C": "Earthquakes happen where pieces of Earth's surface meet and push against each other",
                "D": "Earthquakes are caused by underground explosions"
            },
            "correct": "C",
            "feedback_correct": "Correct! Earthquakes occur most often at plate boundaries, where large pieces of Earth's crust (tectonic plates) meet and interact.",
            "feedback_incorrect": "Not quite. Earthquakes are not random. They occur most frequently at plate boundaries, where large sections of Earth's crust push together, pull apart, or slide past each other."
        },
        {
            "question": "What do you think causes the ground to shake during an earthquake?",
            "choices": {
                "A": "Wind pushing on the ground",
                "B": "The Moon's gravity pulling on Earth",
                "C": "Energy released when rocks suddenly break or slip",
                "D": "Heavy rain soaking into the ground"
            },
            "correct": "C",
            "feedback_correct": "Correct! Earthquakes happen when built-up stress in rocks is suddenly released as energy, creating seismic waves that shake the ground.",
            "feedback_incorrect": "Not quite. Earthquakes occur when stress builds up in rocks at plate boundaries and is suddenly released as energy. This energy travels as seismic waves that shake the ground."
        },
        {
            "question": "What is beneath the solid ground you walk on?",
            "choices": {
                "A": "More solid rock all the way to the center of the Earth",
                "B": "Empty space and underground caves",
                "C": "Layers of increasingly hot rock, some of which flows very slowly",
                "D": "Water and underground rivers"
            },
            "correct": "C",
            "feedback_correct": "Correct! Beneath the crust are layers of increasingly hot rock. The mantle is semi-solid and flows very slowly, and the core is extremely hot metal.",
            "feedback_incorrect": "Not quite. Beneath the surface are layers of rock that get hotter with depth. The mantle is semi-solid rock that flows very slowly over millions of years, driven by heat from the core."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "What drives the movement of tectonic plates?",
            "choices": {
                "A": "Gravity pulling plates toward the equator",
                "B": "Convection currents in the mantle caused by heat from Earth's core",
                "C": "The Moon's gravitational pull on Earth's surface",
                "D": "Wind and ocean currents pushing on the continents"
            },
            "correct": "B",
            "feedback_correct": "Correct! Heat from Earth's core creates convection currents in the mantle. Hot rock rises, cool rock sinks, and this circular flow drags tectonic plates along.",
            "feedback_incorrect": "Not quite. Tectonic plates are moved by convection currents in the mantle. Heat from Earth's core makes rock rise, and cooler rock sinks, creating a slow circular flow that drags plates."
        },
        {
            "question": "In the tectonic model, what happens when Boundary Friction is set to maximum?",
            "choices": {
                "A": "Earthquakes happen more frequently but are very small",
                "B": "Plates stop moving permanently",
                "C": "Energy builds up for a long time, then releases as a large earthquake",
                "D": "Volcanic activity increases because friction melts rock"
            },
            "correct": "C",
            "feedback_correct": "Correct! Maximum friction locks plates together, allowing enormous stress to accumulate. When the friction finally fails, all that energy releases at once as a powerful earthquake.",
            "feedback_incorrect": "Not quite. High friction locks plates together, preventing small releases. Energy builds up over time, and when the plates finally slip, the result is a large, powerful earthquake."
        },
        {
            "question": "Which explains why about 90% of earthquakes occur along the Ring of Fire?",
            "choices": {
                "A": "The Pacific Ocean's water causes the crust to crack",
                "B": "The Ring of Fire is the boundary of the Pacific Plate, where multiple plates interact",
                "C": "Volcanic gases weaken the rock along the Ring of Fire",
                "D": "The Ring of Fire receives more heat from the Sun"
            },
            "correct": "B",
            "feedback_correct": "Correct! The Ring of Fire traces the boundaries of the Pacific Plate, where it interacts with many other plates. Plate boundary interactions cause earthquakes and volcanoes.",
            "feedback_incorrect": "Not quite. The Ring of Fire marks the edges of the Pacific Plate, where it meets several other tectonic plates. These boundary zones are where plates collide, separate, or slide past each other, causing earthquakes and volcanoes."
        },
        {
            "question": "A coastal region has not had a major earthquake in 150 years, even though it sits on a plate boundary. Based on the tectonic model, what should scientists predict?",
            "choices": {
                "A": "The plates have stopped moving, so the region is now safe",
                "B": "A large earthquake is likely because stress has been building for 150 years",
                "C": "The boundary has changed from convergent to divergent",
                "D": "Earthquakes will never happen there again"
            },
            "correct": "B",
            "feedback_correct": "Correct! A long quiet period at a plate boundary means friction is locking the plates while stress accumulates. The longer the quiet, the bigger the eventual release.",
            "feedback_incorrect": "Not quite. Plate boundaries don't stop being active. A long period without earthquakes means friction is holding the plates locked while stress builds. This makes a large earthquake more likely, not less."
        }
    ]
}

L03_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "When you hold a hot mug, your hands feel warm. What is happening?",
            "choices": {
                "A": "Cold is leaving your hands and going into the mug",
                "B": "Heat energy is transferring from the hot mug to your cooler hands",
                "C": "Your hands are creating their own heat in response to the mug",
                "D": "The mug's color is making your hands feel warm"
            },
            "correct": "B",
            "feedback_correct": "Correct! Thermal energy always transfers from warmer objects to cooler objects through direct contact, a process called conduction.",
            "feedback_incorrect": "Not quite. Heat energy transfers from the hotter object (the mug) to the cooler object (your hands). Cold is not a substance that moves; rather, heat energy flows from hot to cold."
        },
        {
            "question": "If you leave a hot drink on the counter, what will eventually happen to its temperature?",
            "choices": {
                "A": "It will stay hot forever",
                "B": "It will get colder than room temperature",
                "C": "It will cool down until it matches room temperature",
                "D": "It depends on the color of the cup"
            },
            "correct": "C",
            "feedback_correct": "Correct! Heat flows from the hot drink to the cooler surroundings until both reach the same temperature, called thermal equilibrium.",
            "feedback_incorrect": "Not quite. A hot drink will always cool down to match the temperature of its surroundings. Heat flows from hot to cold until temperatures equalize."
        },
        {
            "question": "Why does a metal spoon in hot soup feel hotter than a wooden spoon?",
            "choices": {
                "A": "Metal is always hotter than wood",
                "B": "Metal transfers heat to your hand faster than wood does",
                "C": "Wood absorbs all the heat so none reaches your hand",
                "D": "The metal spoon is closer to the heat source"
            },
            "correct": "B",
            "feedback_correct": "Correct! Metal is a better conductor of heat than wood. It transfers thermal energy to your hand much faster, making it feel hotter even at the same temperature.",
            "feedback_incorrect": "Not quite. Metal conducts heat much faster than wood. Both spoons may be the same temperature, but the metal one transfers that heat to your hand more quickly, so it feels hotter."
        },
        {
            "question": "What do you think keeps a drink warm inside a thermos?",
            "choices": {
                "A": "A thermos generates its own heat",
                "B": "The thermos adds chemicals that heat the drink",
                "C": "The thermos has materials that slow down heat from escaping",
                "D": "The drink stays hot because no air can get in"
            },
            "correct": "C",
            "feedback_correct": "Correct! A thermos uses insulating materials and a vacuum layer to slow down thermal energy transfer, keeping the drink hot longer.",
            "feedback_incorrect": "Not quite. A thermos works by using insulation to slow down the transfer of heat from the hot drink to the cooler surroundings. It doesn't add heat; it just slows the loss."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "Which of the three methods of heat transfer is responsible for warm air rising above a hot cup of cocoa?",
            "choices": {
                "A": "Conduction — heat transfers through direct contact",
                "B": "Convection — warm air rises and carries heat away",
                "C": "Radiation — heat travels as infrared waves",
                "D": "Insulation — air traps the heat near the cup"
            },
            "correct": "B",
            "feedback_correct": "Correct! Convection is the transfer of heat through the movement of fluids (liquids and gases). Warm air above the cocoa rises, carrying thermal energy away.",
            "feedback_incorrect": "Not quite. When warm air rises above a hot drink, that is convection. Convection is heat transfer through the movement of fluids, including air. Warm air is less dense, so it rises."
        },
        {
            "question": "In the thermal energy model, which variable has a NEGATIVE relationship with heat loss rate?",
            "choices": {
                "A": "Temperature Difference — greater difference means faster heat loss",
                "B": "Container Surface Area — more area means faster heat loss",
                "C": "Insulation Level — more insulation means slower heat loss",
                "D": "Air Movement — more wind means faster heat loss"
            },
            "correct": "C",
            "feedback_correct": "Correct! Insulation Level has a negative relationship with heat loss. As insulation increases, the rate of heat loss decreases because insulation slows thermal energy transfer.",
            "feedback_incorrect": "Not quite. Insulation Level has a negative relationship with heat loss rate. More insulation means less heat escapes. The other options (temperature difference, surface area, air movement) all have positive relationships with heat loss."
        },
        {
            "question": "Why does a tall, thin mug lose heat faster than a short, wide mug that holds the same amount of cocoa?",
            "choices": {
                "A": "The tall mug has more surface area exposed to the air",
                "B": "Tall mugs are made of thinner material",
                "C": "Heat rises, so tall mugs push heat out the top faster",
                "D": "Short mugs have stronger insulation"
            },
            "correct": "A",
            "feedback_correct": "Correct! A tall, thin mug has more surface area relative to its volume than a short, wide mug. More surface area means more area for heat to escape through conduction and convection.",
            "feedback_incorrect": "Not quite. The key factor is surface area. A tall, thin mug exposes more surface to the surrounding air, giving heat more area to escape through. This is why mug shape matters for keeping drinks hot."
        },
        {
            "question": "A student designs two containers: one wrapped in foam and one left bare. Both start at 80 degrees C. After 30 minutes, the foam container is at 65 degrees C and the bare one is at 45 degrees C. What does this evidence show?",
            "choices": {
                "A": "Foam generates heat to keep the drink warm",
                "B": "Foam slows thermal energy transfer, reducing the rate of heat loss",
                "C": "The bare container had a chemical reaction that cooled it faster",
                "D": "Foam changes the boiling point of the liquid inside"
            },
            "correct": "B",
            "feedback_correct": "Correct! The foam insulation slowed the transfer of thermal energy from the hot liquid to the cooler environment. Both containers lost heat, but the insulated one lost it more slowly.",
            "feedback_incorrect": "Not quite. The foam acts as insulation, which slows thermal energy transfer. Both drinks cooled, but the insulated container lost heat more slowly because the foam reduced conduction through the container walls."
        }
    ]
}

L04_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Which type of rock is formed when melted rock (magma or lava) cools and hardens?",
            "choices": {
                "A": "Sedimentary rock",
                "B": "Metamorphic rock",
                "C": "Igneous rock",
                "D": "Fossil rock"
            },
            "correct": "C",
            "feedback_correct": "Correct! Igneous rock forms when magma (underground) or lava (on the surface) cools and solidifies. 'Igneous' comes from the Latin word for fire.",
            "feedback_incorrect": "Not quite. When melted rock cools and hardens, it forms igneous rock. Sedimentary rock forms from compressed layers, and metamorphic rock forms from heat and pressure changing existing rock."
        },
        {
            "question": "Where are fossils most commonly found?",
            "choices": {
                "A": "Inside volcanic lava flows",
                "B": "In layers of sedimentary rock",
                "C": "Deep inside metamorphic rock",
                "D": "On the surface of igneous rock"
            },
            "correct": "B",
            "feedback_correct": "Correct! Fossils are preserved in sedimentary rock because organisms get buried in layers of sediment that compress over time without destroying the remains.",
            "feedback_incorrect": "Not quite. Fossils are almost always found in sedimentary rock. The gentle process of burial in sediment layers preserves organisms, while the extreme heat of igneous and metamorphic processes destroys them."
        },
        {
            "question": "What do you think causes rocks to break down into smaller pieces over time?",
            "choices": {
                "A": "Rocks don't break down — they last forever",
                "B": "Only earthquakes can break rocks",
                "C": "Wind, water, ice, and chemicals gradually wear rocks down",
                "D": "Rocks dissolve in sunlight"
            },
            "correct": "C",
            "feedback_correct": "Correct! Weathering is the process by which wind, water, ice, and chemical reactions gradually break rocks into smaller pieces over time.",
            "feedback_incorrect": "Not quite. Rocks are constantly being broken down by weathering: wind blows particles against them, water seeps into cracks and freezes, and chemical reactions dissolve minerals. This is a slow but powerful process."
        },
        {
            "question": "Can one type of rock change into a different type of rock?",
            "choices": {
                "A": "No, rocks stay the same type forever",
                "B": "Yes, but only if they melt completely",
                "C": "Yes, heat, pressure, and weathering can transform rocks from one type to another",
                "D": "Only scientists can change rock types in a laboratory"
            },
            "correct": "C",
            "feedback_correct": "Correct! The rock cycle continuously transforms rocks from one type to another through processes like melting, cooling, weathering, compression, and heat and pressure.",
            "feedback_incorrect": "Not quite. Rocks are constantly being transformed through the rock cycle. Heat and pressure can change sedimentary rock into metamorphic rock, weathering can break any rock into sediment, and melting and cooling creates igneous rock."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "How can seashell fossils be found on top of a mountain thousands of meters above sea level?",
            "choices": {
                "A": "Ancient people carried the shells up the mountain",
                "B": "Sedimentary rock with shells formed on an ancient ocean floor, then tectonic forces uplifted it into a mountain",
                "C": "The shells were blown to the mountaintop by powerful ancient winds",
                "D": "The mountain was always above water, and the shells are from freshwater animals"
            },
            "correct": "B",
            "feedback_correct": "Correct! Shells accumulated on an ancient seafloor and were buried in sediment that became rock. Over millions of years, tectonic plate collisions pushed that rock upward, forming mountains with ocean fossils inside.",
            "feedback_incorrect": "Not quite. Shell fossils on mountains formed on ancient ocean floors where shells were buried in sediment. Over millions of years, tectonic forces pushed that sedimentary rock upward to become mountain ranges."
        },
        {
            "question": "In the rock cycle model, what happens when Heat & Pressure are set to maximum while Weathering Rate is low?",
            "choices": {
                "A": "Sedimentary rock forms quickly from compressed particles",
                "B": "Existing rock transforms into metamorphic rock without melting",
                "C": "All rocks melt and become igneous rock",
                "D": "Nothing happens because rocks can't change without weathering"
            },
            "correct": "B",
            "feedback_correct": "Correct! Extreme heat and pressure transform existing rock into metamorphic rock. The rock's mineral structure changes without the rock actually melting. This happens deep underground at plate boundaries.",
            "feedback_incorrect": "Not quite. When heat and pressure are extreme, rocks are transformed into metamorphic rock. The minerals recrystallize into new forms without melting. If the rock fully melts, it would eventually form igneous rock instead."
        },
        {
            "question": "Why are fossils ONLY preserved in sedimentary rock and not in igneous or metamorphic rock?",
            "choices": {
                "A": "Igneous and metamorphic rocks are too hard to contain fossils",
                "B": "Animals only lived near sedimentary rock formations",
                "C": "The extreme heat and pressure that form igneous and metamorphic rocks destroy any organic remains",
                "D": "Sedimentary rock has special chemicals that preserve fossils"
            },
            "correct": "C",
            "feedback_correct": "Correct! Igneous rock forms from melting (destroying any remains), and metamorphic rock forms under extreme heat and pressure (also destroying remains). Only sedimentary rock forms gently enough to preserve fossils.",
            "feedback_incorrect": "Not quite. The processes that create igneous rock (melting) and metamorphic rock (extreme heat and pressure) are so intense they destroy any organic material. Sedimentary rock forms through gentle burial and compression, preserving fossils."
        },
        {
            "question": "The rock cycle is driven by two energy sources. What are they?",
            "choices": {
                "A": "Wind and water",
                "B": "Gravity and magnetism",
                "C": "Earth's internal heat and the Sun's energy",
                "D": "Earthquakes and volcanoes"
            },
            "correct": "C",
            "feedback_correct": "Correct! Earth's internal heat drives metamorphism, melting, and tectonic uplift, while the Sun's energy drives weathering and erosion through wind, rain, and temperature changes.",
            "feedback_incorrect": "Not quite. The rock cycle is powered by Earth's internal heat (which causes melting, metamorphism, and plate movement) and the Sun's energy (which drives weather patterns that cause erosion and weathering)."
        }
    ]
}

L05_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is the smallest particle of a compound that still has the properties of that compound?",
            "choices": {
                "A": "An atom",
                "B": "A molecule",
                "C": "A cell",
                "D": "An electron"
            },
            "correct": "B",
            "feedback_correct": "Correct! A molecule is the smallest unit of a compound. It consists of two or more atoms bonded together in a specific arrangement.",
            "feedback_incorrect": "Not quite. A molecule is the smallest particle of a compound that retains the compound's properties. Atoms are the building blocks of molecules, but a single atom isn't the compound itself."
        },
        {
            "question": "Why do you think honey flows more slowly than water?",
            "choices": {
                "A": "Honey is heavier than water",
                "B": "Honey is colder than water",
                "C": "Honey has a thicker consistency because its molecules resist flowing",
                "D": "Honey sticks to the container walls more"
            },
            "correct": "C",
            "feedback_correct": "Correct! Honey has higher viscosity than water. Its larger, more complex molecules are tangled together and resist flowing past each other.",
            "feedback_incorrect": "Not quite. Honey flows slowly because it has high viscosity, meaning its molecules resist flowing. The large, complex sugar molecules in honey interact with each other and create resistance to flow."
        },
        {
            "question": "What happens to most substances when they are heated?",
            "choices": {
                "A": "They get heavier",
                "B": "They flow more easily and may change state",
                "C": "They get harder and more rigid",
                "D": "Nothing happens unless chemicals are added"
            },
            "correct": "B",
            "feedback_correct": "Correct! Heating gives molecules more energy, making them move faster. This causes substances to flow more easily and can cause state changes like melting or boiling.",
            "feedback_incorrect": "Not quite. When substances are heated, their molecules move faster with more energy. This generally makes solids softer and liquids flow more easily, and can cause changes of state."
        },
        {
            "question": "Is slime a solid or a liquid?",
            "choices": {
                "A": "It is a solid because you can hold it",
                "B": "It is a liquid because it can flow and drip",
                "C": "It can behave like both a solid and a liquid depending on the force applied",
                "D": "It is a gas trapped inside a liquid"
            },
            "correct": "C",
            "feedback_correct": "Correct! Slime is a non-Newtonian fluid. It acts solid when you squeeze it quickly but flows like a liquid when you let it sit. Its behavior depends on the force applied.",
            "feedback_incorrect": "Not quite. Slime is a special type of material called a non-Newtonian fluid. It behaves like a solid under quick force (squeezing) but flows like a liquid when force is gentle or absent."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "Why does slime act like a solid when you squeeze it quickly but flow like a liquid when left alone?",
            "choices": {
                "A": "Slime contains both solid and liquid particles mixed together",
                "B": "Quick force tangles the polymer chains, making them lock up; slow force lets chains slide past each other",
                "C": "Squeezing heats the slime and changes its state of matter",
                "D": "The glue in slime hardens when touched and melts when released"
            },
            "correct": "B",
            "feedback_correct": "Correct! Slime is made of long polymer chains. Rapid force tangles the chains so they resist movement (solid-like), but slow force or no force lets the chains slide past each other (liquid-like).",
            "feedback_incorrect": "Not quite. Slime's behavior comes from its polymer chains. When force is applied quickly, the long chains tangle and lock up, resisting flow. When left alone, the chains slowly slide past each other, allowing the slime to flow."
        },
        {
            "question": "In the molecular model, what happens when Concentration is increased from 20% to 90%?",
            "choices": {
                "A": "The substance becomes more transparent",
                "B": "The substance flows more easily because molecules are closer together",
                "C": "The substance becomes thicker and more resistant to flow as more polymer chains interact",
                "D": "Temperature increases because more molecules create friction"
            },
            "correct": "C",
            "feedback_correct": "Correct! Higher concentration means more polymer chains in the mixture. More chains means more tangling and interaction between molecules, making the substance thicker and more viscous.",
            "feedback_incorrect": "Not quite. Increasing concentration packs more polymer chains into the mixture. With more chains present, there are more opportunities for tangling and interaction, which increases viscosity and makes the substance thicker."
        },
        {
            "question": "How does increasing Temperature affect the viscosity of a polymer substance?",
            "choices": {
                "A": "Higher temperature makes the substance thicker",
                "B": "Higher temperature has no effect on viscosity",
                "C": "Higher temperature loosens molecular bonds, making the substance flow more easily",
                "D": "Higher temperature causes polymer chains to grow longer"
            },
            "correct": "C",
            "feedback_correct": "Correct! Higher temperature gives molecules more kinetic energy, causing them to vibrate and move faster. This loosens the bonds between polymer chains, reducing viscosity and making the substance flow more easily.",
            "feedback_incorrect": "Not quite. Temperature increases molecular movement. When molecules vibrate faster, the bonds between polymer chains loosen, reducing the substance's viscosity (thickness) and allowing it to flow more easily."
        },
        {
            "question": "A toy designer wants to create a slime that is very stretchy but does not flow when set on a table. Which model settings would best achieve this?",
            "choices": {
                "A": "Short polymer chains, low concentration, high temperature",
                "B": "Long polymer chains, moderate concentration, moderate bond strength",
                "C": "Short polymer chains, maximum concentration, maximum bond strength",
                "D": "Long polymer chains, low concentration, low bond strength"
            },
            "correct": "B",
            "feedback_correct": "Correct! Long polymer chains allow stretching, moderate concentration provides structure without being rigid, and moderate bond strength lets chains slide slowly (stretchy) without flowing freely.",
            "feedback_incorrect": "Not quite. For stretchiness, you need long polymer chains that can extend. Moderate concentration and bond strength give the slime enough structure to hold its shape on a table while still being flexible enough to stretch."
        }
    ]
}

L06_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is the correct order of organization in the human body, from smallest to largest?",
            "choices": {
                "A": "Organs, cells, tissues, organ systems",
                "B": "Cells, tissues, organs, organ systems",
                "C": "Tissues, cells, organ systems, organs",
                "D": "Organ systems, organs, tissues, cells"
            },
            "correct": "B",
            "feedback_correct": "Correct! The body is organized from smallest to largest: cells form tissues, tissues form organs, and organs form organ systems that work together.",
            "feedback_incorrect": "Not quite. The correct order from smallest to largest is: cells (the smallest unit of life), tissues (groups of similar cells), organs (groups of tissues), and organ systems (groups of organs working together)."
        },
        {
            "question": "Why does your heart beat faster when you exercise?",
            "choices": {
                "A": "Exercise scares the heart into beating faster",
                "B": "Your muscles need more oxygen and nutrients, so the heart pumps blood faster",
                "C": "The heart gets warmer during exercise and naturally speeds up",
                "D": "Exercise makes your blood thicker so the heart has to work harder"
            },
            "correct": "B",
            "feedback_correct": "Correct! During exercise, your muscles demand more oxygen and nutrients. The heart beats faster to increase blood flow and deliver these resources to working muscles.",
            "feedback_incorrect": "Not quite. When you exercise, your muscles need extra oxygen and nutrients for energy. Your heart responds by beating faster to pump more blood, delivering those resources to where they are needed."
        },
        {
            "question": "Which body system is responsible for breaking down the food you eat?",
            "choices": {
                "A": "Circulatory system",
                "B": "Respiratory system",
                "C": "Digestive system",
                "D": "Muscular system"
            },
            "correct": "C",
            "feedback_correct": "Correct! The digestive system breaks down food into nutrients that cells can use for energy and building materials.",
            "feedback_incorrect": "Not quite. The digestive system is responsible for breaking down food into nutrients. The circulatory system transports those nutrients, the respiratory system handles oxygen, and the muscular system enables movement."
        },
        {
            "question": "Can your body systems work independently, or do they depend on each other?",
            "choices": {
                "A": "Each system works independently without needing the others",
                "B": "Only the heart and lungs depend on each other",
                "C": "All body systems are interconnected and depend on each other to function",
                "D": "Systems only interact when the body is sick"
            },
            "correct": "C",
            "feedback_correct": "Correct! All body systems are interconnected. The digestive system provides nutrients, the respiratory system provides oxygen, the circulatory system delivers both, and the muscular system depends on all three.",
            "feedback_incorrect": "Not quite. All body systems are deeply interconnected. No system can function alone. For example, muscles need oxygen (from lungs) and nutrients (from digestion), both delivered by the circulatory system."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the body systems model, what happens when Physical Activity is set to maximum?",
            "choices": {
                "A": "Heart Rate decreases because the body relaxes",
                "B": "Heart Rate increases, Blood Oxygen drops, and Nutrient Intake demand rises",
                "C": "Only the muscular system is affected; other systems stay the same",
                "D": "Blood Oxygen increases because the lungs work faster"
            },
            "correct": "B",
            "feedback_correct": "Correct! Maximum physical activity causes the heart to beat faster (to deliver more blood), blood oxygen to drop (muscles consume it faster), and the body demands more nutrients for energy.",
            "feedback_incorrect": "Not quite. During intense activity, the heart rate increases to deliver more blood, blood oxygen drops because muscles consume it faster than lungs replace it, and the body demands more nutrients. All systems are affected."
        },
        {
            "question": "What is homeostasis and why is it important for body function?",
            "choices": {
                "A": "The process of building new muscles during exercise",
                "B": "The body's ability to maintain stable internal conditions despite changes in the external environment",
                "C": "The chemical reaction that converts food into energy",
                "D": "The way the immune system fights diseases"
            },
            "correct": "B",
            "feedback_correct": "Correct! Homeostasis is the body's ability to keep internal conditions stable, like temperature, blood oxygen, and nutrient levels, even when the outside environment changes. All organ systems contribute.",
            "feedback_incorrect": "Not quite. Homeostasis is the body's ability to maintain a stable internal environment. When you exercise, get cold, or skip a meal, your body systems work together to keep conditions balanced for cell survival."
        },
        {
            "question": "A student skips lunch and then tries to run the 400-meter dash. Based on the body systems model, what would happen?",
            "choices": {
                "A": "Performance would be normal because the body stores enough energy",
                "B": "Only the digestive system would be affected",
                "C": "Performance would decline because low nutrient intake limits energy production, affecting the muscular, circulatory, and respiratory systems",
                "D": "The student would run faster because the body is lighter without food"
            },
            "correct": "C",
            "feedback_correct": "Correct! Without adequate nutrients, cells can't produce enough energy for intense activity. This affects muscles (less power), the heart (must compensate), and breathing (increased demand). All systems are interconnected.",
            "feedback_incorrect": "Not quite. When nutrient intake is low, the body can't produce enough energy for intense physical activity. This cascades through all systems: muscles weaken, the heart must work harder, and breathing increases. Body systems are interconnected."
        },
        {
            "question": "Which statement best supports the claim that the body is a system of interacting subsystems?",
            "choices": {
                "A": "The skeletal system provides structure for the body",
                "B": "When the respiratory system fails to get enough oxygen, the circulatory system compensates by increasing heart rate, but muscles still decline",
                "C": "The skin is the largest organ in the body",
                "D": "Red blood cells carry oxygen through the bloodstream"
            },
            "correct": "B",
            "feedback_correct": "Correct! This example shows three systems interacting: the respiratory system's failure triggers a response in the circulatory system, and the muscular system is still affected. This chain reaction proves systems are interconnected.",
            "feedback_incorrect": "Not quite. The best evidence for interacting subsystems shows how changes in one system cause responses in other systems. When oxygen intake drops, the heart compensates by beating faster, but muscles still decline, proving the systems are interdependent."
        }
    ]
}

L07_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Where do plants get the energy they need to grow?",
            "choices": {
                "A": "From the soil through their roots",
                "B": "From sunlight through their leaves",
                "C": "From water in the ground",
                "D": "From other organisms they consume"
            },
            "correct": "B",
            "feedback_correct": "Correct! Plants capture light energy from the Sun using chlorophyll in their leaves and convert it into chemical energy through photosynthesis.",
            "feedback_incorrect": "Not quite. Plants get their energy from sunlight. Their leaves contain chlorophyll, a green pigment that captures light energy and uses it to power photosynthesis, the process of making food."
        },
        {
            "question": "What gas do plants take in from the air to make food?",
            "choices": {
                "A": "Oxygen",
                "B": "Nitrogen",
                "C": "Carbon dioxide",
                "D": "Hydrogen"
            },
            "correct": "C",
            "feedback_correct": "Correct! Plants absorb carbon dioxide (CO2) from the air through tiny pores in their leaves and use it as a carbon source during photosynthesis.",
            "feedback_incorrect": "Not quite. Plants take in carbon dioxide (CO2) from the air. They use the carbon atoms from CO2 to build sugar molecules during photosynthesis. Plants actually release oxygen as a byproduct."
        },
        {
            "question": "Where do you think the MASS of a large tree comes from?",
            "choices": {
                "A": "Mostly from the soil it grows in",
                "B": "Mostly from the water it absorbs",
                "C": "Mostly from the carbon dioxide in the air",
                "D": "Mostly from sunlight energy"
            },
            "correct": "C",
            "feedback_correct": "Correct! Most of a tree's mass comes from carbon dioxide in the air. Plants use carbon atoms from CO2 to build glucose, cellulose, and all the organic molecules that make up wood, bark, and leaves.",
            "feedback_incorrect": "Not quite. This is a common misconception! Most of a tree's mass actually comes from carbon dioxide in the air. The carbon atoms from CO2 are rearranged into sugars and other organic molecules that become the tree's wood, bark, and leaves."
        },
        {
            "question": "What is the role of the green color in plant leaves?",
            "choices": {
                "A": "It is just decoration to attract pollinators",
                "B": "It is a pigment called chlorophyll that captures light energy",
                "C": "It helps plants absorb water",
                "D": "It protects leaves from insects"
            },
            "correct": "B",
            "feedback_correct": "Correct! The green color comes from chlorophyll, a pigment that absorbs light energy (especially red and blue light) and uses it to power photosynthesis.",
            "feedback_incorrect": "Not quite. The green color in leaves is caused by chlorophyll, a pigment molecule that captures light energy from the Sun. This captured energy drives the chemical reactions of photosynthesis."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the photosynthesis model, what happens when Sunlight Intensity is locked at 20% while water and CO2 remain normal?",
            "choices": {
                "A": "The plant produces the same amount of glucose because water compensates",
                "B": "Glucose production drops significantly because light energy is the power source for the reaction",
                "C": "The plant switches to cellular respiration to make energy",
                "D": "Chlorophyll Amount increases automatically to capture more light"
            },
            "correct": "B",
            "feedback_correct": "Correct! Sunlight provides the energy that drives photosynthesis. Without sufficient light, the plant cannot convert CO2 and water into glucose, even if those inputs are abundant.",
            "feedback_incorrect": "Not quite. Sunlight is the energy source for photosynthesis. Even with plenty of water and CO2, the plant cannot make glucose without adequate light energy. All three inputs are essential."
        },
        {
            "question": "Which statement correctly explains why most of a tree's mass comes from the air and not the soil?",
            "choices": {
                "A": "Trees absorb tiny soil particles through their roots and build them into wood",
                "B": "Trees capture carbon from CO2 in the air and use photosynthesis to build carbon-based molecules like cellulose that form wood",
                "C": "Trees absorb water from rain, and water makes up most of the wood's weight",
                "D": "Sunlight energy becomes solid matter inside the tree"
            },
            "correct": "B",
            "feedback_correct": "Correct! During photosynthesis, trees take CO2 from the air and use light energy to rearrange the carbon atoms into glucose. That glucose is then converted into cellulose and other molecules that form wood, bark, and leaves.",
            "feedback_incorrect": "Not quite. Trees pull carbon dioxide out of the air and use photosynthesis to convert the carbon atoms into glucose molecules. Those glucose molecules are then used to build cellulose (wood fiber) and other structural molecules. The carbon in wood literally came from the air."
        },
        {
            "question": "How are photosynthesis and cellular respiration related?",
            "choices": {
                "A": "They are the same process happening in different cells",
                "B": "They are opposite reactions: photosynthesis builds glucose from CO2 and water, while respiration breaks glucose down into CO2 and water",
                "C": "Photosynthesis only happens in plants and respiration only happens in animals",
                "D": "They both require sunlight to function"
            },
            "correct": "B",
            "feedback_correct": "Correct! Photosynthesis and cellular respiration are balanced, opposite reactions. Photosynthesis uses light energy to build glucose from CO2 and water; respiration breaks glucose down to release energy, producing CO2 and water.",
            "feedback_incorrect": "Not quite. Photosynthesis and cellular respiration are reverse processes. Photosynthesis: CO2 + water + light -> glucose + O2. Respiration: glucose + O2 -> CO2 + water + energy. Plants actually do BOTH processes."
        },
        {
            "question": "A scientist grows two identical plants. Plant A receives normal CO2 levels, and Plant B is placed in a sealed chamber with very low CO2. After four weeks, Plant B has grown much less. What does this evidence support?",
            "choices": {
                "A": "CO2 is not important for plant growth",
                "B": "Plants need CO2 as a carbon source to build the molecules that make up their body mass",
                "C": "Plant B didn't grow because the sealed chamber blocked sunlight",
                "D": "Low CO2 caused the plant to overheat"
            },
            "correct": "B",
            "feedback_correct": "Correct! The plant with low CO2 grew less because CO2 provides the carbon atoms plants need to build glucose and other organic molecules. Without enough CO2, the plant cannot produce enough material to grow.",
            "feedback_incorrect": "Not quite. This experiment shows that CO2 is essential for plant growth. Carbon dioxide provides the carbon atoms that plants use to build glucose and structural molecules. Less CO2 means less raw material for growth."
        }
    ]
}

L08_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Which of these is an example of a natural hazard?",
            "choices": {
                "A": "A car accident on the highway",
                "B": "A hurricane making landfall on a coastal city",
                "C": "A building collapsing due to poor construction",
                "D": "Air pollution from a factory"
            },
            "correct": "B",
            "feedback_correct": "Correct! Natural hazards are naturally occurring events like hurricanes, earthquakes, floods, and wildfires that can threaten human life and property.",
            "feedback_incorrect": "Not quite. Natural hazards are events caused by natural processes, not human activity. Hurricanes, earthquakes, floods, tornadoes, and wildfires are all natural hazards."
        },
        {
            "question": "Why do you think some communities recover from natural disasters faster than others?",
            "choices": {
                "A": "Some places just get weaker storms",
                "B": "It depends on how well prepared the community is, including buildings, warning systems, and emergency plans",
                "C": "Wealthier communities always recover faster regardless of preparation",
                "D": "Recovery speed is completely random"
            },
            "correct": "B",
            "feedback_correct": "Correct! Community preparation, including building codes, early warning systems, evacuation plans, and emergency resources, is the biggest factor in how well a community survives and recovers from a disaster.",
            "feedback_incorrect": "Not quite. The level of preparation is the key factor. Communities with strong building codes, early warning systems, emergency plans, and trained responders survive disasters better and recover faster."
        },
        {
            "question": "Can scientists predict when and where natural disasters will happen?",
            "choices": {
                "A": "Yes, scientists can predict exact dates and locations of all disasters",
                "B": "No, natural disasters are completely unpredictable",
                "C": "Scientists can identify high-risk areas and patterns but cannot predict exact events",
                "D": "Only volcanic eruptions can be predicted"
            },
            "correct": "C",
            "feedback_correct": "Correct! Scientists use data on past events, geological features, and weather patterns to identify where hazards are likely and forecast general timeframes, but exact predictions remain very difficult.",
            "feedback_incorrect": "Not quite. Scientists can analyze data patterns to determine which areas are at highest risk for specific hazards and provide general forecasts, but they cannot predict exact dates and locations of most natural disasters."
        },
        {
            "question": "What does it mean to 'mitigate' a natural hazard?",
            "choices": {
                "A": "To prevent the hazard from ever happening",
                "B": "To take actions before a disaster to reduce its impact",
                "C": "To clean up after a disaster",
                "D": "To study the hazard in a laboratory"
            },
            "correct": "B",
            "feedback_correct": "Correct! Mitigation means actions taken BEFORE a disaster to reduce its impact, such as building levees, enforcing building codes, creating firebreaks, and developing warning systems.",
            "feedback_incorrect": "Not quite. Mitigation refers to proactive steps taken before a disaster to reduce the damage it causes. We cannot stop natural hazards, but we can reduce their impact through engineering and planning."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the natural hazards model, which factor most effectively reduces BOTH casualties AND property damage?",
            "choices": {
                "A": "Warning Time — giving people time to evacuate",
                "B": "Building Design — engineering structures to withstand hazards",
                "C": "Population Density — having fewer people in the area",
                "D": "Hazard Intensity — hoping for weaker storms"
            },
            "correct": "B",
            "feedback_correct": "Correct! Building Design is the only factor that protects both people AND property. Warning time saves lives through evacuation but can't move buildings. Well-designed structures survive the hazard and protect people inside.",
            "feedback_incorrect": "Not quite. While warning time helps evacuate people, it doesn't protect buildings. Building Design is the most effective factor for reducing both casualties AND property damage because strong buildings survive the hazard and protect people inside."
        },
        {
            "question": "The model shows that Warning Time dramatically reduces casualties but NOT property damage. Why?",
            "choices": {
                "A": "Warning systems are not accurate enough to help",
                "B": "People can be evacuated, but buildings and infrastructure cannot be moved out of the hazard's path",
                "C": "Property damage only happens during earthquakes, not other hazards",
                "D": "Warning time actually reduces property damage too"
            },
            "correct": "B",
            "feedback_correct": "Correct! Early warnings give people time to evacuate to safety, reducing deaths. But buildings, roads, and infrastructure stay in place and cannot be moved, so property damage remains the same regardless of warning time.",
            "feedback_incorrect": "Not quite. Warning systems help save lives because people can move to safety. However, buildings, bridges, power lines, and other infrastructure stay in place and absorb the full force of the hazard, so property damage is not reduced by warning time alone."
        },
        {
            "question": "Japan and Haiti both experience earthquakes, but Japan typically suffers far fewer deaths from similar-magnitude quakes. Based on the model, what explains this?",
            "choices": {
                "A": "Japan has weaker earthquakes than Haiti",
                "B": "Japan has invested heavily in earthquake-resistant building codes, early warning systems, and disaster preparedness training",
                "C": "Haiti has more people than Japan",
                "D": "Japan's earthquakes happen further from cities"
            },
            "correct": "B",
            "feedback_correct": "Correct! Japan has decades of investment in building codes requiring earthquake-resistant design, advanced seismic warning systems, and regular disaster preparedness training. These mitigation measures save thousands of lives.",
            "feedback_incorrect": "Not quite. The key difference is preparation. Japan has invested heavily in earthquake-resistant building codes, early warning technology, and citizen training. These mitigation measures dramatically reduce casualties even from powerful earthquakes."
        },
        {
            "question": "A city planner has a limited budget and must choose between upgrading building codes OR installing a new early warning system. Based on the model, which should they prioritize and why?",
            "choices": {
                "A": "Warning system, because it helps with all types of hazards equally",
                "B": "Building codes, because they reduce both casualties and property damage, while warning systems only reduce casualties",
                "C": "Neither, because no preparation can help against extreme hazards",
                "D": "Warning system, because it is always cheaper than building upgrades"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model shows building design reduces both casualties AND property damage. Warning systems save lives but not property. With a limited budget, building codes provide the most comprehensive protection.",
            "feedback_incorrect": "Not quite. According to the model, building design is the most effective single investment because it reduces both casualties and property damage. Warning systems are valuable for saving lives but don't protect infrastructure."
        }
    ]
}

L09_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is the difference between a natural material and a synthetic material?",
            "choices": {
                "A": "Natural materials are always better than synthetic ones",
                "B": "Natural materials come from the Earth; synthetic materials are made by humans through chemical processes",
                "C": "Synthetic materials are only used in laboratories",
                "D": "There is no difference — all materials are the same"
            },
            "correct": "B",
            "feedback_correct": "Correct! Natural materials (wood, cotton, stone) come directly from nature, while synthetic materials (plastic, nylon, polyester) are manufactured by humans through chemical processes.",
            "feedback_incorrect": "Not quite. Natural materials like wood, cotton, and stone come from the Earth as-is. Synthetic materials like plastic, nylon, and polyester are created by humans through chemical processes, often from natural resources like petroleum."
        },
        {
            "question": "What natural resource is most commonly used to make plastics?",
            "choices": {
                "A": "Sand",
                "B": "Wood",
                "C": "Petroleum (oil)",
                "D": "Water"
            },
            "correct": "C",
            "feedback_correct": "Correct! Most plastics are made from petroleum (crude oil), which is a natural resource formed from ancient organisms over millions of years.",
            "feedback_incorrect": "Not quite. Most plastics are manufactured from petroleum (crude oil). Petroleum contains hydrocarbon molecules that can be chemically rearranged into polymer chains that form plastic."
        },
        {
            "question": "Why do you think scientists create synthetic materials instead of just using natural ones?",
            "choices": {
                "A": "Synthetic materials are always cheaper",
                "B": "Natural materials have run out completely",
                "C": "Synthetic materials can be engineered to have specific properties that natural materials don't have",
                "D": "Scientists create synthetic materials just for fun"
            },
            "correct": "C",
            "feedback_correct": "Correct! Scientists engineer synthetic materials to have specific combinations of properties, like being lightweight AND strong, or flexible AND waterproof, that don't exist naturally.",
            "feedback_incorrect": "Not quite. The main reason for creating synthetic materials is that they can be precisely engineered to have specific properties. A single synthetic material can be lightweight, waterproof, flexible, and durable in ways that natural materials cannot."
        },
        {
            "question": "What is a polymer?",
            "choices": {
                "A": "A type of metal alloy",
                "B": "A very long chain of repeating smaller molecules linked together",
                "C": "A chemical that dissolves plastic",
                "D": "A mineral found in volcanic rock"
            },
            "correct": "B",
            "feedback_correct": "Correct! A polymer is a large molecule made of many smaller repeating units (monomers) linked together in a chain, like a molecular train. Plastics, nylon, and DNA are all polymers.",
            "feedback_incorrect": "Not quite. A polymer is a long chain molecule made of many small, repeating units (monomers) bonded together. Think of it like a train made of identical cars. Examples include plastics, rubber, nylon, and even DNA."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the synthetic materials model, what happens when Polymer Chain Length is increased from short to maximum?",
            "choices": {
                "A": "The material becomes weaker and more brittle",
                "B": "The material becomes stronger because longer chains tangle and hold together better",
                "C": "The material becomes more transparent",
                "D": "The material's melting point decreases"
            },
            "correct": "B",
            "feedback_correct": "Correct! Longer polymer chains create stronger materials because the chains become tangled with each other, creating more friction and connection points that resist pulling apart.",
            "feedback_incorrect": "Not quite. Longer polymer chains produce stronger materials. This is because long chains get tangled and intertwined, creating many points of contact that hold the material together, similar to how long strands of spaghetti tangle more than short pieces."
        },
        {
            "question": "How can the SAME base polymer be made into either a rigid plastic container or a flexible plastic wrap?",
            "choices": {
                "A": "By painting it different colors",
                "B": "By adding chemical additives like plasticizers that change its flexibility",
                "C": "By heating it to different temperatures during use",
                "D": "They are actually made from completely different polymers"
            },
            "correct": "B",
            "feedback_correct": "Correct! Chemical additives, especially plasticizers, can dramatically change a polymer's properties. Plasticizers insert between polymer chains, allowing them to slide more easily and making the material flexible.",
            "feedback_incorrect": "Not quite. Chemical additives like plasticizers can completely change a material's properties. Plasticizers work by inserting between polymer chains, allowing them to move more freely. This turns a rigid plastic into a flexible film without changing the base polymer."
        },
        {
            "question": "Why is it accurate to say that 'your sneakers are made of dinosaurs'?",
            "choices": {
                "A": "Scientists extract DNA from dinosaur bones to make plastic",
                "B": "Sneaker materials come from petroleum, which formed from the remains of ancient organisms that lived alongside dinosaurs",
                "C": "Dinosaur fossils are ground up to make rubber soles",
                "D": "Sneakers are shaped like dinosaur feet for better grip"
            },
            "correct": "B",
            "feedback_correct": "Correct! Petroleum formed from ancient organisms (plankton, algae, and other life from the dinosaur era) that were buried and transformed over millions of years. The synthetic materials in sneakers are manufactured from this petroleum.",
            "feedback_incorrect": "Not quite. Petroleum, the primary raw material for most plastics and synthetic materials in sneakers, formed from the remains of ancient organisms that lived during and before the age of dinosaurs. Over millions of years, those organisms became the oil we refine into plastics."
        },
        {
            "question": "A materials engineer needs a synthetic material that is both strong AND lightweight for airplane parts. Based on the model, which combination of properties should they target?",
            "choices": {
                "A": "Short polymer chains with maximum plasticizer additives",
                "B": "Long polymer chains with optimal heat treatment and minimal heavy additives",
                "C": "Maximum concentration of every additive available",
                "D": "Short polymer chains with no heat treatment"
            },
            "correct": "B",
            "feedback_correct": "Correct! Long polymer chains provide strength through tangling, optimal heat treatment organizes chains into strong crystalline structures, and minimizing heavy additives keeps the material lightweight.",
            "feedback_incorrect": "Not quite. For strong AND lightweight material: long polymer chains create strength through tangling, optimal heat treatment organizes chains into crystalline structures for additional strength, and avoiding heavy additives keeps the weight down."
        }
    ]
}

L10_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is an ecosystem?",
            "choices": {
                "A": "A collection of only animals in one area",
                "B": "A community of living organisms interacting with each other and their nonliving environment",
                "C": "A zoo where different species are kept together",
                "D": "Any area with plants growing in it"
            },
            "correct": "B",
            "feedback_correct": "Correct! An ecosystem includes all living things (plants, animals, fungi, bacteria) AND nonliving things (water, soil, sunlight, air) in an area, plus all their interactions.",
            "feedback_incorrect": "Not quite. An ecosystem is a complete community of living organisms (plants, animals, decomposers) interacting with each other AND with the nonliving parts of their environment (water, soil, sunlight, temperature)."
        },
        {
            "question": "What happens to a prey population if all the predators are removed from an ecosystem?",
            "choices": {
                "A": "The prey population stays the same",
                "B": "The prey population grows without limit forever",
                "C": "The prey population grows rapidly at first, but eventually runs out of food and crashes",
                "D": "The prey population decreases because they need predators to survive"
            },
            "correct": "C",
            "feedback_correct": "Correct! Without predators, prey populations grow rapidly. But eventually they exceed the carrying capacity, consuming all available food and resources, leading to a population crash.",
            "feedback_incorrect": "Not quite. Without predators to control their numbers, prey populations initially explode. But they eventually eat all the available food and overshoot the carrying capacity, leading to starvation and a dramatic population crash."
        },
        {
            "question": "Why is biodiversity (having many different species) important for an ecosystem?",
            "choices": {
                "A": "It makes the ecosystem look more interesting",
                "B": "It doesn't matter — only the largest animals are important",
                "C": "More species means the ecosystem is more stable and can recover from disturbances",
                "D": "Biodiversity only matters in tropical rainforests"
            },
            "correct": "C",
            "feedback_correct": "Correct! High biodiversity makes ecosystems more resilient. When there are many species, the loss of one has less impact because other species can fill similar roles, keeping the system functioning.",
            "feedback_incorrect": "Not quite. Biodiversity makes ecosystems stronger and more resilient. Diverse ecosystems have more species filling different roles, so if one species declines, others can compensate. This stability helps ecosystems recover from disturbances."
        },
        {
            "question": "In a food chain, what is the role of a decomposer?",
            "choices": {
                "A": "To hunt and eat other animals",
                "B": "To produce food using sunlight",
                "C": "To break down dead organisms and recycle nutrients back into the ecosystem",
                "D": "To pollinate flowers and spread seeds"
            },
            "correct": "C",
            "feedback_correct": "Correct! Decomposers like fungi and bacteria break down dead organisms and waste, recycling nutrients back into the soil where plants can use them again. They close the loop in nutrient cycling.",
            "feedback_incorrect": "Not quite. Decomposers break down dead organisms and waste material, returning nutrients to the soil. This nutrient recycling is essential because it allows producers (plants) to grow, keeping the food chain going."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the ecosystem model, what pattern do predator and prey populations follow over time in a balanced ecosystem?",
            "choices": {
                "A": "Both populations remain constant and never change",
                "B": "Predators and prey cycle: prey increases, then predators increase, then prey decreases, then predators decrease",
                "C": "Predators always increase while prey always decrease",
                "D": "Populations change randomly with no predictable pattern"
            },
            "correct": "B",
            "feedback_correct": "Correct! Predator-prey populations follow a natural cycle. More prey means more food for predators, so predators increase. More predators means more prey eaten, so prey decreases. Then predators decline from lack of food, and the cycle repeats.",
            "feedback_incorrect": "Not quite. Predator and prey populations follow a cyclical pattern. When prey is abundant, predators thrive and increase. This increased predation causes prey to decline, which then causes predators to decline from food scarcity. With fewer predators, prey recovers, and the cycle repeats."
        },
        {
            "question": "In the model, when Predator Population is locked at zero, the prey population initially explodes but then crashes. What causes the crash?",
            "choices": {
                "A": "Disease spreads faster in large populations",
                "B": "Without predators, prey overshoot carrying capacity by consuming all available resources, leading to starvation",
                "C": "New predators evolve to replace the removed ones",
                "D": "The prey migrate to a different ecosystem"
            },
            "correct": "B",
            "feedback_correct": "Correct! Without predators controlling their numbers, prey populations grow beyond what the habitat can support (carrying capacity). They deplete food and resources, leading to mass starvation and a population crash.",
            "feedback_incorrect": "Not quite. Without predators, prey populations grow unchecked past the environment's carrying capacity. They consume all available food and resources, and when resources are depleted, the population crashes due to starvation."
        },
        {
            "question": "When Habitat Size is reduced to 25% in the model, what happens to BOTH predator and prey populations?",
            "choices": {
                "A": "Both populations stay the same but are more crowded",
                "B": "Only prey populations decline because they need more space",
                "C": "Both populations decline because reduced habitat means reduced carrying capacity for all species",
                "D": "Predator populations increase because prey are easier to catch in a smaller area"
            },
            "correct": "C",
            "feedback_correct": "Correct! Reducing habitat shrinks the carrying capacity for ALL species. Less habitat means less food, water, and shelter, so both predator and prey populations decline. The smallest populations are pushed toward extinction first.",
            "feedback_incorrect": "Not quite. Habitat loss reduces the carrying capacity for every species in the ecosystem. With only 25% of the original habitat, there is less food, water, and shelter to support populations. Both predator and prey populations decline."
        },
        {
            "question": "A nature preserve has lost most of its wolves, and deer populations have exploded, overgrazing vegetation and degrading streams. Based on the model, which intervention would be most effective?",
            "choices": {
                "A": "Plant more trees to increase food supply for deer",
                "B": "Build fences to keep deer in one area",
                "C": "Reintroduce wolves to restore the predator-prey balance and allow vegetation to recover",
                "D": "Remove all deer and start over with new animals"
            },
            "correct": "C",
            "feedback_correct": "Correct! Reintroducing predators restores the natural predator-prey cycle. With wolves present, deer populations are controlled, allowing vegetation to recover. This is exactly what happened when wolves were reintroduced to Yellowstone National Park.",
            "feedback_incorrect": "Not quite. The most effective intervention is reintroducing wolves to restore the predator-prey balance. This is a real-world example: when wolves were returned to Yellowstone, deer populations stabilized, vegetation recovered, and the entire ecosystem improved."
        }
    ]
}

# ─── Master dictionary ───────────────────────────────────────────────────────

ALL_QUESTIONS = {
    "G06-L01": L01_QUESTIONS,
    "G06-L02": L02_QUESTIONS,
    "G06-L03": L03_QUESTIONS,
    "G06-L04": L04_QUESTIONS,
    "G06-L05": L05_QUESTIONS,
    "G06-L06": L06_QUESTIONS,
    "G06-L07": L07_QUESTIONS,
    "G06-L08": L08_QUESTIONS,
    "G06-L09": L09_QUESTIONS,
    "G06-L10": L10_QUESTIONS,
}
