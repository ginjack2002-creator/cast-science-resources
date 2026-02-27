#!/usr/bin/env python3
"""Complete lesson data for G02-L01 through G02-L10 (Grade 2 ModelIt! Lessons)"""

L01 = {
    "id": "G02-L01",
    "title": "Can You Bend Water?",
    "subtitle": "Exploring the Properties of Matter",
    "ngss": "2-PS1-1",
    "ngss_desc": "Plan and conduct an investigation to describe and classify different kinds of materials by their observable properties.",
    "big_question": "Can water bend, stretch, or change shape — and what does that tell us about matter?",
    "objectives": [
        "Observe and describe how water behaves when poured into different containers",
        "Classify materials as solids or liquids based on their observable properties",
        "Explain that liquids take the shape of their container because their tiny parts move freely"
    ],
    "vocabulary": [
        ("Matter", "Anything you can touch, hold, or feel — it takes up space"),
        ("Property", "Something you can observe about an object, like its color, shape, or how it feels"),
        ("Liquid", "A type of matter that flows and takes the shape of whatever container it is in"),
        ("Solid", "A type of matter that keeps its own shape no matter where you put it")
    ],
    "components": [
        ("Container Shape", "The shape of the cup, bowl, or jar you pour water into — tall, wide, round, or flat", True),
        ("Water Shape", "The shape the water takes after being poured — it changes to match the container", False),
        ("Water Level", "How high the water fills up in the container — changes depending on the container shape", False)
    ],
    "think_about_it": "When you change the container shape, what happens to the water shape? Does water keep its old shape or take a new one?",
    "scenarios": [
        ("Tall Skinny Cup", "Pour water into a tall skinny cup and observe what shape the water takes"),
        ("Wide Flat Bowl", "Pour the same water into a wide flat bowl and observe how the shape changes")
    ],
    "sim_scenarios": [
        ("Tall Skinny Cup", "Container Shape set to tall and narrow", "What do you predict will happen to the Water Shape when you pour it into a tall skinny cup?"),
        ("Wide Flat Bowl", "Container Shape set to wide and flat", "What do you predict will happen to the Water Level when the same water goes into a wide flat bowl?"),
        ("Round Jar", "Container Shape set to round", "Will the water be the same shape as the tall cup? Why or why not?")
    ],
    "discoveries": [
        "Water always takes the shape of its container — it does not have its own fixed shape",
        "The amount of water stays the same even when the shape changes",
        "Solids keep their shape, but liquids flow and fill the space they are given",
        "Properties like shape help us tell the difference between solids and liquids"
    ],
    "answer": "Water does not really bend — but it FLOWS! Liquids like water do not have a fixed shape. When you pour water into a new container, it takes the shape of that container. This is a property that makes liquids different from solids. Solids keep their own shape, but liquids always change to fit!",
    "stem_title": "Design a Water Maze",
    "stem_mission": "Build a water maze that moves water through at least three different container shapes to show how liquid changes shape.",
    "stem_scenario": "A water park needs a new attraction that shows visitors how cool water is! Your team has been asked to build a mini water maze that moves water through different shapes. Use what you learned about liquid properties to explain your design.",
    "stem_questions": [
        "What shapes will you use for each part of your water maze?",
        "Will the water look the same in every part of the maze? Why or why not?",
        "How can you prove the amount of water stays the same even when the shape changes?"
    ],
    "stem_design_qs": [
        "What materials will you use to build your containers?",
        "How will you move the water from one shape to the next?",
        "How will you keep the water from spilling between containers?",
        "How will you show visitors that the water changed shape but the amount stayed the same?"
    ],
    "career": "Materials Scientists study the properties of different materials to help make new products, from water bottles to building materials. They earn $55,000–$100,000/year.",
    "images": {
        "cover": ("cover-water.png", "A close-up of crystal-clear water being poured between colorful containers of different shapes, bright studio lighting, vivid colors, clean white background"),
        "landscape": ("landscape-water.png", "Diverse 2nd grade students (7-8 years old, wide variety of ethnicities) excitedly pouring water between different shaped containers at a science table in a bright modern classroom, natural window light, editorial photo quality"),
        "modeling": ("modeling-water.png", "A colorful kid-friendly scientific diagram showing water molecules moving freely inside different shaped containers — a tall cup, a flat bowl, and a round jar — cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-water.png", "A teacher with diverse 2nd graders (7-8 years old, wide variety of ethnicities) sitting in a circle discussing why water changes shape, teacher holding a clear cup of water, bright classroom"),
        "stem": ("stem-water.png", "Diverse 2nd graders (7-8 years old, wide mix of ethnicities) building water mazes from plastic cups, funnels, and tubes on a table covered in towels, excited collaborative group work")
    },
    "pre_assessment": [
        "What happens to the shape of water when you pour it from a cup into a bowl?",
        "Can you bend a rock? Can you bend water? What is different about them?",
        "Draw what you think water looks like inside a tall cup and inside a flat plate."
    ],
    "reflections": [
        "What surprised you most about how water changes shape?",
        "How is water different from a block of wood when you put them in a new container?"
    ],
    "reflection_exemplars": [
        ("How is water different from a block of wood when you put them in a new container?", "Water flows and fills up the container, taking its shape. A block of wood stays the same shape no matter what container you put it in. Water is a liquid so its tiny parts move around freely, but wood is a solid so its parts are stuck together and keep their shape.")
    ],
    "cast_items": [
        "Describe how water changes shape when poured into different containers",
        "Classify materials as solids or liquids based on their properties",
        "Explain why liquids behave differently than solids"
    ],
    "cast_questions": [
        ("Multiple Choice:", "You pour water from a tall skinny glass into a wide flat bowl. What happens to the shape of the water?"),
        ("Constructed Response:", "Explain how you can tell the difference between a solid and a liquid by observing their properties. Use an example from your investigation.")
    ],
    "extend_components": [
        ("Temperature", "How hot or cold the water is — cold water moves more slowly than warm water"),
        ("Amount of Water", "How much water you have — more water fills more of the container"),
        ("Container Material", "What the container is made of — some materials absorb water and some do not")
    ],
    "dimensions": [
        ("Science Practice", "Planning and Carrying Out Investigations", "Students investigate how water changes shape by pouring it into different containers and recording their observations."),
        ("Disciplinary Core Idea", "PS1.A Structure and Properties of Matter", "Different kinds of matter exist and many of them can be either solid or liquid depending on temperature. Matter can be described and classified by its observable properties."),
        ("Crosscutting Concept", "Patterns", "Students observe the pattern that liquids always take the shape of their container while solids do not.")
    ],
    "background_intro": "Matter is everything around us — the air we breathe, the water we drink, and the ground we walk on. Understanding the properties of matter helps young scientists classify and describe the world.",
    "background_sections": [
        ("What Is Matter?", "Matter is anything that takes up space and has weight. Everything you can see, touch, and feel is made of matter — your desk, your pencil, the air around you, and even you! Scientists sort matter into groups based on properties we can observe, like shape, color, texture, and whether it flows."),
        ("Solids and Liquids", "Solids have a fixed shape. A crayon stays crayon-shaped whether it is on your desk or in your backpack. Liquids flow and take the shape of whatever container they are in. Water in a cup is cup-shaped, but the same water poured into a bowl becomes bowl-shaped. The amount of matter does not change — only the shape does."),
        ("Why Do Liquids Flow?", "Inside every liquid, tiny pieces of matter (too small to see) are constantly moving and sliding past each other. Because these tiny pieces are not locked in place, the liquid can flow and fill any shape. In a solid, the tiny pieces are locked tightly together, so the solid keeps its shape.")
    ],
    "lever_L": "Students identify container shape as an external component and water shape and water level as internal components that change in response to the container.",
    "lever_E": "Students determine that changing the container shape causes the water shape to change (positive relationship), and that a wider container means a lower water level for the same amount of water.",
    "lever_V": "Students build a model showing how pouring water into different containers changes its shape but not the total amount.",
    "lever_Ev": "Students run tall cup, wide bowl, and round jar scenarios to see how the same water looks different in each container.",
    "lever_R": "Students add temperature or amount of water to explore how other factors affect what they observe.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with colorful water images", "say": "Who here has ever tried to grab water? What happened? Could you hold it in your hands?", "do": "Let students share. If possible, have a small tub of water for a quick demo.", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn Today?", "visual": "Learning goals and vocabulary words", "say": "Today we are going to figure out something really cool about water — can it change shape?", "do": "Read objectives aloud together. Introduce the words matter, property, liquid, and solid with hand motions.", "time": "3 min"},
        {"num": "Slide 3", "title": "The Big Question", "visual": "Can water bend, stretch, or change shape?", "say": "Here is our big question: Can you bend water? What do you think?", "do": "Thumbs up or thumbs down: Can you bend water? Have 2-3 students share their thinking.", "time": "3 min"},
        {"num": "Slide 4", "title": "Let's Build a Model!", "visual": "LEVER steps overview", "say": "We are going to build a model to figure this out — step by step, like real scientists.", "do": "Preview each step briefly. Remind students that models help us understand how things work.", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Sort the Parts", "visual": "Component cards: Container Shape, Water Shape, Water Level", "say": "What are the parts of our experiment? Which part do WE control, and which parts change on their own?", "do": "Guide students to sort Container Shape as external (we pick it) and Water Shape and Water Level as internal (they change by themselves).", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect with Arrows", "visual": "Relationship arrows between components", "say": "When we change the container shape, what happens to the water shape? Does it change or stay the same?", "do": "Help students draw arrows from Container Shape to Water Shape and Water Level. Discuss whether the change is positive or negative.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Run the Simulation!", "visual": "Simulation predictions and results", "say": "Time to test! Let us start by pouring water into a tall skinny cup. What do you think will happen?", "do": "Have students predict first, then run each scenario. Use real containers if possible. Compare tall cup vs. flat bowl vs. round jar.", "time": "8 min"},
        {"num": "Slide 8", "title": "What Did We Discover?", "visual": "Key discoveries and answer to big question", "say": "So can you bend water? Not exactly — but water does something even cooler. It FLOWS into any shape!", "do": "Review discoveries together. Compare water to a solid object like a block. Have students share one thing they learned with a partner.", "time": "7 min"}
    ],
    "sort_reasoning": "Container Shape is external because we choose which container to use — it is a decision we make before the experiment starts. Water Shape and Water Level are internal because they change on their own when the water is poured into a new container.",
    "relationships": [
        ("Container Shape to Water Shape", "POSITIVE (+)", "When you change the container shape, the water shape changes to match it. A tall container makes the water tall; a flat container makes the water flat. The water always copies the container."),
        ("Container Shape to Water Level", "NEGATIVE (-)", "When the container gets wider, the water level gets lower because the same amount of water spreads out more. A narrow container pushes the water up higher.")
    ],
    "sim_answers": [
        ("Tall Skinny Cup", "When Container Shape is set to tall and narrow, Water Shape becomes tall and narrow to match. Water Level is high because the water is squeezed into a small space. The water fills up the skinny cup and rises to a high level."),
        ("Wide Flat Bowl", "When Container Shape is set to wide and flat, Water Shape becomes wide and flat. Water Level is low because the same amount of water spreads out across the wide bottom. The water barely covers the bottom of the big bowl.")
    ],
    "stem_intro": "Present the challenge: A water park needs a new attraction that shows visitors how cool water is! Your team will build a mini water maze that moves water through at least three different container shapes to show how liquid changes shape.",
    "stem_concepts": [
        ("Liquids Take Container Shape", "Water has no shape of its own. It always takes the shape of whatever container it is in. Your water maze should show water changing shape at least three times."),
        ("Amount Stays the Same", "Even though the shape changes, the amount of water does not change. If you start with one cup of water, you still have one cup at the end — just in a different shape."),
        ("Flow and Gravity", "Water flows downhill because of gravity. Your maze can use gravity to move water from one container to the next.")
    ],
    "stem_eval": [
        ("Expert (4)", "Water maze has 3+ container shapes, student explains that water takes the container shape and the amount stays the same"),
        ("Proficient (3)", "Water maze works with at least 3 shapes and student can describe how the water shape changed"),
        ("Developing (2)", "Water maze has containers but student has difficulty explaining why the water changed shape"),
        ("Beginning (1)", "Water maze is incomplete or student cannot explain what happened to the water")
    ],
    "support": [
        "Provide pre-labeled component cards with pictures so students can sort without reading difficulty",
        "Use real containers and water for hands-on experience before the digital model",
        "Sentence frame: 'When I pour water into a ___, the water shape becomes ___ because ___'"
    ],
    "extensions": [
        "Try pouring water into unusual containers like a glove or a ziplock bag — what shape does it take?",
        "Compare water to sand — does sand take the shape of its container like water does?",
        "Investigate what happens when you freeze water — does it still take the container shape?"
    ],
    "cross_curr": [
        ("Math", "Measure the water level in different containers using a ruler and compare the numbers — same water, different heights!"),
        ("ELA", "Write a short story about a water drop that travels through different containers and changes shape each time"),
        ("Art", "Draw and color the water in three different container shapes, showing how the same water looks different each time")
    ],
    "misconceptions": [
        ("Water disappears when you pour it out", "Water does not disappear — it moves! When you pour water from one container to another, all the water is still there. It just changed shape and location. If water spills, it spreads out on the surface but it is still there.", "Pour water from a cup into a bowl in front of students. Ask: Did any water disappear? Where did it all go?"),
        ("Water has its own shape", "Water does NOT have a fixed shape like a block or a ball. Water is a liquid, which means it takes the shape of whatever container holds it. If there is no container, water flows and spreads out flat because of gravity.", "Show water in three different containers. Ask: Is the water the same shape each time? Why not?"),
        ("Bigger containers have more water", "A bigger container does not mean more water. The same amount of water just looks different in different containers. In a tall skinny cup the water looks like a lot because it is high, but in a wide bowl it looks like less even though it is the same amount.", "Pour the same measured cup of water into a tall glass and then a wide bowl. Ask: Which has more water? Surprise — it is the same!")
    ]
}

L02 = {
    "id": "G02-L02",
    "title": "Where Did the Puddle Go?",
    "subtitle": "How Heating and Cooling Change Matter",
    "ngss": "2-PS1-4",
    "ngss_desc": "Construct an argument with evidence that some changes caused by heating or cooling can be reversed and some cannot.",
    "big_question": "When a puddle disappears on a sunny day, where does the water actually go?",
    "objectives": [
        "Describe what happens to water when it is heated by the sun",
        "Explain that water can change from liquid to gas when heated and back again when cooled",
        "Give an example of a change caused by heating that can be reversed"
    ],
    "vocabulary": [
        ("Evaporation", "When liquid water heats up and turns into an invisible gas called water vapor"),
        ("Water Vapor", "Water in the form of a gas — you cannot see it, but it is in the air all around us"),
        ("Condensation", "When water vapor cools down and turns back into tiny drops of liquid water"),
        ("Reversible", "A change that can be undone — like freezing water and then melting it back")
    ],
    "components": [
        ("Sun Heat", "How much heat energy comes from the sun — more sun means more heat on the puddle", True),
        ("Evaporation Speed", "How quickly the puddle water turns into water vapor and goes into the air", False),
        ("Puddle Size", "How big the puddle is — it gets smaller as water evaporates into the air", False)
    ],
    "think_about_it": "When the sun heat increases, what happens to evaporation speed? What happens to puddle size?",
    "scenarios": [
        ("Sunny Day", "Set Sun Heat to high and observe what happens to the puddle over time"),
        ("Cloudy Day", "Set Sun Heat to low and observe how the evaporation speed and puddle size change")
    ],
    "sim_scenarios": [
        ("Sunny Day", "Sun Heat set to high", "What do you predict will happen to the Puddle Size when the sun is very hot?"),
        ("Cloudy Day", "Sun Heat set to low", "What do you predict will happen to Evaporation Speed when there is not much sun?"),
        ("Partly Cloudy", "Sun Heat set to medium", "Will the puddle disappear faster or slower than on a sunny day?")
    ],
    "discoveries": [
        "Heat from the sun causes puddle water to evaporate — it turns into invisible water vapor",
        "On hot sunny days, puddles disappear faster because evaporation speed increases",
        "The water did not disappear forever — it went into the air as water vapor",
        "When water vapor cools down, it can turn back into liquid water (condensation) — this change is reversible"
    ],
    "answer": "The puddle did not really disappear! Heat from the sun gave the water energy to change from a liquid into an invisible gas called water vapor. The water floated up into the air. This is called evaporation. When that water vapor cools down high in the sky, it can turn back into tiny water droplets and form clouds. The change is reversible!",
    "stem_title": "Build a Mini Water Cycle",
    "stem_mission": "Design a sealed container that shows evaporation and condensation happening — your own mini water cycle!",
    "stem_scenario": "A science museum wants a simple display that shows kids where puddles go. Your team will build a mini water cycle in a sealed container so visitors can watch water evaporate and condense over and over again.",
    "stem_questions": [
        "Where will you put the heat source to make evaporation happen?",
        "Where will the water vapor go inside your sealed container?",
        "How will you know when condensation is happening?"
    ],
    "stem_design_qs": [
        "What kind of sealed container will you use — a bag, a jar, or a plastic box?",
        "How will you add heat — sunlight, a lamp, or warm water?",
        "Where will you look for condensation — on the lid, on the sides, or somewhere else?",
        "How will you prove that the water that evaporated is the same water that condensed?"
    ],
    "career": "Meteorologists study weather and predict when it will rain, snow, or be sunny. They use science about evaporation and condensation every day. They earn $50,000–$95,000/year.",
    "images": {
        "cover": ("cover-puddle.png", "A close-up of a puddle on a playground with the bright sun reflecting off the water surface, steam wisps rising from the puddle, vivid colors, cinematic outdoor photography"),
        "landscape": ("landscape-puddle.png", "Diverse 2nd grade students (7-8 years old, wide variety of ethnicities) crouching around a puddle on a sunny playground, pointing at it and looking curious, natural sunlight, editorial photo quality"),
        "modeling": ("modeling-puddle.png", "A colorful kid-friendly scientific diagram showing the journey of a water droplet from a puddle up into the air as vapor then forming a cloud — cartoon-style, white background, bold outlines, arrows showing the path"),
        "discussion": ("discussion-puddle.png", "A teacher with diverse 2nd graders (7-8 years old, wide variety of ethnicities) looking at a foggy window in a classroom, discussing condensation, bright modern classroom"),
        "stem": ("stem-puddle.png", "Diverse 2nd graders (7-8 years old, wide mix of ethnicities) building mini water cycles in sealed plastic bags with water and blue food coloring, taping them to a sunny window, excited faces")
    },
    "pre_assessment": [
        "Have you ever noticed a puddle after rain? What happened to it later?",
        "Where do you think the water goes when a puddle dries up?",
        "Draw what you think happens to puddle water on a hot sunny day."
    ],
    "reflections": [
        "Where is the puddle water right now if it is not on the ground anymore?",
        "How is what happened to the puddle similar to what happens when you breathe on a cold window?"
    ],
    "reflection_exemplars": [
        ("Where is the puddle water right now if it is not on the ground anymore?", "The puddle water turned into water vapor, which is an invisible gas in the air. The sun heated the water and gave it enough energy to evaporate. The water is still here — we just cannot see it because it is a gas now. When it cools down, it can become liquid water again.")
    ],
    "cast_items": [
        "Describe what happens to a puddle on a sunny day",
        "Explain the difference between evaporation and condensation",
        "Give an example of a reversible change caused by heating"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A puddle on the playground gets smaller and smaller on a sunny day. Where did the water go?"),
        ("Constructed Response:", "Explain what happens to water in a puddle when the sun heats it up. Use the words 'evaporation' and 'water vapor' in your answer.")
    ],
    "extend_components": [
        ("Wind Speed", "How fast the air is moving over the puddle — wind helps carry water vapor away faster"),
        ("Puddle Depth", "How deep the puddle is at the start — deeper puddles take longer to evaporate")
    ],
    "dimensions": [
        ("Science Practice", "Constructing Explanations", "Students construct an explanation for where puddle water goes, using evidence from their model about heating and evaporation."),
        ("Disciplinary Core Idea", "PS1.B Chemical Reactions", "Heating or cooling a substance may cause changes that can be observed. Sometimes these changes are reversible, and sometimes they are not."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify that heat from the sun causes water to evaporate, and cooling causes water vapor to condense.")
    ],
    "background_intro": "Water is always on the move! It travels from puddles to the sky and back again in a never-ending journey. Understanding how heating and cooling change water helps us explain weather, clouds, and rain.",
    "background_sections": [
        ("Evaporation: Liquid to Gas", "When the sun heats water, it gives the water energy. The water molecules at the surface start moving faster and faster until they escape into the air as water vapor — an invisible gas. This process is called evaporation. It happens all the time, but it happens faster when it is hot, windy, or dry."),
        ("Condensation: Gas to Liquid", "When water vapor rises into the sky, it cools down. As it cools, the water molecules slow down and clump back together into tiny liquid droplets. This is condensation. You can see condensation on a cold glass of water on a hot day — those water drops on the outside come from water vapor in the air cooling down on the cold glass."),
        ("Reversible Changes", "Evaporation and condensation are reversible changes. The water can go from liquid to gas and back to liquid over and over again. Freezing and melting are also reversible — ice melts into water, and water can freeze back into ice. Not all changes are reversible though — you cannot un-bake a cookie!")
    ],
    "lever_L": "Students identify sun heat as an external component and evaporation speed and puddle size as internal components that change when the sun heats the puddle.",
    "lever_E": "Students determine that more sun heat causes faster evaporation (positive), and faster evaporation causes the puddle to get smaller (negative — puddle size decreases).",
    "lever_V": "Students build a model showing how the sun's heat drives evaporation, which shrinks the puddle over time.",
    "lever_Ev": "Students run sunny day and cloudy day scenarios to compare how fast puddles disappear under different heat conditions.",
    "lever_R": "Students add wind speed or puddle depth to explore other factors that affect how quickly puddles evaporate.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with puddle and sunshine imagery", "say": "Have you ever seen a puddle after it rains? What happens to it the next day?", "do": "Let students share their observations about puddles. Show a time-lapse of a puddle evaporating if available.", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn Today?", "visual": "Learning goals and vocabulary words", "say": "Today we are going to solve a mystery — where do puddles go when they dry up?", "do": "Read objectives together. Introduce evaporation, water vapor, condensation, and reversible with gestures.", "time": "3 min"},
        {"num": "Slide 3", "title": "The Big Question", "visual": "Where did the puddle go?", "say": "When a puddle disappears on a sunny day, does the water just vanish? Where does it go?", "do": "Think-pair-share: Where do you think puddle water goes? Collect ideas on the board.", "time": "3 min"},
        {"num": "Slide 4", "title": "Let's Build a Model!", "visual": "LEVER steps overview", "say": "Let us build a model to track where the puddle water goes — step by step.", "do": "Preview each LEVER step. Remind students that scientists use models to explain things they cannot easily see.", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Sort the Parts", "visual": "Component cards: Sun Heat, Evaporation Speed, Puddle Size", "say": "What makes a puddle disappear? What parts are involved? Which part do we control?", "do": "Guide students to sort Sun Heat as external and Evaporation Speed and Puddle Size as internal.", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect with Arrows", "visual": "Arrows between components", "say": "When there is more sun heat, does the puddle evaporate faster or slower? Does the puddle get bigger or smaller?", "do": "Draw positive arrow from Sun Heat to Evaporation Speed. Draw negative arrow from Evaporation Speed to Puddle Size.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Run the Simulation!", "visual": "Simulation predictions and results", "say": "Let us test our model! First a super sunny day, then a cloudy day. What do you predict?", "do": "Students predict then run scenarios. Compare sunny vs. cloudy results. Discuss why the difference.", "time": "8 min"},
        {"num": "Slide 8", "title": "What Did We Discover?", "visual": "Key discoveries and answer", "say": "The puddle water did not disappear — it just changed into something invisible! Who can tell me what it became?", "do": "Breathe on a cold window or mirror to show condensation. Connect evaporation and condensation as reverse processes.", "time": "7 min"}
    ],
    "sort_reasoning": "Sun Heat is external because it comes from outside the puddle system — we cannot control the sun, but it is the input that drives the changes. Evaporation Speed and Puddle Size are internal because they change as a result of how much heat the puddle receives.",
    "relationships": [
        ("Sun Heat to Evaporation Speed", "POSITIVE (+)", "More sun heat gives the water more energy, making it evaporate faster. On a hot day the puddle dries up quickly because the sun is heating the water and turning it to vapor faster."),
        ("Evaporation Speed to Puddle Size", "NEGATIVE (-)", "When evaporation is faster, the puddle gets smaller more quickly. The water is leaving the puddle and going into the air, so the puddle shrinks.")
    ],
    "sim_answers": [
        ("Sunny Day", "When Sun Heat is high, Evaporation Speed is fast and Puddle Size shrinks quickly. The strong sun gives the water lots of energy so it turns into water vapor fast. The puddle almost disappears!"),
        ("Cloudy Day", "When Sun Heat is low, Evaporation Speed is slow and Puddle Size stays large for a long time. Without much sun, the water does not get enough energy to evaporate quickly. The puddle is still there hours later.")
    ],
    "stem_intro": "Present the challenge: A science museum wants a display that shows kids where puddles go. Your team will build a mini water cycle in a sealed container so visitors can watch water evaporate and condense right before their eyes!",
    "stem_concepts": [
        ("Evaporation Needs Heat", "Water turns into vapor when it gets enough heat energy. In your mini water cycle, you need a heat source like sunlight or a lamp to make evaporation happen."),
        ("Condensation Needs Cooling", "When water vapor hits a cool surface, it turns back into liquid drops. Look for condensation on the top or sides of your container."),
        ("The Water Cycle Is Reversible", "Water goes from liquid to gas and back to liquid over and over. Your sealed container should show this cycle repeating.")
    ],
    "stem_eval": [
        ("Expert (4)", "Mini water cycle clearly shows both evaporation and condensation, and student explains the cycle using vocabulary words"),
        ("Proficient (3)", "Mini water cycle works and student can describe evaporation and condensation happening inside"),
        ("Developing (2)", "Mini water cycle is built but student has trouble explaining what is happening to the water"),
        ("Beginning (1)", "Mini water cycle is incomplete or student cannot describe what happened to the water")
    ],
    "support": [
        "Place two wet paper towels — one in the sun and one in the shade — so students can see evaporation happen at different speeds",
        "Use blue food coloring in the water so students can see the liquid more easily inside containers",
        "Sentence frame: 'The sun heats the water, so it ___ and turns into ___'"
    ],
    "extensions": [
        "Investigate whether puddles dry up faster in the sun, in the shade, or when a fan blows on them",
        "Leave a shallow dish of water on a windowsill and measure how much disappears each day for a week",
        "Research how clouds form from evaporated water and draw the water cycle"
    ],
    "cross_curr": [
        ("Math", "Measure the puddle width each hour using a ruler and graph how it changes over time"),
        ("ELA", "Write a diary entry as a water drop — describe your journey from a puddle up into the sky and back down as rain"),
        ("Art", "Paint a before and after picture showing a playground with a puddle and then the same playground on a sunny day")
    ],
    "misconceptions": [
        ("The puddle water is gone forever", "The water did not disappear — it changed form! It turned into an invisible gas called water vapor through evaporation. The water is still in the air around us, and it can turn back into liquid when it cools down.", "Breathe on a cold mirror — see the water drops? That water was invisible vapor in your breath until it hit the cold surface!"),
        ("Only boiling water makes steam or vapor", "Water does not have to boil to evaporate! Evaporation happens at any temperature — even on cool days. The sun slowly gives water enough energy for some molecules to escape into the air. Boiling just makes it happen much faster.", "Leave a wet paper towel out — it dries without boiling! The water evaporated slowly into the air."),
        ("Water vapor is the same as clouds or steam you can see", "Real water vapor is completely invisible — you cannot see it at all. The white mist you see above a boiling pot or in clouds is actually tiny liquid water droplets, not vapor. True water vapor is a gas hiding in the air.", "Point to the space just above a pot of hot water — the invisible gap right above the surface is water vapor. The white mist higher up is condensed droplets!")
    ]
}

L03 = {
    "id": "G02-L03",
    "title": "Why Do Some Seeds Travel Far?",
    "subtitle": "The Amazing Ways Seeds Move to New Places",
    "ngss": "2-LS2-2",
    "ngss_desc": "Develop a simple model that mimics the function of an animal in dispersing seeds or pollinating plants.",
    "big_question": "How do seeds travel to new places if plants cannot walk, run, or fly?",
    "objectives": [
        "Describe at least two ways seeds travel from the parent plant to a new place",
        "Explain how seed shape helps seeds move by wind, water, or animals",
        "Build a simple model showing how seed shape affects how far it travels"
    ],
    "vocabulary": [
        ("Seed Dispersal", "When seeds move away from the parent plant to a new place where they can grow"),
        ("Adaptation", "A body part or feature that helps a living thing survive — like wings on a seed for flying"),
        ("Dispersal Agent", "Something that carries seeds to new places — like wind, water, or animals")
    ],
    "components": [
        ("Seed Shape", "The shape and features of the seed — wings, hooks, fluff, or heavy shell", True),
        ("Wind Interaction", "How the seed moves through the air — floaty seeds stay up longer", True),
        ("Travel Distance", "How far the seed gets from the parent plant — farther means more chance to find a good spot to grow", False)
    ],
    "think_about_it": "When a seed has a fluffy or winged shape, what happens to how far it travels in the wind? Is that positive or negative?",
    "scenarios": [
        ("Fluffy Dandelion Seed", "Set Seed Shape to fluffy and Wind Interaction to breezy, then observe Travel Distance"),
        ("Heavy Acorn", "Set Seed Shape to heavy round and Wind Interaction to breezy, then observe Travel Distance")
    ],
    "sim_scenarios": [
        ("Fluffy Dandelion Seed", "Seed Shape is fluffy, Wind is breezy", "What do you predict will happen to Travel Distance when a fluffy seed is in the wind?"),
        ("Heavy Acorn", "Seed Shape is heavy round, Wind is breezy", "What do you predict will happen to Travel Distance when a heavy acorn is in the wind?"),
        ("Helicopter Maple Seed", "Seed Shape is winged, Wind is breezy", "Will a winged seed travel more like the fluffy seed or the acorn?")
    ],
    "discoveries": [
        "Seeds with fluffy or winged shapes travel farther in the wind than heavy round seeds",
        "The shape of a seed is an adaptation that helps it get to a new place to grow",
        "Different seeds use different methods — wind, water, animals, or even popping open",
        "Seeds need to travel away from the parent plant so they have enough room, sunlight, and water to grow"
    ],
    "answer": "Plants cannot walk, but their seeds have amazing adaptations for travel! Fluffy seeds like dandelions float on the wind. Winged seeds like maples spin through the air like helicopters. Sticky or hooked seeds hitch rides on animal fur. Seeds need to travel so they can find a new place with enough sunlight, water, and space to grow!",
    "stem_title": "Design a Super Seed",
    "stem_mission": "Design and build a seed model that can travel as far as possible when dropped from the same height.",
    "stem_scenario": "A nature center wants to teach visitors about seed dispersal. Your team will design a model seed that travels the farthest when dropped from shoulder height. Use what you learned about seed shape and wind to make your design!",
    "stem_questions": [
        "What shape will help your seed travel the farthest — fluffy, winged, or something else?",
        "How does making your seed lighter or heavier change how far it goes?",
        "Why is it important for real seeds to travel far away from the parent plant?"
    ],
    "stem_design_qs": [
        "What materials will you use — paper, cotton balls, tissue paper, pipe cleaners?",
        "What shape will your seed be and why did you choose that shape?",
        "How will you test whether your seed design travels far?",
        "How can you make your seed travel even farther after the first test?"
    ],
    "career": "Botanists study plants and how they grow, spread, and survive. They work in forests, gardens, labs, and farms to help plants thrive. They earn $45,000–$85,000/year.",
    "images": {
        "cover": ("cover-seeds.png", "A close-up of a dandelion puff with seeds floating away against a bright blue sky, golden sunlight, cinematic macro photography, vivid detail"),
        "landscape": ("landscape-seeds.png", "Diverse 2nd grade students (7-8 years old, wide variety of ethnicities) outside on a school field examining different seeds they collected — dandelion puffs, maple helicopters, acorns — natural sunlight, editorial photo quality"),
        "modeling": ("modeling-seeds.png", "A colorful kid-friendly scientific diagram showing three types of seed dispersal — a fluffy seed in wind, a sticky seed on animal fur, and a heavy seed falling — cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-seeds.png", "A teacher with diverse 2nd graders (7-8 years old, wide variety of ethnicities) sitting in a circle looking at real seeds on a tray, teacher holding a dandelion puff, bright classroom with plant posters"),
        "stem": ("stem-seeds.png", "Diverse 2nd graders (7-8 years old, wide mix of ethnicities) building model seeds from paper, cotton balls, and pipe cleaners at their desks, testing by dropping them, excited expressions")
    },
    "pre_assessment": [
        "How do you think seeds get to new places if plants cannot move?",
        "Have you ever blown on a dandelion? What happened to the seeds?",
        "Draw a seed that you think could travel very far — what features does it have?"
    ],
    "reflections": [
        "Why is it important for seeds to travel away from the parent plant?",
        "Which seed design surprised you the most — the fluffy, winged, or heavy one?"
    ],
    "reflection_exemplars": [
        ("Why is it important for seeds to travel away from the parent plant?", "Seeds need to travel away so they can find their own space to grow. If all the seeds just fell right under the parent plant, they would be too crowded. They would have to share sunlight, water, and soil nutrients. By traveling far, seeds find new spots with plenty of room and resources to grow into healthy plants.")
    ],
    "cast_items": [
        "Describe two different ways seeds can travel to new places",
        "Explain how the shape of a seed helps it travel by wind",
        "Use a model to show how seed shape affects travel distance"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A dandelion seed has a fluffy top and floats on the wind. A coconut is heavy and falls to the ground. Which seed will travel farther by wind and why?"),
        ("Constructed Response:", "Explain how the shape of a seed helps it travel to a new place. Give an example of a seed that uses wind to travel and describe what makes its shape special.")
    ],
    "extend_components": [
        ("Animal Carriers", "Animals like squirrels, birds, and dogs that carry seeds on their fur or in their bellies to new places"),
        ("Water Flow", "Rivers, streams, and rain that carry seeds from one place to another — coconuts float across oceans!")
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model showing how seed shape affects how far seeds travel, mimicking real seed dispersal."),
        ("Disciplinary Core Idea", "LS2.A Interdependent Relationships in Ecosystems", "Plants depend on animals for pollination or to move their seeds around. Seeds have features that help them move to new locations."),
        ("Crosscutting Concept", "Structure and Function", "Students connect the shape (structure) of a seed to how it moves (function) — fluffy shapes float, hooks stick, and wings spin.")
    ],
    "background_intro": "Plants are rooted in one spot, but their seeds can travel incredible distances. Understanding seed dispersal helps us learn how forests grow, how plants spread to new areas, and why seed shapes are so amazingly diverse.",
    "background_sections": [
        ("Why Seeds Need to Travel", "If all seeds fell right under the parent plant, they would be too crowded. They would compete for sunlight, water, and nutrients. Seed dispersal spreads seeds to new locations where they have a better chance of growing into healthy plants. Some seeds travel just a few feet, while others cross entire oceans!"),
        ("Wind Dispersal", "Many seeds have special shapes that help them fly. Dandelion seeds have fluffy parachutes that catch the wind. Maple seeds have papery wings that spin like helicopters. These shapes increase the seed's surface area so air pushes on them and keeps them floating longer, carrying them farther from the parent plant."),
        ("Animal and Water Dispersal", "Some seeds have hooks or sticky coatings that grab onto animal fur and get carried to new places. Some seeds are inside tasty fruits — animals eat the fruit and the seeds come out later in a new location. Other seeds, like coconuts, can float in water and travel to distant shores.")
    ],
    "lever_L": "Students identify seed shape and wind interaction as external components and travel distance as an internal component that changes based on how the seed interacts with wind.",
    "lever_E": "Students determine that fluffy or winged seed shapes increase travel distance (positive), while heavy round shapes decrease travel distance.",
    "lever_V": "Students build a model showing how seed shape affects how far a seed travels in the wind.",
    "lever_Ev": "Students run fluffy seed, heavy seed, and winged seed scenarios to compare travel distances.",
    "lever_R": "Students add animal carriers or water flow to explore other ways seeds disperse beyond wind.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dandelion seeds floating", "say": "Have you ever blown on a dandelion and watched the seeds fly away? Where do they go?", "do": "If possible, bring in a real dandelion puff or show a video of seeds floating in the wind.", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn Today?", "visual": "Learning goals and vocabulary", "say": "Today we are going to find out how seeds travel to new places even though plants cannot walk!", "do": "Read objectives together. Introduce seed dispersal, adaptation, and dispersal agent with real seed examples.", "time": "3 min"},
        {"num": "Slide 3", "title": "The Big Question", "visual": "How do seeds travel if plants can't move?", "say": "Plants are stuck in the ground — they cannot move! So how do their seeds get to new places?", "do": "Show students 3 real seeds (dandelion puff, maple wing, acorn). Ask: How do you think each one travels?", "time": "3 min"},
        {"num": "Slide 4", "title": "Let's Build a Model!", "visual": "LEVER steps overview", "say": "Let us build a model to figure out which seeds can travel the farthest and why.", "do": "Preview LEVER steps. Explain that we will test different seed shapes to see how they move.", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Sort the Parts", "visual": "Component cards: Seed Shape, Wind Interaction, Travel Distance", "say": "What are the parts of our seed travel system? Which parts can we control?", "do": "Guide sorting: Seed Shape and Wind Interaction are external (we choose them), Travel Distance is internal (it depends on the others).", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect with Arrows", "visual": "Arrows between seed components", "say": "If a seed is fluffy, will it travel far or not far in the wind? Let us draw our arrows.", "do": "Help students connect Seed Shape and Wind Interaction to Travel Distance with positive arrows for fluffy/winged shapes.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Run the Simulation!", "visual": "Simulation predictions and results", "say": "Time to test! We will drop a fluffy seed, a heavy acorn, and a winged seed and see which goes farthest.", "do": "Students predict first. Run simulations (or drop real model seeds). Measure and compare travel distances.", "time": "8 min"},
        {"num": "Slide 8", "title": "What Did We Discover?", "visual": "Key discoveries about seed travel", "say": "Which seed won the travel contest? Why did that shape help it go the farthest?", "do": "Discuss how seed shape is an adaptation. Connect to why plants need seeds to travel — room to grow!", "time": "7 min"}
    ],
    "sort_reasoning": "Seed Shape and Wind Interaction are external because they exist before the seed starts traveling — the plant makes the seed shape, and the wind is a natural force we cannot control. Travel Distance is internal because it is the result of how the seed shape interacts with the wind.",
    "relationships": [
        ("Seed Shape (fluffy/winged) to Travel Distance", "POSITIVE (+)", "Seeds with fluffy or winged shapes catch more air and float longer, so they travel farther from the parent plant. The more surface area the seed has, the more the wind can push it along."),
        ("Wind Interaction to Travel Distance", "POSITIVE (+)", "Stronger wind or better wind-catching seed shapes mean the seed travels farther. More wind energy helps carry the seed a longer distance before it lands.")
    ],
    "sim_answers": [
        ("Fluffy Dandelion Seed", "When Seed Shape is fluffy and Wind is breezy, Travel Distance is far. The fluffy parachute catches the wind and keeps the seed floating for a long time. The dandelion seed drifts far away from the parent plant."),
        ("Heavy Acorn", "When Seed Shape is heavy round and Wind is breezy, Travel Distance is very short. The acorn is too heavy for the wind to carry. It falls straight down near the parent tree. Acorns need animals like squirrels to move them to new places instead.")
    ],
    "stem_intro": "Present the challenge: A nature center wants to teach visitors about seed dispersal. Your team will design and build a model seed from simple materials. The goal is to make a seed that travels the farthest when dropped from shoulder height.",
    "stem_concepts": [
        ("Shape Matters", "The shape of a seed determines how it interacts with the air. Fluffy and winged shapes catch air and float, while heavy round shapes fall quickly. Your design should use shape to travel far."),
        ("Lightweight Helps", "Lighter seeds travel farther in the wind because air can push them more easily. But a seed also needs to be heavy enough to carry the baby plant inside."),
        ("Real Seeds Inspire Design", "Look at real seeds for ideas — dandelion parachutes, maple helicopters, and cottonwood fluff are all nature's designs for traveling by wind.")
    ],
    "stem_eval": [
        ("Expert (4)", "Seed model travels far, student explains how shape helps it catch air, and connects to real seed adaptations"),
        ("Proficient (3)", "Seed model travels and student can explain how the shape affects distance"),
        ("Developing (2)", "Seed model is built but student has difficulty explaining why the shape helps or hinders travel"),
        ("Beginning (1)", "Seed model is incomplete or does not demonstrate seed dispersal principles")
    ],
    "support": [
        "Provide real seeds (dandelion puffs, maple wings, acorns) for students to touch and observe before modeling",
        "Use a fan on low setting to create consistent wind for fair testing of model seeds",
        "Sentence frame: 'My seed has a ___ shape so it can travel ___ because ___'"
    ],
    "extensions": [
        "Investigate how seeds that travel by animal (burrs, berries) are different from seeds that travel by wind",
        "Plant a few different seeds in cups and observe which ones grow — seeds need the right conditions even after they travel!",
        "Research the seed that travels the farthest in nature and create a poster about it"
    ],
    "cross_curr": [
        ("Math", "Measure how far each model seed travels in centimeters and create a bar graph comparing the three types"),
        ("ELA", "Write a short adventure story from the point of view of a seed traveling to a new home"),
        ("Art", "Observe real seeds closely and draw detailed scientific illustrations showing their special features")
    ],
    "misconceptions": [
        ("Seeds are planted by people or they do not grow", "Most seeds in nature are NOT planted by people! Seeds have their own ways of getting to new places — wind, water, animals, and even exploding pods. Forests and meadows grew from seeds that dispersed naturally.", "Take students outside and look for seeds on the ground, in cracks, on clothing — seeds are everywhere and no one planted them!"),
        ("All seeds travel the same way", "Different seeds have very different shapes because they travel in different ways. Dandelion seeds fly on the wind, burr seeds hitch rides on animals, coconut seeds float in water, and some seeds even pop out of exploding pods!", "Show 3-4 different real seeds. Ask: How is each one shaped differently? How might each one travel?"),
        ("Seeds are not alive", "Seeds ARE alive — they have a tiny baby plant inside waiting to grow! Seeds look like they are not doing anything, but inside they are just waiting for the right conditions: water, warmth, and soil. Then they wake up and start growing.", "Place a bean seed on a wet paper towel in a bag. In a few days, students will see it sprout — proof it is alive!")
    ]
}

L04 = {
    "id": "G02-L04",
    "title": "Can Plants Grow Without Soil?",
    "subtitle": "What Plants Really Need to Survive",
    "ngss": "2-LS2-1",
    "ngss_desc": "Plan and conduct an investigation to determine if plants need sunlight and water to grow.",
    "big_question": "Do plants really need soil to grow, or can they grow with just water and sunlight?",
    "objectives": [
        "Identify what plants need to grow — sunlight, water, air, and nutrients",
        "Compare how plants grow with soil versus without soil",
        "Explain why plants can grow in water alone if they have sunlight and nutrients"
    ],
    "vocabulary": [
        ("Nutrients", "Tiny bits of food in soil or water that plants need to grow strong and healthy"),
        ("Sunlight", "Light energy from the sun that plants use to make their own food"),
        ("Roots", "The parts of a plant that grow underground and soak up water and nutrients"),
        ("Germinate", "When a seed starts to sprout and grow into a tiny new plant")
    ],
    "components": [
        ("Sunlight Amount", "How much light the plant gets each day — from no light to full bright sunshine", True),
        ("Water Availability", "How much water the plant can reach with its roots — from dry to soaking wet", True),
        ("Plant Growth", "How tall the plant grows and how healthy its leaves look — depends on sunlight and water", False)
    ],
    "think_about_it": "When sunlight amount increases, what happens to plant growth? What about when water availability increases?",
    "scenarios": [
        ("Full Sun and Water", "Set Sunlight Amount to high and Water Availability to high, then observe Plant Growth"),
        ("No Sunlight", "Set Sunlight Amount to zero and Water Availability to high, then observe Plant Growth")
    ],
    "sim_scenarios": [
        ("Full Sun and Water", "Sunlight high, Water high", "What do you predict will happen to Plant Growth when a plant gets lots of sun and water?"),
        ("No Sunlight", "Sunlight zero, Water high", "What do you predict will happen to Plant Growth when a plant gets water but no sunlight?"),
        ("No Water", "Sunlight high, Water zero", "What do you predict will happen to Plant Growth when a plant gets sun but no water?")
    ],
    "discoveries": [
        "Plants need BOTH sunlight and water to grow — missing either one causes the plant to struggle",
        "Plants can grow without soil if they get water and nutrients another way — this is called hydroponics",
        "Sunlight gives plants energy to make their own food inside their leaves",
        "Roots soak up water and nutrients, whether they are in soil or in water"
    ],
    "answer": "Plants do not actually need soil to grow — they need what is IN the soil! Plants really need water, sunlight, air, and nutrients. Soil is helpful because it holds water and nutrients near the roots, but if a plant can get water and nutrients from another source (like growing in a cup of water), it can grow just fine without any soil at all!",
    "stem_title": "Build a Soil-Free Garden",
    "stem_mission": "Design a small garden where plants grow without soil — using only water, sunlight, and nutrients.",
    "stem_scenario": "A space station needs to grow fresh food for astronauts, but there is no soil in space! Your team has been asked to design a small soil-free garden that grows plants using only water, light, and nutrients. Use what you learned to make your garden work.",
    "stem_questions": [
        "How will your plants get water if there is no soil to hold it?",
        "Where will the light come from for your soil-free garden?",
        "How can you tell if your plants are growing well without soil?"
    ],
    "stem_design_qs": [
        "What will you use to hold the plant up if there is no soil — sponge, cotton, or something else?",
        "How will the roots stay in the water?",
        "Where will you put your garden so it gets enough light?",
        "How will you add nutrients to the water?"
    ],
    "career": "Agricultural Scientists study how to grow food better and help feed people around the world. Some work on hydroponic farms that grow food without soil. They earn $50,000–$90,000/year.",
    "images": {
        "cover": ("cover-plants.png", "A vibrant green plant growing in a clear glass jar of water with visible white roots, bright natural light, clean background, vivid macro photography"),
        "landscape": ("landscape-plants.png", "Diverse 2nd grade students (7-8 years old, wide variety of ethnicities) at a table with small plants growing in cups of water and cups of soil side by side, comparing them, bright modern classroom, natural window light, editorial photo quality"),
        "modeling": ("modeling-plants.png", "A colorful kid-friendly scientific diagram showing a plant with roots in soil on one side and roots in water on the other side, labeled arrows for sunlight, water, and nutrients — cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-plants.png", "A teacher with diverse 2nd graders (7-8 years old, wide variety of ethnicities) gathered around a table with plants growing in different conditions, pointing and discussing observations, bright classroom"),
        "stem": ("stem-plants.png", "Diverse 2nd graders (7-8 years old, wide mix of ethnicities) building small hydroponic gardens from plastic cups, sponges, and bean seeds, water and sunlight visible, excited collaborative group work")
    },
    "pre_assessment": [
        "What do you think plants need to grow big and healthy?",
        "Do you think a plant could grow if you just put it in water with no soil? Why or why not?",
        "Draw a plant and label all the things you think it needs to survive."
    ],
    "reflections": [
        "Were you surprised that plants can grow without soil? What did the soil actually do for the plant?",
        "If you were an astronaut, how would you grow food in space where there is no soil?"
    ],
    "reflection_exemplars": [
        ("Were you surprised that plants can grow without soil? What did the soil actually do for the plant?", "I was surprised because I always thought plants needed soil. But soil just holds the water and nutrients near the roots. The plant really needs water, sunlight, and nutrients — not the soil itself. If we give the roots water and nutrients a different way, the plant can grow just fine without any dirt!")
    ],
    "cast_items": [
        "Identify the things plants need to grow — sunlight, water, and nutrients",
        "Explain why plants can grow without soil if other needs are met",
        "Compare plant growth with and without sunlight using evidence"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student puts one plant in sunlight with water and another plant in a dark closet with water. After two weeks, the plant in the dark is pale and droopy. What does this tell us?"),
        ("Constructed Response:", "Explain what plants really need to grow. Can a plant grow without soil? Use evidence from your investigation to support your answer.")
    ],
    "extend_components": [
        ("Nutrients in Water", "Adding nutrients to the water to replace what soil usually provides — like plant vitamins"),
        ("Air Flow", "Moving air around the plant helps it get carbon dioxide, which it needs to make food in its leaves")
    ],
    "dimensions": [
        ("Science Practice", "Planning and Carrying Out Investigations", "Students plan and conduct an investigation to determine if plants need sunlight and water to grow, testing different conditions."),
        ("Disciplinary Core Idea", "LS2.A Interdependent Relationships in Ecosystems", "Plants depend on water and light to grow. Plants depend on animals for pollination or to move their seeds around."),
        ("Crosscutting Concept", "Cause and Effect", "Students observe that removing sunlight or water causes poor plant growth, establishing a cause-and-effect relationship.")
    ],
    "background_intro": "Plants are amazing living things that make their own food from sunlight, water, and air. Understanding what plants truly need to grow helps us grow food in new and creative ways — even in places without soil!",
    "background_sections": [
        ("What Do Plants Need?", "Plants need four things to survive and grow: sunlight, water, air (specifically carbon dioxide), and nutrients. Sunlight gives plants the energy to make food in their leaves through a process called photosynthesis. Water travels up through the roots and into every part of the plant. Nutrients are like vitamins that help the plant grow strong."),
        ("The Role of Soil", "Soil is helpful for plants, but it is not actually required. Soil holds water near the roots so the plant can drink. It also contains nutrients that the plant needs. But if we give the plant water and nutrients a different way, the plant does not need soil at all. This is the idea behind hydroponics — growing plants in water."),
        ("Plants in Space", "NASA scientists grow plants on the International Space Station without any soil! They use special systems that deliver water, nutrients, and light directly to the roots. Astronauts have grown lettuce, radishes, and peppers in space. This research helps us figure out how to grow food for long missions to the Moon and Mars.")
    ],
    "lever_L": "Students identify sunlight amount and water availability as external components and plant growth as an internal component that depends on both sunlight and water.",
    "lever_E": "Students determine that both sunlight and water have positive effects on plant growth — more of each helps the plant grow taller and healthier.",
    "lever_V": "Students build a model showing how sunlight and water together determine how well a plant grows.",
    "lever_Ev": "Students run full sun/water, no sunlight, and no water scenarios to see the effects of removing each need.",
    "lever_R": "Students add nutrients in water or air flow to explore other factors that affect plant growth.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with a plant growing in water", "say": "Do you think a plant can grow without any dirt? Just water and sunshine? Let us find out!", "do": "Show a plant growing in a clear jar of water. Let students observe the roots.", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn Today?", "visual": "Learning goals and vocabulary", "say": "Today we are going to investigate what plants REALLY need to grow.", "do": "Read objectives aloud. Introduce nutrients, sunlight, roots, and germinate with real examples.", "time": "3 min"},
        {"num": "Slide 3", "title": "The Big Question", "visual": "Do plants really need soil?", "say": "Everybody thinks plants need soil. But what if they do not? What do plants REALLY need?", "do": "Quick poll: Raise your hand if you think plants MUST have soil. We will find out who is right!", "time": "3 min"},
        {"num": "Slide 4", "title": "Let's Build a Model!", "visual": "LEVER steps overview", "say": "We are going to build a model to test what happens when plants get different things.", "do": "Preview LEVER steps. Show examples of plants in soil and plants in water side by side.", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Sort the Parts", "visual": "Component cards: Sunlight Amount, Water Availability, Plant Growth", "say": "What are the parts of our plant system? Sunlight and water are inputs we can control. Plant growth is what we observe.", "do": "Guide sorting: Sunlight and Water are external, Plant Growth is internal.", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect with Arrows", "visual": "Arrows between components", "say": "When we give a plant MORE sunlight, does it grow better or worse? What about more water?", "do": "Draw positive arrows from Sunlight and Water to Plant Growth. Discuss why both are needed.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Run the Simulation!", "visual": "Simulation predictions and results", "say": "Let us test three conditions: lots of sun and water, no sun, and no water. Predict what happens!", "do": "Students predict, then run simulations. Compare results. Discuss which conditions matter most.", "time": "8 min"},
        {"num": "Slide 8", "title": "What Did We Discover?", "visual": "Key discoveries and answer", "say": "So do plants need soil? The answer might surprise you — they need what is IN the soil, not the soil itself!", "do": "Show a hydroponic plant as proof. Discuss how astronauts grow food in space without soil.", "time": "7 min"}
    ],
    "sort_reasoning": "Sunlight Amount and Water Availability are external because they come from outside the plant — the sun provides light and we provide water. Plant Growth is internal because it is the plant's response to the sunlight and water it receives.",
    "relationships": [
        ("Sunlight Amount to Plant Growth", "POSITIVE (+)", "More sunlight gives the plant more energy to make food in its leaves. Plants in bright sunlight grow taller and greener. Plants with no sunlight become pale and weak because they cannot make food."),
        ("Water Availability to Plant Growth", "POSITIVE (+)", "More water available to the roots means the plant can stay hydrated and transport nutrients. Plants with plenty of water grow well. Plants without water wilt and eventually stop growing.")
    ],
    "sim_answers": [
        ("Full Sun and Water", "When Sunlight is high and Water is high, Plant Growth is strong. The plant grows tall with bright green leaves because it has everything it needs to make food and stay healthy. This is the best condition for plant growth."),
        ("No Sunlight", "When Sunlight is zero and Water is high, Plant Growth is very poor. The plant becomes pale yellow and weak because it cannot make food without light. Even though it has water, sunlight is essential for the plant to create its own energy.")
    ],
    "stem_intro": "Present the challenge: A space station needs to grow food for astronauts, but there is no soil in space! Your team will design a small soil-free garden that grows plants using only water, light, and nutrients.",
    "stem_concepts": [
        ("Hydroponics", "Growing plants in water instead of soil. The water must contain nutrients so the plant gets the vitamins it needs. The roots sit directly in the water."),
        ("Light Is Energy", "Plants use sunlight to make their own food. Without light, a plant cannot feed itself and will stop growing. Your garden needs a light source."),
        ("Roots Absorb Water", "Roots are the drinking straws of the plant. In a hydroponic garden, the roots hang directly in the water and soak up what the plant needs.")
    ],
    "stem_eval": [
        ("Expert (4)", "Soil-free garden supports plant growth, and student explains how it meets the plant's needs for water, light, and nutrients"),
        ("Proficient (3)", "Soil-free garden holds a plant in water with light, and student can explain why it works"),
        ("Developing (2)", "Garden is built but student struggles to explain how the plant gets what it needs without soil"),
        ("Beginning (1)", "Garden is incomplete or the plant is not set up to receive water and light")
    ],
    "support": [
        "Provide bean seeds pre-soaked for 24 hours so they germinate quickly during the lesson",
        "Use clear cups so students can watch roots grow into the water",
        "Sentence frame: 'My plant can grow without soil because it gets ___ from ___ and ___ from ___'"
    ],
    "extensions": [
        "Compare plant growth in soil vs. water over two weeks — measure height every other day and graph it",
        "Research hydroponic farms and find out what crops can be grown without soil",
        "Try growing a plant in different liquids — water, juice, milk — and observe what happens"
    ],
    "cross_curr": [
        ("Math", "Measure plant height in centimeters every two days and create a line graph showing growth over time"),
        ("ELA", "Write a persuasion paragraph: Why should astronauts grow their own food in space?"),
        ("Art", "Draw a before-and-after picture of a seed becoming a plant, labeling sunlight, water, and roots")
    ],
    "misconceptions": [
        ("Plants eat soil", "Plants do NOT eat soil! Plants make their own food using sunlight, water, and air. Roots absorb water and tiny nutrients from the soil, but the soil itself is not food. That is why plants can grow in just water if nutrients are added.", "Put soil in one cup and water in another. Ask: Which one would YOU rather drink? Plants drink the water — they do not eat the dirt!"),
        ("Plants only need water to survive", "Water is very important, but it is not enough by itself. Plants also need sunlight to make food and air to breathe. A plant in a dark room with plenty of water will still get sick and pale because it cannot make food without light.", "Put one watered plant in a sunny window and one watered plant in a dark closet. Compare after 5 days — the dark plant is pale and droopy!"),
        ("Plants get their food from soil or fertilizer", "Fertilizer and soil nutrients are like vitamins — they help the plant grow strong, but they are not the plant's main food. Plants make their own food from sunlight and air through photosynthesis. Nutrients from soil are just helpers.", "Ask: Where do the biggest, tallest trees get their food? Not from someone feeding them! They make it themselves from sunlight and air.")
    ]
}

L05 = {
    "id": "G02-L05",
    "title": "Why Don't We See Dinosaurs?",
    "subtitle": "What Fossils Tell Us About Long Ago",
    "ngss": "2-LS4-1",
    "ngss_desc": "Make observations of plants and animals to compare the diversity of life in different habitats.",
    "big_question": "If dinosaurs lived on Earth millions of years ago, why are there no dinosaurs alive today — and how do we know they existed?",
    "objectives": [
        "Explain that fossils are evidence of plants and animals that lived long ago",
        "Describe how scientists use fossils to learn about animals that no longer exist",
        "Compare animals that are alive today with animals that lived long ago using fossil evidence"
    ],
    "vocabulary": [
        ("Fossil", "The remains or trace of a plant or animal from long, long ago preserved in rock"),
        ("Extinct", "When every single one of a type of plant or animal has died and none are left alive anywhere"),
        ("Habitat", "The place where a plant or animal lives that provides everything it needs to survive"),
        ("Evidence", "Clues and observations that help us figure out what happened — like detective work!")
    ],
    "components": [
        ("Habitat Change", "How much the environment changes — temperature, food, water, or other big shifts", True),
        ("Animal Survival", "How well the animals can find food, water, and shelter in the changed habitat", False),
        ("Population Size", "How many of that type of animal are still alive — gets smaller when survival is hard", False)
    ],
    "think_about_it": "When a habitat changes a lot (like getting much colder), what happens to animal survival? What happens to population size?",
    "scenarios": [
        ("Small Change", "Set Habitat Change to small and observe how Animal Survival and Population Size respond"),
        ("Huge Change", "Set Habitat Change to very large and observe what happens to the animal population")
    ],
    "sim_scenarios": [
        ("Small Habitat Change", "Habitat Change set to small", "What do you predict will happen to Animal Survival when the habitat only changes a little bit?"),
        ("Huge Habitat Change", "Habitat Change set to very large", "What do you predict will happen to Population Size when the habitat changes a LOT — like an ice age?"),
        ("Medium Change", "Habitat Change set to medium", "Will the animals all survive, all die, or will some survive? Why?")
    ],
    "discoveries": [
        "When habitats change a little, most animals can survive and adapt",
        "When habitats change a LOT (like a huge asteroid hitting Earth), many animals cannot survive and go extinct",
        "Fossils are our evidence that extinct animals once lived here — they are like nature's history books",
        "Some animals alive today look similar to fossils from long ago — they are related to ancient animals"
    ],
    "answer": "Dinosaurs are not alive today because their habitat changed in a HUGE way about 66 million years ago. A giant asteroid hit Earth and caused the climate to change so much that dinosaurs could not survive. They went extinct. But we know they existed because they left behind fossils — bones, teeth, and footprints preserved in rock. Fossils are the evidence that tells us the story of life on Earth!",
    "stem_title": "Create a Fossil Museum Exhibit",
    "stem_mission": "Design a mini museum exhibit that uses fossil evidence to teach visitors about an extinct animal.",
    "stem_scenario": "A children's museum wants to create a new exhibit about extinct animals. Your team has been hired to choose one extinct animal, make a model fossil, and create a display that teaches visitors what the animal looked like, where it lived, and why it is no longer alive.",
    "stem_questions": [
        "Which extinct animal will you choose for your exhibit?",
        "What kind of fossil evidence would scientists find from your animal?",
        "How will your exhibit show visitors why this animal went extinct?"
    ],
    "stem_design_qs": [
        "What materials will you use to make your model fossil — clay, plaster, or something else?",
        "What information will you include on the exhibit sign?",
        "How will you show what the animal looked like when it was alive?",
        "How will your exhibit explain what happened to the animal's habitat?"
    ],
    "career": "Paleontologists are scientists who study fossils to learn about plants and animals that lived millions of years ago. They dig up fossils, study them, and teach us about ancient life. They earn $50,000–$95,000/year.",
    "images": {
        "cover": ("cover-dinosaur.png", "A dramatic fossil of a dinosaur skeleton embedded in rock layers, museum-quality lighting, warm tones, cinematic archaeological photography"),
        "landscape": ("landscape-dinosaur.png", "Diverse 2nd grade students (7-8 years old, wide variety of ethnicities) at a natural history museum looking up at a large dinosaur skeleton with amazed expressions, museum lighting, editorial photo quality"),
        "modeling": ("modeling-dinosaur.png", "A colorful kid-friendly scientific diagram showing how a dinosaur becomes a fossil over millions of years — the dinosaur, buried in mud, layers of rock forming, fossil revealed — cartoon-style, white background, bold outlines, timeline arrow"),
        "discussion": ("discussion-dinosaur.png", "A teacher with diverse 2nd graders (7-8 years old, wide variety of ethnicities) sitting in a circle examining toy fossils and comparing them to pictures of living animals, bright classroom"),
        "stem": ("stem-dinosaur.png", "Diverse 2nd graders (7-8 years old, wide mix of ethnicities) pressing toy dinosaur bones into clay to make model fossils and creating museum display signs, colorful classroom work tables")
    },
    "pre_assessment": [
        "What do you know about dinosaurs? Did they really exist?",
        "What is a fossil? Have you ever seen one in a museum or a picture?",
        "Draw what you think happened to the dinosaurs — why are they not here anymore?"
    ],
    "reflections": [
        "How do fossils help us learn about animals we have never seen alive?",
        "If habitats are still changing today, could any animals alive now become extinct in the future?"
    ],
    "reflection_exemplars": [
        ("How do fossils help us learn about animals we have never seen alive?", "Fossils are like clues left behind in the rocks. When scientists find fossil bones, they can figure out how big the animal was, what shape it was, and even what it ate by looking at the teeth. Footprint fossils tell us how it walked. Fossils are evidence that helps us put together the story of animals that lived millions of years ago, even though nobody was there to see them.")
    ],
    "cast_items": [
        "Explain what a fossil is and how it helps us learn about the past",
        "Describe what happens to animals when their habitat changes a lot",
        "Compare an extinct animal to a living animal using evidence"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Scientists found a fossil of a fish in the middle of a desert. What does this tell us about this place long ago?"),
        ("Constructed Response:", "Explain how fossils help scientists learn about animals that lived long ago. Give an example of something a fossil can tell us about an extinct animal.")
    ],
    "extend_components": [
        ("Food Supply", "How much food is available in the habitat — when food runs out, animals struggle to survive"),
        ("Climate Speed", "How fast the habitat changes — slow changes let animals adapt, but fast changes are harder to survive")
    ],
    "dimensions": [
        ("Science Practice", "Analyzing and Interpreting Data", "Students analyze fossil evidence to draw conclusions about what extinct animals looked like and why they are no longer alive."),
        ("Disciplinary Core Idea", "LS4.A Evidence of Common Ancestry and Diversity", "There are many different kinds of living things in any area, and they exist in different places. Fossils provide evidence about the types of organisms that lived long ago."),
        ("Crosscutting Concept", "Stability and Change", "Students explore how changes in habitat can cause animal populations to shrink or go extinct, and how stable habitats support diverse life.")
    ],
    "background_intro": "Long before humans existed, amazing creatures walked, swam, and flew across Earth. We know about them because they left behind fossils — preserved clues in the rocks that tell the story of ancient life.",
    "background_sections": [
        ("What Are Fossils?", "Fossils are the preserved remains or traces of living things from long ago. When an animal dies and gets buried in mud or sand, sometimes its bones, teeth, or shells get slowly replaced by minerals and turn to stone over millions of years. Trace fossils like footprints, nests, and even poop (called coprolites!) can also be preserved. Each fossil is a clue about ancient life."),
        ("Why Did Dinosaurs Go Extinct?", "About 66 million years ago, a giant asteroid (a rock from space) hit Earth near what is now Mexico. The impact caused massive fires, dust clouds that blocked the sun, and dramatic climate change. Without sunlight, plants died. Without plants, plant-eating dinosaurs starved. Without plant-eaters, meat-eating dinosaurs starved too. The habitat changed so fast and so much that most dinosaurs could not survive."),
        ("Living Relatives", "Not all dinosaurs died out! Scientists have discovered that birds are actually living dinosaurs — they evolved from small feathered dinosaurs millions of years ago. When you see a chicken, a robin, or an eagle, you are looking at a modern dinosaur! Fossils helped scientists make this amazing discovery by showing the link between feathered dinosaur fossils and modern birds.")
    ],
    "lever_L": "Students identify habitat change as an external component and animal survival and population size as internal components that respond to environmental shifts.",
    "lever_E": "Students determine that large habitat changes cause animal survival to decrease (negative), which causes population size to decrease. Small changes allow survival to remain high.",
    "lever_V": "Students build a model showing how the size of habitat change affects whether animal populations survive or go extinct.",
    "lever_Ev": "Students run small change, medium change, and huge change scenarios to observe different outcomes for animal populations.",
    "lever_R": "Students add food supply or climate speed to explore why some habitat changes are more dangerous than others.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with fossil imagery", "say": "Raise your hand if you have ever wanted to see a real dinosaur. Well, today we are going to figure out what happened to them!", "do": "Show pictures of dinosaur fossils. Pass around a small fossil or replica if available.", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn Today?", "visual": "Learning goals and vocabulary", "say": "Today we are going to be fossil detectives! We will figure out what happened to the dinosaurs.", "do": "Read objectives together. Introduce fossil, extinct, habitat, and evidence with pictures.", "time": "3 min"},
        {"num": "Slide 3", "title": "The Big Question", "visual": "Why don't we see dinosaurs today?", "say": "Dinosaurs lived on Earth for over 160 million years. That is way longer than humans! So what happened?", "do": "Think-pair-share: What do you think happened to the dinosaurs? Collect theories on the board.", "time": "3 min"},
        {"num": "Slide 4", "title": "Let's Build a Model!", "visual": "LEVER steps overview", "say": "We are going to build a model to understand why some animals survive habitat changes and some do not.", "do": "Preview LEVER steps. Explain that this model will help us understand extinction.", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Sort the Parts", "visual": "Component cards: Habitat Change, Animal Survival, Population Size", "say": "What are the parts of our extinction model? Habitat Change is what happens to the environment. The other parts show what happens to the animals.", "do": "Guide students to sort Habitat Change as external and Animal Survival and Population Size as internal.", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect with Arrows", "visual": "Arrows between components", "say": "When the habitat changes A LOT, do animals survive better or worse? What happens to the number of animals?", "do": "Draw negative arrow from Habitat Change to Animal Survival. Draw positive arrow from Animal Survival to Population Size.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Run the Simulation!", "visual": "Simulation predictions and results", "say": "Let us test! First a tiny change, then a HUGE change — like an asteroid hitting Earth!", "do": "Students predict, then run scenarios. Compare small vs. huge habitat change effects on the population.", "time": "8 min"},
        {"num": "Slide 8", "title": "What Did We Discover?", "visual": "Key discoveries and fossil evidence", "say": "Dinosaurs went extinct because the habitat changed too fast and too much. But they left us clues — fossils!", "do": "Show fossil pictures. Compare a T-rex fossil to a chicken skeleton. Fun fact: birds ARE dinosaurs!", "time": "7 min"}
    ],
    "sort_reasoning": "Habitat Change is external because it comes from outside forces like weather, asteroid impacts, or volcanic eruptions — the animals do not control it. Animal Survival and Population Size are internal because they change as a result of how much the habitat changes.",
    "relationships": [
        ("Habitat Change to Animal Survival", "NEGATIVE (-)", "When the habitat changes a lot, it becomes harder for animals to find food, water, and shelter. The bigger the change, the harder it is to survive. Small changes are okay, but huge changes can be deadly."),
        ("Animal Survival to Population Size", "POSITIVE (+)", "When animals survive well, the population stays large and healthy. When survival drops, the population gets smaller and smaller. If survival drops to zero, the animal goes extinct — gone forever.")
    ],
    "sim_answers": [
        ("Small Habitat Change", "When Habitat Change is small, Animal Survival stays high and Population Size remains large. The animals can still find food, water, and shelter because not much changed. They adapt to the small differences in their habitat."),
        ("Huge Habitat Change", "When Habitat Change is very large, Animal Survival drops dramatically and Population Size shrinks toward zero. The animals cannot find food or shelter in the drastically changed habitat. This is what happened to the dinosaurs — the asteroid caused such a huge change that they could not survive.")
    ],
    "stem_intro": "Present the challenge: A children's museum wants a new exhibit about extinct animals. Your team will choose an extinct animal, make a model fossil, and create a display that teaches visitors about the animal and why it is no longer alive.",
    "stem_concepts": [
        ("Fossils as Evidence", "Fossils are the main way we learn about extinct animals. Bones tell us about body shape and size. Teeth tell us what the animal ate. Footprints tell us how it moved. Your exhibit should show what fossils teach us."),
        ("Habitat Change Causes Extinction", "Animals go extinct when their habitat changes too much for them to survive. Your exhibit should explain what changed in your animal's habitat."),
        ("Comparing Past and Present", "Many extinct animals have living relatives. Comparing fossils to modern animals helps us see connections across millions of years.")
    ],
    "stem_eval": [
        ("Expert (4)", "Museum exhibit includes a model fossil, explains what the animal was like, and uses evidence to show why it went extinct"),
        ("Proficient (3)", "Exhibit includes a fossil model and basic information about the extinct animal"),
        ("Developing (2)", "Exhibit is built but student struggles to explain the connection between habitat change and extinction"),
        ("Beginning (1)", "Exhibit is incomplete or student cannot explain what a fossil tells us")
    ],
    "support": [
        "Provide pictures of real fossils alongside pictures of living animals for comparison",
        "Use clay and toy animal figures to demonstrate how fossils form step by step",
        "Sentence frame: 'My fossil tells us ___ about this animal because ___'"
    ],
    "extensions": [
        "Research one extinct animal besides dinosaurs (like mammoths, dodo birds, or saber-toothed cats) and report findings to the class",
        "Compare a fossil shark tooth to a modern shark tooth — how are they similar and different?",
        "Create a timeline showing when dinosaurs lived, when they went extinct, and when humans appeared"
    ],
    "cross_curr": [
        ("Math", "Use a number line to show how long ago dinosaurs lived (66 million years) compared to how long humans have been around (about 300,000 years)"),
        ("ELA", "Write a letter from a dinosaur fossil to a museum visitor, explaining what life was like long ago"),
        ("Art", "Create a clay fossil imprint by pressing a leaf, shell, or toy dinosaur into soft clay and letting it harden")
    ],
    "misconceptions": [
        ("Dinosaurs and humans lived at the same time", "Dinosaurs went extinct about 66 million years before the first humans appeared! They never met each other. Movies and cartoons sometimes show them together, but in real life there is a huge time gap between dinosaurs and humans.", "Use a long paper strip timeline. Put dinosaurs at one end and humans at the other. Show students how far apart they are in time — like opposite ends of the hallway!"),
        ("Extinct means the animal was not strong enough", "Extinction is not about being strong or weak. Even the biggest, most powerful dinosaurs went extinct because their habitat changed too fast. Extinction happens when the environment changes so much that the animals cannot find what they need to survive — no matter how strong they are.", "Ask: Was a T-rex strong? (Yes!) Did it go extinct? (Yes!) So being strong does not protect you if your habitat disappears."),
        ("Fossils are just regular rocks", "Fossils look like rocks, but they are special — they contain the remains or traces of living things from long ago. The original bone or shell was slowly replaced by minerals over millions of years, turning it to stone. Fossils are rocks with a story inside them!", "Compare a regular rock to a fossil with visible bone or leaf detail. Ask: What makes this one special? What can you see that tells you something lived here?")
    ]
}

L06 = {
    "id": "G02-L06",
    "title": "How Do Maps Help Us Find Things?",
    "subtitle": "Mapping the Land, Water, and Features of Earth",
    "ngss": "2-ESS2-2",
    "ngss_desc": "Develop a model to represent the shapes and kinds of land and bodies of water in an area.",
    "big_question": "How do maps help us understand what the land and water look like in a place we have never visited?",
    "objectives": [
        "Identify different land and water features on a map — mountains, rivers, lakes, and plains",
        "Build a simple model that represents the shapes of land and water in an area",
        "Explain how maps help people understand places they cannot see from the ground"
    ],
    "vocabulary": [
        ("Map", "A flat picture that shows what land and water look like from above — like a bird's eye view"),
        ("Landform", "A natural shape on Earth's surface, like a mountain, hill, valley, or plain"),
        ("Body of Water", "A large area of water on Earth's surface, like an ocean, river, lake, or stream")
    ],
    "components": [
        ("Land Height", "How tall or flat the land is — mountains are tall, plains are flat, valleys are low", True),
        ("Water Location", "Where water collects or flows — in rivers, lakes, and oceans at the lowest spots", False),
        ("Map Features", "What the map shows — symbols, colors, and shapes that represent the real land and water", False)
    ],
    "think_about_it": "When the land gets higher (like a mountain), what happens to where water flows? Does water go up mountains or down into valleys?",
    "scenarios": [
        ("Mountain Area", "Set Land Height to very tall (mountain) and observe where Water Location and Map Features appear"),
        ("Flat Plains", "Set Land Height to flat and observe how the water and map features are different")
    ],
    "sim_scenarios": [
        ("Mountain Area", "Land Height set to tall mountain", "What do you predict the map will show for a mountain area? Where will the water be?"),
        ("Flat Plains", "Land Height set to flat", "What do you predict the map will look like for flat land? Will there be rivers or lakes?"),
        ("Valley With River", "Land Height set to low valley", "Where do you predict water will collect in a valley? How will the map show this?")
    ],
    "discoveries": [
        "Maps use colors and symbols to represent real land and water features from above",
        "Water flows downhill, so it collects in the lowest parts of the land — valleys, lakes, and rivers",
        "Mountains appear on maps with special markings because they are the highest points",
        "Maps help us understand places we cannot see or visit by showing the shapes of land and water"
    ],
    "answer": "Maps are like pictures of the Earth taken from way up high! They use colors, lines, and symbols to show us what the land and water look like. Blue areas show water like rivers and lakes. Green and brown areas show land — flat plains, rolling hills, or tall mountains. Maps help us understand places we have never been by showing the shapes and features of the land from a bird's eye view!",
    "stem_title": "Build a 3D Map of Our Area",
    "stem_mission": "Create a 3D model map that shows the land and water features of a real or imaginary area.",
    "stem_scenario": "A park ranger needs a 3D map to help visitors understand the land around a new nature park. Your team will build a model that shows mountains, valleys, rivers, and lakes so visitors can see what the park looks like before they explore it.",
    "stem_questions": [
        "What land features will you include in your 3D map — mountains, hills, valleys, or plains?",
        "Where will you put the water in your map and why?",
        "How will visitors be able to tell which parts are high and which are low?"
    ],
    "stem_design_qs": [
        "What materials will you use to build the land — clay, playdough, or crumpled paper?",
        "How will you show water — blue paint, foil, or plastic wrap?",
        "How will you label the different features so visitors know what they are looking at?",
        "How does your 3D map compare to a flat map of the same area?"
    ],
    "career": "Cartographers make maps that help people explore, build roads, and understand the Earth. They use computers, satellites, and math to create detailed maps. They earn $45,000–$80,000/year.",
    "images": {
        "cover": ("cover-map.png", "A beautiful illustrated topographic map showing mountains, rivers, and valleys with vibrant blue water and green-brown terrain, bright colors, bird's eye view, clean design"),
        "landscape": ("landscape-map.png", "Diverse 2nd grade students (7-8 years old, wide variety of ethnicities) leaning over a large colorful floor map together, pointing at features, modern classroom with natural lighting, editorial photo quality"),
        "modeling": ("modeling-map.png", "A colorful kid-friendly scientific diagram showing a side view of mountains, a valley, and a river flowing downhill into a lake, with a matching bird's-eye-view map below it — cartoon-style, white background, bold outlines, labeled features"),
        "discussion": ("discussion-map.png", "A teacher with diverse 2nd graders (7-8 years old, wide variety of ethnicities) gathered around a globe and a wall map, teacher pointing at a mountain range, students looking engaged, bright classroom"),
        "stem": ("stem-map.png", "Diverse 2nd graders (7-8 years old, wide mix of ethnicities) building 3D terrain maps from clay and playdough on trays, painting blue rivers and green valleys, collaborative group work")
    },
    "pre_assessment": [
        "Have you ever used a map to find something? What did the map look like?",
        "What do you think a river looks like on a map versus in real life?",
        "Draw a map of your classroom — what would it look like from above?"
    ],
    "reflections": [
        "How is looking at a map different from standing on the ground looking around?",
        "Why do you think water always ends up in the lowest parts of the land?"
    ],
    "reflection_exemplars": [
        ("How is looking at a map different from standing on the ground looking around?", "When you stand on the ground, you can only see what is right in front of you. You cannot see what is on the other side of a mountain or how a river bends. A map shows you everything from above, like you are a bird flying very high. You can see the whole area at once — all the mountains, rivers, and lakes — and understand how they fit together.")
    ],
    "cast_items": [
        "Identify land and water features on a map",
        "Explain how a map represents what the land looks like from above",
        "Describe where water collects based on the shape of the land"
    ],
    "cast_questions": [
        ("Multiple Choice:", "On a map, you see a blue winding line between two brown mountain shapes. What does the blue line most likely represent?"),
        ("Constructed Response:", "Explain how a map helps us understand a place we have never visited. What can a map show us about the land and water?")
    ],
    "extend_components": [
        ("Map Scale", "How big or small the map is compared to the real world — a map of your school fits on paper, but the real school is much bigger"),
        ("Map Symbols", "Special shapes and colors on maps that stand for real things — like blue for water, triangles for mountains, and green for forests")
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model (map) to represent the shapes and kinds of land and bodies of water in an area."),
        ("Disciplinary Core Idea", "ESS2.B Plate Tectonics and Large-Scale System Interactions", "Maps show where things are located. One can map the shapes and kinds of land and water in any area."),
        ("Crosscutting Concept", "Patterns", "Students identify patterns in where water collects (low areas) and where land rises (high areas) on maps.")
    ],
    "background_intro": "Maps are one of the oldest and most useful tools humans have ever created. From ancient cave drawings to satellite images, maps help us understand the shape of our world and find our way around it.",
    "background_sections": [
        ("What Maps Show Us", "Maps are flat representations of the Earth's surface, showing features from a bird's eye view. They use colors, lines, and symbols to represent real things. Blue usually shows water — oceans, rivers, and lakes. Green often shows forests or low-lying land. Brown shows mountains or deserts. Maps can show a small area like your neighborhood or a whole continent."),
        ("Landforms and Bodies of Water", "Earth's surface has many different shapes. Mountains are tall peaks of land that rise high above the surrounding area. Valleys are low areas between mountains. Plains are large flat areas of land. Rivers are flowing bodies of water that travel from high areas to low areas. Lakes are bodies of water surrounded by land. Oceans are the largest bodies of water on Earth."),
        ("How Water Shapes the Land", "Water always flows downhill because of gravity. Rain falls on mountains and flows down into valleys, creating streams and rivers. Rivers carry water to the lowest points, where it collects in lakes or flows all the way to the ocean. Over millions of years, water carves valleys, creates canyons, and shapes the land we see today.")
    ],
    "lever_L": "Students identify land height as an external component and water location and map features as internal components that change based on the shape of the terrain.",
    "lever_E": "Students determine that land height affects where water flows — water moves from high areas to low areas (negative relationship between land height and water accumulation at that spot).",
    "lever_V": "Students build a model (map) showing how different land heights create different features and determine where water collects.",
    "lever_Ev": "Students run mountain, flat plains, and valley scenarios to see how different land shapes create different maps and water patterns.",
    "lever_R": "Students add map scale or map symbols to explore how maps communicate additional information about the land.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with colorful map imagery", "say": "Have you ever looked at a map? What did you see on it? Today we are going to learn how maps show us what the Earth looks like!", "do": "Show a simple map and a satellite photo of the same area. Ask: Can you see the same things in both?", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn Today?", "visual": "Learning goals and vocabulary", "say": "Today we are going to learn to read maps AND build our own 3D map!", "do": "Read objectives together. Introduce map, landform, and body of water with pictures.", "time": "3 min"},
        {"num": "Slide 3", "title": "The Big Question", "visual": "How do maps help us find and understand things?", "say": "How can a piece of paper or a screen show you what a mountain or a river looks like? Maps are like magic pictures of the Earth!", "do": "Show a photo of a mountain and then the same mountain on a map. Ask: How did the mapmaker show the mountain?", "time": "3 min"},
        {"num": "Slide 4", "title": "Let's Build a Model!", "visual": "LEVER steps overview", "say": "We are going to build a model to understand how the shape of the land decides where water goes.", "do": "Preview LEVER steps. Show crumpled paper as a quick 3D land model — pour water on it to show flow.", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Sort the Parts", "visual": "Component cards: Land Height, Water Location, Map Features", "say": "What are the parts of our mapping system? Land Height is something nature built. Water and Map Features change based on the land.", "do": "Guide sorting: Land Height is external, Water Location and Map Features are internal.", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect with Arrows", "visual": "Arrows between components", "say": "When the land is very tall like a mountain, where does the water go? Up or down?", "do": "Draw arrows showing Land Height affects Water Location (water flows to low areas). Discuss how maps show these features.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Run the Simulation!", "visual": "Simulation predictions and results", "say": "Let us test three areas: a mountain, flat plains, and a valley. Where will the water be in each?", "do": "Students predict then run simulations. Compare how each area looks on a map. Use clay models if possible.", "time": "8 min"},
        {"num": "Slide 8", "title": "What Did We Discover?", "visual": "Key discoveries about maps and landforms", "say": "Now you can read a map! Blue means water, and water always flows to the lowest spot. Maps show us the world from above!", "do": "Give each student a simple map to read. Ask them to find the mountains, rivers, and flat areas.", "time": "7 min"}
    ],
    "sort_reasoning": "Land Height is external because it is determined by natural forces over millions of years — mountains, valleys, and plains already exist before we make a map. Water Location and Map Features are internal because where water collects depends on the land shape, and what appears on the map depends on what the land and water look like.",
    "relationships": [
        ("Land Height to Water Location", "NEGATIVE (-)", "When land is high (mountains), water does not stay there — it flows downhill. Water collects in the lowest areas like valleys, lakes, and rivers. So tall land means less water at the top and more water at the bottom."),
        ("Land Height to Map Features", "POSITIVE (+)", "Different land heights create different map features. Mountains show as brown bumpy shapes, valleys show as low areas between peaks, and flat plains show as smooth green areas. The more varied the land height, the more interesting the map.")
    ],
    "sim_answers": [
        ("Mountain Area", "When Land Height is tall (mountain), Water Location is at the bottom in valleys and rivers. The map shows brown peaked shapes for mountains with blue lines (rivers) running down the sides into the valleys. Water flows away from the mountain tops."),
        ("Flat Plains", "When Land Height is flat, water spreads out across the land or collects in shallow lakes. The map shows large green or brown flat areas with some blue patches for lakes. There are no mountain symbols because the land is smooth and even.")
    ],
    "stem_intro": "Present the challenge: A park ranger needs a 3D map to help visitors understand the land around a new nature park. Your team will build a model with mountains, valleys, rivers, and lakes so visitors can see what the park looks like before they explore it.",
    "stem_concepts": [
        ("Bird's Eye View", "Maps show the world from above — like you are a bird flying over the area. Your 3D model should make sense when looked at from the top and from the side."),
        ("Water Flows Downhill", "Water always moves from high places to low places because of gravity. When building your map, put rivers flowing from mountains down into valleys and lakes."),
        ("Map Colors and Symbols", "Real maps use colors to show features — blue for water, green for low land, brown for high land. Use colors on your 3D model to help visitors understand what they are looking at.")
    ],
    "stem_eval": [
        ("Expert (4)", "3D map includes multiple landforms and water features, is accurately colored, and student explains how the map represents real land"),
        ("Proficient (3)", "3D map includes mountains and water features and student can explain what each part represents"),
        ("Developing (2)", "3D map has some features but student struggles to explain how maps represent real places"),
        ("Beginning (1)", "3D map is incomplete or does not accurately show land and water features")
    ],
    "support": [
        "Provide a simple satellite photo alongside a map of the same area for comparison",
        "Use pre-made clay shapes (mountain, valley, flat) that students can arrange before building their own",
        "Sentence frame: 'On my map, the ___ is shown by ___ because ___'"
    ],
    "extensions": [
        "Use a satellite view on a classroom computer to look at your school from above — compare to a hand-drawn map of the school",
        "Research the deepest ocean and the tallest mountain on Earth — how far apart are they on a world map?",
        "Create a treasure map of the school playground using map symbols for landmarks"
    ],
    "cross_curr": [
        ("Math", "Measure the height of your clay mountains in centimeters and compare — which mountain is tallest? Create a bar graph."),
        ("ELA", "Write directions to a treasure on your 3D map using words like north, south, near the river, and over the mountain"),
        ("Art", "Paint a landscape picture showing the same area your map represents — what does it look like from the ground versus from above?")
    ],
    "misconceptions": [
        ("Maps show exactly what you see from the ground", "Maps show a bird's eye view — from above. They look very different from what you see standing on the ground. You cannot see a river winding for miles when you stand next to it, but on a map you can see its entire path from start to end.", "Stand up and describe what you see in the classroom. Then look at a floor plan of the classroom. Ask: Do these look the same? Why not?"),
        ("Blue on a map means the sky", "Blue on most maps represents water — oceans, rivers, lakes, and streams. Maps show the Earth's surface, not the sky. When you see blue on a map, think water!", "Point to blue areas on a map. Ask: Is this the sky? No! It is the ocean (or a lake or river). Blue means water on maps."),
        ("Mountains are always covered in snow", "Not all mountains have snow! Only the very tallest mountains are cold enough at the top for snow to stay year-round. Many mountains are covered in forests, grass, or bare rock. The height and location of the mountain determines what is on top.", "Show pictures of different mountains — snowy ones, green forested ones, and desert mountains. Ask: Are these all mountains? Yes! Mountains come in many types.")
    ]
}

L07 = {
    "id": "G02-L07",
    "title": "What Makes Wind Blow?",
    "subtitle": "The Invisible Force That Moves the Air",
    "ngss": "2-ESS2-3",
    "ngss_desc": "Obtain information to identify where water is found on Earth and that it can be solid or liquid.",
    "big_question": "You cannot see wind, but you can feel it — what makes the air start moving?",
    "objectives": [
        "Describe what wind is and how we know it is there even though we cannot see it",
        "Explain that the sun heating the ground unevenly causes air to move and create wind",
        "Observe and record how wind affects objects in the environment"
    ],
    "vocabulary": [
        ("Wind", "Moving air — when air flows from one place to another you feel it as wind"),
        ("Temperature", "How hot or cold something is — the sun makes some areas warmer than others"),
        ("Weather", "What the air outside is like on any given day — sunny, rainy, windy, cloudy, hot, or cold")
    ],
    "components": [
        ("Sun Heating", "How much the sun warms the ground — dark surfaces heat up more than light surfaces", True),
        ("Air Movement", "How fast the air moves from warm areas to cool areas — warm air rises, cool air rushes in", False),
        ("Wind Strength", "How strong the wind blows — depends on how much the air is moving", False)
    ],
    "think_about_it": "When the sun heats the ground a lot, what happens to the air above it? Does more heating make more wind or less wind?",
    "scenarios": [
        ("Hot Sunny Day", "Set Sun Heating to high and observe how Air Movement and Wind Strength change"),
        ("Cool Cloudy Day", "Set Sun Heating to low and observe the difference in Air Movement and Wind Strength")
    ],
    "sim_scenarios": [
        ("Hot Sunny Day", "Sun Heating set to high", "What do you predict will happen to Wind Strength when the sun heats the ground a lot?"),
        ("Cool Cloudy Day", "Sun Heating set to low", "What do you predict will happen to Air Movement when it is cloudy and the ground stays cool?"),
        ("Beach Breeze", "Sun Heating set to high over land, low over water", "At the beach, the sand gets hot but the water stays cool. Will there be wind? Which way?")
    ],
    "discoveries": [
        "Wind is moving air — it happens when air flows from one area to another",
        "The sun heats the ground unevenly — dark areas and land heat up faster than light areas and water",
        "Warm air rises because it is lighter, and cooler air rushes in to take its place — that rushing air is wind!",
        "More heating difference means stronger wind — that is why beaches are breezy on hot days"
    ],
    "answer": "Wind is air on the move! The sun heats the ground, but it does not heat it evenly — some spots get hotter than others. The air above hot spots warms up and rises because warm air is lighter. Then cooler air from nearby rushes in to fill the space. That rushing air is what we feel as wind! The bigger the temperature difference, the stronger the wind blows.",
    "stem_title": "Build a Wind Detector",
    "stem_mission": "Design and build a simple tool that can detect wind and show which direction it is blowing.",
    "stem_scenario": "A weather station at your school needs a tool to measure wind. Your team has been asked to build a wind detector that shows when wind is blowing and which direction it comes from. Test it outside!",
    "stem_questions": [
        "How will your wind detector move when the wind blows?",
        "How will you tell which DIRECTION the wind is coming from?",
        "What will happen to your detector on a calm day with no wind?"
    ],
    "stem_design_qs": [
        "What lightweight materials will you use that can move in the wind — streamers, paper, or fabric?",
        "How will your detector be attached so it does not blow away?",
        "How will you test your detector — by a fan first, then outside?",
        "How can you improve your detector after the first test?"
    ],
    "career": "Meteorologists study weather patterns, including wind, to predict storms, temperature changes, and weather conditions. They use tools like weather vanes and anemometers every day. They earn $50,000–$95,000/year.",
    "images": {
        "cover": ("cover-wind.png", "Colorful ribbons and streamers blowing dramatically in strong wind against a bright blue sky, dynamic motion blur, vivid colors, cinematic outdoor photography"),
        "landscape": ("landscape-wind.png", "Diverse 2nd grade students (7-8 years old, wide variety of ethnicities) outside on a windy day with hair and jackets blowing, holding pinwheels and streamers, laughing, bright natural sunlight, editorial photo quality"),
        "modeling": ("modeling-wind.png", "A colorful kid-friendly scientific diagram showing the sun heating the ground, warm air rising with red arrows, cool air rushing in with blue arrows to create wind — cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-wind.png", "A teacher with diverse 2nd graders (7-8 years old, wide variety of ethnicities) gathered by a window watching tree branches move in the wind, teacher asking questions, bright modern classroom"),
        "stem": ("stem-wind.png", "Diverse 2nd graders (7-8 years old, wide mix of ethnicities) building wind detectors from straws, paper cups, and streamers at their desks, testing them with a small fan, excited collaborative group work")
    },
    "pre_assessment": [
        "Can you see wind? How do you know when it is windy outside?",
        "What do you think makes the air start moving?",
        "Draw a picture showing a windy day — how can we tell it is windy in your picture?"
    ],
    "reflections": [
        "If you cannot see wind, how do you know it is there?",
        "Why do you think it is often breezier near the ocean or a lake?"
    ],
    "reflection_exemplars": [
        ("If you cannot see wind, how do you know it is there?", "Even though wind is invisible, we can feel it on our skin, hear it whooshing, and see what it does. Wind blows leaves around, makes flags wave, pushes clouds across the sky, and moves our hair. We use evidence from our senses to know wind is there even though the air itself is invisible.")
    ],
    "cast_items": [
        "Describe what wind is and how it is created by the sun",
        "Explain how we can observe wind even though we cannot see it",
        "Predict wind strength based on how much the sun heats the ground"
    ],
    "cast_questions": [
        ("Multiple Choice:", "On a hot summer day at the beach, you feel a cool breeze blowing from the water toward the sand. Why does the breeze blow from the water to the sand?"),
        ("Constructed Response:", "Explain what wind is and what causes it. Use the words 'sun,' 'warm air,' and 'cool air' in your answer.")
    ],
    "extend_components": [
        ("Surface Type", "What the ground is made of — dark pavement heats up faster than grass or water, creating temperature differences"),
        ("Time of Day", "How the sun's position changes heating — midday sun heats more than morning or evening sun")
    ],
    "dimensions": [
        ("Science Practice", "Obtaining, Evaluating, and Communicating Information", "Students obtain information about wind patterns and communicate observations about how wind affects objects in the environment."),
        ("Disciplinary Core Idea", "ESS2.D Weather and Climate", "Weather is the combination of sunlight, wind, snow or rain, and temperature in a particular region at a particular time. Wind is one of the key components of weather."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify that uneven heating by the sun causes air to move, creating wind as a direct effect.")
    ],
    "background_intro": "Wind is one of the most common weather phenomena on Earth, yet most people never think about what actually causes it. Understanding wind helps us predict weather, design buildings, and even generate electricity.",
    "background_sections": [
        ("What Is Wind?", "Wind is simply air in motion. Air is real matter — it has weight and takes up space, even though we cannot see it. When air moves from one place to another, we feel it as wind. A gentle wind is called a breeze, and a very strong wind can be a gust or even a storm. Wind can be as soft as a whisper or as powerful as a hurricane."),
        ("Why Does Air Move?", "The sun heats the Earth's surface, but it does not heat it evenly. Dark surfaces like pavement absorb more heat and get hotter. Light surfaces and water stay cooler. The air above hot spots warms up and becomes lighter, so it rises. Cooler, heavier air nearby rushes in to take the warm air's place. This movement of air is wind. The bigger the temperature difference between two areas, the stronger the wind blows."),
        ("Wind in Our Lives", "Wind affects our daily lives in many ways. It carries seeds to new places, pushes clouds across the sky, creates waves on the ocean, and can even generate electricity through wind turbines. People have used wind power for thousands of years — from sailing ships to windmills. Understanding wind patterns helps meteorologists predict the weather and warn us about storms.")
    ],
    "lever_L": "Students identify sun heating as an external component and air movement and wind strength as internal components that change based on how much the sun heats the ground.",
    "lever_E": "Students determine that more sun heating causes more air movement (positive), and more air movement causes stronger wind (positive).",
    "lever_V": "Students build a model showing how the sun's uneven heating creates air movement and wind.",
    "lever_Ev": "Students run hot day and cool day scenarios to compare how heating affects wind strength.",
    "lever_R": "Students add surface type or time of day to explore why wind changes throughout the day and in different locations.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with windy day imagery", "say": "Can you see wind? No! But you can FEEL it. What do you think makes the air move?", "do": "Turn on a small fan. Ask: Is there wind in our classroom now? How do you know?", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn Today?", "visual": "Learning goals and vocabulary", "say": "Today we are going to solve the mystery of what makes wind blow!", "do": "Read objectives together. Introduce wind, temperature, and weather with examples.", "time": "3 min"},
        {"num": "Slide 3", "title": "The Big Question", "visual": "What makes wind blow?", "say": "Wind is invisible — so what is it really? And where does it come from?", "do": "Hold up a tissue near a fan to show wind in action. Ask: What is pushing the tissue?", "time": "3 min"},
        {"num": "Slide 4", "title": "Let's Build a Model!", "visual": "LEVER steps overview", "say": "We are going to build a model to figure out how the sun creates wind.", "do": "Preview LEVER steps. Quick demo: hold hands above a warm surface and a cool surface — feel the difference.", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Sort the Parts", "visual": "Component cards: Sun Heating, Air Movement, Wind Strength", "say": "What causes wind? The sun heats the ground. The air starts to move. We feel wind! Which part starts it all?", "do": "Guide sorting: Sun Heating is external (it starts the process), Air Movement and Wind Strength are internal.", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect with Arrows", "visual": "Arrows between components", "say": "When the sun heats the ground MORE, does the air move more or less? Does the wind get stronger or weaker?", "do": "Draw positive arrows from Sun Heating to Air Movement and from Air Movement to Wind Strength.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Run the Simulation!", "visual": "Simulation predictions and results", "say": "Let us test a hot sunny day and a cool cloudy day. Predict first: which one will be windier?", "do": "Students predict, then run simulations. Compare wind strength in each scenario. Discuss the beach breeze scenario.", "time": "8 min"},
        {"num": "Slide 8", "title": "What Did We Discover?", "visual": "Key discoveries about wind", "say": "Now you know the secret of wind — it is all about the sun heating things up unevenly! Warm air rises, cool air rushes in, and that is WIND!", "do": "Go outside briefly to observe wind clues — flags, tree branches, leaves. Record wind observations.", "time": "7 min"}
    ],
    "sort_reasoning": "Sun Heating is external because the sun provides heat from outside the air system — we cannot control how much the sun shines. Air Movement and Wind Strength are internal because they happen as a result of the sun's heating. The air responds to temperature differences by moving.",
    "relationships": [
        ("Sun Heating to Air Movement", "POSITIVE (+)", "When the sun heats the ground more, the air above it warms up and rises faster. This creates more air movement as cooler air rushes in to replace the rising warm air. More heating means more air circulation."),
        ("Air Movement to Wind Strength", "POSITIVE (+)", "When air moves faster from cool areas to warm areas, the wind is stronger. More air movement means stronger gusts. On calm days when the sun is hidden, there is less air movement and lighter wind.")
    ],
    "sim_answers": [
        ("Hot Sunny Day", "When Sun Heating is high, Air Movement is fast and Wind Strength is strong. The sun heats the ground a lot, making the air above it very warm. That warm air rises quickly and cool air rushes in fast — creating strong wind. This is why hot summer days can be breezy."),
        ("Cool Cloudy Day", "When Sun Heating is low, Air Movement is slow and Wind Strength is weak. Without much sun, the ground stays cool and the air temperature is more even. There is not much temperature difference to push air around, so the wind is gentle or barely there.")
    ],
    "stem_intro": "Present the challenge: Your school needs a weather station! Your team will build a wind detector that shows when wind is blowing and which direction it comes from. Test it with a fan first, then take it outside to see if real wind works the same way.",
    "stem_concepts": [
        ("Wind Is Moving Air", "Wind is invisible air in motion. Your detector needs to respond to moving air by moving itself — lightweight materials like streamers, pinwheels, or paper flags work great."),
        ("Direction Matters", "Wind blows FROM one direction TO another. Your detector should show which way the wind is coming from, not just that wind exists."),
        ("Strength Varies", "Some winds are gentle breezes and some are strong gusts. A good wind detector can show the difference — moving a little in light wind and a lot in strong wind.")
    ],
    "stem_eval": [
        ("Expert (4)", "Wind detector responds to wind, shows direction, indicates strength, and student explains how wind is created"),
        ("Proficient (3)", "Wind detector moves in wind and student can describe what wind is and what causes it"),
        ("Developing (2)", "Wind detector moves but student has difficulty explaining what wind is or what causes it"),
        ("Beginning (1)", "Wind detector does not respond to wind or student cannot describe wind")
    ],
    "support": [
        "Provide pre-cut streamers and pinwheel templates so students can focus on design rather than cutting",
        "Use a fan at different speeds to demonstrate light breeze versus strong wind",
        "Sentence frame: 'Wind is ___ moving from ___ to ___. My detector shows this because ___'"
    ],
    "extensions": [
        "Check wind direction every day for a week using your detector and record the data on a chart",
        "Research how wind turbines use wind to make electricity and draw a diagram",
        "Compare how wind affects different objects — a feather, a leaf, a rock, and a paper cup"
    ],
    "cross_curr": [
        ("Math", "Record wind observations (strong, medium, weak, none) for five days and make a tally chart and bar graph"),
        ("ELA", "Write a short weather report for your school describing today's wind — direction, strength, and what it is moving"),
        ("Art", "Create a windy day painting using streaks and swirls to show invisible wind moving through a landscape")
    ],
    "misconceptions": [
        ("Wind comes from fans or machines", "Natural wind is NOT made by machines — it is created by the sun! The sun heats the Earth unevenly, warm air rises, and cooler air rushes in. That rushing air is wind. Fans copy nature by pushing air with spinning blades, but outdoor wind comes from temperature differences.", "Go outside on a windy day. Ask: Is there a giant fan somewhere? No! The sun is making this wind by heating the ground."),
        ("Wind is only there on stormy days", "Wind happens almost every day, not just during storms! Even on nice sunny days, you can often feel a breeze. Storms have VERY strong wind, but gentle breezes happen whenever there are temperature differences in the air — which is almost always.", "Take students outside on a calm day. Hold up a streamer or tissue. Ask: Is there ANY air movement? Usually there is at least a tiny breeze!"),
        ("Cold air makes wind", "Cold air alone does not make wind — the DIFFERENCE between warm and cold air makes wind. You need warm air in one place and cool air in another. The warm air rises and the cool air moves in to replace it. Without a temperature difference, there would be no wind.", "Use two balloons — one filled with warm breath and one from the fridge. Ask: Does one balloon move the other? No — they need to be in different places to create air movement.")
    ]
}

L08 = {
    "id": "G02-L08",
    "title": "How Fast Does Ice Melt?",
    "subtitle": "Exploring Reversible Changes in Matter",
    "ngss": "2-PS1-4",
    "ngss_desc": "Construct an argument with evidence that some changes caused by heating or cooling can be reversed and some cannot.",
    "big_question": "What makes ice melt fast or slow — and can you turn the water back into ice again?",
    "objectives": [
        "Observe and describe how temperature affects the speed at which ice melts",
        "Explain that melting ice is a reversible change — the water can be frozen back into ice",
        "Compare ice melting under different conditions and use evidence to explain the differences"
    ],
    "vocabulary": [
        ("Melting", "When a solid heats up enough to turn into a liquid — like ice turning into water"),
        ("Freezing", "When a liquid cools down enough to turn into a solid — like water turning into ice"),
        ("Reversible Change", "A change that can be undone — melting and freezing go back and forth"),
        ("Temperature", "How hot or cold something is — measured with a thermometer")
    ],
    "components": [
        ("Surrounding Temperature", "How warm or cool the area around the ice cube is — warmer rooms melt ice faster", True),
        ("Melting Speed", "How quickly the ice cube changes from solid to liquid — depends on how much heat it gets", False),
        ("Ice Size", "How big the ice cube is — it gets smaller as it melts and the water puddle grows", False)
    ],
    "think_about_it": "When the surrounding temperature gets hotter, what happens to the melting speed? What happens to the ice size?",
    "scenarios": [
        ("Warm Room", "Set Surrounding Temperature to warm and observe how fast the ice melts"),
        ("Cold Spot", "Set Surrounding Temperature to cold and observe the melting speed and ice size over time")
    ],
    "sim_scenarios": [
        ("Warm Room", "Surrounding Temperature set to warm", "What do you predict will happen to Melting Speed when the ice is in a warm room?"),
        ("Cold Spot", "Surrounding Temperature set to cold", "What do you predict will happen to Ice Size when the ice is in a cold place like a refrigerator?"),
        ("Hot Sunshine", "Surrounding Temperature set to very hot", "How fast will the ice melt in direct hot sunshine compared to a warm room?")
    ],
    "discoveries": [
        "Ice melts faster in warmer temperatures because more heat energy transfers to the ice",
        "In cold temperatures, ice melts very slowly or not at all because there is less heat to transfer",
        "Melting is a reversible change — you can freeze the water back into ice by cooling it down",
        "The amount of water from a melted ice cube is the same amount of matter as the original ice cube"
    ],
    "answer": "Ice melts because heat energy from the surroundings transfers into the ice. The warmer the surroundings, the faster the heat transfers, and the faster the ice melts! In a hot place, ice melts quickly. In a cold place, it melts slowly or stays frozen. The amazing part? This change is REVERSIBLE! You can freeze the water back into ice, and it is the same amount of matter — just in a different form.",
    "stem_title": "Design an Ice Keeper",
    "stem_mission": "Build a container that keeps an ice cube frozen as long as possible — the team whose ice lasts longest wins!",
    "stem_scenario": "A lunch company wants to keep food cold during delivery without using electricity. Your team has been challenged to design an Ice Keeper — a container that slows down melting as much as possible. Use what you learned about temperature and melting to make your design.",
    "stem_questions": [
        "What materials might keep heat AWAY from the ice to slow melting?",
        "Would wrapping the ice in something make it melt faster or slower?",
        "How will you know if your Ice Keeper is working?"
    ],
    "stem_design_qs": [
        "What insulating materials will you test — fabric, cotton, bubble wrap, foil, or newspaper?",
        "Should you use one layer or many layers around the ice?",
        "How will you compare your Ice Keeper to just leaving the ice in the open?",
        "How long do you predict your ice will last compared to the open ice cube?"
    ],
    "career": "Refrigeration Engineers design cooling systems for homes, restaurants, hospitals, and trucks that deliver food. They keep things cold so food stays fresh and medicine stays safe. They earn $50,000–$90,000/year.",
    "images": {
        "cover": ("cover-ice.png", "A crystal-clear ice cube melting on a warm surface with water droplets and light refractions, close-up macro photography, vivid colors, bright studio lighting"),
        "landscape": ("landscape-ice.png", "Diverse 2nd grade students (7-8 years old, wide variety of ethnicities) sitting at a table watching ice cubes melt in different conditions — one in the sun, one wrapped in fabric, one in the shade — comparing and recording observations, bright modern classroom, editorial photo quality"),
        "modeling": ("modeling-ice.png", "A colorful kid-friendly scientific diagram showing an ice cube in three stages — solid ice, partially melted, fully melted water — with red heat arrows showing energy transfer, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-ice.png", "A teacher with diverse 2nd graders (7-8 years old, wide variety of ethnicities) discussing ice melting, teacher holding a dripping ice cube, students watching with fascination, bright classroom"),
        "stem": ("stem-ice.png", "Diverse 2nd graders (7-8 years old, wide mix of ethnicities) wrapping ice cubes in various materials — fabric, foil, newspaper, cotton — testing their Ice Keeper designs, excited collaborative group work")
    },
    "pre_assessment": [
        "What happens to an ice cube when you take it out of the freezer?",
        "Can you turn water back into ice? How?",
        "Draw what you think happens to an ice cube when it melts — where does the ice go?"
    ],
    "reflections": [
        "Why does ice melt faster in some places than others?",
        "What makes melting ice different from baking a cookie — can you undo both changes?"
    ],
    "reflection_exemplars": [
        ("What makes melting ice different from baking a cookie — can you undo both changes?", "Melting ice is a reversible change because you can freeze the water back into ice again. The water just changes back and forth between solid and liquid. Baking a cookie is NOT reversible — you cannot un-bake it back into flour, sugar, and eggs. Once the cookie is baked, the ingredients have changed in a way that cannot be undone.")
    ],
    "cast_items": [
        "Describe what causes ice to melt at different speeds",
        "Explain why melting is a reversible change",
        "Use evidence from an investigation to compare melting in different conditions"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Two ice cubes of the same size are placed outside. One is in the shade and one is in direct sunlight. Which ice cube will melt first and why?"),
        ("Constructed Response:", "Explain what happens when an ice cube melts. Is this change reversible? Use evidence from your investigation to support your answer.")
    ],
    "extend_components": [
        ("Insulation", "Materials wrapped around the ice that slow heat transfer — like a blanket for the ice cube"),
        ("Ice Surface Area", "How much of the ice is touching warm air — crushed ice melts faster than a big cube because more surface touches the warm air")
    ],
    "dimensions": [
        ("Science Practice", "Constructing Explanations and Engaging in Argument from Evidence", "Students construct an argument with evidence about what affects ice melting speed and whether the change can be reversed."),
        ("Disciplinary Core Idea", "PS1.B Chemical Reactions", "Heating or cooling a substance may cause changes that can be observed. Sometimes these changes are reversible (like melting/freezing) and sometimes they are not."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify temperature as the cause of melting speed changes and gather evidence to support their explanations.")
    ],
    "background_intro": "Every winter, icicles form and melt, ponds freeze and thaw, and snowflakes turn to puddles. These everyday events demonstrate one of science's most important ideas: matter can change form, and some changes can be reversed.",
    "background_sections": [
        ("How Melting Works", "Ice is solid water — its tiny molecules are locked together in a rigid structure. When heat energy flows into the ice from warmer surroundings, the molecules start vibrating faster. At 0 degrees Celsius (32 degrees Fahrenheit), the molecules break free of their rigid bonds and start sliding past each other. The solid ice becomes liquid water. The warmer the surroundings, the faster heat transfers into the ice, and the faster it melts."),
        ("Reversible vs. Irreversible Changes", "Melting and freezing are reversible changes. Water can go from liquid to solid and back again unlimited times without changing what it is — it is always water. Other changes are irreversible. When you bake a cake, you cannot un-bake it. When you burn wood, you cannot un-burn it. The key difference is that reversible changes only change the FORM of the matter, not WHAT it is."),
        ("Insulators and Heat Transfer", "Some materials slow down the transfer of heat. These are called insulators. Thick fabric, foam, and trapped air all make good insulators. This is why a cooler keeps ice from melting — the insulated walls slow down heat from the warm outside air reaching the cold ice inside. It is also why you wear a coat in winter — the coat insulates your body heat and keeps the cold air out.")
    ],
    "lever_L": "Students identify surrounding temperature as an external component and melting speed and ice size as internal components that change based on how warm or cool the environment is.",
    "lever_E": "Students determine that higher surrounding temperature causes faster melting speed (positive), and faster melting speed causes ice size to shrink more quickly (negative).",
    "lever_V": "Students build a model showing how the surrounding temperature drives melting speed and controls how quickly ice disappears.",
    "lever_Ev": "Students run warm room, cold spot, and hot sunshine scenarios to compare melting speeds under different temperature conditions.",
    "lever_R": "Students add insulation or ice surface area to explore other factors that affect how fast ice melts.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with melting ice imagery", "say": "Who has ever held an ice cube and watched it melt in your hand? What happened? Where did the ice go?", "do": "Give each table group an ice cube on a plate. Ask: What is happening to it right now?", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn Today?", "visual": "Learning goals and vocabulary", "say": "Today we are going to investigate what makes ice melt fast or slow — and whether we can reverse it!", "do": "Read objectives together. Introduce melting, freezing, reversible change, and temperature.", "time": "3 min"},
        {"num": "Slide 3", "title": "The Big Question", "visual": "How fast does ice melt?", "say": "Does ice always melt at the same speed? Or can we make it melt faster or slower? What do you think controls it?", "do": "Quick brainstorm: What could make ice melt FAST? What could keep it frozen LONG? List ideas on the board.", "time": "3 min"},
        {"num": "Slide 4", "title": "Let's Build a Model!", "visual": "LEVER steps overview", "say": "We are going to build a model to figure out what controls how fast ice melts.", "do": "Preview LEVER steps. Show ice cubes in two spots — sunny windowsill and shady corner.", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Sort the Parts", "visual": "Component cards: Surrounding Temperature, Melting Speed, Ice Size", "say": "What affects ice melting? The temperature around the ice is our input. Melting speed and ice size are what we observe.", "do": "Guide sorting: Surrounding Temperature is external; Melting Speed and Ice Size are internal.", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect with Arrows", "visual": "Arrows between components", "say": "When the temperature goes UP, does melting go faster or slower? And what happens to the ice size?", "do": "Draw positive arrow from Temperature to Melting Speed. Draw negative arrow from Melting Speed to Ice Size (ice shrinks).", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Run the Simulation!", "visual": "Simulation predictions and results", "say": "Let us test! One ice cube in a warm spot, one in a cold spot. Predict which melts first!", "do": "Students predict, then run simulations or observe real ice cubes. Record melting times. Compare results.", "time": "8 min"},
        {"num": "Slide 8", "title": "What Did We Discover?", "visual": "Key discoveries and reversibility", "say": "The best part? We can REVERSE this! If we freeze the melted water, it becomes ice again. Not all changes can be undone — but this one can!", "do": "Pour melted ice water into a cup to put in the freezer. Compare to baking a cookie (irreversible). Discuss the difference.", "time": "7 min"}
    ],
    "sort_reasoning": "Surrounding Temperature is external because it is the temperature of the room, sunlight, or shade — it exists before the ice is placed there and we can choose where to put the ice. Melting Speed and Ice Size are internal because they change as a result of how much heat the ice receives from its surroundings.",
    "relationships": [
        ("Surrounding Temperature to Melting Speed", "POSITIVE (+)", "Warmer surroundings transfer more heat energy to the ice, making it melt faster. On a hot day, ice melts very quickly. In a refrigerator, ice melts extremely slowly because there is very little heat to transfer."),
        ("Melting Speed to Ice Size", "NEGATIVE (-)", "When the ice melts faster, it gets smaller more quickly. The solid ice is turning into liquid water, so the ice cube shrinks. Faster melting means the ice disappears sooner.")
    ],
    "sim_answers": [
        ("Warm Room", "When Surrounding Temperature is warm, Melting Speed is fast and Ice Size shrinks quickly. The warm air sends lots of heat energy into the ice, causing it to melt rapidly. Within minutes, the ice cube is much smaller and sitting in a puddle of water."),
        ("Cold Spot", "When Surrounding Temperature is cold, Melting Speed is very slow and Ice Size stays large for a long time. Very little heat transfers to the ice because the surrounding area is already cold. The ice cube barely changes after many minutes.")
    ],
    "stem_intro": "Present the challenge: A lunch delivery company needs to keep food cold without electricity. Your team will design an Ice Keeper container that slows down melting as long as possible. The team whose ice cube lasts the longest wins!",
    "stem_concepts": [
        ("Heat Transfer", "Ice melts because heat energy moves from warm surroundings into the cold ice. To keep ice frozen longer, you need to block that heat transfer with insulating materials."),
        ("Insulation Blocks Heat", "Insulators are materials that slow down heat transfer. Fabric, foam, newspaper, and trapped air are good insulators. Wrapping ice in insulation keeps the warm air away."),
        ("Reversible Changes", "Melting ice into water and freezing water into ice is the same change in two directions. Your Ice Keeper just slows down one direction of this reversible change.")
    ],
    "stem_eval": [
        ("Expert (4)", "Ice Keeper significantly slows melting, student explains how insulation blocks heat transfer, and connects to reversible changes"),
        ("Proficient (3)", "Ice Keeper slows melting and student can explain that insulation keeps heat away from the ice"),
        ("Developing (2)", "Ice Keeper is built but student struggles to explain why insulation slows melting"),
        ("Beginning (1)", "Ice Keeper does not slow melting or student cannot explain the concept")
    ],
    "support": [
        "Provide a variety of insulating materials pre-cut and ready to use so students can focus on design",
        "Set up a control ice cube in the open so students can compare their designs to no protection",
        "Sentence frame: 'My ice melted ___ because the ___ (kept heat away / let heat in) by ___'"
    ],
    "extensions": [
        "Test whether crushed ice or a whole ice cube melts faster — why might size and shape matter?",
        "Investigate whether salt, sugar, or sand changes how fast ice melts when sprinkled on top",
        "Research how Inuit peoples built igloos from ice and snow to stay WARM — how does that work?"
    ],
    "cross_curr": [
        ("Math", "Time how long each ice cube takes to melt in different conditions using a stopwatch, then compare the numbers on a chart"),
        ("ELA", "Write a how-to guide explaining how to keep ice from melting, using step-by-step instructions"),
        ("Art", "Draw a comic strip showing an ice cube's journey from freezer to melting to being refrozen — showing the reversible change")
    ],
    "misconceptions": [
        ("Ice melts because it wants to be water", "Ice does not 'want' anything — it is not alive! Ice melts because heat energy from the warmer surroundings flows into the ice. When enough heat energy enters, the solid structure breaks apart and the ice becomes liquid water. It is all about energy, not choice.", "Hold an ice cube. Ask: Is it choosing to melt? No! YOUR warm hand is sending heat into the ice. Your hand is making it melt."),
        ("The water from melted ice is less than the original ice", "The melted water and the original ice are the same amount of matter! Nothing disappears during melting — the solid just changes into a liquid. If you freeze the water back into ice, you get the same amount of ice back.", "Weigh an ice cube on a scale. Let it melt completely. Weigh the water. Same weight! The matter did not go anywhere."),
        ("You cannot freeze water back into ice at home", "You absolutely can! Just pour water into an ice tray and put it in the freezer. In a few hours, it will be solid ice again. This is what makes melting a REVERSIBLE change — you can go back and forth between solid and liquid over and over.", "Freeze water in a cup. Melt it. Freeze it again. Ask: Is it still water? (Yes!) Can we keep doing this forever? (Yes!)")
    ]
}

L09 = {
    "id": "G02-L09",
    "title": "Why Are There So Many Kinds of Bugs?",
    "subtitle": "Exploring the Diversity of Life on Earth",
    "ngss": "2-LS4-1",
    "ngss_desc": "Make observations of plants and animals to compare the diversity of life in different habitats.",
    "big_question": "Why are there so many different kinds of bugs — and why do they all look so different from each other?",
    "objectives": [
        "Observe and describe differences between insects in the same habitat",
        "Explain that different body features help insects survive in their specific habitat",
        "Compare insects from two different habitats and describe why they look different"
    ],
    "vocabulary": [
        ("Diversity", "Having many different kinds of living things — lots of variety"),
        ("Habitat", "The place where an animal lives and finds everything it needs — food, water, and shelter"),
        ("Insect", "A small animal with six legs, three body parts, and usually wings — like ants, butterflies, and beetles"),
        ("Feature", "A body part or characteristic that helps an animal survive — like wings for flying or hard shells for protection")
    ],
    "components": [
        ("Habitat Type", "The kind of place the insect lives — garden, pond, forest floor, or desert", True),
        ("Body Features", "The special body parts the insect has — wings, shells, long legs, camouflage colors, or antennae", False),
        ("Survival Success", "How well the insect can find food, escape danger, and survive in its habitat", False)
    ],
    "think_about_it": "When the habitat type changes from a garden to a pond, do the insect body features change too? Why would water insects need different features than garden insects?",
    "scenarios": [
        ("Garden Habitat", "Set Habitat Type to garden and observe which Body Features and Survival Success appear"),
        ("Pond Habitat", "Set Habitat Type to pond and observe how the Body Features and Survival Success differ")
    ],
    "sim_scenarios": [
        ("Garden Habitat", "Habitat Type set to garden", "What Body Features do you predict garden insects need to survive? Wings? Camouflage?"),
        ("Pond Habitat", "Habitat Type set to pond", "What Body Features do you predict pond insects need? Can they fly, or do they need to swim?"),
        ("Forest Floor", "Habitat Type set to dark forest floor", "What features would help an insect survive on a dark, damp forest floor?")
    ],
    "discoveries": [
        "Different habitats have different kinds of insects because each habitat requires different survival features",
        "Garden insects often have wings, bright colors for warning, or camouflage to blend in with plants",
        "Pond insects have features for swimming or walking on water, like flat legs or air bubbles",
        "The diversity of insects exists because there are so many different habitats, each needing different adaptations"
    ],
    "answer": "There are so many different kinds of bugs because there are so many different places to live! Each habitat — garden, pond, forest, desert — has different challenges. Insects that live in a garden need wings to fly between flowers and camouflage to hide from birds. Insects near a pond need to swim or walk on water. Over a long time, insects developed different body features to help them survive in their specific home. That is why they all look so different — each one is perfectly designed for its habitat!",
    "stem_title": "Design a Bug for a New Habitat",
    "stem_mission": "Design an imaginary insect with body features perfectly suited to survive in a habitat you choose.",
    "stem_scenario": "Scientists have discovered a brand-new habitat — and they need your help to predict what kind of insect could survive there! Your team will choose a habitat (real or imaginary) and design an insect with body features that help it find food, escape danger, and thrive.",
    "stem_questions": [
        "What habitat will your insect live in and what challenges does that habitat have?",
        "What body features will help your insect find food in that habitat?",
        "How will your insect escape from predators — speed, camouflage, armor, or something else?"
    ],
    "stem_design_qs": [
        "What materials will you use to build your insect model — clay, pipe cleaners, paper, or recycled materials?",
        "How many legs, wings, and special features does your insect have?",
        "What colors and patterns will you give it and why?",
        "How will you present your insect to the class and explain why it is perfect for its habitat?"
    ],
    "career": "Entomologists are scientists who study insects — the most diverse group of animals on Earth! They discover new species, protect crops from pests, and study how insects help ecosystems. They earn $45,000–$85,000/year.",
    "images": {
        "cover": ("cover-bugs.png", "A stunning close-up collage of diverse insects — a colorful butterfly, a shiny beetle, a ladybug, and a dragonfly — against a bright green leaf background, vivid macro photography"),
        "landscape": ("landscape-bugs.png", "Diverse 2nd grade students (7-8 years old, wide variety of ethnicities) outside in a school garden using magnifying glasses to observe insects on plants, bright natural sunlight, curious expressions, editorial photo quality"),
        "modeling": ("modeling-bugs.png", "A colorful kid-friendly scientific diagram showing four insects in their habitats — a butterfly in a garden, a water beetle in a pond, an ant on a forest floor, a beetle in sand — cartoon-style, white background, bold outlines, labeled features"),
        "discussion": ("discussion-bugs.png", "A teacher with diverse 2nd graders (7-8 years old, wide variety of ethnicities) gathered around a terrarium looking at live insects, teacher asking questions and pointing, bright modern classroom"),
        "stem": ("stem-bugs.png", "Diverse 2nd graders (7-8 years old, wide mix of ethnicities) building model insects from clay, pipe cleaners, and recycled materials at their desks, habitat dioramas visible, excited collaborative group work")
    },
    "pre_assessment": [
        "How many different kinds of bugs can you name? Why do you think there are so many?",
        "Do you think a butterfly and a beetle need the same body features? Why or why not?",
        "Draw your favorite insect and label the body parts that you think help it survive."
    ],
    "reflections": [
        "Why do insects in a pond look so different from insects in a garden?",
        "If all insects had the exact same body, could they all survive in every habitat? Why or why not?"
    ],
    "reflection_exemplars": [
        ("Why do insects in a pond look so different from insects in a garden?", "Insects in a pond need to swim, breathe underwater, or walk on water, so they have flat legs, air bubbles, and streamlined bodies. Garden insects need to fly between flowers, hide from birds, and eat leaves, so they have wings, camouflage colors, and special mouthparts. Each habitat has different challenges, so the insects need different body features to survive there.")
    ],
    "cast_items": [
        "Describe how insects in different habitats have different body features",
        "Explain why there are so many different kinds of insects on Earth",
        "Compare two insects from different habitats and describe how their features help them survive"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A water beetle has flat paddle-shaped legs. A grasshopper has long strong jumping legs. Why are their legs so different?"),
        ("Constructed Response:", "Choose two insects from different habitats. Explain how their body features help each one survive in its own habitat.")
    ],
    "extend_components": [
        ("Predator Type", "The kind of animals that eat the insect — birds, frogs, or bigger insects. Different predators require different defenses."),
        ("Food Source", "What the insect eats in its habitat — nectar, leaves, other insects, or decaying matter. Different foods need different mouthparts.")
    ],
    "dimensions": [
        ("Science Practice", "Making Observations", "Students observe and compare insects in different habitats, noting differences in body features and behavior."),
        ("Disciplinary Core Idea", "LS4.D Biodiversity and Humans", "There are many different kinds of living things in any area, and they exist in different places. The diversity of life is connected to the diversity of habitats."),
        ("Crosscutting Concept", "Structure and Function", "Students connect insect body features (structure) to how those features help the insect survive (function) in a specific habitat.")
    ],
    "background_intro": "Insects are the most diverse group of animals on Earth. There are more species of insects than all other animals combined! Understanding why insects are so diverse teaches us about how life adapts to different environments.",
    "background_sections": [
        ("The World of Insects", "Scientists have discovered over one million species of insects, and they estimate there may be millions more waiting to be found! Insects live on every continent including Antarctica. They are found in gardens, forests, deserts, ponds, caves, and even inside our homes. Insects are incredibly diverse because they have adapted to nearly every habitat on Earth."),
        ("Body Features Match Habitats", "Each insect species has body features that help it survive in its specific habitat. Butterflies have long tongues for reaching nectar deep inside flowers. Water beetles have flat, paddle-shaped legs for swimming. Stick insects are shaped and colored exactly like twigs to hide from predators. Walking sticks, leaf insects, and bark beetles all use camouflage to blend into their surroundings. Each feature is an adaptation — a body part that helps the animal survive."),
        ("Why So Many Species?", "There are so many insect species because there are so many different habitats and food sources on Earth. Each unique habitat creates opportunities for insects with different features. A pond needs swimmers. A garden needs fliers. A forest floor needs diggers. Over millions of years, insects have evolved different features for different habitats, creating the incredible diversity we see today.")
    ],
    "lever_L": "Students identify habitat type as an external component and body features and survival success as internal components that are determined by the habitat's challenges.",
    "lever_E": "Students determine that different habitat types produce different body features (the habitat shapes which features are useful), and better-matched features lead to higher survival success.",
    "lever_V": "Students build a model showing how the type of habitat determines which insect body features lead to the best survival.",
    "lever_Ev": "Students run garden, pond, and forest floor scenarios to compare how different habitats produce different insect features.",
    "lever_R": "Students add predator type or food source to explore more reasons why insects in different habitats look different.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with diverse insect imagery", "say": "How many different kinds of bugs can you think of? Beetles, butterflies, ants, dragonflies — why are there SO many?", "do": "Show a poster or slideshow of 8-10 very different-looking insects. Ask: Why do they all look so different?", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn Today?", "visual": "Learning goals and vocabulary", "say": "Today we are going to figure out why there are so many different bugs and why they all look different!", "do": "Read objectives together. Introduce diversity, habitat, insect, and feature with picture cards.", "time": "3 min"},
        {"num": "Slide 3", "title": "The Big Question", "visual": "Why are there so many kinds of bugs?", "say": "There are more than a MILLION different kinds of insects! Why so many? And why do they all have different bodies?", "do": "Show a butterfly and a water beetle side by side. Ask: Why does one have wings and the other has paddles?", "time": "3 min"},
        {"num": "Slide 4", "title": "Let's Build a Model!", "visual": "LEVER steps overview", "say": "We are going to build a model that shows how habitats create different kinds of insects.", "do": "Preview LEVER steps. Show pictures of a garden, a pond, and a forest floor. Ask: Would the same bug survive in all three?", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Sort the Parts", "visual": "Component cards: Habitat Type, Body Features, Survival Success", "say": "The habitat is where the insect lives. Its body features help it survive there. Let us sort our components!", "do": "Guide sorting: Habitat Type is external (it already exists), Body Features and Survival Success are internal.", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect with Arrows", "visual": "Arrows between components", "say": "When we change from a garden to a pond, do the insect features stay the same or change? Why?", "do": "Draw arrows from Habitat Type to Body Features (habitat determines needed features). Draw arrow from Body Features to Survival Success.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Run the Simulation!", "visual": "Simulation predictions and results", "say": "Let us test! What features does an insect need in a garden? A pond? A dark forest floor?", "do": "Students predict which features match each habitat, then run simulations. Compare insects across habitats.", "time": "8 min"},
        {"num": "Slide 8", "title": "What Did We Discover?", "visual": "Key discoveries about insect diversity", "say": "Now we know! There are so many kinds of bugs because there are so many different places to live. Each habitat needs different features!", "do": "Show the million-species statistic. Have students share which habitat-insect match surprised them most.", "time": "7 min"}
    ],
    "sort_reasoning": "Habitat Type is external because the habitat already exists before the insect arrives — gardens, ponds, and forests were not created by insects. Body Features and Survival Success are internal because the insect's features develop in response to habitat challenges, and survival depends on how well those features match the habitat.",
    "relationships": [
        ("Habitat Type to Body Features", "POSITIVE (+)", "Different habitats produce different body feature needs. A pond habitat needs swimming features. A garden habitat needs flying and camouflage features. The habitat shapes which features are most useful for survival."),
        ("Body Features to Survival Success", "POSITIVE (+)", "When an insect has body features that match its habitat well, survival success is high. A water beetle with paddle legs thrives in a pond. A butterfly with wings thrives in a garden. Good feature-habitat match means better survival.")
    ],
    "sim_answers": [
        ("Garden Habitat", "When Habitat Type is garden, the most successful Body Features include wings for flying between flowers, camouflage colors to blend in with leaves, and special mouthparts for eating plants or drinking nectar. Survival Success is high for insects with these features."),
        ("Pond Habitat", "When Habitat Type is pond, the most successful Body Features include flat paddle legs for swimming, ability to breathe underwater using air bubbles, and streamlined bodies for moving through water. Garden features like camouflage coloring for leaves would not help here — pond insects need water features.")
    ],
    "stem_intro": "Present the challenge: Scientists discovered a new habitat and need your help predicting what kind of insect could survive there. Your team will choose a habitat and design an insect with body features perfectly suited to find food, escape danger, and thrive.",
    "stem_concepts": [
        ("Features Match Habitat", "Every insect has body features that help it survive in its specific habitat. Wings help in open spaces, paddle legs help in water, and camouflage helps where predators lurk. Your design should match features to habitat challenges."),
        ("Diversity Comes from Variety", "There are so many insect species because Earth has so many different habitats. Each new habitat creates opportunities for new kinds of insects with new features."),
        ("Survival Depends on Fit", "An insect survives best when its body features match its habitat. A butterfly in a pond would struggle. A water beetle in a desert would fail. Good design means matching features to challenges.")
    ],
    "stem_eval": [
        ("Expert (4)", "Insect model has habitat-appropriate features, student explains how each feature helps survival, and connects to real insect diversity"),
        ("Proficient (3)", "Insect model has features that match the chosen habitat and student can explain why"),
        ("Developing (2)", "Insect model is built but features do not clearly match the habitat or student has difficulty explaining"),
        ("Beginning (1)", "Insect model is incomplete or features have no connection to the chosen habitat")
    ],
    "support": [
        "Provide picture cards of real insects and their habitats for inspiration before designing",
        "Offer pre-made body part options (clay wings, pipe cleaner legs, paper shells) students can combine",
        "Sentence frame: 'My insect has ___ because in the ___ habitat, it needs to ___'"
    ],
    "extensions": [
        "Go on an insect hunt around the school — how many different species can you find in one area?",
        "Compare insects and spiders — what makes them different? (Hint: count the legs!)",
        "Research the rarest insect in the world and create a poster about what makes it special and where it lives"
    ],
    "cross_curr": [
        ("Math", "Count and tally the different types of insects found during an outdoor insect hunt, then make a bar graph of the results"),
        ("ELA", "Write a description of your designed insect as if you are a scientist who just discovered a new species"),
        ("Art", "Create a detailed scientific illustration of your designed insect with labeled body parts and habitat background")
    ],
    "misconceptions": [
        ("All bugs are the same", "Insects are incredibly diverse — there are over a million different species! A ladybug, a dragonfly, and an ant may all be insects, but they have very different bodies, eat different foods, and live in different places. Their differences help them survive in their own specific habitats.", "Show pictures of 5 very different insects. Ask: Are these the same? They are all insects, but look how different they are! Each is designed for its own habitat."),
        ("Bugs live everywhere and do not need a specific home", "Every insect species has a habitat it is best suited for. A water beetle cannot survive in a desert, and a desert beetle would struggle in a pond. Insects need specific conditions — temperature, food, water, shelter — that their body features are designed for.", "Ask: Could a fish live in a tree? Could a bird live underwater? Insects are the same — each species needs its own kind of home."),
        ("Insects choose to look the way they do", "Insects do not choose their body features — they are born with them! Over many, many generations, insects that had features matching their habitat survived better and had more babies. Those babies inherited the same helpful features. This is how species develop features that match their habitats over a very long time.", "Show a stick insect. Ask: Did this bug decide to look like a stick? No! Bugs that happened to look like sticks were better at hiding, so they survived and had babies that also looked like sticks.")
    ]
}

L10 = {
    "id": "G02-L10",
    "title": "How Do Rocks Tell Stories?",
    "subtitle": "Reading Earth's History from Rocks and Layers",
    "ngss": "2-ESS1-1",
    "ngss_desc": "Use information from several sources to provide evidence that Earth events can occur quickly or slowly.",
    "big_question": "How can a rock tell us a story about something that happened on Earth a long, long time ago?",
    "objectives": [
        "Describe how different types of rocks form from different Earth events",
        "Explain that rock layers tell a story about what happened in the past — older layers are on the bottom",
        "Use rock evidence to figure out whether an Earth event happened quickly or slowly"
    ],
    "vocabulary": [
        ("Rock Layer", "A flat section of rock that formed at a specific time — like pages in a history book stacked on top of each other"),
        ("Erosion", "When wind, water, or ice slowly wears away rock and carries tiny pieces to new places"),
        ("Sediment", "Tiny pieces of rock, sand, and soil that settle in layers and can eventually become new rock")
    ],
    "components": [
        ("Earth Event", "Something that happens on Earth — a volcano erupting, a river flowing, a flood, or wind blowing sand", True),
        ("Rock Type", "What kind of rock forms — smooth river rock, layered sedimentary rock, or rough volcanic rock", False),
        ("Rock Layer Pattern", "How the rock layers stack up and what they look like — each layer tells about a different time", False)
    ],
    "think_about_it": "When a different Earth event happens (like a volcano versus a river), does the same type of rock form? Or do different events make different rocks?",
    "scenarios": [
        ("Slow River", "Set Earth Event to slow-flowing river and observe what Rock Type and Rock Layer Pattern form"),
        ("Fast Volcano", "Set Earth Event to volcanic eruption and observe how the Rock Type and Rock Layer Pattern are different")
    ],
    "sim_scenarios": [
        ("Slow River", "Earth Event set to slow-flowing river over many years", "What do you predict the rock will look like if it forms slowly in a river? Smooth or rough?"),
        ("Fast Volcano", "Earth Event set to volcanic eruption", "What do you predict volcanic rock will look like? Will it have smooth layers or be rough and bubbly?"),
        ("Slow Wind Erosion", "Earth Event set to wind blowing sand for thousands of years", "What kind of layers do you predict wind-blown sand will create?")
    ],
    "discoveries": [
        "Different Earth events create different types of rocks — volcanoes make rough, bubbly rock, rivers make smooth, rounded rock",
        "Rock layers are like pages in a history book — the bottom layers are oldest and the top layers are newest",
        "Some Earth events happen quickly (earthquakes, volcanoes) and some happen slowly (erosion, sediment building up)",
        "Scientists read rock layers to figure out what happened on Earth millions of years ago"
    ],
    "answer": "Rocks are Earth's history books! Each type of rock tells a different story. Smooth, rounded rocks were shaped by water flowing over them for a very long time. Rough, bubbly rocks were made by volcanoes erupting quickly. Rock layers stack up over time — the bottom layer is the oldest and the top is the newest. By studying rocks and their layers, scientists can figure out what happened on Earth long before any humans were around to see it!",
    "stem_title": "Build a Rock Layer Timeline",
    "stem_mission": "Create a model showing rock layers that tell the story of three different Earth events over time.",
    "stem_scenario": "A museum needs a display that shows how rock layers record Earth's history. Your team will build a model with at least three layers, each representing a different Earth event, to teach visitors how scientists read rocks like history books.",
    "stem_questions": [
        "What three Earth events will your layers represent?",
        "Which layer is the oldest in your model and which is the newest?",
        "How can visitors tell the difference between a layer made by a river and one made by a volcano?"
    ],
    "stem_design_qs": [
        "What materials will you use for each layer — sand, clay, gravel, or pebbles?",
        "How will you make each layer look different to represent different Earth events?",
        "How will you label your layers so visitors know what each one represents?",
        "How does your model show that some events are fast and some are slow?"
    ],
    "career": "Geologists study rocks, minerals, and the Earth's history. They help find resources like water and minerals, predict earthquakes and volcanoes, and teach us about Earth's past. They earn $55,000–$100,000/year.",
    "images": {
        "cover": ("cover-rocks.png", "A dramatic canyon wall showing colorful horizontal rock layers in reds, oranges, and tans, bright sunlight, vivid geological photography, clear blue sky above"),
        "landscape": ("landscape-rocks.png", "Diverse 2nd grade students (7-8 years old, wide variety of ethnicities) on a nature walk examining rocks with magnifying glasses and rock hammers, colorful rocks visible, bright outdoor natural light, editorial photo quality"),
        "modeling": ("modeling-rocks.png", "A colorful kid-friendly scientific diagram showing three rock layers stacked on top of each other — a sandy river layer on top, a dark volcanic layer in the middle, a fossil-filled layer on the bottom — cartoon-style, white background, bold outlines, labels with time arrows"),
        "discussion": ("discussion-rocks.png", "A teacher with diverse 2nd graders (7-8 years old, wide variety of ethnicities) gathered around a table with different rock samples, teacher holding a layered rock, students examining samples, bright classroom"),
        "stem": ("stem-rocks.png", "Diverse 2nd graders (7-8 years old, wide mix of ethnicities) building rock layer models in clear cups using sand, gravel, clay, and pebbles, layering materials carefully, excited collaborative group work")
    },
    "pre_assessment": [
        "Have you ever picked up a rock and wondered how it got there? What did you notice about it?",
        "Do you think all rocks are the same or are there different kinds? How are they different?",
        "Draw what you think is inside a mountain — what would you see if you cut it in half?"
    ],
    "reflections": [
        "How is reading rock layers similar to reading pages in a book?",
        "What is one thing a rock at your school could tell you about the past?"
    ],
    "reflection_exemplars": [
        ("How is reading rock layers similar to reading pages in a book?", "Rock layers are like pages in a history book about Earth. The bottom layer is the oldest, just like the first page of a book tells the beginning of the story. Each layer on top was made later, telling the next part of the story. By reading the layers from bottom to top, scientists can figure out what happened on Earth in order — first this, then this, then this — just like reading a book from the first page to the last.")
    ],
    "cast_items": [
        "Describe how different Earth events create different types of rocks",
        "Explain how rock layers show what happened on Earth in the past",
        "Compare a fast Earth event (volcano) to a slow Earth event (erosion)"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A scientist finds smooth, round rocks at the bottom of a valley. What Earth event most likely shaped these rocks?"),
        ("Constructed Response:", "Explain how rock layers help scientists figure out what happened on Earth long ago. How can you tell which layer is the oldest?")
    ],
    "extend_components": [
        ("Fossils in Layers", "Remains of ancient plants and animals found inside rock layers — they tell us what was alive at the time that layer formed"),
        ("Weathering Speed", "How fast the rock breaks down from weather — soft rock erodes quickly, hard rock lasts a long time")
    ],
    "dimensions": [
        ("Science Practice", "Obtaining, Evaluating, and Communicating Information", "Students use information from rocks and layers to provide evidence about Earth events and whether they occurred quickly or slowly."),
        ("Disciplinary Core Idea", "ESS1.C The History of Planet Earth", "Some events happen very quickly; others occur very slowly, over a time period much longer than one can observe. Rock layers and fossils provide evidence about Earth's history."),
        ("Crosscutting Concept", "Stability and Change", "Students explore how some Earth processes are slow and steady (erosion) while others are sudden and dramatic (volcanic eruptions), and how both leave evidence in rocks.")
    ],
    "background_intro": "Rocks are the oldest storytellers on Earth. Long before humans existed, rocks were being formed, broken down, and reformed — creating a record of Earth's history that scientists can read like a book.",
    "background_sections": [
        ("Rocks Tell Stories", "Every rock has a story about how it formed. Igneous rocks formed from hot melted rock (lava or magma) that cooled and hardened — often from volcanic eruptions. Sedimentary rocks formed when tiny pieces of rock, sand, and dirt (called sediment) settled in layers and were pressed together over millions of years. Metamorphic rocks formed when existing rocks were changed by heat and pressure deep underground. Each type gives us clues about what happened in the past."),
        ("Reading Rock Layers", "When sediment settles, it forms layers — like pancakes stacking up over time. The bottom layer is the oldest because it was deposited first. Each new layer on top is younger. Scientists called geologists read these layers like chapters in a history book. Different colored or textured layers show different time periods and different events. A dark layer might be from a volcanic eruption. A sandy layer might be from an ancient beach."),
        ("Fast and Slow Earth Events", "Some Earth events happen in seconds or minutes — earthquakes shake the ground, volcanoes erupt with explosive force, and landslides send rock tumbling down mountains. Other events take thousands or millions of years — rivers slowly carve canyons, wind gradually sculpts rock formations, and sediment builds up one grain at a time. Both fast and slow events leave evidence in rocks that scientists can study today.")
    ],
    "lever_L": "Students identify Earth event as an external component and rock type and rock layer pattern as internal components that form differently depending on what event occurred.",
    "lever_E": "Students determine that different Earth events produce different rock types — slow events create smooth layered rocks, while fast events create rough textured rocks.",
    "lever_V": "Students build a model showing how different Earth events (river, volcano, wind) create different rock types and layer patterns.",
    "lever_Ev": "Students run slow river, fast volcano, and slow wind scenarios to compare the rock types and layers each event produces.",
    "lever_R": "Students add fossils in layers or weathering speed to explore more of what rock layers can tell us about the past.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with colorful rock layers", "say": "What if I told you that rocks can tell STORIES? Not with words — but with clues hidden inside them!", "do": "Pass around 2-3 different rocks (smooth river rock, rough volcanic rock, layered sedimentary rock). Ask: How are these different?", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn Today?", "visual": "Learning goals and vocabulary", "say": "Today we are going to learn to read rocks like books — each one tells a story about Earth's past!", "do": "Read objectives together. Introduce rock layer, erosion, and sediment with real examples.", "time": "3 min"},
        {"num": "Slide 3", "title": "The Big Question", "visual": "How do rocks tell stories?", "say": "These rocks are millions of years old. They were here before people, before cities, even before most animals! What stories are they hiding?", "do": "Show a photo of the Grand Canyon. Ask: Do you see the layers? Each layer is a different chapter in Earth's story.", "time": "3 min"},
        {"num": "Slide 4", "title": "Let's Build a Model!", "visual": "LEVER steps overview", "say": "We are going to build a model to understand how different events on Earth create different rocks.", "do": "Preview LEVER steps. Demo: shake a jar of water with sand and gravel — watch the layers settle. That is how sediment works!", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Sort the Parts", "visual": "Component cards: Earth Event, Rock Type, Rock Layer Pattern", "say": "What are the parts of our rock story system? An Earth event happens. Then a certain type of rock forms. Then we see it in the layers.", "do": "Guide sorting: Earth Event is external (nature does it). Rock Type and Rock Layer Pattern are internal (they result from the event).", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect with Arrows", "visual": "Arrows between components", "say": "When a volcano erupts, does it make the same kind of rock as a gentle river? Let us connect our parts!", "do": "Draw arrows from Earth Event to Rock Type and Rock Layer Pattern. Discuss how volcanoes and rivers make DIFFERENT rocks.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Run the Simulation!", "visual": "Simulation predictions and results", "say": "Let us test a slow river and a fast volcano! What kind of rock does each one make?", "do": "Students predict, then run simulations. Compare smooth river rocks to rough volcanic rocks. Discuss fast vs. slow events.", "time": "8 min"},
        {"num": "Slide 8", "title": "What Did We Discover?", "visual": "Key discoveries about rock stories", "say": "Now you can read rocks! Smooth rocks tell slow stories. Rough rocks tell fast, exciting stories. And rock layers are like chapters in Earth's history book!", "do": "Each student gets a rock sample and writes one sentence about what story it might tell. Share with a partner.", "time": "7 min"}
    ],
    "sort_reasoning": "Earth Event is external because natural events like volcanoes, rivers, and wind happen whether or not we observe them — they are forces that act on the rock. Rock Type and Rock Layer Pattern are internal because they are the RESULTS of those events — the rock and layers form in response to what happened.",
    "relationships": [
        ("Earth Event (slow) to Rock Type", "POSITIVE (+)", "Slow, gentle Earth events like rivers flowing for millions of years create smooth, layered sedimentary rocks. The longer and gentler the event, the smoother and more organized the rock layers become."),
        ("Earth Event (fast) to Rock Type", "POSITIVE (+)", "Fast, powerful Earth events like volcanic eruptions create rough, bubbly igneous rocks. The hotter and faster the event, the more dramatic and textured the resulting rock.")
    ],
    "sim_answers": [
        ("Slow River", "When Earth Event is a slow-flowing river, Rock Type is smooth and rounded because water wore down the rough edges over a very long time. Rock Layer Pattern shows thin, even layers of sediment that settled gently on the river bottom. This tells us a calm, slow process happened over thousands or millions of years."),
        ("Fast Volcano", "When Earth Event is a volcanic eruption, Rock Type is rough, dark, and bubbly because hot lava cooled very quickly. Rock Layer Pattern shows a thick, uneven dark layer that interrupts the other layers. This tells us something fast and dramatic happened — a sudden eruption that changed the landscape instantly.")
    ],
    "stem_intro": "Present the challenge: A museum needs a display showing how rock layers record Earth's history. Your team will build a model with at least three layers, each representing a different Earth event, to help visitors understand how scientists read rocks like history books.",
    "stem_concepts": [
        ("Layers Are Time", "Each layer of rock represents a different time period. The bottom layer formed first and is oldest. The top layer formed most recently and is youngest. Your model should clearly show this bottom-to-top timeline."),
        ("Different Events, Different Rocks", "Each Earth event creates a different kind of rock. River sediment creates smooth sandy layers. Volcanic eruptions create dark rough layers. Wind-blown sand creates fine even layers. Each layer in your model should look different."),
        ("Reading the Evidence", "Scientists look at rock layers and figure out what happened — just like reading a mystery novel. Your museum exhibit should teach visitors how to read the evidence in the layers.")
    ],
    "stem_eval": [
        ("Expert (4)", "Rock layer model has 3+ distinct layers representing different events, is correctly ordered oldest-to-newest, and student explains each layer's story"),
        ("Proficient (3)", "Model has 3 layers in correct order and student can explain what event each layer represents"),
        ("Developing (2)", "Model has layers but student struggles to explain the connection between events and rock types"),
        ("Beginning (1)", "Model is incomplete or layers are not connected to Earth events")
    ],
    "support": [
        "Provide clear cups and pre-sorted materials (sand, gravel, clay, pebbles) for easy layering",
        "Use a labeled example model so students can see what a finished rock layer timeline looks like",
        "Sentence frame: 'The bottom layer is ___ because it formed when ___ and it is the ___ (oldest/newest)'"
    ],
    "extensions": [
        "Collect rocks from the school yard and try to identify whether each was formed by water, wind, or heat",
        "Research the Grand Canyon — how many layers does it have and what stories do they tell?",
        "Create a timeline of Earth events from oldest to newest using rock layer evidence"
    ],
    "cross_curr": [
        ("Math", "Stack layers in a clear cup and measure the height of each layer in centimeters — which event left the thickest layer?"),
        ("ELA", "Write a short story from the perspective of a rock layer — describe the Earth event that created you and what you have seen over millions of years"),
        ("Art", "Paint a cross-section of a canyon wall showing colorful rock layers, label each layer with the Earth event that formed it")
    ],
    "misconceptions": [
        ("All rocks are the same", "Rocks are incredibly different from each other! Smooth river rocks, rough volcanic rocks, sparkly mineral rocks, and layered sedimentary rocks all formed in completely different ways. The type of rock tells us what Earth event created it — like a clue about the past.", "Show three very different rocks. Ask: Are these the same? Feel them, look at them closely. What is different? Each one has a different story."),
        ("Rocks have always been there and never change", "Rocks are constantly being created and destroyed! Volcanoes make new rock from lava. Rivers slowly wear rock down into sand. Sand gets pressed into new rock over millions of years. Rocks are always changing — it just happens so slowly we usually cannot see it.", "Put a piece of chalk in a cup of vinegar. Watch it dissolve slowly. Ask: Is the rock changing? This is what water does to rock over millions of years, just much slower."),
        ("The top layer of rock is the oldest", "Actually, the BOTTOM layer is the oldest! Layers build up from the bottom, one on top of another. The bottom layer was there first. Each new layer settles on top. So if you dig down into the Earth, you are going BACK in time. The deepest rocks tell the oldest stories.", "Stack three colored layers of sand in a clear cup, one at a time. Ask after each: Which layer is the oldest? The one we put in first — on the bottom!")
    ]
}

ALL_LESSONS = [L01, L02, L03, L04, L05, L06, L07, L08, L09, L10]
