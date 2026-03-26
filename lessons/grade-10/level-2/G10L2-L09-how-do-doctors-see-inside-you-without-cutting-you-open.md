# Lesson: How Do Doctors See Inside You Without Cutting You Open?

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G10L2-L09 |
| **Grade** | 10th Grade — Level 2: Systems Under Pressure |
| **Lesson Name** | How Do Doctors See Inside You Without Cutting You Open? |
| **Status** | Template |

---

## Platform

### Title
**How Do Doctors See Inside You Without Cutting You Open? — Modeling MRI Physics and Medical Imaging Technology**

### Overview
Magnetic Resonance Imaging is one of the most remarkable achievements of applied physics — it turns the quantum mechanical properties of hydrogen atoms into detailed images of the human body's interior. Without a single X-ray photon or surgical incision, MRI can distinguish between healthy and diseased tissue, map brain activity, visualize blood flow, and detect tumors as small as a few millimeters. Students investigate the driving question: How can a machine create detailed images of your brain, muscles, and organs using nothing but a magnetic field and radio waves — without a single X-ray or incision? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of a modern MRI machine in a clinical setting with a patient entering the scanner bore, the machine's sleek white design illuminated by ambient blue clinical lighting, showing the impressive scale of the technology]

### Grade
10th Grade — Level 2: Systems Under Pressure

### NGSS Standard
**HS-PS2-4, HS-PS4-4**: Use mathematical representations of Newton's law of gravitation and Coulomb's law to describe and predict the gravitational and electrostatic forces between objects. Evaluate the validity and reliability of claims in published materials of the effects that different frequencies of electromagnetic radiation have when absorbed by matter.

### Learning Objectives
- Model how magnetic field strength, radio frequency pulses, and tissue properties interact to produce diagnostic-quality medical images
- Analyze why MRI provides superior tissue contrast compared to X-rays and CT scans for certain medical conditions
- Predict how changes in magnetic field strength and coil temperature affect image resolution and diagnostic accuracy
- Evaluate the trade-offs between image quality, patient safety, scan time, and energy consumption in MRI system design

### Component List (Starting Model: 7 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Magnetic Field Strength | External | The intensity of the static magnetic field in Tesla, which aligns hydrogen nuclei in the patient's body and determines the signal-to-noise ratio of the resulting images |
| Coil Temperature | External | The temperature of the superconducting magnet coils, which must remain below the critical temperature (-269 degrees Celsius for NbTi) to maintain zero electrical resistance and stable magnetic field |
| Image Resolution | Internal | The spatial detail visible in the MRI image, measured in millimeters — determined by magnetic field strength, gradient coil precision, and signal-to-noise ratio |
| Tissue Contrast | Internal | The ability to visually distinguish different tissue types in the image based on their different relaxation times — the primary advantage of MRI over other imaging modalities |
| Patient Safety | Internal | The level of risk to the patient during scanning, affected by magnetic field interactions with implants, specific absorption rate (SAR) of radiofrequency energy, and acoustic noise from gradient switching |
| Energy Consumption | Internal | The total electrical power required to operate the MRI system, including maintaining cryogenic cooling for superconducting coils, powering gradient amplifiers, and running computing systems |
| Diagnostic Accuracy | Internal | The probability that the MRI image provides sufficient information for a correct medical diagnosis, determined by the combination of Image Resolution, Tissue Contrast, and the radiologist's expertise |

### Research for Lesson
- The Physics of Nuclear Magnetic Resonance — reference materials and textbook resources
- How Contrast Works — reference materials and textbook resources
- The Superconducting Magnet — reference materials and textbook resources
- Safety and Limitations — reference materials and textbook resources

---

## Step 1: LOCATE — Build Your System

### Text Editor

```
HOW DO DOCTORS SEE INSIDE YOU WITHOUT CUTTING YOU OPEN?

Modeling MRI Physics and Medical Imaging Technology.
How can a machine create detailed images of your brain, muscles, and organs using nothing but a magnetic field and radio waves — without a single X-ray or incision?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Magnetic Field Strength" — the intensity of the static magnetic field in tesla
  ○ Click "Coil Temperature" — the temperature of the superconducting magnet coils
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Image Resolution" — the spatial detail visible in the mri image
  ○ Click "Tissue Contrast" — the ability to visually distinguish different tissue types in the image based on their different relaxation times — the primary advantage of mri over other imaging modalities
  ○ Click "Patient Safety" — the level of risk to the patient during scanning
  ○ Click "Energy Consumption" — the total electrical power required to operate the mri system
  ○ Click "Diagnostic Accuracy" — the probability that the mri image provides sufficient information for a correct medical diagnosis

Task B: ADD TO YOUR MODEL
• Click the PLUS (+) button to add each component to your picture
• You should now see 7 components on your canvas

Task C: SORT YOUR COMPONENTS
• Sort your components into EXTERNAL and INTERNAL
• EXTERNAL = things we can't control (inputs from outside the system)
• INTERNAL = things that change because of other things in the system
• Your teacher will show you how this works in the video

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You now have the basic pieces of your system.
But pieces alone don't explain anything — next, we connect them.
```

### Video Script

```
"How can a machine create detailed images of your brain, muscles, and organs using nothing but a magnetic field and radio waves — without a single X-ray or incision?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Magnetic Field Strength' — that's external. The intensity of the static magnetic field in Tesla.
Click on 'Coil Temperature' — that's external. The temperature of the superconducting magnet coils.
Click on 'Image Resolution' — that's internal. The spatial detail visible in the MRI image.
Click on 'Tissue Contrast' — that's internal. The ability to visually distinguish different tissue types in the image based on their different relaxation times — the primary advantage of MRI over other imaging modalities.
Click on 'Patient Safety' — that's internal. The level of risk to the patient during scanning.
Click on 'Energy Consumption' — that's internal. The total electrical power required to operate the MRI system.
Click on 'Diagnostic Accuracy' — that's internal. The probability that the MRI image provides sufficient information for a correct medical diagnosis.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Magnetic Field Strength and Coil Temperature are external components because they are engineering parameters that can be specified and controlled during system design and operation. Magnetic Field Strength is chosen based on the desired image quality, and Coil Temperature is maintained by the cryogenic cooling system. Image Resolution, Tissue Contrast, Patient Safety, Energy Consumption, and Diagnostic Accuracy are internal because they are determined by the physics of nuclear magnetic resonance responding to the field strength and operational conditions.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next step, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 7 components sorted: Magnetic Field Strength, Coil Temperature (External), Image Resolution, Tissue Contrast, Patient Safety, Energy Consumption, Diagnostic Accuracy (Internal)]

### Graph
[Empty graph panel — no simulation yet]

---

## Step 2: ESTABLISH — Connect the Relationships

### Text Editor

```
TIME TO DRAW THE INVISIBLE LINES

Those 7 components don't just sit there — they AFFECT each other.
When one changes, others change too. Let's map those connections.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: OPEN CONNECTION MODE
• Click the "Connect" icon in the TOP LEFT corner of your screen
• Your cursor is now ready to draw relationship arrows

Task B: DRAW YOUR RELATIONSHIPS
• Click on "Magnetic Field Strength" and drag an arrow to "Image Resolution"
• Click on "Magnetic Field Strength" and drag an arrow to "Tissue Contrast"
• Click on "Image Resolution" and drag an arrow to "Diagnostic Accuracy"

Task C: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Magnetic Field Strength → Image Resolution = POSITIVE (+)
    Higher Magnetic Field Strength increases the signal-to-noise ratio of the detected radiofrequency emissions from hydrogen nuclei. More signal relative to noise allows finer spatial detail to be resolved, improving Image Resolution approximately proportionally to field strength.

  ○ Magnetic Field Strength → Tissue Contrast = POSITIVE (+)
    Higher Magnetic Field Strength increases the difference in signal intensity between different tissue types because the Boltzmann distribution creates a larger population difference between aligned and anti-aligned spin states, enhancing the contrast-generating relaxation time differences.

  ○ Image Resolution → Diagnostic Accuracy = POSITIVE (+)
    Higher Image Resolution allows radiologists to detect smaller abnormalities and distinguish fine structural details, directly improving the probability of correct diagnosis. A 1mm resolution MRI can detect tumors invisible on a 3mm resolution scan.

Task D: CHECK YOUR MODEL
• You should have 3 arrows total
• 0 negative relationship(s), 3 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: Higher Magnetic Field Strength improves Image Resolution and Tissue Contrast, increasing Diagnostic Accuracy. But it also increases Energy Consumption, requires colder Coil Temperature, and creates greater Patient Safety risks for people with metallic implants. Where is the optimal balance?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Magnetic Field Strength' and drag an arrow
over to 'Image Resolution.'

Here's the key question: When magnetic field strength goes UP, does
image resolution go UP or DOWN?

Higher Magnetic Field Strength increases the signal-to-noise ratio of the detected radiofrequency emissions from hydrogen nuclei. More signal relative to noise allows finer spatial detail to be resolved, improving Image Resolution approximately proportionally to field strength.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Magnetic Field Strength' and drag an arrow
over to 'Tissue Contrast.'

Here's the key question: When magnetic field strength goes UP, does
tissue contrast go UP or DOWN?

Higher Magnetic Field Strength increases the difference in signal intensity between different tissue types because the Boltzmann distribution creates a larger population difference between aligned and anti-aligned spin states, enhancing the contrast-generating relaxation time differences.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'Image Resolution' and drag an arrow
over to 'Diagnostic Accuracy.'

Here's the key question: When image resolution goes UP, does
diagnostic accuracy go UP or DOWN?

Higher Image Resolution allows radiologists to detect smaller abnormalities and distinguish fine structural details, directly improving the probability of correct diagnosis. A 1mm resolution MRI can detect tumors invisible on a 3mm resolution scan.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Look at your model now. You've got 0 negative and 3
positive relationships. 3 arrows total.

Higher Magnetic Field Strength improves Image Resolution and Tissue Contrast, increasing Diagnostic Accuracy. But it also increases Energy Consumption, requires colder Coil Temperature, and creates greater Patient Safety risks for people with metallic implants. Where is the optimal balance?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Magnetic Field Strength +→ Image Resolution, Magnetic Field Strength +→ Tissue Contrast, Image Resolution +→ Diagnostic Accuracy]

---

## Step 3: VISUALIZE & EVALUATE — Run Your Model

### Text Editor

```
TIME TO SEE YOUR SYSTEM IN ACTION

You built it. You connected it. Now let's see if it actually WORKS
like the real world.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: RUN THE SIMULATION
• Click the "Play" button in the TOP LEFT corner
• Watch the graph panel — you'll see percentage lines for each component

Task B: OBSERVE THE BASELINE
• Let it run for about 30 time steps
• Notice how the lines relate to each other
• When Magnetic Field Strength is HIGH, what happens to the internal components?

Task C: SCENARIO — STANDARD 1.5T
• Clinical standard field strength
• PREDICT FIRST: What do you predict is the relationship between Magnetic Field Strength and Image Resolution at 1.5 Tesla?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task D: SCENARIO — HIGH-FIELD 3T
• Double the standard field strength
• PREDICT FIRST: What do you predict happens to Tissue Contrast and Patient Safety when Magnetic Field Strength doubles from 1.5T to 3T?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task E: SCENARIO — COIL FAILURE
• Superconducting coil warms above critical temperature
• PREDICT FIRST: What do you predict happens to the entire MRI system if the liquid helium cooling fails and Coil Temperature rises?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• MRI creates images using only magnetic fields and radio waves — no ionizing radiation is involved, making it fundamentally safer than X-rays or CT scans for repeated imaging
• Image Resolution and Tissue Contrast both improve with higher Magnetic Field Strength, but the relationship is not linear — doubling field strength from 1.5T to 3T roughly doubles signal-to-noise ratio
• The superconducting coil is the most critical and fragile component — if Coil Temperature rises above the critical threshold, the magnet 'quenches,' explosively boiling the liquid helium and destroying the magnetic field
• The trade-off between image quality and patient safety means that the most powerful MRI machines are not always the best choice — 1.5T is sufficient for most diagnoses and presents fewer safety challenges

THE ANSWER: MRI works by exploiting the magnetic properties of hydrogen atoms — which are abundant in every tissue of the body because we are mostly water. The scanner generates a powerful magnetic field (1.5-3 Tesla) that aligns hydrogen nuclei. Short bursts of radiofrequency energy are then applied, knocking the nuclei out of alignment. As they return to equilibrium, they emit radiofrequency signals that are detected by receiver coils. Different tissues (fat, muscle, cerebrospinal fluid, tumor) have different relaxation times, producing different signal intensities that create contrast in the final image. A computer processes millions of these signals to construct detailed cross-sectional images. No X-rays, no radiation, no incision — just magnets, radio waves, and the hydrogen atoms already inside you.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Standard 1.5T. Clinical standard field strength.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: High-Field 3T.
Double the standard field strength.

Before you run it — make a prediction. What do you predict happens to Tissue Contrast and Patient Safety when Magnetic Field Strength doubles from 1.5T to 3T?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Coil Failure. Superconducting coil warms above critical temperature.
What do you predict happens to the entire MRI system if the liquid helium cooling fails and Coil Temperature rises?

Here's what our model reveals: MRI works by exploiting the magnetic properties of hydrogen atoms — which are abundant in every tissue of the body because we are mostly water. The scanner generates a powerful magnetic field (1.5-3 Tesla) that aligns hydrogen nuclei. Short bursts of radiofrequency energy are then applied, knocking the nuclei out of alignment. As they return to equilibrium, they emit radiofrequency signals that are detected by receiver coils. Different tissues (fat, muscle, cerebrospinal fluid, tumor) have different relaxation times, producing different signal intensities that create contrast in the final image. A computer processes millions of these signals to construct detailed cross-sectional images. No X-rays, no radiation, no incision — just magnets, radio waves, and the hydrogen atoms already inside you.

You just used a computational model to explain a real-world
phenomenon. That's what scientists do every day.

Now it's your turn to ModelIt!"
```

### Graph
[Screenshot showing simulation graph with scenario results — baseline vs. experimental conditions]

---

## Step 4: REVISE & EXTEND — Play, Research, Expand

### Text Editor

```
YOUR MODEL WORKS — BUT IT'S NOT COMPLETE

You built a system model. It explains the basics. But real
systems involve WAY more factors.

Time to play, explore, and make your model BETTER.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PLAY TIME CHALLENGES:

1. TELL THE STORY
   • Run your simulation
   • Pretend you're a scientist presenting your findings
   • Explain what's happening and WHY to your partner

2. BREAK THE SYSTEM
   • What happens if you turn OFF Magnetic Field Strength?
   • What happens if you turn OFF Coil Temperature?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Gradient Coil Precision — The accuracy of the additional magnetic field gradients that encode spatial location in the MRI signal — more precise gradients produce higher resolution images but generate louder noise and more heat
   • Scan Duration — The total time required to acquire sufficient data for a diagnostic-quality image — longer scans produce better images but increase patient discomfort, motion artifacts, and system operating costs
   • RF Pulse Sequence Design — The specific pattern and timing of radiofrequency pulses used to generate tissue-specific contrast — different sequences (T1-weighted, T2-weighted, FLAIR) highlight different tissue properties for different diagnostic purposes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • The Physics of Nuclear Magnetic Resonance — how does this connect to your model?
   • How Contrast Works — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model demonstrate why MRI is preferred over CT scans for soft tissue imaging despite being more expensive and slower?
   • What does the coil failure scenario reveal about the engineering fragility of the superconducting magnet system?
   • Why is there an optimal Magnetic Field Strength rather than simply using the strongest possible magnet?
   • How does your model help explain the extreme cost of MRI machines ($1-3 million) and MRI scans ($500-$5,000)?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ADD TO YOUR MODEL:
   • Pick ONE new component from your research
   • Decide: Is it INTERNAL or EXTERNAL?
   • Add it to your model (Plus button)
   • Connect it with relationships (+/−)
   • Run the simulation — does it work like you expected?

What story does your NEW model tell?
```

### Video Script

```
"Your model works. It showed us how the key components interact
and why things happen the way they do. But you and I both know
this isn't the whole story.

Real systems are way more complicated. So now it's time to PLAY,
QUESTION, and EXPAND.

First — tell the story. Run your simulation and pretend you're
a scientist presenting your findings at a conference. Explain
what's happening and WHY to someone next to you. If you can
explain it, you understand it.

Second — break the system. Change the variables. Turn things
on and off. What combinations create extreme results? What
keeps things stable? This is where real insight happens.

Third — and this is the big one — ask what's MISSING.

Your model has 7 components. Real systems involve
way more. Think about...

Gradient Coil Precision. The accuracy of the additional magnetic field gradients that encode spatial location in the MRI signal — more precise gradients produce higher resolution images but generate louder noise and more heat
How would you model that?

Scan Duration. The total time required to acquire sufficient data for a diagnostic-quality image — longer scans produce better images but increase patient discomfort, motion artifacts, and system operating costs
How would you model that?

RF Pulse Sequence Design. The specific pattern and timing of radiofrequency pulses used to generate tissue-specific contrast — different sequences (T1-weighted, T2-weighted, FLAIR) highlight different tissue properties for different diagnostic purposes
How would you model that?

Here's your mission: Research ONE new factor. Find out how it
actually works in the real world. Then add it to your model.

Is it internal or external? Click the plus button to add it.
Draw the connections. Set positive or negative. Run the simulation.

Does your new model match reality better than before?

This is how real scientists work. Start simple. Test it. Add
complexity. Test again. Your model is never 'done' — it's
always getting better.

What story will YOUR expanded model tell?

Now it's your turn to ModelIt!"
```

### Activity Network
[Screenshot showing expanded model with 1-2 additional components added by student]

---

## Fun Fact (Career Connection)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔬 CAREER CONNECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MRI Physicists design and optimize MRI scanning protocols and develop new imaging techniques. They work in hospitals, research universities, and medical device companies, earning $90,000–$180,000/year. Biomedical Engineers who design medical imaging equipment earn $75,000–$150,000/year.

These professionals build models just like the one you made
today — understanding cause-and-effect relationships to solve
real-world problems. Your simple model? That's step one toward
this career.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## TPT Materials

### PowerPoint Slides

```
SLIDE 1: COVER
Visual: Title slide with dramatic MRI scanner image
Say: "This machine can see inside your skull without touching you. No X-rays. No cutting. Just magnets and radio waves. How is that even possible?"
Do: Show a stunning MRI brain scan image. Ask: How can a magnet create a picture of something it can't touch? Collect initial hypotheses.
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and vocabulary terms
Say: "Today you're modeling one of the most sophisticated machines in modern medicine — and the physics that makes it work is something you already know: electromagnetism."
Do: Have students read objectives. Pre-teach 'nuclear magnetic resonance' and 'relaxation time.' Quick-write: What do you think happens to atoms in a magnetic field?
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: How do doctors see inside you without cutting you open?
Say: "Your body is 60% water. Water is H2O. Those hydrogen atoms are about to become the most important atoms in medicine."
Do: Students estimate: How many hydrogen atoms are in your body? (Answer: approximately 4 x 10^27.) Ask: What if you could make every single one of them send you a signal?
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps overview
Say: "We're going to model how magnets, cold, and radio waves combine to create the most detailed images of the human body ever possible."
Do: Preview each LEVER step. Emphasize that MRI connects quantum physics (nuclear spin) to clinical medicine (diagnosis).
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Seven component cards for MRI system model
Say: "Two things engineers control: how strong to make the magnet and how cold to keep it. The physics and the patient determine everything else."
Do: Guide component sorting. Discuss why Magnetic Field Strength and Coil Temperature are external (engineering choices) while image quality and safety are internal responses.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows between MRI system components
Say: "Stronger magnet means better images. But it also means more energy, more danger, and one malfunction away from a catastrophic quench."
Do: Help students map the trade-offs: field strength improves image quality but increases energy, cost, and safety concerns. Trace the coil temperature failure cascade.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Graph predictions and simulation results for three scenarios
Say: "Let's compare a standard hospital MRI, a research powerhouse, and what happens when the cooling fails spectacularly."
Do: Students predict outcomes for each scenario. Run simulations. The quench scenario is particularly dramatic — discuss what happens physically.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key findings from MRI system model
Say: "You just modeled a $2 million machine that uses the coldest temperature in the hospital to detect the warmest thing in medicine: living tissue."
Do: Lead discussion connecting model findings to real MRI capabilities and limitations. Show clinical MRI images comparing healthy and diseased tissue.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Portable MRI design challenge
Say: "70% of the world has no access to MRI. Design the machine that changes that — even if it means sacrificing the Rolls Royce version for something that actually reaches people."
Do: Groups design portable MRI concepts. Must specify magnet type, field strength, target diagnoses, power requirements, and cost estimate. Present as startup pitches.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: How Do Doctors See Inside You Without Cutting You Open?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
Magnetic Resonance Imaging is one of the most remarkable achievements of applied physics — it turns the quantum mechanical properties of hydrogen atoms into detailed images of the human body's interior. Without a single X-ray photon or surgical incision, MRI can distinguish between healthy and diseased tissue, map brain activity, visualize blood flow, and detect tumors as small as a few millimeters.

NGSS ALIGNMENT:
HS-PS2-4, HS-PS4-4: Use mathematical representations of Newton's law of gravitation and Coulomb's law to describe and predict the gravitational and electrostatic forces between objects. Evaluate the validity and reliability of claims in published materials of the effects that different frequencies of electromagnetic radiation have when absorbed by matter.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Evaluating Claims
  Students evaluate claims about medical imaging technologies by modeling the physics-based trade-offs between field strength, image quality, safety, and cost.
• Disciplinary Core Idea: PS2.B Types of Interactions / PS4.B Electromagnetic Radiation
  Magnetic fields exert forces on aligned nuclear magnetic moments; radiofrequency electromagnetic radiation can be absorbed and re-emitted by atomic nuclei, with tissue-dependent properties that enable medical imaging.
• Crosscutting Concept: Structure and Function
  Students analyze how the physical structure of MRI components (superconducting coils, gradient coils, RF transmitters) determines the functional capability of the imaging system.

PACING GUIDE:
• Step 1 (Locate): 8-10 minutes
• Step 2 (Establish): 8-10 minutes
• Step 3 (Visualize & Evaluate): 10-12 minutes
• Step 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Nuclear Magnetic Resonance, Magnetic Field Strength, Relaxation Time, Superconducting Coil
□ Prepare How can a machine create detailed images of your brain, muscles, and organs using nothing but a magnetic field and radio waves — without a single X-ray or incision discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify seven components of the MRI system: Magnetic Field Strength, Coil Temperature, Image Resolution, Tissue Contrast, Patient Safety, Energy Consumption, and Diagnostic Accuracy — with Magnetic Field Strength and Coil Temperature as external engineering parameters.
• Establish: Students determine that Magnetic Field Strength drives Image Resolution and Tissue Contrast (both improving signal-to-noise ratio), which together determine Diagnostic Accuracy. Higher field strength increases Energy Consumption and creates greater Patient Safety concerns. Coil Temperature must stay below the superconducting critical point.
• Visualize: Students build a computational model showing how field strength affects all downstream parameters and the trade-offs between image quality, safety, and cost.
• Evaluate: Students run 1.5T standard, 3T high-field, and coil failure scenarios to compare image quality, safety profiles, and the consequences of system failure.
• Revise: Students add Gradient Coil Precision, Scan Duration, or RF Pulse Sequence Design to explore how additional engineering parameters affect MRI performance optimization.

BACKGROUND CONTENT:
• The Physics of Nuclear Magnetic Resonance:
  Every hydrogen atom has a nucleus (single proton) that acts as a tiny magnetic dipole — a miniature bar magnet. Normally, these nuclear magnets point in random directions, canceling out. But when placed in a strong external magnetic field, the protons align either parallel or antiparallel to the field, with a slight majority parallel (lower energy state). This creates a net magnetization that can be manipulated with radio waves. When a radiofrequency pulse at the precise resonance frequency (the Larmor frequency, proportional to field strength) is applied, it flips the aligned protons to the higher energy state. When the pulse stops, the protons relax back to equilibrium, emitting radiofrequency signals as they do. These signals are the raw data of MRI.

• How Contrast Works:
  The key to MRI's diagnostic power is that different tissues have different relaxation times. T1 relaxation (spin-lattice) measures how quickly protons return to alignment with the main field. T2 relaxation (spin-spin) measures how quickly the precessing protons fall out of phase with each other. Fat has short T1 (recovers quickly, appears bright on T1-weighted images). Cerebrospinal fluid has long T1 and long T2 (appears dark on T1, bright on T2). Tumors often have different relaxation times from surrounding healthy tissue, making them visible. By adjusting the timing of RF pulses (the pulse sequence), radiologists can create images that highlight specific tissue properties.

• The Superconducting Magnet:
  Creating a stable, powerful, and homogeneous magnetic field requires a superconducting electromagnet. Miles of niobium-titanium wire are wound into coils and cooled to 4.2 Kelvin (-269 degrees Celsius) using liquid helium. At this temperature, the wire's electrical resistance drops to exactly zero, allowing thousands of amperes to flow without energy loss. Once energized, the current circulates indefinitely — many MRI magnets have been running continuously for years without being re-energized. But the system is fragile: if any section of the coil warms above the critical temperature, resistance appears, generating heat that boils the helium explosively in a 'quench' — a dramatic and expensive failure.

• Safety and Limitations:
  MRI is generally very safe because it uses non-ionizing radiation (radio waves, not X-rays). However, the powerful magnetic field creates unique hazards. Ferromagnetic objects (iron, steel) become high-velocity projectiles when brought near the scanner — MRI-related accidents from chairs, oxygen tanks, and tools being pulled into the bore have caused injuries and deaths. Patients with certain metallic implants (pacemakers, cochlear implants, shrapnel) cannot safely enter the magnetic field. The strong radiofrequency pulses deposit energy in tissue (measured as Specific Absorption Rate, SAR), which can cause heating. The loud noise from gradient coil switching (up to 130 dB) requires hearing protection.

COMMON MISCONCEPTIONS:
• "MRI uses radiation like X-rays"
  Reality: MRI uses radiofrequency electromagnetic radiation, which is non-ionizing — the same fundamental type as FM radio signals and Wi-Fi, just at specific frequencies that resonate with hydrogen nuclei. Unlike X-rays and CT scans, MRI does not use ionizing radiation that can damage DNA. This is why MRI is preferred for repeated imaging and for patients where radiation exposure is a concern (children, pregnant women).
  Strategy: Compare photon energies: An X-ray photon carries enough energy to ionize atoms and break DNA bonds. An MRI radiofrequency photon has about 100 million times LESS energy per photon — far too low to cause any ionization damage.

• "Stronger magnets are always better for MRI"
  Reality: While higher field strength improves signal-to-noise ratio and image resolution, it also increases safety risks (stronger forces on metallic objects, higher SAR), cost, energy consumption, and technical complexity. For most clinical diagnoses, 1.5T provides sufficient image quality. The trend toward higher fields (3T, 7T) is driven by research applications that need extremely fine detail, not by clinical necessity.
  Strategy: Real-world context: Most hospitals worldwide use 1.5T MRI and achieve excellent diagnostic outcomes. A 3T scanner costs 50-100% more to purchase and operate but provides only marginal improvement for the majority of clinical scans.

• "MRI is perfectly safe for everyone"
  Reality: While MRI does not use ionizing radiation, it is not risk-free. The powerful magnetic field can turn ferromagnetic objects into dangerous projectiles, cause implanted devices (pacemakers, neurostimulators) to malfunction, and move metallic foreign bodies within the body. The RF pulses deposit thermal energy in tissue, which can be problematic at high field strengths. The gradient coil switching produces noise levels up to 130 dB — loud enough to cause hearing damage without ear protection.
  Strategy: Safety perspective: More people have been injured by MRI accidents involving metallic objects being pulled into the scanner than by any radiation effect from MRI — because the radiation risk is essentially zero but the magnetic projectile risk is real and immediate.

FACILITATION TIPS:
• Step 1: Let students explore the interface. Don't over-explain.
  Let them discover. Circulate and support, don't lecture.
• Step 2: Ask "When this goes up, what happens to that?" to
  guide positive/negative relationship decisions. Let students debate.
• Step 3: Give time for students to "break" the model — turn
  things on/off and observe. This is where real insight happens.
• Step 4: Don't give answers. Ask questions. Let curiosity drive
  the research. Celebrate when students' additions don't work as
  expected — that's authentic science.

ANSWER KEY:
Big Question: How can a machine create detailed images of your brain, muscles, and organs using nothing but a magnetic field and radio waves — without a single X-ray or incision?
Answer: MRI works by exploiting the magnetic properties of hydrogen atoms — which are abundant in every tissue of the body because we are mostly water. The scanner generates a powerful magnetic field (1.5-3 Tesla) that aligns hydrogen nuclei. Short bursts of radiofrequency energy are then applied, knocking the nuclei out of alignment. As they return to equilibrium, they emit radiofrequency signals that are detected by receiver coils. Different tissues (fat, muscle, cerebrospinal fluid, tumor) have different relaxation times, producing different signal intensities that create contrast in the final image. A computer processes millions of these signals to construct detailed cross-sectional images. No X-rays, no radiation, no incision — just magnets, radio waves, and the hydrogen atoms already inside you.

Simulation Answers:
• Standard 1.5T Scenario: At 1.5 Tesla, the MRI produces clinical-quality images with adequate Image Resolution (approximately 1mm) and good Tissue Contrast for most diagnostic purposes. Patient Safety is well-managed at this field strength with standard screening protocols. Energy Consumption is substantial but manageable for hospital infrastructure. Diagnostic Accuracy is sufficient for the vast majority of clinical indications — this is why 1.5T remains the global clinical workhorse.
• Coil Failure Scenario: When Coil Temperature rises above the superconducting critical point (9.2K for NbTi), electrical resistance suddenly appears. The enormous current (hundreds of amperes) generates intense heat, which boils the liquid helium explosively. The magnetic field collapses in seconds as the quench propagates through all coils. The scanner becomes non-functional, requiring weeks of repair, re-cooling, and re-energization. In worst cases, the explosive helium boil-off can displace oxygen from the scanner room, creating an asphyxiation hazard.

Reflection Exemplars:
• Q: Why is MRI safer than CT but more expensive?
  A: MRI uses non-ionizing radiation (radiofrequency waves) while CT uses ionizing X-rays that can damage DNA and increase cancer risk. This makes MRI inherently safer for repeated imaging and for vulnerable populations like children and pregnant women. However, MRI's safety comes at an engineering cost: generating the powerful magnetic field requires superconducting coils cooled to near absolute zero with liquid helium, which is expensive to install, maintain, and operate. A CT scanner costs $500K-$1M; an MRI costs $1-3M. CT scan costs $200-$1,000; MRI scan costs $500-$5,000.
• Q: Why is there an optimal field strength?
  A: The model shows that increasing Magnetic Field Strength improves Image Resolution and Tissue Contrast, but with diminishing returns at higher strengths. Meanwhile, Patient Safety concerns increase because stronger fields create greater forces on metallic implants, higher RF energy deposition (SAR), and louder noise. Energy Consumption scales with field strength as well. For most clinical diagnoses, 1.5T provides sufficient quality at manageable cost and safety. 3T is used when higher resolution is needed (neuroimaging, research). 7T and above are research-only because Patient Safety challenges become severe.

STEM CHALLENGE GUIDANCE:
Title: Design a Next-Generation Portable MRI System
Mission: Design a compact, lower-cost MRI system that could be deployed in rural clinics, ambulances, or developing countries where traditional MRI is unavailable.
Scenario: A medical technology startup wants to bring MRI capabilities to the 70% of the world's population that currently has no access to MRI imaging. Your team has been hired to design a portable MRI system that sacrifices some image quality for dramatic reductions in cost, size, and power requirements.
Introduction: Present the challenge: A medical startup wants to bring MRI to the 70% of the world without access. Your team will design a portable MRI system that dramatically reduces cost, size, and power requirements — accepting some image quality trade-offs to make the technology accessible to billions of people.

Key Concepts:
• Permanent Magnet MRI: Instead of superconducting coils requiring liquid helium, portable MRI systems can use permanent magnets made of rare-earth materials (neodymium). These generate weaker fields (0.05-0.5T) but require no cooling, no electricity for the magnet, and weigh hundreds of kilograms instead of tons. The trade-off is lower Image Resolution and longer scan times.
• Point-of-Care Diagnostics: In resource-limited settings, the diagnostic question is often simpler: Is there a stroke? Is this bone fractured? Is there a brain tumor? These binary diagnostic decisions may not require 1mm resolution — a portable 0.05T system that can answer these questions could save more lives than a 3T research scanner that serves only wealthy hospitals.
• AI-Enhanced Imaging: Machine learning algorithms can significantly improve the quality of images from low-field MRI systems by reducing noise, enhancing contrast, and compensating for resolution limitations. This allows portable MRI to approach diagnostic accuracy of higher-field systems for specific clinical questions.

Evaluation Rubric:
• Expert (4): Design specifies magnet type, field strength, target diagnostic applications, power and cooling requirements, estimated cost, AI enhancement strategy, and addresses patient safety — with model data justifying all trade-off decisions
• Proficient (3): Design addresses magnet technology and target applications with reasonable specifications and some model-based justification
• Developing (2): Design includes some specifications but lacks clear trade-off analysis or connection to model evidence
• Beginning (1): Design is incomplete or does not address the fundamental physics constraints of portable MRI

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a comparison chart showing field strength, image resolution, cost, weight, and power requirements for 3T, 1.5T, 0.5T, and 0.05T MRI systems
  • Use a diagram showing the basic MRI signal chain: magnetic field alignment, RF pulse excitation, relaxation signal emission, and image reconstruction
  • Sentence frames: 'When Magnetic Field Strength is reduced from __ to __, Image Resolution decreases by approximately __ because __, but the system becomes portable because __'

Extensions (Advanced Learners):
  • Research the Hyperfine Research portable MRI system (0.064T, $50,000) and analyze how it achieves diagnostic utility at a fraction of the cost and field strength of traditional systems
  • Investigate functional MRI (fMRI) and how it detects brain activity by measuring blood oxygen level changes — model how this extends MRI from structural to functional imaging
  • Compare the physics of MRI, CT, PET, and ultrasound imaging and create a decision guide for when each modality is most appropriate

Cross-Curricular Connections:
  • Math: Calculate the Larmor frequency for hydrogen protons at 1.5T and 3T (gyromagnetic ratio = 42.576 MHz/T) and explain why different field strengths require different RF frequencies
  • ELA: Write a patient information sheet that explains MRI in accessible language, addressing common fears (claustrophobia, loud noise, magnetic safety) while accurately conveying the science
  • Social Studies: Research global access to medical imaging technology and analyze how the distribution of MRI machines correlates with national wealth, healthcare spending, and health outcomes

CAST ALIGNMENT:
• Model how magnetic field strength and tissue relaxation properties interact to produce diagnostic medical images
• Analyze the trade-offs between image quality, patient safety, and system cost in MRI technology
• Evaluate why MRI uses non-ionizing radiation and how this affects its safety profile compared to X-ray and CT imaging

CAST-Style Assessment Questions:
• Multiple Choice: A hospital is choosing between a 1.5T MRI and a 3T MRI. Based on your model, which factor would most improve by upgrading to 3T?
• Constructed Response: Using your model, explain how MRI creates images of soft tissues without using X-rays or any ionizing radiation. Reference Magnetic Field Strength, Tissue Contrast, and the role of hydrogen nuclei in your explanation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: How Do Doctors See Inside You Without Cutting You Open?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. What do you know about how MRI machines create images of the inside of the body?

   _________________________________________________________

   _________________________________________________________

2. Why might a doctor choose MRI over an X-ray for certain types of injuries or conditions?

   _________________________________________________________

   _________________________________________________________

3. Draw a diagram showing what you think happens inside an MRI machine when it scans a patient.

   [DRAWING BOX]

4. What role do magnets play in medical imaging — how could a magnet help see inside a person?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Nuclear Magnetic Resonance    
___ Magnetic Field Strength       
___ Relaxation Time               
___ Superconducting Coil          

A. The physical phenomenon where atomic nuclei with odd numbers of protons or neutrons absorb and re-emit radiofrequency energy when placed in a magnetic field — the principle underlying MRI technology
B. The intensity of the magnetic field generated by the MRI scanner, measured in Tesla — clinical MRI machines typically operate at 1.5 to 3 Tesla, which is 30,000 to 60,000 times Earth's magnetic field
C. The time it takes for hydrogen nuclei to return to their equilibrium alignment after being excited by a radiofrequency pulse — different tissues have different relaxation times, creating the contrast that makes MRI images useful
D. An electromagnet made of special alloys (niobium-titanium) cooled to near absolute zero (-269 degrees Celsius) with liquid helium, which carries electrical current with zero resistance to generate the powerful, stable magnetic field required for MRI

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MODEL PLANNING SPACE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before you build in ModelIt, sort your components here:

EXTERNAL (can't control):
_______________ _______________ _______________

INTERNAL (changes based on other things):
_______________ _______________ _______________

Draw arrows showing relationships. Label each + or −.

[MODEL SKETCH BOX]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SIMULATION OBSERVATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SCENARIO: Standard 1.5T
Settings: Clinical standard field strength
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: High-Field 3T
Settings: Double the standard field strength
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Coil Failure
Settings: Superconducting coil warms above critical temperature
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

The KEY discovery from my simulation is:

_________________________________________________________

_________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESEARCH & EXTEND
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NEW COMPONENT I want to add: _____________________________

Is it EXTERNAL or INTERNAL? (circle one)

What does it connect to? _________________________________

Is the relationship POSITIVE or NEGATIVE? _________________

Why? ____________________________________________________

_________________________________________________________

After adding it, my simulation showed:

_________________________________________________________

_________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. How does your model demonstrate why MRI is preferred over CT scans for soft tissue imaging despite being more expensive and slower?

   _________________________________________________________

   _________________________________________________________

2. What does the coil failure scenario reveal about the engineering fragility of the superconducting magnet system?

   _________________________________________________________

   _________________________________________________________

3. Why is there an optimal Magnetic Field Strength rather than simply using the strongest possible magnet?

   _________________________________________________________

   _________________________________________________________

4. How does your model help explain the extreme cost of MRI machines ($1-3 million) and MRI scans ($500-$5,000)?

   _________________________________________________________

   _________________________________________________________

5. What are the limitations of modeling MRI physics with only seven components when real MRI involves quantum spin physics, Fourier transforms, and complex pulse sequence programming?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. How can a machine create detailed images of your brain, muscles, and organs using nothing but a magnetic field and radio waves — without a single X-ray or incision? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Evaluating Claims
   □ Disciplinary Core Idea: PS2.B Types of Interactions / PS4.B Electromagnetic Radiation
   □ Crosscutting Concept: Structure and Function

3. What are the limitations of modeling MRI physics with only seven components when real MRI involves quantum spin physics, Fourier transforms, and complex pulse sequence programming?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Next-Generation Portable MRI System
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design a compact, lower-cost MRI system that could be deployed in rural clinics, ambulances, or developing countries where traditional MRI is unavailable.

SCENARIO: A medical technology startup wants to bring MRI capabilities to the 70% of the world's population that currently has no access to MRI imaging. Your team has been hired to design a portable MRI system that sacrifices some image quality for dramatic reductions in cost, size, and power requirements.

GUIDING QUESTIONS:
• What Magnetic Field Strength would you use for a portable system — and what diagnostic capabilities would you sacrifice?
• Could you eliminate the superconducting coils (and liquid helium cooling) by using permanent magnets, and what would that trade away?
• What is the minimum Image Resolution needed to diagnose the most common conditions in underserved areas (stroke, fractures, tumors)?

DESIGN THINKING:
• What type of magnet technology would you use — superconducting, permanent, or resistive electromagnets?

  _________________________________________________________

• How would you power the system in locations without reliable electricity?

  _________________________________________________________

• What imaging protocols would you prioritize for the most impactful diagnoses in resource-limited settings?

  _________________________________________________________

• How would you address patient safety with a system that might be operated by non-specialist technicians?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Design specifies magnet type, field strength, target diagnostic applications, power and cooling requirements, estimated cost, AI enhancement strategy, and addresses patient safety — with model data justifying all trade-off decisions
• Proficient (3): Design addresses magnet technology and target applications with reasonable specifications and some model-based justification
• Developing (2): Design includes some specifications but lacks clear trade-off analysis or connection to model evidence
• Beginning (1): Design is incomplete or does not address the fundamental physics constraints of portable MRI

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-10/G10L2-L09/G10L2-L09-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-10/G10L2-L09/G10L2-L09-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-10/G10L2-L09/G10L2-L09-Student-Presentation.pptx] |
| Platform Link | [ModelIt lesson link] |

---

## Lesson Metadata

| Field | Value |
|-------|-------|
| Created | February 2026 |
| Author | Alexandria's Design |
| Template Version | 1.0 |
| Platform | ModelIt (formerly Cell Collective) |
| Estimated Time | 50-70 minutes |
| Can Split Across | 2 class periods |