#!/usr/bin/env python3
"""Complete lesson data for G03-L01 through G03-L10 (Grade 3 ModelIt! Lessons)"""

L01 = {
    "id": "G03-L01",
    "title": "Why Do Magnets Stick?",
    "subtitle": "Exploring Magnetic Forces and Fields",
    "ngss": "3-PS2-3",
    "ngss_desc": "Ask questions to determine cause and effect relationships of electric or magnetic interactions between two objects not in contact with each other.",
    "big_question": "Why do magnets stick to some things but not others?",
    "objectives": [
        "Explain how magnets pull on certain metals without touching them",
        "Model how magnet strength, magnetic force, and attraction are connected",
        "Describe why magnets stick to some objects but not others"
    ],
    "vocabulary": [
        ("Magnet", "A special object that can push or pull certain metals without touching them"),
        ("Magnetic Force", "The invisible push or pull that a magnet makes around itself"),
        ("Attract", "When a magnet pulls something toward it — like a fridge magnet sticking to a fridge")
    ],
    "components": [
        ("Magnet Strength", "How powerful the magnet is — bigger or stronger magnets pull harder", True),
        ("Magnetic Force", "The invisible pulling power between a magnet and a metal object", False),
        ("Attraction", "Whether the object sticks to the magnet or not — only certain metals are attracted", False)
    ],
    "think_about_it": "When magnet strength increases, what happens to magnetic force? Is the relationship positive or negative?",
    "scenarios": [
        ("Weak Magnet", "Set Magnet Strength to low and observe what happens to Magnetic Force and Attraction"),
        ("Strong Magnet", "Set Magnet Strength to maximum and observe how Magnetic Force and Attraction change"),
        ("Medium Magnet", "Set Magnet Strength to 50% and compare it to the weak and strong magnet")
    ],
    "sim_scenarios": [
        ("Weak Magnet", "Magnet Strength set to low", "What do you predict will happen to Attraction when the magnet is weak?"),
        ("Strong Magnet", "Magnet Strength set to maximum", "What do you predict will happen to Magnetic Force when the magnet is very strong?"),
        ("Medium Magnet", "Magnet Strength set to 50%", "Will the magnetic force be exactly halfway between the weak and strong magnet?")
    ],
    "discoveries": [
        "Stronger magnets create a stronger magnetic force that can pull from farther away",
        "Magnets only attract certain metals like iron, nickel, and cobalt — not plastic, wood, or paper",
        "Magnetic force can work through air without the magnet touching the object",
        "The closer a magnet gets to a metal object, the stronger the pull feels"
    ],
    "answer": "Magnets stick to some things because of an invisible force called magnetic force! Magnets create a special field around them that can pull on metals like iron and steel. Stronger magnets make a bigger invisible field that pulls harder. But magnets cannot pull on everything — only certain metals have the right stuff inside to feel the magnetic force. That is why a magnet sticks to your fridge but not to a wooden table!",
    "stem_title": "Design a Magnetic Sorting Machine",
    "stem_mission": "Design a tool that uses magnets to sort metal objects from non-metal objects, like a recycling helper.",
    "stem_scenario": "A recycling center needs help sorting metal cans from plastic bottles and paper. Your team must design a magnetic sorting tool that can quickly pick up metal items without picking up non-metal items. Use what you learned about magnetic force to make your design!",
    "stem_questions": [
        "How strong does your magnet need to be to pick up the metal objects?",
        "Why does your magnet only pick up some things and not others?",
        "How could you sort a mixed pile of objects using only your magnet?"
    ],
    "stem_design_qs": [
        "What type of magnet will you use — a bar magnet, a horseshoe magnet, or a disk magnet?",
        "How will you attach the magnet to a handle so you can move it over the pile?",
        "What objects will you test to prove your sorter works?",
        "How will you make your sorter work faster for a really big pile?"
    ],
    "career": "Materials Scientists study what things are made of and why they behave the way they do, including magnetic materials. They earn $60,000-$105,000/year.",
    "images": {
        "cover": ("cover-magnets.png", "A close-up photorealistic image of a colorful horseshoe magnet attracting shiny metal paperclips and small iron filings, showing the invisible magnetic field lines made visible with iron filings on a white surface, dramatic lighting"),
        "landscape": ("landscape-magnets.png", "Diverse 3rd grade students (8-9 years old, wide variety of ethnicities including Black, Latino, Asian, and white children with natural hairstyles) excitedly testing magnets on different objects at their desks in a bright modern classroom, natural window light, editorial photo quality"),
        "modeling": ("modeling-magnets.png", "A colorful kid-friendly scientific diagram showing a magnet surrounded by invisible force field lines pulling on a metal paperclip, with arrows showing the direction of magnetic force, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-magnets.png", "A teacher with diverse 3rd graders (8-9 years old, wide variety of ethnicities with natural hairstyles) gathered on a colorful rug, holding magnets and testing them on different materials, animated conversation, bright classroom"),
        "stem": ("stem-magnets.png", "Diverse 3rd graders (8-9 years old, wide mix of ethnicities including Black, Latino, Asian children) building magnetic sorting tools from craft sticks and magnets, testing on piles of mixed materials at tables, collaborative and excited")
    },
    "pre_assessment": [
        "Have you ever played with a magnet? What happened when you put it near different things?",
        "Why do you think magnets stick to the refrigerator but not to a wooden door?",
        "Draw what you think is happening between a magnet and a paperclip when the magnet pulls it."
    ],
    "reflections": [
        "How does magnetic force work even when the magnet is not touching the object?",
        "How did your model help you understand why magnets only stick to certain things?"
    ],
    "reflection_exemplars": [
        ("How does magnetic force work even when the magnet is not touching the object?", "Magnets create an invisible field of force around them. This magnetic field reaches out through the air and pulls on metals like iron and steel. The stronger the magnet, the farther the field reaches. It is like how you can feel the warmth of a campfire without touching it — the heat reaches out to you through the air. Magnetic force reaches out the same way!")
    ],
    "cast_items": [
        "Explain how magnet strength affects the magnetic force on a nearby metal object",
        "Use a model to describe why magnets attract some objects but not others",
        "Describe how distance affects the strength of a magnetic pull"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student holds a magnet near a paperclip, a wooden block, and a plastic cup. Only the paperclip moves toward the magnet. Which best explains why?"),
        ("Constructed Response:", "Using what you know about magnetic force, explain why a strong magnet can pick up a paperclip from farther away than a weak magnet can. Use the words 'magnet strength' and 'magnetic force' in your answer.")
    ],
    "extend_components": [
        ("Distance", "How far the magnet is from the metal object — magnetic force gets weaker when the magnet is farther away"),
        ("Object Material", "What the object is made of — only metals like iron, nickel, and cobalt are attracted to magnets")
    ],
    "dimensions": [
        ("Science Practice", "Asking Questions and Defining Problems", "Students ask questions about why magnets interact with some materials and not others, and investigate cause and effect relationships in magnetic systems."),
        ("Disciplinary Core Idea", "PS2.B Types of Interactions", "Electric and magnetic forces between a pair of objects do not require that the objects be in contact. The sizes of the forces in each situation depend on the properties of the objects and their distances apart."),
        ("Crosscutting Concept", "Cause and Effect", "Students investigate how changing magnet strength (cause) affects magnetic force and attraction (effects) in a predictable pattern.")
    ],
    "background_intro": "Magnetism is one of nature's most fascinating forces. It is invisible, acts at a distance, and has been used by humans for thousands of years — from ancient compasses to modern electric motors and MRI machines in hospitals.",
    "background_sections": [
        ("What Is a Magnet?", "A magnet is an object that produces an invisible magnetic field around itself. This field can attract (pull toward) or repel (push away) other magnets and certain metals. Every magnet has two poles — a north pole and a south pole. Opposite poles attract each other, while same poles repel. The magnetic field is strongest at the poles."),
        ("Why Do Magnets Attract Some Things?", "Magnets only attract metals that contain iron, nickel, or cobalt. Inside these metals, tiny groups of atoms called magnetic domains can line up in the same direction when a magnet is nearby. When the domains line up, the metal becomes temporarily magnetic itself and is pulled toward the magnet. Materials like wood, plastic, and glass do not have magnetic domains, so magnets have no effect on them."),
        ("Magnetic Force and Distance", "Magnetic force follows an important rule: the closer the magnet is to the object, the stronger the pull. As the distance doubles, the force drops dramatically. A strong magnet might pick up a paperclip from two inches away, but at four inches, the force may be too weak. This is why you have to get a fridge magnet close to the fridge for it to stick — the force needs to be strong enough to hold it up against gravity.")
    ],
    "lever_L": "Students identify magnet strength as an external component and magnetic force and attraction as internal components that change in response to how powerful the magnet is.",
    "lever_E": "Students determine that magnet strength positively affects magnetic force, and magnetic force positively affects attraction — creating a direct chain of cause and effect.",
    "lever_V": "Students build a model showing how increasing magnet strength leads to greater magnetic force and stronger attraction to metal objects.",
    "lever_Ev": "Students run weak magnet, medium magnet, and strong magnet scenarios to observe how changing one input (strength) affects the entire system.",
    "lever_R": "Students add distance or object material to explore why magnets work better up close and only on certain metals.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with colorful magnets and metal objects", "say": "Who has ever put a magnet on the refrigerator? Did you ever wonder HOW it sticks up there without falling?", "do": "Pass out magnets and let students test them on their desks, pencils, and zippers for 30 seconds.", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn Today?", "visual": "Learning goals and vocabulary words", "say": "Today we are going to figure out the mystery of magnets — why they stick to some things but not others!", "do": "Read objectives together. Introduce vocabulary with a quick demo: hold a magnet near a paperclip and ask what force is acting.", "time": "3 min"},
        {"num": "Slide 3", "title": "The Big Question", "visual": "Image of magnet near different materials", "say": "Here is our big question: why does a magnet grab a paperclip but totally ignore a pencil?", "do": "Have students turn and talk with a partner: What do YOU think makes a magnet stick to some things? Collect ideas on the board.", "time": "3 min"},
        {"num": "Slide 4", "title": "Let's Build a Model!", "visual": "LEVER steps overview for kids", "say": "We are going to build a model to solve this magnet mystery — step by step, like real scientists!", "do": "Preview each LEVER step briefly. Remind students that a model helps us understand how things work.", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Sort the Parts", "visual": "Component cards for the magnet model", "say": "What parts of the magnet system can we identify? What can we control, and what happens on its own?", "do": "Guide sorting of three components. Explain that magnet strength is external because WE choose which magnet to use.", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect with Arrows", "visual": "Arrow diagrams between components", "say": "When we use a stronger magnet, does the pulling force go up or down? Let us draw our arrows!", "do": "Help students draw positive arrows from magnet strength to magnetic force, and from magnetic force to attraction.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Run the Simulation!", "visual": "Simulation predictions and results graphs", "say": "Time to test our model! Let us start with a weak magnet and see what happens.", "do": "Have students predict first, then run each scenario. Compare weak vs. medium vs. strong magnet results on the graph.", "time": "8 min"},
        {"num": "Slide 8", "title": "What Did We Discover?", "visual": "Key findings summary with magnet images", "say": "Now we know the secret — magnets have an invisible force that only works on certain metals!", "do": "Summarize findings. Demo: sprinkle iron filings around a magnet to make the invisible field visible. Students draw what they see.", "time": "7 min"}
    ],
    "sort_reasoning": "Magnet Strength is external because it depends on which magnet we choose to use — it is decided before the experiment begins. Magnetic Force and Attraction are internal because they are results that happen INSIDE the system when the magnet interacts with an object.",
    "relationships": [
        ("Magnet Strength to Magnetic Force", "POSITIVE (+)", "A stronger magnet creates a bigger invisible field with more pulling power. When you switch from a weak magnet to a strong one, the magnetic force increases — you can feel the pull get stronger."),
        ("Magnetic Force to Attraction", "POSITIVE (+)", "When the magnetic force is stronger, the magnet pulls harder on metal objects. More force means stronger attraction — the paperclip jumps to the magnet from farther away.")
    ],
    "sim_answers": [
        ("Weak Magnet Scenario", "When Magnet Strength is set to low, Magnetic Force is weak and Attraction is low. The magnet can only pick up a paperclip when it is very close. The invisible field around the magnet is small and does not reach far."),
        ("Strong Magnet Scenario", "When Magnet Strength is set to maximum, Magnetic Force is very strong and Attraction is high. The magnet can grab a paperclip from farther away and hold more paperclips at once. The invisible field is big and powerful.")
    ],
    "stem_intro": "Present the challenge: A recycling center needs your help sorting metal cans from plastic bottles and paper. Your team must design a magnetic sorting tool that quickly picks up only the metal items. Use what your model taught you about magnetic force!",
    "stem_concepts": [
        ("Magnetic Force", "Magnets create an invisible field that pulls on certain metals. Stronger magnets create bigger fields with more pulling power for your sorting tool."),
        ("Selective Attraction", "Magnets only attract iron, nickel, and cobalt. This is what makes magnets perfect for sorting — they grab metal and ignore everything else."),
        ("Distance Matters", "Magnetic force is strongest up close. Your sorting tool needs to get the magnet close enough to the metal items to pick them up.")
    ],
    "stem_eval": [
        ("Expert (4)", "Sorting tool successfully separates metal from non-metal, student explains design using magnetic force concepts from the model"),
        ("Proficient (3)", "Sorting tool works and student can explain why magnets pick up some objects but not others"),
        ("Developing (2)", "Sorting tool is built but student struggles to connect magnet strength to sorting ability"),
        ("Beginning (1)", "Sorting tool is incomplete or student cannot explain why the magnet picks up certain objects")
    ],
    "support": [
        "Provide a T-chart labeled 'Magnetic' and 'Not Magnetic' for students to sort test objects before building",
        "Use a physical magnet and various objects so students can feel the difference in pull strength",
        "Sentence frames: 'The magnet picked up the ___ because ___ but not the ___ because ___'"
    ],
    "extensions": [
        "Test whether magnetic force can pass through different materials like paper, cardboard, and fabric",
        "Research how magnets are used in everyday life — from fridge magnets to MRI machines to maglev trains",
        "Investigate what happens when you put two magnets near each other — when do they attract and when do they repel?"
    ],
    "cross_curr": [
        ("Math", "Count and graph how many paperclips each magnet can hold to compare magnet strength using bar graphs"),
        ("ELA", "Write an explanation for a younger student about why magnets stick to some things but not others"),
        ("Art", "Create a colorful poster showing the invisible magnetic field around a magnet using iron filing patterns as inspiration")
    ],
    "misconceptions": [
        ("Magnets stick to all metals", "Magnets only attract metals that contain iron, nickel, or cobalt. Many metals like aluminum (soda cans), copper (pennies), and gold (jewelry) are NOT magnetic at all. Test different metals to see which ones a magnet attracts.", "Bring in aluminum foil, a copper penny, and a steel paperclip. Test each with a magnet. Ask: Which ones stick? Are they ALL metals? This proves not all metals are magnetic."),
        ("Magnets lose their power over time just from using them", "Permanent magnets keep their magnetism for a very long time. They can lose strength if they are dropped hard, heated up, or stored incorrectly, but normal use does not weaken them. The magnetic field is created by the arrangement of atoms inside the magnet.", "Show that a magnet picks up the same number of paperclips at the start and end of class. Ask: Did it get weaker from all our experiments today?"),
        ("Bigger magnets are always stronger", "Size does not always determine magnet strength. A small neodymium magnet can be much stronger than a large ceramic magnet. What matters is the material the magnet is made from and how its atoms are arranged inside, not just how big it is.", "Compare a small strong magnet with a large weak magnet. Test how many paperclips each can hold. Ask: Which is stronger? Which is bigger? What does this tell us?")
    ]
}

L02 = {
    "id": "G03-L02",
    "title": "Can You Predict the Weather?",
    "subtitle": "Patterns in Weather and Climate",
    "ngss": "3-ESS2-1",
    "ngss_desc": "Represent data in tables and graphical displays to describe typical weather conditions expected during a particular season.",
    "big_question": "Can we figure out what the weather will be like tomorrow by looking at patterns from the past?",
    "objectives": [
        "Describe how weather follows patterns that repeat with the seasons",
        "Model how temperature, cloud cover, and chance of rain are connected",
        "Use weather data to predict what might happen next"
    ],
    "vocabulary": [
        ("Weather", "What the sky and air are doing right now — sunny, rainy, windy, hot, or cold"),
        ("Climate", "The pattern of weather in a place over a long time — like how summers are usually hot"),
        ("Temperature", "How hot or cold the air is, measured with a thermometer"),
        ("Precipitation", "Water that falls from the sky — rain, snow, sleet, or hail")
    ],
    "components": [
        ("Temperature", "How hot or cold the air is outside — measured in degrees", True),
        ("Cloud Cover", "How many clouds are in the sky — more clouds can block the sun and hold water", False),
        ("Chance of Rain", "How likely it is that rain will fall — depends on clouds and temperature", False)
    ],
    "think_about_it": "When temperature changes, what happens to cloud cover and chance of rain? Is the relationship always the same?",
    "scenarios": [
        ("Hot Summer Day", "Set Temperature to high and observe what happens to Cloud Cover and Chance of Rain"),
        ("Cold Winter Day", "Set Temperature to low and observe how Cloud Cover and Chance of Rain change"),
        ("Cool Spring Day", "Set Temperature to medium and compare to the summer and winter results")
    ],
    "sim_scenarios": [
        ("Hot Summer Day", "Temperature set to high", "What do you predict will happen to Chance of Rain on a very hot day?"),
        ("Cold Winter Day", "Temperature set to low", "What do you predict will happen to Cloud Cover when it is very cold?"),
        ("Cool Spring Day", "Temperature set to medium", "Will the chance of rain be higher or lower than on the hot summer day?")
    ],
    "discoveries": [
        "Weather follows patterns — certain seasons tend to have similar types of weather year after year",
        "Temperature, cloud cover, and precipitation are all connected in a weather system",
        "Scientists called meteorologists use patterns in weather data to make predictions about future weather",
        "Climate is the long-term pattern of weather — it tells us what weather is TYPICAL for a place and season"
    ],
    "answer": "Yes, we can predict the weather by studying patterns! Weather is not random — it follows patterns that repeat with the seasons. By tracking temperature, cloud cover, and rain over time, scientists spot trends that help them guess what will happen next. Summer days tend to be hot and sunny, winter days tend to be cold and cloudy. Meteorologists use these patterns plus special tools to forecast the weather every single day!",
    "stem_title": "Build a Class Weather Station",
    "stem_mission": "Design and build a simple weather station that tracks temperature and cloud cover to make weather predictions for your school.",
    "stem_scenario": "Your school principal wants students to predict the weather for morning announcements each day. Your team must design a weather tracking station that collects data and uses patterns to make forecasts. Use what you learned about weather patterns to build it!",
    "stem_questions": [
        "What weather data do you need to collect every day to spot patterns?",
        "How many days of data do you need before you can start making predictions?",
        "How will you display your data so that patterns are easy to see?"
    ],
    "stem_design_qs": [
        "Where is the best place to put your weather station so you get accurate readings?",
        "How will you measure temperature — with a real thermometer or a weather app?",
        "What chart or graph will you use to track data over time?",
        "How will you share your weather predictions with the school?"
    ],
    "career": "Meteorologists study weather patterns and use science to predict storms, temperature, and precipitation. They earn $50,000-$100,000/year.",
    "images": {
        "cover": ("cover-weather.png", "A dramatic photorealistic sky showing different weather conditions side by side — sunny blue sky transitioning to storm clouds with rain, beautiful nature photography with vibrant colors and dramatic lighting"),
        "landscape": ("landscape-weather.png", "Diverse 3rd grade students (8-9 years old, wide variety of ethnicities including Black, Latino, Asian, and white children with natural hairstyles) looking out a classroom window at the sky, some holding thermometers, bright modern classroom, natural light"),
        "modeling": ("modeling-weather.png", "A colorful kid-friendly scientific diagram showing the water cycle with clouds, rain, and a thermometer, arrows connecting temperature to clouds to rain, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-weather.png", "A teacher with diverse 3rd graders (8-9 years old, wide variety of ethnicities with natural hairstyles) gathered around a weather chart on the wall, students pointing at temperature graphs and cloud pictures, animated conversation"),
        "stem": ("stem-weather.png", "Diverse 3rd graders (8-9 years old, wide mix of ethnicities including Black, Latino, Asian children) building simple weather stations with thermometers, rain gauges from plastic bottles, and cloud observation charts at outdoor tables")
    },
    "pre_assessment": [
        "What is the weather like today? How do you know without looking outside?",
        "If it is July, can you guess if it will be hot or cold? How do you know?",
        "Draw your favorite kind of weather and explain why you think it happens."
    ],
    "reflections": [
        "How are weather and climate different, and why does knowing the difference matter?",
        "How did your model help you understand why meteorologists can predict the weather?"
    ],
    "reflection_exemplars": [
        ("How are weather and climate different?", "Weather is what is happening in the sky RIGHT NOW — it could be sunny this morning and rainy this afternoon. Climate is the BIG PICTURE pattern of weather over many years. Climate tells us that summer is usually hot and winter is usually cold. Knowing the difference matters because climate helps us predict what type of weather to expect in each season, even though we cannot know the exact weather every single day.")
    ],
    "cast_items": [
        "Describe how temperature, cloud cover, and precipitation are connected in a weather system",
        "Use weather data to identify seasonal patterns and make predictions",
        "Explain the difference between weather and climate using examples"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student collects temperature data for one year. She notices that July is always the hottest month. Which best describes what she discovered?"),
        ("Constructed Response:", "Your friend says the weather is totally random and nobody can predict it. Using what you know about weather patterns, explain why meteorologists CAN predict the weather. Use the words 'pattern' and 'data' in your answer.")
    ],
    "extend_components": [
        ("Wind Speed", "How fast the air is moving — wind can bring in new weather from other places"),
        ("Humidity", "How much water vapor is in the air — more humidity means more chance of rain"),
        ("Season", "What time of year it is — seasons create the biggest weather patterns")
    ],
    "dimensions": [
        ("Science Practice", "Analyzing and Interpreting Data", "Students analyze weather data displayed in tables and graphs to identify seasonal patterns and make evidence-based weather predictions."),
        ("Disciplinary Core Idea", "ESS2.D Weather and Climate", "Scientists record patterns of the weather across different times and areas so that they can make predictions about what kind of weather might happen next."),
        ("Crosscutting Concept", "Patterns", "Students identify repeating patterns in weather data across seasons and use those patterns to predict future weather conditions.")
    ],
    "background_intro": "Weather affects our lives every single day — what we wear, what we do outside, and even how we feel. Understanding weather patterns helps us plan ahead and stay safe during storms, heat waves, and cold snaps.",
    "background_sections": [
        ("What Is Weather?", "Weather describes the conditions of the atmosphere at a specific time and place. It includes temperature (how hot or cold), precipitation (rain, snow, sleet, hail), wind (how fast and which direction air moves), humidity (how much moisture is in the air), and cloud cover (how many clouds are in the sky). Weather can change quickly — it might be sunny in the morning and stormy by afternoon."),
        ("What Is Climate?", "Climate is the average pattern of weather in a place over 30 or more years. While weather changes day to day, climate changes very slowly. For example, the weather in Phoenix, Arizona on any given day might be cloudy, but the climate there is hot and dry. Knowing the climate helps us predict what KINDS of weather to expect in a place during each season."),
        ("How Do Meteorologists Predict Weather?", "Meteorologists are scientists who study weather. They use tools like thermometers (temperature), barometers (air pressure), anemometers (wind speed), and rain gauges (precipitation). They also use satellites, weather balloons, and radar. By collecting data over time, they spot patterns. They know that certain cloud types bring rain, dropping air pressure often means a storm is coming, and seasons follow predictable temperature patterns. Modern computers help them make forecasts up to 10 days ahead.")
    ],
    "lever_L": "Students identify temperature as an external component and cloud cover and chance of rain as internal components that change in response to temperature conditions.",
    "lever_E": "Students determine that temperature affects cloud cover and chance of rain — warmer air holds more moisture, and different temperatures create different weather patterns.",
    "lever_V": "Students build a model showing how temperature connects to cloud cover and chance of rain in a weather system.",
    "lever_Ev": "Students run hot summer day, cold winter day, and cool spring day scenarios to observe how changing temperature affects cloud cover and precipitation.",
    "lever_R": "Students add wind speed or humidity to explore how additional factors make weather prediction more accurate but also more complex.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic weather images", "say": "Look outside right now — what is the weather doing? Could you have guessed this morning what it would be like?", "do": "Have students look out the window and describe today's weather. Ask: Do you think we could have predicted this yesterday?", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn Today?", "visual": "Learning goals and vocabulary words", "say": "Today we are going to become weather detectives and figure out if we can predict what the sky will do next!", "do": "Read objectives together. Introduce vocabulary — have students act out different types of weather (shivering for cold, fanning for hot).", "time": "3 min"},
        {"num": "Slide 3", "title": "The Big Question", "visual": "Question mark over a weather map", "say": "Can we actually predict the weather? Or is it just random? Let us investigate!", "do": "Show a week of weather data from your city. Ask students: Do you see any patterns? Turn and talk with a partner.", "time": "3 min"},
        {"num": "Slide 4", "title": "Let's Build a Model!", "visual": "LEVER steps overview for kids", "say": "We are going to build a weather model to see if patterns can help us predict rain and sunshine!", "do": "Preview each LEVER step. Explain that weather scientists use models every day to make forecasts.", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Sort the Parts", "visual": "Component cards for the weather model", "say": "What parts of weather can we measure? Which one do we set, and which ones change on their own?", "do": "Guide sorting of three components. Explain temperature is external because it is set by the sun and seasons.", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect with Arrows", "visual": "Arrow diagrams between weather components", "say": "When the temperature goes up in summer, what usually happens to clouds and rain? Let us connect the parts!", "do": "Help students draw arrows showing how temperature connects to cloud cover and chance of rain.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Run the Simulation!", "visual": "Simulation with weather graphs and predictions", "say": "Let us test our weather model! We will try a hot summer day, a cold winter day, and a cool spring day.", "do": "Have students predict first, then run each scenario. Compare results across seasons on the graph.", "time": "8 min"},
        {"num": "Slide 8", "title": "What Did We Discover?", "visual": "Key findings about weather patterns", "say": "Now we know the secret — weather follows PATTERNS, and patterns help us predict what comes next!", "do": "Summarize discoveries. Show a real 7-day forecast and point out the patterns. Ask: What do you predict for next week?", "time": "7 min"}
    ],
    "sort_reasoning": "Temperature is external because it is determined by the sun's energy and the season — we cannot control it, but it drives the weather system. Cloud Cover and Chance of Rain are internal because they are results that happen INSIDE the weather system in response to temperature and other conditions.",
    "relationships": [
        ("Temperature to Cloud Cover", "POSITIVE (+)", "When temperature rises, more water evaporates into the air, which can form more clouds. Warm, humid days often have big puffy clouds building up, especially in summer afternoon thunderstorms."),
        ("Cloud Cover to Chance of Rain", "POSITIVE (+)", "More clouds in the sky means more water droplets are gathered together. When enough water collects in clouds, it falls as precipitation. A sky full of dark clouds has a much higher chance of rain than a clear blue sky.")
    ],
    "sim_answers": [
        ("Hot Summer Day Scenario", "When Temperature is set to high, Cloud Cover can build up during the afternoon as warm air rises and forms thunderstorm clouds. Chance of Rain increases in the afternoon. Hot summer days often start clear but can end with big storms as the heat builds clouds."),
        ("Cold Winter Day Scenario", "When Temperature is set to low, Cloud Cover may be steady and gray. Chance of Rain (or snow) depends on whether moisture is present. Cold days can be clear and dry or overcast and snowy — temperature alone does not tell the whole story, which is why meteorologists track many factors.")
    ],
    "stem_intro": "Present the challenge: Your school principal wants students to predict the weather for morning announcements. Your team must design a weather tracking station that collects data on temperature and cloud cover, then uses patterns to make forecasts!",
    "stem_concepts": [
        ("Weather Patterns", "Weather follows patterns that repeat with the seasons. By tracking data over time, you can spot these patterns and use them to predict what comes next."),
        ("Data Collection", "Good predictions need good data. Recording temperature, cloud cover, and rain every day builds a picture of your local weather patterns over time."),
        ("Seasonal Trends", "Summer tends to be hot with afternoon storms, winter tends to be cold with gray skies. These seasonal patterns are the biggest clues for predicting weather.")
    ],
    "stem_eval": [
        ("Expert (4)", "Weather station collects accurate data, student identifies patterns and makes predictions supported by evidence from the model"),
        ("Proficient (3)", "Weather station tracks data and student can explain how patterns help predict weather"),
        ("Developing (2)", "Weather station is built but student struggles to connect data patterns to weather predictions"),
        ("Beginning (1)", "Weather station is incomplete or student cannot explain how weather patterns work")
    ],
    "support": [
        "Provide a simple daily weather log with pictures of sun, clouds, and rain for students to circle each day",
        "Use a large classroom thermometer and have students read it together each morning",
        "Sentence frames: 'I predict tomorrow will be ___ because the pattern shows ___'"
    ],
    "extensions": [
        "Track weather data for a full month and create graphs to show patterns over time",
        "Compare your city's climate to a city in a different part of the country using online weather data",
        "Research how animals predict weather — can cows, birds, or crickets sense storms coming?"
    ],
    "cross_curr": [
        ("Math", "Create bar graphs and line graphs of daily temperature data to find patterns and calculate averages for each week"),
        ("ELA", "Write a weather forecast report for your city using data and patterns, like a TV meteorologist"),
        ("Art", "Design a colorful weather tracking poster for the classroom that displays data in a creative, easy-to-read way")
    ],
    "misconceptions": [
        ("Weather is completely random and cannot be predicted", "Weather follows patterns that repeat over time, especially with the seasons. Meteorologists use data, patterns, and computer models to make predictions. Forecasts are not perfect, but they are right most of the time because weather is NOT random.", "Show a chart of average temperatures for each month in your city. Ask: Is there a pattern? Could you guess if February or July will be hotter? That is a prediction based on a pattern!"),
        ("Climate and weather are the same thing", "Weather is what is happening right now — it changes every day. Climate is the average pattern of weather over 30+ years. You can have a cold day in summer (weather) even though summers are usually hot (climate). Climate is like your personality — weather is like your mood today.", "Ask: Is it possible to have a rainy day in a desert? Yes! That is weather. But the desert's CLIMATE is still dry because it almost never rains there."),
        ("Hot weather always means sunny and no rain", "Some of the rainiest places on Earth are also the hottest, like tropical rainforests. Hot air can hold more moisture, which can lead to bigger storms. Summer thunderstorms happen BECAUSE it is hot — the heat causes air to rise rapidly, forming towering storm clouds.", "Show pictures of a tropical thunderstorm and a cold, dry winter day. Ask: Which one has more rain? Which is hotter? Hot does not always mean dry!")
    ]
}

L03 = {
    "id": "G03-L03",
    "title": "Why Do Animals Live in Groups?",
    "subtitle": "The Power of Teamwork in Nature",
    "ngss": "3-LS2-1",
    "ngss_desc": "Construct an argument that some animals form groups that help members survive.",
    "big_question": "Why do so many animals choose to live together in groups instead of living alone?",
    "objectives": [
        "Explain how living in a group helps animals survive dangers like predators",
        "Model how group size, predator detection, and survival rate are connected",
        "Describe at least two advantages that group living gives animals"
    ],
    "vocabulary": [
        ("Predator", "An animal that hunts and eats other animals to survive"),
        ("Survival", "Staying alive by finding food, water, shelter, and staying safe from danger"),
        ("Group Behavior", "When animals work together as a team to help each other stay safe or find food")
    ],
    "components": [
        ("Group Size", "How many animals are living together in the group — from a few to hundreds", True),
        ("Predator Detection", "How quickly the group notices a predator coming — more eyes watching means faster detection", False),
        ("Survival Rate", "How many animals in the group stay safe and survive — better detection means more survive", False)
    ],
    "think_about_it": "When group size increases, what happens to predator detection? Is the relationship positive or negative?",
    "scenarios": [
        ("Alone", "Set Group Size to 1 animal and observe Predator Detection and Survival Rate"),
        ("Small Group", "Set Group Size to 5 animals and observe how detection and survival change"),
        ("Large Herd", "Set Group Size to 50 animals and compare to being alone and in a small group")
    ],
    "sim_scenarios": [
        ("Alone", "Group Size set to 1", "What do you predict will happen to Survival Rate when an animal is all alone?"),
        ("Small Group", "Group Size set to 5", "What do you predict will happen to Predator Detection with 5 animals watching?"),
        ("Large Herd", "Group Size set to 50", "Will a herd of 50 animals detect a predator faster than a group of 5? Why?")
    ],
    "discoveries": [
        "Animals in bigger groups detect predators faster because more eyes are watching for danger",
        "Higher predator detection leads to higher survival rates — early warning saves lives",
        "Group living has other benefits too, like sharing body heat, finding food together, and protecting babies",
        "Even though groups attract attention, the safety in numbers advantage usually outweighs the risk"
    ],
    "answer": "Animals live in groups because teamwork helps them survive! When more animals are together, there are more eyes watching for danger. A lion sneaking toward a herd of zebras is much more likely to be spotted than if it were sneaking up on one zebra alone. When one animal sees danger, it warns the whole group, and everyone runs! This is called 'safety in numbers' — the bigger the group, the more likely each animal is to survive.",
    "stem_title": "Design an Animal Alarm System",
    "stem_mission": "Design a model alarm system inspired by how animal groups warn each other about predators approaching.",
    "stem_scenario": "A wildlife park wants to protect a group of animals from predators. Your team must design an alarm system that works like animal group behavior — the more watchers you have, the faster danger is detected. Use what you learned about group behavior to create your design!",
    "stem_questions": [
        "How do real animals warn each other when they spot a predator?",
        "Why is having more watchers better than having just one?",
        "How will your alarm system get the warning to everyone quickly?"
    ],
    "stem_design_qs": [
        "How many lookout stations will your alarm system have?",
        "What kind of signal will the lookouts send — sound, light, or movement?",
        "How will you test whether more lookouts detect danger faster?",
        "What happens if one lookout misses the danger — does the system still work?"
    ],
    "career": "Wildlife Biologists study animals in their natural habitats, observing group behavior, migration, and survival strategies. They earn $45,000-$85,000/year.",
    "images": {
        "cover": ("cover-animal-groups.png", "A stunning photorealistic image of a large herd of zebras standing together on the African savanna at golden hour, with a few zebras alert and watching the horizon, dramatic wildlife photography"),
        "landscape": ("landscape-animal-groups.png", "Diverse 3rd grade students (8-9 years old, wide variety of ethnicities including Black, Latino, Asian, and white children with natural hairstyles) watching a nature video about animal herds on a smartboard, leaning forward with fascination, bright modern classroom"),
        "modeling": ("modeling-animal-groups.png", "A colorful kid-friendly scientific diagram showing a group of animals with dotted lines representing their field of vision watching for predators, arrows showing warning signals spreading through the group, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-animal-groups.png", "A teacher with diverse 3rd graders (8-9 years old, wide variety of ethnicities with natural hairstyles) sitting in a circle, students acting out animal group behavior, some pretending to be lookouts while others pretend to eat, animated and fun"),
        "stem": ("stem-animal-groups.png", "Diverse 3rd graders (8-9 years old, wide mix of ethnicities including Black, Latino, Asian children) building model alarm systems with cups, string, and bells at tables, testing how quickly signals travel through their designs")
    },
    "pre_assessment": [
        "Can you name an animal that lives in a group? Why do you think they stay together?",
        "Would you rather walk through a dark forest alone or with ten friends? Why?",
        "Draw a group of animals working together and explain what they are doing."
    ],
    "reflections": [
        "Why is 'safety in numbers' a good way to describe how animal groups work?",
        "How did your model help you understand why animals are safer in groups than alone?"
    ],
    "reflection_exemplars": [
        ("Why is 'safety in numbers' a good way to describe how animal groups work?", "'Safety in numbers' means that being in a big group makes each animal safer. When there are more animals, there are more eyes watching for predators, so danger gets spotted faster. Also, even if a predator attacks, each individual animal has a smaller chance of being the one caught. It is like playing tag — the more people on your team, the less likely YOU are the one who gets tagged!")
    ],
    "cast_items": [
        "Explain how group size affects predator detection and survival in animal groups",
        "Use a model to argue that living in groups helps animals survive",
        "Describe at least two advantages of group living for animals"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A herd of 30 antelope spots a lion sooner than a single antelope standing alone. Which best explains why the herd detected the lion faster?"),
        ("Constructed Response:", "A student says that animals should live alone because groups attract more predators. Using evidence from your model, explain why living in a group is actually SAFER for most animals. Use the words 'group size' and 'predator detection' in your answer.")
    ],
    "extend_components": [
        ("Food Availability", "How much food is nearby — larger groups need more food, which can cause competition"),
        ("Warning Signal Speed", "How fast the alarm call spreads through the group — faster signals save more lives")
    ],
    "dimensions": [
        ("Science Practice", "Engaging in Argument from Evidence", "Students construct an argument supported by model evidence that animals forming groups increases survival rates through improved predator detection."),
        ("Disciplinary Core Idea", "LS2.D Social Interactions and Group Behavior", "Being part of a group helps animals obtain food, defend themselves, and cope with changes. Groups may serve different functions and vary dramatically in size."),
        ("Crosscutting Concept", "Cause and Effect", "Students investigate how changing group size (cause) affects predator detection and survival rate (effects) in a predictable, positive relationship.")
    ],
    "background_intro": "From tiny ants to enormous elephants, millions of animal species choose to live in groups. This is not random — group living provides real survival advantages that scientists have studied for decades.",
    "background_sections": [
        ("Why Do Animals Form Groups?", "Animals form groups for several important reasons. The most common is protection from predators — more animals means more eyes and ears watching for danger. Groups also help animals find food more efficiently, stay warm by huddling together, care for young by sharing babysitting duties, and even hunt more successfully. Different species form different types of groups — herds, flocks, packs, schools, and colonies."),
        ("Safety in Numbers", "The 'many eyes' hypothesis explains one of the biggest advantages of group living. In a group of 50 meerkats, while some eat, others stand guard as sentinels. If any sentinel spots a hawk or jackal, it gives an alarm call and everyone dashes for cover. A lone meerkat must both eat AND watch for predators — it cannot do both well. The dilution effect also helps: even if a predator attacks, each individual's chance of being caught is only 1 in 50 instead of 1 in 1."),
        ("Costs of Group Living", "Group living is not all positive. Large groups need more food, which can lead to competition. Diseases spread faster in crowded groups. Some animals must share territory and mates. And large groups are easier for predators to FIND, even though individual members are harder to catch. Despite these costs, for most social animals, the survival benefits of group living far outweigh the drawbacks.")
    ],
    "lever_L": "Students identify group size as an external component and predator detection and survival rate as internal components that change in response to how many animals are in the group.",
    "lever_E": "Students determine that group size positively affects predator detection, and predator detection positively affects survival rate — more animals means faster warning means more survive.",
    "lever_V": "Students build a model showing how increasing group size leads to better predator detection and higher survival rates for the group.",
    "lever_Ev": "Students run alone, small group, and large herd scenarios to observe how changing group size affects detection and survival across the system.",
    "lever_R": "Students add food availability or warning signal speed to explore tradeoffs of group living — bigger groups are safer but need more food.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with a herd of animals on the savanna", "say": "Imagine you are a zebra on the African plains. Would you rather be alone or with a hundred friends? Why?", "do": "Let students share their answers. Show images of animal groups: a wolf pack, a school of fish, a flock of birds.", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn Today?", "visual": "Learning goals and vocabulary words", "say": "Today we are going to figure out why SO many animals choose to live in groups instead of going solo!", "do": "Read objectives together. Introduce vocabulary with examples: a lion is a predator, a zebra uses group behavior for survival.", "time": "3 min"},
        {"num": "Slide 3", "title": "The Big Question", "visual": "Single animal vs. a large group", "say": "Why do animals live in groups? Is it just because they like having friends, or is there a survival reason?", "do": "Play a quick game: one student closes their eyes while others watch for a 'predator' (teacher holding a picture). Which spots it first?", "time": "3 min"},
        {"num": "Slide 4", "title": "Let's Build a Model!", "visual": "LEVER steps overview for kids", "say": "We are going to build a model to prove whether groups really do help animals survive!", "do": "Preview each LEVER step. Explain that scientists use models to test ideas about animal behavior.", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Sort the Parts", "visual": "Component cards for the group behavior model", "say": "What parts of this system can we identify? What can we change, and what happens as a result?", "do": "Guide sorting of three components. Explain group size is external because the number of animals is what we are testing.", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect with Arrows", "visual": "Arrow diagrams between group components", "say": "When there are MORE animals in the group, does predator detection go up or down? And what about survival?", "do": "Help students draw positive arrows from group size to predator detection, and from detection to survival rate.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Run the Simulation!", "visual": "Simulation graphs comparing group sizes", "say": "Let us test it! First one animal alone, then a small group, then a big herd. What do you predict?", "do": "Have students write predictions first, then run each scenario. Discuss: Were you surprised by any results?", "time": "8 min"},
        {"num": "Slide 8", "title": "What Did We Discover?", "visual": "Key findings about group behavior", "say": "The evidence is clear — groups save lives! Safety in numbers is REAL.", "do": "Summarize discoveries. Show a short video clip of meerkats taking turns as sentinels. Ask: How does this connect to our model?", "time": "7 min"}
    ],
    "sort_reasoning": "Group Size is external because it is the variable we are testing — we decide how many animals are in the group before the scenario runs. Predator Detection and Survival Rate are internal because they are outcomes that change INSIDE the system based on how many animals are watching for danger.",
    "relationships": [
        ("Group Size to Predator Detection", "POSITIVE (+)", "More animals in the group means more eyes and ears scanning for danger. A group of 50 animals is much more likely to spot a predator quickly than a single animal trying to watch in all directions alone."),
        ("Predator Detection to Survival Rate", "POSITIVE (+)", "When predators are detected earlier, the group has more time to escape. Early warning gives animals a head start to run, hide, or defend themselves, which means more of them survive the encounter.")
    ],
    "sim_answers": [
        ("Alone Scenario", "When Group Size is set to 1, Predator Detection is very slow because only one animal is watching. Survival Rate is low because the animal has to find food AND watch for predators at the same time. A lone animal is an easy target."),
        ("Large Herd Scenario", "When Group Size is set to 50, Predator Detection is very fast because many animals are watching in all directions. Survival Rate is high because the early warning gives everyone time to escape, and each individual animal has a lower chance of being caught.")
    ],
    "stem_intro": "Present the challenge: A wildlife park needs to protect its animals from predators. Your team must design an alarm system inspired by how animal groups warn each other. The more watchers you have, the faster danger is detected — just like in nature!",
    "stem_concepts": [
        ("Safety in Numbers", "More eyes watching means faster predator detection. Your alarm system should have multiple lookout points to spot danger from any direction."),
        ("Warning Signals", "Animals use calls, movements, and body language to warn their group. Your alarm system needs a fast way to spread the warning to everyone."),
        ("Early Detection", "The sooner danger is spotted, the more time animals have to escape. Design your system to detect threats as early as possible.")
    ],
    "stem_eval": [
        ("Expert (4)", "Alarm system uses multiple lookouts, spreads warnings quickly, and student explains the design using group behavior concepts from the model"),
        ("Proficient (3)", "Alarm system works and student can explain how more lookouts improve detection speed"),
        ("Developing (2)", "Alarm system is built but student struggles to connect it to animal group behavior concepts"),
        ("Beginning (1)", "Alarm system is incomplete or student cannot explain why more lookouts help detect danger faster")
    ],
    "support": [
        "Act out a group survival scenario — assign students as lookouts, feeders, and a pretend predator to physically experience the concept",
        "Show a simple diagram comparing one animal watching vs. many animals watching in different directions",
        "Sentence frames: 'When the group is bigger, predator detection is ___ because ___'"
    ],
    "extensions": [
        "Research a specific animal group (wolf pack, bee colony, penguin huddle) and present how their group behavior helps them survive",
        "Investigate animals that are better off living alone — what advantages does solo living have for some species?",
        "Design an experiment to test whether your class can spot a hidden object faster with more people searching"
    ],
    "cross_curr": [
        ("Math", "Create a bar graph comparing survival rates for groups of 1, 5, 10, 25, and 50 animals based on model data"),
        ("ELA", "Write a persuasive paragraph arguing whether it is better for a specific animal to live in a group or alone, using model evidence"),
        ("Art", "Create a mural showing an animal group working together, with labels explaining each animal's role in keeping the group safe")
    ],
    "misconceptions": [
        ("Animals live in groups just because they are friendly", "Group living is primarily about survival, not friendship. Animals form groups because it increases their chances of detecting predators, finding food, and staying safe. While some animals do form social bonds, the main reason for grouping is survival advantage.", "Ask: Do fish in a school know each other's names? No! They swim together because it confuses predators and helps them survive — not because they are friends."),
        ("Bigger groups are always better for every animal", "Very large groups have disadvantages — they need more food, attract more predators, and diseases spread faster. Each species has an ideal group size that balances safety with food competition. Lions live in small prides while wildebeest form herds of thousands — each size fits that animal's needs.", "Compare: Why do lions live in groups of 15 but wildebeest live in groups of 1,000? Because lions are predators who need to share kills, while wildebeest are prey who benefit most from safety in numbers."),
        ("Predators only attack animals that are alone", "Predators attack groups too, but they have a much harder time. Predators often target the edges of a group or try to separate one animal from the herd. The confusion of many animals running in different directions makes it harder for a predator to focus on one target.", "Show a video of a lion chasing a herd — the lion gets confused by all the movement. Ask: Why is it harder to catch one animal when they are all running together?")
    ]
}

L04 = {
    "id": "G03-L04",
    "title": "How Do Fossils Form?",
    "subtitle": "Clues from Ancient Life",
    "ngss": "3-LS4-1",
    "ngss_desc": "Analyze and interpret data from fossils to provide evidence of the organisms and the environments in which they lived long ago.",
    "big_question": "How do the bones and shells of ancient animals turn into rock fossils that last millions of years?",
    "objectives": [
        "Explain the step-by-step process of how fossils form over millions of years",
        "Model how burial depth, pressure, and fossilization are connected",
        "Describe what fossils can tell us about animals and environments from long ago"
    ],
    "vocabulary": [
        ("Fossil", "The preserved remains or traces of an animal or plant that lived long ago, usually found in rock"),
        ("Sediment", "Tiny pieces of sand, mud, and dirt that settle in layers on the ground or at the bottom of water"),
        ("Paleontologist", "A scientist who studies fossils to learn about life on Earth millions of years ago")
    ],
    "components": [
        ("Burial Depth", "How deep the remains are buried under layers of sediment over time", True),
        ("Pressure", "The squeezing force from all the sediment layers piled on top — deeper means more pressure", False),
        ("Fossilization", "The process of remains slowly turning into rock as minerals replace the original material", False)
    ],
    "think_about_it": "When burial depth increases, what happens to pressure? Is the relationship positive or negative?",
    "scenarios": [
        ("Shallow Burial", "Set Burial Depth to low and observe what happens to Pressure and Fossilization"),
        ("Deep Burial", "Set Burial Depth to maximum and observe how Pressure and Fossilization change"),
        ("Medium Burial", "Set Burial Depth to 50% and compare it to shallow and deep burial")
    ],
    "sim_scenarios": [
        ("Shallow Burial", "Burial Depth set to low", "What do you predict will happen to Fossilization when remains are barely buried?"),
        ("Deep Burial", "Burial Depth set to maximum", "What do you predict will happen to Pressure when remains are buried very deep?"),
        ("Medium Burial", "Burial Depth set to 50%", "Will a medium burial produce a fossil that is as good as a deep burial?")
    ],
    "discoveries": [
        "Fossils form when remains are buried deep under layers of sediment over millions of years",
        "More burial depth creates more pressure, which helps the fossilization process happen more completely",
        "Minerals in groundwater slowly replace the original bone or shell material, turning it into rock",
        "Fossils tell us what animals looked like, what they ate, and what their environment was like long ago"
    ],
    "answer": "Fossils form through an amazing process that takes millions of years! When an animal dies, its body can get buried under layers of sand and mud called sediment. Over time, more and more layers pile on top, creating enormous pressure. Underground water carrying dissolved minerals seeps through the remains, slowly replacing the original bone or shell with rock-hard minerals. After millions of years of burial and mineral replacement, what was once a bone is now a fossil — a rock copy of the original!",
    "stem_title": "Create a Fossil Time Capsule",
    "stem_mission": "Design a model that shows how fossils form step by step, creating a layered fossil time capsule that demonstrates the burial and fossilization process.",
    "stem_scenario": "A natural history museum wants a hands-on exhibit that shows visitors how fossils form. Your team must create a layered model that demonstrates burial, pressure, and fossilization step by step. Use what you learned about the fossilization process!",
    "stem_questions": [
        "What materials can you use to represent sediment layers building up over time?",
        "How will you show that pressure increases with depth?",
        "How can you demonstrate that the original material gets replaced by minerals?"
    ],
    "stem_design_qs": [
        "What will you use for the animal remains — a shell, a plastic bone, or a leaf?",
        "What materials will represent sediment layers — sand, clay, plaster?",
        "How will you stack the layers to show time passing?",
        "How will you label your model so museum visitors can understand each step?"
    ],
    "career": "Paleontologists travel the world digging up fossils and studying ancient life to understand the history of our planet. They earn $50,000-$95,000/year.",
    "images": {
        "cover": ("cover-fossils.png", "A dramatic photorealistic close-up of a beautifully preserved ammonite fossil embedded in layered sedimentary rock, showing incredible spiral detail, warm lighting on natural stone texture"),
        "landscape": ("landscape-fossils.png", "Diverse 3rd grade students (8-9 years old, wide variety of ethnicities including Black, Latino, Asian, and white children with natural hairstyles) carefully examining fossil specimens with magnifying glasses at their desks, bright modern classroom with a fossil display in the background"),
        "modeling": ("modeling-fossils.png", "A colorful kid-friendly scientific diagram showing the fossil formation process in four layers — an animal on the surface, then buried by sediment, then deeper with pressure arrows, then a fossil in rock, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-fossils.png", "A teacher with diverse 3rd graders (8-9 years old, wide variety of ethnicities with natural hairstyles) gathered around a table with fossil specimens, students pointing and asking questions, engaged and curious expressions"),
        "stem": ("stem-fossils.png", "Diverse 3rd graders (8-9 years old, wide mix of ethnicities including Black, Latino, Asian children) creating layered fossil models using sand, clay, plaster, and small plastic dinosaur bones in clear cups, collaborative work at tables")
    },
    "pre_assessment": [
        "Have you ever seen a fossil? What did it look like and where was it?",
        "How do you think the bones of a dinosaur that lived millions of years ago can still exist today?",
        "Draw what you think happens to an animal's bones after it dies and gets buried underground."
    ],
    "reflections": [
        "Why do most animals that die NOT become fossils, and what makes some animals more likely to fossilize?",
        "How did your model help you understand why fossils take millions of years to form?"
    ],
    "reflection_exemplars": [
        ("Why do most animals that die NOT become fossils?", "Most animals that die get eaten by scavengers or decompose before they can be buried. For a fossil to form, the remains need to be buried QUICKLY under sediment before they are destroyed. Then they need millions of years of pressure and mineral replacement. That is why fossils are so rare and special — everything has to happen just right. Animals near water, like rivers and oceans, are more likely to become fossils because sediment settles there naturally.")
    ],
    "cast_items": [
        "Explain the step-by-step process of how burial, pressure, and mineral replacement create fossils",
        "Use a model to describe how burial depth affects the fossilization process",
        "Describe what information scientists can learn from studying fossils"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A scientist finds a fish fossil in a rock layer high up on a mountain. What does this fossil tell us about that mountain long ago?"),
        ("Constructed Response:", "Explain the steps of how a dinosaur bone that is 65 million years old turned into a fossil we can find today. Use the words 'sediment,' 'pressure,' and 'minerals' in your answer.")
    ],
    "extend_components": [
        ("Mineral Content", "How many dissolved minerals are in the groundwater — more minerals means faster replacement of original material"),
        ("Time", "How many millions of years the remains have been buried — more time allows more complete fossilization")
    ],
    "dimensions": [
        ("Science Practice", "Analyzing and Interpreting Data", "Students analyze data from fossil models to provide evidence of how burial conditions affect the fossilization process and what fossils reveal about past environments."),
        ("Disciplinary Core Idea", "LS4.A Evidence of Common Ancestry and Diversity", "Some kinds of plants and animals that once lived on Earth are no longer found anywhere. Fossils provide evidence about the types of organisms that lived long ago and the nature of their environments."),
        ("Crosscutting Concept", "Scale, Proportion, and Quantity", "Students consider how the enormous scales of time (millions of years) and depth (deep underground) are necessary for the fossilization process to occur.")
    ],
    "background_intro": "Fossils are like nature's time capsules — windows into a world that existed millions or even billions of years ago. Every fossil tells a story about an ancient organism and the environment where it lived.",
    "background_sections": [
        ("How Fossils Form", "Fossil formation begins when an organism dies and is quickly buried by sediment — sand, mud, or volcanic ash. Quick burial is essential because it protects the remains from scavengers, weather, and decomposition. Over millions of years, more sediment piles on top, creating enormous pressure that compacts the lower layers into sedimentary rock. Meanwhile, mineral-rich groundwater seeps through the remains, slowly replacing the original bone, shell, or wood material with minerals like calcite, silica, and pyrite. The result is a rock replica of the original organism."),
        ("Types of Fossils", "There are several types of fossils. Body fossils preserve actual remains like bones, teeth, and shells. Mold fossils form when an organism decomposes but leaves an impression in the rock, like a cookie cutter shape. Cast fossils form when a mold gets filled with minerals, creating a 3D copy. Trace fossils preserve evidence of animal activity — footprints, burrows, and nests. Even ancient poop (called coprolites) can become fossils and tell scientists what animals ate!"),
        ("What Fossils Tell Us", "Fossils are the primary evidence scientists use to understand life on ancient Earth. By studying fossil shapes, sizes, and locations, paleontologists can determine what an organism looked like, what it ate, how it moved, and what environment it lived in. A fish fossil found on a mountain tells us that area was once underwater. Tropical plant fossils found in Antarctica tell us the continent was once warm. Fossils are like puzzle pieces that help us reconstruct Earth's incredible history.")
    ],
    "lever_L": "Students identify burial depth as an external component and pressure and fossilization as internal components that change in response to how deeply the remains are buried.",
    "lever_E": "Students determine that burial depth positively affects pressure, and pressure positively affects fossilization — deeper burial creates more pressure which drives more complete fossilization.",
    "lever_V": "Students build a model showing how increasing burial depth leads to greater pressure and more complete fossilization of remains.",
    "lever_Ev": "Students run shallow, medium, and deep burial scenarios to observe how changing burial depth affects pressure and fossilization across the system.",
    "lever_R": "Students add mineral content or time to explore how additional factors affect fossil quality — more minerals and more time produce better-preserved fossils.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with stunning fossil images", "say": "What if I told you that this rock is actually a BONE from an animal that lived 100 million years ago? How is that possible?", "do": "Pass around fossil specimens or high-quality images. Let students examine them closely and share observations.", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn Today?", "visual": "Learning goals and vocabulary words", "say": "Today we are going to solve the mystery of how ancient bones turn into rock fossils that last FOREVER!", "do": "Read objectives together. Introduce vocabulary — show real sediment (sand, mud) and explain what a paleontologist does.", "time": "3 min"},
        {"num": "Slide 3", "title": "The Big Question", "visual": "Dinosaur skeleton in a museum", "say": "How does something that was once alive turn into solid rock? That is our mystery to solve!", "do": "Have students turn and talk: What do you THINK happens to bones underground over millions of years? Share ideas with the class.", "time": "3 min"},
        {"num": "Slide 4", "title": "Let's Build a Model!", "visual": "LEVER steps overview for kids", "say": "We are going to build a model of how fossils form — step by step, layer by layer!", "do": "Preview each LEVER step. Show a simple animation of sediment layers building up over time.", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Sort the Parts", "visual": "Component cards for the fossil model", "say": "What parts of the fossil formation system can we identify? What starts the process?", "do": "Guide sorting of three components. Explain burial depth is external because natural events like floods and volcanic eruptions cause burial.", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect with Arrows", "visual": "Arrow diagrams between fossil components", "say": "When remains are buried deeper, does pressure go up or down? And how does that affect fossilization?", "do": "Help students draw positive arrows from burial depth to pressure, and from pressure to fossilization.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Run the Simulation!", "visual": "Simulation with burial depth scenarios", "say": "Time to test! What happens when bones are barely buried versus buried super deep? Let us find out!", "do": "Have students predict first, then run each scenario. Compare shallow vs. medium vs. deep burial results.", "time": "8 min"},
        {"num": "Slide 8", "title": "What Did We Discover?", "visual": "Key findings about fossil formation", "say": "Now we know the secret — fossils are made by TIME, PRESSURE, and MINERALS working together underground!", "do": "Summarize discoveries. Stack books on a student's hand to demonstrate how pressure increases with depth. Connect to the model.", "time": "7 min"}
    ],
    "sort_reasoning": "Burial Depth is external because it is determined by natural events like floods, landslides, and volcanic eruptions that bury remains under sediment — it happens to the organism from outside. Pressure and Fossilization are internal because they are processes that happen INSIDE the earth as a result of how deeply the remains are buried.",
    "relationships": [
        ("Burial Depth to Pressure", "POSITIVE (+)", "The deeper the remains are buried, the more layers of sediment sit on top of them. Each layer adds weight, so deeper burial means much more pressure squeezing down on the remains. Think of stacking heavy books — the bottom book feels the most pressure."),
        ("Pressure to Fossilization", "POSITIVE (+)", "Greater pressure helps compact the sediment into rock and pushes mineral-rich water through the remains. This mineral replacement process works better under high pressure, producing more complete and well-preserved fossils over millions of years.")
    ],
    "sim_answers": [
        ("Shallow Burial Scenario", "When Burial Depth is set to low, Pressure is minimal and Fossilization is poor or incomplete. The remains may decompose before the fossilization process can finish because there is not enough sediment protecting them from the surface. Shallow burials rarely produce good fossils."),
        ("Deep Burial Scenario", "When Burial Depth is set to maximum, Pressure is very high and Fossilization is excellent. The enormous weight of sediment compresses the layers into rock, and mineral-rich water thoroughly replaces the original material. Deep burial produces the most complete and detailed fossils.")
    ],
    "stem_intro": "Present the challenge: A natural history museum wants YOU to create a hands-on exhibit showing how fossils form. Your team must build a layered model demonstrating burial, pressure, and fossilization step by step so visitors can understand this amazing process!",
    "stem_concepts": [
        ("Sediment Layers", "Fossils form inside layers of sediment that build up over time. Each layer represents thousands or millions of years. Your model should show clear layers building up."),
        ("Pressure and Time", "The weight of sediment above creates pressure that helps turn remains into fossils. Deeper burial means more pressure and better fossils."),
        ("Mineral Replacement", "Groundwater carrying dissolved minerals slowly replaces original bone and shell material. This is what turns once-living material into solid rock.")
    ],
    "stem_eval": [
        ("Expert (4)", "Fossil model clearly shows layered burial with increasing pressure, student explains each step using fossilization concepts from the model"),
        ("Proficient (3)", "Fossil model shows layers and student can explain how burial and pressure create fossils"),
        ("Developing (2)", "Fossil model is built but student struggles to explain the connection between burial depth and fossilization"),
        ("Beginning (1)", "Fossil model is incomplete or student cannot explain how fossils form")
    ],
    "support": [
        "Provide a step-by-step visual showing the four stages of fossil formation with simple pictures",
        "Use a physical demonstration: press a shell into clay to make a mold fossil students can touch and understand",
        "Sentence frames: 'The deeper the burial, the more ___ which helps ___'"
    ],
    "extensions": [
        "Research a famous fossil discovery (like Sue the T. rex) and present what scientists learned from it",
        "Visit a virtual museum exhibit to explore real fossils and guess what environments those animals lived in",
        "Investigate why some parts of animals (bones, teeth, shells) fossilize better than soft parts (skin, muscles, organs)"
    ],
    "cross_curr": [
        ("Math", "Create a timeline showing how many millions of years ago different types of fossils formed, using a number line and scale"),
        ("ELA", "Write a story from the perspective of a fossil — describe your journey from living animal to rock over millions of years"),
        ("Art", "Create fossil rubbings or clay imprint fossils and display them with labels describing what organism they came from")
    ],
    "misconceptions": [
        ("Fossils are actual bones", "Fossils are NOT the original bones — they are rock copies. The original bone material was slowly replaced by minerals over millions of years. A fossil has the exact shape of the original bone but is made entirely of rock minerals. It is like making a copy of a key — the copy works the same but is made of different material.", "Hold up a rock and a bone. Ask: Which is heavier? Fossils are heavy like rocks because they ARE rocks — the original bone material is long gone, replaced by minerals."),
        ("Dinosaurs are the only animals that become fossils", "All kinds of organisms can become fossils — fish, insects, plants, shells, even bacteria! In fact, the most common fossils are sea creatures like trilobites and ammonites because ocean sediment buries remains quickly. Dinosaur fossils are actually quite rare compared to marine fossils.", "Show pictures of various fossils: a fern leaf, a seashell, an insect in amber, a fish. Ask: Are any of these dinosaurs? Nope! Any living thing can become a fossil under the right conditions."),
        ("Fossils form quickly, like in a few years", "Fossilization is an incredibly slow process that takes millions of years. The mineral replacement happens molecule by molecule as groundwater slowly seeps through the buried remains. There are no shortcuts — time and pressure are both essential for creating a true fossil.", "Ask: How old are you? 8? A fossil takes about 10,000 years just to START forming, and millions of years to complete. That is longer than all of human history! Write the numbers on the board to show the scale.")
    ]
}

L05 = {
    "id": "G03-L05",
    "title": "Why Do Some Animals Look Different?",
    "subtitle": "Inherited Traits vs. Learned Behaviors",
    "ngss": "3-LS3-1",
    "ngss_desc": "Analyze and interpret data to provide evidence that plants and animals have traits inherited from parents and that variation of these traits exists in a group of similar organisms.",
    "big_question": "Why do some puppies from the same litter look different from each other?",
    "objectives": [
        "Explain the difference between traits inherited from parents and traits caused by the environment",
        "Model how parent traits, genetic variation, and offspring appearance are connected",
        "Describe why brothers and sisters can look similar but not exactly alike"
    ],
    "vocabulary": [
        ("Trait", "A feature or characteristic of a living thing, like eye color, fur pattern, or height"),
        ("Inherited", "A trait that is passed from parents to their babies through genes — like your eye color"),
        ("Variation", "The differences between individual organisms of the same kind — like different fur colors in puppies"),
        ("Environment", "Everything around a living thing that can affect how it grows — food, sunlight, water, and weather")
    ],
    "components": [
        ("Parent Traits", "The characteristics that the mother and father have — these are passed down to offspring", True),
        ("Genetic Variation", "The natural mixing and shuffling of parent traits that creates unique combinations in each offspring", False),
        ("Offspring Appearance", "What the baby animal or plant looks like — a unique blend of traits from both parents", False)
    ],
    "think_about_it": "When parent traits are different from each other, what happens to genetic variation in the offspring? Is the relationship positive or negative?",
    "scenarios": [
        ("Similar Parents", "Set Parent Traits to very similar and observe Genetic Variation and Offspring Appearance"),
        ("Different Parents", "Set Parent Traits to very different and observe how Genetic Variation and Offspring Appearance change"),
        ("Mixed Parents", "Set Parent Traits to somewhat different and compare to similar and different parents")
    ],
    "sim_scenarios": [
        ("Similar Parents", "Parent Traits set to very similar", "What do you predict the offspring will look like when both parents look almost the same?"),
        ("Different Parents", "Parent Traits set to very different", "What do you predict will happen to Genetic Variation when the parents look very different from each other?"),
        ("Mixed Parents", "Parent Traits set to somewhat different", "Will the offspring look more like one parent or a mix of both?")
    ],
    "discoveries": [
        "Offspring inherit traits from BOTH parents, which is why children look similar to their parents but not identical",
        "Genetic variation means each offspring gets a unique combination of traits — that is why siblings look different",
        "Some traits are inherited (eye color, hair type) while others are influenced by the environment (scars, learned skills)",
        "Variation in a group is normal and healthy — it helps species survive changes in their environment"
    ],
    "answer": "Puppies in the same litter look different because each one gets a unique MIX of traits from mom and dad! When a mother dog and father dog have puppies, each puppy gets a random combination of the parents' traits — fur color, ear shape, size, and more. It is like shuffling a deck of cards — the same cards are in the deck, but every hand you deal is different. This natural variation is why you and your siblings might have the same parents but look a little different from each other!",
    "stem_title": "Design a Trait Prediction Game",
    "stem_mission": "Create a game that shows how mixing parent traits produces unique offspring with different combinations of features.",
    "stem_scenario": "A children's science museum wants a fun, interactive game that teaches kids about inherited traits. Your team must design a game where players combine parent trait cards to predict what their offspring will look like. Use what you learned about traits and variation!",
    "stem_questions": [
        "What traits will you include in your game — fur color, eye color, ear shape, tail length?",
        "How will you show that offspring get traits from BOTH parents, not just one?",
        "Why does your game produce different offspring every time you play?"
    ],
    "stem_design_qs": [
        "How many traits will each parent card have?",
        "How will players combine parent cards to create offspring — flipping coins, rolling dice, drawing cards?",
        "How will you draw or show what the offspring looks like based on the combined traits?",
        "Can you make it so no two offspring are exactly the same?"
    ],
    "career": "Geneticists study how traits are passed from parents to offspring and why living things look the way they do. They earn $55,000-$100,000/year.",
    "images": {
        "cover": ("cover-traits.png", "A photorealistic image of a litter of puppies with different coat colors and patterns — some spotted, some solid, some brown, some black — all cuddled together, adorable and diverse, warm natural lighting"),
        "landscape": ("landscape-traits.png", "Diverse 3rd grade students (8-9 years old, wide variety of ethnicities including Black, Latino, Asian, and white children with natural hairstyles) comparing their own traits like hair color, eye color, and height, standing in a line in a bright modern classroom, laughing and comparing features"),
        "modeling": ("modeling-traits.png", "A colorful kid-friendly scientific diagram showing two parent animals at the top with trait labels, arrows pointing down to several different-looking offspring below, showing how traits mix and produce variation, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-traits.png", "A teacher with diverse 3rd graders (8-9 years old, wide variety of ethnicities with natural hairstyles) looking at photos of animal families on a smartboard, comparing parent and baby animal features, engaged discussion"),
        "stem": ("stem-traits.png", "Diverse 3rd graders (8-9 years old, wide mix of ethnicities including Black, Latino, Asian children) playing a trait-mixing card game at tables, flipping cards and drawing offspring animals based on combined parent traits, excited and creative")
    },
    "pre_assessment": [
        "Do you look more like your mom or your dad? What features did you get from each?",
        "Why do you think brothers and sisters from the same family do not look exactly the same?",
        "Draw two parent animals and what you think their baby might look like."
    ],
    "reflections": [
        "What is the difference between a trait you inherited and something you learned or got from your environment?",
        "How did your model help you understand why no two animals (or people) are exactly alike?"
    ],
    "reflection_exemplars": [
        ("What is the difference between inherited and environmental traits?", "Inherited traits are ones you get from your parents through genes — like your eye color, hair texture, and natural height. Environmental traits are caused by things that happen to you during your life — like a scar from falling off your bike, muscles from exercising, or being able to read because someone taught you. You are born with inherited traits, but environmental traits develop as you grow and experience life.")
    ],
    "cast_items": [
        "Explain how offspring inherit traits from both parents to create unique combinations",
        "Use a model to show how genetic variation produces different-looking individuals in the same family",
        "Distinguish between inherited traits and traits influenced by the environment"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Two brown dogs have a litter of puppies. Most puppies are brown, but one is golden. Which best explains why one puppy looks different?"),
        ("Constructed Response:", "A student has brown eyes like her dad and curly hair like her mom, but her brother has blue eyes and straight hair. Using what you know about inherited traits, explain how two children from the same parents can look different. Use the words 'inherited' and 'variation' in your answer.")
    ],
    "extend_components": [
        ("Environmental Factors", "Things in the environment that change how an organism grows — like sunlight, food quality, and temperature"),
        ("Number of Offspring", "How many babies are born — more offspring means more chances to see trait variation in the group")
    ],
    "dimensions": [
        ("Science Practice", "Analyzing and Interpreting Data", "Students analyze data about parent and offspring traits to identify patterns of inheritance and explain why variation exists within groups of similar organisms."),
        ("Disciplinary Core Idea", "LS3.A Inheritance of Traits", "Many characteristics of organisms are inherited from their parents. Other characteristics result from individuals' interactions with the environment, which can range from diet to learning."),
        ("Crosscutting Concept", "Patterns", "Students identify patterns in how traits are passed from parents to offspring and how variation creates predictable differences within groups.")
    ],
    "background_intro": "Every living thing on Earth has traits — characteristics that make it unique. Understanding where traits come from helps us explain the incredible diversity of life, from the smallest flower to the largest whale.",
    "background_sections": [
        ("What Are Traits?", "Traits are observable characteristics of living things. In animals, traits include fur color, eye color, body size, ear shape, and behavior patterns. In plants, traits include flower color, leaf shape, and height. Some traits are structural (what the organism looks like), while others are behavioral (what the organism does). Every individual organism has its own unique combination of traits."),
        ("Inherited vs. Environmental Traits", "Inherited traits are passed from parents to offspring through genes — microscopic instructions inside every cell. Eye color, hair texture, skin tone, and blood type are all inherited. Environmental traits are influenced by the world around the organism. A plant grown in shade will be taller and thinner than the same plant grown in sunlight. A dog that exercises a lot will be more muscular. These are changes caused by the environment, not by genes."),
        ("Why Siblings Look Different", "Even though siblings share the same parents, each one inherits a different combination of genes. Think of it like mixing paint — the same two colors can be blended in different amounts to create many shades. Each child gets roughly half their genes from mom and half from dad, but WHICH half is random each time. This genetic shuffling creates variation. Identical twins are the exception — they share the exact same genes because they developed from one fertilized egg that split in two.")
    ],
    "lever_L": "Students identify parent traits as an external component and genetic variation and offspring appearance as internal components that change based on what traits the parents have.",
    "lever_E": "Students determine that parent traits drive genetic variation, and genetic variation determines offspring appearance — different parent combinations produce different levels of variation.",
    "lever_V": "Students build a model showing how parent traits combine through genetic variation to produce unique offspring appearances.",
    "lever_Ev": "Students run similar parents, different parents, and mixed parents scenarios to observe how the diversity of parent traits affects variation and offspring appearance.",
    "lever_R": "Students add environmental factors to explore how things like food, sunlight, and temperature can change how inherited traits are expressed.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with a family of animals showing variation", "say": "Look at these puppies — they are all from the same mom and dad, but they look totally different! How is that possible?", "do": "Show photos of animal families with visible variation. Ask students to spot differences between siblings.", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn Today?", "visual": "Learning goals and vocabulary words", "say": "Today we are going to figure out why YOU look like your parents but not exactly like your brothers or sisters!", "do": "Read objectives together. Quick activity: have students identify one trait from their mom and one from their dad.", "time": "3 min"},
        {"num": "Slide 3", "title": "The Big Question", "visual": "Side-by-side parent animals and their different offspring", "say": "Why do puppies from the same litter look different? If they have the same parents, should not they all look the same?", "do": "Turn and talk: Do you look exactly like your siblings? Why or why not? Share answers.", "time": "3 min"},
        {"num": "Slide 4", "title": "Let's Build a Model!", "visual": "LEVER steps overview for kids", "say": "We are going to build a model to crack this mystery of why siblings look different!", "do": "Preview each LEVER step. Explain that scientists called geneticists study how traits are passed down.", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Sort the Parts", "visual": "Component cards for the traits model", "say": "What parts of this system can we identify? Where do the traits come from?", "do": "Guide sorting of three components. Explain parent traits are external because they exist before the offspring is born.", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect with Arrows", "visual": "Arrow diagrams between trait components", "say": "When parents have very different traits, does variation go up or down? What about offspring appearance?", "do": "Help students draw arrows showing parent traits drive genetic variation, which determines offspring appearance.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Run the Simulation!", "visual": "Simulation comparing parent and offspring traits", "say": "Let us test our model! What happens when similar parents have babies versus very different parents?", "do": "Have students predict first, then run each scenario. Compare offspring from similar vs. different parents.", "time": "8 min"},
        {"num": "Slide 8", "title": "What Did We Discover?", "visual": "Key findings about inherited traits and variation", "say": "Now we know — every living thing is unique because of the special MIX of traits from both parents!", "do": "Summarize discoveries. Do a class trait survey (hair color, eye color, attached/detached earlobes) and chart the variation.", "time": "7 min"}
    ],
    "sort_reasoning": "Parent Traits are external because they are determined before the offspring is born — the parents already have their traits, and those traits enter the system as inputs. Genetic Variation and Offspring Appearance are internal because they are outcomes that happen INSIDE the system when parent traits combine during reproduction.",
    "relationships": [
        ("Parent Traits to Genetic Variation", "POSITIVE (+)", "When parents have more diverse traits between them, there are more possible combinations for offspring. Two very different parents can produce offspring with a wider range of appearances than two very similar parents."),
        ("Genetic Variation to Offspring Appearance", "POSITIVE (+)", "More genetic variation means more possible outcomes for what offspring look like. High variation means each sibling is likely to look noticeably different, while low variation means siblings will look more similar to each other.")
    ],
    "sim_answers": [
        ("Similar Parents Scenario", "When Parent Traits are set to very similar, Genetic Variation is low and Offspring Appearance is predictable — the offspring all look fairly similar to each other and to the parents. With less trait diversity to mix, the possible combinations are limited."),
        ("Different Parents Scenario", "When Parent Traits are set to very different, Genetic Variation is high and Offspring Appearance varies a lot. Some offspring may look more like one parent, some like the other, and some like a brand-new combination. The wider range of parent traits creates more unique mixes.")
    ],
    "stem_intro": "Present the challenge: A children's science museum wants a fun game that teaches kids about inherited traits. Your team must design a game where players combine parent trait cards to create unique offspring. Use what your model taught you about how traits mix!",
    "stem_concepts": [
        ("Trait Inheritance", "Offspring get traits from BOTH parents, not just one. Each baby receives a mix of characteristics from mom and dad, creating a unique combination."),
        ("Genetic Variation", "The random mixing of parent traits means each offspring is different. Even with the same parents, no two siblings are exactly alike — except identical twins."),
        ("Inherited vs. Environmental", "Some traits come from parents (inherited) and some come from life experiences (environmental). Your game should focus on inherited traits that are passed down.")
    ],
    "stem_eval": [
        ("Expert (4)", "Game clearly shows trait mixing from two parents, produces varied offspring, and student explains inheritance concepts from the model"),
        ("Proficient (3)", "Game produces different offspring from parent combinations and student can explain why offspring vary"),
        ("Developing (2)", "Game is built but student struggles to explain how parent traits combine to create variation"),
        ("Beginning (1)", "Game is incomplete or student cannot explain how traits are inherited from parents")
    ],
    "support": [
        "Provide pre-made parent trait cards with simple features (fur color, ear shape, tail type) so students can focus on combining them",
        "Use a coin flip or dice roll to model the randomness of which parent's trait each offspring gets",
        "Sentence frames: 'The offspring got ___ from one parent and ___ from the other parent because ___'"
    ],
    "extensions": [
        "Research how selective breeding works — why do dog breeders choose specific parents for specific traits?",
        "Survey your class for a trait like tongue rolling (can you roll your tongue?) and graph how many can vs. cannot — this is an inherited trait!",
        "Investigate identical twins — if they have the same genes, why might they still look slightly different over time?"
    ],
    "cross_curr": [
        ("Math", "Collect class data on inherited traits (hair color, eye color, earlobes) and create pie charts showing trait frequency in the class"),
        ("ELA", "Write a compare-and-contrast paragraph about two siblings (animal or human) explaining which traits they share and which are different"),
        ("Art", "Draw a family portrait of a made-up animal family, showing how parent traits mix in different ways for each offspring")
    ],
    "misconceptions": [
        ("Children are exact copies of one parent", "Children inherit traits from BOTH parents, not just one. The combination is unique each time, which is why siblings look different. You might have your mom's eyes and your dad's smile — each trait can come from either parent.", "Have students list one trait from each parent. Ask: Are you a copy of your mom? A copy of your dad? No — you are a unique MIX of both!"),
        ("All differences between individuals come from their genes", "While many traits are inherited, some differences come from the environment. A plant grown in sunlight may be shorter and greener than the same plant grown in shade. Scars, learned skills, and muscle development are all environmental, not inherited.", "Ask: If you dye your hair blue, will your future children have blue hair? No! Dye changes your appearance (environment) but not your genes. Only inherited traits are passed to children."),
        ("Siblings should look the same since they have the same parents", "Each sibling gets a DIFFERENT random combination of parent genes. With thousands of genes mixing in different ways each time, the chances of two siblings being identical are incredibly small. It is like shuffling a deck of cards — you almost never get the same hand twice.", "Shuffle a deck of cards and deal two hands of five cards. Ask: Are the hands the same? No! Same deck, different combinations. That is how siblings work — same parents, different trait mixes.")
    ]
}

L06 = {
    "id": "G03-L06",
    "title": "How Does Water Shape the Land?",
    "subtitle": "The Power of Weathering and Erosion",
    "ngss": "3-ESS2-1",
    "ngss_desc": "Represent data in tables and graphical displays to describe typical weather conditions expected during a particular season.",
    "big_question": "How can something as soft as water carve giant canyons and move huge boulders?",
    "objectives": [
        "Explain how water breaks down and moves rocks and soil over time",
        "Model how water flow, erosion strength, and land shape change are connected",
        "Describe how weathering and erosion work together to change the land"
    ],
    "vocabulary": [
        ("Weathering", "The slow breaking apart of rocks by water, ice, wind, or plant roots over time"),
        ("Erosion", "When water, wind, or ice picks up broken rock and soil and carries it to a new place"),
        ("Deposition", "When water slows down and drops the rocks and soil it was carrying, building up new landforms")
    ],
    "components": [
        ("Water Flow", "How much water is flowing over the land — from a gentle stream to a raging river or flood", True),
        ("Erosion Strength", "How much rock and soil the water can pick up and carry away — stronger flow means more erosion", False),
        ("Land Shape Change", "How much the land changes its shape — deep valleys, wide river beds, carved canyons", False)
    ],
    "think_about_it": "When water flow increases, what happens to erosion strength? Is the relationship positive or negative?",
    "scenarios": [
        ("Gentle Stream", "Set Water Flow to low and observe Erosion Strength and Land Shape Change"),
        ("Flooding River", "Set Water Flow to maximum and observe how Erosion Strength and Land Shape Change increase"),
        ("Steady Rain", "Set Water Flow to medium and compare to the gentle stream and flooding river")
    ],
    "sim_scenarios": [
        ("Gentle Stream", "Water Flow set to low", "What do you predict will happen to Land Shape Change when water flows gently?"),
        ("Flooding River", "Water Flow set to maximum", "What do you predict will happen to Erosion Strength during a powerful flood?"),
        ("Steady Rain", "Water Flow set to medium", "Will steady rain change the land as much as a flood? Why or why not?")
    ],
    "discoveries": [
        "Faster and stronger water flow causes more erosion — floods can move huge boulders and carve deep channels",
        "Even gentle water flow causes erosion over long periods of time — dripping water carved the Grand Canyon over millions of years",
        "Erosion picks up material and deposition drops it off — this is how deltas, beaches, and sandbars form",
        "Weathering and erosion are constantly changing the shape of Earth's surface, even when we cannot see it happening"
    ],
    "answer": "Water shapes the land through two powerful processes: weathering and erosion! Weathering breaks rocks into smaller pieces — water seeps into cracks, freezes, and expands, splitting the rock apart. Erosion then carries those broken pieces away. The faster the water flows, the more material it can pick up and move. Over millions of years, even a small stream can carve a massive canyon! The Grand Canyon was carved by the Colorado River — one drop at a time over 6 million years!",
    "stem_title": "Design an Erosion-Proof Hillside",
    "stem_mission": "Design a hillside model that resists erosion by using plants, rocks, or barriers to slow water flow and prevent soil from washing away.",
    "stem_scenario": "A town built on a hillside is losing soil every time it rains. The town council hired your engineering team to design a solution that prevents erosion and keeps the hillside stable. Use what you learned about water flow and erosion to protect the town!",
    "stem_questions": [
        "How do plant roots help hold soil in place during rain?",
        "What happens when water flows fast down a steep hill with no plants?",
        "How can you slow down water flow to reduce erosion?"
    ],
    "stem_design_qs": [
        "What materials will you use to build your hillside — soil, sand, gravel, clay?",
        "What will you plant or place on the hill to slow erosion — grass, rocks, terraces?",
        "How will you test your design — pouring water from a cup, using a spray bottle?",
        "How will you measure how much soil washed away?"
    ],
    "career": "Geologists study rocks, landforms, and Earth's processes including weathering and erosion. They earn $55,000-$105,000/year.",
    "images": {
        "cover": ("cover-erosion.png", "A stunning photorealistic aerial view of the Grand Canyon showing dramatic layered rock formations carved by the Colorado River, golden hour lighting, awe-inspiring natural landscape photography"),
        "landscape": ("landscape-erosion.png", "Diverse 3rd grade students (8-9 years old, wide variety of ethnicities including Black, Latino, Asian, and white children with natural hairstyles) pouring water over a sand and soil model on a tray, watching water carve channels, bright modern classroom"),
        "modeling": ("modeling-erosion.png", "A colorful kid-friendly scientific diagram showing water flowing over a hillside, arrows showing erosion carrying soil downhill, and deposition where the water slows down at the bottom, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-erosion.png", "A teacher with diverse 3rd graders (8-9 years old, wide variety of ethnicities with natural hairstyles) examining before-and-after photos of eroded landscapes on a smartboard, students pointing and comparing changes"),
        "stem": ("stem-erosion.png", "Diverse 3rd graders (8-9 years old, wide mix of ethnicities including Black, Latino, Asian children) building hillside erosion models in aluminum trays with soil, rocks, and small plants, testing with water from cups, collaborative teamwork")
    },
    "pre_assessment": [
        "Have you ever seen a stream or river carving a path through dirt or mud? What did it look like?",
        "How do you think the Grand Canyon — one of the biggest holes on Earth — was made?",
        "Draw what you think happens to soil on a hillside when it rains really hard."
    ],
    "reflections": [
        "How can something as soft as water be powerful enough to carve through solid rock?",
        "How did your model help you understand why some places on Earth look the way they do?"
    ],
    "reflection_exemplars": [
        ("How can soft water carve through solid rock?", "Water is soft compared to rock, but it has two superpowers: time and persistence. A single drop of water cannot do much, but billions of drops flowing over millions of years can wear away the hardest rock. Water also seeps into tiny cracks and freezes — when water freezes it expands, pushing the crack wider and wider until the rock splits apart. Erosion is slow but unstoppable. The Grand Canyon proves that patience and persistence can move mountains — literally!")
    ],
    "cast_items": [
        "Explain how water flow strength affects the amount of erosion and land shape change",
        "Use a model to describe the relationship between weathering, erosion, and deposition",
        "Describe how the Grand Canyon or similar landforms were shaped by water over time"
    ],
    "cast_questions": [
        ("Multiple Choice:", "After a heavy rainstorm, a student notices that a path of mud and small rocks has formed going downhill from the school playground. Which process BEST explains what happened?"),
        ("Constructed Response:", "Explain how a river can carve a canyon over time. Use the words 'water flow,' 'erosion,' and 'land shape' in your answer to describe the process step by step.")
    ],
    "extend_components": [
        ("Slope Steepness", "How steep the hill or mountain is — steeper slopes cause water to flow faster and erode more"),
        ("Vegetation Cover", "How many plants and trees cover the ground — plant roots hold soil in place and slow erosion")
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a model showing how water flow, erosion strength, and land shape change are connected, then use simulations to test how different water flows affect erosion."),
        ("Disciplinary Core Idea", "ESS2.A Earth Materials and Systems", "Wind and water can change the shape of the land. Weathering and erosion by water, ice, wind, and vegetation break rocks, soils, and sediments into smaller particles and move them around."),
        ("Crosscutting Concept", "Cause and Effect", "Students investigate how increasing water flow (cause) leads to stronger erosion and greater land shape changes (effects) in a clear cause-and-effect relationship.")
    ],
    "background_intro": "Earth's surface is constantly changing, shaped by powerful forces that work day and night, year after year. Weathering and erosion are two of the most important processes that sculpt our planet's landscapes.",
    "background_sections": [
        ("Weathering: Breaking Rocks Apart", "Weathering is the process of breaking rocks into smaller and smaller pieces. Physical weathering happens when water seeps into cracks, freezes, expands, and splits the rock (called frost wedging). Plant roots grow into cracks and push rocks apart. Chemical weathering happens when rainwater (which is slightly acidic) slowly dissolves certain minerals in rocks. Over time, even the hardest granite mountain is broken down into sand and soil by these relentless processes."),
        ("Erosion: Moving Material Around", "Erosion is the transportation of weathered material from one place to another. Water is the most powerful erosion agent — rivers carry billions of tons of sediment to the ocean every year. Wind picks up fine particles and blows them across deserts. Glaciers (giant rivers of ice) grind valleys as they slowly flow downhill. Gravity pulls loose rocks downslope in landslides. The faster the agent moves, the more material it can carry."),
        ("Deposition: Building New Landforms", "When the erosion agent slows down, it drops the material it was carrying — this is deposition. Rivers deposit sediment at their mouths, forming deltas. Wind deposits sand in dunes. Ocean waves deposit sand on beaches. The Mississippi River delta was built entirely from sediment the river carried from as far away as Montana. Erosion takes material from one place and deposition builds it up somewhere else — constantly reshaping Earth.")
    ],
    "lever_L": "Students identify water flow as an external component and erosion strength and land shape change as internal components that respond to how much water is moving across the land.",
    "lever_E": "Students determine that water flow positively affects erosion strength, and erosion strength positively affects land shape change — more water means more erosion means bigger changes to the land.",
    "lever_V": "Students build a model showing how increasing water flow leads to stronger erosion and more dramatic changes in land shape over time.",
    "lever_Ev": "Students run gentle stream, steady rain, and flooding river scenarios to observe how changing water flow affects erosion and land shape across the system.",
    "lever_R": "Students add slope steepness or vegetation cover to explore how hills and plants affect the erosion process — steeper slopes erode faster, plants slow erosion down.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with Grand Canyon or dramatic erosion imagery", "say": "Look at this canyon — it is a MILE deep! How do you think it got there? A giant shovel? An earthquake? Nope — just water!", "do": "Show photos of the Grand Canyon and other water-carved landscapes. Ask students to guess how they formed.", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn Today?", "visual": "Learning goals and vocabulary words", "say": "Today we are going to discover how something as simple as water can carve through solid rock and reshape entire mountains!", "do": "Read objectives together. Introduce vocabulary — pour a small amount of water on a pile of sand to show erosion in action.", "time": "3 min"},
        {"num": "Slide 3", "title": "The Big Question", "visual": "Water flowing over rocks and carving channels", "say": "Water is soft. Rock is hard. So how can water possibly carve through rock? This is our mystery!", "do": "Have students feel water and a rock. Ask: Which is harder? Which is softer? So how did WATER carve the Grand Canyon?", "time": "3 min"},
        {"num": "Slide 4", "title": "Let's Build a Model!", "visual": "LEVER steps overview for kids", "say": "We are going to build an erosion model to see how water really does change the land!", "do": "Preview each LEVER step. Show a quick before-and-after of a landscape that changed due to erosion.", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Sort the Parts", "visual": "Component cards for the erosion model", "say": "What parts of this erosion system can we identify? What drives the whole process?", "do": "Guide sorting of three components. Explain water flow is external because rainfall and rivers bring water to the land.", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect with Arrows", "visual": "Arrow diagrams between erosion components", "say": "When water flow gets stronger — like during a flood — does erosion increase or decrease?", "do": "Help students draw positive arrows from water flow to erosion strength, and from erosion strength to land shape change.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Run the Simulation!", "visual": "Simulation comparing different water flows", "say": "Let us test it! We will try a gentle stream, steady rain, and a powerful flood. What do you predict?", "do": "Have students predict first, then run each scenario. Compare the amount of erosion and land change in each.", "time": "8 min"},
        {"num": "Slide 8", "title": "What Did We Discover?", "visual": "Key findings about weathering and erosion", "say": "Water is the most powerful sculptor on Earth! Given enough time, it can carve through anything.", "do": "Summarize discoveries. Quick demo: drip water onto a sugar cube to show how water dissolves and erodes material. Connect to the Grand Canyon.", "time": "7 min"}
    ],
    "sort_reasoning": "Water Flow is external because it comes from rain, rivers, and weather events — it is determined by forces outside the erosion system itself. Erosion Strength and Land Shape Change are internal because they are results that happen INSIDE the system in response to how much and how fast water is flowing over the land.",
    "relationships": [
        ("Water Flow to Erosion Strength", "POSITIVE (+)", "Faster, stronger water flow picks up more rock and soil. A gentle stream might carry tiny sand particles, but a flooding river can move boulders. The more water flowing, the more powerful the erosion force."),
        ("Erosion Strength to Land Shape Change", "POSITIVE (+)", "Stronger erosion removes more material, creating bigger changes in the land. Weak erosion might make tiny grooves, but strong erosion over time can carve mile-deep canyons and reshape entire coastlines.")
    ],
    "sim_answers": [
        ("Gentle Stream Scenario", "When Water Flow is set to low, Erosion Strength is weak and Land Shape Change is minimal. The gentle water can only carry tiny particles of sand and silt. Changes to the land are very slow and barely noticeable — but over millions of years, even gentle streams carve valleys."),
        ("Flooding River Scenario", "When Water Flow is set to maximum, Erosion Strength is extremely powerful and Land Shape Change is dramatic. The rushing water carries rocks, boulders, and tons of soil. Floods can reshape landscapes in hours, carving new channels and moving material long distances.")
    ],
    "stem_intro": "Present the challenge: A town on a hillside is losing soil every time it rains. Your engineering team must design a hillside that resists erosion. Use plants, rocks, and barriers to slow water flow and keep the soil in place!",
    "stem_concepts": [
        ("Water Flow and Erosion", "Faster water erodes more soil. Slowing the water down is the key to preventing erosion. Your design should include features that reduce water speed on the hillside."),
        ("Plant Power", "Plant roots act like anchors that hold soil in place. Grass, shrubs, and trees are nature's best erosion fighters. Consider adding vegetation to your design."),
        ("Barriers and Terraces", "Rocks, walls, and terraces (flat steps cut into a hillside) slow water flow and catch sediment before it washes away. Engineers use these techniques on real hillsides around the world.")
    ],
    "stem_eval": [
        ("Expert (4)", "Hillside design effectively reduces erosion, uses multiple strategies, and student explains choices using water flow and erosion concepts from the model"),
        ("Proficient (3)", "Hillside design slows erosion and student can explain how their features reduce water flow and soil loss"),
        ("Developing (2)", "Hillside design is built but student struggles to explain how the features prevent erosion"),
        ("Beginning (1)", "Hillside design is incomplete or student cannot explain the connection between water flow and erosion")
    ],
    "support": [
        "Provide a pre-built soil hillside in a tray so students can focus on adding erosion-prevention features",
        "Show before-and-after photos of hills with and without vegetation after a rainstorm",
        "Sentence frames: 'When water flows faster, erosion is ___ because ___'"
    ],
    "extensions": [
        "Research how the Grand Canyon was formed and create a poster showing the erosion timeline over millions of years",
        "Investigate how beaches are formed by erosion and deposition — where does all that sand come from?",
        "Design an experiment to test whether grass, rocks, or mulch is best at preventing erosion on a small hill model"
    ],
    "cross_curr": [
        ("Math", "Measure the amount of soil that washes off hillside models with different amounts of water and create comparison charts"),
        ("ELA", "Write an adventure story about a drop of water traveling from a mountain peak to the ocean, describing all the erosion it causes along the way"),
        ("Art", "Create a before-and-after landscape painting showing how erosion changed a mountain over millions of years")
    ],
    "misconceptions": [
        ("Erosion only happens during floods and storms", "Erosion happens constantly, even on sunny days. Rivers, streams, and waves are always carrying sediment. Wind erodes deserts every day. Even dew and frost can cause tiny amounts of weathering. Big storms cause dramatic erosion, but the slow, everyday erosion adds up to enormous changes over time.", "Pour a tiny trickle of water on a sand pile repeatedly. Ask: Is anything moving? Yes! Even a tiny amount of water moves sand. Now imagine that happening every day for a million years."),
        ("Rocks last forever and never change", "Rocks seem permanent, but they are constantly being broken down by weathering. Water, ice, wind, plant roots, and even temperature changes slowly crack, dissolve, and crumble rocks. A granite mountain that looks unchanged today will be worn down to a hill in a few million years. No rock lasts forever.", "Show a smooth river stone and a rough rock from a field. Ask: Why is the river stone smooth? Because water has been wearing it down for thousands of years! Rocks DO change — just very slowly."),
        ("Water only erodes soft things like sand and dirt", "Water can erode any material given enough time, including the hardest rocks. The Grand Canyon is carved through layers of limestone, sandstone, and even hard granite. Water gets into microscopic cracks, freezes and expands, and slowly breaks the rock apart. Chemical reactions between water and minerals also dissolve rock from the inside out.", "Show a limestone rock with water-worn holes or grooves. Ask: Is this soft? No — it is solid rock! But water carved these holes over thousands of years. Water beats rock — it just takes patience.")
    ]
}

L07 = {
    "id": "G03-L07",
    "title": "What Happens When Habitats Change?",
    "subtitle": "How Animals Survive Environmental Change",
    "ngss": "3-LS4-4",
    "ngss_desc": "Make a claim about the merit of a solution to a problem caused when the environment changes and the types of plants and animals that live there may change.",
    "big_question": "What happens to animals when their habitat suddenly changes — do they all survive, or do some struggle?",
    "objectives": [
        "Explain how changes in a habitat affect the plants and animals that live there",
        "Model how habitat change, food availability, and animal population are connected",
        "Describe solutions that help animals survive when their habitat changes"
    ],
    "vocabulary": [
        ("Habitat", "The natural home where an animal or plant lives, which provides food, water, shelter, and space"),
        ("Population", "The number of one type of animal or plant living in an area"),
        ("Adaptation", "A special body part or behavior that helps a living thing survive in its habitat")
    ],
    "components": [
        ("Habitat Change", "How much the environment changes — from a small disturbance to a major event like a fire, flood, or drought", True),
        ("Food Availability", "How much food is left for animals after the habitat changes — less habitat means less food", False),
        ("Animal Population", "How many animals can survive in the changed habitat — depends on whether enough food and shelter remain", False)
    ],
    "think_about_it": "When habitat change increases, what happens to food availability? Is the relationship positive or negative?",
    "scenarios": [
        ("Small Change", "Set Habitat Change to low (a few trees removed) and observe Food Availability and Animal Population"),
        ("Major Change", "Set Habitat Change to maximum (wildfire burns most of forest) and observe how Food Availability and Animal Population drop"),
        ("Moderate Change", "Set Habitat Change to medium (drought reduces water) and compare to small and major changes")
    ],
    "sim_scenarios": [
        ("Small Change", "Habitat Change set to low", "What do you predict will happen to Animal Population when only a few trees are removed?"),
        ("Major Change", "Habitat Change set to maximum", "What do you predict will happen to Food Availability after a wildfire burns most of the forest?"),
        ("Moderate Change", "Habitat Change set to medium", "Will animals survive a drought better than a wildfire? Why?")
    ],
    "discoveries": [
        "When habitats change, food and shelter decrease, which causes animal populations to drop",
        "Some animals can adapt to changes — they move to new areas, change what they eat, or use different shelters",
        "Animals that are specialized (eat only one food or live in only one type of place) are most at risk when habitats change",
        "Humans can help by creating wildlife corridors, replanting forests, and protecting remaining habitats"
    ],
    "answer": "When a habitat changes, it is like someone rearranging your whole house while you are asleep! Animals that depended on specific food, water, or shelter suddenly cannot find what they need. If a forest burns, animals that lived in the trees lose their homes and food sources. Some animals adapt — birds fly to new areas, raccoons learn to find new food. But animals that can only eat one thing or live in one place may not survive. The bigger the habitat change, the more animals are affected!",
    "stem_title": "Design a Wildlife Rescue Plan",
    "stem_mission": "Create a plan to help animals survive after a major habitat change, using strategies like wildlife corridors, food stations, or habitat restoration.",
    "stem_scenario": "A forest fire has destroyed half of a national park's habitat. The park rangers need your help creating a plan to save the animals that live there. Your team must design solutions using what you learned about habitat change and animal survival!",
    "stem_questions": [
        "Which animals are most at risk after the fire — those that eat many foods or those that eat only one?",
        "How can we help animals move safely from the burned area to healthy forest?",
        "What can we do to help the burned forest grow back faster?"
    ],
    "stem_design_qs": [
        "What wildlife corridors or safe paths will you create for animals to move to healthy habitat?",
        "Will you set up temporary food or water stations for animals in need?",
        "How will you help the forest regrow — planting seeds, protecting young trees?",
        "How will you know if your plan is working — what signs of recovery will you look for?"
    ],
    "career": "Conservation Biologists work to protect endangered species and restore damaged habitats around the world. They earn $45,000-$90,000/year.",
    "images": {
        "cover": ("cover-habitat-change.png", "A split photorealistic image showing a lush green forest on one side transitioning to a burned, charred forest on the other side, dramatic contrast between healthy and damaged habitat, cinematic lighting"),
        "landscape": ("landscape-habitat-change.png", "Diverse 3rd grade students (8-9 years old, wide variety of ethnicities including Black, Latino, Asian, and white children with natural hairstyles) examining a habitat diorama showing before-and-after environmental change, bright modern classroom with nature displays"),
        "modeling": ("modeling-habitat-change.png", "A colorful kid-friendly scientific diagram showing a forest habitat before and after a fire, with arrows showing how food decreases and animal populations drop, some animals moving to new areas, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-habitat-change.png", "A teacher with diverse 3rd graders (8-9 years old, wide variety of ethnicities with natural hairstyles) looking at before-and-after photos of habitats on a smartboard, students raising hands and discussing what happened to the animals"),
        "stem": ("stem-habitat-change.png", "Diverse 3rd graders (8-9 years old, wide mix of ethnicities including Black, Latino, Asian children) creating wildlife rescue plan posters with drawings of corridors, food stations, and replanting zones, collaborative work at tables")
    },
    "pre_assessment": [
        "What would happen to a fish if its pond dried up? What choices would the fish have?",
        "Have you ever seen a place where trees were cut down or a fire burned the land? What happened to the animals?",
        "Draw a habitat before and after a big change, and show what happens to the animals that lived there."
    ],
    "reflections": [
        "Why are animals that eat only one type of food at greater risk when habitats change than animals that eat many foods?",
        "How did your model help you understand why some animals survive habitat changes while others do not?"
    ],
    "reflection_exemplars": [
        ("Why are specialized eaters at greater risk when habitats change?", "Animals that eat only one type of food are in big trouble when their habitat changes because if that ONE food disappears, they have nothing to eat. A panda that eats only bamboo is in danger if the bamboo forest is destroyed. But a raccoon that eats berries, insects, fish, and garbage can switch to whatever food is still available. Having more food options is like having a backup plan — if Plan A fails, you still have Plan B, C, and D!")
    ],
    "cast_items": [
        "Explain how habitat change affects food availability and animal populations",
        "Use model evidence to argue which animals are most at risk when habitats change",
        "Describe solutions that can help animals survive environmental changes"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A drought dries up most of the water in a wetland. Which animal is MOST likely to survive — a frog that only lives in water, or a deer that can walk to find new water sources?"),
        ("Constructed Response:", "A forest fire destroys half of a national park. Using your model, explain what happens to the animals that lived there and suggest one solution to help them survive. Use the words 'habitat change' and 'food availability' in your answer.")
    ],
    "extend_components": [
        ("Shelter Availability", "How much shelter and safe hiding places remain after the habitat changes — animals need cover from predators and weather"),
        ("Species Flexibility", "How well an animal can switch to different foods, shelters, or behaviors when its habitat changes")
    ],
    "dimensions": [
        ("Science Practice", "Engaging in Argument from Evidence", "Students make claims about the merit of solutions to problems caused by environmental changes, supporting their arguments with evidence from their model about habitat change effects."),
        ("Disciplinary Core Idea", "LS4.D Biodiversity and Humans", "Populations live in a variety of habitats, and change in those habitats affects the organisms living there. When the environment changes, some organisms survive, some move to new locations, and some die."),
        ("Crosscutting Concept", "Cause and Effect", "Students investigate how environmental changes (cause) lead to decreased food availability and lower animal populations (effects), then evaluate solutions to mitigate these effects.")
    ],
    "background_intro": "Habitats are the homes of every plant and animal on Earth. When these homes change — from natural events or human activity — the living things that depend on them face serious challenges to their survival.",
    "background_sections": [
        ("What Is a Habitat?", "A habitat provides four essential things every organism needs: food, water, shelter, and space. A coral reef provides all four for thousands of fish species. A forest provides them for birds, mammals, insects, and plants. Each species is adapted to its specific habitat — a polar bear is perfectly suited for Arctic ice but would struggle in a desert. When any of the four essentials is reduced or removed, the organisms in that habitat face survival challenges."),
        ("How Do Habitats Change?", "Habitats change through both natural events and human activities. Natural changes include wildfires, droughts, floods, volcanic eruptions, and storms. Human-caused changes include deforestation, urban development, pollution, and climate change. Some changes are sudden (a fire can destroy a forest in days) while others are gradual (pollution can slowly poison a river over years). The speed and size of the change determines how much impact it has on the living things there."),
        ("How Do Animals Respond?", "When habitats change, animals have three basic options: adapt, move, or perish. Some animals adapt by changing their behavior — eating different foods, using different shelters, or being active at different times. Some animals migrate to new habitats that still have what they need. Unfortunately, animals that cannot adapt or move may die. Generalist species (those that eat many foods and live in many habitats) survive changes better than specialist species (those that depend on one specific food or habitat).")
    ],
    "lever_L": "Students identify habitat change as an external component and food availability and animal population as internal components that respond to how much the environment has changed.",
    "lever_E": "Students determine that habitat change negatively affects food availability, and food availability positively affects animal population — more habitat destruction means less food means fewer surviving animals.",
    "lever_V": "Students build a model showing how increasing habitat change leads to decreased food availability and lower animal populations.",
    "lever_Ev": "Students run small change, moderate change, and major change scenarios to observe how the severity of habitat change affects food and population across the system.",
    "lever_R": "Students add shelter availability or species flexibility to explore why some animals survive habitat changes better than others.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide showing a changing habitat", "say": "Imagine you come home from school and your house has been completely rearranged — your bedroom is gone, the kitchen is different. How would you feel? That is what animals experience when habitats change!", "do": "Show before-and-after photos of a real habitat change (forest fire, deforestation). Ask students to describe what changed.", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn Today?", "visual": "Learning goals and vocabulary words", "say": "Today we are going to discover what happens to animals when their home — their habitat — suddenly changes!", "do": "Read objectives together. Introduce vocabulary — show pictures of different habitats and name the populations living in each.", "time": "3 min"},
        {"num": "Slide 3", "title": "The Big Question", "visual": "Animals in a changing habitat", "say": "When a forest burns or a river dries up, what happens to all the animals that lived there? Do they all make it?", "do": "Turn and talk: What would you do if your home suddenly changed? Would all your neighbors survive the change?", "time": "3 min"},
        {"num": "Slide 4", "title": "Let's Build a Model!", "visual": "LEVER steps overview for kids", "say": "We are going to build a model to test what happens when habitats change — and find out which animals survive!", "do": "Preview each LEVER step. Explain that conservation biologists study this exact question every day.", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Sort the Parts", "visual": "Component cards for the habitat model", "say": "What parts of this system can we identify? What causes the changes, and what are the results?", "do": "Guide sorting of three components. Explain habitat change is external because events like fires and droughts happen to the habitat from outside.", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect with Arrows", "visual": "Arrow diagrams between habitat components", "say": "When a habitat changes a LOT, does food go up or down? And what happens to animal population?", "do": "Help students draw a negative arrow from habitat change to food availability, and a positive arrow from food to population.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Run the Simulation!", "visual": "Simulation with habitat change scenarios", "say": "Let us test our model! What happens with a small change versus a disaster? Let us find out!", "do": "Have students predict first, then run each scenario. Discuss which animals survived in each and why.", "time": "8 min"},
        {"num": "Slide 8", "title": "What Did We Discover?", "visual": "Key findings about habitat change and survival", "say": "Habitat change is a real challenge for animals — but there ARE solutions we can use to help!", "do": "Summarize discoveries. Discuss real-world solutions: wildlife corridors, replanting programs, protected areas. Ask: What can WE do?", "time": "7 min"}
    ],
    "sort_reasoning": "Habitat Change is external because it is caused by outside events like fires, droughts, floods, or human activity — these forces act ON the habitat from outside the system. Food Availability and Animal Population are internal because they are outcomes that change INSIDE the ecosystem in response to how much the habitat has been altered.",
    "relationships": [
        ("Habitat Change to Food Availability", "POSITIVE (+)", "Greater habitat change destroys more of the food sources that animals depend on. A small change might remove a few food plants, but a major change like a wildfire can destroy most of the food supply. Note: this is actually a negative relationship in real terms — more change means LESS food — but the model shows that as habitat change increases, the impact on food availability increases."),
        ("Food Availability to Animal Population", "POSITIVE (+)", "When more food is available, more animals can survive and the population stays healthy. When food decreases, animals compete, some starve, and the population drops. Food is the most important factor determining how many animals a habitat can support.")
    ],
    "sim_answers": [
        ("Small Change Scenario", "When Habitat Change is set to low (a few trees removed), Food Availability drops slightly and Animal Population is mostly unaffected. Most animals can find other food sources nearby. The habitat recovers quickly from small disturbances."),
        ("Major Change Scenario", "When Habitat Change is set to maximum (wildfire burns most of forest), Food Availability drops dramatically and Animal Population crashes. Many animals must flee, and those that cannot leave may not survive. Only the most adaptable species remain, and full recovery may take decades.")
    ],
    "stem_intro": "Present the challenge: A forest fire has destroyed half of a national park. Park rangers need YOUR help creating a wildlife rescue plan. Design solutions using corridors, food stations, and replanting to help animals survive and the forest recover!",
    "stem_concepts": [
        ("Wildlife Corridors", "Safe pathways that connect areas of healthy habitat so animals can move from damaged areas to places with food and shelter. Corridors are like bridges between habitats."),
        ("Habitat Restoration", "Replanting trees, restoring water sources, and removing pollution to help a damaged habitat recover. Nature can heal, but sometimes it needs human help to get started."),
        ("Species Vulnerability", "Specialist species that eat only one food or live in only one habitat are most at risk. Rescue plans should prioritize the most vulnerable animals first.")
    ],
    "stem_eval": [
        ("Expert (4)", "Rescue plan includes multiple strategies (corridors, food stations, replanting), prioritizes vulnerable species, and student explains choices using model evidence"),
        ("Proficient (3)", "Rescue plan addresses animal survival and student can explain how habitat change affects populations"),
        ("Developing (2)", "Rescue plan is created but student struggles to connect solutions to habitat change concepts from the model"),
        ("Beginning (1)", "Rescue plan is incomplete or student cannot explain how habitat change affects animals")
    ],
    "support": [
        "Provide a simple map showing burned and unburned areas so students can plan corridors and restoration zones",
        "Show pictures of real wildlife corridors (highway overpasses for animals) as inspiration",
        "Sentence frames: 'When the habitat changed, food availability ___ because ___, so the animals ___'"
    ],
    "extensions": [
        "Research a real species that was saved by habitat protection (like the bald eagle or California condor) and present its story",
        "Investigate how your school or neighborhood could create a mini wildlife habitat with bird feeders, native plants, or a butterfly garden",
        "Study how forests naturally regrow after a fire — what grows first, and how long does full recovery take?"
    ],
    "cross_curr": [
        ("Math", "Create a graph showing how animal population changes as habitat loss increases from 10% to 90%, using data from the model"),
        ("ELA", "Write a letter to a park ranger explaining your wildlife rescue plan and why you think it will work, using evidence from your model"),
        ("Art", "Create a before-and-after diorama showing a habitat before and after environmental change, with animal figures showing which stayed and which left")
    ],
    "misconceptions": [
        ("Animals can just move somewhere else when their habitat changes", "Moving is not easy for all animals. Some animals (like turtles and salamanders) move very slowly. Some (like specialized insects) need very specific plants that only grow in certain places. And even fast animals face dangers when crossing roads, farmland, or cities to reach new habitat. Moving is not always an option.", "Ask: If your neighborhood flooded, could you just walk to a new house? What problems would you face? Animals face the same challenges — roads, fences, predators, and competition from animals already living in the new area."),
        ("Nature always bounces back quickly after changes", "Some habitats recover quickly (grasslands after fire can regrow in one year), but others take decades or centuries. Old-growth forests that took 500 years to develop cannot be replaced quickly. Coral reefs damaged by pollution may take 25-75 years to recover. Some ecosystems, once destroyed, may never fully return.", "Show a timeline: grass regrows in 1 year, a small tree takes 10 years, a full forest takes 100+ years. Ask: If animals need big trees to survive, can they wait 100 years?"),
        ("Only big changes matter — small changes do not affect animals", "Small, repeated changes can add up to major impacts over time. Removing a few trees each year seems small, but after 20 years, half the forest is gone. Pollution that is barely noticeable each day can build up to toxic levels over months. Scientists call this 'death by a thousand cuts' — many small changes can be just as devastating as one big change.", "Drop one marble in a glass each time you make this point throughout the lesson. By the end, the glass is overflowing. Ask: Did any single marble seem like a big deal? No, but together they filled the whole glass!")
    ]
}

L08 = {
    "id": "G03-L08",
    "title": "Can Plants Survive Without Bees?",
    "subtitle": "The Amazing World of Pollination",
    "ngss": "3-LS2-1",
    "ngss_desc": "Construct an argument that some animals form groups that help members survive.",
    "big_question": "If all the bees disappeared tomorrow, would our food still grow?",
    "objectives": [
        "Explain how bees and other pollinators help plants make seeds and fruit",
        "Model how pollinator visits, pollination success, and fruit production are connected",
        "Describe why the relationship between plants and pollinators is so important"
    ],
    "vocabulary": [
        ("Pollination", "When pollen moves from one flower to another, helping the plant make seeds and fruit"),
        ("Pollinator", "An animal that carries pollen between flowers — like bees, butterflies, hummingbirds, and bats"),
        ("Interdependence", "When two living things need each other to survive — the plant needs the bee, and the bee needs the plant")
    ],
    "components": [
        ("Pollinator Visits", "How many times bees and other pollinators visit flowers to collect nectar and spread pollen", True),
        ("Pollination Success", "How many flowers successfully receive pollen and can start making seeds", False),
        ("Fruit Production", "How much fruit and seeds the plant produces — more pollination means more fruit", False)
    ],
    "think_about_it": "When pollinator visits increase, what happens to pollination success? Is the relationship positive or negative?",
    "scenarios": [
        ("No Pollinators", "Set Pollinator Visits to zero and observe Pollination Success and Fruit Production"),
        ("Many Pollinators", "Set Pollinator Visits to maximum and observe how Pollination Success and Fruit Production change"),
        ("Some Pollinators", "Set Pollinator Visits to medium and compare to no pollinators and many pollinators")
    ],
    "sim_scenarios": [
        ("No Pollinators", "Pollinator Visits set to zero", "What do you predict will happen to Fruit Production if no bees visit the flowers?"),
        ("Many Pollinators", "Pollinator Visits set to maximum", "What do you predict will happen to Pollination Success with lots of bee visits?"),
        ("Some Pollinators", "Pollinator Visits set to medium", "Will some pollinators produce half as much fruit as many pollinators?")
    ],
    "discoveries": [
        "More pollinator visits lead to more successful pollination, which produces more fruit and seeds",
        "Without pollinators, many plants cannot reproduce — no bees means no apples, strawberries, or almonds",
        "Bees and plants are interdependent — bees need flower nectar for food, and flowers need bees to spread pollen",
        "About 75% of the food crops humans eat depend on pollinators like bees, butterflies, and hummingbirds"
    ],
    "answer": "No — most plants could NOT survive without bees and other pollinators! Here is why: for a plant to make fruit and seeds, pollen must move from one flower to another. Bees do this job by accident — they visit flowers to drink sugary nectar, and sticky pollen hitches a ride on their fuzzy bodies. When the bee visits the next flower, some pollen falls off and — pollination happens! Without bees, about 75% of our food crops would fail. No apples, no strawberries, no almonds, no chocolate!",
    "stem_title": "Build a Pollinator Garden Design",
    "stem_mission": "Design a garden that attracts the most pollinators possible, using the right flowers, colors, and layouts to create a pollinator paradise.",
    "stem_scenario": "Your school wants to help bees and butterflies by planting a pollinator garden. Your team must design the garden to attract the most pollinators. Use what you learned about pollination to choose the best flowers, arrangement, and features!",
    "stem_questions": [
        "What colors and shapes of flowers attract the most bees and butterflies?",
        "Why is it important to have flowers blooming at different times throughout the year?",
        "How will your garden help both the pollinators AND the plants in your neighborhood?"
    ],
    "stem_design_qs": [
        "Which flowers will you plant — what colors, shapes, and scents attract pollinators?",
        "How will you arrange the flowers — in rows, clusters, or scattered patches?",
        "Will you include a water source for pollinators like a shallow dish with pebbles?",
        "How will you make sure something is always blooming from spring through fall?"
    ],
    "career": "Entomologists study insects including bees and butterflies, learning how they live, pollinate, and affect ecosystems. They earn $45,000-$85,000/year.",
    "images": {
        "cover": ("cover-pollination.png", "A stunning photorealistic macro photograph of a honeybee covered in golden pollen visiting a bright purple flower, showing incredible detail of pollen grains and bee fuzz, shallow depth of field, warm natural light"),
        "landscape": ("landscape-pollination.png", "Diverse 3rd grade students (8-9 years old, wide variety of ethnicities including Black, Latino, Asian, and white children with natural hairstyles) in a school garden observing bees on flowers with magnifying glasses, sunny outdoor scene, natural light"),
        "modeling": ("modeling-pollination.png", "A colorful kid-friendly scientific diagram showing a bee traveling between two flowers, pollen grains sticking to its body, arrows showing pollen transfer leading to fruit and seed production, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-pollination.png", "A teacher with diverse 3rd graders (8-9 years old, wide variety of ethnicities with natural hairstyles) examining real flowers and looking at pollen under magnifying glasses at a table, engaged conversation about what they see"),
        "stem": ("stem-pollination.png", "Diverse 3rd graders (8-9 years old, wide mix of ethnicities including Black, Latino, Asian children) designing pollinator garden plans on large poster paper with colored markers, drawing flowers, bees, and butterflies, creative teamwork")
    },
    "pre_assessment": [
        "Have you ever watched a bee visit a flower? What was the bee doing?",
        "Where do you think fruits like apples and strawberries come from? How do they grow?",
        "Draw a bee visiting a flower and show what you think is happening."
    ],
    "reflections": [
        "Why do we say bees and flowers NEED each other — what would happen if one disappeared?",
        "How did your model help you understand why protecting pollinators is so important for our food?"
    ],
    "reflection_exemplars": [
        ("Why do bees and flowers need each other?", "Bees and flowers are interdependent — they NEED each other to survive. Flowers produce sweet nectar that bees drink for energy and pollen that bees collect to feed their babies. In return, bees carry pollen from flower to flower, which is how plants reproduce and make fruit. If bees disappeared, flowers could not spread their pollen and would stop making fruit and seeds. If flowers disappeared, bees would have no food. They are a team — and both would be in trouble without the other!")
    ],
    "cast_items": [
        "Explain how pollinator visits affect pollination success and fruit production in plants",
        "Use model evidence to argue why bees are essential for growing the food we eat",
        "Describe the interdependent relationship between pollinators and flowering plants"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A farmer notices that one apple tree near a wildflower meadow produces lots of apples, but an identical tree far from flowers produces very few. Which best explains the difference?"),
        ("Constructed Response:", "Explain what would happen to a strawberry farm if all the bees in the area disappeared. Use the words 'pollinator,' 'pollination,' and 'fruit production' in your answer.")
    ],
    "extend_components": [
        ("Flower Diversity", "How many different types of flowers are available — more variety attracts more types of pollinators"),
        ("Pesticide Use", "Chemicals sprayed on crops to kill pests — some pesticides accidentally harm pollinators too")
    ],
    "dimensions": [
        ("Science Practice", "Engaging in Argument from Evidence", "Students construct arguments using model evidence that pollinators are essential for plant reproduction and food production, supporting their claims with simulation data."),
        ("Disciplinary Core Idea", "LS2.A Interdependent Relationships in Ecosystems", "The food of almost any kind of animal can be traced back to plants. Organisms are related in food webs in which some animals eat plants for food and other animals eat the animals that eat plants. Many organisms can survive only in their particular habitats."),
        ("Crosscutting Concept", "Systems and System Models", "Students model the pollination system showing how pollinators, flowers, and fruit production are interconnected components that depend on each other to function.")
    ],
    "background_intro": "Pollination is one of nature's most important partnerships. Without pollinators, most of the foods we eat and flowers we enjoy would simply not exist. Understanding this relationship helps us protect both plants and pollinators.",
    "background_sections": [
        ("What Is Pollination?", "Pollination is the transfer of pollen from the male part of a flower (anther) to the female part (stigma), which allows the plant to make seeds and fruit. While some plants can pollinate themselves or use wind, about 87.5% of flowering plants need animal pollinators. Bees are the most important pollinators, but butterflies, moths, hummingbirds, bats, beetles, and even ants also pollinate plants. When a bee lands on a flower to drink nectar, pollen sticks to its fuzzy body and transfers to the next flower it visits."),
        ("Why Pollinators Matter for Food", "About 75% of the world's food crops depend at least partly on pollination. Without bees and other pollinators, we would lose apples, almonds, blueberries, strawberries, chocolate, coffee, and many more foods. One out of every three bites of food you eat exists because a pollinator helped make it. The economic value of pollination to agriculture is estimated at over $200 billion worldwide each year."),
        ("Threats to Pollinators", "Pollinator populations are declining worldwide due to habitat loss, pesticide use, disease, and climate change. Bees are losing wildflower meadows where they feed. Pesticides called neonicotinoids can harm bees' navigation and memory. A disease called colony collapse disorder has killed millions of honeybee colonies. Scientists and farmers are working to protect pollinators by reducing pesticide use, planting pollinator gardens, and creating bee-friendly habitats.")
    ],
    "lever_L": "Students identify pollinator visits as an external component and pollination success and fruit production as internal components that change based on how many pollinators visit the flowers.",
    "lever_E": "Students determine that pollinator visits positively affect pollination success, and pollination success positively affects fruit production — more bee visits means more flowers get pollinated means more fruit.",
    "lever_V": "Students build a model showing how increasing pollinator visits leads to greater pollination success and higher fruit production.",
    "lever_Ev": "Students run no pollinators, some pollinators, and many pollinators scenarios to observe how the number of visits affects pollination and fruit across the system.",
    "lever_R": "Students add flower diversity or pesticide use to explore how garden variety attracts more pollinators while chemicals can reduce their numbers.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with a bee on a flower", "say": "Who likes apples? Strawberries? Chocolate? What if I told you that NONE of those would exist without bees?", "do": "Hold up an apple or show a photo. Ask: What does this apple have to do with a bee? Collect ideas.", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn Today?", "visual": "Learning goals and vocabulary words", "say": "Today we are going to discover why bees are some of the most important animals on the entire planet!", "do": "Read objectives together. Show a close-up image of pollen on a bee's body and explain what pollen is.", "time": "3 min"},
        {"num": "Slide 3", "title": "The Big Question", "visual": "Grocery store with and without pollinator-dependent foods", "say": "If all the bees disappeared tomorrow, would your favorite foods still exist? Let us investigate!", "do": "Show a picture of a grocery store. Ask students to guess which foods need bees. Reveal: about 1 in 3 items would disappear!", "time": "3 min"},
        {"num": "Slide 4", "title": "Let's Build a Model!", "visual": "LEVER steps overview for kids", "say": "We are going to build a model to test exactly how important pollinators are for making food.", "do": "Preview each LEVER step. Explain that scientists study pollination to help protect our food supply.", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Sort the Parts", "visual": "Component cards for the pollination model", "say": "What parts of the pollination system can we identify? What starts the whole process?", "do": "Guide sorting of three components. Explain pollinator visits are external because the number of bees depends on factors outside the plant.", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect with Arrows", "visual": "Arrow diagrams between pollination components", "say": "When MORE bees visit, does pollination go up or down? And what about the amount of fruit?", "do": "Help students draw positive arrows from pollinator visits to pollination success, and from pollination to fruit production.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Run the Simulation!", "visual": "Simulation comparing pollinator visit levels", "say": "Let us test it! What happens with zero bees, some bees, and LOTS of bees? Predict first!", "do": "Have students predict, then run each scenario. Discuss the dramatic difference between zero and many pollinators.", "time": "8 min"},
        {"num": "Slide 8", "title": "What Did We Discover?", "visual": "Key findings about pollination and food", "say": "Now we know — bees are not just making honey, they are making our FOOD! We need to protect them!", "do": "Summarize discoveries. Show the list of foods that depend on bees. Brainstorm ways the class can help pollinators.", "time": "7 min"}
    ],
    "sort_reasoning": "Pollinator Visits are external because the number of pollinators coming to a garden depends on factors outside the plant's control — how many bees are in the area, what flowers are nearby, and whether pesticides have been used. Pollination Success and Fruit Production are internal because they are results that happen INSIDE the plant system when pollinators do their work.",
    "relationships": [
        ("Pollinator Visits to Pollination Success", "POSITIVE (+)", "Each time a bee visits a flower, it has a chance to transfer pollen. More visits mean more flowers receive pollen and more pollination events are successful. A flower visited by 10 bees has a much better chance of being pollinated than one visited by only 1."),
        ("Pollination Success to Fruit Production", "POSITIVE (+)", "Only pollinated flowers can produce fruit and seeds. The more flowers that are successfully pollinated, the more fruit the plant produces. An apple tree with 100% pollination success produces a full crop, while one with only 10% pollination produces very few apples.")
    ],
    "sim_answers": [
        ("No Pollinators Scenario", "When Pollinator Visits is set to zero, Pollination Success drops to almost nothing and Fruit Production nearly stops. Without bees carrying pollen between flowers, most flowers wither without producing fruit. Only wind-pollinated plants (like corn and wheat) would still produce."),
        ("Many Pollinators Scenario", "When Pollinator Visits is set to maximum, Pollination Success is very high and Fruit Production is abundant. Nearly every flower receives pollen, and the plant produces its full potential of fruit and seeds. This is why farmers often rent beehives to place near their orchards during blooming season.")
    ],
    "stem_intro": "Present the challenge: Your school wants to help bees and butterflies by creating a pollinator garden. Design the ultimate pollinator paradise with the right flowers, layout, and features to attract as many pollinators as possible!",
    "stem_concepts": [
        ("Flower Attraction", "Bees are attracted to blue, purple, yellow, and white flowers. Butterflies prefer red, orange, and pink. Including a variety of colors attracts the most pollinators to your garden."),
        ("Blooming Schedule", "If your garden only has flowers that bloom in June, pollinators have no food the rest of the year. Plant a mix of early, mid, and late-season flowers so something is always blooming."),
        ("Pollinator Needs", "Pollinators need more than just flowers — they also need water (shallow dishes with pebbles), shelter (bundles of hollow stems or bee houses), and protection from pesticides.")
    ],
    "stem_eval": [
        ("Expert (4)", "Garden design includes diverse flowers, a blooming schedule, water source, and shelter; student explains how the design maximizes pollinator visits using model concepts"),
        ("Proficient (3)", "Garden design attracts pollinators with appropriate flowers and student can explain the pollination-to-fruit connection"),
        ("Developing (2)", "Garden design includes flowers but student struggles to explain how it connects to pollination and food production"),
        ("Beginning (1)", "Garden design is incomplete or student cannot explain why pollinators are important for plants")
    ],
    "support": [
        "Provide a list of local pollinator-friendly plants with pictures so students can choose from real options",
        "Show a simple diagram of a bee visiting a flower with pollen transfer labeled step by step",
        "Sentence frames: 'When more pollinators visit, pollination success ___ because ___'"
    ],
    "extensions": [
        "Research the decline of bee populations worldwide and create an informational poster about how people can help",
        "Investigate other pollinators besides bees — how do butterflies, hummingbirds, and bats pollinate differently?",
        "Start a real school pollinator garden project using your design — plant seeds, observe visitors, and track results"
    ],
    "cross_curr": [
        ("Math", "Count and graph the number of different pollinators that visit a garden or flower patch during a 15-minute observation period"),
        ("ELA", "Write a persuasive letter to the school principal explaining why the school should plant a pollinator garden, using evidence from your model"),
        ("Art", "Create detailed scientific illustrations of three different pollinators (bee, butterfly, hummingbird) visiting flowers, showing pollen transfer")
    ],
    "misconceptions": [
        ("Bees only make honey — that is their purpose", "Honey production is only a small part of what bees do. Their most important role is pollination — transferring pollen between flowers so plants can make fruit and seeds. Without bee pollination, most of our food crops would fail. Honey is a bonus, but pollination is the main reason bees are so essential.", "Ask: If bees only made honey, would it matter if they disappeared? Then reveal that 75% of food crops need bees. Honey is nice, but pollination feeds the world!"),
        ("Plants can make fruit without any help from animals", "While some plants use wind or self-pollination, about 87.5% of flowering plants need animal pollinators to reproduce. Fruit only forms after successful pollination. Without pollinators, apple trees would bloom but produce no apples, strawberry plants would flower but grow no berries.", "Show two pictures: an apple tree full of fruit vs. one with only flowers and no fruit. Ask: What was the difference? One had bees visiting, the other did not."),
        ("Only honeybees are important pollinators", "There are over 20,000 species of bees worldwide, and many other animals pollinate too. Bumblebees, sweat bees, and mason bees are excellent pollinators. Butterflies, moths, hummingbirds, bats, beetles, and even some lizards pollinate flowers. A healthy ecosystem has MANY types of pollinators working together.", "Show pictures of five different pollinators. Ask: Which one is the most important? Trick question — they ALL are! Different pollinators work on different flowers, so we need all of them.")
    ]
}

L09 = {
    "id": "G03-L09",
    "title": "How Can We Protect Against Natural Hazards?",
    "subtitle": "Engineering Solutions for Dangerous Events",
    "ngss": "3-ESS3-1",
    "ngss_desc": "Make a claim about the merit of a design solution that reduces the impacts of a weather-related hazard.",
    "big_question": "How can people build things that protect them from dangerous natural events like floods, tornadoes, and earthquakes?",
    "objectives": [
        "Explain how natural hazards can cause damage and why some places are more at risk than others",
        "Model how hazard strength, protection design, and damage reduction are connected",
        "Describe engineering solutions that reduce the impact of natural hazards on people"
    ],
    "vocabulary": [
        ("Natural Hazard", "A dangerous natural event that can harm people and property — like floods, tornadoes, hurricanes, and earthquakes"),
        ("Engineering", "Using science and math to design and build solutions to problems"),
        ("Mitigation", "Actions people take to reduce the damage caused by natural hazards — like building levees or storm shelters")
    ],
    "components": [
        ("Hazard Strength", "How powerful the natural hazard is — from a minor event to a severe disaster", True),
        ("Protection Design", "How well the protective structures are designed — stronger designs resist more damage", True),
        ("Damage Reduction", "How much less damage occurs because of the protection — better design means more damage prevented", False)
    ],
    "think_about_it": "When protection design gets stronger, what happens to damage reduction? Is the relationship positive or negative?",
    "scenarios": [
        ("Weak Storm, No Protection", "Set Hazard Strength to low and Protection Design to none — observe Damage Reduction"),
        ("Strong Storm, Strong Protection", "Set Hazard Strength to high and Protection Design to maximum — observe how Damage Reduction changes"),
        ("Strong Storm, Weak Protection", "Set Hazard Strength to high and Protection Design to low — will the weak protection help at all?")
    ],
    "sim_scenarios": [
        ("Weak Storm, No Protection", "Hazard Strength low, Protection Design none", "What do you predict will happen to damage when a weak storm hits with no protection?"),
        ("Strong Storm, Strong Protection", "Hazard Strength high, Protection Design maximum", "What do you predict will happen to Damage Reduction with strong protection against a big storm?"),
        ("Strong Storm, Weak Protection", "Hazard Strength high, Protection Design low", "Will weak protection help at all against a strong storm, or will it make no difference?")
    ],
    "discoveries": [
        "Better-designed protection reduces more damage from natural hazards — engineering saves lives",
        "Even weak protection helps some, but strong hazards require strong engineering solutions",
        "No design can prevent ALL damage from the most extreme natural events — but good design greatly reduces harm",
        "Engineers study past disasters to design better protection for the future"
    ],
    "answer": "People protect themselves from natural hazards through smart engineering! For floods, engineers build levees (walls that hold back water), flood channels, and raised buildings. For tornadoes, they design storm shelters and reinforced buildings. For earthquakes, they create flexible building frames that bend without breaking. The stronger and smarter the design, the more damage it prevents. No protection is perfect against the most extreme events, but good engineering can save thousands of lives!",
    "stem_title": "Design a Flood-Proof Building",
    "stem_mission": "Design and build a model structure that can survive a flood by keeping the inside dry when water rises around it.",
    "stem_scenario": "A town near a river floods every spring. The mayor has hired your engineering team to design a building that stays dry even when floodwater rises two feet high. Use what you learned about hazard protection to create your design!",
    "stem_questions": [
        "What features of your building will keep water from getting inside?",
        "Should your building be raised above the ground, waterproofed, or both?",
        "How will you test whether your design actually works against rising water?"
    ],
    "stem_design_qs": [
        "What materials will you use for your building — waterproof or water-resistant materials?",
        "How will you seal the bottom and sides to prevent water from seeping in?",
        "Will you raise the building on stilts or pillars above the flood level?",
        "How will you test your design — placing it in a tray of water and slowly raising the level?"
    ],
    "career": "Civil Engineers design bridges, buildings, dams, and other structures that keep people safe from natural hazards. They earn $60,000-$110,000/year.",
    "images": {
        "cover": ("cover-natural-hazards.png", "A dramatic photorealistic split image showing a powerful flood on one side and a strong levee wall holding back water on the other side, demonstrating engineering protection against nature, cinematic lighting and scale"),
        "landscape": ("landscape-natural-hazards.png", "Diverse 3rd grade students (8-9 years old, wide variety of ethnicities including Black, Latino, Asian, and white children with natural hairstyles) studying a model flood barrier on their desks, pouring water to test it, bright modern classroom, natural light"),
        "modeling": ("modeling-natural-hazards.png", "A colorful kid-friendly scientific diagram showing a house with different protection features labeled — raised foundation, storm shutters, reinforced roof, sandbags — with arrows showing how each feature reduces damage, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-natural-hazards.png", "A teacher with diverse 3rd graders (8-9 years old, wide variety of ethnicities with natural hairstyles) looking at photos of natural hazards and engineering solutions on a smartboard, students discussing which designs work best"),
        "stem": ("stem-natural-hazards.png", "Diverse 3rd graders (8-9 years old, wide mix of ethnicities including Black, Latino, Asian children) building model flood-proof structures from clay, foil, and craft sticks in aluminum trays, testing with water, collaborative engineering teamwork")
    },
    "pre_assessment": [
        "What natural hazards happen where you live — floods, earthquakes, tornadoes, hurricanes, or wildfires?",
        "How do people protect their homes from dangerous weather events?",
        "Draw a building that you think could survive a flood, and explain what makes it strong."
    ],
    "reflections": [
        "Why can not engineers build something that protects against ALL natural hazards perfectly?",
        "How did your model help you understand why some buildings survive storms while others do not?"
    ],
    "reflection_exemplars": [
        ("Why can not engineers build perfect protection against all hazards?", "Natural hazards come in all sizes — from small events to extreme disasters. Engineers design protection for the hazards that are MOST LIKELY to happen, not the worst-case scenario every time, because making everything survive the strongest possible event would be incredibly expensive. A house in a flood zone is designed to handle typical floods, but a once-in-500-year mega-flood might overwhelm even the best design. Engineers use data from past events to find the right balance between protection and cost.")
    ],
    "cast_items": [
        "Explain how engineering design features reduce damage from natural hazards",
        "Use model evidence to evaluate which protection designs work best against different hazard strengths",
        "Describe a real-world engineering solution that reduces the impact of a specific natural hazard"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Two houses are in a flood zone. House A is built on stilts 3 feet above the ground. House B sits flat on the ground. A flood sends 2 feet of water through the area. Which house has less damage, and why?"),
        ("Constructed Response:", "Design a solution to protect a school from a natural hazard in your area. Explain how your design reduces damage. Use the words 'hazard,' 'protection,' and 'damage reduction' in your answer.")
    ],
    "extend_components": [
        ("Warning Time", "How much advance notice people have before the hazard hits — more warning time allows better preparation"),
        ("Building Materials", "What the structure is made of — some materials resist water, wind, or shaking better than others")
    ],
    "dimensions": [
        ("Science Practice", "Engaging in Argument from Evidence", "Students make claims about the merit of design solutions that reduce the impact of weather-related hazards, supporting their arguments with evidence from model simulations."),
        ("Disciplinary Core Idea", "ESS3.B Natural Hazards", "A variety of natural hazards result from natural processes. Humans cannot eliminate natural hazards but can take steps to reduce their impacts."),
        ("Crosscutting Concept", "Cause and Effect", "Students investigate how engineering design features (cause) reduce the damage from natural hazards (effect), and evaluate which designs are most effective against different hazard strengths.")
    ],
    "background_intro": "Natural hazards have threatened humans throughout history. While we cannot stop earthquakes, floods, or tornadoes from happening, engineers have developed remarkable solutions to protect people and reduce damage.",
    "background_sections": [
        ("Types of Natural Hazards", "Natural hazards include weather events (floods, tornadoes, hurricanes, blizzards, droughts), geological events (earthquakes, volcanic eruptions, landslides, tsunamis), and wildfires. Each type of hazard causes damage in different ways — floods push water into buildings, tornadoes rip structures apart with wind, and earthquakes shake buildings until they collapse. Understanding HOW each hazard causes damage is the first step in designing protection against it."),
        ("Engineering Solutions", "Engineers have developed many solutions to reduce hazard damage. Levees and floodwalls hold back floodwater. Storm shelters protect people from tornado winds. Earthquake-resistant buildings use flexible steel frames that sway without breaking. Hurricane shutters protect windows from flying debris. Seawalls shield coastlines from storm surges. Fire-resistant materials and defensible space around homes reduce wildfire damage. Each solution is specifically designed to counter the way that particular hazard causes harm."),
        ("Reducing Impact, Not Eliminating Risk", "It is important to understand that engineering can REDUCE hazard impacts but never eliminate them completely. A levee can hold back a 20-foot flood but may fail in a 30-foot flood. A tornado shelter protects against most tornadoes but could be damaged by the most extreme ones. Engineers design for the most likely hazard levels, using historical data to determine how strong protection needs to be. Building stronger costs more money, so communities must balance protection level with cost.")
    ],
    "lever_L": "Students identify hazard strength and protection design as components — hazard strength is external (we cannot control it) while protection design is also external (we choose how to build it). Damage reduction is the internal outcome.",
    "lever_E": "Students determine that stronger protection design leads to more damage reduction, while stronger hazards overwhelm weaker protections. The relationship between protection and reduction is positive.",
    "lever_V": "Students build a model showing how the interaction between hazard strength and protection design determines how much damage is prevented.",
    "lever_Ev": "Students run multiple scenarios combining different hazard strengths with different protection levels to find the best engineering solutions.",
    "lever_R": "Students add warning time or building materials to explore how early evacuation and material choice affect overall damage reduction.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with images of natural hazards and protection", "say": "What would you do if a big flood was heading straight for your neighborhood? How would you protect your home?", "do": "Show photos of natural hazards and engineering solutions side by side. Ask students what they notice about how people prepare.", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn Today?", "visual": "Learning goals and vocabulary words", "say": "Today we become engineers! We are going to figure out how to protect people from dangerous natural events!", "do": "Read objectives together. Introduce vocabulary — show examples of natural hazards and ask which ones students have heard about.", "time": "3 min"},
        {"num": "Slide 3", "title": "The Big Question", "visual": "House in a flood zone with and without protection", "say": "We cannot stop floods, tornadoes, or earthquakes. But CAN we build things that keep people safe?", "do": "Show before-and-after photos of a flood — protected buildings vs. unprotected. Ask: What made the difference?", "time": "3 min"},
        {"num": "Slide 4", "title": "Let's Build a Model!", "visual": "LEVER steps overview for kids", "say": "We are going to build a model that tests different protection designs against different hazard strengths!", "do": "Preview each LEVER step. Explain that civil engineers use models to test designs before building them in real life.", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Sort the Parts", "visual": "Component cards for the hazard protection model", "say": "What parts of this protection system can we identify? What can we control, and what is the result?", "do": "Guide sorting of three components. Discuss that both hazard strength AND protection design are inputs, but we can only control the protection.", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect with Arrows", "visual": "Arrow diagrams between hazard components", "say": "When we make protection stronger, does damage reduction go up or down? What about when the hazard gets stronger?", "do": "Help students draw arrows showing that stronger protection increases damage reduction, while stronger hazards challenge the protection.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Run the Simulation!", "visual": "Simulation comparing protection levels vs. hazard strengths", "say": "Engineer test time! Does strong protection save us from a big storm? Does weak protection help at all?", "do": "Have students predict, then run each scenario. Compare results to see which combinations prevent the most damage.", "time": "8 min"},
        {"num": "Slide 8", "title": "What Did We Discover?", "visual": "Key findings about hazard protection", "say": "Good engineering saves lives! We cannot stop natural hazards, but we CAN build smarter to reduce the damage.", "do": "Summarize discoveries. Show real examples of engineering solutions (levees, storm shelters, earthquake-proof buildings). Discuss what our community uses.", "time": "7 min"}
    ],
    "sort_reasoning": "Hazard Strength is external because natural events like floods and tornadoes happen on their own — we cannot control them. Protection Design is also external because engineers decide how to build it before the hazard occurs. Damage Reduction is internal because it is the RESULT of how well the protection holds up against the hazard — it happens inside the system when the two forces interact.",
    "relationships": [
        ("Protection Design to Damage Reduction", "POSITIVE (+)", "Stronger, better-designed protection reduces more damage. A house on 4-foot stilts prevents more flood damage than a house on 1-foot stilts. A reinforced concrete storm shelter provides more tornado protection than a wooden shed. Better engineering means less harm."),
        ("Hazard Strength to Damage Reduction", "POSITIVE (+)", "Note: this relationship means that as hazard strength increases, the CHALLENGE to damage reduction increases. Very strong hazards can overwhelm even good protection. A Category 5 hurricane may damage even well-engineered buildings, while a Category 1 hurricane causes little damage to the same structures.")
    ],
    "sim_answers": [
        ("Weak Storm, No Protection Scenario", "When Hazard Strength is low and Protection Design is none, damage is minor because the storm itself is not very strong. Even without protection, a weak storm does not cause much harm. However, adding protection would still help."),
        ("Strong Storm, Strong Protection Scenario", "When Hazard Strength is high and Protection Design is maximum, Damage Reduction is significant. The strong protection prevents most of the potential damage. While some damage may still occur from an extreme event, the well-engineered protection saves the majority of the structure and keeps people safe.")
    ],
    "stem_intro": "Present the challenge: A town near a river floods every spring. The mayor hired YOUR engineering team to design a building that stays dry even when floodwater rises two feet. Build a model, test it with real water, and prove your design works!",
    "stem_concepts": [
        ("Elevated Design", "Raising a building above the expected flood level is one of the most effective strategies. If water rises 2 feet, a building on 3-foot stilts stays dry. Height is your best friend against floods."),
        ("Waterproofing", "Sealing the bottom and sides of a structure prevents water from seeping in. Materials like plastic, rubber, and sealed concrete keep water out better than wood or cardboard."),
        ("Drainage", "Designing slopes, channels, and drains around a building directs water AWAY from the structure instead of letting it pool around the foundation. Moving water away is just as important as keeping water out.")
    ],
    "stem_eval": [
        ("Expert (4)", "Flood-proof building stays dry during testing, uses multiple strategies (elevation, waterproofing, drainage), and student explains design choices using model evidence"),
        ("Proficient (3)", "Building resists water and student can explain how the design features reduce flood damage"),
        ("Developing (2)", "Building is built but lets water in; student struggles to connect design features to damage reduction"),
        ("Beginning (1)", "Building is incomplete or student cannot explain how the design is supposed to protect against flooding")
    ],
    "support": [
        "Provide a list of waterproof vs. non-waterproof materials so students can make informed design choices",
        "Show photos of real flood-proof buildings on stilts and explain how the design works",
        "Sentence frames: 'My design protects against floods by ___ because ___'"
    ],
    "extensions": [
        "Research how your community prepares for its most common natural hazard and present what you find",
        "Design protection for a DIFFERENT natural hazard — how would you protect a building from an earthquake or tornado?",
        "Investigate why some communities are more affected by natural hazards than others — is it only about the strength of the hazard, or are there other factors?"
    ],
    "cross_curr": [
        ("Math", "Compare the cost of different protection features (stilts, waterproofing, drainage) and calculate the total cost of your design within a pretend budget"),
        ("ELA", "Write a proposal to the town mayor explaining your flood protection design and arguing why it should be built, using evidence from your model"),
        ("Art", "Create a detailed blueprint-style drawing of your flood-proof building, labeling each protective feature and explaining how it reduces damage")
    ],
    "misconceptions": [
        ("Technology can protect us from all natural hazards completely", "Even the best engineering cannot prevent ALL damage from extreme natural events. A massive earthquake, a Category 5 hurricane, or a once-in-a-thousand-year flood can overwhelm any human-made structure. Engineering reduces risk and saves lives, but it cannot eliminate all danger from nature's most powerful forces.", "Ask: Can you build a wall that stops ALL water, no matter how much? What if the water is 100 feet deep? Even dams have limits. Good engineering protects against MOST events, but nature can always be bigger."),
        ("Natural hazards are completely unpredictable and random", "While we cannot predict the exact moment a hazard will occur, scientists use data and patterns to identify WHERE hazards are most likely and roughly WHEN certain hazards are more common. Hurricanes have a season (June-November). Earthquakes cluster along fault lines. Floods happen in low-lying areas near rivers. This knowledge helps engineers build protection where it is needed most.", "Show a map of earthquake zones, flood plains, or tornado alley. Ask: Do natural hazards happen everywhere equally? No! Patterns help us predict where to build the strongest protection."),
        ("The best solution is always to just build things stronger", "Building stronger is one approach, but it is not always the best or only solution. Sometimes the smartest solution is to NOT build in dangerous areas at all, or to design buildings that move with the hazard (like flexible earthquake-resistant frames) instead of trying to resist it. Warning systems, evacuation plans, and community preparedness are just as important as physical structures.", "Ask: What is better — building the world's strongest house in a flood zone, or building a regular house on higher ground? Sometimes the smartest engineering solution is choosing a better location!")
    ]
}

L10 = {
    "id": "G03-L10",
    "title": "Why Do Objects Move Differently?",
    "subtitle": "Balanced and Unbalanced Forces",
    "ngss": "3-PS2-1",
    "ngss_desc": "Plan and conduct an investigation to provide evidence of the effects of balanced and unbalanced forces on the motion of an object.",
    "big_question": "Why does a ball roll when you push it, but a book on a table stays perfectly still?",
    "objectives": [
        "Explain the difference between balanced and unbalanced forces and how each affects motion",
        "Model how push force, friction, and object motion are connected",
        "Describe what makes objects start moving, change direction, speed up, or slow down"
    ],
    "vocabulary": [
        ("Force", "A push or a pull that can make an object move, stop, or change direction"),
        ("Balanced Forces", "When forces on an object are equal and opposite, so the object stays still or keeps moving the same way"),
        ("Unbalanced Forces", "When one force is stronger than the other, causing the object to start moving, speed up, slow down, or change direction"),
        ("Friction", "A force that happens when two surfaces rub together — it slows things down")
    ],
    "components": [
        ("Push Force", "How hard you push an object — a stronger push applies more force to make it move", True),
        ("Friction", "The rubbing force between the object and the surface it moves on — rough surfaces create more friction", False),
        ("Object Motion", "How the object moves — whether it stays still, moves slowly, or zooms across the surface", False)
    ],
    "think_about_it": "When push force increases, what happens to object motion? And what role does friction play?",
    "scenarios": [
        ("Gentle Push on Smooth Floor", "Set Push Force to low on a smooth surface and observe Friction and Object Motion"),
        ("Hard Push on Rough Carpet", "Set Push Force to high on a rough surface and observe how Friction and Object Motion change"),
        ("Hard Push on Smooth Floor", "Set Push Force to high on a smooth surface and compare to the carpet scenario")
    ],
    "sim_scenarios": [
        ("Gentle Push on Smooth Floor", "Push Force set to low, surface is smooth", "What do you predict will happen to Object Motion with a gentle push on a smooth floor?"),
        ("Hard Push on Rough Carpet", "Push Force set to high, surface is rough", "What do you predict will happen to Object Motion when friction from the carpet is fighting the push?"),
        ("Hard Push on Smooth Floor", "Push Force set to high, surface is smooth", "Will the object go farther on a smooth floor or rough carpet with the same push?")
    ],
    "discoveries": [
        "Objects only move when forces are UNBALANCED — the push must be stronger than friction for the object to move",
        "Stronger pushes create more motion because the force is more unbalanced — the push overcomes friction easily",
        "Rough surfaces create more friction, which slows objects down and makes them stop sooner",
        "A book on a table stays still because the forces are balanced — gravity pulls it down and the table pushes it up equally"
    ],
    "answer": "A ball rolls when you push it because your push creates an unbalanced force — your push is stronger than the friction trying to stop the ball, so it moves! A book on a table stays still because the forces on it are perfectly balanced — gravity pulls it down and the table pushes it up with exactly the same amount of force. When forces are balanced, nothing changes. When forces are unbalanced — when one side is stronger — that is when objects start moving, speed up, slow down, or change direction!",
    "stem_title": "Design the Ultimate Sliding Race",
    "stem_mission": "Design a race course that tests how different surfaces and push forces affect how far objects slide, proving that friction and force determine motion.",
    "stem_scenario": "A toy company wants to create a game where players push objects across different surfaces to see which goes the farthest. Your team must design and test a race course that uses at least three different surfaces to show how friction affects motion!",
    "stem_questions": [
        "Which surface lets objects slide the farthest with the same push?",
        "Why does the same push move an object different distances on different surfaces?",
        "How can you make sure each test is fair — using the same push force every time?"
    ],
    "stem_design_qs": [
        "What three surfaces will you test — tile, carpet, sandpaper, wood, ice?",
        "How will you make sure you push with the same force each time — using a ramp or a ruler launcher?",
        "What objects will you slide — a block, a toy car, a coin?",
        "How will you measure how far the object travels on each surface?"
    ],
    "career": "Mechanical Engineers study forces and motion to design machines, vehicles, and equipment that move efficiently and safely. They earn $60,000-$100,000/year.",
    "images": {
        "cover": ("cover-forces.png", "A dynamic photorealistic image of a soccer ball being kicked by a foot, showing motion blur and the moment of impact, grass field background, cinematic sports photography with dramatic lighting"),
        "landscape": ("landscape-forces.png", "Diverse 3rd grade students (8-9 years old, wide variety of ethnicities including Black, Latino, Asian, and white children with natural hairstyles) pushing toy cars across different surfaces — tile, carpet, sandpaper — measuring distances, bright modern classroom"),
        "modeling": ("modeling-forces.png", "A colorful kid-friendly scientific diagram showing balanced forces (equal arrows on a still book) versus unbalanced forces (bigger push arrow making a ball roll) with a friction arrow underneath, cartoon-style, white background, bold outlines"),
        "discussion": ("discussion-forces.png", "A teacher with diverse 3rd graders (8-9 years old, wide variety of ethnicities with natural hairstyles) doing a tug-of-war demonstration to show balanced and unbalanced forces, students pulling rope with excited expressions"),
        "stem": ("stem-forces.png", "Diverse 3rd graders (8-9 years old, wide mix of ethnicities including Black, Latino, Asian children) setting up race courses with different surface materials on desks, pushing blocks with rulers and measuring how far they slide, excited competition")
    },
    "pre_assessment": [
        "Why do you think it is easier to push a shopping cart on a smooth floor than on grass?",
        "What happens when you push a ball on ice versus on carpet? Which goes farther and why?",
        "Draw a picture showing all the forces acting on a ball when you kick it across a field."
    ],
    "reflections": [
        "Why does a book sitting on a table not fall through the table or float up into the air?",
        "How did your model help you understand why objects move differently on different surfaces?"
    ],
    "reflection_exemplars": [
        ("Why does a book not fall through the table or float up?", "A book on a table has TWO forces acting on it that are perfectly balanced. Gravity pulls the book DOWN, and the table pushes the book UP with exactly the same amount of force. These balanced forces cancel each other out, so the book stays perfectly still. It does not fall through because the table is solid and pushes back. It does not float because gravity is always pulling it down. When forces are balanced, nothing moves — and that is exactly what we see!")
    ],
    "cast_items": [
        "Explain the difference between balanced and unbalanced forces and how each affects an object's motion",
        "Use model evidence to describe how push force and friction interact to determine how far an object moves",
        "Predict what will happen to an object's motion when the balance of forces changes"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student pushes a block across a smooth table and then across a rough carpet with the same force. The block slides farther on the table. Which best explains why?"),
        ("Constructed Response:", "A toy car is sitting still on a flat table. You give it a push and it rolls across the table and eventually stops. Using what you know about forces, explain why the car started moving and why it stopped. Use the words 'unbalanced forces' and 'friction' in your answer.")
    ],
    "extend_components": [
        ("Object Weight", "How heavy the object is — heavier objects are harder to push because they press harder on the surface, creating more friction"),
        ("Surface Type", "What the surface is made of — smooth surfaces like ice create less friction than rough surfaces like sandpaper")
    ],
    "dimensions": [
        ("Science Practice", "Planning and Carrying Out Investigations", "Students plan and conduct an investigation to provide evidence of how balanced and unbalanced forces affect the motion of an object across different surfaces."),
        ("Disciplinary Core Idea", "PS2.A Forces and Motion", "Each force acts on one particular object and has both strength and a direction. An object at rest typically has multiple forces acting on it, but they add to give zero net force on the object. If the total force on the object is not zero, its motion will change."),
        ("Crosscutting Concept", "Cause and Effect", "Students investigate how changing the push force (cause) and surface friction (cause) affect the motion of objects (effect) in a predictable pattern.")
    ],
    "background_intro": "Forces are everywhere — every push, pull, twist, and turn involves forces. Understanding how forces interact helps us explain why things move the way they do, from a rolling ball to a flying airplane.",
    "background_sections": [
        ("What Is a Force?", "A force is any push or pull on an object. Forces have two important properties: strength (how hard the push or pull is) and direction (which way the push or pull goes). Forces can make objects start moving, stop moving, speed up, slow down, or change direction. Gravity is a force that pulls everything toward Earth. Friction is a force that resists motion when surfaces rub together. Magnetic force pulls certain metals. Forces are measured in units called Newtons."),
        ("Balanced vs. Unbalanced Forces", "When all the forces on an object add up to zero, the forces are balanced and the object does not change its motion. A book on a table has balanced forces — gravity pulls down and the table pushes up equally. When forces do NOT add up to zero, they are unbalanced, and the object's motion changes. Kicking a ball applies an unbalanced force — the kick is much stronger than friction, so the ball moves. Two people pushing a box with equal force from opposite sides create balanced forces — the box stays still."),
        ("Friction: The Hidden Force", "Friction is a force that opposes motion whenever two surfaces touch and slide against each other. Rough surfaces create more friction than smooth ones — that is why it is harder to slide on carpet than on ice. Friction converts kinetic energy into heat energy, which is why rubbing your hands together makes them warm. While friction can be annoying (it slows things down), it is also essential — without friction, you could not walk (your feet would slip), drive (tires would spin), or even hold a pencil (it would slide out of your hand).")
    ],
    "lever_L": "Students identify push force as an external component and friction and object motion as internal components that interact to determine how the object moves.",
    "lever_E": "Students determine that push force positively affects object motion (bigger push means more movement) while friction negatively affects it (more friction means less movement). Object motion depends on the balance between push and friction.",
    "lever_V": "Students build a model showing how push force and friction interact to determine the speed and distance of object motion.",
    "lever_Ev": "Students run scenarios with different push forces on different surfaces to observe how changing both variables affects object motion across the system.",
    "lever_R": "Students add object weight or surface type to explore how heavier objects and different materials change the balance of forces and resulting motion.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with objects in motion and at rest", "say": "Push your pencil across your desk right now. Why did it move? Now push down on your desk — why did it NOT move?", "do": "Have students push various objects and observe what happens. Collect observations: What makes things move? What keeps things still?", "time": "2 min"},
        {"num": "Slide 2", "title": "What Will We Learn Today?", "visual": "Learning goals and vocabulary words", "say": "Today we are going to figure out the secret rules that control why things move — or stay perfectly still!", "do": "Read objectives together. Introduce vocabulary with demos: push a book (force), rub hands (friction), tug-of-war (balanced/unbalanced).", "time": "3 min"},
        {"num": "Slide 3", "title": "The Big Question", "visual": "Ball rolling vs. book staying still", "say": "Why does a ball roll when you push it but a book on a table just sits there? Same world, same forces — so what is different?", "do": "Turn and talk: If everything has forces on it, why do some things move and some do not? Collect theories.", "time": "3 min"},
        {"num": "Slide 4", "title": "Let's Build a Model!", "visual": "LEVER steps overview for kids", "say": "We are going to build a model to test how pushes and friction work together to control motion!", "do": "Preview each LEVER step. Do a quick tug-of-war to demonstrate balanced (tied) and unbalanced (one side wins) forces.", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Sort the Parts", "visual": "Component cards for the forces model", "say": "What parts of this system can we identify? What forces are at work when we push something?", "do": "Guide sorting of three components. Explain push force is external because WE decide how hard to push, while friction and motion happen inside the system.", "time": "7 min"},
        {"num": "Slide 6", "title": "Activity 2: Connect with Arrows", "visual": "Arrow diagrams between force components", "say": "When you push harder, does the object move more or less? And what does friction do to motion?", "do": "Help students draw a positive arrow from push force to object motion, and discuss how friction opposes motion.", "time": "7 min"},
        {"num": "Slide 7", "title": "Activity 3: Run the Simulation!", "visual": "Simulation with force and surface scenarios", "say": "Experiment time! Same push, different surfaces — and then same surface, different pushes. What will happen?", "do": "Have students predict first, then run each scenario. Compare results: smooth vs. rough, gentle vs. hard push.", "time": "8 min"},
        {"num": "Slide 8", "title": "What Did We Discover?", "visual": "Key findings about balanced and unbalanced forces", "say": "Now we know the secret rules of motion — it is ALL about whether forces are balanced or unbalanced!", "do": "Summarize discoveries. Final demo: push a book on the table (unbalanced force makes it move), then let go (friction balances the push and it stops).", "time": "7 min"}
    ],
    "sort_reasoning": "Push Force is external because it comes from outside the object — WE decide how hard to push, and that force enters the system from the outside. Friction and Object Motion are internal because they happen INSIDE the system as a result of the push interacting with the surface. Friction is a response to the push, and motion is the outcome of the battle between push and friction.",
    "relationships": [
        ("Push Force to Object Motion", "POSITIVE (+)", "A stronger push applies more force to the object, making it move faster and farther. Double the push force and the object covers significantly more distance. The push gives the object energy to move."),
        ("Friction to Object Motion", "POSITIVE (+)", "Note: friction OPPOSES motion, but in the model, as friction increases, its EFFECT on slowing motion increases. More friction means the object slows down faster and stops sooner. Rough surfaces create high friction that fights against the push force.")
    ],
    "sim_answers": [
        ("Gentle Push on Smooth Floor Scenario", "When Push Force is low on a smooth surface, Friction is low (smooth floor) and Object Motion is moderate. The gentle push gives the object some speed, and the smooth floor does not slow it down much. The object slides a decent distance before stopping."),
        ("Hard Push on Rough Carpet Scenario", "When Push Force is high on a rough surface, Friction is very high (carpet grabs the object) and Object Motion is reduced despite the strong push. The carpet's rough fibers create a lot of friction that fights the push. The object moves but stops much sooner than it would on a smooth floor.")
    ],
    "stem_intro": "Present the challenge: A toy company wants to create a sliding game where players push objects across different surfaces. Design a race course with at least three surfaces to show how friction and push force control how far objects travel!",
    "stem_concepts": [
        ("Force and Motion", "Objects move when the push force is greater than friction. A stronger push on a smoother surface makes objects travel the farthest because both factors favor motion."),
        ("Friction Differences", "Different surfaces create different amounts of friction. Ice and smooth tile create very little friction, while carpet and sandpaper create a lot. Your race course should include surfaces with different friction levels."),
        ("Fair Testing", "To prove that surface friction matters, you need to push with the SAME force each time and only change the surface. A ramp or ruler launcher ensures consistent push force across all tests.")
    ],
    "stem_eval": [
        ("Expert (4)", "Race course tests three or more surfaces, uses consistent push force, measures distances, and student explains results using balanced/unbalanced force concepts from the model"),
        ("Proficient (3)", "Race course compares surfaces and student can explain why objects travel different distances using friction concepts"),
        ("Developing (2)", "Race course is built but student struggles to explain the connection between surface friction and object motion"),
        ("Beginning (1)", "Race course is incomplete or student cannot explain why objects move differently on different surfaces")
    ],
    "support": [
        "Provide pre-cut surface samples (tile, carpet, sandpaper, foil) so students can focus on testing rather than gathering materials",
        "Use a ramp with a marked starting line to ensure every push is the same force (gravity does the pushing consistently)",
        "Sentence frames: 'The object went farther on ___ because the friction was ___ compared to ___'"
    ],
    "extensions": [
        "Research how friction is used in sports — why do basketball shoes have textured soles? Why are bowling lanes oiled?",
        "Investigate what would happen if there were NO friction at all — could you walk, write, or even sit in a chair?",
        "Design a test to find the material with the MOST friction and the LEAST friction in your classroom"
    ],
    "cross_curr": [
        ("Math", "Measure and graph the distances objects travel on each surface, calculating the average of three trials per surface for accuracy"),
        ("ELA", "Write a lab report describing your force and friction experiment, including hypothesis, procedure, results, and conclusion"),
        ("Art", "Create a comic strip showing a character learning about balanced and unbalanced forces through everyday situations like skateboarding, playing soccer, or riding a bike")
    ],
    "misconceptions": [
        ("Objects need a constant push to keep moving", "Once an object is moving, it will keep moving until another force (like friction or a wall) stops it. This is Newton's first law of motion — an object in motion stays in motion unless acted on by an outside force. A hockey puck slides across ice for a long time because there is very little friction to stop it. You do not need to keep pushing!", "Slide a ball across a smooth floor. Ask: Are you still pushing it? No! But it keeps moving. What finally stops it? Friction! Objects do not need a constant push — they need friction to STOP."),
        ("Heavier objects always move slower", "Weight does not determine speed — force and friction do. A heavy bowling ball and a light tennis ball dropped from the same height fall at the same speed (ignoring air resistance). On a flat surface, a heavier object needs more force to START moving, but once moving, it can travel just as fast or faster than a lighter one if friction is the same.", "Roll a heavy ball and a light ball down the same ramp. Ask: Which one went farther? The heavy one! It had more momentum (force of motion) even though it was heavier. Weight is not the only thing that matters."),
        ("Friction is always bad and we should try to eliminate it", "Friction can slow things down, which sometimes seems annoying. But friction is ESSENTIAL for everyday life. Without friction, you could not walk (your feet would slip), cars could not drive (tires would spin), and you could not hold anything (everything would slide out of your hands). Brakes use friction to stop cars. Shoes use friction to grip the ground. Friction is a HELPER, not just a nuisance.", "Ask students to rub their hands together — feel the heat? That is friction! Now ask: What if there was no friction on the floor? You could not stand up, walk, or stop moving once you started sliding. Friction keeps us safe and in control!")
    ]
}

ALL_LESSONS = [L01, L02, L03, L04, L05, L06, L07, L08, L09, L10]
