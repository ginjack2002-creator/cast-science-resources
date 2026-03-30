#!/usr/bin/env python3
"""Multiple choice pre/post assessment questions for Nature's Engineers ModelIt! Lessons"""

# Format: Each lesson has mc_pre_assessment and mc_post_assessment lists
# Each question is a dict with: question, choices (dict A-D), correct (letter), feedback_correct, feedback_incorrect
# Nature's Engineers is a cross-grade unit covering biomimicry, beaver ecology, ecohydrology, neuroscience, and AI ethics

# =============================================================================
# LEVEL 1 LESSONS (Introductory)
# =============================================================================

L1_01_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is a dam?",
            "choices": {
                "A": "A wall built across a stream that holds water back",
                "B": "A type of boat that floats on water",
                "C": "A hole dug into the ground to find water",
                "D": "A bridge that lets animals cross a river"
            },
            "correct": "A",
            "feedback_correct": "Correct! A dam is a wall built across a stream that holds water back and creates a pond.",
            "feedback_incorrect": "A dam is a wall built across a stream that holds water back. When a dam blocks flowing water, it creates a pond behind it."
        },
        {
            "question": "What do beavers use to build their dams?",
            "choices": {
                "A": "Rocks and sand only",
                "B": "Trees, sticks, and mud",
                "C": "Leaves and grass",
                "D": "They do not build anything"
            },
            "correct": "B",
            "feedback_correct": "That is right! Beavers use trees, sticks, and mud to build their dams across streams.",
            "feedback_incorrect": "Beavers are natural builders that use trees, sticks, and mud to construct their dams. They chew down trees with their strong teeth and drag them into the water."
        },
        {
            "question": "What do you think happens to a stream when something blocks the water?",
            "choices": {
                "A": "The water disappears completely",
                "B": "The water flows faster downstream",
                "C": "The water collects and forms a pond",
                "D": "The water turns into ice"
            },
            "correct": "C",
            "feedback_correct": "Yes! When something blocks a stream, water collects behind the blockage and forms a pond.",
            "feedback_incorrect": "When water is blocked, it does not disappear. Instead, it collects behind the blockage and forms a pond or lake."
        },
        {
            "question": "Why might other animals care about a beaver dam?",
            "choices": {
                "A": "Other animals are afraid of beaver dams",
                "B": "The pond creates a new place for animals to live",
                "C": "Other animals want to destroy the dam",
                "D": "Other animals do not notice beaver dams at all"
            },
            "correct": "B",
            "feedback_correct": "Correct! The pond created by a beaver dam becomes a new habitat where many animals like fish, frogs, and birds can live.",
            "feedback_incorrect": "Beaver dams are important to many animals because the pond they create becomes a new habitat. Fish, frogs, birds, and many other animals move in and make the pond their home."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "Why are beavers called 'ecosystem engineers'?",
            "choices": {
                "A": "They wear hard hats when they work",
                "B": "They change their environment by building dams that create new habitats",
                "C": "They are the biggest animals in the forest",
                "D": "They only build things for themselves"
            },
            "correct": "B",
            "feedback_correct": "That is right! Beavers are called ecosystem engineers because their dam-building changes the whole environment, creating habitats for many other species.",
            "feedback_incorrect": "Beavers are called ecosystem engineers because they change their environment in big ways. Their dams create ponds that become habitats for fish, frogs, birds, and many other animals."
        },
        {
            "question": "In the model, what TWO things do beavers need to build a successful dam?",
            "choices": {
                "A": "Sunshine and wind",
                "B": "Enough beaver family members AND enough trees",
                "C": "Rocks and concrete",
                "D": "Only lots of water"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model showed that beavers need both enough family members to do the work AND enough trees as building material.",
            "feedback_incorrect": "The model showed that beavers need TWO inputs to build a dam: enough beaver family members to do the building work AND enough trees to use as construction material. If either one is missing, the dam cannot grow."
        },
        {
            "question": "What happens in the model when there are many beavers but NO trees?",
            "choices": {
                "A": "The dam grows very large anyway",
                "B": "The beavers use rocks instead",
                "C": "The dam cannot grow because beavers need trees as building material",
                "D": "The pond gets bigger without a dam"
            },
            "correct": "C",
            "feedback_correct": "Yes! Even with many beavers, the dam cannot grow without trees. Both inputs are needed for the system to work.",
            "feedback_incorrect": "Without trees, even lots of beavers cannot build a dam. The model shows that BOTH inputs (beavers AND trees) must be present for the dam to grow and the pond to form."
        },
        {
            "question": "How does dam size affect pond size in the model?",
            "choices": {
                "A": "A bigger dam holds back more water, creating a bigger pond",
                "B": "Dam size and pond size are not related",
                "C": "A bigger dam makes the pond smaller",
                "D": "Only rainfall affects pond size"
            },
            "correct": "A",
            "feedback_correct": "Correct! In the model, a bigger dam holds back more water, which creates a bigger pond. This is a cause and effect relationship.",
            "feedback_incorrect": "In the model, dam size directly affects pond size. A bigger dam holds back more water, creating a bigger pond. This is a cause and effect relationship where one component influences another."
        }
    ]
}

L1_02_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What does it mean to copy an idea from nature to solve a problem?",
            "choices": {
                "A": "Taking an animal home as a pet",
                "B": "Using a design found in nature to build something useful",
                "C": "Drawing a picture of an animal",
                "D": "Planting a garden"
            },
            "correct": "B",
            "feedback_correct": "Yes! Using designs found in nature to build useful things is called biomimicry. Engineers study animals and plants to get ideas for better technology.",
            "feedback_incorrect": "Copying ideas from nature means studying how animals and plants solve problems, then using those ideas to build better technology. This is called biomimicry."
        },
        {
            "question": "Why do you think a beaver has a flat tail?",
            "choices": {
                "A": "It looks nice",
                "B": "It helps the beaver swim and steer in the water",
                "C": "It keeps the beaver warm at night",
                "D": "It has no purpose at all"
            },
            "correct": "B",
            "feedback_correct": "Correct! A beaver's flat tail is an adaptation that helps it swim efficiently by pushing against the water like a paddle.",
            "feedback_incorrect": "A beaver's flat tail is specially shaped to help it swim. The flat shape pushes against water like a paddle, giving the beaver speed and steering ability. This is called an adaptation."
        },
        {
            "question": "If an engineer wanted to build a swimming robot, where might they look for ideas?",
            "choices": {
                "A": "At a car factory",
                "B": "At animals that are good swimmers",
                "C": "At a grocery store",
                "D": "At a library for fiction books"
            },
            "correct": "B",
            "feedback_correct": "That is right! Engineers often study animals that are good swimmers, like beavers, fish, and dolphins, to get ideas for designing swimming robots.",
            "feedback_incorrect": "Engineers look at animals that are good at swimming. By studying how fish, beavers, and dolphins move through water, engineers can design better swimming robots. Nature has been testing designs for millions of years."
        },
        {
            "question": "What is a tradeoff?",
            "choices": {
                "A": "When you trade toys with a friend",
                "B": "When improving one thing means making another thing worse",
                "C": "When you get everything you want with no problems",
                "D": "When two people agree on the same answer"
            },
            "correct": "B",
            "feedback_correct": "Correct! A tradeoff is when improving one thing means another thing gets worse. You cannot have everything at once.",
            "feedback_incorrect": "A tradeoff happens when making one thing better causes another thing to get worse. For example, making a robot bigger might give it more power, but it would also use more energy. You cannot have everything."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "What is biomimicry?",
            "choices": {
                "A": "Training animals to do human jobs",
                "B": "Designing human technology by copying ideas from nature",
                "C": "Building houses for animals in the wild",
                "D": "Taking photographs of animals"
            },
            "correct": "B",
            "feedback_correct": "Correct! Biomimicry is the practice of designing human technology by copying ideas and strategies found in nature.",
            "feedback_incorrect": "Biomimicry means designing technology by studying and copying ideas from nature. Engineers look at how animals solve problems and use those strategies to build better machines."
        },
        {
            "question": "In the model, what happened when you changed the tail shape from flat (beaver) to round?",
            "choices": {
                "A": "Swimming speed increased and energy use decreased",
                "B": "Swimming speed decreased because a round tail pushes less water",
                "C": "Nothing changed at all",
                "D": "The robot could not swim at all"
            },
            "correct": "B",
            "feedback_correct": "Yes! A flat tail pushes more water and creates more swimming speed. Changing to a round tail decreased speed because it pushes less water.",
            "feedback_incorrect": "The model showed that a flat tail (like a beaver's) pushes more water than a round tail, creating more swimming speed. When you switched to a round tail, speed went down because less water was being pushed."
        },
        {
            "question": "What tradeoff did the model reveal about body size?",
            "choices": {
                "A": "Bigger bodies are always better in every way",
                "B": "Smaller bodies are always better in every way",
                "C": "A bigger body gives more power but uses more energy",
                "D": "Body size has no effect on swimming"
            },
            "correct": "C",
            "feedback_correct": "Correct! The model showed that bigger bodies provide more power but also use more energy. This is a classic engineering tradeoff.",
            "feedback_incorrect": "The model revealed a tradeoff: a bigger body is stronger and more powerful, but it also uses more energy to move through water. Good engineering means finding the best balance between power and energy use."
        },
        {
            "question": "Why do engineers study animal shapes instead of inventing designs from scratch?",
            "choices": {
                "A": "Because animals tell engineers what to build",
                "B": "Because millions of years of evolution have already tested and refined these designs",
                "C": "Because it is easier to copy than to think",
                "D": "Because the government requires it"
            },
            "correct": "B",
            "feedback_correct": "That is right! Nature has been testing designs through evolution for millions of years. Animals alive today have shapes and features that have been refined over a very long time.",
            "feedback_incorrect": "Engineers study animal shapes because evolution has been testing and improving these designs for millions of years. The animals alive today have features that have been refined over vast stretches of time, making them excellent starting points for engineering designs."
        }
    ]
}

L1_03_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What happens to rain when it falls on a grassy field?",
            "choices": {
                "A": "It bounces back up into the sky",
                "B": "It soaks into the ground",
                "C": "It turns into ice immediately",
                "D": "It disappears completely"
            },
            "correct": "B",
            "feedback_correct": "Yes! When rain falls on a grassy field, much of it soaks into the soil. The ground acts like a sponge and absorbs the water.",
            "feedback_incorrect": "When rain hits a grassy field, the soil absorbs it like a sponge. The water soaks down into the ground where plant roots can use it."
        },
        {
            "question": "What happens to rain when it falls on a parking lot?",
            "choices": {
                "A": "It soaks into the pavement",
                "B": "It evaporates instantly",
                "C": "It flows across the surface as runoff",
                "D": "It stays in one spot and never moves"
            },
            "correct": "C",
            "feedback_correct": "Correct! Pavement does not absorb water, so rain flows across the surface as runoff, often collecting in low spots or drains.",
            "feedback_incorrect": "Pavement cannot absorb water the way soil does. Instead, rain flows across the hard surface as runoff, moving toward drains, gutters, and low spots."
        },
        {
            "question": "Why do some neighborhoods have more flooding problems than others?",
            "choices": {
                "A": "Because it rains more in some neighborhoods",
                "B": "Because some neighborhoods have more pavement and less soil to absorb water",
                "C": "Because floods only happen near the ocean",
                "D": "Because some people leave their sprinklers on"
            },
            "correct": "B",
            "feedback_correct": "Yes! Neighborhoods with more pavement and less natural ground have more flooding because the water has no place to soak in.",
            "feedback_incorrect": "Flooding is often worse in areas with more pavement. When natural ground is replaced with roads, parking lots, and buildings, rainwater cannot soak in and instead runs off the surface, causing floods."
        },
        {
            "question": "What does 'permeable' mean?",
            "choices": {
                "A": "Something that is very hard and strong",
                "B": "Something that lets water pass through it",
                "C": "Something that is colorful",
                "D": "Something that floats on water"
            },
            "correct": "B",
            "feedback_correct": "Correct! Permeable means a surface lets water pass through it, like soil or gravel.",
            "feedback_incorrect": "Permeable means a surface allows water to pass through it. Soil and gravel are permeable because water can soak through them. Pavement is impermeable because it blocks water."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "What is the difference between a permeable and an impermeable surface?",
            "choices": {
                "A": "Permeable surfaces are always wet and impermeable surfaces are always dry",
                "B": "Permeable surfaces let water pass through, impermeable surfaces block water",
                "C": "Permeable surfaces are natural and impermeable surfaces are always human-made",
                "D": "There is no difference between them"
            },
            "correct": "B",
            "feedback_correct": "That is right! Permeable surfaces like soil let water soak through, while impermeable surfaces like pavement block water from passing through.",
            "feedback_incorrect": "Permeable surfaces (like soil and gravel) allow water to pass through and soak in. Impermeable surfaces (like pavement and rock) block water from passing through, causing it to flow across the surface as runoff."
        },
        {
            "question": "In the model, what happened to runoff when the ground type was changed from soil to pavement?",
            "choices": {
                "A": "Runoff decreased because pavement absorbs more water",
                "B": "Runoff stayed the same regardless of ground type",
                "C": "Runoff increased significantly because pavement cannot absorb water",
                "D": "Runoff and absorption both increased equally"
            },
            "correct": "C",
            "feedback_correct": "Correct! The model showed that runoff increased dramatically on pavement because the impermeable surface cannot absorb water, forcing it all to flow across the surface.",
            "feedback_incorrect": "The model showed that switching from soil to pavement caused a large increase in runoff. Pavement is impermeable, meaning it blocks water from soaking in, so nearly all rain becomes runoff that flows across the surface."
        },
        {
            "question": "According to the model, what is the main reason cities experience more flooding than natural areas?",
            "choices": {
                "A": "Cities get more rainfall than natural areas",
                "B": "Cities have replaced natural soil with impermeable pavement, increasing runoff",
                "C": "Cities are built in areas that naturally flood",
                "D": "City buildings attract more rain clouds"
            },
            "correct": "B",
            "feedback_correct": "Yes! The model showed that replacing permeable soil with impermeable pavement is the main cause of urban flooding. Water that would normally soak into the ground instead becomes runoff.",
            "feedback_incorrect": "The model demonstrated that cities flood more because they have replaced natural soil (which absorbs water) with pavement (which blocks absorption). This turns rain into surface runoff, overwhelming drainage systems and causing floods."
        },
        {
            "question": "What does the model predict will happen if rainfall doubles on a soil surface?",
            "choices": {
                "A": "All the extra water will be absorbed by the soil",
                "B": "Both absorption and runoff increase, but the soil still absorbs more than pavement would",
                "C": "The soil will turn into pavement",
                "D": "Runoff will decrease because more rain makes soil absorb better"
            },
            "correct": "B",
            "feedback_correct": "Correct! When rainfall doubles on soil, both absorption and runoff increase. The soil can only absorb so much, but it still handles heavy rain far better than pavement.",
            "feedback_incorrect": "When rainfall increases on soil, both absorption and runoff go up. Soil has a limit to how much water it can absorb, so some extra rain becomes runoff. But soil still handles heavy rain much better than pavement, which produces nearly 100% runoff."
        }
    ]
}

L1_04_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "How does your brain send a message to your hand to pick something up?",
            "choices": {
                "A": "Your brain yells really loudly",
                "B": "Your brain sends electrical signals through your nerves",
                "C": "Your hand moves on its own without the brain",
                "D": "Your brain sends a letter through the mail"
            },
            "correct": "B",
            "feedback_correct": "Correct! Your brain sends tiny electrical signals along your nerves to tell your muscles what to do.",
            "feedback_incorrect": "Your brain communicates by sending tiny electrical signals through your nervous system. These signals travel along nerves from your brain to your muscles, telling them when and how to move."
        },
        {
            "question": "What happens to a message when there is a lot of noise around you?",
            "choices": {
                "A": "The message gets clearer",
                "B": "The message becomes harder to hear or understand",
                "C": "Noise does not affect messages at all",
                "D": "The message speeds up"
            },
            "correct": "B",
            "feedback_correct": "Yes! Noise makes messages harder to hear and understand. The same thing happens with electronic and brain signals.",
            "feedback_incorrect": "Noise interferes with messages and makes them harder to understand. Just like trying to hear someone in a loud room, electronic and brain signals can also be disrupted by interference."
        },
        {
            "question": "If you whisper to someone far away, why might they not hear you?",
            "choices": {
                "A": "Whispers are invisible",
                "B": "The sound is too weak to travel that far",
                "C": "Their ears stop working when you whisper",
                "D": "Whispers only work at night"
            },
            "correct": "B",
            "feedback_correct": "Correct! A whisper is a weak signal that loses strength as it travels. The farther it goes, the harder it is to hear.",
            "feedback_incorrect": "A whisper is a weak signal. As sound travels, it loses strength over distance. This is called signal degradation, and it happens with all types of signals, not just sound."
        },
        {
            "question": "What is a brain-computer interface?",
            "choices": {
                "A": "A computer that has a brain inside it",
                "B": "A system that reads brain signals and uses them to control a machine",
                "C": "A video game about brains",
                "D": "A type of brain surgery"
            },
            "correct": "B",
            "feedback_correct": "Yes! A brain-computer interface (BCI) is a system that reads electrical signals from the brain and translates them into commands that control a computer or machine.",
            "feedback_incorrect": "A brain-computer interface (BCI) reads the electrical signals your brain produces and translates them into commands that can control a computer, robotic arm, or other machine. It is a bridge between your brain and technology."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the model, which THREE factors affect whether a message arrives accurately?",
            "choices": {
                "A": "Color, size, and weight",
                "B": "Signal strength, distance traveled, and noise level",
                "C": "Temperature, time of day, and weather",
                "D": "Speed, direction, and shape"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model showed that signal strength, distance, and noise level are the three inputs that determine message accuracy.",
            "feedback_incorrect": "The model identified three key factors: signal strength (how strong the message starts), distance traveled (how far it must go), and noise level (how much interference is in the environment). All three affect whether the message arrives accurately."
        },
        {
            "question": "What did the model show happens when signal strength is high but noise level is also very high?",
            "choices": {
                "A": "The message always arrives perfectly because signal strength overcomes noise",
                "B": "Message accuracy drops because even strong signals can be ruined by extreme noise",
                "C": "Noise and signal strength cancel each other out",
                "D": "The distance automatically gets shorter"
            },
            "correct": "B",
            "feedback_correct": "Yes! The model showed that extreme noise can degrade even a strong signal. No signal is immune to overwhelming interference.",
            "feedback_incorrect": "Even a strong signal can be ruined by extreme noise. The model showed that while high signal strength helps, it cannot completely overcome very high noise levels. Message accuracy still drops when interference is too great."
        },
        {
            "question": "How is the telephone game similar to the challenges of brain-computer interfaces?",
            "choices": {
                "A": "They both use telephones",
                "B": "In both cases, signals degrade over distance and are disrupted by noise",
                "C": "They both require electricity",
                "D": "They are not similar at all"
            },
            "correct": "B",
            "feedback_correct": "Correct! Both the telephone game and BCIs face the same challenge: signals lose accuracy as they travel farther and encounter more noise along the way.",
            "feedback_incorrect": "The telephone game and brain-computer interfaces share the same core challenge: messages (signals) get distorted as they travel over distance, and noise in the environment makes them even harder to decode accurately."
        },
        {
            "question": "Why is reading brain signals so much harder than reading a keyboard press?",
            "choices": {
                "A": "Keyboards are more expensive than brain sensors",
                "B": "Brain signals are tiny, must travel through tissue, and are surrounded by billions of other signals creating noise",
                "C": "Brain signals are too fast for computers to read",
                "D": "Brains do not actually produce electrical signals"
            },
            "correct": "B",
            "feedback_correct": "That is right! Brain signals face all three challenges from the model: they are weak (low signal strength), must travel through tissue (distance), and are surrounded by billions of competing neural signals (noise).",
            "feedback_incorrect": "Reading brain signals is hard because of all three factors from our model. Brain signals are very weak (low signal strength), must travel through tissue and wires (distance), and are buried among billions of other neural signals (noise). Scientists must solve all three problems at once."
        }
    ]
}

L1_05_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Are all species in an ecosystem equally important?",
            "choices": {
                "A": "Yes, every species has exactly the same importance",
                "B": "No, some species have a bigger impact on the ecosystem than others",
                "C": "Only the biggest animals are important",
                "D": "Only plants are important in an ecosystem"
            },
            "correct": "B",
            "feedback_correct": "Correct! While all species play a role, some species have an outsized impact on their ecosystem. These are called keystone species.",
            "feedback_incorrect": "Not all species have the same impact. Some species, called keystone species, have a much bigger effect on their ecosystem than others. Removing them can change the entire system."
        },
        {
            "question": "What do you think happens to other animals when a beaver pond dries up?",
            "choices": {
                "A": "Nothing changes for the other animals",
                "B": "Other animals benefit from the dry land",
                "C": "Many animals lose their habitat and food sources",
                "D": "New animals immediately take their place"
            },
            "correct": "C",
            "feedback_correct": "Yes! When a beaver pond dries up, the fish, frogs, birds, and other animals that depended on that pond lose their habitat and food sources.",
            "feedback_incorrect": "When a beaver pond dries up, many animals are affected. Fish cannot survive without water, frogs lose their breeding ground, and birds lose food sources. The pond was habitat for many species."
        },
        {
            "question": "What is biodiversity?",
            "choices": {
                "A": "The total number of animals in the world",
                "B": "The variety of different species living in an ecosystem",
                "C": "How big an ecosystem is",
                "D": "The color of plants in an area"
            },
            "correct": "B",
            "feedback_correct": "Correct! Biodiversity is the variety of different species living in an ecosystem. More biodiversity generally means a healthier system.",
            "feedback_incorrect": "Biodiversity refers to the variety of different species living in an ecosystem. An area with many different types of plants, animals, and insects has high biodiversity. Higher biodiversity usually means a healthier ecosystem."
        },
        {
            "question": "What is a feedback loop?",
            "choices": {
                "A": "When something is fed back to animals in a zoo",
                "B": "When the output of a system circles back and affects its own input",
                "C": "When you leave feedback on a website",
                "D": "When a loop of rope is used in an experiment"
            },
            "correct": "B",
            "feedback_correct": "Yes! A feedback loop happens when the output of a system circles back and affects the input, creating a cycle that can amplify or reduce changes.",
            "feedback_incorrect": "A feedback loop is when the result (output) of a system circles back and affects what goes into the system (input). This creates a cycle. For example, more species improve habitat quality, which then supports even more species."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "What is a keystone species?",
            "choices": {
                "A": "The largest animal in an ecosystem",
                "B": "A species that has an outsized impact on its ecosystem, and removing it changes everything",
                "C": "A species that lives in rocky habitats",
                "D": "The most common species in an area"
            },
            "correct": "B",
            "feedback_correct": "Correct! A keystone species has an outsized impact on its ecosystem. Like a keystone in an arch, removing it causes the whole structure to change or collapse.",
            "feedback_incorrect": "A keystone species is one that has a much bigger impact on its ecosystem than its numbers would suggest. Removing a keystone species triggers a cascade of changes throughout the entire ecosystem."
        },
        {
            "question": "What did the model show when the keystone species population was set to zero?",
            "choices": {
                "A": "Only the keystone species was affected",
                "B": "Habitat quality, food availability, and biodiversity all declined in a cascade",
                "C": "The ecosystem immediately recovered on its own",
                "D": "Other species became keystone species instead"
            },
            "correct": "B",
            "feedback_correct": "Yes! The model showed a cascade effect: removing the keystone species caused habitat quality to drop, then food availability dropped, and then biodiversity crashed.",
            "feedback_incorrect": "The model demonstrated a cascade effect. When the keystone species was removed, habitat quality declined, which caused food availability to drop, which then led to a decline in the number of other species. One change triggered a chain of decline."
        },
        {
            "question": "What type of feedback loop did the model reveal between biodiversity and habitat quality?",
            "choices": {
                "A": "A negative feedback loop where they cancel each other out",
                "B": "A reinforcing feedback loop where more species improve habitat, which supports even more species",
                "C": "No feedback loop exists between them",
                "D": "A loop that only works in one direction"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model showed a reinforcing feedback loop: more species improve habitat quality, and better habitat supports even more species, creating a cycle of growth.",
            "feedback_incorrect": "The model revealed a reinforcing (positive) feedback loop. More species improve habitat quality by contributing to soil health, water filtering, and vegetation growth. Better habitat then supports even more species. This cycle amplifies recovery."
        },
        {
            "question": "According to the model, what happens when keystone species are brought back after being removed?",
            "choices": {
                "A": "The ecosystem recovers instantly",
                "B": "The ecosystem never recovers",
                "C": "Recovery takes time because the ecosystem must rebuild step by step",
                "D": "Only the keystone species benefits, not other species"
            },
            "correct": "C",
            "feedback_correct": "That is right! The model showed that recovery takes time. The ecosystem must rebuild gradually because each step in the cascade depends on the one before it.",
            "feedback_incorrect": "The model showed that ecosystems do not bounce back instantly. Recovery takes time because each part of the cascade (habitat, food, biodiversity) must rebuild in sequence. The reinforcing feedback loop eventually accelerates recovery, but it starts slowly."
        }
    ]
}

L1_06_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "When scientists discover a new technology that could help the environment, should they always use it right away?",
            "choices": {
                "A": "Yes, if it could help, they should use it immediately",
                "B": "No, they should first consider whether it might cause new problems",
                "C": "It does not matter because technology always works perfectly",
                "D": "Scientists should never use technology on the environment"
            },
            "correct": "B",
            "feedback_correct": "Correct! Before using a new technology, scientists should carefully consider whether it might cause unintended negative consequences.",
            "feedback_incorrect": "Before using any technology, especially in the environment, scientists must think carefully about whether it could cause new problems. Good intentions do not guarantee good outcomes."
        },
        {
            "question": "What does 'risk assessment' mean?",
            "choices": {
                "A": "Deciding how much money something will cost",
                "B": "Carefully evaluating what could go wrong before taking action",
                "C": "Testing how fast something can move",
                "D": "Asking your friends what they think"
            },
            "correct": "B",
            "feedback_correct": "Yes! Risk assessment means carefully evaluating potential negative outcomes before taking action. It is a critical step in responsible decision-making.",
            "feedback_incorrect": "Risk assessment is the process of carefully evaluating what could go wrong before taking action. Scientists and engineers use risk assessment to weigh potential benefits against potential harm."
        },
        {
            "question": "What are 'unintended consequences'?",
            "choices": {
                "A": "Results that you planned for and expected",
                "B": "Unexpected negative outcomes from an action that was meant to help",
                "C": "Consequences that do not actually happen",
                "D": "Positive results that always follow good decisions"
            },
            "correct": "B",
            "feedback_correct": "Correct! Unintended consequences are unexpected negative outcomes that happen as a result of an action meant to be helpful.",
            "feedback_incorrect": "Unintended consequences are unexpected negative results that come from actions meant to help. For example, introducing a new animal to control pests might cause that animal to harm native species too."
        },
        {
            "question": "Should decisions about the environment be based on feelings or on scientific evidence?",
            "choices": {
                "A": "Only on feelings because science is too complicated",
                "B": "Only on evidence because feelings never matter",
                "C": "Primarily on evidence, but values and ethics also play a role",
                "D": "On whatever the majority votes for"
            },
            "correct": "C",
            "feedback_correct": "Yes! Environmental decisions should be based primarily on scientific evidence, but values, ethics, and community input also matter in making responsible choices.",
            "feedback_incorrect": "Environmental decisions work best when they are based on scientific evidence combined with ethical reasoning. Evidence tells us what will happen; ethics helps us decide what should happen. Both matter."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the model, what THREE factors determine whether an environmental intervention is justified?",
            "choices": {
                "A": "Cost, speed, and popularity",
                "B": "Problem severity, solution risk, and available evidence",
                "C": "Location, season, and weather",
                "D": "Number of scientists, amount of funding, and public opinion"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model showed that problem severity, solution risk, and available evidence are the three key inputs that determine whether intervention makes sense.",
            "feedback_incorrect": "The model identified three critical inputs: how severe the problem is, how risky the proposed solution is, and how strong the scientific evidence supporting the solution is. All three must be considered together."
        },
        {
            "question": "What did the model show when problem severity was high, solution risk was high, and evidence was moderate?",
            "choices": {
                "A": "The answer was clearly 'yes, intervene'",
                "B": "The answer was clearly 'no, do not intervene'",
                "C": "It was a hard call because the factors conflicted with each other",
                "D": "The model could not produce any result"
            },
            "correct": "C",
            "feedback_correct": "Yes! This was a 'hard call' scenario. The severe problem pushes toward action, but the high risk and only moderate evidence create genuine uncertainty.",
            "feedback_incorrect": "When factors conflict (severe problem pushing for action, high risk pushing against it, moderate evidence), the model shows a 'hard call.' Most real-world ethical decisions fall in this gray area where the answer is not obvious."
        },
        {
            "question": "According to the model, what is the main limitation of using computational models for ethical decisions?",
            "choices": {
                "A": "Models are too slow to be useful",
                "B": "Models can show all the factors clearly but cannot tell us what is morally right",
                "C": "Models always give wrong answers about ethics",
                "D": "Models can only work with environmental problems"
            },
            "correct": "B",
            "feedback_correct": "Correct! Models are powerful tools for seeing all the factors clearly, but they cannot determine what is morally right. That judgment requires human reasoning and ethical values.",
            "feedback_incorrect": "Models help us see the factors and tradeoffs clearly, but they cannot make moral judgments for us. Science tells us what WILL happen; ethics tells us what SHOULD happen. Models inform ethical decisions but cannot replace human moral reasoning."
        },
        {
            "question": "What did the model reveal about when ethical decisions are easiest vs. hardest?",
            "choices": {
                "A": "Ethical decisions are always equally difficult",
                "B": "Decisions are easy when all factors align (severe problem, safe fix, strong evidence) and hard when factors conflict",
                "C": "Decisions are easy when you have a lot of money",
                "D": "Decisions are hard only when you do not have a computer model"
            },
            "correct": "B",
            "feedback_correct": "That is right! Ethical decisions are straightforward when all factors point the same direction, but they become genuinely difficult when factors pull in opposing directions.",
            "feedback_incorrect": "The model showed that decisions are easy when all factors align (severe problem, safe solution, strong evidence). They become truly difficult when factors conflict, like a very severe problem with a very risky solution. Most real-world decisions fall in the 'hard call' zone."
        }
    ]
}

# =============================================================================
# LEVEL 2 LESSONS (Advanced)
# =============================================================================

L2_01_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is a cascade effect in nature?",
            "choices": {
                "A": "When water flows down a waterfall",
                "B": "When a change in one part of a system triggers changes in many other parts",
                "C": "When animals migrate in a long line",
                "D": "When trees grow taller each year"
            },
            "correct": "B",
            "feedback_correct": "Correct! A cascade effect is when a change in one part of a system triggers a chain of changes in many other connected parts, like dominoes falling.",
            "feedback_incorrect": "A cascade effect happens when a change in one part of a system triggers changes in many other parts. Think of it like dominoes falling: one change sets off the next, which sets off the next."
        },
        {
            "question": "What is a wetland?",
            "choices": {
                "A": "An area that is always covered by deep ocean water",
                "B": "An area of land saturated with water that supports unique plants and animals",
                "C": "A dry desert with no water at all",
                "D": "A swimming pool for wildlife"
            },
            "correct": "B",
            "feedback_correct": "Yes! A wetland is an area of land saturated with water. Wetlands support unique communities of plants and animals that thrive in wet conditions.",
            "feedback_incorrect": "A wetland is an area where land meets water. The ground is saturated with moisture, creating conditions that support unique plants (like cattails and sedges) and animals (like herons, frogs, and fish) that thrive in wet environments."
        },
        {
            "question": "How many species do you think a beaver pond can support?",
            "choices": {
                "A": "Only beavers live in beaver ponds",
                "B": "Maybe 5 to 10 other species",
                "C": "Hundreds of different species of plants, insects, fish, birds, and mammals",
                "D": "No species can live in a beaver pond because the dam blocks them"
            },
            "correct": "C",
            "feedback_correct": "Correct! Beaver ponds can support hundreds of species. The wetland habitat they create is one of the most biodiverse ecosystems in nature.",
            "feedback_incorrect": "Beaver ponds are incredibly rich habitats. They support hundreds of species including fish, amphibians, insects, birds, mammals, and diverse plants. The wetland created by a single beaver dam can become one of the most biodiverse places in the landscape."
        },
        {
            "question": "What happens to a beaver pond if the beavers leave and stop maintaining the dam?",
            "choices": {
                "A": "The pond stays exactly the same forever",
                "B": "The dam eventually breaks down, the pond drains, and the habitat changes",
                "C": "Other animals repair the dam and keep the pond",
                "D": "The pond gets deeper and turns into a lake"
            },
            "correct": "B",
            "feedback_correct": "Yes! Without beavers maintaining the dam, it eventually breaks down. The pond drains, the wetland dries up, and the habitat changes dramatically.",
            "feedback_incorrect": "Without beavers maintaining the dam, it deteriorates over time. Water breaks through, the pond drains, and the wetland gradually dries up. All the species that depended on the pond habitat are affected."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the 7-component model, what is the correct cascade chain from beaver activity to biodiversity?",
            "choices": {
                "A": "Beavers create biodiversity directly without any steps in between",
                "B": "Beavers + Trees build Dam, Dam raises Water Level, Water creates Wetland Area, Wetland supports Biodiversity",
                "C": "Rainfall creates beavers, beavers create trees, trees create water",
                "D": "Biodiversity creates beavers, which then create dams"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model showed the full cascade chain: Beavers + Trees build a Dam, the Dam raises the Water Level, higher Water creates Wetland Area, and Wetland Area supports Biodiversity.",
            "feedback_incorrect": "The model revealed a step-by-step cascade: Beaver Population + Tree Availability determine Dam Size, Dam Size determines Water Level, Water Level determines Wetland Area, and Wetland Area determines Biodiversity. Each step depends on the one before it."
        },
        {
            "question": "What did the model show happens during a drought year when beavers and trees are present?",
            "choices": {
                "A": "The ecosystem collapses completely because there is no rain",
                "B": "Beaver dams can buffer against drought by storing water, but they cannot create water from nothing",
                "C": "Drought has no effect on beaver ecosystems",
                "D": "Beavers leave the area immediately when drought begins"
            },
            "correct": "B",
            "feedback_correct": "Yes! The model showed that beaver dams store water and can buffer against moderate drought, but they cannot create water. Extreme drought still weakens the system.",
            "feedback_incorrect": "The model demonstrated that beaver dams help during drought by storing water in the pond and surrounding wetland. This buffering effect protects the ecosystem from moderate drought. However, beaver dams cannot create water, so extreme, prolonged drought still weakens the entire cascade."
        },
        {
            "question": "According to the model, why does removing beavers affect the ENTIRE ecosystem, not just the pond?",
            "choices": {
                "A": "Because beavers eat everything in the ecosystem",
                "B": "Because every component in the cascade depends on the one before it, so removing the first link collapses all downstream components",
                "C": "Because other animals are afraid of living without beavers",
                "D": "The model showed that removing beavers only affects the pond, not other parts"
            },
            "correct": "B",
            "feedback_correct": "Correct! The cascade means each component depends on the previous one. Remove beavers and dam size drops, water level drops, wetland area shrinks, and biodiversity crashes.",
            "feedback_incorrect": "The cascade structure means each step depends on the one before it. Without beavers, there is no dam maintenance. Without the dam, water level drops. Without high water, wetlands shrink. Without wetlands, biodiversity crashes. The entire chain unravels from top to bottom."
        },
        {
            "question": "What did the deforestation scenario reveal about the relationship between trees and the beaver ecosystem?",
            "choices": {
                "A": "Trees are not important because beavers can use other materials",
                "B": "Without trees, beavers cannot build or maintain dams, breaking the entire cascade even if beaver population is high",
                "C": "Deforestation helps beavers by giving them more open space",
                "D": "Trees only matter for the appearance of the ecosystem"
            },
            "correct": "B",
            "feedback_correct": "That is right! The deforestation scenario showed that trees are an essential input. Even a large beaver population cannot maintain the ecosystem cascade without building materials.",
            "feedback_incorrect": "The model clearly showed that tree availability is critical. Without trees, beavers have no building material for their dams, regardless of how many beavers are present. This breaks the first link in the cascade and all downstream components (water level, wetland area, biodiversity) decline."
        }
    ]
}

L2_02_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What does 'fidelity' mean in engineering design?",
            "choices": {
                "A": "How much a design costs to build",
                "B": "How accurately an artificial design replicates the original natural feature",
                "C": "How fast a machine can move",
                "D": "How many people like the design"
            },
            "correct": "B",
            "feedback_correct": "Correct! Fidelity refers to how accurately an artificial design copies or replicates the original natural feature it is based on.",
            "feedback_incorrect": "In engineering, fidelity means how accurately an artificial design replicates the original. High fidelity means the design closely matches the real thing; low fidelity means it is a rough approximation."
        },
        {
            "question": "Why is it difficult to build a robot that perfectly mimics an animal?",
            "choices": {
                "A": "Animals are too small to copy",
                "B": "Every design improvement creates tradeoffs with other performance aspects",
                "C": "Robots cannot be built in animal shapes",
                "D": "Engineers are not allowed to study animals"
            },
            "correct": "B",
            "feedback_correct": "Yes! Building animal-like robots is challenging because improving one aspect (like movement accuracy) often creates tradeoffs with other aspects (like energy use or durability).",
            "feedback_incorrect": "Creating a lifelike animal robot is hard because every design choice involves tradeoffs. Making the robot move more naturally might require more energy. Using lifelike materials might reduce durability. Engineers must balance multiple competing goals."
        },
        {
            "question": "What is an iteration in the engineering design process?",
            "choices": {
                "A": "The final step where you stop working",
                "B": "A cycle of testing, evaluating, and improving a design",
                "C": "When you copy someone else's design exactly",
                "D": "When you give up on a project"
            },
            "correct": "B",
            "feedback_correct": "Correct! An iteration is one cycle of testing, evaluating results, and making improvements to a design. Good engineering involves many iterations.",
            "feedback_incorrect": "An iteration is a complete cycle of the design process: build, test, evaluate, and improve. Engineers rarely get a design right on the first try. Each iteration brings the design closer to the goal."
        },
        {
            "question": "Can a robot with the wrong basic shape be fixed by using better materials?",
            "choices": {
                "A": "Yes, better materials always fix design problems",
                "B": "No, the fundamental design must be correct first, then materials improve it",
                "C": "Materials do not matter at all in engineering",
                "D": "Only the color of the materials matters"
            },
            "correct": "B",
            "feedback_correct": "Yes! The fundamental design choice matters most. Better materials can improve a good design, but they cannot rescue a fundamentally flawed one.",
            "feedback_incorrect": "The fundamental shape and design must be correct first. No amount of expensive or high-tech materials can fix a design that copies the wrong animal feature. The basic concept must work before materials and power can enhance it."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the model, which input had the GREATEST impact on overall performance?",
            "choices": {
                "A": "Power Source, because more power always fixes everything",
                "B": "Material Choice, because expensive materials are always best",
                "C": "Animal Feature Selected, because the fundamental design choice matters more than materials or power",
                "D": "All three inputs have exactly equal impact"
            },
            "correct": "C",
            "feedback_correct": "Correct! The model showed that the fundamental design choice (which animal feature to copy) had the greatest impact. No material or power boost could fix a bad fundamental design.",
            "feedback_incorrect": "The model clearly demonstrated that selecting the right animal feature to copy is the most important decision. When the wrong feature was chosen (pointed tail instead of flat for swimming), even the best materials and maximum power could not compensate."
        },
        {
            "question": "What tradeoff did the model reveal about using lifelike materials?",
            "choices": {
                "A": "Lifelike materials had no tradeoffs and were best in every category",
                "B": "Lifelike materials reduced detection risk but increased energy use and decreased durability",
                "C": "Lifelike materials were the cheapest option available",
                "D": "Lifelike materials only affected appearance, nothing else"
            },
            "correct": "B",
            "feedback_correct": "Yes! The model showed that lifelike materials (like silicone) made the robot harder to detect as artificial, but they also increased energy use and reduced durability. This is a classic engineering tradeoff.",
            "feedback_incorrect": "Lifelike materials like silicone reduced detection risk (the robot looked more real) but came with costs: they increased energy use and decreased durability. This demonstrates that in engineering, improving one metric often worsens another."
        },
        {
            "question": "What did the model show about whether more power can overcome material limitations?",
            "choices": {
                "A": "More power completely solves all material problems",
                "B": "More power helps somewhat but creates its own problems, like heavier batteries and shorter lifespan",
                "C": "Power and materials are completely unrelated in the model",
                "D": "More power always makes performance worse"
            },
            "correct": "B",
            "feedback_correct": "Correct! More power improved some outputs but introduced new tradeoffs: heavier batteries, more heat, and shorter operational lifespan. There is no free lunch in engineering.",
            "feedback_incorrect": "The model showed that increasing power helped improve movement accuracy, but it also brought new problems: the power source was heavier, generated more heat, and reduced operational lifespan. Engineering tradeoffs mean you cannot simply add more power to solve every problem."
        },
        {
            "question": "Why are nature's designs so efficient compared to human engineering?",
            "choices": {
                "A": "Nature uses better computers than humans",
                "B": "Nature's designs have been optimized through millions of years of evolution",
                "C": "Nature does not follow the laws of physics",
                "D": "Nature's designs are not actually efficient"
            },
            "correct": "B",
            "feedback_correct": "That is right! Evolution has been testing and refining animal designs for millions of years. Only the most efficient designs survived, making them excellent models for human engineering.",
            "feedback_incorrect": "Nature's designs are efficient because evolution has been testing and selecting the best solutions for millions of years. Animals that survived had the most efficient body structures and features. This is why biomimicry is so valuable: engineers can start from solutions that have already been refined over vast timescales."
        }
    ]
}

L2_03_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is ecohydrology?",
            "choices": {
                "A": "The study of how water is used in factories",
                "B": "The study of how water movement through ecosystems affects living things, and how living things affect water movement",
                "C": "The study of how to build hydroelectric dams",
                "D": "The study of ocean currents"
            },
            "correct": "B",
            "feedback_correct": "Correct! Ecohydrology studies the two-way relationship between water movement and living organisms in ecosystems.",
            "feedback_incorrect": "Ecohydrology is the study of how water movement through ecosystems affects living things AND how living things affect water movement. It is a two-way relationship between water and life."
        },
        {
            "question": "What is groundwater?",
            "choices": {
                "A": "Water that sits on the surface of the ground",
                "B": "Water stored underground in soil and rock",
                "C": "Water that falls from the sky as rain",
                "D": "Water in rivers and streams only"
            },
            "correct": "B",
            "feedback_correct": "Yes! Groundwater is water stored underground in the spaces between soil and rock particles. It is a hidden water supply that keeps plants alive during dry periods.",
            "feedback_incorrect": "Groundwater is water stored underground in soil and rock. Unlike surface water (rivers and ponds), groundwater is hidden below the surface. Plant roots tap into groundwater to survive dry periods."
        },
        {
            "question": "Why do wildfires spread more easily during a drought?",
            "choices": {
                "A": "Because the sun is closer to Earth during drought",
                "B": "Because drought dries out vegetation, turning it into fuel that burns easily",
                "C": "Because more lightning strikes happen during drought",
                "D": "Because wind stops blowing during drought"
            },
            "correct": "B",
            "feedback_correct": "Correct! Drought dries out vegetation, reducing its moisture content. Dry vegetation burns much more easily and intensely than green, hydrated plants.",
            "feedback_incorrect": "During drought, vegetation loses moisture and dries out. Dry, dead vegetation becomes fuel that ignites easily and burns quickly. Green, hydrated plants resist fire because the water inside them must evaporate before the plant can burn."
        },
        {
            "question": "Can beavers help prevent wildfires?",
            "choices": {
                "A": "No, beavers have nothing to do with fire",
                "B": "Yes, beaver dams store water that keeps surrounding areas green and fire-resistant",
                "C": "Yes, beavers fight fires directly with water from their ponds",
                "D": "Only firefighters can prevent wildfires"
            },
            "correct": "B",
            "feedback_correct": "Yes! Research shows that beaver dams store water and raise groundwater levels, keeping nearby vegetation green and moist even during drought. These green corridors resist fire.",
            "feedback_incorrect": "Research by scientists like Dr. Emily Fairfax shows that beaver dams raise groundwater levels and keep vegetation hydrated during drought. These well-watered areas create green corridors that resist fire while surrounding dry areas burn."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the 8-component model, what is the chain from beaver dams to fire resistance?",
            "choices": {
                "A": "Beaver Dams put out fires directly with water",
                "B": "Beaver Dams raise Groundwater Level, which increases Soil Moisture, which keeps Vegetation healthy, which reduces Fire Spread Rate",
                "C": "Beaver Dams block fire from crossing rivers",
                "D": "Beaver Dams have no connection to fire in the model"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model shows the chain: Beaver Dams raise Groundwater, higher Groundwater increases Soil Moisture, moist soil keeps Vegetation healthy and green, and healthy vegetation resists Fire Spread.",
            "feedback_incorrect": "The model traces a clear chain: Beaver Dams raise the Groundwater Level by storing and spreading water. Higher Groundwater increases Soil Moisture. Moist soil keeps Vegetation healthy and hydrated. And healthy, green vegetation dramatically reduces Fire Spread Rate because wet plants do not burn easily."
        },
        {
            "question": "What happened in the model when drought was severe but beaver dams were present?",
            "choices": {
                "A": "The area burned just as badly as areas without beaver dams",
                "B": "The area near beaver dams stayed greener and more fire-resistant than areas without dams",
                "C": "The beaver dams made the drought worse",
                "D": "The model showed no difference between dammed and undammed areas during drought"
            },
            "correct": "B",
            "feedback_correct": "Yes! The model showed that even during drought, beaver-dammed areas maintained higher groundwater, soil moisture, and vegetation health than undammed areas, reducing fire spread.",
            "feedback_incorrect": "The model demonstrated that beaver-dammed areas stayed greener and more fire-resistant during drought. The stored water raised groundwater levels enough to keep vegetation hydrated while surrounding undammed areas dried out and became vulnerable to fire."
        },
        {
            "question": "What did the model show about the relationship between beaver dams and surface runoff?",
            "choices": {
                "A": "Beaver dams increase surface runoff",
                "B": "Beaver dams have no effect on runoff",
                "C": "Beaver dams reduce surface runoff by keeping more water in the landscape",
                "D": "Surface runoff is not part of the ecohydrology model"
            },
            "correct": "C",
            "feedback_correct": "Correct! The model showed that beaver dams reduce surface runoff by slowing water flow and spreading it across the floodplain, keeping more water stored in the landscape.",
            "feedback_incorrect": "Beaver dams reduce surface runoff by slowing water down and spreading it across the floodplain. Instead of rushing away across the surface, water soaks into the ground, raising the water table and staying in the landscape where it can keep vegetation hydrated."
        },
        {
            "question": "According to the extreme drought scenario, what are the limits of beaver dams as fire protection?",
            "choices": {
                "A": "Beaver dams have no limits and work perfectly in all conditions",
                "B": "Beaver dams only work when there is no drought at all",
                "C": "Beaver dams buffer against moderate drought but cannot maintain green corridors during extreme, prolonged drought with almost no precipitation",
                "D": "Beaver dams make extreme drought worse"
            },
            "correct": "C",
            "feedback_correct": "Yes! The model showed that beaver dams are powerful but have limits. They can buffer moderate drought, but extreme, prolonged drought with almost no rain eventually overwhelms even beaver-managed landscapes.",
            "feedback_incorrect": "The extreme drought scenario revealed that beaver dams have limits. They store and distribute water effectively during moderate drought, but they cannot create water from nothing. When precipitation drops to nearly zero for extended periods, even beaver-managed areas eventually lose moisture and become vulnerable to fire."
        }
    ]
}

L2_04_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is an electrode in the context of brain science?",
            "choices": {
                "A": "A type of battery",
                "B": "A tiny sensor that detects electrical activity from the brain",
                "C": "A medicine that helps the brain work better",
                "D": "A screen that displays brain images"
            },
            "correct": "B",
            "feedback_correct": "Correct! An electrode is a tiny sensor placed on or near the brain that can detect the electrical activity of nearby neurons.",
            "feedback_incorrect": "An electrode is a tiny sensor that is placed on or in the brain to detect electrical activity. Neurons communicate using electrical signals, and electrodes pick up those signals so they can be read by a computer."
        },
        {
            "question": "Why would someone need a brain-computer interface?",
            "choices": {
                "A": "To play video games faster",
                "B": "To help paralyzed patients control computers or robotic limbs with their thoughts",
                "C": "To make people smarter than everyone else",
                "D": "To read other people's minds without their permission"
            },
            "correct": "B",
            "feedback_correct": "Yes! One of the most important uses of brain-computer interfaces is helping people with paralysis control devices using their brain signals, restoring independence and movement.",
            "feedback_incorrect": "Brain-computer interfaces are being developed primarily to help people with paralysis or other conditions. By reading brain signals, a BCI can allow someone who cannot move their arms to control a robotic limb, cursor, or other device using only their thoughts."
        },
        {
            "question": "What is 'neural noise'?",
            "choices": {
                "A": "The sound your brain makes when you think",
                "B": "Random electrical activity from millions of neurons that interferes with reading specific signals",
                "C": "Loud music that makes it hard to study",
                "D": "A new type of hearing aid"
            },
            "correct": "B",
            "feedback_correct": "Correct! Neural noise is the random electrical activity from millions of neurons firing simultaneously, which creates interference when trying to read a specific brain signal.",
            "feedback_incorrect": "Neural noise is the random electrical activity produced by millions of neurons firing all the time in your brain. When you try to read one specific signal (like the intention to move your hand), all those other signals create interference, making it hard to isolate the one you want."
        },
        {
            "question": "Can the brain learn to work better with a machine over time?",
            "choices": {
                "A": "No, the brain cannot change how it sends signals",
                "B": "Yes, the brain can adapt its signals to work more effectively with a BCI system",
                "C": "Only children's brains can adapt, not adults'",
                "D": "The machine adapts, but the brain stays the same"
            },
            "correct": "B",
            "feedback_correct": "Yes! The brain has remarkable plasticity and can learn to produce cleaner, more consistent signals that a BCI can read more easily. This adaptation is a two-way process.",
            "feedback_incorrect": "The brain is remarkably adaptable. Through practice, it can learn to produce cleaner, more consistent signals that a BCI system can read more easily. This process of adaptation goes both ways: the brain learns to produce better signals, and the computer algorithms learn to interpret them better."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the 8-component model, what is the chain from stimulus to motor output?",
            "choices": {
                "A": "Stimulus goes directly to motor output with no steps in between",
                "B": "Stimulus Intensity determines Signal Strength, Electrodes capture it for Encoding Accuracy, which determines Response Time and Motor Output Precision",
                "C": "Electrode Count is the only factor that matters",
                "D": "Motor output happens randomly regardless of input"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model traces the chain: Stimulus Intensity affects Signal Strength, Electrode Count and Noise Level affect Encoding Accuracy, and Encoding Accuracy determines both Response Time and Motor Output Precision.",
            "feedback_incorrect": "The model shows a clear processing chain: Stimulus Intensity creates Signal Strength. More Electrodes and lower Noise improve Encoding Accuracy. Better Encoding produces faster Response Time and higher Motor Output Precision. The Adaptation Level improves the whole chain over time."
        },
        {
            "question": "What role does Adaptation Level play in the model?",
            "choices": {
                "A": "Adaptation has no effect on BCI performance",
                "B": "Adaptation only helps when all other conditions are perfect",
                "C": "Adaptation improves the entire system over time as the brain and computer learn to work together",
                "D": "Adaptation makes the system worse over time because the brain gets tired"
            },
            "correct": "C",
            "feedback_correct": "Yes! The model showed that adaptation is a powerful factor. Over time, the brain produces cleaner signals and the computer gets better at decoding them, improving all downstream performance measures.",
            "feedback_incorrect": "Adaptation is one of the most important findings in the model. Over repeated practice sessions, the brain learns to produce cleaner signals and the computer learns to decode them better. This partnership between biological and artificial intelligence improves the entire system's performance over time."
        },
        {
            "question": "What did the 'Noise Flood' scenario reveal?",
            "choices": {
                "A": "That noise has no effect on a well-designed BCI",
                "B": "That extreme noise degrades performance even with the best hardware, but adaptation can partially compensate",
                "C": "That noise always completely destroys BCI performance with no way to recover",
                "D": "That adding more noise actually improves signal quality"
            },
            "correct": "B",
            "feedback_correct": "Correct! The Noise Flood scenario showed that extreme noise degrades even the best hardware, but adaptation can partially compensate by helping the brain produce cleaner, more distinguishable signals.",
            "feedback_incorrect": "The Noise Flood scenario demonstrated that extreme noise weakens performance even with high-quality equipment. However, the model also showed that adaptation can partially compensate: over time, the brain learns to produce signals that stand out more against the noise, and the computer learns better filtering strategies."
        },
        {
            "question": "According to the model, what makes the best-case BCI scenario work so well?",
            "choices": {
                "A": "Only one factor needs to be optimal for peak performance",
                "B": "All three inputs must align: strong stimulus, many electrodes, and low noise, with adaptation amplifying the results over time",
                "C": "The best case only requires expensive equipment, nothing else",
                "D": "The best case works because the brain does all the work and the computer is passive"
            },
            "correct": "B",
            "feedback_correct": "That is right! Peak BCI performance requires strong stimulus (clear signals), many electrodes (accurate capture), low noise (clean environment), and adaptation (learned partnership between brain and computer).",
            "feedback_incorrect": "The best-case scenario works because all three inputs are optimal: strong stimulus intensity (clear brain signals), high electrode count (accurate capture), and low noise (minimal interference). On top of this, adaptation amplifies the results as the brain and computer learn to work together more effectively."
        }
    ]
}

L2_05_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What does it mean to restore an ecosystem?",
            "choices": {
                "A": "Building a zoo for endangered animals",
                "B": "Helping a damaged ecosystem recover through active human intervention",
                "C": "Paving over damaged land so people can use it",
                "D": "Moving all animals to a different location permanently"
            },
            "correct": "B",
            "feedback_correct": "Correct! Ecosystem restoration is the process of helping a degraded, damaged, or destroyed ecosystem recover through active human intervention like planting, monitoring, and reintroducing key species.",
            "feedback_incorrect": "Ecosystem restoration means actively helping a damaged ecosystem recover. This can include planting native vegetation, removing invasive species, reintroducing keystone species, and monitoring progress until the ecosystem can sustain itself."
        },
        {
            "question": "What is a tipping point in a system?",
            "choices": {
                "A": "The highest point in a mountain range",
                "B": "A critical threshold where a small change causes a large shift in the system",
                "C": "When a boat tips over in the water",
                "D": "The moment when a project runs out of funding"
            },
            "correct": "B",
            "feedback_correct": "Yes! A tipping point is a critical threshold where a small additional change causes a large, often dramatic shift in how the system behaves.",
            "feedback_incorrect": "A tipping point is a critical threshold in a system. Once crossed, even a small additional change can trigger a large, often irreversible shift. Think of it like pushing a ball up a hill: once it reaches the top (the tipping point), it rolls down the other side on its own."
        },
        {
            "question": "What are invasive species?",
            "choices": {
                "A": "Animals that have lived in an area for thousands of years",
                "B": "Non-native organisms that spread aggressively and outcompete native species",
                "C": "Any large predator in an ecosystem",
                "D": "Plants that grow during winter"
            },
            "correct": "B",
            "feedback_correct": "Correct! Invasive species are non-native organisms that have been introduced to an area and spread aggressively, outcompeting native species for resources.",
            "feedback_incorrect": "Invasive species are organisms that are not native to an area. When introduced (often by human activity), they can spread aggressively and outcompete native species for food, water, light, and space, disrupting the ecosystem."
        },
        {
            "question": "Why might an ecosystem fail to recover even after the original damage stops?",
            "choices": {
                "A": "Ecosystems always recover quickly once damage stops",
                "B": "The damage may have pushed the ecosystem past a point where it cannot recover without active help",
                "C": "Ecosystems never recover under any circumstances",
                "D": "Animals choose not to return to damaged areas"
            },
            "correct": "B",
            "feedback_correct": "Yes! If damage pushes an ecosystem past certain thresholds, the natural recovery processes may be too weakened to restore the system without active intervention.",
            "feedback_incorrect": "Some damage pushes ecosystems past critical thresholds. Soil may be too degraded, invasive species may have taken over, or key species may have disappeared. In these cases, the ecosystem cannot recover on its own and needs active human intervention to restart recovery."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "What is the 'self-sustaining threshold' in the model?",
            "choices": {
                "A": "The amount of money needed to start a restoration project",
                "B": "The tipping point where the ecosystem can maintain itself without continued human investment",
                "C": "The maximum number of species an ecosystem can support",
                "D": "The point where all invasive species have been removed"
            },
            "correct": "B",
            "feedback_correct": "Correct! The self-sustaining threshold is the tipping point where the reinforcing feedback loops between habitat quality and biodiversity are strong enough for the ecosystem to maintain itself without ongoing human support.",
            "feedback_incorrect": "The self-sustaining threshold is the critical tipping point where the ecosystem's internal reinforcing feedback loops (between habitat quality, native species diversity, and water quality) become strong enough to maintain recovery on their own, without continued human investment."
        },
        {
            "question": "What did the 'Early Withdrawal' scenario reveal about restoration timing?",
            "choices": {
                "A": "It does not matter when you stop investing because ecosystems always survive",
                "B": "Stopping investment before the self-sustaining threshold is reached causes the ecosystem to collapse back",
                "C": "You should always stop investing as early as possible to save money",
                "D": "Early withdrawal actually helps the ecosystem by forcing it to become independent"
            },
            "correct": "B",
            "feedback_correct": "Yes! The model showed that withdrawing funding before the self-sustaining threshold causes the ecosystem to lose its recovery momentum and collapse back toward a degraded state.",
            "feedback_incorrect": "The Early Withdrawal scenario demonstrated the most common cause of restoration failure: stopping investment before the ecosystem crosses the self-sustaining threshold. Without that continued support, the reinforcing feedback loops are too weak to maintain recovery, and the ecosystem slides back toward degradation."
        },
        {
            "question": "What reinforcing feedback loop did the model reveal between habitat quality and native species diversity?",
            "choices": {
                "A": "Higher habitat quality reduces native species diversity",
                "B": "Better habitat supports more native species, and more native species further improve habitat quality, creating accelerating recovery",
                "C": "Habitat quality and species diversity are not connected in the model",
                "D": "Native species reduce habitat quality over time"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model showed a powerful reinforcing loop: better habitat attracts and supports more native species, and those species (through soil health, pollination, water filtering) further improve habitat quality, creating a virtuous cycle.",
            "feedback_incorrect": "The model revealed a reinforcing (positive) feedback loop: higher habitat quality supports more native species, and those native species improve habitat quality through activities like soil building, water filtering, seed dispersal, and pollination. This creates accelerating recovery once the loop gets established."
        },
        {
            "question": "Why did the model show that keystone species reintroduction is a 'force multiplier' in ecosystem restoration?",
            "choices": {
                "A": "Because keystone species are physically the strongest animals",
                "B": "Because keystone species like beavers simultaneously improve multiple components (water quality AND habitat quality), accelerating the entire recovery process",
                "C": "Because keystone species eat invasive species directly",
                "D": "Because keystone species attract tourism funding"
            },
            "correct": "B",
            "feedback_correct": "That is right! The model showed that keystone species like beavers act as force multipliers because they simultaneously improve water quality and habitat quality, jumpstarting the reinforcing feedback loop and accelerating overall recovery.",
            "feedback_incorrect": "Keystone species are force multipliers because they improve multiple system components at once. Beavers, for example, build dams that improve water quality AND create wetland habitat simultaneously. This dual benefit accelerates the entire recovery process by jumpstarting the reinforcing feedback loop between habitat quality and native species diversity."
        }
    ]
}

L2_06_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What does 'algorithmic transparency' mean?",
            "choices": {
                "A": "Making a computer screen see-through",
                "B": "How clearly a technology's decision-making process can be understood and explained",
                "C": "Using clear glass to build robots",
                "D": "Keeping all technology decisions secret"
            },
            "correct": "B",
            "feedback_correct": "Correct! Algorithmic transparency means making a technology's decision-making process clear and understandable to the public so people can evaluate whether it is being used responsibly.",
            "feedback_incorrect": "Algorithmic transparency refers to how openly and clearly a technology's decision-making process can be explained. When an AI system makes a decision, transparency means people can understand WHY it made that decision and evaluate whether it was appropriate."
        },
        {
            "question": "Should a robot designed to protect wildlife be allowed to make decisions on its own without human oversight?",
            "choices": {
                "A": "Yes, robots always make better decisions than humans",
                "B": "No, robots should never be used for wildlife protection",
                "C": "It depends on the situation, and there are valid arguments on both sides",
                "D": "Only if the robot was built by a government"
            },
            "correct": "C",
            "feedback_correct": "Yes! This is a genuine ethical question with valid arguments on both sides. Autonomous systems can respond faster, but human oversight provides accountability. The answer depends on context.",
            "feedback_incorrect": "The question of robot autonomy in conservation is a real ethical debate. Autonomous systems can respond faster to threats, but they might make mistakes. Human oversight provides accountability but slows response time. The best answer depends on the specific situation, risks, and safeguards in place."
        },
        {
            "question": "What is an ethical framework?",
            "choices": {
                "A": "A set of building materials for making robots",
                "B": "A structured approach for evaluating whether an action is morally right or wrong",
                "C": "A picture frame with ethical quotes on it",
                "D": "A new programming language for computers"
            },
            "correct": "B",
            "feedback_correct": "Correct! An ethical framework is a structured approach for evaluating moral decisions. It provides principles and criteria for determining whether an action is right or wrong.",
            "feedback_incorrect": "An ethical framework provides a structured way to think about moral decisions. It includes principles, values, and criteria that help evaluate whether a particular action or technology is morally acceptable. Different ethical frameworks may lead to different conclusions about the same situation."
        },
        {
            "question": "When a new technology has both potential benefits and potential risks, who should decide whether to use it?",
            "choices": {
                "A": "Only the engineers who built it",
                "B": "Only the government",
                "C": "Multiple stakeholders including engineers, communities, scientists, and government working together",
                "D": "No one, because technology always moves forward regardless"
            },
            "correct": "C",
            "feedback_correct": "Yes! Decisions about powerful technology should involve multiple stakeholders. Engineers understand the technology, communities are affected by it, scientists evaluate the evidence, and government creates regulation.",
            "feedback_incorrect": "Complex technology decisions require input from multiple groups. Engineers understand what the technology can do, communities understand how it affects their lives, scientists evaluate the evidence, and government creates rules and oversight. No single group should make these decisions alone."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the model, what was the single strongest driver of public trust?",
            "choices": {
                "A": "Technology Capability Level",
                "B": "Ecological Crisis Severity",
                "C": "Transparency Level",
                "D": "Regulation Strictness"
            },
            "correct": "C",
            "feedback_correct": "Correct! The model showed that Transparency Level was the single strongest driver of Public Trust. Without transparency, even beneficial technology faces public opposition.",
            "feedback_incorrect": "The model clearly demonstrated that Transparency Level was the strongest driver of Public Trust. When the public can understand how a technology works and why it makes certain decisions, trust increases. Without transparency, even technology that produces good ecological results faces opposition."
        },
        {
            "question": "What did the model reveal about the relationship between Technology Capability and Unintended Consequences?",
            "choices": {
                "A": "More powerful technology has fewer unintended consequences",
                "B": "More powerful technology produces greater ecological benefits AND greater unintended consequences simultaneously",
                "C": "Technology capability has no relationship to unintended consequences",
                "D": "Only low-capability technology creates unintended consequences"
            },
            "correct": "B",
            "feedback_correct": "Yes! The model showed that technology capability is a double-edged sword. More powerful systems create greater ecological benefits but also carry a higher risk of unintended consequences.",
            "feedback_incorrect": "The model revealed that technology capability is a double-edged sword. Increasing capability simultaneously increases both ecological benefits (the good) and the risk of unintended consequences (the bad). This is why powerful technology requires stronger oversight and transparency."
        },
        {
            "question": "How did crisis severity affect the ethical calculus in the model?",
            "choices": {
                "A": "Crisis severity had no effect on ethical justification",
                "B": "Higher crisis severity shifted the ethical balance, making actions that are unjustifiable in normal times potentially necessary during emergencies",
                "C": "Crisis severity always made technology less justified",
                "D": "Only low-severity crises justified technology use"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model showed that crisis severity shifts the ethical calculus. Actions and risks that would be unacceptable during normal conditions may become necessary when a species faces imminent extinction.",
            "feedback_incorrect": "The model demonstrated that crisis severity changes what is ethically justifiable. During normal conditions, risky interventions are hard to justify. But when a species faces extinction or an ecosystem faces irreversible collapse, the urgency shifts the ethical balance toward accepting greater risks."
        },
        {
            "question": "According to the model, what combination of factors produces the highest Ethical Justification Score?",
            "choices": {
                "A": "Maximum technology with no regulation and no transparency",
                "B": "High transparency combined with moderate regulation, where both are present",
                "C": "Maximum regulation with no transparency",
                "D": "No technology use at all, regardless of the crisis"
            },
            "correct": "B",
            "feedback_correct": "That is right! The model showed that the highest ethical justification requires BOTH high transparency AND moderate regulation. Neither alone is sufficient. Too much regulation limits benefits; too little allows harm.",
            "feedback_incorrect": "The model consistently showed that the highest Ethical Justification Scores required both high transparency and moderate regulation working together. Transparency without regulation leaves too much room for harm. Regulation without transparency erodes public trust. And extreme regulation reduces ecological benefit too much. The balance of both produces the most ethically defensible outcomes."
        }
    ]
}

# =============================================================================
# COMBINED DICTIONARY FOR ALL LESSONS
# =============================================================================

ALL_QUESTIONS = {
    "NE-L1-01": L1_01_QUESTIONS,
    "NE-L1-02": L1_02_QUESTIONS,
    "NE-L1-03": L1_03_QUESTIONS,
    "NE-L1-04": L1_04_QUESTIONS,
    "NE-L1-05": L1_05_QUESTIONS,
    "NE-L1-06": L1_06_QUESTIONS,
    "NE-L2-01": L2_01_QUESTIONS,
    "NE-L2-02": L2_02_QUESTIONS,
    "NE-L2-03": L2_03_QUESTIONS,
    "NE-L2-04": L2_04_QUESTIONS,
    "NE-L2-05": L2_05_QUESTIONS,
    "NE-L2-06": L2_06_QUESTIONS,
}
