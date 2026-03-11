#!/usr/bin/env python3
"""Complete lesson data for Nature's Engineers Series — ModelIt! Lessons aligned to real-world science of beaver ecology, biomimicry, ecohydrology, neuroscience, restoration ecology, and AI ethics."""

# =============================================================================
# LEVEL 1 LESSONS (Introductory — 4 components each)
# =============================================================================

L1_01 = {
    "id": "NE-L1-01",
    "title": "Does More Beavers Mean a Bigger Dam?",
    "subtitle": "How Beaver Builders Shape Their World",
    "ngss": "3-LS4-3, 3-LS4-4, 3-5-ETS1-1",
    "ngss_desc": "Construct an argument that in a particular habitat some organisms can survive well, some survive less well, and some cannot survive at all. Make a claim about the merit of a solution to a problem caused when the environment changes. Define a simple design problem reflecting a need or want that includes criteria for success.",
    "big_question": "What happens to a pond when beavers build a dam?",
    "objectives": [
        "Identify beavers as animals that change their environment by building dams",
        "Model how the number of beavers and available trees affect dam size",
        "Predict what happens to a pond when dam size changes",
        "Explain why beavers need BOTH enough members AND enough trees to build"
    ],
    "vocabulary": [
        ("Dam", "A wall built across a stream that holds water back and creates a pond"),
        ("Ecosystem Engineer", "An animal that changes its environment in big ways — like beavers building dams"),
        ("Habitat", "The place where an animal lives that provides food, water, and shelter"),
        ("Pond", "A body of still water created when a dam holds back flowing water")
    ],
    "components": [
        ("Number of Beavers", "How many beavers are living in the area — more beavers can do more building work", True),
        ("Trees Available", "How many trees are nearby that beavers can use to build their dam", True),
        ("Dam Size", "How big and strong the beaver dam grows — depends on beavers AND trees", False),
        ("Pond Size", "How much water collects behind the dam — bigger dams hold back more water", False)
    ],
    "think_about_it": "When the number of beavers increases, what happens to dam size? What if there are lots of beavers but NO trees?",
    "scenarios": [
        ("Beaver Family", "Set Number of Beavers to medium and Trees Available to high — observe what happens"),
        ("No Trees!", "Set Number of Beavers to high but Trees Available to zero — what happens to dam size?"),
        ("Lone Beaver", "Set Number of Beavers to 1 and Trees Available to high — can one beaver build a big dam?")
    ],
    "sim_scenarios": [
        ("Beaver Family", "Medium beavers, lots of trees", "What do you predict will happen to the pond when a family of beavers has plenty of trees?"),
        ("No Trees!", "Lots of beavers, no trees", "What do you predict will happen if beavers have no building materials?"),
        ("Lone Beaver", "One beaver, lots of trees", "Can a single beaver build a dam big enough to make a large pond?")
    ],
    "discoveries": [
        "Beavers need BOTH enough family members AND enough trees to build a big dam",
        "A bigger dam holds back more water, creating a bigger pond",
        "Even lots of beavers cannot build without trees — both inputs matter",
        "Beavers are ecosystem engineers because their building changes the whole environment"
    ],
    "answer": "When beavers build a dam, they change the whole environment! The dam holds back water and creates a pond. But they need two things: enough beaver family members to do the work AND enough trees to use as building material. When both are available, the dam grows big and the pond grows too — creating a whole new habitat for fish, frogs, birds, and other animals!",
    "stem_title": "Build-a-Dam Challenge",
    "stem_mission": "Design and build a miniature dam using craft sticks and clay that holds back the most water in a plastic bin.",
    "stem_scenario": "A nature park wants to understand how beaver dams work. Your engineering team has been hired to build a model dam and test how much water it can hold back. Use what your model taught you about what makes a dam successful!",
    "stem_questions": [
        "How many sticks do you need to build a dam that holds water?",
        "What happens if you use fewer sticks — does the dam still hold water?",
        "Where should you put clay to stop water from leaking through?"
    ],
    "stem_design_qs": [
        "What shape will your dam be — straight, curved, or V-shaped?",
        "How will you seal the gaps between the sticks?",
        "How will you measure how much water your dam holds back?",
        "What can you change to make your dam hold MORE water?"
    ],
    "career": "Wildlife Biologists study how animals like beavers change their environments. They work in forests, wetlands, and national parks to protect wildlife. They earn $50,000–$85,000/year.",
    "images": {
        "cover": ("cover-beaver-dam.png", "A photorealistic image of a large beaver dam across a forest stream, creating a calm pond behind it, lush green trees, clear water, golden hour sunlight, nature documentary photography style"),
        "landscape": ("landscape-beaver-builders.png", "A photorealistic image of diverse 3rd-4th grade students (8-10 years old) excitedly examining a plastic bin water table experiment in a bright modern classroom, genuinely diverse group reflecting US public school diversity — Latin American, Black, Asian/AAPI, and White students all represented, modern everyday clothing, natural window light, editorial photo quality"),
        "modeling": ("modeling-beaver-builders.png", "A photorealistic image of diverse 3rd-4th grade students (8-10 years old) working in pairs on Chromebooks building a simple digital model, Black student in the lead explaining to their group, modern classroom with colorful science posters about habitats, natural light"),
        "discussion": ("discussion-beaver-builders.png", "A photorealistic image of a Latin American female teacher leading an animated discussion with diverse 3rd-4th graders about beavers, pointing at pictures of beaver dams on a smartboard, students with hands raised eagerly, bright classroom with natural light"),
        "stem": ("stem-beaver-builders.png", "A photorealistic image of diverse 3rd-4th grade students (8-10 years old) building miniature dams with craft sticks and clay in plastic bins, water being poured to test them, Asian/AAPI student leading the group, excited collaborative teamwork")
    },
    "pre_assessment": [
        "Have you ever seen a beaver or a beaver dam? Where?",
        "Why do you think beavers build dams?",
        "Draw what you think a beaver dam looks like from the side.",
        "What do you think happens to the water when a dam blocks a stream?"
    ],
    "extend_components": [
        ("Rainfall", "How much rain falls — more rain means more water flowing toward the dam"),
        ("Number of Other Animals", "How many fish, frogs, and birds move into the new pond habitat"),
        ("Dam Strength", "How well the dam holds up over time — stronger dams last longer")
    ],
    "reflections": [
        "Why do beavers need BOTH enough family members AND enough trees to build a good dam?",
        "What would happen to all the animals living in the pond if the beavers left?",
        "How is what beavers do similar to what human builders do?",
        "Why do scientists call beavers 'ecosystem engineers'?",
        "How did your model help you understand something about nature?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how beaver population and tree availability affect dam and pond size."),
        ("Disciplinary Core Idea", "LS4.C Adaptation", "Beavers are adapted to build dams, which changes the environment to better suit their survival needs and creates habitat for other species."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify that changes in beaver population or tree availability cause predictable effects on dam size and pond size.")
    ],
    "cast_items": [
        "Explain how the number of beavers affects dam size",
        "Use a model to describe the relationship between dam size and pond size",
        "Describe why beavers need both population AND resources to build effectively"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A beaver family moves to a stream with lots of trees. Over time, what will MOST LIKELY happen? A) The stream stays the same B) A pond forms behind a new dam C) The trees grow taller D) The beavers move away"),
        ("Constructed Response:", "Using what you learned from your model, explain what would happen if a beaver family tried to build a dam but there were almost no trees nearby. Use the words 'dam size' and 'pond size' in your answer.")
    ],
    "background_intro": "Beavers are one of nature's most impressive builders. They are the only animals besides humans that significantly change their environment by building structures. Understanding how beavers shape ecosystems helps scientists manage wetlands and watersheds.",
    "background_sections": [
        ("Beavers as Ecosystem Engineers", "An ecosystem engineer is an organism that creates, significantly modifies, or destroys a habitat. Beavers are the classic example. By felling trees and building dams, they transform flowing streams into still ponds, creating entirely new ecosystems. A single beaver family can transform acres of landscape."),
        ("How Beaver Dams Work", "Beavers use their large front teeth to cut down trees, then drag branches and logs to a stream. They pack mud and vegetation between the logs to make the dam watertight. The dam slows the stream and creates a pond. Beaver dams can be tiny or massive — the longest known beaver dam in Alberta, Canada is over 2,700 feet long!"),
        ("Why Dams Matter", "The ponds created by beaver dams provide habitat for fish, amphibians, birds, insects, and plants. They also filter water, reduce flooding downstream, and recharge groundwater. When beavers are removed from an area, the dam eventually breaks down, the pond drains, and all the species that depended on it must find new homes."),
        ("Beavers and Trees", "Beavers prefer softwood trees like willow, aspen, and cottonwood. They eat the bark and use the wood for building. A single beaver can fell a tree 6 inches in diameter in about 15 minutes. If beavers use up all nearby trees, they must either travel farther (risking predators) or move to a new location.")
    ],
    "lever_L": "Students identify Number of Beavers and Trees Available as external components (things we can set) and Dam Size and Pond Size as internal components (things that change based on the externals).",
    "lever_E": "Students determine that both Number of Beavers and Trees Available positively affect Dam Size, and Dam Size positively affects Pond Size — but BOTH externals are needed.",
    "lever_V": "Students build a model showing how two external inputs feed into Dam Size, which then feeds into Pond Size.",
    "lever_Ev": "Students run scenarios with different beaver/tree combinations and observe that removing either input collapses the system.",
    "lever_R": "Students add Rainfall or Number of Other Animals to see how the pond creates a ripple effect in the ecosystem.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with beaver dam photography", "say": "Have you ever seen a beaver? They are one of nature's greatest builders! Today we are going to figure out HOW they build and WHY it matters.", "do": "Show a short video clip of beavers building a dam (30 seconds). Ask: What do you notice?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are going to build our own computer model to figure out what makes a beaver dam successful.", "do": "Have students read objectives aloud. Pre-teach 'ecosystem engineer' with examples.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "What happens to a pond when beavers build a dam?", "say": "Here is our big question. What do YOU think happens when beavers start building?", "do": "Have students turn and talk: What do you think a beaver needs to build a dam? Share out.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We are going to use a step-by-step process called LEVER to build our model. Each letter stands for a step.", "do": "Briefly introduce each LEVER step. Explain that models help us test ideas without going to a real beaver pond.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for beaver dam model", "say": "Let us figure out the parts of our system. What things affect the dam? What things CHANGE because of the dam?", "do": "Guide component sorting: Number of Beavers and Trees Available are things WE set (external). Dam Size and Pond Size CHANGE on their own (internal).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "Now let us connect them! When the number of beavers goes UP, does dam size go UP or DOWN?", "do": "Help students draw positive arrows. Key moment: What happens when trees go to zero? Dam size drops no matter how many beavers there are.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Model scenarios and predictions", "say": "Time to test! First, PREDICT what will happen. Then we will run the model and see if you were right.", "do": "Run all three scenarios. Have students record predictions BEFORE running each one. Compare results to predictions.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "So what did we discover? Beavers are amazing builders — but they need their team AND their materials!", "do": "Summarize key findings. Ask: What other animals change their environment?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Build-a-Dam Challenge", "say": "Now YOU are the beaver engineers! Build a dam that holds back the most water.", "do": "Distribute materials (craft sticks, clay, plastic bins). Groups design and test dams. Measure water held.", "time": "12 min"}
    ],
    "sort_reasoning": "Number of Beavers and Trees Available are external because they are conditions we can observe and set — they exist before the dam is built. Dam Size and Pond Size are internal because they are outcomes that CHANGE based on those inputs — the dam grows (or doesn't) depending on beavers and trees, and the pond grows depending on the dam.",
    "relationships": [
        ("Number of Beavers to Dam Size", "POSITIVE (+)", "More beavers means more workers to cut trees, haul branches, and pack mud. A larger beaver family can build a bigger dam faster."),
        ("Trees Available to Dam Size", "POSITIVE (+)", "More trees means more building material. Even a large beaver family cannot build much without trees nearby."),
        ("Dam Size to Pond Size", "POSITIVE (+)", "A bigger dam holds back more water, creating a larger and deeper pond behind it.")
    ],
    "sim_answers": [
        ("Beaver Family Scenario", "When Number of Beavers is medium and Trees Available is high, Dam Size grows to a good size and Pond Size increases noticeably. The family has plenty of materials and enough workers to build a solid dam that creates a nice pond."),
        ("No Trees Scenario", "When Number of Beavers is high but Trees Available is zero, Dam Size stays near zero and Pond Size does not increase. Even lots of beavers cannot build without materials — this shows that BOTH inputs are needed."),
        ("Lone Beaver Scenario", "When Number of Beavers is 1 and Trees Available is high, Dam Size grows very slowly and stays small. One beaver alone can do some building but cannot create a large dam — beavers work as a team.")
    ],
    "reflection_exemplars": [
        ("Why do beavers need both members and trees?", "Beavers need family members because building a dam is a LOT of work — they have to cut down trees, drag them to the water, and pack them with mud. But even a huge beaver family cannot build if there are no trees! It is like trying to build a house with a big construction crew but no wood or bricks. You need BOTH the workers AND the materials."),
        ("What happens if beavers leave?", "If the beavers leave, nobody repairs the dam when it gets damaged by storms or water flow. Over time, the dam breaks apart, the water drains out, and the pond disappears. All the fish, frogs, and birds that lived in the pond lose their home. This shows how one species — the beaver — supports an entire community of animals.")
    ],
    "stem_intro": "Present the challenge: A nature park wants to understand how beaver dams work. Your team will build a miniature dam in a plastic bin and test how much water it holds back. Use what your model taught you about what makes dams big and strong!",
    "stem_concepts": [
        ("Building Materials Matter", "Just like beavers need trees, your dam needs enough sticks. More sticks means a bigger, stronger dam."),
        ("Sealing the Gaps", "Beavers use mud to fill gaps in their dams. You can use clay to stop water from leaking through."),
        ("Shape Affects Strength", "Real beaver dams are often curved — the curve helps the dam resist the push of water. Try different shapes!")
    ],
    "stem_eval": [
        ("Expert (4)", "Dam holds water effectively, student explains connection between model findings and dam design, tests multiple designs"),
        ("Proficient (3)", "Dam holds some water and student can explain why more sticks and better sealing improve the dam"),
        ("Developing (2)", "Dam is built but leaks significantly; student struggles to connect model to design choices"),
        ("Beginning (1)", "Dam is incomplete or does not hold water; student cannot explain the connection between inputs and outcomes")
    ],
    "support": [
        "Provide a step-by-step visual guide showing how to lay sticks and pack clay",
        "Use a real beaver dam photo as a reference — point out how beavers stack and seal",
        "Sentence frames: 'When we added more sticks, the dam got __ because __'"
    ],
    "extensions": [
        "Research what animals live in beaver ponds and draw a food web",
        "Test what happens when you pour MORE water (like heavy rain) — does the dam hold?",
        "Design a dam that lets SOME water through but not all — like a real beaver dam overflow"
    ],
    "cross_curr": [
        ("Math", "Measure the water level before and after building the dam. Calculate how much water the dam holds back in milliliters."),
        ("ELA", "Write a story from the perspective of a beaver building its first dam — what challenges does it face?"),
        ("Art", "Create a before-and-after drawing showing a stream without a dam vs. the same stream with a beaver dam and pond")
    ],
    "misconceptions": [
        ("Beavers build dams to live inside", "Beavers actually live in a separate structure called a lodge — a dome-shaped pile of sticks in the middle of the pond. The dam creates the pond, and the lodge is their home IN the pond. The dam and the lodge are two different structures!", "Show a diagram with both the dam (across the stream) and the lodge (in the pond). Ask: Which one do the beavers live in?"),
        ("Dams are bad for the environment", "Human-made dams can sometimes cause problems, but BEAVER dams are part of the natural ecosystem. They create wetlands that support hundreds of species, filter water, reduce flooding, and recharge groundwater. Beaver dams are one of nature's best tools for keeping water systems healthy!", "Compare a photo of a landscape WITH and WITHOUT beaver dams — which one has more green plants and animals?"),
        ("One beaver can build a big dam by itself", "While a single beaver CAN start a dam, building and maintaining a large dam requires a family group (colony) of 4-8 beavers. Dam building is teamwork! A big dam needs constant repair, and one beaver cannot keep up with the work alone.", "Ask: Could you build a house all by yourself? Even if you had all the materials, it would take a very long time. Beavers are the same — they work as a team!")
    ],
    "game": {
        "title": "Dam Stackers",
        "type": "Physical Card Game",
        "description": "Students draw beaver cards (showing 1-5 beavers) and tree cards. They stack wooden blocks to build a dam. More beavers = more blocks per turn, but only if they also have tree cards. If they draw a flood card, the dam must withstand a ball rolled at it. First team to build a dam 10 blocks tall wins.",
        "materials": ["Wooden building blocks (50+ per group)", "Custom card deck (beaver cards 1-5, tree cards, flood cards)", "Small rubber ball for flood testing", "Flat surface or table edge as the 'stream bank'"],
        "learning_connection": "Reinforces that BOTH beavers and trees are needed — drawing a 5-beaver card with no tree cards means no blocks that turn."
    },
    "steam_activity": {
        "title": "Build-a-Dam Challenge",
        "type": "Engineering Design",
        "description": "Using craft sticks, clay, and a shallow plastic bin with a water source, student teams build a miniature dam. They measure how much water it holds back in milliliters. Teams iterate on their design — testing, measuring, redesigning. Compare results to model predictions.",
        "materials": ["Craft sticks (50 per group)", "Modeling clay (1 block per group)", "Shallow plastic bins", "Measuring cups", "Water pitcher", "Rulers", "Data recording sheets"],
        "learning_connection": "Direct physical test of the model — does adding more sticks (like more trees) really make the dam bigger? Does a bigger dam really hold more water?"
    }
}

L1_02 = {
    "id": "NE-L1-02",
    "title": "Can a Robot Swim Like a Beaver?",
    "subtitle": "How Nature Inspires Engineering Design",
    "ngss": "4-LS1-1, 3-5-ETS1-1, 3-5-ETS1-3",
    "ngss_desc": "Construct an argument that plants and animals have internal and external structures that function to support survival, growth, behavior, and reproduction. Define a simple design problem reflecting a need or want that includes criteria for success. Plan and carry out fair tests in which variables are controlled and failure points are considered.",
    "big_question": "Why do engineers study animals when they want to build better machines?",
    "objectives": [
        "Explain how a beaver's flat tail helps it swim efficiently",
        "Model how tail shape and body size affect swimming speed and energy use",
        "Describe the tradeoff between speed and energy in design",
        "Connect animal structures to engineering design inspiration"
    ],
    "vocabulary": [
        ("Biomimicry", "Designing human technology by copying ideas from nature"),
        ("Tradeoff", "When improving one thing means making another thing worse — you cannot have everything"),
        ("Efficiency", "Getting the most work done while using the least energy"),
        ("Adaptation", "A body feature that helps an animal survive in its environment")
    ],
    "components": [
        ("Tail Shape", "The design of the swimming tail — flat like a beaver, round, or pointed", True),
        ("Body Size", "How big the robot swimmer is — small, medium, or large", True),
        ("Swimming Speed", "How fast the robot moves through the water", False),
        ("Energy Used", "How much power it takes to swim — like how tired you get", False)
    ],
    "think_about_it": "When you change the tail shape to flat (like a beaver), what happens to swimming speed? What happens to energy used?",
    "scenarios": [
        ("Beaver Tail", "Set Tail Shape to flat and Body Size to medium — observe speed and energy"),
        ("Round Tail", "Set Tail Shape to round and Body Size to medium — compare to beaver tail"),
        ("Big vs. Small", "Keep Tail Shape flat but change Body Size from small to large — what changes?")
    ],
    "sim_scenarios": [
        ("Beaver Tail", "Flat tail, medium body", "What do you predict — will a flat tail make the robot fast, slow, or medium speed?"),
        ("Round Tail", "Round tail, medium body", "Will a round tail be faster or slower than the beaver's flat tail in water?"),
        ("Big vs. Small", "Flat tail, changing body size", "If we make the robot bigger, will it use more or less energy?")
    ],
    "discoveries": [
        "A flat tail (like a beaver's) pushes more water and creates more swimming speed",
        "A bigger body is harder to move through water — it uses more energy",
        "There is a TRADEOFF: being bigger gives more power but costs more energy",
        "Engineers study animal shapes because millions of years of evolution already solved these design problems"
    ],
    "answer": "Engineers study animals because nature has been testing designs for millions of years! A beaver's flat tail is perfectly shaped to push water and swim fast. When engineers copy ideas from nature — like making a robot tail flat instead of round — they get better designs faster. But there are always tradeoffs: a bigger robot is stronger but uses more energy. Good engineering means finding the best balance!",
    "stem_title": "Paddle Design Challenge",
    "stem_mission": "Design a paddle inspired by a beaver tail that moves a toy boat the farthest distance across a water bin in one push.",
    "stem_scenario": "A toy company wants to make the best paddle-powered boat. Your engineering team has been asked to test different paddle shapes inspired by animal tails. Use your model data to make your design choices!",
    "stem_questions": [
        "Which paddle shape moved the boat the farthest?",
        "Did the biggest paddle always work the best? Why or why not?",
        "How is your paddle similar to a beaver's tail?"
    ],
    "stem_design_qs": [
        "What shape will you make your paddle — flat, curved, cupped, or something else?",
        "What size should your paddle be?",
        "What material will you use — will it be stiff or flexible?",
        "How will you measure which paddle works best?"
    ],
    "career": "Biomechanical Engineers study how animals move and use those ideas to design better robots, prosthetics, and vehicles. They earn $70,000–$120,000/year.",
    "images": {
        "cover": ("cover-biomimicry.png", "A photorealistic split image — left side shows a beaver swimming underwater with its flat tail visible, right side shows a sleek underwater robot with a similar flat tail design, crystal clear water, dramatic underwater photography"),
        "landscape": ("landscape-biomimicry.png", "A photorealistic image of diverse 4th-6th grade students (9-12 years old) testing homemade paddle designs in water troughs on tables, genuinely diverse group — Latin American student leading the experiment, Black, Asian/AAPI, and White students collaborating, modern everyday clothing, bright modern classroom"),
        "modeling": ("modeling-biomimicry.png", "A photorealistic image of diverse 4th-6th grade students working on Chromebooks building a digital model of tail shapes and swimming speed, Asian/AAPI student explaining their model to the group, modern classroom with engineering posters"),
        "discussion": ("discussion-biomimicry.png", "A photorealistic image of a Black male teacher showing pictures of animal adaptations on a smartboard — beaver tail, duck feet, whale fins — while diverse students discuss which designs are best for swimming, students engaged and pointing"),
        "stem": ("stem-biomimicry.png", "A photorealistic image of diverse 4th-6th grade students cutting paddle shapes from foam board and cardboard, attaching them to toy boats, testing in water bins, Latin American and Black students collaborating in the lead, creative engineering workspace")
    },
    "pre_assessment": [
        "What animals do you think are the best swimmers? Why?",
        "If you were designing a robot that needed to swim, what animal would you copy?",
        "Draw what you think the perfect swimming tail looks like.",
        "What does the word 'tradeoff' mean to you?"
    ],
    "extend_components": [
        ("Tail Flexibility", "How stiff or bendy the tail is — flexibility affects how water flows around it"),
        ("Water Temperature", "Cold water is thicker than warm water, which changes how easy it is to swim"),
        ("Surface Texture", "Whether the tail surface is smooth, rough, or has scales")
    ],
    "reflections": [
        "Why is a flat tail better for swimming than a round one?",
        "What is the tradeoff between body size and energy use?",
        "Name another animal with a body part that engineers might want to copy. Why?",
        "Why do engineers study nature instead of just inventing everything from scratch?",
        "How did the model help you make better design choices for your paddle?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how tail shape and body size affect swimming speed and energy use."),
        ("Disciplinary Core Idea", "LS1.A Structure and Function", "The beaver's flat tail is a structure adapted for the function of swimming — its shape pushes water efficiently."),
        ("Crosscutting Concept", "Structure and Function", "Students explore how the shape (structure) of a tail determines how well it works for swimming (function).")
    ],
    "cast_items": [
        "Explain how the shape of a beaver's tail helps it swim",
        "Use a model to describe the tradeoff between body size and energy use",
        "Connect an animal structure to an engineering design"
    ],
    "cast_questions": [
        ("Multiple Choice:", "An engineer is designing an underwater robot. She tests three tail shapes: flat, round, and pointed. The flat tail moves the robot fastest. Which best explains why? A) Flat is the lightest shape B) Flat pushes the most water backward C) Flat is the easiest to build D) Flat looks most like a fish"),
        ("Constructed Response:", "A company wants to build a robot that swims like a beaver. Using what you learned from your model, explain what tail shape they should use and what tradeoff they need to think about with body size. Use the words 'speed' and 'energy' in your answer.")
    ],
    "background_intro": "Biomimicry — learning from nature to solve human engineering problems — is one of the fastest-growing fields in engineering. From bullet trains inspired by kingfisher beaks to swimsuits modeled on shark skin, nature's designs are helping engineers create better technology.",
    "background_sections": [
        ("The Beaver's Tail", "A beaver's tail is uniquely shaped — flat, wide, and paddle-like. It serves multiple functions: steering while swimming, slapping the water surface as a danger warning, propping the beaver up while gnawing trees, and storing fat for winter. The flat shape is ideal for pushing water, giving the beaver powerful swimming ability despite its heavy body."),
        ("What Is Biomimicry?", "Biomimicry comes from the Greek words 'bios' (life) and 'mimesis' (to imitate). It is the practice of learning from nature's strategies to solve human design challenges. The idea is simple: nature has been solving engineering problems for 3.8 billion years through evolution. Why start from scratch when we can learn from what already works?"),
        ("Famous Examples", "Velcro was inspired by burrs that stuck to a dog's fur. Japanese bullet trains were redesigned with kingfisher-beak-shaped noses to reduce sonic booms. Wind turbines were improved by studying the bumpy edges of humpback whale fins. In every case, studying an animal adaptation led to better human technology."),
        ("Engineering Tradeoffs", "Every design involves tradeoffs. A bigger engine is more powerful but heavier and uses more fuel. A bigger paddle pushes more water but takes more energy to move. Engineers must find the best balance — and nature has already found many of these balances through millions of years of natural selection.")
    ],
    "lever_L": "Students identify Tail Shape and Body Size as external components (design choices we make) and Swimming Speed and Energy Used as internal components (outcomes that change based on our choices).",
    "lever_E": "Students determine that flat tail shape increases swimming speed, larger body size decreases speed but increases energy use, and higher swimming speed also increases energy use.",
    "lever_V": "Students build a model showing how two design inputs produce two competing outputs — revealing the tradeoff.",
    "lever_Ev": "Students run beaver tail vs. round tail scenarios, and big vs. small body scenarios, to see the tradeoff in action.",
    "lever_R": "Students add tail flexibility or water temperature to explore how additional factors change the design equation.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Split image of beaver and robot", "say": "What do a beaver and a robot have in common? More than you think! Today we discover how engineers learn from animals.", "do": "Show side-by-side images of animal features and technologies they inspired (Velcro/burrs, bullet train/kingfisher).", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are going to figure out WHY a beaver's tail shape is so good for swimming — and use that knowledge to build something.", "do": "Have students read objectives. Pre-teach 'biomimicry' and 'tradeoff' with simple examples.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why do engineers study animals?", "say": "If you were building a robot that needed to swim, would you rather invent a brand new design or copy the best swimmer in nature?", "do": "Have students turn and talk: What animal would you copy and why?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "Let us use our modeling process to test whether copying a beaver tail really works better.", "do": "Briefly review LEVER steps.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for biomimicry model", "say": "What design choices can we make? What outcomes will we measure?", "do": "Guide sorting: Tail Shape and Body Size are choices WE make (external). Speed and Energy are results (internal).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Here is the tricky part — making the tail flat makes speed go UP, but does energy go up or down too?", "do": "Help students draw arrows. Key teaching moment: the TRADEOFF between speed and energy.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Model scenarios and predictions", "say": "Let us test: flat tail vs. round tail. Then big body vs. small body. Predict FIRST!", "do": "Run three scenarios. Record predictions before each. Discuss surprises.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "Nature already figured this out! Beavers have flat tails because evolution tested every shape over millions of years.", "do": "Summarize findings. Show real biomimicry examples: shark skin swimsuits, whale fin turbines.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Paddle Design Challenge", "say": "Now use what the model taught you to design the best paddle. Your data should guide your choices!", "do": "Distribute materials. Groups design, test, and iterate on paddle designs. Measure distance.", "time": "12 min"}
    ],
    "sort_reasoning": "Tail Shape and Body Size are external because they are design choices we make BEFORE the robot goes in the water. Swimming Speed and Energy Used are internal because they are outcomes we MEASURE — they change based on our design choices.",
    "relationships": [
        ("Tail Shape to Swimming Speed", "VARIES", "A flat tail (like a beaver's) pushes more water backward with each stroke, creating more forward thrust. A round tail pushes less water. A pointed tail pushes the least. Flat = fastest."),
        ("Body Size to Swimming Speed", "NEGATIVE (-)", "A bigger body has more surface area dragging through water (water resistance). This slows it down. Smaller bodies move through water more easily."),
        ("Body Size to Energy Used", "POSITIVE (+)", "A bigger body requires more energy to push through water. Like how it takes more effort to push a big box than a small one."),
        ("Swimming Speed to Energy Used", "POSITIVE (+)", "Going faster always takes more energy — whether you are swimming, running, or driving. Speed costs energy.")
    ],
    "sim_answers": [
        ("Beaver Tail Scenario", "With a flat tail and medium body, Swimming Speed is high and Energy Used is moderate. The flat shape is very efficient — it produces lots of speed for a reasonable energy cost. This is why beavers evolved this tail shape!"),
        ("Round Tail Scenario", "With a round tail and medium body, Swimming Speed drops noticeably but Energy Used stays similar. The round shape wastes energy pushing water to the sides instead of straight back. Less efficient design."),
        ("Big vs. Small Scenario", "When Body Size increases from small to large (keeping flat tail), Swimming Speed decreases and Energy Used increases significantly. Bigger bodies are harder to push through water — this is the tradeoff.")
    ],
    "reflection_exemplars": [
        ("Why is flat better than round for swimming?", "A flat tail pushes water straight BACKWARD, which pushes the swimmer straight FORWARD (like Newton's Third Law). A round tail pushes water in all directions — sideways, up, down — wasting energy. The flat shape is more efficient because all the push goes in the useful direction."),
        ("What is the tradeoff between size and energy?", "The tradeoff is that a bigger body is harder to move through water because there is more surface area for the water to push against. So even though a bigger body might be more powerful, it needs a LOT more energy to move. Engineers have to find the sweet spot — big enough to be useful but not so big that it wastes all its energy just moving.")
    ],
    "stem_intro": "Present the challenge: A toy company wants the best paddle-powered boat. Your team will design paddles inspired by animal tails, test them in water, and use your model data to explain why your design works best.",
    "stem_concepts": [
        ("Shape Determines Push", "The shape of your paddle determines how much water it pushes and in what direction. Flat paddles push more water straight back."),
        ("Size vs. Energy Tradeoff", "A bigger paddle pushes more water but is harder to move. Find the best balance."),
        ("Biomimicry in Action", "Your paddle design should be inspired by real animal features. Which animal's swimming tool will you copy?")
    ],
    "stem_eval": [
        ("Expert (4)", "Paddle design clearly inspired by an animal, student uses model data to explain why the shape works, tests multiple designs and iterates"),
        ("Proficient (3)", "Paddle moves the boat well and student can explain the connection between shape and speed"),
        ("Developing (2)", "Paddle is built but student struggles to explain why their shape was chosen"),
        ("Beginning (1)", "Paddle is incomplete or student cannot connect the design to the model or animal adaptations")
    ],
    "support": [
        "Provide photos of different animal tails (beaver, fish, whale, duck) for design inspiration",
        "Pre-cut basic shapes (flat, round, pointed) so students can start testing immediately",
        "Sentence frames: 'I chose a __ shape because my model showed that __'"
    ],
    "extensions": [
        "Research three more examples of biomimicry in real engineering (e.g., Velcro, bullet trains, wind turbines)",
        "Design a tail that works well for BOTH swimming and walking on land — what compromises do you have to make?",
        "Test your paddle in cold vs. warm water — does temperature change how well it works?"
    ],
    "cross_curr": [
        ("Math", "Measure the distance each paddle design pushes the boat. Create a bar graph comparing flat, round, and pointed paddles."),
        ("ELA", "Write a persuasive letter to a toy company explaining why they should use a beaver-inspired paddle design, citing your test data."),
        ("Art", "Create a detailed scientific illustration of a beaver showing all the body parts that help it swim, with labels and function descriptions.")
    ],
    "misconceptions": [
        ("Copying animals exactly will give the best design", "Biomimicry means being INSPIRED by nature, not making an exact copy. Engineers adapt natural designs for human needs. A robot does not need fur or teeth like a beaver — just the tail shape principle. Good biomimicry takes the IDEA and improves it for the specific use.", "Compare a humpback whale fin to a wind turbine blade — they are similar but not identical. The engineer took the bumpy-edge CONCEPT, not the whole fin."),
        ("Bigger is always better in engineering", "Bigger often means more powerful, but it ALSO means more energy needed, more materials, and more cost. The best design is not always the biggest — it is the one that does the job with the least waste. This is why engineers care about EFFICIENCY, not just size.", "Compare two paper airplanes: a large one and a small one. Which flies farther? Often the smaller, more efficient design wins."),
        ("Animals designed their own bodies", "Animals did not choose their features. Evolution through natural selection shaped them over millions of years. Beavers with slightly flatter tails swam better, survived longer, and had more babies. Over thousands of generations, the flat tail became standard. Nature does not design — it selects.", "Play a quick selection game: give each student a random 'tail shape' card, then 'test' them — flat tails survive and 'reproduce,' round tails don't. After 3 rounds, which shape dominates?")
    ],
    "game": {
        "title": "Tail Race",
        "type": "Hands-On Experiment Race",
        "description": "Students cut three different tail shapes from foam board (flat, round, pointed), attach them to identical toy boat bodies, and race them in a water trough. They predict which will be fastest, test, then compare to the model. Quick, splashy, memorable.",
        "materials": ["Foam board sheets", "Scissors", "Identical toy boat bodies or carved pool noodle boats", "Long water trough or rain gutter", "Stopwatch", "Data recording sheets"],
        "learning_connection": "Directly tests the model's prediction that flat tails produce the most speed in water."
    },
    "steam_activity": {
        "title": "Paddle Design Challenge",
        "type": "Engineering Design + Art",
        "description": "Using recycled materials (cardboard, tape, popsicle sticks, foam), students design a paddle/propulsion system inspired by a beaver tail. Test in a water bin — measure distance traveled in one push. Iterate on the design based on data. Classic engineering design loop with biomimicry inspiration.",
        "materials": ["Cardboard scraps", "Foam sheets", "Popsicle sticks", "Waterproof tape", "Small toy boats", "Water bins", "Rulers and measuring tape", "Data recording sheets"],
        "learning_connection": "Students apply the model's tail shape findings to a real engineering challenge, experiencing the design-test-redesign cycle firsthand."
    }
}

L1_03 = {
    "id": "NE-L1-03",
    "title": "Sponge vs. Pavement",
    "subtitle": "Where Does the Water Go When It Rains?",
    "ngss": "MS-ESS2-4, MS-ESS3-3",
    "ngss_desc": "Develop a model to describe the cycling of water through Earth's systems driven by energy from the sun and the force of gravity. Apply scientific principles to design a method for monitoring and minimizing a human impact on the environment.",
    "big_question": "Why do some places flood when it rains and other places do not?",
    "objectives": [
        "Explain how different ground surfaces absorb or deflect water",
        "Model how ground type and rainfall affect water absorption and runoff",
        "Predict which surfaces will cause more flooding during a rainstorm",
        "Connect human land use decisions to flooding problems"
    ],
    "vocabulary": [
        ("Absorption", "When water soaks INTO the ground instead of flowing across the surface"),
        ("Runoff", "Water that flows ACROSS the surface because the ground cannot absorb it"),
        ("Permeable", "A surface that lets water pass through it — like soil or gravel"),
        ("Impermeable", "A surface that blocks water from passing through — like pavement or rock")
    ],
    "components": [
        ("Ground Type", "What the surface is made of — soil, gravel, rock, or pavement", True),
        ("Rainfall Amount", "How much rain falls on the surface — light drizzle to heavy downpour", True),
        ("Water Absorbed", "How much water soaks into the ground below the surface", False),
        ("Runoff", "How much water flows across the surface toward streams, drains, and low spots", False)
    ],
    "think_about_it": "When rainfall increases, what happens to both water absorbed AND runoff? Do they both go up, or does one go up while the other stays the same?",
    "scenarios": [
        ("Rain on Soil", "Set Ground Type to soil and Rainfall to heavy — where does the water go?"),
        ("Rain on Pavement", "Set Ground Type to pavement and Rainfall to heavy — compare to soil"),
        ("Light vs. Heavy Rain", "Keep Ground Type as soil but change Rainfall from light to heavy — what changes?")
    ],
    "sim_scenarios": [
        ("Rain on Soil", "Soil surface, heavy rain", "What do you predict — will most water absorb or run off on soil?"),
        ("Rain on Pavement", "Pavement surface, heavy rain", "What do you predict will happen to runoff when rain hits pavement?"),
        ("Light vs. Heavy Rain", "Soil surface, changing rainfall", "If we double the rain on soil, does absorption double too?")
    ],
    "discoveries": [
        "Soil absorbs much more water than pavement — it acts like a sponge",
        "Pavement is nearly impermeable — almost all rain becomes runoff",
        "More rain means more of BOTH absorption and runoff, but the ground type determines the split",
        "When cities replace soil with pavement, they create flooding problems because water has nowhere to soak in"
    ],
    "answer": "Some places flood because the ground cannot absorb the rain! Soil acts like a sponge — it soaks up water and stores it underground. But pavement and concrete are impermeable — they block water from soaking in, so almost ALL the rain becomes runoff that flows across the surface. When cities pave over natural ground, they turn rain into floods because the water has nowhere to go!",
    "stem_title": "Schoolyard Watershed Map",
    "stem_mission": "Map every surface type on your school grounds and predict where water collects during a rainstorm.",
    "stem_scenario": "The school principal wants to reduce puddles and flooding on the playground. Your team has been asked to study the school grounds, identify problem areas, and recommend solutions based on your model data.",
    "stem_questions": [
        "What percentage of your school grounds is covered by pavement vs. grass vs. bare soil?",
        "Where do the biggest puddles form after rain? Is it on grass or pavement?",
        "What could the school do to reduce flooding on the playground?"
    ],
    "stem_design_qs": [
        "How will you map the different surface types on your school grounds?",
        "How will you measure or estimate the area of each surface type?",
        "Where do you predict the water will flow based on your model?",
        "What changes would you recommend to reduce runoff?"
    ],
    "career": "Hydrologists study how water moves through the environment — where it flows, where it soaks in, and where it causes problems. They help cities design better drainage and prevent floods. They earn $65,000–$100,000/year.",
    "images": {
        "cover": ("cover-sponge-pavement.png", "A dramatic split image — left side shows rain soaking into lush green soil with earthworms visible, right side shows rain bouncing off grey pavement creating a rushing flood of runoff, overhead view, cinematic weather photography"),
        "landscape": ("landscape-water-absorption.png", "A photorealistic image of diverse 6th-7th grade students (11-13 years old) pouring water onto different surface samples in clear containers on a lab table — soil, gravel, and a tile, genuinely diverse group with Black student recording data, Latin American student pouring, Asian/AAPI student observing, modern science lab"),
        "modeling": ("modeling-water-absorption.png", "A photorealistic image of diverse 6th-7th grade students working in pairs on laptops building a watershed model, White female student and Black male student collaborating, modern classroom with water cycle posters"),
        "discussion": ("discussion-water-absorption.png", "A photorealistic image of an Asian/AAPI male teacher showing a diagram of permeable vs. impermeable surfaces on a smartboard, diverse students discussing and debating, some pointing at the diagram, bright classroom"),
        "stem": ("stem-water-absorption.png", "A photorealistic image of diverse 6th-7th grade students outside on school grounds with clipboards, mapping surface types, Latin American female student leading the group and pointing at different ground surfaces, sunny day, authentic outdoor learning")
    },
    "pre_assessment": [
        "Where does rain go after it hits the ground?",
        "Why do you think parking lots get big puddles but forests usually do not?",
        "Draw what you think happens to rain when it hits soil vs. when it hits pavement.",
        "What does the word 'absorb' mean to you?"
    ],
    "extend_components": [
        ("Slope Angle", "How steep the ground is — steeper slopes mean water flows faster before it can soak in"),
        ("Vegetation Cover", "Plants and their roots help water soak into the ground and slow down runoff"),
        ("Soil Saturation", "How much water the soil already holds — saturated soil cannot absorb more")
    ],
    "reflections": [
        "Why does a parking lot flood more easily than a field of grass?",
        "What happens underground when soil absorbs water?",
        "How do cities make flooding worse by building roads and buildings?",
        "What are some ways to add more permeable surfaces to a city?",
        "How did the model help you predict where water goes during a storm?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how ground type and rainfall determine the split between absorption and runoff."),
        ("Disciplinary Core Idea", "ESS2.C The Roles of Water in Earth's Surface Processes", "Water cycles through Earth's systems — ground type determines whether precipitation is absorbed or becomes surface runoff."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify that ground type and rainfall amount cause predictable effects on absorption and runoff patterns.")
    ],
    "cast_items": [
        "Explain how different ground surfaces affect water absorption",
        "Use a model to predict where runoff will flow",
        "Connect human land use to changes in water flow patterns"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A city replaces a grass field with a new parking lot. During the next heavy rain, what will MOST LIKELY happen? A) Less flooding nearby B) More flooding nearby C) No change in flooding D) The rain will stop sooner"),
        ("Constructed Response:", "Your model shows that pavement creates much more runoff than soil during heavy rain. Using this evidence, explain why cities that have more pavement tend to have worse flooding problems. Use the words 'absorption' and 'runoff' in your answer.")
    ],
    "background_intro": "Water is constantly cycling through Earth's systems — evaporating from oceans, forming clouds, falling as rain, soaking into soil or flowing across surfaces. Understanding how water moves across different surfaces is critical for managing floods, droughts, and water quality.",
    "background_sections": [
        ("Permeable vs. Impermeable", "Permeable surfaces have tiny spaces (pores) between particles that water can flow through. Soil, gravel, and sand are permeable. Impermeable surfaces block water — concrete, asphalt, and solid rock have no pores. When rain hits permeable ground, it soaks in. When it hits impermeable ground, it runs off."),
        ("The Urban Flooding Problem", "In natural landscapes, about 10% of rainfall becomes runoff and 90% soaks in. In cities with 75% impermeable surfaces, those numbers flip — 55% or more becomes runoff. This overwhelms storm drains, causes flash flooding, and carries pollutants into waterways. Urban flooding is getting worse as cities grow."),
        ("Green Infrastructure Solutions", "Cities are increasingly using 'green infrastructure' to reduce runoff: rain gardens, permeable pavement, green roofs, bioswales, and urban trees. These solutions mimic natural ground by allowing water to soak in. Some cities, like Philadelphia, have invested billions in green infrastructure instead of expanding traditional storm drains."),
        ("Connection to Beaver Ecology", "In natural watersheds, beaver dams serve a similar function to green infrastructure — they slow water flow, spread it across floodplains, and allow it to soak into the ground. Research shows that watersheds with active beaver populations have significantly less flooding and better groundwater recharge than those without beavers.")
    ],
    "lever_L": "Students identify Ground Type and Rainfall Amount as external components (conditions we set or observe) and Water Absorbed and Runoff as internal components (outcomes that change based on ground type and rainfall).",
    "lever_E": "Students determine that rainfall increases BOTH absorption and runoff, but ground type determines the RATIO — soil favors absorption while pavement favors runoff.",
    "lever_V": "Students build a model showing how two externals produce two competing internals, with ground type acting as a 'switch' that changes the balance.",
    "lever_Ev": "Students run soil vs. pavement scenarios and light vs. heavy rain scenarios to see how the balance shifts.",
    "lever_R": "Students add slope angle or vegetation cover to see how additional factors modify the absorption-runoff split.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Split image of soil absorbing vs. pavement flooding", "say": "Have you ever noticed that some places get huge puddles when it rains and other places do not? Why is that?", "do": "Show two photos side by side: a flooded parking lot vs. a forest after the same rainstorm. Ask: What is different?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are going to build a model that explains WHERE water goes when it rains — and why cities flood.", "do": "Have students read objectives. Pre-teach 'permeable' and 'impermeable' with demo: pour water on a sponge vs. a plastic plate.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why do some places flood and others do not?", "say": "Think about it — the same rain falls on a forest AND a parking lot. One floods, one does not. What is going on?", "do": "Have students discuss in pairs and share out their hypotheses.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We are going to model this system to figure out exactly what controls where water goes.", "do": "Briefly review LEVER steps.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards", "say": "What factors determine where rain goes? What can we control, and what happens as a RESULT?", "do": "Guide sorting: Ground Type and Rainfall are external. Water Absorbed and Runoff are internal. Key question: Can the same rain produce BOTH absorption and runoff?", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Here is what makes this interesting — the same rain can go two different directions depending on the ground!", "do": "Draw arrows. Key teaching: Water Absorbed and Runoff are COMPETING — what soaks in cannot run off, and vice versa.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Model scenarios", "say": "Let us test soil vs. pavement with the same heavy rain. Predict first — then run it!", "do": "Run all three scenarios. Have students record predictions. Key moment: the dramatic difference between soil and pavement results.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "Now you know WHY cities flood! When we pave over natural ground, we turn rain into a problem.", "do": "Discuss: What percentage of our school grounds is paved? What does that mean for water?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Schoolyard Watershed Map", "say": "Let us put this to the test — we are going outside to map our school and predict where water goes!", "do": "Distribute clipboards and mapping supplies. Go outside to map surface types and predict water flow.", "time": "12 min"}
    ],
    "sort_reasoning": "Ground Type and Rainfall Amount are external because they are conditions that exist in the environment — we can observe and set them, but they are not caused by other parts of the model. Water Absorbed and Runoff are internal because they are OUTCOMES determined by the interaction of ground type and rainfall.",
    "relationships": [
        ("Ground Type to Water Absorbed", "VARIES BY TYPE", "Soil (permeable) absorbs a large percentage of rainfall. Gravel absorbs a moderate amount. Pavement (impermeable) absorbs almost nothing. The type of ground acts like a switch that determines how much water soaks in."),
        ("Ground Type to Runoff", "VARIES BY TYPE (opposite of absorption)", "Soil produces little runoff. Pavement produces heavy runoff. Whatever water does NOT absorb becomes runoff — so these two outputs are inversely related."),
        ("Rainfall Amount to Water Absorbed", "POSITIVE (+)", "More rain means more water available to soak in — up to a limit. Eventually the ground becomes saturated and cannot absorb any more."),
        ("Rainfall Amount to Runoff", "POSITIVE (+)", "More rain means more runoff, especially on impermeable surfaces. Even on soil, very heavy rain overwhelms the absorption rate and creates runoff.")
    ],
    "sim_answers": [
        ("Rain on Soil Scenario", "When Ground Type is soil and Rainfall is heavy, most water is absorbed with moderate runoff. Soil acts like a sponge — it soaks up a large percentage of the rain. Some runoff occurs because very heavy rain can overwhelm absorption, but most water goes into the ground."),
        ("Rain on Pavement Scenario", "When Ground Type is pavement and Rainfall is heavy, almost NO water is absorbed and runoff is extremely high. Pavement is impermeable — water cannot pass through it. Nearly 100% of rain becomes runoff, flowing across the surface toward the lowest point."),
        ("Light vs. Heavy Rain Scenario", "On soil, light rain is almost entirely absorbed with minimal runoff. As rainfall increases, absorption increases too but eventually plateaus as the soil fills up. Once soil is saturated, additional rain becomes runoff. This is why even natural areas can flood during extreme storms.")
    ],
    "reflection_exemplars": [
        ("Why does a parking lot flood more than a field?", "A parking lot is made of pavement, which is impermeable — water cannot soak through it. So nearly all the rain becomes runoff that pools in low spots. A grass field has permeable soil that absorbs water like a sponge, so much less runoff is produced. Even during heavy rain, the field handles water better because it has somewhere for the water to GO — into the ground."),
        ("How do cities make flooding worse?", "Cities replace natural permeable surfaces (soil, grass, trees) with impermeable surfaces (roads, buildings, parking lots). Every time we pave over ground, we take away a sponge and replace it with a slide. The rain has nowhere to soak in, so it all runs off the surface, overwhelming drains and causing floods. The more we pave, the worse it gets.")
    ],
    "stem_intro": "Present the challenge: The school principal wants to reduce flooding on the playground. Your team will map every surface type on the school grounds, calculate the permeable vs. impermeable ratio, and use your model to predict problem areas and recommend solutions.",
    "stem_concepts": [
        ("Permeable = Sponge", "Surfaces like soil and grass let water soak in. More permeable area = less flooding."),
        ("Impermeable = Slide", "Surfaces like pavement and concrete block water. More impermeable area = more runoff and flooding."),
        ("Solutions Exist", "Rain gardens, permeable pavement, and planting trees can add absorption back to paved areas.")
    ],
    "stem_eval": [
        ("Expert (4)", "Map accurately identifies all surface types, calculates ratios, predicts flood zones correctly, and proposes evidence-based solutions"),
        ("Proficient (3)", "Map identifies major surface types and student can explain the connection between pavement and flooding"),
        ("Developing (2)", "Map is completed but predictions are not clearly connected to model data"),
        ("Beginning (1)", "Map is incomplete or student cannot explain how surface type affects flooding")
    ],
    "support": [
        "Provide a simplified school map outline for students to fill in",
        "Color-coding system: green = permeable, red = impermeable, blue = water flow arrows",
        "Sentence frames: 'This area will likely flood because __ and our model showed that __'"
    ],
    "extensions": [
        "Calculate the total impermeable area of your school grounds in square meters",
        "Research 'rain gardens' and design one for a problem area on your school grounds",
        "Compare satellite photos of your neighborhood from 20 years ago to today — how has pavement changed?"
    ],
    "cross_curr": [
        ("Math", "Calculate the percentage of your school grounds that is permeable vs. impermeable. If the school adds a rain garden, how does the percentage change?"),
        ("ELA", "Write a proposal letter to the school principal recommending a specific change to reduce playground flooding, using your map and model data as evidence."),
        ("Social Studies", "Research how your city or town manages stormwater. What infrastructure exists? Is it enough?")
    ],
    "misconceptions": [
        ("Water just disappears into the ground", "Water does not disappear — it moves through soil into underground aquifers (groundwater) or is absorbed by plant roots. The ground acts as a filter and a storage system. This groundwater slowly feeds streams, wells, and springs. When we pave over ground, we cut off this entire underground water system.", "Pour water into a clear container with layers of gravel and sand — watch it filter through. Ask: Where did the water go? It is still there — just underground!"),
        ("All dirt absorbs the same amount of water", "Different soil types absorb very different amounts. Sandy soil is very permeable and absorbs quickly. Clay soil is much less permeable and can cause runoff even in natural areas. Healthy soil with lots of organic matter and earthworm tunnels absorbs the most.", "Test three soil types in clear cups: sand, clay, and garden soil. Pour the same amount of water in each and time how fast it drains."),
        ("Flooding is only caused by too much rain", "While heavy rain is one factor, flooding is heavily influenced by what the ground is made of. A moderate rain can cause flooding on pavement while the same rain on soil causes no flooding at all. Land use is often MORE important than rainfall amount in determining flood risk.", "Show two identical funnels — one with a sponge at the bottom, one with plastic wrap. Pour the same water into both. One overflows, one does not. Same rain, different result!")
    ],
    "game": {
        "title": "Absorption Race",
        "type": "Hands-On Experiment",
        "description": "Three clear containers: one with soil, one with gravel, one with a sealed bottom (pavement). Students pour equal amounts of water into each and time how long until water appears at the bottom drain. Predict first, measure second. Simple, visual, powerful.",
        "materials": ["Three large clear containers with drain holes", "Soil", "Gravel", "Plastic wrap or tray (to simulate pavement)", "Measuring cups", "Stopwatch", "Data recording sheets"],
        "learning_connection": "Directly demonstrates the model's core concept — different ground types absorb different amounts of water, and what doesn't absorb becomes runoff."
    },
    "steam_activity": {
        "title": "Schoolyard Watershed Map",
        "type": "Field Investigation + Cartography",
        "description": "Students walk the school grounds with clipboards and map every surface type (grass, concrete, asphalt, mulch, bare soil). They calculate the percentage of permeable vs. impermeable surface. Then they use their model to predict where water collects during rain. Go outside during the next rain to check predictions.",
        "materials": ["Clipboards", "School grounds map outline (pre-printed)", "Colored pencils (green for permeable, red for impermeable)", "Measuring wheels or long tape measures", "Calculators", "Camera or tablet for documentation"],
        "learning_connection": "Applies the model to a real, local environment students interact with daily — making the science personal and actionable."
    }
}

L1_04 = {
    "id": "NE-L1-04",
    "title": "Telephone Game — How Signals Travel",
    "subtitle": "Why Messages Get Lost Along the Way",
    "ngss": "MS-LS1-8, MS-PS4-2",
    "ngss_desc": "Gather and synthesize information that sensory receptors respond to stimuli by sending messages to the brain for immediate behavior or storage as memories. Develop and use a model to describe that waves are reflected, absorbed, or transmitted through various materials.",
    "big_question": "Why is it so hard for your brain to control a machine on the other side of the room?",
    "objectives": [
        "Explain how signals travel from sensors to processors in both living and designed systems",
        "Model how signal strength, distance, and noise affect message accuracy",
        "Predict when signals will be strong enough to deliver an accurate message",
        "Connect signal degradation to real challenges in brain-computer interface technology"
    ],
    "vocabulary": [
        ("Signal", "A message sent from one place to another — like a nerve impulse or an electronic pulse"),
        ("Noise", "Anything that interferes with a signal and makes it harder to understand"),
        ("Accuracy", "How close the received message is to the original message that was sent"),
        ("Degradation", "When a signal gets weaker or more distorted as it travels")
    ],
    "components": [
        ("Signal Strength", "How strong the original message is when it is first sent — like speaking loudly vs. whispering", True),
        ("Distance Traveled", "How far the signal has to go from sender to receiver", True),
        ("Noise Level", "How much interference is in the environment — other signals, static, distractions", True),
        ("Message Accuracy", "How much of the original message arrives correctly at the destination", False)
    ],
    "think_about_it": "When signal strength increases, does message accuracy go up or down? What about when distance increases? What about noise?",
    "scenarios": [
        ("Strong and Close", "Set Signal Strength to high, Distance to short, Noise to low — what happens to accuracy?"),
        ("Weak and Far", "Set Signal Strength to low, Distance to far, Noise to high — what happens?"),
        ("Noisy Room", "Keep Signal Strength high and Distance short, but increase Noise to maximum — does accuracy survive?")
    ],
    "sim_scenarios": [
        ("Strong and Close", "High signal, short distance, low noise", "What do you predict — will the message arrive accurately?"),
        ("Weak and Far", "Low signal, far distance, high noise", "What do you predict will happen to the message?"),
        ("Noisy Room", "High signal, short distance, high noise", "Can a strong signal overcome lots of noise at short range?")
    ],
    "discoveries": [
        "Three different factors ALL affect whether a message arrives accurately",
        "Signal strength HELPS accuracy, but distance and noise HURT it",
        "Even a strong signal can be ruined by too much noise",
        "This is exactly the challenge scientists face when trying to read brain signals for brain-computer interfaces"
    ],
    "answer": "Sending signals from your brain to a machine is hard because of THREE challenges: the signals are tiny (low strength), they have to travel through tissue and wires (distance), and there are billions of other brain signals creating noise. Scientists building brain-computer interfaces must solve all three problems at once — boosting signal strength, minimizing distance, and filtering out noise. Our model shows that failing on ANY one of these can ruin the message!",
    "stem_title": "Build a Signal Circuit",
    "stem_mission": "Using simple circuits, build a signal chain where pressing a button at one end lights an LED at the other. Then test what happens when you extend the wire and add noise.",
    "stem_scenario": "A medical device company wants to build a system that reads a patient's muscle signals and moves a robotic arm. Your team needs to understand the challenges of sending signals over distance with noise. Build a circuit to test these limits!",
    "stem_questions": [
        "Does the LED light up as brightly when the wire is longer?",
        "What happens when you add a buzzer (noise) to the same circuit?",
        "How is this similar to the challenge of reading brain signals?"
    ],
    "stem_design_qs": [
        "How will you measure signal accuracy — brightness, speed, or on/off reliability?",
        "What length of wire causes the signal to noticeably weaken?",
        "Can you shield your circuit from noise? How?",
        "How could you boost the signal to overcome distance?"
    ],
    "career": "Biomedical Engineers design medical devices including brain-computer interfaces that help paralyzed patients control computers and robotic limbs with their thoughts. They earn $75,000–$130,000/year.",
    "images": {
        "cover": ("cover-brain-signals.png", "A dramatic photorealistic image of glowing neural pathways in a brain, electric blue signals traveling along nerve fibers, dark background with bioluminescent quality, scientific visualization style"),
        "landscape": ("landscape-signal-travel.png", "A photorealistic image of diverse 7th-8th grade students (12-14 years old) playing a relay communication game in a gym, passing messages by tapping patterns on shoulders, Black student at the front of the line, genuinely diverse group, modern athletic clothing, natural gymnasium lighting"),
        "modeling": ("modeling-signal-travel.png", "A photorealistic image of diverse 7th-8th grade students working on laptops building a signal model, Latin American student leading the discussion and pointing at the screen, modern science classroom with neuroscience posters"),
        "discussion": ("discussion-signal-travel.png", "A photorealistic image of a White female teacher holding up a diagram of a brain-computer interface on a tablet, diverse 7th-8th grade students looking fascinated, some taking notes, bright modern classroom"),
        "stem": ("stem-signal-travel.png", "A photorealistic image of diverse 7th-8th grade students building simple LED circuits with batteries and long wires at lab tables, Asian/AAPI student testing wire length while Black student records data, collaborative engineering workspace")
    },
    "pre_assessment": [
        "Have you ever played the telephone game? What happens to the message by the end?",
        "Why do you think phone calls sometimes sound crackly or break up?",
        "If you could control a robot with your brain, what would you make it do?",
        "Draw what you think a brain signal looks like as it travels to your hand."
    ],
    "extend_components": [
        ("Shielding", "Protection around the signal path that blocks outside interference"),
        ("Signal Encoding", "How the message is packaged — better encoding resists noise"),
        ("Number of Channels", "How many signal paths are used — more channels means more data")
    ],
    "reflections": [
        "Why does playing telephone with more people make the message less accurate?",
        "Which factor hurt accuracy the most in your model — distance, noise, or low signal?",
        "How do real engineers solve the noise problem in electronic systems?",
        "Why is it harder to read brain signals than to read a simple button press?",
        "How did modeling three inputs affecting one output help you understand this system?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how signal strength, distance, and noise determine message accuracy."),
        ("Disciplinary Core Idea", "LS1.D Information Processing", "Sensory receptors send signals to the brain that are affected by the same degradation factors modeled in this lesson."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify that three separate causes (signal strength, distance, noise) all produce effects on the same output (accuracy), sometimes in competing directions.")
    ],
    "cast_items": [
        "Explain how signal strength, distance, and noise affect message accuracy",
        "Use a model to predict when a signal will be too degraded to be useful",
        "Connect signal challenges to real brain-computer interface technology"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A scientist is trying to read brain signals to control a robotic arm. The signals are very weak. Which change would MOST improve accuracy? A) Move the sensors farther from the brain B) Increase noise in the room C) Place sensors closer to the brain D) Use thinner wires"),
        ("Constructed Response:", "Using your model, explain why brain-computer interfaces are so challenging to build. Describe at least two factors that work against signal accuracy and what engineers might do about each one.")
    ],
    "background_intro": "Every thought, movement, and sensation involves electrical signals traveling through your nervous system. Understanding how these signals work — and what degrades them — is key to building technology that connects brains directly to machines.",
    "background_sections": [
        ("How Neural Signals Work", "Neurons communicate using electrical impulses called action potentials. These signals travel at speeds of 1-120 meters per second along nerve fibers. Each signal is very small — measured in millivolts (thousandths of a volt). When millions of neurons fire together, their combined electrical activity can be detected on the scalp using electrodes."),
        ("The Signal Degradation Problem", "As signals travel through tissue, they weaken and spread. The skull and skin between the brain and external sensors act as barriers that reduce signal strength. Additionally, the brain produces billions of signals simultaneously, creating enormous 'noise' that makes it hard to isolate the specific signal you want to read."),
        ("Brain-Computer Interfaces Today", "Current BCIs range from non-invasive (EEG headsets worn on the scalp) to invasive (electrode arrays implanted directly in the brain). Non-invasive BCIs have low signal strength but are safe. Invasive BCIs have high signal strength but require surgery. Engineers are constantly working to get better signals with less invasive methods."),
        ("Why This Matters", "BCIs have the potential to restore movement to paralyzed patients, allow locked-in patients to communicate, and treat neurological conditions. The fundamental challenge is always the same: getting a clean, accurate signal from the brain to the machine despite distance, noise, and signal weakness.")
    ],
    "lever_L": "Students identify Signal Strength, Distance Traveled, and Noise Level as external components (conditions we can set) and Message Accuracy as the single internal component (the outcome determined by all three inputs).",
    "lever_E": "Students determine that Signal Strength positively affects accuracy, while Distance and Noise both negatively affect it — three forces acting on one output.",
    "lever_V": "Students build a model showing three external arrows pointing into one internal component, with positive and negative relationships.",
    "lever_Ev": "Students run best-case, worst-case, and noise-test scenarios to see how different combinations affect accuracy.",
    "lever_R": "Students add Shielding or Number of Channels to explore how engineers fight back against signal degradation.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Glowing neural pathway imagery", "say": "What if you could control a robot just by THINKING? That is what brain-computer interfaces try to do. But it is incredibly hard. Today we find out why.", "do": "Show a brief video clip of a BCI patient moving a robotic arm with their thoughts (many are available on YouTube). Ask: What made that possible?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "We are going to model the biggest challenges in sending signals from one place to another.", "do": "Have students read objectives. Pre-teach 'signal' and 'noise' with everyday examples (phone static, crowded room).", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why is it hard for a brain to control a distant machine?", "say": "Your brain controls your hand perfectly. But what if your brain had to control a robot across the room? What goes wrong?", "do": "Play a quick telephone game with 8-10 students. The message degrades. Ask: Why?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We are going to model this problem to figure out what we can do about it.", "do": "Briefly review LEVER steps.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards", "say": "What affects whether a message arrives correctly? Three things work against us — and one helps.", "do": "Guide sorting: Three externals (signal strength, distance, noise) and one internal (accuracy). Discuss why this lesson has more externals than internals.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Signal strength HELPS accuracy — that is a positive arrow. But what about distance and noise?", "do": "Help students draw positive arrow from signal strength and negative arrows from distance and noise. Key: three arrows, one output.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Model scenarios", "say": "Best case: strong signal, close, quiet. Worst case: weak signal, far, noisy. Let us see the difference!", "do": "Run three scenarios with predictions. Key moment: the noisy room scenario — can strength overcome noise?", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "Now you understand WHY building a brain-computer interface is one of the hardest engineering challenges on Earth.", "do": "Summarize findings. Connect to real BCI challenges: brain signals are tiny, skull creates distance, other neurons create noise.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Build a Signal Circuit", "say": "Let us experience signal degradation firsthand with a real circuit!", "do": "Distribute circuit materials. Groups build LED circuits and test effect of wire length and buzzer noise.", "time": "12 min"}
    ],
    "sort_reasoning": "Signal Strength, Distance Traveled, and Noise Level are external because they are conditions we can observe, measure, and set — they exist independently of each other. Message Accuracy is internal because it is the RESULT of all three external factors acting together — it is not something we set, it is something that HAPPENS.",
    "relationships": [
        ("Signal Strength to Message Accuracy", "POSITIVE (+)", "A stronger original signal is harder to degrade. Like shouting vs. whispering — a shout can be heard even in a noisy room."),
        ("Distance Traveled to Message Accuracy", "NEGATIVE (-)", "Signals weaken as they travel farther. Like how a flashlight gets dimmer the farther away you hold it. More distance = more degradation."),
        ("Noise Level to Message Accuracy", "NEGATIVE (-)", "Noise drowns out the signal. Like trying to hear someone talk at a loud concert — the message gets buried under interference.")
    ],
    "sim_answers": [
        ("Strong and Close Scenario", "With high Signal Strength, short Distance, and low Noise, Message Accuracy is very high — near perfect. The signal is strong enough to survive the short trip with minimal interference. This is like talking to someone right next to you in a quiet room."),
        ("Weak and Far Scenario", "With low Signal Strength, far Distance, and high Noise, Message Accuracy drops dramatically — possibly to near zero. The weak signal cannot survive the long trip through heavy interference. This is the worst case for BCI: tiny brain signals traveling through skull and tissue in a noisy electrical environment."),
        ("Noisy Room Scenario", "With high Signal Strength, short Distance, but high Noise, Message Accuracy is moderate — better than expected but not great. A strong signal at close range can partially overcome noise, but not completely. This shows that noise is a powerful factor even when other conditions are favorable.")
    ],
    "reflection_exemplars": [
        ("Which factor matters most?", "In my model, noise had the biggest negative impact on accuracy. Even when the signal was strong and close, cranking up noise dropped accuracy significantly. This makes sense for brain signals — the brain produces billions of electrical signals at once, creating enormous noise. Any BCI has to filter through all that noise to find the one signal it wants."),
        ("How do engineers solve this?", "Engineers use several strategies: they move sensors CLOSER to the brain (some implant electrodes directly into brain tissue), they use STRONGER amplifiers to boost the signal, and they use sophisticated computer algorithms to FILTER noise. Each strategy addresses one of the three factors in our model — reducing distance, boosting strength, or cutting noise.")
    ],
    "stem_intro": "Present the challenge: A medical device company needs to understand signal degradation. Your team will build a simple LED circuit and test how wire length and electromagnetic noise affect signal quality — then propose solutions.",
    "stem_concepts": [
        ("Signal Strength Matters", "A brighter LED at the source means a stronger signal. But even strong signals weaken over distance."),
        ("Distance Creates Resistance", "Longer wires have more resistance, which weakens the electrical signal. This is like brain signals weakening as they pass through skull and tissue."),
        ("Noise Is the Enemy", "A buzzer on the same circuit adds electrical noise. Real brain signals face the same problem from millions of neighboring neurons.")
    ],
    "stem_eval": [
        ("Expert (4)", "Circuit demonstrates signal degradation, student measures and records data at multiple distances, proposes evidence-based solutions to noise"),
        ("Proficient (3)", "Circuit works and student can explain the connection between wire length and signal degradation"),
        ("Developing (2)", "Circuit is built but student struggles to connect physical observations to the model"),
        ("Beginning (1)", "Circuit is incomplete or student cannot explain signal degradation")
    ],
    "support": [
        "Provide pre-built circuits that students only need to extend (not build from scratch)",
        "Use a brightness meter app on a phone to quantify LED brightness at different distances",
        "Sentence frames: 'When I made the wire longer, the LED got __ because __'"
    ],
    "extensions": [
        "Research how cochlear implants use signal processing to help deaf patients hear",
        "Test whether wrapping wire in aluminum foil (shielding) reduces the effect of buzzer noise",
        "Design an experiment to find the maximum wire length that still delivers a readable signal"
    ],
    "cross_curr": [
        ("Math", "Graph LED brightness vs. wire length. Is the relationship linear or curved? Calculate the rate of signal loss per meter."),
        ("ELA", "Write a news article about brain-computer interface technology, explaining the signal challenges in language a non-scientist could understand."),
        ("History", "Research the history of the telegraph — the first long-distance signal system. What signal degradation problems did early telegraph operators face?")
    ],
    "misconceptions": [
        ("Brain signals are like Wi-Fi — they broadcast everywhere", "Brain signals are NOT like radio waves. They are tiny electrical impulses that travel along specific nerve fibers, like electricity through a wire. They do not broadcast outward — sensors have to be very close to detect them. This is why BCI sensors need to be on or in the head, not across the room.", "Compare: shine a flashlight (directed signal, like a nerve) vs. turn on a light bulb (broadcast signal, like Wi-Fi). Brain signals are more like the flashlight."),
        ("A stronger signal always fixes accuracy problems", "While stronger signals help, they cannot overcome all challenges. If noise is extremely high, even a very strong signal gets drowned out. And increasing signal strength in the brain is not really an option — you cannot tell your neurons to 'fire harder.' Engineers have to work with the signals the brain naturally produces.", "Demonstrate: play music at maximum volume while also running a vacuum cleaner. Can you hear the lyrics clearly? Stronger signal helps but noise still wins."),
        ("Computers can easily separate signals from noise", "While computers are getting better at filtering noise, it remains one of the hardest problems in engineering. The brain produces trillions of signals per second, and the one you want might be a tiny fraction of that. Modern BCI software uses machine learning to get better at finding the signal, but it is still far from perfect.", "Play an audio clip of several people talking at once. Ask students to write down what one specific person said. Hard, right? Now imagine doing that with millions of voices.")
    ],
    "game": {
        "title": "Neural Relay Race",
        "type": "Kinesthetic Team Game",
        "description": "Students form a line (the 'nerve'). First student sees a simple shape drawn on a card. They tap a pattern on the next student's shoulder to describe it (e.g., 3 taps = triangle). Message passes down the line. Last student draws what they think it is. Then repeat with a longer line (more distance) and with 'noise' (other students clapping nearby). Compare accuracy across conditions.",
        "materials": ["Shape cards (triangle, square, circle, star, etc.)", "Drawing paper and markers", "Noise-making instruments (clapping, tambourines)", "Stopwatch", "Data recording sheets"],
        "learning_connection": "Directly demonstrates all three model variables: signal strength (how firmly you tap), distance (line length), and noise (background clapping). Students feel the degradation happen."
    },
    "steam_activity": {
        "title": "Build a Signal Circuit",
        "type": "Electronics Engineering",
        "description": "Using Makey Makey or simple circuit kits, students create a signal chain: press a sensor at one end, an LED lights up at the other end. Then extend the wire length (increasing distance). Then add a buzzer on the same circuit (noise). Measure LED brightness and response time at each stage. Directly models neural signal challenges.",
        "materials": ["Simple circuit kits or Makey Makey", "LEDs", "Long wire spools (various lengths)", "Buzzers", "Batteries", "Brightness meter app (phone)", "Stopwatch", "Data recording sheets"],
        "learning_connection": "Students physically experience signal degradation — watching the LED dim with distance and flicker with noise — making the abstract model tangible."
    }
}

L1_05 = {
    "id": "NE-L1-05",
    "title": "One Species Changes Everything",
    "subtitle": "How Keystone Species Hold Ecosystems Together",
    "ngss": "MS-LS2-4, HS-LS2-6",
    "ngss_desc": "Construct an argument supported by empirical evidence that changes to physical or biological components of an ecosystem affect populations. Evaluate claims, evidence, and reasoning that the complex interactions in ecosystems maintain relatively consistent numbers and types of organisms in stable conditions, but changing conditions may result in a new ecosystem.",
    "big_question": "Can removing just ONE species really destroy an entire ecosystem?",
    "objectives": [
        "Explain what a keystone species is and why some species matter more than others",
        "Model how keystone species population affects habitat quality, food availability, and biodiversity",
        "Identify feedback loops where outputs feed back into the system",
        "Predict what happens to an ecosystem when its keystone species is removed"
    ],
    "vocabulary": [
        ("Keystone Species", "A species that has an outsized impact on its ecosystem — remove it and everything changes"),
        ("Biodiversity", "The variety of different species living in an ecosystem"),
        ("Feedback Loop", "When the output of a system circles back and affects its own input — creating a cycle"),
        ("Cascade Effect", "When one change triggers a chain of changes throughout a system")
    ],
    "components": [
        ("Keystone Species Population", "How many of the key species (like beavers) are present in the ecosystem", True),
        ("Habitat Quality", "Overall health of the ecosystem — water, soil, shelter, nesting sites", False),
        ("Food Availability", "How much food the ecosystem produces for all species", False),
        ("Number of Other Species", "How many different species can survive in the ecosystem", False)
    ],
    "think_about_it": "When keystone species population increases, what happens to habitat quality? And when habitat quality increases, what happens to the number of other species? Does anything loop back?",
    "scenarios": [
        ("Thriving Colony", "Set Keystone Species Population to high and observe the cascade through habitat, food, and species"),
        ("Species Removed", "Set Keystone Species Population to zero and observe what happens to everything else"),
        ("Recovery", "Start at zero, then slowly increase Keystone Species Population — how fast does the ecosystem recover?")
    ],
    "sim_scenarios": [
        ("Thriving Colony", "High keystone population", "What do you predict will happen to biodiversity when the keystone species is thriving?"),
        ("Species Removed", "Zero keystone population", "If we remove the keystone species entirely, what do you predict happens to all three internal components?"),
        ("Recovery", "Gradually increasing from zero", "When we bring the keystone species back, will the ecosystem recover immediately or slowly?")
    ],
    "discoveries": [
        "One species can support an entire ecosystem — losing it causes a cascade of decline",
        "Habitat quality, food availability, and biodiversity are all connected in a chain",
        "There is a FEEDBACK LOOP: more species improve habitat quality, which supports even more species",
        "Recovery takes time — ecosystems do not bounce back instantly when the keystone returns"
    ],
    "answer": "YES — removing just one keystone species can transform an entire ecosystem! When beavers are removed, their dams decay, ponds drain, wetlands dry up, and hundreds of species lose their habitat. But here is the hopeful part: when keystone species are brought back, they restart the chain. The key is the FEEDBACK LOOP — once the ecosystem starts recovering, it builds on itself, getting healthier and healthier over time.",
    "stem_title": "Jenga Ecosystem",
    "stem_mission": "Play a modified Jenga game where each block represents a species. Discover which removals cause the tower to collapse and which ones the ecosystem can survive.",
    "stem_scenario": "A conservation agency needs to understand which species are most critical to protect. Your team will simulate species removal using a Jenga tower and identify which species, if removed, cause the ecosystem to crash.",
    "stem_questions": [
        "Which block (species) caused the tower to fall? Why was that one so important?",
        "Could the tower survive losing some species but not others?",
        "How is this game similar to what happens in a real ecosystem?"
    ],
    "stem_design_qs": [
        "Which blocks will you label as 'keystone' species?",
        "How will you record which species were removed before the crash?",
        "Can you predict which removal will cause the collapse before pulling?",
        "What pattern do you notice about which species are safe to remove vs. dangerous?"
    ],
    "career": "Conservation Biologists protect endangered species and restore damaged ecosystems. They identify keystone species and design recovery plans for habitats around the world. They earn $55,000–$95,000/year.",
    "images": {
        "cover": ("cover-keystone-species.png", "A dramatic photorealistic landscape showing the same river valley in two halves — left side lush with beaver ponds, green vegetation, and diverse wildlife; right side dry, barren, and lifeless without beavers — powerful visual comparison, nature documentary photography"),
        "landscape": ("landscape-keystone.png", "A photorealistic image of diverse 9th-10th grade students (14-16 years old) engaged in an animated discussion around a table with ecosystem diagrams and species cards, Black female student making a point while others listen, genuinely diverse group, modern classroom"),
        "modeling": ("modeling-keystone.png", "A photorealistic image of diverse 9th-10th grade students working on laptops building an ecosystem model, Latin American male student pointing at his screen showing a feedback loop diagram, modern science classroom with ecology posters"),
        "discussion": ("discussion-keystone.png", "A photorealistic image of a Black male teacher at a smartboard showing before/after satellite images of a landscape with and without beaver activity, diverse students looking intrigued and taking notes, bright modern classroom"),
        "stem": ("stem-keystone.png", "A photorealistic image of diverse 9th-10th grade students playing a modified Jenga game with species labels on blocks, Asian/AAPI female student carefully removing a block while others watch tensely, fun engaged learning atmosphere")
    },
    "pre_assessment": [
        "What do you think would happen if ALL the bees disappeared from an area?",
        "Are all species equally important to an ecosystem, or are some more important than others?",
        "What does the word 'keystone' mean in architecture? How might that apply to ecology?",
        "Draw what you think a healthy ecosystem looks like vs. a damaged one."
    ],
    "extend_components": [
        ("Invasive Species Pressure", "Non-native species that compete with natives for resources"),
        ("Human Development", "Construction, roads, and agriculture that reduce habitat"),
        ("Water Quality", "Health of the water system — affected by beaver activity and vegetation")
    ],
    "reflections": [
        "Why are some species called 'keystone' species? What does the architectural metaphor mean?",
        "Explain the feedback loop in your model — how does biodiversity feed back into habitat quality?",
        "Why does ecosystem recovery take time even after the keystone species returns?",
        "Name a keystone species besides beavers and explain why it is critical to its ecosystem.",
        "How could this model help conservation agencies decide which species to prioritize for protection?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model showing how a keystone species creates a cascade effect through habitat quality, food availability, and biodiversity."),
        ("Disciplinary Core Idea", "LS2.A Interdependent Relationships in Ecosystems", "Organisms are connected through their relationships — removing a keystone species disrupts the entire web of interdependence."),
        ("Crosscutting Concept", "Stability and Change", "The ecosystem is stable when the feedback loop is active, but removing the keystone species destabilizes the entire system — demonstrating how small changes can have large effects.")
    ],
    "cast_items": [
        "Explain how a keystone species supports an entire ecosystem",
        "Use a model to show the cascade effect of species removal",
        "Identify and explain a feedback loop in an ecosystem model"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Beavers are removed from a watershed. Over the next 5 years, which change would you MOST expect to see? A) More fish in the streams B) Fewer bird species in the area C) Larger trees growing D) Cooler summer temperatures"),
        ("Constructed Response:", "Using your model, explain what happens to an ecosystem when its keystone species is removed. Include the concepts of cascade effect and feedback loop in your answer.")
    ],
    "background_intro": "The concept of the keystone species is one of the most important ideas in ecology. Just as a keystone holds an arch together, certain species hold entire ecosystems together — and removing them causes everything to collapse.",
    "background_sections": [
        ("What Makes a Species 'Keystone'?", "A keystone species has a disproportionately large effect on its ecosystem relative to its population size. Remove it, and the ecosystem changes dramatically. Not all species are keystone — some can be removed with minimal impact. The term was coined by ecologist Robert Paine in 1969 after studying starfish in tide pools."),
        ("Beavers: The Ultimate Ecosystem Engineers", "Beavers are perhaps the most powerful keystone species in North America. Their dams create ponds and wetlands that support fish, amphibians, birds, insects, and plants. A single beaver family can increase local biodiversity by 30-50%. When beavers are removed, dams decay, ponds drain, and this entire web of life collapses."),
        ("Feedback Loops in Ecosystems", "Ecosystems contain feedback loops — chains of cause and effect that circle back on themselves. A positive feedback loop amplifies change: more beavers → better habitat → more food → more species → even better habitat. But feedback loops work in both directions: fewer beavers → worse habitat → less food → fewer species → even worse habitat. This is why ecosystem decline can accelerate."),
        ("Trophic Cascades", "When a keystone species is removed, the effects cascade through the entire food web. The classic example is wolves in Yellowstone: removing wolves → elk overpopulation → overgrazing → river erosion → loss of songbird habitat. Reintroducing wolves reversed the entire cascade. This is called a trophic cascade.")
    ],
    "lever_L": "Students identify Keystone Species Population as the single external component and Habitat Quality, Food Availability, and Number of Other Species as internal components that form a cascade with a feedback loop.",
    "lever_E": "Students determine that Keystone Species positively affects Habitat Quality, which positively affects Food Availability, which positively affects Number of Other Species. The feedback loop: Number of Other Species positively affects Habitat Quality.",
    "lever_V": "Students build a model showing a linear cascade from the external input through three internal components, PLUS a feedback arrow from the last internal back to the second.",
    "lever_Ev": "Students run thriving, removal, and recovery scenarios to observe the cascade and feedback loop in action.",
    "lever_R": "Students add Invasive Species or Human Development to see how additional pressures interact with the keystone dynamic.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Split landscape comparison", "say": "Can one species really matter that much? What if I told you that removing ONE animal could turn a lush valley into a desert?", "do": "Show before/after photos of landscapes with and without beaver activity. The contrast is dramatic.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we are modeling something called a keystone species — and discovering feedback loops.", "do": "Pre-teach 'keystone' using the architecture analogy (show a real stone arch, identify the keystone). If the keystone is removed, the arch collapses.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Can removing one species destroy an ecosystem?", "say": "Think about your favorite place in nature. What would happen if one species disappeared?", "do": "Quick brainstorm: students list species they think might be keystone in their local ecosystem.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps", "say": "We are going to build a model with a new feature today — a feedback loop.", "do": "Preview LEVER steps. Flag that this lesson introduces loops, which are a new modeling concept.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards", "say": "One external component drives THREE internal ones. Which is the input and which are the results?", "do": "Guide sorting. Key discussion: why is Keystone Species the only external? Because it is the trigger for everything else.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows with feedback loop", "say": "Here is the cascade: keystone → habitat → food → species. But here is the COOL part — species feeds BACK into habitat!", "do": "Draw the cascade arrows, then add the feedback loop arrow. Discuss: What does this loop mean? It means the system builds on itself!", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Model scenarios", "say": "Let us see the cascade in action. First with a thriving colony, then we pull the keystone out entirely.", "do": "Run all three scenarios. Key moment: the removal scenario — watch everything collapse in sequence.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings including feedback loop", "say": "The feedback loop is what makes this so powerful — AND so dangerous. It amplifies change in BOTH directions.", "do": "Discuss the Yellowstone wolf reintroduction as a real-world parallel.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Jenga Ecosystem game", "say": "Time to experience the cascade physically — with Jenga!", "do": "Distribute labeled Jenga sets. Groups play and record which removals cause collapse.", "time": "12 min"}
    ],
    "sort_reasoning": "Keystone Species Population is external because it is the initial condition we set — how many keystone organisms are present. Habitat Quality, Food Availability, and Number of Other Species are all internal because they CHANGE as a result of the keystone species' presence or absence. They are not inputs we control — they are outcomes the system produces.",
    "relationships": [
        ("Keystone Species Population to Habitat Quality", "POSITIVE (+)", "More keystone organisms (like beavers) create and maintain habitat — dams create ponds, dig channels, flood areas that become wetlands. Their physical activity directly improves habitat quality."),
        ("Habitat Quality to Food Availability", "POSITIVE (+)", "Better habitat supports more plant growth, more insects, more small animals — all of which are food for other species. A healthy wetland produces far more food than a dry streambed."),
        ("Food Availability to Number of Other Species", "POSITIVE (+)", "More available food supports more species. When food is abundant, specialists and generalists alike can find niches. When food is scarce, only the toughest generalists survive."),
        ("Number of Other Species to Habitat Quality", "POSITIVE (+) — FEEDBACK LOOP", "More species improve habitat quality — plants stabilize soil, predators control herbivore overgrazing, decomposers recycle nutrients. Biodiversity itself is a habitat-building force. This creates a REINFORCING LOOP.")
    ],
    "sim_answers": [
        ("Thriving Colony Scenario", "With high Keystone Species Population, Habitat Quality rises quickly, which drives Food Availability up, which drives Number of Other Species up. The feedback loop then kicks in: more species improve habitat further, creating a virtuous cycle. The ecosystem is robust and self-reinforcing."),
        ("Species Removed Scenario", "With zero Keystone Species, Habitat Quality declines as dams decay and ponds drain. Food Availability drops as plants die. Number of Other Species crashes as animals lose food and shelter. The feedback loop now works in REVERSE: fewer species → worse habitat → even fewer species. A death spiral."),
        ("Recovery Scenario", "When Keystone Species is slowly reintroduced, recovery is NOT instant. It takes time for dams to be rebuilt, ponds to fill, vegetation to regrow, and other species to return. The feedback loop eventually kicks in positively, but there is a lag — the ecosystem has to reach a critical point before the virtuous cycle restarts.")
    ],
    "reflection_exemplars": [
        ("Why is the feedback loop important?", "The feedback loop is what makes keystone species so powerful. Without the loop, removing beavers would only affect things directly connected to them. But because Number of Other Species feeds BACK into Habitat Quality, the decline ACCELERATES. Each loss makes the next loss worse. The same is true in reverse during recovery — once the ecosystem gets going, it builds on itself and recovery accelerates. The loop is what creates both the crash and the comeback."),
        ("Why does recovery take time?", "Recovery takes time because ecosystems are not like light switches. Beavers have to build new dams (weeks to months). Ponds have to fill (months). Vegetation has to grow back (a growing season). Other animals have to discover and colonize the new habitat (months to years). The feedback loop helps, but it takes time to get the first cycle going. This is why conservation is about PREVENTION — it is much easier to keep an ecosystem healthy than to rebuild one from scratch.")
    ],
    "stem_intro": "Present the challenge: Play a modified Jenga game where each block is labeled with a species name. One block is marked KEYSTONE. Players remove species one at a time. When the keystone is removed, three additional blocks must also be removed immediately (the cascade). Which removals collapse the tower?",
    "stem_concepts": [
        ("Keystone Removal = Cascade", "When the keystone block is pulled, it does not just remove one piece — it forces three more removals, simulating the cascade effect."),
        ("Not All Species Are Equal", "Some blocks can be removed with no effect. Others cause wobbling. Only the keystone causes a cascade."),
        ("Position Matters", "Like in real ecosystems, WHERE a species sits in the web (or tower) determines its impact when removed.")
    ],
    "stem_eval": [
        ("Expert (4)", "Student accurately identifies the keystone block before pulling, predicts cascade effects, and connects the game to real ecosystem dynamics using model evidence"),
        ("Proficient (3)", "Student plays the game successfully and can explain why the keystone removal was more destructive than other removals"),
        ("Developing (2)", "Student participates but struggles to connect the game mechanics to real ecosystem concepts"),
        ("Beginning (1)", "Student plays the game but cannot identify which removal represented the keystone or explain the cascade")
    ],
    "support": [
        "Pre-label blocks with species names and color-code by role (green = producer, red = consumer, gold = keystone)",
        "Provide a reference card listing which species depend on which — so students can predict cascade effects",
        "Sentence frames: 'Removing __ caused the tower to __ because __'"
    ],
    "extensions": [
        "Research the Yellowstone wolf reintroduction and map the trophic cascade it caused",
        "Identify three keystone species in your local ecosystem and explain what would happen if each were removed",
        "Design a conservation plan for a keystone species that includes budget, timeline, and success metrics"
    ],
    "cross_curr": [
        ("Math", "Graph the number of species over time in both the removal and recovery scenarios. Calculate the rate of decline vs. rate of recovery."),
        ("ELA", "Write a persuasive essay arguing that protecting ONE keystone species is more cost-effective than trying to protect every species individually."),
        ("Social Studies", "Research the Endangered Species Act. How does the law prioritize which species to protect? Should keystone species get special priority?")
    ],
    "misconceptions": [
        ("All species are equally important to an ecosystem", "While every species plays a role, some species have dramatically larger impacts than others. Keystone species support the structure of the entire community. Removing a common grass species might have minimal effect, but removing the beavers that created the wetland where that grass grows changes EVERYTHING.", "Use the Jenga game: remove a middle block (minor species) — usually fine. Remove the keystone block — cascade collapse. Not all pieces are equal."),
        ("Ecosystems recover instantly when you fix the problem", "Ecosystem recovery takes years to decades, not days. Even after beavers are reintroduced, it takes time for dams to be built, ponds to form, vegetation to grow, and other species to return. The feedback loop helps, but the first cycle is the hardest to start. This is why prevention is always better than restoration.", "Analogy: If you knock over a line of dominoes, you cannot just stand the first one back up and expect the rest to jump back into place. You have to rebuild the whole line, one at a time."),
        ("Top predators are always the keystone species", "Keystone species can be predators (wolves), herbivores (elephants), or even small organisms (sea stars, beavers). What makes them keystone is not their size or position in the food chain — it is the MAGNITUDE of their effect on the ecosystem. Beavers are herbivores, but they reshape entire landscapes.", "List keystone species across different ecosystems: wolves (Yellowstone), beavers (wetlands), sea otters (kelp forests), elephants (savannas), coral (reefs). Note: they span all trophic levels.")
    ],
    "game": {
        "title": "Jenga Ecosystem",
        "type": "Modified Board Game",
        "description": "Label Jenga blocks as different species (beaver, frog, dragonfly, willow tree, trout, etc.). One block is marked KEYSTONE. Students take turns removing species. The game plays normally until someone removes the keystone block — then they must also remove 3 additional blocks immediately (cascade collapse). Visceral demonstration of keystone species importance.",
        "materials": ["Jenga set", "Species label stickers (pre-printed)", "Gold star sticker for KEYSTONE block", "Ecosystem web reference card", "Data recording sheets"],
        "learning_connection": "Students physically experience the difference between removing a regular species (tower wobbles) and removing the keystone (cascade collapse). Makes the abstract concept visceral."
    },
    "steam_activity": {
        "title": "Restoration Case Study Data Lab",
        "type": "Data Analysis + Visualization",
        "description": "Students receive real datasets from actual beaver reintroduction projects (Methow Valley WA, River Otter UK, Yellowstone). They graph species counts, water quality, and vegetation cover over time before and after reintroduction. Compare real data to model predictions.",
        "materials": ["Printed datasets from real reintroduction projects", "Graph paper or graphing software", "Colored pencils", "Calculators", "Comparison worksheet"],
        "learning_connection": "Students see that their simple 4-component model actually predicts real-world outcomes — the cascade and feedback loop appear in actual data from real restoration projects."
    }
}

L1_06 = {
    "id": "NE-L1-06",
    "title": "Should We or Shouldn't We?",
    "subtitle": "When Science Meets Hard Choices",
    "ngss": "HS-ETS1-1, HS-ETS1-3",
    "ngss_desc": "Analyze a major global challenge to specify qualitative and quantitative criteria and constraints for solutions that account for societal needs and wants. Evaluate a solution to a complex real-world problem based on prioritized criteria and trade-offs that account for a range of constraints.",
    "big_question": "How do we decide whether to use technology to fix an environmental problem — even if the fix might cause new problems?",
    "objectives": [
        "Explain how ethical decisions involve weighing competing factors",
        "Model how problem severity, solution risk, and available evidence affect whether intervention is justified",
        "Predict how changing one factor shifts the ethical balance",
        "Apply the model to real-world conservation dilemmas"
    ],
    "vocabulary": [
        ("Intervention", "Taking action to change a situation — especially using technology to fix an environmental problem"),
        ("Risk Assessment", "Carefully evaluating what could go wrong before taking action"),
        ("Evidence-Based Decision", "Making choices based on research and data, not just opinions or feelings"),
        ("Unintended Consequences", "Unexpected negative outcomes that result from an action meant to help")
    ],
    "components": [
        ("Problem Severity", "How serious the environmental crisis is — minor concern to emergency", True),
        ("Solution Risk", "How much could go wrong if we try the proposed fix — low risk to dangerous", True),
        ("Available Evidence", "How much scientific research supports the proposed solution — none to strong", True),
        ("Intervention Justified", "Whether taking action makes sense given all the factors", False)
    ],
    "think_about_it": "If the problem is very serious AND the evidence is strong, but the solution is very risky — should we intervene? What if the problem is minor but the solution is safe?",
    "scenarios": [
        ("Clear Yes", "Set Problem Severity to high, Solution Risk to low, and Available Evidence to strong — should we act?"),
        ("Clear No", "Set Problem Severity to low, Solution Risk to high, and Available Evidence to weak — should we act?"),
        ("Hard Call", "Set Problem Severity to high, Solution Risk to high, and Available Evidence to moderate — what now?")
    ],
    "sim_scenarios": [
        ("Clear Yes", "Severe problem, safe solution, strong evidence", "What does your gut say — should we intervene? Does the model agree?"),
        ("Clear No", "Minor problem, risky solution, weak evidence", "Is it worth risking a dangerous fix for a minor problem?"),
        ("Hard Call", "Severe problem, risky solution, moderate evidence", "This is where it gets hard. What do you predict the model will say?")
    ],
    "discoveries": [
        "Most ethical decisions are NOT clear-cut — they involve competing factors pulling in different directions",
        "Problem severity, solution risk, and available evidence ALL matter — you cannot ignore any of them",
        "The 'hard calls' happen when factors conflict — severe problem but risky solution",
        "Models cannot tell us what is RIGHT, but they can help us see all the factors clearly"
    ],
    "answer": "There is no simple formula for ethical decisions, but our model reveals the key factors: How BAD is the problem? How RISKY is the fix? How STRONG is the evidence? When all three align (bad problem, safe fix, strong evidence), the choice is easy. When they conflict, we need careful debate, transparent reasoning, and willingness to act on the best available evidence while watching for unintended consequences.",
    "stem_title": "Ethics Courtroom",
    "stem_mission": "In structured debates, argue FOR or AGAINST technological intervention in real conservation scenarios. Use your model data as evidence.",
    "stem_scenario": "A conservation agency must decide whether to use new technology to help a struggling ecosystem. Two expert teams will present their cases — one arguing for intervention, one against. A jury of classmates will decide based on the evidence.",
    "stem_questions": [
        "What is the strongest argument FOR intervention in your case?",
        "What is the strongest argument AGAINST intervention?",
        "What additional evidence would help you make a better decision?"
    ],
    "stem_design_qs": [
        "How will you rate problem severity on a scale of 1-10 with evidence?",
        "What specific risks have been documented for your proposed solution?",
        "What does the peer-reviewed research say about this approach?",
        "How will you address the strongest counterargument?"
    ],
    "career": "Environmental Ethicists and Science Policy Advisors help governments and organizations make difficult decisions about technology, conservation, and environmental intervention. They earn $65,000–$120,000/year.",
    "images": {
        "cover": ("cover-ethics.png", "A dramatic photorealistic image of a crossroads sign in a natural landscape — one direction labeled 'ACT' and the other 'WAIT', with a lush ecosystem on one side and a degraded one on the other, golden hour lighting, cinematic nature photography"),
        "landscape": ("landscape-ethics.png", "A photorealistic image of diverse 10th-12th grade students (15-18 years old) in a structured debate format in a modern classroom, two teams facing each other with notes and laptops, Latin American female student standing and making an argument, genuinely diverse group, professional debate atmosphere"),
        "modeling": ("modeling-ethics.png", "A photorealistic image of diverse 10th-12th grade students working on laptops building an ethical decision model, Black male student and White female student collaborating and discussing, modern classroom with environmental science posters"),
        "discussion": ("discussion-ethics.png", "A photorealistic image of an Asian/AAPI female teacher facilitating a Socratic discussion with diverse 10th-12th grade students seated in a circle, students leaning forward engaged in debate, modern classroom with natural light"),
        "stem": ("stem-ethics.png", "A photorealistic image of diverse 10th-12th grade students role-playing a government hearing, one student at a podium presenting while others sit as panel members with name placards, professional and engaged atmosphere")
    },
    "pre_assessment": [
        "Have you ever had to make a decision where there was no clearly right answer? What did you do?",
        "Should scientists always use new technology to fix environmental problems? Why or why not?",
        "What does 'unintended consequences' mean? Can you think of an example?",
        "Is it ever wrong to help — even if your intentions are good?"
    ],
    "extend_components": [
        ("Cost", "How expensive the intervention is — limited budgets mean not everything can be funded"),
        ("Public Support", "Whether the community supports or opposes the intervention"),
        ("Reversibility", "Whether the intervention can be undone if it goes wrong")
    ],
    "reflections": [
        "Why is it important to consider ALL three factors (severity, risk, evidence) before making a decision?",
        "In the 'Hard Call' scenario, what additional information would change your decision?",
        "Can a model ever tell you what is morally right? What can it tell you?",
        "Think of a real-world example where good intentions led to unintended consequences. What went wrong?",
        "How does the amount of evidence change how much risk you are willing to accept?"
    ],
    "dimensions": [
        ("Science Practice", "Engaging in Argument from Evidence", "Students use model outputs as evidence to argue for or against intervention in conservation scenarios."),
        ("Disciplinary Core Idea", "ETS1.B Developing Possible Solutions", "Students evaluate solutions by weighing criteria (problem severity, evidence strength) against constraints (solution risk, unintended consequences)."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify that three separate causes (problem severity, risk, evidence) combine to produce an effect (whether intervention is justified), and that predicting effects requires considering all inputs.")
    ],
    "cast_items": [
        "Explain how competing factors affect ethical decision-making",
        "Use a model to evaluate whether technological intervention in an ecosystem is justified",
        "Argue for or against a conservation intervention using evidence"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Scientists propose releasing genetically modified mosquitoes to fight malaria. The disease kills 600,000 people/year, but the long-term ecological effects are unknown. Using your model framework, which factor creates the most uncertainty? A) Problem Severity B) Solution Risk C) Available Evidence D) Intervention cost"),
        ("Constructed Response:", "A city proposes using AI-controlled drones to replant a burned forest. Using your model, evaluate this intervention by rating Problem Severity, Solution Risk, and Available Evidence. Then argue whether the city should proceed or wait for more research.")
    ],
    "background_intro": "As technology becomes more powerful, we face increasingly difficult decisions about when and how to use it. Environmental ethics is the branch of philosophy that helps us navigate these choices — especially when the stakes are high and the answers are not clear.",
    "background_sections": [
        ("The Intervention Dilemma", "When an ecosystem is in trouble, humans face a choice: intervene using technology, or let nature take its course. Both options have risks. Intervention might cause unintended consequences. But doing nothing might allow irreversible damage. There is no risk-free option — only different risks."),
        ("The Precautionary Principle", "The precautionary principle states: when an action raises threats to the environment, precautionary measures should be taken even if some cause-and-effect relationships are not fully established scientifically. In other words, if something MIGHT be harmful, err on the side of caution. Critics argue this can prevent beneficial interventions."),
        ("Real-World Dilemmas", "CRISPR gene drives could eliminate malaria-carrying mosquitoes but might cascade through food webs. Coral reef robots can plant coral fragments but may alter natural reef development. AI-managed wildlife reserves can detect poachers but raise surveillance concerns. Each dilemma involves the same three factors: severity, risk, and evidence."),
        ("Why Models Help", "Ethical models do not provide answers — they provide STRUCTURE. They force decision-makers to explicitly rate each factor instead of relying on gut feelings. They reveal where disagreements actually lie (is it about the severity of the problem or the risk of the solution?). And they make the reasoning transparent so others can evaluate and challenge it.")
    ],
    "lever_L": "Students identify Problem Severity, Solution Risk, and Available Evidence as external components (factors we can assess and rate) and Intervention Justified as the single internal component (the decision output).",
    "lever_E": "Students determine that Problem Severity and Available Evidence positively affect justification, while Solution Risk negatively affects it — three competing forces on one output.",
    "lever_V": "Students build a model with three external inputs (two positive, one negative) pointing to one internal output.",
    "lever_Ev": "Students run clear-yes, clear-no, and hard-call scenarios to see how the balance shifts.",
    "lever_R": "Students add Cost, Public Support, or Reversibility to see how additional real-world constraints complicate the decision.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Crossroads in nature", "say": "Imagine you have the technology to save a dying forest — but using it might create a NEW problem. Do you act?", "do": "Present a real dilemma: Yellowstone controlled burns. Show photos of the 1988 fires and the recovery. Was the 'do nothing' approach right?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we build a model for something you would not expect — ethical decision-making.", "do": "Pre-teach 'unintended consequences' with examples: cane toads in Australia, kudzu in the US South.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How do we decide?", "say": "This is not a question with a right answer. It is a question about HOW to think clearly when the stakes are high.", "do": "Quick poll: 'A species is going extinct. A risky new technology might save it. Who says act? Who says wait?' Then ask: What would change your mind?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps", "say": "We are going to model this decision the same way we model physical systems. Three inputs, one output.", "do": "Emphasize: this is the first time we are modeling a DECISION, not a physical process. Same tools, different application.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards", "say": "What factors should we weigh? How bad is the problem? How risky is the fix? How much do we know?", "do": "Guide sorting: Three externals (severity, risk, evidence) and one internal (justified). Discuss: Why are these the right factors?", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Severity and evidence PUSH toward action. Risk PUSHES against action. What happens when they fight?", "do": "Draw arrows. Key insight: two positive and one negative arrow on the same output. This is what makes decisions hard.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Model scenarios", "say": "Easy case, easy case, then the HARD case. Predict before we run each one.", "do": "Run all three scenarios. Spend extra time on the 'Hard Call' — have students debate what they would do.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "Models do not tell us what is right. They tell us what we are WEIGHING. That clarity is the first step to a good decision.", "do": "Discuss: Where do you and your classmates disagree? Is it about the severity, the risk, or the evidence?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Ethics Courtroom", "say": "Time to put your reasoning to the test — in a courtroom debate!", "do": "Assign teams and dilemmas. Give prep time, then run structured debates with jury deliberation.", "time": "12 min"}
    ],
    "sort_reasoning": "Problem Severity, Solution Risk, and Available Evidence are external because they are assessments we make based on available information — they are inputs to the decision, not outputs of it. Intervention Justified is internal because it is the RESULT of weighing those three factors — it is what the model produces, not what we set.",
    "relationships": [
        ("Problem Severity to Intervention Justified", "POSITIVE (+)", "The more severe the problem, the more justified intervention becomes. A species going extinct demands more action than a minor population dip."),
        ("Solution Risk to Intervention Justified", "NEGATIVE (-)", "The riskier the solution, the LESS justified intervention becomes. A solution that might cause more harm than good is harder to justify."),
        ("Available Evidence to Intervention Justified", "POSITIVE (+)", "The more scientific evidence supporting the solution, the more justified intervention becomes. Acting on strong research is more defensible than acting on a hunch.")
    ],
    "sim_answers": [
        ("Clear Yes Scenario", "With high Problem Severity, low Solution Risk, and strong Available Evidence, Intervention Justified scores very high. All three factors align in favor of action. This represents cases like vaccinating against a deadly disease — the problem is severe, the solution is proven safe, and decades of evidence support it."),
        ("Clear No Scenario", "With low Problem Severity, high Solution Risk, and weak Available Evidence, Intervention Justified scores very low. All three factors align against action. This represents cases where someone proposes a risky, unproven fix for a minor issue — there is no good reason to take that risk."),
        ("Hard Call Scenario", "With high Problem Severity, high Solution Risk, and moderate Available Evidence, Intervention Justified is ambiguous — near the middle. This is where ethical debates actually happen. The problem is real and serious, but the fix could backfire. People will disagree based on how they weight each factor. This is the scenario that requires the most discussion.")
    ],
    "reflection_exemplars": [
        ("Why consider all three factors?", "If you only consider problem severity, you would always act — even with dangerous, unproven solutions. If you only consider risk, you would never act — even when ecosystems are collapsing. If you only consider evidence, you would miss the urgency of crises that haven't been fully studied yet. You NEED all three because each one alone gives an incomplete picture. The model forces you to face all three honestly."),
        ("Can a model tell you what is right?", "No — a model cannot tell you what is morally right. Morality involves values, priorities, and beliefs that vary between people and cultures. What a model CAN do is make your reasoning VISIBLE. It shows you exactly what you are weighing and how. When people disagree, the model helps them pinpoint WHERE they disagree — is it about how severe the problem is? How risky the solution is? How strong the evidence is? That clarity is the foundation for productive debate instead of just arguing past each other.")
    ],
    "stem_intro": "Set up structured debates: one team argues FOR technological intervention in a real conservation scenario, the other argues AGAINST. A jury of classmates scores based on evidence quality, reasoning clarity, and use of model data. Rotate scenarios each round.",
    "stem_concepts": [
        ("Structured Reasoning", "Use the model's three factors to organize your argument. Rate each factor with evidence, not just opinions."),
        ("Steelmanning", "Before arguing your side, state the STRONGEST version of the opposing argument. This shows intellectual honesty."),
        ("Evidence Hierarchy", "Not all evidence is equal: peer-reviewed studies > case studies > expert opinions > anecdotes. Know where your evidence sits.")
    ],
    "stem_eval": [
        ("Expert (4)", "Argument uses model data explicitly, addresses all three factors with evidence, acknowledges and responds to counterarguments"),
        ("Proficient (3)", "Argument references model factors and uses at least two pieces of evidence to support the position"),
        ("Developing (2)", "Argument states a position but relies more on opinion than evidence from the model"),
        ("Beginning (1)", "Argument is unclear or does not connect to the model's framework")
    ],
    "support": [
        "Provide case file cards with pre-rated severity, risk, and evidence levels for each dilemma",
        "Argument template: 'The problem severity is __ because __. The solution risk is __ because __. Therefore, intervention is/is not justified because __.'",
        "Sentence frames for responding to opponents: 'While the opposing team raises a valid point about __, the evidence shows __'"
    ],
    "extensions": [
        "Research the history of DDT — initially praised for fighting malaria, later banned for environmental damage. Rate it using the model at different time periods.",
        "Write an op-ed for a local newspaper arguing for or against a specific environmental intervention in your community",
        "Design your own ethical dilemma scenario, complete with severity, risk, and evidence ratings, and present it to the class"
    ],
    "cross_curr": [
        ("Math", "Create a weighted scoring system for the model: if you think evidence matters twice as much as severity, how does the scoring change? What if risk matters most?"),
        ("ELA", "Write a position paper arguing for a specific intervention, using model data, real case studies, and rhetorical techniques."),
        ("Social Studies", "Research the Precautionary Principle in European Union policy vs. US regulatory approaches. How do different nations weigh risk vs. evidence?")
    ],
    "misconceptions": [
        ("Science alone can answer ethical questions", "Science provides DATA — how severe is the problem, what does the evidence show, what are the risks. But the DECISION of what to do involves values, priorities, and moral principles that science alone cannot determine. Two people can agree on all the facts and still disagree on the right action because they weight the factors differently.", "Present a scenario where two students agree on all the model inputs but reach different conclusions. Ask: Who is right? Both are — the disagreement is about VALUES, not facts."),
        ("If the technology exists, we should use it", "Just because we CAN do something does not mean we SHOULD. Nuclear weapons exist but most nations agree not to use them. Gene editing can modify human embryos but most countries have banned it. The existence of a tool says nothing about whether using it is wise. Our model helps evaluate each case individually.", "List technologies that exist but are restricted: biological weapons, human cloning, certain pesticides. Ask: Why are these restricted if they could theoretically be useful?"),
        ("Doing nothing is always the safe option", "Inaction is itself a choice with consequences. If an ecosystem is collapsing and we choose not to intervene, we are choosing to let it collapse. Sometimes the risk of doing nothing exceeds the risk of acting. Our model captures this through the Problem Severity factor — when severity is extreme, the cost of inaction is also extreme.", "Present the trolley problem adapted for ecology: a river ecosystem will die in 5 years without intervention. An experimental treatment has a 20% chance of making it worse. Is doing nothing truly 'safe'?")
    ],
    "game": {
        "title": "Ethics Courtroom",
        "type": "Structured Debate Game",
        "description": "One team argues FOR technological intervention in an ecosystem (e.g., using drones to plant trees, releasing lab-bred species, using robots to monitor wildlife). The other argues AGAINST. A jury of classmates scores based on evidence quality, not just persuasiveness. Scenarios rotate each round.",
        "materials": ["Case file cards (4 real-world dilemmas)", "Scoring rubrics for jury members", "Timer (5 min per side, 2 min rebuttal)", "Argument planning templates", "Model reference sheets"],
        "learning_connection": "Students practice using model outputs as evidence in structured arguments — connecting abstract modeling to real-world decision-making."
    },
    "steam_activity": {
        "title": "Case File Analysis",
        "type": "Research + Decision Matrix",
        "description": "Students receive 4 real-world case files: (1) Wolf reintroduction in Yellowstone, (2) CRISPR gene drives for mosquito control, (3) Coral reef robot planters, (4) AI-monitored wildlife preserves. For each, they rate Problem Severity (1-10), Solution Risk (1-10), and Available Evidence (1-10), compute their model's Intervention Justified score, then compare to what actually happened in the real world.",
        "materials": ["Printed case file packets (4 per group)", "Decision matrix worksheets", "Access to research databases or pre-selected articles", "Calculators", "Presentation materials"],
        "learning_connection": "Students apply their model to real decisions that have already been made — then compare their model's recommendation to what actually happened. Did the real world follow the model's logic?"
    }
}

# =============================================================================
# LEVEL 2 LESSONS (Full Models — 7-9 components each)
# =============================================================================

L2_01 = {
    "id": "NE-L2-01",
    "title": "Ecosystem Engineers",
    "subtitle": "How One Species Creates a World",
    "ngss": "5-LS2-1, 5-ESS2-1, 3-5-ETS1-3",
    "ngss_desc": "Develop a model to describe the movement of matter among plants, animals, decomposers, and the environment. Develop a model using an example to describe ways the geosphere, biosphere, hydrosphere, and atmosphere interact. Plan and carry out fair tests in which variables are controlled and failure points are considered.",
    "big_question": "How does a family of beavers create an entire ecosystem that hundreds of species depend on?",
    "objectives": [
        "Explain how beavers change water flow, create wetlands, and support biodiversity",
        "Model a 7-component system showing cascading relationships from beaver activity to biodiversity",
        "Run scenarios that test what happens when key inputs are changed",
        "Predict the ecosystem-wide consequences of beaver removal"
    ],
    "vocabulary": [
        ("Cascade Effect", "When a change in one part of a system triggers changes in many other parts, like dominoes falling"),
        ("Wetland", "An area of land that is saturated with water, supporting unique plants and animals"),
        ("Biodiversity", "The variety of different species living in an ecosystem — more diversity means a healthier system"),
        ("Ecosystem Engineer", "A species that physically changes its environment, creating or destroying habitat for other species"),
        ("Hydrosphere", "All of Earth's water — rivers, lakes, groundwater, rain, and oceans")
    ],
    "components": [
        ("Beaver Population", "How many beavers live in the area — more beavers means more building activity", True),
        ("Tree Availability", "How many trees are nearby for building dams — the essential construction material", True),
        ("Rainfall", "How much precipitation falls in the watershed area", True),
        ("Dam Size", "How big and sturdy the beaver dam grows — determined by beavers AND trees", False),
        ("Water Level", "How high the water rises behind the dam — creates the pond", False),
        ("Wetland Area", "How much wetland habitat is created as water spreads across the floodplain", False),
        ("Biodiversity", "The number of different species living in and around the beaver-created ecosystem", False)
    ],
    "think_about_it": "Trace the chain: Beavers + Trees → Dam → Water → Wetland → Species. What happens at EACH step when you remove the beavers?",
    "scenarios": [
        ("Thriving Colony", "Beaver Population high, Tree Availability high, Rainfall normal — observe the full cascade"),
        ("Drought Year", "Keep Beaver Population and Trees high, but drop Rainfall to very low — what survives?"),
        ("Beavers Removed", "Set Beaver Population to zero — watch the cascade collapse over time"),
        ("Deforestation", "Beaver Population high but Tree Availability drops to near zero — what happens to the dam?")
    ],
    "sim_scenarios": [
        ("Thriving Colony", "Full resources available", "What do you predict biodiversity will be when beavers have everything they need?"),
        ("Drought Year", "Low rainfall despite beavers", "Can beavers maintain the ecosystem during a drought?"),
        ("Beavers Removed", "Zero beavers", "How long does the cascade take to collapse? What goes first?"),
        ("Deforestation", "No trees available", "If beavers have no building material, can they still engineer the ecosystem?")
    ],
    "discoveries": [
        "Beaver activity creates a CASCADE: dam → water → wetland → biodiversity — each step depends on the one before it",
        "Three external inputs ALL matter — losing any one significantly weakens the system",
        "Beavers can buffer against drought because their dams store water — but they cannot create water from nothing",
        "Removing beavers doesn't just affect the pond — it collapses the ENTIRE chain of dependent species",
        "The beaver-created wetland supports more species than the original stream ever could"
    ],
    "answer": "A beaver family creates an entire ecosystem through a CHAIN of engineering: they use trees to build dams, dams raise water levels, higher water creates wetlands, and wetlands support hundreds of species from fish to birds to insects to plants. This cascade means that ONE species — the beaver — is responsible for a vast web of life. Remove the beavers, and the whole chain unravels, step by step.",
    "stem_title": "Wetland Watercolor Mural",
    "stem_mission": "After running the simulation, create a large collaborative mural showing the ecosystem at three stages: no beavers, small colony, and thriving colony. Every species depicted must match what the model predicted.",
    "stem_scenario": "A nature center wants a mural that teaches visitors how beavers create wetlands. Your team will use model data to ensure every species and habitat feature shown is scientifically accurate at each stage.",
    "stem_questions": [
        "Which species appear FIRST as the wetland develops? Which come last?",
        "How does the landscape look different at each stage?",
        "What evidence from your model supports the species you chose to include?"
    ],
    "stem_design_qs": [
        "How will you divide the mural into three panels (no beavers, small colony, thriving)?",
        "Which species will you include in each panel and why?",
        "How will you show the water level difference between stages?",
        "How will you make the mural both scientifically accurate AND visually compelling?"
    ],
    "career": "Wetland Ecologists study how wetland ecosystems function and design restoration projects. They work with government agencies, conservation organizations, and universities. They earn $55,000–$90,000/year.",
    "images": {
        "cover": ("cover-ecosystem-engineers.png", "An epic photorealistic aerial view of a beaver-engineered landscape — multiple dams creating a chain of ponds surrounded by lush green vegetation, drone photography style, golden hour, nature documentary quality"),
        "landscape": ("landscape-ecosystem-eng.png", "A photorealistic image of diverse 4th-5th grade students (9-11 years old) examining a large classroom terrarium with a miniature wetland setup, genuinely diverse group — Black female student pointing out a frog while Latin American and Asian/AAPI students observe, modern science classroom, natural light"),
        "modeling": ("modeling-ecosystem-eng.png", "A photorealistic image of diverse 4th-5th grade students working on Chromebooks with a 7-component model visible on screen, White male student and Black female student discussing relationships, modern classroom with ecosystem posters"),
        "discussion": ("discussion-ecosystem-eng.png", "A photorealistic image of a Latin American male teacher leading a discussion with diverse 4th-5th graders, drawing a cascade diagram on a whiteboard showing beaver → dam → water → wetland → species, students engaged and asking questions"),
        "stem": ("stem-ecosystem-eng.png", "A photorealistic image of diverse 4th-5th grade students painting a large collaborative mural on butcher paper, showing a wetland ecosystem with beavers, fish, birds, and plants, Asian/AAPI student in the lead painting, art supplies spread across tables")
    },
    "pre_assessment": [
        "In your Level 1 lesson, you modeled beavers, trees, dam size, and pond size. What do you think comes AFTER the pond?",
        "How many different animals do you think could live in a beaver pond? List as many as you can.",
        "What would happen to all those animals if the beavers disappeared?",
        "Draw what you think a beaver-created wetland looks like from above."
    ],
    "extend_components": [
        ("Water Temperature", "The temperature of the pond — affected by depth, shade, and flow rate"),
        ("Sediment Filtering", "How much dirt and pollution the wetland traps — clean water supports more life"),
        ("Predator Population", "Number of predators like otters, eagles, and herons that move into the rich ecosystem")
    ],
    "reflections": [
        "How is the Level 2 model different from the Level 1 model? What does adding more components reveal?",
        "Trace the cascade: if Tree Availability drops by half, what happens at each step all the way to Biodiversity?",
        "Why are beavers sometimes called 'nature's water managers'?",
        "What surprised you most about the simulation results?",
        "How could this model help real conservation planners decide where to reintroduce beavers?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a 7-component computational model showing cascading relationships from beaver activity through dam construction, water management, wetland creation, to biodiversity support."),
        ("Disciplinary Core Idea", "LS2.A Interdependent Relationships in Ecosystems", "Multiple species depend on the habitat created by beavers — demonstrating how organisms in an ecosystem are interconnected through their physical environment."),
        ("Crosscutting Concept", "Systems and System Models", "A system can be described in terms of its components and their interactions — the 7-component model reveals how changing one input cascades through the entire system.")
    ],
    "cast_items": [
        "Describe the cascade from beaver activity through dam, water, wetland, to biodiversity",
        "Use the model to predict what happens when a key input is removed",
        "Explain how one species can support an entire ecosystem"
    ],
    "cast_questions": [
        ("Multiple Choice:", "In a watershed with beavers, a logging company removes most of the nearby trees. According to the cascade model, which component will be affected FIRST? A) Biodiversity B) Dam Size C) Wetland Area D) Water Level"),
        ("Constructed Response:", "Using your 7-component model, explain what happens to the entire ecosystem over time when beavers are removed from a watershed. Describe each step in the cascade from dam decay to biodiversity loss.")
    ],
    "background_intro": "This lesson builds on Level 1 by expanding the simple beaver-dam-pond model into a full ecosystem cascade. Students now see how the basic building process creates a chain of effects that extends far beyond the dam itself.",
    "background_sections": [
        ("From Dam to Ecosystem", "A beaver dam does not just create a pond — it creates an entirely new type of habitat. The dam slows water flow, raises the water table, floods adjacent land, creates deep-water zones, generates edge habitat where water meets land, and increases the overall complexity of the landscape. Each of these changes supports different species."),
        ("The Wetland Effect", "Beaver-created wetlands are among the most biologically productive ecosystems on Earth. They support amphibians that need still water for breeding, fish that need deep pools for refuge, birds that need shoreline for nesting, insects that need standing water for larvae, and plants that need waterlogged soil. A single beaver pond can increase local bird species by 75%."),
        ("Water Management", "Beavers are remarkably effective water managers. Their dams slow flood waters, reducing downstream flooding by 20-60%. They recharge groundwater aquifers by spreading water across floodplains. They filter sediment and pollutants from water as it passes through their ponds. And they store water during wet periods and release it during dry periods, buffering against both floods and droughts."),
        ("The Removal Cascade", "When beavers are removed (by trapping, habitat destruction, or predation), the cascade reverses. Dams decay within 1-3 years without maintenance. Ponds drain, lowering the water table. Wetlands dry out, killing aquatic vegetation. Fish, amphibians, and invertebrates lose habitat. Birds and mammals that depended on the wetland must relocate or die. The rich ecosystem reverts to a simple stream channel.")
    ],
    "lever_L": "Students identify Beaver Population, Tree Availability, and Rainfall as external components. Dam Size, Water Level, Wetland Area, and Biodiversity are internal components forming a cascade chain.",
    "lever_E": "Students trace the cascade: Beaver Population + Tree Availability → Dam Size → Water Level (also boosted by Rainfall) → Wetland Area → Biodiversity. Each link is positive.",
    "lever_V": "Students build the full 7-component model with three external inputs feeding a four-step cascade of internal components.",
    "lever_Ev": "Students run thriving, drought, removal, and deforestation scenarios to test different parts of the cascade.",
    "lever_R": "Students add Water Temperature, Sediment Filtering, or Predator Population to further explore ecosystem complexity.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Aerial view of beaver ecosystem", "say": "Remember our Level 1 model? Beavers, trees, dam, pond. Today we go FURTHER — what happens AFTER the pond forms?", "do": "Show aerial drone footage of beaver wetlands. Ask: How many different species can you spot?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "We are expanding from 4 components to 7. This is a BIG model — but you are ready.", "do": "Preview the new vocabulary: cascade, wetland, hydrosphere. Connect to Level 1 knowledge.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How does one family create an entire ecosystem?", "say": "A beaver family is usually 4-8 animals. How can 8 beavers support HUNDREDS of other species?", "do": "Quick brainstorm: students list species that might live in a beaver wetland. Aim for 20+.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps with cascade emphasis", "say": "Our model today has a CHAIN — each component feeds the next. This is called a cascade.", "do": "Draw the cascade as a staircase: beaver → dam → water → wetland → biodiversity. Each step higher.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "7 component cards", "say": "Three things WE can control, four things the SYSTEM produces. Let us sort them.", "do": "Guide sorting of all 7 components. Emphasize: Level 1 had 4. Level 2 has 7. More components = more realistic.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Cascade diagram with arrows", "say": "Trace the chain. Beavers + Trees feed the Dam. The Dam feeds Water Level. Rainfall ALSO feeds Water Level. Water feeds Wetland. Wetland feeds Biodiversity.", "do": "Build the cascade arrow by arrow. Key moment: Rainfall feeds Water Level directly, not through the dam.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Four scenario tests", "say": "Four tests today. Thriving colony, drought, beavers removed, and deforestation. Predict each one!", "do": "Run scenarios in order. After each, pause to compare predictions to results. Drought is the most surprising.", "time": "12 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key cascade findings", "say": "One family of beavers, hundreds of species supported. That is the power of ecosystem engineering.", "do": "Summarize cascade findings. Compare: What did Level 1 teach us? What did Level 2 ADD?", "time": "4 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Wetland mural project", "say": "Now paint what you modeled — three stages, scientifically accurate, and beautiful!", "do": "Distribute art supplies. Groups plan panels, assign species, and begin painting.", "time": "12 min"}
    ],
    "sort_reasoning": "Beaver Population, Tree Availability, and Rainfall are external because they are environmental conditions that exist independently — we can observe and set them. Dam Size, Water Level, Wetland Area, and Biodiversity are internal because they are PRODUCED by the system — each one depends on the components before it in the cascade chain.",
    "relationships": [
        ("Beaver Population to Dam Size", "POSITIVE (+)", "More beavers means more workers to cut trees, haul branches, and pack mud. Larger families build bigger, more complex dam systems."),
        ("Tree Availability to Dam Size", "POSITIVE (+)", "More trees means more building material. Even large beaver families are limited by material availability."),
        ("Dam Size to Water Level", "POSITIVE (+)", "Bigger dams hold back more water, raising the water level higher behind the dam and flooding a larger area."),
        ("Rainfall to Water Level", "POSITIVE (+)", "More rainfall fills the pond faster and maintains higher water levels. This input feeds Water Level directly, bypassing the dam."),
        ("Water Level to Wetland Area", "POSITIVE (+)", "Higher water levels spread across more land, creating more wetland habitat. Water seeps into surrounding soil, raising the water table."),
        ("Wetland Area to Biodiversity", "POSITIVE (+)", "Larger wetlands support more diverse habitat types (deep water, shallow water, mudflat, shoreline), each attracting different species.")
    ],
    "sim_answers": [
        ("Thriving Colony Scenario", "With all three externals high, the full cascade is active: large dam → high water → extensive wetland → high biodiversity. The system is at maximum productivity. This represents an undisturbed beaver ecosystem at its best."),
        ("Drought Year Scenario", "With low Rainfall but high Beaver Population and Trees, Dam Size stays large but Water Level drops because there is less water coming in. The dam can hold water but there is less TO hold. Wetland Area shrinks. Biodiversity declines but NOT as much as you might expect — the dam BUFFERS the drought by retaining what water exists. Without the dam, biodiversity would crash completely."),
        ("Beavers Removed Scenario", "With zero Beaver Population, Dam Size begins declining immediately as the dam is not maintained and begins decaying. Water Level drops as the dam loses integrity. Wetland Area shrinks as water drains. Biodiversity declines as aquatic and wetland species lose habitat. The full collapse takes 1-3 years."),
        ("Deforestation Scenario", "With high Beaver Population but near-zero Trees, Dam Size cannot grow because there is no building material. Existing dams weaken without fresh wood. Water Level drops. Wetland Area and Biodiversity follow. Beavers may abandon the site to find better habitat — accelerating the collapse.")
    ],
    "reflection_exemplars": [
        ("How is Level 2 different from Level 1?", "Level 1 showed us the basic chain: beavers + trees → dam → pond. Level 2 extends that chain to show what the pond CREATES: wetland habitat that supports an entire community of species. Adding three more components (Water Level, Wetland Area, Biodiversity) reveals the full cascade — one thing leads to the next, which leads to the next. It shows that the impact of beavers extends far beyond just a dam and a pond."),
        ("Why can beavers buffer against drought?", "In the drought scenario, the dam still holds water even though less rain is coming in. It is like a savings account — the dam STORES water from previous rains. Without the dam, all the water would flow downstream immediately and the area would be dry. With the dam, some water is retained, keeping the wetland partially alive. The beavers cannot create water, but they can SAVE it. This is why researchers call beavers 'nature's water infrastructure.'")
    ],
    "stem_intro": "Present the mural challenge: Three panels showing the same river valley at three stages of beaver colonization. Students must use their model data to determine which species appear at each stage and how the landscape changes.",
    "stem_concepts": [
        ("Succession", "Ecosystems develop in stages. First come aquatic plants, then insects, then fish, then amphibians, then birds and mammals. Your mural should show this sequence."),
        ("Habitat Complexity", "More water features (deep pools, shallow edges, islands, channels) = more species. Show this in your mural."),
        ("Landscape Transformation", "The same land looks completely different with and without beavers. Your mural should make this transformation dramatic and clear.")
    ],
    "stem_eval": [
        ("Expert (4)", "Mural accurately depicts three stages with correct species succession, uses model data to justify species placement, and is artistically compelling"),
        ("Proficient (3)", "Mural shows clear differences between stages and includes scientifically reasonable species choices"),
        ("Developing (2)", "Mural shows some progression but species choices are not clearly connected to model data"),
        ("Beginning (1)", "Mural is incomplete or does not show meaningful differences between stages")
    ],
    "support": [
        "Provide species cards with habitat requirements — students match species to the stage where their habitat first appears",
        "Show real before/after photos of beaver restoration sites as reference",
        "Sentence frames for labels: 'At this stage, __ lives here because the model shows __'"
    ],
    "extensions": [
        "Research the 'Beaver Deceivers' — human-made flow devices that let beavers build dams without flooding roads",
        "Calculate the volume of water a beaver dam holds using estimated dam dimensions",
        "Design a school presentation explaining why your town should consider beaver reintroduction"
    ],
    "cross_curr": [
        ("Math", "Estimate the surface area of a beaver wetland from an aerial photo using grid overlay. Calculate how biodiversity scales with wetland area."),
        ("ELA", "Write a narrative from the perspective of a fish living in a beaver pond — describe the habitat and the other species you interact with."),
        ("Art", "The mural IS the art integration — students practice scale, perspective, and color to accurately depict a changing landscape.")
    ],
    "misconceptions": [
        ("Beaver dams are permanent structures", "Beaver dams require constant maintenance. Without beavers actively repairing them, dams begin decaying within months. Water pressure, storms, and ice damage all wear on the dam. This is why beaver REMOVAL leads to dam COLLAPSE — no maintenance means no dam.", "Show time-lapse photos of dam decay after beaver removal. Ask: How long does it take for the ecosystem to change?"),
        ("Any water creates a wetland", "A puddle is not a wetland. Wetlands require sustained water saturation that changes soil chemistry, supports specific plant communities, and provides habitat structure. Beaver dams create the sustained, managed water levels that true wetlands need — a one-time flood does not.", "Compare a photo of a temporary flood puddle to a beaver wetland. Ask: Which one supports more species? Why?"),
        ("More rainfall is always better for wetlands", "While wetlands need water, TOO much rainfall can actually cause problems: flooding the dam, washing away dam material, and creating fast-flowing water that destroys habitat structure. Beaver dams work best with moderate, consistent rainfall. Extreme events can overwhelm the system.", "Discuss: What happens in the drought scenario? The dam BUFFERS it. What would happen in an extreme flood scenario? The dam might breach.")
    ],
    "game": {
        "title": "Wetland Web",
        "type": "Strategy Board Game",
        "description": "Students place beaver tokens, tree tokens, and rain tokens to build a food web on a grid board. Each wetland tile placed lets them add species cards. The player with the most connected food web wins. Introduces cascade thinking in a competitive format.",
        "materials": ["Grid game boards (1 per group)", "Beaver, tree, and rain tokens", "Wetland tiles", "Species cards with food web connections", "Score sheets"],
        "learning_connection": "Reinforces the cascade — students must build from beaver → dam → water → wetland before they can place species, mirroring the model's chain of dependencies."
    },
    "steam_activity": {
        "title": "Wetland Watercolor Mural",
        "type": "Art + Science Integration",
        "description": "After running the simulation, student groups paint a large collaborative mural showing the ecosystem at three stages: no beavers (dry streambed), small colony (small pond), thriving colony (full wetland with diverse species). The art must be scientifically accurate — species depicted must match what their model predicted at each stage.",
        "materials": ["Large butcher paper rolls", "Watercolor paint sets", "Reference photos of beaver wetlands at various stages", "Species reference cards", "Model printouts for reference"],
        "learning_connection": "Translates model data into visual art — students must decide WHICH species appear at WHICH stage based on what the model predicts about habitat quality at each level of beaver activity."
    }
}

L2_02 = {
    "id": "NE-L2-02",
    "title": "Biomimicry Design Lab",
    "subtitle": "Engineering Solutions Inspired by Nature",
    "ngss": "MS-LS4-4, MS-ETS1-1, MS-ETS1-2, MS-ETS1-3, MS-ETS1-4",
    "ngss_desc": "Construct an explanation based on evidence that describes how genetic variations of traits in a population increase some individuals' probability of surviving and reproducing. Define the criteria and constraints of a design problem. Evaluate competing design solutions. Analyze data from tests to determine similarities and differences. Develop a model to generate data for iterative testing.",
    "big_question": "Can engineers build a robot so lifelike that real animals cannot tell it apart from one of their own?",
    "objectives": [
        "Explain how animal adaptations inspire engineering design through biomimicry",
        "Model a 7-component system showing how design choices create tradeoffs in performance",
        "Evaluate competing designs by comparing multiple performance metrics simultaneously",
        "Design and iterate on a biomimicry prototype using model data"
    ],
    "vocabulary": [
        ("Biomimicry", "The practice of designing technology by studying and copying strategies found in nature"),
        ("Fidelity", "How accurately an artificial design replicates the original natural feature"),
        ("Constraint", "A limitation that restricts the design — like weight, cost, or power supply"),
        ("Iteration", "The process of testing, evaluating, and improving a design through repeated cycles"),
        ("Detection Risk", "The likelihood that observers can identify the design as artificial rather than natural")
    ],
    "components": [
        ("Animal Feature Selected", "Which biological feature the design copies — tail shape, fur texture, body movement pattern", True),
        ("Material Choice", "What the design is built from — determines weight, flexibility, appearance, and cost", True),
        ("Power Source", "Type and size of energy supply — battery capacity, solar, etc.", True),
        ("Movement Accuracy", "How closely the design moves like the real animal — gait, speed, fluidity", False),
        ("Energy Use", "How quickly the design drains its power supply during operation", False),
        ("Durability", "How long the design lasts in real-world conditions before needing repair", False),
        ("Detection Risk", "How easily observers can tell the design is artificial rather than a real animal", False)
    ],
    "think_about_it": "If you choose the most lifelike material, what happens to movement accuracy AND energy use? Can you maximize everything, or must you make tradeoffs?",
    "scenarios": [
        ("High Fidelity", "Animal Feature set to beaver tail, Material set to silicone (lifelike), Power Source medium — observe all outputs"),
        ("Budget Build", "Animal Feature set to beaver tail, Material set to hard plastic (cheap), Power Source small — compare to high fidelity"),
        ("Power Boost", "Same as high fidelity but Power Source set to maximum — does more power fix the tradeoffs?"),
        ("Wrong Feature", "Animal Feature set to pointed tail (poor for water), best materials and power — can great materials fix a bad design?")
    ],
    "sim_scenarios": [
        ("High Fidelity", "Lifelike materials, moderate power", "What do you predict — will lifelike materials give the best detection risk score?"),
        ("Budget Build", "Cheap materials, small power", "How much performance do you lose with cheaper materials?"),
        ("Power Boost", "Maximum power source", "Can throwing more power at the problem overcome material limitations?"),
        ("Wrong Feature", "Bad fundamental design", "If the basic shape is wrong, can expensive materials save it?")
    ],
    "discoveries": [
        "The fundamental design choice (which animal feature to copy) matters MORE than materials or power",
        "Lifelike materials reduce detection risk but increase energy use and decrease durability",
        "More power helps but creates its own problems — heavier batteries, more heat, shorter lifespan",
        "No single design maximizes ALL outputs — engineering is about finding the BEST BALANCE of tradeoffs",
        "Nature's designs are efficient because evolution has been optimizing for millions of years"
    ],
    "answer": "Building a lifelike animal robot is one of engineering's hardest challenges because EVERY design choice involves tradeoffs. Copying the right animal feature is the most important decision — no amount of fancy materials can fix a fundamentally wrong shape. After that, engineers must balance movement accuracy against energy use, and durability against detection risk. Nature solved these tradeoffs through millions of years of evolution. Engineers try to match that with smart materials, efficient power, and iterative testing.",
    "stem_title": "Animal Robot Sketchbook",
    "stem_mission": "Choose a real animal, research three of its key adaptations, then design a robot that borrows those features. Create a detailed engineering sketchbook with design rationale based on model data.",
    "stem_scenario": "A wildlife research organization needs robots that can observe animals without disturbing them. Your team will design an animal-mimicking robot, using your model to make and justify every design decision.",
    "stem_questions": [
        "Which animal did you choose and what three adaptations did you borrow?",
        "What tradeoffs does your design make — where did you sacrifice one metric to improve another?",
        "How does your model data support your design choices?"
    ],
    "stem_design_qs": [
        "What are the three most important adaptations of your chosen animal?",
        "What material will you use for each adaptation and why?",
        "How much power does your design need — and how will you provide it?",
        "What is the biggest weakness of your design, and could a future iteration fix it?"
    ],
    "career": "Robotics Engineers specializing in biomimicry design robots inspired by nature for exploration, medical devices, search and rescue, and environmental monitoring. They earn $80,000–$140,000/year.",
    "images": {
        "cover": ("cover-biomimicry-lab.png", "A stunning photorealistic image of a robotic fish swimming alongside real fish in a coral reef, the robot is nearly indistinguishable from the real fish, underwater photography with natural light filtering through water"),
        "landscape": ("landscape-biomimicry-lab.png", "A photorealistic image of diverse 6th-8th grade students (11-14 years old) at a design table covered with animal reference photos, sketching blueprints, Black male student leading the discussion, Latin American and White students contributing ideas, modern STEM lab"),
        "modeling": ("modeling-biomimicry-lab.png", "A photorealistic image of diverse 6th-8th grade students comparing model outputs on laptops, one screen showing a spider chart of tradeoffs, Asian/AAPI female student pointing out a key data point, collaborative learning environment"),
        "discussion": ("discussion-biomimicry-lab.png", "A photorealistic image of a Black female teacher showing real biomimicry examples on a smartboard — robot fish, drone birds, gecko-grip gloves — diverse students fascinated and taking notes"),
        "stem": ("stem-biomimicry-lab.png", "A photorealistic image of diverse 6th-8th grade students creating detailed engineering sketches of animal-inspired robots, colored pencils and rulers on tables, Latin American female student presenting her design to her group, creative engineering atmosphere")
    },
    "pre_assessment": [
        "In Level 1, you discovered that tail shape affects swimming speed. What OTHER animal features might engineers want to copy?",
        "What makes a robot 'lifelike'? List as many factors as you can.",
        "Why would a wildlife researcher want a robot that looks like a real animal?",
        "What is a 'tradeoff' in engineering? Give an example from everyday life."
    ],
    "extend_components": [
        ("Cost", "Total expense to build the design — more lifelike materials and larger power sources cost more"),
        ("Environmental Resistance", "How well the design handles rain, mud, extreme temperatures, and UV exposure"),
        ("Noise Level", "How much sound the design produces during operation — quieter is harder to detect")
    ],
    "reflections": [
        "Why does the fundamental feature choice matter more than materials or power?",
        "Describe a tradeoff in your model where improving one output made another worse.",
        "How is iterative design similar to evolution by natural selection?",
        "What would it take to build a robot that is truly indistinguishable from a real animal?",
        "How did running multiple scenarios help you understand the design space?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a 7-component model to evaluate competing biomimicry designs across multiple performance metrics."),
        ("Disciplinary Core Idea", "LS4.C Adaptation", "Animal features are adaptations shaped by natural selection — understanding their function is essential to effective biomimicry."),
        ("Crosscutting Concept", "Structure and Function", "The structure of an animal feature determines its function — and replicating that structure in an engineering context requires understanding WHY the shape works, not just WHAT it looks like.")
    ],
    "cast_items": [
        "Explain how animal adaptations can inspire engineering solutions",
        "Use a model to evaluate tradeoffs between competing design priorities",
        "Iterate on a design based on model data and testing results"
    ],
    "cast_questions": [
        ("Multiple Choice:", "An engineer designs two underwater robots: Robot A uses silicone skin (lifelike) and Robot B uses hard plastic. Both have the same power source. According to the tradeoff model, which statement is MOST LIKELY true? A) Robot A has better durability B) Robot B has lower detection risk C) Robot A uses more energy D) Both have identical performance"),
        ("Constructed Response:", "A wildlife research team needs a robot bird to observe eagle nests. Using your model, recommend a design approach. Which animal feature should they copy first? What material and power tradeoffs should they consider? Use evidence from your model simulations.")
    ],
    "background_intro": "This lesson builds on Level 1's simple tail-shape model by expanding to a full engineering design system with seven interacting components. Students now experience the full complexity of biomimicry design decisions.",
    "background_sections": [
        ("The Science of Biomimicry", "Biomimicry has produced remarkable innovations: Velcro (burrs), bullet trains (kingfisher beaks), solar panels (leaf photosynthesis), water collection (Namib beetle), adhesives (gecko feet), and more. In each case, engineers studied HOW a natural feature works, then adapted the PRINCIPLE (not an exact copy) for human use."),
        ("Real Animal Robots", "Engineers have built robotic fish (MIT's SoFi, which swims alongside real fish), robotic birds (Festo's SmartBird), robotic insects (Harvard's RoboBee), and robotic snakes (Carnegie Mellon). These bio-inspired robots are used for environmental monitoring, search and rescue, and scientific research."),
        ("The Tradeoff Challenge", "Every engineering design involves tradeoffs. Making a robot more lifelike requires softer, more flexible materials — but these are less durable. Larger batteries provide more runtime — but add weight that reduces mobility. Faster movement looks more natural — but drains power quickly. There is no perfect design, only optimal balances for specific use cases."),
        ("Evolution as R&D", "Evolution through natural selection has been 'testing designs' for 3.8 billion years. Every living organism represents a solution that has been refined over millions of generations. This is why biomimicry works — nature has already explored the design space more thoroughly than any human R&D department ever could.")
    ],
    "lever_L": "Students identify Animal Feature, Material Choice, and Power Source as external design decisions. Movement Accuracy, Energy Use, Durability, and Detection Risk are internal performance outcomes.",
    "lever_E": "Students discover complex relationships: better materials improve accuracy and reduce detection risk but increase energy use and decrease durability. More power improves all performance metrics but has diminishing returns and adds weight.",
    "lever_V": "Students build the 7-component model with three inputs feeding four outputs through interconnected relationships.",
    "lever_Ev": "Students run four scenarios testing different design philosophies and comparing outcomes across all four metrics.",
    "lever_R": "Students add Cost, Environmental Resistance, or Noise Level to see how real-world constraints further complicate design decisions.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Robot fish swimming with real fish", "say": "Remember Level 1 — we learned that flat tails swim best. NOW we design a complete animal robot. Can we fool real animals?", "do": "Show video of MIT's SoFi robot fish swimming with real fish in coral reefs.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we tackle the FULL design challenge — not just one feature, but the whole robot.", "do": "Pre-teach 'fidelity,' 'constraint,' and 'iteration.' Connect to Level 1 vocabulary.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Can a robot fool real animals?", "say": "What would it take to build a robot so lifelike that a real beaver thinks it is another beaver?", "do": "Brainstorm in groups: List everything a robot would need to fool a real animal (appearance, movement, sound, smell?).", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps with tradeoff emphasis", "say": "This model has TRADEOFFS — improving one thing makes another worse. Welcome to real engineering.", "do": "Preview the concept of tradeoffs with a simple example: a heavier backpack carries more but is harder to walk with.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "7 component cards", "say": "Three design decisions you make, four performance outcomes you measure. Sort them.", "do": "Guide sorting. Emphasize: the externals are CHOICES, the internals are CONSEQUENCES of those choices.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Complex relationship web", "say": "This is where it gets interesting. Better materials improve accuracy BUT also increase energy use. That is a tradeoff.", "do": "Draw relationships. Key: some arrows are positive AND negative from the same input. Highlight the tradeoff tension.", "time": "10 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Four design scenarios", "say": "Four designs, four philosophies. High fidelity, budget build, power boost, and wrong feature. Which wins?", "do": "Run all four scenarios. Create a comparison table. Key moment: wrong feature scenario shows that fundamentals beat materials.", "time": "12 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Tradeoff analysis", "say": "There is NO perfect design. But there are SMART designs that balance tradeoffs for the specific mission.", "do": "Summarize the key tradeoffs. Discuss: Which design would YOU choose for a specific mission?", "time": "4 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Engineering sketchbook", "say": "Now design YOUR animal robot. Every choice must be justified with model data.", "do": "Distribute sketchbook materials. Students choose an animal, research adaptations, and design a robot with tradeoff analysis.", "time": "12 min"}
    ],
    "sort_reasoning": "Animal Feature Selected, Material Choice, and Power Source are external because they are DESIGN DECISIONS the engineer makes before building. Movement Accuracy, Energy Use, Durability, and Detection Risk are internal because they are PERFORMANCE OUTCOMES determined by those design choices — you cannot set them directly, only influence them through your decisions.",
    "relationships": [
        ("Animal Feature to Movement Accuracy", "VARIES", "Choosing the right feature (e.g., flat tail for swimming) dramatically improves movement accuracy. The wrong feature (pointed tail in water) cannot be compensated for by other choices."),
        ("Material Choice to Movement Accuracy", "POSITIVE (+) with more lifelike materials", "More flexible, lifelike materials (silicone, soft polymers) allow more natural movement. Rigid materials (hard plastic, metal) create stiff, unnatural motion."),
        ("Material Choice to Detection Risk", "NEGATIVE (-) with more lifelike materials", "More lifelike materials reduce detection risk — they look and feel more like real animal tissue. Hard, shiny materials are immediately identifiable as artificial."),
        ("Material Choice to Energy Use", "POSITIVE (+) with more lifelike materials", "Softer, more lifelike materials require more energy to actuate — they absorb energy that rigid materials would transmit directly. Moving a soft silicone tail takes more power than a hard plastic one."),
        ("Material Choice to Durability", "NEGATIVE (-) with more lifelike materials", "Soft, flexible materials wear out faster than rigid ones. Silicone tears, soft polymers degrade in UV light, while hard plastic lasts years."),
        ("Power Source to all outputs", "GENERALLY POSITIVE", "More power improves movement accuracy and reduces detection risk (smoother movement), but has diminishing returns and adds weight that can increase detection risk if the robot becomes unnaturally heavy.")
    ],
    "sim_answers": [
        ("High Fidelity Scenario", "Silicone materials give excellent Movement Accuracy and low Detection Risk, but Energy Use is high and Durability is moderate. This is the best design for short-term observation missions where looking realistic is critical."),
        ("Budget Build Scenario", "Hard plastic reduces Movement Accuracy and increases Detection Risk (looks obviously artificial), but Energy Use is low and Durability is high. Good for long-term monitoring where animals have already habituated to the device."),
        ("Power Boost Scenario", "Maximum power improves Movement Accuracy over the base high-fidelity design, but the larger battery adds weight and size, slightly increasing Detection Risk. Diminishing returns — twice the power does NOT give twice the accuracy."),
        ("Wrong Feature Scenario", "A pointed tail in water gives poor Movement Accuracy regardless of premium materials and maximum power. Detection Risk is high because the movement pattern is unnatural. This proves that fundamental feature choice matters more than execution quality — you cannot polish a bad design into a good one.")
    ],
    "reflection_exemplars": [
        ("Why does feature choice matter most?", "The animal feature determines the FUNDAMENTAL physics of how the robot interacts with its environment. A flat tail pushes water efficiently because of how fluid dynamics work — no material or power source can change the physics. If the basic shape is wrong, everything built on top of it is compromised. This is like building a house on a bad foundation — no amount of beautiful furniture fixes a cracked foundation."),
        ("How is iteration like evolution?", "In iteration, engineers test a design, measure what works and what doesn't, change the weakest part, and test again. Over many cycles, the design improves. In evolution, organisms with better-adapted features survive and reproduce, passing on those features. Over many generations, the species improves. Both processes improve designs through repeated testing and selection — the difference is that evolution is unguided and takes millions of years, while engineering is intentional and takes months.")
    ],
    "stem_intro": "Present the challenge: Choose a real animal, research its three most important adaptations, then design a robot that borrows those features. Create a detailed engineering sketchbook with: labeled diagrams, material specifications, power budget, tradeoff analysis, and model data supporting each decision.",
    "stem_concepts": [
        ("Form Follows Function", "Copy the PRINCIPLE of the adaptation, not just the appearance. A gecko-grip glove does not look like a gecko — it copies the microscopic hair structure."),
        ("Tradeoff Matrix", "Create a table comparing your design across all four output metrics. Which tradeoffs are acceptable for your specific mission?"),
        ("Iterative Improvement", "Your first design will not be perfect. Identify the weakest metric and redesign to improve it — without destroying other metrics.")
    ],
    "stem_eval": [
        ("Expert (4)", "Sketchbook includes detailed diagrams, justified material choices, power budget, tradeoff matrix, and model data references for each decision. Design is iterated at least once."),
        ("Proficient (3)", "Sketchbook includes clear diagrams, material choices with some justification, and identifies at least two tradeoffs"),
        ("Developing (2)", "Sketchbook has a design but lacks clear connection between choices and model data"),
        ("Beginning (1)", "Sketchbook is incomplete or design choices are not justified with evidence")
    ],
    "support": [
        "Provide animal adaptation reference cards with photos and function descriptions",
        "Pre-made tradeoff matrix template for students to fill in",
        "Gallery of real biomimicry products for inspiration (gecko tape, shark skin swimsuit, kingfisher train)"
    ],
    "extensions": [
        "Build a physical prototype of one component of your robot design using recycled materials",
        "Research the cost of real biomimicry materials and create a budget for your design",
        "Compare your design to an existing biomimicry robot — how do the tradeoffs differ?"
    ],
    "cross_curr": [
        ("Math", "Create a radar/spider chart comparing your design's four output metrics. Calculate a composite score using weighted averages based on mission priorities."),
        ("ELA", "Write a grant proposal requesting funding for your robot design, including the problem it solves, the science behind it, and the expected tradeoffs."),
        ("Art", "Create a full-color rendering of your robot design in its natural habitat, showing how it blends in with real animals.")
    ],
    "misconceptions": [
        ("The most expensive design is always the best", "Expensive materials and large power sources do not guarantee the best performance. The 'wrong feature' scenario proves that a fundamentally flawed design cannot be saved by premium components. The best design is the one that makes the RIGHT fundamental choices, then uses appropriate (not necessarily expensive) materials to execute them.", "Compare: a cheap bicycle with the right gear ratio beats an expensive car in a narrow alley. The right tool for the job beats the most expensive tool."),
        ("Robots need to look exactly like animals to fool them", "Most animals rely primarily on MOVEMENT and BEHAVIOR, not visual appearance. A robot that moves like a real animal but looks slightly different may fool animals better than a photorealistic robot that moves unnaturally. Movement accuracy is often more important than visual fidelity.", "Show video of a crude sock puppet that moves naturally vs. a detailed stuffed animal that sits still. Which attracts the real animal's attention?"),
        ("More power always makes robots better", "The power boost scenario shows diminishing returns. Doubling battery size does NOT double performance. Extra power adds weight, heat, and size — all of which can INCREASE detection risk. Real engineers optimize for efficiency (maximum output per unit of energy), not raw power.", "Analogy: eating twice as much food does not make you twice as fast. There is an optimal amount — too little and you are weak, too much and you are sluggish.")
    ],
    "game": {
        "title": "Bio-Blueprint Bingo",
        "type": "Vocabulary + Matching Game",
        "description": "Each bingo card has animal adaptations (echolocation, webbed feet, camouflage, compound eyes, etc.) paired with engineering applications. Teacher calls out an engineering problem ('We need a robot that can navigate in the dark'), students mark the matching animal adaptation. Five in a row wins.",
        "materials": ["Custom bingo cards (class set)", "Engineering problem call-out cards (25+)", "Bingo markers", "Prize stickers"],
        "learning_connection": "Builds biomimicry vocabulary rapidly and trains students to connect engineering problems to nature's solutions — the core thinking skill of biomimicry design."
    },
    "steam_activity": {
        "title": "Animal Robot Sketchbook",
        "type": "Engineering Design + Art",
        "description": "Students choose a real animal, research three key adaptations, then create a detailed engineering sketchbook of a robot that borrows those features. Each adaptation must be labeled with: (1) what the animal uses it for, (2) what the robot uses it for, (3) what tradeoff it creates. Gallery walk for peer review and feedback.",
        "materials": ["Blank sketchbooks or folded paper booklets", "Colored pencils and fine-tip markers", "Animal adaptation reference library", "Tradeoff matrix templates", "Gallery walk feedback forms"],
        "learning_connection": "Students apply the full 7-component model thinking to an original design — making choices, predicting tradeoffs, and defending decisions with model data."
    }
}

L2_03 = {
    "id": "NE-L2-03",
    "title": "Ecohydrology — Fire-Resistant Landscapes",
    "subtitle": "How Beavers Create Nature's Firebreaks",
    "ngss": "MS-ESS2-4, MS-ESS3-3, MS-ESS3-4, MS-LS2-4",
    "ngss_desc": "Develop a model to describe the cycling of water through Earth's systems driven by energy from the sun and the force of gravity. Apply scientific principles to design a method for monitoring and minimizing a human impact on the environment. Construct an argument supported by evidence for how increases in human population and per-capita consumption of natural resources impact Earth's systems. Construct an argument supported by empirical evidence that changes to physical or biological components of an ecosystem affect populations.",
    "big_question": "How do beaver dams create fire-resistant green corridors in landscapes devastated by wildfire?",
    "objectives": [
        "Explain how beaver dams raise groundwater levels and maintain soil moisture during drought",
        "Model an 8-component ecohydrology system showing how beaver activity reduces fire spread",
        "Analyze the relationship between drought severity, groundwater, vegetation health, and fire behavior",
        "Evaluate the role of beavers as a nature-based solution for wildfire resilience"
    ],
    "vocabulary": [
        ("Ecohydrology", "The study of how water movement through ecosystems affects living things — and how living things affect water movement"),
        ("Firebreak", "A gap or barrier in vegetation that slows or stops the spread of wildfire"),
        ("Groundwater", "Water stored underground in soil and rock — the hidden water supply that keeps plants alive during drought"),
        ("Green Corridor", "A strip of lush, well-watered vegetation that stays green even when surrounding areas dry out and burn"),
        ("Water Table", "The underground level below which the ground is completely saturated with water")
    ],
    "components": [
        ("Precipitation", "How much rain and snow falls in the watershed — the primary water input to the system", True),
        ("Beaver Dam Count", "How many beaver dams are present along the waterway — more dams means more water storage and distribution", True),
        ("Drought Severity", "How intense and prolonged the dry conditions are — higher drought means less available moisture everywhere", True),
        ("Groundwater Level", "How high the underground water table sits — higher groundwater means plant roots can reach water even in dry conditions", False),
        ("Soil Moisture", "How much water is held in the top layers of soil — determines whether plants can survive and whether the ground can burn", False),
        ("Vegetation Health", "How green, hydrated, and alive the plants are — healthy vegetation resists fire, stressed vegetation becomes fuel", False),
        ("Surface Runoff", "How much water flows across the surface without soaking in — lower runoff means more water stays in the landscape", False),
        ("Fire Spread Rate", "How quickly wildfire moves across the landscape — determined by vegetation moisture, wind, and terrain", False)
    ],
    "think_about_it": "Trace two paths: What happens when beaver dams are PRESENT during a drought vs. when they are ABSENT? How does each path end at Fire Spread Rate?",
    "scenarios": [
        ("With Beavers in Drought", "Beaver Dam Count high, Precipitation low, Drought Severity high — observe how the beaver-created corridor responds"),
        ("Without Beavers in Drought", "Beaver Dam Count zero, Precipitation low, Drought Severity high — compare fire spread to the beaver scenario"),
        ("Normal Rainfall", "Beaver Dam Count moderate, Precipitation normal, Drought Severity low — observe baseline conditions"),
        ("Extreme Drought", "Beaver Dam Count high, Precipitation near zero, Drought Severity extreme — can even beavers survive this?")
    ],
    "sim_scenarios": [
        ("With Beavers in Drought", "Many dams, low rain, high drought", "What do you predict — will the area near beaver dams stay green during a drought?"),
        ("Without Beavers in Drought", "No dams, low rain, high drought", "Without beaver dams storing water, what happens to groundwater and vegetation?"),
        ("Normal Rainfall", "Moderate dams, normal conditions", "How does the system behave when water is not scarce?"),
        ("Extreme Drought", "Many dams, almost no rain, extreme drought", "Is there a drought level so severe that even beaver dams cannot maintain green corridors?")
    ],
    "discoveries": [
        "Beaver dams raise the groundwater level by spreading and storing water across the floodplain — creating an underground reservoir",
        "Higher groundwater keeps soil moist even during drought, allowing vegetation to stay green and hydrated",
        "Green, hydrated vegetation does NOT burn easily — it creates a natural firebreak that slows or stops fire spread",
        "Without beaver dams, drought quickly drains soil moisture, vegetation dries out, and fire spreads rapidly through the landscape",
        "Beaver dams also REDUCE surface runoff — keeping more water in the landscape instead of letting it flow away"
    ],
    "answer": "Beaver dams create fire-resistant green corridors through a chain of water management. The dams slow water flow, spread it across the floodplain, and raise the groundwater table. This elevated groundwater keeps soil moist and vegetation green — even during drought when surrounding areas dry out and become fuel for wildfire. Dr. Emily Fairfax's peer-reviewed research shows that beaver-dammed areas stay green and resist fire while adjacent undammed areas burn. The beavers are not fighting fire directly — they are managing WATER in a way that makes the landscape naturally fire-resistant.",
    "stem_title": "Drought vs. Dam Time-Lapse Terrarium",
    "stem_mission": "Build two terrariums — one with a miniature dam and water reservoir, one without — then withhold water for two weeks to observe which landscape stays green longer.",
    "stem_scenario": "A wildfire research team wants to demonstrate how beaver dams protect landscapes during drought. Your team will build a physical model that shows the difference between a dammed and undammed watershed over a simulated drought period.",
    "stem_questions": [
        "After one week without water, which terrarium has greener vegetation — the one with or without the dam?",
        "Where is the soil still moist in each terrarium? Dig down and compare.",
        "How does this physical model connect to what your computational model predicted about groundwater and vegetation health?"
    ],
    "stem_design_qs": [
        "How will you build a miniature dam and reservoir that actually stores water in the soil?",
        "What plants will you use that will show visible changes when they lose water?",
        "How will you measure soil moisture at different depths over the two weeks?",
        "How will you control all variables so the ONLY difference between the two terrariums is the dam?"
    ],
    "career": "Ecohydrologists study how water and ecosystems interact. They work on wildfire management, watershed restoration, and climate adaptation projects for government agencies, universities, and conservation organizations. They earn $60,000–$100,000/year.",
    "images": {
        "cover": ("cover-ecohydrology-fire.png", "A stunning photorealistic aerial image showing a dramatic contrast — a lush green riparian corridor with beaver ponds snaking through a charred, blackened post-wildfire landscape, the green corridor is vivid and alive while the surrounding hills are burned, drone photography, golden hour light, nature documentary quality"),
        "landscape": ("landscape-ecohydrology.png", "A photorealistic image of diverse 6th-8th grade students (11-14 years old) examining two terrariums side by side on a lab table, one with a small dam and reservoir showing green plants and one without showing wilted brown plants, Latin American female student in the lead measuring soil moisture with a probe, Black, Asian/AAPI, and White students recording data, modern science classroom, natural window light"),
        "modeling": ("modeling-ecohydrology.png", "A photorealistic image of diverse 6th-8th grade students working on Chromebooks with an 8-component model visible on screen showing water flow relationships, Black male student pointing at the screen explaining a connection to his group, genuinely diverse classmates engaged and taking notes, modern STEM classroom"),
        "discussion": ("discussion-ecohydrology.png", "A photorealistic image of an Asian/AAPI female teacher projecting satellite imagery showing green beaver corridors surrounded by burned landscape, diverse 6th-8th grade students fascinated and raising hands, modern classroom with science posters about watersheds and fire ecology"),
        "stem": ("stem-ecohydrology.png", "A photorealistic image of diverse 6th-8th grade students building terrariums with soil layers, small plants, and miniature dams made from clay and sticks, White female student and Latin American male student collaborating on the dam construction, science lab with natural light")
    },
    "pre_assessment": [
        "In Level 1 Sponge vs. Pavement, you learned that ground type affects water absorption and runoff. What happens to water absorption in a NATURAL landscape during drought?",
        "Have you ever seen areas that stayed green when everything around them was brown and dry? Why do you think that happens?",
        "How might a beaver dam affect the land AROUND it — not just the pond behind it?",
        "Draw what you think happens underground when a beaver dam stores water."
    ],
    "extend_components": [
        ("Wind Speed", "How fast the wind blows during a fire event — wind accelerates fire spread and dries vegetation faster"),
        ("Terrain Slope", "How steep the land is — fire moves faster uphill and water drains faster on steep slopes"),
        ("Vegetation Density", "How thick the plant cover is — denser vegetation can mean more fuel OR more moisture depending on health")
    ],
    "reflections": [
        "How is the Level 2 ecohydrology model different from the Level 1 Sponge vs. Pavement model? What new components reveal about fire resistance?",
        "Compare the With Beavers and Without Beavers drought scenarios — what is the CRITICAL difference in the cascade?",
        "Why are beavers sometimes called 'nature's firefighters' even though they do not fight fire directly?",
        "What surprised you most when comparing the simulation scenarios?",
        "How could land managers use this model to make decisions about wildfire prevention?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop an 8-component computational model showing how beaver-driven water management creates fire-resistant green corridors through cascading ecohydrological relationships."),
        ("Disciplinary Core Idea", "ESS2.C The Roles of Water in Earth's Surface Processes", "Water movement through beaver-dammed landscapes raises groundwater, maintains soil moisture, and sustains vegetation — demonstrating how water cycling shapes surface conditions and fire behavior."),
        ("Crosscutting Concept", "Cause and Effect", "Students trace the causal chain from beaver dams through groundwater, soil moisture, and vegetation health to fire spread rate — identifying that each step in the cascade has a predictable effect on the next.")
    ],
    "cast_items": [
        "Explain the ecohydrological cascade from beaver dams to fire resistance",
        "Use the model to compare fire outcomes in beaver-dammed vs. undammed landscapes during drought",
        "Evaluate beavers as a nature-based solution for wildfire management"
    ],
    "cast_questions": [
        ("Multiple Choice:", "During a severe drought, satellite imagery shows a narrow strip of green vegetation along a stream while the surrounding hillsides are brown and dry. According to the ecohydrology model, what is the MOST LIKELY explanation? A) The stream has more rainfall than the hillsides B) Beaver dams raised the groundwater level, keeping soil moist and vegetation green C) The vegetation along the stream is a different species that does not need water D) The fire burned everything except the stream area by coincidence"),
        ("Constructed Response:", "Using your 8-component model, explain step by step why a landscape WITHOUT beaver dams is more vulnerable to wildfire during drought than one WITH beaver dams. Trace the cascade from Beaver Dam Count through Groundwater Level, Soil Moisture, Vegetation Health, and Fire Spread Rate. Use evidence from your simulation scenarios.")
    ],
    "background_intro": "This lesson builds on Level 1 Sponge vs. Pavement by expanding the water absorption concept into a full ecohydrology system. Students now see how beaver-engineered water management creates fire-resistant landscapes — based on peer-reviewed research by Dr. Emily Fairfax and colleagues.",
    "background_sections": [
        ("The Fairfax Research", "In 2020, Dr. Emily Fairfax and colleagues published groundbreaking research in the journal Ecosphere showing that beaver-dammed sections of streams maintained green, hydrated vegetation corridors even when surrounding landscapes were scorched by wildfire. Using satellite imagery from multiple large wildfires across the American West, the research team demonstrated that beaver-created wetlands acted as natural firebreaks. The key mechanism: beaver dams raise the water table, keeping soil saturated and vegetation too moist to burn."),
        ("How Beaver Dams Manage Water", "Beaver dams do not just create ponds — they fundamentally change how water moves through a landscape. By slowing streamflow, beaver dams force water to spread laterally across the floodplain. This water soaks into the ground, raising the water table for hundreds of meters on either side of the stream. The elevated water table keeps plant roots in contact with moisture even during surface-level drought. The result: a green, hydrated ribbon of vegetation surrounded by dry, fire-prone land."),
        ("Fire Behavior and Vegetation Moisture", "Fire spreads through dry fuel — dead leaves, dry grass, and stressed vegetation with low moisture content. When vegetation is well-hydrated, it resists ignition and slows fire spread dramatically. A strip of green, moist vegetation can act as a natural firebreak, stopping or redirecting a wildfire the same way a paved road or a cleared strip would. The difference is that beaver-created firebreaks are LIVING ecosystems that also support wildlife, filter water, and store carbon."),
        ("Beavers as Climate Adaptation", "As climate change increases drought frequency and wildfire intensity across the western United States, land managers are increasingly looking to beavers as a low-cost, self-maintaining wildfire resilience strategy. Reintroducing beavers to degraded streams costs far less than engineered firebreaks and provides year-round ecosystem services. Several states have begun 'beaver relocation' programs, moving conflict beavers from urban areas to fire-prone watersheds.")
    ],
    "lever_L": "Students identify Precipitation, Beaver Dam Count, and Drought Severity as external components — environmental conditions that can be observed and set. Groundwater Level, Soil Moisture, Vegetation Health, Surface Runoff, and Fire Spread Rate are internal components that change based on the externals and each other.",
    "lever_E": "Students trace the relationships: Beaver Dam Count positively affects Groundwater Level and negatively affects Surface Runoff. Precipitation positively affects Groundwater Level. Drought Severity negatively affects Soil Moisture. Groundwater Level positively affects Soil Moisture. Soil Moisture positively affects Vegetation Health. Vegetation Health negatively affects Fire Spread Rate.",
    "lever_V": "Students build the full 8-component model with three external inputs feeding five internal components through a web of positive and negative relationships.",
    "lever_Ev": "Students run four scenarios — with beavers, without beavers, normal conditions, and extreme drought — to see how beaver presence dramatically changes fire outcomes.",
    "lever_R": "Students add Wind Speed, Terrain Slope, or Vegetation Density to explore how additional factors modify the fire behavior equation.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Aerial photo of green beaver corridor through burned landscape", "say": "Look at this image. The land burned everywhere EXCEPT along this stream. Why? Today we figure out how beavers create nature's firebreaks.", "do": "Show satellite or aerial imagery from Dr. Fairfax's research. Ask: What do you notice about the green area vs. the burned area?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "We are building an 8-component ecohydrology model — our biggest yet. This model explains how water underground connects to fire above ground.", "do": "Preview vocabulary: ecohydrology, firebreak, groundwater, green corridor. Connect to Level 1 Sponge vs. Pavement knowledge.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How do beaver dams create fire-resistant landscapes?", "say": "Beavers do not spray water on fires. They do not clear brush. So how do scientists say they create fire-resistant landscapes?", "do": "Think-pair-share: How could an animal that builds dams in water affect fire on land? Students brainstorm connections.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps with ecohydrology focus", "say": "Our model today has BOTH positive and negative relationships — and the cascade goes from water underground to fire above ground.", "do": "Preview the cascade direction: water inputs → groundwater → soil → vegetation → fire. Emphasize underground-to-surface connection.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "8 component cards for ecohydrology model", "say": "Three things the environment controls, five things the SYSTEM produces. Let us sort them — which are inputs and which are outputs?", "do": "Guide sorting of all 8 components. Key discussion: Drought Severity is external because humans do not control it, but it has powerful effects on the system.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship web with positive and negative arrows", "say": "Here is where it gets fascinating. Beaver dams push Groundwater UP but push Surface Runoff DOWN. And Vegetation Health pushes Fire Spread Rate DOWN. These negative relationships are KEY.", "do": "Build the relationship web arrow by arrow. Color-code: green arrows for positive, red arrows for negative. Key teaching moment: the negative relationship between Vegetation Health and Fire Spread Rate.", "time": "10 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Four scenario comparisons", "say": "Our big test: same drought, same landscape — the ONLY difference is beaver dams. Predict what happens, then watch the model.", "do": "Run With Beavers vs. Without Beavers scenarios back-to-back. Record predictions BEFORE running. The contrast is dramatic. Then test Normal and Extreme Drought.", "time": "12 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key ecohydrology findings and real research images", "say": "Beavers are not firefighters — they are water managers. And managing water turns out to be the best way to manage fire.", "do": "Summarize key findings. Show Dr. Fairfax's real satellite imagery. Discuss: How could this change wildfire policy?", "time": "4 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Drought vs. Dam terrarium experiment", "say": "Now build it and prove it. Two terrariums, two weeks, one question: does the dam keep the landscape green?", "do": "Distribute terrarium materials. Groups set up paired terrariums with and without dams. Begin the two-week drought observation.", "time": "12 min"}
    ],
    "sort_reasoning": "Precipitation, Beaver Dam Count, and Drought Severity are external because they are environmental conditions that exist independently of the model — we can observe and set them. Groundwater Level, Soil Moisture, Vegetation Health, Surface Runoff, and Fire Spread Rate are internal because they are PRODUCED by the system — each one depends on the external inputs and on other internal components in the cascade chain.",
    "relationships": [
        ("Beaver Dam Count to Groundwater Level", "POSITIVE (+)", "More beaver dams slow water flow and spread it across the floodplain, forcing water to soak underground. Each dam raises the water table in the surrounding area by creating sustained water contact with the soil."),
        ("Beaver Dam Count to Surface Runoff", "NEGATIVE (-)", "More beaver dams trap and slow surface water, reducing the amount that flows downstream as runoff. Water that would have rushed away is instead stored in ponds and soaked into the ground."),
        ("Precipitation to Groundwater Level", "POSITIVE (+)", "More rain and snow provide more water to recharge groundwater. Precipitation is the primary water input — without it, even beaver dams cannot maintain groundwater indefinitely."),
        ("Drought Severity to Soil Moisture", "NEGATIVE (-)", "Longer, more intense drought dries out the upper soil layers through evaporation and plant water use. Drought directly attacks soil moisture from the surface downward."),
        ("Groundwater Level to Soil Moisture", "POSITIVE (+)", "Higher groundwater tables keep the lower and middle soil layers saturated, which wicks moisture upward to plant roots. Even when the surface is dry, elevated groundwater maintains deeper soil moisture."),
        ("Soil Moisture to Vegetation Health", "POSITIVE (+)", "Plants with access to soil moisture stay green, hydrated, and alive. When soil moisture drops below a critical threshold, plants wilt, dry out, and become dead fuel for fire."),
        ("Vegetation Health to Fire Spread Rate", "NEGATIVE (-)", "Healthy, hydrated vegetation resists ignition and slows fire spread. Green plants contain 100-200% of their dry weight in water, making them extremely difficult to burn. Dry, dead vegetation burns rapidly.")
    ],
    "sim_answers": [
        ("With Beavers in Drought Scenario", "Despite low Precipitation and high Drought Severity, Beaver Dam Count keeps Groundwater Level elevated because the dams stored water from previous rains. Groundwater maintains Soil Moisture in the root zone. Vegetation Health stays moderate to good — plants remain green. Fire Spread Rate is LOW along the beaver corridor because the vegetation is too moist to burn easily. Surface Runoff is low because the dams trapped the water. This is exactly what Dr. Fairfax observed in real wildfires."),
        ("Without Beavers in Drought Scenario", "With zero Beaver Dam Count, Groundwater Level drops quickly because there is nothing to slow and store water. Drought Severity drains Soil Moisture from above while low groundwater fails to replenish it from below. Vegetation Health crashes — plants dry out, wilt, and die. Fire Spread Rate is HIGH because the dry vegetation is perfect fuel. Surface Runoff was high during previous rains (no dams to stop it), meaning less water was stored in the landscape."),
        ("Normal Rainfall Scenario", "With moderate Beaver Dam Count and normal Precipitation, the system is well-balanced. Groundwater Level is healthy. Soil Moisture is adequate. Vegetation Health is good. Fire Spread Rate is low. Surface Runoff is moderate. This baseline shows the system working as intended — beaver dams enhance water storage but the benefit is less dramatic when rain is plentiful."),
        ("Extreme Drought Scenario", "Even with high Beaver Dam Count, extreme drought with near-zero Precipitation eventually overwhelms the beaver-created buffer. Groundwater Level drops as stored water is depleted without replenishment. Soil Moisture falls despite the elevated groundwater. Vegetation Health declines. Fire Spread Rate increases — though still LOWER than without beavers. This shows that beavers BUFFER drought but cannot create water from nothing. There is a limit to their protection.")
    ],
    "reflection_exemplars": [
        ("How is this model different from Level 1?", "Level 1 Sponge vs. Pavement showed that ground type affects absorption and runoff — a simple 4-component system. Level 2 expands this into an 8-component ecohydrology model that includes underground water, living vegetation, AND fire behavior. The biggest difference is seeing the CHAIN: water goes underground (groundwater), feeds the soil, feeds the plants, and those living plants stop fire. Level 1 was about surfaces. Level 2 is about the hidden underground system that keeps the surface alive."),
        ("Why are beavers called nature's firefighters?", "Beavers do not fight fire directly — they manage WATER in a way that makes landscapes fire-resistant. Their dams slow water down, spread it across the floodplain, and push it underground. This underground reservoir keeps soil moist and vegetation green during drought. When wildfire comes, the green beaver corridor does not burn because the plants are too wet. The beavers created a firebreak not by clearing vegetation, but by keeping it ALIVE. Dr. Fairfax's satellite imagery proves this — you can literally see the green beaver corridors surrounded by burned land.")
    ],
    "stem_intro": "Present the terrarium challenge: Build two identical terrariums — one with a miniature dam and reservoir made from clay and sticks, one without. Plant the same fast-growing seeds in both. Water both equally for one week, then stop ALL watering for two weeks. Observe which landscape stays green, measure soil moisture at multiple depths, and photograph changes daily.",
    "stem_concepts": [
        ("Water Storage Underground", "The dam in your terrarium should store water in the soil layers below the surface — not just in a visible pond. Pack the dam into the soil so water seeps down and spreads."),
        ("Drought Simulation", "Stopping all watering simulates drought. The terrarium with stored underground water should keep plants alive longer — just like beaver dams during real droughts."),
        ("Controlled Experiment", "Both terrariums must be IDENTICAL except for the dam. Same soil, same seeds, same light, same initial watering. The dam is the only variable.")
    ],
    "stem_eval": [
        ("Expert (4)", "Both terrariums built with identical conditions except dam, daily measurements of soil moisture and plant health, clear data showing difference, strong connection to computational model predictions"),
        ("Proficient (3)", "Terrariums built with reasonable controls, regular measurements taken, student can explain how the dam affects soil moisture"),
        ("Developing (2)", "Terrariums built but controls are inconsistent, measurements are sporadic, weak connection to model"),
        ("Beginning (1)", "Terrarium setup is incomplete or student cannot explain the connection between the dam, soil moisture, and plant health")
    ],
    "support": [
        "Provide a step-by-step terrarium setup guide with photos showing how to embed the miniature dam in soil layers",
        "Give students pre-made data recording sheets with spaces for daily soil moisture readings and plant health observations",
        "Sentence frames: 'After __ days without water, the terrarium WITH the dam had __ soil moisture because __'"
    ],
    "extensions": [
        "Research Dr. Emily Fairfax's actual published study and compare her satellite imagery findings to your terrarium results",
        "Design a proposal for beaver reintroduction in a fire-prone watershed near your school — include costs, benefits, and potential challenges",
        "Model how CLIMATE CHANGE (increasing drought frequency) changes the value of beaver dams over time — do they become MORE important as droughts worsen?"
    ],
    "cross_curr": [
        ("Math", "Measure soil moisture at three depths (surface, mid, deep) in both terrariums daily for two weeks. Create line graphs comparing moisture retention over time and calculate the rate of moisture loss in each."),
        ("ELA", "Write a scientific argument using the Claim-Evidence-Reasoning framework: Claim that beaver dams reduce wildfire risk, Evidence from your model and terrarium data, Reasoning that connects the ecohydrological cascade."),
        ("Art", "Create an infographic showing the underground water system of a beaver-dammed landscape vs. an undammed landscape, with labeled cross-section views showing groundwater, soil moisture, root zones, and fire behavior.")
    ],
    "misconceptions": [
        ("Beavers prevent all wildfires", "Beavers do not prevent wildfire — they create LOCALIZED fire-resistant corridors along waterways. The green corridor may be only 50-200 meters wide on either side of the stream. Upland areas away from the stream still burn. Beavers are part of a wildfire resilience strategy, not a complete solution.", "Show aerial imagery of a beaver corridor: green along the stream, burned on the hillsides. Ask: If you were a wildfire manager, where would you place beaver dams and what ELSE would you do?"),
        ("Water on the surface is what stops fire", "Surface water (ponds, streams) helps, but the REAL mechanism is UNDERGROUND water. Beaver dams raise the water table, which keeps soil saturated and plant roots hydrated. A dry hillside with a stream at the bottom can still burn. But a hillside with a HIGH WATER TABLE — where the underground water reaches plant roots — stays green and resists fire.", "Demonstrate: pour water on top of dry soil (it runs off). Then show soil that was saturated from below (it stays moist even on the surface). Which one would burn?"),
        ("Beaver dams last forever once built", "Beaver dams require constant maintenance by the beaver colony. Without active beavers repairing damage from storms, ice, and water pressure, dams begin failing within months. Once the dam fails, stored groundwater drains away, soil dries out, vegetation health declines, and the fire resistance disappears. This is why beaver POPULATIONS matter — not just individual dams.", "Show timeline: dam built → maintained → beavers removed → dam decays → water drains → drought vulnerability returns. How long does each stage take?")
    ],
    "game": {
        "title": "Firebreak Challenge",
        "type": "Grid-Based Strategy Game",
        "description": "Students play on a grid board representing a watershed landscape. Wildfire starts at one edge and advances each turn based on dice rolls. Players place beaver dam tokens on stream squares to raise groundwater in adjacent cells, turning them green (fire-resistant). The goal is to strategically place dams to create connected green corridors that stop the fire from reaching a town on the opposite edge. Players must balance limited dam tokens against an advancing fire front.",
        "materials": ["Grid game boards (10x10, 1 per group)", "Beaver dam tokens (8 per team)", "Fire advance tokens (red)", "Green corridor markers", "Dice for fire spread rolls", "Stream path printed on the grid", "Score sheets"],
        "learning_connection": "Reinforces that beaver dams create LOCALIZED fire resistance along waterways — students must think strategically about WHERE to place dams for maximum protection, mirroring real land management decisions."
    },
    "steam_activity": {
        "title": "Drought vs. Dam Time-Lapse Terrarium",
        "type": "Long-Term Experimental Investigation",
        "description": "Student teams build two identical terrariums with soil layers and fast-growing seeds. One terrarium includes a miniature dam and reservoir made from clay and sticks embedded in the soil. Both receive equal watering for one week, then all water is withheld for two weeks to simulate drought. Students photograph changes daily, measure soil moisture at multiple depths, and compare which landscape retains moisture and keeps plants alive. Results are compared to computational model predictions.",
        "materials": ["Clear plastic containers (2 per group)", "Potting soil", "Fast-growing seeds (radish, grass, or bean)", "Modeling clay for miniature dams", "Small sticks for dam structure", "Spray bottles for controlled watering", "Soil moisture meters or probes", "Rulers for plant height measurements", "Daily observation recording sheets", "Phone or tablet for daily photos"],
        "learning_connection": "Physically demonstrates the computational model's core prediction — that stored underground water (from dam-created reservoirs) keeps soil moist and vegetation alive during drought, directly connecting to Dr. Fairfax's research on beaver-created fire-resistant corridors."
    }
}

L2_04 = {
    "id": "NE-L2-04",
    "title": "The Brain-Machine Connection",
    "subtitle": "How Scientists Are Learning to Read Your Mind",
    "ngss": "MS-LS1-8, HS-LS1-2, HS-ETS1-2, HS-ETS1-4",
    "ngss_desc": "Gather and synthesize information that sensory receptors respond to stimuli by sending messages to the brain for immediate behavior or storage as memories. Develop and use a model to describe how the structure of the nervous system allows it to receive, process, and respond to information. Evaluate competing design solutions using a systematic process. Develop a model to generate data for iterative testing and modification of a proposed object, tool, or process.",
    "big_question": "How can scientists decode the electrical language of your brain well enough to move a robotic arm — and why is it so incredibly hard?",
    "objectives": [
        "Explain how brain-computer interfaces convert neural signals into machine commands through sensory pathways",
        "Model an 8-component system showing how stimulus intensity, electrode count, and noise interact to determine motor output",
        "Run scenarios that reveal how noise, adaptation, and electrode placement create tradeoffs in BCI performance",
        "Design and test a communication system that demonstrates the core challenges of brain signal decoding"
    ],
    "vocabulary": [
        ("Brain-Computer Interface (BCI)", "A system that reads electrical signals from the brain and translates them into commands that control a computer or machine"),
        ("Electrode", "A tiny sensor placed on or in the brain that detects electrical activity from nearby neurons"),
        ("Signal Encoding", "The process of translating raw brain signals into a digital code that a computer can interpret"),
        ("Neural Noise", "Random electrical activity from millions of neurons firing at once, which interferes with reading specific signals"),
        ("Adaptation", "The brain's ability to adjust its signal patterns over time to work more effectively with a BCI system")
    ],
    "components": [
        ("Stimulus Intensity", "How strong the sensory input is — a firm touch vs. a light brush, a loud sound vs. a whisper", True),
        ("Electrode Count", "How many sensors are placed on or near the brain to detect electrical signals", True),
        ("Noise Level", "The amount of random neural activity and electronic interference that obscures the target signal", True),
        ("Signal Strength", "How powerful and detectable the brain's electrical response is to the stimulus", False),
        ("Encoding Accuracy", "How precisely the computer translates raw brain signals into meaningful commands", False),
        ("Response Time", "How quickly the system converts a brain signal into a machine action — milliseconds matter", False),
        ("Motor Output Precision", "How accurately the robotic limb or device performs the intended movement", False),
        ("Adaptation Level", "How much the brain and computer have learned to work together through repeated practice", False)
    ],
    "think_about_it": "Trace the chain: A strong stimulus creates a strong signal. More electrodes improve encoding. But what happens when noise floods the system? Can adaptation overcome a noisy environment?",
    "scenarios": [
        ("Best Case", "Stimulus Intensity high, Electrode Count high, Noise Level low — the ideal BCI setup. Observe all outputs at their best."),
        ("Worst Case", "Stimulus Intensity low, Electrode Count low, Noise Level high — everything working against the system. Watch it struggle."),
        ("Adaptation Test", "Same setup as Best Case, but observe how outputs change as Adaptation Level increases over multiple simulated trials."),
        ("Noise Flood", "Stimulus Intensity high, Electrode Count high, Noise Level extreme — can a great setup survive overwhelming interference?")
    ],
    "sim_scenarios": [
        ("Best Case", "Strong stimulus, many electrodes, quiet environment", "What do you predict motor output precision will be when everything is optimal?"),
        ("Worst Case", "Weak stimulus, few electrodes, noisy environment", "How badly does performance degrade when all three inputs are unfavorable?"),
        ("Adaptation Test", "Optimal setup over multiple trials", "Does the system get better with practice? How much can adaptation compensate?"),
        ("Noise Flood", "Great hardware, extreme noise", "Can excellent equipment overcome overwhelming neural noise?")
    ],
    "discoveries": [
        "Stimulus Intensity directly determines Signal Strength — weak inputs produce weak, hard-to-read brain responses",
        "More electrodes dramatically improve Encoding Accuracy by sampling more neural activity from different brain regions",
        "Noise is the greatest enemy of BCI systems — it degrades Encoding Accuracy AND Motor Output Precision simultaneously",
        "Signal Strength and Response Time have an inverse relationship — stronger signals are decoded faster",
        "Adaptation is remarkably powerful — over time, the brain learns to produce cleaner signals that the computer can read more easily",
        "Even the best hardware cannot fully overcome extreme noise, but adaptation can partially compensate"
    ],
    "answer": "Reading the brain's electrical language is one of the greatest challenges in modern science because the brain produces billions of signals simultaneously, and the one you want is buried in an ocean of neural noise. A BCI must detect tiny electrical signals (stimulus intensity), capture them with enough sensors (electrode count), fight through interference (noise level), and then translate that noisy data into precise machine movements. The breakthrough insight is ADAPTATION — the brain and computer learn to work together over time, with the brain producing cleaner signals and the computer getting better at decoding them. This partnership between biological and artificial intelligence is what makes modern BCIs possible.",
    "stem_title": "Prosthetic Hand Design",
    "stem_mission": "Design and build a cardboard-and-string mechanical hand that a partner controls through a barrier using only coded signals — then test how noise and practice affect performance.",
    "stem_scenario": "A biomedical engineering lab needs a demonstration showing why brain-computer interfaces are so challenging. Your team will build a mechanical hand and a signal system that shows how encoding, noise, and adaptation affect motor control — just like a real BCI.",
    "stem_questions": [
        "How accurately can your partner control the hand using only your coded signals?",
        "What happens to performance when noise is introduced to your communication channel?",
        "Does performance improve with practice — and if so, by how much?"
    ],
    "stem_design_qs": [
        "How will you design the coding system — how many distinct signals do you need for five fingers?",
        "What materials will give your hand the most realistic finger movement?",
        "How will you test the effect of noise on your signal accuracy?",
        "How will you measure whether adaptation (practice) improves performance over time?"
    ],
    "career": "Neuroengineers design brain-computer interfaces that help paralyzed patients control robotic limbs, allow locked-in patients to communicate, and treat neurological disorders like epilepsy and Parkinson's disease. They work at research hospitals, tech companies, and universities. They earn $85,000–$150,000/year.",
    "images": {
        "cover": ("cover-brain-machine.png", "A stunning photorealistic close-up of a modern brain-computer interface headset with glowing electrode nodes, soft blue and white light tracing neural pathways across a translucent skull overlay, dark background, scientific visualization meets futuristic technology, cinematic lighting"),
        "landscape": ("landscape-brain-machine.png", "A photorealistic image of genuinely diverse 8th-10th grade students (13-16 years old) in a modern science lab, a Latin American female student wearing an EEG demonstration headset while her classmates watch readings on a monitor, Black male student pointing at the signal display, Asian/AAPI and White students taking notes, modern school lab with neuroscience equipment, natural light from large windows"),
        "modeling": ("modeling-brain-machine.png", "A photorealistic image of genuinely diverse 8th-10th grade students building an 8-component model on laptops, Black female student leading the group discussion and gesturing at the screen showing component relationships, Latin American male student and White female student contributing ideas, modern STEM classroom with brain anatomy posters"),
        "discussion": ("discussion-brain-machine.png", "A photorealistic image of an Asian/AAPI male teacher drawing a diagram on a whiteboard showing the pathway from stimulus to brain signal to electrode to computer to robotic arm, genuinely diverse 8th-10th grade students engaged in discussion, some raising hands, bright modern classroom"),
        "stem": ("stem-brain-machine.png", "A photorealistic image of genuinely diverse 8th-10th grade students building cardboard mechanical hands with strings and straws at lab tables, Black male student in the lead testing finger movements while a Latin American female student pulls control strings from behind a cardboard barrier, White and Asian/AAPI students recording observations, creative engineering workspace with materials spread across tables")
    },
    "pre_assessment": [
        "In the Level 1 Telephone Game lesson, you modeled how signal strength, distance, and noise affect message accuracy. What do you think happens when we add MORE sensors to capture the signal?",
        "If a person who lost their arm could control a robotic hand with their thoughts, what challenges do you think the technology would face?",
        "What does 'practice makes perfect' mean in terms of your brain and body learning to work together?",
        "Draw what you think happens between a person's brain and a robotic arm — what are the steps?"
    ],
    "extend_components": [
        ("Feedback Loop", "Information sent BACK from the robotic limb to the brain — does the user feel what the robot touches?"),
        ("Algorithm Complexity", "How sophisticated the computer software is at filtering noise and decoding signals — more complex algorithms take longer but are more accurate"),
        ("Electrode Invasiveness", "Whether sensors sit on the scalp (safe but weak signals) or are implanted in the brain (risky but strong signals)")
    ],
    "reflections": [
        "How is the Level 2 model different from the Level 1 Telephone Game model? What does adding more components reveal about BCI systems?",
        "Trace the full pathway: Stimulus → Signal Strength → Encoding Accuracy → Motor Output Precision. What happens at each step when noise increases?",
        "Why is adaptation such a powerful factor in BCI performance? What does it tell us about the relationship between brains and machines?",
        "Which scenario surprised you the most and why?",
        "If you were designing a BCI for a real patient, which component would you try to optimize first — and why?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop an 8-component computational model showing how stimulus input, electrode configuration, and noise interact through signal encoding and adaptation to determine motor output precision."),
        ("Disciplinary Core Idea", "LS1.A Structure and Function / LS1.D Information Processing", "The nervous system receives stimuli, encodes signals, and transmits information to produce responses — the same pathway that BCI technology must interface with and decode."),
        ("Crosscutting Concept", "Cause and Effect / Systems and System Models", "Students trace causal chains through an 8-component system where multiple inputs produce cascading effects, and feedback through adaptation creates a dynamic system that changes over time.")
    ],
    "cast_items": [
        "Explain how brain signals are detected, encoded, and translated into machine commands",
        "Use the model to predict how noise and electrode count affect motor output precision",
        "Evaluate the role of adaptation in improving BCI performance over time"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A BCI patient is learning to control a robotic arm. On Day 1, the arm moves jerkily and often misses the target. By Day 30, the movements are smooth and accurate. Which model component BEST explains this improvement? A) Stimulus Intensity increased B) Noise Level decreased C) Adaptation Level increased D) Electrode Count increased"),
        ("Constructed Response:", "Using your 8-component model, explain why a BCI system with many electrodes in a noisy environment might STILL perform poorly. Then describe how adaptation could partially compensate for the noise problem. Use evidence from at least two simulation scenarios in your answer.")
    ],
    "background_intro": "This lesson builds on the Level 1 Telephone Game by expanding the simple signal-noise-accuracy model into a full brain-computer interface system with eight interacting components. Students now see the complete pathway from sensory stimulus to motor output, including the critical role of adaptation.",
    "background_sections": [
        ("From Signals to Commands", "In the Level 1 lesson, students learned that signals degrade with distance and noise. A real BCI faces this challenge at an extreme scale. The brain produces electrical signals measured in microvolts — millionths of a volt. An EEG headset on the scalp detects these signals through bone and skin, losing enormous amounts of information. Implanted electrodes get closer to the source but require brain surgery. Either way, the raw signal must be amplified, filtered, and decoded before it can control anything."),
        ("The Electrode Revolution", "Early BCIs used just a few electrodes and could only detect very simple brain patterns (like 'thinking left' vs. 'thinking right'). Modern systems use arrays of hundreds or thousands of electrodes, each capturing activity from different groups of neurons. More electrodes means more data points, which means the computer has more information to work with when decoding the user's intentions. The Utah Array, for example, has 96 tiny electrodes on a chip smaller than a penny."),
        ("Neural Noise: The Biggest Challenge", "The brain contains roughly 86 billion neurons, and millions of them are firing at any given moment. When a BCI tries to read the signals controlling arm movement, it must pick out the relevant neural activity from an ocean of unrelated firing. This 'neural noise' is the single biggest obstacle in BCI development. Engineers use sophisticated algorithms, machine learning, and signal processing to filter noise — but it remains an unsolved problem at scale."),
        ("The Power of Adaptation", "One of the most remarkable discoveries in BCI research is that the brain ADAPTS to the interface. Over days and weeks of practice, patients learn to produce cleaner, more distinct neural patterns that are easier for the computer to decode. Simultaneously, the computer's algorithms improve as they gather more training data. This two-way adaptation — biological and artificial intelligence learning to communicate — is what transforms a crude, jerky BCI into a smooth, responsive system. Some patients have described it as learning a new language that only they and their computer speak.")
    ],
    "lever_L": "Students identify Stimulus Intensity, Electrode Count, and Noise Level as external components — conditions that can be set or measured independently. Signal Strength, Encoding Accuracy, Response Time, Motor Output Precision, and Adaptation Level are internal components produced by the system.",
    "lever_E": "Students trace relationships: Stimulus Intensity → Signal Strength (positive), Electrode Count → Encoding Accuracy (positive), Noise Level → Encoding Accuracy (negative) → Motor Output Precision (negative). Signal Strength → Response Time (inverse). Adaptation Level → Encoding Accuracy (positive feedback loop over time).",
    "lever_V": "Students build the full 8-component model with three external inputs feeding five internal components through a network of positive, negative, and inverse relationships.",
    "lever_Ev": "Students run Best Case, Worst Case, Adaptation Test, and Noise Flood scenarios to explore how different combinations of inputs and adaptation affect motor output precision.",
    "lever_R": "Students add Feedback Loop, Algorithm Complexity, or Electrode Invasiveness to explore deeper BCI engineering tradeoffs.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "BCI headset with glowing electrodes", "say": "In Level 1, we learned why signals degrade. Today we build the FULL system — from brain signal to robotic movement. This is the technology that lets paralyzed patients move again.", "do": "Show a brief video of a real BCI patient controlling a robotic arm (many research demonstrations are publicly available). Ask: What do you think is happening between the brain and the arm?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "We are going from 4 components to 8. This is the most complex model in the series — but you already understand the foundation from Level 1.", "do": "Preview new vocabulary: electrode, encoding, adaptation. Connect to Level 1 vocabulary: signal, noise, accuracy. Show how Level 2 EXPANDS on Level 1.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How do scientists decode the brain's electrical language?", "say": "Your brain produces billions of electrical signals every second. Somewhere in that storm of activity is the command to move your finger. How do scientists find THAT signal among billions of others?", "do": "Quick demonstration: have 30 students all talk at the same time. One student says a secret word. Can anyone identify it? That is what a BCI faces — one signal among billions.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps with cascade and feedback emphasis", "say": "This model has something new — ADAPTATION. The system gets better over time. That is a feedback loop, and it changes everything.", "do": "Draw the basic cascade on the board, then add the adaptation arrow looping back. Discuss: How is a feedback loop different from a simple chain?", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "8 component cards for sorting", "say": "Three things we can control, five things the system produces. Notice we have MORE internal components than external — that is what makes this system complex.", "do": "Guide sorting of all 8 components. Key discussion: Why are there 5 internal and only 3 external? (Because the system has many steps between input and output.)", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship diagram with positive, negative, and inverse arrows", "say": "Stimulus Intensity boosts Signal Strength. Electrode Count boosts Encoding Accuracy. But Noise ATTACKS Encoding Accuracy. And here is the twist — Adaptation fights back against noise over time.", "do": "Build the relationship web step by step. Highlight the negative arrow from Noise and the feedback loop from Adaptation. Key moment: the Signal Strength to Response Time inverse relationship — stronger signals are decoded FASTER.", "time": "10 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Four BCI scenarios", "say": "Four tests: the perfect setup, the worst setup, the adaptation experiment, and the noise flood. Predict each one before we run it!", "do": "Run scenarios in order. After each, compare predictions to results. The Adaptation Test is the most revealing — students see the system IMPROVE over simulated time. The Noise Flood shows limits even great hardware cannot overcome.", "time": "12 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key BCI findings and adaptation graph", "say": "The brain and the computer LEARN to work together. That is the most important discovery — adaptation transforms a crude system into a precise one.", "do": "Summarize findings. Draw an adaptation curve showing improvement over trials. Ask: What does this tell us about patience in BCI training?", "time": "4 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Prosthetic hand with barrier and signal codes", "say": "Now build it! A mechanical hand, a coding system, a barrier, and a partner. Can you control a hand using ONLY coded signals? Let us find out.", "do": "Distribute materials. Demonstrate the basic hand mechanism. Groups design their coding system, build the hand, and test through the barrier. Add noise halfway through. Measure improvement with practice.", "time": "12 min"}
    ],
    "sort_reasoning": "Stimulus Intensity, Electrode Count, and Noise Level are external because they are conditions that exist independently and can be set or measured before the system runs — you choose how strong the stimulus is, how many electrodes to use, and you observe how noisy the environment is. Signal Strength, Encoding Accuracy, Response Time, Motor Output Precision, and Adaptation Level are internal because they are PRODUCED by the system — Signal Strength depends on Stimulus Intensity, Encoding Accuracy depends on Electrode Count and Noise, and Motor Output Precision is the final result of the entire chain. Adaptation Level is internal because it emerges from the system's repeated operation over time.",
    "relationships": [
        ("Stimulus Intensity to Signal Strength", "POSITIVE (+)", "A stronger stimulus (louder sound, firmer touch) activates more neurons, producing a larger electrical response. This gives the electrodes a bigger signal to detect — like the difference between hearing someone shout versus whisper."),
        ("Electrode Count to Encoding Accuracy", "POSITIVE (+)", "More electrodes capture neural activity from more locations in the brain, giving the computer more data points to work with. It is like the difference between reading a book through one tiny window versus a large picture window — more viewpoints means a clearer picture."),
        ("Noise Level to Encoding Accuracy", "NEGATIVE (-)", "Neural noise drowns out the target signal, making it harder for the computer to determine what the brain is trying to communicate. High noise forces the encoding algorithm to guess more and decode less — like trying to read a message written in sand during a windstorm."),
        ("Signal Strength to Response Time", "INVERSE (-)", "Stronger signals are detected and decoded faster because they stand out more clearly from background activity. The computer spends less time amplifying and filtering. Weak signals require more processing, creating lag between thought and action."),
        ("Encoding Accuracy to Motor Output Precision", "POSITIVE (+)", "If the computer accurately decodes the brain's intended command, the robotic limb performs the correct movement precisely. Inaccurate encoding means the wrong command is sent — like typing with your eyes closed and hitting the wrong keys."),
        ("Adaptation Level to Encoding Accuracy", "POSITIVE (+)", "Over time, the brain learns to produce cleaner, more distinct signal patterns, and the computer's algorithms improve at recognizing those patterns. This two-way learning progressively improves how accurately the system translates thought into code.")
    ],
    "sim_answers": [
        ("Best Case Scenario", "With high Stimulus Intensity, many electrodes, and low noise, the full pathway performs optimally. Signal Strength is high, giving the encoding algorithm clean data to work with. Encoding Accuracy is high because many electrodes capture detailed neural patterns with minimal interference. Response Time is fast because strong signals are decoded quickly. Motor Output Precision is excellent — the robotic limb moves exactly as intended. This represents the ideal laboratory BCI setup."),
        ("Worst Case Scenario", "With low Stimulus Intensity, few electrodes, and high noise, every component suffers. Signal Strength is weak, making it hard for the sparse electrodes to detect anything meaningful. Encoding Accuracy collapses because the few electrodes cannot capture enough data, and the noise overwhelms what little signal exists. Response Time slows dramatically as the computer struggles to decode. Motor Output Precision is extremely poor — movements are jerky, delayed, and inaccurate. This shows why early BCIs were so limited."),
        ("Adaptation Test Scenario", "Starting with the same Best Case setup, the simulation shows how outputs IMPROVE over multiple trials as Adaptation Level rises. Early trials show good but imperfect performance. Over time, Encoding Accuracy increases as the brain-computer partnership strengthens. Motor Output Precision improves noticeably. Response Time decreases. The improvement curve is steep at first and then plateaus — just like learning any new skill. This demonstrates the most hopeful aspect of BCI technology: it gets better with practice."),
        ("Noise Flood Scenario", "Despite high Stimulus Intensity and many electrodes, extreme noise severely degrades performance. Signal Strength remains high (it depends on stimulus, not noise), but Encoding Accuracy plummets because the noise overwhelms the decoding algorithms. Motor Output Precision drops sharply. Interestingly, the system still performs BETTER than the Worst Case because the strong signal and many electrodes partially compensate — but noise ultimately limits the ceiling. This shows why noise reduction is the highest priority in BCI engineering.")
    ],
    "reflection_exemplars": [
        ("How is Level 2 different from Level 1?", "The Level 1 Telephone Game showed us the basic problem: signals degrade with distance and noise. Level 2 expands that into a complete BCI system with EIGHT components. Now we see the full pathway: stimulus creates a signal, electrodes detect it, the computer encodes it, and a motor responds. We also discover something Level 1 could not show — ADAPTATION. The system improves over time as the brain and computer learn to communicate. Level 1 taught us the problem. Level 2 shows us both the problem AND the solution."),
        ("Why is adaptation so powerful?", "Adaptation is the secret weapon of BCI technology. In the simulation, even when noise was moderate and electrodes were limited, increasing Adaptation Level significantly improved Encoding Accuracy and Motor Output Precision. This happens because the brain is not a passive signal generator — it actively LEARNS to produce clearer patterns that the computer can recognize. Meanwhile, the computer learns the specific patterns of THAT brain. It is like two people developing their own secret language — the more they practice, the better they communicate, even in a noisy room.")
    ],
    "stem_intro": "Present the challenge: Your team will build a mechanical hand from cardboard, straws, and string, then develop a coded signal system to control it from behind a barrier. One partner sends coded signals (like a brain), the other operates the hand (like a BCI decoder). Test accuracy, add noise, and measure whether practice improves performance — just like real BCI adaptation.",
    "stem_concepts": [
        ("Signal Encoding", "You must design a code that maps specific signals to specific finger movements. How many distinct signals do you need? How will your partner know which finger to pull?"),
        ("Noise Interference", "When we add noise (clapping, talking, music), your coded signals become harder to receive. Can your encoding system survive the noise?"),
        ("Adaptation Through Practice", "Record accuracy on Trial 1, Trial 5, and Trial 10. Does your team's performance improve? How does this mirror what happens in real BCI systems?")
    ],
    "stem_eval": [
        ("Expert (4)", "Hand has articulating fingers, signal code is clearly defined, team tests noise and adaptation systematically with recorded data, and connects results to the 8-component model"),
        ("Proficient (3)", "Hand functions with basic finger movement, signal code works, team tests at least noise or adaptation and can explain the connection to the model"),
        ("Developing (2)", "Hand is built and signal code exists but testing is informal and connection to model is vague"),
        ("Beginning (1)", "Hand is incomplete or no systematic testing of noise and adaptation was conducted")
    ],
    "support": [
        "Provide pre-cut hand templates so students focus on the signal system rather than construction",
        "Offer a simple coding framework: 1 clap = thumb, 2 claps = index finger, etc. — students can customize from there",
        "Sentence frames for data recording: 'In Trial __, our accuracy was __% because __'"
    ],
    "extensions": [
        "Research how the Utah Array electrode implant works and compare its signal quality to a scalp-based EEG headset",
        "Design a more complex signal code that can communicate finger COMBINATIONS (like a piano chord) rather than individual fingers",
        "Investigate how machine learning algorithms improve BCI decoding accuracy over time — what does the computer 'learn'?"
    ],
    "cross_curr": [
        ("Math", "Graph adaptation curves: plot accuracy (y-axis) vs. trial number (x-axis) for your team and other teams. Calculate the rate of improvement. Does the curve match a logarithmic growth pattern?"),
        ("ELA", "Write a patient journal entry from the perspective of someone learning to use a BCI for the first time — describe the frustration of early trials and the breakthrough of adaptation."),
        ("History", "Research the history of prosthetic limbs from ancient Egypt to modern BCI-controlled arms. How has the technology changed, and what remained constant about the human desire to restore function?")
    ],
    "misconceptions": [
        ("BCIs can read your thoughts like a mind-reading machine", "Current BCIs do NOT read thoughts, emotions, or memories. They detect specific patterns of electrical activity associated with intended MOVEMENTS — like the neural pattern for 'move right hand up.' Reading a thought like 'I want pizza' is far beyond current technology. The brain's electrical activity is incredibly complex, and we can only decode a tiny fraction of it.", "Demonstrate: have a student think of a number. Can anyone in the class guess it? No — and neither can a BCI. Now have the student imagine squeezing their right hand. A BCI CAN detect that specific motor pattern because it is a localized, repeatable signal."),
        ("More electrodes always means better performance", "While more electrodes generally help, there are diminishing returns. After a certain point, additional electrodes add more noise than signal because they pick up activity from neurons unrelated to the target movement. There is also a practical limit — more electrodes means more data to process, which can SLOW response time. The optimal number depends on the specific application.", "Analogy: listening with two ears is better than one. But would listening with 100 ears be 50 times better? No — you would hear so many overlapping sounds that it would become harder, not easier, to focus on one voice."),
        ("BCI technology will work immediately once connected", "The Adaptation Test scenario clearly shows that BCI performance starts mediocre and improves dramatically with practice. Real BCI patients often spend weeks or months training with their systems before achieving useful control. The brain must learn new signal patterns, and the computer must learn to recognize that specific brain's signals. There is no plug-and-play — it is more like learning to play an instrument.", "Connect to students' experience: remember learning to ride a bicycle? Day 1 was wobbly and slow. After weeks of practice, it became automatic. BCI adaptation works the same way — the brain-computer partnership must be trained through repetition.")
    ],
    "game": {
        "title": "BCI Simon Says",
        "type": "Kinesthetic Communication Game",
        "description": "One student is blindfolded and holds a marker. Their partner stands behind them and can ONLY communicate using clap codes (1 clap = move up, 2 claps = move down, 3 claps = move left, 4 claps = move right, 5 claps = draw). The blindfolded student must draw a simple shape (circle, square, star) using only the coded signals. Round 2: add noise (other students clapping randomly nearby). Round 3: same team tries again — does adaptation improve performance?",
        "materials": ["Blindfolds (1 per pair)", "Large paper sheets on clipboards", "Markers", "Noise-making instruments (clapping hands, rhythm sticks)", "Shape target cards", "Stopwatch for timed rounds", "Accuracy scoring rubric"],
        "learning_connection": "Directly models the BCI pathway: the shape card is the stimulus, the clap code is the electrode signal, the blindfolded student's interpretation is encoding accuracy, the drawing is motor output precision, and the noise round demonstrates neural interference. Repeated rounds demonstrate adaptation."
    },
    "steam_activity": {
        "title": "Prosthetic Hand Design",
        "type": "Engineering Design + Neuroscience",
        "description": "Students build a mechanical hand from cardboard, straws (finger joints), and string (tendons). One partner sits behind a cardboard barrier and pulls strings to control the hand's fingers. The other partner sends coded signals (taps, claps, or written codes passed through a slot) telling which fingers to move. Teams test accuracy in quiet conditions, then with noise (music, clapping), and finally measure improvement over 10 trials to demonstrate adaptation. Data is recorded and graphed.",
        "materials": ["Cardboard sheets for hand base and barrier", "Plastic straws (cut into finger segments)", "String or yarn (tendons)", "Tape and hot glue sticks", "Scissors", "Markers for labeling", "Data recording sheets", "Graph paper for adaptation curves", "Timer/stopwatch", "Noise source (portable speaker or classroom clapping)"],
        "learning_connection": "The mechanical hand is the motor output, the string-pulling partner is the BCI decoder, the signal-sending partner is the brain, and the barrier represents the skull. Students physically experience every component of their 8-component model: stimulus (finger command), signal transmission (coded signal), encoding (interpreting the code), motor output (pulling the right string), and adaptation (improving with practice)."
    }
}

L2_05 = {
    "id": "NE-L2-05",
    "title": "Restoring Ecosystems — Data-Driven Recovery",
    "subtitle": "Using Science to Heal Damaged Landscapes",
    "ngss": "HS-LS2-6, HS-LS2-7, HS-ESS3-3, HS-ESS3-4, HS-ETS1-4",
    "ngss_desc": "Evaluate claims, evidence, and reasoning that the complex interactions in ecosystems maintain relatively consistent numbers and types of organisms in stable conditions, but changing conditions may result in a new ecosystem. Design, evaluate, and refine a solution for reducing the impacts of human activities on the environment and biodiversity. Create a computational simulation of a natural phenomenon. Evaluate or refine a technological solution that reduces impacts of human activities on natural systems. Use a computer simulation to model the impact of proposed solutions to a complex real-world problem.",
    "big_question": "How do scientists know when a damaged ecosystem has healed enough to sustain itself — and what happens if we stop investing too early?",
    "objectives": [
        "Explain how ecosystem restoration uses keystone species reintroduction and targeted investment to rebuild damaged landscapes",
        "Model a 9-component system showing how restoration inputs, biotic recovery, and abiotic conditions interact to reach a self-sustaining threshold",
        "Identify reinforcing feedback loops between habitat quality and native species diversity",
        "Predict what happens when restoration funding is withdrawn before the self-sustaining threshold is reached",
        "Evaluate the role of tipping points in ecosystem recovery using simulation data"
    ],
    "vocabulary": [
        ("Ecosystem Restoration", "The process of assisting the recovery of a degraded, damaged, or destroyed ecosystem through active human intervention"),
        ("Tipping Point", "A critical threshold where a small additional change causes a large, often irreversible shift in system behavior"),
        ("Self-Sustaining Threshold", "The point at which an ecosystem can maintain itself without ongoing human investment or intervention"),
        ("Invasive Species", "Non-native organisms that spread aggressively and outcompete native species for resources"),
        ("Reinforcing Loop", "A feedback loop where the output amplifies the input, accelerating change in the same direction — either growth or decline")
    ],
    "components": [
        ("Restoration Investment", "Level of funding, labor, and resources dedicated to ecosystem recovery — includes planting, monitoring, and habitat engineering", True),
        ("Keystone Species Reintroduced", "Number of keystone organisms (such as beavers) actively released into the restoration site", True),
        ("Human Development Pressure", "Intensity of nearby construction, agriculture, pollution, and land-use change that degrades habitat", True),
        ("Habitat Quality", "Overall health of the physical environment — water availability, soil condition, shelter, nesting sites, and vegetation cover", False),
        ("Native Species Diversity", "The number and abundance of native plant and animal species successfully established in the recovering ecosystem", False),
        ("Invasive Species Pressure", "The dominance of non-native species competing for space, light, water, and nutrients against native species", False),
        ("Water Quality", "Health of the aquatic system — dissolved oxygen, sediment load, nutrient balance, and pollutant levels", False),
        ("Recovery Rate", "The speed at which the ecosystem is rebuilding toward full function — driven by all internal components working together", False),
        ("Self-Sustaining Threshold", "A composite measure of whether the ecosystem has reached the tipping point where it can maintain itself without continued human input", False)
    ],
    "think_about_it": "Trace the chain: Restoration Investment and Keystone Reintroduction boost Habitat Quality. Habitat Quality boosts Native Species Diversity — and Native Diversity feeds BACK into Habitat Quality. What kind of loop is that? What happens to Invasive Species when Habitat Quality rises? When do all these signals combine to cross the Self-Sustaining Threshold?",
    "scenarios": [
        ("Full Investment", "Restoration Investment high, Keystone Species Reintroduced high, Human Development Pressure low — observe all nine components over time"),
        ("Underfunded Restoration", "Restoration Investment low, Keystone Species Reintroduced moderate, Human Development Pressure low — can a cheap approach still work?"),
        ("Development Pressure", "Restoration Investment high, Keystone Species Reintroduced high, Human Development Pressure high — can investment overcome ongoing damage?"),
        ("Early Withdrawal", "Start with Full Investment settings, then drop Restoration Investment to zero at mid-simulation — does the ecosystem sustain itself or collapse?")
    ],
    "sim_scenarios": [
        ("Full Investment", "Maximum resources, keystone reintroduction, minimal pressure", "What do you predict will happen to Recovery Rate and Self-Sustaining Threshold when all conditions are optimal?"),
        ("Underfunded Restoration", "Low funding, some keystone species, no development pressure", "Can the reinforcing feedback loop between habitat quality and native diversity compensate for low investment?"),
        ("Development Pressure", "Full investment against active habitat destruction", "When investment and destruction happen simultaneously, which force wins — and does it depend on timing?"),
        ("Early Withdrawal", "Funding cut before threshold reached", "What happens to all internal components if we stop investing before the ecosystem can sustain itself?")
    ],
    "discoveries": [
        "Ecosystem restoration is not linear — the reinforcing loop between Habitat Quality and Native Species Diversity creates accelerating recovery once it gets going",
        "Invasive Species Pressure drops as Habitat Quality rises — healthy native ecosystems naturally resist invasion",
        "Keystone species reintroduction is a force multiplier — beavers improve Water Quality AND Habitat Quality simultaneously",
        "Human Development Pressure can overwhelm even well-funded restoration if it is severe enough",
        "The Self-Sustaining Threshold is a real tipping point — ecosystems that cross it continue recovering even without funding, but ecosystems that do not cross it collapse when funding stops",
        "Early withdrawal of funding is the most common cause of restoration failure — timing matters as much as money"
    ],
    "answer": "Scientists determine when an ecosystem has healed by tracking multiple indicators — habitat quality, native species diversity, water quality, and invasive species pressure — and looking for the self-sustaining threshold: the tipping point where the reinforcing feedback loop between habitat and biodiversity is strong enough to maintain itself. Keystone species like beavers accelerate this process by simultaneously improving water quality and habitat structure. But the critical lesson is timing: if investment stops BEFORE the threshold is reached, the ecosystem cannot maintain itself and collapses back. Data-driven restoration means tracking these indicators in real time so we know exactly when it is safe to step back — and when it is too early.",
    "stem_title": "Restoration Proposal Pitch",
    "stem_mission": "Select a real degraded ecosystem in your state, research its current condition, and design a data-driven restoration plan that you pitch to a panel of judges acting as a state conservation board.",
    "stem_scenario": "Your state's Department of Natural Resources has a limited budget and must choose which degraded ecosystem to restore first. Your team will research a real site, use model data to design a restoration plan with a timeline and budget, and pitch it to a panel. The most compelling, evidence-based pitch wins funding.",
    "stem_questions": [
        "What is the current state of your chosen ecosystem — which components are most degraded?",
        "Which keystone species, if any, could accelerate recovery at your site?",
        "How long does your model predict it will take to reach the self-sustaining threshold?",
        "What is the risk if funding is cut 2 years early? 5 years early?"
    ],
    "stem_design_qs": [
        "What data sources did you use to assess the current condition of your ecosystem?",
        "How will you allocate your restoration budget across different interventions (planting, species reintroduction, invasive removal, monitoring)?",
        "What metrics will you track to know when the self-sustaining threshold has been reached?",
        "How does your plan account for ongoing human development pressure near the site?",
        "What is your contingency plan if the ecosystem is not recovering on schedule?"
    ],
    "career": "Restoration Ecologists design and manage projects that return degraded ecosystems to healthy function. They work with government agencies, conservation nonprofits, and engineering firms to plan reintroductions, monitor recovery, and manage invasive species. They earn $60,000–$100,000/year.",
    "images": {
        "cover": ("cover-restoring-ecosystems.png", "A stunning photorealistic aerial view showing ecosystem restoration in progress — left side shows degraded brown landscape with eroded banks and sparse vegetation, right side shows lush green wetland with beaver ponds, wildflowers, and birds in flight, dramatic transition line between the two halves, nature documentary drone photography, golden hour light"),
        "landscape": ("landscape-restoring-eco.png", "A photorealistic image of diverse 10th-12th grade students (15-18 years old) conducting field research along a restored wetland, collecting water samples and recording data on tablets, Black male student leading the data collection while Latin American and Asian/AAPI students take measurements, modern field gear, natural outdoor light, editorial photo quality"),
        "modeling": ("modeling-restoring-eco.png", "A photorealistic image of diverse 10th-12th grade students working on laptops building a 9-component ecosystem restoration model, Latin American female student pointing at a feedback loop diagram on her screen while explaining to the group, modern science classroom with restoration ecology posters and maps on the walls"),
        "discussion": ("discussion-restoring-eco.png", "A photorealistic image of a Black female teacher leading a data analysis discussion with diverse 10th-12th graders, smartboard showing before-and-after satellite imagery and recovery graphs of a real restoration site, students engaged with notebooks open, bright modern classroom with natural light"),
        "stem": ("stem-restoring-eco.png", "A photorealistic image of diverse 10th-12th grade students presenting a restoration proposal to a panel of teachers acting as judges, Asian/AAPI male student at the front with a poster showing budget allocation and timeline charts, teammates behind him, professional pitch atmosphere with confidence and preparation visible")
    },
    "pre_assessment": [
        "In Level 1, you modeled how removing a keystone species collapses an ecosystem. Now think about the reverse: what does it take to REBUILD one?",
        "Why do you think some ecosystem restoration projects succeed and others fail?",
        "What data would you need to determine whether a damaged ecosystem is recovering?",
        "What do you think 'self-sustaining' means in the context of an ecosystem — when can scientists stop actively managing it?"
    ],
    "extend_components": [
        ("Climate Variability", "Year-to-year changes in temperature and precipitation patterns that can accelerate or slow recovery"),
        ("Community Engagement", "Level of local public support and volunteer involvement in restoration — affects long-term protection"),
        ("Soil Microbiome Health", "The diversity and activity of soil fungi, bacteria, and invertebrates that drive nutrient cycling and plant establishment")
    ],
    "reflections": [
        "How does the reinforcing loop between Habitat Quality and Native Species Diversity create a tipping point?",
        "Why is the Early Withdrawal scenario the most important one for real-world conservation planners?",
        "Compare the Full Investment and Underfunded scenarios — what does this tell you about the relationship between money and recovery speed?",
        "How does keystone species reintroduction act as a 'force multiplier' in restoration?",
        "If you were advising a state conservation board, what single metric would you track to decide when it is safe to reduce funding — and why?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a 9-component computational model of ecosystem restoration with reinforcing feedback loops, tipping points, and competing pressures to evaluate restoration strategies."),
        ("Disciplinary Core Idea", "LS2.C Ecosystem Dynamics, Functioning, and Resilience", "Ecosystems can recover from disturbance through restoration, but recovery depends on the strength of species interactions, the presence of keystone species, and whether the system crosses a self-sustaining threshold."),
        ("Crosscutting Concept", "Stability and Change", "The self-sustaining threshold represents a critical transition point — small changes near the threshold produce large shifts in system behavior, demonstrating how stability and change are interconnected in complex systems.")
    ],
    "cast_items": [
        "Explain how restoration investment and keystone reintroduction interact to rebuild ecosystem function",
        "Use the model to identify the self-sustaining threshold and explain what happens on either side of it",
        "Evaluate the consequences of early funding withdrawal using simulation data as evidence"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A restoration team reintroduces beavers to a degraded watershed and monitors recovery for 5 years. Native species diversity is increasing and invasive species are declining, but the self-sustaining threshold has not yet been reached. What should the team recommend? A) Withdraw funding — the ecosystem is improving on its own B) Continue funding — stopping now risks collapse C) Double the number of beavers to speed up the timeline D) Remove all invasive species manually instead of waiting"),
        ("Constructed Response:", "Using your 9-component model, explain why the Early Withdrawal scenario produces different outcomes depending on WHEN funding is stopped. Include the concepts of reinforcing feedback loop and self-sustaining threshold in your answer, and use specific simulation data as evidence.")
    ],
    "background_intro": "This lesson builds on Level 1's keystone species model by expanding from a 4-component removal-and-recovery system to a 9-component restoration system with reinforcing feedback loops, competing pressures, and tipping points. Students now experience the full complexity of real-world ecosystem restoration decisions.",
    "background_sections": [
        ("The Science of Ecosystem Restoration", "Ecosystem restoration is one of the most important applied sciences of the 21st century. The UN declared 2021-2030 the Decade on Ecosystem Restoration, recognizing that reversing environmental degradation is essential for climate, biodiversity, and human well-being. Restoration ecology combines biology, hydrology, soil science, and data analytics to design recovery plans for damaged landscapes."),
        ("Beaver Reintroduction as Restoration Strategy", "Across North America and Europe, scientists are reintroducing beavers as a cost-effective restoration strategy. In degraded watersheds, beavers rebuild dams, raise water tables, filter sediment, create wetlands, and dramatically increase biodiversity — all without ongoing human labor. Studies in Washington, Oregon, Utah, and the UK show that beaver reintroduction can restore watersheds at a fraction of the cost of engineered solutions. A single beaver family can restore 5-15 acres of wetland habitat."),
        ("Tipping Points and Self-Sustaining Ecosystems", "Ecological research shows that recovering ecosystems exhibit tipping points — thresholds beyond which the system switches from requiring active management to maintaining itself. Before the tipping point, removing support causes collapse. After the tipping point, the reinforcing feedback loops between species diversity, habitat quality, and water health are strong enough to sustain the ecosystem independently. Identifying this threshold is one of the hardest problems in restoration ecology."),
        ("Why Restoration Projects Fail", "The most common cause of restoration failure is premature withdrawal of support. Political cycles (4-year election cycles) are shorter than ecological recovery timelines (10-30 years). When funding is cut before the self-sustaining threshold is reached, ecosystems collapse back to degraded states, wasting all prior investment. Data-driven monitoring allows scientists to identify exactly where a system sits relative to the threshold, providing evidence-based arguments for continued support."),
        ("Invasive Species and Recovery", "Invasive species are one of the biggest obstacles to restoration. In degraded ecosystems, invasive plants and animals exploit the open niches left by native species decline. As restoration progresses and native species reclaim their niches, invasive pressure naturally decreases — but only if native recovery is strong enough. If restoration is underfunded, invasive species can lock the ecosystem into a degraded state permanently.")
    ],
    "lever_L": "Students identify Restoration Investment, Keystone Species Reintroduced, and Human Development Pressure as external components — conditions set by human decisions. Habitat Quality, Native Species Diversity, Invasive Species Pressure, Water Quality, Recovery Rate, and Self-Sustaining Threshold are internal components that change based on the interactions between externals and each other.",
    "lever_E": "Students trace the key relationships: Restoration Investment positively affects Habitat Quality. Keystone Species Reintroduced positively affects both Habitat Quality and Water Quality. Habitat Quality positively affects Native Species Diversity (and Native Species Diversity feeds BACK into Habitat Quality — reinforcing loop). Habitat Quality negatively affects Invasive Species Pressure. Human Development Pressure negatively affects Habitat Quality. All internal components feed into Recovery Rate and Self-Sustaining Threshold.",
    "lever_V": "Students build the full 9-component model with three external inputs, six internal components, a reinforcing feedback loop, and a threshold output that aggregates system health.",
    "lever_Ev": "Students run four scenarios — Full Investment, Underfunded, Development Pressure, and Early Withdrawal — to test how different restoration strategies and pressures affect whether the system crosses the self-sustaining threshold.",
    "lever_R": "Students add Climate Variability, Community Engagement, or Soil Microbiome Health to explore how additional real-world factors complicate restoration timelines and outcomes.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Split aerial image — degraded vs. restored landscape", "say": "In Level 1, we watched an ecosystem COLLAPSE when we removed the keystone species. Today we reverse the question: how do we put it back TOGETHER — and how do we know when it can stand on its own?", "do": "Show before-and-after satellite imagery of a real beaver reintroduction site (e.g., Bridge Creek, Oregon). Ask: What differences do you see?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Nine components today — the biggest model in our series. We are adding investment, invasive species, water quality, and the concept of a self-sustaining threshold.", "do": "Pre-teach 'tipping point' and 'self-sustaining threshold' with a physical analogy: push a ball up a hill — if you stop pushing before the top, it rolls back. If you push it past the top, it rolls forward on its own.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How do we know when a damaged ecosystem has healed enough?", "say": "Imagine you are in charge of a restoration project with a limited budget. When is it safe to stop spending — and what happens if you guess wrong?", "do": "Think-pair-share: Students discuss what they think 'self-sustaining' means. How would you measure it? What data would convince you?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps with feedback loop and threshold emphasis", "say": "This model has two new features: a reinforcing feedback LOOP and a THRESHOLD — a tipping point where the system shifts from needing help to helping itself.", "do": "Draw the reinforcing loop (Habitat Quality and Native Diversity) on the board. Ask: What happens when this loop is spinning fast? What if it stalls?", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "9 component cards for sorting", "say": "Three things humans DECIDE, six things the ecosystem PRODUCES. But watch out — one of those externals is working AGAINST recovery.", "do": "Guide component sorting. Key discussion: Human Development Pressure is external but NEGATIVE. Unlike the other two externals, more of this is BAD. Why did we include it?", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship web with feedback loop and threshold", "say": "This is where it gets real. Restoration and Keystone Reintroduction push Habitat Quality UP. Human Development pushes it DOWN. Habitat Quality and Native Diversity reinforce each other. And everything flows into the Self-Sustaining Threshold.", "do": "Build the relationship web step by step. Key moment: draw the reinforcing loop between Habitat Quality and Native Diversity. Ask: What kind of loop is this? What happens when it activates?", "time": "10 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Four restoration scenarios", "say": "Four strategies, four outcomes. Full investment, underfunded, fighting development pressure, and the critical one — what happens when we stop too early?", "do": "Run all four scenarios. Require written predictions BEFORE each run. The Early Withdrawal scenario is the climax — run it last. Watch the Self-Sustaining Threshold carefully.", "time": "12 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings with threshold analysis", "say": "The tipping point is real. Cross it and the ecosystem takes over. Fall short and everything you invested is lost. This is why data-driven monitoring is not optional — it is essential.", "do": "Summarize findings. Discuss: How does this change how you think about funding timelines? Why is the Early Withdrawal scenario the most important lesson for policymakers?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Restoration Proposal Pitch", "say": "Now you are the restoration ecologists. Pick a real degraded ecosystem in our state, design a recovery plan, and pitch it to our conservation board.", "do": "Form teams, assign research roles, distribute pitch guidelines. Teams research a real degraded site, apply model logic to design a plan with budget and timeline, and prepare a 5-minute pitch.", "time": "12 min"}
    ],
    "sort_reasoning": "Restoration Investment, Keystone Species Reintroduced, and Human Development Pressure are external because they are determined by human decisions — conservation agencies control funding levels, species reintroduction numbers, and zoning policy. Habitat Quality, Native Species Diversity, Invasive Species Pressure, Water Quality, Recovery Rate, and Self-Sustaining Threshold are internal because they are OUTCOMES of the system's dynamics — they emerge from the interactions between external inputs and internal feedback loops. No one sets Habitat Quality directly; it results from investment, keystone activity, and development pressure working together.",
    "relationships": [
        ("Restoration Investment to Habitat Quality", "POSITIVE (+)", "Higher investment funds planting native vegetation, removing invasive species, engineering water features, and monitoring progress — all of which directly improve habitat structure and function."),
        ("Keystone Species Reintroduced to Habitat Quality", "POSITIVE (+)", "Reintroduced keystone species like beavers physically reshape the landscape — building dams, creating ponds, raising water tables, and generating complex habitat structure that no amount of human engineering can replicate as efficiently."),
        ("Keystone Species Reintroduced to Water Quality", "POSITIVE (+)", "Beaver dams slow water flow, allowing sediment to settle, filtering pollutants, increasing dissolved oxygen through aeration, and raising the water table — all measurable improvements in water quality."),
        ("Human Development Pressure to Habitat Quality", "NEGATIVE (-)", "Construction, agriculture, roads, and pollution degrade habitat by fragmenting landscapes, introducing pollutants, reducing water availability, and disturbing wildlife. This force works AGAINST restoration investment."),
        ("Habitat Quality to Native Species Diversity", "POSITIVE (+)", "Higher habitat quality provides more niches, better food sources, more nesting sites, and cleaner water — all of which support a greater variety of native species colonizing the recovering ecosystem."),
        ("Native Species Diversity to Habitat Quality", "POSITIVE (+) — REINFORCING FEEDBACK LOOP", "More native species improve habitat through pollination, seed dispersal, nutrient cycling, soil stabilization, and pest control. Biodiversity itself is a habitat-building force. This creates a reinforcing loop that ACCELERATES recovery once it gets going."),
        ("Habitat Quality to Invasive Species Pressure", "NEGATIVE (-)", "As habitat quality improves and native species fill ecological niches, invasive species face increasing competition. Healthy native ecosystems naturally resist invasion through competitive exclusion."),
        ("Habitat Quality, Native Species Diversity, Invasive Species Pressure, and Water Quality to Recovery Rate", "COMPOSITE", "Recovery Rate is driven by the combined health of all internal biotic and abiotic indicators. High Habitat Quality, high Native Diversity, low Invasive Pressure, and high Water Quality all accelerate recovery."),
        ("Recovery Rate to Self-Sustaining Threshold", "POSITIVE (+) with THRESHOLD BEHAVIOR", "As Recovery Rate accumulates over time, the system approaches the Self-Sustaining Threshold — the tipping point where internal feedback loops are strong enough to maintain the ecosystem without external investment. Below the threshold, the system collapses without support. Above it, the system sustains itself.")
    ],
    "sim_answers": [
        ("Full Investment Scenario", "With high Restoration Investment, high Keystone Reintroduction, and low Development Pressure, Habitat Quality rises quickly. Native Species Diversity follows, activating the reinforcing feedback loop. Invasive Species Pressure declines as natives reclaim niches. Water Quality improves as beaver activity filters and manages water flow. Recovery Rate accelerates, and the Self-Sustaining Threshold is crossed within the simulation period. This represents the ideal outcome — the ecosystem reaches independence."),
        ("Underfunded Scenario", "With low Restoration Investment, recovery is slow. Habitat Quality improves only modestly, and the reinforcing loop between Habitat Quality and Native Diversity barely activates. Invasive species remain competitive because natives cannot establish strongly enough to exclude them. Recovery Rate stays low, and the Self-Sustaining Threshold is NOT reached within the simulation period. The ecosystem remains dependent on continued (inadequate) support — spending money without achieving independence."),
        ("Development Pressure Scenario", "With high investment AND high Development Pressure, the two forces partially cancel each other. Habitat Quality improves but is constantly dragged down by ongoing degradation. The reinforcing loop activates weakly. Whether the threshold is reached depends on the RATIO of investment to pressure — if development is severe enough, even maximum investment cannot overcome it. This demonstrates that restoration must be paired with land-use policy."),
        ("Early Withdrawal Scenario", "This is the critical test. When funding is high and conditions are optimal, the system tracks toward the threshold. If funding is cut BEFORE the threshold is reached, the reinforcing loop is not yet strong enough to sustain itself. Habitat Quality begins declining, Native Diversity drops, Invasive Pressure rebounds, Water Quality deteriorates, and Recovery Rate reverses. All prior investment is lost as the ecosystem slides back toward degradation. If funding continues until AFTER the threshold, the system sustains itself. The difference between success and failure is timing.")
    ],
    "reflection_exemplars": [
        ("Why is the reinforcing loop between Habitat Quality and Native Diversity so important?", "The reinforcing loop is what creates the possibility of self-sustaining recovery. Without it, the ecosystem would need permanent human support — we would have to keep investing forever. But because native species IMPROVE habitat quality (through pollination, seed dispersal, soil stabilization, nutrient cycling), and improved habitat supports MORE native species, the system can build on itself. Once this loop is spinning fast enough, it generates its own momentum. That is the self-sustaining threshold — the point where the loop is strong enough to maintain the ecosystem without external help. Before that point, the loop is too weak and the system collapses without support."),
        ("Why is the Early Withdrawal scenario the most important for policymakers?", "The Early Withdrawal scenario demonstrates the most expensive mistake in conservation: spending millions on restoration and then cutting funding right before the ecosystem can sustain itself. All that investment is wasted because the system cannot maintain itself yet. It is like climbing 90% of the way up a mountain and then sliding all the way back to the bottom. The model shows that there is a SPECIFIC threshold — not a vague feeling of 'good enough' — that data can identify. This is why data-driven monitoring is essential: it tells policymakers EXACTLY when it is safe to reduce funding. Without data, they are guessing, and guessing wrong wastes everything.")
    ],
    "stem_intro": "Present the challenge: Your state has three degraded ecosystems competing for limited restoration funding. Each team selects one real site in your state, researches its current condition using publicly available data (satellite imagery, water quality reports, species surveys), and designs a restoration plan using model logic. Teams pitch their plan to a panel of teachers acting as the State Conservation Board. The most compelling, data-supported pitch wins the 'funding.' Pitches must include: site assessment, restoration strategy, budget allocation, keystone species plan, timeline to self-sustaining threshold, and risk analysis for early withdrawal.",
    "stem_concepts": [
        ("Data-Driven Decision Making", "Restoration plans must be based on measurable indicators — not guesswork. Track habitat quality, species counts, water quality, and invasive coverage to know where you are relative to the threshold."),
        ("Budget Allocation Tradeoffs", "With a fixed budget, every dollar spent on planting is a dollar NOT spent on invasive removal or monitoring. Your model helps you decide where investment has the highest return."),
        ("Threshold Thinking", "The self-sustaining threshold changes your strategy. The goal is not maximum investment forever — it is reaching the tipping point as efficiently as possible, then allowing the reinforcing loop to take over.")
    ],
    "stem_eval": [
        ("Expert (4)", "Proposal includes real site data, justified budget allocation, keystone species plan, threshold timeline with model evidence, risk analysis for early withdrawal, and compelling presentation with data visualizations"),
        ("Proficient (3)", "Proposal includes a real site, reasonable restoration strategy, budget with some justification, and references to model data for key decisions"),
        ("Developing (2)", "Proposal identifies a site and a general restoration approach but lacks data-driven justification or threshold analysis"),
        ("Beginning (1)", "Proposal is incomplete or does not connect restoration decisions to model evidence")
    ],
    "support": [
        "Provide a list of degraded ecosystems in the state with basic data (location, type, key issues) so students can choose quickly",
        "Pre-made budget template with categories (planting, invasive removal, species reintroduction, monitoring, community engagement)",
        "Sentence frames for pitch: 'Our model predicts that __ will reach the self-sustaining threshold in __ years because __'",
        "Threshold checklist: list of indicators and target values that signal the ecosystem is self-sustaining"
    ],
    "extensions": [
        "Research the UN Decade on Ecosystem Restoration (2021-2030) and evaluate one featured project using your model framework",
        "Calculate the cost-per-acre of beaver-assisted restoration vs. traditional engineered restoration using published data",
        "Design a 10-year monitoring dashboard that tracks all nine model components for a real restoration site",
        "Write a policy brief for your state legislature arguing for minimum restoration funding timelines based on threshold science"
    ],
    "cross_curr": [
        ("Math", "Calculate the return on investment (ROI) for restoration: compare the cost of restoration to the economic value of ecosystem services (water filtration, flood control, carbon storage) the recovered ecosystem provides. Graph cumulative cost vs. cumulative benefit over a 20-year timeline."),
        ("ELA", "Write a grant proposal requesting 10 years of funding for your restoration site. Include problem statement, proposed solution, budget, timeline, and evidence from your model simulations. Address the risk of early withdrawal explicitly."),
        ("Social Studies", "Research the political history of a real restoration project that was defunded early. Who made the decision? What were the consequences? How could data-driven threshold monitoring have changed the outcome?")
    ],
    "misconceptions": [
        ("Ecosystems recover naturally if you just leave them alone", "Some mildly degraded ecosystems can self-recover, but severely degraded systems often cannot. When keystone species are gone, invasive species dominate, and soil and water systems are damaged, the ecosystem is trapped in a degraded state. Active restoration — reintroducing species, removing invasives, engineering water features — is required to push the system past the tipping point where natural recovery processes can take over.", "Compare two scenarios: one where you just stop the damage vs. one where you actively restore. The model shows that passive approaches take dramatically longer — or may never cross the threshold at all."),
        ("More money always means better restoration", "The Underfunded scenario shows that inadequate funding fails, but the Development Pressure scenario shows that even MAXIMUM funding can fail if opposing forces are strong enough. Money is necessary but not sufficient — the relationship between investment and development pressure matters more than the raw dollar amount. Smart allocation beats bigger budgets.", "Ask: Would you rather have a large budget with heavy development pressure, or a moderate budget with no development pressure? Run both in the model and compare."),
        ("Once you see improvement, the ecosystem is saved", "Early improvement does NOT mean the self-sustaining threshold has been reached. The Early Withdrawal scenario demonstrates this clearly: the ecosystem can look like it is recovering — rising habitat quality, increasing species diversity — but if the reinforcing feedback loop is not yet strong enough to sustain itself, cutting support causes collapse. Improvement is a sign of PROGRESS, not completion. Only data showing that internal feedback loops are self-maintaining indicates true recovery.", "Analogy: A patient in the hospital may feel better after a few days of treatment, but leaving the hospital too early can be dangerous. The doctor uses data (vital signs, blood tests) to determine when the patient can sustain their own recovery. Ecosystems are the same — feeling better is not the same as being healed."),
        ("Invasive species must be completely eliminated for restoration to succeed", "Complete elimination of invasive species is rarely possible or necessary. What matters is reducing invasive pressure enough that native species can outcompete them. As Habitat Quality improves and Native Diversity increases, the ecosystem naturally resists invasion through competitive exclusion. The goal is tipping the balance, not achieving zero invasives.", "Run the model: watch how Invasive Species Pressure declines as Habitat Quality and Native Diversity rise. The ecosystem manages the invasives itself once it is healthy enough.")
    ],
    "game": {
        "title": "Restoration Budget Board Game",
        "type": "Strategy Board Game",
        "description": "Teams start with a fixed restoration budget (play money) and a degraded ecosystem game board with nine component tracks. Each round, teams allocate budget tokens across interventions (planting, keystone reintroduction, invasive removal, water engineering, monitoring). They roll event dice that introduce random challenges (drought, political pressure, invasive outbreak, volunteer surge). Component tracks move up or down based on allocations and events. The reinforcing loop between Habitat Quality and Native Diversity is built into the rules — when both are above 5, they boost each other automatically. First team to push Self-Sustaining Threshold past the red line wins. If a team runs out of budget before crossing the threshold, their ecosystem collapses.",
        "materials": ["Game boards with nine component tracks (1 per team)", "Budget tokens (play money, 100 units per team)", "Allocation cards for each intervention type", "Event dice with challenge and bonus faces", "Component track markers", "Threshold line overlay", "Round tracker", "Rules reference card"],
        "learning_connection": "Reinforces every model concept through strategic gameplay: budget allocation forces tradeoff thinking, random events introduce uncertainty, the reinforcing loop rewards building Habitat Quality and Native Diversity together, and the threshold creates urgency — spend wisely or run out of money before the ecosystem can sustain itself."
    },
    "steam_activity": {
        "title": "Restoration Proposal Pitch",
        "type": "Research + Public Speaking + Data Visualization",
        "description": "Student teams select a real degraded ecosystem in their state (river, wetland, forest, grassland) and develop a comprehensive restoration proposal. They research the site using publicly available data (satellite imagery, government reports, species databases), design a restoration strategy using model logic, create data visualizations showing projected recovery timelines, and deliver a 5-minute pitch to a panel of teachers acting as a state conservation board. Teams must address: current site condition, proposed interventions, budget allocation, keystone species plan, timeline to self-sustaining threshold, and risk analysis for early funding withdrawal.",
        "materials": ["Laptops for research", "Poster paper or digital presentation tools", "Graphing software or colored pencils for data visualizations", "State ecosystem database access or printed reference sheets", "Budget worksheet templates", "Pitch evaluation rubrics for judges", "Timer for 5-minute presentations"],
        "learning_connection": "Students apply every concept from the 9-component model to a real-world context — translating simulation data into actionable restoration strategy and communicating it persuasively. The pitch format develops scientific communication skills essential for careers in conservation and environmental policy."
    }
}

L2_06 = {
    "id": "NE-L2-06",
    "title": "AI, Robotics & Ethics — Modeling Hard Choices",
    "subtitle": "When Technology Meets Nature, Who Decides What's Right?",
    "ngss": "HS-ETS1-1, HS-ETS1-3, HS-LS2-7, HS-LS4-6",
    "ngss_desc": "Analyze a major global challenge to specify qualitative and quantitative criteria and constraints for solutions that account for societal needs and wants. Evaluate a solution to a complex real-world problem based on prioritized criteria and trade-offs that account for a range of constraints. Design, evaluate, and refine a solution for reducing the impacts of human activities on the environment and biodiversity. Create or revise a simulation to test a solution to mitigate adverse impacts of human activity on biodiversity.",
    "big_question": "When AI and robots are used to protect wildlife, who decides what is ethical — the engineers, the communities, the government, or the algorithms themselves?",
    "objectives": [
        "Explain how AI and robotics create ethical tensions between capability, transparency, autonomy, and regulation in conservation",
        "Model a 9-component system showing how technology decisions cascade into ecological, social, and ethical outcomes",
        "Evaluate competing conservation technology strategies by analyzing tradeoffs across multiple ethical dimensions",
        "Design and defend an ethical framework for deploying AI-driven conservation technology"
    ],
    "vocabulary": [
        ("Algorithmic Transparency", "How clearly a technology's decision-making process can be understood and explained to the public"),
        ("Autonomous System", "A technology that makes decisions and takes action without direct human control"),
        ("Ethical Justification", "The reasoning that explains WHY a particular action is morally acceptable given the circumstances"),
        ("Animal Autonomy", "The freedom of wild animals to behave naturally without technological interference or control"),
        ("Regulatory Framework", "The set of laws, rules, and guidelines that govern how a technology can be used")
    ],
    "components": [
        ("Technology Capability Level", "How powerful and advanced the AI or robotic system is — from basic monitoring to fully autonomous intervention", True),
        ("Transparency Level", "How openly the technology's methods, data, and decision-making processes are shared with the public", True),
        ("Ecological Crisis Severity", "How urgent the environmental threat is — from minor habitat concern to imminent species extinction", True),
        ("Regulation Strictness", "How tightly government rules constrain what the technology is allowed to do", True),
        ("Ecological Benefit", "The measurable improvement to ecosystems and species resulting from the technology deployment", False),
        ("Unintended Consequences", "Unexpected negative outcomes that emerge from deploying the technology in complex ecosystems", False),
        ("Animal Autonomy Impact", "How much the technology disrupts natural animal behavior, movement, and decision-making", False),
        ("Public Trust", "The degree to which communities, scientists, and the public believe the technology is being used responsibly", False),
        ("Ethical Justification Score", "An overall measure of whether deploying the technology is morally defensible given all factors", False)
    ],
    "think_about_it": "If you increase Technology Capability, Ecological Benefit goes UP — but so do Unintended Consequences. Transparency builds Public Trust, but Unintended Consequences destroy it. When does a crisis become severe enough to justify risks that would normally be unacceptable?",
    "scenarios": [
        ("Transparent and Regulated", "Technology Capability medium, Transparency high, Crisis Severity moderate, Regulation strict — observe all outputs"),
        ("Unregulated Cowboy", "Technology Capability high, Transparency low, Crisis Severity low, Regulation none — what happens to trust and ethics?"),
        ("Emergency Override", "Technology Capability maximum, Transparency medium, Crisis Severity extreme, Regulation relaxed — does the emergency justify the approach?"),
        ("Surveillance State", "Technology Capability maximum, Transparency low, Crisis Severity moderate, Regulation strict — what happens when power meets secrecy?")
    ],
    "sim_scenarios": [
        ("Transparent and Regulated", "Moderate tech, open methods, strict rules", "What do you predict — does transparency combined with regulation produce high ethical justification?"),
        ("Unregulated Cowboy", "High tech, low transparency, no rules", "What happens to public trust when powerful technology operates in the shadows?"),
        ("Emergency Override", "Maximum tech, extreme crisis, relaxed rules", "When a species is days from extinction, does the emergency change what is ethically acceptable?"),
        ("Surveillance State", "Maximum tech, low transparency, strict rules", "Can strict regulation compensate for a lack of transparency — or do you need both?")
    ],
    "discoveries": [
        "Technology capability is a double-edged sword — more powerful systems produce greater ecological benefits AND greater unintended consequences simultaneously",
        "Transparency is the single strongest driver of public trust — without it, even beneficial technology faces public opposition",
        "Unintended consequences erode public trust through a feedback loop: low trust leads to stricter regulation, which reduces ecological benefit",
        "Crisis severity shifts the ethical calculus — actions that are unjustifiable in normal times may become necessary during emergencies",
        "Animal autonomy impact works AGAINST ethical justification — the more technology controls animal behavior, the harder it is to justify morally",
        "Regulation reduces unintended consequences but ALSO reduces ecological benefit — there is no regulation level that maximizes both",
        "The highest ethical justification scores require BOTH high transparency AND moderate regulation — neither alone is sufficient"
    ],
    "answer": "When AI and robots enter conservation, every design choice carries ethical weight. More powerful technology helps ecosystems but also creates more unintended consequences and threatens animal autonomy. Transparency builds the public trust needed for long-term support, while regulation reduces harm but also limits benefit. The ethical justification for deploying conservation technology depends on ALL these factors — and the balance shifts depending on crisis severity. There is no universal answer, but our model reveals that the combination of transparency, proportional regulation, and honest assessment of animal autonomy impact consistently produces the most ethically defensible outcomes.",
    "stem_title": "Speculative Design Project",
    "stem_mission": "Design a fictional conservation technology of the future, then evaluate it through your ethical model. Produce a technical blueprint, ethical impact assessment, public communication plan, and a 2-minute pitch video defending your design.",
    "stem_scenario": "A global conservation council is accepting proposals for next-generation AI-powered conservation technologies. Your team must design a system that addresses a real ecological crisis, but you must also prove that your technology is ethically justifiable. The council will evaluate your proposal on ecological benefit, ethical safeguards, and public communication quality.",
    "stem_questions": [
        "What ecological crisis does your technology address, and how severe is it?",
        "What are the three most likely unintended consequences of your design, and how do you mitigate them?",
        "How will you ensure transparency — what will the public know about how your technology works?"
    ],
    "stem_design_qs": [
        "What level of autonomy does your technology have — does it recommend actions or take them independently?",
        "How does your design protect animal autonomy while still achieving ecological benefit?",
        "What regulatory framework would you propose for governing your technology?",
        "How would you communicate your technology's purpose and risks to a skeptical public?"
    ],
    "career": "AI Ethics Researchers and Conservation Technology Policy Analysts develop frameworks for responsible deployment of AI and robotics in environmental contexts. They work with tech companies, government agencies, and NGOs to ensure emerging technologies protect both ecosystems and civil liberties. They earn $85,000–$150,000/year.",
    "images": {
        "cover": ("cover-ai-ethics.png", "A photorealistic image of a small autonomous drone hovering near a bird's nest in a forest canopy, the drone has a subtle green LED, the bird watches cautiously, tension between technology and nature, golden hour forest light, cinematic nature documentary style"),
        "landscape": ("landscape-ai-ethics.png", "A photorealistic image of diverse 10th-12th grade students (15-18 years old) gathered around a large table covered with blueprint paper, sticky notes, and laptops, collaboratively designing a conservation technology prototype, Black female student leading the discussion and pointing at a diagram, Latin American male student and Asian/AAPI female student contributing ideas, White male student taking notes, modern STEM innovation lab with natural light"),
        "modeling": ("modeling-ai-ethics.png", "A photorealistic image of diverse 10th-12th grade students working in pairs on laptops building a 9-component ethical decision model, Latin American male student explaining a relationship arrow on screen to his partner, a White female student, modern classroom with environmental ethics posters on the wall, natural light"),
        "discussion": ("discussion-ai-ethics.png", "A photorealistic image of a Black male teacher facilitating an intense Socratic seminar with diverse 10th-12th grade students seated in a circle, Asian/AAPI male student making a passionate argument while others listen intently, some students nodding and some looking skeptical, modern classroom with large windows and natural light"),
        "stem": ("stem-ai-ethics.png", "A photorealistic image of diverse 10th-12th grade students presenting a speculative technology design at a podium with a projected blueprint behind them, Latin American female student at the microphone delivering a pitch, Black male student and White female student standing alongside as teammates, panel of student judges seated at a table with scoring sheets, professional presentation atmosphere")
    },
    "pre_assessment": [
        "In Level 1, you modeled whether intervention is justified using severity, risk, and evidence. What NEW factors matter when the technology making decisions is AI — not a human?",
        "Should an AI system be allowed to make life-or-death decisions about wildlife without human approval? Why or why not?",
        "What does 'transparency' mean when it comes to technology? Why might people demand it?",
        "Can you think of a technology that was created to help but ended up causing harm? What went wrong?"
    ],
    "extend_components": [
        ("Community Benefit", "Whether local and Indigenous communities benefit from or are harmed by the technology deployment"),
        ("Data Security", "How well the technology protects sensitive ecological data from misuse, poaching, or commercial exploitation"),
        ("Long-Term Dependency", "Whether ecosystems become reliant on the technology to survive, reducing natural resilience")
    ],
    "reflections": [
        "How is the Level 2 model different from the Level 1 ethics model? What does adding 5 more components reveal about the complexity of real ethical decisions?",
        "Trace the feedback loop: Unintended Consequences → Public Trust → Regulation → Ecological Benefit. What makes this loop so difficult to manage?",
        "In the Emergency Override scenario, the ethical justification shifts. Is it ever acceptable to lower ethical standards during a crisis? Where do you draw the line?",
        "How does animal autonomy factor into ethical justification — and why do some people weight it more heavily than others?",
        "If you were advising a government on AI conservation policy, what would your top three recommendations be based on your model results?"
    ],
    "dimensions": [
        ("Science Practice", "Engaging in Argument from Evidence", "Students use 9-component model outputs as quantitative evidence to argue for or against specific AI conservation deployment strategies across multiple ethical dimensions."),
        ("Disciplinary Core Idea", "ETS1.B Developing Possible Solutions", "Students evaluate technology solutions by weighing ecological benefit criteria against ethical constraints including transparency, animal autonomy, and public trust."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify that technology deployment creates cascading and sometimes contradictory effects — the same input (high capability) simultaneously causes positive outcomes (ecological benefit) and negative outcomes (unintended consequences), requiring systems-level analysis.")
    ],
    "cast_items": [
        "Explain how technology capability creates simultaneous positive and negative outcomes in conservation contexts",
        "Use a 9-component model to evaluate competing ethical frameworks for AI deployment in ecosystems",
        "Design and defend an ethical justification for a specific conservation technology deployment using model evidence"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A conservation agency deploys an autonomous drone network to monitor endangered sea turtles. The drones operate with high capability but low transparency. According to the model, which outcome is MOST LIKELY? A) High public trust due to ecological benefit B) Low public trust despite ecological benefit C) High ethical justification due to crisis severity D) Low unintended consequences due to regulation"),
        ("Constructed Response:", "A government proposes using AI-controlled robotic predators to manage an invasive species threatening native birds. Using your 9-component model, evaluate this proposal by analyzing Technology Capability, Transparency, Crisis Severity, and Regulation. Then argue whether this deployment is ethically justified, addressing ecological benefit, unintended consequences, animal autonomy, and public trust.")
    ],
    "background_intro": "This lesson builds on Level 1's simple three-factor ethics model by expanding to a full 9-component system that captures the real complexity of deploying AI and robotics in conservation. Students now grapple with feedback loops, competing values, and the uncomfortable reality that there is no deployment strategy that maximizes all ethical outcomes simultaneously.",
    "background_sections": [
        ("AI in Conservation Today", "AI is already transforming conservation: machine learning identifies species from camera trap images, drones monitor deforestation in real time, acoustic sensors detect poaching activity, and predictive algorithms guide ranger patrol routes. These technologies have produced measurable gains — but each deployment raises questions about surveillance, data ownership, community consent, and what happens when algorithms make mistakes."),
        ("The Capability-Consequence Paradox", "More powerful conservation technology produces greater ecological benefits — but also greater potential for harm. A basic camera trap has limited benefit but also limited risk. A fully autonomous system that can track, identify, and intervene with wildlife has enormous potential benefit but also enormous potential for unintended consequences: disrupting migration patterns, habituating animals to technology, creating dependency, or misidentifying threats. This paradox means that the most powerful tools demand the most careful governance."),
        ("Transparency and Trust", "Public trust in conservation technology is fundamentally tied to transparency. When communities understand how a technology works, what data it collects, and who controls the decisions, they are far more likely to support its deployment. When technology operates opaquely — collecting data without explanation, making decisions without accountability — public opposition grows regardless of ecological results. The history of conservation is filled with well-intentioned projects that failed because they lost community trust."),
        ("The Regulation Dilemma", "Regulation protects against harm but also limits benefit. Strict rules slow deployment, increase costs, and may prevent timely intervention during ecological emergencies. No regulation allows rapid action but invites recklessness, profiteering, and abuse. The challenge is finding proportional regulation — strict enough to prevent harm, flexible enough to allow benefit, and adaptive enough to evolve as technology changes. Our model reveals this tension directly: increasing Regulation Strictness decreases Unintended Consequences but also decreases Ecological Benefit.")
    ],
    "lever_L": "Students identify Technology Capability Level, Transparency Level, Ecological Crisis Severity, and Regulation Strictness as external components (conditions and policy choices we can set). Ecological Benefit, Unintended Consequences, Animal Autonomy Impact, Public Trust, and Ethical Justification Score are internal components (outcomes produced by the system).",
    "lever_E": "Students discover complex and sometimes contradictory relationships: Technology Capability positively affects BOTH Ecological Benefit AND Unintended Consequences. Transparency positively affects Public Trust. Unintended Consequences negatively affect Public Trust (feedback loop). Crisis Severity positively affects Ethical Justification. Animal Autonomy Impact negatively affects Ethical Justification. Regulation reduces Unintended Consequences but also reduces Ecological Benefit. Low Public Trust drives increased Regulation (feedback loop).",
    "lever_V": "Students build the full 9-component model with four external inputs feeding five internal outputs through interconnected, sometimes contradictory relationships including feedback loops.",
    "lever_Ev": "Students run four scenarios — Transparent and Regulated, Unregulated Cowboy, Emergency Override, and Surveillance State — to test how different governance philosophies produce different ethical outcomes.",
    "lever_R": "Students add Community Benefit, Data Security, or Long-Term Dependency to see how additional real-world factors further complicate the ethical landscape.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Drone hovering near wildlife in forest", "say": "In Level 1, we asked 'should we or should we not?' Today we ask something harder: WHEN we use AI and robots to protect nature, who decides what is ethical — and how?", "do": "Show a montage of real conservation technology: camera traps, drones, acoustic sensors, robotic fish. Ask: What could go wrong with each?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "We are building a 9-component model today — the most complex system in this series. Nine moving parts, feedback loops, and no easy answers.", "do": "Pre-teach 'algorithmic transparency,' 'autonomous system,' and 'animal autonomy.' Connect to Level 1 vocabulary: intervention, risk assessment, unintended consequences.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Who decides what is ethical?", "say": "An AI drone detects a poacher and decides to alert rangers. Another AI decides to herd endangered animals away from a wildfire. A third AI decides which habitat patches to restore first. Who programmed those decisions? Who approved them? Who is accountable if something goes wrong?", "do": "Think-pair-share: If an AI makes a mistake that harms wildlife, who is responsible — the engineer, the government, or the AI itself? Collect diverse perspectives.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps with feedback loop emphasis", "say": "This model has something new — FEEDBACK LOOPS. When unintended consequences happen, public trust drops, which causes MORE regulation, which reduces ecological benefit. Actions have echoes.", "do": "Draw the feedback loop on the board: Unintended Consequences → Public Trust drops → Regulation increases → Ecological Benefit drops. Ask: How do you break this cycle?", "time": "3 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "9 component cards for sorting", "say": "Four things we can set: how powerful the tech is, how transparent we are, how severe the crisis is, and how strict the rules are. Five things the system produces. Sort them.", "do": "Guide component sorting. Emphasize: this is the first model with NINE components. The externals are policy and design CHOICES. The internals are CONSEQUENCES of those choices.", "time": "10 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Complex relationship web with feedback loops", "say": "Here is where it gets intense. Technology Capability feeds Ecological Benefit with a positive arrow AND feeds Unintended Consequences with ANOTHER positive arrow. The same input causes good AND bad. That is the paradox.", "do": "Build relationships step by step. Key moments: (1) dual arrows from Tech Capability, (2) Transparency to Public Trust positive, (3) Unintended Consequences to Public Trust negative, (4) feedback loop from Public Trust to Regulation. Have students trace each path.", "time": "12 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Four ethical scenarios", "say": "Four governance philosophies. Transparent and Regulated, Unregulated Cowboy, Emergency Override, and Surveillance State. Predict BEFORE we run. Which approach scores highest on ethical justification?", "do": "Run all four scenarios. After each, pause for comparison. Key discussion: Emergency Override — does crisis severity change what is ethical? Surveillance State — can regulation substitute for transparency?", "time": "14 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings and feedback loops", "say": "No deployment strategy maximizes everything. But transparency combined with proportional regulation consistently produces the most ethically defensible outcomes. The model does not tell us what is right — it shows us what we are trading away with every choice.", "do": "Summarize key findings. Revisit the big question: Who decides? Discuss: Should it be engineers, communities, governments, or all three? What role does the model play in that decision?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Speculative Design Project", "say": "Now you become conservation technology designers AND ethicists. Design a fictional technology, evaluate it through your model, and pitch it to the class.", "do": "Distribute project materials. Teams choose a crisis, design a technology, create a blueprint and ethical impact assessment, draft a public communication plan, and prepare a 2-minute pitch.", "time": "12 min"}
    ],
    "sort_reasoning": "Technology Capability Level, Transparency Level, Ecological Crisis Severity, and Regulation Strictness are external because they represent design decisions, policy choices, and environmental conditions that exist independently and can be observed or set. Ecological Benefit, Unintended Consequences, Animal Autonomy Impact, Public Trust, and Ethical Justification Score are internal because they are OUTCOMES produced by the interaction of those external factors — you cannot set them directly, only influence them through the choices you make about capability, transparency, crisis response, and regulation.",
    "relationships": [
        ("Technology Capability to Ecological Benefit", "POSITIVE (+)", "More powerful AI and robotic systems can monitor more area, respond faster, and manage more complex ecological interventions. Higher capability translates directly to greater conservation impact."),
        ("Technology Capability to Unintended Consequences", "POSITIVE (+)", "More powerful systems interact with ecosystems in more ways, creating more opportunities for unexpected outcomes — algorithm errors, behavioral disruption, cascading ecological effects that simpler tools would not trigger."),
        ("Technology Capability to Animal Autonomy Impact", "POSITIVE (+)", "More capable systems interact more directly with wildlife — tracking, herding, deterring, or managing animal behavior. Higher capability means more intrusion into natural behavioral patterns."),
        ("Transparency Level to Public Trust", "POSITIVE (+)", "When the public can see how the technology works, what data it collects, and how decisions are made, trust increases substantially. Transparency is the single strongest predictor of sustained public support."),
        ("Unintended Consequences to Public Trust", "NEGATIVE (-)", "Every unintended negative outcome erodes public confidence. Even one highly visible failure can destroy years of trust-building, regardless of the overall ecological benefit achieved."),
        ("Ecological Crisis Severity to Ethical Justification Score", "POSITIVE (+)", "The more severe the crisis, the more ethically acceptable it becomes to deploy powerful technology — emergency conditions shift the moral calculus toward action even when risks are elevated."),
        ("Animal Autonomy Impact to Ethical Justification Score", "NEGATIVE (-)", "Greater disruption to natural animal behavior weakens ethical justification. Wildlife has intrinsic value as autonomous beings — the more technology controls or constrains that autonomy, the harder the intervention is to justify morally."),
        ("Regulation Strictness to Unintended Consequences", "NEGATIVE (-)", "Stricter regulations require more testing, more safeguards, and more oversight, which reduces the likelihood and severity of unintended negative outcomes."),
        ("Regulation Strictness to Ecological Benefit", "NEGATIVE (-)", "Stricter regulations slow deployment, limit the scope of intervention, and increase costs — all of which reduce the total ecological benefit that can be achieved within a given timeframe."),
        ("Public Trust to Regulation Strictness", "NEGATIVE (-) FEEDBACK LOOP", "When public trust drops, political pressure increases for stricter regulations. Low trust drives regulatory backlash, which further constrains the technology. This feedback loop can spiral: unintended consequences → trust drops → more regulation → less benefit → question the whole program.")
    ],
    "sim_answers": [
        ("Transparent and Regulated Scenario", "With medium Technology Capability, high Transparency, moderate Crisis Severity, and strict Regulation, Ecological Benefit is moderate (limited by regulation and moderate tech), Unintended Consequences are low (regulation provides safeguards), Animal Autonomy Impact is low to moderate, Public Trust is HIGH (transparency drives it), and Ethical Justification Score is solidly positive. This is the slow-and-steady approach — less dramatic benefit but sustainable and defensible."),
        ("Unregulated Cowboy Scenario", "With high Technology Capability, low Transparency, low Crisis Severity, and no Regulation, Ecological Benefit is moderate (no real crisis to solve), Unintended Consequences are HIGH (no safeguards), Animal Autonomy Impact is high, Public Trust is VERY LOW (no transparency, no accountability), and Ethical Justification Score is very low. Without a genuine crisis AND without transparency, deploying powerful technology is ethically indefensible — it looks like surveillance, not conservation."),
        ("Emergency Override Scenario", "With maximum Technology Capability, medium Transparency, extreme Crisis Severity, and relaxed Regulation, Ecological Benefit is HIGH (maximum tech addressing real emergency), Unintended Consequences are moderate to high (relaxed safeguards), Animal Autonomy Impact is high, Public Trust is moderate (transparency helps but consequences worry people), and Ethical Justification Score is HIGH — the extreme crisis severity tips the balance. This is the scenario that generates the most debate: is a genuine emergency enough to justify elevated risk?"),
        ("Surveillance State Scenario", "With maximum Technology Capability, low Transparency, moderate Crisis Severity, and strict Regulation, Ecological Benefit is moderate (regulation limits it), Unintended Consequences are low to moderate (regulation helps), Animal Autonomy Impact is high (maximum tech), Public Trust is LOW (strict rules cannot compensate for secrecy — people do not trust what they cannot see), and Ethical Justification Score is moderate to low. Regulation without transparency creates a control-without-accountability dynamic that undermines ethical standing.")
    ],
    "reflection_exemplars": [
        ("How is Level 2 different from Level 1?", "Level 1 gave us three factors and one output — a simple framework for 'should we act?' Level 2 explodes that into nine components with feedback loops and competing outputs. The big revelation is that real ethical decisions are not linear — they loop back on themselves. Unintended consequences do not just happen and stop; they destroy public trust, which changes regulation, which changes benefit. Every action echoes. The 9-component model shows that ethics is not a one-time calculation but an ongoing, dynamic system that requires constant monitoring and adjustment."),
        ("Does crisis severity change what is ethical?", "The Emergency Override scenario shows that crisis severity genuinely shifts the ethical calculus. Actions that would be unjustifiable under normal conditions — deploying untested technology, relaxing safety regulations, accepting higher risk of unintended consequences — become more defensible when a species is days from extinction. But this creates a dangerous precedent: if emergency can justify anything, who defines what counts as an emergency? The model helps by requiring you to explicitly rate crisis severity rather than letting emotions drive the decision. It forces transparency about WHY you believe the crisis justifies the risk.")
    ],
    "stem_intro": "Present the Speculative Design Project: Teams will design a fictional next-generation conservation technology that addresses a real ecological crisis. Each team must produce four deliverables: (1) a technical blueprint showing how the technology works, (2) an ethical impact assessment using their 9-component model, (3) a public communication plan explaining the technology to a skeptical audience, and (4) a 2-minute pitch video defending their design to a panel of judges.",
    "stem_concepts": [
        ("Dual-Use Technology", "The same AI system that protects endangered species could be repurposed for surveillance, poaching intelligence, or commercial exploitation. Your design must include safeguards against misuse."),
        ("Proportional Response", "The power of the technology should match the severity of the crisis. Deploying maximum capability for a minor concern is ethically questionable even if technically possible."),
        ("Stakeholder Analysis", "Your design affects multiple groups: scientists, local communities, Indigenous peoples, governments, and the animals themselves. Each stakeholder has different needs and concerns.")
    ],
    "stem_eval": [
        ("Expert (4)", "Blueprint is technically detailed, ethical impact assessment addresses all 9 components with model data, public communication plan anticipates objections, pitch video is compelling and evidence-based"),
        ("Proficient (3)", "Blueprint shows clear design thinking, ethical assessment addresses at least 6 components, communication plan is coherent, pitch video presents a clear argument"),
        ("Developing (2)", "Blueprint exists but lacks detail, ethical assessment is incomplete or disconnected from model, communication plan is vague"),
        ("Beginning (1)", "Deliverables are incomplete or ethical analysis does not connect to the 9-component model")
    ],
    "support": [
        "Provide crisis scenario cards with pre-rated severity levels and background information",
        "Ethical impact assessment template with all 9 components listed and rating scales",
        "Argument frames: 'Our technology is ethically justified because the crisis severity is __, our transparency plan includes __, and we mitigate unintended consequences by __'",
        "Sample public communication plan outline: purpose statement, how it works (plain language), data collected, who controls it, what could go wrong, how we will fix it"
    ],
    "extensions": [
        "Research a real AI conservation deployment (e.g., SMART ranger patrols, Wildlife Insights camera traps, or acoustic monitoring in rainforests) and rate it using your 9-component model",
        "Write a policy brief for a fictional government recommending a regulatory framework for AI in conservation, citing your model results as evidence",
        "Design an 'AI Ethics Review Board' for conservation technology — who sits on it, what criteria do they use, and how do they balance speed against caution?"
    ],
    "cross_curr": [
        ("Math", "Create a weighted scoring algorithm for Ethical Justification: assign percentage weights to Ecological Benefit, Unintended Consequences, Animal Autonomy Impact, and Public Trust. How do different weightings change the justification score? Graph the sensitivity."),
        ("ELA", "Write a persuasive op-ed from the perspective of a conservation technologist defending a controversial AI deployment to a skeptical public. Use model data, rhetorical strategies, and anticipatory counterarguments."),
        ("Social Studies", "Compare how different nations regulate AI in environmental contexts — the EU's precautionary approach vs. China's rapid deployment vs. the US's industry self-regulation. Which approach does your model suggest produces the best ethical outcomes?")
    ],
    "misconceptions": [
        ("More advanced technology is always better for conservation", "The model directly contradicts this: higher Technology Capability increases Ecological Benefit AND Unintended Consequences simultaneously. The most powerful tools carry the most risk. A simpler technology with fewer unintended consequences and higher public trust may achieve more long-term conservation success than a powerful system that triggers a regulatory backlash. The right technology is the one proportional to the crisis, not the most advanced one available.", "Run the model with maximum tech capability and low crisis severity. Compare to moderate tech with moderate crisis. Ask: Which scenario has higher Ethical Justification? Why?"),
        ("Strict regulation solves all ethical problems", "Regulation reduces unintended consequences, but it also reduces ecological benefit — and it cannot substitute for transparency. The Surveillance State scenario proves this: strict rules with low transparency still produces low public trust and low ethical justification. Regulation without transparency creates a 'trust us, we have rules' dynamic that the public sees through. Effective governance requires BOTH regulatory safeguards AND transparent communication.", "Compare the Transparent and Regulated scenario to the Surveillance State scenario. Both have strict regulation. Which has higher public trust? What is the difference?"),
        ("If the ecological benefit is large enough, nothing else matters", "This is consequentialist thinking — and the model shows its limits. Even with maximum ecological benefit, high unintended consequences, low public trust, and high animal autonomy impact drag down the ethical justification score. Conservation that ignores community trust, animal welfare, and transparency may achieve short-term gains but creates long-term opposition that undermines the entire program. Sustainable conservation requires ethical legitimacy, not just ecological results.", "Ask: If a technology saves 1,000 animals but destroys public trust in conservation science, was it worth it? What happens to the NEXT 1,000 animals when the public refuses to fund conservation technology?")
    ],
    "game": {
        "title": "AI Ethics Escape Room",
        "type": "Collaborative Puzzle Challenge",
        "description": "Five ethical dilemmas are presented as locked puzzles. Each puzzle presents a conservation AI scenario with conflicting stakeholder perspectives. Teams must discuss, debate, and reach consensus on an ethical framework before they can 'unlock' the next challenge. Puzzles escalate in complexity: (1) basic monitoring vs. privacy, (2) autonomous intervention vs. human oversight, (3) data sharing vs. poaching risk, (4) emergency deployment vs. precautionary principle, (5) final scenario combining all tensions. Teams that reach consensus on all five within the time limit escape.",
        "materials": ["5 sealed puzzle envelopes with scenario cards and stakeholder role cards", "Consensus recording sheets (all team members must sign)", "Timer (40 minutes total)", "Ethical framework reference guide", "Model relationship summary sheet", "Lock combination cards (revealed when consensus is documented)"],
        "learning_connection": "Forces students to move beyond individual opinions to collaborative ethical reasoning — they cannot advance without genuine consensus, mirroring the real-world requirement that technology governance requires broad agreement among diverse stakeholders."
    },
    "steam_activity": {
        "title": "Speculative Design Project",
        "type": "Engineering Design + Ethics + Communication",
        "description": "Student teams design a fictional next-generation conservation technology (e.g., autonomous reef restoration swarms, AI-guided seed dispersal drones, robotic pollinator networks). Each team produces four deliverables: (1) a technical blueprint showing system architecture and capabilities, (2) an ethical impact assessment rating all 9 model components with evidence, (3) a public communication plan explaining the technology to a skeptical community, and (4) a 2-minute pitch video defending the design to a panel of judges. Teams present to the class, and judges score on ecological merit, ethical rigor, and communication clarity.",
        "materials": ["Blueprint paper and colored markers", "Ethical impact assessment templates", "Public communication plan outlines", "Video recording devices (phones or tablets)", "Presentation scoring rubrics", "Real conservation technology case studies for inspiration"],
        "learning_connection": "Integrates all nine model components into a single creative project — students must balance technical capability against ethical constraints, design transparency into their system from the start, and communicate complex tradeoffs to a non-expert audience."
    }
}

# =============================================================================
# COLLECTIONS FOR IMPORT
# =============================================================================

LEVEL_1_LESSONS = [L1_01, L1_02, L1_03, L1_04, L1_05, L1_06]
LEVEL_2_LESSONS = [L2_01, L2_02, L2_03, L2_04, L2_05, L2_06]
ALL_LESSONS = LEVEL_1_LESSONS + LEVEL_2_LESSONS
