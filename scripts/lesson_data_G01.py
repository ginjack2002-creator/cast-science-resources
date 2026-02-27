#!/usr/bin/env python3
"""Complete lesson data for G01-L01 through G01-L10 (Grade 1 ModelIt! Lessons)"""

L01 = {
    "id": "G01-L01",
    "title": "How Does Sound Travel?",
    "subtitle": "The Science of Vibrations and Sound Waves",
    "ngss": "1-PS4-1",
    "ngss_desc": "Plan and conduct investigations to provide evidence that vibrating materials can make sound and that sound can make materials vibrate.",
    "big_question": "How does sound get from one place to another?",
    "objectives": [
        "Show that vibrations make sound",
        "Explain how sound moves through the air to our ears",
        "Describe what happens when sound hits different objects"
    ],
    "vocabulary": [
        ("Vibration", "A very fast back-and-forth movement that makes sound"),
        ("Sound Wave", "The way sound moves through the air, like ripples in water")
    ],
    "components": [
        ("Vibration Strength", "How hard something shakes back and forth — like tapping a drum softly or hard", True),
        ("Sound Volume", "How loud or soft the sound is when it reaches your ears", False)
    ],
    "think_about_it": "When you tap a drum harder, does the sound get louder or softer?",
    "scenarios": [
        ("Soft Tap", "Set Vibration Strength to low and listen to the Sound Volume"),
        ("Hard Tap", "Set Vibration Strength to high and listen to how the Sound Volume changes")
    ],
    "sim_scenarios": [
        ("Soft Tap", "Vibration Strength set to low", "What do you predict will happen to Sound Volume when you tap softly?"),
        ("Hard Tap", "Vibration Strength set to high", "What do you predict will happen to Sound Volume when you tap really hard?")
    ],
    "discoveries": [
        "Bigger vibrations make louder sounds",
        "Sound travels through the air from the thing that vibrates to your ears",
        "You can feel vibrations if you touch something that is making sound"
    ],
    "answer": "Sound travels through the air as vibrations! When something shakes back and forth really fast, it pushes the air around it. Those air pushes travel like ripples in a pond until they reach your ears. Bigger shakes make louder sounds, and smaller shakes make softer sounds.",
    "stem_title": "Build a Musical Instrument",
    "stem_mission": "Design and build a simple instrument that can make both loud and soft sounds using vibrations.",
    "stem_scenario": "Your class is putting on a music show! You need to build an instrument from everyday materials that can play loud sounds AND soft sounds. Use what you learned about vibrations to make your instrument work.",
    "stem_questions": [
        "How can you make your instrument vibrate to create sound?",
        "What can you change to make the sound louder or softer?"
    ],
    "stem_design_qs": [
        "What materials will you use to make something vibrate?",
        "How will you make a loud sound with your instrument?",
        "How will you make a soft sound with your instrument?",
        "Can you feel the vibrations when your instrument makes sound?"
    ],
    "career": "Sound Engineers help record music and make movies sound amazing. They use science to control vibrations and sound waves. They earn $35,000-$80,000/year.",
    "images": {
        "cover": ("cover-sound.png", "A colorful, close-up visualization of sound waves rippling outward from a vibrating drum, bright colors against a clean background, cinematic and kid-friendly"),
        "landscape": ("landscape-sound.png", "Diverse 1st grade students (6-7 years old, wide variety of ethnicities including Black, Latino, Asian, and white children) excitedly exploring musical instruments in a bright modern classroom, natural window light, editorial photo quality"),
        "modeling": ("modeling-sound.png", "A simple, colorful kid-friendly diagram showing sound waves traveling from a drum to an ear, with wavy lines representing vibrations, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-sound.png", "A teacher with diverse 1st graders (6-7 years old, wide variety of ethnicities) sitting in a circle on a colorful rug, touching a vibrating tuning fork, bright classroom with science posters"),
        "stem": ("stem-sound.png", "Diverse 1st graders (6-7 years old, wide mix of ethnicities) building simple instruments from rubber bands, boxes, and cups at their desks, excited expressions, modern classroom")
    },
    "pre_assessment": [
        "Draw a picture of something that makes sound. Show how the sound gets to your ears.",
        "Circle the things that vibrate: a ringing bell, a rock sitting still, a guitar string being plucked, a sleeping cat."
    ],
    "dimensions": [
        ("Science Practice", "Planning and Carrying Out Investigations", "Students investigate how changing vibration strength affects the loudness of sound."),
        ("Disciplinary Core Idea", "PS4.A Wave Properties", "Sound can make matter vibrate, and vibrating matter can make sound."),
        ("Crosscutting Concept", "Cause and Effect", "Students explore how stronger vibrations cause louder sounds.")
    ],
    "background_intro": "Sound is all around us every day. From birds singing to cars honking, all sounds are made by vibrations — things shaking back and forth very quickly.",
    "background_sections": [
        ("What Makes Sound?", "Every sound starts with a vibration. When you pluck a guitar string, it shakes back and forth very fast. When you hit a drum, the drum skin vibrates. These vibrations push the air around them, creating invisible waves that travel outward in all directions, like ripples when you drop a stone in water. When these air waves reach our ears, tiny parts inside our ears vibrate too, and our brain understands it as sound."),
        ("Loud and Soft Sounds", "The strength of a vibration determines how loud a sound is. When you tap a drum gently, it vibrates a little and makes a soft sound. When you hit it hard, it vibrates a lot and makes a loud sound. Scientists call the size of a vibration its amplitude. Big amplitude means loud sound, and small amplitude means soft sound. Sound can travel through air, water, and even solid objects like walls and tables.")
    ],
    "lever_L": "Students identify vibration strength as something we can control (external) and sound volume as something that changes in response (internal).",
    "lever_E": "Students figure out that when vibration strength goes up, sound volume also goes up — a positive relationship.",
    "lever_V": "Students build a simple model with two parts showing how vibration strength connects to sound volume.",
    "lever_Ev": "Students test their model by trying soft taps and hard taps and observing how the sound changes.",
    "lever_R": "Students reflect on how their model matches what happens when they play real instruments or clap their hands.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with colorful sound wave image", "say": "Today we are going to explore something invisible but very powerful — SOUND! Can everyone clap their hands? You just made sound!", "do": "Have students clap, snap, and stomp to make different sounds. Ask: How are we making these sounds?", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn?", "visual": "Learning goals with picture icons", "say": "We are going to find out how sound travels from one place to another. We will learn a new word: vibration!", "do": "Introduce the word vibration. Have students place their hand on their throat and hum to feel vibrations.", "time": "3 min"},
        {"num": "Slide 3", "title": "Let's Be Scientists!", "visual": "Big question with question mark graphic", "say": "Here is our big question: How does sound get from one place to another? What do you think?", "do": "Give students 30 seconds to think, then share with a partner. Collect a few ideas from the class.", "time": "3 min"},
        {"num": "Slide 4", "title": "What Are the Parts?", "visual": "Two component cards with pictures", "say": "Our model has two parts: Vibration Strength is how hard something shakes. Sound Volume is how loud the sound is.", "do": "Hold up a drum or rubber band. Show a gentle pluck vs. a strong pluck. Ask: Which one can we control?", "time": "5 min"},
        {"num": "Slide 5", "title": "How Are They Connected?", "visual": "Arrow connecting the two components", "say": "When vibration strength goes UP, what happens to the sound? Does it get louder or softer?", "do": "Students use sentence frame: When vibration strength goes up, sound volume goes up. Draw the arrow together.", "time": "5 min"},
        {"num": "Slide 6", "title": "What Did We Find Out?", "visual": "Key discoveries with simple icons", "say": "We found out that bigger vibrations make louder sounds! Sound is just vibrations traveling through the air.", "do": "Review discoveries. Sprinkle rice on a drum and tap it so students can SEE the vibrations.", "time": "5 min"},
        {"num": "Slide 7", "title": "STEM Challenge", "visual": "Musical instrument building challenge", "say": "Now it is YOUR turn to build an instrument! Can you make something that plays loud AND soft sounds?", "do": "Distribute materials (rubber bands, cups, boxes, paper towel tubes). Students build and test instruments.", "time": "10 min"}
    ],
    "sort_reasoning": "Vibration Strength is external because we control how hard we tap, pluck, or hit something. Sound Volume is internal because it changes as a result of how strong the vibration is.",
    "relationships": [
        ("Vibration Strength to Sound Volume", "POSITIVE (+)", "When you make stronger vibrations by tapping harder, the sound gets louder. Bigger shakes make bigger sounds.")
    ],
    "sim_answers": [
        ("Soft Tap", "When Vibration Strength is set to low, Sound Volume is quiet. The drum barely shakes, so the air barely moves, and the sound is very soft."),
        ("Hard Tap", "When Vibration Strength is set to high, Sound Volume is loud. The drum shakes a lot, pushing the air hard, and the sound is much louder.")
    ],
    "stem_intro": "Present the challenge: Your class is putting on a music show! You need to build an instrument from everyday materials. It must be able to make both loud and soft sounds. Think about what you learned — vibrations make sound!",
    "stem_concepts": [
        ("Vibrations Make Sound", "Every sound starts with something shaking. Your instrument needs a part that vibrates — like a rubber band stretched over a box or a paper plate you can tap."),
        ("Control the Volume", "To make loud sounds, you need big vibrations. To make soft sounds, you need small vibrations. Think about how to tap, pluck, or shake your instrument differently.")
    ],
    "stem_eval": [
        ("Expert (4)", "Instrument makes both loud and soft sounds and student explains that bigger vibrations make louder sounds"),
        ("Proficient (3)", "Instrument makes sound and student can describe that vibrations are involved"),
        ("Developing (2)", "Instrument makes sound but student has trouble explaining why it is loud or soft"),
        ("Beginning (1)", "Student needs help building an instrument or explaining how sound works")
    ],
    "support": [
        "Provide a pre-made rubber band guitar for students who need a model to copy",
        "Use hand-over-hand guidance to help students feel vibrations on instruments",
        "Sentence frame: When I tap harder, the sound gets _______ because the vibration is _______."
    ],
    "extensions": [
        "Try putting your instrument in a box — does the sound change? Why?",
        "Can you make your instrument play a high sound and a low sound? What did you change?",
        "Put rice on a drum and watch it jump when you tap — draw what you see"
    ],
    "cross_curr": [
        ("Math", "Count and compare how many taps it takes to make 5 loud sounds and 5 soft sounds"),
        ("ELA", "Draw and label your instrument, then tell a partner how it makes sound using the word vibration"),
        ("Art", "Decorate your instrument and draw the sound waves coming out of it")
    ],
    "misconceptions": [
        ("Sound just happens by itself", "Sound never happens without a vibration. Something always has to shake or move back and forth to make sound. Even your voice comes from tiny parts in your throat vibrating!", "Have students touch their throat while humming — they can feel the vibrations that make their voice."),
        ("Sound only travels through air", "Sound can travel through solids and liquids too! Put your ear on a table and have a friend tap the other end — you can hear it through the wood. Whales sing to each other through water.", "Tap on a desk and have students listen with their ear pressed to the surface. Ask: Could you hear it? The sound traveled through the table!")
    ],
    "sentence_frame": "When vibration strength goes up, sound volume goes up.",
    "coloring_description": "A big drum with wavy sound lines coming out of it, reaching a happy child's ear. The sound waves get smaller as they travel farther from the drum."
}

L02 = {
    "id": "G01-L02",
    "title": "Why Can We See Through Some Things?",
    "subtitle": "The Science of Light and Materials",
    "ngss": "1-PS4-3",
    "ngss_desc": "Plan and conduct investigations to determine the effect of placing objects made with different materials in the path of a beam of light.",
    "big_question": "Why can you see through a window but not through a wall?",
    "objectives": [
        "Sort materials into groups based on how much light passes through them",
        "Explain why some things are see-through and some are not",
        "Predict what will happen when light hits different materials"
    ],
    "vocabulary": [
        ("Transparent", "Something you can see through clearly, like a window or clear water"),
        ("Opaque", "Something you cannot see through at all, like a wall or a book"),
        ("Translucent", "Something that lets some light through but is blurry, like frosted glass")
    ],
    "components": [
        ("Material Type", "What kind of material the light hits — clear, frosted, or solid", True),
        ("Light Passing Through", "How much light gets through the material to the other side", False)
    ],
    "think_about_it": "When you shine a flashlight through a clear cup, does more light or less light get through compared to a paper cup?",
    "scenarios": [
        ("Clear Plastic Cup", "Set Material Type to transparent and observe how much Light Passes Through"),
        ("Cardboard Cup", "Set Material Type to opaque and observe how much Light Passes Through")
    ],
    "sim_scenarios": [
        ("Clear Plastic Cup", "Material Type set to transparent", "What do you predict will happen to the light when it hits a clear cup?"),
        ("Cardboard Cup", "Material Type set to opaque", "What do you predict will happen to the light when it hits a cardboard cup?")
    ],
    "discoveries": [
        "Transparent materials let almost all light pass through so you can see clearly",
        "Opaque materials block all the light so you cannot see through them",
        "Translucent materials let some light through but things look blurry",
        "The type of material decides how much light gets through"
    ],
    "answer": "You can see through a window because glass is transparent — it lets almost all the light pass right through! A wall is opaque — it blocks all the light so nothing gets through. Some things, like wax paper, are translucent — they let some light through but make things look blurry. The material something is made of decides how much light can travel through it.",
    "stem_title": "Design a Flashlight Viewer",
    "stem_mission": "Build a tube viewer that uses different materials to change how much light gets through, like a fun light filter.",
    "stem_scenario": "A toy company wants you to design a cool flashlight viewer! When you look through it, you should be able to change what you see by switching the material on the end. Use what you learned about transparent, translucent, and opaque materials.",
    "stem_questions": [
        "Which material should you use if you want to see clearly through your viewer?",
        "What happens when you put wax paper on the end instead of clear plastic?"
    ],
    "stem_design_qs": [
        "What will you use for the tube part of your viewer?",
        "What three different materials will you test on the end?",
        "How will you attach the materials so you can switch them?",
        "Which material lets you see the most? Which lets you see the least?"
    ],
    "career": "Window Designers and Architects choose the right materials so buildings let in the perfect amount of light. They earn $50,000-$90,000/year.",
    "images": {
        "cover": ("cover-light-materials.png", "A beam of bright light passing through a prism creating colorful light rays, clean bright background, cinematic and kid-friendly"),
        "landscape": ("landscape-light-materials.png", "Diverse 1st grade students (6-7 years old, wide variety of ethnicities including Black, Latino, Asian, and white children) shining flashlights through different materials in a bright modern classroom, natural window light, editorial photo quality"),
        "modeling": ("modeling-light-materials.png", "A simple, colorful kid-friendly diagram showing light passing through three materials: clear glass, frosted glass, and a solid wall, with arrows showing light going through or being blocked, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-light-materials.png", "A teacher with diverse 1st graders (6-7 years old, wide variety of ethnicities) gathered around a table with a flashlight and various materials like plastic wrap, wax paper, and cardboard, bright classroom"),
        "stem": ("stem-light-materials.png", "Diverse 1st graders (6-7 years old, wide mix of ethnicities) building tube viewers from paper towel rolls with different materials taped to the ends, flashlights on their desks, excited expressions")
    },
    "pre_assessment": [
        "Draw something you can see through and something you cannot see through.",
        "Circle the things that light can pass through: a window, a brick wall, a clear water bottle, a book, plastic wrap."
    ],
    "dimensions": [
        ("Science Practice", "Planning and Carrying Out Investigations", "Students investigate how different materials affect the amount of light that passes through them."),
        ("Disciplinary Core Idea", "PS4.B Electromagnetic Radiation", "Some materials allow light to pass through them, others allow only some light through, and others block all the light."),
        ("Crosscutting Concept", "Cause and Effect", "Students explore how the type of material causes different amounts of light to pass through.")
    ],
    "background_intro": "Light is a form of energy that travels in straight lines. When light hits different materials, different things happen — and that is why we can see through some things but not others.",
    "background_sections": [
        ("Three Kinds of Materials", "Scientists sort materials into three groups based on how they interact with light. Transparent materials like clear glass and plastic wrap let almost all light pass through — that is why windows are made of glass! Opaque materials like wood, metal, and cardboard block all the light — you cannot see through a door. Translucent materials like frosted glass, wax paper, and thin fabric let some light through but scatter it, making things look blurry."),
        ("Why It Matters", "Understanding how light passes through materials helps people make important choices every day. Builders choose glass for windows so sunlight can brighten rooms. Sunglasses are made with special translucent lenses that block some light to protect our eyes. Privacy screens on bathrooms use frosted glass that lets in light but keeps things private. Even the clothes we wear are chosen partly based on how much light they let through!")
    ],
    "lever_L": "Students identify material type as something we choose (external) and light passing through as something that changes depending on the material (internal).",
    "lever_E": "Students figure out that transparent materials let the most light through, opaque materials block all light, and translucent materials are in between.",
    "lever_V": "Students build a simple model showing how the type of material affects how much light passes through.",
    "lever_Ev": "Students test their model by shining a flashlight through different materials and recording what they observe.",
    "lever_R": "Students reflect on how their model helps explain everyday things like why windows are glass and walls are wood.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with light beams and colorful materials", "say": "Look around the room. Can you find something you can see through? Can you find something you cannot see through? Today we find out WHY!", "do": "Have students point to things in the room that are see-through and not see-through. Make a quick list.", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn?", "visual": "Learning goals with picture icons", "say": "We are going to learn three big words today: transparent, translucent, and opaque. These words tell us how much light goes through things.", "do": "Teach the three words with hand motions: transparent = hands open wide, translucent = hands halfway, opaque = hands blocking.", "time": "3 min"},
        {"num": "Slide 3", "title": "Let's Be Scientists!", "visual": "Big question with flashlight graphic", "say": "Why can you see through a window but not through a wall? What do you think is different about them?", "do": "Think-pair-share. Students whisper their idea to a partner, then share with the class.", "time": "3 min"},
        {"num": "Slide 4", "title": "What Are the Parts?", "visual": "Two component cards with pictures of materials and light", "say": "Our model has two parts: Material Type is what the thing is made of. Light Passing Through is how much light gets to the other side.", "do": "Show three materials: clear plastic, wax paper, cardboard. Ask: Which one do you think lets the most light through?", "time": "5 min"},
        {"num": "Slide 5", "title": "How Are They Connected?", "visual": "Sorting chart with three categories", "say": "Different materials do different things to light. Let us sort them! Transparent lets all light through, opaque blocks it, translucent lets some through.", "do": "Students sort material samples into three groups. Use sentence frame: This material is _______ because light _______.", "time": "5 min"},
        {"num": "Slide 6", "title": "What Did We Find Out?", "visual": "Key discoveries with material examples", "say": "We discovered that the type of material decides how much light gets through. That is why windows are made of glass!", "do": "Review discoveries. Shine a flashlight through each material type one more time to reinforce.", "time": "5 min"},
        {"num": "Slide 7", "title": "STEM Challenge", "visual": "Flashlight viewer building challenge", "say": "Now you get to build a flashlight viewer! You will put different materials on the end and see how your view changes.", "do": "Distribute paper towel tubes, plastic wrap, wax paper, cardboard circles, tape, and flashlights. Students build and test.", "time": "10 min"}
    ],
    "sort_reasoning": "Material Type is external because we choose what material to test — we pick up the clear cup or the cardboard cup. Light Passing Through is internal because it changes depending on which material we chose.",
    "relationships": [
        ("Material Type to Light Passing Through", "POSITIVE (+)", "More transparent materials let more light pass through. When the material is clearer, more light gets to the other side.")
    ],
    "sim_answers": [
        ("Clear Plastic Cup", "When Material Type is set to transparent, Light Passing Through is very high. You can see clearly through the cup because the clear plastic lets almost all the light go right through."),
        ("Cardboard Cup", "When Material Type is set to opaque, Light Passing Through is zero. You cannot see through the cardboard at all because it blocks all the light.")
    ],
    "stem_intro": "Present the challenge: A toy company wants you to design a flashlight viewer. You will test different materials on the end of a tube to see how they change what you can see. Use what you learned about transparent, translucent, and opaque materials!",
    "stem_concepts": [
        ("Materials Control Light", "Different materials let different amounts of light through. Clear plastic lets all light through. Wax paper lets some through. Cardboard blocks it all."),
        ("Choosing the Right Material", "When you want to see clearly, use transparent materials. When you want privacy or darkness, use opaque materials. Translucent materials give you something in between.")
    ],
    "stem_eval": [
        ("Expert (4)", "Viewer uses all three material types and student correctly names them as transparent, translucent, and opaque"),
        ("Proficient (3)", "Viewer works with at least two materials and student can explain why one lets more light through"),
        ("Developing (2)", "Viewer is built but student has trouble using the vocabulary words to explain differences"),
        ("Beginning (1)", "Student needs help building the viewer or sorting materials by how much light passes through")
    ],
    "support": [
        "Pre-label materials with picture icons showing transparent, translucent, and opaque",
        "Use a strong flashlight so the difference between materials is very obvious",
        "Sentence frame: _______ is transparent/translucent/opaque because light _______."
    ],
    "extensions": [
        "Can you find five things in the classroom that are transparent, translucent, or opaque? Make a chart!",
        "What happens if you stack two translucent materials together? Does it become opaque?",
        "Go on a light walk around the school — sort things you see into the three categories"
    ],
    "cross_curr": [
        ("Math", "Count how many transparent, translucent, and opaque items you found and make a bar graph"),
        ("ELA", "Write a sentence about each material type using the words transparent, translucent, and opaque"),
        ("Art", "Make a collage using transparent, translucent, and opaque materials layered on top of each other")
    ],
    "misconceptions": [
        ("Light goes through everything a little bit", "Some materials block ALL light completely. These are called opaque. No light at all passes through a thick wall or a piece of cardboard, which is why you cannot see through them.", "Shine a flashlight at cardboard in a dark room. Ask: Can you see ANY light on the other side? No — that is what opaque means!"),
        ("Clear things have holes in them that light goes through", "Transparent materials do not have tiny holes. The material itself lets light energy pass through it. Glass is completely solid with no holes, but light can still travel through it because of how the material is made.", "Let students feel a piece of clear glass or plastic — it is smooth and solid with no holes, but light still goes through!")
    ],
    "sentence_frame": "When the material is more clear, the light passing through goes up.",
    "coloring_description": "A flashlight shining a beam of light at three objects in a row: a clear window (light goes through), a piece of wax paper (some light goes through with wavy lines), and a brick wall (light is blocked with an X)."
}

L03 = {
    "id": "G01-L03",
    "title": "How Do Baby Animals Look Like Their Parents?",
    "subtitle": "The Science of Inherited Traits",
    "ngss": "1-LS3-1",
    "ngss_desc": "Make observations to construct an evidence-based account that young plants and animals are like, but not exactly like, their parents.",
    "big_question": "Why do baby animals look like their parents but not exactly the same?",
    "objectives": [
        "Observe that baby animals have features similar to their parents",
        "Identify ways that baby animals are different from their parents",
        "Explain that parents pass traits to their babies"
    ],
    "vocabulary": [
        ("Trait", "A feature or body part that an animal has, like fur color, eye shape, or ear size"),
        ("Inherited", "Something you get from your parents, like the color of your hair or eyes")
    ],
    "components": [
        ("Parent Traits", "The features that the mom and dad animal have, like fur color and pattern", True),
        ("Baby Traits", "The features that the baby animal gets, which are similar but not exactly the same", False)
    ],
    "think_about_it": "When a parent dog has spots, do you think the puppies will have spots too?",
    "scenarios": [
        ("Spotted Parent", "Set Parent Traits to spotted fur and observe what Baby Traits look like"),
        ("Striped Parent", "Set Parent Traits to striped fur and observe what Baby Traits look like")
    ],
    "sim_scenarios": [
        ("Spotted Parent", "Parent Traits set to spotted fur", "What do you predict the baby will look like when the parent has spots?"),
        ("Striped Parent", "Parent Traits set to striped fur", "What do you predict the baby will look like when the parent has stripes?")
    ],
    "discoveries": [
        "Baby animals look a lot like their parents because traits are inherited",
        "Baby animals are not EXACTLY like their parents — there are always small differences",
        "Traits like fur color, ear shape, and body size are passed from parents to babies"
    ],
    "answer": "Baby animals look like their parents because they inherit traits from them! A kitten gets its fur color, ear shape, and body type from its mom and dad cat. But babies are never exact copies — they always have small differences. A puppy might have the same spots as its dad but in slightly different places. This is how traits are passed from one generation to the next.",
    "stem_title": "Design a Baby Animal",
    "stem_mission": "Draw a baby animal based on the traits of two parent animals and explain which traits came from which parent.",
    "stem_scenario": "A zoo needs your help! Two parent animals just had a baby and the zookeepers need to know what the baby might look like. Look at the parent traits and draw what you think the baby will look like. Explain your thinking!",
    "stem_questions": [
        "Which traits do you think the baby will get from each parent?",
        "Will the baby look exactly like one parent or be a mix of both?"
    ],
    "stem_design_qs": [
        "What color will the baby animal be?",
        "What size ears will it have — big like one parent or small like the other?",
        "Will the baby have spots, stripes, or solid color?",
        "How is the baby different from both parents?"
    ],
    "career": "Zoologists study animals and their babies to learn how traits are passed along. They work at zoos, wildlife parks, and research centers. They earn $45,000-$75,000/year.",
    "images": {
        "cover": ("cover-baby-animals.png", "A heartwarming photorealistic image of a mother dog with her puppies, showing similar fur patterns and colors, warm lighting, shallow depth of field"),
        "landscape": ("landscape-baby-animals.png", "Diverse 1st grade students (6-7 years old, wide variety of ethnicities including Black, Latino, Asian, and white children) looking at photos of animal families on a smartboard, bright modern classroom, natural window light, editorial photo quality"),
        "modeling": ("modeling-baby-animals.png", "A simple, colorful kid-friendly diagram showing a parent cat with spotted fur connected by arrows to a kitten with similar but slightly different spots, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-baby-animals.png", "A teacher with diverse 1st graders (6-7 years old, wide variety of ethnicities) comparing photos of parent and baby animals on a table, students pointing and talking excitedly, bright classroom"),
        "stem": ("stem-baby-animals.png", "Diverse 1st graders (6-7 years old, wide mix of ethnicities) drawing baby animals with crayons at their desks, looking at pictures of parent animals for reference, colorful modern classroom")
    },
    "pre_assessment": [
        "Draw a baby cat next to its parent cat. How are they alike? How are they different?",
        "Circle the baby that matches its parent: show pictures of a brown dog with three puppies of different colors."
    ],
    "dimensions": [
        ("Science Practice", "Constructing Explanations", "Students use observations of parent and baby animals to explain how traits are inherited."),
        ("Disciplinary Core Idea", "LS3.A Inheritance of Traits", "Young animals are very much, but not exactly, like their parents. Plants also are very much, but not exactly, like their parents."),
        ("Crosscutting Concept", "Patterns", "Students observe patterns of similarity between parents and their offspring.")
    ],
    "background_intro": "Every baby animal in the world looks something like its parents. This is because parents pass special information to their babies that controls what they look like.",
    "background_sections": [
        ("What Are Traits?", "A trait is any feature of a living thing. Fur color, eye color, ear shape, body size, tail length — these are all traits. Animals inherit most of their traits from their parents. That is why puppies look like dogs and kittens look like cats. The information for these traits is passed from parents to babies before the baby is even born."),
        ("Similar But Not the Same", "Even though baby animals look like their parents, they are never exact copies. A litter of kittens from the same parents can have different fur colors and patterns. Some might have long tails and others shorter ones. This variation is completely normal and is what makes each animal unique. The differences come from the way parent traits mix together in new combinations.")
    ],
    "lever_L": "Students identify parent traits as something that already exist (external) and baby traits as something that results from those parent traits (internal).",
    "lever_E": "Students discover that baby traits are similar to parent traits — when a parent has a certain feature, the baby is likely to have a similar feature.",
    "lever_V": "Students build a simple model connecting parent traits to baby traits with an arrow.",
    "lever_Ev": "Students test their model by predicting what babies might look like based on their parents, then comparing to real photos.",
    "lever_R": "Students reflect on their own traits and think about which ones they might have inherited from their own families.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with adorable parent-baby animal photo", "say": "Look at this mama dog and her puppies! Do the puppies look like their mom? How?", "do": "Show a photo of a parent animal with babies. Have students call out similarities they notice.", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn?", "visual": "Learning goals with animal pictures", "say": "Today we will learn why baby animals look like their parents. We will learn the word TRAIT — that means a feature an animal has.", "do": "Point to your own traits: hair color, eye color. Ask students to name their own traits.", "time": "3 min"},
        {"num": "Slide 3", "title": "Let's Be Scientists!", "visual": "Big question with parent and baby animal photos", "say": "Why do baby animals look like their parents but not exactly the same? What do you think?", "do": "Show side-by-side photos of parents and babies. Students share what is the same and what is different.", "time": "3 min"},
        {"num": "Slide 4", "title": "What Are the Parts?", "visual": "Two component cards showing parent and baby", "say": "Our model has two parts: Parent Traits are the features the mom and dad have. Baby Traits are the features the baby gets.", "do": "Show a parent animal card with labeled traits. Ask: What traits might the baby get?", "time": "5 min"},
        {"num": "Slide 5", "title": "How Are They Connected?", "visual": "Arrow from parent traits to baby traits", "say": "Parents pass their traits to their babies. When a parent has spots, the baby will probably have spots too! But maybe not in the exact same places.", "do": "Students use sentence frame: The baby looks like its parent because it inherited _______.", "time": "5 min"},
        {"num": "Slide 6", "title": "What Did We Find Out?", "visual": "Key discoveries with comparison photos", "say": "We discovered that babies inherit traits from their parents. They look similar but not exactly the same — and that is what makes every animal special!", "do": "Review discoveries. Show one more parent-baby pair and have students identify inherited traits.", "time": "5 min"},
        {"num": "Slide 7", "title": "STEM Challenge", "visual": "Baby animal drawing challenge", "say": "A zoo needs your help! Look at these two parent animals and draw what their baby might look like. Use the traits you see!", "do": "Give students parent animal cards with clear traits. Students draw predicted babies and explain their choices.", "time": "10 min"}
    ],
    "sort_reasoning": "Parent Traits are external because they already exist before the baby is born — we cannot change what the parents look like. Baby Traits are internal because they develop as a result of what the parents passed along.",
    "relationships": [
        ("Parent Traits to Baby Traits", "POSITIVE (+)", "When a parent has a strong trait like spots or long ears, the baby is very likely to show a similar trait. More parent traits passed along means the baby looks more like the parent.")
    ],
    "sim_answers": [
        ("Spotted Parent", "When Parent Traits are set to spotted fur, Baby Traits show similar spots. The baby has spots like the parent but they might be in slightly different places or be slightly different sizes."),
        ("Striped Parent", "When Parent Traits are set to striped fur, Baby Traits show similar stripes. The baby has stripes like the parent but the stripes might be a little wider, thinner, or differently spaced.")
    ],
    "stem_intro": "Present the challenge: A zoo has two parent animals and they just had a baby! The zookeepers need you to predict what the baby looks like. Study both parents and draw the baby. Explain which traits you think came from which parent.",
    "stem_concepts": [
        ("Inherited Traits", "Babies get their traits from their parents. If a parent has big ears, the baby will probably have big ears too. Look closely at both parents to predict the baby."),
        ("Variation", "Babies are never exact copies. Even with the same parents, each baby is a little different. The traits from mom and dad mix together in new and unique ways.")
    ],
    "stem_eval": [
        ("Expert (4)", "Baby drawing includes traits from both parents and student can explain which trait came from which parent"),
        ("Proficient (3)", "Baby drawing shows similarities to parents and student can identify at least two inherited traits"),
        ("Developing (2)", "Baby drawing shows some connection to parents but student has trouble explaining why"),
        ("Beginning (1)", "Student needs help connecting the baby's features to the parent traits")
    ],
    "support": [
        "Provide a checklist of traits to compare: fur color, ear shape, tail length, eye color, body size",
        "Use side-by-side photos with arrows pointing to matching traits between parent and baby",
        "Sentence frame: The baby has _______ just like its parent because traits are _______."
    ],
    "extensions": [
        "Find a photo of yourself as a baby — what traits do you share with your parents?",
        "Compare two litters of kittens from the same parents — are the kittens all the same?",
        "Research an animal where the babies look very different from the parents, like butterflies"
    ],
    "cross_curr": [
        ("Math", "Make a chart comparing three traits between a parent and baby animal — mark same or different for each"),
        ("ELA", "Write three sentences comparing a baby animal to its parent using the word inherited"),
        ("Art", "Create a parent and baby animal art project showing matching traits with bright colors")
    ],
    "misconceptions": [
        ("Baby animals are exact copies of their parents", "Babies are SIMILAR to their parents but never exactly the same. Just like brothers and sisters look alike but are not identical, baby animals get a mix of traits that makes each one unique.", "Show photos of a litter of puppies from the same parents. Ask: Do they all look exactly the same? Why not?"),
        ("Baby animals choose what they look like", "Animals cannot choose their traits. Traits are passed from parents to babies automatically, before the baby is even born. A kitten cannot decide to have stripes if its parents have spots.", "Ask: Did you choose your eye color? No! You inherited it from your parents, just like baby animals do.")
    ],
    "sentence_frame": "When the parent has _______, the baby also has _______.",
    "coloring_description": "A mama cat with spotted fur sitting next to two kittens — one has spots like mama and the other has slightly different spots. Arrows point from the mama's spots to the kittens' spots to show the trait was passed along."
}

L04 = {
    "id": "G01-L04",
    "title": "What Do Animals Need to Survive?",
    "subtitle": "The Science of Animal Needs",
    "ngss": "1-LS1-1",
    "ngss_desc": "Use materials to design a solution to a human problem by mimicking how plants and animals use their external parts to help them survive, grow, and meet their needs.",
    "big_question": "What do animals need to stay alive and healthy?",
    "objectives": [
        "Name the basic things all animals need to survive",
        "Explain what happens when an animal does not get what it needs",
        "Describe how animals find food, water, and shelter in nature"
    ],
    "vocabulary": [
        ("Survive", "To stay alive and healthy by getting everything you need"),
        ("Shelter", "A safe place where an animal can hide from danger and bad weather"),
        ("Habitat", "The place where an animal lives that has everything it needs")
    ],
    "components": [
        ("Resources Available", "How much food, water, and shelter an animal can find in its habitat", True),
        ("Animal Health", "How strong and healthy the animal is based on whether it gets what it needs", False)
    ],
    "think_about_it": "If an animal has lots of food and water and a safe place to live, will it be healthy or sick?",
    "scenarios": [
        ("Plenty of Resources", "Set Resources Available to high and observe how Animal Health changes"),
        ("Very Few Resources", "Set Resources Available to low and observe how Animal Health changes")
    ],
    "sim_scenarios": [
        ("Plenty of Resources", "Resources Available set to high", "What do you predict will happen to Animal Health when there is plenty of food, water, and shelter?"),
        ("Very Few Resources", "Resources Available set to low", "What do you predict will happen to Animal Health when there is almost no food or water?")
    ],
    "discoveries": [
        "All animals need food, water, air, and shelter to survive",
        "When animals have plenty of resources, they are healthy and strong",
        "When resources are scarce, animals get weak and may not survive",
        "Different animals find their needs in different ways"
    ],
    "answer": "All animals need four basic things to survive: food for energy, water to drink, air to breathe, and shelter to stay safe. When an animal lives in a place that has plenty of all four things, it stays healthy and strong. If any of these needs are not met, the animal gets weak and could get sick. That is why the habitat an animal lives in is so important!",
    "stem_title": "Design an Animal Habitat",
    "stem_mission": "Build a model habitat for a chosen animal that provides everything it needs to survive.",
    "stem_scenario": "A wildlife rescue center needs your help! They found a lost animal and need to build it a perfect home. Design a habitat that gives the animal food, water, air, and shelter. Make sure it has everything the animal needs!",
    "stem_questions": [
        "What kind of food does your animal need in its habitat?",
        "Where will your animal find water and shelter?"
    ],
    "stem_design_qs": [
        "What animal are you building a habitat for?",
        "Where will the food be in your habitat?",
        "How will the animal get fresh water?",
        "What will the shelter look like to keep the animal safe?"
    ],
    "career": "Wildlife Biologists study animals in their natural habitats to make sure they have everything they need to survive. They earn $45,000-$80,000/year.",
    "images": {
        "cover": ("cover-animal-needs.png", "A photorealistic image of a bird family in a nest with a nearby stream, green leaves, and berries, warm natural lighting, cinematic nature photography"),
        "landscape": ("landscape-animal-needs.png", "Diverse 1st grade students (6-7 years old, wide variety of ethnicities including Black, Latino, Asian, and white children) building animal habitats from shoeboxes with craft materials, bright modern classroom, natural window light, editorial photo quality"),
        "modeling": ("modeling-animal-needs.png", "A simple, colorful kid-friendly diagram showing four icons around an animal: food (apple), water (droplet), air (cloud), shelter (house), connected by arrows, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-animal-needs.png", "A teacher with diverse 1st graders (6-7 years old, wide variety of ethnicities) looking at pictures of different animal habitats on a smartboard, students sitting on a colorful rug pointing at the screen"),
        "stem": ("stem-animal-needs.png", "Diverse 1st graders (6-7 years old, wide mix of ethnicities) building model habitats from shoeboxes with clay animals, paper trees, and blue fabric for water, excited collaborative work")
    },
    "pre_assessment": [
        "Draw a picture of an animal in a place where it has everything it needs. Label the things the animal needs.",
        "Circle what animals need to survive: food, a TV, water, a phone, air, shelter, toys."
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students build a model habitat showing how resources connect to animal health and survival."),
        ("Disciplinary Core Idea", "LS1.A Structure and Function", "All organisms have external parts that they use to perform daily functions including survival, growth, and reproduction."),
        ("Crosscutting Concept", "Cause and Effect", "Students explore how having or lacking resources causes animals to be healthy or unhealthy.")
    ],
    "background_intro": "Every animal on Earth needs certain things to survive. From tiny ants to giant elephants, all animals share the same basic needs.",
    "background_sections": [
        ("The Four Basic Needs", "All animals need four things to stay alive: food gives them energy to move, grow, and stay warm; water keeps their bodies working properly since all living things are mostly made of water; air provides oxygen that every animal needs to breathe; and shelter protects them from bad weather, extreme temperatures, and predators. If any one of these needs is missing, the animal will struggle to survive."),
        ("Habitats Provide What Animals Need", "A habitat is the natural home of an animal — the place where it can find all four of its basic needs. A pond is a great habitat for a frog because it has water to swim in, insects to eat, air to breathe, and lily pads and mud for shelter. A desert is perfect for a lizard because it has insects to eat, small water sources, air, and rocks for shelter. When a habitat is damaged or changed, animals may lose the resources they need.")
    ],
    "lever_L": "Students identify resources available as something that depends on the habitat (external) and animal health as something that changes based on those resources (internal).",
    "lever_E": "Students discover that when resources go up, animal health goes up — a positive connection.",
    "lever_V": "Students build a simple model showing how the amount of resources affects animal health.",
    "lever_Ev": "Students test their model by comparing what happens with plenty of resources versus very few resources.",
    "lever_R": "Students reflect on how their model explains why some animals thrive in certain habitats and struggle in others.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with animals in a healthy habitat", "say": "Think about your pet or an animal you know. What does it need every single day? Let us make a list!", "do": "Create a class list of things animals need. Accept all answers and revisit at the end to see which ones are correct.", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn?", "visual": "Learning goals with animal icons", "say": "Today we are going to learn the four things every animal needs to survive. We will also learn what a habitat is!", "do": "Introduce vocabulary: survive, shelter, habitat. Use pictures and gestures for each word.", "time": "3 min"},
        {"num": "Slide 3", "title": "Let's Be Scientists!", "visual": "Big question with photos of animals in different habitats", "say": "What do animals need to stay alive and healthy? Do all animals need the same things?", "do": "Think-pair-share. Students discuss what they think animals need most. Collect ideas.", "time": "3 min"},
        {"num": "Slide 4", "title": "What Are the Parts?", "visual": "Two component cards with resource and health icons", "say": "Our model has two parts: Resources Available is how much food, water, and shelter is around. Animal Health is how strong and healthy the animal is.", "do": "Show pictures of a well-fed animal vs. a thin animal. Ask: What is different? Why?", "time": "5 min"},
        {"num": "Slide 5", "title": "How Are They Connected?", "visual": "Arrow connecting resources to health", "say": "When there are MORE resources, what happens to the animal? Does it get healthier or weaker?", "do": "Students use sentence frame: When resources go up, animal health goes up. Draw the positive arrow together.", "time": "5 min"},
        {"num": "Slide 6", "title": "What Did We Find Out?", "visual": "Key discoveries with habitat photos", "say": "We discovered that all animals need food, water, air, and shelter. When they have these things, they are healthy!", "do": "Review the class list from Slide 1. Check off which items were correct. Add any that were missing.", "time": "5 min"},
        {"num": "Slide 7", "title": "STEM Challenge", "visual": "Habitat building challenge", "say": "Time to build a home for an animal! Make sure your habitat has food, water, and shelter.", "do": "Distribute shoeboxes and craft materials. Students choose an animal and build its habitat, labeling the four needs.", "time": "10 min"}
    ],
    "sort_reasoning": "Resources Available is external because the habitat determines how much food, water, and shelter exists — the animal does not control this. Animal Health is internal because it changes depending on how many resources the animal can get.",
    "relationships": [
        ("Resources Available to Animal Health", "POSITIVE (+)", "When more resources like food, water, and shelter are available, the animal stays healthier and stronger. Less resources means the animal gets weaker.")
    ],
    "sim_answers": [
        ("Plenty of Resources", "When Resources Available is set to high, Animal Health is excellent. The animal has all the food, water, and shelter it needs, so it grows strong, has energy, and stays healthy."),
        ("Very Few Resources", "When Resources Available is set to low, Animal Health drops. Without enough food or water, the animal gets weak, tired, and may get sick because its body does not have what it needs.")
    ],
    "stem_intro": "Present the challenge: A wildlife rescue center found a lost animal and needs your help building it a perfect home. Choose an animal and design a habitat with food, water, air, and shelter. Make sure it has everything your animal needs to be healthy!",
    "stem_concepts": [
        ("Four Basic Needs", "Every animal needs food, water, air, and shelter. Your habitat design must include all four of these things or the animal will not survive."),
        ("Habitats Match Animals", "Different animals need different habitats. A fish needs a pond but a bird needs a tree. Make sure your habitat matches what YOUR animal needs.")
    ],
    "stem_eval": [
        ("Expert (4)", "Habitat includes all four basic needs labeled and student explains how each one helps the animal survive"),
        ("Proficient (3)", "Habitat includes at least three needs and student can explain why the animal needs them"),
        ("Developing (2)", "Habitat is built but is missing some needs or student has trouble explaining their importance"),
        ("Beginning (1)", "Student needs help identifying what the animal needs or building the habitat")
    ],
    "support": [
        "Provide a checklist with pictures: food, water, air, shelter — students check each one as they add it",
        "Pre-cut pictures of food, water, and shelter items that students can glue into their habitat",
        "Sentence frame: My animal needs _______ to survive because _______."
    ],
    "extensions": [
        "What happens to animals when their habitat is destroyed? Draw a before and after picture.",
        "Compare what a fish needs versus what a bird needs — what is the same and what is different?",
        "Go outside and look for animal habitats on the school grounds — what needs can you find being met?"
    ],
    "cross_curr": [
        ("Math", "Sort pictures of 10 animals by how many of the four needs their habitat provides and count each group"),
        ("ELA", "Write a letter to a zookeeper explaining what an animal needs and why each need is important"),
        ("Art", "Create a mural of a healthy habitat showing all four needs with labels and bright colors")
    ],
    "misconceptions": [
        ("Animals only need food to survive", "Food is important but it is only ONE of four things animals need. Without water, animals would dry out. Without air, they could not breathe. Without shelter, they would have no protection from weather or predators. All four needs must be met.", "Ask: What would happen if you had all the food in the world but no water? Could you survive? Animals are the same way!"),
        ("All animals need the same kind of food", "Different animals eat very different things. Lions eat meat, rabbits eat plants, and bears eat both. But ALL animals need SOME kind of food for energy. The type of food changes, but the need for food stays the same for every animal.", "Show pictures of different animals eating different foods. Ask: What does each one eat? They are all different but they ALL need food!")
    ],
    "sentence_frame": "When resources available goes up, animal health goes up.",
    "coloring_description": "A happy rabbit in a meadow surrounded by its four needs: a carrot (food), a little stream (water), clouds in the sky (air), and a burrow hole (shelter). Each need has a label with a dotted line connecting it to the rabbit."
}

L05 = {
    "id": "G01-L05",
    "title": "How Do Animals Use Their Body Parts?",
    "subtitle": "The Science of Structure and Function",
    "ngss": "1-LS1-1",
    "ngss_desc": "Use materials to design a solution to a human problem by mimicking how plants and animals use their external parts to help them survive, grow, and meet their needs.",
    "big_question": "How do animals use their body parts to help them survive?",
    "objectives": [
        "Name body parts that help animals survive",
        "Match animal body parts to what they help the animal do",
        "Explain how body part size or shape helps an animal do its job"
    ],
    "vocabulary": [
        ("Structure", "A body part that has a special shape, like claws, wings, or a beak"),
        ("Function", "The job that a body part does, like grabbing, flying, or eating")
    ],
    "components": [
        ("Body Part Size", "How big or long an animal's body part is — like a long beak versus a short beak", True),
        ("Ability to Get Food", "How well the animal can catch, reach, or eat its food using that body part", False)
    ],
    "think_about_it": "If a bird has a very long beak, can it reach food inside a deep flower better than a bird with a short beak?",
    "scenarios": [
        ("Long Beak", "Set Body Part Size to long and observe the Ability to Get Food from a deep flower"),
        ("Short Beak", "Set Body Part Size to short and observe the Ability to Get Food from a deep flower")
    ],
    "sim_scenarios": [
        ("Long Beak", "Body Part Size set to long beak", "What do you predict will happen to the bird's Ability to Get Food from a deep flower with a long beak?"),
        ("Short Beak", "Body Part Size set to short beak", "What do you predict will happen to the bird's Ability to Get Food from a deep flower with a short beak?")
    ],
    "discoveries": [
        "Animals have special body parts that help them survive",
        "The shape and size of a body part matches the job it needs to do",
        "A long beak helps birds reach food that short-beaked birds cannot reach"
    ],
    "answer": "Animals have body parts that are specially shaped to help them survive! A bird's beak is shaped to match the kind of food it eats — long beaks reach deep into flowers for nectar, and short strong beaks crack open seeds. Every animal body part has a job: claws help grab, legs help run, and fins help swim. The shape of the part matches the job it does!",
    "stem_title": "Design an Animal Tool",
    "stem_mission": "Build a tool inspired by an animal body part that helps solve a problem, like picking up small objects.",
    "stem_scenario": "Scientists need your help! They want to pick up small beads from a cup without using their fingers. Look at animal body parts for ideas. Can you design a tool that works like an animal's beak, claw, or trunk to grab the beads?",
    "stem_questions": [
        "Which animal body part gives you the best idea for your tool?",
        "Why is the shape of your tool important for grabbing small things?"
    ],
    "stem_design_qs": [
        "What animal body part inspired your tool design?",
        "What materials will you use to build your tool?",
        "How will you test if your tool can pick up small beads?",
        "Can you make your tool work better by changing its shape or size?"
    ],
    "career": "Biomedical Engineers design tools and devices inspired by animal body parts, like robotic arms that work like elephant trunks. They earn $50,000-$95,000/year.",
    "images": {
        "cover": ("cover-body-parts.png", "A photorealistic close-up of a hummingbird with its long beak reaching into a bright red flower, vivid colors, shallow depth of field, cinematic nature photography"),
        "landscape": ("landscape-body-parts.png", "Diverse 1st grade students (6-7 years old, wide variety of ethnicities including Black, Latino, Asian, and white children) looking at animal photos and matching body parts to functions on a worksheet, bright modern classroom, natural window light"),
        "modeling": ("modeling-body-parts.png", "A simple, colorful kid-friendly diagram showing three birds with different beak sizes next to the food they eat, arrows connecting each beak to its food, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-body-parts.png", "A teacher with diverse 1st graders (6-7 years old, wide variety of ethnicities) comparing toy animal figures and pointing to different body parts like claws, beaks, and fins, bright classroom with animal posters"),
        "stem": ("stem-body-parts.png", "Diverse 1st graders (6-7 years old, wide mix of ethnicities) building grabbing tools from clothespins, spoons, and pipe cleaners to pick up small objects, excited expressions, modern classroom")
    },
    "pre_assessment": [
        "Draw an animal and circle one body part. Write or tell what job that body part does.",
        "Circle the body part that helps a bird eat: wings, beak, tail feathers."
    ],
    "dimensions": [
        ("Science Practice", "Constructing Explanations", "Students explain how specific body parts help animals survive by matching structure to function."),
        ("Disciplinary Core Idea", "LS1.A Structure and Function", "All organisms have external parts that help them survive, grow, and meet their needs."),
        ("Crosscutting Concept", "Structure and Function", "Students explore how the shape and size of body parts relate to the jobs they perform.")
    ],
    "background_intro": "Animals have amazing body parts that are perfectly designed for the jobs they need to do. From eagle talons to elephant trunks, every structure has a function.",
    "background_sections": [
        ("Structure Matches Function", "In science, structure means the shape or form of something, and function means the job it does. A bird's wings are shaped for flying — they are wide, flat, and lightweight. A fish's fins are shaped for swimming — they push water to help the fish move. A cat's claws are curved and sharp for climbing and catching. Every animal body part has a shape that matches its job perfectly."),
        ("Different Body Parts for Different Jobs", "Animals use their body parts to meet their basic needs: getting food, staying safe, and moving around. A frog's long sticky tongue catches flies. A turtle's hard shell protects it from predators. A cheetah's long legs help it run fast to catch prey. Even the same body part can look different in different animals — an eagle's beak is hooked for tearing meat, while a hummingbird's beak is long and thin for sipping nectar. The shape tells us what the animal eats and how it lives.")
    ],
    "lever_L": "Students identify body part size as something that varies between animals (external) and ability to get food as something that depends on the body part (internal).",
    "lever_E": "Students discover that when a body part better matches the food source, the ability to get food goes up.",
    "lever_V": "Students build a simple model showing how body part size connects to the ability to get food.",
    "lever_Ev": "Students test their model by comparing long-beaked and short-beaked scenarios with deep flowers.",
    "lever_R": "Students reflect on how their model explains why different birds have different beak shapes in nature.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with amazing animal body part close-up", "say": "Look at this hummingbird's beak! It is so long and thin. Why do you think it looks like that? Let us find out!", "do": "Show photos of three different animal body parts. Ask: What job does each one do?", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn?", "visual": "Learning goals with body part pictures", "say": "Today we will learn two important words: STRUCTURE means a body part's shape. FUNCTION means the job it does.", "do": "Practice: Point to your hand (structure) and show grabbing (function). Point to legs (structure) and show walking (function).", "time": "3 min"},
        {"num": "Slide 3", "title": "Let's Be Scientists!", "visual": "Big question with animal collage", "say": "How do animals use their body parts to survive? Why does a bird's beak look different from a dog's mouth?", "do": "Show three different bird beaks. Students predict what each bird eats based on beak shape.", "time": "3 min"},
        {"num": "Slide 4", "title": "What Are the Parts?", "visual": "Two component cards showing beak and food", "say": "Our model has two parts: Body Part Size is how big or long the beak is. Ability to Get Food is how well the bird can eat.", "do": "Show a long straw and a short straw. Ask: Which one could reach the bottom of a tall glass?", "time": "5 min"},
        {"num": "Slide 5", "title": "How Are They Connected?", "visual": "Arrow connecting body part to food ability", "say": "When the beak is longer, can the bird reach deeper into a flower? Yes! Longer beak means better ability to get nectar.", "do": "Students try picking up small items with long tweezers vs. short tweezers to feel the difference.", "time": "5 min"},
        {"num": "Slide 6", "title": "What Did We Find Out?", "visual": "Key discoveries with animal examples", "say": "We found out that body parts have special shapes that match their jobs. A long beak is perfect for reaching deep flowers!", "do": "Review discoveries. Match three animals to their body parts and functions as a class.", "time": "5 min"},
        {"num": "Slide 7", "title": "STEM Challenge", "visual": "Animal tool design challenge", "say": "Now YOU will design a tool inspired by an animal body part. Can you build something that picks up small beads?", "do": "Distribute clothespins, spoons, pipe cleaners, cups of beads. Students design and test grabbing tools.", "time": "10 min"}
    ],
    "sort_reasoning": "Body Part Size is external because it is a feature the animal already has — we are comparing different animals with different body parts. Ability to Get Food is internal because it changes depending on how well the body part matches the food source.",
    "relationships": [
        ("Body Part Size to Ability to Get Food", "POSITIVE (+)", "A longer beak helps the bird reach food in deep flowers better. When the body part better matches the food source, the animal is better at getting food.")
    ],
    "sim_answers": [
        ("Long Beak", "When Body Part Size is set to long, Ability to Get Food from deep flowers is very high. The long beak can reach all the way to the bottom of the flower to sip the nectar."),
        ("Short Beak", "When Body Part Size is set to short, Ability to Get Food from deep flowers is low. The short beak cannot reach the nectar at the bottom of a deep flower, so the bird goes hungry.")
    ],
    "stem_intro": "Present the challenge: Scientists need a tool that can pick up tiny beads from a cup without using fingers. Look at animal body parts for inspiration! Beaks grab, claws pinch, trunks wrap around things. Design and build your tool, then test it!",
    "stem_concepts": [
        ("Structure and Function", "The shape of a tool matters — just like animal body parts. A wide grabber is good for big things. A narrow grabber is good for small things. Match your tool shape to the job."),
        ("Biomimicry", "Biomimicry means copying ideas from nature. Engineers look at animal body parts to get ideas for tools, machines, and inventions. You are doing the same thing!")
    ],
    "stem_eval": [
        ("Expert (4)", "Tool successfully picks up beads and student explains which animal body part inspired the design and why the shape matters"),
        ("Proficient (3)", "Tool picks up some beads and student can name the animal body part that inspired it"),
        ("Developing (2)", "Tool is built but has trouble picking up beads; student has difficulty explaining the connection to animals"),
        ("Beginning (1)", "Student needs help building the tool or connecting it to an animal body part")
    ],
    "support": [
        "Provide photos of animal body parts with labels showing what each one does",
        "Pre-assemble one example tool for students to copy and then modify",
        "Sentence frame: My tool works like a _______ because it can _______."
    ],
    "extensions": [
        "Try to design a tool that works like an elephant trunk — can you make something that wraps around objects?",
        "Research an animal with a body part you find amazing. Draw it and explain what job it does.",
        "Compare a human hand to a bird claw — what can each one do? What is different?"
    ],
    "cross_curr": [
        ("Math", "Count how many beads your tool picks up in 30 seconds and compare with other students using a chart"),
        ("ELA", "Write about your favorite animal body part: what is its structure and what is its function?"),
        ("Art", "Draw your dream animal with body parts from three different real animals and explain each one")
    ],
    "misconceptions": [
        ("Animals choose to grow body parts they need", "Animals do not choose their body parts. They are born with them! Over many, many years, animals that had body parts that helped them survive had more babies, and those babies inherited the same helpful body parts.", "Ask: Did you choose to have fingers? No! You were born with them. Animals are the same — they are born with the body parts they have."),
        ("All beaks do the same job", "Different beak shapes do different jobs. A pelican's wide beak scoops fish from water. A woodpecker's strong pointy beak hammers into trees. A parrot's curved beak cracks open hard nuts. The shape tells us what the bird eats!", "Show photos of five different bird beaks. Ask: Could a hummingbird crack a nut? Could a pelican sip from a tiny flower? Shape matters!")
    ],
    "sentence_frame": "When body part size goes up, ability to get food goes up.",
    "coloring_description": "Three birds sitting on a branch, each with a different beak shape: one long and thin reaching into a flower, one short and thick cracking a seed, and one wide and flat scooping a fish. Labels show each beak's job."
}

L06 = {
    "id": "G01-L06",
    "title": "Why Is It Dark at Night?",
    "subtitle": "The Science of Day and Night Patterns",
    "ngss": "1-ESS1-1",
    "ngss_desc": "Use observations of the sun, moon, and stars to describe patterns that can be predicted.",
    "big_question": "Why does the sky get dark at night and bright during the day?",
    "objectives": [
        "Describe the pattern of day and night",
        "Explain that the Earth spinning causes day and night",
        "Predict when it will be light or dark based on Earth's position"
    ],
    "vocabulary": [
        ("Rotate", "To spin around in a circle, like a top — the Earth rotates once every day"),
        ("Pattern", "Something that repeats the same way over and over, like day then night then day again")
    ],
    "components": [
        ("Earth's Position", "Which side of the Earth is facing the sun as the Earth slowly spins", True),
        ("Amount of Sunlight", "How much light from the sun reaches your part of the Earth — lots during the day, none at night", False)
    ],
    "think_about_it": "When your side of the Earth faces the sun, is it daytime or nighttime where you are?",
    "scenarios": [
        ("Facing the Sun", "Set Earth's Position to facing the sun and observe the Amount of Sunlight"),
        ("Facing Away", "Set Earth's Position to facing away from the sun and observe the Amount of Sunlight")
    ],
    "sim_scenarios": [
        ("Facing the Sun", "Earth's Position set to facing the sun", "What do you predict the Amount of Sunlight will be when your side of Earth faces the sun?"),
        ("Facing Away", "Earth's Position set to facing away from the sun", "What do you predict the Amount of Sunlight will be when your side of Earth faces away from the sun?")
    ],
    "discoveries": [
        "The Earth spins slowly all the time, which causes day and night",
        "When your side of Earth faces the sun, it is daytime and the sky is bright",
        "When your side of Earth faces away from the sun, it is nighttime and the sky is dark",
        "Day and night is a pattern that repeats every single day"
    ],
    "answer": "It gets dark at night because the Earth is always slowly spinning like a top! The sun does not move — WE move. When your part of the Earth faces the sun, sunlight shines on you and it is daytime. As the Earth keeps spinning, your part turns away from the sun, and it gets dark — that is nighttime. Then the Earth keeps spinning and brings you back around to face the sun again. Day, night, day, night — it is a pattern that never stops!",
    "stem_title": "Build a Day and Night Model",
    "stem_mission": "Create a model showing how the Earth spinning causes day and night using a ball and a flashlight.",
    "stem_scenario": "A young student from another class asked you: Why does the sun go away at night? You know the answer — the sun does NOT go away! Build a model to show this younger student how day and night really work.",
    "stem_questions": [
        "In your model, what represents the Earth and what represents the sun?",
        "How can you show that the Earth spinning causes daytime on one side and nighttime on the other?"
    ],
    "stem_design_qs": [
        "What round object will you use for the Earth?",
        "How will you show which part of the Earth has daytime?",
        "How will you spin the Earth to show day changing to night?",
        "Can you mark a spot on your Earth to show where YOU live and track when it is day and night?"
    ],
    "career": "Astronomers study the sun, moon, stars, and planets to understand how they move. They use telescopes and computers. They earn $60,000-$120,000/year.",
    "images": {
        "cover": ("cover-day-night.png", "A stunning split image showing daytime sky with bright sun on one side and nighttime sky with stars and moon on the other, smooth gradient transition, cinematic and vivid"),
        "landscape": ("landscape-day-night.png", "Diverse 1st grade students (6-7 years old, wide variety of ethnicities including Black, Latino, Asian, and white children) using flashlights and globes to model day and night in a slightly darkened classroom, wonder on their faces, editorial photo quality"),
        "modeling": ("modeling-day-night.png", "A simple, colorful kid-friendly diagram showing the Earth as a circle with a sunny side labeled Day and a dark side labeled Night, with the sun on one side, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-day-night.png", "A teacher with diverse 1st graders (6-7 years old, wide variety of ethnicities) pointing at a large globe while holding a flashlight, students gathered around watching the light and shadow, bright classroom"),
        "stem": ("stem-day-night.png", "Diverse 1st graders (6-7 years old, wide mix of ethnicities) working in pairs with balls and flashlights, shining light on one side and pointing to the dark side, excited discovery expressions")
    },
    "pre_assessment": [
        "Draw what the sky looks like during the day and what it looks like at night.",
        "Circle the correct answer: The sun goes away at night / The Earth spins and our side faces away from the sun."
    ],
    "dimensions": [
        ("Science Practice", "Analyzing and Interpreting Data", "Students observe and describe the pattern of day and night caused by Earth's rotation."),
        ("Disciplinary Core Idea", "ESS1.A The Universe and its Stars", "Patterns of the motion of the sun, moon, and stars in the sky can be observed, described, and predicted."),
        ("Crosscutting Concept", "Patterns", "Students identify that day and night is a repeating, predictable pattern caused by Earth's rotation.")
    ],
    "background_intro": "Day and night is one of the most important patterns in nature. Understanding why it happens helps us learn how our planet moves through space.",
    "background_sections": [
        ("Why Day and Night Happen", "The Earth is always spinning, rotating once every 24 hours. This spinning is what causes day and night. The sun stays in one place — it does not rise and set like it looks from the ground. Instead, the Earth turns so that different parts face the sun at different times. When your part of the Earth faces the sun, it is daytime. When your part rotates away from the sun, it is nighttime. This is why day and night always follow each other in a predictable pattern."),
        ("A Pattern We Can Predict", "Because the Earth spins at the same steady speed, day and night follow a very reliable pattern. We know exactly when the sun will rise and set every single day. This pattern is so reliable that people have used it to tell time for thousands of years. Sunrise, daytime, sunset, nighttime — and then it starts all over again. The whole cycle takes about 24 hours, which is why we say a day is 24 hours long.")
    ],
    "lever_L": "Students identify Earth's position as the external component we can set (facing sun or away) and amount of sunlight as the internal result that changes.",
    "lever_E": "Students discover that when your side of Earth faces the sun, sunlight is high (day), and when it faces away, sunlight is zero (night).",
    "lever_V": "Students build a simple model with two parts showing how Earth's position controls the amount of sunlight.",
    "lever_Ev": "Students test their model by simulating both positions and comparing the results.",
    "lever_R": "Students reflect on how their model explains the daily pattern of day and night they experience.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with day/night split sky", "say": "Why is it bright outside right now but it will be dark tonight? Where does the sun go? Or does it go anywhere at all?", "do": "Ask students to share what they think happens to the sun at night. Write ideas on the board to revisit later.", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn?", "visual": "Learning goals with sun and Earth icons", "say": "Today we will learn WHY it gets dark at night. We will learn a big word: ROTATE. It means to spin around!", "do": "Have students stand up and rotate in place slowly. Say: That is what the Earth does all the time!", "time": "3 min"},
        {"num": "Slide 3", "title": "Let's Be Scientists!", "visual": "Big question with sun and dark sky images", "say": "Here is our big question: Why does the sky get dark at night? Does the sun really go away, or does something else happen?", "do": "Think-pair-share. Students share their ideas with a partner. Collect predictions.", "time": "3 min"},
        {"num": "Slide 4", "title": "What Are the Parts?", "visual": "Two component cards with Earth and sun diagrams", "say": "Our model has two parts: Earth's Position is which way we face. Amount of Sunlight is how much light we get.", "do": "Hold up a ball (Earth) and a flashlight (sun). Shine the light on one side. Ask: Is the other side bright or dark?", "time": "5 min"},
        {"num": "Slide 5", "title": "How Are They Connected?", "visual": "Diagram showing rotation and light", "say": "When our side faces the sun, we get sunlight — that is DAY. When we spin away, no sunlight — that is NIGHT!", "do": "Slowly rotate the ball in front of the flashlight. Students watch the lit side and dark side switch. Use sentence frame.", "time": "5 min"},
        {"num": "Slide 6", "title": "What Did We Find Out?", "visual": "Key discoveries with day/night cycle", "say": "The sun does NOT go away at night! The Earth spins and our side turns away from the sun. It is a pattern that happens every single day.", "do": "Revisit predictions from Slide 1. Ask: Were we right? What did we learn that surprised us?", "time": "5 min"},
        {"num": "Slide 7", "title": "STEM Challenge", "visual": "Day/night model building challenge", "say": "Now build your own model to show a younger student why it gets dark at night. Use a ball and flashlight!", "do": "Distribute balls, flashlights, and stickers (to mark your location). Students build and demonstrate their models.", "time": "10 min"}
    ],
    "sort_reasoning": "Earth's Position is external because it is the input we set — which side faces the sun. Amount of Sunlight is internal because it changes automatically depending on which way the Earth is facing.",
    "relationships": [
        ("Earth's Position to Amount of Sunlight", "POSITIVE (+)", "When your side of Earth faces more toward the sun, you get more sunlight. Facing the sun means daytime. Facing away means nighttime.")
    ],
    "sim_answers": [
        ("Facing the Sun", "When Earth's Position is set to facing the sun, Amount of Sunlight is very high. The sun's light shines directly on your part of the Earth, making it bright and warm — this is daytime!"),
        ("Facing Away", "When Earth's Position is set to facing away from the sun, Amount of Sunlight is zero. Your part of the Earth is in shadow because the sun's light cannot reach the far side — this is nighttime!")
    ],
    "stem_intro": "Present the challenge: A younger student thinks the sun goes away at night. You know the truth — the sun stays in the same place and the EARTH spins! Build a model with a ball and flashlight to show how day and night really work.",
    "stem_concepts": [
        ("Earth Rotates", "The Earth spins like a top, once every 24 hours. This spinning is what causes day and night. The sun does not move — we do!"),
        ("Predictable Patterns", "Day and night follow the same pattern every single day. We can predict when the sun will rise and set because the Earth spins at the same speed all the time.")
    ],
    "stem_eval": [
        ("Expert (4)", "Model correctly shows Earth rotating to cause day and night, and student explains that the sun does not move"),
        ("Proficient (3)", "Model shows light and dark sides and student can explain which side has daytime"),
        ("Developing (2)", "Model shows light on one side but student has trouble explaining that Earth's spinning causes the pattern"),
        ("Beginning (1)", "Student needs help understanding that the Earth rotates or setting up the model")
    ],
    "support": [
        "Put a sticker on the ball where the student lives so they can track their location as the ball rotates",
        "Use a darkened room so the flashlight effect is very obvious",
        "Sentence frame: When my side of Earth faces the sun, it is _______. When it faces away, it is _______."
    ],
    "extensions": [
        "If it is daytime where you live, where on the globe is it nighttime right now? Find it on a map!",
        "Keep a sunrise/sunset journal for a week — what pattern do you notice about the times?",
        "What would happen if the Earth stopped spinning? Would one side always be day and the other always night?"
    ],
    "cross_curr": [
        ("Math", "Track sunrise and sunset times for five days and look for number patterns on a chart"),
        ("ELA", "Write a short story about what the Earth says as it spins from day to night"),
        ("Art", "Paint a picture showing half of the Earth in bright sunshine and half in dark starry night")
    ],
    "misconceptions": [
        ("The sun goes away at night and comes back in the morning", "The sun never goes away! It stays in the same spot all the time. What changes is which part of the Earth faces the sun. When your side turns away from the sun, it looks like the sun disappears, but really YOU moved, not the sun.", "Shine a flashlight on a ball. Slowly spin the ball. Ask: Did the flashlight move? No! But the lit side changed. That is what happens with the Earth and sun!"),
        ("The moon makes it dark at night", "The moon does not cause nighttime. Nighttime happens because your part of the Earth has rotated away from the sun. The moon actually reflects sunlight — that is why it glows at night! Sometimes the moon is visible during the day too.", "Show a photo of the moon during daytime. Ask: If the moon causes night, why can we sometimes see it during the day? Night is caused by Earth spinning, not the moon.")
    ],
    "sentence_frame": "When Earth's position faces the sun, the amount of sunlight goes up.",
    "coloring_description": "The Earth shown as a big circle with the sun on one side. The side facing the sun is bright with a smiling child playing outside. The side facing away is dark with a sleeping child in bed with stars outside the window."
}

L07 = {
    "id": "G01-L07",
    "title": "How Do Seasons Change?",
    "subtitle": "The Science of Seasonal Patterns",
    "ngss": "1-ESS1-2",
    "ngss_desc": "Make observations at different times of year to relate the amount of daylight to the time of year.",
    "big_question": "Why is it hot in summer and cold in winter?",
    "objectives": [
        "Name the four seasons and describe what each one looks like",
        "Explain that seasons follow a pattern that repeats every year",
        "Connect the amount of daylight to the temperature in each season"
    ],
    "vocabulary": [
        ("Season", "One of four times of the year — spring, summer, fall, and winter — each with different weather"),
        ("Daylight", "The hours when the sun is shining and the sky is bright — some seasons have more daylight than others")
    ],
    "components": [
        ("Amount of Daylight", "How many hours of sunshine there are in a day — long sunny days in summer, short sunny days in winter", True),
        ("Temperature", "How hot or cold it is outside — warmer when there is more daylight, cooler when there is less", False)
    ],
    "think_about_it": "In summer, the sun is out for a long time. In winter, it gets dark early. Which season do you think is warmer?",
    "scenarios": [
        ("Summer Days", "Set Amount of Daylight to very high and observe what happens to Temperature"),
        ("Winter Days", "Set Amount of Daylight to very low and observe what happens to Temperature")
    ],
    "sim_scenarios": [
        ("Summer Days", "Amount of Daylight set to very high (long sunny days)", "What do you predict will happen to Temperature when there are many hours of sunlight?"),
        ("Winter Days", "Amount of Daylight set to very low (short sunny days)", "What do you predict will happen to Temperature when there are only a few hours of sunlight?")
    ],
    "discoveries": [
        "Seasons follow a pattern: spring, summer, fall, winter, and then it starts again",
        "Summer has the most daylight hours and the warmest temperatures",
        "Winter has the fewest daylight hours and the coldest temperatures",
        "More daylight means warmer weather because the sun warms the Earth longer"
    ],
    "answer": "Seasons change because the amount of daylight changes throughout the year! In summer, the sun shines for many hours each day, warming the Earth and making it hot. In winter, the sun is out for only a short time, so the Earth does not get as warm and it stays cold. Spring and fall are in between — not too much sun and not too little. This pattern of seasons repeats every single year!",
    "stem_title": "Create a Season Wheel",
    "stem_mission": "Build a spinning season wheel that shows what happens to daylight and temperature in each of the four seasons.",
    "stem_scenario": "A weather station needs a tool to help explain seasons to kids. Design a season wheel that shows how daylight and temperature change from spring to summer to fall to winter. Make it spin to show the pattern!",
    "stem_questions": [
        "Which season on your wheel has the most daylight and warmest temperature?",
        "Does the pattern on your wheel ever stop, or does it keep repeating?"
    ],
    "stem_design_qs": [
        "How will you divide your wheel into four equal parts for four seasons?",
        "What colors will you use to show warm and cold temperatures?",
        "How will you show that summer has more daylight than winter?",
        "How will you make your wheel spin to show the pattern repeating?"
    ],
    "career": "Meteorologists study weather patterns and seasons to help people prepare for storms, heat waves, and cold snaps. They earn $50,000-$100,000/year.",
    "images": {
        "cover": ("cover-seasons.png", "A beautiful photorealistic four-panel image showing the same tree in all four seasons: spring blossoms, summer green leaves, fall orange and red leaves, winter bare branches with snow, cinematic nature photography"),
        "landscape": ("landscape-seasons.png", "Diverse 1st grade students (6-7 years old, wide variety of ethnicities including Black, Latino, Asian, and white children) creating season artwork with paper plates divided into four sections, bright modern classroom, natural window light, editorial photo quality"),
        "modeling": ("modeling-seasons.png", "A simple, colorful kid-friendly diagram showing a circle divided into four sections labeled Spring, Summer, Fall, Winter with a sun icon and thermometer in each section showing different sizes, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-seasons.png", "A teacher with diverse 1st graders (6-7 years old, wide variety of ethnicities) pointing at a large poster of the four seasons, students sitting on a rug sharing their favorite season, bright classroom with season decorations"),
        "stem": ("stem-seasons.png", "Diverse 1st graders (6-7 years old, wide mix of ethnicities) building spinning season wheels from paper plates and brass fasteners, coloring each section with seasonal colors, modern classroom")
    },
    "pre_assessment": [
        "Draw your favorite season. Show what the weather is like and what you wear outside.",
        "Circle the season when the sun shines the longest each day: spring, summer, fall, winter."
    ],
    "dimensions": [
        ("Science Practice", "Analyzing and Interpreting Data", "Students observe and analyze how daylight and temperature change across the four seasons."),
        ("Disciplinary Core Idea", "ESS1.B Earth and the Solar System", "Seasonal patterns of sunrise and sunset can be observed, described, and predicted."),
        ("Crosscutting Concept", "Patterns", "Students recognize that seasons follow a predictable, repeating pattern throughout the year.")
    ],
    "background_intro": "The four seasons are one of nature's most important patterns. Spring, summer, fall, and winter bring changes in weather, daylight, and the natural world around us.",
    "background_sections": [
        ("What Causes Seasons", "Seasons happen because the Earth is tilted as it moves around the sun. During summer, your part of the Earth tilts toward the sun, so the sun is higher in the sky and shines for more hours each day. During winter, your part tilts away from the sun, so the sun is lower in the sky and shines for fewer hours. More hours of sunlight means more warmth, which is why summer is hot and winter is cold."),
        ("The Seasonal Pattern", "Seasons always follow the same order: spring, summer, fall, winter. This pattern repeats every year without fail. In spring, days get longer and temperatures warm up. In summer, days are the longest and temperatures are the warmest. In fall, days get shorter and temperatures cool down. In winter, days are the shortest and temperatures are the coldest. Then spring comes again and the cycle starts over. People, plants, and animals all depend on this reliable pattern.")
    ],
    "lever_L": "Students identify amount of daylight as the external component (it changes with the seasons and we cannot control it) and temperature as the internal response.",
    "lever_E": "Students discover that when daylight increases, temperature increases — a positive relationship.",
    "lever_V": "Students build a simple model connecting amount of daylight to temperature.",
    "lever_Ev": "Students test their model by comparing summer (high daylight) and winter (low daylight) scenarios.",
    "lever_R": "Students reflect on how their model matches their own experience of warm summers and cold winters.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with four-season tree", "say": "What season is it right now? How do you know? What is different about summer, fall, winter, and spring?", "do": "Show the four-season tree image. Students call out what they notice about each season.", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn?", "visual": "Learning goals with season icons", "say": "Today we will learn WHY the seasons change. We will discover the connection between sunlight and temperature.", "do": "Introduce vocabulary: season and daylight. Ask: When is it light outside the longest — summer or winter?", "time": "3 min"},
        {"num": "Slide 3", "title": "Let's Be Scientists!", "visual": "Big question with thermometer graphics", "say": "Why is it hot in summer and cold in winter? What do you think causes the difference?", "do": "Students share their ideas. Record predictions on chart paper to revisit at the end.", "time": "3 min"},
        {"num": "Slide 4", "title": "What Are the Parts?", "visual": "Two component cards with sun and thermometer", "say": "Our model has two parts: Amount of Daylight is how long the sun shines. Temperature is how hot or cold it gets.", "do": "Show a long yellow strip (summer daylight) and a short yellow strip (winter daylight). Ask: Which is warmer?", "time": "5 min"},
        {"num": "Slide 5", "title": "How Are They Connected?", "visual": "Arrow from daylight to temperature", "say": "When there is MORE daylight, the temperature goes UP because the sun warms the Earth longer. More sun means more warmth!", "do": "Students use sentence frame: When daylight goes up, temperature goes up. Draw the positive arrow together.", "time": "5 min"},
        {"num": "Slide 6", "title": "What Did We Find Out?", "visual": "Key discoveries with seasonal photos", "say": "We discovered that the amount of sunlight controls the temperature. Summer has the most sun and is warmest. Winter has the least sun and is coldest.", "do": "Revisit predictions. Show a graph of daylight hours across the year and trace the pattern together.", "time": "5 min"},
        {"num": "Slide 7", "title": "STEM Challenge", "visual": "Season wheel building challenge", "say": "Now build a season wheel that shows how daylight and temperature change! It should spin to show the pattern repeating.", "do": "Distribute paper plates, brass fasteners, and coloring supplies. Students create and present their season wheels.", "time": "10 min"}
    ],
    "sort_reasoning": "Amount of Daylight is external because it is determined by the season and Earth's tilt — we cannot control how many hours the sun shines. Temperature is internal because it changes as a result of how much daylight there is.",
    "relationships": [
        ("Amount of Daylight to Temperature", "POSITIVE (+)", "More hours of sunlight warm the Earth more, raising the temperature. In summer, long days make it hot. In winter, short days mean less warming and colder temperatures.")
    ],
    "sim_answers": [
        ("Summer Days", "When Amount of Daylight is set to very high, Temperature is warm and hot. The sun shines for many hours, giving the Earth lots of time to warm up. This is why summer days feel so hot!"),
        ("Winter Days", "When Amount of Daylight is set to very low, Temperature is cold. The sun only shines for a few hours, so the Earth does not warm up much. This is why winter days feel so cold!")
    ],
    "stem_intro": "Present the challenge: A weather station needs you to design a season wheel that teaches kids about the four seasons. Show how daylight and temperature change in each season. Make your wheel spin to show the pattern repeats every year!",
    "stem_concepts": [
        ("Daylight Drives Temperature", "The number of sunshine hours controls how warm or cold it gets. Summer has the most sun and the most warmth. Winter has the least sun and the least warmth."),
        ("Repeating Pattern", "Seasons always go in the same order: spring, summer, fall, winter. The pattern never changes and it repeats every single year. This is called a cycle.")
    ],
    "stem_eval": [
        ("Expert (4)", "Season wheel shows all four seasons with correct daylight and temperature patterns, and student explains why summer is warmest"),
        ("Proficient (3)", "Season wheel includes all four seasons and student can identify which has the most and least daylight"),
        ("Developing (2)", "Season wheel shows four seasons but student has trouble connecting daylight to temperature"),
        ("Beginning (1)", "Student needs help naming the four seasons or understanding the connection between sun and warmth")
    ],
    "support": [
        "Provide a pre-divided paper plate with season labels so students only need to add details",
        "Use large sun stickers — big sun for summer, small sun for winter — to show daylight differences",
        "Sentence frame: In summer, there is more daylight so the temperature is _______."
    ],
    "extensions": [
        "Interview a family member about their favorite season and what the weather is like during it",
        "Track the temperature outside your school for two weeks — is it going up or down? What season is coming?",
        "Research a place near the equator — do they have the same four seasons? Why or why not?"
    ],
    "cross_curr": [
        ("Math", "Compare daylight hours in summer (about 15) and winter (about 9) — what is the difference?"),
        ("ELA", "Write four sentences, one about each season, describing the weather and what you like to do"),
        ("Art", "Create a four-panel painting of the same outdoor scene in each of the four seasons")
    ],
    "misconceptions": [
        ("Seasons happen because the Earth is closer to the sun in summer", "The Earth's distance from the sun does NOT cause seasons. In fact, Earth is actually slightly closer to the sun during January in the Northern Hemisphere! Seasons are caused by the Earth's tilt, which changes how directly sunlight hits your part of the Earth and how many hours it shines.", "Hold a flashlight straight down on a table (summer — focused light) and then at a steep angle (winter — spread out light). The same amount of light covers more area when tilted, so it feels less warm."),
        ("It is cold in winter because the sun is turned off or weaker", "The sun shines just as strong in winter as in summer! The difference is that in winter, your part of the Earth is tilted away from the sun. The sun is lower in the sky and out for fewer hours, so it has less time to warm the ground. The sun is always powerful — it just reaches us differently in winter.", "Ask: Is the sun still shining on a cold winter day? Yes! Feel the sunshine on your face even in winter. The sun is there, but it is out for fewer hours.")
    ],
    "sentence_frame": "When amount of daylight goes up, temperature goes up.",
    "coloring_description": "Four boxes in a row showing the same tree in each season: spring with flowers and a small sun, summer with full leaves and a big bright sun, fall with orange leaves and a medium sun, winter with bare branches and a tiny sun. A thermometer next to each shows the temperature going up and then back down."
}

L08 = {
    "id": "G01-L08",
    "title": "Can You Send a Message with Light?",
    "subtitle": "The Science of Light Communication",
    "ngss": "1-PS4-4",
    "ngss_desc": "Use tools and materials to design and build a device that uses light or sound to solve the problem of communicating over a distance.",
    "big_question": "How can we use light to send a message to someone far away?",
    "objectives": [
        "Explain that light can be used to send messages",
        "Design a way to communicate using a flashlight",
        "Show that a light signal must be seen by the receiver to work"
    ],
    "vocabulary": [
        ("Signal", "A message sent using light, sound, or movement to tell someone something"),
        ("Communicate", "To share a message or idea with another person, even from far away")
    ],
    "components": [
        ("Signal Brightness", "How bright the light signal is — a bright flash is easier to see than a dim one", True),
        ("Message Received", "Whether the person far away can see and understand the light signal you sent", False)
    ],
    "think_about_it": "If you flash a bright light at someone across the room, can they see it? What about a very dim light?",
    "scenarios": [
        ("Bright Flashlight", "Set Signal Brightness to high and observe if the Message is Received clearly"),
        ("Dim Flashlight", "Set Signal Brightness to low and observe if the Message is Received clearly")
    ],
    "sim_scenarios": [
        ("Bright Flashlight", "Signal Brightness set to high", "What do you predict will happen — will the person receive the message when the light is very bright?"),
        ("Dim Flashlight", "Signal Brightness set to low", "What do you predict will happen — will the person receive the message when the light is very dim?")
    ],
    "discoveries": [
        "Light can be used to send messages to people far away",
        "Brighter signals are easier to see and understand from a distance",
        "The person receiving the message must be able to see the light for communication to work",
        "People have used light signals for hundreds of years, like lighthouses and signal fires"
    ],
    "answer": "Yes, you can send a message with light! When you flash a light on and off in a pattern, the person watching can understand what you mean. Brighter lights work better because they are easier to see from far away. People have been using light to communicate for a very long time — lighthouses warn ships about rocks, traffic lights tell cars when to stop and go, and emergency vehicles flash lights to say 'get out of the way!'",
    "stem_title": "Build a Light Communicator",
    "stem_mission": "Design a device that uses light to send a simple message to a partner across the room.",
    "stem_scenario": "Two friends live on different sides of a valley. They cannot shout loud enough to hear each other. Can you help them design a light communicator so they can send simple messages back and forth? Make a code so they know what the light flashes mean!",
    "stem_questions": [
        "How many flashes will you use for 'yes' and how many for 'no'?",
        "What happens if the light is not bright enough for your partner to see?"
    ],
    "stem_design_qs": [
        "What will you use as your light source?",
        "How will you create different signals for different messages?",
        "How will you make sure your partner can see the light from far away?",
        "What code will you use — how many flashes for each message?"
    ],
    "career": "Telecommunications Engineers design systems that send messages using light, radio waves, and signals. Even internet cables use light! They earn $55,000-$100,000/year.",
    "images": {
        "cover": ("cover-light-message.png", "A dramatic photorealistic image of a lighthouse sending a bright beam of light across dark water at dusk, cinematic lighting, vivid colors"),
        "landscape": ("landscape-light-message.png", "Diverse 1st grade students (6-7 years old, wide variety of ethnicities including Black, Latino, Asian, and white children) using flashlights to signal to partners across a slightly dimmed classroom, excited expressions, editorial photo quality"),
        "modeling": ("modeling-light-message.png", "A simple, colorful kid-friendly diagram showing a flashlight sending light beams to an eye, with flash patterns (on-off-on) shown as dots, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-light-message.png", "A teacher with diverse 1st graders (6-7 years old, wide variety of ethnicities) discussing a poster of different light signals like traffic lights, lighthouse beams, and emergency vehicle lights, bright classroom"),
        "stem": ("stem-light-message.png", "Diverse 1st graders (6-7 years old, wide mix of ethnicities) working in pairs, one flashing a flashlight and the other writing down the message, dimmed classroom with focused expressions")
    },
    "pre_assessment": [
        "Draw a picture of someone sending a message to a friend far away using light.",
        "Circle the things that use light to send a message: a traffic light, a pillow, a lighthouse, a lamp, a shoe."
    ],
    "dimensions": [
        ("Science Practice", "Designing Solutions", "Students design a device that uses light signals to communicate a message over a distance."),
        ("Disciplinary Core Idea", "PS4.C Information Technologies and Instrumentation", "People use devices to send and receive information, including light-based signals."),
        ("Crosscutting Concept", "Cause and Effect", "Students explore how changing signal brightness affects whether a message is successfully received.")
    ],
    "background_intro": "People have been using light to send messages for thousands of years. From ancient signal fires to modern fiber optic cables, light is one of the fastest and most reliable ways to communicate.",
    "background_sections": [
        ("Light as Communication", "Long before telephones or the internet, people used light to send messages over great distances. Ancient warriors lit fires on hilltops to warn of approaching enemies. Lighthouses flash patterns of light to guide ships safely past dangerous rocks. Traffic lights use red, yellow, and green to tell drivers what to do. Even today, the internet sends information as tiny pulses of light through thin glass cables called fiber optics. Light travels very fast, making it perfect for sending messages."),
        ("How Light Signals Work", "For a light signal to work, three things must happen: someone must send the signal, the light must travel to the receiver, and the receiver must be able to see and understand it. Brighter lights can be seen from farther away. A code helps both people understand the message — like one flash means yes and two flashes mean no. If anything blocks the light, like a wall or fog, the message will not get through. That is why lighthouses are built very tall and use very bright lights.")
    ],
    "lever_L": "Students identify signal brightness as the external component we control (how bright the flashlight is) and message received as the internal result (whether the partner gets the message).",
    "lever_E": "Students discover that brighter signals are more likely to be received successfully — a positive relationship.",
    "lever_V": "Students build a simple model showing how signal brightness connects to message received.",
    "lever_Ev": "Students test their model by trying bright and dim flashlights at different distances.",
    "lever_R": "Students reflect on how their model explains why lighthouses need to be so bright and tall.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with lighthouse image", "say": "What if you needed to tell someone something but they were really far away and you could not yell? Could you use LIGHT?", "do": "Show pictures of light signals: traffic lights, lighthouse, emergency vehicles. Ask: What is the light telling us?", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn?", "visual": "Learning goals with signal icons", "say": "Today we will learn how to use light to send messages. We will learn two words: SIGNAL and COMMUNICATE.", "do": "Practice communicating without words: thumbs up, waving, nodding. Say: These are all signals! Light can be a signal too.", "time": "3 min"},
        {"num": "Slide 3", "title": "Let's Be Scientists!", "visual": "Big question with flashlight graphic", "say": "How can we use light to send a message to someone far away? Has anyone ever played with flashlights at night?", "do": "Students share ideas about how they could use light to say something. Record ideas on chart paper.", "time": "3 min"},
        {"num": "Slide 4", "title": "What Are the Parts?", "visual": "Two component cards with flashlight and eye", "say": "Our model has two parts: Signal Brightness is how strong the light is. Message Received is whether the other person sees and understands it.", "do": "Demonstrate with a flashlight: shine it bright, then cover it with a hand to make it dim. Ask: Which is easier to see?", "time": "5 min"},
        {"num": "Slide 5", "title": "How Are They Connected?", "visual": "Arrow from signal brightness to message received", "say": "When the signal is brighter, is the message easier or harder to receive? Brighter means BETTER communication!", "do": "Students use sentence frame: When signal brightness goes up, message received goes up. Draw the connection arrow.", "time": "5 min"},
        {"num": "Slide 6", "title": "What Did We Find Out?", "visual": "Key discoveries with real-world light signal examples", "say": "We discovered that light can carry messages! Brighter signals work better, and people have used light signals for hundreds of years.", "do": "Review discoveries. Show one more example of light communication (fiber optic cable or Morse code lamp).", "time": "5 min"},
        {"num": "Slide 7", "title": "STEM Challenge", "visual": "Light communicator building challenge", "say": "Now work with a partner to create a light code! Decide what one flash, two flashes, and three flashes mean. Then test it!", "do": "Distribute flashlights. Partners move apart and practice sending coded messages. Groups share their codes with the class.", "time": "10 min"}
    ],
    "sort_reasoning": "Signal Brightness is external because we control how bright we make the flashlight — it is our choice. Message Received is internal because it depends on whether the signal was bright enough and clear enough to reach the other person.",
    "relationships": [
        ("Signal Brightness to Message Received", "POSITIVE (+)", "A brighter signal is easier to see from far away, so the message is more likely to be received and understood. Dim signals are hard to see and the message may be lost.")
    ],
    "sim_answers": [
        ("Bright Flashlight", "When Signal Brightness is set to high, Message Received is successful. The bright light is easy to see across the room, and the partner can clearly count the flashes to decode the message."),
        ("Dim Flashlight", "When Signal Brightness is set to low, Message Received is unsuccessful. The dim light is hard to see, especially from far away, and the partner may miss flashes or not see the signal at all.")
    ],
    "stem_intro": "Present the challenge: Two friends live on different sides of a valley and need to send each other messages. They cannot shout that far! Design a light communication system with a code. Decide what different flash patterns mean and test if your partner can receive the message!",
    "stem_concepts": [
        ("Light Travels Far", "Light can travel much farther than sound. A bright flashlight can be seen from very far away, which makes light perfect for sending messages over long distances."),
        ("Codes Make Messages Clear", "A code is a system where certain patterns have certain meanings. One flash might mean yes, two flashes might mean no. Without a code, the receiver would see the light but not understand the message.")
    ],
    "stem_eval": [
        ("Expert (4)", "Light code has at least three messages, partner can receive and decode them, and student explains why brightness matters"),
        ("Proficient (3)", "Light code works for at least two messages and partner can decode most of them"),
        ("Developing (2)", "Light code is created but partner has trouble decoding the messages consistently"),
        ("Beginning (1)", "Student needs help creating a light code or understanding how to flash a pattern")
    ],
    "support": [
        "Provide a pre-made code card: 1 flash = yes, 2 flashes = no, 3 flashes = help",
        "Use a darkened corner of the room so the flashlight signal is easier to see",
        "Sentence frame: I sent _______ flashes, which means _______."
    ],
    "extensions": [
        "Can you send a message with light from one end of the hallway to the other? How bright does the light need to be?",
        "Research how Morse code uses light — try sending your name in Morse code with a flashlight",
        "Design a new code that uses different COLORS of light for different messages"
    ],
    "cross_curr": [
        ("Math", "Count flashes and match numbers to messages — if 2 flashes means no, how many flashes for three no messages?"),
        ("ELA", "Write instructions for your light code so someone else could use it to send messages"),
        ("Art", "Design a colorful poster showing your light code with pictures for each message")
    ],
    "misconceptions": [
        ("You can only communicate by talking", "People communicate in many ways besides talking! Sign language uses hands, Braille uses bumps for reading, traffic lights use colors, and lighthouses use light beams. Light signals are a powerful way to send messages, especially over long distances where voices cannot reach.", "Ask: How does a traffic light tell you what to do? It uses light! No talking needed. Light is a way to communicate."),
        ("Light signals only work at night", "Light signals work during the day too, but they need to be very bright. Traffic lights work perfectly during the day because they use powerful LEDs. At night, even a small flashlight can be seen from far away because the dark background makes the light stand out more.", "Point to a traffic light visible from the window (or show a photo). Ask: Can you see it during the day? Yes! It is a bright light signal that works all the time.")
    ],
    "sentence_frame": "When signal brightness goes up, message received goes up.",
    "coloring_description": "Two children standing far apart — one holding a flashlight pointed at the other. Between them, dotted lines show the light traveling. The child receiving the signal has a big smile and is holding up a card that says the message. A lighthouse is in the background."
}

L09 = {
    "id": "G01-L09",
    "title": "How Do Plants Grow from Seeds?",
    "subtitle": "The Science of the Plant Life Cycle",
    "ngss": "1-LS1-1",
    "ngss_desc": "Use materials to design a solution to a human problem by mimicking how plants and animals use their external parts to help them survive, grow, and meet their needs.",
    "big_question": "How does a tiny seed turn into a big plant?",
    "objectives": [
        "Describe the stages of a plant growing from a seed",
        "Explain what a seed needs to start growing",
        "Show how water helps a seed sprout and a plant grow tall"
    ],
    "vocabulary": [
        ("Seed", "A tiny package that holds a baby plant inside along with food to help it start growing"),
        ("Sprout", "When a baby plant first pushes out of the seed and pokes through the soil")
    ],
    "components": [
        ("Water Amount", "How much water the seed or plant gets — plants need water to grow but not too much", True),
        ("Plant Growth", "How tall and healthy the plant grows — more water means more growth, up to a point", False)
    ],
    "think_about_it": "What do you think will happen to a seed if you give it water every day? What if you never give it water?",
    "scenarios": [
        ("Watered Every Day", "Set Water Amount to just right and observe how Plant Growth changes over time"),
        ("No Water at All", "Set Water Amount to zero and observe what happens to Plant Growth")
    ],
    "sim_scenarios": [
        ("Watered Every Day", "Water Amount set to regular watering", "What do you predict will happen to Plant Growth when the seed gets water every day?"),
        ("No Water at All", "Water Amount set to zero", "What do you predict will happen to Plant Growth when the seed gets no water at all?")
    ],
    "discoveries": [
        "Seeds need water, sunlight, and soil to start growing",
        "A plant grows from seed to sprout to a full plant with leaves and sometimes flowers",
        "Water is very important for plant growth — without it, the plant will not survive",
        "Plants grow taller and stronger when they get the right amount of water"
    ],
    "answer": "A tiny seed turns into a big plant by going through stages! First, the seed absorbs water and the baby plant inside starts to grow. Then a tiny sprout pushes up through the soil toward the sunlight. The sprout grows a stem, then leaves, and eventually it can become a big plant with flowers or fruit. Water is super important — it helps the plant grow at every stage. Without water, the seed will just sit there and nothing will happen!",
    "stem_title": "Design a Seed Starter Garden",
    "stem_mission": "Build a mini garden that gives seeds the best chance to sprout and grow by providing water, light, and good soil.",
    "stem_scenario": "Your school wants to start a garden but needs to figure out the best way to grow seeds. Design a mini garden in a cup that gives your seed everything it needs to grow. Track how it changes each day!",
    "stem_questions": [
        "What three things does your seed need to start growing?",
        "How will you know when your seed has sprouted?"
    ],
    "stem_design_qs": [
        "What kind of container will you use for your mini garden?",
        "How much water will you give your seed each day?",
        "Where will you put your garden so it gets sunlight?",
        "How will you record your plant's growth each day?"
    ],
    "career": "Botanists study plants and help farmers grow healthier crops. They work in gardens, farms, and laboratories to discover how to grow better food. They earn $45,000-$85,000/year.",
    "images": {
        "cover": ("cover-plant-growth.png", "A beautiful photorealistic close-up of a green sprout just emerging from dark soil with water droplets on its leaves, warm sunlight streaming in, shallow depth of field, cinematic nature photography"),
        "landscape": ("landscape-plant-growth.png", "Diverse 1st grade students (6-7 years old, wide variety of ethnicities including Black, Latino, Asian, and white children) planting seeds in small cups filled with soil, bright modern classroom with plants on the windowsill, natural window light, editorial photo quality"),
        "modeling": ("modeling-plant-growth.png", "A simple, colorful kid-friendly diagram showing the stages of plant growth from seed to sprout to small plant to tall plant with flowers, left to right with arrows between stages, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-plant-growth.png", "A teacher with diverse 1st graders (6-7 years old, wide variety of ethnicities) gathered around a table with sprouting seeds in clear cups, students peering at the roots and tiny green leaves, bright classroom"),
        "stem": ("stem-plant-growth.png", "Diverse 1st graders (6-7 years old, wide mix of ethnicities) watering their mini cup gardens and measuring sprout height with rulers, growth tracking charts on their desks, sunny modern classroom")
    },
    "pre_assessment": [
        "Draw what you think is inside a seed. Show what happens when you put it in soil and add water.",
        "Circle what a seed needs to grow: water, candy, sunlight, soil, a hat, air."
    ],
    "dimensions": [
        ("Science Practice", "Planning and Carrying Out Investigations", "Students plant seeds and investigate how water affects plant growth over time."),
        ("Disciplinary Core Idea", "LS1.A Structure and Function", "Plants have different parts that help them survive, grow, and make more plants."),
        ("Crosscutting Concept", "Cause and Effect", "Students explore how providing or withholding water causes plants to grow or not grow.")
    ],
    "background_intro": "Every plant on Earth started as a tiny seed. Inside each seed is a baby plant waiting for the right conditions to start growing. Understanding how seeds grow helps us grow food and take care of our planet.",
    "background_sections": [
        ("What a Seed Needs", "A seed is like a tiny survival kit. Inside it is a baby plant and a small amount of food to get it started. But the seed will not grow unless it gets three things from the outside: water, warmth, and eventually sunlight. When a seed absorbs water, it swells up and the hard outer coat softens. The baby plant inside begins to grow, sending a root down into the soil and a tiny stem up toward the light. This process is called germination."),
        ("Stages of Plant Growth", "After the seed germinates, the plant goes through several stages. First, a small sprout appears above the soil — this is called a seedling. The seedling grows a stem and its first leaves, which capture sunlight to make food through a process called photosynthesis. As the plant gets more sunlight, water, and nutrients from the soil, it grows taller and stronger. Eventually, many plants produce flowers, which can make seeds of their own. Then the cycle starts all over again!")
    ],
    "lever_L": "Students identify water amount as the external component they control (how much they water the plant) and plant growth as the internal result that changes.",
    "lever_E": "Students discover that when water amount goes up (to a point), plant growth goes up — a positive relationship.",
    "lever_V": "Students build a simple model showing how water amount connects to plant growth.",
    "lever_Ev": "Students test their model by comparing a watered seed to an unwatered seed and observing the difference.",
    "lever_R": "Students reflect on how their model explains why farmers water their crops and gardeners tend their plants.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with sprouting seed close-up", "say": "Look at this tiny green sprout! It used to be just a little seed. How did it change? How does a seed know how to grow?", "do": "Pass around some dry seeds. Ask: What do you think is inside this tiny thing? Could a whole plant really come from this?", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn?", "visual": "Learning goals with plant stage pictures", "say": "Today we will learn how a tiny seed becomes a big plant. We will learn the word SPROUT — that is when the baby plant first pokes out of the seed.", "do": "Show real sprouted seeds (or photos). Say: This is what a sprout looks like! It started as a seed just like the ones you are holding.", "time": "3 min"},
        {"num": "Slide 3", "title": "Let's Be Scientists!", "visual": "Big question with seed-to-plant sequence", "say": "How does a tiny seed turn into a big plant? What does the seed need to start growing?", "do": "Think-pair-share. Students list what they think seeds need. Write ideas on the board.", "time": "3 min"},
        {"num": "Slide 4", "title": "What Are the Parts?", "visual": "Two component cards with water and plant icons", "say": "Our model has two parts: Water Amount is how much water we give the seed. Plant Growth is how tall and healthy the plant becomes.", "do": "Show two cups of soil with seeds — add water to one, leave the other dry. Say: We will check these every day!", "time": "5 min"},
        {"num": "Slide 5", "title": "How Are They Connected?", "visual": "Arrow from water to growth", "say": "When we give the seed water, what do you think will happen? Will it grow or stay the same?", "do": "Students use sentence frame: When water amount goes up, plant growth goes up. Draw the positive arrow together.", "time": "5 min"},
        {"num": "Slide 6", "title": "What Did We Find Out?", "visual": "Key discoveries with growth photos", "say": "We found out that seeds need water to grow! The water helps the baby plant inside the seed wake up and start growing into a sprout.", "do": "Show time-lapse video or photos of a seed growing. Compare watered vs. unwatered results.", "time": "5 min"},
        {"num": "Slide 7", "title": "STEM Challenge", "visual": "Seed starter garden challenge", "say": "Now plant your OWN seed garden! Give it water, put it near sunlight, and track how it grows each day.", "do": "Distribute cups, soil, seeds, water. Students plant seeds and create a growth tracking chart to fill in daily.", "time": "10 min"}
    ],
    "sort_reasoning": "Water Amount is external because we decide how much water to give the plant — it is our choice and we control it. Plant Growth is internal because it changes based on how much water the seed gets.",
    "relationships": [
        ("Water Amount to Plant Growth", "POSITIVE (+)", "When a plant gets the right amount of water, it grows taller and healthier. Water helps the seed germinate and gives the plant what it needs to grow strong stems and green leaves.")
    ],
    "sim_answers": [
        ("Watered Every Day", "When Water Amount is set to regular watering, Plant Growth increases over time. The seed absorbs the water, sprouts within a few days, and grows into a healthy green plant with leaves."),
        ("No Water at All", "When Water Amount is set to zero, Plant Growth stays at zero. The seed sits in dry soil and nothing happens because without water, the baby plant inside cannot start growing.")
    ],
    "stem_intro": "Present the challenge: Your school wants to start a garden! Plant a seed in a cup and give it everything it needs to grow. Water it, put it in sunlight, and track how tall it gets each day. Who can grow the tallest sprout?",
    "stem_concepts": [
        ("Seeds Need Water", "Water is the key that starts seed growth. When a seed absorbs water, the baby plant inside wakes up and starts pushing roots down and a stem up. Without water, nothing happens."),
        ("Growth Takes Time", "Plants do not grow overnight. It takes days for a seed to sprout and weeks for it to become a full plant. Be patient and keep watering — your plant is growing even when you cannot see it yet!")
    ],
    "stem_eval": [
        ("Expert (4)", "Seed is properly planted with water and sunlight, student tracks growth daily, and explains that water causes the seed to sprout"),
        ("Proficient (3)", "Seed is planted and watered, and student can explain that seeds need water to grow"),
        ("Developing (2)", "Seed is planted but student has trouble explaining why water is needed or tracking growth"),
        ("Beginning (1)", "Student needs help planting the seed or understanding what it needs to grow")
    ],
    "support": [
        "Use clear plastic cups so students can see the roots growing even before the sprout appears above soil",
        "Provide a simple picture chart for students to draw their plant each day instead of writing",
        "Sentence frame: My seed needs _______ to grow. Today my plant looks _______."
    ],
    "extensions": [
        "What happens if you give a seed WAY too much water? Try it and see! Can a plant get too much water?",
        "Plant the same kind of seed in a sunny spot and a dark spot — which grows better?",
        "Research the biggest seed in the world (coconut!) — does it need the same things to grow as your tiny seed?"
    ],
    "cross_curr": [
        ("Math", "Measure your plant's height each day with a ruler and record the numbers on a chart — is it getting taller?"),
        ("ELA", "Write a diary from the seed's point of view: Day 1, I am a tiny seed in dark soil. Day 5, I feel myself growing!"),
        ("Art", "Draw the four stages of your plant's life: seed, sprout, small plant, big plant with flowers")
    ],
    "misconceptions": [
        ("Seeds are not alive", "Seeds are alive, just sleeping! Inside every seed is a tiny baby plant that is waiting for water and warmth to wake up and start growing. When conditions are right, the seed comes to life and begins to grow. If seeds were not alive, they could never become plants.", "Put a dry seed and a watered seed side by side. Wait a few days. The watered seed sprouts! Ask: Could it do that if it were not alive?"),
        ("Plants eat soil to grow", "Plants do not eat soil. They get nutrients from the soil through their roots, but most of their food comes from SUNLIGHT. Plants use sunlight, water, and air to make their own food in their leaves. Soil gives them a place to stand and some minerals, but the sun is their main food source.", "Ask: If plants eat soil, why does the soil not disappear? Because plants make their own food from sunlight and water — the soil just holds them up and provides some extra nutrients!")
    ],
    "sentence_frame": "When water amount goes up, plant growth goes up.",
    "coloring_description": "A row of four cups showing the stages of a seed growing: Cup 1 has a seed buried in soil with a watering can above. Cup 2 shows a tiny sprout poking up. Cup 3 shows a small plant with two leaves. Cup 4 shows a tall plant with a flower on top. A smiling sun shines above all four cups."
}

L10 = {
    "id": "G01-L10",
    "title": "What Makes a Shadow?",
    "subtitle": "The Science of Light and Shadows",
    "ngss": "1-PS4-3",
    "ngss_desc": "Plan and conduct investigations to determine the effect of placing objects made with different materials in the path of a beam of light.",
    "big_question": "What makes a shadow appear, and why do shadows change shape?",
    "objectives": [
        "Explain that shadows are made when an object blocks light",
        "Show that shadows change size when the light source moves",
        "Predict where a shadow will appear based on where the light is"
    ],
    "vocabulary": [
        ("Shadow", "A dark shape that appears when something blocks the light from getting through"),
        ("Light Source", "The thing that makes light, like the sun, a flashlight, or a lamp")
    ],
    "components": [
        ("Light Position", "Where the light source is compared to the object — close, far, high, or low", True),
        ("Shadow Size", "How big or small the shadow is on the ground or wall", False)
    ],
    "think_about_it": "When you hold a flashlight close to a toy, is the shadow bigger or smaller than when the flashlight is far away?",
    "scenarios": [
        ("Light Close to Object", "Set Light Position to close to the object and observe the Shadow Size"),
        ("Light Far from Object", "Set Light Position to far from the object and observe the Shadow Size")
    ],
    "sim_scenarios": [
        ("Light Close to Object", "Light Position set to close to the object", "What do you predict will happen to Shadow Size when the light is very close to the object?"),
        ("Light Far from Object", "Light Position set to far from the object", "What do you predict will happen to Shadow Size when the light is far away from the object?")
    ],
    "discoveries": [
        "Shadows appear when an object blocks light from passing through",
        "When the light is closer to the object, the shadow gets bigger",
        "When the light is farther from the object, the shadow gets smaller",
        "Shadows always appear on the opposite side of the object from the light"
    ],
    "answer": "A shadow appears when something blocks the light! Light travels in straight lines, so when it hits an opaque object, the light cannot get through. Behind the object, there is a dark area where the light cannot reach — that is the shadow! Shadows change size depending on where the light is. When the light is close to the object, the shadow is BIG. When the light is far away, the shadow is SMALLER. That is why your shadow is long in the morning and short at noon!",
    "stem_title": "Shadow Puppet Show",
    "stem_mission": "Design shadow puppets and use a flashlight to put on a short shadow puppet show for the class.",
    "stem_scenario": "Your class is hosting a shadow puppet theater! Cut out fun shapes from cardboard, attach them to sticks, and figure out how to make big shadows and small shadows on the wall. Use what you learned about light and distance!",
    "stem_questions": [
        "How can you make your puppet's shadow really big on the wall?",
        "How can you make it really small?"
    ],
    "stem_design_qs": [
        "What shapes will you cut out for your shadow puppets?",
        "How will you hold your puppets between the light and the wall?",
        "How close should the light be to make the biggest shadow?",
        "Can you make your puppet's shadow move and tell a story?"
    ],
    "career": "Lighting Designers create the perfect lighting for movies, theater shows, and concerts. They use lights and shadows to make scenes look amazing. They earn $40,000-$85,000/year.",
    "images": {
        "cover": ("cover-shadows.png", "A dramatic photorealistic image of a child making a shadow puppet on a wall with a flashlight, the shadow clearly visible and larger than the hand making it, warm moody lighting, cinematic"),
        "landscape": ("landscape-shadows.png", "Diverse 1st grade students (6-7 years old, wide variety of ethnicities including Black, Latino, Asian, and white children) playing with flashlights and making shadows on a white wall in a slightly darkened classroom, laughing and excited, editorial photo quality"),
        "modeling": ("modeling-shadows.png", "A simple, colorful kid-friendly diagram showing a flashlight, an object blocking the light, and a shadow behind the object on a wall, with labeled arrows showing light direction, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-shadows.png", "A teacher with diverse 1st graders (6-7 years old, wide variety of ethnicities) looking at shadows created by toy dinosaurs on a table, flashlight shining from the side, students tracing the shadows with their fingers"),
        "stem": ("stem-shadows.png", "Diverse 1st graders (6-7 years old, wide mix of ethnicities) performing a shadow puppet show with cardboard cutouts on sticks, a bright flashlight behind them creating large shadows on a white sheet, wonder and delight on their faces")
    },
    "pre_assessment": [
        "Draw yourself standing outside in the sun with your shadow. Where is the shadow?",
        "Circle what you need to make a shadow: light, an object that blocks light, darkness behind the object, a sandwich."
    ],
    "dimensions": [
        ("Science Practice", "Planning and Carrying Out Investigations", "Students investigate how changing the position of a light source affects the size and shape of shadows."),
        ("Disciplinary Core Idea", "PS4.B Electromagnetic Radiation", "Objects can be seen only when light is available to illuminate them; some materials block light and create shadows."),
        ("Crosscutting Concept", "Cause and Effect", "Students explore how changing the light position causes the shadow size to change.")
    ],
    "background_intro": "Shadows are everywhere! Every time light hits an object that blocks it, a shadow is created. Understanding shadows helps us learn how light works and how it travels.",
    "background_sections": [
        ("How Shadows Form", "Light travels in straight lines. When light hits a transparent material like glass, it passes right through. But when light hits an opaque material like cardboard or your body, it cannot get through. The area behind the object is dark because the light is blocked — this dark area is a shadow. Every shadow needs three things: a light source, an object to block the light, and a surface for the shadow to fall on. Without any one of these three, you cannot make a shadow."),
        ("Why Shadows Change Size", "The size of a shadow depends on where the light source is. When the light is CLOSE to the object, the shadow is very BIG because the object blocks a large portion of the light. When the light is FAR from the object, the shadow is SMALLER because the object blocks a smaller portion of the total light. You can see this in real life — your shadow is very long early in the morning when the sun is low and close to the horizon, and very short at noon when the sun is high overhead. Shadow puppeteers use this trick to make their puppets look huge on the wall!")
    ],
    "lever_L": "Students identify light position as the external component they control (moving the flashlight closer or farther) and shadow size as the internal result that changes.",
    "lever_E": "Students discover that when the light gets closer, the shadow gets bigger — and when the light moves away, the shadow gets smaller.",
    "lever_V": "Students build a simple model showing how light position connects to shadow size.",
    "lever_Ev": "Students test their model by moving a flashlight closer and farther from an object and measuring the shadow.",
    "lever_R": "Students reflect on how their model explains why shadows are long in the morning and short at noon.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic shadow puppet image", "say": "Have you ever made a shadow puppet on the wall? How did you do it? What did you need?", "do": "Turn off some lights and use a flashlight to make a shadow on the wall. Ask: What three things do we need to make a shadow?", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn?", "visual": "Learning goals with shadow examples", "say": "Today we will learn what makes shadows and why they change size! We will learn two words: SHADOW and LIGHT SOURCE.", "do": "Ask: What are some light sources you know? (sun, flashlight, lamp) Practice saying shadow and light source together.", "time": "3 min"},
        {"num": "Slide 3", "title": "Let's Be Scientists!", "visual": "Big question with shadow photographs", "say": "What makes a shadow appear, and why do shadows change shape? Have you noticed your shadow looks different at different times?", "do": "If possible, go outside briefly and observe shadows. Or show photos of shadows at morning vs. noon.", "time": "3 min"},
        {"num": "Slide 4", "title": "What Are the Parts?", "visual": "Two component cards with flashlight and shadow", "say": "Our model has two parts: Light Position is where we put the flashlight. Shadow Size is how big the shadow gets.", "do": "Place a toy on a table. Shine a flashlight from different positions. Ask: What happens to the shadow?", "time": "5 min"},
        {"num": "Slide 5", "title": "How Are They Connected?", "visual": "Diagram showing light close vs. far and shadow sizes", "say": "When the light moves closer, does the shadow get bigger or smaller? Closer means BIGGER! Can anyone tell me why?", "do": "Let students move the flashlight closer and farther to see the effect. Use sentence frame for the connection.", "time": "5 min"},
        {"num": "Slide 6", "title": "What Did We Find Out?", "visual": "Key discoveries with shadow examples", "say": "We learned that shadows happen when something blocks light. The closer the light, the bigger the shadow. The farther the light, the smaller the shadow.", "do": "Review all discoveries. Challenge students: Can you make a shadow with a clear cup? (No! Light goes through it.)", "time": "5 min"},
        {"num": "Slide 7", "title": "STEM Challenge", "visual": "Shadow puppet theater challenge", "say": "Time for a shadow puppet show! Cut out shapes, attach them to sticks, and put on a show. Make your puppets look big and small!", "do": "Distribute cardboard, scissors, popsicle sticks, tape, and flashlights. Students create shadow puppets and perform short shows.", "time": "10 min"}
    ],
    "sort_reasoning": "Light Position is external because we control where we place the flashlight — we move it closer or farther. Shadow Size is internal because it changes automatically depending on where the light is positioned.",
    "relationships": [
        ("Light Position to Shadow Size", "POSITIVE (+)", "When the light moves closer to the object, the shadow gets bigger because the object blocks a larger area of the light. Moving the light farther away makes the shadow smaller.")
    ],
    "sim_answers": [
        ("Light Close to Object", "When Light Position is set to close, Shadow Size is very large. The flashlight is near the object, so the object blocks a big area of light, creating a huge shadow on the wall behind it."),
        ("Light Far from Object", "When Light Position is set to far, Shadow Size is small. The flashlight is far from the object, so the object only blocks a small area of the total light, making a smaller, more focused shadow.")
    ],
    "stem_intro": "Present the challenge: Your class is hosting a shadow puppet theater! Cut out fun shapes from cardboard, tape them to sticks, and use a flashlight to make shadow puppets on the wall. Figure out how to make your puppet look huge and how to make it small!",
    "stem_concepts": [
        ("Blocking Light Creates Shadows", "When something stands in the way of light, a shadow appears behind it. Your cardboard puppet blocks the flashlight beam and makes a dark shape on the wall."),
        ("Distance Changes Shadow Size", "Move the flashlight closer to your puppet to make a giant shadow. Move it farther away to make a small shadow. Shadow puppet experts use this trick to make their shows exciting!")
    ],
    "stem_eval": [
        ("Expert (4)", "Shadow puppets create clear shadows, student can make them bigger and smaller on command, and explains why distance matters"),
        ("Proficient (3)", "Shadow puppets work and student can demonstrate making the shadow bigger or smaller"),
        ("Developing (2)", "Shadow puppets create shadows but student has trouble explaining why the shadow size changes"),
        ("Beginning (1)", "Student needs help creating shadow puppets or understanding how to make shadows")
    ],
    "support": [
        "Pre-cut some simple puppet shapes for students who need help with scissors",
        "Mark two spots on the floor: CLOSE (big shadow) and FAR (small shadow) so students can test both",
        "Sentence frame: When the light is close, the shadow is _______. When the light is far, the shadow is _______."
    ],
    "extensions": [
        "Go outside at three different times during the day and trace your shadow — how does it change?",
        "Can you make a shadow disappear? What would you need to do? (Hint: use a transparent object!)",
        "Research how sundials use shadows to tell time — can you make one?"
    ],
    "cross_curr": [
        ("Math", "Measure the shadow of the same object with the light at three different distances and compare the sizes"),
        ("ELA", "Write a short story that your shadow puppets can act out during the shadow puppet show"),
        ("Art", "Trace your shadow on large paper and decorate it with colors and patterns")
    ],
    "misconceptions": [
        ("Shadows are alive or are part of you", "Shadows are not alive and they are not a piece of you. A shadow is just a dark area where light cannot reach because your body is blocking it. If you move, the shadow moves because the blocked area moves. If the light goes away, the shadow disappears completely.", "Turn on and off a flashlight aimed at a toy. Ask: Where did the shadow go? Did it run away? No! It disappeared because the light turned off. Shadows only exist when there is light to block."),
        ("Dark objects make darker shadows than light objects", "The color of an object does not change how dark a shadow is. A white ball and a black ball both make the same shadow because shadows are created by BLOCKING light, not by color. What matters is whether the object is opaque — whether it blocks light. A clear object makes no shadow at all, regardless of its color.", "Shine a flashlight at a white piece of paper and then a black piece of paper. Compare the shadows. They look the same! Then try a clear sheet of plastic — no shadow!")
    ],
    "sentence_frame": "When the light is closer, the shadow size goes up.",
    "coloring_description": "A child holding a cardboard butterfly on a stick between a flashlight and a wall. On the wall, a big butterfly shadow appears. Dotted lines from the flashlight show how the light is blocked by the cardboard and creates the dark shadow behind it."
}

ALL_LESSONS = [L01, L02, L03, L04, L05, L06, L07, L08, L09, L10]
