#!/usr/bin/env python3
"""Multiple choice pre/post assessment questions for Grade 4 Level 2 ModelIt! Lessons"""

# =============================================================================
# G04L2-L01: The Energy Roller Coaster: Where Does Speed Come From?
# NGSS 4-PS3-1, 4-PS3-4: Energy transformation, friction, and conservation
# =============================================================================
L01_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "A roller coaster starts at the top of a tall hill and rolls down to the bottom. What happens to its potential energy and kinetic energy during the ride down?",
            "choices": {
                "A": "Both potential energy and kinetic energy increase together",
                "B": "Potential energy decreases while kinetic energy increases",
                "C": "Potential energy increases while kinetic energy decreases",
                "D": "Both potential energy and kinetic energy stay the same"
            },
            "correct": "B",
            "feedback_correct": "That is right! As the coaster rolls downhill, its stored potential energy transforms into kinetic energy. The higher the starting hill, the more kinetic energy the coaster gains at the bottom.",
            "feedback_incorrect": "Think about what changes as the coaster moves downhill. It loses height (so potential energy decreases) and gains speed (so kinetic energy increases). Energy transforms from one form to the other."
        },
        {
            "question": "In the model, Hill Height and Track Friction are external components. Why are they external?",
            "choices": {
                "A": "Because they are the biggest components in the model",
                "B": "Because they are located outside the roller coaster car",
                "C": "Because they are design choices we can control before the ride starts",
                "D": "Because they do not affect the coaster's speed"
            },
            "correct": "C",
            "feedback_correct": "Correct! External components are things we can set or control. Engineers decide how tall to build the hill and what surface material to use for the track before the coaster starts moving.",
            "feedback_incorrect": "In a model, external components are things we can control or decide. Hill Height and Track Friction are choices engineers make when designing the ride, so they are external."
        },
        {
            "question": "The model shows that when Track Friction increases, Heat Loss increases, and Kinetic Energy decreases. What does this tell us about friction?",
            "choices": {
                "A": "Friction creates new energy that makes the coaster go faster",
                "B": "Friction destroys the coaster's energy so it disappears completely",
                "C": "Friction transforms kinetic energy into heat, leaving less energy for motion",
                "D": "Friction has no effect on how fast the coaster moves"
            },
            "correct": "C",
            "feedback_correct": "Exactly! Friction transforms motion energy into heat energy. The energy is not destroyed, it just changes form. With more energy going to heat, less is available for speed.",
            "feedback_incorrect": "Energy is never created or destroyed. Friction transforms kinetic energy (motion) into heat energy. That heat escapes into the air, so less energy is left to keep the coaster moving fast."
        },
        {
            "question": "A student tests two roller coasters. Coaster A has a tall hill and a smooth track. Coaster B has the same tall hill but a rough track. Which coaster will be faster at the bottom, and why?",
            "choices": {
                "A": "Coaster B, because rough tracks push the coaster forward harder",
                "B": "They will be the same speed because they start from the same height",
                "C": "Coaster A, because less friction means less energy is lost to heat, so more energy stays as kinetic energy",
                "D": "Coaster B, because friction adds extra energy to the system"
            },
            "correct": "C",
            "feedback_correct": "Right! Both coasters start with the same potential energy, but Coaster A's smooth track loses less energy to heat. More energy stays as kinetic energy, so Coaster A is faster at the bottom.",
            "feedback_incorrect": "Both coasters start with the same potential energy from the same hill height. The difference is friction. The smooth track (Coaster A) converts less energy to heat, so more energy remains as speed."
        },
        {
            "question": "The relationship between Heat Loss and Kinetic Energy is NEGATIVE. What does a negative relationship mean in this model?",
            "choices": {
                "A": "Heat Loss and Kinetic Energy both decrease at the same time",
                "B": "When Heat Loss increases, Kinetic Energy decreases because energy going to heat cannot also be used for motion",
                "C": "The relationship is bad for the roller coaster so scientists call it negative",
                "D": "Heat Loss and Kinetic Energy are not connected to each other"
            },
            "correct": "B",
            "feedback_correct": "That is right! A negative relationship means when one goes up, the other goes down. More energy lost as heat means less energy available for speed. Energy is conserved, so it can only be in one form at a time.",
            "feedback_incorrect": "A negative relationship in a model means the two components move in opposite directions. When Heat Loss goes up, Kinetic Energy goes down because the total energy is conserved and energy spent as heat cannot also power motion."
        }
    ]
}

# =============================================================================
# G04L2-L02: Can Sound Travel Through Space?
# NGSS 4-PS4-1, 4-PS4-3: Sound waves, media, and information transfer
# =============================================================================
L02_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "An astronaut in space watches a satellite explode 50 meters away. What does the astronaut hear?",
            "choices": {
                "A": "A very loud boom because explosions are always loud",
                "B": "A quiet boom because the sound gets weaker in space",
                "C": "Nothing at all, because sound cannot travel through the vacuum of space",
                "D": "A delayed boom because sound travels slowly in space"
            },
            "correct": "C",
            "feedback_correct": "Correct! Space is a vacuum with no molecules. Sound waves need molecules to vibrate and carry the wave from one place to another. With no medium, there is no sound at all.",
            "feedback_incorrect": "Sound needs a medium (air, water, or a solid) to travel through. Space is a vacuum with almost no molecules. Without molecules to vibrate and pass the wave along, sound simply cannot exist in space."
        },
        {
            "question": "In the model, Vibration Strength and Medium Density are external components. What makes them external?",
            "choices": {
                "A": "They are the loudest parts of the model",
                "B": "They are conditions we can set or control, and the other components respond to them",
                "C": "They happen outside of the classroom",
                "D": "They are the parts of the model that do not change"
            },
            "correct": "B",
            "feedback_correct": "Right! External components are inputs we can control. We decide how hard to hit a drum (Vibration Strength) and what material the sound travels through (Medium Density). The internal components respond to those choices.",
            "feedback_incorrect": "In a model, external components are things we can set or control before running the system. Vibration Strength (how hard the source vibrates) and Medium Density (what the sound travels through) are choices we make, and everything else responds."
        },
        {
            "question": "The model shows that when Medium Density increases (from air to water to steel), Wave Speed also increases. Which best explains why?",
            "choices": {
                "A": "Denser materials are heavier, so they push sound waves forward with more force",
                "B": "In denser materials, molecules are packed closer together, so each molecule bumps into the next one faster",
                "C": "Sound creates its own molecules in denser materials",
                "D": "Denser materials have less friction, so sound slides through them easily"
            },
            "correct": "B",
            "feedback_correct": "Exactly! In denser materials like water and steel, molecules are packed tightly together. When one molecule vibrates, it quickly bumps the next one, passing the sound wave along faster.",
            "feedback_incorrect": "Sound travels by molecules bumping into each other. In denser materials, the molecules are closer together, so each vibration reaches the next molecule faster. That is why sound in steel is about 15 times faster than in air."
        },
        {
            "question": "The relationship between Wave Absorption and Sound Loudness is NEGATIVE. What does this mean for how loud a sound is when it reaches you?",
            "choices": {
                "A": "When absorption increases, loudness also increases because the medium amplifies the sound",
                "B": "Absorption and loudness always stay the same no matter what",
                "C": "When absorption increases, loudness decreases because more sound energy is soaked up before reaching the listener",
                "D": "Absorption only affects pitch, not loudness"
            },
            "correct": "C",
            "feedback_correct": "That is right! When a material absorbs more sound energy, less energy reaches your ears, so the sound is quieter. This is why whale songs travel far in water (low absorption) but shouts fade quickly in air (higher absorption).",
            "feedback_incorrect": "A negative relationship means when one goes up, the other goes down. When Wave Absorption increases, more sound energy is soaked up by the material, so less energy reaches the listener and the sound is quieter."
        },
        {
            "question": "A student sets Medium Density to 0% in the model, representing the vacuum of space. What happens to ALL the internal components?",
            "choices": {
                "A": "Wave Speed increases because there is nothing to slow the sound down",
                "B": "Sound Loudness increases because there is nothing to absorb the sound",
                "C": "All internal components drop to zero because there are no molecules to carry the sound wave",
                "D": "Wave Speed stays the same but Sound Loudness decreases slightly"
            },
            "correct": "C",
            "feedback_correct": "Correct! With no molecules at all, there is nothing to vibrate, nothing to carry a wave, and nothing to absorb. Every internal component drops to zero. This proves that sound absolutely requires a medium.",
            "feedback_incorrect": "When there are zero molecules (a vacuum), sound cannot exist at all. There is nothing to vibrate, nothing to carry a wave, and no sound to absorb. All internal components go to zero because sound requires a medium."
        }
    ]
}

# =============================================================================
# G04L2-L03: Why Do Some Animals Survive Winter?
# NGSS 4-LS1-1, 4-LS1-2: Internal/external structures for survival
# =============================================================================
L03_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "An arctic fox has thick fur and a layer of fat under its skin. How do these features help it survive freezing temperatures?",
            "choices": {
                "A": "They make the fox heavier so it does not blow away in the wind",
                "B": "They provide insulation that slows down heat loss, so the fox's body does not have to burn energy as fast to stay warm",
                "C": "They help the fox run faster to escape predators in the snow",
                "D": "They absorb sunlight and convert it into body heat"
            },
            "correct": "B",
            "feedback_correct": "That is right! Fur and fat act as insulation, keeping body heat from escaping. This means the fox's metabolic rate does not have to spike as high, saving precious energy during winter.",
            "feedback_incorrect": "Fur and fat are insulation. Insulation slows down heat loss from the body. When less heat escapes, the animal's body does not need to burn energy as fast (lower metabolic rate) to maintain its temperature."
        },
        {
            "question": "In the model, Temperature and Food Availability are external components. Why are these external rather than internal?",
            "choices": {
                "A": "Because they happen outside the animal's body",
                "B": "Because they are environmental conditions the animal cannot control, and the other components respond to them",
                "C": "Because they are the most important parts of the model",
                "D": "Because they never change during winter"
            },
            "correct": "B",
            "feedback_correct": "Correct! External components are the inputs or conditions that drive the system. An animal cannot control the weather or how much food exists in the environment. The internal components (Body Insulation, Metabolic Rate, Survival Chance) respond to these conditions.",
            "feedback_incorrect": "External components in a model are the conditions or inputs we set. Temperature and Food Availability are things the animal cannot control. The internal components (insulation, metabolic rate, survival chance) change in response to them."
        },
        {
            "question": "The model shows that when Temperature drops, Metabolic Rate increases. This is a NEGATIVE relationship. Why does the animal's body burn energy faster in the cold?",
            "choices": {
                "A": "Because cold temperatures make food taste better, so the animal eats more",
                "B": "Because the body must generate more heat to maintain a safe internal temperature when it is cold outside",
                "C": "Because cold temperatures make the animal's muscles stronger",
                "D": "Because metabolic rate always increases no matter what the temperature is"
            },
            "correct": "B",
            "feedback_correct": "Exactly! Warm-blooded animals must keep their body temperature constant. When it is freezing outside, the body works harder (burns more energy) to produce heat and stay warm. This is why cold weather demands more food energy.",
            "feedback_incorrect": "Warm-blooded animals need to maintain a constant body temperature. In cold conditions, heat escapes from the body faster, so the body must burn energy faster (higher metabolic rate) to generate enough heat to survive."
        },
        {
            "question": "A student runs the model with Temperature at 10% and Food Availability at 20%. Survival Chance drops very low. Which best explains why?",
            "choices": {
                "A": "The animal is too cold to move, so it cannot find shelter",
                "B": "Cold temperatures raise the metabolic rate, but there is not enough food to fuel that high energy demand, so the animal runs out of energy",
                "C": "Low food availability makes the temperature feel even colder",
                "D": "The animal's insulation disappears when food is scarce"
            },
            "correct": "B",
            "feedback_correct": "Right! Extreme cold forces the metabolic rate up, meaning the body burns energy very fast. But with very little food, the animal cannot replace that energy. It burns through its reserves and survival chance drops. This is the deadly combination.",
            "feedback_incorrect": "In the model, cold temperatures increase metabolic rate (the body burns energy faster to stay warm). When Food Availability is also low, the animal cannot get enough energy to fuel that high burn rate, and it depletes its reserves."
        },
        {
            "question": "The model shows that Body Insulation has a NEGATIVE relationship with Metabolic Rate. How does better insulation help an animal survive?",
            "choices": {
                "A": "Better insulation makes the animal lighter so it uses less energy moving around",
                "B": "Better insulation traps body heat inside, so the body does not need to burn as much energy to stay warm, leaving more energy available for survival",
                "C": "Better insulation makes food last longer by keeping it frozen",
                "D": "Better insulation raises the temperature around the animal"
            },
            "correct": "B",
            "feedback_correct": "That is right! When insulation keeps heat from escaping, the body does not have to work as hard (lower metabolic rate) to maintain its temperature. This means the animal uses less energy and can survive longer on less food.",
            "feedback_incorrect": "Insulation slows down heat loss. When less heat escapes, the body does not have to burn energy as fast to stay warm. A lower metabolic rate means the animal's energy reserves last longer, improving survival chance."
        }
    ]
}

# =============================================================================
# G04L2-L04: The Mountain That Used to Be an Ocean
# NGSS 4-ESS1-1, 4-ESS2-1: Rock formations, fossils, and landscape change
# =============================================================================
L04_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "Scientists find fossils of ocean creatures on top of a mountain that is thousands of feet above sea level. How did those fossils get there?",
            "choices": {
                "A": "Ocean animals climbed up the mountain millions of years ago",
                "B": "A giant wave carried the fossils to the mountaintop",
                "C": "Tectonic plate collisions pushed ancient ocean floor rock upward over millions of years, carrying the fossils with it",
                "D": "People carried the fossils up the mountain and left them there"
            },
            "correct": "C",
            "feedback_correct": "Correct! The rock at the top of mountains like the Himalayas was once ocean floor. Tectonic plates collided and the compression force pushed that ocean floor upward over millions of years, bringing the fossils along.",
            "feedback_incorrect": "These fossils were not carried or moved by animals or waves. The rock itself was pushed upward. Tectonic plates colliding created compression forces that slowly lifted ancient ocean floor (with its fossils) into mountains over millions of years."
        },
        {
            "question": "In the model, Plate Movement Speed and Sediment Deposit Rate are external components. What does this mean?",
            "choices": {
                "A": "They are the newest parts of the model",
                "B": "They are the starting conditions that drive the system, and the internal components respond to them",
                "C": "They happen on the outside surface of the Earth",
                "D": "They can be turned off to stop the model"
            },
            "correct": "B",
            "feedback_correct": "Right! External components are the inputs that drive the system. Plate Movement Speed determines how fast plates collide, and Sediment Deposit Rate determines how thick the fossil layers are. Everything else responds to these.",
            "feedback_incorrect": "In a model, external components are the conditions or inputs that the rest of the system responds to. Plate Movement Speed and Sediment Deposit Rate are the driving forces that determine what happens to compression, uplift, and fossil elevation."
        },
        {
            "question": "The model shows that Plate Movement Speed has a POSITIVE relationship with Compression Force. What does this mean?",
            "choices": {
                "A": "Faster plate movement creates weaker compression because the plates slide past each other",
                "B": "Plate Movement Speed and Compression Force are not related",
                "C": "When Plate Movement Speed increases, Compression Force also increases because faster collisions push harder",
                "D": "Compression Force stays the same no matter how fast the plates move"
            },
            "correct": "C",
            "feedback_correct": "Exactly! A positive relationship means both go up together. Faster-moving plates crash into each other with more energy, creating stronger compression forces that squeeze and fold rock more powerfully.",
            "feedback_incorrect": "A positive relationship means when one increases, the other increases too. Faster plate movement means more energy in the collision, which creates stronger compression forces that squeeze the rock layers."
        },
        {
            "question": "A student sets Plate Movement Speed to 0% in the model. What happens to all the internal components?",
            "choices": {
                "A": "Compression Force, Rock Uplift, and Fossil Elevation all continue increasing on their own",
                "B": "Compression Force drops to zero, Rock Uplift stops, and Fossil Elevation stays where it is",
                "C": "The fossils sink back down to the ocean floor",
                "D": "Sediment Deposit Rate increases to make up for the missing plate movement"
            },
            "correct": "B",
            "feedback_correct": "That is right! Without plate movement, there is no collision and no compression force. Without compression, there is no uplift. The fossils stay at whatever elevation they have already reached. Mountains stop growing.",
            "feedback_incorrect": "When plates stop moving, there is no collision energy. Compression Force drops to zero because nothing is pushing. Without compression, Rock Uplift stops. Fossil Elevation stays at its current level because there is no force to push it higher."
        },
        {
            "question": "The model has two external components that both contribute to where fossils end up. Why do you need BOTH thick sediment layers AND strong plate movement to find many ocean fossils on mountaintops?",
            "choices": {
                "A": "Thick sediment makes the plates move faster",
                "B": "Plate movement creates the fossils and sediment carries them upward",
                "C": "Thick sediment layers contain the fossils, and plate movement creates the compression and uplift that pushes those layers to high elevations",
                "D": "Neither one matters because fossils always end up at the same elevation"
            },
            "correct": "C",
            "feedback_correct": "Correct! Sediment layers are where the fossils are trapped (more sediment means more fossils). Plate movement creates the compression and uplift that pushes those layers skyward. Without both, you either have no fossils to lift or no force to lift them.",
            "feedback_incorrect": "Both components play different roles. Sediment Deposit Rate determines how many fossil-containing layers build up on the ocean floor. Plate Movement Speed creates the compression and uplift forces that push those layers to high elevations. You need both."
        }
    ]
}

# =============================================================================
# G04L2-L05: Can We Power a City with Wind?
# NGSS 4-ESS3-1, 4-PS3-1: Renewable energy and energy resources
# =============================================================================
L05_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "Wind turbines convert one form of energy into another. What energy transformation happens inside a wind turbine?",
            "choices": {
                "A": "Heat energy from the sun is converted into wind energy",
                "B": "The kinetic energy of moving air is converted into electrical energy",
                "C": "Electrical energy is converted into wind energy to make the blades spin",
                "D": "Sound energy from the wind is converted into light energy"
            },
            "correct": "B",
            "feedback_correct": "That is right! Wind turbines capture the kinetic energy (motion energy) of the wind. As the blades spin, generators inside convert that motion into electrical energy that can power homes and schools.",
            "feedback_incorrect": "Wind turbines do not create wind or use electricity to spin. They work the other way around. Moving air (kinetic energy) pushes the blades, and generators inside the turbine convert that motion into electricity."
        },
        {
            "question": "In the model, Wind Speed and Number of Turbines are external components. Why are these considered external?",
            "choices": {
                "A": "Because they are located outside in the wind farm",
                "B": "Because they are conditions or design choices that determine how the rest of the system behaves",
                "C": "Because they are the smallest parts of the system",
                "D": "Because they respond to changes in Electricity Generated"
            },
            "correct": "B",
            "feedback_correct": "Correct! External components are the inputs we set. Wind Speed is the environmental condition, and Number of Turbines is the design choice. The internal components (Electricity Generated, City Energy Demand, Grid Reliability) respond to these inputs.",
            "feedback_incorrect": "External components are the inputs or starting conditions that drive the system. Wind Speed is a natural condition, and Number of Turbines is an engineering decision. The internal components change in response to these."
        },
        {
            "question": "The model shows that City Energy Demand has a NEGATIVE relationship with Grid Reliability. What does this mean for a city?",
            "choices": {
                "A": "When the city uses more energy, the grid becomes more reliable because more power flows through it",
                "B": "When City Energy Demand increases but electricity supply stays the same, Grid Reliability decreases because demand outpaces supply",
                "C": "City Energy Demand and Grid Reliability always move in the same direction",
                "D": "Grid Reliability has nothing to do with how much energy the city needs"
            },
            "correct": "B",
            "feedback_correct": "Exactly! A negative relationship means when one goes up, the other goes down. If the city needs more power but the turbines are not producing enough, the gap between supply and demand grows, making blackouts more likely.",
            "feedback_incorrect": "A negative relationship means the two move in opposite directions. When City Energy Demand goes up but supply does not match it, Grid Reliability goes down. The grid becomes unstable when demand exceeds what the turbines can produce."
        },
        {
            "question": "A student runs the model with Wind Speed at 15% and Number of Turbines at 80%. Grid Reliability drops very low. What does this tell us about wind energy?",
            "choices": {
                "A": "Wind energy does not work because turbines are too expensive",
                "B": "Having many turbines guarantees reliable power for the city",
                "C": "Wind energy is intermittent, so even many turbines produce very little electricity on calm days, causing the supply to fall below the city's demand",
                "D": "The turbines broke because the wind was too weak to spin them"
            },
            "correct": "C",
            "feedback_correct": "Right! This is the core challenge of wind energy. Wind is intermittent, meaning it does not blow constantly. Even 100 turbines produce almost nothing on a calm day, but the city still needs power for hospitals, schools, and homes.",
            "feedback_incorrect": "The turbines did not break. The problem is that wind energy depends on the wind blowing. When wind is weak, turbines produce very little electricity no matter how many you have. Cities need power 24/7, but wind is not constant."
        },
        {
            "question": "Based on the model, why can wind energy alone NOT reliably power a whole city?",
            "choices": {
                "A": "Wind turbines are too small to make enough electricity",
                "B": "Wind is free, so the city would not make any money from it",
                "C": "Wind speed changes constantly, so electricity generation goes up and down while the city's demand stays high, causing blackouts on calm days",
                "D": "Wind energy only works at night when people are sleeping"
            },
            "correct": "C",
            "feedback_correct": "That is right! The model shows that Grid Reliability depends on supply matching demand. Wind speed is unpredictable and intermittent, so generation fluctuates. On calm days, supply drops far below demand. That is why wind works best as part of an energy mix with solar, batteries, or other sources.",
            "feedback_incorrect": "The model reveals that the biggest problem is reliability. Cities need constant power, but wind does not blow constantly. When wind speed drops, electricity generation drops too, creating a gap between supply and demand that causes blackouts."
        }
    ]
}

# =============================================================================
# G04L2-L06: Building for the Big One: Earthquake Engineering Lab
# NGSS 4-ESS3-2, 4-ETS1-2: Reducing impacts of natural hazards, engineering
# =============================================================================
L06_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "During an earthquake, a flexible building sways back and forth but does not collapse, while a rigid building next to it cracks and crumbles. Why does the flexible building survive?",
            "choices": {
                "A": "The flexible building is lighter, so the earthquake cannot reach it",
                "B": "The flexible building moves WITH the earthquake, absorbing and distributing the shaking energy instead of fighting against it",
                "C": "The flexible building is built with stronger materials that cannot be damaged",
                "D": "The earthquake was weaker on the side where the flexible building stood"
            },
            "correct": "B",
            "feedback_correct": "Correct! Flexible buildings survive because they sway, bend, and absorb shaking energy. Like a living tree bending in a storm instead of snapping, flexible buildings move with the earthquake rather than resisting it.",
            "feedback_incorrect": "Both buildings experienced the same earthquake. The difference is how they respond to shaking. Flexible buildings absorb and distribute the force by bending and swaying. Rigid buildings try to resist, and the force overwhelms them, causing cracks and collapse."
        },
        {
            "question": "In the model, Earthquake Magnitude and Building Flexibility are external components. Why?",
            "choices": {
                "A": "Because they are the most dangerous parts of the model",
                "B": "Because they are the starting conditions, one natural and one engineered, that determine what happens to the internal components",
                "C": "Because they happen outside the building",
                "D": "Because they cannot be measured by scientists"
            },
            "correct": "B",
            "feedback_correct": "Right! Earthquake Magnitude is a natural condition we cannot control, and Building Flexibility is an engineering design choice. Together, these external inputs determine the Shaking Force, Structural Damage, and Occupant Safety inside the system.",
            "feedback_incorrect": "External components are the inputs that drive the system. Earthquake Magnitude is a natural event, and Building Flexibility is a design choice. The internal components (Shaking Force, Structural Damage, Occupant Safety) all respond to these two inputs."
        },
        {
            "question": "The model shows that Building Flexibility has a NEGATIVE relationship with Structural Damage. What does this mean for earthquake engineering?",
            "choices": {
                "A": "More flexible buildings cause more damage during earthquakes",
                "B": "Building Flexibility and Structural Damage always increase together",
                "C": "When Building Flexibility increases, Structural Damage decreases because the building absorbs shaking energy instead of cracking",
                "D": "Flexibility has no effect on how much damage a building takes"
            },
            "correct": "C",
            "feedback_correct": "Exactly! A negative relationship means when one goes up, the other goes down. More flexibility means less damage because the building can bend and sway to absorb the earthquake's energy without breaking apart.",
            "feedback_incorrect": "A negative relationship means the two move in opposite directions. When Building Flexibility increases, Structural Damage decreases. The building absorbs and distributes shaking energy by flexing rather than cracking."
        },
        {
            "question": "A student compares two scenarios: a magnitude 90% earthquake hitting a building with 20% flexibility versus the same earthquake hitting a building with 80% flexibility. What difference would the model show?",
            "choices": {
                "A": "Both buildings would have the same damage because the earthquake is the same strength",
                "B": "The rigid building (20% flexibility) would have much more Structural Damage and much lower Occupant Safety than the flexible building (80% flexibility)",
                "C": "The flexible building would have more damage because bending weakens the structure",
                "D": "Neither building would be damaged because modern buildings are always safe"
            },
            "correct": "B",
            "feedback_correct": "Right! Even though the earthquake is the same, the flexible building absorbs the shaking energy by bending and swaying. The rigid building fights the force, leading to cracks, collapses, and much greater danger to people inside.",
            "feedback_incorrect": "The earthquake is the same, but the buildings respond differently. The rigid building (low flexibility) cannot absorb the shaking force and suffers severe damage. The flexible building (high flexibility) sways with the earthquake, reducing damage and keeping occupants safer."
        },
        {
            "question": "The model shows that Structural Damage has a NEGATIVE relationship with Occupant Safety. Why is this the most important relationship for earthquake engineers?",
            "choices": {
                "A": "Because engineers want to increase both damage and safety at the same time",
                "B": "Because when Structural Damage increases, Occupant Safety decreases, meaning cracking walls and falling debris put people in danger",
                "C": "Because Occupant Safety causes Structural Damage, not the other way around",
                "D": "Because this relationship only matters for small earthquakes"
            },
            "correct": "B",
            "feedback_correct": "That is right! This is the key relationship because it directly connects building performance to human lives. When walls crack, floors collapse, and debris falls, people inside are at extreme risk. Engineers design for flexibility to keep damage low and safety high.",
            "feedback_incorrect": "More Structural Damage means less Occupant Safety because cracking walls, collapsing floors, and falling debris endanger people inside. This is why earthquake engineers focus on reducing damage through flexible design, saving lives."
        }
    ]
}

# =============================================================================
# G04L2-L07: Chain Reaction: When Energy Moves Object to Object
# NGSS 4-PS3-3, 4-PS3-4: Energy transfer in collisions, energy conversion
# =============================================================================
L07_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "When a moving marble hits a row of stationary marbles, the last marble in the row rolls away. What happened to the energy?",
            "choices": {
                "A": "The moving marble created new energy that appeared in the last marble",
                "B": "The kinetic energy from the first marble transferred through the chain from marble to marble until it reached the last one",
                "C": "The last marble moved on its own because it saw the first marble coming",
                "D": "Gravity pulled the last marble forward when the first marble stopped"
            },
            "correct": "B",
            "feedback_correct": "Correct! Kinetic energy (motion energy) transfers from one object to the next during each collision. The first marble's energy passes through the chain until the last marble receives it and moves.",
            "feedback_incorrect": "Energy is not created or pulled by gravity in this situation. The kinetic energy from the first marble transfers to the second, then to the third, and so on through collisions until it reaches the last marble."
        },
        {
            "question": "In the model, Initial Push Force and Object Mass are external components. Why are these external?",
            "choices": {
                "A": "Because they are the parts we cannot see in the chain reaction",
                "B": "Because they are the starting conditions we control, and the internal components respond to them",
                "C": "Because they happen after the chain reaction is finished",
                "D": "Because they are the parts of the model that change the most"
            },
            "correct": "B",
            "feedback_correct": "Right! External components are the inputs we set before the system runs. We decide how hard to push the first object and how heavy the objects are. Kinetic Energy Transfer, Energy Lost to Sound, and Final Object Speed all respond to these choices.",
            "feedback_incorrect": "External components are the conditions we can control or decide. Initial Push Force (how hard we push) and Object Mass (how heavy the objects are) are set before the chain starts. The internal components change as a result."
        },
        {
            "question": "Every time one domino hits the next in a chain, you hear a clicking sound. What does that clicking sound tell you about energy?",
            "choices": {
                "A": "The sound means new energy is being created at each collision",
                "B": "The sound is proof that some kinetic energy is transforming into sound energy at each collision, reducing the energy available for motion",
                "C": "The sound has nothing to do with energy",
                "D": "The sound means the dominoes are gaining energy as they fall"
            },
            "correct": "B",
            "feedback_correct": "Exactly! Every click you hear represents kinetic energy that transformed into sound energy. That energy is no longer available to push the next domino. This is why chain reactions lose energy at every collision.",
            "feedback_incorrect": "The clicking sound is not free. It takes energy to make sound. At each collision, some kinetic energy transforms into sound (and a tiny bit of heat). That energy is lost from the motion system, which is why the chain gets weaker."
        },
        {
            "question": "The model shows that Object Mass has a NEGATIVE relationship with Final Object Speed. A student tests the chain with light marbles and then with heavy steel balls. What will they observe?",
            "choices": {
                "A": "Heavy objects will make the last object move faster because they hit harder",
                "B": "Both chains will have the same Final Object Speed because the push was the same",
                "C": "The light marble chain will have a faster Final Object Speed because lighter objects transfer energy more efficiently and require less energy to get moving",
                "D": "Neither chain will work because objects cannot transfer energy"
            },
            "correct": "C",
            "feedback_correct": "Right! Lighter objects require less energy to accelerate, so more kinetic energy passes through the chain. Heavier objects absorb more energy just getting started, leaving less energy for the final object. The negative relationship means more mass leads to less final speed.",
            "feedback_incorrect": "A negative relationship means when one goes up, the other goes down. Heavier objects require more energy to get moving, so more energy is absorbed at each step. Light objects transfer energy more efficiently, resulting in a faster Final Object Speed."
        },
        {
            "question": "The model shows that Energy Lost to Sound has a NEGATIVE relationship with Final Object Speed. Why does a long chain of 20 dominoes produce a slower final domino than a short chain of 5 dominoes with the same starting push?",
            "choices": {
                "A": "The dominoes get tired after falling for too long",
                "B": "A longer chain has more collisions, and each collision loses energy to sound and heat, so less energy reaches the final domino",
                "C": "The first domino in the long chain pushes harder than the first domino in the short chain",
                "D": "Longer chains create friction between the dominoes and the table"
            },
            "correct": "B",
            "feedback_correct": "That is right! Every collision is an energy leak. With 20 collisions, the energy losses add up. Each click of sound and tiny bit of heat removes energy from the motion system. By the time energy reaches domino 20, much less is left than what domino 5 received.",
            "feedback_incorrect": "Dominoes do not get tired. The issue is energy loss. At every single collision, a small amount of kinetic energy becomes sound and heat. More collisions means more total energy lost. A 20-domino chain has 19 energy-leaking collisions compared to only 4 in a 5-domino chain."
        }
    ]
}


# =============================================================================
# Combined dictionary for all Grade 4 Level 2 lessons
# =============================================================================
ALL_QUESTIONS = {
    "G04L2-L01": L01_QUESTIONS,
    "G04L2-L02": L02_QUESTIONS,
    "G04L2-L03": L03_QUESTIONS,
    "G04L2-L04": L04_QUESTIONS,
    "G04L2-L05": L05_QUESTIONS,
    "G04L2-L06": L06_QUESTIONS,
    "G04L2-L07": L07_QUESTIONS,
}
