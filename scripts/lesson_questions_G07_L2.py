#!/usr/bin/env python3
"""Multiple choice post-assessment questions for Grade 7 Level 2 ModelIt! Lessons"""

# ── G07L2-L01: The Invisible War: How Your Immune System Fights Back ──
L01_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "A vaccinated person and an unvaccinated person are both exposed to the same high dose of a virus. The vaccinated person recovers in two days with mild symptoms, while the unvaccinated person is sick for ten days. Based on the immune system model, which explanation best accounts for this difference?",
            "choices": {
                "A": "The vaccinated person has a stronger physical barrier that prevents pathogens from entering the body",
                "B": "The vaccinated person's memory cells enable rapid antibody production, neutralizing the pathogen before it can spread widely",
                "C": "The vaccine destroyed the virus before it could enter the vaccinated person's body",
                "D": "The unvaccinated person has fewer white blood cells than the vaccinated person"
            },
            "correct": "B",
            "feedback_correct": "Correct! Vaccination creates memory cells that recognize the pathogen immediately upon re-exposure. This allows antibody production to begin within hours instead of the 7-10 days it takes for a first encounter, reducing infection severity dramatically.",
            "feedback_incorrect": "Vaccines do not create physical barriers or destroy pathogens before they enter the body. The key difference is immune memory: vaccination trains memory cells so that antibody production begins almost immediately upon infection, rather than taking 7-10 days for a first-time response."
        },
        {
            "question": "In the immune system model, when Pathogen Load is set to high and Vaccine Status is off, Infection Severity rises rapidly before White Blood Cell Response can contain the invasion. Which relationship in the model best explains this outcome?",
            "choices": {
                "A": "Pathogen Load has a negative relationship with Infection Severity",
                "B": "White Blood Cell Response has a positive relationship with Infection Severity",
                "C": "Pathogen Load has a positive relationship with Infection Severity, and antibody production is delayed without prior vaccination",
                "D": "Vaccine Status has a negative relationship with White Blood Cell Response"
            },
            "correct": "C",
            "feedback_correct": "Correct! Pathogen Load positively drives Infection Severity, meaning more pathogens cause worse illness. Without vaccination, there are no memory cells, so the targeted antibody response takes 7-10 days to ramp up, allowing the infection to spread during that critical delay.",
            "feedback_incorrect": "Pathogen Load has a positive (not negative) relationship with Infection Severity: more pathogens mean worse infection. The critical factor is that without vaccination, the body lacks memory cells, so the specific antibody response is delayed by 7-10 days while the pathogen multiplies."
        },
        {
            "question": "A student claims that white blood cells and antibodies perform the same function in the immune system. Using the model, which response best corrects this misconception?",
            "choices": {
                "A": "White blood cells provide a fast, general response against any invader, while antibodies are custom-built proteins that specifically target one pathogen type",
                "B": "White blood cells only work during vaccinated responses, while antibodies work during unvaccinated responses",
                "C": "Antibodies arrive first and white blood cells arrive later to clean up remaining pathogens",
                "D": "White blood cells and antibodies are the same thing but are measured differently in the model"
            },
            "correct": "A",
            "feedback_correct": "Correct! The immune system operates as interacting subsystems. White blood cells provide the immediate, non-specific first response, attacking any invader within hours. Antibodies are produced by B-cells and are custom-designed to target specific pathogens, but take days to produce during a first infection.",
            "feedback_incorrect": "White blood cells and antibodies are distinct subsystems with different roles. White blood cells respond rapidly and non-specifically to any invader. Antibodies are specific, targeted proteins produced by B-cells that lock onto particular pathogens. Both work together as interacting subsystems."
        },
        {
            "question": "In the model, setting Pathogen Load to low with Vaccine Status off still results in low Infection Severity. Which explanation best accounts for why the body can handle a small invasion without prior vaccination?",
            "choices": {
                "A": "Low pathogen loads do not trigger any immune response",
                "B": "The non-specific white blood cell response is sufficient to contain a small number of pathogens before they can multiply significantly",
                "C": "The body only uses antibodies against small pathogen loads",
                "D": "Low pathogen loads cannot cause any disease regardless of immune system function"
            },
            "correct": "B",
            "feedback_correct": "Correct! When pathogen load is low, the fast-acting white blood cell response can engulf and destroy the invaders before they multiply to overwhelming numbers. The body does not need the slower antibody response because the initial defense handles the small threat.",
            "feedback_incorrect": "Even small pathogen loads trigger an immune response. The reason infection stays mild is that white blood cells provide a rapid, non-specific defense that can contain small numbers of pathogens before they multiply. The slower antibody response may not even be needed."
        },
        {
            "question": "A community has 90% vaccination rates for a particular virus. A student who cannot be vaccinated due to a medical condition is protected from the disease. Which concept from the model best explains this protection?",
            "choices": {
                "A": "The unvaccinated student develops antibodies by breathing the same air as vaccinated students",
                "B": "When most people in a community are immune, the pathogen cannot spread easily enough to reach vulnerable individuals, which is known as herd immunity",
                "C": "Vaccines release protective chemicals into the environment that shield nearby unvaccinated people",
                "D": "The unvaccinated student's white blood cells are strengthened by proximity to vaccinated individuals"
            },
            "correct": "B",
            "feedback_correct": "Correct! Herd immunity occurs when enough people in a population are immune that the pathogen cannot find enough susceptible hosts to sustain transmission. This protects individuals who cannot be vaccinated because the pathogen simply cannot reach them through the immune community.",
            "feedback_incorrect": "Immunity is not transmitted through the air or proximity. Herd immunity works because when most people are vaccinated, the pathogen cannot spread from person to person effectively. The chain of transmission is broken, protecting vulnerable individuals who cannot be vaccinated."
        }
    ]
}

# ── G07L2-L02: DNA Decoded: Why You Are (Mostly) Unique ──
L02_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "A farmer plants a field with genetically identical crop plants (produced by asexual reproduction). A new fungal disease arrives and destroys the entire crop. Based on the genetics model, which explanation best accounts for why the entire field was lost?",
            "choices": {
                "A": "Asexual reproduction produces weaker organisms that are always more susceptible to disease",
                "B": "All plants had identical DNA, so if one lacked resistance to the fungus, none of them had resistance",
                "C": "The fungal disease was too strong for any plant to survive regardless of genetic variation",
                "D": "Asexual reproduction causes more harmful mutations than sexual reproduction"
            },
            "correct": "B",
            "feedback_correct": "Correct! With zero genetic variation, all individuals share the same vulnerabilities. If one plant lacks resistance to the fungus, every plant in the genetically identical population lacks it. This is the fundamental danger of low genetic diversity.",
            "feedback_incorrect": "Asexual reproduction does not produce inherently weaker organisms. The problem is uniformity: all plants are genetically identical clones. If the original lacks resistance to the fungus, every copy also lacks it. A sexually reproducing population would have variation, and some individuals might carry resistance genes."
        },
        {
            "question": "Two siblings share the same parents but look noticeably different from each other. According to the model, which factor is most responsible for their physical differences?",
            "choices": {
                "A": "One sibling received more DNA from the mother and the other received more from the father",
                "B": "Sexual reproduction randomly combines different allele combinations from each parent during meiosis, creating unique offspring every time",
                "C": "Siblings always have completely different genes because each parent produces entirely new DNA for each child",
                "D": "Physical differences between siblings are caused entirely by environmental conditions, not genetics"
            },
            "correct": "B",
            "feedback_correct": "Correct! During meiosis, each parent contributes a random half of their chromosomes. Crossing over further shuffles genes. With millions of possible allele combinations, each sibling receives a unique genetic hand, which is why they look different despite sharing parents.",
            "feedback_incorrect": "Each parent contributes exactly half their DNA to every child, not more to one and less to another. The key is that WHICH half is contributed is random each time. Meiosis and crossing over create unique allele combinations, making each sibling genetically distinct."
        },
        {
            "question": "In the model, when Environmental Conditions change but Parent Gene Variation stays constant, some offspring gain a Survival Advantage while others lose it. Which crosscutting concept best explains this observation?",
            "choices": {
                "A": "Structure and Function: the structure of DNA determines the function of every organism",
                "B": "Cause and Effect: the environmental change causes certain trait combinations to become advantageous or disadvantageous",
                "C": "Scale and Proportion: larger organisms always have better survival advantages",
                "D": "Stability and Change: organisms always maintain stability regardless of environmental conditions"
            },
            "correct": "B",
            "feedback_correct": "Correct! The Cause and Effect relationship is central: a change in environmental conditions (cause) shifts which traits provide survival advantages (effect). A trait that was neutral or harmful in one environment may become beneficial in another.",
            "feedback_incorrect": "The correct crosscutting concept is Cause and Effect. Environmental change is the cause, and shifts in which traits provide survival advantages are the effect. Whether a trait helps or harms an organism depends entirely on the environmental context."
        },
        {
            "question": "A student argues that a mutation that causes sickle-shaped red blood cells is always harmful. Using the model's concept of environmental influence on survival advantage, which response best challenges this claim?",
            "choices": {
                "A": "All mutations are neutral and have no effect on survival",
                "B": "In regions with malaria, carrying one copy of the sickle cell allele provides resistance to the disease, making the same mutation beneficial in that environmental context",
                "C": "Sickle cell mutations are beneficial everywhere because they make blood cells stronger",
                "D": "Mutations cannot be both harmful and beneficial because DNA is either functional or broken"
            },
            "correct": "B",
            "feedback_correct": "Correct! Whether a trait is harmful or beneficial depends on the environment. The sickle cell allele in its full form causes disease, but carrying just one copy provides malaria resistance. In malaria-prone regions, this mutation increases survival advantage, demonstrating that context determines whether a trait helps or harms.",
            "feedback_incorrect": "The sickle cell example demonstrates that the same genetic variation can be harmful in one context and beneficial in another. In its full form, it causes sickle cell disease. But carrying one copy provides malaria resistance, which is advantageous in regions where malaria is common. Environment determines whether a trait is helpful or harmful."
        },
        {
            "question": "In the model, when Parent Gene Variation is set to low (simulating asexual-like reproduction), Trait Variation in Offspring is minimal and Survival Advantage drops sharply when Environmental Conditions change. A student concludes that asexual reproduction is always inferior to sexual reproduction. Why is this conclusion too broad?",
            "choices": {
                "A": "Asexual reproduction is actually always superior because it produces more offspring faster",
                "B": "Asexual reproduction is highly efficient in stable environments because identical offspring are already well-adapted, but it becomes dangerous when conditions change",
                "C": "The model is inaccurate because asexual organisms never face environmental changes",
                "D": "Asexual reproduction produces more genetic variation than sexual reproduction through faster mutation rates"
            },
            "correct": "B",
            "feedback_correct": "Correct! Asexual reproduction is efficient in stable environments because every offspring is already well-adapted (no wasted variation). But this advantage becomes a liability when the environment changes, because the population lacks the diversity needed to adapt. Neither strategy is universally superior.",
            "feedback_incorrect": "Asexual reproduction is not always inferior. In stable environments, producing identical, well-adapted offspring is highly efficient. The danger arises only when environmental conditions change, because the population lacks genetic diversity to respond. The correct answer recognizes that each reproductive strategy has context-dependent advantages."
        }
    ]
}

# ── G07L2-L03: Ocean Currents and Climate: The Conveyor Belt ──
L03_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "London, England, and Goose Bay, Canada, are at nearly the same latitude, yet London's average winter temperature is about 10 degrees Celsius warmer. Based on the ocean circulation model, which factor best explains this difference?",
            "choices": {
                "A": "London receives more direct sunlight than Goose Bay because of Earth's axial tilt",
                "B": "The Gulf Stream carries warm tropical water across the Atlantic to northwestern Europe, delivering heat that moderates London's climate",
                "C": "England is a smaller landmass, so it heats up faster than the Canadian mainland",
                "D": "London is at a lower elevation than Goose Bay, and lower elevations are always warmer"
            },
            "correct": "B",
            "feedback_correct": "Correct! The Gulf Stream transports enormous amounts of thermal energy from the tropical Atlantic to northwestern Europe. This warm current heats the air above it, giving coastal Europe much milder winters than locations at the same latitude without this ocean heat delivery.",
            "feedback_incorrect": "Both cities are at the same latitude, so they receive similar amounts of sunlight. The critical difference is ocean current heat transport. The Gulf Stream carries warm tropical water across the Atlantic, delivering heat that moderates Europe's climate far beyond what its latitude would predict."
        },
        {
            "question": "In the model, reducing the Temperature Difference between the equator and poles (simulating polar ice melt) causes Ocean Current Speed to decrease. Which cascade of effects does this trigger?",
            "choices": {
                "A": "Slower currents increase Heat Distribution, making all regions warmer",
                "B": "Slower currents reduce Heat Distribution, causing tropical regions to overheat while polar-adjacent regions lose warmth, destabilizing regional climates",
                "C": "Slower currents have no effect on Heat Distribution because wind patterns compensate completely",
                "D": "Slower currents cause the Temperature Difference to increase, creating a self-correcting cycle"
            },
            "correct": "B",
            "feedback_correct": "Correct! When ocean currents slow, they transport less heat from the equator toward the poles. Heat accumulates in tropical regions while areas that depended on ocean heat delivery (like Europe) lose their warming input. This uneven distribution destabilizes regional climates.",
            "feedback_incorrect": "Slower ocean currents transport LESS heat, not more. Without the conveyor belt moving warm water poleward, heat accumulates near the equator while regions like Europe lose the Gulf Stream warmth they depend on. This creates climate instability in multiple regions."
        },
        {
            "question": "A student claims that global warming should make ALL regions warmer, so Europe cannot get colder. Using the ocean circulation model, which argument best refutes this claim?",
            "choices": {
                "A": "Global warming only affects tropical regions, not temperate ones",
                "B": "Global warming melts polar ice, reducing salinity and the temperature gradient that drives ocean currents. Weakened currents reduce heat delivery to Europe, potentially making it colder even as global averages rise",
                "C": "Europe is protected from global warming by the Atlantic Ocean",
                "D": "Climate models cannot predict regional effects because weather is too chaotic"
            },
            "correct": "B",
            "feedback_correct": "Correct! This counterintuitive outcome makes sense through the model. Global warming melts ice, adding fresh water that reduces ocean salinity and weakens the thermohaline circulation. Without the Gulf Stream delivering tropical heat, Europe could experience dramatically colder winters even as the global average temperature rises.",
            "feedback_incorrect": "The key insight is that global averages and regional effects are different. Global warming disrupts the ocean conveyor belt by melting ice and reducing the salinity gradient. This weakens currents that deliver heat to Europe. So while the planet warms overall, specific regions that depend on ocean heat transport could actually cool."
        },
        {
            "question": "The model shows that Heat Distribution has a negative relationship with Temperature Difference. This means that as ocean currents distribute heat more evenly, the temperature gradient that drives them weakens. What type of mechanism does this represent?",
            "choices": {
                "A": "A positive feedback loop that amplifies ocean current speed indefinitely",
                "B": "A self-regulating negative feedback loop where the system moderates its own driving force",
                "C": "A one-directional cause-and-effect chain with no feedback",
                "D": "An error in the model because outputs cannot affect inputs"
            },
            "correct": "B",
            "feedback_correct": "Correct! This is a self-regulating negative feedback loop. Ocean currents distribute heat from equator to poles, reducing the very temperature gradient that drives them. As the gradient weakens, currents slow, heat distribution becomes less even, and the gradient rebuilds. This keeps the system in dynamic balance.",
            "feedback_incorrect": "Outputs can indeed affect inputs in real systems through feedback loops. When ocean currents distribute heat and reduce the temperature gradient that drives them, this is a self-regulating negative feedback loop. The system moderates itself: strong currents reduce their own driving force, which slows them, which allows the gradient to rebuild."
        },
        {
            "question": "In the model, both Temperature Difference and Wind Patterns have positive relationships with Ocean Current Speed. A student wants to determine which factor has a greater influence on current speed. Which investigation approach would best answer this question?",
            "choices": {
                "A": "Set both inputs to maximum and observe the result",
                "B": "Change one variable at a time while holding the other constant, then compare the resulting changes in Ocean Current Speed",
                "C": "Remove both inputs and observe whether currents still flow",
                "D": "Only test extreme values because moderate values do not reveal meaningful patterns"
            },
            "correct": "B",
            "feedback_correct": "Correct! Controlled variable testing is the proper scientific approach. By changing one input while holding the other constant, the student can isolate each factor's individual effect on current speed and determine which has a greater influence.",
            "feedback_incorrect": "The scientific method requires controlling variables to isolate effects. Setting both to maximum tests their combined effect, not their individual contributions. The correct approach is to change one variable at a time while holding the other constant, then compare the magnitude of change in Ocean Current Speed."
        }
    ]
}

# ── G07L2-L04: Newton's Laws: Why Things Move the Way They Do ──
L04_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "Two identical forces are applied to two different objects. Object A has a mass of 2 kg and Object B has a mass of 8 kg. Using the model's demonstration of F = ma, which statement correctly compares their accelerations?",
            "choices": {
                "A": "Both objects accelerate at the same rate because the same force was applied",
                "B": "Object A accelerates four times faster than Object B because acceleration is inversely proportional to mass",
                "C": "Object B accelerates faster because heavier objects have more momentum",
                "D": "Neither object accelerates because friction cancels out the applied force"
            },
            "correct": "B",
            "feedback_correct": "Correct! Newton's Second Law states a = F/m. With the same force, Object A (2 kg) accelerates at F/2, while Object B (8 kg) accelerates at F/8. Since F/2 is four times F/8, Object A accelerates four times faster. Acceleration is inversely proportional to mass.",
            "feedback_incorrect": "When the same force is applied to different masses, the lighter object accelerates more. Newton's Second Law (a = F/m) shows that doubling the mass halves the acceleration. Object A (2 kg) accelerates four times faster than Object B (8 kg) because 8/2 = 4."
        },
        {
            "question": "In the model, increasing Friction Force causes Net Force to decrease even when Applied Force stays constant. A student observes that a hockey puck slides much farther on ice than a ball rolls on grass with the same initial push. Which model relationship explains this?",
            "choices": {
                "A": "Applied Force to Net Force is negative on grass but positive on ice",
                "B": "Friction Force has a negative relationship with Net Force, and ice produces much less friction than grass, so more net force remains to sustain motion",
                "C": "Object Mass is lower on ice because the surface is smoother",
                "D": "Acceleration is not affected by surface type according to the model"
            },
            "correct": "B",
            "feedback_correct": "Correct! Friction opposes motion and subtracts from applied force. On ice, friction is minimal, so nearly all of the applied force remains as net force. On grass, high friction subtracts most of the applied force, leaving little net force to sustain motion. This is why the puck slides farther.",
            "feedback_incorrect": "The key relationship is that Friction Force has a negative effect on Net Force. Ice has very low friction, so the puck retains most of its kinetic energy. Grass has high friction, rapidly converting kinetic energy to heat and slowing the ball. The surface does not change the object's mass or the nature of the force relationship."
        },
        {
            "question": "A loaded truck traveling at 60 mph takes much longer to stop than an empty car traveling at the same speed, even when both apply maximum brakes. Which combination of Newton's Laws best explains this observation?",
            "choices": {
                "A": "Newton's First Law only: the truck has more weight pressing on the road",
                "B": "Newton's First Law (greater mass means greater inertia resisting the change in motion) combined with Newton's Second Law (same braking force applied to greater mass produces less deceleration)",
                "C": "Newton's Third Law only: the road pushes back harder on the truck",
                "D": "None of Newton's Laws apply because braking is a separate phenomenon from motion"
            },
            "correct": "B",
            "feedback_correct": "Correct! The truck has greater mass, which means greater inertia (First Law: it resists changing its motion more). When brakes apply force, the truck's larger mass means less deceleration for the same force (Second Law: a = F/m). Both laws work together to explain the longer stopping distance.",
            "feedback_incorrect": "This situation requires both the First and Second Laws working together. The truck's greater mass gives it more inertia (First Law), meaning it resists stopping more than the lighter car. Additionally, the same braking force divided by the truck's larger mass produces less deceleration (Second Law: a = F/m)."
        },
        {
            "question": "In the model, a student sets Applied Force to 10 N and Object Mass to 5 kg, but observes that the actual Acceleration is less than the expected 2 m/s squared. Which model component accounts for the difference between expected and observed acceleration?",
            "choices": {
                "A": "Net Force, because gravity reduces the applied force on horizontal surfaces",
                "B": "Friction Force, which opposes motion and reduces the net force available for acceleration below the full applied force",
                "C": "Object Mass, which must have increased automatically during the simulation",
                "D": "Acceleration, which has a maximum limit regardless of force and mass values"
            },
            "correct": "B",
            "feedback_correct": "Correct! The calculation F/m = 10/5 = 2 m/s squared assumes no friction. In reality, friction subtracts from the applied force before it can accelerate the object. If friction is 3 N, the net force is only 7 N, producing acceleration of 7/5 = 1.4 m/s squared. The model captures this real-world complication.",
            "feedback_incorrect": "The expected value of 2 m/s squared assumes all 10 N of applied force reaches the object as net force. But friction opposes motion and subtracts from the applied force. The net force (Applied Force minus Friction Force) is what actually determines acceleration via F = ma."
        },
        {
            "question": "A student pushes a friend on a skateboard. Newton's Third Law states that the friend pushes back on the student with equal force. The student asks: 'If the forces are equal, why does anyone move?' Which response correctly resolves this apparent paradox?",
            "choices": {
                "A": "The forces are not actually equal; the pusher always exerts more force",
                "B": "The action and reaction forces act on different objects, so they cannot cancel each other out. Each object accelerates based on the net forces acting on IT",
                "C": "Friction makes the reaction force weaker than the action force",
                "D": "Newton's Third Law only applies to stationary objects, not moving ones"
            },
            "correct": "B",
            "feedback_correct": "Correct! This is a common misconception about Newton's Third Law. The action-reaction forces act on DIFFERENT objects. The push on the friend accelerates the friend (based on the friend's mass). The reaction push on the student accelerates the student backward (based on the student's mass). Forces only cancel when they act on the same object.",
            "feedback_incorrect": "Newton's Third Law forces are always exactly equal and opposite, but they act on DIFFERENT objects. The student pushes the friend (force on friend), and the friend pushes back on the student (force on student). Since these forces act on different objects, they cannot cancel. Each object responds to the forces acting on it individually."
        }
    ]
}

# ── G07L2-L05: Evolution in Action: How Species Change Over Time ──
L05_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "In the evolution model, a small population with low genetic variation faces rapid environmental change. The model predicts extinction. Which chain of relationships in the model explains this outcome?",
            "choices": {
                "A": "Small Population Size leads to high Genetic Variation, which leads to fast Adaptation Rate, but the environment changes too quickly",
                "B": "Small Population Size leads to low Genetic Variation, which limits Adaptation Rate because natural selection has few trait options to act on, and the population cannot keep pace with environmental change",
                "C": "Environmental Change Rate directly reduces Population Size without involving Genetic Variation or Selection Pressure",
                "D": "Small populations evolve faster because there are fewer individuals to change"
            },
            "correct": "B",
            "feedback_correct": "Correct! The model shows a clear cascade: small populations have low genetic variation, which means fewer trait options for natural selection to work with. When the environment changes rapidly, the adaptation rate cannot keep pace because there simply are not enough different traits in the population to select from.",
            "feedback_incorrect": "Small populations have LESS genetic variation, not more. This is the root of the problem. With fewer trait options, natural selection has limited raw material. When environmental change outpaces the population's ability to adapt, extinction becomes likely. Large populations survive better because they have more variation."
        },
        {
            "question": "A student claims that organisms evolve on purpose to survive environmental changes. Using the model, which response best corrects this misconception?",
            "choices": {
                "A": "Organisms do evolve on purpose, but only over many generations",
                "B": "Evolution acts on random genetic variation that already exists in the population. Natural selection favors traits that happen to match the new conditions, not traits organisms chose to develop",
                "C": "Individual organisms change their DNA during their lifetime to adapt to new conditions",
                "D": "Evolution only occurs through mutations caused by environmental stress"
            },
            "correct": "B",
            "feedback_correct": "Correct! Evolution has no direction or intention. Genetic variation arises randomly through mutations and sexual reproduction BEFORE environmental changes occur. Natural selection then acts on this pre-existing variation, favoring individuals whose traits happen to match the new conditions. No organism decides to evolve.",
            "feedback_incorrect": "Evolution is not intentional. Organisms cannot choose to develop new traits. Genetic variation arises randomly before environmental changes. Natural selection then acts as a filter: individuals with traits that happen to suit the new environment survive and reproduce at higher rates. This shifts population traits over generations without any planning."
        },
        {
            "question": "The model shows that when Environmental Change Rate is set to gradual (low), even populations with moderate Genetic Variation can adapt successfully. Which principle explains why slow change is easier for populations to survive?",
            "choices": {
                "A": "Slow environmental change produces weaker Selection Pressure, giving natural selection more time to shift trait frequencies across generations before conditions become critical",
                "B": "Slow environmental change does not create any Selection Pressure at all",
                "C": "Populations can sense gradual changes and prepare their DNA accordingly",
                "D": "Gradual change only affects individual organisms, not entire populations"
            },
            "correct": "A",
            "feedback_correct": "Correct! Gradual environmental change creates milder selection pressure per generation. This gives natural selection time to incrementally shift trait frequencies across many generations. Each generation, slightly better-adapted individuals reproduce more, and the population gradually tracks the changing conditions.",
            "feedback_incorrect": "Gradual change does still create selection pressure, but at a rate that allows natural selection to keep pace. Each generation, individuals with slightly better-adapted traits reproduce more, and the population incrementally shifts. When change is too fast, there is not enough generational time for selection to accumulate enough adaptive change."
        },
        {
            "question": "Two populations of the same species live in separate environments. Population A is large with high genetic variation. Population B is small with low genetic variation. Both face the same disease outbreak. Based on the model, which prediction is most supported?",
            "choices": {
                "A": "Both populations will be equally affected because the disease does not distinguish between population sizes",
                "B": "Population A is more likely to survive because its higher genetic variation means some individuals are more likely to carry disease resistance traits",
                "C": "Population B will survive because smaller populations are easier to manage during disease outbreaks",
                "D": "Neither population will be affected because natural selection prevents disease from spreading"
            },
            "correct": "B",
            "feedback_correct": "Correct! Population A's larger size provides more genetic variation, increasing the probability that some individuals carry resistance traits. Natural selection will favor these resistant individuals, and the population can recover. Population B's low variation means all individuals may share the same vulnerability.",
            "feedback_incorrect": "Genetic variation is the key difference. Population A's large size means more diverse alleles, including potential disease resistance genes. Some individuals are likely to survive, reproduce, and pass on resistance. Population B's uniformity means if one individual is susceptible, they all likely are."
        },
        {
            "question": "The fossil record shows that over 99% of all species that ever lived are now extinct. Based on the evolution model, which factor most strongly determines whether a species survives or goes extinct during a mass extinction event?",
            "choices": {
                "A": "How large and physically strong the species is",
                "B": "Whether the species has enough genetic variation to include individuals with traits suited to the dramatically changed post-extinction environment",
                "C": "How old the species is, because older species have more experience surviving",
                "D": "Whether the species actively chooses to migrate to safer habitats"
            },
            "correct": "B",
            "feedback_correct": "Correct! During mass extinction events, environmental conditions change dramatically and rapidly. Species with high genetic variation have a better chance that some individuals possess traits suited to the new conditions. Size and age do not guarantee survival. The dinosaurs were large and ancient, yet most went extinct while small, genetically diverse mammals survived.",
            "feedback_incorrect": "Physical size and species age do not determine extinction survival. The critical factor is genetic variation. Species with diverse traits have a higher probability that some individuals can survive dramatically changed conditions. This is why small, diverse groups like mammals survived the mass extinction that killed the large dinosaurs."
        }
    ]
}

# ── G07L2-L06: Electromagnetic Spectrum: Beyond Visible Light ──
L06_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "In the electromagnetic spectrum model, increasing Wave Frequency causes Wave Energy to increase. A hospital uses X-rays (high frequency) to image bones inside the body. Based on the model, why do X-rays pass through soft tissue but are stopped by bone?",
            "choices": {
                "A": "X-rays are attracted to calcium in bones and repelled by soft tissue",
                "B": "X-ray photons carry enough energy to penetrate low-density soft tissue but are absorbed by the high-density mineral structure of bone",
                "C": "Bones reflect X-rays while soft tissue absorbs them completely",
                "D": "X-rays only travel in straight lines and bones are in the way"
            },
            "correct": "B",
            "feedback_correct": "Correct! X-rays have high frequency and therefore high energy. This energy is sufficient to pass through low-density materials like skin and muscle but is absorbed by high-density materials like bone and metal. The differential absorption creates the contrast in X-ray images.",
            "feedback_incorrect": "X-rays are not attracted to or repelled by specific tissues. The interaction depends on material density. X-ray photons have enough energy to pass through low-density soft tissue (transmission) but are absorbed by the dense mineral structure of bone. This differential penetration is what creates medical X-ray images."
        },
        {
            "question": "A student wonders why WiFi signals (radio waves) pass through walls but visible light does not. Using the model's relationships between frequency, energy, and material interaction, which explanation is most accurate?",
            "choices": {
                "A": "Radio waves are smaller than visible light waves and can fit between wall molecules",
                "B": "Radio waves have lower frequency and interact weakly with wall materials, passing through without significant absorption, while visible light's frequency matches the absorption properties of wall materials",
                "C": "Walls have special radio-transparent coatings built into them",
                "D": "Radio waves are stronger than visible light, so they can push through walls"
            },
            "correct": "B",
            "feedback_correct": "Correct! Whether a wave is transmitted, absorbed, or reflected depends on the relationship between the wave's frequency and the material's properties. Radio waves have low frequency and do not interact strongly with common wall materials. Visible light has a higher frequency that matches the absorption characteristics of opaque materials like drywall and wood.",
            "feedback_incorrect": "Radio waves actually have LONGER wavelengths than visible light, not smaller. The key is how different frequencies interact with different materials. Radio waves pass through walls because their frequency does not strongly interact with wall materials. Visible light is absorbed or reflected by the same materials because its frequency matches their absorption properties."
        },
        {
            "question": "The model shows that Wave Frequency and Wave Energy have a positive relationship. A student concludes that higher frequency waves are always more dangerous. Which evidence from the model challenges this oversimplification?",
            "choices": {
                "A": "All electromagnetic waves are equally dangerous regardless of frequency",
                "B": "Danger depends on both energy per photon (frequency) AND intensity (amplitude). A weak X-ray beam can be less harmful than an extremely intense radio beam because total energy delivered matters, not just frequency",
                "C": "Lower frequency waves are actually more dangerous because they penetrate deeper",
                "D": "The model does not include any information about wave danger"
            },
            "correct": "B",
            "feedback_correct": "Correct! While higher frequency means more energy per photon, the total energy delivered depends on amplitude (intensity) too. The model shows Wave Amplitude also has a positive relationship with Wave Energy. A brief, low-intensity X-ray for medical imaging is safe, while prolonged exposure to an extremely intense microwave source could be harmful.",
            "feedback_incorrect": "The student's reasoning is partially correct but incomplete. Higher frequency does mean more energy per photon, but danger depends on TOTAL energy delivered, which involves both frequency (energy per photon) and amplitude (number of photons). The model shows both Wave Frequency and Wave Amplitude contribute positively to Wave Energy."
        },
        {
            "question": "Visible light represents less than 1% of the electromagnetic spectrum, yet human eyes evolved to detect this specific frequency range. Based on the model's concepts, which explanation best accounts for why this particular range?",
            "choices": {
                "A": "Visible light is the only type of electromagnetic wave that exists on Earth's surface",
                "B": "The visible range matches the peak output of our Sun and passes efficiently through Earth's atmosphere, making it the most useful range for organisms to detect",
                "C": "All organisms on Earth detect the same frequency range because DNA encodes for visible light detection",
                "D": "Visible light is the safest frequency range, so evolution selected for eyes that avoid detecting dangerous wavelengths"
            },
            "correct": "B",
            "feedback_correct": "Correct! Our Sun emits most of its energy in the visible range, and Earth's atmosphere is largely transparent to these frequencies. Evolving eyes that detect the most abundant, available electromagnetic radiation provides the greatest survival advantage. Other organisms detect different ranges based on their specific environments.",
            "feedback_incorrect": "Many types of electromagnetic waves reach Earth's surface, not just visible light. The reason our eyes detect the visible range is that it matches the Sun's peak output AND passes through the atmosphere efficiently. This makes it the most abundant and useful range for surface-dwelling organisms to detect. Different organisms have evolved to detect different ranges."
        },
        {
            "question": "A telecommunications engineer must choose between analog and digital signals for a long-distance communication system. Based on the model's concepts about signal transmission, which advantage makes digital signals more reliable?",
            "choices": {
                "A": "Digital signals travel faster than analog signals through the same medium",
                "B": "Digital signals use higher frequencies than analog signals",
                "C": "Digital signals encode information as discrete 1s and 0s that can be perfectly regenerated at relay points, while analog signals accumulate noise with distance and cannot be restored to their original form",
                "D": "Digital signals are immune to all forms of electromagnetic interference"
            },
            "correct": "C",
            "feedback_correct": "Correct! Digital signals encode information as discrete pulses (1s and 0s). Any distortion can be filtered because each pulse is either on or off. At relay points, the signal can be perfectly regenerated. Analog signals are continuous waves that degrade with noise, and this degradation cannot be separated from the original signal.",
            "feedback_incorrect": "Digital and analog signals travel at the same speed through the same medium. The advantage of digital is not speed but reliability. Digital signals use discrete values (1 or 0) that can be perfectly restored even after partial degradation. Analog signals are continuous, so noise permanently distorts the information and compounds with distance."
        }
    ]
}

# ── G07L2-L07: Rock Cycle Deep Dive: From Magma to Mountain ──
L07_QUESTIONS = {
    "mc_post_assessment": [
        {
            "question": "A geologist finds a rock that was originally sandstone (sedimentary) but now has a crystalline, folded structure. Based on the rock cycle model, which process and resulting rock type best explains this transformation?",
            "choices": {
                "A": "Weathering transformed the sandstone into igneous rock at the surface",
                "B": "The sandstone was buried deep enough to be subjected to intense heat and pressure, transforming it into metamorphic rock without melting",
                "C": "The sandstone melted completely and resolidified as a new sedimentary rock",
                "D": "Chemical reactions with rainwater dissolved and reformed the sandstone into metamorphic rock at the surface"
            },
            "correct": "B",
            "feedback_correct": "Correct! When sedimentary rock is buried deeply enough, increasing heat and pressure transform its mineral structure without melting it. This metamorphic transformation changes sandstone into quartzite, which displays the crystalline, folded structure the geologist observed.",
            "feedback_incorrect": "Weathering breaks rocks down at the surface rather than transforming them into new rock types with crystalline structure. The rock described underwent metamorphic transformation: intense heat and pressure deep underground changed its mineral structure without melting it. If it had melted completely, it would have become igneous rock, not metamorphic."
        },
        {
            "question": "In the rock cycle model, Sedimentary Layers have a positive relationship with Metamorphic Transformation. Which mechanism explains why the accumulation of sedimentary layers can lead to metamorphism?",
            "choices": {
                "A": "Sedimentary rocks contain chemicals that trigger metamorphic reactions on their own",
                "B": "As sedimentary layers accumulate, the weight of upper layers creates increasing pressure on deeper layers. Combined with geothermal heat at depth, this triggers metamorphic transformation",
                "C": "Sedimentary rocks automatically become metamorphic after a certain age regardless of depth",
                "D": "Metamorphic transformation occurs at the surface where sedimentary layers are deposited"
            },
            "correct": "B",
            "feedback_correct": "Correct! As sedimentary layers stack up over millions of years, the weight of the overlying material creates enormous pressure on the deepest layers. Combined with increasing geothermal heat at greater depths, this pressure is sufficient to transform the mineral structure of the rock without melting it.",
            "feedback_incorrect": "Metamorphic transformation requires heat and pressure, which increase with depth. When sedimentary layers accumulate, the weight of upper layers compresses deeper layers. This pressure, combined with geothermal heat at depth, provides the conditions needed for metamorphism. Time or surface chemistry alone are not sufficient."
        },
        {
            "question": "The model shows that the rock cycle has no beginning or end, meaning any rock type can become any other rock type. A student argues that sedimentary rock must always become metamorphic before becoming igneous. Using the model, which scenario disproves this claim?",
            "choices": {
                "A": "Sedimentary rock can be subducted directly into the mantle where extreme heat melts it into magma, which cools into igneous rock, bypassing the metamorphic stage entirely",
                "B": "Sedimentary rock always follows the sequence: sedimentary to metamorphic to igneous to sedimentary",
                "C": "The rock cycle only operates in one direction, so the student's claim is correct",
                "D": "Sedimentary rock cannot become igneous rock under any circumstances"
            },
            "correct": "A",
            "feedback_correct": "Correct! The rock cycle has multiple pathways, not a single sequence. Sedimentary rock can be pulled into the mantle at subduction zones where temperatures are high enough to melt it directly into magma. When that magma cools, it forms igneous rock without ever passing through a metamorphic stage.",
            "feedback_incorrect": "The rock cycle is NOT a one-directional chain. Any rock type can become any other type through multiple pathways. Sedimentary rock can skip the metamorphic stage entirely if it encounters temperatures high enough to melt it directly into magma, which then cools into igneous rock."
        },
        {
            "question": "In the model, when Heat & Pressure is set to low and Weathering Rate is set to high, Sedimentary Layers dominate while Igneous Rock Formation and Metamorphic Transformation are minimal. If Earth's internal heat source completely shut off, what would the model predict for the long-term rock cycle?",
            "choices": {
                "A": "All three rock types would continue forming at equal rates because the Sun provides enough energy for all processes",
                "B": "Only weathering and sedimentary formation would continue because the Sun drives surface erosion, while metamorphic and igneous processes would stop without internal heat",
                "C": "The rock cycle would immediately stop completely because both energy sources are needed for any process",
                "D": "Igneous rock formation would increase because surface temperatures from the Sun would melt rocks"
            },
            "correct": "B",
            "feedback_correct": "Correct! The rock cycle is powered by TWO energy sources: internal heat (driving metamorphism, melting, and plate tectonics) and solar energy (driving weathering and erosion). Without internal heat, only surface processes would continue. Over time, all exposed rocks would weather into sediment. Mars is an example of a planet where this has happened.",
            "feedback_incorrect": "The rock cycle requires two energy sources. Earth's internal heat drives melting (igneous formation), metamorphism, and plate tectonics. Solar energy drives weathering and erosion at the surface. Without internal heat, only weathering and sedimentary processes continue. Surface temperatures from the Sun are far too low to melt rock."
        },
        {
            "question": "Geologists use the Law of Superposition to determine relative rock ages: in undisturbed strata, older layers are on the bottom and younger layers are on top. A scientist discovers a fossil of a marine organism embedded in rock near a mountain summit. Using the rock cycle model, which sequence of events best explains this finding?",
            "choices": {
                "A": "The marine organism climbed to the mountain top before becoming fossilized",
                "B": "Marine sediment containing the organism was deposited on the ocean floor, lithified into sedimentary rock, then tectonic forces uplifted the rock from the seafloor to mountain height over millions of years",
                "C": "Volcanic eruptions carried marine fossils from the ocean floor and deposited them on mountaintops",
                "D": "Rain washed marine organisms uphill during a massive flood"
            },
            "correct": "B",
            "feedback_correct": "Correct! The rock cycle and plate tectonics work together. Marine organisms die and settle on the ocean floor where they are buried in sediment and fossilized in sedimentary rock. Over millions of years, tectonic forces can push these seafloor rocks upward, even creating mountain ranges. This is why marine fossils are found at high elevations worldwide.",
            "feedback_incorrect": "Marine fossils on mountaintops are explained by the rock cycle combined with plate tectonics. Organisms were fossilized in seafloor sedimentary rock. Over millions of years, tectonic plate collisions pushed these ocean floor rocks upward to form mountains. This process, not floods or volcanic transport, explains marine fossils at high elevations."
        }
    ]
}

# ── Master Dictionary ────────────────────────────────────────────
ALL_QUESTIONS = {
    "G07L2-L01": L01_QUESTIONS,
    "G07L2-L02": L02_QUESTIONS,
    "G07L2-L03": L03_QUESTIONS,
    "G07L2-L04": L04_QUESTIONS,
    "G07L2-L05": L05_QUESTIONS,
    "G07L2-L06": L06_QUESTIONS,
    "G07L2-L07": L07_QUESTIONS,
}
