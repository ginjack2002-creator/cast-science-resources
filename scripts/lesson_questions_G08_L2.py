#!/usr/bin/env python3
"""Multiple choice post-assessment questions for Grade 8 Level 2 ModelIt! Lessons"""

# =============================================================================
# G08L2-L01: Survival of the Fittest: Can You Outrun Natural Selection?
# NGSS: MS-LS4-4, MS-LS4-6
# =============================================================================
L01_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "In your model, a population with 80% genetic diversity survived a severe drought, while a population with 20% diversity collapsed. Which explanation is best supported by the model evidence?",
            "choices": {
                "A": "The diverse population evolved new drought-resistant traits during the drought",
                "B": "The diverse population already contained individuals with drought-resistant traits that natural selection could favor",
                "C": "The diverse population was physically stronger and could endure more heat",
                "D": "The diverse population cooperated better to share water resources"
            },
            "correct": "B",
            "feedback_correct": "Correct! Natural selection acts on traits that already exist. The diverse population had a wider range of pre-existing traits, making it more likely that some individuals already carried drought-resistant variations. Selection favored those individuals.",
            "feedback_incorrect": "Natural selection does not create new traits during a crisis. It selects from variation that already exists. A diverse population is more likely to already contain individuals with traits suited to new conditions, giving natural selection more raw material to work with."
        },
        {
            "question": "Your model shows that Favorable Trait Frequency increased from 15% to 80% over 10 generations under high Environmental Pressure. Which component relationship explains this shift?",
            "choices": {
                "A": "Environmental Pressure directly created favorable traits in the population",
                "B": "Survival Rate increased because the environment became less harsh over time",
                "C": "Individuals with favorable traits survived and reproduced at higher rates, passing those traits to offspring",
                "D": "Reproduction Rate decreased, which concentrated favorable traits in fewer individuals"
            },
            "correct": "C",
            "feedback_correct": "Correct! This is natural selection in action. Individuals with favorable traits had higher survival rates, reproduced more, and passed those traits to the next generation. Over multiple generations, the frequency of favorable traits increased predictably.",
            "feedback_incorrect": "Environmental pressure does not create traits. The shift occurs because individuals with favorable traits survive and reproduce at higher rates. Each generation has a larger proportion of favorable traits because the previous generation's survivors carried those traits."
        },
        {
            "question": "A student claims that natural selection is random because mutations are random. Using evidence from your model, which response best addresses this claim?",
            "choices": {
                "A": "The student is correct because all aspects of evolution are random",
                "B": "The student is partially correct because both mutations and selection are random processes",
                "C": "The student is incorrect because while mutations are random, natural selection is directional, consistently favoring traits that match the environment",
                "D": "The student is incorrect because mutations are not random either"
            },
            "correct": "C",
            "feedback_correct": "Correct! Mutations are random, but natural selection is not. In the model, increasing Environmental Pressure consistently and predictably reduced Survival Rate for individuals without favorable traits. Selection always favors traits that match the current environment.",
            "feedback_incorrect": "Mutations arise randomly, but natural selection is a directional, non-random process. The model demonstrates this: under the same environmental pressure, favorable traits consistently increase in frequency. The outcomes are predictable, not random."
        },
        {
            "question": "Two populations face the same environmental pressure of 90%. Population A has 80% diversity and stabilizes at 70% favorable trait frequency. Population B has 20% diversity and crashes toward extinction. What does this model evidence reveal about conservation?",
            "choices": {
                "A": "Endangered species should be moved to environments with less pressure",
                "B": "Maintaining genetic diversity in a population is critical because it provides the variation natural selection needs to drive adaptation",
                "C": "Population size is more important than genetic diversity for survival",
                "D": "Populations always adapt if given enough time, regardless of diversity"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model shows that genetic diversity is the raw material for natural selection. Without sufficient diversity, a population may lack individuals with traits suited to new conditions, leaving natural selection nothing to work with.",
            "feedback_incorrect": "The model directly compares high and low diversity under identical pressure. The high-diversity population survived because it contained individuals with favorable traits. The low-diversity population lacked those traits entirely. Diversity, not just size or time, determines adaptive potential."
        },
        {
            "question": "In your model, Reproduction Rate feeds back into Favorable Trait Frequency, creating a cycle. What does this feedback relationship represent in biological terms?",
            "choices": {
                "A": "Organisms that reproduce more always create offspring with new, better traits",
                "B": "Surviving individuals with favorable traits reproduce and increase the proportion of favorable traits in the next generation",
                "C": "Higher reproduction rate causes the environment to become less harsh",
                "D": "Reproduction rate has no effect on which traits become more common"
            },
            "correct": "B",
            "feedback_correct": "Correct! This feedback loop IS natural selection. Individuals with favorable traits survive, reproduce, and pass those traits to offspring. Each generation has a higher proportion of favorable traits, which increases survival rates further, creating a reinforcing cycle.",
            "feedback_incorrect": "Reproduction does not create new traits. The feedback loop works because surviving individuals disproportionately carry favorable traits. When they reproduce, their offspring inherit those traits, increasing favorable trait frequency in the next generation."
        }
    ]
}

# =============================================================================
# G08L2-L02: Trophic Cascades: When Predators Disappear
# NGSS: MS-LS2-1, MS-LS2-4
# =============================================================================
L02_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "In your trophic cascade model, removing the Apex Predator Population caused Erosion Rate to spike. Which chain of cause-and-effect relationships from the model explains this?",
            "choices": {
                "A": "No predators caused soil to become drier, leading to erosion",
                "B": "No predators led to herbivore explosion, which overgrazed vegetation, which exposed bare soil to erosion",
                "C": "No predators caused direct physical damage to soil through increased animal movement",
                "D": "No predators meant fewer decomposers, which weakened the soil structure"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model traces a clear causal chain: predator removal leads to unchecked herbivore growth, which leads to overgrazing and vegetation decline, which leads to bare soil vulnerable to wind and water erosion. This is a trophic cascade.",
            "feedback_incorrect": "The cascade follows a step-by-step chain through the food web. Predators control herbivores, herbivores consume vegetation, and vegetation holds soil in place. Remove the first link, and the effects cascade through all downstream components."
        },
        {
            "question": "Your model shows that after predator reintroduction at 50%, ecosystem recovery took significantly longer than the original collapse. What does this asymmetry demonstrate?",
            "choices": {
                "A": "Predators are ineffective at controlling herbivore populations once they have grown too large",
                "B": "Degraded ecosystems can become trapped in unhealthy stable states where damage is self-reinforcing, making recovery slower than collapse",
                "C": "The model is inaccurate because recovery should take the same amount of time as collapse",
                "D": "Herbivores evolved resistance to predation during the absence of predators"
            },
            "correct": "B",
            "feedback_correct": "Correct! Ecosystem degradation can be self-reinforcing. Bare, eroded soil cannot support new plant growth, which keeps herbivores concentrated on remaining vegetation, preventing recovery. Breaking out of this degraded state requires more time than the original collapse.",
            "feedback_incorrect": "The asymmetry between collapse and recovery is a real phenomenon in ecology. Degraded ecosystems develop self-reinforcing patterns: eroded soil resists revegetation, which maintains overgrazing pressure. This is why conservation focuses on prevention over restoration."
        },
        {
            "question": "A student argues that removing wolves from a park should only affect elk, since wolves only eat elk. Using your model, which evidence contradicts this claim?",
            "choices": {
                "A": "Wolves occasionally eat plants, which directly affects vegetation",
                "B": "Removing predators triggers a cascade through herbivore, vegetation, erosion, and ecosystem stability components, affecting the entire system",
                "C": "Wolves are decomposers that recycle nutrients in the soil",
                "D": "Wolves control the weather patterns that affect vegetation growth"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model shows that changes at one trophic level cascade through the entire system. Wolves affect elk, elk affect vegetation, vegetation affects erosion, and erosion affects ecosystem stability. Four components change from removing just one.",
            "feedback_incorrect": "Ecosystems are interconnected networks, not isolated predator-prey pairs. The model demonstrates that removing wolves triggers changes through herbivore populations, vegetation health, erosion rates, and overall ecosystem stability. Indirect effects are as powerful as direct ones."
        },
        {
            "question": "In the model, Vegetation Health has a POSITIVE relationship with Ecosystem Stability and a NEGATIVE relationship with Erosion Rate. If Vegetation Health drops to 20%, what does the model predict?",
            "choices": {
                "A": "Ecosystem Stability increases because there is less competition among plants",
                "B": "Erosion Rate decreases because there are fewer roots disrupting the soil",
                "C": "Erosion Rate increases dramatically while Ecosystem Stability declines, creating compounding damage",
                "D": "Both Erosion Rate and Ecosystem Stability remain unchanged because they are independent of vegetation"
            },
            "correct": "C",
            "feedback_correct": "Correct! Low vegetation means less root structure to hold soil (higher erosion) AND less habitat and food for diverse species (lower ecosystem stability). These effects compound each other, accelerating ecosystem decline.",
            "feedback_incorrect": "Vegetation health directly affects both erosion and ecosystem stability. Plant roots hold soil in place, so less vegetation means more erosion. Plants also provide habitat and food for other species, so less vegetation reduces overall ecosystem health."
        },
        {
            "question": "Based on your model data, a wildlife manager must choose between two strategies for a park with no predators. Which strategy does the model evidence best support?",
            "choices": {
                "A": "Plant new vegetation to directly restore soil cover and stop erosion",
                "B": "Reintroduce apex predators to restore top-down control, which will cascade through herbivores, vegetation, and erosion over time",
                "C": "Reduce erosion with artificial barriers, which will allow vegetation to regrow naturally",
                "D": "Remove herbivores entirely so vegetation can recover without grazing pressure"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model shows that the root cause of the cascade is predator loss. Reintroducing predators addresses the source of the problem, restoring the top-down control mechanism that regulates the entire cascade chain. Treating downstream symptoms alone does not fix the underlying cause.",
            "feedback_incorrect": "The model identifies predator removal as the root cause of the cascade. While treating downstream effects (erosion, vegetation) provides temporary relief, only restoring top-down predator control addresses the fundamental cause and allows the entire cascade to reverse."
        }
    ]
}

# =============================================================================
# G08L2-L03: Why Baking Soda Explodes: Reaction Rates and Energy
# NGSS: MS-PS1-2, MS-PS1-5
# =============================================================================
L03_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "In your model, both the 'Maximum Explosion' and 'Slow Fizz' scenarios produced the same final amount of CO2 gas. Which principle does this evidence demonstrate?",
            "choices": {
                "A": "Faster reactions always produce more gas than slower reactions",
                "B": "The amount of product depends on the amount of reactant, not the speed of the reaction",
                "C": "Surface area determines how much product is formed",
                "D": "Gas production is independent of both reactant amount and surface area"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model shows that reaction rate (speed) and total product (amount) are different things. Surface area affects how fast the reaction proceeds, but the total CO2 produced depends on how much baking soda and vinegar reacted. Same reactant amount means same product amount.",
            "feedback_incorrect": "Reaction speed and total product are separate concepts. Surface area changes the rate (how fast), but the amount of product depends on the amount of reactant. Both scenarios had the same reactant amount, so they produced the same total CO2, just at different speeds."
        },
        {
            "question": "A student weighs a sealed bag containing baking soda and vinegar before and after the reaction. The mass stays the same. Then the student opens the bag, and the mass decreases. Which explanation is supported by the model?",
            "choices": {
                "A": "The chemical reaction destroyed some atoms when the bag was opened",
                "B": "CO2 gas produced during the reaction has mass and escaped when the bag was opened, but no atoms were created or destroyed",
                "C": "The plastic bag absorbed some of the mass during the reaction",
                "D": "Opening the bag allowed new atoms to enter, changing the measurement"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model demonstrates conservation of mass. In the sealed bag, total mass was constant because all products (including CO2 gas) remained inside. Opening the bag allowed CO2 to escape, carrying its mass with it. No atoms were created or destroyed.",
            "feedback_incorrect": "Atoms are never created or destroyed in chemical reactions. The sealed bag proved conservation of mass. When opened, CO2 gas escaped into the air, reducing the mass on the scale. The 'missing' mass is the CO2 that floated away."
        },
        {
            "question": "Your model shows that increasing Surface Area from 20% to 100% dramatically increased Reaction Rate, even though Reactant Amount stayed the same. What particle-level explanation supports this?",
            "choices": {
                "A": "Powder has more atoms than chunks of the same mass",
                "B": "Powder exposes more reactant particles for contact with vinegar, increasing collision frequency and reaction speed",
                "C": "Powder is chemically different from chunks because grinding changes the molecular structure",
                "D": "Powder dissolves in vinegar while chunks do not react at all"
            },
            "correct": "B",
            "feedback_correct": "Correct! Grinding baking soda into powder increases the surface area exposed to vinegar without changing the total amount. More exposed particles means more simultaneous collisions between reactants, dramatically increasing reaction speed.",
            "feedback_incorrect": "Grinding does not change the chemical identity or number of atoms. It increases the surface area exposed to the other reactant. More exposed particles mean more collisions per second between baking soda and vinegar molecules, which is why the reaction proceeds faster."
        },
        {
            "question": "The model shows a NEGATIVE relationship from Reaction Rate back to Reactant Amount. What does this represent in the chemical reaction?",
            "choices": {
                "A": "Faster reactions produce less product than slower reactions",
                "B": "The reaction destroys atoms, reducing the total amount of matter",
                "C": "As the reaction proceeds, reactants are consumed and converted into products, decreasing the remaining reactant",
                "D": "Reaction rate naturally decreases over time regardless of reactant supply"
            },
            "correct": "C",
            "feedback_correct": "Correct! This negative feedback represents reactant consumption. As baking soda and vinegar react, they are converted into sodium acetate, water, and CO2. The reactants are used up as products form. The atoms are rearranged, not destroyed.",
            "feedback_incorrect": "The negative relationship reflects that reactants are consumed during the reaction. As baking soda reacts with vinegar, both are converted into new products. This is why reactions eventually slow down and stop. The atoms are rearranged into new molecules, not destroyed."
        },
        {
            "question": "Based on your model, a student wants to design an experiment that produces the most intense and fastest reaction possible. Which combination of model inputs should they use, and why?",
            "choices": {
                "A": "Low Reactant Amount and high Surface Area, because surface area is the only factor that matters",
                "B": "High Reactant Amount and low Surface Area, because more reactant always means a faster reaction",
                "C": "High Reactant Amount and high Surface Area, because both inputs positively affect Reaction Rate",
                "D": "Low Reactant Amount and low Surface Area, to conserve materials while still getting a reaction"
            },
            "correct": "C",
            "feedback_correct": "Correct! The model shows that both Reactant Amount and Surface Area have POSITIVE relationships with Reaction Rate. Maximizing both inputs produces the most particles available (high amount) with the most exposed surface for collisions (high surface area), creating the fastest, most intense reaction.",
            "feedback_incorrect": "The model clearly shows that both inputs independently increase Reaction Rate. More reactant means more particles overall, and more surface area means more particles exposed for collisions. Maximizing both simultaneously produces the most intense reaction."
        }
    ]
}

# =============================================================================
# G08L2-L04: Climate Feedback Loops: Why Small Changes Get Big
# NGSS: MS-ESS2-6, MS-ESS3-5
# =============================================================================
L04_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "Your model shows that at 90% CO2 Emissions Rate, Global Temperature increases exponentially rather than linearly. Which model feature explains this acceleration?",
            "choices": {
                "A": "CO2 directly heats the atmosphere without any intermediate steps",
                "B": "The positive feedback loop where warming reduces ice, which lowers albedo, which causes more warming, amplifies the initial CO2 effect",
                "C": "Higher CO2 levels cause the sun to emit more radiation",
                "D": "Temperature increases always follow an exponential pattern regardless of the cause"
            },
            "correct": "B",
            "feedback_correct": "Correct! The feedback loop amplifies the initial warming. CO2 raises temperature, which melts ice, which reduces albedo (reflectivity), which causes Earth to absorb more sunlight, which raises temperature further. Each cycle through the loop adds more warming beyond what CO2 alone would cause.",
            "feedback_incorrect": "The acceleration occurs because of the feedback loop, not because of a direct linear relationship. Each degree of warming melts more ice, which exposes dark surfaces that absorb more heat, which causes additional warming beyond the CO2 greenhouse effect. This self-reinforcing cycle creates exponential, not linear, growth."
        },
        {
            "question": "In the model, Albedo has a NEGATIVE relationship with Global Temperature. A student is confused because lower albedo causes higher temperature, which seems like it should be positive. Which explanation correctly resolves this?",
            "choices": {
                "A": "The relationship is mislabeled in the model and should be positive",
                "B": "Higher albedo reflects more sunlight away from Earth, which cools the surface. The negative sign means the two values move in opposite directions.",
                "C": "Albedo and temperature are not actually related in the model",
                "D": "The negative sign indicates that albedo destroys thermal energy"
            },
            "correct": "B",
            "feedback_correct": "Correct! In system models, a negative relationship means the values move in opposite directions. Higher albedo means more reflection and LOWER temperature. Lower albedo means more absorption and HIGHER temperature. The negative sign correctly describes this inverse relationship.",
            "feedback_incorrect": "A negative relationship in a system model means the two components move in opposite directions. When albedo goes UP (more reflection), temperature goes DOWN (less absorption). When albedo goes DOWN (less reflection), temperature goes UP (more absorption). This is correctly labeled as negative."
        },
        {
            "question": "The model shows that even after CO2 Emissions Rate is reduced to 0%, Global Temperature continues rising for several decades. What does this evidence reveal about the climate system?",
            "choices": {
                "A": "The model is flawed because temperature should immediately decrease when emissions stop",
                "B": "The feedback loop has its own momentum. Reduced ice cover continues absorbing extra sunlight, maintaining warming even without new CO2 input",
                "C": "CO2 stays in the atmosphere forever and never breaks down",
                "D": "Reducing emissions has no effect on climate change"
            },
            "correct": "B",
            "feedback_correct": "Correct! The feedback loop has inertia. Even without new CO2, the already-reduced ice cover continues absorbing more sunlight than ice would, maintaining warming. The system needs time to re-freeze ice and restore albedo. This is why prevention is easier than reversal.",
            "feedback_incorrect": "The continued warming demonstrates system inertia. The feedback loop operates independently of emissions once started: less ice means lower albedo, which means more heat absorption, which prevents new ice formation. Stopping emissions removes the input but does not immediately reverse the feedback cycle."
        },
        {
            "question": "A student claims that the ice-albedo feedback loop is a 'positive feedback' that produces positive results for Earth. Using the model, which response best corrects this misunderstanding?",
            "choices": {
                "A": "The student is correct because positive feedback always produces beneficial outcomes",
                "B": "In systems science, 'positive' means the feedback amplifies the original change, not that the outcome is good. The ice-albedo loop amplifies warming, which has harmful consequences.",
                "C": "The feedback is actually negative because it produces harmful effects",
                "D": "The terms 'positive' and 'negative' have no specific meaning in feedback systems"
            },
            "correct": "B",
            "feedback_correct": "Correct! In systems science, 'positive' describes the direction of amplification, not the desirability of the outcome. A positive feedback loop pushes change further in the same direction. The ice-albedo loop amplifies warming, making it worse, even though the word 'positive' might suggest something good.",
            "feedback_incorrect": "'Positive' in feedback loop terminology means amplifying, not beneficial. A positive feedback loop pushes a system further from its starting point. A negative feedback loop would dampen change and return the system toward balance. The ice-albedo loop amplifies warming, which is the definition of positive feedback."
        },
        {
            "question": "Using your model, you must advise a city council on climate action. The model shows that intervening at CO2 Emissions Rate has the largest effect on all downstream components. Why is this the most effective intervention point?",
            "choices": {
                "A": "Because CO2 is the only component that humans can control",
                "B": "Because CO2 Emissions Rate is the external input that drives the entire feedback loop. Reducing it lowers Atmospheric CO2, which slows temperature rise, which preserves ice, which maintains albedo.",
                "C": "Because reducing CO2 immediately reverses all warming that has already occurred",
                "D": "Because CO2 is the most expensive component to address"
            },
            "correct": "B",
            "feedback_correct": "Correct! CO2 Emissions Rate is the only external input in the model. All other components are internal and respond to each other. Reducing the external input slows the entire chain: less CO2 means less greenhouse warming, which means less ice melt, which preserves albedo. Targeting the input is more effective than treating downstream symptoms.",
            "feedback_incorrect": "The model shows CO2 Emissions Rate as the external input driving all internal components. While other components could theoretically be targeted, addressing the root input is most effective because it slows the entire cascade. However, note that reducing emissions does not immediately reverse existing warming due to system inertia."
        }
    ]
}

# =============================================================================
# G08L2-L05: Potential to Kinetic: The Energy Transformation Chain
# NGSS: MS-PS3-1, MS-PS3-5
# =============================================================================
L05_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "Your model shows that a 5 kg ball released from 10 meters has 490 J of potential energy at the top and 490 J of kinetic energy at the bottom on a frictionless ramp. On a ramp with friction, the ball reaches the bottom with only 380 J of kinetic energy. Where are the other 110 J?",
            "choices": {
                "A": "The 110 J were destroyed by friction and no longer exist",
                "B": "The 110 J were converted to thermal energy (heat) in the ramp surface and ball through friction",
                "C": "The 110 J remain as potential energy because the ball did not fall the full distance",
                "D": "The 110 J were absorbed by the air and converted to sound energy only"
            },
            "correct": "B",
            "feedback_correct": "Correct! Energy is never destroyed. Friction converts kinetic energy into thermal energy (heat) at the contact surfaces. The total energy is still 490 J: 380 J kinetic + 110 J thermal = 490 J. Conservation of energy is maintained.",
            "feedback_incorrect": "Conservation of energy means energy cannot be destroyed. The 'missing' 110 J became thermal energy through friction. If you could measure the temperature increase in the ramp surface, you would account for exactly 110 J of heat. Total energy always equals the starting potential energy."
        },
        {
            "question": "In your model, a 2 kg object and a 8 kg object are released from the same height. The model shows the 8 kg object has four times more kinetic energy at the bottom. A student concludes the heavier object must fall four times faster. Is this correct?",
            "choices": {
                "A": "Yes, because more kinetic energy always means more speed",
                "B": "No. The heavier object has more kinetic energy because KE depends on mass AND speed. Both objects fall at the same speed (without air resistance), but the heavier one has more energy due to its greater mass.",
                "C": "Yes, because gravity pulls heavier objects down faster",
                "D": "No, because the lighter object actually falls faster due to less air resistance"
            },
            "correct": "B",
            "feedback_correct": "Correct! KE = 1/2 mv squared. The heavier object has four times the mass but the same speed (gravity accelerates all objects equally). Four times the mass at the same speed gives four times the kinetic energy. Mass affects energy, not fall rate.",
            "feedback_incorrect": "Kinetic energy depends on both mass and speed (KE = 1/2 mv squared). In a vacuum, all objects fall at the same rate regardless of mass. The heavier object has more KE because it has more mass moving at the same speed. This is a common misconception from the equation."
        },
        {
            "question": "The model shows that at the midpoint of a frictionless ramp, an object has both potential and kinetic energy. Which statement is true about the total energy at this point?",
            "choices": {
                "A": "Total energy is less than at the top because some energy has been used up",
                "B": "Total energy equals the PE at the top, split between PE (remaining height) and KE (gained speed)",
                "C": "Total energy is greater than at the top because the object has both PE and KE",
                "D": "Total energy cannot be calculated at the midpoint because the object is in motion"
            },
            "correct": "B",
            "feedback_correct": "Correct! At the midpoint, the object has descended half the height (losing half its PE) and gained speed (gaining KE equal to the lost PE). Total energy is unchanged: PE at midpoint + KE at midpoint = original PE at the top. This holds at every point.",
            "feedback_incorrect": "Conservation of energy means total energy never changes in a closed system. At the midpoint, PE has decreased (less height) and KE has increased (more speed), but their sum equals the original PE at the top. Energy transforms, not increases or decreases."
        },
        {
            "question": "Based on your model, why can a roller coaster's second hill never be taller than its first hill?",
            "choices": {
                "A": "Because the train gains weight as it moves, making it harder to climb",
                "B": "Because friction and air resistance convert some kinetic energy to thermal energy along the way, leaving insufficient energy to reach the original height",
                "C": "Because gravity weakens as the coaster moves farther from the starting point",
                "D": "Because the coaster's engine turns off after the first hill"
            },
            "correct": "B",
            "feedback_correct": "Correct! The first hill sets the total energy budget. Friction and air resistance convert some KE to thermal energy during the ride. Each subsequent hill has less available energy than the previous one. There is never enough energy remaining to reach the original height.",
            "feedback_incorrect": "The total energy available is set by the first hill's height (PE = mgh). As the coaster travels, friction continuously converts some kinetic energy to heat. By the time it reaches the second hill, the total usable energy (PE + KE) is less than the original PE. The coaster cannot climb higher than the energy remaining allows."
        },
        {
            "question": "A student claims that a ball rolling on carpet 'loses energy' compared to rolling on a smooth floor. Using model evidence, how should this claim be corrected?",
            "choices": {
                "A": "The student is correct because carpet absorbs and destroys kinetic energy",
                "B": "The ball does not lose energy. Carpet has higher friction, which converts more kinetic energy to thermal energy. The total energy (KE + thermal) remains the same as on the smooth floor.",
                "C": "The student is wrong because carpet actually adds energy through static electricity",
                "D": "The ball loses energy on both surfaces equally because gravity is the same"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model proves that total energy (PE + KE + Thermal) is always conserved. Carpet has higher friction, converting more KE to thermal energy, so the ball slows down faster. But the energy is not lost; it becomes heat in the carpet fibers. Energy transforms, never disappears.",
            "feedback_incorrect": "Energy is never lost or destroyed. Higher friction on carpet converts more kinetic energy to thermal energy (heat), causing the ball to slow down more quickly. The 'missing' kinetic energy exists as warmth in the carpet. Total energy always remains constant."
        }
    ]
}

# =============================================================================
# G08L2-L06: Genetic Mutations: When DNA Makes a Typo
# NGSS: MS-LS3-1, MS-LS3-2
# =============================================================================
L06_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "Your model shows that when UV Radiation Exposure is set to 90%, Mutation Frequency increases dramatically and Organism Fitness declines. Which explanation is best supported by the model?",
            "choices": {
                "A": "UV radiation directly kills organisms by heating their bodies",
                "B": "UV radiation damages DNA bases, leading to more copying errors during cell division, which produces more mutations that alter protein function and reduce fitness",
                "C": "UV radiation makes organisms weaker by destroying their immune systems",
                "D": "UV radiation causes organisms to stop reproducing entirely"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model traces a causal chain: UV radiation damages DNA, which increases errors during replication, which increases mutation frequency, which alters protein function, which typically reduces organism fitness because harmful mutations outnumber beneficial ones.",
            "feedback_incorrect": "The model shows a specific mechanism: UV → DNA damage → copying errors during cell division → altered proteins → reduced fitness. UV does not directly kill organisms; it damages the molecular instructions for building proteins, and the consequences emerge through the mutation pathway."
        },
        {
            "question": "The model shows that both UV Radiation Exposure and Cell Division Rate independently increase Mutation Frequency. A student asks why skin cells are at higher cancer risk than brain cells. Which model-based explanation is correct?",
            "choices": {
                "A": "Skin cells are larger than brain cells, making them easier targets for UV",
                "B": "Skin cells are exposed to UV radiation AND divide rapidly, meaning both external inputs are high, compounding the mutation frequency",
                "C": "Brain cells are immune to mutations because they are protected by the skull",
                "D": "Skin cells have weaker DNA than brain cells"
            },
            "correct": "B",
            "feedback_correct": "Correct! Skin cells face a double risk: they are directly exposed to UV radiation (a mutagen) AND they divide frequently to replace damaged cells. Both model inputs are elevated, creating a compounded increase in mutation frequency compared to cells like neurons that rarely divide.",
            "feedback_incorrect": "The model shows two independent inputs that each increase mutation frequency. Skin cells have both elevated: high UV exposure (external environment) and high cell division rate (skin constantly regenerates). This combination makes skin cells particularly vulnerable to accumulating mutations."
        },
        {
            "question": "Your model shows that Protein Function Change has a POSITIVE/NEGATIVE (+/-) relationship with Organism Fitness. What does this dual relationship represent?",
            "choices": {
                "A": "Mutations always increase fitness in some organisms and decrease it in others",
                "B": "Most mutations change protein function in ways that are harmful to the organism, but rare mutations can be beneficial, so the effect can go either direction",
                "C": "Protein function changes are always neutral and do not affect fitness",
                "D": "The +/- sign means the relationship is unknown and cannot be predicted"
            },
            "correct": "B",
            "feedback_correct": "Correct! The dual sign reflects that mutations can have different outcomes. Most protein changes disrupt normal function (harmful). Some change non-critical regions (neutral). Rarely, a mutation improves a protein's function in the current environment (beneficial). The net effect depends on which proteins are affected.",
            "feedback_incorrect": "The +/- relationship captures the reality that not all mutations have the same effect. About 70% of point mutations are neutral, 29% are harmful, and less than 1% are beneficial. The direction of the effect depends on where in the protein the mutation occurs and what environmental conditions the organism faces."
        },
        {
            "question": "A student claims that UV radiation causes mutations instantly the moment it hits DNA. Using the model, which response is most accurate?",
            "choices": {
                "A": "The student is correct because UV immediately changes DNA into a mutated form",
                "B": "UV radiation damages DNA bases immediately, but the damage becomes a mutation only when the cell divides and copies the damaged DNA incorrectly",
                "C": "UV radiation has no effect on DNA and mutations are purely random",
                "D": "UV radiation only affects RNA, not DNA"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model shows that Cell Division Rate is a critical link between DNA damage and actual mutations. UV causes chemical damage (like thymine dimers) immediately, but this damage becomes a permanent mutation only during DNA replication. Without cell division, the damage may be repaired before it becomes heritable.",
            "feedback_incorrect": "The model distinguishes between DNA damage and mutation. UV causes immediate chemical damage to DNA bases, but a mutation only occurs when the damaged DNA is copied during cell division and the error is incorporated into the new strand. Cell division is the step where damage becomes mutation."
        },
        {
            "question": "Your model shows that mutations are the raw material for evolution, yet most mutations reduce organism fitness. How do these two facts coexist?",
            "choices": {
                "A": "They cannot coexist. If most mutations are harmful, evolution should not be possible.",
                "B": "Evolution works at the population level over many generations. Most mutations are harmful to individuals, but the rare beneficial mutation spreads through the population via natural selection, driving adaptation.",
                "C": "All mutations are beneficial for evolution because they create variety",
                "D": "Harmful mutations are actually beneficial in disguise because they force organisms to adapt"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model operates at the individual level, where most mutations reduce fitness. But evolution operates at the population level over many generations. Across millions of individuals, the rare beneficial mutation provides a survival advantage that natural selection amplifies, gradually changing the population.",
            "feedback_incorrect": "This is a key distinction between individual and population effects. Most mutations harm individual organisms, but across a population of millions over many generations, even a tiny fraction of beneficial mutations provides the variation that natural selection needs to drive evolutionary adaptation."
        }
    ]
}

# =============================================================================
# G08L2-L07: Wave Properties: Amplitude, Frequency, and Speed
# NGSS: MS-PS4-1, MS-PS4-2
# =============================================================================
L07_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "Your model shows that when a sound wave moves from air (343 m/s) to water (1,480 m/s), wave speed increases but frequency stays the same. Using the wave equation v = f x wavelength, what must happen to wavelength?",
            "choices": {
                "A": "Wavelength decreases because higher speed compresses the waves",
                "B": "Wavelength increases proportionally because speed increased while frequency remained constant",
                "C": "Wavelength stays the same because it is a fixed property of the wave",
                "D": "Wavelength becomes zero because the wave cannot exist in water"
            },
            "correct": "B",
            "feedback_correct": "Correct! From v = f x wavelength, if speed (v) increases and frequency (f) stays constant, wavelength must increase to maintain the equation. The wave stretches out in the denser medium while oscillating at the same rate.",
            "feedback_incorrect": "The wave equation v = f x wavelength must always balance. Frequency is set by the source and does not change when entering a new medium. If speed increases (water transmits sound faster), wavelength must also increase proportionally. Rearranging: wavelength = v / f."
        },
        {
            "question": "In the model, increasing Wave Source Energy from 20% to 90% increased Amplitude dramatically. A student asks: does doubling the amplitude double the energy? What does the model reveal?",
            "choices": {
                "A": "Yes, amplitude and energy have a direct 1:1 relationship",
                "B": "No, energy is proportional to the square of amplitude. Doubling amplitude quadruples the energy carried by the wave.",
                "C": "No, amplitude has no relationship to energy",
                "D": "Yes, but only for sound waves, not light waves"
            },
            "correct": "B",
            "feedback_correct": "Correct! Energy is proportional to amplitude squared. This is why a small increase in earthquake magnitude (related to wave amplitude) represents a huge increase in destructive energy. The relationship is exponential, not linear.",
            "feedback_incorrect": "The energy-amplitude relationship is quadratic, not linear. Doubling amplitude means four times the energy. This is why the difference between a gentle ocean wave and a tsunami is so devastating, even though amplitude is just one wave property."
        },
        {
            "question": "Your model shows a NEGATIVE relationship between Frequency and Wavelength. Which real-world example best illustrates this inverse relationship?",
            "choices": {
                "A": "Radio waves have low frequency and long wavelength, while gamma rays have high frequency and short wavelength",
                "B": "Loud sounds have long wavelengths and quiet sounds have short wavelengths",
                "C": "All waves have the same frequency and wavelength regardless of type",
                "D": "Higher frequency waves always travel slower than lower frequency waves"
            },
            "correct": "A",
            "feedback_correct": "Correct! The electromagnetic spectrum perfectly demonstrates the inverse relationship. Radio waves oscillate slowly (low frequency) with long wavelengths, while gamma rays oscillate rapidly (high frequency) with very short wavelengths. In any given medium, speed = frequency x wavelength.",
            "feedback_incorrect": "The inverse relationship between frequency and wavelength means that when one increases, the other decreases (for waves at the same speed). Radio waves have low frequency and long wavelength. Gamma rays have high frequency and short wavelength. Loudness relates to amplitude, not wavelength."
        },
        {
            "question": "A student observes that frequency stays the same when a wave enters a new medium, even though speed and wavelength change. Why does frequency remain constant?",
            "choices": {
                "A": "Because frequency is a universal constant that never changes for any wave",
                "B": "Because frequency is determined by the source, which continues vibrating at the same rate regardless of what medium the wave enters",
                "C": "Because the new medium forces the frequency to match the old medium",
                "D": "Because frequency and speed are the same property measured differently"
            },
            "correct": "B",
            "feedback_correct": "Correct! Frequency is set by the source. A tuning fork vibrating at 440 Hz pushes air molecules 440 times per second. When those vibrations reach water, the water molecules also vibrate 440 times per second because they are being driven by the same source. The medium changes speed and wavelength, not frequency.",
            "feedback_incorrect": "Frequency is a property of the source, not the medium. The source continues vibrating at the same rate no matter what medium the wave travels through. When a wave enters a new medium, the medium determines the speed, and wavelength adjusts to maintain v = f x wavelength."
        },
        {
            "question": "Based on your model, a marine scientist needs sonar to detect small objects on the ocean floor. High-frequency sonar provides fine detail but has short range, while low-frequency sonar travels far but provides less detail. Which model evidence supports choosing high-frequency sonar for this task?",
            "choices": {
                "A": "High-frequency waves are louder and can bounce off smaller objects",
                "B": "High-frequency waves have shorter wavelengths, which can resolve smaller features because the wavelength is closer to the size of the objects being detected",
                "C": "High-frequency waves travel faster in water, reaching the ocean floor sooner",
                "D": "High-frequency waves carry less energy, making them safer for marine life"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model shows the inverse relationship between frequency and wavelength. Higher frequency means shorter wavelength, and waves can only resolve objects roughly the size of their wavelength or larger. For detecting small objects, short wavelengths (high frequency) provide the necessary resolution.",
            "feedback_incorrect": "Wave resolution depends on wavelength relative to object size. The model shows that higher frequency produces shorter wavelengths. Waves interact most effectively with objects near their wavelength size. Short wavelengths (high frequency) can 'see' smaller features, which is why high-frequency sonar provides finer detail."
        }
    ]
}

# =============================================================================
# Master dictionary mapping lesson IDs to question sets
# =============================================================================
ALL_QUESTIONS = {
    "G08L2-L01": L01_QUESTIONS,
    "G08L2-L02": L02_QUESTIONS,
    "G08L2-L03": L03_QUESTIONS,
    "G08L2-L04": L04_QUESTIONS,
    "G08L2-L05": L05_QUESTIONS,
    "G08L2-L06": L06_QUESTIONS,
    "G08L2-L07": L07_QUESTIONS,
}
