#!/usr/bin/env python3
"""Multiple choice pre/post assessment questions for Grade 2 ModelIt! Lessons"""

# =============================================================================
# G02-L01: Can You Bend Water? (2-PS1-1)
# =============================================================================
L01_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What happens to water when you pour it from a cup into a bowl?",
            "choices": {
                "A": "The water changes shape to match the bowl",
                "B": "The water stays the same shape as the cup",
                "C": "The water disappears",
                "D": "The water gets heavier"
            },
            "correct": "A",
            "feedback_correct": "That is right! Water is a liquid, so it flows and takes the shape of whatever container it is poured into.",
            "feedback_incorrect": "Water is a liquid. Liquids do not keep their shape. When you pour water into a new container, it changes to match the new shape."
        },
        {
            "question": "Which one is a liquid?",
            "choices": {
                "A": "A wooden block",
                "B": "A rock",
                "C": "Juice",
                "D": "A crayon"
            },
            "correct": "C",
            "feedback_correct": "Yes! Juice is a liquid because it flows and takes the shape of its container, just like water.",
            "feedback_incorrect": "A liquid is something that flows and takes the shape of its container. Juice flows just like water, so juice is a liquid."
        },
        {
            "question": "If you put a toy block into a different box, what happens to the block's shape?",
            "choices": {
                "A": "It melts into the new box",
                "B": "It stays the same shape",
                "C": "It gets bigger",
                "D": "It turns into water"
            },
            "correct": "B",
            "feedback_correct": "Correct! A block is a solid. Solids keep their own shape no matter where you put them.",
            "feedback_incorrect": "A toy block is a solid. Solids keep their own shape. No matter what box you put it in, the block stays the same shape."
        },
        {
            "question": "What is matter?",
            "choices": {
                "A": "Only things that are really heavy",
                "B": "Anything you can touch or feel that takes up space",
                "C": "Only things that are hard like rocks",
                "D": "Only things you can see"
            },
            "correct": "B",
            "feedback_correct": "That is right! Matter is anything you can touch or feel that takes up space. Water, air, wood, and even tiny grains of sand are all matter.",
            "feedback_incorrect": "Matter is not just heavy things or hard things. Matter is anything that takes up space and can be touched or felt, including liquids like water and gases like air."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "You pour the same water from a tall skinny cup into a wide flat bowl. What stays the same?",
            "choices": {
                "A": "The shape of the water",
                "B": "The height of the water",
                "C": "The amount of water",
                "D": "Nothing stays the same"
            },
            "correct": "C",
            "feedback_correct": "Correct! The shape and height change, but the amount of water stays the same. You still have the same water, just in a new shape.",
            "feedback_incorrect": "When you pour water into a new container, the shape and height change, but the amount of water stays exactly the same. No water is lost or gained."
        },
        {
            "question": "In the model, Container Shape is an external component. What does that mean?",
            "choices": {
                "A": "It changes on its own",
                "B": "It is something we choose or control",
                "C": "It is always the same",
                "D": "It only works with water"
            },
            "correct": "B",
            "feedback_correct": "Yes! An external component is something we choose or control. We pick which container to use before the experiment starts.",
            "feedback_incorrect": "External components are inputs that we choose or control. We decide which container to use (tall cup, flat bowl, round jar), so Container Shape is external."
        },
        {
            "question": "What is a property of a liquid?",
            "choices": {
                "A": "It keeps its own shape no matter where you put it",
                "B": "It flows and takes the shape of its container",
                "C": "It is always blue",
                "D": "It is always cold"
            },
            "correct": "B",
            "feedback_correct": "That is right! A key property of liquids is that they flow and take the shape of whatever container they are in.",
            "feedback_incorrect": "Liquids do not keep their own shape like solids do. A property of liquids is that they flow and take the shape of whatever container holds them."
        },
        {
            "question": "When the container gets wider, what happens to the water level?",
            "choices": {
                "A": "The water level goes up higher",
                "B": "The water level stays exactly the same",
                "C": "The water level goes down lower",
                "D": "The water level disappears"
            },
            "correct": "C",
            "feedback_correct": "Correct! When the container is wider, the same amount of water spreads out more, so the water level goes down. This is a negative relationship.",
            "feedback_incorrect": "When a container is wider, the same water spreads out across a bigger bottom. Since it spreads out, the water level gets lower. The amount of water has not changed, just how it is spread out."
        }
    ]
}

# =============================================================================
# G02-L02: Where Did the Puddle Go? (2-PS1-4)
# =============================================================================
L02_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What happens to a puddle on a sunny day?",
            "choices": {
                "A": "It gets bigger",
                "B": "It gets smaller and dries up",
                "C": "It turns into ice",
                "D": "It stays the same size all day"
            },
            "correct": "B",
            "feedback_correct": "That is right! On a sunny day, the sun heats the water and the puddle gets smaller and dries up.",
            "feedback_incorrect": "If you watch a puddle on a sunny day, it gets smaller and smaller until it dries up. The sun's heat causes the water to change."
        },
        {
            "question": "Where do you think puddle water goes when it dries up?",
            "choices": {
                "A": "It soaks into outer space",
                "B": "It goes into the air",
                "C": "It disappears forever",
                "D": "It goes underground to the center of Earth"
            },
            "correct": "B",
            "feedback_correct": "Yes! When a puddle dries up, the water goes into the air as an invisible gas called water vapor.",
            "feedback_incorrect": "Puddle water does not disappear forever. It turns into an invisible gas called water vapor and goes into the air around us."
        },
        {
            "question": "Can you see water in the air?",
            "choices": {
                "A": "Yes, water is always visible",
                "B": "No, water in the air is an invisible gas",
                "C": "Only at night",
                "D": "Only when it is cold"
            },
            "correct": "B",
            "feedback_correct": "Correct! When water is a gas (water vapor), it is invisible. You cannot see it, but it is all around us in the air.",
            "feedback_incorrect": "Water vapor is an invisible gas. When water evaporates, it turns into water vapor that you cannot see, even though it is in the air all around us."
        },
        {
            "question": "What makes water get warmer?",
            "choices": {
                "A": "Darkness",
                "B": "Cold wind",
                "C": "Heat from the sun",
                "D": "More water"
            },
            "correct": "C",
            "feedback_correct": "That is right! Heat from the sun warms up water. The sun is our biggest source of heat.",
            "feedback_incorrect": "The sun sends heat energy to Earth. That heat warms up water in puddles, lakes, and oceans. Sunlight is what makes water warmer."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "What is evaporation?",
            "choices": {
                "A": "When water freezes into ice",
                "B": "When liquid water heats up and turns into water vapor",
                "C": "When water falls from the sky as rain",
                "D": "When water gets dirty"
            },
            "correct": "B",
            "feedback_correct": "Yes! Evaporation is when liquid water heats up and turns into an invisible gas called water vapor.",
            "feedback_incorrect": "Evaporation is the process where liquid water gets enough heat energy to turn into water vapor, an invisible gas. It is how puddles dry up."
        },
        {
            "question": "What is condensation?",
            "choices": {
                "A": "When water vapor cools down and turns back into liquid drops",
                "B": "When water turns into ice",
                "C": "When water gets very hot",
                "D": "When water goes underground"
            },
            "correct": "A",
            "feedback_correct": "Correct! Condensation is when water vapor cools down and turns back into tiny drops of liquid water, like on a cold glass.",
            "feedback_incorrect": "Condensation is the opposite of evaporation. When water vapor cools down, it turns back into tiny liquid water drops. You can see this on the outside of a cold glass on a warm day."
        },
        {
            "question": "Why does a puddle dry up faster on a hot sunny day than on a cloudy day?",
            "choices": {
                "A": "Because the ground eats the water",
                "B": "Because more sun heat makes water evaporate faster",
                "C": "Because the puddle is scared of the sun",
                "D": "Because clouds add more water to the puddle"
            },
            "correct": "B",
            "feedback_correct": "That is right! More heat from the sun gives the water more energy to evaporate. Hot sunny days speed up evaporation.",
            "feedback_incorrect": "The sun provides heat energy. More heat makes water evaporate faster. On a hot sunny day, the puddle gets lots of heat, so the water turns into vapor quickly and the puddle shrinks fast."
        },
        {
            "question": "Is evaporation a reversible change?",
            "choices": {
                "A": "No, once water evaporates it is gone forever",
                "B": "Yes, water vapor can cool down and turn back into liquid water",
                "C": "No, water can only go one direction",
                "D": "Yes, but only in winter"
            },
            "correct": "B",
            "feedback_correct": "Correct! Evaporation is reversible. Water can turn from liquid to gas (evaporation) and back from gas to liquid (condensation) over and over again.",
            "feedback_incorrect": "Evaporation IS reversible. Water vapor can cool down and turn back into liquid water through condensation. The water goes from liquid to gas and back to liquid, again and again."
        }
    ]
}

# =============================================================================
# G02-L03: Why Do Some Seeds Travel Far? (2-LS2-2)
# =============================================================================
L03_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "How do seeds get to new places if plants cannot walk?",
            "choices": {
                "A": "Seeds can only grow right under the parent plant",
                "B": "People must plant every seed by hand",
                "C": "Wind, water, and animals can carry seeds to new places",
                "D": "Seeds walk to new places when nobody is watching"
            },
            "correct": "C",
            "feedback_correct": "That is right! Wind, water, and animals are all ways seeds travel to new places, even though the parent plant cannot move.",
            "feedback_incorrect": "Plants cannot walk, but seeds have amazing ways to travel. Wind blows fluffy seeds, water carries floating seeds, and animals carry seeds on their fur or in their bellies."
        },
        {
            "question": "What happens when you blow on a dandelion puff?",
            "choices": {
                "A": "Nothing happens",
                "B": "The seeds float away in the air",
                "C": "The seeds get heavier",
                "D": "The flower grows bigger"
            },
            "correct": "B",
            "feedback_correct": "Yes! Dandelion seeds have fluffy tops that catch the air, so when you blow on them, they float away like tiny parachutes.",
            "feedback_incorrect": "Dandelion seeds are light and fluffy. When you blow on them, the air carries them away. The fluffy part acts like a parachute and helps the seed float to a new place."
        },
        {
            "question": "Why would it be a problem if all seeds fell right under the parent plant?",
            "choices": {
                "A": "It would be fine because they would all grow together",
                "B": "They would be too crowded and not have enough sun and water",
                "C": "The seeds would be happier together",
                "D": "The parent plant would eat the seeds"
            },
            "correct": "B",
            "feedback_correct": "Correct! If all seeds fell in the same spot, they would be too crowded. They would compete for sunlight, water, and space, and many would not survive.",
            "feedback_incorrect": "If too many seeds grow in one spot, they have to share sunlight, water, and nutrients. This is called competition. Seeds travel away so they can find their own spot with enough resources to grow."
        },
        {
            "question": "Which seed shape would help a seed travel far in the wind?",
            "choices": {
                "A": "Heavy and round like a marble",
                "B": "Light and fluffy like a feather",
                "C": "Square and flat like a book",
                "D": "Sticky like tape"
            },
            "correct": "B",
            "feedback_correct": "That is right! Light, fluffy seeds catch the wind and float far away, just like dandelion seeds or cottonwood fluff.",
            "feedback_incorrect": "For wind travel, seeds need to be light and catch the air. Fluffy or winged shapes stay in the air longer and travel farther. Heavy round seeds just drop to the ground."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "What is seed dispersal?",
            "choices": {
                "A": "When seeds stay under the parent plant",
                "B": "When seeds move away from the parent plant to a new place",
                "C": "When seeds get eaten and are gone forever",
                "D": "When plants grow taller"
            },
            "correct": "B",
            "feedback_correct": "Yes! Seed dispersal is when seeds move away from the parent plant to a new place where they can grow.",
            "feedback_incorrect": "Seed dispersal means seeds moving AWAY from the parent plant. Seeds travel to new places using wind, water, or animals so they can find a good spot to grow."
        },
        {
            "question": "A dandelion seed has a fluffy top. An acorn is heavy and round. Which one will travel farther in the wind?",
            "choices": {
                "A": "The acorn because it is bigger",
                "B": "They will travel the same distance",
                "C": "The dandelion seed because its fluffy shape catches the wind",
                "D": "Neither one can travel in the wind"
            },
            "correct": "C",
            "feedback_correct": "Correct! The dandelion seed's fluffy top catches the wind like a parachute, helping it float far away. The heavy acorn cannot float and just drops to the ground.",
            "feedback_incorrect": "Fluffy shapes catch the wind and stay in the air longer. The dandelion seed floats far because its fluffy top acts like a parachute. The heavy acorn falls straight down because the wind cannot carry it."
        },
        {
            "question": "What is an adaptation?",
            "choices": {
                "A": "A toy for plants to play with",
                "B": "A body part or feature that helps a living thing survive",
                "C": "A type of soil",
                "D": "A kind of weather"
            },
            "correct": "B",
            "feedback_correct": "That is right! An adaptation is a body part or feature that helps a living thing survive. Fluffy tops on seeds and wings on maple seeds are adaptations for wind travel.",
            "feedback_incorrect": "An adaptation is a special body part or feature that helps a living thing survive. Seeds have adaptations like fluff, wings, or hooks that help them travel to new places."
        },
        {
            "question": "In our model, what happened to Travel Distance when the Seed Shape was fluffy and there was wind?",
            "choices": {
                "A": "Travel Distance was very short",
                "B": "Travel Distance was very far",
                "C": "Travel Distance did not change at all",
                "D": "The seed could not move"
            },
            "correct": "B",
            "feedback_correct": "Correct! When the Seed Shape was fluffy and there was wind, Travel Distance was far. The fluffy shape catches the air and helps the seed float a long way.",
            "feedback_incorrect": "In our model, fluffy seeds with wind traveled far because the fluffy shape catches the air. This is a positive relationship: more fluffiness plus wind equals more travel distance."
        }
    ]
}

# =============================================================================
# G02-L04: Can Plants Grow Without Soil? (2-LS2-1)
# =============================================================================
L04_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What do you think plants need to grow?",
            "choices": {
                "A": "Only soil",
                "B": "Only water",
                "C": "Sunlight, water, and nutrients",
                "D": "Just a flowerpot"
            },
            "correct": "C",
            "feedback_correct": "That is right! Plants need sunlight, water, and nutrients to grow. They use these to make their own food and stay healthy.",
            "feedback_incorrect": "Plants need more than just one thing. They need sunlight for energy, water to drink, and nutrients like tiny vitamins to grow strong and healthy."
        },
        {
            "question": "Can a plant grow if you put it in water with no soil?",
            "choices": {
                "A": "No, plants always need soil to grow",
                "B": "Yes, plants can grow in water if they get sunlight and nutrients",
                "C": "Only fake plants grow in water",
                "D": "Plants in water die right away"
            },
            "correct": "B",
            "feedback_correct": "Yes! Plants can grow in water if they still get sunlight and nutrients. This is called hydroponics.",
            "feedback_incorrect": "Plants do not actually need soil itself. They need what is IN the soil: water and nutrients. If you give a plant water, nutrients, and sunlight, it can grow just fine without any soil."
        },
        {
            "question": "What do roots do for a plant?",
            "choices": {
                "A": "Roots make flowers bloom",
                "B": "Roots soak up water and nutrients from the ground",
                "C": "Roots make the plant smell nice",
                "D": "Roots help the plant see sunlight"
            },
            "correct": "B",
            "feedback_correct": "Correct! Roots soak up water and nutrients from the soil (or water) and send them up to the rest of the plant.",
            "feedback_incorrect": "Roots are the drinking straws of the plant. They soak up water and nutrients from the soil or from water and send them up through the stem to the rest of the plant."
        },
        {
            "question": "What does sunlight do for a plant?",
            "choices": {
                "A": "Sunlight gives the plant energy to make its own food",
                "B": "Sunlight makes the plant cold",
                "C": "Sunlight makes the soil taste better for the plant",
                "D": "Sunlight does not help plants at all"
            },
            "correct": "A",
            "feedback_correct": "That is right! Sunlight gives plants the energy they need to make their own food inside their leaves.",
            "feedback_incorrect": "Plants use sunlight as energy to make their own food in their leaves. Without sunlight, a plant cannot feed itself and will become pale and weak."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student grows one plant in sunlight with water and another plant in a dark closet with water. After two weeks, the dark plant is pale and droopy. What does this tell us?",
            "choices": {
                "A": "Water is not important for plants",
                "B": "Plants need sunlight to grow healthy",
                "C": "Dark closets have too much soil",
                "D": "The plant in the closet had too much water"
            },
            "correct": "B",
            "feedback_correct": "Correct! Even though both plants had water, the one without sunlight could not make food and became pale and weak. Plants NEED sunlight.",
            "feedback_incorrect": "Both plants had water, but only the sunny plant grew well. The dark plant became pale because it could not make food without sunlight. This proves plants need sunlight to grow healthy."
        },
        {
            "question": "What is hydroponics?",
            "choices": {
                "A": "Growing plants in sand",
                "B": "Growing plants in water instead of soil",
                "C": "Growing plants in the dark",
                "D": "Growing plants with no water at all"
            },
            "correct": "B",
            "feedback_correct": "Yes! Hydroponics is growing plants in water instead of soil. The water has nutrients added so the plant gets everything it needs.",
            "feedback_incorrect": "Hydroponics is a way of growing plants in water with added nutrients, instead of in soil. It works because plants need what is IN the soil, not the soil itself."
        },
        {
            "question": "In our model, what happens to Plant Growth when both Sunlight Amount and Water Availability are high?",
            "choices": {
                "A": "Plant Growth is very poor",
                "B": "Plant Growth is strong and healthy",
                "C": "The plant stops growing",
                "D": "Nothing happens to the plant"
            },
            "correct": "B",
            "feedback_correct": "That is right! When a plant gets lots of sunlight AND lots of water, it has everything it needs to grow strong and healthy.",
            "feedback_incorrect": "Both sunlight and water have a positive effect on plant growth. When both are high, the plant has all the energy and water it needs, so it grows tall with bright green leaves."
        },
        {
            "question": "Why can plants grow without soil?",
            "choices": {
                "A": "Because soil actually hurts plants",
                "B": "Because plants only need air to survive",
                "C": "Because plants need what is IN the soil (water and nutrients), not the soil itself",
                "D": "Because plants do not have roots"
            },
            "correct": "C",
            "feedback_correct": "Correct! Soil is helpful because it holds water and nutrients near the roots, but if the plant gets water and nutrients another way, it does not need soil at all.",
            "feedback_incorrect": "Soil holds water and nutrients near the roots, but soil itself is not what the plant eats. If you give a plant water, nutrients, and sunlight without soil, it can grow just fine."
        }
    ]
}

# =============================================================================
# G02-L05: Why Don't We See Dinosaurs? (2-LS4-1)
# =============================================================================
L05_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Did dinosaurs really live on Earth?",
            "choices": {
                "A": "No, dinosaurs are only in movies",
                "B": "Yes, dinosaurs lived on Earth millions of years ago",
                "C": "Yes, dinosaurs still live on Earth today",
                "D": "No, dinosaurs are just big lizards"
            },
            "correct": "B",
            "feedback_correct": "That is right! Dinosaurs really lived on Earth millions of years ago. We know this because scientists have found their fossils.",
            "feedback_incorrect": "Dinosaurs were real animals that lived on Earth millions of years ago. Scientists have found their bones, teeth, and footprints preserved in rocks called fossils."
        },
        {
            "question": "What is a fossil?",
            "choices": {
                "A": "A type of pet",
                "B": "A fancy rock that sparkles",
                "C": "The remains of a plant or animal from long ago preserved in rock",
                "D": "A toy shaped like a dinosaur"
            },
            "correct": "C",
            "feedback_correct": "Yes! A fossil is the remains or trace of a plant or animal from long ago that has been preserved in rock over millions of years.",
            "feedback_incorrect": "A fossil is not just any rock. It contains the remains or traces of living things from long ago, like bones, teeth, shells, or footprints, that were preserved in rock over millions of years."
        },
        {
            "question": "Why are there no dinosaurs alive today?",
            "choices": {
                "A": "People caught all of them",
                "B": "They are hiding underground",
                "C": "They went to another planet",
                "D": "Something big happened that they could not survive"
            },
            "correct": "D",
            "feedback_correct": "Correct! Something big happened (a giant asteroid hit Earth) that changed the environment so much that dinosaurs could not survive. They went extinct.",
            "feedback_incorrect": "Dinosaurs went extinct because a giant asteroid hit Earth about 66 million years ago. It changed the climate so much that dinosaurs could not find food or survive."
        },
        {
            "question": "What does extinct mean?",
            "choices": {
                "A": "An animal that is sleeping for a long time",
                "B": "An animal that moved to a different place",
                "C": "When every single one of a type of animal has died and none are left",
                "D": "An animal that is very small"
            },
            "correct": "C",
            "feedback_correct": "That is right! Extinct means every single one of that type of animal has died and there are none left alive anywhere on Earth.",
            "feedback_incorrect": "Extinct does not mean hiding or sleeping. It means every last one of that type of animal has died and there are none left alive anywhere on Earth. They are gone forever."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "What happened when the dinosaurs' habitat changed a LOT?",
            "choices": {
                "A": "The dinosaurs grew bigger and stronger",
                "B": "The dinosaurs could not find food or shelter and went extinct",
                "C": "The dinosaurs built houses to stay safe",
                "D": "Nothing happened to the dinosaurs"
            },
            "correct": "B",
            "feedback_correct": "Correct! When the habitat changed too much and too fast, dinosaurs could not find the food, water, and shelter they needed. They went extinct.",
            "feedback_incorrect": "When a habitat changes a lot very quickly, animals cannot adapt fast enough. Dinosaurs could not find food or shelter after the asteroid changed their world, so their population dropped to zero and they went extinct."
        },
        {
            "question": "Scientists found a fossil of a fish in the middle of a desert. What does this tell us?",
            "choices": {
                "A": "Fish can live in sand",
                "B": "Someone put the fish there",
                "C": "That place was once covered by water long ago",
                "D": "The fossil is fake"
            },
            "correct": "C",
            "feedback_correct": "Yes! A fish fossil in a desert is evidence that the area was once covered by water. Habitats change over millions of years.",
            "feedback_incorrect": "Fossils are clues about the past. A fish fossil in a desert tells us that millions of years ago, that spot was underwater. Habitats can change a lot over very long time periods."
        },
        {
            "question": "In our model, what is the relationship between Habitat Change and Animal Survival?",
            "choices": {
                "A": "Positive: more habitat change means better survival",
                "B": "Negative: more habitat change means lower survival",
                "C": "No relationship: habitat change does not affect survival",
                "D": "Positive: animals like when things change a lot"
            },
            "correct": "B",
            "feedback_correct": "Correct! The relationship is negative. When the habitat changes a lot, it becomes harder for animals to find what they need, so survival goes down.",
            "feedback_incorrect": "It is a negative relationship. When habitat change increases, animal survival decreases because the animals cannot find food, water, and shelter in the changed environment."
        },
        {
            "question": "Which animals alive today are related to dinosaurs?",
            "choices": {
                "A": "Dogs and cats",
                "B": "Fish and sharks",
                "C": "Birds like chickens, robins, and eagles",
                "D": "Snakes and lizards only"
            },
            "correct": "C",
            "feedback_correct": "That is right! Scientists discovered that birds are actually living dinosaurs. They evolved from small feathered dinosaurs millions of years ago.",
            "feedback_incorrect": "Fossil evidence shows that birds evolved from small feathered dinosaurs. So every bird you see today, from chickens to eagles, is actually a modern dinosaur!"
        }
    ]
}

# =============================================================================
# G02-L06: How Do Maps Help Us Find Things? (2-ESS2-2)
# =============================================================================
L06_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What does a map show?",
            "choices": {
                "A": "What a place looks like from above, like a bird flying over it",
                "B": "Only buildings and roads",
                "C": "What a place looks like from under the ground",
                "D": "Only oceans and nothing else"
            },
            "correct": "A",
            "feedback_correct": "That is right! A map shows what a place looks like from above, as if you were a bird flying high over the area.",
            "feedback_incorrect": "Maps show a bird's eye view, which means they show what an area looks like from above. They can show land, water, buildings, roads, and many other features."
        },
        {
            "question": "What does the color blue usually mean on a map?",
            "choices": {
                "A": "The sky",
                "B": "Water like rivers, lakes, and oceans",
                "C": "Cold places",
                "D": "Blue flowers"
            },
            "correct": "B",
            "feedback_correct": "Yes! On most maps, blue represents water, including rivers, lakes, streams, and oceans.",
            "feedback_incorrect": "On maps, blue represents water, not the sky. When you see blue on a map, it shows where rivers, lakes, and oceans are located."
        },
        {
            "question": "What is a mountain?",
            "choices": {
                "A": "A very deep hole in the ground",
                "B": "A flat area of land",
                "C": "A tall area of land that rises high above the area around it",
                "D": "A type of river"
            },
            "correct": "C",
            "feedback_correct": "Correct! A mountain is a tall area of land that rises high above the surrounding area. Mountains are one of many landforms on Earth.",
            "feedback_incorrect": "A mountain is a landform that rises high above the surrounding area. Mountains are the tallest features on Earth's surface. Some are covered in snow, forests, or bare rock."
        },
        {
            "question": "Where does water flow when it rains on a mountain?",
            "choices": {
                "A": "Uphill toward the top of the mountain",
                "B": "It stays right where it lands",
                "C": "Downhill toward the bottom and into valleys",
                "D": "Into outer space"
            },
            "correct": "C",
            "feedback_correct": "That is right! Water always flows downhill because of gravity. Rain on a mountain flows down into valleys, streams, and rivers.",
            "feedback_incorrect": "Gravity pulls water downhill. When rain falls on a mountain, it flows down the sides into valleys, creating streams and rivers that carry water to the lowest spots."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "What is a landform?",
            "choices": {
                "A": "A type of plant that grows on land",
                "B": "A natural shape on Earth's surface, like a mountain, hill, valley, or plain",
                "C": "A building made by people",
                "D": "A weather pattern"
            },
            "correct": "B",
            "feedback_correct": "Yes! A landform is a natural shape on Earth's surface. Mountains, hills, valleys, and plains are all landforms.",
            "feedback_incorrect": "Landforms are natural shapes on Earth's surface that were created by nature, not people. Mountains, hills, valleys, plains, and canyons are all examples of landforms."
        },
        {
            "question": "In our model, why does water collect in valleys and low areas?",
            "choices": {
                "A": "Because valleys pull water up from underground",
                "B": "Because water flows downhill and collects at the lowest points",
                "C": "Because valleys are always near the ocean",
                "D": "Because water prefers to be in valleys"
            },
            "correct": "B",
            "feedback_correct": "Correct! Water always flows downhill because of gravity. It naturally collects at the lowest points, which is why rivers and lakes are found in valleys and low areas.",
            "feedback_incorrect": "Gravity pulls water downhill. Water flows from high places like mountains down to the lowest spots. That is why lakes and rivers are found in valleys and low areas, not on top of mountains."
        },
        {
            "question": "On a map, you see a blue winding line between two brown shapes. What does the blue line most likely represent?",
            "choices": {
                "A": "A road between two buildings",
                "B": "A river flowing between two mountains",
                "C": "A crack in the map",
                "D": "A blue fence"
            },
            "correct": "B",
            "feedback_correct": "That is right! Blue on a map means water. A winding blue line between brown shapes (mountains) is a river flowing through a valley.",
            "feedback_incorrect": "Maps use colors to show features. Blue means water and brown often means mountains or high land. A winding blue line between brown shapes is a river flowing between mountains."
        },
        {
            "question": "How is a map different from standing on the ground and looking around?",
            "choices": {
                "A": "A map only shows what is right in front of you",
                "B": "A map shows the whole area from above so you can see everything at once",
                "C": "A map does not show water",
                "D": "Standing on the ground gives you a better view than any map"
            },
            "correct": "B",
            "feedback_correct": "Correct! A map gives you a bird's eye view so you can see the whole area at once, including things you could never see from the ground like how a river bends or what is on the other side of a mountain.",
            "feedback_incorrect": "From the ground, you can only see what is nearby. A map shows you the whole area from above, so you can see all the mountains, rivers, and features at once, even places you cannot see from the ground."
        }
    ]
}

# =============================================================================
# G02-L07: What Makes Wind Blow? (2-ESS2-3)
# =============================================================================
L07_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Can you see wind?",
            "choices": {
                "A": "Yes, wind is blue",
                "B": "Yes, wind looks like white lines",
                "C": "No, but you can feel it and see what it does",
                "D": "No, and wind does not do anything"
            },
            "correct": "C",
            "feedback_correct": "That is right! You cannot see wind because air is invisible, but you can feel it on your skin and see what it does, like blowing leaves and waving flags.",
            "feedback_incorrect": "Wind is invisible because air is invisible. But we can tell wind is there by feeling it on our skin and watching what it does, like moving tree branches, blowing leaves, and making flags wave."
        },
        {
            "question": "What is wind?",
            "choices": {
                "A": "Water falling from the sky",
                "B": "Moving air",
                "C": "A type of cloud",
                "D": "Heat from the sun"
            },
            "correct": "B",
            "feedback_correct": "Yes! Wind is simply air that is moving from one place to another. When air flows, we feel it as wind.",
            "feedback_incorrect": "Wind is moving air. When air flows from one place to another, we feel it as wind. A gentle flow is a breeze, and a strong flow is a gust."
        },
        {
            "question": "What do you think makes the air start moving?",
            "choices": {
                "A": "Giant fans hidden in the sky",
                "B": "The moon pushing the air",
                "C": "The sun heating the ground",
                "D": "Animals running around"
            },
            "correct": "C",
            "feedback_correct": "Correct! The sun heats the ground, which warms the air above it. That warm air rises and cooler air rushes in to take its place, creating wind.",
            "feedback_incorrect": "The sun heats the ground unevenly. Some spots get hotter than others. The warm air above hot spots rises, and cooler air rushes in to fill the space. That moving air is wind."
        },
        {
            "question": "On which day would you expect more wind?",
            "choices": {
                "A": "A hot sunny day at the beach",
                "B": "A cool, cloudy day with even temperatures everywhere",
                "C": "A day with no sun at all",
                "D": "Wind is always the same every day"
            },
            "correct": "A",
            "feedback_correct": "That is right! At the beach on a hot day, the sand heats up while the water stays cool. This temperature difference creates a breeze.",
            "feedback_incorrect": "Wind happens when there are temperature differences. At a hot beach, the sand gets hot while the water stays cool. This big temperature difference makes air move, creating a breeze."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "What causes wind?",
            "choices": {
                "A": "The moon pulls on the air",
                "B": "The sun heats the ground unevenly, warm air rises, and cool air rushes in",
                "C": "Clouds push the air down",
                "D": "Trees blow the air around with their branches"
            },
            "correct": "B",
            "feedback_correct": "Yes! The sun heats the ground unevenly. Warm air rises because it is lighter, and cooler air rushes in to take its place. That rushing air is wind.",
            "feedback_incorrect": "Wind is caused by the sun heating the ground unevenly. The air above hot spots warms up and rises. Then cooler air from nearby rushes in to fill the empty space. That moving air is what we feel as wind."
        },
        {
            "question": "In our model, what is the relationship between Sun Heating and Air Movement?",
            "choices": {
                "A": "Negative: more sun heating means less air movement",
                "B": "No relationship at all",
                "C": "Positive: more sun heating means more air movement",
                "D": "The sun does not affect air movement"
            },
            "correct": "C",
            "feedback_correct": "Correct! It is a positive relationship. More sun heating warms the ground more, which makes the air above it rise faster, causing more air movement and stronger wind.",
            "feedback_incorrect": "More sun heating creates a bigger temperature difference between warm and cool areas. This makes the air move more, creating stronger wind. So it is a positive relationship: more heating equals more movement."
        },
        {
            "question": "At the beach on a hot day, the sand gets very hot but the water stays cool. What happens?",
            "choices": {
                "A": "The wind blows from the hot sand toward the cool water",
                "B": "A breeze blows from the cool water toward the hot sand",
                "C": "There is no wind at the beach",
                "D": "The water gets as hot as the sand"
            },
            "correct": "B",
            "feedback_correct": "That is right! The air above the hot sand rises, and cooler air from over the water rushes in to replace it. This creates a breeze that blows from the water toward the sand.",
            "feedback_incorrect": "Hot air rises above the warm sand. Cooler air from above the water rushes in to fill the space. This means the breeze blows FROM the cool water TOWARD the hot sand."
        },
        {
            "question": "Why is there very little wind on a cool, cloudy day?",
            "choices": {
                "A": "Because clouds block the wind from forming",
                "B": "Because without strong sun, there is little temperature difference to move the air",
                "C": "Because the air is too heavy to move on cloudy days",
                "D": "Because wind only happens at night"
            },
            "correct": "B",
            "feedback_correct": "Correct! Without strong sun heating, the ground stays cool and the temperature is more even everywhere. Without big temperature differences, there is very little air movement and weak wind.",
            "feedback_incorrect": "Wind needs temperature differences. On a cloudy day, the sun does not heat the ground much, so the temperature is more even everywhere. Without a big difference between warm and cool areas, there is not much air movement."
        }
    ]
}

# =============================================================================
# G02-L08: How Fast Does Ice Melt? (2-PS1-4)
# =============================================================================
L08_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What happens to an ice cube when you take it out of the freezer?",
            "choices": {
                "A": "It stays frozen forever",
                "B": "It starts to melt and turn into water",
                "C": "It gets colder",
                "D": "It grows bigger"
            },
            "correct": "B",
            "feedback_correct": "That is right! When you take ice out of the freezer, the warm air around it starts to melt the ice, turning it from a solid into liquid water.",
            "feedback_incorrect": "Ice is frozen water. When you take it out of the freezer, the warmer air transfers heat into the ice, causing it to melt and become liquid water."
        },
        {
            "question": "Can you turn water back into ice?",
            "choices": {
                "A": "No, once ice melts it can never be ice again",
                "B": "Yes, by putting the water in a freezer to make it cold enough",
                "C": "Only if you add special chemicals",
                "D": "Only if the water is blue"
            },
            "correct": "B",
            "feedback_correct": "Yes! You can turn water back into ice by putting it in a freezer. The cold temperature freezes the water back into solid ice.",
            "feedback_incorrect": "Water can absolutely be turned back into ice. Just put it in a freezer and wait. When the water gets cold enough, it freezes into solid ice again."
        },
        {
            "question": "Where would an ice cube melt faster?",
            "choices": {
                "A": "In a freezer",
                "B": "In a refrigerator",
                "C": "On a sunny sidewalk",
                "D": "In a bucket of snow"
            },
            "correct": "C",
            "feedback_correct": "Correct! A sunny sidewalk is the warmest place, so the ice would melt fastest there. More heat means faster melting.",
            "feedback_incorrect": "Ice melts faster in warmer places because more heat transfers into the ice. A sunny sidewalk is very warm, so the ice would melt quickly there."
        },
        {
            "question": "What is melting?",
            "choices": {
                "A": "When a solid heats up and turns into a liquid",
                "B": "When a liquid heats up and turns into a gas",
                "C": "When something gets colder",
                "D": "When something breaks into small pieces"
            },
            "correct": "A",
            "feedback_correct": "That is right! Melting is when a solid gets warm enough to turn into a liquid, like ice turning into water.",
            "feedback_incorrect": "Melting is the process of a solid turning into a liquid because of heat. When ice gets warm enough, it melts and becomes liquid water."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "Two ice cubes of the same size are placed outside. One is in the shade and one is in direct sunlight. Which melts first?",
            "choices": {
                "A": "The one in the shade",
                "B": "They melt at exactly the same speed",
                "C": "The one in direct sunlight",
                "D": "Neither one melts"
            },
            "correct": "C",
            "feedback_correct": "Correct! The ice cube in direct sunlight melts first because it receives more heat energy from the sun, making it melt faster.",
            "feedback_incorrect": "The sun provides heat energy. The ice cube in direct sunlight gets much more heat than the one in the shade, so it melts faster. Warmer surroundings always mean faster melting."
        },
        {
            "question": "What is a reversible change?",
            "choices": {
                "A": "A change that can never happen again",
                "B": "A change that can be undone, like melting and freezing",
                "C": "A change that only happens once",
                "D": "A change that makes things disappear"
            },
            "correct": "B",
            "feedback_correct": "Yes! A reversible change is one that can be undone. Melting ice into water and freezing water back into ice is a reversible change because you can go back and forth.",
            "feedback_incorrect": "A reversible change is one you can undo. Ice can melt into water, and water can freeze back into ice. This change can go back and forth forever, making it reversible."
        },
        {
            "question": "In our model, what is the relationship between Surrounding Temperature and Melting Speed?",
            "choices": {
                "A": "Negative: higher temperature means slower melting",
                "B": "Positive: higher temperature means faster melting",
                "C": "No relationship: temperature does not matter",
                "D": "Temperature only affects big ice cubes"
            },
            "correct": "B",
            "feedback_correct": "Correct! It is a positive relationship. When the surrounding temperature goes up, the melting speed goes up too. Warmer surroundings transfer more heat to the ice.",
            "feedback_incorrect": "Higher surrounding temperature means more heat energy flows into the ice, making it melt faster. This is a positive relationship: as temperature increases, melting speed increases."
        },
        {
            "question": "Which of these is NOT a reversible change?",
            "choices": {
                "A": "Melting ice into water",
                "B": "Freezing water into ice",
                "C": "Baking a cookie from dough",
                "D": "Melting a popsicle"
            },
            "correct": "C",
            "feedback_correct": "That is right! Baking a cookie is NOT reversible. You cannot un-bake a cookie back into flour, sugar, and eggs. Melting and freezing are reversible, but baking is not.",
            "feedback_incorrect": "Melting and freezing are reversible because the water just changes form. But baking changes the ingredients in a way that cannot be undone. You cannot turn a cookie back into raw dough."
        }
    ]
}

# =============================================================================
# G02-L09: Why Are There So Many Kinds of Bugs? (2-LS4-1)
# =============================================================================
L09_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Why do you think there are so many different kinds of insects?",
            "choices": {
                "A": "Because there is only one kind of place to live",
                "B": "Because there are many different places to live and each needs different insects",
                "C": "Because all insects look the same",
                "D": "Because insects choose to look different for fun"
            },
            "correct": "B",
            "feedback_correct": "That is right! There are many different habitats on Earth, and each habitat needs insects with different body features to survive there.",
            "feedback_incorrect": "Earth has many different habitats like gardens, ponds, forests, and deserts. Each habitat has different challenges, so insects in each place need different body features to survive."
        },
        {
            "question": "What is a habitat?",
            "choices": {
                "A": "A type of insect",
                "B": "The place where an animal lives and finds food, water, and shelter",
                "C": "A pet store for bugs",
                "D": "A type of rock"
            },
            "correct": "B",
            "feedback_correct": "Yes! A habitat is the place where an animal lives and finds everything it needs to survive, like food, water, and shelter.",
            "feedback_incorrect": "A habitat is an animal's home in nature. It is the place that provides everything the animal needs to survive, including food, water, and shelter."
        },
        {
            "question": "Do a butterfly and a water beetle need the same body features to survive?",
            "choices": {
                "A": "Yes, all insects need the same body parts",
                "B": "No, they live in different places and need different features",
                "C": "Yes, because they are both insects",
                "D": "No, because one is bigger than the other"
            },
            "correct": "B",
            "feedback_correct": "Correct! A butterfly flies in gardens and needs wings, while a water beetle swims in ponds and needs paddle-shaped legs. Different habitats need different features.",
            "feedback_incorrect": "Even though both are insects, they live in very different places. A butterfly needs wings to fly between flowers. A water beetle needs flat legs to swim in ponds. Their different habitats require different body features."
        },
        {
            "question": "How many legs does an insect have?",
            "choices": {
                "A": "Four legs",
                "B": "Eight legs",
                "C": "Six legs",
                "D": "Two legs"
            },
            "correct": "C",
            "feedback_correct": "That is right! All insects have six legs. This is one feature that makes an insect an insect. Spiders have eight legs, so they are NOT insects.",
            "feedback_incorrect": "All insects have six legs and three body parts. Spiders have eight legs, so they are arachnids, not insects. If you count six legs, it is an insect!"
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A water beetle has flat, paddle-shaped legs. Why does it have this body feature?",
            "choices": {
                "A": "Because it chose to have paddle legs",
                "B": "Because paddle-shaped legs help it swim in its pond habitat",
                "C": "Because all insects have paddle-shaped legs",
                "D": "Because it needs to fly between flowers"
            },
            "correct": "B",
            "feedback_correct": "Correct! The water beetle's flat, paddle-shaped legs are an adaptation that helps it swim in its pond habitat. Its body features match the challenges of living in water.",
            "feedback_incorrect": "Body features match habitats. A water beetle lives in ponds, so it needs features for swimming. Flat, paddle-shaped legs push through water like oars, helping it move and find food in its water habitat."
        },
        {
            "question": "What is diversity?",
            "choices": {
                "A": "When all living things look the same",
                "B": "Having many different kinds of living things with lots of variety",
                "C": "When animals live alone",
                "D": "A type of insect"
            },
            "correct": "B",
            "feedback_correct": "Yes! Diversity means having many different kinds of living things with lots of variety. Earth has incredible diversity, with over a million different insect species alone.",
            "feedback_incorrect": "Diversity means variety. Having many different kinds of living things is what makes life on Earth so diverse. There are over one million different species of insects, each unique."
        },
        {
            "question": "In our model, what happens when you change the Habitat Type from garden to pond?",
            "choices": {
                "A": "The Body Features stay exactly the same",
                "B": "The Body Features change because pond insects need different features than garden insects",
                "C": "The insects disappear",
                "D": "Nothing changes at all"
            },
            "correct": "B",
            "feedback_correct": "Correct! Different habitats need different body features. Garden insects need wings and camouflage, while pond insects need swimming legs and waterproof bodies.",
            "feedback_incorrect": "When the habitat changes, the body features that help an insect survive also change. A garden needs fliers with camouflage, while a pond needs swimmers with paddle legs. Different habitat, different features."
        },
        {
            "question": "Why is it important for an insect's body features to match its habitat?",
            "choices": {
                "A": "It is not important at all",
                "B": "So the insect looks pretty",
                "C": "Because matching features help the insect find food, escape danger, and survive",
                "D": "Because insects with the wrong features grow bigger"
            },
            "correct": "C",
            "feedback_correct": "That is right! When body features match the habitat, the insect can find food, hide from predators, and survive. A butterfly's wings help it fly to flowers in a garden, and a beetle's paddle legs help it swim in a pond.",
            "feedback_incorrect": "An insect survives best when its features match its habitat. A water beetle with paddle legs thrives in a pond. A butterfly with wings thrives in a garden. If the features do not match the habitat, the insect cannot find food or escape danger."
        }
    ]
}

# =============================================================================
# G02-L10: How Do Rocks Tell Stories? (2-ESS1-1)
# =============================================================================
L10_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Are all rocks the same?",
            "choices": {
                "A": "Yes, all rocks are exactly alike",
                "B": "No, there are many different kinds of rocks that look and feel different",
                "C": "Yes, rocks are just gray and hard",
                "D": "No, but there are only two kinds of rocks"
            },
            "correct": "B",
            "feedback_correct": "That is right! Rocks come in many different types. Some are smooth, some are rough, some are sparkly, and some have layers. Each type formed in a different way.",
            "feedback_incorrect": "Rocks are very different from each other. Some are smooth from river water, some are rough from volcanoes, and some have colorful layers. Each rock formed from a different event on Earth."
        },
        {
            "question": "What do you think is inside a mountain?",
            "choices": {
                "A": "Empty space like a cave",
                "B": "Layers of rock stacked on top of each other",
                "C": "Just dirt all the way through",
                "D": "Water all the way through"
            },
            "correct": "B",
            "feedback_correct": "Yes! If you could cut a mountain in half, you would see layers of rock stacked on top of each other, like pages in a book. Each layer formed at a different time.",
            "feedback_incorrect": "Mountains are made of layers of rock. If you could slice a mountain in half, you would see different layers stacked up. Each layer was formed at a different time by different events."
        },
        {
            "question": "Can rocks change over time?",
            "choices": {
                "A": "No, rocks never change",
                "B": "Yes, but only if people break them",
                "C": "Yes, wind and water can slowly change rocks over a very long time",
                "D": "Rocks change every day"
            },
            "correct": "C",
            "feedback_correct": "Correct! Wind and water slowly wear down rocks over thousands and millions of years. This process is called erosion.",
            "feedback_incorrect": "Rocks do change, but usually very slowly. Over thousands and millions of years, wind and water wear rocks down, breaking off tiny pieces and carrying them away. This slow change is called erosion."
        },
        {
            "question": "What is a volcano?",
            "choices": {
                "A": "A type of cloud",
                "B": "An opening in the Earth where hot melted rock comes out",
                "C": "A very tall tree",
                "D": "A deep lake"
            },
            "correct": "B",
            "feedback_correct": "That is right! A volcano is an opening in the Earth's surface where hot melted rock called lava comes out. When the lava cools, it makes new rock.",
            "feedback_incorrect": "A volcano is a place where hot melted rock from deep inside the Earth comes up to the surface. The hot liquid rock is called lava, and when it cools down, it hardens into new rock."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "Which rock layer is the oldest in a stack of rock layers?",
            "choices": {
                "A": "The top layer",
                "B": "The middle layer",
                "C": "The bottom layer",
                "D": "They are all the same age"
            },
            "correct": "C",
            "feedback_correct": "Correct! The bottom layer is the oldest because it formed first. Each new layer settles on top, so the top layer is the newest.",
            "feedback_incorrect": "Rock layers build up from the bottom. The bottom layer was deposited first, making it the oldest. Each layer on top formed later. Reading layers from bottom to top is like reading a book from beginning to end."
        },
        {
            "question": "A scientist finds smooth, round rocks at the bottom of a valley. What Earth event most likely shaped these rocks?",
            "choices": {
                "A": "A fast volcanic eruption",
                "B": "A slow-flowing river over many years",
                "C": "An earthquake",
                "D": "A lightning strike"
            },
            "correct": "B",
            "feedback_correct": "Yes! Smooth, round rocks are shaped by water flowing over them for a very long time. A river slowly wears down the rough edges, making rocks smooth and round.",
            "feedback_incorrect": "Smooth, round rocks are a clue that water shaped them. Rivers flow over rocks for thousands of years, slowly wearing down rough edges and making them smooth and round. This is a slow Earth event."
        },
        {
            "question": "What is the difference between a fast Earth event and a slow Earth event?",
            "choices": {
                "A": "There is no difference",
                "B": "Fast events like volcanoes happen in minutes, while slow events like erosion take thousands of years",
                "C": "Slow events are louder than fast events",
                "D": "Fast events only happen at night"
            },
            "correct": "B",
            "feedback_correct": "Correct! Fast Earth events like volcanic eruptions happen in minutes or hours. Slow Earth events like erosion and sediment building up take thousands or millions of years. Both leave evidence in rocks.",
            "feedback_incorrect": "Some Earth events happen quickly (volcanoes erupt, earthquakes shake) while others take a very long time (rivers carve canyons, wind wears down rock). Both fast and slow events leave evidence in the rocks they create."
        },
        {
            "question": "What is sediment?",
            "choices": {
                "A": "Hot melted rock from a volcano",
                "B": "A type of plant that grows on rocks",
                "C": "Tiny pieces of rock, sand, and soil that settle in layers",
                "D": "Water that is very dirty"
            },
            "correct": "C",
            "feedback_correct": "That is right! Sediment is made up of tiny pieces of rock, sand, and soil. When sediment settles in layers and gets pressed together over millions of years, it becomes sedimentary rock.",
            "feedback_incorrect": "Sediment is tiny pieces of rock, sand, and soil that have been broken off by wind, water, or ice. When these tiny pieces settle in layers and get pressed together over a very long time, they can turn into new rock."
        }
    ]
}

# =============================================================================
# ALL_QUESTIONS: Master dictionary mapping lesson IDs to question sets
# =============================================================================
ALL_QUESTIONS = {
    "G02-L01": L01_QUESTIONS,
    "G02-L02": L02_QUESTIONS,
    "G02-L03": L03_QUESTIONS,
    "G02-L04": L04_QUESTIONS,
    "G02-L05": L05_QUESTIONS,
    "G02-L06": L06_QUESTIONS,
    "G02-L07": L07_QUESTIONS,
    "G02-L08": L08_QUESTIONS,
    "G02-L09": L09_QUESTIONS,
    "G02-L10": L10_QUESTIONS,
}
