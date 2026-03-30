#!/usr/bin/env python3
"""Multiple choice pre/post assessment questions for Grade 11 Level 2 ModelIt! Lessons
(Complex Systems & Sustainability)

Each lesson has 5 MC pre-assessment and 5 MC post-assessment questions.
Pre-assessment: gauges prior knowledge before the lesson.
Post-assessment: tests analysis, evaluation, and application after the lesson.
All questions are CAST-exam-style, HS NGSS-aligned, with 4 choices (A-D).
"""

# ---------------------------------------------------------------------------
# L01 — The Ocean's Silent Emergency (HS-ESS2-6, HS-LS2-6)
# ---------------------------------------------------------------------------
L01_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Which of the following best describes what happens chemically when carbon dioxide dissolves in seawater?",
            "choices": {
                "A": "CO2 reacts with water to form carbonic acid, which releases hydrogen ions and lowers pH",
                "B": "CO2 bonds with sodium chloride to form a neutral salt compound",
                "C": "CO2 replaces dissolved oxygen, causing fish to suffocate",
                "D": "CO2 evaporates quickly from warm ocean surfaces without reacting"
            },
            "correct": "A",
            "feedback_correct": "Correct. CO2 + H2O forms carbonic acid (H2CO3), which dissociates to release H+ ions, lowering seawater pH.",
            "feedback_incorrect": "When CO2 dissolves in seawater, it reacts with H2O to form carbonic acid (H2CO3). This acid releases hydrogen ions, which lower the pH of the ocean."
        },
        {
            "question": "The pH scale is logarithmic. A decrease from pH 8.2 to pH 8.1 means the ocean has become approximately how much more acidic?",
            "choices": {
                "A": "1% more acidic",
                "B": "10% more acidic",
                "C": "26% more acidic",
                "D": "100% more acidic"
            },
            "correct": "C",
            "feedback_correct": "Correct. Because the pH scale is logarithmic, a 0.1 unit decrease represents roughly a 26% increase in hydrogen ion concentration.",
            "feedback_incorrect": "The pH scale is logarithmic, so each full unit represents a tenfold change. A 0.1 unit drop corresponds to approximately a 26% increase in hydrogen ion concentration (10^0.1 = 1.26)."
        },
        {
            "question": "Which organisms would likely be most directly harmed by a decrease in carbonate ion availability in the ocean?",
            "choices": {
                "A": "Jellyfish, which have no hard structures",
                "B": "Corals, mollusks, and pteropods that build calcium carbonate shells or skeletons",
                "C": "Deep-sea fish that live in total darkness",
                "D": "Marine mammals such as whales and dolphins"
            },
            "correct": "B",
            "feedback_correct": "Correct. Calcifying organisms like corals, mollusks, and pteropods depend on carbonate ions to build and maintain their CaCO3 structures.",
            "feedback_incorrect": "Organisms that build shells or skeletons from calcium carbonate (CaCO3) are most directly threatened because lower carbonate ion concentrations make it harder to form and maintain these structures."
        },
        {
            "question": "Approximately what percentage of human-produced CO2 emissions does the ocean absorb?",
            "choices": {
                "A": "Less than 5%",
                "B": "About 10%",
                "C": "About 25-30%",
                "D": "More than 60%"
            },
            "correct": "C",
            "feedback_correct": "Correct. The ocean absorbs roughly 25-30% of anthropogenic CO2 emissions, making it Earth's largest carbon sink.",
            "feedback_incorrect": "The ocean absorbs approximately 25-30% of human CO2 emissions annually. While this has buffered atmospheric warming, it has come at the cost of ocean acidification."
        },
        {
            "question": "What is a 'carbon sink' in Earth's climate system?",
            "choices": {
                "A": "A location where carbon is produced through combustion",
                "B": "A natural system that absorbs more CO2 than it releases",
                "C": "A man-made device that captures CO2 from smokestacks",
                "D": "A deep-ocean trench where carbon is permanently destroyed"
            },
            "correct": "B",
            "feedback_correct": "Correct. A carbon sink is any natural system that absorbs more carbon dioxide from the atmosphere than it releases.",
            "feedback_incorrect": "A carbon sink is a natural reservoir that absorbs more CO2 than it releases. The ocean and forests are Earth's two largest carbon sinks."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's model shows that as Atmospheric CO2 rises from 420 ppm to 900 ppm, Seawater pH drops from 8.1 to 7.7 and Shell-Building Organism Survival declines sharply. Which best explains the mechanism connecting these variables?",
            "choices": {
                "A": "Higher CO2 warms the water, which directly kills shell-building organisms through heat stress",
                "B": "Higher CO2 leads to more carbonic acid, which lowers pH and reduces carbonate ion availability needed for calcification",
                "C": "Higher CO2 increases oxygen levels, which makes shells dissolve faster",
                "D": "Higher CO2 causes algal blooms that outcompete shell-building organisms for sunlight"
            },
            "correct": "B",
            "feedback_correct": "Correct. The causal chain is: more atmospheric CO2 increases dissolved CO2 in seawater, forming carbonic acid that lowers pH and binds carbonate ions into bicarbonate, reducing the carbonate available for calcification.",
            "feedback_incorrect": "The mechanism is chemical: CO2 dissolves to form carbonic acid, lowering pH. As pH drops, hydrogen ions react with carbonate ions to form bicarbonate, depleting the carbonate that shell-building organisms need."
        },
        {
            "question": "A researcher compares two model scenarios: one where CO2 stabilizes at 450 ppm and another where CO2 reaches 900 ppm. In the 450 ppm scenario, Marine Food Web Stability remains relatively intact. What does this comparison most strongly support?",
            "choices": {
                "A": "Ocean acidification is entirely reversible once CO2 emissions stop",
                "B": "Marine food webs are unaffected by pH changes below 0.3 units",
                "C": "Aggressive CO2 mitigation can prevent the cascading ecosystem collapse seen in high-emission scenarios",
                "D": "Shell-building organisms can adapt to any pH change given enough time"
            },
            "correct": "C",
            "feedback_correct": "Correct. The comparison shows that limiting CO2 prevents pH from crossing tipping points that trigger cascading food web collapse, supporting the case for aggressive mitigation.",
            "feedback_incorrect": "The comparison demonstrates that stabilizing CO2 at lower levels prevents the pH decline from reaching tipping points where shell-building organisms fail and food web collapse cascades upward."
        },
        {
            "question": "A student claims that ocean acidification is less urgent than atmospheric warming because the pH change is 'only 0.1 units.' Which evidence from the model best refutes this claim?",
            "choices": {
                "A": "The ocean's volume is much larger than the atmosphere",
                "B": "A 0.1 pH drop represents a 26% increase in acidity on the logarithmic scale, and carbonate depletion drops exponentially as pH decreases further",
                "C": "Fish populations have not yet shown decline in response to pH changes",
                "D": "Ocean temperatures are rising faster than ocean pH is changing"
            },
            "correct": "B",
            "feedback_correct": "Correct. The logarithmic nature of pH means 0.1 units is a 26% acidity increase, and the model shows carbonate depletion accelerates nonlinearly, creating tipping points well before pH drops a full unit.",
            "feedback_incorrect": "The 0.1 pH decrease actually represents a ~26% increase in hydrogen ion concentration because pH is logarithmic. Additionally, carbonate depletion is nonlinear and accelerates as pH drops, meaning small further decreases can trigger dramatic ecosystem effects."
        },
        {
            "question": "In the ocean acidification model, which of the following represents a positive feedback loop that could make acidification self-reinforcing?",
            "choices": {
                "A": "Increased CO2 absorption leads to decreased ocean temperature, slowing further absorption",
                "B": "Dying marine organisms release stored carbon, which increases atmospheric CO2, which drives further acidification",
                "C": "Lower pH causes more carbonate to form, strengthening shells",
                "D": "Reduced marine life leads to less oxygen consumption, stabilizing ocean chemistry"
            },
            "correct": "B",
            "feedback_correct": "Correct. When marine organisms die and decompose, they release stored carbon. This adds CO2 to the system, further lowering pH in a self-reinforcing positive feedback loop.",
            "feedback_incorrect": "A positive feedback loop amplifies the original change. Dying organisms release stored carbon as CO2, which increases acidification, which kills more organisms, reinforcing the cycle."
        },
        {
            "question": "An ocean monitoring station detects that local pH has dropped below the aragonite undersaturation threshold. What does a systems-level analysis predict will happen next?",
            "choices": {
                "A": "Shell-building organisms will adapt by switching to alternative shell materials within one generation",
                "B": "Aragonite shells will begin dissolving faster than organisms can build them, threatening pteropods, corals, and the food webs they support",
                "C": "The pH will self-correct through increased biological activity",
                "D": "Only organisms deeper than 200 meters will be affected"
            },
            "correct": "B",
            "feedback_correct": "Correct. Below the aragonite undersaturation threshold, seawater becomes corrosive to aragonite shells. Shell dissolution exceeds formation, threatening calcifiers and cascading through dependent food webs.",
            "feedback_incorrect": "When water drops below the aragonite undersaturation point, it becomes corrosive to aragonite (a form of CaCO3). Shells dissolve faster than they can be built, threatening organisms like pteropods that form the base of many marine food chains."
        }
    ]
}

# ---------------------------------------------------------------------------
# L02 — Can Cities Run on 100% Clean Energy? (HS-PS3-3, HS-ESS3-2)
# ---------------------------------------------------------------------------
L02_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Which of the following best describes the concept of 'intermittency' as it applies to renewable energy?",
            "choices": {
                "A": "Renewable energy sources produce electricity only when natural conditions allow, creating gaps in supply",
                "B": "Renewable energy systems break down frequently and need constant repair",
                "C": "Renewable energy costs fluctuate unpredictably from day to day",
                "D": "Renewable energy sources can only be installed in certain geographic regions"
            },
            "correct": "A",
            "feedback_correct": "Correct. Intermittency refers to the variable nature of solar and wind power, which depends on weather and time of day.",
            "feedback_incorrect": "Intermittency means that renewable sources like solar and wind produce electricity only when conditions permit (sun shining, wind blowing), creating periods when generation is low or zero."
        },
        {
            "question": "What does the term 'capacity factor' measure for an energy source?",
            "choices": {
                "A": "The maximum number of homes it can power at peak output",
                "B": "The ratio of actual electricity output to maximum possible output over time",
                "C": "The physical size of the generating equipment relative to its power rating",
                "D": "The number of years the equipment can operate before replacement"
            },
            "correct": "B",
            "feedback_correct": "Correct. Capacity factor is the ratio of actual output to maximum possible output, reflecting how much of the time a source operates at full capacity.",
            "feedback_incorrect": "Capacity factor compares actual electricity produced to what would be produced if the source ran at full power 24/7. Solar panels average 20-25% capacity factor because they only generate during daylight."
        },
        {
            "question": "On an electrical grid, what must always be true about the relationship between electricity supply and demand?",
            "choices": {
                "A": "Supply should always exceed demand by at least 50% for safety",
                "B": "Supply and demand must be balanced in real time to maintain grid stability",
                "C": "Demand can safely exceed supply for up to 24 hours using voltage reduction",
                "D": "Supply and demand only need to match on a monthly average basis"
            },
            "correct": "B",
            "feedback_correct": "Correct. Electricity supply and demand must be matched essentially instantaneously. Even seconds of imbalance can cause frequency deviations and blackouts.",
            "feedback_incorrect": "Unlike other commodities, electricity cannot be easily inventoried. Supply and demand must balance in real time, or the grid experiences frequency instability that can cascade into blackouts."
        },
        {
            "question": "Which statement best explains why energy storage is important for renewable energy grids?",
            "choices": {
                "A": "Stored energy is cheaper to produce than directly generated energy",
                "B": "Storage allows excess energy produced during high-generation periods to be used during low-generation periods",
                "C": "Energy storage eliminates the need for any grid infrastructure",
                "D": "Storage converts renewable energy into a more efficient form of power"
            },
            "correct": "B",
            "feedback_correct": "Correct. Storage bridges the timing gap between when renewables generate electricity and when consumers need it.",
            "feedback_incorrect": "Energy storage captures surplus generation (e.g., midday solar) and releases it when generation is low but demand is high (e.g., evening peaks), solving the timing mismatch inherent to intermittent sources."
        },
        {
            "question": "What is 'curtailment' in the context of renewable energy?",
            "choices": {
                "A": "The gradual phase-out of fossil fuel power plants",
                "B": "Government regulations that limit renewable energy installation",
                "C": "Deliberately reducing renewable energy output because the grid cannot absorb all the power being generated",
                "D": "The loss of energy during transmission over long distances"
            },
            "correct": "C",
            "feedback_correct": "Correct. Curtailment is the intentional reduction of renewable output when production exceeds demand and storage capacity, effectively wasting clean energy.",
            "feedback_incorrect": "Curtailment occurs when renewable generation exceeds what the grid and storage can absorb. The energy is essentially wasted, which is a paradox of high-renewable grids."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A model shows that moving from 50% to 80% renewable energy requires doubling storage capacity, but moving from 80% to 100% requires increasing storage capacity tenfold. Which concept best explains this nonlinear relationship?",
            "choices": {
                "A": "Renewable energy becomes less efficient at higher penetration levels",
                "B": "At high renewable penetration, rare multi-day weather events with minimal sun and wind require enormous storage reserves to avoid blackouts",
                "C": "Battery technology degrades faster when used more frequently",
                "D": "Grid operators intentionally slow renewable adoption above 80%"
            },
            "correct": "B",
            "feedback_correct": "Correct. The exponential storage increase is driven by worst-case scenarios: at 100% renewable, even rare events like a week of cloudy, windless winter weather must be covered entirely by storage.",
            "feedback_incorrect": "At 50% renewable, fossil plants handle gaps. At 80%, daily cycling needs more storage. At 100%, multi-day and seasonal low-generation events must be covered entirely by storage, requiring exponentially more capacity."
        },
        {
            "question": "The 'duck curve' describes a pattern where net electricity demand dips at midday and spikes in the evening. A student proposes solving this by installing more solar panels. Why is this solution insufficient?",
            "choices": {
                "A": "Solar panels cannot be installed on residential rooftops",
                "B": "More solar deepens the midday surplus (increasing curtailment) but does nothing for the evening peak when solar output is zero",
                "C": "The duck curve only occurs in tropical climates",
                "D": "Solar panels generate more electricity in the evening than at midday"
            },
            "correct": "B",
            "feedback_correct": "Correct. Adding more solar worsens the midday oversupply while the evening demand peak remains unmet, making the duck curve problem worse, not better.",
            "feedback_incorrect": "More solar panels increase midday generation when supply already exceeds demand, leading to more curtailment. The evening peak occurs after sunset, so additional solar capacity cannot help. Storage or demand-shifting is needed."
        },
        {
            "question": "A city's grid model achieves 99.97% reliability at 90% renewable energy with 12 hours of battery storage. When pushed to 100% renewable, reliability drops to 98.5%. What systems-level intervention would most effectively close this gap?",
            "choices": {
                "A": "Replace all wind turbines with solar panels to increase consistency",
                "B": "Combine expanded battery storage with pumped hydro for multi-day reserves, demand response programs, and geographic diversification of renewable sources",
                "C": "Reduce the city's population to lower demand",
                "D": "Accept the lower reliability since 98.5% is close enough"
            },
            "correct": "B",
            "feedback_correct": "Correct. Closing the last reliability gap requires a systems approach: long-duration storage (pumped hydro), flexible demand, and geographically diverse generation to reduce the probability of system-wide low generation.",
            "feedback_incorrect": "The 1.47% reliability gap represents ~129 hours of potential blackout per year. Closing it requires multiple complementary strategies: long-duration storage for multi-day events, demand flexibility, and geographic spread to ensure weather events don't affect all sources simultaneously."
        },
        {
            "question": "A student argues that seasonal variation in solar energy is a minor challenge because 'the sun shines every day.' Using model data, which evidence best counters this claim?",
            "choices": {
                "A": "A city at 45 degrees N latitude receives 4x more solar energy in June than December, creating a seasonal generation gap that daily batteries cannot bridge",
                "B": "Solar panels stop working when temperatures drop below freezing",
                "C": "Cloud cover only affects solar generation in the summer months",
                "D": "Wind energy perfectly compensates for all seasonal solar variation"
            },
            "correct": "A",
            "feedback_correct": "Correct. Seasonal variation at mid-latitudes creates a generation gap lasting weeks to months. Daily battery cycling (4-12 hours) cannot bridge a months-long winter solar deficit.",
            "feedback_incorrect": "At mid-latitudes, winter solar generation can be 25% of summer levels. This creates a seasonal deficit lasting months that cannot be addressed by daily battery cycling, requiring either long-duration storage or complementary wind and other sources."
        },
        {
            "question": "Evaluate this claim: 'Since wind and solar are now the cheapest forms of electricity generation, transitioning to 100% renewable energy is primarily an economic decision.' Which model finding most effectively challenges this claim?",
            "choices": {
                "A": "Renewable energy equipment is manufactured using fossil fuels",
                "B": "While generation costs are low, the systems integration costs (storage, grid upgrades, backup capacity) for 100% renewable are the dominant expense and represent a physics and engineering challenge, not just an economic one",
                "C": "Solar and wind are only cheaper in sunny and windy regions",
                "D": "Fossil fuel companies will lobby against the transition"
            },
            "correct": "B",
            "feedback_correct": "Correct. The cost of generating renewable electricity is low, but the systems engineering challenge of maintaining reliability through all weather conditions drives exponentially higher storage and infrastructure costs.",
            "feedback_incorrect": "Generation cost is only part of the equation. The fundamental challenge is physics: matching variable supply to constant demand requires storage, grid flexibility, and backup capacity that become exponentially more expensive as renewable penetration approaches 100%."
        }
    ]
}

# ---------------------------------------------------------------------------
# L03 — The Coral Reef Death Spiral (HS-LS2-2, HS-LS2-6)
# ---------------------------------------------------------------------------
L03_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is coral bleaching?",
            "choices": {
                "A": "A chemical process where ocean pollutants dissolve coral skeletons",
                "B": "A stress response where corals expel their symbiotic algae, turning white and losing their primary energy source",
                "C": "A natural seasonal color change similar to leaves changing in autumn",
                "D": "A disease caused by bacteria that infects coral tissue"
            },
            "correct": "B",
            "feedback_correct": "Correct. Coral bleaching occurs when heat stress causes corals to expel their symbiotic zooxanthellae algae, which normally provide up to 90% of the coral's energy.",
            "feedback_incorrect": "Bleaching is a stress response triggered primarily by elevated water temperatures. Corals expel their zooxanthellae algae, turning white. Without these algae, corals lose their main energy source and can die."
        },
        {
            "question": "What role do zooxanthellae play in coral reef ecosystems?",
            "choices": {
                "A": "They are parasites that slowly weaken coral over time",
                "B": "They are photosynthetic algae living inside coral that provide up to 90% of the coral's energy",
                "C": "They are predators that protect corals from fish",
                "D": "They are bacteria that decompose dead coral material"
            },
            "correct": "B",
            "feedback_correct": "Correct. Zooxanthellae are photosynthetic dinoflagellates that live within coral tissues in a mutualistic symbiosis, providing energy through photosynthesis.",
            "feedback_incorrect": "Zooxanthellae are microscopic photosynthetic algae living symbiotically inside coral tissue. They convert sunlight into energy that the coral uses, providing up to 90% of its nutritional needs."
        },
        {
            "question": "Approximately what percentage of all marine species depend on coral reefs for habitat, even though reefs cover less than 1% of the ocean floor?",
            "choices": {
                "A": "About 5%",
                "B": "About 10%",
                "C": "About 25%",
                "D": "About 50%"
            },
            "correct": "C",
            "feedback_correct": "Correct. Despite covering less than 1% of the ocean floor, coral reefs support approximately 25% of all marine species.",
            "feedback_incorrect": "Coral reefs are among the most biodiverse ecosystems on Earth. They support roughly 25% of all marine species despite occupying less than 1% of ocean area, earning them the title 'rainforests of the sea.'"
        },
        {
            "question": "How long do scientists estimate corals typically need to fully recover after a bleaching event?",
            "choices": {
                "A": "A few weeks to a month",
                "B": "1-2 years",
                "C": "10-15 years",
                "D": "Over 100 years"
            },
            "correct": "C",
            "feedback_correct": "Correct. Full recovery from a major bleaching event typically requires 10-15 years, during which corals must regrow tissue and reestablish zooxanthellae populations.",
            "feedback_incorrect": "Corals generally need 10-15 years to fully recover from a bleaching event. They must regrow tissue, reacquire zooxanthellae, and rebuild energy reserves."
        },
        {
            "question": "What is a 'phase shift' in coral reef ecology?",
            "choices": {
                "A": "The normal seasonal cycle of coral growth and dormancy",
                "B": "An abrupt transition from a coral-dominated reef to an algae-dominated one, often irreversible",
                "C": "The migration of corals to deeper water to escape heat",
                "D": "A temporary increase in coral growth following a bleaching event"
            },
            "correct": "B",
            "feedback_correct": "Correct. A phase shift is an abrupt, often irreversible transition where algae overgrow dead and weakened coral, preventing recolonization.",
            "feedback_incorrect": "A phase shift occurs when a reef transitions from coral-dominated to algae-dominated. Algae colonize dead coral surfaces and prevent new coral larvae from settling, locking the reef in a degraded state."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows bleaching events occurring every 6 years, but full coral recovery requires 10-15 years. What mathematical relationship makes a death spiral inevitable under these conditions?",
            "choices": {
                "A": "The ratio of bleaching frequency to recovery time is less than 1, allowing gradual improvement",
                "B": "The ratio of stress frequency to recovery time exceeds 1, meaning each bleaching event hits a reef that has not recovered from the previous one, compounding damage",
                "C": "The absolute temperature during bleaching determines recovery time regardless of frequency",
                "D": "Bleaching frequency has no relationship to long-term reef health"
            },
            "correct": "B",
            "feedback_correct": "Correct. When stress frequency exceeds recovery capacity (ratio > 1), damage accumulates with each event. A 6-year bleaching cycle with 10-15-year recovery means each event strikes an increasingly weakened reef.",
            "feedback_incorrect": "The death spiral is mathematically driven by the stress-to-recovery ratio. If bleaching occurs every 6 years but recovery takes 10-15 years, each new event hits a reef that is only 40-60% recovered, creating cumulative damage."
        },
        {
            "question": "A student's model shows that after a phase shift from coral to algae dominance, Reef Structural Complexity and Marine Biodiversity both collapse. Why is this phase shift considered largely irreversible on human timescales?",
            "choices": {
                "A": "Algae grow so slowly that it takes centuries for them to be replaced",
                "B": "Algae overgrow dead coral surfaces, preventing coral larvae from settling and recolonizing, while the three-dimensional reef structure erodes without living coral to maintain it",
                "C": "Ocean temperatures never decrease, so bleaching conditions are permanent",
                "D": "Marine species that leave degraded reefs can never navigate back to them"
            },
            "correct": "B",
            "feedback_correct": "Correct. Algae act as a biological barrier to coral recolonization, and without living coral to build and maintain reef structure, the three-dimensional habitat erodes, eliminating the niches that supported biodiversity.",
            "feedback_incorrect": "Phase shifts are self-reinforcing: algae colonize dead coral surfaces and block new coral settlement, while the limestone reef skeleton erodes without living coral to maintain it. The physical habitat is lost along with its biological community."
        },
        {
            "question": "The Great Barrier Reef experienced mass bleaching events in 2016, 2017, 2020, 2022, and 2024. Using the model's framework, which prediction is best supported by this data?",
            "choices": {
                "A": "The reef is demonstrating natural resilience by surviving multiple events",
                "B": "Bleaching frequency has increased to every 1-2 years, virtually eliminating recovery windows and placing the reef on a trajectory toward widespread phase shift",
                "C": "The reef has already fully shifted to algae dominance",
                "D": "Future bleaching events will be less severe because the most vulnerable corals have already died"
            },
            "correct": "B",
            "feedback_correct": "Correct. Five mass bleaching events in 8 years gives a frequency of approximately every 1.6 years, far exceeding the 10-15 year recovery requirement, indicating progressive degradation.",
            "feedback_incorrect": "Five mass bleaching events in 8 years represents a bleaching frequency far shorter than the 10-15 years needed for recovery. The model predicts that sustained high-frequency bleaching will drive the reef toward irreversible phase shift."
        },
        {
            "question": "A conservation team proposes reducing local stressors (pollution, overfishing) to help a reef survive warming. According to the model, why might this be necessary but insufficient as a standalone strategy?",
            "choices": {
                "A": "Local stressors have no measurable effect on reef health",
                "B": "Reducing local stressors improves baseline reef resilience and recovery capacity, but cannot prevent bleaching if sea surface temperatures continue rising above thermal stress thresholds",
                "C": "Overfishing actually helps reefs by reducing the number of coral-eating organisms",
                "D": "Pollution makes corals more resistant to temperature changes"
            },
            "correct": "B",
            "feedback_correct": "Correct. Local stressor reduction improves coral health and recovery speed, but the primary driver of bleaching is thermal stress from global ocean warming, which local management cannot control.",
            "feedback_incorrect": "The model shows two scales of threat: local stressors (pollution, overfishing) degrade reef resilience, while global warming drives thermal bleaching. Addressing local stressors helps corals recover faster, but if warming continues, bleaching will still overwhelm recovery capacity."
        },
        {
            "question": "In the model, Algae Competition increases as coral dies. This creates a feedback loop because algae prevent coral recolonization, which allows more algae to grow. What type of feedback is this, and what is its significance?",
            "choices": {
                "A": "Negative feedback that stabilizes the reef at a healthy equilibrium",
                "B": "Positive feedback that accelerates reef degradation by reinforcing the conditions that caused the initial coral loss",
                "C": "No feedback; algae and coral dynamics are independent of each other",
                "D": "Negative feedback that eventually reverses the phase shift"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is a positive (self-reinforcing) feedback loop: coral death enables algae growth, which prevents coral recovery, which leads to more coral death. It accelerates the phase shift.",
            "feedback_incorrect": "This is a positive feedback loop: it amplifies change in one direction. As coral dies, algae colonize the space and prevent coral recolonization, ensuring more coral loss and more algae growth. This self-reinforcing cycle drives the phase shift."
        }
    ]
}

# ---------------------------------------------------------------------------
# L04 — When Permafrost Melts, What Wakes Up? (HS-ESS2-4, HS-ESS2-6)
# ---------------------------------------------------------------------------
L04_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is permafrost?",
            "choices": {
                "A": "Ice that covers the Arctic Ocean during winter months",
                "B": "Ground that has remained at or below 0 degrees Celsius continuously for at least two years",
                "C": "Glaciers that never melt, even in summer",
                "D": "Frozen precipitation that accumulates on mountain peaks"
            },
            "correct": "B",
            "feedback_correct": "Correct. Permafrost is soil, rock, or sediment that has stayed frozen (at or below 0 degrees C) continuously for at least two consecutive years.",
            "feedback_incorrect": "Permafrost refers to ground (soil, rock, sediment) that remains frozen continuously for at least two years. It is found primarily in Arctic and sub-Arctic regions and can extend hundreds of meters deep."
        },
        {
            "question": "Approximately how much carbon is stored in Arctic permafrost compared to the current atmosphere?",
            "choices": {
                "A": "About 10% as much as the atmosphere",
                "B": "About the same amount as the atmosphere",
                "C": "About twice as much as the atmosphere",
                "D": "About ten times as much as the atmosphere"
            },
            "correct": "C",
            "feedback_correct": "Correct. Arctic permafrost contains approximately 1,500 billion tons of carbon, roughly twice the amount currently in the entire atmosphere.",
            "feedback_incorrect": "Permafrost stores approximately 1,500 billion tons of organic carbon accumulated over thousands of years. This is roughly double the carbon currently in the atmosphere (~880 billion tons)."
        },
        {
            "question": "In climate science, what does a 'positive feedback loop' mean?",
            "choices": {
                "A": "A beneficial process that improves environmental conditions",
                "B": "A self-reinforcing cycle where an initial change triggers processes that amplify that change further",
                "C": "A process that stabilizes temperature by counteracting warming",
                "D": "An accurate climate model prediction that proves correct"
            },
            "correct": "B",
            "feedback_correct": "Correct. In systems science, 'positive' means self-reinforcing, not 'good.' A positive feedback amplifies the initial change.",
            "feedback_incorrect": "In systems science, 'positive feedback' means self-reinforcing: an initial change triggers responses that amplify the original change further. This does not mean beneficial; it means the effect keeps growing."
        },
        {
            "question": "Why is the Arctic warming faster than the global average?",
            "choices": {
                "A": "The Arctic receives more direct sunlight than other regions",
                "B": "Arctic amplification occurs because melting ice exposes darker surfaces that absorb more heat, reinforcing further warming",
                "C": "Most greenhouse gas emissions are produced in Arctic countries",
                "D": "The Arctic's thin atmosphere traps heat more efficiently"
            },
            "correct": "B",
            "feedback_correct": "Correct. Arctic amplification is driven largely by the ice-albedo feedback: as reflective ice melts, darker ocean and land surfaces absorb more solar energy, accelerating warming.",
            "feedback_incorrect": "Arctic amplification occurs because the loss of reflective ice and snow exposes darker surfaces (ocean, land) that absorb more solar energy instead of reflecting it, creating a feedback loop that accelerates regional warming."
        },
        {
            "question": "When organic matter in permafrost thaws, what gases are released and why?",
            "choices": {
                "A": "Oxygen is released because frozen plants resume photosynthesis",
                "B": "Nitrogen is released because permafrost is primarily composed of frozen air",
                "C": "CO2 and methane are released because soil microbes decompose the thawed organic matter",
                "D": "Water vapor is the only gas released as ice melts"
            },
            "correct": "C",
            "feedback_correct": "Correct. When permafrost thaws, soil microbes become active and decompose the previously frozen organic material, producing CO2 in dry conditions and methane in waterlogged conditions.",
            "feedback_incorrect": "Thawed permafrost exposes ancient organic matter to microbial decomposition. In dry conditions, microbes produce CO2; in wet, oxygen-poor conditions, they produce methane, which is about 80 times more potent as a greenhouse gas over 20 years."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that at +4 degrees C Arctic warming, Carbon Release Rate accelerates nonlinearly due to thermokarst formation. Which systems-level explanation best accounts for this nonlinear acceleration?",
            "choices": {
                "A": "Higher temperatures make microbes less efficient at decomposing organic matter",
                "B": "Thermokarst collapse exposes massive volumes of permafrost to warm lake water and air simultaneously, creating localized carbon release hotspots that accelerate thaw far beyond what gradual surface warming alone would produce",
                "C": "At +4 degrees C, all permafrost has already thawed, so carbon release stops",
                "D": "Wind patterns shift at higher temperatures, cooling the Arctic surface"
            },
            "correct": "B",
            "feedback_correct": "Correct. Thermokarst is a threshold process: once ice-rich permafrost begins collapsing, it exposes far more frozen carbon to thawing conditions than gradual surface warming, creating a nonlinear acceleration.",
            "feedback_incorrect": "Thermokarst formation creates a step-change in thaw dynamics. Ground collapse forms lakes and sinkholes that expose permafrost to warm water on multiple surfaces simultaneously, dramatically accelerating carbon release beyond the rate predicted by surface warming alone."
        },
        {
            "question": "A student argues that permafrost carbon feedback is not concerning because 'we can just stop emitting fossil fuels.' Which model finding most directly challenges this reasoning?",
            "choices": {
                "A": "Fossil fuel emissions are too difficult to reduce for political reasons",
                "B": "Once permafrost thaw becomes self-sustaining, carbon release continues regardless of human emission decisions because the feedback loop operates independently of anthropogenic sources",
                "C": "Permafrost carbon is a different type of carbon than fossil fuel carbon",
                "D": "Stopping fossil fuel emissions would cause immediate global cooling"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is the critical distinction: unlike fossil fuel emissions, which humans can choose to stop, permafrost carbon feedback is a natural process that becomes self-sustaining once tipping points are crossed.",
            "feedback_incorrect": "The model reveals that permafrost carbon feedback is fundamentally different from fossil fuel emissions because it is a natural, self-reinforcing process. Once thaw releases enough greenhouse gas to sustain further warming and thaw, it continues regardless of human policy."
        },
        {
            "question": "The model includes both CO2 and methane release from permafrost. Why is the methane pathway particularly concerning even though methane concentrations are much lower than CO2?",
            "choices": {
                "A": "Methane is approximately 80 times more potent as a greenhouse gas than CO2 over a 20-year period, meaning small releases have outsized warming effects",
                "B": "Methane destroys the ozone layer, which is a more urgent problem than warming",
                "C": "Methane is only released in dry conditions, which are becoming more common",
                "D": "Methane release from permafrost has already exceeded fossil fuel methane emissions"
            },
            "correct": "A",
            "feedback_correct": "Correct. Methane's global warming potential is approximately 80x that of CO2 over 20 years, so even relatively small methane releases from waterlogged permafrost have significant warming impacts.",
            "feedback_incorrect": "Methane has a global warming potential roughly 80 times greater than CO2 over a 20-year timeframe. This means methane released from waterlogged thawing permafrost has an outsized impact on warming, even at much lower concentrations."
        },
        {
            "question": "Comparing the +2 degrees C and +6 degrees C Arctic scenarios, the model shows that permafrost carbon release at +2 degrees C adds modest warming, while at +6 degrees C the feedback loop appears to become self-sustaining. What is the most important implication for climate policy?",
            "choices": {
                "A": "Climate policy is irrelevant because warming has already passed the tipping point",
                "B": "Emission reductions must be aggressive enough to keep Arctic warming below the threshold where the permafrost feedback becomes self-reinforcing, because beyond that point, additional warming occurs regardless of human action",
                "C": "All climate policy should focus exclusively on the Arctic region",
                "D": "The difference between +2 and +6 degrees C is too small to matter"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that there is a critical threshold between manageable and self-sustaining permafrost feedback, making it imperative to reduce emissions fast enough to stay below that threshold.",
            "feedback_incorrect": "The model identifies a critical threshold between +2 and +6 degrees C Arctic warming where permafrost feedback transitions from manageable to self-sustaining. Policy must target staying below this threshold, because beyond it, the carbon release cannot be stopped by human action."
        },
        {
            "question": "Most current climate models have historically underestimated permafrost carbon feedback. What does this suggest about the adequacy of current global emission reduction targets?",
            "choices": {
                "A": "Current targets are likely sufficient because models are always conservative",
                "B": "Current targets may need to be more aggressive to account for the additional warming from permafrost carbon release that was not fully included in the models used to set those targets",
                "C": "Emission targets should remain unchanged because permafrost is a minor carbon source",
                "D": "Model underestimation means permafrost feedback is actually less severe than reported"
            },
            "correct": "B",
            "feedback_correct": "Correct. If the models used to determine emission targets underestimated permafrost feedback, then those targets allow more warming than intended and may need to be tightened.",
            "feedback_incorrect": "If the climate models that informed emission reduction targets did not fully account for permafrost carbon feedback, the actual warming produced by those targets will exceed projections. This means targets may need to be more aggressive to achieve the same temperature goals."
        }
    ]
}

# ---------------------------------------------------------------------------
# L05 — Can We Reverse Deforestation Before It's Too Late? (HS-LS2-4, HS-ESS3-3)
# ---------------------------------------------------------------------------
L05_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What makes a forest a 'carbon sink'?",
            "choices": {
                "A": "The forest floor absorbs carbon from underground rock formations",
                "B": "Trees absorb more CO2 through photosynthesis than the forest releases through respiration and decomposition",
                "C": "Forests produce carbon monoxide, which traps less heat than CO2",
                "D": "Carbon sinks are man-made reservoirs installed in forests"
            },
            "correct": "B",
            "feedback_correct": "Correct. A carbon sink absorbs more CO2 than it releases. Intact forests absorb about 2.6 billion tons of CO2 annually through photosynthesis.",
            "feedback_incorrect": "A forest is a carbon sink when its net carbon uptake (via photosynthesis) exceeds its net carbon release (via respiration and decomposition). Intact forests globally absorb approximately 2.6 billion tons of CO2 per year."
        },
        {
            "question": "How do tropical forests contribute to their own rainfall?",
            "choices": {
                "A": "Tree canopies physically block rain from evaporating, trapping moisture",
                "B": "Trees pump water from soil and release it as vapor through evapotranspiration, generating clouds and rainfall",
                "C": "Forests produce chemicals that seed cloud formation from industrial pollutants",
                "D": "Tropical forests do not significantly affect local rainfall patterns"
            },
            "correct": "B",
            "feedback_correct": "Correct. Through evapotranspiration, tropical forests create up to 50% of their own precipitation by recycling water from soil to atmosphere.",
            "feedback_incorrect": "Tropical trees absorb water through their roots and release it as vapor through leaf pores (evapotranspiration). This moisture forms clouds that produce rainfall, recycling up to 50% of the forest's precipitation."
        },
        {
            "question": "What is 'savannification' in the context of tropical forests?",
            "choices": {
                "A": "The natural growth cycle of savanna grasslands",
                "B": "The irreversible transition of a tropical rainforest to a savanna or grassland when tree cover drops below a critical threshold",
                "C": "A conservation strategy that replaces forests with grasslands",
                "D": "The seasonal drying of tropical forests during winter months"
            },
            "correct": "B",
            "feedback_correct": "Correct. Savannification is the irreversible loss of tropical rainforest structure and function, triggered when deforestation reduces tree cover below the threshold needed to sustain the forest's rainfall cycle.",
            "feedback_incorrect": "Savannification occurs when deforestation reduces forest cover below the threshold needed to maintain the evapotranspiration-rainfall cycle. Without enough trees to generate moisture, the forest dries out and transitions irreversibly to savanna."
        },
        {
            "question": "Approximately what percentage of the Amazon rainforest has already been deforested?",
            "choices": {
                "A": "About 5%",
                "B": "About 17%",
                "C": "About 40%",
                "D": "About 65%"
            },
            "correct": "B",
            "feedback_correct": "Correct. The Amazon has lost approximately 17% of its original forest, with scientists estimating the tipping point at 20-25% loss.",
            "feedback_incorrect": "Approximately 17% of the Amazon rainforest has been cleared. Scientists estimate the tipping point for irreversible savannification at 20-25% loss, meaning the Amazon is dangerously close to a critical threshold."
        },
        {
            "question": "If a region loses 30% of its forest cover, how might this affect the local fire risk?",
            "choices": {
                "A": "Fire risk decreases because there is less fuel to burn",
                "B": "Fire risk remains unchanged because fires depend only on temperature",
                "C": "Fire risk increases because reduced evapotranspiration dries out the remaining forest, and fragmented forest edges are more exposed",
                "D": "Fire risk increases only in non-tropical forests"
            },
            "correct": "C",
            "feedback_correct": "Correct. Deforestation reduces rainfall via decreased evapotranspiration, drying out remaining forest. Fragmented edges are exposed to drying winds and human ignition sources, dramatically increasing fire risk.",
            "feedback_incorrect": "Deforestation reduces local rainfall by disrupting evapotranspiration, drying out remaining forest. Forest edges exposed by fragmentation are particularly vulnerable to desiccation and fire, which can destroy more forest in a self-reinforcing cycle."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that at 25% Amazon deforestation, Regional Rainfall drops below a threshold and Fire Susceptibility spikes. Even when Reforestation Rate is set to match Deforestation Rate, the forest continues to decline. What best explains this result?",
            "choices": {
                "A": "Reforestation seedlings consume more water than mature trees",
                "B": "Once the rainfall-fire feedback loop engages, the system is self-reinforcing: reduced forest lowers rainfall, which increases fire, which destroys more forest, regardless of replanting efforts",
                "C": "Deforestation and reforestation rates cancel out perfectly, so the forest should stabilize",
                "D": "The model is flawed because reforestation always restores forest function immediately"
            },
            "correct": "B",
            "feedback_correct": "Correct. The tipping point is where the positive feedback loop (less forest leads to less rain leads to more fire leads to less forest) becomes self-reinforcing and overpowers reforestation efforts.",
            "feedback_incorrect": "Beyond the tipping point, the deforestation-drought-fire feedback loop operates independently of human reforestation efforts. Reduced forest cover decreases evapotranspiration, lowering rainfall, which dries out remaining forest, increasing fire risk in a self-sustaining cycle."
        },
        {
            "question": "A policy team proposes planting 10 million hectares of new forest per year to fully offset 10 million hectares of annual deforestation. The model shows this strategy fails over 30 years. Which timescale mismatch is responsible?",
            "choices": {
                "A": "Newly planted trees grow faster than expected, overshooting carbon targets",
                "B": "Deforestation releases stored carbon instantly, but replanted trees take 20-40 years to reach carbon sequestration maturity, creating a decades-long carbon debt",
                "C": "Reforestation costs decrease over time, making the program unsustainable",
                "D": "Deforestation only affects carbon storage, not water cycles"
            },
            "correct": "B",
            "feedback_correct": "Correct. A chainsaw releases centuries of stored carbon in hours, while a seedling takes 20-40 years to reach maturity. This asymmetry creates an unavoidable carbon debt even with equal area replanting.",
            "feedback_incorrect": "The fundamental timescale mismatch: deforestation releases stored carbon almost instantly, but a newly planted tree needs 20-40 years to reach the carbon sequestration capacity of the mature tree it replaced. Hectare-for-hectare replacement does not equal carbon-for-carbon replacement."
        },
        {
            "question": "The model reveals that forests generate up to 50% of their own rainfall. A student concludes that any amount of deforestation will proportionally reduce rainfall. Why is this linear interpretation incorrect?",
            "choices": {
                "A": "Rainfall is entirely controlled by ocean temperatures, not forests",
                "B": "The system exhibits threshold behavior: below a critical forest cover level, the evapotranspiration-rainfall cycle cannot sustain itself, causing a rapid nonlinear collapse rather than a gradual proportional decline",
                "C": "Deforestation actually increases rainfall because bare ground reflects more heat",
                "D": "Forest rainfall recycling only matters in temperate, not tropical, forests"
            },
            "correct": "B",
            "feedback_correct": "Correct. The forest-rainfall relationship has threshold dynamics. Above the threshold, the cycle is self-sustaining with gradual decline. Below it, the cycle collapses rapidly because the remaining forest cannot generate enough moisture.",
            "feedback_incorrect": "The model shows nonlinear threshold behavior: the evapotranspiration-rainfall system is self-sustaining above a critical forest cover threshold but collapses below it. The transition from forest to savanna is abrupt, not proportional to deforestation area."
        },
        {
            "question": "An economist argues that converting forest to agriculture is rational because farmland generates immediate revenue. Using the model, which systems-level analysis best addresses this argument?",
            "choices": {
                "A": "Forest conservation never generates economic value",
                "B": "While clearing forest is individually rational for landowners, the ecosystem services provided by intact forest (rainfall generation, carbon storage, biodiversity, flood control) are worth far more than agricultural revenue but are externalities not captured by market prices",
                "C": "Agricultural revenue always exceeds the value of ecosystem services",
                "D": "Deforestation has no economic consequences beyond the cleared area"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is a tragedy of the commons: individual economic incentives favor clearing, but the collective value of intact forest ecosystem services far exceeds agricultural revenue when properly accounted for.",
            "feedback_incorrect": "The model demonstrates a classic externality problem: the farmer captures agricultural revenue but the costs of lost ecosystem services (rainfall, carbon storage, biodiversity) are borne by everyone. The total value of ecosystem services exceeds agricultural value, but markets fail to reflect this."
        },
        {
            "question": "Based on the model, which combination of strategies would be most effective at preventing the Amazon from crossing its savannification tipping point?",
            "choices": {
                "A": "Focus exclusively on reforestation of already-cleared areas",
                "B": "Allow continued deforestation but plant twice as many trees elsewhere",
                "C": "Halt deforestation of intact forest to prevent crossing the threshold, while simultaneously reforesting degraded areas and creating economic alternatives that make standing forest more valuable than cleared land",
                "D": "Accept savannification as inevitable and adapt agricultural practices"
            },
            "correct": "C",
            "feedback_correct": "Correct. The model shows that preventing tipping point crossing requires stopping intact forest loss (the primary threat), restoring degraded areas, and changing the economic calculus that drives deforestation.",
            "feedback_incorrect": "The model indicates that the most effective strategy addresses all three dimensions: stopping further loss of intact forest (to stay above the threshold), restoring degraded land (to rebuild the evapotranspiration cycle), and restructuring economic incentives (to make conservation economically viable)."
        }
    ]
}

# ---------------------------------------------------------------------------
# L06 — Why Is Clean Water Becoming Scarce? (HS-ESS2-5, HS-ESS3-1)
# ---------------------------------------------------------------------------
L06_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Earth is approximately 70% water. What percentage of Earth's total water is accessible freshwater?",
            "choices": {
                "A": "About 10%",
                "B": "About 2.5%",
                "C": "About 0.5%",
                "D": "About 25%"
            },
            "correct": "C",
            "feedback_correct": "Correct. Only about 0.5% of Earth's water is accessible freshwater. The rest is saltwater (97.5%) or frozen in ice caps and glaciers.",
            "feedback_incorrect": "Although Earth has vast water, 97.5% is saltwater and about 2% is frozen in ice caps and glaciers. Only about 0.5% is accessible freshwater in rivers, lakes, and reachable groundwater."
        },
        {
            "question": "What is an aquifer?",
            "choices": {
                "A": "A man-made reservoir for storing treated water",
                "B": "An underground layer of rock or sediment that holds and transmits groundwater",
                "C": "A type of water treatment plant",
                "D": "A dam built across a river to store water"
            },
            "correct": "B",
            "feedback_correct": "Correct. An aquifer is a geological formation (rock, gravel, sand) that stores groundwater in pore spaces and can transmit it to wells and springs.",
            "feedback_incorrect": "An aquifer is a natural underground formation of permeable rock, sand, or gravel that holds groundwater. Wells are drilled into aquifers to access this water for drinking, irrigation, and industry."
        },
        {
            "question": "Which sector consumes the largest share of global freshwater withdrawals?",
            "choices": {
                "A": "Residential and municipal use (drinking, bathing, toilets)",
                "B": "Industrial manufacturing",
                "C": "Agriculture (irrigation)",
                "D": "Energy production (power plant cooling)"
            },
            "correct": "C",
            "feedback_correct": "Correct. Agriculture accounts for approximately 70% of all global freshwater withdrawals, primarily for irrigation.",
            "feedback_incorrect": "Agriculture consumes about 70% of all freshwater withdrawn globally. Irrigation is by far the largest use, with much of it using inefficient flood methods that waste 40-60% of applied water."
        },
        {
            "question": "What does 'water stress' mean for a region?",
            "choices": {
                "A": "The region receives too much rainfall, causing flooding",
                "B": "Water demand exceeds available supply, or poor water quality restricts use",
                "C": "Water infrastructure requires expensive repairs",
                "D": "The region has more surface water than groundwater"
            },
            "correct": "B",
            "feedback_correct": "Correct. A region is water-stressed when demand approaches or exceeds the available supply, or when water quality is too poor for intended uses.",
            "feedback_incorrect": "Water stress occurs when the demand for freshwater (from population, agriculture, industry) approaches or exceeds the available supply. Regions where more than 40% of available water is withdrawn are classified as severely stressed."
        },
        {
            "question": "Why might depleting an aquifer be considered 'functionally irreversible'?",
            "choices": {
                "A": "Empty aquifers immediately fill with saltwater that cannot be removed",
                "B": "Many major aquifers accumulated water over thousands to millions of years, and natural recharge replaces less than 1% of withdrawals annually",
                "C": "Government regulations permanently prevent refilling depleted aquifers",
                "D": "Aquifer rock collapses when water is removed, destroying the formation"
            },
            "correct": "B",
            "feedback_correct": "Correct. Major agricultural aquifers like the Ogallala formed over millions of years. Current extraction rates far exceed natural recharge, making depletion effectively permanent on human timescales.",
            "feedback_incorrect": "Many large aquifers are 'fossil water' systems that accumulated over geological timescales. When extraction vastly exceeds the tiny natural recharge rate, the aquifer is being mined like a non-renewable resource. Refilling would take thousands of years."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that the Ogallala Aquifer has lost 30% of its volume in 60 years while natural recharge replaces less than 1% of annual withdrawals. A farmer proposes 'just pumping less.' At what extraction rate does the model show the aquifer stabilizes?",
            "choices": {
                "A": "Extraction must be reduced to 50% of current levels",
                "B": "Extraction must equal the natural recharge rate, which would require reducing current withdrawals by approximately 99%",
                "C": "Any reduction in pumping will stabilize the aquifer within 10 years",
                "D": "The aquifer cannot stabilize because climate change is increasing recharge"
            },
            "correct": "B",
            "feedback_correct": "Correct. For the aquifer to stabilize, extraction cannot exceed recharge. Since recharge is less than 1% of current withdrawal, extraction would need to drop by roughly 99%, which is practically impossible without completely transforming regional agriculture.",
            "feedback_incorrect": "The model shows sustainability requires withdrawal equals recharge. Since natural recharge is less than 1% of current extraction, stabilization requires a near-complete halt to pumping. This reveals the magnitude of the problem: current agriculture depends on mining a non-renewable resource."
        },
        {
            "question": "The model demonstrates a cascading failure: aquifer depletion reduces food production, food shortages drive migration, and migration concentrates populations in cities facing their own water stress. What systems concept does this cascade illustrate?",
            "choices": {
                "A": "Negative feedback that stabilizes the system through migration",
                "B": "A positive feedback loop where each system failure worsens conditions for the connected systems, compounding the crisis",
                "C": "An isolated local problem with no broader systemic effects",
                "D": "A self-correcting market response to resource scarcity"
            },
            "correct": "B",
            "feedback_correct": "Correct. This cascade is a positive feedback loop across coupled systems: water depletion drives food loss, which drives migration, which intensifies urban water stress, worsening conditions across all connected systems.",
            "feedback_incorrect": "The cascade demonstrates how interconnected systems amplify failures: aquifer depletion is not just a water problem but triggers food insecurity, migration, and urban stress in a compounding positive feedback loop that affects multiple sectors simultaneously."
        },
        {
            "question": "A student proposes desalination as the solution to global water scarcity. Based on the model, which limitation most significantly constrains this approach?",
            "choices": {
                "A": "Desalination technology does not yet exist at commercial scale",
                "B": "Desalination is energy-intensive and expensive ($0.50-$2.00/m3), currently supplies less than 1% of global freshwater, and generates concentrated brine waste that harms marine ecosystems",
                "C": "Desalinated water is unsafe for irrigation",
                "D": "Only coastal cities can benefit, and most water stress occurs inland"
            },
            "correct": "B",
            "feedback_correct": "Correct. Desalination faces scalability challenges: high energy costs, limited current contribution (<1% of global supply), and environmental impacts from brine disposal make it a supplementary solution, not a replacement for sustainable groundwater management.",
            "feedback_incorrect": "While desalination works technically, it currently provides less than 1% of global freshwater and faces major scalability constraints: high energy requirements, significant cost per unit volume, and environmental damage from concentrated brine waste discharged into marine environments."
        },
        {
            "question": "The model's 'virtual water' concept reveals that a kilogram of beef requires approximately 15,000 liters of water. How does this inform a systems-level approach to water scarcity?",
            "choices": {
                "A": "Virtual water is theoretical and has no practical policy implications",
                "B": "Shifting dietary patterns and agricultural choices can dramatically reduce water demand because food production accounts for 70% of withdrawals, and water intensity varies enormously between crop and livestock types",
                "C": "Consumers should only eat locally grown food to reduce virtual water",
                "D": "Beef production should be banned in all water-stressed regions"
            },
            "correct": "B",
            "feedback_correct": "Correct. Virtual water analysis reveals that demand-side changes (dietary shifts, crop choice, agricultural efficiency) can achieve far greater water savings than supply-side engineering because agriculture dominates consumption.",
            "feedback_incorrect": "Understanding virtual water shows that water scarcity is partly a demand problem. Since agriculture uses 70% of freshwater and water intensity varies widely (15,000 L/kg beef vs. 1,800 L/kg grain), dietary and crop shifts can yield massive water savings."
        },
        {
            "question": "The model shows that increasing Population and Agricultural Demand by 50% while decreasing Natural Recharge Rate by 20% (due to climate change) causes Aquifer Water Level to crash decades sooner than either factor alone. What does this reveal about compounding stressors in water systems?",
            "choices": {
                "A": "Population growth and climate change affect water systems independently",
                "B": "The interaction between rising demand and declining supply creates a nonlinear acceleration of depletion because both forces simultaneously widen the gap between extraction and recharge",
                "C": "Climate change is the only significant factor in water scarcity",
                "D": "Population growth can always be offset by more efficient irrigation technology"
            },
            "correct": "B",
            "feedback_correct": "Correct. When demand rises while supply falls simultaneously, the depletion gap widens from both sides, creating a multiplicative effect that accelerates collapse far beyond what either stressor would cause independently.",
            "feedback_incorrect": "Compounding stressors are worse than additive: rising demand and declining recharge simultaneously widen the extraction-recharge gap, causing nonlinear acceleration. The aquifer depletes much faster under compound stress than under either factor alone."
        }
    ]
}

# ---------------------------------------------------------------------------
# L07 — The Plastic Paradox (HS-ESS3-4, HS-LS2-6)
# ---------------------------------------------------------------------------
L07_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What are microplastics?",
            "choices": {
                "A": "A type of biodegradable plastic that breaks down in the ocean within weeks",
                "B": "Plastic fragments smaller than 5 millimeters, created by breakdown of larger plastic items",
                "C": "Microscopic organisms that consume plastic waste",
                "D": "Plastic packaging designed to be as small as possible to reduce waste"
            },
            "correct": "B",
            "feedback_correct": "Correct. Microplastics are plastic fragments smaller than 5 mm, produced when larger plastic items break down through UV exposure and physical weathering.",
            "feedback_incorrect": "Microplastics are plastic fragments less than 5 mm in diameter. They form when UV radiation and physical forces break larger plastic items into progressively smaller pieces. An estimated 14 million tons enter the ocean annually."
        },
        {
            "question": "What is biomagnification?",
            "choices": {
                "A": "The use of magnifying equipment to study small organisms",
                "B": "The increasing concentration of a substance at each successive level in a food chain",
                "C": "The rapid growth of organisms exposed to plastic pollution",
                "D": "The expansion of biological populations in polluted areas"
            },
            "correct": "B",
            "feedback_correct": "Correct. Biomagnification is the progressive increase in concentration of a substance (like toxins on microplastics) at each trophic level as predators consume contaminated prey.",
            "feedback_incorrect": "Biomagnification occurs when a toxic substance becomes more concentrated at each step of the food chain. A toxin at 1 ppm in plankton can reach 10,000 ppm in a top predator through cumulative dietary exposure."
        },
        {
            "question": "What is an ocean gyre, and how does it relate to plastic pollution?",
            "choices": {
                "A": "A deep-sea volcano that incinerates plastic waste on the ocean floor",
                "B": "A large system of circular ocean currents that traps floating debris in accumulation zones",
                "C": "A man-made barrier designed to contain oil spills and plastic waste",
                "D": "A type of marine organism that feeds exclusively on plastic"
            },
            "correct": "B",
            "feedback_correct": "Correct. Ocean gyres are large circular current systems that sweep floating debris toward their calm centers, creating massive accumulation zones like the Great Pacific Garbage Patch.",
            "feedback_incorrect": "Ocean gyres are circular current systems driven by wind, Coriolis effect, and continental boundaries. They sweep floating debris inward, trapping it in accumulation zones. The Great Pacific Garbage Patch covers an area twice the size of Texas."
        },
        {
            "question": "Does plastic truly biodegrade in the ocean?",
            "choices": {
                "A": "Yes, most plastic biodegrades within 5-10 years in saltwater",
                "B": "No, plastic photodegrades into ever-smaller fragments but never fully breaks down on human timescales",
                "C": "Yes, ocean bacteria have evolved to completely consume plastic",
                "D": "Plastic only degrades in warm tropical waters"
            },
            "correct": "B",
            "feedback_correct": "Correct. Plastic does not biodegrade. UV light and mechanical forces break it into smaller and smaller fragments, but every piece of plastic ever produced still exists in some form.",
            "feedback_incorrect": "Plastic does not biodegrade in the ocean. It photodegrades, breaking into smaller and smaller pieces through UV exposure and mechanical weathering, but the polymer material persists indefinitely. Every piece of plastic ever made still exists in some form."
        },
        {
            "question": "Approximately how much plastic enters the ocean each year?",
            "choices": {
                "A": "About 1,000 metric tons",
                "B": "About 100,000 metric tons",
                "C": "About 11 million metric tons",
                "D": "About 1 billion metric tons"
            },
            "correct": "C",
            "feedback_correct": "Correct. Approximately 11 million metric tons of plastic enter the ocean each year, projected to triple by 2040 without major intervention.",
            "feedback_incorrect": "An estimated 11 million metric tons of plastic enter the ocean annually through inadequate waste management, industrial discharge, and product degradation. This figure is projected to triple by 2040 without significant intervention."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that even after reducing plastic input by 50%, Marine Ecosystem Health takes decades to improve. Which characteristic of microplastic pollution best explains this delay?",
            "choices": {
                "A": "Ocean cleanup technology is too slow to remove accumulated plastic",
                "B": "Existing microplastics persist for centuries because they do not biodegrade, and ocean gyres trap them in permanent accumulation zones with no natural flushing mechanism",
                "C": "Marine organisms prefer eating microplastics over natural food",
                "D": "Reducing production causes economic disruption that harms coastal communities"
            },
            "correct": "B",
            "feedback_correct": "Correct. The lag exists because microplastics already in the ocean persist essentially forever and gyres have no mechanism to flush accumulated debris. Even with reduced input, the existing stock continues contaminating food webs.",
            "feedback_incorrect": "The delay is caused by the persistence of existing contamination. Microplastics already in the ocean do not degrade, and gyre circulation traps them indefinitely. Reducing input prevents additional contamination but does not remove what is already there."
        },
        {
            "question": "The model demonstrates that toxin concentrations increase by factors of 10-100 at each trophic level through biomagnification. If zooplankton contain microplastic-associated toxins at 1 part per billion, what concentration might be found in a fourth-level predator?",
            "choices": {
                "A": "4 parts per billion (additive increase)",
                "B": "1,000 to 1,000,000 parts per billion (multiplicative increase across three trophic level jumps)",
                "C": "1 part per billion (concentration stays constant)",
                "D": "Less than 1 part per billion (organisms metabolize toxins)"
            },
            "correct": "B",
            "feedback_correct": "Correct. With 10-100x magnification at each trophic level, three jumps from zooplankton to a 4th-level predator could concentrate toxins by 10^3 to 10^6, reaching parts per million or higher.",
            "feedback_incorrect": "Biomagnification is multiplicative, not additive. With 10-100x concentration increase at each trophic level, three jumps produce 10^3 to 10^6 increase (1,000 to 1,000,000x). Starting at 1 ppb, a 4th-level predator could contain 1-1,000 ppm."
        },
        {
            "question": "The model compares source reduction versus ocean cleanup at reducing gyre plastic concentration. Why does source reduction vastly outperform cleanup in the model?",
            "choices": {
                "A": "Cleanup technology does not exist for ocean environments",
                "B": "Fragmentation produces trillions of particles too small to capture, and the inflow rate of 11 million tons per year overwhelms the removal capacity of current cleanup systems at approximately 10,000 tons per year",
                "C": "Source reduction is cheaper but less effective per ton removed",
                "D": "Cleanup operations accidentally harm more marine life than plastic does"
            },
            "correct": "B",
            "feedback_correct": "Correct. The math is decisive: inflow exceeds cleanup capacity by roughly 1,000:1, and fragmentation creates particles too small for collection. Prevention outperforms remediation by orders of magnitude.",
            "feedback_incorrect": "Source reduction outperforms cleanup because of scale: 11 million tons enter annually versus ~10,000 tons that can be removed. Additionally, fragmentation creates trillions of particles below the size threshold for collection technology, making cleanup of existing microplastics physically impossible."
        },
        {
            "question": "Microplastics have been found in human blood, placental tissue, and deep-sea sediments. What does this global distribution pattern reveal about the plastic pollution system?",
            "choices": {
                "A": "Microplastic contamination is limited to areas near plastic production facilities",
                "B": "The contamination is already globally pervasive, crossing biological barriers (cell membranes, placenta) and reaching Earth's most remote environments, indicating that prevention rather than cleanup must be the primary strategy",
                "C": "Microplastics are harmless because the human body can process them",
                "D": "This distribution pattern is normal for all synthetic materials"
            },
            "correct": "B",
            "feedback_correct": "Correct. The ubiquity of microplastics across environments and inside human bodies demonstrates that contamination has reached a scale where prevention is the only viable primary strategy, since cleanup of this diffuse, global pollution is impractical.",
            "feedback_incorrect": "Finding microplastics in blood, placentas, Arctic ice, and the deepest ocean trenches reveals that contamination is already globally systemic. This distribution makes remediation practically impossible and underscores that prevention (reducing plastic entering the environment) must be the primary response."
        },
        {
            "question": "A policy analyst proposes banning single-use plastics as the primary solution. Using the model, evaluate the likely effectiveness of this approach.",
            "choices": {
                "A": "Banning single-use plastics would solve the problem completely within 5 years",
                "B": "Single-use bans address a significant source of ocean plastic but are insufficient alone because existing ocean contamination persists, industrial and textile microplastics contribute substantially, and alternative materials must be verified as genuinely less harmful",
                "C": "Single-use plastic bans are ineffective because all plastic pollution comes from industrial sources",
                "D": "Bans would increase ocean pollution by forcing consumers to use heavier, more harmful materials"
            },
            "correct": "B",
            "feedback_correct": "Correct. Single-use bans address a major input pathway but are one component of a comprehensive strategy. Existing contamination persists, other sources (microfibers, industrial pellets, tire wear) continue, and replacement materials need life-cycle assessment.",
            "feedback_incorrect": "Single-use plastic bans address an important source but the model shows the problem requires a systems approach: existing ocean contamination persists for centuries, other sources (microfibers from textiles, tire wear, industrial pellets) contribute significantly, and replacement materials must be assessed for their own environmental impacts."
        }
    ]
}

# ---------------------------------------------------------------------------
# L08 — Can Soil Save the Climate? (HS-LS2-4, HS-ESS3-3)
# ---------------------------------------------------------------------------
L08_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is the primary process by which carbon enters soil from the atmosphere?",
            "choices": {
                "A": "Carbon falls from the atmosphere as particulate matter during rainstorms",
                "B": "Plants capture CO2 through photosynthesis and transfer carbon to soil through roots, leaf litter, and root exudates",
                "C": "Soil minerals chemically react with atmospheric CO2 to form carbonates",
                "D": "Animals breathe CO2 into the soil through burrows"
            },
            "correct": "B",
            "feedback_correct": "Correct. Atmospheric CO2 enters soil primarily through plant photosynthesis. Plants fix carbon and transfer it belowground via root growth, leaf litter decomposition, and root exudates.",
            "feedback_incorrect": "The primary pathway is photosynthesis: plants capture atmospheric CO2 and transfer the fixed carbon to soil through root growth, leaf litter that decomposes on the surface, and root exudates that feed soil microorganisms."
        },
        {
            "question": "Approximately how much organic carbon do the world's soils contain compared to the atmosphere?",
            "choices": {
                "A": "About 10% as much as the atmosphere",
                "B": "About the same amount",
                "C": "About 3 times as much as the atmosphere",
                "D": "About 10 times as much as the atmosphere"
            },
            "correct": "C",
            "feedback_correct": "Correct. Global soils contain approximately 2,500 gigatons of organic carbon, roughly three times the ~880 gigatons in the atmosphere.",
            "feedback_incorrect": "The world's soils hold approximately 2,500 gigatons of organic carbon, about three times the carbon in the entire atmosphere (~880 Gt) and four times the carbon in all living vegetation (~450 Gt)."
        },
        {
            "question": "What is 'soil respiration'?",
            "choices": {
                "A": "The process of air moving through soil pore spaces",
                "B": "The metabolic activity of soil organisms and roots that converts organic carbon back to CO2",
                "C": "The release of oxygen by plant roots into the soil",
                "D": "The absorption of nitrogen gas by soil bacteria"
            },
            "correct": "B",
            "feedback_correct": "Correct. Soil respiration is the combined metabolic output of soil microbes and plant roots that decomposes organic matter and releases CO2.",
            "feedback_incorrect": "Soil respiration refers to the biological process where microorganisms and plant roots break down organic matter, converting stored carbon back to CO2. The rate of soil respiration determines whether soil gains or loses carbon over time."
        },
        {
            "question": "What percentage of their original organic carbon have agricultural soils lost through centuries of tillage?",
            "choices": {
                "A": "About 5-10%",
                "B": "About 20-30%",
                "C": "About 50-70%",
                "D": "About 90-100%"
            },
            "correct": "C",
            "feedback_correct": "Correct. Agricultural soils have lost 50-70% of their original carbon through centuries of tillage, which exposes buried carbon to oxygen and accelerates microbial decomposition.",
            "feedback_incorrect": "Centuries of conventional tillage have depleted 50-70% of original soil organic carbon. Plowing physically breaks apart soil structure and exposes buried organic matter to oxygen, accelerating microbial decomposition and CO2 release."
        },
        {
            "question": "What is 'regenerative agriculture'?",
            "choices": {
                "A": "Farming that uses only genetically modified crops to increase yields",
                "B": "A system of farming that prioritizes soil health through practices like cover cropping, no-till, and diverse rotations to rebuild soil organic matter",
                "C": "Industrial agriculture that maximizes production regardless of environmental impact",
                "D": "Farming that eliminates all human labor through automation"
            },
            "correct": "B",
            "feedback_correct": "Correct. Regenerative agriculture focuses on rebuilding soil health through practices that increase soil organic matter, enhance biodiversity, and restore ecosystem function.",
            "feedback_incorrect": "Regenerative agriculture prioritizes soil health through practices like no-till farming, cover cropping, diverse crop rotations, and integrated livestock grazing. The goal is to rebuild soil organic matter and restore ecosystem function."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that regenerative agriculture can sequester 0.5-3.0 tons of carbon per hectare per year, but gains slow after 20-30 years. What does this saturation effect imply for the role of soil carbon in climate strategy?",
            "choices": {
                "A": "Soil carbon sequestration is useless because it eventually stops",
                "B": "Soil carbon sequestration is a valuable time-buying strategy that can offset 5-10% of global emissions for 2-3 decades, but it is not a permanent substitute for eliminating fossil fuel emissions because soils reach a new equilibrium",
                "C": "Soil can absorb unlimited carbon if regenerative practices are maintained forever",
                "D": "The saturation effect means soils release all stored carbon after 30 years"
            },
            "correct": "B",
            "feedback_correct": "Correct. Soil carbon sequestration provides meaningful near-term benefits but plateaus as soils reach a new equilibrium. It buys time but cannot replace the need to eliminate fossil fuel emissions.",
            "feedback_incorrect": "The saturation effect means soils approach a new carbon equilibrium under regenerative management. The 20-30 year window provides meaningful mitigation (2-5 Gt CO2/year globally) but is finite. Soil carbon is a bridge strategy, not a permanent solution."
        },
        {
            "question": "The model reveals a dangerous climate feedback: warming accelerates soil respiration, releasing stored carbon, which causes more warming. With 2,500 Gt of carbon in soils (3x the atmosphere), what is the most alarming implication?",
            "choices": {
                "A": "Warming will have no effect on soil carbon because microbes become inactive in warm conditions",
                "B": "If warming pushes soils from net carbon sinks to net sources globally, the resulting carbon release could dwarf any agricultural sequestration effort and create a self-reinforcing warming cycle",
                "C": "Soil warming only affects desert soils, not agricultural or forest soils",
                "D": "This feedback loop would stop once atmospheric CO2 reaches a certain concentration"
            },
            "correct": "B",
            "feedback_correct": "Correct. The soil-climate feedback is potentially catastrophic: if warming accelerates respiration enough to flip soils from sinks to sources, the 2,500 Gt carbon reservoir becomes a warming accelerant rather than a buffer.",
            "feedback_incorrect": "The model shows that soils store 3x the atmospheric carbon. If warming-accelerated respiration exceeds plant carbon inputs globally, soils could release hundreds of gigatons of CO2, dwarfing both human emissions and any sequestration effort in a self-reinforcing cycle."
        },
        {
            "question": "A carbon credit company claims farmers can earn $50/ton for soil carbon sequestration. The model shows that carbon gains are reversible if practices revert to conventional tillage. What risk does this 'permanence problem' create?",
            "choices": {
                "A": "No risk, because carbon credits are permanent by definition",
                "B": "Stored soil carbon can be re-released within a few years if farmers return to tillage-based practices, meaning credits were sold for carbon storage that did not actually persist, undermining the integrity of carbon markets",
                "C": "Soil carbon is geologically permanent once stored, so reversibility is not a concern",
                "D": "The permanence problem only affects tropical soils, not temperate agricultural soils"
            },
            "correct": "B",
            "feedback_correct": "Correct. Unlike geological carbon storage, soil carbon gains are biologically reversible. If economic conditions change and farmers revert to conventional tillage, decades of stored carbon can be released in just a few years.",
            "feedback_incorrect": "Soil carbon storage is biologically active and reversible. If a farmer who earned carbon credits for no-till practice returns to conventional plowing (due to economics, crop disease, or land sale), the stored carbon can be released rapidly, creating a 'phantom credit' problem in carbon markets."
        },
        {
            "question": "The model compares conventional tillage (bare fallow, synthetic inputs) to regenerative management (no-till, cover crops). After 50 years, the conventional scenario shows steadily declining Soil Organic Carbon Stock. Which mechanism drives this decline?",
            "choices": {
                "A": "Synthetic fertilizers chemically destroy soil organic matter",
                "B": "Tillage physically disrupts soil structure, exposing buried organic matter to oxygen, which accelerates microbial decomposition and CO2 release while bare fallow periods provide no new carbon inputs to replace losses",
                "C": "Conventional crops absorb carbon from the soil rather than the atmosphere",
                "D": "Machinery compaction squeezes carbon gas out of the soil"
            },
            "correct": "B",
            "feedback_correct": "Correct. Tillage is the primary driver: it breaks apart soil aggregates that protect organic matter, exposes carbon to aerobic decomposition, and the absence of cover crops during fallow periods means no new carbon inputs to offset losses.",
            "feedback_incorrect": "Conventional tillage accelerates carbon loss through two mechanisms: plowing physically exposes buried organic matter to oxygen, accelerating microbial decomposition, and bare fallow periods between crops provide zero new carbon inputs. The soil steadily loses carbon because outputs exceed inputs."
        },
        {
            "question": "A policymaker asks whether soil carbon sequestration alone could offset all global CO2 emissions (approximately 40 Gt/year). Using the model's data on sequestration rates (0.5-3.0 tons C/hectare/year) and global cropland (1.5 billion hectares), evaluate this claim.",
            "choices": {
                "A": "Yes, soil could easily offset all emissions with current farmland",
                "B": "At maximum theoretical rates (3 t/ha/yr on all 1.5B hectares), soil could offset roughly 4.5 Gt C/year (about 16 Gt CO2/year), which is 5-10% of global emissions, significant but far short of full offset, and even this maximum would plateau within 20-30 years",
                "C": "Soil sequestration could offset emissions if we doubled global farmland",
                "D": "The calculation is irrelevant because soil carbon has no effect on atmospheric CO2"
            },
            "correct": "B",
            "feedback_correct": "Correct. Even the maximum theoretical calculation (3 t C x 1.5B ha = 4.5 Gt C/year = ~16 Gt CO2/year) covers only about 40% of emissions. Realistic adoption rates and the 20-30 year plateau reduce this further to 5-10%.",
            "feedback_incorrect": "The math shows soil carbon sequestration's limits: even at maximum rates across all cropland, the theoretical offset is roughly 16 Gt CO2/year (40% of emissions). Realistically, partial adoption and lower average rates reduce this to 2-5 Gt CO2/year (5-12%), and gains plateau after 20-30 years."
        }
    ]
}

# ---------------------------------------------------------------------------
# L09 — Why Do Invasive Species Win? (HS-LS2-2, HS-LS2-6, HS-LS4-5)
# ---------------------------------------------------------------------------
L09_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What makes a non-native species 'invasive'?",
            "choices": {
                "A": "Any species found outside its native range is considered invasive",
                "B": "A non-native species that establishes self-sustaining populations and causes ecological or economic harm",
                "C": "A native species that becomes unusually abundant due to human activity",
                "D": "Any species that migrates seasonally between different regions"
            },
            "correct": "B",
            "feedback_correct": "Correct. Not all non-native species are invasive. The 'invasive' designation requires that the species establishes, spreads, and causes measurable ecological or economic harm.",
            "feedback_incorrect": "A species is invasive only if it is (1) non-native, (2) establishes self-sustaining populations, and (3) causes harm to the ecosystem, economy, or human health. Many non-native species exist harmlessly."
        },
        {
            "question": "The 'enemy release hypothesis' suggests that invasive species thrive because:",
            "choices": {
                "A": "They evolve new defensive adaptations in their new environment",
                "B": "They are freed from the predators, parasites, and diseases that controlled them in their native range",
                "C": "Native species actively cooperate with invaders to share resources",
                "D": "Human activity eliminates all predators in every ecosystem"
            },
            "correct": "B",
            "feedback_correct": "Correct. Invasive species leave behind the specialized natural enemies (predators, parasites, pathogens) that kept their populations in check, allowing unconstrained growth in new environments.",
            "feedback_incorrect": "The enemy release hypothesis explains that invasive species succeed because they arrive without the specialized predators, parasites, and diseases that evolved alongside them to control their populations. Without these natural checks, their populations can grow exponentially."
        },
        {
            "question": "What is 'competitive exclusion'?",
            "choices": {
                "A": "The principle that two species competing for the same limited resource cannot coexist indefinitely",
                "B": "A conservation strategy that physically separates native and invasive species",
                "C": "The process by which invasive species are excluded from protected areas",
                "D": "A genetic mechanism that prevents hybridization between species"
            },
            "correct": "A",
            "feedback_correct": "Correct. Competitive exclusion states that if two species compete for exactly the same limited resource, the one with even a slight advantage will eventually drive the other to local extinction.",
            "feedback_incorrect": "The competitive exclusion principle states that two species occupying the same ecological niche cannot coexist indefinitely. The species with even a small competitive advantage will eventually outcompete and locally eliminate the other."
        },
        {
            "question": "Invasive species are the second leading cause of species extinction globally. What is the first?",
            "choices": {
                "A": "Climate change",
                "B": "Pollution",
                "C": "Habitat destruction",
                "D": "Overhunting"
            },
            "correct": "C",
            "feedback_correct": "Correct. Habitat destruction is the leading cause of extinction, followed by invasive species, which have contributed to approximately 60% of all documented extinctions.",
            "feedback_incorrect": "Habitat destruction (deforestation, land conversion, urbanization) is the leading cause of species extinction globally. Invasive species rank second, having contributed to about 60% of all documented plant and animal extinctions."
        },
        {
            "question": "Why are island ecosystems disproportionately vulnerable to invasive species?",
            "choices": {
                "A": "Islands have more resources available for invasive species to exploit",
                "B": "Island species evolved in isolation without exposure to aggressive competitors or predators, leaving them with no defensive adaptations",
                "C": "Islands are closer to continental sources of invasive species",
                "D": "Island climates are more favorable for non-native species than mainland climates"
            },
            "correct": "B",
            "feedback_correct": "Correct. Island species evolved in isolation and never developed defenses against the types of predators and competitors found on continents. This evolutionary naivety makes them extremely vulnerable.",
            "feedback_incorrect": "Island species evolved in isolation, often without exposure to mammalian predators, aggressive competitors, or continental diseases. This evolutionary inexperience leaves them defenseless against invaders. About 75% of all documented extinctions have occurred on islands."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that when Invasive Population is at 100 individuals, removal efforts successfully prevent establishment. At 10,000 individuals, the same removal rate fails. What does this threshold behavior demonstrate?",
            "choices": {
                "A": "Removal technology becomes less effective over time regardless of population size",
                "B": "Below the establishment threshold, removal can outpace reproduction, but above it, the invasive population's growth rate exceeds removal capacity, and positive feedback loops (habitat modification, resource monopolization) make eradication increasingly difficult",
                "C": "Invasive species develop resistance to removal methods after reaching 10,000 individuals",
                "D": "At 10,000 individuals, invasive species begin migrating to new areas beyond the removal zone"
            },
            "correct": "B",
            "feedback_correct": "Correct. Below the threshold, removal can suppress growth. Above it, exponential reproduction overwhelms removal capacity, and positive feedbacks (habitat modification, resource depletion) create conditions that further favor the invader.",
            "feedback_incorrect": "The establishment threshold marks a critical transition: below it, removal can outpace reproduction. Above it, exponential growth exceeds management capacity, and the invader begins modifying habitat in its own favor, creating positive feedback loops that make control progressively harder."
        },
        {
            "question": "The model demonstrates that invasive grasses increase fire frequency, which kills fire-intolerant native trees, creating more grassland for the invader. What type of system dynamic does this represent?",
            "choices": {
                "A": "Negative feedback that restores the native tree population",
                "B": "A positive feedback loop where the invasive species modifies the environment to favor its own spread, making each increment of invasion accelerate the next",
                "C": "A neutral interaction with no effect on invasion dynamics",
                "D": "Random environmental variation unrelated to the invasion"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is a textbook invasion-fire feedback loop: invasive grass increases fire frequency, fire eliminates native trees, more open space favors more grass, more grass means more fire. Each cycle accelerates invasion.",
            "feedback_incorrect": "The invasion-fire feedback is a positive (self-reinforcing) loop: the invader modifies its environment (more flammable grass) to create conditions (frequent fire) that eliminate competitors (fire-intolerant trees) and expand its own habitat, accelerating further invasion."
        },
        {
            "question": "The 'invasion curve' shows that spending $1 on prevention or early detection avoids $100-$1,000 in later control costs. A budget committee asks why prevention funding should be prioritized over more visible eradication programs. Which model-based argument is strongest?",
            "choices": {
                "A": "Eradication programs are always unsuccessful",
                "B": "Prevention catches invasions when populations are small and feedback loops have not engaged, making control feasible. Once populations cross the establishment threshold, positive feedbacks make eradication exponentially more expensive and less likely to succeed",
                "C": "Prevention is cheaper because it requires fewer staff",
                "D": "Early detection technology is more advanced than eradication technology"
            },
            "correct": "B",
            "feedback_correct": "Correct. The cost-effectiveness case is rooted in systems dynamics: below the establishment threshold, small populations are manageable. Above it, positive feedbacks create exponentially growing costs and diminishing returns.",
            "feedback_incorrect": "The invasion curve demonstrates that cost-effectiveness declines exponentially with invasion stage. Prevention and early detection target populations before positive feedback loops (habitat modification, resource monopolization) engage, making control feasible and affordable."
        },
        {
            "question": "In the biocontrol scenario, introducing a natural predator from the invader's native range reduces invasive population growth. However, the model shows that Native Biodiversity Index does not return to pre-invasion levels. What best explains this incomplete recovery?",
            "choices": {
                "A": "Biocontrol agents always harm native species more than invasive species",
                "B": "The invasion caused irreversible changes: native species driven to local extinction cannot return, habitat modifications persist, and ecological interactions (pollination networks, predator-prey relationships) were permanently disrupted",
                "C": "Native species refuse to recolonize areas previously occupied by invasive species",
                "D": "Biocontrol agents become invasive themselves 100% of the time"
            },
            "correct": "B",
            "feedback_correct": "Correct. Even after reducing the invader, the ecosystem has undergone lasting changes: species extinctions, altered habitat structure, and disrupted ecological networks create a 'new normal' that differs from the pre-invasion state.",
            "feedback_incorrect": "The ecosystem has undergone a regime shift: some native species are locally extinct and cannot recolonize, habitat has been physically altered, and ecological interaction networks (pollination, seed dispersal, predation) have been rewired. The ecosystem stabilizes at a new, less diverse state."
        },
        {
            "question": "A student examines the model and notes that Resource Availability declines as Invasive Population grows, while Native Species Competitive Fitness drops simultaneously. How do these two variables interact to create the 'biodiversity collapse' seen in the model?",
            "choices": {
                "A": "They are independent variables that coincidentally decline at the same time",
                "B": "As invasive species monopolize resources, native species face both resource scarcity AND reduced competitive ability (due to smaller populations, fragmented habitat, and disrupted ecological partnerships), creating a compounding decline where each factor worsens the other",
                "C": "Resource availability declines because native species consume too much",
                "D": "Native competitive fitness increases as resources decline because scarcity drives adaptation"
            },
            "correct": "B",
            "feedback_correct": "Correct. The interaction is synergistic: invasive resource monopolization weakens native populations, which reduces their competitive fitness, which allows the invader to capture even more resources, compounding the decline in a reinforcing spiral.",
            "feedback_incorrect": "These variables interact synergistically: the invader takes resources, weakening natives. Weakened natives compete less effectively, losing more resources. Smaller native populations lose ecological partnerships (pollinators, seed dispersers). Each factor amplifies the other in a downward spiral."
        }
    ]
}

# ---------------------------------------------------------------------------
# L10 — The Heat Island Effect (HS-ESS3-4, HS-ETS1-1)
# ---------------------------------------------------------------------------
L10_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is the 'urban heat island' effect?",
            "choices": {
                "A": "A volcanic island near a city that generates heat from magma",
                "B": "The phenomenon where metropolitan areas are significantly warmer than surrounding rural areas due to heat-absorbing surfaces and human activities",
                "C": "A tropical island used for urban development",
                "D": "The reflection of heat from city buildings into outer space"
            },
            "correct": "B",
            "feedback_correct": "Correct. Urban heat islands occur because cities replace natural vegetation with dark, heat-absorbing surfaces (asphalt, concrete) and generate waste heat from vehicles and buildings.",
            "feedback_incorrect": "The urban heat island effect is the temperature difference between cities and surrounding rural areas. Cities can be 5-12 degrees F hotter during the day and up to 22 degrees F hotter at night due to heat-absorbing materials and waste heat generation."
        },
        {
            "question": "What is 'albedo' and why does it matter for urban temperatures?",
            "choices": {
                "A": "Albedo is the amount of CO2 a surface absorbs from the atmosphere",
                "B": "Albedo is the fraction of sunlight a surface reflects; low-albedo surfaces (dark asphalt) absorb more heat, raising temperatures",
                "C": "Albedo measures the age of building materials in a city",
                "D": "Albedo is the rate at which cities expand into rural areas"
            },
            "correct": "B",
            "feedback_correct": "Correct. Albedo measures surface reflectivity. Dark asphalt (albedo 0.05-0.10) absorbs 90-95% of solar energy as heat, while lighter surfaces reflect more and absorb less.",
            "feedback_incorrect": "Albedo is the fraction of incoming sunlight that a surface reflects. Fresh snow has high albedo (0.8-0.9, reflects most light), while dark asphalt has very low albedo (0.05-0.10, absorbs most light and converts it to heat)."
        },
        {
            "question": "How does vegetation cool its surroundings?",
            "choices": {
                "A": "Trees block wind, preventing warm air from reaching people",
                "B": "Plants convert solar energy into water vapor through evapotranspiration, cooling the air instead of heating it",
                "C": "Vegetation has no significant cooling effect on local temperatures",
                "D": "Plants absorb heat from the ground and store it permanently in their roots"
            },
            "correct": "B",
            "feedback_correct": "Correct. Through evapotranspiration, vegetation converts solar energy into the latent heat of water vaporization rather than sensible heat, cooling surrounding air by 2-8 degrees F.",
            "feedback_incorrect": "Vegetation cools through evapotranspiration: trees and plants absorb water through roots and release it as vapor through leaves. This process converts solar energy into water vapor rather than heat, providing 2-8 degrees F of cooling compared to impervious surfaces."
        },
        {
            "question": "Which weather phenomenon kills more people annually in the United States than hurricanes, floods, and tornadoes combined?",
            "choices": {
                "A": "Blizzards",
                "B": "Extreme heat",
                "C": "Lightning",
                "D": "Wildfires"
            },
            "correct": "B",
            "feedback_correct": "Correct. Extreme heat is the deadliest weather phenomenon in the United States, causing more annual deaths than all other weather events combined.",
            "feedback_incorrect": "Extreme heat is the deadliest weather phenomenon in the US, causing more deaths annually than hurricanes, floods, and tornadoes combined. Climate change is projected to increase heat-related deaths 3-5x by 2050 in cities without cooling infrastructure investment."
        },
        {
            "question": "Why do cities stay hot even after the sun goes down?",
            "choices": {
                "A": "Streetlights and neon signs generate significant heat at night",
                "B": "Concrete and asphalt have high thermal mass, absorbing heat during the day and slowly re-radiating it at night",
                "C": "Night air in cities is trapped by skyscrapers, preventing cooling",
                "D": "Urban populations generate body heat that keeps the city warm"
            },
            "correct": "B",
            "feedback_correct": "Correct. High thermal mass materials (concrete, asphalt) absorb and store solar energy during the day and re-radiate it as heat at night, preventing the cooling that rural areas experience.",
            "feedback_incorrect": "Concrete, asphalt, and building materials have high thermal mass: they absorb solar energy during the day and release it slowly overnight. This re-radiation keeps cities 10-22 degrees F warmer than rural areas at night, which is particularly dangerous because it prevents the body from recovering from daytime heat stress."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that within a single city, temperature differences of 10-15 degrees F exist between neighborhoods, and these differences map directly onto historic patterns of racial segregation. What systems-level explanation connects redlining to current heat vulnerability?",
            "choices": {
                "A": "Redlined neighborhoods happen to be located on higher ground where it is warmer",
                "B": "Historically redlined neighborhoods received less investment in tree planting, parks, and green infrastructure, resulting in more impervious surface, less evapotranspiration cooling, and higher temperatures today, creating a physical legacy of structural racism",
                "C": "Redlining affected only housing prices, not physical infrastructure or vegetation",
                "D": "All neighborhoods in a city experience identical temperatures regardless of tree cover"
            },
            "correct": "B",
            "feedback_correct": "Correct. Redlining directed investment away from certain neighborhoods for decades, resulting in less tree cover, fewer parks, more impervious surface, and consequently higher temperatures. This is a direct physical legacy of discriminatory policy.",
            "feedback_incorrect": "Historic redlining caused decades of disinvestment in certain neighborhoods: fewer trees were planted, parks were not built, and infrastructure prioritized pavement. Today, these neighborhoods have less vegetation, more impervious surface, and temperatures 10-15 degrees F higher than better-invested areas."
        },
        {
            "question": "The model reveals an air conditioning feedback loop: higher temperatures increase AC demand, but AC units expel waste heat outdoors, which raises ambient temperatures further. What type of system dynamic is this?",
            "choices": {
                "A": "Negative feedback that stabilizes temperatures through mechanical cooling",
                "B": "A positive feedback loop where individual cooling responses collectively worsen the problem they are trying to solve",
                "C": "A neutral loop with no net temperature effect",
                "D": "A negative feedback loop that will eventually eliminate the heat island"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is a positive feedback loop: AC cools interiors but dumps waste heat outside, raising outdoor temperatures, which increases AC demand. Each individual's rational cooling decision collectively amplifies the heat island.",
            "feedback_incorrect": "The AC feedback loop is positive (self-reinforcing): cooling buildings dumps waste heat outside, raising outdoor temperatures, which increases AC demand. Dense urban cores can see 2-4 degrees F of additional warming from waste heat alone, creating a vicious cycle."
        },
        {
            "question": "A green infrastructure plan proposes increasing tree canopy from 10% to 30% in the hottest neighborhood. The model predicts 5-10 degrees F of cooling, but full canopy effect takes 15-20 years. A city council member argues this timeline is unacceptable. Which systems-informed response best addresses this concern?",
            "choices": {
                "A": "Abandon the tree planting plan entirely in favor of faster solutions",
                "B": "Implement a phased strategy combining immediate interventions (cool roofs, shade structures, misting stations) for near-term relief with long-term tree planting for sustained cooling, acknowledging that no single solution addresses all timescales",
                "C": "Plant only fast-growing tree species regardless of their suitability for the climate",
                "D": "Wait until faster-growing tree varieties are developed before beginning"
            },
            "correct": "B",
            "feedback_correct": "Correct. A systems approach layers short-term solutions (immediate cooling) with long-term investments (trees). This addresses the council member's urgency concern while still building toward the most effective permanent solution.",
            "feedback_incorrect": "The systems-informed approach combines time horizons: immediate relief (cool roofs install in months, shade structures in weeks) provides near-term protection while trees grow toward their full 15-20 year cooling potential. A layered strategy addresses both urgency and long-term effectiveness."
        },
        {
            "question": "Climate change is projected to add 3-5 degrees F of baseline warming to urban areas by 2050. The model shows this does not simply 'add' to the heat island but amplifies it. Which mechanism best explains this amplification?",
            "choices": {
                "A": "Climate change only affects rural areas, not cities",
                "B": "Higher baseline temperatures increase AC waste heat, reduce remaining vegetation through heat stress, and push more days above dangerous thresholds, each of which further intensifies the heat island through positive feedback loops",
                "C": "Cities are insulated from climate change by their concrete infrastructure",
                "D": "Climate change reduces urban temperatures by increasing cloud cover over cities"
            },
            "correct": "B",
            "feedback_correct": "Correct. Climate change amplifies the heat island through multiple reinforcing mechanisms: more AC waste heat, vegetation stress, and more frequent threshold exceedances, each feeding back to intensify warming.",
            "feedback_incorrect": "Climate warming amplifies rather than simply adds to the heat island because it triggers feedback loops: higher baseline temperatures increase AC demand (more waste heat), stress urban vegetation (less evapotranspiration), and push more days above health thresholds, each of which further increases temperatures."
        },
        {
            "question": "A student claims that solving the urban heat island is purely an engineering problem (install cool roofs, plant trees). The model reveals a critical additional dimension. Which dimension does the model highlight?",
            "choices": {
                "A": "The problem is too expensive for any city to address",
                "B": "Environmental justice: cooling investments must be directed to the most heat-vulnerable neighborhoods, and plans must include anti-displacement protections to prevent gentrification from displacing the residents the cooling was meant to protect",
                "C": "Engineering solutions are the only dimension that matters",
                "D": "The heat island will resolve itself as cities naturally expand"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that heat burden is not distributed equally. Engineering solutions must be paired with equity-centered policies to ensure cooling benefits reach the most vulnerable populations without causing gentrification and displacement.",
            "feedback_incorrect": "The model reveals that the heat island is both an engineering and an environmental justice problem. The hottest neighborhoods are the most socially vulnerable, and green infrastructure investments can trigger gentrification, displacing the very residents they were meant to protect. Solutions must include anti-displacement policies."
        }
    ]
}

# ---------------------------------------------------------------------------
# Aggregated dictionary for programmatic access
# ---------------------------------------------------------------------------
ALL_QUESTIONS = {
    "G11L2-L01": L01_QUESTIONS,
    "G11L2-L02": L02_QUESTIONS,
    "G11L2-L03": L03_QUESTIONS,
    "G11L2-L04": L04_QUESTIONS,
    "G11L2-L05": L05_QUESTIONS,
    "G11L2-L06": L06_QUESTIONS,
    "G11L2-L07": L07_QUESTIONS,
    "G11L2-L08": L08_QUESTIONS,
    "G11L2-L09": L09_QUESTIONS,
    "G11L2-L10": L10_QUESTIONS,
}
