#!/usr/bin/env python3
"""Multiple choice pre/post assessment questions for Grade 10 Level 2 ModelIt! Lessons
Grade 10 Level 2: Systems Under Pressure
Aligned to HS NGSS standards. CAST-exam-style rigor with analysis, evaluation, and application."""

# =============================================================================
# L01: Why Is Lithium the New Gold?
# NGSS: HS-ESS3-1, HS-PS1-3
# =============================================================================
L01_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Which property of lithium makes it particularly valuable for use in rechargeable batteries compared to other metals?",
            "choices": {
                "A": "It is the lightest metal with a high electrochemical potential, enabling energy-dense batteries",
                "B": "It is the most abundant metal in Earth's crust, making it inexpensive to mine",
                "C": "It is the hardest metal available, making batteries more durable",
                "D": "It has the highest melting point of all metals, preventing battery overheating"
            },
            "correct": "A",
            "feedback_correct": "Correct. Lithium's low atomic mass and high electrochemical potential allow batteries to store large amounts of energy relative to their weight, which is critical for electric vehicles and portable electronics.",
            "feedback_incorrect": "Lithium is actually quite scarce and soft. Its value comes from being the lightest metal with a high electrochemical potential, which enables energy-dense batteries ideal for EVs and electronics."
        },
        {
            "question": "A country holds 60% of the world's known lithium reserves. Which term best describes the type of risk this concentration creates for global EV manufacturers?",
            "choices": {
                "A": "Environmental risk from mining pollution",
                "B": "Supply chain risk from geopolitical concentration",
                "C": "Technological risk from outdated extraction methods",
                "D": "Financial risk from currency fluctuations"
            },
            "correct": "B",
            "feedback_correct": "Correct. When a critical resource is concentrated in a few locations, political instability, trade disputes, or export restrictions in those regions can disrupt the entire global supply chain.",
            "feedback_incorrect": "While environmental and financial risks exist, the primary concern when reserves are geographically concentrated is supply chain vulnerability to geopolitical disruption, trade restrictions, or political instability in those regions."
        },
        {
            "question": "In a linear economy model, what happens to the lithium in a battery at the end of the product's useful life?",
            "choices": {
                "A": "It is recovered and refined for use in new batteries",
                "B": "It is disposed of as waste in landfills or storage facilities",
                "C": "It naturally decomposes and returns to the environment harmlessly",
                "D": "It is converted into a different element through chemical reactions"
            },
            "correct": "B",
            "feedback_correct": "Correct. In a linear economy (extract-use-dispose), materials are discarded after use rather than recovered, leading to resource waste and environmental contamination.",
            "feedback_incorrect": "In a linear economy, the model is extract-use-dispose. Unlike a circular economy where materials are recovered and reused, a linear model sends end-of-life products to landfills or waste storage."
        },
        {
            "question": "Which factor most limits how quickly the global lithium supply can increase in response to rising demand?",
            "choices": {
                "A": "The speed at which electric vehicles can be manufactured",
                "B": "The time required to discover, permit, and develop new mining operations",
                "C": "The cost of transporting lithium from mines to battery factories",
                "D": "The number of scientists researching lithium chemistry"
            },
            "correct": "B",
            "feedback_correct": "Correct. New lithium mines typically require 7-10 years from discovery through permitting to production, creating a significant lag between demand signals and supply responses.",
            "feedback_incorrect": "The primary bottleneck is development time. New lithium mines take 7-10 years to bring online due to exploration, environmental assessment, permitting, and construction, creating a fundamental supply lag."
        },
        {
            "question": "A student claims that switching entirely to electric vehicles will have no negative environmental consequences. Which evidence would best challenge this claim?",
            "choices": {
                "A": "Electric vehicles produce tailpipe emissions when driven at high speeds",
                "B": "Lithium extraction from brine pools consumes massive quantities of water in arid regions",
                "C": "Electric vehicle batteries last forever and never need replacement",
                "D": "Lithium is a renewable resource that replenishes naturally over time"
            },
            "correct": "B",
            "feedback_correct": "Correct. Lithium brine extraction requires pumping underground saltwater into evaporation ponds in some of the world's driest regions, consuming enormous amounts of water and impacting local ecosystems and communities.",
            "feedback_incorrect": "EVs produce zero tailpipe emissions and batteries do degrade over time. The strongest counterargument is that lithium extraction itself causes significant environmental harm, particularly through massive water consumption in arid mining regions."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the lithium supply chain model, when EV Adoption surges but Mining Rate remains flat, which outcome does the model predict?",
            "choices": {
                "A": "Market Price decreases because competition among miners increases supply",
                "B": "Market Price spikes because demand outpaces supply, and Environmental Damage increases as existing mines intensify operations",
                "C": "Recycling Rate automatically increases to fill the supply gap without any investment",
                "D": "Battery Performance improves immediately to reduce the amount of lithium needed per vehicle"
            },
            "correct": "B",
            "feedback_correct": "Correct. When demand exceeds supply, market prices spike. This price pressure also pushes existing mines to expand and intensify operations, increasing environmental damage in mining regions.",
            "feedback_incorrect": "In the model, when demand surges but supply is constrained, prices spike due to scarcity. Recycling and battery improvements require deliberate investment and time; they do not automatically compensate for supply shortfalls."
        },
        {
            "question": "The model reveals that high Market Price triggers investment in both new mining operations AND recycling infrastructure. Why does the model show recycling scaling faster than mining?",
            "choices": {
                "A": "Recycling produces higher-quality lithium than mining does",
                "B": "Recycling facilities can be built in 2-3 years while new mines take 7-10 years to develop",
                "C": "Recycling requires no energy input, making it instantly profitable",
                "D": "Governments ban new mining whenever prices rise above a threshold"
            },
            "correct": "B",
            "feedback_correct": "Correct. Recycling infrastructure has a much shorter development timeline than new mining operations, allowing it to respond to price signals and supply shortages more rapidly.",
            "feedback_incorrect": "The key difference is timescale. Recycling facilities can be built in a few years, while new mines require 7-10 years for discovery, permitting, and development. This makes recycling a faster response to supply gaps."
        },
        {
            "question": "A student runs the 'Circular Economy Transition' scenario with 90% Recycling Rate and moderate EV Adoption. Which system-level outcome best explains why this scenario stabilizes the lithium supply?",
            "choices": {
                "A": "High recycling eliminates the need for any new mining, allowing all mines to close permanently",
                "B": "Recycled lithium reduces pressure on new mining, moderates Market Price swings, and decreases Environmental Damage from extraction",
                "C": "The circular economy makes lithium worthless, so no one invests in EVs anymore",
                "D": "Recycling converts lithium into a different element that works better in batteries"
            },
            "correct": "B",
            "feedback_correct": "Correct. A circular economy reduces but does not eliminate mining demand. By recovering lithium from spent batteries, the system reduces price volatility, decreases extraction pressure, and mitigates environmental damage.",
            "feedback_incorrect": "A circular economy does not eliminate mining entirely or change lithium's chemistry. It stabilizes the system by reducing the fraction of demand that must be met through new extraction, moderating prices and environmental impact."
        },
        {
            "question": "The model demonstrates a 'supply-demand-environment trilemma' in the lithium economy. Which combination of strategies does the model show as the only viable resolution?",
            "choices": {
                "A": "Maximizing mining output regardless of environmental consequences",
                "B": "Banning electric vehicles until lithium supplies recover",
                "C": "Improving Battery Performance to use less lithium per vehicle AND scaling Recycling Rate to recover lithium from spent batteries",
                "D": "Switching all vehicles to hydrogen fuel cells within five years"
            },
            "correct": "C",
            "feedback_correct": "Correct. The model shows that the only sustainable path resolves all three tensions simultaneously: reducing lithium per vehicle through better battery chemistry and recovering lithium through high recycling rates.",
            "feedback_incorrect": "The model shows that neither pure supply-side (more mining) nor demand-side (fewer EVs) approaches solve the trilemma. Only combining reduced lithium requirements (better batteries) with high recycling rates addresses supply, demand, and environment simultaneously."
        },
        {
            "question": "Based on the model's feedback loops, which statement best explains why the lithium economy exhibits extreme price volatility?",
            "choices": {
                "A": "Lithium prices are set by a single government and change unpredictably",
                "B": "Demand responds rapidly to policy changes (months), but supply responds slowly to price signals (years to decades), creating persistent mismatches",
                "C": "Lithium quality varies so much between mines that pricing is arbitrary",
                "D": "Consumers hoard lithium during shortages, creating artificial scarcity"
            },
            "correct": "B",
            "feedback_correct": "Correct. The fundamental source of volatility is the time asymmetry between demand and supply responses. EV adoption and policy can shift demand in months, but new mining capacity takes 7-10 years to come online.",
            "feedback_incorrect": "Price volatility in the lithium market stems from a temporal mismatch: demand can shift rapidly with policy changes and consumer behavior, while supply adjustments require years to decades for new mining development."
        }
    ]
}

# =============================================================================
# L02: How Do Stars Forge Every Atom in Your Body?
# NGSS: HS-ESS1-3, HS-PS1-5
# =============================================================================
L02_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Which process is the primary source of energy that powers stars during their main-sequence lifetime?",
            "choices": {
                "A": "Chemical combustion of hydrogen gas in the presence of oxygen",
                "B": "Nuclear fusion, where lighter nuclei combine to form heavier nuclei and release energy",
                "C": "Nuclear fission, where heavy nuclei split into smaller fragments",
                "D": "Gravitational potential energy from the star slowly contracting over time"
            },
            "correct": "B",
            "feedback_correct": "Correct. Stars are powered by nuclear fusion, primarily fusing hydrogen into helium in their cores at temperatures exceeding 10 million Kelvin.",
            "feedback_incorrect": "Stars are not powered by chemical combustion (there is no oxygen in stellar cores for burning) or fission. Nuclear fusion, the combining of lighter nuclei into heavier ones, is the energy source that powers main-sequence stars."
        },
        {
            "question": "The Big Bang produced primarily hydrogen and helium. Based on this information, where did heavier elements like carbon, oxygen, and iron originate?",
            "choices": {
                "A": "They were created during the formation of the solar system from cosmic dust",
                "B": "They formed through nuclear reactions in the cores of stars and were dispersed when those stars died",
                "C": "They were always present in the universe since its beginning",
                "D": "They formed spontaneously in the vacuum of interstellar space over billions of years"
            },
            "correct": "B",
            "feedback_correct": "Correct. Elements heavier than helium were synthesized through nuclear fusion in stellar cores and released into space through stellar winds and supernova explosions.",
            "feedback_incorrect": "Since the Big Bang only produced hydrogen and helium (with trace lithium), all heavier elements had to be created later. Stars forge these elements through nuclear fusion in their cores and scatter them into space when they die."
        },
        {
            "question": "Two stars form at the same time from the same nebula, but Star A has 20 times more mass than Star B. Which prediction about their lifespans is most scientifically supported?",
            "choices": {
                "A": "Star A will live longer because it has more hydrogen fuel to burn",
                "B": "Star A will have a shorter lifespan because its greater mass drives faster fusion rates",
                "C": "Both stars will have identical lifespans because they formed from the same material",
                "D": "Star B will explode first because smaller stars are less stable"
            },
            "correct": "B",
            "feedback_correct": "Correct. More massive stars have stronger gravitational compression, which drives higher core temperatures and much faster fusion rates. They burn through their fuel far more quickly despite having more of it.",
            "feedback_incorrect": "Counterintuitively, more massive stars live shorter lives. Their greater gravitational pressure creates much higher core temperatures, driving fusion at enormously faster rates. A star 20 times the Sun's mass may live only millions of years versus billions."
        },
        {
            "question": "What force counterbalances gravity to prevent a main-sequence star from collapsing under its own mass?",
            "choices": {
                "A": "Magnetic field pressure from the star's iron core",
                "B": "Outward radiation pressure generated by nuclear fusion reactions in the core",
                "C": "Centrifugal force from the star's rapid rotation",
                "D": "Repulsive electrical forces between hydrogen atoms at the surface"
            },
            "correct": "B",
            "feedback_correct": "Correct. The outward pressure from fusion-generated radiation balances the inward pull of gravity, maintaining hydrostatic equilibrium throughout the star's main-sequence life.",
            "feedback_incorrect": "A star maintains stability through hydrostatic equilibrium: the outward radiation pressure from nuclear fusion in the core exactly balances the inward gravitational force trying to collapse the star."
        },
        {
            "question": "Iron is the heaviest element that can be produced through energy-releasing nuclear fusion in a stellar core. What happens when a massive star's core becomes dominated by iron?",
            "choices": {
                "A": "The star enters a new, more powerful phase of fusion that creates elements heavier than iron",
                "B": "Iron fusion absorbs energy rather than releasing it, removing the radiation pressure that supports the star against gravitational collapse",
                "C": "The iron core cools and solidifies, turning the star into a cold, dark object",
                "D": "Iron nuclei repel each other, causing the star to expand into a nebula"
            },
            "correct": "B",
            "feedback_correct": "Correct. Iron has the highest binding energy per nucleon, so fusing iron absorbs energy instead of releasing it. This removes the outward radiation pressure, leading to catastrophic core collapse.",
            "feedback_incorrect": "Iron-56 has the maximum binding energy per nucleon, making it the endpoint of energy-releasing fusion. Attempting to fuse iron absorbs energy, removing the radiation support against gravity and triggering core collapse."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the stellar nucleosynthesis model, what does the relationship between Gravitational Pressure and Stellar Core Temperature demonstrate about element production?",
            "choices": {
                "A": "Higher gravitational pressure decreases core temperature, slowing element production",
                "B": "Gravitational pressure compresses the core, raising temperature to thresholds that ignite successively heavier fusion stages",
                "C": "Gravitational pressure has no effect on which elements a star can produce",
                "D": "All stars reach the same core temperature regardless of their gravitational pressure"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that gravitational pressure is the master variable: it compresses and heats the core, and each new fusion stage (hydrogen, helium, carbon, etc.) requires progressively higher temperature thresholds.",
            "feedback_incorrect": "In the model, Gravitational Pressure drives everything. Greater mass means greater compression, higher core temperatures, and the ability to ignite heavier fusion stages. This is why only massive stars can produce elements up to iron."
        },
        {
            "question": "A student compares the model results for a Sun-like star (1 solar mass) and a massive star (20 solar masses). Which comparison correctly describes the model's predictions?",
            "choices": {
                "A": "The Sun-like star produces elements up to iron and ends as a neutron star",
                "B": "The massive star produces only hydrogen and helium but lives 100 times longer",
                "C": "The massive star produces elements up to iron and ends in a supernova, while the Sun-like star produces elements up to carbon/oxygen and ends as a white dwarf",
                "D": "Both stars produce the same elements but at different rates"
            },
            "correct": "C",
            "feedback_correct": "Correct. The model demonstrates that stellar mass determines both the range of elements produced and the star's fate. Massive stars reach iron and explode; Sun-like stars stop at carbon/oxygen and shed their outer layers.",
            "feedback_incorrect": "The model clearly shows mass-dependent outcomes. A 20-solar-mass star achieves temperatures high enough to fuse elements all the way to iron before collapsing in a supernova, while a Sun-like star stops at carbon/oxygen and becomes a white dwarf."
        },
        {
            "question": "The model shows that each successive fusion stage in a massive star releases less energy and lasts a shorter time. Why does this pattern inevitably lead to core collapse?",
            "choices": {
                "A": "The star runs out of gravitational potential energy and stops contracting",
                "B": "Each stage produces less radiation pressure to resist gravity while requiring higher temperatures, accelerating the star toward the iron endpoint where fusion absorbs rather than releases energy",
                "C": "The star loses mass through stellar wind until gravity can no longer hold it together",
                "D": "The accumulation of heavy elements makes the star spin faster until it flies apart"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals a countdown: each fusion stage is less efficient and shorter-lived, providing diminishing radiation support against gravity, until iron is reached and fusion can no longer sustain the star.",
            "feedback_incorrect": "The model shows an accelerating progression: hydrogen fusion lasts millions of years, helium fusion thousands, carbon fusion centuries, down to silicon fusion lasting mere days. Each stage supports the star less effectively until iron ends energy-releasing fusion entirely."
        },
        {
            "question": "Based on the model, why are supernova explosions essential for the existence of life on Earth?",
            "choices": {
                "A": "Supernovae create the heat necessary to warm planets in newly forming solar systems",
                "B": "Supernovae disperse heavy elements (carbon, oxygen, iron, and elements heavier than iron) into space, providing the raw materials for rocky planets and biological molecules",
                "C": "Supernovae create black holes that stabilize the orbits of nearby planets",
                "D": "Supernovae produce the dark matter that holds galaxies together"
            },
            "correct": "B",
            "feedback_correct": "Correct. Without supernovae, heavy elements would remain locked in stellar cores. Supernova explosions both create elements heavier than iron (through the r-process) and scatter all heavy elements into interstellar space for incorporation into new stars and planets.",
            "feedback_incorrect": "The model demonstrates that supernovae serve a dual purpose: they create elements heavier than iron through rapid neutron capture, and they disperse all the heavy elements forged during the star's life into space, seeding future planetary systems."
        },
        {
            "question": "A student claims that the elements in the human body could have come from a single star. Using evidence from the model, which response best evaluates this claim?",
            "choices": {
                "A": "The claim is correct because one massive star can produce all elements through iron",
                "B": "The claim is incorrect because the human body contains elements heavier than iron, which require supernova nucleosynthesis, and different elements were produced by stars of different masses across multiple stellar generations",
                "C": "The claim is correct because all elements were produced during the Big Bang",
                "D": "The claim is incorrect because human body elements come from chemical reactions on Earth, not from stars"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that different mass stars produce different element ranges, and elements heavier than iron require the extreme conditions of supernovae. The atoms in your body represent the contributions of multiple stellar generations.",
            "feedback_incorrect": "The model reveals that our bodies require elements from multiple stellar sources: hydrogen from the Big Bang, carbon and oxygen from medium-mass stars, iron from massive stars, and elements like iodine and zinc from supernova explosions."
        }
    ]
}

# =============================================================================
# L03: The Carbon Bomb: Why Thawing Permafrost Terrifies Scientists
# NGSS: HS-ESS2-6, HS-LS2-3
# =============================================================================
L03_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Permafrost is ground that has remained frozen for at least two consecutive years. Approximately what fraction of the Northern Hemisphere's land surface is covered by permafrost?",
            "choices": {
                "A": "About 1% of the Northern Hemisphere's land surface",
                "B": "About 10% of the Northern Hemisphere's land surface",
                "C": "About 25% of the Northern Hemisphere's land surface",
                "D": "About 75% of the Northern Hemisphere's land surface"
            },
            "correct": "C",
            "feedback_correct": "Correct. Approximately 25% of the Northern Hemisphere's land surface is underlain by permafrost, storing an estimated 1,500 billion tons of organic carbon.",
            "feedback_incorrect": "Permafrost covers approximately 25% of the Northern Hemisphere's land surface, spanning vast areas of Siberia, Canada, and Alaska. This enormous area stores roughly 1,500 billion tons of organic carbon."
        },
        {
            "question": "A scientist states that methane is a more potent greenhouse gas than carbon dioxide. Which comparison best supports this claim?",
            "choices": {
                "A": "Methane is produced in larger quantities than CO2 from industrial sources",
                "B": "Methane traps approximately 80 times more heat than CO2 over a 20-year period per molecule",
                "C": "Methane remains in the atmosphere for thousands of years while CO2 breaks down quickly",
                "D": "Methane absorbs visible light while CO2 only absorbs ultraviolet light"
            },
            "correct": "B",
            "feedback_correct": "Correct. While methane has a shorter atmospheric lifetime than CO2, its heat-trapping capacity is approximately 80 times greater over a 20-year period, making it an extremely potent greenhouse gas.",
            "feedback_incorrect": "Methane is more potent per molecule because it traps approximately 80 times more heat than CO2 over a 20-year period. However, methane has a shorter atmospheric lifetime (about 12 years) compared to CO2 (hundreds of years)."
        },
        {
            "question": "In a positive feedback loop, how does the output of a process relate to its input?",
            "choices": {
                "A": "The output counteracts the input, stabilizing the system",
                "B": "The output amplifies the input, causing the process to accelerate",
                "C": "The output has no relationship to the input",
                "D": "The output always decreases the input over time"
            },
            "correct": "B",
            "feedback_correct": "Correct. In a positive feedback loop, the output reinforces the original input, creating a self-amplifying cycle. This does not mean the outcome is 'positive' or beneficial; it means the change accelerates.",
            "feedback_incorrect": "A positive feedback loop is self-amplifying: the output of a process reinforces its own input, causing acceleration. The word 'positive' refers to amplification, not to whether the outcome is good or bad."
        },
        {
            "question": "Which process is primarily responsible for converting dead organic matter into CO2 and methane in thawed soil?",
            "choices": {
                "A": "Photosynthesis by newly established plants",
                "B": "Volcanic outgassing from geothermal activity",
                "C": "Microbial decomposition by bacteria and fungi",
                "D": "Chemical weathering of exposed rock surfaces"
            },
            "correct": "C",
            "feedback_correct": "Correct. When permafrost thaws, dormant microorganisms (bacteria and archaea) reactivate and begin decomposing the ancient organic carbon, producing CO2 in aerobic conditions and methane in anaerobic conditions.",
            "feedback_incorrect": "Microbial decomposition is the primary process. When frozen ground thaws, soil microorganisms awaken from dormancy and begin metabolizing organic matter that has been frozen for thousands of years, releasing CO2 and methane."
        },
        {
            "question": "A tipping point in an environmental system is best described as which of the following?",
            "choices": {
                "A": "The point at which pollution levels begin to affect human health",
                "B": "A critical threshold beyond which a system shifts rapidly and potentially irreversibly to a new state",
                "C": "The maximum temperature any ecosystem can tolerate before all organisms die",
                "D": "The moment when government policy reverses an environmental trend"
            },
            "correct": "B",
            "feedback_correct": "Correct. A tipping point is a threshold where small additional changes trigger a large, often irreversible shift in the system's behavior, moving it to a fundamentally different state.",
            "feedback_incorrect": "A tipping point is a critical threshold in a system. Once crossed, the system undergoes a rapid, self-reinforcing shift to a new state that may be irreversible on human timescales, regardless of subsequent interventions."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the permafrost carbon feedback model, which sequence correctly describes the positive feedback loop that drives accelerating warming?",
            "choices": {
                "A": "Atmospheric CO2 rises -> Permafrost Temperature increases -> Microbial Decomposition releases greenhouse gases -> Atmospheric CO2 rises further",
                "B": "Ocean Absorption increases -> Permafrost Temperature drops -> Vegetation Growth expands -> Atmospheric CO2 drops",
                "C": "Vegetation Growth increases -> Methane Release Rate decreases -> Permafrost Temperature decreases -> Feedback Amplification stops",
                "D": "Atmospheric CO2 rises -> Ocean Absorption increases -> Permafrost Temperature decreases -> Methane Release Rate stops"
            },
            "correct": "A",
            "feedback_correct": "Correct. The model demonstrates a self-amplifying cycle: rising CO2 warms the atmosphere, thawing permafrost, activating microbes that release more greenhouse gases, further increasing atmospheric CO2.",
            "feedback_incorrect": "The positive feedback loop in the model follows a clear causal chain: atmospheric CO2 raises temperature, which thaws permafrost, which activates microbial decomposition of ancient carbon, which releases more CO2 and methane, which raises temperature further."
        },
        {
            "question": "The model includes Ocean Absorption and Vegetation Growth as components. What role do these play in the permafrost feedback system?",
            "choices": {
                "A": "They amplify the positive feedback loop, making warming faster",
                "B": "They act as negative feedbacks that slow the warming cycle but cannot stop it if the tipping point is crossed",
                "C": "They have no measurable effect on the permafrost carbon cycle",
                "D": "They completely offset all carbon released from thawing permafrost"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that Ocean Absorption and Vegetation Growth provide negative feedback (slowing the cycle), but the volume of carbon stored in permafrost vastly exceeds what these sinks can absorb, especially after the tipping point.",
            "feedback_incorrect": "These components act as partial brakes on the system. They absorb some CO2, slowing the feedback loop, but the 1,500 billion tons of carbon in permafrost overwhelms their capacity, particularly once Feedback Amplification becomes self-sustaining."
        },
        {
            "question": "A student runs the model with Atmospheric CO2 increasing at current rates and observes Feedback Amplification becoming self-sustaining. What does 'self-sustaining' mean in this context?",
            "choices": {
                "A": "Human emissions are the only driver of further warming",
                "B": "Permafrost carbon release would continue even if all human CO2 emissions stopped immediately",
                "C": "The feedback will reverse naturally within a few decades",
                "D": "Vegetation Growth will eventually absorb all released carbon"
            },
            "correct": "B",
            "feedback_correct": "Correct. Once the feedback becomes self-sustaining, the system generates enough warming from its own carbon releases to continue thawing more permafrost, independent of human emissions. This is what makes the tipping point so dangerous.",
            "feedback_incorrect": "A self-sustaining feedback means the process no longer requires an external driver. The warming from permafrost carbon release alone is sufficient to thaw more permafrost, creating an autonomous cycle that persists even if human emissions cease entirely."
        },
        {
            "question": "The model compares the 1,500 billion tons of carbon in permafrost to the approximately 900 billion tons currently in the atmosphere. Why does this comparison alarm climate scientists?",
            "choices": {
                "A": "Because permafrost carbon is less harmful than atmospheric carbon",
                "B": "Because releasing even a fraction of permafrost carbon could nearly double atmospheric CO2, overwhelming natural sinks and accelerating warming beyond current projections",
                "C": "Because all of the permafrost carbon will be released within one year of thawing",
                "D": "Because permafrost carbon is composed of a different isotope that traps less heat"
            },
            "correct": "B",
            "feedback_correct": "Correct. With nearly twice as much carbon stored in permafrost as exists in the entire atmosphere, even partial release represents an enormous addition to atmospheric greenhouse gases that current climate models may underestimate.",
            "feedback_incorrect": "The sheer scale is the concern: permafrost holds approximately 1.7 times more carbon than the entire atmosphere. Its release over decades rather than millennia would overwhelm Earth's carbon sinks and push warming far beyond current projections."
        },
        {
            "question": "Based on the model, which intervention strategy would be most effective at preventing the permafrost feedback from reaching the tipping point?",
            "choices": {
                "A": "Increasing Ocean Absorption by fertilizing the oceans with iron",
                "B": "Reducing Atmospheric CO2 emissions rapidly enough to keep Permafrost Temperature below thawing thresholds before the feedback becomes self-sustaining",
                "C": "Planting trees on top of permafrost to shade it from the sun",
                "D": "Pumping cold water underground to refreeze thawed permafrost"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that the only realistic prevention strategy is reducing global emissions fast enough to limit warming before permafrost thaw crosses the self-sustaining threshold. Once crossed, no practical intervention can reverse the feedback.",
            "feedback_incorrect": "The model reveals that the window for action is before the tipping point. Once the feedback becomes self-sustaining, it is practically irreversible. Only rapid reduction of atmospheric CO2 emissions can keep Permafrost Temperature below critical thresholds."
        }
    ]
}

# =============================================================================
# L04: Can We Engineer the Amazon Back to Life?
# NGSS: HS-LS2-7, HS-ESS2-7
# =============================================================================
L04_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "The Amazon rainforest generates approximately what percentage of its own rainfall through evapotranspiration?",
            "choices": {
                "A": "About 5% of its rainfall",
                "B": "About 25% of its rainfall",
                "C": "About 50% of its rainfall",
                "D": "About 95% of its rainfall"
            },
            "correct": "C",
            "feedback_correct": "Correct. The Amazon generates approximately 50% of its own rainfall through evapotranspiration, where trees release water vapor that forms clouds and falls as rain downwind, creating a self-sustaining moisture recycling system.",
            "feedback_incorrect": "The Amazon's hydrological cycle is remarkably self-sustaining: approximately 50% of the rainfall in the Amazon basin is recycled moisture generated by the forest's own evapotranspiration."
        },
        {
            "question": "Ecological succession describes the process by which ecosystems recover after disturbance. Which characteristic of tropical rainforest succession makes restoration particularly challenging?",
            "choices": {
                "A": "Tropical trees grow faster than any other vegetation type",
                "B": "Mature tropical forest requires complex soil fungal networks and biodiversity that take decades to centuries to re-establish",
                "C": "Tropical rainforests can only grow in volcanic soil",
                "D": "Tropical trees do not reproduce through seeds, making replanting impossible"
            },
            "correct": "B",
            "feedback_correct": "Correct. Tropical rainforest recovery requires not just trees but the re-establishment of mycorrhizal fungal networks, nutrient cycling, and complex species interactions that develop over very long timescales.",
            "feedback_incorrect": "Rainforest restoration is far more than planting trees. Mature forest depends on complex underground fungal networks (mycorrhizae), soil nutrient cycling, and interdependent species relationships that require 15-50+ years to develop."
        },
        {
            "question": "Carbon sequestration refers to the process by which growing forests remove CO2 from the atmosphere. What is the primary mechanism by which trees sequester carbon?",
            "choices": {
                "A": "Trees filter carbon particles from the air through their bark",
                "B": "Trees absorb CO2 through photosynthesis and store it as biomass in wood, roots, and leaves",
                "C": "Trees convert CO2 into oxygen, and the carbon disappears",
                "D": "Trees push carbon underground through their roots into bedrock"
            },
            "correct": "B",
            "feedback_correct": "Correct. Through photosynthesis, trees absorb atmospheric CO2 and convert it into organic carbon compounds stored in their biomass, including trunks, branches, roots, and leaves.",
            "feedback_incorrect": "Trees sequester carbon through photosynthesis, converting atmospheric CO2 into organic molecules that become wood, roots, and leaves. The carbon is stored as biomass for the life of the tree, not destroyed or eliminated."
        },
        {
            "question": "Which human activity is the primary driver of Amazon deforestation?",
            "choices": {
                "A": "Urban expansion of major cities into forest areas",
                "B": "Cattle ranching and soybean farming clearing forest for agricultural land",
                "C": "Highway construction connecting remote communities",
                "D": "Tourism infrastructure development in protected areas"
            },
            "correct": "B",
            "feedback_correct": "Correct. Cattle ranching is the single largest driver of Amazon deforestation, followed by soybean farming. Together, these agricultural activities account for the majority of forest clearing.",
            "feedback_incorrect": "Agricultural expansion is the dominant driver. Cattle ranching alone accounts for approximately 80% of Amazon deforestation, with soybean cultivation contributing an additional significant share."
        },
        {
            "question": "What is a tipping point threshold in the context of Amazon deforestation?",
            "choices": {
                "A": "The number of tree species that must be present for a forest to be classified as a rainforest",
                "B": "The level of deforestation beyond which the forest can no longer sustain its own water cycle, leading to irreversible conversion to savanna",
                "C": "The annual rainfall amount needed to support tropical vegetation",
                "D": "The temperature at which tropical trees begin to lose their leaves seasonally"
            },
            "correct": "B",
            "feedback_correct": "Correct. The tipping point threshold for the Amazon is estimated at 20-25% total deforestation, beyond which the forest cannot generate enough moisture through evapotranspiration to sustain itself.",
            "feedback_incorrect": "The tipping point threshold refers to a critical deforestation level (estimated at 20-25% of total forest area) beyond which the Amazon's self-sustaining water cycle collapses, triggering irreversible conversion to drier savanna."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the Amazon restoration model, why does the Tipping Point Threshold approach even when Reforestation Effort matches Deforestation Rate?",
            "choices": {
                "A": "Because newly planted trees immediately provide the same ecological services as mature forest",
                "B": "Because Soil Nutrient Recovery and Water Cycle Restoration take decades, so replanted areas cannot compensate for mature forest functions during the recovery period",
                "C": "Because the model does not account for Reforestation Effort at all",
                "D": "Because climate change has no effect on the Amazon water cycle"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals a critical time lag: newly planted trees cannot generate the evapotranspiration, soil networks, or ecological complexity of mature forest for 15-50+ years, so matching replanting to clearing still leads to net functional loss.",
            "feedback_incorrect": "The model shows that reforestation is not simply replacing trees. Young replanted areas lack mature root systems, mycorrhizal networks, and evapotranspiration capacity. This 15-50 year recovery gap means functional forest area continues to decline."
        },
        {
            "question": "The model demonstrates that the Amazon's water cycle is a self-reinforcing system. Which feedback loop does the model reveal as most critical to forest survival?",
            "choices": {
                "A": "More forest -> more evapotranspiration -> more rainfall -> more forest growth (positive feedback supporting the ecosystem)",
                "B": "More forest -> more carbon emissions -> more global warming -> more forest growth",
                "C": "Less rainfall -> faster tree growth -> more water consumption -> less rainfall",
                "D": "More biodiversity -> less rainfall -> more deforestation -> less biodiversity"
            },
            "correct": "A",
            "feedback_correct": "Correct. The model shows that the Amazon's water cycle is a positive feedback loop where forest creates its own rain. This is also why deforestation is so dangerous: losing forest reduces rainfall, which kills more forest.",
            "feedback_incorrect": "The critical feedback loop is: forest generates moisture through evapotranspiration -> moisture forms rainfall -> rainfall supports forest growth. This self-reinforcing cycle means the forest sustains itself, but it also means losing forest triggers a death spiral."
        },
        {
            "question": "A student runs the model with 'Aggressive Restoration' settings: zero Deforestation Rate and maximum Reforestation Effort. The model shows full Biodiversity Return requires 100-200+ years. What does this reveal about ecosystem complexity?",
            "choices": {
                "A": "That Biodiversity Return is unrelated to forest age and depends only on planting density",
                "B": "That complex ecological relationships, specialist species colonization, and mature ecosystem functions require generations to re-establish, even under optimal conditions",
                "C": "That the model is inaccurate because trees grow to full maturity in 10 years",
                "D": "That Biodiversity Return can be accelerated to 5 years by introducing more species simultaneously"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that mature tropical forests are among the most complex ecosystems on Earth. Specialist species, intricate food webs, and symbiotic relationships cannot be manufactured quickly regardless of resources invested.",
            "feedback_incorrect": "The 100-200+ year timeline reflects the reality that tropical forest ecosystems involve thousands of interdependent species, complex soil communities, and ecological relationships that develop through natural succession, not by engineering."
        },
        {
            "question": "The model shows that approximately 17% of the Amazon has already been deforested, with the tipping point estimated at 20-25%. Based on the model's feedback dynamics, what makes the remaining margin so dangerous?",
            "choices": {
                "A": "The remaining forest is all in protected areas that cannot be deforested",
                "B": "As the tipping point approaches, each additional percentage of deforestation reduces rainfall more severely, creating accelerating feedback that pushes the system toward collapse faster",
                "C": "The 20-25% estimate is not supported by any scientific evidence",
                "D": "The remaining 3-8% margin represents only unproductive forest that has no economic value"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals non-linear dynamics near the tipping point: the water cycle feedback intensifies as forest cover decreases, meaning each additional loss has a proportionally greater impact than the previous one.",
            "feedback_incorrect": "The model shows that the approach to the tipping point is non-linear. As forest cover decreases, each additional loss has a disproportionately larger effect on the water cycle, creating accelerating feedback that can push the system past the threshold rapidly."
        },
        {
            "question": "Based on the model's evidence, which strategy is necessary to prevent the Amazon from crossing its tipping point?",
            "choices": {
                "A": "Reforestation alone is sufficient since trees can be planted faster than they are cut",
                "B": "Simultaneously halting deforestation AND investing in long-term reforestation with soil and water cycle recovery, because the model shows replanting without stopping clearing cannot overcome the functional recovery lag",
                "C": "Replacing the Amazon with fast-growing plantation forests that produce more wood",
                "D": "Allowing natural regeneration without any human intervention"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that both actions are required: stopping the loss and actively restoring what was lost, with the understanding that functional recovery takes decades and cannot be rushed.",
            "feedback_incorrect": "The model shows that neither stopping deforestation nor reforestation alone is sufficient. Both must happen simultaneously, and the restoration must include soil recovery, water cycle restoration, and patience for the decades-long recovery process."
        }
    ]
}

# =============================================================================
# L05: Why Did Dinosaurs Rule and Then Vanish?
# NGSS: HS-LS4-1, HS-LS4-4
# =============================================================================
L05_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Dinosaurs dominated Earth for approximately 165 million years. Which statement best describes the primary cause of their mass extinction approximately 66 million years ago?",
            "choices": {
                "A": "A gradual cooling trend over millions of years that slowly reduced their habitat",
                "B": "A catastrophic asteroid impact that caused rapid, global environmental changes exceeding their ability to adapt",
                "C": "Competition from early mammals that outcompeted dinosaurs for food resources",
                "D": "A series of volcanic eruptions that heated the planet beyond what dinosaurs could tolerate"
            },
            "correct": "B",
            "feedback_correct": "Correct. The Chicxulub asteroid impact triggered rapid global environmental changes including impact winter, acid rain, and food web collapse that overwhelmed the adaptive capacity of most dinosaur species.",
            "feedback_incorrect": "While volcanic activity (Deccan Traps) may have contributed to stress, the primary cause was the Chicxulub asteroid impact, which caused rapid environmental devastation that exceeded the dinosaurs' ability to adapt."
        },
        {
            "question": "After a mass extinction event, the fossil record shows a pattern called adaptive radiation. What does this term describe?",
            "choices": {
                "A": "The emission of radioactive energy from fossils over time",
                "B": "The rapid diversification of surviving species into newly vacant ecological niches",
                "C": "The gradual accumulation of harmful mutations after a catastrophe",
                "D": "The process by which predators radiate outward from their territory"
            },
            "correct": "B",
            "feedback_correct": "Correct. After mass extinctions create vacant niches, surviving lineages rapidly diversify to fill those opportunities, as seen in the mammalian radiation after the dinosaur extinction.",
            "feedback_incorrect": "Adaptive radiation is an evolutionary pattern where surviving species rapidly diversify to fill ecological niches left empty by extinct organisms. The mammalian diversification after the dinosaur extinction is a classic example."
        },
        {
            "question": "Natural selection acts on the variation within populations. During a period of rapid environmental change, which type of organisms are most likely to survive?",
            "choices": {
                "A": "The largest and most dominant predators in the ecosystem",
                "B": "Organisms with traits that happen to be advantageous in the new environmental conditions",
                "C": "The oldest individuals with the most experience in the ecosystem",
                "D": "Organisms that have remained unchanged for the longest evolutionary time"
            },
            "correct": "B",
            "feedback_correct": "Correct. Natural selection favors traits that are advantageous in the current environment, not traits that were advantageous before the change. Survival depends on having pre-existing variation that matches new conditions.",
            "feedback_incorrect": "Natural selection is blind to past success. What matters is which organisms possess traits that happen to be beneficial under the new conditions. This is why dominant species can go extinct while seemingly insignificant ones survive."
        },
        {
            "question": "Which factor most limits how quickly a population can evolve new traits in response to environmental change?",
            "choices": {
                "A": "The intelligence of individual organisms",
                "B": "Generation time and the amount of genetic variation available in the population",
                "C": "The physical size of the organisms",
                "D": "The temperature of the environment"
            },
            "correct": "B",
            "feedback_correct": "Correct. Evolutionary adaptation requires genetic variation to act on and reproduction to pass traits to offspring. Shorter generation times allow faster evolutionary responses because selection acts each generation.",
            "feedback_incorrect": "Adaptation speed is constrained by two key factors: the available genetic variation (the raw material for selection) and generation time (how quickly selected traits can spread through the population)."
        },
        {
            "question": "Some scientists describe the current era as a 'sixth mass extinction.' What evidence would support this classification?",
            "choices": {
                "A": "A few species have gone extinct in the past century",
                "B": "Current species extinction rates are estimated at 100-1,000 times higher than the natural background rate",
                "C": "The climate is warmer now than it was during the last ice age",
                "D": "Human population has grown rapidly in the past century"
            },
            "correct": "B",
            "feedback_correct": "Correct. The defining characteristic of a mass extinction is an extinction rate dramatically exceeding the background rate. Current estimates suggest species are disappearing 100-1,000 times faster than the natural baseline.",
            "feedback_incorrect": "A mass extinction is defined by extinction rates far exceeding background levels, typically eliminating 75%+ of species. Current rates are estimated at 100-1,000 times the natural background rate, which meets the threshold for mass extinction classification."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the extinction dynamics model, what happens when Environmental Change Rate exceeds Adaptation Speed?",
            "choices": {
                "A": "Species automatically develop mutations to cope with the change",
                "B": "Extinction Pressure increases because organisms cannot evolve traits matching new conditions fast enough, leading to population collapse",
                "C": "Species Diversity increases as new ecological niches are created",
                "D": "Niche Competition decreases as resources become more abundant"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that when environmental conditions change faster than populations can adapt, Extinction Pressure overwhelms Species Diversity and populations decline toward extinction.",
            "feedback_incorrect": "The model clearly shows that adaptation has a biological speed limit. When environmental change outpaces this limit, populations cannot evolve fast enough, Extinction Pressure rises, and extinction becomes inevitable regardless of previous fitness."
        },
        {
            "question": "The model reveals that during the asteroid impact scenario, Survival Advantage shifts dramatically. Which combination of traits does the model show as most important for surviving a mass extinction?",
            "choices": {
                "A": "Large body size, specialized diet, and high metabolic rate",
                "B": "Small body size, generalist diet, ability to enter torpor, and rapid reproduction",
                "C": "Aquatic lifestyle, cold-blooded metabolism, and long lifespan",
                "D": "Bright coloration, territorial behavior, and complex social structures"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that mass extinction reverses the competitive hierarchy: traits advantageous in stable environments (large size, specialization) become liabilities, while small size, dietary flexibility, and torpor become critical survival advantages.",
            "feedback_incorrect": "The model demonstrates a competitive reversal during mass extinction. Small body size requires less food, generalist diets allow flexibility when food webs collapse, torpor allows surviving periods of extreme conditions, and rapid reproduction enables faster recovery."
        },
        {
            "question": "In the model, the 'Gradual Climate Change' scenario shows a different extinction pattern than the 'Catastrophic Impact' scenario. What is the key difference?",
            "choices": {
                "A": "Gradual change causes no extinctions while catastrophic change causes total extinction",
                "B": "Gradual change allows Adaptation Speed to keep pace with Environmental Change Rate, enabling species turnover rather than mass extinction, while catastrophic change overwhelms all adaptation",
                "C": "Both scenarios produce identical extinction outcomes regardless of rate",
                "D": "Gradual change only affects plants while catastrophic change only affects animals"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that when environmental change is gradual, populations can evolve and species can be replaced through normal turnover. Catastrophic change overwhelms adaptation entirely, causing mass extinction.",
            "feedback_incorrect": "The critical variable is rate. The model shows that gradual change allows evolutionary adaptation to keep pace, enabling normal species turnover and niche competition. Catastrophic change exceeds all biological adaptation limits simultaneously."
        },
        {
            "question": "The model demonstrates that Population Recovery after mass extinction follows a predictable pattern. Which sequence does the model show?",
            "choices": {
                "A": "All species recover simultaneously and return to pre-extinction diversity immediately",
                "B": "Opportunistic generalist species colonize first, followed by gradual specialization and adaptive radiation into empty niches over millions of years",
                "C": "The exact same species that went extinct re-evolve from remaining populations",
                "D": "Recovery occurs only when a new asteroid impact creates fresh ecological opportunities"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows recovery beginning with generalist 'weedy' species, followed by increasing specialization as populations diversify to exploit available ecological niches through adaptive radiation.",
            "feedback_incorrect": "The model demonstrates predictable recovery stages: fast-reproducing generalists colonize first because they can exploit varied resources, then gradual specialization and adaptive radiation fill the empty niches over evolutionary timescales."
        },
        {
            "question": "A student uses the model to argue that the current human-caused biodiversity loss is comparable to past mass extinctions. Which model evidence most strongly supports this argument?",
            "choices": {
                "A": "The model shows that any species going extinct qualifies as a mass extinction",
                "B": "The model demonstrates that when Environmental Change Rate exceeds Adaptation Speed across multiple ecosystems simultaneously, the result mirrors mass extinction dynamics regardless of the cause of the change",
                "C": "The model proves that humans are more destructive than asteroid impacts",
                "D": "The model shows that only natural disasters can cause mass extinctions"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that mass extinction dynamics depend on the rate and scale of environmental change relative to adaptation capacity, not on the specific cause. Human activities that rapidly change environments across the globe produce the same systemic pressures.",
            "feedback_incorrect": "The model is agnostic about cause. It shows that whenever Environmental Change Rate exceeds Adaptation Speed across broad geographic scales, the resulting Extinction Pressure produces mass extinction dynamics, whether the driver is an asteroid, volcanism, or human activity."
        }
    ]
}

# =============================================================================
# L06: How Does 5G Actually Work?
# NGSS: HS-PS4-2, HS-PS4-3
# =============================================================================
L06_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Electromagnetic waves are used for wireless communication. Which relationship between frequency and wavelength is correct?",
            "choices": {
                "A": "Higher frequency corresponds to longer wavelength",
                "B": "Higher frequency corresponds to shorter wavelength",
                "C": "Frequency and wavelength are independent of each other",
                "D": "All electromagnetic waves have the same wavelength regardless of frequency"
            },
            "correct": "B",
            "feedback_correct": "Correct. Frequency and wavelength are inversely related. Since all electromagnetic waves travel at the speed of light, higher frequency waves must have shorter wavelengths.",
            "feedback_incorrect": "Frequency and wavelength have an inverse relationship: as frequency increases, wavelength decreases. This follows from the wave equation: speed of light = frequency x wavelength."
        },
        {
            "question": "When an electromagnetic wave encounters a solid wall, some of its energy is absorbed. Which factor most determines how much energy is absorbed?",
            "choices": {
                "A": "The color of the wall",
                "B": "The frequency of the electromagnetic wave and the material composition of the wall",
                "C": "The speed at which the wave is traveling",
                "D": "The number of walls in the building"
            },
            "correct": "B",
            "feedback_correct": "Correct. Absorption depends on the interaction between the wave's frequency and the material's molecular structure. Higher-frequency waves are generally absorbed more readily by common building materials.",
            "feedback_incorrect": "Absorption depends on two factors: the frequency of the wave (higher frequencies tend to be absorbed more) and the material properties of the obstacle (density, composition, moisture content)."
        },
        {
            "question": "A cell tower broadcasts a signal. According to the inverse square law, what happens to the signal strength when the distance from the tower is doubled?",
            "choices": {
                "A": "Signal strength is reduced to one-half",
                "B": "Signal strength is reduced to one-quarter",
                "C": "Signal strength remains the same",
                "D": "Signal strength doubles"
            },
            "correct": "B",
            "feedback_correct": "Correct. The inverse square law states that signal intensity is inversely proportional to the square of the distance. Doubling the distance reduces signal strength to (1/2)^2 = 1/4.",
            "feedback_incorrect": "The inverse square law states that intensity decreases with the square of the distance. At twice the distance, intensity drops to 1/4, not 1/2. This is because the signal spreads over four times the area."
        },
        {
            "question": "5G networks use frequencies in the 'millimeter wave' range (30-300 GHz). What trade-off does this frequency range present for network engineers?",
            "choices": {
                "A": "Millimeter waves travel farther but carry less data than lower frequencies",
                "B": "Millimeter waves carry enormous amounts of data but are easily blocked by buildings, trees, and rain",
                "C": "Millimeter waves are invisible to detection equipment, making network monitoring impossible",
                "D": "Millimeter waves require less energy to transmit than lower-frequency signals"
            },
            "correct": "B",
            "feedback_correct": "Correct. This fundamental trade-off between data capacity and penetration ability is the central engineering challenge of 5G: higher frequencies enable faster data rates but are absorbed and blocked by obstacles far more easily.",
            "feedback_incorrect": "The millimeter wave trade-off is fundamental: these high frequencies can carry vastly more data (10+ Gbps) but are easily absorbed by buildings, vegetation, rain, and even humidity, severely limiting their range and penetration."
        },
        {
            "question": "MIMO (Multiple-Input Multiple-Output) antenna technology uses multiple antennas simultaneously. What is the primary advantage of this approach?",
            "choices": {
                "A": "It allows a single antenna to broadcast at multiple frequencies simultaneously",
                "B": "It increases network capacity by transmitting and receiving multiple independent data streams at the same time",
                "C": "It eliminates the need for cell towers entirely",
                "D": "It converts electromagnetic waves into sound waves for clearer voice calls"
            },
            "correct": "B",
            "feedback_correct": "Correct. MIMO uses spatial multiplexing to send multiple independent data streams through multiple antennas simultaneously, dramatically increasing the total data capacity of the network.",
            "feedback_incorrect": "MIMO's primary advantage is increased capacity through spatial multiplexing. By using multiple antennas to transmit and receive independent data streams simultaneously, the network can serve more users at higher speeds."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the wireless communication model, what is the fundamental trade-off that the relationship between Signal Frequency and Wave Penetration reveals?",
            "choices": {
                "A": "Higher frequencies penetrate materials better but carry less data",
                "B": "Higher frequencies carry more data but penetrate materials less effectively, requiring more infrastructure to compensate",
                "C": "Signal frequency has no measurable effect on wave penetration in the model",
                "D": "Lower frequencies require more tower density because they carry less data per tower"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates the core physics trade-off: Data Transfer Rate increases with frequency but Wave Penetration decreases, forcing engineers to dramatically increase Tower Density to maintain coverage.",
            "feedback_incorrect": "The model reveals the fundamental constraint: as Signal Frequency increases, Data Transfer Rate rises (more bandwidth) but Wave Penetration drops (signals blocked more easily). This trade-off is the defining engineering challenge of 5G."
        },
        {
            "question": "A student compares the 4G scenario (700 MHz) to the 5G millimeter wave scenario (39 GHz) in the model. Tower Density must increase dramatically for 5G. What does the model show as the primary reason?",
            "choices": {
                "A": "5G towers are physically smaller and cannot transmit as much power",
                "B": "Each 5G millimeter wave cell covers only 200-300 meters versus 2-5 kilometers for 4G because higher-frequency signals are absorbed more rapidly by the atmosphere and obstacles",
                "C": "5G towers are more expensive, so more small towers are needed to reduce cost",
                "D": "4G towers broadcast in all directions while 5G towers can only broadcast in one direction"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that millimeter wave signals attenuate so rapidly that each cell covers a fraction of the area of a 4G cell, requiring a massive increase in the number of transmitters to provide continuous coverage.",
            "feedback_incorrect": "The model demonstrates that coverage area per cell shrinks dramatically at higher frequencies. A 4G cell at 700 MHz might cover 2-5 km, but a 5G millimeter wave cell at 39 GHz covers only 200-300 meters due to rapid signal attenuation."
        },
        {
            "question": "The model shows that increasing Tower Density to compensate for poor Wave Penetration creates a secondary problem. What is it?",
            "choices": {
                "A": "More towers reduce the total network capacity by splitting the available bandwidth",
                "B": "Interference Level increases as more closely spaced towers produce overlapping signals, requiring beamforming and MIMO to manage",
                "C": "More towers consume less total energy because each tower is smaller",
                "D": "Tower Density has no effect on any other variable in the model"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals a cascade: more towers create more signal overlap and interference, which degrades network quality. Engineers must deploy beamforming and MIMO technology to direct signals precisely and manage interference.",
            "feedback_incorrect": "The model shows that Tower Density creates a secondary challenge: more closely-spaced towers produce overlapping signals that interfere with each other, requiring sophisticated beamforming and MIMO technology to maintain signal quality."
        },
        {
            "question": "Based on the model, why did engineers design 5G as a layered network using multiple frequency bands rather than a single millimeter wave frequency?",
            "choices": {
                "A": "Because a single frequency would have been too simple to implement",
                "B": "Because no single frequency band resolves the coverage-versus-capacity trade-off; low-band provides wide coverage, mid-band balances speed and reach, and millimeter wave provides high-density capacity",
                "C": "Because the model shows that all frequency bands perform identically",
                "D": "Because millimeter waves are dangerous to human health at high power levels"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that no single frequency band can optimize both coverage and capacity. The layered approach uses each band's strengths: low-band for reach, mid-band for balance, and millimeter wave for dense, high-speed areas.",
            "feedback_incorrect": "The model shows that the coverage-capacity trade-off cannot be resolved with a single frequency. A layered approach assigns low-band frequencies for rural coverage, mid-band for urban areas, and millimeter wave for high-density locations like stadiums."
        },
        {
            "question": "A student claims that 5G is simply 'better 4G' with no fundamental physics differences. Using evidence from the model, which response best evaluates this claim?",
            "choices": {
                "A": "The claim is correct because both use electromagnetic waves for communication",
                "B": "The claim is incorrect because 5G operates at fundamentally different frequencies that introduce new physics trade-offs: millimeter waves behave qualitatively differently than sub-6 GHz signals regarding penetration, absorption, and infrastructure requirements",
                "C": "The claim is correct because tower density is the same for both technologies",
                "D": "The claim is incorrect because 5G uses sound waves instead of electromagnetic waves"
            },
            "correct": "B",
            "feedback_correct": "Correct. While both use electromagnetic waves, the model shows that millimeter wave frequencies introduce qualitatively different behavior: near-total absorption by obstacles, atmospheric attenuation by rain, and coverage areas orders of magnitude smaller.",
            "feedback_incorrect": "The model demonstrates that 5G is not simply a faster version of 4G. The jump to millimeter wave frequencies introduces fundamentally different physics: signals that cannot penetrate walls, are absorbed by rain, and require completely different infrastructure."
        }
    ]
}

# =============================================================================
# L07: Why Does a Glow Stick Stop Glowing?
# NGSS: HS-PS1-4, HS-PS1-6
# =============================================================================
L07_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Chemiluminescence is the production of light from a chemical reaction. What distinguishes chemiluminescence from incandescence (such as a light bulb filament)?",
            "choices": {
                "A": "Chemiluminescence requires electricity while incandescence does not",
                "B": "Chemiluminescence converts chemical energy directly to light without requiring high temperatures, while incandescence produces light by heating a material",
                "C": "Chemiluminescence produces only ultraviolet light while incandescence produces visible light",
                "D": "There is no meaningful difference between the two processes"
            },
            "correct": "B",
            "feedback_correct": "Correct. Chemiluminescence is 'cold light' produced directly from chemical bond energy, while incandescence requires heating a material to such high temperatures that it emits visible radiation.",
            "feedback_incorrect": "The key distinction is the energy source. Chemiluminescence converts chemical bond energy directly into photons without significant heat, while incandescence produces light by heating a material until it glows. This is why glow sticks are cool to the touch."
        },
        {
            "question": "Activation energy is the minimum energy that reacting molecules must possess for a chemical reaction to occur. How does increasing temperature affect the fraction of molecules that exceed this threshold?",
            "choices": {
                "A": "Higher temperature decreases the fraction of molecules exceeding the activation energy",
                "B": "Higher temperature increases the fraction of molecules exceeding the activation energy, accelerating the reaction",
                "C": "Temperature has no effect on the activation energy of a reaction",
                "D": "Higher temperature eliminates the need for activation energy entirely"
            },
            "correct": "B",
            "feedback_correct": "Correct. Higher temperature increases the average kinetic energy of molecules, shifting the distribution so that a greater fraction exceeds the activation energy threshold, resulting in more successful collisions per unit time.",
            "feedback_incorrect": "Temperature increases the kinetic energy of molecules, shifting the Maxwell-Boltzmann distribution so that more molecules exceed the activation energy threshold. This is why chemical reactions generally speed up when heated."
        },
        {
            "question": "In a chemical reaction, reactants are converted to products. As a reaction proceeds in a closed system (like a glow stick), what happens to the concentration of reactants over time?",
            "choices": {
                "A": "Reactant concentration remains constant throughout the reaction",
                "B": "Reactant concentration increases as the reaction proceeds",
                "C": "Reactant concentration decreases as reactants are consumed and converted to products",
                "D": "Reactant concentration oscillates between high and low values"
            },
            "correct": "C",
            "feedback_correct": "Correct. In a closed system, reactants are consumed as they are converted to products. This decrease in concentration is why chemical reactions typically slow down over time.",
            "feedback_incorrect": "In a closed system like a glow stick, reactants are consumed as the reaction proceeds. Their concentration decreases steadily as they are converted into products, which is why glow sticks gradually dim."
        },
        {
            "question": "A student places one glow stick in hot water and an identical one in ice water. Both are activated at the same time. Which observation is the student most likely to make?",
            "choices": {
                "A": "Both glow sticks will have identical brightness and duration",
                "B": "The hot glow stick will glow brighter but stop sooner; the cold one will glow dimmer but last longer",
                "C": "The cold glow stick will glow brighter because cold preserves chemical energy",
                "D": "Neither glow stick will work because extreme temperatures prevent the chemical reaction"
            },
            "correct": "B",
            "feedback_correct": "Correct. Heat increases the reaction rate, producing brighter light but consuming reactants faster. Cold slows the reaction, producing dimmer light but extending the duration.",
            "feedback_incorrect": "Temperature controls reaction rate. The heated glow stick has a faster reaction rate (brighter glow) but exhausts its reactants sooner. The cooled glow stick has a slower rate (dimmer glow) but its reactants last longer."
        },
        {
            "question": "Chemical equilibrium in a reaction system is reached when which condition is met?",
            "choices": {
                "A": "All reactants have been completely converted to products",
                "B": "The forward and reverse reactions occur at equal rates, resulting in no net change in concentrations",
                "C": "The reaction has completely stopped and no molecular motion occurs",
                "D": "The temperature of the system equals room temperature"
            },
            "correct": "B",
            "feedback_correct": "Correct. At chemical equilibrium, the forward and reverse reactions continue but at equal rates, so concentrations of reactants and products remain constant. The reaction has not stopped; it is dynamically balanced.",
            "feedback_incorrect": "Chemical equilibrium is a dynamic state where forward and reverse reactions occur at equal rates. Concentrations of reactants and products remain constant, but the reactions have not stopped. It is balance, not cessation."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the glow stick model, Temperature is identified as the master controller. Why does the model assign this role to Temperature?",
            "choices": {
                "A": "Because Temperature is the only variable in the model",
                "B": "Because Temperature directly determines Reaction Rate, which cascades to affect Light Output, Chemical Concentration depletion, and glow duration",
                "C": "Because Temperature determines the color of the glow stick",
                "D": "Because Temperature is the only component students can observe without instruments"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows Temperature as the upstream driver that sets the pace of the entire system: higher temperature increases Reaction Rate, which increases Light Output but also accelerates Chemical Concentration depletion.",
            "feedback_incorrect": "Temperature is the master controller because it directly sets the Reaction Rate, which then determines how quickly Chemical Concentration drops, how bright Light Output is, and how long the glow lasts. All other dynamics flow from this variable."
        },
        {
            "question": "The model reveals a fundamental trade-off between brightness and duration. A student asks: 'Does a hot glow stick produce more total light than a cold one?' What does the model show?",
            "choices": {
                "A": "The hot glow stick produces significantly more total light because heat creates additional chemical energy",
                "B": "Total light output is roughly constant regardless of temperature because the same amount of chemical energy is converted to light; temperature only affects the rate of conversion",
                "C": "The cold glow stick produces more total light because less energy is wasted as heat",
                "D": "Total light output depends entirely on the color of the fluorescent dye, not temperature"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates conservation of energy: the same chemical fuel produces approximately the same total light output, just distributed differently over time. Temperature controls the rate, not the total energy conversion.",
            "feedback_incorrect": "The model reveals that total light output is approximately constant because temperature changes the rate of energy conversion, not the total amount of chemical energy available. A hot glow stick is brighter but shorter; a cold one is dimmer but longer."
        },
        {
            "question": "In the model, Product Buildup creates a negative feedback loop. What effect does this have on the reaction over time?",
            "choices": {
                "A": "Product Buildup accelerates the reaction, making the glow stick brighter over time",
                "B": "Product Buildup dilutes remaining reactants and shifts the system toward equilibrium, progressively slowing the reaction and dimming the glow",
                "C": "Product Buildup has no effect on reaction rate because products do not interact with reactants",
                "D": "Product Buildup causes the glow stick to switch colors as different products accumulate"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that as products (phenol and CO2) accumulate, they dilute the remaining reactants, reducing collision frequency and pushing the system toward equilibrium, which explains the gradual dimming of glow sticks.",
            "feedback_incorrect": "Product Buildup creates negative feedback: accumulated products dilute the remaining reactants, reduce the probability of reactant collisions, and drive the system toward equilibrium. This is why glow sticks gradually dim rather than shutting off suddenly."
        },
        {
            "question": "A student runs the model at three temperatures and observes that the glow stick at high temperature emits the same total light as the one at low temperature, just over a shorter period. Which chemical principle does this observation illustrate?",
            "choices": {
                "A": "Le Chatelier's principle of chemical equilibrium shifts",
                "B": "Conservation of energy: the total chemical energy in the reactants is fixed and temperature only affects the rate of its conversion to light",
                "C": "The law of definite proportions in chemical compounds",
                "D": "Hess's law of constant heat summation"
            },
            "correct": "B",
            "feedback_correct": "Correct. This observation perfectly illustrates conservation of energy: the total energy stored in the chemical reactants is fixed at the time of activation. Temperature controls how quickly that energy is converted, not how much is available.",
            "feedback_incorrect": "The observation demonstrates conservation of energy. The glow stick contains a fixed amount of chemical energy. Temperature changes the rate of energy release (power) but not the total energy available (work), so total light output remains approximately constant."
        },
        {
            "question": "Based on the model, a glow stick manufacturer wants to maximize the duration of glow for a 12-hour emergency light. Which combination of conditions does the model recommend?",
            "choices": {
                "A": "High initial chemical concentration and high temperature to maximize brightness",
                "B": "High initial chemical concentration with moderate-to-low temperature to slow the reaction rate while maintaining adequate brightness over the longest possible duration",
                "C": "Low chemical concentration and high temperature to produce the most efficient light",
                "D": "Add a catalyst to speed up the reaction so it finishes faster"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that maximizing duration requires more reactant fuel (high concentration) combined with conditions that slow consumption (moderate-to-low temperature), producing adequate light over a longer period.",
            "feedback_incorrect": "The model demonstrates that duration depends on two factors: total reactant supply and consumption rate. For a 12-hour emergency light, you need abundant reactants (high concentration) consumed slowly (moderate-to-low temperature)."
        }
    ]
}

# =============================================================================
# L08: The Nitrogen Crisis: Why Fertilizer Is Destroying Our Rivers
# NGSS: HS-LS2-4, HS-ESS2-2
# =============================================================================
L08_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Nitrogen is essential for plant growth. In what form do most plants absorb nitrogen from the soil?",
            "choices": {
                "A": "As nitrogen gas (N2) directly from the atmosphere through their leaves",
                "B": "As dissolved nitrate (NO3-) or ammonium (NH4+) ions through their roots",
                "C": "As solid nitrogen crystals extracted from bedrock by root pressure",
                "D": "As nitrogen dioxide (NO2) absorbed from automobile exhaust"
            },
            "correct": "B",
            "feedback_correct": "Correct. Most plants absorb nitrogen as dissolved nitrate or ammonium ions through their root systems. Plants cannot use atmospheric N2 directly because the triple bond between nitrogen atoms is too stable.",
            "feedback_incorrect": "Plants absorb nitrogen primarily as dissolved nitrate (NO3-) or ammonium (NH4+) ions through their roots. Most plants cannot fix atmospheric N2 directly because the triple bond requires enormous energy to break."
        },
        {
            "question": "Eutrophication is a process that occurs in water bodies receiving excess nutrients. Which sequence correctly describes the eutrophication process?",
            "choices": {
                "A": "Excess nutrients -> algal bloom -> algae die -> bacterial decomposition consumes oxygen -> aquatic organisms suffocate",
                "B": "Excess nutrients -> fish population increases -> water temperature rises -> algae die",
                "C": "Excess nutrients -> water becomes clearer -> more sunlight reaches the bottom -> plants grow on the lakebed",
                "D": "Excess nutrients -> bacteria consume the nutrients directly -> oxygen levels increase -> fish populations boom"
            },
            "correct": "A",
            "feedback_correct": "Correct. Eutrophication follows a predictable cascade: excess nutrients fuel explosive algal growth, the algae die and sink, bacteria decompose the dead algae and consume dissolved oxygen, creating hypoxic conditions that kill aquatic life.",
            "feedback_incorrect": "Eutrophication follows a specific causal chain: nutrient enrichment fuels algal blooms, the algae eventually die, bacterial decomposition of the dead biomass consumes dissolved oxygen, and the resulting hypoxia kills fish and other organisms."
        },
        {
            "question": "What is nonpoint source pollution, and why is it particularly difficult to control?",
            "choices": {
                "A": "Pollution from a single, identifiable discharge pipe that can be easily regulated",
                "B": "Pollution from many diffuse sources across a landscape, such as agricultural runoff, making it difficult to trace and regulate",
                "C": "Pollution that occurs at a single geographic point but at unpredictable intervals",
                "D": "Pollution visible to the naked eye that can be physically collected and removed"
            },
            "correct": "B",
            "feedback_correct": "Correct. Nonpoint source pollution comes from widespread, diffuse sources rather than a single discharge point. Agricultural runoff from millions of individual fields is virtually impossible to monitor or regulate at each source.",
            "feedback_incorrect": "Nonpoint source pollution originates from many scattered sources (farm fields, lawns, roads) rather than a single pipe or outfall. Its diffuse nature makes it extremely difficult to monitor, regulate, or control compared to point-source pollution."
        },
        {
            "question": "The Gulf of Mexico contains one of the world's largest 'dead zones.' What defines a dead zone in aquatic ecology?",
            "choices": {
                "A": "An area where water temperature exceeds 40 degrees Celsius",
                "B": "An area where dissolved oxygen levels are too low to support most marine life",
                "C": "An area where no water currents flow, creating stagnant conditions",
                "D": "An area where radioactive contamination prevents any biological activity"
            },
            "correct": "B",
            "feedback_correct": "Correct. A dead zone is an area of hypoxia where dissolved oxygen drops below approximately 2 mg/L, suffocating most marine organisms. The Gulf of Mexico dead zone can exceed 22,000 square kilometers annually.",
            "feedback_incorrect": "A dead zone is defined by hypoxia, dissolved oxygen levels below approximately 2 mg/L that cannot support most marine life. The Gulf of Mexico dead zone, fed by agricultural runoff from the Mississippi River basin, can cover over 22,000 km2."
        },
        {
            "question": "Only a fraction of nitrogen fertilizer applied to crops is actually absorbed by plants. What happens to the remainder?",
            "choices": {
                "A": "It is completely broken down by soil bacteria into harmless atmospheric nitrogen within hours",
                "B": "It remains permanently bound to soil particles and never moves",
                "C": "A significant portion washes off fields as runoff into streams and rivers or leaches into groundwater",
                "D": "It evaporates into the atmosphere as nitrogen gas within minutes of application"
            },
            "correct": "C",
            "feedback_correct": "Correct. Typically only 30-50% of applied nitrogen is absorbed by crops. The remainder enters waterways through surface runoff and groundwater leaching, making agriculture the largest source of nutrient pollution.",
            "feedback_incorrect": "Only 30-50% of applied nitrogen fertilizer is absorbed by crops. Much of the rest is lost through surface runoff during rain events and leaching into groundwater, eventually reaching streams, rivers, and ultimately coastal waters."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the nitrogen pollution model, Soil Depletion creates a vicious cycle with Fertilizer Application. How does the model represent this feedback?",
            "choices": {
                "A": "Soil Depletion reduces the need for fertilizer because degraded soil cannot support crops",
                "B": "Intensive farming degrades soil, which holds less nitrogen, requiring more fertilizer application, which further degrades soil structure in a self-reinforcing loop",
                "C": "Soil Depletion and Fertilizer Application are independent variables with no interaction",
                "D": "Soil Depletion is beneficial because it increases the soil's ability to filter nitrogen"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals a positive feedback loop: intensive farming with high fertilizer use degrades soil organic matter and structure, reducing the soil's capacity to retain nitrogen, which demands even more fertilizer application.",
            "feedback_incorrect": "The model shows a self-reinforcing cycle: heavy fertilizer use and intensive monoculture deplete soil organic matter, reducing the soil's natural nitrogen-holding capacity. This forces farmers to apply even more synthetic fertilizer, further degrading the soil."
        },
        {
            "question": "The model demonstrates a threshold effect in the relationship between Nitrogen Runoff and Algal Bloom Growth. What does this threshold reveal?",
            "choices": {
                "A": "Any amount of nitrogen runoff immediately causes algal blooms",
                "B": "Below a critical nitrogen concentration, waterways can process excess nutrients; above it, algal growth overwhelms the system's capacity and dead zones form",
                "C": "Algal blooms are caused by temperature, not nitrogen, so the threshold is irrelevant",
                "D": "The threshold represents the point where algal growth becomes beneficial to the ecosystem"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows a non-linear response: aquatic ecosystems can absorb and process moderate nitrogen loading, but above a critical concentration, the system tips into uncontrollable algal bloom and subsequent oxygen collapse.",
            "feedback_incorrect": "The model reveals non-linear dynamics: rivers and coastal waters have a finite capacity to process nitrogen. Below the threshold, natural processes handle the load. Above it, algal growth becomes explosive and self-sustaining, leading to dead zones."
        },
        {
            "question": "A student compares the 'Conventional Farming' and 'Precision Agriculture' scenarios in the model. The precision agriculture scenario reduces Fertilizer Application by 40% while maintaining crop yields. What does the model show happens to downstream impacts?",
            "choices": {
                "A": "Downstream impacts remain unchanged because crop uptake absorbs all the saved fertilizer",
                "B": "Nitrogen Runoff, Algal Bloom Growth, and Oxygen Depletion all decrease significantly because less excess nitrogen enters waterways",
                "C": "Downstream impacts worsen because less fertilizer means weaker crops that erode soil faster",
                "D": "Only Water Treatment Cost changes; biological impacts remain the same"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that reducing excess fertilizer application directly reduces the cascade: less nitrogen runs off, fewer algal blooms develop, oxygen depletion decreases, and dead zone formation is reduced.",
            "feedback_incorrect": "The model demonstrates that reducing Fertilizer Application to match actual crop needs dramatically reduces the entire downstream cascade. Since most pollution comes from excess application (the 50-70% not absorbed by crops), precision agriculture addresses the root cause."
        },
        {
            "question": "The model reveals that the economic costs of nutrient pollution often exceed the economic gains from the excess fertilizer that caused it. Which model components support this finding?",
            "choices": {
                "A": "Only Fertilizer Application cost matters because all other costs are externalized",
                "B": "Water Treatment Cost from removing nitrogen from drinking water, fishery losses from dead zones, and tourism damage collectively exceed the marginal agricultural revenue from excess fertilizer application",
                "C": "The model does not track any economic variables",
                "D": "Fertilizer always generates more economic value than it costs, regardless of environmental damage"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that when all costs are accounted for, the marginal revenue from excess fertilizer is dwarfed by Water Treatment Cost, fishery collapse losses, and tourism damage from dead zones.",
            "feedback_incorrect": "The model integrates economic analysis showing that excess fertilizer (beyond what crops absorb) generates minimal additional revenue while creating billions in downstream costs: water treatment, fishery losses, tourism decline, and ecosystem restoration."
        },
        {
            "question": "Based on the model, which approach most effectively breaks the nitrogen pollution cycle?",
            "choices": {
                "A": "Applying more fertilizer to grow more crops that absorb more nitrogen",
                "B": "Combining precision agriculture (reducing excess application), soil health restoration (increasing nitrogen retention), and buffer zones (intercepting runoff before it reaches waterways)",
                "C": "Banning all fertilizer use immediately and relying on natural soil nitrogen",
                "D": "Building larger water treatment plants downstream to remove all nitrogen"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that breaking the cycle requires addressing multiple points: reducing excess input (precision agriculture), restoring the soil's natural capacity (soil health), and intercepting pollution before it reaches water (buffer zones).",
            "feedback_incorrect": "The model demonstrates that effective intervention requires a multi-pronged approach: precision application reduces excess input, soil restoration rebuilds natural nitrogen retention, and buffer zones provide a last line of defense before nitrogen reaches waterways."
        }
    ]
}

# =============================================================================
# L09: How Do Doctors See Inside You Without Cutting You Open?
# NGSS: HS-PS2-4, HS-PS4-4
# =============================================================================
L09_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "MRI (Magnetic Resonance Imaging) creates detailed images of internal body structures. Which type of energy does MRI use to generate these images?",
            "choices": {
                "A": "Ionizing X-ray radiation that passes through the body",
                "B": "Strong magnetic fields and radiofrequency electromagnetic waves",
                "C": "Ultrasonic sound waves that reflect off internal organs",
                "D": "Infrared heat radiation detected through the skin"
            },
            "correct": "B",
            "feedback_correct": "Correct. MRI uses a powerful static magnetic field to align hydrogen nuclei in the body, then applies radiofrequency pulses to excite them. The signals emitted as nuclei return to equilibrium are used to construct images.",
            "feedback_incorrect": "MRI does not use X-rays, sound waves, or infrared radiation. It works by placing the body in a strong magnetic field, applying radiofrequency electromagnetic pulses, and detecting the signals emitted by hydrogen nuclei as they relax."
        },
        {
            "question": "Clinical MRI machines operate at magnetic field strengths of 1.5 to 3 Tesla. How does this compare to Earth's natural magnetic field?",
            "choices": {
                "A": "MRI machines produce a field about twice as strong as Earth's",
                "B": "MRI machines produce a field 30,000 to 60,000 times stronger than Earth's magnetic field",
                "C": "MRI machines and Earth have approximately the same magnetic field strength",
                "D": "Earth's magnetic field is stronger than any MRI machine"
            },
            "correct": "B",
            "feedback_correct": "Correct. Earth's magnetic field is approximately 50 microtesla (0.00005 Tesla). A 3 Tesla MRI is 60,000 times stronger, which is why MRI rooms require strict safety protocols for metallic objects.",
            "feedback_incorrect": "Clinical MRI magnets are extraordinarily powerful: 1.5 to 3 Tesla compared to Earth's approximately 50 microtesla. This means an MRI magnet is 30,000 to 60,000 times stronger than the planet's natural magnetic field."
        },
        {
            "question": "The superconducting coils in an MRI machine must be cooled to near absolute zero using liquid helium. What property does superconductivity provide that is essential for MRI?",
            "choices": {
                "A": "Superconducting coils emit X-rays that help create the image",
                "B": "Zero electrical resistance allows the coils to carry enormous electrical currents without energy loss, generating a stable, powerful magnetic field",
                "C": "Superconducting coils are magnetic only at low temperatures and become non-magnetic when warm",
                "D": "Liquid helium creates the radio waves used to excite hydrogen nuclei"
            },
            "correct": "B",
            "feedback_correct": "Correct. At superconducting temperatures, the coil wire has zero electrical resistance, allowing massive persistent currents to flow without energy loss, producing the stable, powerful magnetic field MRI requires.",
            "feedback_incorrect": "Superconductivity provides zero electrical resistance, allowing the coils to sustain enormous currents indefinitely without energy input or heat generation. This is the only practical way to produce the powerful, stable magnetic fields that MRI requires."
        },
        {
            "question": "Different tissue types appear as different shades in an MRI image. What property of tissues creates this contrast?",
            "choices": {
                "A": "Different tissues have different colors that are directly photographed by the scanner",
                "B": "Different tissues have different densities that block magnetic fields differently",
                "C": "Different tissues contain different amounts of hydrogen, and the hydrogen nuclei in each tissue type have different relaxation times after radiofrequency excitation",
                "D": "Different tissues reflect radio waves at different angles"
            },
            "correct": "C",
            "feedback_correct": "Correct. MRI contrast comes from differences in how quickly hydrogen nuclei in different tissues return to equilibrium (relaxation times) after being excited by a radiofrequency pulse. Fat, muscle, and fluid all have distinct relaxation behaviors.",
            "feedback_incorrect": "MRI contrast depends on tissue-specific relaxation times. After radiofrequency excitation, hydrogen nuclei in different tissues (fat, muscle, fluid, bone) return to equilibrium at different rates, creating the signal differences that produce image contrast."
        },
        {
            "question": "Why is MRI generally considered safer than CT scans for repeated imaging of the same patient?",
            "choices": {
                "A": "MRI machines are smaller and less intimidating for patients",
                "B": "MRI does not use ionizing radiation, eliminating the cumulative cancer risk associated with repeated X-ray or CT exposure",
                "C": "MRI scans take less time than CT scans",
                "D": "CT scans require injection of toxic contrast agents while MRI does not use any contrast"
            },
            "correct": "B",
            "feedback_correct": "Correct. MRI uses magnetic fields and radio waves, which are non-ionizing and do not damage DNA. CT scans use ionizing X-ray radiation, which carries a small but cumulative cancer risk with repeated exposure.",
            "feedback_incorrect": "The key safety advantage of MRI is that it uses non-ionizing radiation (magnetic fields and radio waves) that does not damage DNA. CT scans use ionizing X-rays that carry cumulative cancer risk, making repeated CT scanning a clinical concern."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the MRI physics model, Magnetic Field Strength is identified as a primary driver of image quality. What specific relationship does the model demonstrate?",
            "choices": {
                "A": "Higher field strength reduces Image Resolution because stronger magnets distort the image",
                "B": "Higher field strength increases both Image Resolution and Tissue Contrast by improving the signal-to-noise ratio of detected signals",
                "C": "Magnetic Field Strength affects only scan time, not image quality",
                "D": "Lower field strength produces better images because weaker magnets create less interference"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that stronger magnetic fields align more hydrogen nuclei, producing stronger signals relative to background noise. This improved signal-to-noise ratio directly enhances both spatial resolution and tissue contrast.",
            "feedback_incorrect": "The model demonstrates that Magnetic Field Strength improves image quality by increasing the signal-to-noise ratio. More nuclei are aligned in a stronger field, producing stronger detectable signals that translate to better resolution and tissue differentiation."
        },
        {
            "question": "The model reveals a critical vulnerability in MRI systems related to Coil Temperature. What happens if the superconducting coils warm above their critical temperature?",
            "choices": {
                "A": "The image quality improves because warmer coils produce stronger magnetic fields",
                "B": "A 'quench' occurs: the coils lose superconductivity, resistance appears, enormous currents generate heat that explosively boils the liquid helium, and the magnetic field collapses",
                "C": "The coils gradually reduce their magnetic field output over several hours",
                "D": "Nothing happens because modern MRI coils work at any temperature"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model identifies the quench as the most catastrophic failure mode in MRI: loss of superconductivity causes the enormous stored current to generate extreme heat, explosively vaporizing liquid helium and destroying the magnetic field.",
            "feedback_incorrect": "A quench is a rapid, dangerous failure where superconductivity is lost. The enormous persistent current suddenly encounters electrical resistance, generating extreme heat that boils the liquid helium explosively. The magnetic field collapses and the system is disabled."
        },
        {
            "question": "A student compares 1.5T and 7T MRI scenarios in the model. The 7T scanner produces dramatically better Image Resolution but the model also shows significant increases in Patient Safety concerns. Why?",
            "choices": {
                "A": "7T magnets are physically larger and patients feel claustrophobic",
                "B": "Stronger magnetic fields create greater forces on metallic implants, increase radiofrequency energy absorption in tissue (SAR), and produce louder gradient noise, all posing elevated safety risks",
                "C": "7T scanners take longer, and patients become bored during the scan",
                "D": "7T scanners require patients to hold their breath for the entire scan duration"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that higher field strength amplifies multiple safety concerns: greater forces on any ferromagnetic materials near the scanner, increased specific absorption rate (SAR) heating of tissue, and louder acoustic noise from gradient coils.",
            "feedback_incorrect": "The model demonstrates that Patient Safety concerns scale with field strength. Stronger magnets exert greater forces on metallic objects, deposit more radiofrequency energy into tissue (potential heating), and produce louder gradient switching noise."
        },
        {
            "question": "The model shows that Diagnostic Accuracy depends on the combination of Image Resolution, Tissue Contrast, and radiologist expertise. Why does the model indicate that the most powerful MRI machine is not always the best clinical choice?",
            "choices": {
                "A": "Because more powerful machines always produce worse images",
                "B": "Because 1.5T provides sufficient Diagnostic Accuracy for most clinical diagnoses while presenting fewer Patient Safety challenges and lower Energy Consumption, making it the optimal trade-off",
                "C": "Because radiologists cannot interpret images from machines above 3T",
                "D": "Because all MRI machines produce identical images regardless of field strength"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that clinical decision-making must balance image quality against safety, cost, and energy. For most diagnoses, 1.5T provides adequate accuracy with lower risk, making it the practical optimum.",
            "feedback_incorrect": "The model reveals that optimal clinical practice involves trade-offs. While 7T provides superior images, 1.5T meets diagnostic needs for most conditions with significantly lower safety risks, energy costs, and infrastructure requirements."
        },
        {
            "question": "Based on the model, why is MRI particularly superior to CT or X-ray for imaging soft tissue structures like the brain, muscles, and ligaments?",
            "choices": {
                "A": "Because MRI uses stronger radiation that penetrates soft tissue more deeply",
                "B": "Because different soft tissues have distinct hydrogen content and relaxation times, creating excellent contrast on MRI, while X-rays and CT primarily differentiate tissues based on density differences that are minimal between soft tissues",
                "C": "Because soft tissues are transparent to magnetic fields and invisible to X-rays",
                "D": "Because MRI scans are faster than CT scans for soft tissue imaging"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model explains that MRI's tissue contrast mechanism (hydrogen relaxation times) varies significantly between soft tissues, while X-ray/CT contrast (density-based attenuation) shows minimal differences between soft tissue types.",
            "feedback_incorrect": "MRI excels at soft tissue because its contrast mechanism depends on hydrogen content and relaxation times, which differ substantially between muscle, fat, ligament, and brain tissue. X-rays and CT rely on density differences, which are small between soft tissues."
        }
    ]
}

# =============================================================================
# L10: Why Do Animals Migrate Thousands of Miles?
# NGSS: HS-LS2-8, HS-LS4-6
# =============================================================================
L10_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Animal migration is a seasonal movement between distinct habitats. What is the primary evolutionary driver that maintains migration behavior in a population?",
            "choices": {
                "A": "Animals migrate because they enjoy traveling and exploring new environments",
                "B": "Migration provides a net reproductive advantage: animals that migrate produce more surviving offspring than those that do not, despite the journey's risks",
                "C": "Animals migrate because other animals in the group force them to follow",
                "D": "Migration occurs randomly with no evolutionary explanation"
            },
            "correct": "B",
            "feedback_correct": "Correct. Migration is maintained by natural selection because the reproductive benefits at the destination (abundant food, safe breeding grounds) outweigh the mortality costs of the journey. It is a cost-benefit equation refined over millions of years.",
            "feedback_incorrect": "Migration persists because it is an evolutionarily stable strategy: the reproductive payoff at the destination exceeds the mortality cost of the journey. Natural selection maintains migration when stay-at-home individuals produce fewer surviving offspring."
        },
        {
            "question": "Many migratory birds navigate using Earth's magnetic field. What is the term for this biological ability?",
            "choices": {
                "A": "Echolocation",
                "B": "Magnetoreception",
                "C": "Phototropism",
                "D": "Chemotaxis"
            },
            "correct": "B",
            "feedback_correct": "Correct. Magnetoreception is the ability to detect and orient using Earth's magnetic field. It has been documented in birds, sea turtles, salmon, and other migratory species, likely using magnetite crystals or cryptochrome proteins.",
            "feedback_incorrect": "Magnetoreception is the biological sense that allows organisms to detect Earth's magnetic field for navigation. It is distinct from echolocation (sound-based), phototropism (light-directed growth), and chemotaxis (chemical-directed movement)."
        },
        {
            "question": "Stopover sites are locations where migratory animals rest and refuel during their journey. Why are these sites considered critical to species survival?",
            "choices": {
                "A": "Stopover sites are where migratory animals permanently settle and establish new populations",
                "B": "Loss of even a single critical stopover site can cause population collapse across the entire migration route because animals cannot complete the journey without refueling",
                "C": "Stopover sites are only used by weak or injured animals and are not important for healthy migrants",
                "D": "Animals do not actually need to stop during migration because they carry enough energy for the entire journey"
            },
            "correct": "B",
            "feedback_correct": "Correct. Most migratory species cannot carry enough energy reserves for the entire journey. They depend on a chain of stopover sites to refuel, and losing one critical link can strand entire populations mid-migration.",
            "feedback_incorrect": "Stopover sites function as essential refueling stations. Most migrants cannot complete their journey on a single energy load and must stop to eat and rest. Losing a critical stopover site can cause population-level mortality across the species' entire range."
        },
        {
            "question": "Climate change is altering the timing of seasonal events like insect emergence and plant flowering. How might this affect migratory species?",
            "choices": {
                "A": "Climate change benefits all migrants by extending the growing season at their destination",
                "B": "A phenological mismatch can occur when migrants arrive at breeding grounds on their genetically programmed schedule but peak food resources have already passed due to earlier warming",
                "C": "Climate change has no effect on migration because animals can instantly adjust their departure timing",
                "D": "Climate change only affects non-migratory species because migrants can escape to better climates"
            },
            "correct": "B",
            "feedback_correct": "Correct. Phenological mismatch occurs when migration timing (often triggered by day length, which is not changing) falls out of sync with food availability (which is shifting earlier due to warming), creating a survival crisis at the destination.",
            "feedback_incorrect": "Climate change creates phenological mismatch: migration timing is often controlled by photoperiod (unchanged), while food availability at the destination shifts with temperature (changing). Animals arrive 'on time' but the food peak has already passed."
        },
        {
            "question": "Many migratory species travel in large groups rather than individually. Which benefit of group migration provides the most direct survival advantage during the journey?",
            "choices": {
                "A": "Larger groups attract more predators, giving individuals practice at escaping",
                "B": "Group migration provides predator dilution (reduced individual risk), collective navigation accuracy, and energy savings through aerodynamic drafting",
                "C": "Groups migrate faster because dominant individuals force slower members to speed up",
                "D": "Group migration is purely social and provides no survival benefit"
            },
            "correct": "B",
            "feedback_correct": "Correct. Group migration provides multiple survival benefits: each individual's predation risk decreases with group size (dilution), navigation errors average out (collective intelligence), and aerodynamic drafting reduces energy costs.",
            "feedback_incorrect": "Group migration confers compound survival benefits: predator dilution (lower individual risk in larger groups), collective navigation (averaging out individual errors), and energy efficiency (drafting reduces flight costs by up to 25%)."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In the migration model, what does the relationship between Climate Trigger and Food Availability reveal as the most dangerous threat to migratory species?",
            "choices": {
                "A": "That food availability has no relationship to migration timing",
                "B": "That climate change is decoupling these two variables: Climate Trigger (photoperiod) remains constant while Food Availability shifts with temperature, creating a phenological mismatch that undermines the entire migration strategy",
                "C": "That Climate Trigger and Food Availability always remain perfectly synchronized",
                "D": "That animals can consciously adjust their departure date to match food availability"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that migration evolved when these two clocks were synchronized. Climate change is disrupting Food Availability timing while leaving the photoperiod trigger unchanged, creating a potentially fatal mismatch.",
            "feedback_incorrect": "The model demonstrates that migration timing evolved when photoperiod (the departure trigger) reliably predicted food availability at the destination. Climate change is shifting food timing independently of day length, breaking this ancient coordination."
        },
        {
            "question": "The model shows that Group Size provides compound benefits through the 'many wrongs' principle. What does this principle demonstrate about collective navigation?",
            "choices": {
                "A": "That all individuals in a group navigate perfectly, making no errors",
                "B": "That individual navigation errors are random and tend to cancel out when averaged across a group, resulting in a more accurate collective trajectory than any single individual could achieve",
                "C": "That only the lead animal navigates while all others follow blindly",
                "D": "That groups always navigate worse than individuals because they argue about direction"
            },
            "correct": "B",
            "feedback_correct": "Correct. The 'many wrongs' principle shows that when individual navigation errors are independent and random, the group's average heading is more accurate than any single member's heading, improving collective navigation accuracy.",
            "feedback_incorrect": "The 'many wrongs' principle is a statistical phenomenon: each individual's navigation has some random error, but when the group averages these independent errors, they cancel out, producing a collective heading more accurate than any individual's."
        },
        {
            "question": "A student runs the model with a scenario where one critical stopover site is removed from the migration route. What does the model predict?",
            "choices": {
                "A": "Animals easily skip the missing stopover and continue to the next one",
                "B": "Energy Reserves become depleted before reaching the next refueling point, leading to increased mortality that can cause population-level collapse even when breeding and wintering grounds remain intact",
                "C": "Animals permanently settle at the last available stopover site",
                "D": "Only old or weak animals are affected; healthy animals complete the journey without stopping"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that migration routes function as a chain of energy stations. Removing one link creates a gap too large for energy reserves to bridge, causing widespread mortality that cascades to population-level impacts.",
            "feedback_incorrect": "The model shows that stopover sites form an interconnected chain. Most migrants cannot simply skip a stop because their energy reserves are calibrated for the distance between established refueling points. Removing a critical stopover creates a lethal energy gap."
        },
        {
            "question": "The model demonstrates that migration is an evolutionary cost-benefit calculation. Which evidence from the model best explains why migration remains stable in a population?",
            "choices": {
                "A": "Migration is a learned behavior that parents teach to offspring each generation",
                "B": "Reproductive Success at the destination consistently exceeds the mortality cost of the journey, making migratory individuals produce more surviving offspring than non-migratory competitors",
                "C": "All animals migrate because it is an instinct that cannot be selected against",
                "D": "Migration exists because habitats are always identical at both endpoints"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that migration is evolutionarily stable only when the reproductive payoff exceeds the journey's mortality cost. If conditions change to shift this balance, migration can be lost from a population.",
            "feedback_incorrect": "The model frames migration as an ongoing cost-benefit equation shaped by natural selection. Reproductive Success at the destination must consistently exceed journey mortality for migration to be maintained. When this balance shifts, populations may evolve to become sedentary."
        },
        {
            "question": "Based on the model, which combination of human-caused changes poses the greatest threat to migratory species survival?",
            "choices": {
                "A": "Increased tourism at bird-watching sites along migration routes",
                "B": "Climate change disrupting food timing (phenological mismatch) combined with habitat destruction eliminating critical stopover sites, simultaneously breaking both the navigation reliability and energy supply that migration depends on",
                "C": "Construction of wind farms at the final destination only",
                "D": "Artificial lighting in cities that attracts migrating birds at night"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that migration depends on two pillars: timing coordination (food must be available on arrival) and infrastructure (stopover sites must exist for refueling). Climate change attacks the first while habitat destruction attacks the second, creating a compound threat.",
            "feedback_incorrect": "The model reveals that migration is vulnerable to compound threats. Climate change creates phenological mismatch (timing failure), while habitat destruction removes stopover sites (energy failure). Together, these simultaneously undermine the two fundamental requirements for successful migration."
        }
    ]
}

# =============================================================================
# Aggregated dictionary for all Grade 10 Level 2 lessons
# =============================================================================
ALL_QUESTIONS = {
    "G10L2-L01": L01_QUESTIONS,
    "G10L2-L02": L02_QUESTIONS,
    "G10L2-L03": L03_QUESTIONS,
    "G10L2-L04": L04_QUESTIONS,
    "G10L2-L05": L05_QUESTIONS,
    "G10L2-L06": L06_QUESTIONS,
    "G10L2-L07": L07_QUESTIONS,
    "G10L2-L08": L08_QUESTIONS,
    "G10L2-L09": L09_QUESTIONS,
    "G10L2-L10": L10_QUESTIONS,
}
