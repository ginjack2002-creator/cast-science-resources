#!/usr/bin/env python3
"""Multiple choice pre/post assessment questions for Grade 12 Level 2 ModelIt! Lessons
Grade 12 Level 2: Global Systems & Sustainability
NGSS-aligned, CAST-exam-style rigor — analysis, evaluation, and application level questions.
"""

L01_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A scientist models the global carbon cycle and finds that the ocean currently absorbs about 25% of human CO2 emissions. Which factor would most likely reduce the ocean's capacity as a carbon sink over time?",
            "choices": {
                "A": "Increasing ocean surface temperature and rising acidity",
                "B": "Increasing wind speed across ocean surfaces",
                "C": "Decreasing the salinity of surface waters",
                "D": "Increasing the depth of the thermocline layer"
            },
            "correct": "A",
            "feedback_correct": "Correct. Warmer water dissolves less CO2, and increased acidity from absorbed CO2 shifts the carbonate equilibrium, both reducing the ocean's absorption capacity and creating a positive feedback loop.",
            "feedback_incorrect": "Incorrect. Consider how temperature and chemical changes in seawater affect CO2 solubility. Warmer, more acidic water holds less dissolved CO2, reducing the ocean's function as a carbon sink."
        },
        {
            "question": "Which statement best describes why positive feedback loops make climate change difficult to reverse?",
            "choices": {
                "A": "They slow down the rate of warming, giving ecosystems time to adapt",
                "B": "They amplify an initial change, causing the system to accelerate away from its original state",
                "C": "They maintain the climate in a stable equilibrium regardless of CO2 levels",
                "D": "They only operate when temperatures exceed 3 degrees Celsius above pre-industrial levels"
            },
            "correct": "B",
            "feedback_correct": "Correct. Positive feedback loops amplify change. For example, warming melts ice, reducing albedo, which causes more warming. This self-reinforcing cycle makes it progressively harder to return to the original state.",
            "feedback_incorrect": "Incorrect. Positive feedback loops do not stabilize or slow a system. They amplify the original perturbation, creating a self-reinforcing cycle that accelerates change in one direction."
        },
        {
            "question": "Pre-industrial atmospheric CO2 was approximately 280 ppm. Current levels are approximately 424 ppm. A student claims that reducing emissions to zero would immediately return CO2 to 280 ppm. What is the primary flaw in this reasoning?",
            "choices": {
                "A": "CO2 has a very short atmospheric residence time and would dissipate within weeks",
                "B": "Natural carbon sinks can only remove excess CO2 gradually over centuries, and activated feedback loops continue releasing CO2 independently",
                "C": "Volcanic eruptions would replace the CO2 removed by natural sinks within a few years",
                "D": "Plant photosynthesis rates would immediately double to compensate for reduced emissions"
            },
            "correct": "B",
            "feedback_correct": "Correct. Even at zero emissions, natural sinks like oceans and forests remove excess CO2 slowly over centuries, not instantly. Meanwhile, activated feedback loops such as permafrost thaw continue adding CO2 to the atmosphere independently of human activity.",
            "feedback_incorrect": "Incorrect. The key concept is thermal inertia and feedback loops. CO2 has an atmospheric residence time of centuries, natural sinks operate slowly, and feedback mechanisms like permafrost methane release continue independently of human emissions."
        },
        {
            "question": "A climate model shows that after all emissions stop, global temperature continues rising for 20-40 years before stabilizing. Which concept best explains this delay?",
            "choices": {
                "A": "Albedo effect from increased cloud cover",
                "B": "Thermal inertia of the ocean, which has absorbed and slowly releases stored heat",
                "C": "Rapid growth of vegetation absorbing excess solar radiation",
                "D": "Increased volcanic activity triggered by atmospheric pressure changes"
            },
            "correct": "B",
            "feedback_correct": "Correct. The ocean absorbs enormous amounts of heat, which it continues to release over decades. This thermal inertia means the climate system responds with a significant lag, so temperature continues rising even after the forcing (emissions) stops.",
            "feedback_incorrect": "Incorrect. The delay is primarily due to the ocean's thermal inertia. The ocean acts as a massive heat reservoir, and the energy already stored continues warming the atmosphere for decades after emissions cease."
        },
        {
            "question": "Which strategy would be most effective at preventing climate tipping points from being crossed, based on carbon cycle dynamics?",
            "choices": {
                "A": "Relying solely on tree planting to offset continued fossil fuel emissions at current rates",
                "B": "Combining aggressive emission reductions with enhanced carbon sinks to limit total cumulative CO2",
                "C": "Waiting for natural carbon sinks to absorb all excess CO2 before taking policy action",
                "D": "Focusing exclusively on reducing methane emissions while maintaining current CO2 output"
            },
            "correct": "B",
            "feedback_correct": "Correct. Tipping points depend on cumulative CO2 and total warming. Only a combined approach that reduces emissions at the source AND enhances carbon sinks can limit cumulative CO2 enough to prevent crossing critical thresholds.",
            "feedback_incorrect": "Incorrect. No single approach is sufficient. Tree planting alone cannot offset current emission rates, waiting allows further accumulation, and methane alone does not address the primary driver. A combined strategy targeting both emission reduction and sink enhancement is necessary."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student runs a climate model simulation where fossil fuel emissions drop to zero immediately. The model shows temperature continuing to rise for 30 years. Which combination of factors best explains this result?",
            "choices": {
                "A": "Ocean thermal inertia releasing stored heat and self-sustaining positive feedback loops continuing to operate",
                "B": "Increased solar output and reduced cloud cover after emission sources shut down",
                "C": "Rising population growth increasing energy demand despite zero emissions",
                "D": "Natural variation in Earth's orbital parameters causing a warming cycle"
            },
            "correct": "A",
            "feedback_correct": "Correct. The ocean has absorbed vast amounts of heat that continues warming the atmosphere (thermal inertia), and positive feedback loops like ice-albedo reduction and permafrost methane release have been triggered and operate independently of human emissions.",
            "feedback_incorrect": "Incorrect. The continued warming results from two system-level properties: the ocean's thermal inertia (stored heat being released gradually) and self-sustaining positive feedback loops (ice-albedo, permafrost thaw) that were activated by prior warming and no longer depend on human emissions."
        },
        {
            "question": "In a carbon cycle model, a student observes that increasing terrestrial carbon storage by 30% while reducing emissions by 50% still results in rising temperatures for 15 years. What does this demonstrate about the climate system?",
            "choices": {
                "A": "Carbon sinks have no measurable effect on atmospheric CO2 levels",
                "B": "The climate system has built-in lag times and activated feedbacks that persist even under improved conditions",
                "C": "Terrestrial carbon storage is less important than ocean absorption in all scenarios",
                "D": "A 50% emission reduction is identical in effect to no reduction at all"
            },
            "correct": "B",
            "feedback_correct": "Correct. The continued temperature rise despite improved conditions demonstrates that the climate system has significant lag times (thermal inertia) and that previously activated feedback loops continue operating. The combined strategy does eventually stabilize temperatures, but the system does not respond instantly.",
            "feedback_incorrect": "Incorrect. The enhanced sinks and reduced emissions do help, as temperatures eventually stabilize rather than continuing to rise indefinitely. The temporary continued warming demonstrates system lag and feedback persistence, not that the interventions are ineffective."
        },
        {
            "question": "Which evidence from a carbon cycle model most strongly supports the conclusion that some aspects of climate change are irreversible on human timescales?",
            "choices": {
                "A": "Atmospheric CO2 fluctuates seasonally with plant growth cycles",
                "B": "Once permafrost thaw and ice-albedo feedback loops are triggered, they continue driving warming independently of human emissions",
                "C": "Ocean temperatures vary with El Nino and La Nina patterns",
                "D": "Different tree species absorb CO2 at different rates depending on latitude"
            },
            "correct": "B",
            "feedback_correct": "Correct. Self-sustaining feedback loops represent potential tipping points. Once permafrost begins releasing stored methane and ice loss reduces albedo, these processes continue regardless of emission reductions, making the resulting warming effectively irreversible on human timescales.",
            "feedback_incorrect": "Incorrect. The key to irreversibility is self-sustaining positive feedback loops. Seasonal fluctuations and ocean oscillations are natural cycles, not indicators of irreversibility. The activation of feedbacks that operate independently of human action is what creates irreversible change."
        },
        {
            "question": "A policy team uses a climate model to compare three scenarios: business as usual, immediate net zero, and gradual reduction with enhanced sinks. Which finding would provide the strongest evidence for recommending the combined approach over net zero alone?",
            "choices": {
                "A": "The combined approach achieves temperature stabilization 5 years faster than net zero alone because enhanced sinks actively remove atmospheric CO2 rather than just stopping additions",
                "B": "The combined approach costs less to implement in the first year",
                "C": "The combined approach requires fewer technological innovations",
                "D": "The combined approach results in higher atmospheric CO2 levels but lower temperatures"
            },
            "correct": "A",
            "feedback_correct": "Correct. Enhanced carbon sinks actively draw down atmospheric CO2, addressing the stock of greenhouse gases already accumulated, while net zero only stops new additions. The faster stabilization timeline provides the strongest science-based justification for the combined approach.",
            "feedback_incorrect": "Incorrect. The strongest evidence is scientific, not economic or logistical. Enhanced sinks combined with emission reduction actively removes CO2 from the atmosphere, addressing the existing stock rather than just stopping new flow, which accelerates temperature stabilization."
        },
        {
            "question": "A student argues that since the ocean absorbs 25% of human CO2 emissions, increasing emissions would actually increase ocean carbon absorption and help solve climate change. Evaluate this claim using carbon cycle dynamics.",
            "choices": {
                "A": "The claim is correct because ocean absorption scales linearly with atmospheric CO2 without limit",
                "B": "The claim ignores that increased absorption causes ocean acidification and that warming reduces absorption capacity, creating a negative feedback that limits uptake",
                "C": "The claim is correct because deeper ocean waters have unlimited CO2 storage capacity",
                "D": "The claim is invalid only because ocean organisms would die from excess CO2, not because of any physical limitation"
            },
            "correct": "B",
            "feedback_correct": "Correct. While the ocean does absorb more CO2 as atmospheric levels rise, this absorption causes acidification that harms marine life, and warming reduces the ocean's ability to dissolve CO2. These factors create a diminishing-returns dynamic where the ocean's sink capacity decreases as it is needed most.",
            "feedback_incorrect": "Incorrect. The claim fails because it ignores crucial system dynamics: CO2 absorption causes harmful acidification, and as the ocean warms, it becomes less capable of absorbing CO2. The relationship is not linear and unlimited but is constrained by chemistry and temperature."
        }
    ]
}

L02_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Coral reefs cover less than 1% of the ocean floor but support approximately 25% of all marine species. Which ecological concept best explains this disproportionate importance?",
            "choices": {
                "A": "Competitive exclusion, where one species dominates all others",
                "B": "Structural complexity that creates diverse microhabitats, supporting high species richness",
                "C": "Uniform environmental conditions that favor a single dominant species",
                "D": "Low predation pressure that allows unlimited population growth"
            },
            "correct": "B",
            "feedback_correct": "Correct. Coral reefs create three-dimensional structural complexity with crevices, overhangs, and surfaces that provide diverse microhabitats for feeding, shelter, spawning, and nursery areas, supporting extraordinarily high biodiversity relative to their area.",
            "feedback_incorrect": "Incorrect. The key is structural complexity. Coral reefs are not uniform environments. Their intricate physical structure creates thousands of distinct microhabitats that support different species with different ecological needs."
        },
        {
            "question": "Ocean pH has dropped from 8.2 to 8.1 since pre-industrial times, a change that represents a 26% increase in acidity. Why is this small numerical change significant for coral reef organisms?",
            "choices": {
                "A": "The pH scale is logarithmic, so a 0.1 unit change represents a much larger proportional change in hydrogen ion concentration",
                "B": "Marine organisms can only survive within a pH range of exactly 8.2 to 8.3",
                "C": "The change only affects organisms larger than 1 centimeter in length",
                "D": "pH changes in the ocean are immediately reversed by wave action mixing"
            },
            "correct": "A",
            "feedback_correct": "Correct. Because pH is a logarithmic scale, a decrease of 0.1 units represents a 26% increase in hydrogen ion concentration. This substantial chemical change reduces carbonate ion availability, which corals and shellfish need to build calcium carbonate skeletons.",
            "feedback_incorrect": "Incorrect. The pH scale is logarithmic, meaning each unit change represents a tenfold change in hydrogen ion concentration. A 0.1 decrease equals approximately 26% more acidity, which significantly reduces the carbonate ions available for coral skeleton building."
        },
        {
            "question": "Zooxanthellae algae provide up to 90% of a coral's energy through photosynthesis. If ocean temperatures rise 1-2 degrees Celsius above the normal summer maximum, what would you predict happens to this symbiotic relationship?",
            "choices": {
                "A": "Zooxanthellae increase photosynthesis rates, providing more energy to the coral",
                "B": "Corals expel the zooxanthellae under thermal stress, losing their primary energy source and their color",
                "C": "Zooxanthellae migrate deeper into coral tissue where temperatures are cooler",
                "D": "The coral secretes protective mucus that insulates the zooxanthellae from temperature change"
            },
            "correct": "B",
            "feedback_correct": "Correct. Thermal stress causes corals to expel their zooxanthellae in a process called coral bleaching. The loss of these algae reveals the white skeleton and deprives the coral of up to 90% of its energy, leading to starvation and death if the stress persists.",
            "feedback_incorrect": "Incorrect. Under thermal stress, corals do not protect their zooxanthellae. Instead, they expel them in a stress response called bleaching. Without these symbiotic algae, corals lose both their color and their primary energy source."
        },
        {
            "question": "A marine biologist observes that a coral reef has shifted from being coral-dominated to algae-dominated after a series of bleaching events. Which term best describes this ecological change?",
            "choices": {
                "A": "Primary succession beginning on newly formed substrate",
                "B": "A phase shift representing a regime change that is difficult to reverse due to positive feedback loops",
                "C": "Normal seasonal variation in reef community composition",
                "D": "Competitive exclusion that will naturally reverse once coral populations recover"
            },
            "correct": "B",
            "feedback_correct": "Correct. A phase shift from coral to algae dominance represents a regime change. Positive feedback loops maintain the new state: algae smother coral larvae, dead coral provides algae substrate, and reduced reef structure drives away herbivorous fish that would control algae.",
            "feedback_incorrect": "Incorrect. This transition is a phase shift, not a temporary fluctuation. Once algae dominate, positive feedback loops (algae blocking coral recruitment, loss of herbivore fish habitat, dead coral becoming algae substrate) lock in the degraded state."
        },
        {
            "question": "Herbivorous fish like parrotfish play a critical role on coral reefs by consuming algae. If overfishing reduces parrotfish populations by 80%, which outcome is most likely during a moderate bleaching event?",
            "choices": {
                "A": "The reef recovers faster because there is less competition for coral larvae settlement",
                "B": "The reef is more likely to undergo a phase shift to algae dominance because unchecked algae growth prevents coral recovery",
                "C": "Algae populations decline because they lose a dispersal mechanism provided by fish",
                "D": "Coral bleaching severity is reduced because fewer fish means less physical damage to coral"
            },
            "correct": "B",
            "feedback_correct": "Correct. Without herbivorous fish to control algae growth, macroalgae rapidly colonize space left by bleached coral, preventing recovery. The reef loses its primary biological defense against phase shifts, making even moderate bleaching events potentially catastrophic.",
            "feedback_incorrect": "Incorrect. Herbivorous fish are critical for reef resilience. They control algae growth that would otherwise smother recovering corals. Without this top-down control, even moderate bleaching events can trigger irreversible phase shifts to algae dominance."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's reef model shows that a single bleaching event requires 10-15 years of stable conditions for full coral recovery, but bleaching events are now occurring every 2-3 years. What conclusion is best supported by this data?",
            "choices": {
                "A": "Corals are adapting to tolerate more frequent bleaching, so the frequency is not a concern",
                "B": "The recovery deficit created by increasing bleaching frequency will cause cumulative coral decline even without any increase in bleaching severity",
                "C": "The model must be inaccurate because natural systems always achieve equilibrium",
                "D": "Recovery time is determined solely by water temperature and is unrelated to bleaching frequency"
            },
            "correct": "B",
            "feedback_correct": "Correct. When disturbance frequency exceeds recovery time, the system experiences cumulative decline. Each bleaching event further weakens coral before it has recovered from the previous one, creating a ratchet effect that drives progressive reef degradation.",
            "feedback_incorrect": "Incorrect. The critical insight is the mismatch between recovery time (10-15 years) and disturbance frequency (2-3 years). When events recur faster than recovery can occur, each event starts from a more degraded baseline, creating cumulative decline."
        },
        {
            "question": "A student compares two model scenarios: one with warming only and one with warming plus acidification. Both show coral decline, but the combined scenario shows decline at a significantly lower temperature threshold. What does this demonstrate?",
            "choices": {
                "A": "Acidification and warming are independent stressors with no interaction",
                "B": "Multiple simultaneous stressors produce compounding effects that lower the threshold for ecosystem collapse",
                "C": "Acidification is always more damaging than warming in isolation",
                "D": "The model is flawed because real ecosystems experience only one stressor at a time"
            },
            "correct": "B",
            "feedback_correct": "Correct. The lower threshold under combined stress demonstrates a synergistic effect. Acidification weakens coral skeletons while warming disrupts the symbiosis, and the combined stress exceeds the sum of individual effects, pushing the system past tipping points at lower levels of each individual stressor.",
            "feedback_incorrect": "Incorrect. The combined scenario's lower threshold demonstrates synergistic interaction between stressors. In real ecosystems, multiple stressors operate simultaneously, and their combined effect is often greater than the sum of individual effects."
        },
        {
            "question": "In a reef model, maintaining high herbivore fish populations significantly increases reef resilience to bleaching. Which systems thinking concept does this illustrate?",
            "choices": {
                "A": "Removing a component has no effect if other components compensate",
                "B": "Local management of one system component can buffer the system against external stressors by maintaining critical ecological functions",
                "C": "Only global interventions can affect reef outcomes because climate is a global system",
                "D": "Herbivore populations are independent of reef health and can be managed separately"
            },
            "correct": "B",
            "feedback_correct": "Correct. Protecting herbivore fish populations is a local management action that maintains the ecological function of algae control, giving reefs more time to recover between bleaching events. This demonstrates how managing controllable local variables can buffer a system against uncontrollable global stressors.",
            "feedback_incorrect": "Incorrect. The model demonstrates that local management actions can meaningfully increase system resilience. By protecting herbivore fish, managers maintain algae control, which gives coral more recovery time between bleaching events, even though they cannot control global temperature."
        },
        {
            "question": "A reef ecologist presents model evidence showing that once coral cover drops below 10%, positive feedback loops make recovery nearly impossible without major intervention. Which set of feedback loops most accurately describes why?",
            "choices": {
                "A": "More dead coral provides substrate for algae, algae smother coral larvae, reduced reef structure drives away herbivorous fish, and fewer herbivores allow more algae growth",
                "B": "Increased water clarity from fewer organisms causes UV damage to remaining coral",
                "C": "Reduced reef size increases wave exposure, which improves water circulation and coral health",
                "D": "Lower coral cover attracts more predatory fish that consume the remaining coral polyps"
            },
            "correct": "A",
            "feedback_correct": "Correct. This describes a set of interconnected positive feedback loops that reinforce algae dominance: dead coral becomes algae substrate, algae block coral recruitment, degraded structure loses herbivore habitat, and reduced herbivory allows more algae growth. Each loop reinforces the others.",
            "feedback_incorrect": "Incorrect. The feedback loops maintaining a degraded reef state involve algae colonizing dead coral, algae preventing new coral settlement, loss of structural habitat driving away herbivorous fish, and reduced herbivory allowing more algae growth. These interconnected loops lock in the degraded state."
        },
        {
            "question": "Based on coral reef model evidence, which conservation strategy would be most effective for maximizing reef survival over the next 50 years?",
            "choices": {
                "A": "Focusing exclusively on local pollution reduction while ignoring global CO2 emissions",
                "B": "A multi-scale approach combining local herbivore protection and pollution reduction with global emission reductions to slow warming and acidification",
                "C": "Relocating all coral to deeper, cooler waters where they are protected from surface warming",
                "D": "Allowing natural selection to produce heat-resistant coral strains without any human intervention"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that local management (herbivore protection, pollution reduction) buys time by increasing resilience, but long-term reef survival ultimately requires addressing global stressors (warming and acidification) through emission reductions. Neither local nor global action alone is sufficient.",
            "feedback_incorrect": "Incorrect. Model evidence shows that effective conservation requires action at multiple scales. Local protection increases resilience and buys time, but without addressing global warming and acidification through emission reductions, even well-managed reefs will eventually succumb to overwhelming thermal and chemical stress."
        }
    ]
}

L03_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Global food systems currently waste approximately one-third of all food produced. If this waste were eliminated, what would be the equivalent effect on agricultural land?",
            "choices": {
                "A": "It would be equivalent to increasing agricultural land by approximately 25% without any environmental cost",
                "B": "It would have no measurable impact because waste occurs after food leaves the farm",
                "C": "It would require doubling chemical fertilizer use to compensate for reduced composting",
                "D": "It would increase water consumption because more food would need to be transported"
            },
            "correct": "A",
            "feedback_correct": "Correct. Eliminating one-third of food waste is effectively equivalent to producing 33% more food from existing land, which translates to roughly a 25% increase in effective agricultural area without requiring deforestation, water use, or chemical inputs.",
            "feedback_incorrect": "Incorrect. Food waste represents enormous embedded resources. Reducing waste by one-third effectively increases the food available from existing agricultural land by about 25%, making it the single highest-leverage intervention in the food system."
        },
        {
            "question": "A farmer increases crop yields by applying maximum chemical fertilizers to a monoculture field for 20 years. Based on agricultural systems dynamics, what is the most likely long-term outcome?",
            "choices": {
                "A": "Yields continue increasing indefinitely as soil adapts to higher nutrient levels",
                "B": "Soil degradation through nutrient depletion, loss of soil biology, and compaction leads to declining yields despite increasing inputs",
                "C": "The soil becomes permanently improved and requires less fertilizer over time",
                "D": "Monoculture farming has no negative effects on soil as long as fertilizer is applied"
            },
            "correct": "B",
            "feedback_correct": "Correct. Intensive monoculture with chemical fertilizers degrades soil biology, structure, and organic matter over time. While short-term yields increase, long-term productivity declines as the soil loses its natural fertility, creating dependence on ever-increasing chemical inputs with diminishing returns.",
            "feedback_incorrect": "Incorrect. The key concept is that intensive farming mines soil health. Chemical fertilizers provide macronutrients but damage soil biology, structure, and organic matter. Over 20 years, this degradation reduces the soil's capacity to support crops, causing yields to plateau and eventually decline."
        },
        {
            "question": "Agriculture uses approximately 70% of global freshwater withdrawals. Which change in farming practice would have the greatest impact on reducing agricultural water demand?",
            "choices": {
                "A": "Replacing flood irrigation with drip irrigation systems",
                "B": "Planting crops only during the rainy season",
                "C": "Increasing pesticide application to reduce crop losses",
                "D": "Converting all farms to hydroponic greenhouses"
            },
            "correct": "A",
            "feedback_correct": "Correct. Flood irrigation wastes 40-60% of water through evaporation and runoff. Drip irrigation delivers water directly to plant roots with 90-95% efficiency. Because agriculture is the dominant water user, this single change has the largest potential impact on total freshwater demand.",
            "feedback_incorrect": "Incorrect. Since agriculture consumes 70% of freshwater, the most impactful change targets irrigation efficiency. Drip irrigation reduces water use by 40-60% compared to flood irrigation by delivering water directly to roots, making it the highest-impact intervention."
        },
        {
            "question": "The concept of carrying capacity in agricultural systems differs from simple population limits. Which factor makes carrying capacity a dynamic rather than fixed number?",
            "choices": {
                "A": "It depends only on total land area and cannot change",
                "B": "It changes based on the sustainability of farming practices, distribution efficiency, and resource management",
                "C": "It is determined exclusively by genetic modifications to crop species",
                "D": "It remains constant regardless of how resources are managed"
            },
            "correct": "B",
            "feedback_correct": "Correct. Agricultural carrying capacity is dynamic because it depends on how resources are managed. Sustainable practices maintain or increase it over time, while exploitative practices deplete soil and water, reducing it. Distribution efficiency also matters because food waste effectively lowers carrying capacity.",
            "feedback_incorrect": "Incorrect. Carrying capacity is not fixed. It depends on agricultural practices (sustainable vs. exploitative), resource management (water, soil), distribution efficiency (waste levels), and dietary choices. These human decisions make carrying capacity a moving target."
        },
        {
            "question": "Biodiversity in agricultural landscapes provides ecosystem services such as pollination, pest control, and soil health. What happens to these services under intensive monoculture farming?",
            "choices": {
                "A": "They increase because monoculture simplifies ecological interactions",
                "B": "They decline as habitat loss and chemical use reduce populations of pollinators, predators, and soil organisms",
                "C": "They remain unchanged because ecosystem services are provided by wild areas far from farms",
                "D": "They are replaced entirely by chemical substitutes with no loss of function"
            },
            "correct": "B",
            "feedback_correct": "Correct. Intensive monoculture eliminates the habitat diversity that supports beneficial organisms. Pollinators lose nesting sites, natural pest predators lose prey diversity, and soil organisms are killed by tillage and chemicals, undermining the ecosystem services that agriculture depends on.",
            "feedback_incorrect": "Incorrect. Ecosystem services require living organisms that depend on habitat within and around farms. Monoculture eliminates this habitat, while pesticides and tillage directly harm beneficial organisms. Chemical substitutes cannot fully replicate these complex biological services."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A food system model shows that industrial intensification increases yields by 30% in 5 years but decreases soil health index by 40% over 30 years. A student concludes that intensification is the best strategy because it produces more food. What critical flaw exists in this reasoning?",
            "choices": {
                "A": "The student is considering only the short-term output without accounting for the long-term decline in the system's productive capacity",
                "B": "The student should focus on water use rather than soil health",
                "C": "The 5-year data is unreliable compared to the 30-year data",
                "D": "Soil health is unrelated to crop yield in modern agriculture"
            },
            "correct": "A",
            "feedback_correct": "Correct. The student commits a temporal scale error by evaluating a long-term system using short-term data. The 30-year trajectory shows that the initial yield gains are unsustainable because they come at the cost of the soil health that ultimately determines productive capacity.",
            "feedback_incorrect": "Incorrect. The critical flaw is the mismatch in timescales. Short-term yield increases can mask long-term productive capacity loss. The soil health decline means that after 30 years, the system produces less food than it would have under sustainable management."
        },
        {
            "question": "A model shows that water availability becomes the binding constraint on food production before land runs out. Which evidence from the model would most strongly support this conclusion?",
            "choices": {
                "A": "Aquifer levels decline to economically non-pumpable depths while significant agricultural land remains available but unirrigable",
                "B": "More land is converted to agriculture each year",
                "C": "Crop prices increase due to transportation costs",
                "D": "Population growth slows in water-scarce regions"
            },
            "correct": "A",
            "feedback_correct": "Correct. If aquifers are depleted to the point where pumping is no longer economical while cultivable land still exists but cannot be farmed without irrigation, this directly demonstrates that water, not land, is the binding constraint on production capacity.",
            "feedback_incorrect": "Incorrect. The strongest evidence for water as the binding constraint would show that available land exists but cannot produce food due to water scarcity. Aquifer depletion rendering existing farmland unirrigable while potential cropland goes unused directly proves water is the limiting factor."
        },
        {
            "question": "The model demonstrates that sustainable intensification can theoretically feed 10 billion people on current agricultural land. Why does the word 'theoretically' represent an important qualification?",
            "choices": {
                "A": "Because the model uses inaccurate data about crop yields",
                "B": "Because achieving this outcome requires fundamental transformation of farming practices, food distribution systems, and political-economic structures that face significant implementation barriers",
                "C": "Because 10 billion people is an unrealistically high population projection",
                "D": "Because sustainable farming always produces less food than industrial farming"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows biophysical feasibility, but real-world implementation requires transforming subsidies, supply chains, dietary patterns, trade policies, and land ownership structures. The gap between what is technically possible and what is politically achievable is the central challenge.",
            "feedback_incorrect": "Incorrect. The 'theoretical' qualification acknowledges the gap between biophysical capacity and real-world implementation. Feeding 10 billion sustainably is scientifically possible but requires political, economic, and social transformations that are far more challenging than the technical aspects."
        },
        {
            "question": "A student's model shows that combining waste reduction, soil regeneration, and biodiversity protection produces better long-term food security than any single intervention alone. Which systems concept does this demonstrate?",
            "choices": {
                "A": "Negative feedback loops always dominate positive feedback loops",
                "B": "Interventions at multiple leverage points simultaneously produce synergistic effects greater than the sum of individual actions",
                "C": "Complex systems are too unpredictable to model accurately",
                "D": "Single interventions are always more cost-effective than combined approaches"
            },
            "correct": "B",
            "feedback_correct": "Correct. This demonstrates synergy in complex systems. Waste reduction frees resources, healthy soil sustains yields, and biodiversity provides ecosystem services. These interventions reinforce each other, producing combined benefits that exceed what any single intervention could achieve alone.",
            "feedback_incorrect": "Incorrect. The model demonstrates synergistic effects. Multiple interventions targeting different leverage points in a complex system produce benefits that reinforce each other, yielding outcomes greater than the sum of individual actions. This is a fundamental property of complex adaptive systems."
        },
        {
            "question": "Based on the food system model, a policy advisor must choose where to invest limited resources. Which model finding provides the strongest evidence for prioritizing food waste reduction over agricultural land expansion?",
            "choices": {
                "A": "Land expansion produces immediate results while waste reduction takes decades to implement",
                "B": "Waste reduction provides equivalent food availability gains without the environmental costs of deforestation, habitat loss, and soil degradation that come with land expansion",
                "C": "Food waste only occurs in developed countries and is irrelevant globally",
                "D": "Agricultural land expansion has no environmental consequences in most regions"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that reducing waste by 50% is equivalent to expanding farmland by 25%, but without deforestation, biodiversity loss, increased water demand, or soil degradation. The same food availability outcome with dramatically lower environmental cost makes waste reduction the superior investment.",
            "feedback_incorrect": "Incorrect. The model evidence shows waste reduction achieves comparable food availability gains to land expansion but without the associated environmental damage. This cost-benefit analysis, grounded in model data, provides the strongest evidence for prioritizing waste reduction."
        }
    ]
}

L04_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Since 1950, humans have produced 8.3 billion metric tons of plastic. Of all plastic waste ever generated, approximately what percentage has been recycled?",
            "choices": {
                "A": "About 45%, with most recycled into new products",
                "B": "About 30%, with recycling rates increasing each decade",
                "C": "About 9%, with 79% accumulating in landfills or the environment",
                "D": "About 60%, with advanced recycling technologies processing most waste"
            },
            "correct": "C",
            "feedback_correct": "Correct. Only 9% of all plastic ever produced has been recycled, 12% has been incinerated, and 79% has accumulated in landfills or the natural environment. This extremely low recycling rate is a central factor in the plastic pollution crisis.",
            "feedback_incorrect": "Incorrect. The recycling rate for plastic is far lower than most people assume. Only 9% of all plastic ever produced has been recycled. The remaining 91% has been incinerated (12%) or accumulated in landfills and the environment (79%)."
        },
        {
            "question": "Microplastics have been detected in human blood, lungs, placenta, and breast milk. Which process best explains how plastic particles from the ocean reach human tissue?",
            "choices": {
                "A": "Plastic fragments evaporate from ocean surfaces and are inhaled directly",
                "B": "Bioaccumulation through the food web, where microplastics consumed by small organisms concentrate at each trophic level until reaching humans",
                "C": "Microplastics are absorbed through skin contact with ocean water during swimming",
                "D": "Plastic particles are only found in people who work in plastic manufacturing"
            },
            "correct": "B",
            "feedback_correct": "Correct. Microplastics enter food webs when filter feeders and small organisms ingest them. At each trophic level, concentrations increase through biomagnification. Humans at the top of food chains accumulate microplastics from seafood and other contaminated food sources.",
            "feedback_incorrect": "Incorrect. The primary pathway is bioaccumulation through food webs. Small organisms ingest microplastics, which concentrate at each trophic level through biomagnification. Humans consume contaminated seafood and other products, accumulating plastic particles in their tissues."
        },
        {
            "question": "Plastic production is currently growing at approximately 4% per year. If recycling rates triple from 9% to 27%, what would a systems analysis predict about total environmental plastic accumulation?",
            "choices": {
                "A": "Environmental plastic would decrease rapidly because recycling is tripling",
                "B": "Environmental plastic would continue increasing because production growth outpaces the improved recycling rate",
                "C": "Environmental plastic would remain exactly constant because the two rates would balance",
                "D": "Environmental plastic would disappear within 10 years due to natural degradation"
            },
            "correct": "B",
            "feedback_correct": "Correct. At 4% annual production growth, total plastic output doubles roughly every 18 years. Tripling recycling from 9% to 27% still leaves 73% of a rapidly growing total entering landfills or the environment. The exponential growth of production overwhelms the linear improvement in recycling.",
            "feedback_incorrect": "Incorrect. This is a rate comparison problem. Tripling recycling sounds impressive but only moves from 9% to 27% of waste recycled. Meanwhile, 4% annual production growth is exponential. The growing total output means more plastic enters the environment each year despite improved recycling."
        },
        {
            "question": "Plastics absorb and concentrate persistent organic pollutants (POPs) like PCBs from surrounding water. Why does this property make microplastics especially dangerous in food webs?",
            "choices": {
                "A": "The POPs make plastics biodegradable, releasing toxins all at once",
                "B": "Microplastics act as delivery vehicles for concentrated toxins that are released in animal tissue upon ingestion, amplifying chemical exposure at each trophic level",
                "C": "POPs attached to plastics are neutralized by stomach acid and pose no health risk",
                "D": "Only plastics larger than 5mm can absorb POPs from the environment"
            },
            "correct": "B",
            "feedback_correct": "Correct. Microplastics concentrate POPs from water on their surface, acting like toxic sponges. When organisms ingest these particles, the toxins transfer to their tissue. Through biomagnification, toxin concentrations increase at each trophic level, making top predators and humans most exposed.",
            "feedback_incorrect": "Incorrect. Microplastics absorb and concentrate toxic chemicals from surrounding water. When ingested by organisms, these concentrated toxins transfer to tissue. Biomagnification amplifies concentrations up the food chain, making microplastics essentially toxic delivery vehicles."
        },
        {
            "question": "A circular economy model for plastics would fundamentally differ from the current linear model. Which characteristic best defines a circular economy approach?",
            "choices": {
                "A": "Producing plastic more cheaply so more people can afford to buy and discard products",
                "B": "Designing products for reuse, repair, and recycling so that no plastic ever becomes pollution",
                "C": "Increasing landfill capacity to store more plastic waste",
                "D": "Replacing all plastic with paper products regardless of functionality"
            },
            "correct": "B",
            "feedback_correct": "Correct. A circular economy eliminates waste by design. Products are created for durability, reuse, repair, and eventual recycling into new products. This contrasts with the current take-make-waste model where plastic is designed for single use and disposal.",
            "feedback_incorrect": "Incorrect. A circular economy fundamentally redesigns the production-consumption cycle. Instead of a linear path from production to disposal, materials continuously cycle through use, reuse, repair, and recycling, so nothing becomes waste or pollution."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's model shows that even after all new plastic input to the ocean stops, microplastic concentration continues increasing for decades. What mechanism best explains this finding?",
            "choices": {
                "A": "New plastic is secretly being dumped into the ocean by unmonitored sources",
                "B": "Existing macroplastics already in the ocean continue fragmenting into microplastics through UV radiation, wave action, and biological processes",
                "C": "Microplastics are spontaneously generated from dissolved organic matter in seawater",
                "D": "Ocean currents concentrate microplastics in measurement areas, creating an illusion of increase"
            },
            "correct": "B",
            "feedback_correct": "Correct. The estimated 150 million metric tons of plastic already in the ocean continuously fragment into smaller pieces through UV degradation, mechanical wave action, and biological processes. This existing stock creates a legacy effect where microplastic concentrations rise even without new input.",
            "feedback_incorrect": "Incorrect. The legacy effect explains this pattern. The massive existing stock of macroplastics in the ocean (approximately 150 million tons) continuously breaks down into microplastics through UV, wave action, and biological processes. This fragmentation continues for centuries regardless of new input."
        },
        {
            "question": "A student compares three model scenarios: business as usual, recycling improvement only, and system transformation (production reduction + circular economy + producer responsibility). Only the system transformation shows a meaningful decline in environmental plastic. What does this reveal about the plastic pollution problem?",
            "choices": {
                "A": "Recycling is a waste of resources and should be abandoned entirely",
                "B": "Downstream solutions alone cannot solve a problem driven by exponential upstream production growth; addressing the source is essential",
                "C": "System transformation is too expensive to be practical",
                "D": "Plastic pollution will solve itself naturally over time without any intervention"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that when production grows exponentially, downstream waste management can only slow accumulation, not reverse it. Only reducing production at the source, combined with circular design and recycling, can actually decrease environmental plastic loading.",
            "feedback_incorrect": "Incorrect. The model evidence shows a fundamental asymmetry: downstream solutions (recycling, cleanup) cannot keep pace with exponential upstream growth (production). Only addressing the source (reducing production, circular design) while also improving downstream management can reverse the trend."
        },
        {
            "question": "The model shows that bioaccumulation causes microplastic concentrations in top predators to be orders of magnitude higher than in surrounding water. Which principle of ecology explains this amplification?",
            "choices": {
                "A": "Energy flows efficiently from lower to higher trophic levels",
                "B": "Biomagnification, where persistent substances that are ingested but not excreted accumulate at each trophic level, reaching highest concentrations in top predators",
                "C": "Top predators preferentially seek out and consume plastic-contaminated prey",
                "D": "Ocean currents deliver microplastics directly to top predator habitats"
            },
            "correct": "B",
            "feedback_correct": "Correct. Biomagnification occurs because persistent substances like microplastics are consumed at each trophic level but not efficiently excreted. Each predator accumulates the plastics from all the prey it consumes over its lifetime, resulting in exponentially increasing concentrations up the food chain.",
            "feedback_incorrect": "Incorrect. Biomagnification is the key process. Since microplastics are persistent and not efficiently eliminated by organisms, each consumer accumulates the plastic burden of all the organisms it eats. Across multiple trophic levels, this produces dramatically amplified concentrations in top predators."
        },
        {
            "question": "A student argues that ocean cleanup projects are the solution to marine plastic pollution. Based on model evidence about plastic pathways and accumulation dynamics, what is the most accurate evaluation of this claim?",
            "choices": {
                "A": "Ocean cleanup is the complete solution because all plastic pollution is in the ocean",
                "B": "Ocean cleanup addresses the symptom but not the cause; without reducing input, cleanup efforts are overwhelmed by the 8-12 million tons entering the ocean annually, and they cannot capture microplastics",
                "C": "Ocean cleanup is unnecessary because plastic naturally biodegrades within a few years",
                "D": "Ocean cleanup should be the sole focus because it is more cost-effective than reducing production"
            },
            "correct": "B",
            "feedback_correct": "Correct. Model evidence shows that 8-12 million tons of plastic enter the ocean annually, far exceeding any cleanup capacity. Additionally, cleanup technologies cannot effectively capture microplastics, which are the most harmful form. Without reducing the input, cleanup is necessary but insufficient.",
            "feedback_incorrect": "Incorrect. The model clearly shows that input rate (8-12 million tons/year) vastly exceeds any realistic cleanup capacity. Furthermore, once plastic fragments into microplastics, it becomes essentially impossible to remove. Cleanup is a valuable complement but cannot solve the problem without source reduction."
        },
        {
            "question": "Based on the model's findings about plastic pollution pathways, which policy intervention would most effectively reduce long-term environmental plastic accumulation and human health exposure?",
            "choices": {
                "A": "Banning plastic straws and bags while allowing production growth to continue",
                "B": "Extended producer responsibility laws that require manufacturers to design for circularity and fund end-of-life management, combined with production caps",
                "C": "Subsidizing plastic production to make recycling more economically attractive",
                "D": "Increasing landfill capacity in coastal areas to prevent ocean leakage"
            },
            "correct": "B",
            "feedback_correct": "Correct. Extended producer responsibility addresses the root cause by shifting the cost of waste management to producers, incentivizing design for circularity. Combined with production caps, it addresses both the upstream source and downstream management, which the model shows is the only effective combination.",
            "feedback_incorrect": "Incorrect. The model shows that effective solutions must address both production and waste management. Extended producer responsibility creates economic incentives for manufacturers to design durable, recyclable products, while production caps prevent exponential growth from overwhelming improved waste management."
        }
    ]
}

L05_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Current extinction rates are estimated at 100-1,000 times the natural background rate. Which factor has the strongest correlation with species extinction risk in terrestrial ecosystems?",
            "choices": {
                "A": "Natural predation pressure within food webs",
                "B": "Habitat loss and fragmentation from land use change",
                "C": "Natural climate variability within historical ranges",
                "D": "Competition from closely related species"
            },
            "correct": "B",
            "feedback_correct": "Correct. Habitat loss and fragmentation from human land use change is the primary driver of the current extinction crisis. It reduces total habitat area, isolates populations below viable sizes, and blocks migration corridors needed for climate adaptation.",
            "feedback_incorrect": "Incorrect. While multiple factors contribute to extinction, habitat loss and fragmentation from human land use change is overwhelmingly the strongest driver. It directly reduces population sizes, isolates gene pools, and prevents the movement needed for climate adaptation."
        },
        {
            "question": "Why is habitat fragmentation considered more damaging to biodiversity than an equivalent amount of simple habitat loss?",
            "choices": {
                "A": "Fragmentation only affects plant species, not animals",
                "B": "Fragmentation creates edge effects, blocks migration corridors, isolates populations genetically, and prevents species from tracking climate change",
                "C": "Fragmentation increases total habitat area by creating more edges",
                "D": "Fragmented habitats have higher species diversity because of increased habitat types"
            },
            "correct": "B",
            "feedback_correct": "Correct. Fragmentation compounds the damage of area loss by creating multiple additional threats: edge effects degrade habitat quality, isolation prevents gene flow and recolonization, migration barriers trap populations in unsuitable conditions, and small isolated populations face inbreeding depression.",
            "feedback_incorrect": "Incorrect. Fragmentation is more destructive because it does much more than reduce area. It isolates populations into patches too small for viability, creates degraded edge habitat, blocks the corridors species need to migrate with climate change, and prevents the gene flow needed for genetic health."
        },
        {
            "question": "The concept of minimum viable population (MVP) suggests that most mammals need 500-5,000 individuals to survive long-term. What happens to populations that fall below this threshold?",
            "choices": {
                "A": "They rapidly evolve adaptations to survive at small population sizes",
                "B": "They face increasing risk from inbreeding depression, genetic drift, and random demographic events that can drive extinction",
                "C": "They are automatically protected by natural compensatory mechanisms",
                "D": "They stabilize at a lower population level with no change in viability"
            },
            "correct": "B",
            "feedback_correct": "Correct. Below MVP, populations enter an extinction vortex: inbreeding reduces fitness, genetic drift erodes adaptive variation, and small numbers make the population vulnerable to random events (disease outbreaks, extreme weather) that larger populations would survive.",
            "feedback_incorrect": "Incorrect. Below minimum viable population size, populations face compounding genetic and demographic threats. Inbreeding reduces reproductive fitness, genetic drift eliminates beneficial alleles, and small populations cannot buffer against random catastrophic events. These factors create a downward spiral called an extinction vortex."
        },
        {
            "question": "Ecosystem services such as pollination, water purification, and carbon storage are provided by biodiversity. What is the relationship between species loss and ecosystem function?",
            "choices": {
                "A": "Ecosystem function declines linearly with each species lost",
                "B": "Ecosystem function is maintained initially as redundant species compensate, but collapses rapidly past a threshold when critical functions are no longer covered",
                "C": "Ecosystem function improves as competition is reduced by species loss",
                "D": "Ecosystem function is independent of species diversity"
            },
            "correct": "B",
            "feedback_correct": "Correct. Ecosystems show functional redundancy up to a point. As species are lost, remaining species may compensate. But past a threshold, when species performing unique ecological roles disappear, ecosystem function collapses non-linearly because critical processes lose their biological agents.",
            "feedback_incorrect": "Incorrect. The relationship between biodiversity and ecosystem function is non-linear. Initial species losses may be buffered by functional redundancy, but past a critical threshold, the loss of species performing irreplaceable ecological roles causes rapid ecosystem function collapse."
        },
        {
            "question": "An extinction cascade occurs when the loss of one species triggers the decline of dependent species. Which type of species would most likely trigger the largest extinction cascade if removed?",
            "choices": {
                "A": "A rare species that occupies a specialized niche with few interactions",
                "B": "A keystone species with many ecological connections, such as a primary pollinator or top predator",
                "C": "The most abundant species in the ecosystem",
                "D": "A recently introduced invasive species"
            },
            "correct": "B",
            "feedback_correct": "Correct. Keystone species have disproportionate effects on ecosystem structure relative to their abundance. A primary pollinator connects to many plant species, which in turn support herbivores, predators, and decomposers. Removing this hub species propagates disruption throughout the interaction network.",
            "feedback_incorrect": "Incorrect. Extinction cascades are largest when highly connected species are removed. Keystone species like primary pollinators or top predators interact with many other species, so their loss cascades through the entire interaction network, affecting far more species than their direct dependents."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A model shows that extinction rates increase slowly with the first 30% of habitat loss but accelerate dramatically after 70% loss. What ecological principle explains this non-linear pattern?",
            "choices": {
                "A": "Species are equally distributed across all habitat, so loss is proportional",
                "B": "Below 70% loss, remaining patches are large enough to support viable populations and maintain connectivity, but beyond that threshold, populations become too small and isolated to persist",
                "C": "The first 30% of habitat lost contains no species",
                "D": "After 70% loss, invasive species immediately colonize all remaining habitat"
            },
            "correct": "B",
            "feedback_correct": "Correct. The non-linearity reflects population viability thresholds. Early habitat loss still leaves patches large and connected enough for viable populations. Beyond approximately 70% loss, remaining patches are too small for minimum viable populations and too isolated for recolonization, triggering rapid extinction.",
            "feedback_incorrect": "Incorrect. The non-linear pattern results from population viability thresholds. Large connected patches support viable populations, so moderate loss has limited effect. But past a critical threshold, remaining patches drop below minimum viable population sizes and lose connectivity, causing extinction rates to accelerate dramatically."
        },
        {
            "question": "A student's model compares two landscapes with identical total protected area: one has a single large connected reserve, and the other has multiple small isolated fragments. The connected reserve supports significantly more species. Which concept does this demonstrate?",
            "choices": {
                "A": "Larger individual areas have lower per-hectare species diversity",
                "B": "Connectivity is a force multiplier that makes protected areas more effective than equal area in isolated fragments, due to gene flow, migration, and viable population sizes",
                "C": "Small fragments are always more species-rich due to edge effects",
                "D": "Protected area size has no relationship to species conservation outcomes"
            },
            "correct": "B",
            "feedback_correct": "Correct. This demonstrates the SLOSS principle (Single Large Or Several Small). Connected habitat supports larger, genetically healthier populations, enables migration and recolonization, and allows species to track climate change. The same total area in isolated fragments loses these connectivity benefits.",
            "feedback_incorrect": "Incorrect. Connectivity multiplies the conservation value of protected areas. A connected reserve supports larger populations above MVP thresholds, enables gene flow that prevents inbreeding, allows recolonization after local extinctions, and provides migration corridors for climate adaptation."
        },
        {
            "question": "The model shows that wildlife corridors connecting fragmented habitats significantly reduce extinction rates even without stopping habitat loss. What mechanism best explains this finding?",
            "choices": {
                "A": "Corridors increase total habitat area enough to offset ongoing losses",
                "B": "Corridors enable gene flow between isolated populations, allow recolonization of patches after local extinction, and permit species to shift ranges in response to climate change",
                "C": "Corridors prevent all human access to protected areas",
                "D": "Corridors only benefit large mammal species and have no effect on overall extinction rates"
            },
            "correct": "B",
            "feedback_correct": "Correct. Corridors do not add significant habitat area but provide critical connectivity functions: gene flow prevents inbreeding in small populations, recolonization rescues patches from local extinction, and range-shifting enables climate adaptation. These functions reduce extinction risk disproportionately to the area corridors occupy.",
            "feedback_incorrect": "Incorrect. Corridors work not by adding area but by restoring connectivity. They enable gene flow (preventing inbreeding), rescue effects (recolonization after local extinction), and climate migration (range shifts tracking temperature). These connectivity functions dramatically improve population viability across the landscape."
        },
        {
            "question": "A student models the removal of a keystone pollinator species and observes that 12 plant species decline, followed by 8 herbivore species, 3 predator species, and 2 decomposer species. Which systems concept does this cascade demonstrate?",
            "choices": {
                "A": "Simple linear cause and effect",
                "B": "Network propagation, where disruption at one node cascades through interdependent connections, amplifying the impact far beyond the directly affected species",
                "C": "Random species loss unrelated to the initial removal",
                "D": "Ecosystem resilience preventing any cascading effects"
            },
            "correct": "B",
            "feedback_correct": "Correct. The cascade demonstrates network propagation through species interaction networks. The pollinator's removal affects its plant partners, which affects their herbivores, which affects their predators, creating an amplifying chain reaction where one species loss triggers 25 additional declines.",
            "feedback_incorrect": "Incorrect. This is network propagation through an ecological interaction web. The initial loss propagates through trophic connections: pollinator loss reduces plant reproduction, plant decline reduces herbivore food, herbivore decline reduces predator prey, demonstrating how highly connected networks amplify disturbances."
        },
        {
            "question": "Based on model evidence, a conservation planner has a budget to either protect 5% more habitat or create wildlife corridors connecting existing protected areas. Which strategy would the model predict is more effective for reducing extinction rates, and why?",
            "choices": {
                "A": "Protecting 5% more habitat, because total area is always more important than connectivity",
                "B": "Creating corridors, because connectivity transforms isolated habitat islands into a functional network, producing biodiversity benefits disproportionate to the land area used",
                "C": "Neither strategy has any measurable effect on extinction rates",
                "D": "The strategies are exactly equivalent in their conservation outcomes"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that connectivity is a force multiplier. Wildlife corridors transform isolated protected areas into a functional network where gene flow, recolonization, and climate migration can occur. This connectivity benefit exceeds the marginal value of adding small amounts of unconnected area.",
            "feedback_incorrect": "Incorrect. Model evidence consistently shows that connectivity has disproportionate conservation value. Corridors enable the ecological processes (gene flow, recolonization, migration) that make existing protected areas functional, producing larger reductions in extinction risk per unit of land area than additional isolated habitat."
        }
    ]
}

L06_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Solar and wind energy are now cheaper than fossil fuels for new electricity generation in most of the world. What is the primary technical barrier preventing these sources from replacing fossil fuels entirely?",
            "choices": {
                "A": "Solar panels and wind turbines cannot generate enough total energy",
                "B": "Intermittency: solar and wind generation varies with weather and time of day, creating a mismatch between variable supply and relatively constant demand",
                "C": "Renewable energy cannot be transmitted through existing power lines",
                "D": "Fossil fuels produce higher quality electricity than renewables"
            },
            "correct": "B",
            "feedback_correct": "Correct. The fundamental challenge is intermittency. Solar produces no power at night, wind varies with weather, and electricity demand does not follow these patterns. Without sufficient storage and grid flexibility, this supply-demand mismatch limits renewable penetration.",
            "feedback_incorrect": "Incorrect. The primary barrier is intermittency. Renewables can generate sufficient total energy, but their output varies with weather and time of day. Matching variable supply to constant demand requires energy storage and grid flexibility that are currently insufficient."
        },
        {
            "question": "The capacity factor of solar panels is typically 15-25%, while natural gas plants achieve 90%+. What does this difference mean for grid planning?",
            "choices": {
                "A": "Solar panels are inherently less efficient at converting energy than gas plants",
                "B": "A renewable grid needs significantly more installed generation capacity than a fossil fuel grid to produce the same total energy output",
                "C": "Solar panels can only operate for 15-25% of their expected lifespan",
                "D": "Gas plants produce electricity that is 90% higher quality than solar electricity"
            },
            "correct": "B",
            "feedback_correct": "Correct. Capacity factor measures actual output versus maximum possible output. A 15-25% capacity factor means solar panels produce peak power only during sunny hours. To generate the same annual energy as a 90% capacity factor gas plant, a solar installation needs 3-6 times more nameplate capacity.",
            "feedback_incorrect": "Incorrect. Capacity factor reflects how much of the time a source produces at its rated output. Solar panels only produce at peak during sunny hours (15-25% of the time), so renewable grids need substantially more installed capacity to match the total energy output of always-on fossil fuel plants."
        },
        {
            "question": "Grid inertia is provided by the spinning mass of conventional generators. Why is the loss of grid inertia a concern as fossil fuel generators are replaced by solar and wind?",
            "choices": {
                "A": "Solar panels and wind turbines have no physical spinning mass, so grid frequency becomes harder to maintain during supply-demand imbalances",
                "B": "Grid inertia only matters in winter when energy demand is highest",
                "C": "Loss of inertia causes power lines to physically break",
                "D": "Wind turbines provide more inertia than conventional generators"
            },
            "correct": "A",
            "feedback_correct": "Correct. Grid frequency stability depends on the rotational inertia of large generators that resist frequency changes. Solar panels and most wind installations lack this physical inertia, requiring new solutions like synthetic inertia from battery inverters to maintain grid stability.",
            "feedback_incorrect": "Incorrect. Conventional generators have massive spinning rotors that naturally resist frequency changes, stabilizing the grid. Solar panels have no moving parts and provide no inertia. As fossil generators retire, new technologies must provide the frequency stabilization that spinning mass once supplied."
        },
        {
            "question": "A region wants to operate its grid on 100% renewable energy. Which technology is considered the most critical enabler for achieving this goal?",
            "choices": {
                "A": "More efficient solar panels",
                "B": "Energy storage systems (batteries, pumped hydro) that can absorb excess generation and dispatch it during low-generation periods",
                "C": "Larger wind turbines that generate more power per unit",
                "D": "Longer-lasting power transmission cables"
            },
            "correct": "B",
            "feedback_correct": "Correct. Energy storage is the keystone technology because it bridges the temporal mismatch between when renewable energy is generated (sunny/windy periods) and when it is needed (demand peaks, nighttime, calm periods). Without sufficient storage, high-renewable grids cannot maintain reliability.",
            "feedback_incorrect": "Incorrect. While all components matter, energy storage is the critical enabler. It solves the fundamental intermittency challenge by storing excess renewable generation for dispatch during low-generation periods, enabling reliable operation even when the sun is not shining and wind is not blowing."
        },
        {
            "question": "Global fossil fuel subsidies total approximately $5.9 trillion per year. How do these subsidies affect the renewable energy transition?",
            "choices": {
                "A": "They accelerate the transition by making fossil fuels too expensive to use",
                "B": "They slow the transition by artificially lowering fossil fuel prices, making it harder for renewables to compete despite lower unsubsidized costs",
                "C": "They have no effect because energy markets operate independently of government policy",
                "D": "They primarily fund renewable energy research and development"
            },
            "correct": "B",
            "feedback_correct": "Correct. Massive subsidies artificially reduce fossil fuel costs, creating an uneven playing field even though unsubsidized renewable generation is now cheaper. This policy distortion slows the transition by maintaining fossil fuel competitiveness that the market alone would not support.",
            "feedback_incorrect": "Incorrect. Fossil fuel subsidies create an artificial market distortion that slows the energy transition. By keeping fossil fuel prices below their true cost, subsidies undermine the natural cost advantage that renewables have achieved, maintaining fossil fuel market share that economics alone would not support."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's model shows that doubling renewable capacity without increasing storage causes grid instability above 40% renewable penetration. What system-level insight does this reveal?",
            "choices": {
                "A": "Renewable energy is fundamentally incapable of providing reliable power",
                "B": "The energy system has interdependent components; generation capacity alone is insufficient without proportional investment in storage and grid infrastructure to manage intermittency",
                "C": "40% renewable penetration is the absolute physical maximum for any grid",
                "D": "Storage technology cannot improve beyond current capabilities"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that the energy system functions as an integrated whole. Adding generation without storage creates excess power during sunny/windy periods and deficits during others. Reliable high-renewable operation requires coordinated investment across generation, storage, and grid management.",
            "feedback_incorrect": "Incorrect. The model demonstrates system interdependence, not a fundamental limitation. The 40% threshold is not a physical limit but a system integration constraint. With proportional storage and grid modernization, grids can operate reliably at 80-100% renewable penetration."
        },
        {
            "question": "The model shows that tripling storage capacity has a larger positive impact on grid reliability and carbon reduction than doubling renewable generation alone. What does this reveal about leverage points in the energy transition?",
            "choices": {
                "A": "Renewable generation is unnecessary if sufficient storage exists",
                "B": "Storage is the current bottleneck, and investing in the most constrained component produces the greatest system-wide improvement",
                "C": "Storage is always more important than generation in all energy systems",
                "D": "Carbon reduction is unrelated to grid reliability"
            },
            "correct": "B",
            "feedback_correct": "Correct. In systems thinking, the bottleneck constrains overall performance. Currently, storage is the binding constraint. Relieving this bottleneck unlocks the full potential of existing renewable capacity, producing outsized improvements in both reliability and carbon reduction compared to adding more generation alone.",
            "feedback_incorrect": "Incorrect. The finding reflects a bottleneck effect. In the current system, insufficient storage constrains the value of renewable generation. Relieving this bottleneck allows existing and planned renewable capacity to be used more effectively, producing the largest improvement per unit of investment."
        },
        {
            "question": "A model's integrated transition scenario achieves 80% renewable operation with maintained grid reliability. Which combination of factors makes this possible?",
            "choices": {
                "A": "Increased generation capacity alone without any other changes",
                "B": "Coordinated investment in renewable generation, energy storage, grid modernization, and demand flexibility working together as an integrated system",
                "C": "Maintaining fossil fuel backup for 80% of total capacity",
                "D": "Reducing total energy demand by 80% so that existing renewables are sufficient"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that reliable high-renewable operation requires coordinated investment in all system components. Generation provides the energy, storage bridges intermittency, modernized grids handle variable flows, and demand flexibility matches consumption to supply. No single component suffices alone.",
            "feedback_incorrect": "Incorrect. The model clearly demonstrates that 80% reliable renewable operation requires an integrated approach. No single component achieves this alone. Generation, storage, grid infrastructure, and demand flexibility must be developed in coordination, each addressing a different aspect of the intermittency challenge."
        },
        {
            "question": "A student analyzes why fossil fuels still provide 80% of global energy despite renewables being cheaper. Based on model evidence, which explanation best accounts for this paradox?",
            "choices": {
                "A": "Renewables are actually more expensive when all costs are included",
                "B": "Entrenched infrastructure, $5.9 trillion in annual subsidies, incumbent industry opposition, permitting delays, and the massive capital needed for grid transformation create barriers that override pure cost advantages",
                "C": "Consumers prefer fossil fuel electricity because it is higher quality",
                "D": "Renewable technology was only invented within the last 5 years"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that economic efficiency alone does not determine energy system composition. Entrenched infrastructure represents sunk costs, subsidies distort markets, incumbent industries resist change, and the enormous capital needed for grid transformation creates financing barriers despite favorable long-term economics.",
            "feedback_incorrect": "Incorrect. The paradox is explained by systemic barriers beyond simple cost comparison. Existing fossil fuel infrastructure, massive subsidies, political resistance from incumbent industries, permitting processes, and the scale of required grid investment all prevent the cost advantage of renewables from translating into rapid market replacement."
        },
        {
            "question": "Based on model evidence about the energy transition, a policy advisor must recommend the most effective single investment priority. Which recommendation is most strongly supported by the model?",
            "choices": {
                "A": "Invest exclusively in new renewable generation and let market forces handle the rest",
                "B": "Prioritize energy storage deployment because it is the current bottleneck that limits the effectiveness of all other clean energy investments",
                "C": "Invest exclusively in nuclear power as the only reliable low-carbon source",
                "D": "Focus solely on reducing energy demand rather than changing how energy is generated"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model consistently identifies storage as the bottleneck. Without sufficient storage, additional renewable capacity is curtailed during excess generation and cannot fill gaps during low generation. Storage investment unlocks the value of both existing and future renewable generation capacity.",
            "feedback_incorrect": "Incorrect. The model identifies storage as the binding constraint. As the current bottleneck, storage investment produces the largest marginal improvement in grid reliability and carbon reduction. It enables existing renewable capacity to be used fully and creates headroom for additional generation."
        }
    ]
}

L07_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Only 0.5% of Earth's total water is accessible freshwater. Which statement best explains why some regions face severe water scarcity despite Earth having abundant total water?",
            "choices": {
                "A": "Water evaporates too quickly for humans to use it",
                "B": "Most water is saltwater or frozen, and accessible freshwater is unevenly distributed, with many regions extracting groundwater faster than natural recharge",
                "C": "Freshwater cannot be transported between regions",
                "D": "All freshwater is polluted and unusable"
            },
            "correct": "B",
            "feedback_correct": "Correct. Of Earth's total water, 97.5% is saltwater and most freshwater is locked in ice caps. The tiny fraction that is accessible is unevenly distributed geographically, and many regions pump groundwater far faster than the slow natural recharge process, depleting supplies that took millennia to accumulate.",
            "feedback_incorrect": "Incorrect. Water scarcity results from the combination of limited accessibility (only 0.5% is usable freshwater), uneven geographic distribution, and unsustainable extraction rates that deplete groundwater aquifers much faster than natural processes can recharge them."
        },
        {
            "question": "Agriculture accounts for approximately 70% of global freshwater withdrawals. Which irrigation method is most responsible for water waste in agricultural systems?",
            "choices": {
                "A": "Drip irrigation, which delivers water directly to plant roots",
                "B": "Flood irrigation, which loses 40-60% of water to evaporation and runoff",
                "C": "Subsurface irrigation, which delivers water below the soil surface",
                "D": "Precision irrigation guided by soil moisture sensors"
            },
            "correct": "B",
            "feedback_correct": "Correct. Flood irrigation is extremely inefficient, losing 40-60% of water to evaporation and surface runoff before it reaches plant roots. Despite this waste, it remains the most common irrigation method globally because of its low technology requirements and initial cost.",
            "feedback_incorrect": "Incorrect. Flood irrigation is the most wasteful method, losing 40-60% of water to evaporation and runoff. In contrast, drip and precision irrigation systems deliver water directly to plant roots with 90-95% efficiency. Converting from flood to drip irrigation would dramatically reduce agricultural water demand."
        },
        {
            "question": "An aquifer that took 10,000 years to fill is being depleted at a rate that will exhaust it in 50 years. Why is this considered effectively irreversible on human timescales?",
            "choices": {
                "A": "Modern pumping technology can refill the aquifer once it is depleted",
                "B": "Natural recharge rates are measured in millimeters per year, meaning the aquifer would take thousands of years to recover, far beyond any human planning horizon",
                "C": "Artificial recharge can instantly replace depleted groundwater",
                "D": "Rain will automatically refill the aquifer within 5-10 years of pumping cessation"
            },
            "correct": "B",
            "feedback_correct": "Correct. Natural groundwater recharge occurs through slow percolation at rates of millimeters to centimeters per year. An aquifer depleted in decades would require thousands of years to refill naturally. This timescale mismatch makes aquifer depletion effectively permanent for any practical planning purpose.",
            "feedback_incorrect": "Incorrect. The key is the timescale mismatch between extraction and recharge. Water percolates into aquifers at millimeters per year through natural geological processes. Depleting in 50 years what took 10,000 years to accumulate means recovery would require millennia, making it irreversible for all practical purposes."
        },
        {
            "question": "Climate change is projected to make wet regions wetter and dry regions drier. How does this pattern affect global water security?",
            "choices": {
                "A": "It improves water security by increasing total global precipitation",
                "B": "It worsens water insecurity by concentrating precipitation in already water-rich areas while further reducing it in water-stressed regions that most need it",
                "C": "It has no effect because water can be easily redistributed between regions",
                "D": "It eliminates water scarcity by increasing evaporation and cloud formation"
            },
            "correct": "B",
            "feedback_correct": "Correct. Climate change intensifies the existing geographic inequality of water distribution. Regions already experiencing water stress receive less precipitation, while water-rich regions get more. This amplifies existing scarcity where it is most dangerous, threatening agriculture and populations in arid regions.",
            "feedback_incorrect": "Incorrect. The pattern of wet-gets-wetter, dry-gets-drier amplifies existing geographic inequality. Regions already facing water stress become drier while water-rich areas receive more precipitation. This spatial mismatch worsens water insecurity where it matters most, particularly in agricultural regions dependent on irrigation."
        },
        {
            "question": "Desalination can theoretically provide unlimited freshwater from the ocean. What are the primary limitations that prevent desalination from solving the global water crisis?",
            "choices": {
                "A": "Desalination technology does not yet exist at any scale",
                "B": "High energy requirements (3-10 kWh per cubic meter), concentrated brine waste, and costs 3-5 times higher than conventional freshwater make it impractical for large-scale agricultural use",
                "C": "Desalinated water is unsafe for human consumption",
                "D": "There is not enough ocean water to meet freshwater demand through desalination"
            },
            "correct": "B",
            "feedback_correct": "Correct. Desalination is technologically feasible but limited by high energy costs, environmental damage from brine waste discharge, and economics that make it 3-5 times more expensive than conventional freshwater. These constraints make it viable for urban drinking water but impractical for the massive volumes needed in agriculture.",
            "feedback_incorrect": "Incorrect. Desalination technology works but faces practical constraints. Its high energy requirement makes it expensive, concentrated brine waste damages marine ecosystems, and costs 3-5 times higher than conventional sources make it unsuitable for the agricultural sector, which consumes 70% of freshwater."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's water system model shows that increasing demand by 30% causes groundwater levels to accelerate their decline non-linearly. What explains this acceleration rather than a proportional increase in depletion rate?",
            "choices": {
                "A": "The model is incorrectly programmed",
                "B": "As groundwater levels drop, pumping requires more energy and draws from less productive zones, while reduced water tables decrease recharge rates, creating a positive feedback loop that accelerates depletion",
                "C": "Demand increases are always non-linear regardless of the system",
                "D": "Surface water compensates for groundwater loss, hiding the true rate"
            },
            "correct": "B",
            "feedback_correct": "Correct. Groundwater depletion involves positive feedback. As levels drop, recharge pathways shorten, reducing natural replenishment. Deeper pumping accesses less permeable zones with lower yields. The aquifer's ability to sustain extraction decreases as it depletes, accelerating the decline beyond the proportional increase in demand.",
            "feedback_incorrect": "Incorrect. The non-linear acceleration results from feedback dynamics in the groundwater system. As aquifer levels decline, recharge rates decrease, pumping efficiency drops, and land subsidence can permanently reduce storage capacity. These feedbacks compound the direct effect of increased extraction."
        },
        {
            "question": "The model shows that a 20% precipitation decline causes water crisis faster than a 30% demand increase. What does this comparison reveal about the water system?",
            "choices": {
                "A": "Demand management is irrelevant to water security",
                "B": "Supply-side disruptions are more destabilizing because they simultaneously reduce surface water, groundwater recharge, and ecosystem water, while demand increases affect only extraction rates",
                "C": "Precipitation has no connection to groundwater levels",
                "D": "The 20% and 30% numbers are not comparable because they measure different things"
            },
            "correct": "B",
            "feedback_correct": "Correct. Precipitation decline acts as a supply shock that affects every component simultaneously: rivers drop, reservoir storage decreases, groundwater recharge slows, soil moisture falls, and ecosystem water needs go unmet. Demand increases only affect the extraction side, leaving natural recharge intact.",
            "feedback_incorrect": "Incorrect. Precipitation decline is more destabilizing because it reduces the fundamental input to the entire water system. Every component suffers simultaneously: surface flows, groundwater recharge, soil moisture, and ecosystem water. Demand increases only accelerate withdrawal without affecting the supply side."
        },
        {
            "question": "A student models a conservation strategy with 40% efficiency improvements and active water recycling. The model shows this can offset 30% demand growth but cannot restore depleted groundwater. What does this finding demonstrate about water system management?",
            "choices": {
                "A": "Efficiency improvements are useless because they cannot restore groundwater",
                "B": "Efficiency measures are necessary but insufficient in regions where demand already exceeds sustainable supply; structural changes to water allocation are also required",
                "C": "Groundwater depletion is a natural process that should not concern water managers",
                "D": "Recycling produces water of lower quality that cannot substitute for freshwater"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that efficiency gains can manage future demand growth but cannot undo historical overextraction. In regions where aquifers are already depleted beyond recovery, conservation must be paired with structural reforms: changing crop types, reducing irrigated acreage, or developing alternative water sources.",
            "feedback_incorrect": "Incorrect. Efficiency improvements are valuable for managing growth but cannot reverse existing depletion. The model shows that in overdrafted regions, demand management alone is insufficient. Structural changes to agricultural practices, water rights allocation, and alternative supply development are required to achieve sustainability."
        },
        {
            "question": "The model shows that ignoring ecosystem water requirements to meet human demand ultimately reduces total usable water. Which mechanism explains this counterintuitive finding?",
            "choices": {
                "A": "Ecosystems consume water that could otherwise be used by humans",
                "B": "Healthy riparian ecosystems filter water, reduce erosion, maintain water tables, and recharge aquifers; degrading these systems reduces water quality and quantity for everyone",
                "C": "Ecosystem water requirements are always larger than human water needs",
                "D": "Ecosystems transport water from dry regions to wet regions"
            },
            "correct": "B",
            "feedback_correct": "Correct. Ecosystems provide essential water services: wetlands filter pollutants, riparian vegetation prevents erosion, forest soils enhance infiltration and groundwater recharge, and healthy watersheds regulate flow. Depriving ecosystems of water degrades these services, ultimately reducing the quantity and quality of water available for human use.",
            "feedback_incorrect": "Incorrect. The counterintuitive finding reflects the water-provisioning role of ecosystems. Wetlands purify water, vegetation controls erosion, forests enhance groundwater recharge, and healthy watersheds regulate flow timing. When these ecosystem functions are degraded by water diversion, total water availability and quality decline."
        },
        {
            "question": "Based on the model, a water manager must advise a semi-arid agricultural region facing both population growth and climate-driven precipitation decline. Which recommendation is most strongly supported by the model evidence?",
            "choices": {
                "A": "Continue current groundwater pumping rates and drill deeper wells as levels decline",
                "B": "Implement a comprehensive strategy combining irrigation efficiency improvements, crop transitions to less water-intensive varieties, managed aquifer recharge, and enforceable extraction limits to stabilize groundwater levels",
                "C": "Abandon all agriculture and rely entirely on food imports",
                "D": "Build a single large desalination plant to replace all groundwater use"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that no single intervention is sufficient. The comprehensive strategy addresses demand (efficiency, crop transitions), supply (managed recharge), and governance (extraction limits). This multi-pronged approach is the only pathway that achieves long-term groundwater stability.",
            "feedback_incorrect": "Incorrect. Model evidence clearly supports a comprehensive approach. Efficiency gains alone are insufficient, drilling deeper accelerates depletion, desalination is too expensive for agriculture, and abandoning agriculture is socioeconomically catastrophic. Only the combination of demand reduction, supply enhancement, and governance reform can achieve sustainability."
        }
    ]
}

L08_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Fire ecologists argue that frequent low-intensity fires are essential for maintaining healthy forest ecosystems. What ecological benefit do these natural fires provide?",
            "choices": {
                "A": "They permanently sterilize the soil to prevent invasive plant growth",
                "B": "They clear understory fuel, recycle nutrients, stimulate seed germination, and maintain open forest structure that supports biodiversity",
                "C": "They eliminate all plant species so the ecosystem can start fresh",
                "D": "They have no ecological benefit and only cause destruction"
            },
            "correct": "B",
            "feedback_correct": "Correct. Low-intensity surface fires perform essential ecological functions: clearing dead vegetation reduces fuel accumulation, burning releases locked-up nutrients back to soil, fire-adapted species depend on fire cues for seed germination, and open understory structure supports diverse plant and animal communities.",
            "feedback_incorrect": "Incorrect. Natural low-intensity fires are ecological maintenance processes. They reduce fuel loads, cycle nutrients from dead material back into soil, trigger reproduction in fire-adapted species, and maintain the open forest structure that many species require. Many ecosystems evolved with and depend on regular fire."
        },
        {
            "question": "A century of fire suppression has dramatically increased fuel loads in many forests. What is a fuel load, and why is its accumulation dangerous?",
            "choices": {
                "A": "Fuel load is the energy content of living trees, which decreases with forest age",
                "B": "Fuel load is the amount of combustible dead vegetation, branches, and debris that accumulates when fire is excluded, creating conditions for catastrophic high-intensity fires",
                "C": "Fuel load is the water content of forest soil, which fire suppression increases",
                "D": "Fuel load is a measure of forest productivity that has no relationship to fire behavior"
            },
            "correct": "B",
            "feedback_correct": "Correct. Without periodic fire to clear dead vegetation, fuel accumulates to 5-10 times natural levels. This dense layer of dead material, combined with ladder fuels that connect the ground to the canopy, transforms what would be a manageable surface fire into an uncontrollable crown fire.",
            "feedback_incorrect": "Incorrect. Fuel load is the total combustible material in a forest. When fire is suppressed for decades, dead leaves, branches, small trees, and other vegetation accumulate instead of being periodically cleared by natural fire. This creates conditions for fires of unprecedented intensity that exceed the ecosystem's tolerance."
        },
        {
            "question": "What is the difference between a surface fire and a crown fire, and why does this distinction matter ecologically?",
            "choices": {
                "A": "Surface fires burn along the ground and most trees survive; crown fires burn through the canopy at extreme intensity, often killing even fire-resistant trees and destroying seed sources",
                "B": "Surface fires are hotter than crown fires but cover less area",
                "C": "Crown fires only occur in deciduous forests, while surface fires occur in coniferous forests",
                "D": "There is no ecological difference between surface and crown fires"
            },
            "correct": "A",
            "feedback_correct": "Correct. This distinction is ecologically crucial. Surface fires burn at temperatures that thick-barked trees survive, leaving mature trees and seed sources intact for rapid recovery. Crown fires burn at extreme temperatures that kill even fire-resistant species and destroy the seed bank, potentially preventing forest regeneration entirely.",
            "feedback_incorrect": "Incorrect. The surface versus crown fire distinction determines ecological outcome. Surface fires burn at low intensity along the ground, leaving mature trees alive for regeneration. Crown fires burn through the canopy at extreme temperatures, killing even large fire-resistant trees and potentially eliminating the seed sources needed for recovery."
        },
        {
            "question": "Climate change has extended fire seasons by 40-80 days in many regions. How does this interact with accumulated fuel loads from fire suppression?",
            "choices": {
                "A": "Extended fire seasons have no effect because fire suppression prevents all fires",
                "B": "Hotter, drier conditions combined with unprecedented fuel loads create conditions for fires of intensity and duration that have no historical precedent in these ecosystems",
                "C": "Climate change makes forests wetter, reducing fire risk despite accumulated fuel",
                "D": "Extended fire seasons allow more prescribed burns, naturally solving the fuel accumulation problem"
            },
            "correct": "B",
            "feedback_correct": "Correct. Climate change and fire suppression create a compounding interaction. A century of fuel accumulation meets hotter temperatures, longer droughts, lower humidity, and stronger winds, producing fire behavior that exceeds anything in the historical record and overwhelms ecosystems adapted to lower-intensity fire regimes.",
            "feedback_incorrect": "Incorrect. Climate change and fire suppression compound each other's effects. The accumulated fuel from decades of suppression is now exposed to hotter, drier, and windier conditions from climate change, producing megafires of unprecedented intensity that exceed both historical fire regimes and current firefighting capacity."
        },
        {
            "question": "What is ecological succession, and how does fire intensity determine the trajectory of post-fire ecosystem recovery?",
            "choices": {
                "A": "Succession is the replacement of one species by a more competitive species, unrelated to fire",
                "B": "Succession is the process by which ecosystems change in composition over time after disturbance. Low-intensity fire promotes recovery along historical trajectories, while extreme fire can redirect succession toward entirely different ecosystem types",
                "C": "Succession always produces the same ecosystem regardless of disturbance type",
                "D": "Succession only occurs in aquatic ecosystems after flooding events"
            },
            "correct": "B",
            "feedback_correct": "Correct. Fire intensity determines whether succession follows a recovery pathway or a conversion pathway. Low-intensity fire leaves seed sources, mycorrhizal networks, and seed banks intact, enabling the ecosystem to recover its original composition. Extreme fire can destroy all of these, redirecting succession toward shrubland or grassland.",
            "feedback_incorrect": "Incorrect. Ecological succession is the directional change in community composition after disturbance. Fire intensity critically determines the trajectory: moderate fire allows recovery to the original community type, while extreme fire that sterilizes soil and destroys seed sources can permanently redirect succession toward a different ecosystem type."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student compares model outputs for a natural fire regime (moderate fuel, historical climate) versus a fire after 100 years of suppression (maximum fuel, current climate). The suppression-legacy fire shows 10 times greater intensity and severely degraded soil health. What systemic lesson does this comparison illustrate?",
            "choices": {
                "A": "Fire suppression has no long-term consequences for forest health",
                "B": "Attempting to prevent all disturbance in a disturbance-dependent system does not eliminate the disturbance but transforms it from a manageable, beneficial process into a catastrophic one",
                "C": "Fuel load has no effect on fire intensity",
                "D": "Historical fire regimes were more destructive than modern fires"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is a fundamental systems lesson: fire-adapted ecosystems require periodic disturbance. Suppressing natural fire does not eliminate fire but guarantees that when fire eventually occurs (as it inevitably will), it will be catastrophically intense due to accumulated fuel, causing far more damage than the natural fires that were prevented.",
            "feedback_incorrect": "Incorrect. The comparison reveals the paradox of fire suppression: preventing small fires guarantees large ones. Fire-adapted ecosystems evolved with periodic burning. Removing fire from these systems does not create safety but accumulates risk, transforming inevitable future fire from beneficial to catastrophic."
        },
        {
            "question": "The model shows that a climate-amplified megafire (maximum fuel + extreme heat, drought, and wind) can sterilize soil to 10+ cm depth and destroy seed banks. A student predicts that the forest will recover naturally within 15 years. What does the model evidence suggest about this prediction?",
            "choices": {
                "A": "The prediction is accurate because all fires are followed by rapid recovery",
                "B": "The prediction is likely wrong because soil sterilization and seed bank destruction remove the biological resources needed for forest recovery, potentially causing permanent type-conversion to shrubland or grassland",
                "C": "The forest will recover faster than 15 years because fire releases nutrients",
                "D": "The soil sterilization only affects the first growing season"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that when fire exceeds ecosystem tolerance thresholds, recovery may be impossible. Sterilized soil lacks mycorrhizal fungi, seed banks are destroyed, and mature seed-producing trees are killed. Without these biological resources, the ecosystem cannot regenerate as forest and may convert permanently to a different vegetation type.",
            "feedback_incorrect": "Incorrect. The model evidence contradicts natural recovery from extreme fire. When soil is sterilized to depth, seed banks destroyed, and seed-producing trees killed, the biological resources for forest recovery no longer exist. The ecosystem may undergo type-conversion to shrubland or grassland, representing permanent habitat loss."
        },
        {
            "question": "A model shows that healthy forests are carbon sinks, absorbing more CO2 than they release. After a megafire, the model shows the forest becoming a net carbon source for decades. What mechanism drives this reversal?",
            "choices": {
                "A": "Wildfires absorb CO2 from the atmosphere during combustion",
                "B": "The fire rapidly releases stored carbon through combustion, while killing the living trees that would reabsorb it, and decomposition of dead wood continues releasing carbon for years after the fire",
                "C": "Carbon sinks and sources are unrelated to living biomass",
                "D": "Post-fire vegetation immediately compensates for all carbon lost in the fire"
            },
            "correct": "B",
            "feedback_correct": "Correct. Megafires release decades of stored carbon in hours through combustion. They also kill the trees that serve as active carbon sinks. Dead trees and roots then decompose over years, continuing to release CO2. Without living trees to reabsorb carbon, the area remains a net source for decades, creating a positive climate feedback.",
            "feedback_incorrect": "Incorrect. The carbon reversal occurs through two mechanisms: rapid release of stored carbon during combustion, and the loss of living trees that would otherwise continue absorbing CO2. Dead biomass continues decomposing and releasing carbon for years, while regeneration (if it occurs at all) takes decades to restore sink function."
        },
        {
            "question": "The model demonstrates that prescribed burns reduce fuel loads and lower the intensity of subsequent wildfires. A community member opposes prescribed burns because 'setting fires in forests is never safe.' Based on model evidence, how should a fire ecologist respond?",
            "choices": {
                "A": "Agree that all fire in forests should be prevented",
                "B": "Explain that model evidence shows controlled low-intensity prescribed burns reduce future wildfire intensity by removing accumulated fuel, and that the alternative to managed fire is not no fire but rather unmanaged catastrophic fire",
                "C": "Ignore the community member's concern because science always overrides public opinion",
                "D": "Recommend clear-cutting the forest instead of prescribed burning"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model provides clear evidence that the choice is not between fire and no fire, but between managed fire (prescribed burns at low intensity) and unmanaged fire (catastrophic wildfire at extreme intensity). Model data showing that fuel reduction through prescribed burns dramatically lowers future fire intensity makes the evidence-based case for proactive fire management.",
            "feedback_incorrect": "Incorrect. The model evidence directly addresses this concern. It shows that fire in fire-adapted ecosystems is inevitable. The real choice is between deliberate low-intensity prescribed burns that reduce fuel and maintain ecosystem health, or waiting for catastrophic wildfire that destroys ecosystems and threatens communities."
        },
        {
            "question": "Based on model evidence about fire ecology, climate change, and ecosystem resilience, which fire management strategy would be most effective for long-term forest and community protection?",
            "choices": {
                "A": "Continue aggressive fire suppression of all fires to protect communities",
                "B": "An integrated approach that uses prescribed burns to reduce fuel in strategic areas, creates defensible space around communities, and allows ecological fire to play its natural role in wilderness areas",
                "C": "Allow all fires to burn without any management or community protection",
                "D": "Remove all forests within 50 miles of communities to eliminate fire risk"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that effective fire management requires an integrated strategy: prescribed burns reduce fuel loads and restore natural fire regimes, defensible space protects communities at the wildland-urban interface, and allowing ecological fire in appropriate areas maintains ecosystem health. This approach addresses both human safety and ecological integrity.",
            "feedback_incorrect": "Incorrect. Model evidence supports an integrated approach. Neither total suppression (which guarantees catastrophic fires) nor unmanaged fire (which threatens communities) is optimal. The evidence-based strategy combines proactive fuel management, community protection, and ecological fire stewardship."
        }
    ]
}

L09_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Solar radiation management (SRM) and carbon dioxide removal (CDR) are two categories of geoengineering. What is the fundamental difference between their approaches to addressing climate change?",
            "choices": {
                "A": "SRM removes CO2 from the atmosphere while CDR blocks sunlight",
                "B": "SRM masks warming by reducing incoming sunlight without removing CO2, while CDR addresses the root cause by removing CO2 from the atmosphere",
                "C": "SRM and CDR are identical technologies with different names",
                "D": "SRM increases greenhouse gas concentrations while CDR decreases solar output"
            },
            "correct": "B",
            "feedback_correct": "Correct. SRM (like stratospheric aerosol injection) reduces sunlight reaching Earth's surface, counteracting greenhouse warming without changing CO2 levels. CDR (like direct air capture) removes CO2 from the atmosphere, addressing the root cause. This distinction has critical implications for effectiveness, risk, and long-term dependency.",
            "feedback_incorrect": "Incorrect. The fundamental difference is that SRM treats the symptom (temperature) by reducing incoming sunlight, while CDR treats the cause (CO2) by removing greenhouse gases from the atmosphere. SRM creates dependency because the underlying CO2 problem persists, while CDR can produce permanent resolution."
        },
        {
            "question": "Termination shock is a major risk associated with solar radiation management. What would cause termination shock?",
            "choices": {
                "A": "SRM technologies becoming too effective at cooling the planet",
                "B": "Sudden cessation of SRM deployment, exposing the planet to the full accumulated greenhouse warming that was being masked",
                "C": "Gradual reduction in solar output from the sun",
                "D": "Increased volcanic eruptions triggered by SRM aerosols"
            },
            "correct": "B",
            "feedback_correct": "Correct. SRM masks warming without reducing CO2. If deployed for decades while CO2 continues accumulating, stopping SRM suddenly would expose Earth to all the hidden warming within months. This could produce several degrees of warming in under a decade, a rate of change far exceeding anything in human history.",
            "feedback_incorrect": "Incorrect. Termination shock would occur if SRM were suddenly stopped after years of deployment. Because SRM masks warming without reducing CO2, all the accumulated greenhouse warming hidden behind the solar shield would be unleashed rapidly, causing catastrophic temperature increases within months to years."
        },
        {
            "question": "Current carbon dioxide removal (CDR) technology removes approximately 0.01 gigatons of CO2 per year, while annual emissions are approximately 36 gigatons. What does this gap reveal about CDR as a climate solution?",
            "choices": {
                "A": "CDR is already operating at sufficient scale to solve climate change",
                "B": "CDR must be scaled up by approximately 3,600 times just to match current emissions, making it a complement to emission reduction rather than a substitute",
                "C": "The gap shows that CDR is impossible and should be abandoned",
                "D": "CDR will automatically scale to match emissions through market forces within 5 years"
            },
            "correct": "B",
            "feedback_correct": "Correct. The 3,600-fold gap between current CDR capacity and annual emissions demonstrates that CDR cannot substitute for emission reduction at any realistic timescale. It can be a valuable complement by drawing down legacy CO2 after emissions are drastically cut, but achieving net-negative emissions requires massive emission reduction first.",
            "feedback_incorrect": "Incorrect. The gap between 0.01 Gt/year CDR capacity and 36 Gt/year emissions represents a 3,600-fold scale difference. This makes clear that CDR cannot replace emission reduction in any realistic scenario but can play a supporting role in achieving net-negative emissions after the heavy lifting of decarbonization."
        },
        {
            "question": "The moral hazard of geoengineering refers to which risk?",
            "choices": {
                "A": "Geoengineering technologies could directly harm human health",
                "B": "The availability of geoengineering could reduce the urgency to cut emissions, leading to continued fossil fuel dependence and ultimately worsening the problem",
                "C": "Geoengineering would be too expensive for any country to implement",
                "D": "Geoengineering would eliminate all natural weather variability"
            },
            "correct": "B",
            "feedback_correct": "Correct. Moral hazard is the risk that a perceived safety net reduces motivation to address the underlying problem. If policymakers believe geoengineering can fix climate change, they may delay the difficult transition away from fossil fuels, increasing long-term CO2 accumulation and making the climate problem worse while creating dependence on risky interventions.",
            "feedback_incorrect": "Incorrect. Moral hazard refers to the behavioral risk: if geoengineering is seen as a viable alternative to emission reduction, it could undermine political will for decarbonization. This delay would increase cumulative CO2, worsen the underlying problem, and create deeper dependence on interventions with serious risks and side effects."
        },
        {
            "question": "If a single nation unilaterally deployed stratospheric aerosol injection, what global governance challenge would this create?",
            "choices": {
                "A": "No governance challenge, because the effects would be limited to that nation's territory",
                "B": "SRM would alter global climate patterns including monsoon rainfall, creating international winners and losers from a decision made without the consent of affected nations",
                "C": "The technology is so expensive that no single nation could afford it",
                "D": "Other nations would automatically benefit equally from the cooling effect"
            },
            "correct": "B",
            "feedback_correct": "Correct. SRM's effects are inherently global and uneven. Stratospheric aerosols would reduce temperatures globally but could disrupt monsoon rainfall in South and East Asia, alter precipitation in Africa, and change tropical cyclone patterns. A unilateral decision affecting billions of people raises fundamental questions about global governance and justice.",
            "feedback_incorrect": "Incorrect. SRM is a global intervention with asymmetric effects. While it would cool the planet overall, it would alter regional weather patterns, potentially reducing monsoon rainfall critical for billions of people. Unilateral deployment creates a governance crisis: one nation's climate intervention becomes every nation's climate disruption."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's model shows that deploying SRM for 50 years while emissions continue causes Termination Risk to increase every year. What system dynamic creates this escalating risk?",
            "choices": {
                "A": "SRM aerosols accumulate in the stratosphere, becoming toxic over time",
                "B": "Each year of SRM masks additional CO2 accumulation, so the gap between actual temperature and masked temperature grows larger, making the consequences of stopping SRM progressively more catastrophic",
                "C": "SRM technology naturally degrades over time, losing effectiveness",
                "D": "Termination Risk decreases over time as ecosystems adapt to SRM conditions"
            },
            "correct": "B",
            "feedback_correct": "Correct. SRM creates a growing temperature debt. Each year that CO2 continues accumulating while warming is masked increases the difference between the temperature Earth would experience without SRM and the temperature being maintained. Stopping SRM would expose this ever-growing temperature gap, making termination shock progressively worse.",
            "feedback_incorrect": "Incorrect. The escalating risk comes from the growing gap between masked and actual greenhouse forcing. SRM holds temperature down while CO2 rises behind the shield. Each year, the accumulated CO2 represents more warming potential, so stopping SRM would produce an ever-larger temperature jump."
        },
        {
            "question": "A student's model shows that SRM stabilizes global temperature but ocean acidification continues worsening. What does this divergence reveal about the difference between treating symptoms versus causes?",
            "choices": {
                "A": "The model is flawed because temperature and acidification should always move together",
                "B": "SRM only addresses the temperature symptom of excess CO2 while leaving the chemical cause (atmospheric CO2 dissolving in oceans) completely unaddressed",
                "C": "Ocean acidification is unrelated to atmospheric CO2 and has a separate cause",
                "D": "SRM should increase ocean pH because cooler water absorbs less CO2"
            },
            "correct": "B",
            "feedback_correct": "Correct. This divergence powerfully demonstrates the difference between symptom management and cause treatment. SRM reduces incoming solar radiation (the temperature symptom) but does nothing about atmospheric CO2 (the cause). Since ocean acidification is driven by CO2 absorption, not temperature, it continues unabated.",
            "feedback_incorrect": "Incorrect. The divergence is a critical insight: SRM masks the temperature effect of CO2 but does nothing about the CO2 itself. Ocean acidification is caused by dissolved CO2 lowering ocean pH, a process entirely independent of temperature management. SRM's selective effect on temperature but not chemistry exposes its fundamental limitation."
        },
        {
            "question": "A model comparison shows that emission reduction combined with CDR produces the best outcomes with the lowest risk. A student asks why emission reduction alone is not sufficient. Which answer is best supported by the model?",
            "choices": {
                "A": "Emission reduction has no effect on atmospheric CO2 levels",
                "B": "Even with aggressive emission reduction, the legacy CO2 already in the atmosphere continues driving warming and acidification. CDR can actively draw down this legacy stock, accelerating the return to safer CO2 levels",
                "C": "CDR is easier and cheaper than emission reduction in all scenarios",
                "D": "Emission reduction only affects CO2 while CDR affects all greenhouse gases simultaneously"
            },
            "correct": "B",
            "feedback_correct": "Correct. Emission reduction stops adding new CO2 (addressing flow) but does not remove the approximately 1 trillion tons of excess CO2 already accumulated (the stock). CDR addresses this legacy stock, actively drawing down atmospheric CO2 toward safer levels. The combination addresses both flow and stock.",
            "feedback_incorrect": "Incorrect. The distinction is between flow and stock. Emission reduction stops the flow of new CO2 into the atmosphere, but the accumulated stock of excess CO2 continues affecting climate. CDR addresses this stock by actively removing legacy CO2, which emission reduction alone cannot do."
        },
        {
            "question": "A model reveals that SRM deployment would reduce monsoon rainfall in South Asia, where 1.5 billion people depend on monsoon agriculture. A wealthy nation proposes SRM to reduce its heat wave deaths. What ethical framework is most relevant for evaluating this decision?",
            "choices": {
                "A": "Cost-benefit analysis focused exclusively on the deploying nation",
                "B": "Environmental justice, which requires evaluating whether the intervention distributes benefits and harms equitably and whether affected populations have meaningful consent in the decision",
                "C": "Technological determinism, which holds that all available technologies should be deployed regardless of consequences",
                "D": "Free market principles, where whichever nation can afford the technology should deploy it"
            },
            "correct": "B",
            "feedback_correct": "Correct. Environmental justice demands that climate interventions distribute benefits and burdens equitably and that affected populations participate in decisions. SRM that reduces one nation's heat waves while disrupting another's food supply raises fundamental justice questions about who bears the risks of global climate engineering.",
            "feedback_incorrect": "Incorrect. The environmental justice framework is most relevant because it addresses the central ethical issue: one population's benefit at another's expense. Justice requires that affected communities (1.5 billion people dependent on monsoon agriculture) have meaningful voice and consent in decisions that affect their lives."
        },
        {
            "question": "Based on model evidence, a climate advisor must recommend a pathway for addressing warming that has reached 1.8 degrees Celsius. Which recommendation is most strongly supported by the combined scientific and ethical evidence?",
            "choices": {
                "A": "Immediate SRM deployment to prevent crossing 2 degrees, with no emission reduction",
                "B": "Aggressive emission reduction as the primary strategy, complemented by moderate CDR deployment, with SRM held in reserve only as an emergency measure with international governance and consent frameworks",
                "C": "No action, because climate engineering technologies are too risky to consider under any circumstances",
                "D": "Maximum CDR deployment to remove all excess CO2 within 5 years while maintaining current emission levels"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that emission reduction addresses the root cause with the lowest risk. CDR complements it by drawing down legacy CO2. SRM carries significant risks (termination shock, regional disruption, governance challenges) but may be warranted as an emergency measure if tipping points are imminent, provided international governance ensures equitable decision-making.",
            "feedback_incorrect": "Incorrect. Model evidence supports a layered approach: emission reduction as the foundation (lowest risk, addresses root cause), CDR as a complement (draws down legacy CO2), and SRM only as a governed emergency measure. This balances scientific effectiveness with ethical requirements for equitable global governance."
        }
    ]
}

L10_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Environmental justice research consistently finds that low-income communities and communities of color bear disproportionate pollution burdens. Which systemic factor most strongly explains this pattern?",
            "choices": {
                "A": "These communities voluntarily choose to live near pollution sources",
                "B": "Historical zoning decisions, industrial siting practices, and differential political power concentrated pollution sources where land was cheapest and political resistance was weakest",
                "C": "Pollution is randomly distributed across all communities equally",
                "D": "Environmental regulations apply equally to all communities with perfect enforcement"
            },
            "correct": "B",
            "feedback_correct": "Correct. Environmental inequity results from systemic processes: industrial facilities were sited where land costs were lowest and political opposition weakest, exclusionary zoning policies concentrated polluting uses in disadvantaged neighborhoods, and unequal political power prevented communities from blocking unwanted facilities.",
            "feedback_incorrect": "Incorrect. The pattern is not voluntary or random. It results from historical decisions that concentrated pollution sources in communities with lower land values, weaker political representation, and less capacity to resist unwanted facility siting. These systemic factors created persistent spatial inequality in environmental burden."
        },
        {
            "question": "The concept of cumulative impact refers to the total environmental burden on a community from all combined sources. Why is cumulative impact a more accurate measure of environmental injustice than evaluating individual pollution sources?",
            "choices": {
                "A": "Individual sources are always below regulatory limits, so cumulative impact is irrelevant",
                "B": "Communities face multiple simultaneous exposures, such as air pollution, contaminated water, toxic facilities, and lack of green space. The combined health effect far exceeds the sum of individual exposures",
                "C": "Cumulative impact only applies to communities with a single pollution source",
                "D": "Regulatory agencies already account for cumulative impact in all permits"
            },
            "correct": "B",
            "feedback_correct": "Correct. Cumulative impact captures the reality that disadvantaged communities typically face multiple overlapping environmental burdens. A community near a highway, a refinery, and a waste facility with lead-contaminated water experiences a total exposure that is far more harmful than any single source alone, yet regulations typically evaluate sources individually.",
            "feedback_incorrect": "Incorrect. Cumulative impact is the correct framework because environmental injustice involves multiple stacking exposures. Communities may face air pollution, water contamination, toxic facilities, noise, and lack of green space simultaneously. Their combined effect on health is synergistic, not merely additive, and is not captured by evaluating sources individually."
        },
        {
            "question": "A sacrifice zone is an area subjected to extreme environmental degradation. Which description best captures why sacrifice zones exist?",
            "choices": {
                "A": "They contain land that is naturally contaminated regardless of human activity",
                "B": "They are communities that absorb the pollution costs of production so that other communities can enjoy the products without health consequences, reflecting unequal power to resist facility siting",
                "C": "They are voluntarily designated by community vote",
                "D": "They exist equally across all income levels and demographics"
            },
            "correct": "B",
            "feedback_correct": "Correct. Sacrifice zones reflect a power imbalance. Refineries, chemical plants, and waste facilities must exist somewhere, and they are systematically placed where communities have the least power to resist. The benefits (products, energy) flow to society broadly while the health costs concentrate in specific disadvantaged communities.",
            "feedback_incorrect": "Incorrect. Sacrifice zones are not natural or voluntary. They result from power-driven facility siting decisions where the environmental costs of production are concentrated in communities with the least political power to resist. The term itself highlights that these communities are sacrificed for others' economic benefit."
        },
        {
            "question": "Studies show that environmental regulatory enforcement varies dramatically between communities. Which pattern do researchers typically find?",
            "choices": {
                "A": "Low-income communities receive more enforcement because they have more pollution",
                "B": "Polluters in low-income communities and communities of color face fewer inspections, lower penalties, and slower cleanup compared to polluters in affluent areas",
                "C": "Enforcement is perfectly equal across all demographics and income levels",
                "D": "Affluent communities receive less enforcement because they have fewer pollution sources"
            },
            "correct": "B",
            "feedback_correct": "Correct. Research consistently documents an enforcement gap: facilities in disadvantaged communities receive fewer inspections, face lower penalties for violations, and wait longer for contamination cleanup. This differential enforcement compounds the original inequity of pollution siting, allowing ongoing violations to persist.",
            "feedback_incorrect": "Incorrect. Research documents a significant enforcement gap. Polluting facilities in low-income communities and communities of color face less regulatory oversight, lower fines for violations, and slower cleanup timelines than identical facilities in affluent areas. This enforcement disparity compounds the original inequity of unequal pollution siting."
        },
        {
            "question": "Why is community political power considered a critical factor in environmental justice?",
            "choices": {
                "A": "Political power has no relationship to environmental conditions",
                "B": "Communities with greater political power can prevent unwanted facility siting, demand enforcement of environmental regulations, and influence zoning and planning decisions that affect their environmental quality",
                "C": "Political power only affects economic development, not environmental conditions",
                "D": "All communities have equal political power in environmental decision-making"
            },
            "correct": "B",
            "feedback_correct": "Correct. Political power determines whether communities can influence the decisions that shape their environmental conditions. Affluent communities successfully oppose polluting facilities, demand cleanup, and influence zoning. Communities with less political power cannot effectively resist unwanted siting or demand regulatory attention.",
            "feedback_incorrect": "Incorrect. Political power is the mechanism through which environmental conditions are determined. Communities with political influence can block polluting facilities, demand regulatory enforcement, and shape zoning decisions. Communities without this power become targets for unwanted land uses that more powerful communities refuse."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's model shows that environmental inequity is maintained by feedback loops: pollution reduces health, poor health reduces economic opportunity, reduced income limits political power, and less political power allows more pollution. What type of system dynamic does this represent?",
            "choices": {
                "A": "A negative feedback loop that self-corrects over time",
                "B": "A positive feedback loop (reinforcing cycle) that perpetuates and deepens inequity without external intervention",
                "C": "A simple linear cause-and-effect relationship",
                "D": "A random process with no systematic pattern"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is a positive (reinforcing) feedback loop where each consequence becomes a cause of further degradation. Pollution degrades health, which reduces income, which reduces political power, which allows more pollution. The cycle self-reinforces, deepening inequity over time without external intervention to break the loop.",
            "feedback_incorrect": "Incorrect. This is a positive (reinforcing) feedback loop, not self-correcting. Each consequence amplifies the next: pollution harms health, which limits economic opportunity, which reduces political power, which permits more pollution. Without external intervention to break the cycle, inequity deepens over time."
        },
        {
            "question": "A student's model shows that equalizing regulatory enforcement across all communities reduces ongoing violations but does not significantly reduce pollution exposure disparities. What does this reveal about the limitations of enforcement-only approaches?",
            "choices": {
                "A": "Enforcement is completely ineffective and should be abandoned",
                "B": "Equal enforcement addresses ongoing violations but does not relocate existing pollution sources, clean up historical contamination, or change the underlying power dynamics that created the inequity",
                "C": "Enforcement is the only intervention needed to achieve environmental justice",
                "D": "Pollution exposure is determined entirely by individual behavior, not facility location"
            },
            "correct": "B",
            "feedback_correct": "Correct. Equal enforcement is necessary but insufficient. It can reduce ongoing violations but cannot undo the physical reality of concentrated pollution sources, accumulated contamination in soil and water, or the structural power imbalances that allowed the concentration in the first place. Comprehensive justice requires addressing all these layers.",
            "feedback_incorrect": "Incorrect. The model shows that enforcement alone cannot achieve environmental justice because it addresses only one layer of a multi-layered problem. Existing facilities remain, historical contamination persists, and the power imbalances that created the inequity continue to operate. A comprehensive approach must address all these structural factors."
        },
        {
            "question": "The model identifies community political power as the strongest leverage point for reducing environmental inequity. What mechanism makes empowered communities more effective at improving their environmental conditions?",
            "choices": {
                "A": "Empowered communities can physically remove pollution sources by force",
                "B": "Communities with genuine decision-making authority can prevent new pollution siting, demand enforcement of existing regulations, influence zoning policy, and hold polluters accountable, breaking the feedback loop at its most effective point",
                "C": "Political power allows communities to ignore environmental regulations",
                "D": "Empowered communities can relocate to less polluted areas"
            },
            "correct": "B",
            "feedback_correct": "Correct. Community political power is the most effective leverage point because it addresses the root cause of environmental inequity: unequal decision-making authority. When communities have genuine power over facility siting, zoning, and enforcement, they can prevent new pollution, demand accountability, and break the reinforcing cycle that perpetuates inequity.",
            "feedback_incorrect": "Incorrect. Community empowerment works by giving affected populations genuine authority over the decisions that shape their environment. This means influence over facility siting, zoning policy, enforcement priorities, and cleanup timelines. By addressing the power imbalance at the root of environmental inequity, empowerment breaks the feedback loop at its most effective point."
        },
        {
            "question": "A student's model shows that comprehensive intervention (pollution reduction + equal enforcement + community empowerment + green infrastructure) produces dramatically larger improvements than any single intervention. What systems principle explains this finding?",
            "choices": {
                "A": "Adding more interventions always produces linearly additive results",
                "B": "Multiple interventions targeting different feedback loops simultaneously produce synergistic effects because they break reinforcing cycles at multiple points, preventing any single loop from maintaining the status quo",
                "C": "Comprehensive interventions are always more expensive and therefore more effective",
                "D": "The model is biased toward showing positive results for comprehensive approaches"
            },
            "correct": "B",
            "feedback_correct": "Correct. Environmental inequity is maintained by multiple interconnected feedback loops. A single intervention breaks one loop but the others can maintain the status quo. Comprehensive interventions break multiple loops simultaneously, producing synergistic effects where the combined impact exceeds the sum of individual interventions because no remaining loop can sustain the inequity.",
            "feedback_incorrect": "Incorrect. The synergistic effect results from addressing multiple feedback loops simultaneously. When environmental inequity is maintained by several reinforcing cycles, breaking only one leaves others to perpetuate the pattern. Comprehensive intervention disrupts all major feedback loops at once, preventing any remaining cycle from maintaining the status quo."
        },
        {
            "question": "Based on model evidence, a city council must allocate $50 million for environmental justice improvements in an overburdened community. Which allocation strategy is most strongly supported by the model's findings about systemic drivers?",
            "choices": {
                "A": "Spend all $50 million on air quality monitoring equipment to document pollution levels",
                "B": "Distribute funds across pollution source reduction, community health infrastructure, green space development, community organizing support, and environmental legal resources, addressing multiple feedback loops simultaneously",
                "C": "Use all funds for a single large park, which will solve environmental justice concerns",
                "D": "Return the money to the general fund because environmental inequity cannot be addressed through investment"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that comprehensive approaches targeting multiple feedback loops produce the largest improvements. Distributing investment across pollution reduction (addressing the environmental burden), health infrastructure (addressing health impacts), green space (providing environmental benefits), and community empowerment (breaking the power imbalance) creates synergistic effects that no single investment can match.",
            "feedback_incorrect": "Incorrect. Model evidence shows that environmental inequity is maintained by multiple reinforcing feedback loops. Only a distributed investment strategy that addresses pollution sources, health consequences, missing environmental benefits, and community decision-making power can break enough loops simultaneously to produce meaningful systemic change."
        }
    ]
}

ALL_QUESTIONS = {
    "G12L2-L01": L01_QUESTIONS,
    "G12L2-L02": L02_QUESTIONS,
    "G12L2-L03": L03_QUESTIONS,
    "G12L2-L04": L04_QUESTIONS,
    "G12L2-L05": L05_QUESTIONS,
    "G12L2-L06": L06_QUESTIONS,
    "G12L2-L07": L07_QUESTIONS,
    "G12L2-L08": L08_QUESTIONS,
    "G12L2-L09": L09_QUESTIONS,
    "G12L2-L10": L10_QUESTIONS,
}
