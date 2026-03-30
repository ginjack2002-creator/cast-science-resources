#!/usr/bin/env python3
"""Multiple choice pre/post assessment questions for Grade 8 ModelIt! Lessons"""

# =============================================================================
# G08-L01: Superbugs: Evolution You Can See
# NGSS: MS-LS4-4, MS-LS4-6
# =============================================================================
L01_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is the primary function of antibiotics?",
            "choices": {
                "A": "To kill or stop the growth of bacteria",
                "B": "To boost the human immune system",
                "C": "To kill viruses that cause the common cold",
                "D": "To prevent all types of infections permanently"
            },
            "correct": "A",
            "feedback_correct": "Correct! Antibiotics specifically target bacteria. They do not work against viruses or permanently prevent infections.",
            "feedback_incorrect": "Antibiotics are medicines designed to kill or inhibit the growth of bacteria. They do not affect viruses, boost the immune system directly, or provide permanent protection."
        },
        {
            "question": "Where do new traits in a population originally come from?",
            "choices": {
                "A": "Organisms choose to develop traits they need to survive",
                "B": "Random changes (mutations) in an organism's DNA",
                "C": "The environment directly changes the organism's genes",
                "D": "Traits are created by natural selection itself"
            },
            "correct": "B",
            "feedback_correct": "Correct! Mutations are random changes in DNA that introduce new traits into a population. Natural selection then acts on those traits.",
            "feedback_incorrect": "New traits arise from random mutations in DNA. Organisms cannot choose traits, the environment does not directly rewrite genes, and natural selection acts on existing variation rather than creating it."
        },
        {
            "question": "In the process of natural selection, which organisms are most likely to survive and reproduce?",
            "choices": {
                "A": "The largest and strongest organisms",
                "B": "Organisms with traits that are best suited to their current environment",
                "C": "The oldest organisms in the population",
                "D": "Organisms that can change their traits when the environment changes"
            },
            "correct": "B",
            "feedback_correct": "Correct! Natural selection favors organisms with traits that provide an advantage in their specific environment, regardless of size, age, or intentional adaptation.",
            "feedback_incorrect": "'Survival of the fittest' does not mean strongest or largest. It means organisms whose traits happen to be best suited to the current environment are more likely to survive and pass on those traits."
        },
        {
            "question": "A doctor prescribes antibiotics for a patient with a bacterial infection. The patient feels better after 3 days but has a 10-day prescription. What should the patient do?",
            "choices": {
                "A": "Stop taking the antibiotics since the infection is gone",
                "B": "Take the remaining pills all at once to finish faster",
                "C": "Complete the full 10-day course as prescribed",
                "D": "Save the remaining pills for the next time they get sick"
            },
            "correct": "C",
            "feedback_correct": "Correct! Completing the full course ensures that even partially resistant bacteria are killed. Stopping early can leave the most resistant bacteria alive to reproduce.",
            "feedback_incorrect": "Patients should always complete the full antibiotic course. Stopping early, taking pills all at once, or saving them can all contribute to antibiotic resistance by allowing resistant bacteria to survive."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In a population of bacteria exposed to antibiotics, resistant bacteria survive while non-resistant bacteria die. Which statement best explains why the resistant bacteria survived?",
            "choices": {
                "A": "The antibiotics caused the bacteria to mutate into resistant forms",
                "B": "The resistant bacteria chose to activate their defense genes",
                "C": "Random mutations that occurred before antibiotic exposure happened to provide resistance",
                "D": "The resistant bacteria learned to fight the antibiotic through repeated exposure"
            },
            "correct": "C",
            "feedback_correct": "Correct! Resistance genes arise from random mutations that exist before antibiotic exposure. Antibiotics do not cause resistance; they select for bacteria that already carry resistance genes.",
            "feedback_incorrect": "Antibiotics do not cause mutations or teach bacteria to resist. Resistance genes arise from random mutations that happened before any antibiotic was present. The antibiotic acts as a selective pressure, favoring bacteria that already have resistance."
        },
        {
            "question": "A model shows that when antibiotic use is set to 100%, resistant bacteria reach 90% of the population in 10 generations. When antibiotic use is set to 30%, resistant bacteria reach only 25% in the same time. What does this evidence support?",
            "choices": {
                "A": "Lower antibiotic use prevents all mutations from occurring",
                "B": "Higher antibiotic use creates a stronger selective pressure, accelerating resistance evolution",
                "C": "Resistant bacteria only appear when antibiotic use is above 50%",
                "D": "Antibiotics at 30% are too weak to kill any bacteria"
            },
            "correct": "B",
            "feedback_correct": "Correct! Higher antibiotic use creates stronger selective pressure. More non-resistant bacteria are killed, giving resistant bacteria a larger reproductive advantage and accelerating population change.",
            "feedback_incorrect": "Reducing antibiotic use does not stop mutations. Resistant bacteria can appear at any antibiotic level. The key insight is that higher use creates stronger selective pressure, so the resistant population grows faster."
        },
        {
            "question": "A hospital notices that MRSA infections have increased by 300% over 10 years. Using your understanding of natural selection, which factor most directly drove this increase?",
            "choices": {
                "A": "Bacteria deliberately evolved to resist methicillin",
                "B": "Repeated antibiotic use selected for bacteria carrying pre-existing resistance genes over many generations",
                "C": "The hospital became dirtier over time, creating new resistant bacteria",
                "D": "Patients' immune systems became weaker, allowing bacteria to mutate faster"
            },
            "correct": "B",
            "feedback_correct": "Correct! Repeated antibiotic use acts as a sustained selective pressure. Over many generations, bacteria with pre-existing resistance genes outcompete susceptible bacteria, increasing the resistant population.",
            "feedback_incorrect": "Bacteria do not deliberately evolve. Cleanliness and immune strength affect infection rates but do not drive resistance evolution. The mechanism is natural selection: repeated antibiotic use selects for bacteria that already carry resistance genes."
        },
        {
            "question": "Your model includes Mutation Rate and Antibiotic Use as external components and Resistant Bacteria and Treatment Effectiveness as internal components. If you wanted to slow the rise of resistant bacteria, which strategy would your model support?",
            "choices": {
                "A": "Increase mutation rate to create bacteria that are too mutated to survive",
                "B": "Use antibiotics at maximum levels to kill all bacteria before they can reproduce",
                "C": "Reduce antibiotic use to decrease the selective pressure favoring resistant bacteria",
                "D": "Eliminate all bacteria from hospitals using stronger chemicals"
            },
            "correct": "C",
            "feedback_correct": "Correct! Reducing antibiotic use decreases selective pressure. Without strong selection against non-resistant bacteria, resistant bacteria do not gain as large a reproductive advantage, slowing the spread of resistance.",
            "feedback_incorrect": "Increasing mutation rate would create more variation, not fewer survivors. Maximum antibiotic use increases selective pressure. The model shows that reducing antibiotic use (lowering selective pressure) is the most effective strategy to slow resistance evolution."
        }
    ]
}

# =============================================================================
# G08-L02: The Reef Is Bleaching
# NGSS: MS-LS2-1, MS-LS2-4
# =============================================================================
L02_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Coral reefs are sometimes called 'rainforests of the sea.' What does this comparison most likely refer to?",
            "choices": {
                "A": "Both receive a lot of rainfall",
                "B": "Both support an extremely high diversity of species",
                "C": "Both are located in tropical land environments",
                "D": "Both are made entirely of plants"
            },
            "correct": "B",
            "feedback_correct": "Correct! Coral reefs, like tropical rainforests, support an extraordinary diversity of life. Reefs host roughly 25% of all marine species despite covering less than 1% of the ocean floor.",
            "feedback_incorrect": "The comparison refers to biodiversity. Coral reefs support roughly 25% of all marine species, making them one of the most species-rich ecosystems on Earth, similar to rainforests on land."
        },
        {
            "question": "Which of the following best describes coral?",
            "choices": {
                "A": "A type of colorful underwater rock",
                "B": "A plant that grows on the ocean floor",
                "C": "A colony of tiny animals called polyps",
                "D": "A type of seaweed with a hard outer shell"
            },
            "correct": "C",
            "feedback_correct": "Correct! Coral is an animal. Each coral colony is made up of thousands of tiny polyps that are related to jellyfish and sea anemones.",
            "feedback_incorrect": "Despite looking like rocks or plants, coral is actually an animal. Coral colonies are made up of thousands of tiny polyps, which are invertebrate animals related to jellyfish."
        },
        {
            "question": "What is symbiosis?",
            "choices": {
                "A": "When one organism hunts and eats another",
                "B": "A close, long-term relationship between two different species",
                "C": "When organisms compete for the same resources",
                "D": "The process of organisms adapting to a new environment"
            },
            "correct": "B",
            "feedback_correct": "Correct! Symbiosis describes a close and long-term biological interaction between two different species, which can be mutualistic, parasitic, or commensal.",
            "feedback_incorrect": "Symbiosis is not predation or competition. It specifically refers to a close, long-term relationship between two different species that live in close association."
        },
        {
            "question": "How might rising ocean temperatures affect organisms that live in the sea?",
            "choices": {
                "A": "Warmer water always helps marine organisms grow faster",
                "B": "Temperature changes have no effect on marine organisms because water stays the same temperature",
                "C": "Organisms adapted to specific temperature ranges may become stressed if temperatures change beyond their tolerance",
                "D": "Only land organisms are affected by temperature changes"
            },
            "correct": "C",
            "feedback_correct": "Correct! Marine organisms are adapted to specific temperature ranges. When temperatures exceed their tolerance, they can become stressed, which may disrupt feeding, reproduction, or survival.",
            "feedback_incorrect": "Marine organisms are highly sensitive to temperature. Many are adapted to narrow ranges, and even small increases (1-2 degrees Celsius) can cause significant stress, disrupting biological processes."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In your model, when Ocean Temperature was increased +3 degrees Celsius, Zooxanthellae Population dropped first, and then Coral Health declined. What type of ecological relationship does this sequence demonstrate?",
            "choices": {
                "A": "Competition between coral and zooxanthellae for resources",
                "B": "A trophic cascade where disrupting one level causes chain effects through the system",
                "C": "Predation where rising temperatures help coral consume zooxanthellae",
                "D": "Parasitism where zooxanthellae harm coral when temperatures rise"
            },
            "correct": "B",
            "feedback_correct": "Correct! This is a trophic cascade. The temperature disrupts the coral-zooxanthellae symbiosis first (zooxanthellae expelled), which then cascades to affect coral health because coral depends on zooxanthellae for up to 90% of its energy.",
            "feedback_incorrect": "The sequence shows a cascade effect. Temperature stress does not make coral eat zooxanthellae or turn the relationship parasitic. It disrupts the mutualistic symbiosis, and because coral depends on zooxanthellae for energy, the coral then declines."
        },
        {
            "question": "Your model showed that the 'Double Threat' scenario (increased temperature AND acidity) caused far worse coral decline than temperature alone. Which explanation best accounts for this?",
            "choices": {
                "A": "Acidic water directly kills zooxanthellae, so both factors target the same component",
                "B": "Temperature causes coral to expel zooxanthellae (losing its food source), while acidity weakens the coral skeleton (losing structural integrity), attacking the system through two different pathways",
                "C": "Acidity and temperature cancel each other out, but the combination creates a new chemical that kills coral",
                "D": "The model was inaccurate because in reality these factors do not interact"
            },
            "correct": "B",
            "feedback_correct": "Correct! The two stressors attack the coral system through different pathways: temperature disrupts the energy supply (zooxanthellae), while acidity weakens the physical structure (skeleton). Together, recovery becomes nearly impossible.",
            "feedback_incorrect": "The double threat is worse because the two factors target different vulnerabilities. Temperature causes bleaching (energy loss), while acidification weakens the calcium carbonate skeleton. These simultaneous attacks through different pathways make recovery far more difficult."
        },
        {
            "question": "A marine biologist observes that a reef bleached during a heat wave but recovered six months later when temperatures returned to normal. Which component of the model best explains the recovery?",
            "choices": {
                "A": "The coral grew a new skeleton resistant to temperature changes",
                "B": "New coral polyps migrated from cooler waters to replace the dead ones",
                "C": "Zooxanthellae were able to recolonize the coral tissue once temperatures dropped back within tolerance",
                "D": "The ocean became more acidic, which helped coral rebuild"
            },
            "correct": "C",
            "feedback_correct": "Correct! Bleached coral is stressed and starving but not necessarily dead. If conditions return to normal quickly enough, zooxanthellae can recolonize the coral tissue, restoring the energy supply and allowing recovery.",
            "feedback_incorrect": "Bleaching occurs when coral expels its zooxanthellae under heat stress. The coral is still alive during early bleaching. Recovery happens when temperatures drop and zooxanthellae return to the coral tissue, restoring the mutualistic energy supply."
        },
        {
            "question": "Based on your model, which intervention would most effectively protect coral reefs in the long term?",
            "choices": {
                "A": "Painting bleached coral with colorful dye to attract fish back to the reef",
                "B": "Reducing CO2 emissions, which would slow both ocean warming and acidification",
                "C": "Moving all fish to aquariums so they are not affected by reef decline",
                "D": "Adding more salt to the ocean to increase its buffering capacity"
            },
            "correct": "B",
            "feedback_correct": "Correct! Since CO2 drives both ocean warming (through the greenhouse effect) and ocean acidification (CO2 dissolving in seawater), reducing emissions addresses the root causes of both external stressors in the model.",
            "feedback_incorrect": "The model shows that temperature and acidity are the external drivers of reef decline, and both are linked to CO2. Reducing emissions is the only option that addresses the root cause of both stressors simultaneously."
        }
    ]
}

# =============================================================================
# G08-L03: Your Phone's Dirty Secret
# NGSS: MS-ESS3-3, MS-ESS3-4
# =============================================================================
L03_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What are rare earth minerals used for?",
            "choices": {
                "A": "Only for making jewelry and decorative items",
                "B": "Essential components in modern electronics like smartphones, computers, and renewable energy technology",
                "C": "Only for building roads and bridges",
                "D": "They have no practical uses and are only collected by scientists"
            },
            "correct": "B",
            "feedback_correct": "Correct! Rare earth minerals are critical components in smartphones, computers, electric vehicles, wind turbines, and many other modern technologies.",
            "feedback_incorrect": "Rare earth minerals are essential for modern electronics and clean energy technology. A single smartphone contains over 30 different minerals that enable its screen, battery, speakers, and processing power."
        },
        {
            "question": "What happens to most electronic devices when people are done using them?",
            "choices": {
                "A": "Nearly all electronics are recycled and their materials are fully recovered",
                "B": "Most are sent back to the manufacturer for reuse",
                "C": "A large percentage end up in landfills or are exported to developing countries",
                "D": "Electronic materials naturally decompose within a few months"
            },
            "correct": "C",
            "feedback_correct": "Correct! Only about 20% of e-waste is properly recycled. The rest ends up in landfills or is shipped to developing countries where it is often processed in unsafe conditions.",
            "feedback_incorrect": "Unfortunately, the majority of e-waste is not properly recycled. Only about 20% is recovered through formal recycling programs. The rest goes to landfills or is exported to developing countries."
        },
        {
            "question": "What does 'resource extraction' mean?",
            "choices": {
                "A": "Recycling old materials into new products",
                "B": "Removing raw materials like minerals and metals from the Earth",
                "C": "Growing crops for food production",
                "D": "Filtering pollutants from water"
            },
            "correct": "B",
            "feedback_correct": "Correct! Resource extraction refers to the process of removing natural resources such as minerals, metals, oil, or timber from the Earth for human use.",
            "feedback_incorrect": "Resource extraction specifically means removing raw materials from the Earth. Mining for minerals, drilling for oil, and logging forests are all forms of resource extraction."
        },
        {
            "question": "How does increased human population affect natural resource use?",
            "choices": {
                "A": "Population growth has no relationship to resource consumption",
                "B": "Larger populations always find ways to use fewer resources through innovation",
                "C": "More people generally means higher demand for resources, increasing pressure on Earth's systems",
                "D": "Natural resources are unlimited, so population size does not matter"
            },
            "correct": "C",
            "feedback_correct": "Correct! As population grows, demand for food, water, energy, and materials increases, putting greater pressure on Earth's systems and natural resources.",
            "feedback_incorrect": "There is a direct relationship between population growth and resource demand. More people require more food, water, energy, and materials, which increases the rate of resource extraction and environmental impact."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In your model, Consumer Demand is an external component that drives Mining Intensity. When Consumer Demand was set to maximum, Environmental Damage increased significantly. What does this relationship demonstrate about Earth's systems?",
            "choices": {
                "A": "Technology development always leads to environmental improvement",
                "B": "Human consumption patterns have direct, measurable impacts on Earth's systems through resource extraction",
                "C": "Mining has no significant environmental effects if done properly",
                "D": "Environmental damage only occurs in developing countries"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model demonstrates a clear cause-and-effect chain: human consumption drives demand, which drives extraction, which causes environmental damage. This shows how per-capita consumption directly impacts Earth's systems.",
            "feedback_incorrect": "The model clearly shows that increased consumer demand leads to increased mining, which increases environmental damage. This demonstrates the direct link between human consumption patterns and impacts on Earth's systems."
        },
        {
            "question": "Your model showed that reducing Consumer Demand by 50% had a larger positive environmental impact than recycling alone. What is the best scientific explanation for this?",
            "choices": {
                "A": "Recycling is not worth doing because it has no benefits",
                "B": "Reducing demand prevents the environmental damage from mining and manufacturing that recycling cannot undo",
                "C": "Consumers cannot actually reduce their demand for electronics",
                "D": "Recycling creates more pollution than manufacturing new devices"
            },
            "correct": "B",
            "feedback_correct": "Correct! Reducing demand prevents environmental damage at the source. Recycling recovers some materials but cannot undo the land destruction, water pollution, and carbon emissions that already occurred during extraction and manufacturing.",
            "feedback_incorrect": "Recycling is valuable, but it addresses the problem after damage has already been done. Reducing demand is more effective because it prevents the mining, manufacturing, and transportation impacts from occurring in the first place."
        },
        {
            "question": "A student argues that smartphone production has no significant environmental impact because phones are small. Using evidence from the model, which response best refutes this claim?",
            "choices": {
                "A": "The student is correct because small devices require very few materials",
                "B": "Each phone requires over 30 different minerals from mines worldwide, and with billions of phones produced annually, the cumulative extraction and e-waste create massive environmental impact",
                "C": "Phone production only affects the air, not the land or water",
                "D": "Environmental impact only comes from the packaging, not the phone itself"
            },
            "correct": "B",
            "feedback_correct": "Correct! While each phone is small, it contains over 30 minerals that must be mined. When multiplied by billions of devices, the cumulative impact on land, water, and atmosphere is substantial. The model shows this scaling effect.",
            "feedback_incorrect": "A single phone may be small, but it contains over 30 different mined minerals. Scale matters: billions of phones are produced each year, creating massive cumulative mining, manufacturing, and e-waste impacts across multiple Earth systems."
        },
        {
            "question": "Based on your model's results, which approach would create the most sustainable lifecycle for electronics?",
            "choices": {
                "A": "Design devices to be replaced every six months with faster upgrades",
                "B": "Ship all e-waste to space to avoid landfill problems",
                "C": "A circular economy: extend device lifespan, design for easy recycling, and recover materials from old devices to reduce new mining",
                "D": "Stop using all electronic devices entirely"
            },
            "correct": "C",
            "feedback_correct": "Correct! A circular economy addresses all components in the model: reducing demand (extending lifespan) decreases mining intensity, designing for recycling reduces e-waste, and material recovery closes the loop.",
            "feedback_incorrect": "The model shows that the most effective approach combines reduced demand with material recovery. A circular economy addresses the problem at every stage of the lifecycle rather than focusing on just one part."
        }
    ]
}

# =============================================================================
# G08-L04: Why Hurricanes Are Getting Angrier
# NGSS: MS-ESS2-5, MS-ESS2-6
# =============================================================================
L04_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What provides the primary energy source for a hurricane?",
            "choices": {
                "A": "Cold air masses from the Arctic",
                "B": "Warm ocean water that evaporates into the atmosphere",
                "C": "Lightning strikes that generate heat",
                "D": "Wind from nearby weather systems"
            },
            "correct": "B",
            "feedback_correct": "Correct! Hurricanes are heat engines powered by the evaporation of warm ocean water. The warmer the water, the more energy is available for the storm.",
            "feedback_incorrect": "Hurricanes get their energy from warm ocean water. When water evaporates from the warm ocean surface, it releases heat energy into the atmosphere, which fuels the storm's winds and circulation."
        },
        {
            "question": "What is convection?",
            "choices": {
                "A": "The transfer of heat through solid materials by direct contact",
                "B": "The rising of warm air and sinking of cool air that creates circulation patterns",
                "C": "The reflection of sunlight off the ocean surface",
                "D": "The spinning motion of the Earth on its axis"
            },
            "correct": "B",
            "feedback_correct": "Correct! Convection is the circular motion that occurs when warm, less dense air rises and cool, denser air sinks to replace it, creating circulation patterns.",
            "feedback_incorrect": "Convection refers to heat transfer through fluid movement. Warm air rises because it is less dense, and cooler air sinks to take its place. This creates circular patterns that drive weather systems."
        },
        {
            "question": "What is a storm surge?",
            "choices": {
                "A": "The increase in wind speed during a thunderstorm",
                "B": "A sudden burst of lightning during a storm",
                "C": "An abnormal rise in sea level pushed onshore by a storm's winds and low pressure",
                "D": "The calm area at the center of a hurricane"
            },
            "correct": "C",
            "feedback_correct": "Correct! Storm surge is a rise in ocean water level caused by a storm's strong winds and low atmospheric pressure pushing water toward and onto the shore.",
            "feedback_incorrect": "Storm surge is the abnormal rise in sea level during a storm. It occurs when powerful winds and low air pressure push ocean water onto the coast, causing flooding that is often the most deadly part of a hurricane."
        },
        {
            "question": "How has the average global temperature of the ocean changed over the past several decades?",
            "choices": {
                "A": "Ocean temperatures have remained exactly the same",
                "B": "Ocean temperatures have been steadily decreasing",
                "C": "Ocean temperatures have been gradually increasing",
                "D": "Ocean temperatures only change during El Nino years"
            },
            "correct": "C",
            "feedback_correct": "Correct! Global ocean temperatures have been gradually rising. The ocean absorbs about 90% of the excess heat from global warming, leading to warmer sea surface temperatures.",
            "feedback_incorrect": "Data from NOAA and other agencies show that global ocean temperatures have been gradually increasing. The ocean absorbs approximately 90% of excess heat trapped by greenhouse gases."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In your model, when Sea Surface Temperature was increased from 80 degrees F to 90 degrees F, Hurricane Wind Speed increased dramatically. This relationship shows that hurricanes function as:",
            "choices": {
                "A": "Cold air converters that turn cool ocean water into wind",
                "B": "Heat engines that convert thermal energy from warm water into kinetic energy of wind",
                "C": "Electrical generators that create lightning from ocean salt",
                "D": "Random weather events with no predictable relationship to ocean temperature"
            },
            "correct": "B",
            "feedback_correct": "Correct! Hurricanes function as heat engines. They convert the thermal energy stored in warm ocean water into the kinetic energy of powerful winds through evaporation and convection.",
            "feedback_incorrect": "The model shows a clear cause-and-effect relationship: warmer water provides more thermal energy, which is converted into stronger winds. Hurricanes are essentially heat engines that run on warm ocean water."
        },
        {
            "question": "Your model demonstrated 'rapid intensification' when Sea Surface Temperature was locked at 90 degrees F. A hurricane's wind speed increased by 45 mph in 24 hours. What does this suggest about the relationship between ocean temperature and hurricane risk?",
            "choices": {
                "A": "Rapid intensification is impossible and the model must be wrong",
                "B": "A small increase in ocean temperature produces only a small, proportional increase in wind speed",
                "C": "Warmer ocean temperatures can fuel disproportionately large and sudden increases in storm intensity, making hurricanes less predictable and more dangerous",
                "D": "Rapid intensification only happens when two hurricanes collide"
            },
            "correct": "C",
            "feedback_correct": "Correct! The model shows a non-linear relationship. Small temperature increases can trigger rapid intensification, where storms strengthen disproportionately fast. This makes forecasting more difficult and communities more vulnerable.",
            "feedback_incorrect": "Rapid intensification is a real and increasingly common phenomenon. The model demonstrates that the relationship between ocean temperature and storm intensity is not simply proportional. Slightly warmer water can cause dramatic, sudden jumps in hurricane strength."
        },
        {
            "question": "In the 'Cool Water Encounter' scenario, the hurricane weakened rapidly when sea surface temperature dropped from 90 degrees F to 75 degrees F. Which model component explains this?",
            "choices": {
                "A": "Cool water added mass to the hurricane, making it too heavy to maintain wind speed",
                "B": "The hurricane lost its energy source because cooler water provides less evaporation and less thermal energy for convection",
                "C": "Cool water created ice that blocked the hurricane's rotation",
                "D": "The atmospheric moisture increased, making the storm too wet to continue"
            },
            "correct": "B",
            "feedback_correct": "Correct! When a hurricane moves over cooler water, evaporation decreases and less thermal energy enters the system. Without its fuel supply, the convection cycle weakens and wind speeds drop.",
            "feedback_incorrect": "The model shows that hurricanes depend on warm ocean water as their energy source. Cooler water means less evaporation, less heat released into the atmosphere, and therefore less energy to sustain the storm's convection and winds."
        },
        {
            "question": "Based on your model, if average sea surface temperatures continue to rise over the next 50 years, which prediction is best supported by the evidence?",
            "choices": {
                "A": "Hurricanes will become weaker because warmer air is less dense",
                "B": "Hurricane frequency will decrease because warm water prevents storms from forming",
                "C": "Hurricanes will have access to more energy, increasing the likelihood of stronger storms with higher storm surges",
                "D": "Ocean temperature has no effect on long-term hurricane patterns"
            },
            "correct": "C",
            "feedback_correct": "Correct! The model shows that warmer water provides more energy for hurricanes. Continued warming means more fuel available for storms, supporting predictions of more intense hurricanes with higher storm surges.",
            "feedback_incorrect": "The model provides clear evidence that warmer water increases hurricane intensity and storm surge height. Continued ocean warming would mean more thermal energy available to fuel stronger storms."
        }
    ]
}

# =============================================================================
# G08-L05: The Roller Coaster Equation
# NGSS: MS-PS3-1, MS-PS3-2
# =============================================================================
L05_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A ball is held at the top of a ramp. What type of energy does it have because of its position?",
            "choices": {
                "A": "Kinetic energy",
                "B": "Chemical energy",
                "C": "Potential energy",
                "D": "Thermal energy"
            },
            "correct": "C",
            "feedback_correct": "Correct! An object held at a height has gravitational potential energy because of its position. This energy is stored and can be converted to motion.",
            "feedback_incorrect": "An object at a height has potential energy, which is energy stored due to its position in a gravitational field. Kinetic energy is the energy of motion, which it would gain as it moves down the ramp."
        },
        {
            "question": "When a moving car comes to a stop by braking, what happens to its kinetic energy?",
            "choices": {
                "A": "The kinetic energy is destroyed",
                "B": "The kinetic energy is transformed into thermal energy (heat) in the brakes",
                "C": "The kinetic energy disappears because the car stopped moving",
                "D": "The kinetic energy stays the same but is hidden inside the car"
            },
            "correct": "B",
            "feedback_correct": "Correct! Energy cannot be destroyed. When the car brakes, kinetic energy is transformed into thermal energy through friction between the brake pads and rotors.",
            "feedback_incorrect": "Energy cannot be created or destroyed (conservation of energy). When a car brakes, its kinetic energy does not disappear. It is transformed into thermal energy (heat) through friction in the braking system."
        },
        {
            "question": "A roller coaster reaches its fastest speed at which point on the track?",
            "choices": {
                "A": "At the very top of the highest hill",
                "B": "At the lowest point after the biggest drop",
                "C": "Halfway up the second hill",
                "D": "At the start of the ride before any hills"
            },
            "correct": "B",
            "feedback_correct": "Correct! As the coaster descends, potential energy converts to kinetic energy. The lowest point after the biggest drop is where the most potential energy has been converted to speed.",
            "feedback_incorrect": "The coaster is fastest at the bottom of the biggest drop. This is where the maximum amount of potential energy (from height) has been converted into kinetic energy (speed)."
        },
        {
            "question": "If you double the height of a ramp, what happens to the speed of a ball at the bottom?",
            "choices": {
                "A": "The speed exactly doubles",
                "B": "The speed increases but does not quite double",
                "C": "The speed stays the same regardless of height",
                "D": "The speed decreases because the ball has farther to travel"
            },
            "correct": "B",
            "feedback_correct": "Correct! Speed increases with height, but the relationship involves a square root. Doubling the height increases speed by a factor of about 1.4 (the square root of 2), not 2.",
            "feedback_incorrect": "Speed at the bottom increases with ramp height, but not proportionally. The relationship involves a square root: doubling the height increases speed by approximately 1.4 times, not 2 times."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "Your model showed that at the top of the first hill, potential energy is at maximum and kinetic energy is near zero. At the bottom, potential energy is near zero and kinetic energy is at maximum. The total energy remained constant throughout. This demonstrates:",
            "choices": {
                "A": "Energy was created at the bottom of the hill",
                "B": "The law of conservation of energy: energy transforms between forms but the total stays the same",
                "C": "Potential energy is more powerful than kinetic energy",
                "D": "The roller coaster used an engine at the bottom to speed up"
            },
            "correct": "B",
            "feedback_correct": "Correct! The constant total energy demonstrates the law of conservation of energy. Energy was not created or destroyed. It transformed from potential (height) to kinetic (speed) and back again.",
            "feedback_incorrect": "The model demonstrates conservation of energy. No energy was created or destroyed. Potential energy transformed into kinetic energy during the descent and back into potential energy during the ascent, with the total remaining constant."
        },
        {
            "question": "In the 'Heavy Coaster' scenario, doubling the mass of the coaster doubled both the potential and kinetic energy at every point. However, the speed at the bottom was the same as the lighter coaster. What explains this?",
            "choices": {
                "A": "The model was inaccurate because heavier objects should move faster",
                "B": "Kinetic energy depends on both mass and speed (KE = 1/2 mv squared), so when mass doubles, the same speed still means double the kinetic energy",
                "C": "Heavier objects always move at the same speed as lighter objects",
                "D": "The extra mass created friction that slowed the coaster to match the lighter one"
            },
            "correct": "B",
            "feedback_correct": "Correct! Since KE = 1/2 mv squared, doubling mass doubles kinetic energy even at the same speed. The height determines the speed, regardless of mass, because both potential and kinetic energy scale equally with mass.",
            "feedback_incorrect": "The key is the mathematical relationship KE = 1/2 mv squared. When mass doubles, kinetic energy doubles, but speed stays the same because potential energy also doubled. Mass cancels out when converting between PE and KE, so speed at the bottom depends only on height."
        },
        {
            "question": "Using your model, a coaster starts at 30 meters high and must complete a loop that is 20 meters tall. At the top of the loop, the coaster still has kinetic energy. Why is this possible?",
            "choices": {
                "A": "The loop generated extra energy that did not exist at the start",
                "B": "The coaster started at 30m, so after climbing 20m it still has 10m worth of potential energy that remains as kinetic energy (speed)",
                "C": "The coaster accelerated inside the loop using centrifugal force",
                "D": "Potential energy is always greater than kinetic energy in loops"
            },
            "correct": "B",
            "feedback_correct": "Correct! Starting at 30m and climbing to 20m means 10m worth of potential energy was converted to kinetic energy at the loop top. The coaster still has speed because it has not used all its initial potential energy.",
            "feedback_incorrect": "Conservation of energy explains this. The coaster started with 30m worth of potential energy. At the top of the 20m loop, it used 20m of PE to climb, leaving 10m worth of energy as kinetic energy (motion). This is why the first hill must always be the tallest."
        },
        {
            "question": "A theme park engineer wants the second hill to be taller than the first. Based on your model, why is this impossible without adding an engine?",
            "choices": {
                "A": "The coaster would be moving too fast to climb a taller hill",
                "B": "Conservation of energy means the coaster cannot have more potential energy at any point than it started with, and some energy is always lost to friction",
                "C": "Taller hills are structurally unsafe for roller coasters",
                "D": "Gravity only works on the first hill of a roller coaster"
            },
            "correct": "B",
            "feedback_correct": "Correct! Without an external energy source, the coaster cannot gain more energy than it started with. A taller second hill would require more potential energy than the total energy available, violating conservation of energy.",
            "feedback_incorrect": "The law of conservation of energy sets this limit. The coaster's total energy is fixed by the height of the first hill. A second hill taller than the first would require more potential energy than the coaster possesses, which is impossible without adding energy from an engine."
        }
    ]
}

# =============================================================================
# G08-L06: The Concussion Problem
# NGSS: MS-PS2-1, MS-PS2-2
# =============================================================================
L06_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "According to Newton's First Law, what happens to an object in motion when no external force acts on it?",
            "choices": {
                "A": "It gradually slows down and stops",
                "B": "It continues moving at the same speed in the same direction",
                "C": "It speeds up over time",
                "D": "It changes direction randomly"
            },
            "correct": "B",
            "feedback_correct": "Correct! Newton's First Law (inertia) states that an object in motion stays in motion at constant speed and direction unless acted upon by an unbalanced force.",
            "feedback_incorrect": "Newton's First Law states that an object in motion remains in motion at constant velocity unless an external force acts on it. This property is called inertia."
        },
        {
            "question": "When you push against a wall, the wall pushes back against you with an equal force. This is an example of:",
            "choices": {
                "A": "Newton's First Law (inertia)",
                "B": "Newton's Second Law (F=ma)",
                "C": "Newton's Third Law (action-reaction)",
                "D": "The law of gravity"
            },
            "correct": "C",
            "feedback_correct": "Correct! Newton's Third Law states that for every action force, there is an equal and opposite reaction force. The wall pushes back with the same force you apply.",
            "feedback_incorrect": "This is Newton's Third Law: for every action, there is an equal and opposite reaction. When you push the wall, it exerts an equal force back on you in the opposite direction."
        },
        {
            "question": "What is a concussion?",
            "choices": {
                "A": "A bruise on the outside of the skull",
                "B": "A brain injury caused by the brain moving inside the skull during a sudden impact",
                "C": "A cracked skull bone",
                "D": "Temporary dizziness that has no lasting effects"
            },
            "correct": "B",
            "feedback_correct": "Correct! A concussion occurs when a sudden impact causes the brain to move inside the skull, potentially damaging brain cells and disrupting normal brain function.",
            "feedback_incorrect": "A concussion is a traumatic brain injury that occurs when the brain shifts inside the skull during a sudden deceleration or impact. It is not just a skull bruise or crack, and it can have lasting effects."
        },
        {
            "question": "If you double the speed of a moving object, how does the force of impact change when it suddenly stops?",
            "choices": {
                "A": "The force stays the same regardless of speed",
                "B": "The force doubles",
                "C": "The force more than doubles",
                "D": "The force decreases because faster objects stop more smoothly"
            },
            "correct": "C",
            "feedback_correct": "Correct! Force of impact increases with speed, but because kinetic energy depends on speed squared, doubling speed more than doubles the impact force.",
            "feedback_incorrect": "When speed doubles, the impact force more than doubles. This is because kinetic energy depends on speed squared (KE = 1/2 mv squared). Doubling speed quadruples the kinetic energy that must be absorbed during the stop."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "Your model showed that even with a helmet, Brain Acceleration remained significant during a 20 mph collision. Using Newton's Laws, which explanation best accounts for why helmets cannot eliminate concussions?",
            "choices": {
                "A": "Helmets are not strong enough to withstand high-speed impacts",
                "B": "The brain floats in fluid inside the skull and continues moving (inertia) when the skull suddenly decelerates, so no external helmet can prevent the brain from moving inside the skull",
                "C": "Helmets make players overconfident, causing them to hit harder",
                "D": "Concussions are caused by neck injuries, not brain movement"
            },
            "correct": "B",
            "feedback_correct": "Correct! Newton's First Law explains that the brain, floating in cerebrospinal fluid, keeps moving when the skull stops suddenly. No helmet can stop the brain from decelerating inside the skull because the helmet only protects the outside.",
            "feedback_incorrect": "The fundamental physics problem is inertia. The brain floats inside the skull in fluid. During a collision, the skull stops, but the brain continues moving (Newton's First Law), striking the inside of the skull. Helmets protect the skull but cannot prevent this internal brain movement."
        },
        {
            "question": "Your model showed that helmets reduce Impact Force by extending the time of collision. This demonstrates the concept of impulse. If a helmet extends the collision time from 5 milliseconds to 50 milliseconds, what happens to the peak force?",
            "choices": {
                "A": "Peak force increases tenfold because the collision lasts longer",
                "B": "Peak force is reduced to approximately one-tenth because the same momentum change is spread over 10 times longer",
                "C": "Peak force stays the same because momentum is conserved",
                "D": "Peak force is eliminated entirely by extending the time"
            },
            "correct": "B",
            "feedback_correct": "Correct! Impulse = Force x Time. Since the total momentum change stays the same, spreading it over 10 times longer reduces the peak force to about one-tenth. This is exactly how helmet padding works.",
            "feedback_incorrect": "Impulse = Force x Time, and momentum change is fixed. By extending the collision time by a factor of 10, the peak force must decrease by the same factor to maintain the same impulse. This is the physics principle behind all impact protection."
        },
        {
            "question": "In the model, when Player Mass was doubled at 15 mph, Impact Force increased significantly. When Collision Speed was doubled at normal mass, Impact Force increased even more. What does this comparison reveal?",
            "choices": {
                "A": "Mass and speed affect impact force equally",
                "B": "Speed has a greater effect on impact force than mass because kinetic energy depends on speed squared (v squared) but only linearly on mass",
                "C": "Mass has no effect on impact force; only speed matters",
                "D": "The model was inaccurate because mass should not affect collisions"
            },
            "correct": "B",
            "feedback_correct": "Correct! KE = 1/2 mv squared means doubling speed quadruples kinetic energy, while doubling mass only doubles it. Speed has a disproportionately larger effect on collision force.",
            "feedback_incorrect": "Both mass and speed affect impact force, but not equally. Because kinetic energy is proportional to speed squared (v squared) but only proportional to mass (m), doubling speed has a much larger effect than doubling mass."
        },
        {
            "question": "Based on your model results, a sports equipment company wants to design a helmet that better reduces concussion risk. Which design principle is best supported by the model evidence?",
            "choices": {
                "A": "Make the helmet as hard and rigid as possible to block all force",
                "B": "Use materials that compress slowly to maximize the time of deceleration, reducing peak force on the brain",
                "C": "Make the helmet as light as possible to reduce the mass involved in the collision",
                "D": "Add a sharp outer edge to deflect opponents during contact"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model shows that extending collision time reduces peak force (impulse principle). Materials that compress slowly and progressively absorb energy over a longer period, reducing the peak deceleration the brain experiences.",
            "feedback_incorrect": "A rigid helmet would transfer force more quickly, not less. The model supports using materials that compress progressively, extending the deceleration time and thereby reducing peak force through the impulse principle."
        }
    ]
}

# =============================================================================
# G08-L07: How LeBron Turns Food Into Dunks
# NGSS: MS-LS1-5, MS-LS1-7
# =============================================================================
L07_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is the primary source of energy for the human body?",
            "choices": {
                "A": "Water",
                "B": "Oxygen",
                "C": "Food (glucose and other nutrients)",
                "D": "Sunlight"
            },
            "correct": "C",
            "feedback_correct": "Correct! Food, particularly glucose from carbohydrates, provides the chemical energy that cells break down to power all body functions.",
            "feedback_incorrect": "While water, oxygen, and sunlight are important for life, food is the primary energy source. Glucose from digested food is the main fuel that cells use to produce energy."
        },
        {
            "question": "Why do you breathe harder during exercise?",
            "choices": {
                "A": "Your lungs need to cool down from the heat of exercise",
                "B": "Your muscles need more oxygen to produce energy for increased activity",
                "C": "Breathing harder pushes more blood to your muscles",
                "D": "Exercise makes your lungs bigger so they need more air"
            },
            "correct": "B",
            "feedback_correct": "Correct! During exercise, your muscles demand more energy. Producing that energy requires more oxygen, so your breathing rate increases to deliver it.",
            "feedback_incorrect": "Your muscles need oxygen to break down glucose and produce energy (ATP). During exercise, energy demand increases dramatically, so your body breathes faster to deliver more oxygen to working muscles."
        },
        {
            "question": "What happens to the food you eat after it is digested?",
            "choices": {
                "A": "It disappears completely and is used up",
                "B": "It is broken down into smaller molecules that are absorbed into the bloodstream",
                "C": "It stays in your stomach until you need energy",
                "D": "It is converted directly into muscle tissue"
            },
            "correct": "B",
            "feedback_correct": "Correct! Digestion breaks food into small molecules like glucose, amino acids, and fatty acids that are absorbed into the bloodstream and delivered to cells throughout the body.",
            "feedback_incorrect": "During digestion, food is broken down into small molecules (like glucose) that pass into the bloodstream. These molecules are then transported to cells where they are used for energy or building materials."
        },
        {
            "question": "What is ATP?",
            "choices": {
                "A": "A type of muscle fiber that contracts during exercise",
                "B": "A protein that builds new cells",
                "C": "A molecule that stores and releases energy for cell activities",
                "D": "A hormone that regulates body temperature"
            },
            "correct": "C",
            "feedback_correct": "Correct! ATP (adenosine triphosphate) is the 'energy currency' of cells. It stores chemical energy that is released when cells need power for activities like muscle contraction.",
            "feedback_incorrect": "ATP (adenosine triphosphate) is a molecule that serves as the universal energy currency of cells. It is produced during cellular respiration and releases energy when cells need to perform work."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In your model, when Food Intake (Glucose) was set to zero, ATP Production dropped to near zero and Athletic Output collapsed. This demonstrates that:",
            "choices": {
                "A": "Oxygen alone is sufficient to power muscle contraction",
                "B": "Glucose is a required reactant in cellular respiration; without it, cells cannot produce ATP energy",
                "C": "Athletes do not actually need food to perform, they just need rest",
                "D": "ATP can be produced from water when glucose is unavailable"
            },
            "correct": "B",
            "feedback_correct": "Correct! The equation for cellular respiration (Glucose + Oxygen -> CO2 + Water + ATP) shows that glucose is a required reactant. Without glucose, the reaction cannot proceed and no ATP is produced.",
            "feedback_incorrect": "Cellular respiration requires both glucose and oxygen as reactants. Without glucose, the reaction cannot occur, and cells cannot produce the ATP needed to power muscle contraction and all other cellular activities."
        },
        {
            "question": "Your model showed that during 'Maximum Effort,' both Food Intake and Oxygen Supply needed to be high for peak Athletic Output. If oxygen supply is limited (like exercising at high altitude), what does the model predict will happen?",
            "choices": {
                "A": "ATP production increases because cells work harder to compensate",
                "B": "ATP production decreases because oxygen is a required reactant in aerobic cellular respiration, limiting energy production",
                "C": "Athletic output stays the same because food provides enough energy on its own",
                "D": "The body switches to using carbon dioxide instead of oxygen"
            },
            "correct": "B",
            "feedback_correct": "Correct! Oxygen is a required reactant in aerobic cellular respiration. When oxygen is limited, cells cannot fully break down glucose, reducing ATP production and therefore athletic performance.",
            "feedback_incorrect": "The model clearly shows that both glucose and oxygen are needed for maximum ATP production. Limited oxygen means cells switch to anaerobic respiration, which produces far less ATP and generates lactic acid, reducing performance."
        },
        {
            "question": "The chemical equation for cellular respiration is: Glucose + Oxygen -> Carbon Dioxide + Water + ATP (energy). A student claims that food 'gives you energy.' Using the model, which is a more scientifically accurate statement?",
            "choices": {
                "A": "Food creates new energy that did not exist before you ate it",
                "B": "Food molecules are rearranged through chemical reactions, and the energy stored in glucose bonds is transferred to ATP molecules",
                "C": "Food is directly burned in your stomach to produce heat energy",
                "D": "Food energy comes from the oxygen you breathe, not the food itself"
            },
            "correct": "B",
            "feedback_correct": "Correct! Energy is not created from food. The chemical energy stored in glucose bonds is released through cellular respiration and transferred to ATP. The atoms are rearranged into new molecules (CO2 and H2O).",
            "feedback_incorrect": "Food does not create energy or burn in the stomach. During cellular respiration, the chemical bonds in glucose are broken and atoms are rearranged into CO2 and H2O. The energy from those bonds is transferred to ATP molecules."
        },
        {
            "question": "An athlete eats a large meal and then immediately tries to run a race but performs poorly. Using your model, which explanation best accounts for this?",
            "choices": {
                "A": "The food was too heavy and weighed the athlete down physically",
                "B": "Digestion takes time to break food into glucose; the glucose was not yet available for cellular respiration in the muscles",
                "C": "Eating food removes oxygen from the blood, leaving less for the muscles",
                "D": "The model does not account for meal timing"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model shows that Food Intake (Glucose) is the input. Digestion must first convert food into glucose and deliver it via the bloodstream. This takes time, so eating immediately before activity means glucose is not yet available to muscles.",
            "feedback_incorrect": "The model uses glucose as the food input, but food must first be digested into glucose before it can enter cellular respiration. Digestion and absorption take time, so a meal eaten immediately before exercise cannot yet supply glucose to working muscles."
        }
    ]
}

# =============================================================================
# G08-L08: Why Do You Look Like That?
# NGSS: MS-LS3-1, MS-LS3-2
# =============================================================================
L08_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Humans have 46 chromosomes. How many come from each parent?",
            "choices": {
                "A": "46 from the mother and 46 from the father",
                "B": "23 from each parent",
                "C": "All 46 from the mother; the father contributes none",
                "D": "It varies randomly from person to person"
            },
            "correct": "B",
            "feedback_correct": "Correct! Humans inherit 23 chromosomes from each parent, for a total of 46. This is why you share traits with both parents but are not identical to either.",
            "feedback_incorrect": "During sexual reproduction, each parent contributes 23 chromosomes through their reproductive cells (egg and sperm), resulting in offspring with 46 chromosomes total."
        },
        {
            "question": "What is a gene?",
            "choices": {
                "A": "A type of clothing brand",
                "B": "A segment of DNA that contains instructions for a specific protein or trait",
                "C": "A complete chromosome that determines all traits at once",
                "D": "A chemical that only controls hair and eye color"
            },
            "correct": "B",
            "feedback_correct": "Correct! A gene is a segment of DNA on a chromosome that provides instructions for making a specific protein, which in turn influences a trait.",
            "feedback_incorrect": "A gene is a specific segment of DNA located on a chromosome. It contains the instructions for making a particular protein, which contributes to an organism's traits."
        },
        {
            "question": "Two brown-eyed parents have a child with blue eyes. How is this possible?",
            "choices": {
                "A": "It is impossible; brown-eyed parents can only have brown-eyed children",
                "B": "The child's eye color was determined by environmental factors, not genes",
                "C": "Both parents may carry a hidden (recessive) blue eye gene that they each passed to the child",
                "D": "The child mutated spontaneously to develop blue eyes"
            },
            "correct": "C",
            "feedback_correct": "Correct! Brown eye color is dominant over blue. Both parents can be carriers of the recessive blue allele (Bb) without showing it. If both pass on the recessive allele, the child is bb (blue eyes).",
            "feedback_incorrect": "Brown-eyed parents can have blue-eyed children if both carry a recessive blue eye allele. They would each have the genotype Bb (heterozygous). When both pass on their recessive b allele, the child is bb and expresses blue eyes."
        },
        {
            "question": "Why are siblings who share the same parents not identical to each other (unless they are identical twins)?",
            "choices": {
                "A": "Siblings receive different amounts of DNA from their parents",
                "B": "Each sibling receives a different random combination of alleles from the same parents",
                "C": "Only the first-born child inherits genes from both parents",
                "D": "Siblings are only related to one parent, not both"
            },
            "correct": "B",
            "feedback_correct": "Correct! Each parent has two alleles for every gene and randomly passes on one. The specific combination each sibling receives is different, creating genetic uniqueness.",
            "feedback_incorrect": "Each reproductive cell (egg or sperm) contains a random assortment of alleles. Since each parent randomly passes on one of their two alleles for every gene, each sibling receives a unique combination."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the model, when both parents were set to Bb (heterozygous) for a trait, the offspring showed a 3:1 phenotype ratio. What does this ratio mean?",
            "choices": {
                "A": "3 out of 4 offspring are heterozygous and 1 is homozygous",
                "B": "Approximately 75% of offspring display the dominant trait and 25% display the recessive trait",
                "C": "The dominant trait is 3 times stronger than the recessive trait",
                "D": "3 offspring survive and 1 does not"
            },
            "correct": "B",
            "feedback_correct": "Correct! In a Bb x Bb cross, the possible genotypes are BB, Bb, Bb, and bb. Three out of four (BB, Bb, Bb) express the dominant phenotype, while one (bb) expresses the recessive phenotype.",
            "feedback_incorrect": "The 3:1 ratio refers to phenotype expression. From a Bb x Bb cross, three possible genotypes (BB, Bb, Bb) show the dominant trait, while one (bb) shows the recessive trait. This is about trait expression, not survival or trait strength."
        },
        {
            "question": "Your model showed that a Bb x bb cross produced offspring that were 50% Bb and 50% bb. A student claims the recessive parent 'weakened' the dominant trait. Using the model, what is the correct explanation?",
            "choices": {
                "A": "The student is correct; recessive alleles weaken dominant ones",
                "B": "Each parent contributes one allele randomly. The Bb parent passes B or b (50/50), while the bb parent always passes b. This produces Bb or bb offspring in equal proportions",
                "C": "The dominant allele became recessive after mixing with the other parent's genes",
                "D": "Allele inheritance depends on which parent is taller"
            },
            "correct": "B",
            "feedback_correct": "Correct! Alleles are not weakened or strengthened. The Bb parent randomly passes either B or b with equal probability. The bb parent can only pass b. So offspring are either Bb (dominant phenotype) or bb (recessive phenotype).",
            "feedback_incorrect": "Recessive alleles do not weaken dominant ones. Inheritance is about random allele distribution. The Bb parent has a 50% chance of passing B and 50% of passing b. The bb parent always passes b. This produces a 1:1 ratio of Bb to bb offspring."
        },
        {
            "question": "The model demonstrates that sexual reproduction produces offspring with genetic variation, while asexual reproduction produces genetically identical offspring. Why is genetic variation important for species survival?",
            "choices": {
                "A": "Genetic variation makes organisms look different, which is important for identification",
                "B": "Genetic variation ensures that some individuals in a population are likely to have traits that help them survive if environmental conditions change",
                "C": "Genetic variation is not important; identical organisms are better adapted",
                "D": "Variation only matters for plants, not animals"
            },
            "correct": "B",
            "feedback_correct": "Correct! Genetic variation is the raw material for natural selection. When the environment changes, a genetically diverse population is more likely to include individuals with traits suited to the new conditions, preventing extinction.",
            "feedback_incorrect": "Genetic variation provides a survival advantage for populations. If all individuals were genetically identical, a single disease or environmental change could wipe out the entire population. Variation ensures some individuals may have traits suited to new conditions."
        },
        {
            "question": "In the STEM challenge, you used genotype and phenotype data to identify the parents of an unknown cub. The cub expressed a recessive trait (bb). Which parent combinations could NOT have produced this cub?",
            "choices": {
                "A": "Bb x Bb (both heterozygous carriers)",
                "B": "Bb x bb (one carrier, one recessive)",
                "C": "BB x BB (both homozygous dominant)",
                "D": "bb x bb (both homozygous recessive)"
            },
            "correct": "C",
            "feedback_correct": "Correct! BB x BB can only produce BB offspring. Since the cub is bb (two recessive alleles), at least one b allele must come from each parent. Two BB parents cannot provide any b alleles.",
            "feedback_incorrect": "A bb offspring must inherit one b allele from each parent. If both parents are BB, they have no b alleles to pass on. Only parents with at least one b allele each (Bb or bb) can produce bb offspring."
        }
    ]
}

# =============================================================================
# G08-L09: Your Music Is a Wave
# NGSS: MS-PS4-1, MS-PS4-2
# =============================================================================
L09_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What causes sound?",
            "choices": {
                "A": "Light waves bouncing off objects",
                "B": "Vibrations that travel through a medium like air",
                "C": "Electricity flowing through the air",
                "D": "Temperature changes in the atmosphere"
            },
            "correct": "B",
            "feedback_correct": "Correct! Sound is produced by vibrations (from a speaker, vocal cord, instrument, etc.) that create pressure waves traveling through a medium such as air, water, or solids.",
            "feedback_incorrect": "Sound is caused by vibrations that create pressure waves in a medium (air, water, or solids). When a speaker vibrates, it compresses and stretches the air, creating waves that travel to your ears."
        },
        {
            "question": "When you turn up the volume on your phone, what property of the sound wave are you changing?",
            "choices": {
                "A": "The speed of the wave",
                "B": "The wavelength of the wave",
                "C": "The amplitude (height) of the wave",
                "D": "The direction the wave travels"
            },
            "correct": "C",
            "feedback_correct": "Correct! Volume corresponds to amplitude. Turning up the volume increases the amplitude (height) of the sound wave, which carries more energy and sounds louder.",
            "feedback_incorrect": "Volume is related to amplitude, not speed or wavelength. Increasing the volume increases the amplitude of the sound wave, meaning larger pressure variations reach your ear, and you perceive louder sound."
        },
        {
            "question": "What determines the pitch of a sound (whether it sounds high or low)?",
            "choices": {
                "A": "The speed at which the sound travels",
                "B": "The number of wave cycles per second (frequency)",
                "C": "The distance between the sound source and your ear",
                "D": "The temperature of the air"
            },
            "correct": "B",
            "feedback_correct": "Correct! Pitch is determined by frequency, measured in Hertz (Hz). Higher frequency means more wave cycles per second and a higher-pitched sound.",
            "feedback_incorrect": "Pitch is determined by frequency. A high-frequency wave (many cycles per second) sounds high-pitched, while a low-frequency wave sounds low-pitched. Frequency is measured in Hertz (Hz)."
        },
        {
            "question": "Can sound travel through a vacuum (completely empty space)?",
            "choices": {
                "A": "Yes, sound travels through everything",
                "B": "No, sound requires a medium (matter) to travel through",
                "C": "Yes, but only very loud sounds",
                "D": "Sound travels faster in a vacuum than in air"
            },
            "correct": "B",
            "feedback_correct": "Correct! Sound is a mechanical wave that requires particles to vibrate. In a vacuum (no particles), there is nothing to carry the vibrations, so sound cannot travel.",
            "feedback_incorrect": "Sound is a mechanical wave that travels by vibrating particles in a medium. A vacuum has no particles, so sound waves have nothing to travel through. This is why there is no sound in outer space."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "Your model showed that doubling the amplitude quadrupled the wave energy. What mathematical relationship does this demonstrate?",
            "choices": {
                "A": "Energy and amplitude are inversely proportional (as one goes up, the other goes down)",
                "B": "Energy is proportional to the square of amplitude (E is proportional to A squared)",
                "C": "Energy and amplitude are directly proportional (doubling one doubles the other)",
                "D": "Energy and amplitude are unrelated"
            },
            "correct": "B",
            "feedback_correct": "Correct! Wave energy is proportional to amplitude squared. This is why doubling the amplitude (2 squared = 4) quadruples the energy. A small increase in amplitude means a large increase in energy.",
            "feedback_incorrect": "The model demonstrates a squared relationship. Since energy is proportional to amplitude squared, doubling amplitude increases energy by 2 squared = 4 times. This is a fundamental property of waves."
        },
        {
            "question": "In the 'Bass Drop' scenario, amplitude was maximum but frequency was minimum. In the 'Screaming High Note' scenario, both were maximum. Both had high Wave Energy. What does this tell you about what determines wave energy?",
            "choices": {
                "A": "Only amplitude determines wave energy; frequency has no effect",
                "B": "Only frequency determines wave energy; amplitude has no effect",
                "C": "Both amplitude and frequency contribute to the total energy of a wave",
                "D": "Wave energy is constant regardless of amplitude or frequency"
            },
            "correct": "C",
            "feedback_correct": "Correct! The model shows that both amplitude and frequency contribute to wave energy. A loud bass note (high amplitude, low frequency) and a screaming high note (high amplitude, high frequency) both carry significant energy.",
            "feedback_incorrect": "Both amplitude and frequency contribute to wave energy. A wave can have high energy from high amplitude (loud), high frequency (rapid oscillation), or both. The model shows these contributions through different scenarios."
        },
        {
            "question": "Sound, light, radio, and WiFi are all waves. Your model showed that amplitude controls loudness in sound. In light waves, what does amplitude control?",
            "choices": {
                "A": "The color of light",
                "B": "The brightness (intensity) of light",
                "C": "The speed of light",
                "D": "Whether light can pass through glass"
            },
            "correct": "B",
            "feedback_correct": "Correct! Just as amplitude determines loudness in sound, amplitude determines brightness in light. The same wave property (amplitude = energy intensity) manifests differently in different types of waves.",
            "feedback_incorrect": "Amplitude is the intensity property of all waves. In sound, higher amplitude means louder. In light, higher amplitude means brighter. Color is determined by frequency, just as pitch is determined by frequency in sound."
        },
        {
            "question": "In the STEM challenge, you designed a concert venue. A student suggests making all walls from hard, smooth materials like glass. Using your model's principles about wave behavior, what problem would this create?",
            "choices": {
                "A": "Glass walls would block all sound from entering the venue",
                "B": "Hard, smooth surfaces reflect sound waves rather than absorbing them, creating excessive echoes and reverberation that distort the music",
                "C": "Glass would amplify the sound waves, making them dangerously loud",
                "D": "Smooth walls would cause sound to travel faster, distorting the pitch"
            },
            "correct": "B",
            "feedback_correct": "Correct! Hard, smooth surfaces reflect rather than absorb sound waves. This creates echoes and reverberation where reflected waves overlap with direct sound, muddying the audio. Good acoustics require a balance of reflective and absorptive materials.",
            "feedback_incorrect": "When waves encounter a surface, they can be reflected, absorbed, or transmitted. Hard, smooth surfaces primarily reflect sound waves. Multiple reflections create echoes and reverberation that distort musical clarity. Concert venues need absorptive materials to control reflections."
        }
    ]
}

# =============================================================================
# G08-L10: Hand Warmers and Hidden Reactions
# NGSS: MS-PS1-4, MS-PS1-5
# =============================================================================
L10_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is a chemical reaction?",
            "choices": {
                "A": "Mixing two substances together without any change",
                "B": "A process where atoms rearrange to form new substances with different properties",
                "C": "Heating a substance until it melts",
                "D": "Breaking an object into smaller pieces"
            },
            "correct": "B",
            "feedback_correct": "Correct! A chemical reaction involves the rearrangement of atoms to form new substances. The products have different chemical properties than the reactants.",
            "feedback_incorrect": "A chemical reaction is not just mixing or physical change. It involves the rearrangement of atoms, breaking and forming chemical bonds to create entirely new substances with different properties."
        },
        {
            "question": "When wood burns in a fireplace, the ashes weigh less than the original wood. Does this mean mass was destroyed?",
            "choices": {
                "A": "Yes, burning destroys mass permanently",
                "B": "No, the 'missing' mass escaped as gases (CO2 and water vapor) into the air",
                "C": "Yes, fire consumes mass and converts it to pure energy",
                "D": "No, the ashes actually weigh the same as the wood"
            },
            "correct": "B",
            "feedback_correct": "Correct! Mass is conserved in chemical reactions. The 'missing' mass was released as carbon dioxide and water vapor gases. If you could capture all products (ash + gases), the total mass would equal the original wood plus the oxygen used.",
            "feedback_incorrect": "Mass is never destroyed in a chemical reaction (conservation of mass). When wood burns, carbon and hydrogen atoms combine with oxygen to form CO2 and H2O gases that escape into the air. The total mass of all products equals the total mass of all reactants."
        },
        {
            "question": "What is the difference between an exothermic and an endothermic reaction?",
            "choices": {
                "A": "Exothermic reactions are fast; endothermic reactions are slow",
                "B": "Exothermic reactions release heat to the surroundings; endothermic reactions absorb heat from the surroundings",
                "C": "Exothermic reactions only occur in living things; endothermic reactions only occur in non-living things",
                "D": "There is no difference; they are the same thing"
            },
            "correct": "B",
            "feedback_correct": "Correct! Exothermic reactions release energy as heat (the surroundings warm up), while endothermic reactions absorb energy as heat (the surroundings cool down).",
            "feedback_incorrect": "The key distinction is energy flow. Exothermic reactions release heat to the surroundings (you feel warmth), while endothermic reactions absorb heat from the surroundings (you feel cooling). Speed is not the defining difference."
        },
        {
            "question": "If you combine baking soda and vinegar and the mixture gets colder, what type of reaction occurred?",
            "choices": {
                "A": "Exothermic, because a chemical reaction happened",
                "B": "Endothermic, because the reaction absorbed heat from the surroundings",
                "C": "No reaction occurred because temperature changed",
                "D": "Both exothermic and endothermic at the same time"
            },
            "correct": "B",
            "feedback_correct": "Correct! If the surroundings (mixture) got colder, the reaction absorbed heat energy from the surroundings. This is the hallmark of an endothermic reaction.",
            "feedback_incorrect": "A temperature decrease in the surroundings indicates an endothermic reaction. The reaction absorbed thermal energy from its surroundings, causing the temperature to drop. This is the opposite of an exothermic reaction, which would release heat."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In your model, when Oxygen Exposure was set to zero, the iron powder remained unchanged and Heat Output stayed at zero, even though Iron Powder Amount was at maximum. What does this demonstrate?",
            "choices": {
                "A": "Iron powder does not contain any chemical energy",
                "B": "Both reactants (iron and oxygen) must be present for the chemical reaction to occur; removing one prevents the reaction entirely",
                "C": "The model was inaccurate because iron should generate heat on its own",
                "D": "Oxygen has no role in chemical reactions with metals"
            },
            "correct": "B",
            "feedback_correct": "Correct! Chemical reactions require all reactants to be present. Iron + Oxygen -> Iron Oxide + Heat. Without oxygen, the iron cannot oxidize, so no reaction occurs and no heat is released. This is why hand warmers work only when opened (exposed to air).",
            "feedback_incorrect": "The model demonstrates a fundamental chemistry principle: all reactants must be present for a reaction to proceed. The iron oxidation reaction (Iron + Oxygen -> Iron Oxide) requires both iron and oxygen. This is why hand warmers are sealed until use."
        },
        {
            "question": "Your model showed that the hand warmer eventually stopped producing heat even though oxygen was still available. The iron had been fully consumed. This is an example of:",
            "choices": {
                "A": "The reaction reaching equilibrium where forward and reverse reactions balance",
                "B": "A limiting reactant: the iron was completely used up, so the reaction could not continue even with excess oxygen",
                "C": "The reaction losing energy over time due to entropy",
                "D": "Oxygen becoming too concentrated for the reaction to continue"
            },
            "correct": "B",
            "feedback_correct": "Correct! Iron was the limiting reactant. Once all the iron reacted with oxygen, no more iron oxide (or heat) could be produced, regardless of how much oxygen remained. The limiting reactant determines when the reaction stops.",
            "feedback_incorrect": "This demonstrates the concept of a limiting reactant. Even with plenty of oxygen available, the reaction stops when all the iron has been consumed. The iron limits how much product (iron oxide and heat) can be formed."
        },
        {
            "question": "A student weighs a sealed hand warmer before and after the reaction is complete. The mass stays the same, yet new substances (iron oxide) have formed. Which law explains this?",
            "choices": {
                "A": "The law of gravity, because the hand warmer stays on the ground",
                "B": "The law of conservation of energy, because energy cannot be created",
                "C": "The law of conservation of mass: the total number of atoms does not change in a chemical reaction, so total mass is conserved",
                "D": "Newton's Third Law, because every reaction has an equal and opposite reaction"
            },
            "correct": "C",
            "feedback_correct": "Correct! Conservation of mass states that atoms are neither created nor destroyed in a chemical reaction. The same iron and oxygen atoms that started as reactants are now rearranged as iron oxide. Same atoms, same total mass, new substance.",
            "feedback_incorrect": "The law of conservation of mass explains this observation. In a chemical reaction, atoms rearrange but are never created or destroyed. The iron and oxygen atoms still exist as iron oxide. Since no atoms were added or removed, the total mass remains unchanged."
        },
        {
            "question": "Based on your model, you need to design a hand warmer that lasts exactly 8 hours. Currently, your prototype lasts only 4 hours. Which modification is best supported by the model evidence?",
            "choices": {
                "A": "Double the amount of iron powder to provide twice as much reactant for the exothermic reaction",
                "B": "Use a different metal that does not react with oxygen",
                "C": "Remove the oxygen exposure holes to trap more heat inside",
                "D": "Make the packet smaller to concentrate the heat"
            },
            "correct": "A",
            "feedback_correct": "Correct! The model shows that Iron Powder Amount directly affects how long the reaction lasts (more reactant = longer reaction). Doubling the iron gives twice as much fuel for the exothermic reaction. You might also control oxygen exposure rate to regulate how fast the iron reacts.",
            "feedback_incorrect": "The model shows that the amount of iron (the limiting reactant) determines how long the reaction lasts. Doubling the iron provides twice as much fuel for the oxidation reaction. Removing oxygen would stop the reaction, and a non-reactive metal would produce no heat."
        }
    ]
}

# =============================================================================
# Master dictionary mapping lesson IDs to question sets
# =============================================================================
ALL_QUESTIONS = {
    "G08-L01": L01_QUESTIONS,
    "G08-L02": L02_QUESTIONS,
    "G08-L03": L03_QUESTIONS,
    "G08-L04": L04_QUESTIONS,
    "G08-L05": L05_QUESTIONS,
    "G08-L06": L06_QUESTIONS,
    "G08-L07": L07_QUESTIONS,
    "G08-L08": L08_QUESTIONS,
    "G08-L09": L09_QUESTIONS,
    "G08-L10": L10_QUESTIONS,
}
