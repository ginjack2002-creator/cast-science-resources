#!/usr/bin/env python3
"""Multiple choice pre/post assessment questions for Kindergarten ModelIt! Lessons"""

# Format: Each lesson has mc_pre_assessment and mc_post_assessment lists
# Each question is a dict with: question, choices (dict), correct (letter), feedback_correct, feedback_incorrect

L01_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What happens when you let go of a ball?",
            "choices": {"A": "It falls down", "B": "It floats up", "C": "It stays in the air"},
            "correct": "A",
            "feedback_correct": "Yes! When you let go of a ball, it always falls down to the ground.",
            "feedback_incorrect": "Actually, when you let go of a ball, it falls down. Something called gravity pulls it toward the ground."
        },
        {
            "question": "If you drop a rock, which way does it go?",
            "choices": {"A": "It goes sideways", "B": "It goes up", "C": "It goes down"},
            "correct": "C",
            "feedback_correct": "That is right! A rock always falls down when you drop it.",
            "feedback_incorrect": "When you drop a rock, it goes down toward the ground. Everything falls down when you let go of it."
        },
        {
            "question": "What do you think makes things fall to the ground?",
            "choices": {"A": "The wind blows them down", "B": "Something invisible pulls them down", "C": "They want to be on the ground"},
            "correct": "B",
            "feedback_correct": "Good thinking! Something invisible called gravity pulls everything down toward the ground.",
            "feedback_incorrect": "There is an invisible force called gravity that pulls everything down toward the ground. You cannot see it, but it is always working."
        },
        {
            "question": "If you hold a toy up high and let go, what will happen?",
            "choices": {"A": "It will fly away", "B": "It will fall down", "C": "Nothing will happen"},
            "correct": "B",
            "feedback_correct": "Yes! The toy will fall down because gravity pulls it toward the ground.",
            "feedback_incorrect": "When you let go of a toy, it falls down. Gravity is always pulling things toward the ground."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "What is gravity?",
            "choices": {"A": "A push that makes things go up", "B": "A pull that makes things fall down", "C": "A sound you hear"},
            "correct": "B",
            "feedback_correct": "That is right! Gravity is a pull that makes things fall down toward the ground.",
            "feedback_incorrect": "Gravity is a pull. It pulls everything down toward the ground. That is why things always fall when you let go."
        },
        {
            "question": "When you drop a ball from HIGH up, what happens?",
            "choices": {"A": "It falls slowly", "B": "It falls faster", "C": "It does not fall at all"},
            "correct": "B",
            "feedback_correct": "Yes! Dropping from higher up makes the ball fall faster because gravity has more time to pull on it.",
            "feedback_incorrect": "When you drop a ball from higher up, it falls faster. Gravity pulls it for a longer time, so it speeds up more."
        },
        {
            "question": "In our model, which part do WE get to decide?",
            "choices": {"A": "Fall Speed", "B": "Drop Height", "C": "Gravity"},
            "correct": "B",
            "feedback_correct": "Yes! WE choose how high to hold the ball. That is the Drop Height, and it is the outside part of our model.",
            "feedback_incorrect": "Drop Height is the part we decide. We choose how high to hold the ball before letting go."
        },
        {
            "question": "Does gravity ever stop pulling on things?",
            "choices": {"A": "Yes, at night time", "B": "Yes, when things are sitting still", "C": "No, it never stops"},
            "correct": "C",
            "feedback_correct": "That is right! Gravity never stops. It is always pulling on everything, even when things are sitting on a table.",
            "feedback_incorrect": "Gravity never stops. It is always pulling on everything, all the time, day and night."
        }
    ]
}

L02_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What makes a toy car start moving?",
            "choices": {"A": "It moves by itself", "B": "Someone pushes or pulls it", "C": "It wants to move"},
            "correct": "B",
            "feedback_correct": "Yes! A toy car moves when someone pushes or pulls it. It cannot move by itself.",
            "feedback_incorrect": "A toy car cannot move by itself. It needs someone to push it or pull it to make it go."
        },
        {
            "question": "When you push a door, what happens?",
            "choices": {"A": "The door moves away from you", "B": "The door comes toward you", "C": "The door does not move"},
            "correct": "A",
            "feedback_correct": "Yes! A push moves things away from you. When you push a door, it moves away.",
            "feedback_incorrect": "When you push a door, it moves away from you. A push sends things in the direction you are pushing."
        },
        {
            "question": "What is a pull?",
            "choices": {"A": "When something moves away from you", "B": "When something comes closer to you", "C": "When something stays still"},
            "correct": "B",
            "feedback_correct": "That is right! A pull brings something closer to you, like pulling a wagon toward you.",
            "feedback_incorrect": "A pull is when you bring something closer to you. When you pull a wagon, it comes toward you."
        },
        {
            "question": "If you push a ball harder, what do you think happens?",
            "choices": {"A": "It stops right away", "B": "It goes the same distance", "C": "It goes farther"},
            "correct": "C",
            "feedback_correct": "Good thinking! A harder push makes a ball go farther across the floor.",
            "feedback_incorrect": "When you push a ball harder, it goes farther. A bigger push gives the ball more energy to keep rolling."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "What is a force?",
            "choices": {"A": "A color", "B": "A push or a pull", "C": "A kind of sound"},
            "correct": "B",
            "feedback_correct": "Yes! A force is a push or a pull. Forces make things move, stop, or change direction.",
            "feedback_incorrect": "A force is a push or a pull. Pushes and pulls are forces that make things move."
        },
        {
            "question": "When Push Strength goes UP, what happens to Distance Traveled?",
            "choices": {"A": "It goes up too", "B": "It goes down", "C": "It stays the same"},
            "correct": "A",
            "feedback_correct": "That is right! When you push harder, the car goes farther. That is a positive connection.",
            "feedback_incorrect": "When Push Strength goes up, Distance Traveled goes up too. A harder push makes the car roll farther."
        },
        {
            "question": "Why did the car go farther with a big push?",
            "choices": {"A": "The car got lighter", "B": "The strong force gave it more energy", "C": "The floor got smoother"},
            "correct": "B",
            "feedback_correct": "Yes! A strong push gives the car more energy, so it rolls farther before stopping.",
            "feedback_incorrect": "A big push gives the car more energy to keep rolling. More force means more energy, so the car travels farther."
        },
        {
            "question": "Push Strength is which part of our model?",
            "choices": {"A": "The inside part", "B": "The outside part", "C": "It is not in our model"},
            "correct": "B",
            "feedback_correct": "Yes! Push Strength is the outside part because WE decide how hard to push.",
            "feedback_incorrect": "Push Strength is the outside part of our model. We choose how hard to push, so it goes on the outside."
        }
    ]
}

L03_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "On a hot sunny day, which spot feels warmer?",
            "choices": {"A": "Under a big tree in the shade", "B": "Out in the sunshine", "C": "They feel the same"},
            "correct": "B",
            "feedback_correct": "Yes! The spot in the sunshine feels warmer because the sun heats it up.",
            "feedback_incorrect": "A spot in the sunshine feels warmer than a spot in the shade. The sun sends heat to the ground."
        },
        {
            "question": "What does the sun give us?",
            "choices": {"A": "Only light", "B": "Light and warmth", "C": "Only wind"},
            "correct": "B",
            "feedback_correct": "That is right! The sun gives us both light and warmth.",
            "feedback_incorrect": "The sun gives us light AND warmth. That is why sunny days feel warm."
        },
        {
            "question": "Why do people sit in the shade on a hot day?",
            "choices": {"A": "To get more sun", "B": "To stay cooler", "C": "To get wet"},
            "correct": "B",
            "feedback_correct": "Yes! People sit in the shade to stay cooler because shade blocks the hot sunlight.",
            "feedback_incorrect": "People sit in the shade to stay cooler. The shade blocks sunlight so it is not as hot."
        },
        {
            "question": "If you touch a sidewalk in the sun, how does it feel?",
            "choices": {"A": "Cold", "B": "Warm or hot", "C": "Wet"},
            "correct": "B",
            "feedback_correct": "Yes! A sidewalk in the sun feels warm or hot because the sun heats it up.",
            "feedback_incorrect": "A sidewalk in the sun feels warm or hot. The sunlight carries energy that heats up the sidewalk."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "When there is MORE sunlight on a spot, what happens to the temperature?",
            "choices": {"A": "It goes down", "B": "It stays the same", "C": "It goes up"},
            "correct": "C",
            "feedback_correct": "Yes! More sunlight makes the temperature go up. The sun's energy heats things up.",
            "feedback_incorrect": "When there is more sunlight, the temperature goes up. Sunlight carries energy that warms the ground."
        },
        {
            "question": "What does shade do?",
            "choices": {"A": "It makes things hotter", "B": "It blocks sunlight and keeps things cooler", "C": "It makes rain"},
            "correct": "B",
            "feedback_correct": "That is right! Shade blocks sunlight, so the spot stays cooler than a sunny spot.",
            "feedback_incorrect": "Shade blocks sunlight from reaching the ground. That is why shady spots feel cooler than sunny spots."
        },
        {
            "question": "Amount of Sunlight and Surface Temperature have what kind of connection?",
            "choices": {"A": "Positive: both go up together", "B": "Negative: one goes up, one goes down", "C": "No connection"},
            "correct": "A",
            "feedback_correct": "Yes! It is a positive connection. When sunlight goes up, temperature goes up too.",
            "feedback_incorrect": "It is a positive connection. More sunlight means higher temperature. They go up together."
        },
        {
            "question": "Which would feel hotter in the sun?",
            "choices": {"A": "A white piece of paper", "B": "A black piece of paper", "C": "They feel the same"},
            "correct": "B",
            "feedback_correct": "Yes! Dark colors soak up more sunlight and get hotter than light colors.",
            "feedback_incorrect": "A black piece of paper gets hotter in the sun because dark colors absorb more sunlight and heat up more."
        }
    ]
}

L04_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What do plants need to grow?",
            "choices": {"A": "Toys", "B": "Water and sunlight", "C": "Candy"},
            "correct": "B",
            "feedback_correct": "Yes! Plants need water and sunlight to grow big and healthy.",
            "feedback_incorrect": "Plants need water and sunlight to grow. Water and sunshine help them make food and get bigger."
        },
        {
            "question": "What happens if a plant does not get any water?",
            "choices": {"A": "It grows bigger", "B": "Nothing happens", "C": "It gets droopy and sad"},
            "correct": "C",
            "feedback_correct": "That is right! A plant without water gets droopy, wilts, and can turn brown.",
            "feedback_incorrect": "Without water, a plant gets droopy and sad. Plants need water to stay healthy and stand up tall."
        },
        {
            "question": "Where do plants get their water?",
            "choices": {"A": "From their leaves", "B": "From the sky and ground", "C": "From other plants"},
            "correct": "B",
            "feedback_correct": "Yes! Plants get water from rain and from the ground through their roots.",
            "feedback_incorrect": "Plants get water from rain falling from the sky and from the soil through their roots."
        },
        {
            "question": "Do plants need sunlight?",
            "choices": {"A": "Yes, they use it to make food", "B": "No, they only need water", "C": "No, they only need soil"},
            "correct": "A",
            "feedback_correct": "Yes! Plants use sunlight to make their own food so they can grow.",
            "feedback_incorrect": "Plants do need sunlight. They use the sun's light to make their own food inside their leaves."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "When a plant gets MORE water, what happens to Plant Growth?",
            "choices": {"A": "It grows less", "B": "It grows more", "C": "It does not change"},
            "correct": "B",
            "feedback_correct": "Yes! More water helps the plant grow bigger and taller. Water carries nutrients through the plant.",
            "feedback_incorrect": "When a plant gets more water, it grows more. Water carries nutrients and helps the plant make food."
        },
        {
            "question": "What are nutrients?",
            "choices": {"A": "Bugs that live in the soil", "B": "Good things in water and soil that help plants grow", "C": "The color of the leaves"},
            "correct": "B",
            "feedback_correct": "That is right! Nutrients are good things in water and soil. They are like food for the plant.",
            "feedback_incorrect": "Nutrients are good things found in water and soil that help plants grow. They are like food for the plant."
        },
        {
            "question": "How does water get from the soil to the top of the plant?",
            "choices": {"A": "It jumps up", "B": "The roots suck it up like a straw", "C": "Someone pours it on the leaves"},
            "correct": "B",
            "feedback_correct": "Yes! The roots suck up water from the soil and send it all through the plant, like a straw.",
            "feedback_incorrect": "The plant's roots suck up water from the soil, like a straw. The water travels up through the stem to the leaves."
        },
        {
            "question": "In our model, Amount of Water is the outside part. Why?",
            "choices": {"A": "Because the plant decides how much water it gets", "B": "Because WE decide how much water to give the plant", "C": "Because water is always the same"},
            "correct": "B",
            "feedback_correct": "Yes! WE decide how much water to give the plant, so Amount of Water is the outside part of our model.",
            "feedback_incorrect": "Amount of Water is outside because WE choose how much to water the plant. We control that part."
        }
    ]
}

L05_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Where does a fish live?",
            "choices": {"A": "In a tree", "B": "In the water", "C": "In the desert"},
            "correct": "B",
            "feedback_correct": "Yes! Fish live in the water because that is where they can breathe and find food.",
            "feedback_incorrect": "Fish live in the water. They need water to breathe through their gills and to find food."
        },
        {
            "question": "What do animals need to stay alive?",
            "choices": {"A": "Toys and games", "B": "Food, water, and a safe place", "C": "Only sunshine"},
            "correct": "B",
            "feedback_correct": "Yes! Animals need food to eat, water to drink, and a safe place to live.",
            "feedback_incorrect": "Animals need food, water, and a safe place called a shelter. These things help them stay alive."
        },
        {
            "question": "Why can a polar bear live in the cold snow?",
            "choices": {"A": "It has thick fur to keep warm", "B": "It does not like the cold", "C": "It lives inside a house"},
            "correct": "A",
            "feedback_correct": "Yes! Polar bears have thick fur that keeps them warm in the cold, snowy Arctic.",
            "feedback_incorrect": "Polar bears have thick fur that helps them stay warm. Their bodies are built for the cold, snowy place where they live."
        },
        {
            "question": "If a pond has lots of fish, how many ducks can eat there?",
            "choices": {"A": "No ducks", "B": "Only one duck", "C": "Many ducks"},
            "correct": "C",
            "feedback_correct": "Yes! If there are lots of fish to eat, many ducks can live at that pond.",
            "feedback_incorrect": "When there are lots of fish, many ducks can eat there. More food means more animals can live in that place."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "What is a habitat?",
            "choices": {"A": "A type of animal", "B": "The place where an animal lives that has what it needs", "C": "A kind of food"},
            "correct": "B",
            "feedback_correct": "Yes! A habitat is the place where an animal lives. It has the food, water, and shelter the animal needs.",
            "feedback_incorrect": "A habitat is an animal's home. It gives the animal food, water, and a safe place to live."
        },
        {
            "question": "When there is MORE food in a habitat, what happens to the Number of Animals?",
            "choices": {"A": "It goes down", "B": "It stays the same", "C": "It goes up"},
            "correct": "C",
            "feedback_correct": "Yes! More food means more animals can live there. That is a positive connection.",
            "feedback_incorrect": "When there is more food, more animals can live in that habitat. More food supports more animals."
        },
        {
            "question": "What is a shelter?",
            "choices": {"A": "A type of food for animals", "B": "A safe place where an animal can hide and rest", "C": "The water in a pond"},
            "correct": "B",
            "feedback_correct": "That is right! A shelter is a safe place where an animal can hide, rest, and stay warm or cool.",
            "feedback_incorrect": "A shelter is a safe place for an animal. It is where they hide from danger, rest, and stay warm or cool."
        },
        {
            "question": "What happens when food runs out in a habitat?",
            "choices": {"A": "More animals come", "B": "Animals have to leave or there are fewer of them", "C": "Nothing changes"},
            "correct": "B",
            "feedback_correct": "Yes! When food runs out, animals have to move to find a new home or fewer animals can survive there.",
            "feedback_incorrect": "When food is gone, animals must find a new place to live. Without food, fewer animals can stay in that habitat."
        }
    ]
}

L06_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is the weather like when the sun is shining and there are no clouds?",
            "choices": {"A": "Rainy", "B": "Sunny", "C": "Snowy"},
            "correct": "B",
            "feedback_correct": "Yes! When the sun is shining with no clouds, the weather is sunny.",
            "feedback_incorrect": "When the sun is out and there are no clouds, we call the weather sunny. The sun shines bright."
        },
        {
            "question": "What do clouds look like in the sky?",
            "choices": {"A": "Like white or gray fluffy shapes", "B": "Like stars", "C": "Like rainbows"},
            "correct": "A",
            "feedback_correct": "Yes! Clouds look like white or gray fluffy shapes floating in the sky.",
            "feedback_incorrect": "Clouds are white or gray fluffy shapes in the sky. They can be big and puffy or thin and wispy."
        },
        {
            "question": "Can the weather change from one day to the next?",
            "choices": {"A": "No, it is always the same", "B": "Yes, it can be different every day", "C": "Only in winter"},
            "correct": "B",
            "feedback_correct": "Yes! The weather can be different every day. It might be sunny today and rainy tomorrow.",
            "feedback_incorrect": "Weather changes from day to day. One day might be sunny and the next might be cloudy or rainy."
        },
        {
            "question": "When big dark clouds fill the sky, what might happen?",
            "choices": {"A": "It will get very hot", "B": "It might rain", "C": "The clouds will go away quickly"},
            "correct": "B",
            "feedback_correct": "Yes! Dark clouds often mean rain is coming. The clouds are full of water.",
            "feedback_incorrect": "When dark clouds fill the sky, it often means rain is coming. Dark clouds hold lots of water."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "When there are MORE clouds, what happens to the Amount of Sunshine?",
            "choices": {"A": "It goes up", "B": "It goes down", "C": "It stays the same"},
            "correct": "B",
            "feedback_correct": "Yes! More clouds means less sunshine. The clouds block the sunlight. That is a negative connection.",
            "feedback_incorrect": "When clouds go up, sunshine goes down. Clouds block the sun's light from reaching the ground."
        },
        {
            "question": "What kind of connection do Number of Clouds and Amount of Sunshine have?",
            "choices": {"A": "Positive: they go the same way", "B": "Negative: one goes up, the other goes down", "C": "They are not connected"},
            "correct": "B",
            "feedback_correct": "Yes! It is a negative connection. When clouds go up, sunshine goes down. They go in opposite directions.",
            "feedback_incorrect": "It is a negative connection. More clouds means less sunshine. When one goes up, the other goes down."
        },
        {
            "question": "What is a pattern?",
            "choices": {"A": "Something that happens only once", "B": "Something that happens the same way again and again", "C": "A type of cloud"},
            "correct": "B",
            "feedback_correct": "Yes! A pattern is something that happens the same way again and again, like sunny weeks in summer.",
            "feedback_incorrect": "A pattern is something that repeats. In weather, we might see patterns like sunny days followed by rainy days."
        },
        {
            "question": "Why is it dimmer and cooler when the sky is full of clouds?",
            "choices": {"A": "The sun turned off", "B": "The clouds block the sunlight", "C": "The ground is wet"},
            "correct": "B",
            "feedback_correct": "Yes! Clouds block the sunlight like a big blanket in the sky, making it dimmer and cooler below.",
            "feedback_incorrect": "The sun is still shining, but the clouds block the light from reaching us. That is why it is dimmer and cooler."
        }
    ]
}

L07_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is a flood?",
            "choices": {"A": "When the sun comes out", "B": "When too much water covers the ground", "C": "When it snows"},
            "correct": "B",
            "feedback_correct": "Yes! A flood is when too much water covers land that is usually dry.",
            "feedback_incorrect": "A flood happens when too much water covers the ground. Water gets so deep it covers roads and yards."
        },
        {
            "question": "What causes a flood?",
            "choices": {"A": "Too much sunshine", "B": "Too much wind", "C": "Too much rain"},
            "correct": "C",
            "feedback_correct": "Yes! Too much rain is the most common cause of floods. The ground cannot soak up all the water.",
            "feedback_incorrect": "Floods usually happen when too much rain falls. The water has nowhere to go, so it spreads out and covers the ground."
        },
        {
            "question": "Can people do anything to stop water from flooding?",
            "choices": {"A": "No, we cannot do anything", "B": "Yes, we can build walls to block the water", "C": "Yes, we can make the rain stop"},
            "correct": "B",
            "feedback_correct": "Yes! People can build walls, sandbags, and other barriers to block flood water.",
            "feedback_incorrect": "People cannot stop the rain, but they CAN build walls and barriers to block the water from reaching homes."
        },
        {
            "question": "What happens after a big rainstorm?",
            "choices": {"A": "The ground gets very dry", "B": "Big puddles and standing water appear", "C": "The sky gets sunny right away"},
            "correct": "B",
            "feedback_correct": "Yes! After a big rainstorm, there are big puddles and lots of water on the ground.",
            "feedback_incorrect": "After a big rainstorm, water collects on the ground as puddles. If there is too much water, it can become a flood."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "When the Amount of Rain goes UP, what happens to the Flood Level?",
            "choices": {"A": "It goes down", "B": "It goes up", "C": "It stays the same"},
            "correct": "B",
            "feedback_correct": "Yes! More rain means the flood level gets higher. That is a positive connection.",
            "feedback_incorrect": "When more rain falls, the flood level goes up. More water falls than the ground can soak up."
        },
        {
            "question": "What is a barrier?",
            "choices": {"A": "Something that makes more rain", "B": "Something that blocks water from going where it should not", "C": "A type of cloud"},
            "correct": "B",
            "feedback_correct": "Yes! A barrier blocks or stops water from going where it should not go, like toward homes.",
            "feedback_incorrect": "A barrier is something that blocks water. Sandbags and walls are barriers that stop flood water from reaching houses."
        },
        {
            "question": "What can people build to protect homes from floods?",
            "choices": {"A": "More windows", "B": "Walls, sandbags, and levees", "C": "Taller roofs"},
            "correct": "B",
            "feedback_correct": "Yes! People build walls, sandbags, and levees to block flood water and keep homes safe.",
            "feedback_incorrect": "Walls, sandbags, and levees are barriers that block flood water. Engineers design these to protect people."
        },
        {
            "question": "Why is it important to know when a big storm is coming?",
            "choices": {"A": "So we can play outside", "B": "So we can prepare and stay safe", "C": "So we can water the plants"},
            "correct": "B",
            "feedback_correct": "Yes! Knowing about storms helps people prepare by building barriers, moving to higher ground, and staying safe.",
            "feedback_incorrect": "Weather reports help people get ready before a big storm. They can build barriers and move to safe places."
        }
    ]
}

L08_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Where does rain come from?",
            "choices": {"A": "From the ground", "B": "From the clouds", "C": "From the ocean"},
            "correct": "B",
            "feedback_correct": "Yes! Rain falls from clouds in the sky.",
            "feedback_incorrect": "Rain falls from clouds. When clouds get very full of tiny water drops, the drops fall down as rain."
        },
        {
            "question": "What happens to a puddle on a sunny day?",
            "choices": {"A": "It gets bigger", "B": "It stays the same", "C": "It dries up and goes away"},
            "correct": "C",
            "feedback_correct": "Yes! A puddle on a sunny day dries up because the sun heats the water and it goes up into the sky.",
            "feedback_incorrect": "On a sunny day, a puddle dries up. The sun's heat turns the water into an invisible gas that floats into the sky."
        },
        {
            "question": "What are clouds made of?",
            "choices": {"A": "Cotton", "B": "Smoke", "C": "Tiny drops of water"},
            "correct": "C",
            "feedback_correct": "Yes! Clouds are made of tiny, tiny drops of water floating in the sky.",
            "feedback_incorrect": "Clouds are made of very tiny drops of water or bits of ice floating in the air. They look soft but they are actually water."
        },
        {
            "question": "Does the sun help make rain?",
            "choices": {"A": "Yes, it heats up water so it goes into the sky", "B": "No, the sun has nothing to do with rain", "C": "The sun only makes snow"},
            "correct": "A",
            "feedback_correct": "Yes! The sun heats up water, which makes it float up into the sky where it can become clouds and then rain.",
            "feedback_incorrect": "The sun does help make rain. It heats up water on the ground, the water goes up into the sky, forms clouds, and falls as rain."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "What is evaporation?",
            "choices": {"A": "When water freezes into ice", "B": "When the sun heats water and it floats up into the sky", "C": "When rain falls from clouds"},
            "correct": "B",
            "feedback_correct": "Yes! Evaporation is when the sun heats water and it turns into invisible gas that floats up into the sky.",
            "feedback_incorrect": "Evaporation is when the sun's heat turns water into an invisible gas that rises up into the sky. That is the first step of the water cycle."
        },
        {
            "question": "When the Sun's Heat goes UP, what happens to Evaporation Speed?",
            "choices": {"A": "It slows down", "B": "It speeds up", "C": "It stops"},
            "correct": "B",
            "feedback_correct": "Yes! More heat from the sun makes water evaporate faster. That is a positive connection.",
            "feedback_incorrect": "When the sun is hotter, evaporation goes faster. More heat gives water more energy to float up into the sky."
        },
        {
            "question": "What is the water cycle?",
            "choices": {"A": "Water going from the ground to the sky and back as rain, over and over", "B": "Water sitting in a glass", "C": "Water coming from a faucet"},
            "correct": "A",
            "feedback_correct": "Yes! The water cycle is water's journey. It goes up to the sky, makes clouds, and falls back as rain, over and over.",
            "feedback_incorrect": "The water cycle is the journey water takes: up to the sky (evaporation), into clouds, then back down as rain, over and over again."
        },
        {
            "question": "On a hot sunny day, a puddle dries up fast. Where did the water go?",
            "choices": {"A": "It soaked into the ground only", "B": "It turned into invisible gas and floated into the sky", "C": "It disappeared forever"},
            "correct": "B",
            "feedback_correct": "Yes! The sun heated the water and it turned into invisible gas that floated up into the sky. That is evaporation!",
            "feedback_incorrect": "The water did not disappear. The sun turned it into invisible gas (water vapor) that floated into the sky. It will become part of a cloud."
        }
    ]
}

L09_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What happens when people throw trash on the ground?",
            "choices": {"A": "It makes the Earth cleaner", "B": "It makes the Earth dirty", "C": "Nothing happens"},
            "correct": "B",
            "feedback_correct": "Yes! Throwing trash on the ground makes the Earth dirty and can hurt animals.",
            "feedback_incorrect": "Trash on the ground makes the Earth dirty. It can hurt animals and make water yucky."
        },
        {
            "question": "What does it mean to recycle?",
            "choices": {"A": "To throw things in the trash", "B": "To turn old things into new things", "C": "To buy new toys"},
            "correct": "B",
            "feedback_correct": "Yes! Recycling means turning old things into new things instead of throwing them away.",
            "feedback_incorrect": "Recycling is when old materials like paper and plastic are turned into brand new things instead of becoming trash."
        },
        {
            "question": "Can kids help take care of the Earth?",
            "choices": {"A": "No, only adults can help", "B": "Yes, kids can help too", "C": "The Earth does not need help"},
            "correct": "B",
            "feedback_correct": "Yes! Kids can help by using less, reusing things, and putting paper and plastic in recycling bins.",
            "feedback_incorrect": "Kids can absolutely help take care of the Earth. Even small things like recycling paper make a difference."
        },
        {
            "question": "Which bin should a plastic bottle go in?",
            "choices": {"A": "The trash can", "B": "The recycling bin", "C": "On the ground"},
            "correct": "B",
            "feedback_correct": "Yes! A plastic bottle should go in the recycling bin so it can be turned into something new.",
            "feedback_incorrect": "Plastic bottles go in the recycling bin. There they get cleaned and turned into new things instead of sitting in a landfill."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "When the Amount of Trash goes UP, what happens to Pollution Level?",
            "choices": {"A": "It goes down", "B": "It stays the same", "C": "It goes up"},
            "correct": "C",
            "feedback_correct": "Yes! More trash means more pollution. The Earth gets dirtier when people throw away more garbage.",
            "feedback_incorrect": "When trash goes up, pollution goes up too. More garbage makes the land, water, and air dirtier."
        },
        {
            "question": "What does REDUCE mean?",
            "choices": {"A": "To use MORE of something", "B": "To use LESS of something so we make less trash", "C": "To throw things away"},
            "correct": "B",
            "feedback_correct": "Yes! Reduce means to use less so we make less trash in the first place.",
            "feedback_incorrect": "Reduce means using less of something. When we use less, we create less trash, and that helps the Earth."
        },
        {
            "question": "How can reusing things help the Earth?",
            "choices": {"A": "It makes more trash", "B": "Every item reused is one less item in the trash", "C": "It does not help"},
            "correct": "B",
            "feedback_correct": "Yes! When we reuse something instead of throwing it away, that is one less piece of trash hurting the Earth.",
            "feedback_incorrect": "Reusing helps because every time we use something again, that is one less item going to the landfill."
        },
        {
            "question": "What are the three R's that help the Earth?",
            "choices": {"A": "Run, Rest, Read", "B": "Reduce, Reuse, Recycle", "C": "Rain, Rivers, Rocks"},
            "correct": "B",
            "feedback_correct": "Yes! Reduce, Reuse, Recycle are the three R's. They help us make less trash and keep the Earth clean.",
            "feedback_incorrect": "The three R's are Reduce (use less), Reuse (use again), and Recycle (turn old into new). They all help the Earth."
        }
    ]
}

L10_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "If you push a ball gently, what happens?",
            "choices": {"A": "It rolls fast", "B": "It rolls slowly", "C": "It does not move at all"},
            "correct": "B",
            "feedback_correct": "Yes! A gentle push makes the ball roll slowly because it is a small force.",
            "feedback_incorrect": "A gentle push makes the ball roll slowly. A small push gives the ball only a little bit of energy to move."
        },
        {
            "question": "What makes a soccer ball go really fast?",
            "choices": {"A": "A tiny tap", "B": "A really hard kick", "C": "Leaving it on the ground"},
            "correct": "B",
            "feedback_correct": "Yes! A really hard kick gives the ball lots of force, making it go really fast.",
            "feedback_incorrect": "A hard kick is a big force. More force makes the ball go faster."
        },
        {
            "question": "Can the same ball go fast AND slow?",
            "choices": {"A": "No, it always goes the same speed", "B": "Yes, it depends on how hard you push it", "C": "No, only big balls go fast"},
            "correct": "B",
            "feedback_correct": "Yes! The same ball can go fast with a big push or slow with a gentle push.",
            "feedback_incorrect": "The same ball can go fast or slow. It all depends on how hard you push it. A big push makes it fast, a small push makes it slow."
        },
        {
            "question": "What happens if you do NOT push a ball?",
            "choices": {"A": "It rolls by itself", "B": "It stays still", "C": "It goes backward"},
            "correct": "B",
            "feedback_correct": "Yes! A ball stays still unless something pushes it. It needs a force to start moving.",
            "feedback_incorrect": "A ball stays still if nothing pushes it. Things need a force, like a push, to start moving."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "When Push Force goes UP, what happens to Ball Speed?",
            "choices": {"A": "Ball Speed goes down", "B": "Ball Speed stays the same", "C": "Ball Speed goes up"},
            "correct": "C",
            "feedback_correct": "Yes! A harder push makes the ball go faster. More force means more speed. That is a positive connection.",
            "feedback_incorrect": "When Push Force goes up, Ball Speed goes up too. A bigger push gives the ball more energy to move faster."
        },
        {
            "question": "What is speed?",
            "choices": {"A": "How heavy something is", "B": "How fast something is moving", "C": "How big something is"},
            "correct": "B",
            "feedback_correct": "Yes! Speed is how fast something is moving, like slow as a turtle or fast as a cheetah.",
            "feedback_incorrect": "Speed means how fast something is moving. A slow ball has low speed, and a fast ball has high speed."
        },
        {
            "question": "Push Force is the OUTSIDE part of our model. Why?",
            "choices": {"A": "Because WE choose how hard to push", "B": "Because the ball decides the push", "C": "Because force is invisible"},
            "correct": "A",
            "feedback_correct": "Yes! WE decide how hard to push, so Push Force is the outside part. We control it.",
            "feedback_incorrect": "Push Force is outside because WE choose how hard to push. It is something we control."
        },
        {
            "question": "Why does the ball stop rolling after you push it?",
            "choices": {"A": "Gravity makes it stop", "B": "The floor rubs against the ball and slows it down", "C": "The ball gets tired"},
            "correct": "B",
            "feedback_correct": "Yes! The floor rubs against the ball. That rubbing is called friction, and it slows the ball down until it stops.",
            "feedback_incorrect": "The ball stops because the floor rubs against it. This rubbing force is called friction, and it slows moving things down."
        }
    ]
}

ALL_QUESTIONS = {
    "GK-L01": L01_QUESTIONS,
    "GK-L02": L02_QUESTIONS,
    "GK-L03": L03_QUESTIONS,
    "GK-L04": L04_QUESTIONS,
    "GK-L05": L05_QUESTIONS,
    "GK-L06": L06_QUESTIONS,
    "GK-L07": L07_QUESTIONS,
    "GK-L08": L08_QUESTIONS,
    "GK-L09": L09_QUESTIONS,
    "GK-L10": L10_QUESTIONS,
}
