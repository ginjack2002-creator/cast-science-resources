#!/usr/bin/env python3
"""Multiple choice pre/post assessment questions for Grade 9 Level 1 ModelIt! Lessons"""

# ── L01: Why Do Athletes Collapse in the Heat? ──────────────────────

L01_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A student claims that sweating is a sign of being out of shape. Which of the following best explains why this claim is scientifically inaccurate?",
            "choices": {
                "A": "Sweating is the body's primary mechanism for evaporative cooling and is more efficient in well-conditioned athletes",
                "B": "Sweating only occurs when the body is overheating due to illness",
                "C": "Sweating is controlled by voluntary muscles and can be stopped at will",
                "D": "Sweating depletes the body's salt reserves, which is harmful regardless of fitness level"
            },
            "correct": "A",
            "feedback_correct": "Correct. Sweating is the body's primary thermoregulatory response, and trained athletes often sweat more efficiently because their cooling systems are better adapted to dissipate heat.",
            "feedback_incorrect": "Sweating is actually a sign of an efficient cooling system. Well-trained athletes often sweat MORE than untrained individuals because their thermoregulatory systems are better adapted to dissipate metabolic heat through evaporative cooling."
        },
        {
            "question": "During a football game on a hot day, two players of similar fitness levels are performing at the same intensity. Player A collapses from heat exhaustion while Player B continues playing. Which factor most likely explains this difference?",
            "choices": {
                "A": "Player A has a genetic condition that prevents all sweating",
                "B": "Player A consumed significantly less water before and during the game than Player B",
                "C": "Player B is naturally immune to heat-related illness",
                "D": "Player A was wearing a darker uniform color that absorbed more heat"
            },
            "correct": "B",
            "feedback_correct": "Correct. Hydration level is the most common variable that determines individual vulnerability to heat illness. Dehydration reduces the body's ability to produce sweat and maintain core temperature.",
            "feedback_incorrect": "The most likely explanation is a difference in hydration. When the body lacks sufficient water, it cannot produce enough sweat to cool itself, causing core temperature to rise uncontrollably. Uniform color has minimal impact compared to internal hydration status."
        },
        {
            "question": "Which of the following best describes the concept of homeostasis?",
            "choices": {
                "A": "The body's ability to increase temperature during exercise to improve performance",
                "B": "A state where the body's internal conditions remain perfectly constant at all times",
                "C": "The body's ability to maintain stable internal conditions within a functional range despite changing external conditions",
                "D": "A process that only occurs when the body is at rest and not under physical stress"
            },
            "correct": "C",
            "feedback_correct": "Correct. Homeostasis is the maintenance of stable internal conditions within a functional range, even as external conditions change. It is dynamic, not static, and operates continuously.",
            "feedback_incorrect": "Homeostasis does not mean conditions are perfectly constant or only maintained at rest. It refers to the body's ability to keep internal conditions like temperature, pH, and blood sugar within a functional range despite external changes."
        },
        {
            "question": "An athlete's core body temperature rises from 37°C to 39°C during a workout. The body responds by increasing sweat production, which eventually brings the temperature back toward 37°C. This process is an example of which type of biological mechanism?",
            "choices": {
                "A": "Positive feedback, because the response amplifies the original change",
                "B": "Negative feedback, because the response counteracts the original change",
                "C": "Passive diffusion, because heat naturally moves from hot to cold",
                "D": "Active transport, because the body uses energy to move heat molecules"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is a negative feedback mechanism because the body's response (increased sweating) opposes the initial change (rising temperature), working to restore the original set point.",
            "feedback_incorrect": "When the body detects a change (rising temperature) and responds in a way that reverses that change (sweating to cool down), this is negative feedback. The response negates the stimulus, restoring balance."
        },
        {
            "question": "A coach notices that heat-related illness incidents at their school have occurred at outdoor temperatures as low as 78°F (26°C). Which explanation best accounts for this observation?",
            "choices": {
                "A": "Heat illness can only occur above 100°F, so these incidents must have been misdiagnosed",
                "B": "Air temperature alone does not determine heat illness risk; humidity, exertion level, and hydration status interact to determine vulnerability",
                "C": "The thermometers used to measure temperature were likely inaccurate",
                "D": "Heat illness at low temperatures is caused by an allergic reaction to sunlight rather than thermoregulatory failure"
            },
            "correct": "B",
            "feedback_correct": "Correct. Heat illness results from the interaction of multiple factors including humidity (which reduces evaporative cooling efficiency), exercise intensity (which generates metabolic heat), and hydration status. Air temperature is only one variable.",
            "feedback_incorrect": "Heat illness can occur at surprisingly moderate temperatures when other factors align. High humidity reduces the effectiveness of sweating, intense exertion generates large amounts of metabolic heat, and dehydration limits the body's cooling capacity. The combination of these factors matters more than air temperature alone."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In a computational model of thermoregulation, a student sets Physical Exertion to maximum and Hydration Level to low. The model shows Core Temperature rising sharply while Sweat Rate initially increases then drops to near zero. Which explanation best interprets this model behavior?",
            "choices": {
                "A": "The model is malfunctioning because sweat rate should continue to increase with temperature",
                "B": "The negative feedback loop has broken down because the body cannot produce sweat without adequate water, causing an uncontrolled temperature increase",
                "C": "The body has switched from negative feedback to a more efficient cooling mechanism",
                "D": "Sweat rate decreases because the body has successfully cooled itself and no longer needs evaporative cooling"
            },
            "correct": "B",
            "feedback_correct": "Correct. This model output demonstrates the critical failure point in thermoregulation. Sweat production requires water. When hydration is depleted, the negative feedback loop breaks because the effector (sweat glands) can no longer function, converting the system to a dangerous positive feedback scenario.",
            "feedback_incorrect": "The model shows the breaking point of the thermoregulatory feedback loop. Sweating requires water. When hydration is too low, the body physically cannot produce sweat to cool itself. The negative feedback loop fails, and core temperature spirals upward without any mechanism to bring it back down."
        },
        {
            "question": "A student's model shows that during the 'Gradual Dehydration' scenario, core temperature remains stable for the first 45 minutes, then begins rising rapidly. Which concept best explains this pattern?",
            "choices": {
                "A": "The system has a tipping point where the feedback loop transitions from maintaining homeostasis to failing catastrophically",
                "B": "The body's thermostat resets to a higher temperature after 45 minutes of exercise",
                "C": "The model has a built-in delay that prevents temperature changes for the first 45 minutes",
                "D": "Core temperature always rises linearly during exercise regardless of hydration"
            },
            "correct": "A",
            "feedback_correct": "Correct. The model reveals a critical tipping point. Initially, the body has enough hydration to maintain the negative feedback loop. As water depletes, the system reaches a threshold where cooling capacity can no longer match heat production, and the system shifts from stable homeostasis to runaway heating.",
            "feedback_incorrect": "The delayed temperature rise followed by rapid increase demonstrates a tipping point in the system. The body maintains homeostasis as long as sufficient water is available for sweating. When hydration crosses a critical threshold, the cooling system fails and temperature rises uncontrollably."
        },
        {
            "question": "Two students build models of thermoregulation. Student A's model includes only Core Temperature and Sweat Rate. Student B's model adds Hydration Level and Physical Exertion. Which statement best evaluates the difference between these models?",
            "choices": {
                "A": "Student A's model is superior because simpler models are always more accurate",
                "B": "Student B's model can predict system failure conditions that Student A's model cannot, because it includes the external inputs that drive and constrain the feedback loop",
                "C": "Both models are equally valid because they contain the same core feedback mechanism",
                "D": "Neither model is useful because thermoregulation requires at least ten components to model accurately"
            },
            "correct": "B",
            "feedback_correct": "Correct. Student B's model includes the external variables (hydration and exertion) that determine whether the feedback loop functions or breaks down. Without these inputs, Student A's model cannot predict the conditions under which homeostasis fails.",
            "feedback_incorrect": "Student B's model is more powerful because it includes the external drivers (Physical Exertion and Hydration Level) that determine whether the negative feedback loop operates successfully. Student A's model can show the feedback mechanism but cannot predict when or why it fails."
        },
        {
            "question": "Based on model evidence, which intervention would be most effective at preventing heat-related illness during a high-intensity outdoor practice in 90°F weather?",
            "choices": {
                "A": "Moving practice to a shaded area, because shade eliminates the risk of overheating",
                "B": "Implementing mandatory hydration breaks every 15 minutes, because maintaining hydration preserves the integrity of the negative feedback loop",
                "C": "Reducing practice duration to 30 minutes, because heat illness cannot occur in short time periods",
                "D": "Having athletes wear lighter-colored clothing, because clothing color is the primary determinant of core temperature"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that hydration is the critical variable that determines whether the thermoregulatory feedback loop continues to function. Mandatory hydration breaks maintain the body's ability to produce sweat and sustain evaporative cooling.",
            "feedback_incorrect": "The computational model shows that the feedback loop breaks when hydration drops below a critical threshold. Mandatory hydration breaks directly address the most important controllable variable in the system, ensuring the body can continue producing sweat to regulate core temperature."
        },
        {
            "question": "A student extends their thermoregulation model by adding an Acclimatization Level component. They find that higher acclimatization shifts the tipping point, allowing athletes to exercise longer before the feedback loop fails. Which reasoning best explains this model prediction?",
            "choices": {
                "A": "Acclimatized athletes do not produce body heat during exercise",
                "B": "Acclimatization improves sweating efficiency and plasma volume, allowing the cooling system to operate effectively at higher core temperatures and lower hydration levels",
                "C": "Acclimatization eliminates the body's need for water during exercise",
                "D": "Acclimatized athletes have a lower resting core temperature, so they can tolerate unlimited heat exposure"
            },
            "correct": "B",
            "feedback_correct": "Correct. Heat acclimatization produces physiological adaptations including earlier onset of sweating, increased sweat volume, expanded plasma volume, and improved cardiovascular efficiency. These changes extend the functional range of the feedback loop before it reaches its tipping point.",
            "feedback_incorrect": "Acclimatization does not eliminate the need for hydration or heat production. Instead, it improves the efficiency of the cooling system through physiological adaptations like increased sweat output, expanded blood plasma volume, and improved cardiovascular function, which extends how long the body can maintain homeostasis before the tipping point."
        }
    ]
}

# ── L02: The Vaping Crisis ──────────────────────────────────────────

L02_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A classmate claims that vaping is safe because 'it's just water vapor.' Which scientific evidence most directly contradicts this claim?",
            "choices": {
                "A": "E-cigarette aerosol contains nicotine, formaldehyde, heavy metals, and ultrafine particles that penetrate deep into lung tissue",
                "B": "Water vapor is always harmful when inhaled in any quantity",
                "C": "Vaping devices use batteries, which emit radiation that damages lungs",
                "D": "The flavoring in vapes is the only harmful component"
            },
            "correct": "A",
            "feedback_correct": "Correct. Chemical analysis of e-cigarette aerosol reveals it contains far more than water vapor, including nicotine, formaldehyde, acrolein, heavy metals like lead and nickel, and ultrafine particles that reach the deepest parts of the lungs.",
            "feedback_incorrect": "E-cigarette aerosol is not water vapor. Chemical analysis shows it contains nicotine, propylene glycol, vegetable glycerin, formaldehyde, acrolein, heavy metals, and ultrafine particles. These substances cause direct cellular damage to lung tissue."
        },
        {
            "question": "Which of the following best describes the function of epithelial cells in the respiratory system?",
            "choices": {
                "A": "They produce red blood cells for oxygen transport",
                "B": "They line the airways and alveoli, facilitating gas exchange and protecting against pathogens",
                "C": "They break down food particles that accidentally enter the lungs",
                "D": "They produce the surfactant that inflates the lungs during breathing"
            },
            "correct": "B",
            "feedback_correct": "Correct. Epithelial cells form the thin lining of airways and alveoli, serving as the surface where oxygen and carbon dioxide exchange occurs and as a barrier protecting the lungs from foreign particles and pathogens.",
            "feedback_incorrect": "Epithelial cells line the airways and alveoli of the respiratory system. They form the delicate surface where gas exchange occurs between air and blood, and they serve as a protective barrier against inhaled particles and pathogens."
        },
        {
            "question": "A person experiences no noticeable symptoms after vaping daily for three months. Which statement best evaluates the conclusion that 'vaping is not causing any harm'?",
            "choices": {
                "A": "This conclusion is valid because symptoms always appear immediately when damage occurs",
                "B": "This conclusion is flawed because cumulative cellular damage can accumulate silently before symptoms become noticeable",
                "C": "This conclusion is valid because the lungs have a perfect self-repair mechanism",
                "D": "This conclusion is flawed only if the person is using nicotine-containing products"
            },
            "correct": "B",
            "feedback_correct": "Correct. Many forms of biological damage are cumulative and subclinical, meaning they build up over time without producing noticeable symptoms. Like UV skin damage, the effects of chronic chemical exposure may not manifest as symptoms until significant tissue damage has occurred.",
            "feedback_incorrect": "The absence of symptoms does not mean absence of harm. Cumulative damage to lung cells can occur at the microscopic level for months or years before clinical symptoms appear, similar to how sun damage accumulates invisibly before eventually causing visible skin changes."
        },
        {
            "question": "When foreign chemicals enter the lungs, the immune system responds with inflammation. Which of the following best describes the purpose of this response?",
            "choices": {
                "A": "Inflammation permanently strengthens lung tissue against future chemical exposure",
                "B": "Inflammation sends immune cells and fluids to the damaged area to fight infection and begin repair",
                "C": "Inflammation increases the absorption rate of chemicals to process them faster",
                "D": "Inflammation shuts down the lungs temporarily to prevent further chemical entry"
            },
            "correct": "B",
            "feedback_correct": "Correct. Inflammation is the body's acute defense response, mobilizing white blood cells, increasing blood flow, and releasing chemical signals to combat threats and initiate tissue repair at the site of injury.",
            "feedback_incorrect": "The inflammatory response is the immune system's way of defending damaged tissue. It recruits white blood cells to the injury site, increases blood flow to deliver healing factors, and initiates the repair process. It is meant to be a short-term protective response."
        },
        {
            "question": "The respiratory system is organized hierarchically: trachea branches into bronchi, which branch into bronchioles, which terminate in alveoli. What is the primary advantage of this organizational pattern?",
            "choices": {
                "A": "It slows down airflow to prevent damage to delicate tissue",
                "B": "It maximizes the surface area available for gas exchange while fitting within the chest cavity",
                "C": "It ensures that all inhaled particles are trapped before reaching the blood",
                "D": "It creates a one-way airflow system similar to bird lungs"
            },
            "correct": "B",
            "feedback_correct": "Correct. The branching structure creates an enormous surface area for gas exchange (approximately the size of a tennis court) while efficiently fitting within the limited space of the chest cavity. This hierarchical design maximizes oxygen absorption.",
            "feedback_incorrect": "The branching hierarchy of the respiratory system maximizes surface area for gas exchange. By subdividing into progressively smaller structures, the lungs achieve a gas exchange surface area equivalent to a tennis court within the compact space of the chest."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In a computational model of vaping damage, a student observes that Inflammation Response increases steadily over time even when Nicotine Concentration remains constant. Which mechanism best explains this model behavior?",
            "choices": {
                "A": "The model contains an error because inflammation should remain constant if chemical input is constant",
                "B": "Chronic inflammation creates a destructive feedback loop where the immune response itself damages healthy cells, triggering additional inflammation",
                "C": "The body gradually becomes more allergic to nicotine over time",
                "D": "Inflammation increases because the lungs are successfully healing and need more immune activity"
            },
            "correct": "B",
            "feedback_correct": "Correct. Chronic inflammation produces a self-reinforcing cycle. The immune molecules (reactive oxygen species, cytokines) released to fight damage also destroy healthy neighboring cells, which triggers more inflammation to address the new damage. This destructive feedback loop escalates even at constant exposure levels.",
            "feedback_incorrect": "The model shows a destructive feedback loop. Chronic inflammation damages healthy cells through collateral immune activity. This new damage triggers additional inflammation, which causes more collateral damage. The cycle escalates even without increasing the chemical input."
        },
        {
            "question": "A student's model predicts that a person who quits vaping after 6 months recovers most lung cell health, while a person who quits after 3 years shows only partial recovery. What concept does this comparison best demonstrate?",
            "choices": {
                "A": "Lung cells regenerate at a constant rate regardless of damage severity",
                "B": "Some cellular damage is reversible while prolonged exposure causes irreversible damage through permanent scar tissue formation",
                "C": "The body develops immunity to chemical damage over longer exposure periods",
                "D": "Recovery rate depends entirely on age, not duration of exposure"
            },
            "correct": "B",
            "feedback_correct": "Correct. Short-term damage primarily involves repairable cellular injury. However, prolonged chronic inflammation leads to fibrosis (scarring), where functional lung tissue is permanently replaced by non-functional scar tissue that cannot regenerate.",
            "feedback_incorrect": "The model reveals that recovery potential depends on the type and extent of damage. Short-term exposure causes primarily reversible cellular damage. Prolonged exposure leads to fibrosis, where scar tissue permanently replaces functional lung tissue. Once scarring occurs, that damage cannot be reversed."
        },
        {
            "question": "Using the hierarchical organization framework, which sequence correctly traces the impact of vaping chemicals from the smallest to largest scale of biological organization?",
            "choices": {
                "A": "Whole lung function decreases → alveolar cells are damaged → molecules in aerosol enter airways",
                "B": "Chemical molecules damage epithelial cells → damaged cells impair alveolar gas exchange → reduced gas exchange decreases whole lung function",
                "C": "The respiratory system fails → individual cells die → chemical reactions are disrupted",
                "D": "Nicotine enters the brain → the brain signals lungs to stop working → lung cells die"
            },
            "correct": "B",
            "feedback_correct": "Correct. This sequence follows the hierarchical cascade from molecular level (chemical interaction with cells) to cellular level (epithelial damage) to tissue level (alveolar function) to organ level (whole lung function). Damage at smaller scales propagates upward through the hierarchy.",
            "feedback_incorrect": "The correct cascade follows hierarchical organization from small to large: chemical molecules interact with individual epithelial cells, damaged cells impair the function of alveolar structures, and compromised alveoli reduce overall lung function. Each level of organization is affected by damage at the level below it."
        },
        {
            "question": "A student's model shows that the 'Occasional Use' scenario still produces measurable decreases in Lung Cell Health, even though the person has no symptoms. What is the most important implication of this finding for public health messaging?",
            "choices": {
                "A": "Occasional use is completely safe because the damage is too small to matter",
                "B": "Any level of vaping causes some degree of cellular damage, and the absence of symptoms does not indicate the absence of harm",
                "C": "The model must be inaccurate because people with no symptoms cannot have any cellular damage",
                "D": "Occasional use is only harmful if combined with cigarette smoking"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that even low-level exposure causes measurable biological changes at the cellular level. Symptoms are a lagging indicator that appear only after substantial cumulative damage. Absence of symptoms is not evidence of absence of harm.",
            "feedback_incorrect": "The model provides evidence that cellular damage occurs even at low exposure levels, below the threshold that produces noticeable symptoms. This means a person can sustain progressive lung cell damage without feeling any effects, making the damage invisible until it becomes clinically significant."
        },
        {
            "question": "A public health team uses model data to design an anti-vaping campaign. Which approach best applies the scientific evidence from the vaping damage model?",
            "choices": {
                "A": "Show graphic images of diseased lungs with the message 'Vaping kills' to scare teens into quitting",
                "B": "Present the dose-response data showing cumulative cellular damage over time, with visualizations of how the inflammation-damage feedback loop escalates even after exposure stops",
                "C": "Tell teens that vaping is illegal and they will be punished if caught",
                "D": "Claim that one puff of a vape causes immediate lung cancer"
            },
            "correct": "B",
            "feedback_correct": "Correct. Evidence-based science communication uses accurate data to inform decision-making. The model provides compelling data about cumulative damage, feedback loops, and the gap between symptoms and actual cellular harm. Presenting this evidence accurately is more credible and effective than fear tactics or exaggeration.",
            "feedback_incorrect": "Effective science communication presents accurate biological evidence in an accessible way. The model provides powerful evidence about cumulative damage and the destructive feedback loop that can be presented without exaggeration or fear tactics. Accuracy builds credibility, while scare tactics often backfire with skeptical teenage audiences."
        }
    ]
}

# ── L03: Can We Actually Live on Mars? ──────────────────────────────

L03_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Mars has an atmospheric pressure of approximately 0.6 kPa, while Earth's is 101.3 kPa. What would be the most immediate consequence for an unprotected human exposed to Mars' atmosphere?",
            "choices": {
                "A": "They would freeze to death within minutes due to the cold temperature",
                "B": "The extremely low pressure would cause body fluids to boil at body temperature and prevent breathing",
                "C": "They would suffocate slowly over several hours as oxygen depleted",
                "D": "They would be crushed by the high atmospheric pressure of Mars"
            },
            "correct": "B",
            "feedback_correct": "Correct. At 0.6 kPa, water boils at temperatures well below body temperature. An unprotected human would experience ebullism (body fluids vaporizing), inability to breathe, and loss of consciousness within approximately 15 seconds.",
            "feedback_incorrect": "While Mars is extremely cold, the most immediate lethal threat is the near-vacuum pressure. At 0.6 kPa (less than 1% of Earth's), water boils at body temperature, making blood and tissue fluids vaporize. This effect is more immediately lethal than the temperature."
        },
        {
            "question": "Earth is protected from most solar radiation by its magnetic field and thick atmosphere. Mars lacks both of these protections. What is the primary biological danger of this radiation exposure?",
            "choices": {
                "A": "Radiation causes sunburn on exposed skin",
                "B": "Ionizing radiation damages DNA, increasing the risk of cancer and cellular dysfunction",
                "C": "Radiation heats the body, causing overheating similar to heat stroke",
                "D": "Radiation prevents photosynthesis in all plant species"
            },
            "correct": "B",
            "feedback_correct": "Correct. Ionizing radiation from solar wind and cosmic rays has enough energy to break chemical bonds in DNA, causing mutations that can lead to cancer, cellular dysfunction, and potentially lethal organ damage over extended exposure periods.",
            "feedback_incorrect": "The primary danger of Mars' unshielded radiation is DNA damage. Ionizing radiation breaks chemical bonds within DNA molecules, causing mutations. Over a two-year Mars stay, astronauts would receive radiation doses that significantly increase cancer risk and can impair cellular function."
        },
        {
            "question": "A student argues that Mars colonization is mainly a discovery problem: 'We just need to find the right resources on Mars.' Which response best evaluates this claim?",
            "choices": {
                "A": "This is correct because we don't know what Mars has to offer yet",
                "B": "This is partially correct; we need to discover new physics to survive on Mars",
                "C": "This is incorrect; Mars colonization is primarily an engineering problem because we already understand the challenges but lack the technology to solve them all simultaneously",
                "D": "This is incorrect because Mars has no useful resources whatsoever"
            },
            "correct": "C",
            "feedback_correct": "Correct. We already know Mars has water ice, a CO2 atmosphere, and mineral resources. The challenge is engineering all the systems needed to maintain human life simultaneously: pressurized habitats, radiation shielding, water extraction, food production, and temperature control, all with virtually zero margin for error.",
            "feedback_incorrect": "Mars colonization is fundamentally an engineering challenge, not a discovery one. We know what Mars has (water ice, CO2 atmosphere, minerals) and what humans need (pressure, oxygen, water, food, radiation shielding). The challenge is building systems that deliver all of these simultaneously and reliably in an environment where any single failure is catastrophic."
        },
        {
            "question": "Which statement best describes why growing food on Mars is particularly challenging?",
            "choices": {
                "A": "Mars soil contains all necessary nutrients but receives too much sunlight for plant growth",
                "B": "Plants require controlled atmospheric pressure, radiation shielding, appropriate temperature, and purified water, none of which Mars provides naturally",
                "C": "Earth plants cannot grow in reduced gravity under any circumstances",
                "D": "Mars has adequate conditions for plant growth in its equatorial regions during summer"
            },
            "correct": "B",
            "feedback_correct": "Correct. Food production on Mars requires simultaneously solving multiple environmental challenges: maintaining atmospheric pressure above the boiling point of water, shielding crops from lethal radiation, controlling temperature within growth ranges, and providing clean water free of toxic perchlorates found in Martian soil.",
            "feedback_incorrect": "Growing food on Mars requires engineering solutions for every environmental factor plants need: adequate pressure (Mars has less than 1% of Earth's), radiation protection, temperature control (Mars averages -60 degrees C), and clean water. Mars soil also contains toxic perchlorates that must be removed."
        },
        {
            "question": "An engineer designing a Mars habitat says: 'If we can solve the water problem, everything else falls into place.' Why is this statement an oversimplification?",
            "choices": {
                "A": "Water is not actually needed on Mars because astronauts can bring enough from Earth",
                "B": "Mars survival requires solving multiple interdependent challenges simultaneously; failure of any single system, not just water, can be catastrophic",
                "C": "Water is the least important resource on Mars",
                "D": "The water problem on Mars has already been solved by robotic missions"
            },
            "correct": "B",
            "feedback_correct": "Correct. Mars survival is a systems problem. Pressure, radiation, temperature, water, and food must all be maintained simultaneously. Solving water alone does not address the other four critical factors, each of which can independently cause mission failure.",
            "feedback_incorrect": "Mars colonization requires solving all five survival factors simultaneously: atmospheric pressure, radiation shielding, temperature control, water availability, and food production. Solving any one problem in isolation does not prevent catastrophic failure from the others. It is the interdependence of these systems that makes Mars colonization so challenging."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In a Mars habitat model, a student simulates a slow atmospheric pressure leak that reduces habitat pressure by 20% over three days. The model shows Crop Viability dropping before any other system reaches critical levels. Why do crops fail first?",
            "choices": {
                "A": "Crops are more sensitive to pressure changes than humans because plants require higher pressure for liquid water transport and gas exchange through stomata",
                "B": "Crops fail first because they are planted outside the habitat",
                "C": "Pressure changes only affect plants, not humans or equipment",
                "D": "Crops fail because lower pressure increases radiation inside the habitat"
            },
            "correct": "A",
            "feedback_correct": "Correct. Plants rely on adequate atmospheric pressure for transpiration, water transport through xylem, and gas exchange through stomata. As pressure drops, water begins to boil at lower temperatures, disrupting plant physiology before the pressure becomes immediately lethal to humans who can don emergency pressure suits.",
            "feedback_incorrect": "Crops are particularly sensitive to pressure changes because plant physiology depends on adequate atmospheric pressure for water transport, transpiration, and gas exchange. Plants cannot don emergency equipment like humans can, making them the most vulnerable biological component during a gradual pressure loss."
        },
        {
            "question": "A student compares the 'Pressure Breach' and 'Water Crisis' scenarios in their Mars habitat model. Which conclusion is best supported by the model evidence?",
            "choices": {
                "A": "Both scenarios produce identical outcomes because pressure and water are the same variable",
                "B": "Pressure breach is more immediately lethal (minutes to hours) while water crisis is more strategically threatening (weeks to months), demonstrating that 'most critical' depends on timescale",
                "C": "Water crisis is always more dangerous than pressure breach",
                "D": "Neither scenario is truly dangerous because backup systems would prevent any failure"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that different failure modes operate on different timescales. A pressure breach can kill within minutes, making it the most time-critical threat. A water crisis develops over weeks but threatens long-term survival by limiting food production and life support. The 'most critical' factor depends on whether you are evaluating immediate or sustained survival.",
            "feedback_incorrect": "The model demonstrates that different system failures have different temporal profiles. Pressure loss is the most acute threat because humans and plants cannot survive without adequate pressure for more than minutes. Water scarcity is a slower-developing but equally fatal threat because it limits food production, oxygen generation, and basic life support over weeks to months."
        },
        {
            "question": "A student's Mars habitat model has four external components (Pressure, Radiation, Water, Temperature) all affecting one internal component (Crop Viability). What does this model structure reveal about system vulnerability?",
            "choices": {
                "A": "The system is robust because it has many inputs supporting one output",
                "B": "The system is fragile because Crop Viability is a single point of failure that depends on ALL four external factors being within acceptable ranges simultaneously",
                "C": "The system is efficient because only one component needs to be monitored",
                "D": "The model structure shows that only one external factor needs to be controlled at a time"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model structure reveals that Crop Viability acts as a single point of failure with four independent failure pathways. Since ANY one of the four external factors dropping below its threshold can destroy crops, the system has no redundancy at this critical node. This explains why Mars colonization requires near-perfect engineering across all systems simultaneously.",
            "feedback_incorrect": "Having four independent failure pathways converging on a single critical output (Crop Viability) makes the system extremely fragile. If any ONE external factor fails, crops die regardless of the other three being perfect. This lack of redundancy means the probability of system failure is the sum of all individual failure probabilities."
        },
        {
            "question": "After running all scenarios, a student concludes: 'Mars colonization is fundamentally different from any engineering challenge on Earth.' Which model evidence best supports this conclusion?",
            "choices": {
                "A": "Earth engineering projects are always more complex than Mars projects",
                "B": "On Earth, the natural environment provides baseline life support (breathable air, moderate pressure, liquid water, tolerable temperatures); on Mars, every survival requirement must be artificially maintained with zero backup from the environment",
                "C": "Mars projects cost more money than Earth projects",
                "D": "Mars has different gravity, which is the only significant engineering challenge"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that Earth engineering can rely on baseline environmental support. If a building's climate control fails on Earth, occupants can open a window. On Mars, failure of any life support system means death because the external environment provides nothing humans need. This zero-backup condition makes Mars engineering fundamentally different in kind, not just degree.",
            "feedback_incorrect": "The key insight from the model is that Earth always provides environmental backup. On Earth, if one system fails, the natural environment still provides breathable air, drinkable water, tolerable temperatures, and adequate pressure. On Mars, the environment provides none of these, so every single system must function perfectly with no fallback."
        },
        {
            "question": "A student adds Energy Production as a new component to their Mars model and discovers that ALL other systems depend on it. What does this reveal about the system's interdependencies?",
            "choices": {
                "A": "Energy is a luxury component that improves comfort but is not essential for survival",
                "B": "Energy production is a foundational dependency because maintaining pressure, temperature, water extraction, and radiation shielding all require continuous power, making energy failure equivalent to simultaneous failure of all other systems",
                "C": "Energy only affects crop viability and has no impact on other components",
                "D": "Adding more components always makes models less accurate"
            },
            "correct": "B",
            "feedback_correct": "Correct. The extended model reveals that energy production is a 'master dependency' because every other survival system requires continuous power. Pressure pumps, heating systems, water extraction equipment, and radiation shielding all consume energy. An energy failure cascades immediately into failure of all dependent systems, making it arguably the most critical component.",
            "feedback_incorrect": "Adding energy production to the model reveals a critical insight: it is a foundational dependency that all other systems require. Without power, pressure cannot be maintained, temperature cannot be regulated, water cannot be extracted, and many forms of radiation shielding require active systems. Energy failure effectively causes simultaneous failure of every other survival system."
        }
    ]
}

# ── L04: Why Your Phone Battery Dies So Fast ────────────────────────

L04_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A phone battery stores energy in chemical form. When the phone is used, this energy is converted into multiple other forms. Which sequence correctly represents this energy conversion chain?",
            "choices": {
                "A": "Light energy → chemical energy → electrical energy → heat",
                "B": "Chemical energy → electrical energy → light, sound, computation, and heat",
                "C": "Electrical energy → chemical energy → nuclear energy → light",
                "D": "Heat energy → electrical energy → chemical energy → light"
            },
            "correct": "B",
            "feedback_correct": "Correct. Phone batteries store chemical energy in lithium-ion bonds. During discharge, this converts to electrical energy flowing through circuits, which then converts to light (screen), sound (speakers), computation (processor), and inevitably heat (waste energy at every conversion step).",
            "feedback_incorrect": "Batteries store energy as chemical potential energy. When discharged, this converts to electrical current, which is then converted to various useful forms (light from the screen, sound from speakers, computation from the processor) plus waste heat at every conversion step."
        },
        {
            "question": "Your phone gets noticeably warm after 30 minutes of gaming. Where is this thermal energy coming from?",
            "choices": {
                "A": "The phone absorbs heat from the user's hands",
                "B": "The battery produces heat as a separate function to keep the phone warm",
                "C": "It is wasted energy from inefficient conversion of electrical energy to computation and display, released as heat through electrical resistance",
                "D": "The phone's antenna generates heat by receiving wireless signals"
            },
            "correct": "C",
            "feedback_correct": "Correct. Heat generation in phones results from energy conversion inefficiency. Every time electrical energy converts to computation (transistor switching) or light (screen operation), some energy is inevitably lost as thermal energy due to electrical resistance. This waste heat represents battery energy that produced no useful output.",
            "feedback_incorrect": "The heat your phone generates during intensive use is wasted battery energy. Every energy conversion step loses some energy as heat due to electrical resistance in circuits and transistor switching. A gaming phone generating 3-5 watts of heat means 3-5 watts of battery energy are being converted to useless thermal output."
        },
        {
            "question": "The term 'energy efficiency' refers to the ratio of useful energy output to total energy input. Which statement best describes why no device can achieve 100% energy efficiency?",
            "choices": {
                "A": "Engineers are not skilled enough to build perfectly efficient devices",
                "B": "The second law of thermodynamics states that every energy conversion inevitably produces some waste heat",
                "C": "Devices intentionally waste energy to prevent overheating",
                "D": "100% efficiency is achievable but would make devices too expensive"
            },
            "correct": "B",
            "feedback_correct": "Correct. The second law of thermodynamics establishes that entropy increases in any energy conversion, meaning some energy always degrades to thermal energy. This is a fundamental physical law, not an engineering limitation.",
            "feedback_incorrect": "The second law of thermodynamics dictates that every energy conversion produces some waste heat. This is a fundamental law of physics, not an engineering shortcoming. No device in the universe can convert energy from one form to another with perfect efficiency."
        },
        {
            "question": "A student notices their phone battery lasts 24 hours on standby but only 3 hours while gaming. What is the primary reason for this difference?",
            "choices": {
                "A": "Gaming uses a different type of battery chemistry than standby mode",
                "B": "Gaming simultaneously drives maximum power draw from the screen and processor, consuming energy 20-50 times faster than standby",
                "C": "The phone's battery shrinks during gaming due to heat damage",
                "D": "Standby mode recharges the battery using ambient electromagnetic radiation"
            },
            "correct": "B",
            "feedback_correct": "Correct. Gaming requires both the screen at high brightness and the CPU/GPU at maximum processing capacity simultaneously, drawing 5-8 watts compared to standby's 0.1-0.3 watts. This 20-50x power draw difference directly explains the proportional difference in battery life.",
            "feedback_incorrect": "The difference is entirely about power draw rate. Gaming demands maximum output from both the display (2-3 watts) and processor (3-5 watts) simultaneously, totaling 5-8 watts. Standby uses only 0.1-0.3 watts for basic radio operations. The same battery drains proportionally faster at higher power draw."
        },
        {
            "question": "A two-year-old phone has noticeably worse battery life than when it was new, even with the same usage patterns. What is the most likely explanation?",
            "choices": {
                "A": "The phone's software has become heavier and requires more energy",
                "B": "Repeated charge-discharge cycles have degraded the battery's chemical structure, reducing its total energy storage capacity",
                "C": "The phone's screen has become less efficient over time",
                "D": "Electromagnetic interference from nearby devices drains the battery faster"
            },
            "correct": "B",
            "feedback_correct": "Correct. Lithium-ion batteries degrade through repeated charge cycles. The electrode materials develop microscopic cracks, and a growing SEI layer permanently traps lithium ions. After approximately 500 full cycles, most batteries retain only about 80% of their original capacity.",
            "feedback_incorrect": "Battery degradation is a chemical process. Each charge-discharge cycle causes microscopic structural damage to electrode materials and growth of the SEI (solid electrolyte interphase) layer, which permanently traps lithium ions. This reduces the total amount of energy the battery can store, even though the phone's power consumption remains the same."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In a phone energy model, a student observes that increasing Processing Load from LOW to HIGH increases both Battery Drain and Heat Generation. However, Heat Generation increases at a faster rate than useful computation output. What principle explains this observation?",
            "choices": {
                "A": "The processor deliberately generates extra heat to improve performance",
                "B": "At higher processing loads, energy conversion efficiency decreases because more transistor switching events produce proportionally more waste heat through electrical resistance",
                "C": "The phone heats up only because of the screen, not the processor",
                "D": "Heat generation is unrelated to processing load and is caused by battery chemistry"
            },
            "correct": "B",
            "feedback_correct": "Correct. At higher processing loads, the CPU/GPU performs billions of additional transistor switching events per second. Each switching event generates a small amount of waste heat through Joule heating (electrical resistance). The cumulative effect means heat generation scales disproportionately with processing intensity, reducing overall efficiency.",
            "feedback_incorrect": "The model shows that higher processing demands create disproportionately more waste heat because each additional transistor switching event produces its own small heat contribution. As billions of additional operations occur per second, the cumulative heat output increases faster than the useful computational output, reducing overall energy efficiency."
        },
        {
            "question": "A student runs the 'Brightness Test' scenario, keeping Processing Load at MEDIUM while increasing Screen Brightness from LOW to HIGH. The model shows that the screen alone accounts for the largest single battery drain. What design trade-off does this reveal?",
            "choices": {
                "A": "Phone screens should always be at minimum brightness to maximize battery life",
                "B": "Screen brightness represents a direct trade-off between user experience (visibility) and energy consumption, requiring adaptive management to balance both",
                "C": "Screen brightness has no impact on battery life in modern phones",
                "D": "Processing load is always more important than screen brightness for battery life"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that screen brightness is often the single largest energy consumer, but visibility is essential for user experience. This creates a design trade-off that engineers address through adaptive brightness systems that adjust output based on ambient light, maximizing visibility while minimizing unnecessary energy waste.",
            "feedback_incorrect": "The model data shows that screen brightness is a major energy consumer that directly trades off against battery life. However, turning it to minimum is not practical. Engineers address this through adaptive brightness technology that adjusts screen output to match ambient lighting conditions, providing adequate visibility without wasting energy."
        },
        {
            "question": "A phone battery stores 15.4 Wh of energy. During gaming, the screen draws 2.5 W, the processor draws 3.0 W, and 0.8 W is dissipated as heat. What is the total power draw and approximately how long will the battery last?",
            "choices": {
                "A": "Total: 5.5 W; battery life: approximately 2.8 hours",
                "B": "Total: 6.3 W; battery life: approximately 2.4 hours",
                "C": "Total: 3.3 W; battery life: approximately 4.7 hours",
                "D": "Total: 0.8 W; battery life: approximately 19.3 hours"
            },
            "correct": "B",
            "feedback_correct": "Correct. Total power draw = 2.5 W + 3.0 W + 0.8 W = 6.3 W. Battery life = 15.4 Wh / 6.3 W = approximately 2.4 hours. Note that the 0.8 W heat is NOT separate from the battery drain. It IS battery energy being wasted, reducing both efficiency and battery life.",
            "feedback_incorrect": "Total power draw includes ALL energy pathways: screen (2.5 W) + processor (3.0 W) + heat (0.8 W) = 6.3 W total. Battery life = energy stored / power draw = 15.4 Wh / 6.3 W = 2.4 hours. The heat generation is wasted battery energy that must be included in the total draw calculation."
        },
        {
            "question": "A student extends their model by adding a Battery Age component. They discover that after 500 charge cycles, the same gaming session that lasted 2.4 hours on a new battery now lasts only 1.9 hours. What does this reveal about the relationship between battery chemistry and user experience?",
            "choices": {
                "A": "The phone is using more power because it has become less efficient with age",
                "B": "The battery's chemical degradation reduces stored energy capacity while power consumption remains constant, meaning identical usage produces shorter battery life over the device's lifespan",
                "C": "Older phones automatically increase screen brightness, causing faster drain",
                "D": "Battery age only affects standby time, not active usage time"
            },
            "correct": "B",
            "feedback_correct": "Correct. Battery degradation reduces the numerator (stored energy) while the denominator (power draw) remains unchanged. A battery retaining 80% capacity after 500 cycles stores 12.3 Wh instead of 15.4 Wh, but the phone still draws 6.3 W during gaming, resulting in proportionally shorter battery life (12.3 / 6.3 = 1.95 hours).",
            "feedback_incorrect": "Battery aging reduces the total energy stored (capacity) through chemical degradation, but the phone's energy consumption stays the same. With only 80% of original capacity remaining, the same gaming session drains the smaller energy reserve faster. The user experiences this as shorter battery life despite identical usage patterns."
        },
        {
            "question": "Based on their model, a student designs a power management plan for an 8-hour school day. Which strategy best applies the energy conversion principles from the model?",
            "choices": {
                "A": "Close all background apps every hour, since they are the primary battery drain",
                "B": "Schedule high-power activities (video, gaming) during specific windows and maintain low brightness and minimal processing during class time, budgeting total energy expenditure across the day",
                "C": "Keep the phone plugged into a charger at all times to maintain 100% battery",
                "D": "Turn the phone completely off except during lunch break"
            },
            "correct": "B",
            "feedback_correct": "Correct. This strategy applies the model's key finding: power draw varies enormously between use cases (0.2 W standby to 6+ W gaming). By scheduling high-power activities into specific windows and maintaining low-power settings otherwise, total energy expenditure can be budgeted to match available battery capacity across the full day.",
            "feedback_incorrect": "Effective power management applies the model insight that different activities draw vastly different amounts of power. By concentrating high-power activities into planned windows and maintaining low-power settings during class time, the total energy budget can be spread across 8 hours. Closing background apps actually wastes energy because reopening them requires more processing than leaving them suspended."
        }
    ]
}

# ── L05: The Ocean Is Turning to Acid ───────────────────────────────

L05_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "The pH scale measures acidity on a scale from 0 to 14. Ocean water has decreased from pH 8.2 to pH 8.1 since the Industrial Revolution. A student says this change is 'basically nothing.' Why is this assessment scientifically incorrect?",
            "choices": {
                "A": "Any pH change in any system is always catastrophic",
                "B": "The pH scale is logarithmic, so a 0.1-unit change represents approximately a 30% increase in hydrogen ion concentration",
                "C": "The pH scale only goes from 0 to 7, so 0.1 out of 7 is significant",
                "D": "Ocean pH should be exactly 7.0, so any deviation is a problem"
            },
            "correct": "B",
            "feedback_correct": "Correct. Because pH is a logarithmic scale (each unit represents a 10x change), a 0.1-unit decrease represents approximately a 26-30% increase in hydrogen ion concentration. For organisms that evolved over millions of years in stable pH conditions, this rate of change is biologically significant.",
            "feedback_incorrect": "The pH scale is logarithmic, meaning each whole unit represents a 10-fold change in hydrogen ion concentration. A drop of 0.1 units means a roughly 30% increase in acidity. This may seem small on a linear scale, but marine organisms evolved in extremely stable pH conditions, and a 30% shift in their chemical environment causes measurable biological damage."
        },
        {
            "question": "Approximately what percentage of human CO2 emissions does the ocean absorb?",
            "choices": {
                "A": "Less than 1%",
                "B": "About 10%",
                "C": "About 30%",
                "D": "About 90%"
            },
            "correct": "C",
            "feedback_correct": "Correct. The ocean absorbs approximately 30% of atmospheric CO2 emissions, making it a massive carbon sink. However, this absorption service comes at the cost of changing ocean chemistry through acidification.",
            "feedback_incorrect": "The ocean absorbs approximately 30% of the CO2 that humans emit into the atmosphere. This absorption has helped slow atmospheric warming but has fundamentally changed ocean chemistry, producing carbonic acid that lowers pH."
        },
        {
            "question": "Coral reefs and shellfish build their structures from calcium carbonate (CaCO3). How might increased ocean acidity affect these organisms?",
            "choices": {
                "A": "Increased acidity strengthens calcium carbonate structures",
                "B": "Acidic water dissolves calcium carbonate, threatening the structural integrity of shells and coral skeletons",
                "C": "Ocean acidity has no effect on calcium carbonate because it is a mineral, not a living tissue",
                "D": "Coral and shellfish can switch to building their structures from alternative materials"
            },
            "correct": "B",
            "feedback_correct": "Correct. Calcium carbonate dissolves in acidic conditions. As ocean pH drops, the rate of dissolution increases while the organisms' ability to build new shell material decreases, creating a double threat to their structural survival.",
            "feedback_incorrect": "Calcium carbonate is an acid-soluble compound. In more acidic ocean water, existing shells and coral skeletons dissolve faster, while the reduced availability of carbonate ions makes it harder for organisms to build new structures. Below a critical pH threshold, dissolution exceeds construction."
        },
        {
            "question": "A student asks: 'If CO2 is a natural part of the atmosphere, how can it be harmful to the ocean?' Which response best addresses this question?",
            "choices": {
                "A": "CO2 is not natural; it is entirely a human-created pollutant",
                "B": "The issue is not CO2 itself but the unprecedented rate of increase; humans have raised atmospheric CO2 by 50% in 150 years, far faster than ocean chemistry can adapt",
                "C": "CO2 is always harmful in any concentration",
                "D": "Natural CO2 is different from human-produced CO2 at the molecular level"
            },
            "correct": "B",
            "feedback_correct": "Correct. CO2 is natural and essential for photosynthesis. The problem is the rate: atmospheric CO2 was stable at ~280 ppm for 10,000 years before humans raised it to 420+ ppm in just 150 years. Natural CO2 cycling takes thousands of years; the ocean cannot adapt to changes this rapid.",
            "feedback_incorrect": "CO2 is chemically identical whether natural or human-produced. The critical issue is the unprecedented rate of increase. The ocean can absorb and process CO2 gradually over thousands of years. Human emissions have increased atmospheric CO2 by 50% in just 150 years, overwhelming the ocean's ability to adapt."
        },
        {
            "question": "Which of the following best explains how burning gasoline in a car can affect coral reefs thousands of miles away?",
            "choices": {
                "A": "Gasoline fumes travel through the air and directly contact coral reefs",
                "B": "CO2 from combustion enters the atmosphere, dissolves into ocean surface water globally, forms carbonic acid that lowers pH, and the acidified water dissolves coral's calcium carbonate structures",
                "C": "Car exhaust creates acid rain that falls directly on coral reefs",
                "D": "The vibrations from car engines travel through the Earth's crust and damage coral"
            },
            "correct": "B",
            "feedback_correct": "Correct. This traces the complete pathway: combustion produces CO2, CO2 mixes into the global atmosphere, approximately 30% dissolves into ocean surface water, dissolved CO2 reacts with water to form carbonic acid, the acid releases hydrogen ions that lower pH, and lower pH dissolves calcium carbonate structures that corals and shellfish depend on.",
            "feedback_incorrect": "The pathway from car to coral is: burning gasoline produces CO2, which enters the atmosphere and mixes globally. About 30% of atmospheric CO2 dissolves into ocean surface water. When CO2 meets seawater, it forms carbonic acid, which releases hydrogen ions that lower ocean pH. This more acidic water dissolves the calcium carbonate structures of corals and shellfish."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In a student's ocean acidification model, the 'Zero Emissions' scenario shows that ocean pH continues to decrease for several decades even after CO2 emissions stop completely. Which mechanism best explains this model behavior?",
            "choices": {
                "A": "The model has an error because stopping emissions should immediately stop acidification",
                "B": "Existing atmospheric CO2 (currently at 420+ ppm) continues dissolving into the ocean for decades, and deep ocean circulation operates on millennial timescales, preventing rapid recovery",
                "C": "The ocean produces its own CO2 through volcanic activity on the seafloor",
                "D": "Marine organisms release CO2 when they die, creating a separate acidification pathway"
            },
            "correct": "B",
            "feedback_correct": "Correct. Even at zero emissions, the 420+ ppm of CO2 already in the atmosphere continues dissolving into ocean surface water. Additionally, the deep ocean, which contains 90% of ocean water, mixes with surface water through thermohaline circulation that takes 500-1,000 years per cycle. Full pH recovery would take tens of thousands of years.",
            "feedback_incorrect": "The lag effect exists because stopping emissions does not remove CO2 already in the atmosphere. The existing 420+ ppm continues to dissolve into the ocean. Furthermore, the deep ocean mixes with the surface on timescales of centuries to millennia, meaning acidification spreads throughout the entire ocean volume long after surface emissions stop."
        },
        {
            "question": "A student traces a carbon atom from a car's gasoline tank to a dissolved acid molecule in the ocean. Which sequence correctly represents the conservation of matter through this process?",
            "choices": {
                "A": "Carbon is destroyed during combustion and recreated in the ocean",
                "B": "C in gasoline (C8H18) → CO2 from combustion → CO2 dissolves in seawater → H2CO3 (carbonic acid) → H+ ions that lower pH",
                "C": "Carbon in gasoline converts to nitrogen in the atmosphere, then to acid in the ocean",
                "D": "Carbon atoms change into hydrogen atoms when they enter the ocean"
            },
            "correct": "B",
            "feedback_correct": "Correct. This sequence demonstrates conservation of mass: the carbon atom in the hydrocarbon fuel is oxidized to CO2 during combustion, the CO2 molecule dissolves into seawater intact, then reacts with water to form carbonic acid (H2CO3), which dissociates to release H+ ions. The carbon atom is conserved throughout every transformation.",
            "feedback_incorrect": "Atoms are conserved in all chemical reactions. The carbon atom in gasoline becomes part of CO2 during combustion, the CO2 dissolves into seawater, reacts with water to form carbonic acid (H2CO3), which then dissociates to release hydrogen ions (H+) that lower pH. The same carbon atom is present at every stage, just in different molecular arrangements."
        },
        {
            "question": "A policy advisor claims: 'The ocean is cleaning up our CO2 for free.' Using evidence from the model, which response best evaluates this statement?",
            "choices": {
                "A": "This statement is accurate because the ocean absorbs CO2 without any negative consequences",
                "B": "This statement is dangerously misleading because the ocean's CO2 absorption service comes at the enormous cost of acidification, which is destroying marine ecosystems worth billions of dollars in ecological services",
                "C": "This statement is incorrect because the ocean does not absorb any CO2",
                "D": "This statement is correct but incomplete; the ocean charges a small fee through slightly warmer water"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that ocean CO2 absorption is not 'free.' The payment is a fundamental change in ocean chemistry that dissolves coral reefs (supporting 25% of marine species), damages shellfish populations, and threatens food chains. The economic value of these ecosystem services is estimated in the trillions of dollars.",
            "feedback_incorrect": "The model clearly shows that ocean CO2 absorption has an enormous hidden cost: acidification. While the ocean has absorbed 30% of human emissions (slowing atmospheric warming), this service is destroying coral reefs that support 25% of all marine species, threatening shellfish at the base of food chains, and fundamentally altering ocean chemistry. The 'service' is anything but free."
        },
        {
            "question": "Comparing the 'Current Trajectory' and 'Paris Agreement' scenarios, a student finds that the Paris scenario still shows significant pH decline, just at a slower rate. What is the most important policy implication of this finding?",
            "choices": {
                "A": "The Paris Agreement targets are sufficient to protect marine ecosystems",
                "B": "Emission reduction slows acidification but does not stop it, meaning even ambitious emission cuts must be combined with other interventions to protect vulnerable marine ecosystems in the near term",
                "C": "The Paris Agreement should be abandoned because it doesn't solve acidification",
                "D": "Ocean acidification is not a real concern because it happens slowly"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that emission reduction changes the rate of acidification but cannot stop it in the near term because of the lag effect from existing atmospheric CO2. This means marine ecosystem protection requires both emission reduction (addressing the cause) AND near-term interventions like marine protected areas (addressing the symptoms).",
            "feedback_incorrect": "The model reveals that even under Paris Agreement targets, acidification continues because existing atmospheric CO2 keeps dissolving. This does not mean emission reduction is pointless; it dramatically reduces the long-term severity. But it does mean that protecting vulnerable ecosystems like coral reefs requires a dual strategy: reducing emissions AND implementing near-term protective measures."
        },
        {
            "question": "A student adds a 'Biological Buffering' component to their model, representing how healthy marine ecosystems (seagrasses, kelp forests) can partially buffer pH changes through photosynthesis. The model shows that destroying these ecosystems accelerates acidification. What systems thinking principle does this demonstrate?",
            "choices": {
                "A": "Biological buffering is irrelevant to ocean chemistry",
                "B": "Removing a natural negative feedback mechanism (biological buffering) accelerates the system's shift away from stability, demonstrating how ecosystem destruction compounds the chemical problem",
                "C": "Marine plants cause acidification by producing CO2 during respiration",
                "D": "Adding components to models always produces the same results"
            },
            "correct": "B",
            "feedback_correct": "Correct. Healthy marine vegetation absorbs CO2 during photosynthesis, providing a local buffering effect that partially counteracts acidification. Destroying these ecosystems removes this natural negative feedback, causing pH to drop faster. This demonstrates how interconnected systems can compound problems when multiple stressors act simultaneously.",
            "feedback_incorrect": "Marine plants act as a natural buffer by absorbing CO2 through photosynthesis, locally raising pH. When these ecosystems are destroyed (through pollution, development, or the acidification itself), the buffering capacity is lost, and pH drops faster. This shows how removing natural feedback mechanisms from a system accelerates destabilization."
        }
    ]
}

# ── L06: Why Some People Can't Drink Milk ───────────────────────────

L06_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Which of the following best describes the function of an enzyme in a biological system?",
            "choices": {
                "A": "Enzymes provide energy for cellular processes by breaking down ATP",
                "B": "Enzymes are proteins that speed up specific chemical reactions without being consumed in the process",
                "C": "Enzymes are carbohydrates that store genetic information",
                "D": "Enzymes are lipids that form the cell membrane"
            },
            "correct": "B",
            "feedback_correct": "Correct. Enzymes are biological catalysts, proteins that lower the activation energy of specific chemical reactions, allowing them to proceed much faster. Each enzyme is specific to a particular substrate, and the enzyme itself is not consumed or altered permanently by the reaction.",
            "feedback_incorrect": "Enzymes are proteins that function as biological catalysts. They speed up specific chemical reactions by lowering the activation energy required, and they are not consumed in the process. Each enzyme has a specific shape that fits only certain substrates, giving it high specificity."
        },
        {
            "question": "What does it mean when scientists say a gene is 'expressed'?",
            "choices": {
                "A": "The gene has been deleted from the DNA sequence",
                "B": "The gene's information is being actively read and used to produce a functional protein",
                "C": "The gene is present in the DNA but has no function",
                "D": "The gene has mutated into a different form"
            },
            "correct": "B",
            "feedback_correct": "Correct. Gene expression is the process by which the information encoded in a gene is used to synthesize a functional protein. This involves transcription (DNA to mRNA) and translation (mRNA to protein). A gene that is 'expressed' is actively producing its protein product.",
            "feedback_incorrect": "Gene expression refers to the process where a gene's DNA sequence is transcribed into mRNA and then translated into a functional protein. When a gene is expressed, the cell is actively using that gene's instructions to make a specific protein. Genes can be 'turned on' (expressed) or 'turned off' (silenced)."
        },
        {
            "question": "A student says: 'Lactose intolerance is a disease that some people are born with.' Which correction is most scientifically accurate?",
            "choices": {
                "A": "Lactose intolerance is caused by a virus, not genetics",
                "B": "Lactose intolerance is not a disease; it is the ancestral default human condition where lactase production naturally decreases after childhood",
                "C": "Lactose intolerance only develops in people who drink too much milk",
                "D": "Lactose intolerance and lactose allergy are the same condition"
            },
            "correct": "B",
            "feedback_correct": "Correct. Lactase non-persistence (commonly called lactose intolerance) is the ancestral human condition shared by all mammals. Lactase production naturally decreases after weaning. Lactose tolerance is actually the mutation, arising approximately 7,500 years ago in dairy-farming populations.",
            "feedback_incorrect": "Lactose intolerance is not a disease or disorder. It is the default condition for most mammals, including most humans. All mammals naturally reduce lactase production after weaning because there is no nutritional need for it. Lactose tolerance in adults is the genetic mutation, which evolved approximately 7,500 years ago in populations that domesticated dairy animals."
        },
        {
            "question": "Approximately what percentage of the world's adult population is lactose intolerant?",
            "choices": {
                "A": "About 5%",
                "B": "About 25%",
                "C": "About 65%",
                "D": "About 95%"
            },
            "correct": "C",
            "feedback_correct": "Correct. Approximately 65-70% of the world's adult population has reduced lactase production after childhood. The distribution varies dramatically by region, with rates over 90% in East Asia and under 10% in Northern Europe, reflecting historical dairy farming practices.",
            "feedback_incorrect": "About 65% of the global adult population experiences reduced lactase production. This varies significantly by ancestry: over 90% in East Asian populations, 70-80% in African and Latin American populations, and under 10% in Northern European populations, closely tracking the history of dairy farming in different regions."
        },
        {
            "question": "When a lactose-intolerant person drinks milk, they often experience bloating, cramps, and diarrhea. What is the direct biological cause of these symptoms?",
            "choices": {
                "A": "The immune system attacks the milk proteins, causing an allergic reaction",
                "B": "Undigested lactose passes to the large intestine where bacteria ferment it, producing gas, and the lactose draws water in through osmosis",
                "C": "Milk contains toxins that are only harmful to certain people",
                "D": "The stomach acid reacts with milk to produce a corrosive substance"
            },
            "correct": "B",
            "feedback_correct": "Correct. Without sufficient lactase in the small intestine, lactose passes undigested to the large intestine. Gut bacteria ferment the lactose anaerobically, producing hydrogen, methane, and CO2 gas (causing bloating and cramps). The undigested lactose is also osmotically active, drawing water into the intestinal lumen (causing diarrhea).",
            "feedback_incorrect": "Lactose intolerance is not an immune response (that would be a milk allergy, which is different). The symptoms occur because undigested lactose reaches the large intestine, where bacteria ferment it to produce gas (bloating, cramps) and where its osmotic activity draws water into the gut (diarrhea)."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In a student's model, setting Lactase Gene Activity to MEDIUM produces a scenario where small amounts of dairy cause no symptoms but large amounts cause significant discomfort. Which concept does this model behavior best demonstrate?",
            "choices": {
                "A": "Enzymes work in an all-or-nothing fashion with no intermediate states",
                "B": "There is a threshold effect where limited enzyme can process a small substrate load but is overwhelmed by a large one, meaning intolerance exists on a spectrum rather than as a binary condition",
                "C": "The model is inaccurate because lactose intolerance is always complete",
                "D": "Medium gene activity means the person is allergic to some dairy products but not others"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals a threshold effect: limited lactase enzyme can successfully break down small amounts of lactose before it reaches the colon. But when lactose intake exceeds the enzyme's processing capacity, the excess passes to the large intestine and causes symptoms. This explains why many intolerant people can eat aged cheese or yogurt but not drink a full glass of milk.",
            "feedback_incorrect": "The model demonstrates that lactose intolerance is not binary but exists on a spectrum determined by the ratio of available enzyme to consumed lactose. At medium gene activity, there is enough lactase to process small amounts, but large dairy servings overwhelm the available enzyme, with excess lactose passing to the colon to be fermented by bacteria."
        },
        {
            "question": "A student's model traces the causal chain: Lactase Gene Activity → Lactase Enzyme Production → Lactose Breakdown → Gut Bacteria Response. If two siblings eat identical ice cream sundaes but only one gets sick, which part of the chain most likely differs between them?",
            "choices": {
                "A": "They have different gut bacteria species, which is the primary variable",
                "B": "Their Lactase Gene Activity levels differ due to inherited genetic variation in LCT gene regulation, causing different amounts of enzyme to be produced",
                "C": "One sibling has a stronger stomach that destroys lactose before it reaches the intestine",
                "D": "The ice cream affected them differently because of their blood types"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model identifies Lactase Gene Activity as the primary driver of the entire causal chain. Siblings can inherit different regulatory variants of the LCT gene from their parents, resulting in different levels of lactase enzyme production and therefore different digestive outcomes from the same dairy intake.",
            "feedback_incorrect": "The model shows that the entire downstream chain depends on the initial gene activity level. Since siblings can inherit different combinations of LCT gene regulatory variants from their parents, they may have different levels of lactase production. The sibling with lower gene activity produces less enzyme, leading to more undigested lactose reaching gut bacteria."
        },
        {
            "question": "About 90% of Northern Europeans are lactose tolerant while 90% of East Asian populations are intolerant. A student's model of gene expression and natural selection best explains this pattern through which mechanism?",
            "choices": {
                "A": "Northern Europeans evolved a completely different digestive system from East Asians",
                "B": "A mutation that kept the LCT gene active into adulthood provided a strong survival advantage in dairy-farming populations, spreading rapidly through natural selection over approximately 7,500 years",
                "C": "East Asian populations lost the ability to digest milk due to lack of exercise",
                "D": "Northern Europeans drink more milk during childhood, which permanently activates the gene"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is gene-culture co-evolution: the cultural practice of dairy farming created strong selective pressure favoring a mutation that maintains lactase production into adulthood. Populations without dairy farming traditions had no selective advantage for this mutation. The geographic distribution of lactose tolerance maps almost perfectly onto the history of dairy cattle domestication.",
            "feedback_incorrect": "The pattern reflects gene-culture co-evolution. Approximately 7,500 years ago, a mutation arose that prevents the normal age-related decrease in LCT gene expression. In populations that domesticated dairy animals, this mutation provided access to a rich, reliable food source, conferring a strong survival advantage. Natural selection rapidly spread this mutation. Populations without dairy farming traditions experienced no selective pressure for the mutation."
        },
        {
            "question": "A food scientist uses the model to design a lactose-free milk product. They add microbial lactase enzyme to milk during processing. Based on the model, why does this approach work?",
            "choices": {
                "A": "The added enzyme destroys the milk protein that causes allergic reactions",
                "B": "The added enzyme changes the person's gene expression permanently",
                "C": "The added enzyme performs the same lactose-to-glucose/galactose breakdown reaction externally that the body's own lactase would perform in the small intestine, eliminating the substrate before gut bacteria encounter it",
                "D": "The added enzyme kills the gut bacteria that cause symptoms"
            },
            "correct": "C",
            "feedback_correct": "Correct. The model shows that symptoms occur when undigested lactose reaches gut bacteria. Adding lactase to milk during processing breaks down lactose before the person ever drinks it, effectively performing the chemical reaction outside the body. The result is milk that contains glucose and galactose instead of lactose, which the body absorbs normally without any enzyme requirement.",
            "feedback_incorrect": "The model reveals that the critical step is lactose breakdown. Whether this happens via the person's own lactase in the small intestine or via externally added enzyme during milk processing, the result is the same: lactose is converted to absorbable glucose and galactose. Without intact lactose reaching the large intestine, there is nothing for bacteria to ferment, and no symptoms occur."
        },
        {
            "question": "A student reflects on their model and states: 'This is one of the clearest examples of how a single gene directly controls a physical trait through a protein intermediary.' Which reasoning best supports this claim?",
            "choices": {
                "A": "Many genes contribute to lactose digestion, so a single-gene model is oversimplified",
                "B": "The causal chain from DNA sequence (LCT gene) → mRNA → protein (lactase enzyme) → chemical reaction (lactose hydrolysis) → observable phenotype (digestion vs. symptoms) traces the central dogma of molecular biology through a single, verifiable example",
                "C": "Gene expression does not actually control protein production",
                "D": "The trait of lactose tolerance is controlled by environmental factors, not genetics"
            },
            "correct": "B",
            "feedback_correct": "Correct. Lactose tolerance/intolerance is an unusually clear example of the central dogma pathway from gene to phenotype. A single gene (LCT) is transcribed to mRNA, translated to a specific protein (lactase enzyme), which catalyzes a specific reaction (lactose hydrolysis), producing an observable physical outcome (comfortable digestion vs. gastrointestinal distress). Every link in the chain is well-characterized.",
            "feedback_incorrect": "This example elegantly demonstrates the central dogma of molecular biology in action: DNA (LCT gene regulation) determines mRNA levels, mRNA determines protein (lactase enzyme) quantity, enzyme quantity determines the rate of a specific chemical reaction (lactose breakdown), and the completeness of that reaction determines the observable phenotype (digestion vs. symptoms). Each step is directly traceable."
        }
    ]
}

# ── L07: How Social Media Hacks Your Brain ──────────────────────────

L07_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Dopamine is a neurotransmitter often associated with reward and pleasure. Which statement most accurately describes dopamine's role in the brain?",
            "choices": {
                "A": "Dopamine directly causes feelings of happiness and contentment",
                "B": "Dopamine signals anticipation of reward and reinforces behaviors that triggered its release, motivating repetition of those behaviors",
                "C": "Dopamine is only released during physical exercise",
                "D": "Dopamine is a hormone that controls sleep cycles"
            },
            "correct": "B",
            "feedback_correct": "Correct. Dopamine functions primarily as a reward-prediction signal, not just a pleasure chemical. It is released in anticipation of a potential reward and reinforces the neural pathways associated with the behavior that preceded the reward, making you more likely to repeat that behavior.",
            "feedback_incorrect": "Dopamine is more accurately described as a reward-anticipation and reinforcement signal rather than a simple pleasure chemical. It is released when the brain anticipates a potential reward and strengthens the neural connections associated with the behavior that preceded the reward, driving future repetition of that behavior."
        },
        {
            "question": "Slot machines are designed so that payouts occur at random, unpredictable intervals. Why is this pattern more addictive than receiving a reward every time?",
            "choices": {
                "A": "Random rewards are always larger in value than predictable ones",
                "B": "Unpredictable reward timing keeps the brain in a constant state of anticipation, generating more dopamine than predictable rewards because each attempt might be the big payoff",
                "C": "Predictable rewards are boring because humans only enjoy surprises",
                "D": "Random rewards trick people into thinking they are winning more often than they actually are"
            },
            "correct": "B",
            "feedback_correct": "Correct. Variable ratio reinforcement schedules produce the highest and most persistent engagement because the brain remains in a state of anticipatory dopamine release. Each attempt could be rewarded, maintaining the motivation to continue. The brain actually releases more dopamine during anticipation than during the reward itself.",
            "feedback_incorrect": "Variable (unpredictable) reward schedules are the most addictive pattern because the brain maintains a constant state of anticipation. The uncertainty about when the next reward will arrive keeps dopamine levels elevated, and the brain releases more dopamine during anticipation of a possible reward than during the actual reward delivery."
        },
        {
            "question": "A student reports feeling worse about themselves after spending two hours scrolling through Instagram. Which psychological mechanism best explains this experience?",
            "choices": {
                "A": "The blue light from the screen directly causes depression",
                "B": "Social comparison with curated, idealized content makes the student perceive their own life as less attractive, successful, or exciting by comparison",
                "C": "Instagram sends subliminal messages that make users feel bad",
                "D": "Two hours is not enough time for social media to affect mood"
            },
            "correct": "B",
            "feedback_correct": "Correct. Social comparison theory explains that humans evaluate themselves by comparing to others. On social media, users compare their unfiltered daily reality to others' curated highlight reels, consistently producing unfavorable comparisons that erode self-esteem and life satisfaction.",
            "feedback_incorrect": "Social comparison theory describes our innate tendency to evaluate ourselves against others. Social media amplifies this by presenting curated, filtered, idealized versions of other people's lives. When you compare your authentic daily experience to someone else's carefully constructed highlight reel, the comparison consistently makes you feel worse about yourself."
        },
        {
            "question": "The human brain continues developing until approximately age 25, with the prefrontal cortex being one of the last regions to mature. Why does this make adolescents particularly vulnerable to social media's addictive design?",
            "choices": {
                "A": "Adolescents have smaller brains that cannot process social media content",
                "B": "The prefrontal cortex, which controls impulse regulation and long-term decision-making, is not yet fully developed in teenagers, while the reward system (dopamine pathways) is fully active",
                "C": "Adolescents are not actually more vulnerable than adults to social media addiction",
                "D": "The prefrontal cortex controls vision, which makes teens see social media differently"
            },
            "correct": "B",
            "feedback_correct": "Correct. There is an imbalance in adolescent brain development: the dopamine reward system is fully functional and highly responsive, while the prefrontal cortex (responsible for impulse control, delayed gratification, and risk assessment) is still maturing. This creates a neurological vulnerability where teens can experience the full addictive pull of variable rewards without the fully developed capacity to resist it.",
            "feedback_incorrect": "Adolescent vulnerability stems from a developmental imbalance: the brain's reward circuitry (dopamine pathways) is fully active and highly responsive to social stimuli, while the prefrontal cortex, which provides impulse control and long-term decision-making, is still developing. This means teens experience the full addictive pull without the neurological brakes that adults have."
        },
        {
            "question": "A student claims: 'I use social media because I choose to. It's completely my decision.' Which counterargument best challenges this claim using neuroscience evidence?",
            "choices": {
                "A": "Social media is controlled by the government, so no one truly chooses to use it",
                "B": "While the initial download is a choice, continued use is heavily influenced by design features (variable rewards, infinite scroll, notification timing) specifically engineered to bypass conscious decision-making and exploit the dopamine system",
                "C": "Teenagers are incapable of making any real choices",
                "D": "Social media is perfectly safe and does not influence behavior at all"
            },
            "correct": "B",
            "feedback_correct": "Correct. Social media platforms employ teams of behavioral psychologists to optimize features like variable notification timing, infinite scroll, autoplay, and algorithmic content delivery. These are specifically designed to maximize engagement by exploiting the brain's reward pathways, operating below the level of conscious decision-making.",
            "feedback_incorrect": "The initial choice to use social media is genuine, but the continued engagement is heavily shaped by design features engineered to exploit unconscious neurological processes. Variable reward schedules, infinite scroll, autoplay, and personalized notification timing are all optimized through A/B testing to maximize the time users spend on the platform, often bypassing conscious intention."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In a student's computational model, reducing Notification Frequency from HIGH to LOW decreases Dopamine Release, which decreases Screen Time, which decreases Social Comparison, which stabilizes Self-Esteem. What does this model output demonstrate about the system?",
            "choices": {
                "A": "Self-esteem is determined entirely by genetics and cannot be influenced by external factors",
                "B": "Controlling the entry point of the feedback loop (notifications) can disrupt the entire chain, because each downstream component depends on the one before it",
                "C": "Reducing notifications has no effect on dopamine because dopamine is released regardless of external stimuli",
                "D": "The model proves that social media has no negative effects"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that the feedback loop has a controllable entry point. By reducing notification frequency, the initial dopamine trigger is diminished, which reduces the behavioral response (screen time), which reduces the psychological exposure (social comparison), which stabilizes the outcome (self-esteem). Intervening early in the chain disrupts all downstream effects.",
            "feedback_incorrect": "The model reveals that the addictive loop has a single controllable entry point: notification frequency. Since each component in the chain depends on the previous one, reducing the initial stimulus (notifications) cascades through the entire system, reducing dopamine release, screen time, social comparison, and ultimately protecting self-esteem."
        },
        {
            "question": "A student's model shows that during the 'High Notifications' scenario, Screen Time continues to increase even after the student reports wanting to stop. The model predicts this behavior because:",
            "choices": {
                "A": "The phone physically prevents the user from putting it down",
                "B": "The positive feedback loop has become self-sustaining: dopamine-driven habits bypass conscious decision-making because neuroplasticity has physically rewired the brain's neural pathways to automate phone-checking behavior",
                "C": "The student does not actually want to stop and is lying about their intentions",
                "D": "Notification frequency has no relationship to screen time in the model"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model illustrates how a positive feedback loop becomes self-sustaining through neuroplasticity. Repeated dopamine-driven phone-checking physically strengthens the neural pathways associated with this behavior, eventually making it automatic and habitual. At this point, the behavior continues even when the conscious mind wants to stop, because the habit pathway bypasses deliberate decision-making.",
            "feedback_incorrect": "The model shows how positive feedback loops become self-sustaining. Through neuroplasticity, repeated phone-checking behavior physically strengthens the neural pathways involved, making the behavior increasingly automatic. Once the habit pathway is established, it operates below conscious control, which is why people report being unable to stop scrolling even when they consciously want to."
        },
        {
            "question": "Two students compare their models. Student A's model only includes Notifications → Dopamine → Screen Time. Student B's model adds Social Comparison → Self-Esteem, with low Self-Esteem feeding back to increase Screen Time (seeking validation). Which model better captures the addictive nature of social media?",
            "choices": {
                "A": "Student A's model is better because simpler models are always more accurate",
                "B": "Student B's model is more complete because it includes the self-reinforcing loop where decreased self-esteem drives users to seek MORE online validation, creating the positive feedback cycle that makes the system truly addictive",
                "C": "Both models are equally valid because they contain the same core mechanism",
                "D": "Neither model is useful because addiction cannot be modeled computationally"
            },
            "correct": "B",
            "feedback_correct": "Correct. Student B's model captures the critical self-reinforcing loop: social comparison erodes self-esteem, and low self-esteem drives users to seek validation online (more likes, followers, comments), which increases screen time and exposure to more comparison content. This positive feedback loop is what makes the system self-sustaining and difficult to escape.",
            "feedback_incorrect": "Student B's model more accurately represents the addictive dynamic because it includes the feedback loop where the output (reduced self-esteem) becomes an input (seeking online validation). This creates a self-reinforcing cycle where each pass through the loop intensifies the next, making the behavior progressively harder to stop. Student A's model shows the initial pathway but misses this critical self-perpetuating mechanism."
        },
        {
            "question": "A student designs a digital wellness app that detects when a user has been scrolling for 30 minutes and suggests they message a real friend instead. Which neuroscience principle from the model does this intervention apply?",
            "choices": {
                "A": "Eliminating dopamine from the brain entirely",
                "B": "Habit replacement theory: the intervention redirects the social connection need from passive scrolling (which triggers comparison) to active social engagement (which satisfies the underlying need without the harmful comparison cycle)",
                "C": "Forcing the user to stop using their phone completely",
                "D": "Increasing notification frequency to overwhelm the dopamine system"
            },
            "correct": "B",
            "feedback_correct": "Correct. Neuroscience shows that habits cannot simply be deleted; they must be replaced with alternative behaviors that satisfy the same underlying need. The need for social connection can be met through direct messaging (without the comparison content of feeds). This redirects the behavior without fighting the fundamental human drive for social interaction.",
            "feedback_incorrect": "Habit replacement theory, supported by neuroscience, states that successful behavior change comes from redirecting the underlying need to a healthier alternative, not from eliminating the behavior entirely. The underlying need (social connection) is legitimate; the problem is that passive scrolling satisfies it through a pathway that includes harmful social comparison. Direct messaging satisfies the same need without the comparison element."
        },
        {
            "question": "After studying the model, a student argues: 'Social media companies are doing the same thing the tobacco industry did. They're designing products they know cause harm to maximize profit.' Evaluate this analogy using evidence from the model.",
            "choices": {
                "A": "The analogy is completely wrong because social media is nothing like tobacco",
                "B": "The analogy is supported by model evidence: both industries engineer products to exploit biological vulnerabilities (dopamine pathways / nicotine receptors), both use research to maximize addictive potential, and both have internal data showing harm to users that they continued to suppress",
                "C": "The analogy fails because social media is free while tobacco costs money",
                "D": "The analogy is exaggerated because social media has no documented negative health effects"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model supports this analogy on multiple levels: both industries target biological vulnerabilities (the dopamine reward system for social media, nicotine receptors for tobacco), both use behavioral research to maximize engagement/addiction, and both have demonstrated awareness of harm to users (Facebook's internal research showing Instagram's effect on teen mental health mirrors tobacco companies' suppressed cancer research). The mechanism of exploitation is remarkably parallel.",
            "feedback_incorrect": "The model provides strong evidence for this analogy. Both industries exploit specific biological vulnerabilities to create habit-forming products. Both conduct internal research on health effects and continue optimizing for engagement despite negative findings. Both use variable reinforcement to maximize compulsive behavior. Leaked internal documents from Meta (formerly Facebook) showed the company knew Instagram harmed teen mental health, paralleling tobacco industry suppression of cancer evidence."
        }
    ]
}

# ── L08: Fast Fashion Is Killing the Planet ─────────────────────────

L08_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "The average American throws away approximately 81.5 pounds of clothing per year. What is the primary driver of this high disposal rate?",
            "choices": {
                "A": "Clothing is manufactured to decompose quickly for environmental reasons",
                "B": "The fast fashion business model produces trendy, low-cost clothing designed to be frequently replaced rather than kept long-term",
                "C": "Americans have unusually large wardrobes compared to all other countries",
                "D": "Clothing donation programs encourage people to replace their wardrobes annually"
            },
            "correct": "B",
            "feedback_correct": "Correct. Fast fashion brands produce thousands of new styles weekly at extremely low prices, creating a business model based on rapid consumption and disposal. When a T-shirt costs $5, consumers treat it as disposable rather than a long-term investment, driving high disposal rates.",
            "feedback_incorrect": "The fast fashion business model is designed around rapid trend cycles and low prices. Brands like Shein release thousands of new styles daily, encouraging consumers to buy frequently and discard quickly. When garments are priced so low they feel disposable, that is exactly how they get treated."
        },
        {
            "question": "A single cotton T-shirt requires approximately 2,700 liters of water to produce. What stages of production contribute to this water footprint?",
            "choices": {
                "A": "Water is only used during the final washing stage before packaging",
                "B": "Cotton agriculture (irrigation), fabric dyeing, textile washing, and finishing processes all consume significant quantities of water throughout the supply chain",
                "C": "The water is only used for shipping the T-shirt across the ocean",
                "D": "Most of the water is used by consumers washing the shirt at home"
            },
            "correct": "B",
            "feedback_correct": "Correct. Water consumption occurs at multiple stages: growing cotton requires extensive irrigation, dyeing fabric is extremely water-intensive (the fashion industry is the second-largest freshwater polluter globally), and washing and finishing the textile adds additional water use before the product ever reaches the consumer.",
            "feedback_incorrect": "The water footprint of a T-shirt spans the entire production chain: cotton agriculture requires extensive irrigation (the largest share), fabric dyeing uses large volumes of water and chemicals, and washing and finishing processes add further consumption. The fashion industry is the second-largest polluter of fresh water globally."
        },
        {
            "question": "The fashion industry produces approximately 10% of global carbon emissions. Which comparison best puts this figure in perspective?",
            "choices": {
                "A": "This is a negligible amount compared to other industries",
                "B": "This exceeds the carbon emissions from all international flights and maritime shipping combined",
                "C": "This is the same as residential home heating globally",
                "D": "This represents only carbon from transportation of clothing"
            },
            "correct": "B",
            "feedback_correct": "Correct. The fashion industry's 10% share of global carbon emissions exceeds the combined emissions from all international aviation and maritime shipping. This carbon comes from every stage: petroleum-based synthetic fibers, energy-intensive manufacturing, global shipping, and methane from textile waste decomposition.",
            "feedback_incorrect": "The fashion industry's carbon footprint is larger than most people realize. At 10% of global emissions, it exceeds the combined emissions from all international flights and maritime shipping. The carbon is produced at every stage of the supply chain: raw material production, manufacturing, global transportation, and decomposition in landfills."
        },
        {
            "question": "A student argues: 'I donate all my old clothes, so my fashion consumption doesn't create waste.' What evidence most effectively challenges this claim?",
            "choices": {
                "A": "Donated clothes are always thrown away immediately by charities",
                "B": "Only 10-20% of donated clothing is sold domestically; the rest is exported to developing nations where up to 40% goes directly to landfills, often destroying local textile industries",
                "C": "Donation bins are illegal in most countries",
                "D": "Donating clothes is worse than throwing them away because of transportation emissions"
            },
            "correct": "B",
            "feedback_correct": "Correct. The reality of clothing donation is far from the popular perception. Most donated clothing is not worn again domestically. It is exported in massive bales to developing nations, where a large percentage arrives in such poor condition it goes straight to landfills. This practice also undermines local textile manufacturing in receiving countries.",
            "feedback_incorrect": "Clothing donation creates an illusion of sustainability. Only a small fraction of donated items are sold to new consumers domestically. The majority is exported to developing nations where much of it ends up in landfills, just in a different country. The environmental impact of production (water, carbon, chemicals) has already occurred regardless of how the garment is later disposed of."
        },
        {
            "question": "Why might the environmental cost of clothing not be reflected in its price tag?",
            "choices": {
                "A": "Environmental costs are always included in retail prices",
                "B": "The water pollution, carbon emissions, and waste disposal costs are externalities borne by communities and ecosystems rather than by the companies producing the clothing or the consumers purchasing it",
                "C": "There are no environmental costs associated with clothing production",
                "D": "Governments pay all environmental costs through tax revenue"
            },
            "correct": "B",
            "feedback_correct": "Correct. Environmental costs in the fashion industry are externalities, meaning they are imposed on third parties (communities near factories, ecosystems, future generations) rather than being included in the product price. The $5 T-shirt price reflects only the direct costs of materials, labor, and distribution, not the environmental damage.",
            "feedback_incorrect": "The low price of fast fashion exists because environmental costs are externalized. The water used for cotton irrigation, the chemicals dumped into rivers during dyeing, the carbon emitted during manufacturing, and the landfill space consumed by textile waste are all costs paid by communities, ecosystems, and future generations rather than by the companies or consumers."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In a student's fast fashion model, reducing Consumer Demand by 50% reduces ALL environmental outputs (textile waste, water consumption, and carbon emissions) roughly proportionally. Why does demand reduction have this comprehensive effect?",
            "choices": {
                "A": "Consumer demand is unrelated to environmental impact",
                "B": "Consumer demand drives production rate, and since water consumption, carbon emissions, and textile waste are all outputs of the production process, reducing the input (demand) proportionally reduces all outputs simultaneously",
                "C": "Reducing demand only affects textile waste, not water or carbon",
                "D": "The model oversimplifies by linking all outputs to a single input"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that consumer demand is the primary driver of the entire system. Production rate responds to demand, and all three environmental outputs (waste, water, carbon) are direct consequences of production. Reducing the input variable proportionally reduces all output variables because they are all products of the same production process.",
            "feedback_incorrect": "The model structure shows that demand drives production, and production simultaneously generates waste, consumes water, and emits carbon. Since all three environmental outputs are products of the same production process, reducing the input (consumer demand) proportionally reduces every output. This is why demand reduction is the single most effective intervention point."
        },
        {
            "question": "A student compares two interventions: (A) recycling 50% of textile waste and (B) reducing consumer demand by 50%. The model shows intervention B has a greater total environmental impact. Why?",
            "choices": {
                "A": "Recycling technology does not exist yet",
                "B": "Recycling addresses only the disposal stage, while demand reduction prevents environmental damage at the production stage, where the majority of water consumption, carbon emissions, and chemical pollution occur",
                "C": "Both interventions have identical environmental impact",
                "D": "Recycling actually increases carbon emissions"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that most environmental damage occurs during production (growing cotton, dyeing fabric, manufacturing, shipping), not during disposal. Recycling addresses only the waste output at the end of the lifecycle, while demand reduction prevents the production-stage impacts from occurring at all. Prevention is inherently more impactful than end-of-pipe treatment.",
            "feedback_incorrect": "The critical insight is that environmental damage is concentrated in the production phase. By the time a garment reaches the disposal stage, its water has already been consumed, its carbon already emitted, and its chemicals already discharged. Recycling can reduce waste going to landfills but cannot reverse the environmental damage that occurred during manufacturing. Reducing demand prevents that damage entirely."
        },
        {
            "question": "A clothing company claims to be 'carbon neutral' through purchasing carbon offsets. Using the model, which analysis best evaluates this claim?",
            "choices": {
                "A": "Carbon neutrality fully resolves the company's environmental impact",
                "B": "Carbon offsets may address one of the model's outputs (carbon emissions) but ignore textile waste, water consumption, chemical pollution, and microplastic release, which the model shows are equally significant environmental impacts",
                "C": "Carbon offsets are better than reducing production because they don't affect profits",
                "D": "The model shows that carbon is the only significant environmental output of the fashion industry"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model identifies multiple environmental output pathways from production. Carbon offsets potentially address only one (carbon emissions), leaving textile waste (92 million tons/year), water consumption (79 trillion liters/year), chemical pollution, and microplastic release completely unaddressed. The carbon neutral claim creates a misleading impression of comprehensive environmental responsibility.",
            "feedback_incorrect": "The model shows that the fashion industry's environmental impact includes multiple output pathways: carbon emissions, water consumption, textile waste, and chemical pollution. Carbon offsets, even if perfectly executed, address only one of these pathways. The remaining impacts continue unabated, making the 'carbon neutral' claim an incomplete and potentially misleading representation of the company's total environmental footprint."
        },
        {
            "question": "A student calculates the 'cost per wearing' of two shirts: a $5 fast fashion shirt worn 5 times ($1.00/wear) versus a $50 quality shirt worn 100 times ($0.50/wear). What does this analysis reveal about the economics of sustainable fashion?",
            "choices": {
                "A": "Cheap clothing is always more economical regardless of how long it lasts",
                "B": "When measured by cost per use rather than purchase price, higher-quality clothing can be more economical than fast fashion while generating far less environmental waste per wearing",
                "C": "Quality and price are unrelated in the clothing industry",
                "D": "Consumers should never consider price when making purchasing decisions"
            },
            "correct": "B",
            "feedback_correct": "Correct. Cost-per-wearing analysis reframes the economics of fashion. While the initial price of a quality garment is higher, dividing cost by the number of uses often reveals that durable clothing is cheaper per wearing than disposable fast fashion. Additionally, fewer garments purchased means proportionally less production-stage environmental damage per unit of wardrobe utility.",
            "feedback_incorrect": "Cost-per-wearing analysis reveals that the apparent affordability of fast fashion is an illusion. When total cost is divided by total uses, durable clothing often costs less per wearing. More importantly, one quality garment replacing ten disposable ones means one-tenth of the production-stage environmental impact (water, carbon, chemicals) for the same wardrobe function."
        },
        {
            "question": "After analyzing all model scenarios, a student concludes that solving the fast fashion environmental crisis requires intervention at multiple levels. Which combination of interventions does the model evidence best support?",
            "choices": {
                "A": "Only consumer behavior change can solve this problem",
                "B": "Only government regulation of the fashion industry can solve this problem",
                "C": "A combination of reduced consumer demand (addresses the driver), sustainable production methods (reduces per-unit impact), and improved recycling systems (addresses disposal), with policy mechanisms to internalize environmental costs in pricing",
                "D": "Only technological innovation in materials can solve this problem"
            },
            "correct": "C",
            "feedback_correct": "Correct. The model shows that consumer demand is the primary driver, but production methods determine the per-unit environmental cost, and disposal systems determine end-of-life impact. Effective solutions must address all three stages while policy mechanisms (taxes, regulations, extended producer responsibility) ensure that environmental costs are no longer externalized. No single intervention is sufficient.",
            "feedback_incorrect": "The model reveals that the fast fashion problem exists at every stage of the lifecycle: demand drives overproduction, production methods determine per-unit environmental cost, and inadequate disposal creates waste. Comprehensive solutions must address all three levels simultaneously, with policy mechanisms ensuring that currently externalized environmental costs are reflected in product prices."
        }
    ]
}

# ── L09: Why Earthquakes Hit Some Cities Harder ─────────────────────

L09_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Which of the following best describes what causes earthquakes?",
            "choices": {
                "A": "Underground explosions caused by volcanic gases",
                "B": "The sudden release of accumulated tectonic stress when rocks along a fault boundary slip past each other",
                "C": "The gravitational pull of the Moon on Earth's crust",
                "D": "Changes in temperature deep within the Earth's core"
            },
            "correct": "B",
            "feedback_correct": "Correct. Earthquakes occur when tectonic plates, moving at 1-15 cm/year, build up stress along their boundaries. When accumulated stress exceeds the frictional strength of the rocks, the rocks suddenly slip, releasing stored energy as seismic waves.",
            "feedback_incorrect": "Earthquakes result from the sudden release of tectonic stress. Earth's plates move slowly but are locked together by friction at their boundaries. Stress accumulates over decades to centuries until it exceeds the rock's frictional strength, causing sudden slip and releasing stored energy as seismic waves."
        },
        {
            "question": "The 2010 Haiti earthquake (magnitude 7.0) killed approximately 230,000 people, while the 2010 Chile earthquake (magnitude 8.8, releasing nearly 500 times more energy) killed 525 people. Which factor most likely explains this difference?",
            "choices": {
                "A": "Chile's earthquake occurred in an unpopulated area",
                "B": "Chile has strict seismic building codes and better infrastructure, while Haiti had virtually no building codes and widespread unreinforced construction",
                "C": "Haiti's earthquake lasted much longer than Chile's",
                "D": "Chile experienced an aftershock that reduced the main earthquake's impact"
            },
            "correct": "B",
            "feedback_correct": "Correct. Chile's strict building codes, developed through extensive experience with earthquakes, meant most structures were designed to withstand severe shaking. Haiti had virtually no seismic building standards, and most structures were unreinforced masonry that collapsed at relatively moderate shaking levels.",
            "feedback_incorrect": "Building quality is the primary determinant of earthquake casualties. Chile's extensive building codes required seismic-resistant design. Haiti's structures were mostly unreinforced concrete and masonry with no seismic engineering. The saying 'earthquakes don't kill people, buildings do' directly applies here."
        },
        {
            "question": "A student claims: 'If you're far enough from an earthquake, you'll be safe.' What geological factor could make this claim inaccurate?",
            "choices": {
                "A": "Earthquakes can change direction mid-propagation to target specific cities",
                "B": "Soft, loose soil can amplify seismic waves by factors of 2-10x, meaning a distant city on clay may experience worse shaking than a closer city on bedrock",
                "C": "Earthquake waves speed up over distance, becoming more destructive",
                "D": "All locations at the same distance from an earthquake experience identical shaking"
            },
            "correct": "B",
            "feedback_correct": "Correct. Ground amplification is a critical factor that can override distance effects. When seismic waves travel from dense bedrock into soft, loose sediments, conservation of energy forces the waves to slow down and increase in amplitude. Mexico City, built on an ancient lakebed, was devastated by a 1985 earthquake whose epicenter was 350 km away.",
            "feedback_incorrect": "Distance alone does not determine earthquake damage. Ground amplification occurs when seismic waves pass from solid bedrock into soft sediments, causing the waves to increase in amplitude (like ocean waves growing taller near shore). A city on clay can experience 2-10 times more shaking than a city on bedrock at the same distance from the earthquake."
        },
        {
            "question": "Scientists can identify where earthquakes are likely to occur and roughly how strong they might be. Why can they not predict exactly when an earthquake will happen?",
            "choices": {
                "A": "Scientists have the technology but governments suppress the information",
                "B": "The precise conditions under which accumulated stress exceeds rock friction and triggers rupture involve too many microscale variables to predict deterministically with current technology",
                "C": "Earthquakes occur completely randomly with no underlying geological cause",
                "D": "Earthquake prediction is easy but scientists choose not to share their predictions"
            },
            "correct": "B",
            "feedback_correct": "Correct. While scientists can map fault lines, measure accumulated stress, and estimate potential magnitudes, the exact moment of rupture depends on microscale conditions at the fault surface (rock composition, fluid pressure, temperature, locked asperities) that are impossible to measure comprehensively at depth. Reliable short-term prediction remains beyond current capability.",
            "feedback_incorrect": "Earthquake prediction is limited by the complexity of fault mechanics. Scientists can identify where earthquakes will occur (plate boundaries, known faults) and estimate how strong they could be (based on fault length and accumulated stress), but the exact timing of rupture depends on unmeasurable conditions deep underground. The best approach is preparation, not prediction."
        },
        {
            "question": "If you were designing a building in a known earthquake zone, which feature would be most important for structural survival?",
            "choices": {
                "A": "Making the building as rigid as possible so it doesn't move at all",
                "B": "Using a design that allows the building to flex and absorb seismic energy without collapsing",
                "C": "Building the tallest possible structure to rise above the seismic waves",
                "D": "Using the heaviest possible materials to anchor the building to the ground"
            },
            "correct": "B",
            "feedback_correct": "Correct. Modern seismic engineering designs buildings to flex and absorb energy rather than resist it rigidly. Techniques like base isolation (rubber bearings that allow the building to 'float'), moment-resisting frames (flexible steel), and shear walls allow structures to deform without catastrophic failure.",
            "feedback_incorrect": "Counterintuitively, rigid buildings are often more vulnerable to earthquakes because they cannot absorb seismic energy. Modern earthquake-resistant design allows controlled flexibility: base isolation lets the building move independently of the ground, moment-resisting frames flex without breaking, and shear walls absorb lateral forces. The goal is to dissipate energy, not resist it."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In a student's earthquake model, the same magnitude earthquake produces dramatically different outcomes in two simulated cities: City A (on bedrock, modern codes) shows minimal damage, while City B (on clay, older buildings) shows widespread destruction. Which model principle best explains this divergence?",
            "choices": {
                "A": "Earthquake magnitude is the only factor that determines destruction",
                "B": "Local conditions (ground amplification and building vulnerability) act as multipliers that can transform the same seismic input into vastly different outcomes, demonstrating that magnitude alone is a poor predictor of damage",
                "C": "City B must have been closer to the epicenter than City A",
                "D": "The model is flawed because all locations should experience the same shaking from the same earthquake"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that earthquake magnitude describes energy released at the source, but destruction is determined by how local conditions modify that energy. Ground amplification multiplies seismic wave intensity (2-10x on soft soil), and building vulnerability determines whether structures survive or collapse under the modified shaking. These local factors can be more important than the earthquake itself.",
            "feedback_incorrect": "The model shows that identical seismic input produces different outcomes because local conditions act as multipliers. Soft soil amplifies shaking by 2-10x compared to bedrock, and unreinforced buildings fail at shaking levels that engineered buildings easily survive. Magnitude describes the source; local conditions determine the destination impact."
        },
        {
            "question": "A student's model includes a causal chain: Tectonic Stress → Fault Slip → Seismic Wave Energy → Ground Amplification → Building Vulnerability. At which point in this chain can humans most effectively intervene to reduce earthquake damage?",
            "choices": {
                "A": "Reducing tectonic stress through drilling into fault zones",
                "B": "At the Ground Amplification and Building Vulnerability stages, through soil remediation, seismic building codes, and retrofitting existing structures",
                "C": "Preventing fault slip by injecting concrete into fault lines",
                "D": "Reducing seismic wave energy by building walls around cities"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that tectonic stress, fault slip, and seismic wave generation are geological processes beyond human control. However, Ground Amplification can be partially addressed through soil stabilization and foundation engineering, and Building Vulnerability can be directly addressed through seismic building codes, retrofitting, and appropriate land-use planning.",
            "feedback_incorrect": "The model reveals that the first three steps (tectonic stress, fault slip, seismic waves) are uncontrollable geological processes. Human intervention is only effective at the last two stages: engineering foundations that reduce ground amplification effects, and designing buildings that withstand amplified shaking through modern seismic codes and retrofitting programs."
        },
        {
            "question": "A student extends their model by adding Infrastructure Interdependency as a component. They find that earthquake damage cascades beyond structural collapse: gas lines rupture causing fires, broken water mains prevent firefighting, and downed power lines block roads. What systems thinking concept does this demonstrate?",
            "choices": {
                "A": "Infrastructure systems are independent and do not affect each other",
                "B": "Cascading failures occur when the failure of one interconnected system triggers failures in other dependent systems, amplifying total damage far beyond direct seismic effects",
                "C": "Infrastructure damage only occurs during earthquakes above magnitude 8.0",
                "D": "Modern infrastructure is earthquake-proof and does not fail during seismic events"
            },
            "correct": "B",
            "feedback_correct": "Correct. Infrastructure interdependency creates cascading failure pathways: seismic damage to gas infrastructure causes fires, damage to water infrastructure prevents firefighting, damage to electrical infrastructure blocks communication and access, and damage to transportation infrastructure prevents emergency response. Total damage from cascading failures often exceeds direct seismic damage.",
            "feedback_incorrect": "Cascading failures demonstrate how interconnected systems multiply damage beyond the initial seismic impact. When one system fails (gas lines rupture), it triggers failures in other systems (fires start, water mains break preventing firefighting, power failures prevent communication). The model shows that total earthquake impact is often determined more by infrastructure interdependencies than by the direct shaking damage alone."
        },
        {
            "question": "A city council is reviewing seismic risk. The model shows that neighborhoods on soft soil with older construction face 5-10x higher risk than neighborhoods on bedrock with modern buildings. Historically, low-income communities disproportionately occupy the high-risk zones. What does this model evidence reveal about the intersection of geology and social equity?",
            "choices": {
                "A": "Earthquake risk is purely a geological phenomenon with no social dimension",
                "B": "Earthquake vulnerability is shaped by socioeconomic factors because lower-income communities historically settle on cheaper land (often soft soil) and occupy older, unreinforced buildings, meaning seismic risk maps and poverty maps frequently overlap",
                "C": "All neighborhoods face identical earthquake risk regardless of geology or construction",
                "D": "Wealthy neighborhoods should be prioritized for seismic retrofitting because their buildings are more valuable"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that earthquake risk is not just geological but deeply socioeconomic. The cheapest land in earthquake-prone cities is often on soft soil (former lakebeds, landfill, river deltas), and lower-income communities disproportionately live in older buildings without seismic engineering. Equitable earthquake preparedness requires prioritizing the most vulnerable communities, not just the most valuable properties.",
            "feedback_incorrect": "The model shows that earthquake risk has a social justice dimension. The geological factors that increase vulnerability (soft soil, ground amplification) correlate with lower land values, which correlate with lower-income communities. These same communities also tend to occupy older buildings without seismic engineering. Earthquake risk is distributed inequitably along socioeconomic lines."
        },
        {
            "question": "A student notes that the San Andreas Fault has not produced a major earthquake since 1906 and has accumulated approximately 5 meters of slip deficit. Based on the model, why does a long quiet period represent INCREASED rather than decreased risk?",
            "choices": {
                "A": "Faults become safer over time as they settle into stable positions",
                "B": "Tectonic stress accumulates continuously during quiet periods; the longer the interval since the last major earthquake, the more stored energy is available for release, meaning the next earthquake is likely to be larger",
                "C": "The absence of earthquakes means the fault has become inactive and poses no future risk",
                "D": "Long quiet periods indicate that the tectonic plates have stopped moving"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model clearly shows that tectonic stress accumulates continuously because plate motion never stops. A long quiet period means more stress has built up without release. The San Andreas Fault's 5-meter slip deficit represents an enormous amount of stored elastic energy that will eventually be released, potentially in a single catastrophic event. Silence is not safety; it is energy storage.",
            "feedback_incorrect": "Tectonic plates move continuously, and stress accumulates continuously. A fault that has been quiet for 120 years has 120 years of stored energy waiting for release. The model demonstrates that the longer the quiet period, the more stored energy, and the more powerful the eventual earthquake. The San Andreas Fault's long silence means it has accumulated enormous potential for a major seismic event."
        }
    ]
}

# ── L10: The Wildfire Feedback Loop ─────────────────────────────────

L10_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Over the past several decades, wildfires in the western United States have become larger, more intense, and more destructive. Which combination of factors best explains this trend?",
            "choices": {
                "A": "Increased arson and careless campfire use are the sole causes",
                "B": "A century of fire suppression has accumulated unnaturally high fuel loads, while climate change has made conditions hotter and drier, creating a compounding effect",
                "C": "Wildfires have always been this destructive; modern media just reports on them more",
                "D": "Increased urbanization has reduced the land available for fires to burn"
            },
            "correct": "B",
            "feedback_correct": "Correct. The worsening wildfire crisis results from two compounding human interventions: a century of fire suppression that allowed fuel to accumulate to 5-10 times natural levels, and climate change that has raised temperatures, reduced soil moisture, and extended fire seasons by over 80 days since 1970.",
            "feedback_incorrect": "Worsening wildfires result from multiple compounding factors: 100+ years of fire suppression allowed dead wood and brush to accumulate far beyond natural levels, climate change has raised temperatures and extended drought, and development in fire-prone areas has increased exposure. These factors compound each other, creating conditions far worse than any single cause alone."
        },
        {
            "question": "Many ecosystems, including longleaf pine forests and tallgrass prairies, evolved with periodic natural fire. What role does low-intensity fire play in these ecosystems?",
            "choices": {
                "A": "Fire always destroys ecosystems and should be prevented in all cases",
                "B": "Low-intensity fire clears accumulated dead material, recycles nutrients to the soil, kills disease organisms, and prevents fuel buildup that could cause catastrophic fires",
                "C": "Fire has no ecological function and only occurs due to human activity",
                "D": "Low-intensity fire only benefits animals by clearing paths for movement"
            },
            "correct": "B",
            "feedback_correct": "Correct. Low-intensity surface fires are a natural and necessary disturbance in fire-adapted ecosystems. They clear dead vegetation, return nutrients to soil, create space for new growth, reduce disease, and most importantly prevent the fuel accumulation that leads to catastrophic, ecosystem-destroying crown fires.",
            "feedback_incorrect": "Many ecosystems evolved to depend on periodic fire. Low-intensity surface fires sweep through every 5-30 years naturally, clearing accumulated dead material, recycling nutrients, reducing disease, promoting biodiversity, and preventing the dangerous fuel buildup that leads to catastrophic crown fires. Fire is nature's maintenance tool."
        },
        {
            "question": "Which of the following best describes a positive feedback loop in an environmental system?",
            "choices": {
                "A": "A loop where the system always produces positive outcomes for the environment",
                "B": "A self-reinforcing cycle where the output of a process amplifies the input, causing the system to accelerate in one direction",
                "C": "A loop where the system maintains stable conditions through self-correction",
                "D": "A feedback loop that only operates in human-engineered systems"
            },
            "correct": "B",
            "feedback_correct": "Correct. A positive feedback loop is self-reinforcing: the output amplifies the original input, pushing the system further in the same direction. In wildfires, this means fire creates conditions for more fire. Unlike negative feedback (which stabilizes), positive feedback accelerates change and can lead to runaway effects.",
            "feedback_incorrect": "Despite the name, 'positive' feedback does not mean beneficial. It means self-reinforcing: the output of the process becomes an input that amplifies the process further. Positive feedback pushes systems away from equilibrium, potentially creating runaway effects. Negative feedback, by contrast, counteracts change and stabilizes systems."
        },
        {
            "question": "Climate change is often cited as a driver of worsening wildfires. Through which mechanisms does climate change increase wildfire risk?",
            "choices": {
                "A": "Climate change only increases lightning strikes, which start more fires",
                "B": "Higher temperatures dry out vegetation and soil, earlier snowmelt reduces summer moisture, and longer drought periods extend the fire season, creating drier fuels over longer periods",
                "C": "Climate change reduces wind speeds, which traps heat in forests",
                "D": "Climate change causes more rain, which promotes vegetation growth that eventually becomes fuel"
            },
            "correct": "B",
            "feedback_correct": "Correct. Climate change attacks wildfire risk through multiple mechanisms simultaneously: higher temperatures increase evapotranspiration (drying vegetation), earlier snowmelt reduces summer soil moisture, extended drought periods stress vegetation, and the fire season has lengthened by over 80 days in the western U.S. since 1970.",
            "feedback_incorrect": "Climate change increases wildfire risk through several interacting mechanisms: higher average temperatures dry out vegetation faster, snowpack melts earlier reducing summer water availability, drought periods are longer and more severe, and the overall fire season has extended by 80+ days since 1970. These factors compound each other, creating fire conditions that would have been extreme in the past but are now routine."
        },
        {
            "question": "Indigenous peoples across the Americas, Australia, and Africa have used controlled burning for thousands of years. What was the primary purpose of these 'cultural burns'?",
            "choices": {
                "A": "Cultural burns were purely ceremonial with no ecological purpose",
                "B": "Cultural burns maintained healthy landscapes by periodically reducing fuel loads, promoting new growth, managing wildlife habitat, and preventing the conditions for catastrophic wildfire",
                "C": "Indigenous peoples set fires to destroy enemy territories",
                "D": "Cultural burns were accidental fires that were later given cultural significance"
            },
            "correct": "B",
            "feedback_correct": "Correct. Indigenous fire management was sophisticated ecological engineering. Aboriginal Australians practiced 'fire-stick farming' for tens of thousands of years, and Native American tribes used controlled burns to manage forests, promote game habitat, and maintain productive landscapes. These practices effectively maintained the natural fire cycle that European colonizers disrupted through suppression.",
            "feedback_incorrect": "Indigenous cultural burning was a sophisticated land management practice. It served multiple purposes: reducing accumulated fuel loads, promoting new plant growth for food and materials, managing wildlife habitat, clearing travel corridors, and preventing catastrophic wildfire. These practices maintained healthy landscapes for millennia and are now being revived as modern fire management recognizes their effectiveness."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "In a student's wildfire model, the 'Healthy Fire Cycle' scenario shows that low-intensity fire actually REDUCES Fuel Load and stabilizes the system. The 'Catastrophic Fire' scenario shows that high-intensity fire INCREASES conditions for future catastrophic fire. What fundamental difference in system behavior do these two scenarios demonstrate?",
            "choices": {
                "A": "Both scenarios produce identical outcomes because all fire is the same",
                "B": "Low-intensity fire acts as a stabilizing negative feedback (reducing fuel prevents future fire escalation), while high-intensity fire creates a destabilizing positive feedback (destroying vegetation leads to drier conditions and more combustible fuel for the next fire)",
                "C": "The model shows that fire intensity has no relationship to ecosystem recovery",
                "D": "Catastrophic fire is actually better for the ecosystem than low-intensity fire"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals two fundamentally different system behaviors depending on fire intensity. Low-intensity fire is a stabilizing force: it removes fuel, which reduces the potential energy for future fires, creating a negative feedback loop that maintains ecosystem health. High-intensity fire is destabilizing: it destroys vegetation, dries soil, and creates conditions that make the next fire equally or more catastrophic, creating a positive feedback loop.",
            "feedback_incorrect": "The model demonstrates that fire intensity determines whether the system behaves with negative feedback (stabilizing) or positive feedback (destabilizing). Low-intensity fire reduces fuel loads, preventing future catastrophic fires. High-intensity fire destroys the ecosystem's ability to recover, creating conditions for equally destructive future fires. The same process (fire) can either stabilize or destabilize the system depending on its intensity."
        },
        {
            "question": "A student traces the wildfire positive feedback loop in their model: Fire Intensity (high) → Soil Moisture (decreases) → Vegetation Recovery (slows) → Fuel Load (increases as dead material accumulates faster than living recovery) → next Fire Intensity (increases). Where in this loop could human intervention most effectively break the cycle?",
            "choices": {
                "A": "By increasing Wind Speed to blow fires out more quickly",
                "B": "By reducing Fuel Load through prescribed burns and mechanical thinning before a wildfire occurs, breaking the cycle between accumulated fuel and catastrophic fire intensity",
                "C": "By preventing all vegetation from growing in fire-prone areas",
                "D": "By increasing Soil Moisture through continuous irrigation of all forests"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model identifies Fuel Load as the most practical intervention point. While Wind Speed is uncontrollable and Soil Moisture cannot be artificially maintained at forest scale, Fuel Load can be directly reduced through prescribed burns and mechanical thinning. Reducing fuel before a wildfire occurs prevents high-intensity fire, which prevents the downstream cascade of soil drying, vegetation destruction, and further fuel accumulation.",
            "feedback_incorrect": "The model shows that Fuel Load is the most actionable intervention point. Prescribed burns and mechanical thinning directly reduce accumulated combustible material, preventing the high-intensity fire that triggers the destructive feedback loop. This mimics the natural low-intensity fire cycle that maintained healthy forests for millennia before fire suppression disrupted it."
        },
        {
            "question": "A student's model shows that after 80 years of fire suppression, fuel loads are 5-10 times higher than natural levels. A forest manager proposes continuing suppression but investing more in firefighting technology. Using model evidence, evaluate this proposal.",
            "choices": {
                "A": "This is the best approach because firefighting technology is always improving",
                "B": "This approach treats the symptom (active fire) without addressing the cause (excessive fuel accumulation); the model shows that suppression has created the problem, and continuing it will make fuel loads even more extreme, guaranteeing increasingly catastrophic fires that eventually overwhelm any firefighting capability",
                "C": "Firefighting budgets should be unlimited because fire is always bad",
                "D": "The model shows that fire suppression has been successful and should continue"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model clearly demonstrates that fire suppression created the current crisis by allowing fuel to accumulate to unprecedented levels. Continuing suppression while investing in firefighting is analogous to buying bigger mops while leaving a broken pipe unfixed. The fuel continues to accumulate, making each future fire more extreme. The model shows that prevention (prescribed burns, fuel management) is fundamentally more effective than reaction (firefighting).",
            "feedback_incorrect": "The model provides clear evidence that fire suppression is the underlying cause of worsening wildfires, not the solution. Each year of additional suppression adds more fuel. The U.S. already spends over $3 billion annually on wildfire suppression, yet fires continue to worsen. The model shows that breaking the feedback loop requires reducing fuel loads through prescribed burns, not fighting ever-larger fires with ever-larger budgets."
        },
        {
            "question": "A student adds Carbon Release as a component to their model. They discover that wildfire releases massive amounts of stored CO2, which contributes to climate change, which creates hotter/drier conditions, which makes future fires worse. What does this reveal about the wildfire-climate relationship?",
            "choices": {
                "A": "Carbon release from wildfires is negligible compared to human emissions",
                "B": "Wildfire and climate change form a nested positive feedback loop: fire releases carbon that accelerates climate change, which creates conditions for worse fires, creating a self-reinforcing cycle that operates at a larger scale than the vegetation-soil-fuel loop alone",
                "C": "Climate change has no connection to wildfire behavior",
                "D": "Wildfire carbon release actually helps cool the atmosphere by blocking sunlight with smoke"
            },
            "correct": "B",
            "feedback_correct": "Correct. The extended model reveals a feedback loop operating at a larger scale than the original vegetation-soil-fuel cycle. Wildfire releases decades of stored carbon as CO2 in days. This CO2 contributes to atmospheric greenhouse gas concentration, which accelerates climate warming, which creates hotter and drier conditions, which makes future fires more intense and carbon-releasing. This creates a planetary-scale positive feedback loop.",
            "feedback_incorrect": "Adding Carbon Release to the model reveals a nested positive feedback loop operating at a larger scale. Individual fires release stored carbon that contributes to climate change, and climate change creates conditions for worse fires. This means the wildfire crisis is not just a local ecosystem problem but a component of a global climate feedback system where fire and warming reinforce each other."
        },
        {
            "question": "A student's community wildfire resilience plan proposes prescribed burns, defensible space requirements, fire-resistant building codes, and post-fire restoration. Their model shows this comprehensive approach reduces catastrophic fire risk by 70%. Why does the model predict that addressing the feedback loop at multiple points is more effective than targeting a single intervention?",
            "choices": {
                "A": "Multiple interventions always produce exactly additive results",
                "B": "Targeting multiple points in the feedback loop reduces the probability that the cycle can self-sustain, because even if one intervention is imperfect, the others provide redundancy that prevents the system from reaching conditions for catastrophic fire",
                "C": "The model is wrong because a single intervention should be sufficient",
                "D": "Multiple interventions are only necessary in areas with high wind speeds"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that addressing the feedback loop at multiple points creates a resilient defense system. Prescribed burns reduce fuel (breaking the fuel-to-intensity link), defensible space protects structures even if fire occurs, building codes ensure structures survive moderate shaking, and post-fire restoration prevents the recovery-failure pathway. Each intervention reduces the probability of the next link in the chain activating, and together they prevent the feedback loop from completing its cycle.",
            "feedback_incorrect": "The model demonstrates that positive feedback loops can be disrupted most effectively by intervening at multiple points simultaneously. No single intervention is foolproof. Prescribed burns reduce fuel but cannot eliminate all risk. Defensible space protects structures but does not prevent fires from starting. Building codes help buildings survive but do not address ecosystem health. Together, these interventions provide overlapping protection that prevents the feedback loop from completing its cycle."
        }
    ]
}

# ── Aggregate dictionary ────────────────────────────────────────────

ALL_QUESTIONS = {
    "G09L1-L01": L01_QUESTIONS,
    "G09L1-L02": L02_QUESTIONS,
    "G09L1-L03": L03_QUESTIONS,
    "G09L1-L04": L04_QUESTIONS,
    "G09L1-L05": L05_QUESTIONS,
    "G09L1-L06": L06_QUESTIONS,
    "G09L1-L07": L07_QUESTIONS,
    "G09L1-L08": L08_QUESTIONS,
    "G09L1-L09": L09_QUESTIONS,
    "G09L1-L10": L10_QUESTIONS,
}
