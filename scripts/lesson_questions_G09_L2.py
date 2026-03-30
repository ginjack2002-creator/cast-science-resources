#!/usr/bin/env python3
"""Multiple choice pre/post assessment questions for Grade 9 Level 2 ModelIt! Lessons"""

L01_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is the primary mechanism by which bacteria develop resistance to antibiotics?",
            "choices": {
                "A": "Bacteria intentionally mutate their DNA in response to antibiotic exposure",
                "B": "Random genetic mutations occur naturally, and antibiotics select for individuals carrying resistance traits",
                "C": "Antibiotics chemically alter bacterial DNA to create resistant strains",
                "D": "Bacteria learn to recognize and avoid antibiotics through repeated exposure"
            },
            "correct": "B",
            "feedback_correct": "Correct. Antibiotic resistance arises from random mutations that exist before antibiotic exposure. Antibiotics create selective pressure that favors already-resistant individuals, allowing them to survive and reproduce.",
            "feedback_incorrect": "Bacteria do not intentionally mutate or learn. Resistance genes arise from random mutations that happen naturally. Antibiotics then act as a selective pressure, killing susceptible bacteria while resistant ones survive and multiply."
        },
        {
            "question": "A patient feels better after 4 days of a 10-day antibiotic prescription and stops taking the medication. What is the most likely outcome?",
            "choices": {
                "A": "The infection is cured because the patient's symptoms have resolved",
                "B": "The remaining bacteria are too weak to cause further illness",
                "C": "The surviving bacteria are disproportionately resistant, increasing the chance of a harder-to-treat reinfection",
                "D": "The patient's immune system will easily handle any remaining bacteria without further treatment"
            },
            "correct": "C",
            "feedback_correct": "Correct. Incomplete treatment kills susceptible bacteria first, leaving behind a population enriched with resistant strains. These resistant survivors can multiply and cause reinfection that is more difficult to treat.",
            "feedback_incorrect": "Feeling better does not mean the infection is eliminated. The first bacteria killed are the susceptible ones. Stopping early leaves resistant bacteria alive, free from competition, and able to multiply into a resistant population."
        },
        {
            "question": "Which term best describes a cycle in which more resistant bacteria lead to less effective antibiotics, which in turn allows even more resistant bacteria to survive?",
            "choices": {
                "A": "Balancing feedback loop",
                "B": "Reinforcing feedback loop",
                "C": "Negative feedback loop",
                "D": "Stabilizing feedback loop"
            },
            "correct": "B",
            "feedback_correct": "Correct. A reinforcing (positive) feedback loop amplifies change in the same direction. More resistance reduces antibiotic effectiveness, which allows more resistant bacteria to thrive, further reducing effectiveness.",
            "feedback_incorrect": "Balancing, negative, and stabilizing feedback loops all describe self-correcting systems that return to equilibrium. The resistance cycle amplifies itself, which is the defining characteristic of a reinforcing feedback loop."
        },
        {
            "question": "What role does natural selection play in the development of antibiotic-resistant bacterial populations?",
            "choices": {
                "A": "Natural selection creates new resistance genes in response to environmental stress",
                "B": "Natural selection has no role because resistance is entirely caused by human overuse of antibiotics",
                "C": "Natural selection favors bacteria with pre-existing resistance traits when antibiotics create selective pressure",
                "D": "Natural selection eliminates resistant bacteria because they require more energy to maintain resistance genes"
            },
            "correct": "C",
            "feedback_correct": "Correct. Natural selection acts on existing variation. When antibiotics are present, bacteria that already carry resistance genes have a survival advantage and reproduce at higher rates than susceptible individuals.",
            "feedback_incorrect": "Natural selection does not create new traits; it acts on variation that already exists. In the presence of antibiotics, pre-existing resistance mutations become advantageous, and individuals carrying them survive and reproduce preferentially."
        },
        {
            "question": "Horizontal gene transfer allows bacteria to share resistance genes across species. Why does this make the antibiotic resistance problem more severe?",
            "choices": {
                "A": "It means resistance can only spread through reproduction within a single species",
                "B": "It allows resistance to spread much faster than mutation alone, even to unrelated bacterial species",
                "C": "It reduces the overall mutation rate in bacterial populations",
                "D": "It ensures that only harmful bacteria receive resistance genes"
            },
            "correct": "B",
            "feedback_correct": "Correct. Horizontal gene transfer allows resistance genes to jump between species via plasmids, dramatically accelerating the spread of resistance beyond what mutation and vertical inheritance alone could achieve.",
            "feedback_incorrect": "Horizontal gene transfer is significant precisely because it is NOT limited to a single species. Bacteria can share resistance genes across species boundaries, meaning one resistant strain can arm entirely different bacterial populations."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the antibiotic resistance model, which scenario produces the most dangerous long-term outcome for public health?",
            "choices": {
                "A": "No antibiotic treatment at all",
                "B": "Full-course treatment at the prescribed dosage",
                "C": "Sub-therapeutic dosage maintained for the full course duration",
                "D": "A single high dose followed by immediate discontinuation"
            },
            "correct": "C",
            "feedback_correct": "Correct. Sub-therapeutic dosage is the most dangerous because it creates enough selective pressure to favor resistant bacteria but is too weak to eliminate them. This provides the ideal environment for evolving resistance over an extended period.",
            "feedback_incorrect": "Sub-therapeutic dosage creates the worst outcome because the antibiotic is strong enough to kill susceptible bacteria (selecting for resistance) but too weak to kill resistant ones. This sustained selective pressure breeds resistance more effectively than no treatment or brief treatment."
        },
        {
            "question": "A computational model shows that Resistant Bacteria Percentage increases exponentially after Treatment Duration is reduced to 50%. Which systems thinking concept best explains this behavior?",
            "choices": {
                "A": "A balancing feedback loop restoring equilibrium",
                "B": "A reinforcing feedback loop where resistance amplifies itself",
                "C": "A linear cause-and-effect relationship between dosage and resistance",
                "D": "Random variation in bacterial population dynamics"
            },
            "correct": "B",
            "feedback_correct": "Correct. The exponential increase is driven by a reinforcing feedback loop: as resistant bacteria increase, antibiotic effectiveness decreases, allowing even more resistant bacteria to survive and reproduce, further reducing effectiveness.",
            "feedback_incorrect": "Exponential growth in resistance is the signature of a reinforcing feedback loop, not random variation or a linear relationship. Each cycle through the loop amplifies the previous change, creating accelerating resistance."
        },
        {
            "question": "A student's model predicts that reducing the Immune Response component to low while maintaining full antibiotic treatment results in treatment failure. What does this reveal about the system?",
            "choices": {
                "A": "Antibiotics are unnecessary if the immune system is functioning",
                "B": "The immune system and antibiotics are redundant systems that perform the same function",
                "C": "Antibiotics alone cannot reliably eliminate infections; the immune system is a critical partner in clearing bacteria",
                "D": "Immune response has no measurable effect on bacterial population dynamics"
            },
            "correct": "C",
            "feedback_correct": "Correct. The model reveals that antibiotics reduce bacterial populations but rely on the immune system to clear remaining bacteria. Without adequate immune support, even full antibiotic courses may fail to eliminate the infection.",
            "feedback_incorrect": "The model demonstrates that antibiotics and the immune system work as partners. Antibiotics reduce the bacterial load to a level the immune system can handle, but neither system alone is sufficient in many cases."
        },
        {
            "question": "Using evidence from the simulation, a student argues that 'antibiotics create resistant bacteria.' Which response most accurately corrects this misconception?",
            "choices": {
                "A": "The student is correct; antibiotics directly cause mutations that confer resistance",
                "B": "Antibiotics do not create resistance; they create the selective conditions under which pre-existing resistant bacteria have a survival advantage",
                "C": "Resistance is entirely genetic and has nothing to do with antibiotic use",
                "D": "Only overuse of antibiotics creates resistance; proper use never contributes to resistance"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is a critical distinction. Resistance mutations arise randomly regardless of antibiotic presence. Antibiotics create the environmental conditions where those mutations become advantageous, selecting for resistant individuals.",
            "feedback_incorrect": "The key insight is that antibiotics do not cause mutations. Resistance genes exist before antibiotic exposure. Antibiotics act as a selective filter, killing susceptible bacteria and allowing resistant ones to dominate the population."
        },
        {
            "question": "Based on the model, which public health intervention would be most effective at slowing the reinforcing feedback loop driving antibiotic resistance?",
            "choices": {
                "A": "Developing stronger antibiotics that kill bacteria faster",
                "B": "Ensuring patients complete full prescribed courses and eliminating unnecessary prescriptions",
                "C": "Restricting antibiotics to hospital use only",
                "D": "Increasing the mutation rate in bacterial populations to introduce harmful mutations"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that incomplete courses and unnecessary prescriptions are the primary drivers of the reinforcing loop. Completing full courses interrupts the loop by eliminating partially resistant bacteria, and reducing unnecessary prescriptions limits selective pressure.",
            "feedback_incorrect": "The model identifies incomplete treatment and unnecessary prescriptions as the key drivers activating the reinforcing loop. Stronger antibiotics face the same resistance dynamics, and restricting access alone does not address misuse patterns."
        }
    ]
}

L02_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is a 'tipping point' in the context of Earth's climate system?",
            "choices": {
                "A": "The point at which global temperatures begin to rise above pre-industrial levels",
                "B": "A critical threshold where a small additional change triggers a dramatic, often irreversible shift in system behavior",
                "C": "The moment when CO2 emissions reach their peak before declining",
                "D": "A natural cycle of warming and cooling that repeats every few thousand years"
            },
            "correct": "B",
            "feedback_correct": "Correct. A tipping point is a threshold beyond which the system undergoes rapid, nonlinear change that may be irreversible on human timescales, fundamentally altering system behavior.",
            "feedback_incorrect": "A tipping point is not simply a gradual temperature increase or emissions peak. It is a critical threshold where the system shifts from one state to another, often abruptly and irreversibly."
        },
        {
            "question": "When Arctic ice melts, it exposes darker ocean water that absorbs more solar radiation, causing further warming and more ice melt. What type of feedback is this?",
            "choices": {
                "A": "Negative feedback that stabilizes the climate",
                "B": "A reinforcing feedback loop that amplifies the original change",
                "C": "A balancing feedback loop that returns the system to equilibrium",
                "D": "A linear response where change is proportional to input"
            },
            "correct": "B",
            "feedback_correct": "Correct. The ice-albedo feedback is a reinforcing loop: warming melts ice, reducing reflectivity (albedo), which absorbs more heat, causing more warming and more melting.",
            "feedback_incorrect": "This is a reinforcing (positive) feedback loop because the output amplifies the input. More warming causes more melting, which causes more absorption of solar energy, leading to even more warming."
        },
        {
            "question": "Permafrost in Arctic regions contains approximately how much carbon relative to the current atmosphere?",
            "choices": {
                "A": "About 10% of current atmospheric carbon",
                "B": "Roughly equal to current atmospheric carbon",
                "C": "About twice the carbon currently in the atmosphere",
                "D": "A negligible amount that has little impact on climate"
            },
            "correct": "C",
            "feedback_correct": "Correct. Arctic permafrost contains an estimated 1.5 trillion tons of carbon, roughly twice the amount currently in the atmosphere, making permafrost thaw a potentially massive additional source of greenhouse gases.",
            "feedback_incorrect": "Arctic permafrost contains approximately 1.5 trillion tons of carbon, about twice what is currently in the atmosphere. If released through thawing, this represents a massive greenhouse gas source independent of human emissions."
        },
        {
            "question": "Why do scientists describe some climate tipping points as 'irreversible on human timescales'?",
            "choices": {
                "A": "Because humans lack the technology to reverse climate change",
                "B": "Because once certain feedback loops are activated, the system continues changing even if the original cause is removed",
                "C": "Because governments are unwilling to take action on climate policy",
                "D": "Because Earth has never experienced rapid climate shifts before"
            },
            "correct": "B",
            "feedback_correct": "Correct. Once reinforcing feedback loops are fully activated, they become self-sustaining. For example, once permafrost begins releasing methane, the warming this causes triggers more permafrost thaw, regardless of human emissions reductions.",
            "feedback_incorrect": "Irreversibility refers to the self-sustaining nature of activated feedback loops. Once crossed, the system's own internal dynamics drive continued change even if the original trigger is removed."
        },
        {
            "question": "Which concept explains why the full effects of today's greenhouse gas emissions will not be felt for decades?",
            "choices": {
                "A": "The greenhouse effect",
                "B": "Thermal inertia of the oceans",
                "C": "Photosynthetic carbon absorption",
                "D": "Atmospheric dilution of CO2"
            },
            "correct": "B",
            "feedback_correct": "Correct. Oceans have enormous thermal inertia, meaning they absorb and slowly distribute heat over time. This creates a dangerous delay between emissions and their full warming impact.",
            "feedback_incorrect": "Thermal inertia describes the tendency of large systems like oceans to resist rapid temperature change. Oceans absorb excess heat slowly, creating a time lag that masks the true warming trajectory."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's climate model shows that reducing CO2 emissions to zero after crossing the ice-albedo tipping point does not restore ice cover within 200 years. What does this demonstrate?",
            "choices": {
                "A": "The model contains an error because reducing emissions should reverse warming",
                "B": "The reinforcing feedback loop has become self-sustaining, driving continued warming independent of emissions",
                "C": "CO2 emissions have no effect on ice cover",
                "D": "The ice-albedo effect is a balancing feedback loop that requires time to respond"
            },
            "correct": "B",
            "feedback_correct": "Correct. Once the tipping point is crossed, the ice-albedo reinforcing loop sustains itself: less ice means more absorption, more warming, and still less ice. Eliminating the original trigger (emissions) does not break the loop.",
            "feedback_incorrect": "This is the defining characteristic of a tipping point. Once crossed, the system's internal reinforcing feedback loops drive continued change. Removing the original cause is insufficient to reverse the process."
        },
        {
            "question": "The simulation reveals that the climate system has multiple reinforcing feedback loops (ice-albedo, permafrost methane, ocean heat absorption). How do these coupled loops affect system behavior compared to a system with only one feedback loop?",
            "choices": {
                "A": "Multiple loops cancel each other out, creating stability",
                "B": "Multiple loops create cascading tipping points where crossing one threshold triggers others",
                "C": "Each loop operates independently with no interaction",
                "D": "Multiple loops slow the overall rate of change by distributing energy"
            },
            "correct": "B",
            "feedback_correct": "Correct. Coupled reinforcing loops create cascading tipping points. Crossing the ice-albedo threshold can trigger permafrost thaw, which releases methane, causing more warming that accelerates ice loss further.",
            "feedback_incorrect": "Multiple reinforcing loops do not cancel out or operate independently. They cascade, meaning crossing one tipping point can trigger additional tipping points, creating a domino effect of accelerating change."
        },
        {
            "question": "A model comparison shows that the same CO2 emission level produces stable conditions in one scenario but runaway warming in another. What variable most likely differs between the two scenarios?",
            "choices": {
                "A": "The color of the sky in the simulation",
                "B": "Whether the system's initial temperature is above or below the tipping point threshold",
                "C": "The number of components in the model",
                "D": "The speed at which the simulation runs"
            },
            "correct": "B",
            "feedback_correct": "Correct. Threshold dynamics mean that the same input can produce dramatically different outcomes depending on the system's starting state. Below the threshold, the system absorbs the change; above it, reinforcing feedback loops activate.",
            "feedback_incorrect": "This is an example of threshold dynamics. The system's behavior depends critically on whether it is above or below the tipping point. The same emission level can be manageable in one state and catastrophic in another."
        },
        {
            "question": "Ocean heat absorption has been described as 'masking' the true rate of global warming. Based on the model, why is this masking effect dangerous rather than protective?",
            "choices": {
                "A": "Oceans are cooling the planet permanently, so there is no danger",
                "B": "The absorbed heat will eventually be released, and the delay creates a false sense of security while committed warming accumulates",
                "C": "Ocean absorption reduces CO2 levels in the atmosphere directly",
                "D": "Ocean heat absorption has no significant effect on climate modeling"
            },
            "correct": "B",
            "feedback_correct": "Correct. Ocean heat absorption creates a dangerous time delay. The warming is committed but not yet felt. When oceans reach absorption capacity, surface temperatures will rise to reflect all accumulated excess heat, revealing the true extent of warming.",
            "feedback_incorrect": "Ocean heat absorption is temporary storage, not permanent removal. The delay means we experience less warming than we have committed to, creating a false sense that the problem is manageable when the full impact has simply been deferred."
        },
        {
            "question": "Based on simulation evidence, which statement best describes the relationship between CO2 emissions and climate tipping points?",
            "choices": {
                "A": "Reducing emissions always prevents tipping points from being crossed",
                "B": "Tipping points exist at specific temperature thresholds, and the current trajectory may cross multiple thresholds even with moderate emission reductions",
                "C": "Tipping points are theoretical constructs with no basis in climate data",
                "D": "Only complete elimination of all emissions can prevent any climate change"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that tipping points occur at specific thresholds (estimated at 1.5-2.0 degrees C above pre-industrial). Moderate reductions may slow the approach but not prevent crossing if the trajectory is already aimed at these thresholds.",
            "feedback_incorrect": "The simulation demonstrates that tipping points are real thresholds in the climate system. Moderate emission reductions change the timeline but may not prevent threshold crossing if cumulative warming is already on track to reach critical levels."
        }
    ]
}

L03_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "In epidemiology, what does R-naught (R0) represent?",
            "choices": {
                "A": "The total number of people who will be infected during a pandemic",
                "B": "The average number of new infections caused by one infected person in a fully susceptible population",
                "C": "The mortality rate of a disease in a given population",
                "D": "The speed at which a vaccine can be distributed"
            },
            "correct": "B",
            "feedback_correct": "Correct. R0 represents the basic reproduction number, indicating how many secondary infections one infected person generates on average in a population where everyone is susceptible.",
            "feedback_incorrect": "R0 is not a count of total infections or a mortality rate. It specifically measures transmission potential: how many new cases one infected person typically creates in a fully susceptible population."
        },
        {
            "question": "Why does an infectious disease initially spread exponentially through a population?",
            "choices": {
                "A": "Because the virus mutates to become more contagious over time",
                "B": "Because hospitals become overwhelmed and cannot treat patients",
                "C": "Because each infected person infects multiple new people, and each of those infects multiple more, creating compound growth",
                "D": "Because governments delay their response to the outbreak"
            },
            "correct": "C",
            "feedback_correct": "Correct. Exponential growth occurs because the rate of increase is proportional to the current number infected. If each person infects 3 others, one case becomes 3, then 9, then 27, with each generation multiplying by the same factor.",
            "feedback_incorrect": "Exponential spread is a mathematical property of compound transmission, not a result of mutations or policy failures. When each infected person creates multiple new infections, the total grows by a multiplying factor each generation."
        },
        {
            "question": "The SIR model divides a population into three compartments: Susceptible, Infected, and Recovered. Why does the epidemic eventually peak and decline even without intervention?",
            "choices": {
                "A": "The virus naturally becomes weaker over time",
                "B": "As more people recover and gain immunity, fewer susceptible people remain for the virus to infect",
                "C": "Infected people stop being contagious after a fixed period",
                "D": "The population develops collective behavioral changes"
            },
            "correct": "B",
            "feedback_correct": "Correct. The epidemic peaks when the susceptible population is depleted to the point where each infected person cannot sustain transmission to enough new hosts. As Recovered increases, Susceptible decreases, naturally reducing the transmission rate.",
            "feedback_incorrect": "The epidemic declines because the Susceptible pool shrinks. As individuals move from Susceptible to Infected to Recovered, fewer susceptible hosts remain, reducing the effective reproduction number below 1."
        },
        {
            "question": "What is the herd immunity threshold?",
            "choices": {
                "A": "The point at which everyone in the population has been infected",
                "B": "The proportion of the population that must be immune to stop sustained transmission",
                "C": "The minimum number of hospital beds needed during a pandemic",
                "D": "The temperature at which the virus can no longer survive"
            },
            "correct": "B",
            "feedback_correct": "Correct. The herd immunity threshold is the proportion of the population that must be immune (through infection or vaccination) so that each infected person generates fewer than one new infection on average, causing the epidemic to decline.",
            "feedback_incorrect": "Herd immunity does not require everyone to be infected. It is the percentage of immune individuals needed to reduce the effective reproduction number below 1, preventing sustained transmission through the population."
        },
        {
            "question": "A city implements strict quarantine measures that reduce person-to-person contact by 75%. How does this affect the course of an epidemic?",
            "choices": {
                "A": "It eliminates the disease completely within days",
                "B": "It has no effect because the virus will eventually infect everyone",
                "C": "It reduces the effective reproduction number, slowing the spread and lowering the peak number of infections",
                "D": "It only delays the epidemic without changing the total number of infections"
            },
            "correct": "C",
            "feedback_correct": "Correct. Reducing contact rate directly reduces the effective R value. If R0 is 3 and contact is reduced 75%, the effective R drops to about 0.75, meaning the epidemic shrinks rather than grows.",
            "feedback_incorrect": "Quarantine works by reducing the contact rate, which directly lowers the effective reproduction number. This both slows the spread and reduces the total number of infections, not just the timing."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's SIR model shows that implementing quarantine at 1% infection rate versus 10% infection rate results in 60% fewer total infections despite identical quarantine strength. What principle does this demonstrate?",
            "choices": {
                "A": "Quarantine only works during the early stages of an epidemic",
                "B": "The timing of intervention is critically important because exponential growth makes early action disproportionately effective",
                "C": "The 10% scenario used a weaker quarantine measure",
                "D": "The 1% scenario had a smaller initial population"
            },
            "correct": "B",
            "feedback_correct": "Correct. During exponential growth, the number of infected people doubles rapidly. Intervening early (at 1%) stops the doubling chain much sooner, preventing vastly more infections than the same intervention applied after significant spread.",
            "feedback_incorrect": "The intervention was identical in both scenarios. The difference in outcome is entirely due to timing. Exponential growth means that waiting from 1% to 10% infection allows enormous additional transmission that even strong intervention cannot undo."
        },
        {
            "question": "In the SIR model, the Susceptible, Infected, and Recovered compartments are described as 'coupled.' What does this mean in systems thinking terms?",
            "choices": {
                "A": "Each compartment operates independently with fixed populations",
                "B": "Changes in one compartment directly affect the flows into and out of the other compartments",
                "C": "The compartments are grouped together for mathematical convenience but do not interact",
                "D": "Coupling means the model requires three separate simulations to run"
            },
            "correct": "B",
            "feedback_correct": "Correct. Coupled compartments means the state of each compartment influences the others. New infections depend on BOTH the number of Susceptible AND Infected people simultaneously, creating interdependent dynamics.",
            "feedback_incorrect": "Coupling means the compartments are dynamically linked. The flow from Susceptible to Infected depends on the product of Susceptible and Infected populations. As one changes, all flows in the system adjust."
        },
        {
            "question": "The model shows that vaccination moves people directly from Susceptible to Recovered without passing through Infected. Why is this pathway so valuable compared to natural immunity?",
            "choices": {
                "A": "Vaccinated people develop stronger immunity than naturally infected people",
                "B": "Vaccination achieves the same epidemic-slowing effect (reducing the Susceptible pool) without the disease burden, hospital strain, and deaths of the Infected stage",
                "C": "Vaccination completely eliminates the pathogen from the environment",
                "D": "Vaccination works faster than natural infection"
            },
            "correct": "B",
            "feedback_correct": "Correct. In the SIR model, both infection and vaccination reduce the Susceptible pool. But vaccination achieves this without the suffering, healthcare burden, and mortality of passing through the Infected compartment.",
            "feedback_incorrect": "The model shows that both pathways reduce Susceptible and increase Recovered, slowing the epidemic identically from a mathematical perspective. The critical advantage of vaccination is bypassing the Infected stage and its associated harm."
        },
        {
            "question": "A simulation compares an uncontrolled epidemic to one with moderate intervention. Both ultimately infect similar percentages of the population, but the intervention scenario has far fewer deaths. What explains this?",
            "choices": {
                "A": "The intervened epidemic used a less deadly strain",
                "B": "Flattening the curve spread infections over more time, keeping hospital capacity from being overwhelmed",
                "C": "Fewer people were actually infected in the intervention scenario",
                "D": "The intervention eliminated the most dangerous variant"
            },
            "correct": "B",
            "feedback_correct": "Correct. Flattening the curve does not necessarily reduce total infections, but it spreads them over a longer period. This prevents hospitals from being overwhelmed, ensuring patients receive adequate care, which reduces mortality.",
            "feedback_incorrect": "The question states that similar percentages were infected. The difference in deaths comes from the rate of infection. When the peak is flattened, hospitals can treat patients effectively. When overwhelmed, patients who could have survived die from inadequate care."
        },
        {
            "question": "Based on the model, what happens to the effective reproduction number as more people are vaccinated, and what is the significance of this change?",
            "choices": {
                "A": "The effective R stays constant because vaccination does not affect viral transmission",
                "B": "The effective R increases because vaccinated people create new evolutionary pressure on the virus",
                "C": "The effective R decreases proportionally as the Susceptible pool shrinks, and the epidemic can no longer sustain itself when R drops below 1",
                "D": "The effective R drops to exactly zero once any vaccination program begins"
            },
            "correct": "C",
            "feedback_correct": "Correct. The effective R equals R0 multiplied by the fraction of the population still susceptible. Vaccination reduces this fraction, lowering the effective R. When it drops below 1, each infection generates less than one new case, and the epidemic declines.",
            "feedback_incorrect": "Vaccination shrinks the Susceptible pool, directly reducing the effective reproduction number. The critical threshold is R < 1, at which point the epidemic declines rather than grows. This is the mathematical basis of herd immunity."
        }
    ]
}

L04_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is the difference between opioid tolerance and opioid dependence?",
            "choices": {
                "A": "Tolerance and dependence are the same thing, just different terms for addiction",
                "B": "Tolerance means the body needs higher doses for the same effect; dependence means the body cannot function normally without the drug",
                "C": "Tolerance is a psychological condition; dependence is a social behavior",
                "D": "Tolerance develops only with illegal opioids; dependence develops only with prescription opioids"
            },
            "correct": "B",
            "feedback_correct": "Correct. Tolerance is a neurological adaptation where repeated exposure reduces receptor sensitivity, requiring higher doses. Dependence is a state where the brain has physically adapted to the drug's presence and experiences withdrawal without it.",
            "feedback_incorrect": "Tolerance and dependence are distinct neurological processes. Tolerance means diminished response requiring dose escalation. Dependence means the brain has restructured to require the drug for normal function."
        },
        {
            "question": "How do opioids produce their pain-relieving and euphoric effects in the brain?",
            "choices": {
                "A": "They destroy pain-sensing nerve cells permanently",
                "B": "They bind to opioid receptors, triggering dopamine release in the brain's reward pathways",
                "C": "They increase blood flow to injured areas, accelerating healing",
                "D": "They strengthen the immune system to fight the source of pain"
            },
            "correct": "B",
            "feedback_correct": "Correct. Opioids bind to mu-opioid receptors in the brain, triggering an excessive release of dopamine in reward pathways. This produces both pain relief and the euphoria that contributes to addiction potential.",
            "feedback_incorrect": "Opioids work by mimicking natural endorphins and binding to opioid receptors in the brain. This binding triggers a surge of dopamine, the neurotransmitter associated with pleasure and reward."
        },
        {
            "question": "Why does chronic opioid use often lead to increased pain sensitivity rather than continued pain relief?",
            "choices": {
                "A": "The injury worsens over time regardless of medication",
                "B": "Opioids have no actual effect on pain after the first dose",
                "C": "The brain compensates for chronic opioid exposure by increasing pain sensitivity, a phenomenon called opioid-induced hyperalgesia",
                "D": "Patients become psychologically convinced their pain is worse"
            },
            "correct": "C",
            "feedback_correct": "Correct. Opioid-induced hyperalgesia occurs when chronic opioid use causes the nervous system to amplify pain signals as a compensatory response, paradoxically making the patient more sensitive to pain than before treatment.",
            "feedback_incorrect": "Opioid-induced hyperalgesia is a neurological adaptation, not psychological. The brain upregulates pain sensitivity pathways to compensate for chronic opioid receptor activation, creating a paradox where the treatment increases the problem."
        },
        {
            "question": "What role did pharmaceutical marketing play in the opioid epidemic?",
            "choices": {
                "A": "Pharmaceutical companies had no involvement; the epidemic was entirely caused by illegal drug use",
                "B": "Companies aggressively marketed prescription opioids as non-addictive, leading to widespread over-prescribing",
                "C": "Companies accurately represented the risks, but patients misused the medications",
                "D": "Marketing only affected a small number of prescriptions in rural areas"
            },
            "correct": "B",
            "feedback_correct": "Correct. Pharmaceutical companies, most notably Purdue Pharma, marketed opioids like OxyContin as having very low addiction risk. This led to massive over-prescribing, creating millions of dependent patients who fueled the epidemic.",
            "feedback_incorrect": "The opioid epidemic was significantly driven by pharmaceutical marketing that downplayed addiction risks. This led to over-prescribing on a massive scale, creating the initial wave of dependence that cascaded into a broader crisis."
        },
        {
            "question": "How can one person's opioid prescription contribute to addiction in other people within their community?",
            "choices": {
                "A": "Opioid addiction is contagious through casual contact",
                "B": "Unused prescription pills can be diverted to friends or family, and social network effects normalize opioid use in the community",
                "C": "Other people become addicted by being in the same room as someone taking opioids",
                "D": "Prescriptions have no effect on anyone other than the prescribed patient"
            },
            "correct": "B",
            "feedback_correct": "Correct. Unused pills become a source of exposure for others. Social network effects mean that as opioid use becomes normalized in a community, more people are exposed, creating a reinforcing loop that amplifies the epidemic beyond the original patient.",
            "feedback_incorrect": "Opioid spread through communities occurs through pill diversion (sharing or selling unused prescriptions) and social normalization. One prescription creates a supply that can expose multiple individuals through social networks."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The opioid model contains multiple reinforcing feedback loops. Which of the following correctly describes the tolerance-dose escalation loop?",
            "choices": {
                "A": "Higher doses cause tolerance, which reduces pain, which eliminates the need for opioids",
                "B": "Tolerance reduces opioid effectiveness, requiring higher doses, which accelerates further tolerance development, creating a spiral of escalation",
                "C": "Tolerance protects patients from addiction by making them less sensitive to opioids",
                "D": "Higher doses reduce tolerance, allowing patients to return to lower doses over time"
            },
            "correct": "B",
            "feedback_correct": "Correct. The tolerance loop is a classic reinforcing cycle: opioid exposure reduces receptor sensitivity (tolerance), requiring higher doses for the same effect, which drives faster receptor adaptation, demanding even higher doses.",
            "feedback_incorrect": "The tolerance-escalation loop is reinforcing, not self-correcting. As tolerance develops, the effective dose decreases, prompting dose increases that accelerate receptor adaptation, creating a spiraling cycle of escalation."
        },
        {
            "question": "A student's model identifies a threshold in the system where a patient transitions from manageable pain treatment to physiological dependence. What makes this threshold so significant?",
            "choices": {
                "A": "It is the point where the patient decides to become addicted",
                "B": "It marks the transition from reversible receptor adaptation to structural brain changes that make normal function impossible without the drug",
                "C": "It is an arbitrary line that has no biological basis",
                "D": "It only applies to patients who misuse their prescriptions"
            },
            "correct": "B",
            "feedback_correct": "Correct. The dependence threshold represents a shift from temporary receptor changes (which reverse when the drug is removed) to structural neurological adaptations. Past this point, the brain has physically reorganized to require opioids for normal function.",
            "feedback_incorrect": "Addiction is not a choice but a neurological state change. The threshold represents the point where brain adaptations become structural, making dependence a physiological condition that persists even if the patient wants to stop."
        },
        {
            "question": "The simulation shows that the opioid epidemic has three distinct reinforcing loops: tolerance-escalation, hyperalgesia, and social network spread. How do these coupled loops make the crisis more difficult to address than a single-loop problem?",
            "choices": {
                "A": "Multiple loops have no additional effect compared to a single loop",
                "B": "Each loop operates at a different scale (individual brain, patient experience, community), requiring simultaneous intervention at all levels",
                "C": "Multiple loops cancel each other out, naturally stabilizing the system",
                "D": "Only the social network loop matters; the brain-level loops are insignificant"
            },
            "correct": "B",
            "feedback_correct": "Correct. The three loops operate at neurochemical, physiological, and social scales. Addressing only one level (e.g., reducing prescriptions) does not break the other loops (existing dependence, community supply). Effective intervention must target all three simultaneously.",
            "feedback_incorrect": "Multi-scale reinforcing loops create a multi-level crisis. Breaking the prescription loop does not break the tolerance loop in already-dependent individuals, and neither addresses the social network that has created alternative supply chains."
        },
        {
            "question": "Based on model evidence, which intervention strategy would be most effective at addressing the opioid epidemic?",
            "choices": {
                "A": "Criminalizing all opioid use to deter patients from seeking prescriptions",
                "B": "A combined approach targeting prescription practices, medication-assisted treatment for dependent patients, and community-level supply reduction",
                "C": "Relying solely on education campaigns to inform patients about addiction risks",
                "D": "Developing more potent opioids that require smaller doses"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows three coupled feedback loops operating at different scales. Effective intervention must simultaneously address prescribing (prevention), dependence (treatment with medication-assisted therapy), and social spread (community supply reduction).",
            "feedback_incorrect": "The model demonstrates that single-target interventions fail because they leave other reinforcing loops intact. Only a multi-level approach targeting all three loops simultaneously can interrupt the cascading dynamics of the epidemic."
        },
        {
            "question": "A student argues that 'addiction is a choice, not a disease.' How does the computational model challenge this claim?",
            "choices": {
                "A": "The model supports the claim because patients choose to take the first dose",
                "B": "The model shows that once dopamine receptor downregulation crosses the dependence threshold, brain chemistry is physically altered in ways that override voluntary decision-making",
                "C": "The model shows that willpower is the primary variable determining addiction outcomes",
                "D": "The model cannot address whether addiction is a choice or a disease"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that past the dependence threshold, tolerance and receptor downregulation physically restructure brain reward pathways. The compulsive drug-seeking behavior is driven by altered neurochemistry, not character or willpower.",
            "feedback_incorrect": "The computational model provides evidence that addiction involves measurable, physical changes in brain chemistry. Receptor downregulation and tolerance create neurological states where the brain requires opioids for normal function, which is a disease process, not a behavioral choice."
        }
    ]
}

L05_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is coral bleaching, and what causes it?",
            "choices": {
                "A": "Coral turns white because ocean pollution physically coats its surface",
                "B": "Coral expels its symbiotic algae (zooxanthellae) due to thermal stress, losing its color and primary energy source",
                "C": "Coral bleaching is a natural seasonal process that strengthens the coral over time",
                "D": "Bleaching occurs when predators consume the outer layer of coral tissue"
            },
            "correct": "B",
            "feedback_correct": "Correct. Coral bleaching occurs when thermal stress causes coral to expel the zooxanthellae that live within its tissues. These symbiotic algae provide up to 90% of coral's energy through photosynthesis, and their loss can be fatal.",
            "feedback_incorrect": "Coral bleaching is a stress response, not pollution coating or natural cycling. When water temperatures exceed a threshold, coral expels the photosynthetic zooxanthellae living in its tissue, losing both color and its primary energy source."
        },
        {
            "question": "Zooxanthellae are photosynthetic organisms that live within coral tissue. What percentage of the coral's energy do they provide?",
            "choices": {
                "A": "About 10%, with coral getting most energy from filter feeding",
                "B": "About 50%, split evenly with other energy sources",
                "C": "Up to 90%, making them essential for coral survival",
                "D": "Less than 5%, making them relatively unimportant to coral health"
            },
            "correct": "C",
            "feedback_correct": "Correct. Zooxanthellae provide up to 90% of the coral's energy through photosynthesis, making the symbiotic relationship essential. When zooxanthellae are expelled during bleaching, the coral is effectively starved of its primary energy supply.",
            "feedback_incorrect": "Zooxanthellae provide up to 90% of coral energy, making them far more than a minor contributor. This is why bleaching (expelling zooxanthellae) is so devastating, as it eliminates the coral's primary energy source."
        },
        {
            "question": "What is a 'phase shift' in the context of coral reef ecosystems?",
            "choices": {
                "A": "A temporary change in ocean currents that affects reef temperature",
                "B": "A fundamental transition from a coral-dominated ecosystem to an algae-dominated one that is extremely difficult to reverse",
                "C": "The daily cycle of photosynthesis and respiration on the reef",
                "D": "A seasonal migration of fish species between reef habitats"
            },
            "correct": "B",
            "feedback_correct": "Correct. A phase shift is a fundamental state change where the reef transitions from coral-dominated to algae-dominated. This new state is self-reinforcing and extremely difficult to reverse because the conditions that support coral recovery are eliminated.",
            "feedback_incorrect": "A phase shift represents a permanent state change, not a temporary fluctuation. Once a reef shifts from coral-dominated to algae-dominated, the algae prevent coral recovery by smothering settlement surfaces and altering water chemistry."
        },
        {
            "question": "How does ocean acidification affect coral reef organisms?",
            "choices": {
                "A": "It makes coral grow faster by providing more dissolved minerals",
                "B": "It has no measurable effect on marine organisms",
                "C": "It reduces the ability of coral and other calcifying organisms to build and maintain their calcium carbonate skeletons",
                "D": "It only affects fish populations, not coral itself"
            },
            "correct": "C",
            "feedback_correct": "Correct. As oceans absorb CO2, pH decreases, making it harder for coral and other calcifiers to precipitate calcium carbonate for their skeletons. This weakens existing structures and slows new growth.",
            "feedback_incorrect": "Ocean acidification reduces the availability of carbonate ions that coral needs to build its calcium carbonate skeleton. Lower pH means coral must expend more energy to calcify, weakening structures and slowing growth."
        },
        {
            "question": "Why are herbivorous fish important to coral reef health?",
            "choices": {
                "A": "They provide food for coral polyps through their waste products",
                "B": "They graze on algae that would otherwise smother coral, keeping reef surfaces clear for coral growth",
                "C": "They have no significant relationship with coral health",
                "D": "They transport nutrients from deep water to the reef surface"
            },
            "correct": "B",
            "feedback_correct": "Correct. Herbivorous fish like parrotfish and tangs graze algae off reef surfaces, preventing algae overgrowth that would smother coral. When fish populations decline, algae can outcompete coral for space and light.",
            "feedback_incorrect": "Herbivorous fish play a critical role in controlling algae. Without grazing pressure, fast-growing algae outcompete slow-growing coral for light and space, accelerating the transition toward an algae-dominated state."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The simulation shows that a 0.5-degree C temperature increase for one season causes bleaching, but coral recovers when temperatures normalize. However, a sustained 1.5-degree C increase causes permanent phase shift. What systems concept explains this difference?",
            "choices": {
                "A": "Linear response, where greater input always produces proportionally greater output",
                "B": "Threshold dynamics, where the system can absorb stress up to a point but collapses rapidly beyond it",
                "C": "Random variation in coral resilience between the two scenarios",
                "D": "The 1.5-degree scenario lasted longer simply because the temperature was higher"
            },
            "correct": "B",
            "feedback_correct": "Correct. This demonstrates threshold dynamics. Below the threshold, the system has enough resilience to recover. Above it, cascading feedback loops activate and the system enters a new stable state (phase shift) that resists reversal.",
            "feedback_incorrect": "The difference is not proportional (linear) but threshold-based. The 0.5-degree scenario stays within the system's recovery capacity, while 1.5 degrees crosses a critical threshold that activates self-reinforcing cascading feedback loops."
        },
        {
            "question": "The model reveals that three moderate stressors (temperature +1 degree C, acidity +0.1 pH, high fishing pressure) applied simultaneously cause reef collapse, while any single stressor at the same level does not. What does this demonstrate about coupled systems?",
            "choices": {
                "A": "The three stressors cancel each other out in some way",
                "B": "Multiple stressors interact synergistically, meaning their combined effect exceeds the sum of their individual effects",
                "C": "Only temperature matters; the other stressors are irrelevant",
                "D": "The model is flawed because individual stressors should produce the same result as combined ones"
            },
            "correct": "B",
            "feedback_correct": "Correct. The stressors interact synergistically through coupled feedback loops. Acidification lowers the bleaching threshold, fishing removes algae grazers, and temperature triggers bleaching. Together they push the system past a threshold that no single stressor could reach alone.",
            "feedback_incorrect": "This is synergistic interaction, where combined stressors produce effects greater than the sum of individual effects. Each stressor weakens the system's resilience, lowering the threshold for the other stressors to cause collapse."
        },
        {
            "question": "After a phase shift to algae dominance, the model shows the reef does not recover even when temperature returns to normal. Which systems thinking concept explains this irreversibility?",
            "choices": {
                "A": "The model has an error because removing the stressor should restore the system",
                "B": "The algae-dominated state is a stable alternative equilibrium maintained by its own reinforcing feedback loops",
                "C": "Temperature is not actually a factor in reef health",
                "D": "The reef needs more time but will eventually recover on its own"
            },
            "correct": "B",
            "feedback_correct": "Correct. The phase shift creates a new stable state. Algae smother coral settlement surfaces, degraded reef structure cannot support herbivorous fish, and without fish, algae grows unchecked. These self-reinforcing dynamics maintain the algae-dominated state.",
            "feedback_incorrect": "The algae-dominated state is self-reinforcing. Without coral structure, fish leave. Without fish, algae is uncontrolled. Algae smothers any new coral. This new equilibrium persists even after the original temperature stress is removed."
        },
        {
            "question": "A student's model identifies zooxanthellae density as the most sensitive component in the system. What makes this component a critical leverage point?",
            "choices": {
                "A": "Zooxanthellae are the most visually obvious component of the reef",
                "B": "Zooxanthellae provide 90% of coral energy, so their loss triggers cascading failure through every connected component in the system",
                "C": "Zooxanthellae are the easiest component to measure in the field",
                "D": "Zooxanthellae only affect coral color, not reef function"
            },
            "correct": "B",
            "feedback_correct": "Correct. Because zooxanthellae supply 90% of coral energy, their loss triggers a cascade: coral weakens and dies, reef structure degrades, fish lose habitat, algae overgrows. This single component's failure propagates through the entire coupled system.",
            "feedback_incorrect": "Zooxanthellae are a leverage point because they are the energy foundation of the entire reef ecosystem. Their loss does not just affect coral color; it initiates a cascading failure that propagates through energy supply, structural integrity, fish habitat, and algae competition."
        },
        {
            "question": "Based on the model, which reef restoration strategy would be most effective at preventing phase shift?",
            "choices": {
                "A": "Adding artificial color to bleached coral to make it look healthy",
                "B": "Targeting multiple leverage points simultaneously: protecting herbivorous fish populations, reducing local acidification sources, and establishing marine temperature monitoring with early warning systems",
                "C": "Focusing exclusively on reducing global CO2 emissions",
                "D": "Relocating all coral to aquariums until ocean conditions improve"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that multiple coupled stressors drive collapse, so effective intervention must target multiple leverage points. Protecting fish controls algae, reducing local acidification raises bleaching thresholds, and monitoring enables early response.",
            "feedback_incorrect": "Because the reef system involves coupled feedback loops with multiple stressors, effective intervention must address multiple leverage points simultaneously. Single-factor approaches (emissions-only or relocation) fail to address the coupled dynamics."
        }
    ]
}

L06_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What does 'nexus thinking' mean in the context of resource management?",
            "choices": {
                "A": "Managing each resource (water, energy, food) independently for maximum efficiency",
                "B": "Analyzing the interconnections between resource systems and understanding how changes in one affect the others",
                "C": "Prioritizing one critical resource above all others during a crisis",
                "D": "Using advanced technology to eliminate the need for natural resources"
            },
            "correct": "B",
            "feedback_correct": "Correct. Nexus thinking recognizes that water, energy, and food systems are deeply interconnected. Managing one without considering the others can create unintended consequences that worsen the overall resource situation.",
            "feedback_incorrect": "Nexus thinking is fundamentally about recognizing interconnections. Managing resources in isolation (siloed thinking) ignores the trade-offs and feedback loops that connect water, energy, and food production."
        },
        {
            "question": "Why does producing more food typically require more water AND more energy?",
            "choices": {
                "A": "Food production has no significant relationship with water or energy use",
                "B": "Crops need irrigation (water) and processing, transportation, and equipment all consume energy, while irrigation systems themselves require energy to operate",
                "C": "Food production only requires water, not energy",
                "D": "Modern farming has eliminated the need for water through synthetic alternatives"
            },
            "correct": "B",
            "feedback_correct": "Correct. Agriculture is both water-intensive (irrigation, crop growth) and energy-intensive (pumping water, running equipment, processing, refrigeration, transportation). Expanding food production amplifies demand for both resources simultaneously.",
            "feedback_incorrect": "Food production sits at the intersection of water and energy systems. Growing crops requires irrigation, which consumes both water and the energy to pump it. Processing, refrigeration, and transportation add further energy demands."
        },
        {
            "question": "A region builds a desalination plant to address water scarcity. What is the most likely unintended consequence?",
            "choices": {
                "A": "The desalination plant will also generate surplus energy",
                "B": "The plant will significantly increase energy consumption, potentially straining the energy supply",
                "C": "Desalination has no effect on other resource systems",
                "D": "The plant will reduce food production by taking farmland"
            },
            "correct": "B",
            "feedback_correct": "Correct. Desalination is extremely energy-intensive, requiring large amounts of electricity to force water through membranes. Solving the water problem creates increased demand on the energy system, illustrating the nexus trade-off.",
            "feedback_incorrect": "Desalination exemplifies a nexus trade-off. While it addresses water scarcity, it is one of the most energy-intensive water treatment processes, creating significant new demand on the energy system."
        },
        {
            "question": "What is meant by 'carrying capacity' in the context of regional resource systems?",
            "choices": {
                "A": "The maximum weight that transportation infrastructure can support",
                "B": "The maximum population a region can sustain given its available water, energy, and food resources",
                "C": "The number of vehicles that can travel on a highway simultaneously",
                "D": "The amount of cargo a single ship can transport"
            },
            "correct": "B",
            "feedback_correct": "Correct. Carrying capacity is the maximum population that a region's resources can sustain. It is determined by the most limited resource, which means the scarcest of water, energy, or food sets the ceiling for population support.",
            "feedback_incorrect": "In resource management, carrying capacity refers to the sustainable population limit based on available resources. The limiting factor (the scarcest resource) determines the ceiling."
        },
        {
            "question": "How does a circular economy approach differ from a linear 'take-make-dispose' economy in resource management?",
            "choices": {
                "A": "A circular economy uses more resources but creates less pollution",
                "B": "A circular economy minimizes waste by recycling outputs from one process as inputs to another, reducing total resource demand",
                "C": "There is no practical difference between the two approaches",
                "D": "A circular economy only applies to manufacturing, not to water or energy"
            },
            "correct": "B",
            "feedback_correct": "Correct. A circular economy closes resource loops by treating waste as input for other processes. Wastewater becomes irrigation water, food waste becomes biogas energy, and agricultural byproducts become fertilizer.",
            "feedback_incorrect": "A circular economy fundamentally redesigns resource flows to minimize waste. Instead of extract-use-dispose, it recycles outputs as inputs, reducing the total demand on raw resource supplies."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that increasing energy production to meet growing demand causes water availability to decline. What system dynamic explains this?",
            "choices": {
                "A": "Energy production and water availability are unrelated variables in the model",
                "B": "Power generation (especially thermal and nuclear) requires enormous quantities of cooling water, creating direct competition between energy and water systems",
                "C": "Energy production evaporates all nearby water sources",
                "D": "The model is showing random fluctuations, not a causal relationship"
            },
            "correct": "B",
            "feedback_correct": "Correct. Thermal power plants are among the largest industrial water consumers, using water for cooling. Increasing energy output directly increases water withdrawal, creating resource competition between the energy and water systems.",
            "feedback_incorrect": "Power generation is extremely water-intensive. Thermal and nuclear plants require massive cooling water volumes. This creates a direct, measurable trade-off where expanding energy production reduces water available for agriculture and municipalities."
        },
        {
            "question": "A simulation of 30% population growth shows that the water system fails before energy or food. What does this reveal about system constraints?",
            "choices": {
                "A": "Water is always the first resource to fail in any scenario",
                "B": "The most constrained resource (the bottleneck) determines the system's carrying capacity, regardless of how abundant other resources are",
                "C": "Population growth only affects water systems",
                "D": "Energy and food systems are immune to population pressure"
            },
            "correct": "B",
            "feedback_correct": "Correct. This illustrates the concept of a limiting factor or bottleneck. The system's carrying capacity is determined by its weakest link. Even if energy and food are abundant, water scarcity limits the population that can be sustained.",
            "feedback_incorrect": "The bottleneck principle means the scarcest resource sets the system limit. In this scenario, water is the constraint, but in different regions or conditions, energy or food could be the limiting factor."
        },
        {
            "question": "The model demonstrates that a drought reduces water availability by 40%, which then reduces both energy production AND agricultural output. What systems concept does this illustrate?",
            "choices": {
                "A": "Isolated impact, where drought only affects water supply",
                "B": "Cascading failure through coupled systems, where a shock to one resource propagates through interconnected systems",
                "C": "Resilience, where the system absorbs the shock without any downstream effects",
                "D": "The drought scenario is unrealistic and does not reflect real resource dynamics"
            },
            "correct": "B",
            "feedback_correct": "Correct. This demonstrates cascading failure in coupled systems. Because energy production needs cooling water and agriculture needs irrigation water, a water shock propagates through all connected systems, amplifying the original disruption.",
            "feedback_incorrect": "In coupled systems, a disruption to one component propagates to all connected components. Drought reduces water, which reduces energy (cooling) and food (irrigation), creating a multi-system crisis from a single initial shock."
        },
        {
            "question": "A student's model shows that increasing wastewater recycling to 90% partially decouples the water-energy-food nexus. What does 'decoupling' mean in this context?",
            "choices": {
                "A": "The three resources become completely independent of each other",
                "B": "Recycling reduces the competition between systems by creating an alternative water supply that does not require drawing from the same finite source",
                "C": "Decoupling means the model stops working correctly",
                "D": "Wastewater recycling has no effect on resource interdependence"
            },
            "correct": "B",
            "feedback_correct": "Correct. Decoupling reduces the strength of competition between systems. Recycled water provides an alternative supply that reduces the demand on shared freshwater sources, allowing energy and agriculture to draw from different pools.",
            "feedback_incorrect": "Decoupling does not mean complete independence; it means reduced interdependence. By creating an alternative water supply through recycling, the competition between systems for the same finite source is reduced."
        },
        {
            "question": "Based on the model, why is siloed resource planning (managing water, energy, and food independently) likely to fail as populations grow?",
            "choices": {
                "A": "Siloed planning works well at any population scale",
                "B": "Each siloed solution optimizes one resource but creates unintended trade-offs that worsen the others, and population growth amplifies all competition simultaneously",
                "C": "Siloed planning fails only because of poor communication between agencies",
                "D": "Population growth does not affect resource planning approaches"
            },
            "correct": "B",
            "feedback_correct": "Correct. Siloed optimization creates a whack-a-mole dynamic: solving water scarcity with desalination strains energy, expanding energy strains water, expanding agriculture strains both. Population growth multiplies all demands simultaneously, making integrated planning essential.",
            "feedback_incorrect": "The model demonstrates that optimizing one resource in isolation inevitably creates pressure on the others because of their interconnections. As population grows, these trade-offs intensify, making integrated nexus planning the only viable approach."
        }
    ]
}

L07_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is an urban heat island?",
            "choices": {
                "A": "A tropical island located near a major city",
                "B": "A metropolitan area that is significantly warmer than surrounding rural areas due to human-modified surfaces and activities",
                "C": "A heat wave that only affects coastal cities",
                "D": "An area of a city designated for industrial heat production"
            },
            "correct": "B",
            "feedback_correct": "Correct. An urban heat island is the phenomenon where cities experience significantly higher temperatures than surrounding rural and forested areas due to heat-absorbing surfaces, reduced vegetation, and waste heat from buildings and vehicles.",
            "feedback_incorrect": "An urban heat island is not a geographic feature but a temperature phenomenon. Cities with their dark pavement, concrete, and limited vegetation absorb and retain more heat than surrounding natural landscapes."
        },
        {
            "question": "What is albedo, and how does it relate to surface temperature?",
            "choices": {
                "A": "Albedo is the amount of heat a surface generates; high albedo surfaces produce more heat",
                "B": "Albedo is the reflectivity of a surface; high-albedo surfaces reflect more solar radiation and stay cooler",
                "C": "Albedo is a measure of wind speed over urban areas",
                "D": "Albedo is the humidity level in a city compared to rural areas"
            },
            "correct": "B",
            "feedback_correct": "Correct. Albedo measures how much incoming solar radiation a surface reflects. Light-colored and vegetated surfaces have high albedo (reflect more, absorb less heat), while dark surfaces like asphalt have low albedo (absorb more, get hotter).",
            "feedback_incorrect": "Albedo is specifically about reflectivity, not heat generation. A surface with high albedo reflects most incoming solar energy back to space, staying cooler. Low-albedo surfaces (dark pavement, rooftops) absorb that energy as heat."
        },
        {
            "question": "How does air conditioning contribute to outdoor temperatures in a city?",
            "choices": {
                "A": "Air conditioning has no effect on outdoor temperatures",
                "B": "AC units cool both indoor and outdoor air equally",
                "C": "AC units transfer heat from indoors to outdoors, adding waste heat to the surrounding environment",
                "D": "AC units create cold spots in outdoor areas near buildings"
            },
            "correct": "C",
            "feedback_correct": "Correct. Air conditioners work by transferring heat from inside a building to outside. This waste heat warms the surrounding outdoor air, contributing to higher urban temperatures, especially during heat waves when AC use peaks.",
            "feedback_incorrect": "AC units do not destroy heat; they move it. They cool indoor spaces by pumping thermal energy outside, where it warms the surrounding air. During peak cooling demand, the cumulative waste heat from millions of AC units measurably raises outdoor temperatures."
        },
        {
            "question": "What is environmental justice, and how does it relate to urban heat?",
            "choices": {
                "A": "Environmental justice is a legal term for environmental regulations that apply equally to all areas",
                "B": "The principle that no community should bear a disproportionate share of environmental hazards due to race, income, or political power",
                "C": "Environmental justice means all neighborhoods have equal access to air conditioning",
                "D": "It refers to criminal penalties for polluting companies"
            },
            "correct": "B",
            "feedback_correct": "Correct. Environmental justice recognizes that environmental hazards, including extreme heat, are often disproportionately concentrated in low-income communities and communities of color due to historical investment patterns.",
            "feedback_incorrect": "Environmental justice addresses the inequitable distribution of environmental burdens. In urban heat, this means that historically marginalized communities often have less tree cover, more pavement, and greater heat exposure than wealthier neighborhoods."
        },
        {
            "question": "Why do trees and vegetation help cool urban areas?",
            "choices": {
                "A": "Trees block wind, which reduces the wind chill factor and makes areas feel warmer",
                "B": "Trees and vegetation cool air through evapotranspiration (releasing water vapor) and by providing shade that prevents surfaces from absorbing solar radiation",
                "C": "Vegetation has no measurable effect on urban temperatures",
                "D": "Trees only provide psychological cooling, not actual temperature reduction"
            },
            "correct": "B",
            "feedback_correct": "Correct. Trees cool through two mechanisms: evapotranspiration (releasing water vapor that absorbs heat as it evaporates) and shading (preventing solar radiation from heating pavement and buildings). Together, these can reduce local temperatures by several degrees.",
            "feedback_incorrect": "Trees provide measurable cooling through evapotranspiration (a process similar to sweating, where water evaporation absorbs heat) and shading. Studies show tree cover can reduce local temperatures by 2-8 degrees Fahrenheit."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model reveals a reinforcing feedback loop involving air conditioning. Which of the following correctly describes this loop?",
            "choices": {
                "A": "Higher temperatures drive more AC use, which cools the city, reducing temperatures",
                "B": "Higher temperatures drive more AC use, which pumps waste heat outdoors, raising temperatures further, which drives even more AC use",
                "C": "AC use reduces energy consumption by making buildings more efficient",
                "D": "The AC loop is a balancing feedback that stabilizes urban temperatures"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is a reinforcing loop: heat drives AC demand, AC waste heat warms outdoor air, warmer air drives more AC demand. This loop amplifies temperatures, especially during heat waves when the effect is most concentrated.",
            "feedback_incorrect": "AC creates a reinforcing (not balancing) loop. While it cools indoors, it heats outdoors. The cumulative effect of millions of AC units pumping heat into already-hot air creates a self-amplifying cycle."
        },
        {
            "question": "The simulation comparing two neighborhoods shows a 10-degree F temperature difference between a high-green-space neighborhood and a high-concrete neighborhood during a heat wave. The model also shows different health outcomes. What structural factor explains both the temperature AND health disparities?",
            "choices": {
                "A": "Random weather variation between neighborhoods",
                "B": "Historical investment patterns that concentrated green space in wealthy neighborhoods and impervious surfaces in low-income communities, creating both heat exposure and health vulnerability disparities",
                "C": "People in hotter neighborhoods simply prefer warmer temperatures",
                "D": "The two neighborhoods are in different climate zones"
            },
            "correct": "B",
            "feedback_correct": "Correct. The temperature disparity is structural, rooted in historical investment patterns including redlining. Low-income communities received less green infrastructure and more industrial/commercial development, creating heat islands that compound health vulnerabilities.",
            "feedback_incorrect": "Urban heat inequality is not random but structural. Historical policies directed green infrastructure investment to wealthier neighborhoods while concentrating heat-absorbing development in lower-income areas, creating measurable disparities in both temperature and health outcomes."
        },
        {
            "question": "A student's model shows that a regional heat wave of +5 degrees C produces +8 degrees C in the urban core but only +5.5 degrees C in suburban areas. What does this amplification effect demonstrate?",
            "choices": {
                "A": "The model is inaccurate because all areas should experience the same temperature increase",
                "B": "The urban heat island acts as an amplifier, taking a regional temperature increase and magnifying it through heat-absorbing surfaces, reduced vegetation, and reinforcing AC feedback",
                "C": "Suburban areas are immune to heat waves",
                "D": "The urban core has a different climate than surrounding areas"
            },
            "correct": "B",
            "feedback_correct": "Correct. Urban areas amplify regional heat events because their existing heat island infrastructure (dark surfaces, minimal vegetation, waste heat) adds to the regional increase. The AC reinforcing loop further amplifies temperatures during extreme heat.",
            "feedback_incorrect": "The urban heat island does not merely add a constant offset; it amplifies heat events. During a heat wave, the existing urban infrastructure absorbs more energy, vegetation provides less cooling, and the AC feedback loop intensifies."
        },
        {
            "question": "The model identifies green infrastructure as an intervention that 'breaks the reinforcing loop.' How does increasing green space from 10% to 40% break this loop?",
            "choices": {
                "A": "Green space has no effect on the AC feedback loop",
                "B": "Vegetation provides passive cooling through evapotranspiration and shade, reducing ambient temperatures, which reduces AC demand, which reduces waste heat output, interrupting the reinforcing cycle",
                "C": "Green space only improves aesthetics, not temperatures",
                "D": "Increasing green space increases humidity, which makes heat feel worse"
            },
            "correct": "B",
            "feedback_correct": "Correct. Green infrastructure interrupts the reinforcing loop at its source. By cooling the environment passively through evapotranspiration and shade, it reduces the temperature trigger that drives AC use, thereby reducing the waste heat that amplifies outdoor temperatures.",
            "feedback_incorrect": "Green space breaks the loop by providing passive cooling that replaces the need for active (heat-generating) cooling. Lower ambient temperatures mean less AC demand, less waste heat, and a dampened reinforcing cycle."
        },
        {
            "question": "Based on the model, a city has limited budget for cooling interventions. Which approach best reflects systems thinking and environmental justice principles?",
            "choices": {
                "A": "Distribute cooling investments equally across all neighborhoods regardless of current conditions",
                "B": "Invest cooling interventions first in the most heat-vulnerable neighborhoods, where the reinforcing loop is strongest and health risks are highest",
                "C": "Focus investments on the wealthiest neighborhoods because they generate the most tax revenue",
                "D": "Wait until new cooling technologies are developed before investing"
            },
            "correct": "B",
            "feedback_correct": "Correct. Systems thinking shows the reinforcing loop is strongest where green space is lowest and impervious surface is highest. Environmental justice demands that the most vulnerable communities, who bear the greatest heat burden, receive priority investment.",
            "feedback_incorrect": "Equal distribution ignores that the heat burden is unequally distributed. Systems analysis shows that targeting the hottest, most vulnerable neighborhoods breaks the reinforcing loop where it is strongest, producing the greatest temperature reduction per dollar invested."
        }
    ]
}

L08_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "In normal Mendelian inheritance, what percentage of offspring receive a specific allele from one parent?",
            "choices": {
                "A": "100% of offspring",
                "B": "75% of offspring",
                "C": "50% of offspring",
                "D": "25% of offspring"
            },
            "correct": "C",
            "feedback_correct": "Correct. In standard Mendelian inheritance, each parent has two copies of a gene and passes one to each offspring, giving each allele a 50% chance of being inherited.",
            "feedback_incorrect": "Mendelian inheritance follows a 50/50 pattern. Each parent passes one of their two alleles at random, giving any specific allele a 50% chance of being transmitted to each offspring."
        },
        {
            "question": "What is a gene drive?",
            "choices": {
                "A": "A natural process by which genes spread through a population over thousands of generations",
                "B": "A genetic engineering technology that biases inheritance so an engineered gene is passed to nearly all offspring (95-99%) rather than the normal 50%",
                "C": "A device used to sequence DNA in a laboratory",
                "D": "A type of gene therapy used to treat human diseases"
            },
            "correct": "B",
            "feedback_correct": "Correct. A gene drive uses CRISPR technology to copy itself onto both chromosomes, ensuring nearly all offspring inherit the engineered gene. This allows the modification to spread through a wild population far faster than normal inheritance would allow.",
            "feedback_incorrect": "Gene drives are engineered systems that 'cheat' at inheritance. By copying themselves to both chromosomes, they achieve 95-99% inheritance instead of the normal 50%, allowing rapid spread through a population."
        },
        {
            "question": "What is a 'fitness cost' in evolutionary biology?",
            "choices": {
                "A": "The financial cost of maintaining a genetic engineering program",
                "B": "A reduction in an organism's survival or reproductive success caused by carrying a particular genetic trait",
                "C": "The energy required for an organism to exercise",
                "D": "The price of genetic testing for a particular allele"
            },
            "correct": "B",
            "feedback_correct": "Correct. A fitness cost means carrying a specific gene reduces the organism's ability to survive or reproduce. Natural selection acts against genes with fitness costs, which is relevant to gene drives because engineered genes may reduce host fitness.",
            "feedback_incorrect": "In evolutionary terms, fitness refers to reproductive success, not physical exercise. A fitness cost means a gene reduces the carrier's survival or reproduction rate, making natural selection work against that gene over time."
        },
        {
            "question": "Why is the potential application of gene drives to malaria-carrying mosquitoes considered both promising and controversial?",
            "choices": {
                "A": "Gene drives would be too expensive to deploy in tropical regions",
                "B": "Gene drives could eliminate malaria (which kills 600,000 people per year) but could also have unpredictable ecological consequences from removing or modifying an entire species",
                "C": "Gene drives have already been proven completely safe through decades of field testing",
                "D": "Malaria mosquitoes are immune to genetic modification"
            },
            "correct": "B",
            "feedback_correct": "Correct. The tension is between massive humanitarian benefit (preventing 600,000 deaths annually) and unknown ecological risk (what happens when you suppress or modify a species that is part of complex food webs and ecosystems).",
            "feedback_incorrect": "Gene drives for malaria represent a genuine ethical dilemma: the technology could save hundreds of thousands of lives, but the ecological consequences of altering wild populations are largely unknown and potentially irreversible."
        },
        {
            "question": "What happens if natural resistance evolves against a gene drive after it has been released into a wild population?",
            "choices": {
                "A": "Resistance is impossible because gene drives are too powerful",
                "B": "Resistance mutations could halt the drive's spread, leaving a partially modified population with unknown consequences",
                "C": "Resistance would strengthen the gene drive's effect",
                "D": "Scientists can simply recall the gene drive from the wild population"
            },
            "correct": "B",
            "feedback_correct": "Correct. Resistance mutations that prevent the gene drive from copying itself can arise and spread through natural selection. If this happens mid-deployment, the population is partially modified, potentially the worst outcome because neither the goal nor the original state is achieved.",
            "feedback_incorrect": "Resistance evolution is a real concern. Gene drives cannot be recalled from wild populations, and if resistance halts the drive partway through, the result is a partially modified population in an unknown ecological state."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The simulation shows that a gene drive with 99% inheritance bias and zero fitness cost reaches fixation (100% of population) in approximately 12 generations. When fitness cost is added at 10%, the drive still reaches fixation but takes 20 generations. What does this comparison reveal about the relative strength of inheritance bias versus natural selection?",
            "choices": {
                "A": "Natural selection completely overrides the gene drive",
                "B": "The mathematical advantage of 99% inheritance is strong enough to overcome moderate natural selection against the drive, though fitness costs slow the process",
                "C": "Fitness costs have no effect on gene drive dynamics",
                "D": "The drive reaches fixation at the same speed regardless of fitness cost"
            },
            "correct": "B",
            "feedback_correct": "Correct. The 99% inheritance bias creates a powerful mathematical advantage over the normal 50%. Even with a 10% fitness cost (natural selection pushing back), the inheritance advantage dominates, reaching fixation at a slower but still inevitable pace.",
            "feedback_incorrect": "The gene drive's inheritance advantage (99% vs. 50%) is a powerful mathematical force. Fitness costs create opposing selection pressure, but moderate costs only slow the drive without stopping it, because the inheritance bias is disproportionately strong."
        },
        {
            "question": "The model reveals a critical race between gene drive spread and resistance evolution. Under what conditions does resistance 'win' against the drive?",
            "choices": {
                "A": "Resistance always wins because natural selection is all-powerful",
                "B": "Resistance wins when the rate of resistance mutation emergence exceeds the drive's ability to spread faster than resistant individuals reproduce",
                "C": "Resistance never wins against a properly designed gene drive",
                "D": "Resistance only matters in laboratory settings, not in wild populations"
            },
            "correct": "B",
            "feedback_correct": "Correct. It is a rate competition. If resistance mutations arise and spread through natural selection faster than the drive can reach fixation, resistance individuals outcompete drive carriers, and the drive stalls.",
            "feedback_incorrect": "The outcome depends on relative rates. In large populations with high genetic diversity, resistance mutations are more likely to arise. If they spread fast enough through natural selection, they can outcompete the drive before it reaches fixation."
        },
        {
            "question": "A student's model shows that suppressing mosquito populations by 90% causes significant declines in bat, bird, and fish populations that feed on mosquitoes. What systems concept does this demonstrate?",
            "choices": {
                "A": "Mosquitoes are unimportant in ecosystems and can be safely removed",
                "B": "Ecological cascading effects, where removing one species propagates disruptions through the food web to species that depend on it",
                "C": "The model is flawed because mosquitoes have no ecological role",
                "D": "Only the mosquito population is affected by gene drive deployment"
            },
            "correct": "B",
            "feedback_correct": "Correct. Removing or suppressing a species creates ripple effects through the food web. Species that depend on mosquitoes as food (bats, birds, fish, other insects) lose a resource, which can cascade further up the food chain.",
            "feedback_incorrect": "Ecosystems are interconnected networks. Suppressing one species affects all species connected to it. Mosquitoes serve as food for many predators, and their removal or reduction triggers cascading effects that propagate through the entire food web."
        },
        {
            "question": "The simulation demonstrates that once a gene drive is released into a wild population, it cannot be recalled. Why is this irreversibility fundamentally different from other biotechnologies?",
            "choices": {
                "A": "All biotechnologies are equally irreversible",
                "B": "Unlike contained technologies, a self-propagating gene drive reproduces and spreads autonomously through the ecosystem, making it impossible to retrieve or control after release",
                "C": "Gene drives can be reversed by releasing a second gene drive",
                "D": "Irreversibility is only a theoretical concern with no practical implications"
            },
            "correct": "B",
            "feedback_correct": "Correct. A gene drive is self-propagating, meaning it reproduces and spreads through natural mating. Unlike a chemical spill (which can be cleaned) or a GMO crop (which can be contained), a gene drive becomes part of the wild gene pool permanently.",
            "feedback_incorrect": "The key distinction is self-propagation. Most technologies can be recalled, deactivated, or contained. A gene drive, once released, spreads autonomously through reproduction. It cannot be collected from wild organisms or reversed once integrated into the gene pool."
        },
        {
            "question": "Based on the model evidence, which deployment strategy best balances the humanitarian goal of malaria elimination with ecological safety?",
            "choices": {
                "A": "Immediate global release of the strongest possible gene drive to maximize speed",
                "B": "A phased approach: contained testing, isolated island trials, staged regional deployment with continuous monitoring for resistance and ecological impacts, with predefined halt criteria",
                "C": "Avoid gene drive technology entirely because the risks are too high",
                "D": "Deploy the gene drive only in laboratories and never release it into the wild"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that outcomes depend on parameters (fitness cost, resistance rate, ecological connections) that vary across environments. A phased approach allows data collection at each stage, with the ability to halt before irreversible consequences occur.",
            "feedback_incorrect": "The model demonstrates that uncertainty in ecological impacts and resistance dynamics requires a cautious, staged approach. Phased deployment with monitoring and halt criteria balances the urgency of disease elimination with the irreversibility of the technology."
        }
    ]
}

L09_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What are microplastics?",
            "choices": {
                "A": "A type of biodegradable plastic designed to break down quickly in the environment",
                "B": "Plastic particles smaller than 5mm that result from degradation of larger plastics or are manufactured as microbeads, persisting in the environment for centuries",
                "C": "Microscopic organisms that feed on plastic waste in the ocean",
                "D": "A new type of recyclable plastic developed for marine environments"
            },
            "correct": "B",
            "feedback_correct": "Correct. Microplastics are plastic particles under 5mm that persist in the environment for hundreds of years. They come from breakdown of larger plastics and from products containing manufactured microbeads.",
            "feedback_incorrect": "Microplastics are defined as plastic particles smaller than 5mm. They are not biodegradable and persist for centuries, entering food chains and accumulating at every trophic level."
        },
        {
            "question": "What is the difference between bioaccumulation and biomagnification?",
            "choices": {
                "A": "They are the same process described with different terms",
                "B": "Bioaccumulation is the buildup of a substance within a single organism over time; biomagnification is the increasing concentration at each higher level of the food chain",
                "C": "Bioaccumulation only occurs in marine organisms; biomagnification only occurs on land",
                "D": "Bioaccumulation reduces toxin levels; biomagnification increases them"
            },
            "correct": "B",
            "feedback_correct": "Correct. Bioaccumulation occurs within one organism as intake exceeds excretion. Biomagnification occurs across trophic levels as predators accumulate the combined load from all their prey, creating progressively higher concentrations up the food chain.",
            "feedback_incorrect": "These are related but distinct processes. Bioaccumulation is the buildup within a single organism. Biomagnification is the amplification across trophic levels, where each predator inherits the accumulated load of all its prey organisms."
        },
        {
            "question": "Why is the extremely slow decomposition rate of plastics a significant environmental concern?",
            "choices": {
                "A": "Slow decomposition means plastics are recyclable and therefore not a problem",
                "B": "Because plastic input far exceeds decomposition, concentrations in the environment can only increase over time, creating a one-way accumulation problem",
                "C": "Slow decomposition is beneficial because it means plastic products last longer",
                "D": "Decomposition rate has no relationship to environmental impact"
            },
            "correct": "B",
            "feedback_correct": "Correct. With a decomposition rate measured in centuries and an input rate measured in millions of tons per year, environmental plastic concentration can only go up. Even stopping all new plastic input would not reduce existing concentrations for hundreds of years.",
            "feedback_incorrect": "The mismatch between input rate (millions of tons per year) and decomposition rate (centuries) means plastic accumulates relentlessly. This one-way ratchet ensures environmental concentrations rise year after year."
        },
        {
            "question": "How do microplastics enter the human food supply?",
            "choices": {
                "A": "Only through direct ingestion of plastic products",
                "B": "Through the food chain: marine organisms ingest microplastics, fish eat those organisms, and humans eat the fish, inheriting accumulated plastic from every trophic level below",
                "C": "Microplastics do not enter the human food supply",
                "D": "Only through drinking water contamination, not through food"
            },
            "correct": "B",
            "feedback_correct": "Correct. Microplastics enter the food chain at the lowest level (plankton) and are amplified through trophic transfer. Humans, as top consumers, ingest the accumulated plastic from the entire food chain, plus additional exposure from water and air.",
            "feedback_incorrect": "Microplastics reach humans through multiple pathways, but the food chain is a major route. Biomagnification means that each trophic level concentrates the plastic load from the level below, and humans at the top inherit the highest concentrations."
        },
        {
            "question": "Approximately how much plastic does the average person ingest per week according to recent research estimates?",
            "choices": {
                "A": "A barely detectable amount with no health significance",
                "B": "About the weight of a credit card (approximately 5 grams)",
                "C": "Several kilograms of plastic per week",
                "D": "Exactly zero, because food safety regulations prevent any plastic from entering food"
            },
            "correct": "B",
            "feedback_correct": "Correct. Research estimates suggest the average person ingests approximately 5 grams of microplastic per week, roughly equivalent to the weight of a credit card, through food, water, and air.",
            "feedback_incorrect": "Studies estimate approximately 5 grams per week, the equivalent of a credit card. This plastic comes from seafood, drinking water, food packaging, and airborne particles, and the long-term health effects are still being studied."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The simulation projects microplastic concentration 50 years forward under current input rates with near-zero decomposition. The model shows concentration increasing linearly, not exponentially. What does this linear pattern reveal about the accumulation dynamics?",
            "choices": {
                "A": "The linear pattern means the problem is not serious",
                "B": "Unlike systems with reinforcing feedback, microplastic accumulation is driven by constant input against near-zero removal, creating steady linear growth rather than accelerating growth",
                "C": "The concentration should decrease over time as organisms filter plastics from the environment",
                "D": "Linear growth indicates the model is incorrect"
            },
            "correct": "B",
            "feedback_correct": "Correct. Microplastic accumulation is a stock-flow problem: constant input with negligible output produces linear growth. There is no reinforcing feedback accelerating the input, but the absence of any meaningful removal mechanism means concentrations rise relentlessly.",
            "feedback_incorrect": "The linear pattern reflects the stock-flow dynamics: a constant input rate combined with near-zero decomposition creates steady accumulation. While not exponential, linear growth of a persistent pollutant over decades produces massive cumulative concentrations."
        },
        {
            "question": "A student's model tracks microplastic concentration through four trophic levels: water, plankton, small fish, and tuna. The concentration increases by roughly 10x at each level. What mechanism drives this amplification?",
            "choices": {
                "A": "Each organism manufactures new plastic internally",
                "B": "Each predator consumes many prey organisms, inheriting and concentrating the accumulated plastic from all of them, while excreting very little",
                "C": "Higher trophic levels are exposed to different, more concentrated sources of plastic",
                "D": "The amplification is an artifact of the model and does not occur in real food chains"
            },
            "correct": "B",
            "feedback_correct": "Correct. Biomagnification occurs because each predator consumes many prey items, inheriting the plastic load from each one. Since plastic is not metabolized or excreted efficiently, it accumulates in the predator at the combined concentration of all its prey.",
            "feedback_incorrect": "The 10x amplification at each level reflects biomagnification. A tuna eats hundreds of small fish, each of which ate thousands of plankton. The plastic from every organism consumed accumulates in the predator because plastic resists metabolic breakdown."
        },
        {
            "question": "The model shows that reducing plastic input by 50% today causes ocean concentrations to continue rising (just more slowly) rather than declining. What does this reveal about the timescale mismatch in this system?",
            "choices": {
                "A": "Reducing plastic input is pointless because concentrations will keep rising regardless",
                "B": "Even with reduced input, the existing stock of persistent plastic continues to accumulate because decomposition is negligible; the system has enormous inertia due to the timescale mismatch between input (years) and decomposition (centuries)",
                "C": "The model shows that concentrations should drop immediately after reducing input",
                "D": "The 50% reduction was not enough to matter"
            },
            "correct": "B",
            "feedback_correct": "Correct. The timescale mismatch is the core problem. Plastic enters the system in years but takes centuries to degrade. Even halving input means new plastic continues to add to the existing stock, which barely decomposes. Concentrations only stabilize when input equals the negligible decomposition rate.",
            "feedback_incorrect": "The system has massive inertia because existing plastic persists for centuries. Reducing input slows the rate of increase but cannot reverse it quickly because the decomposition timescale (hundreds of years) vastly exceeds the input timescale (ongoing annual additions)."
        },
        {
            "question": "Based on the model, which intervention point in the plastic pathway would produce the greatest reduction in human microplastic exposure?",
            "choices": {
                "A": "Removing microplastics from individual fish before consumption",
                "B": "Reducing plastic input at the source before it enters the environment, because it prevents accumulation at every subsequent stage of the pathway",
                "C": "Developing bacteria that can eat plastic in the deep ocean",
                "D": "Filtering microplastics from the air inside homes"
            },
            "correct": "B",
            "feedback_correct": "Correct. Source reduction is the highest-leverage intervention because it prevents plastic from entering the accumulation pathway at all. Every unit of plastic prevented at the source avoids amplification through bioaccumulation and biomagnification at every subsequent trophic level.",
            "feedback_incorrect": "The model shows that plastic amplifies at each stage of the pathway. Preventing one unit of plastic at the source prevents its amplified presence at every subsequent level. End-of-chain interventions (filtering fish, cleaning air) cannot match the leverage of source prevention."
        },
        {
            "question": "A student argues that 'the plastic problem will eventually solve itself because organisms will evolve to digest plastic.' Based on the model's timescale analysis, what is the flaw in this reasoning?",
            "choices": {
                "A": "The reasoning is correct; evolution will solve the problem within a few decades",
                "B": "Evolutionary adaptation operates on timescales of thousands to millions of years, while microplastic accumulation is causing measurable ecological harm on timescales of decades, creating a dangerous mismatch",
                "C": "Some organisms already efficiently digest plastic, so the problem is already being solved",
                "D": "Evolution cannot act on plastic because plastic is not a biological substance"
            },
            "correct": "B",
            "feedback_correct": "Correct. The timescale mismatch is critical. Even if plastic-digesting enzymes evolve (some primitive examples exist), the evolutionary timescale is vastly longer than the decades over which accumulation is causing ecological damage. Relying on evolution means accepting centuries of harm.",
            "feedback_incorrect": "While evolution could theoretically produce plastic-digesting organisms, this process operates on timescales far longer than the rapid accumulation of microplastics. The ecological damage occurring now and in coming decades cannot wait for an evolutionary solution that may take millennia."
        }
    ]
}

L10_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "What is grid intermittency, and why is it a challenge for renewable energy?",
            "choices": {
                "A": "Intermittency means renewable energy costs fluctuate with market demand",
                "B": "Intermittency means solar and wind energy production varies with weather and time of day, making supply unpredictable and sometimes unavailable when demand is highest",
                "C": "Intermittency refers to planned maintenance shutdowns of power plants",
                "D": "Intermittency only affects hydroelectric power, not solar or wind"
            },
            "correct": "B",
            "feedback_correct": "Correct. Solar output drops to zero at night and varies with cloud cover. Wind output depends on weather patterns. This intermittency means renewable supply cannot be controlled to match demand, unlike fossil fuel plants that generate power on command.",
            "feedback_incorrect": "Intermittency is the fundamental challenge of renewable energy. Unlike fossil fuel plants that generate power whenever needed, solar and wind produce electricity only when nature cooperates, creating gaps between supply and demand."
        },
        {
            "question": "Why is energy storage considered essential for a renewable energy grid?",
            "choices": {
                "A": "Storage is not necessary because renewable energy is always available when needed",
                "B": "Storage captures excess renewable energy during high-production periods and releases it during low-production periods, bridging the intermittency gap",
                "C": "Storage is only needed for fossil fuel power plants",
                "D": "Storage makes renewable energy more expensive without any benefit"
            },
            "correct": "B",
            "feedback_correct": "Correct. Energy storage acts as a buffer between variable renewable supply and relatively constant demand. Batteries charge when solar/wind produce excess and discharge when production drops, smoothing out the intermittency.",
            "feedback_incorrect": "Storage is the bridge between when renewables produce energy and when consumers need it. Without storage, excess daytime solar power is wasted, and nighttime demand must be met by other sources."
        },
        {
            "question": "What is 'grid balancing' and why does it become more complex with high renewable penetration?",
            "choices": {
                "A": "Grid balancing means distributing power plants evenly across a geographic area",
                "B": "Grid balancing is the continuous process of matching electricity supply to demand in real time, which becomes harder when a large portion of supply is variable and weather-dependent",
                "C": "Grid balancing is only necessary during extreme weather events",
                "D": "Grid balancing refers to equalizing electricity prices across regions"
            },
            "correct": "B",
            "feedback_correct": "Correct. Electricity supply must match demand every second. With dispatchable fossil fuel plants, operators control output. With intermittent renewables, supply depends on weather, making the balancing act more complex and requiring storage and backup systems.",
            "feedback_incorrect": "Grid balancing is the real-time matching of supply and demand. When supply is weather-dependent (solar, wind), operators cannot simply increase production on demand, requiring sophisticated forecasting, storage, and backup generation."
        },
        {
            "question": "What is a 'dispatchable' energy source, and why is it important?",
            "choices": {
                "A": "A dispatchable source is one that can be delivered to remote locations",
                "B": "A dispatchable source can be turned on and off on demand to meet grid needs, unlike solar and wind which produce power only when conditions allow",
                "C": "All energy sources are dispatchable if enough capacity is built",
                "D": "Dispatchable refers to the speed at which electricity travels through power lines"
            },
            "correct": "B",
            "feedback_correct": "Correct. Dispatchable sources (natural gas, hydroelectric, nuclear) can increase or decrease output on command. This controllability is essential for filling gaps when renewable output drops, maintaining grid stability.",
            "feedback_incorrect": "Dispatchability means the ability to generate electricity on demand. Natural gas plants can ramp up in minutes to fill gaps when clouds cover solar panels or wind dies down. Solar and wind cannot increase output on command."
        },
        {
            "question": "Why is transitioning from 80% to 100% renewable energy considered much harder than going from 0% to 80%?",
            "choices": {
                "A": "The technology for 100% renewable energy does not exist yet",
                "B": "The last 20% requires covering worst-case intermittency scenarios (multi-day periods of low sun AND low wind), which demands massive storage or overbuilding capacity at enormous cost",
                "C": "It is equally difficult at every stage of the transition",
                "D": "Political opposition increases proportionally with renewable percentage"
            },
            "correct": "B",
            "feedback_correct": "Correct. At 80% renewable, fossil backup handles occasional gaps. At 100%, every gap must be covered by storage or excess renewable capacity. Multi-day weather events (cloudy calm periods) require enormous storage that is currently prohibitively expensive.",
            "feedback_incorrect": "The difficulty curve is exponential, not linear. The first 80% replaces baseload fossil fuel during periods when renewables produce plenty. The last 20% requires bridging worst-case multi-day intermittency gaps, demanding storage capacity that grows exponentially with the reliability requirement."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that during a sunny, windy day, renewable output exceeds demand by 40%. What happens to this excess energy in a grid with adequate battery storage versus one without?",
            "choices": {
                "A": "Excess energy is the same problem in both scenarios",
                "B": "With adequate storage, excess energy charges batteries for later use during low-production periods; without storage, the excess is curtailed (wasted) because the grid cannot absorb more power than demand requires",
                "C": "Excess renewable energy automatically increases demand to match supply",
                "D": "The grid shuts down when supply exceeds demand regardless of storage"
            },
            "correct": "B",
            "feedback_correct": "Correct. Storage converts a waste problem into an asset. Without batteries, excess renewable generation must be curtailed (dumped) because the grid requires constant supply-demand balance. With storage, that energy is captured for later use.",
            "feedback_incorrect": "Battery storage is the key differentiator. Excess energy that cannot be stored must be curtailed, representing a waste of generation capacity. Storage captures this surplus and makes it available during low-production periods."
        },
        {
            "question": "A simulation of a calm winter night shows battery storage depleting in 6 hours, after which fossil fuel backup activates to meet demand. What does this reveal about the current limitations of battery storage?",
            "choices": {
                "A": "Batteries are useless for renewable energy systems",
                "B": "Current battery capacity can bridge short intermittency gaps (hours) but cannot economically cover extended periods of low renewable production, making some backup generation necessary",
                "C": "The simulation proves that 100% renewable energy is impossible",
                "D": "Battery technology has no room for improvement"
            },
            "correct": "B",
            "feedback_correct": "Correct. Current battery technology effectively handles short gaps (hours) but the cost of storing enough energy for multi-day events (calm cloudy periods) is prohibitive. This is why backup generation remains necessary at high renewable penetration levels.",
            "feedback_incorrect": "The simulation reveals a duration limitation, not a fundamental failure. Batteries handle hourly fluctuations well but cannot economically bridge multi-day intermittency events. This gap is where backup generation or alternative long-duration storage technologies are needed."
        },
        {
            "question": "The model allows students to optimize energy mix across three competing objectives: minimize cost, minimize emissions, and maximize reliability. What does the optimization reveal?",
            "choices": {
                "A": "There is a single optimal solution that simultaneously minimizes cost, emissions, and maximizes reliability",
                "B": "The three objectives create trade-offs where improving one metric often worsens another, requiring stakeholders to decide which priorities matter most",
                "C": "Cost and emissions always improve together with no trade-off",
                "D": "Reliability is independent of the energy mix chosen"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is a multi-objective optimization problem with inherent trade-offs. Maximum renewable (lowest emissions) costs more and may reduce reliability. Maximum reliability requires backup fossil fuel (higher emissions). There is no single solution that maximizes all three.",
            "feedback_incorrect": "Real engineering involves trade-offs. Minimizing emissions (more renewables) increases cost and may reduce reliability. Maximizing reliability (more backup) increases emissions. The optimization surface reveals that stakeholders must prioritize which objectives matter most."
        },
        {
            "question": "A student's model shows that connecting two geographically distant regions (one solar-rich, one wind-rich) reduces the probability of system-wide intermittency by 60%. What principle does this demonstrate?",
            "choices": {
                "A": "Geographic diversity has no effect on grid reliability",
                "B": "Geographic diversity reduces correlated intermittency because weather patterns affecting solar and wind in one region are often independent of patterns in another, making simultaneous low production less likely",
                "C": "Connecting distant regions doubles the total energy production",
                "D": "Long-distance transmission has no energy losses"
            },
            "correct": "B",
            "feedback_correct": "Correct. Geographic diversity exploits the fact that weather is a local phenomenon. When one region has clouds (low solar), another may have sun. When one area is calm (low wind), another may be windy. Connecting diverse regions reduces the probability that all sources fail simultaneously.",
            "feedback_incorrect": "Geographic diversity is a powerful strategy because it reduces the correlation between renewable output at different locations. The sun is not cloudy everywhere at once, and the wind does not stop everywhere simultaneously, so connecting diverse regions smooths out variability."
        },
        {
            "question": "Based on the complete model analysis, why does the transition to 100% clean energy require systems thinking rather than simply building more solar panels and wind turbines?",
            "choices": {
                "A": "Because solar panels and wind turbines are inherently unreliable technologies",
                "B": "Because the grid is an interconnected system where generation, storage, transmission, demand, and backup must be balanced simultaneously, and optimizing one component without considering the others creates new problems",
                "C": "Because renewable energy is more expensive than fossil fuels in all scenarios",
                "D": "Because building more renewable capacity always solves the intermittency problem"
            },
            "correct": "B",
            "feedback_correct": "Correct. The grid is a coupled system. Adding solar without storage creates curtailment waste. Adding storage without grid interconnection limits geographic diversity benefits. Removing backup without adequate storage risks blackouts. Every component interacts, requiring integrated systems thinking.",
            "feedback_incorrect": "The energy grid is a complex system where every component affects every other. Overbuilding renewables creates curtailment. Insufficient storage causes reliability gaps. Removing backup prematurely risks blackouts. Only systems thinking that considers all interactions simultaneously can design an effective transition."
        }
    ]
}

ALL_QUESTIONS = {
    "G09L2-L01": L01_QUESTIONS,
    "G09L2-L02": L02_QUESTIONS,
    "G09L2-L03": L03_QUESTIONS,
    "G09L2-L04": L04_QUESTIONS,
    "G09L2-L05": L05_QUESTIONS,
    "G09L2-L06": L06_QUESTIONS,
    "G09L2-L07": L07_QUESTIONS,
    "G09L2-L08": L08_QUESTIONS,
    "G09L2-L09": L09_QUESTIONS,
    "G09L2-L10": L10_QUESTIONS,
}
