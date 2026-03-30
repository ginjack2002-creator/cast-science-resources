#!/usr/bin/env python3
"""Multiple choice pre/post assessment questions for Grade 4 ModelIt! Lessons"""

# =============================================================================
# G04-L01: Why Do Roller Coasters Go So Fast?
# NGSS 4-PS3-1: Use evidence to construct an explanation relating the speed
# of an object to the energy of that object.
# =============================================================================
L01_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What makes a roller coaster speed up as it goes down a hill?",
            "choices": {
                "A": "An engine inside the roller coaster pushes it forward the whole ride",
                "B": "Gravity pulls the coaster downhill and it picks up speed",
                "C": "The wind blows it down the hill",
                "D": "The passengers lean forward to make it go faster"
            },
            "correct": "B",
            "feedback_correct": "That is right! Gravity pulls the coaster downhill, and it gains speed as it drops. No engine is needed after the first hill.",
            "feedback_incorrect": "Think again. Roller coasters do not have engines pushing them after the first hill. Gravity is the force that pulls the coaster down and makes it speed up."
        },
        {
            "question": "What is energy?",
            "choices": {
                "A": "Something only batteries and electricity have",
                "B": "How tired or awake you feel",
                "C": "The ability to make things move, change, or do work",
                "D": "A type of gas that makes machines run"
            },
            "correct": "C",
            "feedback_correct": "Exactly! Energy is the ability to cause change or do work. It comes in many forms, including motion, heat, light, and sound.",
            "feedback_incorrect": "Energy is not just about batteries or how you feel. In science, energy means the ability to make things move, change, or do work."
        },
        {
            "question": "When a ball rolls down a tall ramp, what happens to its speed compared to a short ramp?",
            "choices": {
                "A": "It goes the same speed no matter how tall the ramp is",
                "B": "It goes slower on the tall ramp because it is scared of heights",
                "C": "It goes faster at the bottom of the tall ramp",
                "D": "It stops halfway down the tall ramp"
            },
            "correct": "C",
            "feedback_correct": "Correct! A ball rolling down a taller ramp reaches a faster speed at the bottom because it has more stored energy at the top.",
            "feedback_incorrect": "Try again. The height of the ramp matters. A taller ramp gives the ball more energy, so it goes faster at the bottom."
        },
        {
            "question": "What happens to a roller coaster's energy when it slows down and stops?",
            "choices": {
                "A": "The energy disappears completely",
                "B": "The energy turns into heat and sound from friction",
                "C": "The energy floats away into the sky",
                "D": "The energy was never real in the first place"
            },
            "correct": "B",
            "feedback_correct": "Right! Energy is never destroyed. When a coaster slows down, its motion energy transforms into heat and sound energy through friction.",
            "feedback_incorrect": "Energy cannot disappear or float away. When a coaster slows down, its motion energy changes into other forms like heat and sound."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A roller coaster is at the very top of the tallest hill. What type of energy does it have the MOST of?",
            "choices": {
                "A": "Kinetic energy because it is moving fast",
                "B": "Sound energy because the riders are screaming",
                "C": "Potential energy because of its high position",
                "D": "Heat energy because the sun is shining on it"
            },
            "correct": "C",
            "feedback_correct": "That is right! At the top of a tall hill, the coaster has lots of potential energy stored because of its high position. That energy will convert to kinetic energy as it rolls down.",
            "feedback_incorrect": "At the top of a hill, the coaster is barely moving, so it does not have much kinetic energy. Its energy is stored as potential energy because of its height."
        },
        {
            "question": "In the roller coaster model, hill height is an EXTERNAL component. What does that mean?",
            "choices": {
                "A": "It is located outside the amusement park",
                "B": "It is a part of the system we can control or set before the ride starts",
                "C": "It only matters when the weather is nice outside",
                "D": "It has no effect on the coaster's speed"
            },
            "correct": "B",
            "feedback_correct": "Correct! An external component is something we can control or decide before the system runs. Hill height is a design choice made before the coaster moves.",
            "feedback_incorrect": "In a model, an external component is something we can set or control. Hill height is external because engineers decide how tall to build the hill before the ride operates."
        },
        {
            "question": "As a roller coaster rolls from the top of a hill to the bottom, what happens to its energy?",
            "choices": {
                "A": "Potential energy transforms into kinetic energy",
                "B": "Kinetic energy transforms into potential energy",
                "C": "All energy is used up by the time it reaches the bottom",
                "D": "New energy is created as the coaster goes faster"
            },
            "correct": "A",
            "feedback_correct": "Exactly! As the coaster goes downhill, its stored potential energy transforms into kinetic energy (energy of motion). That is why it speeds up!",
            "feedback_incorrect": "When a coaster goes downhill, its stored energy (potential energy) changes into motion energy (kinetic energy). Energy is never created or destroyed, just transformed."
        },
        {
            "question": "The relationship between hill height and speed at the bottom is POSITIVE. What does that mean?",
            "choices": {
                "A": "The roller coaster is always happy when it is tall",
                "B": "When hill height goes up, speed at the bottom also goes up",
                "C": "When hill height goes up, speed at the bottom goes down",
                "D": "Hill height and speed are not connected at all"
            },
            "correct": "B",
            "feedback_correct": "Right! A positive relationship means both things increase together. Taller hill means more stored energy, which means more speed at the bottom.",
            "feedback_incorrect": "A positive relationship in a model means when one thing increases, the other increases too. Taller hills produce more speed at the bottom."
        }
    ]
}

# =============================================================================
# G04-L02: How Does Your Phone Hear Your Voice?
# NGSS 4-PS4-1: Develop a model of waves to describe patterns in terms of
# amplitude and wavelength and that waves can cause objects to move.
# =============================================================================
L02_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is sound?",
            "choices": {
                "A": "An invisible gas that floats through the air",
                "B": "Vibrations that travel through air, water, or other materials",
                "C": "A type of light that our ears can detect",
                "D": "Something that only exists when music is playing"
            },
            "correct": "B",
            "feedback_correct": "That is right! Sound is made of vibrations. When something vibrates, it pushes air molecules back and forth, creating sound waves.",
            "feedback_incorrect": "Sound is not a gas or a type of light. Sound is actually vibrations that travel through materials like air, water, or even solid objects."
        },
        {
            "question": "Why is a shout louder than a whisper?",
            "choices": {
                "A": "A shout uses different air molecules than a whisper",
                "B": "A shout pushes more air and makes bigger vibrations",
                "C": "A shout travels faster through the air",
                "D": "A shout creates a different type of sound wave"
            },
            "correct": "B",
            "feedback_correct": "Correct! When you shout, you push more air with more force, creating bigger vibrations (larger amplitude), which your ears hear as louder sound.",
            "feedback_incorrect": "Loud and quiet sounds travel at the same speed through air. The difference is how big the vibrations are. Shouting pushes more air, making bigger vibrations."
        },
        {
            "question": "Can sound travel through outer space?",
            "choices": {
                "A": "Yes, sound travels everywhere",
                "B": "Yes, but only very loud sounds",
                "C": "No, because there is no air or material for sound to travel through",
                "D": "No, because space is too cold for sound"
            },
            "correct": "C",
            "feedback_correct": "Right! Sound needs a material (like air, water, or a solid) to travel through. Space is a vacuum with almost no molecules, so sound cannot travel there.",
            "feedback_incorrect": "Temperature is not the reason. Sound needs molecules to vibrate and carry the wave. In space, there are almost no molecules, so sound cannot travel."
        },
        {
            "question": "How does a phone know you are talking to it?",
            "choices": {
                "A": "It reads your lips through the camera",
                "B": "It has a tiny person inside listening",
                "C": "It has a microphone that vibrates when sound waves hit it",
                "D": "It guesses what you might be saying"
            },
            "correct": "C",
            "feedback_correct": "Exactly! A phone's microphone has a small part called a diaphragm that vibrates when sound waves hit it, turning your voice into electrical signals.",
            "feedback_incorrect": "Phones detect your voice using a microphone. The microphone has a tiny part inside that vibrates when sound waves from your voice hit it."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "What is amplitude?",
            "choices": {
                "A": "How fast a sound wave travels through the air",
                "B": "How high or low a sound's pitch is",
                "C": "How big a wave is from top to bottom",
                "D": "The number of waves that pass by in one second"
            },
            "correct": "C",
            "feedback_correct": "That is right! Amplitude is the size of the wave from top to bottom. Bigger amplitude means the air molecules move farther back and forth, creating a louder sound.",
            "feedback_incorrect": "Amplitude is not about speed or pitch. It measures how big the wave is. Larger amplitude means louder sound because the air molecules vibrate more."
        },
        {
            "question": "In the sound wave model, Sound Wave Strength is an external component. Vibration Size and Volume Level are internal components. Why?",
            "choices": {
                "A": "Because vibration size and volume are inside the phone",
                "B": "Because the speaker controls sound wave strength, and vibration size and volume respond to it",
                "C": "Because volume level is always the same",
                "D": "Because external means louder and internal means quieter"
            },
            "correct": "B",
            "feedback_correct": "Correct! Sound wave strength is external because the speaker controls it. Vibration size and volume level are internal because they change as a result of how strong the sound source is.",
            "feedback_incorrect": "In a model, external components are things we can control. Internal components are things that change in response. The speaker controls sound strength, and vibration size and volume change as a result."
        },
        {
            "question": "A student plucks a guitar string gently, then plucks it hard. The hard pluck makes a louder sound. Which best explains why?",
            "choices": {
                "A": "The hard pluck makes the string vibrate with larger amplitude, sending bigger sound waves to our ears",
                "B": "The hard pluck makes the sound travel faster through the air",
                "C": "The hard pluck changes the type of sound wave from one kind to another",
                "D": "The hard pluck creates a higher-pitched sound that seems louder"
            },
            "correct": "A",
            "feedback_correct": "Exactly! Plucking harder makes the string vibrate more, creating sound waves with larger amplitude. Larger amplitude means louder sound.",
            "feedback_incorrect": "Plucking harder does not change speed or pitch. It makes the string vibrate with bigger movements (larger amplitude), which creates louder sound waves."
        },
        {
            "question": "The model shows that when sound wave strength increases, vibration size increases, and volume level increases. This is an example of what kind of relationship?",
            "choices": {
                "A": "A negative relationship because loud sounds are bad for your ears",
                "B": "A positive relationship because when one goes up, the others go up too",
                "C": "No relationship because they are separate things",
                "D": "A random relationship because it changes every time"
            },
            "correct": "B",
            "feedback_correct": "Right! This is a positive relationship. When sound wave strength increases, vibration size increases, and volume level increases. They all go up together in a cause-and-effect chain.",
            "feedback_incorrect": "When one component increases and another also increases, that is a positive relationship. All three components increase together in a direct chain."
        }
    ]
}

# =============================================================================
# G04-L03: Why Can't You See in the Dark?
# NGSS 4-PS4-2: Develop a model to describe that light reflecting from objects
# and entering the eye allows objects to be seen.
# =============================================================================
L03_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "How do your eyes let you see objects?",
            "choices": {
                "A": "Your eyes shoot out invisible beams that bounce off objects",
                "B": "Light bounces off objects and enters your eyes",
                "C": "Your brain imagines what things look like and sends pictures to your eyes",
                "D": "Objects glow with their own light so your eyes can see them"
            },
            "correct": "B",
            "feedback_correct": "That is right! You see objects because light from a source hits them, bounces off, and enters your eyes. Your eyes receive light, they do not send it out.",
            "feedback_incorrect": "Your eyes do not shoot out beams, and most objects do not make their own light. You see objects because light bounces off them and enters your eyes."
        },
        {
            "question": "Why is it hard to see anything in a completely dark room?",
            "choices": {
                "A": "Your eyes need time to warm up before they can see",
                "B": "Dark rooms have too much air blocking your vision",
                "C": "There is no light to bounce off objects and enter your eyes",
                "D": "Objects turn invisible when the lights go off"
            },
            "correct": "C",
            "feedback_correct": "Correct! Without a light source, there is no light to bounce off objects. Your eyes need reflected light to see, so no light means no vision.",
            "feedback_incorrect": "Objects do not actually become invisible. The problem is that without a light source, there is no light to bounce off objects and reach your eyes."
        },
        {
            "question": "Which of these is a light source?",
            "choices": {
                "A": "A mirror",
                "B": "A white piece of paper",
                "C": "The Moon",
                "D": "The Sun"
            },
            "correct": "D",
            "feedback_correct": "Right! The Sun makes its own light, so it is a light source. Mirrors and paper only reflect light, and the Moon also reflects light from the Sun.",
            "feedback_incorrect": "A light source must make its own light. Mirrors and paper reflect light, and the Moon only shines because it reflects sunlight. The Sun creates its own light."
        },
        {
            "question": "What is the black circle in the middle of your eye called?",
            "choices": {
                "A": "The eyelid",
                "B": "The pupil",
                "C": "The eyebrow",
                "D": "The iris"
            },
            "correct": "B",
            "feedback_correct": "That is right! The pupil is the black opening in your eye that lets light in. It gets bigger in dim light to let more light in and smaller in bright light.",
            "feedback_incorrect": "The black circle in the center of your eye is called the pupil. It is the opening that lets light enter your eye so you can see."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the light and vision model, what are the three components?",
            "choices": {
                "A": "Eye color, room size, and object weight",
                "B": "Light source brightness, light bouncing off objects, and eye detection",
                "C": "Darkness level, eye strength, and brain power",
                "D": "Lamp size, mirror angle, and pupil color"
            },
            "correct": "B",
            "feedback_correct": "Exactly! The model has three components: light source brightness (external), light bouncing off objects (internal), and eye detection (internal).",
            "feedback_incorrect": "The three model components are light source brightness, light bouncing off objects, and eye detection. These show the chain from light source to seeing."
        },
        {
            "question": "What does it mean that most objects REFLECT light rather than making their own light?",
            "choices": {
                "A": "Most objects glow in the dark after lights are turned off",
                "B": "Most objects bounce light from a source back to our eyes, which is how we see them",
                "C": "Most objects absorb all light and never let any bounce off",
                "D": "Most objects create light but only when we look at them"
            },
            "correct": "B",
            "feedback_correct": "Right! Most objects do not make their own light. We see them because light from a source (like the Sun or a lamp) hits them, bounces off, and enters our eyes.",
            "feedback_incorrect": "Most objects are not light sources. They reflect (bounce back) light that hits them from a light source. That reflected light enters your eyes, and that is how you see."
        },
        {
            "question": "A student shines a flashlight in a dark room. They can see a white ball but a black ball is harder to see. Why?",
            "choices": {
                "A": "The black ball is smaller than the white ball",
                "B": "The white ball reflects more light back to the student's eyes, while the black ball absorbs more light",
                "C": "The white ball makes its own light and the black ball does not",
                "D": "The flashlight only works on white objects"
            },
            "correct": "B",
            "feedback_correct": "That is right! White objects reflect most of the light that hits them, so more light reaches your eyes. Dark objects absorb more light and reflect less, making them harder to see.",
            "feedback_incorrect": "Neither ball makes its own light. The difference is that white surfaces reflect most light while dark surfaces absorb most of it. More reflected light means easier to see."
        },
        {
            "question": "Based on the model, what must happen for you to see an object?",
            "choices": {
                "A": "The object must be close enough for your eyes to reach it with beams",
                "B": "A light source must create light, the light must bounce off the object, and the reflected light must enter your eyes",
                "C": "You must stare at the object for at least five seconds",
                "D": "The object must be brighter than everything else in the room"
            },
            "correct": "B",
            "feedback_correct": "Exactly! The model shows a three-step chain: light source creates light, light reflects off the object, and the reflected light enters your eyes. All three steps are needed to see.",
            "feedback_incorrect": "Your eyes do not send out beams. The model shows three connected steps: a light source creates light, that light bounces off an object, and the reflected light enters your eyes."
        }
    ]
}

# =============================================================================
# G04-L04: Why Do Animals Have Superpowers?
# NGSS 4-LS1-1: Construct an argument that plants and animals have internal
# and external structures that function to support survival.
# =============================================================================
L04_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Why do polar bears have thick white fur?",
            "choices": {
                "A": "Because they think it looks nice",
                "B": "Because the fur keeps them warm and helps them hide in the snow",
                "C": "Because all bears have white fur",
                "D": "Because they eat too much snow"
            },
            "correct": "B",
            "feedback_correct": "That is right! A polar bear's thick fur is a body structure that serves two functions: keeping the bear warm in freezing temperatures and providing camouflage in the snow.",
            "feedback_incorrect": "Polar bears have thick white fur because it helps them survive. The fur keeps them warm in the Arctic cold and helps them blend in with the snow to hunt."
        },
        {
            "question": "What is the difference between an external structure and an internal structure?",
            "choices": {
                "A": "External structures are big and internal structures are small",
                "B": "External structures are on the outside of the body and internal structures are on the inside",
                "C": "External structures are useful and internal structures are not",
                "D": "There is no difference between them"
            },
            "correct": "B",
            "feedback_correct": "Correct! External structures are body parts on the outside (like fur, claws, and shells) and internal structures are body parts on the inside (like bones, lungs, and hearts).",
            "feedback_incorrect": "The difference is location. External structures are on the outside of the animal's body, and internal structures are on the inside. Both are important for survival."
        },
        {
            "question": "A bird has a long, thin beak. What do you think this beak helps the bird do?",
            "choices": {
                "A": "Dig underground tunnels",
                "B": "Reach insects or nectar deep inside flowers or bark",
                "C": "Fly faster through the air",
                "D": "Breathe underwater"
            },
            "correct": "B",
            "feedback_correct": "Right! A long, thin beak is a body structure that helps a bird reach food in hard-to-reach places, like insects inside tree bark or nectar inside flowers.",
            "feedback_incorrect": "Think about what a long, thin shape is good for. It can reach into narrow spaces. Birds with long beaks use them to reach insects or nectar that other birds cannot get to."
        },
        {
            "question": "What does 'survival' mean for an animal?",
            "choices": {
                "A": "Being the biggest animal in the area",
                "B": "Living in a zoo where people take care of you",
                "C": "Staying alive by finding food, avoiding predators, and having babies",
                "D": "Being able to run faster than every other animal"
            },
            "correct": "C",
            "feedback_correct": "Exactly! Survival means staying alive by meeting basic needs: finding food and water, staying safe from predators, and reproducing (having babies) to continue the species.",
            "feedback_incorrect": "Survival is not about being the biggest or fastest. It means staying alive by finding food, avoiding danger, and having babies so the species continues."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the model, Body Structure Type and Environment Danger Level are both EXTERNAL components. What does this tell us?",
            "choices": {
                "A": "They are both found outside the animal's body",
                "B": "They are both things we can set or change to see how survival rate responds",
                "C": "They are both unimportant to the model",
                "D": "They both cause the animal to run away"
            },
            "correct": "B",
            "feedback_correct": "Right! In the model, external components are the inputs we can control. We set the body structure type and the environment danger level, then observe how survival rate responds.",
            "feedback_incorrect": "In a model, external components are inputs we can set and change. Body structure type and environment danger level are both inputs that affect the survival rate output."
        },
        {
            "question": "An animal with thick fur is placed in a hot desert environment. What does the model predict will happen to its survival rate?",
            "choices": {
                "A": "Survival rate will be high because fur always helps animals survive",
                "B": "Survival rate will be low because the body structure does not match the environment",
                "C": "Survival rate will stay the same because fur does not affect survival",
                "D": "Survival rate depends only on how fast the animal can run"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model showed that survival rate drops when body structures do not match the environment. Thick fur would overheat an animal in a desert.",
            "feedback_incorrect": "The same body structure can help or hurt survival depending on the environment. Thick fur is great in the Arctic but harmful in a desert because it traps too much heat."
        },
        {
            "question": "Which statement best describes the relationship between body structure and survival?",
            "choices": {
                "A": "Animals with any body structure can survive anywhere",
                "B": "Only external structures matter for survival, not internal structures",
                "C": "Animals with structures that match their environment's dangers have the best chance of survival",
                "D": "Bigger animals always survive better than smaller animals"
            },
            "correct": "C",
            "feedback_correct": "Exactly! The model demonstrated that animals survive best when their body structures match the specific dangers in their environment. A perfect match leads to high survival.",
            "feedback_incorrect": "Survival depends on how well an animal's body structures fit its environment. Both internal and external structures matter, and size alone does not determine survival."
        },
        {
            "question": "A cactus has a thick waxy coating and sharp spines. How do these structures help it survive in the desert?",
            "choices": {
                "A": "The wax keeps it cool and the spines make music in the wind",
                "B": "The wax keeps water inside the plant and the spines protect it from animals that want to eat it",
                "C": "The wax makes it shiny and the spines help it walk",
                "D": "The wax attracts rain and the spines collect sunlight"
            },
            "correct": "B",
            "feedback_correct": "Right! In a dry desert, the waxy coating prevents water loss (function: water conservation) and the spines protect the cactus from thirsty animals (function: defense). Each structure has a survival function.",
            "feedback_incorrect": "Each body structure has a job (function) that helps survival. The waxy coating prevents water from escaping, and the spines protect the cactus from animals trying to eat it for water."
        }
    ]
}

# =============================================================================
# G04-L05: How Does Your Brain Know That's Hot?
# NGSS 4-LS1-2: Use a model to describe that animals receive different types
# of information through their senses, process it in their brain, and respond.
# =============================================================================
L05_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What happens inside your body when you touch something hot?",
            "choices": {
                "A": "Your hand pulls away by magic",
                "B": "Your skin sends a signal through your nerves to your brain, and your brain tells your hand to move",
                "C": "The hot object pushes your hand away",
                "D": "Your bones sense the heat and move your hand automatically"
            },
            "correct": "B",
            "feedback_correct": "That is right! Your skin has sensors that detect heat. They send electrical signals through your nerves to your brain, and your brain sends a message back to your muscles to pull away.",
            "feedback_incorrect": "When you touch something hot, sensors in your skin detect the heat and send electrical signals through your nerves. Your brain processes the signal and tells your muscles to react."
        },
        {
            "question": "How many senses do humans have?",
            "choices": {
                "A": "Two: seeing and hearing",
                "B": "Three: seeing, hearing, and smelling",
                "C": "Five: seeing, hearing, smelling, tasting, and touching",
                "D": "One: feeling"
            },
            "correct": "C",
            "feedback_correct": "Correct! Humans have five main senses: sight (eyes), hearing (ears), smell (nose), taste (tongue), and touch (skin). Each sense detects different types of information.",
            "feedback_incorrect": "Humans have five main senses: seeing with our eyes, hearing with our ears, smelling with our nose, tasting with our tongue, and touching with our skin."
        },
        {
            "question": "What are nerves?",
            "choices": {
                "A": "The muscles in your arms and legs",
                "B": "Thin fibers in your body that carry signals between your brain and other body parts",
                "C": "The bones that protect your brain",
                "D": "A feeling you get when you are scared"
            },
            "correct": "B",
            "feedback_correct": "Right! Nerves are like electrical wires inside your body. They carry signals from your senses to your brain and from your brain back to your muscles.",
            "feedback_incorrect": "In science, nerves are thin fibers in your body that carry electrical signals. They connect your senses to your brain and your brain to your muscles."
        },
        {
            "question": "Why do you think your hand pulls back from a hot stove SO fast, even before you feel the pain?",
            "choices": {
                "A": "Because your hand has its own brain",
                "B": "Because the stove pushes your hand away",
                "C": "Because your body has a fast emergency response system",
                "D": "Because your eyes see the stove and tell your hand to move"
            },
            "correct": "C",
            "feedback_correct": "Exactly! Your body has reflexes, a fast emergency response system. Some signals are so urgent that your spinal cord triggers a response even before the signal reaches your brain!",
            "feedback_incorrect": "Your body has an emergency system called a reflex. For serious dangers, the signal does not even have to reach your brain first. Your spinal cord can trigger the response to pull away instantly."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the model, Heat Source Intensity is an external component. What does that mean?",
            "choices": {
                "A": "The heat comes from outside the house",
                "B": "It is the input we can change to see how the body's nervous system responds",
                "C": "It is the least important part of the model",
                "D": "It only works when the temperature is very high"
            },
            "correct": "B",
            "feedback_correct": "Right! Heat source intensity is the external component because it is the input we control. We change it (warm cup vs. hot stove vs. boiling water) to see how nerve signal speed and brain response time change.",
            "feedback_incorrect": "In the model, external components are inputs we can set. Heat source intensity is external because we change it to observe how the nervous system responds."
        },
        {
            "question": "What is the correct order of events when you touch something hot?",
            "choices": {
                "A": "Brain responds, nerve sends signal, skin detects heat",
                "B": "Skin detects heat, nerve sends signal, brain responds and triggers muscle movement",
                "C": "Muscles move hand, then brain processes, then skin detects",
                "D": "Brain detects heat, sends signal to skin, muscles move"
            },
            "correct": "B",
            "feedback_correct": "Exactly! The chain is: sensory receptors in skin detect heat, nerves carry an electrical signal to the brain, and the brain processes the danger and tells muscles to respond.",
            "feedback_incorrect": "The correct order is: skin sensors detect heat first, then nerves carry the signal to the brain, and then the brain processes the danger and sends a signal to muscles to react."
        },
        {
            "question": "The model shows that when heat source intensity increases, nerve signals travel faster and brain response time gets quicker. Why?",
            "choices": {
                "A": "Because hotter objects make nerves grow longer",
                "B": "Because the body treats more intense heat as a greater emergency and prioritizes a fast response",
                "C": "Because brain response time never changes",
                "D": "Because cooler objects make nerves work faster"
            },
            "correct": "B",
            "feedback_correct": "Correct! Greater danger triggers stronger, faster signals because the body's survival system treats high heat as an emergency. The nervous system is built for speed when danger is high.",
            "feedback_incorrect": "More intense heat means greater danger. The body's nervous system responds to emergencies by sending signals faster and reacting more quickly to protect you."
        },
        {
            "question": "A reflex is a response that happens before the signal even reaches your brain. Why is this important for survival?",
            "choices": {
                "A": "It lets you think about the danger carefully before reacting",
                "B": "It saves time in an emergency by letting your spinal cord trigger a response instantly",
                "C": "It means your brain does not have to do any work",
                "D": "It only works for cold objects, not hot ones"
            },
            "correct": "B",
            "feedback_correct": "Right! Reflexes save precious time. Instead of the signal traveling all the way to the brain and back, the spinal cord can trigger muscle movement immediately. This protects you from serious burns and injuries.",
            "feedback_incorrect": "Reflexes are emergency shortcuts. The spinal cord triggers the response without waiting for the brain, saving time and protecting the body from serious harm."
        }
    ]
}

# =============================================================================
# G04-L06: Why Are There Seashells on Mountains?
# NGSS 4-ESS1-1: Identify evidence from patterns in rock formations and
# fossils in rock layers to support an explanation for changes in a landscape.
# =============================================================================
L06_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is a fossil?",
            "choices": {
                "A": "A type of rock that looks like an animal",
                "B": "A living animal that lives inside rocks",
                "C": "The preserved remains or trace of a living thing from long ago",
                "D": "A bone from an animal that died last year"
            },
            "correct": "C",
            "feedback_correct": "That is right! A fossil is the preserved remains or trace of a living thing from long ago. Fossils form when living things get buried in sediment that hardens into rock over millions of years.",
            "feedback_incorrect": "A fossil is not a living thing or a recent bone. It is the preserved remains or trace of something that lived long ago, found in rock that formed over millions of years."
        },
        {
            "question": "How do you think seashells could end up on top of a mountain?",
            "choices": {
                "A": "Birds carried them up there",
                "B": "People left them there during a hike",
                "C": "The mountain was once under the ocean and the land was pushed up over time",
                "D": "The seashells grew on the mountain like plants"
            },
            "correct": "C",
            "feedback_correct": "Correct! Many mountains were once ocean floor. Over millions of years, forces inside the Earth pushed the rock layers (with their fossils) upward, creating mountains.",
            "feedback_incorrect": "Finding ocean fossils on mountaintops is evidence that those mountains were once under the ocean. Earth's forces slowly pushed the ocean floor rock upward over millions of years."
        },
        {
            "question": "What is sediment?",
            "choices": {
                "A": "A type of glue that holds rocks together",
                "B": "Tiny pieces of rock, sand, mud, and shells that settle in layers",
                "C": "A fossil that has been broken into pieces",
                "D": "Hot liquid rock that comes out of volcanoes"
            },
            "correct": "B",
            "feedback_correct": "Right! Sediment is tiny pieces of rock, sand, mud, and shells that settle and pile up in layers over time. When sediment hardens, it becomes sedimentary rock.",
            "feedback_incorrect": "Sediment is made of tiny pieces of rock, sand, mud, and shell fragments that settle in layers. Over millions of years, these layers get pressed together and harden into rock."
        },
        {
            "question": "How long do you think it takes for a fossil to form?",
            "choices": {
                "A": "A few days",
                "B": "About one year",
                "C": "A few hundred years",
                "D": "Thousands to millions of years"
            },
            "correct": "D",
            "feedback_correct": "Exactly! Fossils take thousands to millions of years to form. The living thing must be buried in sediment, and the sediment must slowly harden into rock over a very long time.",
            "feedback_incorrect": "Fossil formation is an extremely slow process. It takes thousands to millions of years for sediment to bury a living thing and harden into rock with the fossil inside."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the fossil model, Sediment Buildup and Earth Movement Speed are external components. What does Fossil Exposure (internal) depend on?",
            "choices": {
                "A": "How many people go looking for fossils",
                "B": "Both the amount of sediment that buries organisms and how fast Earth pushes layers upward",
                "C": "Only the weather on the day you look for fossils",
                "D": "The color of the rock layers"
            },
            "correct": "B",
            "feedback_correct": "Right! Fossil exposure depends on both external inputs. Sediment buildup creates fossils by burying organisms, and Earth movement pushes those layers to the surface where erosion reveals them.",
            "feedback_incorrect": "The model shows that fossil exposure depends on both sediment buildup (which creates fossils) and Earth movement speed (which pushes fossil layers to the surface)."
        },
        {
            "question": "A scientist finds fish fossils on top of a mountain. What does this evidence tell us about the mountain's history?",
            "choices": {
                "A": "Fish once flew through the air and landed on the mountain",
                "B": "Someone placed the fish fossils there recently",
                "C": "The rock layers now on top of the mountain were once at the bottom of an ocean",
                "D": "The fish climbed the mountain millions of years ago"
            },
            "correct": "C",
            "feedback_correct": "Exactly! Fish fossils on a mountain are evidence that those rock layers were once underwater. Earth movement pushed the ocean floor rock upward over millions of years to form the mountain.",
            "feedback_incorrect": "Fish fossils on a mountain are powerful evidence that the rock was once ocean floor. Over millions of years, forces inside Earth pushed those rock layers up to become a mountain."
        },
        {
            "question": "Put these events in the correct order for how ocean fossils end up on mountains.",
            "choices": {
                "A": "Earth pushes layers up, then organisms die and get buried, then erosion reveals fossils",
                "B": "Organisms die and get buried in sediment, sediment hardens to rock, Earth pushes rock layers up, erosion reveals fossils at the surface",
                "C": "Erosion reveals fossils, then organisms die, then Earth pushes layers up",
                "D": "Sediment builds up, erosion breaks it apart, then organisms get buried"
            },
            "correct": "B",
            "feedback_correct": "That is right! The correct sequence is: organisms die and get buried in sediment layers, the sediment hardens into rock over time, Earth movement pushes the rock layers upward, and then wind and rain erode the surface to reveal the fossils.",
            "feedback_incorrect": "The correct order is: organisms die and get buried in sediment, sediment turns to rock, Earth movement pushes rock layers upward to form mountains, and then erosion at the surface reveals the ancient fossils."
        },
        {
            "question": "Which rock layer would contain the OLDEST fossils?",
            "choices": {
                "A": "The top layer because it has been there the longest",
                "B": "The bottom layer because it was deposited first",
                "C": "The middle layer because it is the most protected",
                "D": "All layers contain fossils of the same age"
            },
            "correct": "B",
            "feedback_correct": "Correct! The bottom rock layer was deposited first, so it contains the oldest fossils. Each layer above is younger. This is called the law of superposition.",
            "feedback_incorrect": "Rock layers build up from the bottom. The bottom layer was deposited first and is the oldest, so it contains the oldest fossils. Newer layers stack on top."
        }
    ]
}

# =============================================================================
# G04-L07: Can a River Eat a Mountain?
# NGSS 4-ESS2-1: Make observations and/or measurements to provide evidence of
# the effects of weathering or the rate of erosion by water, wind, ice, vegetation.
# =============================================================================
L07_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Can water break apart solid rock?",
            "choices": {
                "A": "No, water is too soft to break anything hard",
                "B": "Yes, but only if the water is boiling hot",
                "C": "Yes, flowing water can slowly wear away even the hardest rock over time",
                "D": "No, only earthquakes can break rocks"
            },
            "correct": "C",
            "feedback_correct": "That is right! Even though water seems soft, flowing water can carry sand and small rocks that grind against larger rocks. Over millions of years, water can carve through mountains.",
            "feedback_incorrect": "Water is more powerful than it seems! Flowing water carries sand and pebbles that grind away rock like sandpaper. Given enough time, water can wear away even the hardest rock."
        },
        {
            "question": "What is erosion?",
            "choices": {
                "A": "When rocks get bigger over time",
                "B": "When broken rock and soil are moved from one place to another by water, wind, or ice",
                "C": "When animals dig holes in the ground",
                "D": "When the Earth shakes during an earthquake"
            },
            "correct": "B",
            "feedback_correct": "Correct! Erosion is the movement of broken rock and soil from one place to another by natural forces like water, wind, or ice.",
            "feedback_incorrect": "Erosion is the process of broken rock and soil being carried away from one place to another. Water, wind, and ice are the main forces that cause erosion."
        },
        {
            "question": "How was the Grand Canyon formed?",
            "choices": {
                "A": "People dug it with shovels a long time ago",
                "B": "An earthquake cracked the ground open all at once",
                "C": "A river slowly carved through the rock over millions of years",
                "D": "A volcano blew a hole in the ground"
            },
            "correct": "C",
            "feedback_correct": "Right! The Colorado River carved the Grand Canyon over about 5 to 6 million years. Flowing water slowly wore away layer after layer of rock.",
            "feedback_incorrect": "The Grand Canyon was not created by a sudden event. The Colorado River slowly carved through the rock over millions of years, cutting deeper and deeper."
        },
        {
            "question": "What is the difference between weathering and erosion?",
            "choices": {
                "A": "They are the same thing",
                "B": "Weathering breaks rock apart, erosion moves the broken pieces away",
                "C": "Weathering is caused by rain and erosion is caused by wind",
                "D": "Weathering only happens to old rocks and erosion only happens to new rocks"
            },
            "correct": "B",
            "feedback_correct": "Exactly! Weathering is the breaking apart of rock. Erosion is the movement of that broken material to a new location. Weathering happens first, then erosion carries the pieces away.",
            "feedback_incorrect": "Weathering and erosion are related but different. Weathering is the breaking down of rock into smaller pieces. Erosion is the movement of those broken pieces to a new place."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the erosion model, Water Flow Speed and Rock Hardness are external components. What is the relationship between Water Flow Speed and Erosion Rate?",
            "choices": {
                "A": "Negative: faster water causes less erosion",
                "B": "Positive: faster water causes more erosion",
                "C": "No relationship: water speed does not affect erosion",
                "D": "It depends on what day of the week it is"
            },
            "correct": "B",
            "feedback_correct": "Right! The relationship is positive. Faster water has more energy and can break apart and carry away more rock. When water flow speed goes up, erosion rate goes up.",
            "feedback_incorrect": "Faster water carries more energy and more force. The model shows a positive relationship: when water flow speed increases, the erosion rate also increases."
        },
        {
            "question": "What is the relationship between Rock Hardness and Erosion Rate?",
            "choices": {
                "A": "Positive: harder rock erodes faster",
                "B": "Negative: harder rock erodes slower",
                "C": "No relationship: rock hardness does not matter",
                "D": "Positive: all rocks erode at the same speed"
            },
            "correct": "B",
            "feedback_correct": "Correct! The relationship is negative. Harder rock is more resistant to erosion, so it erodes more slowly. When rock hardness goes up, erosion rate goes down.",
            "feedback_incorrect": "This is a negative relationship. Harder rock is more resistant to being broken apart. When rock hardness increases, erosion rate decreases."
        },
        {
            "question": "A gentle stream flows over very soft rock for millions of years. What does the model predict will happen?",
            "choices": {
                "A": "Nothing, because the stream is too gentle to cause any erosion",
                "B": "The rock will get harder over time",
                "C": "Even the gentle stream will eventually carve through the soft rock, creating a canyon",
                "D": "The stream will dry up before any erosion happens"
            },
            "correct": "C",
            "feedback_correct": "That is right! Even slow-moving water can erode soft rock over long periods of time. The model shows that soft rock plus any flowing water leads to erosion. Given millions of years, even gentle streams can carve canyons.",
            "feedback_incorrect": "The model shows that even slow water erodes soft rock. Given enough time, even a gentle stream can carve a significant canyon through soft rock."
        },
        {
            "question": "An engineer wants to protect a riverbank from erosion. Based on the model, which approach would work best?",
            "choices": {
                "A": "Make the water flow faster so it passes by quickly",
                "B": "Slow down the water flow and add hard materials like rocks along the bank",
                "C": "Remove all the soil from the riverbank",
                "D": "Make the riverbank out of softer materials so the water flows smoothly"
            },
            "correct": "B",
            "feedback_correct": "Exactly! The model shows two ways to reduce erosion: slow down the water (reduce water flow speed) and increase the hardness of the bank material. Placing rocks along the bank does both.",
            "feedback_incorrect": "The model shows that slower water and harder rock both reduce erosion. So slowing the water AND adding hard materials to the bank is the best engineering solution."
        }
    ]
}

# =============================================================================
# G04-L08: Where Does Your Electricity Come From?
# NGSS 4-ESS3-1: Obtain and combine information to describe that energy and
# fuels are derived from natural resources and their uses affect the environment.
# =============================================================================
L08_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Where does the electricity in your home come from?",
            "choices": {
                "A": "It is created inside the walls of your house",
                "B": "It comes from a power plant that converts natural resources into electricity",
                "C": "It comes directly from the Sun through the windows",
                "D": "It is stored inside the light switches"
            },
            "correct": "B",
            "feedback_correct": "That is right! Electricity is generated at power plants that convert natural resources (like coal, gas, sunlight, or wind) into electrical energy, which then travels through wires to your home.",
            "feedback_incorrect": "Electricity does not come from walls or switches. Power plants convert natural resources into electricity, and wires carry that electricity to homes and buildings."
        },
        {
            "question": "What is a natural resource?",
            "choices": {
                "A": "Something made in a factory",
                "B": "A material from nature that people use, like water, coal, sunlight, or wind",
                "C": "A type of electricity",
                "D": "Something that only exists underground"
            },
            "correct": "B",
            "feedback_correct": "Correct! Natural resources are materials from nature that people use. Examples include water, coal, natural gas, sunlight, wind, and soil.",
            "feedback_incorrect": "Natural resources are not man-made. They are materials found in nature that people use, such as water, sunlight, wind, coal, and natural gas."
        },
        {
            "question": "What is the difference between renewable and nonrenewable energy?",
            "choices": {
                "A": "Renewable energy is more expensive and nonrenewable is free",
                "B": "Renewable energy sources never run out (like sunlight and wind), but nonrenewable sources can be used up (like coal and gas)",
                "C": "Renewable energy is old and nonrenewable is new",
                "D": "There is no real difference between them"
            },
            "correct": "B",
            "feedback_correct": "Right! Renewable energy sources like sunlight, wind, and water replenish naturally and will not run out. Nonrenewable sources like coal, oil, and gas took millions of years to form and can be used up.",
            "feedback_incorrect": "Renewable energy comes from sources that nature replenishes, like sunlight and wind. Nonrenewable energy comes from sources like coal and gas that can run out."
        },
        {
            "question": "How does burning coal affect the environment?",
            "choices": {
                "A": "It has no effect on the environment at all",
                "B": "It makes the air cleaner",
                "C": "It releases pollution and gases that contribute to climate change",
                "D": "It only affects the area right around the power plant"
            },
            "correct": "C",
            "feedback_correct": "Exactly! Burning coal releases pollution, including carbon dioxide and other gases that contribute to climate change and can harm air quality.",
            "feedback_incorrect": "Burning coal does affect the environment. It releases smoke, pollution, and greenhouse gases into the air that can harm air quality and contribute to climate change."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the energy model, Energy Source Amount is an external component. Power Plant Output and Home Electricity are internal components. What chain does this create?",
            "choices": {
                "A": "Home electricity controls how much energy source is available",
                "B": "More energy source leads to more power plant output, which leads to more home electricity",
                "C": "Power plant output has nothing to do with energy source amount",
                "D": "Home electricity creates the energy source"
            },
            "correct": "B",
            "feedback_correct": "Right! The model shows a positive chain: when more natural resource is available, the power plant produces more electricity, and more electricity reaches homes.",
            "feedback_incorrect": "The model shows a cause-and-effect chain: more energy source available means the power plant can produce more output, which means more electricity reaches homes."
        },
        {
            "question": "A town relies on solar panels for electricity. It has been cloudy for a week. What does the model predict?",
            "choices": {
                "A": "The solar panels will work even better because they are rested",
                "B": "Power plant output and home electricity will both decrease because the energy source (sunlight) is low",
                "C": "Home electricity will increase because clouds store energy",
                "D": "Nothing changes because solar panels do not need sunlight"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model shows that when the energy source amount decreases (less sunlight), power plant output drops, and home electricity also drops. This is a challenge of solar energy.",
            "feedback_incorrect": "Solar panels need sunlight to generate electricity. When clouds block the sun, the energy source is reduced, so the power plant produces less electricity and homes receive less."
        },
        {
            "question": "Which energy plan would give a town the MOST reliable electricity while being kindest to the environment?",
            "choices": {
                "A": "Use only coal because it works day and night",
                "B": "Use only solar because it is clean",
                "C": "Use a mix of solar and wind so that when one source is low, the other may be available",
                "D": "Do not use any electricity to protect the environment"
            },
            "correct": "C",
            "feedback_correct": "Exactly! A mix of renewable sources provides more reliability. If the sun is not shining, the wind might be blowing. Combining sources helps ensure the town always has clean electricity.",
            "feedback_incorrect": "Using just one source has weaknesses. Coal pollutes, and solar only works when sunny. A mix of clean sources like solar and wind is more reliable because they cover for each other."
        },
        {
            "question": "Why is it important to know that ALL energy sources affect the environment in some way?",
            "choices": {
                "A": "Because it means we should stop using all electricity",
                "B": "Because it helps us make informed choices about which energy sources to use and how to reduce harm",
                "C": "Because it proves that natural resources are not real",
                "D": "Because it means renewable energy is just as bad as fossil fuels"
            },
            "correct": "B",
            "feedback_correct": "Right! Understanding that every energy source has trade-offs helps us make better choices. Renewable sources have fewer environmental impacts than fossil fuels, even though they still need space and materials.",
            "feedback_incorrect": "Knowing about environmental impacts helps us make better decisions. We cannot stop using energy, but we can choose sources with less impact and find ways to reduce harm."
        }
    ]
}

# =============================================================================
# G04-L09: Can We Stop an Earthquake from Breaking Buildings?
# NGSS 4-ESS3-2: Generate and compare multiple solutions to reduce the impacts
# of natural Earth processes on humans.
# =============================================================================
L09_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What causes an earthquake?",
            "choices": {
                "A": "Heavy trucks driving on the roads",
                "B": "Movement of large pieces of rock deep beneath Earth's surface",
                "C": "Strong wind blowing against the ground",
                "D": "Too many buildings in one area"
            },
            "correct": "B",
            "feedback_correct": "That is right! Earthquakes happen when large pieces of Earth's crust (tectonic plates) move, slide, or bump against each other deep underground, causing the ground to shake.",
            "feedback_incorrect": "Earthquakes are not caused by things on the surface. They happen when huge pieces of rock deep underground shift and release energy, making the ground shake."
        },
        {
            "question": "Can engineers stop earthquakes from happening?",
            "choices": {
                "A": "Yes, they can prevent all earthquakes",
                "B": "Yes, but only small ones",
                "C": "No, but they can design buildings to survive them",
                "D": "No, and there is nothing anyone can do about earthquake damage"
            },
            "correct": "C",
            "feedback_correct": "Correct! Engineers cannot prevent earthquakes because they are caused by natural forces deep underground. But engineers CAN design buildings and structures that survive shaking.",
            "feedback_incorrect": "Nobody can stop earthquakes. But engineers have found ways to design buildings that can survive even strong earthquakes by using special building techniques."
        },
        {
            "question": "What is a natural hazard?",
            "choices": {
                "A": "Any danger caused by people",
                "B": "A natural event like an earthquake, flood, or hurricane that can harm people",
                "C": "A hazard sign posted in a park",
                "D": "A dangerous animal in the wild"
            },
            "correct": "B",
            "feedback_correct": "Right! A natural hazard is a natural event, like an earthquake, flood, volcano eruption, or hurricane, that has the potential to harm people and property.",
            "feedback_incorrect": "A natural hazard is a natural event, not a human-caused danger. Earthquakes, floods, and hurricanes are examples of natural hazards that can harm people and property."
        },
        {
            "question": "Why do some buildings fall down during earthquakes while others stay standing?",
            "choices": {
                "A": "The fallen buildings were older and the standing ones were newer",
                "B": "It depends on luck and nothing else",
                "C": "The standing buildings were designed with special features to handle shaking",
                "D": "The earthquake only shook certain blocks and skipped others"
            },
            "correct": "C",
            "feedback_correct": "Exactly! Buildings that survive earthquakes are usually designed with special engineering features like flexibility, strong foundations, and cross-bracing that help them absorb and withstand shaking.",
            "feedback_incorrect": "Building design makes a big difference. Buildings with special engineering features, like flexible frames and strong foundations, are much more likely to survive earthquake shaking."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the earthquake model, what is the relationship between Earthquake Strength and Damage Level?",
            "choices": {
                "A": "Negative: stronger earthquakes cause less damage",
                "B": "Positive: stronger earthquakes cause more damage",
                "C": "No relationship: earthquake strength does not affect damage",
                "D": "The relationship changes every time"
            },
            "correct": "B",
            "feedback_correct": "Right! The relationship is positive. As earthquake strength increases, damage level also increases. Stronger shaking causes more destruction.",
            "feedback_incorrect": "Stronger earthquakes release more energy and cause more shaking. The model shows a positive relationship: more earthquake strength means more damage."
        },
        {
            "question": "What is the relationship between Building Flexibility and Damage Level?",
            "choices": {
                "A": "Positive: more flexible buildings have more damage",
                "B": "Negative: more flexible buildings have less damage",
                "C": "No relationship: flexibility does not matter",
                "D": "Flexible buildings always collapse"
            },
            "correct": "B",
            "feedback_correct": "Correct! The relationship is negative. When building flexibility increases, damage decreases. Flexible buildings sway WITH the earthquake instead of fighting against it.",
            "feedback_incorrect": "More flexibility means less damage. Flexible buildings bend and sway with the shaking instead of cracking. This is a negative relationship: flexibility goes up, damage goes down."
        },
        {
            "question": "Two buildings face the same strong earthquake. Building A is stiff and rigid. Building B is flexible with base isolation pads. Which building will likely have LESS damage, and why?",
            "choices": {
                "A": "Building A, because stiff buildings are stronger than flexible ones",
                "B": "Building B, because it can sway with the earthquake and the base pads absorb shaking energy",
                "C": "Both will have the same damage because the earthquake was the same strength",
                "D": "Building A, because base isolation pads make buildings weaker"
            },
            "correct": "B",
            "feedback_correct": "Exactly! Building B will have less damage. Flexible buildings sway with the earthquake, and base isolation pads absorb shaking energy. The model shows that flexibility reduces damage even in strong earthquakes.",
            "feedback_incorrect": "The model shows that stiff buildings crack because they fight against the shaking. Flexible buildings with base isolators absorb the energy and experience less damage."
        },
        {
            "question": "An engineer is asked to design a new school in earthquake country. Based on the model, what is the MOST important design feature to include?",
            "choices": {
                "A": "Very thick, rigid concrete walls that resist all movement",
                "B": "Flexibility features like cross-bracing and a strong but bendable frame",
                "C": "Extra heavy materials to keep the building from shaking",
                "D": "Windows that open during earthquakes to let the shaking out"
            },
            "correct": "B",
            "feedback_correct": "Right! The model clearly shows that flexibility reduces damage. Cross-bracing, flexible frames, and base isolation help buildings absorb earthquake energy instead of cracking.",
            "feedback_incorrect": "The model shows that stiff, rigid buildings suffer more damage. The best design includes flexibility features like cross-bracing and bendable frames that absorb earthquake energy."
        }
    ]
}

# =============================================================================
# G04-L10: Why Do Marbles Crash and Bounce?
# NGSS 4-PS3-3: Ask questions and predict outcomes about the changes in energy
# that occur when objects collide.
# =============================================================================
L10_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "When a moving marble hits a marble that is sitting still, what happens?",
            "choices": {
                "A": "Both marbles stop moving completely",
                "B": "The moving marble stops or slows down, and the still marble starts moving",
                "C": "The still marble disappears",
                "D": "Nothing happens because marbles are too small to have energy"
            },
            "correct": "B",
            "feedback_correct": "That is right! When a moving marble hits a still marble, energy transfers from the moving one to the still one. The first marble slows down, and the second marble starts moving.",
            "feedback_incorrect": "When a moving marble hits a still one, the energy moves from the first marble to the second. The first marble slows down or stops, and the second marble starts rolling."
        },
        {
            "question": "What is energy transfer?",
            "choices": {
                "A": "When energy is created from nothing",
                "B": "When energy moves from one object to another",
                "C": "When energy disappears forever",
                "D": "When energy turns into a solid object"
            },
            "correct": "B",
            "feedback_correct": "Correct! Energy transfer is when energy moves from one object to another. During a collision, the moving object gives some or all of its energy to the object it hits.",
            "feedback_incorrect": "Energy is never created or destroyed. Energy transfer means energy moves from one object to another, like from a moving marble to a still marble during a collision."
        },
        {
            "question": "If you roll a marble slowly and it taps another marble, what do you think will happen compared to rolling it fast?",
            "choices": {
                "A": "The slow marble and the fast marble will have the exact same effect",
                "B": "The slow marble will make the other marble move less than the fast marble would",
                "C": "The slow marble will make the other marble move more because it is gentler",
                "D": "Speed does not matter at all in a collision"
            },
            "correct": "B",
            "feedback_correct": "Right! A slower marble has less energy, so it transfers less energy to the other marble. A faster marble has more energy and causes a stronger collision.",
            "feedback_incorrect": "Speed matters in collisions. A slow marble has less energy to transfer, so the marble it hits will move less. A fast marble carries more energy and creates a stronger impact."
        },
        {
            "question": "When two marbles crash and you hear a clicking sound, where does that sound come from?",
            "choices": {
                "A": "The marbles are talking to each other",
                "B": "Some of the collision energy turns into sound energy",
                "C": "The air makes the sound, not the marbles",
                "D": "The sound was already there before the collision"
            },
            "correct": "B",
            "feedback_correct": "Exactly! The clicking sound is energy! During a collision, some energy transforms into sound energy (the click you hear) and a tiny bit into heat energy.",
            "feedback_incorrect": "The clicking sound is actually energy being transformed. During a collision, some of the motion energy changes into sound energy, which is the click you hear."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the collision model, Marble Speed is an external component. What are the two internal components?",
            "choices": {
                "A": "Marble color and marble size",
                "B": "Collision force and energy transfer",
                "C": "Table height and room temperature",
                "D": "Sound volume and marble weight"
            },
            "correct": "B",
            "feedback_correct": "Right! Collision force and energy transfer are the internal components. They respond to changes in marble speed. Faster marble speed causes greater collision force, which causes more energy transfer.",
            "feedback_incorrect": "The model's internal components are collision force and energy transfer. They change in response to the external component (marble speed)."
        },
        {
            "question": "The model shows that when marble speed increases, collision force increases, and energy transfer increases. What type of relationships are these?",
            "choices": {
                "A": "Negative relationships because collisions destroy energy",
                "B": "Positive relationships because when one goes up, the next goes up too",
                "C": "No relationships because the components are not connected",
                "D": "Random relationships that change unpredictably"
            },
            "correct": "B",
            "feedback_correct": "Correct! These are positive relationships. More speed leads to more collision force, which leads to more energy transfer. All three increase together in a cause-and-effect chain.",
            "feedback_incorrect": "When one component increases and the next component also increases, that is a positive relationship. Speed, force, and energy transfer all increase together."
        },
        {
            "question": "A fast-moving marble hits a still marble. The fast marble stops completely and the still marble rolls away at the same speed. What happened to the energy?",
            "choices": {
                "A": "The energy was destroyed in the collision",
                "B": "New energy was created for the second marble",
                "C": "The energy transferred from the first marble to the second marble",
                "D": "Both marbles created their own energy"
            },
            "correct": "C",
            "feedback_correct": "Exactly! Energy was transferred, not created or destroyed. The first marble's kinetic energy moved to the second marble. The total energy stayed the same, it just changed location.",
            "feedback_incorrect": "Energy is never created or destroyed. In this collision, the motion energy transferred from the moving marble to the still marble. The total energy in the system stays the same."
        },
        {
            "question": "A student rolls a marble from a tall ramp and it collides with a still marble. Then the student rolls a marble from a short ramp into another still marble. Which collision will transfer MORE energy, and why?",
            "choices": {
                "A": "The short ramp, because the marble had more time to build energy",
                "B": "Both will transfer the same amount of energy",
                "C": "The tall ramp, because the marble rolls faster and has more kinetic energy to transfer",
                "D": "Neither will transfer energy because marbles are too light"
            },
            "correct": "C",
            "feedback_correct": "Right! The marble from the tall ramp has more speed and more kinetic energy. More kinetic energy means a stronger collision force, which means more energy transfers to the still marble.",
            "feedback_incorrect": "A taller ramp gives the marble more speed (more kinetic energy). The model shows that more speed leads to more collision force and more energy transfer."
        }
    ]
}


# =============================================================================
# Combined dictionary for all Grade 4 lessons
# =============================================================================
ALL_QUESTIONS = {
    "G04-L01": L01_QUESTIONS,
    "G04-L02": L02_QUESTIONS,
    "G04-L03": L03_QUESTIONS,
    "G04-L04": L04_QUESTIONS,
    "G04-L05": L05_QUESTIONS,
    "G04-L06": L06_QUESTIONS,
    "G04-L07": L07_QUESTIONS,
    "G04-L08": L08_QUESTIONS,
    "G04-L09": L09_QUESTIONS,
    "G04-L10": L10_QUESTIONS,
}
