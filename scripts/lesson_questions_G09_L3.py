#!/usr/bin/env python3
"""Multiple choice pre/post assessment questions for Grade 9 Level 3 ModelIt! Lessons"""

L01_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A patient receives a chemotherapy drug that kills 95% of cancer cells in a petri dish. Which factor BEST explains why the same drug might fail when given to a patient?",
            "choices": {
                "A": "The drug must travel through the body and may never reach sufficient concentration at the tumor site",
                "B": "Cancer cells in a petri dish are genetically different from those in a patient",
                "C": "Chemotherapy drugs only work on blood cancers, not solid tumors",
                "D": "The petri dish contains more oxygen than the human body"
            },
            "correct": "A",
            "feedback_correct": "Correct. Pharmacokinetics describes how drugs move through the body. Absorption, metabolism, and clearance all reduce the concentration that actually reaches the tumor, which is often far lower than the controlled dose in a petri dish.",
            "feedback_incorrect": "Consider how a drug must be absorbed, distributed through the bloodstream, and metabolized before it reaches a tumor. The concentration at the tumor site may be very different from the dose administered."
        },
        {
            "question": "Which of the following BEST describes why chemotherapy often causes severe side effects such as hair loss and nausea?",
            "choices": {
                "A": "Chemotherapy drugs are designed to only target cancer cells but sometimes malfunction",
                "B": "The drugs damage rapidly dividing healthy cells in addition to cancer cells because they cannot distinguish between the two",
                "C": "Side effects are caused by allergic reactions to the drug compounds",
                "D": "Chemotherapy weakens the immune system, which causes all other symptoms"
            },
            "correct": "B",
            "feedback_correct": "Correct. Most chemotherapy drugs target rapidly dividing cells. Since both cancer cells and certain healthy cells (hair follicles, gut lining, bone marrow) divide rapidly, the drugs damage both, producing severe side effects.",
            "feedback_incorrect": "Think about what cancer cells and certain healthy cells (like those in hair follicles and the digestive tract) have in common. Chemotherapy targets a cellular behavior, not a specific cell type."
        },
        {
            "question": "A doctor says a drug has a 'narrow therapeutic window.' What does this MOST LIKELY mean?",
            "choices": {
                "A": "The drug is only effective during a short time period after administration",
                "B": "The difference between an effective dose and a toxic dose is very small",
                "C": "The drug can only be given through one specific route of administration",
                "D": "Only a narrow range of patients can benefit from the drug"
            },
            "correct": "B",
            "feedback_correct": "Correct. A narrow therapeutic window means the minimum dose needed for effectiveness is dangerously close to the maximum dose the body can tolerate, leaving very little room for dosing error.",
            "feedback_incorrect": "A therapeutic window refers to the range of drug concentrations in the blood between the minimum effective dose and the maximum safe dose. Consider what 'narrow' means in that context."
        },
        {
            "question": "After taking a medication, a patient's blood test shows the drug concentration rising, peaking, and then declining over 12 hours. Which organs are MOST responsible for the decline phase?",
            "choices": {
                "A": "The heart and lungs, which pump the drug out of the body",
                "B": "The liver and kidneys, which metabolize and excrete the drug",
                "C": "The stomach and intestines, which stop absorbing the drug",
                "D": "The brain and spinal cord, which signal the body to reject foreign chemicals"
            },
            "correct": "B",
            "feedback_correct": "Correct. The liver enzymatically breaks down drugs into inactive metabolites, and the kidneys filter these metabolites from the blood for excretion in urine. Together, they are primarily responsible for drug clearance.",
            "feedback_incorrect": "Consider which organs are responsible for breaking down substances in the blood and removing waste products from the body."
        },
        {
            "question": "Why would a computational model be useful in designing cancer drug dosing protocols BEFORE testing on patients?",
            "choices": {
                "A": "Computer models can perfectly predict every patient's response to a drug",
                "B": "Models allow researchers to simulate thousands of dosing strategies and identify the most promising ones without risking patient safety",
                "C": "Computational models eliminate the need for clinical trials entirely",
                "D": "Models can generate new drug molecules that are guaranteed to work"
            },
            "correct": "B",
            "feedback_correct": "Correct. Computational models enable researchers to test many variables (dose, timing, frequency) virtually, narrowing down the most promising strategies before expensive and risky human trials. They do not replace clinical trials but make them more efficient.",
            "feedback_incorrect": "Think about the purpose of modeling. Models are tools for exploring possibilities and reducing risk, not for producing guaranteed outcomes or replacing experimental validation."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In a multi-scale pharmacokinetic model, Drug Dosage is increased by 50%. Blood Concentration rises proportionally, but Tumor Uptake only increases by 10%. Which explanation BEST accounts for this discrepancy?",
            "choices": {
                "A": "The tumor has limited blood supply and receptor binding capacity, so additional circulating drug cannot all be absorbed by the tumor",
                "B": "The kidneys immediately excrete the additional drug before it reaches the tumor",
                "C": "Higher doses always decrease tumor uptake due to receptor saturation",
                "D": "Blood concentration and tumor uptake are independent variables in pharmacokinetic models"
            },
            "correct": "A",
            "feedback_correct": "Correct. Tumor uptake depends on the tumor's blood vessel density, permeability, and available receptor binding sites. Once these are saturated, additional circulating drug provides diminishing returns at the tumor while increasing systemic toxicity.",
            "feedback_incorrect": "Consider what limits the amount of drug that can cross from the bloodstream into the tumor microenvironment. Blood concentration is a necessary but not sufficient condition for tumor uptake."
        },
        {
            "question": "A pharmacokineticist compares two dosing strategies: (1) a single high dose every 3 weeks and (2) lower doses given 3 times per week. Both deliver the same total drug amount. Which outcome does the metronomic (frequent low-dose) strategy MOST LIKELY produce?",
            "choices": {
                "A": "Higher peak toxicity but longer time within the therapeutic window",
                "B": "More consistent blood concentration within the therapeutic window with reduced peak side effects",
                "C": "Lower overall drug effectiveness because each individual dose is too small",
                "D": "Identical outcomes because the total drug amount is the same"
            },
            "correct": "B",
            "feedback_correct": "Correct. Metronomic dosing maintains more consistent drug levels by avoiding the extreme peaks (which cause toxicity) and deep troughs (which allow tumor regrowth) of single high-dose protocols. The total amount matters less than the time spent within the therapeutic window.",
            "feedback_incorrect": "Consider what happens to blood concentration over time with each strategy. A single large dose creates a high peak followed by a long trough, while frequent smaller doses create a more level concentration profile."
        },
        {
            "question": "Two patients receive identical chemotherapy doses, but Patient A experiences severe toxicity while Patient B shows minimal side effects. Based on pharmacokinetic modeling, which variable MOST LIKELY differs between them?",
            "choices": {
                "A": "The type of cancer they have",
                "B": "Their liver metabolism rate, which determines how quickly the drug is broken down",
                "C": "The hospital where they received treatment",
                "D": "The time of day the drug was administered"
            },
            "correct": "B",
            "feedback_correct": "Correct. Liver enzyme activity (metabolism rate) varies significantly between individuals due to genetic polymorphisms. A patient with slow metabolism will maintain higher blood drug concentrations for longer, potentially exceeding the toxic threshold, while a fast metabolizer may clear the drug before it reaches effective levels.",
            "feedback_incorrect": "In pharmacokinetic modeling, the same dose produces different blood concentration profiles in different patients. Consider which biological process most directly controls how long the drug remains active in the body."
        },
        {
            "question": "A student's pharmacokinetic model shows that increasing Kidney Clearance rate while holding all other variables constant results in DECREASED Side Effect Severity but ALSO decreased Tumor Uptake. Which analysis BEST explains this trade-off?",
            "choices": {
                "A": "Faster kidney clearance removes the drug from the blood more quickly, reducing both the time for tumor absorption and the duration of healthy cell exposure",
                "B": "The kidneys selectively filter drug molecules headed toward healthy tissues but not those headed toward the tumor",
                "C": "Kidney clearance and tumor uptake are unrelated variables that happen to change simultaneously",
                "D": "Increased kidney function strengthens the immune system, which independently reduces side effects"
            },
            "correct": "A",
            "feedback_correct": "Correct. Kidney clearance reduces overall blood concentration over time. This shorter exposure window means less time for healthy cells to absorb the drug (reducing side effects) but also less time for the tumor to accumulate sufficient drug (reducing efficacy). This is a systems-level trade-off.",
            "feedback_incorrect": "Consider that kidney clearance affects the overall drug concentration in the blood, which is the supply for BOTH tumor uptake and healthy cell damage. What happens when you reduce that shared supply faster?"
        },
        {
            "question": "An adaptive dosing algorithm monitors a cancer patient's blood biomarkers in real time and automatically adjusts the next dose. Which design principle is MOST critical for patient safety in this system?",
            "choices": {
                "A": "The algorithm should always increase the dose to maximize tumor kill rate",
                "B": "The algorithm must include safety thresholds that trigger automatic dose reduction or treatment pause when blood concentration approaches the toxic limit",
                "C": "The algorithm should prioritize cost reduction over treatment effectiveness",
                "D": "The algorithm should use a fixed dosing schedule regardless of biomarker readings to ensure consistency"
            },
            "correct": "B",
            "feedback_correct": "Correct. Safety thresholds are non-negotiable in adaptive dosing. The algorithm must continuously monitor blood concentration against the upper bound of the therapeutic window and automatically reduce or pause dosing before toxicity occurs, even if this temporarily reduces tumor kill rate.",
            "feedback_incorrect": "Consider the primary risk of automated medical dosing. What safeguard must be built into any system that adjusts drug doses without direct physician intervention for each decision?"
        }
    ]
}

L02_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Antibiotic-resistant bacteria are considered a major global health threat. Which process BEST explains how bacterial populations develop resistance to antibiotics?",
            "choices": {
                "A": "Individual bacteria learn to recognize and avoid antibiotics through repeated exposure",
                "B": "Random genetic mutations produce resistant individuals, and natural selection favors their survival when antibiotics are applied",
                "C": "Antibiotics cause bacteria to intentionally mutate their DNA for protection",
                "D": "Resistant bacteria are a completely different species that is naturally immune"
            },
            "correct": "B",
            "feedback_correct": "Correct. Resistance arises through random mutations that occur before antibiotic exposure. When antibiotics are applied, susceptible bacteria die while resistant mutants survive and reproduce, increasing the frequency of resistance genes in the population through natural selection.",
            "feedback_incorrect": "Think about how evolution by natural selection works. Mutations occur randomly, and the environment determines which individuals survive. Bacteria do not choose to become resistant."
        },
        {
            "question": "A bacteriophage is a type of virus. What distinguishes bacteriophages from viruses that cause human diseases like influenza?",
            "choices": {
                "A": "Bacteriophages are larger than human viruses",
                "B": "Bacteriophages exclusively infect bacteria and cannot infect human cells",
                "C": "Bacteriophages contain DNA while human viruses contain RNA",
                "D": "Bacteriophages do not replicate like other viruses"
            },
            "correct": "B",
            "feedback_correct": "Correct. Bacteriophages require specific bacterial surface receptors for attachment and infection. Human cells lack these receptors, making phages biologically incapable of infecting human cells. This specificity is what makes them potentially useful as targeted antibacterial treatments.",
            "feedback_incorrect": "Consider what determines which cells a virus can infect. Viruses need specific surface receptors on their target cells. Think about whether bacterial surface receptors are the same as human cell surface receptors."
        },
        {
            "question": "A hospital patient has an infection caused by a bacterium resistant to all available antibiotics. A doctor suggests using a virus to treat the infection. What is the MOST reasonable concern about this approach?",
            "choices": {
                "A": "The virus might infect the patient's own cells and cause additional illness",
                "B": "The bacteria might evolve resistance to the virus, just as they evolved resistance to antibiotics",
                "C": "Viruses cannot kill bacteria because they are smaller",
                "D": "The immune system would prevent any virus from entering the body"
            },
            "correct": "B",
            "feedback_correct": "Correct. Just as bacteria evolve antibiotic resistance through natural selection, they can also evolve resistance to bacteriophages by modifying the surface receptors that phages use for attachment. This is a legitimate scientific concern for phage therapy.",
            "feedback_incorrect": "Consider the evolutionary principle at work. If natural selection drives resistance to one type of selective pressure (antibiotics), could the same process operate against a different selective pressure (viral predation)?"
        },
        {
            "question": "Unlike antibiotics, which degrade after administration, bacteriophages can increase in number inside a patient during treatment. What biological process allows this?",
            "choices": {
                "A": "Phages undergo cell division like bacteria",
                "B": "The patient's immune system produces more phages",
                "C": "Phages replicate inside the bacteria they infect, releasing new phage particles when the bacterial cell bursts",
                "D": "Phages absorb nutrients from the patient's bloodstream to grow"
            },
            "correct": "C",
            "feedback_correct": "Correct. Phages inject their genetic material into bacterial cells, hijack the cell's protein synthesis machinery to produce new phage components, assemble 50-200 new phage particles, and lyse (burst) the cell. This makes phage therapy self-amplifying.",
            "feedback_incorrect": "Remember that viruses cannot reproduce independently. They need a host cell's machinery. In phage therapy, what serves as the host cell?"
        },
        {
            "question": "The human gut contains trillions of beneficial bacteria that aid in digestion and immune function. Why is this relevant when considering phage therapy for a bacterial infection?",
            "choices": {
                "A": "Beneficial gut bacteria would prevent phages from reaching the pathogenic bacteria",
                "B": "Phage therapy must be specific enough to kill pathogenic bacteria without destroying the beneficial microbiome",
                "C": "Gut bacteria are immune to all viruses and would be unaffected",
                "D": "The microbiome has no relevance to infection treatment decisions"
            },
            "correct": "B",
            "feedback_correct": "Correct. A treatment that kills both pathogenic and beneficial bacteria (as many broad-spectrum antibiotics do) can cause serious complications. Phage specificity, the ability to target only the disease-causing strain, is a critical design parameter.",
            "feedback_incorrect": "Consider the consequences of a treatment that does not distinguish between harmful bacteria and the beneficial bacteria your body depends on for normal function."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In a phage therapy model, a student observes that increasing initial Phage Dosage leads to faster bacterial clearance, but the effect plateaus after a certain dose. Which explanation BEST accounts for this plateau?",
            "choices": {
                "A": "Phages are self-amplifying, so once enough phages establish successful infections, additional initial phages are redundant because the population grows exponentially from bacterial lysis",
                "B": "Higher doses are always toxic to the patient",
                "C": "The immune system destroys all phages above a certain concentration",
                "D": "Bacteria become instantly resistant when phage concentration is too high"
            },
            "correct": "A",
            "feedback_correct": "Correct. Because phage therapy is self-amplifying (each lysed bacterium releases 50-200 new phages), the initial dose only needs to be large enough to establish productive infections. Beyond that threshold, the phage population grows exponentially regardless of the starting dose.",
            "feedback_incorrect": "Consider what makes phage therapy fundamentally different from antibiotic treatment. Antibiotics degrade over time, but phages do something unique when they encounter target bacteria."
        },
        {
            "question": "A model simulation shows that when Treatment Timing is delayed from Day 1 to Day 5 of infection, the probability of treatment failure increases dramatically. Which factor MOST directly explains this finding?",
            "choices": {
                "A": "The patient's immune system becomes too weak to support phage therapy after 5 days",
                "B": "A larger, more genetically diverse bacterial population is more likely to contain pre-existing resistance mutations that natural selection can amplify",
                "C": "Phages lose their effectiveness after being stored for 5 days",
                "D": "The infection has already caused irreversible organ damage by Day 5"
            },
            "correct": "B",
            "feedback_correct": "Correct. As bacterial populations grow, they accumulate genetic diversity through random mutation. A population of 10 billion bacteria is far more likely to contain individuals with phage-resistant mutations than a population of 10,000. Natural selection rapidly amplifies these resistant mutants under phage pressure.",
            "feedback_incorrect": "Consider the relationship between population size and genetic diversity. How does a larger bacterial population change the probability that resistance-conferring mutations exist before treatment begins?"
        },
        {
            "question": "A researcher observes that bacteria which evolve resistance to a phage by modifying their surface receptors simultaneously become susceptible to an antibiotic they were previously resistant to. This phenomenon is BEST explained by which concept?",
            "choices": {
                "A": "Genetic linkage, where the resistance and susceptibility genes are on the same chromosome",
                "B": "Evolutionary trade-offs, where the surface receptors used for phage attachment are the same receptors that confer antibiotic resistance, so modifying them costs both functions",
                "C": "Horizontal gene transfer from phage DNA to bacterial DNA",
                "D": "The antibiotic was reformulated to be more effective against the mutant strain"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is phage-antibiotic synergy. Surface receptor proteins often serve multiple functions. When bacteria modify a receptor to block phage attachment, they may lose the efflux pump or structural feature that made them antibiotic-resistant. Evolution forces a trade-off between two survival strategies.",
            "feedback_incorrect": "Think about the dual function of bacterial surface receptors. If a receptor protein both enables antibiotic resistance AND serves as the phage attachment site, what happens when the bacterium mutates that receptor to escape the phage?"
        },
        {
            "question": "A phage therapy optimization model includes both Phage Specificity and Healthy Microbiome Impact as components. A student increases Phage Specificity to its maximum value. What is the MOST LIKELY effect on Healthy Microbiome Impact?",
            "choices": {
                "A": "Healthy Microbiome Impact increases because more specific phages are more potent",
                "B": "Healthy Microbiome Impact decreases because highly specific phages only target the pathogenic strain and leave beneficial bacteria unharmed",
                "C": "There is no relationship between specificity and microbiome impact",
                "D": "Healthy Microbiome Impact remains the same because the microbiome is immune to phages"
            },
            "correct": "B",
            "feedback_correct": "Correct. Phage Specificity and Healthy Microbiome Impact have a negative relationship. Higher specificity means the phage more precisely distinguishes between pathogenic bacteria and beneficial microbiome species, resulting in less collateral damage to the gut ecosystem.",
            "feedback_incorrect": "Consider what specificity means in biological targeting. A highly specific phage recognizes only one bacterial strain's receptors. How would this affect bacteria in the gut that have different surface receptors?"
        },
        {
            "question": "A clinical team is designing a phage cocktail containing three different phages, each targeting a different surface receptor on the same pathogenic bacterium. What is the PRIMARY advantage of this multi-phage approach over using a single phage type?",
            "choices": {
                "A": "Three phages kill bacteria three times faster than one phage",
                "B": "The probability of simultaneous resistance to all three phages is exponentially lower than resistance to any single phage, making treatment failure far less likely",
                "C": "Different phages target different organs in the body, increasing tissue coverage",
                "D": "Using three phages reduces the immune system's response to the treatment"
            },
            "correct": "B",
            "feedback_correct": "Correct. If resistance to one phage occurs at a rate of 1 in 10^6, simultaneous resistance to three independent phages targeting different receptors occurs at approximately 1 in 10^18. This combinatorial principle is the same logic behind HIV combination therapy and makes resistance evolution astronomically unlikely.",
            "feedback_incorrect": "Consider the mathematics of probability. If each phage targets a different receptor, a bacterium must independently mutate all three receptors simultaneously to survive. How does requiring multiple simultaneous mutations change the odds?"
        }
    ]
}

L03_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "In normal Mendelian inheritance, a gene from one parent has a 50% chance of being passed to each offspring. A gene drive technology increases this to over 99%. What biological mechanism could MOST PLAUSIBLY achieve this?",
            "choices": {
                "A": "The gene drive kills all offspring that do not inherit it",
                "B": "The gene drive copies itself onto the partner chromosome during reproduction, converting heterozygotes into homozygotes",
                "C": "The gene drive makes the organism produce more eggs or sperm",
                "D": "The gene drive prevents meiosis from occurring normally"
            },
            "correct": "B",
            "feedback_correct": "Correct. CRISPR-based gene drives cut the wild-type allele on the partner chromosome and use homology-directed repair to copy the drive sequence onto it. This converts a heterozygous individual (one copy) into a homozygous individual (two copies), ensuring nearly 100% of offspring inherit the drive.",
            "feedback_incorrect": "Think about what would need to happen at the chromosomal level to change the inheritance ratio from 50% to over 99%. The drive must somehow ensure both copies of the gene carry the engineered sequence."
        },
        {
            "question": "Malaria is transmitted to humans through mosquito bites. If mosquitoes could be genetically modified to be unable to carry the malaria parasite, what would be the MOST DIRECT effect?",
            "choices": {
                "A": "The malaria parasite would go extinct globally",
                "B": "Human malaria transmission rates would decrease because mosquitoes could no longer serve as vectors",
                "C": "All mosquito species would die because they depend on the malaria parasite",
                "D": "Humans would develop natural immunity to malaria"
            },
            "correct": "B",
            "feedback_correct": "Correct. Mosquitoes are the vector (carrier) for malaria. If they cannot carry the parasite, they cannot transmit it to humans during blood meals, breaking the transmission cycle. The parasite would not necessarily go extinct, as it could persist in other reservoirs.",
            "feedback_incorrect": "Consider the role mosquitoes play in the malaria life cycle. They are the bridge between infected and uninfected humans. What happens when that bridge is removed?"
        },
        {
            "question": "An ecologist argues that eliminating all mosquitoes could have serious consequences for other species. Which reasoning BEST supports this concern?",
            "choices": {
                "A": "Mosquitoes are the most important species on Earth",
                "B": "Many species of bats, birds, fish, and other organisms rely on mosquitoes as a food source, and their removal could trigger cascading effects through food webs",
                "C": "Without mosquitoes, there would be no insects left in the ecosystem",
                "D": "Mosquito elimination would cause immediate extinction of all predator species"
            },
            "correct": "B",
            "feedback_correct": "Correct. Mosquitoes occupy ecological niches as food sources for many organisms and as pollinators in some ecosystems. Removing them could cause population declines in species that depend on them, which could cascade through multiple trophic levels in the food web.",
            "feedback_incorrect": "Consider the concept of ecological cascades. When one species is removed from a food web, which other species are affected and how do those effects ripple outward?"
        },
        {
            "question": "A scientist proposes releasing genetically modified organisms into the wild to solve an environmental problem. A critic responds that 'you cannot recall a gene drive once it is released.' What does this criticism MOST LIKELY mean?",
            "choices": {
                "A": "The modified organisms cannot be physically recaptured",
                "B": "Once a self-spreading genetic modification enters a wild population, it will continue to propagate through reproduction and cannot be retrieved or reversed",
                "C": "The gene drive will eventually spread to all species, not just the target",
                "D": "Scientists will forget the genetic sequence they used"
            },
            "correct": "B",
            "feedback_correct": "Correct. Gene drives are self-propagating through natural reproduction. Once released into a wild population, the engineered gene spreads through mating and is inherited by future generations. Unlike a chemical pesticide that degrades over time, a gene drive persists and spreads indefinitely.",
            "feedback_incorrect": "Think about how genetic information is transmitted. Once an engineered gene enters a breeding population, what natural process ensures it continues to spread?"
        },
        {
            "question": "Why might natural selection eventually undermine a gene drive designed to suppress a mosquito population?",
            "choices": {
                "A": "Mosquitoes will migrate to areas without the gene drive",
                "B": "Random mutations that block the gene drive mechanism will be strongly favored by natural selection, since individuals with those mutations survive and reproduce while drive-carrying individuals do not",
                "C": "Gene drives cannot function in tropical climates",
                "D": "Natural selection does not act on engineered genes"
            },
            "correct": "B",
            "feedback_correct": "Correct. Any mosquito that develops a mutation preventing the gene drive from copying itself onto its chromosomes will have a survival advantage. Natural selection will amplify this resistance mutation in the population, potentially rendering the gene drive ineffective.",
            "feedback_incorrect": "Apply the logic of natural selection. If the gene drive reduces mosquito fitness, what happens to any individual that happens to carry a mutation blocking the drive? Does it have a survival advantage?"
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's gene drive model shows that at 95% Gene Drive Efficiency, Wild-Type Gene Frequency drops to near zero within 12 generations. When Gene Drive Efficiency is reduced to 85%, Wild-Type Gene Frequency stabilizes at approximately 40% even after 50 generations. Which factor BEST explains this difference?",
            "choices": {
                "A": "At 85% efficiency, resistance mutations accumulate faster than the drive can spread, creating an evolutionary equilibrium between drive-carrying and resistant wild-type mosquitoes",
                "B": "85% is below the minimum threshold for gene drives to function at all",
                "C": "The model contains a mathematical error at lower efficiency values",
                "D": "Wild-type mosquitoes reproduce faster than drive-carrying mosquitoes at any efficiency level"
            },
            "correct": "A",
            "feedback_correct": "Correct. At lower drive efficiency, there is more time per generation for resistance mutations to arise and be selected for. The population reaches an equilibrium where the rate of drive spread is balanced by the rate of resistance evolution, preventing complete population suppression.",
            "feedback_incorrect": "Consider the race between gene drive propagation and resistance evolution. At lower efficiency, which process gains a relative advantage, and what does that mean for the long-term population composition?"
        },
        {
            "question": "A simulation of global gene drive release shows that Ecosystem Disruption Risk increases nonlinearly as Mosquito Population approaches zero. Which ecological principle BEST explains this nonlinear relationship?",
            "choices": {
                "A": "Ecosystems respond linearly to species removal until a critical threshold is crossed",
                "B": "Redundant ecological roles mask the impact of mosquito decline until the population drops below the level where other species can compensate, triggering cascading food web collapse",
                "C": "Ecosystems are unaffected by the removal of any single species",
                "D": "Mosquito population decline automatically increases all other insect populations"
            },
            "correct": "B",
            "feedback_correct": "Correct. Ecosystems exhibit functional redundancy, where other species can partially fill ecological roles. But below a critical threshold, predator species that depend on mosquitoes cannot switch to alternative prey fast enough, triggering cascading population declines through the food web. This is a nonlinear tipping point effect.",
            "feedback_incorrect": "Think about ecosystem resilience. Ecosystems can absorb some perturbation, but there is a point where compensatory mechanisms are overwhelmed. What determines that threshold?"
        },
        {
            "question": "A gene drive cannot be geographically contained because mosquitoes that carry the drive can migrate to new areas. A student proposes engineering a 'self-limiting' gene drive that weakens after a set number of generations. Which trade-off does this design MOST DIRECTLY create?",
            "choices": {
                "A": "The drive achieves local population suppression but may not persist long enough to eliminate malaria transmission before it degrades",
                "B": "The drive becomes more effective over time as it weakens",
                "C": "Self-limiting drives spread faster than standard drives",
                "D": "Self-limiting drives eliminate the ecological risks entirely"
            },
            "correct": "A",
            "feedback_correct": "Correct. A self-limiting drive trades long-term persistence for containability. It reduces the risk of irreversible global ecosystem disruption but may not sustain itself long enough to achieve the goal of malaria elimination. This is a fundamental trade-off between safety and efficacy.",
            "feedback_incorrect": "Consider what happens when a gene drive is designed to degrade over generations. It addresses the 'cannot be recalled' problem, but what new problem does it introduce for the malaria elimination goal?"
        },
        {
            "question": "In a gene drive governance debate, one argument is that communities most affected by malaria should have decision-making authority over gene drive deployment, even if the drive will cross national borders. Which ethical principle does this argument MOST DIRECTLY invoke?",
            "choices": {
                "A": "Economic efficiency, because affected communities bear the treatment costs",
                "B": "Environmental justice and self-determination, because the communities bearing the greatest disease burden should have agency over interventions in their environment",
                "C": "Scientific authority, because local scientists are more qualified than international ones",
                "D": "National sovereignty, because each country controls its own borders"
            },
            "correct": "B",
            "feedback_correct": "Correct. This invokes the principle that communities most impacted by both the disease and the intervention should have meaningful input into the decision. Environmental justice recognizes that those who bear the risks and consequences of an action should have proportional voice in deciding whether to proceed.",
            "feedback_incorrect": "Consider who is most affected by both malaria (600,000 deaths/year, primarily in sub-Saharan Africa) and by the potential ecological consequences of gene drive release. Which ethical framework addresses this asymmetry?"
        },
        {
            "question": "A coupled gene drive model shows that reducing Mosquito Population by 90% decreases Human Malaria Cases by only 60%. Which systems-level explanation BEST accounts for this result?",
            "choices": {
                "A": "The remaining 10% of mosquitoes are more efficient at transmitting malaria because they face less competition for blood meals",
                "B": "Malaria transmission depends on contact frequency, bite rates, and parasite development time, not just mosquito numbers, and the remaining population may increase per-mosquito transmission efficiency",
                "C": "The model does not accurately represent malaria biology",
                "D": "Humans develop resistance to malaria when mosquito populations decrease"
            },
            "correct": "B",
            "feedback_correct": "Correct. Malaria transmission is a complex function of mosquito density, biting frequency, parasite development time, and human immune status. Reducing mosquito numbers shifts other parameters. Surviving mosquitoes may bite more frequently with less competition, and reduced exposure may decrease population-level immunity, partially offsetting the benefit of fewer vectors.",
            "feedback_incorrect": "Think about malaria transmission as a system with multiple interacting variables, not just mosquito count. When one variable changes dramatically, how might other variables in the system respond?"
        }
    ]
}

L04_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Cultured meat is grown from animal cells in a laboratory rather than by raising and slaughtering animals. Which biological process is MOST fundamental to this technology?",
            "choices": {
                "A": "Photosynthesis, which provides energy for cell growth",
                "B": "Cell division, which allows a small sample of muscle cells to multiply into a large quantity of tissue",
                "C": "Fermentation, which converts plant material directly into meat",
                "D": "Genetic modification, which transforms plant cells into animal cells"
            },
            "correct": "B",
            "feedback_correct": "Correct. Cultured meat relies on the natural ability of animal muscle cells (satellite cells) to divide and proliferate when given appropriate nutrients and growth conditions. Starting from a small tissue biopsy, millions of cells can be grown through repeated cell division.",
            "feedback_incorrect": "Consider what happens at the cellular level. Cultured meat starts with real animal cells and needs them to multiply. Which fundamental cellular process makes this multiplication possible?"
        },
        {
            "question": "A bioreactor is an enclosed vessel used to grow cells at large scale. Which condition would be MOST critical to maintain for mammalian cell growth?",
            "choices": {
                "A": "Ultraviolet light exposure to stimulate cell division",
                "B": "Temperature at approximately 37 degrees C with controlled oxygen and nutrient delivery",
                "C": "Extremely high pressure to compress cells into dense tissue",
                "D": "Acidic pH below 4.0 to prevent bacterial contamination"
            },
            "correct": "B",
            "feedback_correct": "Correct. Mammalian cells evolved to function at body temperature (37 degrees C) and require continuous oxygen and nutrient supply. Bioreactors must precisely maintain these conditions while removing metabolic waste products to keep cells healthy and dividing.",
            "feedback_incorrect": "Think about the conditions inside a living animal's body where muscle cells naturally grow. What temperature, nutrient supply, and gas exchange do they experience?"
        },
        {
            "question": "Why does conventional meat production have a significant environmental impact compared to growing crops directly for human consumption?",
            "choices": {
                "A": "Animals are inherently inefficient converters of feed to meat, requiring many kilograms of grain and thousands of liters of water per kilogram of meat produced",
                "B": "Meat production has no significant environmental impact",
                "C": "Crop production requires more land than animal agriculture",
                "D": "Animals release oxygen, which damages the atmosphere"
            },
            "correct": "A",
            "feedback_correct": "Correct. The trophic efficiency of converting plant feed to animal tissue is approximately 10%. Producing 1 kg of beef requires roughly 7-10 kg of grain and 15,000 liters of water, along with significant greenhouse gas emissions from enteric fermentation and manure management.",
            "feedback_incorrect": "Consider energy transfer between trophic levels in an ecosystem. When animals eat grain, what fraction of that energy is converted into body mass versus being used for the animal's own metabolism?"
        },
        {
            "question": "The first cultured meat hamburger in 2013 cost approximately $330,000 to produce. Which factor MOST LIKELY contributed to this extreme cost?",
            "choices": {
                "A": "The meat was made from endangered animal cells",
                "B": "Growth factors and nutrient media required for cell culture were extremely expensive at small production scale",
                "C": "The energy cost of maintaining a bioreactor is inherently prohibitive",
                "D": "The technology required rare minerals found only in space"
            },
            "correct": "B",
            "feedback_correct": "Correct. Growth factors (signaling proteins like FGF2 and IGF-1) are the most expensive component of cell culture media, costing thousands of dollars per gram. At early development scale, these costs dominated. Prices have since dropped by over 99% as production has scaled up.",
            "feedback_incorrect": "Think about what cells need to grow outside the body. The nutrients and growth signals that an animal's body provides for free must be supplied artificially. What makes that artificial supply expensive?"
        },
        {
            "question": "A key challenge in growing cultured meat is creating tissue that has the texture of real steak rather than a paste-like consistency. Which structural feature of natural muscle is MOST responsible for meat's fibrous texture?",
            "choices": {
                "A": "The high water content of muscle cells",
                "B": "Aligned, organized muscle fibers that are structured by connective tissue into bundles",
                "C": "The color pigments in muscle tissue",
                "D": "Fat deposits between muscle groups"
            },
            "correct": "B",
            "feedback_correct": "Correct. Natural meat gets its characteristic texture from muscle fibers aligned in parallel, organized into bundles by connective tissue. Recreating this alignment in cultured meat requires scaffolds that guide cell growth and mechanical stimulation that exercises the developing tissue.",
            "feedback_incorrect": "When you pull apart a piece of steak, you can see the fibrous structure. What gives meat this directional, fiber-like quality at the cellular and tissue level?"
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In a bioreactor optimization model, a student maximizes Nutrient Medium Concentration and Oxygen Supply simultaneously. Cell Growth Rate increases initially but then crashes. Which model component BEST explains this crash?",
            "choices": {
                "A": "Waste Product Accumulation increases proportionally with rapid cell growth, and the toxic byproducts (ammonia, lactate) inhibit further cell division when they exceed tolerable concentrations",
                "B": "Cells have a maximum lifespan regardless of nutrient availability",
                "C": "Oxygen is toxic to mammalian cells at high concentrations",
                "D": "The bioreactor physically breaks from the increased cell mass"
            },
            "correct": "A",
            "feedback_correct": "Correct. Faster cell growth means faster metabolism, which produces waste products (ammonia, lactate, CO2) at higher rates. When these toxic byproducts accumulate beyond threshold concentrations, they inhibit cell division and can cause cell death. This is a negative feedback loop in the system.",
            "feedback_incorrect": "Think about what happens at the metabolic level when cells are growing as fast as possible. Every nutrient consumed produces metabolic byproducts. What happens when those byproducts are generated faster than they can be removed?"
        },
        {
            "question": "A cultured meat company scales their bioreactor from 1 liter to 10,000 liters. The per-kilogram cost decreases by 80% for some components but Oxygen Supply becomes a critical bottleneck. Which physical principle BEST explains why oxygen delivery fails at large scale?",
            "choices": {
                "A": "Oxygen molecules are too large to penetrate dense cell cultures",
                "B": "Oxygen diffusion is limited to approximately 200 micrometers from the source, and larger bioreactors have more cells located far from oxygen delivery surfaces",
                "C": "Large bioreactors generate too much heat for oxygen to remain dissolved",
                "D": "Oxygen is consumed by chemical reactions with the nutrient medium before reaching cells"
            },
            "correct": "B",
            "feedback_correct": "Correct. Oxygen diffusion in liquid is limited to approximately 200 micrometers before concentration drops below what cells need. In a small bioreactor, most cells are within this distance of a gas-liquid interface. At large scale, cells deep in the culture become hypoxic, limiting tissue thickness and cell viability.",
            "feedback_incorrect": "Consider the physics of gas diffusion in liquid. Oxygen dissolves at the surface and diffuses inward, but it is consumed by cells along the way. How does increasing the volume change the ratio of surface area to volume?"
        },
        {
            "question": "A model shows that improving Scaffold Structure increases Texture Quality but also increases Production Cost. A student argues that the scaffold cost is acceptable because consumers will pay more for a steak-like product than a paste-like product. This reasoning is BEST described as:",
            "choices": {
                "A": "An optimization trade-off analysis that considers market value alongside production cost to determine overall economic viability",
                "B": "A scientific error because cost and quality should never be compared",
                "C": "An irrelevant business consideration with no connection to the biological model",
                "D": "A misunderstanding of how scaffolds work in cell culture"
            },
            "correct": "A",
            "feedback_correct": "Correct. Engineering optimization often requires evaluating trade-offs in terms of overall value, not just minimizing a single variable. If improved texture commands a higher market price, the increased scaffold cost may be justified by increased revenue per kilogram.",
            "feedback_incorrect": "In real-world engineering problems, optimization involves balancing multiple constraints including cost, quality, and market value. Is a higher production cost always bad if it enables a higher-value product?"
        },
        {
            "question": "Two bioreactor designs produce cultured meat at the same cost. Design A uses 40% less energy but produces meat with lower Texture Quality. Design B uses more energy but achieves steak-like texture. From an environmental sustainability perspective, which analysis is MOST complete?",
            "choices": {
                "A": "Design A is always more sustainable because it uses less energy",
                "B": "Design B is always more sustainable because higher quality means less food waste",
                "C": "The comparison requires life-cycle analysis including energy source (renewable vs. fossil fuel), consumer acceptance (which affects adoption rate and displacement of conventional meat), and waste stream differences",
                "D": "Environmental sustainability is irrelevant to cultured meat design"
            },
            "correct": "C",
            "feedback_correct": "Correct. Sustainability assessment requires life-cycle analysis. Design A's lower energy use matters less if powered by fossil fuels than Design B powered by renewables. Consumer acceptance affects total market displacement of conventional meat. A thorough analysis considers the entire system, not just one variable.",
            "feedback_incorrect": "Consider all the factors that determine environmental impact. Energy quantity is one input, but what about energy source, consumer adoption rates (which affect how much conventional meat is displaced), and the full product lifecycle?"
        },
        {
            "question": "A student's model reveals that increasing Scale Factor from lab to commercial production reduces per-kilogram Production Cost but introduces new challenges not present at lab scale. Which challenge is MOST directly a consequence of the scale-up?",
            "choices": {
                "A": "The chemistry of cell growth changes at larger volumes",
                "B": "Maintaining uniform temperature, oxygen, and nutrient distribution throughout a large bioreactor volume becomes exponentially more difficult, creating zones of cell death",
                "C": "Larger bioreactors require different cell types",
                "D": "Commercial bioreactors cannot be sterilized"
            },
            "correct": "B",
            "feedback_correct": "Correct. In a small bioreactor, mixing ensures relatively uniform conditions throughout. At commercial scale (10,000+ liters), maintaining homogeneous temperature, oxygen, nutrient concentration, and waste removal across the entire volume is a fundamental engineering challenge. Heterogeneity creates dead zones where conditions are suboptimal.",
            "feedback_incorrect": "Think about the physics of mixing and diffusion. What happens when you scale a well-mixed 1-liter container to a 10,000-liter vessel? Can you ensure every cell in the larger volume experiences the same conditions?"
        }
    ]
}

L05_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "COVID-19 is believed to have originated when a virus jumped from an animal species to humans. This type of cross-species infection event is called:",
            "choices": {
                "A": "Horizontal gene transfer",
                "B": "Zoonotic spillover",
                "C": "Symbiotic exchange",
                "D": "Antigenic shift"
            },
            "correct": "B",
            "feedback_correct": "Correct. Zoonotic spillover occurs when a pathogen crosses the species barrier from an animal host to a human. Most emerging infectious diseases (HIV, Ebola, SARS, COVID-19) originated through zoonotic spillover events.",
            "feedback_incorrect": "Consider the term for a pathogen 'spilling over' from its animal reservoir into the human population. This is distinct from mutations that occur within an already-circulating human pathogen."
        },
        {
            "question": "When a completely new virus infects humans for the first time, why does it often spread rapidly through the population?",
            "choices": {
                "A": "New viruses are always more deadly than existing ones",
                "B": "The human population has no pre-existing immunity to the novel pathogen, so virtually everyone is susceptible",
                "C": "New viruses can only spread through water supplies",
                "D": "Hospitals are unable to diagnose new viruses"
            },
            "correct": "B",
            "feedback_correct": "Correct. Immune naivety means the entire human population lacks antibodies or immune memory against the new pathogen. With no pre-existing immunity, every person exposed is a potential host, enabling explosive epidemic growth that would not occur with a familiar pathogen.",
            "feedback_incorrect": "Think about the role of the immune system. When your body has encountered a pathogen before, immune memory enables a rapid response. What happens when nobody has ever been exposed?"
        },
        {
            "question": "Deforestation and expansion of agriculture into wildlife habitats are considered risk factors for pandemic emergence. Which reasoning BEST explains this connection?",
            "choices": {
                "A": "Trees release antiviral compounds that protect nearby human populations",
                "B": "Destroying wildlife habitat increases the frequency of contact between humans and wild animals that carry novel viruses",
                "C": "Deforestation directly creates new viruses through environmental pollution",
                "D": "Agricultural animals are immune to all wildlife viruses"
            },
            "correct": "B",
            "feedback_correct": "Correct. As humans encroach into wildlife habitats through deforestation, farming, and urbanization, the frequency of contact between humans and wild animals (and their pathogens) increases. Each contact event is an opportunity for zoonotic spillover.",
            "feedback_incorrect": "Consider the spatial relationship between humans and wildlife. When forests are cleared for farms, what happens to the animals that lived there, and how does that change the frequency of human-animal interactions?"
        },
        {
            "question": "A new respiratory virus is detected in a rural village of 200 people. Which factor would MOST increase the risk of this local outbreak becoming a global pandemic?",
            "choices": {
                "A": "The village is located at high altitude",
                "B": "The village has a major airport or highway connection to densely populated cities",
                "C": "The village has abundant medical supplies",
                "D": "The virus causes visible symptoms within hours"
            },
            "correct": "B",
            "feedback_correct": "Correct. Travel connectivity determines how quickly a local outbreak reaches other populations. A village connected to major transportation networks can seed infections in distant cities within days, far outpacing containment efforts.",
            "feedback_incorrect": "Think about what enables a pathogen to spread from a small, localized population to the entire world. What infrastructure connects remote locations to major population centers?"
        },
        {
            "question": "During the early weeks of COVID-19, different countries detected and responded to the outbreak at different speeds. Based on pandemic science, which factor MOST LIKELY determined whether a country contained the outbreak or experienced widespread community transmission?",
            "choices": {
                "A": "The genetic makeup of the country's population",
                "B": "The speed of surveillance detection and implementation of containment measures such as testing, contact tracing, and isolation",
                "C": "The country's average temperature and humidity",
                "D": "The number of hospitals in the country"
            },
            "correct": "B",
            "feedback_correct": "Correct. Surveillance speed and intervention speed are the most critical determinants of outbreak trajectory. Countries that rapidly detected cases, implemented widespread testing, and isolated infected individuals (like South Korea and Taiwan) contained spread far more effectively than those with delayed responses.",
            "feedback_incorrect": "Consider what actions can be taken between the first infection and widespread community transmission. What capabilities determine whether that critical window of opportunity is used effectively?"
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A pandemic prediction model shows that reducing Surveillance Detection Speed from 28 days to 7 days decreases total predicted infections by 95%. Which systems-level principle explains why this relatively modest intervention has such a disproportionately large effect?",
            "choices": {
                "A": "Earlier detection allows containment during the exponential growth phase when case numbers are still small enough to trace and isolate",
                "B": "Faster detection automatically cures infected patients",
                "C": "Surveillance somehow reduces the mutation rate of the virus",
                "D": "The 95% reduction is coincidental and does not reflect a causal relationship"
            },
            "correct": "A",
            "feedback_correct": "Correct. During exponential growth, case counts double at regular intervals. At 7 days, there may be dozens of cases that can be individually traced and isolated. By 28 days, those dozens have become thousands or millions, making containment impossible. Early intervention operates during the period when each individual case still matters.",
            "feedback_incorrect": "Think about exponential growth. If cases double every 3 days, how many cases exist after 7 days versus 28 days? What does that mean for the feasibility of case-by-case containment?"
        },
        {
            "question": "A student's model identifies a geographic region as a 'pandemic hotspot' based on four overlapping risk factors. Which combination of factors represents the MOST scientifically valid set of hotspot indicators?",
            "choices": {
                "A": "High wildlife diversity, rapid deforestation, dense human population, and limited healthcare infrastructure",
                "B": "Cold climate, low population density, advanced hospitals, and strict border controls",
                "C": "High altitude, oceanic climate, rural population, and abundant wildlife veterinarians",
                "D": "Urban development, low wildlife diversity, high vaccination rates, and minimal travel"
            },
            "correct": "A",
            "feedback_correct": "Correct. Pandemic hotspots occur where high wildlife diversity (more potential reservoir species) overlaps with rapid deforestation (increasing human-wildlife contact), dense human populations (enabling human-to-human transmission), and limited healthcare (delayed detection and response). These factors collectively maximize spillover probability and minimize containment capacity.",
            "feedback_incorrect": "Consider each step in the pandemic emergence pathway: spillover requires wildlife-human contact, which is increased by habitat destruction. Spread requires human density. Containment failure requires weak surveillance. Which combination captures all these risk factors?"
        },
        {
            "question": "A model simulation shows that a virus with a Viral Mutation Rate 10x higher than average produces successful zoonotic spillover events 3x more frequently. However, only 1 in 50 spillover events leads to sustained human-to-human transmission. What does this reveal about pandemic emergence?",
            "choices": {
                "A": "Most pandemics are caused by viruses with low mutation rates",
                "B": "Spillover events are necessary but not sufficient for pandemic emergence; the virus must also acquire mutations enabling efficient human-to-human transmission, which is a rare additional evolutionary step",
                "C": "Mutation rate has no relationship to pandemic risk",
                "D": "If spillover occurs 50 times, a pandemic is guaranteed"
            },
            "correct": "B",
            "feedback_correct": "Correct. Spillover is the first barrier, but sustained human-to-human transmission requires additional adaptations (receptor binding optimization, airborne transmission capability, immune evasion). Most spillover events are evolutionary dead ends. Pandemic emergence requires crossing multiple biological barriers, each with its own probability.",
            "feedback_incorrect": "Think of pandemic emergence as a multi-step process, not a single event. A virus must first jump to humans (spillover) AND then evolve the ability to spread between humans. Why are most spillover events 'dead ends'?"
        },
        {
            "question": "A student compares two intervention strategies in the pandemic model: (1) reducing Wildlife-Human Contact Rate by 50% and (2) improving Surveillance Detection Speed by 50%. The model shows Strategy 2 prevents more pandemics. Which analysis BEST explains this result?",
            "choices": {
                "A": "Reducing contact is irrelevant to pandemic prevention",
                "B": "Contact reduction prevents spillover events but has diminishing returns because some level of human-wildlife interaction is unavoidable; surveillance improvement is effective against ALL spillover events regardless of how they occur",
                "C": "Surveillance is always cheaper than habitat protection",
                "D": "Contact reduction increases mutation rate, which cancels out the benefit"
            },
            "correct": "B",
            "feedback_correct": "Correct. Reducing contact rate decreases the frequency of spillover opportunities but cannot eliminate them entirely because human-wildlife interaction is unavoidable in agriculture, conservation, and daily life. Improved surveillance operates downstream, catching and containing spillover events regardless of their source, making it a more robust intervention point.",
            "feedback_incorrect": "Consider where each intervention acts in the pandemic emergence pathway. Contact reduction targets the first step (spillover), but can it eliminate all risk? Surveillance improvement targets the detection step. Which intervention is effective against a broader range of scenarios?"
        },
        {
            "question": "A pandemic prediction model shows that two scenarios with identical Zoonotic Spillover Probability produce vastly different outcomes: Scenario A results in 50 total cases while Scenario B results in 5 million cases. Which pair of variable differences MOST PLAUSIBLY explains the divergent outcomes?",
            "choices": {
                "A": "Scenario B had higher Viral Mutation Rate and lower Immune Naivety",
                "B": "Scenario B had higher Population Density and Travel Connectivity combined with slower Surveillance Detection Speed",
                "C": "Scenario B occurred in a warmer climate with more rainfall",
                "D": "Scenario B involved a different animal reservoir species"
            },
            "correct": "B",
            "feedback_correct": "Correct. Once spillover occurs, the trajectory depends on spread and detection variables. High Population Density provides more potential contacts, Travel Connectivity exports cases to other regions before containment, and slow Surveillance delays the response. Together, these variables determine whether a spillover becomes a contained cluster or a global pandemic.",
            "feedback_incorrect": "Both scenarios start with the same spillover probability, so the difference lies in what happens AFTER the first human infection. Which variables determine whether those initial cases are contained or amplified into millions?"
        }
    ]
}

L06_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Plastic pollution is considered a persistent environmental problem because most plastics do not break down naturally. Which property of synthetic polymers BEST explains their environmental persistence?",
            "choices": {
                "A": "Plastics are too heavy for natural decomposition processes to affect",
                "B": "The chemical bonds in synthetic polymers did not exist in nature before humans created them, so no organisms have evolved enzymes to break them down efficiently",
                "C": "Plastics are made of organic materials that decompose rapidly",
                "D": "All plastics dissolve in salt water within a few decades"
            },
            "correct": "B",
            "feedback_correct": "Correct. Synthetic polymers like PET and polyethylene were invented in the 20th century. Natural decomposer organisms have had millions of years to evolve enzymes for breaking down natural polymers (cellulose, chitin), but synthetic polymers are too new for efficient enzymatic degradation to have evolved naturally.",
            "feedback_incorrect": "Consider why natural decomposition processes (bacteria, fungi) can break down wood, leaves, and bone but not plastic bottles. What would an organism need to degrade a material that has only existed for about 100 years?"
        },
        {
            "question": "In 2016, scientists discovered a bacterium (Ideonella sakaiensis) that can break down PET plastic. This bacterium produces an enzyme called PETase. What does this discovery suggest about the possibility of using biology to address plastic pollution?",
            "choices": {
                "A": "The plastic pollution problem has already been solved",
                "B": "Natural evolution has begun producing organisms that can degrade synthetic plastics, and these enzymes could potentially be engineered for faster, more efficient plastic degradation",
                "C": "PETase can only work on one specific piece of plastic",
                "D": "Bacteria should not be used for environmental applications because they are dangerous"
            },
            "correct": "B",
            "feedback_correct": "Correct. The discovery of PETase proves that enzymatic plastic degradation is biologically possible. Scientists can now use protein engineering and synthetic biology to enhance PETase activity, improve its temperature tolerance, and design organisms with complete degradation pathways.",
            "feedback_incorrect": "The natural PETase enzyme is slow and limited, but its existence demonstrates a principle. What does it tell us about the possibility of engineering better versions?"
        },
        {
            "question": "A synthetic biologist proposes releasing an engineered plastic-eating organism into the ocean. Which concern is MOST scientifically justified?",
            "choices": {
                "A": "The organism might evolve to eat metal instead of plastic",
                "B": "Releasing self-replicating engineered organisms into open environments creates unpredictable ecological risks because their interactions with natural ecosystems cannot be fully controlled or reversed",
                "C": "Engineered organisms cannot survive outside laboratory conditions",
                "D": "The ocean is too salty for any microorganism to survive"
            },
            "correct": "B",
            "feedback_correct": "Correct. The containment challenge is a central issue in environmental synthetic biology. Self-replicating organisms that are released into open environments can evolve, spread, and interact with native ecosystems in unpredictable ways. Unlike chemical cleanups, biological releases are essentially irreversible.",
            "feedback_incorrect": "Consider the unique property of living organisms compared to chemical treatments. What happens when you release something that can reproduce, evolve, and interact with other living things in an uncontrolled environment?"
        },
        {
            "question": "An enzyme breaks down PET plastic most efficiently at 65 degrees C in a laboratory setting. Why would this be a significant limitation for using the enzyme to clean up ocean plastic pollution?",
            "choices": {
                "A": "Ocean water is too clean for the enzyme to function",
                "B": "Average ocean temperature is approximately 15 degrees C, far below the enzyme's optimal temperature, which would dramatically reduce its catalytic activity",
                "C": "Enzymes cannot function in salt water",
                "D": "The ocean does not contain PET plastic"
            },
            "correct": "B",
            "feedback_correct": "Correct. Enzyme activity is highly temperature-dependent. An enzyme optimized for 65 degrees C would lose 80-95% of its catalytic activity at 15 degrees C ocean temperatures. This is why engineering cold-active enzyme variants is a critical challenge for environmental bioremediation.",
            "feedback_incorrect": "Consider how temperature affects enzyme kinetics. Enzymes have optimal temperature ranges, and their activity decreases significantly outside those ranges. How does this affect real-world deployment?"
        },
        {
            "question": "Metabolic engineering involves modifying an organism's biochemical pathways to enable new capabilities. In the context of plastic degradation, why is it insufficient to simply add a plastic-breaking enzyme to an organism?",
            "choices": {
                "A": "The organism also needs a complete metabolic pathway to process the breakdown products into harmless compounds and usable energy, not just break the plastic into potentially toxic intermediates",
                "B": "Enzymes cannot be added to organisms",
                "C": "Organisms already have all the enzymes they need",
                "D": "Plastic-breaking enzymes are too large to fit inside a cell"
            },
            "correct": "A",
            "feedback_correct": "Correct. PETase breaks PET into terephthalic acid and ethylene glycol. Without additional enzymes to further process these intermediates, they accumulate and can be more toxic than the original plastic. Complete bioremediation requires a full pathway from polymer to harmless end products.",
            "feedback_incorrect": "Think about what happens after the enzyme breaks the first bond in a plastic polymer. The initial breakdown products are not the final, harmless products. What additional biochemistry is needed?"
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's model shows that maximizing Enzyme Activity Level increases Degradation Rate in the lab but actually DECREASES overall environmental remediation effectiveness when Metabolic Pathway Efficiency is low. Which explanation BEST accounts for this counterintuitive result?",
            "choices": {
                "A": "High enzyme activity breaks plastic into intermediate compounds faster than the metabolic pathway can process them, leading to accumulation of toxic byproducts that may be more harmful than the original plastic",
                "B": "Enzyme activity and degradation rate are always positively correlated",
                "C": "The model is incorrect because higher enzyme activity should always produce better outcomes",
                "D": "Environmental conditions reduce enzyme activity to zero"
            },
            "correct": "A",
            "feedback_correct": "Correct. This is a rate-mismatch problem. When the first enzyme in a pathway works faster than downstream enzymes, intermediates accumulate. If those intermediates are toxic (as terephthalic acid can be), the fast first step actually worsens the pollution problem. The system must be optimized holistically, not component by component.",
            "feedback_incorrect": "Think of the degradation pathway as an assembly line. What happens when the first station works much faster than all the subsequent stations? Where do the partially processed products accumulate?"
        },
        {
            "question": "A simulation comparing lab conditions versus ocean deployment shows that Degradation Rate drops by 90% when the organism is moved to ocean conditions. The student identifies Environmental Temperature as the primary factor. Which additional factor would create the SECOND largest performance reduction?",
            "choices": {
                "A": "Substrate Concentration, because ocean plastic is dispersed across vast areas rather than concentrated in a beaker, reducing the frequency of enzyme-plastic contact",
                "B": "The color of the ocean water",
                "C": "The depth of the ocean floor",
                "D": "The presence of fish in the ocean"
            },
            "correct": "A",
            "feedback_correct": "Correct. In a lab, plastic substrate can be concentrated in a small volume, ensuring frequent enzyme-substrate contact. In the ocean, plastic is distributed across millions of square kilometers at very low density, meaning the engineered organisms rarely encounter plastic particles. Enzyme kinetics depend on substrate availability.",
            "feedback_incorrect": "Consider the difference between a concentrated laboratory culture and the open ocean. In enzyme kinetics, the rate of reaction depends on how frequently enzymes encounter their substrate. How does the vast dilution of the ocean affect this?"
        },
        {
            "question": "The containment-effectiveness paradox states that maximizing Containment Level reduces ecological risk but also limits Degradation Rate. A student proposes using an organism with an engineered 'kill switch' that causes cell death if a specific chemical is absent. What does this design achieve?",
            "choices": {
                "A": "It eliminates all ecological risk while maintaining maximum degradation capacity",
                "B": "It provides a recall mechanism so the organism can be stopped by withdrawing the chemical, but limits the organism's range to areas where the chemical is actively supplied",
                "C": "Kill switches make the organism more dangerous because it could evolve to ignore the switch",
                "D": "Kill switches have no practical function in environmental applications"
            },
            "correct": "B",
            "feedback_correct": "Correct. A kill switch dependent on an externally supplied chemical (auxotrophy) means the organism can only survive where that chemical is provided. This limits its geographic spread but also limits its reach to areas where the plastic is. The paradox remains: containment and effectiveness are fundamentally opposed for dispersed pollutants.",
            "feedback_incorrect": "Consider how a chemical dependency creates geographic control. The organism survives only where the chemical is supplied. What does this mean for its ability to reach plastic scattered across the open ocean?"
        },
        {
            "question": "A research team compares three organism designs for ocean plastic cleanup: Design A has high Enzyme Activity but low pH Tolerance, Design B has moderate Enzyme Activity with broad pH Tolerance, and Design C has the highest Enzyme Activity but requires warm temperatures (50 degrees C). For deployment across diverse ocean environments, which design is MOST viable and why?",
            "choices": {
                "A": "Design C, because maximum enzyme activity always produces the best results",
                "B": "Design A, because pH variation in the ocean is minimal",
                "C": "Design B, because moderate activity across a broad range of environmental conditions produces more total degradation than high activity that only functions in narrow conditions",
                "D": "All three designs would perform identically in the ocean"
            },
            "correct": "C",
            "feedback_correct": "Correct. This is a robustness versus peak performance trade-off. Design B's moderate enzyme activity across broad conditions means it functions in more ocean environments (varying pH zones, coastal versus deep water) than designs that achieve higher peak activity but only in narrow conditions. Total real-world degradation depends on operating range, not just peak capacity.",
            "feedback_incorrect": "Think about the diversity of ocean environments: different pH levels, temperatures, and oxygen concentrations across different regions and depths. Which design functions in the most environments, and therefore degrades the most total plastic?"
        },
        {
            "question": "After analyzing the model, a student concludes that engineering a single organism to solve ocean plastic pollution is insufficient and proposes a multi-organism system instead. Which argument BEST supports this systems-level approach?",
            "choices": {
                "A": "Using multiple organisms is always better than using one",
                "B": "Different organisms could be optimized for different plastic types (PET, polyethylene, polystyrene), different environmental conditions (warm vs. cold, shallow vs. deep), and different stages of degradation (initial breakdown vs. intermediate processing), creating a more complete and resilient remediation system",
                "C": "Multiple organisms would compete with each other and reduce effectiveness",
                "D": "Regulatory agencies require multiple organisms for any environmental release"
            },
            "correct": "B",
            "feedback_correct": "Correct. Ocean plastic pollution involves multiple polymer types distributed across diverse environmental conditions. No single organism can be optimized for all plastic types, all temperatures, all pH levels, and all stages of degradation. A consortium approach mirrors natural ecosystem division of labor, where different species specialize in different functions.",
            "feedback_incorrect": "Consider the diversity of the plastic pollution problem: multiple plastic types, multiple environmental conditions, and multiple stages of chemical degradation. Can any single organism be optimally designed for all of these simultaneously?"
        }
    ]
}

L07_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Fossil fuels (oil, coal, natural gas) are considered non-renewable resources. Which statement BEST explains why scientists are working to develop alternative fuel sources?",
            "choices": {
                "A": "Fossil fuels are too expensive for most countries to afford",
                "B": "Fossil fuel reserves are finite and their combustion releases greenhouse gases that drive climate change, creating both supply and environmental sustainability crises",
                "C": "Fossil fuels are a recent discovery and we have not yet learned how to use them efficiently",
                "D": "Alternative fuels have already replaced fossil fuels in most applications"
            },
            "correct": "B",
            "feedback_correct": "Correct. Fossil fuels are finite geological resources formed over millions of years. Their combustion releases stored carbon as CO2, contributing to climate change. Developing renewable alternatives addresses both resource depletion and environmental impact.",
            "feedback_incorrect": "Consider the two fundamental problems with fossil fuel dependence: one is about supply (how much is left) and one is about impact (what happens when we burn it). Which answer addresses both?"
        },
        {
            "question": "Microorganisms like yeast have been used for thousands of years to ferment sugars into ethanol (alcohol). How does modern metabolic engineering differ from traditional fermentation?",
            "choices": {
                "A": "Modern metabolic engineering uses larger fermentation vessels",
                "B": "Metabolic engineering modifies the organism's genetic pathways to produce specific desired products more efficiently, rather than relying on the organism's natural metabolic capabilities",
                "C": "Traditional fermentation produces ethanol while modern methods cannot",
                "D": "There is no meaningful difference between the two approaches"
            },
            "correct": "B",
            "feedback_correct": "Correct. Traditional fermentation relies on organisms' natural metabolic capabilities. Metabolic engineering redesigns those pathways, adding new enzyme genes, deleting competing pathways, and optimizing regulatory elements to redirect cellular resources toward a specific product like advanced biofuels.",
            "feedback_incorrect": "Consider the difference between using an organism as-is versus deliberately modifying its internal biochemistry to redirect its metabolism toward a product it would not naturally produce at useful levels."
        },
        {
            "question": "A cell converts glucose into energy through a series of enzyme-catalyzed reactions. If you wanted a cell to produce biofuel instead of its normal products, what would you need to change?",
            "choices": {
                "A": "Feed the cell a different sugar",
                "B": "Add new enzyme genes that redirect metabolic intermediates toward fuel molecules instead of the cell's normal products",
                "C": "Increase the temperature to force different reactions",
                "D": "Remove all of the cell's original DNA"
            },
            "correct": "B",
            "feedback_correct": "Correct. Metabolic engineering introduces new enzymatic steps (via gene insertion) that divert carbon from normal metabolic pathways toward desired fuel molecules. The cell's existing pathways provide the precursors, and engineered enzymes redirect them toward biofuel production.",
            "feedback_incorrect": "Think about metabolism as a network of enzyme-catalyzed reactions. Each enzyme catalyzes a specific conversion. To create a new product, you need to insert what at the appropriate branch point in the network?"
        },
        {
            "question": "An engineer observes that when a microbial biofuel pathway is pushed to maximum production, the cells grow very slowly and sometimes die. Which concept BEST explains this observation?",
            "choices": {
                "A": "The biofuel product is always toxic to cells",
                "B": "The engineered pathway competes with the cell's own essential processes for shared resources like energy, amino acids, and ribosomes, creating a metabolic burden that compromises cell viability",
                "C": "The cells are allergic to the engineered genes",
                "D": "Maximum production always kills cells regardless of the product"
            },
            "correct": "B",
            "feedback_correct": "Correct. Cells have finite resources. Ribosomes making engineered pathway enzymes are not available for making essential cellular proteins. ATP spent on the biofuel pathway is not available for cell maintenance. This resource competition is called metabolic burden.",
            "feedback_incorrect": "Consider a factory analogy: if you reassign most of your workers to a new product line, who maintains the building, runs the cafeteria, and keeps the lights on? Cells face the same resource allocation problem."
        },
        {
            "question": "Many biochemical reactions require helper molecules called cofactors (such as NAD+/NADH and ATP/ADP) to proceed. Why is cofactor availability important in metabolic engineering?",
            "choices": {
                "A": "Cofactors are only needed in small quantities and never limit reactions",
                "B": "Engineered pathways may consume cofactors faster than the cell can regenerate them, causing the entire pathway to stall even if all enzymes are present and active",
                "C": "Cofactors are only important in animal cells, not microbes",
                "D": "Cofactors are catalysts that are never consumed in reactions"
            },
            "correct": "B",
            "feedback_correct": "Correct. Cofactors like NADH and ATP are recycled, not created from scratch for each reaction. If an engineered pathway consumes NAD+ to NADH faster than the cell regenerates NAD+, the cofactor pool becomes imbalanced and pathway flux stalls, regardless of enzyme availability.",
            "feedback_incorrect": "Cofactors participate in reactions and must be recycled back to their original form. Consider what happens when an engineered pathway uses a cofactor at a rate that exceeds the cell's ability to regenerate it."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's model shows that setting all pathway enzymes to maximum expression DECREASES total biofuel Fermentation Efficiency compared to a moderately expressed pathway. Which systems-level explanation BEST accounts for this paradox?",
            "choices": {
                "A": "Maximum enzyme expression creates extreme Metabolic Burden that crashes Cell Growth Rate, resulting in fewer total cells producing less total product despite each cell's pathway being theoretically more active",
                "B": "The model contains a mathematical error",
                "C": "Enzyme expression level has no effect on biofuel production",
                "D": "Maximum expression always improves production in real biological systems"
            },
            "correct": "A",
            "feedback_correct": "Correct. This is the central paradox of metabolic engineering. Total productivity = per-cell production x number of cells. Maximum enzyme expression may increase per-cell production capacity but simultaneously crashes cell growth through metabolic burden. The optimal expression level balances per-cell yield against population growth.",
            "feedback_incorrect": "Total biofuel production depends on two factors: how much each cell produces AND how many cells there are. What happens to the second factor when the first is pushed to its absolute maximum?"
        },
        {
            "question": "A model simulation reveals that a pathway bottleneck at the third enzymatic step limits overall Pathway Flux to 30% of theoretical maximum, even though all other enzymes operate at near-maximum capacity. Which optimization strategy is MOST effective?",
            "choices": {
                "A": "Increase expression of ALL enzymes to compensate for the bottleneck",
                "B": "Increase expression of only the bottleneck enzyme (step 3) while maintaining other enzyme levels, to relieve the specific rate-limiting step without adding unnecessary metabolic burden",
                "C": "Remove the bottleneck enzyme entirely so flux bypasses it",
                "D": "Decrease expression of the bottleneck enzyme to reduce competition"
            },
            "correct": "B",
            "feedback_correct": "Correct. In a metabolic pathway, overall flux is limited by the slowest step (the bottleneck). Increasing non-bottleneck enzymes wastes resources without improving flux. Targeted overexpression of only the bottleneck enzyme relieves the rate-limiting step with minimal additional metabolic burden.",
            "feedback_incorrect": "Think of a pathway as water flowing through pipes of different diameters. If one pipe is narrower than the others, what is the most efficient way to increase total flow? Do you need to widen all pipes, or just the narrowest one?"
        },
        {
            "question": "A student observes that Byproduct Accumulation of acetate above 8 g/L inhibits further Cell Growth Rate in their model. Which intervention would MOST effectively address this problem?",
            "choices": {
                "A": "Increase Substrate Concentration to overwhelm the acetate production",
                "B": "Engineer the organism to delete or downregulate the acetate-producing pathway while simultaneously using continuous fermentation with real-time acetate removal",
                "C": "Accept acetate accumulation as an unavoidable consequence",
                "D": "Increase bioreactor temperature to evaporate the acetate"
            },
            "correct": "B",
            "feedback_correct": "Correct. A two-pronged approach is most effective: genetic engineering eliminates or reduces the metabolic branch that produces acetate (redirecting carbon toward the desired product), while process engineering (continuous fermentation with in-line removal) prevents any residual acetate from reaching inhibitory concentrations.",
            "feedback_incorrect": "Byproduct accumulation is both a carbon diversion problem (lost yield) and a toxicity problem (growth inhibition). What combination of genetic and process engineering strategies addresses both aspects simultaneously?"
        },
        {
            "question": "An economic analysis within the model shows that achieving 85% of theoretical maximum Product Yield at titers above 50 g/L is required for commercial viability. Current laboratory strains achieve 45% yield at 15 g/L. Which assessment MOST accurately characterizes the engineering challenge?",
            "choices": {
                "A": "The gap is too large to ever close with current technology",
                "B": "The gap requires simultaneous optimization of pathway flux, cofactor balance, byproduct elimination, metabolic burden management, and fermentation conditions, representing a multi-dimensional engineering challenge that must be solved as an integrated system",
                "C": "Simply running the fermentation longer will achieve the required titer",
                "D": "The economic targets are arbitrary and can be changed to match current performance"
            },
            "correct": "B",
            "feedback_correct": "Correct. The lab-to-commercial gap cannot be closed by optimizing any single variable. It requires integrated systems engineering: improving yield (pathway optimization), increasing titer (toxicity tolerance, continuous removal), reducing burden (balanced expression), and maintaining cofactor balance, all simultaneously within a viable cell.",
            "feedback_incorrect": "Consider that 45% to 85% yield AND 15 to 50 g/L titer are both required. These are different metrics that depend on different cellular processes. Can either be achieved by modifying just one aspect of the system?"
        },
        {
            "question": "A student's model demonstrates that reducing Enzyme Activity from maximum to 60% of maximum INCREASES total Fermentation Efficiency by 25%. The student claims this proves that 'less is more' in metabolic engineering. Which refinement makes this claim MORE scientifically precise?",
            "choices": {
                "A": "The claim is wrong because more enzyme activity should always be better",
                "B": "The optimal enzyme expression level is the one that maximizes the product of per-cell yield and cell growth rate, which occurs at an intermediate expression level where metabolic burden does not significantly impair cell viability",
                "C": "The improvement is due to random variation in the model",
                "D": "Reducing enzyme activity reduces product quality, making the comparison invalid"
            },
            "correct": "B",
            "feedback_correct": "Correct. Total productivity = (per-cell production rate) x (total cell number). Maximum enzyme expression maximizes the first term but minimizes the second through metabolic burden. The optimal expression level is where the product of both terms is maximized, which is always an intermediate value when burden is significant.",
            "feedback_incorrect": "The student's observation is real but needs quantitative framing. Total production is a function of BOTH per-cell yield and population size. At what enzyme expression level is this two-variable product maximized?"
        }
    ]
}

L08_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Every cell in your body contains the same DNA, yet a liver cell looks and functions completely differently from a neuron. Which mechanism BEST explains how identical genomes produce different cell types?",
            "choices": {
                "A": "Different cell types have different DNA sequences",
                "B": "Different cell types express different subsets of their shared genes, with some genes turned on and others turned off in each cell type",
                "C": "Cells randomly change their DNA after they divide",
                "D": "Only stem cells contain the complete genome"
            },
            "correct": "B",
            "feedback_correct": "Correct. Differential gene expression is the mechanism by which identical genomes produce diverse cell types. Transcription factors, epigenetic modifications, and signaling molecules determine which of the ~20,000 genes are active in each cell, creating the functional specialization observed in different tissues.",
            "feedback_incorrect": "Consider that a liver cell and a neuron have identical DNA sequences. If the DNA is the same, what must be different to produce different proteins and therefore different cell functions?"
        },
        {
            "question": "A transcription factor is a protein that binds to specific DNA sequences near a gene. What is the PRIMARY function of transcription factors in gene regulation?",
            "choices": {
                "A": "To physically copy the DNA during cell division",
                "B": "To increase or decrease the rate at which a gene is transcribed into mRNA, controlling how much protein that gene produces",
                "C": "To transport proteins from the nucleus to the cytoplasm",
                "D": "To provide structural support for the chromosome"
            },
            "correct": "B",
            "feedback_correct": "Correct. Transcription factors are regulatory proteins that bind to promoter or enhancer sequences and recruit or block RNA polymerase, thereby controlling the rate of mRNA synthesis. They are the molecular decision-makers of gene expression.",
            "feedback_incorrect": "The word 'transcription' refers to copying DNA into mRNA. A transcription 'factor' is something that influences this process. What would a protein that binds near a gene do to affect how much mRNA that gene produces?"
        },
        {
            "question": "In a feedback loop, the output of a process influences its own input. Which of the following is a biological example of negative feedback?",
            "choices": {
                "A": "A gene produces a protein that activates its own transcription, producing more and more protein",
                "B": "A gene produces a protein that represses its own transcription, maintaining a stable protein level",
                "C": "A gene is permanently silenced and never produces any protein",
                "D": "Two genes are transcribed at the same rate regardless of conditions"
            },
            "correct": "B",
            "feedback_correct": "Correct. When a gene product represses its own transcription, it creates a self-correcting system. If protein levels rise too high, increased repression reduces production. If levels drop too low, reduced repression allows more production. This maintains homeostasis.",
            "feedback_incorrect": "Negative feedback opposes change. Think about what happens when the output of a system acts to reduce its own production. Does the system stabilize or become unstable?"
        },
        {
            "question": "DNA methylation is a chemical modification that does not change the DNA sequence but can silence gene expression. This type of modification is called:",
            "choices": {
                "A": "A mutation",
                "B": "An epigenetic modification",
                "C": "A deletion",
                "D": "A point substitution"
            },
            "correct": "B",
            "feedback_correct": "Correct. Epigenetic modifications (epi = above/upon) alter gene expression without changing the DNA sequence itself. DNA methylation, histone modifications, and chromatin remodeling are epigenetic mechanisms that control gene accessibility and can be inherited through cell division.",
            "feedback_incorrect": "The prefix 'epi' means above or upon. What term describes modifications that sit 'on top of' the genetic code, affecting its expression without changing the sequence?"
        },
        {
            "question": "Cancer is often described as a disease of uncontrolled cell division. Which type of gene regulatory failure could MOST directly lead to uncontrolled cell growth?",
            "choices": {
                "A": "A mutation that permanently activates a gene promoting cell division, or permanently inactivates a gene that normally stops cell division",
                "B": "A mutation in a gene that controls hair color",
                "C": "Overexpression of a gene for muscle protein production",
                "D": "Complete silencing of all genes in the affected cell"
            },
            "correct": "A",
            "feedback_correct": "Correct. Cancer results from disrupted gene regulation: oncogenes (pro-growth genes) become permanently activated and/or tumor suppressor genes (anti-growth genes) become inactivated. Both types of regulatory failure remove the checks on cell division, enabling uncontrolled proliferation.",
            "feedback_incorrect": "Cell division is normally controlled by a balance between pro-growth and anti-growth signals. What happens when either the accelerator gets stuck or the brakes are removed?"
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's gene regulatory network model shows that doubling Transcription Factor Concentration doubles mRNA Transcription Rate but only increases final Protein Translation Rate by 30%. Which component MOST LIKELY creates this discrepancy?",
            "choices": {
                "A": "mRNA Degradation Rate, which destroys a significant fraction of the additional mRNA before it can be translated, and limited Ribosome Availability, which prevents all remaining mRNA from being simultaneously translated",
                "B": "Protein Degradation Rate alone accounts for the entire discrepancy",
                "C": "The DNA sequence limits how much protein can be produced",
                "D": "Transcription Factor Concentration has no effect on downstream protein levels"
            },
            "correct": "A",
            "feedback_correct": "Correct. Two attenuation points operate between mRNA production and protein output. First, mRNA is constantly degraded, so more rapid transcription only modestly increases steady-state mRNA levels. Second, ribosomes are a shared, limited resource, so even higher mRNA levels cannot all be translated simultaneously. Together, these factors dampen the signal at each level.",
            "feedback_incorrect": "Consider the multi-step cascade from transcription factor to protein. At each step, both production AND degradation operate simultaneously. If you double input at step 1, the output at step 3 depends on what happens at each intermediate step."
        },
        {
            "question": "A model simulation demonstrates that switching Feedback Signal Strength from negative to positive converts a system with stable, graded gene expression into a bistable switch with only two possible states (high or low). Which property of positive feedback BEST explains this behavior?",
            "choices": {
                "A": "Positive feedback is inherently destructive and crashes the system",
                "B": "When a protein activates its own gene, small increases in protein level trigger further increases, creating a self-reinforcing loop that drives the system to its maximum state; once at maximum, the loop maintains itself, making the high state self-sustaining and difficult to reverse",
                "C": "Positive feedback has no effect on gene expression dynamics",
                "D": "Positive feedback reduces protein levels by increasing degradation"
            },
            "correct": "B",
            "feedback_correct": "Correct. Positive autoregulation creates bistability. Above a threshold concentration, the protein activates its own gene sufficiently to maintain high expression indefinitely. Below the threshold, expression decays to the basal low state. The system 'locks in' to whichever state it reaches, creating a binary switch from a continuous input.",
            "feedback_incorrect": "Think about what happens when a protein promotes its own production. If protein levels increase slightly, this increases production, which increases protein levels further. Where does this cycle end?"
        },
        {
            "question": "In the model, increasing Epigenetic Modification (closing chromatin) at a gene locus renders the gene unresponsive to even high Transcription Factor Concentration. A student concludes that epigenetic silencing overrides transcription factor signaling. Which additional evidence from the model would STRENGTHEN this conclusion?",
            "choices": {
                "A": "Showing that the same transcription factor activates the gene normally when chromatin is open, demonstrating that the factor is functional and the silencing is specifically due to chromatin state, not transcription factor inactivity",
                "B": "Showing that epigenetic modification affects all genes in the genome equally",
                "C": "Demonstrating that transcription factors are destroyed by epigenetic modifications",
                "D": "Proving that closed chromatin cannot be reopened under any conditions"
            },
            "correct": "A",
            "feedback_correct": "Correct. This is a controlled comparison. By demonstrating that the same transcription factor successfully activates the gene when chromatin is open (control) but fails when chromatin is closed (experimental), the student isolates chromatin state as the variable responsible for silencing, ruling out transcription factor dysfunction as an alternative explanation.",
            "feedback_incorrect": "To strengthen a causal claim, you need a control condition. If the claim is that closed chromatin blocks gene activation, what control would demonstrate that the transcription factor itself is functional?"
        },
        {
            "question": "A model of a gene regulatory network shows that Negative Feedback produces stable output despite random fluctuations (noise) in Transcription Factor Concentration. Which property of negative feedback MOST directly explains this noise reduction?",
            "choices": {
                "A": "Negative feedback eliminates all molecular noise at the DNA level",
                "B": "When protein levels randomly rise above the set point, the feedback loop increases repression, pushing levels back down; when levels randomly drop below the set point, reduced repression allows levels to recover, creating a self-correcting homeostatic mechanism",
                "C": "Negative feedback slows all cellular processes equally",
                "D": "Negative feedback prevents transcription factors from binding to DNA"
            },
            "correct": "B",
            "feedback_correct": "Correct. Negative feedback acts as an error-correction mechanism. Any deviation from the steady-state protein level triggers a proportional opposing response. This self-correction dampens random fluctuations, maintaining consistent gene expression output despite the inherently noisy cellular environment.",
            "feedback_incorrect": "Think about a thermostat. When temperature rises above the set point, cooling activates. When it drops below, heating activates. The temperature fluctuates but stays near the set point. How does negative feedback in gene regulation achieve the same result?"
        },
        {
            "question": "A student analyzes how a mutation in a transcription factor that regulates cell cycle genes could lead to cancer. The model shows that the mutant transcription factor has increased Promoter Binding Affinity for pro-growth genes AND decreased binding to anti-growth genes. Which consequence does the model predict?",
            "choices": {
                "A": "Cell division rate remains unchanged because the two effects cancel out",
                "B": "Simultaneous overexpression of growth-promoting genes and underexpression of growth-inhibiting genes removes both the accelerator limit and the brakes on cell division, producing uncontrolled proliferation characteristic of cancer",
                "C": "The cell immediately dies because it cannot sustain high transcription rates",
                "D": "The mutation only affects one gene at a time and cannot cause systemic effects"
            },
            "correct": "B",
            "feedback_correct": "Correct. This dual disruption represents a 'two-hit' regulatory failure. Increased activation of oncogenes (accelerator) combined with decreased activation of tumor suppressors (brakes) removes two independent layers of growth control simultaneously, producing the unregulated cell division that defines cancer.",
            "feedback_incorrect": "Consider cell division as controlled by both accelerator (pro-growth) and brake (anti-growth) systems. What happens when a single mutation simultaneously increases one and decreases the other?"
        }
    ]
}

L09_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Vaccines work by training the immune system to recognize a pathogen before natural infection occurs. Which component of the immune system is MOST directly responsible for providing long-lasting protection after vaccination?",
            "choices": {
                "A": "Red blood cells, which carry oxygen to fight infection",
                "B": "Memory B cells and memory T cells, which 'remember' the pathogen and mount a rapid response upon future exposure",
                "C": "White blood cells that only live for a few hours",
                "D": "Antibiotics produced by the immune system"
            },
            "correct": "B",
            "feedback_correct": "Correct. Immunological memory is the basis of vaccination. Memory B cells can persist for decades and rapidly produce antibodies upon re-exposure, while memory T cells directly kill infected cells. This remembered response is faster and stronger than the initial response.",
            "feedback_incorrect": "Consider what makes vaccine protection last for months or years. Which immune cells persist long-term and 'remember' the pathogen?"
        },
        {
            "question": "COVID-19 vaccines were developed in under a year, while most vaccines historically take 10-15 years. Which factor MOST contributed to this acceleration?",
            "choices": {
                "A": "The COVID-19 virus was simpler than other viruses",
                "B": "mRNA vaccine technology, which had been in development for decades, allowed rapid design and manufacturing once the viral genome was sequenced",
                "C": "Safety testing was completely skipped to save time",
                "D": "COVID-19 vaccines were less effective than traditional vaccines but faster to produce"
            },
            "correct": "B",
            "feedback_correct": "Correct. mRNA vaccine technology had been researched for over 20 years before COVID-19. Once the SARS-CoV-2 spike protein sequence was published, scientists could design an mRNA vaccine within days. The platform technology was ready; it just needed the target sequence.",
            "feedback_incorrect": "Consider what technological advances were already in place before the pandemic. The speed came not from cutting corners but from having a platform ready to be customized for a new target."
        },
        {
            "question": "Influenza (flu) vaccines must be redesigned every year because the virus changes. What is the term for the gradual mutation of surface proteins that allows the virus to partially evade existing immunity?",
            "choices": {
                "A": "Genetic drift (random changes in allele frequency in small populations)",
                "B": "Antigenic drift, where small mutations accumulate in the virus's surface proteins",
                "C": "Horizontal gene transfer between viral strains",
                "D": "Planned obsolescence engineered by vaccine manufacturers"
            },
            "correct": "B",
            "feedback_correct": "Correct. Antigenic drift is the gradual accumulation of mutations in surface proteins (like hemagglutinin) that changes the virus's appearance to the immune system. This is why last year's flu vaccine becomes less effective against this year's strains.",
            "feedback_incorrect": "Distinguish between genetic drift (random population changes) and antigenic drift (viral surface protein changes). Which one specifically describes how viral mutations erode vaccine effectiveness over time?"
        },
        {
            "question": "An adjuvant is a substance added to vaccines to enhance the immune response. Why might a vaccine need an adjuvant rather than just the antigen alone?",
            "choices": {
                "A": "Adjuvants make the vaccine taste better",
                "B": "Some antigens alone produce a weak immune response, and adjuvants activate innate immune cells that amplify the adaptive immune response, enabling protection with lower antigen doses",
                "C": "Adjuvants prevent the vaccine from expiring",
                "D": "All vaccines require adjuvants; no vaccine works without one"
            },
            "correct": "B",
            "feedback_correct": "Correct. Adjuvants activate innate immune cells (dendritic cells, macrophages) that process and present the antigen more effectively to adaptive immune cells. This bridge between innate and adaptive immunity amplifies the response, allowing lower antigen doses to achieve protective immunity.",
            "feedback_incorrect": "Consider the two branches of the immune system: innate (rapid, nonspecific) and adaptive (slower, specific). How might enhancing the innate response improve the adaptive response to a vaccine antigen?"
        },
        {
            "question": "A scientist proposes designing a 'universal' vaccine that protects against all variants of a rapidly mutating virus. What is the fundamental challenge this approach faces?",
            "choices": {
                "A": "Universal vaccines are physically impossible to manufacture",
                "B": "Targeting highly conserved (unchanging) viral regions typically generates weaker immune responses than targeting variable regions, creating a trade-off between breadth of protection and strength of protection",
                "C": "All viral proteins mutate at the same rate, so there are no conserved targets",
                "D": "The immune system cannot recognize conserved viral proteins"
            },
            "correct": "B",
            "feedback_correct": "Correct. Conserved viral regions (which would provide broad protection) are often less immunogenic or less accessible on the virus surface than the highly variable regions that current vaccines target. Designing a vaccine that generates a strong response to conserved regions is the central challenge of universal vaccine design.",
            "feedback_incorrect": "Consider why viruses keep some regions constant (they are essential for function) and let other regions mutate (to escape immunity). Which regions do current vaccines target, and which regions would a universal vaccine need to target? What is the trade-off?"
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's vaccine model shows that a strain-specific vaccine targeting the dominant viral variant produces high Antibody Production Rate initially, but Duration of Immunity drops to near zero after 12 months as the virus undergoes antigenic drift. Which design modification would MOST effectively extend Duration of Immunity?",
            "choices": {
                "A": "Increasing Adjuvant Strength to maximum to produce more antibodies against the same strain",
                "B": "Switching Antigen Selection to target a conserved region that is shared across variants, accepting lower peak antibody levels in exchange for broader Cross-Reactivity that remains effective as the virus mutates",
                "C": "Administering the same strain-specific vaccine more frequently",
                "D": "Removing the adjuvant to reduce immune overstimulation"
            },
            "correct": "B",
            "feedback_correct": "Correct. The root cause of declining immunity is antigenic drift changing the target. More antibodies against an outdated target do not solve this. Targeting a conserved region trades peak antibody levels for durability, because the conserved target changes slowly even as the rest of the virus mutates.",
            "feedback_incorrect": "If the problem is that the virus mutates away from the vaccine target, does producing more antibodies against that same target solve the problem? What alternative targeting strategy addresses the mutation issue directly?"
        },
        {
            "question": "In the model, increasing Adjuvant Strength from 0 to moderate produces a large increase in Immune Cell Activation and Antibody Production Rate. Increasing from moderate to maximum produces only a small additional increase in protection but a large increase in side effects. This pattern is BEST described as:",
            "choices": {
                "A": "A linear dose-response relationship",
                "B": "Diminishing returns, where each additional unit of adjuvant produces progressively less additional benefit while side effects continue to increase proportionally, defining an optimal adjuvant level that maximizes the benefit-to-risk ratio",
                "C": "Evidence that adjuvants are unnecessary",
                "D": "A measurement error in the model"
            },
            "correct": "B",
            "feedback_correct": "Correct. Adjuvant dose-response follows a law of diminishing returns. The immune system has a finite capacity for activation, so beyond the saturation point, additional adjuvant stimulates marginal additional protection while continuing to increase inflammatory side effects. The optimal dose maximizes the ratio of benefit to adverse reactions.",
            "feedback_incorrect": "Graph the relationship: benefit rises steeply at low doses then plateaus, while side effects continue to increase. At what point is the gap between benefit and side effects maximized? That is the optimal dose."
        },
        {
            "question": "A model simulation shows that two vaccines with identical Antibody Production Rates produce very different long-term outcomes: Vaccine A provides protection for 6 months while Vaccine B provides protection for 10 years. Which component MOST LIKELY differs between them?",
            "choices": {
                "A": "Memory Cell Formation, where Vaccine B stimulates more robust differentiation of long-lived memory B cells and T cells that persist and rapidly reactivate upon pathogen re-exposure",
                "B": "The number of total antibodies produced during the initial response",
                "C": "The size of the injection needle used for administration",
                "D": "The color of the vaccine formulation"
            },
            "correct": "A",
            "feedback_correct": "Correct. Antibody levels wane over months as short-lived plasma cells die. Long-term protection depends on memory cells, which persist for years or decades. Vaccine B likely triggers more effective memory cell differentiation, enabling rapid recall responses that re-establish protective antibody levels upon future pathogen encounter.",
            "feedback_incorrect": "Short-term protection comes from circulating antibodies that wane over months. Long-term protection comes from something that persists much longer. What immune cell type provides this durable protection?"
        },
        {
            "question": "A vaccine designer uses the model to evaluate Population Coverage across a genetically diverse population. The model shows that the vaccine protects 95% of individuals with one HLA type but only 40% of individuals with a different HLA type. What does this reveal about vaccine design?",
            "choices": {
                "A": "The vaccine is defective and should not be used",
                "B": "Human genetic diversity in immune response genes (HLA) means the same antigen is presented differently to immune cells in different individuals, making it impossible to achieve equal protection across all genetic backgrounds with a single antigen design",
                "C": "HLA type has no effect on vaccine efficacy",
                "D": "Population coverage cannot be measured using computational models"
            },
            "correct": "B",
            "feedback_correct": "Correct. HLA molecules determine which peptide fragments of the antigen are presented to T cells. Different HLA types present different fragments, meaning the same vaccine antigen triggers different immune responses in different people. This genetic diversity is a fundamental challenge for universal vaccine design and often requires multi-epitope vaccines.",
            "feedback_incorrect": "HLA genes are among the most variable in the human genome. They determine which pieces of a pathogen's protein the immune system 'sees.' If different people's immune systems see different pieces, how does this affect vaccine effectiveness across a diverse population?"
        },
        {
            "question": "A student runs two simulations with identical vaccine designs but different Pathogen Mutation Rates. At low mutation rate, Cross-Reactivity maintains protection for 15 years. At high mutation rate, protection degrades after 2 years. Based on this analysis, which vaccine development strategy is MOST appropriate for a rapidly mutating pathogen?",
            "choices": {
                "A": "Design one perfect vaccine and administer it once",
                "B": "A platform technology (like mRNA) that can be rapidly updated to match new variants, combined with targeting of the most conserved epitopes to extend the effective period between updates",
                "C": "Abandon vaccination entirely for rapidly mutating pathogens",
                "D": "Increase the dose of the original vaccine to compensate for mutations"
            },
            "correct": "B",
            "feedback_correct": "Correct. For rapidly mutating pathogens, the strategy must combine two approaches: (1) target conserved regions to maximize the interval before updates are needed, and (2) use a platform technology that enables rapid redesign when updates become necessary. This is exactly the strategy used for COVID-19 variant-updated mRNA boosters.",
            "feedback_incorrect": "If the virus changes faster than any single vaccine can keep up with, what two-pronged approach combines durable design with the ability to rapidly update? Think about both the target choice and the manufacturing platform."
        }
    ]
}

L10_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "The greenhouse effect is a natural process that keeps Earth's surface warm enough to support life. Which statement BEST describes how human activities have altered this process?",
            "choices": {
                "A": "Humans have created the greenhouse effect, which did not exist before industrialization",
                "B": "Burning fossil fuels has increased atmospheric CO2 concentration, which enhances the natural greenhouse effect and causes additional warming beyond what would occur naturally",
                "C": "The greenhouse effect only affects greenhouse buildings, not the entire planet",
                "D": "Human activities have weakened the greenhouse effect, causing cooling"
            },
            "correct": "B",
            "feedback_correct": "Correct. The greenhouse effect existed naturally for billions of years. Human activities (primarily fossil fuel combustion and deforestation) have increased atmospheric CO2 from ~280 ppm (pre-industrial) to ~425 ppm, enhancing the effect and driving additional warming.",
            "feedback_incorrect": "Distinguish between the natural greenhouse effect (which has always existed and made Earth habitable) and the enhanced greenhouse effect caused by human activity. What specific change have humans made to the atmosphere?"
        },
        {
            "question": "A positive feedback loop in climate science refers to a process where warming causes changes that produce MORE warming. Which of the following is an example of a climate positive feedback loop?",
            "choices": {
                "A": "Warmer temperatures increase plant growth, which absorbs more CO2 and reduces warming",
                "B": "Warming melts arctic ice, which exposes dark ocean water that absorbs more sunlight, which causes more warming",
                "C": "Increased cloud cover reflects sunlight back to space",
                "D": "Ocean currents distribute heat evenly across the planet"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is the ice-albedo feedback. White ice reflects sunlight (high albedo), but when ice melts, it exposes dark ocean water that absorbs sunlight (low albedo). This absorption warms the water further, melting more ice, creating a self-amplifying cycle.",
            "feedback_incorrect": "A positive feedback amplifies the original change. Which process creates a cycle where warming leads to changes that cause even more warming, rather than counteracting it?"
        },
        {
            "question": "Scientists warn about 'tipping points' in the climate system. What does a climate tipping point represent?",
            "choices": {
                "A": "The point at which climate change begins to occur",
                "B": "A critical threshold beyond which a large, potentially irreversible change in the climate system is triggered, even if the original cause is removed",
                "C": "The exact temperature at which all ice on Earth melts simultaneously",
                "D": "A point that can only be identified after it has been passed, making it scientifically useless"
            },
            "correct": "B",
            "feedback_correct": "Correct. Tipping points represent thresholds where self-reinforcing feedbacks take over. For example, if permafrost warming triggers methane release that causes more warming that releases more methane, the process may become self-sustaining even if human emissions stop. The system transitions to a new state.",
            "feedback_incorrect": "Think about what makes a threshold 'irreversible.' If you push a ball over the edge of a hill, it continues rolling down even if you stop pushing. What climate processes behave similarly once a critical temperature is reached?"
        },
        {
            "question": "Forests absorb CO2 from the atmosphere through photosynthesis. A student claims that planting enough trees could solve climate change entirely. Which scientific limitation is MOST important for evaluating this claim?",
            "choices": {
                "A": "Trees do not actually absorb CO2",
                "B": "While forests sequester significant carbon, there is not enough land area to plant sufficient trees to offset current annual emissions of ~40 billion tons of CO2, and forests under heat stress can flip from carbon sinks to carbon sources",
                "C": "Trees produce more CO2 than they absorb",
                "D": "Planting trees would block too much sunlight from reaching the ground"
            },
            "correct": "B",
            "feedback_correct": "Correct. Global forests currently absorb ~2.6 billion tons of CO2/year, but annual emissions are ~40 billion tons. Even massive reforestation cannot offset total emissions. Additionally, forests under climate stress (drought, heat, wildfire) can die and release their stored carbon, converting from sinks to sources.",
            "feedback_incorrect": "Compare the scale of the solution to the scale of the problem. How much CO2 do forests absorb versus how much humans emit? And what happens to forest carbon storage under climate stress?"
        },
        {
            "question": "Climate change impacts are often described as 'disproportionate,' meaning some communities are affected much more severely than others. Which factor MOST directly determines a community's vulnerability to climate impacts?",
            "choices": {
                "A": "The community's latitude (distance from the equator)",
                "B": "The community's economic resources, infrastructure, and institutional capacity to adapt to changing conditions",
                "C": "The community's historical CO2 emissions",
                "D": "The community's total population size"
            },
            "correct": "B",
            "feedback_correct": "Correct. Adaptation capacity depends on wealth, infrastructure, governance, and institutional capacity. Wealthy nations can build sea walls, develop drought-resistant crops, and relocate populations. Vulnerable communities with fewer resources face the same or worse physical impacts with far less ability to respond.",
            "feedback_incorrect": "Consider two coastal cities facing identical sea level rise: one has billions of dollars for flood infrastructure and the other has minimal resources. Which will be more severely impacted, and why?"
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's coupled climate-ecosystem model shows that Forest Carbon Sequestration increases initially as Atmospheric CO2 rises (due to CO2 fertilization), but then sharply decreases after Global Temperature exceeds 2.5 degrees C above pre-industrial levels. Which phenomenon BEST explains this reversal?",
            "choices": {
                "A": "CO2 fertilization saturates at a fixed concentration level",
                "B": "Above 2.5 degrees C, widespread forest die-off from heat stress, drought, and wildfire converts forests from carbon sinks to carbon sources, flipping a negative feedback into a positive feedback that accelerates warming",
                "C": "Forest growth always decreases linearly with temperature",
                "D": "CO2 fertilization does not exist and the initial increase was a model error"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is a critical tipping point in the carbon cycle. Below 2.5 degrees C, forests partially counteract warming by absorbing CO2 (negative feedback). Above this threshold, forests die back and release stored carbon (positive feedback). This flip from sink to source accelerates the very warming that caused it, exemplifying nonlinear system behavior.",
            "feedback_incorrect": "Consider what happens to a forest when temperatures and drought exceed what trees can tolerate. What becomes of the carbon stored in dead trees? Does the forest continue to absorb CO2, or does it release it?"
        },
        {
            "question": "The model reveals that Permafrost Methane Release becomes self-sustaining above a specific Global Temperature threshold. A student identifies this as a tipping point. Which characteristic of the permafrost system MOST directly makes this self-sustaining?",
            "choices": {
                "A": "Methane is heavier than CO2 and sinks to ground level",
                "B": "Released methane is a powerful greenhouse gas (80x CO2 over 20 years) that causes additional warming, which thaws more permafrost, releasing more methane, creating a positive feedback loop that continues regardless of human emission reductions",
                "C": "Permafrost methane is released all at once in a single event",
                "D": "Methane in permafrost is replenished by underground geological processes"
            },
            "correct": "B",
            "feedback_correct": "Correct. The permafrost-methane feedback is a classic positive feedback tipping point. Once warming triggers sufficient methane release, the warming from that methane thaws additional permafrost, releasing more methane. Beyond the tipping point, this cycle generates enough warming to sustain itself regardless of whether human emissions continue.",
            "feedback_incorrect": "Think about the cycle: warming causes methane release, which causes more warming, which causes more methane release. At what point does this cycle generate enough warming on its own that it no longer needs human emissions as a driver?"
        },
        {
            "question": "A student compares the Paris Agreement scenario (1.5-2.0 degrees C warming) with the Business-As-Usual scenario (3-4 degrees C warming) in the model. Sea Level Rise projections differ by a factor of 4 between the scenarios even though temperature differs by only a factor of 2. Which property of the climate system explains this disproportionate response?",
            "choices": {
                "A": "Sea level rise is directly proportional to temperature change",
                "B": "Nonlinear ice sheet dynamics: above critical temperature thresholds, ice sheet collapse accelerates dramatically through feedback mechanisms (marine ice cliff instability, albedo loss) that do not operate below those thresholds",
                "C": "The ocean in the higher scenario contains four times more water",
                "D": "Measurement uncertainty accounts for the entire difference"
            },
            "correct": "B",
            "feedback_correct": "Correct. Ice sheet loss is not linear. Below certain thresholds, ice sheets lose mass gradually from surface melting. Above those thresholds, catastrophic processes activate: marine ice cliffs become unstable and collapse, exposed dark surfaces absorb more heat, and warm water undercuts ice shelves. These nonlinear processes produce disproportionately large sea level rise at higher temperatures.",
            "feedback_incorrect": "If the response were linear, a 2x temperature increase would produce a 2x sea level increase. The fact that the relationship is 4x suggests nonlinear processes are operating. What changes about ice sheet dynamics above certain temperature thresholds?"
        },
        {
            "question": "The model shows that Societal Adaptation Capacity is the most unevenly distributed component globally. A student uses this finding to argue that climate change is fundamentally a justice issue, not just an environmental one. Which evidence from the model MOST STRONGLY supports this argument?",
            "choices": {
                "A": "All countries experience identical climate impacts",
                "B": "Nations that have contributed the least to Atmospheric CO2 (e.g., sub-Saharan Africa, Pacific island nations) face the most severe physical impacts (extreme heat, sea level rise, crop failure) while having the fewest economic and institutional resources to adapt",
                "C": "Wealthy nations experience worse climate impacts than poor nations",
                "D": "Societal Adaptation Capacity is unrelated to climate outcomes"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates a fundamental asymmetry: the nations that industrialized and generated most historical emissions have the wealth and infrastructure to adapt, while nations that contributed minimally to the problem face disproportionate impacts with minimal resources. This mismatch between contribution and consequence is the core of climate justice.",
            "feedback_incorrect": "Climate justice asks: who caused the problem, who suffers the consequences, and who has the resources to adapt? Use the model to trace the relationship between historical emissions, current vulnerability, and adaptation capacity across different regions."
        },
        {
            "question": "A student proposes two climate intervention strategies and uses the model to evaluate them: Strategy A reduces Atmospheric CO2 emissions by 50% immediately; Strategy B invests in maximizing Societal Adaptation Capacity while maintaining current emission levels. The model shows that Strategy A produces better long-term outcomes. Which systems-level principle EXPLAINS why emission reduction outperforms adaptation alone?",
            "choices": {
                "A": "Adaptation is always inferior to mitigation",
                "B": "Adaptation addresses symptoms while emission reduction addresses the root cause; once positive feedback tipping points are crossed, adaptation capacity cannot compensate for self-reinforcing warming regardless of investment, making early emission reduction mathematically necessary to stay below irreversible thresholds",
                "C": "Emission reduction is cheaper than adaptation",
                "D": "The model is biased toward emission reduction strategies"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is the fundamental asymmetry between mitigation and adaptation. Adaptation has limits: no amount of adaptation can sustain agriculture, coastal cities, or ecosystems under 4+ degrees of warming with self-reinforcing feedbacks. Emission reduction operates upstream, preventing the tipping point crossings that would overwhelm any adaptation strategy. Both are necessary, but emission reduction is the only intervention that prevents irreversible system state changes.",
            "feedback_incorrect": "Think about where each strategy operates in the causal chain. Emission reduction prevents warming from crossing tipping points. Adaptation manages the consequences of warming that has already occurred. What happens when adaptation faces consequences that exceed its capacity because tipping points were crossed?"
        }
    ]
}

# Aggregate all questions
ALL_QUESTIONS = {
    "G09L3-L01": L01_QUESTIONS,
    "G09L3-L02": L02_QUESTIONS,
    "G09L3-L03": L03_QUESTIONS,
    "G09L3-L04": L04_QUESTIONS,
    "G09L3-L05": L05_QUESTIONS,
    "G09L3-L06": L06_QUESTIONS,
    "G09L3-L07": L07_QUESTIONS,
    "G09L3-L08": L08_QUESTIONS,
    "G09L3-L09": L09_QUESTIONS,
    "G09L3-L10": L10_QUESTIONS,
}
