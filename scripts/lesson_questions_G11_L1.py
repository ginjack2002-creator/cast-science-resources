#!/usr/bin/env python3
"""Multiple choice pre/post assessment questions for Grade 11 Level 1 ModelIt! Lessons (Science & Society)"""

# =============================================================================
# L01: Why Is Your Phone Designed to Be Addictive?
# NGSS: HS-LS1-3 (Feedback mechanisms maintain homeostasis)
# =============================================================================
L01_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A student notices that she checks her phone more frequently during the evening, even though she receives the same number of notifications as during the morning. Which explanation best accounts for this pattern from a homeostatic feedback perspective?",
            "choices": {
                "A": "Her dopamine receptor sensitivity has decreased throughout the day due to repeated stimulation, requiring more frequent checking to achieve the same reward feeling",
                "B": "Her phone sends more notifications at night because the algorithm detects lower usage",
                "C": "She is simply more bored in the evening and has more free time to check her phone",
                "D": "Her brain produces more dopamine at night due to circadian rhythm cycles"
            },
            "correct": "A",
            "feedback_correct": "Correct. Tolerance buildup from repeated dopamine stimulation throughout the day reduces receptor sensitivity, requiring more frequent checking to achieve the same neurochemical reward, a classic homeostatic disruption.",
            "feedback_incorrect": "Consider what happens to neurotransmitter receptors when they are repeatedly stimulated over the course of a day. The brain adapts by reducing sensitivity, which drives the need for more frequent stimulation."
        },
        {
            "question": "Which of the following best describes the role of variable reward schedules in social media app design?",
            "choices": {
                "A": "They ensure users receive a consistent experience each time they open the app",
                "B": "They deliver unpredictable rewards that produce stronger dopamine responses than predictable ones, mimicking slot machine psychology",
                "C": "They reduce the total time users spend on the app by making content less engaging",
                "D": "They help users develop healthy habits by spacing out notifications at regular intervals"
            },
            "correct": "B",
            "feedback_correct": "Correct. Variable reward schedules, where the outcome of checking is unpredictable, produce significantly stronger and more persistent dopamine responses than consistent rewards. This is the same mechanism exploited in gambling.",
            "feedback_incorrect": "Think about why slot machines are more addictive than vending machines. The unpredictability of the reward, not the reward itself, is what drives the strongest neurochemical response."
        },
        {
            "question": "A neuroscientist proposes that phone addiction operates through a positive feedback loop rather than a negative feedback loop. Which evidence would best support this claim?",
            "choices": {
                "A": "Users who turn off their phones for a week report reduced urges to check them",
                "B": "Increased phone checking leads to tolerance, which leads to even more checking, escalating the behavior over time",
                "C": "Users who receive consistent notifications check their phones at a steady rate",
                "D": "The brain eventually reaches a saturation point where no further dopamine is released"
            },
            "correct": "B",
            "feedback_correct": "Correct. A positive feedback loop amplifies the output: more checking leads to more tolerance, which leads to more checking. The behavior escalates rather than stabilizing, which is the hallmark of positive feedback.",
            "feedback_incorrect": "Recall the difference between positive and negative feedback. Positive feedback amplifies a response (it spirals), while negative feedback dampens it (it stabilizes). Which answer describes an escalating spiral?"
        },
        {
            "question": "In the context of dopamine and phone usage, tolerance is best defined as which of the following?",
            "choices": {
                "A": "The brain's ability to handle increasing amounts of screen time without physical harm",
                "B": "A social willingness to accept smartphone use in professional settings",
                "C": "A neurological adaptation where repeated stimulation reduces receptor sensitivity, requiring more intense or frequent stimulation for the same effect",
                "D": "The maximum number of notifications a user can receive before feeling overwhelmed"
            },
            "correct": "C",
            "feedback_correct": "Correct. Tolerance is a neurological adaptation involving dopamine receptor downregulation. As sensitivity decreases, the brain requires increasingly frequent or intense stimulation to produce the same reward feeling.",
            "feedback_incorrect": "Tolerance in neuroscience refers to a specific biological adaptation at the receptor level, not a social or behavioral threshold. Consider how the brain physically changes in response to repeated chemical stimulation."
        },
        {
            "question": "A researcher compares two groups: one uses an app with randomly timed notifications, and the other uses an app with notifications at fixed hourly intervals. Which prediction is most consistent with behavioral neuroscience?",
            "choices": {
                "A": "The fixed-interval group will show higher compulsive checking because they can anticipate when rewards arrive",
                "B": "Both groups will show identical checking behavior because the total number of notifications is the same",
                "C": "The random-interval group will show higher compulsive checking because unpredictable timing produces stronger dopamine anticipation responses",
                "D": "The fixed-interval group will develop tolerance faster because their dopamine spikes are more regular"
            },
            "correct": "C",
            "feedback_correct": "Correct. Unpredictable reward timing triggers stronger dopamine anticipation responses. The uncertainty about when a reward will arrive keeps the brain in a heightened state of anticipation, driving more frequent checking behavior.",
            "feedback_incorrect": "Consider the variable reward schedule principle: which timing pattern creates more uncertainty and anticipation? The brain's dopamine system responds most strongly to unpredictable rewards, not to predictable ones."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's computational model shows that reducing notification frequency to zero for 7 days causes dopamine receptor sensitivity to partially recover, but compulsive checking behavior persists. Which explanation best accounts for these two different recovery patterns?",
            "choices": {
                "A": "The model has an error because behavior should always match receptor sensitivity",
                "B": "Receptor sensitivity is a neurological adaptation that reverses when stimulation stops, but learned anticipation behavior is a conditioned response that persists independently of receptor state",
                "C": "The checking behavior persists because the phone continues to receive notifications even when alerts are turned off",
                "D": "Dopamine receptors cannot actually recover once tolerance is established"
            },
            "correct": "B",
            "feedback_correct": "Correct. Receptor sensitivity is a physiological adaptation that can partially reverse, but the learned behavior, a conditioned anticipation response, is encoded in neural pathways and persists even after the chemical stimulus is removed. This explains why digital detoxes only partially work.",
            "feedback_incorrect": "The model reveals two different biological systems at work: receptor chemistry (which can recover) and conditioned behavioral patterns (which are learned). These operate on different timescales and through different mechanisms."
        },
        {
            "question": "Using model evidence, a student argues that making social media rewards predictable rather than variable would reduce compulsive behavior. A classmate counters that this would also reduce engagement, making the app commercially unviable. Which response best evaluates this trade-off using systems thinking?",
            "choices": {
                "A": "The classmate is correct because reducing dopamine responses will always reduce engagement proportionally",
                "B": "Predictable rewards reduce the dopamine-driven compulsive loop but can maintain engagement through content quality and social connection, meaning the trade-off is not zero-sum",
                "C": "The student is wrong because predictable rewards produce the same dopamine response as variable rewards",
                "D": "The trade-off is irrelevant because all apps eventually lose users regardless of reward schedule"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that reducing variable rewards breaks the compulsive dopamine loop, but engagement can be sustained through other mechanisms (content quality, genuine social interaction) that do not exploit neurological vulnerabilities. The trade-off is not zero-sum.",
            "feedback_incorrect": "Systems thinking requires considering multiple pathways. Engagement is not solely driven by dopamine exploitation. Consider whether there are other reasons people use social media that do not depend on addictive design patterns."
        },
        {
            "question": "A model simulation shows that after 30 days of high-frequency variable notifications, screen time increased by 340% while self-reported satisfaction decreased by 60%. Which interpretation best explains this divergence?",
            "choices": {
                "A": "The simulation has an error because increased usage should correlate with increased satisfaction",
                "B": "Users are spending more time on the app because they enjoy it more but are unwilling to admit it on surveys",
                "C": "Tolerance buildup means users need more stimulation to achieve diminishing dopamine rewards, driving increased usage while reducing the subjective reward per interaction",
                "D": "The app's content quality decreased over the 30-day period, frustrating users"
            },
            "correct": "C",
            "feedback_correct": "Correct. This is the signature of a tolerance-driven addiction cycle: behavior escalates (more screen time) while the reward per interaction diminishes (less satisfaction). The dopamine system drives the behavior, not the subjective experience of enjoyment.",
            "feedback_incorrect": "Consider what tolerance does to the relationship between behavior and reward. When receptor sensitivity decreases, each interaction produces less reward, so the brain drives more frequent behavior to compensate. Usage goes up, satisfaction goes down."
        },
        {
            "question": "An ethical app design team proposes three changes: (1) predictable notification timing, (2) daily usage limits, and (3) removal of infinite scroll. Based on the dopamine feedback model, which change would have the greatest impact on reducing compulsive behavior?",
            "choices": {
                "A": "Daily usage limits, because they physically prevent excessive screen time",
                "B": "Removal of infinite scroll, because it eliminates the visual stimulus",
                "C": "Predictable notification timing, because it eliminates the variable reward schedule that drives the strongest dopamine anticipation responses",
                "D": "All three changes would have equal impact because they all reduce screen time"
            },
            "correct": "C",
            "feedback_correct": "Correct. The model identifies variable reward schedules as the primary driver of compulsive dopamine responses. Making rewards predictable addresses the root cause of the feedback loop, while usage limits and scroll changes address symptoms without altering the neurochemical driver.",
            "feedback_incorrect": "The model shows that the variable reward schedule is the primary mechanism driving the dopamine-tolerance-checking loop. Which intervention targets this root mechanism directly rather than addressing downstream symptoms?"
        },
        {
            "question": "A policymaker uses the model to argue for regulations requiring social media companies to disclose how their notification algorithms work. An opponent argues that algorithms are proprietary trade secrets. Which claim is best supported by the model evidence?",
            "choices": {
                "A": "The opponent is correct because algorithms are too complex for the public to understand",
                "B": "The model shows that specific design choices (variable rewards, notification frequency) directly exploit homeostatic feedback mechanisms, and transparency about these choices is necessary for informed consent about neurological risks",
                "C": "The policymaker is wrong because the model shows that individual willpower is the primary factor in phone addiction",
                "D": "Both positions are equally valid because the model cannot distinguish between engineered addiction and user choice"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model provides evidence that specific, identifiable design features exploit homeostatic feedback mechanisms in measurable ways. This evidence supports the argument that users deserve transparency about how their neurochemistry is being targeted, analogous to nutritional labels on food.",
            "feedback_incorrect": "Review what the model demonstrates about the relationship between design choices and neurological outcomes. The model provides quantifiable evidence that specific design features cause specific neurochemical effects. Consider whether this evidence supports or undermines the case for transparency."
        }
    ]
}

# =============================================================================
# L02: Can We Actually Feed 10 Billion People?
# NGSS: HS-LS2-1, HS-ESS3-3 (Carrying capacity, natural resource management)
# =============================================================================
L02_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Global food production currently generates approximately 6,000 calories per person per day, yet 735 million people are chronically hungry. Which factor best explains this paradox?",
            "choices": {
                "A": "The world does not produce enough total food to feed 8 billion people",
                "B": "Distribution inefficiencies, food waste, and diversion to animal feed and biofuels prevent produced calories from reaching people as food",
                "C": "The 735 million hungry people live in regions where crops cannot physically grow",
                "D": "Food production data is inaccurate and actual output is much lower than reported"
            },
            "correct": "B",
            "feedback_correct": "Correct. The world produces sufficient total calories, but roughly two-thirds are lost to waste, animal feed conversion, and biofuel production before reaching humans as food. Hunger is a distribution and allocation problem, not a production problem.",
            "feedback_incorrect": "Consider the math: 6,000 calories produced per person versus 2,000 needed. The total is sufficient. What happens to the other 4,000 calories per person? The answer involves the entire supply chain, not production capacity."
        },
        {
            "question": "A farmer applies maximum synthetic fertilizer to increase crop yield. Which long-term consequence is most likely based on soil science?",
            "choices": {
                "A": "Soil organic matter will increase indefinitely as crops grow larger and return more biomass",
                "B": "Soil health will remain unchanged because synthetic fertilizer replaces natural nutrients",
                "C": "Soil degradation will accelerate as microbial diversity declines, organic matter decreases, and chemical runoff pollutes waterways",
                "D": "Crop yields will increase linearly with fertilizer application without any diminishing returns"
            },
            "correct": "C",
            "feedback_correct": "Correct. Excessive synthetic fertilizer degrades soil health by reducing microbial diversity, decreasing organic matter, causing acidification, and contributing to waterway pollution through runoff. Short-term yield gains mask long-term soil destruction.",
            "feedback_incorrect": "Consider what soil health depends on beyond just chemical nutrients. Healthy soil is a living ecosystem of microorganisms, organic matter, and nutrient cycles. How does flooding it with synthetic chemicals affect these biological systems over years?"
        },
        {
            "question": "Carrying capacity for a human population depends on which set of factors?",
            "choices": {
                "A": "Only the total land area of the planet",
                "B": "Agricultural technology, diet choices, resource distribution, and environmental sustainability practices",
                "C": "The birth rate and death rate of the population alone",
                "D": "The number of animal species in an ecosystem"
            },
            "correct": "B",
            "feedback_correct": "Correct. Human carrying capacity is not a fixed number. It depends on how efficiently we produce food (technology), what we eat (diet choices affect land use 10x), how we share resources (distribution), and whether we maintain the ecosystems that sustain agriculture.",
            "feedback_incorrect": "Unlike most species, human carrying capacity is highly flexible because we can modify our technology, diet, and resource management. Consider how switching from beef to plant-based diets would change how many people the same land could feed."
        },
        {
            "question": "Which strategy would most effectively increase food production while minimizing environmental damage?",
            "choices": {
                "A": "Converting all remaining forests to farmland to maximize arable land area",
                "B": "Applying maximum fertilizer to existing farmland to push yields higher",
                "C": "Sustainable intensification that maintains soil health while improving yield per hectare on existing farmland",
                "D": "Reducing the global population to match current food distribution capacity"
            },
            "correct": "C",
            "feedback_correct": "Correct. Sustainable intensification improves yield on existing land through precision agriculture, soil conservation, and integrated pest management without the environmental costs of land expansion or chemical overuse.",
            "feedback_incorrect": "Consider the trade-offs of each approach. Land expansion destroys ecosystems. Maximum fertilizer degrades soil. The challenge is increasing output per hectare without destroying the resource base. Which approach achieves both?"
        },
        {
            "question": "A computational model of global agriculture shows that crop yields initially increase with fertilizer application but eventually plateau and then decline. This pattern is best explained by which concept?",
            "choices": {
                "A": "Linear growth, where outputs always increase proportionally with inputs",
                "B": "Diminishing returns followed by degradation, where initial gains are offset by cumulative damage to the soil ecosystem",
                "C": "Random variation in weather patterns that occasionally reduce yields",
                "D": "Government regulations that limit how much fertilizer farmers can apply"
            },
            "correct": "B",
            "feedback_correct": "Correct. The yield curve demonstrates diminishing returns (each additional unit of fertilizer produces less additional yield) followed by negative returns as soil degradation from excess chemicals reduces the land's productive capacity.",
            "feedback_incorrect": "Think about what happens to the soil, not just the crop, when fertilizer is applied repeatedly at maximum levels. Initially yields rise, then the gains shrink, and eventually the soil is damaged enough that yields actually fall."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's 30-year simulation shows that the Green Revolution strategy (maximum fertilizer and water) produces higher yields than sustainable intensification for the first 15 years, but then yields crash while the sustainable approach maintains steady output. Which conclusion is best supported by this model data?",
            "choices": {
                "A": "The Green Revolution strategy is superior because it feeds more people during the critical near-term period",
                "B": "The model is unreliable because real-world yields have not yet shown this crash pattern globally",
                "C": "Short-term yield maximization creates a soil degradation debt that accumulates invisibly until the system collapses, making the sustainable approach more productive over the full 30-year period",
                "D": "Both strategies produce the same total food over 30 years, just distributed differently across time"
            },
            "correct": "C",
            "feedback_correct": "Correct. The simulation reveals a time-delayed feedback: soil degradation accumulates beneath rising yields until a tipping point is reached. The sustainable strategy avoids this crash by maintaining the resource base, producing more total food across the full period.",
            "feedback_incorrect": "Compare total food produced over the entire 30-year period, not just the peak year. The Green Revolution strategy borrows from future productivity. When the soil debt comes due, the crash erases the early gains."
        },
        {
            "question": "The model shows that converting 30% of forest to farmland increases total food production by only 18%, not 30%. Which factor best explains why the production increase is less than proportional to the land increase?",
            "choices": {
                "A": "Newly converted forest land has lower soil fertility, less established irrigation, and higher erosion rates than existing optimized farmland",
                "B": "The model incorrectly assumes that new farmland produces no food",
                "C": "Farmers on new land use less fertilizer because they are unfamiliar with the soil",
                "D": "Global food demand decreased during the simulation period"
            },
            "correct": "A",
            "feedback_correct": "Correct. Forest soils, once cleared, lose organic matter rapidly, lack irrigation infrastructure, and are prone to erosion. New farmland is inherently less productive than established agricultural land, and deforestation disrupts local water cycles that previously supported the ecosystem.",
            "feedback_incorrect": "Think about what makes existing farmland productive: decades of soil management, irrigation systems, local climate adapted to open land. Newly cleared forest has none of these advantages and faces additional challenges like rapid topsoil loss."
        },
        {
            "question": "A student proposes reducing food waste by 50% as an alternative to increasing production. Based on the model, which assessment of this proposal is most accurate?",
            "choices": {
                "A": "Waste reduction is irrelevant because the problem is production, not distribution",
                "B": "Reducing waste by 50% would effectively increase food availability by the equivalent of farming millions of additional hectares, without any environmental cost from land conversion or intensification",
                "C": "Waste reduction would only affect wealthy nations and have no impact on global food security",
                "D": "The model shows waste reduction is impossible because spoilage is a natural and unavoidable process"
            },
            "correct": "B",
            "feedback_correct": "Correct. Since roughly one-third of all food produced is wasted, a 50% reduction in waste would free up massive amounts of food without any additional environmental burden. This is the most resource-efficient strategy for closing the food gap.",
            "feedback_incorrect": "Consider that approximately one-third of global food production is wasted. Recovering even half of that waste means more food is available without planting a single additional hectare or applying any additional fertilizer."
        },
        {
            "question": "The simulation reveals that water availability is the first resource to become limiting in the Green Revolution scenario. Which systems-level explanation accounts for water becoming the bottleneck before soil degradation or land availability?",
            "choices": {
                "A": "Water is the only resource that cannot be manufactured or substituted with technology",
                "B": "Maximum fertilizer use increases crop water demand while simultaneously depleting aquifers and degrading watershed ecosystems, creating a self-reinforcing scarcity cycle",
                "C": "Climate change is the only factor affecting water availability in the model",
                "D": "Water limitations are an artifact of the model and do not reflect real-world agricultural constraints"
            },
            "correct": "B",
            "feedback_correct": "Correct. Intensive agriculture creates a water scarcity feedback loop: higher fertilizer increases crop water demand, irrigation depletes aquifers faster than they recharge, and agricultural runoff degrades the watersheds that supply fresh water. The water crisis is both driven by and amplified by intensification.",
            "feedback_incorrect": "Consider how intensive farming affects water from multiple directions simultaneously. High-yield crops need more water, irrigation draws down aquifers, and chemical runoff pollutes water sources. These effects compound each other."
        },
        {
            "question": "Based on the complete model analysis, which policy recommendation is best supported by the simulation evidence for feeding 10 billion people by 2058?",
            "choices": {
                "A": "Maximize chemical inputs on existing farmland to push yields as high as possible in the short term",
                "B": "A combined strategy of sustainable intensification, 50% waste reduction, and dietary shifts away from resource-intensive animal agriculture",
                "C": "Convert all remaining forests to farmland to ensure maximum food production capacity",
                "D": "Maintain current agricultural practices and rely on future technological breakthroughs to close the gap"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that no single strategy is sufficient. Sustainable intensification maintains yields without soil degradation, waste reduction frees existing food without environmental cost, and dietary shifts dramatically reduce the land and water needed per calorie. The combined approach is the only one that closes the gap sustainably.",
            "feedback_incorrect": "Review the model results for each individual strategy. None of them alone feeds 10 billion people sustainably for 30 years. The question is which combination of strategies addresses production, distribution, and demand simultaneously."
        }
    ]
}

# =============================================================================
# L03: Why Do Some Neighborhoods Flood While Others Don't?
# NGSS: HS-ESS3-4, HS-ETS1-1 (Environmental justice, engineered solutions)
# =============================================================================
L03_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Two neighborhoods in the same city receive identical rainfall during a storm. Neighborhood A experiences 60 cm of flooding while Neighborhood B has no flooding at all. Which factor most likely accounts for this difference?",
            "choices": {
                "A": "Neighborhood A is located at a higher elevation than Neighborhood B",
                "B": "Neighborhood A has significantly higher impervious surface coverage and older, lower-capacity storm drains than Neighborhood B",
                "C": "Neighborhood A receives more rainfall because storms preferentially target certain areas",
                "D": "The residents of Neighborhood A failed to prepare for the storm"
            },
            "correct": "B",
            "feedback_correct": "Correct. Impervious surfaces prevent water infiltration, forcing it to flow overland as runoff. Combined with undersized storm drains, the system cannot handle the water volume. These are infrastructure characteristics, not weather differences.",
            "feedback_incorrect": "Since both neighborhoods received the same rainfall, the difference must be in how each neighborhood handles the water. Consider what physical features determine whether rainwater soaks in, drains away, or pools on the surface."
        },
        {
            "question": "Environmental justice in the context of urban flooding refers to which principle?",
            "choices": {
                "A": "All neighborhoods should receive equal amounts of rainfall",
                "B": "No community should bear a disproportionate burden of flood risk due to race, income, or historical disinvestment",
                "C": "Environmental regulations should be enforced equally regardless of neighborhood demographics",
                "D": "Natural disasters affect all communities equally regardless of infrastructure quality"
            },
            "correct": "B",
            "feedback_correct": "Correct. Environmental justice specifically addresses the disproportionate environmental burdens borne by marginalized communities due to historical and ongoing inequities in infrastructure investment, zoning decisions, and political power.",
            "feedback_incorrect": "Environmental justice is about the distribution of environmental risks and benefits. Consider which communities consistently experience the worst environmental outcomes and why. The pattern is not random."
        },
        {
            "question": "Green infrastructure such as rain gardens, bioswales, and permeable pavement reduces flood risk primarily by which mechanism?",
            "choices": {
                "A": "Blocking rainfall from reaching the ground",
                "B": "Increasing the rate of evaporation so water disappears faster",
                "C": "Allowing rainwater to infiltrate into the ground rather than flowing across impervious surfaces as runoff",
                "D": "Redirecting storm water to other neighborhoods"
            },
            "correct": "C",
            "feedback_correct": "Correct. Green infrastructure mimics natural water infiltration processes. By allowing water to soak into the ground through permeable surfaces, vegetation, and engineered soil systems, it reduces the volume of surface runoff that overwhelms storm drains.",
            "feedback_incorrect": "Think about what happens to rainwater in a forest versus a parking lot. In the forest, water soaks in. On the parking lot, it flows across the surface. Green infrastructure brings the forest's water-handling properties into urban areas."
        },
        {
            "question": "A city's 1935 redlining map shows that neighborhoods marked 'hazardous' (predominantly communities of color) correspond almost exactly with areas that experience severe flooding today. Which explanation best accounts for this correlation?",
            "choices": {
                "A": "Coincidence, since redlining maps and flood maps measure completely unrelated phenomena",
                "B": "Redlined neighborhoods received decades of disinvestment in infrastructure, resulting in outdated storm drains, fewer parks, and more impervious surfaces",
                "C": "Communities of color chose to live in flood-prone areas voluntarily",
                "D": "Modern flooding patterns are caused entirely by climate change, not historical infrastructure decisions"
            },
            "correct": "B",
            "feedback_correct": "Correct. Redlining systematically denied investment to Black and Brown neighborhoods for decades. This disinvestment resulted in aging infrastructure, inadequate storm drainage, removal of green space, and high impervious surface coverage, all of which increase flood vulnerability.",
            "feedback_incorrect": "Consider what happens to a neighborhood's infrastructure over 90 years of systematic disinvestment: pipes age without replacement, green spaces are paved over, and storm systems are never upgraded. These are cumulative effects of policy, not coincidence."
        },
        {
            "question": "Which of the following is an example of an impervious surface?",
            "choices": {
                "A": "A grass lawn in a residential yard",
                "B": "A concrete parking lot covering three city blocks",
                "C": "A rain garden planted with native vegetation",
                "D": "A gravel path through a community park"
            },
            "correct": "B",
            "feedback_correct": "Correct. Concrete is impervious, meaning water cannot pass through it. A large parking lot converts rainfall entirely into surface runoff, dramatically increasing flood risk downstream. Urban areas can be 80-95% impervious.",
            "feedback_incorrect": "Impervious means water cannot soak through. Consider which surfaces allow water to pass into the ground (permeable) versus which surfaces force water to flow across the top."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's model simulation shows that adding green infrastructure to a disinvested neighborhood reduces flood depth by 45%, but the neighborhood still floods more than the affluent comparison neighborhood. Which conclusion is best supported by this evidence?",
            "choices": {
                "A": "Green infrastructure is ineffective and should not be pursued",
                "B": "Green infrastructure alone cannot overcome the compounding effects of outdated storm drains, high impervious coverage, and decades of underinvestment; a comprehensive multi-factor retrofit is needed",
                "C": "The affluent neighborhood has a natural advantage that cannot be replicated",
                "D": "The model is inaccurate because green infrastructure should completely eliminate flooding"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that flood inequity results from multiple compounding factors: impervious surfaces, drain capacity, and green space all interact. Addressing only one factor (green infrastructure) reduces but cannot eliminate the disparity created by the full set of infrastructure deficits.",
            "feedback_incorrect": "The 45% reduction shows green infrastructure works, but the remaining gap shows it is not enough alone. Consider the other infrastructure differences between the neighborhoods that also contribute to flood risk."
        },
        {
            "question": "The model shows that impervious surface coverage has a nonlinear relationship with flood depth: increasing coverage from 60% to 70% adds 8 cm of flood depth, but increasing from 80% to 90% adds 22 cm. Which explanation best accounts for this nonlinear pattern?",
            "choices": {
                "A": "The model contains a calculation error at higher percentages",
                "B": "At high impervious coverage, the remaining permeable surfaces are insufficient to absorb meaningful rainfall, so each additional percentage of pavement has a disproportionately large effect on runoff volume",
                "C": "Higher impervious coverage causes more rainfall to fall on the neighborhood",
                "D": "Storm drain capacity automatically increases at higher coverage levels, partially compensating"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is a threshold effect: when almost all ground is paved, the few remaining permeable surfaces provide the last buffer against flooding. Removing that final buffer has outsized consequences because the system has no remaining capacity to absorb water.",
            "feedback_incorrect": "Think about what happens as you approach 100% pavement. At 60% coverage, 40% of land still absorbs rain. At 90%, only 10% absorbs rain. Losing half of that remaining 10% has a much bigger relative impact than losing the same amount at lower coverage."
        },
        {
            "question": "A city council is debating two flood mitigation plans for a historically disinvested neighborhood. Plan A installs a new high-capacity storm drain system ($50M). Plan B adds green infrastructure throughout the neighborhood ($30M). Based on the model, which evaluation is most accurate?",
            "choices": {
                "A": "Plan A is always superior because engineered systems handle more water volume",
                "B": "Plan B is always superior because it costs less",
                "C": "The optimal approach combines both plans because storm drains handle peak flow while green infrastructure reduces total runoff volume, and together they address the problem at multiple points in the system",
                "D": "Neither plan will work because flooding is determined by weather, not infrastructure"
            },
            "correct": "C",
            "feedback_correct": "Correct. The model shows that storm drains and green infrastructure address different aspects of the flood system. Green infrastructure reduces the total volume of runoff entering the system, while storm drains increase the capacity to move water that does run off. Together they provide more protection than either alone.",
            "feedback_incorrect": "Consider what each intervention does in the water system. Green infrastructure reduces how much water becomes runoff. Storm drains increase how fast runoff is removed. These are complementary functions addressing different parts of the system."
        },
        {
            "question": "A student uses the model to compare the same storm hitting the same neighborhood in 1960 versus 2020. The 2020 simulation shows 3x more flooding despite the same rainfall. Which combination of changes best explains the increase?",
            "choices": {
                "A": "Climate change caused the 2020 storm to produce more rain",
                "B": "Increased impervious surfaces from development, aging storm infrastructure that has not been upgraded, and loss of green space from urban expansion",
                "C": "The neighborhood's elevation decreased between 1960 and 2020",
                "D": "Population growth in the neighborhood made flooding worse through more water usage"
            },
            "correct": "B",
            "feedback_correct": "Correct. Over 60 years, urban development increased impervious coverage, the storm drain system aged without upgrades, and green spaces were converted to buildings and pavement. These cumulative infrastructure changes dramatically increased flood vulnerability to the same storm.",
            "feedback_incorrect": "The question specifies the same rainfall amount in both periods. The difference must come from changes in the neighborhood's physical characteristics. Consider how 60 years of development altered the ground surface and drainage infrastructure."
        },
        {
            "question": "Based on the model evidence, a student argues that flood risk disparities between neighborhoods constitute environmental racism because they result from racially motivated historical policies. An opponent argues the disparities are simply the result of economics, not race. Which model evidence is most relevant to evaluating these claims?",
            "choices": {
                "A": "The model cannot address social questions because it only simulates physical water flow",
                "B": "The model shows that current infrastructure quality maps directly onto historical redlining boundaries, which were explicitly race-based policies, demonstrating that the physical infrastructure disparities have racial origins even if current maintenance decisions are economics-based",
                "C": "The model proves that flooding affects wealthy and poor neighborhoods equally",
                "D": "The model shows that all neighborhoods would flood equally if green infrastructure were removed"
            },
            "correct": "B",
            "feedback_correct": "Correct. While the model simulates physical water flow, the input conditions (impervious coverage, drain capacity, green space) were shaped by explicitly race-based redlining policies. The model connects current physical disparities to their historical racial origins, showing that today's 'economic' patterns inherited their geography from racial policies.",
            "feedback_incorrect": "Consider the causal chain: redlining (explicitly racial) caused disinvestment, which caused infrastructure disparities, which cause unequal flooding. The model traces the physical consequences of historical racial policy, even though the model itself only simulates water."
        }
    ]
}

# =============================================================================
# L04: How Does Your Immune System Learn?
# NGSS: HS-LS1-2, HS-LS1-4 (Hierarchical organization, cellular division)
# =============================================================================
L04_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A person is vaccinated against measles at age 2 and encounters the actual measles virus at age 17. Their immune system mounts a rapid, powerful response. Which component of the immune system is primarily responsible for this rapid secondary response?",
            "choices": {
                "A": "Innate immune cells that provide the same nonspecific defense against all pathogens",
                "B": "Memory B cells that retained the molecular blueprint for producing measles-specific antibodies for 15 years",
                "C": "Red blood cells that carry antibodies through the bloodstream",
                "D": "The vaccine itself, which remains active in the body for decades"
            },
            "correct": "B",
            "feedback_correct": "Correct. Memory B cells are long-lived cells that persist for years or decades after the initial immune response. Upon re-exposure to the measles antigen, they rapidly differentiate into plasma cells that produce targeted antibodies within hours rather than the weeks required for a primary response.",
            "feedback_incorrect": "Consider what makes the secondary immune response different from the first. The speed and specificity suggest the immune system 'remembers' the pathogen. Which cell type stores this molecular memory?"
        },
        {
            "question": "The herd immunity threshold for measles (R0 = 15) is approximately 93%. What does this percentage represent?",
            "choices": {
                "A": "The percentage of infected people who will recover from measles",
                "B": "The proportion of the population that must be immune to prevent sustained community transmission",
                "C": "The effectiveness rate of the measles vaccine",
                "D": "The percentage of the population that will eventually contract measles"
            },
            "correct": "B",
            "feedback_correct": "Correct. The herd immunity threshold (1 - 1/R0) is the proportion of the population that must be immune to break transmission chains. For measles, 93% immunity means each infected person encounters mostly immune individuals, reducing their effective transmission below 1.",
            "feedback_incorrect": "Herd immunity is a population-level concept. It refers to the point at which enough people are immune that the pathogen can no longer sustain transmission chains through the community. Calculate 1 - (1/15) to find the threshold."
        },
        {
            "question": "Which statement best describes how vaccines train the immune system?",
            "choices": {
                "A": "Vaccines inject pre-made antibodies that fight pathogens directly",
                "B": "Vaccines introduce weakened or inactivated pathogen components that trigger the adaptive immune system to produce its own memory cells without causing disease",
                "C": "Vaccines strengthen the innate immune system by increasing white blood cell production",
                "D": "Vaccines create a permanent barrier in the bloodstream that prevents all pathogens from entering"
            },
            "correct": "B",
            "feedback_correct": "Correct. Vaccines expose the immune system to antigens (pathogen components) in a safe form. This triggers the full adaptive immune response, including antibody production and memory cell formation, without the risk of disease. The immune system builds its own lasting protection.",
            "feedback_incorrect": "Vaccines work WITH your immune system, not as a substitute for it. They provide a safe preview of the pathogen so your immune system can build memory before encountering the real threat."
        },
        {
            "question": "If a community has 80% vaccination coverage against a disease requiring 93% coverage for herd immunity, which prediction is most accurate?",
            "choices": {
                "A": "The community is fully protected because 80% is close enough to 93%",
                "B": "Outbreaks can still occur among the susceptible 20%, and unvaccinated individuals who cannot receive vaccines (infants, immunocompromised) remain at risk",
                "C": "Only vaccinated individuals can contract the disease",
                "D": "The disease will spontaneously disappear because 80% coverage eliminates the pathogen"
            },
            "correct": "B",
            "feedback_correct": "Correct. The 13% gap below the herd immunity threshold means transmission chains can still propagate through the susceptible population. This puts everyone who cannot be vaccinated (infants, cancer patients, organ recipients) at risk because the community shield is incomplete.",
            "feedback_incorrect": "Herd immunity is a threshold effect, not a gradual one. Below the threshold, enough susceptible people remain connected in the population for the pathogen to spread. Consider who is most vulnerable when community protection is incomplete."
        },
        {
            "question": "After receiving a vaccine, a patient's blood test shows antibody levels that peak at 2 weeks, then gradually decline over the following months. Does this decline mean the vaccine has stopped working?",
            "choices": {
                "A": "Yes, declining antibodies mean the patient is no longer protected",
                "B": "No, because memory B cells persist long after circulating antibody levels decline, enabling rapid antibody production upon re-exposure",
                "C": "Yes, which is why booster shots must be given every month",
                "D": "No, because the vaccine continuously produces new antibodies"
            },
            "correct": "B",
            "feedback_correct": "Correct. Circulating antibody levels naturally decline after the initial immune response, but the critical memory cells persist for years or decades. These memory cells can reactivate within hours of re-exposure, producing antibodies far faster than the original response.",
            "feedback_incorrect": "Distinguish between circulating antibodies (which are active proteins in the blood) and memory cells (which are living cells that store the blueprint for making those antibodies). Which one provides long-term protection?"
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's model shows that when vaccination rate crosses the herd immunity threshold, disease transmission drops sharply rather than gradually. Which explanation best accounts for this threshold behavior?",
            "choices": {
                "A": "The vaccine becomes more effective at higher coverage levels",
                "B": "Below the threshold, transmission chains can connect susceptible individuals across the population; at the threshold, immune individuals fragment these chains into disconnected clusters that cannot sustain spread",
                "C": "The pathogen mutates to become less infectious at high vaccination rates",
                "D": "People change their behavior when they know most of the population is vaccinated"
            },
            "correct": "B",
            "feedback_correct": "Correct. Herd immunity operates as a percolation threshold: when enough nodes (people) are immune, the network of susceptible individuals becomes fragmented into small, disconnected clusters. The pathogen can no longer find a continuous path through the population, and transmission collapses.",
            "feedback_incorrect": "Think of the population as a network. Each immune person removes a node from the transmission network. At some point, the network fractures into small disconnected groups. This is a sudden transition, not a gradual decline."
        },
        {
            "question": "The model simulates an outbreak in a population with 85% vaccination coverage for a disease with R0 = 5 (herd immunity threshold = 80%). Despite being above the threshold, a small outbreak occurs. Which explanation is most consistent with the model?",
            "choices": {
                "A": "The model is incorrect because outbreaks should be impossible above the herd immunity threshold",
                "B": "Clustering of unvaccinated individuals in geographic or social groups can create local pockets of susceptibility that sustain limited transmission even when overall coverage exceeds the threshold",
                "C": "The vaccine failed in all affected individuals simultaneously",
                "D": "The pathogen's R0 increased spontaneously during the simulation"
            },
            "correct": "B",
            "feedback_correct": "Correct. Herd immunity thresholds assume uniform mixing. When unvaccinated individuals cluster together (by geography, community, or belief system), local susceptibility can exceed the threshold even when the overall population average is above it. This is why spatially uniform coverage matters.",
            "feedback_incorrect": "The overall percentage is above the threshold, but herd immunity assumes uniform distribution. Consider what happens if unvaccinated individuals are concentrated in the same school, neighborhood, or community rather than evenly spread across the population."
        },
        {
            "question": "A model comparison shows that the individual immune response simulation takes 14 days to reach peak antibody production on first exposure but only 2 days on second exposure. Which cellular mechanism accounts for this 7-fold speed increase?",
            "choices": {
                "A": "The pathogen is weaker on second exposure",
                "B": "Memory B cells bypass the initial antigen recognition and clonal expansion phases, immediately differentiating into antibody-producing plasma cells",
                "C": "The innate immune system handles the second infection entirely without adaptive immunity",
                "D": "Antibodies from the first exposure remain in the blood permanently"
            },
            "correct": "B",
            "feedback_correct": "Correct. During the primary response, naive B cells must encounter the antigen, become activated, undergo clonal expansion, and differentiate into plasma cells. Memory B cells skip these early steps, having already been selected and expanded. They can begin producing antibodies almost immediately.",
            "feedback_incorrect": "Consider what steps are required during the first immune response that can be skipped during the second. Memory cells exist precisely to accelerate this process. What steps do they eliminate?"
        },
        {
            "question": "A pandemic response team uses the model to plan a vaccination rollout with limited supply. For a disease with R0 = 4.5 and a 6-month timeline, which prioritization strategy would the model evidence best support?",
            "choices": {
                "A": "Vaccinate the youngest populations first because they have the longest remaining lifespan",
                "B": "Distribute vaccines randomly through a lottery system for fairness",
                "C": "Prioritize high-transmission groups (healthcare workers, essential workers, densely housed populations) first to reduce Re below 1 as quickly as possible with limited supply",
                "D": "Vaccinate only the elderly because they have the highest mortality risk"
            },
            "correct": "C",
            "feedback_correct": "Correct. The model shows that reducing Re below 1 is the critical objective for stopping exponential growth. Vaccinating high-transmission individuals first has the largest impact on Re per dose administered, slowing spread most efficiently while supply is limited.",
            "feedback_incorrect": "The model tracks transmission dynamics, not just individual protection. With limited supply, the strategic question is: which vaccinations reduce the most transmission per dose? Consider who drives the most spread in the population."
        },
        {
            "question": "A student observes that their model produces different outcomes for the same 85% vaccination rate depending on whether the disease has R0 = 3 or R0 = 12. For R0 = 3, the outbreak is contained; for R0 = 12, it spreads widely. Which analysis best explains this difference?",
            "choices": {
                "A": "The vaccine is less effective against diseases with higher R0",
                "B": "85% coverage exceeds the herd immunity threshold for R0 = 3 (threshold = 67%) but falls far short of the threshold for R0 = 12 (threshold = 92%), so the same coverage produces opposite outcomes",
                "C": "Diseases with higher R0 mutate faster and evade the vaccine",
                "D": "The model assigns random outcomes when coverage is between 80% and 90%"
            },
            "correct": "B",
            "feedback_correct": "Correct. The herd immunity threshold depends directly on R0 (formula: 1 - 1/R0). At 85% coverage, R0 = 3 requires only 67% (covered), but R0 = 12 requires 92% (not covered). The same population-level immunity can be sufficient or inadequate depending on the pathogen's transmissibility.",
            "feedback_incorrect": "Calculate the herd immunity threshold for each R0 using 1 - (1/R0). For R0 = 3: 1 - (1/3) = 0.67 or 67%. For R0 = 12: 1 - (1/12) = 0.92 or 92%. Now compare each threshold to the 85% coverage."
        }
    ]
}

# =============================================================================
# L05: Is Fast Fashion Destroying the Planet?
# NGSS: HS-ESS3-2, HS-ETS1-3 (Energy/mineral resources, design solutions)
# =============================================================================
L05_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A student calculates that a $5 polyester t-shirt requires 2,700 liters of water, produces 5.5 kg of CO2, and releases 700,000 microplastic fibers per wash. These costs are not reflected in the purchase price. What economic concept best describes this situation?",
            "choices": {
                "A": "Supply and demand equilibrium, where the price accurately reflects all costs",
                "B": "Externalities, where environmental and social costs are borne by third parties (ecosystems, communities) rather than the producer or consumer",
                "C": "Overpricing, where the shirt costs more to produce than its retail price",
                "D": "Market efficiency, where the price automatically includes all costs"
            },
            "correct": "B",
            "feedback_correct": "Correct. Externalities are costs imposed on third parties who did not choose to incur them. Water pollution, carbon emissions, and microplastic contamination are absorbed by ecosystems and communities rather than reflected in the shirt's price, creating a false sense of cheapness.",
            "feedback_incorrect": "If the environmental costs are not in the price, someone or something else must be paying them. Consider who absorbs the cost of water pollution, carbon emissions, and microplastic contamination. These are costs shifted away from the transaction."
        },
        {
            "question": "Which material used in clothing production is most associated with long-lasting microplastic pollution in oceans?",
            "choices": {
                "A": "Organic cotton, which biodegrades in water",
                "B": "Polyester, a petroleum-based synthetic that sheds microscopic plastic fibers during washing",
                "C": "Wool, which is a natural animal fiber",
                "D": "Hemp, which requires minimal processing"
            },
            "correct": "B",
            "feedback_correct": "Correct. Polyester is made from petroleum and sheds up to 700,000 microplastic fibers per wash load. These fibers are too small for water treatment plants to filter, accumulating in oceans, soil, food chains, and even human tissue, persisting for centuries.",
            "feedback_incorrect": "Consider which clothing materials are derived from petroleum. Synthetic fabrics like polyester are essentially plastic in fiber form. When washed, they shed microscopic plastic particles that enter the water system."
        },
        {
            "question": "A life cycle assessment of clothing tracks environmental impact from which starting point to which ending point?",
            "choices": {
                "A": "From the retail store to the consumer's closet",
                "B": "From raw material extraction through manufacturing, consumer use, and end-of-life disposal or recycling",
                "C": "Only the manufacturing phase, which produces the most pollution",
                "D": "From the consumer's purchase to their first washing of the garment"
            },
            "correct": "B",
            "feedback_correct": "Correct. A life cycle assessment is a cradle-to-grave analysis that accounts for every stage: growing or extracting raw materials, processing and manufacturing, shipping, consumer use (including washing), and final disposal or recycling. Each stage contributes to the total environmental footprint.",
            "feedback_incorrect": "A life cycle assessment is meant to capture the TOTAL environmental impact. Consider all the stages a garment passes through from the moment raw materials are extracted from the earth to the moment the garment reaches its final destination (landfill, incinerator, or recycling facility)."
        },
        {
            "question": "The fashion industry produces over 100 billion garments per year for a global population of 8 billion. Which trend best describes the relationship between production volume and garment lifespan over the past 20 years?",
            "choices": {
                "A": "Production has increased while garment lifespan has decreased, with average garments worn only 7-10 times before disposal",
                "B": "Production has decreased as consumers buy fewer, higher-quality items",
                "C": "Both production and lifespan have increased proportionally",
                "D": "Production has remained constant while lifespan has doubled due to better materials"
            },
            "correct": "A",
            "feedback_correct": "Correct. Fast fashion has driven a dramatic increase in production volume while simultaneously reducing how long garments are worn. This combination maximizes waste: more garments produced, each worn fewer times, creating an accelerating stream of textile waste.",
            "feedback_incorrect": "Consider the fast fashion business model: low prices encourage frequent purchasing, trend cycles encourage rapid disposal, and low quality means garments do not last. How would these incentives affect both production volume and how long each item is used?"
        },
        {
            "question": "If a consumer extends a garment's lifespan from 10 wears to 50 wears, the per-wear environmental impact is reduced by what factor?",
            "choices": {
                "A": "It remains the same because the total impact was already created during manufacturing",
                "B": "It is reduced by a factor of 5, because the fixed manufacturing impact is distributed across 5 times as many uses",
                "C": "It doubles because the garment is washed more times",
                "D": "It cannot be calculated without knowing the specific garment material"
            },
            "correct": "B",
            "feedback_correct": "Correct. Most of a garment's environmental impact occurs during production (water, carbon, chemicals). By wearing it 5 times longer, that fixed production cost is amortized across 5 times more uses, reducing the per-wear impact by a factor of 5. This makes garment lifespan the most powerful lever consumers have.",
            "feedback_incorrect": "Think about the per-wear cost. If manufacturing a shirt uses 2,700 liters of water, wearing it 10 times means 270 liters per wear. Wearing it 50 times means 54 liters per wear. The fixed production cost is simply divided across more uses."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's model simulation compares three scenarios over one year for 1,000 consumers. Fast fashion (100B garments/polyester/7 wears) produces 847,000 kg of textile waste. Sustainable wardrobe (50B garments/organic cotton/100 wears) produces 29,000 kg. Which factor contributes most to the 29x difference?",
            "choices": {
                "A": "The material change from polyester to organic cotton, which biodegrades faster",
                "B": "The 14x increase in garment lifespan (7 to 100 wears), which delays disposal and reduces the replacement rate",
                "C": "The 50% reduction in production volume alone",
                "D": "The difference in retail price between the two scenarios"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows garment lifespan is the dominant variable. A 14x increase in lifespan means each garment replaces 14 fast-fashion equivalents, reducing both production demand and waste generation multiplicatively. The 50% production cut is significant but secondary to the lifespan effect.",
            "feedback_incorrect": "Compare the magnitudes: production is halved (2x reduction), but lifespan increases 14x. In a waste model, each long-lasting garment replaces many short-lived ones. The compound effect of longer lifespan on both production needs and waste generation makes it the dominant factor."
        },
        {
            "question": "The circular fashion model shows that 70% fiber recycling reduces virgin material demand but does not eliminate it entirely. Based on the model, which factor prevents 100% circularity?",
            "choices": {
                "A": "Recycled fiber is too expensive to compete with virgin polyester",
                "B": "Each recycling cycle degrades fiber quality, blended fabrics are difficult to separate, and collection rates never reach 100%, so virgin material is always needed to replace losses",
                "C": "Consumers refuse to buy clothing made from recycled materials",
                "D": "The technology for textile recycling does not exist yet"
            },
            "correct": "B",
            "feedback_correct": "Correct. Circular systems face inherent material losses at every step: collection inefficiency (not all garments are returned), sorting challenges (blended fabrics cannot be separated), and fiber degradation (each recycling cycle shortens fibers, reducing quality). These losses require virgin material inputs to maintain the system.",
            "feedback_incorrect": "Think about what happens at each step of the recycling process. Not all garments are collected. Mixed materials are hard to separate. Recycled fiber is shorter and weaker. Each of these losses means some virgin material must enter the system to replace what is lost."
        },
        {
            "question": "A student argues that switching from polyester to organic cotton would solve the fashion industry's environmental problem. Based on the model, which critique of this argument is most accurate?",
            "choices": {
                "A": "The student is correct because organic cotton has zero environmental impact",
                "B": "Organic cotton eliminates microplastic pollution but still requires 2,700 liters of water per shirt and significant land use; without also addressing production volume and garment lifespan, the total environmental impact remains unsustainably high",
                "C": "Material type has no effect on environmental impact according to the model",
                "D": "Polyester is actually more sustainable than organic cotton in all categories"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that material substitution addresses some impacts (microplastics) but not others (water use, land use, carbon from manufacturing and shipping). The fundamental problem is the volume-lifespan equation: producing too many garments that are used too few times, regardless of material.",
            "feedback_incorrect": "Consider whether changing the material addresses the core problem of overproduction and underuse. Organic cotton has advantages (no microplastics, biodegradable) but still requires enormous resources per garment. If you still make 100 billion garments worn 7 times each, how much does the material change help?"
        },
        {
            "question": "The model reveals that the fashion industry produces 10% of global CO2 emissions, more than international flights and maritime shipping combined. A student identifies manufacturing and dyeing as the largest emission sources. Which intervention would the model predict to have the greatest impact on total fashion carbon emissions?",
            "choices": {
                "A": "Using renewable energy in shipping to reduce transport emissions",
                "B": "Extending average garment lifespan from 7 to 30 wears, which reduces the number of garments manufactured and dyed by over 75%",
                "C": "Encouraging consumers to wash clothes in cold water",
                "D": "Switching to electric delivery vehicles for last-mile retail distribution"
            },
            "correct": "B",
            "feedback_correct": "Correct. Since manufacturing and dyeing are the largest emission sources, the most effective intervention is reducing how many garments need to be manufactured and dyed. Extending lifespan from 7 to 30 wears means producing roughly one-quarter as many garments, cutting the dominant emission sources by over 75%.",
            "feedback_incorrect": "If manufacturing and dyeing are the biggest carbon sources, which intervention most directly reduces the number of garments that need to be manufactured and dyed? Shipping and washing are smaller contributors. The leverage point is reducing total production volume."
        },
        {
            "question": "Based on the complete model analysis, a student proposes a fashion sustainability policy requiring all garments to display an 'environmental cost label' showing water use, carbon emissions, and expected lifespan. Which argument best supports this policy using model evidence?",
            "choices": {
                "A": "Labels are unnecessary because consumers already understand fashion's environmental impact",
                "B": "The model demonstrates that the true environmental cost is invisible in the purchase price, and per-wear cost calculations show dramatic differences between fast and sustainable fashion that consumers cannot assess without data",
                "C": "Labels would increase the cost of garments, making fashion less accessible",
                "D": "The model shows that consumer behavior has no impact on fashion's environmental footprint"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals massive hidden costs that are not reflected in price. A $5 shirt worn 7 times costs $0.71/wear plus enormous environmental externalities, while a $30 shirt worn 100 times costs $0.30/wear with a fraction of the impact. Without labels, consumers cannot make informed comparisons.",
            "feedback_incorrect": "The model showed that a $5 fast-fashion shirt is actually more expensive per wear AND more environmentally damaging than a $30 quality shirt. This counter-intuitive finding is invisible without data. Consider whether making this data visible would change purchasing decisions."
        }
    ]
}

# =============================================================================
# L06: Can an Algorithm Be Racist?
# NGSS: HS-ETS1-1, HS-ETS1-4 (Major global challenges, computer simulations)
# =============================================================================
L06_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A hiring algorithm trained on 20 years of company data consistently ranks male candidates higher than equally qualified female candidates. The algorithm does not use gender as an input variable. Which explanation best accounts for this bias?",
            "choices": {
                "A": "The algorithm is functioning correctly because men are objectively better candidates",
                "B": "The algorithm learned patterns from historically biased hiring decisions, using proxy variables correlated with gender to replicate past discrimination",
                "C": "The algorithm randomly generates different scores for different candidates",
                "D": "The programmer deliberately coded gender discrimination into the algorithm"
            },
            "correct": "B",
            "feedback_correct": "Correct. If the company historically favored men for leadership roles, the training data encodes this bias. The algorithm learns that features correlated with being male (name patterns, activity types, school affiliations) predict 'success,' reproducing the bias without explicitly using gender.",
            "feedback_incorrect": "Consider what the algorithm is actually learning from. If the training data consists of 20 years of biased hiring decisions, the algorithm learns to replicate those biased patterns. It does not need to use gender directly if other variables are correlated with gender."
        },
        {
            "question": "In machine learning, a proxy variable is best described as which of the following?",
            "choices": {
                "A": "A variable that directly measures what the algorithm is trying to predict",
                "B": "A data feature that is not directly discriminatory but is highly correlated with a protected characteristic due to historical patterns, such as zip code serving as a proxy for race",
                "C": "A random variable added to improve algorithm accuracy",
                "D": "A variable that the algorithm ignores during processing"
            },
            "correct": "B",
            "feedback_correct": "Correct. Proxy variables are indirect indicators of protected characteristics. For example, zip code strongly correlates with race in American cities due to residential segregation from redlining. An algorithm using zip code effectively uses race without naming it.",
            "feedback_incorrect": "Think about how removing race from an algorithm's inputs does not guarantee fairness. If other variables (zip code, school name, criminal record) are strongly correlated with race due to historical segregation and discrimination, the algorithm can discriminate without ever seeing race."
        },
        {
            "question": "An algorithm used in criminal sentencing has 85% overall accuracy but is found to have a false positive rate of 45% for Black defendants and only 23% for white defendants. Which term best describes this outcome?",
            "choices": {
                "A": "Algorithmic efficiency, because the overall accuracy is high",
                "B": "Disparate impact, where the algorithm disproportionately harms one demographic group despite appearing neutral overall",
                "C": "Random error, because all algorithms make mistakes",
                "D": "Acceptable performance, because no algorithm can be 100% accurate"
            },
            "correct": "B",
            "feedback_correct": "Correct. Disparate impact occurs when a seemingly neutral practice produces significantly different outcomes for different groups. The algorithm's overall accuracy masks a severe inequity: Black defendants are nearly twice as likely to be incorrectly flagged as high-risk.",
            "feedback_incorrect": "Look beyond the overall accuracy. An 85% overall accuracy can hide severe inequities if errors are concentrated in one group. A false positive rate of 45% for one group versus 23% for another means the algorithm treats these groups very differently."
        },
        {
            "question": "Which of the following is the most accurate statement about the relationship between algorithms and objectivity?",
            "choices": {
                "A": "Algorithms are inherently objective because they are based on mathematics, not human judgment",
                "B": "Algorithms can only be as unbiased as the data they are trained on and the decisions made by their designers about which features to include",
                "C": "Algorithms always produce fair outcomes because they treat all inputs equally",
                "D": "Bias in algorithms is impossible to detect or measure"
            },
            "correct": "B",
            "feedback_correct": "Correct. Algorithms process data according to rules, but both the data and the rules are products of human choices and historical patterns. If the training data contains bias, the algorithm learns bias. If the designer selects biased features, the algorithm amplifies bias. Math is neutral; the inputs and design choices are not.",
            "feedback_incorrect": "Consider the chain of human decisions behind every algorithm: who collected the data, what data was included, which features were selected, and how success was defined. Each decision introduces human assumptions and historical patterns into the 'objective' system."
        },
        {
            "question": "A lending algorithm denies loans at higher rates to applicants from predominantly Black zip codes, even though it does not use race as an input. A data scientist argues that removing zip code from the algorithm would eliminate the racial bias. Which assessment of this argument is most accurate?",
            "choices": {
                "A": "The data scientist is correct because removing zip code removes the source of racial correlation",
                "B": "Removing zip code may reduce but not eliminate bias because other features (school district, credit history, employment patterns) may also serve as proxies for race due to systemic segregation",
                "C": "Zip code has no relationship to race, so removing it would have no effect",
                "D": "The algorithm should use race directly to ensure fair outcomes"
            },
            "correct": "B",
            "feedback_correct": "Correct. In a society with systemic racial segregation, many features beyond zip code correlate with race: school quality, credit history, employment stability, and neighborhood characteristics all reflect the cumulative effects of discrimination. Removing one proxy does not eliminate bias if others remain.",
            "feedback_incorrect": "Consider how deeply racial segregation has structured American society. Zip code is just one of many features that correlate with race. School district quality, credit access, employment patterns, and neighborhood characteristics are all shaped by the same historical forces."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's model shows that retraining a hiring algorithm on demographically balanced data improves the Disparate Impact Ratio from 0.62 to 0.89, but overall Prediction Accuracy drops from 92% to 86%. A stakeholder argues the accuracy loss is unacceptable. Which response best applies systems thinking to evaluate this trade-off?",
            "choices": {
                "A": "The stakeholder is correct because accuracy should always be maximized",
                "B": "The 6% accuracy drop reflects the removal of discriminatory patterns that inflated apparent accuracy by systematically disadvantaging one group; the 'lost' accuracy was built on bias, not genuine predictive power",
                "C": "The model proves that fairness and accuracy are always in direct conflict",
                "D": "The algorithm should be abandoned entirely because no level of accuracy justifies deployment"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals that the original 92% accuracy was partly achieved by exploiting biased patterns in historical data. Those patterns predicted who was SELECTED in the past, not who was QUALIFIED. Removing bias exposes that some of the original accuracy was discriminatory signal, not genuine predictive power.",
            "feedback_incorrect": "Consider what the algorithm was actually predicting at 92% accuracy. If it was predicting who got hired in a biased system, it was predicting bias, not merit. The accuracy decrease when bias is removed suggests some of the original accuracy was built on discriminatory patterns."
        },
        {
            "question": "The model demonstrates that adding a fairness constraint (equal false positive rates across groups) reduces the Disparate Impact Ratio to 1.0 (perfect parity) but reveals a new problem: the algorithm now rejects qualified candidates from the majority group at a higher rate. Which concept best describes this outcome?",
            "choices": {
                "A": "Reverse discrimination, proving that fairness constraints are inherently unjust",
                "B": "A fairness-accuracy trade-off where constraining for equal false positive rates redistributes error across groups, revealing that multiple valid definitions of fairness can conflict with each other",
                "C": "An error in the fairness constraint implementation",
                "D": "Evidence that algorithms should never use fairness constraints"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model reveals a fundamental insight in algorithmic fairness: there are multiple mathematically valid definitions of fairness (equal false positive rates, equal false negative rates, demographic parity), and satisfying one can violate another. This is the impossibility theorem in action.",
            "feedback_incorrect": "The model shows something deeper than simple reverse discrimination. There are multiple valid ways to define fairness, and they can mathematically conflict. Equal false positive rates, equal false negative rates, and equal selection rates cannot all be satisfied simultaneously in most real-world data."
        },
        {
            "question": "A student discovers that their model's algorithm uses 'years of experience' as a top predictive feature. In a field where women were historically excluded before 1990, this feature correlates strongly with gender for workers over 35. Which model-based intervention would most effectively address this bias?",
            "choices": {
                "A": "Remove 'years of experience' entirely from the algorithm",
                "B": "Cap the maximum value of 'years of experience' at a level that postdates the historical exclusion period, neutralizing its proxy effect while retaining its legitimate predictive value for recent cohorts",
                "C": "Double the weight of 'years of experience' to reward long careers",
                "D": "Replace 'years of experience' with age, which is more objective"
            },
            "correct": "B",
            "feedback_correct": "Correct. Capping experience at a post-exclusion threshold (e.g., 15 years) preserves the feature's legitimate predictive value for recent career progression while neutralizing its role as a gender proxy for workers whose career length was artificially shortened by historical discrimination.",
            "feedback_incorrect": "The challenge is that 'years of experience' has both legitimate predictive value AND serves as a proxy for historical gender discrimination. Simply removing it loses useful information. Consider an approach that retains its value while neutralizing its discriminatory correlation."
        },
        {
            "question": "The model shows that an algorithm deployed in healthcare allocates fewer resources to Black patients despite them having more severe health conditions. Investigation reveals the algorithm uses healthcare spending history as a proxy for health needs. Why does this produce racially biased outcomes?",
            "choices": {
                "A": "Black patients have fewer health needs on average",
                "B": "Historical barriers to healthcare access (insurance gaps, provider discrimination, geographic access) mean Black patients spent less on healthcare not because they were healthier, but because they faced systemic barriers to care",
                "C": "The algorithm correctly identifies that lower spending indicates better health",
                "D": "Healthcare algorithms cannot produce biased outcomes because health data is objective"
            },
            "correct": "B",
            "feedback_correct": "Correct. The algorithm conflated spending with health need, but spending reflects ACCESS to care, not need for care. Systemic barriers (insurance inequities, provider bias, geographic access) suppressed healthcare spending for Black patients, causing the algorithm to underestimate their health needs.",
            "feedback_incorrect": "Consider why spending might not equal need. If a person faces barriers to accessing healthcare (no insurance, no nearby providers, provider discrimination), they will spend less. Lower spending does not mean better health; it can mean less access to care."
        },
        {
            "question": "Based on the complete model analysis, which recommendation is best supported by the evidence for deploying algorithms in high-stakes decisions?",
            "choices": {
                "A": "Algorithms should replace human decision-making entirely because they are more consistent",
                "B": "Algorithms should never be used in high-stakes decisions because bias cannot be eliminated",
                "C": "Algorithms should be deployed with mandatory bias auditing, transparent feature disclosure, defined fairness metrics, and ongoing monitoring, because bias can be measured and mitigated even if it cannot be perfectly eliminated",
                "D": "Algorithms should only be trained on data from the last 5 years to avoid historical bias"
            },
            "correct": "C",
            "feedback_correct": "Correct. The model demonstrates that bias is measurable and reducible through deliberate interventions: balanced training data, proxy variable analysis, fairness constraints, and disparate impact auditing. Perfect fairness may be mathematically impossible, but accountability and transparency can ensure continuous improvement.",
            "feedback_incorrect": "The model showed that bias is a quantifiable, measurable phenomenon in algorithms. This means it can be detected, measured, and reduced through systematic interventions. Consider whether the evidence supports complete rejection, unconditional acceptance, or an approach that requires accountability."
        }
    ]
}

# =============================================================================
# L07: Why Do Bridges Collapse?
# NGSS: HS-PS2-1, HS-ETS1-2 (Newton's second law, engineering design)
# =============================================================================
L07_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A bridge is designed with a factor of safety of 2.0. This means the bridge can handle which of the following?",
            "choices": {
                "A": "Exactly the maximum expected load, with no margin for error",
                "B": "Twice the maximum expected load, providing a margin for unexpected loads, material defects, and degradation over time",
                "C": "Half the maximum expected load, meaning it is underdesigned",
                "D": "Two times its own weight but not any additional traffic load"
            },
            "correct": "B",
            "feedback_correct": "Correct. A factor of safety of 2.0 means the bridge's designed capacity is double the maximum expected load. This margin accounts for unexpected traffic surges, material degradation, design uncertainties, and other factors that could increase actual loads above predictions.",
            "feedback_incorrect": "The factor of safety is a ratio: designed capacity divided by expected maximum load. A factor of 2.0 means the bridge is built to handle 2x what it is expected to experience. This buffer protects against unknowns."
        },
        {
            "question": "Material fatigue causes structural failure through which process?",
            "choices": {
                "A": "A single application of force exceeding the material's ultimate strength",
                "B": "Progressive microscopic crack growth from millions of repeated loading cycles, even at forces well below the material's breaking strength",
                "C": "Chemical corrosion that dissolves the material from the outside",
                "D": "Gravitational settling that gradually lowers the bridge over decades"
            },
            "correct": "B",
            "feedback_correct": "Correct. Material fatigue is insidious because each individual load is safely below the material's capacity. But millions of cycles create microscopic cracks that grow invisibly until they reach a critical length, at which point the structure fails suddenly without warning.",
            "feedback_incorrect": "Consider why fatigue is different from simple overloading. A paper clip does not break on the first bend or the second. But after enough bending cycles, it snaps. The same principle applies to bridge materials under repeated traffic loads."
        },
        {
            "question": "A truss bridge distributes forces primarily through which combination of force types?",
            "choices": {
                "A": "Magnetic attraction and electrical resistance",
                "B": "Tension in lower members that are being pulled and compression in upper members that are being pushed",
                "C": "Friction between the bridge deck and vehicle tires",
                "D": "Centripetal force that curves the load around the bridge structure"
            },
            "correct": "B",
            "feedback_correct": "Correct. A truss converts applied loads into tension (pulling forces in the bottom chord and diagonals) and compression (pushing forces in the top chord and verticals). This distribution allows efficient load-bearing using relatively lightweight triangular members.",
            "feedback_incorrect": "Think about what happens to the structural members when a heavy truck drives across a truss bridge. Some members are stretched (pulled apart) and some are squeezed (pushed together). These are the two fundamental force types in structures."
        },
        {
            "question": "Which factor is most important in determining whether a bridge lasts 30 years or 80 years, assuming it was properly designed and constructed?",
            "choices": {
                "A": "The color of the paint used on the bridge",
                "B": "The frequency and quality of inspection and maintenance that catches fatigue damage before it reaches critical levels",
                "C": "The number of pedestrians who walk across the bridge daily",
                "D": "The geographic latitude where the bridge is located"
            },
            "correct": "B",
            "feedback_correct": "Correct. All bridges accumulate fatigue damage over time. The difference between a bridge that lasts decades longer is whether inspections catch growing cracks before they reach critical failure length. Regular maintenance can repair damage and extend service life dramatically.",
            "feedback_incorrect": "Consider that all bridges degrade over time. The question is whether that degradation is detected and repaired before it becomes dangerous. Which factor directly addresses the detection and repair of accumulating damage?"
        },
        {
            "question": "A bridge designer must choose between a beam bridge, an arch bridge, and a suspension bridge for a 500-meter span across a river. Which design is most suitable for this span length?",
            "choices": {
                "A": "A beam bridge, which is ideal for spans of any length",
                "B": "An arch bridge, which is most efficient for spans under 50 meters",
                "C": "A suspension bridge, which can span long distances by transferring deck loads through cables to main cables and towers that direct forces into compression",
                "D": "None of these designs can span 500 meters"
            },
            "correct": "C",
            "feedback_correct": "Correct. Suspension bridges excel at long spans (hundreds to thousands of meters) because they transfer the deck's weight through vertical cables to main cables that carry the load in tension to towers, which direct forces downward in compression to the foundation. This efficient force path enables very long spans.",
            "feedback_incorrect": "Consider how each bridge type handles long distances. Beam bridges sag under their own weight over long spans. Arch bridges are limited by the arch geometry. Suspension bridges use cables to transfer loads to towers, enabling spans that other designs cannot achieve."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's 50-year simulation shows that Structural Integrity decreases linearly for the first 30 years but then drops exponentially in years 30-40 when maintenance is deferred. Which explanation best accounts for this nonlinear transition?",
            "choices": {
                "A": "The material suddenly becomes weaker at the 30-year mark due to age",
                "B": "Without maintenance to repair small cracks, fatigue damage compounds: existing cracks accelerate the growth of new cracks through stress concentration, creating a self-reinforcing degradation cycle",
                "C": "Traffic volume always increases exponentially after 30 years",
                "D": "The simulation model switches to a different equation at year 30"
            },
            "correct": "B",
            "feedback_correct": "Correct. Deferred maintenance allows fatigue cracks to grow past the point where they concentrate stress at their tips, accelerating further crack growth. Small cracks that could have been cheaply repaired become large cracks that create stress concentrations, which generate more cracks. The degradation becomes self-reinforcing.",
            "feedback_incorrect": "Consider what happens when small fatigue cracks are not repaired. A crack concentrates stress at its tip, making that location more likely to crack further. This self-reinforcing process means crack growth accelerates over time, especially when maintenance that would have interrupted this cycle is skipped."
        },
        {
            "question": "The model compares three bridge designs under identical loading: beam, truss, and arch. The truss bridge shows the most even force distribution across its members, while the beam bridge shows high stress concentration at midspan. What structural principle explains this difference?",
            "choices": {
                "A": "Truss bridges are always made of stronger materials than beam bridges",
                "B": "The truss geometry converts bending forces into axial tension and compression distributed across many triangular members, while the beam concentrates bending stress at a single cross-section",
                "C": "Beam bridges receive more traffic than truss bridges",
                "D": "Truss bridges weigh less than beam bridges, so they experience less force"
            },
            "correct": "B",
            "feedback_correct": "Correct. The fundamental advantage of a truss is geometric: triangular elements convert applied bending loads into axial forces (pure tension or compression) in individual members. This distributes stress across many members rather than concentrating it at the critical midspan section of a beam.",
            "feedback_incorrect": "Think about why triangles are structurally efficient. A single beam must resist bending at its weakest point (midspan). A truss breaks the same load into many smaller tension and compression forces in individual members. The same total load is shared across the structure."
        },
        {
            "question": "A student's model predicts that doubling the maintenance inspection frequency extends bridge service life by 40%, while doubling the factor of safety at design only extends it by 15%. Which analysis best explains why maintenance has a larger effect than initial overdesign?",
            "choices": {
                "A": "Maintenance is always cheaper than building a stronger bridge",
                "B": "A higher factor of safety delays the onset of critical damage but does not stop fatigue accumulation, while regular inspections catch and repair damage before it enters the exponential growth phase, resetting the degradation clock",
                "C": "The factor of safety has no effect on bridge longevity",
                "D": "Maintenance makes the bridge stronger than its original design"
            },
            "correct": "B",
            "feedback_correct": "Correct. The factor of safety provides a larger initial margin before reaching critical levels, but fatigue still accumulates at the same rate. Maintenance actively interrupts the damage accumulation process by repairing cracks before they enter the self-reinforcing exponential growth phase, providing a much larger net benefit.",
            "feedback_incorrect": "Consider what each intervention actually does. Doubling the factor of safety means starting with more margin but still accumulating damage at the same rate. Maintenance catches and repairs damage, effectively restarting the clock. Which approach addresses the ongoing process rather than just the starting point?"
        },
        {
            "question": "The simulation reveals that a bridge designed for 20,000 vehicles per day is now carrying 35,000 per day. The model predicts failure 18 years earlier than the original design life. A student argues this is solely the result of increased load exceeding the factor of safety. Which model-based critique identifies the missing factor?",
            "choices": {
                "A": "The student's analysis is complete and correct",
                "B": "The student ignores the fatigue acceleration: 75% more load cycles per day means fatigue damage accumulates 75% faster, and fatigue failure can occur even while the instantaneous load remains within the factor of safety margin",
                "C": "The bridge should be able to handle any amount of traffic because it was overdesigned",
                "D": "Vehicle weight has not changed, so the total load is the same"
            },
            "correct": "B",
            "feedback_correct": "Correct. The student focused only on peak load versus capacity, missing the critical fatigue component. Even if each individual truck is within the load limit, 75% more cycles per day means 75% more fatigue damage accumulation. Fatigue failure depends on cumulative cycles, not just peak force.",
            "feedback_incorrect": "The student is thinking about static load (can the bridge hold the weight right now?) but missing the dynamic effect. Material fatigue depends on the NUMBER of loading cycles, not just the magnitude of each cycle. More vehicles means more cycles, which means faster fatigue accumulation."
        },
        {
            "question": "Based on the complete model analysis, which policy recommendation is best supported by the evidence for preventing bridge failures?",
            "choices": {
                "A": "Build all bridges with a factor of safety of 10.0 to ensure they never fail",
                "B": "Reduce traffic on all bridges to 50% of design capacity",
                "C": "Implement risk-based inspection schedules that increase inspection frequency as bridges age and approach their fatigue damage thresholds, with mandatory repair protocols for detected damage",
                "D": "Replace all bridges every 20 years regardless of condition"
            },
            "correct": "C",
            "feedback_correct": "Correct. The model shows that fatigue damage accelerates nonlinearly with age. Risk-based inspection schedules that intensify as bridges age match the inspection frequency to the increasing risk, catching damage during the early growth phase when repairs are effective and affordable.",
            "feedback_incorrect": "The model showed that fatigue accumulation accelerates over time and that early detection through inspection is the most effective intervention. Consider which policy matches inspection effort to risk level throughout the bridge's life."
        }
    ]
}

# =============================================================================
# L08: How Do Noise-Canceling Headphones Work?
# NGSS: HS-PS4-1, HS-PS4-5 (Wave relationships, wave-based technology)
# =============================================================================
L08_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Noise-canceling headphones eliminate unwanted sound through which physical principle?",
            "choices": {
                "A": "Blocking sound waves from entering the ear by using thick padding as a physical barrier",
                "B": "Destructive interference, where a generated anti-phase sound wave combines with the noise wave to cancel it",
                "C": "Converting sound energy into heat energy through friction in the ear cushions",
                "D": "Increasing the frequency of the noise until it is above the range of human hearing"
            },
            "correct": "B",
            "feedback_correct": "Correct. Active noise cancellation generates an anti-phase signal that is identical to the incoming noise but shifted by 180 degrees. When these two waves combine, their amplitudes cancel through destructive interference, producing silence or significantly reduced noise.",
            "feedback_incorrect": "Active noise cancellation does not block sound or absorb it. Instead, it fights sound with sound. Consider what happens when two waves of equal amplitude but opposite phase occupy the same space."
        },
        {
            "question": "The principle of superposition states that when two waves occupy the same space, the resulting displacement at any point equals which value?",
            "choices": {
                "A": "The displacement of the louder wave only",
                "B": "The algebraic sum of the individual wave displacements at that point",
                "C": "The average of the two wave displacements",
                "D": "Zero, because waves always cancel each other"
            },
            "correct": "B",
            "feedback_correct": "Correct. Superposition is the addition of wave amplitudes at each point. If both waves have positive displacement at a point, they add constructively (louder). If one is positive and the other equally negative, they add destructively (silence). The result depends on the relative phase at each point.",
            "feedback_incorrect": "Superposition is fundamentally about addition. At any given point, you simply add the displacement of wave 1 to the displacement of wave 2. The result can be constructive (louder), destructive (quieter), or anything in between."
        },
        {
            "question": "For complete destructive interference to occur between two sound waves, which conditions must both be met?",
            "choices": {
                "A": "The waves must have different frequencies and random phase relationships",
                "B": "The waves must have the same frequency and amplitude, with a phase difference of exactly 180 degrees (half a wavelength)",
                "C": "The waves must have the same frequency but different amplitudes",
                "D": "The waves must be traveling in the same direction at different speeds"
            },
            "correct": "B",
            "feedback_correct": "Correct. Complete cancellation requires three conditions: same frequency (so the waves stay in phase relationship), same amplitude (so the peaks and troughs are equal in magnitude), and 180-degree phase offset (so peaks of one wave align exactly with troughs of the other).",
            "feedback_incorrect": "For one wave to perfectly cancel another, what must be true? Each peak of the noise wave must be met by an equally deep trough from the canceling wave. This requires matching frequency, matching amplitude, and exact opposite phase alignment."
        },
        {
            "question": "Noise-canceling headphones are significantly more effective at canceling low-frequency sounds (like airplane engine hum) than high-frequency sounds (like human speech). Which physical explanation accounts for this limitation?",
            "choices": {
                "A": "Low-frequency sounds are louder than high-frequency sounds",
                "B": "High-frequency sounds have shorter wavelengths, requiring the electronics to process and generate the anti-phase signal with much tighter timing precision to maintain accurate phase alignment",
                "C": "Human ears are more sensitive to low frequencies, so cancellation seems more effective",
                "D": "High-frequency sounds cannot undergo destructive interference"
            },
            "correct": "B",
            "feedback_correct": "Correct. High frequencies have short wavelengths, meaning a given timing error represents a larger fraction of the wavelength. At 100 Hz (wavelength 3.4 m), a microsecond error is negligible. At 4,000 Hz (wavelength 0.085 m), the same error causes significant phase misalignment, reducing cancellation effectiveness.",
            "feedback_incorrect": "Consider the relationship between frequency and wavelength. Higher frequency means shorter wavelength. A small timing error in generating the anti-phase signal represents a tiny fraction of a long wavelength (low frequency) but a significant fraction of a short wavelength (high frequency)."
        },
        {
            "question": "If a sound wave has a frequency of 200 Hz and travels at 343 m/s through air, what is its wavelength?",
            "choices": {
                "A": "0.58 meters",
                "B": "1.715 meters",
                "C": "68,600 meters",
                "D": "143 meters"
            },
            "correct": "B",
            "feedback_correct": "Correct. Wavelength = speed / frequency = 343 m/s / 200 Hz = 1.715 meters. This relatively long wavelength is why low frequencies are easier to cancel; the anti-phase signal has more temporal margin for error.",
            "feedback_incorrect": "Use the wave equation: wavelength = speed / frequency. Speed of sound in air is 343 m/s, frequency is 200 Hz. Divide speed by frequency to find the wavelength."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's model shows that at 100 Hz, a 5-microsecond timing error in the anti-phase signal reduces cancellation effectiveness by only 2%, but at 5,000 Hz the same error reduces effectiveness by 45%. Which analysis best explains this frequency-dependent sensitivity?",
            "choices": {
                "A": "The electronics work harder at high frequencies, introducing more noise",
                "B": "At 100 Hz (wavelength 3.4 m), 5 microseconds represents 0.05% of the wave period, barely affecting phase alignment; at 5,000 Hz (wavelength 0.069 m), the same delay represents 2.5% of the wave period, creating significant phase misalignment that prevents destructive interference",
                "C": "Low-frequency sounds are naturally quieter, so less cancellation is needed",
                "D": "The model applies different equations for low and high frequencies"
            },
            "correct": "B",
            "feedback_correct": "Correct. Phase accuracy is relative to wavelength, not absolute. A fixed timing error is a small fraction of a long-period wave (low frequency) but a large fraction of a short-period wave (high frequency). This is why the same hardware achieves excellent low-frequency cancellation but poor high-frequency cancellation.",
            "feedback_incorrect": "Think of the timing error as a fraction of the wave's period. At 100 Hz, the period is 0.01 seconds (10 ms), so 5 microseconds is 0.05% of one cycle. At 5,000 Hz, the period is 0.0002 seconds (0.2 ms), so 5 microseconds is 2.5% of one cycle. Which fraction causes more phase misalignment?"
        },
        {
            "question": "The model reveals that when the anti-phase signal has 95% amplitude accuracy but perfect phase alignment, cancellation effectiveness is 90%. When phase accuracy is 95% but amplitude is perfect, cancellation effectiveness drops to 72%. Which conclusion is best supported by this comparison?",
            "choices": {
                "A": "Amplitude and phase contribute equally to cancellation effectiveness",
                "B": "Phase accuracy has a more critical effect on cancellation than amplitude accuracy because even small phase errors create regions where the waves partially reinforce rather than cancel",
                "C": "Amplitude accuracy is more important than phase accuracy",
                "D": "Neither accuracy matters because cancellation is an all-or-nothing phenomenon"
            },
            "correct": "B",
            "feedback_correct": "Correct. Phase errors cause portions of the anti-phase signal to shift from canceling (destructive) to reinforcing (constructive), actively adding energy rather than removing it. Amplitude errors merely leave residual noise proportional to the mismatch. Phase errors have more severe consequences because they can reverse the intended effect.",
            "feedback_incorrect": "Compare what each type of error does. An amplitude error means the anti-phase signal is slightly too weak (leaving some residual noise) or too strong (adding some extra). A phase error means portions of the waves ADD together instead of canceling. Which has the more severe consequence?"
        },
        {
            "question": "A student proposes improving noise cancellation by adding a second microphone farther from the ear to give the processor more time to compute the anti-phase signal. Based on the model, which evaluation of this proposal is most accurate?",
            "choices": {
                "A": "The proposal would not help because all microphones are equally fast",
                "B": "The proposal is sound: a forward-facing microphone detects noise earlier, giving the processor more time to analyze frequency content and generate an accurate anti-phase signal, particularly improving performance at higher frequencies",
                "C": "Two microphones would create twice as much noise to cancel",
                "D": "The additional microphone would cancel the first microphone's signal"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is exactly how modern feedforward noise cancellation works. An external microphone captures noise before it reaches the ear, providing crucial extra processing time. This advance warning is particularly valuable for higher frequencies, where the short wavelengths demand faster and more precise anti-phase generation.",
            "feedback_incorrect": "Consider the timing problem: the processor needs time to sample the noise, compute the anti-phase signal, and output it before the original noise reaches the ear. A microphone placed farther away detects the noise earlier, giving the processor a head start."
        },
        {
            "question": "The model shows that noise cancellation achieves 28 dB reduction at 100 Hz, 22 dB at 500 Hz, 12 dB at 2,000 Hz, and only 3 dB at 8,000 Hz. A student asks why the headphones do not simply use passive isolation (physical blocking) for high frequencies instead. Based on wave physics, which response is most accurate?",
            "choices": {
                "A": "Passive isolation does not work for any frequency",
                "B": "This is exactly what modern headphones do: high-frequency sounds have short wavelengths that are easily blocked by the physical ear cup padding, while low-frequency long wavelengths diffract around barriers, requiring active cancellation",
                "C": "Passive isolation only works for low frequencies",
                "D": "High frequencies are too quiet to need isolation"
            },
            "correct": "B",
            "feedback_correct": "Correct. This is a fundamental insight about wave behavior: long-wavelength (low-frequency) waves diffract around barriers, making them hard to block physically but their long period makes them easy to cancel actively. Short-wavelength (high-frequency) waves are easily blocked by physical barriers but hard to cancel actively. Modern headphones combine both methods.",
            "feedback_incorrect": "Consider how waves interact with barriers. Long wavelengths bend around obstacles (diffraction), making physical blocking ineffective for low frequencies. Short wavelengths are absorbed or reflected by barriers. Each approach handles different parts of the frequency spectrum."
        },
        {
            "question": "Based on the complete model analysis, a student claims that perfect noise cancellation across all frequencies is theoretically possible with fast enough electronics. Which model-based assessment is most accurate?",
            "choices": {
                "A": "The student is correct because faster processing solves all phase accuracy problems",
                "B": "Even with infinitely fast processing, perfect cancellation faces fundamental limits: the acoustic environment changes continuously, reflected sound arrives from multiple angles and distances, and the ear canal's geometry creates resonances that shift the phase relationship unpredictably",
                "C": "The student is correct because noise cancellation is limited only by processing speed",
                "D": "Perfect cancellation is already achieved by current technology"
            },
            "correct": "B",
            "feedback_correct": "Correct. Processing speed is one limit, but not the only one. Sound reaches the ear from multiple directions with different delays, the listener's head movement changes the acoustic geometry, ear canal resonances alter phase relationships, and environmental noise is constantly changing. These physical realities impose limits beyond processing speed.",
            "feedback_incorrect": "Consider all the factors that affect whether two waves cancel perfectly. The anti-phase signal must match the noise at the exact point where the eardrum is. But sound reflects off surfaces, arrives from multiple angles, and the listener moves. Can a single speaker perfectly cancel a complex, changing acoustic field?"
        }
    ]
}

# =============================================================================
# L09: Could We Actually Mine Asteroids?
# NGSS: HS-ESS1-4, HS-ETS1-3 (Orbital mechanics, design solutions with constraints)
# =============================================================================
L09_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "Delta-v is the most important parameter in space mission planning. What does it measure?",
            "choices": {
                "A": "The maximum speed a spacecraft can reach in a straight line",
                "B": "The total change in velocity a spacecraft needs to accomplish throughout a mission, which determines fuel requirements",
                "C": "The distance between Earth and the target asteroid",
                "D": "The mass of the spacecraft at launch"
            },
            "correct": "B",
            "feedback_correct": "Correct. Delta-v (change in velocity) is the sum of all velocity changes needed for orbital maneuvers: escaping Earth, course corrections, matching the asteroid's orbit, and potentially returning. Each meter per second of delta-v requires fuel, and the relationship is exponential.",
            "feedback_incorrect": "Delta-v is not about maximum speed or distance. It represents the total velocity budget for all maneuvers in a mission. Think of it as the total amount of 'pushing' the spacecraft needs to do, which directly determines how much fuel it needs."
        },
        {
            "question": "The Tsiolkovsky rocket equation shows that fuel requirements increase with delta-v in which mathematical relationship?",
            "choices": {
                "A": "Linearly, so doubling delta-v doubles fuel requirements",
                "B": "Exponentially, so doubling delta-v can increase fuel requirements by 10x or more",
                "C": "Logarithmically, so large increases in delta-v require only small increases in fuel",
                "D": "There is no mathematical relationship between delta-v and fuel"
            },
            "correct": "B",
            "feedback_correct": "Correct. The Tsiolkovsky equation contains an exponential function: the mass ratio (fuel mass / payload mass) increases exponentially with delta-v. This means that missions requiring twice the delta-v can need 10x or more fuel, making high delta-v missions prohibitively expensive.",
            "feedback_incorrect": "The rocket equation is fundamentally exponential. Each increment of delta-v requires carrying fuel to accelerate the fuel you are already carrying. This cascading fuel requirement grows exponentially, not linearly, with the total delta-v needed."
        },
        {
            "question": "Three types of asteroids have different compositions: C-type (carbonaceous), S-type (silicaceous), and M-type (metallic). Which type and resource combination is most likely to be economically viable for early space mining?",
            "choices": {
                "A": "M-type asteroids for platinum, because platinum is the most valuable metal",
                "B": "C-type asteroids for water, because water can be converted to rocket fuel and sold in space, avoiding the cost of launching fuel from Earth",
                "C": "S-type asteroids for silicon, because silicon is used in computer chips",
                "D": "All asteroid types are equally profitable because resources are resources"
            },
            "correct": "B",
            "feedback_correct": "Correct. Water from C-type asteroids can be split into hydrogen and oxygen for rocket fuel. Selling fuel in space eliminates the enormous cost of launching fuel from Earth's gravity well ($2,700-$10,000/kg). This in-space fuel market is the most viable early business model because the customer is already in space.",
            "feedback_incorrect": "Consider where the customer is and what they need. Bringing platinum back to Earth means paying the full round-trip cost. Selling water as fuel to spacecraft already in space means the product never needs to enter a gravity well. Which business model avoids the most expensive step?"
        },
        {
            "question": "An asteroid contains an estimated $10 trillion worth of platinum at current Earth market prices. A student claims mining it would make the mining company the richest in history. Which economic critique is most valid?",
            "choices": {
                "A": "The student is correct because the platinum's value is fixed",
                "B": "Flooding the market with 1000x the current platinum supply would crash the price, meaning the resource is worth $10 trillion only as long as it remains unmined",
                "C": "The company would need to sell all the platinum at once to realize its value",
                "D": "Platinum has no industrial uses, so its price would remain stable"
            },
            "correct": "B",
            "feedback_correct": "Correct. Commodity prices are determined by supply and demand. Increasing the platinum supply by 1000x would collapse the price per ounce. The asteroid's $10 trillion valuation assumes current scarcity prices, which would not survive the introduction of that much supply. This is the paradox of abundance.",
            "feedback_incorrect": "Think about supply and demand. Platinum is valuable partly because it is rare. If you suddenly add 1000 times the current supply to the market, what happens to the price per unit? The total value of the resource is not fixed; it depends on how much exists."
        },
        {
            "question": "Near-Earth asteroids (NEAs) are attractive mining targets primarily because of which characteristic?",
            "choices": {
                "A": "They are the largest asteroids in the solar system",
                "B": "They require less delta-v to reach than most other asteroids, and some require less delta-v than reaching the Moon",
                "C": "They always contain the most valuable resources",
                "D": "They are visible to the naked eye from Earth's surface"
            },
            "correct": "B",
            "feedback_correct": "Correct. NEAs orbit within 1.3 AU of the Sun, bringing them close to Earth. Some have orbital characteristics that make them accessible with less delta-v than a Moon mission. Since delta-v drives mission cost exponentially, accessibility is the primary economic advantage of NEAs.",
            "feedback_incorrect": "The key constraint in asteroid mining is mission cost, which is driven by delta-v. NEAs are attractive not because of their size or composition, but because their proximity to Earth reduces the delta-v (and therefore fuel cost) required to reach them."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's model shows that a near-Earth C-type asteroid water mining mission has a positive ROI of 2.3, while a main-belt M-type platinum mining mission has a negative ROI of -0.7. The platinum asteroid contains 50x more valuable resources. Which analysis best explains why the cheaper target is more profitable?",
            "choices": {
                "A": "Water is inherently more valuable than platinum",
                "B": "The exponential relationship between delta-v and fuel cost means the much higher delta-v to the main belt increases mission cost far more than the higher resource value compensates for, and water sold as fuel in space avoids Earth return costs entirely",
                "C": "The model underestimates platinum's value",
                "D": "C-type asteroids are always closer than M-type asteroids"
            },
            "correct": "B",
            "feedback_correct": "Correct. The Tsiolkovsky equation is the key: the main-belt mission requires roughly 3x the delta-v of the NEA mission, but due to exponential fuel scaling, this means roughly 20x the fuel mass and mission cost. The 50x resource advantage cannot overcome the exponential cost penalty. Additionally, water sold in space never needs the expensive Earth return trip.",
            "feedback_incorrect": "Consider the exponential nature of the rocket equation. Higher delta-v does not just add cost linearly. Tripling delta-v can increase fuel requirements by 20x or more. Now compare this exponential cost increase to the 50x resource value difference. Which grows faster?"
        },
        {
            "question": "The model simulation reveals that in-situ resource utilization (ISRU), where mined water is converted to fuel and sold in space, transforms the economics of asteroid mining. Which systems-level explanation best describes why ISRU is transformative?",
            "choices": {
                "A": "ISRU reduces the asteroid's orbital distance",
                "B": "ISRU breaks the Earth launch cost bottleneck: instead of lifting every kilogram of fuel from Earth at $2,700-$10,000/kg, spacecraft refuel from asteroid-derived fuel in space, where the fuel never had to escape Earth's gravity",
                "C": "ISRU makes platinum more valuable",
                "D": "ISRU allows spacecraft to travel faster than the speed of light"
            },
            "correct": "B",
            "feedback_correct": "Correct. ISRU fundamentally changes the economic equation by eliminating the most expensive step: launching fuel from Earth's deep gravity well. A kilogram of water-derived fuel produced in space never paid the $2,700-$10,000/kg Earth launch tax. This transforms space economics from a single-use to a sustainable model.",
            "feedback_incorrect": "Think about what makes space missions so expensive. The single largest cost is launching material from Earth against its gravity. ISRU means fuel produced in space never had to be launched from Earth. How does this change the entire economic model?"
        },
        {
            "question": "A student's model tests three mission profiles: (1) water mining at a near-Earth asteroid, (2) platinum mining at a near-Earth asteroid, and (3) water mining in the main belt. Only mission 1 shows positive ROI. Which variable has the greatest influence on profitability?",
            "choices": {
                "A": "Resource type alone determines profitability",
                "B": "Orbital distance alone determines profitability",
                "C": "The interaction between orbital distance (which drives delta-v and mission cost exponentially) and whether the product can be sold in space (avoiding Earth return costs) together determine profitability",
                "D": "None of the variables significantly affect profitability"
            },
            "correct": "C",
            "feedback_correct": "Correct. Profitability depends on two interacting factors: mission cost (driven exponentially by delta-v from orbital distance) and revenue model (in-space fuel sales vs. Earth return). Mission 1 succeeds because it minimizes BOTH: low delta-v AND no return trip. The other missions fail on one or both dimensions.",
            "feedback_incorrect": "Compare all three missions. Mission 1 (near + water) is profitable. Mission 2 (near + platinum) is not. Mission 3 (far + water) is not. What is different between 1 and 2? Between 1 and 3? The answer involves the interaction of two variables."
        },
        {
            "question": "The model shows that a 500-meter M-type asteroid at 2.5 AU contains $5 trillion in platinum group metals, but the mission cost is $8 trillion. A student proposes waiting for the asteroid to pass closer to Earth in its orbit. Based on orbital mechanics, which assessment is most accurate?",
            "choices": {
                "A": "All asteroids eventually pass close enough to Earth for profitable mining",
                "B": "Main-belt asteroids have relatively circular orbits that never bring them close to Earth; only near-Earth asteroids (which cross Earth's orbital region) have close approach windows that temporarily reduce delta-v requirements",
                "C": "Waiting will always make missions cheaper because fuel prices decrease over time",
                "D": "Orbital distance is irrelevant to mission cost"
            },
            "correct": "B",
            "feedback_correct": "Correct. Main-belt asteroids orbit between Mars and Jupiter in relatively circular paths that never approach Earth. Their delta-v requirements are fundamentally high regardless of timing. Only NEAs, which have eccentric orbits crossing Earth's orbital region, offer periodic close approaches that reduce delta-v. The student's proposal confuses the two populations.",
            "feedback_incorrect": "Consider where main-belt asteroids orbit (between Mars and Jupiter) versus where near-Earth asteroids orbit (crossing Earth's region). A main-belt asteroid's orbit never brings it near Earth. Only asteroids with eccentric, Earth-crossing orbits have periodic close approaches."
        },
        {
            "question": "Based on the complete model analysis, which business strategy is best supported by the evidence for the first generation of asteroid mining companies?",
            "choices": {
                "A": "Target the most valuable M-type asteroids in the main belt to maximize resource returns",
                "B": "Mine water from accessible near-Earth C-type asteroids and sell it as in-space fuel, building infrastructure and reducing costs for future missions to more distant, resource-rich targets",
                "C": "Wait for technology to improve enough to make any mission profitable",
                "D": "Mine platinum from near-Earth asteroids and return it to Earth for maximum profit"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model shows that the infrastructure-first strategy is the only profitable path. Water mining at low delta-v targets generates revenue from in-space fuel sales while building the refueling infrastructure that reduces costs for all subsequent missions. This creates a flywheel effect: each successful mission makes the next one cheaper.",
            "feedback_incorrect": "The model showed that mission cost (driven by delta-v) and Earth return costs are the two biggest barriers. Which strategy addresses both simultaneously while creating infrastructure that reduces costs for future, more ambitious missions?"
        }
    ]
}

# =============================================================================
# L10: Why Do Pandemics Spiral Out of Control?
# NGSS: HS-LS2-2, HS-LS4-6 (Population dynamics, mitigating human impacts)
# =============================================================================
L10_QUESTIONS = {
    "mc_pre_assessment": [
        {
            "question": "A disease has a basic reproduction number (R0) of 3.0. In a fully susceptible population, what does this value indicate?",
            "choices": {
                "A": "The disease will infect exactly 3 people total before dying out",
                "B": "Each infected person will, on average, transmit the disease to 3 new people, causing exponential growth",
                "C": "The disease has a 3% chance of causing a pandemic",
                "D": "Three people must be infected simultaneously for the disease to spread"
            },
            "correct": "B",
            "feedback_correct": "Correct. R0 = 3 means each infected individual infects 3 others on average in a fully susceptible population. This creates exponential growth: 1 becomes 3, 3 becomes 9, 9 becomes 27. Any R0 greater than 1 indicates the outbreak will grow rather than die out.",
            "feedback_incorrect": "R0 is a multiplication factor per generation of infection. If one person infects 3, and each of those infects 3 more, the number grows as a power of 3 with each generation. Calculate: 3, 9, 27, 81. This is exponential growth."
        },
        {
            "question": "In the SIR model of infectious disease, people flow through three compartments. Which sequence correctly describes this flow?",
            "choices": {
                "A": "Recovered to Infected to Susceptible",
                "B": "Susceptible to Infected to Recovered",
                "C": "Infected to Susceptible to Recovered",
                "D": "Susceptible to Recovered to Infected"
            },
            "correct": "B",
            "feedback_correct": "Correct. In the SIR model, individuals start as Susceptible (can be infected), move to Infected (have the disease and can transmit it), and then move to Recovered (immune and no longer transmitting). The rate of flow between compartments determines the epidemic curve.",
            "feedback_incorrect": "Think about the natural progression of disease in a person: first they are vulnerable to catching it (Susceptible), then they catch it (Infected), then they recover with immunity (Recovered). This one-directional flow is the foundation of the SIR model."
        },
        {
            "question": "SARS (2003) infected 8,098 people and was contained. COVID-19 (2020) infected over 700 million people globally. Both were respiratory viruses originating in Asia. Which factor most likely explains the dramatically different outcomes?",
            "choices": {
                "A": "SARS was a less dangerous virus with lower mortality",
                "B": "COVID-19 had a longer presymptomatic infectious period, allowing infected people to spread the virus before showing symptoms and being identified for isolation",
                "C": "Public health response was identical for both outbreaks",
                "D": "SARS spread through water while COVID-19 spread through air"
            },
            "correct": "B",
            "feedback_correct": "Correct. SARS patients became symptomatic before becoming highly infectious, making them identifiable for isolation before spreading the virus. COVID-19 patients were most infectious 1-2 days BEFORE symptom onset, creating invisible transmission chains that could not be detected through symptom-based surveillance.",
            "feedback_incorrect": "Consider what makes a disease easy or hard to contain. If infected people show symptoms quickly, they can be identified and isolated. If they spread the virus before showing any symptoms, how do you find them? This timing difference between symptoms and infectiousness is critical."
        },
        {
            "question": "The effective reproduction number (Re) differs from R0 in which way?",
            "choices": {
                "A": "Re is always higher than R0",
                "B": "Re accounts for the current population immunity and intervention measures, representing the actual transmission rate at a given point in the epidemic rather than the baseline maximum",
                "C": "Re only applies to the first case in an outbreak",
                "D": "Re measures the total number of people who have recovered"
            },
            "correct": "B",
            "feedback_correct": "Correct. R0 is the theoretical maximum in a fully susceptible population with no interventions. Re adjusts for reality: as people become immune (through infection or vaccination) and interventions are implemented (masks, distancing), Re decreases. When Re drops below 1, the epidemic declines.",
            "feedback_incorrect": "R0 assumes everyone is susceptible and no interventions exist. Re adjusts this number for the actual conditions at any point in the epidemic. As immunity builds and interventions are deployed, the effective transmission rate changes. Which answer describes this adjustment?"
        },
        {
            "question": "An epidemic curve shows a sharp spike followed by a rapid decline. This pattern indicates which of the following?",
            "choices": {
                "A": "The disease is not very contagious",
                "B": "The outbreak grew rapidly through a susceptible population and declined as the susceptible population was exhausted, either through infection or intervention",
                "C": "The disease mutated to become less infectious over time",
                "D": "The population was already immune before the outbreak began"
            },
            "correct": "B",
            "feedback_correct": "Correct. A sharp epidemic curve indicates rapid transmission through a largely susceptible population. The peak occurs when the rate of new infections equals the rate of recoveries. The decline happens as the susceptible pool shrinks (through infection or intervention), reducing Re below 1.",
            "feedback_incorrect": "The shape of an epidemic curve reflects the balance between new infections and the remaining susceptible population. A sharp spike means rapid transmission. The decline means the susceptible pool is shrinking. Why would the susceptible pool shrink? People are either getting infected or getting vaccinated."
        }
    ],
    "mc_post_assessment": [
        {
            "question": "A student's model shows that implementing social distancing on day 10 of an outbreak reduces total infections by 85%, but implementing the same measure on day 30 reduces total infections by only 22%. Which mathematical concept best explains this dramatic difference?",
            "choices": {
                "A": "Social distancing becomes less effective over time because the virus adapts",
                "B": "Exponential growth means the 20-day delay allows the infected population to double approximately 5 times (at a 4-day doubling period), resulting in roughly 32 times more infections at the point of intervention",
                "C": "The model assigns less effectiveness to later interventions",
                "D": "Social distancing only works in the first two weeks of any outbreak"
            },
            "correct": "B",
            "feedback_correct": "Correct. During exponential growth, delays are devastating. With a 4-day doubling period, 20 days represents 5 doublings: 2^5 = 32. Intervening at 32x the infection level means 32x more people are already infected and transmitting. The same intervention is applied to a vastly larger problem, reducing its relative impact dramatically.",
            "feedback_incorrect": "During exponential growth, the number of infected people doubles at a fixed interval. Calculate how many doublings occur in 20 days with a 4-day doubling time: 20/4 = 5 doublings, meaning 2^5 = 32 times more infections. How does intervening against 32x more infections reduce the relative impact?"
        },
        {
            "question": "The model compares an uncontrolled outbreak (R0 = 2.5, no interventions) with a managed outbreak (same R0, vaccination + social distancing started at day 14). The uncontrolled outbreak infects 78% of the population; the managed outbreak infects 31%. A student observes that Re dropped below 1 on day 42 in the managed scenario. What caused Re to cross this critical threshold?",
            "choices": {
                "A": "The virus mutated to become less contagious at day 42",
                "B": "The combination of growing natural immunity from recovered individuals, vaccine-induced immunity, and reduced contact rates from social distancing collectively reduced the susceptible population below the level needed to sustain Re above 1",
                "C": "All infected individuals recovered simultaneously on day 42",
                "D": "The model automatically forces Re below 1 after a fixed number of days"
            },
            "correct": "B",
            "feedback_correct": "Correct. Re = R0 * (susceptible fraction) * (1 - intervention effectiveness). Three factors compound: natural immunity removes people from the susceptible pool, vaccination removes more, and social distancing reduces the transmission probability per contact. Together they pushed the effective susceptible fraction below the epidemic threshold.",
            "feedback_incorrect": "Re is a product of multiple factors: the baseline R0, the fraction of people still susceptible, and the effectiveness of interventions. Each factor that reduces any of these components brings Re closer to 1. The threshold is crossed when their combined effect is sufficient."
        },
        {
            "question": "A student compares two diseases in the model: Disease A (R0 = 2, 14-day infectious period) and Disease B (R0 = 2, 3-day infectious period). Both produce the same peak infection percentage but Disease B's epidemic is over in 45 days while Disease A's lasts 180 days. Which analysis best explains the timeline difference?",
            "choices": {
                "A": "Disease B is more dangerous because it spreads faster",
                "B": "With the same R0 but shorter infectious period, Disease B must have a higher per-day transmission probability. This compresses the same total epidemic into a shorter timeframe because each generation of infection cycles faster, even though the final size is determined by R0",
                "C": "Disease A is less contagious than Disease B",
                "D": "The infectious period has no effect on epidemic timeline"
            },
            "correct": "B",
            "feedback_correct": "Correct. R0 determines the final epidemic size (how many total infections), but the generation time (related to infectious period) determines the speed. Disease B cycles through the S-I-R compartments much faster because each infected person transmits and recovers in 3 days instead of 14, compressing the same total epidemic into fewer days.",
            "feedback_incorrect": "R0 determines how many people are ultimately infected, but the infectious period determines how fast the epidemic progresses. If each generation of infection is 3 days instead of 14, the entire epidemic runs through the population in roughly 1/4.7 the time, even with the same final outcome."
        },
        {
            "question": "The model shows that quarantining 50% of detected cases reduces total infections by 40%, while quarantining 90% of detected cases reduces total infections by 75%. A student notes this is not proportional. Which factor accounts for the diminishing returns?",
            "choices": {
                "A": "Quarantine becomes less effective at higher rates because the virus evolves to escape",
                "B": "Undetected presymptomatic and asymptomatic transmission continues regardless of quarantine rates for detected cases, creating a transmission floor that quarantine alone cannot eliminate",
                "C": "The model incorrectly calculates quarantine effectiveness at high rates",
                "D": "People refuse to comply with quarantine at higher rates"
            },
            "correct": "B",
            "feedback_correct": "Correct. Quarantine can only isolate DETECTED cases. Presymptomatic transmission (before symptoms appear) and asymptomatic transmission (in people who never show symptoms) create chains of invisible spread that are unaffected by quarantine. This undetectable transmission becomes the dominant pathway as quarantine catches more detected cases.",
            "feedback_incorrect": "Consider what quarantine can and cannot do. It isolates people who are KNOWN to be infected. But what about people who are infectious but do not know it yet (presymptomatic) or who never show symptoms (asymptomatic)? These invisible transmitters are unaffected by quarantine."
        },
        {
            "question": "Based on the complete model analysis, a public health official must choose between two strategies with limited resources: (A) achieve 60% vaccination coverage slowly over 6 months, or (B) achieve 40% vaccination coverage quickly in the first 2 months. For a disease with R0 = 2.5 and herd immunity threshold of 60%, which strategy does the model predict will result in fewer total infections, and why?",
            "choices": {
                "A": "Strategy A, because 60% coverage meets the herd immunity threshold",
                "B": "Strategy B, because early vaccination during exponential growth has a disproportionate impact on total infections: reducing Re below 1 even temporarily during the early exponential phase prevents far more infections than reaching a higher final coverage after the epidemic peak has already passed",
                "C": "Both strategies produce identical outcomes because the same number of people are eventually vaccinated",
                "D": "Strategy A, because higher coverage is always better regardless of timing"
            },
            "correct": "B",
            "feedback_correct": "Correct. The model demonstrates that timing matters more than final coverage during exponential growth. Vaccinating 40% of the population in the first 2 months reduces Re during the critical growth phase, potentially preventing millions of infections that would otherwise occur before Strategy A reaches its higher but later coverage target. The epidemic does not wait for vaccination programs to finish.",
            "feedback_incorrect": "Remember the model's key finding about intervention timing: the same action taken 20 days earlier can prevent 85% more infections versus 22%. During exponential growth, speed of deployment matters enormously because each day of delay means dramatically more infections. Apply this principle to the vaccination timing question."
        }
    ]
}

# =============================================================================
# Aggregated question bank
# =============================================================================
ALL_QUESTIONS = {
    "G11L1-L01": L01_QUESTIONS,
    "G11L1-L02": L02_QUESTIONS,
    "G11L1-L03": L03_QUESTIONS,
    "G11L1-L04": L04_QUESTIONS,
    "G11L1-L05": L05_QUESTIONS,
    "G11L1-L06": L06_QUESTIONS,
    "G11L1-L07": L07_QUESTIONS,
    "G11L1-L08": L08_QUESTIONS,
    "G11L1-L09": L09_QUESTIONS,
    "G11L1-L10": L10_QUESTIONS,
}
