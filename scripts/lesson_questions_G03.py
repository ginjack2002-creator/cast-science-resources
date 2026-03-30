#!/usr/bin/env python3
"""Multiple choice pre/post assessment questions for Grade 3 ModelIt! Lessons"""

# =============================================================================
# G03-L01: Why Do Magnets Stick?
# NGSS 3-PS2-3 — Magnetic interactions between objects not in contact
# =============================================================================
L01_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What do you think happens when you hold a magnet near a metal paperclip?",
            "choices": {
                "A": "The paperclip moves toward the magnet",
                "B": "The paperclip melts",
                "C": "The paperclip gets bigger",
                "D": "Nothing happens"
            },
            "correct": "A",
            "feedback_correct": "That is right! A magnet pulls a metal paperclip toward it using an invisible force called magnetic force.",
            "feedback_incorrect": "Think again. Magnets create a pulling force on certain metals. A paperclip is made of steel, so a magnet will pull it closer."
        },
        {
            "question": "Which of these materials do you think a magnet will stick to?",
            "choices": {
                "A": "A wooden block",
                "B": "A plastic cup",
                "C": "A steel spoon",
                "D": "A sheet of paper"
            },
            "correct": "C",
            "feedback_correct": "Great thinking! Steel is a metal that contains iron, so magnets stick to it. Magnets do not stick to wood, plastic, or paper.",
            "feedback_incorrect": "Magnets only stick to certain metals like iron and steel. A steel spoon is the only metal item in this list."
        },
        {
            "question": "Do you think a magnet can pull on a paperclip without touching it?",
            "choices": {
                "A": "No, the magnet must touch the paperclip to pull it",
                "B": "Yes, the magnet can pull the paperclip from a short distance away",
                "C": "Only if the paperclip is wet",
                "D": "Only if someone pushes the paperclip first"
            },
            "correct": "B",
            "feedback_correct": "You got it! Magnetic force is an invisible force that works through the air. A magnet can pull on metal objects even without touching them.",
            "feedback_incorrect": "Magnets actually can pull on metal objects without touching them. The invisible magnetic force reaches out through the air."
        },
        {
            "question": "A big magnet and a small magnet are both held near a paperclip. Which magnet will pull harder?",
            "choices": {
                "A": "The small magnet always pulls harder",
                "B": "Both magnets always pull the same amount",
                "C": "It depends on how strong each magnet is, not just its size",
                "D": "Neither magnet can pull on a paperclip"
            },
            "correct": "C",
            "feedback_correct": "Nice job! The strength of a magnet depends on what it is made of, not just its size. A small strong magnet can pull harder than a big weak one.",
            "feedback_incorrect": "Size does not always determine how strong a magnet is. A small magnet made of strong material can pull harder than a larger, weaker magnet."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the model, when Magnet Strength increases, what happens to Magnetic Force?",
            "choices": {
                "A": "Magnetic Force decreases",
                "B": "Magnetic Force stays the same",
                "C": "Magnetic Force increases",
                "D": "Magnetic Force disappears"
            },
            "correct": "C",
            "feedback_correct": "Correct! Magnet Strength and Magnetic Force have a positive relationship. A stronger magnet creates a stronger invisible pulling force.",
            "feedback_incorrect": "Remember the positive relationship in the model. When Magnet Strength goes up, Magnetic Force also goes up because the magnet creates a bigger invisible field."
        },
        {
            "question": "Why does a magnet stick to a steel refrigerator but NOT to a wooden door?",
            "choices": {
                "A": "The refrigerator is colder",
                "B": "Steel contains iron, which is attracted to magnets, but wood is not magnetic",
                "C": "The refrigerator is bigger",
                "D": "Wood is too heavy for magnets"
            },
            "correct": "B",
            "feedback_correct": "Exactly! Magnets only attract metals that contain iron, nickel, or cobalt. Steel has iron in it, so magnets stick to it. Wood has no magnetic metals.",
            "feedback_incorrect": "Temperature and size do not matter. Magnets only attract certain metals like iron, nickel, and cobalt. Steel has iron, but wood has no magnetic metals at all."
        },
        {
            "question": "A student tested a weak magnet and a strong magnet. The strong magnet picked up a paperclip from 3 inches away, but the weak magnet had to be 1 inch away. What does this tell us?",
            "choices": {
                "A": "Weak magnets do not work at all",
                "B": "Stronger magnets have a bigger magnetic field that reaches farther",
                "C": "The paperclip moved on its own",
                "D": "Distance does not affect magnets"
            },
            "correct": "B",
            "feedback_correct": "You got it! Stronger magnets create a bigger invisible magnetic field, so they can pull on objects from farther away.",
            "feedback_incorrect": "The strong magnet pulled from farther away because it has a larger magnetic field. Stronger magnets can reach farther with their invisible force."
        },
        {
            "question": "In the magnet model, which component is the EXTERNAL component that you can control?",
            "choices": {
                "A": "Magnetic Force",
                "B": "Attraction",
                "C": "Magnet Strength",
                "D": "Distance"
            },
            "correct": "C",
            "feedback_correct": "Right! Magnet Strength is the external component because YOU choose which magnet to use. Magnetic Force and Attraction are internal, meaning they change as a result.",
            "feedback_incorrect": "The external component is the one you set before the experiment. You choose the Magnet Strength by picking which magnet to use. The other parts change on their own inside the system."
        }
    ]
}

# =============================================================================
# G03-L02: Can You Predict the Weather?
# NGSS 3-ESS2-1 — Weather patterns and climate
# =============================================================================
L02_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "If it is usually hot in July and cold in January, what is the word for this pattern over many years?",
            "choices": {
                "A": "Weather",
                "B": "Climate",
                "C": "A storm",
                "D": "Temperature"
            },
            "correct": "B",
            "feedback_correct": "Nice thinking! Climate is the pattern of weather over a long time. Knowing that July is hot and January is cold is understanding climate.",
            "feedback_incorrect": "Weather is what is happening right now. The long-term pattern of weather over many years is called climate. Climate tells us what weather is typical for each season."
        },
        {
            "question": "Can scientists predict what the weather will be like tomorrow?",
            "choices": {
                "A": "No, weather is completely random and no one can predict it",
                "B": "Yes, but only if they guess",
                "C": "Yes, they use patterns in weather data to make predictions",
                "D": "Only animals can predict the weather"
            },
            "correct": "C",
            "feedback_correct": "That is right! Scientists called meteorologists use patterns in weather data to predict what will happen next. Weather is not random.",
            "feedback_incorrect": "Weather follows patterns that repeat over time. Meteorologists collect data on temperature, clouds, and rain, then use those patterns to make predictions."
        },
        {
            "question": "What tool do you think measures how hot or cold the air is?",
            "choices": {
                "A": "A ruler",
                "B": "A thermometer",
                "C": "A magnifying glass",
                "D": "A clock"
            },
            "correct": "B",
            "feedback_correct": "Correct! A thermometer measures temperature, which tells us how hot or cold the air is.",
            "feedback_incorrect": "A thermometer is the tool that measures temperature. It shows us how hot or cold the air is using degrees."
        },
        {
            "question": "What do you think precipitation means?",
            "choices": {
                "A": "How fast the wind blows",
                "B": "How bright the sun is",
                "C": "Water that falls from the sky, like rain or snow",
                "D": "How many clouds are in the sky"
            },
            "correct": "C",
            "feedback_correct": "You got it! Precipitation is any water that falls from the sky. This includes rain, snow, sleet, and hail.",
            "feedback_incorrect": "Precipitation is the science word for water that falls from the sky. Rain, snow, sleet, and hail are all types of precipitation."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the weather model, when Temperature increases, what happens to Cloud Cover?",
            "choices": {
                "A": "Cloud Cover always decreases to zero",
                "B": "Cloud Cover can increase because warm air causes more water to evaporate and form clouds",
                "C": "Cloud Cover is not connected to Temperature at all",
                "D": "Clouds disappear when it is warm"
            },
            "correct": "B",
            "feedback_correct": "Correct! When temperature rises, more water evaporates into the air, which can build up into clouds, especially during summer afternoons.",
            "feedback_incorrect": "In the model, Temperature and Cloud Cover have a positive relationship. Warmer air causes more water to evaporate, which can form more clouds."
        },
        {
            "question": "A student collected temperature data for a full year. She found that June, July, and August were always the hottest months. What did she discover?",
            "choices": {
                "A": "A weather event",
                "B": "A seasonal pattern in climate data",
                "C": "A random coincidence",
                "D": "A mistake in her data"
            },
            "correct": "B",
            "feedback_correct": "Exactly! She found a seasonal pattern. Climate is made of these repeating patterns. Summer months are typically the hottest year after year.",
            "feedback_incorrect": "When the same months are hot every year, that is a seasonal pattern, not a coincidence. Climate is the long-term pattern of weather, and seasons create the biggest patterns."
        },
        {
            "question": "What is the difference between weather and climate?",
            "choices": {
                "A": "Weather and climate mean the same thing",
                "B": "Weather is what is happening right now; climate is the pattern of weather over many years",
                "C": "Climate is only about rain; weather is about everything else",
                "D": "Weather lasts longer than climate"
            },
            "correct": "B",
            "feedback_correct": "You got it! Weather is what the sky and air are doing right now. Climate is the average weather pattern over 30 or more years.",
            "feedback_incorrect": "Weather is what is happening in the sky today. Climate is the BIG PICTURE pattern of weather over many years. Weather is like your mood today, climate is like your personality."
        },
        {
            "question": "In the model, Temperature is the external component. Why is it considered external?",
            "choices": {
                "A": "Because it changes every second",
                "B": "Because it is set by the sun and seasons, and it drives the weather system",
                "C": "Because it is not important to weather",
                "D": "Because students can change the temperature outside"
            },
            "correct": "B",
            "feedback_correct": "Right! Temperature is external because it is determined by the sun and seasons. We do not control it, but it drives Cloud Cover and Chance of Rain inside the system.",
            "feedback_incorrect": "An external component is something set by outside conditions that drives the system. Temperature is set by the sun and seasons, and it causes changes in Cloud Cover and Chance of Rain."
        }
    ]
}

# =============================================================================
# G03-L03: Why Do Animals Live in Groups?
# NGSS 3-LS2-1 — Animals forming groups for survival
# =============================================================================
L03_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Why do you think zebras live together in large herds instead of living alone?",
            "choices": {
                "A": "Zebras like to play games together",
                "B": "Living in a group helps protect them from predators",
                "C": "Zebras cannot find food by themselves",
                "D": "Zebras are afraid of the dark"
            },
            "correct": "B",
            "feedback_correct": "Great thinking! One of the biggest reasons animals live in groups is that it helps them stay safe from predators. More eyes watching means danger is spotted faster.",
            "feedback_incorrect": "While animals may enjoy being together, the main reason many animals live in groups is safety. A group has more eyes watching for predators, so danger is spotted faster."
        },
        {
            "question": "What is a predator?",
            "choices": {
                "A": "An animal that eats only plants",
                "B": "An animal that sleeps during the day",
                "C": "An animal that hunts and eats other animals",
                "D": "An animal that lives underground"
            },
            "correct": "C",
            "feedback_correct": "That is right! A predator is an animal that hunts and eats other animals. Lions, hawks, and wolves are examples of predators.",
            "feedback_incorrect": "A predator is an animal that hunts other animals for food. Think of a lion hunting a zebra or a hawk catching a mouse."
        },
        {
            "question": "Would you feel safer walking through a dark forest alone or with ten friends? Why?",
            "choices": {
                "A": "Alone, because friends slow you down",
                "B": "With friends, because more people can watch for danger and help each other",
                "C": "It does not matter how many people are with you",
                "D": "Alone, because a group makes too much noise"
            },
            "correct": "B",
            "feedback_correct": "Exactly! More friends means more eyes watching for danger and more people to help if something happens. Animals feel the same way!",
            "feedback_incorrect": "Most people feel safer in a group because more people can watch for danger and help each other. This is the same reason many animals live in groups."
        },
        {
            "question": "Which of these animals do you think lives in a group?",
            "choices": {
                "A": "A wolf in a pack",
                "B": "A polar bear that hunts alone",
                "C": "A tiger that lives by itself",
                "D": "An octopus at the bottom of the ocean"
            },
            "correct": "A",
            "feedback_correct": "Yes! Wolves live in groups called packs. They hunt together, protect each other, and raise their pups as a team.",
            "feedback_incorrect": "Wolves live in groups called packs. Unlike polar bears, tigers, and octopuses, wolves work as a team to hunt, protect each other, and raise their young."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the model, when Group Size increases, what happens to Predator Detection?",
            "choices": {
                "A": "Predator Detection decreases because the group is too noisy",
                "B": "Predator Detection stays the same no matter the group size",
                "C": "Predator Detection increases because more eyes are watching for danger",
                "D": "Predator Detection disappears in large groups"
            },
            "correct": "C",
            "feedback_correct": "Correct! Group Size and Predator Detection have a positive relationship. More animals in the group means more eyes watching, so predators are spotted faster.",
            "feedback_incorrect": "In the model, more animals means more eyes watching for predators. When Group Size goes up, Predator Detection goes up too. This is a positive relationship."
        },
        {
            "question": "A herd of 30 antelope spots a lion faster than one antelope standing alone. What is the BEST explanation?",
            "choices": {
                "A": "The herd is louder and scares the lion away",
                "B": "With 30 animals watching in different directions, the lion is spotted sooner",
                "C": "Antelope can only see when they are in a group",
                "D": "The lion is afraid of large numbers"
            },
            "correct": "B",
            "feedback_correct": "You got it! With 30 animals watching in different directions, there is a much better chance that at least one will spot the lion early and warn the others.",
            "feedback_incorrect": "The key idea is that 30 pairs of eyes watching in different directions will spot danger faster than just one. When one animal sees the lion, it warns everyone else."
        },
        {
            "question": "What does 'safety in numbers' mean for animal groups?",
            "choices": {
                "A": "Animals in groups can count higher than animals alone",
                "B": "Being in a bigger group makes each individual animal safer because predators are detected faster and each animal is less likely to be caught",
                "C": "Groups of animals are never attacked by predators",
                "D": "Numbers are safe but letters are dangerous"
            },
            "correct": "B",
            "feedback_correct": "Exactly! Safety in numbers means that a bigger group detects predators faster AND each individual has a smaller chance of being the one caught. Both factors help animals survive.",
            "feedback_incorrect": "Safety in numbers means being in a bigger group makes each animal safer. More watchers spot danger faster, and each individual animal has a smaller chance of being the one a predator catches."
        },
        {
            "question": "Which component in the animal group model is EXTERNAL?",
            "choices": {
                "A": "Predator Detection",
                "B": "Survival Rate",
                "C": "Group Size",
                "D": "Warning Signals"
            },
            "correct": "C",
            "feedback_correct": "Right! Group Size is external because it is the starting condition we set. Predator Detection and Survival Rate are internal components that change in response to Group Size.",
            "feedback_incorrect": "The external component is the one we control at the start. We set the Group Size, and then Predator Detection and Survival Rate change as a result inside the system."
        }
    ]
}

# =============================================================================
# G03-L04: How Do Fossils Form?
# NGSS 3-LS4-1 — Fossils as evidence of past organisms and environments
# =============================================================================
L04_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What do you think a fossil is?",
            "choices": {
                "A": "A living animal found underground",
                "B": "The preserved remains of an animal or plant from long ago, usually found in rock",
                "C": "A type of rock that looks like an animal",
                "D": "A toy dinosaur bone"
            },
            "correct": "B",
            "feedback_correct": "That is right! A fossil is the preserved remains or traces of an animal or plant that lived long ago. Most fossils are found in rock.",
            "feedback_incorrect": "A fossil is not a living thing or a toy. It is the preserved remains of an animal or plant from long ago, and fossils are usually found inside rocks."
        },
        {
            "question": "How long do you think it takes for a fossil to form?",
            "choices": {
                "A": "A few days",
                "B": "A few weeks",
                "C": "About one year",
                "D": "Millions of years"
            },
            "correct": "D",
            "feedback_correct": "You got it! Fossils take millions of years to form. The process of turning bones and shells into rock is very, very slow.",
            "feedback_incorrect": "Fossil formation is an extremely slow process. It takes millions of years for remains to be buried, pressed, and slowly turned into rock by minerals."
        },
        {
            "question": "Where do you think fossils are usually found?",
            "choices": {
                "A": "On top of mountains in the snow",
                "B": "Floating in the ocean",
                "C": "Inside layers of rock underground",
                "D": "Growing on trees"
            },
            "correct": "C",
            "feedback_correct": "Correct! Most fossils are found inside layers of sedimentary rock underground. They were buried by layers of sand and mud over millions of years.",
            "feedback_incorrect": "Fossils form when remains are buried under layers of sand and mud. Over millions of years, those layers turn to rock, so fossils are found inside layers of rock underground."
        },
        {
            "question": "What can fossils tell us about the past?",
            "choices": {
                "A": "Nothing useful",
                "B": "What animals looked like and where they lived long ago",
                "C": "What the weather will be tomorrow",
                "D": "How to make new animals"
            },
            "correct": "B",
            "feedback_correct": "Great thinking! Fossils are like clues from the past. They tell us what animals and plants looked like, what they ate, and what their environment was like millions of years ago.",
            "feedback_incorrect": "Fossils give us important clues about the past. By studying fossils, scientists can figure out what ancient animals looked like, what they ate, and what kind of environment they lived in."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the fossil model, when Burial Depth increases, what happens to Pressure?",
            "choices": {
                "A": "Pressure decreases because there is more space underground",
                "B": "Pressure increases because more layers of sediment pile on top",
                "C": "Pressure stays the same no matter how deep the burial",
                "D": "Pressure has nothing to do with burial"
            },
            "correct": "B",
            "feedback_correct": "Correct! Burial Depth and Pressure have a positive relationship. The deeper the remains are buried, the more sediment layers press down on top, creating more pressure.",
            "feedback_incorrect": "Think about what happens when more layers pile up. Each new layer adds weight. The deeper something is buried, the more layers are pressing down, so pressure increases."
        },
        {
            "question": "What is the correct order for how a fossil forms?",
            "choices": {
                "A": "Animal dies, fossil appears the next day, scientist digs it up",
                "B": "Animal dies, remains get buried by sediment, pressure builds, minerals replace bones over millions of years",
                "C": "Rocks turn into animals, then back into rocks",
                "D": "Scientists make fossils in a laboratory"
            },
            "correct": "B",
            "feedback_correct": "Exactly! First the animal dies, then its remains get buried by sediment layers. Over millions of years, pressure builds and minerals slowly replace the bones, turning them into rock.",
            "feedback_incorrect": "Fossils form in steps: an animal dies and gets buried by sediment. Over millions of years, more layers pile on (pressure), and minerals in groundwater slowly replace the bone material with rock."
        },
        {
            "question": "A scientist who studies fossils to learn about ancient life is called a:",
            "choices": {
                "A": "Meteorologist",
                "B": "Paleontologist",
                "C": "Veterinarian",
                "D": "Astronaut"
            },
            "correct": "B",
            "feedback_correct": "Right! A paleontologist is a scientist who studies fossils to learn about life on Earth millions of years ago.",
            "feedback_incorrect": "A paleontologist studies fossils and ancient life. A meteorologist studies weather, a veterinarian cares for animals, and an astronaut travels to space."
        },
        {
            "question": "Why did the shallow burial scenario produce a weaker fossil than the deep burial scenario?",
            "choices": {
                "A": "Shallow burials happen too fast",
                "B": "Shallow burial means less pressure and less mineral replacement, so fossilization is less complete",
                "C": "Deep burials are closer to the sun",
                "D": "Shallow burials use different minerals"
            },
            "correct": "B",
            "feedback_correct": "You got it! Shallow burial means fewer sediment layers, less pressure, and less mineral replacement. The deeper the burial, the more completely the remains turn into a fossil.",
            "feedback_incorrect": "With shallow burial, there are fewer layers pressing down, so there is less pressure. Less pressure means the mineral replacement process is less complete, resulting in a weaker fossil."
        }
    ]
}

# =============================================================================
# G03-L05: Why Do Some Animals Look Different?
# NGSS 3-LS3-1 — Inherited traits and variation
# =============================================================================
L05_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Why do you think puppies from the same litter can have different fur colors?",
            "choices": {
                "A": "Someone painted them different colors",
                "B": "Each puppy gets a different mix of traits from the mom and dad",
                "C": "Puppies choose their own fur color",
                "D": "All puppies from the same litter look exactly the same"
            },
            "correct": "B",
            "feedback_correct": "Great thinking! Each puppy gets a unique combination of traits from both parents. That is why siblings can look different from each other.",
            "feedback_incorrect": "Puppies get their traits from both their mom and dad. Each puppy gets a different mix, which is why brothers and sisters can have different fur colors."
        },
        {
            "question": "What is a trait?",
            "choices": {
                "A": "A type of food that animals eat",
                "B": "A feature of a living thing, like eye color, fur pattern, or height",
                "C": "A trick an animal can do",
                "D": "A place where animals live"
            },
            "correct": "B",
            "feedback_correct": "That is right! A trait is a feature or characteristic of a living thing. Eye color, hair type, height, and fur pattern are all examples of traits.",
            "feedback_incorrect": "A trait is a feature or characteristic of a living thing. Your eye color, hair type, and height are all traits. Animals have traits too, like fur color and ear shape."
        },
        {
            "question": "Which of these traits do you think you got from your parents?",
            "choices": {
                "A": "Your favorite video game",
                "B": "Your eye color",
                "C": "Your best friend's name",
                "D": "The language you speak"
            },
            "correct": "B",
            "feedback_correct": "Correct! Eye color is an inherited trait, meaning it is passed from your parents to you. Favorite games and languages are learned, not inherited.",
            "feedback_incorrect": "Eye color is inherited, meaning you got it from your parents through their genes. Things like favorite games, friends, and languages are learned, not inherited."
        },
        {
            "question": "Do you think two kittens from the same parents will look exactly the same?",
            "choices": {
                "A": "Yes, siblings always look identical",
                "B": "No, each kitten gets a different mix of traits from the parents",
                "C": "Only if they are born on the same day",
                "D": "Only if they eat the same food"
            },
            "correct": "B",
            "feedback_correct": "You got it! Each kitten gets a unique combination of the parents' traits. That is why siblings often look similar but not exactly alike.",
            "feedback_incorrect": "Siblings do not look exactly the same because each one gets a different mix of traits from the parents. Traits shuffle differently for each baby, like dealing different hands from the same deck of cards."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the model, when Parent Traits are very different from each other, what happens to Genetic Variation in the offspring?",
            "choices": {
                "A": "Genetic Variation decreases because different traits cancel out",
                "B": "Genetic Variation increases because there are more possible trait combinations",
                "C": "Genetic Variation stays the same no matter what",
                "D": "The offspring will have no traits at all"
            },
            "correct": "B",
            "feedback_correct": "Correct! When parents are very different, there are more possible combinations of traits, which creates more genetic variation in the offspring.",
            "feedback_incorrect": "When parents have very different traits, there are more possible combinations for the offspring. This means more genetic variation, with siblings looking more different from each other."
        },
        {
            "question": "What is the difference between an inherited trait and a trait caused by the environment?",
            "choices": {
                "A": "There is no difference",
                "B": "Inherited traits come from parents through genes; environmental traits are caused by surroundings like food and sunlight",
                "C": "Environmental traits are passed to babies; inherited traits are not",
                "D": "Inherited traits can be chosen; environmental traits cannot"
            },
            "correct": "B",
            "feedback_correct": "Exactly! Inherited traits (like eye color) come from your parents through genes. Environmental traits (like a scar or learned skills) are caused by your surroundings.",
            "feedback_incorrect": "Inherited traits are passed from parents to offspring through genes, like eye color or fur pattern. Environmental traits are caused by surroundings, like how much sunlight a plant gets or a scar from an injury."
        },
        {
            "question": "Why is variation in a group of animals important?",
            "choices": {
                "A": "It is not important at all",
                "B": "It makes the group look prettier",
                "C": "It helps the species survive changes in the environment because different individuals may be better suited to new conditions",
                "D": "It confuses predators so they cannot count the animals"
            },
            "correct": "C",
            "feedback_correct": "You got it! Variation is important because when the environment changes, some animals with certain traits may be better at surviving. Variation gives a species a better chance of surviving change.",
            "feedback_incorrect": "Variation helps species survive! If all animals were exactly the same and the environment changed, they might all struggle. With variation, some individuals may have traits that help them survive the new conditions."
        },
        {
            "question": "In the trait model, which component is EXTERNAL?",
            "choices": {
                "A": "Genetic Variation",
                "B": "Offspring Appearance",
                "C": "Parent Traits",
                "D": "Environment"
            },
            "correct": "C",
            "feedback_correct": "Right! Parent Traits is external because it is the starting condition. The parents' traits are set before reproduction. Genetic Variation and Offspring Appearance are internal results.",
            "feedback_incorrect": "Parent Traits is the external component because the parents' features are the starting input. Genetic Variation and Offspring Appearance are internal components that result from how the parents' traits mix."
        }
    ]
}

# =============================================================================
# G03-L06: How Does Water Shape the Land?
# NGSS 3-ESS2-1 — Weathering and erosion
# =============================================================================
L06_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "How do you think the Grand Canyon was formed?",
            "choices": {
                "A": "People dug it with shovels",
                "B": "Water from a river slowly carved it over millions of years",
                "C": "It was always there since Earth was created",
                "D": "A giant earthquake split the ground open"
            },
            "correct": "B",
            "feedback_correct": "That is right! The Grand Canyon was carved by the Colorado River over about 6 million years. Water is a powerful force that shapes the land very slowly.",
            "feedback_incorrect": "The Grand Canyon was carved by the Colorado River over millions of years. Even though water seems soft, it can carve through rock when given enough time."
        },
        {
            "question": "What do you think happens when a lot of rain falls on a dirt hill?",
            "choices": {
                "A": "Nothing changes",
                "B": "The dirt turns into rock",
                "C": "The water washes some of the dirt away",
                "D": "The hill gets taller"
            },
            "correct": "C",
            "feedback_correct": "Good thinking! When rain falls on a dirt hill, the water picks up soil and carries it downhill. This process of water moving soil is called erosion.",
            "feedback_incorrect": "When water flows over dirt, it picks up loose soil and carries it away. This is called erosion. You might have seen dirt washing away during a rainstorm."
        },
        {
            "question": "What is the word for tiny pieces of sand, mud, and dirt that settle in layers?",
            "choices": {
                "A": "Fossils",
                "B": "Magnets",
                "C": "Sediment",
                "D": "Pollution"
            },
            "correct": "C",
            "feedback_correct": "Correct! Sediment is the name for tiny pieces of sand, mud, and dirt that settle in layers on the ground or at the bottom of water.",
            "feedback_incorrect": "Tiny pieces of sand, mud, and dirt that settle in layers are called sediment. Rivers carry sediment and drop it off when the water slows down."
        },
        {
            "question": "Do you think a fast river or a slow stream moves more rocks and soil?",
            "choices": {
                "A": "A slow stream moves more because it has more time",
                "B": "They move the same amount",
                "C": "A fast river moves more because it has more power",
                "D": "Neither one can move rocks"
            },
            "correct": "C",
            "feedback_correct": "You got it! A fast river has more power to pick up and carry rocks and soil. The faster water flows, the bigger the pieces it can move.",
            "feedback_incorrect": "Faster water has more energy and more power. A fast river can pick up and move much bigger pieces of rock and soil than a slow, gentle stream."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the erosion model, when Water Flow increases, what happens to Erosion Strength?",
            "choices": {
                "A": "Erosion Strength decreases because the water spreads out",
                "B": "Erosion Strength increases because faster water can pick up and carry more material",
                "C": "Erosion Strength stays the same",
                "D": "The water stops flowing"
            },
            "correct": "B",
            "feedback_correct": "Correct! Water Flow and Erosion Strength have a positive relationship. Faster, stronger water can pick up more rocks and soil, causing more erosion.",
            "feedback_incorrect": "In the model, Water Flow and Erosion Strength have a positive relationship. When water flows faster, it has more energy to pick up and carry rocks and soil."
        },
        {
            "question": "What is the difference between weathering and erosion?",
            "choices": {
                "A": "They are the same thing",
                "B": "Weathering breaks rocks apart; erosion carries the broken pieces to a new place",
                "C": "Erosion breaks rocks; weathering carries them away",
                "D": "Weathering only happens in winter; erosion only happens in summer"
            },
            "correct": "B",
            "feedback_correct": "Exactly! Weathering is the breaking apart of rocks by water, ice, wind, or roots. Erosion is when water, wind, or ice picks up the broken pieces and carries them somewhere else.",
            "feedback_incorrect": "Weathering and erosion are two different processes. Weathering breaks rocks into smaller pieces. Then erosion picks up those pieces and carries them to a new location."
        },
        {
            "question": "When water slows down and drops the rocks and soil it was carrying, this is called:",
            "choices": {
                "A": "Weathering",
                "B": "Erosion",
                "C": "Deposition",
                "D": "Evaporation"
            },
            "correct": "C",
            "feedback_correct": "Right! Deposition is when water slows down and drops the material it was carrying. This is how deltas, beaches, and sandbars are formed.",
            "feedback_incorrect": "When moving water slows down, it drops the rocks and soil it was carrying. This process is called deposition. It is the opposite of erosion and creates new landforms like deltas and beaches."
        },
        {
            "question": "In the flooding river scenario, Erosion Strength and Land Shape Change were both very high. Why?",
            "choices": {
                "A": "Because floods happen at night",
                "B": "Because powerful flood water has enough energy to pick up large rocks and carve deep channels into the land",
                "C": "Because floods make the land flat",
                "D": "Because Land Shape Change is not connected to Erosion Strength"
            },
            "correct": "B",
            "feedback_correct": "You got it! Flooding rivers have enormous energy. The powerful water picks up large rocks and carves deep channels, causing major changes to the shape of the land.",
            "feedback_incorrect": "During a flood, the water flows very fast and has enormous energy. This strong flow picks up large amounts of rock and soil and can carve deep channels, causing big changes to the land."
        }
    ]
}

# =============================================================================
# G03-L07: What Happens When Habitats Change?
# NGSS 3-LS4-4 — Solutions for environmental change
# =============================================================================
L07_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What do you think a habitat is?",
            "choices": {
                "A": "A type of clothing animals wear",
                "B": "The natural home where an animal lives, which provides food, water, and shelter",
                "C": "A cage at the zoo",
                "D": "A type of food animals eat"
            },
            "correct": "B",
            "feedback_correct": "That is right! A habitat is the natural place where an animal or plant lives. It provides everything the organism needs: food, water, shelter, and space.",
            "feedback_incorrect": "A habitat is an animal's natural home. It provides food, water, shelter, and space. A forest, ocean, desert, and pond are all examples of habitats."
        },
        {
            "question": "What do you think happens to animals when a forest fire burns down their home?",
            "choices": {
                "A": "Nothing changes for the animals",
                "B": "The animals may lose their food and shelter, and some may not survive",
                "C": "The animals enjoy the warmth of the fire",
                "D": "New animals appear from the fire"
            },
            "correct": "B",
            "feedback_correct": "Good thinking! When a habitat is destroyed by fire, animals lose their food and shelter. Some may move to new areas, but others may not survive the change.",
            "feedback_incorrect": "When a forest burns, animals lose their homes, food, and shelter. This is a major habitat change. Some animals can move to new areas, but others struggle to survive."
        },
        {
            "question": "What does the word population mean?",
            "choices": {
                "A": "How popular an animal is",
                "B": "The number of one type of animal living in an area",
                "C": "How fast an animal can run",
                "D": "The color of an animal's fur"
            },
            "correct": "B",
            "feedback_correct": "Correct! Population is the number of one type of animal or plant living in an area. For example, if there are 50 deer in a forest, the deer population is 50.",
            "feedback_incorrect": "Population means the number of one type of animal living in an area. If a forest has 50 rabbits, the rabbit population is 50."
        },
        {
            "question": "Do you think all animals are affected the same way when their habitat changes?",
            "choices": {
                "A": "Yes, all animals react the same way",
                "B": "No, some animals can adapt better than others",
                "C": "Animals do not notice habitat changes",
                "D": "Only big animals are affected"
            },
            "correct": "B",
            "feedback_correct": "You got it! Some animals can adapt, meaning they can change what they eat, where they live, or how they behave. Others that depend on only one food or place may struggle more.",
            "feedback_incorrect": "Animals respond differently to habitat changes. Some can adapt by finding new food or shelter. Others that eat only one type of food or live in only one type of place may have a harder time surviving."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the habitat model, when Habitat Change increases, what happens to Food Availability?",
            "choices": {
                "A": "Food Availability increases because new plants grow",
                "B": "Food Availability decreases because the habitat that provided food is damaged or destroyed",
                "C": "Food Availability stays the same",
                "D": "Food Availability is not connected to Habitat Change"
            },
            "correct": "B",
            "feedback_correct": "Correct! Habitat Change and Food Availability have a negative relationship. When the habitat changes a lot (like a fire or drought), less food is available for animals.",
            "feedback_incorrect": "When a habitat is damaged or destroyed, the plants and food sources in that habitat are lost. More habitat change means less food available for animals. This is a negative relationship."
        },
        {
            "question": "Which animals are MOST at risk when their habitat changes?",
            "choices": {
                "A": "Animals that can eat many different foods and live in many places",
                "B": "Animals that eat only one type of food or live in only one type of place",
                "C": "Animals that are very large",
                "D": "Animals that are very fast"
            },
            "correct": "B",
            "feedback_correct": "Exactly! Specialized animals that depend on only one food or one type of habitat are most at risk. If their specific food or home is destroyed, they have no backup plan.",
            "feedback_incorrect": "Animals that eat only one food or live in only one place are the most at risk. If that specific food or habitat is destroyed, they cannot switch to something else. Animals that eat many foods have more options."
        },
        {
            "question": "What is one way humans can help animals when their habitat is damaged?",
            "choices": {
                "A": "Do nothing and let nature take its course",
                "B": "Build wildlife corridors so animals can move safely to healthy habitat",
                "C": "Remove all the animals from the wild",
                "D": "Make the habitat change happen faster"
            },
            "correct": "B",
            "feedback_correct": "Right! Wildlife corridors are safe paths that connect healthy habitats. They help animals move from damaged areas to places with food and shelter.",
            "feedback_incorrect": "Humans can help by creating wildlife corridors (safe paths to healthy areas), replanting forests, and protecting remaining habitats. These solutions help animals survive major habitat changes."
        },
        {
            "question": "In the major change scenario (wildfire), both Food Availability and Animal Population dropped a lot. Why did the population drop?",
            "choices": {
                "A": "The animals moved to a different planet",
                "B": "Without enough food and shelter, many animals cannot survive in the changed habitat",
                "C": "The animals got bored and left",
                "D": "Population is not connected to food"
            },
            "correct": "B",
            "feedback_correct": "You got it! When a wildfire destroys most of the forest, food and shelter are greatly reduced. Without enough resources, many animals cannot survive, so the population drops.",
            "feedback_incorrect": "Animal populations depend on food and shelter. When a wildfire destroys the forest, food and shelter decrease dramatically. Fewer resources means fewer animals can survive, so the population drops."
        }
    ]
}

# =============================================================================
# G03-L08: Can Plants Survive Without Bees?
# NGSS 3-LS2-1 — Interdependence of plants and pollinators
# =============================================================================
L08_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Why do you think bees visit flowers?",
            "choices": {
                "A": "Bees like to smell the flowers",
                "B": "Bees drink a sugary liquid called nectar from inside the flowers",
                "C": "Bees are lost and looking for their hive",
                "D": "Bees want to sting the flowers"
            },
            "correct": "B",
            "feedback_correct": "That is right! Bees visit flowers to drink nectar, a sweet liquid that flowers make. While drinking, pollen sticks to the bee's fuzzy body.",
            "feedback_incorrect": "Bees visit flowers for food. Flowers make a sweet liquid called nectar that bees drink. While the bee drinks, pollen sticks to its fuzzy body."
        },
        {
            "question": "What do you think happens to a flower's pollen when a bee visits?",
            "choices": {
                "A": "The bee eats all the pollen",
                "B": "Pollen sticks to the bee's body and gets carried to the next flower",
                "C": "The pollen falls on the ground and is wasted",
                "D": "Nothing happens to the pollen"
            },
            "correct": "B",
            "feedback_correct": "Correct! Sticky pollen hitches a ride on the bee's fuzzy body. When the bee visits the next flower, some pollen falls off and pollinates that flower.",
            "feedback_incorrect": "When a bee visits a flower, sticky pollen attaches to its fuzzy body. The bee then carries this pollen to the next flower it visits, helping the plant reproduce."
        },
        {
            "question": "What do you think would happen if there were no bees?",
            "choices": {
                "A": "Nothing would change",
                "B": "Flowers would still make fruit on their own",
                "C": "Many plants could not make fruit or seeds, and we would have less food",
                "D": "Only beeswax would disappear"
            },
            "correct": "C",
            "feedback_correct": "Great thinking! Without bees and other pollinators, many plants could not make fruit or seeds. About 75% of our food crops need pollinators.",
            "feedback_incorrect": "Bees are essential for most plants to make fruit and seeds. Without bees, many of our favorite foods like apples, strawberries, and almonds would not grow."
        },
        {
            "question": "Which of these is an example of a pollinator?",
            "choices": {
                "A": "A rock",
                "B": "A butterfly",
                "C": "A fish",
                "D": "A pencil"
            },
            "correct": "B",
            "feedback_correct": "Yes! Butterflies are pollinators, just like bees, hummingbirds, and bats. They all carry pollen from flower to flower.",
            "feedback_incorrect": "A pollinator is an animal that carries pollen between flowers. Butterflies, bees, hummingbirds, and bats are all pollinators."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the pollination model, when Pollinator Visits increase, what happens to Pollination Success?",
            "choices": {
                "A": "Pollination Success decreases because the bees get tired",
                "B": "Pollination Success increases because more flowers receive pollen",
                "C": "Pollination Success stays the same",
                "D": "Pollination Success disappears"
            },
            "correct": "B",
            "feedback_correct": "Correct! Pollinator Visits and Pollination Success have a positive relationship. More bee visits means more flowers receive pollen and can start making seeds.",
            "feedback_incorrect": "More pollinator visits means more flowers get pollen delivered to them. When Pollinator Visits go up, Pollination Success goes up too. This is a positive relationship."
        },
        {
            "question": "What does interdependence mean in the relationship between bees and flowers?",
            "choices": {
                "A": "Bees and flowers have nothing to do with each other",
                "B": "Only bees need flowers, but flowers do not need bees",
                "C": "Bees and flowers need each other to survive: bees need nectar for food, and flowers need bees to spread pollen",
                "D": "Only flowers need bees, but bees do not need flowers"
            },
            "correct": "C",
            "feedback_correct": "Exactly! Interdependence means they BOTH need each other. Bees need flower nectar for food, and flowers need bees to carry pollen so they can make seeds and fruit.",
            "feedback_incorrect": "Interdependence means two living things need EACH OTHER. Bees depend on flowers for nectar (food), and flowers depend on bees to spread their pollen. Neither can thrive without the other."
        },
        {
            "question": "In the 'No Pollinators' scenario, what happened to Fruit Production?",
            "choices": {
                "A": "Fruit Production stayed normal",
                "B": "Fruit Production increased",
                "C": "Fruit Production dropped to very low or zero because no pollen was being moved between flowers",
                "D": "Fruit Production doubled"
            },
            "correct": "C",
            "feedback_correct": "You got it! With no pollinators visiting, no pollen moves between flowers. Without pollination, plants cannot make fruit or seeds, so Fruit Production drops to near zero.",
            "feedback_incorrect": "Without pollinators, no pollen is carried from flower to flower. Plants need pollination to make fruit and seeds. With zero pollinator visits, fruit production drops to very low or zero."
        },
        {
            "question": "About what percentage of food crops depend on pollinators like bees?",
            "choices": {
                "A": "About 10%",
                "B": "About 25%",
                "C": "About 50%",
                "D": "About 75%"
            },
            "correct": "D",
            "feedback_correct": "Right! About 75% of food crops depend on pollinators. That includes apples, strawberries, almonds, chocolate, and many more foods we eat every day.",
            "feedback_incorrect": "About 75% of the food crops that humans eat depend on pollinators like bees, butterflies, and hummingbirds. Without pollinators, most of our favorite foods would disappear."
        }
    ]
}

# =============================================================================
# G03-L09: How Can We Protect Against Natural Hazards?
# NGSS 3-ESS3-1 — Engineering solutions for weather-related hazards
# =============================================================================
L09_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is a natural hazard?",
            "choices": {
                "A": "A game you play outside",
                "B": "A dangerous natural event like a flood, tornado, or earthquake",
                "C": "A type of animal",
                "D": "A safe place to play"
            },
            "correct": "B",
            "feedback_correct": "That is right! A natural hazard is a dangerous event caused by nature, like floods, tornadoes, hurricanes, and earthquakes. They can harm people and damage buildings.",
            "feedback_incorrect": "A natural hazard is a dangerous event that happens in nature. Floods, tornadoes, hurricanes, and earthquakes are all natural hazards that can cause harm to people and property."
        },
        {
            "question": "Do you think people can build things to protect themselves from floods?",
            "choices": {
                "A": "No, there is nothing we can do about floods",
                "B": "Yes, engineers can design walls, channels, and raised buildings to reduce flood damage",
                "C": "Only by building houses underground",
                "D": "Only by moving to outer space"
            },
            "correct": "B",
            "feedback_correct": "Good thinking! Engineers design special structures like levees (flood walls), channels, and raised buildings to protect people from floods.",
            "feedback_incorrect": "Engineers use science and math to design solutions for natural hazards. Levees (walls that hold back water), flood channels, and raised buildings all help reduce flood damage."
        },
        {
            "question": "What does the word engineering mean?",
            "choices": {
                "A": "Driving a train",
                "B": "Using science and math to design and build solutions to problems",
                "C": "Drawing pictures of buildings",
                "D": "Watching the weather on TV"
            },
            "correct": "B",
            "feedback_correct": "Correct! Engineering is using science and math to design and build things that solve problems. Engineers design everything from bridges to storm shelters.",
            "feedback_incorrect": "Engineering means using science and math to design and build solutions to problems. Engineers study how things work and use that knowledge to make things that help people."
        },
        {
            "question": "Which natural hazard involves strong winds that can damage buildings?",
            "choices": {
                "A": "A drought",
                "B": "A tornado",
                "C": "An earthquake",
                "D": "A flood"
            },
            "correct": "B",
            "feedback_correct": "Yes! Tornadoes are powerful spinning winds that can damage or destroy buildings, flip cars, and knock down trees.",
            "feedback_incorrect": "Tornadoes are columns of rapidly spinning air with very strong winds. They can tear apart buildings and cause major damage. Droughts are about lack of rain, earthquakes shake the ground, and floods involve water."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the natural hazards model, when Protection Design gets stronger, what happens to Damage Reduction?",
            "choices": {
                "A": "Damage Reduction decreases",
                "B": "Damage Reduction increases because stronger protection prevents more damage",
                "C": "Damage Reduction stays the same no matter the design",
                "D": "Protection Design is not connected to Damage Reduction"
            },
            "correct": "B",
            "feedback_correct": "Correct! Protection Design and Damage Reduction have a positive relationship. Stronger, better-designed protection prevents more damage from natural hazards.",
            "feedback_incorrect": "Better protection design means more damage is prevented. When Protection Design gets stronger, Damage Reduction increases. This is a positive relationship."
        },
        {
            "question": "In the 'Strong Storm, Weak Protection' scenario, what happened?",
            "choices": {
                "A": "The weak protection stopped all the damage",
                "B": "The weak protection helped a little but could not stop most of the damage from the strong storm",
                "C": "The weak protection made the storm worse",
                "D": "The strong storm had no effect"
            },
            "correct": "B",
            "feedback_correct": "Exactly! Even weak protection helps some, but a strong storm requires strong engineering. Weak protection cannot stop most of the damage from a powerful natural hazard.",
            "feedback_incorrect": "Weak protection is better than no protection, but it cannot stop a strong storm from causing major damage. Strong hazards need strong engineering solutions to prevent serious harm."
        },
        {
            "question": "What is mitigation?",
            "choices": {
                "A": "Making natural hazards happen more often",
                "B": "Actions people take to reduce the damage caused by natural hazards",
                "C": "Running away from all storms",
                "D": "Predicting when hazards will happen"
            },
            "correct": "B",
            "feedback_correct": "Right! Mitigation means taking actions to reduce damage from natural hazards. Building levees, storm shelters, and reinforced buildings are all examples of mitigation.",
            "feedback_incorrect": "Mitigation means reducing the impact of natural hazards. It includes things like building levees to hold back floodwater, designing storm shelters for tornadoes, and making buildings that can withstand earthquakes."
        },
        {
            "question": "Why do engineers study past disasters when designing new protection?",
            "choices": {
                "A": "They like reading about old storms",
                "B": "Past disasters teach them what failed and what worked, so they can design better protection for the future",
                "C": "They want to build the same things that failed before",
                "D": "Past disasters are not useful for future design"
            },
            "correct": "B",
            "feedback_correct": "You got it! Engineers study past disasters to learn what worked and what did not. This helps them design stronger, smarter protection that saves more lives in the future.",
            "feedback_incorrect": "Engineers learn from the past. By studying what failed and what survived during previous disasters, they can design better, stronger protection for the future."
        }
    ]
}

# =============================================================================
# G03-L10: Why Do Objects Move Differently?
# NGSS 3-PS2-1 — Balanced and unbalanced forces on motion
# =============================================================================
L10_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What do you think makes a ball start moving?",
            "choices": {
                "A": "The ball decides to move on its own",
                "B": "A push or a pull (a force) makes the ball move",
                "C": "The ball moves because it is round",
                "D": "Gravity makes all balls roll all the time"
            },
            "correct": "B",
            "feedback_correct": "That is right! A force is a push or pull. When you push a ball, you apply a force that makes it start moving.",
            "feedback_incorrect": "Objects need a force (a push or a pull) to start moving. A ball sits still until someone or something pushes it. That push is a force."
        },
        {
            "question": "Why do you think a ball rolling on carpet stops faster than a ball rolling on a smooth floor?",
            "choices": {
                "A": "Carpet is softer, so the ball gets sleepy",
                "B": "Carpet is rougher and creates more friction, which slows the ball down",
                "C": "Carpet makes the ball lighter",
                "D": "The ball does not like carpet"
            },
            "correct": "B",
            "feedback_correct": "Great thinking! Rough surfaces like carpet create more friction, which is a force that slows objects down. Smooth surfaces create less friction.",
            "feedback_incorrect": "Carpet is rougher than a smooth floor, so it creates more friction. Friction is a force that happens when surfaces rub together, and it slows things down."
        },
        {
            "question": "A book is sitting still on a table. What do you think is happening to the forces on the book?",
            "choices": {
                "A": "There are no forces on the book",
                "B": "The forces are balanced, so the book stays still",
                "C": "The book is being pushed in one direction",
                "D": "Only gravity is acting on the book"
            },
            "correct": "B",
            "feedback_correct": "Good thinking! The book has forces acting on it. Gravity pulls it down and the table pushes it up with equal force. Since the forces are balanced, the book stays still.",
            "feedback_incorrect": "Even though the book is not moving, forces ARE acting on it. Gravity pulls it down and the table pushes it up. These forces are equal and opposite (balanced), so the book stays still."
        },
        {
            "question": "What do you think friction is?",
            "choices": {
                "A": "A type of glue",
                "B": "A force that happens when two surfaces rub together, which slows things down",
                "C": "The color of a surface",
                "D": "A type of push that makes things go faster"
            },
            "correct": "B",
            "feedback_correct": "Correct! Friction is a force created when two surfaces rub against each other. It works against motion and slows things down.",
            "feedback_incorrect": "Friction is a force that happens when two surfaces rub together. It always works against the direction of motion, slowing things down. Rough surfaces create more friction than smooth ones."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the forces model, when Push Force increases on a smooth surface, what happens to Object Motion?",
            "choices": {
                "A": "Object Motion decreases",
                "B": "Object Motion increases because a stronger push creates a bigger unbalanced force",
                "C": "Object Motion stays the same no matter how hard you push",
                "D": "The object does not move at all"
            },
            "correct": "B",
            "feedback_correct": "Correct! A stronger push creates a bigger unbalanced force. The push easily overcomes friction on a smooth surface, so the object moves faster and farther.",
            "feedback_incorrect": "When you push harder, the force becomes more unbalanced. The push is much stronger than friction, so the object moves faster and farther. Push Force and Object Motion have a positive relationship."
        },
        {
            "question": "What is the difference between balanced and unbalanced forces?",
            "choices": {
                "A": "There is no difference",
                "B": "Balanced forces are equal and opposite so nothing changes; unbalanced forces are unequal so the object moves, speeds up, or slows down",
                "C": "Balanced forces make things move; unbalanced forces make things stop",
                "D": "Balanced forces are stronger than unbalanced forces"
            },
            "correct": "B",
            "feedback_correct": "Exactly! When forces are balanced (equal and opposite), nothing changes. When forces are unbalanced (one is stronger), the object starts moving, speeds up, slows down, or changes direction.",
            "feedback_incorrect": "Balanced forces are equal and opposite, so the object stays still or keeps moving the same way. Unbalanced forces happen when one force is stronger, causing the object to change its motion."
        },
        {
            "question": "In the 'Hard Push on Rough Carpet' scenario, why did the object not travel as far as on the smooth floor?",
            "choices": {
                "A": "The push was weaker on the carpet",
                "B": "The rough carpet created more friction, which opposed the push and slowed the object down sooner",
                "C": "The carpet made the object heavier",
                "D": "The object wanted to stop on the carpet"
            },
            "correct": "B",
            "feedback_correct": "You got it! Rough carpet creates more friction than a smooth floor. Even with the same push, more friction means the object slows down faster and does not travel as far.",
            "feedback_incorrect": "The same push was used both times, but carpet creates much more friction than a smooth floor. More friction means more force opposing the motion, so the object slows down and stops sooner."
        },
        {
            "question": "A book is sitting still on a table. Which statement correctly explains why it does not move?",
            "choices": {
                "A": "There are no forces acting on the book",
                "B": "Gravity pulls the book down and the table pushes it up with equal force, so the forces are balanced",
                "C": "The book is too heavy to move",
                "D": "Friction is holding the book in the air"
            },
            "correct": "B",
            "feedback_correct": "Right! Two forces act on the book: gravity pulls it down and the table pushes it up. These forces are equal and opposite (balanced), so the book stays perfectly still.",
            "feedback_incorrect": "Even though the book is still, forces ARE acting on it. Gravity pulls it down toward the floor, and the table pushes it up with an equal force. Because these forces are balanced, the book does not move."
        }
    ]
}

# =============================================================================
# Combined dictionary for all Grade 3 lessons
# =============================================================================
ALL_QUESTIONS = {
    "G03-L01": L01_QUESTIONS,
    "G03-L02": L02_QUESTIONS,
    "G03-L03": L03_QUESTIONS,
    "G03-L04": L04_QUESTIONS,
    "G03-L05": L05_QUESTIONS,
    "G03-L06": L06_QUESTIONS,
    "G03-L07": L07_QUESTIONS,
    "G03-L08": L08_QUESTIONS,
    "G03-L09": L09_QUESTIONS,
    "G03-L10": L10_QUESTIONS,
}
