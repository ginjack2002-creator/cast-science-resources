#!/usr/bin/env python3
"""Multiple choice pre/post assessment questions for Grade 10 Level 3 ModelIt! Lessons
Advanced Engineering & Design — CAST-aligned, HS NGSS standards"""

L01_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A Mars habitat relies on solar panels for energy and a closed-loop system for water recycling. If a dust storm reduces solar output by 50%, which outcome is most likely based on systems engineering principles?",
            "choices": {
                "A": "Only the lighting system is affected because other systems have independent power sources",
                "B": "Water recycling, temperature regulation, and food production all degrade because they depend on the shared energy supply",
                "C": "The habitat automatically switches to backup wind power from Martian winds",
                "D": "Crew psychological well-being improves because dust storms reduce outside radiation exposure"
            },
            "correct": "B",
            "feedback_correct": "Correct. In an interdependent system, energy generation is the keystone variable. When it degrades, all downstream systems that require power — water recycling, temperature regulation, food production lighting — are affected in a cascading failure.",
            "feedback_incorrect": "Consider that most habitat systems require continuous electrical power. When the primary energy source degrades, any system dependent on that power will also degrade. This is the principle of cascading failure in interdependent systems."
        },
        {
            "question": "Why is systems redundancy considered essential in Mars habitat engineering but less critical for buildings on Earth?",
            "choices": {
                "A": "Mars habitats use more advanced technology that breaks down more frequently",
                "B": "Earth buildings never experience system failures",
                "C": "On Mars, there is no possibility of rapid resupply or external rescue, so a single-point failure could be fatal",
                "D": "Redundancy is equally important on Earth but is never implemented due to cost"
            },
            "correct": "C",
            "feedback_correct": "Correct. The nearest help is 225 million km away with a 6-9 month transit time. Unlike Earth, where emergency services, replacement parts, and evacuation are available, Mars demands built-in redundancy because there is no external backup.",
            "feedback_incorrect": "Think about what makes Mars fundamentally different from Earth as an engineering environment. The key factor is isolation — the inability to receive help, parts, or rescue in a timely manner."
        },
        {
            "question": "In-situ resource utilization (ISRU) on Mars involves extracting oxygen from atmospheric CO2. Which scientific principle best explains why this is preferable to transporting oxygen from Earth?",
            "choices": {
                "A": "Martian oxygen is chemically purer than Earth-produced oxygen",
                "B": "The energy cost of launching mass from Earth's gravity well makes local resource harvesting far more economical",
                "C": "Oxygen cannot survive the radiation environment during the transit from Earth to Mars",
                "D": "Earth does not have sufficient oxygen reserves to supply a Mars colony"
            },
            "correct": "B",
            "feedback_correct": "Correct. Launching mass from Earth costs approximately $10,000-$50,000 per kilogram. Extracting resources locally eliminates launch mass costs, making ISRU essential for long-term sustainability despite the energy required for extraction.",
            "feedback_incorrect": "Consider the economics and physics of space travel. Moving mass from Earth's surface to Mars requires overcoming Earth's gravitational pull with enormous amounts of rocket fuel, making every kilogram extremely expensive."
        },
        {
            "question": "A habitat engineer argues that psychological well-being should be deprioritized during a crisis because it is not a physical survival system. What is the strongest scientific counterargument?",
            "choices": {
                "A": "Psychological well-being has no measurable effect on physical systems",
                "B": "Degraded mental health directly impairs crew decision-making, maintenance quality, and conflict resolution — creating feedback loops that worsen the crisis",
                "C": "Crew members can simply be ordered to maintain good morale during emergencies",
                "D": "Psychological monitoring equipment uses too much energy during power shortages"
            },
            "correct": "B",
            "feedback_correct": "Correct. Psychological well-being is a survival variable, not a luxury. Research from ISS missions and Antarctic isolation studies shows that degraded mental health leads to poor decisions, maintenance errors, and interpersonal conflict — all of which can compound a physical crisis.",
            "feedback_incorrect": "Consider how human performance under stress affects every other system. If crew members are making poor decisions due to psychological deterioration, every system they maintain or manage is at greater risk."
        },
        {
            "question": "Which engineering design philosophy is most appropriate for a Mars habitat that must survive unpredictable equipment failures?",
            "choices": {
                "A": "Design for maximum efficiency so every component operates at peak capacity with no wasted resources",
                "B": "Design for graceful degradation so the habitat can operate at reduced capacity rather than failing completely",
                "C": "Design for minimum mass to reduce launch costs, even if it means eliminating backup systems",
                "D": "Design for rapid replacement so failed components can be swapped out within hours"
            },
            "correct": "B",
            "feedback_correct": "Correct. Graceful degradation means the habitat continues functioning at reduced capacity during failures rather than experiencing catastrophic collapse. This approach keeps the crew alive while repairs are made, unlike binary success/failure designs.",
            "feedback_incorrect": "Think about what happens when a system fails on Mars. The best engineering approach is one where failure of a component reduces performance but does not cause total system collapse."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's computational model shows that reducing Energy Generation by 40% causes Atmosphere Control to drop to critical levels within 2 days, but Food Production does not reach critical levels for 30 days. What does this difference reveal about crisis management priorities?",
            "choices": {
                "A": "Food Production is not important during a crisis",
                "B": "Atmosphere Control has a shorter time-to-critical because breathable air cannot be stored in large quantities, while food reserves provide a buffer",
                "C": "The model must contain an error because all systems should fail at the same rate",
                "D": "Energy Generation does not actually affect Atmosphere Control"
            },
            "correct": "B",
            "feedback_correct": "Correct. Different systems have different buffer capacities. Atmosphere composition changes within hours to days without active management, while stored food can sustain crew for weeks. This time-to-critical difference directly informs triage priorities during energy crises.",
            "feedback_incorrect": "Consider that different systems have different reserves or buffers. A system with large stored reserves (food) can tolerate power loss longer than a system requiring continuous operation (air composition management)."
        },
        {
            "question": "In the Mars habitat model, Energy Generation is classified as an external (input) variable while Temperature Regulation is classified as internal. What is the best justification for this distinction?",
            "choices": {
                "A": "External variables are always more important than internal variables",
                "B": "Energy Generation represents a resource that engineers directly control, while Temperature Regulation is a system response that depends on energy availability and environmental conditions",
                "C": "Internal variables cannot be measured, only estimated",
                "D": "The classification is arbitrary and could be reversed without affecting the model"
            },
            "correct": "B",
            "feedback_correct": "Correct. In computational modeling, external (input) variables represent quantities that operators set or control directly. Internal variables emerge from the interactions between inputs and system dynamics. Energy Generation is set by the power system design; Temperature Regulation responds to available energy and Mars surface conditions.",
            "feedback_incorrect": "Think about the difference between variables you directly set (inputs you control) and variables that result from the system's behavior (outputs that emerge from interactions)."
        },
        {
            "question": "The model predicts that during a 45-day dust storm, crew psychological well-being degrades, which causes maintenance quality to decline, which causes additional system failures. This pattern is best described as:",
            "choices": {
                "A": "A linear cause-and-effect chain with no feedback",
                "B": "A positive feedback loop where declining well-being and system failures reinforce each other",
                "C": "A negative feedback loop that stabilizes the system at a lower performance level",
                "D": "An artifact of the model that would not occur in a real habitat"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is a positive (amplifying) feedback loop: psychological stress reduces maintenance quality, which causes more system failures, which increases stress further. Without intervention, the loop spirals toward increasingly dangerous conditions.",
            "feedback_incorrect": "Consider the direction of the cycle: does each step make the next step better or worse? When worsening conditions cause further worsening in a circular pattern, that is a specific type of feedback loop."
        },
        {
            "question": "A team redesigns the habitat to use nuclear power instead of solar as the primary energy source. According to the model's systems logic, which prediction is best supported?",
            "choices": {
                "A": "All other variables remain unchanged because only the energy source is different",
                "B": "The dust storm crisis scenario becomes far less severe because nuclear power is unaffected by atmospheric dust, eliminating the primary trigger for cascading failures",
                "C": "Nuclear power eliminates the need for systems redundancy entirely",
                "D": "Psychological well-being automatically improves because nuclear energy is more powerful"
            },
            "correct": "B",
            "feedback_correct": "Correct. The dust storm crisis in the model is triggered by reduced solar energy generation. Nuclear power operates independently of atmospheric conditions, so the primary cascade trigger is eliminated. However, nuclear introduces different risks (radiation, mechanical failure) that would need to be modeled separately.",
            "feedback_incorrect": "Consider what specifically triggers the cascading failure in the dust storm scenario. If the energy source is not affected by dust, does the same cascade occur?"
        },
        {
            "question": "A model limitation is that it uses nine components to represent a habitat that would actually contain hundreds of subsystems. How does this simplification most likely affect the model's predictions?",
            "choices": {
                "A": "The model cannot provide any useful predictions because it is too simplified",
                "B": "The model accurately captures overall system behavior and cascade dynamics but may miss specific failure modes or unexpected interactions between subsystems not represented",
                "C": "Simplification makes the model more accurate because complexity introduces errors",
                "D": "The model overestimates system resilience because it includes too many redundant components"
            },
            "correct": "B",
            "feedback_correct": "Correct. Model simplification is a standard scientific practice that captures essential dynamics while sacrificing detail. The nine-component model reveals fundamental interdependencies and cascade patterns but cannot predict every specific failure pathway that hundreds of subsystems might produce.",
            "feedback_incorrect": "Think about the purpose of modeling. All models are simplifications of reality. The question is whether the simplification preserves the important dynamics (cascade effects, interdependencies) even if it misses specific details."
        }
    ]
}

L02_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Nuclear fusion combines light atomic nuclei to form heavier ones. What is the fundamental physical difference between fusion and fission that makes fusion potentially cleaner?",
            "choices": {
                "A": "Fusion uses renewable fuel while fission uses non-renewable fuel",
                "B": "Fusion produces helium and neutrons with no long-lived radioactive actinides, while fission produces heavy radioactive isotopes that remain dangerous for thousands of years",
                "C": "Fusion reactions produce no radiation of any kind",
                "D": "Fission requires higher temperatures than fusion"
            },
            "correct": "B",
            "feedback_correct": "Correct. Fusion of deuterium and tritium produces helium-4 and a neutron. While fusion-activated structural materials are radioactive for 50-100 years, fission produces actinides like plutonium-239 (half-life 24,000 years) that remain hazardous for hundreds of thousands of years.",
            "feedback_incorrect": "Compare the products of each reaction. Fission splits heavy nuclei into lighter but still radioactive fragments. Fusion combines light nuclei into helium. Consider which products are more problematic long-term."
        },
        {
            "question": "Fusion fuel (plasma) must reach 150 million degrees Celsius, yet the superconducting magnets confining it must operate near -250 degrees Celsius. What engineering challenge does this extreme temperature contrast create?",
            "choices": {
                "A": "The magnets melt from the plasma heat, requiring frequent replacement",
                "B": "Thermal management systems must maintain a 150-million-degree temperature gradient across just a few meters while preventing any heat transfer between systems",
                "C": "The cold magnets extinguish the plasma through heat absorption",
                "D": "No engineering challenge exists because vacuum insulation perfectly separates the two"
            },
            "correct": "B",
            "feedback_correct": "Correct. Maintaining the most extreme temperature gradient engineered by humans — from 150 million degrees Celsius to nearly absolute zero across a few meters — requires extraordinary thermal isolation, cryogenic cooling systems, and radiation shielding, all operating simultaneously and continuously.",
            "feedback_incorrect": "Consider the practical challenge of having the hottest and nearly the coldest temperatures on Earth within meters of each other inside the same machine. Heat naturally flows from hot to cold, and preventing that flow is an enormous engineering task."
        },
        {
            "question": "The Lawson criterion states that fusion requires the simultaneous achievement of sufficient temperature, density, and confinement time. Why can these requirements not be met one at a time?",
            "choices": {
                "A": "Each parameter is independent and can be optimized separately",
                "B": "The fusion reaction rate depends on the product of all three — if any one is too low, the reaction rate drops below the threshold for net energy regardless of the others",
                "C": "Scientists have not tried optimizing them separately yet",
                "D": "The Lawson criterion is a theoretical concept that does not apply to real reactors"
            },
            "correct": "B",
            "feedback_correct": "Correct. The Lawson criterion is expressed as the triple product n*T*tau, where all three must simultaneously exceed a threshold. Extremely high temperature with low density or short confinement time yields insufficient fusion reactions for net energy gain.",
            "feedback_incorrect": "The Lawson criterion is a product (multiplication) of three variables. What happens to a product when one factor is very small, even if the others are very large?"
        },
        {
            "question": "Every deuterium-tritium fusion reaction produces both 17.6 MeV of energy and a 14.1 MeV neutron. Why does this create a fundamental engineering tension?",
            "choices": {
                "A": "The neutron carries away energy that could otherwise be used for electricity",
                "B": "Neutrons are impossible to detect so engineers cannot track them",
                "C": "Each energy-producing reaction simultaneously damages the reactor structure through neutron bombardment, coupling energy output with material degradation",
                "D": "Neutrons trigger additional unwanted fusion reactions in the reactor walls"
            },
            "correct": "C",
            "feedback_correct": "Correct. This is the cruel paradox of fusion: the same nuclear reaction that produces useful energy also produces a high-energy neutron that damages reactor walls. More energy output means more material damage, creating a direct trade-off between power production and reactor lifespan.",
            "feedback_incorrect": "Consider that the neutron from each reaction does not simply disappear — it escapes the magnetic confinement (neutrons are uncharged) and strikes the reactor wall materials at extremely high velocity."
        },
        {
            "question": "Magnetic confinement fusion uses powerful magnets to suspend plasma away from reactor walls. What would happen if the magnetic field weakened by 20% during operation?",
            "choices": {
                "A": "The fusion reaction would become 20% more efficient due to lower energy consumption by magnets",
                "B": "The plasma would expand, contact the reactor walls, cool instantly, and fusion would stop while potentially damaging wall materials",
                "C": "Nothing would change because the plasma is self-confining at fusion temperatures",
                "D": "The weakened field would cause a nuclear explosion similar to a hydrogen bomb"
            },
            "correct": "B",
            "feedback_correct": "Correct. Magnetic confinement creates a magnetic bottle that prevents 150-million-degree plasma from touching physical walls. If the field weakens, the plasma drifts outward, contacts the wall, and cools in milliseconds — stopping fusion and potentially melting or eroding wall materials. No explosion occurs because fusion requires extreme conditions to sustain.",
            "feedback_incorrect": "Remember that no physical material can survive contact with 150-million-degree plasma. The magnetic field is the only barrier keeping the plasma suspended. What happens when that barrier weakens?"
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the computational model, a student increases Plasma Temperature to maximum while keeping Magnetic Containment at moderate levels. The model shows Energy Output initially rising but then Net Energy Gain declining. What best explains this result?",
            "choices": {
                "A": "The model has a calculation error at high temperatures",
                "B": "Higher temperatures increase fusion reactions but also increase plasma instability, requiring more energy for containment and cooling — eventually the energy consumed exceeds the additional energy produced",
                "C": "Plasma Temperature has no effect on Net Energy Gain in the model",
                "D": "Net Energy Gain always increases with temperature because more fusion reactions always mean more net energy"
            },
            "correct": "B",
            "feedback_correct": "Correct. This reveals the optimization challenge in fusion: pushing temperature higher increases fusion output but also increases the energy cost of containment, cooling, and managing instabilities. Net energy gain is maximized at a specific operating point, not at maximum temperature.",
            "feedback_incorrect": "Consider that Energy Output and Net Energy Gain are different variables. Net Energy Gain subtracts all input energy (heating, magnets, cooling) from output energy. What happens to input costs as temperature increases?"
        },
        {
            "question": "The model shows three relationships: Plasma Temperature positively affects Energy Output, Energy Output positively affects Neutron Damage, and Neutron Damage positively affects Materials Degradation. What type of systemic pattern does this represent?",
            "choices": {
                "A": "A negative feedback loop that stabilizes the system",
                "B": "An independent chain with no systemic implications",
                "C": "A feedforward cascade where the desired output (energy) inevitably drives the undesired output (degradation) through a linked chain",
                "D": "A random correlation with no causal mechanism"
            },
            "correct": "C",
            "feedback_correct": "Correct. This is a feedforward cascade — a causal chain where increasing the input to get more desired output automatically increases undesired consequences downstream. In fusion, you cannot increase energy production without increasing neutron-induced material damage.",
            "feedback_incorrect": "Trace the causal chain: higher temperature causes more energy output, which causes more neutrons, which causes more material damage. Is this cycle self-correcting (negative feedback) or does it represent a one-directional cascade?"
        },
        {
            "question": "ITER is designed to achieve Q=10, meaning it produces 10 times more fusion energy than the heating energy input. Why is Q=10 a more meaningful milestone than Q=1?",
            "choices": {
                "A": "Q=1 was already achieved by NIF in 2022, so it is no longer important",
                "B": "Q=10 provides enough surplus energy to power the reactor's own magnets, cooling, and support systems while still delivering net electricity — Q=1 produces only enough to equal its heating input with nothing left over",
                "C": "Q=10 means the reactor runs 10 times longer than Q=1",
                "D": "There is no practical difference between Q=1 and Q=10"
            },
            "correct": "B",
            "feedback_correct": "Correct. Q measures only fusion energy output versus heating energy input. But a reactor also needs energy for magnets, cooling, tritium breeding, and facility operations. Q=1 means fusion output equals heating input — there is nothing left for everything else. Q=10 provides sufficient surplus to cover all auxiliary systems and deliver net electricity.",
            "feedback_incorrect": "Consider that Q only compares fusion energy to heating energy. A reactor has many other energy-consuming systems (magnets, cooling, control systems). How much surplus is needed to cover all of those AND deliver useful electricity?"
        },
        {
            "question": "A student claims that discovering a material immune to neutron damage would solve all remaining fusion challenges. Using the model, which response best evaluates this claim?",
            "choices": {
                "A": "The claim is correct — material damage is the only barrier to commercial fusion",
                "B": "The claim is partially correct — it would remove the materials degradation constraint but plasma confinement instability, tritium supply, and net energy optimization remain independent challenges",
                "C": "The claim is incorrect — materials play no significant role in the fusion challenge",
                "D": "The claim is correct because neutron damage is the only variable connected to all other variables in the model"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that materials degradation is ONE of several major constraints. Solving it would be transformative — allowing longer reactor lifetimes and higher operating parameters. But plasma instabilities, tritium breeding sufficiency, and the overall energy balance remain challenges that materials alone do not address.",
            "feedback_incorrect": "Look at all the variables in the model. Materials Degradation is connected to reactor lifetime, but are there other variables (plasma stability, fuel supply, energy balance) that represent independent challenges?"
        },
        {
            "question": "The model uses nine components to represent a fusion reactor system. A critic argues that a real tokamak has thousands of interacting subsystems. What is the most scientifically valid defense of the simplified model?",
            "choices": {
                "A": "Nine components are enough to capture every detail of a real fusion reactor",
                "B": "The model captures the essential trade-offs and coupling dynamics (output-damage, temperature-confinement-time) that govern system behavior, even though individual subsystem interactions are abstracted",
                "C": "More complex models always produce worse predictions",
                "D": "The critic is wrong because fusion reactors are simple enough to model with nine variables"
            },
            "correct": "B",
            "feedback_correct": "Correct. Scientific models are deliberately simplified to reveal essential dynamics. The nine-component model captures the fundamental trade-offs — energy output coupled with material damage, temperature requirements versus confinement stability — that determine system behavior at the highest level, even though it cannot predict every subsystem interaction.",
            "feedback_incorrect": "Consider the purpose of a model in science. Models are not meant to be perfect replicas of reality. They are simplifications that highlight the most important relationships. What essential dynamics does this model successfully capture?"
        }
    ]
}

L03_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A classical computer with 3 bits can represent one of 8 possible states at any time. A quantum computer with 3 qubits in superposition can represent how many states simultaneously?",
            "choices": {
                "A": "3 states (one per qubit)",
                "B": "6 states (twice the classical number)",
                "C": "8 states (all possible combinations at once through superposition)",
                "D": "24 states (3 factorial times the classical number)"
            },
            "correct": "C",
            "feedback_correct": "Correct. N qubits in superposition can represent all 2^N states simultaneously. With 3 qubits, that is 2^3 = 8 states explored in parallel. This exponential scaling is the source of quantum computing's potential power — 300 qubits represent more states than atoms in the observable universe.",
            "feedback_incorrect": "A qubit in superposition exists in a combination of 0 and 1 simultaneously. With N qubits, the system can represent all 2^N combinations at once. Calculate 2^3."
        },
        {
            "question": "Quantum computers must be cooled to approximately 15 millikelvin (colder than outer space). What is the primary scientific reason for this extreme cooling?",
            "choices": {
                "A": "Superconducting circuits only work at low temperatures to reduce electrical resistance",
                "B": "Thermal energy causes random interactions with qubits that destroy quantum superposition (decoherence), and cooling minimizes these interactions",
                "C": "Cold temperatures make qubits process information faster",
                "D": "The cooling system generates the magnetic fields needed to control qubits"
            },
            "correct": "B",
            "feedback_correct": "Correct. Thermal energy produces photons and phonons that interact with qubits, causing decoherence — the collapse of quantum superposition into classical states. At 15 millikelvin, thermal noise is minimized, extending the time qubits maintain their quantum properties.",
            "feedback_incorrect": "Consider what temperature represents at the atomic level — the kinetic energy and vibration of particles. How would energetic particles in the environment interact with a fragile quantum state?"
        },
        {
            "question": "A quantum computer has a per-gate error rate of 0.5%. After a circuit of 200 sequential gate operations, what is the approximate probability that NO errors have occurred?",
            "choices": {
                "A": "99.5% (almost certain success)",
                "B": "99.0% (very high success)",
                "C": "Approximately 37% (0.995^200), meaning the majority of runs will contain at least one error",
                "D": "0.5% (almost certain failure)"
            },
            "correct": "C",
            "feedback_correct": "Correct. Error probabilities compound multiplicatively across sequential operations. (1 - 0.005)^200 = 0.995^200 is approximately 0.37, meaning only about 37% of runs will be error-free after just 200 gates. This is why error correction is essential for any useful quantum computation.",
            "feedback_incorrect": "Error rates compound across sequential operations. If each gate has a 99.5% chance of being correct, the probability of ALL 200 gates being correct is 0.995 multiplied by itself 200 times. Calculate this compound probability."
        },
        {
            "question": "Entanglement links two qubits so that measuring one instantly determines the state of the other. Why is this property essential for quantum computing rather than merely a curiosity?",
            "choices": {
                "A": "Entanglement allows qubits to communicate faster than light, speeding up the computer",
                "B": "Entanglement creates correlations between qubits that enable quantum algorithms to coordinate operations across many qubits simultaneously, which is necessary for quantum speedup",
                "C": "Entanglement doubles the number of qubits available for computation",
                "D": "Entanglement is not actually used in quantum computing algorithms"
            },
            "correct": "B",
            "feedback_correct": "Correct. Entanglement allows quantum algorithms to create correlated multi-qubit states that cannot be represented classically. These correlations enable interference patterns where correct answers are amplified and wrong answers are suppressed — the fundamental mechanism of quantum speedup.",
            "feedback_incorrect": "Think about what entanglement provides that classical bits cannot achieve. Classical bits are independent. Entangled qubits are correlated in ways that allow quantum algorithms to process information fundamentally differently."
        },
        {
            "question": "If quantum computers are potentially millions of times faster than classical computers for certain problems, why are they not used for everyday computing tasks like email and web browsing?",
            "choices": {
                "A": "Quantum computers are too expensive for consumer use but would be faster at everything",
                "B": "Quantum advantage is problem-specific — quantum algorithms exist only for certain problem types (cryptography, molecular simulation, optimization), and classical computers are already optimal for most everyday tasks",
                "C": "Quantum computers are banned from consumer applications by government regulation",
                "D": "Quantum computers will replace classical computers completely within 5 years"
            },
            "correct": "B",
            "feedback_correct": "Correct. Quantum advantage emerges only for specific problem classes where quantum algorithms exploit superposition and entanglement. For sequential tasks like word processing or video streaming, quantum computers offer no speedup. They are complementary tools, not replacements.",
            "feedback_incorrect": "Consider whether every type of computation benefits from quantum parallelism. Some problems have inherent sequential structure that quantum mechanics cannot accelerate."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the model, a student reduces Cooling Temperature from 15 millikelvin to 100 millikelvin. The model shows Decoherence Rate increasing dramatically, Qubit Coherence Time dropping, and Computational Advantage falling to near zero. Which relationship chain best explains this cascade?",
            "choices": {
                "A": "Higher temperature increases thermal noise, which accelerates decoherence, which shortens the time window for computation, which prevents completion of useful quantum circuits",
                "B": "Higher temperature directly destroys the qubits physically, requiring replacement",
                "C": "The model incorrectly links temperature to computational performance",
                "D": "Cooling temperature only affects energy consumption, not computation quality"
            },
            "correct": "A",
            "feedback_correct": "Correct. The model reveals a clear causal cascade: temperature increase leads to more thermal photons/phonons, which interact with qubits faster (higher decoherence rate), which shortens coherence time, which limits circuit depth, which eliminates computational advantage. Each link is a direct physical mechanism.",
            "feedback_incorrect": "Trace the chain: temperature affects the environment around the qubits. How does a noisier environment affect quantum states? How does that affect the time available for computation?"
        },
        {
            "question": "The model shows that reducing Error Rate from 0.5% to 0.01% causes a dramatic nonlinear increase in Quantum Volume and Computational Advantage. What best explains this threshold behavior?",
            "choices": {
                "A": "The relationship between error rate and performance is always linear, so the dramatic change must be a model error",
                "B": "Below a critical error threshold, error correction becomes efficient enough that correction gains outpace errors introduced by the correction process itself, unlocking exponentially deeper circuits",
                "C": "Lower error rates allow the computer to run at higher clock speeds",
                "D": "The improvement is due to needing fewer physical qubits, not related to error rates"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is the fault-tolerance threshold. Above it, error correction consumes more resources than it saves. Below it, correction gains exceed correction costs, creating a virtuous cycle where logical qubit quality improves with more physical qubits. This threshold behavior is a fundamental feature of quantum error correction.",
            "feedback_incorrect": "Consider the error correction paradox: correction itself uses quantum operations that can introduce errors. At what point does the correction process start winning against the errors it introduces?"
        },
        {
            "question": "A 1,000 physical qubit processor uses a surface code requiring 1,000 physical qubits per logical qubit at current error rates. How many error-corrected logical qubits are available for actual computation?",
            "choices": {
                "A": "1,000 logical qubits (each physical qubit becomes one logical qubit)",
                "B": "500 logical qubits (half for error correction, half for computation)",
                "C": "Approximately 1 logical qubit, with all remaining physical qubits dedicated to error correction",
                "D": "Zero logical qubits because 1,000 is below the minimum threshold"
            },
            "correct": "C",
            "feedback_correct": "Correct. At a 1,000:1 overhead ratio, 1,000 physical qubits yield approximately 1 error-corrected logical qubit. This reveals why current quantum computers are called NISQ (Noisy Intermediate-Scale Quantum) — they lack enough physical qubits for meaningful error correction. Millions of physical qubits are needed for thousands of logical qubits.",
            "feedback_incorrect": "Divide the total physical qubits by the overhead ratio (physical qubits per logical qubit). At a 1,000:1 ratio, how many logical qubits can 1,000 physical qubits produce?"
        },
        {
            "question": "The model classifies Cooling Temperature and Classical Overhead as external variables. A student proposes reclassifying Qubit Coherence Time as external. What is the strongest argument against this reclassification?",
            "choices": {
                "A": "External variables must always represent temperature or energy",
                "B": "Qubit Coherence Time is determined by the interaction between cooling temperature, material quality, and electromagnetic shielding — it is an emergent property of multiple factors, not a directly set parameter",
                "C": "Models cannot have more than two external variables",
                "D": "Coherence Time is too difficult to measure to be classified as anything"
            },
            "correct": "B",
            "feedback_correct": "Correct. External variables represent direct engineering inputs that operators set. Qubit Coherence Time emerges from the combination of cooling temperature, material properties, shielding quality, and other physical factors. It cannot be directly dialed to a value — it is a consequence of other conditions.",
            "feedback_incorrect": "Ask whether engineers can directly set Qubit Coherence Time with a dial or switch, or whether it emerges as a result of other controllable conditions. External variables are direct inputs; internal variables are system responses."
        },
        {
            "question": "Based on model evidence, a student concludes that quantum computing will never be practical because current error rates are too high. Using the model's scenario comparisons, what is the best evaluation of this conclusion?",
            "choices": {
                "A": "The conclusion is correct — the model proves quantum computing is impossible",
                "B": "The conclusion extrapolates current limitations into permanent barriers, ignoring the model's near-perfect qubits scenario that shows dramatic improvement with achievable error rate reductions",
                "C": "The conclusion is correct because the model shows no path from current to near-perfect qubits",
                "D": "Error rates are irrelevant to quantum computing practicality"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows two distinct regimes: current technology (limited advantage) and near-perfect qubits (transformative advantage). The gap between them is large but represents an engineering challenge, not a physical impossibility. Extrapolating current limitations as permanent ignores historical patterns of technology improvement.",
            "feedback_incorrect": "Compare the model's current technology scenario with the near-perfect qubits scenario. Does the model suggest the current state is a permanent condition, or does it show what becomes possible with achievable improvements?"
        }
    ]
}

L04_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A direct air capture facility removes 10,000 tons of CO2 per year but is powered by natural gas that emits 4,000 tons of CO2. What is the facility's net CO2 removal, and what does this reveal about the importance of energy source?",
            "choices": {
                "A": "Net removal is 10,000 tons because emissions from power generation are counted separately",
                "B": "Net removal is 6,000 tons, demonstrating that the energy source directly determines the actual climate benefit",
                "C": "Net removal is 14,000 tons because the facility also captures its own emissions",
                "D": "Net removal cannot be calculated without knowing the carbon credit price"
            },
            "correct": "B",
            "feedback_correct": "Correct. Net removal = gross capture minus process emissions = 10,000 - 4,000 = 6,000 tons. The energy source reduces the climate benefit by 40%. If powered by coal, emissions could exceed capture, making the facility a net climate harm. This is the energy-emissions paradox.",
            "feedback_incorrect": "Calculate: if the facility removes 10,000 tons from the atmosphere but the energy source adds 4,000 tons back, what is the net effect on atmospheric CO2?"
        },
        {
            "question": "Global CO2 emissions exceed 36 billion tons per year. The world's largest direct air capture facility removes 4,000 tons per year. How many facilities of this size would be needed to capture just 1% of annual emissions?",
            "choices": {
                "A": "360 facilities",
                "B": "3,600 facilities",
                "C": "90,000 facilities",
                "D": "900,000 facilities"
            },
            "correct": "C",
            "feedback_correct": "Correct. 1% of 36 billion tons = 360 million tons. At 4,000 tons per facility, that requires 360,000,000 / 4,000 = 90,000 facilities. This scale comparison demonstrates why carbon capture alone cannot substitute for emission reduction.",
            "feedback_incorrect": "Calculate step by step: 1% of 36 billion = 360 million tons. Then divide by the capacity of one facility (4,000 tons/year)."
        },
        {
            "question": "A sorbent material captures CO2 from ambient air at 420 parts per million. Why does the low concentration of CO2 in the atmosphere make direct air capture inherently more challenging than capturing CO2 from a power plant exhaust?",
            "choices": {
                "A": "Atmospheric CO2 is chemically different from power plant CO2",
                "B": "At 420 ppm, CO2 constitutes only 0.042% of the air, meaning enormous volumes of air must be processed to capture significant quantities — power plant exhaust is 10-15% CO2, a concentration 250-350 times higher",
                "C": "Low concentration makes no difference because the same sorbent works at any concentration",
                "D": "Direct air capture is actually easier because atmospheric air is cleaner than power plant exhaust"
            },
            "correct": "B",
            "feedback_correct": "Correct. Thermodynamic and practical constraints make capturing dilute CO2 far more energy-intensive and expensive than capturing concentrated CO2. Processing air at 420 ppm requires 250-350 times more air volume than capturing from power plant exhaust at 10-15% concentration.",
            "feedback_incorrect": "Think about what happens when you try to capture a substance that makes up only 0.042% of a gas mixture. How much gas must you process to collect a significant amount of that substance?"
        },
        {
            "question": "Geological sequestration involves injecting captured CO2 into deep underground rock formations. What is the primary scientific basis for expecting this storage to be permanent?",
            "choices": {
                "A": "The CO2 is compressed into a solid that cannot escape",
                "B": "CO2 dissolves in brine, reacts with minerals, and eventually converts to carbonate rock — processes that trap it permanently, as demonstrated by natural CO2 reservoirs that have held gas for millions of years",
                "C": "Underground formations are sealed with cement caps that prevent any leakage",
                "D": "The CO2 naturally decomposes underground within a few years"
            },
            "correct": "B",
            "feedback_correct": "Correct. Multiple trapping mechanisms ensure permanence: structural trapping (impermeable cap rock), dissolution in brine, chemical reaction with minerals to form carbonates, and capillary trapping. Natural analogs prove these mechanisms hold CO2 for geological timescales.",
            "feedback_incorrect": "Consider the natural geological processes that trap CO2 underground. Some natural formations have held CO2 for over 100,000 years. What physical and chemical mechanisms make this possible?"
        },
        {
            "question": "Carbon credits create a financial incentive for CO2 removal. At a current price range of $100-$1,000 per ton and a capture cost of $400-$1,000 per ton, what does this suggest about the economic viability of direct air capture without additional policy support?",
            "choices": {
                "A": "DAC is already highly profitable at all credit prices",
                "B": "DAC is economically marginal — only viable when credit prices are at the high end of the range and capture costs are at the low end, suggesting that policy incentives or technology cost reductions are needed for widespread deployment",
                "C": "Credit prices are irrelevant because governments fund all capture operations directly",
                "D": "The economics prove that DAC should be abandoned in favor of tree planting exclusively"
            },
            "correct": "B",
            "feedback_correct": "Correct. When costs overlap with or exceed credit prices, the operation is only viable under favorable conditions. Widespread deployment requires either credit prices rising sustainably above $200/ton, technology improvements reducing costs below $200/ton, or both — alongside supportive policies.",
            "feedback_incorrect": "Compare the cost range ($400-$1,000/ton) with the credit price range ($100-$1,000/ton). Under what conditions does revenue exceed cost? How often does that occur across the ranges?"
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that switching from fossil-powered to renewable-powered energy input increases net CO2 removal from 6,000 to 10,000 tons per year for the same facility. What variable in the model changes to produce this result?",
            "choices": {
                "A": "Capture Rate increases because renewable energy is more powerful",
                "B": "The gross capture remains the same, but the process emissions drop to near zero, so net removal equals gross capture",
                "C": "Carbon Credit Value increases when the facility uses renewables",
                "D": "Sorbent Efficiency improves when powered by renewable energy"
            },
            "correct": "B",
            "feedback_correct": "Correct. The facility's capture technology performs the same regardless of energy source. What changes is the emissions from energy generation: fossil fuel produces CO2 that offsets capture, while renewables produce zero operational CO2. Net removal = gross capture minus process emissions.",
            "feedback_incorrect": "Identify what specifically changes when you switch the energy source. Does the capture technology itself change, or does something about the process emissions change?"
        },
        {
            "question": "A student's model predicts that scaling capture from 4,000 tons/year to 1 billion tons/year would require energy equivalent to 1% of global energy production. What does this reveal about the scale challenge?",
            "choices": {
                "A": "1% of global energy is trivial and easily allocated to carbon capture",
                "B": "The energy requirement demonstrates that climate-scale capture competes with other critical energy demands and requires massive expansion of clean energy infrastructure specifically dedicated to capture",
                "C": "The energy calculation proves carbon capture is physically impossible",
                "D": "The model overestimates energy requirements by a factor of 100"
            },
            "correct": "B",
            "feedback_correct": "Correct. Dedicating 1% of global energy to carbon capture is a massive infrastructure investment — equivalent to the entire energy output of a major industrial nation. This energy must come from clean sources (or the capture is self-defeating), requiring purpose-built renewable capacity beyond what is needed to decarbonize existing energy demand.",
            "feedback_incorrect": "Consider what 1% of global energy production represents in absolute terms. Is this a trivial amount, or does it represent a significant industrial undertaking? And what must be true about the source of that energy?"
        },
        {
            "question": "In the model, CO2 Concentration is classified as an external variable even though it changes with global emissions over time. What is the best justification for this classification?",
            "choices": {
                "A": "External variables never change in any model",
                "B": "From the perspective of a single capture facility, atmospheric CO2 concentration is an environmental condition that the facility encounters but cannot meaningfully alter — it is set by global-scale processes beyond the facility's control",
                "C": "CO2 concentration is the easiest variable to measure, so it must be external",
                "D": "The classification is arbitrary and has no scientific basis"
            },
            "correct": "B",
            "feedback_correct": "Correct. External variables represent conditions that affect the modeled system but are not significantly changed by it. A single capture facility removing 4,000 tons from an atmosphere containing 3.3 trillion tons has negligible effect on global concentration — it is a boundary condition, not a dependent variable.",
            "feedback_incorrect": "Consider the scale difference between what one facility captures and total atmospheric CO2. Can one facility meaningfully change the atmospheric concentration? If not, the concentration is an external condition, not a system output."
        },
        {
            "question": "The model includes both Sorbent Efficiency and Regeneration Cost as separate variables. A student argues they should be combined into one variable. What is the strongest argument for keeping them separate?",
            "choices": {
                "A": "Combining variables always makes models less accurate",
                "B": "They respond to different physical factors: Sorbent Efficiency is determined by chemistry and contact time, while Regeneration Cost depends on thermal energy prices, sorbent cycle life, and maintenance — they can change independently based on different innovations",
                "C": "They are already combined in real carbon capture facilities",
                "D": "The model needs a minimum number of variables to be valid"
            },
            "correct": "B",
            "feedback_correct": "Correct. A breakthrough in sorbent chemistry (higher CO2 affinity) could increase Sorbent Efficiency without changing Regeneration Cost. Conversely, cheaper renewable heat could reduce Regeneration Cost without affecting Sorbent Efficiency. Keeping them separate reveals which innovations most impact overall economic viability.",
            "feedback_incorrect": "Consider whether improvements in one area necessarily improve the other. Could you improve how well the sorbent captures CO2 without changing how much it costs to regenerate it, or vice versa?"
        },
        {
            "question": "Based on the model's three scenarios, a student concludes that carbon capture should be deployed only after all fossil fuel emissions are eliminated. Using model evidence, what is the strongest counterargument?",
            "choices": {
                "A": "There is no counterargument — the student is correct that capture should wait",
                "B": "Some emission sources (aviation, cement, steel) cannot be fully eliminated with current technology, and the 1.5 trillion tons of legacy CO2 already in the atmosphere will continue causing warming even if all new emissions stop — capture is needed for both residual and legacy emissions",
                "C": "Carbon capture is cheaper than emission reduction in all sectors",
                "D": "The model does not address this question"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that capture and emission reduction serve different functions. Emission reduction prevents new CO2 from entering the atmosphere. Capture addresses hard-to-abate sectors (where elimination is technically impossible) and removes legacy CO2 that will otherwise cause warming for centuries. Both are necessary simultaneously.",
            "feedback_incorrect": "Consider whether all emission sources can be eliminated. Some industrial processes (cement production, steel manufacturing, long-haul aviation) inherently produce CO2. Also consider the CO2 already in the atmosphere from past emissions."
        }
    ]
}

L05_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Two identical buildings experience the same earthquake. Building A is rigidly connected to its foundation. Building B sits on flexible rubber-steel bearings (base isolation). Which building experiences greater floor acceleration, and why?",
            "choices": {
                "A": "Building B, because the flexible bearings amplify ground motion like a trampoline",
                "B": "Building A, because the rigid connection transmits 100% of ground acceleration directly to the structure, while base isolation decouples the building from ground motion",
                "C": "Both experience identical acceleration because they have the same mass",
                "D": "Neither experiences significant acceleration because modern buildings are earthquake-proof"
            },
            "correct": "B",
            "feedback_correct": "Correct. Base isolation works by decoupling the building from ground motion. The flexible bearings absorb and spread seismic energy over a longer period, reducing the peak acceleration transmitted to the structure by 50-80%. The rigid building transmits every ground acceleration directly.",
            "feedback_incorrect": "Consider what happens when you shake a table with a cup glued to it versus a cup sitting on a rubber pad. Which cup experiences more force from the shaking?"
        },
        {
            "question": "In the 1985 Mexico City earthquake, buildings of 8-15 stories collapsed while shorter and taller buildings survived. What physical phenomenon best explains this selective destruction?",
            "choices": {
                "A": "Buildings of 8-15 stories were built with weaker materials",
                "B": "The earthquake's dominant wave frequency matched the natural oscillation period of 8-15 story buildings, causing resonance amplification that multiplied forces by 5-10 times",
                "C": "Only 8-15 story buildings were occupied at the time of the earthquake",
                "D": "Taller buildings have deeper foundations that protected them from ground motion"
            },
            "correct": "B",
            "feedback_correct": "Correct. Resonance occurs when external forcing frequency matches a structure's natural frequency. Medium-rise buildings (8-15 stories) have natural periods of approximately 1-2 seconds, which matched the 2-second dominant period of the Mexico City earthquake. This amplified ground motion 5-10 times, causing selective destruction.",
            "feedback_incorrect": "Consider why ONLY buildings of a certain height range were destroyed. What physical property changes with building height, and how could matching with earthquake characteristics cause amplified damage?"
        },
        {
            "question": "A tuned mass damper is a heavy pendulum mounted near the top of a skyscraper. During an earthquake, the damper swings opposite to the building's motion. What physical principle explains how this reduces damage?",
            "choices": {
                "A": "The damper's weight prevents the building from moving at all",
                "B": "The damper absorbs kinetic energy from the building's oscillation and converts it to heat through friction, reducing the amplitude of building motion by 30-50%",
                "C": "The damper pushes the building back to vertical using stored gravitational energy",
                "D": "The damper is primarily decorative and has minimal structural benefit"
            },
            "correct": "B",
            "feedback_correct": "Correct. The tuned mass damper acts as an energy sink. When the building sways right, the damper swings left, absorbing kinetic energy through friction and viscous resistance. This energy is converted to heat rather than continuing to build up in the structure. Taipei 101's 730-ton damper reduces sway by approximately 40%.",
            "feedback_incorrect": "Think about energy conservation: the earthquake pumps kinetic energy into the building. Where does that energy go? The damper provides a mechanism to remove energy from the building's oscillation."
        },
        {
            "question": "Newton's second law states F = ma. During an earthquake, a 200,000-ton skyscraper experiences a floor acceleration of 0.5g. What is the approximate lateral force on the structure?",
            "choices": {
                "A": "100,000 newtons",
                "B": "1 million newtons (1 MN)",
                "C": "Approximately 980 million newtons (980 MN) — almost 1 billion newtons",
                "D": "The force cannot be calculated without knowing the building height"
            },
            "correct": "C",
            "feedback_correct": "Correct. F = ma = 200,000,000 kg x 0.5 x 9.8 m/s^2 = 980,000,000 N = 980 MN. This enormous force — nearly 1 billion newtons — demonstrates why seismic engineering focuses on reducing acceleration (through base isolation and damping) rather than just strengthening structures.",
            "feedback_incorrect": "Apply F = ma directly. Convert 200,000 metric tons to kilograms (multiply by 1,000,000). Multiply by 0.5g (where g = 9.8 m/s^2)."
        },
        {
            "question": "Modern earthquake engineering designs buildings for 'life safety' rather than 'zero damage.' What engineering principle justifies this approach?",
            "choices": {
                "A": "Engineers do not know how to build damage-free structures",
                "B": "Designing for zero damage in the maximum credible earthquake would be prohibitively expensive, so buildings are designed to sustain controlled structural damage that protects occupants while potentially sacrificing the building itself",
                "C": "All earthquake damage can be repaired after the event, so prevention is unnecessary",
                "D": "Life safety and zero damage require the same engineering approach"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is performance-based design: the building absorbs seismic energy through planned damage in designated structural members (like sacrificial fuses) while maintaining enough integrity for safe evacuation. The building may be demolished afterward, but no one dies. This philosophy optimizes cost versus safety.",
            "feedback_incorrect": "Consider the cost-benefit analysis. Designing for the absolute worst-case earthquake with zero damage would require enormous structural capacity. Is it more practical to accept some damage while ensuring the building does not collapse?"
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows Building A (natural period 3.0 seconds) in an earthquake with a dominant period of 3.1 seconds. Building B (natural period 1.2 seconds) is in the same earthquake. The model predicts Building A's Damage Index is 5 times higher. What variable drives this difference?",
            "choices": {
                "A": "Building A is taller and therefore always more vulnerable",
                "B": "Resonance Frequency — Building A's natural period nearly matches the earthquake's dominant period, causing resonance amplification of forces, while Building B is far from resonance",
                "C": "Building B has stronger materials based on its shorter natural period",
                "D": "The earthquake hits Building B with less intensity because it is shorter"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that resonance is the primary determinant of damage, not building height or material strength. Building A's 3.0-second period nearly matches the earthquake's 3.1-second period, causing amplification. Building B's 1.2-second period is far from resonance, so it experiences the earthquake at its actual intensity.",
            "feedback_incorrect": "Look at the relationship between each building's natural period and the earthquake's dominant period. When do forces amplify? When the frequencies are close to matching, or when they are far apart?"
        },
        {
            "question": "In the model, a student increases Material Strength by 50% while keeping all other variables the same, including resonance risk. The Damage Index decreases by only 10%. What does this disproportionate response reveal?",
            "choices": {
                "A": "Material Strength is incorrectly modeled and should have more impact",
                "B": "The model is broken because stronger materials should always dramatically reduce damage",
                "C": "When resonance amplifies forces by 5-10 times, a 50% increase in material strength is overwhelmed — addressing resonance avoidance (through flexibility or isolation) is more effective than adding strength",
                "D": "Material Strength has no relationship to Damage Index in the model"
            },
            "correct": "C",
            "feedback_correct": "Correct. This is a key model insight: strength alone cannot overcome resonance amplification. If an earthquake at resonance multiplies forces by 5-10x, a 50% stronger structure still fails under those amplified forces. The model shows that avoiding resonance (through base isolation or period-shifting) reduces damage far more effectively than adding strength.",
            "feedback_incorrect": "Consider the magnitude of resonance amplification (5-10x) versus the material improvement (1.5x). If forces are multiplied by 7 through resonance, does making the structure 1.5 times stronger prevent failure?"
        },
        {
            "question": "The model classifies Seismic Wave Intensity and Foundation Flexibility as external variables. A student argues that Building Mass should also be external because it is set during design. What is the best evaluation of this argument?",
            "choices": {
                "A": "The argument is correct — Building Mass is a design choice and should be external",
                "B": "While Building Mass is determined during design, in the model's context it is treated as a system property that interacts with seismic forces through F=ma — it is a characteristic of the system being analyzed, not a condition imposed on it",
                "C": "Building Mass cannot be classified as either external or internal",
                "D": "The classification makes no difference to model behavior"
            },
            "correct": "B",
            "feedback_correct": "Correct. The distinction is nuanced: external variables represent conditions that the system encounters (earthquake intensity, foundation engineering choice). Building Mass, while determined during design, is a property of the system itself — it interacts with acceleration to produce force (F=ma) and with natural period to determine resonance risk. The model treats it as a system characteristic.",
            "feedback_incorrect": "Consider the difference between conditions the building encounters (earthquake characteristics, foundation type) and properties of the building itself. The model analyzes how the building system responds to seismic conditions."
        },
        {
            "question": "The model's moderate earthquake scenario (0.3g) with base isolation shows a Damage Index near zero, while the same earthquake at resonance (without isolation) shows a Damage Index near 0.8. Both scenarios have identical earthquake intensity. What does this comparison demonstrate about seismic design?",
            "choices": {
                "A": "Base isolation makes buildings completely indestructible",
                "B": "The comparison demonstrates that resonance avoidance and energy decoupling are more important than earthquake intensity alone — the same earthquake can be harmless or catastrophic depending on the structural design",
                "C": "The 0.3g earthquake is too weak to damage any building, so the comparison is meaningless",
                "D": "Damage Index is not a reliable metric for comparing seismic scenarios"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is the model's most powerful finding: the same earthquake produces radically different outcomes based solely on structural design. Base isolation prevents resonance and decouples the building from ground motion. Without it, resonance amplifies the same moderate earthquake to destructive levels. Design, not earthquake size, determines survival.",
            "feedback_incorrect": "Compare the two scenarios: same earthquake intensity, same building, but dramatically different outcomes. What is the only difference between them? What does that tell you about what determines building survival?"
        },
        {
            "question": "After running all three scenarios, a student concludes that base isolation alone is sufficient seismic protection for any building. Using model evidence, what is the strongest limitation of this conclusion?",
            "choices": {
                "A": "Base isolation is too expensive to be practical",
                "B": "The maximum credible earthquake scenario (1.5g near-fault) shows that even base-isolated buildings experience significant forces — a multi-layered defense (isolation + dampers + flexible design) is needed for extreme events because no single strategy handles all scenarios",
                "C": "Base isolation only works for buildings under 10 stories",
                "D": "The model does not include a base isolation variable"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model's three scenarios reveal that base isolation handles moderate earthquakes excellently but has limits under extreme near-fault ground motion. The maximum credible earthquake scenario demonstrates that combined strategies — isolation, structural flexibility, and energy-dissipating dampers — are needed for comprehensive protection.",
            "feedback_incorrect": "Look at the maximum credible earthquake scenario results. Does base isolation alone reduce the Damage Index to near zero in that extreme case, or does the building still experience significant forces?"
        }
    ]
}

L06_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A self-driving car uses LIDAR, cameras, and radar simultaneously. Why is this multi-sensor approach (sensor fusion) more reliable than using any single sensor?",
            "choices": {
                "A": "More sensors make the car look more advanced and increase consumer confidence",
                "B": "Each sensor type excels in different conditions and detects different properties — LIDAR provides 3D mapping, cameras provide color and sign recognition, radar works in all weather — so combining them creates redundancy where one sensor's weakness is covered by another's strength",
                "C": "Using three sensors makes the car exactly three times safer",
                "D": "Single sensors are never used in any vehicle application"
            },
            "correct": "B",
            "feedback_correct": "Correct. Sensor fusion combines complementary strengths: LIDAR provides precise 3D spatial mapping but fails in rain, cameras provide color/texture for classification but struggle in fog, and radar measures velocity and penetrates weather but lacks spatial detail. Together, they create a perception model more robust than any single source.",
            "feedback_incorrect": "Consider what each sensor type is good at and what it struggles with. LIDAR fires lasers, cameras capture visible light, and radar uses radio waves. Each interacts with the environment differently."
        },
        {
            "question": "An autonomous vehicle's decision latency is 200 milliseconds, while a human driver's reaction time is approximately 1,500 milliseconds. At 60 mph (27 m/s), how much additional stopping distance does the human driver need compared to the autonomous system?",
            "choices": {
                "A": "Approximately 5 meters (negligible difference)",
                "B": "Approximately 15 meters (the human needs about 35 meters of reaction distance versus the car's 5.4 meters)",
                "C": "Approximately 35 meters (the human needs about 40 meters versus 5.4 meters)",
                "D": "The difference depends on the type of obstacle, not the reaction time"
            },
            "correct": "C",
            "feedback_correct": "Correct. Human reaction distance = 27 m/s x 1.5 s = 40.5 m. AV reaction distance = 27 m/s x 0.2 s = 5.4 m. The difference is approximately 35 meters — enough to determine whether a collision occurs. This demonstrates the reaction time advantage of autonomous systems.",
            "feedback_incorrect": "Calculate distance = speed x time for both reaction times. At 27 m/s, how far does the vehicle travel during 1.5 seconds (human) versus 0.2 seconds (autonomous)?"
        },
        {
            "question": "An autonomous vehicle encounters an object it cannot classify with high confidence — a deflated mylar balloon in the road. This situation is called an 'edge case.' Why are edge cases particularly dangerous for autonomous systems?",
            "choices": {
                "A": "Edge cases cause the sensors to malfunction permanently",
                "B": "The system's machine learning models were trained on common scenarios and may misclassify novel objects — stopping for a harmless balloon wastes time, but driving over an object misidentified as harmless could be fatal",
                "C": "Edge cases only occur in bad weather, so they are easily avoided",
                "D": "Human drivers also cannot handle edge cases, so it is not a unique autonomous vehicle problem"
            },
            "correct": "B",
            "feedback_correct": "Correct. Edge cases expose the fundamental limitation of pattern-matching AI: it excels at recognizing common objects from training data but struggles with novel situations. Humans use general intelligence and common sense to assess unknown objects; autonomous systems must choose between stopping (safe but potentially disruptive) or proceeding (efficient but potentially dangerous).",
            "feedback_incorrect": "Consider how the system decides what to do with an object. It compares what it sees to patterns it learned during training. What happens when the object does not match any learned pattern?"
        },
        {
            "question": "During heavy rain, a self-driving car's LIDAR loses 60% of its effectiveness because laser pulses scatter off water droplets. Which alternative sensor is LEAST affected by rain and could compensate?",
            "choices": {
                "A": "Additional LIDAR units mounted at different angles",
                "B": "High-resolution cameras, which also use visible light affected by rain",
                "C": "Radar, which uses radio waves that penetrate rain, fog, and snow with minimal degradation",
                "D": "Ultrasonic sensors, which have sufficient range to replace LIDAR"
            },
            "correct": "C",
            "feedback_correct": "Correct. Radar uses radio waves (centimeter wavelengths) that pass through rain droplets with minimal scattering, unlike LIDAR (near-infrared, micrometer wavelengths) and cameras (visible light) which are significantly degraded. This is why sensor fusion is essential — radar provides reliable distance and velocity data when other sensors fail.",
            "feedback_incorrect": "Consider the wavelength of each sensor's emissions relative to the size of rain droplets. Longer wavelengths pass through small obstacles more easily than shorter wavelengths."
        },
        {
            "question": "An autonomous vehicle maintains a safety margin — a buffer distance beyond the minimum required for safe braking. Increasing this margin makes the car safer but has a trade-off. What is the primary trade-off?",
            "choices": {
                "A": "Larger safety margins require more fuel, increasing emissions",
                "B": "Larger margins cause the car to brake earlier, drive slower, and create gaps in traffic flow — reducing efficiency and potentially frustrating other drivers who may drive unpredictably in response",
                "C": "Larger margins increase the risk of rear-end collisions from following vehicles",
                "D": "There is no trade-off — larger safety margins are always better in every way"
            },
            "correct": "B",
            "feedback_correct": "Correct. The safety margin trade-off is both an engineering and societal question. Overly conservative driving reduces throughput, increases congestion, and may cause human drivers to behave aggressively around the autonomous vehicle. Finding the optimal margin balances individual safety against traffic flow and social integration.",
            "feedback_incorrect": "Think about what happens when a car maintains very large following distances and brakes much earlier than necessary. How does this affect the overall traffic system and other drivers?"
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that in heavy rain, LIDAR performance drops 60%, camera drops 40%, but radar drops only 10%. Despite these individual degradations, Sensor Fusion Accuracy drops by only 25%. What system property explains this resilience?",
            "choices": {
                "A": "The model underestimates the impact of rain on sensor performance",
                "B": "Sensor fusion creates redundancy — the algorithm dynamically reweights sensors, relying more heavily on radar when LIDAR and cameras are degraded, maintaining combined accuracy above any single degraded sensor",
                "C": "The 25% drop is unacceptable and means the system should shut down immediately",
                "D": "Rain does not actually affect autonomous vehicle performance in real systems"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates the core value of sensor fusion: when individual sensors degrade at different rates due to environmental conditions, the fusion algorithm shifts weighting toward the most reliable sensor. This built-in redundancy maintains system-level performance above any single sensor's degraded level.",
            "feedback_incorrect": "Consider what happens when the fusion algorithm knows that LIDAR and cameras are less reliable in rain. Can it adjust how much it trusts each sensor's data? What sensor remains reliable?"
        },
        {
            "question": "In the edge case scenario, the model shows Obstacle Classification confidence dropping below 50% for a novel object. The system responds by expanding Safety Margin and reducing speed. What decision-making principle does this represent?",
            "choices": {
                "A": "The system is malfunctioning because confidence should always be above 90%",
                "B": "Conservative fallback — when uncertainty is high, the system increases caution by trading efficiency for safety, buying more time to classify the object or allowing the human to take control",
                "C": "The system ignores unclassified objects to maintain traffic flow",
                "D": "Speed reduction is the only response the system has to any anomaly"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates a fundamental safety principle: when the perception system has low confidence, the decision system compensates by increasing safety margins. This buys time for additional sensor data, allows the object to be observed from closer range, and provides the option for human takeover.",
            "feedback_incorrect": "Think about what a cautious human driver would do when encountering something unexpected on the road. Would they speed up, maintain speed, or slow down? Why?"
        },
        {
            "question": "The model classifies LIDAR Pulse Frequency and Weather Interference as external variables. Why is Weather Interference classified as external even though it directly affects sensor performance?",
            "choices": {
                "A": "External variables must always be environmental conditions",
                "B": "Weather Interference is a condition the autonomous system encounters but cannot control or change — it is an input from the environment, not a property of the engineering system being modeled",
                "C": "Weather interference is too unpredictable to be modeled as an internal variable",
                "D": "The classification is incorrect and should be changed"
            },
            "correct": "B",
            "feedback_correct": "Correct. External variables represent conditions imposed on the system from outside. The autonomous vehicle cannot change the weather — it can only respond to it. Weather Interference is an environmental input that affects system performance but is not controlled by the system.",
            "feedback_incorrect": "Ask: can the autonomous vehicle control the weather? If not, weather is an environmental condition the system must deal with, not a system property it can adjust."
        },
        {
            "question": "The model predicts that Decision Latency increases from 150 ms in clear conditions to 350 ms in the edge case scenario. What system interaction causes this increase?",
            "choices": {
                "A": "The processors slow down in unusual situations",
                "B": "Low Obstacle Classification confidence triggers additional processing cycles — the system runs more analysis algorithms, cross-references additional data sources, and may request human verification, all adding time before a decision is made",
                "C": "Decision Latency is constant and does not change between scenarios",
                "D": "The increase is caused by physical distance to the obstacle, not processing time"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals an important trade-off: when the system encounters an ambiguous object, it spends more time trying to classify it correctly before deciding on an action. This is the speed-accuracy trade-off — taking longer to decide increases accuracy but also increases the distance traveled before responding.",
            "feedback_incorrect": "Consider what the system does when it encounters an object it cannot quickly classify. Does it immediately decide, or does it run additional analysis to improve classification confidence?"
        },
        {
            "question": "A student argues that autonomous vehicles should not be deployed until they can handle 100% of edge cases correctly. Based on the model, what is the most scientifically valid evaluation of this standard?",
            "choices": {
                "A": "The standard is achievable within 5 years with current technology trajectories",
                "B": "The 100% standard is mathematically impossible — the set of possible edge cases is effectively infinite, and the model shows that the system's strength lies in safe fallback responses (slowing, stopping, human handoff) when it encounters situations beyond its classification ability",
                "C": "Edge cases are rare enough that they can be ignored",
                "D": "Human drivers handle 100% of edge cases correctly, so autonomous vehicles should too"
            },
            "correct": "B",
            "feedback_correct": "Correct. The real world presents an effectively infinite set of possible situations. No system — human or autonomous — handles all of them correctly. The model shows that the engineering solution is not perfect classification but safe degradation: when confidence is low, the system increases caution and can hand control to a human driver.",
            "feedback_incorrect": "Consider whether it is possible to train a system on every possible situation it might ever encounter. Also consider: do human drivers handle 100% of situations correctly? The relevant question is how the system responds when it encounters uncertainty."
        }
    ]
}

L07_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "The human immune system evolved to destroy foreign materials inside the body. Why does this present a fundamental challenge for artificial organ design?",
            "choices": {
                "A": "Artificial organs are too large for the immune system to attack",
                "B": "Every synthetic material triggers some degree of immune response, causing inflammation, fibrous encapsulation, and potential device failure — the very defense system that protects us also attacks the device meant to save us",
                "C": "The immune system only attacks bacteria and viruses, not synthetic materials",
                "D": "Immune rejection can be completely prevented with current medications"
            },
            "correct": "B",
            "feedback_correct": "Correct. The immune system evolved to attack anything it does not recognize as 'self.' Artificial materials are inherently foreign, triggering inflammatory cascades that can encapsulate the device in fibrous tissue, block blood supply, and cause chronic inflammation — the fundamental biocompatibility challenge.",
            "feedback_incorrect": "Consider what the immune system does when it detects something foreign inside the body. Does it distinguish between a harmful bacterium and a helpful medical device?"
        },
        {
            "question": "Surface chemistry modifications (like PEG coatings) are applied to implant surfaces to reduce immune recognition. Why is surface chemistry more important than the bulk material for determining biocompatibility?",
            "choices": {
                "A": "The bulk material is invisible to the immune system because it is inside the device",
                "B": "The body's first interaction is with the outermost nanometer-thick surface layer — proteins adsorb, cells attach, and immune cells probe this surface, making its molecular properties more important than the interior material for immune compatibility",
                "C": "Surface coatings make the implant physically stronger",
                "D": "Bulk materials have no effect on the body because they are inert"
            },
            "correct": "B",
            "feedback_correct": "Correct. Biological interactions occur at the interface — the outermost molecular layer. Within seconds of implantation, proteins from blood adsorb onto the surface, and their configuration (determined by surface chemistry) signals to immune cells whether the material is 'friend or foe.' The interior bulk material is never directly contacted by immune cells.",
            "feedback_incorrect": "Think about what the immune system actually contacts. Does it interact with the center of the implant or only with the outermost surface? What happens at that surface within seconds of implantation?"
        },
        {
            "question": "An artificial heart valve must survive approximately 40 million cycles per year (heartbeats) in a warm, corrosive biochemical environment. What engineering property is most critical for long-term survival?",
            "choices": {
                "A": "Maximum hardness to resist any deformation",
                "B": "Fatigue resistance — the ability to withstand tens of millions of loading cycles without developing micro-cracks that propagate to catastrophic failure under combined mechanical, thermal, and chemical stress",
                "C": "Minimum weight to reduce strain on surrounding tissue",
                "D": "Maximum flexibility to match the natural valve's motion exactly"
            },
            "correct": "B",
            "feedback_correct": "Correct. Fatigue failure from cyclic loading is the primary mechanical failure mode for cardiovascular implants. Each heartbeat applies stress, and over years, micro-cracks initiate and propagate through the material. The biochemical environment accelerates this through corrosion-assisted fatigue. This is why pyrolytic carbon is used for heart valves — its fatigue life exceeds 40 years of heartbeats.",
            "feedback_incorrect": "Consider the combination of stresses an artificial heart valve faces: tens of millions of repetitive loading cycles, warm (37 degrees C) saline environment, and biological molecules that can corrode materials. What property determines survival under these combined conditions?"
        },
        {
            "question": "An artificial kidney must filter blood to remove waste products while retaining essential proteins and cells. Why is this filtering function so difficult to replicate synthetically?",
            "choices": {
                "A": "Synthetic filters cannot separate molecules of different sizes",
                "B": "Natural kidneys perform complex active transport, selective reabsorption, and hormone production in addition to passive filtration — functions that require living cells and cannot be fully replicated by synthetic membranes alone",
                "C": "Artificial kidneys have already been perfected through dialysis machines",
                "D": "Blood is too viscous for any artificial filter to process"
            },
            "correct": "B",
            "feedback_correct": "Correct. Kidneys perform far more than passive filtration. They actively reabsorb 99% of filtered water and glucose, secrete hormones (erythropoietin, renin), regulate pH, and selectively transport molecules. Current dialysis replaces only basic filtration, which is why patients remain chronically ill. A true artificial kidney requires biological integration.",
            "feedback_incorrect": "Consider what natural kidneys do beyond simple filtering. Do they just remove waste, or do they also add things back, produce hormones, and make complex decisions about what to keep and what to discard?"
        },
        {
            "question": "Tissue integration — where the patient's own cells grow into the implant — is essential for long-term function. Why is achieving tissue integration particularly challenging?",
            "choices": {
                "A": "Human cells cannot attach to any synthetic material",
                "B": "Successful integration requires simultaneously promoting cell attachment and blood vessel growth while suppressing immune rejection — these goals often conflict because the immune response that attacks the device also prevents tissue from connecting to it",
                "C": "Tissue integration is easily achieved with any biocompatible material",
                "D": "Only bone tissue can integrate with implants; soft tissue integration is impossible"
            },
            "correct": "B",
            "feedback_correct": "Correct. Integration requires cell attachment, vascularization, and functional tissue formation — all of which are impaired by the inflammatory response to a foreign body. The immune system's fibrous encapsulation physically blocks blood vessels and tissue from reaching the implant surface, creating a fundamental conflict between biocompatibility and integration.",
            "feedback_incorrect": "Consider the immune response timeline: inflammation occurs first, forming a barrier around the implant. How does this barrier affect the ability of blood vessels and tissue cells to reach and integrate with the device surface?"
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that reducing Immune Response Rate from high to low increases Functional Lifespan from 2 years to 15+ years, even when Structural Durability remains unchanged. What does this reveal about the dominant failure mode?",
            "choices": {
                "A": "Structural failure is the primary cause of implant failure in all cases",
                "B": "Immune rejection drives the majority of implant failures — chronic inflammation degrades blood flow, blocks cell attachment, and creates fibrous barriers that impair function long before mechanical wear becomes critical",
                "C": "The model incorrectly overweights the immune response variable",
                "D": "Immune response has no effect on Functional Lifespan"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that for many implant types, immune rejection — not mechanical failure — is the life-limiting variable. Chronic inflammation creates fibrous capsules that block nutrient transport, prevent tissue integration, and progressively impair device function. Solving biocompatibility extends lifespan more than improving mechanical durability.",
            "feedback_incorrect": "Compare what changed (Immune Response Rate) with what stayed the same (Structural Durability) and what improved dramatically (Functional Lifespan). Which variable was controlling the lifespan?"
        },
        {
            "question": "In the model, Biocompatible Material and Molecular Surface Chemistry are both classified as external variables. A student argues that Immune Response Rate should also be external because doctors can prescribe immunosuppressive drugs. What is the best evaluation?",
            "choices": {
                "A": "The student is correct — any variable that can be influenced is external",
                "B": "Immune Response Rate emerges from the interaction between the material, its surface chemistry, and the patient's individual immune system — while drugs can modulate it, it is fundamentally a system response to the implant rather than a directly set parameter",
                "C": "Immune Response Rate cannot be measured, so it cannot be classified",
                "D": "Immunosuppressive drugs eliminate immune response entirely, making it irrelevant"
            },
            "correct": "B",
            "feedback_correct": "Correct. External variables are direct engineering inputs set before implantation. Immune Response Rate emerges from the interaction between the chosen material, its surface modification, and the patient's unique biology. While drugs can modulate this response, it remains a system output — the model correctly captures this distinction.",
            "feedback_incorrect": "Consider whether Immune Response Rate is directly controlled (like choosing a material) or whether it emerges from the interaction between the implant and the patient's biology. Can a doctor set the immune response to an exact value?"
        },
        {
            "question": "The model predicts that a pyrolytic carbon heart valve has excellent Structural Durability (30+ year fatigue life) but triggers moderate immune activation, while a new polymer valve has low immune response but only 8-year Structural Durability. Which model concept best describes this comparison?",
            "choices": {
                "A": "The polymer is always superior because immune response is more important",
                "B": "Functional Lifespan is limited by whichever variable fails first — the carbon valve's lifespan is limited by immune response, the polymer valve's by mechanical wear — demonstrating that different materials face different life-limiting constraints",
                "C": "Both materials will have identical Functional Lifespans",
                "D": "Material choice has no effect on Functional Lifespan in the model"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates the 'weakest link' principle: Functional Lifespan is determined by whichever variable reaches its failure threshold first. Each material trades strength in one area for weakness in another. The optimal material would excel in both, but no current material achieves that.",
            "feedback_incorrect": "Think about what limits each valve's lifespan. If one variable is excellent but another fails, which determines how long the device lasts? The device fails when ANY critical variable reaches its limit."
        },
        {
            "question": "The immune rejection cascade scenario shows the following chain: high Immune Response Rate reduces Blood Flow Integration, which reduces Nutrient Transport, which reduces Cell Attachment Rate, which reduces Functional Lifespan. What type of systemic pattern is this?",
            "choices": {
                "A": "A negative feedback loop that self-corrects",
                "B": "A feedforward degradation cascade where immune activation triggers sequential failures across multiple dependent variables, with each failure worsening the next",
                "C": "A random correlation with no causal mechanism",
                "D": "A positive feedback loop where the last variable feeds back to the first"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is a feedforward cascade: immune activation causes inflammation, inflammation reduces blood vessel formation around the implant, reduced blood flow starves cells of nutrients, and nutrient-deprived cells cannot attach and integrate. Each step directly causes the next in a unidirectional chain of degradation.",
            "feedback_incorrect": "Trace the causal direction: does each variable in the chain cause the next one to worsen? Does the last variable loop back to affect the first, or is this a one-directional cascade?"
        },
        {
            "question": "A team proposes incorporating living kidney cells into a synthetic filtration membrane to create a bioartificial kidney. Based on the model, what new challenge does adding living cells introduce that a purely synthetic device does not face?",
            "choices": {
                "A": "Living cells make the device heavier, which is the only concern",
                "B": "Living cells require continuous Nutrient Transport and oxygen supply, are vulnerable to immune attack as foreign biological material, and can die if Blood Flow Integration is insufficient — adding biological complexity to the engineering challenge",
                "C": "Living cells eliminate all biocompatibility concerns because they are biological",
                "D": "Adding living cells has no significant effect on any model variable"
            },
            "correct": "B",
            "feedback_correct": "Correct. Living cells transform the engineering challenge: they require vascularization for nutrients and oxygen (diffusion limits cells to within 200 micrometers of a blood vessel), they may trigger immune responses if they come from a different individual, and they can die from insufficient blood flow. The device must now sustain living tissue in addition to performing mechanical filtration.",
            "feedback_incorrect": "Consider what living cells need to survive inside a device. Unlike synthetic materials, cells require oxygen, glucose, and waste removal. What model variables become critical when the device contains living tissue?"
        }
    ]
}

L08_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Ocean surface water in the tropics is approximately 25-30 degrees Celsius while deep water at 1,000 meters is approximately 4-5 degrees Celsius. What physical principle allows this temperature difference to be used for electricity generation?",
            "choices": {
                "A": "Cold water naturally generates electricity when brought to the surface",
                "B": "A heat engine can extract work from any temperature difference — warm water evaporates a working fluid, the vapor drives a turbine, and cold water condenses it back to liquid, completing the thermodynamic cycle",
                "C": "The temperature difference creates pressure that directly drives a turbine",
                "D": "The mixing of warm and cold water creates a chemical reaction that produces electricity"
            },
            "correct": "B",
            "feedback_correct": "Correct. OTEC uses the same thermodynamic principle as any heat engine (like a steam power plant): heat flows from a hot source to a cold sink, and work is extracted during the transfer. The unique aspect is that both the heat source and sink are seawater at relatively low temperatures.",
            "feedback_incorrect": "Think about how a conventional power plant works: it uses a temperature difference to evaporate a fluid, drive a turbine, and condense the fluid. OTEC applies the same principle but uses ocean water as both the heat source and cold sink."
        },
        {
            "question": "The Carnot efficiency formula gives the maximum possible efficiency for a heat engine: efficiency = 1 - (T_cold / T_hot), where temperatures are in Kelvin. For OTEC with surface water at 28 degrees C (301 K) and deep water at 4 degrees C (277 K), what is the maximum theoretical efficiency?",
            "choices": {
                "A": "Approximately 86% (very high efficiency like a modern gas turbine)",
                "B": "Approximately 50% (moderate efficiency)",
                "C": "Approximately 8% (very low efficiency due to the small temperature difference)",
                "D": "Approximately 0.1% (essentially zero usable energy)"
            },
            "correct": "C",
            "feedback_correct": "Correct. Carnot efficiency = 1 - (277/301) = 1 - 0.920 = 0.080 or about 8%. This is the theoretical MAXIMUM — actual net efficiency is 2-3% after pumping costs. The small temperature differential (24 degrees vs. hundreds of degrees in fossil plants) fundamentally limits OTEC efficiency.",
            "feedback_incorrect": "Apply the Carnot formula: efficiency = 1 - (T_cold/T_hot) = 1 - (277/301). Note that both temperatures must be in Kelvin (add 273 to Celsius). The result shows the maximum fraction of thermal energy that can be converted to work."
        },
        {
            "question": "A conventional natural gas power plant operates with a temperature difference of approximately 1,000 degrees Celsius. OTEC operates with approximately 20 degrees Celsius. What engineering consequence does this 50-fold difference in temperature gradient have?",
            "choices": {
                "A": "No engineering consequence — both systems produce similar amounts of electricity",
                "B": "OTEC must process approximately 50 times more working fluid per unit of electricity generated, requiring massive heat exchangers and seawater pumps",
                "C": "OTEC compensates by running 50 times faster than gas turbines",
                "D": "The temperature difference only affects efficiency, not equipment size"
            },
            "correct": "B",
            "feedback_correct": "Correct. Because each unit of seawater contains very little extractable energy (due to the small temperature difference and low Carnot efficiency), enormous volumes must be processed. A 100 MW OTEC plant must pump millions of gallons of seawater per minute, requiring massive infrastructure that dominates the engineering challenge and cost.",
            "feedback_incorrect": "If each gallon of water provides very little energy (due to low efficiency), how much water must be processed to generate significant electricity? Compare this to a gas plant that extracts much more energy per unit of fuel."
        },
        {
            "question": "OTEC deep-water intake pipes must extend to 800-1,000 meters depth. What is the primary engineering challenge of building and maintaining these pipes in the open ocean?",
            "choices": {
                "A": "The pipes must be heated to prevent the cold water from freezing",
                "B": "The pipes face enormous hydrostatic pressure, ocean current forces, corrosive saltwater, biofouling by marine organisms, and potential damage from storms — all while maintaining structural integrity over decades",
                "C": "Deep water cannot be pumped to the surface because of pressure differences",
                "D": "The pipes are too expensive to manufacture but are otherwise straightforward to maintain"
            },
            "correct": "B",
            "feedback_correct": "Correct. The deep-water pipe faces multiple simultaneous challenges: hydrostatic pressure increases with depth, ocean currents exert lateral forces, saltwater corrodes metals, marine organisms (barnacles, algae) colonize surfaces and reduce thermal efficiency, and tropical storms can damage surface connections. These combined stresses must be managed for 20-30 year operational lifespans.",
            "feedback_incorrect": "Consider all the environmental forces acting on a pipe that extends 1 km into the ocean: pressure, currents, corrosion, biological growth, and storm damage. What makes maintaining such infrastructure challenging?"
        },
        {
            "question": "Unlike solar and wind energy, OTEC can generate electricity 24 hours a day, 365 days a year. What physical characteristic of the ocean makes this baseload consistency possible?",
            "choices": {
                "A": "The ocean is heated by underwater volcanoes that operate continuously",
                "B": "Ocean surface temperature and deep water temperature remain relatively stable regardless of time of day or season in tropical regions — the thermal gradient is always present because of the ocean's enormous heat capacity",
                "C": "OTEC plants store energy during the day for nighttime use",
                "D": "Wind drives the temperature differential, and wind blows at night too"
            },
            "correct": "B",
            "feedback_correct": "Correct. The ocean's enormous thermal mass (high heat capacity) means surface temperatures in the tropics vary by only 1-2 degrees Celsius between day and night, and deep water temperature is essentially constant. Unlike solar (no sun at night) or wind (intermittent), the temperature gradient is continuously available.",
            "feedback_incorrect": "Consider what drives solar and wind intermittency versus what drives OTEC. Solar depends on sunlight (absent at night). Wind varies unpredictably. What about the ocean temperature gradient — does it change significantly between day and night?"
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that reducing the Temperature Differential from 24 degrees to 15 degrees Celsius causes Power Output to drop by more than 50%, even though the temperature change is only about 35%. What physical relationship explains this nonlinear response?",
            "choices": {
                "A": "The model has a calculation error for small temperature differentials",
                "B": "Carnot efficiency is proportional to the temperature differential relative to the absolute temperature, so a 35% reduction in differential reduces maximum efficiency by a similar fraction — but the net power output drops more because the fixed energy cost of pumping becomes a larger fraction of the reduced output",
                "C": "Temperature differential has a linear relationship with power output",
                "D": "The deep water pump automatically shuts down at lower differentials"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals a compounding effect: reduced differential lowers both the Carnot efficiency ceiling and the thermal energy available per unit of water. Meanwhile, pumping costs (which are roughly fixed) consume a larger percentage of the reduced output. Net power drops faster than the differential reduction because of this double squeeze on efficiency.",
            "feedback_incorrect": "Consider two effects: (1) lower temperature differential means lower theoretical efficiency, and (2) the energy cost of pumping water remains roughly the same. If the gross output decreases but the pumping cost stays constant, what happens to net output?"
        },
        {
            "question": "The model includes Environmental Impact as an internal variable that increases with Fluid Flow Rate. A student argues this trade-off makes OTEC environmentally harmful. What evidence from the model provides a more nuanced evaluation?",
            "choices": {
                "A": "The model shows zero environmental impact at all flow rates",
                "B": "Environmental Impact has both negative effects (ecosystem disruption from temperature changes) and potential positive effects (nutrient-rich deep water upwelling enhances marine productivity) — the net effect depends on flow rate, location, and management practices",
                "C": "OTEC has no environmental impact because it uses natural ocean water",
                "D": "The model does not address environmental impact"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model captures a genuine duality: cold, nutrient-rich deep water brought to the surface can fertilize marine ecosystems and enhance fisheries (positive), but it also changes local temperature patterns and disrupts existing ecosystem structure (negative). Responsible OTEC design must manage this trade-off through careful siting and discharge management.",
            "feedback_incorrect": "Consider what happens when you pump nutrient-rich deep water to the nutrient-depleted surface. Is the ecological effect entirely negative, or could there be beneficial consequences alongside the disruptive ones?"
        },
        {
            "question": "The model classifies Surface Water Temperature and Deep Water Temperature as external variables. Why is Temperature Differential classified as internal even though it is simply the mathematical difference between them?",
            "choices": {
                "A": "All mathematical relationships between variables must be internal",
                "B": "Temperature Differential is an emergent system property — it depends on both external temperatures and on local conditions like mixing, seasonal variation, and the OTEC system's own cold water discharge, making it more than a simple subtraction of two inputs",
                "C": "Temperature Differential cannot be calculated, only measured empirically",
                "D": "The classification is incorrect and should be changed"
            },
            "correct": "B",
            "feedback_correct": "Correct. While Temperature Differential appears to be a simple calculation, in practice it is affected by the system's own operation. Cold water discharged near the surface can reduce the local surface temperature, decreasing the effective differential. This feedback makes it an emergent property rather than a pure input.",
            "feedback_incorrect": "Consider whether the OTEC system itself can change the local temperature conditions. If the system discharges cold deep water near the surface, what happens to the local surface temperature? Does the differential remain constant?"
        },
        {
            "question": "The maximum scale scenario shows that increasing Fluid Flow Rate 10x increases Power Output approximately 10x but increases Infrastructure Cost by 15x and Environmental Impact by 12x. What does this disproportionate scaling reveal?",
            "choices": {
                "A": "OTEC scales perfectly and should be built as large as possible",
                "B": "Diminishing returns at scale — each additional unit of power becomes progressively more expensive and environmentally impactful because larger pipes, pumps, and platforms have disproportionately higher costs and ecological footprints",
                "C": "The model incorrectly overestimates the cost of larger systems",
                "D": "Infrastructure Cost and Environmental Impact are unrelated to Fluid Flow Rate"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that power output scales approximately linearly with flow rate, but costs and impacts scale superlinearly (faster than linear). This means there is an economically optimal facility size beyond which each additional megawatt costs more and causes more harm per unit of energy — a critical insight for OTEC deployment planning.",
            "feedback_incorrect": "Compare the scaling factors: power goes up 10x but cost goes up 15x. Does the cost per unit of energy decrease, stay the same, or increase as the facility scales up?"
        },
        {
            "question": "An island nation currently pays $0.40/kWh for diesel electricity. The model predicts OTEC could deliver power at $0.15-0.25/kWh. A student argues OTEC is clearly the better option. What important variable from the model should temper this conclusion?",
            "choices": {
                "A": "The model proves diesel is always cheaper than OTEC",
                "B": "Infrastructure Cost — the massive upfront capital investment for the offshore platform, deep-water pipes, and submarine power cables requires billions of dollars and decades of operation to recover, creating financial risk even when per-kWh costs are lower",
                "C": "OTEC produces electricity of lower quality than diesel generators",
                "D": "The diesel price will decrease to below OTEC cost in the future"
            },
            "correct": "B",
            "feedback_correct": "Correct. While operating cost per kWh favors OTEC, the model shows that Infrastructure Cost is enormous — $25,000-$50,000 per installed kilowatt, orders of magnitude higher than diesel generators. The island must finance billions in upfront construction costs and operate for decades to achieve the per-kWh savings. This capital barrier, not operating cost, is typically the limiting factor.",
            "feedback_incorrect": "Consider the difference between operating cost (per kWh) and capital cost (upfront investment). Even if OTEC is cheaper to run, what about the cost to build the facility in the first place?"
        }
    ]
}

L09_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Scientists have recovered fragmented DNA from woolly mammoth specimens preserved in permafrost. Why is ancient DNA always incomplete, and what does this mean for de-extinction?",
            "choices": {
                "A": "Ancient DNA is complete but encoded differently than modern DNA",
                "B": "DNA degrades over time through hydrolysis, oxidation, and cross-linking, breaking into increasingly short fragments — meaning the reconstructed genome is a patchwork of recovered mammoth sequences and gap-filling from the closest living relative (Asian elephant)",
                "C": "Permafrost perfectly preserves DNA in its original complete form",
                "D": "DNA degradation only occurs in tropical environments, not permafrost"
            },
            "correct": "B",
            "feedback_correct": "Correct. Even under the best preservation conditions (permafrost at -50 degrees Celsius), chemical processes slowly break DNA strands and modify individual bases. After 4,000+ years, the mammoth genome is fragmentary. Scientists must assemble these fragments and fill gaps with Asian elephant DNA, creating a hybrid genome rather than a true mammoth genome.",
            "feedback_incorrect": "Consider what happens to complex organic molecules over thousands of years. Even in frozen conditions, chemical reactions slowly break and modify DNA. What implications does this have for reconstructing a complete genome?"
        },
        {
            "question": "CRISPR gene editing can modify an Asian elephant cell to express mammoth traits like cold-adapted hemoglobin, thick fat layers, and long hair. Why does this not constitute true de-extinction?",
            "choices": {
                "A": "CRISPR cannot make precise enough edits for de-extinction",
                "B": "The result is an Asian elephant with selected mammoth traits — a hybrid organism with primarily elephant genetics — not a complete resurrection of the mammoth species with its full genome, behavioral repertoire, and ecological relationships",
                "C": "The edited cells cannot develop into a living organism",
                "D": "CRISPR only works on bacteria, not mammalian cells"
            },
            "correct": "B",
            "feedback_correct": "Correct. CRISPR can insert specific mammoth genes into an elephant genome, but a species is more than a collection of traits. The resulting organism has an elephant developmental program, elephant immune system, and no inherited mammoth behaviors (migration routes, social structures, foraging strategies). It is a cold-adapted elephant, not a mammoth.",
            "feedback_incorrect": "Consider what makes a species more than its visible physical traits. A mammoth's genome contained tens of thousands of genes controlling development, immunity, behavior, and physiology. Can editing a few dozen genes recreate the full organism?"
        },
        {
            "question": "The minimum viable population (MVP) for large mammals is estimated at 500-5,000 individuals. Why does de-extinction require creating hundreds of genetically diverse individuals rather than just one?",
            "choices": {
                "A": "One individual is sufficient to establish a population through cloning",
                "B": "A population below MVP lacks sufficient genetic diversity, leading to inbreeding depression — reduced fertility, increased disease susceptibility, and loss of adaptive potential that causes population decline toward extinction a second time",
                "C": "Multiple individuals are needed only for companionship",
                "D": "The MVP concept applies only to currently living species, not de-extinct ones"
            },
            "correct": "B",
            "feedback_correct": "Correct. A self-sustaining population requires genetic diversity to maintain fertility, disease resistance, and adaptive potential across generations. A population founded from one or a few individuals becomes increasingly inbred, accumulating harmful recessive alleles and losing the genetic variation needed to adapt to environmental changes.",
            "feedback_incorrect": "Consider what happens to a population with very few individuals. Over generations, they must mate with relatives. What happens to the health and reproductive success of inbred populations?"
        },
        {
            "question": "The mammoth steppe — the vast grassland ecosystem mammoths inhabited — has largely converted to boreal forest and tundra over the past 10,000 years. What does this habitat transformation mean for de-extinction plans?",
            "choices": {
                "A": "The habitat change is irrelevant because mammoths can adapt to any environment",
                "B": "Mammoths evolved for an ecosystem that no longer exists, meaning reintroduced mammoths would face unfamiliar vegetation, different predators, novel diseases, and a fundamentally altered ecological context",
                "C": "The mammoth steppe still exists exactly as it was 10,000 years ago in Siberia",
                "D": "Habitat changes occurred too slowly to affect large mammals"
            },
            "correct": "B",
            "feedback_correct": "Correct. De-extinction faces the 'ecological niche' problem: the ecological role mammoths played (maintaining grasslands through grazing, compacting snow, dispersing seeds) may no longer be supported by the current ecosystem. The food sources, competitors, predators, and climate conditions have all changed. Reintroduced mammoths would inhabit a world that has moved on without them.",
            "feedback_incorrect": "Consider what happens when you place an organism in an ecosystem it did not evolve to inhabit. Are the right food plants available? Are there new diseases? Has the climate changed?"
        },
        {
            "question": "Some scientists argue that de-extinction funds would be better spent protecting currently endangered species. What is the strongest scientific basis for this opportunity cost argument?",
            "choices": {
                "A": "Endangered species are less interesting to the public than mammoths",
                "B": "Currently endangered species have intact genomes, known ecological roles, existing habitats (though threatened), and established conservation methods — the same investment could protect entire ecosystems with existing species rather than attempting to recreate one species for an uncertain ecological outcome",
                "C": "De-extinction is guaranteed to fail so the money would be completely wasted",
                "D": "Endangered species do not need additional funding because they are already protected by law"
            },
            "correct": "B",
            "feedback_correct": "Correct. Conservation triage asks where limited resources produce the greatest biodiversity benefit. Protecting existing species preserves functional ecosystems, intact genomes, and evolved ecological relationships. De-extinction requires solving DNA recovery, genome reconstruction, surrogate pregnancy, population founding, habitat restoration, and disease resistance — with uncertain outcomes. The comparison is between proven conservation and experimental resurrection.",
            "feedback_incorrect": "Compare what you know and can protect (existing species with known needs) versus what you must reconstruct from scratch (an extinct species with incomplete DNA, no habitat, and no immune defense against modern diseases). Where does each dollar produce more conservation value?"
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model shows that even with maximum DNA Recovery Quality and Gene Editing Accuracy, Population Viability remains low until hundreds of genetically distinct individuals are created. What bottleneck does this reveal?",
            "choices": {
                "A": "DNA technology is not advanced enough for de-extinction",
                "B": "The genetic diversity bottleneck — each ancient specimen provides only one genome's worth of variation, and creating a viable population requires many distinct genomes to prevent inbreeding depression, regardless of how accurately individual genomes are reconstructed",
                "C": "Population Viability is unrelated to genetic diversity in the model",
                "D": "Creating one individual is sufficient because it can reproduce asexually"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that technological perfection in reconstructing one genome does not solve the population-level challenge. Each ancient specimen provides unique genetic variation, and few well-preserved specimens exist. Without enough distinct genomes, the founding population lacks the diversity needed for long-term viability, regardless of the quality of individual reconstructions.",
            "feedback_incorrect": "Consider the difference between individual and population genetics. Even a perfectly reconstructed genome from one specimen provides only that individual's genetic variation. How many different individuals' DNA do you need for a diverse founding population?"
        },
        {
            "question": "The ecological mismatch scenario shows viable de-extinct individuals but low Ecosystem Readiness and Habitat Availability. The model predicts Ecological Integration remains low despite healthy individuals. What does this demonstrate?",
            "choices": {
                "A": "Healthy individuals always integrate successfully into any ecosystem",
                "B": "De-extinction is not just a genetics problem but an integrated ecological challenge — a genetically viable organism that lacks an ecological niche, appropriate habitat, and established species relationships cannot sustain itself in the wild",
                "C": "The model incorrectly separates genetics from ecology",
                "D": "Ecological factors are irrelevant to de-extinction success"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates the cascade structure of de-extinction: solving technology (DNA + gene editing) is necessary but insufficient. Without solving ecology (habitat + niche + species interactions), the animals are confined to managed care — expensive zoo exhibits rather than self-sustaining wild populations. All ten variables must reach viable levels simultaneously.",
            "feedback_incorrect": "Consider what happens when you place a healthy animal in an ecosystem where its food sources, climate conditions, and ecological relationships have changed. Can the animal survive even if it is genetically healthy?"
        },
        {
            "question": "The model classifies Ethical Threshold as an external variable alongside DNA Recovery Quality and Gene Editing Accuracy. Why is an ethical variable included in a scientific model?",
            "choices": {
                "A": "Ethics is not relevant to science and should be removed from the model",
                "B": "Ethical and societal considerations directly affect funding, regulatory approval, and public support — which determine whether a technically viable project actually proceeds and receives the resources needed for success",
                "C": "The model includes Ethical Threshold only as a placeholder with no functional connections",
                "D": "All external variables in scientific models must include ethical considerations"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model recognizes that scientific projects exist within societal contexts. High ethical concerns can reduce funding, increase regulatory barriers, and erode public support — all of which constrain the project's ability to achieve the scale needed for population viability. Ethics is not separate from feasibility; it is a determining factor.",
            "feedback_incorrect": "Consider what happens to a research project when the public objects to it, regulators impose restrictions, or funding agencies redirect money to less controversial alternatives. Do ethical concerns affect whether a scientifically possible project actually happens?"
        },
        {
            "question": "The model includes Disease Resistance as a variable showing that de-extinct mammoths would face modern pathogens their immune systems never evolved to fight. Which analogy from history best illustrates this vulnerability?",
            "choices": {
                "A": "The domestication of cats, which adapted easily to human environments",
                "B": "The introduction of European diseases to Indigenous populations in the Americas — populations without evolutionary exposure to specific pathogens suffered catastrophic mortality because their immune systems lacked evolved defenses",
                "C": "The extinction of dinosaurs from asteroid impact, which is unrelated to disease",
                "D": "Modern humans traveling to Mars, who would face only known Earth pathogens"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is a direct parallel: populations without evolutionary exposure to specific pathogens are highly vulnerable. Mammoths have been absent for 4,000 years, during which bacteria, viruses, and parasites have continued evolving. The de-extinct mammoth's immune system would have no evolved defense against these modern pathogens, creating a serious survival challenge.",
            "feedback_incorrect": "Think about what happens when an organism encounters pathogens it has no evolutionary history with. Has this happened before in human history? What were the consequences?"
        },
        {
            "question": "After running all three scenarios, a student argues that de-extinction should proceed because the technology is nearly viable, even though ecological barriers remain unsolved. Using model evidence, what is the strongest counterargument?",
            "choices": {
                "A": "The technology is not actually viable, so the argument fails on its first premise",
                "B": "The model shows that Population Viability, Ecological Integration, and Habitat Availability must ALL reach viable levels for a self-sustaining wild population — technology alone produces managed zoo specimens, not species restoration, and the ecological barriers require habitat-scale interventions that may take decades or centuries",
                "C": "There are no counterarguments to proceeding with de-extinction",
                "D": "The ecological barriers will resolve themselves once the technology is perfected"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that de-extinction success requires ALL ten variables at viable levels simultaneously. Technology addresses 2-3 variables (DNA, gene editing, surrogate pregnancy). The remaining 7 ecological, population, and ethical variables require separate, potentially more difficult solutions. Proceeding on technology alone creates expensive captive animals, not restored species.",
            "feedback_incorrect": "Count how many of the ten model variables are addressed by technology alone versus how many require ecological and societal solutions. If only 2-3 out of 10 are solved, is the project likely to achieve its goal of species restoration?"
        }
    ]
}

L10_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A space elevator cable must extend from Earth's surface to beyond geostationary orbit (35,786 km). What two forces keep the cable taut and stationary relative to the ground?",
            "choices": {
                "A": "Electromagnetic attraction between the cable and the atmosphere, and wind pushing the cable upward",
                "B": "Gravity pulling the lower portion toward Earth and centrifugal force from Earth's rotation pulling the upper portion and counterweight outward — these forces balance at geostationary orbit",
                "C": "Rocket thrust at the top and magnetic anchoring at the base",
                "D": "The cable is so rigid that it does not need any forces to maintain its shape"
            },
            "correct": "B",
            "feedback_correct": "Correct. Below geostationary orbit, gravity dominates (pulling the cable down). Above it, centrifugal force from Earth's rotation dominates (pulling the cable outward). The cable is balanced with its center of mass at geostationary altitude, with the counterweight beyond geostationary orbit providing the centrifugal force to keep the whole structure taut.",
            "feedback_incorrect": "Think about what happens to an object attached to a rotating body. Below a certain altitude, gravity pulls it inward. Above that altitude, the centrifugal effect of rotation pulls it outward. Where is the balance point?"
        },
        {
            "question": "Carbon nanotubes have a theoretical tensile strength of 100+ GPa, making them the strongest material ever theorized. Current manufacturing produces fibers of only 1-2 GPa. What does this 50-100x gap represent?",
            "choices": {
                "A": "A fundamental physical impossibility — the theoretical strength is wrong",
                "B": "The difference between the perfect atomic structure theorized for individual nanotubes and the defects, misalignment, and weak junctions that occur when manufacturing bulk fibers from billions of nanotubes at practical scale",
                "C": "A measurement error in the theoretical calculations",
                "D": "The gap is small enough that current materials already work for a space elevator"
            },
            "correct": "B",
            "feedback_correct": "Correct. Individual carbon nanotubes approach theoretical strength because their atomic structure can be nearly perfect at nanometer scales. Manufacturing bulk fibers requires assembling billions of nanotubes, introducing defects, misalignment, impurities, and weak inter-tube junctions. Each defect is a potential failure point that dramatically reduces bulk strength below theoretical limits.",
            "feedback_incorrect": "Consider the difference between one perfect nanotube (nanometers long) and a fiber made from billions of nanotubes (meters to kilometers long). What happens at the junctions between individual nanotubes? What effect do even small defects have?"
        },
        {
            "question": "Current rocket launches cost approximately $2,000-$10,000 per kilogram to reach orbit. A space elevator could potentially reduce this to under $200 per kilogram. What physical property of rockets drives their high cost?",
            "choices": {
                "A": "Rockets are made from expensive materials that cannot be recycled",
                "B": "Rockets must carry their own fuel, and the fuel needed to lift the fuel creates an exponential mass penalty (the Tsiolkovsky rocket equation) — a space elevator uses external energy to lift the climber, avoiding this mass penalty entirely",
                "C": "Launch facilities are located in expensive real estate areas",
                "D": "Rocket engineers command higher salaries than elevator engineers"
            },
            "correct": "B",
            "feedback_correct": "Correct. The tyranny of the rocket equation: to lift 1 kg of payload, rockets must carry many kilograms of fuel, plus fuel to lift that fuel, plus fuel to lift THAT fuel. This exponential relationship means 90-95% of a rocket's launch mass is fuel. A space elevator eliminates this by transmitting energy externally (laser or microwave) to the climber, so no fuel mass is carried.",
            "feedback_incorrect": "Consider what makes up most of a rocket's mass at launch. Approximately 90-95% is fuel. Why? Because the fuel must also lift itself. A space elevator climber receives energy externally, so it carries no fuel. How does this change the economics?"
        },
        {
            "question": "The cable must support its own weight across 36,000+ km. Gravity is strongest at the surface (9.8 m/s^2) and decreases with altitude squared. At what point along the cable is the stress (tension) maximum?",
            "choices": {
                "A": "At the surface where the cable attaches to the ground anchor",
                "B": "At geostationary orbit (35,786 km) where the transition from gravity-dominated to centrifugal-dominated occurs and the cable supports the maximum total weight below while being pulled outward above",
                "C": "At the very top where the counterweight is attached",
                "D": "Stress is uniform throughout the cable because gravity is the same everywhere"
            },
            "correct": "B",
            "feedback_correct": "Correct. At geostationary orbit, the cable must support the weight of all the cable below it (pulled down by gravity) while being pulled upward by the centrifugal force on the cable and counterweight above. This dual-direction loading creates maximum stress at the geostationary point, which is why cable taper designs are thickest at this altitude.",
            "feedback_incorrect": "Think about what the cable at geostationary altitude must support: below it, all the cable being pulled down by gravity; above it, all the cable and counterweight pulling upward from centrifugal force. Where does the cable bear the most total load?"
        },
        {
            "question": "The lower 100 km of a space elevator cable passes through Earth's atmosphere. What unique challenges does this atmospheric section face that the rest of the cable does not?",
            "choices": {
                "A": "No unique challenges — the atmosphere is too thin to affect the cable",
                "B": "Lightning strikes, wind loading from jet streams and storms, ice accumulation, chemical corrosion from atmospheric gases, and aerodynamic vibration — forces not present in the vacuum of space above",
                "C": "The only challenge is air resistance slowing down the climber vehicle",
                "D": "Atmospheric pressure would crush the cable material"
            },
            "correct": "B",
            "feedback_correct": "Correct. The atmospheric section faces a unique combination of hazards: lightning (the cable is an ideal conductor extending into thunderstorms), wind forces (including jet streams at 200+ mph), ice buildup (adding mass and drag), ozone and UV degradation of materials, and vibration from aerodynamic forces. None of these challenges exist in the vacuum above 100 km.",
            "feedback_incorrect": "Consider what conditions exist in the atmosphere that do not exist in space: weather, wind, lightning, ice, and reactive gases. How would each of these affect a thin cable extending vertically through the atmosphere?"
        }
    ],
    "mc_post_assessment": [
        {
            "question": "The model's current materials scenario (1-2 GPa cable strength) shows the cable snapping under its own weight at approximately 100 km altitude. The carbon nanotube ideal scenario (100+ GPa) shows a viable system. What does this 50-100x gap tell us about the nature of the space elevator problem?",
            "choices": {
                "A": "The space elevator is physically impossible regardless of material advances",
                "B": "The space elevator is a materials science problem, not a physics or engineering problem — the concept is sound, the design is feasible, and the sole blocking obstacle is manufacturing cable material with sufficient tensile strength-to-weight ratio",
                "C": "Better engineering design can compensate for weaker materials",
                "D": "The gap between scenarios is too small to be significant"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model cleanly separates physics (which works — forces balance, the concept is viable) from materials science (which is currently insufficient). When the model uses theoretical material properties, the system functions. When it uses current manufacturing capabilities, it fails catastrophically. This identifies the precise bottleneck.",
            "feedback_incorrect": "Compare what changes between the two scenarios. The physics, the forces, and the engineering design are identical. Only the material strength changes. What does this tell you about where the challenge lies?"
        },
        {
            "question": "In the model, increasing Climber Mass from 5 tons to 20 tons increases Payload Capacity proportionally but requires a corresponding increase in Cable Tensile Strength. What engineering trade-off does this relationship represent?",
            "choices": {
                "A": "Heavier climbers always improve economic viability without any drawbacks",
                "B": "Each additional ton of payload requires a stronger (and therefore heavier or thicker) cable, which itself requires more strength to support — a circular constraint where payload capacity is limited by the cable's strength-to-weight ratio margin above self-support requirements",
                "C": "Climber Mass has no effect on cable requirements in the model",
                "D": "Lighter climbers are always preferable because they reduce cable stress"
            },
            "correct": "B",
            "feedback_correct": "Correct. The cable must support its own weight plus climber loads. A heavier climber requires a thicker cable section where it climbs, which adds cable mass, which requires even more strength. This circular dependency means the cable material's strength-to-weight ratio determines the maximum payload, not just the maximum weight it can hold at one point.",
            "feedback_incorrect": "Consider the chain reaction: heavier climber needs stronger cable, stronger cable means thicker or denser cable, which means more cable mass to support. This creates a constraint where gains in payload are partially offset by the need for more cable material."
        },
        {
            "question": "The model classifies Cable Tensile Strength, Centrifugal Counterweight, and Climber Mass as external variables. Why is Gravitational Force Gradient classified as internal despite being determined by well-known physics?",
            "choices": {
                "A": "Gravitational Force Gradient cannot be calculated accurately",
                "B": "While the gravitational field is a known physical property, in the model it represents how gravitational loading is distributed along the cable — this distribution is an interaction between the cable's physical properties (length, mass distribution, taper) and the gravitational field, making it a system response rather than a design input",
                "C": "All force variables must be classified as internal by convention",
                "D": "The classification is arbitrary"
            },
            "correct": "B",
            "feedback_correct": "Correct. The gravitational force gradient describes how the cable experiences gravity along its length — this depends on the cable's mass distribution, taper profile, and material density interacting with the inverse-square law. Engineers do not set the gradient; they set the cable properties, and the gradient is the resulting load profile. It is a system response to the design choices.",
            "feedback_incorrect": "Ask whether engineers set the gravitational gradient as a design choice (external) or whether it emerges from how the cable they designed interacts with Earth's gravitational field (internal). What can engineers actually control?"
        },
        {
            "question": "The model includes Atmospheric Stress as a variable affecting only the lowest 100 km of cable, while Gravitational Force Gradient affects the entire 100,000+ km structure. A student argues that Atmospheric Stress is negligible because it affects only 0.1% of the cable length. What model evidence counters this argument?",
            "choices": {
                "A": "The student is correct — 100 km out of 100,000+ km is negligible",
                "B": "The atmospheric section faces unique and severe threats (lightning, wind, ice, corrosion) that no other section encounters — a cable break anywhere, including in the atmosphere, is catastrophic for the entire structure regardless of how short that section is",
                "C": "Atmospheric Stress is not included in the model",
                "D": "The atmospheric section can be made from a different, cheaper material"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates the 'weakest link' principle: the cable is only as strong as its most vulnerable section. Lightning, wind loading, ice accumulation, and chemical corrosion in the atmospheric section can cause failure even though it represents a tiny fraction of total length. A break anywhere causes catastrophic collapse of the entire structure.",
            "feedback_incorrect": "Consider what happens if the cable breaks at ANY point along its length. Does it matter whether that break occurs in the atmosphere (100 km) or in space (50,000 km)? A chain is only as strong as its weakest link."
        },
        {
            "question": "Based on all model scenarios, a student concludes that a space elevator will be built within 10 years because the physics is sound. Using model evidence across all ten variables, what is the most comprehensive evaluation of this prediction?",
            "choices": {
                "A": "The prediction is reasonable because the physics and engineering are well understood",
                "B": "The prediction ignores the model's central finding: the materials science gap is 50-100x, no known manufacturing process can produce carbon nanotube fibers at the required strength and length, and even if materials were solved, atmospheric stress, orbital debris, energy transmission, and economic viability present additional unsolved challenges",
                "C": "The model proves the space elevator will never be built",
                "D": "10 years is too conservative — it could be built in 5 years"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that the physics is sound (the concept works) but the implementation faces multiple unsolved challenges across many variables. The materials gap alone is enormous, and it is compounded by atmospheric vulnerability, orbital debris risk, energy transmission challenges, and the need for economically competitive operations. Sound physics is necessary but far from sufficient for an engineering megaproject.",
            "feedback_incorrect": "Look at all ten variables in the model. How many are at viable levels with current technology? The physics works (the concept is valid), but how many engineering and materials science variables remain far from their required values?"
        }
    ]
}

# Aggregate all questions
ALL_QUESTIONS = {
    "G10L3-L01": L01_QUESTIONS,
    "G10L3-L02": L02_QUESTIONS,
    "G10L3-L03": L03_QUESTIONS,
    "G10L3-L04": L04_QUESTIONS,
    "G10L3-L05": L05_QUESTIONS,
    "G10L3-L06": L06_QUESTIONS,
    "G10L3-L07": L07_QUESTIONS,
    "G10L3-L08": L08_QUESTIONS,
    "G10L3-L09": L09_QUESTIONS,
    "G10L3-L10": L10_QUESTIONS,
}
