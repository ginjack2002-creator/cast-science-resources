#!/usr/bin/env python3
"""Complete lesson data for G04-L01 through G04-L10 (Grade 4 ModelIt! Lessons)"""

L01 = {
    "id": "G04-L01",
    "title": "Why Do Roller Coasters Go So Fast?",
    "subtitle": "The Amazing Science of Energy and Speed",
    "ngss": "4-PS3-1",
    "ngss_desc": "Use evidence to construct an explanation relating the speed of an object to the energy of that object.",
    "big_question": "How does a roller coaster go super fast at the bottom of a hill without any engine pushing it?",
    "objectives": [
        "Explain how the height of a hill affects how fast a roller coaster goes at the bottom",
        "Model how hill height, speed, and energy of motion are connected",
        "Describe how energy changes form as a roller coaster moves along a track"
    ],
    "vocabulary": [
        ("Energy", "The ability to make things move, change, or do work"),
        ("Speed", "How fast an object is moving from one place to another"),
        ("Kinetic Energy", "The energy an object has because it is moving — the faster it goes, the more it has"),
        ("Potential Energy", "Stored energy that an object has because of its height or position")
    ],
    "components": [
        ("Hill Height", "How tall the roller coaster hill is — taller hills store more energy at the top", True),
        ("Speed at Bottom", "How fast the roller coaster car is moving when it reaches the bottom of the hill", False),
        ("Energy of Motion", "The amount of kinetic energy the roller coaster has — more speed means more energy", False)
    ],
    "think_about_it": "When hill height increases, what happens to speed at the bottom? Is the relationship positive or negative?",
    "scenarios": [
        ("Small Hill", "Set Hill Height to low and observe the speed at the bottom of the hill"),
        ("Giant Hill", "Set Hill Height to maximum and observe how speed and energy change"),
        ("Medium Hill", "Set Hill Height to 50% and compare speed to both the small and giant hill")
    ],
    "sim_scenarios": [
        ("Small Hill", "Hill Height set to low", "What do you predict will happen to Speed at Bottom when the hill is small?"),
        ("Giant Hill", "Hill Height set to maximum", "What do you predict will happen to Energy of Motion when the hill is really tall?"),
        ("Medium Hill", "Hill Height set to 50%", "Will the speed at the bottom be exactly half of the giant hill speed? Why or why not?")
    ],
    "discoveries": [
        "Taller hills give the roller coaster more stored energy at the top, which turns into more speed at the bottom",
        "Speed and energy of motion are connected — when speed goes up, energy of motion goes up too",
        "Energy is never created or destroyed — it just changes from one form to another",
        "A roller coaster at the top of a hill has lots of potential energy that converts to kinetic energy as it rolls down"
    ],
    "answer": "A roller coaster goes fast at the bottom because of ENERGY! At the top of a tall hill, the coaster has stored-up potential energy. As it rolls down, that stored energy transforms into kinetic energy — the energy of motion. The taller the hill, the more energy gets stored, and the faster the coaster zooms at the bottom!",
    "stem_title": "Design the Ultimate Marble Run",
    "stem_mission": "Design a marble run track that makes a marble go as fast as possible at the bottom using what you learned about height and energy.",
    "stem_scenario": "A toy company wants to create the most exciting marble run ever! Your engineering team has been hired to design a track that uses hills and ramps to make the marble reach maximum speed. Use evidence from your model to make your design choices.",
    "stem_questions": [
        "How tall should your first hill be to get the most speed at the bottom?",
        "What happens if you add a second hill that is taller than the first one?",
        "How can you prove that your marble has more energy of motion at the bottom than at the top?"
    ],
    "stem_design_qs": [
        "What is the tallest hill you can build with the materials you have?",
        "How will you measure the speed of your marble at the bottom?",
        "What shape should your ramp be — straight, curved, or bumpy?",
        "How will you compare different hill heights to see which gives the most speed?"
    ],
    "career": "Roller Coaster Engineers and Mechanical Engineers design theme park rides by using math and science to make sure rides are thrilling AND safe. They earn $65,000–$110,000/year.",
    "images": {
        "cover": ("cover-rollercoaster.png", "A thrilling, colorful roller coaster at the peak of a tall hill against a bright blue sky, dramatic angle looking up, cinematic amusement park photography with vivid colors"),
        "landscape": ("landscape-rollercoaster.png", "A photorealistic image of diverse 4th grade students (9-10 years old, 70-80% Black and Brown children with realistic coils, curls, locs, and braids) excitedly building marble ramps on their desks in a bright modern classroom, natural window light, editorial photo quality"),
        "modeling": ("modeling-rollercoaster.png", "A photorealistic image of diverse 4th grade students (9-10 years old, Black and Brown children centered with realistic hair detail) working together on laptops building a digital roller coaster model, modern classroom with colorful science posters"),
        "discussion": ("discussion-rollercoaster.png", "A photorealistic image of a Black female teacher leading an animated discussion with diverse 4th graders (9-10 years old, Black and Brown children centered) about roller coasters, pointing at a diagram on a smartboard showing hills and speed arrows, students with hands raised"),
        "stem": ("stem-rollercoaster.png", "A photorealistic image of diverse 4th grade students (9-10 years old, 70-80% Black and Brown children with coils, curls, locs, braids) building marble run tracks from cardboard tubes and tape, testing marbles, excited collaborative group work at tables")
    },
    "pre_assessment": [
        "Have you ever been on a roller coaster? What was the scariest part?",
        "Why do you think roller coasters go really fast at the bottom of a big hill?",
        "Draw what you think happens to a roller coaster's speed as it goes up and down hills.",
        "What do you think 'energy' means in science?"
    ],
    "extend_components": [
        ("Friction", "The rubbing force between the coaster and the track that slows it down and turns energy into heat"),
        ("Coaster Mass", "How heavy the roller coaster car is — heavier cars have more energy at the same speed"),
        ("Track Curve Shape", "Whether the track is straight, curved, or looping affects how speed changes")
    ],
    "reflections": [
        "Why does a roller coaster go fastest at the very bottom of the tallest hill?",
        "If energy can't be created or destroyed, where does the roller coaster's energy come from in the first place?",
        "Why does a roller coaster eventually slow down and stop if energy is never destroyed?",
        "How is rolling a ball down a ramp similar to a roller coaster going down a hill?",
        "How did your model help you understand something you can see at an amusement park?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how hill height, speed, and energy of motion are connected in a roller coaster system."),
        ("Disciplinary Core Idea", "PS3.A Definitions of Energy", "The faster a given object is moving, the more energy it possesses. Energy can be moved from place to place by moving objects or through sound, light, or electric currents."),
        ("Crosscutting Concept", "Energy and Matter", "Students explore how energy transforms from potential to kinetic as a roller coaster moves, demonstrating that energy is conserved but changes form.")
    ],
    "cast_items": [
        "Explain how the height of a hill affects the speed at the bottom",
        "Use a model to describe the relationship between speed and energy of motion",
        "Describe how energy changes form in a roller coaster system"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A marble rolls down a tall ramp and then a short ramp. It goes faster at the bottom of the tall ramp. Which best explains why?"),
        ("Constructed Response:", "Using what you know about energy, explain why a roller coaster goes fastest at the bottom of the tallest hill on the track. Use the words 'potential energy' and 'kinetic energy' in your answer.")
    ],
    "background_intro": "Energy is one of the most important concepts in all of science. Understanding how energy changes form helps us explain everything from roller coasters to rocket ships to why our food gives us the power to run and play.",
    "background_sections": [
        ("What Is Energy?", "Energy is the ability to cause change or do work. It comes in many forms: kinetic energy (motion), potential energy (stored), thermal energy (heat), sound energy, light energy, and more. Energy is never created or destroyed — it only changes from one form to another. This is called the Law of Conservation of Energy."),
        ("Potential Energy and Height", "When an object is lifted up high, it gains gravitational potential energy — energy stored because of its position. The higher the object, the more potential energy it has. A roller coaster at the top of a 100-foot hill has much more stored energy than one at the top of a 20-foot hill. This stored energy is like a battery waiting to be used."),
        ("Kinetic Energy and Speed", "Kinetic energy is the energy of motion. Any moving object has kinetic energy, and the faster it moves, the more kinetic energy it has. When a roller coaster rolls downhill, its potential energy converts to kinetic energy. At the very bottom of the hill, nearly all the stored energy has become motion energy — that is when the coaster is going fastest."),
        ("Energy in Everyday Life", "Energy transformations happen all around us every day. When you eat food, chemical energy transforms into kinetic energy so you can move. When you turn on a light, electrical energy transforms into light and heat energy. A bouncing ball converts kinetic energy to potential energy and back with every bounce. Understanding energy helps engineers design everything from cars to buildings to playground equipment.")
    ],
    "lever_L": "Students identify hill height as an external component and speed at bottom and energy of motion as internal components that change in response to hill height.",
    "lever_E": "Students determine that hill height positively affects speed at bottom, and speed at bottom positively affects energy of motion — creating a direct chain of cause and effect.",
    "lever_V": "Students build a model showing how increasing hill height leads to greater speed and more energy of motion at the bottom of the hill.",
    "lever_Ev": "Students run small hill, medium hill, and giant hill scenarios to observe how changing one input (height) affects the entire system.",
    "lever_R": "Students add friction or coaster mass to explore why real roller coasters eventually slow down even though energy is conserved.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with exciting roller coaster imagery", "say": "Who here has been on a roller coaster? What is the most exciting part — going up or zooming down?", "do": "Show a short roller coaster video clip. Let students share their experiences briefly.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are going to figure out the SCIENCE behind why roller coasters go so fast!", "do": "Have students read objectives aloud. Pre-teach 'kinetic energy' and 'potential energy' with simple examples.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How does a coaster go fast without an engine?", "say": "Here is the mystery: a roller coaster has NO engine pushing it downhill. So where does all that speed come from?", "do": "Have students turn and talk with a partner: What do you think makes a roller coaster go fast at the bottom?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We are going to build a model to crack this mystery — step by step.", "do": "Briefly preview each LEVER step. Remind students what a model is and why scientists use them.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for roller coaster model", "say": "What things affect how fast a roller coaster goes? Let us sort them into things we can control and things that happen inside the system.", "do": "Guide sorting of three components. Explain that hill height is external because WE decide how tall to build the hill.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "When the hill gets taller, what happens to the speed? Does speed go UP or DOWN?", "do": "Help students draw positive arrows from hill height to speed, and from speed to energy of motion.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Time to test our model! Let us start with a tiny hill and work our way up to the biggest hill possible.", "do": "Have students predict first, then run each scenario. Compare small vs. medium vs. giant hill results.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "So NOW we know the secret — it is all about ENERGY changing form!", "do": "Summarize findings. Use a ball and ramp to physically demonstrate energy conversion.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Marble run design challenge", "say": "Now YOU are the engineers! Design the fastest marble run you can.", "do": "Distribute materials (cardboard tubes, tape, marbles). Groups design and test marble runs using model evidence.", "time": "12 min"}
    ],
    "sort_reasoning": "Hill Height is external because it is determined by how the track is built — it is a design choice that exists before the coaster even starts moving. Speed at Bottom and Energy of Motion are internal because they are results that happen INSIDE the system in response to the hill height.",
    "relationships": [
        ("Hill Height to Speed at Bottom", "POSITIVE (+)", "A taller hill gives the coaster more stored potential energy. As it rolls down, more stored energy converts to more speed. Double the height means noticeably more speed at the bottom."),
        ("Speed at Bottom to Energy of Motion", "POSITIVE (+)", "The faster the coaster moves, the more kinetic energy it has. Speed and energy of motion always increase together — you cannot have high speed without high energy.")
    ],
    "sim_answers": [
        ("Small Hill Scenario", "When Hill Height is set to low, Speed at Bottom is slow and Energy of Motion is low. The coaster barely picks up speed because there is not much stored energy at the top of a short hill. The marble rolls gently to the bottom."),
        ("Giant Hill Scenario", "When Hill Height is set to maximum, Speed at Bottom is very fast and Energy of Motion is very high. The tall hill stores a huge amount of potential energy that all converts to kinetic energy on the way down. This is why the biggest hills on roller coasters are always the most exciting!")
    ],
    "reflection_exemplars": [
        ("Why does the coaster go fastest at the very bottom?", "At the top of the hill, the coaster has lots of potential energy (stored energy from being up high) but is barely moving. As it rolls down, that stored energy changes into kinetic energy (energy of motion). At the very bottom, almost ALL the stored energy has become motion energy, so that is when the coaster is going the fastest."),
        ("Where does the energy come from if there is no engine?", "The energy comes from GRAVITY and HEIGHT. When the coaster is pulled to the top of the first hill, energy is stored in its position — like stretching a rubber band. Gravity pulls the coaster down and that stored energy transforms into speed. The chain lift at the beginning is the only part that needs an engine — after that, energy does all the work!")
    ],
    "stem_intro": "Present the challenge: A toy company wants you to design the most exciting marble run ever. Your track must use hills and ramps to make the marble go as fast as possible at the finish line. Use what your model taught you about height and energy!",
    "stem_concepts": [
        ("Energy Transformation", "Energy changes form but is never lost. At the top of a hill, energy is stored (potential). At the bottom, it becomes motion (kinetic). Your marble run should use this transformation to build speed."),
        ("Height Equals Stored Energy", "The taller your starting hill, the more energy your marble stores before it rolls. This is the single biggest factor in how fast your marble will go."),
        ("Friction Steals Energy", "In the real world, some energy turns into heat from friction between the marble and the track. Smooth tracks lose less energy than bumpy ones.")
    ],
    "stem_eval": [
        ("Expert (4)", "Marble run uses model evidence to explain design choices, tests multiple hill heights, and connects results to energy transformation"),
        ("Proficient (3)", "Marble run demonstrates height-speed relationship and student can explain why taller hills produce more speed"),
        ("Developing (2)", "Marble run is built but student struggles to connect hill height to speed using energy concepts"),
        ("Beginning (1)", "Marble run is incomplete or student cannot explain the connection between height and speed")
    ],
    "support": [
        "Provide a labeled diagram showing potential energy at the top and kinetic energy at the bottom of a hill",
        "Use a physical ramp and ball to let students feel the difference between rolling from a high vs. low point",
        "Sentence frames: 'When the hill is taller, the speed at the bottom is __ because __'"
    ],
    "extensions": [
        "Research how real roller coaster engineers decide how tall to make the first hill",
        "Test what happens when you change the mass of the rolling object — does a heavier marble go faster?",
        "Design a roller coaster track where the coaster must make it over a second hill — how tall can that hill be?"
    ],
    "cross_curr": [
        ("Math", "Measure the height of different ramps and the speed of marbles at the bottom to look for a pattern using tables and graphs"),
        ("ELA", "Write a letter to a roller coaster company explaining why their biggest hill should be first, using science evidence"),
        ("Art", "Design and draw a roller coaster that shows where potential and kinetic energy are highest using color coding")
    ],
    "misconceptions": [
        ("Roller coasters have engines that push them the whole time", "Most roller coasters only use a motor for the first hill (the chain lift). After that, gravity and energy do all the work! The coaster converts stored potential energy into kinetic energy as it goes downhill.", "Demo: Pull a marble to the top of a ramp and let go — it speeds up without any push. Ask: What is making it move?"),
        ("Heavier things always go faster", "On a frictionless ramp, all objects fall at the same rate regardless of weight — Galileo proved this! In real life, heavier objects may roll slightly differently because of friction, but height is what really determines speed at the bottom.", "Drop a heavy and a light ball from the same height at the same time — they land together! Height matters more than weight."),
        ("Energy gets used up and disappears", "Energy is NEVER destroyed — it only changes form. When a roller coaster slows down, the kinetic energy does not vanish. It transforms into heat energy from friction and sound energy from the rumbling wheels. The total amount of energy stays the same.", "Ask: If the coaster slows down, where did the energy go? Rub your hands together fast — feel the heat? That is kinetic energy turning into thermal energy!")
    ]
}

L02 = {
    "id": "G04-L02",
    "title": "How Does Your Phone Hear Your Voice?",
    "subtitle": "The Invisible Science of Sound Waves",
    "ngss": "4-PS4-1",
    "ngss_desc": "Develop a model of waves to describe patterns in terms of amplitude and wavelength and that waves can cause objects to move.",
    "big_question": "When you talk to your phone, how does it turn the invisible vibrations in the air into something it can understand?",
    "objectives": [
        "Explain how sound waves are created by vibrations and travel through the air",
        "Model how sound wave strength, vibration size, and volume level are connected",
        "Describe how changing the strength of a sound changes its amplitude and volume"
    ],
    "vocabulary": [
        ("Sound Wave", "A vibration that travels through air, water, or other materials and can be heard by our ears"),
        ("Vibration", "A back-and-forth movement that happens very quickly — all sounds start with vibrations"),
        ("Amplitude", "How big a wave is from top to bottom — bigger amplitude means louder sound"),
        ("Volume", "How loud or soft a sound is — it depends on the amplitude of the sound wave")
    ],
    "components": [
        ("Sound Wave Strength", "How much energy goes into making the sound — like speaking softly vs. shouting", True),
        ("Vibration Size", "How far back and forth the air particles move — this is the amplitude of the wave", False),
        ("Volume Level", "How loud the sound is when it reaches your ear or a microphone", False)
    ],
    "think_about_it": "When sound wave strength increases, what happens to vibration size? Is the relationship positive or negative?",
    "scenarios": [
        ("Whisper", "Set Sound Wave Strength to low and observe Vibration Size and Volume Level"),
        ("Shout", "Set Sound Wave Strength to maximum and observe how Vibration Size and Volume change"),
        ("Normal Voice", "Set Sound Wave Strength to 50% and compare to whisper and shout")
    ],
    "sim_scenarios": [
        ("Whisper", "Sound Wave Strength set to low", "What do you predict will happen to Volume Level when someone whispers?"),
        ("Shout", "Sound Wave Strength set to maximum", "What do you predict will happen to Vibration Size when someone shouts?"),
        ("Normal Voice", "Sound Wave Strength set to 50%", "Will Volume Level be exactly halfway between a whisper and a shout?")
    ],
    "discoveries": [
        "Sound is created by vibrations — every sound you hear started with something moving back and forth very fast",
        "Bigger vibrations (larger amplitude) make louder sounds, and smaller vibrations make softer sounds",
        "Sound waves need something to travel through — they cannot travel through empty space",
        "Your phone's microphone has a tiny part inside that vibrates when sound waves hit it, turning sound into electrical signals"
    ],
    "answer": "Your phone hears you because sound waves are real, physical vibrations in the air! When you speak, your vocal cords vibrate and push air molecules back and forth. Those vibrations travel through the air as sound waves. Inside your phone, a tiny microphone has a piece called a diaphragm that vibrates when sound waves hit it — turning your voice into electrical signals the phone can process!",
    "stem_title": "Build a Sound Wave Catcher",
    "stem_mission": "Design a device that can detect and show sound waves using simple materials, proving that sound is made of real vibrations.",
    "stem_scenario": "A music studio needs a way to SHOW musicians how loud they are playing without using electronics. Your engineering team must design a simple device that makes sound waves visible so musicians can see how strong their sound is.",
    "stem_questions": [
        "How can you make invisible sound waves visible so you can see them?",
        "What materials vibrate the most when sound waves hit them?",
        "How does your device show the difference between a loud sound and a soft sound?"
    ],
    "stem_design_qs": [
        "What material will you use to catch sound vibrations (plastic wrap, paper, foil)?",
        "How will you make the vibrations visible (salt, rice, glitter on the surface)?",
        "How will you test your device with different volumes?",
        "How will you prove that louder sounds cause bigger vibrations?"
    ],
    "career": "Sound Engineers and Audio Technicians use science to record, mix, and design sound for music, movies, and live events. They earn $45,000–$95,000/year.",
    "images": {
        "cover": ("cover-soundwaves.png", "A stunning visualization of colorful sound waves radiating outward from a smartphone microphone, showing wave patterns in vibrant blues and purples against a dark background, scientific and dramatic"),
        "landscape": ("landscape-soundwaves.png", "A photorealistic image of diverse 4th grade students (9-10 years old, 70-80% Black and Brown children with realistic coils, curls, locs, and braids) exploring sound with tuning forks and cups-and-string phones in a bright modern classroom, natural window light"),
        "modeling": ("modeling-soundwaves.png", "A photorealistic image of diverse 4th grade students (9-10 years old, Black and Brown children centered with realistic hair detail) working together on laptops building a digital sound wave model, modern classroom with sound wave diagrams on the wall"),
        "discussion": ("discussion-soundwaves.png", "A photorealistic image of a Black male teacher leading an animated discussion with diverse 4th graders (9-10 years old, Black and Brown children centered) about how phones hear sound, pointing at a sound wave diagram on a smartboard"),
        "stem": ("stem-soundwaves.png", "A photorealistic image of diverse 4th grade students (9-10 years old, 70-80% Black and Brown children with coils, curls, locs, braids) building sound catchers with plastic wrap stretched over bowls with rice on top, testing by making sounds nearby")
    },
    "pre_assessment": [
        "What do you think sound is? How does it get from one place to another?",
        "Why do you think you can hear someone even when you cannot see them?",
        "Draw what you think happens in the air between your mouth and someone's ear when you talk.",
        "How do you think a phone knows when you are talking to it?"
    ],
    "extend_components": [
        ("Distance from Source", "How far away you are from the sound — sound gets quieter the farther it travels"),
        ("Material Type", "What the sound is traveling through — sound moves differently through air, water, and solids"),
        ("Pitch", "How high or low a sound is — this depends on how fast the vibrations happen")
    ],
    "reflections": [
        "If sound is made of vibrations, what is vibrating when you hear music from a speaker?",
        "Why is it impossible to hear sounds in outer space?",
        "How is a loud shout different from a soft whisper in terms of what the air is doing?",
        "What would happen if you tried to talk to someone on the Moon with no equipment?",
        "How did your model help you understand something invisible like sound waves?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how sound wave strength, vibration size, and volume level are connected in a wave system."),
        ("Disciplinary Core Idea", "PS4.A Wave Properties", "Waves, which are regular patterns of motion, can be made in water by disturbing the surface. Waves of the same type can differ in amplitude and wavelength. Waves can cause objects to move."),
        ("Crosscutting Concept", "Cause and Effect", "Students explore how changing the strength of a sound (cause) directly affects vibration size and volume (effects) in a predictable pattern.")
    ],
    "cast_items": [
        "Explain how sound waves are created by vibrations and travel through the air",
        "Use a model to describe the relationship between wave strength and volume",
        "Describe how amplitude determines how loud a sound is"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student plucks a guitar string gently, then plucks it hard. The hard pluck makes a louder sound. Which best explains why the sound is louder?"),
        ("Constructed Response:", "Using what you know about sound waves, explain how your voice travels from your mouth to a friend's ear across the room. Use the words 'vibration,' 'sound wave,' and 'amplitude' in your answer.")
    ],
    "background_intro": "Sound is all around us every moment of every day, yet we cannot see it. Understanding sound waves helps us explain how we communicate, how music works, and how modern technology like phones and speakers turn invisible vibrations into the sounds we love.",
    "background_sections": [
        ("What Makes Sound?", "Every sound begins with a vibration. When you speak, your vocal cords vibrate. When you clap, your hands vibrate. When a drum is hit, the drum skin vibrates. These vibrations push air molecules back and forth, creating a chain reaction of moving air particles that spreads outward in all directions — these traveling vibrations are sound waves."),
        ("How Sound Waves Travel", "Sound waves are longitudinal waves — the air molecules compress together (compression) and spread apart (rarefaction) in the same direction the wave is traveling. Sound needs a medium (material) to travel through. It moves through air at about 343 meters per second, faster through water (1,480 m/s), and even faster through solids like steel (5,960 m/s). Sound cannot travel through a vacuum (empty space)."),
        ("Amplitude and Volume", "Amplitude is the height of a wave — how far the air molecules move from their resting position. Larger amplitude means the molecules move farther back and forth, carrying more energy, which our ears detect as louder sound. When you whisper, the amplitude is tiny. When you shout, the amplitude is large. Volume is measured in decibels (dB). A whisper is about 30 dB, normal talking is 60 dB, and a rock concert is 110 dB."),
        ("How Microphones Work", "A microphone is a device that converts sound waves into electrical signals. Inside a basic microphone is a thin membrane called a diaphragm. When sound waves hit the diaphragm, it vibrates back and forth just like the original source. These vibrations are converted into electrical signals that match the pattern of the original sound wave. This is how phones, computers, and recording studios capture sound.")
    ],
    "lever_L": "Students identify sound wave strength as an external component and vibration size and volume level as internal components that respond to the strength of the sound.",
    "lever_E": "Students determine that sound wave strength positively affects vibration size, and vibration size positively affects volume level — a direct cause-and-effect chain.",
    "lever_V": "Students build a model showing how stronger sounds create bigger vibrations that produce louder volume.",
    "lever_Ev": "Students run whisper, normal voice, and shout scenarios to observe how changing sound wave strength affects the entire system.",
    "lever_R": "Students add distance from source or material type to explore why sounds get quieter over distance or sound different underwater.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with sound wave imagery and smartphone", "say": "Hey everyone — talk to your hand right now. Can you FEEL the vibrations? That is actually sound waves hitting your skin!", "do": "Have students talk into their cupped hands to feel vibrations. Then ask: How does your phone feel these same vibrations?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are going to figure out how your phone can HEAR you — even though it does not have ears!", "do": "Have students read objectives aloud. Pre-teach 'vibration' and 'amplitude' with a ruler vibrating off a desk edge.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How does a phone turn invisible air vibrations into sound?", "say": "You cannot see sound. You cannot touch it. But somehow your phone catches it perfectly. How?", "do": "Have students turn and talk: What do you think is happening in the air between your mouth and the phone?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We are going to build a model of sound to solve this mystery.", "do": "Briefly preview each LEVER step. Remind students that a model helps us understand things we cannot see.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for sound wave model", "say": "What makes a sound loud or soft? What parts of this system can we identify?", "do": "Guide sorting of three components. Explain that sound wave strength is external because the SPEAKER controls how hard they push air.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "When you shout, are the vibrations bigger or smaller? What about the volume?", "do": "Help students draw positive arrows showing the chain: more strength leads to bigger vibrations leads to louder volume.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let us test it! We will start with a whisper and end with a shout.", "do": "Have students predict first, then run simulations for whisper, normal, and shout. Compare the wave diagrams.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "Now we know the secret — sound is made of real vibrations, and louder means BIGGER vibrations!", "do": "Summarize discoveries. Demonstrate with a tuning fork in water to make vibrations visible.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Sound wave catcher design challenge", "say": "Can you build something that SHOWS sound waves? Let us make the invisible visible!", "do": "Distribute materials (bowls, plastic wrap, rice, rubber bands). Groups build sound catchers and test with different volumes.", "time": "12 min"}
    ],
    "sort_reasoning": "Sound Wave Strength is external because it comes from the sound source (the person speaking, the instrument playing) — it is determined by something outside the wave system itself. Vibration Size and Volume Level are internal because they are properties of the wave that change as a result of how strong the source is.",
    "relationships": [
        ("Sound Wave Strength to Vibration Size", "POSITIVE (+)", "A stronger sound pushes air molecules harder, making them move farther back and forth. More energy in means bigger vibrations — shout and the waves are big, whisper and they are tiny."),
        ("Vibration Size to Volume Level", "POSITIVE (+)", "Bigger vibrations carry more energy to your ear (or a microphone). Your ear detects bigger vibrations as louder sound. This is why amplitude and volume are directly connected.")
    ],
    "sim_answers": [
        ("Whisper Scenario", "When Sound Wave Strength is set to low, Vibration Size is very small and Volume Level is quiet. The air molecules barely move back and forth, carrying only a tiny amount of energy. The sound can only be heard very close to the source."),
        ("Shout Scenario", "When Sound Wave Strength is set to maximum, Vibration Size is very large and Volume Level is very loud. The air molecules move far back and forth, carrying lots of energy. The model clearly shows that stronger sounds create bigger waves with more volume.")
    ],
    "reflection_exemplars": [
        ("Why can't you hear sounds in outer space?", "Sound waves are vibrations that travel by pushing air molecules back and forth. In outer space, there are almost no molecules at all — it is a vacuum. With nothing to vibrate and push, the sound wave cannot travel. It is like trying to do the wave at a stadium with no people — the wave needs something to move through!"),
        ("How is a shout different from a whisper in terms of what the air is doing?", "When you whisper, you push a tiny amount of air out gently. The air molecules barely move back and forth — the vibrations are small, so the amplitude is low and the sound is quiet. When you shout, you push a LOT of air out forcefully. The air molecules move much farther back and forth — big vibrations, big amplitude, loud sound. Same type of wave, just bigger!")
    ],
    "stem_intro": "Present the challenge: A music studio needs a device that makes sound waves visible without electronics. Your team must design a simple sound catcher that shows the difference between loud and soft sounds so musicians can SEE how strong their sound is.",
    "stem_concepts": [
        ("Sound Waves Are Physical", "Sound is not just something you hear — it is actual air molecules moving back and forth. Anything light enough will vibrate when sound waves hit it, which is how we can make sound visible."),
        ("Amplitude Equals Loudness", "The bigger the vibrations (amplitude), the louder the sound. Your device should show bigger movement for louder sounds and smaller movement for softer sounds."),
        ("Resonance", "Some materials vibrate more easily than others when sound waves hit them. Choosing the right material for your sound catcher is key to making it work well.")
    ],
    "stem_eval": [
        ("Expert (4)", "Sound catcher clearly shows different vibration sizes for loud vs. soft sounds, student explains using wave vocabulary and connects to model evidence"),
        ("Proficient (3)", "Sound catcher detects sound and student can explain the connection between volume and vibration size"),
        ("Developing (2)", "Sound catcher shows some response to sound but student struggles to explain using wave concepts"),
        ("Beginning (1)", "Sound catcher is incomplete or does not visibly respond to sound")
    ],
    "support": [
        "Provide a simple diagram showing sound waves as compressions and rarefactions in air",
        "Let students feel vibrations by touching a speaker, humming while touching their throat, or holding a vibrating tuning fork",
        "Sentence frames: 'When the sound is louder, the vibrations are __ because __'"
    ],
    "extensions": [
        "Research how cochlear implants help deaf people hear by turning sound waves into electrical signals",
        "Test whether sound travels faster through air, water, or a solid table by tapping on different materials",
        "Record your voice on a phone and look at the sound wave picture — what do you notice about loud vs. quiet parts?"
    ],
    "cross_curr": [
        ("Math", "Measure the volume of different sounds using a decibel meter app and create a bar graph comparing them"),
        ("ELA", "Write a story from the perspective of a sound wave traveling from a singer's mouth to an audience member's ear"),
        ("Music", "Explore how different instruments create sound through different types of vibrations — strings, air columns, and drum skins")
    ],
    "misconceptions": [
        ("Sound can travel through empty space", "Sound MUST have a medium (air, water, or a solid) to travel through. Unlike light, sound cannot travel through a vacuum because there are no molecules to vibrate. This is why there is no sound in outer space — even if a star explodes!", "Put a ringing phone inside a sealed jar and show that it gets quieter as you pump out the air (or show a video of this experiment)."),
        ("Louder sounds travel faster", "Loud and quiet sounds travel at the SAME speed through the same material. A whisper and a shout both travel through air at about 343 meters per second. Volume only changes the SIZE of the vibrations (amplitude), not the speed of the wave.", "Clap loudly and softly from the same distance — both sounds reach the listener at the same time."),
        ("Sound only travels in one direction", "Sound waves spread out in ALL directions from the source, like ripples from a stone dropped in water. That is why you can hear someone talking even if you are behind them or around a corner. Sound waves expand as a sphere from the source.", "Have one student talk while others listen from different positions around the room — everyone can hear, proving sound goes in all directions.")
    ]
}

L03 = {
    "id": "G04-L03",
    "title": "Why Can't You See in the Dark?",
    "subtitle": "The Surprising Science of Light and Vision",
    "ngss": "4-PS4-2",
    "ngss_desc": "Develop a model to describe that light reflecting from objects and entering the eye allows objects to be seen.",
    "big_question": "If your eyes are open in a completely dark room, why can you not see anything at all?",
    "objectives": [
        "Explain that objects are seen only when light bounces off them and enters the eye",
        "Model how light source brightness, light bouncing off objects, and eye detection are connected",
        "Describe why complete darkness means complete invisibility"
    ],
    "vocabulary": [
        ("Light Source", "Anything that makes its own light — like the Sun, a lamp, or a phone screen"),
        ("Reflection", "When light bounces off an object — this is how we see most things around us"),
        ("Pupil", "The black opening in your eye that lets light in so you can see"),
        ("Absorb", "When an object takes in light instead of bouncing it back — dark objects absorb more light")
    ],
    "components": [
        ("Light Source Brightness", "How bright the light source is — brighter light means more light hits objects around you", True),
        ("Light Bouncing Off Objects", "How much light reflects off an object and travels toward your eyes", False),
        ("Eye Detection", "How well your eyes can pick up the reflected light and send signals to your brain", False)
    ],
    "think_about_it": "When light source brightness increases, what happens to the amount of light bouncing off objects? How does that affect eye detection?",
    "scenarios": [
        ("Pitch Black Room", "Set Light Source Brightness to zero and observe what your eyes can detect"),
        ("Bright Sunny Day", "Set Light Source Brightness to maximum and observe how much light bounces off objects"),
        ("Dim Flashlight", "Set Light Source Brightness to 20% and compare what you can see to the other scenarios")
    ],
    "sim_scenarios": [
        ("Pitch Black Room", "Light Source Brightness set to zero", "What do you predict will happen to Eye Detection when there is absolutely no light?"),
        ("Bright Sunny Day", "Light Source Brightness set to maximum", "What do you predict will happen to Light Bouncing Off Objects on a bright day?"),
        ("Dim Flashlight", "Light Source Brightness set to 20%", "Will you be able to see objects clearly with only a dim flashlight?")
    ],
    "discoveries": [
        "You can ONLY see an object when light bounces off it and enters your eyes — no light means no vision",
        "Light sources create light, but most objects just REFLECT light — they do not make their own",
        "Brighter light means more light bounces off objects, which means better eye detection",
        "Your eyes do not shoot out beams to see things — they RECEIVE light that comes in from outside"
    ],
    "answer": "You cannot see in the dark because seeing requires LIGHT! Here is how it works: a light source (like the Sun or a lamp) sends out light. That light hits objects and bounces off them (reflection). The reflected light enters your eyes through your pupils, hits the back of your eye, and your brain turns it into a picture. No light source = no reflection = nothing for your eyes to detect!",
    "stem_title": "Design a Light Maze",
    "stem_mission": "Design a maze where light must bounce off mirrors to reach a target, proving that we see objects because light reflects off them.",
    "stem_scenario": "A science museum wants an interactive exhibit that teaches visitors how light and vision work. Your engineering team must design a light maze where visitors use mirrors to bounce a flashlight beam through a maze to hit a target. The exhibit must prove that seeing requires light to bounce off objects.",
    "stem_questions": [
        "How many times can you bounce a flashlight beam off mirrors and still hit the target?",
        "What happens when light hits a dark surface vs. a shiny surface?",
        "How does your maze prove that we see objects because light bounces off them?"
    ],
    "stem_design_qs": [
        "How many mirrors will you need and where will you place them?",
        "What angle do the mirrors need to be at to bounce light in the right direction?",
        "What material will your target be made of so it is easy to see when light hits it?",
        "How will you block light from taking shortcuts through the maze?"
    ],
    "career": "Optical Engineers and Vision Scientists study how light behaves and design things like cameras, telescopes, eyeglasses, and laser systems. They earn $70,000–$120,000/year.",
    "images": {
        "cover": ("cover-lightvision.png", "A dramatic image of a beam of white light hitting a prism and splitting into a rainbow spectrum in a dark room, vibrant colors against black background, scientific and cinematic"),
        "landscape": ("landscape-lightvision.png", "A photorealistic image of diverse 4th grade students (9-10 years old, 70-80% Black and Brown children with realistic coils, curls, locs, and braids) experimenting with flashlights and mirrors in a dimmed classroom, beams of light visible, natural and dramatic lighting"),
        "modeling": ("modeling-lightvision.png", "A photorealistic image of diverse 4th grade students (9-10 years old, Black and Brown children centered with realistic hair detail) working together on laptops building a digital light and vision model, modern classroom with eye diagrams on the wall"),
        "discussion": ("discussion-lightvision.png", "A photorealistic image of a Black female teacher leading a discussion with diverse 4th graders (9-10 years old, Black and Brown children centered) about how we see, drawing a diagram on a whiteboard showing light going from a lamp to an object to an eye"),
        "stem": ("stem-lightvision.png", "A photorealistic image of diverse 4th grade students (9-10 years old, 70-80% Black and Brown children with coils, curls, locs, braids) building light mazes with small mirrors, flashlights, and cardboard walls on their desks, concentrated and having fun")
    },
    "pre_assessment": [
        "Why do you think you cannot see in a completely dark room?",
        "Do your eyes send something OUT to see things, or do they take something IN?",
        "Draw a picture showing how you think you see a book on a table.",
        "What is the difference between something that makes light and something that just reflects light?"
    ],
    "extend_components": [
        ("Object Color", "Different colors reflect different amounts of light — white reflects the most, black absorbs the most"),
        ("Object Distance", "How far away an object is — light spreads out over distance, making far-away objects dimmer"),
        ("Pupil Size", "Your pupil gets bigger in the dark to let in more light and smaller in bright light to protect your eye")
    ],
    "reflections": [
        "Why can you see the Moon at night even though it does not make its own light?",
        "If light did not bounce off objects, what would the world look like?",
        "Why is it easier to see a white shirt in the dark than a black shirt?",
        "How are your eyes similar to a camera?",
        "How did your model help you understand why darkness means invisibility?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how light source brightness, light reflection, and eye detection work together in the vision system."),
        ("Disciplinary Core Idea", "PS4.B Electromagnetic Radiation", "An object can be seen when light reflected from its surface enters the eyes. Objects can be seen only when light is available to illuminate them."),
        ("Crosscutting Concept", "Cause and Effect", "Students explore how the presence or absence of light (cause) directly determines whether objects can be seen (effect).")
    ],
    "cast_items": [
        "Explain why light must bounce off an object and enter the eye for us to see it",
        "Use a model to describe how brightness affects visibility",
        "Describe the path light takes from a source to an object to the eye"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student walks into a dark closet and cannot see anything, even though the closet is full of clothes. Which best explains why the student cannot see?"),
        ("Constructed Response:", "Explain how you are able to see this paper right now. Trace the path of light from where it starts to how it reaches your eyes. Use the words 'light source,' 'reflection,' and 'eye' in your answer.")
    ],
    "background_intro": "Light is the reason we can see the beautiful world around us. Without light, vision is impossible — no matter how good your eyes are. Understanding how light, objects, and eyes work together is one of the most important ideas in physical science.",
    "background_sections": [
        ("Light Sources vs. Reflectors", "There are two kinds of objects in the world: those that make their own light (luminous objects) and those that reflect light made by something else (illuminated objects). The Sun, light bulbs, phone screens, and fire are all light sources. Everything else — books, tables, people, the Moon — is visible only because light bounces off them. The Moon looks bright, but it is actually just reflecting sunlight!"),
        ("How Reflection Works", "When light hits an object, some of it bounces off (reflects), some passes through (transmits), and some is absorbed (turned into heat). Smooth, shiny surfaces like mirrors reflect light in an organized way — this is called specular reflection. Rough surfaces like paper scatter light in many directions — this is called diffuse reflection. Both types of reflection allow us to see objects, but mirrors create clear images while rough surfaces just look lit up."),
        ("How the Eye Works", "Light enters the eye through the cornea (clear front surface), passes through the pupil (the opening that controls how much light gets in), and is focused by the lens onto the retina at the back of the eye. The retina has millions of special cells called rods and cones that detect light and color. These cells send electrical signals through the optic nerve to the brain, which assembles the signals into the images you see."),
        ("Why Darkness Means Invisibility", "In complete darkness, there is no light to bounce off objects and enter your eyes. Your retina has nothing to detect, so no signals are sent to your brain. This is why you cannot see anything in a pitch-black room, no matter how long you wait. Your eyes need incoming light to create vision — they do not produce their own light to scan the room, despite what some ancient Greeks believed!")
    ],
    "lever_L": "Students identify light source brightness as an external component and light bouncing off objects and eye detection as internal components that respond to the amount of available light.",
    "lever_E": "Students determine that light source brightness positively affects light bouncing off objects, and more reflected light positively affects eye detection — a clear cause-and-effect chain.",
    "lever_V": "Students build a model showing how brighter light leads to more reflection, which leads to better vision, and how removing light eliminates vision entirely.",
    "lever_Ev": "Students run pitch black, dim flashlight, and bright sunny day scenarios to observe how changing brightness affects the whole vision system.",
    "lever_R": "Students add object color or pupil size to explore why some objects are easier to see than others.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with light beam and eye imagery", "say": "Close your eyes tight. What do you see? Nothing! Now open them. What changed? The same room was always there.", "do": "Have students close their eyes for 5 seconds, then open. Discuss: the room did not change, but your ability to see it did.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are going to solve the mystery of WHY darkness makes things invisible.", "do": "Have students read objectives aloud. Pre-teach 'reflection' by bouncing a flashlight off a mirror.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why can't you see in a pitch-black room?", "say": "Imagine a room full of your favorite things — toys, games, snacks — but it is completely dark. They are ALL there. Why can you not see a single one?", "do": "Have students turn and talk: What does your eye actually need to see something?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We are going to build a model of light and vision to figure this out.", "do": "Preview each LEVER step. Ask: Do you think your eyes send out something, or take something in?", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for light and vision model", "say": "What are the key parts of the seeing system? What has to happen for you to see a book?", "do": "Guide sorting. Explain that light source brightness is external because it comes from outside the vision system.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "When the light gets brighter, does MORE or LESS light bounce off the book? And what happens in your eye?", "do": "Help students draw positive arrows through the chain: brightness to reflection to eye detection.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let us test it! What happens when we take ALL the light away?", "do": "Students predict first. Run pitch black, dim, and bright scenarios. The pitch black result is the key 'aha' moment.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "Now you know — your eyes do not make light, they COLLECT light! No light means no vision.", "do": "Draw the full path on the board: light source to object to eye to brain. Emphasize that the eye is a receiver, not a sender.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Light maze design challenge", "say": "Time to become light engineers! Can you bounce light through a maze using mirrors?", "do": "Distribute materials (small mirrors, flashlights, cardboard). Groups build light mazes and guide a beam to a target.", "time": "12 min"}
    ],
    "sort_reasoning": "Light Source Brightness is external because it comes from outside the vision system — the Sun, a lamp, or a flashlight provides light independent of the object or the eye. Light Bouncing Off Objects and Eye Detection are internal because they are processes that happen within the system in response to how much light is available.",
    "relationships": [
        ("Light Source Brightness to Light Bouncing Off Objects", "POSITIVE (+)", "Brighter light means more light rays hit objects and more light bounces off them. On a sunny day, everything looks vivid because tons of light is reflecting everywhere."),
        ("Light Bouncing Off Objects to Eye Detection", "POSITIVE (+)", "More reflected light entering the eye means the retina detects a stronger signal. This is why objects are easy to see in bright light and hard to see in dim light — your eyes need reflected light to work.")
    ],
    "sim_answers": [
        ("Pitch Black Scenario", "When Light Source Brightness is set to zero, Light Bouncing Off Objects drops to zero and Eye Detection drops to zero. No light means nothing reflects, and nothing enters the eye. This proves that vision is 100% dependent on light — without it, even perfect eyes see nothing."),
        ("Bright Sunny Day Scenario", "When Light Source Brightness is at maximum, Light Bouncing Off Objects is very high and Eye Detection is excellent. Everything is clearly visible because plenty of light reflects off every surface and floods into the eyes. The model clearly shows why sunny days make everything easy to see.")
    ],
    "reflection_exemplars": [
        ("Why can you see the Moon at night?", "The Moon does not make its own light — it is just a big rock in space! You can see it because the Sun's light hits the Moon and bounces off its surface toward Earth. The reflected sunlight enters your eyes, and your brain sees a bright Moon. It is the same reason you can see a ball in a park — light from a source bounces off it to your eyes."),
        ("How are your eyes like a camera?", "Both eyes and cameras have an opening that lets light in (pupil vs. aperture), a lens that focuses the light, and a surface that captures the image (retina vs. sensor). Both need light to work — a camera in total darkness takes a black picture, just like your eyes see nothing in the dark. The biggest difference is that your brain processes the image instantly!")
    ],
    "stem_intro": "Present the challenge: A science museum wants an interactive exhibit about light and vision. Your team must design a light maze where visitors bounce a flashlight beam through walls using mirrors to hit a target — proving that we see things because light bounces off them.",
    "stem_concepts": [
        ("Reflection", "Light bounces off surfaces at predictable angles. A mirror reflects light very well, which is why mirrors can redirect a flashlight beam. Understanding reflection helps you aim the light through the maze."),
        ("Light Travels in Straight Lines", "Light always moves in a straight line until it hits something. In your maze, you must use mirrors to change the direction because light cannot go around corners by itself."),
        ("Absorption vs. Reflection", "Dark surfaces absorb light (take it in as heat) while light or shiny surfaces reflect it (bounce it back). Your maze walls should absorb light to block shortcuts, while mirrors should reflect it to guide the beam.")
    ],
    "stem_eval": [
        ("Expert (4)", "Light maze successfully bounces light to the target using multiple mirrors, student explains the path using reflection vocabulary and connects to the vision model"),
        ("Proficient (3)", "Light maze bounces light using mirrors and student can explain how reflection works"),
        ("Developing (2)", "Light maze uses mirrors but beam does not consistently reach the target, student partially explains reflection"),
        ("Beginning (1)", "Light maze is incomplete or student cannot explain how mirrors redirect light")
    ],
    "support": [
        "Provide a simple diagram showing light traveling from a source to an object to an eye in a straight path",
        "Use a flashlight in a slightly darkened room to physically demonstrate how light bounces off different objects",
        "Sentence frames: 'When the light source is brighter, I can see better because __'"
    ],
    "extensions": [
        "Research how animals that live in caves have evolved to not need eyes — what does this tell us about light and vision?",
        "Test which colors of paper reflect the most light using a flashlight and a light sensor app",
        "Design an experiment to prove that light travels in straight lines using cardboard with holes in a row"
    ],
    "cross_curr": [
        ("Math", "Measure the angle of incoming light and the angle of reflected light off a mirror — what pattern do you notice?"),
        ("ELA", "Write a short story about a world where there is no light — how would people survive? What senses would matter most?"),
        ("Art", "Create a drawing that shows the path of light from the Sun to an object to a person's eye, using arrows to trace the journey")
    ],
    "misconceptions": [
        ("Your eyes send out invisible beams to see things", "Your eyes do NOT send out anything. They are receivers, like a satellite dish. Light from a source hits an object, bounces off, and enters your eye. The eye collects incoming light — it does not project outgoing beams. Ancient Greeks called this the 'emission theory' and it is wrong!", "Shine a flashlight at a mirror — the light comes FROM the flashlight, bounces off the mirror, and goes TO your eye. Your eye just catches what comes in."),
        ("You can see in total darkness if you wait long enough", "No matter how long you wait, you cannot see in total darkness. Your eyes need light to function. In dim light, your pupils get bigger to collect more of the available light, which is why your eyes 'adjust' — but if there is truly ZERO light, there is nothing to adjust to.", "Put an object in a box with NO light leaks. No matter how long students look, they cannot see it. Then open a tiny hole to let light in — suddenly it is visible!"),
        ("The Moon makes its own light", "The Moon is a rocky object that does not produce any light at all. It appears bright because sunlight hits its surface and reflects toward Earth. During a lunar eclipse, when Earth blocks the sunlight from reaching the Moon, the Moon goes dark — proving it needs the Sun's light to be visible.", "Show photos of a lunar eclipse where the Moon goes dark. Ask: If the Moon made its own light, why would it go dark when Earth blocks the Sun?")
    ]
}

L04 = {
    "id": "G04-L04",
    "title": "Why Do Animals Have Superpowers?",
    "subtitle": "The Science of Body Structures and Survival",
    "ngss": "4-LS1-1",
    "ngss_desc": "Construct an argument that plants and animals have internal and external structures that function to support survival, growth, behavior, and reproduction.",
    "big_question": "How do animals survive in dangerous environments using just the body parts they were born with?",
    "objectives": [
        "Explain how different body structures help animals survive in their environments",
        "Model how body structure type, environment danger level, and survival rate are connected",
        "Describe how animals with better-matched structures survive at higher rates in dangerous environments"
    ],
    "vocabulary": [
        ("Structure", "A body part or feature that helps an animal do something important for survival"),
        ("Function", "The job that a body structure does — like how wings help a bird fly"),
        ("External Structure", "A body part on the outside of an animal, like claws, fur, beaks, or shells"),
        ("Internal Structure", "A body part on the inside of an animal, like bones, lungs, or a heart")
    ],
    "components": [
        ("Body Structure Type", "The kind of survival features an animal has — thick fur, sharp claws, camouflage, hard shell, etc.", True),
        ("Environment Danger Level", "How many threats exist in the habitat — predators, extreme weather, food scarcity, etc.", True),
        ("Survival Rate", "How likely an animal is to survive based on how well its structures match its environment's dangers", False)
    ],
    "think_about_it": "When an animal has a body structure that matches its environment's dangers, what happens to its survival rate? What if the dangers change?",
    "scenarios": [
        ("Perfect Match", "Set Body Structure Type to thick fur and Environment Danger Level to arctic cold — observe Survival Rate"),
        ("Mismatch", "Set Body Structure Type to thick fur but Environment Danger Level to desert heat — observe what happens"),
        ("High Danger", "Lock Environment Danger Level to maximum and compare different body structures")
    ],
    "sim_scenarios": [
        ("Perfect Match", "Thick fur in arctic cold", "What do you predict will happen to Survival Rate when an animal's body perfectly matches its environment?"),
        ("Mismatch", "Thick fur in desert heat", "What do you predict will happen when an animal's body does NOT match its environment?"),
        ("High Danger", "Maximum danger, comparing structures", "Which body structure type do you predict will survive best in a very dangerous environment?")
    ],
    "discoveries": [
        "Animals with body structures that match their environment's dangers have much higher survival rates",
        "The same body structure can be helpful in one environment but harmful in another",
        "Both external structures (claws, shells, fur) and internal structures (strong bones, efficient lungs) are critical for survival",
        "Animals in more dangerous environments tend to have more specialized survival structures"
    ],
    "answer": "Animals have 'superpowers' because their body structures are perfectly designed for the dangers in their environment! A polar bear's thick fur is a superpower in the Arctic but would be terrible in a desert. An armadillo's armor is perfect for protection against predators. These structures evolved over millions of years — animals with the best body parts for their environment survived and passed those features to their babies!",
    "stem_title": "Design a Survival Animal",
    "stem_mission": "Design an imaginary animal with the perfect body structures to survive in a specific extreme environment using evidence from your model.",
    "stem_scenario": "A nature documentary team is filming in an extreme environment. They have hired your team to predict what kind of animal could survive there based on the dangers present. Design an animal with body structures that perfectly match the environment's challenges.",
    "stem_questions": [
        "What are the biggest dangers in your chosen environment?",
        "What body structures (both external and internal) would help your animal survive each danger?",
        "How does your animal's design compare to real animals that live in similar environments?"
    ],
    "stem_design_qs": [
        "What extreme environment will your animal live in (desert, deep ocean, arctic, jungle canopy)?",
        "What external structures will it have (fur, claws, wings, camouflage, armor)?",
        "What internal structures will help it survive (strong bones, large lungs, fast muscles)?",
        "How will you show that each structure matches a specific danger in the environment?"
    ],
    "career": "Wildlife Biologists and Zoologists study how animals survive in the wild and work to protect endangered species and their habitats. They earn $50,000–$85,000/year.",
    "images": {
        "cover": ("cover-animalstructures.png", "A dramatic, cinematic close-up of a chameleon changing colors on a branch in a tropical rainforest, vivid green and brown tones, incredible detail showing the textured skin and swiveling eye, nature photography style"),
        "landscape": ("landscape-animalstructures.png", "A photorealistic image of diverse 4th grade students (9-10 years old, 70-80% Black and Brown children with realistic coils, curls, locs, and braids) examining animal models, skulls, and shells at a science station in a bright classroom, engaged and curious"),
        "modeling": ("modeling-animalstructures.png", "A photorealistic image of diverse 4th grade students (9-10 years old, Black and Brown children centered with realistic hair detail) working together on laptops building a digital animal survival model, modern classroom with animal posters on the wall"),
        "discussion": ("discussion-animalstructures.png", "A photorealistic image of a Black male teacher leading a discussion with diverse 4th graders (9-10 years old, Black and Brown children centered) about animal adaptations, pointing at images of different animals on a smartboard, students eagerly raising hands"),
        "stem": ("stem-animalstructures.png", "A photorealistic image of diverse 4th grade students (9-10 years old, 70-80% Black and Brown children with coils, curls, locs, braids) drawing and building model animals from clay and craft materials, designing imaginary creatures at their desks")
    },
    "pre_assessment": [
        "What animal do you think has the coolest 'superpower'? What does it do?",
        "Why do you think polar bears have thick fur but lizards do not?",
        "Draw an animal and label the body parts that help it survive.",
        "What do you think would happen if you put a fish on dry land?"
    ],
    "extend_components": [
        ("Food Availability", "How much food is available in the environment — animals need structures to find and eat the right food"),
        ("Predator Speed", "How fast the predators in the environment can move — prey need escape structures to survive"),
        ("Temperature Extreme", "How hot or cold the environment gets — animals need temperature-regulation structures to survive")
    ],
    "reflections": [
        "Why would thick fur be a superpower in the Arctic but a problem in the desert?",
        "Can you think of a human-made invention that copies an animal's survival structure?",
        "What body structures do YOU have that help you survive?",
        "Why do animals in the same environment often have similar body features?",
        "How did your model help you understand why animals look the way they do?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how body structure type and environment danger level interact to determine survival rate."),
        ("Disciplinary Core Idea", "LS1.A Structure and Function", "Plants and animals have both internal and external structures that serve various functions in growth, survival, behavior, and reproduction."),
        ("Crosscutting Concept", "Structure and Function", "Students explore how the structure (shape, form, material) of an animal's body parts directly relates to their function (what job they do for survival).")
    ],
    "cast_items": [
        "Explain how a specific body structure helps an animal survive in its environment",
        "Use a model to show the relationship between body structures, environmental dangers, and survival",
        "Compare how the same structure can help in one environment but hurt in another"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A scientist observes that desert foxes have very large ears while arctic foxes have very small ears. Which best explains this difference?"),
        ("Constructed Response:", "Choose an animal and describe two body structures (one external and one internal) that help it survive. Explain how each structure's shape or design helps it do its job.")
    ],
    "background_intro": "Every animal on Earth is equipped with an amazing set of body structures — both inside and outside — that help it survive, find food, avoid danger, and raise its young. These structures are like built-in tools that have been perfected over millions of years of evolution.",
    "background_sections": [
        ("External Structures", "External structures are body parts on the outside that you can see. Examples include a bird's beak (shaped for the type of food it eats), a turtle's shell (armor against predators), a polar bear's thick fur (insulation against cold), a chameleon's color-changing skin (camouflage from predators), and a cheetah's long legs (speed for catching prey). Each structure's shape and design matches the specific job it needs to do."),
        ("Internal Structures", "Internal structures are body parts inside the animal that you cannot see. A bird's hollow bones make it light enough to fly. A whale's enormous lungs let it hold its breath for over an hour while diving. A snake's flexible spine lets it squeeze through tight spaces. An eagle's sharp-focused eyes (with internal structures for magnification) let it spot a mouse from a mile away."),
        ("Structure Matches Environment", "The key idea is that an animal's structures match the challenges of its environment. Desert animals have structures for conserving water and staying cool. Arctic animals have structures for staying warm and walking on ice. Forest animals have structures for climbing and hiding among trees. When the environment changes faster than animals can adapt, species can become endangered or extinct."),
        ("Biomimicry — Copying Nature's Designs", "Engineers often study animal structures to inspire human inventions. Velcro was inspired by burrs that stick to animal fur. Bullet trains were redesigned after the kingfisher's beak to reduce noise. Shark skin patterns inspired swimsuits that reduce drag. This field is called biomimicry — 'bio' means life and 'mimicry' means copying. Animals have been solving engineering problems for millions of years!")
    ],
    "lever_L": "Students identify body structure type and environment danger level as external components and survival rate as an internal component that responds to how well structures match dangers.",
    "lever_E": "Students determine that better structure-environment matches positively affect survival rate, and that mismatches reduce survival rate.",
    "lever_V": "Students build a model showing how different structure types perform differently depending on the environment's danger profile.",
    "lever_Ev": "Students run perfect match, mismatch, and high danger scenarios to observe how the relationship between structure and environment determines survival.",
    "lever_R": "Students add food availability or predator speed to explore more complex survival challenges.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with amazing animal imagery", "say": "If you could have any animal's superpower, what would it be? A cheetah's speed? An eagle's eyesight? A chameleon's camouflage?", "do": "Let students share their animal superpower picks. Then reveal: those are not superpowers — they are STRUCTURES.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are going to discover why animals have the amazing body features they do.", "do": "Have students read objectives aloud. Pre-teach 'structure' and 'function' using a pencil as an example (structure = shape, function = writing).", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How do animals survive using just the body parts they were born with?", "say": "Animals do not have backpacks, houses, or jackets. They survive using ONLY their body. How is that possible in dangerous environments?", "do": "Show images of extreme environments and ask: What would an animal NEED to survive here?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We are going to build a model to figure out why certain animals survive where others would not.", "do": "Preview LEVER steps. Remind students that models help us test ideas without going to dangerous places.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for animal survival model", "say": "What determines whether an animal survives? Think about the animal AND its environment.", "do": "Guide sorting. Explain that both body structure type and environment danger level are external — they are set before the model runs.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "When an animal's body matches its environment's dangers, survival goes UP. But what if there is a mismatch?", "do": "Help students draw arrows. Discuss how the same structure can help or hurt depending on the environment.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let us test it! What happens when we put a thick-furred animal in the desert?", "do": "Students predict first, then run scenarios. The mismatch scenario is the most surprising result.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "Every animal superpower is actually a survival structure that MATCHES its environment!", "do": "Show real examples: polar bear fur, cactus spines, eagle talons. Ask students to identify the structure and its function.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Design-a-survival-animal challenge", "say": "Now YOU are nature's engineers! Design the perfect animal for an extreme environment.", "do": "Assign or let groups choose extreme environments. Groups design and draw animals with labeled survival structures.", "time": "12 min"}
    ],
    "sort_reasoning": "Body Structure Type and Environment Danger Level are both external because they exist before the model runs — the animal already has its structures and the environment already has its dangers. Survival Rate is internal because it is the OUTCOME that results from how well the external components interact with each other.",
    "relationships": [
        ("Body Structure Type to Survival Rate", "POSITIVE (+) when matched", "When an animal's body structures match the dangers in its environment (like thick fur in the cold), survival rate is high. The better the match between structure and environment, the more likely the animal is to survive and thrive."),
        ("Environment Danger Level to Survival Rate", "NEGATIVE (-)", "More dangers in the environment make it harder for all animals to survive. Higher danger means lower survival rate unless the animal has structures that specifically counter those dangers.")
    ],
    "sim_answers": [
        ("Perfect Match Scenario", "When Body Structure Type is set to thick fur and Environment Danger Level is set to arctic cold, Survival Rate is very high. The thick fur provides excellent insulation, keeping the animal warm despite freezing temperatures. The structure perfectly matches the environmental challenge."),
        ("Mismatch Scenario", "When Body Structure Type is set to thick fur but Environment Danger Level is desert heat, Survival Rate drops dramatically. The thick fur that was a superpower in the cold becomes a deadly problem in the heat — the animal cannot cool down. This proves that the SAME structure can help or hurt depending on the environment.")
    ],
    "reflection_exemplars": [
        ("Why would thick fur be a problem in the desert?", "Thick fur is designed to trap heat close to the body — it is like wearing a winter coat. In the Arctic, trapping heat is exactly what you need to survive the freezing cold. But in the desert, the problem is the opposite — it is TOO hot. Thick fur would trap body heat and prevent the animal from cooling down, causing it to overheat. The same structure that saves a life in one place could end a life in another!"),
        ("What body structures do YOU have that help you survive?", "Humans have many survival structures! Our skin protects us from germs and holds water in. Our bones support our body and protect organs like the brain (skull) and heart (rib cage). Our eyes help us see danger. Our fingers can grip tools. Our sweat glands cool us down when we are hot. We even have tiny hairs in our noses that filter out dust and dirt from the air we breathe!")
    ],
    "stem_intro": "Present the challenge: A nature documentary team is filming in an extreme environment and needs your team to predict what kind of animal could survive there. Design an imaginary animal with body structures that perfectly match the environment's dangers. Every structure must have a survival purpose!",
    "stem_concepts": [
        ("Structure and Function", "Every body structure has a specific job (function). The shape, material, and design of the structure are perfectly matched to that job. When designing your animal, every feature should solve a specific survival problem."),
        ("Environment Matching", "The best survival structures are ones that directly address the most dangerous challenges in the environment. A desert animal needs structures for heat, water conservation, and sand. An ocean animal needs structures for swimming, breathing underwater, and pressure."),
        ("Biomimicry", "Engineers study animal structures to create human inventions. Your animal design might inspire real engineering solutions! Think about what humans could learn from your animal's survival features.")
    ],
    "stem_eval": [
        ("Expert (4)", "Animal design includes both external and internal structures, each labeled with its function, and student explains survival rate using model evidence"),
        ("Proficient (3)", "Animal has 3+ labeled structures that match the environment and student can explain how they help survival"),
        ("Developing (2)", "Animal has some structures but not all are clearly connected to environmental dangers"),
        ("Beginning (1)", "Animal design is incomplete or structures do not logically match the chosen environment")
    ],
    "support": [
        "Provide photo cards of real animal structures with descriptions of what they do",
        "Give students a graphic organizer with columns: Environment Danger | Structure Needed | What It Does",
        "Sentence frames: 'My animal has __ because in this environment, the danger is __ and this structure helps by __'"
    ],
    "extensions": [
        "Research a real animal that went extinct because its environment changed faster than it could adapt",
        "Compare two animals from the same environment and find three structures they share — why do they have similar features?",
        "Design an invention inspired by an animal structure (biomimicry) that could help people solve a problem"
    ],
    "cross_curr": [
        ("Math", "Create a bar graph comparing survival rates of different animals in the same environment based on how many matching structures they have"),
        ("ELA", "Write a nature documentary script describing your designed animal and how its structures help it survive"),
        ("Art", "Create a detailed, labeled illustration of your survival animal showing both external and internal structures with color coding")
    ],
    "misconceptions": [
        ("Animals choose to grow the structures they need", "Animals cannot choose their body structures — they are born with them based on their genes from their parents. Over millions of years, animals with better-matched structures survived more often and had more babies, passing those useful features to the next generation. This is called natural selection.", "Ask: Can you choose to grow claws or wings? No! You were born with the structures your parents' genes gave you. Animals work the same way."),
        ("All animals in the same environment look the same", "Animals in the same environment can have VERY different structures that solve the same problem in different ways. In the Arctic, polar bears have thick fur for warmth while walruses have thick blubber. Both stay warm, but the structure is totally different.", "Show images of multiple animals from the same environment and compare their different strategies for solving the same survival challenge."),
        ("Body structures are only on the outside", "Many of the most important survival structures are INSIDE the animal where you cannot see them. A bird's hollow bones let it fly. A whale's giant lungs let it dive for hours. A snake's flexible spine lets it squeeze through tight spaces. Both internal AND external structures are essential for survival.", "Have students list structures they can see (fur, claws, shells) AND structures they cannot see (bones, lungs, muscles) to show that both types matter equally.")
    ]
}

L05 = {
    "id": "G04-L05",
    "title": "How Does Your Brain Know That's Hot?",
    "subtitle": "The Lightning-Fast Science of Senses and Signals",
    "ngss": "4-LS1-2",
    "ngss_desc": "Use a model to describe that animals receive different types of information through their senses, process the information in their brain, and respond to the information in different ways.",
    "big_question": "When you touch a hot stove, your hand pulls back before you even think about it — how does your body react SO fast?",
    "objectives": [
        "Explain how your senses detect information from the environment and send signals to the brain",
        "Model how heat source intensity, nerve signal speed, and brain response time are connected",
        "Describe how the nervous system helps animals respond quickly to danger"
    ],
    "vocabulary": [
        ("Nerve", "A thin fiber in your body that carries electrical signals between your brain and other body parts"),
        ("Sensory Receptor", "A special cell in your skin, eyes, ears, nose, or tongue that detects information from the environment"),
        ("Signal", "An electrical message that travels along nerves from your senses to your brain and back to your muscles"),
        ("Response", "What your body does after your brain gets the signal — like pulling your hand away from something hot")
    ],
    "components": [
        ("Heat Source Intensity", "How hot the object is — hotter objects are more dangerous and trigger stronger signals", True),
        ("Nerve Signal Speed", "How fast the electrical message travels from your skin to your brain through your nerves", False),
        ("Brain Response Time", "How quickly your brain processes the danger signal and tells your muscles to react", False)
    ],
    "think_about_it": "When heat source intensity increases, what happens to nerve signal speed? Does your brain respond faster or slower when the danger is greater?",
    "scenarios": [
        ("Warm Cup", "Set Heat Source Intensity to low and observe how fast your body responds"),
        ("Hot Stove", "Set Heat Source Intensity to high and observe how Nerve Signal Speed and Brain Response Time change"),
        ("Boiling Water", "Set Heat Source Intensity to maximum and compare reaction speed to the other scenarios")
    ],
    "sim_scenarios": [
        ("Warm Cup", "Heat Source Intensity set to low", "What do you predict will happen to Brain Response Time when you touch something just warm?"),
        ("Hot Stove", "Heat Source Intensity set to high", "What do you predict will happen to Nerve Signal Speed when you touch something very hot?"),
        ("Boiling Water", "Heat Source Intensity set to maximum", "Will your body respond even faster when the danger is extreme? Why?")
    ],
    "discoveries": [
        "Your body has special sensor cells in your skin that detect heat, cold, pressure, and pain",
        "Nerve signals travel like electricity through wires — they can move over 100 meters per second through your body",
        "Stronger dangers (hotter objects) trigger faster, stronger nerve signals because your body treats it as an emergency",
        "Some responses (like pulling your hand from a hot stove) happen so fast that the signal does not even reach your brain first — it is called a reflex"
    ],
    "answer": "Your body has an incredible alarm system! When you touch something hot, sensory receptors in your skin instantly detect the heat and fire electrical signals through your nerves at incredible speed. For extreme danger, your spinal cord can trigger a REFLEX — pulling your hand back even before the signal reaches your brain! Then your brain processes the signal and you feel the pain. It all happens in a fraction of a second because your nervous system is built for speed and survival!",
    "stem_title": "Design a Human Alarm System",
    "stem_mission": "Design a model of a body alarm system that detects a danger signal, sends it quickly, and triggers a response — just like your nervous system.",
    "stem_scenario": "A children's hospital needs a teaching model to help young patients understand how their nervous system works. Your team must design a hands-on model that shows how a signal travels from a sensor to the brain and triggers a response. The faster the signal, the better!",
    "stem_questions": [
        "What will represent the sensor that detects danger in your model?",
        "How will you show the signal traveling along the nerve to the brain?",
        "How will you demonstrate the response (the body reacting to the signal)?"
    ],
    "stem_design_qs": [
        "What material will represent nerves carrying the signal (string, dominoes, tubes)?",
        "How will you show the speed difference between a weak signal and a strong danger signal?",
        "What will represent the brain making a decision?",
        "How will you show the response (muscles moving) at the end of the chain?"
    ],
    "career": "Neuroscientists and Neurologists study how the brain and nervous system work, helping people with brain injuries, nerve disorders, and sensory problems. They earn $80,000–$150,000/year.",
    "images": {
        "cover": ("cover-nervoussystem.png", "A stunning, colorful scientific visualization of electrical nerve signals traveling through neurons with glowing synapses and branching pathways, neon blue and purple on a dark background, dramatic and futuristic"),
        "landscape": ("landscape-nervoussystem.png", "A photorealistic image of diverse 4th grade students (9-10 years old, 70-80% Black and Brown children with realistic coils, curls, locs, and braids) testing their reflexes by catching falling rulers in a bright modern classroom, laughing and engaged, natural window light"),
        "modeling": ("modeling-nervoussystem.png", "A photorealistic image of diverse 4th grade students (9-10 years old, Black and Brown children centered with realistic hair detail) working together on laptops building a digital nervous system model, modern classroom with brain and nerve diagrams on the wall"),
        "discussion": ("discussion-nervoussystem.png", "A photorealistic image of a Black female teacher leading an animated discussion with diverse 4th graders (9-10 years old, Black and Brown children centered) about how the brain receives signals, pointing at a diagram of the nervous system on a smartboard"),
        "stem": ("stem-nervoussystem.png", "A photorealistic image of diverse 4th grade students (9-10 years old, 70-80% Black and Brown children with coils, curls, locs, braids) building model alarm systems with dominoes, string, and bells to represent nerve signals, enthusiastic group work at tables")
    },
    "pre_assessment": [
        "How do you think your body knows when something is hot or cold?",
        "Why do you pull your hand away from something hot before you even think about it?",
        "Draw a picture showing how a message might travel from your finger to your brain.",
        "What are your five senses and what does each one detect?"
    ],
    "extend_components": [
        ("Pain Level", "How much pain the sensation causes — more pain triggers faster and stronger responses"),
        ("Nerve Pathway Length", "How far the signal has to travel — signals from your toes take longer to reach your brain than signals from your face"),
        ("Attention Level", "Whether you are paying attention — your brain can process signals faster when you are focused and alert")
    ],
    "reflections": [
        "Why does your body pull away from hot things even before you feel the pain?",
        "What would happen if your nerves could not send signals to your brain?",
        "Why do you think your reflexes are faster than your thinking?",
        "How are nerves in your body similar to electrical wires in a building?",
        "How did your model help you understand something happening inside your body that you cannot see?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how heat source intensity, nerve signal speed, and brain response time work together in the nervous system."),
        ("Disciplinary Core Idea", "LS1.D Information Processing", "Different sense receptors are specialized for particular kinds of information; animals use their perceptions and memories to guide their actions."),
        ("Crosscutting Concept", "Cause and Effect", "Students explore how the intensity of a stimulus (cause) affects the speed and strength of the nervous system's response (effect).")
    ],
    "cast_items": [
        "Explain how sensory receptors detect information and send signals through nerves to the brain",
        "Use a model to describe the relationship between danger intensity and response speed",
        "Describe how the nervous system helps animals survive by responding quickly to danger"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student accidentally touches a hot pan and pulls their hand back instantly, even before feeling pain. Which best explains why the hand moved before the brain processed the pain?"),
        ("Constructed Response:", "Describe the journey of a signal from when your finger touches a hot object to when your hand pulls away. Use the words 'sensory receptor,' 'nerve,' 'signal,' and 'response' in your answer.")
    ],
    "background_intro": "Your nervous system is the most incredible communication network on Earth. It connects every part of your body to your brain, allowing you to sense the world, make decisions, and react to danger in fractions of a second. Understanding how signals travel through your body helps explain everything from reflexes to memory.",
    "background_sections": [
        ("Sensory Receptors", "Your body has millions of sensory receptors — specialized cells that detect specific types of information. Thermoreceptors in your skin detect temperature (hot and cold). Mechanoreceptors detect pressure and touch. Nociceptors detect pain. Photoreceptors in your eyes detect light. Chemoreceptors in your nose and tongue detect chemicals (smell and taste). Each type converts its specific stimulus into an electrical signal."),
        ("How Nerve Signals Travel", "When a sensory receptor is activated, it generates an electrical signal called a nerve impulse. This impulse travels along nerve fibers (neurons) at speeds up to 120 meters per second — that is 270 miles per hour! The signal passes from one neuron to the next through tiny gaps called synapses. Signals from your finger can reach your brain in about 20 milliseconds."),
        ("Reflexes — The Shortcut", "For extreme dangers like touching a hot stove, your body has a shortcut called a reflex arc. Instead of waiting for the signal to travel all the way to the brain and back, the signal goes only to the spinal cord, which immediately sends a response signal back to the muscles to MOVE. Your hand pulls away in about 50 milliseconds — before your brain even registers pain! This reflex system evolved because those fractions of a second can prevent serious injury."),
        ("The Brain — Mission Control", "The brain is the command center of the nervous system. It receives signals from all sensory receptors, processes the information, stores memories, makes decisions, and sends signals back out to muscles and organs. The brain processes about 11 million bits of sensory information every second, but you are only aware of about 50 bits at a time. Most processing happens automatically without you thinking about it!")
    ],
    "lever_L": "Students identify heat source intensity as an external component and nerve signal speed and brain response time as internal components that respond to the intensity of the stimulus.",
    "lever_E": "Students determine that heat source intensity positively affects nerve signal speed (hotter objects trigger faster signals), and faster nerve signals positively reduce brain response time.",
    "lever_V": "Students build a model showing how more intense heat triggers faster nerve signals and quicker brain responses, creating a survival system that reacts faster to greater danger.",
    "lever_Ev": "Students run warm cup, hot stove, and boiling water scenarios to observe how increasing heat intensity affects signal speed and response time.",
    "lever_R": "Students add pain level or nerve pathway length to explore why some body parts are more sensitive than others.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with nerve signal imagery", "say": "Quick — clap your hands! How did your brain tell your hands to do that so fast? The signal traveled at over 200 miles per hour!", "do": "Have students clap, then ask: How did the message get from your brain to your hands? Could you feel it traveling?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are going to discover the incredible alarm system hidden inside your body.", "do": "Have students read objectives aloud. Pre-teach 'nerve' and 'signal' by comparing nerves to electrical wires.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How does your body react so fast to danger?", "say": "Have you ever touched something really hot and your hand flew away on its own? You did not even think about it! How is that possible?", "do": "Have students share stories of fast reflexes. Then ask: How does the message get from your finger to your muscles?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We are going to build a model of your body's alarm system to understand how you react to danger.", "do": "Preview LEVER steps. Explain that we are modeling something invisible happening inside their bodies.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for nervous system model", "say": "What are the key parts of your body's danger detection system?", "do": "Guide sorting. Explain that heat source intensity is external because it comes from outside the body. Signal speed and response time are internal.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "When the heat is more intense, do you think the signal goes FASTER or SLOWER? Why would that help you survive?", "do": "Help students draw positive arrows. Discuss why faster signals for bigger dangers makes sense for survival.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let us test it! We will compare touching a warm cup vs. a hot stove vs. boiling water.", "do": "Students predict first. Run all three scenarios. The speed difference should surprise them!", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "Your body is like a superhero — it reacts to danger even faster than you can think!", "do": "Demonstrate the ruler-drop reflex test. Students test each other's reaction times and connect results to the model.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Human alarm system design challenge", "say": "Can you build a model that works like your nervous system? Detect, send, respond!", "do": "Distribute materials (dominoes, string, bells, cups). Groups build alarm systems that detect a 'signal' and trigger a 'response.'", "time": "12 min"}
    ],
    "sort_reasoning": "Heat Source Intensity is external because it comes from the environment outside the body — the hot object exists whether or not the body is there. Nerve Signal Speed and Brain Response Time are internal because they are processes that happen INSIDE the nervous system in response to the external stimulus.",
    "relationships": [
        ("Heat Source Intensity to Nerve Signal Speed", "POSITIVE (+)", "A hotter, more dangerous stimulus triggers a stronger, faster nerve signal. Your body treats higher intensity as a bigger emergency, sending the alarm faster to protect you from injury."),
        ("Nerve Signal Speed to Brain Response Time", "POSITIVE (+)", "Faster nerve signals mean the brain (or spinal cord for reflexes) receives the information sooner and can trigger a response more quickly. Speed is survival — the faster the signal, the faster you react.")
    ],
    "sim_answers": [
        ("Warm Cup Scenario", "When Heat Source Intensity is set to low (a warm cup), Nerve Signal Speed is moderate and Brain Response Time is relaxed. Your body detects the warmth but does not treat it as an emergency. You feel the warmth and can casually decide to hold or set down the cup."),
        ("Hot Stove Scenario", "When Heat Source Intensity is set to high (a hot stove), Nerve Signal Speed jumps dramatically and Brain Response Time becomes nearly instant. Your body detects serious danger and fires an emergency signal. For extreme heat, the reflex arc bypasses the brain entirely — your spinal cord triggers muscle movement before you even feel pain!")
    ],
    "reflection_exemplars": [
        ("Why does your hand pull back before you feel pain?", "Your body has a survival shortcut called a reflex arc. When sensory receptors detect extreme heat, they send a signal to the spinal cord. Instead of waiting for the signal to travel all the way up to the brain (which takes time), the spinal cord sends a response signal immediately to the muscles in your arm: PULL BACK! Your hand moves in about 50 milliseconds. The pain signal reaches your brain a moment later — that is why you pull away FIRST and feel the ouch SECOND."),
        ("How are nerves similar to electrical wires?", "Nerves and electrical wires both carry signals using electricity. Just like wires have insulation (plastic coating) to keep the signal from leaking out, nerves have a coating called myelin that keeps the signal strong and fast. Both carry messages from one place to another. The big difference is that nerves are alive and can heal themselves, while wires cannot. Also, nerve signals are much slower than electricity in a wire, but they are still incredibly fast for a biological system!")
    ],
    "stem_intro": "Present the challenge: A children's hospital needs a teaching model to help young patients understand how their nervous system works. Your team must design a hands-on alarm system that shows how a danger signal is detected, travels quickly through the body, and triggers a response. Make it as fast as possible!",
    "stem_concepts": [
        ("Signal Detection", "Your body has sensory receptors that detect specific things: thermoreceptors for temperature, mechanoreceptors for touch, nociceptors for pain. Your alarm system needs a 'detector' that senses the danger."),
        ("Signal Transmission", "Nerve impulses travel along neurons at high speed, passing from cell to cell. Your alarm system needs a way to move the signal from the detector to the 'brain' quickly."),
        ("Response Trigger", "Once the brain (or spinal cord) receives the signal, it sends a command to muscles to respond. Your alarm system needs an output — something that moves or makes noise when the signal arrives.")
    ],
    "stem_eval": [
        ("Expert (4)", "Alarm system clearly shows detection, transmission, and response stages, student explains each stage using nervous system vocabulary and connects to model evidence"),
        ("Proficient (3)", "Alarm system shows a signal traveling from sensor to response and student can explain the connection to the nervous system"),
        ("Developing (2)", "Alarm system demonstrates a chain reaction but student struggles to connect it to how the nervous system works"),
        ("Beginning (1)", "Alarm system is incomplete or does not show a clear signal path from detection to response")
    ],
    "support": [
        "Provide a simple diagram showing the path: sensory receptor sends signal through nerve to brain, brain sends signal to muscle",
        "Use the ruler-drop reflex test to give students a physical experience of reaction time",
        "Sentence frames: 'When the heat is more intense, the nerve signal is __ because __'"
    ],
    "extensions": [
        "Research how animals like pit vipers can detect heat with special sensors on their faces — what could humans learn from this?",
        "Test your reaction time with an online reaction timer and compare different senses — is seeing or hearing faster?",
        "Investigate why doctors tap your knee with a rubber hammer during checkups — what does this test about your nervous system?"
    ],
    "cross_curr": [
        ("Math", "Measure and compare reaction times using the ruler-drop test, calculate averages, and create a class data chart"),
        ("ELA", "Write a first-person narrative from the perspective of a nerve signal traveling from a burned finger to the brain"),
        ("Health", "Research how wearing protective gear (helmets, gloves) helps protect the nervous system from damage during sports and activities")
    ],
    "misconceptions": [
        ("Your brain controls every single movement you make", "Many fast responses (reflexes) bypass the brain entirely! When you touch something dangerously hot, the signal goes to your spinal cord, which triggers the muscle response immediately. Your brain finds out about the pain AFTER your hand has already moved. This reflex system exists because waiting for the brain would be too slow for extreme dangers.", "Do the ruler-drop test: your hand catches the ruler before your brain 'decides' to — that is a reflex, not a conscious choice."),
        ("Nerves only send signals about pain", "Nerves carry ALL kinds of sensory information — not just pain! They send signals about temperature, pressure, texture, position, balance, sound, light, smell, and taste. You feel the softness of a pillow, the coldness of ice cream, and the tickle of a feather all through nerve signals. Pain is just one of many types of information nerves carry.", "Have students close their eyes and identify objects by touch alone. Ask: How does your brain know what you are touching without seeing it? That is your nerves sending detailed information!"),
        ("Signals travel instantly — there is no delay", "Nerve signals are fast but NOT instant. They travel at 1 to 120 meters per second depending on the nerve type. A signal from your toe to your brain takes about 60 milliseconds. That is why you can sometimes feel a stubbed toe in stages — you see it happen, then feel the pressure, THEN feel the pain. Each signal type travels at a different speed!", "Have a student stand at one end of the room. Touch their foot and time how long until they react. Then touch their shoulder and compare — the shoulder reaction is slightly faster because the signal has less distance to travel.")
    ]
}

L06 = {
    "id": "G04-L06",
    "title": "Why Are There Seashells on Mountains?",
    "subtitle": "The Mystery of Fossils Found in Surprising Places",
    "ngss": "4-ESS1-1",
    "ngss_desc": "Identify evidence from patterns in rock formations and fossils in rock layers to support an explanation for changes in a landscape over time.",
    "big_question": "How did seashells and ocean fossils end up on top of a mountain thousands of feet above the sea?",
    "objectives": [
        "Explain how sediment layers build up over time and trap living things as fossils",
        "Model how sediment buildup and Earth movement work together to expose fossils on mountains",
        "Use fossil evidence to describe how a landscape has changed over millions of years"
    ],
    "vocabulary": [
        ("Fossil", "The preserved remains or trace of a living thing from long ago, found in rock"),
        ("Sediment", "Tiny pieces of rock, sand, mud, and shells that settle in layers over time"),
        ("Rock Layer", "A horizontal band of rock formed when sediment was pressed and hardened over millions of years"),
        ("Erosion", "The wearing away of rock and soil by water, wind, or ice that can reveal hidden fossils")
    ],
    "components": [
        ("Sediment Buildup", "Layers of sand, mud, and shells that pile up on ocean floors and lake bottoms over time", True),
        ("Earth Movement Speed", "How fast the ground pushes upward when tectonic forces squeeze and lift rock layers", True),
        ("Fossil Exposure", "How many fossils become visible at the surface as layers are lifted and worn away", False)
    ],
    "think_about_it": "When more sediment builds up, does that create more or fewer fossils? When Earth movement pushes layers higher, what happens to fossil exposure?",
    "scenarios": [
        ("Ocean Floor", "Set Sediment Buildup to high and Earth Movement Speed to 0 — observe what happens"),
        ("Mountain Building", "Lock Earth Movement Speed to high and observe how fossils become exposed"),
        ("Erosion Reveal", "Set both Sediment Buildup and Earth Movement Speed to moderate levels")
    ],
    "sim_scenarios": [
        ("Ocean Floor", "High sediment, no Earth movement", "What do you predict will happen to Fossil Exposure when layers just keep piling up underwater?"),
        ("Mountain Building", "Earth Movement Speed set to high", "What do you predict will happen to Fossil Exposure as the ground pushes upward?"),
        ("Erosion Reveal", "Moderate sediment and moderate movement", "How do you think sediment buildup and Earth movement work together to expose fossils?")
    ],
    "discoveries": [
        "Fossils form when living things get buried in sediment layers on ocean floors or lake bottoms",
        "Earth movement slowly pushes ocean floor rock layers upward over millions of years, creating mountains",
        "Once rock layers are lifted high, wind and rain wear away the surface, exposing ancient fossils",
        "Finding ocean fossils on a mountain is proof that the land was once underwater"
    ],
    "answer": "Seashells ended up on mountains because those mountains used to be ocean floor! Over millions of years, sediment buried sea creatures and turned them into fossils. Then enormous forces inside the Earth slowly pushed those rock layers upward, creating mountains. Wind and rain then wore away the surface, revealing the ancient ocean fossils at the top!",
    "stem_title": "Design a Fossil Dig Site",
    "stem_mission": "Design a model showing how fossils from different time periods end up in different rock layers, and plan a dig to find them.",
    "stem_scenario": "A museum has hired your team to plan a fossil dig in the mountains. You need to predict which rock layers will contain which types of fossils, and design a dig plan that carefully removes layers without damaging the fossils below.",
    "stem_questions": [
        "Which rock layer would contain the oldest fossils — the top layer or the bottom layer?",
        "If you find ocean fossils high on a mountain, what does that tell you about the area's history?",
        "How can you carefully dig through layers without destroying fossils in the layer below?"
    ],
    "stem_design_qs": [
        "How many rock layers will your model show, and what fossils are in each?",
        "What tools would a real paleontologist use to carefully remove rock from fossils?",
        "How will you label each layer with its age and the type of environment it came from?",
        "What safety rules should your dig team follow to protect the fossils?"
    ],
    "career": "Paleontologists study fossils to understand ancient life and how Earth has changed. They dig up dinosaur bones, ancient plants, and ocean creatures found in rock. They earn $55,000–$100,000/year.",
    "images": {
        "cover": ("cover-fossils.png", "A stunning close-up of a detailed seashell fossil embedded in rocky mountain stone with a dramatic mountain landscape visible in the background, warm golden light, cinematic nature photography"),
        "landscape": ("landscape-fossils.png", "A diverse group of 4th grade students (9-10 years old, 70-80% Black and Brown children with realistic coils, curls, locs, braids) on a field trip examining rock layers on a hillside, pointing at visible fossil impressions, bright sunny day, photorealistic"),
        "modeling": ("modeling-fossils.png", "A diverse group of 4th grade students (9-10 years old, Black and Brown children centered) working together on laptops building a digital model of rock layers, modern classroom with geology posters, natural light, photorealistic"),
        "discussion": ("discussion-fossils.png", "A teacher showing fossil specimens to engaged 4th grade students (9-10 years old, diverse with Black and Brown children centered, realistic hair coils curls locs braids), students with wide eyes and raised hands, bright classroom, photorealistic"),
        "stem": ("stem-fossil-dig.png", "4th grade students (9-10 years old, diverse multicultural group with Black children centered) carefully excavating a simulated fossil dig using small brushes and tools at tables, excited expressions, classroom science activity, photorealistic")
    },
    "pre_assessment": [
        "Have you ever found a fossil or seen one in a museum? What did it look like?",
        "How do you think fossils get inside of rocks?",
        "If you found a seashell on top of a mountain, how would you explain it?",
        "Draw what you think the layers of rock under the ground look like."
    ],
    "extend_components": [
        ("Erosion Rate", "Wind and rain wear away mountain surfaces, revealing deeper and older fossil layers"),
        ("Volcanic Activity", "Volcanic ash creates new layers that can preserve fossils in fine detail"),
        ("Climate Changes", "Different climates create different types of sediment and preserve different organisms")
    ],
    "reflections": [
        "If a mountain has ocean fossils at the top, what was that land like millions of years ago?",
        "Why are the oldest fossils usually found in the deepest rock layers?",
        "How is finding a fossil like reading a page from Earth's history book?",
        "What could happen to fossils if erosion wears away the rock they are trapped in?",
        "How does your model help explain something that took millions of years to happen?"
    ],
    "dimensions": [
        ("Science Practice", "Constructing Explanations and Designing Solutions", "Students use fossil evidence and rock layer patterns to construct an explanation for how landscapes change over time."),
        ("Disciplinary Core Idea", "ESS1.C The History of Planet Earth", "Local, regional, and global patterns of rock formations reveal changes over time due to Earth forces such as earthquakes and volcanic eruptions."),
        ("Crosscutting Concept", "Patterns", "Students identify patterns in rock layers and fossil locations to explain how landscapes have changed over millions of years.")
    ],
    "cast_items": [
        "Identify fossil evidence that shows how a landscape has changed over time",
        "Use patterns in rock layers to explain the order of geological events",
        "Describe how Earth forces like uplift and erosion reveal fossils at the surface"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A hiker finds a fish fossil on top of a mountain. Which explanation best describes how it got there?"),
        ("Constructed Response:", "You find three rock layers on a cliff: the bottom layer has ocean shells, the middle layer has fern leaves, and the top layer has land animal bones. Describe what happened to this area over time.")
    ],
    "background_intro": "The discovery of marine fossils on mountaintops was one of the great mysteries that early geologists had to solve. It is now understood as powerful evidence for the dynamic nature of Earth's surface.",
    "background_sections": [
        ("How Fossils Form", "Fossils form when an organism dies and is quickly buried by sediment like mud, sand, or volcanic ash. Over thousands to millions of years, the sediment hardens into rock, and minerals replace the original biological material. The most common fossils are from hard parts like shells, bones, and teeth, but soft-bodied organisms can be preserved under exceptional conditions."),
        ("Rock Layers Tell a Story", "The principle of superposition states that in undisturbed rock layers, the oldest layers are on the bottom and the youngest are on top. Each layer represents a different period in Earth's history. By examining the fossils in each layer, scientists can reconstruct what the environment was like at that time — ocean, swamp, desert, or forest."),
        ("How Mountains Rise", "Mountains form through tectonic forces — when two plates collide, the crust crumples and folds upward. The Himalayas, for example, contain marine limestone fossils from an ancient ocean floor (the Tethys Sea) that was pushed upward when the Indian plate collided with the Eurasian plate about 50 million years ago. Mount Everest's summit contains marine fossils."),
        ("Famous Fossil Locations", "The Grand Canyon reveals nearly 2 billion years of rock layers. The Burgess Shale in Canada preserves 500-million-year-old soft-bodied marine creatures. The La Brea Tar Pits in Los Angeles preserve Ice Age mammals. Each location tells a different chapter of Earth's long history through its rock layers and fossils.")
    ],
    "lever_L": "Students identify sediment buildup, Earth movement speed, and fossil exposure as the key components of the fossil formation and discovery system.",
    "lever_E": "Students determine that sediment buildup positively affects fossil creation (more sediment = more burial = more fossils), and Earth movement speed positively affects fossil exposure (more uplift = more surface exposure).",
    "lever_V": "Students build a model showing how sediment layers create fossils underwater, and how Earth movement lifts those layers to where erosion can reveal them.",
    "lever_Ev": "Students run ocean floor and mountain building scenarios to observe how the same fossil can go from deep underwater to a mountaintop.",
    "lever_R": "Students add erosion rate or volcanic activity to explore more complex interactions in the fossil exposure system.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with mountain fossil imagery", "say": "What if I told you the top of a mountain used to be at the bottom of the ocean?", "do": "Show a photo of a seashell fossil found on a mountain. Let students react with wonder.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are going to solve one of nature's biggest mysteries.", "do": "Have students read objectives aloud. Pre-teach fossil and sediment.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How did seashells get on a mountain?", "say": "Imagine hiking up a mountain and finding a seashell. How did it get there?", "do": "Have students turn and talk with a partner. Collect ideas on the board.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We will build a model to figure out this mystery step by step.", "do": "Briefly preview each LEVER step. Build excitement for the discovery.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for fossil system", "say": "What are the pieces of this puzzle? What has to happen for a fossil to end up on a mountain?", "do": "Guide students through identifying components. Discuss external vs internal.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "More sediment means more things get buried. More Earth movement means more fossils get pushed up. Both are positive!", "do": "Help students draw relationship arrows. Emphasize both relationships are positive.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let us travel millions of years into the past and watch what happens!", "do": "Students predict first, then run scenarios. Compare ocean floor vs mountain building.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "Now you know the secret — mountains used to be ocean floors!", "do": "Lead discussion connecting model results to real fossil discoveries like Mount Everest.", "time": "4 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Fossil dig design", "say": "You are now paleontologists! Plan a dig to find ancient treasures hidden in rock.", "do": "Distribute materials. Groups plan their fossil dig using rock layer evidence.", "time": "8 min"}
    ],
    "sort_reasoning": "Sediment Buildup and Earth Movement Speed are external because they are driven by natural forces that students cannot control — sedimentation happens in oceans and lakes, and tectonic forces push the ground upward. Fossil Exposure is internal because it is the result of both external forces working together over time.",
    "relationships": [
        ("Sediment Buildup to Fossil Exposure", "POSITIVE (+)", "More sediment buries more organisms, creating more fossils that can eventually be exposed when layers are lifted up."),
        ("Earth Movement Speed to Fossil Exposure", "POSITIVE (+)", "Faster Earth movement pushes rock layers higher above sea level, where wind and rain can wear away the surface and reveal the fossils trapped inside.")
    ],
    "sim_answers": [
        ("Ocean Floor Scenario", "When Sediment Buildup is high but Earth Movement is zero, many fossils form in the layers but none are exposed at the surface. They stay buried deep underwater. The model shows that fossils need both burial AND uplift to become discoverable."),
        ("Mountain Building Scenario", "When Earth Movement Speed is high, rock layers that were once on the ocean floor get pushed upward. As they rise, erosion wears away the surface layers, revealing the ancient fossils inside. The model shows that Earth movement is the key to bringing deep fossils to the surface.")
    ],
    "reflection_exemplars": [
        ("If a mountain has ocean fossils, what was that land like long ago?", "If there are ocean fossils on a mountain, that land must have been under the ocean millions of years ago. Sea creatures lived there, died, and got buried in sediment on the ocean floor. Over a very long time, enormous forces inside the Earth pushed that ocean floor upward until it became a mountain. The fossils are like a message from the past telling us the land's secret history."),
        ("Why are the oldest fossils in the deepest layers?", "The oldest fossils are deepest because rock layers form from the bottom up. The first layer of sediment settles on the ground and gets buried by the next layer, and the next, and the next. Each new layer is younger than the one below it. So if you dig down, you are going back in time — the deeper you go, the older the fossils you find. It is like a stack of books where the bottom book was placed first.")
    ],
    "stem_intro": "Present the challenge: A museum needs your team to plan a fossil dig on a mountain. You need to predict what fossils are in each rock layer and design a careful plan to excavate them without damage.",
    "stem_concepts": [
        ("Superposition", "In undisturbed rock layers, the oldest layer is always on the bottom and the youngest is on top. This principle helps scientists figure out the age of fossils without fancy equipment."),
        ("Index Fossils", "Certain fossils are found only in specific time periods. Finding one of these index fossils tells scientists exactly how old that rock layer is, like a timestamp in the rock."),
        ("Preservation", "Not all organisms become fossils. Hard parts like shells and bones preserve best. Soft-bodied creatures rarely fossilize unless conditions are perfect, like being buried in fine mud or volcanic ash very quickly.")
    ],
    "stem_eval": [
        ("Expert (4)", "Dig plan accurately shows multiple rock layers with age-appropriate fossils, explains the history of the site, and includes careful excavation methods"),
        ("Proficient (3)", "Dig plan shows rock layers with fossils in correct order and includes a basic excavation plan"),
        ("Developing (2)", "Dig plan shows some rock layers but fossils are not in correct order or excavation plan is missing"),
        ("Beginning (1)", "Dig plan is incomplete or does not connect rock layers to fossil placement")
    ],
    "support": [
        "Provide a pre-made diagram of rock layers with labels showing oldest at bottom, youngest at top",
        "Use a hands-on demonstration: stack colored sand in a clear jar to show how layers form",
        "Sentence frames: 'The fossil is on the mountain because __ pushed the rock layers __'"
    ],
    "extensions": [
        "Research Mount Everest's marine fossils and create a timeline showing how the ocean floor became the world's tallest peak",
        "Visit a virtual fossil museum online and identify three different types of fossils and what they tell us about the past",
        "Create a comic strip showing the journey of a seashell from the ocean floor to a mountaintop over millions of years"
    ],
    "cross_curr": [
        ("Math", "Create a timeline to scale showing when different rock layers formed — practice working with large numbers like millions of years"),
        ("ELA", "Write a story from the perspective of a fossil: What was your life like? How did you become a fossil? Who found you millions of years later?"),
        ("Art", "Create a layered paper or clay model of rock layers with fossil imprints in each layer, labeled with the environment and time period")
    ],
    "misconceptions": [
        ("Fossils are just old rocks shaped like animals", "Fossils are the actual preserved remains of once-living organisms, not random rock shapes. The organism died, was buried in sediment, and over millions of years the original material was replaced by minerals, turning it to stone while keeping its exact shape. Scientists can identify species, diet, and even diseases from fossils.", "Show a real fossil (or detailed photo) next to the living organism it came from. The detail preserved in fossils — teeth, leaf veins, shell ridges — proves these were once alive."),
        ("Mountains have always been mountains", "Many mountains were once ocean floors, plains, or even swamps. The Himalayas were a shallow sea 50 million years ago. The Appalachian Mountains were once taller than the Himalayas but have been worn down by hundreds of millions of years of erosion. Earth's surface is constantly changing — just very slowly.", "Show before-and-after diagrams of the same location millions of years apart. Ask: If mountains were always there, how do we explain ocean fossils at the summit?"),
        ("Fossils form quickly", "Fossil formation takes thousands to millions of years. An organism must be buried quickly in sediment before it decomposes, then the sediment must harden into rock over vast time periods. The minerals slowly replace the original material molecule by molecule. This is why fossils are rare — most organisms decompose before they can be preserved.", "Ask: Why do we not find fossils of every animal that has ever lived? Because fossilization requires very specific conditions and enormous amounts of time.")
    ]
}

L07 = {
    "id": "G04-L07",
    "title": "Can a River Eat a Mountain?",
    "subtitle": "The Slow but Powerful Force of Water on Rock",
    "ngss": "4-ESS2-1",
    "ngss_desc": "Make observations and/or measurements to provide evidence of the effects of weathering or the rate of erosion by water, wind, ice, and vegetation.",
    "big_question": "Can something as soft as water actually destroy something as hard as a mountain?",
    "objectives": [
        "Explain how water flow speed affects how quickly rock wears away",
        "Model how water flow speed, rock hardness, and erosion rate are connected",
        "Describe how weathering and erosion shape Earth's surface over time"
    ],
    "vocabulary": [
        ("Weathering", "The breaking down of rock into smaller pieces by water, wind, ice, or living things"),
        ("Erosion", "The movement of broken rock and soil from one place to another by water, wind, or ice"),
        ("Sediment", "Small pieces of rock, sand, and soil that have been broken off and carried away"),
        ("Canyon", "A deep valley with steep sides carved by a river over millions of years")
    ],
    "components": [
        ("Water Flow Speed", "How fast the water moves through a river or stream — faster water has more cutting power", True),
        ("Rock Hardness", "How resistant the rock is to being broken apart — soft rock erodes faster than hard rock", True),
        ("Erosion Rate", "How quickly the rock is wearing away and being carried downstream as sediment", False)
    ],
    "think_about_it": "When water flows faster, does it wear away rock faster or slower? When rock is harder, does it erode faster or slower?",
    "scenarios": [
        ("Gentle Stream", "Set Water Flow Speed to low and Rock Hardness to high — observe the erosion rate"),
        ("Raging River", "Lock Water Flow Speed to maximum and observe what happens to erosion rate"),
        ("Soft Rock Canyon", "Set Rock Hardness to low with moderate water flow and watch the canyon form")
    ],
    "sim_scenarios": [
        ("Gentle Stream", "Low water speed, hard rock", "What do you predict will happen to the Erosion Rate when a slow stream meets hard rock?"),
        ("Raging River", "Maximum water flow speed", "What do you predict will happen to the Erosion Rate when a powerful river hits the rock?"),
        ("Soft Rock Canyon", "Low rock hardness, moderate water", "What do you predict will happen when even a moderate stream flows over soft rock?")
    ],
    "discoveries": [
        "Faster water has more energy and can break apart and carry away larger pieces of rock",
        "Softer rock erodes much faster than harder rock, which is why canyons have uneven walls",
        "Even very slow water can wear away the hardest rock if given enough time — millions of years",
        "The Grand Canyon was carved by the Colorado River over about 5-6 million years"
    ],
    "answer": "Yes, a river absolutely CAN eat a mountain! Water may seem soft, but when it flows fast, it carries sand and small rocks that act like sandpaper, grinding away at the riverbed. Over millions of years, even a gentle stream can carve through the hardest rock. The Grand Canyon — a mile deep — was carved by a single river!",
    "stem_title": "Design an Erosion-Proof Riverbank",
    "stem_mission": "Design a riverbank protection system that slows down erosion and keeps soil and rock in place during heavy rains and fast water flow.",
    "stem_scenario": "A town's riverbank is washing away, and homes near the river are in danger. The town council needs your engineering team to design a solution that slows erosion without harming the river's ecosystem. Use your model evidence to choose the best approach.",
    "stem_questions": [
        "Based on your model, what causes the most erosion — fast water, soft rock, or both together?",
        "What materials or structures could slow down the water to reduce erosion?",
        "How can you protect the riverbank without blocking the river or harming wildlife?"
    ],
    "stem_design_qs": [
        "Will you use plants, rocks, walls, or a combination to protect the bank?",
        "How will your design handle both normal water flow and flood conditions?",
        "What materials will you use and why?",
        "How will you test whether your design actually reduces erosion?"
    ],
    "career": "Hydrologists and Geomorphologists study how water shapes the land and design solutions to manage erosion, flooding, and water resources. They earn $60,000–$110,000/year.",
    "images": {
        "cover": ("cover-erosion.png", "A breathtaking aerial view of the Grand Canyon showing deep red and orange rock layers carved by the Colorado River below, dramatic golden hour lighting, cinematic landscape photography"),
        "landscape": ("landscape-erosion.png", "A diverse group of 4th grade students (9-10 years old, 70-80% Black and Brown children with realistic coils, curls, locs, braids) observing a stream cutting through soil and rocks during a field trip, pointing and taking notes, sunny outdoor setting, photorealistic"),
        "modeling": ("modeling-erosion.png", "A diverse group of 4th grade students (9-10 years old, Black and Brown children centered) working on laptops building a digital erosion model, modern classroom with Earth science posters, natural light, photorealistic"),
        "discussion": ("discussion-erosion.png", "A teacher showing before-and-after photos of erosion to engaged 4th grade students (9-10 years old, diverse with Black and Brown children centered, realistic hair details), students pointing at smartboard, bright classroom, photorealistic"),
        "stem": ("stem-riverbank.png", "4th grade students (9-10 years old, diverse multicultural group with Black children centered) building model riverbanks with soil, rocks, and small plants in plastic trays, testing with poured water, excited expressions, classroom science activity, photorealistic")
    },
    "pre_assessment": [
        "Have you ever seen a river or stream? What did the edges look like?",
        "Can water break apart a rock? Why or why not?",
        "What do you think the Grand Canyon looked like before the river carved it?",
        "Draw what you think happens when fast water hits a rocky cliff."
    ],
    "extend_components": [
        ("Wind Speed", "Wind also carries tiny particles that sandblast rock surfaces, especially in dry areas"),
        ("Ice Formation", "Water that freezes in rock cracks expands and splits the rock apart piece by piece"),
        ("Plant Roots", "Plant roots grow into rock cracks and slowly push them apart as they grow bigger")
    ],
    "reflections": [
        "How can something as soft as water destroy something as hard as rock?",
        "Why does the Grand Canyon have layers of different colors on its walls?",
        "What would happen to mountains if there was no rain or rivers for millions of years?",
        "How is erosion both helpful and harmful to humans?",
        "How does your model help explain something that takes millions of years?"
    ],
    "dimensions": [
        ("Science Practice", "Planning and Carrying Out Investigations", "Students make observations and gather evidence about how water flow speed and rock hardness affect erosion rate."),
        ("Disciplinary Core Idea", "ESS2.A Earth Materials and Systems", "Rainfall helps to shape the land and affects the types of living things found in a region. Water, ice, wind, living organisms, and gravity break rocks, soils, and sediments into smaller particles and move them around."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify cause and effect relationships between water speed, rock hardness, and the rate of erosion.")
    ],
    "cast_items": [
        "Describe how water, wind, and ice cause weathering and erosion of rock",
        "Provide evidence that the rate of erosion depends on the speed of water and the hardness of rock",
        "Explain how erosion shapes Earth's surface features like canyons, valleys, and deltas"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Two rivers flow at the same speed. River A flows over soft sandstone and River B flows over hard granite. Which river will carve a deeper channel in the same amount of time?"),
        ("Constructed Response:", "Explain how the Grand Canyon was formed using the words erosion, water flow, and rock layers in your answer.")
    ],
    "background_intro": "Erosion is one of the most powerful forces shaping Earth's surface. While it works slowly compared to human lifetimes, over geological time it has carved the Grand Canyon, worn down entire mountain ranges, and created fertile river deltas.",
    "background_sections": [
        ("How Water Erodes Rock", "Moving water erodes rock through three main processes: hydraulic action (the force of water itself loosening rock), abrasion (sand and pebbles carried by water grinding against rock like sandpaper), and dissolution (water dissolving minerals in certain types of rock). Faster water has more kinetic energy and can erode far more effectively than slow water."),
        ("The Grand Canyon Story", "The Grand Canyon is approximately 277 miles long, up to 18 miles wide, and over a mile deep. It was carved primarily by the Colorado River over 5-6 million years. The canyon's colorful rock layers span nearly 2 billion years of geological history. The oldest rocks at the bottom (Vishnu Basement Rocks) are about 1.84 billion years old."),
        ("Rock Hardness and Erosion", "The Mohs hardness scale rates minerals from 1 (talc) to 10 (diamond). Soft rocks like limestone and sandstone erode much faster than hard rocks like granite and quartzite. This differential erosion is why canyon walls often have a staircase pattern — hard layers stick out while soft layers are carved deeper. It also explains why some mountains are taller than others."),
        ("Erosion and Human Life", "Erosion creates fertile farmland by depositing nutrient-rich sediment in river valleys and deltas. The Nile Delta, Mississippi Delta, and Ganges Delta are among the most productive agricultural areas on Earth — all created by erosion. However, erosion also threatens structures, roads, and homes built near rivers and coastlines. Managing erosion is a major engineering challenge.")
    ],
    "lever_L": "Students identify water flow speed, rock hardness, and erosion rate as the key components of the weathering and erosion system.",
    "lever_E": "Students determine that water flow speed positively affects erosion rate (faster water = more erosion), while rock hardness negatively affects erosion rate (harder rock = less erosion).",
    "lever_V": "Students build a model showing how fast-flowing water interacts with different types of rock to produce different erosion rates.",
    "lever_Ev": "Students run gentle stream, raging river, and soft rock scenarios to observe how changing water speed and rock type affects erosion.",
    "lever_R": "Students add wind speed, ice formation, or plant roots to explore other forces that break down rock.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with Grand Canyon imagery", "say": "This canyon is a MILE deep. And the only thing that carved it was water. How is that possible?", "do": "Show a dramatic photo of the Grand Canyon. Let students express wonder.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are going to figure out how something soft can destroy something hard.", "do": "Have students read objectives aloud. Pre-teach weathering and erosion.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Can water really destroy rock?", "say": "You drink water. You swim in water. You wash your hands with water. Can it really eat a mountain?", "do": "Quick poll: How many students think water can break rock? Discuss initial ideas.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We will build a model to test whether water can really destroy rock.", "do": "Preview LEVER steps. Connect to student curiosity.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for erosion system", "say": "What affects how fast rock wears away? Think about the water AND the rock.", "do": "Guide component sorting. Discuss why water speed and rock hardness come from outside the system.", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Faster water means MORE erosion — that is positive. But harder rock means LESS erosion — that is negative!", "do": "Help students draw arrows. This lesson has one positive and one negative relationship.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let us see what happens when a raging river meets soft rock!", "do": "Students predict, then run scenarios. Compare gentle stream vs raging river.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "Now you know the answer — yes, a river CAN eat a mountain. It just takes millions of years!", "do": "Connect model results to Grand Canyon. Discuss how time changes everything.", "time": "4 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Riverbank protection design", "say": "A town needs your help — the river is eating their riverbank! Design a solution.", "do": "Distribute materials. Groups design erosion-proof riverbank solutions.", "time": "8 min"}
    ],
    "sort_reasoning": "Water Flow Speed and Rock Hardness are external because they are determined by nature — rainfall and terrain control water speed, and the type of rock is determined by geological history. Erosion Rate is internal because it is the outcome of how fast water meets how hard the rock is.",
    "relationships": [
        ("Water Flow Speed to Erosion Rate", "POSITIVE (+)", "Faster water has more energy to break apart rock and carry away pieces. A raging river erodes much faster than a gentle stream."),
        ("Rock Hardness to Erosion Rate", "NEGATIVE (-)", "Harder rock resists being broken apart. Soft sandstone erodes easily while hard granite takes much longer to wear away.")
    ],
    "sim_answers": [
        ("Raging River Scenario", "When Water Flow Speed is at maximum, Erosion Rate increases dramatically. The fast-moving water has enormous energy that breaks apart even moderately hard rock. The model shows that water speed is the most powerful factor in erosion — doubling the speed more than doubles the erosion because the water's energy increases with the square of its speed."),
        ("Soft Rock Canyon Scenario", "When Rock Hardness is low with moderate water flow, the Erosion Rate is surprisingly high. Even moderate water can quickly carve through soft rock. This explains why some canyons form faster than others — the type of rock matters as much as the water speed. In real life, the Grand Canyon carved through softer limestone layers much faster than through harder granite layers.")
    ],
    "reflection_exemplars": [
        ("How can soft water destroy hard rock?", "Water seems soft because it flows around your hands, but when it moves fast, it has a LOT of energy. Fast-moving water also carries sand and small rocks that act like sandpaper, grinding away at the riverbed. Plus, water can dissolve certain minerals in rock, weakening it from the inside. Over millions of years, even a gentle stream can carve through the hardest granite. It is not about strength — it is about time and persistence."),
        ("How is erosion both helpful and harmful?", "Erosion is helpful because it creates fertile farmland. When rivers flood, they deposit nutrient-rich sediment on the surrounding land, making it perfect for growing crops. The Nile River in Egypt made farming possible for thousands of years this way. But erosion is harmful when it washes away soil that farmers need, undermines buildings and roads, and causes landslides. Engineers have to design solutions to manage erosion in both helpful and harmful ways.")
    ],
    "stem_intro": "Present the scenario: A town's riverbank is washing away during every rainstorm, and houses are getting dangerously close to the edge. The town needs your engineering team to design a riverbank protection system that slows erosion without harming the river ecosystem.",
    "stem_concepts": [
        ("Riprap", "Large rocks placed along riverbanks to absorb the energy of fast-moving water and prevent it from eroding the soil beneath. This is one of the oldest and most common erosion control methods."),
        ("Bioengineering", "Using living plants to control erosion. Deep-rooted plants hold soil in place, and their stems slow down water flow. Willow trees and native grasses are commonly used along riverbanks."),
        ("Velocity and Energy", "The energy of moving water increases with the square of its velocity. This means that water moving twice as fast has FOUR times the erosive power. Slowing water down even a little can dramatically reduce erosion.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design uses model evidence about water speed and rock hardness, includes multiple erosion control methods, and considers environmental impact"),
        ("Proficient (3)", "Design references model data and includes at least two erosion control methods"),
        ("Developing (2)", "Design mentions erosion but does not clearly connect protection methods to model evidence"),
        ("Beginning (1)", "Design is incomplete or does not demonstrate understanding of erosion factors")
    ],
    "support": [
        "Provide photos of real erosion control methods (riprap, retaining walls, plant barriers) for reference",
        "Do a hands-on demo: pour water over a pile of sand vs a pile of gravel to show erosion differences",
        "Sentence frames: 'When water flows faster, erosion __ because __'"
    ],
    "extensions": [
        "Research the Grand Canyon and create a poster showing how it was formed layer by layer over millions of years",
        "Design an experiment to test which type of soil erodes fastest: sand, clay, or soil with plant roots",
        "Investigate coastal erosion and how engineers protect beaches from ocean waves"
    ],
    "cross_curr": [
        ("Math", "Measure and compare erosion rates by timing how long it takes water to wash away different amounts of soil in a stream table experiment"),
        ("ELA", "Write an informational paragraph explaining to a younger student how the Grand Canyon was formed, using vocabulary from the lesson"),
        ("Art", "Create a before-and-after landscape painting showing a mountain being slowly carved by a river over millions of years")
    ],
    "misconceptions": [
        ("Water is too soft to break rock", "While individual water molecules are tiny, moving water has tremendous energy. A fast-flowing river carries sand and pebbles that act like sandpaper, grinding rock away. Water also seeps into cracks and freezes, expanding and breaking rock apart. Over millions of years, water has carved the deepest canyons and worn down the tallest mountains on Earth.", "Demo: Rub a piece of chalk with a dry cloth (nothing happens). Now rub it with a wet cloth — it wears away quickly. Water changes everything."),
        ("Erosion only happens during floods or storms", "Erosion happens every single day, even when you cannot see it. Every raindrop that hits soil, every stream that flows over rock, and every wave that hits a beach is causing erosion. Major storms cause dramatic erosion, but the slow, constant erosion happening every day actually shapes more of the landscape over geological time.", "Ask: Does a dripping faucet ever wear a mark in a sink? That is everyday erosion happening right in your home."),
        ("The Grand Canyon was formed quickly by a huge flood", "The Grand Canyon was carved primarily by the steady flow of the Colorado River over 5-6 million years, not by a single catastrophic event. While floods did speed up erosion at times, the canyon is the result of constant, slow erosion over an almost unimaginable span of time. The deepest rock layers exposed at the bottom are nearly 2 billion years old.", "Show a time-lapse concept: If the Grand Canyon took 5 million years to form, and it is about 1 mile deep, the river carved about 1 inch every 100 years. That is incredibly slow — but incredibly persistent.")
    ]
}

L08 = {
    "id": "G04-L08",
    "title": "Where Does Your Electricity Come From?",
    "subtitle": "Tracing Energy from Natural Resources to Your Light Switch",
    "ngss": "4-ESS3-1",
    "ngss_desc": "Obtain and combine information to describe that energy and fuels are derived from natural resources and their uses affect the environment.",
    "big_question": "What happens between a power plant and your light switch to make electricity flow to your home?",
    "objectives": [
        "Explain how natural resources like coal, gas, wind, and sunlight are used to generate electricity",
        "Model how the amount of energy source, power plant output, and home electricity are connected",
        "Describe how different energy sources affect the environment in different ways"
    ],
    "vocabulary": [
        ("Natural Resource", "A material from nature that people use, like water, coal, sunlight, or wind"),
        ("Energy Source", "The natural resource that is converted into electricity at a power plant"),
        ("Power Plant", "A facility that converts energy from natural resources into electricity for homes and businesses"),
        ("Renewable Energy", "Energy from sources that never run out, like sunlight, wind, and flowing water")
    ],
    "components": [
        ("Energy Source Amount", "How much natural resource (coal, gas, sunlight, wind) is available to make electricity", True),
        ("Power Plant Output", "How much electricity the power plant produces from the energy source", False),
        ("Home Electricity", "The amount of electricity that reaches homes for lights, devices, and appliances", False)
    ],
    "think_about_it": "When the energy source amount increases (more coal, more sunlight, more wind), what happens to power plant output? What happens to home electricity?",
    "scenarios": [
        ("Sunny Day Solar", "Set Energy Source Amount to high (lots of sunlight) and observe electricity flow"),
        ("Cloudy Week", "Lock Energy Source Amount to low (very little sunlight) and observe what happens"),
        ("Windy Night", "Set Energy Source to moderate (wind) and observe power plant output")
    ],
    "sim_scenarios": [
        ("Sunny Day Solar", "High energy source (lots of sunlight)", "What do you predict will happen to Home Electricity when the sun is shining brightly all day?"),
        ("Cloudy Week", "Low energy source (very little sunlight)", "What do you predict will happen to Power Plant Output when clouds block the sun for a week?"),
        ("Windy Night", "Moderate energy source (steady wind)", "What do you predict will happen to Home Electricity when it is dark but windy?")
    ],
    "discoveries": [
        "All electricity comes from converting natural resources — we cannot create energy from nothing",
        "More available energy source means more power plant output and more home electricity",
        "Renewable sources like solar and wind depend on weather, while fossil fuels can be burned anytime",
        "Every energy source affects the environment — fossil fuels create pollution, while renewables need space for panels and turbines"
    ],
    "answer": "Your electricity comes from natural resources! Power plants convert coal, natural gas, sunlight, wind, or flowing water into electrical energy. The electricity then travels through wires to your home. Different energy sources have different trade-offs — fossil fuels work anytime but pollute the air, while renewable sources are clean but depend on weather conditions.",
    "stem_title": "Design Your Town's Energy Plan",
    "stem_mission": "Design an energy plan for a small town that provides reliable electricity while being as kind to the environment as possible.",
    "stem_scenario": "Your town of 1,000 homes needs a new energy plan. The town council wants you to choose the best mix of energy sources. You have options: a coal plant, a solar farm, a wind farm, or a small dam. Each has advantages and disadvantages. Use your model to recommend the best plan.",
    "stem_questions": [
        "Which energy sources are available all the time, and which depend on weather?",
        "Which energy sources are cleanest for the environment?",
        "How can you combine sources to make sure the town always has enough electricity?"
    ],
    "stem_design_qs": [
        "What mix of energy sources will you recommend for the town?",
        "How will you make sure there is electricity at night when solar panels do not work?",
        "What are the environmental trade-offs of each energy source you chose?",
        "How will your plan change if the town grows to 2,000 homes?"
    ],
    "career": "Energy Engineers and Sustainability Planners design power systems and help communities switch to cleaner energy sources. They earn $65,000–$120,000/year.",
    "images": {
        "cover": ("cover-electricity.png", "A dramatic split image showing a power plant with cooling towers on one side and a solar panel farm with wind turbines on the other side, connected by power lines, golden sunset light, cinematic photography"),
        "landscape": ("landscape-electricity.png", "A diverse group of 4th grade students (9-10 years old, 70-80% Black and Brown children with realistic coils, curls, locs, braids) visiting a solar panel installation, looking up at the panels with curiosity, bright sunny day, photorealistic"),
        "modeling": ("modeling-electricity.png", "A diverse group of 4th grade students (9-10 years old, Black and Brown children centered) working on laptops building a digital energy model, modern classroom with science posters about energy, natural light, photorealistic"),
        "discussion": ("discussion-electricity.png", "A teacher leading a discussion about energy sources with engaged 4th grade students (9-10 years old, diverse with Black and Brown children centered, realistic hair details), diagram of energy sources on smartboard, bright classroom, photorealistic"),
        "stem": ("stem-energy-plan.png", "4th grade students (9-10 years old, diverse multicultural group with Black children centered) designing town energy plans on large paper with markers and small model turbines and solar panels on the table, collaborative group work, photorealistic")
    },
    "pre_assessment": [
        "What happens when you flip a light switch? Where does the electricity come from?",
        "Can you name any ways that electricity is made?",
        "What is the difference between energy from the sun and energy from coal?",
        "Draw a picture showing how electricity gets from a power plant to your home."
    ],
    "extend_components": [
        ("Battery Storage", "Batteries can store extra electricity from solar and wind for use when the sun is not shining or the wind is not blowing"),
        ("Transmission Distance", "Electricity loses some energy as heat when it travels long distances through power lines"),
        ("Energy Demand", "The amount of electricity people use changes throughout the day — highest in the evening when everyone is home")
    ],
    "reflections": [
        "Why can we not just use one type of energy source for everything?",
        "What happens to a solar-powered town when it is cloudy for a whole week?",
        "How does burning coal to make electricity affect the air and the environment?",
        "If you could design the perfect energy source, what would it be like?",
        "How does your model help you understand the trade-offs between different energy sources?"
    ],
    "dimensions": [
        ("Science Practice", "Obtaining, Evaluating, and Communicating Information", "Students gather and combine information about different energy sources and their environmental impacts to make informed decisions."),
        ("Disciplinary Core Idea", "ESS3.A Natural Resources", "Energy and fuels that humans use are derived from natural sources, and their use affects the environment in multiple ways. Some resources are renewable over human lifetimes, and some are not."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify cause and effect relationships between energy source availability, power production, and electricity delivery to homes.")
    ],
    "cast_items": [
        "Describe how different natural resources are used to generate electricity",
        "Explain how the use of fossil fuels affects the environment compared to renewable sources",
        "Identify trade-offs between different energy sources for a community"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A town uses only solar panels for electricity. During a week of cloudy weather, what problem would the town face, and which addition would best solve it?"),
        ("Constructed Response:", "Compare two energy sources — coal and wind — by explaining where each comes from, how it makes electricity, and how it affects the environment.")
    ],
    "background_intro": "Electricity is so common in modern life that we rarely think about where it comes from. Yet the journey from natural resource to wall outlet is a fascinating chain of energy conversions with significant environmental implications.",
    "background_sections": [
        ("How Power Plants Work", "Most power plants work by spinning a turbine connected to a generator. In fossil fuel plants, burning coal or natural gas heats water to create steam, which spins the turbine. In wind farms, moving air spins the turbine directly. In hydroelectric dams, falling water spins the turbine. Solar panels are different — they convert sunlight directly into electricity using photovoltaic cells without any spinning parts."),
        ("Fossil Fuels", "Coal, natural gas, and oil are fossil fuels formed from ancient plants and animals buried millions of years ago. They store enormous amounts of chemical energy, which is released when burned. However, burning fossil fuels releases carbon dioxide (CO2) and other pollutants into the atmosphere, contributing to climate change and air quality problems. Fossil fuels are nonrenewable — once used, they take millions of years to form again."),
        ("Renewable Energy Sources", "Solar, wind, hydroelectric, and geothermal energy are renewable — they replenish naturally. Solar power from the sun and wind power from moving air are the fastest-growing energy sources worldwide. Their main limitation is intermittency: solar panels do not produce electricity at night, and wind turbines need wind to spin. Battery storage technology is rapidly improving to address this challenge."),
        ("The Power Grid", "Electricity travels from power plants to homes through the power grid — a vast network of transmission lines, transformers, and substations. High-voltage transmission lines carry electricity over long distances, and transformers step down the voltage for safe home use. The grid must constantly balance supply and demand because electricity cannot be easily stored in large quantities, though battery technology is changing this.")
    ],
    "lever_L": "Students identify energy source amount, power plant output, and home electricity as the key components of the electricity generation and delivery system.",
    "lever_E": "Students determine that energy source amount positively affects power plant output (more fuel or sunlight = more electricity produced), and power plant output positively affects home electricity (more production = more electricity available for homes).",
    "lever_V": "Students build a model showing how natural resources flow through power plants to become the electricity that powers homes.",
    "lever_Ev": "Students run sunny day, cloudy week, and windy night scenarios to observe how energy source availability affects the entire electricity chain.",
    "lever_R": "Students add battery storage or transmission distance to explore more realistic electricity system dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with power plant and solar panel imagery", "say": "Right now, electricity is flowing through the walls around you. But where did it come from?", "do": "Turn off the classroom lights for 3 seconds, then turn them back on. Ask: What just happened?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are going to trace electricity from its source all the way to your light switch.", "do": "Have students read objectives aloud. Pre-teach natural resource and renewable energy.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Where does your electricity come from?", "say": "Think about everything you used electricity for today. Now — where did ALL that electricity come from?", "do": "Have students list 5 things they used electricity for. Then ask: But where does it START?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We will build a model to understand the journey of electricity from nature to your home.", "do": "Preview LEVER steps. Build curiosity about the energy chain.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for energy system", "say": "Every light switch connects back to a natural resource. Let us figure out the chain.", "do": "Guide component sorting. Discuss why energy sources come from outside the system.", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "More sunlight means more electricity from solar panels. More electricity from the plant means more power for homes. Both positive!", "do": "Help students draw relationship arrows. Both relationships are positive in this system.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "What happens to your electricity when a cloud covers the sun? Let us find out!", "do": "Students predict, then run scenarios. Compare sunny day vs cloudy week.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "Now you know — every time you flip a switch, nature is working to power it!", "do": "Lead discussion about trade-offs between energy sources. Show real-world examples.", "time": "4 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Town energy plan design", "say": "Your town needs a new energy plan. You decide how to power 1,000 homes!", "do": "Distribute materials. Groups design energy plans balancing reliability and environment.", "time": "8 min"}
    ],
    "sort_reasoning": "Energy Source Amount is external because it comes from nature — sunlight, wind, coal deposits, and water flow are not controlled by the power system itself. Power Plant Output and Home Electricity are internal because they depend on how much energy source is available and how efficiently the system converts and delivers it.",
    "relationships": [
        ("Energy Source Amount to Power Plant Output", "POSITIVE (+)", "More available energy source (more sunlight, more wind, more coal) means the power plant can produce more electricity. Less source means less output."),
        ("Power Plant Output to Home Electricity", "POSITIVE (+)", "When the power plant produces more electricity, more is available to flow through power lines to homes. When output drops, homes may experience brownouts or blackouts.")
    ],
    "sim_answers": [
        ("Cloudy Week Scenario", "When Energy Source Amount is locked to low (very little sunlight), Power Plant Output drops dramatically. Home Electricity also drops because there is not enough power being generated. The model shows that solar energy is completely dependent on sunshine — without it, the system produces almost no electricity."),
        ("Windy Night Scenario", "With moderate wind energy source, Power Plant Output stays at a moderate level even at night. This shows that wind energy can work when solar cannot — it does not need sunlight. The model reveals why combining energy sources (solar + wind) is more reliable than using just one.")
    ],
    "reflection_exemplars": [
        ("Why can we not use just one energy source?", "Every energy source has limitations. Solar only works during sunny days. Wind only works when it is windy. Coal can work anytime but pollutes the air. Hydroelectric needs a river with a dam. No single source is perfect for every situation. That is why most communities use a MIX of energy sources — so when one is not available, another can fill in. It is like having a backup plan for your backup plan."),
        ("How does burning coal affect the environment?", "When coal burns in a power plant, it releases carbon dioxide (CO2) into the atmosphere. CO2 traps heat from the sun and warms the planet, which is called climate change. Burning coal also releases tiny particles and other pollutants that make the air dirty and can cause breathing problems for people and animals. Coal mining also damages the land where the coal is dug up. That is why many communities are switching to cleaner energy sources like solar and wind.")
    ],
    "stem_intro": "Present the challenge: Your town of 1,000 homes needs a new energy plan. The old coal plant is being retired. You must recommend a mix of energy sources that keeps the lights on AND protects the environment.",
    "stem_concepts": [
        ("Energy Mix", "Most communities use multiple energy sources rather than relying on just one. This provides backup when one source is unavailable and allows balancing cost, reliability, and environmental impact."),
        ("Intermittency", "Some energy sources, like solar and wind, are intermittent — they only produce electricity when the sun shines or wind blows. This is the biggest challenge for renewable energy and is why battery storage is so important."),
        ("Environmental Trade-offs", "Every energy source has some environmental impact. Fossil fuels pollute the air. Solar farms and wind farms need large amounts of land. Dams change river ecosystems. The goal is to minimize overall environmental harm while meeting energy needs.")
    ],
    "stem_eval": [
        ("Expert (4)", "Energy plan uses model evidence, includes multiple sources for reliability, addresses environmental trade-offs, and considers growth"),
        ("Proficient (3)", "Energy plan includes multiple sources and mentions environmental considerations"),
        ("Developing (2)", "Energy plan lists energy sources but does not explain trade-offs or use model evidence"),
        ("Beginning (1)", "Energy plan is incomplete or relies on only one source without explanation")
    ],
    "support": [
        "Provide a comparison chart of energy sources with icons showing advantages and disadvantages",
        "Use a hands-on demonstration: a hand-crank flashlight to show how mechanical energy becomes electricity",
        "Sentence frames: 'When the energy source amount increases, power plant output __ because __'"
    ],
    "extensions": [
        "Research where your home's electricity actually comes from — what power plants serve your area?",
        "Calculate how many solar panels it would take to power your classroom for one day",
        "Design a poster comparing the environmental impact of three different energy sources"
    ],
    "cross_curr": [
        ("Math", "Create a pie chart showing the percentage of electricity from different sources in your state, and calculate how it would change with more solar panels"),
        ("ELA", "Write a persuasive letter to your school principal recommending whether the school should install solar panels, using evidence from the lesson"),
        ("Social Studies", "Research how access to electricity varies around the world and how it affects the quality of life in different communities")
    ],
    "misconceptions": [
        ("Electricity comes from the wall outlet", "The outlet is just the final delivery point. Electricity is generated far away at a power plant by converting natural resources into electrical energy. It then travels through miles of power lines and multiple transformers to reach your home. The outlet is like a faucet — the water does not come from the faucet, it comes from a water source far away.", "Trace the path: Outlet > wires in wall > meter outside > power lines > transformer > more power lines > power plant > natural resource. It is a long journey!"),
        ("Renewable energy is free", "While sunlight and wind are free, the equipment to capture them is not. Solar panels, wind turbines, and batteries all cost money to build, install, and maintain. However, once installed, the ongoing cost is much lower than fossil fuels because you do not need to keep buying fuel. Over time, renewable energy often becomes cheaper than fossil fuel energy.", "Compare: A coal plant must buy coal every day forever. A solar farm pays for panels once, then gets free sunlight for 25+ years. Which costs less over time?"),
        ("We can just turn off power plants when we do not need electricity", "Power plants cannot turn on and off like a light switch. Coal and nuclear plants take hours or even days to start up and shut down. This is why the power grid must constantly balance supply and demand in real time. Solar and wind add complexity because their output varies with weather. Grid operators work 24/7 to keep everything balanced.", "Ask: What would happen if everyone in your city turned on their air conditioning at exactly the same time? The grid has to be ready for that peak demand.")
    ]
}

L09 = {
    "id": "G04-L09",
    "title": "Can We Stop an Earthquake from Breaking Buildings?",
    "subtitle": "Engineering Solutions to Protect People from Natural Hazards",
    "ngss": "4-ESS3-2",
    "ngss_desc": "Generate and compare multiple solutions to reduce the impacts of natural Earth processes on humans.",
    "big_question": "How do engineers design buildings that can survive an earthquake without falling down?",
    "objectives": [
        "Explain how earthquake strength and building flexibility affect how much damage occurs",
        "Model how earthquake strength, building flexibility, and damage level are connected",
        "Compare different engineering solutions that reduce earthquake damage"
    ],
    "vocabulary": [
        ("Earthquake", "A sudden shaking of the ground caused by movement of rock deep beneath Earth's surface"),
        ("Natural Hazard", "A natural event like an earthquake, flood, or hurricane that can harm people and property"),
        ("Flexible", "Able to bend without breaking — flexible buildings sway during earthquakes instead of cracking"),
        ("Base Isolation", "A design that places a building on special pads that absorb shaking, keeping the building still")
    ],
    "components": [
        ("Earthquake Strength", "How powerful the earthquake is, measured by how much the ground shakes", True),
        ("Building Flexibility", "How much a building can sway and bend during shaking without cracking or falling", False),
        ("Damage Level", "How much destruction the earthquake causes to the building and things inside it", False)
    ],
    "think_about_it": "When earthquake strength increases, what happens to damage level? When building flexibility increases, what happens to damage level?",
    "scenarios": [
        ("Small Tremor", "Set Earthquake Strength to low and Building Flexibility to moderate — observe damage"),
        ("Major Quake, Stiff Building", "Lock Earthquake Strength to high and Building Flexibility to low — observe damage"),
        ("Major Quake, Flexible Building", "Lock Earthquake Strength to high and Building Flexibility to high — compare damage")
    ],
    "sim_scenarios": [
        ("Small Tremor", "Low earthquake, moderate flexibility", "What do you predict will happen to the Damage Level during a small earthquake in a normal building?"),
        ("Major Quake, Stiff Building", "High earthquake, low flexibility", "What do you predict will happen to the Damage Level when a big earthquake hits a stiff building?"),
        ("Major Quake, Flexible Building", "High earthquake, high flexibility", "What do you predict will happen to the Damage Level when the SAME big earthquake hits a flexible building?")
    ],
    "discoveries": [
        "Stronger earthquakes cause more damage, but building design can dramatically reduce it",
        "Stiff buildings crack and break during earthquakes because they fight against the shaking",
        "Flexible buildings sway WITH the earthquake, absorbing the energy instead of breaking",
        "Engineers cannot stop earthquakes, but they CAN design buildings that survive them"
    ],
    "answer": "Engineers cannot stop earthquakes, but they CAN stop buildings from falling down! They design flexible buildings that sway with the shaking instead of fighting it. Special features like base isolators (rubber pads under the building), cross-bracing (X-shaped supports), and deep foundations help buildings absorb earthquake energy. A well-designed building can survive even a powerful earthquake!",
    "stem_title": "Design an Earthquake-Proof Structure",
    "stem_mission": "Design and build a model structure that can survive simulated earthquake shaking on a shake table without collapsing.",
    "stem_scenario": "A city in earthquake country needs new buildings designed to protect people during the next big quake. Your engineering team must design a structure that stays standing when the ground shakes. You will test your design on a shake table and compare results with other teams.",
    "stem_questions": [
        "Based on your model, what happens to stiff buildings vs flexible buildings during a strong earthquake?",
        "What design features will help your structure absorb earthquake energy instead of breaking?",
        "How will you test your design to make sure it works?"
    ],
    "stem_design_qs": [
        "What materials will you use to make your structure flexible but strong?",
        "How will you connect the base of your structure to the ground — rigidly or with some movement allowed?",
        "What shape will your structure be — tall and thin, or wide and low?",
        "How will you make sure your structure can survive multiple shakes, not just one?"
    ],
    "career": "Structural Engineers and Seismic Design Specialists design buildings, bridges, and structures that can withstand earthquakes, hurricanes, and other natural forces. They earn $70,000–$130,000/year.",
    "images": {
        "cover": ("cover-earthquake.png", "A dramatic split image showing a damaged cracked building on one side and a modern earthquake-resistant building with base isolators and cross-bracing on the other side, earthquake design engineering concept, cinematic photography"),
        "landscape": ("landscape-earthquake.png", "A diverse group of 4th grade students (9-10 years old, 70-80% Black and Brown children with realistic coils, curls, locs, braids) looking at a model building on a shake table, excited and curious expressions, modern classroom, photorealistic"),
        "modeling": ("modeling-earthquake.png", "A diverse group of 4th grade students (9-10 years old, Black and Brown children centered) working on laptops building a digital earthquake model, modern classroom with engineering posters, natural light, photorealistic"),
        "discussion": ("discussion-earthquake.png", "A teacher explaining earthquake engineering to engaged 4th grade students (9-10 years old, diverse with Black and Brown children centered, realistic hair details), showing a cross-bracing diagram on smartboard, bright classroom, photorealistic"),
        "stem": ("stem-earthquake-build.png", "4th grade students (9-10 years old, diverse multicultural group with Black children centered) building model structures with craft sticks, marshmallows, and tape, testing on a homemade shake table, excited collaborative engineering activity, photorealistic")
    },
    "pre_assessment": [
        "Have you ever felt an earthquake or seen earthquake damage on the news?",
        "Why do some buildings fall down during earthquakes and others stay standing?",
        "If you were going to build an earthquake-proof building, what would you do differently?",
        "Draw what you think happens to a building during an earthquake."
    ],
    "extend_components": [
        ("Foundation Depth", "Deeper foundations anchor buildings more securely to stable ground below the shaking surface"),
        ("Building Height", "Taller buildings sway more during earthquakes and need special engineering to stay safe"),
        ("Ground Type", "Buildings on soft soil shake more than buildings on hard rock during the same earthquake")
    ],
    "reflections": [
        "Why is a flexible building safer than a stiff building during an earthquake?",
        "How is earthquake engineering similar to how trees survive strong windstorms?",
        "If we cannot stop earthquakes from happening, what CAN we do to keep people safe?",
        "What other natural hazards could engineers design solutions for?",
        "How does your model help engineers make better decisions about building design?"
    ],
    "dimensions": [
        ("Science Practice", "Constructing Explanations and Designing Solutions", "Students generate and compare multiple engineering solutions to reduce earthquake damage, using model evidence to evaluate their effectiveness."),
        ("Disciplinary Core Idea", "ESS3.B Natural Hazards", "A variety of hazards result from natural processes. Humans cannot eliminate the hazards but can take steps to reduce their impacts."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify cause and effect relationships between earthquake strength, building design, and damage levels to engineer protective solutions.")
    ],
    "cast_items": [
        "Describe how natural hazards like earthquakes affect human communities",
        "Compare multiple engineering solutions designed to reduce earthquake damage",
        "Use evidence to explain why flexible buildings survive earthquakes better than stiff buildings"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Two buildings experience the same earthquake. Building A is made of stiff concrete with no flexibility. Building B has a steel frame with cross-bracing that allows it to sway. Which building is more likely to survive, and why?"),
        ("Constructed Response:", "Describe two different engineering solutions that help buildings survive earthquakes. Explain how each one works to reduce damage.")
    ],
    "background_intro": "Earthquake engineering is one of the most important applications of science to human safety. Engineers cannot prevent earthquakes, but they have developed remarkable technologies that allow buildings to survive even the most powerful shaking.",
    "background_sections": [
        ("How Earthquakes Damage Buildings", "Earthquakes damage buildings through ground shaking, which causes structures to vibrate. If the shaking frequency matches the building's natural frequency (resonance), the vibrations amplify dramatically. Stiff, rigid buildings tend to crack and crumble because they resist the movement. The most dangerous situation is when heavy concrete buildings on soft soil experience a strong earthquake — the soft soil amplifies the shaking."),
        ("Flexible Design Philosophy", "Modern earthquake engineering follows the principle that buildings should bend, not break. Steel-frame buildings with cross-bracing can sway several feet during an earthquake and return to their original position. This flexibility absorbs the earthquake's energy gradually rather than resisting it rigidly. Think of it like a palm tree in a hurricane — it bends with the wind and survives, while a stiff oak might snap."),
        ("Base Isolation Technology", "Base isolation is one of the most effective earthquake protection technologies. The building sits on special rubber and steel pads (isolators) that allow the foundation to move with the ground while the building above stays relatively still. During an earthquake, the ground may move several inches, but the building barely moves. This technology is used in hospitals, museums, and critical infrastructure worldwide."),
        ("Real-World Success Stories", "Japan's Yokohama Landmark Tower (296m tall) uses a combination of base isolation and active dampers to survive earthquakes. During the 2011 magnitude 9.0 earthquake, buildings designed with modern seismic technology performed remarkably well while older buildings suffered severe damage. Chile's building codes, updated after the 1960 magnitude 9.5 earthquake (the largest ever recorded), have saved countless lives in subsequent earthquakes.")
    ],
    "lever_L": "Students identify earthquake strength, building flexibility, and damage level as the key components of the earthquake engineering system.",
    "lever_E": "Students determine that earthquake strength positively affects damage level (stronger quake = more damage), while building flexibility negatively affects damage level (more flexibility = less damage).",
    "lever_V": "Students build a model showing how earthquake intensity interacts with building design to determine how much damage occurs.",
    "lever_Ev": "Students run scenarios comparing stiff vs flexible buildings in the same earthquake to see the dramatic difference in damage levels.",
    "lever_R": "Students add foundation depth or ground type to explore more complex factors in earthquake engineering.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with earthquake engineering imagery", "say": "Imagine the ground starts shaking right now. Would this building survive? Let us find out!", "do": "Show a quick video of earthquake shaking. Ask: What would you do if this happened?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we become earthquake engineers — people who design buildings to survive nature's most powerful force.", "do": "Have students read objectives aloud. Pre-teach flexible and base isolation.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How do buildings survive earthquakes?", "say": "Some buildings crumble in an earthquake while the building right next door stays standing. WHY?", "do": "Show before-and-after photos of earthquake damage. Ask students why some buildings survived.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We will build a model to discover the secret of earthquake-proof design.", "do": "Preview LEVER steps. Connect to the engineering design process.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for earthquake system", "say": "What determines whether a building survives or collapses?", "do": "Guide component sorting. Discuss why earthquake strength is external (we cannot control it).", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Stronger earthquake means MORE damage — positive. But more flexibility means LESS damage — negative! Engineers use that negative relationship to save lives.", "do": "Help students draw arrows. Emphasize the critical negative relationship.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let us hit a stiff building and a flexible building with the same earthquake and see what happens!", "do": "Students predict first. Run both scenarios side by side for dramatic comparison.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "Engineers cannot stop earthquakes — but they CAN stop buildings from falling down!", "do": "Lead discussion about how flexibility saves buildings. Connect to real engineering examples.", "time": "4 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Earthquake-proof structure design", "say": "Now YOU are the engineers. Build a structure that survives the shake table!", "do": "Distribute materials (craft sticks, marshmallows, tape). Groups build and test structures.", "time": "8 min"}
    ],
    "sort_reasoning": "Earthquake Strength is external because it is determined by natural forces deep underground that humans cannot control. Building Flexibility and Damage Level are internal because they are properties of the building system — flexibility is designed by engineers, and damage is the outcome of how the building responds to the earthquake.",
    "relationships": [
        ("Earthquake Strength to Damage Level", "POSITIVE (+)", "Stronger earthquakes shake the ground more violently, causing more damage to buildings. A magnitude 7 earthquake is about 30 times more powerful than a magnitude 6."),
        ("Building Flexibility to Damage Level", "NEGATIVE (-)", "More flexible buildings absorb earthquake energy by swaying instead of cracking. Increasing flexibility DECREASES damage because the building moves WITH the shaking instead of fighting it.")
    ],
    "sim_answers": [
        ("Major Quake, Stiff Building Scenario", "When Earthquake Strength is high and Building Flexibility is low, Damage Level skyrockets. The stiff building fights against the shaking and cracks under the stress. The model shows that rigidity is dangerous in an earthquake — the stiffer the building, the more likely it is to break because it cannot absorb the energy."),
        ("Major Quake, Flexible Building Scenario", "When the same high Earthquake Strength hits a building with high flexibility, Damage Level is dramatically lower. The flexible building sways with the earthquake, absorbing and dissipating the energy gradually. Comparing the two scenarios side by side shows that building design is MORE important than earthquake strength in determining survival.")
    ],
    "reflection_exemplars": [
        ("Why is a flexible building safer than a stiff building?", "A flexible building is safer because it moves WITH the earthquake instead of fighting against it. Imagine holding a stiff stick and shaking it hard — it snaps. Now imagine holding a rubber band and shaking it — it stretches and bounces but does not break. A flexible building works like the rubber band. It bends, sways, and absorbs the earthquake's energy gradually, then returns to its original shape when the shaking stops. A stiff building is like the stick — it resists the shaking until the stress becomes too much, then it cracks and crumbles."),
        ("What other natural hazards could engineers design solutions for?", "Engineers design solutions for many natural hazards! For hurricanes, they build houses with reinforced roofs and impact-resistant windows. For floods, they build levees, seawalls, and elevated homes. For tornadoes, they design underground storm shelters and reinforced safe rooms. For wildfires, they use fire-resistant building materials and create defensible space around homes. For tsunamis, they build seawalls and design buildings that can withstand wave forces. In every case, the key idea is the same as with earthquakes — you cannot stop the natural hazard, but you CAN design structures that survive it.")
    ],
    "stem_intro": "Present the challenge: A city in earthquake country needs new buildings. Your engineering team must design a structure that stays standing when the ground shakes. You will build a model, test it on a shake table, and present your design to the class.",
    "stem_concepts": [
        ("Cross-Bracing", "X-shaped supports in the walls of a building that help it resist sideways forces. Cross-bracing allows the building to flex without collapsing, like how a spider web bends in wind but does not break."),
        ("Base Isolation", "Special rubber and steel pads placed between the building and its foundation. During an earthquake, the ground moves but the building stays still because the isolators absorb the motion — like a hockey puck sliding on ice."),
        ("Dampers", "Large shock absorbers built into tall buildings that slow down the swaying motion. They work just like the shock absorbers in a car that smooth out bumps in the road, but they are much bigger and designed for earthquake forces.")
    ],
    "stem_eval": [
        ("Expert (4)", "Structure uses model evidence about flexibility, includes multiple earthquake-resistant features, survives shake table testing, and student explains WHY it worked"),
        ("Proficient (3)", "Structure includes earthquake-resistant features and survives shake table testing"),
        ("Developing (2)", "Structure shows some earthquake design thinking but does not survive testing or lacks explanation"),
        ("Beginning (1)", "Structure is incomplete or does not demonstrate understanding of earthquake engineering principles")
    ],
    "support": [
        "Provide photos and diagrams of real earthquake engineering features (cross-bracing, base isolators, dampers)",
        "Do a hands-on demo: shake a rigid block of clay vs a flexible structure of straws — which survives?",
        "Sentence frames: 'When earthquake strength increases, damage level __ because __'"
    ],
    "extensions": [
        "Research the 2011 Japan earthquake and find out how modern buildings performed vs older buildings",
        "Design an earthquake early warning system for a school — what would it include and how would it work?",
        "Build two different model structures and test them on a shake table to compare flexible vs stiff designs"
    ],
    "cross_curr": [
        ("Math", "Measure and compare the sway distance of different model structures during shake table tests, and graph the results"),
        ("ELA", "Write a safety manual for families living in earthquake zones, explaining what to do before, during, and after an earthquake"),
        ("Art", "Design a poster showing the cross-section of an earthquake-proof building with labels explaining each safety feature")
    ],
    "misconceptions": [
        ("Earthquakes destroy all buildings equally", "Building design is the biggest factor in whether a structure survives an earthquake. In the same earthquake, a poorly designed building might collapse while a well-designed one next door suffers no damage. Modern earthquake engineering can make buildings that survive even the strongest earthquakes. Japan, Chile, and California have proven this with decades of building code improvements.", "Show photos from the same earthquake where modern buildings survived and older buildings collapsed side by side. Design matters more than earthquake strength."),
        ("The strongest building is the stiffest building", "This is the opposite of what earthquake engineering teaches. Stiff buildings are actually MORE dangerous in earthquakes because they resist the shaking until they break catastrophically. Flexible buildings that sway with the earthquake absorb the energy gradually and survive. Think of a palm tree vs an oak in a hurricane — the palm bends and survives, the oak can snap.", "Demo with two pencils: try to shake a wooden pencil (it stays rigid until it snaps) vs a flexible straw (it bends in all directions but never breaks). Which one would you want your building to be like?"),
        ("We cannot do anything about earthquakes", "While we cannot prevent earthquakes, we have enormous power to reduce their impact. Better building codes, earthquake-resistant design, early warning systems, emergency preparedness plans, and community education have saved millions of lives. Countries with strong building codes (Japan, Chile, New Zealand) experience far fewer earthquake deaths than countries without them, even from stronger earthquakes.", "Compare: The 2010 Haiti earthquake (magnitude 7.0) killed over 200,000 people. The 2010 Chile earthquake (magnitude 8.8 — nearly 500 times more powerful) killed about 500 people. Why? Chile had modern building codes. Engineering saves lives.")
    ]
}

L10 = {
    "id": "G04-L10",
    "title": "Why Do Marbles Crash and Bounce?",
    "subtitle": "The Surprising Science of Energy in Collisions",
    "ngss": "4-PS3-3",
    "ngss_desc": "Ask questions and predict outcomes about the changes in energy that occur when objects collide.",
    "big_question": "When two marbles crash into each other, where does the energy go?",
    "objectives": [
        "Explain how the speed of a marble affects how much energy it has when it collides",
        "Model how marble speed, collision force, and energy transfer are connected",
        "Predict what happens to energy when objects of different speeds collide"
    ],
    "vocabulary": [
        ("Collision", "When two objects crash into each other and exchange energy"),
        ("Energy Transfer", "When energy moves from one object to another during a collision"),
        ("Force", "A push or pull that can make an object start moving, stop, speed up, or change direction"),
        ("Momentum", "The combination of how heavy an object is and how fast it is moving — heavier and faster means more momentum")
    ],
    "components": [
        ("Marble Speed", "How fast the marble is rolling before it hits another marble — faster means more energy", True),
        ("Collision Force", "How strong the impact is when two marbles crash into each other", False),
        ("Energy Transfer", "How much energy moves from the moving marble to the marble it hits", False)
    ],
    "think_about_it": "When marble speed increases, what happens to collision force? When collision force increases, what happens to energy transfer?",
    "scenarios": [
        ("Gentle Tap", "Set Marble Speed to low and observe collision force and energy transfer"),
        ("Fast Roll", "Lock Marble Speed to high and observe what happens to the marble that gets hit"),
        ("Speed Comparison", "Run low speed and high speed side by side and compare energy transfer amounts")
    ],
    "sim_scenarios": [
        ("Gentle Tap", "Low marble speed", "What do you predict will happen to the other marble when it gets tapped gently?"),
        ("Fast Roll", "High marble speed", "What do you predict will happen to the collision force and energy transfer when a fast marble hits a still one?"),
        ("Speed Comparison", "Compare low and high speed collisions", "What do you predict will be different about the energy transferred in a slow collision vs a fast one?")
    ],
    "discoveries": [
        "Faster-moving marbles have more energy and create stronger collisions",
        "When a moving marble hits a still marble, energy transfers — the moving one slows down and the still one starts moving",
        "Energy is never lost in a collision — it just moves from one object to another (and some becomes sound and heat)",
        "The speed of the second marble after the collision depends on how much energy was transferred"
    ],
    "answer": "When marbles crash, energy transfers from the moving marble to the one it hits! The first marble slows down (loses energy) while the second marble starts moving (gains energy). The faster the first marble was rolling, the more energy gets transferred and the faster the second marble shoots away. Some energy also turns into the sound you hear (the click!) and a tiny bit of heat.",
    "stem_title": "Design the Ultimate Marble Run",
    "stem_mission": "Design a marble run course that uses collisions to move marbles through a series of obstacles and hit a target at the end.",
    "stem_scenario": "A toy company is holding a design competition for the best marble run. Your engineering team needs to design a course where one marble starts at the top and uses collisions to transfer energy through multiple marbles to hit a target cup at the end. The most accurate and creative design wins!",
    "stem_questions": [
        "How will you use hill height to control the speed and energy of your first marble?",
        "How many marbles will be involved in your collision chain, and how will you line them up?",
        "What happens if you change the starting height — does the marble at the end go farther?"
    ],
    "stem_design_qs": [
        "What materials will you use to build your marble run track?",
        "How high will your starting ramp be to give the first marble enough energy?",
        "How will you aim the collisions so energy transfers in the right direction?",
        "How will you test and improve your design after each attempt?"
    ],
    "career": "Mechanical Engineers and Crash Safety Scientists use the science of collisions to design safer cars, better sports equipment, and more efficient machines. They earn $65,000–$120,000/year.",
    "images": {
        "cover": ("cover-collisions.png", "A dramatic high-speed close-up photograph of colorful glass marbles colliding on a smooth surface, frozen in the moment of impact with one marble flying away, crisp detail, cinematic lighting"),
        "landscape": ("landscape-collisions.png", "A diverse group of 4th grade students (9-10 years old, 70-80% Black and Brown children with realistic coils, curls, locs, braids) excitedly watching marbles collide on a classroom table, pointing and cheering, bright modern classroom, photorealistic"),
        "modeling": ("modeling-collisions.png", "A diverse group of 4th grade students (9-10 years old, Black and Brown children centered) working on laptops building a digital collision model, modern classroom with physics posters, natural light, photorealistic"),
        "discussion": ("discussion-collisions.png", "A teacher demonstrating marble collisions on a track to engaged 4th grade students (9-10 years old, diverse with Black and Brown children centered, realistic hair details), students leaning in with excitement, bright classroom, photorealistic"),
        "stem": ("stem-marble-run.png", "4th grade students (9-10 years old, diverse multicultural group with Black children centered) building elaborate marble runs with cardboard tubes, ramps, and tracks on classroom tables, testing collisions, excited collaborative engineering, photorealistic")
    },
    "pre_assessment": [
        "What happens when you roll a marble into another marble that is sitting still?",
        "Does a fast marble or a slow marble make a bigger crash? Why?",
        "Where does the energy go when two things bump into each other?",
        "Draw what you think happens when a fast marble hits a still marble."
    ],
    "extend_components": [
        ("Marble Size", "Bigger, heavier marbles have more momentum and transfer more energy in collisions"),
        ("Surface Friction", "Rough surfaces slow marbles down and reduce the energy available for collision"),
        ("Angle of Impact", "Head-on collisions transfer more energy than glancing collisions that just barely touch")
    ],
    "reflections": [
        "Why does the first marble slow down after hitting the second marble?",
        "If energy cannot be created or destroyed, where does the click sound come from during a marble collision?",
        "How are marble collisions similar to what happens when a baseball bat hits a ball?",
        "What would happen if you rolled two marbles at each other at the same speed?",
        "How does your model help explain what happens in car crashes?"
    ],
    "dimensions": [
        ("Science Practice", "Asking Questions and Defining Problems", "Students ask questions about what happens to energy during collisions and predict outcomes before testing with their model."),
        ("Disciplinary Core Idea", "PS3.B Conservation of Energy and Energy Transfer", "Energy is present whenever there are moving objects, sound, light, or heat. When objects collide, energy can be transferred from one object to another."),
        ("Crosscutting Concept", "Energy and Matter", "Students track how energy moves from one marble to another during collisions, understanding that energy is transferred, not created or destroyed.")
    ],
    "cast_items": [
        "Predict what will happen to the energy of two objects when they collide",
        "Describe how the speed of a moving object relates to the energy it has",
        "Explain where the energy goes when a moving object hits a stationary object"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A fast-rolling marble hits a marble that is sitting still. After the collision, the first marble slows down and the second marble starts moving. Which best explains what happened to the energy?"),
        ("Constructed Response:", "Two students each roll a marble toward a target. Student A rolls slowly and Student B rolls quickly. Explain what will be different about how each marble hits the target, using the words energy and speed in your answer.")
    ],
    "background_intro": "The science of collisions is fundamental to understanding how energy works in the physical world. From billiard balls to car crashes to particle physics, collisions reveal the basic rules that govern how energy moves between objects.",
    "background_sections": [
        ("Energy in Motion", "Any moving object has kinetic energy — the energy of motion. The amount of kinetic energy depends on two things: the object's mass (how heavy it is) and its speed. Doubling the speed of an object QUADRUPLES its kinetic energy (energy is proportional to speed squared). This is why high-speed car crashes are so much more dangerous than low-speed ones — a car going 60 mph has four times the kinetic energy of one going 30 mph."),
        ("Types of Collisions", "There are two main types of collisions. In an elastic collision (like billiard balls), the objects bounce apart and kinetic energy is conserved — the total kinetic energy before and after is the same. In an inelastic collision (like a car crash), some kinetic energy is converted to other forms — heat, sound, and deformation. Most real-world collisions are partially inelastic."),
        ("Conservation of Energy", "The law of conservation of energy states that energy cannot be created or destroyed — only transformed from one type to another. In a marble collision, the kinetic energy of the moving marble transfers to the stationary marble. Some energy also converts to sound (the click you hear) and a tiny amount of heat (from friction). If you add up all the energy after, it equals the energy before."),
        ("Real-World Applications", "Understanding collisions is critical for car safety engineering (crumple zones absorb collision energy), sports equipment design (helmets, golf clubs, baseball bats), and even space science (spacecraft use gravity-assist maneuvers that are essentially collisions with a planet's gravitational field). Newton's Cradle — the classic desk toy with swinging metal balls — perfectly demonstrates energy transfer through collisions.")
    ],
    "lever_L": "Students identify marble speed, collision force, and energy transfer as the key components of the collision system.",
    "lever_E": "Students determine that marble speed positively affects collision force (faster marble = stronger collision), and collision force positively affects energy transfer (stronger collision = more energy moves to the second marble).",
    "lever_V": "Students build a model showing how the speed of a rolling marble determines the force of collision and how much energy transfers to the marble it hits.",
    "lever_Ev": "Students run gentle tap and fast roll scenarios to observe how speed dramatically changes the collision outcome.",
    "lever_R": "Students add marble size or surface friction to explore more complex collision dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with marble collision imagery", "say": "Everyone has played with marbles. But have you ever wondered — what ACTUALLY happens when they crash?", "do": "Roll two marbles together on a desk and let students observe. Ask: Where did the energy go?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are going to figure out the secret science behind every crash, bounce, and bump.", "do": "Have students read objectives aloud. Pre-teach collision and energy transfer.", "time": "2 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Where does the energy go in a collision?", "say": "When a moving marble hits a still marble and the still one shoots away — where did THAT energy come from?", "do": "Quick demonstration with marbles. Have students describe what they see.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We will build a model to understand exactly what happens to energy in a collision.", "do": "Preview LEVER steps. Connect to marble play experiences.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for collision system", "say": "What determines how hard marbles crash and how much energy moves between them?", "do": "Guide component sorting. Discuss why marble speed is the starting input.", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Faster marble means bigger crash. Bigger crash means more energy moves. Both positive!", "do": "Help students draw arrows. Both relationships in this system are positive.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let us crash some marbles! First predict, then test with our model.", "do": "Students predict, then run scenarios. Compare gentle tap vs fast roll side by side.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "Energy is never created or destroyed — it just moves from one marble to another!", "do": "Lead discussion about conservation of energy. Connect to real-world examples.", "time": "4 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Marble run design challenge", "say": "Now design the ultimate marble run where collisions transfer energy to hit a target!", "do": "Distribute materials. Groups design and test marble run collision courses.", "time": "8 min"}
    ],
    "sort_reasoning": "Marble Speed is external because it is set by the student before the collision — how hard they push or how high the ramp is. Collision Force and Energy Transfer are internal because they are determined by the marble's speed at the moment of impact and cannot be controlled separately.",
    "relationships": [
        ("Marble Speed to Collision Force", "POSITIVE (+)", "A faster marble has more kinetic energy, which produces a stronger collision force when it hits another marble. Doubling the speed actually quadruples the energy."),
        ("Collision Force to Energy Transfer", "POSITIVE (+)", "A stronger collision transfers more energy from the moving marble to the stationary marble. The harder the crash, the faster the second marble shoots away.")
    ],
    "sim_answers": [
        ("Fast Roll Scenario", "When Marble Speed is set to high, Collision Force increases dramatically and Energy Transfer is also very high. The stationary marble shoots away quickly, while the moving marble slows down significantly. The model shows that speed is the key factor — a marble going twice as fast transfers much more energy because kinetic energy increases with the square of speed."),
        ("Speed Comparison", "Comparing low and high speed collisions side by side reveals a dramatic difference. The slow marble gently nudges the stationary marble, which barely moves. The fast marble creates a strong collision that sends the stationary marble flying. The model clearly shows that the relationship between speed and energy is not linear — a small increase in speed creates a much larger increase in energy transfer.")
    ],
    "reflection_exemplars": [
        ("Why does the first marble slow down?", "The first marble slows down because it gave some of its energy to the second marble. Energy cannot be created — it can only move from one place to another. Before the collision, the first marble had all the kinetic energy and the second marble had none. After the collision, the energy is shared between them. The first marble has less energy (so it moves slower) and the second marble has gained energy (so it starts moving). It is like sharing candy — if you give some away, you have less."),
        ("Where does the click sound come from?", "The clicking sound during a marble collision IS energy! When the marbles crash, most of the kinetic energy transfers from one marble to the other. But a small amount of that energy converts into sound waves — the click you hear. Another tiny bit converts to heat from the friction of the impact (though you cannot feel it because it is so small). This is the law of conservation of energy in action — the total energy before the collision equals the total energy after, including the sound and heat.")
    ],
    "stem_intro": "Present the challenge: A toy company wants a marble run that uses collisions to transfer energy through a chain of marbles to hit a target cup at the end. Your team must design the track, test it, and prove that energy transfers predict the outcome.",
    "stem_concepts": [
        ("Newton's Cradle", "The famous desk toy with hanging metal balls demonstrates perfect energy transfer through collisions. When one ball swings in and hits the row, the energy passes through all the balls and the last one swings out at the same speed. Energy is conserved throughout the chain."),
        ("Kinetic Energy Formula", "The energy of a moving object depends on both its mass and speed. A heavier marble has more energy at the same speed, and a faster marble has more energy at the same mass. Speed matters MORE than mass because energy is proportional to speed squared."),
        ("Crumple Zones", "Car engineers use the science of collisions to save lives. They design cars with crumple zones — areas that crush on purpose during a crash to absorb energy gradually. This means less energy reaches the passengers inside. The crumpling converts kinetic energy into the energy of bending metal, protecting the people inside.")
    ],
    "stem_eval": [
        ("Expert (4)", "Marble run uses model evidence about speed and energy, includes multiple collision points, hits the target consistently, and student explains the energy transfer at each collision"),
        ("Proficient (3)", "Marble run includes collisions that transfer energy and hits the target, with basic explanation"),
        ("Developing (2)", "Marble run has collisions but does not consistently hit the target or lacks energy transfer explanation"),
        ("Beginning (1)", "Marble run is incomplete or does not demonstrate understanding of energy transfer in collisions")
    ],
    "support": [
        "Provide marbles and a simple ramp to let students physically experience collisions before modeling",
        "Use slow-motion video of marble collisions so students can see the energy transfer happen",
        "Sentence frames: 'When marble speed increases, collision force __ because __'"
    ],
    "extensions": [
        "Research how car crumple zones use collision science to save lives and create a poster explaining the design",
        "Experiment with marbles of different sizes — does a big marble transfer more energy than a small one?",
        "Build a Newton's Cradle from hanging marbles and explain how energy transfers through the chain"
    ],
    "cross_curr": [
        ("Math", "Measure the distance the second marble rolls after different speed collisions, create a data table, and graph the results to show the relationship between speed and energy"),
        ("ELA", "Write a step-by-step explanation of what happens to energy during a marble collision, using vocabulary from the lesson, for a student one grade below you"),
        ("Art", "Create a stop-motion animation or comic strip showing energy transferring between marbles during a collision, with energy shown as a glowing color that moves between objects")
    ],
    "misconceptions": [
        ("Energy disappears when things stop moving", "Energy NEVER disappears. When a marble stops, its kinetic energy has been transferred to other marbles, converted to sound (the click), converted to heat (from friction), or absorbed by the surface it is rolling on. If you add up ALL the forms of energy after a collision, the total is exactly the same as before. This is one of the most important laws in all of science — the conservation of energy.", "Clap your hands hard. Your hands get warm! The energy of motion (kinetic) became heat (thermal) energy. Energy did not disappear — it changed form."),
        ("Heavier objects always win in collisions", "While heavier objects have more momentum at the same speed, the outcome of a collision depends on BOTH mass and speed. A small, fast marble can transfer more energy than a large, slow marble because kinetic energy increases with the SQUARE of speed. Doubling speed quadruples the energy, but doubling mass only doubles the energy. Speed matters more!", "Compare: a fast-moving ping pong ball vs a slow-moving bowling ball. Which has more energy? It depends on HOW fast the ping pong ball is going!"),
        ("Collisions only happen between solid objects", "Collisions happen between ALL types of matter — including liquids and gases. When wind hits a sail, that is a collision between air molecules and fabric. When a raindrop hits a puddle, that is a liquid-liquid collision. Even light can collide with matter (that is how solar panels work). The science of energy transfer in collisions applies everywhere, not just to marbles and balls.", "Ask: Have you ever felt the wind push you? That is billions of air molecules colliding with your body and transferring their energy to you.")
    ]
}

ALL_LESSONS = [L01, L02, L03, L04, L05, L06, L07, L08, L09, L10]
