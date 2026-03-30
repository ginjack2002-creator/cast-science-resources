#!/usr/bin/env python3
"""Multiple choice pre/post assessment questions for Grade 11 Level 3 ModelIt! Lessons

Grade 11 Level 3: Emerging Science & Technology
10 lessons, 5 MC pre-assessment + 5 MC post-assessment per lesson
CAST-exam-style, HS NGSS aligned, testing analysis/evaluation/application
"""

# =============================================================================
# L01: Can CRISPR Cure Genetic Diseases?
# NGSS: HS-LS3-1, HS-LS3-2
# =============================================================================
L01_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A scientist designs a guide RNA to target a specific gene mutation. Which factor most directly determines whether the CRISPR-Cas9 system will cut only the intended DNA sequence and not similar sequences elsewhere in the genome?",
            "choices": {
                "A": "The degree of complementarity between the guide RNA and the target DNA sequence",
                "B": "The total number of genes in the organism's genome",
                "C": "The temperature at which the editing reaction is performed",
                "D": "The type of cell being edited"
            },
            "correct": "A",
            "feedback_correct": "Correct. Guide RNA specificity, the degree to which it matches only the intended target and not similar sequences, is the primary determinant of on-target versus off-target cutting by Cas9.",
            "feedback_incorrect": "The guide RNA's complementarity to the target sequence is the key factor. If it closely matches other genomic locations, Cas9 will cut at those off-target sites as well."
        },
        {
            "question": "Why does editing human germline cells raise different ethical concerns than editing somatic cells?",
            "choices": {
                "A": "Germline cells are harder to access surgically than somatic cells",
                "B": "Changes to germline cells are passed to all future generations without their consent",
                "C": "Somatic cell edits are always more precise than germline cell edits",
                "D": "Germline cells contain different DNA than somatic cells"
            },
            "correct": "B",
            "feedback_correct": "Correct. Germline edits are heritable, meaning every descendant carries the modification, raising unique ethical concerns about consent and unintended consequences across generations.",
            "feedback_incorrect": "The central ethical distinction is heritability. Somatic edits affect only the individual patient, but germline edits become permanent changes in the human gene pool, affecting descendants who never consented."
        },
        {
            "question": "After Cas9 cuts a DNA double strand, the cell can repair the break through two different pathways. Which outcome is most likely when the cell uses non-homologous end joining (NHEJ) instead of homology-directed repair (HDR)?",
            "choices": {
                "A": "The original disease-causing mutation is precisely corrected",
                "B": "Random insertions or deletions are introduced at the cut site",
                "C": "The cut DNA strand is left permanently unrepaired",
                "D": "A template sequence is automatically inserted from a neighboring chromosome"
            },
            "correct": "B",
            "feedback_correct": "Correct. Non-homologous end joining is error-prone and typically introduces random insertions or deletions (indels) at the break site, rather than making a precise correction.",
            "feedback_incorrect": "NHEJ is the error-prone repair pathway. Unlike homology-directed repair, which uses a template to make precise corrections, NHEJ simply joins broken DNA ends and frequently introduces random insertions or deletions."
        },
        {
            "question": "A research team reports that their CRISPR therapy successfully edited 60% of target cells but also produced off-target edits at a rate of 0.1%. Why might this seemingly low off-target rate still be a significant safety concern?",
            "choices": {
                "A": "The 60% editing efficiency is too low to produce any therapeutic benefit",
                "B": "A 0.1% rate applied across 3.2 billion base pairs means millions of potential off-target sites could be affected",
                "C": "Off-target edits only occur in germline cells, not somatic cells",
                "D": "The 0.1% rate will decrease to zero in subsequent cell divisions"
            },
            "correct": "B",
            "feedback_correct": "Correct. Even a 0.1% off-target rate is concerning because the human genome is enormous. Across billions of base pairs and many similar sequences, even a low percentage translates to a meaningful number of unintended edits that could disrupt essential genes.",
            "feedback_incorrect": "The concern is scale. The human genome contains 3.2 billion base pairs with many sequences similar to the target. A 0.1% off-target rate across this vast genome can still produce numerous unintended cuts, some potentially in critical genes."
        },
        {
            "question": "Which statement best describes a fundamental limitation of using CRISPR-Cas9 for gene therapy in living patients?",
            "choices": {
                "A": "CRISPR can only edit bacterial DNA, not human DNA",
                "B": "The Cas9 protein is too large to enter any human cell",
                "C": "Delivering CRISPR components to all affected cells in a tissue while minimizing off-target effects remains a major challenge",
                "D": "CRISPR technology has not yet been tested in any clinical setting"
            },
            "correct": "C",
            "feedback_correct": "Correct. Delivery efficiency is a central challenge: getting CRISPR components into enough target cells to achieve therapeutic benefit while limiting off-target edits and immune reactions remains a major engineering hurdle.",
            "feedback_incorrect": "CRISPR works in human cells and has been used in clinical trials. The fundamental limitation is delivery: efficiently reaching all affected cells while controlling off-target effects and immune responses."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A computational model shows that increasing guide RNA specificity from 85% to 99% reduces off-target edits by 90% but also decreases on-target editing efficiency by 25%. Which interpretation best reflects the system-level trade-off?",
            "choices": {
                "A": "The decrease in efficiency makes high-specificity guide RNAs impractical for all applications",
                "B": "Higher specificity creates a precision-efficiency trade-off that must be evaluated in the context of the disease severity and available alternatives",
                "C": "Off-target reduction is always more important than on-target efficiency regardless of context",
                "D": "The 25% efficiency loss can be eliminated by simply using more Cas9 protein"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is a context-dependent trade-off. For a fatal disease with no alternatives, accepting lower efficiency for higher precision may be justified, while for a non-lethal condition, the calculus may differ.",
            "feedback_incorrect": "The trade-off between precision and efficiency must be evaluated in context. For fatal diseases with no alternatives, reduced efficiency may be acceptable if precision is high. The optimal balance depends on the clinical scenario."
        },
        {
            "question": "In a CRISPR gene therapy model, a student observes that doubling the delivery dose of CRISPR components increases both on-target editing (from 40% to 70% of cells) and off-target events (from 50 to 180 per genome). What does this relationship reveal about the system?",
            "choices": {
                "A": "Off-target events are independent of CRISPR concentration",
                "B": "The dose-response relationship is linear and proportional for both on-target and off-target effects",
                "C": "Off-target events increase disproportionately faster than on-target editing, creating diminishing therapeutic returns at higher doses",
                "D": "Doubling the dose always doubles the therapeutic benefit"
            },
            "correct": "C",
            "feedback_correct": "Correct. On-target editing increased 1.75x while off-target events increased 3.6x, demonstrating a nonlinear relationship where safety risks escalate faster than therapeutic benefits at higher doses.",
            "feedback_incorrect": "Compare the ratios: on-target editing increased from 40% to 70% (1.75x), but off-target events increased from 50 to 180 (3.6x). The off-target risk scales disproportionately, meaning higher doses yield diminishing net therapeutic value."
        },
        {
            "question": "A model compares somatic cell editing for sickle cell disease with germline editing of the same HBB gene mutation. Which analysis best explains why the risk assessment differs fundamentally between these two approaches?",
            "choices": {
                "A": "Somatic editing uses different guide RNAs than germline editing",
                "B": "Germline editing risks are confined to the individual patient while somatic editing affects future generations",
                "C": "In somatic editing, off-target errors affect one patient and can potentially be monitored, while in germline editing, off-target errors become heritable and propagate through the gene pool indefinitely",
                "D": "Somatic cells have fewer off-target sites than germline cells"
            },
            "correct": "C",
            "feedback_correct": "Correct. The fundamental difference is that somatic editing errors are contained within one patient's lifetime and can be monitored, while germline errors become permanent heritable changes that propagate through all future descendants.",
            "feedback_incorrect": "The key distinction is heritability of errors. Somatic editing errors are limited to one patient; germline editing errors enter the human gene pool and are inherited by all descendants, making the consequences of off-target edits irreversible at a population level."
        },
        {
            "question": "A student's CRISPR model shows that homology-directed repair (HDR) occurs in only 20% of edited cells while non-homologous end joining (NHEJ) occurs in 80%. The student proposes increasing Cas9 concentration to improve the HDR rate. Why is this proposal scientifically flawed?",
            "choices": {
                "A": "Increasing Cas9 increases the total number of cuts but does not change the cell's intrinsic preference for NHEJ over HDR, which is determined by cell cycle stage and repair machinery",
                "B": "Higher Cas9 concentration would prevent any DNA repair from occurring",
                "C": "NHEJ and HDR are the same repair pathway at different concentrations",
                "D": "Cas9 concentration only affects germline cells, not somatic cells"
            },
            "correct": "A",
            "feedback_correct": "Correct. The ratio of HDR to NHEJ is determined by the cell's intrinsic repair machinery and cell cycle phase, not by Cas9 concentration. More Cas9 creates more cuts but does not shift which repair pathway the cell activates.",
            "feedback_incorrect": "The cell's choice between HDR and NHEJ depends on its repair machinery availability and cell cycle stage, not on Cas9 levels. Adding more Cas9 increases total cuts (including off-target) without changing the fundamental repair pathway ratio."
        },
        {
            "question": "Based on the CRISPR gene editing model, which conclusion about the relationship between guide RNA design and therapeutic outcomes is best supported by the simulation data?",
            "choices": {
                "A": "Perfect guide RNA specificity guarantees zero off-target effects in all patients",
                "B": "Guide RNA specificity is the single most important variable in the system because it determines the initial distribution of on-target versus off-target Cas9 activity, which cascades through repair pathway selection and clinical outcomes",
                "C": "Guide RNA design has minimal impact on therapeutic outcomes because delivery efficiency is the only variable that matters",
                "D": "Longer guide RNA sequences always produce better therapeutic outcomes than shorter sequences"
            },
            "correct": "B",
            "feedback_correct": "Correct. Guide RNA specificity is the upstream variable that determines where Cas9 cuts. Every downstream outcome, from repair pathway activation to therapeutic benefit to unintended mutations, depends on this initial targeting accuracy.",
            "feedback_incorrect": "Guide RNA specificity is the foundational upstream variable in the system. It determines where Cas9 cuts, which then cascades to affect repair pathway selection, on-target correction rates, off-target mutation rates, and ultimately clinical outcomes."
        }
    ]
}

# =============================================================================
# L02: The Quantum Computing Revolution
# NGSS: HS-PS4-3, HS-PS4-5
# =============================================================================
L02_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A qubit differs from a classical bit because a qubit can exist in superposition. What does this mean for computational processing?",
            "choices": {
                "A": "A qubit processes information twice as fast as a classical bit",
                "B": "A qubit can represent both 0 and 1 simultaneously with different probability amplitudes, enabling quantum parallelism",
                "C": "A qubit stores two classical bits of information in the same physical space",
                "D": "A qubit switches between 0 and 1 faster than a classical bit"
            },
            "correct": "B",
            "feedback_correct": "Correct. Superposition allows a qubit to exist in a combination of 0 and 1 states simultaneously, described by probability amplitudes. This enables quantum algorithms to explore many solutions in parallel.",
            "feedback_incorrect": "Superposition is not about speed or storage size. A qubit occupies both 0 and 1 states simultaneously with different probability amplitudes until measured. This allows quantum algorithms to process exponentially many states in parallel."
        },
        {
            "question": "Superconducting qubits must be cooled to approximately 15 millikelvin, colder than outer space. What is the primary reason for this extreme cooling requirement?",
            "choices": {
                "A": "Superconducting materials only become conductive at very low temperatures",
                "B": "Thermal energy at higher temperatures destroys the fragile quantum superposition states that enable quantum computation",
                "C": "The cooling system generates the magnetic fields needed for qubit operations",
                "D": "Low temperatures increase the physical size of qubits, making them easier to manufacture"
            },
            "correct": "B",
            "feedback_correct": "Correct. Even tiny amounts of thermal energy cause decoherence, destroying the quantum superposition that gives qubits their computational advantage. Extreme cooling minimizes this environmental interference.",
            "feedback_incorrect": "The primary reason is decoherence. Thermal vibrations, even at millikelvin scales, can destroy the quantum superposition states. Extreme cooling minimizes thermal noise so qubits maintain their quantum properties long enough to complete calculations."
        },
        {
            "question": "Why is quantum error correction fundamentally different from classical error correction?",
            "choices": {
                "A": "Quantum systems do not experience errors during computation",
                "B": "Classical errors can be detected by copying the data and comparing, but quantum states cannot be copied without destroying them",
                "C": "Quantum error correction requires fewer resources than classical error correction",
                "D": "Classical computers use parity bits while quantum computers use standard checksums"
            },
            "correct": "B",
            "feedback_correct": "Correct. The no-cloning theorem prevents copying quantum states, so error correction must use fundamentally different strategies, such as encoding one logical qubit across many physical qubits to detect and correct errors indirectly.",
            "feedback_incorrect": "The core difference is that quantum states cannot be copied or directly measured without destroying them (the no-cloning theorem). Classical error correction relies on copying data to detect errors, but quantum error correction must encode information redundantly across many physical qubits."
        },
        {
            "question": "A quantum computer with 50 qubits can theoretically represent 2^50 states simultaneously. Why doesn't this automatically make it faster than a classical supercomputer for all problems?",
            "choices": {
                "A": "50 qubits cannot store enough data for complex problems",
                "B": "Quantum advantage only exists for specific problem types where quantum algorithms exploit interference and entanglement; many problems have no known quantum speedup",
                "C": "Classical supercomputers always run faster because they operate at room temperature",
                "D": "The 2^50 states are all identical and provide no computational diversity"
            },
            "correct": "B",
            "feedback_correct": "Correct. Quantum advantage is problem-specific. Only certain problems, such as factoring, optimization, and quantum simulation, have quantum algorithms that are provably faster. For many everyday computations, classical computers are equally or more efficient.",
            "feedback_incorrect": "Quantum speedup is not universal. It requires quantum algorithms that exploit superposition, entanglement, and interference for specific problem structures. Many computational tasks have no known quantum advantage."
        },
        {
            "question": "Decoherence sets a time limit on quantum computation. Which statement best describes the engineering challenge this creates?",
            "choices": {
                "A": "All quantum computations must complete before qubits lose their quantum states, but error correction to extend this time requires additional qubits and gate operations that themselves introduce errors",
                "B": "Decoherence can be completely eliminated by using better materials",
                "C": "Decoherence only affects the final measurement step, not the computation itself",
                "D": "Longer computations produce more accurate results because qubits stabilize over time"
            },
            "correct": "A",
            "feedback_correct": "Correct. This is the central paradox: decoherence limits computation time, but error correction (the solution) consumes the very qubits and gate operations that decoherence is degrading, creating a challenging resource trade-off.",
            "feedback_incorrect": "Decoherence creates a countdown clock. The solution, quantum error correction, requires more qubits and more gates, which themselves are imperfect and consume limited resources. This creates a paradox where the cure for errors consumes the resources errors are destroying."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's quantum computing model shows that increasing qubit count from 50 to 100 doubles the potential computational power but increases the gate error rate from 0.5% to 0.8% per operation. For a 1,000-gate circuit, what is the most accurate analysis of this trade-off?",
            "choices": {
                "A": "The increased qubit count will always outweigh the higher error rate",
                "B": "At 0.8% error per gate across 1,000 gates, the cumulative error probability approaches certainty, meaning the additional qubits provide no usable computational advantage without improved error correction",
                "C": "The error rate increase is negligible because individual gate errors do not compound",
                "D": "Reducing the circuit to 100 gates would eliminate all errors"
            },
            "correct": "B",
            "feedback_correct": "Correct. Compound error probability across 1,000 gates at 0.8% per gate means the probability of zero errors is approximately (0.992)^1000, which is vanishingly small. More qubits are useless if the computation is drowned in errors.",
            "feedback_incorrect": "Gate errors compound across circuit depth. At 0.8% per gate over 1,000 gates, the probability that the entire circuit executes correctly is (0.992)^1000, which is extremely small. The additional qubits cannot overcome this error accumulation without better error correction."
        },
        {
            "question": "The model demonstrates that quantum volume, not raw qubit count, determines actual computational capability. Which combination of improvements would most effectively increase quantum volume?",
            "choices": {
                "A": "Doubling qubit count while keeping all other parameters the same",
                "B": "Simultaneously improving gate fidelity, coherence time, and qubit connectivity while modestly increasing qubit count",
                "C": "Maximizing qubit count and accepting higher error rates as a necessary trade-off",
                "D": "Reducing operating temperature from 15 millikelvin to 10 millikelvin without any other changes"
            },
            "correct": "B",
            "feedback_correct": "Correct. Quantum volume is a holistic metric. Increasing qubit count without improving gate fidelity, coherence, and connectivity produces an unusable system. Balanced improvement across all parameters yields the greatest gain in actual computational capability.",
            "feedback_incorrect": "Quantum volume combines qubit count, gate fidelity, coherence time, and connectivity into a single metric. Improving one dimension alone, especially qubit count, without improving others provides minimal real-world computational gain."
        },
        {
            "question": "A simulation shows that a quantum algorithm solves an optimization problem in 10 seconds that would take a classical computer 10,000 years. A student claims this proves quantum computers are universally superior. Which response best evaluates this claim?",
            "choices": {
                "A": "The claim is correct because the speedup factor is enormous",
                "B": "The claim is incorrect because the comparison only demonstrates quantum advantage for that specific problem class; quantum computers may offer no speedup for sorting, databases, or many other computational tasks",
                "C": "The claim is incorrect because classical computers will eventually match quantum speed through hardware improvements",
                "D": "The claim is correct because all NP-hard problems can be solved faster on quantum computers"
            },
            "correct": "B",
            "feedback_correct": "Correct. Quantum advantage is problem-specific. Exponential speedups exist for certain problem classes (factoring, certain optimizations, quantum simulation) but not for general-purpose computing. The dramatic speedup in one domain does not generalize.",
            "feedback_incorrect": "Quantum advantage is domain-specific. Some problems have provable quantum speedups, but many do not. Quantum computers are not universally faster; they exploit specific mathematical structures that only some problems possess."
        },
        {
            "question": "In the model, a student notices that entanglement fidelity drops from 99.5% to 97% when the system scales from 20 to 80 qubits. What is the most significant consequence of this degradation for quantum algorithms?",
            "choices": {
                "A": "The system will consume 2.5% more electricity",
                "B": "Algorithms that depend on entanglement to coordinate multi-qubit operations will produce increasingly unreliable results, potentially making the larger system less capable than the smaller one for entanglement-dependent computations",
                "C": "Individual qubit performance improves to compensate for lower fidelity",
                "D": "The system can still execute all quantum algorithms with minor output adjustments"
            },
            "correct": "B",
            "feedback_correct": "Correct. Many quantum algorithms rely on high-fidelity entanglement. A drop from 99.5% to 97% compounds across operations, and for algorithms requiring extensive entanglement, the larger system may produce worse results than the smaller, higher-fidelity one.",
            "feedback_incorrect": "Entanglement fidelity drops compound across multi-qubit operations. For algorithms heavily dependent on entanglement, the error accumulation in the 80-qubit system could make it effectively less capable than the 20-qubit system despite having four times more qubits."
        },
        {
            "question": "Based on the quantum computing model, which conclusion about the relationship between coherence time and circuit depth is best supported by the simulation data?",
            "choices": {
                "A": "Coherence time and circuit depth are independent variables with no relationship",
                "B": "Coherence time sets an absolute ceiling on circuit depth because all gate operations must complete before quantum states decohere, making coherence time the fundamental bottleneck that limits the complexity of solvable problems",
                "C": "Longer circuits always produce more accurate results regardless of coherence time",
                "D": "Circuit depth can exceed coherence time limits by using faster gate operations without any trade-offs"
            },
            "correct": "B",
            "feedback_correct": "Correct. Coherence time is the fundamental constraint. Every gate operation takes time, and the total circuit must complete before decoherence destroys the quantum state. This makes coherence time the ultimate limit on computational depth and problem complexity.",
            "feedback_incorrect": "Coherence time acts as a hard deadline. Since each gate operation consumes time, the maximum circuit depth equals coherence time divided by gate time. This ceiling limits which problems quantum computers can solve, making coherence time the foundational constraint."
        }
    ]
}

# =============================================================================
# L03: Can We Build a Fusion Reactor?
# NGSS: HS-PS1-8, HS-PS3-2
# =============================================================================
L03_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "The Lawson criterion requires that three plasma parameters must simultaneously exceed critical thresholds for sustained fusion. What makes this a fundamentally difficult engineering challenge?",
            "choices": {
                "A": "Each parameter is easy to achieve individually, but improving one parameter often degrades another",
                "B": "The three parameters are completely independent and can be optimized separately",
                "C": "Only one parameter needs to exceed its threshold; the other two are secondary",
                "D": "Current materials can withstand all required conditions without degradation"
            },
            "correct": "A",
            "feedback_correct": "Correct. The difficulty lies in the coupling between parameters: hotter plasma is harder to confine, denser plasma generates more instabilities, and longer confinement requires stronger magnetic fields. Optimizing all three simultaneously is the central challenge.",
            "feedback_incorrect": "The parameters are coupled, not independent. Increasing plasma temperature makes confinement harder; increasing density generates instabilities; extending confinement time requires ever-stronger magnetic fields. The simultaneous optimization is the core challenge."
        },
        {
            "question": "In a fusion reactor, plasma must be heated to over 150 million degrees Celsius. Why is magnetic confinement necessary at these temperatures?",
            "choices": {
                "A": "Magnetic fields accelerate the fusion reaction rate",
                "B": "No known physical material can survive direct contact with plasma at fusion temperatures, so magnetic fields suspend the plasma away from all surfaces",
                "C": "Magnetic fields cool the plasma to a safe temperature for the reactor walls",
                "D": "The magnetic field provides the neutrons needed for the fusion reaction"
            },
            "correct": "B",
            "feedback_correct": "Correct. At 150 million degrees, any material touching the plasma would instantly vaporize. Superconducting magnets create a 'magnetic bottle' that suspends the charged plasma particles away from physical surfaces.",
            "feedback_incorrect": "The purpose of magnetic confinement is containment, not reaction enhancement. No material exists that can withstand 150 million degrees. Magnetic fields create an invisible container that holds the plasma without physical contact."
        },
        {
            "question": "The Q factor in fusion energy represents the ratio of energy output to energy input. Which Q factor value would indicate that a fusion reactor has achieved the minimum condition for commercial viability?",
            "choices": {
                "A": "Q = 0.5, because any fusion output is valuable",
                "B": "Q = 1, because this means energy breakeven",
                "C": "Q greater than 10, because the reactor must produce enough surplus energy to cover all facility operations, conversion losses, and still deliver power to the grid",
                "D": "Q = infinity, because only self-sustaining plasma is commercially viable"
            },
            "correct": "C",
            "feedback_correct": "Correct. Q = 1 is scientific breakeven, but commercial viability requires Q much greater than 1 to cover energy conversion losses, facility operations, magnet cooling, and other parasitic loads while still delivering net power.",
            "feedback_incorrect": "Scientific breakeven (Q = 1) means energy out equals energy in, but this ignores conversion losses and facility operations. Commercial viability likely requires Q greater than 10 to produce enough surplus energy for practical power generation."
        },
        {
            "question": "Deuterium-tritium fusion produces helium and a high-energy neutron. Why does the neutron flux from fusion reactions pose a long-term challenge for reactor design?",
            "choices": {
                "A": "Neutrons carry negative charges that interfere with the magnetic confinement system",
                "B": "Neutrons are absorbed by the plasma and reduce the fusion reaction rate",
                "C": "High-energy neutrons bombard reactor structural materials, displacing atoms and causing cumulative degradation that limits reactor lifetime",
                "D": "Neutrons escape the reactor and pose radiation hazards to nearby cities"
            },
            "correct": "C",
            "feedback_correct": "Correct. 14.1 MeV neutrons penetrate structural materials, displacing atoms from crystal lattices, creating helium bubbles, and transmuting elements. This cumulative damage limits the lifetime of reactor components.",
            "feedback_incorrect": "Neutrons are uncharged and pass through the magnetic field unconfined. They bombard the reactor's structural first wall, displacing atoms and causing cumulative material degradation that limits component lifetime and creates an engineering challenge for long-term operation."
        },
        {
            "question": "Why must a commercial fusion reactor breed its own tritium fuel?",
            "choices": {
                "A": "Tritium is the most abundant element on Earth but is difficult to extract",
                "B": "Tritium is radioactive with a 12.3-year half-life and does not exist in useful natural quantities, so the reactor must produce it by bombarding lithium with fusion neutrons",
                "C": "Tritium breeding reduces the reactor's Q factor to improve safety",
                "D": "Tritium can only be created through the fusion reaction itself"
            },
            "correct": "B",
            "feedback_correct": "Correct. Tritium's short half-life means it decays away and cannot be stockpiled from natural sources. The reactor must manufacture its own fuel by using fusion neutrons to convert lithium in a breeding blanket into tritium.",
            "feedback_incorrect": "Tritium is radioactive and decays with a 12.3-year half-life. It does not exist in useful natural quantities. A commercial fusion reactor must breed tritium by bombarding lithium in a blanket surrounding the reactor with the neutrons produced by the fusion reaction."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's fusion model shows that increasing plasma temperature from 100M to 200M degrees Celsius doubles the fusion reaction rate but causes a 40% increase in plasma instabilities that degrade confinement time. What does this reveal about the system dynamics?",
            "choices": {
                "A": "Temperature should always be maximized because fusion rate is the only important variable",
                "B": "The system exhibits a coupled feedback where improving one Lawson criterion parameter (temperature) degrades another (confinement time), demonstrating why fusion optimization requires balancing competing constraints",
                "C": "The instabilities can be eliminated by simply increasing magnetic field strength proportionally",
                "D": "The model indicates that lower temperatures are always preferable for fusion"
            },
            "correct": "B",
            "feedback_correct": "Correct. This demonstrates the fundamental coupling in fusion systems: the Lawson criterion parameters are not independent. Optimizing temperature degrades confinement, illustrating why meeting all three conditions simultaneously has been so challenging.",
            "feedback_incorrect": "The key insight is parameter coupling. The Lawson criterion requires temperature, density, and confinement time to all exceed thresholds simultaneously, but increasing temperature drives instabilities that reduce confinement time. This coupling is why fusion optimization is a multi-dimensional balancing act."
        },
        {
            "question": "In the fusion reactor model, doubling magnetic field strength from 5T to 10T improves plasma confinement but requires superconducting magnets that consume 3x more cooling energy. How should this trade-off be evaluated in terms of net energy gain (Q factor)?",
            "choices": {
                "A": "Stronger magnets always improve Q because confinement is the only factor in the energy balance",
                "B": "The additional cooling energy must be subtracted from the fusion energy output; if the increased confinement does not produce enough additional fusion energy to offset the 3x cooling cost, the net Q factor may actually decrease",
                "C": "Cooling energy is free because it comes from the fusion reactor itself",
                "D": "The Q factor only accounts for plasma heating energy, not magnet cooling"
            },
            "correct": "B",
            "feedback_correct": "Correct. The Q factor represents total energy balance. Any energy consumed by the system, including magnet cooling, must be subtracted from the fusion output. Stronger magnets that improve confinement may actually reduce net energy gain if their cooling costs are too high.",
            "feedback_incorrect": "Net energy gain (Q) accounts for ALL energy inputs, including magnet cooling. If doubling field strength triples cooling costs, the improved confinement must produce enough additional fusion energy to more than offset this parasitic load, or Q actually decreases."
        },
        {
            "question": "The model reveals that neutron flux causes first-wall material degradation that follows a nonlinear curve: damage increases slowly for the first 5 years, then accelerates. What engineering implication does this have for commercial reactor design?",
            "choices": {
                "A": "Reactors should be designed for unlimited operational lifetime since early degradation is slow",
                "B": "The nonlinear degradation curve means that reactor first-wall components must be designed for periodic replacement on a schedule determined by the acceleration point, and the replacement cost and downtime must be factored into economic viability",
                "C": "Thicker walls will permanently solve the degradation problem",
                "D": "The accelerating damage indicates that fusion power becomes more efficient over time"
            },
            "correct": "B",
            "feedback_correct": "Correct. Nonlinear degradation with an acceleration point means components have a predictable but limited service life. Commercial reactor design must include engineered replacement schedules, and the associated costs and downtime directly affect economic viability.",
            "feedback_incorrect": "The accelerating degradation curve creates a maintenance engineering challenge. Components cannot last indefinitely, so commercial reactors must be designed with replaceable first-wall modules on predictable schedules, with replacement cost and reactor downtime factored into the economic model."
        },
        {
            "question": "A student uses the model to compare two reactor designs: Design A achieves Q = 15 but has a tritium breeding ratio of 0.9, while Design B achieves Q = 8 but has a breeding ratio of 1.15. Which analysis correctly identifies the long-term viability issue?",
            "choices": {
                "A": "Design A is superior because higher Q always means better commercial performance",
                "B": "Design B is more viable long-term because a breeding ratio below 1.0 means Design A consumes more tritium than it produces, eventually running out of fuel regardless of its energy output",
                "C": "Both designs are equally viable because tritium can be purchased commercially",
                "D": "Design A's higher Q compensates for its lower breeding ratio over time"
            },
            "correct": "B",
            "feedback_correct": "Correct. A tritium breeding ratio below 1.0 means the reactor consumes more tritium than it creates. No matter how much energy it produces, Design A will eventually exhaust its fuel supply. Design B is self-sustaining in fuel production.",
            "feedback_incorrect": "A tritium breeding ratio below 1.0 is fatal to long-term operation. Tritium cannot be sourced naturally in useful quantities. Design A produces more energy per cycle but will run out of fuel, while Design B is fuel self-sufficient and can operate indefinitely."
        },
        {
            "question": "Based on the fusion reactor model, which conclusion about the relationship between energy output and wall material degradation is best supported by the simulation?",
            "choices": {
                "A": "Energy output and wall degradation are independent variables that can be optimized separately",
                "B": "Higher fusion energy output necessarily produces more neutrons, which cause more wall degradation, creating an inherent coupling where the energy source and the primary damage mechanism are products of the same nuclear reaction",
                "C": "Wall degradation can be eliminated by using alternative fusion fuels that produce no neutrons",
                "D": "Reducing energy output to zero is the only way to prevent wall degradation"
            },
            "correct": "B",
            "feedback_correct": "Correct. In D-T fusion, 80% of the energy is carried by the neutron. The very reaction that produces energy also produces the particles that damage the reactor. This inherent coupling means more power necessarily means more damage.",
            "feedback_incorrect": "Energy output and wall degradation are coupled by the physics of the D-T reaction: fusion produces helium AND a 14.1 MeV neutron that carries 80% of the energy. You cannot have the energy without the neutrons that cause structural damage."
        }
    ]
}

# =============================================================================
# L04: How Does a Neural Network Learn?
# NGSS: HS-ETS1-1, HS-ETS1-4
# =============================================================================
L04_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Backpropagation is the primary algorithm used to train neural networks. Which description best explains what backpropagation does?",
            "choices": {
                "A": "It forwards data through the network to produce a prediction",
                "B": "It calculates how much each connection weight contributed to the prediction error and adjusts weights to reduce that error",
                "C": "It randomly generates new connection weights after each training cycle",
                "D": "It removes neurons that produce incorrect outputs"
            },
            "correct": "B",
            "feedback_correct": "Correct. Backpropagation calculates the gradient of the error with respect to each weight, then adjusts weights in the direction that reduces the error. This process repeats millions of times to gradually improve the network's predictions.",
            "feedback_incorrect": "Backpropagation works backward from the output error, calculating each weight's contribution to that error, then adjusting weights to reduce the error. It is a systematic optimization process, not random or destructive."
        },
        {
            "question": "A neural network achieves 99% accuracy on its training data but only 60% accuracy on new, unseen data. Which concept best explains this discrepancy?",
            "choices": {
                "A": "The network needs more training time to improve on new data",
                "B": "Overfitting: the network memorized specific training examples rather than learning generalizable patterns",
                "C": "The new data contains errors that confuse the network",
                "D": "The network has too few layers to process new data types"
            },
            "correct": "B",
            "feedback_correct": "Correct. The large gap between training accuracy (99%) and validation accuracy (60%) is the hallmark of overfitting. The network memorized the training examples instead of learning the underlying patterns that would generalize to new data.",
            "feedback_incorrect": "This gap between training and validation performance is the classic signature of overfitting. The network essentially memorized answers rather than understanding patterns, like a student who memorizes test answers without understanding the concepts."
        },
        {
            "question": "Why does training data quality have a more significant impact on neural network fairness than network architecture?",
            "choices": {
                "A": "Network architecture determines the speed of training but not the quality of outputs",
                "B": "The network never sees the real world directly; it only learns patterns from whatever data humans provide, so biases in the data become biases in the model",
                "C": "Network architecture is always unbiased regardless of training data",
                "D": "Training data quality only affects accuracy, not fairness"
            },
            "correct": "B",
            "feedback_correct": "Correct. A neural network's understanding of the world is entirely derived from its training data. If the data underrepresents certain populations or encodes historical biases, the model will reproduce and potentially amplify those biases.",
            "feedback_incorrect": "Neural networks learn exclusively from their training data. They have no independent knowledge of the world. If training data is biased, incomplete, or unrepresentative, the model's outputs will reflect and potentially amplify those biases regardless of architecture."
        },
        {
            "question": "The learning rate is a critical hyperparameter in neural network training. What happens if the learning rate is set too high?",
            "choices": {
                "A": "The network trains more slowly but achieves higher accuracy",
                "B": "The network's weight adjustments are too large, causing it to overshoot optimal values and potentially never converge on a good solution",
                "C": "The network automatically adjusts the learning rate to compensate",
                "D": "Training data quality becomes less important at higher learning rates"
            },
            "correct": "B",
            "feedback_correct": "Correct. A learning rate that is too high causes weight updates that are too large, causing the optimization to oscillate wildly or diverge rather than converging on the optimal solution.",
            "feedback_incorrect": "When the learning rate is too high, each weight adjustment overshoots the optimum. Instead of gradually descending toward the best solution, the network bounces around or diverges, failing to learn effectively."
        },
        {
            "question": "Training GPT-4 reportedly cost over $100 million in computational resources. What does this reveal about the relationship between model capability and resource consumption in current AI development?",
            "choices": {
                "A": "The high cost indicates that the model is inefficient and should use fewer parameters",
                "B": "Current state-of-the-art performance relies on scaling data, parameters, and compute, creating an exponentially increasing resource demand that raises questions about sustainability and access",
                "C": "The cost is a one-time investment that does not recur for future models",
                "D": "More expensive models always produce proportionally better results"
            },
            "correct": "B",
            "feedback_correct": "Correct. The 'scaling paradigm' in AI achieves performance gains by increasing data, parameters, and compute, but each increment of improvement requires exponentially more resources, raising questions about sustainability, energy consumption, and who can afford to build frontier models.",
            "feedback_incorrect": "The enormous training cost reflects the scaling paradigm: bigger models with more data and compute produce better results, but the resource requirements grow exponentially. This raises fundamental questions about sustainability and whether only a few organizations can afford frontier AI."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's neural network model shows that increasing network depth from 5 to 20 layers improves pattern recognition accuracy from 75% to 92% but increases overfitting risk from 10% to 45%. What is the most scientifically sound interpretation of this trade-off?",
            "choices": {
                "A": "Deeper networks are always better because accuracy is the only metric that matters",
                "B": "The depth-accuracy relationship exhibits diminishing returns that are offset by accelerating overfitting risk, suggesting that optimal network design requires balancing representational power against generalization ability",
                "C": "The overfitting can be ignored if the training accuracy is high enough",
                "D": "Reducing depth to 1 layer would eliminate overfitting while maintaining accuracy"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals a nonlinear trade-off: accuracy gains diminish with depth while overfitting risk accelerates. Optimal design requires finding the depth that maximizes the gap between genuine pattern learning and memorization.",
            "feedback_incorrect": "The data shows diminishing accuracy returns (75% to 92%) against accelerating overfitting risk (10% to 45%). Optimal network design must balance the representational power of deeper networks against their tendency to memorize rather than generalize."
        },
        {
            "question": "In the model, a student trains two identical networks on the same task, one with a diverse, representative dataset and one with a dataset that overrepresents one demographic group. Both achieve 90% overall accuracy. Why does the second network pose a fairness problem despite equal overall accuracy?",
            "choices": {
                "A": "Overall accuracy masks performance disparities across subgroups; the biased network likely performs well on the overrepresented group and poorly on underrepresented groups",
                "B": "Both networks are equally fair because they have the same overall accuracy",
                "C": "The second network will naturally correct its bias through continued training",
                "D": "Demographic composition of training data does not affect neural network outputs"
            },
            "correct": "A",
            "feedback_correct": "Correct. Aggregate accuracy can hide severe disparities. A model trained on biased data may achieve 98% accuracy on the overrepresented group and 60% on others, averaging to 90% overall but performing unacceptably for underrepresented populations.",
            "feedback_incorrect": "Overall accuracy is a misleading metric when data is biased. The biased network likely achieves high accuracy on the overrepresented group and much lower accuracy on underrepresented groups, creating discriminatory performance that is hidden by the aggregate number."
        },
        {
            "question": "The model demonstrates that reducing the learning rate from 0.01 to 0.001 increases training time by 10x but reduces the loss function value by 30%. A student proposes using the higher learning rate to save time. What critical factor does this proposal overlook?",
            "choices": {
                "A": "Training time is the only relevant cost metric",
                "B": "The higher learning rate may cause the optimization to settle in a suboptimal local minimum or oscillate, while the lower rate's 30% better loss translates to meaningfully better real-world performance that justifies the computational investment",
                "C": "Learning rate has no effect on final model quality",
                "D": "The 10x time increase can be eliminated by using fewer training examples"
            },
            "correct": "B",
            "feedback_correct": "Correct. The 30% improvement in loss function represents meaningfully better pattern learning. The higher learning rate saves time but risks suboptimal convergence. The trade-off between training cost and model quality must be evaluated against the application's requirements.",
            "feedback_incorrect": "A higher learning rate often settles in suboptimal solutions because it overshoots better minima. The 30% loss improvement from the lower rate represents substantially better learning quality. For high-stakes applications, the 10x time investment may be essential."
        },
        {
            "question": "A student observes that their model's computational cost scales quadratically with the number of parameters but performance improvements scale logarithmically. What does this relationship predict about the long-term sustainability of the 'scale everything up' approach to AI?",
            "choices": {
                "A": "Scaling will always produce proportional improvements in performance",
                "B": "The widening gap between exponentially growing costs and diminishing performance returns suggests that scaling alone will eventually become economically and environmentally unsustainable, necessitating fundamental algorithmic breakthroughs",
                "C": "Hardware improvements will always keep pace with scaling demands",
                "D": "The logarithmic performance curve indicates that AI has reached its maximum capability"
            },
            "correct": "B",
            "feedback_correct": "Correct. When costs grow quadratically but returns grow logarithmically, each increment of improvement becomes dramatically more expensive. This divergence predicts that pure scaling will hit economic and environmental limits, requiring new approaches.",
            "feedback_incorrect": "The divergence between quadratic cost growth and logarithmic performance improvement means each additional unit of capability costs far more than the last. This trajectory is unsustainable and implies that continued AI progress will require algorithmic innovations, not just bigger models."
        },
        {
            "question": "Based on the neural network model, which conclusion about the relationship between training data volume and model generalization is best supported by the simulation?",
            "choices": {
                "A": "More training data always produces better generalization without any diminishing returns",
                "B": "Training data volume improves generalization with diminishing returns, and beyond a threshold, additional data quality and diversity matter more than volume because the model has already captured the primary patterns in the data distribution",
                "C": "Training data volume has no effect on generalization; only network architecture matters",
                "D": "Generalization decreases with more training data because the network becomes confused"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows diminishing returns from data volume. After the network captures the distribution's primary patterns, additional identical data provides little benefit. Data quality and diversity, ensuring all subgroups and edge cases are represented, become more important than raw volume.",
            "feedback_incorrect": "Data volume helps generalization but with diminishing returns. Once the primary patterns are learned, adding more data of the same type provides minimal benefit. At that point, data quality and diversity, covering edge cases and underrepresented scenarios, become the limiting factors."
        }
    ]
}

# =============================================================================
# L05: Can Synthetic Biology Create New Life?
# NGSS: HS-LS1-1, HS-LS3-1
# =============================================================================
L05_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Synthetic biologists design genetic circuits that function as biological logic gates. What does a genetic AND gate do in an engineered organism?",
            "choices": {
                "A": "It produces the output protein only when both molecular inputs are present simultaneously",
                "B": "It produces the output protein when either input is present",
                "C": "It blocks all protein production regardless of inputs",
                "D": "It copies the organism's natural genes into a synthetic chromosome"
            },
            "correct": "A",
            "feedback_correct": "Correct. Like an electronic AND gate, a biological AND gate requires both input signals (typically specific molecules or environmental conditions) to be present before activating gene expression and producing the output protein.",
            "feedback_incorrect": "A genetic AND gate functions like its electronic counterpart: it requires both molecular inputs to be present before the circuit activates gene expression. A single input alone is insufficient to produce the output."
        },
        {
            "question": "Why does metabolic burden threaten the long-term stability of engineered genetic circuits in synthetic organisms?",
            "choices": {
                "A": "Metabolic burden causes the organism to grow faster, overwhelming the laboratory containment",
                "B": "The synthetic circuit consumes cellular energy and resources, creating evolutionary pressure for mutations that disable the circuit because cells without the burden grow faster",
                "C": "Metabolic burden only affects organisms in natural environments, not in laboratories",
                "D": "The burden increases the organism's resistance to antibiotics"
            },
            "correct": "B",
            "feedback_correct": "Correct. Synthetic circuits divert energy from growth. Natural selection favors cells that mutate to disable the costly circuit, meaning evolution actively works to break engineered systems over generations.",
            "feedback_incorrect": "Metabolic burden means the synthetic circuit diverts resources from normal cell functions. Cells with mutations that break the circuit grow faster, and natural selection amplifies these mutants over generations. Evolution is actively working against the engineer's design."
        },
        {
            "question": "Craig Venter's team created JCVI-syn3.0, a synthetic organism with only 473 genes. What was the scientific significance of this achievement?",
            "choices": {
                "A": "It proved that organisms do not need DNA to survive",
                "B": "It established the minimal genome, the smallest set of genes required to sustain a free-living organism, revealing the minimum blueprint for life",
                "C": "It created the first organism that cannot evolve",
                "D": "It demonstrated that synthetic organisms are always more efficient than natural ones"
            },
            "correct": "B",
            "feedback_correct": "Correct. JCVI-syn3.0 identified the minimal set of genes necessary for independent life. This achievement established a baseline understanding of what is truly essential for a living cell to function.",
            "feedback_incorrect": "The significance was defining the minimal genome: the fewest genes needed for a free-living cell. With 473 genes (compared to thousands in natural bacteria), this experiment identified the essential blueprint for life."
        },
        {
            "question": "Biocontainment strategies are engineered into synthetic organisms for safety. Which approach would be most effective at preventing environmental escape?",
            "choices": {
                "A": "Making the organism grow as fast as possible so it outcompetes natural organisms",
                "B": "Engineering dependence on synthetic amino acids that do not exist in nature, so the organism cannot survive outside the laboratory",
                "C": "Removing all antibiotic resistance genes from the organism",
                "D": "Making the organism bioluminescent so it can be easily tracked"
            },
            "correct": "B",
            "feedback_correct": "Correct. Creating dependence on synthetic nutrients not found in nature makes environmental survival effectively impossible. The organism cannot obtain the required nutrient outside the laboratory, making escape nonviable.",
            "feedback_incorrect": "The most effective containment creates a hard biological dependency. Engineering the organism to require synthetic amino acids that do not exist in nature means it cannot survive outside controlled conditions, regardless of mutations to other systems."
        },
        {
            "question": "Why is evolution considered both a tool and a threat in synthetic biology?",
            "choices": {
                "A": "Evolution only creates beneficial mutations in synthetic organisms",
                "B": "Evolution can be used to optimize engineered organisms through directed evolution, but it also generates random mutations that can disable engineered circuits, defeat containment, or create unpredicted behaviors",
                "C": "Synthetic organisms cannot evolve because their DNA is artificial",
                "D": "Evolution only affects natural organisms in the wild, not laboratory-grown organisms"
            },
            "correct": "B",
            "feedback_correct": "Correct. Directed evolution is a powerful tool for optimizing synthetic organisms, but uncontrolled evolution generates random mutations that may break engineered functions, defeat safety mechanisms, or produce unexpected behaviors.",
            "feedback_incorrect": "Evolution is a double-edged sword. Scientists harness it through directed evolution to optimize circuits, but spontaneous mutations constantly test engineered designs. Any mutation that reduces metabolic burden will be selected for, potentially disabling the engineered function."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's model shows that a simple biosensor circuit (2 genes) maintains function for 500 generations, while a complex metabolic pathway circuit (12 genes) loses function within 50 generations. What principle of evolutionary stability does this demonstrate?",
            "choices": {
                "A": "More complex circuits are always better because they have more redundancy",
                "B": "Circuit complexity and evolutionary stability are inversely related because more genes create more mutational targets, and the greater metabolic burden of complex circuits increases the selective advantage of loss-of-function mutations",
                "C": "The complex circuit failed because it contained design errors, not because of evolutionary pressure",
                "D": "Simple circuits always outperform complex circuits in all applications"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates an inverse relationship: complexity increases both the number of mutational targets and the metabolic burden. Together, these factors dramatically accelerate the rate at which evolution disables engineered functions.",
            "feedback_incorrect": "The 10x difference in stability directly reflects the complexity-stability trade-off. More genes means more targets for disabling mutations, and greater metabolic burden means stronger selection for those mutations. Evolution breaks complex circuits faster because they are costlier to maintain."
        },
        {
            "question": "In the model, a student increases biocontainment strength by adding a second independent kill switch. The single kill switch had an escape frequency of 10^-6 per generation; the dual system has 10^-12. Why does this dual system provide disproportionately better containment?",
            "choices": {
                "A": "Two kill switches consume less metabolic energy than one",
                "B": "The probability of simultaneously defeating two independent safety mechanisms is the product of their individual defeat probabilities, making dual containment exponentially rather than additively more secure",
                "C": "The second kill switch corrects errors made by the first",
                "D": "Dual systems prevent all mutations from occurring in the organism"
            },
            "correct": "B",
            "feedback_correct": "Correct. Independent safety mechanisms multiply their reliability. If each has a 10^-6 failure rate, defeating both requires both failures to occur simultaneously: 10^-6 x 10^-6 = 10^-12. This multiplicative security is a fundamental principle of layered containment.",
            "feedback_incorrect": "Independent containment systems provide multiplicative, not additive, security. The probability of defeating both is the product of defeating each individually (10^-6 x 10^-6 = 10^-12), making layered containment exponentially more secure."
        },
        {
            "question": "The model reveals that output fidelity (precision of the genetic circuit) decreases as the cell's growth rate increases. A student proposes solving this by engineering a faster-growing host cell. Why would this approach likely worsen the problem?",
            "choices": {
                "A": "Faster-growing cells have smaller genomes that cannot support synthetic circuits",
                "B": "Faster growth increases the competition between natural and synthetic gene expression for limited cellular resources, intensifying the metabolic burden and further reducing circuit fidelity",
                "C": "Growth rate and fidelity are independent variables in the model",
                "D": "Faster-growing cells eliminate all mutations through more frequent DNA replication"
            },
            "correct": "B",
            "feedback_correct": "Correct. Faster growth demands more cellular resources for natural functions, leaving fewer for the synthetic circuit. This intensifies the metabolic conflict and reduces the precision of the engineered output.",
            "feedback_incorrect": "Faster growth means the cell allocates more resources to its own replication, intensifying competition with the synthetic circuit for ribosomes, amino acids, and ATP. This increases metabolic burden and reduces circuit fidelity rather than improving it."
        },
        {
            "question": "A student's model shows that an engineered organism designed to produce biofuel maintains 95% output in generation 1 but only 40% by generation 100. The student identifies three mutations in the circuit. Which analysis best explains the trajectory?",
            "choices": {
                "A": "The mutations are random and would have occurred regardless of the circuit's metabolic cost",
                "B": "Natural selection progressively enriched loss-of-function mutations because cells with reduced circuit output grew faster, and each mutation was additively selected, creating a compounding decline in engineered function",
                "C": "The organism developed immunity to its own biofuel product",
                "D": "The laboratory conditions degraded over 100 generations, not the organism"
            },
            "correct": "B",
            "feedback_correct": "Correct. Each mutation that partially disables the costly circuit gives those cells a growth advantage. Natural selection amplifies these mutants, and as multiple mutations accumulate, the engineered output declines progressively. This is evolution actively optimizing against the engineered design.",
            "feedback_incorrect": "The decline follows a predictable pattern of evolutionary erosion. Each loss-of-function mutation reduces metabolic burden, giving mutant cells a growth advantage. Over generations, natural selection enriches these mutants, and as mutations accumulate, circuit output compounds downward."
        },
        {
            "question": "Based on the synthetic biology model, which conclusion about the fundamental tension between engineering control and biological evolution is best supported by the simulation data?",
            "choices": {
                "A": "Engineered organisms can be designed to be completely immune to evolutionary change",
                "B": "Evolution is the most powerful force acting on synthetic organisms: any engineered function that imposes metabolic cost will be under constant selective pressure, making long-term stability achievable only through designs that either minimize burden or align engineered function with the organism's fitness",
                "C": "Evolution has no effect on synthetic organisms because their DNA is artificial",
                "D": "All synthetic circuits will maintain function indefinitely if the laboratory conditions are kept constant"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model consistently demonstrates that evolution pressures synthetic circuits proportionally to their metabolic cost. Sustainable designs must either minimize burden or create circuits that benefit the organism's fitness, aligning engineering goals with evolutionary incentives.",
            "feedback_incorrect": "The fundamental lesson is that evolution cannot be defeated, only managed. Circuits that impose metabolic cost will face constant selective pressure. The only durable strategies are minimizing burden or designing circuits where engineered function and organismal fitness are aligned."
        }
    ]
}

# =============================================================================
# L06: Can We Capture Carbon from Thin Air?
# NGSS: HS-ESS3-4, HS-PS1-4, HS-ETS1-3
# =============================================================================
L06_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "CO2 exists at approximately 420 parts per million (ppm) in the atmosphere. Why does this low concentration make direct air capture significantly more energy-intensive than capturing CO2 from power plant exhaust?",
            "choices": {
                "A": "Power plant exhaust contains no CO2, making it easier to process",
                "B": "At 420 ppm, CO2 is extremely dilute compared to exhaust gases at ~120,000 ppm, and thermodynamics requires exponentially more energy to separate increasingly dilute components from a mixture",
                "C": "Direct air capture equipment is always less efficient than industrial capture equipment",
                "D": "The atmosphere contains pollutants that block CO2 capture"
            },
            "correct": "B",
            "feedback_correct": "Correct. Thermodynamics dictates that separating a dilute component from a mixture requires more energy as the concentration decreases. CO2 in air is ~300x more dilute than in exhaust, making air capture fundamentally more energy-intensive.",
            "feedback_incorrect": "The challenge is thermodynamic: separating a substance from a dilute mixture requires more energy than from a concentrated one. At 420 ppm, CO2 in air is nearly 300 times more dilute than in power plant exhaust (~120,000 ppm), demanding proportionally more energy."
        },
        {
            "question": "A direct air capture system powered by natural gas captures 1,000 tonnes of CO2 per year but the gas combustion emits 400 tonnes of CO2. What is the net carbon removal?",
            "choices": {
                "A": "1,000 tonnes because only captured CO2 counts",
                "B": "600 tonnes because the system's own emissions must be subtracted from gross capture to determine actual atmospheric CO2 reduction",
                "C": "1,400 tonnes because both captured and emitted CO2 should be counted as removed",
                "D": "0 tonnes because any fossil fuel use invalidates the capture"
            },
            "correct": "B",
            "feedback_correct": "Correct. Net carbon removal equals gross capture minus all system emissions. If the DAC system emits 400 tonnes while capturing 1,000, the net removal is 600 tonnes. This is why energy source carbon intensity is a critical design variable.",
            "feedback_incorrect": "Net removal accounts for the full carbon budget of the system. Gross capture (1,000 tonnes) minus system emissions (400 tonnes) yields 600 tonnes of net removal. Ignoring system emissions would overstate the climate benefit."
        },
        {
            "question": "The thermodynamic minimum energy required to separate CO2 from air at 420 ppm is approximately 250 kWh per tonne. Current DAC systems require 1,000-2,500 kWh per tonne. What explains this gap?",
            "choices": {
                "A": "Current systems violate the laws of thermodynamics",
                "B": "Real systems have engineering inefficiencies including heat losses, fan power, sorbent degradation, and incomplete CO2 release during regeneration that increase energy requirements 3-5x above the theoretical minimum",
                "C": "The thermodynamic minimum calculation is incorrect",
                "D": "Current systems capture more CO2 than intended, using extra energy"
            },
            "correct": "B",
            "feedback_correct": "Correct. The thermodynamic minimum represents a theoretical floor under perfect conditions. Real engineering systems face unavoidable losses from heat transfer, air movement, sorbent cycling, and regeneration inefficiency that multiply the actual energy requirement.",
            "feedback_incorrect": "The gap between theoretical and actual energy use reflects real-world engineering losses. No system achieves 100% efficiency: fans require power, heat is lost during sorbent regeneration, sorbents degrade over cycles, and CO2 is not fully released. These compound to 3-5x the theoretical minimum."
        },
        {
            "question": "Why is the energy source used to power a direct air capture system the single most important variable in determining whether the system actually reduces atmospheric CO2?",
            "choices": {
                "A": "Renewable energy is cheaper than fossil energy for all applications",
                "B": "If the energy source emits CO2 (e.g., fossil fuels), those emissions can partially or completely negate the CO2 captured, potentially making the system a net emitter rather than a net remover",
                "C": "The energy source determines the physical location of the DAC facility",
                "D": "Only nuclear energy produces enough power for DAC systems"
            },
            "correct": "B",
            "feedback_correct": "Correct. A fossil-powered DAC system could emit more CO2 from its energy source than it captures from the air, creating a net positive emission rather than net removal. The carbon intensity of the energy source directly determines whether DAC helps or harms.",
            "feedback_incorrect": "The energy source's carbon intensity is critical because it can negate or exceed the CO2 captured. A coal-powered DAC system could theoretically emit more CO2 from combustion than it removes from the air, making it counterproductive."
        },
        {
            "question": "Humanity emits approximately 37 gigatonnes of CO2 per year. If each DAC facility captures 4,000 tonnes per year (like Climeworks' Orca plant), approximately how many facilities would be needed to capture just 1% of annual emissions?",
            "choices": {
                "A": "About 370 facilities",
                "B": "About 9,250 facilities",
                "C": "About 92,500 facilities",
                "D": "About 925,000 facilities"
            },
            "correct": "C",
            "feedback_correct": "Correct. 1% of 37 gigatonnes = 370 million tonnes. At 4,000 tonnes per facility, that requires 92,500 facilities. This calculation reveals the enormous scale challenge: even 1% of emissions requires tens of thousands of industrial-scale plants.",
            "feedback_incorrect": "The math: 1% of 37 Gt = 0.37 Gt = 370,000,000 tonnes. Divided by 4,000 tonnes per facility = 92,500 facilities. This reveals the daunting scale challenge that makes DAC a supplement to, not a replacement for, emissions reduction."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's DAC model shows that switching from natural gas power to 100% renewable energy increases net carbon removal from 600 to 1,000 tonnes per year (per facility) but increases capture cost from $400 to $550 per tonne. What is the most complete analysis of this trade-off?",
            "choices": {
                "A": "The cost increase makes renewable-powered DAC economically nonviable",
                "B": "The renewable system removes 67% more net CO2 per facility despite costing 38% more per tonne, and the fossil-powered system's lower cost is misleading because it includes 400 tonnes of self-generated emissions that the cost per tonne does not reflect",
                "C": "Cost per tonne is the only metric that matters for evaluating DAC systems",
                "D": "Both systems are equally effective because they use the same capture technology"
            },
            "correct": "B",
            "feedback_correct": "Correct. Cost per tonne alone is misleading without accounting for net removal. The renewable system captures more net CO2 per dollar of total investment because it eliminates the 400 tonnes of self-generated emissions that reduce the fossil system's actual climate impact.",
            "feedback_incorrect": "The analysis must compare net removal, not gross capture or cost alone. The fossil system's apparent cost advantage disappears when you account for its 400 tonnes of self-generated emissions. Per net tonne removed, the renewable system is actually more cost-effective."
        },
        {
            "question": "The model demonstrates that sorbent efficiency degrades by 2% per cycle over thousands of regeneration cycles. After 500 cycles, what is the cumulative impact on system performance, and what does this imply for operational planning?",
            "choices": {
                "A": "2% per cycle is negligible and can be ignored over any number of cycles",
                "B": "After 500 cycles at 2% degradation per cycle, the sorbent has lost substantial capacity, requiring periodic replacement that adds to operational costs and creates secondary waste streams that must be factored into the system's life-cycle carbon footprint",
                "C": "The sorbent improves with use as it becomes more selective for CO2",
                "D": "Degradation stops after the first 100 cycles as the sorbent reaches equilibrium"
            },
            "correct": "B",
            "feedback_correct": "Correct. Cumulative degradation means sorbent replacement is a recurring operational cost. The replacement schedule, disposal/recycling of spent sorbent, and the carbon footprint of manufacturing new sorbent must all be included in the system's true cost and environmental analysis.",
            "feedback_incorrect": "Sorbent degradation is cumulative and creates a maintenance cycle: periodic replacement adds cost, generates waste, and requires manufacturing new sorbent (with its own carbon footprint). Life-cycle analysis must include these recurring costs."
        },
        {
            "question": "A student models the land use required for DAC at gigatonne scale and finds that powering the systems with solar energy would require solar farms covering an area the size of a small state. Another student argues this makes DAC impractical. Which response best evaluates this claim?",
            "choices": {
                "A": "The claim is correct; DAC should be abandoned due to land requirements",
                "B": "The land use concern is valid and represents a real constraint, but must be compared against the land use of alternative carbon removal strategies (reforestation, BECCS) and evaluated alongside the land impact of unmitigated climate change, which threatens far more land through desertification and sea level rise",
                "C": "Land use is irrelevant because solar panels can be placed on existing buildings",
                "D": "The calculation must be wrong because no technology requires that much land"
            },
            "correct": "B",
            "feedback_correct": "Correct. Land use is a legitimate constraint but must be evaluated comparatively. Reforestation for equivalent CO2 removal requires even more land, and unmitigated climate change threatens vastly more land through environmental degradation. No carbon removal option is free of trade-offs.",
            "feedback_incorrect": "The analysis requires comparison: what is the land footprint of alternative approaches? Reforestation for equivalent removal requires 5-10x more land. And unmitigated climate change threatens far more land. DAC's land use is a valid constraint but not a unique disqualification."
        },
        {
            "question": "The model shows that DAC capture cost follows a learning curve: costs decrease by 15% for every doubling of cumulative installed capacity. Current costs are $600/tonne at 0.01 Mt/year capacity. Approximately what cost per tonne would the model predict at 10 Mt/year capacity (roughly 10 doublings)?",
            "choices": {
                "A": "$600/tonne because costs are fixed by thermodynamics",
                "B": "Approximately $120/tonne, applying the 15% cost reduction across approximately 10 doublings of capacity (0.85^10 x $600)",
                "C": "$0/tonne because enough scale eliminates all costs",
                "D": "$6,000/tonne because costs increase with scale"
            },
            "correct": "B",
            "feedback_correct": "Correct. Learning curve economics: 0.85^10 = approximately 0.20, so costs would fall to roughly $120/tonne. This is optimistic but grounded in observed learning rates for analogous technologies. However, the thermodynamic minimum sets a floor below which costs cannot fall.",
            "feedback_incorrect": "Learning curve analysis: each doubling reduces cost by 15% (multiply by 0.85). After 10 doublings: $600 x 0.85^10 = approximately $120/tonne. This assumes the historical learning rate holds, though the thermodynamic minimum energy cost sets a permanent floor."
        },
        {
            "question": "Based on the DAC model, which conclusion about the role of direct air capture in climate strategy is best supported by the simulation data?",
            "choices": {
                "A": "DAC can replace emissions reduction as the primary climate strategy because it removes CO2 directly",
                "B": "DAC is a necessary complement to emissions reduction, not a substitute: the scale, cost, and energy requirements make it capable of addressing residual and historical emissions but incapable of keeping pace with current emission rates without dramatic emissions cuts first",
                "C": "DAC is too expensive to ever play a meaningful role in climate strategy",
                "D": "DAC should only be deployed after all fossil fuel use has been eliminated"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that DAC cannot scale fast enough or cheaply enough to offset 37 Gt/year of ongoing emissions. Its role is addressing hard-to-abate sectors and historical emissions after aggressive emissions reduction brings the remaining gap to a manageable scale.",
            "feedback_incorrect": "The model shows that DAC's current cost and energy requirements make it unable to match the scale of ongoing emissions. It is most valuable as a complement to emissions reduction, addressing residual emissions from hard-to-decarbonize sectors and drawing down historical atmospheric CO2."
        }
    ]
}

# =============================================================================
# L07: How Do Self-Driving Cars See?
# NGSS: HS-PS4-1, HS-ETS1-2
# =============================================================================
L07_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "LiDAR generates a 3D point cloud of the vehicle's surroundings. What physical principle does LiDAR use to measure distance to objects?",
            "choices": {
                "A": "It measures the color of reflected light to estimate distance",
                "B": "It emits laser pulses and measures the time each pulse takes to bounce back from objects, using the speed of light to calculate distance",
                "C": "It uses sound waves like sonar to detect nearby objects",
                "D": "It detects the magnetic field of metallic objects in the environment"
            },
            "correct": "B",
            "feedback_correct": "Correct. LiDAR is based on time-of-flight measurement: a laser pulse is emitted, bounces off an object, and returns. Since light travels at a known constant speed, the round-trip time directly determines the distance.",
            "feedback_incorrect": "LiDAR uses time-of-flight: it emits laser pulses and measures the time for each pulse to return. Since the speed of light is known, the round-trip time yields precise distance. This creates a detailed 3D point cloud of the environment."
        },
        {
            "question": "Why do autonomous vehicles use sensor fusion rather than relying on a single sensor type?",
            "choices": {
                "A": "Using multiple sensors is required by government regulations",
                "B": "Each sensor type has different strengths and weaknesses: LiDAR provides precise 3D mapping but no color, cameras provide color and texture but poor depth, and radar works in bad weather but has low resolution. Combining them creates a more complete and reliable environmental model",
                "C": "Multiple sensors are cheaper than a single high-quality sensor",
                "D": "Sensor fusion eliminates all processing latency"
            },
            "correct": "B",
            "feedback_correct": "Correct. No single sensor is sufficient for all conditions. Sensor fusion exploits each sensor's strengths while compensating for its weaknesses, creating a unified model that is more accurate and reliable than any individual sensor.",
            "feedback_incorrect": "Sensor fusion addresses the limitations of individual sensors. LiDAR excels at 3D mapping but fails in heavy rain; cameras detect color and signs but struggle in darkness; radar penetrates weather but has low resolution. Combining them creates redundancy and reliability."
        },
        {
            "question": "At 65 mph, a vehicle travels approximately 100 feet per second. If the perception-to-action pipeline takes 300 milliseconds, what is the practical safety implication?",
            "choices": {
                "A": "The delay is too short to matter at any speed",
                "B": "The vehicle travels approximately 30 feet before it can respond to newly detected information, creating a fundamental gap between sensing reality and acting on it that grows with speed",
                "C": "The vehicle automatically stops during the processing time",
                "D": "The 300 milliseconds only applies to the braking system, not steering"
            },
            "correct": "B",
            "feedback_correct": "Correct. At 100 feet/second, 300ms of processing means the car moves 30 feet 'blind' to new information. This latency gap is a fundamental safety constraint that must be compensated for through predictive algorithms and conservative speed management.",
            "feedback_incorrect": "Processing latency creates a distance gap: at 65 mph (100 ft/s), 300ms means the car travels 30 feet before it can respond to new sensor data. This gap grows with speed and represents a fundamental challenge for autonomous vehicle safety design."
        },
        {
            "question": "Object classification in autonomous vehicles must distinguish between a pedestrian and a mailbox, or a bicycle and a motorcycle. Why is this task particularly challenging for machine learning systems?",
            "choices": {
                "A": "All objects look identical to LiDAR sensors",
                "B": "The system must correctly classify objects it may have never seen before in training data, handle partial occlusion, unusual angles, and novel combinations of conditions, all within milliseconds at highway speeds",
                "C": "Classification only needs to distinguish between two categories: obstacles and non-obstacles",
                "D": "Machine learning systems always classify objects with 100% accuracy"
            },
            "correct": "B",
            "feedback_correct": "Correct. Real-world driving presents an open-ended set of objects, conditions, and scenarios that no training dataset can fully cover. The system must handle novel situations, partial views, and edge cases at extreme speed, making perfect classification fundamentally impossible.",
            "feedback_incorrect": "Classification in driving is an open-world problem: the system encounters objects, conditions, and combinations not in its training data. A child in an unusual costume, a fallen tree, or a wheelchair user may not match any learned category. This uncertainty, combined with time pressure, is the core challenge."
        },
        {
            "question": "Rain, fog, and sun glare all degrade autonomous vehicle sensor performance. Which sensor is most affected by heavy rain, and why?",
            "choices": {
                "A": "Radar, because water absorbs radio waves",
                "B": "LiDAR, because water droplets scatter the laser beams and create false returns that corrupt the point cloud data",
                "C": "GPS, because rain clouds block satellite signals",
                "D": "Cameras, because raindrops on the lens block all visual input permanently"
            },
            "correct": "B",
            "feedback_correct": "Correct. LiDAR laser beams are scattered by water droplets in heavy rain, creating false distance measurements (noise) in the point cloud. This degrades the 3D map quality and can cause missed or phantom object detections.",
            "feedback_incorrect": "Heavy rain scatters LiDAR laser pulses, creating false returns from water droplets that appear as noise in the point cloud. This corrupts the 3D environmental model. Radar, by contrast, is relatively unaffected by rain because radio waves pass through water droplets."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's model shows that increasing LiDAR resolution from 100 to 400 points per square meter improves object detection by 25% but increases processing latency from 150ms to 350ms. At 65 mph, what is the safety implication of this trade-off?",
            "choices": {
                "A": "Higher resolution is always safer because detection is more accurate",
                "B": "The improved detection is offset by increased latency: the vehicle now travels 35 feet instead of 15 feet before responding, meaning the system detects objects better but reacts to them slower, potentially creating a net decrease in safety at highway speeds",
                "C": "Processing latency has no effect on safety if detection accuracy is high",
                "D": "The vehicle should switch to camera-only mode at high speeds"
            },
            "correct": "B",
            "feedback_correct": "Correct. Better detection is meaningless if the response comes too late. The 200ms increase in latency adds 20 feet of travel before response. Optimal system design must balance detection quality against response time for the given speed envelope.",
            "feedback_incorrect": "Detection accuracy and response speed are coupled safety factors. The additional 200ms latency means the vehicle travels an extra 20 feet before reacting. At highway speeds, the faster but less detailed system may actually be safer because it responds sooner."
        },
        {
            "question": "The model demonstrates that sensor fusion confidence drops sharply when LiDAR and camera disagree about an object's classification. A LiDAR return suggests a large solid object, but the camera classifies it as a plastic bag. How should the decision algorithm handle this conflict?",
            "choices": {
                "A": "Always trust the camera because it provides richer visual information",
                "B": "The system should apply a conservative safety hierarchy: treat the object as the more dangerous interpretation (solid obstacle) until additional sensor data or time resolves the conflict, because the cost of hitting a solid object far exceeds the cost of briefly avoiding a plastic bag",
                "C": "Average the two sensor readings to create a compromise classification",
                "D": "Ignore both sensors and maintain current speed and direction"
            },
            "correct": "B",
            "feedback_correct": "Correct. Asymmetric risk demands conservative decision-making. Misclassifying a solid object as a bag could be fatal, while briefly treating a bag as a solid object merely causes a momentary slowdown. The cost of being wrong differs dramatically between the two errors.",
            "feedback_incorrect": "When sensors disagree, the system must consider the asymmetric consequences of each possible error. Treating a bag as a rock causes a brief inconvenience; treating a rock as a bag could cause a fatal collision. Conservative classification, defaulting to the more dangerous interpretation, is the safety-rational approach."
        },
        {
            "question": "A student observes that the model's decision algorithm performs well in scenarios represented in its training data but fails unpredictably in novel situations (e.g., a fallen tree across the road). What fundamental limitation of machine-learning-based decision systems does this reveal?",
            "choices": {
                "A": "The algorithm needs more processing power to handle novel scenarios",
                "B": "Machine learning systems can only reliably handle situations similar to their training data; truly novel scenarios that fall outside the training distribution expose the system's inability to reason from first principles, unlike human drivers who can improvise",
                "C": "All novel scenarios can be solved by adding more training data",
                "D": "The algorithm should ignore novel scenarios and continue driving normally"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is the 'long tail' problem in autonomous driving. ML systems excel at pattern matching within their training distribution but cannot reason about genuinely novel situations. This limitation is why fully autonomous driving in all conditions remains unsolved.",
            "feedback_incorrect": "The fundamental issue is distribution shift: ML systems perform well within their training distribution but degrade unpredictably on novel inputs. Human drivers can reason about unfamiliar situations using general knowledge, but current AI systems lack this ability, creating the 'long tail' of rare but critical edge cases."
        },
        {
            "question": "The model shows that Environmental Degradation (heavy rain) reduces LiDAR range by 40%, camera detection by 60%, but radar by only 5%. What does this demonstrate about the critical role of sensor diversity in the system?",
            "choices": {
                "A": "The vehicle should only use radar and eliminate LiDAR and cameras",
                "B": "Sensor diversity provides graceful degradation: when weather impairs optical sensors, radar maintains environmental awareness, preventing complete perception failure. No single sensor type is optimal in all conditions, making diversity a safety requirement rather than a luxury",
                "C": "Heavy rain makes autonomous driving completely impossible regardless of sensors",
                "D": "The degradation percentages are too small to affect driving safety"
            },
            "correct": "B",
            "feedback_correct": "Correct. The asymmetric impact of rain across sensor types demonstrates why diversity is essential. Radar's weather resilience compensates for optical sensor degradation, maintaining minimum perception capability. Eliminating any sensor type would create conditions where the system is blind.",
            "feedback_incorrect": "Sensor diversity provides resilience through complementary failure modes. Rain severely degrades optical sensors but barely affects radar. Without sensor diversity, a single weather condition could eliminate all perception. The system degrades gracefully rather than catastrophically."
        },
        {
            "question": "Based on the autonomous vehicle model, which conclusion about the relationship between safety margin and processing latency is best supported by the simulation data?",
            "choices": {
                "A": "Safety margin is independent of processing latency at all speeds",
                "B": "Safety margin decreases proportionally with both increasing speed and increasing processing latency, because the distance traveled during processing time is the product of speed and latency. This means safety-critical decisions are fundamentally constrained by computation speed, and faster algorithms directly translate to safer vehicles",
                "C": "Safety margin only depends on the driver's reaction time, not the computer's processing time",
                "D": "Reducing speed to zero is the only way to ensure an adequate safety margin"
            },
            "correct": "B",
            "feedback_correct": "Correct. The blind distance (speed x latency) directly determines the minimum safety margin. This mathematical relationship means that improving processing speed has a direct, quantifiable safety benefit that increases with vehicle speed.",
            "feedback_incorrect": "Safety margin = available stopping distance minus blind distance (speed x latency). As speed or latency increases, the blind distance grows and the safety margin shrinks. Faster processing directly and proportionally improves safety at any given speed."
        }
    ]
}

# =============================================================================
# L08: Can We 3D-Print a Human Organ?
# NGSS: HS-LS1-2, HS-ETS1-2
# =============================================================================
L08_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "The 200-micrometer nutrient diffusion limit is the most critical constraint in bioprinting. What does this limit mean for tissue engineering?",
            "choices": {
                "A": "Cells cannot be printed smaller than 200 micrometers in diameter",
                "B": "Every cell in bioprinted tissue must be within 200 micrometers of a blood capillary or nutrient source, or it will die from oxygen and nutrient deprivation within hours",
                "C": "Bioprinted tissues cannot exceed 200 micrometers in total width",
                "D": "The printer nozzle cannot be smaller than 200 micrometers"
            },
            "correct": "B",
            "feedback_correct": "Correct. Oxygen and nutrients can only diffuse approximately 200 micrometers through tissue before being consumed. Beyond this distance, cells die. This is why vascularization, creating blood vessel networks, is the central challenge of printing thick tissues.",
            "feedback_incorrect": "The diffusion limit means cells cannot survive beyond 200 micrometers from a nutrient source. In native tissue, capillaries ensure every cell is within this distance. Without engineered blood vessel networks, bioprinted tissue thicker than ~400 micrometers will develop a necrotic core."
        },
        {
            "question": "Why is vascularization considered the single greatest challenge in bioprinting functional organs?",
            "choices": {
                "A": "Blood vessels are made of only one cell type, making them simple but fragile",
                "B": "Organs like the kidney contain over 100 miles of blood vessels reaching every functional unit, and replicating this density and complexity at the capillary scale with current printing technology is beyond our resolution",
                "C": "Vascularization is only needed for organs larger than the heart",
                "D": "Blood vessels cannot be made from the patient's own cells"
            },
            "correct": "B",
            "feedback_correct": "Correct. The complexity and density of native vascular networks is staggering. A human kidney contains ~100 miles of blood vessels branching down to capillary scale. Printing this network at the required resolution while maintaining cell viability is the defining engineering challenge.",
            "feedback_incorrect": "Native organs have extraordinarily dense vascular networks. Replicating networks that branch from arteries down to capillaries at ~10-micrometer scale, while maintaining cell viability during the printing process, exceeds current bioprinting resolution by orders of magnitude."
        },
        {
            "question": "Bioink must balance multiple competing requirements during the printing process. Which property conflict is most challenging to resolve?",
            "choices": {
                "A": "Color versus transparency of the printed material",
                "B": "The bioink must be viscous enough to hold its shape during printing but soft enough that cells survive the shear stress of being pushed through the print nozzle",
                "C": "The bioink must be both hot and cold simultaneously",
                "D": "The bioink must contain both living cells and plastic polymers"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is the central bioink dilemma: structural integrity requires high viscosity (stiff material), but cell viability requires low shear stress (soft material). These requirements directly conflict, and finding the optimal balance is a core engineering challenge.",
            "feedback_incorrect": "The bioink paradox: it must be stiff enough to maintain its printed shape (high viscosity) yet gentle enough that cells survive the mechanical forces of extrusion (low shear stress). These requirements are fundamentally in tension."
        },
        {
            "question": "After printing, bioprinted tissue requires weeks to months of maturation in a bioreactor. What happens during this maturation period?",
            "choices": {
                "A": "The printer continues to add new layers to the construct",
                "B": "Cells proliferate, form cell-cell junctions, deposit extracellular matrix, and develop the mechanical and functional properties of native tissue",
                "C": "The scaffold material is injected with drugs to prevent rejection",
                "D": "The construct is frozen to preserve it for future transplantation"
            },
            "correct": "B",
            "feedback_correct": "Correct. Immediately after printing, tissue is structurally and functionally immature. During maturation, cells establish connections, produce their own structural matrix, and develop specialized functions. A bioprinted heart patch must learn to contract rhythmically during this period.",
            "feedback_incorrect": "Maturation is the period where printed cells transition from a passive arrangement to an active, functional tissue. Cells multiply, establish junctions, produce extracellular matrix, and develop specialized tissue-specific functions like contraction or secretion."
        },
        {
            "question": "Using a patient's own cells (autologous cells) for bioprinting eliminates immune rejection but creates a different challenge. What is it?",
            "choices": {
                "A": "Autologous cells cannot survive the printing process",
                "B": "Growing sufficient quantities of a patient's cells requires weeks of cell culture, creating a time constraint that is incompatible with emergency transplantation needs",
                "C": "Autologous cells are always of lower quality than donor cells",
                "D": "Autologous cells cannot differentiate into specialized cell types"
            },
            "correct": "B",
            "feedback_correct": "Correct. While autologous cells eliminate rejection, the weeks required to culture enough cells from a small biopsy mean this approach cannot serve patients who need immediate transplantation. This creates a trade-off between immune compatibility and time-to-treatment.",
            "feedback_incorrect": "The trade-off is time versus compatibility. Autologous cells provide perfect immune matching but require weeks of culture to reach sufficient quantities. For patients deteriorating rapidly on transplant waiting lists, this timeline may be too long."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's bioprinting model shows that increasing print resolution from 200 to 50 micrometers improves tissue architecture fidelity by 60% but reduces cell viability from 90% to 65% due to increased shear stress. How should this trade-off be evaluated?",
            "choices": {
                "A": "Higher resolution is always preferable because tissue architecture determines function",
                "B": "The trade-off reveals that better structural precision comes at the cost of cell survival; a construct with beautiful architecture but 35% dead cells may fail to function. Optimal resolution must balance structural fidelity against the minimum cell viability required for tissue function",
                "C": "Cell viability is unimportant because dead cells will be replaced by living ones",
                "D": "The 50-micrometer resolution should be used for all tissue types regardless of viability impact"
            },
            "correct": "B",
            "feedback_correct": "Correct. Architecture is meaningless if cells die. The optimal print resolution varies by tissue type: complex organs may need 50-micrometer precision, but only if cell viability remains above the threshold for functional maturation.",
            "feedback_incorrect": "Resolution and viability are coupled through shear stress. Finer printing requires smaller nozzles, generating more shear force. The optimal resolution is tissue-specific: some tissues require architectural precision, others prioritize cell survival. Neither variable can be maximized independently."
        },
        {
            "question": "The model shows that scaffold degradation rate must match the rate of cell-produced extracellular matrix deposition. If the scaffold degrades faster than cells produce matrix, what is the structural consequence?",
            "choices": {
                "A": "The construct becomes stronger because cells compensate by producing more matrix",
                "B": "The construct collapses because the supporting scaffold disappears before cells have produced sufficient structural matrix to maintain the tissue's shape and mechanical integrity",
                "C": "Faster scaffold degradation improves nutrient diffusion and cell survival",
                "D": "The degradation rate has no effect on construct integrity after printing"
            },
            "correct": "B",
            "feedback_correct": "Correct. The scaffold provides mechanical support during maturation. If it degrades before cells produce their own structural matrix, the construct loses its shape and collapses. Matching these rates is critical for successful tissue engineering.",
            "feedback_incorrect": "The scaffold is a temporary structure that must persist until cells produce their own matrix. If degradation outpaces matrix production, the construct loses mechanical support and collapses. This timing mismatch is a common failure mode in bioprinted tissues."
        },
        {
            "question": "A student models two bioprinting approaches for a heart patch: Approach A achieves immediate structural integrity but requires donor cells with rejection risk. Approach B uses autologous cells with no rejection but requires 6 weeks of cell culture before printing. For a patient with heart failure deteriorating over 2-3 months, which analysis best evaluates these options?",
            "choices": {
                "A": "Approach A is always superior because time is the only factor",
                "B": "The decision depends on the patient's deterioration timeline versus the 6-week culture period: if the patient can survive 6 weeks plus printing and maturation time, Approach B's immune compatibility advantage may produce better long-term outcomes despite the delay",
                "C": "Approach B is always superior because rejection will always destroy Approach A constructs",
                "D": "Both approaches are equivalent because maturation time is the same"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is a patient-specific clinical trade-off. The immune compatibility advantage of autologous cells provides long-term benefit, but only if the patient survives the cell culture delay. Medical decision-making must weigh acute survival against long-term graft success.",
            "feedback_incorrect": "The optimal approach depends on the individual patient's condition. A rapidly deteriorating patient may not survive the 6-week culture period, making donor cells necessary despite rejection risk. A more stable patient benefits from the immune compatibility of autologous cells."
        },
        {
            "question": "The model reveals that bioprinted tissue thicker than 1 mm develops necrotic cores within 24 hours without vascularization, regardless of how perfectly the cells were printed. What does this demonstrate about the hierarchy of engineering challenges in bioprinting?",
            "choices": {
                "A": "Cell viability during printing is more important than vascularization",
                "B": "Vascularization is the gating constraint: no matter how well you solve printing resolution, bioink composition, cell sourcing, or scaffold design, the construct will fail without adequate blood vessel networks, making vascularization the prerequisite that all other improvements depend on",
                "C": "Thicker tissues are unnecessary because thin patches are sufficient for all applications",
                "D": "The necrotic core will eventually be cleared by the body's immune system"
            },
            "correct": "B",
            "feedback_correct": "Correct. Vascularization is the hierarchical gating constraint. All other bioprinting advances are necessary but insufficient without solving the vascular challenge. A perfectly printed organ with no blood supply is a dead organ.",
            "feedback_incorrect": "The model demonstrates a hierarchy of constraints: vascularization sits at the top. Without adequate blood vessel networks, improvements in every other parameter, resolution, bioink, cell viability, and scaffold design, cannot produce a viable thick tissue. Vascularization is the prerequisite for all other advances."
        },
        {
            "question": "Based on the bioprinting model, which conclusion about the relationship between construct complexity and functional maturation time is best supported by the simulation data?",
            "choices": {
                "A": "More complex constructs mature faster because they contain more diverse cell types",
                "B": "Functional maturation time increases nonlinearly with construct complexity because multi-tissue constructs require coordinated development of multiple cell types, formation of tissue-tissue interfaces, and integration of vascular, structural, and functional systems that must develop in the correct sequence",
                "C": "Maturation time is constant regardless of construct complexity",
                "D": "Simpler constructs require longer maturation because they have fewer cells to produce matrix"
            },
            "correct": "B",
            "feedback_correct": "Correct. Complex constructs face a sequential development challenge: different tissue types must mature in coordination, interfaces must form between tissues, and vascular networks must integrate with functional units. This orchestration requires substantially more time than simple, single-tissue constructs.",
            "feedback_incorrect": "Complexity and maturation time have a nonlinear relationship. Simple tissue patches need only one cell type to mature. Multi-tissue constructs require coordinated development of multiple cell populations, tissue-tissue interface formation, and vascular integration, each adding time and complexity."
        }
    ]
}

# =============================================================================
# L09: Can Nanotechnology Deliver Medicine to Individual Cells?
# NGSS: HS-LS1-3, HS-PS2-4
# =============================================================================
L09_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Only approximately 0.7% of injected nanoparticles actually reach a tumor. What is the primary reason for this extremely low delivery efficiency?",
            "choices": {
                "A": "Nanoparticles are too large to travel through blood vessels",
                "B": "The body's immune system, particularly liver and spleen macrophages, recognizes and removes the vast majority of nanoparticles from the bloodstream before they can reach the target",
                "C": "Tumors actively repel nanoparticles through electrical fields",
                "D": "Nanoparticles dissolve in the bloodstream before reaching the tumor"
            },
            "correct": "B",
            "feedback_correct": "Correct. The mononuclear phagocyte system, primarily macrophages in the liver and spleen, aggressively clears foreign particles from the blood. 30-99% of injected nanoparticles are sequestered by the liver, leaving less than 1% to reach the tumor.",
            "feedback_incorrect": "The body's immune surveillance system treats nanoparticles as foreign invaders. Liver and spleen macrophages remove the vast majority from circulation within minutes. This biological barrier, not particle design, is the primary reason for low tumor delivery."
        },
        {
            "question": "What is opsonization, and why is it the first obstacle nanoparticles face after injection?",
            "choices": {
                "A": "Opsonization is the process by which nanoparticles absorb water and swell",
                "B": "Blood proteins coat the nanoparticle surface, marking it for immune cell recognition and destruction, which begins within seconds of entering the bloodstream",
                "C": "Opsonization is the chemical breakdown of the nanoparticle's drug payload",
                "D": "Opsonization is the process by which nanoparticles bind to red blood cells"
            },
            "correct": "B",
            "feedback_correct": "Correct. Opsonization begins almost immediately: blood proteins adsorb onto the nanoparticle surface, creating a 'protein corona' that immune cells recognize as foreign. This triggers phagocytosis and rapid clearance from the bloodstream.",
            "feedback_incorrect": "Opsonization is the body's first defense against foreign particles. Blood proteins coat the nanoparticle within seconds, acting as a 'eat me' signal for macrophages. Without countermeasures like PEGylation, nanoparticles are cleared from the blood in minutes."
        },
        {
            "question": "The enhanced permeability and retention (EPR) effect allows nanoparticles to accumulate in tumors passively. What biological feature of tumors enables this effect?",
            "choices": {
                "A": "Tumors produce magnetic fields that attract nanoparticles",
                "B": "Tumor blood vessels are leaky with gaps of 200-800 nm, and the tumor's poor lymphatic drainage prevents nanoparticles from being cleared once they pass through the gaps",
                "C": "Tumors are warmer than surrounding tissue, drawing nanoparticles toward them",
                "D": "Tumor cells actively engulf all particles in the bloodstream"
            },
            "correct": "B",
            "feedback_correct": "Correct. Tumors grow rapidly and form abnormal, leaky blood vessels with large gaps. Nanoparticles of the right size (20-200 nm) pass through these gaps, and the tumor's poorly developed lymphatic system cannot clear them, causing passive accumulation.",
            "feedback_incorrect": "The EPR effect relies on two tumor characteristics: 1) leaky blood vessels with 200-800 nm gaps that allow nanoparticles to pass through, and 2) poor lymphatic drainage that prevents clearance. This creates passive accumulation without any targeting ligand."
        },
        {
            "question": "PEGylation involves coating nanoparticles with polyethylene glycol (PEG) chains. What is the primary purpose of this surface modification?",
            "choices": {
                "A": "PEG increases the drug payload capacity of the nanoparticle",
                "B": "PEG creates a hydrophilic stealth layer that reduces protein adsorption and immune recognition, extending the nanoparticle's circulation time from minutes to hours",
                "C": "PEG makes nanoparticles magnetic for MRI tracking",
                "D": "PEG increases the nanoparticle's size to improve tumor accumulation"
            },
            "correct": "B",
            "feedback_correct": "Correct. PEG creates a hydrophilic shell that repels blood proteins, reducing opsonization and delaying immune recognition. This 'stealth' coating extends circulation half-life, giving nanoparticles more time to reach the tumor.",
            "feedback_incorrect": "PEGylation is a stealth strategy: the PEG polymer layer creates a hydrophilic brush that prevents blood proteins from adsorbing onto the nanoparticle surface, reducing immune recognition and extending circulation time from minutes to hours."
        },
        {
            "question": "Controlled drug release from nanoparticles can be triggered by conditions at the tumor site. Which tumor microenvironment condition is most commonly exploited for triggered release?",
            "choices": {
                "A": "The tumor's high oxygen concentration",
                "B": "The acidic pH inside tumors (pH 5.5-6.5 compared to blood at pH 7.4), which can be used to design pH-sensitive nanoparticle coatings that dissolve and release drugs in the acidic tumor environment",
                "C": "The tumor's low temperature compared to surrounding tissue",
                "D": "The tumor's high electrical conductivity"
            },
            "correct": "B",
            "feedback_correct": "Correct. Tumors typically have an acidic microenvironment (pH 5.5-6.5) due to rapid metabolism and poor blood flow. pH-sensitive nanoparticle coatings remain stable at blood pH (7.4) but dissolve in acidic conditions, releasing drugs specifically at the tumor.",
            "feedback_incorrect": "The acidic tumor microenvironment (pH 5.5-6.5) is the most widely exploited trigger. Nanoparticles can be designed with pH-sensitive bonds or coatings that are stable in blood (pH 7.4) but dissolve in the acidic tumor, providing site-specific drug release."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's model shows that increasing PEGylation density from 5% to 20% surface coverage extends circulation half-life from 2 to 12 hours but reduces cellular uptake at the tumor by 40%. What does this reveal about the design trade-off?",
            "choices": {
                "A": "Higher PEGylation is always better because longer circulation is the only goal",
                "B": "The stealth effect of PEG that evades immune cells also reduces the nanoparticle's ability to interact with and enter target tumor cells, creating a fundamental tension between surviving the journey and completing the delivery",
                "C": "PEGylation has no effect on tumor cell interactions",
                "D": "The reduced uptake is caused by the nanoparticle becoming too large"
            },
            "correct": "B",
            "feedback_correct": "Correct. The same PEG layer that protects nanoparticles from immune clearance also hinders their interaction with target cells. This 'PEG dilemma' is a central design challenge: stealth for the journey versus accessibility at the destination.",
            "feedback_incorrect": "This is the 'PEG dilemma': the stealth coating that enables immune evasion also prevents interaction with target cells. The nanoparticle must evade immune cells during transit but engage target cells at the tumor. These requirements are fundamentally in tension."
        },
        {
            "question": "The model shows that adding targeting ligands increases tumor cell binding by 300% but also increases liver accumulation by 150% because liver cells express low levels of the same receptor. What does this demonstrate about the specificity challenge?",
            "choices": {
                "A": "Targeting ligands should never be used because they increase off-target accumulation",
                "B": "Active targeting improves tumor delivery but is limited by the fact that target receptors are rarely exclusive to tumor cells. Low-level expression on healthy cells creates off-target binding that concentrates the drug in the liver, potentially causing hepatotoxicity",
                "C": "The 300% improvement in tumor binding outweighs all other considerations",
                "D": "Liver accumulation is beneficial because it helps clear the drug from the body"
            },
            "correct": "B",
            "feedback_correct": "Correct. The specificity challenge arises because few receptors are truly unique to tumor cells. Any receptor expressed (even at low levels) on healthy cells will capture targeting nanoparticles, concentrating drug in unintended organs and potentially causing toxicity.",
            "feedback_incorrect": "Targeting ligands improve tumor delivery but expose a specificity limitation: target receptors are rarely tumor-exclusive. Low-level expression on healthy cells, especially in the liver (which filters all blood), creates significant off-target accumulation. The therapeutic index must account for this."
        },
        {
            "question": "A student models nanoparticle size optimization and finds that 100 nm particles have the best balance of EPR-mediated tumor accumulation and immune evasion. Particles of 20 nm accumulate well but are cleared by the kidneys; 200 nm particles avoid kidney clearance but are captured more efficiently by liver macrophages. What principle does this size optimization demonstrate?",
            "choices": {
                "A": "All nanoparticle sizes perform equally well in the body",
                "B": "Nanoparticle size must navigate between two biological barriers: renal filtration (removing particles that are too small) and phagocytic clearance (removing particles that are too large), creating a narrow optimal size window determined by the body's filtration and immune architecture",
                "C": "Larger particles are always better because they carry more drug",
                "D": "Size optimization is unnecessary because targeting ligands compensate for any size"
            },
            "correct": "B",
            "feedback_correct": "Correct. The body imposes size-dependent barriers: kidneys clear small particles, liver macrophages clear large particles. The optimal size window (~60-120 nm) avoids both barriers while exploiting the EPR effect for tumor accumulation.",
            "feedback_incorrect": "The body's filtration systems create a size window: too small (<30 nm) and kidneys clear them; too large (>200 nm) and macrophages capture them more efficiently. The optimal range (~60-120 nm) threads between these biological barriers while maximizing tumor accumulation via the EPR effect."
        },
        {
            "question": "The model reveals that drug release rate must be tuned to a specific window: too fast and the drug is lost during circulation before reaching the tumor; too slow and therapeutic concentrations are never achieved at the target. A student proposes using the fastest possible release rate. Why is this approach counterproductive?",
            "choices": {
                "A": "Fast release increases the drug's potency at the tumor",
                "B": "With fast release, most of the drug payload leaks out during the hours of circulation before the nanoparticle reaches the tumor, resulting in systemic drug exposure (conventional chemotherapy's side effect profile) rather than targeted delivery",
                "C": "Release rate has no effect on therapeutic outcomes",
                "D": "Fast release makes nanoparticles easier for the immune system to detect"
            },
            "correct": "B",
            "feedback_correct": "Correct. If the drug releases during transit, the nanoparticle delivers free drug throughout the body rather than concentrated drug at the tumor. This negates the entire advantage of targeted delivery and reverts to the side-effect profile of conventional chemotherapy.",
            "feedback_incorrect": "Premature drug release defeats the purpose of nanoparticle delivery. If the drug leaks out during the hours of bloodstream circulation, it distributes systemically, just like conventional chemotherapy. The nanoparticle must retain its payload until it reaches the tumor."
        },
        {
            "question": "Based on the nanoparticle drug delivery model, which conclusion about the 0.7% tumor delivery rate is best supported by the simulation data?",
            "choices": {
                "A": "The 0.7% rate proves that nanoparticle drug delivery is a failed technology",
                "B": "Despite the low percentage, the 0.7% delivery rate still represents a significant improvement over conventional chemotherapy because nanoparticles concentrate drug at the tumor while reducing exposure to healthy tissues. However, the model demonstrates that each biological barrier (opsonization, liver clearance, EPR variability, cellular uptake) multiplicatively reduces delivery, and meaningful improvement requires addressing multiple barriers simultaneously rather than optimizing any single parameter",
                "C": "The 0.7% rate will naturally improve to 50% with continued use",
                "D": "Tumor delivery percentage is irrelevant to therapeutic efficacy"
            },
            "correct": "B",
            "feedback_correct": "Correct. The barriers are multiplicative: if each of 5 barriers removes 50% of particles, only 0.5^5 = 3% survive. Improving one barrier from 50% to 25% loss yields only a modest gain. Meaningful improvement requires addressing multiple barriers simultaneously.",
            "feedback_incorrect": "The delivery barriers are multiplicative, not additive. Each biological obstacle removes a fraction of particles, and the fractions compound. This means optimizing a single barrier provides limited benefit; only simultaneous improvement across multiple barriers can substantially increase tumor delivery."
        }
    ]
}

# =============================================================================
# L10: Will Brain-Computer Interfaces Change Humanity?
# NGSS: HS-LS1-2, HS-LS1-3, HS-ETS1-1
# =============================================================================
L10_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A brain-computer interface (BCI) translates neural electrical activity into digital commands. What type of biological signal does an intracortical electrode array detect?",
            "choices": {
                "A": "Chemical neurotransmitter concentrations in the cerebrospinal fluid",
                "B": "Electrical signals from action potentials and local field potentials generated by populations of neurons near the electrode tips",
                "C": "Magnetic fields produced by the brain's iron-containing structures",
                "D": "Heat patterns from active brain regions"
            },
            "correct": "B",
            "feedback_correct": "Correct. Intracortical arrays detect the electrical activity of nearby neurons: individual action potentials from neurons within ~100 micrometers and local field potentials from larger neural populations, providing high-resolution signal data for decoding.",
            "feedback_incorrect": "Intracortical electrode arrays detect electrical signals: action potentials (spikes) from individual nearby neurons and local field potentials from neural populations. These electrical signals are the raw data that neural decoding algorithms interpret to determine the user's intentions."
        },
        {
            "question": "Current BCIs record from approximately 1,000-10,000 neurons out of 86 billion in the human brain. Despite sampling less than 0.00001% of neurons, paralyzed patients can control robotic arms. What does this suggest about neural coding?",
            "choices": {
                "A": "Most neurons are inactive and unnecessary for brain function",
                "B": "Neural activity is highly redundant: movement intentions are encoded across large populations, so sampling even a small fraction of the relevant cortical area captures enough of the distributed pattern to decode basic motor commands",
                "C": "Each neuron independently controls one specific movement",
                "D": "The BCI works by stimulating muscles directly, not by reading brain signals"
            },
            "correct": "B",
            "feedback_correct": "Correct. Motor cortex neurons encode movement in distributed population patterns with substantial redundancy. Even a small sample captures enough of the pattern to decode basic motor intentions, though finer control requires more neurons.",
            "feedback_incorrect": "Neural coding for movement is distributed and redundant across large populations. Because many neurons participate in encoding each movement, sampling even a small fraction captures enough of the distributed pattern to reconstruct basic motor commands, though resolution improves with more neurons."
        },
        {
            "question": "Why does the brain's tissue response to implanted electrodes degrade signal quality over months to years?",
            "choices": {
                "A": "The electrodes physically move to different brain regions over time",
                "B": "Chronic immune response causes glial cells to form a scar around each electrode, increasing electrical impedance and pushing neurons away from the recording surface, weakening the detected signals",
                "C": "The brain's neurons die whenever they are recorded from",
                "D": "The electrode materials corrode and release toxic chemicals"
            },
            "correct": "B",
            "feedback_correct": "Correct. The brain mounts a chronic immune response to foreign materials. Astrocytes and microglia form a glial scar that encapsulates electrodes, increasing the distance between the electrode and nearby neurons and raising electrical impedance, both of which degrade signal quality.",
            "feedback_incorrect": "The foreign body response causes glial scarring around implanted electrodes. This scar tissue increases electrical impedance (making signals harder to detect) and physically displaces neurons away from the electrode surface. Over months, signals weaken as the scar thickens."
        },
        {
            "question": "Noninvasive BCIs (scalp EEG) achieve 1-5 bits per second of information transfer, while invasive intracortical arrays achieve 10-50 bits per second. Natural typing is approximately 40 bits per second. What does this comparison reveal about the invasiveness-performance trade-off?",
            "choices": {
                "A": "Noninvasive BCIs are always preferable because they avoid surgical risk",
                "B": "There is a direct relationship between how close electrodes are to neurons and signal quality: invasive arrays provide higher resolution but require brain surgery, creating a trade-off between performance capability and medical risk",
                "C": "Invasive BCIs match natural communication speed and should replace keyboards",
                "D": "The information transfer rate is unrelated to electrode placement"
            },
            "correct": "B",
            "feedback_correct": "Correct. Signal quality improves dramatically with proximity to neurons. Scalp EEG averages signals across millions of neurons, losing detail. Intracortical arrays detect individual neurons but require surgery. The trade-off between signal quality and medical risk is fundamental.",
            "feedback_incorrect": "The 10x performance gap between noninvasive and invasive BCIs reflects the physics of signal detection: closer electrodes receive stronger, more specific signals. Scalp EEG detects averaged activity from vast neural populations, while intracortical arrays resolve individual neurons."
        },
        {
            "question": "Neuroplasticity plays a critical role in BCI function. How does the brain adapt to a BCI over weeks of use?",
            "choices": {
                "A": "The brain rejects the interface and stops producing signals near the electrodes",
                "B": "The brain learns to produce neural patterns that are more easily decoded by the interface, effectively meeting the machine halfway in a bidirectional learning process",
                "C": "Neuroplasticity has no effect on BCI performance",
                "D": "The brain creates new neurons specifically to communicate with the interface"
            },
            "correct": "B",
            "feedback_correct": "Correct. Both brain and machine adapt: the decoding algorithm is refined to better interpret neural signals, and the brain reorganizes its neural patterns to produce signals the algorithm can more reliably decode. This co-adaptation improves performance over time.",
            "feedback_incorrect": "BCI learning is bidirectional: the machine learning decoder improves its interpretation of neural signals, and simultaneously the brain's neuroplasticity enables it to produce neural patterns that are more consistent and distinguishable for the decoder. Both sides of the interface adapt."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's BCI model shows that doubling electrode count from 96 to 192 improves decoding accuracy from 78% to 89% but increases the tissue response severity index by 60%. What is the most scientifically rigorous evaluation of this trade-off?",
            "choices": {
                "A": "More electrodes are always better because accuracy is the primary goal",
                "B": "The accuracy improvement exhibits diminishing returns (11 percentage points from doubling), while the tissue response increases substantially (60%), suggesting that at some electrode density the chronic immune damage will degrade signals faster than additional electrodes improve them, creating a practical ceiling on electrode count",
                "C": "Tissue response is irrelevant because it only affects the first month after implantation",
                "D": "The solution is to use 1,000 electrodes to overcome any tissue response"
            },
            "correct": "B",
            "feedback_correct": "Correct. The diminishing accuracy returns versus accelerating tissue damage predicts a crossover point where more electrodes actually harm long-term performance. The optimal count balances acute decoding improvement against chronic signal degradation from immune response.",
            "feedback_incorrect": "The key insight is the asymmetry: accuracy gains diminish while tissue damage accelerates. At some density, the chronic glial scarring from additional electrodes will degrade signals faster than the extra channels improve decoding, creating a practical ceiling determined by the immune response."
        },
        {
            "question": "The model demonstrates that brain adaptation rate (neuroplasticity) initially improves BCI performance rapidly, then plateaus after 2-3 months. A student claims that performance will continue to improve indefinitely with training. What does the model data suggest?",
            "choices": {
                "A": "The student is correct; brain adaptation has no limits",
                "B": "The plateau suggests that neuroplasticity has finite capacity for BCI-related adaptation: the brain can only reorganize neural patterns so much before it reaches the limits of cortical reorganization for the given electrode configuration, setting a performance ceiling for each hardware design",
                "C": "The plateau is caused by the user losing motivation, not biological limits",
                "D": "Performance will eventually decrease because the brain forgets how to use the BCI"
            },
            "correct": "B",
            "feedback_correct": "Correct. Neuroplasticity is powerful but bounded. The brain can optimize its patterns for a given electrode configuration, but the information capacity is ultimately limited by the number and placement of electrodes. Higher performance requires better hardware, not just more training.",
            "feedback_incorrect": "The plateau reflects biological limits of cortical reorganization. While the brain can learn to produce more BCI-compatible patterns, this adaptation is constrained by the electrode array's spatial sampling. To exceed the plateau requires hardware improvements, not additional training time."
        },
        {
            "question": "In the model, a student compares the signal-to-noise ratio (SNR) of noninvasive EEG, surface electrocorticography (ECoG), and penetrating intracortical arrays. The SNR values are 3:1, 30:1, and 300:1 respectively. What does this 100x range in SNR predict about the types of neural commands each system can decode?",
            "choices": {
                "A": "All three systems can decode the same neural commands with equal accuracy",
                "B": "Higher SNR enables decoding of finer-grained neural commands: EEG can decode gross states (attention, relaxation), ECoG can decode individual finger movements, and intracortical arrays can potentially decode individual finger forces and fine motor sequences, because more precise neural patterns require higher signal fidelity to distinguish",
                "C": "SNR only affects the speed of decoding, not the types of commands",
                "D": "Lower SNR systems are preferable because they detect broader brain activity"
            },
            "correct": "B",
            "feedback_correct": "Correct. SNR directly determines decoding granularity. Coarse mental states produce large, distinguishable signals detectable even at low SNR. Fine motor commands like individual finger movements produce subtle, similar signals that require high SNR to differentiate.",
            "feedback_incorrect": "The 100x SNR range maps directly to decoding resolution. Low SNR can only distinguish large-scale brain states; medium SNR resolves individual body parts; high SNR can potentially distinguish individual finger movements. Signal fidelity determines how fine-grained the decoded commands can be."
        },
        {
            "question": "The model shows that information transfer rate (ITR) is the product of decoding accuracy and decoding speed. A system with 95% accuracy at 5 decisions/second achieves higher ITR than a system with 70% accuracy at 10 decisions/second. What design principle does this illustrate?",
            "choices": {
                "A": "Speed is always more important than accuracy in BCI design",
                "B": "Accuracy and speed jointly determine information throughput, and a system that is fast but inaccurate wastes bandwidth on errors and corrections. Optimal BCI design must maximize the accuracy-speed product, not either factor alone",
                "C": "Accuracy above 80% has no additional benefit",
                "D": "The two systems are equivalent because they use different decoding algorithms"
            },
            "correct": "B",
            "feedback_correct": "Correct. ITR = accuracy x speed. The 95%/5Hz system achieves 4.75 effective decisions/second, while the 70%/10Hz system achieves only 7 effective decisions/second but requires significant error correction overhead. The accuracy-speed product is the true performance metric.",
            "feedback_incorrect": "Information transfer rate is the product of accuracy and speed. Fast but inaccurate decisions require corrections that consume bandwidth. The optimal design point maximizes this product, and typically moderate speed with high accuracy outperforms high speed with poor accuracy."
        },
        {
            "question": "Based on the BCI model, which conclusion about the long-term future of brain-computer interfaces is best supported by the simulation data?",
            "choices": {
                "A": "BCIs will replace all conventional computer interfaces within a decade",
                "B": "The model reveals three interdependent bottlenecks: the tissue response limits implant longevity, the SNR ceiling limits decoding complexity, and neuroplasticity limits set performance plateaus for each hardware configuration. Meaningful advances require simultaneous progress across all three constraints, and each improvement enables but does not guarantee progress on the others",
                "C": "BCIs will never advance beyond current capabilities because the brain is too complex",
                "D": "Only noninvasive BCIs have a viable future because invasive systems cause too much tissue damage"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model identifies three coupled bottlenecks that must be addressed together. Better electrodes (reduced tissue response) enable higher SNR, which enables finer decoding, which benefits from neuroplasticity. But each constraint limits the others, requiring coordinated advancement.",
            "feedback_incorrect": "The model reveals three interdependent constraints: tissue biocompatibility limits how long implants function, SNR limits what can be decoded, and neuroplasticity limits how well the brain adapts. Progress requires addressing all three simultaneously because they constrain each other."
        }
    ]
}

# =============================================================================
# Combined dictionary for all lessons
# =============================================================================
ALL_QUESTIONS = {
    "G11L3-L01": L01_QUESTIONS,
    "G11L3-L02": L02_QUESTIONS,
    "G11L3-L03": L03_QUESTIONS,
    "G11L3-L04": L04_QUESTIONS,
    "G11L3-L05": L05_QUESTIONS,
    "G11L3-L06": L06_QUESTIONS,
    "G11L3-L07": L07_QUESTIONS,
    "G11L3-L08": L08_QUESTIONS,
    "G11L3-L09": L09_QUESTIONS,
    "G11L3-L10": L10_QUESTIONS,
}
