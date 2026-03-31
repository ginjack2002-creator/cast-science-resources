#!/usr/bin/env python3
"""Complete lesson data for G04L2-L01 through G04L2-L07 (Grade 4 Level 2 ModelIt! Lessons)"""

L01 = {
    "id": "G04L2-L01",
    "title": "The Energy Roller Coaster: Where Does Speed Come From?",
    "subtitle": "How Energy Transforms, Transfers, and Gets Lost Along the Way",
    "ngss": "4-PS3-1, 4-PS3-4",
    "ngss_desc": "Use evidence to construct an explanation relating the speed of an object to the energy of that object. Apply scientific ideas to design, test, and refine a device that converts energy from one form to another.",
    "big_question": "If energy is never destroyed, why does a roller coaster eventually slow down and stop?",
    "objectives": [
        "Explain how potential energy at the top of a hill converts to kinetic energy at the bottom",
        "Model how hill height, track friction, potential energy, kinetic energy, and heat loss interact in a system",
        "Describe how friction causes energy to leave the motion system as heat, reducing speed",
        "Use evidence from a model to explain why roller coasters slow down even though energy is conserved"
    ],
    "vocabulary": [
        ("Potential Energy", "Stored energy an object has because of its position or height — like a roller coaster waiting at the top of a hill"),
        ("Kinetic Energy", "The energy of motion — the faster something moves, the more kinetic energy it has"),
        ("Friction", "A force that happens when two surfaces rub together, slowing things down and creating heat"),
        ("Heat Loss", "Energy that transforms into heat because of friction — this energy leaves the motion system"),
        ("Energy Conservation", "The scientific law that energy is never created or destroyed — it only changes form")
    ],
    "components": [
        ("Hill Height", "How tall the starting hill of the roller coaster is — taller hills store more potential energy at the top", True),
        ("Track Friction", "How rough or smooth the track surface is — rougher tracks create more friction between the car and the rails", True),
        ("Potential Energy", "The stored energy the coaster has at the top of the hill because of its height — waiting to be converted into motion", False),
        ("Kinetic Energy", "The energy of the coaster's motion at the bottom of the hill — how fast and powerful the movement is", False),
        ("Heat Loss", "Energy that gets transformed into heat because of friction between the coaster wheels and the track surface", False)
    ],
    "think_about_it": "When Hill Height increases, what happens to Potential Energy? When Track Friction increases, what happens to Heat Loss, and how does that affect Kinetic Energy?",
    "scenarios": [
        ("Smooth Track, Tall Hill", "Set Hill Height to 80% and Track Friction to 10% — observe how much kinetic energy the coaster has at the bottom"),
        ("Rough Track, Tall Hill", "Keep Hill Height at 80% but increase Track Friction to 80% — what happens to the coaster's speed?"),
        ("Smooth Track, Short Hill", "Set Hill Height to 20% and Track Friction to 10% — compare kinetic energy to the tall hill scenario"),
        ("Worst Case", "Set Hill Height to 30% and Track Friction to 90% — can the coaster even make it through the track?")
    ],
    "sim_scenarios": [
        ("Smooth Track, Tall Hill", "Hill Height at 80%, Track Friction at 10%", "What do you predict will happen to Kinetic Energy when the hill is tall and the track is smooth?"),
        ("Rough Track, Tall Hill", "Hill Height at 80%, Track Friction at 80%", "What do you predict will happen to Heat Loss when friction is high? How will that affect Kinetic Energy?"),
        ("Smooth Track, Short Hill", "Hill Height at 20%, Track Friction at 10%", "Will a short smooth hill give the coaster enough energy to go fast?"),
        ("Worst Case", "Hill Height at 30%, Track Friction at 90%", "What happens when the hill is short AND the track is rough? Where does all the energy go?")
    ],
    "discoveries": [
        "Taller hills give the coaster more potential energy at the top, which converts to more kinetic energy (speed) at the bottom",
        "Friction transforms kinetic energy into heat — the energy does not disappear, it just changes into a form that does not help the coaster move",
        "When friction is high, more energy is lost as heat, so less energy is available for motion — the coaster slows down",
        "Energy is CONSERVED (never created or destroyed), but it can change forms — and once it becomes heat from friction, it cannot easily change back to motion"
    ],
    "answer": "A roller coaster slows down because of FRICTION! At the top of the hill, the coaster has lots of potential energy. As it rolls down, that energy converts to kinetic energy (speed). But friction between the wheels and the track transforms some of that kinetic energy into HEAT. The energy is not destroyed — it is just changed into heat that escapes into the air. With every meter of track, a little more energy becomes heat instead of speed. That is why the coaster eventually stops — all of its energy has been transformed into heat!",
    "stem_title": "Design the Friction-Fighting Coaster",
    "stem_mission": "Design a marble track that minimizes energy loss to friction so the marble maintains the most speed from start to finish.",
    "stem_scenario": "A theme park is losing money because their roller coaster slows down too quickly and riders complain it is not exciting enough. Your engineering team has been hired to redesign the track to reduce friction and keep the coaster fast for longer. Use evidence from your model to make design decisions about hill height and track surface.",
    "stem_questions": [
        "What track surface material would create the least friction for your marble?",
        "How does changing the starting hill height affect how far the marble travels before stopping?",
        "If you cannot eliminate friction completely, what is the best combination of height and smoothness?"
    ],
    "stem_design_qs": [
        "What materials will you test for the smoothest track surface (foil, wax paper, plastic, cardboard)?",
        "How will you measure how far the marble travels before friction stops it?",
        "What starting height gives the marble enough energy to overcome friction on each surface?",
        "How will you keep your test fair by changing only one variable at a time?"
    ],
    "career": "Mechanical Engineers design machines, vehicles, and rides by understanding how energy, friction, and motion work together. They design everything from roller coasters to electric cars. They earn $70,000–$115,000/year.",
    "images": {
        "cover": ("cover-energy-coaster.png", "A dramatic close-up of a roller coaster car at the very top of a steep hill, showing the track curving downward with motion blur suggesting speed, golden hour lighting, cinematic amusement park photography"),
        "landscape": ("landscape-energy-coaster.png", "A photorealistic image of diverse 4th grade students (9-10 years old) with a White boy and a Latina girl leading the group, building marble ramps with different surface textures on their desks in a bright modern classroom, natural window light, editorial photo quality, genuinely diverse group including Black, Asian, White, and Latino students"),
        "modeling": ("modeling-energy-coaster.png", "A photorealistic image of diverse 4th grade students (9-10 years old) with an Asian American girl taking the lead at the laptop, working together building a digital energy model on screen, modern classroom with energy transformation posters, genuinely diverse group with varied hairstyles and features"),
        "discussion": ("discussion-energy-coaster.png", "A photorealistic image of a Latino male teacher leading an animated discussion with diverse 4th graders (9-10 years old) about energy and friction, pointing at a smartboard showing a roller coaster diagram with PE and KE labels, students with hands raised, balanced diversity"),
        "stem": ("stem-energy-coaster.png", "A photorealistic image of diverse 4th grade students (9-10 years old) with a Black girl and White boy working side by side in the foreground, testing marble runs on tracks made from different materials like foil and wax paper, excited collaborative group work at tables, balanced diversity")
    },
    "pre_assessment": [
        "If you let a marble roll down a ramp, it eventually stops. Where do you think the energy went?",
        "What do you think friction is, and how does it affect moving objects?",
        "Draw what you think happens to a roller coaster's energy as it goes from the top of a hill to the bottom and then along a flat track.",
        "Do you think a roller coaster would go faster on a smooth track or a rough track? Why?"
    ],
    "extend_components": [
        ("Loop Size", "How big a loop in the track is — the coaster needs enough kinetic energy to make it through without falling"),
        ("Air Resistance", "The force of air pushing against the coaster as it moves — faster coasters experience more air drag"),
        ("Coaster Mass", "How heavy the roller coaster car and riders are — heavier cars have more energy at the same speed but also more friction")
    ],
    "reflections": [
        "If energy is never destroyed, why does the roller coaster eventually stop?",
        "How is rubbing your hands together related to what happens between the coaster and the track?",
        "Why do roller coaster designers make the first hill the tallest one on the ride?",
        "If you could build a track with zero friction, would the coaster ever stop? Why or why not?",
        "How did your model help you understand the difference between what happens on a smooth track vs. a rough track?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model with five components showing how hill height and friction interact to determine kinetic energy through energy transformation and heat loss."),
        ("Disciplinary Core Idea", "PS3.A Definitions of Energy / PS3.B Conservation of Energy", "Energy can be moved from place to place and can be transferred between objects. Energy is conserved — when a moving object slows down, its energy is transferred to heat through friction."),
        ("Crosscutting Concept", "Energy and Matter", "Students trace energy through a system, identifying how it transforms from potential to kinetic to heat, demonstrating conservation while explaining why motion decreases.")
    ],
    "cast_items": [
        "Explain how potential energy converts to kinetic energy as a coaster descends a hill",
        "Use a model to describe how friction transforms kinetic energy into heat",
        "Describe why a roller coaster slows down even though energy is conserved"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A marble rolls down a tall ramp on a smooth surface and then on a rough surface. It travels farther on the smooth surface. Which best explains why?"),
        ("Constructed Response:", "Using what you know about energy conservation and friction, explain why a roller coaster eventually stops even though energy can never be destroyed. Use the words 'potential energy,' 'kinetic energy,' and 'heat loss' in your answer.")
    ],
    "background_intro": "Energy transformation is one of the most powerful ideas in science. Every ride at a theme park, every car on the road, and every ball you throw demonstrates how energy changes form. Understanding friction's role in energy transformation explains why perpetual motion machines are impossible and why engineers work so hard to reduce friction in machines.",
    "background_sections": [
        ("Energy Transformation on a Roller Coaster", "A roller coaster is a perfect laboratory for studying energy transformation. At the top of the first hill, the coaster has maximum potential energy (PE) — energy stored because of its height. As it descends, PE converts to kinetic energy (KE) — the energy of motion. At the very bottom, nearly all PE has become KE, and the coaster is moving at its fastest speed. As it climbs the next hill, KE converts back to PE. This back-and-forth conversion would continue forever if not for one thing: friction."),
        ("Friction and Heat Loss", "Friction occurs wherever two surfaces slide against each other. On a roller coaster, friction happens between the wheels and the track, and between the coaster and the air (air resistance). Friction transforms kinetic energy into thermal energy (heat). You can feel this effect by rubbing your hands together quickly — they get warm because friction converts your motion energy into heat. On a coaster, this heat radiates into the air and is lost from the motion system forever."),
        ("The Law of Conservation of Energy", "The total amount of energy in a closed system never changes — this is the Law of Conservation of Energy. When a roller coaster slows down, energy has not been destroyed. It has been transformed into heat, sound, and vibration. If you could measure ALL the energy (kinetic + potential + heat + sound), the total would equal the original potential energy at the top of the first hill. Engineers cannot eliminate friction, but they can reduce it with smooth surfaces, lubricated wheels, and aerodynamic designs."),
        ("Real-World Engineering Applications", "Understanding energy and friction is critical for engineers in many fields. Car engineers design sleek shapes to reduce air friction and improve fuel efficiency. Roller coaster designers calculate exactly how much energy is lost to friction to ensure the car makes it through every loop and hill. Space engineers use friction (drag) to slow spacecraft when entering an atmosphere. Even ice skaters know that smoother ice means less friction and faster spins.")
    ],
    "lever_L": "Students identify Hill Height and Track Friction as external components (design choices) and Potential Energy, Kinetic Energy, and Heat Loss as internal components that respond to the externals.",
    "lever_E": "Students determine that Hill Height positively affects PE, PE positively affects KE, Track Friction positively affects Heat Loss, and Heat Loss negatively affects KE — creating a system with competing influences.",
    "lever_V": "Students build a five-component model showing how energy flows from height to potential energy to kinetic energy, while friction diverts energy into heat loss that reduces speed.",
    "lever_Ev": "Students run four scenarios (smooth tall, rough tall, smooth short, worst case) to observe how changing two external inputs creates different outcomes in the system.",
    "lever_R": "Students add loop size or air resistance to explore why some coaster designs fail — a loop requires minimum KE to complete, so too much friction can make the coaster fall at the top of a loop.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with roller coaster at top of hill, energy arrows showing PE and KE", "say": "Who remembers our first roller coaster lesson? Today we are going DEEPER — we are going to figure out why every roller coaster eventually stops.", "do": "Show a quick video of a roller coaster slowing to a stop. Ask: Where did all that speed go?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary with PE, KE, friction, and heat loss", "say": "Today we have FIVE system parts to work with instead of three — we are leveling up our modeling skills!", "do": "Have students read objectives aloud. Review PE and KE from L1, then introduce friction and heat loss.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why does a coaster stop if energy is never destroyed?", "say": "Here is the puzzle: scientists say energy can NEVER be destroyed. But the coaster stops. So where does the energy GO?", "do": "Have students turn and talk: If energy cannot be destroyed, why does the coaster eventually stop? Write predictions.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps with five components previewed", "say": "This model is more complex than our first one. We have two things we control and three things that respond.", "do": "Preview the five components. Explain that having two external components means we can test combinations.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Five component cards for energy system", "say": "Which of these five parts do WE control, and which ones respond on their own?", "do": "Guide sorting of five components. Discuss why Hill Height and Track Friction are external (design choices) while PE, KE, and Heat Loss are internal (they respond automatically).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows showing + and - connections", "say": "Here is where it gets interesting — some arrows are POSITIVE and some are NEGATIVE. What does a negative arrow mean?", "do": "Help students draw all four relationships. Emphasize the negative arrow from Heat Loss to KE — this is the key insight.", "time": "10 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph with five component lines", "say": "Watch what happens when we change friction. Keep your eyes on the KE and Heat Loss lines!", "do": "Run scenarios in order. Have students record observations in their activity pack. Focus on the smooth vs. rough comparison.", "time": "12 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings with energy flow diagram", "say": "Now we know the answer — energy is CONSERVED but TRANSFORMED. Friction turns motion energy into heat!", "do": "Have students rub hands together to feel friction heat. Draw the complete energy flow on the board.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Friction-fighting coaster design challenge", "say": "You are engineers now. Your mission: design a track that fights friction and keeps the marble fast!", "do": "Distribute materials (ramps, foil, wax paper, sandpaper, marbles). Groups test surfaces and record distances.", "time": "12 min"}
    ],
    "sort_reasoning": "Hill Height and Track Friction are external because they are design choices made before the coaster starts — engineers decide how tall to build the hill and what material to use for the track surface. Potential Energy, Kinetic Energy, and Heat Loss are internal because they are results that happen automatically inside the system in response to those design choices.",
    "relationships": [
        ("Hill Height to Potential Energy", "POSITIVE (+)", "A taller hill lifts the coaster higher above the ground, storing more gravitational potential energy. Doubling the height roughly doubles the stored energy available for conversion to motion."),
        ("Potential Energy to Kinetic Energy", "POSITIVE (+)", "As the coaster descends, stored potential energy converts into kinetic energy (motion). More PE at the top means more KE at the bottom — this is direct energy transformation."),
        ("Track Friction to Heat Loss", "POSITIVE (+)", "A rougher track surface creates more friction between the wheels and the rails. More friction means more kinetic energy gets transformed into heat energy, which escapes into the surrounding air."),
        ("Heat Loss to Kinetic Energy", "NEGATIVE (-)", "Energy lost as heat is energy that is NOT available for motion. When Heat Loss increases, Kinetic Energy decreases because the total energy is conserved — more going to heat means less going to speed.")
    ],
    "sim_answers": [
        ("Smooth Track, Tall Hill", "When Hill Height is high and Track Friction is low, Potential Energy is very high at the top, most of it converts to Kinetic Energy at the bottom, and Heat Loss is minimal. The coaster zooms through at near-maximum speed because almost all the stored energy becomes motion."),
        ("Rough Track, Tall Hill", "When Hill Height is high but Track Friction is also high, the coaster starts with lots of Potential Energy, but a significant portion gets converted to Heat Loss instead of Kinetic Energy. The graph clearly shows KE dropping as Heat Loss rises — the coaster is noticeably slower even though it started from the same height.")
    ],
    "reflection_exemplars": [
        ("If energy is never destroyed, why does the coaster stop?", "The coaster stops because all of its energy has been TRANSFORMED — not destroyed. At the top of the hill, energy is stored as potential energy. As the coaster moves, that energy converts to kinetic energy. But friction between the wheels and the track gradually transforms kinetic energy into heat energy. The heat radiates into the air and is spread out so thinly that it cannot be gathered back up to push the coaster. The energy still exists as heat in the environment, but it is no longer useful for motion."),
        ("Why do engineers make the first hill the tallest?", "The first hill is the energy bank for the entire ride. The taller the first hill, the more potential energy is stored. Every subsequent hill must be shorter than the first because friction has already stolen some energy as heat by the time the coaster reaches the next hill. If a later hill were taller, the coaster would not have enough kinetic energy to make it over — it would roll backward!")
    ],
    "stem_intro": "Present the challenge: A theme park's roller coaster is losing riders because it slows down too quickly. Your engineering team must redesign the track to minimize friction and maximize speed. Test different track surfaces and starting heights to find the best combination. Use your model evidence to justify your design choices!",
    "stem_concepts": [
        ("Energy Conservation", "Energy is never created or destroyed — it only changes form. On a roller coaster, potential energy becomes kinetic energy becomes heat energy. Your job as an engineer is to keep as much energy in the kinetic form as possible."),
        ("Friction Reduction", "Smoother surfaces create less friction, which means less energy is lost to heat. Real engineers use polished steel rails, lubricated wheels, and aerodynamic shapes to minimize friction on roller coasters."),
        ("Height as Energy Storage", "The taller your starting hill, the more potential energy you store. A taller hill gives you more energy to work with, so even if some is lost to friction, there is still enough left for an exciting ride.")
    ],
    "stem_eval": [
        ("Expert (4)", "Tests multiple surface materials AND heights, uses model evidence to explain why specific combinations produce the best results, connects findings to energy conservation"),
        ("Proficient (3)", "Tests at least two surfaces or heights, can explain how friction affects speed using energy vocabulary"),
        ("Developing (2)", "Builds a track and tests it but struggles to connect results to friction and energy concepts"),
        ("Beginning (1)", "Track is incomplete or student cannot explain how friction affects the marble's speed")
    ],
    "support": [
        "Provide a labeled energy flow diagram showing PE at the top converting to KE at the bottom, with a branch showing energy going to Heat Loss",
        "Let students rub their hands together fast, then slow — they can feel that faster rubbing creates more heat (more friction, more energy transformed)",
        "Sentence frames: 'When Track Friction increases, Heat Loss __ because __ . This causes Kinetic Energy to __ because __.'"
    ],
    "extensions": [
        "Research how real roller coaster engineers use magnetic braking systems that convert kinetic energy into electrical energy instead of wasting it as heat",
        "Design a track where the marble must complete a loop — calculate the minimum starting height needed to overcome friction AND complete the loop",
        "Compare the distance a marble travels on five different surfaces and create a friction ranking chart"
    ],
    "cross_curr": [
        ("Math", "Measure how far a marble rolls on different surfaces from the same height and calculate the percentage of energy lost to friction for each surface"),
        ("ELA", "Write a persuasive letter to a theme park explaining why they should invest in smoother track materials, using energy science as evidence"),
        ("Art", "Create an infographic showing the energy journey of a roller coaster from the top of the first hill to the final stop, with color-coded arrows for PE, KE, and heat")
    ],
    "misconceptions": [
        ("The roller coaster runs out of energy", "Energy is NEVER used up or destroyed. When a coaster slows down, its kinetic energy has been transformed into heat energy through friction and sound energy from the rumbling. The total energy in the universe stays the same — it has just changed into forms that cannot push the coaster forward anymore.", "Rub your hands together fast until they feel warm. Ask: Where did the motion energy go? It became heat — same thing happens with the coaster and the track."),
        ("Friction only happens on rough surfaces", "ALL surfaces have friction, even ones that look perfectly smooth. Under a microscope, every surface has tiny bumps and ridges that catch on each other. Engineers can reduce friction but never eliminate it completely. Even ice has friction — that is why ice skaters eventually slow down.", "Have students slide a book on a desk versus on sandpaper. Both have friction, but the amounts are very different."),
        ("A taller second hill would make the coaster go faster", "The coaster can NEVER go higher than its starting hill (without an engine boost) because friction has already converted some energy to heat. Each hill on a coaster must be shorter than the previous one. If a hill were taller, the coaster would not have enough energy to make it over the top.", "Set up a marble ramp with a second ramp that is taller than the first — students see the marble cannot make it over. Lower the second ramp until it works.")
    ]
}

L02 = {
    "id": "G04L2-L02",
    "title": "Can Sound Travel Through Space?",
    "subtitle": "Why Astronauts Need Radios and Explosions Are Silent in a Vacuum",
    "ngss": "4-PS4-1, 4-PS4-3",
    "ngss_desc": "Develop a model of waves to describe patterns in terms of amplitude and wavelength. Generate and compare multiple solutions that use light or sound to transfer information.",
    "big_question": "In every space movie, explosions make huge booming sounds. But is that what would really happen in space?",
    "objectives": [
        "Explain how sound waves require a medium (air, water, or solids) to travel",
        "Model how vibration strength, medium density, wave speed, sound loudness, and wave absorption interact",
        "Describe why sound travels at different speeds through different materials",
        "Use evidence from a model to explain why sound cannot travel through the vacuum of space"
    ],
    "vocabulary": [
        ("Medium", "The material that sound travels through — it can be a gas (air), liquid (water), or solid (metal, wood)"),
        ("Vibration", "A rapid back-and-forth movement that creates sound waves when it pushes on nearby molecules"),
        ("Wave Speed", "How fast a sound wave moves through a material — sound travels at different speeds in different media"),
        ("Absorption", "When a material soaks up sound energy instead of passing it along, making the sound quieter"),
        ("Vacuum", "A space with no matter in it at all — no air, no water, nothing for sound to travel through")
    ],
    "components": [
        ("Vibration Strength", "How hard the sound source vibrates — like the difference between tapping a drum gently vs. hitting it hard", True),
        ("Medium Density", "How tightly packed the molecules are in the material sound is traveling through — air is thin, water is dense, steel is very dense", True),
        ("Wave Speed", "How fast the sound wave moves through the medium — denser materials with tightly packed molecules pass vibrations faster", False),
        ("Sound Loudness", "How loud the sound is when it reaches the listener — depends on both the source strength and how much energy is absorbed along the way", False),
        ("Wave Absorption", "How much sound energy gets soaked up by the medium as the wave passes through — some materials absorb more than others", False)
    ],
    "think_about_it": "When Medium Density increases, what happens to Wave Speed? What happens to Wave Absorption? How do these two effects combine to determine Sound Loudness?",
    "scenarios": [
        ("Sound in Air", "Set Vibration Strength to 70% and Medium Density to 30% — this represents sound traveling through normal air"),
        ("Sound in Water", "Keep Vibration Strength at 70% but increase Medium Density to 70% — this represents sound traveling through water"),
        ("Sound in Space", "Set Medium Density to 0% — this represents the vacuum of outer space with no molecules at all"),
        ("Loud vs. Quiet Source", "Compare Vibration Strength at 20% vs. 90% with Medium Density at 30% — how does source strength affect loudness?")
    ],
    "sim_scenarios": [
        ("Sound in Air", "Vibration Strength at 70%, Medium Density at 30%", "What do you predict will happen to Wave Speed and Sound Loudness when sound travels through normal air?"),
        ("Sound in Water", "Vibration Strength at 70%, Medium Density at 70%", "Do you think sound will travel faster or slower in water compared to air? Why?"),
        ("Sound in Space", "Medium Density at 0%", "What do you predict will happen to ALL the internal components when there are zero molecules to vibrate?"),
        ("Loud vs. Quiet Source", "Vibration Strength at 20% vs. 90%, Medium Density at 30%", "How much louder will the strong vibration be compared to the weak one?")
    ],
    "discoveries": [
        "Sound MUST have a medium to travel through — in a vacuum (like space), there are no molecules to vibrate, so sound cannot exist",
        "Sound travels faster through denser materials — it moves about 4 times faster in water than in air, and about 15 times faster in steel than in air",
        "Denser media absorb less sound energy, so sound stays louder over longer distances in water and solids compared to air",
        "Both vibration strength and the medium affect loudness — a shout in water carries farther than a shout in air because water absorbs less energy"
    ],
    "answer": "Sound CANNOT travel through space! In movies, explosions in space are shown with huge booming sounds, but that is completely wrong. Sound waves are vibrations that pass from one molecule to the next, like a chain of dominoes. In space, there are almost no molecules at all — it is a vacuum. With no molecules to vibrate, the sound wave has nothing to push on, so it simply cannot travel. If you were an astronaut watching an explosion in space, you would see the flash of light but hear absolutely nothing. That is why astronauts use radios that send electromagnetic waves (which DO travel through vacuum) instead of relying on sound.",
    "stem_title": "Design the Best Sound Transmitter",
    "stem_mission": "Design and test a system that transmits sound as clearly as possible from one side of the classroom to the other using different materials.",
    "stem_scenario": "A submarine crew needs to communicate between sealed rooms without using electronics. Your engineering team must design a sound transmission system that carries voices as clearly as possible through solid materials. Test different materials to find which one transmits sound the best and explain WHY using your model evidence.",
    "stem_questions": [
        "Which material transmits sound the clearest — string, wire, a wooden stick, or a plastic tube?",
        "Why do some materials carry sound better than others?",
        "How does the length of the material affect how well sound transmits?"
    ],
    "stem_design_qs": [
        "What materials will you test as your sound transmission medium (string, wire, wood, metal, plastic)?",
        "How will you measure which material transmits sound the clearest?",
        "How will you keep your test fair — same sound source, same distance, same listener?",
        "How will you connect your material between the sender and receiver (cups, funnels, direct contact)?"
    ],
    "career": "Acoustical Engineers design spaces and systems for optimal sound — from concert halls to noise-canceling headphones to submarine sonar systems. They earn $65,000–$110,000/year.",
    "images": {
        "cover": ("cover-sound-space.png", "A dramatic split image showing an explosion in space on one side (silent, with no sound waves visible) and an explosion on Earth on the other side (with visible sound wave rings), dark space background, cinematic and scientific"),
        "landscape": ("landscape-sound-space.png", "A photorealistic image of diverse 4th grade students (9-10 years old) with an Asian American boy and a Black girl leading the activity, testing sound transmission through different materials like string telephones and metal rods in a bright modern classroom, natural window light, genuinely diverse group"),
        "modeling": ("modeling-sound-space.png", "A photorealistic image of diverse 4th grade students (9-10 years old) with a White girl taking the lead at the computer, working together building a digital sound wave model on screen, modern classroom with wave diagrams on the wall, balanced diversity with varied hairstyles"),
        "discussion": ("discussion-sound-space.png", "A photorealistic image of a Black female teacher leading a discussion with diverse 4th graders (9-10 years old) about why sound cannot travel in space, showing a diagram of molecules vibrating on a smartboard, students with hands raised, balanced diversity"),
        "stem": ("stem-sound-space.png", "A photorealistic image of diverse 4th grade students (9-10 years old) with a Latino boy and White girl in the foreground, building cup-and-string telephones using different materials, testing which carries sound best, excited and engaged, balanced diversity")
    },
    "pre_assessment": [
        "Do you think you could hear an explosion in outer space? Why or why not?",
        "Why do you think you can hear someone talking underwater in a swimming pool?",
        "Draw what you think is happening in the air between a drum being hit and your ear hearing the sound.",
        "If sound needs something to travel through, what do you think happens in a place with nothing in it?"
    ],
    "extend_components": [
        ("Distance from Source", "How far the listener is from the sound — sound gets quieter over distance as the wave spreads out"),
        ("Temperature", "How hot or cold the medium is — warmer air carries sound slightly faster because molecules move more quickly"),
        ("Frequency", "How fast the vibrations happen — this determines whether we hear a high pitch or a low pitch")
    ],
    "reflections": [
        "Why do space movies get the sound of explosions wrong?",
        "If you were on the Moon with a friend standing right next to you, could you talk to each other without a radio? Why or why not?",
        "Why does sound travel faster through water than through air?",
        "How is sound traveling through a medium like a line of dominoes falling?",
        "How did your model help you understand something you cannot directly experience, like silence in space?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a five-component model showing how vibration strength and medium density interact to determine wave speed, absorption, and loudness in different environments."),
        ("Disciplinary Core Idea", "PS4.A Wave Properties / PS4.C Information Transfer", "Waves can be made in water by disturbing the surface. Sound waves need a medium to travel. Information can be transferred through sound waves or electromagnetic waves."),
        ("Crosscutting Concept", "Cause and Effect", "Students investigate how changes in medium density cause predictable effects on wave speed and absorption, and discover the special case where removing the medium entirely eliminates sound.")
    ],
    "cast_items": [
        "Explain why sound requires a medium to travel and cannot move through a vacuum",
        "Use a model to describe how medium density affects wave speed and absorption",
        "Compare sound transmission through different materials using evidence"
    ],
    "cast_questions": [
        ("Multiple Choice:", "An astronaut in space watches a satellite explode 100 meters away. What does the astronaut hear?"),
        ("Constructed Response:", "Using what you know about sound waves and media, explain why whales can communicate across hundreds of miles underwater but humans can only shout across a few hundred feet in air. Use the words 'medium,' 'wave speed,' and 'absorption' in your answer.")
    ],
    "background_intro": "Sound is something we experience every moment of our lives, yet most people never think about what sound actually IS. Understanding that sound requires a medium to travel changes how we think about the universe — most of space is completely silent, no matter how dramatic the events happening there.",
    "background_sections": [
        ("What Sound Really Is", "Sound is a mechanical wave — a vibration that passes through matter by bumping molecules into each other. When a drum is struck, the drum skin pushes air molecules forward, which bump into the next molecules, which bump into the next, creating a chain reaction that travels outward in all directions. This is fundamentally different from light, which is an electromagnetic wave that does NOT need molecules to travel."),
        ("Sound in Different Media", "Sound travels at different speeds depending on the medium. In air at room temperature, sound moves at about 343 meters per second (767 mph). In water, it moves at about 1,480 m/s — over 4 times faster. In steel, it moves at about 5,960 m/s — over 17 times faster than in air. Why? In denser materials, molecules are packed closer together, so each molecule does not have to travel as far to bump into the next one. The chain reaction happens faster."),
        ("The Silence of Space", "Space is an almost perfect vacuum — there are only about 1-10 atoms per cubic centimeter in interstellar space, compared to about 25 billion billion (2.5 x 10^19) molecules per cubic centimeter in air at sea level. With virtually no molecules, there is nothing to vibrate, and sound simply cannot exist. Astronauts communicate using radio waves, which are electromagnetic waves like light and can travel through vacuum. Every space movie that shows explosions with sound is scientifically wrong."),
        ("How Animals Use Sound in Different Media", "Different animals have evolved to use sound in the medium that surrounds them. Whales use low-frequency sound waves that can travel thousands of miles through ocean water because water transmits sound efficiently with low absorption. Elephants communicate using infrasound (very low frequency sounds) that travel through the ground — they detect these vibrations through their feet. Bats use ultrasound (very high frequency) in air to navigate and find insects in the dark.")
    ],
    "lever_L": "Students identify Vibration Strength and Medium Density as external components (what we control) and Wave Speed, Sound Loudness, and Wave Absorption as internal components that respond based on the medium and source.",
    "lever_E": "Students determine that Vibration Strength positively affects Loudness, Medium Density positively affects Wave Speed, Medium Density negatively affects Wave Absorption, and Wave Absorption negatively affects Loudness — creating competing pathways.",
    "lever_V": "Students build a five-component model showing how sound depends on both the source AND the medium, with two pathways affecting loudness (direct from source, and indirect through absorption).",
    "lever_Ev": "Students run four scenarios (air, water, vacuum, strong vs. weak source) to observe how the medium dramatically changes sound behavior, with the vacuum scenario showing complete system shutdown.",
    "lever_R": "Students add distance or temperature to explore why sounds get quieter over distance and why sound behaves differently on hot vs. cold days.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with space explosion imagery and question mark over sound waves", "say": "Raise your hand if you have seen a space movie where something explodes with a big BOOM. What if I told you those movies are lying to you?", "do": "Play a clip from a space movie with a loud explosion. Ask: Do you think that is what it would really sound like?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary including medium, vacuum, absorption", "say": "Today we are going to figure out whether sound can travel through NOTHING — and why that matters for astronauts.", "do": "Have students read objectives aloud. Introduce the word 'medium' and 'vacuum' with real examples.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Can sound travel through the vacuum of space?", "say": "Here is the question: space has almost nothing in it. Can sound travel through nothing?", "do": "Have students vote with thumbs up/down, then write their prediction and reasoning.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps with five components previewed", "say": "We have five parts in our model today — two we control and three that respond. Let us figure out how they connect.", "do": "Preview all five components. Explain that Medium Density can go to ZERO, which represents the vacuum of space.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Five component cards for sound system", "say": "Which parts of this system do WE control? The person making the sound controls one thing, and the material controls another.", "do": "Guide sorting. Vibration Strength is external (the sound maker controls it). Medium Density is external (we choose what material sound travels through).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows with + and - connections", "say": "This is tricky — some of these connections help sound and some work AGAINST sound. Let us figure out which is which.", "do": "Help students map all five relationships. Emphasize the negative connections and how they reduce loudness.", "time": "10 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph with all five components, especially the vacuum scenario", "say": "Now the big test — what happens when we set Medium Density to ZERO? Watch every single line on the graph.", "do": "Run air scenario first, then water, then set density to 0%. Students observe that ALL internal components drop to zero with no medium.", "time": "12 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings with medium comparison chart", "say": "The answer is clear — no molecules, no sound. Space movies have been lying to us this whole time!", "do": "Create a class chart comparing sound in air vs. water vs. vacuum. Discuss why astronauts need radios.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Sound transmitter design challenge", "say": "Now you are acoustic engineers. Which material carries sound the best from one side of the room to the other?", "do": "Distribute materials (cups, string, wire, wooden dowels, plastic tubes). Groups build and test sound transmitters.", "time": "12 min"}
    ],
    "sort_reasoning": "Vibration Strength is external because the sound source (a person, instrument, or machine) controls how hard it vibrates — this is a choice made outside the wave system. Medium Density is external because the environment determines what material sound travels through — air, water, or solid. Wave Speed, Sound Loudness, and Wave Absorption are internal because they are determined by the physics of how the wave interacts with the medium.",
    "relationships": [
        ("Vibration Strength to Sound Loudness", "POSITIVE (+)", "A stronger vibration sends out sound waves with more energy (higher amplitude). More energy in the wave means louder sound when it reaches the listener, just like how shouting is louder than whispering."),
        ("Medium Density to Wave Speed", "POSITIVE (+)", "In denser materials, molecules are packed closer together, so each molecule bumps into the next one faster. Sound travels about 4x faster in water than in air, and about 17x faster in steel than in air."),
        ("Medium Density to Wave Absorption", "NEGATIVE (-)", "Denser materials actually absorb LESS sound energy as the wave passes through. In air, the loosely packed molecules scatter sound energy, absorbing it faster. In water and solids, the tightly packed molecules pass energy along more efficiently."),
        ("Wave Absorption to Sound Loudness", "NEGATIVE (-)", "When more sound energy is absorbed by the medium, less energy reaches the listener, making the sound quieter. This is why whale songs can travel hundreds of miles in water (low absorption) but a shout barely carries a few hundred feet in air (higher absorption)."),
        ("Vibration Strength to Wave Speed", "POSITIVE (+)", "Stronger vibrations create waves with slightly more energy, which can push through a medium a bit faster. However, this effect is much smaller than the effect of medium density on wave speed.")
    ],
    "sim_answers": [
        ("Sound in Air", "With Vibration Strength at 70% and Medium Density at 30%, Wave Speed is moderate (sound moves at its normal air speed), Wave Absorption is moderate, and Sound Loudness is moderate. This is the baseline — normal sound traveling through normal air."),
        ("Sound in Space (Vacuum)", "With Medium Density at 0%, ALL internal components drop to zero regardless of Vibration Strength. Wave Speed is zero because there are no molecules to bump into each other. Wave Absorption is irrelevant. Sound Loudness is zero. This dramatically proves that sound REQUIRES a medium — in space, no one can hear you scream.")
    ],
    "reflection_exemplars": [
        ("Why do space movies get sound wrong?", "Space is a vacuum — there are almost no molecules in it. Sound is a vibration that travels by bumping molecules into each other, like a chain of dominoes. In space, there are no dominoes to knock over, so the vibration has nowhere to go. Movie makers add sound to explosions because silent explosions are not as exciting for audiences, but in reality, an astronaut watching an explosion in space would see the flash of light and feel nothing and hear nothing."),
        ("Why does sound travel faster in water than in air?", "In water, the molecules are packed much more tightly together than in air. When one water molecule vibrates, it does not have to travel far to bump into the next one — they are already touching. In air, molecules are spread out, so each one has to travel farther before bumping the next. It is like passing a message down a line of people — if everyone is shoulder to shoulder, the message goes fast, but if everyone is 10 feet apart, it takes longer.")
    ],
    "stem_intro": "Present the challenge: A submarine crew needs to communicate between sealed rooms without electronics. Your team must test different solid materials to find which one transmits voice most clearly from sender to receiver. Build your transmitter, test it, and explain WHY your best material works using your model evidence about medium density and absorption!",
    "stem_concepts": [
        ("Sound Needs a Medium", "Sound waves are vibrations passed between molecules. No molecules means no sound. Your transmitter MUST have a continuous material connecting the sender and receiver for sound to travel through."),
        ("Denser Media Transmit Better", "Materials with tightly packed molecules (metals, solids) transmit sound more clearly and with less energy loss than loosely packed materials (air, cotton). Your best transmitter will likely be a solid material."),
        ("Absorption Reduces Clarity", "Some materials soak up sound energy as it passes through. Soft, porous materials absorb more sound. Hard, dense materials absorb less. Choose your transmitter material wisely.")
    ],
    "stem_eval": [
        ("Expert (4)", "Tests multiple materials, ranks them by transmission quality, explains results using medium density and absorption concepts from the model"),
        ("Proficient (3)", "Tests at least two materials and can explain why the denser material transmitted sound better"),
        ("Developing (2)", "Builds a transmitter and tests it but struggles to connect material choice to sound science concepts"),
        ("Beginning (1)", "Transmitter is incomplete or student cannot explain why material choice matters for sound transmission")
    ],
    "support": [
        "Provide a visual showing molecules packed tightly (solid), loosely (gas), and empty (vacuum) to illustrate why sound needs a medium",
        "Let students put their ear to a desk and have someone tap the other end — they will hear the tap much more clearly through the solid desk than through air",
        "Sentence frames: 'Sound travels faster in __ because the molecules are __. When Medium Density is zero, sound __ because __.'"
    ],
    "extensions": [
        "Research how NASA astronauts communicate in space using radio waves instead of sound waves — what is the difference between sound waves and radio waves?",
        "Test whether sound travels faster through a wooden meter stick or a metal rod by tapping one end and listening at the other",
        "Investigate how whales communicate across hundreds of miles underwater and create a poster comparing whale communication to human communication"
    ],
    "cross_curr": [
        ("Math", "Create a bar graph comparing the speed of sound in air (343 m/s), water (1,480 m/s), and steel (5,960 m/s) and calculate how many times faster sound is in each medium"),
        ("ELA", "Write a scientifically accurate short story about an astronaut who has to communicate with a partner during a spacewalk without using a radio"),
        ("Social Studies", "Research how different ancient civilizations used sound transmission through solids — like Native Americans listening for horse hooves through the ground")
    ],
    "misconceptions": [
        ("Sound can travel through empty space", "Sound absolutely CANNOT travel through a vacuum. Sound is a mechanical wave that requires molecules to vibrate. In space, there are virtually no molecules. This is different from light and radio waves, which ARE electromagnetic and can travel through vacuum. Every space movie showing loud explosions in space is scientifically wrong.", "Show a video of the bell jar experiment — a ringing bell becomes silent as air is pumped out of the jar."),
        ("Sound travels at the same speed in all materials", "Sound speed changes dramatically depending on the medium. In air: 343 m/s. In water: 1,480 m/s. In steel: 5,960 m/s. Sound is FASTER in denser media because the molecules are closer together and transfer vibrations more quickly. Think of it like a line of people passing a ball — closer together means faster passing.", "Have students tap one end of a metal rail and listen at the other — the sound arrives through the metal before the sound through the air does."),
        ("Louder sounds travel faster", "Volume (loudness) and speed are completely independent. A whisper and a scream both travel through air at 343 m/s. Loudness depends on amplitude (how big the vibrations are), while speed depends on the medium. A soft tap on steel travels at 5,960 m/s — much faster than a loud scream through air at 343 m/s.", "Have two students clap loudly and softly from the same distance at the same time — both sounds arrive at the listener simultaneously.")
    ]
}

L03 = {
    "id": "G04L2-L03",
    "title": "Why Do Some Animals Survive Winter?",
    "subtitle": "The Hidden Science of Insulation, Metabolism, and Staying Alive",
    "ngss": "4-LS1-1, 4-LS1-2",
    "ngss_desc": "Construct an argument that plants and animals have internal and external structures that function to support survival, growth, behavior, and reproduction.",
    "big_question": "How do arctic foxes, polar bears, and penguins survive in freezing temperatures that would be dangerous for humans in minutes?",
    "objectives": [
        "Explain how body insulation (fur, fat, feathers) helps animals survive cold temperatures",
        "Model how temperature, food availability, body insulation, metabolic rate, and survival chance interact",
        "Describe how metabolic rate increases in cold temperatures and why that can be dangerous without enough food",
        "Use evidence from a model to explain why some animals thrive in winter while others migrate or hibernate"
    ],
    "vocabulary": [
        ("Insulation", "A layer that slows down heat loss — like fur, fat, or feathers that keep body heat from escaping"),
        ("Metabolic Rate", "How fast an animal's body burns energy to stay warm and alive — cold temperatures make it speed up"),
        ("Adaptation", "A body feature or behavior that helps an animal survive in its environment over many generations"),
        ("Hibernation", "A deep sleep-like state where an animal dramatically lowers its metabolic rate to save energy during winter"),
        ("Thermoregulation", "How an animal controls its body temperature — warm-blooded animals must maintain a constant internal temperature")
    ],
    "components": [
        ("Temperature", "The environmental temperature — how cold or warm it is outside, which the animal cannot control", True),
        ("Food Availability", "How much food is accessible in the environment — less food is available in winter for most animals", True),
        ("Body Insulation", "How well the animal's body prevents heat loss — thick fur, blubber, dense feathers all provide insulation", False),
        ("Metabolic Rate", "How fast the animal's body burns energy to maintain body temperature — colder conditions require faster energy burning", False),
        ("Survival Chance", "The overall probability that the animal will survive the season — depends on the balance between energy needs and energy supply", False)
    ],
    "think_about_it": "When Temperature drops, what happens to Metabolic Rate? How does Food Availability affect Survival Chance? How does Body Insulation change the relationship between temperature and survival?",
    "scenarios": [
        ("Mild Winter, Plenty of Food", "Set Temperature to 60% and Food Availability to 80% — a mild winter with abundant food"),
        ("Harsh Winter, Scarce Food", "Set Temperature to 10% and Food Availability to 20% — a brutal winter with very little food"),
        ("Harsh Winter, Abundant Food", "Set Temperature to 10% but Food Availability to 80% — cold but well-fed"),
        ("Comparing Insulation Levels", "Run the harsh winter scenario and observe what happens when Body Insulation is high vs. low")
    ],
    "sim_scenarios": [
        ("Mild Winter, Plenty of Food", "Temperature at 60%, Food Availability at 80%", "What do you predict will happen to Survival Chance when winter is mild and food is plentiful?"),
        ("Harsh Winter, Scarce Food", "Temperature at 10%, Food Availability at 20%", "What do you predict will happen to Metabolic Rate and Survival Chance in the worst conditions?"),
        ("Harsh Winter, Abundant Food", "Temperature at 10%, Food Availability at 80%", "Can abundant food make up for extreme cold? What do you predict?"),
        ("Comparing Insulation", "Harsh winter conditions with high vs. low Body Insulation", "How much difference does insulation make when everything else stays the same?")
    ],
    "discoveries": [
        "When temperature drops, metabolic rate increases — the animal's body works harder to generate heat, burning more energy",
        "Better body insulation reduces metabolic rate because less heat escapes, so the body does not have to work as hard to stay warm",
        "High metabolic rate without enough food is a death sentence — the animal burns through its energy reserves and cannot survive",
        "Animals survive winter through a combination of insulation (keeping heat in), food stores (energy supply), and in some cases hibernation (reducing energy demand)"
    ],
    "answer": "Arctic animals survive freezing winters through an amazing system of adaptations! Their thick fur, dense feathers, or layers of blubber provide incredible INSULATION that keeps body heat from escaping. This means their METABOLIC RATE does not have to spike as high as it would for a poorly insulated animal. They also store extra fat before winter and some cache food. The key is the BALANCE: insulation reduces how much energy the body needs to stay warm, and food provides the energy to keep the metabolism running. Animals that cannot insulate well enough either MIGRATE to warmer places, HIBERNATE to dramatically lower their metabolic rate, or sadly do not survive.",
    "stem_title": "Design the Ultimate Winter Survival Shelter",
    "stem_mission": "Design and test a shelter that keeps a cup of warm water from cooling down, using insulation principles from the animal survival model.",
    "stem_scenario": "A wildlife rescue center needs to build emergency warming shelters for injured animals during blizzards. Your engineering team must design a shelter using available materials that keeps a warm animal (represented by warm water) from losing heat to the cold environment. Use evidence from your model to choose insulating materials.",
    "stem_questions": [
        "Which insulating material keeps the warm water hottest for the longest time?",
        "How is your shelter design similar to how an arctic fox's fur works?",
        "Why do some materials insulate better than others — what do the best insulators have in common?"
    ],
    "stem_design_qs": [
        "What materials will you test as insulation (cotton balls, bubble wrap, aluminum foil, newspaper, fabric)?",
        "How will you measure heat loss over time (thermometer readings every 2 minutes)?",
        "How will you make sure your test is fair — same amount of water, same starting temperature?",
        "Can you combine materials to make even better insulation?"
    ],
    "career": "Wildlife Biologists and Conservation Scientists study how animals survive in different environments and develop plans to protect endangered species. They earn $55,000–$95,000/year.",
    "images": {
        "cover": ("cover-winter-survival.png", "A stunning close-up of an arctic fox in thick white winter fur against a snowy landscape, fur detail showing insulation layers, dramatic winter lighting with soft snowfall, cinematic wildlife photography"),
        "landscape": ("landscape-winter-survival.png", "A photorealistic image of diverse 4th grade students (9-10 years old) with a Black boy and an Asian American girl leading the group, examining animal fur samples and insulation materials at their desks in a bright modern classroom, natural window light, genuinely diverse group"),
        "modeling": ("modeling-winter-survival.png", "A photorealistic image of diverse 4th grade students (9-10 years old) with a Latina girl taking the lead at the laptop, working together building a digital animal survival model on screen, modern classroom with animal adaptation posters, balanced diversity with varied hairstyles"),
        "discussion": ("discussion-winter-survival.png", "A photorealistic image of a White female teacher leading a discussion with diverse 4th graders (9-10 years old) about how animals survive winter, showing images of arctic animals on a smartboard, students with hands raised, balanced diversity"),
        "stem": ("stem-winter-survival.png", "A photorealistic image of diverse 4th grade students (9-10 years old) with a White boy and Black girl working together in the foreground, wrapping cups of warm water in different insulating materials, thermometers visible, excited and engaged, balanced diversity")
    },
    "pre_assessment": [
        "How do you think polar bears stay warm when it is -40 degrees outside?",
        "Why do some animals leave (migrate) before winter instead of staying?",
        "Draw what you think is inside an arctic animal's fur or skin that keeps it warm.",
        "If an animal gets very cold, what do you think its body does to try to warm up?"
    ],
    "extend_components": [
        ("Body Size", "Larger animals lose heat more slowly because they have less surface area compared to their volume — this is why arctic animals tend to be large"),
        ("Activity Level", "How much the animal moves — more movement generates more heat but also burns more energy"),
        ("Group Behavior", "Whether the animal huddles with others — penguins huddle to share body heat and reduce heat loss")
    ],
    "reflections": [
        "Why do arctic animals tend to have thicker fur and more body fat than animals in warm climates?",
        "If an animal cannot find enough food in winter, what are its options for survival?",
        "How is wearing a winter coat similar to an animal having thick fur?",
        "Why is hibernation a successful survival strategy — what does it do to metabolic rate?",
        "How did your model help you understand why some animals survive winter easily while others struggle?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a five-component model showing how temperature and food availability interact with body insulation and metabolic rate to determine an animal's survival chance."),
        ("Disciplinary Core Idea", "LS1.A Structure and Function", "Plants and animals have both internal and external structures that serve various functions in growth, survival, behavior, and reproduction. Body insulation is an internal structure that functions to maintain body temperature."),
        ("Crosscutting Concept", "Systems and System Models", "Students explore an animal survival system with multiple interacting components, competing influences, and emergent outcomes that depend on the balance between energy supply and energy demand.")
    ],
    "cast_items": [
        "Explain how body insulation helps animals survive cold temperatures by reducing heat loss",
        "Use a model to describe the relationship between temperature, metabolic rate, and survival",
        "Construct an argument for why different animals have different winter survival strategies"
    ],
    "cast_questions": [
        ("Multiple Choice:", "An arctic fox has very thick fur while a desert fox has thin fur. Which best explains why the arctic fox's thick fur helps it survive?"),
        ("Constructed Response:", "Using what you know about insulation, metabolic rate, and survival, explain why some animals hibernate during winter instead of staying active. Use the words 'metabolic rate,' 'insulation,' and 'energy' in your answer.")
    ],
    "background_intro": "Every winter, animals face a life-or-death challenge: stay warm enough to survive while having enough energy to fuel their bodies. The strategies animals use — from thick fur to hibernation to migration — are the result of millions of years of evolution solving this energy balance problem.",
    "background_sections": [
        ("The Cold Challenge", "Warm-blooded animals (mammals and birds) must maintain a constant internal body temperature regardless of the outside temperature. A human's body stays at about 98.6 degrees F (37 degrees C) whether it is 100 degrees F or -20 degrees F outside. This is called thermoregulation. In cold weather, heat constantly flows from the warm body to the cold environment. The bigger the temperature difference, the faster heat escapes. An animal must generate enough internal heat to replace what is lost, or its body temperature drops and it dies."),
        ("Insulation: The First Line of Defense", "Insulation is any material that slows down heat transfer. In animals, insulation takes several forms: fur (mammals), feathers (birds), and blubber or fat layers (marine mammals, bears). Arctic animals have evolved remarkable insulation. Polar bear fur has two layers — a dense underfur and longer guard hairs that trap air close to the skin. Penguin feathers are so dense that they create a nearly waterproof layer that traps warm air. A walrus's blubber can be 6 inches thick, creating an insulating barrier between warm blood and freezing ocean water."),
        ("Metabolic Rate: The Energy Engine", "Metabolism is the process of converting food into energy. Metabolic rate measures how fast this happens. In cold conditions, an animal's metabolic rate increases because the body needs to generate more heat to maintain its temperature. This means the animal needs MORE food in winter — exactly when food is often scarce. This creates a dangerous energy equation: the colder it is, the more energy the body needs, but the harder food is to find."),
        ("Survival Strategies: Insulate, Migrate, or Hibernate", "Animals have evolved three main strategies for surviving winter. First, INSULATE: grow thick fur, feathers, or fat to reduce heat loss and keep metabolic rate manageable (arctic fox, polar bear, snowy owl). Second, MIGRATE: travel to warmer areas where food is plentiful and heat loss is lower (monarch butterfly, arctic tern, caribou). Third, HIBERNATE: dramatically reduce metabolic rate to near-zero, living off stored fat, and barely using any energy for months (ground squirrels, some bears, wood frogs). Each strategy solves the same problem differently — balancing energy supply with energy demand.")
    ],
    "lever_L": "Students identify Temperature and Food Availability as external components (environmental conditions the animal cannot control) and Body Insulation, Metabolic Rate, and Survival Chance as internal components that respond to conditions.",
    "lever_E": "Students determine that lower Temperature increases Metabolic Rate (negative), Food Availability increases Survival (positive), Body Insulation decreases Metabolic Rate (negative — insulation reduces energy needs), and high Metabolic Rate decreases Survival (negative — burning too much energy without food is fatal).",
    "lever_V": "Students build a five-component model showing competing influences on survival: temperature drives up metabolic rate while insulation drives it down, and food availability must match energy demand for the animal to survive.",
    "lever_Ev": "Students run four scenarios to observe how changing temperature and food availability creates different survival outcomes, and how insulation acts as a buffer that shifts the survival threshold.",
    "lever_R": "Students add body size or group behavior to explore why arctic animals tend to be larger (less surface area per volume = less heat loss) and why penguins huddle in groups.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with arctic animals in winter landscape", "say": "Right now, at the North Pole, it is negative 30 degrees. A polar bear is walking around in a T-shirt of fur. How is that possible?", "do": "Show images of arctic animals in extreme cold. Ask: How do THEY survive when WE would freeze in minutes?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are building a model of SURVIVAL — figuring out what makes the difference between an animal that thrives in winter and one that does not.", "do": "Have students read objectives aloud. Pre-teach metabolic rate using the analogy of a car engine running faster in cold weather.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How do arctic animals survive freezing temperatures?", "say": "Your body temperature is 98.6 degrees. An arctic fox keeps the same temperature in minus 50 degree weather. How?", "do": "Have students turn and talk: What do you think arctic animals have that we do not?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps with five components previewed", "say": "Our model today has two things the ENVIRONMENT controls and three things that happen inside the animal's body.", "do": "Preview five components. Explain the concept of external = environment and internal = the animal's body response.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Five component cards for animal survival system", "say": "Can the animal control the temperature? Can it control how much food is in the forest? These are things that happen TO it.", "do": "Guide sorting. Temperature and Food Availability are external (the environment controls them). Body Insulation, Metabolic Rate, and Survival Chance are internal.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows with + and - connections", "say": "Here is the key — when temperature DROPS, metabolic rate goes UP. That is a NEGATIVE relationship. Why is high metabolic rate dangerous?", "do": "Help students map relationships. Focus on the negative connections and why they create a survival challenge.", "time": "10 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph showing all five components changing across scenarios", "say": "Let us send our animal into the worst winter possible and see what happens. Then let us give it thick fur and see if it survives.", "do": "Run mild winter first, then harsh winter (students see survival drop), then harsh winter with good insulation (survival recovers).", "time": "12 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings with animal strategy comparison", "say": "Now we know WHY arctic animals have thick fur — it is not just about being warm, it is about keeping metabolic rate LOW so they do not burn through their energy.", "do": "Compare three strategies: insulate, migrate, hibernate. Which solves the energy equation differently?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Insulation shelter design challenge", "say": "You are wildlife rescue engineers. Design a shelter that keeps this warm water from losing heat — just like fur keeps an animal warm!", "do": "Distribute materials (cups, warm water, thermometers, cotton, bubble wrap, foil, newspaper). Groups test insulation and record temperature every 2 minutes.", "time": "12 min"}
    ],
    "sort_reasoning": "Temperature and Food Availability are external because they are environmental conditions that exist independently of the animal — the weather and the ecosystem determine these, not the animal. Body Insulation, Metabolic Rate, and Survival Chance are internal because they are properties of or responses within the animal's body that change based on environmental conditions.",
    "relationships": [
        ("Temperature to Metabolic Rate", "NEGATIVE (-)", "When temperature DROPS (gets colder), metabolic rate INCREASES — the animal's body works harder to generate heat. In freezing conditions, the body burns energy much faster than in mild weather. This is a negative relationship because the variables move in opposite directions."),
        ("Food Availability to Survival Chance", "POSITIVE (+)", "More food means more energy available to fuel the body's metabolic needs. When food is plentiful, the animal can sustain a high metabolic rate and survive. When food is scarce, the animal runs out of energy and survival drops."),
        ("Body Insulation to Metabolic Rate", "NEGATIVE (-)", "Better insulation means less heat escapes from the body, so the body does not need to burn energy as fast to stay warm. A well-insulated animal has a LOWER metabolic rate in the same cold conditions compared to a poorly insulated animal."),
        ("Metabolic Rate to Survival Chance", "NEGATIVE (-)", "A HIGHER metabolic rate means the animal is burning through its energy reserves faster. If the animal cannot replace that energy through food, high metabolic rate leads to starvation and death. This is why uncontrolled high metabolic rate is dangerous."),
        ("Food Availability to Body Insulation", "POSITIVE (+)", "More food allows the animal to build up fat stores, which provide both energy reserves and physical insulation. Well-fed animals develop thicker fat layers before winter, improving their insulation. Starving animals lose fat and become poorly insulated.")
    ],
    "sim_answers": [
        ("Mild Winter, Plenty of Food", "With Temperature at 60% and Food at 80%, Metabolic Rate stays moderate because the animal does not need to generate excessive heat. Food Availability is high, so the energy supply easily meets the demand. Survival Chance is very high. Most animals handle mild winters well."),
        ("Harsh Winter, Scarce Food", "With Temperature at 10% and Food at 20%, Metabolic Rate spikes because the body is fighting to stay warm in extreme cold. But Food Availability is too low to sustain that high burn rate. The animal depletes its energy reserves rapidly. Body Insulation may help somewhat, but without food, Survival Chance plummets. This is why many animals die in harsh winters with food shortages.")
    ],
    "reflection_exemplars": [
        ("Why do arctic animals have thick fur?", "Arctic animals have thick fur because it provides insulation that dramatically slows heat loss from their bodies. Our model showed that when insulation is high, the animal's metabolic rate stays lower — the body does not have to burn energy as fast to maintain temperature. This means the animal needs LESS food to survive, which is critical when food is scarce in winter. Thick fur is not just about comfort — it is about keeping the energy equation balanced so the animal can survive on the food available."),
        ("Why do some animals hibernate instead of staying active?", "Hibernation is a strategy for animals that cannot find enough food to fuel a high winter metabolic rate and do not have enough insulation to keep metabolic rate low. By entering hibernation, they drop their metabolic rate to near zero — their heart rate, breathing, and body temperature all plummet. They survive on stored body fat for months, burning almost no energy. Our model shows that when metabolic rate is high and food is low, survival drops. Hibernation solves this by making metabolic rate nearly zero, so even without food, the animal survives.")
    ],
    "stem_intro": "Present the challenge: A wildlife rescue center needs emergency warming shelters for injured animals during winter storms. Your team must design and test a shelter that keeps a cup of warm water from cooling down using insulating materials. The best shelter will lose the least heat over 10 minutes. Use your model evidence about insulation and heat loss to choose your materials!",
    "stem_concepts": [
        ("Insulation Slows Heat Transfer", "Just like animal fur traps air close to the body, good insulating materials trap air in small pockets. Air is a poor conductor of heat, so trapped air slows down heat loss. Materials like cotton, bubble wrap, and feathers work because they trap lots of air."),
        ("The Energy Balance", "Survival depends on balancing energy loss with energy supply. Your shelter cannot GIVE the warm water more heat, but it can SLOW DOWN heat loss — just like insulation helps an animal by reducing how fast it needs to burn energy."),
        ("Layering Effect", "Many animals have multiple insulation layers (underfur + guard hairs + fat). Combining insulation materials can be more effective than using a single material because each layer traps additional air and creates another barrier to heat flow.")
    ],
    "stem_eval": [
        ("Expert (4)", "Tests multiple insulating materials, records temperature data accurately, explains why the best material works using insulation and heat loss concepts from the model"),
        ("Proficient (3)", "Tests at least two materials, records data, and can explain why insulation slows heat loss"),
        ("Developing (2)", "Builds a shelter and records some data but struggles to connect insulation to the survival model"),
        ("Beginning (1)", "Shelter is incomplete or student cannot explain how insulation relates to animal survival")
    ],
    "support": [
        "Provide a labeled diagram comparing a well-insulated animal (thick fur, low metabolic rate) to a poorly insulated animal (thin fur, high metabolic rate) in the same cold temperature",
        "Let students feel the difference between putting their hand in a mitten versus holding it in the air on a cold day — the mitten does not CREATE heat, it just keeps YOUR heat from escaping",
        "Sentence frames: 'When Temperature drops, Metabolic Rate __ because __. Body Insulation helps by __ which means __.'"
    ],
    "extensions": [
        "Research the Emperor penguin huddle — how does group behavior change the effective insulation and survival of individual penguins?",
        "Compare the fur of an arctic fox in summer vs. winter — how does the animal change its insulation seasonally?",
        "Calculate how many calories a hibernating bear burns per day vs. an active bear and determine how long its fat stores would last in each state"
    ],
    "cross_curr": [
        ("Math", "Create a line graph showing temperature over 10 minutes for cups wrapped in different insulating materials, then calculate the rate of heat loss per minute for each"),
        ("ELA", "Write a survival journal from the perspective of an arctic fox during the coldest week of winter, incorporating science vocabulary about insulation, metabolism, and energy"),
        ("Social Studies", "Research how Indigenous Arctic peoples (Inuit, Yupik) designed clothing and shelters using animal insulation principles — sealskin, caribou fur, igloos that trap warm air")
    ],
    "misconceptions": [
        ("Fur and coats create heat", "Insulation does NOT create heat — it only SLOWS the loss of heat that the body is already producing. A coat does not warm you up; it keeps YOUR body heat from escaping into the cold air. If you put a coat on a snowman, it would actually stay frozen LONGER because the coat would keep cold air from warming the snow.", "Wrap a thermometer in a blanket and check it after 10 minutes — it stays at room temperature because the blanket is not creating heat, just trapping it."),
        ("Animals do not feel cold because they have fur", "Arctic animals DO feel cold, and their bodies DO respond to it. Their metabolic rate increases in cold weather just like ours does. The difference is that their insulation is so effective that the metabolic increase is manageable. A polar bear in extreme cold still burns more energy than a polar bear in mild weather — the fur just makes the difference smaller.", "Compare metabolic rate data for arctic animals in summer vs. winter — their energy use still increases, just not as dramatically as it would without insulation."),
        ("Hibernation is just sleeping", "Hibernation is NOT sleep — it is a dramatic physiological shutdown. A hibernating ground squirrel's heart rate drops from 200 beats per minute to about 5. Its body temperature drops from 98 degrees F to just above freezing. It breathes only once or twice per minute. This is a controlled near-death state that allows the animal to survive months without eating by burning almost zero energy.", "Show students a comparison chart: active bear (40 heartbeats/min, 98 degrees F) vs. hibernating bear (8 heartbeats/min, 88 degrees F). It is not just sleeping with the lights off!")
    ]
}

L04 = {
    "id": "G04L2-L04",
    "title": "The Mountain That Used to Be an Ocean",
    "subtitle": "How Seashells End Up on Mountaintops Millions of Years Later",
    "ngss": "4-ESS1-1, 4-ESS2-1",
    "ngss_desc": "Identify evidence from patterns in rock formations and fossils in rock layers to support an explanation for changes in a landscape over time. Make observations and measurements to identify materials based on their properties.",
    "big_question": "How is it possible to find fossils of ocean creatures on top of mountains that are thousands of feet above sea level?",
    "objectives": [
        "Explain how tectonic plate movement creates the forces that push ocean floors upward into mountains",
        "Model how plate movement speed, sediment deposit rate, compression force, rock uplift, and fossil elevation interact",
        "Describe how fossils trapped in ocean sediment layers can end up at high elevations over millions of years",
        "Use evidence from a model to explain why the Himalayas contain fossils of sea creatures"
    ],
    "vocabulary": [
        ("Tectonic Plates", "Giant slabs of rock that make up Earth's outer surface — they float on hot, slow-moving rock beneath and move very slowly over time"),
        ("Compression", "The squeezing force that happens when two tectonic plates push into each other, crushing and folding rock layers"),
        ("Uplift", "The process of rock being pushed upward by tectonic forces — this is how flat ocean floors become towering mountains"),
        ("Sediment", "Tiny particles of sand, mud, and dead organisms that settle on the ocean floor and build up in layers over millions of years"),
        ("Fossil", "The preserved remains or traces of ancient living things found in rock — they tell us what lived in a place millions of years ago")
    ],
    "components": [
        ("Plate Movement Speed", "How fast the tectonic plates are pushing toward each other — faster movement creates more force", True),
        ("Sediment Deposit Rate", "How fast layers of sediment (sand, mud, shells) accumulate on the ocean floor — more sediment means thicker layers with more fossils", True),
        ("Compression Force", "The pressure created when two plates collide — more speed means more compression, which squeezes and folds rock layers", False),
        ("Rock Uplift", "How quickly the compressed rock layers are pushed upward — stronger compression creates faster uplift", False),
        ("Fossil Elevation", "The height above sea level where ocean fossils end up — determined by both how thick the sediment layers are and how much uplift has occurred", False)
    ],
    "think_about_it": "When Plate Movement Speed increases, what happens to Compression Force? How does Compression Force affect Rock Uplift? Where do the fossils end up?",
    "scenarios": [
        ("Fast Collision, Thick Sediment", "Set Plate Movement Speed to 80% and Sediment Deposit Rate to 80% — like the formation of the Himalayas"),
        ("Slow Collision, Thin Sediment", "Set Plate Movement Speed to 20% and Sediment Deposit Rate to 20% — slow, gentle mountain building"),
        ("No Movement", "Set Plate Movement Speed to 0% — what happens when plates stop moving?"),
        ("Fast Collision, Thin Sediment", "Set Plate Movement Speed to 80% but Sediment Deposit Rate to 20% — strong forces but few fossil layers")
    ],
    "sim_scenarios": [
        ("Fast Collision, Thick Sediment", "Plate Movement Speed at 80%, Sediment Deposit Rate at 80%", "What do you predict will happen to Fossil Elevation when plates collide fast and sediment layers are thick?"),
        ("Slow Collision, Thin Sediment", "Plate Movement Speed at 20%, Sediment Deposit Rate at 20%", "Will mountains still form if the plates are barely moving? How high will fossils get?"),
        ("No Movement", "Plate Movement Speed at 0%", "What happens to all the internal components when plates stop moving entirely?"),
        ("Fast Collision, Thin Sediment", "Plate Movement Speed at 80%, Sediment Deposit Rate at 20%", "If plates collide fast but there is little sediment, will we find many fossils at high elevations?")
    ],
    "discoveries": [
        "Tectonic plate collisions create compression forces that squeeze and fold rock, pushing it upward — this is how mountains form",
        "Ocean sediment layers containing fossils of marine creatures get caught in this uplift and are carried to high elevations over millions of years",
        "Faster plate movement creates stronger compression, which causes faster rock uplift and higher fossil elevation",
        "Both plate movement and sediment deposits contribute to fossil elevation — you need thick sediment layers (with fossils in them) AND strong uplift to find ocean fossils on mountaintops"
    ],
    "answer": "Finding seashells on mountaintops is one of geology's greatest detective stories! Millions of years ago, the rock that makes up mountains like the Himalayas was at the bottom of an ancient ocean. Sea creatures lived, died, and were buried in layers of sediment on the ocean floor. Then tectonic plates began colliding. The enormous COMPRESSION FORCE from the collision squeezed and folded the ocean floor rock, pushing it UPWARD in a process called UPLIFT. Over millions of years, what was once the bottom of the sea was pushed kilometers into the sky — carrying the fossils of ancient sea creatures with it. Mount Everest's summit is made of limestone that formed from ocean sediment containing the shells of creatures called crinoids!",
    "stem_title": "Build a Tectonic Collision Model",
    "stem_mission": "Design a hands-on model that demonstrates how tectonic plate collisions push ocean floor layers (with fossils) upward into mountains.",
    "stem_scenario": "A natural history museum wants a hands-on exhibit that shows visitors how ocean fossils end up on mountains. Your engineering team must build a physical model using layered materials that demonstrates how plate collision, compression, and uplift work together to push ocean floor sediment (with fossils) to high elevations.",
    "stem_questions": [
        "How will you show the layers of sediment that build up on the ocean floor?",
        "How will you demonstrate what happens when two plates collide and compress the layers?",
        "Can visitors see the fossils moving from the bottom to the top as uplift occurs?"
    ],
    "stem_design_qs": [
        "What materials will you use for rock layers (clay, foam, towels, construction paper)?",
        "How will you represent fossils inside the layers (small shells, beads, stickers)?",
        "How will you simulate tectonic plate collision (pushing from both sides)?",
        "How will you show visitors that the fossils moved from sea level to mountaintop level?"
    ],
    "career": "Geologists and Paleontologists study Earth's rocks, fossils, and history to understand how our planet has changed over billions of years. They discover ancient oceans, vanished continents, and extinct creatures. They earn $60,000–$110,000/year.",
    "images": {
        "cover": ("cover-mountain-ocean.png", "A dramatic split image showing the same rock formation as ocean floor with marine fossils underwater on one side and as a towering mountain peak with visible fossil layers on the other side, cinematic geological photography"),
        "landscape": ("landscape-mountain-ocean.png", "A photorealistic image of diverse 4th grade students (9-10 years old) with a Latino boy and Asian American girl leading the group, examining real fossil specimens and rock samples at their desks in a bright modern classroom, natural window light, genuinely diverse group"),
        "modeling": ("modeling-mountain-ocean.png", "A photorealistic image of diverse 4th grade students (9-10 years old) with a Black boy taking the lead at the laptop, working together building a digital tectonic plate model on screen, modern classroom with geological posters showing plate boundaries, balanced diversity"),
        "discussion": ("discussion-mountain-ocean.png", "A photorealistic image of an Asian American male teacher leading a discussion with diverse 4th graders (9-10 years old) about how mountains form, showing a cross-section diagram of colliding plates on a smartboard, students with hands raised, balanced diversity"),
        "stem": ("stem-mountain-ocean.png", "A photorealistic image of diverse 4th grade students (9-10 years old) with a White girl and Latino boy in the foreground, building layered models from colored clay with small shells embedded in the layers, pushing the layers together to simulate plate collision, balanced diversity")
    },
    "pre_assessment": [
        "Have you ever found a seashell far from the ocean? Where do you think it came from?",
        "How do you think mountains are formed? Do they grow, or are they pushed up?",
        "Draw what you think the ground under a mountain looks like — are the layers flat or folded?",
        "What would it mean to find a fossil of a fish on top of a mountain?"
    ],
    "extend_components": [
        ("Erosion Rate", "How fast wind and water wear down the mountain after it forms — erosion can expose or destroy fossils"),
        ("Rock Type", "Whether the rock is hard or soft affects how much it deforms during compression — soft rock folds while hard rock cracks"),
        ("Time Scale", "How many millions of years the process has been happening — more time means more uplift and higher mountains")
    ],
    "reflections": [
        "How can finding a seashell on a mountaintop tell us about the history of that place?",
        "Why do mountains like the Himalayas have fossils of ocean creatures but mountains like volcanic islands do not?",
        "If tectonic plates suddenly stopped moving, would mountains keep growing? Why or why not?",
        "How is squeezing play dough between your hands similar to what happens when tectonic plates collide?",
        "How did your model help you understand something that takes millions of years to happen?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a five-component model showing how plate movement and sediment deposition interact through compression and uplift to determine fossil elevation over geological time."),
        ("Disciplinary Core Idea", "ESS1.C The History of Planet Earth / ESS2.A Earth Materials and Systems", "Local, regional, and global patterns of rock formations reveal changes over time due to Earth forces such as tectonic plate movement. Fossils provide evidence of organisms that lived long ago."),
        ("Crosscutting Concept", "Cause and Effect", "Students trace a chain of cause and effect from plate movement to compression to uplift to fossil elevation, demonstrating how slow, persistent forces create dramatic results over millions of years.")
    ],
    "cast_items": [
        "Explain how tectonic plate movement creates compression forces that push rock upward",
        "Use a model to describe how ocean fossils end up at high elevations",
        "Identify fossil evidence that supports the explanation that mountains were once under the ocean"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Scientists find fossils of ancient sea creatures in rock layers near the top of the Himalayan mountains. Which best explains how those fossils got there?"),
        ("Constructed Response:", "Using what you know about tectonic plates, compression, and uplift, explain how a fossil of a sea creature could end up on a mountain that is 5 miles above the ocean. Use the words 'plate movement,' 'compression,' and 'uplift' in your answer.")
    ],
    "background_intro": "One of the most astonishing facts in science is that the tallest mountains on Earth were once at the bottom of the ocean. The evidence is literally written in stone — marine fossils found at elevations of over 25,000 feet. Understanding how this happened requires thinking about Earth processes that operate over millions of years.",
    "background_sections": [
        ("Earth's Moving Puzzle", "Earth's outer layer (lithosphere) is broken into about 15 major tectonic plates that float on the hot, partially molten rock beneath (asthenosphere). These plates move very slowly — typically 2-10 centimeters per year, about as fast as your fingernails grow. But over millions of years, this slow movement has rearranged entire continents, opened and closed oceans, and built the world's greatest mountain ranges."),
        ("Ocean Floors Become Mountains", "The Himalayan mountains are the best example of ocean floor becoming mountaintop. About 200 million years ago, the Indian Plate was a separate landmass far south of Asia. Between India and Asia lay the Tethys Sea, a vast ocean. For millions of years, sea creatures lived and died in this ocean, their shells settling to the bottom and becoming part of the sediment layers. Starting about 50 million years ago, the Indian Plate collided with the Asian Plate. The enormous compression force began folding and pushing up the ocean floor."),
        ("Compression, Folding, and Uplift", "When two continental plates collide, neither can sink beneath the other (unlike ocean plates, which are denser). Instead, the collision crumples and folds the rock layers like pushing two pieces of paper together on a desk — they buckle upward. This folding and uplift is what creates mountains. The Himalayas are STILL growing today — the Indian Plate continues to push into Asia at about 5 cm per year, and Mount Everest grows about 4 mm taller each year."),
        ("Fossils as Evidence", "The fossils found in Himalayan rock are the definitive proof that this rock was once ocean floor. Scientists have found fossils of ammonites (ancient shelled sea creatures), crinoids (sea lilies), and marine brachiopods at elevations above 25,000 feet on Mount Everest. The limestone summit of Everest is made of compressed ocean sediment. These fossils could not have formed at that elevation — they MUST have formed at sea level and been carried up by tectonic forces.")
    ],
    "lever_L": "Students identify Plate Movement Speed and Sediment Deposit Rate as external components (geological conditions) and Compression Force, Rock Uplift, and Fossil Elevation as internal components that respond to those conditions over geological time.",
    "lever_E": "Students determine that Plate Movement Speed positively affects Compression Force, Compression Force positively affects Rock Uplift, Sediment Deposit Rate positively affects Fossil Elevation, and Rock Uplift positively affects Fossil Elevation — a system with converging inputs.",
    "lever_V": "Students build a five-component model showing how plate collision creates compression that drives uplift, while sediment deposits determine how many fossil-bearing layers are available to be lifted.",
    "lever_Ev": "Students run four scenarios (fast/thick, slow/thin, no movement, fast/thin) to observe how both inputs contribute to fossil elevation and what happens when one or both are absent.",
    "lever_R": "Students add erosion rate to explore why some mountains with fossils are shorter than expected — erosion removes material from the top even as uplift pushes from below.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with mountain peak and ocean fossil imagery", "say": "I have a mystery for you. Scientists found SEASHELLS on top of Mount Everest — five miles above the ocean. How did ocean creatures get to the top of the tallest mountain on Earth?", "do": "Show a real photo of marine fossils found on Himalayan peaks. Let students react and discuss initial ideas.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are going to model something that took FIFTY MILLION YEARS to happen — but we will do it in one class period!", "do": "Have students read objectives aloud. Pre-teach tectonic plates, compression, and uplift with hand gestures.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How do ocean fossils end up on mountaintops?", "say": "The fossils on Everest are NOT from a flood. They are from the actual ocean floor. The entire mountain used to be under the sea.", "do": "Have students turn and talk: What force could possibly push the ocean floor five miles into the sky?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps with five components previewed", "say": "Our model has two things that EARTH controls and three responses that happen over millions of years.", "do": "Preview all five components. Emphasize the time scale — these processes are incredibly slow but incredibly powerful.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Five component cards for tectonic system", "say": "Can we control how fast tectonic plates move? No — Earth controls that. Can we control how much sediment piles up on the ocean floor? No — nature controls that too.", "do": "Guide sorting. Both externals are geological processes humans cannot control. All three internals are results of those processes.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows — all positive in this model", "say": "Notice something special about this model — ALL the relationships are POSITIVE. More plate movement leads to more compression leads to more uplift leads to higher fossils.", "do": "Help students draw the chain of positive relationships. Discuss why all positive creates a system where everything amplifies.", "time": "10 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph showing fossil elevation climbing over time", "say": "Watch the Fossil Elevation line climb as we run the fast collision scenario. Remember — in real life, this took fifty million years!", "do": "Run scenarios in order. The no-movement scenario shows nothing happening. The fast/thick scenario shows dramatic fossil elevation.", "time": "12 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Before and after diagram of ocean floor to mountain", "say": "The answer to our mystery: the mountain DID NOT rise up from the land — the OCEAN FLOOR was pushed up to become the mountain!", "do": "Show the geological time sequence: ocean floor with creatures, sediment building, plates colliding, mountain rising with fossils.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Tectonic collision model design challenge", "say": "Build a model that shows a museum visitor exactly how this works — layers of ocean sediment with fossils getting pushed up by plate collision.", "do": "Distribute materials (colored clay/play dough, small shells/beads, cardboard plates). Groups build layered models and simulate collision.", "time": "12 min"}
    ],
    "sort_reasoning": "Plate Movement Speed and Sediment Deposit Rate are external because they are geological processes driven by Earth's internal heat and ocean chemistry — they happen independently of the mountain-building results. Compression Force, Rock Uplift, and Fossil Elevation are internal because they are direct consequences of plate movement and sedimentation interacting over time.",
    "relationships": [
        ("Plate Movement Speed to Compression Force", "POSITIVE (+)", "Faster plate movement means more energy is transferred when plates collide, creating stronger compression forces. The Indian Plate crashing into Asia at 5 cm/year generates enormous compression that folds and crumples rock layers."),
        ("Compression Force to Rock Uplift", "POSITIVE (+)", "Greater compression force pushes rock layers upward more powerfully. Stronger squeezing means more folding, more crumpling, and faster uplift. This is why rapidly colliding plates create the tallest mountains."),
        ("Sediment Deposit Rate to Fossil Elevation", "POSITIVE (+)", "More sediment accumulation on the ocean floor means thicker layers of fossil-bearing rock. When uplift occurs, thicker layers result in fossils being found at a wider range of elevations. High sedimentation areas produce mountains rich with fossils at many levels."),
        ("Rock Uplift to Fossil Elevation", "POSITIVE (+)", "More uplift pushes the entire rock column higher, carrying embedded fossils to greater elevations. This is the direct mechanism that moves ocean floor fossils from sea level to mountaintop heights.")
    ],
    "sim_answers": [
        ("Fast Collision, Thick Sediment", "With Plate Movement at 80% and Sediment Deposit at 80%, Compression Force is very high, Rock Uplift is rapid, and Fossil Elevation climbs dramatically. This is the Himalayan scenario — fast collision with thick sediment layers produces the highest mountains with the most fossils. Marine fossils end up at extreme elevations."),
        ("No Movement", "With Plate Movement Speed at 0%, Compression Force drops to zero, Rock Uplift stops, and Fossil Elevation remains at its current level. If plates stopped moving, mountains would stop growing. Existing mountains would slowly erode away over millions of years. The fossils would stay where they are until erosion exposes or destroys them.")
    ],
    "reflection_exemplars": [
        ("How can a seashell on a mountaintop tell us about history?", "A seashell fossil on a mountaintop is evidence that tells us two things: first, that location was once under the ocean (because the creature that made the shell lived in the sea), and second, that enormous tectonic forces pushed that ocean floor upward over millions of years. The fossil is like a message from the past — it tells us what that place used to be. Without understanding plate tectonics, finding seashells on mountains would be a complete mystery."),
        ("If plates stopped moving, would mountains keep growing?", "No. Mountains grow because of the compression force created by plate collision. If plates stopped, there would be no more compression, no more uplift, and no more growth. In fact, mountains would start SHRINKING because erosion from wind and rain would wear them down with nothing pushing them back up. Over millions of years, even the tallest mountains would be worn flat. The only reason the Himalayas are still growing is because the Indian Plate is still pushing.")
    ],
    "stem_intro": "Present the challenge: A natural history museum wants a hands-on exhibit showing how ocean fossils get to mountaintops. Build a layered model with 'fossils' embedded in 'sediment layers' and demonstrate what happens when 'tectonic plates' collide by pushing from both sides. Visitors should be able to see the fossils move from the bottom to the top!",
    "stem_concepts": [
        ("Layered Sediment", "Ocean sediment builds up in layers over millions of years, with each layer containing the fossils of creatures that lived during that time period. Your model should show distinct colored layers with small objects representing fossils."),
        ("Plate Collision", "When two continental plates collide, the enormous force folds and crumples the rock layers, pushing them upward. Demonstrate this by pushing your layered materials together from both sides."),
        ("Time Scale", "This process takes millions of years. The Himalayas have been forming for about 50 million years and are still growing. Your model compresses millions of years into seconds.")
    ],
    "stem_eval": [
        ("Expert (4)", "Model clearly shows layered sediment with embedded fossils being uplifted through plate collision, student explains the process using tectonic vocabulary and connects to real-world examples"),
        ("Proficient (3)", "Model demonstrates layers and collision, student can explain how fossils move from bottom to top"),
        ("Developing (2)", "Model shows some layers but collision demonstration is unclear, student struggles to explain the process"),
        ("Beginning (1)", "Model is incomplete or student cannot explain the connection between plate movement and fossil elevation")
    ],
    "support": [
        "Provide a step-by-step visual showing the process: 1) ocean floor with creatures, 2) sediment layers building, 3) plates start to collide, 4) layers fold upward, 5) mountain with fossils at the top",
        "Let students push two stacks of towels together from opposite sides — they will see the towels fold and rise up, just like rock layers during plate collision",
        "Sentence frames: 'When Plate Movement Speed increases, Compression Force __ which causes Rock Uplift to __ and Fossil Elevation to __.'"
    ],
    "extensions": [
        "Research the formation of the Appalachian Mountains — they are much older and shorter than the Himalayas. What does this tell us about erosion over time?",
        "Map the major tectonic plate boundaries around the world and identify where the tallest mountains are — is there a pattern?",
        "Calculate how many years it would take for Mount Everest to double its height at the current growth rate of 4 mm per year"
    ],
    "cross_curr": [
        ("Math", "If tectonic plates move at 5 cm per year, calculate how far the Indian Plate has moved in 50 million years. Convert to kilometers."),
        ("ELA", "Write a creative time-lapse narrative from the perspective of a fossil — from being a living sea creature to being discovered on a mountaintop millions of years later"),
        ("Geography", "Create a map showing where the Tethys Sea once existed and where its fossils are found today across the Himalayan mountain range")
    ],
    "misconceptions": [
        ("Mountains grow up from the ground like plants", "Mountains do NOT grow from below. They are pushed UP by the horizontal collision of tectonic plates. When two plates crash into each other, the rock has nowhere to go but up. It is like pushing two pieces of paper together on a table — they buckle and rise upward. Mountains are made of rock that was originally at or below the surface and was forced upward by compression.", "Push two stacks of paper or towels together from opposite sides on a desk. Watch them fold and rise. That is exactly how mountains form."),
        ("The ocean used to be much higher and covered the mountains", "The fossils on mountains are NOT from a time when the ocean was higher. The rock itself was UNDER the ocean and was pushed UP by plate movement. The ocean did not drain away — the ocean floor was lifted out of the water. This is proven by the fact that the fossils are embedded deep within the rock layers, not just sitting on the surface.", "Show layers of clay with shells embedded inside, not on top. The shells are PART of the rock layers, proving they formed at the same time as the rock — on the ocean floor."),
        ("This all happened a long time ago and is done", "Mountain building is NOT a thing of the past — it is happening RIGHT NOW. The Himalayas are still growing because the Indian Plate is still pushing into Asia. Mount Everest grows about 4 mm taller every year. Earthquakes in the Himalayan region are caused by the same plate collision that is still building the mountains.", "Show students current GPS data showing the Indian Plate is still moving north at about 5 cm/year. Mountains are being built under our feet, just too slowly for us to notice.")
    ]
}

L05 = {
    "id": "G04L2-L05",
    "title": "Can We Power a City with Wind?",
    "subtitle": "The Science and Challenge of Renewable Energy for Everyone",
    "ngss": "4-ESS3-1, 4-PS3-1",
    "ngss_desc": "Obtain and combine information to describe that energy and fuels are derived from natural resources and their uses affect the environment. Use evidence to construct an explanation relating the speed of an object to the energy of that object.",
    "big_question": "If wind is free and everywhere, why can we not just use wind turbines to power every city in the world?",
    "objectives": [
        "Explain how wind turbines convert the kinetic energy of moving air into electrical energy",
        "Model how wind speed, number of turbines, electricity generated, city energy demand, and grid reliability interact",
        "Describe the challenge of intermittent energy sources and why grid reliability depends on supply matching demand",
        "Use evidence from a model to evaluate the strengths and limitations of wind energy"
    ],
    "vocabulary": [
        ("Wind Turbine", "A tall machine with spinning blades that converts the kinetic energy of wind into electrical energy"),
        ("Electricity", "A form of energy that flows through wires and powers our homes, schools, and devices"),
        ("Grid Reliability", "How consistently the electrical grid can deliver power to everyone who needs it — unreliable grids cause blackouts"),
        ("Renewable Energy", "Energy from sources that never run out, like wind, solar, and water — unlike fossil fuels which are limited"),
        ("Intermittent", "Not constant — wind energy is intermittent because the wind does not blow at the same speed all the time")
    ],
    "components": [
        ("Wind Speed", "How fast the wind is blowing — faster wind spins turbine blades faster and generates more electricity", True),
        ("Number of Turbines", "How many wind turbines are installed in the wind farm — more turbines can capture more wind energy", True),
        ("Electricity Generated", "The total amount of electrical power produced by all the turbines combined", False),
        ("City Energy Demand", "How much electricity the city needs to power all homes, businesses, schools, and hospitals", False),
        ("Grid Reliability", "Whether the electrical supply consistently meets the city's demand — high reliability means no blackouts", False)
    ],
    "think_about_it": "When Wind Speed increases, what happens to Electricity Generated? When the city's Energy Demand is high but Electricity Generated is low, what happens to Grid Reliability?",
    "scenarios": [
        ("Windy Day, Plenty of Turbines", "Set Wind Speed to 80% and Number of Turbines to 80% — a perfect day for wind power"),
        ("Calm Day, Plenty of Turbines", "Set Wind Speed to 15% but keep Number of Turbines at 80% — what happens when the wind dies down?"),
        ("Windy Day, Few Turbines", "Set Wind Speed to 80% but Number of Turbines to 20% — lots of wind but not enough turbines to capture it"),
        ("Building Up the Farm", "Start with Number of Turbines at 20% and gradually increase to 100% with Wind Speed at 50% — does adding more turbines solve the reliability problem?")
    ],
    "sim_scenarios": [
        ("Windy Day, Plenty of Turbines", "Wind Speed at 80%, Turbines at 80%", "What do you predict will happen to Grid Reliability when wind is strong and many turbines are running?"),
        ("Calm Day, Plenty of Turbines", "Wind Speed at 15%, Turbines at 80%", "What happens to Grid Reliability when the wind drops even though you have lots of turbines?"),
        ("Windy Day, Few Turbines", "Wind Speed at 80%, Turbines at 20%", "Can a few turbines in strong wind match the power of many turbines in weak wind?"),
        ("Building Up the Farm", "Turbines increasing from 20% to 100%, Wind Speed at 50%", "Does adding more turbines guarantee reliable power for the city?")
    ],
    "discoveries": [
        "Wind turbines convert the kinetic energy of moving air into electrical energy — faster wind produces more electricity",
        "Grid reliability depends on SUPPLY matching DEMAND — if the wind drops and generation falls below what the city needs, blackouts happen",
        "Wind energy is intermittent (not constant) — this is the biggest challenge, because cities need power 24/7 but wind does not blow 24/7",
        "Adding more turbines helps generate more electricity on windy days, but cannot solve the fundamental problem of calm days"
    ],
    "answer": "Wind power is amazing but has a big challenge: RELIABILITY! Wind turbines work by converting the kinetic energy of moving air into electricity. On a windy day with lots of turbines, they can generate more than enough power for a city. The problem is that wind is INTERMITTENT — it does not blow constantly or predictably. On calm days, turbines produce very little electricity, but the city still needs power for hospitals, schools, and homes. When electricity supply drops below demand, blackouts happen. This is why most places use wind energy combined with other sources (solar, natural gas, batteries) to keep the grid reliable. Wind cannot power a city alone — yet — but it is an important part of the energy mix!",
    "stem_title": "Design a Wind-Powered Community",
    "stem_mission": "Design a plan for a community that gets most of its electricity from wind, including a solution for what happens when the wind stops.",
    "stem_scenario": "A new eco-friendly community is being built and wants to be powered primarily by wind energy. Your engineering team must design the community's energy plan: how many turbines are needed, where they should go, and what backup plan will keep the lights on during calm days. Use your model evidence to justify every decision.",
    "stem_questions": [
        "How many turbines would your community need on a typical day vs. a very windy day?",
        "What is your backup plan for calm days when turbines produce almost no electricity?",
        "How would you store extra electricity from very windy days to use during calm days?"
    ],
    "stem_design_qs": [
        "How will you calculate the number of turbines needed based on your community's size?",
        "Where is the best location for your wind farm (hilltop, coastline, open plains)?",
        "What backup energy source will you include (solar, batteries, hydropower)?",
        "How will you convince community members that wind energy is worth the investment?"
    ],
    "career": "Wind Energy Engineers and Renewable Energy Specialists design, build, and maintain wind farms that generate clean electricity. As the world shifts to renewable energy, this field is growing rapidly. They earn $65,000–$120,000/year.",
    "images": {
        "cover": ("cover-wind-city.png", "A stunning wide shot of a large wind farm with dozens of white turbines spinning against a dramatic blue sky with a modern city skyline visible in the background, golden hour lighting, cinematic energy photography"),
        "landscape": ("landscape-wind-city.png", "A photorealistic image of diverse 4th grade students (9-10 years old) with a White girl and a Black boy leading the group, building small pinwheel wind turbines at their desks with batteries and wires in a bright modern classroom, natural window light, genuinely diverse group"),
        "modeling": ("modeling-wind-city.png", "A photorealistic image of diverse 4th grade students (9-10 years old) with a Latino boy taking the lead at the laptop, working together building a digital energy model on screen, modern classroom with renewable energy posters, balanced diversity with varied hairstyles"),
        "discussion": ("discussion-wind-city.png", "A photorealistic image of a Black male teacher leading a discussion with diverse 4th graders (9-10 years old) about wind energy and grid reliability, showing a graph of wind speed over a week on a smartboard, students with hands raised, balanced diversity"),
        "stem": ("stem-wind-city.png", "A photorealistic image of diverse 4th grade students (9-10 years old) with an Asian American boy and Latina girl in the foreground, working on a community energy plan poster with wind turbine drawings, solar panels, and battery storage diagrams, balanced diversity")
    },
    "pre_assessment": [
        "Have you ever seen a wind turbine? What do you think it does?",
        "If wind is free, why do you think we still use fossil fuels like coal and natural gas for electricity?",
        "Draw what you think happens inside a wind turbine when the wind blows.",
        "What would happen to a city that gets all its electricity from wind if the wind stopped blowing for three days?"
    ],
    "extend_components": [
        ("Battery Storage", "Large batteries that store extra electricity from windy days to use during calm days — like saving money in a bank for emergencies"),
        ("Solar Panels", "A second renewable energy source that generates electricity from sunlight — often windy days and sunny days happen at different times"),
        ("Fossil Fuel Backup", "A natural gas power plant that can be turned on quickly when renewables are not producing enough — reliable but produces carbon emissions")
    ],
    "reflections": [
        "What is the biggest advantage of wind energy? What is its biggest disadvantage?",
        "Why is it important for electricity supply to MATCH demand at all times?",
        "How could combining wind energy with solar energy make the grid more reliable?",
        "If you were a city planner, would you choose 100% wind energy or a mix of sources? Why?",
        "How did your model help you understand why switching entirely to wind energy is challenging?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a five-component model showing how wind speed and turbine count interact with electricity generation, city demand, and grid reliability."),
        ("Disciplinary Core Idea", "ESS3.A Natural Resources / PS3.A Definitions of Energy", "Energy and fuels humans use are derived from natural resources. Wind is a renewable resource that can be converted to electricity, but its intermittent nature creates challenges for reliable energy supply."),
        ("Crosscutting Concept", "Cause and Effect", "Students investigate how changes in wind speed cause predictable changes in electricity generation, and how the relationship between supply and demand determines whether the grid is reliable or fails.")
    ],
    "cast_items": [
        "Explain how wind turbines convert kinetic energy into electrical energy",
        "Use a model to describe the relationship between electricity supply and grid reliability",
        "Evaluate wind energy's strengths and limitations as a power source for cities"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A city gets all its electricity from a wind farm. On Monday the wind blows strongly, but on Tuesday it is calm. What will most likely happen to the city on Tuesday?"),
        ("Constructed Response:", "Using what you know about wind energy and grid reliability, explain why most cities use a MIX of energy sources instead of relying on wind alone. Use the words 'intermittent,' 'demand,' and 'reliability' in your answer.")
    ],
    "background_intro": "The world is racing to replace fossil fuels with clean, renewable energy sources. Wind power is one of the fastest-growing energy sources on Earth, but it comes with a unique challenge that engineers are still working to solve: the wind does not always blow.",
    "background_sections": [
        ("How Wind Turbines Work", "A wind turbine converts the kinetic energy of moving air into electrical energy through a surprisingly simple process. Wind pushes the turbine's blades, which are shaped like airplane wings to maximize lift. The spinning blades turn a shaft connected to a generator — a device that converts mechanical (spinning) energy into electrical energy using magnets and copper wire. A single large turbine can generate enough electricity for about 500 homes when the wind is blowing at full speed."),
        ("The Intermittency Problem", "The biggest challenge with wind energy is intermittency — the wind does not blow at a constant, predictable speed. Wind varies by season, time of day, weather patterns, and geography. A wind farm might produce 100% of a city's needs during a storm and only 5% during a calm day. But the city needs power ALL the time — hospitals cannot lose electricity, refrigerators must keep running, and traffic lights cannot go dark. This mismatch between variable supply and constant demand is the core engineering challenge."),
        ("Grid Reliability: Supply Must Match Demand", "The electrical grid is like a giant balancing act. Every moment of every day, the total electricity being generated must EXACTLY match the total electricity being used. If supply drops below demand, voltage drops and equipment fails — causing brownouts or blackouts. If supply exceeds demand, equipment can be damaged. Grid operators must constantly adjust generation sources to match demand, which is much harder when a major source (wind) is unpredictable."),
        ("Solutions: Batteries, Solar, and Smart Grids", "Engineers are developing several solutions to wind's intermittency. Battery storage allows excess electricity from windy days to be saved for calm days — like a rechargeable energy bank. Combining wind with solar energy helps because often when it is not windy, it is sunny (and vice versa). Smart grids use computers to automatically switch between energy sources based on availability. And some regions are building massive pumped-water storage systems where excess electricity pumps water uphill, and when power is needed, the water flows downhill through turbines to generate electricity.")
    ],
    "lever_L": "Students identify Wind Speed and Number of Turbines as external components (environmental conditions and human decisions) and Electricity Generated, City Energy Demand, and Grid Reliability as internal components.",
    "lever_E": "Students determine that Wind Speed and Number of Turbines both positively affect Electricity Generated, City Energy Demand negatively affects Grid Reliability (more demand strains the system), and Electricity Generated positively affects Grid Reliability (more supply stabilizes it).",
    "lever_V": "Students build a five-component model showing how two inputs (wind and turbines) create electricity that must compete with city demand to determine whether the grid stays reliable.",
    "lever_Ev": "Students run four scenarios to observe how wind variability creates reliability problems even with many turbines, discovering that adding turbines helps but cannot solve calm-day shortages.",
    "lever_R": "Students add battery storage or solar panels to explore how combining energy sources and storing excess electricity can stabilize the grid and reduce blackout risk.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic wind farm imagery", "say": "The wind is free. It is everywhere. It never runs out. So why can we not just use it to power every city on Earth?", "do": "Show images of wind farms. Ask: If wind is free, why does your city still burn coal and gas? What is the problem?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are going to build a model that shows the REAL challenge of wind energy — and it is not what you think.", "do": "Have students read objectives aloud. Pre-teach 'intermittent' and 'grid reliability' with simple examples.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Can wind power a whole city?", "say": "Here is the question every energy engineer is trying to answer: can wind replace all the coal, gas, and oil that power our cities?", "do": "Have students vote: do you think wind can power a city by itself? Write predictions and reasoning.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps with five components previewed", "say": "We are modeling an ENTIRE energy system today — from the wind blowing to the lights turning on in your house.", "do": "Preview all five components. Explain that this model connects nature (wind) to engineering (turbines) to society (city demand).", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Five component cards for energy system", "say": "Which of these can humans control? We cannot control the wind, but we CAN choose how many turbines to build.", "do": "Guide sorting. Wind Speed is external (nature controls it). Number of Turbines is external (humans choose). The three internals are results.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows with + and - connections", "say": "Look carefully — Energy Demand has a NEGATIVE effect on Grid Reliability. Why? Because more demand without more supply creates problems.", "do": "Help students map all four relationships. Discuss why supply must match demand and what happens when it does not.", "time": "10 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph showing grid reliability rising and falling with wind", "say": "Watch Grid Reliability when we change the wind. On a windy day, we are golden. But what happens when the wind drops?", "do": "Run all four scenarios. The calm-day scenario is the key moment — students see grid reliability crash even with many turbines.", "time": "12 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings with pros and cons chart", "say": "Wind energy is incredible — it is clean, free, and renewable. But it has one big weakness. Can anyone name it?", "do": "Class discussion: What did the model show us about wind's biggest limitation? Introduce the word 'intermittent' formally.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Community energy plan design challenge", "say": "Your challenge: design a community energy plan that uses MOSTLY wind but has a smart backup plan for calm days.", "do": "Groups design energy plans on poster paper: how many turbines, where, and what backup. Present and defend with model evidence.", "time": "12 min"}
    ],
    "sort_reasoning": "Wind Speed is external because it is determined by weather and geography — humans cannot control how fast the wind blows. Number of Turbines is external because it is a human engineering decision — we choose how many to build. Electricity Generated, City Energy Demand, and Grid Reliability are internal because they are outcomes determined by the interaction between wind conditions and engineering choices.",
    "relationships": [
        ("Wind Speed to Electricity Generated", "POSITIVE (+)", "Faster wind spins turbine blades faster, generating more electricity. Wind energy increases with the cube of wind speed — doubling wind speed actually produces eight times more energy. This is why wind farms are built in the windiest locations possible."),
        ("Number of Turbines to Electricity Generated", "POSITIVE (+)", "More turbines capture more wind energy. A wind farm with 100 turbines generates roughly five times more electricity than one with 20 turbines. Building more turbines is the most direct way to increase total generation capacity."),
        ("City Energy Demand to Grid Reliability", "NEGATIVE (-)", "Higher energy demand puts more strain on the grid. If demand increases but supply stays the same, the gap between what is needed and what is available grows, making blackouts more likely. Cities with higher demand need more generation to maintain reliability."),
        ("Electricity Generated to Grid Reliability", "POSITIVE (+)", "More electricity generation means more supply available to meet the city's demand. When generation exceeds demand, the grid is stable and reliable. The closer generation gets to matching or exceeding demand, the more reliable the grid becomes.")
    ],
    "sim_answers": [
        ("Windy Day, Plenty of Turbines", "With Wind Speed at 80% and Turbines at 80%, Electricity Generated is very high — easily exceeding City Energy Demand. Grid Reliability is high because supply comfortably exceeds demand. On days like this, wind energy works beautifully and the city has more than enough clean power."),
        ("Calm Day, Plenty of Turbines", "With Wind Speed at 15% and Turbines at 80%, Electricity Generated drops dramatically despite having many turbines. With generation far below City Energy Demand, Grid Reliability plummets. This is the core problem with wind energy — even 100 turbines produce almost nothing on a calm day, but the city still needs power.")
    ],
    "reflection_exemplars": [
        ("What is wind energy's biggest disadvantage?", "Wind energy's biggest disadvantage is that it is intermittent — the wind does not blow constantly or predictably. Our model showed that even with many turbines, a calm day produces almost no electricity. But the city needs power 24 hours a day, 7 days a week — hospitals, schools, homes, and traffic lights cannot simply shut off when the wind stops. This means wind energy alone cannot reliably power a city. You need either backup energy sources or massive battery storage to fill the gaps during calm periods."),
        ("Would you choose 100% wind or a mix?", "I would choose a MIX of energy sources based on what our model showed. Wind is amazing when it is blowing — it is free, clean, and renewable. But its intermittency makes it unreliable as the ONLY source. Adding solar panels helps because often when it is not windy, it is sunny. Adding battery storage helps save windy-day excess for calm days. Having a small natural gas backup ensures the grid never fails completely. The goal is to make wind the PRIMARY source while having reliable backups for when nature does not cooperate.")
    ],
    "stem_intro": "Present the challenge: A new eco-community wants to be powered primarily by wind. Your team must design the energy plan — how many turbines, where to put them, and what happens during calm days. Use your model evidence to justify every decision and present your plan to the class as if presenting to the community's planning board!",
    "stem_concepts": [
        ("Energy Supply Must Match Demand", "A city cannot function if electricity supply drops below demand. Your community plan must account for the WORST case (calm day) not just the BEST case (windy day). Plan for the calm days."),
        ("Intermittency Requires Backup", "Wind energy alone cannot guarantee reliable power because the wind is unpredictable. Your plan should include at least one backup strategy — batteries, solar, or another source that can fill the gap on calm days."),
        ("Location Matters", "Wind farms produce more energy in consistently windy locations like coastlines, mountain passes, and open plains. Your community plan should consider where to place turbines for maximum wind exposure.")
    ],
    "stem_eval": [
        ("Expert (4)", "Community plan addresses generation capacity, backup strategy, turbine placement, and uses model evidence to justify all decisions, including a solution for calm days"),
        ("Proficient (3)", "Plan includes turbines and a backup strategy, student can explain why wind alone is not reliable"),
        ("Developing (2)", "Plan includes turbines but no clear backup strategy, student struggles to explain intermittency"),
        ("Beginning (1)", "Plan is incomplete or student cannot explain why wind energy alone creates reliability problems")
    ],
    "support": [
        "Provide a simple graph showing wind speed variation over a week so students can see the intermittency visually",
        "Use the analogy of a piggy bank: on windy days you save extra electricity, on calm days you spend your savings. If you run out of savings, the lights go out",
        "Sentence frames: 'When Wind Speed drops, Electricity Generated __ which causes Grid Reliability to __ because __.'"
    ],
    "extensions": [
        "Research the largest wind farm in the world — how many turbines does it have and how much electricity does it generate?",
        "Design a combination energy plan using wind, solar, and batteries — when would each source be most important throughout the day?",
        "Investigate pumped hydro storage — how does pumping water uphill on windy days and releasing it through turbines on calm days solve the intermittency problem?"
    ],
    "cross_curr": [
        ("Math", "If one turbine powers 500 homes, calculate how many turbines a city of 50,000 homes would need on a day when turbines run at 100% vs. a day when they run at 25%"),
        ("ELA", "Write a persuasive essay arguing whether your city should invest in a wind farm, using evidence from your model about both the benefits and limitations"),
        ("Social Studies", "Research which states in the US generate the most wind energy and create a map showing the windiest regions — why are wind farms concentrated in certain areas?")
    ],
    "misconceptions": [
        ("Wind turbines work all the time as long as they are built", "Wind turbines only generate electricity when the wind is blowing above a minimum speed (usually about 7-9 mph). On calm days, they produce almost nothing. Even in the windiest locations, turbines typically operate at full capacity only about 25-45% of the time. The rest of the time, they are either idle or running at reduced output.", "Show a graph of actual wind farm output over a month — students will see the dramatic ups and downs that make wind energy intermittent."),
        ("We just need to build more turbines to solve the energy problem", "Adding more turbines increases capacity on WINDY days but does nothing to help on CALM days. If the wind is not blowing, it does not matter if you have 10 turbines or 10,000 — they all produce zero electricity. The solution is not just more turbines but STORAGE (batteries) and DIVERSITY (multiple energy sources). Our model showed that even at 100% turbines, a calm day crashes grid reliability.", "Run the model with turbines at 100% but wind at 10% — students see that even maximum turbines cannot overcome zero wind."),
        ("Wind energy is too unreliable to use", "While wind alone cannot power a city reliably, it is an essential part of the energy mix. Wind already provides about 10% of US electricity and over 50% in some countries like Denmark. The key is combining wind with solar, batteries, and other sources. Wind's variability is a challenge, not a dealbreaker — smart engineering solutions are making wind energy more reliable every year.", "Show data from Denmark where wind provides over 50% of electricity — ask: if wind is too unreliable, how does Denmark do it?")
    ]
}

L06 = {
    "id": "G04L2-L06",
    "title": "Building for the Big One: Earthquake Engineering Lab",
    "subtitle": "How Engineers Design Buildings That Bend Instead of Break",
    "ngss": "4-ESS3-2, 4-ETS1-2",
    "ngss_desc": "Generate and compare multiple solutions to reduce the impacts of natural Earth processes on humans. Generate and compare multiple solutions to a problem based on how well they meet the criteria and constraints of the design problem.",
    "big_question": "Why do some buildings collapse during earthquakes while others right next to them survive with barely a crack?",
    "objectives": [
        "Explain how earthquake magnitude determines the shaking force experienced by buildings",
        "Model how earthquake magnitude, building flexibility, shaking force, structural damage, and occupant safety interact",
        "Describe why flexible buildings survive earthquakes better than rigid buildings",
        "Use evidence from a model to design buildings that reduce earthquake damage and protect occupants"
    ],
    "vocabulary": [
        ("Earthquake Magnitude", "A measurement of how much energy an earthquake releases — higher magnitude means stronger shaking"),
        ("Flexibility", "The ability of a structure to bend, sway, or absorb movement without breaking — like a tree bending in the wind"),
        ("Shaking Force", "The actual force that gets transferred from the ground into a building during an earthquake"),
        ("Structural Damage", "Cracks, breaks, and collapses in a building caused by the shaking force exceeding the building's strength"),
        ("Engineering Design", "The process of creating solutions to problems using science, math, and creativity — earthquake engineers design safer buildings")
    ],
    "components": [
        ("Earthquake Magnitude", "The strength of the earthquake as measured on the Richter scale — stronger earthquakes release more energy and shake the ground harder", True),
        ("Building Flexibility", "How well the building can absorb and distribute shaking forces by bending, swaying, or flexing without breaking apart", True),
        ("Shaking Force", "The actual force transmitted from the moving ground into the building's structure — stronger earthquakes create stronger shaking forces", False),
        ("Structural Damage", "The amount of physical damage to the building — cracks in walls, broken windows, collapsed floors, and foundation failures", False),
        ("Occupant Safety", "How safe the people inside the building are during and after the earthquake — depends on whether the structure protects them from falling debris", False)
    ],
    "think_about_it": "When Earthquake Magnitude increases, what happens to Shaking Force? How does Building Flexibility affect Structural Damage? How does Structural Damage affect Occupant Safety?",
    "scenarios": [
        ("Small Earthquake, Rigid Building", "Set Earthquake Magnitude to 30% and Building Flexibility to 20% — a small quake hitting a stiff, rigid building"),
        ("Big Earthquake, Rigid Building", "Set Earthquake Magnitude to 90% and Building Flexibility to 20% — a major quake hitting a stiff building"),
        ("Big Earthquake, Flexible Building", "Set Earthquake Magnitude to 90% and Building Flexibility to 80% — the same major quake but hitting a flexible building"),
        ("Comparing Designs", "Run the same earthquake (70%) against buildings with 20%, 50%, and 80% flexibility")
    ],
    "sim_scenarios": [
        ("Small Earthquake, Rigid Building", "Earthquake Magnitude at 30%, Building Flexibility at 20%", "What do you predict will happen to Structural Damage when a small earthquake hits a rigid building?"),
        ("Big Earthquake, Rigid Building", "Earthquake Magnitude at 90%, Building Flexibility at 20%", "What do you predict will happen to Occupant Safety when a major earthquake hits a rigid building?"),
        ("Big Earthquake, Flexible Building", "Earthquake Magnitude at 90%, Building Flexibility at 80%", "What do you predict will happen to Structural Damage when the SAME big earthquake hits a flexible building?"),
        ("Comparing Designs", "Same earthquake (70%) vs. 20%, 50%, 80% flexibility", "How much does each increase in flexibility reduce damage?")
    ],
    "discoveries": [
        "Stronger earthquakes create stronger shaking forces that cause more damage to buildings and endanger more people",
        "Flexible buildings survive earthquakes much better than rigid ones because they absorb and distribute shaking energy instead of fighting it",
        "Building flexibility REDUCES structural damage (negative relationship) because the building moves WITH the earthquake instead of against it",
        "Occupant safety depends directly on structural damage — the less damage, the safer the people inside, which is why engineering design saves lives"
    ],
    "answer": "The secret to earthquake survival is FLEXIBILITY! When the ground shakes, rigid buildings try to resist the motion — but the forces are too strong, and the building cracks, crumbles, and collapses. Flexible buildings are designed to MOVE WITH the earthquake. They sway, bend, and absorb the shaking energy without breaking. Think of it like a tree in a storm: a stiff dead tree snaps, but a living tree bends and bounces back. Modern earthquake engineers design buildings with flexible materials, shock absorbers, and even giant pendulums inside that swing in the opposite direction of the shaking to keep the building stable. The difference between a rigid building and a flexible one can be the difference between life and death.",
    "stem_title": "Earthquake-Proof Tower Challenge",
    "stem_mission": "Design and build the tallest tower that can survive a simulated earthquake (shaking table) without collapsing.",
    "stem_scenario": "A city in an earthquake zone needs a new hospital that can survive a major earthquake and keep patients safe. Your engineering team must design and build a tower model that is as tall as possible while surviving a simulated earthquake on a shaking table. Use your model evidence to decide what materials and shapes make the most earthquake-resistant structure.",
    "stem_questions": [
        "What materials make your tower more flexible and better able to survive shaking?",
        "Does the shape of your tower (wide base, narrow top, cross-bracing) affect how well it survives?",
        "How can you test your tower's earthquake resistance before the final test?"
    ],
    "stem_design_qs": [
        "What building materials will you use (straws, pipe cleaners, popsicle sticks, marshmallows, tape)?",
        "How will you make your tower flexible enough to sway without collapsing?",
        "What is the tallest you can build while still surviving the shake test?",
        "How will you simulate an earthquake to test your design (shaking a cookie sheet, tapping a table)?"
    ],
    "career": "Structural Engineers and Seismic Engineers design buildings, bridges, and infrastructure that can withstand earthquakes, hurricanes, and other natural disasters. Their work directly saves thousands of lives. They earn $70,000–$130,000/year.",
    "images": {
        "cover": ("cover-earthquake-engineering.png", "A dramatic split image showing two buildings during an earthquake — one crumbling and collapsing while the other flexes and stays standing, with visible seismic waves in the ground beneath, cinematic disaster photography"),
        "landscape": ("landscape-earthquake-engineering.png", "A photorealistic image of diverse 4th grade students (9-10 years old) with a Black girl and a White boy leading the group, building tower structures from straws and marshmallows at their desks in a bright modern classroom, natural window light, genuinely diverse group"),
        "modeling": ("modeling-earthquake-engineering.png", "A photorealistic image of diverse 4th grade students (9-10 years old) with an Asian American girl taking the lead at the laptop, working together building a digital earthquake simulation model on screen, modern classroom with earthquake safety posters, balanced diversity"),
        "discussion": ("discussion-earthquake-engineering.png", "A photorealistic image of a Latina female teacher leading a discussion with diverse 4th graders (9-10 years old) about earthquake engineering, showing before and after earthquake photos on a smartboard, students with hands raised, balanced diversity"),
        "stem": ("stem-earthquake-engineering.png", "A photorealistic image of diverse 4th grade students (9-10 years old) with a Latino boy and a Black girl in the foreground, testing their tower designs on a shaking table (cookie sheet being shaken), towers of various heights and materials, excited and engaged, balanced diversity")
    },
    "pre_assessment": [
        "Why do you think some buildings fall down during earthquakes while others stay standing?",
        "Would you rather be in a building made of rigid concrete or one that can sway back and forth during an earthquake? Why?",
        "Draw what you think happens to a building when the ground underneath it starts shaking.",
        "What do you think engineers do differently when they build buildings in earthquake zones?"
    ],
    "extend_components": [
        ("Foundation Type", "How the building connects to the ground — some foundations are rigid while others use base isolation that allows the building to slide independently of the ground"),
        ("Building Height", "How tall the building is — taller buildings experience more swaying at the top during earthquakes"),
        ("Material Strength", "How strong the building materials are — reinforced concrete and steel are stronger than brick and unreinforced masonry")
    ],
    "reflections": [
        "Why is a flexible building safer than a rigid one during an earthquake?",
        "How is a building swaying in an earthquake similar to a tree bending in a strong wind?",
        "If you were designing a hospital in an earthquake zone, what would be your top three design priorities?",
        "Why can we not prevent earthquakes, so we have to design buildings that survive them?",
        "How did your model help you understand what makes the difference between buildings that survive and buildings that collapse?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models / Designing Solutions", "Students develop a five-component model of earthquake impact on buildings and use model evidence to design structures that minimize damage and maximize occupant safety."),
        ("Disciplinary Core Idea", "ESS3.B Natural Hazards / ETS1.B Developing Possible Solutions", "Natural hazards like earthquakes cannot be prevented, but their impacts can be reduced through engineering design. Testing and comparing multiple solutions helps identify the most effective approach."),
        ("Crosscutting Concept", "Cause and Effect", "Students investigate the causal chain from earthquake magnitude to shaking force to structural damage to occupant safety, and how engineering interventions (flexibility) can interrupt this chain.")
    ],
    "cast_items": [
        "Explain how earthquake magnitude relates to building damage and occupant safety",
        "Use a model to describe how building flexibility reduces structural damage",
        "Design and compare multiple solutions for earthquake-resistant buildings"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Two buildings are next to each other during a magnitude 7.0 earthquake. Building A is made of rigid unreinforced brick. Building B has a flexible steel frame with shock absorbers. Which building is most likely to survive? Why?"),
        ("Constructed Response:", "Using what you know about earthquakes and engineering, explain why a building that can SWAY during an earthquake is actually SAFER than one that stays perfectly still. Use the words 'flexibility,' 'shaking force,' and 'structural damage' in your answer.")
    ],
    "background_intro": "Earthquakes are one of nature's most destructive forces, but they do not have to be deadly. The difference between a disaster with thousands of casualties and one where everyone walks away is often the ENGINEERING of the buildings. Understanding how buildings interact with earthquake forces is the key to saving lives.",
    "background_sections": [
        ("How Earthquakes Work", "Earthquakes happen when tectonic plates suddenly slip past each other along a fault line, releasing enormous amounts of stored energy as seismic waves. These waves travel through the ground and shake everything on the surface. Earthquake magnitude is measured on the Richter scale — each whole number increase represents about 32 times more energy. A magnitude 7 earthquake releases about 32 times more energy than a magnitude 6, and about 1,000 times more than a magnitude 5."),
        ("Rigid vs. Flexible: Why Buildings Fail", "When the ground shakes during an earthquake, the bottom of a building moves with the ground but the top tries to stay still (due to inertia). This creates enormous stress in the structure. Rigid buildings — made of unreinforced brick, concrete blocks, or adobe — cannot flex to absorb this stress. Like a dry twig, they snap. The connections between walls and floors fail, and the building pancakes. Flexible buildings — with steel frames, reinforced concrete, and engineered connections — bend and sway with the motion, distributing the stress throughout the structure instead of concentrating it at weak points."),
        ("Engineering Solutions That Save Lives", "Modern earthquake engineering uses several strategies. Base isolation places the building on rubber and steel pads that let the foundation slide horizontally while the building stays relatively still — like a book sliding on a table. Tuned mass dampers are heavy pendulums near the top of skyscrapers that swing in the opposite direction of the earthquake, counteracting the sway. Cross-bracing uses diagonal steel beams that resist lateral forces. Energy dissipation devices are essentially shock absorbers built into the building that convert shaking energy into heat."),
        ("The Cost of Not Building Better", "The difference between earthquake engineering and no engineering is measured in lives. The 2010 Haiti earthquake (magnitude 7.0) killed over 200,000 people because most buildings were unreinforced concrete. The 2011 Japan earthquake (magnitude 9.0 — over 900 times stronger) killed about 20,000 people, mostly from the tsunami, because Japanese buildings are engineered for earthquakes. Japan experienced a much stronger earthquake but far fewer building collapses because they invested in engineering.")
    ],
    "lever_L": "Students identify Earthquake Magnitude and Building Flexibility as external components (one natural, one engineered) and Shaking Force, Structural Damage, and Occupant Safety as internal components that result from the interaction.",
    "lever_E": "Students determine that Earthquake Magnitude positively affects Shaking Force, Building Flexibility negatively affects Structural Damage (flexible buildings resist damage), Shaking Force positively affects Structural Damage, Structural Damage negatively affects Occupant Safety, and Building Flexibility positively affects Occupant Safety.",
    "lever_V": "Students build a five-component model showing how earthquake force travels through a building and how engineering flexibility interrupts the damage chain to protect occupants.",
    "lever_Ev": "Students run four scenarios comparing rigid vs. flexible buildings in small and large earthquakes, discovering that flexibility makes the biggest difference in large earthquakes.",
    "lever_R": "Students add foundation type or building height to explore base isolation and why taller buildings need special engineering to handle amplified swaying at the top.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with earthquake damage vs. earthquake-proof building comparison", "say": "Look at these two buildings. Same earthquake. Same street. One collapsed, the other is fine. What is the difference?", "do": "Show before/after earthquake photos of collapsed vs. surviving buildings. Ask: What do you think the surviving building had that the other did not?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today you are going to become earthquake engineers. You will figure out WHY some buildings survive and design one that can handle the big one.", "do": "Have students read objectives aloud. Pre-teach 'flexibility' vs. 'rigidity' by bending a pipe cleaner vs. trying to bend a pencil.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why do some buildings collapse while neighbors survive?", "say": "If two buildings are right next to each other and feel the SAME earthquake, why would one collapse and the other survive?", "do": "Have students turn and talk: What design choices could make one building survive and another fail?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps with five components previewed", "say": "Our model has one thing from NATURE and one thing from ENGINEERING. The question is: can engineering beat nature?", "do": "Preview components. Explain that this model is special because one external is a natural hazard and the other is a human solution.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Five component cards for earthquake system", "say": "We cannot control earthquakes — but we CAN control how we build. That is the key to this whole model.", "do": "Guide sorting. Earthquake Magnitude is external (nature). Building Flexibility is external (engineering choice). Three internals are results.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows with + and - connections", "say": "Building Flexibility has a NEGATIVE relationship with Structural Damage. What does that mean? More flexibility means LESS damage!", "do": "Help students draw all five relationships. Emphasize the two negative arrows — these are where engineering saves lives.", "time": "10 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph comparing rigid vs. flexible building outcomes", "say": "Now let us test it. Same earthquake, two different buildings. Watch what happens to Structural Damage and Occupant Safety.", "do": "Run the rigid vs. flexible comparison. Students record the dramatic difference in damage and safety outcomes.", "time": "12 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings with engineering solution examples", "say": "Engineers cannot stop earthquakes, but they CAN stop buildings from killing people. The answer is designing buildings that MOVE instead of FIGHT.", "do": "Show examples of base isolation and tuned mass dampers. Connect each engineering solution back to the model's flexibility component.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Earthquake-proof tower design challenge", "say": "Your mission: build the tallest tower that survives the earthquake test. But here is the twist — it also has to be tall enough to be useful!", "do": "Distribute materials (straws, pipe cleaners, marshmallows, tape, clay). Groups build, test on shaking tables, iterate, and retest.", "time": "12 min"}
    ],
    "sort_reasoning": "Earthquake Magnitude is external because it is a natural force determined by tectonic activity — humans cannot control it. Building Flexibility is external because it is an engineering DESIGN CHOICE made by architects and engineers before the earthquake happens. Shaking Force, Structural Damage, and Occupant Safety are internal because they are outcomes that emerge from the interaction between the earthquake and the building design.",
    "relationships": [
        ("Earthquake Magnitude to Shaking Force", "POSITIVE (+)", "Stronger earthquakes release more energy, creating stronger seismic waves that produce more violent shaking forces on buildings. A magnitude 7 earthquake produces about 32 times more energy than a magnitude 6, creating proportionally more shaking force."),
        ("Building Flexibility to Structural Damage", "NEGATIVE (-)", "More flexible buildings experience LESS structural damage because they absorb and distribute shaking energy by swaying, bending, and flexing instead of cracking and collapsing. Flexibility allows the building to move WITH the earthquake rather than fighting against it."),
        ("Shaking Force to Structural Damage", "POSITIVE (+)", "Stronger shaking forces cause more structural damage — more cracks, more broken connections, more collapsed sections. When shaking force exceeds what the structure can handle, failure is catastrophic and rapid."),
        ("Structural Damage to Occupant Safety", "NEGATIVE (-)", "More structural damage means LESS safety for the people inside. When walls crack, floors collapse, and debris falls, occupants are at extreme risk. The goal of earthquake engineering is to keep structural damage low enough that the building protects everyone inside."),
        ("Building Flexibility to Occupant Safety", "POSITIVE (+)", "More flexible buildings directly improve occupant safety because they maintain structural integrity during shaking. A building that sways but does not break keeps its occupants safe even in strong earthquakes.")
    ],
    "sim_answers": [
        ("Big Earthquake, Rigid Building", "With Earthquake Magnitude at 90% and Building Flexibility at 20%, Shaking Force is extremely high and the rigid building cannot absorb it. Structural Damage is catastrophic — walls crack, floors collapse, the building may pancake. Occupant Safety is extremely low. This scenario represents the devastating building failures seen in earthquakes where construction was not engineered for seismic forces."),
        ("Big Earthquake, Flexible Building", "With the SAME Earthquake Magnitude at 90% but Building Flexibility at 80%, the shaking force is identical but the outcome is dramatically different. The flexible building absorbs and distributes the energy through its engineered frame. Structural Damage is significantly reduced — some cosmetic cracking but no structural failure. Occupant Safety remains high. This is the same earthquake that destroyed the rigid building, but engineering made the difference between life and death.")
    ],
    "reflection_exemplars": [
        ("Why is flexibility better than rigidity during an earthquake?", "A rigid building tries to resist the earthquake's motion by staying perfectly still. But the shaking force is too strong — the rigid materials cannot handle the stress and they crack, break, and collapse. A flexible building does the opposite — it MOVES WITH the earthquake, bending and swaying to absorb the energy. Think of it like a tree in a hurricane: a dead, rigid tree snaps, but a living tree with flexible branches bends all the way to the ground and bounces back. The flexible building is not fighting the earthquake — it is going with the flow and surviving."),
        ("If you were designing a hospital in an earthquake zone, what would you prioritize?", "My top three priorities would be: 1) FLEXIBILITY — the building must have a flexible steel frame with seismic joints that allow controlled swaying, because our model showed that flexibility is the biggest factor in reducing damage. 2) BASE ISOLATION — I would put the building on rubber isolation pads so the ground can shake without transmitting full force to the building. 3) BACKUP SYSTEMS — hospitals need power, water, and medical equipment that keep working even during shaking, so I would secure all heavy equipment and have backup generators. A hospital that collapses during an earthquake turns from a place of healing into a disaster.")
    ],
    "stem_intro": "Present the challenge: A city in an earthquake zone needs a new hospital that can survive a major earthquake. Your team must design and build a tower model that is as TALL as possible while surviving a simulated earthquake on a shaking table. You have limited materials and must make engineering decisions about flexibility, shape, and reinforcement. Test your design, observe what fails, improve it, and test again!",
    "stem_concepts": [
        ("Flexibility Over Rigidity", "Your tower should be able to sway and bend without breaking. Stiff, rigid towers resist shaking — and when the force exceeds their strength, they collapse suddenly. Flexible towers absorb shaking energy gradually."),
        ("Cross-Bracing and Triangles", "Triangles are the strongest shape in engineering. Adding diagonal cross-bracing (X-patterns) to your tower adds strength while maintaining flexibility. Real earthquake-resistant buildings use cross-bracing extensively."),
        ("Base Width and Stability", "A wider base distributes the shaking force over a larger area, making the tower more stable. Real earthquake-resistant buildings often have wide foundations that taper as they go higher.")
    ],
    "stem_eval": [
        ("Expert (4)", "Tower is tall, survives the shake test, student explains design choices using flexibility and shaking force concepts, and iterates based on test results"),
        ("Proficient (3)", "Tower survives moderate shaking, student can explain why flexibility helps using model evidence"),
        ("Developing (2)", "Tower is built but fails the shake test, student understands that flexibility matters but design does not demonstrate it"),
        ("Beginning (1)", "Tower is incomplete or collapses immediately, student cannot connect design choices to earthquake science")
    ],
    "support": [
        "Provide examples of cross-bracing, wide bases, and flexible connections before students start building",
        "Let students bend a pipe cleaner (flexible) and try to bend a pencil (rigid) — ask which would you rather be inside during an earthquake?",
        "Sentence frames: 'When Earthquake Magnitude is high and Building Flexibility is low, Structural Damage __ because __. If we increase Flexibility, damage __ because __.'"
    ],
    "extensions": [
        "Research Taipei 101's tuned mass damper — a 730-ton golden pendulum that swings to counteract earthquake and wind forces. How does it work?",
        "Compare the building codes of earthquake-prone countries (Japan, Chile) to countries that rarely experience earthquakes — what differences do you notice?",
        "Design a base isolation system for your tower using rubber bands or sponges and test whether it reduces damage compared to a fixed foundation"
    ],
    "cross_curr": [
        ("Math", "Measure the height of each team's tower, record whether it survived the shake test, and create a scatter plot of height vs. survival — is there a pattern?"),
        ("ELA", "Write a newspaper article reporting on an earthquake in your model city, describing which buildings survived and why, using engineering vocabulary"),
        ("Social Studies", "Research how ancient civilizations built earthquake-resistant structures — the Incas used trapezoidal doorways and fitted stone without mortar that could shift and resettle during earthquakes")
    ],
    "misconceptions": [
        ("The strongest building is the safest during an earthquake", "STRENGTH alone does not make a building earthquake-safe — FLEXIBILITY does. A building can be extremely strong but also extremely rigid, meaning it resists shaking forces until those forces exceed its strength, at which point it fails catastrophically. A flexible building may appear weaker but absorbs shaking energy by moving, preventing the catastrophic failure that kills people.", "Hold a rigid cracker and a flexible piece of cooked spaghetti. Shake both. The cracker snaps; the spaghetti bends. Which would you rather be inside?"),
        ("Earthquakes directly kill people", "Earthquakes themselves almost never directly kill people — BUILDINGS do. Falling debris, collapsing walls, and pancaking floors are responsible for the vast majority of earthquake deaths. In an open field during an earthquake, you would feel the shaking but be completely safe. This is why earthquake engineering is so important — better buildings mean fewer deaths, even in strong earthquakes.", "Compare the Haiti 2010 earthquake (magnitude 7.0, 200,000+ deaths from building collapse) to the Japan 2011 earthquake (magnitude 9.0, about 20,000 deaths mostly from tsunami, NOT building collapse). Better buildings saved lives despite a much stronger earthquake."),
        ("We should just avoid building in earthquake zones", "About 1.5 billion people live in earthquake zones worldwide. Major cities like Tokyo, Los Angeles, San Francisco, Mexico City, and Istanbul are all in high-risk zones. We cannot simply abandon these areas — instead, we use engineering to make buildings safe. Japan proves this is possible: they experience thousands of earthquakes per year but their buildings are so well-engineered that most earthquakes cause no damage at all.", "Show a map of earthquake zones overlaid with major world cities. Avoiding these areas would mean relocating billions of people. Engineering is the practical solution.")
    ]
}

L07 = {
    "id": "G04L2-L07",
    "title": "Chain Reaction: When Energy Moves Object to Object",
    "subtitle": "Why Each Collision Loses a Little Energy Along the Way",
    "ngss": "4-PS3-3, 4-PS3-4",
    "ngss_desc": "Ask questions and predict outcomes about the changes in energy that occur when objects collide. Apply scientific ideas to design, test, and refine a device that converts energy from one form to another.",
    "big_question": "If you set up a line of dominoes and push the first one, why does the last domino always fall slower than the first one was pushed?",
    "objectives": [
        "Explain how kinetic energy transfers from one object to the next during collisions",
        "Model how initial push force, object mass, kinetic energy transfer, energy lost to sound, and final object speed interact",
        "Describe how energy is lost to sound and heat at each collision, reducing the energy available for the next object",
        "Use evidence from a model to explain why chain reactions lose energy over successive collisions"
    ],
    "vocabulary": [
        ("Collision", "When two objects hit each other, transferring energy from one to the other"),
        ("Kinetic Energy Transfer", "When a moving object hits a stationary object and passes some of its motion energy to it"),
        ("Energy Loss", "Energy that changes from motion into sound, heat, or vibration during a collision — it does not disappear but is no longer useful for movement"),
        ("Mass", "How much matter (stuff) is in an object — heavier objects have more mass and are harder to get moving"),
        ("Chain Reaction", "A series of events where each event triggers the next one — like dominoes falling or billiard balls hitting each other")
    ],
    "components": [
        ("Initial Push Force", "How hard the first object in the chain is pushed — a stronger push gives the first object more kinetic energy to transfer", True),
        ("Object Mass", "How heavy the objects in the chain are — heavier objects are harder to get moving and require more energy to push", True),
        ("Kinetic Energy Transfer", "The amount of motion energy that passes from one object to the next during each collision", False),
        ("Energy Lost to Sound", "The kinetic energy that transforms into sound energy during each collision — you can hear each impact", False),
        ("Final Object Speed", "How fast the last object in the chain moves after receiving energy through all the previous collisions", False)
    ],
    "think_about_it": "When Initial Push Force increases, what happens to Kinetic Energy Transfer? At each collision, some energy becomes sound. How does this affect the Final Object Speed?",
    "scenarios": [
        ("Strong Push, Light Objects", "Set Initial Push Force to 80% and Object Mass to 20% — hard push on lightweight objects"),
        ("Weak Push, Heavy Objects", "Set Initial Push Force to 20% and Object Mass to 80% — gentle push on heavy objects"),
        ("Strong Push, Heavy Objects", "Set Initial Push Force to 80% and Object Mass to 80% — hard push on heavy objects"),
        ("Comparing Mass Effect", "Keep Initial Push Force at 60% and compare Object Mass at 20% vs. 50% vs. 80%")
    ],
    "sim_scenarios": [
        ("Strong Push, Light Objects", "Initial Push Force at 80%, Object Mass at 20%", "What do you predict will happen to Final Object Speed when you push light objects hard?"),
        ("Weak Push, Heavy Objects", "Initial Push Force at 20%, Object Mass at 80%", "What do you predict will happen when you gently push heavy objects? Will the chain even reach the end?"),
        ("Strong Push, Heavy Objects", "Initial Push Force at 80%, Object Mass at 80%", "Can a strong push overcome the challenge of moving heavy objects through a chain?"),
        ("Comparing Mass Effect", "Push Force at 60%, Mass at 20% vs. 50% vs. 80%", "How does changing mass affect how much energy reaches the final object?")
    ],
    "discoveries": [
        "Energy transfers from object to object during collisions, but some energy is LOST to sound and heat at each collision point",
        "Heavier objects require more energy to get moving, so less kinetic energy transfers through a chain of heavy objects compared to light ones",
        "A stronger initial push gives the chain more total energy to work with, so more energy survives the losses at each collision",
        "Every chain reaction gets weaker over time because energy is lost at every collision — this is why the last domino falls with less force than the first one was pushed"
    ],
    "answer": "Every collision in a chain reaction is a tiny energy leak! When the first domino hits the second, MOST of the kinetic energy transfers to the second domino. But not ALL of it — some energy becomes SOUND (the clicking noise you hear) and some becomes HEAT (tiny amounts of friction and deformation). The second domino has slightly less energy than the first one received. When the second hits the third, the same thing happens — more energy leaks as sound and heat. By the time energy reaches the last domino in a long chain, it has been reduced by all those tiny losses added together. The last domino falls with less energy than the first was given. It is like pouring water through a series of cups with tiny holes — each cup leaks a little, and there is less water at the end!",
    "stem_title": "Build the Longest Energy Chain",
    "stem_mission": "Design a chain reaction where energy transfers through as many objects as possible while still having enough energy to complete the final action.",
    "stem_scenario": "A science museum wants a Rube Goldberg machine exhibit that shows visitors how energy transfers from object to object. Your engineering team must build the longest chain reaction possible where a push at the start causes a final action at the end — like ringing a bell, knocking over a cup, or launching a small ball. The chain must have at least five collisions, and you must explain where energy is lost at each step.",
    "stem_questions": [
        "How many collisions can your chain reaction have before the energy runs out?",
        "What objects transfer energy most efficiently — heavy or light ones?",
        "Where can you hear or see energy being lost at each collision in your chain?"
    ],
    "stem_design_qs": [
        "What objects will you use in your chain (marbles, dominoes, toy cars, balls, blocks)?",
        "How will you arrange them so each collision triggers the next?",
        "What will your final action be — what does the last object do to prove energy made it through?",
        "How will you minimize energy loss at each collision to make the chain as long as possible?"
    ],
    "career": "Mechanical Engineers and Physicists study how energy transfers between objects to design everything from car safety systems (crumple zones absorb collision energy) to sports equipment (bats and clubs transfer energy efficiently to balls). They earn $70,000–$120,000/year.",
    "images": {
        "cover": ("cover-chain-reaction.png", "A dramatic high-speed photography image of a Newton's cradle in action, one ball swinging out while the others remain still, showing the moment of energy transfer with motion blur, dark background, cinematic physics photography"),
        "landscape": ("landscape-chain-reaction.png", "A photorealistic image of diverse 4th grade students (9-10 years old) with a Latino boy and a White girl leading the group, setting up rows of dominoes and marble chains on their desks in a bright modern classroom, natural window light, genuinely diverse group"),
        "modeling": ("modeling-chain-reaction.png", "A photorealistic image of diverse 4th grade students (9-10 years old) with a Black girl taking the lead at the laptop, working together building a digital collision model on screen, modern classroom with energy transfer diagrams on the wall, balanced diversity"),
        "discussion": ("discussion-chain-reaction.png", "A photorealistic image of a White male teacher leading a discussion with diverse 4th graders (9-10 years old) about energy transfer during collisions, using a Newton's cradle on the desk as a visual aid, students watching intently, balanced diversity"),
        "stem": ("stem-chain-reaction.png", "A photorealistic image of diverse 4th grade students (9-10 years old) with an Asian American boy and a Black boy working together in the foreground, building a Rube Goldberg chain reaction machine with marbles, ramps, dominoes, and toy cars, excited and collaborative, balanced diversity")
    },
    "pre_assessment": [
        "When you knock over a line of dominoes, what do you think makes each domino fall?",
        "If you roll a marble into a line of marbles, why does the last marble shoot out the other end?",
        "Draw what you think happens to the ENERGY when a moving ball hits a stationary ball.",
        "Why do you think you can HEAR collisions? Where does that sound come from?"
    ],
    "extend_components": [
        ("Number of Objects in Chain", "How many objects the energy must pass through — more objects means more collisions and more opportunities for energy loss"),
        ("Object Material", "What the objects are made of — rubber balls bounce and transfer energy differently than steel balls or wooden blocks"),
        ("Collision Angle", "Whether the objects hit each other straight on or at an angle — straight-on collisions transfer energy more efficiently")
    ],
    "reflections": [
        "Why does each collision in a chain reaction have slightly less energy than the one before it?",
        "If you can hear a collision, what does that tell you about where some energy went?",
        "How is a Newton's cradle different from a line of dominoes in terms of energy transfer?",
        "If you wanted to send energy through the longest possible chain, would you use heavy or light objects? Why?",
        "How did your model help you understand why chain reactions eventually run out of energy?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models / Asking Questions", "Students develop a five-component model of energy transfer through collisions and ask questions about how push force and mass affect the energy available at the end of a chain."),
        ("Disciplinary Core Idea", "PS3.C Relationship Between Energy and Forces / PS3.D Energy in Chemical Processes and Everyday Life", "When objects collide, energy is transferred. The transfer is not 100% efficient — some energy becomes sound, heat, and vibration, reducing the energy available for movement."),
        ("Crosscutting Concept", "Energy and Matter", "Students trace energy flow through a chain of collisions, identifying where energy enters the system, how it transfers between objects, and where it exits as sound and heat.")
    ],
    "cast_items": [
        "Explain how kinetic energy transfers from one object to another during collisions",
        "Use a model to describe how energy is lost to sound and heat at each collision",
        "Apply energy transfer concepts to design a chain reaction that maximizes energy reaching the final object"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student pushes a marble into a line of 10 identical marbles. The last marble rolls out the other end but moves slower than the first marble was pushed. Which best explains why?"),
        ("Constructed Response:", "Using what you know about energy transfer and collisions, explain why a Rube Goldberg machine with 20 steps needs a stronger starting push than one with 5 steps. Use the words 'kinetic energy transfer,' 'energy loss,' and 'collision' in your answer.")
    ],
    "background_intro": "Every time two objects collide, energy is transferred — but never perfectly. Understanding how energy moves from object to object and where it gets lost helps us explain everything from how Newton's cradles work to why car crumple zones save lives to why the last domino in a long chain falls with less force than the first.",
    "background_sections": [
        ("What Happens During a Collision", "When a moving object hits a stationary object, kinetic energy transfers from the moving object to the stationary one. In a perfectly elastic collision (like ideal billiard balls), all kinetic energy transfers and no energy is lost to other forms. In reality, perfectly elastic collisions do not exist. Every real collision converts some kinetic energy into sound (the bang or click you hear), heat (friction and deformation at the contact point), and vibration (the objects shake briefly after impact)."),
        ("Energy Loss at Every Step", "In a chain reaction with multiple collisions, energy is lost at EACH collision point. If 5% of kinetic energy is lost as sound and heat at each collision, then after 1 collision you have 95% of the original energy, after 2 collisions about 90%, after 5 collisions about 77%, and after 10 collisions only about 60%. This is why long chain reactions require a strong initial push — there must be enough energy at the start to survive all the losses and still have enough at the end to complete the final action."),
        ("Mass Matters", "The mass of the objects in a chain dramatically affects energy transfer. When a moving object collides with a stationary object of the SAME mass, nearly all kinetic energy transfers (minus losses). When a light object hits a heavy one, most energy bounces back and little transfers to the heavy object. When a heavy object hits a light one, the heavy object barely slows down and the light one shoots away with lots of speed. This is why Newton's cradles use identical balls — same mass ensures maximum energy transfer."),
        ("Real-World Chain Reactions", "Chain reactions are everywhere in the real world. In bowling, the ball transfers energy to the first pin, which transfers energy to pins behind it in a chain reaction. In car accidents, crumple zones are designed to absorb collision energy through a chain of controlled deformations, protecting the people inside. In nuclear reactions, one atom splitting releases energy that triggers neighboring atoms to split — a chain reaction that powers nuclear plants. Even your body uses chain reactions — nerve signals pass from cell to cell in a chain.")
    ],
    "lever_L": "Students identify Initial Push Force and Object Mass as external components (controllable choices) and Kinetic Energy Transfer, Energy Lost to Sound, and Final Object Speed as internal components that result from the collision chain.",
    "lever_E": "Students determine that Initial Push Force positively affects Kinetic Energy Transfer, Object Mass negatively affects Final Object Speed (heavier objects are harder to move), KE Transfer positively affects both Final Object Speed and Energy Lost to Sound, and Energy Lost to Sound negatively affects Final Object Speed.",
    "lever_V": "Students build a five-component model showing how energy flows from an initial push through a chain of collisions, with each collision leaking energy as sound, until what remains determines the final object's speed.",
    "lever_Ev": "Students run four scenarios to observe how push force and object mass combine to determine how much energy survives the chain, discovering that both strong pushes and light objects maximize final speed.",
    "lever_R": "Students add number of objects in chain or object material to explore how chain length amplifies energy loss and how different materials transfer energy with different efficiency.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with Newton's cradle and domino chain imagery", "say": "Watch this — I am going to push ONE marble, and something is going to happen at the OTHER end of this line. How does the energy get from here to there?", "do": "Demonstrate a Newton's cradle or a line of marbles. Pull back one ball, let it go, and watch the last ball fly out. Ask: How did the energy travel through all those balls?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are tracking energy as it JUMPS from one object to the next — and finding out where it leaks away at every step.", "do": "Have students read objectives aloud. Pre-teach 'collision' and 'energy transfer' by rolling a marble into a stationary marble.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why does the last domino fall slower than the first was pushed?", "say": "If I push the first domino hard, the last domino should fall just as hard, right? But it does not. Where does the energy GO?", "do": "Set up a line of 10 dominoes. Push the first one. Ask students to watch carefully — does the last one fall with the same force? Why not?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps with five components previewed", "say": "We are modeling what happens at every single collision in a chain reaction. Five components, and a sneaky energy leak.", "do": "Preview all five components. Tell students to listen for the 'click' sound at each collision — that click is ENERGY ESCAPING as sound.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Five component cards for collision system", "say": "We control two things: how hard we push and how heavy the objects are. Everything else is physics.", "do": "Guide sorting. Initial Push Force and Object Mass are external (we choose them). KE Transfer, Sound Loss, and Final Speed are internal (physics determines them).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows with + and - connections", "say": "Here is the tricky part: Kinetic Energy Transfer has TWO positive arrows going out — one to Final Object Speed and one to Energy Lost to Sound. They are COMPETING for the same energy!", "do": "Help students map the relationships. Emphasize that KE Transfer feeds both final speed AND sound loss — more energy transferring also means more energy leaking.", "time": "10 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph showing energy diminishing through chain", "say": "Watch the energy graph as the chain runs. See how each collision takes a little bite out of the energy? By the end, there is much less.", "do": "Run all four scenarios. Focus on the strong/light vs. weak/heavy comparison — the difference in final speed is dramatic.", "time": "12 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings with energy loss diagram", "say": "Every collision is an energy leak. The sound you hear is PROOF that energy is escaping from the motion system.", "do": "Have students clap their hands — the sound they hear IS kinetic energy transforming into sound energy. Each collision does the same thing.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Rube Goldberg chain reaction challenge", "say": "Build the LONGEST chain reaction you can where energy transfers through at least five collisions and completes a final action at the end!", "do": "Distribute materials (marbles, dominoes, toy cars, blocks, ramps). Groups design, build, and test chain reactions. Count successful collisions.", "time": "12 min"}
    ],
    "sort_reasoning": "Initial Push Force is external because the person starting the chain decides how hard to push — it is a choice made outside the chain system. Object Mass is external because we choose which objects to include in the chain — their mass is a design decision. Kinetic Energy Transfer, Energy Lost to Sound, and Final Object Speed are internal because they are physical outcomes determined by the laws of physics during each collision.",
    "relationships": [
        ("Initial Push Force to Kinetic Energy Transfer", "POSITIVE (+)", "A harder push gives the first object more kinetic energy, which means more energy is available to transfer through the chain. Double the push force and you roughly double the kinetic energy entering the system."),
        ("Object Mass to Final Object Speed", "NEGATIVE (-)", "Heavier objects require more energy to accelerate. In a chain of heavy objects, more energy is absorbed by each object's inertia, leaving less energy available for the final object's speed. Light objects transfer energy more efficiently."),
        ("Kinetic Energy Transfer to Final Object Speed", "POSITIVE (+)", "More kinetic energy transferring through the chain means more energy reaches the final object. The final object's speed depends directly on how much energy survives all the collisions to reach it."),
        ("Kinetic Energy Transfer to Energy Lost to Sound", "POSITIVE (+)", "When more energy transfers during a collision, the collision is also more energetic — producing a louder sound. More energy flowing through the system means more energy leaking out as sound at each collision point."),
        ("Energy Lost to Sound to Final Object Speed", "NEGATIVE (-)", "Energy converted to sound is energy that is no longer available for motion. Every bit of energy that becomes sound at each collision is subtracted from the energy that could have reached the final object. More sound loss means slower final object.")
    ],
    "sim_answers": [
        ("Strong Push, Light Objects", "With Initial Push Force at 80% and Object Mass at 20%, lots of kinetic energy enters the system and light objects transfer it efficiently. Energy Lost to Sound is noticeable at each collision (you can hear the clicks) but relatively small compared to the total energy. Final Object Speed is high because the strong start and efficient transfer overcome the losses."),
        ("Weak Push, Heavy Objects", "With Initial Push Force at 20% and Object Mass at 80%, very little kinetic energy enters the system and the heavy objects absorb much of it just getting started. Energy Lost to Sound is present at each collision, and combined with the mass-related losses, Final Object Speed is extremely low — the chain may barely complete, and the last object may hardly move at all.")
    ],
    "reflection_exemplars": [
        ("Why does each collision lose energy?", "Every collision converts a small percentage of kinetic energy into other forms — primarily sound and heat. The 'click' or 'bang' you hear when objects collide IS kinetic energy that has been transformed into sound wave energy. At the contact point, there is also friction and slight deformation of the materials, which converts some kinetic energy into heat (though the amount is too small to feel). These losses are required by physics — there is no such thing as a perfectly efficient collision in the real world. Each loss is small, but across many collisions, they add up significantly."),
        ("Would you use heavy or light objects for the longest chain?", "I would use LIGHT objects for the longest chain. Our model showed that Object Mass has a negative relationship with Final Object Speed — heavier objects absorb more energy from each collision just to get moving, leaving less energy to pass on. Light objects move easily, requiring less energy to accelerate, so more kinetic energy transfers through to the next collision. With light objects, the energy survives more collisions before running out. Of course, I would also want a strong initial push to give the chain maximum starting energy.")
    ],
    "stem_intro": "Present the challenge: A science museum wants a Rube Goldberg machine exhibit showing visitors how energy passes from object to object. Your team must build the LONGEST chain reaction possible — at least five collisions — where a push at the start triggers a final action at the end (ring a bell, knock over a cup, launch a marble into a target). Explain where energy is gained, transferred, and lost at each step!",
    "stem_concepts": [
        ("Energy Enters at the Start", "The initial push is the only energy input. Everything after that is energy transferring from object to object. A stronger push gives your chain more energy to work with, allowing it to be longer."),
        ("Energy Leaks at Every Collision", "Each time objects collide, some energy becomes sound and heat. You can hear these losses (the clicks and bangs). The more collisions in your chain, the more total energy is lost, which is why the chain eventually runs out of energy."),
        ("Mass and Efficiency", "Light objects transfer energy more efficiently than heavy ones. If you mix heavy and light objects, think about the order — a heavy object hitting a light one will send the light one flying, but a light object hitting a heavy one barely moves it.")
    ],
    "stem_eval": [
        ("Expert (4)", "Chain has 5+ successful collisions with a clear final action, student explains energy input, transfer, and loss at each step using model vocabulary, and can identify where most energy is lost"),
        ("Proficient (3)", "Chain has 4+ collisions with a final action, student can explain energy transfer and loss in general terms"),
        ("Developing (2)", "Chain has 3 collisions but final action is weak or absent, student understands energy transfers but cannot explain losses"),
        ("Beginning (1)", "Chain has fewer than 3 successful collisions or student cannot explain how energy moves through the chain")
    ],
    "support": [
        "Provide a labeled diagram of a Newton's cradle showing where energy enters, transfers, and exits as sound at each collision",
        "Let students clap their hands together — the sound they hear is kinetic energy (their hands moving) transforming into sound energy (the clap). Every collision does the same thing.",
        "Sentence frames: 'When Initial Push Force increases, Kinetic Energy Transfer __ because __. At each collision, Energy Lost to Sound __ which makes Final Object Speed __.'"
    ],
    "extensions": [
        "Research how car crumple zones use chain reaction energy absorption to protect passengers — each crumple zone panel absorbs energy through controlled deformation",
        "Build a Newton's cradle and test what happens when you pull back 1, 2, or 3 balls — how does the number of input balls change the output?",
        "Calculate the percentage of energy lost at each collision by measuring the speed of marbles before and after each hit in a chain"
    ],
    "cross_curr": [
        ("Math", "If 5% of energy is lost at each of 10 collisions, calculate the percentage of original energy remaining after each collision and create a decreasing line graph"),
        ("ELA", "Write a creative story from the perspective of kinetic energy traveling through a Rube Goldberg machine, describing what happens at each collision and each transformation"),
        ("Music", "Connect energy transfer to percussion instruments — when a drumstick hits a drum, kinetic energy transfers to the drum skin, which vibrates to create sound. Different materials create different sounds based on how they absorb and release energy.")
    ],
    "misconceptions": [
        ("Energy passes through the chain without any loss", "Every real collision loses some energy to sound, heat, and vibration. You can HEAR this loss — the clicking or banging sound during each collision IS kinetic energy that has transformed into sound energy and left the motion system. If energy transferred perfectly, every chain reaction would go on forever, but they do not because of these unavoidable losses.", "Line up 10 dominoes and push the first one. Listen to the click at each collision — that sound is PROOF that energy is leaking from the system at every step."),
        ("Heavier objects are better for chain reactions because they have more energy", "While heavier objects CAN carry more kinetic energy when moving at the same speed, they also require MORE energy to get moving in the first place. In a chain reaction, a heavy stationary object absorbs more of the incoming energy just to start moving, leaving less to pass to the next object. LIGHTER objects require less energy to accelerate, so more energy flows through the chain.", "Roll a marble into a line of identical marbles, then roll the same marble into a bowling ball. The marble chain transfers energy efficiently; the bowling ball barely moves. Same push, very different results."),
        ("The sound of a collision is separate from the energy transfer", "The sound IS part of the energy transfer — or more accurately, it is energy LEAKING from the transfer. When two objects collide, kinetic energy transforms into several forms simultaneously: some transfers as kinetic energy to the next object, some becomes sound waves, and some becomes heat. The sound and heat are not separate events — they are part of the same collision physics. Louder collisions mean more energy was converted to sound, meaning LESS energy was available for motion.", "Collide two objects gently (soft sound) then forcefully (loud sound). The louder collision had more energy in it, and more energy was converted to sound. Ask: if the sound is louder, does the next object get MORE or LESS kinetic energy?")
    ]
}
