#!/usr/bin/env python3
"""Multiple choice pre/post assessment questions for Grade 7 ModelIt! Lessons"""

# ── G07-L01: Blood Moon: When the Sky Turns Red ──────────────────
L01_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What causes the Moon to appear to change shape throughout the month?",
            "choices": {
                "A": "Earth's shadow falls on different parts of the Moon each night",
                "B": "We see different amounts of the Moon's sunlit side as it orbits Earth",
                "C": "The Moon rotates and shows us different sides each night",
                "D": "Clouds in Earth's atmosphere block parts of the Moon"
            },
            "correct": "B",
            "feedback_correct": "Correct! As the Moon orbits Earth, the angle between the Sun, Moon, and Earth changes, so we see different amounts of the Moon's sunlit surface.",
            "feedback_incorrect": "Not quite. Moon phases are caused by seeing different portions of the Moon's sunlit side as it orbits Earth, not by Earth's shadow, rotation showing different sides, or clouds."
        },
        {
            "question": "Where does the light we see from the Moon actually come from?",
            "choices": {
                "A": "The Moon generates its own light like a star",
                "B": "The Moon glows because of radioactive minerals on its surface",
                "C": "The Moon reflects light from the Sun",
                "D": "Light from distant stars bounces off the Moon"
            },
            "correct": "C",
            "feedback_correct": "Correct! The Moon has no light of its own. What we call moonlight is sunlight reflecting off the Moon's surface.",
            "feedback_incorrect": "Not quite. The Moon does not produce its own light. Moonlight is actually sunlight that reflects off the Moon's surface back toward Earth."
        },
        {
            "question": "How long does it take the Moon to complete one full orbit around Earth?",
            "choices": {
                "A": "About 24 hours",
                "B": "About 7 days",
                "C": "About 29.5 days",
                "D": "About 365 days"
            },
            "correct": "C",
            "feedback_correct": "Correct! The Moon's orbital period is approximately 29.5 days, which is why the cycle of Moon phases repeats roughly every month.",
            "feedback_incorrect": "Not quite. The Moon takes about 29.5 days to orbit Earth once, which is why we see a full cycle of phases approximately every month."
        },
        {
            "question": "What force keeps the Moon in orbit around Earth?",
            "choices": {
                "A": "Magnetism from Earth's core",
                "B": "The push of solar wind from the Sun",
                "C": "Gravity between Earth and the Moon",
                "D": "The Moon's own spinning motion"
            },
            "correct": "C",
            "feedback_correct": "Correct! Gravity is the attractive force between Earth and the Moon that keeps the Moon in a stable orbit.",
            "feedback_incorrect": "Not quite. Gravity is the force responsible for keeping the Moon in orbit around Earth. It is the attractive force between all objects with mass."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "During a lunar eclipse, the Moon appears red instead of disappearing completely. Which explanation best accounts for this observation?",
            "choices": {
                "A": "The Sun emits red light that passes through the Moon's interior",
                "B": "Earth's atmosphere bends red wavelengths of sunlight into Earth's shadow",
                "C": "The Moon's surface minerals glow red when they cool down in shadow",
                "D": "Mars reflects red light onto the Moon during eclipse alignment"
            },
            "correct": "B",
            "feedback_correct": "Correct! Earth's atmosphere acts like a lens, refracting red wavelengths of sunlight into the shadow zone. Blue and green wavelengths scatter away, but red light bends enough to reach the Moon.",
            "feedback_incorrect": "Not quite. During a lunar eclipse, Earth's atmosphere bends red wavelengths of sunlight into the shadow. It is essentially projecting all of Earth's sunsets onto the Moon at once."
        },
        {
            "question": "A student claims that we should see a lunar eclipse every month during the full Moon. Why is this claim incorrect?",
            "choices": {
                "A": "The Moon only passes through Earth's shadow during summer months",
                "B": "The Moon's orbit is tilted about 5 degrees relative to Earth's orbit around the Sun",
                "C": "Earth's shadow is too small to cover the Moon most months",
                "D": "The Sun moves out of alignment with Earth and the Moon after each eclipse"
            },
            "correct": "B",
            "feedback_correct": "Correct! Because the Moon's orbit is tilted about 5 degrees, the Moon usually passes above or below Earth's shadow during full Moon. Eclipses only occur when the Moon crosses the plane of Earth's orbit at the right time.",
            "feedback_incorrect": "Not quite. Eclipses are rare because the Moon's orbit is tilted about 5 degrees relative to Earth's orbital plane. Most months, the Moon passes above or below Earth's shadow."
        },
        {
            "question": "In a model of the Earth-Moon-Sun system, a student sets the Moon's position directly between Earth and the Sun. What phase will the model predict?",
            "choices": {
                "A": "Full Moon, because the Moon is closest to the Sun",
                "B": "Waxing crescent, because the Moon is partially lit",
                "C": "New Moon, because the sunlit side of the Moon faces away from Earth",
                "D": "Lunar eclipse, because the Moon is in Earth's shadow"
            },
            "correct": "C",
            "feedback_correct": "Correct! When the Moon is between Earth and the Sun, the sunlit side faces away from us, making the Moon invisible from Earth. This is a new Moon.",
            "feedback_incorrect": "Not quite. When the Moon is positioned between Earth and the Sun, the side of the Moon that faces Earth is not illuminated. This configuration produces a new Moon."
        },
        {
            "question": "Which statement best describes the role of gravity in the Earth-Moon-Sun system?",
            "choices": {
                "A": "Gravity only affects the Moon during eclipses when objects are aligned",
                "B": "Gravity keeps the Moon orbiting Earth and Earth orbiting the Sun, creating the patterns we observe",
                "C": "Gravity pushes the Moon away from Earth, causing it to move through phases",
                "D": "Gravity has no effect on the Moon because there is no air in space to transmit force"
            },
            "correct": "B",
            "feedback_correct": "Correct! Gravity is the fundamental force that maintains the orbital motions of the entire system. Without gravity, there would be no orbits, no phases, no eclipses, and no tides.",
            "feedback_incorrect": "Not quite. Gravity is the attractive force that keeps the Moon orbiting Earth and Earth orbiting the Sun. It acts continuously, not just during eclipses, and it works through empty space."
        }
    ]
}

# ── G07-L02: Your Inner Fish ─────────────────────────────────────
L02_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is a fossil?",
            "choices": {
                "A": "Any rock that is more than 1,000 years old",
                "B": "The preserved remains or traces of an ancient organism found in rock",
                "C": "A mineral that forms in the shape of a living thing by coincidence",
                "D": "A bone from a dinosaur that has turned into calcium powder"
            },
            "correct": "B",
            "feedback_correct": "Correct! Fossils are the preserved remains or traces of organisms that lived in the past, typically found embedded in sedimentary rock.",
            "feedback_incorrect": "Not quite. A fossil is the preserved remains or traces of an ancient organism, such as bones, shells, or imprints, found in rock."
        },
        {
            "question": "A whale's flipper, a bat's wing, and a human arm all contain the same basic bone structure. What might this suggest?",
            "choices": {
                "A": "These animals all live in the same habitat",
                "B": "These animals evolved from a common ancestor that had that bone structure",
                "C": "These animals copied each other's bone design over time",
                "D": "Having the same bones is just a random coincidence"
            },
            "correct": "B",
            "feedback_correct": "Correct! Shared bone structures, called homologous structures, are strong evidence that these animals inherited their basic body plan from a common ancestor.",
            "feedback_incorrect": "Not quite. When very different animals share the same underlying bone structure, it is evidence of common ancestry. These are called homologous structures."
        },
        {
            "question": "How do scientists determine which organisms are related to each other?",
            "choices": {
                "A": "By looking at whether animals live in the same area today",
                "B": "By comparing body structures, DNA, and fossil evidence",
                "C": "By checking if animals eat the same food",
                "D": "By asking zookeepers which animals look alike"
            },
            "correct": "B",
            "feedback_correct": "Correct! Scientists use multiple types of evidence including anatomy, DNA sequences, and the fossil record to determine evolutionary relationships.",
            "feedback_incorrect": "Not quite. Scientists determine evolutionary relationships by comparing body structures (anatomy), DNA sequences, and fossil evidence, not just by appearance or habitat."
        },
        {
            "question": "What happens to most organisms after they die?",
            "choices": {
                "A": "They automatically become fossils within a few years",
                "B": "They decompose and are not preserved as fossils",
                "C": "They are always preserved if they are buried underground",
                "D": "Only dinosaurs can become fossils"
            },
            "correct": "B",
            "feedback_correct": "Correct! Most organisms decompose completely after death. Fossilization is actually very rare and requires specific conditions like rapid burial in sediment.",
            "feedback_incorrect": "Not quite. The vast majority of organisms decompose and leave no fossil record. Fossilization is extremely rare and requires rapid burial under the right conditions."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "Tiktaalik is a 375-million-year-old fossil that has fish features (scales, fins) AND land animal features (flat head, wrist bones). What type of fossil is this?",
            "choices": {
                "A": "An index fossil used only for dating rock layers",
                "B": "A transitional fossil showing features of both an ancestral and a descendant group",
                "C": "A trace fossil showing only the footprints of an ancient animal",
                "D": "A modern fossil that formed recently from a living species"
            },
            "correct": "B",
            "feedback_correct": "Correct! Tiktaalik is a transitional fossil because it shows features of both fish (ancestral group) and land vertebrates (descendant group), providing evidence of evolutionary transition.",
            "feedback_incorrect": "Not quite. Tiktaalik is classified as a transitional fossil because it displays characteristics of both fish and land animals, bridging the evolutionary gap between these groups."
        },
        {
            "question": "In a model of evolutionary change, environmental change rate is set to maximum, simulating a mass extinction event. What does the model predict will happen to species diversity?",
            "choices": {
                "A": "Species diversity increases because organisms evolve faster under pressure",
                "B": "Species diversity stays the same because organisms always adapt",
                "C": "Species diversity drops sharply as many species cannot adapt fast enough",
                "D": "Species diversity is unaffected because evolution is too slow to notice"
            },
            "correct": "C",
            "feedback_correct": "Correct! Rapid environmental change causes mass extinction because many species cannot adapt fast enough. However, after the change stabilizes, surviving species can diversify into empty ecological niches.",
            "feedback_incorrect": "Not quite. When environmental change is rapid and extreme, many species go extinct because they cannot adapt quickly enough, causing species diversity to crash."
        },
        {
            "question": "A student asks: 'If humans evolved from fish, why do fish still exist?' Which response best addresses this misconception?",
            "choices": {
                "A": "Fish will eventually evolve into humans if given enough time",
                "B": "Humans did not evolve from modern fish; both evolved from a common ancestor millions of years ago",
                "C": "Fish stopped evolving because their environment has not changed",
                "D": "Only certain special fish evolved into humans while the rest stayed the same"
            },
            "correct": "B",
            "feedback_correct": "Correct! Humans and modern fish share a common ancestor from about 375 million years ago. Both lineages have been evolving separately since then. Modern fish are not our ancestors; they are our very distant evolutionary cousins.",
            "feedback_incorrect": "Not quite. Humans did not evolve from modern fish. Both humans and today's fish descended from a common ancestor. The two lineages have been evolving independently for hundreds of millions of years."
        },
        {
            "question": "Which pattern in the fossil record provides the strongest evidence that life on Earth has changed over time?",
            "choices": {
                "A": "All fossils look identical regardless of the rock layer they are found in",
                "B": "Older rock layers contain simpler organisms, while younger layers contain more complex ones",
                "C": "Fossils are only found in volcanic rock from eruptions",
                "D": "The same exact species appears in every rock layer across Earth's history"
            },
            "correct": "B",
            "feedback_correct": "Correct! The fossil record shows a clear pattern: the oldest layers contain simple, single-celled organisms, and complexity increases in younger layers. This documents how life has changed and diversified over billions of years.",
            "feedback_incorrect": "Not quite. The fossil record shows that simpler organisms appear in older rock layers and more complex organisms appear in younger layers, demonstrating that life has changed over geological time."
        }
    ]
}

# ── G07-L03: Earth Has a Fever ───────────────────────────────────
L03_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is the greenhouse effect?",
            "choices": {
                "A": "When greenhouses release chemicals that warm the atmosphere",
                "B": "When certain gases in the atmosphere trap heat from the Sun, warming Earth's surface",
                "C": "When the Sun's rays are reflected by green plants back into space",
                "D": "When Earth's temperature drops because clouds block sunlight"
            },
            "correct": "B",
            "feedback_correct": "Correct! The greenhouse effect occurs when gases like CO2 and methane in the atmosphere trap heat energy, keeping Earth's surface warmer than it would otherwise be.",
            "feedback_incorrect": "Not quite. The greenhouse effect is the process by which certain atmospheric gases (like CO2 and methane) trap heat radiated from Earth's surface, warming the planet."
        },
        {
            "question": "Which human activity contributes MOST to increasing carbon dioxide in the atmosphere?",
            "choices": {
                "A": "Planting new forests and gardens",
                "B": "Burning fossil fuels like coal, oil, and natural gas",
                "C": "Recycling plastic bottles and aluminum cans",
                "D": "Building taller skyscrapers in cities"
            },
            "correct": "B",
            "feedback_correct": "Correct! Burning fossil fuels for energy, transportation, and industry is the largest source of human-caused CO2 emissions.",
            "feedback_incorrect": "Not quite. Burning fossil fuels (coal, oil, natural gas) for energy and transportation is the primary human activity that increases atmospheric CO2."
        },
        {
            "question": "What is the difference between weather and climate?",
            "choices": {
                "A": "Weather and climate mean the same thing",
                "B": "Weather is long-term patterns; climate is what happens today",
                "C": "Weather is short-term, local conditions; climate is long-term, global patterns",
                "D": "Climate only applies to tropical regions; weather applies everywhere"
            },
            "correct": "C",
            "feedback_correct": "Correct! Weather describes short-term, local atmospheric conditions (today's temperature), while climate describes long-term patterns averaged over decades or more.",
            "feedback_incorrect": "Not quite. Weather is the short-term state of the atmosphere in a specific place (daily temperature, rain). Climate is the long-term average pattern over decades across a region or globally."
        },
        {
            "question": "Why do you think ice at the North and South Poles has been melting in recent decades?",
            "choices": {
                "A": "The Sun has been getting significantly hotter each year",
                "B": "Ocean currents have shifted and now carry warm water to the poles",
                "C": "Increased greenhouse gases are trapping more heat, raising global temperatures",
                "D": "Volcanic eruptions under the ice are melting it from below"
            },
            "correct": "C",
            "feedback_correct": "Correct! Rising concentrations of greenhouse gases in the atmosphere are trapping more heat, causing global temperatures to rise and polar ice to melt.",
            "feedback_incorrect": "Not quite. The primary driver of polar ice melt in recent decades is the increase in greenhouse gas concentrations (especially CO2) that trap more heat and raise global temperatures."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In your climate model, CO2 concentration is increased from 280 ppm (pre-industrial) to 420 ppm (current levels). Which cascade of effects does the model predict?",
            "choices": {
                "A": "Temperature decreases, ice sheets grow, sea level drops",
                "B": "Temperature rises, ice sheets melt, which exposes dark ocean that absorbs more heat",
                "C": "Temperature stays the same because Earth's systems are perfectly balanced",
                "D": "Ice sheets grow thicker because warmer air holds more moisture for snowfall"
            },
            "correct": "B",
            "feedback_correct": "Correct! More CO2 traps more heat, raising temperatures. Higher temperatures melt ice sheets, exposing dark ocean that absorbs even more heat, creating a positive feedback loop that accelerates warming.",
            "feedback_incorrect": "Not quite. Increasing CO2 traps more heat (greenhouse effect), which raises temperatures, melts ice, and exposes dark surfaces that absorb more heat. This positive feedback loop accelerates climate change."
        },
        {
            "question": "A classmate says: 'It was really cold last week, so climate change is not real.' Which response uses the best scientific reasoning?",
            "choices": {
                "A": "You're right. Cold weather proves the climate is not warming.",
                "B": "Last week's cold is weather (short-term, local). Climate change is about long-term global temperature trends over decades.",
                "C": "Climate change only happens in summer, so winter cold is expected.",
                "D": "Cold weather means climate change has reversed itself."
            },
            "correct": "B",
            "feedback_correct": "Correct! A single cold week is weather, not climate. Climate change refers to long-term shifts in global average temperatures measured over decades. Short-term local variation does not contradict the long-term trend.",
            "feedback_incorrect": "Not quite. Weather (daily or weekly conditions) is different from climate (long-term patterns over decades). A cold week in one location does not disprove the decades-long trend of rising global average temperatures."
        },
        {
            "question": "Which best explains why the ice-albedo effect is called a 'positive feedback loop'?",
            "choices": {
                "A": "It has a positive impact on the environment by cooling Earth down",
                "B": "Melting ice exposes dark surfaces that absorb more heat, causing more melting, which amplifies the original warming",
                "C": "Adding more ice to the poles increases Earth's reflectivity and lowers temperature",
                "D": "It only occurs in positively charged regions of the atmosphere"
            },
            "correct": "B",
            "feedback_correct": "Correct! In a positive feedback loop, the output amplifies the input. Warming melts ice, exposing dark ocean, which absorbs more heat, causing more warming and more melting. The cycle reinforces itself.",
            "feedback_incorrect": "Not quite. 'Positive feedback' in science means the output amplifies the original change. Warming melts ice, revealing dark surfaces that absorb more heat, causing more warming and more melting. The cycle accelerates itself."
        },
        {
            "question": "Based on the climate model, what is the key difference between the 'current trajectory' and the 'emission reduction' scenarios?",
            "choices": {
                "A": "Emission reduction immediately reverses warming and restores all ice sheets",
                "B": "Both scenarios show the same outcome because CO2 has no effect on temperature",
                "C": "Emission reduction slows the rate of warming and ice loss significantly, though it does not immediately reverse the trend",
                "D": "Current trajectory cools the planet because more CO2 means more plants absorbing heat"
            },
            "correct": "C",
            "feedback_correct": "Correct! Reducing emissions does not instantly reverse warming, but it significantly slows the rate of temperature increase and ice loss, giving ecosystems more time to adapt.",
            "feedback_incorrect": "Not quite. The model shows that reducing emissions slows warming and ice loss significantly compared to the current trajectory, even though it does not instantly reverse the effects already underway."
        }
    ]
}

# ── G07-L04: The Invisible Force That Charges Your Phone ─────────
L04_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is a magnet?",
            "choices": {
                "A": "Any metal object that is painted silver",
                "B": "An object that produces an invisible field that can attract or repel certain materials",
                "C": "A rock that only works when connected to electricity",
                "D": "A special type of battery that stores electrical energy"
            },
            "correct": "B",
            "feedback_correct": "Correct! A magnet produces a magnetic field, an invisible area of force that can attract magnetic materials like iron and repel other magnets.",
            "feedback_incorrect": "Not quite. A magnet is an object that produces an invisible magnetic field capable of attracting magnetic materials (like iron) or repelling other magnets."
        },
        {
            "question": "Can you make a magnet stronger or weaker?",
            "choices": {
                "A": "No. All magnets have a fixed strength that never changes.",
                "B": "Yes, but only by painting the magnet a different color",
                "C": "Yes. Factors like material, size, and electrical current can affect magnet strength.",
                "D": "Magnets only get weaker over time and can never be made stronger"
            },
            "correct": "C",
            "feedback_correct": "Correct! Magnet strength can be changed by the material used, the design of the magnet, and in the case of electromagnets, by adjusting the electric current.",
            "feedback_incorrect": "Not quite. The strength of a magnet depends on factors like its material and design. Electromagnets can be made stronger or weaker by changing the electric current flowing through them."
        },
        {
            "question": "What do you think connects electricity and magnetism?",
            "choices": {
                "A": "They are completely separate forces with nothing in common",
                "B": "Moving electric charges create magnetic fields, linking the two forces",
                "C": "Magnetism is a type of static electricity stored in metal",
                "D": "Electricity and magnetism only interact inside batteries"
            },
            "correct": "B",
            "feedback_correct": "Correct! Electricity and magnetism are connected. Moving electric charges (current) create magnetic fields, and moving magnets can generate electric current.",
            "feedback_incorrect": "Not quite. Electricity and magnetism are aspects of the same fundamental force. Moving electric charges create magnetic fields, and moving magnets can generate electric current."
        },
        {
            "question": "How can a magnet attract a paper clip without touching it?",
            "choices": {
                "A": "The magnet shoots invisible particles at the paper clip",
                "B": "The magnet creates a field of force that extends through the air to the paper clip",
                "C": "Air molecules carry the magnetic force from the magnet to the paper clip",
                "D": "The paper clip moves on its own when it senses the magnet nearby"
            },
            "correct": "B",
            "feedback_correct": "Correct! Magnets produce a magnetic field that extends through space. This field exerts a force on magnetic materials like the iron in a paper clip, even without physical contact.",
            "feedback_incorrect": "Not quite. A magnet creates an invisible magnetic field that extends through the space around it. This field exerts force on magnetic materials at a distance, without needing contact."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student builds an electromagnet by wrapping 50 turns of wire around an iron nail and connecting it to a battery. It picks up 8 paper clips. Which change would most likely INCREASE the number of paper clips it lifts?",
            "choices": {
                "A": "Replacing the iron nail with a wooden dowel",
                "B": "Wrapping 100 turns of wire instead of 50",
                "C": "Using a longer nail with the same number of wraps",
                "D": "Moving the electromagnet farther from the paper clips before turning it on"
            },
            "correct": "B",
            "feedback_correct": "Correct! Doubling the number of coil wraps concentrates and amplifies the magnetic field, significantly increasing the electromagnet's lifting capacity.",
            "feedback_incorrect": "Not quite. Increasing the number of coil wraps is one of the most effective ways to strengthen an electromagnet because each additional loop adds its magnetic field to the total."
        },
        {
            "question": "In the electromagnet model, setting both electric current AND number of coil wraps to maximum produces a much stronger result than changing just one variable. What does this demonstrate?",
            "choices": {
                "A": "Only one variable matters, and the other has no real effect",
                "B": "The two variables have a combined (multiplicative) effect on magnetic field strength",
                "C": "Magnetic field strength has a maximum limit that cannot be exceeded",
                "D": "Electric current cancels out the effect of additional coils"
            },
            "correct": "B",
            "feedback_correct": "Correct! Current and coils work together. More current through more coils produces a much stronger field than either change alone, demonstrating a combined effect on electromagnetic force.",
            "feedback_incorrect": "Not quite. The model shows that current and coils have a combined effect on field strength. Increasing both variables together produces a result greater than changing either one alone."
        },
        {
            "question": "Why are electromagnets more useful than permanent magnets for many real-world applications?",
            "choices": {
                "A": "Electromagnets are cheaper to produce than permanent magnets",
                "B": "Electromagnets can be turned on and off with a switch, and their strength can be adjusted",
                "C": "Permanent magnets are too heavy to use in machines",
                "D": "Electromagnets work in space, but permanent magnets do not"
            },
            "correct": "B",
            "feedback_correct": "Correct! The ability to control electromagnets by switching them on/off and adjusting their strength makes them far more versatile than permanent magnets for applications like cranes, motors, and MRI machines.",
            "feedback_incorrect": "Not quite. The key advantage of electromagnets is controllability. They can be turned on and off and their strength can be adjusted, making them essential for applications like junkyard cranes, electric motors, and MRI machines."
        },
        {
            "question": "Which statement best explains how your model proves that invisible forces are real?",
            "choices": {
                "A": "The model shows that increasing current and coils increases lifting capacity, even though the magnetic field cannot be seen",
                "B": "The model proves that forces only exist when objects are touching each other",
                "C": "The model shows that magnetic force and gravitational force are the same thing",
                "D": "The model demonstrates that invisible forces only work at very short distances"
            },
            "correct": "A",
            "feedback_correct": "Correct! The model demonstrates that changes in current and coils produce measurable changes in lifting capacity. The force acts at a distance through an invisible field, providing evidence that non-contact forces are real.",
            "feedback_incorrect": "Not quite. The model provides evidence that invisible forces exist because changing the inputs (current, coils) produces measurable outputs (lifting capacity) without physical contact between the electromagnet and the objects it lifts."
        }
    ]
}

# ── G07-L05: Every Drop You Drink Is Recycled Dinosaur Water ─────
L05_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What happens to water in a puddle on a hot, sunny day?",
            "choices": {
                "A": "The water seeps into the center of the Earth and disappears",
                "B": "The water absorbs heat and evaporates into water vapor in the air",
                "C": "The Sun's rays destroy the water molecules permanently",
                "D": "The water is absorbed by the wind and carried away as liquid"
            },
            "correct": "B",
            "feedback_correct": "Correct! Solar energy heats the water, giving the molecules enough energy to escape from the liquid surface and enter the air as invisible water vapor. This process is called evaporation.",
            "feedback_incorrect": "Not quite. When the Sun heats a puddle, the water molecules gain enough energy to change from liquid to gas (water vapor) and rise into the atmosphere. This is evaporation."
        },
        {
            "question": "Where does the water that comes out of your tap originally come from?",
            "choices": {
                "A": "It is manufactured in a water factory from hydrogen and oxygen",
                "B": "It cycles through natural systems like rivers, lakes, groundwater, and the atmosphere",
                "C": "It comes directly from the ocean with salt removed at the tap",
                "D": "New water is constantly created by rain clouds"
            },
            "correct": "B",
            "feedback_correct": "Correct! Tap water comes from natural sources like rivers, lakes, and underground aquifers that are continuously replenished by the water cycle.",
            "feedback_incorrect": "Not quite. Your tap water originates from natural water sources (rivers, lakes, groundwater) that are part of the continuous water cycle driven by solar energy and gravity."
        },
        {
            "question": "Could the water you drink today have once been consumed by a dinosaur?",
            "choices": {
                "A": "No, because water molecules break down and new ones are created every few years",
                "B": "No, because dinosaurs lived too long ago for the water to still exist",
                "C": "Yes, because Earth has been recycling the same water for billions of years",
                "D": "Yes, but only if you live near where dinosaurs once lived"
            },
            "correct": "C",
            "feedback_correct": "Correct! Earth has had roughly the same water for over 4 billion years. Water is recycled endlessly through evaporation, condensation, and precipitation, so the same molecules have been used by countless organisms.",
            "feedback_incorrect": "Not quite. Earth's water has been cycling through the same systems for over 4 billion years. No new water is being created. The molecules in your glass have been through countless cycles, including through ancient organisms."
        },
        {
            "question": "What provides the energy that drives the water cycle?",
            "choices": {
                "A": "Wind turbines and hydroelectric dams",
                "B": "Heat from Earth's core",
                "C": "Energy from the Sun",
                "D": "The Moon's gravitational pull"
            },
            "correct": "C",
            "feedback_correct": "Correct! Solar energy is the primary driver of the water cycle. It provides the heat needed to evaporate water from oceans, lakes, and land surfaces.",
            "feedback_incorrect": "Not quite. The Sun provides the energy that drives the water cycle by heating surface water and causing evaporation, which starts the cycle of evaporation, condensation, and precipitation."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the water cycle model, solar energy and ground temperature are both set to maximum (simulating a heat wave). What does the model predict?",
            "choices": {
                "A": "Evaporation rate decreases because the air is too hot to hold water",
                "B": "Evaporation rate increases dramatically, leading to increased precipitation",
                "C": "The water cycle stops because all the water evaporates permanently",
                "D": "Precipitation rate drops because heat destroys cloud formation"
            },
            "correct": "B",
            "feedback_correct": "Correct! More solar energy and higher temperatures provide more energy for evaporation, putting more water vapor into the atmosphere, which eventually condenses and falls as increased precipitation. The cycle accelerates.",
            "feedback_incorrect": "Not quite. Higher temperatures increase evaporation rate, which puts more water vapor into the atmosphere. This leads to more condensation and increased precipitation. The entire water cycle speeds up."
        },
        {
            "question": "A student says, 'Clouds are made of water vapor.' How should this misconception be corrected?",
            "choices": {
                "A": "Clouds are made of tiny liquid water droplets or ice crystals, not invisible water vapor",
                "B": "Clouds are made of dust particles that reflect sunlight to look white",
                "C": "The student is correct. Clouds are entirely composed of water vapor gas.",
                "D": "Clouds are made of frozen oxygen that forms at high altitudes"
            },
            "correct": "A",
            "feedback_correct": "Correct! Water vapor is an invisible gas. Clouds form when water vapor condenses into tiny visible liquid droplets or ice crystals. If you can see it, the water has already changed from vapor to liquid or solid.",
            "feedback_incorrect": "Not quite. Clouds are made of tiny liquid water droplets or ice crystals, not water vapor. Water vapor is invisible. When we see a cloud, the vapor has already condensed into visible droplets."
        },
        {
            "question": "Which two forces work together to drive the water cycle?",
            "choices": {
                "A": "Magnetism and friction",
                "B": "Solar energy and gravity",
                "C": "Wind and volcanic activity",
                "D": "The Moon's gravity and Earth's rotation"
            },
            "correct": "B",
            "feedback_correct": "Correct! Solar energy drives evaporation (lifting water into the atmosphere), and gravity drives precipitation (pulling water back to Earth) and runoff (moving water downhill to the ocean).",
            "feedback_incorrect": "Not quite. The water cycle is driven by solar energy (which provides heat for evaporation) and gravity (which pulls water back as precipitation and drives surface runoff toward the ocean)."
        },
        {
            "question": "How does deforestation affect the water cycle in a region?",
            "choices": {
                "A": "It has no effect because trees do not participate in the water cycle",
                "B": "It increases local rainfall because more sunlight reaches the ground",
                "C": "It reduces local rainfall because trees release water vapor through transpiration, and removing them reduces atmospheric moisture",
                "D": "It stops the water cycle entirely in the deforested area"
            },
            "correct": "C",
            "feedback_correct": "Correct! Trees release significant amounts of water vapor through transpiration. Removing forests reduces this moisture source, which can decrease local rainfall and increase surface runoff and erosion.",
            "feedback_incorrect": "Not quite. Trees contribute water vapor to the atmosphere through transpiration. A single large tree can release over 100 gallons of water per day. Removing forests reduces this moisture, potentially decreasing local rainfall."
        }
    ]
}

# ── G07-L06: Why Hot Cheetos Make You Cry ────────────────────────
L06_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "How does your body detect when something is hot?",
            "choices": {
                "A": "Your skin changes color to signal danger to your brain",
                "B": "Specialized nerve endings called receptors detect the heat and send signals to your brain",
                "C": "Your blood heats up and your brain feels the temperature change directly",
                "D": "Hot objects emit a sound frequency that your ears detect"
            },
            "correct": "B",
            "feedback_correct": "Correct! Your body has specialized sensory receptors (thermoreceptors) in your skin that detect temperature changes and send electrical signals through nerves to your brain.",
            "feedback_incorrect": "Not quite. Your body detects heat through specialized sensory receptors in your skin. These receptors convert the temperature stimulus into electrical nerve signals that travel to your brain."
        },
        {
            "question": "Why do you think eating spicy food makes some people cry and sweat?",
            "choices": {
                "A": "Spicy food contains acid that burns holes in your tongue",
                "B": "The chemicals in spicy food may activate pain or heat receptors in your mouth",
                "C": "Crying is an allergic reaction that only some people have to spices",
                "D": "Spicy food makes you sad, which causes tears"
            },
            "correct": "B",
            "feedback_correct": "Correct! Capsaicin in spicy food activates the same receptors that detect actual heat, triggering a pain response that includes tears, sweating, and a runny nose.",
            "feedback_incorrect": "Not quite. Capsaicin, the chemical that makes food spicy, binds to heat/pain receptors in your mouth, tricking your brain into responding as if your mouth is on fire."
        },
        {
            "question": "What happens inside your body between the moment you touch a hot pan and the moment you pull your hand away?",
            "choices": {
                "A": "Nothing happens inside your body. Your hand moves on its own.",
                "B": "Your hand sends a signal to your brain, which sends a signal back to your muscles",
                "C": "The heat melts the nerves in your hand, causing it to jerk away",
                "D": "Your eyes see the hot pan and tell your hand to move"
            },
            "correct": "B",
            "feedback_correct": "Correct! Sensory receptors detect the heat and send an electrical signal through nerves. Your nervous system processes this signal and sends a response back to your muscles to pull away.",
            "feedback_incorrect": "Not quite. When you touch something hot, receptors send an electrical signal through your nerves. Your nervous system processes the signal and sends a motor signal back to your muscles to pull your hand away."
        },
        {
            "question": "Can your senses ever be tricked into perceiving something that is not real?",
            "choices": {
                "A": "No. Our senses always give us a perfectly accurate picture of reality.",
                "B": "Yes. Optical illusions, phantom vibrations, and certain chemicals can fool our sensory receptors.",
                "C": "Only sight can be tricked. All other senses are always accurate.",
                "D": "Senses can only be tricked if a person is asleep"
            },
            "correct": "B",
            "feedback_correct": "Correct! Our senses can be fooled. Optical illusions trick our vision, capsaicin tricks heat receptors, and menthol tricks cold receptors. The brain responds to the signal it receives, even if the stimulus is not what it seems.",
            "feedback_incorrect": "Not quite. All of our senses can be tricked. Optical illusions fool vision, capsaicin makes us feel burning heat that is not real, and menthol creates a sensation of cold without an actual temperature change."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "Capsaicin from a Hot Cheeto binds to TRPV1 receptors in your mouth. What happens next in the nervous system pathway?",
            "choices": {
                "A": "The capsaicin travels through your blood to your brain, where it is tasted",
                "B": "TRPV1 receptors send electrical signals through neurons to the brain, which responds with tears, sweating, and pain",
                "C": "The capsaicin destroys mouth tissue, causing your body to produce tears to heal the damage",
                "D": "TRPV1 receptors release capsaicin back into the mouth, amplifying the spicy flavor"
            },
            "correct": "B",
            "feedback_correct": "Correct! Capsaicin activates TRPV1 heat/pain receptors, which generate electrical signals that travel through neurons to the brain. The brain interprets this as burning and triggers protective responses: tears, sweating, and mucus production.",
            "feedback_incorrect": "Not quite. When capsaicin binds to TRPV1 receptors, those receptors fire electrical signals through neurons to the brain. The brain cannot distinguish this signal from real burning, so it triggers pain responses including tears, sweating, and a runny nose."
        },
        {
            "question": "After being in a room with a strong smell for 10 minutes, you stop noticing the odor. What does the nervous system model predict is happening?",
            "choices": {
                "A": "The smell has actually gone away because the chemicals dispersed",
                "B": "Your sensory receptors have adapted and reduced their firing rate in response to the constant stimulus",
                "C": "Your brain has permanently lost the ability to detect that particular smell",
                "D": "Your nose has become physically blocked by the smell particles"
            },
            "correct": "B",
            "feedback_correct": "Correct! This is sensory adaptation. When exposed to a constant stimulus, receptors gradually decrease their firing rate. The smell is still there, but your nervous system reduces its response because the stimulus has not changed.",
            "feedback_incorrect": "Not quite. This phenomenon is called sensory adaptation. Your receptors reduce their firing rate when exposed to a constant, unchanging stimulus. The smell has not disappeared; your nervous system has simply decreased its response to it."
        },
        {
            "question": "Your hand pulls away from a hot stove BEFORE you consciously feel pain. How does the model explain this?",
            "choices": {
                "A": "Your hand has its own brain that makes decisions independently",
                "B": "The reflex signal goes from receptors to the spinal cord, which sends a motor response back without waiting for the brain",
                "C": "Your hand moves due to the heat expanding the muscles, not due to nerve signals",
                "D": "You saw the stove was hot before touching it, so your hand pulled away from memory"
            },
            "correct": "B",
            "feedback_correct": "Correct! Reflexes bypass the brain for speed. The pain signal goes from sensory receptors to the spinal cord, which immediately sends a motor signal to your arm muscles. Your brain receives the pain signal after your hand has already moved.",
            "feedback_incorrect": "Not quite. Reflex arcs bypass the brain entirely. The signal travels from receptors to the spinal cord, which sends an immediate motor response to your muscles. This takes about 0.05 seconds. Conscious awareness of pain comes later when the signal reaches the brain."
        },
        {
            "question": "Which statement best explains why capsaicin causes a real pain response even though it does not damage any tissue?",
            "choices": {
                "A": "Capsaicin is actually toxic and does cause microscopic tissue damage that we cannot see",
                "B": "The brain responds to the nerve signal it receives, not the actual stimulus, and TRPV1 receptors send the same signal for capsaicin as for real heat",
                "C": "Pain is entirely psychological and has nothing to do with physical receptors",
                "D": "Capsaicin only triggers a mild response that people exaggerate for attention"
            },
            "correct": "B",
            "feedback_correct": "Correct! The brain cannot tell the difference between a signal caused by capsaicin and one caused by actual heat above 43 degrees C. Both activate the same TRPV1 receptor, generating identical nerve signals. The response is genuine even though no damage occurs.",
            "feedback_incorrect": "Not quite. Capsaicin activates the exact same TRPV1 receptor that detects temperatures above 43 degrees C. The receptor sends an identical signal regardless of the cause. The brain responds to the signal, not the source, which is why the pain response is real."
        }
    ]
}

# ── G07-L07: Why You Can't Slide Forever ─────────────────────────
L07_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Why does a ball eventually stop rolling across the floor?",
            "choices": {
                "A": "The ball runs out of energy, and the energy ceases to exist",
                "B": "Friction between the ball and the floor gradually slows the ball down",
                "C": "Gravity pulls the ball downward and stops its forward motion",
                "D": "The air in front of the ball pushes it backward until it stops"
            },
            "correct": "B",
            "feedback_correct": "Correct! Friction is the force between the ball and the floor surface that opposes the ball's motion, gradually converting its kinetic energy into other forms until it stops.",
            "feedback_incorrect": "Not quite. A rolling ball stops because friction between the ball and the floor surface opposes its motion. Friction gradually converts the ball's kinetic energy into thermal energy."
        },
        {
            "question": "When a moving object stops, where does its energy go?",
            "choices": {
                "A": "The energy is destroyed and disappears completely",
                "B": "The energy is converted into other forms, such as heat and sound",
                "C": "The energy stays inside the object but becomes invisible",
                "D": "The energy returns to the person or force that originally pushed the object"
            },
            "correct": "B",
            "feedback_correct": "Correct! Energy cannot be created or destroyed (conservation of energy). When an object stops, its kinetic energy is converted into thermal energy (heat) and sound energy.",
            "feedback_incorrect": "Not quite. According to the law of conservation of energy, energy is never destroyed. When a moving object stops, its kinetic energy is transformed into thermal energy (heat in the surfaces) and sometimes sound."
        },
        {
            "question": "Why do your hands get warm when you rub them together?",
            "choices": {
                "A": "Your blood moves faster when your hands rub, heating them up",
                "B": "Friction between your hands converts kinetic energy (motion) into thermal energy (heat)",
                "C": "Static electricity generated by rubbing heats the skin",
                "D": "Your body temperature increases when you exercise your hand muscles"
            },
            "correct": "B",
            "feedback_correct": "Correct! Rubbing your hands together creates friction, which converts the kinetic energy of your hands' motion into thermal energy (heat) that you feel as warmth.",
            "feedback_incorrect": "Not quite. The warmth you feel is thermal energy created by friction. The kinetic energy of your moving hands is converted into heat through the friction between your skin surfaces."
        },
        {
            "question": "Would an object in deep outer space ever stop moving if nothing was in its way?",
            "choices": {
                "A": "Yes, because all objects naturally slow down and stop eventually",
                "B": "Yes, because gravity from distant stars would slow it to a stop",
                "C": "No, because without friction or resistance, there is nothing to slow it down",
                "D": "No, because objects in space move faster and faster over time"
            },
            "correct": "C",
            "feedback_correct": "Correct! In the vacuum of space, there is virtually no friction. Without a force to oppose motion, an object will continue moving at the same speed indefinitely. This is Newton's First Law.",
            "feedback_incorrect": "Not quite. In space, there is essentially no friction or air resistance. Without a force acting against its motion, an object continues moving at the same speed forever. This is why space probes travel for decades without engines."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the energy model, a toy car starts at the same speed on three different surfaces: ice, concrete, and carpet. On which surface does kinetic energy last the longest, and why?",
            "choices": {
                "A": "Carpet, because rough surfaces generate more kinetic energy",
                "B": "Concrete, because it is the hardest and most durable surface",
                "C": "Ice, because its low friction converts kinetic energy to thermal energy very slowly",
                "D": "All three surfaces produce the same result because initial speed is the same"
            },
            "correct": "C",
            "feedback_correct": "Correct! Ice has very low friction, so it converts kinetic energy to thermal energy at a much slower rate. The car slides farther and retains its kinetic energy longer on ice than on higher-friction surfaces.",
            "feedback_incorrect": "Not quite. Ice has the lowest friction of the three surfaces, meaning it converts kinetic energy to thermal energy the slowest. The car retains its kinetic energy longest on ice and slides the farthest."
        },
        {
            "question": "A student claims: 'When a ball stops rolling, the energy has been used up and no longer exists.' Using the model, what is wrong with this claim?",
            "choices": {
                "A": "Nothing is wrong. The student correctly described how energy works.",
                "B": "Energy is never destroyed. The kinetic energy was transformed into thermal energy through friction.",
                "C": "The energy was not used up; it was stored inside the ball for later use.",
                "D": "The energy was sent back to the person who originally pushed the ball."
            },
            "correct": "B",
            "feedback_correct": "Correct! The law of conservation of energy states that energy cannot be created or destroyed. The ball's kinetic energy was converted into thermal energy (heat) in the surfaces. If you could measure all the heat produced, it would equal the kinetic energy lost.",
            "feedback_incorrect": "Not quite. Energy is never used up or destroyed. When the ball stops, every joule of kinetic energy has been converted into thermal energy through friction. The energy still exists, just in a different form."
        },
        {
            "question": "The model shows that doubling the initial speed of an object quadruples its kinetic energy (KE = 1/2 mv squared). What practical implication does this have?",
            "choices": {
                "A": "Faster objects are lighter because kinetic energy replaces mass",
                "B": "Stopping distance increases dramatically at higher speeds because there is much more energy to convert to heat",
                "C": "Speed has no effect on how long it takes an object to stop",
                "D": "Doubling the speed doubles the stopping distance in a perfectly linear relationship"
            },
            "correct": "B",
            "feedback_correct": "Correct! Because kinetic energy increases with the square of speed, doubling speed means four times as much energy must be converted to heat through friction. This is why stopping distances increase dramatically at higher speeds.",
            "feedback_incorrect": "Not quite. Since KE = 1/2 mv squared, doubling speed quadruples kinetic energy. Four times as much energy must be converted through friction to stop, which means stopping distances increase dramatically. This is why speed limits save lives."
        },
        {
            "question": "An engineer is designing brakes for an electric car. Based on the energy model, what is the most energy-efficient braking system?",
            "choices": {
                "A": "Brakes that convert all kinetic energy into sound energy",
                "B": "Brakes that destroy the kinetic energy so it no longer exists",
                "C": "Regenerative brakes that convert kinetic energy back into electrical energy to recharge the battery",
                "D": "Brakes that increase friction to maximum to stop the car instantly"
            },
            "correct": "C",
            "feedback_correct": "Correct! Regenerative braking captures kinetic energy and converts it back into electrical energy to recharge the battery, rather than wasting it all as heat. This makes electric cars more energy efficient than traditional friction brakes.",
            "feedback_incorrect": "Not quite. Regenerative braking converts kinetic energy back into useful electrical energy instead of wasting it as heat. This allows electric cars to recapture energy during braking and extend their range."
        }
    ]
}

# ── G07-L08: The Crime Scene in Every Rock ───────────────────────
L08_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What can you learn by looking at layers of rock in a cliff or canyon?",
            "choices": {
                "A": "Nothing useful. Rocks are just rocks.",
                "B": "Each layer represents a different time period and can reveal what the environment was like when it formed",
                "C": "Rock layers only form during earthquakes, so they tell us about seismic history",
                "D": "The color of rock layers tells us what temperature it was when they formed"
            },
            "correct": "B",
            "feedback_correct": "Correct! Rock layers (strata) form over time as sediment accumulates. Each layer is like a page in Earth's history, recording the environmental conditions when it was deposited.",
            "feedback_incorrect": "Not quite. Rock layers are records of the past. Each layer formed at a different time and contains evidence about the environment, climate, and organisms that existed during that period."
        },
        {
            "question": "Why are fossils found inside certain types of rocks?",
            "choices": {
                "A": "Fossils can form in any type of rock equally well",
                "B": "Fossils form best in sedimentary rocks because organisms get buried in layers of sediment before they decompose",
                "C": "Fossils only form inside volcanic rocks that melt and preserve organisms",
                "D": "Animals deliberately crawl inside rocks before they die"
            },
            "correct": "B",
            "feedback_correct": "Correct! Sedimentary rocks form from accumulated layers of sediment. When organisms are buried in this sediment quickly enough, they can be preserved as fossils before decomposition.",
            "feedback_incorrect": "Not quite. Fossils are most commonly found in sedimentary rocks because the process of sedimentation can bury organisms before they decompose, preserving them over millions of years."
        },
        {
            "question": "If you found a fish fossil in a rock on top of a mountain, what would that tell you?",
            "choices": {
                "A": "Fish once flew through the air and landed on the mountain",
                "B": "Someone carried the fossil up the mountain and left it there",
                "C": "The rock formed underwater and was later uplifted to become a mountain",
                "D": "The fossil is fake because fish cannot live on mountains"
            },
            "correct": "C",
            "feedback_correct": "Correct! Marine fossils on mountains are evidence that the rock formed on an ancient ocean floor. Tectonic forces later uplifted those ocean-floor rocks thousands of feet into the air.",
            "feedback_incorrect": "Not quite. Finding marine fossils on mountaintops is powerful evidence that those rocks formed at the bottom of an ancient ocean and were later pushed upward by tectonic forces over millions of years."
        },
        {
            "question": "In a stack of undisturbed rock layers, which layer is the oldest?",
            "choices": {
                "A": "The layer at the very top",
                "B": "The thickest layer, regardless of position",
                "C": "The layer at the very bottom",
                "D": "The darkest-colored layer"
            },
            "correct": "C",
            "feedback_correct": "Correct! This is the principle of superposition. In undisturbed rock layers, each new layer is deposited on top of older layers, so the bottom layer is the oldest.",
            "feedback_incorrect": "Not quite. The principle of superposition states that in undisturbed rock sequences, the oldest layers are at the bottom and the youngest are at the top, because each new layer is deposited on top of existing ones."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the rock strata model, sedimentation rate is set to maximum (simulating a flood event). What does the model predict about fossil preservation quality?",
            "choices": {
                "A": "Fossil preservation quality decreases because floods destroy all organisms",
                "B": "Fossil preservation quality is excellent because organisms are buried quickly before they decompose",
                "C": "Fossil preservation quality is unaffected because preservation depends only on the type of organism",
                "D": "No fossils form during floods because water prevents sedimentation"
            },
            "correct": "B",
            "feedback_correct": "Correct! Rapid burial during events like floods protects organisms from decomposition and scavengers, leading to excellent fossil preservation. Many of the world's best fossil sites formed during rapid deposition events.",
            "feedback_incorrect": "Not quite. Rapid sedimentation (like during a flood or volcanic ash fall) buries organisms quickly, protecting them from decomposition and scavengers. This is why rapid burial produces the best-preserved fossils."
        },
        {
            "question": "A geologist finds a rock sequence where a layer containing marine fossils sits between two layers containing land plant fossils. What is the best interpretation?",
            "choices": {
                "A": "The marine fossils were placed there by ancient people",
                "B": "The area was once land, then flooded by ocean (depositing marine sediment), then became land again",
                "C": "The marine and plant fossils formed at the same time but in different parts of the rock",
                "D": "The rock layers have been flipped upside down by an earthquake"
            },
            "correct": "B",
            "feedback_correct": "Correct! The sequence tells a story: the area was initially land (plant fossils), then sea levels rose and the area was covered by ocean (marine fossils), then sea levels dropped and it became land again (more plant fossils).",
            "feedback_incorrect": "Not quite. Using the principle of superposition, we read bottom to top: first land (plant fossils), then ocean covered the area (marine fossils), then the sea retreated and land returned (more plant fossils). The rock records changing environments over time."
        },
        {
            "question": "What does an unconformity in the rock record represent?",
            "choices": {
                "A": "A layer of unusual or rare minerals",
                "B": "A gap where rock layers are missing, representing lost time due to erosion or non-deposition",
                "C": "A layer that contains no fossils at all",
                "D": "A boundary between igneous and metamorphic rock"
            },
            "correct": "B",
            "feedback_correct": "Correct! An unconformity is a gap in the geological record where erosion removed existing layers or deposition did not occur. These gaps can represent millions of years of missing history.",
            "feedback_incorrect": "Not quite. An unconformity is a gap in the rock record where layers are missing. This can happen when erosion wears away existing layers or when new sediment is not deposited. These gaps represent potentially millions of years of lost geological history."
        },
        {
            "question": "In the model, when erosion rate exceeds sedimentation rate for a long period, what happens to the rock record at that location?",
            "choices": {
                "A": "Rock layers continue building normally because erosion has no effect on existing layers",
                "B": "Rock layer thickness decreases as existing layers are worn away, and fossil evidence is destroyed",
                "C": "Erosion creates new types of fossils by exposing them to the air",
                "D": "The rock layers become stronger and more resistant to future erosion"
            },
            "correct": "B",
            "feedback_correct": "Correct! When erosion dominates, it wears away existing rock layers, reducing their thickness and destroying the fossils within them. This is how erosion acts as a 'thief,' stealing pages from Earth's history book.",
            "feedback_incorrect": "Not quite. When erosion rate exceeds sedimentation rate, existing rock layers are worn away. This reduces layer thickness and destroys fossils, creating gaps in the geological record at that location."
        }
    ]
}

# ── G07-L09: We Built a Better Dog (And Maybe a Mistake) ────────
L09_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "How do you think humans got so many different dog breeds from wolves?",
            "choices": {
                "A": "Different dog breeds are actually different species that are unrelated to wolves",
                "B": "Humans selected wolves with specific traits and bred them together over many generations",
                "C": "Dogs evolved naturally into different breeds without any human involvement",
                "D": "Scientists created dog breeds in laboratories using genetic engineering"
            },
            "correct": "B",
            "feedback_correct": "Correct! Over at least 15,000 years, humans selected wolves with desirable traits (friendliness, herding ability, size) and bred them together, gradually creating the hundreds of breeds we have today.",
            "feedback_incorrect": "Not quite. All domestic dog breeds descended from wolves through selective breeding. Humans chose wolves with desired traits and bred them together over thousands of years, gradually producing the wide variety of breeds that exist today."
        },
        {
            "question": "What does it mean to 'breed' plants or animals for specific traits?",
            "choices": {
                "A": "Choosing which organisms reproduce based on the traits they have, so offspring are more likely to have those traits",
                "B": "Feeding organisms special food to change their physical appearance",
                "C": "Painting or dyeing organisms to make them look different",
                "D": "Training organisms to behave differently so their offspring learn the same behaviors"
            },
            "correct": "A",
            "feedback_correct": "Correct! Selective breeding means choosing organisms with desired traits as parents, so those traits are more likely to be passed to the next generation through inheritance.",
            "feedback_incorrect": "Not quite. Breeding for specific traits means selecting organisms that already have the desired characteristics and allowing only those to reproduce. The traits are passed genetically to offspring."
        },
        {
            "question": "What could go wrong if we only breed for one specific trait over many generations?",
            "choices": {
                "A": "Nothing can go wrong because selective breeding always produces healthier organisms",
                "B": "The population could lose genetic variation, making it vulnerable to diseases and health problems",
                "C": "The organisms would eventually evolve back to their original wild form",
                "D": "Only the desired trait would change; everything else stays perfectly the same"
            },
            "correct": "B",
            "feedback_correct": "Correct! Extreme selection for one trait reduces genetic diversity in the population. With less variation, organisms become more vulnerable to diseases, environmental changes, and inherited health problems.",
            "feedback_incorrect": "Not quite. When breeders focus too narrowly on one trait, they reduce the genetic diversity of the population. This makes the entire population more vulnerable to disease, genetic disorders, and environmental changes."
        },
        {
            "question": "How is artificial selection different from natural selection?",
            "choices": {
                "A": "Artificial selection is faster and more powerful than natural selection in every way",
                "B": "In artificial selection, humans choose which traits are favored; in natural selection, the environment determines fitness",
                "C": "Natural selection only affects plants, while artificial selection only affects animals",
                "D": "There is no difference. They are two names for the same process."
            },
            "correct": "B",
            "feedback_correct": "Correct! Both use the same mechanism (variation, selection, inheritance), but in natural selection the environment determines which traits help survival, while in artificial selection humans choose which traits to favor.",
            "feedback_incorrect": "Not quite. The key difference is who does the selecting. In natural selection, environmental pressures determine which organisms survive and reproduce. In artificial selection, humans choose which organisms reproduce based on traits we desire."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the selective breeding model, selection pressure is set to maximum over many generations. The model shows desired trait frequency rising sharply. What also happens to genetic diversity?",
            "choices": {
                "A": "Genetic diversity increases because the population is improving",
                "B": "Genetic diversity stays the same because only the desired trait changes",
                "C": "Genetic diversity crashes because only organisms with the desired trait are allowed to reproduce",
                "D": "Genetic diversity is not tracked in the model"
            },
            "correct": "C",
            "feedback_correct": "Correct! The model reveals a critical trade-off: extreme selection increases the desired trait rapidly but dramatically reduces genetic diversity. By eliminating all individuals without the trait, the gene pool shrinks dangerously.",
            "feedback_incorrect": "Not quite. The model demonstrates that extreme selection pressure creates a trade-off. While the desired trait becomes very common, genetic diversity crashes because only a narrow subset of the population is allowed to reproduce."
        },
        {
            "question": "English Bulldogs were selectively bred for flat faces over many generations. Today, many Bulldogs have severe breathing problems. What does this demonstrate about selective breeding?",
            "choices": {
                "A": "Selective breeding always produces the healthiest possible organisms",
                "B": "Selective breeding can achieve desired traits but may cause unintended harmful consequences",
                "C": "Breathing problems in Bulldogs are unrelated to their breeding history",
                "D": "Only natural selection can produce healthy organisms"
            },
            "correct": "B",
            "feedback_correct": "Correct! The Bulldog example shows that selecting strongly for appearance traits can cause harmful side effects. The flat face that breeders wanted came at the cost of compressed airways that make breathing difficult.",
            "feedback_incorrect": "Not quite. Bulldogs demonstrate a key consequence of extreme selective breeding: the desired trait (flat face) was achieved, but it came with unintended harm (breathing difficulty). Breeding for appearance without considering health has real costs."
        },
        {
            "question": "Why might a population with high genetic diversity be healthier and more resilient than one with low genetic diversity?",
            "choices": {
                "A": "Genetic diversity makes organisms physically larger and stronger",
                "B": "With more genetic variation, the population is more likely to have individuals that can survive new diseases or environmental changes",
                "C": "Genetic diversity causes organisms to reproduce faster",
                "D": "High genetic diversity means all organisms are identical, which is ideal for survival"
            },
            "correct": "B",
            "feedback_correct": "Correct! Genetic diversity acts like an insurance policy. With more variation, some individuals are likely to have traits that help them survive unexpected challenges like new diseases, pests, or climate changes.",
            "feedback_incorrect": "Not quite. Genetic diversity is crucial for resilience. A diverse population contains more genetic variation, so when new threats appear (diseases, environmental changes), some individuals are more likely to have traits that allow them to survive."
        },
        {
            "question": "The Irish Potato Famine of the 1840s killed over one million people when a single disease destroyed the potato crop. How does the selective breeding model help explain this disaster?",
            "choices": {
                "A": "The potatoes were not selectively bred, so they had no protection against disease",
                "B": "Irish farmers grew potatoes with extremely low genetic diversity, so one disease could wipe out the entire crop",
                "C": "The disease was too powerful for any potato variety to resist, regardless of diversity",
                "D": "The famine was caused by weather, not by genetics or breeding"
            },
            "correct": "B",
            "feedback_correct": "Correct! Irish farmers relied on a very small number of genetically similar potato varieties. When a blight arrived, it could destroy them all because none had genetic resistance. This is the real-world consequence of the diversity crash the model predicts.",
            "feedback_incorrect": "Not quite. The Potato Famine is a case study in what happens when genetic diversity is too low. Because nearly all the potatoes were genetically similar, one disease could destroy the entire crop. Greater genetic diversity would have meant some resistant varieties survived."
        }
    ]
}

# ── G07-L10: Your Phone Speaks in 1s and 0s ──────────────────────
L10_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is the main difference between an analog signal and a digital signal?",
            "choices": {
                "A": "Analog signals are newer technology; digital signals are older",
                "B": "Analog signals vary continuously and smoothly; digital signals use discrete values like 1s and 0s",
                "C": "Analog signals can only carry sound; digital signals can only carry images",
                "D": "There is no real difference. They are two words for the same thing."
            },
            "correct": "B",
            "feedback_correct": "Correct! Analog signals are continuous, like the smooth groove in a vinyl record. Digital signals encode information as discrete steps, typically binary values (1s and 0s) that represent measurements of the original signal.",
            "feedback_incorrect": "Not quite. Analog signals vary smoothly and continuously (like a sound wave), while digital signals break information into discrete numerical values (typically 1s and 0s) that can be exactly copied and transmitted."
        },
        {
            "question": "Why might a digital copy of a song sound different from a live performance?",
            "choices": {
                "A": "Digital recordings always sound better than live music",
                "B": "Converting a continuous sound wave into digital format involves measuring it at intervals, which may not capture every detail",
                "C": "Digital recordings add extra sounds that were not in the original performance",
                "D": "Live performances use analog sound, which is always lower quality than digital"
            },
            "correct": "B",
            "feedback_correct": "Correct! When sound is digitized, it is sampled at regular intervals. Some details between samples may be lost. The quality depends on how frequently and precisely the sound is measured.",
            "feedback_incorrect": "Not quite. When analog sound is converted to digital, it is measured at specific intervals (sampling). Details that exist between those measurement points may not be captured, depending on the sampling rate and precision."
        },
        {
            "question": "What does 'compression' mean when talking about digital files like MP3s?",
            "choices": {
                "A": "Physically squishing the device to make files smaller",
                "B": "Reducing the file size by removing some data, which may reduce quality",
                "C": "Making the sound louder by pressing the audio waves closer together",
                "D": "Converting the file from digital back to analog format"
            },
            "correct": "B",
            "feedback_correct": "Correct! Compression reduces file size by removing data. Lossy compression (like MP3) permanently removes data that algorithms predict humans will not notice, trading some quality for much smaller files.",
            "feedback_incorrect": "Not quite. Digital compression reduces file size by removing some data. In lossy compression (like MP3), data deemed least noticeable to human ears is permanently removed, making the file smaller but slightly reducing quality."
        },
        {
            "question": "Why do some music files take up more storage space than others, even if the songs are the same length?",
            "choices": {
                "A": "Longer song titles create larger file sizes",
                "B": "Different formats use different amounts of data to encode the same audio, depending on quality settings",
                "C": "Louder songs take up more space than quieter songs",
                "D": "All songs of the same length have exactly the same file size"
            },
            "correct": "B",
            "feedback_correct": "Correct! Different audio formats and quality settings use different amounts of data. An uncompressed WAV file contains all the original data, while a compressed MP3 removes data to reduce file size. Higher quality settings mean larger files.",
            "feedback_incorrect": "Not quite. File size depends on the format and quality settings used. An uncompressed WAV file stores all audio data and is very large, while an MP3 uses compression to reduce size by removing data. Higher quality settings produce larger files."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the digital signal model, sampling rate is set to maximum and compression level to minimum. What does the model predict about signal accuracy and file size?",
            "choices": {
                "A": "Signal accuracy is low but file size is very small",
                "B": "Signal accuracy is very high but file size is very large",
                "C": "Both signal accuracy and file size are at minimum values",
                "D": "Signal accuracy and file size are unrelated to these settings"
            },
            "correct": "B",
            "feedback_correct": "Correct! Maximum sampling rate captures the most detail (highest accuracy) but produces the most data. Minimum compression keeps all that data intact, resulting in very large files. This is studio-quality audio.",
            "feedback_incorrect": "Not quite. High sampling rate with low compression produces the most accurate digital reproduction of the original signal, but at the cost of very large file sizes. This is the quality-vs-size trade-off engineers must balance."
        },
        {
            "question": "A student claims: 'Digital music is always better than analog vinyl.' Based on the model, which response is most scientifically accurate?",
            "choices": {
                "A": "The student is correct. Digital is superior in every measurable way.",
                "B": "Digital is more RELIABLE (perfect copies, no degradation), but the quality depends on sampling rate and compression settings, and heavily compressed digital audio may sound worse than vinyl",
                "C": "Vinyl is always better because it captures continuous sound without any loss",
                "D": "Neither is better because they produce identical sound"
            },
            "correct": "B",
            "feedback_correct": "Correct! Digital's advantage is reliability: perfect copies with no degradation. But digital quality depends on settings. High-quality digital can sound as good as or better than vinyl, while heavily compressed digital may lose detail that vinyl preserves.",
            "feedback_incorrect": "Not quite. Digital signals are more reliable because they can be copied perfectly without degradation. However, the quality of digital audio depends on sampling rate and compression. Highly compressed digital files may actually lose details that a well-maintained vinyl record preserves."
        },
        {
            "question": "When compression level is pushed to maximum in the model, what happens to the music?",
            "choices": {
                "A": "The music sounds identical because compression only affects file size, not quality",
                "B": "The music quality drops noticeably, with thin, metallic, or watery sound artifacts because too much data has been removed",
                "C": "The music gets louder because compression pushes the sound waves together",
                "D": "The music plays faster because there is less data to process"
            },
            "correct": "B",
            "feedback_correct": "Correct! Extreme compression removes so much audio data that quality drops noticeably. The music may sound thin, watery, or metallic because the compression algorithm removed too many details that human ears can detect.",
            "feedback_incorrect": "Not quite. At extreme compression levels, the algorithm removes enough data that humans can hear the difference. The music may sound thin, metallic, or lacking in detail because important audio information has been permanently deleted."
        },
        {
            "question": "Why are digital signals considered more reliable than analog signals for transmitting and storing information?",
            "choices": {
                "A": "Digital equipment is physically stronger and more durable than analog equipment",
                "B": "Digital signals encode information as exact numbers that can be copied perfectly, while analog signals degrade with each copy or playback",
                "C": "Analog signals can only travel short distances, while digital signals travel worldwide",
                "D": "Digital signals use more electricity, which makes them more powerful"
            },
            "correct": "B",
            "feedback_correct": "Correct! Digital signals are just numbers (binary), and numbers can be copied exactly. The millionth copy is identical to the first. Analog signals are physical patterns that degrade with each copy, like photocopying a photocopy. Digital also includes error correction to fix transmission mistakes.",
            "feedback_incorrect": "Not quite. The key advantage is that digital signals encode information as exact numbers (1s and 0s) that can be copied perfectly every time. Analog signals are physical patterns that degrade with each copy or playback. Digital systems also include error correction to detect and fix transmission errors."
        }
    ]
}

# ── Master Dictionary ────────────────────────────────────────────
ALL_QUESTIONS = {
    "G07-L01": L01_QUESTIONS,
    "G07-L02": L02_QUESTIONS,
    "G07-L03": L03_QUESTIONS,
    "G07-L04": L04_QUESTIONS,
    "G07-L05": L05_QUESTIONS,
    "G07-L06": L06_QUESTIONS,
    "G07-L07": L07_QUESTIONS,
    "G07-L08": L08_QUESTIONS,
    "G07-L09": L09_QUESTIONS,
    "G07-L10": L10_QUESTIONS,
}
