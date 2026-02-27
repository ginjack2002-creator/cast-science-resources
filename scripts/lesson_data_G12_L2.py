#!/usr/bin/env python3
"""Complete lesson data for G12L2-L01 through G12L2-L10 (Grade 12 Level 2: Global Systems & Sustainability)"""

L01 = {
    "id": "G12L2-L01",
    "title": "Is Climate Change Reversible?",
    "subtitle": "Modeling Carbon Cycle Dynamics and Climate Tipping Points",
    "ngss": "HS-ESS3-5",
    "ngss_desc": "Analyze geoscience data and the results from global climate models to make an evidence-based forecast of the current rate of global or regional climate change and associated future impacts to Earth systems.",
    "big_question": "If humanity stopped all carbon emissions tomorrow, would the climate return to normal — or have we already pushed Earth past points of no return that will reshape the planet for thousands of years regardless of what we do next?",
    "objectives": [
        "Model how carbon flows between the atmosphere, ocean, biosphere, and lithosphere in the global carbon cycle",
        "Explain how positive feedback loops such as permafrost thaw and ice-albedo reduction accelerate warming beyond initial forcing",
        "Predict the conditions under which climate tipping points are crossed and why they make warming partially irreversible",
        "Analyze evidence-based strategies for carbon reduction and evaluate their potential to stabilize global temperatures"
    ],
    "vocabulary": [
        ("Carbon Flux", "The rate at which carbon moves between reservoirs in the Earth system — measured in gigatons per year, carbon fluxes include photosynthesis, respiration, ocean absorption, fossil fuel combustion, and volcanic outgassing, with human activities now dominating the atmospheric input"),
        ("Positive Feedback Loop", "A process in which an initial change triggers effects that amplify the original change — in the climate system, warming melts ice which reduces reflectivity which causes more warming, creating a self-reinforcing cycle that accelerates temperature increase"),
        ("Tipping Point", "A critical threshold in the climate system beyond which a small additional change triggers a large, often irreversible shift to a new state — like a ball balanced on a hilltop that only needs a slight push to roll down and cannot easily be pushed back up"),
        ("Carbon Sink", "A natural or artificial reservoir that absorbs and stores more carbon from the atmosphere than it releases — forests, oceans, and soil are major natural sinks, but their capacity to absorb carbon decreases as temperatures rise and ecosystems are degraded")
    ],
    "components": [
        ("Atmospheric CO2", "The concentration of carbon dioxide in the atmosphere measured in parts per million — the primary driver of the greenhouse effect, currently at approximately 424 ppm compared to the pre-industrial level of 280 ppm", True),
        ("Fossil Fuel Emissions", "The rate of carbon dioxide released from burning coal, oil, and natural gas for energy and industry — currently approximately 36 gigatons per year and representing the dominant human contribution to atmospheric CO2", True),
        ("Ocean Carbon Absorption", "The rate at which the ocean dissolves and stores atmospheric CO2 — the ocean currently absorbs about 25% of human emissions but this capacity decreases as water temperature and acidity increase", False),
        ("Terrestrial Carbon Storage", "The amount of carbon held in forests, soils, and permafrost — deforestation and warming reduce storage capacity while reforestation and soil restoration can increase it", False),
        ("Global Temperature Anomaly", "The deviation of global average surface temperature from the pre-industrial baseline — currently approximately 1.2 degrees Celsius above baseline and rising at about 0.2 degrees per decade", False),
        ("Ice-Albedo Feedback", "The self-reinforcing cycle where warming melts reflective ice and snow, exposing darker ocean or land surfaces that absorb more solar energy, causing additional warming and more melting", False),
        ("Permafrost Methane Release", "The emission of methane and CO2 from thawing Arctic permafrost — a massive carbon reservoir containing roughly twice the carbon currently in the atmosphere that becomes an additional emission source as it thaws", False)
    ],
    "think_about_it": "When Fossil Fuel Emissions increase Atmospheric CO2, and higher temperatures trigger Ice-Albedo Feedback and Permafrost Methane Release, what happens to Global Temperature Anomaly even if emissions stop? Why is this different from a simple cause-and-effect relationship?",
    "scenarios": [
        ("Business As Usual", "Keep Fossil Fuel Emissions at current rates for 30 years — observe how Atmospheric CO2, Global Temperature Anomaly, and feedback loops respond over time and whether the system reaches any tipping points"),
        ("Immediate Net Zero", "Set Fossil Fuel Emissions to zero instantly — observe whether Global Temperature Anomaly stabilizes, decreases, or continues rising due to feedback loops and thermal inertia already locked into the system"),
        ("Gradual Reduction Plus Sinks", "Reduce Fossil Fuel Emissions by 50% while increasing Terrestrial Carbon Storage — observe whether enhanced carbon sinks can offset remaining emissions and slow feedback loops")
    ],
    "sim_scenarios": [
        ("Business As Usual", "Fossil Fuel Emissions: Current Rate | Ocean Absorption: Declining | Terrestrial Storage: Declining", "If emissions continue at current rates for 30 years, what do you predict happens to Global Temperature Anomaly and when do feedback loops become self-sustaining?"),
        ("Immediate Net Zero", "Fossil Fuel Emissions: Zero | Ocean Absorption: Current | Terrestrial Storage: Current", "If all emissions stopped today, would Global Temperature Anomaly immediately decrease, slowly decrease, stay the same, or continue rising? Explain your reasoning."),
        ("Enhanced Sinks Strategy", "Fossil Fuel Emissions: 50% Reduction | Ocean Absorption: Current | Terrestrial Storage: Increased 30%", "Can increasing natural carbon sinks compensate for continued partial emissions? What does the model show about the timeline?")
    ],
    "discoveries": [
        "Even with immediate elimination of all fossil fuel emissions, Global Temperature Anomaly continues rising for decades due to thermal inertia in the ocean and activated feedback loops — the climate system has significant lag time",
        "Positive feedback loops like Ice-Albedo Feedback and Permafrost Methane Release can become self-sustaining once triggered, meaning they continue driving warming independently of human emissions",
        "Ocean Carbon Absorption decreases as ocean temperature and acidity increase, creating another positive feedback loop — warmer oceans absorb less CO2 which increases warming which further reduces absorption",
        "Combining emission reductions with enhanced carbon sinks produces the most favorable outcomes, but even the best scenarios show continued warming for 20-40 years before stabilization — there is no instant fix"
    ],
    "answer": "Climate change is partially but not fully reversible on human timescales. Even if humanity achieved net-zero emissions immediately, the climate would continue warming for decades because of thermal inertia — heat already absorbed by the ocean — and activated feedback loops like ice-albedo reduction and permafrost thaw. Some changes, like Arctic sea ice loss and permafrost carbon release, may represent tipping points that are effectively irreversible for centuries. However, aggressive emission reductions combined with enhanced natural and technological carbon sinks can prevent the worst outcomes and eventually stabilize temperatures. The key finding is that delay has compounding costs — every year of continued high emissions pushes us closer to tipping points that remove human control over the trajectory of warming.",
    "stem_title": "Design a Regional Climate Resilience Plan",
    "stem_mission": "Design a comprehensive climate action plan for a specific region that combines emission reduction, carbon sequestration, and adaptation strategies based on your model\\'s predictions about feedback loops and tipping points.",
    "stem_scenario": "A coastal city of 500,000 people faces multiple climate threats: sea level rise from ice sheet melting, increased storm intensity from warmer ocean temperatures, reduced water supply from changing precipitation patterns, and heat waves that exceed historical records. The city council has commissioned your team to design a 30-year climate resilience plan that addresses both mitigation (reducing emissions) and adaptation (preparing for impacts that are already locked in). Your plan must be scientifically grounded in the carbon cycle dynamics and tipping point analysis from your model.",
    "stem_questions": [
        "Based on your model, which climate impacts are already locked in regardless of emission reductions, and which can still be prevented?",
        "How do feedback loops affect the timeline for when the city will experience the most severe impacts?",
        "What does your model suggest about the relative effectiveness of emission reduction versus carbon sequestration for this region?"
    ],
    "stem_design_qs": [
        "What specific emission reduction targets does your plan set, and what evidence from your model supports these targets?",
        "How does your plan address the irreversible changes that are already locked in due to thermal inertia and feedback loops?",
        "What natural and technological carbon sinks does your plan incorporate, and what is their projected impact?",
        "How does your plan prioritize actions that prevent tipping points from being crossed?"
    ],
    "career": "Climate scientists and atmospheric researchers study Earth\\'s climate systems, build predictive models, and analyze data from satellites, ice cores, and ocean sensors. They work at NASA, NOAA, universities, and private research firms, earning $70,000-$140,000/year. Climate policy analysts who translate scientific findings into actionable government and corporate strategies earn $65,000-$130,000/year. Carbon market analysts and sustainability consultants earn $75,000-$150,000/year in the rapidly growing green economy.",
    "images": {
        "cover": ("G12L2-L01-cover.png", "A photorealistic image of diverse 17-18 year old students examining a large interactive digital display showing global temperature anomaly maps and carbon cycle diagrams in a modern science laboratory, dramatic lighting highlighting their focused expressions"),
        "landscape": ("G12L2-L01-landscape.png", "A photorealistic wide shot of a glacier terminus meeting the ocean with visible meltwater streams, juxtaposed with a lush green forest in the foreground, showing the contrast between carbon sources and sinks in the Earth system"),
        "modeling": ("G12L2-L01-modeling.png", "A photorealistic image of diverse 17-18 year old students working collaboratively on laptops building carbon cycle models, with projected climate data visualizations on a smartboard behind them, modern science classroom"),
        "discussion": ("G12L2-L01-discussion.png", "A photorealistic image of a teacher leading an engaged discussion with diverse 17-18 year old students about climate tipping points, with a diagram of feedback loops displayed on screen, students raising hands and debating"),
        "stem": ("G12L2-L01-stem.png", "A photorealistic image of diverse 17-18 year old students working in teams around large poster boards designing climate resilience plans, with maps, graphs, and data printouts spread across their tables")
    },
    "pre_assessment": [
        "What do you think would happen to global temperatures if all fossil fuel burning stopped tomorrow? Would temperatures drop immediately, stay the same, or keep rising?",
        "Can you explain what a feedback loop is? Can you give an example from any system you know about?",
        "Where does the carbon go when you burn gasoline in a car? Trace the carbon atoms through the system.",
        "Do you think climate change can be reversed? What would it take, and how long do you think it would require?"
    ],
    "extend_components": [
        ("Aerosol Masking Effect", "The temporary cooling caused by sulfate aerosols from industrial pollution that reflect sunlight — paradoxically, reducing air pollution unmasks additional warming that was being hidden, meaning cleaner air initially increases temperatures"),
        ("Deep Ocean Circulation", "The global thermohaline conveyor belt that distributes heat and dissolved carbon through ocean basins over centuries — disruption of this circulation by freshwater from melting ice sheets could dramatically alter regional climates"),
        ("Methane Clathrate Stability", "Frozen methane deposits on the ocean floor and in permafrost that become unstable as temperatures rise — the potential release of this massive methane reservoir represents one of the most concerning climate tipping points")
    ],
    "reflections": [
        "How does your model demonstrate that the relationship between emissions and temperature is not a simple linear cause-and-effect but involves delays, feedbacks, and thresholds?",
        "Why do positive feedback loops make climate change harder to reverse than it was to start? Use specific examples from your model.",
        "What does the concept of thermal inertia mean for policy decisions being made today? Why does delay matter so much?",
        "How would you explain to someone who says \\'it\\'s too late to do anything\\' that while some changes are irreversible, action still matters enormously?",
        "What are the limitations of your seven-component model for representing the full complexity of the global climate system?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop computational models of the carbon cycle to predict how changes in emissions, absorption, and feedback loops affect global temperature trajectories over decades."),
        ("Disciplinary Core Idea", "ESS3.D Global Climate Change", "Human activities are responsible for the increase in greenhouse gases, and the resulting climate change has significant consequences for Earth systems including feedback mechanisms that can accelerate warming beyond initial forcing."),
        ("Crosscutting Concept", "Stability and Change", "Students analyze how the climate system can shift from a relatively stable state to a new equilibrium through positive feedback loops and tipping points, and evaluate the conditions under which stability can be maintained or restored.")
    ],
    "cast_items": [
        "Model how carbon flows between Earth system reservoirs and how human activities have altered these flows",
        "Predict the trajectory of global temperature change under different emission scenarios accounting for feedback loops and thermal inertia",
        "Evaluate the effectiveness of combined mitigation and adaptation strategies using evidence from climate system models"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student\\'s climate model shows that even after reducing fossil fuel emissions to zero, Global Temperature Anomaly continues rising for 25 years before stabilizing. Which component of the model best explains this continued warming? A) Increased fossil fuel emissions B) Thermal inertia and activated feedback loops C) Decreased solar output D) Volcanic activity"),
        ("Constructed Response:", "Using your carbon cycle model, explain why a 50% reduction in emissions is not expected to produce a 50% reduction in warming. Reference at least three components and one feedback loop from your model in your explanation.")
    ],
    "background_intro": "The global carbon cycle is one of Earth\\'s most fundamental biogeochemical processes, moving approximately 200 gigatons of carbon between the atmosphere, ocean, biosphere, and lithosphere each year. For millions of years, these flows were roughly balanced, maintaining atmospheric CO2 between 180 and 280 parts per million. Since the Industrial Revolution, human activities have added an additional 36 gigatons of CO2 per year, overwhelming the natural cycle and driving atmospheric concentrations past 424 ppm — the highest level in at least 800,000 years.",
    "background_sections": [
        ("The Carbon Cycle: Natural Balance Disrupted", "Earth\\'s carbon cycle operates on multiple timescales. The fast carbon cycle involves photosynthesis, respiration, and ocean gas exchange, moving carbon between the atmosphere and biosphere on timescales of days to decades. The slow carbon cycle involves geological processes like weathering, sedimentation, and volcanism that operate over millions of years. Fossil fuels represent carbon that was removed from the fast cycle and stored geologically over hundreds of millions of years. By burning fossil fuels, humans are reintroducing this stored carbon into the fast cycle at a rate roughly 100 times faster than natural geological processes — essentially compressing millions of years of carbon release into a few centuries."),
        ("Feedback Loops: Why Warming Amplifies Itself", "The climate system contains multiple positive feedback loops that amplify initial warming. The ice-albedo feedback is the most visually dramatic: as Arctic sea ice melts, the reflective white surface is replaced by dark ocean water that absorbs 94% of incoming solar radiation instead of reflecting 80% of it, causing additional warming. Permafrost feedback is potentially the most dangerous: Arctic permafrost contains an estimated 1,500 gigatons of carbon — roughly twice the total carbon in the atmosphere — and as it thaws, microbial decomposition releases CO2 and methane, a greenhouse gas 80 times more potent than CO2 over 20 years. Water vapor feedback amplifies warming by approximately 50%: warmer air holds more water vapor, which is itself a greenhouse gas."),
        ("Tipping Points: Thresholds of No Return", "Climate tipping points are critical thresholds beyond which a system shifts irreversibly to a new state. Scientists have identified several potential tipping points: collapse of the West Antarctic Ice Sheet (committed to 3-5 meters of sea level rise once triggered), dieback of the Amazon rainforest (converting the world\\'s largest carbon sink into a carbon source), shutdown of the Atlantic Meridional Overturning Circulation (dramatically cooling Europe while warming the tropics), and widespread permafrost collapse. Current warming of 1.2 degrees Celsius may have already committed some of these tipping points. Research published in Science in 2022 concluded that several tipping points become likely between 1.5 and 2.0 degrees of warming — the targets of the Paris Agreement."),
        ("Carbon Sinks and the Race Against Time", "Natural carbon sinks currently remove about 50% of human CO2 emissions — the ocean absorbs roughly 25% and land ecosystems absorb roughly 25%. However, the efficiency of these sinks is declining as temperatures rise. Warmer oceans dissolve less CO2 (just as warm soda goes flat faster than cold soda). Stressed forests from drought, fire, and heat become carbon sources rather than sinks. Technological carbon capture exists but remains extremely expensive at $250-600 per ton of CO2 and currently removes less than 0.01% of annual emissions. Nature-based solutions like reforestation, wetland restoration, and regenerative agriculture offer more cost-effective carbon removal but require massive scale to meaningfully impact atmospheric concentrations.")
    ],
    "lever_L": "Students identify Atmospheric CO2, Fossil Fuel Emissions, Ocean Carbon Absorption, Terrestrial Carbon Storage, Global Temperature Anomaly, Ice-Albedo Feedback, and Permafrost Methane Release as key components of the climate system.",
    "lever_E": "Students determine that fossil fuel emissions drive atmospheric CO2 increases, that temperature anomaly triggers self-reinforcing feedback loops, and that ocean and terrestrial sinks have limited and declining capacity to absorb excess carbon.",
    "lever_V": "Students build a computational model showing how carbon flows between reservoirs, how feedback loops amplify warming, and how tipping points create irreversible shifts in the climate system.",
    "lever_Ev": "Students run business-as-usual, immediate net-zero, and enhanced sinks scenarios to test predictions about the reversibility of climate change under different intervention strategies.",
    "lever_R": "Students add aerosol masking, deep ocean circulation, or methane clathrate components to explore how additional processes affect climate trajectories and tipping point risks.",
    "slides_guide": [
        {
            "num": "Slide 1",
            "title": "Cover",
            "visual": "Title slide with striking image of Earth showing climate data overlays — temperature anomalies, ice extent, CO2 concentration",
            "say": "Today we\\'re investigating the biggest question in environmental science: Is Climate Change Reversible? By the end of class, you\\'ll have model-based evidence to answer this.",
            "do": "Show cover image. Quick poll: Thumbs up if you think climate change is reversible, thumbs down if not, sideways if unsure. Note the distribution.",
            "time": "2 min"
        },
        {
            "num": "Slide 2",
            "title": "Learning Objectives",
            "visual": "Four learning objectives displayed with carbon cycle vocabulary terms highlighted",
            "say": "Here are our four objectives. Notice we\\'re not just learning what climate change is — we\\'re modeling the system dynamics that determine whether it can be reversed.",
            "do": "Have students read objectives aloud. Pre-teach vocabulary: carbon flux, positive feedback loop, tipping point, carbon sink. Use the warm soda analogy for ocean absorption.",
            "time": "3 min"
        },
        {
            "num": "Slide 3",
            "title": "Big Question",
            "visual": "Provocative question displayed over image of melting glacier alongside thriving forest",
            "say": "If we stopped all emissions tomorrow, would the planet cool back down? This is not a simple yes-or-no question — it depends on feedback loops and tipping points we\\'re about to model.",
            "do": "Quick-write: Students write their initial prediction and reasoning in 2-3 sentences. They\\'ll revisit this after modeling.",
            "time": "3 min"
        },
        {
            "num": "Slide 4",
            "title": "LEVER Framework",
            "visual": "LEVER steps overview with climate-specific examples for each step",
            "say": "We\\'ll use the LEVER framework to build a computational model of the carbon cycle. This model will let us test different emission scenarios and see which ones prevent tipping points.",
            "do": "Preview each LEVER step. Emphasize that modeling lets us test scenarios we can\\'t experiment with in real life — we only have one Earth.",
            "time": "2 min"
        },
        {
            "num": "Slide 5",
            "title": "Activity 1: Components",
            "visual": "Seven component cards displayed for sorting: Atmospheric CO2, Fossil Fuel Emissions, Ocean Carbon Absorption, Terrestrial Carbon Storage, Global Temperature Anomaly, Ice-Albedo Feedback, Permafrost Methane Release",
            "say": "Which of these components are inputs from outside the climate system, and which are internal responses? Think about what drives the system versus what the system produces.",
            "do": "Guide sorting: External = Atmospheric CO2 (set by cumulative emissions), Fossil Fuel Emissions (human decision). Internal = the rest. Use think-pair-share for reasoning about borderline cases.",
            "time": "8 min"
        },
        {
            "num": "Slide 6",
            "title": "Activity 2: Connections",
            "visual": "Arrow diagram template showing the seven components with space for students to draw positive and negative relationships",
            "say": "When Fossil Fuel Emissions increase, what happens to Atmospheric CO2? When temperature rises, what happens to Ice-Albedo Feedback? Look for loops where effects cycle back to amplify the original cause.",
            "do": "Students draw arrows with + or - signs. Facilitate discovery of positive feedback loops. Ask: Where do you see a cycle that keeps reinforcing itself?",
            "time": "8 min"
        },
        {
            "num": "Slide 7",
            "title": "Activity 3: Simulation",
            "visual": "Simulation interface showing three scenarios with graphs of CO2, temperature, and feedback strength over time",
            "say": "Now we test our model. Run all three scenarios and watch carefully — the business-as-usual scenario may shock you, and the net-zero scenario will challenge your assumptions.",
            "do": "Students run each scenario, record predictions versus observations. Key discussion: Why does temperature keep rising even after emissions hit zero? This is the critical insight.",
            "time": "10 min"
        },
        {
            "num": "Slide 8",
            "title": "Discoveries",
            "visual": "Four key discoveries displayed with supporting graphs from simulation results",
            "say": "So is climate change reversible? Partially — and the answer depends on how quickly we act. Let\\'s look at what our model revealed about feedback loops, tipping points, and the cost of delay.",
            "do": "Class discussion of discoveries. Have students compare their initial predictions to model evidence. Key question: What surprised you most?",
            "time": "5 min"
        },
        {
            "num": "Slide 9",
            "title": "STEM Challenge",
            "visual": "Engineering challenge brief: Design a Regional Climate Resilience Plan for a coastal city of 500,000",
            "say": "Now apply your model knowledge. Your city faces sea level rise, stronger storms, water scarcity, and heat waves. Some of these are already locked in. Design a plan that addresses both prevention and preparation.",
            "do": "Groups design 30-year climate resilience plans using model data. Must address both mitigation and adaptation. Present key strategies and justify with evidence from simulations.",
            "time": "12 min"
        }
    ],
    "sort_reasoning": "Atmospheric CO2 and Fossil Fuel Emissions are external components because they represent inputs that drive the climate system — CO2 concentration is determined by the cumulative balance of emissions and absorption, and Fossil Fuel Emissions are a human-controlled input. Ocean Carbon Absorption, Terrestrial Carbon Storage, Global Temperature Anomaly, Ice-Albedo Feedback, and Permafrost Methane Release are internal because they are responses generated within the Earth system as it processes the external forcing — they change as a consequence of the inputs and interact with each other through feedback loops.",
    "relationships": [
        ("Fossil Fuel Emissions to Atmospheric CO2", "POSITIVE (+)", "Burning fossil fuels releases stored carbon into the atmosphere, directly increasing CO2 concentration. Higher emission rates produce faster CO2 accumulation."),
        ("Atmospheric CO2 to Global Temperature Anomaly", "POSITIVE (+)", "Higher atmospheric CO2 strengthens the greenhouse effect, trapping more outgoing infrared radiation and increasing global average surface temperature."),
        ("Global Temperature Anomaly to Ice-Albedo Feedback", "POSITIVE (+)", "Higher temperatures melt reflective ice and snow, exposing darker surfaces that absorb more solar energy, which drives additional warming in a self-reinforcing loop."),
        ("Global Temperature Anomaly to Permafrost Methane Release", "POSITIVE (+)", "Higher temperatures thaw Arctic permafrost, releasing stored methane and CO2 that further increase atmospheric greenhouse gas concentrations and drive additional warming."),
        ("Global Temperature Anomaly to Ocean Carbon Absorption", "NEGATIVE (-)", "Warmer ocean water dissolves less CO2, reducing the ocean\\'s capacity as a carbon sink. This means a larger fraction of emissions remains in the atmosphere, accelerating warming."),
        ("Terrestrial Carbon Storage to Atmospheric CO2", "NEGATIVE (-)", "Healthy forests and soils absorb CO2 from the atmosphere through photosynthesis and storage, reducing atmospheric concentration. Deforestation or ecosystem degradation reverses this relationship.")
    ],
    "sim_answers": [
        ("Business As Usual", "With emissions continuing at current rates, Atmospheric CO2 rises rapidly past 500 ppm within 30 years. Global Temperature Anomaly exceeds 2 degrees Celsius, triggering strong Ice-Albedo Feedback and significant Permafrost Methane Release. These feedback loops become partially self-sustaining, meaning warming continues to accelerate even beyond what emissions alone would cause. Ocean Carbon Absorption declines as water warms, creating an additional positive feedback."),
        ("Immediate Net Zero", "Even with emissions instantly reduced to zero, Global Temperature Anomaly continues rising for approximately 20-30 years due to thermal inertia — heat already absorbed by the ocean gradually releases to the atmosphere. Feedback loops that have already been activated (partial ice-albedo, some permafrost thaw) continue contributing to warming for decades. Temperature eventually stabilizes but does not return to pre-industrial levels within the simulation timeframe, demonstrating that some warming is effectively locked in."),
        ("Enhanced Sinks Strategy", "Reducing emissions by 50% while increasing Terrestrial Carbon Storage slows the rate of CO2 accumulation but does not stop it. The enhanced sinks partially offset remaining emissions, and the rate of temperature increase slows significantly. Feedback loops are weaker than in the business-as-usual scenario but still active. This scenario shows stabilization is possible but requires decades and does not reverse changes already underway.")
    ],
    "reflection_exemplars": [
        ("Why does temperature keep rising even after emissions stop?", "The model demonstrates two key reasons. First, thermal inertia: the ocean has absorbed enormous amounts of heat that gradually releases back to the atmosphere over decades, like a hot water bottle slowly warming a bed. Second, activated feedback loops: once Ice-Albedo Feedback and Permafrost Methane Release are triggered, they generate their own warming independent of human emissions. The ice that has already melted exposes dark ocean that absorbs heat, and the permafrost that has already thawed releases methane for years. These processes have momentum that cannot be instantly stopped, which is why climate scientists emphasize that every fraction of a degree matters — the further we push, the stronger these self-reinforcing cycles become."),
        ("Why does delay matter so much in climate action?", "Our model shows that delay has compounding costs because of positive feedback loops. Each year of high emissions not only adds more CO2 to the atmosphere but also pushes the system closer to tipping points where feedback loops become self-sustaining. Once a tipping point is crossed — say, widespread permafrost collapse — the system generates its own emissions regardless of human behavior. The difference between acting now and acting in 10 years is not just 10 years of additional emissions; it is the difference between keeping feedback loops manageable and potentially triggering irreversible cascades. The model clearly shows that early action has disproportionately large benefits compared to delayed action of the same magnitude.")
    ],
    "stem_intro": "Present the challenge: A coastal city of 500,000 people needs a 30-year climate resilience plan. Using your model data, identify which impacts are already locked in (requiring adaptation) and which can still be prevented (requiring mitigation). Design a comprehensive plan that addresses both, with specific strategies justified by your simulation results about feedback loops and tipping points.",
    "stem_concepts": [
        ("Climate Mitigation vs. Adaptation", "Mitigation reduces the cause of climate change by cutting emissions and enhancing carbon sinks. Adaptation prepares for impacts that are already locked in. Both are essential because thermal inertia and feedback loops mean some warming is unavoidable even under aggressive mitigation. A good climate plan integrates both strategies based on what the science says is preventable versus inevitable."),
        ("Nature-Based Solutions", "Using natural ecosystems to sequester carbon and buffer climate impacts — including reforestation, wetland restoration, mangrove protection, and regenerative agriculture. These solutions are cost-effective ($10-100 per ton of CO2 compared to $250-600 for technological capture) and provide co-benefits like biodiversity, water filtration, and flood protection, but require large areas and long timeframes to reach full effectiveness."),
        ("Climate Justice and Equitable Planning", "Climate impacts disproportionately affect low-income communities and communities of color who have contributed least to emissions. Effective resilience planning must prioritize the most vulnerable populations, ensure equitable distribution of resources, and avoid solutions that shift burdens from wealthy to disadvantaged communities. Environmental justice requires that those most affected have the strongest voice in planning.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan integrates both mitigation and adaptation with specific strategies justified by model evidence, addresses feedback loops and tipping points, includes equitable implementation, and provides a realistic timeline based on simulation results"),
        ("Proficient (3)", "Plan addresses both mitigation and adaptation with reasonable strategies and some connection to model data, includes consideration of feedback loops"),
        ("Developing (2)", "Plan addresses either mitigation or adaptation but not both, or strategies are vague and weakly connected to model evidence"),
        ("Beginning (1)", "Plan is incomplete, lacks scientific grounding, or does not connect strategies to carbon cycle dynamics from the model")
    ],
    "support": [
        "Provide a simplified carbon cycle diagram with arrows already labeled showing the direction of carbon flow between reservoirs — students fill in whether each flow increases or decreases with warming",
        "Use a physical analogy: a bathtub with the faucet running (emissions) and the drain partially open (sinks) — when does the tub overflow (tipping point)? What happens when you turn off the faucet but the drain is clogged?",
        "Sentence frames: \\'When ___ increases, it causes ___ to ___ because ___. This creates a feedback loop because the effect then ___.\\'"
    ],
    "extensions": [
        "Research the concept of carbon budgets — how much CO2 can humanity still emit while staying below 1.5 or 2.0 degrees Celsius? Calculate how many years of current emissions this represents and evaluate whether current national pledges are sufficient.",
        "Investigate the potential for marine carbon dioxide removal through ocean alkalinity enhancement — how does changing ocean chemistry affect CO2 absorption, and what are the ecological risks?",
        "Analyze paleoclimate data from ice cores and sediment records to identify past tipping points in Earth\\'s climate history and compare the rate of current change to the fastest natural climate shifts in the geological record."
    ],
    "cross_curr": [
        ("Math", "Use exponential growth models to calculate CO2 accumulation under different emission scenarios and determine the mathematical conditions under which feedback loops produce runaway warming versus stabilization."),
        ("ELA", "Read and analyze competing op-eds about climate policy — one arguing for immediate aggressive action and one arguing for gradual transition. Evaluate how each author uses (or misuses) scientific evidence about tipping points and feedback loops."),
        ("History", "Research the history of international climate negotiations from the 1992 Rio Earth Summit to the Paris Agreement. Analyze why scientific consensus has not translated into proportional policy action and what factors have delayed response.")
    ],
    "misconceptions": [
        ("Climate change will stop as soon as we stop emitting CO2", "Due to thermal inertia (the ocean has absorbed decades of excess heat) and activated feedback loops (ice-albedo, permafrost thaw), warming continues for 20-40 years after emissions cease. Some changes like ice sheet melting may continue for centuries. This does not mean action is pointless — stopping emissions prevents additional tipping points from being crossed — but it does mean there is a time lag between action and result.", "Use the model to show the net-zero scenario: students can see temperature continue rising after emissions drop to zero. Ask: Why? Guide them to identify thermal inertia and self-sustaining feedback loops as the explanation."),
        ("The ocean will keep absorbing our CO2 indefinitely", "The ocean\\'s CO2 absorption capacity decreases with temperature and increasing acidity. Warmer water dissolves less gas (like how warm soda goes flat), and acidification from absorbed CO2 is already disrupting marine chemistry. The ocean currently absorbs about 25% of emissions, but models project this fraction will decline as warming continues, turning a brake on warming into a weaker and weaker buffer.", "Demonstrate with a warm versus cold glass of carbonated water — students can see and hear that warm water holds less dissolved gas. Connect to the model: as temperature rises, ocean absorption declines."),
        ("Individual actions like recycling can solve climate change", "While individual actions matter for building cultural momentum, the scale of the climate challenge is systemic. Individual consumer choices account for a small fraction of global emissions compared to industrial, energy, and transportation systems. Solving climate change requires systemic policy changes — carbon pricing, renewable energy mandates, industrial regulation, and international cooperation. The model shows that only large-scale changes to Fossil Fuel Emissions and Terrestrial Carbon Storage produce meaningful changes in temperature trajectories.", "Show students the relative scale: a person recycling saves perhaps 0.5 tons of CO2 per year; total global emissions are 36 billion tons. Ask: How many individual actions would it take to match one policy change that shifts an entire energy grid?")
    ]
}

L02 = {
    "id": "G12L2-L02",
    "title": "Why Are Coral Reefs Dying?",
    "subtitle": "Modeling Ocean Acidification, Thermal Bleaching, and Ecosystem Collapse",
    "ngss": "HS-LS2-6",
    "ngss_desc": "Evaluate claims, evidence, and reasoning that the complex interactions in ecosystems maintain relatively consistent numbers and types of organisms in stable conditions, but changing conditions may result in a new ecosystem.",
    "big_question": "Coral reefs support 25% of all marine species but cover less than 1% of the ocean floor — so what happens to a quarter of ocean life when rising temperatures and acidification push these irreplaceable ecosystems past their breaking point?",
    "objectives": [
        "Model how ocean temperature, pH, and coral-algae symbiosis interact to determine coral reef health and resilience",
        "Explain the mechanism of coral bleaching and why repeated bleaching events prevent recovery",
        "Predict the threshold conditions under which reef ecosystems shift from coral-dominated to algae-dominated states",
        "Analyze the cascading effects of reef collapse on marine food webs, coastal protection, and human communities"
    ],
    "vocabulary": [
        ("Ocean Acidification", "The decrease in ocean pH caused by absorption of atmospheric CO2 — seawater reacts with dissolved CO2 to form carbonic acid, which reduces the availability of carbonate ions that corals and shellfish need to build their calcium carbonate skeletons"),
        ("Coral Bleaching", "The stress response in which corals expel their symbiotic zooxanthellae algae when water temperatures exceed their tolerance threshold — the loss of these colorful algae reveals the white calcium carbonate skeleton and deprives the coral of up to 90% of its energy"),
        ("Zooxanthellae", "Microscopic photosynthetic algae that live inside coral tissue in a mutualistic symbiosis — they provide up to 90% of the coral\\'s energy through photosynthesis and give coral its color, while the coral provides shelter and nutrients"),
        ("Phase Shift", "An ecological regime change in which a coral reef transitions from a coral-dominated state to an algae-dominated state — once this shift occurs, positive feedback loops make it very difficult for coral to reestablish, effectively locking in a degraded ecosystem")
    ],
    "components": [
        ("Sea Surface Temperature", "The temperature of the upper ocean layer where corals live — even 1-2 degrees Celsius above the normal summer maximum can trigger mass bleaching events, and marine heat waves are becoming more frequent and intense", True),
        ("Ocean pH Level", "The acidity of seawater determined by dissolved CO2 concentration — ocean pH has already dropped from 8.2 to 8.1 since pre-industrial times, representing a 26% increase in acidity that reduces carbonate availability for skeleton building", True),
        ("Coral-Zooxanthellae Symbiosis", "The health and stability of the mutualistic relationship between coral polyps and their photosynthetic algae — this symbiosis provides the energy foundation for the entire reef ecosystem and breaks down under thermal stress", False),
        ("Coral Calcification Rate", "The speed at which corals build their calcium carbonate skeletons — decreases with ocean acidification because lower pH reduces carbonate ion concentration, and weakened skeletons are more vulnerable to storm damage and bioerosion", False),
        ("Reef Biodiversity Index", "The diversity and abundance of species that depend on the coral reef structure — declines as coral cover decreases because reef structure provides habitat, nursery areas, and feeding grounds for thousands of species", False),
        ("Algae Overgrowth", "The proliferation of macroalgae that competes with coral for space on the reef — increases when coral dies or weakens, creating a positive feedback loop where algae prevent coral larvae from settling and recovering", False),
        ("Herbivore Fish Population", "The abundance of parrotfish, surgeonfish, and other algae-eating reef fish — these fish control algae growth and maintain conditions favorable for coral, but overfishing has reduced their populations on many reefs worldwide", False)
    ],
    "think_about_it": "When Sea Surface Temperature rises and causes bleaching that weakens Coral-Zooxanthellae Symbiosis, what happens to Algae Overgrowth? If Herbivore Fish Population is also declining due to overfishing, can the reef recover? Where are the feedback loops?",
    "scenarios": [
        ("Moderate Warming Scenario", "Increase Sea Surface Temperature by 1 degree Celsius above the summer maximum with current Ocean pH — observe how the coral-algae symbiosis responds and whether the reef can recover between bleaching events"),
        ("Acidification Plus Warming", "Increase Sea Surface Temperature by 1.5 degrees while decreasing Ocean pH to 7.9 — observe the combined stress on calcification and symbiosis and whether tipping points are reached"),
        ("Managed Reef Scenario", "Apply moderate warming but maintain high Herbivore Fish Population — observe whether healthy fish populations can buffer the reef against phase shifts by controlling algae overgrowth")
    ],
    "sim_scenarios": [
        ("Moderate Warming", "Sea Surface Temperature: +1C Above Max | Ocean pH: 8.1 (Current) | Herbivore Fish: Current", "When temperature rises moderately with one bleaching event, can the reef recover fully before the next event? What determines recovery time?"),
        ("Double Stress", "Sea Surface Temperature: +1.5C Above Max | Ocean pH: 7.9 | Herbivore Fish: Current", "What happens when corals face both thermal stress and acidification simultaneously? Which stress is more damaging?"),
        ("Managed Resilience", "Sea Surface Temperature: +1C Above Max | Ocean pH: 8.1 | Herbivore Fish: High (Protected)", "Can maintaining healthy herbivore populations through fishing regulations help reefs survive moderate warming? What does this suggest about management strategies?")
    ],
    "discoveries": [
        "Coral bleaching becomes lethal not from a single event but from repeated events that prevent full recovery — the model shows that recovery requires 10-15 years of stable conditions, but bleaching events are now occurring every 2-3 years",
        "Ocean acidification and warming create a compounding double stress — acidification weakens coral skeletons while warming disrupts the symbiosis, and the combined effect is worse than either stressor alone",
        "Phase shifts from coral to algae dominance involve positive feedback loops — dead coral provides substrate for algae, algae smother surviving coral larvae, and reduced reef structure drives away herbivorous fish that would otherwise control algae",
        "Maintaining healthy herbivore fish populations significantly increases reef resilience by controlling algae overgrowth and giving coral time to recover between stress events — local management can buy time even as global stressors increase"
    ],
    "answer": "Coral reefs are dying because they face an unprecedented combination of stressors that overwhelm their capacity to recover. Rising ocean temperatures trigger mass bleaching events that break the symbiosis between corals and the zooxanthellae algae that provide 90% of their energy. Ocean acidification simultaneously weakens coral skeletons by reducing the carbonate ions corals need for calcification. The critical problem is frequency: bleaching events that once occurred every 25-30 years now happen every 2-3 years, leaving no time for recovery. When coral dies, algae quickly colonize the space and create positive feedback loops that prevent coral from returning — a phase shift that locks in ecosystem degradation. The cascading effects are devastating: 25% of all marine species depend on reefs, coastal communities lose storm protection and fisheries, and the economic losses exceed $375 billion per year. Local management of fishing and pollution can increase resilience, but ultimately, saving coral reefs requires addressing the global causes — carbon emissions and the warming and acidification they drive.",
    "stem_title": "Design a Coral Reef Rescue Strategy",
    "stem_mission": "Design a multi-scale intervention plan that combines local reef management with global advocacy to maximize the survival chances of a threatened coral reef ecosystem.",
    "stem_scenario": "A Caribbean coral reef that once supported a thriving fishing community has lost 60% of its coral cover in the past 15 years due to repeated bleaching events, overfishing of herbivorous fish, and nutrient pollution from coastal development. The remaining coral is weakened, algae coverage is increasing rapidly, and the local fishing industry is collapsing. A marine conservation organization has hired your team to design a rescue plan that addresses both immediate local threats and long-term global stressors. Your plan must be scientifically grounded in the reef dynamics your model revealed.",
    "stem_questions": [
        "Based on your model, which local stressors can be addressed immediately to buy the reef time, and which global stressors require long-term systemic change?",
        "What does your model suggest about the relationship between herbivore fish populations and reef recovery potential?",
        "At what point does your model indicate a phase shift becomes irreversible, and how close is this reef to that threshold?"
    ],
    "stem_design_qs": [
        "What specific local management actions does your plan implement first, and how quickly can they take effect?",
        "How does your plan address the positive feedback loops that lock in algae dominance and prevent coral recovery?",
        "What role does coral restoration (transplanting, selective breeding for heat tolerance) play in your strategy?",
        "How does your plan account for the continued increase in ocean temperature and acidification over the next 30 years?"
    ],
    "career": "Marine biologists who specialize in coral reef ecology study the complex interactions that maintain reef health and develop conservation strategies. They work for NOAA, marine sanctuaries, universities, and conservation organizations, earning $55,000-$110,000/year. Coral restoration specialists who develop and implement reef rehabilitation techniques earn $50,000-$95,000/year. Marine policy analysts who translate reef science into fishing regulations and marine protected area designations earn $60,000-$120,000/year.",
    "images": {
        "cover": ("G12L2-L02-cover.png", "A photorealistic image of diverse 17-18 year old students examining coral specimens and marine samples in a modern marine biology laboratory, with an aquarium and reef ecosystem displays visible in the background"),
        "landscape": ("G12L2-L02-landscape.png", "A photorealistic split-view image showing a vibrant healthy coral reef teeming with fish on one side and a bleached, algae-covered degraded reef on the other side, illustrating the contrast between healthy and dying reef ecosystems"),
        "modeling": ("G12L2-L02-modeling.png", "A photorealistic image of diverse 17-18 year old students working on reef ecosystem models on their laptops, with coral reef diagrams and ocean chemistry data projected on a smartboard, modern science classroom"),
        "discussion": ("G12L2-L02-discussion.png", "A photorealistic image of a teacher leading a discussion with diverse 17-18 year old students about coral bleaching, with before-and-after reef images displayed on screen, students engaged in animated debate"),
        "stem": ("G12L2-L02-stem.png", "A photorealistic image of diverse 17-18 year old students designing coral reef rescue strategies on large poster boards with maps of reef locations, marine food web diagrams, and intervention timelines")
    },
    "pre_assessment": [
        "What do you know about coral reefs? Are they plants, animals, or something else? Where in the world do you find them?",
        "Have you heard the term coral bleaching? What do you think causes it, and why is it a problem?",
        "How do you think the health of an underwater ecosystem like a coral reef could be connected to the carbon dioxide we emit on land?",
        "Why might losing coral reefs matter to people who live nowhere near the ocean?"
    ],
    "extend_components": [
        ("Nutrient Pollution Runoff", "Excess nitrogen and phosphorus from agriculture and sewage that enter coastal waters — these nutrients fuel algae growth that smothers coral, blocks light, and consumes oxygen, adding a local stressor on top of global ocean warming and acidification"),
        ("Coral Genetic Diversity", "The range of heat-tolerance genes present in the coral population — more genetically diverse reefs have a greater chance that some individuals can survive warming events, while genetically uniform reefs face total loss from a single heat wave"),
        ("Marine Protected Area Coverage", "The percentage of the reef under legal protection from fishing, development, and pollution — protected areas maintain higher fish populations, lower nutrient pollution, and greater coral cover, increasing overall reef resilience to climate stressors")
    ],
    "reflections": [
        "How does the concept of phase shifts in reef ecosystems parallel tipping points in the climate system you learned about in the previous lesson?",
        "Why is the frequency of bleaching events more important than the severity of any single event? What does your model show about recovery time?",
        "How do local stressors like overfishing and pollution interact with global stressors like warming and acidification? Can addressing local stressors save reefs?",
        "What does the loss of a coral reef mean for the 25% of marine species that depend on it? Trace the cascading effects through the food web.",
        "What are the ethical implications of a warming world where wealthy nations that contributed most to emissions can afford reef restoration while developing nations that depend on reefs for food and income cannot?"
    ],
    "dimensions": [
        ("Science Practice", "Constructing Explanations and Designing Solutions", "Students construct evidence-based explanations for why coral reefs are dying based on their models of symbiosis breakdown, acidification, and phase shifts, and design multi-scale intervention strategies."),
        ("Disciplinary Core Idea", "LS2.C Ecosystem Dynamics, Functioning, and Resilience", "A complex set of interactions within an ecosystem can keep its numbers and types of organisms relatively constant over long periods of time under stable conditions. If a modest biological or physical disturbance to an ecosystem occurs, it may return to its more or less original status, but extreme changes may result in a very different ecosystem."),
        ("Crosscutting Concept", "Stability and Change", "Students analyze how coral reef ecosystems can absorb moderate disturbances and return to stable states, but extreme or repeated disturbances can push the system past a tipping point into a fundamentally different and degraded state.")
    ],
    "cast_items": [
        "Model the interactions between ocean temperature, pH, coral-algae symbiosis, and reef biodiversity that determine reef ecosystem health",
        "Predict the threshold conditions under which a coral reef undergoes a phase shift from coral-dominated to algae-dominated state",
        "Evaluate multi-scale intervention strategies based on model evidence about local versus global stressor management"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A coral reef has experienced three bleaching events in eight years. According to your model, why is the third event more damaging than the first even if water temperatures are similar? A) The coral has adapted to be more heat-sensitive B) Ocean acidification has worsened C) Incomplete recovery left coral weakened and algae encroachment reduced available recovery space D) Bleaching always gets worse over time regardless of conditions"),
        ("Constructed Response:", "Using your reef ecosystem model, explain why protecting herbivorous fish populations from overfishing could significantly increase a coral reef\\'s resilience to climate change. Reference at least three components and one feedback loop in your explanation.")
    ],
    "background_intro": "Coral reefs are among the most biodiverse and economically valuable ecosystems on Earth, supporting approximately 25% of all marine species while covering less than 1% of the ocean floor. These underwater rainforests are built by tiny coral polyps — animals related to jellyfish — that form a remarkable symbiosis with photosynthetic algae called zooxanthellae. This partnership has built massive limestone structures over thousands of years, but it is extraordinarily sensitive to changes in water temperature and chemistry that are now occurring at unprecedented rates.",
    "background_sections": [
        ("The Coral-Zooxanthellae Symbiosis", "Coral polyps are animals that cannot photosynthesize, yet they thrive in nutrient-poor tropical waters because of their partnership with zooxanthellae — single-celled algae that live within the coral\\'s tissue. The zooxanthellae photosynthesize using sunlight and provide up to 90% of the coral\\'s energy needs in the form of sugars and amino acids. In return, the coral provides the algae with shelter, CO2, and nutrients from its waste. This symbiosis is the engine that drives reef productivity, enabling corals to build their calcium carbonate skeletons and support the extraordinary biodiversity that makes reefs the rainforests of the sea. But this partnership has a fatal vulnerability: it breaks down when water temperature exceeds the coral\\'s tolerance threshold by even 1-2 degrees Celsius."),
        ("Bleaching: When Symbiosis Breaks Down", "When sea surface temperature exceeds the coral\\'s thermal tolerance — typically 1-2 degrees above the normal summer maximum — the zooxanthellae begin producing toxic reactive oxygen species instead of beneficial sugars. The coral responds by expelling its algal partners, revealing the white calcium carbonate skeleton beneath — this is bleaching. A bleached coral is not dead but is starving, surviving on stored energy reserves for 4-8 weeks. If temperatures return to normal within this window, the coral can reacquire zooxanthellae and recover, though it remains weakened for months. If high temperatures persist or return too quickly, the coral dies. The critical problem is frequency: the Great Barrier Reef experienced mass bleaching in 1998, 2002, 2016, 2017, 2020, 2022, and 2024 — recovery requires 10-15 years of stable conditions that no longer exist."),
        ("Ocean Acidification: The Other CO2 Problem", "While atmospheric CO2 drives warming through the greenhouse effect, dissolved CO2 directly alters ocean chemistry. When CO2 dissolves in seawater, it forms carbonic acid, releasing hydrogen ions that lower pH and binding with carbonate ions to form bicarbonate. This reduces the concentration of carbonate ions that corals, shellfish, and many marine organisms need to build calcium carbonate structures. Ocean pH has already dropped from 8.2 to 8.1 since pre-industrial times — a 26% increase in acidity that sounds small but is logarithmic. Under current emission trajectories, ocean pH could drop to 7.8 by 2100, representing a 150% increase in acidity from pre-industrial levels. At this pH, coral reefs dissolve faster than they can grow, and many marine organisms cannot form shells or skeletons."),
        ("Phase Shifts: The Point of No Return", "When coral cover drops below a critical threshold — typically around 10-20% — the reef undergoes a phase shift to an algae-dominated state. This shift involves multiple positive feedback loops: dead coral provides substrate for algae, algae smother coral larvae preventing recolonization, reduced coral structure drives away herbivorous fish that would control algae, and the algae-dominated reef supports fewer organisms that maintain reef health. Once established, these feedback loops make the phase shift extremely difficult to reverse — removing one stressor is insufficient because the others maintain the degraded state. Studies of Caribbean reefs show that many crossed this threshold in the 1980s following disease that killed sea urchins (key herbivores), and 40 years later most have not recovered despite management efforts.")
    ],
    "lever_L": "Students identify Sea Surface Temperature, Ocean pH Level, Coral-Zooxanthellae Symbiosis, Coral Calcification Rate, Reef Biodiversity Index, Algae Overgrowth, and Herbivore Fish Population as key components of the reef ecosystem.",
    "lever_E": "Students determine that temperature and pH stress the coral-algae symbiosis, that symbiosis breakdown reduces calcification and biodiversity, that algae overgrowth creates positive feedback loops preventing recovery, and that herbivore fish populations moderate algae growth.",
    "lever_V": "Students build a computational model showing how ocean conditions affect coral health through multiple interacting pathways and identify the feedback loops that can lock reefs into degraded states.",
    "lever_Ev": "Students run moderate warming, double-stress, and managed reef scenarios to test predictions about bleaching recovery, phase shift thresholds, and the effectiveness of local management interventions.",
    "lever_R": "Students add nutrient pollution, coral genetic diversity, or marine protected area coverage to explore how additional factors affect reef resilience and recovery potential.",
    "slides_guide": [
        {
            "num": "Slide 1",
            "title": "Cover",
            "visual": "Title slide with stunning split image of healthy vibrant reef versus bleached white reef",
            "say": "Today we\\'re investigating one of the most urgent ecological crises happening right now — the death of the world\\'s coral reefs. Why are they dying, and can we save them?",
            "do": "Show cover image. Quick share: Has anyone ever seen a coral reef — in person, in a documentary, or online? What did it look like?",
            "time": "2 min"
        },
        {
            "num": "Slide 2",
            "title": "Learning Objectives",
            "visual": "Four learning objectives with coral reef vocabulary terms highlighted and illustrated",
            "say": "By the end of today, you\\'ll understand the science behind coral bleaching, ocean acidification, and why reefs can collapse permanently once they pass a tipping point.",
            "do": "Have students read objectives. Pre-teach vocabulary. Key concept: zooxanthellae — these microscopic algae are the key to everything. Use the symbiosis analogy: coral provides housing, algae pays rent in sugar.",
            "time": "3 min"
        },
        {
            "num": "Slide 3",
            "title": "Big Question",
            "visual": "Provocative question over image showing reef biodiversity and the statistic that 25% of marine species depend on 1% of the ocean floor",
            "say": "Coral reefs support a quarter of all ocean life on less than 1% of the seafloor. What happens to that quarter when the reefs die? Write your prediction.",
            "do": "Quick-write: Students write their initial prediction about cascading effects of reef loss. Save for comparison after modeling.",
            "time": "3 min"
        },
        {
            "num": "Slide 4",
            "title": "LEVER Framework",
            "visual": "LEVER steps overview with reef-specific examples for each step",
            "say": "We\\'ll build a model of the coral reef ecosystem to understand not just what\\'s happening, but why reefs can\\'t recover once they pass certain thresholds.",
            "do": "Preview each LEVER step. Emphasize that this model will reveal feedback loops — processes that make reef death self-reinforcing once they start.",
            "time": "2 min"
        },
        {
            "num": "Slide 5",
            "title": "Activity 1: Components",
            "visual": "Seven component cards for sorting with reef ecosystem illustrations",
            "say": "Which of these components are external drivers that come from outside the reef system, and which are internal responses within the reef ecosystem?",
            "do": "Guide sorting: External = Sea Surface Temperature, Ocean pH Level (driven by global processes). Internal = the five ecosystem responses. Discuss: Why is Herbivore Fish Population internal even though fishing is an external pressure?",
            "time": "8 min"
        },
        {
            "num": "Slide 6",
            "title": "Activity 2: Connections",
            "visual": "Relationship diagram template with seven reef components arranged for arrow drawing",
            "say": "When temperature rises and triggers bleaching, trace the cascade through the system. What happens to the symbiosis, then to calcification, then to biodiversity, then to algae? Look for loops.",
            "do": "Students draw arrows with + or - signs. Key discovery: the positive feedback loop between Algae Overgrowth, Coral-Zooxanthellae Symbiosis, and Herbivore Fish Population. Ask: Once this loop starts, can it stop itself?",
            "time": "8 min"
        },
        {
            "num": "Slide 7",
            "title": "Activity 3: Simulation",
            "visual": "Simulation interface showing three scenarios with graphs of coral cover, algae cover, and biodiversity over time",
            "say": "Run all three scenarios and watch what happens. Pay special attention to the managed reef scenario — it reveals something important about what we can actually do.",
            "do": "Students run each scenario, record predictions vs. observations. Key discussion: Compare the double-stress scenario to the managed scenario. What does this tell us about the value of local conservation?",
            "time": "10 min"
        },
        {
            "num": "Slide 8",
            "title": "Discoveries",
            "visual": "Four key discoveries with supporting graphs showing recovery timelines, phase shifts, and management effects",
            "say": "Our model reveals that reef death is not just about heat — it\\'s about feedback loops, recovery time, and the interaction of multiple stressors. Let\\'s discuss what this means for conservation.",
            "do": "Class discussion of discoveries. Compare initial predictions to model evidence. Key question: What surprised you about the managed reef scenario?",
            "time": "5 min"
        },
        {
            "num": "Slide 9",
            "title": "STEM Challenge",
            "visual": "Engineering challenge: Design a Coral Reef Rescue Strategy for a Caribbean reef that has lost 60% coral cover",
            "say": "Your reef is in crisis but not yet past the point of no return. Use your model data to design a rescue plan that combines local management with long-term strategy.",
            "do": "Groups design multi-scale intervention plans. Must address both local stressors (fishing, pollution) and global stressors (warming, acidification). Present strategies with evidence from model simulations.",
            "time": "12 min"
        }
    ],
    "sort_reasoning": "Sea Surface Temperature and Ocean pH Level are external components because they are driven by global atmospheric and oceanic processes beyond the reef\\'s control — the reef does not set its own temperature or pH. Coral-Zooxanthellae Symbiosis, Coral Calcification Rate, Reef Biodiversity Index, Algae Overgrowth, and Herbivore Fish Population are internal because they are properties of the reef ecosystem that respond to and interact with each other based on the external conditions — they are what the reef does with the inputs it receives.",
    "relationships": [
        ("Sea Surface Temperature to Coral-Zooxanthellae Symbiosis", "NEGATIVE (-)", "Rising temperature above the thermal tolerance triggers bleaching — corals expel their zooxanthellae algae, weakening or destroying the symbiosis that provides 90% of the coral\\'s energy."),
        ("Ocean pH Level to Coral Calcification Rate", "POSITIVE (+)", "As pH decreases (more acidic), carbonate ion concentration drops, directly slowing the rate at which corals can build and maintain their calcium carbonate skeletons. Lower pH means weaker, slower-growing reefs."),
        ("Coral-Zooxanthellae Symbiosis to Reef Biodiversity Index", "POSITIVE (+)", "Healthy symbiosis drives coral growth and reef structure complexity, which provides habitat for thousands of species. When symbiosis breaks down and coral dies, the structural foundation of biodiversity disappears."),
        ("Algae Overgrowth to Coral-Zooxanthellae Symbiosis", "NEGATIVE (-)", "Algae physically smother coral and block light needed by zooxanthellae for photosynthesis. Algae overgrowth on dead coral also prevents coral larvae from settling and establishing new symbioses — a positive feedback loop."),
        ("Herbivore Fish Population to Algae Overgrowth", "NEGATIVE (-)", "Parrotfish, surgeonfish, and other herbivores graze on algae, keeping it in check and maintaining open substrate for coral recruitment. Higher herbivore populations mean less algae overgrowth.")
    ],
    "sim_answers": [
        ("Moderate Warming", "With a 1 degree temperature increase, the model shows moderate bleaching that weakens Coral-Zooxanthellae Symbiosis. If the temperature anomaly is temporary, the reef can recover over 10-15 years. However, Algae Overgrowth increases during the weakened period, and if Herbivore Fish Population is not sufficient to control it, some coral areas shift permanently to algae dominance. The key finding is that a single moderate event is survivable, but the recovery window determines whether the reef can withstand the next event."),
        ("Double Stress", "The combination of +1.5 degrees Celsius warming and pH 7.9 produces devastating results. Bleaching from temperature stress is compounded by weakened skeletons from acidification. Coral Calcification Rate drops below the rate of natural erosion, meaning the reef is literally dissolving. Reef Biodiversity Index crashes as structural complexity disappears. The model shows a clear phase shift to algae dominance that becomes self-sustaining through positive feedback loops."),
        ("Managed Resilience", "With healthy herbivore populations maintained through fishing protection, the reef shows significantly better outcomes under moderate warming. Herbivorous fish control Algae Overgrowth, keeping substrate available for coral recovery. The model demonstrates that local management can delay or prevent phase shifts even under continued warming, buying critical time for global emission reductions to take effect. This scenario shows the tangible value of marine protected areas.")
    ],
    "reflection_exemplars": [
        ("Why is bleaching frequency more important than severity?", "Our model reveals that coral recovery from bleaching requires 10-15 years of stable conditions to fully regenerate zooxanthellae populations and rebuild energy reserves. A single severe bleaching event is survivable if followed by adequate recovery time. But when bleaching occurs every 2-3 years — as is now happening on the Great Barrier Reef — each event hits coral that hasn\\'t recovered from the previous one. The cumulative damage is like repeatedly opening a wound before it heals: eventually, the organism cannot recover at all. The model shows that reducing bleaching frequency (by slowing warming) is more important than reducing the severity of individual events."),
        ("Can local management save reefs from global warming?", "Our model shows that local management — particularly protecting herbivorous fish populations from overfishing — significantly increases reef resilience by maintaining the natural algae control system. In the managed reef scenario, the same temperature stress produced much less permanent damage because herbivores prevented the positive feedback loop of algae overgrowth. However, local management alone cannot save reefs if global warming continues unchecked — there is a temperature threshold beyond which no amount of fish can compensate for the destruction of the coral-algae symbiosis. Local management buys time, but it is not a substitute for addressing the root cause of warming.")
    ],
    "stem_intro": "Present the challenge: A Caribbean reef that supported a fishing community for generations has lost 60% of its coral cover. The remaining 40% is weakened but not yet past the phase shift threshold. Your model shows both the risks (continued warming, acidification) and opportunities (herbivore protection, pollution reduction). Design a rescue plan that addresses immediate local threats while advocating for long-term global solutions.",
    "stem_concepts": [
        ("Coral Restoration Techniques", "Modern reef restoration includes coral gardening (growing fragments in nurseries and transplanting them), selective breeding for heat tolerance, cryopreservation of coral genetics, and substrate stabilization. These techniques can accelerate recovery but are labor-intensive and expensive — restoring one hectare can cost $100,000-$1,000,000. Restoration works best when combined with stressor reduction rather than as a standalone solution."),
        ("Marine Protected Areas", "Designated ocean zones where fishing, development, and extraction are restricted or prohibited. Well-managed MPAs increase fish populations by 400-600% within their boundaries, maintain higher coral cover, and show greater recovery after bleaching events. The spillover effect means fish populations outside the MPA also increase as protected populations grow and migrate. Currently, only about 8% of the ocean is in MPAs."),
        ("Ecosystem Services Valuation", "Coral reefs provide ecosystem services valued at $375 billion per year globally — including fisheries ($6.8 billion), coastal storm protection ($9.0 billion), tourism ($36 billion), and pharmaceutical compounds. Putting economic value on ecosystem services helps policymakers understand the true cost of reef loss and justifies investment in conservation.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan addresses both local and global stressors with specific, evidence-based strategies, includes restoration timeline, breaks positive feedback loops identified in the model, considers economic and community impacts, and cites simulation data"),
        ("Proficient (3)", "Plan addresses multiple stressors with reasonable strategies and connects to model evidence, includes some consideration of feedback loops"),
        ("Developing (2)", "Plan focuses on only local or only global stressors, strategies are general rather than specific, weak connection to model data"),
        ("Beginning (1)", "Plan is incomplete, lacks scientific grounding, or does not address the feedback loop dynamics that drive reef decline")
    ],
    "support": [
        "Provide a simplified food web diagram showing the relationships between coral, zooxanthellae, herbivorous fish, and algae — students can trace the cascade of effects from one component to another",
        "Use the analogy of a building demolition: coral is the structure, zooxanthellae are the energy supply, herbivorous fish are the maintenance crew — what happens if you remove the maintenance crew when the structure is already damaged?",
        "Sentence frames: \\'When ___ increases, ___ decreases because ___. This leads to ___, which creates a feedback loop because ___.\\'"
    ],
    "extensions": [
        "Research assisted gene flow and selective breeding programs for heat-tolerant coral — evaluate the scientific evidence for and ethical concerns about genetically modifying coral to survive warmer oceans",
        "Calculate the economic cost of losing a specific coral reef by quantifying its fisheries, tourism, and coastal protection services — compare the cost of loss to the cost of conservation",
        "Investigate the relationship between coral reef health and deep-ocean biodiversity — how do changes at the surface propagate to ecosystems hundreds of meters below?"
    ],
    "cross_curr": [
        ("Math", "Calculate the rate of ocean pH change given current CO2 emission rates, using the logarithmic relationship between hydrogen ion concentration and pH. Project future pH levels under different emission scenarios and determine when reef dissolution thresholds are crossed."),
        ("ELA", "Read and analyze competing stakeholder perspectives on marine protected area designation — a marine biologist, a commercial fisher, a tourism operator, and a local government official. Write a policy brief that synthesizes scientific evidence with stakeholder concerns."),
        ("History", "Research the history of whaling and the collapse of global whale populations in the 19th and 20th centuries as a case study in marine resource exploitation. Compare the timeline of whale population decline and recovery to current trajectories for coral reef ecosystems.")
    ],
    "misconceptions": [
        ("Coral is a plant or a rock, not a living animal", "Corals are colonies of tiny animals called polyps, related to jellyfish and sea anemones. Each polyp has a mouth, tentacles, and a stomach. They build calcium carbonate skeletons over time, creating the rock-like reef structure. The color comes from their symbiotic zooxanthellae algae, not from the coral animal itself. Understanding that coral is alive — and as vulnerable as any animal — is essential to understanding bleaching and death.", "Show students a close-up video of coral polyps feeding at night, extending their tentacles to catch plankton. This dramatic visual immediately changes the perception from rock to living organism."),
        ("Bleaching means the coral is dead", "Bleaching is a stress response, not death — it means the coral has expelled its zooxanthellae but is still alive, surviving on energy reserves for 4-8 weeks. If temperatures return to normal quickly, the coral can reacquire algae and recover, though it will be weakened for months. Bleaching becomes fatal only when high temperatures persist or when events are so frequent that coral cannot rebuild between them. The distinction matters because it means we have a window of opportunity.", "Show before, during, and after images of coral that has bleached and recovered. Emphasize the timeline: 4-8 weeks to survive without algae, 10-15 years to fully recover. Ask: What happens if the next bleaching event comes in 2 years?"),
        ("Coral reefs only matter to tropical countries", "Reef loss affects the entire global food web and economy. Reefs provide nursery habitat for commercially important fish species that migrate globally. Reef-derived compounds are used in medicines treating cancer, HIV, and cardiovascular disease. Reefs buffer coastlines from storms, protecting billions of dollars in infrastructure. The global economic value of reef services is estimated at $375 billion per year. Furthermore, reef collapse can trigger cascading effects in ocean food webs that affect fisheries worldwide, including in temperate and polar regions.", "Present the economic data: Ask students to calculate their community\\'s indirect connection to reef ecosystems through seafood supply chains, pharmaceutical ingredients, and coastal storm damage costs.")
    ]
}

L03 = {
    "id": "G12L2-L03",
    "title": "Can We Feed 10 Billion People?",
    "subtitle": "Modeling Agricultural Systems, Land Use, and Global Food Security",
    "ngss": "HS-LS2-1",
    "ngss_desc": "Use mathematical and/or computational representations to support explanations of factors that affect carrying capacity of ecosystems at different scales.",
    "big_question": "Earth currently struggles to feed 8 billion people equitably, with 800 million going hungry while one-third of all food is wasted — so when the population hits 10 billion by 2050, can we produce enough food without destroying the ecosystems we depend on?",
    "objectives": [
        "Model how agricultural production, land use change, soil health, and water availability interact to determine food system carrying capacity",
        "Explain how intensive farming practices increase short-term yields while degrading the long-term productivity of soil and water resources",
        "Predict the conditions under which food systems become unsustainable and identify the leverage points for improving efficiency",
        "Analyze the trade-offs between food production, environmental conservation, and equitable distribution in global food systems"
    ],
    "vocabulary": [
        ("Carrying Capacity", "The maximum population an environment can sustain indefinitely given available resources — for global food systems, this depends not just on total production potential but on the sustainability of farming practices, equitable distribution, and the ecological systems that support agriculture"),
        ("Soil Degradation", "The decline in soil quality through erosion, nutrient depletion, compaction, salinization, and loss of organic matter — intensive farming without regenerative practices can reduce soil productivity by 50-70% within decades, and it takes 500-1,000 years to form one inch of new topsoil"),
        ("Food System Efficiency", "The ratio of food consumed by humans to total food produced — globally, approximately one-third of food is lost or wasted between farm and table, and converting plant calories to animal calories loses 75-90% of the original energy, meaning the food system is far less efficient than raw production numbers suggest"),
        ("Agroecology", "A farming approach that applies ecological principles to agriculture — including crop diversity, soil biology, integrated pest management, and water conservation — to produce food sustainably while maintaining ecosystem services like pollination, water filtration, and carbon storage")
    ],
    "components": [
        ("Global Population", "The total number of humans requiring food — projected to reach 9.7-10.4 billion by 2050, with most growth concentrated in sub-Saharan Africa and South Asia where food insecurity is already highest", True),
        ("Agricultural Land Area", "The total land dedicated to crop production and livestock grazing — currently 5 billion hectares (38% of ice-free land), with expansion increasingly limited by ecosystem conservation needs and the decreasing productivity of newly converted land", True),
        ("Crop Yield Per Hectare", "The amount of food produced per unit of farmland — determined by seed genetics, soil health, water availability, fertilizer input, and pest management, with global average yields plateauing in many regions despite increasing inputs", False),
        ("Soil Health Index", "The biological, chemical, and physical quality of agricultural soil — healthy soil contains billions of organisms per gram that cycle nutrients, retain water, and suppress disease, but intensive monoculture, chemical fertilizers, and tillage degrade soil health over time", False),
        ("Water Availability for Agriculture", "The amount of freshwater accessible for irrigation — agriculture uses 70% of global freshwater withdrawals, and many major agricultural regions depend on groundwater aquifers that are being depleted faster than they recharge", False),
        ("Food Waste and Loss", "The portion of food produced that is never consumed — approximately 1.3 billion tons per year globally, lost to spoilage in developing countries (lack of storage and transport) and waste in developed countries (consumer behavior and retail standards)", False),
        ("Biodiversity in Agricultural Landscapes", "The variety of species within and around farmland that provide ecosystem services — pollinators, pest predators, soil organisms, and genetic diversity in crops, all of which decline under intensive monoculture but are essential for long-term productivity", False)
    ],
    "think_about_it": "If Global Population increases while Soil Health Index and Water Availability decline due to intensive farming, what happens to the long-term Crop Yield Per Hectare even if short-term yields increase with more fertilizer? Where is the unsustainable pattern?",
    "scenarios": [
        ("Industrial Intensification", "Increase Agricultural Land Area by 20% through deforestation and maximize chemical inputs — observe the short-term yield increases versus long-term soil degradation and biodiversity loss"),
        ("Business As Usual with Population Growth", "Maintain current farming practices while increasing Global Population to 10 billion — observe whether current food system capacity can meet demand without major changes"),
        ("Sustainable Intensification", "Hold Agricultural Land Area constant, reduce Food Waste by 50%, improve Soil Health through regenerative practices — observe whether these efficiency gains can feed 10 billion people")
    ],
    "sim_scenarios": [
        ("Industrial Expansion", "Agricultural Land: +20% | Chemical Inputs: Maximum | Soil Practices: Conventional Tillage", "What do you predict happens to Crop Yield Per Hectare in the short term (5 years) versus the long term (30 years) under industrial intensification?"),
        ("Population Pressure", "Global Population: 10 Billion | Agricultural Land: Current | Farming: Current Practices", "Can current food systems feed 10 billion people without changes? What component becomes the bottleneck first?"),
        ("Regenerative Transition", "Agricultural Land: Current | Waste Reduction: 50% | Soil Health: Improving | Biodiversity: Protected", "Can we feed more people with the same land by improving efficiency and soil health? What does the model show about the timeline?")
    ],
    "discoveries": [
        "Industrial intensification produces short-term yield gains but long-term productivity collapse — the model shows Soil Health Index declining steadily under conventional practices until yields begin falling despite increasing chemical inputs",
        "Food Waste and Loss is the single largest leverage point in the food system — reducing waste by 50% is equivalent to increasing agricultural land by 25% without any environmental cost",
        "Water Availability becomes the binding constraint before land in most scenarios — aquifer depletion from irrigation is irreversible on human timescales and threatens food production in the world\\'s most productive agricultural regions",
        "Sustainable intensification that combines waste reduction, soil regeneration, and biodiversity protection can theoretically feed 10 billion people on current agricultural land — but requires fundamental transformation of farming practices and food distribution systems"
    ],
    "answer": "Feeding 10 billion people is technically possible but will require fundamental transformation of global food systems. The current industrial model maximizes short-term yields at the expense of the soil health, water resources, and biodiversity that sustain long-term productivity — it is essentially mining the ecological foundation of agriculture. The model reveals three critical leverage points: reducing the one-third of food that is currently wasted would be equivalent to a 25% increase in farmland; regenerating soil health through agroecological practices can maintain or increase yields while rebuilding natural capital; and protecting biodiversity in agricultural landscapes maintains the pollinators, pest predators, and soil organisms that intensive monoculture destroys. Water availability emerges as the most critical constraint, with major agricultural aquifers declining rapidly. The challenge is not primarily technological — we already know how to grow food sustainably. It is political and economic: transforming subsidies, supply chains, diets, and distribution systems to prioritize long-term sustainability and equitable access over short-term profit.",
    "stem_title": "Design a Sustainable Food System for a Growing City",
    "stem_mission": "Design a comprehensive food system plan for a rapidly growing city of 2 million people that maximizes food security while minimizing environmental impact, incorporating local agriculture, waste reduction, and equitable distribution.",
    "stem_scenario": "A rapidly growing city in a semi-arid region is projected to double its population from 1 million to 2 million within 20 years. Currently, 90% of its food is trucked in from distant industrial farms, 35% of food is wasted, local farmland is being paved for development, and the regional aquifer is declining by 2 meters per year. The city government has commissioned your team to design a food system that can feed 2 million people sustainably for at least 50 years. Your model data should guide decisions about local food production, water management, waste reduction, and distribution equity.",
    "stem_questions": [
        "Based on your model, which food system components are most vulnerable to continued population growth in a water-scarce region?",
        "What does your model suggest about the relative impact of waste reduction versus increased production in meeting food demand?",
        "How can urban agriculture and local food production reduce the city\\'s dependence on distant industrial farms?"
    ],
    "stem_design_qs": [
        "How does your food system plan address water scarcity — the most critical constraint identified by your model?",
        "What specific waste reduction strategies does your plan implement, and what percentage of the food gap do they close?",
        "How does your plan ensure equitable food access across all neighborhoods, including low-income communities?",
        "What role does soil health regeneration play in your plan\\'s long-term sustainability?"
    ],
    "career": "Agricultural scientists and food systems researchers study how to produce more food with fewer resources while maintaining ecosystem health. They work for the USDA, universities, international organizations like the FAO, and agricultural technology companies, earning $60,000-$125,000/year. Urban agriculture designers who plan rooftop farms, vertical farms, and community gardens earn $55,000-$100,000/year. Food policy analysts who shape government nutrition programs and agricultural subsidies earn $65,000-$120,000/year.",
    "images": {
        "cover": ("G12L2-L03-cover.png", "A photorealistic image of diverse 17-18 year old students examining soil samples and plant growth experiments in a school greenhouse laboratory, with data collection tablets and agricultural monitoring equipment visible"),
        "landscape": ("G12L2-L03-landscape.png", "A photorealistic aerial view showing the contrast between a lush sustainable farm with diverse crops and healthy soil on one side and a depleted industrial monoculture with eroded, barren soil on the other side"),
        "modeling": ("G12L2-L03-modeling.png", "A photorealistic image of diverse 17-18 year old students working on food system models on laptops, with agricultural data visualizations and population growth charts projected on a smartboard behind them"),
        "discussion": ("G12L2-L03-discussion.png", "A photorealistic image of a teacher leading a discussion with diverse 17-18 year old students about global food security, with a world hunger map and food waste infographic displayed on screen, students actively participating"),
        "stem": ("G12L2-L03-stem.png", "A photorealistic image of diverse 17-18 year old students designing sustainable food system plans on poster boards with city maps, crop layouts, water budgets, and distribution network diagrams")
    },
    "pre_assessment": [
        "Where does your food come from? Can you trace a typical meal from farm to your plate and estimate how far it traveled?",
        "What percentage of food produced globally do you think is wasted or lost before anyone eats it? Why does this happen?",
        "What do you think is the biggest challenge in feeding a growing world population — producing more food, distributing it fairly, or both?",
        "How do you think farming affects the environment? What trade-offs exist between food production and environmental health?"
    ],
    "extend_components": [
        ("Dietary Composition", "The proportion of animal versus plant-based foods in the average diet — producing one calorie of beef requires 25 calories of feed grain and 15,000 liters of water, so dietary shifts toward more plant-based foods could dramatically reduce the land and water footprint of the food system"),
        ("Climate Change Impact on Agriculture", "The effect of rising temperatures, changing precipitation, and extreme weather on crop yields — climate models project 10-25% yield declines in tropical and subtropical regions by 2050, precisely where population growth is highest"),
        ("Agricultural Technology and Innovation", "Advances in precision agriculture, vertical farming, gene editing, and satellite monitoring that can increase yields per hectare — technology can improve efficiency but cannot overcome the fundamental constraints of soil health, water availability, and ecosystem degradation")
    ],
    "reflections": [
        "How does your model illustrate the tension between maximizing short-term food production and maintaining long-term agricultural sustainability?",
        "Why is food waste reduction potentially more impactful than increasing production? What does your model show about the scale of waste?",
        "Water emerged as a critical constraint in your model. What are the implications for agricultural regions that depend on depleting groundwater?",
        "How would shifting global diets toward more plant-based foods change the carrying capacity calculation in your model?",
        "What does your model suggest about the claim that technology alone can solve the food crisis without changes to farming practices, distribution, or consumption?"
    ],
    "dimensions": [
        ("Science Practice", "Using Mathematics and Computational Thinking", "Students use computational models to calculate food system carrying capacity under different scenarios, quantifying the relationships between population growth, resource constraints, and food production potential."),
        ("Disciplinary Core Idea", "LS2.A Interdependent Relationships in Ecosystems", "Ecosystems have carrying capacities that result from biotic and abiotic factors, and the carrying capacity of agricultural ecosystems depends on maintaining the soil biology, water cycles, and biodiversity that sustain productivity."),
        ("Crosscutting Concept", "Systems and System Models", "Students use systems thinking to understand how food production, resource consumption, waste, and environmental degradation form interconnected feedback loops that determine whether food systems are sustainable or self-undermining.")
    ],
    "cast_items": [
        "Model how population growth, agricultural practices, and resource availability interact to determine food system carrying capacity",
        "Predict the conditions under which food systems become unsustainable due to soil degradation, water depletion, or biodiversity loss",
        "Evaluate the relative effectiveness of different food system interventions — waste reduction, yield improvement, and sustainable practices — using computational evidence"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A region increases fertilizer application by 40% to boost crop yields. In the first 5 years, yields increase by 15%. But after 20 years, yields are lower than before the fertilizer increase. Based on your food system model, which explanation is most accurate? A) The fertilizer was the wrong type B) Soil Health Index declined due to biological disruption, canceling out chemical gains C) The crops developed immunity to fertilizer D) Rainfall decreased independently"),
        ("Constructed Response:", "Using your food system model, explain why reducing food waste by 50% could be more effective than increasing agricultural land by 20% for feeding a growing population. Reference at least three components and the concept of carrying capacity in your answer.")
    ],
    "background_intro": "The global food system is one of humanity\\'s greatest achievements and greatest vulnerabilities. Modern agriculture feeds nearly 8 billion people — more than any point in history — but does so by depleting the soil, water, and biodiversity that future food production depends on. We are essentially borrowing from the future to feed the present, and the bill is coming due as population grows toward 10 billion while agricultural resources degrade.",
    "background_sections": [
        ("The Green Revolution: Triumph and Trade-offs", "The Green Revolution of the 1960s-1980s dramatically increased global food production through high-yield crop varieties, synthetic fertilizers, pesticides, and irrigation. Global grain production tripled between 1950 and 2000, preventing predicted mass famines. However, this success came with hidden costs: dependence on fossil fuel-based inputs, groundwater depletion from massive irrigation, soil degradation from monoculture and tillage, biodiversity loss from pesticides and habitat conversion, and dead zones in coastal waters from fertilizer runoff. The Green Revolution showed that technology can dramatically increase production, but it did not solve the underlying challenge of sustainability — it delayed it while making the eventual reckoning larger."),
        ("Soil: The Foundation Under Threat", "Healthy agricultural soil is a living ecosystem containing billions of bacteria, fungi, insects, and worms per gram that cycle nutrients, retain water, suppress disease, and build soil structure. Intensive monoculture, chemical fertilizers, and tillage disrupt this biology, leading to soil that is chemically fed but biologically dead. The consequences are severe: the United Nations estimates that one-third of global topsoil is already degraded, and at current rates of loss, the world has about 60 harvests left in many regions. Regenerative agriculture — cover crops, reduced tillage, composting, crop rotation, and integrated livestock — can reverse soil degradation, but the transition takes 3-7 years and requires support during the yield dip that often occurs initially."),
        ("The Water Crisis in Agriculture", "Agriculture consumes 70% of global freshwater withdrawals, primarily for irrigation. Many of the world\\'s most productive agricultural regions — the US Great Plains, India\\'s Punjab, China\\'s North China Plain — depend on groundwater aquifers that are being depleted far faster than they recharge. The Ogallala Aquifer under the US Great Plains has lost 30% of its volume since 1960 and continues declining. When these aquifers are exhausted, the agricultural production they support will collapse — and unlike soil, depleted aquifers cannot be regenerated on any human timescale. More efficient irrigation (drip systems, soil moisture monitoring) can reduce water use by 30-50%, but ultimately, water-intensive crops in arid regions represent an unsustainable model."),
        ("Food Waste: The Hidden Opportunity", "Approximately one-third of all food produced globally — 1.3 billion tons worth $1 trillion per year — is lost or wasted. In developing countries, losses occur primarily after harvest due to inadequate storage, transport, and processing infrastructure. In developed countries, waste occurs at the retail and consumer level due to cosmetic standards, oversized portions, confusion about expiration dates, and cultural devaluation of food. Reducing food waste by 50% would effectively increase the global food supply by 16% without requiring a single additional acre of farmland or gallon of water. This is the most cost-effective, environmentally beneficial, and technically feasible intervention in the entire food system — yet it receives a fraction of the investment directed at increasing production.")
    ],
    "lever_L": "Students identify Global Population, Agricultural Land Area, Crop Yield Per Hectare, Soil Health Index, Water Availability, Food Waste and Loss, and Biodiversity in Agricultural Landscapes as key components of the food system.",
    "lever_E": "Students determine that population growth drives food demand, that intensive farming degrades soil and water over time, that food waste represents the largest inefficiency, and that biodiversity provides essential ecosystem services for sustainable production.",
    "lever_V": "Students build a computational model showing how food system components interact over time, revealing the tension between short-term production maximization and long-term sustainability.",
    "lever_Ev": "Students run industrial intensification, population pressure, and sustainable intensification scenarios to test predictions about food system capacity and the effectiveness of different intervention strategies.",
    "lever_R": "Students add dietary composition, climate change impacts, or agricultural technology to explore how additional factors affect food system carrying capacity and sustainability.",
    "slides_guide": [
        {
            "num": "Slide 1",
            "title": "Cover",
            "visual": "Title slide with image showing global food production juxtaposed with food insecurity statistics",
            "say": "By 2050, there will be 10 billion people on this planet. Can we feed them all without destroying the ecosystems we depend on? That\\'s what we\\'re modeling today.",
            "do": "Show cover image. Quick poll: How many people think we can feed 10 billion? How many think we can\\'t? What would need to change?",
            "time": "2 min"
        },
        {
            "num": "Slide 2",
            "title": "Learning Objectives",
            "visual": "Four learning objectives with food system vocabulary terms highlighted",
            "say": "Today we\\'re modeling the global food system — not just farming, but the entire chain from soil to plate, including what gets wasted along the way.",
            "do": "Have students read objectives. Pre-teach vocabulary. Key insight: carrying capacity isn\\'t just about maximum production — it\\'s about sustainable production over time.",
            "time": "3 min"
        },
        {
            "num": "Slide 3",
            "title": "Big Question",
            "visual": "Provocative statistics: 800 million hungry, 1.3 billion tons wasted, population growing to 10 billion",
            "say": "We already produce enough calories to feed 10 billion people. So why are 800 million hungry? And what happens when demand grows while soil and water decline?",
            "do": "Quick-write: Students write their initial analysis of the food system challenge. Is it a production problem, a distribution problem, or both?",
            "time": "3 min"
        },
        {
            "num": "Slide 4",
            "title": "LEVER Framework",
            "visual": "LEVER steps overview with food system examples",
            "say": "We\\'ll build a model that reveals the hidden dynamics of the food system — including why producing more food can sometimes make the problem worse in the long run.",
            "do": "Preview each LEVER step. Emphasize that this model will challenge assumptions about whether the food crisis is simply about growing more food.",
            "time": "2 min"
        },
        {
            "num": "Slide 5",
            "title": "Activity 1: Components",
            "visual": "Seven component cards for sorting: population, land, yield, soil, water, waste, biodiversity",
            "say": "Sort these into external drivers and internal system responses. Think about what inputs the food system receives versus what happens inside the system.",
            "do": "Guide sorting: External = Global Population (demographic trend), Agricultural Land Area (policy decision). Internal = the rest. Discuss why Crop Yield is internal even though it feels like an output.",
            "time": "8 min"
        },
        {
            "num": "Slide 6",
            "title": "Activity 2: Connections",
            "visual": "Relationship diagram template with all seven components",
            "say": "How does increasing chemical inputs boost short-term yields while degrading long-term soil health? Trace the feedback loop between soil, yield, and the pressure to add more chemicals.",
            "do": "Students draw arrows. Key discovery: the vicious cycle of soil degradation — declining soil health requires more chemical inputs, which further degrade biology, requiring even more inputs. Compare to the sustainable cycle of regenerative practices.",
            "time": "8 min"
        },
        {
            "num": "Slide 7",
            "title": "Activity 3: Simulation",
            "visual": "Simulation interface with three scenarios showing yield, soil health, and water over time",
            "say": "Run all three scenarios and pay attention to what happens in year 5 versus year 30. The short-term and long-term results may be very different.",
            "do": "Students run scenarios, compare predictions to observations. Key discussion: Why does industrial intensification look good in year 5 but catastrophic in year 30? What changed?",
            "time": "10 min"
        },
        {
            "num": "Slide 8",
            "title": "Discoveries",
            "visual": "Four key discoveries with supporting graphs showing the divergence between short-term and long-term outcomes",
            "say": "The biggest surprise from our model: the most impactful intervention isn\\'t producing more food — it\\'s wasting less. Let\\'s discuss why.",
            "do": "Class discussion. Compare initial predictions to model evidence. Challenge: If we already produce enough food for 10 billion, why do we focus on production instead of waste and distribution?",
            "time": "5 min"
        },
        {
            "num": "Slide 9",
            "title": "STEM Challenge",
            "visual": "Engineering challenge: Design a sustainable food system for a city growing from 1 to 2 million people",
            "say": "Your city is doubling in population in a semi-arid region with a declining aquifer. Design a food system that\\'s still working in 50 years. Use your model data.",
            "do": "Groups design food system plans addressing water, waste, local production, soil health, and equitable distribution. Present with evidence from model simulations.",
            "time": "12 min"
        }
    ],
    "sort_reasoning": "Global Population and Agricultural Land Area are external components because they represent inputs determined by demographic trends and policy decisions that exist outside the agricultural system itself — the food system must respond to population growth and operate within the land allocated to it. Crop Yield Per Hectare, Soil Health Index, Water Availability, Food Waste and Loss, and Biodiversity are internal because they are properties of the food system that change based on how the system is managed — they are the dynamic responses that determine whether the system can sustainably meet the external demand.",
    "relationships": [
        ("Global Population to Crop Yield Per Hectare", "POSITIVE (+)", "Growing population increases demand pressure on agricultural production, pushing for higher yields per hectare through intensification of inputs and farming practices."),
        ("Crop Yield Per Hectare to Soil Health Index", "NEGATIVE (-)", "Higher yields achieved through intensive chemical farming degrade soil biology, organic matter, and structure over time — the short-term production boost comes at the cost of long-term soil health."),
        ("Soil Health Index to Crop Yield Per Hectare", "POSITIVE (+)", "Healthy soil with robust biology provides natural fertility, water retention, and pest suppression that support higher yields. As soil health declines, yields become increasingly dependent on external chemical inputs."),
        ("Water Availability to Crop Yield Per Hectare", "POSITIVE (+)", "Adequate water supply is essential for crop growth. As water availability declines from aquifer depletion, yields drop even with sufficient soil nutrients and other inputs."),
        ("Biodiversity in Agricultural Landscapes to Crop Yield Per Hectare", "POSITIVE (+)", "Pollinators, pest predators, and soil organisms provide ecosystem services essential for crop production. Biodiversity loss from pesticides and habitat destruction removes these natural supports."),
        ("Food Waste and Loss to Global Population", "NEGATIVE (-)", "Higher food waste reduces the effective food supply relative to production, increasing the gap between what is grown and what is available for consumption, effectively raising the production requirement for each person fed.")
    ],
    "sim_answers": [
        ("Industrial Expansion", "In the first 5 years, industrial intensification shows impressive results: Crop Yield Per Hectare increases by 15-20% with more chemical inputs and expanded land. But by year 15-20, Soil Health Index has declined significantly, Water Availability is dropping from increased irrigation demand, and Biodiversity has crashed. By year 30, yields are declining despite increasing chemical inputs because the biological foundation of soil productivity has been undermined. The model demonstrates that industrial intensification borrows from the future — it converts natural capital into short-term production."),
        ("Population Pressure", "With population at 10 billion and current practices, the model shows that Water Availability becomes the binding constraint first, followed by Soil Health Index. Even maintaining current yields requires increasing chemical inputs to compensate for degrading soil, which accelerates degradation in a vicious cycle. Food Waste at current levels means that nearly enough food is produced but distributed so inefficiently that hundreds of millions remain food insecure."),
        ("Regenerative Transition", "Sustainable intensification shows a different trajectory: initial yields may dip slightly during the 3-5 year soil rebuilding period, but then stabilize at levels comparable to industrial farming while Soil Health Index steadily improves. Combined with 50% waste reduction, the model shows sufficient food production for 10 billion people on current agricultural land. The critical finding is that this pathway is sustainable indefinitely because it builds natural capital rather than depleting it.")
    ],
    "reflection_exemplars": [
        ("Why is food waste more impactful than increasing production?", "Our model shows that reducing food waste by 50% — from approximately 33% to 16% — would free up enough food to feed 1.5-2 billion additional people without requiring any additional land, water, fertilizer, or environmental impact. Increasing production by the same amount would require expanding Agricultural Land Area (driving deforestation), intensifying chemical inputs (degrading Soil Health Index), and pumping more Water from depleting aquifers. The waste reduction pathway has zero environmental cost and actually reduces environmental pressure, while the production increase pathway compounds the sustainability crisis. It\\'s mathematically obvious once you model it: it\\'s far cheaper and more sustainable to keep food from being wasted than to grow replacement food."),
        ("Can technology alone solve the food crisis?", "Our model suggests that technology is necessary but not sufficient. Agricultural Technology and Innovation can increase Crop Yield Per Hectare, but the model clearly shows that yield improvements are unsustainable if they come at the expense of Soil Health Index and Water Availability. Technology like precision agriculture and drought-resistant varieties can improve efficiency within the system, but the fundamental constraints — finite land, depleting water, degrading soil — cannot be overcome by technology alone. The model demonstrates that systemic changes — reducing waste, regenerating soil, shifting diets, and improving distribution — are required alongside technological improvements. Technology without system change is like a faster engine in a car running out of fuel.")
    ],
    "stem_intro": "Present the challenge: A city of 1 million is doubling to 2 million in a semi-arid region where the aquifer is declining 2 meters per year. Currently 90% of food is trucked in, 35% is wasted, and local farmland is being paved. Design a food system that works for 2 million people for 50 years. Your model data should guide every decision about water, waste, local production, and equitable access.",
    "stem_concepts": [
        ("Urban Agriculture and Vertical Farming", "Growing food within city limits using rooftop gardens, community plots, indoor vertical farms, and hydroponic systems. Vertical farms can produce 10-20 times more food per square meter than conventional farms using 95% less water, but require significant energy input. Urban agriculture also reduces food miles, provides fresh produce to food deserts, and builds community food literacy."),
        ("Circular Food Economy", "A food system design where waste from one process becomes input for another — food scraps are composted into soil amendments, wastewater is treated and reused for irrigation, and unsold produce is redirected to food banks rather than landfills. A circular food economy can reduce waste to near zero while regenerating soil and water resources."),
        ("Food Justice and Access", "Ensuring that all community members have access to affordable, nutritious food regardless of income or location. Food deserts — areas without grocery stores selling fresh produce — disproportionately affect low-income communities and communities of color. Equitable food system design must address these disparities through strategic placement of markets, transportation solutions, and community-supported agriculture.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan addresses water scarcity, waste reduction, local production, soil regeneration, and equitable access with specific strategies justified by model data, includes a realistic 50-year timeline with milestones"),
        ("Proficient (3)", "Plan addresses most food system challenges with reasonable strategies and some connection to model evidence, includes consideration of sustainability timeline"),
        ("Developing (2)", "Plan addresses some challenges but misses critical constraints like water or equity, strategies are general rather than specific to the model data"),
        ("Beginning (1)", "Plan is incomplete, ignores major constraints, or does not connect strategies to food system dynamics from the model")
    ],
    "support": [
        "Provide a simplified food system diagram showing the flow from farm to table with waste exit points marked — students can identify where the biggest losses occur and design interventions at each point",
        "Use the analogy of a household budget: income (production) minus waste (spending on things you throw away) equals what you actually have. If you waste 33% of your income, earning more isn\\'t the most efficient solution — spending smarter is.",
        "Sentence frames: \\'If ___ continues to decline while population grows, the food system will ___ because ___. The most effective intervention is ___ because the model shows ___.\\'"
    ],
    "extensions": [
        "Research the environmental and ethical implications of lab-grown meat — calculate the land, water, and greenhouse gas savings compared to conventional livestock and evaluate the technological barriers to large-scale production",
        "Investigate the concept of food sovereignty — the right of peoples to define their own food systems — and compare it to the corporate-controlled global food system. Analyze the trade-offs between efficiency and autonomy.",
        "Calculate the water footprint of your own diet for one week, then redesign your meals to reduce water consumption by 50% while maintaining nutritional adequacy. Present the feasibility and challenges of dietary water reduction."
    ],
    "cross_curr": [
        ("Math", "Calculate the caloric efficiency of different food production pathways: grain to human versus grain to beef to human versus grain to chicken to human. Use ratios and percentages to determine how many more people could be fed by shifting 30% of animal feed grain to direct human consumption."),
        ("ELA", "Read excerpts from Wendell Berry\\'s agricultural essays and compare his vision of local, sustainable farming to the globalized industrial food system. Write an argument essay evaluating which model better addresses the challenge of feeding 10 billion people."),
        ("History", "Research the Irish Potato Famine of 1845-1852 as a case study in how monoculture vulnerability, colonial economic systems, and inequitable food distribution can combine to produce mass starvation even when total food production is sufficient. Draw parallels to modern food system vulnerabilities.")
    ],
    "misconceptions": [
        ("We just need to grow more food to solve hunger", "Global food production already exceeds the caloric needs of 10 billion people, yet 800 million are hungry. Hunger is primarily a distribution and access problem, not a production problem. Poverty, conflict, infrastructure gaps, and political failures prevent food from reaching those who need it. Additionally, one-third of food produced is wasted. Simply growing more food within the current system would increase environmental damage without solving the underlying distribution failures.", "Present the paradox: The world produces 6,000 calories per person per day (far more than needed) yet 800 million go hungry. Ask: If production isn\\'t the problem, what is? Guide students toward distribution, access, and waste."),
        ("Organic farming can\\'t feed the world because yields are lower", "While organic yields are typically 10-20% lower than conventional in developed countries, this comparison ignores several critical factors: conventional yields are declining as soil degrades, organic soil health improves over time (closing the yield gap), the one-third of food wasted means production capacity far exceeds actual needs, and conventional farming\\'s dependence on fossil fuel-based inputs and depleting aquifers makes it unsustainable long-term. The real question is not which system produces more per acre in year one, but which system still produces food in year fifty.", "Show the long-term yield curves from the model: conventional starts higher but declines as soil degrades, while regenerative starts slightly lower but stabilizes as soil health improves. Ask: Which system would you choose for the next 50 years?"),
        ("Technology will solve the food crisis without changing how we farm or eat", "While agricultural technology (precision farming, GMOs, vertical farms) can increase efficiency, technology cannot override the fundamental constraints of soil biology, water availability, and ecosystem services. The model shows that yield improvements are temporary if they come at the expense of the ecological foundation. Furthermore, the most impactful interventions — reducing waste, improving distribution, and shifting diets — are behavioral and systemic, not technological. Technology is a tool, not a solution in itself.", "Show the model scenario where technology increases yields short-term but soil and water continue declining. Ask: What happens when you run a more powerful engine but keep draining the fuel tank faster? Technology without system change accelerates collapse, not sustainability.")
    ]
}

L04 = {
    "id": "G12L2-L04",
    "title": "Where Does All the Plastic Go?",
    "subtitle": "Modeling Plastic Pollution Pathways, Microplastic Accumulation, and Bioaccumulation",
    "ngss": "HS-ESS3-4",
    "ngss_desc": "Evaluate or refine a technological solution that reduces impacts of human activities on natural systems.",
    "big_question": "Humans have produced 8.3 billion metric tons of plastic since 1950, and 6.3 billion tons of that is now waste — so where did it all go, why is it showing up inside human blood and breast milk, and can we actually solve a pollution problem this massive?",
    "objectives": [
        "Model how plastic waste moves through environmental pathways from production to ocean accumulation, fragmentation into microplastics, and entry into food webs",
        "Explain the mechanisms by which macroplastics fragment into microplastics and how microplastics bioaccumulate up food chains",
        "Predict the long-term environmental fate of plastic waste under different waste management and production scenarios",
        "Analyze the effectiveness of proposed solutions from individual behavior changes to systemic policy interventions"
    ],
    "vocabulary": [
        ("Microplastic", "Plastic fragments smaller than 5 millimeters in diameter created by the physical, chemical, and biological breakdown of larger plastic items — microplastics are now found in every environment on Earth including deep ocean sediments, Arctic ice, mountain air, human blood, and placental tissue"),
        ("Bioaccumulation", "The process by which a substance builds up in an organism faster than it can be eliminated — plastic and the toxic chemicals it absorbs from the environment accumulate in animal tissues, with concentrations increasing at each level of the food chain through biomagnification"),
        ("Persistent Organic Pollutant", "A toxic chemical that resists environmental degradation and accumulates in living organisms — plastics absorb and concentrate persistent organic pollutants like PCBs, DDT, and flame retardants from surrounding water, acting as a delivery vehicle for toxins into food webs"),
        ("Circular Economy", "An economic model that eliminates waste by designing products for reuse, repair, and recycling from the start — contrasted with the current linear model of take-make-waste, a circular economy for plastics would ensure that no plastic ever becomes pollution")
    ],
    "components": [
        ("Plastic Production Rate", "The global volume of new plastic manufactured per year — currently over 400 million metric tons annually and growing at 4% per year, with production projected to triple by 2060 without intervention", True),
        ("Waste Management Capacity", "The infrastructure and systems available to collect, sort, recycle, or safely dispose of plastic waste — globally, only 9% of all plastic ever produced has been recycled, 12% incinerated, and 79% accumulated in landfills or the environment", True),
        ("Environmental Plastic Load", "The total amount of plastic debris present in terrestrial, freshwater, and marine environments — an estimated 8-12 million metric tons of plastic enter the ocean every year, joining an estimated 150 million metric tons already there", False),
        ("Microplastic Concentration", "The density of plastic particles smaller than 5mm in water, soil, air, and biological tissue — increases over time as macroplastics fragment through UV radiation, wave action, and biological processes, and once created, microplastics persist for centuries", False),
        ("Bioaccumulation in Food Webs", "The concentration of plastic and associated toxins in organisms at different trophic levels — filter feeders ingest microplastics directly, and concentrations increase at each step up the food chain through biomagnification, ultimately reaching humans", False),
        ("Marine Ecosystem Health", "The overall condition of ocean ecosystems as affected by plastic pollution — entanglement kills hundreds of thousands of marine animals annually, ingestion reduces fitness and reproduction, and microplastics alter sediment chemistry and organism behavior", False),
        ("Human Health Exposure", "The level of microplastic and associated chemical exposure in human populations — recent studies have detected microplastics in human blood, lungs, placenta, and breast milk, with health effects still being researched but including potential endocrine disruption and inflammation", False)
    ],
    "think_about_it": "If Plastic Production Rate keeps increasing while only 9% of waste is recycled, what happens to Environmental Plastic Load over time? As macroplastics fragment into Microplastics, how does Bioaccumulation in Food Webs eventually connect plastic pollution to Human Health Exposure?",
    "scenarios": [
        ("Business As Usual", "Maintain current Plastic Production Rate growth of 4% per year with current Waste Management Capacity — observe how Environmental Plastic Load and Microplastic Concentration change over 30 years"),
        ("Improved Recycling Only", "Triple recycling rates from 9% to 27% while maintaining current production growth — observe whether improved waste management alone can reduce the growing environmental plastic load"),
        ("System Transformation", "Reduce Plastic Production Rate by 40%, triple recycling, and implement extended producer responsibility — observe whether combined upstream and downstream interventions can reverse the accumulation trend")
    ],
    "sim_scenarios": [
        ("Business As Usual", "Production Rate: +4%/year | Recycling: 9% | Policy: None", "If plastic production continues growing while waste management barely changes, what do you predict happens to Environmental Plastic Load and Microplastic Concentration in 30 years?"),
        ("Recycling Focus", "Production Rate: +4%/year | Recycling: 27% (Tripled) | Clean-up: Active", "Can better recycling and ocean clean-up solve the plastic crisis while production continues growing? Why or why not?"),
        ("Production Reduction + Circular Economy", "Production Rate: -40% | Recycling: 50% | Design: Circular | Policy: Producer Responsibility", "What happens when you address the source of the problem rather than just the symptoms? How quickly does the environmental plastic load respond?")
    ],
    "discoveries": [
        "Improved recycling alone cannot solve the plastic crisis because production growth outpaces recycling capacity — even tripling recycling rates only slightly slows the growth of environmental plastic accumulation when production continues increasing at 4% per year",
        "Microplastic Concentration continues increasing for decades even after new plastic input stops because existing macroplastics in the environment continue fragmenting — the microplastic problem has significant time lag built into it",
        "Bioaccumulation means that even low environmental concentrations of microplastics result in high tissue concentrations in top predators including humans — the food web acts as a concentration mechanism that amplifies exposure",
        "Only the system transformation scenario — reducing production, improving recycling, and implementing circular design — produces a meaningful decrease in Environmental Plastic Load, and even then, the microplastic legacy persists for generations"
    ],
    "answer": "The 8.3 billion metric tons of plastic humanity has produced since 1950 went everywhere — literally. Of the 6.3 billion tons of plastic waste generated, 79% accumulated in landfills or the natural environment. An estimated 150 million metric tons currently pollute the oceans, with 8-12 million tons added annually. But the most insidious problem is invisible: UV radiation, waves, and biological processes continuously fragment this plastic into microparticles that are now found in every environment on Earth, from the deepest ocean trenches to Mount Everest, and inside human bodies. The model reveals why recycling alone cannot solve this: production grows at 4% annually while only 9% is recycled, so the waste stream overwhelms any downstream solution. Bioaccumulation compounds the problem by concentrating microplastics and their associated toxins at each level of the food web. Only a system transformation that reduces production at the source, designs for circularity, and holds producers responsible for the full lifecycle of their products can reverse the trend — and even then, the microplastic legacy of past production will persist in the environment for centuries.",
    "stem_title": "Design a Zero-Plastic-Waste Community System",
    "stem_mission": "Design a comprehensive waste management and material substitution system for a community that eliminates plastic pollution pathways identified in your model, from production to environmental accumulation.",
    "stem_scenario": "A coastal community of 100,000 people generates 15,000 tons of plastic waste per year, of which only 8% is recycled, 15% is incinerated, and the rest goes to a landfill near the coast. Storm runoff regularly washes landfill plastic into the ocean, and local fisheries have documented increasing microplastic contamination in their catch. The community has committed to becoming zero-plastic-waste within 15 years. Your team must design a system that addresses every stage of the plastic lifecycle — from what enters the community to what leaves it — using your model\\'s evidence about which intervention points are most effective.",
    "stem_questions": [
        "Based on your model, which stage of the plastic lifecycle contributes most to environmental pollution in this community — production, consumption, disposal, or environmental leakage?",
        "What does your model suggest about the relative effectiveness of reducing plastic consumption versus improving recycling for this community?",
        "How does the time lag between macroplastic disposal and microplastic formation affect the urgency and design of your intervention?"
    ],
    "stem_design_qs": [
        "What specific plastic items does your plan eliminate, substitute, or redesign, and what materials replace them?",
        "How does your waste management system achieve near-zero leakage to the environment?",
        "What economic incentives or regulations does your plan use to change producer and consumer behavior?",
        "How does your plan address the existing plastic already in the local environment and coastal waters?"
    ],
    "career": "Environmental engineers who design waste management systems and develop alternatives to plastic pollution earn $65,000-$130,000/year. Materials scientists who develop biodegradable and sustainable alternatives to conventional plastics work for chemical companies, startups, and research universities, earning $70,000-$140,000/year. Environmental toxicologists who study the health effects of microplastics and persistent pollutants earn $60,000-$120,000/year at EPA, FDA, universities, and consulting firms.",
    "images": {
        "cover": ("G12L2-L04-cover.png", "A photorealistic image of diverse 17-18 year old students examining water samples under microscopes in a modern environmental science lab, with projected images of microplastic particles visible on a display behind them"),
        "landscape": ("G12L2-L04-landscape.png", "A photorealistic image showing an ocean surface with visible floating plastic debris in the foreground transitioning to clear blue water in the background, illustrating the scale of marine plastic pollution"),
        "modeling": ("G12L2-L04-modeling.png", "A photorealistic image of diverse 17-18 year old students building plastic pollution pathway models on their laptops, with environmental data and waste flow diagrams projected on screens around the classroom"),
        "discussion": ("G12L2-L04-discussion.png", "A photorealistic image of a teacher leading a discussion with diverse 17-18 year old students about plastic bioaccumulation, with a food web diagram showing microplastic concentration at each trophic level displayed on screen"),
        "stem": ("G12L2-L04-stem.png", "A photorealistic image of diverse 17-18 year old students designing zero-waste community systems on poster boards with waste flow diagrams, material substitution charts, and recycling infrastructure plans")
    },
    "pre_assessment": [
        "When you throw a plastic bottle in the trash, where does it go? Can you trace its journey from your hand to its final destination?",
        "What are microplastics and how do you think they end up in the ocean and eventually in the food you eat?",
        "Only 9% of all plastic ever produced has been recycled. Does that number surprise you? Why do you think it\\'s so low?",
        "Do you think plastic pollution is a problem that individuals can solve through personal choices, or does it require systemic change? Explain your reasoning."
    ],
    "extend_components": [
        ("Chemical Leaching from Plastics", "The release of additives like BPA, phthalates, and flame retardants from plastic as it degrades — these endocrine-disrupting chemicals enter water and food, and their concentrations in leachate increase as plastics fragment into smaller particles with greater surface area"),
        ("Atmospheric Microplastic Transport", "The movement of microplastic particles through the atmosphere — recent research has found microplastics in rain, snow, and air samples from remote locations, demonstrating that plastic pollution is not limited to areas near human activity but is a truly global contaminant"),
        ("Extended Producer Responsibility Policy", "A regulatory framework that makes manufacturers financially responsible for the entire lifecycle of their plastic products, including collection, recycling, and disposal — EPR programs in Europe have increased recycling rates to 30-40% compared to the US average of 5-6%")
    ],
    "reflections": [
        "Why does your model show that recycling alone cannot solve the plastic pollution crisis? What mathematical relationship between production growth and recycling capacity explains this?",
        "How does bioaccumulation transform a seemingly low concentration of microplastics in the ocean into a significant human health concern? Trace the pathway through your model.",
        "What does the time lag between plastic disposal and microplastic formation mean for the urgency of action? Why will microplastic levels continue rising even if we stop producing plastic today?",
        "Compare the effectiveness of individual consumer choices versus systemic policy changes for reducing plastic pollution. What does your model suggest about where the leverage is?",
        "How does the concept of externalized costs apply to the plastic industry — who currently pays for the environmental and health damage of plastic pollution, and who should pay?"
    ],
    "dimensions": [
        ("Science Practice", "Analyzing and Interpreting Data", "Students analyze data from their plastic pollution models to evaluate the effectiveness of different intervention strategies and identify the most impactful leverage points in the plastic lifecycle."),
        ("Disciplinary Core Idea", "ESS3.C Human Impacts on Earth Systems", "Human activities have significantly altered the biosphere through the production and disposal of persistent synthetic materials, and the consequences of plastic pollution extend through all Earth systems including the hydrosphere, atmosphere, lithosphere, and biosphere."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify the causal chain from plastic production through environmental accumulation, fragmentation, bioaccumulation, and human exposure, and evaluate how interventions at different points in this chain produce different outcomes.")
    ],
    "cast_items": [
        "Model how plastic waste moves through environmental pathways from production to oceanic accumulation and biological uptake",
        "Predict the trajectory of microplastic concentration under different production and waste management scenarios",
        "Evaluate the relative effectiveness of upstream interventions (production reduction) versus downstream interventions (recycling and cleanup)"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A community triples its recycling rate from 8% to 24% while plastic production in the region continues growing at 4% per year. According to the model, what is the most likely outcome after 20 years? A) Environmental plastic load decreases significantly B) Environmental plastic load continues growing but more slowly C) Microplastic concentration decreases D) The community achieves zero waste"),
        ("Constructed Response:", "Using your plastic pollution model, explain why microplastic concentrations in top predators like tuna fish are thousands of times higher than microplastic concentrations in the surrounding ocean water. Reference the concepts of bioaccumulation and biomagnification and at least three model components in your explanation.")
    ],
    "background_intro": "Plastic is arguably the most successful and most destructive material humanity has ever created. Since mass production began in the 1950s, we have manufactured 8.3 billion metric tons of plastic — more than one ton for every person alive today. Plastic\\'s extraordinary durability, which makes it so useful, is also what makes it so dangerous: unlike natural materials, plastic does not biodegrade. It fragments into smaller and smaller particles that persist for centuries, spreading through water, air, and soil to reach every corner of the planet and every level of the food web.",
    "background_sections": [
        ("The Scale of the Problem", "Global plastic production has increased from 2 million tons in 1950 to over 400 million tons in 2024, growing at approximately 4% per year. Of the 8.3 billion metric tons produced historically, approximately 6.3 billion tons are now waste. Only 9% has been recycled, 12% incinerated, and 79% accumulated in landfills or the natural environment. An estimated 8-12 million metric tons of plastic enter the ocean every year — equivalent to dumping a garbage truck of plastic into the ocean every minute. At current rates, plastic in the ocean will outweigh fish by 2050. This is not a waste management problem that better recycling can solve — it is a production problem driven by a petrochemical industry that plans to triple plastic output by 2060."),
        ("From Macro to Micro: The Fragmentation Cascade", "Large plastic items exposed to UV radiation, wave action, temperature fluctuations, and biological activity gradually fragment into smaller pieces. A single plastic bottle can break into thousands of microplastic fragments (less than 5mm) and eventually into nanoplastics (less than 1 micrometer) that are invisible to the naked eye. This process takes decades to centuries and is irreversible — once a microplastic exists, it persists in the environment indefinitely. Critically, fragmentation increases the total surface area of plastic, which increases its capacity to absorb toxic chemicals from the surrounding environment. Microplastics act as tiny sponges that concentrate persistent organic pollutants to levels 100,000 to 1,000,000 times higher than surrounding water."),
        ("Bioaccumulation: Plastic in the Food Web", "Marine organisms encounter microplastics throughout the food web. Zooplankton and filter feeders like mussels and oysters ingest microplastics directly from the water. Small fish eat contaminated zooplankton. Larger fish eat contaminated small fish. At each trophic level, plastic and its associated toxins accumulate — a process called biomagnification. Studies have found microplastics in 100% of marine turtle species, 59% of whale species, and 40% of seabird species examined. Humans are not exempt: recent studies have detected microplastics in human blood (80% of samples), human lungs, human placenta, and breast milk. The health effects are still being researched but include potential endocrine disruption, inflammation, and cellular damage."),
        ("Solutions: From Cleanup to System Change", "Current solutions span a spectrum from downstream cleanup to upstream system change. Ocean cleanup projects remove floating plastic but cannot address the vast majority that sinks or fragments into microplastics. Improved recycling helps but is fundamentally limited by economics — virgin plastic from cheap oil is often cheaper than recycled material. The most effective interventions target the source: banning single-use plastics (bags, straws, packaging), implementing Extended Producer Responsibility that makes manufacturers pay for waste management, developing truly biodegradable alternatives, and fundamentally redesigning products for circular economy principles. The Global Plastics Treaty negotiations represent the most significant international effort, aiming to reduce plastic production and create binding regulations — but face opposition from the petrochemical industry that profits from continued growth.")
    ],
    "lever_L": "Students identify Plastic Production Rate, Waste Management Capacity, Environmental Plastic Load, Microplastic Concentration, Bioaccumulation in Food Webs, Marine Ecosystem Health, and Human Health Exposure as key components of the plastic pollution system.",
    "lever_E": "Students determine that production rate overwhelms waste management capacity, that environmental plastic fragments into persistent microplastics over time, that bioaccumulation concentrates plastics up food chains to humans, and that only source reduction meaningfully reduces accumulation.",
    "lever_V": "Students build a computational model showing how plastic flows from production through environmental pathways to biological accumulation, revealing why downstream solutions alone are insufficient.",
    "lever_Ev": "Students run business-as-usual, improved-recycling, and system-transformation scenarios to test predictions about which interventions can reverse the growing plastic pollution trend.",
    "lever_R": "Students add chemical leaching, atmospheric transport, or extended producer responsibility to explore how additional factors affect pollution pathways and the effectiveness of policy interventions.",
    "slides_guide": [
        {
            "num": "Slide 1",
            "title": "Cover",
            "visual": "Title slide with striking image of plastic pollution contrasted with pristine ocean environment",
            "say": "8.3 billion metric tons of plastic. Where did it all go? Today we\\'re tracing every gram of it through the environment and into our own bodies.",
            "do": "Show cover image. Shock stat: Only 9% of all plastic ever made has been recycled. Ask: Where do you think the other 91% went?",
            "time": "2 min"
        },
        {
            "num": "Slide 2",
            "title": "Learning Objectives",
            "visual": "Four learning objectives with plastic pollution vocabulary terms and microplastic images",
            "say": "We\\'re not just learning about trash today — we\\'re modeling a global system that connects your plastic water bottle to microplastics in your bloodstream.",
            "do": "Have students read objectives. Pre-teach vocabulary. Key visual: show the size comparison of microplastics — smaller than a grain of rice, found everywhere on Earth.",
            "time": "3 min"
        },
        {
            "num": "Slide 3",
            "title": "Big Question",
            "visual": "The question displayed over infographic showing plastic production curve, waste fate, and microplastic detection in human tissue",
            "say": "Plastic has been found in human blood, lungs, placenta, and breast milk. How did it get there? Trace the pathway from a plastic bag to your body.",
            "do": "Quick-write: Students write their initial hypothesis about how plastic reaches the human body. Save for comparison after modeling.",
            "time": "3 min"
        },
        {
            "num": "Slide 4",
            "title": "LEVER Framework",
            "visual": "LEVER steps overview with plastic lifecycle examples",
            "say": "We\\'ll model the entire lifecycle of plastic — from production to your bloodstream. This model will reveal why some solutions work and others don\\'t.",
            "do": "Preview LEVER steps. Emphasize that this model will challenge assumptions about recycling as a solution. The model follows the plastic, not the narrative.",
            "time": "2 min"
        },
        {
            "num": "Slide 5",
            "title": "Activity 1: Components",
            "visual": "Seven component cards for sorting with plastic lifecycle illustrations",
            "say": "Which components are external drivers of the plastic pollution system, and which are internal consequences? Think about what pushes plastic into the environment versus what happens once it\\'s there.",
            "do": "Guide sorting: External = Plastic Production Rate, Waste Management Capacity (human decisions). Internal = the five environmental and biological responses. Discuss: Is human health exposure an endpoint or a feedback that could change production policy?",
            "time": "8 min"
        },
        {
            "num": "Slide 6",
            "title": "Activity 2: Connections",
            "visual": "Relationship diagram template showing the seven components arranged as a flow from production to human exposure",
            "say": "Trace the journey: production to environment to microplastics to food web to your body. Where are the positive feedback loops? Where are the bottlenecks that determine how much plastic reaches each stage?",
            "do": "Students draw arrows with + or - signs. Key insight: the one-way nature of plastic fragmentation — once microplastics exist, they persist essentially forever. There is no natural cleanup mechanism.",
            "time": "8 min"
        },
        {
            "num": "Slide 7",
            "title": "Activity 3: Simulation",
            "visual": "Simulation interface showing three scenarios with graphs of plastic load, microplastic concentration, and bioaccumulation over time",
            "say": "Run all three scenarios. Pay attention to the recycling-only scenario — does tripling recycling solve the problem? Why or why not?",
            "do": "Students run scenarios and compare outcomes. Key discussion: Why does improved recycling barely slow the trend? Guide them to see that 4% production growth overwhelms even tripled recycling. Only source reduction changes the trajectory.",
            "time": "10 min"
        },
        {
            "num": "Slide 8",
            "title": "Discoveries",
            "visual": "Four key discoveries with graphs showing why recycling alone fails and why source reduction is essential",
            "say": "The biggest finding: recycling is necessary but mathematically insufficient. When production grows faster than recycling improves, the problem gets worse no matter how much you recycle.",
            "do": "Class discussion. Compare initial hypotheses to model evidence. Challenge question: If recycling alone can\\'t solve this, what does that tell us about where the real solution must come from?",
            "time": "5 min"
        },
        {
            "num": "Slide 9",
            "title": "STEM Challenge",
            "visual": "Engineering challenge: Design a zero-plastic-waste community system for a coastal town of 100,000",
            "say": "Your community generates 15,000 tons of plastic waste per year and it\\'s contaminating local fisheries. Design a system that eliminates plastic pollution at every stage — from what enters the community to what leaves it.",
            "do": "Groups design comprehensive systems addressing production reduction, material substitution, waste management, and environmental remediation. Present with evidence from model simulations.",
            "time": "12 min"
        }
    ],
    "sort_reasoning": "Plastic Production Rate and Waste Management Capacity are external components because they represent human-controlled inputs to the pollution system — they determine how much plastic enters and how much is managed. Environmental Plastic Load, Microplastic Concentration, Bioaccumulation in Food Webs, Marine Ecosystem Health, and Human Health Exposure are internal because they are consequences that emerge within the environmental and biological system once plastic enters it — they represent the cascade of effects that the system produces in response to the external inputs.",
    "relationships": [
        ("Plastic Production Rate to Environmental Plastic Load", "POSITIVE (+)", "Higher production rates generate more plastic waste, and since waste management captures only a fraction, the excess accumulates in the environment. A 4% annual production increase outpaces improvements in recycling."),
        ("Waste Management Capacity to Environmental Plastic Load", "NEGATIVE (-)", "Better waste management — higher recycling rates, improved collection, safer disposal — reduces the fraction of produced plastic that leaks into the environment, though it cannot offset unlimited production growth."),
        ("Environmental Plastic Load to Microplastic Concentration", "POSITIVE (+)", "More plastic in the environment means more material undergoing fragmentation through UV exposure, physical abrasion, and biological processes, steadily increasing the concentration of microplastic particles."),
        ("Microplastic Concentration to Bioaccumulation in Food Webs", "POSITIVE (+)", "Higher environmental microplastic concentrations mean more particles are ingested by organisms at the base of the food web, which then concentrate through biomagnification at each trophic level."),
        ("Bioaccumulation in Food Webs to Human Health Exposure", "POSITIVE (+)", "As microplastics and their associated toxins accumulate in seafood and other food products, human dietary exposure increases proportionally, particularly for populations that consume large amounts of fish and shellfish."),
        ("Marine Ecosystem Health to Bioaccumulation in Food Webs", "NEGATIVE (-)", "Declining marine ecosystem health reduces the abundance and diversity of organisms, but the surviving organisms in degraded ecosystems often have higher plastic loads because there are fewer organisms to dilute the plastic across the food web.")
    ],
    "sim_answers": [
        ("Business As Usual", "With production growing at 4% per year and only 9% recycled, Environmental Plastic Load increases exponentially. By year 30, ocean plastic has more than doubled. Microplastic Concentration rises steadily as accumulated macroplastics continue fragmenting. Bioaccumulation in Food Webs increases to the point where virtually all marine organisms contain detectable microplastics, and Human Health Exposure through seafood, water, and air becomes significant. Marine Ecosystem Health declines measurably."),
        ("Recycling Focus", "Tripling recycling from 9% to 27% is insufficient because production continues growing at 4% per year. In absolute terms, more plastic enters the environment in year 20 than in year 1 despite improved recycling, because the total volume of plastic produced has grown so much. The model clearly demonstrates the mathematical impossibility of recycling our way out of a production growth problem. Microplastic Concentration continues rising because existing environmental plastic keeps fragmenting regardless of improved recycling of new waste.")
    ],
    "reflection_exemplars": [
        ("Why can\\'t recycling solve the plastic crisis?", "The model demonstrates a simple mathematical reality: if production grows at 4% per year, total production doubles every 18 years. Even tripling recycling from 9% to 27% captures only a small fraction of this exponentially growing volume. In absolute terms, 27% of a tripled production is still more unrecycled plastic than 91% of the original production was. Furthermore, recycling faces economic and technical barriers — many plastics cannot be recycled, contamination reduces quality, and virgin plastic from cheap oil undercuts recycled material prices. The model shows that recycling is necessary but can only reduce the rate of environmental accumulation, not reverse it. Only reducing production at the source changes the fundamental trajectory."),
        ("How does a plastic bottle end up in your bloodstream?", "The model traces the pathway: a discarded bottle enters the environment through inadequate waste management. UV radiation and physical weathering fragment it into microplastic particles over months to years. These particles enter waterways and eventually the ocean, where they are ingested by zooplankton and filter feeders. Small fish eat contaminated zooplankton, larger fish eat those, and biomagnification concentrates the plastic and its absorbed toxins at each trophic level. When humans eat seafood, drink water, or breathe air containing microplastics, the particles enter the body. Studies have now detected microplastics in human blood, lungs, placenta, and breast milk — confirming that the pathway from production to human tissue is complete and operating continuously.")
    ],
    "stem_intro": "Present the challenge: A coastal community of 100,000 generates 15,000 tons of plastic waste annually, with only 8% recycled. Storm runoff washes landfill plastic into the ocean, contaminating local fisheries. The community has committed to zero plastic waste within 15 years. Use your model data to design a system that addresses every stage of the plastic lifecycle — what enters the community, how it\\'s used, and what happens to it after use.",
    "stem_concepts": [
        ("Material Substitution and Redesign", "Replacing single-use plastics with reusable, compostable, or recyclable alternatives — this includes redesigning packaging to use fewer materials, switching to paper, glass, metal, or certified compostable bioplastics, and eliminating unnecessary packaging entirely. Material substitution addresses the source of the problem rather than managing its symptoms."),
        ("Extended Producer Responsibility", "A policy framework that shifts the cost and responsibility for waste management from taxpayers and municipalities to the companies that produce and sell plastic products. EPR creates economic incentives for manufacturers to reduce packaging, design for recyclability, and fund collection and recycling infrastructure. Countries with strong EPR laws achieve recycling rates 3-5 times higher than those without."),
        ("Waste-to-Value Technologies", "Advanced recycling technologies that convert plastic waste into useful products — including chemical recycling (breaking polymers back to monomers), pyrolysis (converting plastic to fuel), and biorefinery approaches. These technologies can process plastics that mechanical recycling cannot handle but are energy-intensive and must be evaluated for their full lifecycle environmental impact.")
    ],
    "stem_eval": [
        ("Expert (4)", "System addresses all lifecycle stages from production to disposal, uses model evidence to justify intervention points, includes material substitution and policy mechanisms, provides realistic implementation timeline, and accounts for existing environmental plastic"),
        ("Proficient (3)", "System addresses most lifecycle stages with reasonable strategies and some connection to model data, includes consideration of both upstream and downstream interventions"),
        ("Developing (2)", "System focuses primarily on recycling and cleanup without addressing production and consumption, or strategies are not well connected to model evidence"),
        ("Beginning (1)", "System is incomplete, focuses on a single intervention, or does not connect strategies to the plastic pollution dynamics revealed by the model")
    ],
    "support": [
        "Provide a visual lifecycle flow diagram of a plastic bottle from oil extraction to ocean microplastic — students can identify intervention points at each stage and evaluate which are most effective",
        "Use the bathtub analogy: the faucet is production, the drain is recycling, and the tub is the environment. If the faucet runs faster than the drain, the tub overflows no matter how big the drain is. What\\'s the most effective solution?",
        "Sentence frames: \\'The model shows that ___ is more effective than ___ because ___. Even though ___ seems helpful, the data shows ___ because ___ grows faster than ___ improves.\\'"
    ],
    "extensions": [
        "Research the Global Plastics Treaty negotiations — analyze the competing proposals from environmental groups (binding production caps) versus the petrochemical industry (improved waste management only) and evaluate which approach your model supports",
        "Design and conduct a microplastic sampling study of local water sources — collect water samples, filter them, and examine the filters under a microscope to quantify microplastic concentration in your community\\'s water",
        "Investigate the environmental justice dimensions of plastic pollution — map the locations of plastic production facilities, waste incinerators, and landfills relative to community demographics and analyze the patterns of exposure disparity"
    ],
    "cross_curr": [
        ("Math", "Model the exponential growth of plastic production at 4% annually and calculate when ocean plastic will outweigh fish. Then calculate the recycling rate needed to achieve net-zero environmental accumulation at current production growth rates — is it mathematically possible?"),
        ("ELA", "Read and analyze the marketing campaigns of major plastic producers who promoted recycling as the solution to plastic pollution starting in the 1970s. Evaluate whether these campaigns were genuine solutions or strategic deflection of responsibility from producers to consumers."),
        ("History", "Research the history of lead pollution — from leaded gasoline to lead paint — as a case study of how industries delayed regulation of harmful products through doubt manufacturing, lobbying, and promoting individual responsibility. Compare the timelines and strategies to the plastic industry\\'s current approach.")
    ],
    "misconceptions": [
        ("Recycling solves the plastic problem", "Only 9% of all plastic ever produced has been recycled, and recycling rates have not improved significantly in decades. Many plastics cannot be technically recycled, contamination reduces quality, and recycled plastic is often more expensive than virgin material made from cheap oil. Furthermore, most recycling is actually downcycling — converting a bottle into a lower-quality product that is eventually landfilled anyway. The model shows that even dramatically increased recycling cannot offset continued production growth.", "Present the math: If production grows 4% per year (doubling every 18 years) and recycling improves from 9% to 27% over the same period, calculate the absolute tons of unrecycled plastic in year 1 versus year 18. Students will see that the absolute waste volume increased despite tripled recycling."),
        ("Biodegradable plastics solve the problem", "Most products labeled biodegradable only break down under specific industrial composting conditions (high temperature, specific microorganisms) that don\\'t exist in landfills or oceans. In landfills, biodegradable plastics behave identically to conventional plastics for decades. In the ocean, they fragment into microplastics just like conventional plastic. Truly compostable plastics can be part of the solution but only with proper collection infrastructure and honest labeling — otherwise they give consumers a false sense of environmental safety.", "Bring in samples of biodegradable and conventional plastic. Ask: If these both end up in the ocean, how differently do you think they behave? Show research that biodegradable plastics fragment into microplastics in marine environments just like conventional plastic."),
        ("Ocean cleanup can remove the plastic that\\'s already there", "Ocean cleanup projects like The Ocean Cleanup can remove some floating macroplastics, but they cannot capture the vast majority of ocean plastic — 94% of which has sunk below the surface or fragmented into microplastics too small to collect. The surface plastic that cleanup projects target represents a small fraction of total ocean plastic. Furthermore, cleanup addresses the symptom while the cause — continued production and dumping — adds new plastic faster than any cleanup can remove it. The model shows that cleanup without source reduction is like mopping the floor while the faucet overflows.", "Show the scale comparison: Ocean cleanup projects remove approximately 100,000 tons per year; 8-12 million tons enter the ocean annually. Ask: At this rate, are we falling behind or catching up? Guide students to see that cleanup is 100x slower than input.")
    ]
}

L05 = {
    "id": "G12L2-L05",
    "title": "Why Are Species Going Extinct So Fast?",
    "subtitle": "Modeling Biodiversity Loss, Habitat Fragmentation, and Extinction Cascades",
    "ngss": "HS-LS2-7",
    "ngss_desc": "Design, evaluate, and refine a solution for reducing the impacts of human activities on the environment and biodiversity.",
    "big_question": "Species are disappearing at 1,000 times the natural background rate — a pace not seen since the asteroid that killed the dinosaurs 66 million years ago — so what is driving this sixth mass extinction, and what happens to ecosystems and human civilization when the web of life unravels?",
    "objectives": [
        "Model how habitat loss, fragmentation, climate change, and species interdependencies interact to drive accelerating biodiversity decline",
        "Explain why habitat fragmentation is more damaging than simple habitat loss because it reduces population viability and blocks migration corridors",
        "Predict the conditions under which keystone species loss triggers extinction cascades through dependent species networks",
        "Analyze conservation strategies and evaluate their effectiveness using model evidence about the drivers and dynamics of biodiversity loss"
    ],
    "vocabulary": [
        ("Habitat Fragmentation", "The division of continuous habitat into smaller, isolated patches by roads, agriculture, or development — fragmentation is more damaging than simple area loss because it creates edge effects, blocks migration, isolates populations genetically, and prevents species from tracking climate change"),
        ("Extinction Cascade", "A chain reaction in which the loss of one species triggers the decline or extinction of dependent species — like removing a card from a house of cards, losing a keystone species can cause a collapse that propagates through the entire food web"),
        ("Minimum Viable Population", "The smallest population size at which a species can survive long-term without inbreeding depression, genetic drift, or demographic stochasticity driving it to extinction — for most mammals, this is estimated at 500-5,000 individuals, far more than many fragmented populations contain"),
        ("Ecosystem Services", "The benefits humans receive from functioning ecosystems — including pollination of 75% of food crops, water purification, flood control, carbon storage, soil formation, and pharmaceutical compounds, all of which are provided by biodiversity and degraded by its loss")
    ],
    "components": [
        ("Land Use Change Rate", "The speed at which natural habitat is converted to agriculture, urban development, or infrastructure — currently, an area of primary forest the size of a football field is cleared every 6 seconds, and 75% of Earth\\'s ice-free land has been significantly altered by humans", True),
        ("Climate Velocity", "The speed at which climate zones are shifting geographically due to global warming — species must migrate to track their preferred climate, but fragmented habitats and physical barriers often prevent movement, trapping species in unsuitable conditions", True),
        ("Habitat Connectivity", "The degree to which remaining natural areas are linked by corridors that allow species to move between habitat patches — high connectivity allows gene flow, migration, and climate tracking, while low connectivity isolates populations and accelerates local extinction", False),
        ("Population Viability", "The likelihood that a species population can persist long-term given its size, genetic diversity, reproductive rate, and habitat quality — small, isolated populations face inbreeding depression, genetic drift, and higher vulnerability to random events like disease or drought", False),
        ("Species Interaction Network", "The web of predator-prey, pollinator-plant, parasite-host, and mutualistic relationships that connect species — the loss of one species can cascade through the network, affecting dozens of dependent species in ways that are difficult to predict", False),
        ("Ecosystem Function Index", "The overall capacity of an ecosystem to perform essential functions like nutrient cycling, water purification, pollination, and carbon storage — function declines as species are lost, though the relationship is not linear: some species can be lost without major function loss, but past a threshold, ecosystem function collapses rapidly", False),
        ("Extinction Rate", "The number of species going extinct per unit time — currently estimated at 100-1,000 times the natural background rate of 1-5 species per year, with projections suggesting 1 million species face extinction within decades without major conservation intervention", False)
    ],
    "think_about_it": "When Land Use Change fragments habitat and Climate Velocity requires species to migrate, but Habitat Connectivity is low, what happens to Population Viability? If a keystone species like a pollinator falls below its Minimum Viable Population, how does that cascade through the Species Interaction Network?",
    "scenarios": [
        ("Continued Habitat Loss", "Maintain current Land Use Change Rate with moderate Climate Velocity — observe how ongoing deforestation and development affect Habitat Connectivity, Population Viability, and Extinction Rate over 30 years"),
        ("Climate Shift Without Corridors", "Increase Climate Velocity while Habitat Connectivity remains fragmented — observe whether species can track their required climate conditions and what happens to populations trapped in warming habitat patches"),
        ("Conservation Corridor Strategy", "Maintain current land use pressures but dramatically increase Habitat Connectivity through wildlife corridors — observe whether reconnecting habitat patches can improve Population Viability and reduce Extinction Rate even under continued climate change")
    ],
    "sim_scenarios": [
        ("Continued Habitat Loss", "Land Use Change: Current Rate | Climate Velocity: Moderate | Habitat Connectivity: Declining", "If habitat loss continues at current rates, what do you predict happens to Population Viability and Extinction Rate over 30 years? Is the decline linear or accelerating?"),
        ("Climate Without Corridors", "Land Use Change: Current | Climate Velocity: High | Habitat Connectivity: Low (Fragmented)", "When climate zones shift rapidly but fragmented habitats prevent species from migrating, what happens? Which types of species are most vulnerable?"),
        ("Connected Landscape", "Land Use Change: Current | Climate Velocity: Moderate | Habitat Connectivity: High (Corridors)", "Can wildlife corridors connecting habitat fragments significantly reduce extinction rates even without stopping habitat loss? What does the model show?")
    ],
    "discoveries": [
        "Extinction rates accelerate non-linearly as habitat is lost — the first 30% of habitat loss causes relatively few extinctions, but beyond 70% loss, extinction rates explode because remaining populations are too small and isolated to be viable",
        "Habitat fragmentation is more damaging than equivalent area loss because it creates edge effects, blocks migration, isolates gene pools, and prevents species from tracking climate change — a single connected habitat supports far more species than the same area divided into isolated fragments",
        "Extinction cascades through Species Interaction Networks mean that the direct loss of one keystone species can trigger the decline of dozens of dependent species — the actual extinction toll is always higher than the directly impacted species count",
        "Wildlife corridors that reconnect fragmented habitats significantly improve Population Viability and reduce Extinction Rate even without stopping habitat loss — connectivity is a force multiplier that makes existing protected areas far more effective"
    ],
    "answer": "Species are going extinct at 1,000 times the natural rate because of the combined and compounding effects of habitat destruction, fragmentation, climate change, pollution, and overexploitation. The model reveals that habitat fragmentation is particularly devastating because it does not just reduce the total area available to species — it isolates populations into patches too small to be genetically viable, blocks the migration corridors species need to track climate change, and creates edge effects that degrade even the remaining habitat. Extinction cascades amplify the direct losses: when a keystone species like a pollinator disappears, the plants it pollinated decline, the animals that ate those plants decline, and the cascade propagates through the entire species interaction network. The model shows a critical non-linearity: ecosystems can absorb some species loss with minimal functional impact, but past a threshold, ecosystem services like pollination, water purification, and carbon storage collapse rapidly. The most effective conservation strategy is not creating isolated protected areas but connecting them through wildlife corridors that enable gene flow and climate migration — turning habitat islands into a functional network.",
    "stem_title": "Design a Biodiversity Conservation Network",
    "stem_mission": "Design a connected conservation network for a region experiencing rapid development that maximizes species survival by linking existing protected areas through strategic wildlife corridors.",
    "stem_scenario": "A region with exceptional biodiversity has 15 existing protected areas covering 12% of the landscape, but they are isolated from each other by agriculture, roads, and urban development. Climate models project that many species will need to shift their ranges 50-100 km northward over the next 50 years. Currently, the fragmented landscape makes this migration impossible for most species. A conservation coalition has hired your team to design a corridor network that connects the 15 protected areas, enables climate migration, and prioritizes the species and habitats most at risk. Your budget is limited, so you must use your model data to identify the most strategic connections.",
    "stem_questions": [
        "Based on your model, which connections between protected areas would have the greatest impact on reducing Extinction Rate — those linking the largest areas, those linking the most diverse areas, or those enabling northward climate migration?",
        "What does your model suggest about the minimum width and habitat quality requirements for corridors to actually support species movement?",
        "How does your model\\'s Species Interaction Network data help you identify which species are most critical to protect to prevent extinction cascades?"
    ],
    "stem_design_qs": [
        "Which corridor connections does your network prioritize and why — what model evidence supports these choices?",
        "How does your network design account for both current biodiversity hotspots and projected climate migration needs?",
        "What keystone species does your plan specifically target for protection, and how does preventing their loss reduce cascade risk?",
        "How does your plan balance conservation needs with the economic interests of landowners and developers in corridor zones?"
    ],
    "career": "Conservation biologists who study biodiversity loss and design protected area networks work for national parks, wildlife agencies, and organizations like the Nature Conservancy and World Wildlife Fund, earning $50,000-$110,000/year. Wildlife corridor planners who design landscape-level connectivity for species movement earn $55,000-$105,000/year. Ecological modelers who build computational simulations of species interactions and extinction dynamics earn $65,000-$130,000/year at universities and research institutions.",
    "images": {
        "cover": ("G12L2-L05-cover.png", "A photorealistic image of diverse 17-18 year old students using binoculars and field guides in a nature reserve during a biodiversity survey, with a diverse forest ecosystem and visible wildlife in the background"),
        "landscape": ("G12L2-L05-landscape.png", "A photorealistic aerial image showing a landscape with forest fragments separated by agriculture and development, with a visible wildlife corridor connecting two larger forest patches, illustrating habitat connectivity"),
        "modeling": ("G12L2-L05-modeling.png", "A photorealistic image of diverse 17-18 year old students working on species interaction network models on their laptops, with a large food web diagram and habitat map projected on a smartboard"),
        "discussion": ("G12L2-L05-discussion.png", "A photorealistic image of a teacher leading a discussion with diverse 17-18 year old students about extinction cascades, with an interactive species interaction network displayed on screen showing cascade propagation"),
        "stem": ("G12L2-L05-stem.png", "A photorealistic image of diverse 17-18 year old students designing wildlife corridor networks on large maps spread across tables, using data printouts and species habitat requirements to plan connections")
    },
    "pre_assessment": [
        "How many species do you think go extinct every day? What do you think is the main cause?",
        "What is the difference between a species losing half of its habitat in one large area versus losing that same amount but split into many small, isolated fragments? Which is worse for the species?",
        "Can you think of examples where the loss of one species could cause other species to decline? How might species be connected?",
        "Why should humans care about biodiversity loss? What do we depend on from other species?"
    ],
    "extend_components": [
        ("Invasive Species Pressure", "The impact of non-native species introduced by human activity — invasive species compete with, prey on, or bring diseases to native species, and their impact is amplified in fragmented habitats where native populations are already stressed and cannot escape"),
        ("Genetic Diversity Index", "The range of genetic variation within a species population — small, isolated populations lose genetic diversity through drift and inbreeding, reducing their ability to adapt to changing conditions and making them vulnerable to diseases that can sweep through genetically uniform populations"),
        ("Protected Area Effectiveness", "The degree to which designated conservation areas actually protect biodiversity — many protected areas are too small, poorly managed, or isolated to maintain viable populations, and some exist only on paper with no real enforcement of protection")
    ],
    "reflections": [
        "Why does your model show that extinction rates accelerate non-linearly as habitat loss increases? What happens at the threshold where populations become too small to be viable?",
        "How does habitat fragmentation multiply the damage of habitat loss? Use specific examples from your model to explain why connectivity matters more than total area.",
        "What are extinction cascades and why do they mean the true impact of losing one species is always greater than it appears? Trace a cascade through your model\\'s species interaction network.",
        "Your model showed that wildlife corridors significantly reduce extinction rates even without stopping habitat loss. What is it about connectivity that makes this possible?",
        "What are the ethical dimensions of biodiversity conservation — do species have a right to exist independent of their utility to humans, or is the ecosystem services argument sufficient justification for conservation?"
    ],
    "dimensions": [
        ("Science Practice", "Designing Solutions", "Students design evidence-based conservation networks using their biodiversity models to identify the most strategic connections between protected areas, prioritizing species at highest risk and enabling climate migration."),
        ("Disciplinary Core Idea", "LS2.C Ecosystem Dynamics, Functioning, and Resilience", "Biodiversity is the foundation of ecosystem stability and resilience. As species are lost, ecosystem functions degrade, and past critical thresholds, ecosystems can shift to fundamentally different and less productive states."),
        ("Crosscutting Concept", "Systems and System Models", "Students model biodiversity as a complex network of interacting species where the loss of individual nodes can cascade through connections to affect the entire system, and use this systems understanding to design effective conservation strategies.")
    ],
    "cast_items": [
        "Model how habitat loss, fragmentation, and climate change interact to drive accelerating extinction rates",
        "Predict extinction cascade dynamics based on species interaction network structure and keystone species vulnerability",
        "Design and evaluate conservation corridor networks using model evidence about connectivity, population viability, and climate migration requirements"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A region has lost 50% of its forest habitat. Which scenario results in higher extinction rates? A) The remaining 50% is in one continuous block B) The remaining 50% is in 20 small, isolated fragments C) The remaining 50% is in 20 fragments connected by wildlife corridors D) Fragmentation does not affect extinction rates if total area is the same"),
        ("Constructed Response:", "A keystone pollinator species has been declining due to habitat fragmentation. Using your biodiversity model, predict what happens to the ecosystem when this species falls below its minimum viable population. Trace the extinction cascade through at least three levels of the species interaction network and explain why the total species impact exceeds the loss of just the pollinator.")
    ],
    "background_intro": "Earth is currently experiencing its sixth mass extinction event — the first caused by a single species. The current extinction rate is estimated at 100-1,000 times higher than the natural background rate, rivaling the pace of the asteroid impact that ended the dinosaurs 66 million years ago. Unlike previous mass extinctions driven by catastrophic physical events, this one is driven by the cumulative effects of habitat destruction, fragmentation, climate change, pollution, and overexploitation — all consequences of human activity that are accelerating rather than abating.",
    "background_sections": [
        ("The Scale of Biodiversity Loss", "The 2019 Global Assessment Report on Biodiversity found that approximately 1 million animal and plant species are threatened with extinction within decades — more than at any time in human history. Since 1970, monitored wildlife populations have declined by an average of 69%. Amphibians are the most threatened vertebrate class, with 41% of species at risk. Insect populations have declined by 45% globally over the past 40 years, with devastating implications for pollination and food webs. The Living Planet Index tracks vertebrate populations and shows consistent, accelerating decline across all major ecosystems — freshwater species have declined by 83%, the most of any group. These losses are not just numbers — each represents the unraveling of ecological relationships built over millions of years of evolution."),
        ("Habitat Fragmentation: Death by a Thousand Cuts", "Habitat fragmentation is arguably the most damaging driver of biodiversity loss because it multiplies the effects of all other threats. When continuous forest is divided by roads and agriculture, each resulting fragment suffers from edge effects — changes in microclimate, light, humidity, and wind penetration that alter habitat quality for 100-300 meters inward from each edge. A 100-hectare fragment may have only 20 hectares of true interior habitat. Small fragments cannot support minimum viable populations of large predators, dispersal between fragments is blocked for many species, and genetic isolation leads to inbreeding depression within a few generations. Critically, fragmentation also prevents species from migrating in response to climate change — they are trapped in habitat islands surrounded by hostile landscape."),
        ("Extinction Cascades: The Domino Effect", "Ecosystems are networks of interdependent species, and the loss of one species can cascade through these connections in ways that multiply the direct impact. The classic example is the reintroduction of wolves to Yellowstone: wolves reduced elk overgrazing, which allowed willows and aspens to recover, which stabilized stream banks, which improved habitat for fish and beaver, which created ponds that supported amphibians and songbirds — one species affected dozens. The reverse is also true: losing a keystone species can trigger a cascade of declines. Pollinator loss threatens the 75% of food crops that depend on animal pollination. The decline of large herbivores reduces seed dispersal and nutrient cycling. The loss of apex predators causes herbivore population explosions that overgraze vegetation. Each lost species weakens the network for the survivors."),
        ("Conservation Corridors: Reconnecting the Landscape", "The most promising strategy for combating fragmentation-driven extinction is creating wildlife corridors — strips of habitat that connect isolated protected areas. Corridors enable gene flow between isolated populations (preventing inbreeding), allow animals to migrate in response to climate change, increase effective habitat area by combining connected fragments, and enable recolonization after local extinctions. The Yellowstone to Yukon Conservation Initiative (Y2Y) is creating a 3,200-km corridor connecting protected areas from Yellowstone to the Canadian Yukon, enabling grizzly bear, caribou, and other wide-ranging species to maintain viable populations across their full range. Research consistently shows that connected reserves support 20-30% more species than isolated reserves of the same total area.")
    ],
    "lever_L": "Students identify Land Use Change Rate, Climate Velocity, Habitat Connectivity, Population Viability, Species Interaction Network, Ecosystem Function Index, and Extinction Rate as key components of the biodiversity system.",
    "lever_E": "Students determine that habitat loss and fragmentation reduce population viability, that climate velocity creates migration pressure that fragmentation prevents, that species interaction networks transmit extinction cascades, and that connectivity is the key moderating variable.",
    "lever_V": "Students build a computational model showing how habitat loss and fragmentation interact with climate change to drive species decline, and how corridor connectivity can moderate extinction dynamics.",
    "lever_Ev": "Students run continued habitat loss, climate-without-corridors, and connected landscape scenarios to test predictions about the relative effectiveness of different conservation strategies.",
    "lever_R": "Students add invasive species pressure, genetic diversity, or protected area effectiveness to explore how additional factors affect extinction dynamics and conservation outcomes.",
    "slides_guide": [
        {
            "num": "Slide 1",
            "title": "Cover",
            "visual": "Title slide with powerful image showing diverse wildlife alongside habitat fragmentation aerial imagery",
            "say": "We\\'re in the middle of the sixth mass extinction. Species are disappearing 1,000 times faster than normal. Today we\\'re modeling why — and what we can do about it.",
            "do": "Show cover image. Quick stat: Since 1970, 69% of monitored wildlife populations have declined. Ask: What do you think is the main cause? Take predictions.",
            "time": "2 min"
        },
        {
            "num": "Slide 2",
            "title": "Learning Objectives",
            "visual": "Four learning objectives with biodiversity vocabulary terms and habitat images",
            "say": "By the end of today, you\\'ll understand not just that species are disappearing, but the specific mechanisms that drive extinction — and why the pattern is accelerating.",
            "do": "Have students read objectives. Pre-teach vocabulary. Key concept: fragmentation — cutting habitat into pieces is worse than just losing area. Use the puzzle analogy: a complete picture with some pieces missing versus the same pieces scattered randomly.",
            "time": "3 min"
        },
        {
            "num": "Slide 3",
            "title": "Big Question",
            "visual": "Provocative question displayed over graphs showing extinction rate versus deep time background rate",
            "say": "The last time species disappeared this fast, an asteroid had just hit the planet. This time, the asteroid is us. But unlike an asteroid, we can choose to change course. What would that take?",
            "do": "Quick-write: Students write their initial explanation for why extinctions are accelerating and what they think the most important intervention would be. Save for comparison.",
            "time": "3 min"
        },
        {
            "num": "Slide 4",
            "title": "LEVER Framework",
            "visual": "LEVER steps overview with biodiversity conservation examples",
            "say": "We\\'ll model the extinction crisis as a system to understand the dynamics that drive it. This model will reveal something important: connectivity changes everything.",
            "do": "Preview LEVER steps. Emphasize that understanding the system dynamics of extinction helps us find the highest-leverage interventions — places where a small change produces a big result.",
            "time": "2 min"
        },
        {
            "num": "Slide 5",
            "title": "Activity 1: Components",
            "visual": "Seven component cards for sorting with biodiversity illustrations",
            "say": "Which components are external pressures acting on biodiversity from outside, and which are internal responses within the ecological system?",
            "do": "Guide sorting: External = Land Use Change Rate (human decisions), Climate Velocity (global warming). Internal = the five ecological responses. Discuss: Why is Habitat Connectivity internal even though humans build the roads that fragment it?",
            "time": "8 min"
        },
        {
            "num": "Slide 6",
            "title": "Activity 2: Connections",
            "visual": "Relationship diagram with all seven components and space for arrows",
            "say": "Trace the pathway from habitat loss to extinction. But also look for the multiplier effect — where does fragmentation make everything worse? Where do cascades propagate?",
            "do": "Students draw arrows. Key discoveries: the cascading effect through Species Interaction Networks, and the central role of Habitat Connectivity in moderating multiple pathways. Ask: Which component, if improved, would have the biggest ripple effect?",
            "time": "8 min"
        },
        {
            "num": "Slide 7",
            "title": "Activity 3: Simulation",
            "visual": "Simulation interface showing three scenarios with extinction rate, connectivity, and ecosystem function graphs",
            "say": "Run all three scenarios and focus on the conservation corridor scenario. Does reconnecting habitat actually reduce extinction rates, even without stopping habitat loss?",
            "do": "Students run scenarios. Key discussion: Compare the corridor scenario to continued habitat loss. The improvement from connectivity alone should be striking. Ask: Why does connecting the same total area of habitat produce such different results?",
            "time": "10 min"
        },
        {
            "num": "Slide 8",
            "title": "Discoveries",
            "visual": "Four key discoveries with graphs showing non-linear extinction, fragmentation effects, cascades, and corridor benefits",
            "say": "Our model reveals four critical insights about why species are disappearing and what we can do. The most powerful finding: connectivity is a force multiplier for conservation.",
            "do": "Class discussion. Compare initial predictions to model evidence. Challenge: If corridors are so effective, why aren\\'t we building them everywhere? What are the barriers?",
            "time": "5 min"
        },
        {
            "num": "Slide 9",
            "title": "STEM Challenge",
            "visual": "Engineering challenge: Design a conservation corridor network connecting 15 protected areas",
            "say": "You have a limited budget to connect 15 protected areas in a developing region. Which connections do you prioritize? Use your model data to design the most effective network possible.",
            "do": "Groups design corridor networks on regional maps, prioritizing connections based on model evidence about species vulnerability, climate migration needs, and keystone species protection. Present and defend design choices.",
            "time": "12 min"
        }
    ],
    "sort_reasoning": "Land Use Change Rate and Climate Velocity are external components because they represent pressures acting on the biodiversity system from outside — human development decisions and global warming trends that biodiversity must respond to but cannot control. Habitat Connectivity, Population Viability, Species Interaction Network, Ecosystem Function Index, and Extinction Rate are internal because they are properties of the ecological system that respond to external pressures and interact with each other through complex feedback loops — they represent how biodiversity processes and responds to the pressures imposed on it.",
    "relationships": [
        ("Land Use Change Rate to Habitat Connectivity", "NEGATIVE (-)", "More rapid land conversion fragments remaining habitat into smaller, more isolated patches, reducing the corridors and connections that species need for movement, gene flow, and migration."),
        ("Habitat Connectivity to Population Viability", "POSITIVE (+)", "Higher connectivity enables gene flow between populations, access to mates and resources across larger areas, and migration in response to climate change — all of which increase the likelihood that populations remain above minimum viable levels."),
        ("Climate Velocity to Population Viability", "NEGATIVE (-)", "Faster climate zone shifts require faster species migration. When climate velocity exceeds a species\\' dispersal ability — especially in fragmented landscapes — populations become trapped in unsuitable conditions and decline."),
        ("Population Viability to Species Interaction Network", "POSITIVE (+)", "When populations are viable and stable, they maintain their roles in the species interaction network — as predators, pollinators, seed dispersers, and nutrient cyclers. Population decline weakens or removes these connections."),
        ("Species Interaction Network to Extinction Rate", "NEGATIVE (-)", "A robust interaction network with many species and connections provides redundancy and resilience — the loss of one species can be partially compensated by others. As the network degrades, this resilience disappears and extinction cascades become more likely."),
        ("Ecosystem Function Index to Population Viability", "POSITIVE (+)", "Healthy ecosystem function provides the resources, habitat quality, and environmental stability that species need to maintain viable populations. Declining function degrades habitat quality for all remaining species.")
    ],
    "sim_answers": [
        ("Continued Habitat Loss", "With ongoing habitat loss and declining connectivity, the model shows Population Viability dropping below minimum viable thresholds for an increasing number of species. Extinction Rate accelerates non-linearly — slowly at first, then rapidly as habitat drops below 30% of original extent. Species Interaction Network degrades as species are lost, triggering cascades that drive additional extinctions beyond those directly caused by habitat loss. Ecosystem Function Index shows gradual decline followed by rapid collapse as critical thresholds are crossed."),
        ("Climate Without Corridors", "High climate velocity combined with fragmented habitat produces the worst outcomes. Species that need to migrate northward are trapped in warming habitat patches. Species with small ranges and limited dispersal ability go extinct first, followed by those that depend on them. The model demonstrates that climate change and fragmentation are a lethal combination — either alone is manageable for many species, but together they drive extinctions that neither factor would cause independently."),
        ("Connected Landscape", "Wildlife corridors dramatically improve outcomes even without reducing habitat loss. Population Viability increases because connected populations have larger effective sizes, better genetic diversity, and access to resources across a wider landscape. Species can track climate shifts through the corridor network. The model shows a 20-30% reduction in Extinction Rate from connectivity alone — demonstrating that how habitat is arranged matters as much as how much habitat remains.")
    ],
    "reflection_exemplars": [
        ("Why is fragmentation worse than simple area loss?", "Our model reveals multiple compounding mechanisms. First, edge effects: fragmentation creates proportionally more edge habitat, which is degraded by changes in light, wind, temperature, and invasive species penetration. A 100-hectare fragment may have only 20 hectares of quality interior habitat. Second, isolation: fragmented populations cannot exchange genetic material, leading to inbreeding depression within a few generations. Third, minimum viable population: each isolated fragment may contain too few individuals to sustain a population long-term. Fourth, migration blocking: species cannot move through hostile landscape between fragments to track climate change. The model shows that 100 hectares in one connected block supports significantly more species than 100 hectares divided into ten 10-hectare fragments — same total area, dramatically different biodiversity outcome."),
        ("How do wildlife corridors reduce extinction even without stopping habitat loss?", "Corridors transform isolated habitat islands into a functional network. The model shows that connectivity increases effective population size by allowing gene flow between fragments, reducing inbreeding depression. Connected fragments function as a metapopulation — if a species goes locally extinct in one fragment, it can recolonize from connected fragments. Corridors enable climate migration by providing pathways for species to shift their ranges northward as temperatures rise. And corridors increase habitat quality in fragments by allowing wide-ranging species like large predators to maintain viable populations across multiple connected areas. The model demonstrates that connectivity is the most cost-effective conservation intervention because it multiplies the value of all existing protected areas.")
    ],
    "stem_intro": "Present the challenge: A region has 15 protected areas covering 12% of the landscape, but they\\'re isolated by development. Climate models project species need to migrate 50-100 km northward over 50 years, which is impossible through fragmented landscape. With limited budget, design a corridor network that connects the most critical areas, enables climate migration, and protects keystone species identified by your Species Interaction Network data.",
    "stem_concepts": [
        ("Corridor Ecology and Design", "Wildlife corridors must be wide enough to provide interior habitat (not just edge), contain appropriate vegetation and water sources, and include crossing structures over roads and highways. Research shows that corridors as narrow as 50-100 meters can support small mammal and bird movement, but large mammals need corridors 1-2 km wide. Corridor placement should follow natural landscape features like river valleys and mountain ridges that animals already use as travel routes."),
        ("Keystone Species Prioritization", "Not all species are equally important for ecosystem function. Keystone species — those whose impact is disproportionately large relative to their abundance — should be prioritized in corridor design. Pollinators, seed dispersers, apex predators, and ecosystem engineers like beaver have cascading positive effects when protected. Identifying and protecting keystone species gives the most biodiversity benefit per conservation dollar."),
        ("Conservation Finance and Easements", "Wildlife corridors often cross private land, requiring creative economic solutions. Conservation easements pay landowners to maintain wildlife-friendly land management without requiring government purchase. Payment for ecosystem services programs compensate landowners for maintaining forests, wetlands, and grasslands that provide public benefits like water filtration and carbon storage. These mechanisms align private economic interests with conservation goals.")
    ],
    "stem_eval": [
        ("Expert (4)", "Network design strategically connects priority areas based on model evidence, enables climate migration pathways, protects keystone species identified through interaction network analysis, includes realistic corridor specifications, and considers economic feasibility"),
        ("Proficient (3)", "Network connects multiple protected areas with reasonable corridor designs and some justification from model data, considers species movement needs"),
        ("Developing (2)", "Network connects some areas but lacks strategic prioritization or does not account for climate migration or keystone species, weak connection to model evidence"),
        ("Beginning (1)", "Network design is incomplete, not based on model data, or does not address the core challenges of fragmentation and climate migration")
    ],
    "support": [
        "Provide a simplified regional map with protected areas marked and a grid overlay — students can identify potential corridor routes by finding the shortest habitat connections between areas",
        "Use the analogy of highway networks: just as cities need road connections to function as a transportation system, nature reserves need wildlife corridors to function as a conservation system. Ask: Which connections would you build first if you had limited budget?",
        "Sentence frames: \\'I prioritized connecting ___ to ___ because the model shows ___. This corridor enables ___ species to ___, which reduces extinction cascade risk because ___.\\'"
    ],
    "extensions": [
        "Research the Half-Earth Project proposed by E.O. Wilson — the idea that protecting 50% of Earth\\'s land and ocean is necessary to prevent mass extinction. Evaluate the scientific basis, economic feasibility, and social justice implications of this proposal.",
        "Use GIS mapping software to identify potential wildlife corridor routes in your local area — analyze satellite imagery to find remaining habitat connections between natural areas and assess how development threatens these corridors",
        "Investigate de-extinction technology — the effort to revive extinct species like the woolly mammoth or passenger pigeon through genetic engineering. Evaluate whether de-extinction is a meaningful conservation tool or a distraction from protecting existing species."
    ],
    "cross_curr": [
        ("Math", "Calculate the relationship between habitat area and species number using the species-area curve (S = cA^z) where S is species number, A is area, c is a constant, and z typically equals 0.25. Predict how many species would be lost with 50% habitat reduction and compare to observed extinction rates."),
        ("ELA", "Read Rachel Carson\\'s Silent Spring (excerpts) alongside a modern article about insect decline. Write a comparative analysis of how the environmental threats have changed in 60 years and what Carson\\'s prescient warnings reveal about patterns of ecological crisis."),
        ("History", "Research the extinction of the passenger pigeon — once the most abundant bird in North America with flocks of billions — and analyze how a combination of habitat loss, hunting, and ecological disruption drove a species from billions to zero in less than a century. What lessons does this historical extinction hold for current biodiversity loss?")
    ],
    "misconceptions": [
        ("Extinction is natural, so the current rate is not a problem", "Extinction is indeed natural — the background rate is approximately 1-5 species per year over geological time. But the current rate is 100-1,000 times higher than this natural baseline, driven entirely by human activity. The last time species disappeared this fast was the asteroid impact 66 million years ago that killed 75% of all species. The difference between natural extinction and mass extinction is like the difference between a house settling over centuries and a house being demolished in a day — the outcomes are categorically different in scale and speed.", "Present the comparison visually: natural background rate = 1-5 species/year for millions of years. Current rate = 100-1,000 species/year. Draw both rates on the same graph. Ask: Does this look like a normal pattern to you?"),
        ("Protecting a few charismatic species (pandas, tigers) is sufficient conservation", "While flagship species generate public support and funding, focusing only on charismatic megafauna ignores the ecological reality that ecosystem function depends on thousands of less visible species. Insects pollinate 75% of food crops, fungi decompose organic matter and cycle nutrients, bacteria fix nitrogen that plants need, and countless invertebrates are the foundation of food webs. The loss of pollinators or soil organisms could be far more consequential for ecosystem function — and human food security — than the loss of any single large mammal. Conservation must protect entire functional ecosystems, not just photogenic species.", "Show the food web: ask students to remove the tiger from the web versus removing all pollinators. Which causes more cascading damage? The answer makes the case for ecosystem-level conservation rather than single-species approaches."),
        ("Technology and zoos can save species from extinction", "Captive breeding programs play a role in preventing imminent extinction for some species, but they cannot replace functional habitat. Most captive populations are too small for long-term genetic viability, behavioral adaptation to captivity reduces fitness in the wild, and reintroduction is impossible without suitable habitat. Furthermore, captive breeding is feasible for only a tiny fraction of threatened species — you cannot put a million species in zoos. The only way to prevent mass extinction at scale is to protect and reconnect habitat so that wild populations can sustain themselves. Technology is a supplement to habitat conservation, not a substitute for it.", "Present the numbers: approximately 7,000 species are in captive breeding programs worldwide. Approximately 1 million species are threatened with extinction. Ask: Can zoos save 0.7% of threatened species and call it a success? What does that tell us about where conservation resources should go?")
    ]
}

L06 = {
    "id": "G12L2-L06",
    "title": "Can Renewable Energy Replace Fossil Fuels?",
    "subtitle": "Modeling Energy Systems, Grid Infrastructure, and the Clean Energy Transition",
    "ngss": "HS-ESS3-2",
    "ngss_desc": "Evaluate competing design solutions for developing, managing, and utilizing energy and mineral resources based on cost-benefit ratios.",
    "big_question": "Renewable energy is now cheaper than fossil fuels in most of the world, yet fossil fuels still provide 80% of global energy — so what technical, economic, and political barriers prevent us from making a transition that is already economically rational?",
    "objectives": [
        "Model how energy demand, generation capacity, grid infrastructure, and energy storage interact to determine the feasibility of renewable energy transitions",
        "Explain why the intermittency of solar and wind power creates grid management challenges that require storage and demand flexibility",
        "Predict the conditions under which a regional energy grid can reliably operate on 80-100% renewable energy",
        "Analyze the trade-offs between different energy transition pathways including cost, reliability, environmental impact, and social equity"
    ],
    "vocabulary": [
        ("Grid Intermittency", "The variability of renewable energy generation caused by weather and time of day — solar panels produce no electricity at night and wind turbines stop when wind is calm, creating a fundamental challenge of matching variable supply to constant demand that must be solved through storage, demand flexibility, and grid interconnection"),
        ("Energy Storage Capacity", "The total amount of energy that can be stored and later dispatched when generation is low — including batteries, pumped hydro, compressed air, and hydrogen, storage is the key technology enabling high-penetration renewable grids because it bridges the gap between when energy is produced and when it is needed"),
        ("Capacity Factor", "The ratio of actual energy output to maximum possible output over a period — solar panels typically achieve 15-25% capacity factor (producing peak power only during sunny hours), while wind achieves 25-45%, compared to 90%+ for nuclear and natural gas baseload plants, meaning renewable grids need more installed capacity to generate the same total energy"),
        ("Grid Inertia", "The resistance of large power systems to frequency changes, provided by the spinning mass of conventional generators — renewable energy sources like solar and wind lack physical inertia, requiring new approaches like synthetic inertia from battery inverters to maintain grid stability as fossil fuel generators are retired")
    ],
    "components": [
        ("Total Energy Demand", "The amount of electricity and heat required by all residential, commercial, industrial, and transportation consumers — demand varies by time of day, season, and economic activity, with peak demand occurring when generation is most challenging for renewables", True),
        ("Renewable Generation Capacity", "The installed capacity of solar, wind, hydroelectric, and other renewable energy sources — has grown exponentially in recent years with solar costs dropping 90% since 2010, but installed capacity must exceed demand by a significant margin to account for intermittency", True),
        ("Fossil Fuel Generation", "The amount of electricity produced by coal, natural gas, and oil power plants — currently provides the baseload and dispatchable power that fills gaps in renewable generation, but produces the carbon emissions driving climate change", False),
        ("Energy Storage Capacity", "The total battery, pumped hydro, and other storage available to absorb excess renewable generation and dispatch it during low-generation periods — currently the bottleneck limiting renewable penetration on most grids", False),
        ("Grid Reliability Index", "The ability of the electrical grid to provide consistent, uninterrupted power to all consumers — measured by frequency stability, blackout risk, and power quality, grid reliability must remain extremely high (99.97%+) during the transition from fossil fuels to renewables", False),
        ("Carbon Emission Rate", "The total CO2 emissions from the energy sector — decreases as renewable generation replaces fossil fuel generation, but the rate of decrease depends on how quickly storage and grid infrastructure can support high renewable penetration", False),
        ("Energy Cost Per Kilowatt-Hour", "The average price consumers pay for electricity — influenced by generation costs, grid infrastructure investment, storage costs, and policy mechanisms like carbon pricing, with renewable energy now cheaper than fossil fuels in most regions for new generation", False)
    ],
    "think_about_it": "When Renewable Generation Capacity increases but Energy Storage Capacity remains limited, what happens to Grid Reliability during periods of low sun and wind? How does this bottleneck affect the pace at which Fossil Fuel Generation can be retired?",
    "scenarios": [
        ("Rapid Renewable Deployment", "Double Renewable Generation Capacity over 10 years while maintaining current Energy Storage Capacity — observe how Grid Reliability responds as intermittent generation exceeds the grid\\'s ability to manage variability"),
        ("Storage Breakthrough", "Maintain current renewable deployment rate but triple Energy Storage Capacity — observe how additional storage affects Grid Reliability and the ability to reduce Fossil Fuel Generation"),
        ("Integrated Transition", "Simultaneously increase Renewable Generation Capacity, triple Energy Storage, and modernize grid infrastructure — observe whether the combined approach achieves reliable high-renewable operation and significant carbon reduction")
    ],
    "sim_scenarios": [
        ("Renewables Without Storage", "Renewable Capacity: Doubled | Storage: Current | Grid: Current Infrastructure", "What happens when you add massive renewable capacity without proportional storage? Can the grid handle it, and what role do fossil fuels still play?"),
        ("Storage Breakthrough", "Renewable Capacity: Current Growth | Storage: Tripled | Grid: Current Infrastructure", "If battery costs dropped dramatically and storage tripled, how much fossil fuel generation could be displaced? Where does Grid Reliability improve most?"),
        ("Full System Transition", "Renewable Capacity: Doubled | Storage: Tripled | Grid: Modernized | Demand: Flexible", "What does it take to reliably run a grid on 80-100% renewable energy? What is the role of each component in maintaining reliability?")
    ],
    "discoveries": [
        "Adding renewable generation capacity without proportional storage creates grid instability — the model shows that above approximately 40% renewable penetration, intermittency causes frequency instability and curtailment (wasting excess generation) unless storage and demand flexibility increase",
        "Energy storage is the keystone technology of the renewable transition — the model shows that tripling storage capacity has a larger positive impact on Grid Reliability and Carbon Emission Rate than doubling renewable generation alone",
        "The cheapest kilowatt-hour is renewable, but the cheapest reliable grid requires the integration of generation, storage, transmission, and demand flexibility — no single component can achieve the transition alone",
        "The integrated transition scenario achieves 80% renewable operation with maintained grid reliability and 70% carbon reduction — demonstrating that the technical barriers to clean energy are solvable but require coordinated investment in all system components simultaneously"
    ],
    "answer": "Renewable energy can technically replace fossil fuels for electricity generation, and the economics increasingly favor this transition — solar and wind are now the cheapest sources of new electricity generation in most of the world. However, the transition faces real technical challenges centered on intermittency and grid management. The model reveals that the binding constraint is not generation cost but system integration: energy storage to bridge nighttime and calm periods, modernized grids to handle variable generation, and demand flexibility to match consumption to supply. Currently, storage is the bottleneck — without sufficient battery and pumped hydro capacity, grids cannot reliably exceed 40-50% renewable penetration. The integrated transition scenario shows that coordinated investment in generation, storage, and grid modernization can achieve 80-100% renewable operation while maintaining reliability. The barriers to this transition are less technical than political and economic: fossil fuel subsidies ($5.9 trillion per year globally), incumbent industry opposition, permitting delays, and the enormous capital required for grid infrastructure. The technology exists; the question is whether societies will deploy it fast enough to avoid the worst climate outcomes.",
    "stem_title": "Design a 100% Renewable Energy Grid",
    "stem_mission": "Design a regional energy system that achieves 100% renewable electricity generation while maintaining grid reliability above 99.97%, using your model evidence to determine the optimal mix of generation, storage, and demand management.",
    "stem_scenario": "A state with 5 million people currently generates 60% of its electricity from natural gas, 20% from coal, 15% from solar and wind, and 5% from hydroelectric. The governor has committed to 100% clean electricity by 2045. Your engineering team must design the generation, storage, and grid infrastructure plan that achieves this goal while maintaining reliable power delivery through all weather conditions and demand peaks. Your model data on intermittency, storage requirements, and grid stability should guide every design decision.",
    "stem_questions": [
        "Based on your model, what is the minimum Energy Storage Capacity needed to maintain grid reliability at 80%, 90%, and 100% renewable penetration?",
        "What does your model suggest about the optimal mix of solar versus wind generation for this state, given that their intermittency patterns are complementary (solar peaks during day, wind often peaks at night)?",
        "How does demand flexibility — shifting some consumption to match renewable generation peaks — reduce the storage requirement in your model?"
    ],
    "stem_design_qs": [
        "What specific mix of solar, wind, and other renewable generation does your plan include, and what model evidence supports this mix?",
        "How much energy storage does your plan require, and what storage technologies does it use for different timescales (hours, days, seasons)?",
        "What grid infrastructure upgrades does your plan require, including transmission lines, smart grid technology, and interconnection with neighboring regions?",
        "How does your plan ensure energy affordability and equitable access throughout the transition, especially for low-income households?"
    ],
    "career": "Renewable energy engineers who design solar farms, wind installations, and energy storage systems earn $70,000-$140,000/year. Grid systems engineers who manage the complex task of balancing variable renewable generation with reliable power delivery earn $80,000-$150,000/year at utilities and grid operators. Energy policy analysts who design regulatory frameworks, carbon pricing mechanisms, and clean energy incentives earn $65,000-$130,000/year in government agencies and think tanks.",
    "images": {
        "cover": ("G12L2-L06-cover.png", "A photorealistic image of diverse 17-18 year old students examining a model solar panel and wind turbine setup in a modern engineering classroom, with energy data dashboards and grid diagrams displayed on screens"),
        "landscape": ("G12L2-L06-landscape.png", "A photorealistic panoramic image of a modern energy landscape featuring solar panel arrays and wind turbines alongside battery storage facilities, with transmission lines connecting to a city skyline in the background"),
        "modeling": ("G12L2-L06-modeling.png", "A photorealistic image of diverse 17-18 year old students building energy grid models on their laptops, with real-time grid data and renewable generation curves displayed on a large smartboard"),
        "discussion": ("G12L2-L06-discussion.png", "A photorealistic image of a teacher leading a discussion with diverse 17-18 year old students about renewable energy grid challenges, with charts showing intermittency patterns and storage requirements on screen"),
        "stem": ("G12L2-L06-stem.png", "A photorealistic image of diverse 17-18 year old students designing renewable energy grid systems on whiteboards and poster boards, with generation mix charts, storage calculations, and grid infrastructure maps")
    },
    "pre_assessment": [
        "Where does the electricity in your home come from? Can you trace it from the power plant to your outlet?",
        "What happens when the sun goes down or the wind stops blowing if a region depends on solar and wind power? How could this problem be solved?",
        "If renewable energy is now cheaper than fossil fuels, why do fossil fuels still provide 80% of global energy? What barriers prevent the switch?",
        "What do you think a 100% renewable energy grid would require beyond just solar panels and wind turbines?"
    ],
    "extend_components": [
        ("Nuclear Baseload Generation", "Electricity from nuclear fission that provides constant, carbon-free baseload power with 90%+ capacity factor — nuclear complements intermittent renewables by providing reliable generation but faces challenges of high construction costs, long build times, waste storage, and public opposition"),
        ("Electric Vehicle Grid Integration", "The use of electric vehicle batteries as distributed energy storage for the grid — millions of EVs plugged in during peak solar hours could absorb excess generation, and vehicle-to-grid technology could discharge stored energy during peak demand, turning the transportation fleet into a massive battery"),
        ("Hydrogen Energy Storage", "The production of hydrogen through electrolysis using excess renewable electricity — hydrogen can be stored for weeks to months and converted back to electricity or used directly as fuel, addressing the seasonal storage challenge that batteries cannot solve cost-effectively")
    ],
    "reflections": [
        "Why is adding more renewable capacity insufficient without proportional investment in storage and grid infrastructure? What does your model reveal about the intermittency challenge?",
        "Your model showed that storage is the keystone technology. What types of storage are needed for different timescales — hourly, daily, and seasonal — and what technologies address each?",
        "How does the concept of capacity factor explain why a 100% renewable grid needs much more installed generation capacity than a fossil fuel grid serving the same demand?",
        "What role should nuclear energy play in the clean energy transition? Evaluate the trade-offs using evidence from your model about baseload reliability and carbon reduction.",
        "The technology for 100% renewable energy exists today. What non-technical barriers — political, economic, social — are preventing faster deployment, and how would you address them?"
    ],
    "dimensions": [
        ("Science Practice", "Engaging in Argument from Evidence", "Students evaluate competing energy transition pathways using model evidence about cost, reliability, carbon reduction, and storage requirements to construct arguments for optimal energy system designs."),
        ("Disciplinary Core Idea", "ESS3.A Natural Resources", "All forms of energy production have associated costs, risks, and benefits. The transition from fossil fuels to renewable energy requires evaluating these trade-offs across multiple dimensions including environmental impact, reliability, cost, and equity."),
        ("Crosscutting Concept", "Energy and Matter", "Students track how energy flows through the electrical grid system — from generation through transmission, storage, and consumption — and analyze how the constraints on energy conversion and storage determine the feasibility of renewable energy transitions.")
    ],
    "cast_items": [
        "Model how renewable generation, energy storage, and grid infrastructure interact to determine the reliability and carbon intensity of electrical systems",
        "Predict grid reliability outcomes under different renewable energy penetration levels with varying storage capacity",
        "Evaluate competing energy transition designs based on cost-benefit analysis of generation mix, storage investment, and carbon reduction outcomes"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A grid operator increases solar generation capacity from 20% to 50% of total capacity without adding energy storage. What is the most likely immediate outcome? A) Carbon emissions drop by 30% B) Electricity costs decrease C) Grid reliability decreases during evening hours when solar drops to zero and storage cannot fill the gap D) Fossil fuel plants shut down automatically"),
        ("Constructed Response:", "Using your energy system model, explain why achieving the last 20% of a 100% renewable grid (going from 80% to 100%) is significantly more difficult and expensive than the first 20% (going from 0% to 20%). Reference at least three components including storage, grid reliability, and capacity factor in your answer.")
    ],
    "background_intro": "The global energy system is at an inflection point. Renewable energy — particularly solar and wind — has become the cheapest source of new electricity generation in most of the world, with solar costs falling 90% since 2010 and wind costs falling 70%. Yet fossil fuels still provide approximately 80% of global primary energy. The gap between economic opportunity and actual deployment reveals that the energy transition is not primarily a technology or cost problem — it is a systems integration, infrastructure, and political economy challenge.",
    "background_sections": [
        ("The Renewable Cost Revolution", "The cost decline of renewable energy has been one of the most dramatic technological transitions in history. Solar photovoltaic costs have fallen from $76 per watt in 1977 to less than $0.20 per watt today — a 99.7% decline. Unsubsidized solar and wind are now cheaper than new coal or gas power plants in regions representing 90% of global electricity generation. Battery storage costs have fallen 97% since 1991 and continue declining at 15-20% per year. These cost curves show no signs of flattening, suggesting that the economic case for renewable energy will only strengthen. However, the cost of generating a kilowatt-hour is different from the cost of delivering reliable power 24/7/365 — the system costs of integration, storage, and transmission add significantly to the generation-only price comparison."),
        ("The Intermittency Challenge", "Solar panels generate electricity only during daylight hours and at reduced capacity under clouds. Wind turbines generate only when wind speeds fall within their operating range (typically 3-25 meters per second). This intermittency creates a fundamental mismatch between when renewable energy is produced and when consumers need it. In California, the famous duck curve shows excess solar generation during midday that must be curtailed (wasted) because storage is insufficient, followed by a steep evening ramp when solar disappears and demand peaks. Managing this variability requires a portfolio approach: geographic diversity (wind blows somewhere even when calm locally), temporal diversity (solar and wind complement each other), energy storage (batteries for hours, pumped hydro for days), demand flexibility (shifting industrial loads to match generation), and grid interconnection (importing power from regions with surplus generation)."),
        ("Grid Infrastructure: The Hidden Bottleneck", "The electrical grid is the largest machine ever built — a complex system of generation, transmission, distribution, and control that must balance supply and demand every second of every day. The existing grid was designed for centralized fossil fuel plants, not distributed renewable generation. Transitioning to high-renewable operation requires massive infrastructure upgrades: new high-voltage transmission lines to connect remote solar and wind resources to demand centers (the best solar is in deserts, the best wind is offshore or in rural areas), smart grid technology to manage variable generation, bidirectional power flow to accommodate rooftop solar feeding back into the grid, and new frequency regulation techniques to replace the physical inertia lost when spinning fossil fuel generators are retired. These grid upgrades represent a multi-trillion-dollar investment that is technically feasible but requires sustained political will and capital allocation."),
        ("Energy Justice and Equitable Transition", "The clean energy transition must address equity or it will fail. Low-income communities and communities of color currently bear disproportionate health burdens from fossil fuel pollution — coal plants, refineries, and gas infrastructure are concentrated in disadvantaged neighborhoods. The transition must ensure that these communities benefit first from clean energy, not last. Energy affordability is also critical: if the transition raises electricity costs, low-income households who spend a larger percentage of income on energy will be harmed. A just transition also requires supporting workers and communities dependent on fossil fuel industries through retraining, economic diversification, and direct investment. History shows that ignoring equity in major economic transitions creates political backlash that can derail progress for everyone.")
    ],
    "lever_L": "Students identify Total Energy Demand, Renewable Generation Capacity, Fossil Fuel Generation, Energy Storage Capacity, Grid Reliability Index, Carbon Emission Rate, and Energy Cost Per Kilowatt-Hour as key components of the energy system.",
    "lever_E": "Students determine that renewable capacity alone is insufficient without storage, that intermittency creates a reliability ceiling that storage and grid modernization must address, and that the integrated approach outperforms any single-component strategy.",
    "lever_V": "Students build a computational model of a regional energy grid showing how generation, storage, and demand interact to determine reliability and carbon emissions under different renewable penetration levels.",
    "lever_Ev": "Students run rapid deployment, storage breakthrough, and integrated transition scenarios to test predictions about the technical requirements for high-renewable grid operation.",
    "lever_R": "Students add nuclear baseload, EV grid integration, or hydrogen storage to explore how additional technologies affect the feasibility and cost of 100% clean energy systems.",
    "slides_guide": [
        {
            "num": "Slide 1",
            "title": "Cover",
            "visual": "Title slide with image of modern renewable energy installation — solar panels and wind turbines with battery storage visible",
            "say": "Renewable energy is now the cheapest electricity in human history. So why does fossil fuel still power 80% of the world? Today we model the system to find out.",
            "do": "Show cover image. Quick poll: How quickly do you think the world could switch to 100% renewable energy? 5 years? 20 years? Never? Take predictions and reasoning.",
            "time": "2 min"
        },
        {
            "num": "Slide 2",
            "title": "Learning Objectives",
            "visual": "Four learning objectives with energy system vocabulary terms and generation cost comparison chart",
            "say": "We\\'re not just learning about solar panels today — we\\'re modeling the entire energy system to understand why the cheapest technology doesn\\'t always win, and what it takes to make it work.",
            "do": "Have students read objectives. Pre-teach vocabulary. Key concept: intermittency — the sun goes down, the wind stops. How do you keep the lights on? This is the central challenge.",
            "time": "3 min"
        },
        {
            "num": "Slide 3",
            "title": "Big Question",
            "visual": "Provocative question over chart showing renewable cost decline alongside persistent fossil fuel dominance",
            "say": "If renewables are cheaper, why aren\\'t they everywhere? The answer is more interesting than you think — it\\'s not about the energy, it\\'s about the system.",
            "do": "Quick-write: Students write their hypothesis about what barriers prevent faster renewable adoption. Save for comparison after modeling.",
            "time": "3 min"
        },
        {
            "num": "Slide 4",
            "title": "LEVER Framework",
            "visual": "LEVER steps with energy system examples for each step",
            "say": "We\\'ll build a model of a regional energy grid. This model will reveal why adding solar panels isn\\'t enough — and what else the system needs to work reliably.",
            "do": "Preview LEVER steps. Emphasize: the model will challenge the idea that the energy transition is simple. It\\'s an engineering systems challenge of enormous complexity.",
            "time": "2 min"
        },
        {
            "num": "Slide 5",
            "title": "Activity 1: Components",
            "visual": "Seven component cards for sorting with energy system illustrations",
            "say": "Which are external inputs to the energy system, and which are internal system responses? Think about what society demands from the grid versus what the grid produces internally.",
            "do": "Guide sorting: External = Total Energy Demand (consumer behavior), Renewable Generation Capacity (installed infrastructure). Internal = the five system response variables. Discuss why Fossil Fuel Generation is internal — it responds to fill gaps when renewables fall short.",
            "time": "8 min"
        },
        {
            "num": "Slide 6",
            "title": "Activity 2: Connections",
            "visual": "Relationship diagram with all seven energy system components",
            "say": "When Renewable Generation is high during the day but demand peaks in the evening, what happens to Grid Reliability without storage? Trace the pathway from generation to reliability to the role fossil fuels still play.",
            "do": "Students draw arrows. Key discovery: the central role of Energy Storage as the bridge between intermittent generation and constant demand. Without storage, renewable penetration hits a ceiling. Ask: What is that ceiling and why?",
            "time": "8 min"
        },
        {
            "num": "Slide 7",
            "title": "Activity 3: Simulation",
            "visual": "Simulation showing three scenarios with graphs of renewable penetration, grid reliability, and carbon emissions over time",
            "say": "Run all three scenarios. Pay particular attention to what happens to Grid Reliability in the renewables-without-storage scenario. Then see how the integrated approach changes everything.",
            "do": "Students run scenarios and record observations. Key discussion: Why does adding more solar panels actually decrease grid reliability past a certain point without storage? How does the integrated approach solve this?",
            "time": "10 min"
        },
        {
            "num": "Slide 8",
            "title": "Discoveries",
            "visual": "Four key discoveries with supporting graphs showing the relationship between storage, reliability, and renewable penetration",
            "say": "The cheapest electron is renewable. But the cheapest reliable grid requires the whole system working together — generation, storage, transmission, and flexibility. Let\\'s discuss what this means for energy policy.",
            "do": "Class discussion. Key question: If the technology exists and the economics work, what is actually preventing the transition? Guide toward political economy, infrastructure investment, and fossil fuel industry resistance.",
            "time": "5 min"
        },
        {
            "num": "Slide 9",
            "title": "STEM Challenge",
            "visual": "Engineering challenge: Design a 100% renewable grid for a state of 5 million people",
            "say": "Your state has committed to 100% clean electricity by 2045. Design the system — not just the generation, but the storage, grid upgrades, and demand flexibility that make it reliable. Use your model data.",
            "do": "Groups design complete energy system plans with generation mix, storage capacity, grid infrastructure, and equity provisions. Present designs with evidence from model simulations.",
            "time": "12 min"
        }
    ],
    "sort_reasoning": "Total Energy Demand and Renewable Generation Capacity are external components because they represent the demand placed on the system by consumers and the generation infrastructure that has been built — both are determined by factors outside the grid\\'s internal operations. Fossil Fuel Generation, Energy Storage Capacity, Grid Reliability Index, Carbon Emission Rate, and Energy Cost Per Kilowatt-Hour are internal because they are operational outcomes of how the grid manages the balance between available generation and demand — they change in response to the external inputs and each other.",
    "relationships": [
        ("Renewable Generation Capacity to Carbon Emission Rate", "NEGATIVE (-)", "More renewable generation displaces fossil fuel generation, directly reducing carbon emissions. Each kilowatt-hour of solar or wind that replaces coal or gas eliminates the associated CO2 emissions."),
        ("Renewable Generation Capacity to Grid Reliability Index", "POSITIVE (+) then NEGATIVE (-)", "Initially, adding renewables improves reliability by diversifying the generation mix. Beyond approximately 40% penetration, intermittency begins degrading reliability unless storage and grid flexibility increase proportionally."),
        ("Energy Storage Capacity to Grid Reliability Index", "POSITIVE (+)", "Storage bridges the gap between intermittent renewable generation and constant demand, absorbing excess generation during peak production and dispatching it during low generation, directly improving reliability."),
        ("Fossil Fuel Generation to Carbon Emission Rate", "POSITIVE (+)", "Fossil fuel combustion is the primary source of energy-sector carbon emissions. Each megawatt-hour of coal generation produces approximately 1 ton of CO2; natural gas produces approximately 0.5 tons."),
        ("Grid Reliability Index to Energy Cost Per Kilowatt-Hour", "NEGATIVE (-)", "Maintaining high grid reliability during the transition requires investment in storage, grid infrastructure, and backup capacity that increases system costs. The most reliable configurations cost more than least-cost generation-only calculations suggest.")
    ],
    "sim_answers": [
        ("Renewables Without Storage", "Doubling renewable capacity without storage produces counterintuitive results: during sunny, windy periods, the grid has excess generation that must be curtailed (wasted), while during evening peaks and calm periods, fossil fuels must still ramp up to meet demand. Grid Reliability actually decreases because the variability exceeds the grid\\'s ability to manage it. Carbon emissions decrease modestly but far less than the doubled capacity would suggest because fossil fuels must still provide evening and nighttime power. The model demonstrates that generation capacity alone is insufficient — the system needs storage to capture and shift excess renewable energy."),
        ("Storage Breakthrough", "Tripling storage capacity produces dramatic improvements even without additional generation. Excess renewable energy that would have been curtailed is stored and dispatched during low-generation periods, reducing dependence on fossil fuel backup. Grid Reliability improves because storage provides the buffering the grid needs to handle intermittency. Carbon Emission Rate drops significantly as stored renewable energy displaces fossil fuel generation during evening and nighttime hours. The model shows storage has higher marginal value than additional generation capacity at current renewable penetration levels."),
        ("Full System Transition", "The integrated approach achieves approximately 80% renewable operation with maintained Grid Reliability. Combining doubled renewables with tripled storage and modernized grid infrastructure creates a system where renewable generation meets demand directly during peak production hours, stored energy serves evening and overnight demand, and a small amount of dispatchable clean power (hydroelectric or potentially nuclear) provides reliability backstop during extended low-wind, low-sun periods. Carbon emissions drop by 70-80%. Energy costs are competitive with the current fossil-fuel-dominated system when health and environmental externalities are included.")
    ],
    "reflection_exemplars": [
        ("Why is 100% harder than 80%?", "Our model reveals a fundamental non-linearity in the clean energy transition. The first 40-50% of renewable penetration is relatively straightforward — intermittency can be managed through geographic diversity and existing grid flexibility. Going from 50% to 80% requires significant storage investment but is technically and economically feasible. But the last 20% — from 80% to 100% — requires solving the hardest problem: extended periods of low sun and low wind that can last days or even weeks (known as the dunkelflaute). Battery storage is cost-effective for hours but not for days. Seasonal storage (hydrogen or equivalent) is needed but remains expensive. The model shows that achieving the last 20% costs almost as much as achieving the first 80%, which is why most credible energy plans target 80-90% renewable with the remainder from other clean sources like nuclear or geothermal."),
        ("Why haven\\'t we transitioned faster if the economics work?", "The model shows that the pure generation cost of renewables is lower than fossil fuels, but the system transition cost is enormous because it requires simultaneously building new generation, storage, and transmission infrastructure while maintaining the reliability of the existing system. Beyond economics, the transition faces political barriers: fossil fuel companies with trillions in assets actively oppose policies that strand those assets, subsidies totaling $5.9 trillion per year distort the market in favor of fossil fuels, permitting processes for transmission lines and renewable installations can take 5-10 years, and incumbent utilities resist business model changes that threaten their revenue. The technology is ready; the political economy is the binding constraint.")
    ],
    "stem_intro": "Present the challenge: A state of 5 million people needs to reach 100% clean electricity by 2045. Currently 60% gas, 20% coal, 15% solar/wind, 5% hydro. Your team designs the complete system — generation mix, storage capacity, grid upgrades, and equity provisions — with every choice justified by model evidence about intermittency, reliability, and cost.",
    "stem_concepts": [
        ("Generation Mix Optimization", "The optimal blend of solar, wind, hydroelectric, and potentially nuclear generation depends on regional resources, demand patterns, and complementarity. Solar and wind are complementary — solar peaks during day, wind often peaks at night and in winter. Geographic diversity reduces overall intermittency: if it is cloudy in one location, it may be sunny 200 miles away. The optimal mix minimizes the storage requirement by maximizing the overlap between generation and demand."),
        ("Multi-Duration Storage", "Different storage technologies address different timescales. Lithium-ion batteries (4-8 hours) handle daily cycling — storing midday solar for evening demand. Pumped hydroelectric (8-24 hours) handles longer daily and multi-day gaps. Long-duration storage technologies like iron-air batteries, compressed air, or green hydrogen (days to weeks) address extended low-generation periods. A cost-effective storage strategy deploys each technology for its optimal duration."),
        ("Demand-Side Flexibility", "Shifting some electricity consumption to match renewable generation peaks reduces the storage requirement. Smart charging of electric vehicles during solar peak hours, industrial load shifting, and thermal storage (heating or cooling buildings when energy is cheap for use when it is expensive) can flatten demand curves. Studies suggest demand flexibility can reduce storage needs by 20-30%, significantly lowering system costs.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan specifies generation mix, storage portfolio, grid infrastructure, and demand flexibility with all choices justified by model evidence about intermittency, reliability, and cost. Addresses equity and energy justice. Provides realistic timeline with milestones."),
        ("Proficient (3)", "Plan addresses major system components with reasonable specifications and some connection to model data, includes consideration of storage and reliability challenges"),
        ("Developing (2)", "Plan focuses mainly on generation without adequate attention to storage, grid infrastructure, or reliability challenges, weak connection to model evidence"),
        ("Beginning (1)", "Plan addresses only generation capacity without considering the system requirements for reliable operation, lacks model evidence")
    ],
    "support": [
        "Provide a simplified grid diagram showing generation sources, storage, transmission, and demand — students can trace the flow of electricity and identify where storage and flexibility are needed to bridge intermittency gaps",
        "Use the phone battery analogy: your phone generates no energy (like solar at night) but the battery lets you use it all day. The grid needs the same concept at massive scale. How big would the battery need to be?",
        "Sentence frames: \\'At ___% renewable penetration, Grid Reliability ___ because ___. To maintain reliability above 99.97%, the system needs ___ hours of storage capacity because ___.\\'"
    ],
    "extensions": [
        "Research the energy system of Iceland (nearly 100% renewable) or Costa Rica (98% renewable) — analyze what geographic and geological factors make these countries uniquely suited for high renewable penetration and evaluate what lessons apply to other regions",
        "Calculate the total battery storage capacity needed for your state to go from 50% to 100% renewable — convert this to number of Tesla Megapacks, land area required, and cost, then compare to the state\\'s annual energy budget",
        "Investigate the role of nuclear fusion as a potential future energy source — evaluate the current state of fusion research, realistic timelines for commercial deployment, and whether waiting for fusion is a viable climate strategy compared to deploying existing renewable technology now"
    ],
    "cross_curr": [
        ("Math", "Model the duck curve mathematically: graph solar generation and electricity demand over a 24-hour period, calculate the gap between them, and determine the storage capacity (in megawatt-hours) needed to bridge the evening peak when solar drops to zero and demand is highest."),
        ("ELA", "Analyze the rhetoric of competing stakeholders in energy policy debates — a fossil fuel industry representative, a renewable energy advocate, an environmental justice organizer, and a grid reliability engineer. Write a synthesis essay that evaluates each perspective\\'s evidence quality and identifies common ground."),
        ("History", "Research the history of energy transitions — from wood to coal, coal to oil, and oil to natural gas. Analyze how long each transition took, what drove the change, and what parallels exist with the current fossil-to-renewable transition. Why have past transitions taken 50-100 years, and can this one be faster?")
    ],
    "misconceptions": [
        ("Renewable energy is unreliable because the sun doesn\\'t always shine and the wind doesn\\'t always blow", "While individual solar panels and wind turbines are intermittent, a well-designed renewable energy system achieves high reliability through diversification, storage, and grid management. Geographic diversity means wind is almost always blowing somewhere across a large region. Solar and wind are complementary (solar peaks midday, wind often peaks at night). Energy storage bridges generation gaps. Modern weather forecasting allows grid operators to predict renewable output days in advance. Grids in regions like Denmark (80%+ wind) and South Australia (70%+ renewable) demonstrate that high-renewable operation is compatible with reliability.", "Show the grid data from South Australia or Denmark: despite high renewable penetration, grid reliability remains high. Ask: How is this possible if renewables are unreliable? Guide students to understand that system design, not individual source variability, determines reliability."),
        ("We need fossil fuels for baseload power that renewables cannot provide", "The concept of baseload power — large plants running constantly — is an artifact of the old grid design, not a physical necessity. Modern grids can provide constant, reliable power from a combination of variable renewables, storage, demand flexibility, and a small amount of dispatchable clean generation. The concept of baseload is being replaced by flexibility — the ability to match generation to demand in real time using diverse sources and storage. The model shows that storage and grid management can replace the role fossil fuel baseload plants currently play.", "Challenge the concept: Ask students why a grid needs a single large plant running 24/7 when the same energy can come from a portfolio of sources managed by software. Is baseload a physical requirement or just the way we built the old system?"),
        ("The energy transition will make electricity unaffordable", "Renewable generation is already the cheapest electricity source in most of the world. While the transition requires significant investment in storage and grid infrastructure, the long-term cost trajectory favors renewables because they have zero fuel costs — once built, the marginal cost of solar and wind electricity is essentially free. Fossil fuel costs are volatile and include massive hidden costs: air pollution causes $2.8 trillion in health damage annually, and climate change costs are projected at $38 trillion per year by 2050. When these externalities are included, the renewable transition saves money overall. The key is ensuring that transition costs are shared equitably rather than falling on those least able to pay.", "Present the full cost comparison: generation cost, fuel cost, health cost, and climate cost for fossil fuels versus renewables. Show that renewables are cheaper even today when externalities are included. Ask: Who currently pays the health and climate costs of fossil fuels?")
    ]
}

L07 = {
    "id": "G12L2-L07",
    "title": "Is Our Freshwater Running Out?",
    "subtitle": "Modeling the Water Cycle, Aquifer Depletion, and Global Water Security",
    "ngss": "HS-ESS2-5",
    "ngss_desc": "Plan and conduct an investigation of the properties of water and its effects on Earth materials and surface processes.",
    "big_question": "Water covers 71% of Earth\\'s surface, but only 0.5% is accessible freshwater — so why are aquifers that took thousands of years to fill being drained in decades, and what happens to 2 billion people when the water runs out?",
    "objectives": [
        "Model how precipitation, surface water, groundwater recharge, and human extraction interact to determine freshwater availability in a regional water system",
        "Explain why groundwater depletion is effectively irreversible on human timescales and why aquifers are being used faster than they recharge",
        "Predict the conditions under which regional water systems reach crisis points based on the balance between recharge and extraction",
        "Analyze water management strategies and evaluate their potential to maintain sustainable water supply for growing populations"
    ],
    "vocabulary": [
        ("Aquifer", "An underground layer of rock or sediment that holds and transmits groundwater — aquifers can be confined (trapped between impermeable layers, under pressure) or unconfined (with a water table that rises and falls with recharge), and many major aquifers took thousands to millions of years to fill through slow geological recharge"),
        ("Groundwater Recharge Rate", "The rate at which water percolates from the surface into an aquifer to replenish its supply — determined by precipitation, soil permeability, surface cover, and geology, recharge is typically very slow (millimeters to centimeters per year) compared to the rate at which modern pumping extracts water"),
        ("Water Stress", "A condition in which water demand exceeds or approaches available supply — regions with a withdrawal-to-availability ratio above 40% are considered water-stressed, and approximately 2 billion people currently live in areas experiencing water stress, a number projected to increase significantly with climate change and population growth"),
        ("Desalination", "The process of removing salt and minerals from seawater to produce freshwater — desalination can provide a virtually unlimited water source but requires significant energy input (3-10 kWh per cubic meter), produces concentrated brine waste, and remains 3-5 times more expensive than conventional freshwater sources in most locations")
    ],
    "components": [
        ("Precipitation Rate", "The amount of rain and snowfall that enters the regional water system — varies with climate patterns, season, and geography, and is projected to become more variable and extreme with climate change, with wetter areas getting wetter and drier areas getting drier", True),
        ("Population and Agricultural Demand", "The total freshwater required by domestic, agricultural, and industrial users — agriculture alone accounts for 70% of global freshwater withdrawals, and demand is increasing with population growth, urbanization, and economic development", True),
        ("Surface Water Availability", "The volume of water in rivers, lakes, and reservoirs available for human use — highly variable with precipitation and seasonal patterns, and increasingly stressed by drought, increased demand, and upstream diversions", False),
        ("Groundwater Level", "The depth to the water table in the regional aquifer — declining in many major agricultural regions as extraction exceeds recharge, with some aquifers losing meters of water level per year while natural recharge operates on timescales of decades to millennia", False),
        ("Water Recycling and Efficiency", "The degree to which water is reused, recycled, or used more efficiently — including drip irrigation, water recycling for industry, graywater reuse for landscaping, and smart metering that reduces waste, these measures can reduce demand by 30-50% without reducing services", False),
        ("Ecosystem Water Requirements", "The minimum water flow needed to maintain healthy rivers, wetlands, and aquatic ecosystems — these environmental flows support fisheries, water purification, flood control, and biodiversity, but are often sacrificed when human demand exceeds supply", False),
        ("Water Quality Index", "The purity and safety of available water — contamination from agriculture (nitrates, pesticides), industry (heavy metals, chemicals), and inadequate sanitation (pathogens) can make water unusable even when physically available, effectively reducing the accessible supply", False)
    ],
    "think_about_it": "When Population and Agricultural Demand increases but Precipitation Rate stays constant or decreases with climate change, what happens to Groundwater Level over time? If Ecosystem Water Requirements are ignored to meet human demand, how does declining Water Quality eventually affect human water availability?",
    "scenarios": [
        ("Increasing Extraction", "Increase Population and Agricultural Demand by 30% with current Precipitation — observe how Groundwater Level and Surface Water respond, and when the system reaches crisis thresholds"),
        ("Climate-Driven Drought", "Reduce Precipitation Rate by 20% while maintaining current demand — observe how even moderate precipitation decline affects a water system that is already near capacity"),
        ("Efficiency and Reuse Strategy", "Maintain demand growth but increase Water Recycling and Efficiency by 40% — observe whether conservation measures can offset growing demand and protect groundwater levels")
    ],
    "sim_scenarios": [
        ("Growing Demand", "Population Demand: +30% | Precipitation: Current | Efficiency: Current", "If water demand grows 30% while supply stays constant, what do you predict happens to Groundwater Level? How long until the aquifer reaches critical depletion?"),
        ("Drought Scenario", "Population Demand: Current | Precipitation: -20% | Efficiency: Current", "A 20% reduction in precipitation simulates a sustained drought. Which component of the water system is stressed first? What cascading effects follow?"),
        ("Conservation Strategy", "Population Demand: +30% | Precipitation: Current | Efficiency: +40% | Recycling: Active", "Can efficiency improvements offset 30% demand growth? What does the model show about the water balance, and where does conservation have the most impact?")
    ],
    "discoveries": [
        "Groundwater depletion is effectively irreversible on human timescales — the model shows that aquifers being drained in decades took thousands of years to fill through natural recharge, meaning once depleted, they cannot be replenished within any relevant planning horizon",
        "Agriculture is the dominant driver of water stress, consuming 70% of freshwater — the model shows that even modest improvements in irrigation efficiency (switching from flood to drip irrigation) have larger impacts on the water balance than all other demand reduction measures combined",
        "Climate change acts as a threat multiplier by simultaneously reducing precipitation in already dry regions and increasing evapotranspiration through higher temperatures — the combination compresses the timeline for water crisis compared to either factor alone",
        "Water recycling and efficiency improvements can offset 30-40% of growing demand, but in regions where demand already exceeds sustainable supply, efficiency alone is insufficient — structural changes to water allocation and agricultural practices are required"
    ],
    "answer": "Earth\\'s freshwater is not technically running out — the water cycle continues, and the total volume of water on Earth is constant. But accessible freshwater — the 0.5% in rivers, lakes, and usable aquifers — is being consumed faster than it is replenished in many of the world\\'s most populated and agricultural regions. The critical issue is groundwater: aquifers like the Ogallala (US Great Plains), the Indo-Gangetic (India, Pakistan, Bangladesh), and the North China Plain are being pumped at rates 10-50 times faster than natural recharge. These aquifers took thousands of years to fill and will take thousands of years to refill once depleted — making their loss effectively permanent on human timescales. The model shows that agriculture, which consumes 70% of freshwater, is the dominant driver and the greatest opportunity for conservation. Climate change accelerates the crisis by reducing precipitation in dry regions and increasing evaporation. Solutions exist — drip irrigation, water recycling, desalination, and demand management — but they require fundamental changes to water pricing, agricultural policy, and international water governance that have proven politically difficult. Without these changes, an estimated 2 billion people face severe water stress, and agricultural regions that feed billions could lose irrigation capacity within decades.",
    "stem_title": "Design a Sustainable Water Management System",
    "stem_mission": "Design a comprehensive water management system for a water-stressed region that balances human needs, agricultural demand, and ecosystem requirements while maintaining groundwater sustainability.",
    "stem_scenario": "A semi-arid agricultural region of 3 million people relies on a groundwater aquifer for 60% of its water supply. The aquifer level has been declining 1.5 meters per year for the past 20 years due to agricultural irrigation that far exceeds natural recharge. Climate projections indicate 15% less precipitation over the next 30 years. At current rates, the aquifer will be too depleted for economical pumping within 25 years, threatening the food production that feeds 15 million people beyond the region. Your team must design a water management system that stabilizes the aquifer while maintaining agricultural productivity and supporting population growth.",
    "stem_questions": [
        "Based on your model, how many years until the aquifer reaches critical depletion at current extraction rates, and how does a 15% precipitation decline change this timeline?",
        "What does your model show about the relative impact of irrigation efficiency improvements versus reducing irrigated acreage for stabilizing the groundwater level?",
        "How can water recycling and alternative sources like desalination supplement groundwater without creating new environmental problems?"
    ],
    "stem_design_qs": [
        "What specific water conservation and efficiency measures does your plan implement, and what percentage of demand reduction do they achieve based on model evidence?",
        "How does your plan address agricultural water use — the dominant demand — without devastating the regional economy?",
        "What alternative water sources does your plan develop, and what are their capacities, costs, and environmental impacts?",
        "How does your plan allocate water between human consumption, agriculture, and ecosystem requirements, and what governance mechanisms enforce this allocation?"
    ],
    "career": "Hydrologists who study the movement, distribution, and quality of water work for the USGS, state water agencies, and environmental consulting firms, earning $60,000-$120,000/year. Water resource engineers who design systems for water treatment, distribution, recycling, and desalination earn $70,000-$140,000/year. Water policy analysts who develop regulations, pricing mechanisms, and international water agreements earn $60,000-$125,000/year at government agencies and international organizations.",
    "images": {
        "cover": ("G12L2-L07-cover.png", "A photorealistic image of diverse 17-18 year old students testing water samples in a modern environmental science laboratory, with hydrological maps and aquifer data displays visible on screens behind them"),
        "landscape": ("G12L2-L07-landscape.png", "A photorealistic aerial image showing a drought-stressed landscape with a shrinking reservoir, dried lakebed visible as white salt flats, contrasted with green irrigated agricultural fields fed by declining groundwater"),
        "modeling": ("G12L2-L07-modeling.png", "A photorealistic image of diverse 17-18 year old students building water system models on laptops, with aquifer cross-section diagrams and water balance charts projected on a smartboard"),
        "discussion": ("G12L2-L07-discussion.png", "A photorealistic image of a teacher leading a discussion with diverse 17-18 year old students about water scarcity, with maps showing global water stress regions and declining aquifer levels displayed on screen"),
        "stem": ("G12L2-L07-stem.png", "A photorealistic image of diverse 17-18 year old students designing water management systems on poster boards with aquifer diagrams, water budgets, conservation strategies, and infrastructure plans")
    },
    "pre_assessment": [
        "Where does your tap water come from? Can you trace it from its source to your glass?",
        "What is an aquifer and why does it matter? What happens if an aquifer is pumped dry?",
        "Earth is called the water planet, but most people worry about water scarcity. How can a planet covered in water have a freshwater crisis?",
        "What uses the most freshwater globally — homes, factories, or farms? How much of total freshwater do you think this use consumes?"
    ],
    "extend_components": [
        ("Virtual Water Trade", "The hidden water embedded in traded goods — producing 1 kg of beef requires 15,000 liters of water, and water-scarce countries that import food are effectively importing the water that grew it, making global trade a major mechanism for redistributing water stress across regions"),
        ("Desalination Infrastructure", "The capacity to convert seawater to freshwater using reverse osmosis or thermal distillation — desalination provides a climate-independent water source but requires 3-10 kWh per cubic meter, produces concentrated brine that harms marine ecosystems, and is expensive to build and operate"),
        ("Managed Aquifer Recharge", "The intentional channeling of surface water into underground aquifers to accelerate natural recharge — through injection wells, spreading basins, and stormwater capture, managed recharge can partially offset extraction, but is limited by the availability of excess surface water and suitable geological conditions")
    ],
    "reflections": [
        "Why is groundwater depletion effectively irreversible on human timescales even though the water cycle continues? What timescale mismatch does your model reveal?",
        "Agriculture uses 70% of freshwater. What does your model suggest about the relative impact of improving irrigation efficiency versus other conservation measures?",
        "How does climate change act as a threat multiplier for water scarcity? What two mechanisms does your model show working simultaneously?",
        "What are the ethical dimensions of water allocation — when there isn\\'t enough for everyone, who gets priority: cities, farms, industry, or ecosystems? What happens when ecosystems are sacrificed?",
        "How does the concept of virtual water trade mean that water scarcity in one region becomes a global economic and food security issue?"
    ],
    "dimensions": [
        ("Science Practice", "Planning and Carrying Out Investigations", "Students investigate the properties of water systems by modeling how precipitation, extraction, and recharge interact to determine groundwater availability, and how changing one variable propagates through the interconnected system."),
        ("Disciplinary Core Idea", "ESS2.C The Roles of Water in Earth\\'s Surface Processes", "Water participates in both the chemical and physical processes that shape Earth\\'s surface, including the formation and depletion of groundwater systems that are critical resources for human civilization."),
        ("Crosscutting Concept", "Cause and Effect", "Students trace the causal chains from human water extraction and climate change through groundwater depletion, ecosystem degradation, and water quality decline, identifying how short-term water use decisions produce long-term irreversible consequences.")
    ],
    "cast_items": [
        "Model how precipitation, groundwater recharge, and human extraction interact to determine regional water availability over time",
        "Predict the timeline for aquifer depletion under different demand growth and climate change scenarios",
        "Evaluate water management strategies based on model evidence about their impact on long-term water system sustainability"
    ],
    "cast_questions": [
        ("Multiple Choice:", "An aquifer has been declining 1.5 meters per year for 20 years. Climate models project 15% less precipitation in the region over the next 30 years. Which best describes the expected change to the depletion timeline? A) The aquifer will deplete at the same rate because pumping is constant B) Depletion will accelerate because reduced precipitation decreases recharge while demand stays the same C) Depletion will slow because drought reduces agricultural demand D) The aquifer will stabilize as the water table drops below economical pumping depth"),
        ("Constructed Response:", "Using your water system model, explain why a region that improves irrigation efficiency by 40% may still face groundwater depletion if population grows by 30%. Reference the concepts of recharge rate, extraction rate, and water balance in your answer.")
    ],
    "background_intro": "Water is the most essential resource for human civilization, yet it is among the most poorly managed. While 71% of Earth\\'s surface is covered by water, 97.5% is saltwater. Of the remaining 2.5% freshwater, most is locked in glaciers and ice caps. Only about 0.5% of Earth\\'s total water is accessible freshwater in rivers, lakes, and usable aquifers. This finite supply is under growing pressure from population growth, agricultural expansion, industrial demand, and climate change — a combination that is depleting aquifers faster than they can recharge and threatening the water security of billions.",
    "background_sections": [
        ("The Groundwater Crisis", "Groundwater stored in aquifers provides drinking water for over 2 billion people and irrigates 40% of the world\\'s food crops. Many of the world\\'s most important aquifers are being depleted at alarming rates. The Ogallala Aquifer under the US Great Plains — which irrigates one-third of America\\'s cropland — has lost 30% of its volume since 1960, with some areas losing over 3 meters of water level per year. The Indo-Gangetic aquifer system that supports 600 million people in India, Pakistan, and Bangladesh is declining even faster. NASA\\'s GRACE satellites have documented significant groundwater depletion in 21 of the world\\'s 37 largest aquifer systems. The fundamental problem is a timescale mismatch: these aquifers were filled over thousands to millions of years through slow geological recharge, but modern pumping technology can drain them in decades."),
        ("Agriculture: The Thirsty Giant", "Agriculture accounts for approximately 70% of global freshwater withdrawals, making it by far the largest consumer. Much of this water is used inefficiently: flood irrigation, which simply inundates fields, loses 40-60% of water to evaporation and runoff. Switching to drip irrigation can reduce water use by 50-70% while actually increasing crop yields. However, most of the world\\'s irrigated farmland still uses flood methods because drip systems require capital investment that small-scale farmers cannot afford. The types of crops matter enormously: producing 1 kilogram of wheat requires about 1,500 liters of water, while 1 kilogram of beef requires about 15,000 liters (because cattle consume water-intensive grain over their lifetime). Dietary choices and agricultural efficiency are therefore the largest levers for reducing water demand."),
        ("Climate Change and Water: The Double Squeeze", "Climate change affects water availability through two simultaneous mechanisms. First, precipitation patterns are shifting: wet regions are generally getting wetter while dry regions are getting drier, intensifying existing water stress. Second, higher temperatures increase evapotranspiration — the rate at which water evaporates from soil and transpires from plants — meaning that even with the same precipitation, less water is available because more is lost to the atmosphere. Climate models project that regions already experiencing water stress — the Middle East, North Africa, Central Asia, southwestern US, and southern Australia — will face 10-30% less water availability by 2050. Simultaneously, melting glaciers that provide seasonal meltwater for billions of people in South America and South Asia will lose 30-60% of their volume, disrupting river flows that are critical for drinking water and irrigation."),
        ("Solutions: From Efficiency to Desalination", "Water management solutions span a spectrum of cost and complexity. The cheapest interventions are efficiency improvements: drip irrigation, leak repair in distribution systems (many cities lose 30-50% of treated water to leaks), and water-efficient appliances. Water recycling for industrial and agricultural use can return 60-90% of wastewater to productive use. Managed aquifer recharge — intentionally directing excess surface water underground during wet periods — can partially offset depletion. Desalination can convert seawater to freshwater but requires significant energy (3-10 kWh per cubic meter), produces concentrated brine that harms marine ecosystems when discharged, and costs 3-5 times more than conventional freshwater in most locations. Israel has demonstrated that combining aggressive efficiency, recycling (87% of wastewater is recycled for agriculture), and desalination can transform a desert nation into a water-secure one, but this model requires sustained investment and political commitment.")
    ],
    "lever_L": "Students identify Precipitation Rate, Population and Agricultural Demand, Surface Water Availability, Groundwater Level, Water Recycling and Efficiency, Ecosystem Water Requirements, and Water Quality Index as key components of the water system.",
    "lever_E": "Students determine that extraction exceeds recharge in most agricultural aquifers, that climate change reduces both precipitation and effective water availability, that agriculture dominates demand, and that efficiency and recycling can partially but not fully offset growing demand.",
    "lever_V": "Students build a computational model of a regional water system showing how precipitation, extraction, and conservation measures determine the long-term trajectory of groundwater levels and water availability.",
    "lever_Ev": "Students run increasing extraction, climate-driven drought, and efficiency-and-reuse scenarios to test predictions about water system sustainability and the effectiveness of different management strategies.",
    "lever_R": "Students add virtual water trade, desalination infrastructure, or managed aquifer recharge to explore how additional factors affect regional water security and the options for addressing water stress.",
    "slides_guide": [
        {
            "num": "Slide 1",
            "title": "Cover",
            "visual": "Title slide with image showing contrast between water abundance (ocean) and water scarcity (dry cracked earth)",
            "say": "Water covers most of our planet, but only 0.5% is freshwater we can actually use. Today we\\'re modeling why that tiny fraction is running out in the places that need it most.",
            "do": "Show cover image. Quick stat: 2 billion people already live in water-stressed regions. Ask: What do you think would happen if the aquifer under America\\'s breadbasket ran dry?",
            "time": "2 min"
        },
        {
            "num": "Slide 2",
            "title": "Learning Objectives",
            "visual": "Four learning objectives with water cycle vocabulary and aquifer diagrams",
            "say": "We\\'re modeling the complete water system — from rain falling to aquifer depletion. By the end, you\\'ll understand why water crises are coming and what can be done to prevent them.",
            "do": "Have students read objectives. Pre-teach vocabulary. Key concept: the timescale mismatch — aquifers fill over thousands of years but can be drained in decades. This is the core problem.",
            "time": "3 min"
        },
        {
            "num": "Slide 3",
            "title": "Big Question",
            "visual": "Provocative question displayed over NASA satellite imagery showing aquifer depletion across major agricultural regions",
            "say": "We\\'re draining aquifers that took thousands of years to fill. What happens to the 2 billion people and the agriculture that depends on them when the water is gone?",
            "do": "Quick-write: Students predict what happens to a farming region when its aquifer is depleted. What are the consequences for food production, communities, and ecosystems?",
            "time": "3 min"
        },
        {
            "num": "Slide 4",
            "title": "LEVER Framework",
            "visual": "LEVER steps overview with water system examples",
            "say": "We\\'ll model a regional water system to understand the balance between recharge and extraction. This model will reveal timelines that most people don\\'t realize.",
            "do": "Preview LEVER steps. Emphasize that modeling reveals hidden timelines — the water crisis isn\\'t coming someday, it\\'s arriving on a predictable schedule that the model can calculate.",
            "time": "2 min"
        },
        {
            "num": "Slide 5",
            "title": "Activity 1: Components",
            "visual": "Seven component cards for sorting with water system illustrations",
            "say": "Which components are external inputs to the water system, and which are internal responses? Think about what drives water availability versus what responds to those drivers.",
            "do": "Guide sorting: External = Precipitation Rate (climate), Population and Agricultural Demand (human choices). Internal = the five water system responses. Discuss: Why is Groundwater Level internal when it seems like a fixed resource?",
            "time": "8 min"
        },
        {
            "num": "Slide 6",
            "title": "Activity 2: Connections",
            "visual": "Relationship diagram template with seven water system components",
            "say": "When demand exceeds what precipitation and surface water can provide, where does the extra water come from? What happens to that source over time? Trace the pathway to crisis.",
            "do": "Students draw arrows. Key insight: groundwater acts as a buffer — it fills the gap between demand and renewable supply. But unlike a bank account with deposits, the recharge deposits are tiny compared to the withdrawals. Ask: What happens when the buffer runs out?",
            "time": "8 min"
        },
        {
            "num": "Slide 7",
            "title": "Activity 3: Simulation",
            "visual": "Simulation interface showing three scenarios with groundwater level, surface water, and demand curves over time",
            "say": "Run all three scenarios and focus on the groundwater level graph. In which scenario does the aquifer stabilize? In which does it hit zero? What makes the difference?",
            "do": "Students run scenarios. Key discussion: Compare the depletion timelines across scenarios. Even the efficiency scenario only delays depletion — it doesn\\'t prevent it unless demand growth is also addressed. Ask: What would it take to actually stabilize the aquifer?",
            "time": "10 min"
        },
        {
            "num": "Slide 8",
            "title": "Discoveries",
            "visual": "Four key discoveries with graphs showing depletion rates, agriculture dominance, and climate multiplier effects",
            "say": "The most important number: aquifers took thousands of years to fill and are being drained in decades. This isn\\'t a water cycle problem — it\\'s a timescale mismatch between geology and technology.",
            "do": "Class discussion. Compare predictions to model evidence. Challenge question: If we know the aquifer will run out in 25 years, why isn\\'t that causing an emergency response right now? What explains the gap between knowledge and action?",
            "time": "5 min"
        },
        {
            "num": "Slide 9",
            "title": "STEM Challenge",
            "visual": "Engineering challenge: Design a sustainable water system for a semi-arid agricultural region of 3 million people",
            "say": "Your aquifer is declining 1.5 meters per year and will be too depleted to pump within 25 years. Design a water system that stabilizes the aquifer while keeping agriculture productive and the population growing. Every decision must be justified by your model data.",
            "do": "Groups design comprehensive water management plans addressing efficiency, recycling, alternative sources, and allocation governance. Present with specific numbers from model simulations.",
            "time": "12 min"
        }
    ],
    "sort_reasoning": "Precipitation Rate and Population and Agricultural Demand are external components because they represent inputs that the water system receives from outside — climate determines how much water enters the system, and human activity determines how much is extracted. Surface Water Availability, Groundwater Level, Water Recycling and Efficiency, Ecosystem Water Requirements, and Water Quality Index are internal because they are properties of the water system that respond to these inputs — they represent the dynamic state of the system as it processes the balance between supply and demand.",
    "relationships": [
        ("Precipitation Rate to Surface Water Availability", "POSITIVE (+)", "Higher precipitation increases river flows, lake levels, and reservoir storage, making more surface water available for human use and ecosystem needs."),
        ("Precipitation Rate to Groundwater Level", "POSITIVE (+)", "Precipitation contributes to aquifer recharge through percolation, though the recharge rate is very slow compared to extraction — only a small fraction of precipitation actually reaches the aquifer."),
        ("Population and Agricultural Demand to Groundwater Level", "NEGATIVE (-)", "Higher demand increases groundwater pumping. When extraction exceeds natural recharge, the aquifer depletes progressively, with the rate of decline proportional to the gap between extraction and recharge."),
        ("Groundwater Level to Surface Water Availability", "POSITIVE (+)", "Groundwater and surface water are connected — healthy aquifers feed springs and baseflow to rivers during dry periods. As aquifer levels drop, springs dry up and river baseflows decline, reducing surface water availability."),
        ("Water Recycling and Efficiency to Groundwater Level", "POSITIVE (+)", "Better efficiency and recycling reduce the total volume of water that must be extracted from the aquifer, slowing depletion. Drip irrigation is the single largest efficiency opportunity because agriculture dominates demand."),
        ("Ecosystem Water Requirements to Water Quality Index", "POSITIVE (+)", "When ecosystems receive sufficient water to maintain healthy rivers and wetlands, these ecosystems provide natural water purification services. When environmental flows are sacrificed to meet human demand, water quality declines as these natural treatment systems degrade.")
    ],
    "sim_answers": [
        ("Growing Demand", "With 30% demand growth and constant precipitation, Groundwater Level declines at an accelerating rate as the gap between extraction and recharge widens. Surface Water Availability also declines as rivers and springs fed by the aquifer lose baseflow. Ecosystem Water Requirements are increasingly unmet as human demand takes priority. Water Quality Index declines as less water is available to dilute pollutants. The model shows the aquifer reaching critical depletion approximately 20-25 years sooner than under current demand."),
        ("Drought Scenario", "A 20% precipitation reduction has cascading effects: Surface Water Availability drops proportionally, increasing dependence on groundwater. Groundwater recharge decreases while extraction stays constant or increases, accelerating depletion. Ecosystem Water Requirements are severely unmet. The combination of reduced supply and maintained demand compresses the timeline to crisis dramatically. The model reveals that water systems operating near capacity have almost no buffer for drought — even moderate precipitation decline can trigger rapid depletion."),
        ("Conservation Strategy", "Increasing efficiency by 40% significantly slows groundwater depletion by reducing the gap between extraction and recharge. In the model, the aquifer still declines but at a much slower rate, extending the timeline for critical depletion by 15-20 years. However, with 30% demand growth, efficiency gains alone do not stabilize the aquifer — they buy time but do not solve the fundamental imbalance. Full stabilization requires combining efficiency with demand reduction, alternative sources, and potentially managed aquifer recharge.")
    ],
    "reflection_exemplars": [
        ("Why is aquifer depletion effectively irreversible?", "The model reveals a dramatic timescale mismatch: the Ogallala Aquifer, for example, was filled over approximately 10,000 years through slow geological recharge, but modern pump technology has drained 30% of it in just 60 years. Natural recharge replaces only about 1% of the water extracted annually. At that rate, refilling a depleted aquifer would take thousands of years — far beyond any human planning horizon. Unlike surface water that cycles through evaporation and precipitation relatively quickly, groundwater moves through geological formations at millimeters to centimeters per year. Once depleted, the aquifer is effectively gone for every generation that follows. This is why hydrologists call groundwater mining — extraction faster than recharge — equivalent to mining any other non-renewable resource."),
        ("Why is agricultural water efficiency the biggest lever?", "Agriculture accounts for 70% of global freshwater withdrawals, dwarfing domestic (10%) and industrial (20%) use combined. This means that a 10% improvement in agricultural water efficiency saves more water than eliminating 70% of domestic use. The model clearly shows this dominance: in every scenario, the trajectory of Groundwater Level is primarily determined by agricultural extraction. The specific opportunity is enormous — switching from flood irrigation (which loses 40-60% to evaporation) to drip irrigation (which delivers water directly to plant roots) can reduce agricultural water use by 50-70% while actually increasing yields. No other single intervention has this magnitude of impact on the water balance. The barrier is economic: drip systems cost $1,000-$5,000 per hectare to install, which is prohibitive for subsistence farmers without subsidies or financing.")
    ],
    "stem_intro": "Present the challenge: A semi-arid agricultural region of 3 million people has an aquifer declining 1.5 meters per year, with depletion projected in 25 years at current rates. Climate projections show 15% less precipitation. The agriculture feeds 15 million people. Design a water management system that stabilizes the aquifer, maintains food production, and supports population growth — with every decision justified by model data.",
    "stem_concepts": [
        ("Irrigation Efficiency Technology", "Modern irrigation systems range from flood irrigation (40% efficiency) to center pivot sprinklers (75-85% efficiency) to subsurface drip irrigation (90-95% efficiency). Soil moisture sensors and satellite-guided precision irrigation can further optimize water application to match plant needs exactly. The technology exists to reduce agricultural water use by 50% or more, but adoption requires capital investment, training, and often government subsidies to be economically viable for farmers."),
        ("Water Recycling and Reuse", "Treated wastewater can be safely reused for irrigation, industrial cooling, and even drinking water (as demonstrated in Singapore, Namibia, and Orange County, California). Israel recycles 87% of its wastewater for agriculture, making it the world leader. Advanced treatment technologies including membrane filtration, UV disinfection, and reverse osmosis can produce recycled water that meets or exceeds drinking water standards. Water recycling effectively creates a new water supply from an existing waste stream."),
        ("Water Governance and Pricing", "Water is often priced far below its true cost, encouraging waste and overuse. Agricultural water in many countries is subsidized or free, creating no incentive for efficiency. Implementing water pricing that reflects true scarcity — while protecting low-income access through tiered pricing — is one of the most effective policy tools for reducing demand. Water rights and allocation systems also need reform: many regions still operate under historical allocation systems that distribute water based on outdated priorities rather than current needs and sustainability limits.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan stabilizes or significantly slows aquifer depletion with specific strategies justified by model data, addresses agricultural efficiency, includes alternative sources and recycling, considers equity and governance, and provides a detailed timeline with measurable milestones"),
        ("Proficient (3)", "Plan addresses major water system challenges with reasonable strategies and some connection to model evidence, includes consideration of agricultural water use"),
        ("Developing (2)", "Plan addresses some water challenges but misses critical components like agricultural efficiency or governance, weak connection to model data"),
        ("Beginning (1)", "Plan is incomplete, focuses on a single intervention, or does not address the fundamental imbalance between extraction and recharge")
    ],
    "support": [
        "Provide a visual water balance diagram showing inputs (precipitation), storage (aquifer), outputs (extraction, evaporation), and the current imbalance — students can see that the bathtub is draining faster than filling",
        "Use the bank account analogy: the aquifer is a savings account that took thousands of years to build. Recharge is like a $100/year deposit. Extraction is like $5,000/year in withdrawals. Ask: How long until the account is empty? What can you do?",
        "Sentence frames: \\'The aquifer is declining at ___ per year because extraction (___) exceeds recharge (___) by a factor of ___. The most effective intervention is ___ because it reduces extraction by ___%.\\'"
    ],
    "extensions": [
        "Research Israel\\'s water management system — how has a desert nation with minimal rainfall achieved water security through a combination of desalination, wastewater recycling, drip irrigation, and water pricing? Evaluate which strategies are transferable to other water-stressed regions",
        "Calculate the virtual water content of your daily diet — how many liters of water were required to produce each food item you ate today? Redesign one day\\'s meals to reduce virtual water consumption by 50% and evaluate the practicality of dietary water conservation",
        "Investigate the geopolitics of transboundary water resources — research a specific conflict over shared rivers (Nile, Colorado, Mekong, Jordan) and analyze how upstream water use affects downstream nations and what governance mechanisms exist to manage shared resources"
    ],
    "cross_curr": [
        ("Math", "Calculate the depletion timeline for the Ogallala Aquifer given: current volume = 3,000 cubic kilometers, annual extraction = 30 cubic km, annual recharge = 3 cubic km. Build a spreadsheet model and determine when the aquifer reaches 50% depletion under different extraction rates and with climate-adjusted recharge scenarios."),
        ("ELA", "Read John Steinbeck\\'s description of drought and water scarcity in The Grapes of Wrath alongside contemporary reporting on the Colorado River crisis. Write a comparative essay analyzing how water scarcity creates human suffering across different time periods and how the scale of the crisis has changed."),
        ("History", "Research the collapse of the Aral Sea — once the fourth-largest lake in the world, reduced to 10% of its original size by Soviet-era irrigation diversions. Analyze how centralized water management decisions destroyed an entire ecosystem and the communities that depended on it, and draw parallels to current aquifer depletion patterns.")
    ],
    "misconceptions": [
        ("The water cycle means water is always renewable", "The water cycle does continuously recycle water through evaporation, precipitation, and runoff. However, groundwater operates on a very different timescale from surface water. While rain and river water cycle in days to months, groundwater in deep aquifers can be thousands to millions of years old and recharges at millimeters per year. Extracting this ancient groundwater faster than it recharges is functionally equivalent to mining a non-renewable resource. The water cycle does not replenish aquifers on any timescale relevant to human civilization once they are depleted.", "Fill a large container with water (representing the aquifer) and poke a tiny hole in the bottom (representing natural recharge). Then have students pump water out with a syringe at 50x the drip rate. How long until the container is empty? How long would it take the drip alone to refill it?"),
        ("Desalination can solve all water scarcity problems", "While desalination technology works and is improving, it faces significant limitations. It requires 3-10 kWh per cubic meter of freshwater produced — enormous energy demand at scale. It produces concentrated brine waste that harms marine ecosystems when discharged. It costs 3-5 times more than conventional freshwater in most locations. And it is only practical for coastal areas — landlocked regions and their agriculture cannot benefit. Desalination is one tool in the water management toolkit, but it is not a universal solution and cannot replace sustainable management of existing freshwater resources.", "Calculate the energy needed to desalinate enough water for agricultural irrigation in an inland farming region. Compare this energy to the region\\'s total electricity generation. Students will discover that the energy requirement is impossibly large for agricultural-scale desalination in most locations."),
        ("Water scarcity is a developing-world problem that doesn\\'t affect wealthy nations", "The western United States, Australia, and southern Europe all face severe water stress. The Colorado River — which supplies water to 40 million Americans — no longer reaches the sea because every drop is extracted upstream. California\\'s Central Valley has sunk by up to 9 meters due to groundwater depletion. Cape Town, South Africa nearly ran out of water in 2018. Wealthy nations can afford expensive infrastructure, but they cannot create water that doesn\\'t exist. As climate change intensifies drought and aquifers continue declining, water scarcity will increasingly affect rich and poor nations alike.", "Show satellite images of Lake Mead and the Colorado River delta over the past 30 years. Ask: Does this look like a developing-world problem? Show California\\'s land subsidence maps. The visual evidence makes the case that water scarcity is a universal challenge.")
    ]
}

L08 = {
    "id": "G12L2-L08",
    "title": "How Do Wildfires Reshape Ecosystems?",
    "subtitle": "Modeling Fire Ecology, Ecological Succession, and Climate-Fire Interactions",
    "ngss": "HS-LS2-2",
    "ngss_desc": "Use mathematical representations to support and revise explanations based on evidence about factors affecting biodiversity and populations in ecosystems of different scales.",
    "big_question": "For millions of years, fire was an essential force that maintained healthy ecosystems — so how did something natural become one of the most devastating consequences of climate change, and what does the new era of megafires mean for forests, communities, and the atmosphere?",
    "objectives": [
        "Model how fire behavior, vegetation type, soil moisture, and climate conditions interact to determine the ecological impact of wildfires",
        "Explain why fire suppression policies that prevent natural low-intensity fires create conditions for catastrophic high-intensity fires",
        "Predict how climate change is altering fire regimes and shifting the balance from beneficial to destructive fire in different ecosystems",
        "Analyze fire management strategies that incorporate ecological fire principles while protecting human communities"
    ],
    "vocabulary": [
        ("Fire Regime", "The historical pattern of fire frequency, intensity, and extent in a given ecosystem — fire-adapted ecosystems like longleaf pine savannas evolved with frequent low-intensity fires every 2-5 years, while boreal forests experience high-intensity stand-replacing fires every 100-300 years, and disrupting these natural fire regimes has severe ecological consequences"),
        ("Ecological Succession", "The process by which an ecosystem changes in composition over time following a disturbance — primary succession occurs on bare ground, secondary succession follows fire or other disturbance, and the type and severity of fire determines whether an ecosystem regenerates along its historical trajectory or shifts to a fundamentally different state"),
        ("Fuel Load", "The amount and arrangement of combustible material in an ecosystem — including dead leaves, branches, bark, and entire trees, fuel load accumulates over time when fire is suppressed, creating conditions for high-intensity crown fires instead of the low-intensity surface fires the ecosystem evolved with"),
        ("Crown Fire", "A wildfire that spreads through the canopy of trees rather than along the ground — crown fires are extremely intense, difficult to control, and often kill even large fire-resistant trees, destroying the seed sources needed for forest regeneration and potentially converting forest to shrubland or grassland permanently")
    ],
    "components": [
        ("Climate and Weather Conditions", "Temperature, humidity, wind speed, and drought status that determine fire behavior — hotter, drier, and windier conditions increase fire intensity and spread rate, and climate change is extending fire seasons by an average of 40-80 days in many regions", True),
        ("Fuel Load Accumulation", "The buildup of dead vegetation and ladder fuels in fire-suppressed forests — a century of fire suppression has created unnaturally dense forests with 5-10 times more fuel than historical conditions, setting the stage for catastrophic fires that exceed any historical precedent", True),
        ("Fire Intensity", "The amount of energy released by a wildfire per unit of time and area — determined by fuel load, moisture content, weather, and terrain, with low-intensity surface fires burning at temperatures that most trees survive versus crown fires reaching temperatures that kill even fire-resistant species", False),
        ("Soil Health and Seed Bank", "The condition of soil biology and the viable seeds stored in the soil that determine post-fire recovery — low-intensity fires sterilize the top centimeter of soil while leaving deeper seed banks and mycorrhizal networks intact, but high-intensity fires can sterilize the soil to 10+ cm depth, destroy seed banks, and create hydrophobic layers that increase erosion", False),
        ("Post-Fire Vegetation Recovery", "The speed and composition of plant regrowth after fire — determined by fire intensity, seed availability, soil condition, and post-fire precipitation, with healthy fire-adapted ecosystems recovering within 5-15 years from natural fires but potentially failing to recover from unnaturally severe fires", False),
        ("Forest Carbon Balance", "The net carbon flux between the forest ecosystem and atmosphere — healthy forests are carbon sinks that absorb more CO2 than they release, but catastrophic wildfires release stored carbon rapidly while destroying the living trees that would reabsorb it, potentially converting forests from carbon sinks to carbon sources", False),
        ("Ecosystem Resilience", "The ability of the ecosystem to absorb disturbance and return to a functional state — fire-adapted ecosystems have high resilience to fires within their historical regime but low resilience to fires that exceed historical intensity, and repeated megafires can push ecosystems past tipping points into permanently altered states", False)
    ],
    "think_about_it": "When Climate and Weather Conditions become hotter and drier while Fuel Load Accumulation has been increasing for decades due to fire suppression, what happens to Fire Intensity? If Fire Intensity exceeds the level the ecosystem evolved with, what happens to Soil Health, Post-Fire Recovery, and long-term Ecosystem Resilience?",
    "scenarios": [
        ("Historical Natural Fire", "Model a fire regime consistent with pre-suppression conditions — moderate Fuel Load, natural Climate Conditions, and periodic low-intensity fires — observe how the ecosystem responds and recovers"),
        ("Fire Suppression Legacy", "Model a fire after 100 years of suppression — maximum Fuel Load with current Climate Conditions — observe how accumulated fuel transforms fire behavior and ecological impact"),
        ("Climate-Amplified Megafire", "Model a fire under climate change conditions — maximum Fuel Load combined with extreme heat, drought, and wind — observe the cascading effects on soil, recovery, carbon balance, and long-term ecosystem state")
    ],
    "sim_scenarios": [
        ("Historical Natural Fire", "Fuel Load: Moderate (Natural) | Climate: Historical Average | Fire Type: Surface", "When fire burns through an ecosystem with natural fuel levels under historical conditions, what do you predict happens to Soil Health, Post-Fire Recovery, and Ecosystem Resilience?"),
        ("Suppression Legacy Fire", "Fuel Load: Maximum (100yr Accumulation) | Climate: Current | Fire Type: Mixed Surface/Crown", "After a century of fire suppression, the forest has 5-10x more fuel than natural. What happens when this fuel finally burns? How does fire intensity change and what cascading effects follow?"),
        ("Climate Megafire", "Fuel Load: Maximum | Climate: Extreme (Drought + Heat + Wind) | Fire Type: Crown", "When accumulated fuel meets climate-amplified conditions, what does the model predict about fire intensity, soil sterilization, and the ecosystem\\'s ability to recover? Could this push the ecosystem past a tipping point?")
    ],
    "discoveries": [
        "Natural low-intensity fires are essential for ecosystem health — the model shows that ecosystems with regular, moderate fire maintain higher biodiversity, healthier soil, and greater resilience than fire-suppressed ecosystems",
        "A century of fire suppression has created a dangerous paradox — by preventing small fires that reduce fuel, we have guaranteed large fires that destroy ecosystems, making the forests we tried to protect more vulnerable than they have been in centuries",
        "Climate change amplifies the fire suppression legacy — hotter temperatures, longer droughts, and lower humidity transform already dangerous fuel loads into conditions for fires of unprecedented intensity that exceed any historical analogue",
        "High-intensity megafires can push ecosystems past recovery tipping points — when fire sterilizes soil, destroys seed banks, and kills seed-producing trees, the ecosystem may not regenerate as forest at all, instead converting permanently to shrubland or grassland in a type-conversion that represents irreversible habitat loss"
    ],
    "answer": "Wildfires reshape ecosystems in profoundly different ways depending on their intensity, which is determined by the interaction of fuel load, climate conditions, and historical fire management. For millions of years, natural fires were an essential ecological process — frequent low-intensity surface fires cleared understory, recycled nutrients, stimulated seed germination, and maintained the open forest structure that many species depend on. A century of fire suppression disrupted this process, allowing fuel to accumulate to unprecedented levels. Now, climate change is adding extreme heat, drought, and wind to these fuel-loaded forests, producing megafires of intensity that no historical ecosystem experienced. The model reveals a critical threshold: low-intensity fires rejuvenate ecosystems, but high-intensity crown fires can sterilize soil, destroy seed banks, and kill the mature trees needed for regeneration — pushing the ecosystem past a tipping point from which forest recovery may be impossible. The ecological consequence is type-conversion: forests permanently replaced by shrubland or grassland, with cascading effects on biodiversity, water resources, and carbon storage. The solution is not more fire suppression but smarter fire management — prescribed burns that reduce fuel, strategic thinning, and community protection that allows fire to play its natural ecological role.",
    "stem_title": "Design a Community Wildfire Resilience Plan",
    "stem_mission": "Design a comprehensive wildfire management plan for a community at the wildland-urban interface that balances fire suppression for community protection with ecological fire management for long-term forest health.",
    "stem_scenario": "A mountain community of 25,000 people is surrounded by fire-suppressed forest with extreme fuel loads. The region has experienced increasing drought and temperature, and fire season has lengthened by 50 days over the past 30 years. Two major fires in the past five years burned over 100,000 acres each and destroyed 500 homes. Ecologists warn that continued fire suppression will only make future fires worse. Your team must design a plan that protects the community while restoring natural fire regimes to surrounding forests — reducing the risk of catastrophic fire through proactive management rather than reactive suppression.",
    "stem_questions": [
        "Based on your model, how does reducing Fuel Load through prescribed burns change the predicted Fire Intensity and ecological impact of the next wildfire?",
        "What does your model show about the relationship between defensible space around homes and community survival during moderate versus extreme fire events?",
        "How does restoring natural fire frequency to surrounding forests change long-term Ecosystem Resilience compared to continued total fire suppression?"
    ],
    "stem_design_qs": [
        "What specific fuel reduction strategies does your plan implement — prescribed burns, mechanical thinning, or both — and what is the treatment area and timeline?",
        "How does your plan create defensible space around the community while allowing ecological fire management in surrounding forests?",
        "What early warning and evacuation systems does your plan include for community protection during inevitable wildfire events?",
        "How does your plan balance short-term political pressure to suppress all fires with the scientific evidence that fire suppression increases long-term risk?"
    ],
    "career": "Fire ecologists who study how fire shapes ecosystems and design prescribed burn programs work for the Forest Service, National Park Service, and land management agencies, earning $55,000-$110,000/year. Wildfire management specialists who coordinate fire suppression, community protection, and resource deployment earn $60,000-$120,000/year. Climate adaptation planners who integrate fire risk into community planning and land use policy earn $65,000-$125,000/year.",
    "images": {
        "cover": ("G12L2-L08-cover.png", "A photorealistic image of diverse 17-18 year old students examining fire ecology specimens and charred wood samples in a modern environmental science lab, with prescribed burn images and forest succession diagrams visible on displays"),
        "landscape": ("G12L2-L08-landscape.png", "A photorealistic image showing a split landscape — one side showing a healthy fire-maintained open forest with diverse undergrowth, the other showing a dense fire-suppressed forest choked with dead fuel and ladder fuels"),
        "modeling": ("G12L2-L08-modeling.png", "A photorealistic image of diverse 17-18 year old students building fire behavior and ecosystem recovery models on laptops, with fire intensity maps and succession diagrams projected on a smartboard"),
        "discussion": ("G12L2-L08-discussion.png", "A photorealistic image of a teacher leading a discussion with diverse 17-18 year old students about fire ecology paradoxes, with before-and-after forest images and fire regime graphs displayed on screen"),
        "stem": ("G12L2-L08-stem.png", "A photorealistic image of diverse 17-18 year old students designing wildfire resilience plans on large maps, marking prescribed burn zones, defensible space perimeters, and evacuation routes")
    },
    "pre_assessment": [
        "Is wildfire always bad for the environment, or can it be beneficial? What do you think happened to forests before humans started fighting fires?",
        "Why do you think wildfires have been getting larger and more destructive in recent decades? What factors contribute to this trend?",
        "What is a prescribed burn and why would scientists intentionally set a forest on fire? What would be the purpose?",
        "If you lived in a fire-prone area, what steps could protect your home and community from wildfire?"
    ],
    "extend_components": [
        ("Wildland-Urban Interface Density", "The number of homes and structures built in fire-prone areas at the boundary between developed and natural land — the WUI has expanded dramatically as housing development pushes into fire-adapted landscapes, putting more people and property at risk while making fire suppression politically mandatory even when ecologically harmful"),
        ("Atmospheric Smoke and Air Quality", "The impact of wildfire smoke on regional air quality and human health — megafires produce smoke plumes that travel thousands of miles, causing respiratory illness, cardiovascular problems, and premature death far from the fire itself, with the health burden falling disproportionately on outdoor workers and low-income communities"),
        ("Post-Fire Hydrology", "Changes to watershed behavior after fire — burned forests lose their ability to absorb rainfall, causing increased flooding, erosion, and sediment loading in downstream waterways, with high-intensity fires creating hydrophobic soil layers that dramatically increase runoff and debris flow risk for 3-10 years after the fire")
    ],
    "reflections": [
        "How does your model demonstrate the paradox that preventing fire (suppression) actually increases fire risk? Trace the feedback loop from suppression to fuel accumulation to catastrophic fire.",
        "What is the difference between fire in an ecosystem that evolved with it versus fire in a system with a century of accumulated fuel? How does your model show this difference in ecological outcomes?",
        "Climate change is making fire seasons longer, hotter, and drier. How does your model show the interaction between climate amplification and the fire suppression legacy?",
        "What does type-conversion mean in the context of post-fire recovery, and why is it ecologically significant? How does your model identify the conditions that lead to it?",
        "Why is it politically difficult to implement prescribed burns and allow natural fire even when the science clearly supports it? How would you make the case to a community?"
    ],
    "dimensions": [
        ("Science Practice", "Using Mathematics and Computational Thinking", "Students use computational models to quantify how fire intensity, soil health, and recovery dynamics interact to determine ecosystem outcomes under different fire management and climate scenarios."),
        ("Disciplinary Core Idea", "LS2.C Ecosystem Dynamics, Functioning, and Resilience", "Ecosystems are dynamic and subject to natural disturbances like fire that can be essential for maintaining health and diversity. When disturbance regimes are altered beyond historical ranges, ecosystems may shift to fundamentally different and less diverse states."),
        ("Crosscutting Concept", "Stability and Change", "Students analyze how fire-adapted ecosystems maintain stability through regular natural disturbance, how disrupting the disturbance regime creates instability, and how climate change is shifting the balance from stabilizing fire to destabilizing megafire.")
    ],
    "cast_items": [
        "Model how fuel accumulation, climate conditions, and fire behavior interact to determine ecological impacts of wildfire at different intensities",
        "Predict post-fire ecosystem trajectories based on fire intensity, soil health, and seed bank survival using mathematical representations",
        "Evaluate fire management strategies that balance community protection with ecological fire restoration"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A fire-suppressed forest has 8x the natural fuel load. A wildfire ignites during extreme drought conditions. Which outcome does the model predict? A) The fire burns at low intensity because the trees are large and healthy B) The fire burns at extreme intensity, sterilizing the soil and killing seed-producing trees, potentially preventing forest regeneration C) The thick fuel slows the fire spread D) Fire-adapted trees survive regardless of intensity"),
        ("Constructed Response:", "Using your fire ecology model, explain why a forest managed with regular prescribed burns is more likely to survive a wildfire than a fire-suppressed forest, even under identical climate and weather conditions. Reference at least three components including Fuel Load, Fire Intensity, and Soil Health in your answer.")
    ],
    "background_intro": "Fire has shaped Earth\\'s ecosystems for at least 420 million years — since the first land plants created enough fuel and atmospheric oxygen to sustain combustion. Many of the world\\'s most biodiverse and productive ecosystems evolved with fire as an essential ecological process: grasslands, savannas, Mediterranean shrublands, boreal forests, and many temperate forests depend on periodic fire to maintain their structure and diversity. But over the past century, a profound shift has occurred: fire suppression policies, climate change, and development in fire-prone areas have transformed fire from an ecological ally into one of the most destructive forces facing natural and human communities.",
    "background_sections": [
        ("Fire as an Ecological Necessity", "Many plant species are not merely tolerant of fire — they require it. Longleaf pine cannot regenerate without fire to clear competing hardwoods. Giant sequoias need fire\\'s heat to open their seed cones. Fireweed and other pioneer species are triggered by fire\\'s chemical signals in soil. Fire-adapted grasslands like prairies lose their characteristic plant diversity without periodic burning as woody shrubs invade. The mechanism varies by ecosystem: in frequently-burned systems, low-intensity surface fires clear dead material, recycle nutrients back to the soil, reduce disease and insect populations, and create the open understory conditions that native species need. This is not coincidence — these ecosystems evolved over millions of years with fire as a regular selective pressure, and the species that thrive in them are specifically adapted to the fire regime."),
        ("The Fire Suppression Paradox", "Beginning in the early 1900s, the US adopted a policy of suppressing all wildfires — the famous Smokey Bear campaign. This policy was remarkably successful at reducing burned acreage: by the mid-20th century, annual US fire area had dropped to a fraction of historical levels. But this success created an invisible crisis. In ecosystems that historically burned every 5-15 years, decades without fire allowed unprecedented fuel accumulation: dense understory growth, dead branches and trees, and ladder fuels that connect ground fire to the canopy. Forests that historically had 20-40 trees per acre now had 200-400. When fire inevitably returned to these fuel-loaded forests, it burned with an intensity that no historical fire ever reached — leaping into the canopy, killing entire forest stands, and sterilizing the soil. The paradox: by suppressing small fires, we guaranteed enormous ones."),
        ("Climate Change: Amplifying the Danger", "Climate change is transforming fire regimes worldwide through multiple mechanisms. Higher temperatures increase evapotranspiration, drying vegetation and soil faster. Earlier snowmelt extends the fire season by 40-80 days in many regions. Drought intensity and duration are increasing in fire-prone areas. Warmer winters allow bark beetles to survive and kill more trees, adding dead fuel to already overloaded forests. The result is measurable: the area burned annually in the western US has increased by approximately 1,000% since 1970. Global burned area in boreal and temperate forests is at record levels. Climate models project continued increases in fire weather severity throughout the 21st century, with some regions facing fire conditions that have no historical precedent."),
        ("Megafires and Type-Conversion", "When fire intensity exceeds the evolutionary experience of an ecosystem, recovery may not follow the expected trajectory. Megafires — defined by their extreme behavior, enormous size, and unprecedented intensity — can sterilize soil to depths that destroy seed banks and mycorrhizal networks, create hydrophobic soil layers that prevent water infiltration for years, and kill all seed-producing trees within fire perimeters so large that seeds from surrounding forests cannot reach the center. The result can be type-conversion: permanent ecosystem transformation from forest to shrubland or grassland. This has been documented across the western US, where repeated high-severity fire has converted millions of acres of conifer forest to non-forest vegetation. Type-conversion represents irreversible biodiversity loss and a shift from carbon sink to carbon source — the forest\\'s stored carbon is released by fire and never reabsorbed because the forest does not return.")
    ],
    "lever_L": "Students identify Climate and Weather Conditions, Fuel Load Accumulation, Fire Intensity, Soil Health and Seed Bank, Post-Fire Vegetation Recovery, Forest Carbon Balance, and Ecosystem Resilience as key components of the fire ecology system.",
    "lever_E": "Students determine that fuel load and climate conditions together determine fire intensity, that fire intensity determines whether soil and seed banks survive, that soil and seed bank survival determines recovery trajectory, and that repeated megafires can push ecosystems past resilience tipping points.",
    "lever_V": "Students build a computational model showing how fire behavior interacts with ecosystem components to produce different ecological outcomes depending on the intensity and frequency of fire.",
    "lever_Ev": "Students run historical natural fire, suppression legacy fire, and climate-amplified megafire scenarios to test predictions about how fire management and climate change determine ecosystem trajectories.",
    "lever_R": "Students add wildland-urban interface density, smoke impacts, or post-fire hydrology to explore how additional factors complicate fire management decisions and affect human communities.",
    "slides_guide": [
        {
            "num": "Slide 1",
            "title": "Cover",
            "visual": "Title slide with dramatic split image: healthy fire-maintained forest versus fire-suppressed forest during megafire",
            "say": "For millions of years, fire was an ecosystem\\'s best friend. Now it\\'s one of the most destructive forces on the planet. Today we\\'re modeling what changed and what we can do about it.",
            "do": "Show cover image. Quick question: Is fire always bad for forests? Take initial predictions — most students will say yes. By the end of class, they\\'ll understand why the answer is much more complex.",
            "time": "2 min"
        },
        {
            "num": "Slide 2",
            "title": "Learning Objectives",
            "visual": "Four learning objectives with fire ecology vocabulary and ecosystem succession images",
            "say": "By the end of today, you\\'ll understand a profound paradox: preventing fire is one of the most dangerous things we\\'ve ever done to forests.",
            "do": "Have students read objectives. Pre-teach vocabulary. Key concept: fire regime — the pattern of fire an ecosystem evolved with. Disrupting this pattern has consequences.",
            "time": "3 min"
        },
        {
            "num": "Slide 3",
            "title": "Big Question",
            "visual": "Provocative question over images showing natural fire ecology alongside megafire destruction",
            "say": "How did something natural become one of the most devastating consequences of climate change? The answer involves a century-long experiment in fire suppression that backfired — literally.",
            "do": "Quick-write: Students write what they think would happen if we stopped fighting all wildfires. Save for comparison — the answer is counterintuitive.",
            "time": "3 min"
        },
        {
            "num": "Slide 4",
            "title": "LEVER Framework",
            "visual": "LEVER steps overview with fire ecology examples for each step",
            "say": "We\\'ll model fire as an ecological process — not a disaster. This model will reveal why the intensity of fire, not just its occurrence, determines whether it helps or destroys ecosystems.",
            "do": "Preview LEVER steps. Emphasize that fire is a variable, not a binary — low-intensity fire and high-intensity fire produce completely different ecological outcomes.",
            "time": "2 min"
        },
        {
            "num": "Slide 5",
            "title": "Activity 1: Components",
            "visual": "Seven component cards for sorting with fire ecology illustrations",
            "say": "Which components are external drivers of fire behavior, and which are internal ecosystem responses? Think about what sets up fire conditions versus what happens to the ecosystem during and after fire.",
            "do": "Guide sorting: External = Climate/Weather Conditions, Fuel Load Accumulation. Internal = the five ecosystem response variables. Discuss: Fuel Load is external because it\\'s determined by management history, but it drives internal fire dynamics.",
            "time": "8 min"
        },
        {
            "num": "Slide 6",
            "title": "Activity 2: Connections",
            "visual": "Relationship diagram with seven fire ecology components",
            "say": "Trace the cascade from fuel load and climate to fire intensity to soil health to recovery. Where does the system branch between recovery and permanent ecosystem change?",
            "do": "Students draw arrows. Key discovery: the tipping point where Fire Intensity exceeds Soil Health and Seed Bank survival threshold — this is where the system branches between recovery and type-conversion. Ask: What determines which side of the threshold a fire falls on?",
            "time": "8 min"
        },
        {
            "num": "Slide 7",
            "title": "Activity 3: Simulation",
            "visual": "Simulation showing three fire scenarios with graphs of intensity, soil health, recovery, and carbon balance",
            "say": "Run all three scenarios and watch how dramatically different the outcomes are. The historical natural fire builds ecosystem health. The megafire may destroy it permanently.",
            "do": "Students run scenarios. Key discussion: Compare the natural fire and megafire scenarios — same process (combustion), completely different ecological outcomes. What made the difference? Guide toward fuel load and intensity as the critical variables.",
            "time": "10 min"
        },
        {
            "num": "Slide 8",
            "title": "Discoveries",
            "visual": "Four key discoveries with graphs contrasting natural fire benefits with megafire destruction",
            "say": "The biggest paradox in fire management: by preventing all fire for a century, we created the conditions for the most destructive fires in history. Let\\'s discuss what this means for policy.",
            "do": "Class discussion. Revisit initial predictions. Key challenge: How do you explain to the public that fighting fires can make fires worse? This is a communication challenge as much as a science one.",
            "time": "5 min"
        },
        {
            "num": "Slide 9",
            "title": "STEM Challenge",
            "visual": "Engineering challenge: Design a wildfire resilience plan for a mountain community of 25,000",
            "say": "Your community has experienced two devastating megafires in five years. Ecologists say continued suppression will make things worse. Design a plan that protects people while restoring natural fire. Use your model data.",
            "do": "Groups design comprehensive wildfire resilience plans balancing community protection (defensible space, evacuation) with ecological fire management (prescribed burns, fuel reduction). Present with model evidence.",
            "time": "12 min"
        }
    ],
    "sort_reasoning": "Climate and Weather Conditions and Fuel Load Accumulation are external components because they represent the conditions that exist before a fire occurs — climate is determined by global atmospheric processes, and fuel load is determined by decades of management history. Fire Intensity, Soil Health and Seed Bank, Post-Fire Vegetation Recovery, Forest Carbon Balance, and Ecosystem Resilience are internal because they are responses generated within the ecosystem during and after fire — they represent how the ecosystem processes the external conditions through combustion and recovery dynamics.",
    "relationships": [
        ("Fuel Load Accumulation to Fire Intensity", "POSITIVE (+)", "More fuel produces more intense fire — dense understory, dead trees, and continuous fuel allow surface fires to ladder into the canopy, transforming manageable surface fires into devastating crown fires."),
        ("Climate and Weather Conditions to Fire Intensity", "POSITIVE (+)", "Hotter temperatures, lower humidity, stronger winds, and drought all increase fire intensity by drying fuel, increasing combustion rate, and driving fire spread. Climate change is amplifying all of these factors."),
        ("Fire Intensity to Soil Health and Seed Bank", "NEGATIVE (-)", "Low-intensity surface fires sterilize only the top centimeter of soil, leaving deeper seed banks and mycorrhizal networks intact. High-intensity fires sterilize to 10+ cm, destroy seed banks, and create hydrophobic layers."),
        ("Soil Health and Seed Bank to Post-Fire Vegetation Recovery", "POSITIVE (+)", "Healthy soil with intact seed banks and mycorrhizal networks supports rapid regeneration — seeds germinate, nutrients are available, and water is retained. Sterilized soil lacks all of these prerequisites for recovery."),
        ("Post-Fire Vegetation Recovery to Forest Carbon Balance", "POSITIVE (+)", "Strong vegetation recovery reestablishes the forest as a carbon sink as growing trees absorb CO2. Failed recovery means the carbon released by fire is never reabsorbed, and the ecosystem becomes a permanent carbon source."),
        ("Ecosystem Resilience to Post-Fire Vegetation Recovery", "POSITIVE (+)", "Resilient ecosystems with intact biodiversity, healthy soil biology, and genetic diversity among tree species recover faster and more completely from fire. Repeated megafires erode resilience, making each subsequent recovery more difficult.")
    ],
    "sim_answers": [
        ("Historical Natural Fire", "Under historical conditions with moderate fuel loads, the model produces low-intensity surface fire. Soil Health and Seed Bank are minimally affected — the top centimeter is sterilized but deeper layers remain intact. Post-Fire Vegetation Recovery begins within weeks as fire-adapted species germinate. Within 5-10 years, the ecosystem is fully recovered with increased biodiversity and reduced fuel load. Forest Carbon Balance shows a brief spike of emissions during the fire followed by enhanced absorption as vigorous new growth occurs. Ecosystem Resilience actually increases after natural fire because fuel has been reduced and nutrient cycling refreshed."),
        ("Fire Suppression Legacy", "With 100 years of fuel accumulation, the model produces mixed-severity fire with significant crown fire patches. Fire Intensity is 5-10x higher than the natural scenario. Soil Health is severely impacted in crown fire areas — seed banks destroyed, mycorrhizal networks killed, hydrophobic layers formed. Post-Fire Recovery is delayed and patchy, with forest regeneration occurring in low-severity patches but failing in high-severity areas where no seed sources remain. Forest Carbon Balance shows large net carbon release. Ecosystem Resilience is significantly reduced."),
        ("Climate Megafire", "Maximum fuel combined with extreme climate conditions produces sustained crown fire across the entire landscape. Fire Intensity is unprecedented — exceeding any fire in the ecosystem\\'s evolutionary history. Soil is sterilized deeply and extensively. Seed banks are destroyed across such a large area that recolonization from edges cannot reach the interior. The model predicts type-conversion: the forest does not regenerate as forest but is replaced by shrubs or grass. Forest Carbon Balance shows massive, permanent carbon loss. Ecosystem Resilience effectively reaches zero for the forest ecosystem.")
    ],
    "reflection_exemplars": [
        ("Why does preventing fire make fire more dangerous?", "Our model clearly demonstrates the suppression paradox. When natural low-intensity fires are prevented, Fuel Load Accumulation increases every year — dead branches, leaf litter, small trees, and ladder fuels build up continuously. In ecosystems that historically burned every 5-15 years, a century without fire creates fuel loads 5-10 times higher than natural conditions. When fire inevitably occurs — from lightning, human accident, or arson — this massive fuel load produces Fire Intensity far beyond what the ecosystem evolved to withstand. The model shows that the same forest, under the same climate conditions, produces dramatically different fire outcomes depending on fuel load: natural fuel produces surface fire that rejuvenates; suppression-era fuel produces crown fire that destroys. The policy intended to protect forests has made them more vulnerable than at any point in their evolutionary history."),
        ("What does type-conversion mean for long-term ecosystem health?", "Type-conversion occurs when fire exceeds the ecosystem\\'s evolutionary experience so severely that it cannot recover to its pre-fire state. The model shows the mechanism clearly: when Fire Intensity sterilizes soil deeply enough to destroy seed banks and kill mycorrhizal networks, and when the fire perimeter is so large that seeds from surviving forests cannot reach the interior, the conditions for tree regeneration simply do not exist. Instead, fast-colonizing shrubs and grasses establish and prevent tree seedlings from competing. This is not temporary — the new shrubland is stable and self-reinforcing. The ecological consequences are cascading: species that depended on forest structure lose their habitat, carbon that was stored in the forest is permanently released, watershed function is degraded, and the capacity of the landscape to support biodiversity is fundamentally reduced. Type-conversion is effectively an irreversible loss.")
    ],
    "stem_intro": "Present the challenge: A mountain community of 25,000 has experienced two devastating megafires in five years because surrounding forests are fuel-loaded from a century of suppression and climate is getting hotter and drier. Ecologists say continued total suppression will produce even worse fires. Design a plan that protects the community while restoring healthy fire regimes to surrounding forests — using model data to justify every decision.",
    "stem_concepts": [
        ("Prescribed Burns and Fuel Reduction", "Intentionally setting controlled fires under carefully planned conditions to reduce fuel loads and restore natural fire regimes. Prescribed burns are conducted during moderate weather windows by trained crews who control fire boundaries. When done correctly, they reduce fuel loads by 60-80%, dramatically decreasing the intensity of subsequent wildfires. The barrier is public perception — burning forests intentionally is counterintuitive and faces political opposition, especially when smoke affects nearby communities."),
        ("Defensible Space and Fire-Resistant Communities", "Creating zones around homes and communities where vegetation is managed to reduce fire risk — typically 100+ feet of cleared or thinned vegetation around structures, fire-resistant building materials (metal roofs, tempered glass, fiber cement siding), and landscape design that does not allow fire to ladder from vegetation to structures. Studies show that homes with adequate defensible space survive wildfires at rates 5-10 times higher than homes without."),
        ("Managed Wildfire and Fire Use", "Allowing naturally ignited fires to burn under monitored conditions in designated areas, using them as a free fuel reduction tool. This approach, used successfully in wilderness areas, acknowledges that fire is inevitable and can be beneficial. The key is managing where and when fire burns rather than trying to eliminate it entirely — suppressing fire near communities while allowing it in backcountry areas with appropriate monitoring.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan integrates community protection with ecological fire restoration, specifies fuel reduction areas and methods, includes defensible space standards, addresses climate projections, and justifies all decisions with model evidence about the relationship between fuel load, fire intensity, and ecosystem outcomes"),
        ("Proficient (3)", "Plan addresses both community protection and fuel management with reasonable strategies and some connection to model data"),
        ("Developing (2)", "Plan focuses on either community protection or ecological management but not both, or lacks connection to model evidence about fire intensity and ecosystem dynamics"),
        ("Beginning (1)", "Plan relies solely on fire suppression without addressing the underlying fuel load and climate drivers identified by the model")
    ],
    "support": [
        "Provide a visual showing the same forest under natural fire regime versus fire suppression — students can physically see the difference in fuel density, understory, and forest structure that determines fire behavior",
        "Use the pressure cooker analogy: fire suppression is like sealing the lid on a pressure cooker and turning up the heat. The pressure (fuel) keeps building. Either you release it gradually (prescribed burns) or it explodes catastrophically (megafire). Which is safer?",
        "Sentence frames: \\'Under historical conditions with ___ fuel load, Fire Intensity is ___. After 100 years of suppression with ___ fuel load, Fire Intensity becomes ___ because ___. This changes the ecosystem outcome from ___ to ___.\\'"
    ],
    "extensions": [
        "Research the fire management practices of Indigenous peoples — for thousands of years, Native Americans used cultural burning to manage landscapes across North America. Investigate how traditional ecological knowledge about fire is being integrated into modern fire management and what barriers exist",
        "Analyze satellite imagery of a specific recent megafire (Paradise/Camp Fire 2018 or Marshall Fire 2021) — map the fire perimeter, identify the relationship between vegetation type and burn severity, and evaluate whether the community had adequate defensible space",
        "Design a carbon accounting framework for wildfires — calculate the CO2 emissions from a 100,000-acre megafire versus the carbon savings from prescribed burns that prevent it, and determine the net carbon benefit of proactive fire management"
    ],
    "cross_curr": [
        ("Math", "Model fire spread rate using the Rothermel fire spread equation, which incorporates fuel moisture, wind speed, slope, and fuel characteristics. Calculate how doubling fuel load affects spread rate and intensity, and determine the fuel reduction needed to bring fire behavior within historical ranges."),
        ("ELA", "Read accounts of the 2018 Camp Fire (Paradise, California) alongside historical accounts of beneficial Native American burning practices. Write an analytical essay examining how Western suppression philosophy directly created the conditions for the deadliest wildfire in California history."),
        ("History", "Research the history of US fire policy from the 1910 Big Blowup through the creation of Smokey Bear to the modern recognition of fire\\'s ecological role. Analyze how a single catastrophic fire event (1910) shaped a century of policy that ultimately increased fire risk rather than reducing it.")
    ],
    "misconceptions": [
        ("All wildfire is bad and should be prevented", "Fire is an essential ecological process that many ecosystems require for health and regeneration. Fire-adapted species need periodic fire for seed germination, nutrient cycling, and habitat maintenance. The problem is not fire itself but fire of unnatural intensity in fuel-loaded, climate-stressed forests. Low-intensity fire is ecological medicine; high-intensity megafire is ecological catastrophe. The distinction matters enormously because policies that suppress all fire create the conditions for catastrophic fire.", "Show two videos side-by-side: a prescribed burn moving gently through an open forest floor, and a crown fire exploding through a dense forest. Ask: Are these the same process? (Yes — combustion. But the intensity and outcomes are completely different.) Why are they so different? (Fuel load.)"),
        ("Climate change is the only reason fires are getting worse", "While climate change is a significant amplifier of fire danger, a century of fire suppression is equally responsible for the current megafire crisis. Fire-suppressed forests contain 5-10 times more fuel than historical conditions, creating conditions for unprecedented fire intensity even under historical climate. Climate change and the suppression legacy are compounding factors — each makes the other worse. Addressing only climate (which takes decades) without addressing fuel loads (which can be done now through prescribed burns) leaves communities and ecosystems at extreme risk.", "Show the model comparison: run a fire in a fuel-loaded forest under historical climate conditions versus a natural-fuel forest under current climate conditions. Both produce worse fires than historical natural fires, but the fuel-loaded scenario is worse even under historical climate. Ask: Which factor matters more? (Both — they\\'re multiplicative.)"),
        ("Prescribed burns are too dangerous and should not be done", "While prescribed burns carry some risk, that risk is dramatically lower than the risk of allowing fuel to continue accumulating. Prescribed burns are conducted under carefully controlled conditions — moderate temperature, low wind, adequate humidity, and with trained crews and contingency plans. The risk of a prescribed burn escaping is approximately 1-2%, and escaped prescribed burns are typically small and easily contained. In contrast, the risk of catastrophic wildfire in fuel-loaded forests approaches certainty over time, and megafires kill people, destroy communities, and cause billions in damage. The question is not whether fire will occur, but whether it occurs under controlled conditions or uncontrolled catastrophe.", "Present the risk comparison mathematically: 1-2% risk of a prescribed burn escaping versus near-certainty of megafire without treatment. Calculate the expected damage from each scenario. The numbers make an overwhelming case for prescribed burning.")
    ]
}

L09 = {
    "id": "G12L2-L09",
    "title": "Can We Engineer the Climate?",
    "subtitle": "Modeling Geoengineering Technologies, Carbon Capture, and Ethical Dimensions",
    "ngss": "HS-ESS2-4",
    "ngss_desc": "Use a model to describe how variations in the flow of energy into and out of Earth\\'s systems result in changes in climate.",
    "big_question": "If we cannot reduce emissions fast enough to prevent catastrophic warming, should humanity deliberately intervene in Earth\\'s climate system through technologies like solar radiation management or atmospheric carbon removal — and who gets to decide for the entire planet?",
    "objectives": [
        "Model how solar radiation management and carbon dioxide removal technologies would affect Earth\\'s energy balance and climate system",
        "Explain the mechanisms, potential benefits, and risks of major geoengineering proposals including stratospheric aerosol injection and direct air capture",
        "Predict the climatic consequences of deploying and then stopping geoengineering interventions, including the termination shock problem",
        "Analyze the ethical, governance, and justice dimensions of technologies that give a few nations the power to modify the global climate"
    ],
    "vocabulary": [
        ("Solar Radiation Management", "Geoengineering techniques that reduce the amount of sunlight reaching Earth\\'s surface to counteract greenhouse warming — including stratospheric aerosol injection, marine cloud brightening, and space-based reflectors, SRM does not remove CO2 but masks its warming effect, creating a dependency that must be maintained indefinitely unless emissions are also reduced"),
        ("Carbon Dioxide Removal", "Technologies and processes that extract CO2 from the atmosphere and store it permanently — including direct air capture with carbon storage, enhanced weathering of minerals, ocean alkalinity enhancement, and bioenergy with carbon capture, CDR addresses the root cause of warming but current technologies are extremely expensive and operate at tiny scale compared to annual emissions"),
        ("Termination Shock", "The rapid and catastrophic warming that would occur if solar radiation management were suddenly stopped after years of deployment — because SRM masks warming without reducing CO2, stopping it would expose the planet to the full accumulated greenhouse effect within months, producing temperature increases of several degrees in a single decade"),
        ("Moral Hazard", "The risk that the availability of geoengineering technology reduces the urgency to cut emissions — if policymakers believe they can engineer their way out of climate change, they may delay the difficult but necessary transition away from fossil fuels, ultimately making the problem worse by increasing dependence on interventions with serious risks and side effects")
    ],
    "components": [
        ("Atmospheric CO2 Concentration", "The total amount of carbon dioxide in the atmosphere — currently 424 ppm and rising approximately 2.5 ppm per year, the fundamental driver of greenhouse warming that geoengineering either masks (SRM) or removes (CDR)", True),
        ("Solar Radiation Reaching Surface", "The amount of sunlight that passes through the atmosphere and reaches Earth\\'s surface — can be reduced by stratospheric aerosols or increased cloud reflectivity, cooling the planet without changing CO2 levels", True),
        ("Global Mean Temperature", "The average surface temperature of Earth relative to pre-industrial baseline — currently +1.2 degrees Celsius, rising approximately 0.2 degrees per decade, and the primary variable that geoengineering aims to control", False),
        ("Ocean Acidification Level", "The pH decrease in ocean water caused by dissolved CO2 — solar radiation management does not address acidification because it does not reduce atmospheric CO2, meaning coral reefs and marine organisms continue to be harmed even if temperatures are stabilized through SRM", False),
        ("Regional Climate Disruption", "The uneven and potentially harmful effects of geoengineering on regional weather patterns — stratospheric aerosol injection could reduce monsoon rainfall in South and East Asia, alter precipitation over Africa, and change tropical cyclone patterns, creating winners and losers from a single global intervention", False),
        ("Carbon Removal Rate", "The net rate at which CO2 is removed from the atmosphere by CDR technologies — currently negligible (approximately 0.01 gigatons per year) compared to annual emissions of 36 gigatons, but theoretically scalable if massive investment occurs", False),
        ("Termination Risk", "The probability and consequences of geoengineering being suddenly stopped — SRM must be maintained continuously because stopping it exposes the planet to all accumulated warming within months, creating a multigenerational commitment with no guaranteed institutional stability over centuries", False)
    ],
    "think_about_it": "If Solar Radiation Management reduces Global Mean Temperature without reducing Atmospheric CO2, what happens to Ocean Acidification? If SRM is deployed for 50 years while CO2 continues rising, what happens if it suddenly stops — what is the Termination Risk?",
    "scenarios": [
        ("SRM Deployment", "Deploy stratospheric aerosol injection sufficient to offset 1.5 degrees of warming while emissions continue — observe the effects on temperature, ocean acidification, regional climate, and termination risk over 50 years"),
        ("CDR Scale-Up", "Dramatically increase Carbon Dioxide Removal to 10 gigatons per year while maintaining current emissions — observe whether CDR can meaningfully reduce atmospheric CO2 and whether the scale is achievable"),
        ("Combined CDR Plus Emission Reduction", "Reduce emissions by 50% and deploy 5 gigatons per year of CDR — observe whether the combined approach achieves net-negative emissions and genuine climate stabilization without the risks of SRM")
    ],
    "sim_scenarios": [
        ("Solar Shield", "SRM: Active (1.5C offset) | Emissions: Continuing | CDR: None", "If we deploy a solar shield to cool the planet without reducing emissions, what happens to Ocean Acidification? What is the Termination Risk after 50 years? Is this a solution or a trap?"),
        ("Carbon Removal", "SRM: None | Emissions: Current | CDR: 10 Gt/year", "Can carbon dioxide removal at massive scale reduce atmospheric CO2 meaningfully? What does the model show about the gap between current removal capacity and the scale needed?"),
        ("Integrated Solution", "SRM: None | Emissions: -50% | CDR: 5 Gt/year", "What does the model show when emission reduction is combined with carbon removal? Is this pathway achievable without the risks of solar radiation management?")
    ],
    "discoveries": [
        "Solar Radiation Management masks warming without addressing the root cause — the model shows that while SRM can stabilize temperature, Ocean Acidification continues worsening because atmospheric CO2 is unchanged, and Termination Risk grows every year of deployment",
        "Current Carbon Dioxide Removal capacity (0.01 Gt/year) is approximately 3,600 times smaller than annual emissions (36 Gt/year) — the model reveals the enormous gap between CDR aspiration and reality that makes it a complement to emission reduction, not a substitute",
        "The termination shock problem creates a multigenerational trap — if SRM is deployed for decades while CO2 continues accumulating, stopping it would cause several degrees of warming in under a decade, an unprecedented rate of change that would devastate ecosystems and human systems",
        "The most effective and lowest-risk pathway combines aggressive emission reduction with moderate CDR deployment — this approach addresses the root cause (CO2) rather than masking symptoms (temperature), avoids termination risk, and does not create regional climate disruption"
    ],
    "answer": "Humanity can technically engineer the climate, but the question is whether we should — and the answer depends critically on which technologies we are discussing. Solar Radiation Management through stratospheric aerosol injection could cool the planet relatively quickly and cheaply, but the model reveals devastating limitations: it does not reduce CO2, so ocean acidification continues destroying marine ecosystems; it creates regional winners and losers by altering precipitation patterns; and it creates a termination trap — once deployed, it must be maintained indefinitely because stopping it would cause catastrophic rapid warming from all the CO2 that accumulated behind the solar shield. Carbon Dioxide Removal addresses the actual problem but currently operates at a scale 3,600 times too small. The model clearly shows that no geoengineering technology is a substitute for reducing emissions — at best, CDR is a complement that can help achieve net-negative emissions after the hard work of decarbonization. The governance dimension may be the most challenging: who decides to deploy technologies that alter the climate for all 8 billion people? What happens when one nation\\'s geoengineering reduces another\\'s rainfall? These are questions that science can inform but cannot answer alone.",
    "stem_title": "Design a Climate Intervention Decision Framework",
    "stem_mission": "Design a governance and evaluation framework for deciding whether, when, and how to deploy climate intervention technologies, incorporating scientific risk assessment, ethical principles, and international justice considerations.",
    "stem_scenario": "Global temperatures have reached 1.8 degrees Celsius above pre-industrial levels and emission reduction efforts are failing to meet targets. A coalition of wealthy nations is proposing to deploy stratospheric aerosol injection to prevent crossing the 2-degree threshold, arguing that the risk of inaction exceeds the risk of intervention. Developing nations in the tropics, whose monsoon rainfall could be disrupted by SRM, oppose deployment without their consent. Meanwhile, CDR technology has scaled to 2 gigatons per year — significant but still far below the level needed. The United Nations has commissioned your team to design a decision framework that evaluates whether geoengineering should be deployed and, if so, under what conditions, with what safeguards, and with whose consent.",
    "stem_questions": [
        "Based on your model, what are the specific risks of SRM deployment versus the risks of allowing temperatures to cross 2 degrees? Can you quantify both sides?",
        "What does your model show about the regional climate disruption from SRM — which regions benefit and which are harmed? How does this affect the justice of deployment?",
        "Is there a scenario in your model where SRM could be deployed temporarily while CDR scales up enough to address the root cause, or does the termination trap make temporary deployment impossible?"
    ],
    "stem_design_qs": [
        "What scientific criteria does your framework use to evaluate whether geoengineering deployment is justified?",
        "How does your framework ensure that nations most affected by side effects have genuine decision-making power, not just a voice?",
        "What safeguards does your framework include to prevent moral hazard — the risk that geoengineering availability reduces emission reduction urgency?",
        "What termination protocol does your framework require — how is the long-term commitment managed across generations and changing governments?"
    ],
    "career": "Climate scientists who model geoengineering effects on Earth systems work at NASA, NOAA, universities, and national laboratories, earning $75,000-$150,000/year. Carbon capture engineers who design and operate direct air capture and geological storage systems earn $70,000-$140,000/year. Climate policy ethicists who analyze the governance, justice, and moral dimensions of climate intervention earn $60,000-$130,000/year at universities, think tanks, and international organizations.",
    "images": {
        "cover": ("G12L2-L09-cover.png", "A photorealistic image of diverse 17-18 year old students examining climate models and geoengineering diagrams in a modern science classroom, with Earth\\'s energy balance diagram and carbon capture technology images displayed on screens"),
        "landscape": ("G12L2-L09-landscape.png", "A photorealistic image showing a futuristic carbon capture facility with large fan arrays in a desert landscape, with renewable energy installations nearby and a clear sky above, illustrating the scale of direct air capture technology"),
        "modeling": ("G12L2-L09-modeling.png", "A photorealistic image of diverse 17-18 year old students building climate intervention models on laptops, with global temperature projections and SRM versus CDR comparison charts projected on a smartboard"),
        "discussion": ("G12L2-L09-discussion.png", "A photorealistic image of a teacher facilitating a heated discussion with diverse 17-18 year old students about geoengineering ethics, with a world map showing regional climate effects and a governance framework displayed on screen"),
        "stem": ("G12L2-L09-stem.png", "A photorealistic image of diverse 17-18 year old students designing climate intervention governance frameworks on whiteboards with decision trees, risk matrices, stakeholder maps, and ethical principles")
    },
    "pre_assessment": [
        "Have you heard of geoengineering? What comes to mind when you think about humans deliberately modifying the global climate?",
        "If you could deploy a giant sunshade that cooled the planet by reflecting sunlight, but it didn\\'t remove any CO2 from the atmosphere, would you do it? Why or why not?",
        "Who should get to decide whether to deploy a technology that affects the climate for all 8 billion people on Earth? One nation? A vote? Scientists?",
        "Is it ethical to modify the climate to fix a problem caused by some nations while the side effects may harm other nations that did not cause the problem?"
    ],
    "extend_components": [
        ("Research Governance Gap", "The absence of international regulations or agreements governing geoengineering research and potential deployment — currently, any nation with sufficient resources could unilaterally deploy SRM, as no treaty prohibits it, and the lack of governance creates risks of rogue deployment or conflict"),
        ("Ozone Layer Interaction", "The potential effect of stratospheric aerosol injection on the ozone layer — sulfate aerosols that reflect sunlight also catalyze ozone-destroying reactions, potentially worsening the ozone hole and increasing UV radiation exposure, adding a health risk to the climate intervention"),
        ("Intergenerational Equity", "The ethical dimension of decisions made today that bind future generations — deploying SRM creates a commitment that must be maintained for centuries by future generations who had no voice in the decision, raising fundamental questions about whether one generation has the right to impose such obligations on its descendants")
    ],
    "reflections": [
        "Why does your model show that solar radiation management is not a solution to climate change but rather a new problem layered on top of an existing one?",
        "What is the termination shock problem and why does it make SRM deployment a multigenerational trap? How does your model demonstrate this risk?",
        "Why is the current scale of carbon dioxide removal so inadequate compared to annual emissions? What would it take to close this gap, and is it realistic?",
        "How does the moral hazard concept apply to geoengineering — why might having a technological fix available actually make the climate problem worse?",
        "Who should have the authority to make decisions about deploying technologies that alter the global climate? What principles should guide this governance?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop models of Earth\\'s energy balance to predict how geoengineering interventions would alter climate system dynamics, including unintended consequences like regional disruption and termination shock."),
        ("Disciplinary Core Idea", "ESS2.D Weather and Climate", "The greenhouse effect and energy balance of Earth are determined by atmospheric composition and solar input. Geoengineering proposals alter either the input (SRM) or the composition (CDR), with fundamentally different implications for climate system stability."),
        ("Crosscutting Concept", "Cause and Effect", "Students analyze the causal relationships between geoengineering interventions and their climate system effects, distinguishing between addressing root causes (reducing CO2) and masking symptoms (reflecting sunlight), and identifying the unintended cascading effects of each approach.")
    ],
    "cast_items": [
        "Model how solar radiation management and carbon dioxide removal differently affect Earth\\'s energy balance, ocean chemistry, and regional climate patterns",
        "Predict the consequences of deploying and stopping SRM over different timescales, including the termination shock phenomenon",
        "Evaluate competing climate intervention strategies using model evidence about effectiveness, risks, scalability, and justice implications"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A nation deploys stratospheric aerosol injection for 30 years, successfully keeping Global Mean Temperature stable at 1.5 degrees above pre-industrial. During this time, atmospheric CO2 has risen from 424 to 550 ppm. What would happen if the aerosol injection were suddenly stopped? A) Temperature would remain stable because the climate has adapted B) Temperature would gradually increase over 50 years to the level expected at 550 ppm C) Temperature would rapidly increase by several degrees within a decade as the full greenhouse effect of 550 ppm is unmasked D) The ocean would absorb the excess CO2 and prevent warming"),
        ("Constructed Response:", "Using your climate intervention model, compare the long-term climate outcomes of two strategies: (1) deploying SRM while continuing current emissions, and (2) reducing emissions by 50% while deploying 5 Gt/year of CDR. Reference at least four model components including Ocean Acidification, Termination Risk, and Carbon Removal Rate in your analysis of why these strategies produce fundamentally different outcomes.")
    ],
    "background_intro": "As the gap between climate targets and actual emission reductions widens, attention is increasingly turning to geoengineering — deliberate large-scale interventions in Earth\\'s climate system. These proposals range from reflecting sunlight back to space to pulling CO2 directly from the atmosphere. The technologies are fascinating, controversial, and fraught with risks and ethical dilemmas that go far beyond the science. Understanding geoengineering is essential for every scientifically literate citizen because these decisions may define the 21st century.",
    "background_sections": [
        ("Solar Radiation Management: The Sunshade Approach", "SRM techniques aim to reduce the amount of sunlight reaching Earth\\'s surface. The most discussed approach is stratospheric aerosol injection (SAI) — releasing reflective sulfate particles into the upper atmosphere that scatter incoming sunlight, mimicking the cooling effect of large volcanic eruptions. Mount Pinatubo\\'s 1991 eruption injected 20 million tons of sulfur dioxide into the stratosphere and cooled the planet by approximately 0.5 degrees Celsius for two years. SAI would replicate this effect continuously using a fleet of high-altitude aircraft. Cost estimates are surprisingly low — $2-10 billion per year to offset 1-2 degrees of warming. But SRM does not remove CO2: it masks warming while the root cause continues worsening, like taking painkillers without treating an infection."),
        ("Carbon Dioxide Removal: Addressing the Root Cause", "CDR technologies extract CO2 from the atmosphere and store it permanently. Direct Air Capture (DAC) uses chemical processes to bind CO2 from ambient air, then compresses and injects it underground into geological formations. The technology works — Climeworks in Iceland operates the world\\'s largest DAC plant, removing 36,000 tons of CO2 per year. But the scale challenge is staggering: annual emissions are 36 billion tons, meaning current DAC removes 0.001% of annual emissions. Scaling to 10 billion tons per year would require thousands of facilities, enormous energy input (potentially dedicated renewable farms), and trillions of dollars in investment. Enhanced weathering — accelerating the natural process by which minerals absorb CO2 — and ocean alkalinity enhancement offer potentially cheaper paths but face ecological uncertainty. CDR addresses the fundamental problem but cannot operate at meaningful scale for decades."),
        ("The Termination Problem: A Multigenerational Trap", "The most dangerous aspect of SRM is what happens when it stops. While SRM is deployed, CO2 continues accumulating in the atmosphere. If SRM masks 2 degrees of warming for 50 years, stopping it would expose the planet to the full warming effect of all the CO2 that accumulated behind the solar shield — a rapid temperature increase of several degrees within a decade, far faster than any natural climate change. This rate of change would be catastrophic for ecosystems and agriculture. Termination shock means SRM creates a commitment that must be maintained for centuries — until CO2 levels are naturally or artificially reduced to safe levels. But maintaining a global technological system for centuries requires institutional stability that no human civilization has ever demonstrated. Wars, economic crises, pandemics, or political changes could interrupt deployment with devastating consequences."),
        ("Governance and Justice: Who Decides for the Planet?", "Perhaps the most challenging dimension of geoengineering is governance. SRM affects the entire planet but would be deployed by a few nations — potentially just one. Regional effects would not be evenly distributed: models suggest SAI could reduce monsoon rainfall in South and East Asia, affecting the food production of billions. Nations that benefit from deployment may differ from those that suffer its side effects, creating a new dimension of climate inequity. Currently, no international treaty governs geoengineering, and no consensus exists on whether research, testing, or deployment should proceed. The moral hazard concern adds urgency: if geoengineering makes climate change seem less threatening, governments may reduce efforts to cut emissions, ultimately making the underlying problem worse while adding the new risks of intervention.")
    ],
    "lever_L": "Students identify Atmospheric CO2, Solar Radiation Reaching Surface, Global Mean Temperature, Ocean Acidification Level, Regional Climate Disruption, Carbon Removal Rate, and Termination Risk as key components of the climate intervention system.",
    "lever_E": "Students determine that SRM reduces temperature without addressing CO2 or acidification, that CDR addresses the root cause but at inadequate scale, that SRM creates growing termination risk over time, and that only emission reduction combined with CDR achieves genuine climate stabilization.",
    "lever_V": "Students build a computational model comparing how SRM and CDR differently affect Earth\\'s energy balance, ocean chemistry, and long-term climate stability, revealing the fundamental asymmetry between masking symptoms and treating causes.",
    "lever_Ev": "Students run SRM deployment, CDR scale-up, and combined emission reduction with CDR scenarios to test predictions about effectiveness, risks, and the conditions for genuine climate stabilization.",
    "lever_R": "Students add research governance gaps, ozone layer interactions, or intergenerational equity to explore how additional dimensions affect the risk-benefit calculus and governance requirements of geoengineering.",
    "slides_guide": [
        {
            "num": "Slide 1",
            "title": "Cover",
            "visual": "Title slide with provocative image juxtaposing climate engineering concepts — stratospheric aerosol injection, carbon capture, and Earth from space",
            "say": "Can we engineer the climate? The technology exists. The question is: should we? Today we model the science and confront the ethics.",
            "do": "Show cover image. Quick poll: If you could push a button that cooled the planet but didn\\'t remove any CO2, would you push it? Take responses and reasoning — revisit after modeling.",
            "time": "2 min"
        },
        {
            "num": "Slide 2",
            "title": "Learning Objectives",
            "visual": "Four learning objectives with geoengineering vocabulary and comparison diagrams of SRM versus CDR",
            "say": "Today is as much about ethics and governance as it is about science. We\\'re modeling technologies that could save the planet — or create new disasters.",
            "do": "Have students read objectives. Pre-teach vocabulary. Key distinction: SRM masks symptoms without treating the disease. CDR treats the disease but at tiny scale. This distinction will drive everything.",
            "time": "3 min"
        },
        {
            "num": "Slide 3",
            "title": "Big Question",
            "visual": "Provocative question displayed over split image of climate emergency versus geoengineering risks",
            "say": "Who gets to decide to modify the climate for 8 billion people? What if the intervention helps some nations but harms others? Write your initial position.",
            "do": "Quick-write: Students write whether they think geoengineering should be pursued and why. Save for comparison — many positions will shift after modeling the termination problem.",
            "time": "3 min"
        },
        {
            "num": "Slide 4",
            "title": "LEVER Framework",
            "visual": "LEVER steps with climate intervention examples",
            "say": "We\\'ll build a model that compares two fundamentally different approaches to the climate crisis. One treats the symptom. One treats the cause. The model will reveal why this difference matters enormously.",
            "do": "Preview LEVER steps. Emphasize: this model will reveal a trap — a situation where the seeming solution creates a new and potentially worse problem.",
            "time": "2 min"
        },
        {
            "num": "Slide 5",
            "title": "Activity 1: Components",
            "visual": "Seven component cards for sorting with climate system illustrations",
            "say": "Which components are external inputs we can control, and which are system responses? Think about what we can manipulate versus what the Earth system does in response.",
            "do": "Guide sorting: External = Atmospheric CO2 (emissions + CDR), Solar Radiation Reaching Surface (SRM can modify). Internal = the five climate system responses. Discuss: Why is Termination Risk internal? It\\'s a consequence of deployment decisions, not a controllable input.",
            "time": "8 min"
        },
        {
            "num": "Slide 6",
            "title": "Activity 2: Connections",
            "visual": "Relationship diagram contrasting SRM and CDR pathways through the climate system",
            "say": "Draw two pathways: SRM reduces solar radiation but doesn\\'t touch CO2 — what happens to Ocean Acidification and Termination Risk? CDR reduces CO2 directly — how does this differ?",
            "do": "Students draw arrows for both intervention types. Key discovery: SRM creates a dangerous divergence — temperature goes down but CO2, acidification, and termination risk go up. CDR aligns everything in the right direction but at tiny scale. Ask: Which is actually safer?",
            "time": "8 min"
        },
        {
            "num": "Slide 7",
            "title": "Activity 3: Simulation",
            "visual": "Simulation showing three scenarios with temperature, CO2, ocean pH, and termination risk graphs",
            "say": "Run all three scenarios. The SRM scenario may look good at first — but watch what happens to Ocean Acidification and Termination Risk as the years pass. This is the trap.",
            "do": "Students run scenarios. Key discussion: In the SRM scenario, temperature stabilizes — but everything else gets worse. After 50 years, termination would cause catastrophic rapid warming. Ask: Is this a solution or a different kind of catastrophe?",
            "time": "10 min"
        },
        {
            "num": "Slide 8",
            "title": "Discoveries",
            "visual": "Four key discoveries contrasting SRM trap with CDR inadequacy and the combined approach",
            "say": "Our model reveals a fundamental truth: there is no shortcut past emission reduction. SRM is a trap that makes the underlying problem worse. CDR is real but tiny. The only genuine solution is reducing emissions.",
            "do": "Class discussion. Revisit initial poll: Has anyone changed their position on whether to push the button? Why? The termination problem and ocean acidification should have changed perspectives.",
            "time": "5 min"
        },
        {
            "num": "Slide 9",
            "title": "STEM Challenge",
            "visual": "Governance challenge: Design a decision framework for whether to deploy climate intervention technologies",
            "say": "The UN has asked your team to design the framework for deciding whether geoengineering should be deployed. This is about governance, justice, and science together. Who decides, and how?",
            "do": "Groups design governance frameworks incorporating scientific risk criteria, consent mechanisms, equity principles, and termination protocols. Present and debate frameworks, addressing challenges from other groups.",
            "time": "12 min"
        }
    ],
    "sort_reasoning": "Atmospheric CO2 Concentration and Solar Radiation Reaching Surface are external components because they represent the two variables that geoengineering aims to manipulate — CDR reduces CO2 while SRM reduces incoming solar radiation. Global Mean Temperature, Ocean Acidification Level, Regional Climate Disruption, Carbon Removal Rate, and Termination Risk are internal because they are responses of the climate system and human system to these interventions — they represent the consequences (intended and unintended) of deploying geoengineering technologies.",
    "relationships": [
        ("Atmospheric CO2 Concentration to Global Mean Temperature", "POSITIVE (+)", "Higher atmospheric CO2 strengthens the greenhouse effect, trapping more outgoing radiation and increasing global temperature. This is the fundamental mechanism of climate change that CDR addresses directly."),
        ("Solar Radiation Reaching Surface to Global Mean Temperature", "POSITIVE (+)", "More solar radiation reaching the surface increases energy input and temperature. SRM reduces this input, counteracting greenhouse warming — but only the temperature effect, not the chemical effects of elevated CO2."),
        ("Atmospheric CO2 Concentration to Ocean Acidification Level", "POSITIVE (+)", "Higher atmospheric CO2 increases the amount dissolved in oceans, forming carbonic acid and reducing pH. SRM does not affect this pathway because it does not reduce CO2 — acidification continues regardless of SRM deployment."),
        ("Solar Radiation Reaching Surface to Regional Climate Disruption", "POSITIVE (+)", "Reducing solar input unevenly across the planet — as SRM does — alters temperature gradients that drive weather patterns, potentially disrupting monsoons, shifting precipitation belts, and changing storm tracks."),
        ("Atmospheric CO2 Concentration to Termination Risk", "POSITIVE (+)", "Higher CO2 behind the SRM shield means greater warming exposure if SRM stops. Termination Risk grows every year that SRM masks accumulating CO2, creating an increasingly dangerous dependency.")
    ],
    "sim_answers": [
        ("SRM Deployment", "SRM successfully reduces Global Mean Temperature to target levels, appearing to solve the warming problem. However, the model reveals critical failures: Ocean Acidification continues worsening because atmospheric CO2 is unchanged — coral reefs and marine ecosystems continue deteriorating. Regional Climate Disruption shows altered precipitation patterns, particularly reduced monsoon rainfall in South Asia. Most dangerously, Termination Risk grows steadily: after 50 years, stopping SRM would cause approximately 3-4 degrees of warming in under a decade as the full greenhouse effect of 550+ ppm CO2 is unmasked. The solar shield creates a multigenerational trap."),
        ("CDR Scale-Up", "Deploying 10 Gt/year of CDR while maintaining current emissions (36 Gt/year) reduces net emissions to 26 Gt/year — a significant improvement but still net-positive emissions. Atmospheric CO2 continues rising, though more slowly. Temperature increase slows but does not stop. The model demonstrates that CDR at even massive scale cannot compensate for continued full emissions — it reduces the rate of accumulation but does not reverse it. CDR is effective only as a complement to emission reduction, not a substitute."),
        ("Combined Strategy", "Reducing emissions by 50% (to 18 Gt/year) while deploying 5 Gt/year of CDR achieves net emissions of 13 Gt/year — a dramatic reduction that begins slowing temperature increase significantly. If CDR scales further while emissions continue declining, the model shows a pathway to net-negative emissions and eventual atmospheric CO2 reduction. This is the only scenario that addresses both temperature and ocean acidification, creates no termination risk, and moves toward genuine climate stabilization. It is also the hardest politically because it requires transforming the entire energy and industrial system.")
    ],
    "reflection_exemplars": [
        ("Why is SRM a trap rather than a solution?", "Our model reveals that SRM creates a dangerous divergence between the visible symptom (temperature) and the invisible root cause (CO2). While temperature stabilizes behind the solar shield, CO2 continues accumulating in the atmosphere and dissolving in the oceans. Ocean Acidification worsens steadily, threatening 25% of marine species regardless of temperature management. And every year of deployment, Termination Risk grows — the gap between the masked temperature and the actual temperature that would exist without the shield widens. After 50 years of SRM with continued emissions, stopping it would cause warming of several degrees in under a decade — faster than any natural climate change in Earth\\'s history. The model shows that SRM does not solve climate change; it trades a slow crisis for dependence on a system that, if interrupted, produces a fast catastrophe."),
        ("Who should decide whether to deploy geoengineering?", "This question cannot be answered by science alone — it requires ethical, political, and justice reasoning informed by scientific evidence. Our model shows that SRM creates regional winners and losers: reduced monsoon rainfall in South Asia could affect food production for billions of people who contributed minimally to the emissions causing climate change. A governance framework must therefore ensure that affected populations have genuine decision-making authority, not just consultation. The moral hazard problem adds another dimension: if geoengineering reduces political urgency for emission cuts, the total risk to humanity could increase rather than decrease. Any governance framework must include binding commitments to continue emission reduction alongside any intervention, and must address the intergenerational dimension — the commitment to maintain SRM for centuries cannot ethically be imposed on future generations without their consent.")
    ],
    "stem_intro": "Present the challenge: The UN Security Council has called an emergency session as temperatures approach 2 degrees. A coalition proposes immediate SRM deployment. Developing nations in the tropics oppose it. CDR exists but is too small. Your team designs the decision framework: Under what conditions is deployment justified? Who must consent? What safeguards prevent moral hazard and termination? How are affected nations compensated? Use model data to support every recommendation.",
    "stem_concepts": [
        ("Risk-Risk Tradeoffs", "Geoengineering decisions involve comparing the risks of action against the risks of inaction — neither option is risk-free. The risk of deploying SRM includes regional climate disruption, ocean acidification continuation, and termination dependence. The risk of not deploying SRM includes continued warming past 2 degrees with increasing extreme weather, sea level rise, and ecosystem collapse. Effective governance requires transparent, quantitative comparison of both risk profiles."),
        ("Consent and Legitimacy in Global Governance", "Any technology that affects all nations requires governance mechanisms with broad legitimacy. Unilateral deployment by one nation would lack legitimacy and could provoke geopolitical conflict. The closest existing models are the Montreal Protocol (ozone layer) and the Paris Agreement (emissions), but neither fully addresses the unique challenges of geoengineering — particularly the asymmetric distribution of effects and the multigenerational commitment."),
        ("Precautionary Principle vs. Proportionality", "The precautionary principle suggests that uncertain technologies should not be deployed until risks are fully understood. The proportionality principle suggests that the response should be proportional to the threat — and climate change is an existential threat. These principles can conflict when the risk of inaction (continued warming) competes with the risk of action (geoengineering side effects). Navigating this tension requires clear criteria for when the threshold of action is met.")
    ],
    "stem_eval": [
        ("Expert (4)", "Framework specifies scientific risk criteria, consent mechanisms including affected nations, moral hazard safeguards tied to emission reduction commitments, termination protocols, and compensation mechanisms for harmed regions — all justified by model evidence about SRM risks and CDR limitations"),
        ("Proficient (3)", "Framework addresses major governance challenges with reasonable criteria and some connection to model data about risks and benefits"),
        ("Developing (2)", "Framework addresses some governance issues but lacks scientific risk criteria or does not account for regional effects and justice dimensions"),
        ("Beginning (1)", "Framework is incomplete, does not account for termination risk or moral hazard, or ignores the justice dimensions of unilateral deployment")
    ],
    "support": [
        "Provide a comparison table with two columns: SRM (what it does, what it doesn\\'t do, risks) and CDR (what it does, what it doesn\\'t do, limitations) — students can see at a glance why these approaches are fundamentally different",
        "Use the painkiller analogy: SRM is like taking painkillers for a broken bone — you feel better but the bone is still broken and getting worse. CDR is like actually healing the bone, but it takes a long time. What\\'s the best strategy?",
        "Sentence frames: \\'SRM reduces ___ but does not address ___, creating the risk of ___. CDR addresses ___ directly but at a scale of only ___ compared to the ___ needed. The safest approach is ___ because the model shows ___.\\'"
    ],
    "extensions": [
        "Research the actual governance proposals for geoengineering — compare the Oxford Principles, the Carnegie Climate Governance Initiative recommendations, and proposals from the Solar Radiation Management Governance Initiative. Evaluate which framework best addresses the risks your model identified.",
        "Calculate the cost and energy requirements of scaling direct air capture to 10 gigatons per year — how many Climeworks-scale facilities would be needed, how much energy would they consume, and how does this compare to current global energy production?",
        "Investigate the historical precedent of the Montreal Protocol as a model for geoengineering governance — how did nations agree to phase out ozone-depleting chemicals, what enforcement mechanisms were used, and what lessons apply to governing climate intervention technologies?"
    ],
    "cross_curr": [
        ("Math", "Model the termination shock mathematically: if SRM masks 2 degrees of warming for 50 years while CO2 rises from 424 to 560 ppm, calculate the rate of warming if SRM is stopped and the atmosphere returns to equilibrium in 10 years. Compare this rate to the fastest natural warming in the geological record."),
        ("ELA", "Read Kim Stanley Robinson\\'s novel The Ministry for the Future (excerpt) alongside a scientific paper on SRM governance. Write a comparative essay evaluating how fiction and science differently explore the ethical dimensions of geoengineering and which medium is more effective at communicating the stakes."),
        ("History", "Research the history of failed large-scale environmental interventions — the introduction of cane toads in Australia, the Soviet diversion of the Aral Sea, or the use of DDT — as case studies of unintended consequences from well-intentioned environmental manipulation. What patterns emerge, and how do they inform the geoengineering debate?")
    ],
    "misconceptions": [
        ("Geoengineering can solve climate change without reducing emissions", "Both SRM and CDR have fundamental limitations that make them supplements to, not substitutes for, emission reduction. SRM masks warming without addressing CO2, meaning ocean acidification continues and termination risk grows indefinitely. CDR operates at a scale roughly 3,600 times too small and would take decades and trillions of dollars to scale meaningfully. The model clearly shows that the only pathway to genuine climate stabilization requires aggressive emission reduction as the primary strategy, with CDR as a complement. Geoengineering without decarbonization is like pumping water out of a sinking boat without plugging the hole.", "Run the model: show what happens in each scenario. The SRM-without-reduction scenario shows growing termination risk and worsening acidification. The CDR-without-reduction scenario shows inadequate scale. Only the combined emission reduction plus CDR scenario achieves stabilization. Ask: Which approach actually solves the problem?"),
        ("Solar radiation management is safe because volcanic eruptions have the same effect naturally", "While SRM mimics the cooling effect of volcanic eruptions, there are critical differences. Volcanic cooling is temporary (1-2 years) and uncontrolled; SRM would need to be continuous and sustained for centuries. Volcanic eruptions do cause regional climate disruption — Pinatubo\\'s eruption significantly reduced monsoon rainfall and caused crop failures in some regions. Sustaining that effect indefinitely would compound regional impacts year after year rather than allowing recovery. And volcanic eruptions do not create termination risk because the cooling fades naturally; SRM termination would expose decades of accumulated warming instantly.", "Present the comparison: Pinatubo cooled the planet 0.5 degrees for 2 years, then conditions returned to normal. SRM would cool the planet continuously — but what happens when it stops after 50 years of CO2 accumulation? The volcanic analogy breaks down completely at the scale of sustained, decades-long deployment."),
        ("Carbon capture is too expensive and will never work at scale", "While current CDR costs are high ($250-600 per ton of CO2 for direct air capture), costs are declining rapidly — similar to the trajectory of solar panels, which fell 99.7% from their initial cost. Enhanced weathering and ocean alkalinity enhancement offer potentially cheaper pathways. The more accurate critique is that CDR at the scale needed (10+ Gt/year) requires enormous investment and decades to build — making it a long-term tool rather than an immediate solution. This does not mean CDR will never work; it means we cannot wait for it and must reduce emissions now while building CDR capacity for the future.", "Show the solar panel cost curve as an analogy: technology that was impossibly expensive in 1977 is now the cheapest electricity source. DAC is on a similar trajectory. The question is not whether it will become affordable but whether it can scale fast enough to matter — and the model shows it is a complement to, not a substitute for, emission reduction.")
    ]
}

L10 = {
    "id": "G12L2-L10",
    "title": "Why Do Environmental Inequities Exist?",
    "subtitle": "Modeling Pollution Exposure Disparities, Environmental Justice, and Systemic Solutions",
    "ngss": "HS-ESS3-3",
    "ngss_desc": "Create a computational simulation to illustrate the relationships among the management of natural resources, the sustainability of human populations, and biodiversity.",
    "big_question": "If clean air and clean water are basic human needs, why do low-income communities and communities of color consistently bear the greatest burden of pollution, toxic waste, and environmental hazards — and what systemic forces created and maintain these patterns of environmental inequity?",
    "objectives": [
        "Model how pollution source placement, housing policy, economic factors, and regulatory enforcement interact to create and maintain environmental exposure disparities across communities",
        "Explain the systemic mechanisms — including historical zoning, industrial siting, and differential enforcement — that concentrate environmental hazards in disadvantaged communities",
        "Predict how changes in policy, enforcement, and community empowerment affect the distribution of environmental burdens and benefits across populations",
        "Analyze environmental justice solutions that address root causes of inequitable exposure rather than just treating symptoms"
    ],
    "vocabulary": [
        ("Environmental Justice", "The principle that all people, regardless of race, income, or national origin, deserve equal protection from environmental hazards and equal access to environmental benefits — a framework that recognizes environmental inequity is not random but the result of systemic policies and power imbalances that can be identified and corrected"),
        ("Cumulative Impact", "The total environmental and health burden on a community from all combined sources — a community may face air pollution from highways, toxic contamination from industrial facilities, lead in water pipes, and lack of green space simultaneously, with the combined health effect far exceeding the sum of individual exposures"),
        ("Sacrifice Zone", "An area subjected to extreme environmental degradation for the economic benefit of others — communities living near refineries, chemical plants, waste incinerators, and toxic dumps that absorb pollution so other communities can enjoy the products without the health consequences"),
        ("Environmental Regulatory Gap", "The disparity in environmental monitoring, enforcement, and cleanup between wealthy and disadvantaged communities — studies show that polluters in low-income communities and communities of color face fewer inspections, lower penalties for violations, and slower cleanup timelines than polluters in affluent areas")
    ],
    "components": [
        ("Pollution Source Density", "The concentration of industrial facilities, highways, waste treatment plants, and other pollution sources in a geographic area — determined by historical zoning decisions, land costs, and political power, with pollution sources disproportionately sited in communities with less political influence", True),
        ("Community Socioeconomic Status", "The average income, wealth, education, and political power of a community\\'s residents — lower socioeconomic status is consistently associated with higher pollution exposure because land is cheaper near pollution sources and because disadvantaged communities have less political power to prevent hazardous facility siting", True),
        ("Pollution Exposure Level", "The actual concentration of pollutants — including particulate matter, toxic chemicals, lead, and noise — that community residents breathe, drink, and are exposed to daily, determined by the density of nearby pollution sources and the regulatory environment", False),
        ("Health Outcome Disparity", "The difference in disease rates between communities with high versus low pollution exposure — communities with greater environmental burden experience higher rates of asthma, cancer, cardiovascular disease, premature birth, and reduced life expectancy, with these health impacts compounding existing socioeconomic disadvantages", False),
        ("Regulatory Enforcement Level", "The frequency and rigor of environmental inspections, violation penalties, and cleanup actions in a community — enforcement varies dramatically by neighborhood, with facilities in disadvantaged communities facing less oversight and lower consequences for environmental violations", False),
        ("Community Political Power", "The ability of residents to influence zoning decisions, oppose unwanted facilities, demand environmental enforcement, and participate in policy-making — wealthier communities exercise greater political power to prevent pollution siting and demand cleanup, while disadvantaged communities face barriers to effective participation", False),
        ("Green Infrastructure Access", "The availability of parks, tree canopy, clean water systems, and healthy food options in a community — green infrastructure provides both environmental benefits (air filtration, temperature reduction, stormwater management) and health benefits (physical activity, mental health, heat refuge), and its distribution mirrors the inequitable distribution of pollution", False)
    ],
    "think_about_it": "When Pollution Source Density is high in a low-income community with weak Regulatory Enforcement and low Community Political Power, what feedback loops maintain or worsen the environmental inequity? If health impacts reduce economic opportunity, how does this create a cycle that is difficult to escape?",
    "scenarios": [
        ("Current Inequitable Distribution", "Model the existing pattern where Pollution Source Density is high in low-income communities with low Regulatory Enforcement — observe the resulting health disparities and feedback loops that maintain the pattern"),
        ("Equal Enforcement Scenario", "Increase Regulatory Enforcement Level to equal intensity across all communities — observe whether equal enforcement alone can reduce pollution exposure disparities or whether structural factors maintain the inequity"),
        ("Environmental Justice Transformation", "Combine equal enforcement with increased Community Political Power, pollution source reduction in overburdened areas, and green infrastructure investment — observe whether a comprehensive approach can reverse decades of accumulated environmental inequity")
    ],
    "sim_scenarios": [
        ("Status Quo", "Pollution Sources: Concentrated in Low-Income Areas | Enforcement: Weak in Low-Income Areas | Political Power: Correlated with Income", "What does the model predict about health outcome disparities under current conditions? How do feedback loops prevent disadvantaged communities from escaping the pollution burden?"),
        ("Equal Enforcement", "Pollution Sources: Existing Distribution | Enforcement: Equal Across All Areas | Political Power: Current", "If environmental regulations were enforced equally in all communities, would pollution exposure disparities decrease? Or are there structural factors that maintain inequity even with equal enforcement?"),
        ("Systemic Transformation", "Pollution Sources: Reduced in Overburdened Areas | Enforcement: Equal + Enhanced | Political Power: Equalized | Green Infrastructure: Invested", "What happens when you address multiple drivers simultaneously? Can a comprehensive approach reverse environmental inequity, and how long does the model show it takes?")
    ],
    "discoveries": [
        "Environmental inequity is maintained by feedback loops — health impacts from pollution reduce economic opportunity, which reduces political power, which reduces regulatory enforcement, which allows more pollution, creating a self-reinforcing cycle that concentrations of disadvantage without external intervention",
        "Equal enforcement alone is insufficient to reverse environmental inequity because the physical pollution sources remain concentrated in disadvantaged communities — equal enforcement reduces ongoing violations but does not relocate existing facilities or address cumulative historical contamination",
        "Community Political Power is the strongest leverage point in the model — when communities gain genuine decision-making authority over facility siting, zoning, and enforcement priorities, they can prevent new pollution sources and demand cleanup of existing ones, breaking the feedback loop at its most effective point",
        "The most effective intervention is comprehensive — combining pollution source reduction, equal enforcement, community empowerment, and green infrastructure investment produces dramatically larger improvements than any single intervention, because it addresses multiple feedback loops simultaneously"
    ],
    "answer": "Environmental inequities exist because of systematic patterns — not random chance. The model reveals how historical zoning decisions, industrial siting practices, housing policies, and differential regulatory enforcement have concentrated pollution sources in low-income communities and communities of color over decades. These disparities are maintained by feedback loops: pollution degrades health, which reduces economic opportunity, which reduces political power, which reduces environmental enforcement, which allows continued pollution. The result is that zip code is a stronger predictor of environmental health risk than personal behavior — communities in sacrifice zones near refineries, highways, and waste facilities have life expectancies 10-20 years shorter than affluent neighborhoods just miles away. Equal enforcement alone cannot solve this because it does not address the accumulated physical infrastructure of pollution or the power imbalances that created it. The model shows that genuine environmental justice requires a comprehensive approach: reducing pollution sources in overburdened communities, equalizing enforcement, building community political power to prevent future inequity, and investing in green infrastructure that provides the environmental benefits these communities have been denied. The most powerful lever is community empowerment — when affected communities have genuine decision-making authority, they can break the cycle at its root.",
    "stem_title": "Design an Environmental Justice Action Plan",
    "stem_mission": "Design a comprehensive environmental justice plan for an overburdened community that addresses pollution reduction, health disparities, community empowerment, and equitable development using your model evidence about systemic drivers of environmental inequity.",
    "stem_scenario": "An urban neighborhood of 30,000 people — 85% low-income, 92% people of color — is surrounded by a petroleum refinery, two chemical plants, a major highway interchange, and a waste transfer station. Asthma rates are 4 times the national average, cancer rates are elevated, and life expectancy is 12 years shorter than the affluent suburb 5 miles away. Environmental violations by nearby facilities are rarely enforced. Residents have organized a community environmental justice group and secured a $50 million investment from the state. Your team must design a plan that uses this investment to achieve maximum environmental and health improvement, addressing both immediate pollution exposure and the systemic factors that created the inequity.",
    "stem_questions": [
        "Based on your model, which feedback loops most strongly maintain environmental inequity in this community, and which interventions would most effectively break them?",
        "What does your model suggest about the relative effectiveness of pollution source reduction versus health treatment versus community empowerment for this community?",
        "How should the $50 million investment be allocated across immediate pollution reduction, health services, community organizing, and long-term structural change?"
    ],
    "stem_design_qs": [
        "What specific pollution reduction measures does your plan implement for each source (refinery, chemical plants, highway, waste station), and what exposure reduction do you project?",
        "How does your plan build permanent community political power to prevent future environmental inequity — not just address the current situation?",
        "What green infrastructure investments does your plan include, and how do they address both environmental quality and community health?",
        "How does your plan ensure that environmental improvements do not trigger gentrification that displaces the community members who fought for and deserve the benefits?"
    ],
    "career": "Environmental justice advocates and community organizers who fight for equitable environmental protection work for grassroots organizations, legal aid societies, and government agencies, earning $45,000-$95,000/year. Environmental health scientists who study the relationship between pollution exposure and health outcomes in affected communities earn $60,000-$125,000/year. Environmental lawyers who bring legal action against polluters and advocate for regulatory reform earn $65,000-$160,000/year at public interest firms, government agencies, and private practice.",
    "images": {
        "cover": ("G12L2-L10-cover.png", "A photorealistic image of diverse 17-18 year old students examining community environmental data on laptops and printed maps in a modern classroom, with environmental justice data visualizations showing pollution exposure by neighborhood displayed on screens"),
        "landscape": ("G12L2-L10-landscape.png", "A photorealistic aerial image showing the contrast between an industrial zone with visible smokestacks and highways adjacent to a residential neighborhood, and a lush green affluent suburb with parks and tree-lined streets just miles away"),
        "modeling": ("G12L2-L10-modeling.png", "A photorealistic image of diverse 17-18 year old students building environmental justice models on their laptops, with community health data and pollution maps projected on a smartboard, intense concentration and collaboration"),
        "discussion": ("G12L2-L10-discussion.png", "A photorealistic image of a teacher facilitating a passionate discussion with diverse 17-18 year old students about environmental justice, with a map showing pollution sources overlaid with demographic data displayed on screen"),
        "stem": ("G12L2-L10-stem.png", "A photorealistic image of diverse 17-18 year old students designing environmental justice action plans on poster boards with community maps, budget allocations, timeline charts, and empowerment strategies")
    },
    "pre_assessment": [
        "Do you think all communities in your city or region have the same air quality, water quality, and access to green space? Why or why not?",
        "Why do you think pollution sources like factories, highways, and waste facilities tend to be located in certain neighborhoods rather than others? What determines where they are placed?",
        "What does the term environmental justice mean to you? Can you give an example of environmental injustice?",
        "If a community has higher pollution and worse health outcomes than average, whose responsibility is it to fix the problem — the community itself, the polluting companies, or the government?"
    ],
    "extend_components": [
        ("Historical Zoning and Redlining Legacy", "The lasting impact of discriminatory zoning and lending practices from the 20th century — neighborhoods that were redlined by the Home Owners\\' Loan Corporation in the 1930s are, on average, 5 degrees Fahrenheit hotter, have significantly less tree canopy, and host more pollution sources today than neighborhoods that were rated favorably, demonstrating how historical policy created lasting environmental inequity"),
        ("Green Gentrification Risk", "The paradoxical process by which environmental improvements in disadvantaged communities increase property values and attract wealthier residents, displacing the original community members who fought for and deserve the benefits — anti-displacement policies like community land trusts and right-to-return provisions are essential safeguards"),
        ("Cumulative Impact Screening Tools", "Data platforms like CalEnviroScreen and EJScreen that map the combined environmental, health, and socioeconomic burdens on communities — these tools enable data-driven identification of the most overburdened communities and provide the evidence base for targeted investment and enforcement")
    ],
    "reflections": [
        "How does your model demonstrate that environmental inequity is the result of systemic patterns rather than random chance? What specific feedback loops maintain the disparity?",
        "Why did your model show that equal enforcement alone is insufficient to achieve environmental justice? What structural factors persist even with equal enforcement?",
        "What makes Community Political Power the strongest leverage point in your model? How does empowerment break feedback loops that other interventions do not address?",
        "How does the concept of cumulative impact explain why a community surrounded by multiple pollution sources faces health effects far worse than what any single source would cause?",
        "What is the green gentrification problem, and how can environmental justice plans prevent environmental improvements from displacing the communities they are meant to benefit?"
    ],
    "dimensions": [
        ("Science Practice", "Constructing Explanations and Designing Solutions", "Students construct evidence-based explanations for environmental inequity patterns using their computational models, and design comprehensive solutions that address systemic drivers rather than individual symptoms."),
        ("Disciplinary Core Idea", "ESS3.C Human Impacts on Earth Systems", "The sustainability of human societies depends on the equitable management of natural resources and environmental quality. When environmental burdens are disproportionately concentrated in specific communities, it undermines both social stability and the principles of sustainable development."),
        ("Crosscutting Concept", "Systems and System Models", "Students model environmental inequity as a complex system with feedback loops that maintain disparities, understanding that effective solutions must address multiple system components simultaneously rather than treating individual symptoms in isolation.")
    ],
    "cast_items": [
        "Model how pollution source siting, regulatory enforcement, community power, and health outcomes interact to create and maintain environmental exposure disparities",
        "Predict how different policy interventions — equal enforcement, community empowerment, pollution reduction — affect the distribution of environmental burdens across communities",
        "Design comprehensive environmental justice solutions that address systemic feedback loops rather than individual symptoms"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A low-income community has 5 times more pollution sources per square mile than the nearby affluent suburb. The state implements equal environmental enforcement across all communities. Based on your model, what is the most likely outcome? A) Pollution exposure becomes equal across communities within 5 years B) Ongoing violations decrease but overall exposure remains higher because existing facilities stay in place C) The affluent community\\'s pollution increases to match D) The low-income community gains political power automatically"),
        ("Constructed Response:", "Using your environmental justice model, explain why a community surrounded by a refinery, chemical plants, a highway, and a waste station experiences health impacts far greater than what any single pollution source would cause. Use the concept of cumulative impact and reference at least three model components including the feedback loops that maintain the disparity.")
    ],
    "background_intro": "Environmental justice research has consistently demonstrated that environmental hazards are not randomly distributed across communities. Low-income communities and communities of color bear disproportionate burdens of pollution, toxic contamination, and environmental degradation — a pattern that holds across every region, every city, and nearly every country studied. This is not coincidence but the predictable result of systemic forces that can be identified, modeled, and ultimately changed.",
    "background_sections": [
        ("The Data: Environmental Inequity by the Numbers", "The evidence for environmental inequity is overwhelming and consistent. A landmark 2018 EPA study found that Black Americans are exposed to 54% more particulate matter pollution from industrial sources than the overall population. A 2021 study in Science found that communities of color breathe 56% more pollution from fine particulate matter than they produce through their consumption. Superfund toxic waste sites are disproportionately located in communities of color. Residents within 3 miles of a hazardous waste facility have income levels 15-25% below the national average. In Los Angeles, neighborhoods that were redlined in the 1930s have 50% fewer trees and 3x more industrial facilities today than neighborhoods that were rated favorably. These patterns exist in every US state, most US cities, and across international borders — they are systemic, not anecdotal."),
        ("How Environmental Inequity Was Created", "Environmental inequity was built through decades of policy decisions. Zoning laws in the early 20th century explicitly designated neighborhoods as industrial or residential along racial lines. The Home Owners\\' Loan Corporation redlining maps, created in the 1930s, designated Black and immigrant neighborhoods as hazardous investment risks, directing resources away and industrial development toward these areas. Federal highway construction in the 1950s-1960s deliberately routed interstates through Black neighborhoods, destroying community fabric while concentrating transportation pollution. The siting of waste facilities, power plants, and industrial operations consistently followed the path of least political resistance — which meant communities with the least political power, typically low-income communities of color. These were not individual bad decisions but systemic patterns driven by economic incentives and power imbalances."),
        ("Feedback Loops That Maintain Inequity", "Environmental inequity is self-reinforcing through multiple feedback loops. Pollution lowers property values, which concentrates low-income residents who cannot afford to move, which reduces the community\\'s tax base and political power, which reduces environmental enforcement, which allows more pollution and lower property values. Health impacts from pollution reduce work capacity and increase medical costs, which reduces economic opportunity, which reduces the community\\'s ability to organize politically, which reduces its ability to prevent new pollution sources. Schools in polluted areas have higher student absenteeism and lower academic performance due to health effects, which reduces educational attainment, which limits career options, which keeps residents in the same community. Breaking these cycles requires interventions that address multiple loops simultaneously."),
        ("Environmental Justice Solutions: From Protest to Policy", "The environmental justice movement, which began with community protests against toxic waste siting in Warren County, North Carolina in 1982, has grown into a powerful force for policy change. California\\'s CalEnviroScreen tool maps cumulative environmental burdens and directs 25% of cap-and-trade revenue to the most impacted communities. The Biden administration\\'s Justice40 initiative directs 40% of federal climate investment benefits to disadvantaged communities. Community benefit agreements require that new industrial development provides direct benefits to affected neighborhoods. Right-to-know laws ensure communities can access data about pollution in their neighborhoods. The most effective approaches combine top-down policy (equal enforcement, investment mandates) with bottom-up community power (organizing, legal advocacy, political participation) to address both the symptoms and the systemic causes of environmental inequity.")
    ],
    "lever_L": "Students identify Pollution Source Density, Community Socioeconomic Status, Pollution Exposure Level, Health Outcome Disparity, Regulatory Enforcement Level, Community Political Power, and Green Infrastructure Access as key components of the environmental justice system.",
    "lever_E": "Students determine that pollution concentration correlates with socioeconomic status and political power, that health impacts from pollution reduce economic opportunity in a feedback loop, that regulatory enforcement varies by community power, and that comprehensive interventions outperform single-factor approaches.",
    "lever_V": "Students build a computational model showing how pollution siting, enforcement, community power, and health outcomes interact through feedback loops to create and maintain environmental inequity across communities.",
    "lever_Ev": "Students run status quo, equal enforcement, and systemic transformation scenarios to test predictions about which interventions most effectively reduce environmental disparities.",
    "lever_R": "Students add historical zoning legacy, green gentrification risk, or cumulative impact screening to explore how additional factors affect the dynamics and solutions of environmental inequity.",
    "slides_guide": [
        {
            "num": "Slide 1",
            "title": "Cover",
            "visual": "Title slide with powerful side-by-side aerial images of an industrial neighborhood versus a green affluent suburb in the same city",
            "say": "Your zip code is a better predictor of your health than your genetic code. Today we\\'re modeling why — and building solutions.",
            "do": "Show cover image. Ask: What differences do you notice between these two neighborhoods in the same city? What factors might explain those differences? Take responses without correcting — the model will provide evidence.",
            "time": "2 min"
        },
        {
            "num": "Slide 2",
            "title": "Learning Objectives",
            "visual": "Four learning objectives with environmental justice vocabulary and data visualizations",
            "say": "Today we\\'re using science to understand a social reality: environmental burdens are not distributed equally. Our model will reveal the systemic mechanisms that create and maintain these patterns.",
            "do": "Have students read objectives. Pre-teach vocabulary. Key concept: cumulative impact — it\\'s not just one pollution source, it\\'s the total burden from everything combined. This is why some communities face health crises while neighbors do not.",
            "time": "3 min"
        },
        {
            "num": "Slide 3",
            "title": "Big Question",
            "visual": "Provocative question displayed over data visualization showing pollution exposure correlated with race and income",
            "say": "If clean air and water are basic human needs, why do some communities breathe dirtier air and drink less safe water than others? The answer is not random — it\\'s systemic. Write your hypothesis.",
            "do": "Quick-write: Students write their initial explanation for why environmental burdens are unequally distributed. Save for comparison after modeling reveals the systemic feedback loops.",
            "time": "3 min"
        },
        {
            "num": "Slide 4",
            "title": "LEVER Framework",
            "visual": "LEVER steps overview with environmental justice examples",
            "say": "We\\'ll model environmental inequity as a system — not a collection of individual bad luck. The model will reveal feedback loops that maintain disparities and leverage points that can break them.",
            "do": "Preview LEVER steps. Emphasize: environmental inequity is not random chance — it\\'s a system with identifiable mechanisms. Understanding the system is the first step to changing it.",
            "time": "2 min"
        },
        {
            "num": "Slide 5",
            "title": "Activity 1: Components",
            "visual": "Seven component cards for sorting with environmental justice illustrations",
            "say": "Which components are external drivers of the environmental justice system, and which are internal responses? Think about what sets up the inequity versus what results from it.",
            "do": "Guide sorting: External = Pollution Source Density (historical siting decisions), Community Socioeconomic Status (economic structure). Internal = the five responses. Discuss: These externals were created by policy decisions — they are not natural or inevitable.",
            "time": "8 min"
        },
        {
            "num": "Slide 6",
            "title": "Activity 2: Connections",
            "visual": "Relationship diagram with seven environmental justice components",
            "say": "Trace the feedback loops: pollution affects health, health affects economic opportunity, economic status affects political power, political power affects enforcement, enforcement affects pollution. Where does the cycle feed back on itself?",
            "do": "Students draw arrows. Key discovery: the self-reinforcing cycle of disadvantage. Ask: Once this cycle is running, can it stop on its own? (No — it requires external intervention to break.) Which component, if changed, would disrupt the most feedback loops? (Community Political Power.)",
            "time": "8 min"
        },
        {
            "num": "Slide 7",
            "title": "Activity 3: Simulation",
            "visual": "Simulation showing three scenarios with pollution exposure, health, enforcement, and equity graphs",
            "say": "Run all three scenarios. Pay attention to why equal enforcement alone isn\\'t enough — and what the comprehensive approach achieves that single interventions cannot.",
            "do": "Students run scenarios. Key discussion: Why does equal enforcement reduce violations but not close the exposure gap? Because the physical pollution sources remain concentrated. Ask: What does it take to achieve actual equity, not just equal rules?",
            "time": "10 min"
        },
        {
            "num": "Slide 8",
            "title": "Discoveries",
            "visual": "Four key discoveries with data showing feedback loops, leverage points, and comprehensive intervention outcomes",
            "say": "Environmental inequity isn\\'t random and it isn\\'t inevitable. It was created by systems and it can be changed by systems. But changing it requires understanding — and addressing — the feedback loops that maintain it.",
            "do": "Class discussion. Revisit initial hypotheses. Key question: Now that you\\'ve seen the systemic dynamics, what surprises you about how environmental inequity works? What\\'s the most important insight for creating change?",
            "time": "5 min"
        },
        {
            "num": "Slide 9",
            "title": "STEM Challenge",
            "visual": "Design challenge: Create an Environmental Justice Action Plan for a community facing cumulative pollution burden",
            "say": "A community of 30,000 people surrounded by pollution sources has secured $50 million for environmental justice. Design the plan. Every dollar must be justified by your model data. Who benefits, and how do you prevent displacement?",
            "do": "Groups design comprehensive environmental justice plans allocating $50 million across pollution reduction, health services, community empowerment, green infrastructure, and anti-displacement measures. Present with model evidence for every allocation decision.",
            "time": "12 min"
        }
    ],
    "sort_reasoning": "Pollution Source Density and Community Socioeconomic Status are external components because they represent conditions that were established by historical policy decisions and economic structures before the current environmental justice dynamics operate — they set the stage for the system. Pollution Exposure Level, Health Outcome Disparity, Regulatory Enforcement Level, Community Political Power, and Green Infrastructure Access are internal because they are the dynamic responses and feedback mechanisms within the system that maintain or could change the environmental inequity — they represent how the system operates given its external conditions.",
    "relationships": [
        ("Pollution Source Density to Pollution Exposure Level", "POSITIVE (+)", "More pollution sources in a community directly increase the concentration of pollutants residents breathe, drink, and contact. Each additional source compounds the cumulative burden."),
        ("Pollution Exposure Level to Health Outcome Disparity", "POSITIVE (+)", "Higher pollution exposure causes higher rates of respiratory disease, cardiovascular problems, cancer, developmental delays, and premature death. Health disparities between communities widen as exposure differences increase."),
        ("Health Outcome Disparity to Community Socioeconomic Status", "NEGATIVE (-)", "Poor health reduces work capacity, increases medical costs, lowers educational attainment through absenteeism, and reduces overall economic opportunity, suppressing the socioeconomic status of the affected community."),
        ("Community Socioeconomic Status to Community Political Power", "POSITIVE (+)", "Higher socioeconomic status provides greater access to political participation, legal resources, media attention, and organizational capacity. Wealthier communities are better able to oppose polluting facilities and demand environmental enforcement."),
        ("Community Political Power to Regulatory Enforcement Level", "POSITIVE (+)", "Communities with greater political power successfully demand more frequent inspections, stricter violation penalties, faster cleanup timelines, and stronger opposition to new pollution sources. Political power translates directly to environmental protection."),
        ("Regulatory Enforcement Level to Pollution Exposure Level", "NEGATIVE (-)", "Stronger enforcement reduces pollution by penalizing violations, requiring emission reductions, and compelling cleanup of contaminated sites. Communities with robust enforcement have measurably lower pollution exposure.")
    ],
    "sim_answers": [
        ("Status Quo", "Under current conditions, the model shows a stable pattern of inequity maintained by feedback loops. Pollution Source Density remains high in the low-income community because weak Political Power prevents opposition to facility siting. Regulatory Enforcement is weak because the community lacks political influence. Health Outcome Disparities persist and compound, reducing economic opportunity and further weakening political power. The model demonstrates that without intervention, the system reaches a stable but deeply inequitable equilibrium that will persist indefinitely."),
        ("Equal Enforcement", "Equalizing enforcement reduces ongoing violations and slows the rate of new pollution, but the model shows that overall exposure disparity persists because existing pollution infrastructure remains concentrated in the disadvantaged community. Equal enforcement is necessary but insufficient — it addresses future violations but not accumulated contamination, facility concentration, or the power imbalance that created the inequity. The exposure gap narrows but does not close."),
        ("Systemic Transformation", "The comprehensive approach produces dramatic results: reducing pollution sources in overburdened areas directly lowers exposure, enhanced enforcement prevents new violations, increased Community Political Power enables ongoing protection against future inequity, and green infrastructure investment provides environmental and health benefits that partially offset remaining pollution. The model shows that Health Outcome Disparities begin narrowing within 5-10 years and continue improving as the feedback loops shift from reinforcing inequity to reinforcing improvement. Critically, the empowerment component creates permanent capacity to prevent backsliding — the community gains the power to maintain its own environmental protection.")
    ],
    "reflection_exemplars": [
        ("Why is equal enforcement insufficient for environmental justice?", "The model reveals that equal enforcement addresses only one link in the chain of inequity — it reduces future violations but does not address the accumulated physical infrastructure of pollution. Even with equal enforcement, the community still has 5x more pollution sources per square mile because those facilities were sited there decades ago through decisions the current enforcement regime cannot undo. Equal enforcement also does not address cumulative impact — the combined burden of multiple sources creates health effects far exceeding what any single source\\'s compliance would address. And equal enforcement does not change the power dynamics that led to the inequitable distribution in the first place — without addressing Community Political Power, the enforcement equality may not survive the next budget cut or administration change. True environmental justice requires addressing the root causes, not just leveling the enforcement playing field within an already unequal physical reality."),
        ("How does Community Political Power break the feedback loop?", "The model identifies Community Political Power as the highest-leverage intervention because it addresses the mechanism that maintains all other disparities. When communities gain genuine decision-making authority, they can: prevent new pollution sources from being sited nearby (breaking the accumulation loop), demand enhanced enforcement and faster cleanup of existing contamination (breaking the regulatory gap), advocate for green infrastructure investment that provides environmental benefits (breaking the access gap), and sustain these gains over time because the power remains even when specific projects end. No other single intervention has this cascading effect. Pollution reduction addresses exposure but does not prevent future sources. Enforcement addresses violations but does not address siting or power. Only empowerment changes the fundamental dynamic that created the inequity — the difference in who has the power to say no.")
    ],
    "stem_intro": "Present the challenge: A community of 30,000 people (85% low-income, 92% people of color) is surrounded by a refinery, chemical plants, a highway interchange, and a waste station. Asthma is 4x the national average. Life expectancy is 12 years shorter than the suburb 5 miles away. The community has organized, the state has allocated $50 million, and your team designs the action plan. Every dollar must target the highest-leverage interventions your model identified. And you must prevent green gentrification from displacing the people who fought for change.",
    "stem_concepts": [
        ("Cumulative Impact Assessment", "Tools and methods for quantifying the total environmental and health burden on a community from all combined sources — CalEnviroScreen, EJScreen, and similar platforms assign cumulative impact scores based on pollution exposure, environmental effects, sensitive population indicators, and socioeconomic factors. These scores provide the evidence base for targeting resources to the most overburdened communities and measuring whether interventions are actually reducing disparities."),
        ("Community Benefit Agreements", "Legally binding contracts between developers or industrial operators and community organizations that guarantee specific benefits — including pollution reduction commitments, local hiring requirements, health monitoring, and community investment funds — in exchange for community acceptance of development. CBAs give communities contractual power to hold industry accountable for environmental performance promises."),
        ("Anti-Displacement Strategies", "Policies and programs that prevent environmental improvements from causing gentrification that displaces the original community — including community land trusts that maintain affordable housing regardless of property value increases, right-to-return provisions for displaced residents, rent stabilization, and community ownership of green infrastructure and development projects. Environmental justice without anti-displacement is not justice.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan allocates the $50M across pollution reduction, enforcement, empowerment, green infrastructure, and anti-displacement with every allocation justified by model evidence about leverage points and feedback loops. Addresses cumulative impact, builds permanent community power, and prevents gentrification."),
        ("Proficient (3)", "Plan addresses multiple drivers of environmental inequity with reasonable budget allocation and some connection to model evidence about feedback loops"),
        ("Developing (2)", "Plan focuses on one or two interventions without addressing the systemic feedback loops, or does not consider anti-displacement measures"),
        ("Beginning (1)", "Plan does not address systemic drivers of inequity, lacks model evidence for budget decisions, or ignores the feedback loop dynamics that maintain environmental disparities")
    ],
    "support": [
        "Provide a community map showing the locations of pollution sources, the residential area, and the affluent comparison neighborhood — students can physically see the concentration pattern and discuss why it exists",
        "Use the feedback loop diagram: Pollution reduces Health, which reduces Economic Opportunity, which reduces Political Power, which reduces Enforcement, which allows more Pollution. Ask: Where would you intervene to break this cycle most effectively?",
        "Sentence frames: \\'The model shows that ___ is the most effective leverage point because it breaks the feedback loop between ___ and ___. Allocating $___M to ___ would reduce ___ by ___% because ___.\\'"
    ],
    "extensions": [
        "Use CalEnviroScreen or EJScreen to identify the most environmentally overburdened community in your county or state — map the pollution sources, demographic data, and health indicators, and compare them to the least burdened community to quantify the disparity with real data",
        "Research the environmental justice history of a specific community — such as Cancer Alley in Louisiana, Flint Michigan\\'s water crisis, or the Navajo Nation\\'s uranium mining legacy — and analyze how the systemic mechanisms in your model played out in a real case",
        "Design a cumulative impact screening tool for your community that combines air quality data, industrial facility locations, health indicators, and demographic data into a single score that identifies the neighborhoods most in need of environmental justice investment"
    ],
    "cross_curr": [
        ("Math", "Analyze the statistical correlation between pollution exposure and health outcomes using real data from EJScreen or CalEnviroScreen. Calculate the regression coefficient and R-squared value for the relationship between particulate matter exposure and asthma hospitalization rates, controlling for income. Interpret what the numbers mean for environmental justice policy."),
        ("ELA", "Read excerpts from Robert Bullard\\'s Dumping in Dixie — the foundational text of the environmental justice movement — alongside a recent investigative journalism piece about pollution in a frontline community. Write an analytical essay examining how the patterns Bullard identified in 1990 persist or have changed in the decades since."),
        ("History", "Research the history of redlining in a specific American city using the Mapping Inequality digital archive. Overlay the 1930s HOLC maps with current pollution source locations and demographic data. Write an analysis of how a housing policy from 90 years ago continues to shape environmental health outcomes today.")
    ],
    "misconceptions": [
        ("Environmental inequity is just because poor neighborhoods have cheaper land near industrial areas", "While land costs play a role, this explanation reverses the causation. In many cases, pollution sources were sited in neighborhoods that were already disadvantaged by discriminatory housing policies, not the other way around. Studies show that pollution facilities are disproportionately sited in communities of color even after controlling for income and land cost. Furthermore, the cheap-land explanation treats the inequity as natural market forces when it is actually the result of zoning decisions, permitting processes, and political power differentials that systematically favor placing burdens on communities with less power to resist. The model shows that market forces operate within a system structured by policy — change the policy, and the market outcomes change.", "Present the historical sequence: Show that in many cases, the community existed first and the pollution source was sited there because the community lacked political power to prevent it. The land became cheap because of the pollution, not the other way around. Chicken and egg: which came first, the disadvantage or the pollution?"),
        ("Everyone faces the same environmental risks regardless of where they live", "Environmental monitoring data consistently shows dramatic differences in pollution exposure based on neighborhood, with differences of 2-5x in particulate matter, toxic chemical exposure, and contaminated site proximity between communities in the same city. These are not small variations — they translate to measurable differences in asthma rates (2-4x higher), cancer incidence (elevated), and life expectancy (10-20 years shorter in the most polluted communities). The model demonstrates that these differences are not random but are maintained by feedback loops that concentrate pollution in specific communities.", "Present the data: Show side-by-side air quality measurements, health statistics, and pollution source maps for two neighborhoods in the same city — one affluent and one disadvantaged. The differences are stark and undeniable. Ask: If everyone faces equal risk, how do you explain these data?"),
        ("Individual choices like eating well and exercising can overcome pollution exposure", "While personal health behaviors matter, they cannot overcome the physiological effects of breathing polluted air, drinking contaminated water, and living near toxic waste. A child cannot exercise their way out of lead exposure. An athlete who trains outside in polluted air absorbs more pollution, not less. Studies show that zip code — a proxy for environmental quality — is a stronger predictor of health outcomes than individual behavior, diet, or even genetic risk factors. The model demonstrates that environmental conditions set the baseline from which individual choices operate — and in overburdened communities, that baseline is significantly worse.", "Present the analogy: If two runners race but one must carry a 50-pound weight (pollution burden), individual effort still matters, but the structural disadvantage determines the outcome far more than personal performance. Ask: Is it fair to judge both runners equally when one started with a massive disadvantage?")
    ]
}

ALL_LESSONS = [L01, L02, L03, L04, L05, L06, L07, L08, L09, L10]
