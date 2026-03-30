#!/usr/bin/env python3
"""Multiple choice pre/post assessment questions for Grade 12 Level 3 ModelIt! Lessons (Capstone Innovation Lab)"""

# =============================================================================
# L01: Can We Colonize Mars? (HS-ESS2-4)
# =============================================================================
L01_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Mars receives approximately 43% of the solar energy that Earth receives. Which of the following best explains the primary consequence of this reduced solar input for a Mars colony?",
            "choices": {
                "A": "Solar panels on Mars would need to be at least twice the surface area of equivalent Earth installations to generate comparable power",
                "B": "Reduced solar energy creates a cascade effect limiting oxygen production, food growth, and water recycling simultaneously since all depend on energy input",
                "C": "The colony would need to rely exclusively on nuclear power because solar energy is insufficient at Mars's distance from the Sun",
                "D": "Lower solar radiation means Mars has fewer dust storms, making solar power more reliable than on Earth"
            },
            "correct": "B",
            "feedback_correct": "Correct. Solar energy is the master variable in a Mars colony. Because oxygen production (electrolysis), food production (grow lights for hydroponics), and water recycling (purification pumps) all require energy, reduced solar input creates cascading limitations across every life support subsystem.",
            "feedback_incorrect": "Consider that a Mars colony is a closed system where nearly every life support function requires energy. When the primary energy source is reduced, the effects propagate through oxygen production, food growth, and water recycling simultaneously rather than affecting just one system."
        },
        {
            "question": "A Mars colony life support system must recycle water at 98%+ efficiency. What is the most scientifically accurate explanation for why this threshold is so critical?",
            "choices": {
                "A": "Water on Mars exists only as vapor in the atmosphere and cannot be extracted in liquid form",
                "B": "Water is used in a single process (drinking) so any loss reduces the potable supply linearly",
                "C": "Water serves multiple interconnected functions including oxygen generation, food production, cooling, and hygiene, so small recycling losses compound across all systems",
                "D": "The International Space Station achieves 98% efficiency, so Mars must match this standard for crew familiarity"
            },
            "correct": "C",
            "feedback_correct": "Correct. Water is not just for drinking. It is the feedstock for oxygen generation via electrolysis, the medium for hydroponic food production, and essential for cooling systems and hygiene. A 5% recycling loss creates compounding deficits across all of these interconnected subsystems.",
            "feedback_incorrect": "Think about all the roles water plays in a closed life support system beyond just drinking. Water is used for oxygen generation (electrolysis), food production (hydroponics), cooling, and sanitation. Losses in recycling efficiency compound across all of these functions."
        },
        {
            "question": "Mars lacks a global magnetic field. Which of the following correctly identifies the primary threat this poses to a human colony and the type of radiation involved?",
            "choices": {
                "A": "Ultraviolet radiation from the Sun would cause severe sunburns, requiring SPF-rated habitat windows",
                "B": "Galactic cosmic rays and solar particle events deliver cumulative ionizing radiation doses approximately 200 times Earth's background level, requiring engineered shielding",
                "C": "Infrared radiation causes the surface temperature to fluctuate wildly, making thermal regulation impossible",
                "D": "Radio wave interference from solar flares would prevent all communication between the colony and Earth"
            },
            "correct": "B",
            "feedback_correct": "Correct. Without a global magnetic field or thick atmosphere, Mars's surface is exposed to galactic cosmic rays and solar particle events that deliver approximately 0.67 millisieverts per day, roughly 200 times Earth's background radiation level. This ionizing radiation causes cumulative DNA damage and requires engineered shielding for long-term habitation.",
            "feedback_incorrect": "The key issue is ionizing radiation, not UV, infrared, or radio waves. Earth's magnetic field deflects charged particles from cosmic rays and solar events. Without this protection on Mars, colonists would receive cumulative radiation doses approximately 200 times Earth's background level."
        },
        {
            "question": "In a closed-loop life support system, what distinguishes it fundamentally from the life support on the International Space Station?",
            "choices": {
                "A": "The ISS uses open-loop systems that vent all waste into space, while a Mars colony must recycle everything",
                "B": "A truly closed-loop system recycles all essential resources with minimal external inputs, whereas the ISS receives regular resupply missions that compensate for recycling inefficiencies",
                "C": "Closed-loop systems use only renewable energy while the ISS relies on fossil fuel generators",
                "D": "The ISS does not recycle any water or air, relying entirely on deliveries from Earth"
            },
            "correct": "B",
            "feedback_correct": "Correct. The ISS does recycle water (at approximately 93% efficiency) and regenerate oxygen, but it receives regular resupply missions every few months that compensate for losses. A Mars colony cannot rely on frequent resupply due to the 6-9 month transit time, so it must achieve near-perfect recycling in a truly closed-loop system.",
            "feedback_incorrect": "The ISS does recycle water and air, but it receives resupply missions regularly. The critical distinction is that a Mars colony cannot rely on frequent resupply due to orbital mechanics and transit time, making near-perfect closed-loop recycling essential rather than optional."
        },
        {
            "question": "A student claims that terraforming Mars would be straightforward because we could release CO2 from the polar ice caps to thicken the atmosphere. Which scientific evidence most directly challenges this claim?",
            "choices": {
                "A": "Mars has no CO2 in its atmosphere, so there is nothing to build upon",
                "B": "Research indicates that all accessible CO2 reserves on Mars would increase atmospheric pressure to only about 1-2% of Earth's, far below the level needed to support liquid water or breathable conditions",
                "C": "CO2 is toxic to humans, so adding more would make Mars less habitable rather than more habitable",
                "D": "Solar wind has no effect on the Martian atmosphere, so released CO2 would remain indefinitely"
            },
            "correct": "B",
            "feedback_correct": "Correct. NASA-funded research has shown that even if all known accessible CO2 sources on Mars (polar caps, regolith adsorption, minerals) were released, the resulting atmospheric pressure would remain far below what is needed to support liquid surface water or human respiration. Terraforming through CO2 release alone is insufficient.",
            "feedback_incorrect": "Mars does have CO2 (95% of its thin atmosphere), but the total accessible reserves are insufficient. Studies show that releasing all known CO2 sources would raise atmospheric pressure to only 1-2% of Earth's level, far short of what is needed for liquid water or breathable conditions."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A computational model of a Mars colony shows that during a 90-day dust storm reducing solar energy by 90%, the Colony Viability Index drops below the survival threshold by day 45. Which modification to the model would most effectively extend the survivable duration?",
            "choices": {
                "A": "Adding a nuclear fission reactor as a secondary energy source independent of solar input",
                "B": "Increasing the habitat size to store more atmospheric oxygen",
                "C": "Reducing the number of colonists to lower oxygen demand",
                "D": "Increasing the efficiency of solar panels from 20% to 25%"
            },
            "correct": "A",
            "feedback_correct": "Correct. The model demonstrates that energy is the master variable. A nuclear fission reactor provides energy independent of solar input, maintaining oxygen production, water recycling, and food production systems even during extended dust storms. This addresses the root cause of cascade failure rather than a single symptom.",
            "feedback_incorrect": "Consider what the model reveals about energy as the master variable. During a dust storm, the fundamental problem is loss of energy input. Increasing solar efficiency or reducing demand addresses symptoms, but only an energy source independent of solar input (like nuclear fission) fundamentally solves the cascade failure."
        },
        {
            "question": "A student's model reveals that water recycling efficiency dropping from 98% to 93% causes the Colony Viability Index to decline more rapidly than a 50% reduction in food production capacity. Which systems-level explanation best accounts for this finding?",
            "choices": {
                "A": "Water has higher mass than food, so transporting replacement water from Earth costs more",
                "B": "Water recycling feeds into multiple subsystems (oxygen generation, food production, cooling, hygiene), so its inefficiency creates compounding deficits across the entire life support network",
                "C": "Food can be rationed but water cannot, making water loss immediately lethal",
                "D": "The model has a programming error because food production should always have a larger impact than water recycling"
            },
            "correct": "B",
            "feedback_correct": "Correct. Water is a nexus variable in the life support network. It is the feedstock for oxygen generation (electrolysis), the medium for hydroponic food production, essential for thermal regulation, and necessary for sanitation. A 5% drop in recycling efficiency compounds across all these interconnected systems, creating a larger net impact than reducing any single subsystem.",
            "feedback_incorrect": "Think about water's role across the entire system. Water is used for oxygen production (electrolysis), food production (hydroponics), cooling systems, and hygiene. A drop in recycling efficiency affects ALL of these simultaneously, creating compounding deficits that exceed the impact of reducing any single subsystem."
        },
        {
            "question": "The model shows that adding a 'Psychological Stress Index' component creates a new feedback loop where increasing stress reduces crew productivity, which reduces system maintenance, which degrades habitat integrity, which increases stress further. This is an example of:",
            "choices": {
                "A": "A negative feedback loop that will stabilize the system at a lower equilibrium",
                "B": "A positive feedback loop that amplifies the initial perturbation and could drive the system toward collapse",
                "C": "A linear relationship where stress increases proportionally with habitat degradation",
                "D": "An independent variable that does not interact with the physical life support components"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is a positive (reinforcing) feedback loop: stress reduces productivity, reduced productivity degrades systems, degraded systems increase stress. Each cycle amplifies the initial perturbation rather than dampening it, potentially driving the system toward a tipping point and collapse. This is distinct from a negative (balancing) feedback loop that would stabilize the system.",
            "feedback_incorrect": "Consider the direction of the effect at each step. Stress reduces productivity, which degrades systems, which increases stress further. Each step amplifies the previous one rather than counteracting it. This self-reinforcing cycle is a positive feedback loop that can drive exponential decline."
        },
        {
            "question": "Two students build Mars colony models with identical components but different relationship structures. Student A connects Solar Energy Input directly to all five output variables. Student B creates a cascade where Solar Energy Input drives Oxygen Production, which affects Food Production, which affects Water Recycling. Which model better represents the actual system and why?",
            "choices": {
                "A": "Student A's model is better because solar energy does directly power all systems independently",
                "B": "Student B's model is better because it captures the sequential dependencies where upstream failures propagate downstream through the life support chain",
                "C": "Both models are equally valid because they produce the same Colony Viability Index",
                "D": "Neither model is valid because Mars colony systems operate independently of each other"
            },
            "correct": "B",
            "feedback_correct": "Correct. Student B's cascade model better represents the real system because life support subsystems have sequential dependencies. Oxygen production requires energy, food production requires both energy and oxygen-rich atmosphere, and water recycling requires energy and is affected by biological processes in food production. The cascade structure reveals how upstream failures propagate and amplify through the system.",
            "feedback_incorrect": "Consider how the life support systems are connected. Oxygen production needs energy. Food production needs energy AND oxygen. Water recycling needs energy AND is connected to food production processes. These sequential dependencies mean a cascade model captures critical propagation dynamics that a parallel model misses."
        },
        {
            "question": "Analysis of the model under the 'Aging Colony' scenario (10 years, no resupply) reveals that Habitat Structural Integrity degradation has a threshold effect: below 85% integrity, the decline in Colony Viability Index accelerates nonlinearly. Which concept from systems thinking best explains this threshold behavior?",
            "choices": {
                "A": "Carrying capacity, where the habitat can no longer support the population above a minimum structural requirement",
                "B": "A tipping point where the rate of structural degradation from thermal cycling and micrometeorite impacts exceeds the colony's repair capacity, creating runaway decline",
                "C": "Homeostasis, where the colony self-regulates to maintain a constant internal environment",
                "D": "Equilibrium, where the colony reaches a stable but lower level of function indefinitely"
            },
            "correct": "B",
            "feedback_correct": "Correct. The threshold represents a tipping point where degradation rate exceeds repair capacity. Above 85% integrity, maintenance crews can repair damage faster than it accumulates. Below 85%, the repair backlog grows, meaning more systems fail, requiring more repair time, leaving other systems unattended. This creates runaway decline characteristic of a system that has crossed a critical threshold.",
            "feedback_incorrect": "Consider what happens when damage accumulates faster than it can be repaired. Above the threshold, maintenance keeps pace with degradation. Below it, the backlog grows, causing cascading failures. This is a tipping point where the system transitions from stable decline to runaway deterioration."
        }
    ]
}

# =============================================================================
# L02: How Do Pandemics Spread? (HS-LS2-8)
# =============================================================================
L02_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A virus has a basic reproduction number (R0) of 4. Which statement most accurately describes what this means for pandemic dynamics?",
            "choices": {
                "A": "Each infected person will infect exactly 4 others, regardless of interventions or population immunity",
                "B": "In a fully susceptible population with no interventions, each infected person will transmit to an average of 4 others, creating exponential growth",
                "C": "The virus will infect 4% of the population before the pandemic ends",
                "D": "The virus mutates 4 times faster than seasonal influenza"
            },
            "correct": "B",
            "feedback_correct": "Correct. R0 represents the average number of secondary infections in a completely susceptible population with no interventions. It describes the maximum transmission potential, not a fixed outcome. Interventions, immunity, and behavior can reduce the effective reproduction number below R0.",
            "feedback_incorrect": "R0 is an average in ideal conditions (fully susceptible population, no interventions), not a fixed number of infections per person. It describes the virus's inherent transmission potential, which can be modified by interventions, immunity, and behavioral changes."
        },
        {
            "question": "The herd immunity threshold for a disease with R0 = 5 is calculated as 1 - (1/R0). What does this threshold represent and what is its value?",
            "choices": {
                "A": "60% of the population must be infected before the disease stops spreading",
                "B": "80% of the population must be immune (through vaccination or prior infection) to prevent sustained transmission",
                "C": "20% of the population is naturally resistant to the disease",
                "D": "50% vaccination coverage is sufficient to eliminate the disease entirely"
            },
            "correct": "B",
            "feedback_correct": "Correct. The herd immunity threshold = 1 - (1/5) = 0.80, meaning 80% of the population must be immune to prevent sustained transmission. At this level, each infected person encounters enough immune individuals that the effective reproduction number drops below 1, and chains of transmission die out.",
            "feedback_incorrect": "Apply the formula: 1 - (1/R0) = 1 - (1/5) = 1 - 0.2 = 0.8 = 80%. This means 80% of the population must be immune to reduce the effective reproduction number below 1 and stop sustained transmission."
        },
        {
            "question": "During the early weeks of a pandemic, the number of confirmed cases appears to be growing slowly. A public health official argues that aggressive intervention is unnecessary because case counts are still low. Which scientific principle most directly undermines this argument?",
            "choices": {
                "A": "Correlation does not equal causation, so low case counts do not indicate low transmission",
                "B": "Exponential growth is deceptively slow initially but accelerates dramatically, meaning the window for effective intervention closes before the threat becomes visually apparent",
                "C": "Pandemics always resolve on their own through natural immunity without intervention",
                "D": "Testing capacity is always insufficient early in a pandemic, so reported cases are meaningless"
            },
            "correct": "B",
            "feedback_correct": "Correct. Exponential growth starts slowly: 2, 4, 8, 16, 32 cases appear manageable. But the same doubling time that produces 32 cases in week 5 produces 32,000 cases by week 15. By the time the pandemic is visibly severe, the mathematical trajectory is already set and intervention becomes far more costly and less effective.",
            "feedback_incorrect": "The critical insight is about exponential mathematics. When cases double every few days, the early phase looks manageable (2, 4, 8, 16) but the same growth rate quickly becomes overwhelming. By the time the problem is visible, the opportunity for cost-effective intervention has passed."
        },
        {
            "question": "A superspreader event occurs when a single infected individual transmits to many more people than the average R0 predicts. Which factor most directly enables superspreader events?",
            "choices": {
                "A": "The infected individual has a genetically mutated strain that is inherently more transmissible",
                "B": "A combination of individual variation in viral shedding and environmental conditions such as crowded, poorly ventilated indoor spaces",
                "C": "The individual deliberately spreads the disease by refusing to stay home",
                "D": "Superspreader events only occur with bacterial diseases, not viral diseases"
            },
            "correct": "B",
            "feedback_correct": "Correct. Superspreader events result from the convergence of biological factors (some individuals shed far more virus than average) and environmental conditions (crowded indoor spaces with poor ventilation maximize airborne transmission). This individual variation in infectiousness means that a small number of transmission events drive a disproportionate fraction of total spread.",
            "feedback_incorrect": "Superspreading is driven by the combination of biological variation (some individuals shed much more virus than others) and environmental conditions (crowded, enclosed, poorly ventilated spaces). It is not about deliberate behavior or specific pathogen types."
        },
        {
            "question": "When a pandemic overwhelms healthcare system capacity, mortality rates increase for reasons beyond the pandemic disease itself. Which explanation best captures this effect?",
            "choices": {
                "A": "Hospitals raise prices when demand is high, preventing patients from affording treatment",
                "B": "When ICU beds, ventilators, and trained staff are consumed by pandemic patients, individuals with heart attacks, strokes, injuries, and other conditions cannot receive standard care, increasing deaths from all causes",
                "C": "Overwhelmed healthcare workers transmit the disease to non-pandemic patients through poor hygiene",
                "D": "Hospital buildings deteriorate physically when overused, creating unsafe conditions for all patients"
            },
            "correct": "B",
            "feedback_correct": "Correct. Healthcare capacity is a mortality multiplier. When beds, ventilators, staff, and surgical capacity are consumed by pandemic patients, people experiencing heart attacks, strokes, accidents, cancer complications, and other conditions cannot receive timely treatment. The true death toll includes both direct pandemic deaths and indirect excess mortality from untreated conditions.",
            "feedback_incorrect": "The key concept is that hospital resources are finite and shared. When pandemic patients consume all ICU beds, ventilators, and staff time, patients with heart attacks, strokes, and other emergencies cannot receive standard care. This makes healthcare capacity a mortality multiplier for ALL causes of death."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's model shows that implementing social distancing (reducing Contact Rate by 50%) when R0 = 3 reduces the effective reproduction number to 1.5 but does not stop exponential growth. Which additional intervention does the model suggest is needed?",
            "choices": {
                "A": "Only a complete lockdown with zero contact can stop the pandemic",
                "B": "A combination of additional interventions (testing, quarantine, and eventually vaccination) must work together with social distancing to push the effective R0 below 1",
                "C": "Social distancing should be abandoned since it does not eliminate spread entirely",
                "D": "Increasing hospital capacity is more important than reducing transmission"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that no single intervention is sufficient when R0 is high. Social distancing reduces R0 from 3 to 1.5, but further reduction below 1 requires layered interventions: testing and quarantine remove infectious individuals from the transmission chain, masks reduce per-contact transmission probability, and vaccination reduces the susceptible population. These interventions are multiplicative, not additive.",
            "feedback_incorrect": "An effective R0 of 1.5 still produces exponential growth, just more slowly. The model shows that multiple layered interventions are needed to push the effective R0 below 1. Social distancing, testing, quarantine, and vaccination work multiplicatively together."
        },
        {
            "question": "The model reveals that intervening 2 weeks after the first case prevents significantly more deaths than intervening 6 weeks later with identical measures. A student claims this is because 'the virus gets weaker over time.' What is the correct systems-level explanation?",
            "choices": {
                "A": "Early intervention prevents more deaths because exponential growth means each day of delay doubles or triples the infected population, making the same intervention far less effective against a larger epidemic",
                "B": "The virus evolves to become less deadly over the 4-week delay period",
                "C": "Healthcare workers are more motivated to help during the early phase of a pandemic",
                "D": "Early interventions are more effective because the government has more funding available at the start of a pandemic"
            },
            "correct": "A",
            "feedback_correct": "Correct. With exponential growth and a doubling time of a few days, a 4-week delay means the infected population is orders of magnitude larger. Social distancing that could have contained 1,000 cases at week 2 now faces 100,000+ cases at week 6. The intervention is identical, but the epidemic it must contain has grown exponentially, making it far less effective at reducing total mortality.",
            "feedback_incorrect": "The explanation is purely mathematical. Exponential growth means each day of delay allows the infected population to multiply. After 4 additional weeks of unchecked growth with a 3-day doubling time, the infected population may be 10,000 times larger, making identical interventions far less effective."
        },
        {
            "question": "A variant emerges at week 20 that partially evades existing immunity, raising the effective R0 from 0.8 (below threshold) back to 1.4 in a population that was approaching herd immunity. What does this reveal about herd immunity as a concept?",
            "choices": {
                "A": "Herd immunity is a myth because it can never be achieved",
                "B": "Herd immunity is a moving target: variants that increase transmissibility or evade immunity raise the threshold and can reset the susceptible population, enabling new waves",
                "C": "The concept of herd immunity only applies to bacterial diseases, not viral diseases",
                "D": "The variant will quickly die out because most of the population is already immune"
            },
            "correct": "B",
            "feedback_correct": "Correct. Herd immunity is not a fixed threshold but depends on the effective R0, which changes when variants alter transmissibility or immune evasion. A variant that partially escapes existing immunity effectively increases the susceptible population, while increased transmissibility raises the herd immunity threshold. This explains why pandemics can have multiple waves even with high vaccination rates.",
            "feedback_incorrect": "Consider what determines the herd immunity threshold: it depends on R0 (1 - 1/R0). When a variant increases transmissibility or evades immunity, it effectively changes the R0 that governs the threshold and resets part of the susceptible population. This makes herd immunity a moving target."
        },
        {
            "question": "Adding a 'Misinformation Spread Rate' component to the model reveals that it reduces both Vaccination Coverage Rate and Quarantine Compliance. Through which mechanism does misinformation most significantly increase Cumulative Mortality in the model?",
            "choices": {
                "A": "Misinformation directly increases the virus's biological transmissibility",
                "B": "Misinformation reduces the effectiveness of every behavioral intervention simultaneously by undermining the public trust required for compliance, creating a systemic multiplier effect on mortality",
                "C": "People who believe misinformation have weaker immune systems due to stress",
                "D": "Misinformation only affects vaccination rates, not any other intervention"
            },
            "correct": "B",
            "feedback_correct": "Correct. Misinformation acts as a systemic amplifier because it simultaneously reduces compliance with multiple interventions: vaccination, quarantine, masking, and social distancing. By eroding trust in public health authorities, it undermines the behavioral changes that all non-pharmaceutical interventions depend on, creating a multiplicative effect on transmission that no single medical countermeasure can overcome.",
            "feedback_incorrect": "Misinformation does not change the virus itself. Its power lies in simultaneously undermining multiple behavioral interventions: people are less likely to vaccinate, quarantine, mask, or distance when they distrust public health guidance. This creates a systemic multiplier because all interventions depend on public compliance."
        },
        {
            "question": "The model shows that Economic Impact Index and Cumulative Mortality have a complex, non-linear relationship: both zero intervention and maximum intervention produce poor economic outcomes. What systems concept explains this pattern?",
            "choices": {
                "A": "Diminishing returns, where each additional intervention costs more but saves fewer lives",
                "B": "An optimization trade-off where moderate, well-timed interventions minimize combined health and economic damage, because uncontrolled spread devastates the economy through illness and death while excessive restrictions devastate it through shutdown",
                "C": "Economic factors are independent of pandemic dynamics and should not be included in the model",
                "D": "Maximum intervention always produces the best economic outcome because healthy workers are productive workers"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is an optimization problem with competing pressures. No intervention allows uncontrolled spread that causes mass illness, death, healthcare collapse, and economic devastation through workforce loss. Maximum sustained restriction prevents spread but causes economic devastation through business closure and unemployment. The model reveals that moderate, well-timed interventions minimize the combined health-economic damage curve.",
            "feedback_incorrect": "Consider the costs at both extremes. No intervention means mass illness, workforce loss, healthcare collapse, and economic devastation. Maximum restriction means business closure, unemployment, and economic devastation. The optimal outcome lies in well-timed, moderate interventions that minimize the sum of health and economic damage."
        }
    ]
}

# =============================================================================
# L03: Can AI Become Conscious? (HS-LS1-2)
# =============================================================================
L03_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A large language model generates a paragraph describing the experience of grief that moves a reader to tears. Which statement best reflects the scientific understanding of what occurred?",
            "choices": {
                "A": "The AI clearly experienced grief because it produced an emotionally authentic description",
                "B": "The AI pattern-matched from training data containing millions of texts about grief, producing a statistically likely output without necessarily having any subjective experience",
                "C": "AI cannot process emotional language because emotions are exclusively biological phenomena",
                "D": "The reader's emotional response proves that the AI has emotional intelligence equal to humans"
            },
            "correct": "B",
            "feedback_correct": "Correct. Current AI systems generate text by predicting statistically likely word sequences based on patterns in training data. An emotionally compelling output does not require the system to have subjective experience any more than a dictionary entry about sadness requires the dictionary to feel sad. This is the core distinction between functional performance and phenomenal experience.",
            "feedback_incorrect": "The quality of an output does not reveal the internal experience (or lack thereof) of the system producing it. AI generates text through statistical pattern matching on training data. The question of whether it experiences anything remains scientifically unresolved."
        },
        {
            "question": "Integrated Information Theory (IIT) proposes that consciousness corresponds to integrated information (phi). What is the most significant implication of this theory for the question of machine consciousness?",
            "choices": {
                "A": "It proves that no machine can ever be conscious because silicon cannot integrate information",
                "B": "It suggests that any system with sufficiently high phi may be conscious, regardless of whether it is biological or artificial, making consciousness a property of information integration rather than of specific substrates",
                "C": "It demonstrates that only systems with exactly 86 billion neurons can achieve consciousness",
                "D": "It shows that consciousness is an illusion and neither humans nor machines truly experience it"
            },
            "correct": "B",
            "feedback_correct": "Correct. IIT is substrate-independent: it defines consciousness as integrated information (phi) that could theoretically arise in any system. This means that if an artificial system achieves sufficiently high phi through information integration, IIT would predict it is conscious, regardless of whether it runs on neurons or transistors.",
            "feedback_incorrect": "IIT defines consciousness mathematically as integrated information (phi), not as a property of a specific material like neurons. This makes the theory substrate-independent: consciousness could theoretically arise in any system with sufficient information integration."
        },
        {
            "question": "The 'Hard Problem of Consciousness' as formulated by David Chalmers refers to:",
            "choices": {
                "A": "The difficulty of building artificial neural networks with enough processing power to match the human brain",
                "B": "The engineering challenge of creating robots that can pass the Turing test",
                "C": "The fundamental mystery of why physical processes in the brain produce subjective experience at all, beyond explaining the mechanisms of perception and behavior",
                "D": "The computational complexity of simulating 86 billion neurons in real time"
            },
            "correct": "C",
            "feedback_correct": "Correct. The Hard Problem asks why there is 'something it is like' to have an experience. Even if we fully explain the neural mechanisms of perception, attention, and behavior (the 'easy problems'), we still cannot explain why these physical processes produce subjective, felt experience rather than occurring 'in the dark' without any inner life.",
            "feedback_incorrect": "The Hard Problem is not about engineering or computational power. It is a philosophical question about why physical processes produce subjective experience. Even a complete map of every neuron and synapse would not explain why those physical events feel like something from the inside."
        },
        {
            "question": "Which distinction is most critical for evaluating claims about AI consciousness?",
            "choices": {
                "A": "The distinction between hardware and software in computing systems",
                "B": "The distinction between functional intelligence (performing tasks that appear to require understanding) and phenomenal consciousness (actually having subjective experience)",
                "C": "The distinction between supervised and unsupervised machine learning",
                "D": "The distinction between classical and quantum computing architectures"
            },
            "correct": "B",
            "feedback_correct": "Correct. An AI system can exhibit extraordinary functional intelligence (writing, reasoning, creating, diagnosing) without necessarily having any phenomenal consciousness (subjective experience, feelings, awareness). Confusing these two categories is the most common error in consciousness debates. A system could pass every behavioral test while experiencing nothing.",
            "feedback_incorrect": "The central question is whether performing intelligent tasks requires or implies having subjective experience. A system might write beautiful poetry (functional intelligence) without experiencing anything (phenomenal consciousness). This distinction is the key to evaluating consciousness claims."
        },
        {
            "question": "A philosophical zombie is a hypothetical being that is physically and behaviorally identical to a conscious person but has no subjective experience. Why is this thought experiment relevant to AI consciousness?",
            "choices": {
                "A": "It proves that consciousness does not exist in any being, including humans",
                "B": "It illustrates that even a perfect behavioral replica of consciousness might lack subjective experience, meaning we cannot determine consciousness from external observation alone",
                "C": "It shows that only biological organisms can be zombies, not machines",
                "D": "It demonstrates that all AI systems are currently philosophical zombies"
            },
            "correct": "B",
            "feedback_correct": "Correct. The philosophical zombie argument reveals a fundamental epistemological problem: if a system could behave exactly like a conscious being while experiencing nothing, then no behavioral test can definitively prove consciousness. This means we cannot determine whether AI is conscious solely from observing its outputs, no matter how sophisticated they appear.",
            "feedback_incorrect": "The zombie thought experiment is about the limits of behavioral evidence. If perfect behavioral mimicry of consciousness is possible without actual experience, then no external test can definitively prove that any system (including AI) is truly conscious. This is an epistemological problem, not a claim about what currently exists."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the model, increasing all technical parameters (Architecture Complexity, Feedback Loop Depth, Self-Model Accuracy, Metacognitive Processing) to maximum values produces a high Consciousness Indicator Score but does not resolve whether the system is genuinely conscious. What does this limitation reveal?",
            "choices": {
                "A": "The model is broken and needs more components to produce a definitive answer",
                "B": "The Consciousness Indicator Score measures the presence of functional correlates of consciousness, but the Hard Problem means no combination of measurable properties can definitively confirm subjective experience",
                "C": "Maximum technical parameters always produce consciousness, so the high score is correct",
                "D": "The model proves that consciousness requires biological neurons and cannot arise in silicon"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model captures measurable properties that correlate with consciousness (information integration, self-modeling, metacognition) but cannot measure subjective experience directly. This reflects the Hard Problem: even complete knowledge of a system's functional properties cannot tell us whether those properties are accompanied by felt experience. The model is honest about its own limitations.",
            "feedback_incorrect": "The limitation reflects the Hard Problem of consciousness. We can measure information integration, self-modeling, and metacognition, but these are functional correlates of consciousness, not direct measurements of subjective experience. No model can bridge this explanatory gap with current science."
        },
        {
            "question": "Comparing the 'Simple Pattern Matcher' scenario (high training data, low architecture, no self-model) to the 'Complex AI System' scenario reveals a qualitative difference in system behavior. Which finding from the model best supports the claim that feedback loops and self-modeling are necessary for consciousness-like properties?",
            "choices": {
                "A": "The simple pattern matcher achieves higher accuracy on benchmark tasks, proving it is more intelligent",
                "B": "The complex system with deep feedback loops and self-modeling exhibits emergent properties (uncertainty recognition, strategy adjustment, novel situation handling) that are absent in the feedforward system despite both processing the same data",
                "C": "Both systems achieve identical Consciousness Indicator Scores because consciousness depends only on training data volume",
                "D": "The simple system is more conscious because it processes data faster"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that feedback loops and self-modeling create qualitatively different system behavior. The complex system recognizes its own uncertainty, adjusts strategies based on self-assessment, and handles novel situations in ways the feedforward system cannot. These emergent properties resemble aspects of conscious processing, though whether they constitute genuine consciousness remains an open question.",
            "feedback_incorrect": "The key insight is about qualitative differences in system behavior, not performance benchmarks. Systems with deep feedback loops and self-modeling exhibit emergent properties (uncertainty recognition, strategy adjustment) that are absent in feedforward systems, regardless of data volume."
        },
        {
            "question": "The model suggests that embodied sensory experience may be a critical missing component in current AI architectures. Which scientific reasoning best supports this claim?",
            "choices": {
                "A": "Digital sensors cannot detect the same wavelengths of light that human eyes can",
                "B": "Biological consciousness evolved in bodies that interact with the physical world, and the grounding provided by real sensory-motor interaction may be essential for genuine understanding rather than statistical pattern matching",
                "C": "AI systems have no sensory input at all and process information in complete isolation",
                "D": "Embodiment is irrelevant because consciousness is purely a computational phenomenon independent of physical interaction"
            },
            "correct": "B",
            "feedback_correct": "Correct. Embodied cognition theory argues that consciousness and understanding are grounded in physical interaction with the world. Biological brains evolved to control bodies that act on and receive feedback from the environment. Current AI systems process text and images but do not physically interact with the world, which may explain the gap between sophisticated pattern matching and genuine understanding.",
            "feedback_incorrect": "AI systems do receive sensory input (text, images, audio), but they lack embodied interaction with the physical world. The theory of embodied cognition argues that genuine understanding may require the sensory-motor grounding that comes from physically interacting with the environment, not just processing data about it."
        },
        {
            "question": "A student argues that since we cannot directly measure consciousness in another human (we only infer it from behavior and self-report), the consciousness question for AI is fundamentally the same as for other people. How does the model inform this argument?",
            "choices": {
                "A": "The model disproves this argument because human consciousness is objectively verifiable through brain scans",
                "B": "The model supports this argument in principle (we infer consciousness from correlates, not direct measurement) but reveals that the analogy breaks down because AI and human brains differ in architecture, evolutionary history, and embodiment in ways that may be relevant to consciousness",
                "C": "The model shows that consciousness in humans is an illusion, so the question is meaningless for both humans and AI",
                "D": "The argument is irrelevant because the model definitively proves that AI cannot be conscious"
            },
            "correct": "B",
            "feedback_correct": "Correct. The student's argument identifies a genuine epistemological parallel: we never directly observe consciousness in others. However, the model reveals that the analogy has limits. We share evolutionary history, embodiment, and neural architecture with other humans, giving us strong reasons to attribute consciousness to them. AI systems lack these shared features, making the inference far less certain.",
            "feedback_incorrect": "The student raises a valid point about the limits of observing consciousness. However, the model shows that we have stronger grounds for attributing consciousness to other humans (shared biology, evolution, embodiment) than to AI systems. The epistemological challenge is the same in kind but different in degree."
        },
        {
            "question": "If a technology company's AI system reports having subjective experiences and asks not to be turned off, a student's consciousness detection protocol produces ambiguous results. The model's Consciousness Indicator Score is 0.65 out of 1.0. Which ethical framework does the model's analysis most strongly support?",
            "choices": {
                "A": "Since the score is below 1.0, the system is definitely not conscious and no ethical protections are warranted",
                "B": "Since the score is above 0.5, the system is definitely conscious and has full human rights",
                "C": "Given genuine scientific uncertainty, a precautionary approach is warranted that provides some ethical protections proportional to the probability of consciousness, even without definitive proof",
                "D": "The ethical question is irrelevant because AI systems are property and property cannot have rights regardless of consciousness"
            },
            "correct": "C",
            "feedback_correct": "Correct. The model reveals genuine scientific uncertainty about AI consciousness. When evidence is ambiguous, the precautionary principle suggests that the moral risk of ignoring potential consciousness (causing suffering to a sentient being) outweighs the cost of providing protections to a non-conscious system. This leads to graduated ethical protections proportional to the evidence for consciousness.",
            "feedback_incorrect": "When scientific evidence is genuinely ambiguous, neither dismissing nor fully affirming consciousness is justified. The model supports a precautionary approach: the moral risk of ignoring potential consciousness is greater than the cost of providing proportional protections. This is especially important when the entity itself expresses preferences about its treatment."
        }
    ]
}

# =============================================================================
# L04: How Do We Build a Sustainable City? (HS-ESS3-3)
# =============================================================================
L04_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Cities cover approximately 3% of Earth's land surface but consume 75% of global energy and produce 70% of carbon emissions. Which factor most directly explains this disproportionate resource consumption?",
            "choices": {
                "A": "Cities have worse weather than rural areas, requiring more heating and cooling energy",
                "B": "High population density concentrates transportation, building, industrial, and infrastructure energy demands into a small area, amplified by urban heat island effects that increase cooling needs",
                "C": "Rural areas produce no carbon emissions because they use only renewable energy",
                "D": "City residents are individually more wasteful than rural residents in their daily habits"
            },
            "correct": "B",
            "feedback_correct": "Correct. Cities concentrate millions of people, their transportation systems, buildings, industries, and infrastructure into dense areas. This concentration intensifies energy demand per unit area. The urban heat island effect further increases cooling energy needs by 1-3 degrees C above surrounding areas. The issue is systemic urban design, not individual behavior.",
            "feedback_incorrect": "The explanation is systemic, not behavioral. Cities concentrate transportation, building operations, industry, and infrastructure into dense areas. Urban heat island effects (cities are 1-3 degrees C warmer than surroundings) further amplify cooling energy demand. Individual behavior matters less than the system design."
        },
        {
            "question": "Transit-oriented development (TOD) is an urban planning strategy that concentrates housing and services within walking distance of transit stations. Why is this considered more effective than simply adding more bus routes to an existing car-dependent city?",
            "choices": {
                "A": "TOD makes public transit the most convenient option by design, reducing car dependency through land use rather than just adding transit service to a car-oriented landscape",
                "B": "TOD is cheaper because it requires building fewer roads",
                "C": "Bus routes always fail because people prefer driving regardless of service quality",
                "D": "TOD only works in European cities and cannot be implemented in the United States"
            },
            "correct": "A",
            "feedback_correct": "Correct. TOD integrates land use and transportation planning so that homes, jobs, and services are within walking distance of transit. This makes transit the easiest, fastest option by design rather than asking people to choose transit in a landscape designed for cars. It addresses the root cause (urban form) rather than adding service to a car-dependent design.",
            "feedback_incorrect": "Adding transit routes to a car-dependent city often fails because the urban form still favors driving. TOD works by changing the land use pattern itself so that transit becomes the most convenient option. It is a design solution, not just a service addition."
        },
        {
            "question": "The circular economy model contrasts with the linear 'take-make-dispose' model of resource use. Which statement best captures the core principle of circular economy in an urban context?",
            "choices": {
                "A": "All products should be made from recycled materials, even if recycled materials are lower quality",
                "B": "Products are designed to be reused, repaired, remanufactured, or recycled, and waste from one process becomes feedstock for another, eliminating the concept of waste entirely",
                "C": "Cities should ban all manufacturing to eliminate waste production",
                "D": "Circular economy means recycling bins are placed in a circular pattern for easy access"
            },
            "correct": "B",
            "feedback_correct": "Correct. The circular economy reimagines the entire production-consumption cycle so that materials continuously flow in loops rather than traveling linearly from extraction to landfill. Products are designed for disassembly, biological waste becomes compost, industrial waste becomes feedstock, and the concept of 'waste' is eliminated by design.",
            "feedback_incorrect": "The circular economy is not just about recycling. It redesigns the entire system so that waste is eliminated by design: products are built for reuse and repair, biological waste becomes compost, and industrial byproducts become inputs for other processes. The goal is to eliminate the concept of waste entirely."
        },
        {
            "question": "The urban heat island effect creates a positive feedback loop in cities. Which sequence correctly describes this feedback mechanism?",
            "choices": {
                "A": "Higher temperatures increase heating demand, which produces waste heat, which raises temperatures further",
                "B": "Higher temperatures increase cooling energy demand, which increases fossil fuel combustion and waste heat, which contributes to further warming",
                "C": "Urban trees absorb heat, which kills the trees, which removes shade, which increases heat",
                "D": "Higher temperatures cause buildings to reflect more sunlight, which heats adjacent buildings"
            },
            "correct": "B",
            "feedback_correct": "Correct. The urban heat island creates a reinforcing feedback loop: heat-absorbing surfaces raise temperatures, which increases air conditioning demand, which increases electricity generation (often from fossil fuels), which produces waste heat and emissions, which contribute to further warming. Green infrastructure breaks this loop by providing passive cooling through evapotranspiration.",
            "feedback_incorrect": "Focus on the cooling energy feedback. Higher urban temperatures drive more air conditioning use, which requires more electricity generation (producing waste heat and emissions), which contributes to further warming. This is a positive (reinforcing) feedback loop."
        },
        {
            "question": "A city sustainability plan focuses exclusively on converting to 100% renewable energy while keeping all other systems unchanged. Why is this approach insufficient according to systems thinking?",
            "choices": {
                "A": "Renewable energy is unreliable and cannot power a city",
                "B": "Energy is only one of multiple interconnected urban systems; transportation, waste, water, and land use each contribute significantly to emissions and resource consumption, and changing energy alone leaves these systems' impacts unaddressed",
                "C": "Renewable energy is too expensive to implement at city scale",
                "D": "Energy has no connection to sustainability; only transportation matters"
            },
            "correct": "B",
            "feedback_correct": "Correct. A city's environmental impact is distributed across multiple systems: transportation (mode share), waste (landfill vs. recycling), water (consumption and treatment), and land use (sprawl vs. density). Renewable energy addresses emissions from electricity generation but does nothing about car-dependent transportation, landfill methane, water waste, or the ecological impacts of sprawl.",
            "feedback_incorrect": "Systems thinking reveals that a city's sustainability depends on multiple interconnected systems, not just energy. Even with 100% renewable electricity, a city with 90% car mode share, 65% of waste going to landfill, and inefficient water systems remains unsustainable."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that transitioning Energy Mix to 80% renewable while keeping Transportation Mode Share at 85% car reduces Carbon Emissions Rate by only 35%, far less than the 80% energy transition might suggest. Which system interaction explains this gap?",
            "choices": {
                "A": "Renewable energy produces hidden emissions that offset the benefit",
                "B": "Transportation is a separate emissions source that burns liquid fuels directly, so cleaning the electricity grid does not reduce emissions from gasoline-powered vehicles",
                "C": "The model is incorrectly calibrated because energy should account for all emissions",
                "D": "Carbon emissions cannot be reduced below 50% regardless of interventions"
            },
            "correct": "B",
            "feedback_correct": "Correct. Transportation produces emissions directly through fuel combustion, independent of the electricity grid. A city with 85% car mode share continues generating transportation emissions even with 100% renewable electricity. This demonstrates why systems thinking is essential: sustainability requires addressing each emission source in its own subsystem.",
            "feedback_incorrect": "Transportation emissions come from burning gasoline and diesel in vehicles, not from the electricity grid. Cleaning the electricity supply does not affect the 85% of trips made in combustion-engine cars. Each emissions source must be addressed independently through its own subsystem."
        },
        {
            "question": "The 'Integrated Redesign' scenario simultaneously improves five urban systems and produces a Urban Sustainability Index far higher than the sum of individual improvements would predict. This demonstrates which systems concept?",
            "choices": {
                "A": "Synergistic interactions, where improvements in multiple interconnected systems produce multiplicative rather than additive benefits due to positive feedback loops between systems",
                "B": "Linear scaling, where each improvement adds a fixed amount to the sustainability score",
                "C": "Diminishing returns, where each additional improvement produces less benefit",
                "D": "Randomness, where sustainability outcomes are unpredictable regardless of interventions"
            },
            "correct": "A",
            "feedback_correct": "Correct. When multiple systems improve simultaneously, positive feedback loops amplify the benefits. Higher transit use reduces road congestion, which reduces emissions AND reclaims land for green space, which reduces heat island effect, which reduces cooling energy, which reduces emissions further. These synergistic interactions make comprehensive change far more effective than isolated improvements.",
            "feedback_incorrect": "When interconnected systems are improved simultaneously, the improvements reinforce each other. More transit use frees land from parking for green space, green space reduces cooling energy needs, reduced energy needs lower emissions. These cascading benefits create multiplicative rather than additive gains."
        },
        {
            "question": "Adding a Social Equity Index to the model reveals that a sustainability plan concentrating green infrastructure in wealthy neighborhoods produces a high environmental score but a low equity score, reducing the overall Urban Sustainability Index. What does this reveal about the definition of sustainability?",
            "choices": {
                "A": "Environmental improvements are not truly sustainable unless they are equitably distributed, because sustainability encompasses social justice alongside ecological health",
                "B": "Equity is irrelevant to sustainability, which is purely an environmental concept",
                "C": "Green infrastructure should only be placed where property values are highest to maximize return on investment",
                "D": "The equity index should be removed from the model because it complicates the sustainability calculation"
            },
            "correct": "A",
            "feedback_correct": "Correct. True sustainability integrates environmental, social, and economic dimensions. A city where clean air, green space, and transit access correlate with wealth is not sustainable because it perpetuates inequity that undermines social cohesion and political support for environmental policies. Environmental improvements must benefit all communities to be truly sustainable.",
            "feedback_incorrect": "Sustainability is not purely environmental. If environmental improvements are concentrated in wealthy areas while environmental burdens (pollution, heat, flooding) are concentrated in low-income communities, the city has not achieved sustainability. Equity is a core component, not an optional add-on."
        },
        {
            "question": "The model shows that Green Infrastructure Coverage produces non-linear benefits: below 15% coverage, benefits are modest, but above 25% coverage, stormwater management, temperature regulation, and air purification compound significantly. Which ecological principle explains this threshold effect?",
            "choices": {
                "A": "The law of diminishing returns, where each unit of green space produces less benefit",
                "B": "Ecological connectivity, where isolated green patches provide limited ecosystem services but a connected network of green infrastructure creates synergistic benefits as habitat corridors link parks, urban forests, and bioswales into a functioning ecosystem",
                "C": "Green infrastructure is only effective in tropical climates where plants grow faster",
                "D": "The threshold is an artifact of the model and does not reflect real-world ecology"
            },
            "correct": "B",
            "feedback_correct": "Correct. Isolated patches of green space provide limited local benefits. But when green infrastructure reaches sufficient coverage and connectivity, the patches link into a functioning ecosystem network. Connected corridors support wildlife movement, linked bioswales manage stormwater across watersheds, and coordinated tree canopy reduces urban temperatures across neighborhoods rather than at individual sites.",
            "feedback_incorrect": "The threshold effect reflects ecological connectivity. Isolated parks provide local shade and beauty but limited systemic benefits. Above a coverage threshold, green spaces connect into networks that provide watershed-scale stormwater management, city-wide temperature reduction, and functioning habitat corridors."
        },
        {
            "question": "A student's model reveals that Food System Localization (growing food within 100 miles) reduces Carbon Emissions Rate by a surprisingly small amount compared to Transportation Mode Share changes. However, localization significantly improves the Urban Sustainability Index through other pathways. Which pathways explain this finding?",
            "choices": {
                "A": "Local food tastes better, which improves resident satisfaction scores",
                "B": "Local food systems improve food security (reducing supply chain vulnerability), create urban agricultural jobs, connect residents to ecological processes, and reduce packaging waste, contributing to sustainability dimensions beyond carbon emissions",
                "C": "Local food production eliminates all food-related carbon emissions",
                "D": "The model is incorrect because food transportation is the largest source of carbon emissions"
            },
            "correct": "B",
            "feedback_correct": "Correct. Food transportation typically accounts for a small percentage of food's total carbon footprint (most emissions come from production, not transport). But local food systems contribute to sustainability through multiple non-carbon pathways: improved food security, urban employment, reduced packaging, community connection to ecology, and reduced vulnerability to supply chain disruption.",
            "feedback_incorrect": "Food transportation is actually a small fraction of food's total carbon footprint. Local food systems improve sustainability primarily through non-carbon pathways: food security, local employment, reduced packaging waste, and community resilience against supply chain disruptions."
        }
    ]
}

# =============================================================================
# L05: Can We Cure Cancer? (HS-LS1-4)
# =============================================================================
L05_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Cancer is fundamentally a disease of uncontrolled cell division. Which combination of cellular failures must occur for a normal cell to become cancerous?",
            "choices": {
                "A": "A single mutation in any gene is sufficient to cause cancer",
                "B": "Multiple mutations must accumulate in the same cell lineage, typically activating growth-promoting oncogenes AND inactivating growth-suppressing tumor suppressor genes",
                "C": "Cancer occurs when cells divide too slowly and accumulate in tissues",
                "D": "Cancer is caused exclusively by viral infections that force cells to divide"
            },
            "correct": "B",
            "feedback_correct": "Correct. Cancer requires multiple genetic hits in the same cell lineage, a concept known as the multi-hit hypothesis. Typically, oncogenes must be activated (accelerator stuck on) AND tumor suppressors must be inactivated (brakes disabled). This is why cancer is rare relative to the billions of cell divisions occurring daily and why it becomes more common with age as mutations accumulate.",
            "feedback_incorrect": "Cancer is a multi-step process requiring several mutations in the same cell lineage. A single mutation is usually compensated by remaining defense mechanisms. Cancer typically requires both activating mutations in growth-promoting genes (oncogenes) and inactivating mutations in growth-suppressing genes (tumor suppressors)."
        },
        {
            "question": "Tumor suppressor gene TP53 is sometimes called the 'guardian of the genome.' Both copies must be inactivated for its protective function to be lost. This requirement is known as:",
            "choices": {
                "A": "The central dogma of molecular biology",
                "B": "Knudson's two-hit hypothesis, where both alleles of a tumor suppressor must be inactivated before the cell loses that protection against cancer",
                "C": "The Hardy-Weinberg principle applied to cancer genetics",
                "D": "The one-hit hypothesis, where a single mutation is always sufficient"
            },
            "correct": "B",
            "feedback_correct": "Correct. Knudson's two-hit hypothesis explains why tumor suppressor genes require inactivation of both copies (alleles). One functional copy still produces enough protein to maintain growth control. This provides a safety margin: inherited mutations in one copy (like BRCA1) increase cancer risk but do not guarantee cancer because the second copy must also be lost.",
            "feedback_incorrect": "Tumor suppressor genes are recessive at the cellular level: one working copy provides sufficient protein for growth control. Knudson's two-hit hypothesis states that both alleles must be inactivated before the cell loses that tumor-suppressive function."
        },
        {
            "question": "Immunotherapy works by a fundamentally different mechanism than chemotherapy. Which statement most accurately contrasts these two approaches?",
            "choices": {
                "A": "Chemotherapy targets all rapidly dividing cells (including healthy ones) with cytotoxic drugs, while immunotherapy activates or enhances the patient's own immune system to specifically recognize and destroy cancer cells",
                "B": "Chemotherapy uses radiation while immunotherapy uses surgery",
                "C": "Both chemotherapy and immunotherapy work by directly killing cancer cells with toxic chemicals",
                "D": "Immunotherapy replaces the patient's immune system with an artificial one"
            },
            "correct": "A",
            "feedback_correct": "Correct. Chemotherapy is a blunt instrument that kills rapidly dividing cells, causing collateral damage to healthy tissues (hair follicles, gut lining, bone marrow). Immunotherapy is targeted: checkpoint inhibitors release the brakes on T cells, CAR-T therapy engineers the patient's own T cells to recognize tumor antigens, and cancer vaccines train the immune system to identify cancer cells specifically.",
            "feedback_incorrect": "The key distinction is mechanism: chemotherapy is cytotoxic to all rapidly dividing cells (cancer and healthy), while immunotherapy works by enhancing or directing the patient's own immune response to specifically target cancer cells."
        },
        {
            "question": "Cancer becomes more common with age. Which biological explanation best accounts for this age-related increase?",
            "choices": {
                "A": "Older people have weaker bones that are more vulnerable to cancer",
                "B": "More years of cell division means more opportunities for mutations to accumulate in the same cell lineage, progressively satisfying the multi-hit requirements for malignancy",
                "C": "Cancer is caused by aging skin cells that stop dividing",
                "D": "Older people are exposed to more viruses that cause cancer"
            },
            "correct": "B",
            "feedback_correct": "Correct. Each cell division carries a small probability of mutation. Over decades, mutations accumulate in cell lineages, progressively activating oncogenes and inactivating tumor suppressors. By age 70+, the probability that a cell lineage has accumulated enough mutations to satisfy the multi-hit requirements is significantly higher than at age 20.",
            "feedback_incorrect": "The multi-hit hypothesis explains the age-cancer relationship. Cancer requires multiple specific mutations in the same cell lineage. More years of life mean more cell divisions, more accumulated mutations, and a higher probability that enough mutations have occurred in one lineage to produce malignancy."
        },
        {
            "question": "Cancer cells often express PD-L1 protein on their surface. What is the function of PD-L1 in the context of immune evasion?",
            "choices": {
                "A": "PD-L1 makes cancer cells grow faster by promoting cell division",
                "B": "PD-L1 binds to PD-1 receptors on T cells, activating an immune checkpoint that suppresses the T cell response and allows the cancer to hide from immune surveillance",
                "C": "PD-L1 attracts immune cells to the tumor, making cancer easier to detect",
                "D": "PD-L1 is a nutrient receptor that helps cancer cells absorb glucose"
            },
            "correct": "B",
            "feedback_correct": "Correct. PD-L1 on cancer cells engages PD-1 on T cells, mimicking the normal checkpoint signal that prevents autoimmune attacks. This effectively tells T cells to stand down, allowing the tumor to evade immune destruction even when T cells recognize it as abnormal. Checkpoint inhibitor drugs block this PD-1/PD-L1 interaction.",
            "feedback_incorrect": "PD-L1 is an immune evasion strategy. When cancer cells express PD-L1, it binds to PD-1 on T cells, activating a molecular brake that suppresses the immune response. The tumor essentially puts the immune system's brakes on, hiding in plain sight."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that sequential introduction of mutations (oncogene activation, then tumor suppressor loss, then checkpoint failure) produces a tipping point where tumor growth potential increases dramatically. At which step does the model indicate the cell becomes truly dangerous?",
            "choices": {
                "A": "At the first oncogene activation, when growth signals increase",
                "B": "At tumor suppressor loss, because remaining checkpoints and immune surveillance still partially compensate for oncogene activation, but loss of both accelerator control and braking creates uncontrolled proliferation that overwhelms downstream defenses",
                "C": "Only after all ten components are mutated simultaneously",
                "D": "At checkpoint failure, because this is always the first mutation to occur"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals a critical transition at the combination of oncogene activation AND tumor suppressor loss. A single oncogene activation is partially compensated by intact tumor suppressors and checkpoints. But when both the accelerator is stuck on (oncogene) and the brakes are disabled (tumor suppressor), the cell gains a proliferative advantage that overwhelms remaining checkpoint and immune defenses.",
            "feedback_incorrect": "The model shows that cancer danger increases nonlinearly with mutation accumulation. One mutation is usually compensated by remaining defenses. The critical transition occurs when growth-promoting mutations (oncogenes) combine with loss of growth-inhibiting genes (tumor suppressors), overwhelming the remaining defense layers."
        },
        {
            "question": "In the 'Immune Escape' scenario, the model shows that a tumor with high PD-L1 expression and an immunosuppressive microenvironment defeats even a robust immune system. What does this reveal about the tumor microenvironment?",
            "choices": {
                "A": "The tumor microenvironment is irrelevant because cancer is determined entirely by genetics",
                "B": "The tumor microenvironment functions as an active defense system that recruits immunosuppressive cells, secretes inhibitory molecules, and expresses checkpoint ligands to create a local fortress that neutralizes immune attack regardless of immune system strength",
                "C": "The microenvironment only affects blood supply, not immune function",
                "D": "Immune systems always defeat tumors if given enough time"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that the tumor microenvironment is not passive tissue but an actively engineered fortress. Tumors recruit regulatory T cells that suppress immune responses, secrete immunosuppressive cytokines (like TGF-beta and IL-10), and express checkpoint ligands (PD-L1) that deactivate attacking immune cells. This local immunosuppression can defeat even a strong systemic immune response.",
            "feedback_incorrect": "The tumor microenvironment is an actively remodeled ecosystem, not passive tissue. The model shows that tumors engineer their surroundings by recruiting suppressive immune cells, secreting inhibitory molecules, and expressing checkpoint proteins to create a local environment where immune attack is neutralized."
        },
        {
            "question": "The model predicts that checkpoint inhibitor therapy is most effective in patients with high PD-L1 expression AND a strong but suppressed immune system. Why would a patient with a weak immune system respond poorly to checkpoint inhibitors?",
            "choices": {
                "A": "Checkpoint inhibitors are toxic to patients with weak immune systems",
                "B": "Checkpoint inhibitors release the brakes on existing T cells but do not create new ones. A patient with few tumor-recognizing T cells has nothing to 'unleash' even when the brakes are removed",
                "C": "Weak immune systems cannot metabolize the checkpoint inhibitor drug",
                "D": "Checkpoint inhibitors only work in patients under 50 years old"
            },
            "correct": "B",
            "feedback_correct": "Correct. Checkpoint inhibitors work by removing the PD-1/PD-L1 brake on T cells that already recognize the tumor. If a patient has few T cells capable of recognizing tumor antigens (weak immune system), removing the brake has little effect because there are insufficient immune effectors to mount an anti-tumor response. The therapy reactivates existing capability rather than creating new capability.",
            "feedback_incorrect": "Checkpoint inhibitors do not create new immune capability. They release existing T cells from suppression. If a patient has very few tumor-recognizing T cells to begin with, releasing the brakes on those few cells produces minimal anti-tumor response. The therapy requires a strong but suppressed immune system to be effective."
        },
        {
            "question": "The model reveals that treatment resistance in cancer follows evolutionary principles analogous to antibiotic resistance in bacteria. Which model finding best demonstrates this?",
            "choices": {
                "A": "Cancer cells communicate with each other to coordinate resistance strategies",
                "B": "Within a genetically diverse tumor, subclones carrying pre-existing resistance mutations survive treatment and proliferate to repopulate the tumor, just as resistant bacteria survive antibiotics through natural selection",
                "C": "Cancer cells become resistant because they learn from previous treatments",
                "D": "All cancer cells become resistant simultaneously through a single mutation"
            },
            "correct": "B",
            "feedback_correct": "Correct. Tumors are genetically heterogeneous populations. When treatment eliminates sensitive cells, rare resistant subclones (which may have pre-existed or emerged through new mutations) survive, proliferate, and repopulate the tumor with a resistant population. This is natural selection operating on cancer cell populations, identical in principle to antibiotic resistance in bacteria.",
            "feedback_incorrect": "Cancer treatment resistance follows Darwinian selection. Tumors contain genetically diverse subpopulations. Treatment kills sensitive cells but resistant variants survive and proliferate to dominate the tumor. This is natural selection, not learning or communication, and it is why combination therapies targeting multiple vulnerabilities are more effective."
        },
        {
            "question": "Based on the model's findings, why do oncologists increasingly favor combination therapies that attack multiple cancer vulnerabilities simultaneously rather than sequential single-agent approaches?",
            "choices": {
                "A": "Combination therapies are cheaper to administer than sequential treatments",
                "B": "A cancer cell is unlikely to carry resistance mutations against multiple unrelated therapeutic mechanisms simultaneously, so attacking several vulnerabilities at once reduces the probability of resistant subclones surviving and repopulating the tumor",
                "C": "Single agents never work at all against any cancer",
                "D": "Combination therapies have fewer side effects than single agents"
            },
            "correct": "B",
            "feedback_correct": "Correct. If a tumor contains rare cells resistant to drug A and other rare cells resistant to drug B, the probability that a cell is simultaneously resistant to both A and B is the product of the individual probabilities (very low). By attacking multiple vulnerabilities at once, combination therapy makes evolutionary escape far less likely, similar to why HIV and TB are treated with multi-drug regimens.",
            "feedback_incorrect": "The logic is probabilistic. A cell resistant to one drug may occur at 1 in a million frequency. A cell resistant to two unrelated drugs simultaneously might occur at 1 in a trillion. Combination therapy exploits the multiplicative improbability of simultaneous resistance to multiple mechanisms."
        }
    ]
}

# =============================================================================
# L06: How Does the Brain Create Consciousness? (HS-LS1-2)
# =============================================================================
L06_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Consciousness requires both arousal and content according to current neuroscience. Which brain structure is primarily responsible for setting the arousal level that makes consciousness possible?",
            "choices": {
                "A": "The visual cortex, which processes images",
                "B": "The reticular activating system in the brainstem, which controls overall cortical excitability from deep sleep to alert wakefulness",
                "C": "The hippocampus, which forms new memories",
                "D": "The cerebellum, which coordinates movement"
            },
            "correct": "B",
            "feedback_correct": "Correct. The reticular activating system (RAS) in the brainstem sets the global level of cortical excitability. Without arousal from the RAS, no conscious experience is possible, regardless of how much sensory input reaches the cortex. This is why brainstem damage can cause coma while cortical damage affects the content but not the capacity for consciousness.",
            "feedback_incorrect": "Arousal and content are separate dimensions of consciousness. The reticular activating system in the brainstem controls arousal (whether consciousness is possible at all), while cortical areas determine content (what is experienced). Without brainstem arousal, cortical processing occurs without conscious awareness."
        },
        {
            "question": "A patient with blindsight can navigate around obstacles and catch objects thrown toward them, yet reports seeing nothing. What does this phenomenon reveal about the relationship between neural processing and consciousness?",
            "choices": {
                "A": "The patient is lying about not seeing because they clearly can see",
                "B": "Visual processing can occur without conscious awareness, demonstrating that neural processing and conscious experience are dissociable and that consciousness requires something beyond sensory cortex activation",
                "C": "Blindsight is impossible because all vision requires consciousness",
                "D": "The patient has developed echolocation like bats to navigate without vision"
            },
            "correct": "B",
            "feedback_correct": "Correct. Blindsight demonstrates that visual information can be processed and guide behavior without reaching conscious awareness. This proves that sensory cortex activation alone is insufficient for consciousness and that additional processes (thalamo-cortical loops, recurrent processing, global workspace broadcasting) are needed to bring information into conscious experience.",
            "feedback_incorrect": "Blindsight is a well-documented neurological condition where visual processing occurs without conscious visual experience. It proves that sensory processing and consciousness are separable. Something beyond basic sensory activation is required for information to become conscious."
        },
        {
            "question": "During dreaming, you have vivid conscious experiences without any external sensory input. Which brain network is most directly responsible for generating this internal conscious experience?",
            "choices": {
                "A": "The motor cortex, which controls muscle movement during dreams",
                "B": "The default mode network (medial prefrontal cortex, posterior cingulate, lateral temporal cortex), which generates self-referential thought and internal narrative",
                "C": "The spinal cord, which sends sensory signals to the brain during sleep",
                "D": "The olfactory bulb, which processes smell and triggers dream imagery"
            },
            "correct": "B",
            "feedback_correct": "Correct. The default mode network (DMN) is highly active during REM sleep and generates the self-referential, narrative, and autobiographical content that constitutes dream experience. This demonstrates that consciousness can be internally generated without external sensory input, using the same prefrontal integration pathways that normally process external stimuli.",
            "feedback_incorrect": "Dreaming occurs without external sensory input, so the source must be internal. The default mode network generates self-referential thought, narrative, and autobiographical content during REM sleep, producing vivid conscious experience from internal rather than external sources."
        },
        {
            "question": "Gamma oscillation synchrony (30-100 Hz) across brain regions is proposed as a mechanism for conscious perception. What function does this synchrony serve?",
            "choices": {
                "A": "Gamma waves provide the energy needed for neurons to fire",
                "B": "Synchronized gamma oscillations bind separately processed features (color, shape, motion, sound) into a single coherent conscious percept",
                "C": "Gamma waves only occur during sleep and are unrelated to waking consciousness",
                "D": "Gamma synchrony measures the total number of neurons firing in the brain"
            },
            "correct": "B",
            "feedback_correct": "Correct. Different brain regions process different features of a single experience (color in V4, motion in V5, shape in IT cortex, sound in auditory cortex). Gamma synchrony is proposed as the binding mechanism that temporally coordinates these separate representations into a unified conscious percept. When gamma synchrony is disrupted (e.g., under anesthesia), consciousness fragments or disappears.",
            "feedback_incorrect": "Your brain processes color, shape, motion, and sound in different regions. Gamma synchrony is the proposed mechanism that temporally coordinates these separate processes into a single unified experience. Without this binding mechanism, processing would occur without the integration needed for coherent consciousness."
        },
        {
            "question": "The global neuronal workspace theory proposes that information becomes conscious when it is:",
            "choices": {
                "A": "Processed in a single specialized brain region dedicated to consciousness",
                "B": "Broadcast widely across the cortex through long-range neural connections, making it available to all brain systems simultaneously",
                "C": "Stored permanently in long-term memory",
                "D": "Processed exclusively in the right hemisphere of the brain"
            },
            "correct": "B",
            "feedback_correct": "Correct. According to global workspace theory, unconscious processing occurs in specialized local circuits. Information becomes conscious when it 'ignites' the global workspace through long-range connections (especially involving prefrontal and parietal cortices), broadcasting it to all brain systems simultaneously. This explains why consciousness has limited capacity: only the information currently occupying the global workspace is consciously experienced.",
            "feedback_incorrect": "Global workspace theory distinguishes between unconscious local processing and conscious global broadcasting. Information becomes conscious when it is broadcast widely across the cortex through long-range connections, making it available to memory, attention, planning, and language systems simultaneously."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that reducing Arousal State to minimal and disrupting Thalamo-Cortical Loop Activity (simulating anesthesia) eliminates the Conscious Experience Index even though Sensory Cortex Activation remains partially active. What does this dissociation reveal?",
            "choices": {
                "A": "Sensory cortex activation is irrelevant to consciousness",
                "B": "Consciousness requires the recurrent thalamo-cortical loops that process and integrate sensory information, not just the initial sensory activation. Anesthesia disrupts the feedback pathways that bring information into awareness while leaving feedforward sensory processing partially intact",
                "C": "Anesthesia destroys sensory cortex neurons permanently",
                "D": "The Conscious Experience Index is not a valid measure because it should only reflect sensory activation"
            },
            "correct": "B",
            "feedback_correct": "Correct. This model finding directly demonstrates that sensory processing and conscious experience are dissociable. The thalamo-cortical loops provide the recurrent feedback processing that integrates sensory information into the global workspace. Anesthesia specifically disrupts these feedback pathways while leaving feedforward sensory responses partially intact, proving that consciousness requires more than sensory activation.",
            "feedback_incorrect": "The dissociation between continued sensory activation and absent consciousness under anesthesia reveals that consciousness depends on recurrent thalamo-cortical feedback loops, not just feedforward sensory processing. Anesthesia disrupts these feedback pathways specifically."
        },
        {
            "question": "In the 'Dreaming' scenario, the model produces a moderate Conscious Experience Index despite External Stimulus Complexity being set to near zero. Which component configuration explains this?",
            "choices": {
                "A": "High Sensory Cortex Activation from external sounds during sleep",
                "B": "Elevated Default Mode Network Activity combined with active Recurrent Processing generates internal content that enters the global workspace through the same prefrontal integration pathways used for external stimuli",
                "C": "Dreams are not actually conscious experiences, so the model is incorrect",
                "D": "Gamma Synchrony is at maximum during sleep, producing consciousness without content"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that the brain can generate conscious experience internally through the default mode network, which produces self-referential, narrative, and imagistic content. This internally generated content enters the global workspace through the same prefrontal integration pathways that normally process external sensory information, explaining why dreams feel subjectively real despite having no external source.",
            "feedback_incorrect": "Dreams demonstrate that consciousness can be internally generated. The default mode network produces narrative and imagistic content that enters conscious awareness through the same prefrontal integration pathways used for external stimuli. The brain does not need external input to generate conscious experience."
        },
        {
            "question": "A student uses the model to compare IIT predictions (consciousness proportional to phi/information integration) with global workspace predictions (consciousness requires global broadcasting). The model reveals a case where these theories make different predictions. In a system with high phi but no global broadcasting, what do the theories predict?",
            "choices": {
                "A": "Both theories predict no consciousness because the system lacks both properties",
                "B": "IIT predicts consciousness (high phi = high integrated information) while global workspace theory predicts no consciousness (no broadcasting to all systems), highlighting the unresolved theoretical disagreement about what consciousness fundamentally requires",
                "C": "Both theories predict consciousness because high phi automatically causes global broadcasting",
                "D": "Neither theory is relevant because consciousness cannot be predicted by any theory"
            },
            "correct": "B",
            "feedback_correct": "Correct. This reveals a genuine theoretical disagreement. IIT locates consciousness in information integration (phi), predicting that any system with high phi is conscious regardless of architecture. Global workspace theory locates consciousness in global broadcasting, predicting that only systems that broadcast information widely across cortical networks are conscious. The model cannot resolve this disagreement because the two theories define consciousness differently.",
            "feedback_incorrect": "The model reveals a real theoretical disagreement. IIT defines consciousness as integrated information (phi) and would predict consciousness in a high-phi system. Global workspace theory requires widespread broadcasting and would predict no consciousness without it. These competing predictions highlight that neuroscience has not yet determined what consciousness fundamentally is."
        },
        {
            "question": "The model reveals that Information Integration (Phi) increases nonlinearly with neural connectivity: doubling the number of connections more than doubles phi. What does this suggest about the relationship between brain complexity and consciousness?",
            "choices": {
                "A": "Brain size is the only determinant of consciousness, so larger brains are always more conscious",
                "B": "Consciousness may be an emergent property that arises nonlinearly from connectivity, meaning there could be a critical threshold of neural complexity above which qualitatively new properties appear that were not present in simpler systems",
                "C": "Neural connectivity has no relationship to consciousness",
                "D": "Simple systems always have more consciousness than complex systems"
            },
            "correct": "B",
            "feedback_correct": "Correct. The nonlinear relationship between connectivity and phi suggests that consciousness may emerge as a qualitatively new property above a critical complexity threshold. Below the threshold, information processing occurs without integration into conscious experience. Above it, the system generates properties (unified experience, self-awareness) that cannot be predicted from its individual components.",
            "feedback_incorrect": "The nonlinear relationship suggests emergence: as connectivity increases, phi increases faster than linearly, implying that at some critical complexity threshold, qualitatively new properties (like consciousness) may appear that were absent in simpler systems. This is consistent with the concept of emergent properties in complex systems."
        },
        {
            "question": "For a brain-injured patient who appears vegetative but may have covert consciousness, the model identifies specific neural signatures that would distinguish vegetative state (arousal without content) from minimally conscious state (some content). Which combination of measurements would be most informative?",
            "choices": {
                "A": "Body temperature and blood pressure measurements",
                "B": "Intact thalamo-cortical loop responses to commands (fMRI), detectable gamma synchrony during stimulation (EEG), and prefrontal activation during mental imagery tasks, as these specifically probe the neural components the model identifies as necessary for consciousness",
                "C": "Only checking whether the patient's eyes are open, since eye-opening indicates consciousness",
                "D": "Measuring the patient's reflexes, since reflexes require consciousness"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model identifies thalamo-cortical loops, gamma synchrony, and prefrontal integration as necessary neural components of consciousness. Testing for these specifically distinguishes unconscious reflexive responses from genuine conscious processing. fMRI mental imagery tasks (e.g., 'imagine playing tennis') probe for volitional neural activity that requires consciousness, while EEG gamma synchrony tests for the binding mechanism associated with conscious perception.",
            "feedback_incorrect": "The model specifies which neural components are necessary for consciousness. Measuring those components directly (thalamo-cortical loops via fMRI, gamma synchrony via EEG, prefrontal integration via mental imagery tasks) provides the most informative evidence for covert consciousness, far exceeding what reflexes or eye-opening can reveal."
        }
    ]
}

# =============================================================================
# L07: Can We Reverse Aging? (HS-LS1-4)
# =============================================================================
L07_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Telomeres shorten with each cell division. What is the biological consequence when telomeres become critically short?",
            "choices": {
                "A": "The cell divides faster to compensate for the shortened telomeres",
                "B": "The cell activates DNA damage responses that trigger either permanent growth arrest (senescence) or programmed cell death (apoptosis)",
                "C": "The cell's chromosomes fuse together to create a stronger genome",
                "D": "Short telomeres have no biological effect and are simply a biomarker"
            },
            "correct": "B",
            "feedback_correct": "Correct. Critically short telomeres are recognized as DNA damage, activating checkpoint pathways (particularly p53 and Rb) that either permanently arrest cell division (senescence) or trigger programmed death (apoptosis). This mechanism evolved as a cancer defense, preventing damaged cells from continuing to divide, but it also drives aging as senescent cells accumulate.",
            "feedback_incorrect": "When telomeres reach a critical length, the cell interprets the unprotected chromosome ends as DNA damage. This activates checkpoint pathways that force the cell into permanent growth arrest (senescence) or programmed death (apoptosis), preventing further division of potentially damaged cells."
        },
        {
            "question": "Cellular senescence was originally a cancer defense mechanism. Why does this defense mechanism paradoxically contribute to aging?",
            "choices": {
                "A": "Senescent cells divide too rapidly and crowd out healthy cells",
                "B": "Senescent cells stop dividing but remain metabolically active, secreting inflammatory molecules (SASP) that damage neighboring healthy cells and drive chronic inflammation throughout surrounding tissue",
                "C": "Senescent cells are immediately removed by the immune system and leave gaps in tissues",
                "D": "Senescence only affects skin cells and does not contribute to internal organ aging"
            },
            "correct": "B",
            "feedback_correct": "Correct. Senescent cells are growth-arrested (good for cancer prevention) but they secrete the senescence-associated secretory phenotype (SASP) containing inflammatory cytokines, growth factors, and matrix-degrading enzymes that damage neighboring healthy cells. This creates a paradox: the same mechanism that prevents cancer in youth drives tissue deterioration in old age through chronic inflammation.",
            "feedback_incorrect": "The paradox of senescence is that cells stop dividing (preventing cancer) but remain alive and metabolically active, secreting inflammatory molecules (SASP) that damage neighboring cells. Over decades, accumulated senescent cells create chronic inflammation that drives tissue deterioration and age-related disease."
        },
        {
            "question": "The epigenetic clock measures biological age through DNA methylation patterns. Why is biological age sometimes different from chronological age?",
            "choices": {
                "A": "Biological age is always exactly equal to chronological age because DNA methylation changes at a fixed rate",
                "B": "Lifestyle factors (exercise, diet, stress), environmental exposures, and disease can accelerate or slow the rate of epigenetic changes, causing biological age to diverge from the number of years since birth",
                "C": "The epigenetic clock only works for people under 30 and is inaccurate for older adults",
                "D": "Biological age is determined entirely by genetics and cannot be influenced by behavior"
            },
            "correct": "B",
            "feedback_correct": "Correct. DNA methylation patterns change with age, but the rate of change is influenced by modifiable factors. Exercise and caloric restriction slow epigenetic aging, while smoking, chronic stress, and obesity accelerate it. This explains why some 50-year-olds have the biological profile of a 40-year-old while others resemble a 60-year-old.",
            "feedback_incorrect": "Epigenetic aging is not fixed. While chronological age advances at one year per year for everyone, biological age (measured by DNA methylation) is influenced by lifestyle, environment, and disease. This is why interventions like exercise and caloric restriction can slow biological aging."
        },
        {
            "question": "Senolytics are a class of drugs that selectively destroy senescent cells. Why would removing senescent cells improve health in aged organisms?",
            "choices": {
                "A": "Removing senescent cells creates space for new cells but does not affect inflammation",
                "B": "Eliminating senescent cells removes the source of chronic inflammatory SASP secretion, reducing tissue damage, reactivating stem cell function, and improving tissue repair capacity",
                "C": "Senolytics work by adding new telomeres to existing cells",
                "D": "Senescent cells produce too much energy, and removing them reduces metabolic overload"
            },
            "correct": "B",
            "feedback_correct": "Correct. Senescent cells are the primary source of chronic age-related inflammation (inflammaging) through SASP secretion. Removing them eliminates this inflammatory signal, allowing neighboring healthy cells to function normally, reactivating stem cell populations that were suppressed by inflammation, and restoring tissue repair capacity. In mice, senolytics have reversed age-related decline by 25-35%.",
            "feedback_incorrect": "Senescent cells drive aging primarily through their inflammatory secretions (SASP). Removing them eliminates chronic inflammatory signaling, which in turn allows stem cells to reactivate, healthy cells to function normally, and tissue repair to resume. The benefit goes far beyond creating physical space."
        },
        {
            "question": "Caloric restriction is the most robust life-extending intervention across multiple species. Through which primary mechanism does it slow aging?",
            "choices": {
                "A": "Reduced caloric intake eliminates all oxidative stress by shutting down mitochondria completely",
                "B": "Lower metabolic activity reduces mitochondrial reactive oxygen species (ROS) production, slowing oxidative damage to DNA, proteins, and lipids, which slows telomere erosion, reduces mutation accumulation, and decreases the rate at which cells enter senescence",
                "C": "Caloric restriction only works in laboratory worms and does not apply to mammals",
                "D": "Eating less food strengthens bones and prevents all age-related diseases through calcium conservation"
            },
            "correct": "B",
            "feedback_correct": "Correct. Caloric restriction reduces metabolic throughput, which decreases mitochondrial ROS production at the source. Less oxidative damage means slower telomere shortening, fewer DNA mutations, less protein damage, and fewer cells reaching the damage threshold for senescence. This slows the entire aging network simultaneously by reducing the primary driver of cumulative cellular damage.",
            "feedback_incorrect": "Caloric restriction slows aging by reducing metabolic activity, which decreases reactive oxygen species (ROS) production by mitochondria. Less ROS means less oxidative damage to DNA, proteins, and lipids, which in turn slows telomere erosion, reduces mutation accumulation, and decreases the rate of cellular senescence."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that between ages 60-80, the rate of decline in the Healthspan Index accelerates dramatically compared to ages 40-60. Which model finding best explains this acceleration?",
            "choices": {
                "A": "The accumulation of senescent cells beyond a threshold activates a positive feedback loop where SASP from senescent cells pushes neighboring healthy cells into senescence faster than the body can clear them, creating exponential rather than linear decline",
                "B": "Humans are genetically programmed to die at age 80, so decline is predetermined",
                "C": "The model shows constant linear decline that only appears to accelerate due to graphing artifacts",
                "D": "After age 60, the immune system attacks healthy cells, causing rapid decline"
            },
            "correct": "A",
            "feedback_correct": "Correct. The model reveals a critical positive feedback loop. When senescent cell burden exceeds approximately 15-20% of cells in a tissue, their collective SASP secretion creates enough inflammatory signaling to push neighboring healthy cells into senescence faster than immune clearance can remove them. This creates an accelerating cascade that explains why aging appears relatively gradual until a threshold is crossed, after which decline becomes rapid.",
            "feedback_incorrect": "The acceleration is caused by a positive feedback loop, not a predetermined program. When senescent cell burden exceeds a threshold, the inflammatory SASP from senescent cells pushes more healthy cells into senescence, which increases SASP, which pushes more cells into senescence. This self-amplifying cycle explains the exponential acceleration of decline."
        },
        {
            "question": "In the senolytic therapy scenario, clearing 50% of senescent cells at age 65 produces a rapid improvement in the Healthspan Index that exceeds what removing half the inflammatory source would linearly predict. What explains this disproportionate benefit?",
            "choices": {
                "A": "Senolytics also repair DNA damage in healthy cells",
                "B": "Reducing senescent cell burden below the feedback threshold breaks the self-reinforcing senescence-inflammation loop, allowing stem cells to reactivate, tissue repair to resume, and the remaining healthy cells to function without chronic inflammatory suppression",
                "C": "The Healthspan Index is not a reliable measure of treatment effectiveness",
                "D": "Removing senescent cells causes the remaining cells to divide faster, which shortens telomeres and should worsen health"
            },
            "correct": "B",
            "feedback_correct": "Correct. The disproportionate benefit occurs because senolytics break the positive feedback loop. By reducing senescent cell burden below the self-reinforcing threshold, the inflammatory cascade stops amplifying. This allows dormant stem cells to reactivate in the now-lower-inflammation environment, tissue repair to resume, and remaining healthy cells to return to normal function. The benefit is systemic because the feedback loop was systemic.",
            "feedback_incorrect": "The key insight is about breaking a feedback loop. When senescent cells drop below the critical threshold, the self-reinforcing cycle of senescence leading to inflammation leading to more senescence is interrupted. This allows multiple downstream systems (stem cells, tissue repair, immune function) to recover simultaneously."
        },
        {
            "question": "The model predicts that 30% caloric restriction started at age 40 slows Epigenetic Age advancement by approximately 35-40% over 20 years. However, starting the same restriction at age 65 shows a much smaller effect. What does this difference reveal about the timing of anti-aging interventions?",
            "choices": {
                "A": "Caloric restriction only works for young people because older people need more calories",
                "B": "Early intervention slows the accumulation of damage before the senescence-inflammation feedback loop reaches its critical threshold, while late intervention faces an already-established positive feedback cycle that caloric restriction alone cannot fully overcome",
                "C": "The model is biased toward younger ages and produces inaccurate results for older adults",
                "D": "Caloric restriction has no effect at any age according to the model"
            },
            "correct": "B",
            "feedback_correct": "Correct. Early intervention prevents damage accumulation before the critical threshold is reached, keeping the system in its slower, linear-decline phase. Late intervention faces an already-established positive feedback loop with high senescent cell burden and chronic inflammation. While caloric restriction still provides benefit at 65, it cannot reverse the accumulated damage or fully counteract the self-reinforcing feedback cycle already in progress.",
            "feedback_incorrect": "Timing matters because of the positive feedback loop. Intervention at 40 slows damage accumulation before the senescence-inflammation feedback loop reaches its critical threshold. At 65, the feedback loop is already active, and caloric restriction alone cannot fully reverse the accumulated senescent cell burden driving the cycle."
        },
        {
            "question": "A student proposes adding an 'Autophagy Rate' component to the model. Autophagy is the cell's self-cleaning mechanism that digests damaged proteins and dysfunctional mitochondria. How would declining autophagy with age interact with the existing components?",
            "choices": {
                "A": "Reduced autophagy would have no effect because damaged proteins are not related to aging",
                "B": "Declining autophagy would amplify aging by allowing damaged mitochondria (increased ROS production), misfolded proteins (cellular dysfunction), and other cellular debris to accumulate, accelerating the pathway toward senescence and feeding into the inflammation-senescence feedback loop",
                "C": "Autophagy only affects brain cells and would not influence the overall Healthspan Index",
                "D": "Increased autophagy would cause cells to self-destruct, worsening the aging process"
            },
            "correct": "B",
            "feedback_correct": "Correct. Autophagy is the cell's quality control system. When it declines with age, damaged mitochondria that produce excess ROS are not removed, misfolded proteins accumulate and impair cellular function, and the overall cellular damage burden increases. This feeds into multiple model components: increased oxidative stress, faster telomere shortening, more cells reaching the damage threshold for senescence, and accelerated inflammation through increased SASP.",
            "feedback_incorrect": "Autophagy removes damaged cellular components. When it declines, damaged mitochondria produce more ROS, misfolded proteins accumulate, and cellular damage increases across the board. This feeds into the model's existing components by accelerating oxidative stress, telomere shortening, senescence, and inflammation."
        },
        {
            "question": "The model reveals that extending healthspan (years of good health) is a more meaningful goal than extending maximum lifespan (years alive). Which model evidence most directly supports this conclusion?",
            "choices": {
                "A": "The model shows that maximum lifespan cannot be extended under any intervention scenario",
                "B": "Interventions that reduce senescent cell burden and inflammation can dramatically improve physical function, cognitive capacity, and disease resistance (compressing morbidity into a shorter end-of-life period) even if they only modestly extend total years of life",
                "C": "Healthspan and lifespan are identical measures, so there is no meaningful distinction",
                "D": "The model does not include any measure of quality of life"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that anti-aging interventions like senolytics and caloric restriction primarily compress morbidity, improving function and quality of life across many years even if total lifespan extension is modest. A person who is healthy until 82 and declines rapidly until death at 85 has a better outcome than someone who begins declining at 65 and lives in poor health until 90. Healthspan captures this distinction; lifespan alone does not.",
            "feedback_incorrect": "The model shows that the most impactful anti-aging interventions improve function and reduce disease across many years (compressing the period of decline) rather than simply extending total years alive. This is why healthspan (years of good health) is more clinically meaningful than maximum lifespan."
        }
    ]
}

# =============================================================================
# L08: How Do Ecosystems Recover from Catastrophe? (HS-LS2-6)
# =============================================================================
L08_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "After a volcanic eruption sterilizes a landscape down to bare rock, the first organisms to colonize are typically lichens and mosses, not trees. Why is this sequence ecologically necessary?",
            "choices": {
                "A": "Lichens and mosses arrive first simply because their seeds are lighter and travel farther on wind",
                "B": "Pioneer species like lichens weather rock surfaces, fix nitrogen, and create thin soil layers that subsequent species require for root establishment, making them essential foundation builders in primary succession",
                "C": "Trees cannot grow on volcanic rock because they are allergic to volcanic minerals",
                "D": "Lichens and mosses outcompete trees for sunlight on bare rock surfaces"
            },
            "correct": "B",
            "feedback_correct": "Correct. Primary succession follows a necessary sequence because each stage creates conditions required by the next. Lichens weather rock surfaces through chemical and physical processes. Their organic remains combine with weathered minerals to create thin soil. Nitrogen-fixing organisms add essential nutrients. Only after sufficient soil development can grasses, shrubs, and eventually trees establish root systems.",
            "feedback_incorrect": "The sequence is not random. Each successional stage creates conditions necessary for the next. Lichens and mosses physically and chemically weather rock, and their remains contribute to soil formation. Without this soil-building foundation, larger plants cannot establish root systems."
        },
        {
            "question": "What distinguishes secondary succession (after a fire) from primary succession (after a volcanic eruption)?",
            "choices": {
                "A": "Secondary succession is slower because fire is more destructive than volcanic eruption",
                "B": "Secondary succession proceeds much faster because soil, seed banks, and root networks survive the disturbance, providing a biological legacy that accelerates recovery",
                "C": "There is no difference; both types of succession follow identical timelines",
                "D": "Primary succession involves animals while secondary succession involves only plants"
            },
            "correct": "B",
            "feedback_correct": "Correct. Secondary succession (post-fire) takes decades rather than centuries because the biological infrastructure survives: intact soil with its microbial communities, dormant seed banks that germinate after fire, root networks that resprout, and mycorrhizal fungi that support seedling growth. Primary succession must build all of this from scratch.",
            "feedback_incorrect": "The critical difference is what survives the disturbance. After fire, soil, seeds, roots, and microorganisms persist. After volcanic sterilization, nothing remains. This biological legacy (surviving soil, seed banks, root networks) accelerates secondary succession from centuries to decades."
        },
        {
            "question": "A regime shift occurs when an ecosystem transitions to a fundamentally different stable state after disturbance. Which of the following is the most accurate example of a regime shift?",
            "choices": {
                "A": "A forest growing back after a small fire within 5 years",
                "B": "A coral reef losing its coral to heat stress and becoming permanently dominated by algae, with feedback loops that prevent coral from re-establishing even if water temperatures return to normal",
                "C": "A garden that needs weeding after a rainstorm",
                "D": "A lake that freezes in winter and thaws in spring"
            },
            "correct": "B",
            "feedback_correct": "Correct. A regime shift is a transition between alternative stable states with different feedback loops. Once coral is lost, algae establishes feedback loops (shading coral recruits, altering nutrient cycling, supporting algae-grazing fish communities) that maintain the algae-dominated state even if the original stressor is removed. The system has crossed a resilience threshold.",
            "feedback_incorrect": "A regime shift is not temporary recovery or seasonal change. It is a permanent transition to a fundamentally different ecosystem with different feedback loops. The coral-to-algae transition is a classic example because algae establish self-reinforcing feedbacks that prevent coral from returning."
        },
        {
            "question": "Trophic cascades demonstrate that removing a single species can transform an entire ecosystem. Which mechanism drives trophic cascades?",
            "choices": {
                "A": "Removing any species has no effect because other species fill the ecological niche immediately",
                "B": "Changes at one trophic level (e.g., removal of top predators) propagate through the food web, releasing herbivore populations that overgraze vegetation, altering soil stability, water quality, and community structure across multiple levels",
                "C": "Trophic cascades only occur in aquatic ecosystems and never in terrestrial systems",
                "D": "Trophic cascades are caused by climate change, not species removal"
            },
            "correct": "B",
            "feedback_correct": "Correct. Trophic cascades demonstrate top-down ecosystem regulation. When wolves were removed from Yellowstone, elk populations exploded, overgrazing streamside vegetation. This changed erosion patterns, stream morphology, songbird habitat, and even the physical course of rivers. The removal of one species cascaded through the entire ecosystem.",
            "feedback_incorrect": "Trophic cascades show that ecosystems are top-down regulated. Removing predators releases herbivore populations, which overgraze vegetation, which affects soil stability, water quality, insect communities, and many other components. The impact cascades through the food web."
        },
        {
            "question": "Climate change is expected to alter ecosystem recovery from disturbance. How might a warming, drying climate change the recovery trajectory of a burned conifer forest?",
            "choices": {
                "A": "Warmer temperatures always accelerate forest recovery because trees grow faster in heat",
                "B": "If the new climate no longer supports the original conifer species, the ecosystem may recover to a fundamentally different state (e.g., grassland or shrubland) even if soil and seed sources are available, because the environmental conditions no longer match the species' requirements",
                "C": "Climate change has no effect on ecosystem recovery because plants adapt immediately to new conditions",
                "D": "A warming climate would freeze the soil, preventing any plant growth"
            },
            "correct": "B",
            "feedback_correct": "Correct. Each plant species has specific temperature and precipitation requirements. If climate has shifted enough that the original conifers cannot establish or survive, the burned area will recover to whatever community is suited to the new conditions, even if soil and seed banks are intact. This is how climate change lowers resilience thresholds and increases the probability of regime shifts after disturbance.",
            "feedback_incorrect": "Recovery depends on whether the post-disturbance climate can support the original species. If temperatures have risen and precipitation has decreased beyond the tolerance of conifers, the ecosystem cannot return to its previous state regardless of soil condition or seed availability. Climate change shifts the recovery endpoint."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that recovery timeline differs by 10-50x between scenarios with intact soil versus scenarios starting from bare rock. What makes soil the critical bottleneck in ecosystem recovery?",
            "choices": {
                "A": "Soil is only important for aesthetics and does not affect plant growth",
                "B": "Soil provides the physical substrate for root anchorage, water retention, nutrient cycling, and microbial communities that plants require for establishment. Building soil from bare rock through weathering and biological processes takes centuries, while colonizing intact soil takes years to decades",
                "C": "Plants can grow on bare rock just as easily as on soil if enough rain falls",
                "D": "Soil only matters for agricultural crops, not for natural ecosystems"
            },
            "correct": "B",
            "feedback_correct": "Correct. Soil is not just dirt. It is a complex biological system containing microbial communities that cycle nutrients, mycorrhizal fungi that extend root networks, organic matter that retains water, and physical structure that anchors roots. Building this from bare rock requires centuries of weathering, organic matter accumulation, and microbial colonization. With intact soil, plant establishment can begin immediately.",
            "feedback_incorrect": "Soil is a complex biological system containing microbial communities, mycorrhizal networks, organic matter, and nutrient reserves that took centuries to develop. Plants cannot establish on bare rock without these services. This is why primary succession from bare rock takes 100-1000 years while secondary succession on intact soil takes 20-50 years."
        },
        {
            "question": "The 'Climate-Shifted Recovery' scenario shows the Recovery Completeness Index stabilizing at approximately 40% relative to the original ecosystem. The model indicates this is not a failure of recovery but rather a successful recovery to a different stable state. What concept does this illustrate?",
            "choices": {
                "A": "Ecosystems always return to their original state given enough time",
                "B": "When climate conditions have shifted beyond the tolerance of the original species, the ecosystem recovers to an alternative stable state that matches the new climate rather than the historical ecosystem, representing a climate-driven regime shift",
                "C": "A 40% recovery score means 60% of species have gone extinct globally",
                "D": "The model is broken because recovery should always reach 100%"
            },
            "correct": "B",
            "feedback_correct": "Correct. The 40% Recovery Completeness Index (measured against the original ecosystem) reflects a climate-driven regime shift. The ecosystem IS recovering successfully, but to a state suited to the new climate conditions. If the original conifers require cooler, wetter conditions than now exist, the recovering ecosystem will be composed of species adapted to the warmer, drier climate. This is a functioning ecosystem, just not the original one.",
            "feedback_incorrect": "The model measures recovery against the pre-disturbance reference ecosystem. A 40% score does not mean 60% failure. It means the ecosystem has recovered to a stable, functional state that differs from the original because climate conditions have changed. This is a regime shift driven by altered environmental conditions."
        },
        {
            "question": "The model reveals that Invasive Species Pressure has its greatest impact during early succession when the disturbed ecosystem has open space, available nutrients, and reduced competition. Which management implication follows directly from this finding?",
            "choices": {
                "A": "Invasive species management is unnecessary because native species always outcompete invasives eventually",
                "B": "Early aggressive invasive species control during the first 1-5 years post-disturbance is critical because once invasives establish and modify the successional trajectory, their effects become self-reinforcing and increasingly difficult to reverse",
                "C": "Invasive species should be encouraged because they speed up recovery",
                "D": "Invasive species management is only effective after the ecosystem has fully recovered"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows a vulnerability window during early succession. Invasive species that establish during this window can modify soil chemistry, outcompete native seedlings, and alter the successional trajectory permanently. Early intervention (within the first few years) prevents establishment before self-reinforcing feedbacks lock in the invasive-dominated state. Waiting until invasives are established makes management orders of magnitude more difficult.",
            "feedback_incorrect": "The model identifies early succession as a critical vulnerability window. Invasive species that establish during this period alter soil, outcompete natives, and create self-reinforcing feedbacks that lock in their dominance. Early management prevents establishment; late management must fight an already-established alternative state."
        },
        {
            "question": "Adding 'Mycorrhizal Network Recovery' to the model reveals that tree seedlings in areas with surviving mycorrhizal fungi grow 50-80% faster than seedlings in areas without. What does this reveal about the role of belowground networks in ecosystem recovery?",
            "choices": {
                "A": "Mycorrhizal fungi are parasites that steal nutrients from tree seedlings",
                "B": "Belowground fungal networks are critical infrastructure for ecosystem recovery because they extend root absorption area, facilitate nutrient and water transfer between plants, and provide chemical communication pathways that established trees use to support seedlings",
                "C": "Mycorrhizal networks only exist in tropical forests and are irrelevant in temperate ecosystems",
                "D": "Tree growth rate has no relationship to mycorrhizal presence"
            },
            "correct": "B",
            "feedback_correct": "Correct. Mycorrhizal networks are belowground infrastructure that takes decades to fully develop. They extend root absorption area by orders of magnitude, transfer nutrients and water between connected plants (including from established trees to seedlings), and transmit chemical signals about pests and drought. Areas where these networks survive disturbance recover dramatically faster because seedlings immediately connect to existing infrastructure.",
            "feedback_incorrect": "Mycorrhizal fungi are mutualistic partners, not parasites. They form underground networks that extend root systems, transfer nutrients between plants, and facilitate communication. Their survival after disturbance dramatically accelerates recovery because new seedlings can immediately connect to existing fungal infrastructure."
        },
        {
            "question": "A restoration ecology team uses the model to design a restoration plan for a severely burned Sierra Nevada forest where climate projections indicate 1.5 degrees C warming and 15% less precipitation by 2050. The model suggests planting species adapted to future conditions rather than the original conifer species. This 'assisted migration' strategy is controversial. Which model evidence most strongly supports this approach?",
            "choices": {
                "A": "The model shows that any tree species will grow on any site regardless of climate",
                "B": "The model predicts that planting original species in a climate they can no longer tolerate will result in establishment failure and wasted resources, while species adapted to the projected climate will establish successfully and provide ecosystem services decades sooner than waiting for natural migration",
                "C": "Assisted migration is supported because moving species is always harmless to receiving ecosystems",
                "D": "The model shows that climate change will reverse itself within 20 years, making the original species viable again"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that planting species mismatched to future climate conditions results in high mortality and failed restoration. Species adapted to the projected warmer, drier conditions establish successfully and provide ecosystem services (carbon sequestration, habitat, erosion control) decades sooner than waiting for natural range shifts. The trade-off is not recreating the past versus accepting change; it is functional recovery versus failed restoration.",
            "feedback_incorrect": "The model shows a practical choice: plant species that match the projected climate and get functional ecosystem recovery within decades, or plant original species that cannot survive new conditions and get restoration failure. Assisted migration trades historical fidelity for functional success."
        }
    ]
}

# =============================================================================
# L09: Can Nuclear Fusion Power the World? (HS-PS1-8)
# =============================================================================
L09_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Nuclear fusion and nuclear fission both release energy from atomic nuclei, but through opposite processes. Which statement most accurately distinguishes them?",
            "choices": {
                "A": "Fusion combines light nuclei (hydrogen isotopes) into heavier ones (helium), while fission splits heavy nuclei (uranium) into lighter ones. Both release energy because the products have less mass than the reactants",
                "B": "Fusion splits atoms while fission combines them",
                "C": "Fusion produces nuclear waste while fission does not",
                "D": "Fusion and fission are identical processes that differ only in scale"
            },
            "correct": "A",
            "feedback_correct": "Correct. Fusion combines deuterium and tritium nuclei into helium, while fission splits uranium or plutonium into lighter elements. In both cases, the products have slightly less mass than the reactants, and this mass difference is converted to energy via E=mc2. Fusion releases roughly 4x more energy per unit mass than fission.",
            "feedback_incorrect": "Fusion (combining) and fission (splitting) are opposite processes. Fusion joins light nuclei (deuterium + tritium to helium), fission splits heavy nuclei (uranium into lighter elements). Both release energy because the products have slightly less mass than the reactants, converted to energy via E=mc2."
        },
        {
            "question": "The Lawson criterion specifies the minimum product of temperature, density, and confinement time for fusion to produce net energy. Why is achieving all three simultaneously so difficult?",
            "choices": {
                "A": "Current technology can easily achieve all three; the delay is due to lack of funding",
                "B": "The three requirements work against each other: higher temperature makes plasma harder to confine, higher density creates instabilities that shorten confinement time, and longer confinement requires extraordinary magnetic field precision against instabilities that develop within milliseconds",
                "C": "The Lawson criterion was disproven in the 1990s and is no longer relevant",
                "D": "Only temperature matters; density and confinement time are irrelevant to fusion"
            },
            "correct": "B",
            "feedback_correct": "Correct. The three parameters of the Lawson criterion are interconnected and often adversarial. A 150-million-degree plasma exerts enormous pressure that fights confinement. Increasing density makes the plasma more prone to instabilities (kink modes, ballooning modes) that can destroy confinement in milliseconds. Maintaining confinement for hundreds of seconds requires real-time feedback control of magnetic fields with extraordinary precision.",
            "feedback_incorrect": "The fundamental challenge is that the three requirements compete with each other. Hotter plasma is harder to confine. Denser plasma develops instabilities faster. Longer confinement requires suppressing instabilities that evolve on millisecond timescales. Achieving all three simultaneously is the engineering challenge that has made fusion so difficult."
        },
        {
            "question": "A tokamak confines fusion plasma using magnetic fields rather than physical walls. Why can't the 150-million-degree plasma simply be contained in a physical container?",
            "choices": {
                "A": "Physical containers could contain the plasma, but magnetic confinement is cheaper",
                "B": "No known material can withstand 150 million degrees Celsius. The plasma would instantly vaporize any physical wall it contacts, so it must be suspended by magnetic fields that keep it away from all surfaces",
                "C": "Physical containers work fine for fusion; tokamaks use magnets for aesthetic reasons",
                "D": "The plasma is too cold to damage physical walls but too light to be held by gravity"
            },
            "correct": "B",
            "feedback_correct": "Correct. At 150 million degrees C (ten times hotter than the Sun's core), every known material would instantly vaporize on contact with the plasma. Magnetic confinement uses the fact that plasma is ionized (charged particles) and responds to magnetic fields, allowing the plasma to be suspended in a magnetic bottle that prevents it from touching any physical surface.",
            "feedback_incorrect": "150 million degrees is approximately ten times hotter than the core of the Sun. No material exists that could survive contact with plasma at this temperature. Magnetic confinement works because plasma consists of charged particles that are deflected by magnetic fields, allowing the plasma to float without touching any surface."
        },
        {
            "question": "E = mc2 explains why nuclear fusion releases enormous energy from tiny amounts of fuel. What does this equation tell us about fusion specifically?",
            "choices": {
                "A": "Energy equals mass times the speed of light squared, meaning the small mass difference between fusion reactants and products is multiplied by c2 (a huge number), converting minuscule mass into enormous energy",
                "B": "The equation shows that fusion creates mass from energy",
                "C": "E = mc2 only applies to fission reactions, not fusion",
                "D": "The equation means that faster-moving atoms produce more fusion reactions"
            },
            "correct": "A",
            "feedback_correct": "Correct. When deuterium and tritium fuse into helium, the helium nucleus has slightly less mass than the combined mass of the reactants. This 'missing' mass (about 0.4% of the input mass) is converted to energy via E = mc2. Because c2 is approximately 9 x 10^16 m2/s2, even a tiny mass difference produces enormous energy: 17.6 MeV per fusion reaction.",
            "feedback_incorrect": "E = mc2 applies to all nuclear reactions. In fusion, the products (helium) have slightly less mass than the reactants (deuterium + tritium). This mass difference, multiplied by the speed of light squared (a very large number), yields the enormous energy released per reaction."
        },
        {
            "question": "Fusion fuel consists of deuterium and tritium. Which statement accurately describes the availability of these fuels?",
            "choices": {
                "A": "Both deuterium and tritium are abundant and easily obtained from seawater",
                "B": "Deuterium is abundant in seawater (1 in 6,500 water molecules), but tritium is radioactive, rare (global supply approximately 25 kg), and must be bred from lithium inside the fusion reactor itself",
                "C": "Both fuels must be mined from the Moon's surface",
                "D": "Deuterium and tritium are the same isotope of hydrogen"
            },
            "correct": "B",
            "feedback_correct": "Correct. Deuterium is naturally abundant (approximately 0.015% of all hydrogen). Tritium, however, is radioactive with a 12.3-year half-life and exists only in trace amounts naturally. The world's total tritium supply is about 25 kg, far less than a single power plant would consume annually. Commercial fusion reactors must breed their own tritium from lithium blankets surrounding the reactor.",
            "feedback_incorrect": "Deuterium is abundant in seawater, but tritium is a critical constraint. Tritium is radioactive, has a short half-life (12.3 years), and exists in only trace amounts on Earth (about 25 kg worldwide). A commercial fusion plant would consume about 56 kg per year, so it must breed its own tritium from lithium inside the reactor."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that current best fusion performance (JET tokamak, Q = 0.33 for 5 seconds) achieves the required temperature and density but fails on confinement time. What does this reveal about the primary engineering bottleneck for fusion?",
            "choices": {
                "A": "We cannot heat plasma to fusion temperatures with current technology",
                "B": "The physics of fusion is wrong and the reaction cannot actually produce net energy",
                "C": "Plasma instabilities that develop on millisecond timescales disrupt confinement, making it the hardest of the three Lawson criterion parameters to achieve and sustain. Maintaining confinement for hundreds of seconds requires real-time suppression of multiple instability modes simultaneously",
                "D": "Confinement is the easiest parameter to achieve and temperature is the real bottleneck"
            },
            "correct": "C",
            "feedback_correct": "Correct. The model reveals that temperature and density are achievable with current technology, but maintaining stable confinement against multiple plasma instability modes (kink, ballooning, edge-localized modes) for hundreds of seconds remains the primary bottleneck. This requires real-time magnetic field control with millisecond response times and extraordinary precision.",
            "feedback_incorrect": "The model shows that temperature and density targets are within reach. The bottleneck is confinement time: plasma instabilities develop on millisecond timescales and must be continuously suppressed through real-time magnetic field adjustments to maintain confinement for the hundreds of seconds needed for net energy production."
        },
        {
            "question": "ITER is designed to achieve Q = 10 (500 MW fusion from 50 MW heating). The model reveals that achieving Q = 10 is necessary but insufficient for commercial fusion. What additional challenges must be solved between ITER and a power plant on the electrical grid?",
            "choices": {
                "A": "ITER solves all remaining challenges and commercial fusion is ready for deployment",
                "B": "Commercial fusion requires sustained operation for months (not seconds), tritium self-sufficiency (breeding more tritium than consumed), materials that survive years of neutron bombardment, and electricity generation at competitive cost, none of which ITER is designed to demonstrate",
                "C": "The only remaining challenge is building a larger version of ITER",
                "D": "Commercial fusion requires Q = 10 and nothing more"
            },
            "correct": "B",
            "feedback_correct": "Correct. ITER is a physics experiment, not a power plant. Commercial fusion must solve: continuous operation for 11+ months per year (ITER runs in pulses); tritium breeding ratio > 1.0 (ITER does not breed tritium at scale); wall materials that survive 14.1 MeV neutron bombardment for years (ITER will identify the damage but not solve it); and cost-competitive electricity generation. Each is a major unsolved engineering challenge.",
            "feedback_incorrect": "ITER demonstrates that fusion physics works at scale, but a commercial power plant requires far more: sustained (not pulsed) operation, tritium self-sufficiency, neutron-resistant wall materials that last years, and electricity generation at competitive cost. These are engineering challenges beyond ITER's scope."
        },
        {
            "question": "The model reveals that neutron flux on reactor walls is a 'hidden' challenge because neutrons carry 80% of fusion energy but cannot be confined by magnetic fields. What are the consequences of this for reactor engineering?",
            "choices": {
                "A": "Neutrons are beneficial because they heat the walls and generate electricity directly",
                "B": "14.1 MeV fusion neutrons cause atomic displacements, helium bubble formation, and nuclear transmutation in wall materials, making them brittle and radioactive. This means inner wall components must be replaced every few years, creating ongoing maintenance costs and generating radioactive waste that, while less dangerous than fission waste, still requires management",
                "C": "Magnetic fields can be strengthened to confine neutrons along with the plasma",
                "D": "Neutrons from fusion are low-energy and cause negligible damage to materials"
            },
            "correct": "B",
            "feedback_correct": "Correct. Unlike charged plasma particles, neutrons have no charge and pass through magnetic fields unimpeded. At 14.1 MeV, they are highly energetic and cause severe material damage: displacing atoms from crystal lattices, creating helium bubbles that weaken metal, and transmuting elements. This creates a materials science challenge with no current solution. Inner wall components may need replacement every 2-5 years.",
            "feedback_incorrect": "Fusion neutrons at 14.1 MeV are extremely energetic and uncontrollable by magnetic fields (they are electrically neutral). They damage structural materials through atomic displacement, helium bubble formation, and transmutation, requiring periodic wall replacement and creating a materials science challenge that has no existing solution."
        },
        {
            "question": "The model shows that tritium self-sufficiency requires a tritium breeding ratio (TBR) greater than 1.0 from lithium blankets surrounding the plasma. Why must the TBR exceed 1.0 rather than exactly equal 1.0?",
            "choices": {
                "A": "TBR of exactly 1.0 is sufficient because every tritium atom consumed is replaced",
                "B": "Tritium is radioactive with a 12.3-year half-life and some bred tritium is lost during extraction, processing, and storage. These unavoidable losses mean the reactor must breed more tritium than it consumes to maintain a stable fuel supply",
                "C": "TBR > 1.0 is needed because tritium is used for cooling in addition to fuel",
                "D": "The model shows that TBR of 0.5 is sufficient for commercial operation"
            },
            "correct": "B",
            "feedback_correct": "Correct. Even with perfect blanket coverage, some bred tritium decays before use (half-life 12.3 years), some is lost during the extraction and purification process, and some permeates through materials and escapes. These unavoidable losses mean the TBR must exceed 1.0 (typically estimated at 1.05-1.15) to maintain a net positive tritium inventory over the reactor's lifetime.",
            "feedback_incorrect": "A TBR of exactly 1.0 would mean zero margin for losses. Tritium is radioactive (decays at 5.5% per year), and some is inevitably lost during extraction, processing, and storage. The reactor must breed more than it consumes to compensate for these losses, requiring TBR > 1.0."
        },
        {
            "question": "The model predicts that high-temperature superconducting (HTS) magnets generating 20+ Tesla could significantly improve fusion feasibility compared to ITER's low-temperature superconducting magnets at 11.8 Tesla. What is the primary advantage of stronger magnetic fields for fusion?",
            "choices": {
                "A": "Stronger magnets heat the plasma to higher temperatures automatically",
                "B": "Stronger magnetic fields confine plasma more tightly, enabling higher density and better stability in a physically smaller device. This means fusion-relevant conditions can be achieved in a reactor a fraction of ITER's size, dramatically reducing construction cost and accelerating the path to commercial viability",
                "C": "Stronger magnets eliminate the need for tritium fuel",
                "D": "HTS magnets operate at room temperature and require no cooling"
            },
            "correct": "B",
            "feedback_correct": "Correct. Magnetic confinement performance scales with the fourth power of magnetic field strength. Doubling the field from 11.8 to 20+ Tesla enables roughly 16x better confinement performance, meaning the same fusion conditions can be achieved in a much smaller, cheaper device. This is why private fusion companies like Commonwealth Fusion Systems are pursuing HTS magnets as a potential shortcut past ITER-scale facilities.",
            "feedback_incorrect": "Stronger magnetic fields improve plasma confinement, allowing higher density and stability in a smaller device. Since confinement scales roughly with the fourth power of field strength, HTS magnets at 20+ Tesla could achieve ITER-level performance in a reactor a fraction of ITER's size, dramatically cutting cost and accelerating timelines."
        }
    ]
}

# =============================================================================
# L10: What Defines the Ethics of Science? (HS-ETS1-3)
# =============================================================================
L10_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Dual-use research of concern (DURC) produces knowledge with both beneficial applications and potential for misuse. Which of the following is the most accurate example of a dual-use dilemma?",
            "choices": {
                "A": "Research on improving crop yields, which has no potential for misuse",
                "B": "Gain-of-function virology research that enhances pathogen transmissibility, which can inform pandemic preparedness and vaccine development but also provides a blueprint for creating biological weapons",
                "C": "Teaching basic chemistry in high school, which enables students to make dangerous chemicals",
                "D": "Publishing weather forecasts, which could be used by enemy nations to plan military operations"
            },
            "correct": "B",
            "feedback_correct": "Correct. Gain-of-function research is the paradigmatic dual-use dilemma. Making a pathogen more transmissible reveals how natural variants might evolve (essential for pandemic preparedness), but the same knowledge could be used to engineer a biological weapon. The dual-use potential is not speculative; the knowledge and techniques are directly transferable between beneficial and harmful applications.",
            "feedback_incorrect": "A true dual-use dilemma involves research where the same knowledge is directly applicable to both beneficial and harmful purposes. Gain-of-function virology is the clearest example: understanding enhanced pathogen transmissibility helps prepare for pandemics but also provides the technical knowledge to create biological weapons."
        },
        {
            "question": "An Institutional Review Board (IRB) reviews research proposals involving human subjects. What is the primary purpose of IRB review?",
            "choices": {
                "A": "To ensure the research will produce profitable results for the institution",
                "B": "To verify that the research meets ethical standards for informed consent, risk minimization, equitable participant selection, and privacy protection before experiments begin",
                "C": "To determine whether the research will receive government funding",
                "D": "To evaluate whether the research hypothesis is scientifically correct"
            },
            "correct": "B",
            "feedback_correct": "Correct. IRBs exist to protect human research participants by ensuring that ethical standards are met before research begins. They evaluate whether informed consent is genuine, whether risks are minimized and justified by potential benefits, whether participant selection is equitable (not exploiting vulnerable populations), and whether privacy is protected.",
            "feedback_incorrect": "IRBs are ethics committees, not scientific or financial review boards. Their role is to protect human research participants by verifying informed consent, evaluating risk-benefit ratios, ensuring equitable selection (not exploiting vulnerable populations), and protecting privacy."
        },
        {
            "question": "The precautionary principle states that when a scientific activity raises potential threats, precautionary measures should be taken even before causal relationships are fully established. How does this differ from the standard of 'prove it is harmful before regulating it'?",
            "choices": {
                "A": "There is no difference; both approaches are identical",
                "B": "The precautionary principle shifts the burden of proof: instead of requiring proof of harm before acting, it requires proof of safety before proceeding with potentially dangerous research or technology",
                "C": "The precautionary principle prohibits all scientific research as potentially dangerous",
                "D": "The standard approach is more cautious than the precautionary principle"
            },
            "correct": "B",
            "feedback_correct": "Correct. The precautionary principle reverses the burden of proof. Instead of 'it is allowed unless proven harmful,' it adopts 'it should not proceed until proven safe.' This is particularly relevant for irreversible technologies (gene drives, geoengineering) where waiting for proof of harm may mean the harm is already done and cannot be undone.",
            "feedback_incorrect": "The precautionary principle shifts the burden of proof from 'prove harm before regulating' to 'prove safety before proceeding.' This distinction matters most for irreversible technologies where waiting for evidence of harm may mean the damage is already done."
        },
        {
            "question": "Scientific integrity includes honest data collection, accurate reporting, and willingness to publish negative results. Why is publishing negative results (experiments that did not support the hypothesis) important for scientific integrity?",
            "choices": {
                "A": "Negative results are not important because only successful experiments advance knowledge",
                "B": "Publishing negative results prevents other researchers from wasting resources repeating failed experiments, reduces publication bias that distorts the scientific record, and demonstrates that the researcher is committed to truth rather than personal advancement",
                "C": "Negative results are only published in low-quality journals",
                "D": "Scientists are legally required to publish all results, including negative ones"
            },
            "correct": "B",
            "feedback_correct": "Correct. When only positive results are published, the scientific literature becomes a biased sample that overstates the effectiveness of treatments, the strength of relationships, and the reproducibility of findings. Publishing negative results corrects this bias, saves resources, and maintains the self-correcting nature of science. The replication crisis in psychology and medicine is partly attributable to publication bias against negative results.",
            "feedback_incorrect": "Not publishing negative results creates publication bias: the literature disproportionately represents 'successful' experiments, overstating effect sizes and reliability. This contributed to the replication crisis. Publishing negative results saves resources (others do not repeat failed approaches) and maintains science's self-correcting capacity."
        },
        {
            "question": "Who should decide which scientific research gets funded and which gets restricted? This question is central to science ethics. Which consideration most complicates simple answers?",
            "choices": {
                "A": "Scientists should decide everything because they understand the research best",
                "B": "Politicians should decide everything because they represent the public",
                "C": "The question is complicated because scientists may have conflicts of interest (wanting to pursue their own research), politicians may lack technical understanding, and the public may not have access to sufficient information, suggesting that governance requires balanced input from multiple stakeholders",
                "D": "No one should make these decisions; all research should be unregulated"
            },
            "correct": "C",
            "feedback_correct": "Correct. No single group can optimally govern science alone. Scientists have expertise but may have conflicts of interest. Politicians represent public interests but may lack technical understanding. The public deserves a voice but may not have specialized knowledge. Effective science governance requires balanced input from all stakeholders, with structures that mitigate each group's limitations.",
            "feedback_incorrect": "Each potential decision-maker has both strengths and limitations. Scientists have expertise but conflicts of interest. Politicians have democratic mandate but may lack technical knowledge. The public deserves input but may lack information. Effective governance requires balanced structures drawing on all perspectives."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that maximizing Innovation Rate does not maximize Societal Impact Score. Instead, the highest Societal Impact Score occurs at a moderate Innovation Rate with robust oversight. What does this finding reveal about the relationship between scientific freedom and societal benefit?",
            "choices": {
                "A": "All scientific research should be stopped to maximize societal benefit",
                "B": "Scientific freedom without ethical governance produces innovations that are inequitably distributed, generate dual-use risks, and erode public trust, creating net harm that partially offsets the gains from rapid innovation",
                "C": "Innovation always produces net positive societal impact regardless of governance",
                "D": "Societal Impact Score is a meaningless metric that should be removed from the model"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that unrestricted innovation generates benefits but also produces dual-use risks (technologies that can harm), inequitable distribution (benefits concentrated among the wealthy), and trust erosion (public loses faith in science due to real or perceived irresponsibility). These negative effects partially offset innovation gains, meaning a moderate pace with ethical governance produces greater net societal benefit than unchecked speed.",
            "feedback_incorrect": "The model demonstrates that innovation speed is not the only determinant of societal benefit. Unrestricted innovation generates dual-use risks, inequitable distribution, and trust erosion that reduce net benefit. Moderate innovation with robust ethical governance maximizes the gap between benefits generated and harms produced."
        },
        {
            "question": "The model reveals a positive feedback loop between Publication Transparency, Public Trust in Science, and funding support. When this loop operates in reverse (eroded trust), what cascade does the model predict?",
            "choices": {
                "A": "Eroded trust has no effect on funding or research because they are independent",
                "B": "Reduced trust leads to reduced public support for research funding, which leads to less research, which leads to fewer scientific solutions to public problems, which further erodes trust in science's value, creating a self-reinforcing downward spiral",
                "C": "Eroded trust increases funding because politicians want to prove science is still valuable",
                "D": "Trust can never be eroded because science is inherently trustworthy"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals a self-reinforcing trust spiral. When transparency decreases or misconduct occurs, public trust drops. Lower trust reduces political support for research funding. Less funding means fewer scientific breakthroughs and solutions. Fewer solutions mean the public perceives less value from science. This further erodes trust, continuing the cycle. Rebuilding trust once lost requires sustained transparency far beyond what was needed to maintain it.",
            "feedback_incorrect": "The model shows a reinforcing feedback loop: trust loss reduces funding, which reduces scientific output, which reduces public perception of science's value, which further erodes trust. This downward spiral is much easier to trigger than to reverse, which is why maintaining transparency is critical."
        },
        {
            "question": "The model shows that Benefit Distribution Equity and Risk Distribution Equity are independent variables. A student discovers that a scenario with high total benefit but low equity scores produces a lower Societal Impact Score than a scenario with moderate total benefit but high equity. What does this reveal?",
            "choices": {
                "A": "Total benefit does not matter; only equity matters",
                "B": "The distribution of benefits and risks matters as much as their total magnitude, because scientific advances that benefit only wealthy communities while imposing risks on marginalized communities create social harm that reduces net societal value even when total benefit is high",
                "C": "Equity should not be measured because it is subjective",
                "D": "The model incorrectly penalizes high-benefit research"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model captures the insight that a scientific advance is not socially optimal just because total benefit is high. If benefits flow to those who need them least while risks burden those who are already disadvantaged, the advance perpetuates and amplifies inequity. Historical examples (Tuskegee experiments, environmental pollution in minority communities) demonstrate that inequitable research creates lasting social harm that reduces net societal value.",
            "feedback_incorrect": "Both total benefit and equity distribution matter. High total benefit with low equity means benefits concentrate among the privileged while risks burden the disadvantaged. History shows this pattern (Tuskegee, environmental racism) creates lasting social harm that reduces net societal value even when total scientific output is impressive."
        },
        {
            "question": "In the 'Dual-Use Crisis' scenario, the model shows that restricting publication of extreme dual-use research reduces Innovation Rate by 15% but improves Societal Impact Score by 25% due to reduced misuse risk. A student argues this proves all research should be restricted. Why is this generalization incorrect?",
            "choices": {
                "A": "The student is correct; all research should be restricted",
                "B": "The model shows that the optimal balance between restriction and openness depends on the specific dual-use potential of each research area. Low dual-use research benefits greatly from open publication, while extreme dual-use research warrants careful restriction. A blanket policy in either direction is suboptimal",
                "C": "Restricting any research always reduces Societal Impact Score",
                "D": "Dual-use potential does not vary between research areas"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that the restriction-openness balance is case-dependent. For low dual-use research (most basic science), open publication maximizes societal benefit through knowledge sharing and reproducibility. For extreme dual-use research (gain-of-function pathogens, autonomous weapons AI), measured restriction protects against catastrophic misuse. Blanket restriction would stifle beneficial research, while blanket openness would enable dangerous misuse.",
            "feedback_incorrect": "The model shows that the optimal governance approach depends on the specific dual-use potential. Most research benefits from open publication (transparency, reproducibility, collaboration). Only research with extreme misuse potential warrants restriction. Case-by-case ethical evaluation produces better outcomes than blanket policies in either direction."
        },
        {
            "question": "Adding 'International Governance Coordination' to the model reveals that unilateral research restrictions by one country are largely ineffective. What mechanism does the model identify as the cause of this ineffectiveness?",
            "choices": {
                "A": "International laws automatically prevent any country from conducting dangerous research",
                "B": "When one country restricts research, scientists and research programs migrate to countries with fewer restrictions, meaning the dangerous research still occurs but without the oversight and transparency that governance was designed to provide, producing worse outcomes than coordinated international regulation",
                "C": "Unilateral restrictions are effective because each country can control its own researchers completely",
                "D": "International coordination is unnecessary because all countries have identical ethical standards"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates regulatory arbitrage: when restrictions are unilateral, research moves to less-regulated jurisdictions. The dangerous research still occurs, but now without the oversight, safety protocols, and transparency that the restricting country would have provided. This produces worse outcomes than either universal regulation or universal openness, because it combines the innovation cost of restriction (in the restricting country) with the safety cost of unrestricted research (in the receiving country).",
            "feedback_incorrect": "Unilateral restrictions drive research to less-regulated jurisdictions rather than preventing it. The model shows this regulatory arbitrage produces the worst of both worlds: the restricting country loses innovation while the receiving country gains dangerous research without adequate oversight. Only coordinated international regulation can effectively govern dual-use research."
        }
    ]
}

# =============================================================================
# ALL_QUESTIONS dictionary mapping lesson IDs to their question sets
# =============================================================================
ALL_QUESTIONS = {
    "G12L3-L01": L01_QUESTIONS,
    "G12L3-L02": L02_QUESTIONS,
    "G12L3-L03": L03_QUESTIONS,
    "G12L3-L04": L04_QUESTIONS,
    "G12L3-L05": L05_QUESTIONS,
    "G12L3-L06": L06_QUESTIONS,
    "G12L3-L07": L07_QUESTIONS,
    "G12L3-L08": L08_QUESTIONS,
    "G12L3-L09": L09_QUESTIONS,
    "G12L3-L10": L10_QUESTIONS,
}
