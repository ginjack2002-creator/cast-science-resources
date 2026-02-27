#!/usr/bin/env python3
"""Complete lesson data for GK-L01 through GK-L10 (Kindergarten ModelIt! Lessons)"""

L01 = {
    "id": "GK-L01",
    "title": "Why Do Things Fall Down?",
    "subtitle": "The Science of Gravity and Falling",
    "ngss": "K-PS2-1",
    "ngss_desc": "Plan and conduct an investigation to compare the effects of different strengths or different directions of pushes and pulls on the motion of an object.",
    "big_question": "Why do things always fall down when you let go of them?",
    "objectives": [
        "Observe what happens when objects are dropped from different heights",
        "Describe how gravity pulls everything down toward the ground",
        "Explain how dropping from higher up makes things fall faster"
    ],
    "vocabulary": [
        ("Gravity", "An invisible pull that makes things fall down toward the ground"),
        ("Force", "A push or a pull that makes things move or stop")
    ],
    "components": [
        ("Drop Height", "How high up you hold the ball before letting go", True),
        ("Fall Speed", "How fast the ball falls down to the ground", False)
    ],
    "think_about_it": "When you drop a ball from higher up, does it fall faster or slower?",
    "scenarios": [
        ("Low Drop", "Drop the ball from your knees and watch how fast it falls"),
        ("High Drop", "Drop the ball from above your head and watch how fast it falls")
    ],
    "sim_scenarios": [
        ("Low Drop", "Drop Height set to low", "What will happen to Fall Speed when we drop from low?"),
        ("High Drop", "Drop Height set to high", "What will happen to Fall Speed when we drop from high?")
    ],
    "discoveries": [
        "Gravity pulls everything down toward the ground",
        "When you drop something from higher up, it falls faster",
        "Gravity never stops — it is always pulling things down"
    ],
    "answer": "Things fall down because of GRAVITY! Gravity is an invisible force that pulls everything toward the ground. When you hold a ball up high and let go, gravity pulls it down. The higher you hold it, the faster it goes when it hits the ground because gravity has more time to pull on it!",
    "stem_title": "Build a Ball Drop Tower",
    "stem_mission": "Build a tower and test dropping balls from different levels to see how height changes how fast they fall.",
    "stem_scenario": "Your class has been asked to help build a fun new ball drop game for the school fair! You need to figure out which drop height makes the ball bounce the highest when it lands. Use what you learned about gravity to design the best drop.",
    "stem_questions": [
        "Which drop height made the ball bounce the highest?",
        "Why do you think a higher drop makes a bigger bounce?"
    ],
    "stem_design_qs": [
        "How many levels will your tower have?",
        "How will you make sure the ball drops straight down?",
        "How will you tell which drop made the biggest bounce?"
    ],
    "career": "Astronauts study gravity in space where things float because there is less gravity pulling on them. They earn $66,000-$144,000/year.",
    "images": {
        "cover": ("cover-gravity.png", "A colorful rubber ball frozen in mid-air above a grassy playground, dramatic angle looking up, bright blue sky with fluffy clouds, cinematic lighting"),
        "landscape": ("landscape-gravity.png", "Diverse kindergarten students (5-6 years old, wide variety of ethnicities including White, Black, Latino, Asian, and mixed-race children) dropping balls from different heights in a bright modern classroom with big windows and colorful rugs"),
        "modeling": ("modeling-gravity.png", "A simple, colorful kid-friendly diagram showing a ball at two different heights with big arrows pointing down labeled 'gravity', bright primary colors, cartoon-style, white background, bold outlines, easy to understand"),
        "discussion": ("discussion-gravity.png", "A Black female teacher sitting in a circle with diverse kindergarteners (5-6 years old, wide variety of ethnicities) on a colorful rug, discussing gravity with balls and toys scattered around them, warm natural light"),
        "stem": ("stem-gravity.png", "Diverse kindergarteners (5-6 years old, wide mix of ethnicities) building block towers and dropping balls from different heights, excited faces, bright collaborative classroom with colorful materials")
    },
    "pre_assessment": [
        "What happens when you let go of a ball? (Circle: it falls down / it floats up)",
        "Draw something falling down from the sky."
    ],
    "dimensions": [
        ("Science Practice", "Planning and Carrying Out Investigations", "Students plan a simple drop test to compare what happens when a ball is dropped from low versus high."),
        ("Disciplinary Core Idea", "PS2.A Forces and Motion", "Pushes and pulls can have different strengths and directions. Gravity is a pull that acts on all objects near Earth, pulling them downward."),
        ("Crosscutting Concept", "Cause and Effect", "Students observe that changing the drop height (cause) changes how fast the ball falls (effect).")
    ],
    "background_intro": "Gravity is one of the most important forces in the universe. It keeps our feet on the ground, makes rain fall from clouds, and holds the Moon in orbit around Earth.",
    "background_sections": [
        ("What Is Gravity?", "Gravity is a force — an invisible pull — that attracts objects toward each other. On Earth, gravity pulls everything toward the center of the planet. This is why when you jump, you come back down. When you drop a ball, it falls to the floor. Gravity is always pulling on us, even though we cannot see it."),
        ("Why Things Fall at Different Speeds", "When an object is held up high and released, gravity pulls it downward. The higher the starting point, the longer gravity has to pull on the object, so it reaches a faster speed before hitting the ground. In a vacuum (with no air), all objects fall at the same rate regardless of weight. In air, lighter objects like feathers fall more slowly because air resistance pushes against them.")
    ],
    "lever_L": "Students identify Drop Height as the external component (we choose how high to hold it) and Fall Speed as the internal component (it changes on its own based on height).",
    "lever_E": "Students discover that higher Drop Height leads to faster Fall Speed — a positive relationship.",
    "lever_V": "Students build a simple two-part model connecting Drop Height to Fall Speed with a positive arrow.",
    "lever_Ev": "Students test Low Drop vs. High Drop scenarios and observe the speed difference.",
    "lever_R": "Students explore what happens when they drop different objects (heavy ball, light ball, feather) from the same height.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with a colorful ball in mid-air and the big question", "say": "Have you ever dropped something? What happened? Today we are going to find out WHY things fall down!", "do": "Hold up a ball and drop it. Ask: What just happened? Why did it go DOWN and not UP?", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn?", "visual": "Learning goals with picture icons", "say": "Today we will learn about an invisible force called gravity! Gravity is what makes everything fall down.", "do": "Introduce the word 'gravity.' Have kids say it together three times. Do a gesture: hands up, then pull down.", "time": "3 min"},
        {"num": "Slide 3", "title": "Let's Be Scientists!", "visual": "Big question with a picture of a falling ball", "say": "Scientists ask questions and do experiments to find answers. Our big question is: Why do things ALWAYS fall DOWN?", "do": "Pair-share: Ask a friend what they think. Give 30 seconds, then ask two students to share.", "time": "3 min"},
        {"num": "Slide 4", "title": "What Are the Parts?", "visual": "Two component cards: Drop Height and Fall Speed", "say": "Our model has two parts. Drop Height is how high we hold the ball — WE get to decide that! Fall Speed is how fast the ball falls — that happens all by itself.", "do": "Use sorting mats. Students place Drop Height on the OUTSIDE and Fall Speed on the INSIDE. Act it out: hold ball high, hold ball low.", "time": "5 min"},
        {"num": "Slide 5", "title": "How Are They Connected?", "visual": "Arrow diagram showing Drop Height leading to Fall Speed", "say": "When Drop Height goes UP, what happens to Fall Speed? Does the ball fall faster or slower? That means it is a POSITIVE connection!", "do": "Demonstrate with a real ball: drop from knee height, then from above your head. Students point thumbs up for positive connection.", "time": "5 min"},
        {"num": "Slide 6", "title": "What Did We Find Out?", "visual": "Key discoveries with simple illustrations", "say": "We found out that gravity pulls EVERYTHING down! And when we drop from higher up, it falls FASTER. That is gravity at work!", "do": "Students say: 'When Drop Height goes up, Fall Speed goes up!' Clap it out like a chant. Fill in the sentence frame together.", "time": "5 min"},
        {"num": "Slide 7", "title": "STEM Challenge", "visual": "Ball Drop Tower challenge with materials list", "say": "Now YOU get to be engineers! Build a tower and test dropping balls from different levels. Which level makes the biggest bounce?", "do": "Distribute blocks, cups, and soft balls. Groups build towers with 2-3 levels and test drops. Record with smiley faces (small bounce, medium bounce, big bounce).", "time": "10 min"}
    ],
    "sort_reasoning": "Drop Height is outside because WE decide how high to hold the ball. Fall Speed is inside because it changes on its own based on how high we drop from.",
    "relationships": [
        ("Drop Height to Fall Speed", "POSITIVE (+)", "When you drop from higher up, the ball falls faster because gravity pulls it for a longer time.")
    ],
    "sim_answers": [
        ("Low Drop", "When Drop Height is low, Fall Speed is slow. The ball barely picks up speed before it hits the ground."),
        ("High Drop", "When Drop Height is high, Fall Speed is fast. The ball has more time to speed up as gravity pulls it!")
    ],
    "stem_intro": "In this challenge, students apply their understanding of gravity and drop height to build a simple tower and test how height affects bouncing. This connects directly to their model showing that greater Drop Height leads to greater Fall Speed.",
    "stem_concepts": [
        ("Gravity and Height", "The higher an object starts, the faster it will be moving when it reaches the ground because gravity accelerates it over a greater distance."),
        ("Energy Transfer", "When a ball hits the ground moving fast, some of that energy makes it bounce back up higher — connecting height, speed, and bounce.")
    ],
    "stem_eval": [
        ("Expert (4)", "Student builds a stable tower with multiple levels, tests drops from each level, and clearly explains that higher drops make bigger bounces because of gravity."),
        ("Proficient (3)", "Student builds a tower, tests drops from at least two levels, and states that higher drops make bigger bounces."),
        ("Developing (2)", "Student builds a tower and drops a ball but needs help connecting height to bounce size."),
        ("Beginning (1)", "Student participates in building but does not yet connect drop height to bounce results.")
    ],
    "support": [
        "Provide hand-over-hand guidance for the drop test — teacher holds student's hand at each height",
        "Use only two heights (low and high) instead of three to simplify comparisons",
        "Offer picture cards showing 'high' and 'low' with matching 'fast' and 'slow' labels"
    ],
    "extensions": [
        "Try dropping different objects (cotton ball, block, crumpled paper) from the same height — do they all fall the same?",
        "Count how many seconds each drop takes using a slow count (one-Mississippi, two-Mississippi)",
        "Draw a picture showing what would happen if there were no gravity — would the ball float away?"
    ],
    "cross_curr": [
        ("Math", "Compare heights using words like taller, shorter, higher, lower — early measurement concepts"),
        ("ELA", "Read aloud 'I Fall Down' by Vicki Cobb and discuss the vocabulary word gravity"),
        ("Art", "Create a gravity painting by dripping paint from different heights onto paper and comparing splatter sizes")
    ],
    "misconceptions": [
        ("Heavy things fall faster than light things", "In air, heavy and light objects fall at almost the same speed. A bowling ball and a soccer ball dropped together land at nearly the same time. Air resistance (not weight) is what makes feathers float slowly.", "Drop two different-weight balls side by side to show they land at the same time. Then drop a feather to discuss air pushing against it."),
        ("Gravity only works when you drop something", "Gravity is always pulling on everything, all the time — even when things are sitting still on a table. The table pushes back up to keep things from falling through.", "Place a book on a table and ask: Is gravity pulling on this book right now? Yes! The table is holding it up. Remove the table (slide book off edge) and gravity wins.")
    ],
    "sentence_frame": "When Drop Height goes up, Fall Speed goes _______.",
    "coloring_description": "Color the ball at the top of the picture and at the bottom. Trace the arrow showing gravity pulling the ball down!"
}

L02 = {
    "id": "GK-L02",
    "title": "What Makes Things Move?",
    "subtitle": "Pushes and Pulls All Around Us",
    "ngss": "K-PS2-2",
    "ngss_desc": "Analyze data to determine if a design solution works as intended to change the speed or direction of an object with a push or a pull.",
    "big_question": "What makes a toy car start moving across the floor?",
    "objectives": [
        "Show that pushes make things move away from you and pulls bring things closer",
        "Observe how a bigger push makes a toy car go farther",
        "Describe pushes and pulls as forces that change how things move"
    ],
    "vocabulary": [
        ("Push", "A force that moves something away from you"),
        ("Pull", "A force that brings something closer to you"),
        ("Force", "A push or a pull that can make things move, stop, or change direction")
    ],
    "components": [
        ("Push Strength", "How hard you push the toy car — a gentle tap or a big shove", True),
        ("Distance Traveled", "How far the toy car rolls across the floor", False)
    ],
    "think_about_it": "When you push a toy car harder, does it go farther or not as far?",
    "scenarios": [
        ("Gentle Push", "Give the toy car a tiny, soft push and watch how far it goes"),
        ("Big Push", "Give the toy car a strong, big push and watch how far it goes")
    ],
    "sim_scenarios": [
        ("Gentle Push", "Push Strength set to low", "What will happen to Distance Traveled when we give a gentle push?"),
        ("Big Push", "Push Strength set to high", "What will happen to Distance Traveled when we give a big push?")
    ],
    "discoveries": [
        "A bigger push makes the car go farther across the floor",
        "A tiny push makes the car go only a little bit",
        "Pushes and pulls are forces — they make things start moving, stop, or change direction"
    ],
    "answer": "Things move because of FORCES! A force is a push or a pull. When you push a toy car, your hand gives it a force that makes it roll. The harder you push, the farther it goes! Pulls work too — when you pull a wagon, it moves toward you. Everything that moves was pushed or pulled by something!",
    "stem_title": "Design a Push-Powered Racer",
    "stem_mission": "Build a ramp and test how different push strengths make a toy car travel different distances.",
    "stem_scenario": "The school is holding a Toy Car Race Day! Your team needs to figure out exactly how hard to push your car so it stops right on the finish line — not too far and not too short. Use what you learned about push strength to win!",
    "stem_questions": [
        "How hard should you push to make your car stop on the finish line?",
        "What happened when you pushed too hard? Too soft?"
    ],
    "stem_design_qs": [
        "Where will you put your finish line?",
        "How will you make sure you push the same way each time?",
        "How will you measure how far the car goes?"
    ],
    "career": "Car Engineers design how cars move, stop, and steer safely. They use pushes and pulls every day to make cars work! They earn $65,000-$105,000/year.",
    "images": {
        "cover": ("cover-push-pull.png", "A bright red toy car mid-motion on a smooth wooden floor, motion blur showing speed, colorful kindergarten classroom background, eye-level dramatic angle"),
        "landscape": ("landscape-push-pull.png", "Diverse kindergarten students (5-6 years old, wide variety of ethnicities including White, Black, Latino, Asian, and mixed-race children) pushing toy cars across a smooth floor in a bright modern classroom, natural light, joyful expressions"),
        "modeling": ("modeling-push-pull.png", "A simple, colorful kid-friendly diagram showing a hand pushing a toy car with a big arrow showing direction of motion, a small push with a short arrow and a big push with a long arrow, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-push-pull.png", "A Black male teacher kneeling on the floor with diverse kindergarteners (5-6 years old, wide variety of ethnicities) in a circle, demonstrating pushes and pulls with toy cars and wagons, colorful classroom rug"),
        "stem": ("stem-push-pull.png", "Diverse kindergarteners (5-6 years old, wide mix of ethnicities) racing toy cars across the floor, measuring distances with tape strips, laughing and excited, bright collaborative classroom")
    },
    "pre_assessment": [
        "Circle which one is a PUSH: (picture of pushing a door / picture of pulling a door handle)",
        "Draw yourself pushing something."
    ],
    "dimensions": [
        ("Science Practice", "Analyzing and Interpreting Data", "Students compare how far the car goes with a gentle push versus a big push, analyzing simple data about distance."),
        ("Disciplinary Core Idea", "PS2.A Forces and Motion", "Pushes and pulls can have different strengths and directions. A bigger push or pull makes things speed up more."),
        ("Crosscutting Concept", "Cause and Effect", "Students observe that changing push strength (cause) changes how far the car travels (effect).")
    ],
    "background_intro": "Forces are everywhere in our daily lives. Every time something starts moving, stops, or changes direction, a force is responsible. Understanding pushes and pulls helps young learners make sense of how the world works.",
    "background_sections": [
        ("What Are Pushes and Pulls?", "A push is a force that moves an object away from the source of the force. A pull is a force that moves an object toward the source. These are the two basic types of forces. Opening a door can be a push or a pull. Kicking a ball is a push. Dragging a backpack is a pull. Forces can be big or small, and the size of the force affects how much the object moves."),
        ("How Force Affects Motion", "The strength of a push or pull determines how much an object's motion changes. A gentle push on a toy car makes it roll slowly and stop nearby. A strong push makes it zoom across the room. This is related to Newton's Second Law of Motion — the bigger the force, the greater the acceleration. At the kindergarten level, students simply observe that 'bigger pushes make things go farther and faster.'")
    ],
    "lever_L": "Students identify Push Strength as the external component (we choose how hard to push) and Distance Traveled as the internal component (it changes based on how hard we pushed).",
    "lever_E": "Students discover that stronger Push Strength leads to greater Distance Traveled — a positive relationship.",
    "lever_V": "Students build a simple two-part model connecting Push Strength to Distance Traveled with a positive arrow.",
    "lever_Ev": "Students test Gentle Push vs. Big Push and observe the distance difference.",
    "lever_R": "Students explore what happens on different surfaces (carpet vs. tile) to see how the floor changes things.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with a toy car zooming across the floor", "say": "What makes things move? Can something start moving all by itself? Let us find out!", "do": "Place a toy car on a table. Wait. Ask: Why is it not moving? Then push it. Ask: What did I do?", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn?", "visual": "Learning goals with push/pull icons", "say": "Today we will learn about pushes and pulls! A push moves things away from you. A pull brings things toward you. Together, they are called FORCES.", "do": "Practice push gesture (hands pushing away) and pull gesture (hands pulling toward chest). Say the words together.", "time": "3 min"},
        {"num": "Slide 3", "title": "Let's Be Scientists!", "visual": "Big question with toy car picture", "say": "Our big question is: What makes a toy car start moving? Can it move by itself? What does it need?", "do": "Students turn to a partner and share one thing they push and one thing they pull every day.", "time": "3 min"},
        {"num": "Slide 4", "title": "What Are the Parts?", "visual": "Two component cards: Push Strength and Distance Traveled", "say": "Our model has two parts. Push Strength is how hard we push — WE choose that! Distance Traveled is how far the car goes — that happens on its own after we push.", "do": "Use sorting mats. Students place Push Strength OUTSIDE and Distance Traveled INSIDE. Practice gentle push and big push motions.", "time": "5 min"},
        {"num": "Slide 5", "title": "How Are They Connected?", "visual": "Arrow diagram showing Push Strength to Distance Traveled", "say": "When Push Strength goes UP, what happens to Distance Traveled? The car goes FARTHER! That is a POSITIVE connection.", "do": "Demonstrate: push car gently (short distance), push car hard (long distance). Students give a thumbs up for positive.", "time": "5 min"},
        {"num": "Slide 6", "title": "What Did We Find Out?", "visual": "Key discoveries with simple illustrations", "say": "We discovered that bigger pushes make things go farther! Pushes and pulls are called forces, and forces make everything move.", "do": "Chant together: 'When Push Strength goes up, Distance goes up!' Complete the sentence frame as a class.", "time": "5 min"},
        {"num": "Slide 7", "title": "STEM Challenge", "visual": "Push-Powered Racer with finish line", "say": "Now you are the engineers! Can you push your car so it stops RIGHT on the finish line? Not too far, not too short — just right!", "do": "Place tape finish lines at different distances. Students practice pushing with different strengths. Record results with stickers (too far, too short, just right).", "time": "10 min"}
    ],
    "sort_reasoning": "Push Strength is outside because WE decide how hard to push. Distance Traveled is inside because it changes on its own depending on how hard we pushed.",
    "relationships": [
        ("Push Strength to Distance Traveled", "POSITIVE (+)", "When you push harder, the car goes farther because a stronger force gives the car more energy to keep rolling.")
    ],
    "sim_answers": [
        ("Gentle Push", "When Push Strength is low, Distance Traveled is short. The car only rolls a tiny bit before stopping."),
        ("Big Push", "When Push Strength is high, Distance Traveled is far. The car zooms across the floor because the strong force gave it lots of energy!")
    ],
    "stem_intro": "In this challenge, students apply their understanding of push strength to control how far a toy car travels. They must calibrate their push to reach a specific finish line, connecting directly to the model showing that stronger pushes cause greater distances.",
    "stem_concepts": [
        ("Force and Distance", "A stronger push gives an object more energy, causing it to travel a greater distance before friction slows it to a stop."),
        ("Control and Precision", "Engineers must control forces carefully — too much force or too little force both cause problems in real-world designs.")
    ],
    "stem_eval": [
        ("Expert (4)", "Student consistently controls push strength to land the car near the finish line and explains that stronger pushes make it go farther."),
        ("Proficient (3)", "Student adjusts push strength between tries and gets the car close to the finish line at least once."),
        ("Developing (2)", "Student pushes the car but needs reminders to try different strengths to reach the line."),
        ("Beginning (1)", "Student pushes the car and observes it move but does not yet adjust strength purposefully.")
    ],
    "support": [
        "Place the finish line very close (1 foot away) so even a gentle push can reach it",
        "Use hand-over-hand guidance to help students feel the difference between a gentle and strong push",
        "Provide visual cue cards showing a small hand (gentle) and a big hand (strong) for push strength"
    ],
    "extensions": [
        "Try pushing on different surfaces — carpet, tile, grass — and see which lets the car go farthest",
        "Add weight to the car (tape a penny on top) and see if it still goes the same distance with the same push",
        "Test pulls by tying a string to the car and pulling gently versus hard"
    ],
    "cross_curr": [
        ("Math", "Measure distance with blocks or hands — 'The car went 5 hands far!' — early nonstandard measurement"),
        ("ELA", "Read aloud 'Forces Make Things Move' by Kimberly Brubaker Bradley and act out push/pull examples"),
        ("Art", "Create push and pull collages — cut out magazine pictures of people pushing or pulling things and sort them")
    ],
    "misconceptions": [
        ("Things move by themselves", "Nothing moves without a force acting on it. A ball rolling across the floor was pushed by someone or something. Wind, gravity, and people all provide forces.", "Place a ball on the floor and wait. Ask: Is it moving? No! Now push it. What made it move? YOUR push! Things need a force to start moving."),
        ("Heavier things are harder to push so they never go as far", "While heavier objects need more force to start moving, once in motion they can actually travel far because their weight helps them keep going. The key factor is the force applied, not just the weight.", "Push an empty box and a heavy box with the same force. The empty box moves easily. But then push the heavy box harder and show it can go far too — it just needs a bigger push!")
    ],
    "sentence_frame": "When Push Strength goes up, Distance Traveled goes _______.",
    "coloring_description": "Color the hand pushing the car. Color the car at the start and where it stops. Trace the arrow from the hand to the car!"
}

L03 = {
    "id": "GK-L03",
    "title": "Does the Sun Warm Everything the Same?",
    "subtitle": "Sunlight, Shade, and Temperature",
    "ngss": "K-PS3-1",
    "ngss_desc": "Make observations to determine the effect of sunlight on Earth's surface.",
    "big_question": "Does the sun warm a sunny spot and a shady spot the same way?",
    "objectives": [
        "Observe that sunny places feel warmer than shady places",
        "Describe how sunlight heats up the ground, rocks, and other surfaces",
        "Explain why shade keeps things cooler than direct sun"
    ],
    "vocabulary": [
        ("Sunlight", "Light and warmth that comes from the sun"),
        ("Temperature", "How hot or cold something is")
    ],
    "components": [
        ("Amount of Sunlight", "How much sun shines on a spot — full sun or full shade", True),
        ("Surface Temperature", "How warm the ground or an object feels", False)
    ],
    "think_about_it": "When there is MORE sunlight on a spot, does it get warmer or cooler?",
    "scenarios": [
        ("Shady Spot", "Feel the ground in a shady spot and notice how warm or cool it is"),
        ("Sunny Spot", "Feel the ground in a sunny spot and notice how warm or cool it is")
    ],
    "sim_scenarios": [
        ("Shady Spot", "Amount of Sunlight set to low (shade)", "What will happen to Surface Temperature when the spot is in shade?"),
        ("Sunny Spot", "Amount of Sunlight set to high (full sun)", "What will happen to Surface Temperature when the spot is in full sun?")
    ],
    "discoveries": [
        "Sunny spots feel warmer than shady spots",
        "The sun heats up the ground, sidewalks, and everything it shines on",
        "Shade blocks sunlight, which is why shady spots stay cooler",
        "Dark-colored things in the sun feel hotter than light-colored things"
    ],
    "answer": "The sun does NOT warm everything the same! Sunny spots get much warmer because sunlight carries energy that heats things up. Shady spots stay cooler because something is blocking the sunlight — like a tree, a building, or a cloud. That is why we sit in the shade on a hot day to cool off!",
    "stem_title": "Design a Shade Shelter",
    "stem_mission": "Build a small shelter that blocks sunlight and keeps a toy animal cool on a hot sunny day.",
    "stem_scenario": "It is a super hot day at the zoo, and the toy animals need to cool down! Your team must build a shelter that creates the most shade so the animals do not get too warm. Use what you learned about sunlight and shade to design the best shelter!",
    "stem_questions": [
        "How can you tell if your shelter is making good shade?",
        "Which material blocked the most sunlight?"
    ],
    "stem_design_qs": [
        "What materials will you use to block the sun?",
        "How big does your shelter need to be to cover the toy animal?",
        "How will you test if your shelter really keeps things cooler?"
    ],
    "career": "Solar Energy Scientists study how sunlight can be used to power homes and cars. They help us use the sun's energy in amazing ways! They earn $70,000-$120,000/year.",
    "images": {
        "cover": ("cover-sunlight.png", "A bright sunny day split down the middle — one side shows a golden sunny sidewalk with heat shimmer, the other side shows a cool blue-green shady area under a big tree, dramatic contrast, vivid colors"),
        "landscape": ("landscape-sunlight.png", "Diverse kindergarten students (5-6 years old, wide variety of ethnicities including White, Black, Latino, Asian, and mixed-race children) outside on a playground touching the sunny ground and shady ground, comparing with surprised expressions, bright natural light"),
        "modeling": ("modeling-sunlight.png", "A simple, colorful kid-friendly diagram showing the sun with arrows pointing down to two spots — one sunny (colored orange/warm) and one shady under a tree (colored blue/cool), cartoon-style, white background, bold outlines, thermometer icons"),
        "discussion": ("discussion-sunlight.png", "A Black female teacher outside with diverse kindergarteners (5-6 years old, wide variety of ethnicities) sitting under a tree in the shade, pointing at a sunny patch of grass nearby, warm natural lighting, engaged students"),
        "stem": ("stem-sunlight.png", "Diverse kindergarteners (5-6 years old, wide mix of ethnicities) building small shade shelters with cardboard, fabric, and craft sticks over toy animals, outdoor setting, bright sunny day, collaborative play")
    },
    "pre_assessment": [
        "Circle which spot is warmer: (picture of a sunny sidewalk / picture of a shady sidewalk)",
        "Draw the sun warming something up."
    ],
    "dimensions": [
        ("Science Practice", "Planning and Carrying Out Investigations", "Students feel and compare temperatures of sunny versus shady surfaces, collecting simple observational data."),
        ("Disciplinary Core Idea", "PS3.B Conservation of Energy and Energy Transfer", "Sunlight warms Earth's surface. The warmth felt from sunlight is energy that has been transferred from the sun to objects on Earth."),
        ("Crosscutting Concept", "Cause and Effect", "Students observe that more sunlight (cause) leads to higher surface temperature (effect).")
    ],
    "background_intro": "The sun is the primary source of energy for Earth's surface. Understanding how sunlight warms different areas helps students make sense of daily experiences like seeking shade on a hot day or noticing that metal playground equipment gets hot in the sun.",
    "background_sections": [
        ("How Sunlight Warms the Earth", "Sunlight is a form of energy called radiant energy. When sunlight hits a surface — soil, concrete, water, or any material — the light energy is absorbed and converted to thermal energy (heat). Darker surfaces absorb more light and get hotter, while lighter surfaces reflect more light and stay cooler. This is why a black car parked in the sun feels much hotter than a white car."),
        ("The Role of Shade", "Shade is created when an object blocks sunlight from reaching a surface. Trees, buildings, umbrellas, and clouds all create shade. In shaded areas, surfaces receive less direct sunlight and therefore absorb less energy, staying cooler. Shade does not make things cold — it simply reduces the amount of solar energy reaching the surface. On a 90-degree day, shaded ground might be 20-30 degrees cooler than sunlit ground.")
    ],
    "lever_L": "Students identify Amount of Sunlight as the external component (nature controls whether a spot is sunny or shady) and Surface Temperature as the internal component (it changes based on how much sun a spot gets).",
    "lever_E": "Students discover that more sunlight leads to higher Surface Temperature — a positive relationship.",
    "lever_V": "Students build a simple two-part model connecting Amount of Sunlight to Surface Temperature with a positive arrow.",
    "lever_Ev": "Students test Shady Spot vs. Sunny Spot and compare how warm each feels.",
    "lever_R": "Students explore how different materials (dark paper vs. white paper) heat up differently in the sun.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide showing a sunny/shady split scene", "say": "Have you ever walked on hot sidewalk in bare feet? OUCH! But the grass in the shade is cool. Why is that?", "do": "Show two pictures: a sunny sidewalk and a shady spot. Ask students which they would rather sit on during a hot day and why.", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn?", "visual": "Learning goals with sun and shade icons", "say": "Today we will learn how the sun warms things up! We will discover why sunny spots are warm and shady spots are cool.", "do": "Introduce the words 'sunlight' and 'temperature.' Practice together. Do a gesture: hands spread wide for sun, arms crossed for shade.", "time": "3 min"},
        {"num": "Slide 3", "title": "Let's Be Scientists!", "visual": "Big question with sun and shade photos", "say": "Our big question is: Does the sun warm a sunny spot and a shady spot the same? What do you think?", "do": "Quick vote: raise your hand if you think they are the same. Raise your hand if you think they are different.", "time": "3 min"},
        {"num": "Slide 4", "title": "What Are the Parts?", "visual": "Two component cards: Amount of Sunlight and Surface Temperature", "say": "Our model has two parts. Amount of Sunlight is how much sun shines on a spot — we can CHOOSE a sunny spot or a shady spot. Surface Temperature is how warm it feels — that changes on its own!", "do": "Use sorting mats. Students place Amount of Sunlight on OUTSIDE and Surface Temperature on INSIDE.", "time": "5 min"},
        {"num": "Slide 5", "title": "How Are They Connected?", "visual": "Arrow from Amount of Sunlight to Surface Temperature", "say": "When there is MORE sunlight, the temperature goes UP — it gets warmer! That is a POSITIVE connection. When there is LESS sunlight, temperature goes DOWN.", "do": "If possible, take students outside to touch a sunny spot and a shady spot on the ground. If indoors, use a lamp on dark paper vs. shaded paper.", "time": "5 min"},
        {"num": "Slide 6", "title": "What Did We Find Out?", "visual": "Key discoveries with warm/cool pictures", "say": "The sun does NOT warm everything the same! Sunny spots are warmer because the sun's energy heats them up. Shady spots stay cooler because something blocks the light!", "do": "Chant: 'When Sunlight goes up, Temperature goes up!' Students complete the sentence frame together.", "time": "5 min"},
        {"num": "Slide 7", "title": "STEM Challenge", "visual": "Shade Shelter challenge with materials", "say": "The toy animals are too hot! Can you build a shelter that blocks the sun and keeps them cool? Be creative engineers!", "do": "Distribute cardboard, fabric scraps, craft sticks, tape, and toy animals. Groups build shelters. Test by placing under a lamp or outside in the sun.", "time": "10 min"}
    ],
    "sort_reasoning": "Amount of Sunlight is outside because it depends on where a spot is — sunny or shady — and we choose where to test. Surface Temperature is inside because it changes on its own based on how much sun hits the spot.",
    "relationships": [
        ("Amount of Sunlight to Surface Temperature", "POSITIVE (+)", "When more sunlight shines on a spot, the surface gets warmer because light energy turns into heat energy.")
    ],
    "sim_answers": [
        ("Shady Spot", "When Amount of Sunlight is low (shade), Surface Temperature stays cool. The ground does not heat up much without the sun's energy."),
        ("Sunny Spot", "When Amount of Sunlight is high (full sun), Surface Temperature gets warm. The sun's energy heats up the ground!")
    ],
    "stem_intro": "In this challenge, students design and build shade shelters to protect toy animals from the sun's heat. This directly connects to their model showing that more sunlight leads to higher temperatures, and that blocking sunlight (creating shade) keeps things cooler.",
    "stem_concepts": [
        ("Sunlight as Energy", "Sunlight carries energy from the sun. When it hits a surface, that energy is absorbed and the surface heats up."),
        ("Shade as a Solution", "Blocking sunlight with a shelter prevents energy from reaching the surface, keeping the area underneath cooler — an engineering solution to a heat problem.")
    ],
    "stem_eval": [
        ("Expert (4)", "Student builds a stable shelter that clearly creates shade, tests it, and explains that blocking sunlight keeps the toy animal cooler."),
        ("Proficient (3)", "Student builds a shelter that creates shade and identifies that it blocks the sun from making things hot."),
        ("Developing (2)", "Student builds a structure but needs help connecting it to the idea of blocking sunlight to stay cool."),
        ("Beginning (1)", "Student participates in building but does not yet connect the shelter to sunlight and temperature.")
    ],
    "support": [
        "Provide pre-cut cardboard pieces that can easily stand up to form a simple lean-to shelter",
        "Use a desk lamp as 'the sun' so students can test indoors without needing to go outside",
        "Pair students who need support with a buddy who can help hold materials while building"
    ],
    "extensions": [
        "Test which color of paper gets hottest in the sun — place black, white, and red paper in the sun and feel them after 10 minutes",
        "Make a sun journal — check how a shady spot and sunny spot feel in the morning, at lunch, and in the afternoon",
        "Discuss why people wear hats and light-colored clothes on sunny days"
    ],
    "cross_curr": [
        ("Math", "Use simple bar graphs to show warm vs. cool — students place sun stickers on a chart to vote which spot felt warmer"),
        ("ELA", "Read aloud 'The Sun Is My Favorite Star' by Frank Asch and discuss how the sun gives us light and warmth"),
        ("Art", "Create sun prints by placing objects on dark construction paper in the sun — the covered spots stay dark while exposed paper fades")
    ],
    "misconceptions": [
        ("The sun only warms the air, not the ground", "Sunlight directly warms surfaces it touches — soil, sidewalks, rocks, and water. These warm surfaces then heat up the air above them. The ground can actually be hotter than the air on a sunny day!", "Have students touch the ground in a sunny spot. Is the ground warm? Now wave your hand in the air. The ground might feel even warmer than the air! The sun warms the ground first."),
        ("Shade means it is cold", "Shade does not make things cold — it just keeps them cooler than the sunny spots. On a hot day, the shade is still warm, just not as warm as the sun. Shade blocks the extra heat from sunlight.", "On a warm day, ask: Is the shade freezing cold or just cooler? It is still warm! Shade takes away the extra heat from the sun but does not make things cold.")
    ],
    "sentence_frame": "When Amount of Sunlight goes up, Surface Temperature goes _______.",
    "coloring_description": "Color the sun yellow. Color the sunny spot orange (warm) and the shady spot blue (cool). Draw a tree making the shade!"
}

L04 = {
    "id": "GK-L04",
    "title": "What Do Plants Need to Grow?",
    "subtitle": "Water, Light, and Happy Plants",
    "ngss": "K-LS1-1",
    "ngss_desc": "Use observations to describe patterns of what plants and animals (including humans) need to survive.",
    "big_question": "What does a plant need so it can grow big and strong?",
    "objectives": [
        "Identify that plants need water and sunlight to grow",
        "Observe that plants with more water grow taller than plants with less water",
        "Describe how water helps a plant stay healthy and grow bigger"
    ],
    "vocabulary": [
        ("Nutrients", "Good things in water and soil that help a plant grow, like food for plants"),
        ("Sunlight", "Light from the sun that plants use to make their own food")
    ],
    "components": [
        ("Amount of Water", "How much water the plant gets — a lot or a little", True),
        ("Plant Growth", "How tall and healthy the plant grows over time", False)
    ],
    "think_about_it": "When a plant gets MORE water, does it grow bigger or smaller?",
    "scenarios": [
        ("Little Water", "Give the plant only a tiny bit of water each day and watch what happens"),
        ("Lots of Water", "Give the plant a full cup of water each day and watch what happens")
    ],
    "sim_scenarios": [
        ("Little Water", "Amount of Water set to low", "What will happen to Plant Growth when the plant gets very little water?"),
        ("Lots of Water", "Amount of Water set to high", "What will happen to Plant Growth when the plant gets lots of water?")
    ],
    "discoveries": [
        "Plants that get enough water grow taller and look healthier",
        "Plants that get very little water grow slowly and can wilt or turn brown",
        "Water helps carry nutrients from the soil up into the plant so it can grow"
    ],
    "answer": "Plants need WATER to grow! Water goes into the plant through its roots and carries nutrients all through the stem and leaves — like a straw sucking up a drink! Plants that get the right amount of water grow tall and green. Plants without enough water get droopy and sad. Plants also need sunlight and soil, but water is super important!",
    "stem_title": "Design a Mini Garden",
    "stem_mission": "Plant seeds and design a watering plan that gives your plant the best chance to grow tall and healthy.",
    "stem_scenario": "Your class is growing a garden for the school! Each team gets seeds and a cup of soil. You need to figure out the best watering plan to help your plant grow the tallest. Use what you learned about water and plant growth to win the Tallest Plant Award!",
    "stem_questions": [
        "How much water will you give your plant each day?",
        "What happened to the plant that got too little water?"
    ],
    "stem_design_qs": [
        "Where will you put your plant so it gets sunlight?",
        "How will you measure how much water to give it?",
        "How will you check if your plant is growing each day?"
    ],
    "career": "Botanists are scientists who study plants — how they grow, what they need, and how to keep them healthy. They help us grow food and protect forests! They earn $50,000-$95,000/year.",
    "images": {
        "cover": ("cover-plants.png", "A bright green seedling sprouting from rich dark soil in a small pot, water droplets on the leaves, sunlight streaming in from the side, macro photography style, vivid green colors"),
        "landscape": ("landscape-plants.png", "Diverse kindergarten students (5-6 years old, wide variety of ethnicities including White, Black, Latino, Asian, and mixed-race children) watering small plants in cups at a sunlit classroom window, excited expressions, bright modern classroom"),
        "modeling": ("modeling-plants.png", "A simple, colorful kid-friendly diagram showing two plants side by side — one with lots of water drops and growing tall and green, one with few water drops and small and droopy, cartoon-style, white background, bold outlines, cheerful style"),
        "discussion": ("discussion-plants.png", "A Black male teacher sitting at a table with diverse kindergarteners (5-6 years old, wide variety of ethnicities) examining small potted plants with magnifying glasses, warm natural window light, curious engaged faces"),
        "stem": ("stem-plants.png", "Diverse kindergarteners (5-6 years old, wide mix of ethnicities) planting seeds in soil cups, watering them with small cups, drawing pictures of their plants, bright colorful classroom garden station")
    },
    "pre_assessment": [
        "Circle what a plant needs to grow: (picture of water / picture of a toy car / picture of the sun)",
        "Draw a happy, healthy plant."
    ],
    "dimensions": [
        ("Science Practice", "Planning and Carrying Out Investigations", "Students set up a simple plant growth investigation comparing different amounts of water and observing the results over time."),
        ("Disciplinary Core Idea", "LS1.C Organization for Matter and Energy Flow in Organisms", "All animals need food in order to live and grow. They obtain their food from plants or from other animals. Plants need water and light to live and grow."),
        ("Crosscutting Concept", "Cause and Effect", "Students observe that changing the amount of water (cause) changes how well the plant grows (effect).")
    ],
    "background_intro": "Plants are living organisms that need certain things from their environment to survive and grow. Understanding plant needs is foundational to biology and connects to food systems, ecology, and environmental stewardship.",
    "background_sections": [
        ("What Do Plants Need?", "Plants need four basic things to survive: water, sunlight, air, and nutrients from soil. Water is absorbed through roots and transported up through the stem to every part of the plant. Sunlight provides the energy plants use for photosynthesis — the process of making their own food from light, water, and carbon dioxide. Without adequate water or sunlight, plants cannot make food and will stop growing, wilt, and eventually die."),
        ("How Water Helps Plants Grow", "Water plays several critical roles in plant growth. It carries dissolved minerals and nutrients from soil into the roots and throughout the plant. Water pressure inside plant cells keeps stems and leaves firm and upright — when a plant lacks water, cells lose pressure and the plant wilts. Water is also a key ingredient in photosynthesis. Most kindergarten-appropriate plants (grass seeds, bean sprouts) show visible growth differences within 5-7 days when given different amounts of water.")
    ],
    "lever_L": "Students identify Amount of Water as the external component (we decide how much to water) and Plant Growth as the internal component (the plant grows on its own based on how much water it gets).",
    "lever_E": "Students discover that more water leads to more Plant Growth — a positive relationship (up to a point).",
    "lever_V": "Students build a simple two-part model connecting Amount of Water to Plant Growth with a positive arrow.",
    "lever_Ev": "Students test Little Water vs. Lots of Water over several days and observe growth differences.",
    "lever_R": "Students explore what happens when they change sunlight instead of water — do plants in the dark grow well even with water?",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with a bright green sprout growing from soil", "say": "Have you ever planted a seed? What did you do to help it grow? Today we will learn what plants really need!", "do": "Show a live plant and a wilted plant (or pictures). Ask: Which plant looks happy? Which looks sad? Why?", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn?", "visual": "Learning goals with plant and water icons", "say": "Today we will discover what plants need to grow big and strong! Hint: one thing comes from the sky and one comes from the faucet!", "do": "Introduce 'nutrients' and 'sunlight.' Have students act like a plant — crouch down small, then grow tall with arms out like leaves reaching for sun.", "time": "3 min"},
        {"num": "Slide 3", "title": "Let's Be Scientists!", "visual": "Big question with a growing plant picture", "say": "Our big question is: What does a plant need to grow big and strong? Can a plant grow with NO water? Let us find out!", "do": "Students share with a partner what they think plants need. Make a class list on the board.", "time": "3 min"},
        {"num": "Slide 4", "title": "What Are the Parts?", "visual": "Two component cards: Amount of Water and Plant Growth", "say": "Our model has two parts. Amount of Water is how much water we give the plant — WE decide that! Plant Growth is how big the plant gets — the plant does that on its own.", "do": "Use sorting mats. Students place Amount of Water on OUTSIDE and Plant Growth on INSIDE. Pretend to water a plant with a cup.", "time": "5 min"},
        {"num": "Slide 5", "title": "How Are They Connected?", "visual": "Arrow from Amount of Water to Plant Growth", "say": "When a plant gets MORE water, it grows BIGGER. When it gets LESS water, it grows smaller or wilts. That is a POSITIVE connection!", "do": "Show pictures of a well-watered plant vs. a dry plant. Students give thumbs up for positive connection. Water a class plant together.", "time": "5 min"},
        {"num": "Slide 6", "title": "What Did We Find Out?", "visual": "Key discoveries with happy and sad plant illustrations", "say": "Plants NEED water to grow! Water goes in through the roots and helps the plant make food and stand up tall. No water means a sad, droopy plant.", "do": "Chant: 'When Water goes up, Plant Growth goes up!' Complete the sentence frame. Students draw a well-watered plant.", "time": "5 min"},
        {"num": "Slide 7", "title": "STEM Challenge", "visual": "Mini Garden design challenge with seeds and cups", "say": "Now YOU are the gardeners! Plant your seeds and make a watering plan. How much water will you give your plant each day to help it grow the tallest?", "do": "Distribute cups with soil, seeds (fast-growing grass or bean), water cups with marked amounts. Students plant, water, and draw predictions of how tall their plant will grow.", "time": "10 min"}
    ],
    "sort_reasoning": "Amount of Water is outside because WE decide how much water to give the plant. Plant Growth is inside because the plant grows on its own depending on how much water it receives.",
    "relationships": [
        ("Amount of Water to Plant Growth", "POSITIVE (+)", "When a plant gets more water, it grows bigger and healthier because water carries nutrients and helps the plant make food through photosynthesis.")
    ],
    "sim_answers": [
        ("Little Water", "When Amount of Water is low, Plant Growth is small. The plant barely grows and its leaves may start to droop and turn brown."),
        ("Lots of Water", "When Amount of Water is high, Plant Growth is big. The plant grows tall with bright green leaves because water carries nutrients and helps it make food!")
    ],
    "stem_intro": "In this challenge, students plant seeds and create a watering plan to maximize growth. This connects directly to the model showing that more water leads to more plant growth, while also introducing the idea that plants need consistent care over time.",
    "stem_concepts": [
        ("Water and Growth", "Water is absorbed through plant roots and transported throughout the plant. It carries nutrients and is essential for photosynthesis — the process by which plants make their own food."),
        ("Living Things Need Care", "Unlike toys or rocks, living things like plants need regular attention — water, sunlight, and good soil — to stay healthy and grow. This is what makes them alive!")
    ],
    "stem_eval": [
        ("Expert (4)", "Student plants seeds carefully, creates a reasonable watering plan, and explains that more water helps the plant grow bigger because plants need water to be healthy."),
        ("Proficient (3)", "Student plants seeds and gives their plant water, stating that water helps plants grow."),
        ("Developing (2)", "Student plants seeds and waters the plant but needs help connecting water to plant growth."),
        ("Beginning (1)", "Student participates in planting but does not yet understand why water is important for the plant.")
    ],
    "support": [
        "Pre-fill soil cups so students only need to make a hole, drop in the seed, and water",
        "Use picture schedule cards showing the steps: dig, plant, water, wait, observe",
        "Provide a simple two-column tracking sheet with smiley faces (watered today / did not water today)"
    ],
    "extensions": [
        "Plant two seeds: one by a sunny window and one in a dark closet. Both get the same water. What happens?",
        "Measure plant height with unifix cubes each day and compare who has the tallest plant after one week",
        "Explore what is INSIDE a seed by soaking a large bean overnight and carefully opening it to see the baby plant inside"
    ],
    "cross_curr": [
        ("Math", "Measure plant growth using unifix cubes or paper clip chains — 'My plant is 3 cubes tall!'"),
        ("ELA", "Read aloud 'The Tiny Seed' by Eric Carle and discuss what the seed needed to become a big flower"),
        ("Art", "Create seed-to-plant flip books showing a seed in soil growing step by step into a tall plant")
    ],
    "misconceptions": [
        ("Plants eat dirt", "Plants do not eat soil. They absorb water and tiny nutrients dissolved in the water through their roots. Plants actually make their own food from sunlight, water, and air through a process called photosynthesis.", "Hold up a cup of soil and a cup of water. Ask: Which one does the plant drink? The water! The soil holds the plant in place and has some nutrients, but the plant does not eat the dirt."),
        ("More water is always better", "While plants need water, too much water can actually hurt them. Over-watering can drown the roots because they also need air. The right amount of water — not too much and not too little — is best for plant growth.", "Show a picture of a plant in a flooded pot with yellow leaves. Ask: This plant got TOO much water. What happened? Too much water fills up all the air spaces and the roots cannot breathe!")
    ],
    "sentence_frame": "When Amount of Water goes up, Plant Growth goes _______.",
    "coloring_description": "Color the watering can blue. Color the tall plant green and the small plant light green. Draw water drops going into the soil!"
}

L05 = {
    "id": "GK-L05",
    "title": "Where Do Animals Live?",
    "subtitle": "Animal Homes and Habitats",
    "ngss": "K-LS1-1",
    "ngss_desc": "Use observations to describe patterns of what plants and animals (including humans) need to survive.",
    "big_question": "Why do different animals live in different places?",
    "objectives": [
        "Identify that animals live in places that have what they need — food, water, and shelter",
        "Observe how the amount of food in a habitat affects how many animals can live there",
        "Describe how a habitat gives an animal everything it needs to survive"
    ],
    "vocabulary": [
        ("Habitat", "The place where an animal lives that has everything it needs — food, water, and a home"),
        ("Shelter", "A safe place where an animal can hide, rest, and stay warm or cool")
    ],
    "components": [
        ("Amount of Food", "How much food is available in the animal's habitat", True),
        ("Number of Animals", "How many animals can live and survive in that habitat", False)
    ],
    "think_about_it": "When there is MORE food in a habitat, can more animals or fewer animals live there?",
    "scenarios": [
        ("Little Food", "Imagine a pond with very few fish for the ducks to eat — how many ducks can live there?"),
        ("Lots of Food", "Imagine a pond full of fish for the ducks to eat — how many ducks can live there?")
    ],
    "sim_scenarios": [
        ("Little Food", "Amount of Food set to low", "What will happen to Number of Animals when there is very little food?"),
        ("Lots of Food", "Amount of Food set to high", "What will happen to Number of Animals when there is lots of food?")
    ],
    "discoveries": [
        "Animals live in places that have the food, water, and shelter they need",
        "When there is more food in a habitat, more animals can live there",
        "When food is scarce, animals have to move to a new place or there are fewer of them"
    ],
    "answer": "Animals live in habitats that have what they NEED! A habitat is an animal's home — it gives them food to eat, water to drink, and shelter to stay safe. When a habitat has LOTS of food, more animals can live there. When food runs out, animals have to find a new home. That is why fish live in water, birds live in trees, and bears live in forests — each place has exactly what they need!",
    "stem_title": "Build an Animal Habitat",
    "stem_mission": "Design and build a model habitat for a chosen animal that includes food, water, and shelter.",
    "stem_scenario": "The city zoo is building new habitats for their animals! Your team has been asked to design the perfect home for one animal. It must have food the animal likes, water to drink, and a safe shelter. Use what you learned about habitats to create the best animal home!",
    "stem_questions": [
        "What food does your animal need in its habitat?",
        "Where will your animal find shelter to stay safe and warm?"
    ],
    "stem_design_qs": [
        "Which animal did you choose and where does it live in the wild?",
        "What materials will you use to show food, water, and shelter?",
        "How will you show that your habitat has everything the animal needs?"
    ],
    "career": "Zookeepers take care of animals every day — feeding them, keeping their habitats clean, and making sure they are healthy and happy. They earn $28,000-$45,000/year.",
    "images": {
        "cover": ("cover-habitats.png", "A vibrant split scene showing four animal habitats: a colorful coral reef underwater, a lush green forest, a golden savanna, and a snowy Arctic landscape, each with their animals, vivid colors, cinematic wide shot"),
        "landscape": ("landscape-habitats.png", "Diverse kindergarten students (5-6 years old, wide variety of ethnicities including White, Black, Latino, Asian, and mixed-race children) looking at pictures of animal habitats on a bulletin board, pointing and discussing excitedly, bright modern classroom"),
        "modeling": ("modeling-habitats.png", "A simple, colorful kid-friendly diagram showing a pond habitat with labels pointing to food (fish), water (the pond), and shelter (bushes), with ducks in the pond, cartoon-style, white background, bold outlines, cheerful"),
        "discussion": ("discussion-habitats.png", "A Black female teacher reading a big animal book with diverse kindergarteners (5-6 years old, wide variety of ethnicities) gathered close on a colorful rug, pointing at pictures of animals in their homes, warm engaged atmosphere"),
        "stem": ("stem-habitats.png", "Diverse kindergarteners (5-6 years old, wide mix of ethnicities) building model animal habitats in shoeboxes with craft materials, plastic animals, blue paper for water, green paper for grass, joyful creative play")
    },
    "pre_assessment": [
        "Circle where a duck lives: (picture of a pond / picture of a desert / picture of a house)",
        "Draw an animal in its home."
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students create a model habitat that shows the key things an animal needs to survive — food, water, and shelter."),
        ("Disciplinary Core Idea", "LS1.A Structure and Function", "All organisms have external parts. Different animals use their body parts in different ways to see, hear, grasp objects, protect themselves, move from place to place, and seek, find, and take in food, water, and air."),
        ("Crosscutting Concept", "Cause and Effect", "Students observe that changing the amount of food available (cause) changes how many animals can live in a habitat (effect).")
    ],
    "background_intro": "Every animal on Earth lives in a habitat — a place that provides what it needs to survive. Understanding habitats helps students see how animals and their environments are connected and why protecting natural places is so important.",
    "background_sections": [
        ("What Is a Habitat?", "A habitat is the natural environment where an organism lives. It provides four essential things: food, water, shelter, and space. Different animals need different habitats — a fish needs water, a bird needs trees, and a polar bear needs ice and snow. When a habitat has all the resources an animal needs, the animal can survive, grow, and reproduce. When resources are scarce, animal populations shrink or animals migrate to new areas."),
        ("Food Availability and Animal Populations", "The amount of food in a habitat is one of the biggest factors determining how many animals can live there. A pond full of fish can support many ducks, herons, and otters. A pond with few fish supports fewer animals. This concept is called carrying capacity. When food increases, populations can grow. When food decreases due to drought, pollution, or over-consumption, populations decline. This basic ecological principle is accessible to kindergarteners through simple scenarios about animals and their food.")
    ],
    "lever_L": "Students identify Amount of Food as the external component (nature or people determine how much food is in a habitat) and Number of Animals as the internal component (it changes based on food availability).",
    "lever_E": "Students discover that more food leads to more animals — a positive relationship.",
    "lever_V": "Students build a simple two-part model connecting Amount of Food to Number of Animals with a positive arrow.",
    "lever_Ev": "Students test Little Food vs. Lots of Food scenarios and observe how the number of animals changes.",
    "lever_R": "Students explore what happens when shelter or water is removed from the habitat — can animals survive with food but no shelter?",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with beautiful animal habitats collage", "say": "Where do fish live? Where do birds live? Where do YOU live? Today we are going to learn about animal HOMES!", "do": "Show pictures of animals in their habitats. Ask: Why does a fish live in water? Could a fish live in a tree? Students giggle and discuss.", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn?", "visual": "Learning goals with habitat icons", "say": "Today we learn about habitats! A habitat is an animal's home — it has food, water, and a safe place to live. Every animal needs the right habitat!", "do": "Introduce 'habitat' and 'shelter.' Students say habitat three times. Act it out: pretend to eat (food), drink (water), and hide under a blanket (shelter).", "time": "3 min"},
        {"num": "Slide 3", "title": "Let's Be Scientists!", "visual": "Big question with different animal homes", "say": "Our big question is: Why do different animals live in DIFFERENT places? A polar bear lives in the Arctic and a monkey lives in the jungle — why?", "do": "Matching game on the board: draw a line from each animal to its habitat. Students come up one at a time to draw lines.", "time": "3 min"},
        {"num": "Slide 4", "title": "What Are the Parts?", "visual": "Two component cards: Amount of Food and Number of Animals", "say": "Our model has two parts. Amount of Food is how much food is in the habitat — nature or people control that. Number of Animals is how many animals can live there — that depends on the food!", "do": "Use sorting mats. Students place Amount of Food on OUTSIDE and Number of Animals on INSIDE. Use toy animals and pretend food to demonstrate.", "time": "5 min"},
        {"num": "Slide 5", "title": "How Are They Connected?", "visual": "Arrow from Amount of Food to Number of Animals", "say": "When there is MORE food, MORE animals can live there. When food runs out, animals have to leave. That is a POSITIVE connection!", "do": "Act it out: spread toy fish around the rug (lots of food). Students pretend to be ducks and spread out. Remove most fish (little food). Now only a few ducks can stay.", "time": "5 min"},
        {"num": "Slide 6", "title": "What Did We Find Out?", "visual": "Key discoveries with habitat illustrations", "say": "We found out that animals live in places that have what they need! More food means more animals can live there. Habitats need food, water, AND shelter.", "do": "Chant: 'When Food goes up, Animals go up!' Complete the sentence frame together.", "time": "5 min"},
        {"num": "Slide 7", "title": "STEM Challenge", "visual": "Build-a-Habitat with shoeboxes and craft materials", "say": "Now YOU are the zookeepers! Pick an animal and build it the perfect habitat. Make sure it has food, water, and shelter!", "do": "Distribute shoeboxes, construction paper, craft sticks, cotton balls, plastic animals, glue. Students build habitats and present them: What animal? What food? Where is the water? Where is the shelter?", "time": "10 min"}
    ],
    "sort_reasoning": "Amount of Food is outside because nature or people control how much food is in a habitat — we cannot change that with our model. Number of Animals is inside because it changes on its own based on how much food is available.",
    "relationships": [
        ("Amount of Food to Number of Animals", "POSITIVE (+)", "When there is more food in a habitat, more animals can live there because every animal needs to eat to survive.")
    ],
    "sim_answers": [
        ("Little Food", "When Amount of Food is low, Number of Animals is small. Only a few animals can survive because there is not enough food for everyone."),
        ("Lots of Food", "When Amount of Food is high, Number of Animals is big. Many animals can live there because there is plenty of food for everyone to eat!")
    ],
    "stem_intro": "In this challenge, students design model habitats for a chosen animal, ensuring it includes food, water, and shelter. This connects to their model by demonstrating that a well-supplied habitat (lots of food) can support more animals.",
    "stem_concepts": [
        ("Habitat Needs", "Every animal needs food, water, shelter, and space in its habitat. If any of these is missing, the animal cannot survive in that location."),
        ("Carrying Capacity", "The amount of resources in a habitat limits how many animals can live there. More food and water means more animals can be supported.")
    ],
    "stem_eval": [
        ("Expert (4)", "Student builds a habitat with clear food, water, and shelter elements, names the animal's needs, and explains why more food allows more animals."),
        ("Proficient (3)", "Student builds a habitat with food, water, and shelter and identifies that animals need these things."),
        ("Developing (2)", "Student builds a habitat but includes only one or two of the three needs, requiring prompts to complete."),
        ("Beginning (1)", "Student participates in building but does not yet connect the habitat elements to what the animal needs to survive.")
    ],
    "support": [
        "Provide pre-cut habitat elements (blue paper for water, green strips for grass, brown paper bags for shelters) that students just arrange",
        "Limit animal choices to three familiar options (duck, rabbit, fish) with picture cards showing each animal's needs",
        "Use a simple checklist with pictures: Does your habitat have FOOD? (check) WATER? (check) SHELTER? (check)"
    ],
    "extensions": [
        "Research a real animal habitat — look at books or kid-safe websites to learn where a specific animal lives and what it eats",
        "Discuss what happens when a habitat is damaged — if a forest is cut down, where do the animals go?",
        "Compare two habitats (ocean vs. forest) and list which animals can live in each and why"
    ],
    "cross_curr": [
        ("Math", "Sort and count plastic animals by habitat type — how many live in water? How many live on land? Make a simple graph"),
        ("ELA", "Read aloud 'A House Is a House for Me' by Mary Ann Hoberman and discuss all the different animal homes"),
        ("Art", "Create a large class mural of a habitat — each student paints or glues one animal or one habitat feature onto the shared picture")
    ],
    "misconceptions": [
        ("Animals choose where to live like people choose a house", "Animals do not pick their homes the way people do. Animals live where they can find the food, water, and shelter they need to survive. Their bodies are built for their habitat — fish have gills for water, polar bears have thick fur for cold.", "Ask: Could a fish live in a tree? No! Why not? It needs WATER to breathe. Animals live where their bodies work best and where they can find what they need."),
        ("All animals eat the same food", "Different animals eat very different foods. Some eat plants (herbivores), some eat other animals (carnivores), and some eat both (omnivores). A rabbit eats grass and vegetables, while a hawk eats mice and rabbits.", "Show pictures of different animal foods: grass, fish, berries, insects. Ask: Does a frog eat grass? No, it eats bugs! Different animals need different food, so they live in places where THEIR food is found.")
    ],
    "sentence_frame": "When Amount of Food goes up, Number of Animals goes _______.",
    "coloring_description": "Color the pond blue for water. Color the fish in the pond (food). Draw ducks on the pond and color a bush for shelter!"
}

L06 = {
    "id": "GK-L06",
    "title": "What's the Weather Like Today?",
    "subtitle": "Watching the Sky and Tracking Weather",
    "ngss": "K-ESS2-1",
    "ngss_desc": "Use and share observations of local weather conditions to describe patterns over time.",
    "big_question": "Why is the weather different on different days?",
    "objectives": [
        "Observe and describe today's weather using words like sunny, cloudy, rainy, and windy",
        "Track weather over several days and notice patterns",
        "Explain how the number of clouds in the sky changes how sunny or rainy it is"
    ],
    "vocabulary": [
        ("Weather", "What it is like outside right now — sunny, rainy, cloudy, snowy, or windy"),
        ("Pattern", "Something that happens the same way again and again")
    ],
    "components": [
        ("Number of Clouds", "How many clouds are covering the sky — none, some, or lots", True),
        ("Amount of Sunshine", "How much sunlight reaches the ground", False)
    ],
    "think_about_it": "When there are MORE clouds in the sky, do we get more sunshine or less sunshine?",
    "scenarios": [
        ("Clear Sky", "Look outside on a day with no clouds — how much sunshine do you see?"),
        ("Cloudy Sky", "Look outside on a day with lots of clouds — how much sunshine do you see?")
    ],
    "sim_scenarios": [
        ("Clear Sky", "Number of Clouds set to zero", "What will happen to Amount of Sunshine when there are no clouds?"),
        ("Cloudy Sky", "Number of Clouds set to high", "What will happen to Amount of Sunshine when the sky is full of clouds?")
    ],
    "discoveries": [
        "When the sky has no clouds, we get lots of warm sunshine",
        "When the sky is full of clouds, they block the sun and it feels cooler and darker",
        "Weather changes from day to day, but we can see patterns over time"
    ],
    "answer": "The weather is different on different days because of what is happening in the SKY! When the sky is clear with no clouds, the sun shines down and it is bright and warm. When clouds come, they block the sunlight like a big blanket over the sky, making it cooler and sometimes bringing rain. By watching the weather every day, we can find patterns — like it might be sunny a lot in summer and rainy a lot in winter!",
    "stem_title": "Build a Class Weather Station",
    "stem_mission": "Create weather tracking tools and use them to observe and record the weather for one week.",
    "stem_scenario": "The school principal needs a weather report every day! Your class has been chosen to be the Official School Weather Watchers. You need to build tools to track the weather and report what you see every day for a week. Can your team be the best weather watchers?",
    "stem_questions": [
        "What kinds of weather did you see this week?",
        "Did you notice any patterns — was any type of weather more common?"
    ],
    "stem_design_qs": [
        "How will you show if it is sunny, cloudy, or rainy each day?",
        "Where will you record the weather so everyone can see it?",
        "What symbols will you use for each type of weather?"
    ],
    "career": "Meteorologists study the weather and help people know if it will be sunny, rainy, or snowy. They are the weather reporters on TV! They earn $50,000-$100,000/year.",
    "images": {
        "cover": ("cover-weather.png", "A dramatic sky split into four sections showing different weather — bright sunshine, fluffy white clouds, dark rain clouds with rain falling, and a rainbow, vivid colors, cinematic sky photography"),
        "landscape": ("landscape-weather.png", "Diverse kindergarten students (5-6 years old, wide variety of ethnicities including White, Black, Latino, Asian, and mixed-race children) looking out a large classroom window at the sky, some pointing at clouds, bright modern classroom with a weather chart on the wall"),
        "modeling": ("modeling-weather.png", "A simple, colorful kid-friendly diagram showing a clear sky with big sun and lots of sunshine arrows on the left, and a cloudy sky with blocked sunshine arrows on the right, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-weather.png", "A Black male teacher holding up weather picture cards with diverse kindergarteners (5-6 years old, wide variety of ethnicities) sitting on a colorful rug raising hands, a weather calendar chart visible on the wall behind them"),
        "stem": ("stem-weather.png", "Diverse kindergarteners (5-6 years old, wide mix of ethnicities) placing weather stickers on a large wall calendar, one child looking out the window at clouds, another drawing a sun, bright colorful classroom")
    },
    "pre_assessment": [
        "Circle today's weather: (picture of sun / picture of clouds / picture of rain / picture of snow)",
        "Draw what the sky looks like today."
    ],
    "dimensions": [
        ("Science Practice", "Analyzing and Interpreting Data", "Students collect daily weather observations and look for patterns over time, analyzing simple data about cloud cover and sunshine."),
        ("Disciplinary Core Idea", "ESS2.D Weather and Climate", "Weather is the combination of sunlight, wind, snow or rain, and temperature in a particular region at a particular time. People measure these conditions to describe and record the weather."),
        ("Crosscutting Concept", "Patterns", "Students observe and describe patterns in daily weather data, noticing that certain types of weather occur more frequently than others.")
    ],
    "background_intro": "Weather is the state of the atmosphere at a given time and place. Kindergarteners experience weather every day and can begin to observe, describe, and track it, building foundational skills in data collection and pattern recognition.",
    "background_sections": [
        ("What Is Weather?", "Weather describes the current conditions of the atmosphere — temperature, cloud cover, precipitation (rain, snow, sleet, hail), and wind. Weather changes from hour to hour and day to day. It is influenced by the sun's energy heating Earth's surface unevenly, the movement of air masses, and the water cycle. At the kindergarten level, students observe basic weather conditions: Is it sunny? Cloudy? Rainy? Windy? Cold or warm?"),
        ("Clouds and Sunshine", "Clouds are collections of tiny water droplets or ice crystals floating in the atmosphere. When there are few or no clouds, sunlight reaches the ground directly, making it bright and warm. When clouds cover the sky, they block and scatter sunlight, making it dimmer and cooler below. Thick clouds can block most sunlight and may produce rain or snow. Tracking cloud cover over time reveals weather patterns that help young scientists understand predictability in nature.")
    ],
    "lever_L": "Students identify Number of Clouds as the external component (nature controls how many clouds are in the sky) and Amount of Sunshine as the internal component (it changes based on cloud cover).",
    "lever_E": "Students discover that more clouds lead to less sunshine — a NEGATIVE relationship.",
    "lever_V": "Students build a simple two-part model connecting Number of Clouds to Amount of Sunshine with a negative arrow.",
    "lever_Ev": "Students test Clear Sky vs. Cloudy Sky scenarios and observe the difference in sunshine.",
    "lever_R": "Students explore what happens when clouds bring rain — how does rain change what we can do outside?",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with a dramatic sky showing different weather types", "say": "Look outside! What is the weather like today? Is the sun out? Are there clouds? Today we are going to become WEATHER WATCHERS!", "do": "Walk to the window and look at the sky together. Students describe what they see using their own words.", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn?", "visual": "Learning goals with weather icons", "say": "Today we will learn about weather! Weather is what it is like outside right now. We will learn to watch the sky and find PATTERNS!", "do": "Introduce 'weather' and 'pattern.' Students say each word. Show a pattern (clap-clap-snap, clap-clap-snap) and ask: What comes next?", "time": "3 min"},
        {"num": "Slide 3", "title": "Let's Be Scientists!", "visual": "Big question with weather photos", "say": "Our big question is: Why is the weather different on different days? Yesterday it was ___. Today it is ___. Why does it keep changing?", "do": "Quick weather vote: students hold up sun cards, cloud cards, or rain cards for today's weather. Count and graph results.", "time": "3 min"},
        {"num": "Slide 4", "title": "What Are the Parts?", "visual": "Two component cards: Number of Clouds and Amount of Sunshine", "say": "Our model has two parts. Number of Clouds is how many clouds are in the sky — nature decides that! Amount of Sunshine is how much sun reaches us — that depends on the clouds.", "do": "Use sorting mats. Students place Number of Clouds on OUTSIDE and Amount of Sunshine on INSIDE. Use cotton balls (clouds) and a flashlight (sun) to show blocking.", "time": "5 min"},
        {"num": "Slide 5", "title": "How Are They Connected?", "visual": "Arrow from Number of Clouds to Amount of Sunshine with a minus sign", "say": "When there are MORE clouds, do we get MORE sun or LESS sun? LESS! That is a NEGATIVE connection — when one goes up, the other goes DOWN!", "do": "Demonstrate: shine a flashlight (sun) on a student. Now hold cotton balls (clouds) in front. Did the light get brighter or dimmer? Students show thumbs down for negative.", "time": "5 min"},
        {"num": "Slide 6", "title": "What Did We Find Out?", "visual": "Key discoveries with cloud and sun illustrations", "say": "Clouds block the sunshine! More clouds means less sun. No clouds means lots of bright sunshine. And we can watch for patterns!", "do": "Chant: 'When Clouds go up, Sunshine goes DOWN!' Complete the sentence frame together. This is different — it is negative!", "time": "5 min"},
        {"num": "Slide 7", "title": "STEM Challenge", "visual": "Class Weather Station with tracking calendar", "say": "Now we are Official Weather Watchers! Every day this week we will check the sky and put a sticker on our weather calendar. Let us start TODAY!", "do": "Set up a weather wall chart with days of the week. Students choose the right weather sticker for today. Plan to check every day this week.", "time": "10 min"}
    ],
    "sort_reasoning": "Number of Clouds is outside because nature controls how many clouds are in the sky — we cannot change that. Amount of Sunshine is inside because it changes based on how many clouds are blocking the sun.",
    "relationships": [
        ("Number of Clouds to Amount of Sunshine", "NEGATIVE (-)", "When there are more clouds, less sunshine reaches the ground because clouds block and scatter the sunlight.")
    ],
    "sim_answers": [
        ("Clear Sky", "When Number of Clouds is zero, Amount of Sunshine is high. The sun shines brightly on everything because nothing is blocking it!"),
        ("Cloudy Sky", "When Number of Clouds is high, Amount of Sunshine is low. The clouds block the sun like a blanket, making it dimmer and cooler on the ground.")
    ],
    "stem_intro": "In this challenge, students create and maintain a class weather station for one week. By tracking weather daily, they observe real-world data about cloud cover and sunshine, connecting to their model while building data-collection skills.",
    "stem_concepts": [
        ("Weather Observation", "Scientists observe and record weather conditions every day. By collecting data over time, patterns emerge — like rainy weeks, sunny stretches, or seasonal changes."),
        ("Patterns in Nature", "Weather follows patterns. Some seasons are typically sunnier or rainier than others. Recognizing these patterns helps people plan their activities and even grow food.")
    ],
    "stem_eval": [
        ("Expert (4)", "Student accurately observes and records weather daily, identifies at least one pattern, and explains that clouds block sunshine using the model."),
        ("Proficient (3)", "Student records weather daily and notices that cloudy days are less sunny, connecting to the model."),
        ("Developing (2)", "Student records weather with help but does not yet connect cloud observations to sunshine levels."),
        ("Beginning (1)", "Student participates in daily observation but does not independently record or describe weather conditions.")
    ],
    "support": [
        "Use large, clear weather symbol cards (sun, clouds, rain, wind) that students match to what they see outside",
        "Provide a pre-made weather calendar with picture stickers so students just peel and stick each day",
        "Pair students with a weather buddy so they can discuss what they see before recording"
    ],
    "extensions": [
        "Add temperature to the daily tracking — is it warm, cool, or cold? Use a simple three-face thermometer (happy sun, neutral, cold snowflake)",
        "Compare weather at school with weather in a different city using a kid-friendly weather website",
        "Predict tomorrow's weather based on today's sky — if it is cloudy today, what might happen tomorrow?"
    ],
    "cross_curr": [
        ("Math", "Graph the week's weather data — how many sunny days? How many cloudy days? How many rainy days? Which had the most?"),
        ("ELA", "Keep a simple weather journal with sentence starters: 'Today the weather is ___ because I see ___'"),
        ("Art", "Create weather collages for each type — use cotton balls for clouds, yellow tissue paper for sun, blue streamers for rain")
    ],
    "misconceptions": [
        ("Clouds are made of cotton or smoke", "Clouds are actually made of tiny, tiny drops of water or bits of ice floating in the air. They form when water evaporates from the ground and rises up into the sky where the air is cool enough to turn the water vapor back into tiny droplets.", "Ask: What are clouds made of? Many kids say cotton or smoke. Explain: Clouds are made of teeny-tiny water drops so small they float in the air! Breathe on a cold window to show water vapor becoming visible drops."),
        ("Rain falls from holes in the clouds", "Rain happens when water droplets inside clouds bump into each other and join together, getting bigger and bigger until they are too heavy to float. Then gravity pulls them down as rain. There are no holes in clouds.", "Demonstrate: hold a sponge (cloud) under the faucet. As it soaks up more and more water, it gets heavier until water drips out the bottom. That is how clouds make rain — too much water to hold!")
    ],
    "sentence_frame": "When Number of Clouds goes up, Amount of Sunshine goes _______.",
    "coloring_description": "Color a clear sky bright yellow with a big sun. Color a cloudy sky gray with clouds covering the sun. Circle which sky gives more sunshine!"
}

L07 = {
    "id": "GK-L07",
    "title": "Can We Stop a Flood?",
    "subtitle": "Weather Hazards and Staying Safe",
    "ngss": "K-ESS3-2",
    "ngss_desc": "Ask questions to obtain information about the purpose of weather forecasting to prepare for, and respond to, severe weather.",
    "big_question": "What can people do to stop water from flooding their homes?",
    "objectives": [
        "Identify that too much rain can cause flooding",
        "Observe how a barrier can block water from spreading",
        "Describe how people build things to protect themselves from weather hazards like floods"
    ],
    "vocabulary": [
        ("Flood", "When too much water covers land that is usually dry"),
        ("Barrier", "Something that blocks or stops water from going where it should not go")
    ],
    "components": [
        ("Amount of Rain", "How much rain falls on an area — a little drizzle or a huge downpour", True),
        ("Flood Level", "How deep the water gets on the ground — shallow puddles or deep flooding", False)
    ],
    "think_about_it": "When MORE rain falls, does the flood get deeper or shallower?",
    "scenarios": [
        ("Light Rain", "Pour a little water on the sand table and watch what happens to the toy houses"),
        ("Heavy Rain", "Pour a lot of water on the sand table and watch what happens to the toy houses")
    ],
    "sim_scenarios": [
        ("Light Rain", "Amount of Rain set to low", "What will happen to Flood Level when there is only a little rain?"),
        ("Heavy Rain", "Amount of Rain set to high", "What will happen to Flood Level when there is a lot of rain?")
    ],
    "discoveries": [
        "More rain makes higher flood levels — lots of rain can cover roads and homes",
        "Barriers like walls and sandbags can slow down or stop water from flooding",
        "People can prepare for floods by building barriers and moving to higher ground"
    ],
    "answer": "We CAN help stop a flood! When too much rain falls, water covers the ground and makes a flood. But people are smart — they build BARRIERS to block the water! Sandbags, walls, and levees stop water from reaching homes. People also watch weather reports so they know when heavy rain is coming and can get ready. We cannot stop the rain, but we CAN build things to protect us!",
    "stem_title": "Build a Flood Barrier",
    "stem_mission": "Design and build a barrier out of classroom materials that stops water from reaching a toy house on the sand table.",
    "stem_scenario": "Oh no! A big rainstorm is coming to Toy Town and the houses might flood! Your engineering team must build the best barrier to stop the water from reaching the houses. You have clay, craft sticks, aluminum foil, and plastic wrap. Which materials will keep the water out?",
    "stem_questions": [
        "Which material worked best to stop the water?",
        "Did any water get past your barrier? How could you make it better?"
    ],
    "stem_design_qs": [
        "What material will you use to build your wall?",
        "How tall does your barrier need to be?",
        "How will you test if your barrier keeps the water out?"
    ],
    "career": "Civil Engineers design bridges, roads, dams, and flood walls to keep people safe from water and weather. They earn $60,000-$115,000/year.",
    "images": {
        "cover": ("cover-flood.png", "A dramatic scene of rain pouring heavily on a miniature toy town made of colorful wooden houses, water pooling around the houses, vivid blue water, dark cloudy sky above, tilt-shift miniature photography style"),
        "landscape": ("landscape-flood.png", "Diverse kindergarten students (5-6 years old, wide variety of ethnicities including White, Black, Latino, Asian, and mixed-race children) gathered around a water table building barriers out of clay and craft sticks to protect toy houses, excited problem-solving expressions"),
        "modeling": ("modeling-flood.png", "A simple, colorful kid-friendly diagram showing rain clouds with arrows pointing down to a town, one side has a barrier wall blocking the water, one side has water flooding houses, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-flood.png", "A Black female teacher showing a picture book about floods to diverse kindergarteners (5-6 years old, wide variety of ethnicities) on a colorful rug, students looking engaged and asking questions, cozy classroom atmosphere"),
        "stem": ("stem-flood.png", "Diverse kindergarteners (5-6 years old, wide mix of ethnicities) building flood barriers on a sand table with clay, foil, and craft sticks, pouring water from cups to test their designs, excited and focused")
    },
    "pre_assessment": [
        "Circle what causes a flood: (picture of lots of rain / picture of a sunny day)",
        "Draw a wall that stops water from reaching a house."
    ],
    "dimensions": [
        ("Science Practice", "Asking Questions and Defining Problems", "Students ask questions about how to protect homes from flooding and define the problem of stopping water with a barrier."),
        ("Disciplinary Core Idea", "ESS3.B Natural Hazards", "Some kinds of severe weather are more likely than others in a given region. Weather scientists forecast severe weather so that communities can prepare for and respond to these events."),
        ("Crosscutting Concept", "Cause and Effect", "Students observe that more rain (cause) leads to higher flood levels (effect), and that barriers can reduce the effect.")
    ],
    "background_intro": "Flooding is one of the most common natural hazards. Teaching young children about weather preparedness empowers them to understand that while we cannot control the weather, we can design solutions to reduce its impact on our communities.",
    "background_sections": [
        ("What Causes Floods?", "Floods occur when water overflows onto land that is normally dry. The most common cause is heavy rainfall that exceeds the ground's ability to absorb water. Rivers and streams can overflow their banks, and storm drains can back up in cities. Flash floods happen quickly after intense rain. Coastal areas can flood from storm surges during hurricanes. Understanding that more rain equals more flood risk is the foundational concept for kindergarteners."),
        ("How People Protect Against Floods", "Humans have developed many ways to manage flood risk. Levees and dams hold back river water. Sandbags create temporary barriers during emergencies. Proper drainage systems channel water away from buildings. Retention ponds store excess water during storms. At the kindergarten level, the key concept is that BARRIERS (walls, bags, ditches) can block or redirect water to keep homes safe. This introduces engineering design thinking — identifying a problem and building a solution.")
    ],
    "lever_L": "Students identify Amount of Rain as the external component (weather controls how much rain falls) and Flood Level as the internal component (it rises or falls based on how much rain comes).",
    "lever_E": "Students discover that more rain leads to higher Flood Level — a positive relationship.",
    "lever_V": "Students build a simple two-part model connecting Amount of Rain to Flood Level with a positive arrow.",
    "lever_Ev": "Students test Light Rain vs. Heavy Rain scenarios on the sand table and observe flooding differences.",
    "lever_R": "Students explore what happens when they add a barrier — can they reduce the Flood Level even when rain is heavy?",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with rain over a miniature toy town", "say": "Have you ever seen a really big puddle after it rains? What if the puddle got SO big it covered your whole yard? That is a FLOOD!", "do": "Show a picture of a small puddle next to a picture of a real flood. Ask: What is different? How did the water get so high?", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn?", "visual": "Learning goals with rain and barrier icons", "say": "Today we will learn what causes floods and how people STOP them! We will build our own flood barriers like real engineers!", "do": "Introduce 'flood' and 'barrier.' Students say each word. Show a picture of sandbags and ask: What are these for?", "time": "3 min"},
        {"num": "Slide 3", "title": "Let's Be Scientists!", "visual": "Big question with flooding scene", "say": "Our big question is: Can we STOP a flood? If it rains and rains and rains, what can people build to keep the water away?", "do": "Students brainstorm with a partner: What could you build to stop water? Share ideas as a class and list them on the board.", "time": "3 min"},
        {"num": "Slide 4", "title": "What Are the Parts?", "visual": "Two component cards: Amount of Rain and Flood Level", "say": "Our model has two parts. Amount of Rain is how much rain falls — the WEATHER decides that. Flood Level is how high the water gets — that depends on the rain!", "do": "Use sorting mats. Students place Amount of Rain on OUTSIDE and Flood Level on INSIDE. Sprinkle water (light rain) then pour water (heavy rain) into a shallow pan.", "time": "5 min"},
        {"num": "Slide 5", "title": "How Are They Connected?", "visual": "Arrow from Amount of Rain to Flood Level", "say": "When MORE rain falls, the Flood Level goes UP! That is a POSITIVE connection. More rain means more flooding.", "do": "Demonstrate on the sand table: pour a little water — small puddle. Pour a lot of water — flood! Students give thumbs up for positive.", "time": "5 min"},
        {"num": "Slide 6", "title": "What Did We Find Out?", "visual": "Key discoveries with flood and barrier illustrations", "say": "More rain means more flooding. But smart engineers build BARRIERS to block the water! Sandbags, walls, and levees protect homes.", "do": "Chant: 'When Rain goes up, Flooding goes up!' Complete the sentence frame together. Discuss: What can we BUILD to help?", "time": "5 min"},
        {"num": "Slide 7", "title": "STEM Challenge", "visual": "Flood Barrier building challenge", "say": "A big storm is coming to Toy Town! Can your team build a barrier to stop the flood? Test it by pouring water!", "do": "Distribute sand table supplies: clay, craft sticks, foil, plastic wrap, toy houses. Groups build barriers. Test by slowly pouring water and observing. Discuss what worked and what did not.", "time": "10 min"}
    ],
    "sort_reasoning": "Amount of Rain is outside because the weather controls how much rain falls — we cannot change it. Flood Level is inside because it rises or falls depending on how much rain comes down.",
    "relationships": [
        ("Amount of Rain to Flood Level", "POSITIVE (+)", "When more rain falls, the flood level gets higher because the ground cannot absorb all the water and it pools on the surface.")
    ],
    "sim_answers": [
        ("Light Rain", "When Amount of Rain is low, Flood Level is low. There are just small puddles and the ground soaks up most of the water."),
        ("Heavy Rain", "When Amount of Rain is high, Flood Level is high. The ground cannot hold all the water, so it spreads out and covers roads, yards, and can even reach houses!")
    ],
    "stem_intro": "In this challenge, students design flood barriers to protect toy houses, applying their model knowledge that heavy rain causes high flood levels. They experiment with different materials to discover which creates the most effective barrier — an authentic engineering design experience.",
    "stem_concepts": [
        ("Flood Barriers", "Walls, sandbags, levees, and dams are structures designed to block or redirect water away from areas where people live. The barrier must be taller and stronger than the flood level to be effective."),
        ("Engineering Solutions", "Engineers solve problems by designing and testing solutions. When a barrier does not work perfectly, they redesign and test again — this is called the engineering design cycle.")
    ],
    "stem_eval": [
        ("Expert (4)", "Student builds an effective barrier that blocks most water, tests it, redesigns after failure, and explains why barriers help stop floods."),
        ("Proficient (3)", "Student builds a barrier that blocks some water and explains that barriers stop water from reaching houses."),
        ("Developing (2)", "Student builds a structure but it does not effectively block water; needs guidance connecting the barrier to flood protection."),
        ("Beginning (1)", "Student participates in building but does not yet understand how the barrier relates to stopping flood water.")
    ],
    "support": [
        "Pre-build a simple clay wall and let students observe it blocking water before they build their own",
        "Limit material choices to two options (clay vs. foil) to simplify decision-making",
        "Use a very shallow pan with slow water pouring so students have time to observe and respond"
    ],
    "extensions": [
        "Test what happens when you make the barrier taller — does a taller wall stop more water?",
        "Discuss real flood barriers: show pictures of sandbags, levees, and dams and how communities use them",
        "Design an evacuation plan — if the barrier does not hold, where should the toy people go? Higher ground!"
    ],
    "cross_curr": [
        ("Math", "Measure how many cups of water it takes to flood the toy town — count and compare with and without the barrier"),
        ("ELA", "Read aloud 'Come On, Rain!' by Karen Hesse and discuss the difference between welcome rain and too-much rain"),
        ("Art", "Create rainy day watercolor paintings — use watered-down paint to make real water effects on paper")
    ],
    "misconceptions": [
        ("Floods only happen near the ocean", "Floods can happen anywhere it rains heavily. Rivers, streams, and even streets in cities can flood when too much rain falls too quickly. Floods happen in mountains, plains, deserts, and cities — not just near the ocean.", "Show pictures of floods in different places — a city street, a farm field, a mountain road. Ask: Are any of these near the ocean? No! Floods can happen anywhere there is too much water."),
        ("You can stop all floods with a wall", "While barriers help reduce flooding, very heavy rains or huge storms can overwhelm even strong barriers. That is why weather forecasting is so important — knowing a big storm is coming lets people prepare, evacuate, and stay safe even when barriers are not enough.", "After testing barriers, pour extra water to show that even good barriers can be overwhelmed. Ask: What should people do if the water is too much for the wall? Move to higher ground! That is why we listen to weather reports.")
    ],
    "sentence_frame": "When Amount of Rain goes up, Flood Level goes _______.",
    "coloring_description": "Color the rain clouds dark gray. Color the water blue flooding toward the houses. Draw and color a barrier wall between the water and the houses!"
}

L08 = {
    "id": "GK-L08",
    "title": "Where Does Rain Come From?",
    "subtitle": "The Amazing Water Cycle",
    "ngss": "K-ESS2-1",
    "ngss_desc": "Use and share observations of local weather conditions to describe patterns over time.",
    "big_question": "Where does rain come from and where does it go after it falls?",
    "objectives": [
        "Describe how water goes up into the sky when the sun heats it up",
        "Observe how water turns into clouds and then falls back down as rain",
        "Explain the simple path of water: puddle to sky to cloud to rain"
    ],
    "vocabulary": [
        ("Evaporation", "When the sun heats up water and it floats up into the sky as invisible gas"),
        ("Water Cycle", "The journey water takes — going up to the sky, making clouds, and falling back as rain, over and over again")
    ],
    "components": [
        ("Sun's Heat", "How warm the sun makes the water — hot sun or cool sun", True),
        ("Evaporation Speed", "How fast water goes up into the sky as invisible gas", False)
    ],
    "think_about_it": "When the sun is really hot, does water go up into the sky faster or slower?",
    "scenarios": [
        ("Cool Day", "Watch a puddle on a cool, cloudy day — does it dry up fast or slow?"),
        ("Hot Day", "Watch a puddle on a hot, sunny day — does it dry up fast or slow?")
    ],
    "sim_scenarios": [
        ("Cool Day", "Sun's Heat set to low", "What will happen to Evaporation Speed when the sun is not very warm?"),
        ("Hot Day", "Sun's Heat set to high", "What will happen to Evaporation Speed when the sun is very hot?")
    ],
    "discoveries": [
        "When the sun heats water, it turns into invisible gas and floats up into the sky — that is evaporation",
        "The water collects in the sky and makes clouds, and when clouds get too heavy, it rains",
        "Water goes around and around in a cycle — puddle to sky to cloud to rain, over and over!"
    ],
    "answer": "Rain comes from WATER that was already on the ground! Here is the amazing journey: The sun heats up water in puddles, rivers, and oceans. The warm water turns into invisible gas and floats UP into the sky. Way up high, the gas gets cold and turns back into tiny water drops that make clouds. When the clouds get really full of water drops, they get too heavy and the water falls back down as RAIN! Then it starts all over again — that is the WATER CYCLE!",
    "stem_title": "Make a Mini Water Cycle",
    "stem_mission": "Build a mini water cycle in a zip-lock bag to watch water evaporate, form clouds, and rain back down!",
    "stem_scenario": "Scientists need your help to understand the water cycle! Your team will build a water cycle in a bag so everyone can SEE how water travels from the ground to the sky and back again. Tape it to a sunny window and watch the magic happen!",
    "stem_questions": [
        "Where did the water drops at the top of the bag come from?",
        "What part of the bag is like the sun? What part is like a cloud?"
    ],
    "stem_design_qs": [
        "How much water will you put in the bag?",
        "Where will you tape the bag so the sun can heat it?",
        "How will you draw the water cycle on your bag to label each part?"
    ],
    "career": "Hydrologists study where water goes — in rivers, underground, in clouds, and in the ocean. They help make sure everyone has clean water to drink! They earn $55,000-$95,000/year.",
    "images": {
        "cover": ("cover-water-cycle.png", "A magical scene showing a sparkling puddle with water droplets rising up into fluffy clouds, a rainbow arching overhead, rain falling gently on one side, vivid blues and golds, cinematic dreamy lighting"),
        "landscape": ("landscape-water-cycle.png", "Diverse kindergarten students (5-6 years old, wide variety of ethnicities including White, Black, Latino, Asian, and mixed-race children) looking at a zip-lock bag taped to a sunny window with water drops forming inside, amazed expressions, bright modern classroom"),
        "modeling": ("modeling-water-cycle.png", "A simple, colorful kid-friendly diagram showing the water cycle: a puddle at the bottom with arrows going up (evaporation), a cloud at the top, and arrows going down (rain), big smiling sun, cartoon-style, white background, bold outlines, labels on each step"),
        "discussion": ("discussion-water-cycle.png", "A Black male teacher outside with diverse kindergarteners (5-6 years old, wide variety of ethnicities) looking at a puddle in the sunshine, one child pointing up at clouds, teacher gesturing the water going up, beautiful sunny day"),
        "stem": ("stem-water-cycle.png", "Diverse kindergarteners (5-6 years old, wide mix of ethnicities) decorating and taping zip-lock bags with water to a sunny window, drawing suns and clouds on the bags with markers, excited scientific exploration")
    },
    "pre_assessment": [
        "Circle where rain comes from: (picture of clouds / picture of a faucet / picture of the ground)",
        "Draw a cloud making rain."
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students create a simple bag model of the water cycle, observing evaporation and condensation in real time."),
        ("Disciplinary Core Idea", "ESS2.D Weather and Climate", "Weather is the combination of sunlight, wind, snow or rain, and temperature. Water cycles between the ground and the atmosphere through evaporation and precipitation."),
        ("Crosscutting Concept", "Cause and Effect", "Students observe that the sun's heat (cause) makes water evaporate faster (effect), driving the water cycle.")
    ],
    "background_intro": "The water cycle is one of nature's most important processes. Every drop of rain that falls has made the journey from Earth's surface to the atmosphere and back countless times over billions of years.",
    "background_sections": [
        ("How the Water Cycle Works", "The water cycle has three main stages. Evaporation occurs when the sun heats water on Earth's surface (oceans, lakes, rivers, puddles), turning liquid water into water vapor — an invisible gas that rises into the atmosphere. Condensation happens when water vapor rises high enough to encounter cold air, causing it to turn back into tiny liquid droplets that cling together to form clouds. Precipitation occurs when cloud droplets combine and grow heavy enough to fall as rain, snow, sleet, or hail. The water then collects in bodies of water and the cycle repeats."),
        ("Why the Sun Drives the Cycle", "The sun is the engine of the water cycle. Solar energy heats water at Earth's surface, providing the energy needed for evaporation. Hotter temperatures cause faster evaporation — a puddle on a hot summer day disappears much faster than one on a cool cloudy day. Without the sun's heat, the water cycle would stop and there would be no rain, no rivers, and no fresh water. Understanding that the sun's heat controls evaporation speed is the key concept for kindergarteners.")
    ],
    "lever_L": "Students identify Sun's Heat as the external component (the sun's warmth is controlled by weather/seasons) and Evaporation Speed as the internal component (it changes based on how warm the sun makes the water).",
    "lever_E": "Students discover that more Sun's Heat leads to faster Evaporation Speed — a positive relationship.",
    "lever_V": "Students build a simple two-part model connecting Sun's Heat to Evaporation Speed with a positive arrow.",
    "lever_Ev": "Students test Cool Day vs. Hot Day scenarios and observe how quickly puddles dry up or water rises in a bag.",
    "lever_R": "Students explore what happens when they add wind — does wind make puddles dry up even faster?",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with a magical water cycle scene", "say": "Have you ever seen a puddle disappear? Where did the water go? And where does rain come from? Today we solve BOTH mysteries!", "do": "Show a video or time-lapse of a puddle drying up. Ask: The water disappeared! Did someone drink it? Where did it go?", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn?", "visual": "Learning goals with water cycle icons", "say": "Today we learn about the WATER CYCLE — the amazing journey water takes from the ground to the sky and back! The water in your drink has been on this journey millions of times!", "do": "Introduce 'evaporation' and 'water cycle.' For evaporation, wiggle fingers upward like water floating into the sky. Practice the word together.", "time": "3 min"},
        {"num": "Slide 3", "title": "Let's Be Scientists!", "visual": "Big question with puddle and rain pictures", "say": "Our big question is: Where does rain come from? Here is a clue — the answer starts with a puddle on the ground!", "do": "Pair-share: Where do you think rain comes from? Collect answers. Then reveal: Rain is made from water that was once in a puddle, a river, or the ocean!", "time": "3 min"},
        {"num": "Slide 4", "title": "What Are the Parts?", "visual": "Two component cards: Sun's Heat and Evaporation Speed", "say": "Our model has two parts. Sun's Heat is how warm the sun is — we cannot control the sun! Evaporation Speed is how fast water goes up into the sky — that depends on the sun's heat.", "do": "Use sorting mats. Students place Sun's Heat on OUTSIDE and Evaporation Speed on INSIDE. Warm hands together (that is heat!) then wave fingers up (that is evaporation!).", "time": "5 min"},
        {"num": "Slide 5", "title": "How Are They Connected?", "visual": "Arrow from Sun's Heat to Evaporation Speed", "say": "When the sun is REALLY hot, water goes up into the sky FAST! On a cool day, it goes slowly. More heat means faster evaporation — that is POSITIVE!", "do": "Demonstrate: place a wet paper towel near a warm lamp and another far away. Which dries faster? The one near the heat! Students give thumbs up for positive connection.", "time": "5 min"},
        {"num": "Slide 6", "title": "What Did We Find Out?", "visual": "Key discoveries with water cycle illustration", "say": "We discovered the water cycle! The sun heats water, it floats up as gas, makes clouds, and falls back as rain. It goes around and around forever!", "do": "Act out the water cycle as a class: crouch down (puddle), slowly rise (evaporation), gather together (cloud), fall down (rain). Repeat! Complete sentence frame.", "time": "5 min"},
        {"num": "Slide 7", "title": "STEM Challenge", "visual": "Mini Water Cycle in a bag", "say": "Now let us BUILD a water cycle! We will put water in a bag, tape it to a sunny window, and watch the water travel just like real rain!", "do": "Distribute zip-lock bags, water, blue food coloring. Students add water, seal bags, and draw sun/cloud/rain arrows on them with markers. Tape to sunny window. Check throughout the day for condensation drops.", "time": "10 min"}
    ],
    "sort_reasoning": "Sun's Heat is outside because the sun's warmth is controlled by the weather and seasons — we cannot change how hot the sun shines. Evaporation Speed is inside because it changes on its own depending on how much heat the sun provides.",
    "relationships": [
        ("Sun's Heat to Evaporation Speed", "POSITIVE (+)", "When the sun is hotter, water heats up more and turns into gas faster — evaporation speeds up because more heat energy makes water molecules move faster.")
    ],
    "sim_answers": [
        ("Cool Day", "When Sun's Heat is low, Evaporation Speed is slow. Puddles take a long time to dry up because the water does not get warm enough to float into the sky quickly."),
        ("Hot Day", "When Sun's Heat is high, Evaporation Speed is fast. Puddles dry up quickly because the sun's energy makes water turn into invisible gas and float up into the sky!")
    ],
    "stem_intro": "In this challenge, students create a mini water cycle in a sealed bag taped to a sunny window. As sunlight heats the water, it evaporates, condenses on the cool upper part of the bag, and drips back down — a visible, hands-on demonstration of the entire water cycle.",
    "stem_concepts": [
        ("Evaporation", "When the sun heats water, the liquid water gains enough energy to turn into water vapor — an invisible gas. This gas rises up into the atmosphere, which is the first step of the water cycle."),
        ("Condensation and Precipitation", "When water vapor rises and encounters cooler air, it turns back into tiny liquid drops — condensation. These drops collect to form clouds, and when they get heavy enough, they fall as rain — precipitation.")
    ],
    "stem_eval": [
        ("Expert (4)", "Student sets up the bag experiment, observes condensation forming, and explains that the sun heated the water so it went up, then it got cold and came back down — just like real rain."),
        ("Proficient (3)", "Student sets up the experiment and identifies that the water drops at the top came from the water at the bottom because of the sun's heat."),
        ("Developing (2)", "Student sets up the experiment and notices water drops forming but needs help explaining where they came from."),
        ("Beginning (1)", "Student participates in setting up the bag but does not yet connect the water drops to the evaporation process.")
    ],
    "support": [
        "Pre-fill the bags with water and food coloring so students only need to seal and tape them up",
        "Draw the water cycle steps on the bag beforehand (sun, arrows up, cloud, arrows down) so students can follow along",
        "Check the bag as a whole class at specific times (before lunch, after lunch, end of day) and discuss changes together"
    ],
    "extensions": [
        "Put two bags on the window — one in the sun and one in the shade. Which one shows condensation drops first?",
        "Go on a water cycle walk around the school — find evaporation (wet ground drying), condensation (foggy windows), and collection (puddles)",
        "Keep a puddle journal — draw a puddle on the playground each morning and track how it shrinks over days"
    ],
    "cross_curr": [
        ("Math", "Count the water drops that form on the bag each hour — make a simple number line showing drops over time"),
        ("ELA", "Read aloud 'The Water Cycle' by Rebecca Olien and act out each stage as a class play"),
        ("Art", "Paint a water cycle mural — blue for water, yellow for sun, white and gray for clouds, blue streaks for rain")
    ],
    "misconceptions": [
        ("Rain is new water that the clouds make", "Clouds do not create new water. Rain is made from water that evaporated from the ground, rivers, and oceans. The same water has been recycling through the water cycle for billions of years — the water you drink today might once have been in a dinosaur's lake!", "Ask: Where does the water in clouds come from? It came from the ground! The sun heated it up, it floated into the sky, and it made a cloud. The cloud did not make new water — it collected old water."),
        ("Water disappears when puddles dry up", "Water never disappears — it changes form. When a puddle dries up, the liquid water turned into water vapor (invisible gas) and floated into the air. The water is still there; you just cannot see it because it turned into a gas.", "Ask: Where did the puddle go? Students often say it disappeared. Breathe on a cold mirror to show water vapor becoming visible. Say: The water did not vanish — it turned invisible and floated up into the sky!")
    ],
    "sentence_frame": "When Sun's Heat goes up, Evaporation Speed goes _______.",
    "coloring_description": "Color the sun yellow at the top. Color the puddle blue at the bottom. Trace the arrows going UP from the puddle and DOWN from the cloud. Color the cloud white or gray!"
}

L09 = {
    "id": "GK-L09",
    "title": "How Do We Take Care of Earth?",
    "subtitle": "Reduce, Reuse, and Recycle",
    "ngss": "K-ESS3-3",
    "ngss_desc": "Communicate solutions that will reduce the impact of humans on the land, water, air, and/or other living things in the local environment.",
    "big_question": "What can WE do to help take care of our planet?",
    "objectives": [
        "Identify that people create trash that can hurt animals, water, and land",
        "Observe how reducing the amount of trash we make helps keep the Earth clean",
        "Describe ways we can reduce, reuse, and recycle to take care of our planet"
    ],
    "vocabulary": [
        ("Reduce", "To use less of something so we make less trash"),
        ("Recycle", "To turn old things into new things instead of throwing them away")
    ],
    "components": [
        ("Amount of Trash", "How much garbage people throw away — a lot or a little", True),
        ("Pollution Level", "How dirty and harmful the land, water, and air become", False)
    ],
    "think_about_it": "When people throw away MORE trash, does the Earth get cleaner or dirtier?",
    "scenarios": [
        ("Lots of Trash", "Imagine a park where people leave lots of garbage on the ground — what happens?"),
        ("Less Trash", "Imagine a park where people use less stuff and recycle — what happens?")
    ],
    "sim_scenarios": [
        ("Lots of Trash", "Amount of Trash set to high", "What will happen to Pollution Level when people throw away lots of trash?"),
        ("Less Trash", "Amount of Trash set to low", "What will happen to Pollution Level when people reduce, reuse, and recycle?")
    ],
    "discoveries": [
        "More trash makes more pollution — dirty water, dirty land, and hurt animals",
        "When we reduce, reuse, and recycle, we make LESS trash and the Earth stays cleaner",
        "Even kids can help by using less stuff, reusing containers, and recycling paper and plastic"
    ],
    "answer": "We take care of Earth by making LESS TRASH! When people throw away too much garbage, it makes our land dirty, our water yucky, and it hurts animals who might eat it or get stuck in it. But WE can help! We can REDUCE by using less stuff. We can REUSE by using things again instead of throwing them away. We can RECYCLE by putting paper, cans, and plastic in special bins so they can be turned into new things. Every little bit helps!",
    "stem_title": "Design a Reuse Creation",
    "stem_mission": "Take items from the recycling bin and turn them into something useful or fun instead of throwing them in the trash.",
    "stem_scenario": "The school is having a Reuse Art Show! Your team must take materials from the recycling bin — boxes, bottles, paper tubes, old newspapers — and turn them into something NEW and useful. Show everyone that trash can become treasure!",
    "stem_questions": [
        "What did you make from recycled materials?",
        "How does reusing this item help the Earth?"
    ],
    "stem_design_qs": [
        "What recycled materials will you use?",
        "What will you turn them into?",
        "How will you put the pieces together?"
    ],
    "career": "Environmental Scientists study how to keep our planet healthy — cleaning up pollution, protecting animals, and finding ways to reduce trash. They earn $55,000-$100,000/year.",
    "images": {
        "cover": ("cover-recycle.png", "A vibrant, hopeful scene of a clean green park with a blue recycling bin, bright flowers growing, a sunny sky, and a small globe of Earth surrounded by the recycling arrows symbol, vivid greens and blues, uplifting mood"),
        "landscape": ("landscape-recycle.png", "Diverse kindergarten students (5-6 years old, wide variety of ethnicities including White, Black, Latino, Asian, and mixed-race children) sorting recyclable materials into colorful bins labeled with pictures in a bright modern classroom, enthusiastic and proud expressions"),
        "modeling": ("modeling-recycle.png", "A simple, colorful kid-friendly diagram showing two scenes: on the left a dirty park with lots of trash and a sad face, on the right a clean park with recycling bins and a happy face, cartoon-style, white background, bold outlines, before-and-after style"),
        "discussion": ("discussion-recycle.png", "A Black female teacher sitting in a circle with diverse kindergarteners (5-6 years old, wide variety of ethnicities) on a colorful rug, holding up items and asking which bin they go in — trash, recycle, or reuse, interactive sorting game"),
        "stem": ("stem-recycle.png", "Diverse kindergarteners (5-6 years old, wide mix of ethnicities) creating art and toys from recycled materials — cardboard boxes, plastic bottles, paper tubes — gluing and painting their creations, proud and creative expressions")
    },
    "pre_assessment": [
        "Circle which bin the paper goes in: (picture of trash can / picture of recycling bin)",
        "Draw one thing you can do to help the Earth."
    ],
    "dimensions": [
        ("Science Practice", "Obtaining, Evaluating, and Communicating Information", "Students gather information about how trash affects the environment and communicate solutions like reducing, reusing, and recycling."),
        ("Disciplinary Core Idea", "ESS3.C Human Impacts on Earth Systems", "Things that people do to live comfortably can affect the world around them. But they can make choices that reduce their impacts on the land, water, air, and other living things."),
        ("Crosscutting Concept", "Cause and Effect", "Students observe that more trash (cause) leads to more pollution (effect), and that reducing trash reverses this relationship.")
    ],
    "background_intro": "Humans produce billions of tons of trash every year, much of which ends up in landfills, oceans, and natural habitats. Teaching children about reducing waste empowers them to become responsible stewards of the environment from an early age.",
    "background_sections": [
        ("How Trash Affects the Earth", "When people throw things away, the trash goes to landfills — huge areas of land filled with garbage. Some trash ends up in rivers and oceans, where it can harm fish, sea turtles, birds, and other wildlife. Animals can eat plastic thinking it is food, or get tangled in trash. Chemicals from garbage can leak into soil and groundwater, making water unsafe to drink. The more trash humans produce, the more pollution and habitat destruction result."),
        ("Reduce, Reuse, Recycle", "The three R's provide a framework for minimizing waste. Reduce means using less in the first place — choosing a reusable water bottle instead of buying plastic ones. Reuse means finding new purposes for items instead of throwing them away — turning a cardboard box into a toy castle. Recycle means sending materials like paper, plastic, glass, and metal to facilities that process them into new products. Reducing is the most effective strategy because it prevents trash from being created at all. Even small actions by young children — like using both sides of paper — add up to meaningful impact.")
    ],
    "lever_L": "Students identify Amount of Trash as the external component (people decide how much they throw away) and Pollution Level as the internal component (it changes based on how much trash ends up in the environment).",
    "lever_E": "Students discover that more trash leads to more Pollution Level — a positive relationship.",
    "lever_V": "Students build a simple two-part model connecting Amount of Trash to Pollution Level with a positive arrow.",
    "lever_Ev": "Students test Lots of Trash vs. Less Trash scenarios and observe the difference in how clean or dirty the park looks.",
    "lever_R": "Students explore what happens when they add recycling — if trash goes into recycling bins instead of the ground, does pollution go down?",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with a clean park and recycling symbol", "say": "Look at this beautiful park! Now look at THIS park with trash everywhere. Which one would you rather play in? Today we learn how to keep our Earth clean!", "do": "Show two pictures: a clean park and a littered park. Ask: What is different? How did the trash get there? Can we fix it?", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn?", "visual": "Learning goals with reduce/reuse/recycle icons", "say": "Today we learn THREE magic words to help the Earth: REDUCE — use less. REUSE — use it again. RECYCLE — make it into something new!", "do": "Teach the three R's with gestures: Reduce (make yourself small), Reuse (spin around — use it again!), Recycle (make a circle with your arms). Practice all three.", "time": "3 min"},
        {"num": "Slide 3", "title": "Let's Be Scientists!", "visual": "Big question with clean vs. polluted comparison", "say": "Our big question is: What can WE do to help take care of our planet? Even little kids can make a BIG difference!", "do": "Pair-share: Tell your partner one way you could make less trash at home or school. Share ideas with the class.", "time": "3 min"},
        {"num": "Slide 4", "title": "What Are the Parts?", "visual": "Two component cards: Amount of Trash and Pollution Level", "say": "Our model has two parts. Amount of Trash is how much garbage people throw away — WE decide that! Pollution Level is how dirty the Earth gets — that depends on our trash.", "do": "Use sorting mats. Students place Amount of Trash on OUTSIDE and Pollution Level on INSIDE. Show a clean rug, then scatter paper scraps on it — that is what trash does to the Earth!", "time": "5 min"},
        {"num": "Slide 5", "title": "How Are They Connected?", "visual": "Arrow from Amount of Trash to Pollution Level", "say": "When we throw away MORE trash, Pollution goes UP — the Earth gets dirtier. That is a POSITIVE connection. But if we make LESS trash, pollution goes DOWN!", "do": "Demonstrate: students scatter paper scraps (trash) on a mat (Earth). More trash = dirtier. Now pick it up and recycle it. Less trash = cleaner! Thumbs up for positive.", "time": "5 min"},
        {"num": "Slide 6", "title": "What Did We Find Out?", "visual": "Key discoveries with clean Earth and three R's", "say": "We found out that WE can help the Earth! Reduce, Reuse, Recycle — three ways to make less trash and keep our planet beautiful.", "do": "Chant: 'When Trash goes up, Pollution goes up!' But then: 'When we REDUCE, pollution goes DOWN!' Complete the sentence frame together.", "time": "5 min"},
        {"num": "Slide 7", "title": "STEM Challenge", "visual": "Reuse Art Show with recycled materials", "say": "Time for the Reuse Art Show! Take something from the recycling bin and turn it into something AMAZING. Trash into treasure!", "do": "Set up a reuse station with clean recycled materials: boxes, bottles, tubes, newspapers, tape, glue. Students create a new useful or fun item. Display in a class art show and explain what they reused.", "time": "10 min"}
    ],
    "sort_reasoning": "Amount of Trash is outside because people CHOOSE how much to throw away — we can reduce, reuse, and recycle to make less trash. Pollution Level is inside because it goes up or down depending on how much trash ends up in the environment.",
    "relationships": [
        ("Amount of Trash to Pollution Level", "POSITIVE (+)", "When people throw away more trash, pollution increases because the garbage piles up on land, washes into water, and hurts animals and their habitats.")
    ],
    "sim_answers": [
        ("Lots of Trash", "When Amount of Trash is high, Pollution Level is high. The park is covered in litter, animals can get sick, and the water gets dirty."),
        ("Less Trash", "When Amount of Trash is low, Pollution Level is low. The park stays clean and beautiful because people reduced, reused, and recycled instead of throwing things away!")
    ],
    "stem_intro": "In this challenge, students take clean recyclable materials and transform them into new creations. This tangibly demonstrates the 'reuse' concept from their model — every item reused is one less item in the trash, directly reducing pollution.",
    "stem_concepts": [
        ("Waste Reduction", "Every item we reuse or recycle is one less item in a landfill. If every person reduces their trash a little, the impact adds up to millions of tons of pollution prevented each year."),
        ("Creative Problem Solving", "Engineers and designers look at old materials and imagine new uses. A plastic bottle can become a planter. A cardboard box can become a robot. This creative reuse thinking is a real engineering skill.")
    ],
    "stem_eval": [
        ("Expert (4)", "Student creates a purposeful reuse item, explains what it was before and what it is now, and describes how reusing helps the Earth by reducing trash."),
        ("Proficient (3)", "Student creates a reuse item from recycled materials and states that reusing things makes less trash."),
        ("Developing (2)", "Student creates something from the materials but needs help connecting it to the idea of reusing to reduce trash."),
        ("Beginning (1)", "Student uses the materials to create something but does not yet understand the connection to helping the Earth.")
    ],
    "support": [
        "Pre-sort recycled materials into labeled bins (boxes, tubes, bottles) so students can easily find what they want",
        "Provide simple project ideas with picture instructions (a tube can become binoculars, a box can become a house)",
        "Work alongside students who need support, modeling how to select materials and glue them together"
    ],
    "extensions": [
        "Do a classroom trash audit — collect one day of classroom trash and sort it into categories: Could we have reduced, reused, or recycled any of this?",
        "Start a class recycling station with labeled bins for paper, plastic, and compost",
        "Write a class letter to the principal suggesting ways the school can reduce trash"
    ],
    "cross_curr": [
        ("Math", "Sort and count recyclable items by type — how many paper items? How many plastic items? Make a picture graph"),
        ("ELA", "Read aloud 'The Earth Book' by Todd Parr and discuss one thing each student promises to do for the Earth"),
        ("Art", "Create reuse sculptures from recycled materials and display them in a class Trash-to-Treasure gallery")
    ],
    "misconceptions": [
        ("Trash just disappears when the garbage truck takes it", "Trash does not disappear — the garbage truck takes it to a landfill where it piles up in a huge area. Some trash takes hundreds of years to break down. Plastic bottles can last 450 years! That is why reducing trash is so important.", "Ask: Where does the garbage truck take our trash? Show a picture of a landfill. Explain: The trash goes HERE and stays here for a very, very long time. That is why we want to make LESS trash!"),
        ("Recycling is the same as throwing things away", "Recycling is very different from throwing things in the trash. When you recycle, the materials are collected, cleaned, and turned into brand new things. A plastic bottle can become a new bottle or even a t-shirt! When you throw things in the trash, they sit in a landfill forever.", "Hold up a paper and show two paths: trash can (stays as garbage forever) vs. recycling bin (gets turned into new paper!). The recycling bin gives materials a second life!")
    ],
    "sentence_frame": "When Amount of Trash goes up, Pollution Level goes _______.",
    "coloring_description": "Color the recycling bin green. Color the clean park with green grass and flowers. Draw yourself putting something in the recycling bin!"
}

L10 = {
    "id": "GK-L10",
    "title": "What Happens When You Push Harder?",
    "subtitle": "Force, Speed, and How Things Move",
    "ngss": "K-PS2-1",
    "ngss_desc": "Plan and conduct an investigation to compare the effects of different strengths or different directions of pushes and pulls on the motion of an object.",
    "big_question": "What happens to a ball's speed when you push it harder?",
    "objectives": [
        "Observe that pushing a ball harder makes it roll faster",
        "Compare how gentle and strong pushes change a ball's speed",
        "Explain that a bigger force makes objects move faster"
    ],
    "vocabulary": [
        ("Speed", "How fast something is moving — slow like a turtle or fast like a cheetah"),
        ("Force", "A push or a pull that can make things move, speed up, slow down, or change direction")
    ],
    "components": [
        ("Push Force", "How hard you push the ball — a gentle tap or a powerful shove", True),
        ("Ball Speed", "How fast the ball rolls across the floor after you push it", False)
    ],
    "think_about_it": "When you push a ball HARDER, does it roll faster or slower?",
    "scenarios": [
        ("Gentle Tap", "Tap the ball with one finger and watch how fast it rolls"),
        ("Power Push", "Push the ball with your whole hand as hard as you can and watch how fast it rolls")
    ],
    "sim_scenarios": [
        ("Gentle Tap", "Push Force set to low", "What will happen to Ball Speed when you give just a gentle tap?"),
        ("Power Push", "Push Force set to high", "What will happen to Ball Speed when you give a really strong push?")
    ],
    "discoveries": [
        "A harder push makes the ball go faster — more force means more speed!",
        "A gentle tap makes the ball roll slowly because there is less force",
        "The same ball can go fast OR slow depending on how hard you push it",
        "Force is what changes how things move — without a push, the ball stays still"
    ],
    "answer": "When you push HARDER, things go FASTER! A push is a force, and the bigger the force, the more speed the ball gets. A tiny tap gives the ball just a little bit of speed, so it rolls slowly. A big powerful push gives the ball lots of speed, so it zooms across the floor! This is true for everything — bikes, swings, soccer balls — more force always means more speed. That is one of the most important rules in science!",
    "stem_title": "Design a Speed Test Ramp",
    "stem_mission": "Build a ramp and test how different push strengths make a ball travel at different speeds down the ramp.",
    "stem_scenario": "The school is building a new bowling alley game for Fun Day! Your team needs to figure out the PERFECT push to knock down the pins. Too soft and the ball is too slow. Too hard and it zooms past! Use what you learned about force and speed to design the winning push!",
    "stem_questions": [
        "Which push knocked down the most pins?",
        "What happened when you pushed too gently? Too hard?"
    ],
    "stem_design_qs": [
        "How will you line up the pins so the ball can knock them down?",
        "How will you make sure you push the same way each time?",
        "How will you keep track of which push strength worked best?"
    ],
    "career": "Sports Scientists study how athletes throw, kick, and push to go faster and stronger. They help athletes win medals by understanding force and speed! They earn $50,000-$90,000/year.",
    "images": {
        "cover": ("cover-force-speed.png", "A bright orange ball rolling fast across a smooth gym floor with dramatic motion blur lines behind it, vivid warm lighting, close-up ground-level perspective, cinematic sports photography feel"),
        "landscape": ("landscape-force-speed.png", "Diverse kindergarten students (5-6 years old, wide variety of ethnicities including White, Black, Latino, Asian, and mixed-race children) rolling balls across the gym floor with different push strengths, some crouching for gentle taps, some winding up for big pushes, joyful movement"),
        "modeling": ("modeling-force-speed.png", "A simple, colorful kid-friendly diagram showing two scenes: a small hand giving a gentle tap to a ball with a short arrow (slow), and a big hand giving a strong push to a ball with a long arrow (fast), cartoon-style, white background, bold outlines, speed lines"),
        "discussion": ("discussion-force-speed.png", "A Black male teacher sitting on the gym floor with diverse kindergarteners (5-6 years old, wide variety of ethnicities) in a circle, holding a ball and demonstrating a gentle push versus a strong push, animated expressions, bright gym with colorful equipment"),
        "stem": ("stem-force-speed.png", "Diverse kindergarteners (5-6 years old, wide mix of ethnicities) setting up a bowling game with plastic bottles and a ball, testing different push strengths, cheering when pins fall, bright and fun gym or classroom setting")
    },
    "pre_assessment": [
        "Circle the ball that was pushed harder: (picture of a fast-rolling ball with speed lines / picture of a slowly rolling ball)",
        "Draw yourself pushing a ball really hard."
    ],
    "dimensions": [
        ("Science Practice", "Planning and Carrying Out Investigations", "Students plan and conduct a push strength investigation, comparing gentle versus strong pushes on the same ball and observing speed differences."),
        ("Disciplinary Core Idea", "PS2.A Forces and Motion", "Pushes and pulls can have different strengths and directions. A bigger push makes an object move faster than a smaller push applied to the same object."),
        ("Crosscutting Concept", "Cause and Effect", "Students observe that changing push force (cause) directly changes ball speed (effect) — a stronger push produces a faster ball.")
    ],
    "background_intro": "The relationship between force and motion is one of the most fundamental principles in physics. Understanding that bigger forces produce greater changes in motion helps students make sense of everyday experiences — from kicking a soccer ball to pushing a friend on a swing.",
    "background_sections": [
        ("Force and Speed", "Force is any push or pull that acts on an object. When a force is applied to a stationary object, it begins to move. The greater the force, the faster the object moves. This relationship is described by Newton's Second Law of Motion: Force equals mass times acceleration (F = ma). At the kindergarten level, this translates to a simple, observable truth — push harder, and things go faster. A gentle finger tap on a ball gives it very little speed. A strong two-handed push makes the same ball zoom across the room."),
        ("Comparing Different Forces", "Scientists compare forces by changing one variable at a time. In this lesson, students keep the ball the same but change the push strength. This controlled investigation reveals a clear pattern: gentle tap = slow, medium push = medium speed, strong push = fast. This pattern holds true for all objects — the same force principle applies whether you are pushing a ball, swinging a bat, or pedaling a bicycle. By age 5-6, children have extensive intuitive experience with this concept; the lesson helps them articulate and formalize what they already know from play.")
    ],
    "lever_L": "Students identify Push Force as the external component (we choose how hard to push) and Ball Speed as the internal component (the ball's speed changes based on how hard we pushed it).",
    "lever_E": "Students discover that more Push Force leads to faster Ball Speed — a positive relationship.",
    "lever_V": "Students build a simple two-part model connecting Push Force to Ball Speed with a positive arrow.",
    "lever_Ev": "Students test Gentle Tap vs. Power Push and observe the clear difference in how fast the ball rolls.",
    "lever_R": "Students explore what happens when they push different types of balls (heavy basketball vs. light tennis ball) with the same force — does the heavy ball go as fast?",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with a fast-rolling ball and speed lines", "say": "Watch this! (Gently tap a ball.) Now watch THIS! (Push it hard.) What was different? Today we find out WHY harder pushes make things go faster!", "do": "Demonstrate two pushes on the same ball — a tiny tap and a big push. Students describe what they saw. Ask: Which was faster? WHY?", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn?", "visual": "Learning goals with speed and force icons", "say": "Today we learn about FORCE and SPEED! Force is how hard you push. Speed is how fast things go. More force means more speed!", "do": "Introduce 'speed' and 'force.' Practice: tiptoe slowly (slow speed), run in place fast (fast speed). Gentle clap (small force), big clap (big force).", "time": "3 min"},
        {"num": "Slide 3", "title": "Let's Be Scientists!", "visual": "Big question with fast and slow balls", "say": "Our big question is: What happens when you push a ball HARDER? Does it go faster, slower, or the same? Let us investigate!", "do": "Quick prediction vote: hands up for faster, hands down for slower, hands sideways for the same. Most students will correctly predict faster!", "time": "3 min"},
        {"num": "Slide 4", "title": "What Are the Parts?", "visual": "Two component cards: Push Force and Ball Speed", "say": "Our model has two parts. Push Force is how hard we push — WE choose that! Ball Speed is how fast the ball goes — that depends on our push.", "do": "Use sorting mats. Students place Push Force on OUTSIDE and Ball Speed on INSIDE. Practice: show a gentle push motion and a power push motion.", "time": "5 min"},
        {"num": "Slide 5", "title": "How Are They Connected?", "visual": "Arrow from Push Force to Ball Speed", "say": "When Push Force goes UP, Ball Speed goes UP! That is a POSITIVE connection. Harder push means faster ball!", "do": "Line up students for a push test. Each student pushes the same ball gently, then hard. The class observes: Was it faster the second time? YES! Thumbs up for positive.", "time": "5 min"},
        {"num": "Slide 6", "title": "What Did We Find Out?", "visual": "Key discoveries with speed comparison illustrations", "say": "We discovered the secret to speed — FORCE! A bigger push gives the ball more speed. A tiny push gives only a tiny bit of speed. This works for EVERYTHING!", "do": "Chant: 'When Push Force goes up, Ball Speed goes up!' Complete sentence frame. Students show force with body — gentle push gesture, then POWER push gesture.", "time": "5 min"},
        {"num": "Slide 7", "title": "STEM Challenge", "visual": "Speed Bowling challenge with ramp and pins", "say": "Time for Speed Bowling! Line up the pins and find the PERFECT push. Too gentle and the ball stops short. Too hard and it goes too fast. Find the sweet spot!", "do": "Set up plastic bottle pins. Students take turns pushing a ball at the pins. Try gentle, medium, and strong pushes. Record which push worked best using smiley faces. Crown a Speed Bowling Champion!", "time": "10 min"}
    ],
    "sort_reasoning": "Push Force is outside because WE choose how hard to push the ball — that is our decision. Ball Speed is inside because the ball's speed changes on its own based on how hard we pushed it.",
    "relationships": [
        ("Push Force to Ball Speed", "POSITIVE (+)", "When you push harder, the ball rolls faster because a bigger force transfers more energy to the ball, making it speed up more.")
    ],
    "sim_answers": [
        ("Gentle Tap", "When Push Force is low, Ball Speed is slow. The ball barely rolls because the tiny push did not give it much energy to move."),
        ("Power Push", "When Push Force is high, Ball Speed is fast. The ball zooms across the floor because the big push gave it lots of energy!")
    ],
    "stem_intro": "In this challenge, students apply their understanding of force and speed to a bowling game. They must calibrate their push force to knock down pins — testing the direct relationship between force and speed in a fun, competitive context.",
    "stem_concepts": [
        ("Force and Speed Relationship", "The harder you push an object, the faster it moves. This is one of the most fundamental laws of physics — Newton's Second Law — and students experience it firsthand through repeated push trials."),
        ("Precision Engineering", "Real engineers must control forces precisely. Too much force or too little force both cause problems. Finding the right amount of force for a task is a key engineering skill.")
    ],
    "stem_eval": [
        ("Expert (4)", "Student tests multiple push strengths, finds the best one for knocking down pins, and explains that harder pushes make the ball go faster because more force means more speed."),
        ("Proficient (3)", "Student tests different push strengths and identifies that a medium or strong push works best, connecting force to ball speed."),
        ("Developing (2)", "Student pushes the ball and knocks down pins but does not purposefully adjust force between attempts."),
        ("Beginning (1)", "Student rolls the ball at the pins but does not yet connect push strength to how fast the ball goes.")
    ],
    "support": [
        "Place the pins very close (2-3 feet away) so even a gentle push can reach them",
        "Use a ramp instead of a hand push — students place the ball at different heights on the ramp to control force",
        "Provide hand-over-hand support for students who have difficulty controlling push strength"
    ],
    "extensions": [
        "Test with different balls — a tennis ball, a basketball, and a marble. Which needs the most force to knock down pins?",
        "Add a speed measurement: place tape marks at different distances and see which push strength gets the ball past each mark",
        "Connect to real sports: How does a soccer player kick the ball harder? A baseball player throw faster? They use more FORCE!"
    ],
    "cross_curr": [
        ("Math", "Count pins knocked down for each push strength and make a simple bar graph: Gentle (2 pins), Medium (4 pins), Strong (6 pins)"),
        ("ELA", "Read aloud 'Roll, Slope, and Slide' by Michael Dahl and discuss how pushes make things move in different ways"),
        ("Art", "Create speed art — dip a ball in paint, roll it gently across paper for slow lines, then push it hard for fast splatter lines. Compare the results!")
    ],
    "misconceptions": [
        ("Heavy things always go slower", "A heavy ball pushed with a strong force can go very fast. Weight does not determine speed — force does. A bowling ball rolls fast because the bowler pushes it hard. The same ball would barely move with a gentle tap. Speed depends on how much force is applied, not just how heavy the object is.", "Push a heavy ball gently — it goes slowly. Push the same heavy ball hard — it goes fast! Ask: Did the ball get lighter? No! What changed? The PUSH was harder! Weight stayed the same but speed changed because of force."),
        ("Once you push something it will go forever", "Objects slow down and stop because of friction — the rubbing between the ball and the floor. Friction is a force that works against motion. On a smooth floor, the ball rolls farther because there is less friction. On carpet, it stops sooner because there is more friction.", "Roll a ball on the smooth gym floor — it goes far! Roll the same ball on the carpet — it stops quickly. Ask: Why did it stop sooner on carpet? The carpet is bumpy and rough — it RUBS against the ball and slows it down. That is called friction!")
    ],
    "sentence_frame": "When Push Force goes up, Ball Speed goes _______.",
    "coloring_description": "Color the hand pushing the ball. Draw short arrows behind the slow ball and long arrows behind the fast ball. Color the bowling pins at the end!"
}

ALL_LESSONS = [L01, L02, L03, L04, L05, L06, L07, L08, L09, L10]
