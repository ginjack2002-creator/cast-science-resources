#!/usr/bin/env python3
"""Multiple choice pre/post assessment questions for Grade 10 Level 1 ModelIt! Lessons"""

L01_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "When a metal salt such as strontium chloride is heated in a flame, it produces a characteristic red color. Which of the following best explains why different metals produce different flame colors?",
            "choices": {
                "A": "Each metal has a unique set of electron energy levels, so the photons emitted during electron transitions have different wavelengths.",
                "B": "Different metals burn at different temperatures, and hotter flames always produce bluer colors.",
                "C": "The oxygen in the air reacts differently with each metal, producing unique combustion byproducts that glow different colors.",
                "D": "Larger atoms produce longer wavelengths of light because their electrons are farther from the nucleus."
            },
            "correct": "A",
            "feedback_correct": "Correct. Each element has quantized electron energy levels with unique spacing, so electron transitions emit photons of characteristic wavelengths, producing element-specific colors.",
            "feedback_incorrect": "Incorrect. Flame color is determined by the specific energy gaps between electron levels in each element, not by combustion temperature, oxygen reactions, or atomic size alone."
        },
        {
            "question": "A student observes that heating copper chloride produces a blue-green flame while heating sodium chloride produces a yellow flame. Which statement best explains this observation?",
            "choices": {
                "A": "Copper burns at a higher temperature than sodium, producing a higher-energy color.",
                "B": "The electron energy gaps in copper atoms correspond to blue-green photon wavelengths, while sodium's gaps correspond to yellow wavelengths.",
                "C": "Chloride ions determine the flame color, and different amounts of chloride produce different colors.",
                "D": "Copper reflects blue-green light from the flame while sodium reflects yellow light."
            },
            "correct": "B",
            "feedback_correct": "Correct. The color is determined by the metal's unique electron energy level spacing. When excited electrons fall back to lower levels, they release photons with wavelengths specific to that element.",
            "feedback_incorrect": "Incorrect. The metal cation, not the anion, determines the flame color. The color arises from the specific energy transitions of electrons within each metal's atomic structure."
        },
        {
            "question": "Which of the following statements about electromagnetic radiation is accurate?",
            "choices": {
                "A": "Red light has a shorter wavelength and higher energy than blue light.",
                "B": "All colors of visible light carry the same amount of energy per photon.",
                "C": "Blue light has a shorter wavelength and higher energy per photon than red light.",
                "D": "The energy of a photon is independent of its wavelength."
            },
            "correct": "C",
            "feedback_correct": "Correct. Photon energy is inversely proportional to wavelength (E = hc/lambda). Blue light (~450 nm) has shorter wavelength and higher energy than red light (~650 nm).",
            "feedback_incorrect": "Incorrect. Photon energy and wavelength are inversely related. Shorter wavelengths (blue/violet) carry more energy per photon than longer wavelengths (red)."
        },
        {
            "question": "An atom absorbs energy and one of its electrons moves from a lower energy level to a higher one. What happens when the electron returns to its original energy level?",
            "choices": {
                "A": "The atom absorbs another photon of equal energy.",
                "B": "The electron emits a photon with energy equal to the difference between the two levels.",
                "C": "The electron releases heat energy but no light.",
                "D": "The atom splits into two smaller atoms, releasing nuclear energy."
            },
            "correct": "B",
            "feedback_correct": "Correct. When an excited electron drops to a lower energy level, the energy difference is emitted as a photon whose wavelength corresponds to that specific energy gap.",
            "feedback_incorrect": "Incorrect. Electron transitions to lower energy levels release energy as photons. The photon's energy exactly matches the energy difference between the two levels."
        },
        {
            "question": "A scientist wants to identify an unknown metal sample. She heats the sample and observes its emission spectrum. Why is this method reliable for element identification?",
            "choices": {
                "A": "Every element melts at a unique temperature, which determines the color of light it emits.",
                "B": "Each element has a unique set of electron energy levels, producing a characteristic pattern of spectral lines.",
                "C": "Heavier elements always produce more spectral lines than lighter elements.",
                "D": "The chemical bonds in each element vibrate at unique frequencies when heated."
            },
            "correct": "B",
            "feedback_correct": "Correct. Each element's electron configuration creates unique energy level spacings, producing a distinctive emission spectrum that acts as a chemical fingerprint.",
            "feedback_incorrect": "Incorrect. Emission spectra are unique because each element has a distinct set of quantized electron energy levels. This produces characteristic spectral line patterns regardless of the element's mass or melting point."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A firework shell contains both strontium chloride (red) and copper chloride (blue). When detonated, the firework produces a purple color. Which explanation best accounts for this observation using the computational model?",
            "choices": {
                "A": "The two metals chemically react to form a new compound that emits purple photons.",
                "B": "Both metals independently emit their characteristic photons, and the mixture of red and blue light is perceived as purple by the human eye.",
                "C": "The copper lowers the combustion temperature, shifting the strontium emission from red to purple.",
                "D": "The combined electron clouds of both metals create a new set of energy levels that correspond to purple light."
            },
            "correct": "B",
            "feedback_correct": "Correct. Each metal retains its unique emission spectrum. The strontium emits red photons and the copper emits blue photons independently. The combination is perceived as purple through additive color mixing.",
            "feedback_incorrect": "Incorrect. Each metal's emission is determined by its own atomic structure. When both emit simultaneously, the human eye perceives the combined wavelengths as purple through additive color mixing."
        },
        {
            "question": "In the computational model, increasing the Oxidizer Strength to its maximum value causes the firework color to wash out toward white. Which of the following best explains this result?",
            "choices": {
                "A": "Excessive oxidizer causes the metal salts to decompose before they can emit light.",
                "B": "At extremely high temperatures, blackbody radiation from the heated material overwhelms the characteristic emission lines of the metal.",
                "C": "The oxidizer itself emits white light that covers up the metal's color.",
                "D": "Maximum oxidizer causes all electrons to be stripped from the atoms, preventing any photon emission."
            },
            "correct": "B",
            "feedback_correct": "Correct. At very high combustion temperatures, the intense thermal (blackbody) radiation across all visible wavelengths overwhelms the discrete emission lines of the metal, producing white light.",
            "feedback_incorrect": "Incorrect. Extremely high temperatures produce intense blackbody radiation across all wavelengths. This continuous spectrum drowns out the discrete emission lines from the metal salt, washing the color toward white."
        },
        {
            "question": "A student claims that the color of a firework is determined by the type of gunpowder used, not the metal salt. Based on the model, which evidence best refutes this claim?",
            "choices": {
                "A": "Changing only the metal salt while keeping the same gunpowder produces different colors.",
                "B": "Gunpowder produces smoke that filters out certain colors of light.",
                "C": "Different gunpowder mixtures burn at different rates but all produce white light.",
                "D": "The model shows that gunpowder does not contain any electrons capable of emitting visible light."
            },
            "correct": "A",
            "feedback_correct": "Correct. The model demonstrates that changing only the Element Type component (metal salt) while holding gunpowder constant produces different colors. This proves the color originates from the metal's electron transitions, not the explosive.",
            "feedback_incorrect": "Incorrect. The key evidence is that the same gunpowder produces different colors when paired with different metal salts. This isolates the metal as the source of the color, since its unique electron energy gaps determine the emitted wavelengths."
        },
        {
            "question": "Astronomers use the same principles as firework chemistry to determine the composition of distant stars. Which model component most directly enables this astronomical application?",
            "choices": {
                "A": "Oxidizer Strength, because stars burn fuel similar to firework oxidizers.",
                "B": "Combustion Temperature, because stellar temperatures determine which elements are present.",
                "C": "Element Type, because each element's unique emission spectrum serves as a fingerprint identifiable across any distance.",
                "D": "Color Wavelength, because all stars emit the same wavelengths regardless of composition."
            },
            "correct": "C",
            "feedback_correct": "Correct. Each element produces a unique emission spectrum regardless of distance. Astronomers analyze starlight for these characteristic spectral lines to identify which elements are present in the star's atmosphere.",
            "feedback_incorrect": "Incorrect. The key principle is that each element produces a unique emission spectrum (spectral fingerprint) based on its electron energy levels. This spectrum is the same whether the element is in a firework or a star billions of light-years away."
        },
        {
            "question": "Based on the model, a pyrotechnician wants to produce the purest possible green firework. Which combination of component settings would the model predict will yield the best result?",
            "choices": {
                "A": "Barium chloride with maximum Oxidizer Strength to ensure all electrons are excited.",
                "B": "Barium chloride with moderate Oxidizer Strength to achieve sufficient electron excitation without excessive blackbody radiation.",
                "C": "A mixture of strontium and copper chloride with high Oxidizer Strength.",
                "D": "Any metal salt with maximum Combustion Temperature, since higher temperatures produce brighter and purer colors."
            },
            "correct": "B",
            "feedback_correct": "Correct. Barium produces green emission (~525 nm). Moderate oxidizer provides enough energy to excite electrons without generating excessive blackbody radiation that would wash out the color purity.",
            "feedback_incorrect": "Incorrect. For pure color, the correct metal salt (barium for green) must be paired with moderate oxidizer strength. Too much oxidizer creates excessive blackbody radiation that drowns out the characteristic emission, reducing color purity."
        }
    ]
}

L02_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Nuclear power plants generate electricity through a process called fission. Which of the following best describes what occurs during nuclear fission?",
            "choices": {
                "A": "Two light atomic nuclei combine to form a heavier nucleus, releasing energy.",
                "B": "A heavy atomic nucleus splits into two lighter nuclei, releasing a large amount of energy.",
                "C": "Electrons are stripped from uranium atoms, and the free electrons flow as electric current.",
                "D": "Uranium atoms burn in oxygen like fossil fuels, producing heat to generate steam."
            },
            "correct": "B",
            "feedback_correct": "Correct. Nuclear fission involves splitting heavy nuclei (such as uranium-235) into lighter elements, releasing enormous energy from the conversion of a small amount of mass according to E=mc^2.",
            "feedback_incorrect": "Incorrect. Fission is the splitting of a heavy nucleus into lighter nuclei. This is distinct from fusion (combining nuclei), chemical combustion, or electron stripping."
        },
        {
            "question": "Compared to burning coal, nuclear fission produces approximately how much more energy per kilogram of fuel?",
            "choices": {
                "A": "About 10 times more energy.",
                "B": "About 1,000 times more energy.",
                "C": "About 2 million times more energy.",
                "D": "About the same amount of energy, but with less pollution."
            },
            "correct": "C",
            "feedback_correct": "Correct. Nuclear fission releases roughly 2 million times more energy per kilogram than chemical combustion of coal, making nuclear fuel extraordinarily energy-dense.",
            "feedback_incorrect": "Incorrect. The energy density difference between nuclear fuel and coal is enormous. A single uranium fuel pellet produces as much energy as approximately one ton of coal."
        },
        {
            "question": "Which of the following is the primary environmental concern associated with nuclear power generation?",
            "choices": {
                "A": "Large quantities of carbon dioxide emissions during normal operation.",
                "B": "Radioactive waste that remains hazardous for thousands to hundreds of thousands of years.",
                "C": "Destruction of the ozone layer from radiation leaks.",
                "D": "Consumption of large quantities of fossil fuels to enrich uranium."
            },
            "correct": "B",
            "feedback_correct": "Correct. The primary environmental challenge of nuclear power is the production of radioactive waste, particularly spent fuel containing isotopes that remain dangerous for extremely long periods.",
            "feedback_incorrect": "Incorrect. Nuclear power produces virtually no CO2 during operation. The main concern is long-lived radioactive waste that must be securely stored for thousands of years."
        },
        {
            "question": "The half-life of a radioactive isotope is 30 years. If a sample starts with 1,000 grams of the isotope, approximately how much will remain after 90 years?",
            "choices": {
                "A": "500 grams",
                "B": "250 grams",
                "C": "125 grams",
                "D": "0 grams"
            },
            "correct": "C",
            "feedback_correct": "Correct. After 3 half-lives (90 years / 30 years each): 1,000 -> 500 -> 250 -> 125 grams. Each half-life reduces the remaining quantity by exactly half.",
            "feedback_incorrect": "Incorrect. After 3 half-lives (90/30 = 3), the calculation is: 1,000 x (1/2)^3 = 125 grams. Each half-life halves the remaining amount."
        },
        {
            "question": "When evaluating energy sources for reducing climate change, which factor makes nuclear power a strong candidate despite its drawbacks?",
            "choices": {
                "A": "Nuclear power plants can be built quickly and cheaply compared to renewable energy.",
                "B": "Nuclear power produces near-zero carbon emissions during operation while providing reliable baseload electricity.",
                "C": "Nuclear waste can be safely recycled into new fuel indefinitely.",
                "D": "Nuclear power requires no water for cooling, minimizing environmental impact."
            },
            "correct": "B",
            "feedback_correct": "Correct. Nuclear power's lifecycle carbon emissions (~12 g CO2/kWh) are comparable to wind power and far below fossil fuels, while providing consistent 24/7 baseload power independent of weather.",
            "feedback_incorrect": "Incorrect. Nuclear power's key advantage for climate is its near-zero operational carbon emissions combined with its ability to provide reliable baseload power around the clock, unlike intermittent renewable sources."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the computational model, when Fission Rate is increased, both Energy Output and Radioactive Waste increase proportionally. What does this relationship reveal about nuclear power as an energy source?",
            "choices": {
                "A": "Energy and waste can be independently optimized by adjusting reactor design.",
                "B": "Energy production and waste generation are inseparable outputs of the fission process.",
                "C": "Waste production can be eliminated by increasing the fission rate beyond a critical threshold.",
                "D": "The relationship is coincidental and would not hold in a real reactor."
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that energy and waste are coupled outputs of fission. Every atom that splits produces both useful energy and radioactive fission products. You cannot have one without the other.",
            "feedback_incorrect": "Incorrect. The model shows a fundamental physical reality: fission simultaneously produces energy and radioactive waste. These are inseparable products of the same nuclear reaction."
        },
        {
            "question": "A student uses the model to compare nuclear and natural gas electricity generation. The nuclear plant avoids 4 million tons of CO2 annually but produces 20 metric tons of radioactive waste. Which analysis best evaluates this trade-off?",
            "choices": {
                "A": "The waste is a small volume but remains dangerous for millennia, while the CO2 avoidance provides an immediate, large-scale climate benefit.",
                "B": "Since nuclear waste is more dangerous per kilogram than CO2, nuclear power is always worse for the environment.",
                "C": "The CO2 avoidance is irrelevant because climate change is a less serious threat than nuclear waste.",
                "D": "The trade-off cannot be evaluated because the risks operate on different timescales."
            },
            "correct": "A",
            "feedback_correct": "Correct. This captures the central trade-off: nuclear waste is small in volume but long-lived in hazard, while carbon avoidance is massive in scale and provides immediate climate benefits. Both factors must be weighed.",
            "feedback_incorrect": "Incorrect. Evaluating this trade-off requires considering both the scale and timescale of each impact. The waste is small-volume but long-term; the carbon avoidance is large-scale and addresses an urgent crisis."
        },
        {
            "question": "The model shows that reducing the Fission Rate to 50% decreases Energy Output proportionally. A policy analyst argues this means nuclear plants should always run at full power. Which limitation of this argument does the model reveal?",
            "choices": {
                "A": "Running at full power is unsafe because reactors cannot be controlled at maximum fission rates.",
                "B": "Running at full power also proportionally increases Radioactive Waste, so the cost-benefit ratio remains constant regardless of power level.",
                "C": "The model shows that full power operation depletes uranium fuel too rapidly to be economically viable.",
                "D": "Reduced power operation actually increases efficiency by allowing better neutron moderation."
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that waste scales proportionally with energy output. Running at full power maximizes both energy and waste. The analyst's argument ignores the waste side of the trade-off.",
            "feedback_incorrect": "Incorrect. The key insight is that the waste-to-energy ratio is constant regardless of power level. The argument for full power ignores that waste generation also increases proportionally."
        },
        {
            "question": "Germany phased out nuclear power after Fukushima, and its carbon emissions subsequently increased because it burned more coal. Based on the model, which conclusion is best supported?",
            "choices": {
                "A": "Germany should have kept nuclear power because coal is always worse for the environment.",
                "B": "Removing nuclear baseload power without sufficient replacement led to increased fossil fuel use, demonstrating the interconnected nature of energy portfolio decisions.",
                "C": "The model proves that nuclear power is the only viable alternative to coal.",
                "D": "Germany's decision was purely political and had no scientific basis."
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that energy portfolio decisions are interconnected. Removing one source (nuclear) without adequate zero-carbon replacement forces increased reliance on fossil fuels, increasing emissions.",
            "feedback_incorrect": "Incorrect. The model supports the principle that energy systems are interconnected. Removing nuclear capacity without equivalent zero-carbon replacement creates a gap that fossil fuels typically fill, increasing emissions."
        },
        {
            "question": "Using the model's Fuel Depletion scenario, a single reactor fuel load produces tens of billions of kWh while generating approximately 20 tons of spent fuel. Which statement best characterizes nuclear fuel's energy density based on this evidence?",
            "choices": {
                "A": "Nuclear fuel has moderate energy density, comparable to natural gas.",
                "B": "Nuclear fuel has the highest energy density of any practical fuel source, producing enormous electricity from tiny quantities of material.",
                "C": "Nuclear fuel is energy-dense but not significantly more so than solar panels per unit area.",
                "D": "The energy density depends entirely on reactor design rather than the properties of the fuel itself."
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates nuclear fuel's extraordinary energy density: a single fuel pellet the size of a pencil eraser produces as much energy as a ton of coal, making it roughly 2 million times more energy-dense than chemical fuels.",
            "feedback_incorrect": "Incorrect. The model data shows that nuclear fuel produces enormous energy from small quantities of material. This extreme energy density is a fundamental property of nuclear versus chemical reactions."
        }
    ]
}

L03_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A roller coaster reaches the top of its first hill moving very slowly. As it descends, it accelerates rapidly. Which energy transformation best explains this acceleration?",
            "choices": {
                "A": "Chemical energy from the motor converts to kinetic energy throughout the ride.",
                "B": "Gravitational potential energy converts to kinetic energy as the coaster loses height.",
                "C": "Thermal energy from friction converts to kinetic energy, speeding up the coaster.",
                "D": "The coaster accelerates because air pressure pushes it downhill."
            },
            "correct": "B",
            "feedback_correct": "Correct. At the top of a hill, the coaster has maximum gravitational potential energy (PE = mgh). As it descends, this potential energy converts to kinetic energy (KE = 1/2 mv^2), increasing its speed.",
            "feedback_incorrect": "Incorrect. After the initial chain lift, the coaster has no motor. Its acceleration on descents comes from the conversion of stored gravitational potential energy into kinetic energy."
        },
        {
            "question": "On a roller coaster, why must the second hill always be shorter than the first hill?",
            "choices": {
                "A": "Building taller hills after the first one would be structurally unsafe.",
                "B": "Energy is lost to friction throughout the ride, so the coaster cannot regain its original height without additional energy input.",
                "C": "The coaster gains mass as it moves, requiring less height for the same thrill.",
                "D": "Air resistance pushes the coaster downward, preventing it from climbing as high."
            },
            "correct": "B",
            "feedback_correct": "Correct. The first hill represents the total energy budget. Friction continuously removes energy from the system as heat, so less potential energy is available for subsequent hills, making each one necessarily shorter.",
            "feedback_incorrect": "Incorrect. Conservation of energy dictates that the coaster cannot return to its original height because friction converts some mechanical energy to thermal energy. Each subsequent hill must be shorter than the previous one."
        },
        {
            "question": "Two roller coasters descend from the same height. Coaster A has a mass of 5,000 kg and Coaster B has a mass of 10,000 kg. Ignoring friction, which coaster reaches a greater speed at the bottom?",
            "choices": {
                "A": "Coaster B, because it has more gravitational potential energy.",
                "B": "Coaster A, because lighter objects fall faster.",
                "C": "Both reach the same speed, because mass cancels out of the energy conservation equation.",
                "D": "It depends on the shape of the track, not the mass."
            },
            "correct": "C",
            "feedback_correct": "Correct. Setting PE = KE: mgh = 1/2 mv^2. Mass cancels, giving v = sqrt(2gh). Speed at the bottom depends only on the height of the drop, not the coaster's mass.",
            "feedback_incorrect": "Incorrect. From energy conservation, v = sqrt(2gh). Mass appears on both sides and cancels. Both coasters reach exactly the same speed, confirming Galileo's principle that all objects fall at the same rate."
        },
        {
            "question": "A rider on a roller coaster feels pushed into their seat at the bottom of a steep drop. Which force is responsible for this sensation?",
            "choices": {
                "A": "Gravitational force increasing as the coaster moves faster.",
                "B": "Centripetal acceleration from the curved track, which adds to the normal gravitational force.",
                "C": "Air resistance pushing the rider downward at high speeds.",
                "D": "The rider's inertia pulling them upward while the seat pushes them down."
            },
            "correct": "B",
            "feedback_correct": "Correct. At the bottom of a curve, the track must provide centripetal force (directed upward) in addition to supporting the rider's weight. This combined force creates the sensation of increased G-force.",
            "feedback_incorrect": "Incorrect. The heavy sensation at the bottom of a drop is caused by centripetal acceleration (a = v^2/r) from the curved track. This acceleration adds to gravity, making riders feel heavier than normal."
        },
        {
            "question": "A roller coaster engineer states that the chain lift at the beginning is the only source of energy for the entire ride. Which principle of physics supports this claim?",
            "choices": {
                "A": "Newton's first law of motion (objects in motion stay in motion).",
                "B": "The law of conservation of energy (energy cannot be created or destroyed).",
                "C": "Newton's third law of motion (every action has an equal and opposite reaction).",
                "D": "The second law of thermodynamics (entropy always increases)."
            },
            "correct": "B",
            "feedback_correct": "Correct. Conservation of energy means the total mechanical energy is set by the chain lift. After that, energy only converts between forms (PE to KE) and is lost to friction. No new energy is added.",
            "feedback_incorrect": "Incorrect. The conservation of energy principle explains that the chain lift's energy input is the ride's total energy budget. All subsequent motion comes from converting this stored potential energy."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "Using the computational model, a student tests a 50-meter first hill. The model predicts the coaster reaches 31.3 m/s at the bottom (ignoring friction). The student then changes the coaster mass from 5,000 kg to 15,000 kg and runs the simulation again. What velocity does the model predict at the bottom?",
            "choices": {
                "A": "10.4 m/s, because the heavier coaster has more inertia.",
                "B": "31.3 m/s, because velocity at the bottom is independent of mass.",
                "C": "93.9 m/s, because more mass means more kinetic energy.",
                "D": "The model cannot predict this without knowing the track shape."
            },
            "correct": "B",
            "feedback_correct": "Correct. The model confirms v = sqrt(2gh). Since mass cancels from the equation, the heavier coaster reaches exactly the same speed. This validates Galileo's principle within the computational model.",
            "feedback_incorrect": "Incorrect. The model demonstrates that v = sqrt(2gh), where mass does not appear. Tripling the mass does not change the velocity at the bottom of the same drop."
        },
        {
            "question": "The model shows that a coaster traveling at 30 m/s through a loop with a 10-meter radius produces approximately 9.2 G-forces at the bottom. An engineer wants to reduce this to 4 G. Which model adjustment would achieve this?",
            "choices": {
                "A": "Increase the loop radius to reduce centripetal acceleration while maintaining the same speed.",
                "B": "Decrease the coaster mass to reduce the force on riders.",
                "C": "Increase the height of the preceding hill to give the coaster more energy.",
                "D": "Add friction before the loop to increase the G-force."
            },
            "correct": "A",
            "feedback_correct": "Correct. G-force at the bottom of a loop depends on v^2/r. Increasing the radius (r) while maintaining the same velocity decreases centripetal acceleration and thus the G-force experienced by riders.",
            "feedback_incorrect": "Incorrect. Since G-force depends on centripetal acceleration (a = v^2/r), increasing the loop radius directly reduces the acceleration and G-force without changing the coaster's speed."
        },
        {
            "question": "A student runs the model with a 60-meter first hill and finds the coaster reaches 34 m/s at the bottom. With 10% energy lost to friction, what is the maximum height of the second hill the model would allow?",
            "choices": {
                "A": "60 meters, because some energy is recovered during the climb.",
                "B": "54 meters, because 10% of the original potential energy has been lost to friction.",
                "C": "30 meters, because friction removes half the energy.",
                "D": "The second hill can be any height as long as the track shape provides enough momentum."
            },
            "correct": "B",
            "feedback_correct": "Correct. With 10% energy loss, only 90% of the original PE remains. Since PE = mgh, the maximum height = 0.90 x 60 m = 54 m. The model correctly reflects conservation of energy minus friction losses.",
            "feedback_incorrect": "Incorrect. If 10% of the total energy is lost to friction, only 90% remains as mechanical energy. The maximum second hill height is 90% of the first hill: 0.90 x 60 = 54 meters."
        },
        {
            "question": "The model predicts that riders experience approximately 0 G (weightlessness) at the top of a parabolic hill when v^2/r = g. What does this finding reveal about the physics of 'airtime' on a roller coaster?",
            "choices": {
                "A": "Gravity temporarily stops acting on riders at the top of hills.",
                "B": "The track curves away from the rider at exactly the rate that gravity would pull them, so no normal force is needed from the seat.",
                "C": "Wind resistance lifts the riders out of their seats at high speeds.",
                "D": "The coaster's kinetic energy is converted entirely to gravitational potential energy at the hill crest."
            },
            "correct": "B",
            "feedback_correct": "Correct. At 0 G, the centripetal acceleration needed to follow the track exactly equals gravitational acceleration. The rider is essentially in free fall while following the track curve, so no seat force is felt.",
            "feedback_incorrect": "Incorrect. Weightlessness occurs when the track's curvature matches the trajectory of free fall. The rider's body naturally follows a parabolic path at that speed, requiring zero contact force from the seat."
        },
        {
            "question": "Based on model evidence, a student argues that the coaster's energy is not truly 'conserved' because it slows down and eventually stops. Which response best addresses this argument using the model?",
            "choices": {
                "A": "The student is correct. Energy conservation is only an approximation that doesn't apply to real systems.",
                "B": "Energy IS conserved. The mechanical energy converts to thermal energy through friction, so total energy remains constant even though the coaster's speed decreases.",
                "C": "The model shows that gravity gradually removes energy from the system over time.",
                "D": "The brakes at the end create new energy that replaces what was lost to friction."
            },
            "correct": "B",
            "feedback_correct": "Correct. The law of conservation of energy holds perfectly. Friction converts kinetic energy to thermal energy (heat in wheels, rails, and air). Total energy is constant; only the useful mechanical energy decreases.",
            "feedback_incorrect": "Incorrect. Energy conservation is a universal law. The coaster slows because friction converts mechanical energy to thermal energy, not because energy disappears. Total energy (mechanical + thermal) remains constant."
        }
    ]
}

L04_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Sound travels through air as a wave. When a microphone captures this sound, what physical quantity does it detect?",
            "choices": {
                "A": "Changes in air temperature caused by the sound source.",
                "B": "Variations in air pressure that correspond to the frequency and amplitude of the sound wave.",
                "C": "Electromagnetic radiation emitted by vibrating molecules.",
                "D": "The velocity of individual air molecules traveling from the source to the microphone."
            },
            "correct": "B",
            "feedback_correct": "Correct. Sound is a longitudinal pressure wave. A microphone's diaphragm responds to the alternating compressions and rarefactions of air pressure, converting them to an electrical signal.",
            "feedback_incorrect": "Incorrect. Sound is a mechanical pressure wave. The microphone detects pressure variations in the air that correspond to the sound's frequency (pitch) and amplitude (loudness)."
        },
        {
            "question": "A 3-minute song stored as an uncompressed audio file is approximately 30 MB. The same song compressed as an MP3 is 3 MB. What was removed during compression?",
            "choices": {
                "A": "The lower-quality instruments in the recording.",
                "B": "Every other sound sample, cutting the data in half repeatedly.",
                "C": "Sounds and frequencies that fall below the threshold of human hearing perception.",
                "D": "The silence between notes, which takes up most of the file."
            },
            "correct": "C",
            "feedback_correct": "Correct. Lossy compression algorithms like MP3 use psychoacoustic models to identify and remove frequencies humans cannot hear, sounds masked by louder sounds, and redundant data patterns.",
            "feedback_incorrect": "Incorrect. MP3 compression exploits the limits of human hearing. It removes inaudible frequencies (above ~20 kHz), sounds masked by louder simultaneous sounds, and temporal details the brain fills in."
        },
        {
            "question": "The Nyquist theorem states that to accurately capture a sound wave digitally, the sampling rate must be at least:",
            "choices": {
                "A": "Equal to the frequency of the sound wave.",
                "B": "Twice the highest frequency to be captured.",
                "C": "Ten times the highest frequency to ensure accuracy.",
                "D": "Independent of frequency, as long as bit depth is sufficient."
            },
            "correct": "B",
            "feedback_correct": "Correct. The Nyquist theorem requires sampling at twice the maximum frequency. CD quality samples at 44,100 Hz to capture frequencies up to 22,050 Hz, exceeding the ~20,000 Hz limit of human hearing.",
            "feedback_incorrect": "Incorrect. The Nyquist theorem requires a sampling rate of at least twice the highest frequency in the signal. This prevents aliasing and ensures accurate digital reproduction of the analog waveform."
        },
        {
            "question": "A music streaming service recommends songs to users. Which type of data would be MOST useful for the recommendation algorithm?",
            "choices": {
                "A": "The user's age, gender, and geographic location.",
                "B": "Patterns of listening behavior, including play counts, skip rates, and completion rates across many users.",
                "C": "The recording quality and bit rate of each song file.",
                "D": "The number of awards each artist has won."
            },
            "correct": "B",
            "feedback_correct": "Correct. Recommendation algorithms rely on behavioral data. Play counts, skip rates, listening duration, and patterns across millions of users reveal preferences far more accurately than demographic data alone.",
            "feedback_incorrect": "Incorrect. Behavioral listening data (what people play, skip, repeat, and how they interact with suggestions) provides the richest signal for predicting preferences through collaborative filtering."
        },
        {
            "question": "Which statement accurately describes the relationship between audio file size and sound quality in digital music?",
            "choices": {
                "A": "Larger files always sound better because they contain more data.",
                "B": "There is a trade-off: higher quality requires more data, but beyond a threshold most listeners cannot detect further improvements.",
                "C": "File size has no relationship to sound quality in modern formats.",
                "D": "Smaller files sound better because compression removes noise and distortion."
            },
            "correct": "B",
            "feedback_correct": "Correct. Higher bit rates and sampling rates capture more audio detail, but human hearing has limits. Above approximately 256 kbps, most listeners cannot distinguish compressed from uncompressed audio in blind tests.",
            "feedback_incorrect": "Incorrect. There is a direct trade-off between file size and quality, but it has a perceptual ceiling. Beyond a certain quality level, the human auditory system cannot detect further improvements."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that at maximum Data Compression Rate, audio quality degrades noticeably. At moderate compression, quality is virtually indistinguishable from the original. What concept from wave physics explains why moderate compression works without perceptible quality loss?",
            "choices": {
                "A": "Destructive interference cancels out the removed frequencies.",
                "B": "Psychoacoustic masking means louder sounds hide quieter sounds from perception, so removing the masked sounds is undetectable.",
                "C": "The human ear processes all frequencies equally, so removing some has minimal impact.",
                "D": "Compression algorithms add synthetic frequencies to replace removed data."
            },
            "correct": "B",
            "feedback_correct": "Correct. Psychoacoustic masking is a property of human hearing where loud sounds render quieter nearby sounds imperceptible. Compression algorithms exploit this by removing masked data that the listener would never perceive.",
            "feedback_incorrect": "Incorrect. The model demonstrates that compression works because of psychoacoustic masking. Human hearing naturally suppresses perception of sounds masked by louder sounds, making their removal undetectable."
        },
        {
            "question": "In the model, a new user with no listening history receives recommendations with approximately 20-30% accuracy, while a veteran user with 1,000+ hours has 70-80% accuracy. What system behavior does this demonstrate?",
            "choices": {
                "A": "Linear growth, where accuracy improves at a constant rate with each hour of listening.",
                "B": "A positive feedback loop, where engagement generates data that improves predictions, which increases engagement and generates more data.",
                "C": "Random variation, where accuracy fluctuates unpredictably regardless of data quantity.",
                "D": "Diminishing returns, where additional data beyond the first hour provides no benefit."
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals a positive feedback loop: more listening generates more behavioral data, which trains better algorithms, which provide better recommendations, which increases engagement and data generation.",
            "feedback_incorrect": "Incorrect. The model demonstrates a feedback loop: engagement produces data, data improves algorithm accuracy, better accuracy increases user satisfaction and engagement, generating more data."
        },
        {
            "question": "A student examines the model and notices that a 64 GB device stores approximately 1,200 songs at maximum quality but 12,000 songs at standard compression. The student argues that maximum compression should always be used. Which model evidence challenges this argument?",
            "choices": {
                "A": "Maximum compression makes files too small for the device to read efficiently.",
                "B": "Beyond a critical compression threshold, audio quality degrades enough that user engagement decreases, reducing the effectiveness of recommendation algorithms.",
                "C": "Maximum compression takes too long to process on mobile devices.",
                "D": "The model shows that all compression levels produce identical listening experiences."
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that excessive compression degrades quality, which reduces user engagement, which decreases the data feeding the recommendation algorithm. The system optimizes for a balance, not a single variable.",
            "feedback_incorrect": "Incorrect. The model demonstrates that compression exists on a curve with diminishing returns. Beyond the perception threshold, further compression degrades quality enough to reduce engagement, harming the entire system."
        },
        {
            "question": "Based on the model, which statement best explains why digital music storage became practical for portable devices?",
            "choices": {
                "A": "Storage devices became large enough to hold uncompressed audio files.",
                "B": "Engineers discovered that the physics of human hearing perception could be exploited to reduce file sizes by 90% without perceptible quality loss.",
                "C": "Music quality standards were lowered to accommodate smaller storage.",
                "D": "Digital signals are inherently smaller than analog signals."
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that psychoacoustic compression, based on wave physics and human hearing limits, enables 90% data reduction while maintaining perceptually identical quality, making portable music libraries possible.",
            "feedback_incorrect": "Incorrect. The breakthrough was understanding that human hearing has specific limitations (frequency range, masking effects) that compression algorithms can exploit to dramatically reduce file sizes without perceptible quality loss."
        },
        {
            "question": "The model demonstrates that algorithm accuracy improves from 20% to 80% as listening data increases. A privacy advocate argues that less data should be collected. Using the model, which design approach best addresses both accuracy and privacy concerns?",
            "choices": {
                "A": "Collect all possible data since accuracy is the only goal.",
                "B": "Collect no data and rely on random recommendations.",
                "C": "Identify the minimum data points needed to reach acceptable accuracy, and collect only those, transparently disclosing what is collected and why.",
                "D": "The model proves privacy and accuracy are completely incompatible goals."
            },
            "correct": "C",
            "feedback_correct": "Correct. The model shows diminishing returns in accuracy with additional data. Engineering solutions can identify the optimal data collection level that achieves acceptable accuracy while minimizing privacy intrusion.",
            "feedback_incorrect": "Incorrect. The model shows diminishing returns in the data-accuracy relationship. This means a balance point exists where sufficient accuracy is achieved with limited, transparent data collection."
        }
    ]
}

L05_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A trait like height is described as 'polygenic.' What does this mean?",
            "choices": {
                "A": "The trait is controlled by a single gene with multiple alleles.",
                "B": "The trait is influenced by many different genes, each contributing a small effect.",
                "C": "The trait is determined entirely by environmental factors, not genetics.",
                "D": "The trait skips generations and appears only in every other generation."
            },
            "correct": "B",
            "feedback_correct": "Correct. Polygenic traits like height are influenced by hundreds of genes, each contributing a small amount to the final phenotype, resulting in a continuous distribution in populations.",
            "feedback_incorrect": "Incorrect. 'Polygenic' means controlled by many genes (poly = many). Height is influenced by over 700 identified genetic variants, each contributing a small effect to the overall trait."
        },
        {
            "question": "The average height in the Netherlands increased by 18 cm over the past 160 years. Which factor most likely explains this increase?",
            "choices": {
                "A": "Natural selection favored taller individuals, causing rapid genetic evolution.",
                "B": "Improvements in childhood nutrition allowed people to reach more of their genetic height potential.",
                "C": "Interbreeding with taller populations introduced height-increasing genes.",
                "D": "Climate change in Northern Europe stimulated bone growth in all populations."
            },
            "correct": "B",
            "feedback_correct": "Correct. The secular trend happened over only 6 generations, far too fast for genetic evolution. Improved nutrition during childhood provided the raw materials for maximum bone growth, allowing more genetic potential to be realized.",
            "feedback_incorrect": "Incorrect. Genetic evolution requires hundreds of generations, but this change occurred in just 6. The secular height trend is primarily explained by improved childhood nutrition enabling fuller expression of existing genetic potential."
        },
        {
            "question": "Which of the following best describes the concept of epigenetics?",
            "choices": {
                "A": "Mutations that permanently alter the DNA sequence and are passed to offspring.",
                "B": "Changes in gene activity caused by environmental factors that do not alter the DNA sequence itself.",
                "C": "The study of genetic diseases that appear only in certain ethnic groups.",
                "D": "The process by which genes are copied during cell division."
            },
            "correct": "B",
            "feedback_correct": "Correct. Epigenetics involves chemical modifications (like methylation) that turn genes on or off without changing the DNA sequence. Environmental factors like nutrition can trigger these modifications.",
            "feedback_incorrect": "Incorrect. Epigenetic changes affect gene ACTIVITY (expression), not the DNA sequence itself. Environmental factors like nutrition can activate or silence genes through chemical modifications to DNA or histones."
        },
        {
            "question": "In humans, growth plates are regions of cartilage near the ends of long bones. What happens when growth plates fuse during late adolescence?",
            "choices": {
                "A": "Bones continue to grow but at a slower rate.",
                "B": "Height increase stops permanently because no new bone can be added to the length.",
                "C": "Growth hormone production ceases entirely.",
                "D": "The bones begin to shrink as calcium is reabsorbed."
            },
            "correct": "B",
            "feedback_correct": "Correct. When growth plates fuse (ossify), the cartilage is replaced by solid bone, permanently ending longitudinal bone growth. No amount of nutrition or hormones can increase height after fusion.",
            "feedback_incorrect": "Incorrect. Growth plate fusion is irreversible. Once the cartilage is replaced by bone, no further lengthening is possible, making childhood and adolescent nutrition critically important for reaching full height potential."
        },
        {
            "question": "North Koreans and South Koreans share very similar genetic backgrounds, yet South Koreans are approximately 8 cm taller on average. What does this difference most strongly suggest?",
            "choices": {
                "A": "South Korea has experienced genetic evolution toward taller height over the past 70 years.",
                "B": "Environmental factors, particularly nutrition, significantly influence the expression of height-related genes.",
                "C": "North Koreans carry different height genes due to geographic isolation.",
                "D": "Height is entirely determined by environment, and genetics plays no role."
            },
            "correct": "B",
            "feedback_correct": "Correct. The genetic similarity between the two populations, combined with their dramatically different nutrition environments, demonstrates that environmental factors significantly affect how height genes are expressed.",
            "feedback_incorrect": "Incorrect. This natural experiment shows that with nearly identical genetics, dramatically different nutrition environments produce significant height differences, demonstrating the power of gene-environment interaction."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The computational model shows that setting Nutrition Quality to maximum produces Final Height near the top of the genetic range, while setting it to low produces Final Height well below the genetic range. What does this demonstrate about the nature vs. nurture debate?",
            "choices": {
                "A": "Nature (genetics) is more important than nurture (environment) for determining height.",
                "B": "Nurture (environment) completely overrides nature (genetics) in determining height.",
                "C": "Genetics sets a range of possible heights, and environmental factors determine where within that range an individual falls.",
                "D": "The model cannot distinguish between genetic and environmental effects."
            },
            "correct": "C",
            "feedback_correct": "Correct. The model demonstrates that genes establish the boundaries (range) of possible height, but nutrition determines the actual height achieved within that range. Neither factor alone determines the outcome.",
            "feedback_incorrect": "Incorrect. The model shows an interactive relationship: genetics defines the potential range, and environment (especially nutrition) determines where within that range a person ends up."
        },
        {
            "question": "In the generational comparison scenario, the model produces an 8-12 cm height difference using identical genetic components but 1940s versus 2020s nutrition. A student claims this proves 'genetics doesn't matter.' Which model evidence refutes this claim?",
            "choices": {
                "A": "Both scenarios still produce heights within the genetically defined range, showing genetics sets the boundaries.",
                "B": "The model doesn't include any genetic components.",
                "C": "The nutrition variable had no measurable effect in the model.",
                "D": "The height difference was too small to be significant."
            },
            "correct": "A",
            "feedback_correct": "Correct. Even with dramatic nutritional differences, both heights fall within the genetically defined range. Genetics determines the ceiling and floor; nutrition determines the position within those limits. Both matter.",
            "feedback_incorrect": "Incorrect. The model shows that while nutrition shifts height significantly, the result always stays within the genetically determined range. This proves BOTH genetics and environment are essential determinants."
        },
        {
            "question": "The model reveals a cascade: Nutrition Quality affects Gene Expression Level, which affects Growth Hormone Release, which affects Bone Growth Rate, which determines Final Height. If a child has excellent nutrition but a genetic condition that limits Growth Hormone Release, what does the model predict?",
            "choices": {
                "A": "The child will reach normal height because nutrition can compensate for hormonal deficiency.",
                "B": "The cascade is interrupted. Even with strong gene expression and nutrition, reduced growth hormone will limit bone growth and final height.",
                "C": "The model predicts the child will be taller than average because nutrition is more important than hormones.",
                "D": "The genetic condition will have no effect because growth plates respond directly to nutrition."
            },
            "correct": "B",
            "feedback_correct": "Correct. The model's cascade structure shows that each component depends on the one before it. A disruption at any point in the chain (in this case, Growth Hormone Release) limits all downstream outcomes.",
            "feedback_incorrect": "Incorrect. The cascade model demonstrates sequential dependence. Even with optimal upstream conditions, a limitation at any point in the chain constrains all downstream components, including final height."
        },
        {
            "question": "A public health researcher uses the model to argue for investing in school nutrition programs. Which model scenario provides the strongest evidence for this argument?",
            "choices": {
                "A": "The Optimal Nutrition scenario, which shows that maximum nutrition produces maximum height.",
                "B": "The Generational Comparison scenario, which demonstrates that improving nutrition quality produces measurable height gains within a single generation.",
                "C": "The Nutritional Deprivation scenario, which shows that poor nutrition has no lasting effects.",
                "D": "The model cannot inform public health policy because it only models individual growth."
            },
            "correct": "B",
            "feedback_correct": "Correct. The Generational Comparison scenario directly demonstrates that improving nutrition, not changing genetics, produces significant measurable height gains. This shows a clear return on nutritional investment within one generation.",
            "feedback_incorrect": "Incorrect. The Generational Comparison scenario is the strongest evidence because it isolates nutrition as the variable while holding genetics constant, demonstrating that nutritional improvements produce measurable results within a single generation."
        },
        {
            "question": "The model shows that growth plates fuse in late adolescence, after which no further height increase is possible. What critical implication does this have for the timing of nutrition interventions?",
            "choices": {
                "A": "Nutrition interventions are equally effective at any age.",
                "B": "Interventions in adulthood are most effective because adults need more nutrients.",
                "C": "The window for nutritional impact on height is limited to childhood and adolescence. Interventions must occur before growth plate fusion to affect final height.",
                "D": "Growth plates can reopen with sufficient nutrition, so timing does not matter."
            },
            "correct": "C",
            "feedback_correct": "Correct. The model demonstrates that growth plates represent a limited window of opportunity. Once they fuse, height is permanently set. This makes childhood and adolescent nutrition critically time-sensitive.",
            "feedback_incorrect": "Incorrect. Growth plate fusion is irreversible. The model shows that the window for influencing height through nutrition closes permanently in late adolescence, making early intervention essential."
        }
    ]
}

L06_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "In a food web, what is the most likely consequence of removing the top predator from an ecosystem?",
            "choices": {
                "A": "All other species in the ecosystem will thrive because there is less predation.",
                "B": "Herbivore populations will increase unchecked, potentially overgrazing vegetation and destabilizing the ecosystem.",
                "C": "The ecosystem will quickly self-correct and establish a new stable state.",
                "D": "Only the species directly eaten by the predator will be affected."
            },
            "correct": "B",
            "feedback_correct": "Correct. Without top-down control, herbivore populations can explode beyond carrying capacity, leading to overgrazing, vegetation loss, and cascading effects throughout the ecosystem.",
            "feedback_incorrect": "Incorrect. Removing a top predator allows herbivore populations to grow unchecked, which cascades through the ecosystem as overgrazing damages vegetation and habitat for many other species."
        },
        {
            "question": "The term 'carrying capacity' refers to which ecological concept?",
            "choices": {
                "A": "The maximum number of predators an ecosystem can support.",
                "B": "The maximum population size that an environment can sustain indefinitely given available resources.",
                "C": "The total biomass of all organisms in an ecosystem.",
                "D": "The rate at which a population grows under ideal conditions."
            },
            "correct": "B",
            "feedback_correct": "Correct. Carrying capacity (K) is the maximum population an environment can sustain over time, determined by available food, water, shelter, and space. Populations exceeding K face resource depletion.",
            "feedback_incorrect": "Incorrect. Carrying capacity is the maximum sustainable population size for a given environment, limited by available resources. Exceeding it leads to resource depletion and population decline."
        },
        {
            "question": "A 'keystone species' is best defined as a species that:",
            "choices": {
                "A": "Has the largest population in the ecosystem.",
                "B": "Has an impact on the ecosystem disproportionately large compared to its population size.",
                "C": "Is at the bottom of the food web and supports all other organisms.",
                "D": "Can survive in the widest range of environmental conditions."
            },
            "correct": "B",
            "feedback_correct": "Correct. Keystone species have effects on ecosystem structure and function far beyond what their numbers suggest. Removing them causes fundamental changes to the ecosystem's organization.",
            "feedback_incorrect": "Incorrect. A keystone species has an outsized ecological impact relative to its abundance. Like a keystone in an arch, its removal causes the entire structure to change or collapse."
        },
        {
            "question": "Wolves were reintroduced to Yellowstone National Park in 1995. Which of the following is a documented ecological change that followed their return?",
            "choices": {
                "A": "Elk populations increased because wolves brought more prey into the park.",
                "B": "Vegetation along rivers recovered as elk changed their grazing behavior to avoid wolf predation areas.",
                "C": "All other predator species left the park due to competition with wolves.",
                "D": "The wolf population immediately reached carrying capacity and stopped growing."
            },
            "correct": "B",
            "feedback_correct": "Correct. Wolf reintroduction created an 'ecology of fear' that changed elk behavior. Elk avoided riverbanks where they were vulnerable, allowing willows and aspens to recover, stabilizing riverbanks.",
            "feedback_incorrect": "Incorrect. Wolves reduced elk grazing pressure, particularly along rivers, through both direct predation and behavioral changes (ecology of fear). Riparian vegetation recovered as a result."
        },
        {
            "question": "In a stable ecosystem, predator and prey populations typically exhibit which pattern over time?",
            "choices": {
                "A": "Both populations remain at constant, unchanging levels.",
                "B": "Predator populations always exceed prey populations.",
                "C": "Oscillating cycles where prey increases are followed by predator increases, then prey decreases.",
                "D": "Both populations grow exponentially without limit."
            },
            "correct": "C",
            "feedback_correct": "Correct. Predator-prey dynamics typically produce cyclical oscillations: prey increase leads to predator increase (more food), which reduces prey, which then reduces predators (less food), and the cycle repeats.",
            "feedback_incorrect": "Incorrect. Classic predator-prey dynamics show oscillating cycles. Prey abundance fuels predator growth, predator growth reduces prey, and prey scarcity causes predator decline, restarting the cycle."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the computational model, setting Predator Pressure to zero causes elk Population Size to increase by 300%, Food Availability to crash, and Extinction Risk for other species to spike. This sequence is best described as a:",
            "choices": {
                "A": "Negative feedback loop that stabilizes the ecosystem.",
                "B": "Trophic cascade, where changes at one trophic level ripple through the entire ecosystem.",
                "C": "Random fluctuation in population that will self-correct over time.",
                "D": "Linear cause-and-effect where only the direct prey species is impacted."
            },
            "correct": "B",
            "feedback_correct": "Correct. This is a trophic cascade: removing the top predator causes a chain reaction through multiple trophic levels, from herbivore boom to vegetation collapse to habitat degradation to biodiversity loss.",
            "feedback_incorrect": "Incorrect. The model demonstrates a trophic cascade, a multi-level chain reaction where changes at the top of the food web ripple down through every level, transforming the entire ecosystem."
        },
        {
            "question": "The model shows that after wolf reintroduction, ecosystem recovery takes significantly longer than the degradation that occurred during wolf absence. Which explanation best accounts for this asymmetry?",
            "choices": {
                "A": "Wolves are less effective at controlling elk populations than expected.",
                "B": "Destruction (overgrazing, erosion, species loss) happens quickly, but rebuilding (vegetation regrowth, soil accumulation, species recolonization) requires much more time.",
                "C": "The model overestimates the speed of degradation.",
                "D": "Recovery is slow because elk populations resist predation through learned behavior."
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals a fundamental asymmetry: destroying ecological structures (killing vegetation, eroding soil) is fast, but rebuilding them (growing trees, rebuilding soil, recolonizing species) requires years to decades.",
            "feedback_incorrect": "Incorrect. Ecological degradation is inherently faster than recovery. Overgrazing can kill decades of vegetation growth in a few years, while regrowth, soil rebuilding, and species recolonization take much longer."
        },
        {
            "question": "The model includes a 'Behavioral Response' component showing that elk change WHERE they graze when wolves are present. Why does the model suggest this 'ecology of fear' may be as important as direct predation?",
            "choices": {
                "A": "Fear causes elk to stop eating entirely, leading to population crash.",
                "B": "Behavioral changes redistribute grazing pressure across the landscape, allowing vegetation recovery in previously overgrazed areas without requiring significant elk population reduction.",
                "C": "The ecology of fear only affects young elk, which are not significant grazers.",
                "D": "Fear-based responses last only a few days before elk resume normal behavior."
            },
            "correct": "B",
            "feedback_correct": "Correct. The ecology of fear changes the SPATIAL distribution of grazing, not just the number of elk. Even modest wolf populations can cause elk to avoid riverbanks and valleys, allowing vegetation recovery in these critical areas.",
            "feedback_incorrect": "Incorrect. The model shows that the ecology of fear redistributes grazing spatially. Elk avoid vulnerable areas (riverbanks, narrow valleys), allowing vegetation recovery in these critical zones regardless of total elk numbers."
        },
        {
            "question": "A student proposes simply reducing elk numbers through hunting instead of reintroducing wolves. Based on the model, which limitation of this approach does the trophic cascade evidence reveal?",
            "choices": {
                "A": "Hunting reduces elk numbers but does not create the behavioral changes (ecology of fear) that redistribute grazing pressure across the landscape.",
                "B": "Hunting is more effective than wolf predation at controlling elk populations.",
                "C": "The model shows that hunting and wolf predation produce identical ecological outcomes.",
                "D": "Hunting would reduce elk populations below the level needed for the ecosystem to function."
            },
            "correct": "A",
            "feedback_correct": "Correct. The model distinguishes between population control (reducing numbers) and behavioral control (changing WHERE elk graze). Wolves provide both; hunting primarily provides only population reduction without the fear-driven spatial redistribution.",
            "feedback_incorrect": "Incorrect. The model reveals that wolves provide two types of control: direct population reduction AND behavioral modification (ecology of fear). Hunting can reduce numbers but does not create the landscape-scale behavioral changes that drive vegetation recovery."
        },
        {
            "question": "The model demonstrates that Population Size, Food Availability, Habitat Area, and Extinction Risk are all interconnected through feedback loops. What does this complexity imply for wildlife management decisions?",
            "choices": {
                "A": "Wildlife management is straightforward because changing one variable predictably controls all others.",
                "B": "Ecosystems are too complex to manage, so intervention should be avoided.",
                "C": "Management decisions must consider the entire system because intervening at one trophic level produces cascading effects at all levels, some of which may be unexpected.",
                "D": "Only the top predator matters; managing any other species is unnecessary."
            },
            "correct": "C",
            "feedback_correct": "Correct. The model demonstrates that ecosystems are interconnected systems where single-variable interventions produce cascading effects throughout multiple trophic levels. Effective management requires systems-level thinking.",
            "feedback_incorrect": "Incorrect. The model shows that ecosystem components are tightly coupled through feedback loops. Changing any one variable cascades through the system, requiring managers to think in terms of whole systems, not isolated species."
        }
    ]
}

L07_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Which of the following is the primary energy source that drives all weather patterns on Earth?",
            "choices": {
                "A": "Heat from Earth's interior (geothermal energy).",
                "B": "Differential solar heating of Earth's surface.",
                "C": "The Moon's gravitational pull on the atmosphere.",
                "D": "Chemical reactions in the upper atmosphere."
            },
            "correct": "B",
            "feedback_correct": "Correct. Solar radiation heats Earth's surface unevenly (equator vs. poles, land vs. ocean), creating temperature gradients that drive atmospheric circulation, wind, and all weather patterns.",
            "feedback_incorrect": "Incorrect. All weather is ultimately driven by differential solar heating. The equator receives more solar energy than the poles, creating temperature gradients that produce wind, convection, and precipitation."
        },
        {
            "question": "A weather forecast for tomorrow is typically about 95% accurate, but a forecast for 10 days out is approximately 50% accurate. Which best explains this decrease in accuracy?",
            "choices": {
                "A": "Meteorologists spend less effort on long-range forecasts.",
                "B": "Small measurement errors in current conditions amplify exponentially over time in the chaotic atmospheric system.",
                "C": "Weather satellites can only observe conditions a few days in advance.",
                "D": "The atmosphere follows completely random patterns beyond three days."
            },
            "correct": "B",
            "feedback_correct": "Correct. The atmosphere is a chaotic system exhibiting sensitive dependence on initial conditions. Small measurement uncertainties grow exponentially, making forecasts progressively less reliable over time.",
            "feedback_incorrect": "Incorrect. The atmosphere is a deterministic but chaotic system. Tiny errors in measuring current conditions amplify over time (doubling roughly every 2-3 days), eventually making the forecast unreliable."
        },
        {
            "question": "For a thunderstorm to develop, which combination of atmospheric conditions is generally required?",
            "choices": {
                "A": "Cold, dry air at the surface with clear skies above.",
                "B": "Warm, moist air at the surface with cooler air above, creating atmospheric instability.",
                "C": "Uniform temperature throughout the atmosphere with moderate winds.",
                "D": "High atmospheric pressure with low humidity."
            },
            "correct": "B",
            "feedback_correct": "Correct. Thunderstorms require instability (warm surface air beneath cooler upper air), moisture (for precipitation and latent heat release), and a lifting mechanism to initiate convection.",
            "feedback_incorrect": "Incorrect. Thunderstorm development requires atmospheric instability: warm, moist air near the surface overlain by cooler air aloft. This temperature structure promotes rapid upward convection that fuels storm development."
        },
        {
            "question": "The 'butterfly effect' in the context of weather prediction refers to:",
            "choices": {
                "A": "The effect of butterfly migrations on weather patterns.",
                "B": "The sensitivity of weather systems to tiny changes in initial conditions, where small perturbations can lead to vastly different outcomes.",
                "C": "The pattern of butterfly-shaped cloud formations that signal approaching storms.",
                "D": "The way weather changes unpredictably from season to season."
            },
            "correct": "B",
            "feedback_correct": "Correct. The butterfly effect (sensitive dependence on initial conditions) means that tiny, unmeasurable differences in the atmosphere's starting state can produce completely different weather outcomes days later.",
            "feedback_incorrect": "Incorrect. The butterfly effect describes how infinitesimally small changes in initial atmospheric conditions can lead to dramatically different weather outcomes, placing a fundamental limit on forecast accuracy."
        },
        {
            "question": "What is the key difference between weather and climate prediction?",
            "choices": {
                "A": "There is no difference; both predict the same things over different timescales.",
                "B": "Weather predicts specific atmospheric conditions on a given day (chaotic), while climate predicts statistical averages over decades (driven by energy balance physics).",
                "C": "Climate prediction is more accurate day-to-day than weather prediction.",
                "D": "Weather prediction uses computers while climate prediction uses only historical records."
            },
            "correct": "B",
            "feedback_correct": "Correct. Weather is the specific atmospheric state on a specific day (chaotic, unpredictable beyond ~2 weeks). Climate is the statistical average of weather over decades (predictable through energy balance physics).",
            "feedback_incorrect": "Incorrect. Weather and climate are fundamentally different prediction problems. Weather is chaotic and unpredictable beyond about two weeks. Climate is a statistical average driven by well-understood energy balance, making it highly predictable."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the Butterfly Effect Test scenario, two model runs with Solar Radiation differing by only 0.1% produce nearly identical 3-day forecasts but completely different 10-day forecasts. What mathematical property of the atmosphere does this demonstrate?",
            "choices": {
                "A": "The atmosphere follows random, unpredictable behavior at all timescales.",
                "B": "Deterministic chaos, where the system follows precise physical laws but small initial differences grow exponentially, making long-range prediction impossible.",
                "C": "Measurement instruments are too imprecise for useful forecasting.",
                "D": "The model is flawed because a 0.1% change should not affect the forecast."
            },
            "correct": "B",
            "feedback_correct": "Correct. This demonstrates deterministic chaos: the system obeys exact physical laws (it is not random), but infinitesimal differences in starting conditions amplify exponentially, producing divergent outcomes after several days.",
            "feedback_incorrect": "Incorrect. The atmosphere is a deterministic chaotic system. It follows exact physical laws, so identical initial conditions always produce identical outcomes. But tiny differences in initial conditions grow exponentially, creating a fundamental prediction horizon."
        },
        {
            "question": "The model shows that Storm Probability increases when high Moisture Content coincides with strong Solar Radiation. A student asks why deserts have strong solar radiation but few thunderstorms. Which model component explains this?",
            "choices": {
                "A": "Wind Speed, because deserts have too much wind for storms to form.",
                "B": "Moisture Content, because storms require simultaneous presence of multiple ingredients, and deserts lack sufficient atmospheric moisture despite having strong solar heating.",
                "C": "Air Temperature, because deserts are too hot for storms.",
                "D": "Solar Radiation Input, which is actually weaker in deserts than other regions."
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that storm formation requires MULTIPLE ingredients simultaneously. Deserts have strong heating but lack moisture. Without sufficient moisture, atmospheric instability alone cannot produce storms.",
            "feedback_incorrect": "Incorrect. The model shows storms require multiple conditions converging. Deserts have strong solar heating but lack moisture. Missing any key ingredient (instability, moisture, lift) prevents storm formation."
        },
        {
            "question": "Based on the model's forecast accuracy decay curve (95% at 1 day, 80% at 5 days, 50% at 10 days), a technology company claims its new AI system will produce accurate 30-day forecasts. What does the model's chaos theory framework predict about this claim?",
            "choices": {
                "A": "AI could achieve this because it can process data faster than traditional models.",
                "B": "The claim violates the fundamental predictability limit of chaotic atmospheric systems. No technology can extend useful forecasts beyond approximately 2-3 weeks.",
                "C": "AI would only need slightly more data to achieve 30-day accuracy.",
                "D": "The model cannot evaluate this claim because it doesn't include AI."
            },
            "correct": "B",
            "feedback_correct": "Correct. The theoretical predictability limit for the atmosphere (~2-3 weeks) is a mathematical property of the chaotic equations, not a technology limitation. No computational advancement can overcome this fundamental boundary.",
            "feedback_incorrect": "Incorrect. Chaos theory sets a fundamental prediction horizon (~2-3 weeks) that is a property of the atmospheric equations themselves, not of the computing technology used. Better AI improves short-range forecasts but cannot extend the limit."
        },
        {
            "question": "The model demonstrates that all five atmospheric variables (solar radiation, temperature, moisture, wind, storm probability) interact with each other. Why does this interconnection make weather prediction particularly challenging?",
            "choices": {
                "A": "It means only one variable needs to be measured accurately for a good forecast.",
                "B": "Each variable's error feeds into every other variable's calculation, causing errors to compound and propagate through the entire system simultaneously.",
                "C": "The interactions cancel each other out, making the system simpler than it appears.",
                "D": "Only temperature and moisture interact; the other variables are independent."
            },
            "correct": "B",
            "feedback_correct": "Correct. In an interconnected system, measurement errors in ANY variable propagate to ALL other variables through their interactions. This error propagation compounds exponentially in a chaotic system.",
            "feedback_incorrect": "Incorrect. The model shows all variables are coupled. A temperature error affects wind calculations, which affect moisture transport, which affects storm probability. Errors in any variable cascade through the entire interconnected system."
        },
        {
            "question": "A school principal wants to know if it will rain during an outdoor event in 14 days. Based on the model's findings about forecast accuracy, which recommendation is most scientifically sound?",
            "choices": {
                "A": "Check the 14-day forecast now and plan accordingly.",
                "B": "14-day forecasts are unreliable. Plan for both scenarios now, and check 3-5 day forecasts closer to the event for a more accurate prediction.",
                "C": "Weather 14 days out is completely random, so there is no useful information available.",
                "D": "The model shows that 14-day rain predictions are 90% accurate, so trust the current forecast."
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows 14-day forecasts are near the predictability limit and barely better than climatological averages. The scientifically sound approach is flexible planning now with decision-making based on more accurate 3-5 day forecasts.",
            "feedback_incorrect": "Incorrect. At 14 days, forecast accuracy is near the theoretical limit and provides little useful specific information. The model supports flexible planning with final decisions based on 3-5 day forecasts, which are approximately 80-90% accurate."
        }
    ]
}

L08_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Radioactive decay is a process in which:",
            "choices": {
                "A": "A stable atom absorbs energy and becomes radioactive.",
                "B": "An unstable atomic nucleus spontaneously transforms into a more stable configuration by emitting radiation.",
                "C": "Chemical bonds between atoms break apart due to high temperatures.",
                "D": "Electrons escape from an atom, leaving it electrically charged."
            },
            "correct": "B",
            "feedback_correct": "Correct. Radioactive decay is a nuclear process where unstable nuclei spontaneously emit particles or energy to become more stable. This occurs at a constant rate independent of external conditions.",
            "feedback_incorrect": "Incorrect. Radioactive decay is a spontaneous nuclear transformation. Unstable nuclei emit radiation (alpha, beta, or gamma) as they convert to more stable configurations at a constant, predictable rate."
        },
        {
            "question": "A radioactive isotope has a half-life of 1,000 years. If a sample begins with 800 atoms of the parent isotope, approximately how many parent atoms remain after 3,000 years?",
            "choices": {
                "A": "400 atoms",
                "B": "200 atoms",
                "C": "100 atoms",
                "D": "0 atoms"
            },
            "correct": "C",
            "feedback_correct": "Correct. After 3 half-lives (3,000/1,000 = 3): 800 -> 400 -> 200 -> 100 atoms. Each half-life reduces the remaining parent isotope by exactly half.",
            "feedback_incorrect": "Incorrect. Three half-lives pass in 3,000 years. Each halves the remaining amount: 800/2 = 400, 400/2 = 200, 200/2 = 100 atoms remaining."
        },
        {
            "question": "Why is carbon-14 dating NOT used to determine the age of the Earth?",
            "choices": {
                "A": "Carbon-14 is too abundant in old rocks to measure accurately.",
                "B": "Carbon-14 has a half-life of only 5,730 years, so virtually none remains in samples older than about 50,000 years.",
                "C": "Carbon-14 dating only works on metals, not rocks.",
                "D": "The Earth does not contain any carbon-14."
            },
            "correct": "B",
            "feedback_correct": "Correct. With a half-life of 5,730 years, carbon-14 becomes undetectable after approximately 10 half-lives (~50,000 years). Earth's 4.5-billion-year age requires isotopes with much longer half-lives like uranium-238.",
            "feedback_incorrect": "Incorrect. Carbon-14's short half-life (5,730 years) means it decays to undetectable levels within ~50,000 years. Dating the 4.5-billion-year-old Earth requires isotopes with half-lives of billions of years."
        },
        {
            "question": "A geologist finds a rock where the ratio of parent radioactive isotope to daughter product is 1:3 (25% parent, 75% daughter). How many half-lives have elapsed since the rock formed?",
            "choices": {
                "A": "1 half-life",
                "B": "2 half-lives",
                "C": "3 half-lives",
                "D": "4 half-lives"
            },
            "correct": "B",
            "feedback_correct": "Correct. Starting at 100% parent: after 1 half-life = 50% parent; after 2 half-lives = 25% parent (with 75% daughter). The 25:75 ratio indicates exactly 2 half-lives have passed.",
            "feedback_incorrect": "Incorrect. Track the decay: 100% -> 50% (1 half-life) -> 25% (2 half-lives). A ratio of 25% parent to 75% daughter means 2 half-lives have elapsed."
        },
        {
            "question": "What makes radioactive decay rates reliable for dating geological samples?",
            "choices": {
                "A": "They can be adjusted in the laboratory to speed up the dating process.",
                "B": "They are constant and unaffected by temperature, pressure, or any other environmental conditions.",
                "C": "They change predictably with temperature, allowing corrections.",
                "D": "They are the same for all elements, simplifying calculations."
            },
            "correct": "B",
            "feedback_correct": "Correct. Radioactive decay rates are determined by nuclear physics (the strong force). No known physical or chemical process can alter them, making them the most reliable natural chronometers available.",
            "feedback_incorrect": "Incorrect. Decay rates are fixed by fundamental nuclear forces and are completely independent of external conditions. This constancy is what makes them perfectly reliable clocks for geological dating."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the model's Multiple Methods scenario, three independent isotope systems (U-Pb, K-Ar, Rb-Sr) applied to the same rock all yield the same age within measurement uncertainty. Why is this convergence considered strong scientific evidence?",
            "choices": {
                "A": "Because all three methods use the same mathematical equation.",
                "B": "Because the probability of three independent methods, using different elements and decay mechanisms, accidentally producing the same wrong answer is vanishingly small.",
                "C": "Because averaging three measurements always produces a more accurate result.",
                "D": "Because the methods were calibrated against each other before being applied."
            },
            "correct": "B",
            "feedback_correct": "Correct. Independent convergence is among the strongest forms of scientific evidence. Each system involves different elements, different decay physics, and different half-lives. Agreement among independent methods rules out systematic error.",
            "feedback_incorrect": "Incorrect. The power of convergence comes from independence. Three different isotope systems with different elements, different decay mechanisms, and different half-lives all agreeing on the same age makes coincidental error essentially impossible."
        },
        {
            "question": "The model shows that only 6.25% of a parent isotope remains in an ancient rock. A student calculates this represents 4 half-lives. Using uranium-238 (half-life 4.47 billion years), the calculated age would be 17.9 billion years. The student recognizes this exceeds the age of the universe. What does the model suggest went wrong?",
            "choices": {
                "A": "The half-life of uranium-238 is incorrect.",
                "B": "The wrong isotope system was selected for this sample's age range, or the sample was contaminated with additional daughter product.",
                "C": "The model cannot handle ages greater than 4.5 billion years.",
                "D": "Four half-lives is the maximum measurable by any dating method."
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that selecting the appropriate isotope system for the expected age range is critical. An impossibly old result signals either wrong isotope system choice or open-system behavior (contamination).",
            "feedback_incorrect": "Incorrect. The model teaches that impossible ages indicate either an inappropriate isotope system for the sample's true age or violation of the closed-system assumption (parent loss or daughter gain from external sources)."
        },
        {
            "question": "Based on the model, a rock sample contains 50% parent and 50% daughter isotope using potassium-40 (half-life = 1.25 billion years). What is the calculated age of this rock?",
            "choices": {
                "A": "625 million years",
                "B": "1.25 billion years",
                "C": "2.5 billion years",
                "D": "4.5 billion years"
            },
            "correct": "B",
            "feedback_correct": "Correct. A 50:50 parent:daughter ratio means exactly 1 half-life has elapsed. For K-40 with a half-life of 1.25 billion years, the rock is 1.25 billion years old.",
            "feedback_incorrect": "Incorrect. When 50% of the parent remains, exactly 1 half-life has passed. For potassium-40: 1 half-life = 1.25 billion years. The rock formed 1.25 billion years ago."
        },
        {
            "question": "The model demonstrates that Earth's age (4.567 billion years) was determined using meteorites rather than Earth rocks. Which model concept best explains why Earth's oldest rocks (~4.0 billion years) do not directly record Earth's formation age?",
            "choices": {
                "A": "Earth's oldest rocks are too small to contain measurable radioactive isotopes.",
                "B": "Earth's geological processes (plate tectonics, weathering, metamorphism) recycled the original crust, resetting the radiometric clocks of surface rocks.",
                "C": "Radioactive decay did not begin until 500 million years after Earth formed.",
                "D": "Earth rocks contain different isotopes than meteorites."
            },
            "correct": "B",
            "feedback_correct": "Correct. Earth's dynamic geology continuously recycles crustal material through plate tectonics, metamorphism, and weathering. These processes reset radiometric clocks, erasing the record of Earth's original formation age from surface rocks.",
            "feedback_incorrect": "Incorrect. Earth's active geology recycles its crust. Metamorphism, melting, and tectonic processes reset radiometric clocks in rocks. Meteorites, which have been geologically inactive since formation, preserve the original Solar System age."
        },
        {
            "question": "A student argues that radiometric dating is unreliable because scientists cannot verify ages independently. The model provides multiple forms of counter-evidence. Which is the STRONGEST counter-argument?",
            "choices": {
                "A": "Scientists have carefully calibrated their instruments.",
                "B": "Multiple independent isotope systems using different elements and decay mechanisms consistently produce the same ages for the same rocks, and the natural reactor at Oklo, Gabon confirms decay rates were identical 2 billion years ago.",
                "C": "The ages match what geologists expected based on rock appearance.",
                "D": "Only one isotope system is actually needed for reliable dating."
            },
            "correct": "B",
            "feedback_correct": "Correct. The strongest evidence combines multiple independent convergence (different isotope systems agreeing) with the Oklo natural reactor, which provides a direct physical verification that decay rates 2 billion years ago were identical to today.",
            "feedback_incorrect": "Incorrect. The strongest evidence is independent convergence from multiple isotope systems plus physical verification from the Oklo natural reactor. Together, these provide overwhelming, independently verifiable evidence of reliability."
        }
    ]
}

L09_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A magnet attracts a steel paperclip from a distance without touching it. What mediates this force between the two objects?",
            "choices": {
                "A": "Air molecules carry the magnetic force between the objects.",
                "B": "A magnetic field, which is a physical entity that fills the space around the magnet.",
                "C": "Static electricity builds up on both objects, creating attraction.",
                "D": "Gravity pulls the lighter object toward the heavier magnet."
            },
            "correct": "B",
            "feedback_correct": "Correct. Magnetic force is mediated by the magnetic field, a real physical entity that exists in the space around every magnet. It carries energy and exerts forces on ferromagnetic materials within it.",
            "feedback_incorrect": "Incorrect. Magnetic attraction is mediated by the magnetic field, an invisible but real physical entity that fills space around magnets. It is not carried by air, electricity, or gravity."
        },
        {
            "question": "A student places a magnet on one side of a wooden table and a paperclip on the other side directly below. The paperclip sticks to the underside of the table. What does this demonstrate about magnetic fields?",
            "choices": {
                "A": "The magnet's field is strong enough to physically penetrate and weaken the wood.",
                "B": "Wood is a magnetic material that transmits the force.",
                "C": "Magnetic fields pass through non-ferromagnetic materials like wood with virtually no reduction.",
                "D": "The magnet creates a gravitational effect that attracts the paperclip through the table."
            },
            "correct": "C",
            "feedback_correct": "Correct. Non-ferromagnetic materials (wood, plastic, glass, air) do not interact with magnetic fields. The field passes through them as if they were not present, maintaining its ability to exert force on ferromagnetic objects.",
            "feedback_incorrect": "Incorrect. Magnetic fields pass through non-ferromagnetic materials (wood, plastic, glass) with negligible interaction. The field does not need to 'penetrate' the material; the material is effectively invisible to it."
        },
        {
            "question": "When you move a magnet closer to a piece of iron, the attractive force increases dramatically. Which mathematical relationship best describes how magnetic force changes with distance?",
            "choices": {
                "A": "Force decreases linearly with distance.",
                "B": "Force decreases with the square of distance (inverse square law).",
                "C": "Force decreases with the cube of distance for magnetic dipoles (even steeper than inverse square).",
                "D": "Force remains constant regardless of distance until contact is lost."
            },
            "correct": "C",
            "feedback_correct": "Correct. For magnetic dipoles (bar magnets), force decreases approximately as 1/r^3. Doubling the distance reduces force to about 1/8, explaining the dramatic 'grab' effect when magnets are very close.",
            "feedback_incorrect": "Incorrect. Magnetic dipole force follows an inverse cube relationship (F proportional to 1/r^3), which is even steeper than gravity's inverse square law. This is why magnetic force seems to suddenly 'turn on' at close range."
        },
        {
            "question": "Which of the following materials would MOST effectively block a magnetic field from reaching an object on the other side?",
            "choices": {
                "A": "A thick sheet of glass.",
                "B": "A sheet of aluminum foil.",
                "C": "A thick steel plate.",
                "D": "A sheet of plastic."
            },
            "correct": "C",
            "feedback_correct": "Correct. Steel is ferromagnetic, meaning its atomic magnetic domains interact with and redirect the external field. A thick steel plate absorbs the field, preventing it from reaching objects behind it.",
            "feedback_incorrect": "Incorrect. Only ferromagnetic materials (iron, steel, nickel, cobalt) interact with and redirect magnetic fields. Glass, aluminum, and plastic are non-ferromagnetic and allow fields to pass through freely."
        },
        {
            "question": "When a magnet accelerates a paperclip toward it, the paperclip gains kinetic energy. Where does this energy come from?",
            "choices": {
                "A": "The magnet converts its own mass into energy.",
                "B": "Energy stored in the magnetic field converts to kinetic energy of the moving paperclip.",
                "C": "The paperclip's thermal energy converts to kinetic energy.",
                "D": "Energy is created from nothing by the magnetic force."
            },
            "correct": "B",
            "feedback_correct": "Correct. The magnetic field contains real, measurable energy. When a ferromagnetic object moves to a lower-energy field configuration, the difference in field energy converts to the object's kinetic energy.",
            "feedback_incorrect": "Incorrect. Magnetic fields store real energy (proportional to B^2). When a paperclip moves closer to a magnet, the system moves to a lower-energy configuration, and the released field energy becomes the paperclip's kinetic energy."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that a 3 mm plastic phone case reduces magnetic force by only 15-25%, while a 3 mm iron plate reduces it dramatically. Which model principle explains this difference?",
            "choices": {
                "A": "Plastic is thinner than iron at the molecular level.",
                "B": "The force reduction through plastic is due only to the additional 3 mm of distance, while iron actively interacts with and redirects the field, shielding the target.",
                "C": "Iron is heavier than plastic, so it blocks more of the magnetic field through gravity.",
                "D": "The model shows that all materials reduce magnetic force equally at the same thickness."
            },
            "correct": "B",
            "feedback_correct": "Correct. The model distinguishes between 'transparent' materials (plastic adds only distance) and 'opaque' materials (iron's ferromagnetic domains interact with and redirect the field). The mechanism of force reduction is fundamentally different.",
            "feedback_incorrect": "Incorrect. The model reveals two distinct mechanisms: plastic is magnetically transparent (force reduction comes only from added distance), while iron is ferromagnetic and actively redirects the field away from the target."
        },
        {
            "question": "The Distance Falloff scenario shows that force drops from 5 N at 1 mm to 0.005 N at 10 mm. Which statement best interprets this model result?",
            "choices": {
                "A": "The magnet is defective because it loses its magnetism quickly.",
                "B": "The inverse cube relationship means a 10x increase in distance produces approximately a 1,000x decrease in force, creating a sharp apparent boundary between 'magnetic' and 'non-magnetic' zones.",
                "C": "Air resistance reduces the magnetic force at greater distances.",
                "D": "The model is unrealistic because real magnets maintain constant force."
            },
            "correct": "B",
            "feedback_correct": "Correct. The inverse cube law (F proportional to 1/r^3) produces the dramatic result: 10^3 = 1,000-fold decrease. This explains the common perception that magnets have a sharp 'range' when the falloff is actually continuous but extremely steep.",
            "feedback_incorrect": "Incorrect. The model correctly demonstrates the inverse cube relationship. A 10x distance increase produces a 1,000x force decrease (10^3). The magnet is not weakening; the field follows this steep mathematical decay at all distances."
        },
        {
            "question": "The model includes an Energy Stored in Field component. A student asks whether this energy is 'real' or just mathematical. Which model evidence best demonstrates that field energy is physically real?",
            "choices": {
                "A": "The field lines are visible when iron filings are sprinkled around a magnet.",
                "B": "When a paperclip accelerates toward a magnet, the kinetic energy it gains exactly equals the decrease in field energy, demonstrating energy conservation.",
                "C": "The magnet maintains its field for a very long time without external energy.",
                "D": "The field equation (B^2/2mu_0) produces a number with energy units."
            },
            "correct": "B",
            "feedback_correct": "Correct. Energy conservation provides the strongest evidence: the paperclip's kinetic energy gain exactly matches the field's energy decrease. This measurable, quantitative energy exchange proves the field energy is physically real, not just mathematical.",
            "feedback_incorrect": "Incorrect. The most compelling evidence is energy conservation: the kinetic energy gained by the moving paperclip precisely equals the energy lost from the magnetic field. This quantitative energy exchange proves field energy is physically real."
        },
        {
            "question": "An engineer is designing a magnetic phone mount. The model shows that shear force (sliding) requires much less force to overcome than pull force (pulling straight apart). How should this inform the mount design?",
            "choices": {
                "A": "Design the mount so the phone must be pulled straight off, providing maximum security.",
                "B": "Design the mount so the phone slides off sideways for easy one-handed removal, while the strong normal (pull) force provides secure holding during driving.",
                "C": "Use the weakest possible magnets so the phone can be removed easily.",
                "D": "This information is irrelevant to mount design."
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that shear and pull forces differ significantly for the same magnet. Engineering the removal direction (sliding rather than pulling) allows strong holding force while maintaining easy detachment.",
            "feedback_incorrect": "Incorrect. The model's distinction between shear and pull forces is a critical engineering insight. Strong normal force provides secure holding during bumps and turns, while lower shear force allows easy one-handed sliding removal."
        },
        {
            "question": "Based on the model, a student claims that magnets will eventually 'run out' of energy because they keep attracting things. Which model concept directly refutes this claim?",
            "choices": {
                "A": "The model shows that magnets slowly weaken with each use.",
                "B": "The magnetic field is a property of the material's electron spin structure, not a consumable energy source. After each attraction event, the system can be reset by separating the objects, which restores the field energy.",
                "C": "Magnets absorb energy from sunlight to recharge their fields.",
                "D": "The model does not address whether magnets run out of energy."
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that magnetic fields arise from the quantum mechanical spin of electrons, an intrinsic material property. When objects are separated, energy is put back into the field. The field is a property, not a fuel.",
            "feedback_incorrect": "Incorrect. Magnetism is an intrinsic property of the material's atomic structure (electron spin), not a stored fuel. Pulling objects apart restores the field energy. Under normal conditions, permanent magnets lose less than 1% of field strength per century."
        }
    ]
}

L10_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Which equation correctly represents the overall reaction of photosynthesis?",
            "choices": {
                "A": "C6H12O6 + 6O2 -> 6CO2 + 6H2O + energy",
                "B": "6CO2 + 6H2O + light energy -> C6H12O6 + 6O2",
                "C": "6O2 + 6H2O -> 6CO2 + C6H12O6 + light",
                "D": "C6H12O6 -> 6CO2 + 6H2O + light energy"
            },
            "correct": "B",
            "feedback_correct": "Correct. Photosynthesis uses light energy to convert carbon dioxide and water into glucose and oxygen. This reaction stores solar energy in the chemical bonds of glucose.",
            "feedback_incorrect": "Incorrect. Photosynthesis converts CO2 and H2O into glucose and O2 using light energy. Choice A describes cellular respiration, the reverse process."
        },
        {
            "question": "Cellular respiration is the process by which organisms:",
            "choices": {
                "A": "Absorb oxygen through their skin to cool their body temperature.",
                "B": "Break down glucose using oxygen to release stored chemical energy as ATP.",
                "C": "Convert sunlight into chemical energy stored in glucose.",
                "D": "Eliminate carbon dioxide waste produced by photosynthesis."
            },
            "correct": "B",
            "feedback_correct": "Correct. Cellular respiration breaks the bonds of glucose molecules using oxygen, releasing the stored energy as ATP (the cell's energy currency) with CO2 and H2O as byproducts.",
            "feedback_incorrect": "Incorrect. Cellular respiration is the metabolic process that breaks down glucose (C6H12O6 + 6O2 -> 6CO2 + 6H2O + ATP), releasing energy stored in chemical bonds for cellular work."
        },
        {
            "question": "As organisms increase in size, their surface-area-to-volume ratio:",
            "choices": {
                "A": "Increases, allowing larger organisms to capture more light per unit volume.",
                "B": "Stays the same regardless of size.",
                "C": "Decreases, because volume grows faster (r^3) than surface area (r^2).",
                "D": "Depends only on the organism's shape, not its size."
            },
            "correct": "C",
            "feedback_correct": "Correct. Surface area scales with the square of linear dimensions (r^2) while volume scales with the cube (r^3). Larger organisms have proportionally less surface area relative to their volume.",
            "feedback_incorrect": "Incorrect. As organisms grow, volume increases faster than surface area (cube vs. square relationship). This decreasing surface-area-to-volume ratio has profound implications for energy capture and heat regulation."
        },
        {
            "question": "Photosynthesis converts approximately what percentage of incoming solar energy into chemical energy stored in glucose?",
            "choices": {
                "A": "About 50%, making it highly efficient.",
                "B": "About 25%, comparable to solar panels.",
                "C": "About 1-2% under field conditions.",
                "D": "About 90%, since plants have evolved for billions of years."
            },
            "correct": "C",
            "feedback_correct": "Correct. Despite 3 billion years of evolution, photosynthesis achieves only about 1-2% energy conversion efficiency under field conditions. This is due to losses at multiple steps in the light and dark reactions.",
            "feedback_incorrect": "Incorrect. Natural photosynthesis is surprisingly inefficient, converting only about 1-2% of incoming solar energy to glucose. Losses occur at multiple steps: wrong wavelengths, reflection, heat loss, and photorespiration."
        },
        {
            "question": "What is the relationship between photosynthesis and cellular respiration in the global carbon cycle?",
            "choices": {
                "A": "They are unrelated processes that happen to involve similar molecules.",
                "B": "They are complementary reactions that cycle carbon between the atmosphere (CO2) and living organisms (organic molecules).",
                "C": "Photosynthesis creates carbon while cellular respiration destroys it.",
                "D": "Both processes release CO2 into the atmosphere."
            },
            "correct": "B",
            "feedback_correct": "Correct. Photosynthesis removes CO2 from the atmosphere and stores carbon in glucose. Cellular respiration breaks down glucose and returns CO2 to the atmosphere. Together, they cycle carbon between living and non-living systems.",
            "feedback_incorrect": "Incorrect. Photosynthesis and cellular respiration are mirror-image reactions that together drive the global carbon cycle. Photosynthesis fixes atmospheric CO2 into organic molecules; respiration returns that carbon to the atmosphere."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that a photosynthetic human with 1.7 m^2 of surface area would produce approximately 60-100 kcal/day, while needing 2,000 kcal/day. What is the fundamental constraint the model identifies as making photosynthetic humans impossible?",
            "choices": {
                "A": "Human skin cannot contain chlorophyll molecules.",
                "B": "The surface-area-to-volume ratio: a human's energy needs (proportional to volume) vastly exceed light-capture capacity (proportional to surface area).",
                "C": "Sunlight does not contain enough energy to power any organism.",
                "D": "Cellular respiration prevents photosynthesis from occurring in the same organism."
            },
            "correct": "B",
            "feedback_correct": "Correct. The model identifies the surface-area-to-volume ratio as the fundamental constraint. A human's metabolic demands scale with body volume, but light capture scales with surface area. The geometry makes photosynthetic humans mathematically impossible.",
            "feedback_incorrect": "Incorrect. The model reveals that the fundamental constraint is geometric: energy needs scale with body volume while light capture scales with surface area. As body size increases, the energy deficit grows unavoidably."
        },
        {
            "question": "In the Scaling Problem scenario, the model shows that single-celled organisms can fully meet energy needs through photosynthesis, but organisms at human scale cannot. At what approximate body size does the model predict photosynthesis becomes insufficient?",
            "choices": {
                "A": "At approximately 1 meter in length.",
                "B": "At approximately 10 cm in length.",
                "C": "At approximately millimeter scale for organisms with human-like metabolic rates.",
                "D": "Photosynthesis is sufficient at all body sizes if enough chlorophyll is present."
            },
            "correct": "C",
            "feedback_correct": "Correct. The model shows that for organisms with high metabolic rates like animals, the crossover point where respiration exceeds photosynthetic capacity occurs at roughly millimeter scale. Plants succeed because they are metabolically slow.",
            "feedback_incorrect": "Incorrect. The model demonstrates that the crossover depends on BOTH size and metabolic rate. For organisms with human-like metabolism, photosynthesis becomes insufficient at approximately millimeter scale."
        },
        {
            "question": "The model demonstrates that Sunlight Intensity has a positive effect on Glucose Production Rate, but only up to a saturation point. What biological mechanism explains this saturation?",
            "choices": {
                "A": "Excess light damages chlorophyll, reducing photosynthetic capacity.",
                "B": "The photosynthetic reaction centers have a maximum processing rate. Beyond saturation, additional light photons cannot be utilized because the enzyme machinery is already operating at full capacity.",
                "C": "Plants close their stomata in bright light, preventing CO2 entry.",
                "D": "High light intensity converts glucose back into CO2 through reverse photosynthesis."
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reflects that photosynthetic enzymes (particularly in the Calvin cycle) have maximum reaction rates. Beyond light saturation, the bottleneck shifts from light availability to enzyme processing capacity.",
            "feedback_incorrect": "Incorrect. Light saturation occurs because photosynthetic enzymes have a maximum processing rate. Once the reaction centers are operating at full capacity, additional photons cannot increase glucose production regardless of intensity."
        },
        {
            "question": "A student examines the model and observes that photosynthesis (6CO2 + 6H2O -> C6H12O6 + 6O2) and cellular respiration (C6H12O6 + 6O2 -> 6CO2 + 6H2O) are chemically opposite. Based on the model, what role does this complementary relationship play in Earth's systems?",
            "choices": {
                "A": "The reactions cancel each other out and have no net effect on Earth's atmosphere.",
                "B": "Together they cycle carbon between the atmosphere and biosphere, maintaining atmospheric CO2 balance when not disrupted by external inputs like fossil fuel burning.",
                "C": "They demonstrate that photosynthesis is a more important process than respiration.",
                "D": "The complementary relationship means organisms that photosynthesize do not need to respire."
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows these mirror reactions form the biological carbon cycle. Photosynthesis fixes atmospheric CO2; respiration returns it. This cycle has maintained CO2 balance for hundreds of millions of years until fossil fuel burning disrupted it.",
            "feedback_incorrect": "Incorrect. The model demonstrates that photosynthesis and respiration together form a carbon cycle between atmosphere and biosphere. This cycle maintained atmospheric CO2 balance for hundreds of millions of years before human fossil fuel use disrupted it."
        },
        {
            "question": "Based on model evidence, a biotech company proposes engineering algae that achieve 10% photosynthetic efficiency (compared to the natural 1-2%) for biofuel production. Which model insight best evaluates whether this is scientifically plausible?",
            "choices": {
                "A": "The model shows 10% is impossible because photosynthesis has already been evolutionarily optimized.",
                "B": "The model identifies specific energy loss steps (wrong wavelengths, heat loss, photorespiration) that could theoretically be improved. While the theoretical maximum is about 11%, achieving 10% in practice would require overcoming multiple biological constraints.",
                "C": "The model proves that any efficiency above 2% violates the laws of thermodynamics.",
                "D": "The model does not provide information relevant to bioengineering efficiency."
            },
            "correct": "B",
            "feedback_correct": "Correct. The model identifies where energy is lost at each step. Since the theoretical maximum (~11%) exceeds the proposed 10%, the goal is not thermodynamically impossible but would require addressing multiple specific bottlenecks identified by the model.",
            "feedback_incorrect": "Incorrect. The model maps specific energy losses at each step of photosynthesis. Since the theoretical maximum (~11%) allows room for improvement beyond natural 1-2%, the 10% goal is thermodynamically possible but biologically challenging."
        }
    ]
}

ALL_QUESTIONS = {
    "G10L1-L01": L01_QUESTIONS,
    "G10L1-L02": L02_QUESTIONS,
    "G10L1-L03": L03_QUESTIONS,
    "G10L1-L04": L04_QUESTIONS,
    "G10L1-L05": L05_QUESTIONS,
    "G10L1-L06": L06_QUESTIONS,
    "G10L1-L07": L07_QUESTIONS,
    "G10L1-L08": L08_QUESTIONS,
    "G10L1-L09": L09_QUESTIONS,
    "G10L1-L10": L10_QUESTIONS,
}
