# Lesson: Can Nanotechnology Deliver Medicine to Individual Cells?

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G11L3-L09 |
| **Grade** | 11th Grade — Level 3: Systems Innovation Lab |
| **Lesson Name** | Can Nanotechnology Deliver Medicine to Individual Cells? |
| **Status** | Template |

---

## Platform

### Title
**Can Nanotechnology Deliver Medicine to Individual Cells? — Modeling Targeted Drug Delivery, Nanoparticle Design, and Therapeutic Precision**

### Overview
Conventional chemotherapy is a blunt instrument: toxic drugs are injected into the bloodstream and distribute throughout the entire body, killing rapidly dividing cells wherever they are found — cancer cells in the tumor, but also hair follicle cells, gut lining cells, and bone marrow cells, causing the devastating side effects that make chemotherapy so brutal. The fundamental problem is targeting: how do you get the drug to the cancer and nowhere else? Nanotechnology offers a potential solution by packaging drugs inside nanoscale carriers designed to navigate biological barriers, evade immune destruction, and concentrate their payload at the tumor site. The vision is compelling. The reality is more complex — and more instructive — than the headlines suggest. Students investigate the driving question: Can we design nanoparticles that navigate the human body, find specific diseased cells, and deliver medication directly to them — turning the blunt instrument of chemotherapy into a precision tool? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of nanoparticles navigating through a blood vessel toward a cancer cell with targeting ligands binding to cell surface receptors, subtle glowing visualization of drug release, featuring a diverse multicultural group with Black people centered of 16-17 year old students observing the molecular visualization on advanced displays in a nanomedicine research lab]

### Grade
11th Grade — Level 3: Systems Innovation Lab

### NGSS Standard
**HS-LS1-3, HS-PS2-4**: Plan and conduct an investigation to provide evidence that feedback mechanisms maintain homeostasis. Use mathematical representations of Newton's Law of Gravitation and Coulomb's Law to describe and predict the gravitational and electrostatic forces between objects.

### Learning Objectives
- Model how nanoparticle size, surface chemistry, and targeting ligands determine biodistribution and cellular uptake in the human body
- Analyze the relationship between nanoparticle design parameters, biological barriers, and the percentage of injected dose that reaches the target tissue
- Evaluate the trade-offs between nanoparticle stability in the bloodstream and the ability to release drug payload at the target site
- Predict how the enhanced permeability and retention effect, active targeting, and immune system clearance interact to determine therapeutic efficacy

### Component List (Starting Model: 7 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Nanoparticle Size | External | The diameter of the drug-carrying nanoparticle in nanometers — determines which biological barriers it can cross, how quickly the immune system clears it, and whether it can exploit the enhanced permeability and retention effect to accumulate in tumors |
| Surface PEGylation | External | The coating of the nanoparticle surface with polyethylene glycol polymer chains that create a hydrophilic stealth layer, reducing protein adsorption and immune recognition — extending circulation half-life from minutes to hours but potentially reducing cellular uptake at the target |
| Targeting Ligand Density | Internal | The number of targeting molecules per nanoparticle surface area — more ligands increase binding probability to target cells but also increase immune recognition, production complexity, and the risk of binding to off-target cells that express low levels of the same receptor |
| Immune Clearance Rate | Internal | The speed at which the mononuclear phagocyte system — primarily macrophages in the liver and spleen — recognizes and removes nanoparticles from the bloodstream, determined by particle size, surface charge, and the degree to which blood proteins coat the particle |
| Tumor Accumulation | Internal | The percentage of the injected nanoparticle dose that reaches and remains in the target tumor — typically only 0.7% of injected nanoparticles reach the tumor, with the vast majority sequestered in the liver (30-99%), spleen, and lungs |
| Drug Release Rate | Internal | The speed at which the therapeutic payload is released from the nanoparticle — must be slow enough that the drug is not lost during circulation but fast enough that therapeutic concentrations are achieved at the target site within the drug's activity window |
| Off-Target Toxicity | Internal | The damage caused to healthy tissues by nanoparticles and their drug payloads that do not reach the intended target — even with targeting, the majority of nanoparticles accumulate in the liver and spleen, potentially causing hepatotoxicity and immune suppression |

### Research for Lesson
- Nanoparticles as Drug Carriers — reference materials and textbook resources
- Biological Barriers to Nanoparticle Delivery — reference materials and textbook resources
- PEGylation and the Stealth Challenge — reference materials and textbook resources
- The Targeting Reality Check — reference materials and textbook resources

---

## Step 1: LOCATE — Build Your System

### Text Editor

```
CAN NANOTECHNOLOGY DELIVER MEDICINE TO INDIVIDUAL CELLS?

Modeling Targeted Drug Delivery, Nanoparticle Design, and Therapeutic Precision.
Can we design nanoparticles that navigate the human body, find specific diseased cells, and deliver medication directly to them — turning the blunt instrument of chemotherapy into a precision tool?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Nanoparticle Size" — the diameter of the drug-carrying nanoparticle in nanometers — determines which biological barriers it can cross
  ○ Click "Surface PEGylation" — the coating of the nanoparticle surface with polyethylene glycol polymer chains that create a hydrophilic stealth layer
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Targeting Ligand Density" — the number of targeting molecules per nanoparticle surface area — more ligands increase binding probability to target cells but also increase immune recognition
  ○ Click "Immune Clearance Rate" — the speed at which the mononuclear phagocyte system — primarily macrophages in the liver and spleen — recognizes and removes nanoparticles from the bloodstream
  ○ Click "Tumor Accumulation" — the percentage of the injected nanoparticle dose that reaches and remains in the target tumor — typically only 0
  ○ Click "Drug Release Rate" — the speed at which the therapeutic payload is released from the nanoparticle — must be slow enough that the drug is not lost during circulation but fast enough that therapeutic concentrations are achieved at the target site within the drug's activity window
  ○ Click "Off-Target Toxicity" — the damage caused to healthy tissues by nanoparticles and their drug payloads that do not reach the intended target — even with targeting

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
"Can we design nanoparticles that navigate the human body, find specific diseased cells, and deliver medication directly to them — turning the blunt instrument of chemotherapy into a precision tool?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Nanoparticle Size' — that's external. The diameter of the drug-carrying nanoparticle in nanometers — determines which biological barriers it can cross.
Click on 'Surface PEGylation' — that's external. The coating of the nanoparticle surface with polyethylene glycol polymer chains that create a hydrophilic stealth layer.
Click on 'Targeting Ligand Density' — that's internal. The number of targeting molecules per nanoparticle surface area — more ligands increase binding probability to target cells but also increase immune recognition.
Click on 'Immune Clearance Rate' — that's internal. The speed at which the mononuclear phagocyte system — primarily macrophages in the liver and spleen — recognizes and removes nanoparticles from the bloodstream.
Click on 'Tumor Accumulation' — that's internal. The percentage of the injected nanoparticle dose that reaches and remains in the target tumor — typically only 0.
Click on 'Drug Release Rate' — that's internal. The speed at which the therapeutic payload is released from the nanoparticle — must be slow enough that the drug is not lost during circulation but fast enough that therapeutic concentrations are achieved at the target site within the drug's activity window.
Click on 'Off-Target Toxicity' — that's internal. The damage caused to healthy tissues by nanoparticles and their drug payloads that do not reach the intended target — even with targeting.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Nanoparticle Size is external because it represents a fundamental design parameter selected during nanoparticle manufacturing — engineers choose the synthesis conditions that produce a specific size range. Surface PEGylation is external because it represents a surface modification decision made during particle design and manufacturing, independent of biological conditions. The remaining five components are internal: Targeting Ligand Density is a design output that creates complex biological trade-offs, Immune Clearance Rate is determined by the biological response to the particle's physical and chemical properties, Tumor Accumulation is the outcome of immune clearance rate, EPR effect, and circulation time, Drug Release Rate depends on the interaction between particle chemistry and the biological environment at the target, and Off-Target Toxicity is the consequence of drug distribution to non-target tissues.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next step, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 7 components sorted: Nanoparticle Size, Surface PEGylation (External), Targeting Ligand Density, Immune Clearance Rate, Tumor Accumulation, Drug Release Rate, Off-Target Toxicity (Internal)]

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
• Click on "Surface PEGylation" and drag an arrow to "Immune Clearance Rate"
• Click on "Immune Clearance Rate" and drag an arrow to "Tumor Accumulation"
• Click on "Nanoparticle Size" and drag an arrow to "Tumor Accumulation"
• Click on "Drug Release Rate" and drag an arrow to "Off-Target Toxicity"

Task C: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Surface PEGylation → Immune Clearance Rate = NEGATIVE (−)
    Denser PEG coating creates a more effective stealth layer that reduces protein adsorption and macrophage recognition, directly decreasing the rate at which the immune system removes nanoparticles from circulation. This extended circulation time is the most important effect of PEGylation.

  ○ Immune Clearance Rate → Tumor Accumulation = NEGATIVE (−)
    Faster immune clearance removes nanoparticles from the bloodstream before they can accumulate at the tumor site through the EPR effect. Each pass through the liver removes a fraction of circulating particles, so faster clearance means fewer particles remain available for tumor delivery.

  ○ Nanoparticle Size → Tumor Accumulation = POSITIVE (+)
    Particles must be large enough (greater than 10 nanometers) to avoid rapid kidney filtration and small enough (less than 200 nanometers) to exploit the enhanced permeability and retention effect through tumor vessel gaps. The optimal size range for tumor accumulation is typically 50-150 nanometers, with accumulation dropping off sharply outside this window.

  ○ Drug Release Rate → Off-Target Toxicity = POSITIVE (+)
    If drug is released too quickly — before the nanoparticle reaches the tumor — the freed drug distributes throughout the body causing off-target toxicity similar to conventional chemotherapy. Slower, controlled release that activates preferentially at the tumor site reduces off-target exposure and toxicity.

Task D: CHECK YOUR MODEL
• You should have 4 arrows total
• 2 negative relationship(s), 1 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: When you inject nanoparticles into the bloodstream, they enter a hostile environment: blood proteins immediately coat them, immune cells try to eat them, and the liver and spleen filter them out. Only about 0.7% of injected nanoparticles — less than 1 in 100 — actually reach a tumor. That tiny percentage is still an improvement over conventional chemotherapy. How do you design a particle that survives this gauntlet?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Surface PEGylation' and drag an arrow
over to 'Immune Clearance Rate.'

Here's the key question: When surface pegylation goes UP, does
immune clearance rate go UP or DOWN?

Denser PEG coating creates a more effective stealth layer that reduces protein adsorption and macrophage recognition, directly decreasing the rate at which the immune system removes nanoparticles from circulation. This extended circulation time is the most important effect of PEGylation.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Next connection: Click on 'Immune Clearance Rate' and drag an arrow
over to 'Tumor Accumulation.'

Here's the key question: When immune clearance rate goes UP, does
tumor accumulation go UP or DOWN?

Faster immune clearance removes nanoparticles from the bloodstream before they can accumulate at the tumor site through the EPR effect. Each pass through the liver removes a fraction of circulating particles, so faster clearance means fewer particles remain available for tumor delivery.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Last connection: Click on 'Nanoparticle Size' and drag an arrow
over to 'Tumor Accumulation.'

Here's the key question: When nanoparticle size goes UP, does
tumor accumulation go UP or DOWN?

Particles must be large enough (greater than 10 nanometers) to avoid rapid kidney filtration and small enough (less than 200 nanometers) to exploit the enhanced permeability and retention effect through tumor vessel gaps. The optimal size range for tumor accumulation is typically 50-150 nanometers, with accumulation dropping off sharply outside this window.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Final connection: Click on 'Drug Release Rate' and drag an arrow
over to 'Off-Target Toxicity.'

Here's the key question: When drug release rate goes UP, does
off-target toxicity go UP or DOWN?

If drug is released too quickly — before the nanoparticle reaches the tumor — the freed drug distributes throughout the body causing off-target toxicity similar to conventional chemotherapy. Slower, controlled release that activates preferentially at the tumor site reduces off-target exposure and toxicity.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Look at your model now. You've got 2 negative and 1
positive relationships. 4 arrows total.

When you inject nanoparticles into the bloodstream, they enter a hostile environment: blood proteins immediately coat them, immune cells try to eat them, and the liver and spleen filter them out. Only about 0.7% of injected nanoparticles — less than 1 in 100 — actually reach a tumor. That tiny percentage is still an improvement over conventional chemotherapy. How do you design a particle that survives this gauntlet?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Surface PEGylation −→ Immune Clearance Rate, Immune Clearance Rate −→ Tumor Accumulation, Nanoparticle Size +→ Tumor Accumulation, Drug Release Rate +→ Off-Target Toxicity]

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
• When Nanoparticle Size is HIGH, what happens to the internal components?

Task C: SCENARIO — PEGYLATED PASSIVE TARGETING
• 100nm nanoparticle, dense PEG coating, no targeting ligands, EPR-dependent accumulation
• PREDICT FIRST: What do you predict the percentage of injected dose reaching the tumor will be when relying only on the enhanced permeability and retention effect?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task D: SCENARIO — ACTIVE TARGETING WITH ANTIBODY LIGANDS
• 100nm nanoparticle with PEG coating and tumor-specific antibody ligands
• PREDICT FIRST: What do you predict happens to immune clearance rate when you add targeting ligands that protrude through the stealth PEG coating?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task E: SCENARIO — STIMULUS-RESPONSIVE RELEASE
• pH-sensitive nanoparticles stable at blood pH 7.4 but releasing drug at tumor pH 6.5
• PREDICT FIRST: What do you predict the therapeutic advantage is when drug release is concentrated at the tumor versus distributed throughout the body?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• The enhanced permeability and retention effect is real but modest — tumor blood vessel leakiness allows some nanoparticle accumulation, but the typical 0.7% tumor delivery rate means that 99.3% of the injected dose goes elsewhere, primarily to the liver and spleen where macrophages aggressively clear foreign particles
• PEGylation creates a fundamental trade-off: the stealth coating that protects nanoparticles from immune clearance also reduces their ability to be taken up by target cells, because the same polymer chains that hide the particle from macrophages also physically block targeting ligands from reaching cell surface receptors
• Active targeting with ligands improves the specificity of cellular uptake but does not dramatically increase the total amount of nanoparticles reaching the tumor — the biological barriers of immune clearance and liver sequestration remove most particles before they encounter any target cells
• The therapeutic advantage of nanomedicine over conventional drugs comes less from dramatically improved targeting and more from altered biodistribution, controlled release kinetics, and the ability to deliver drugs that would otherwise be insoluble, unstable, or too toxic in free form

THE ANSWER: Nanoparticle drug delivery represents a significant advance over conventional medicine, but the reality is more nuanced than the vision of molecular missiles finding and destroying individual cancer cells. When nanoparticles are injected into the bloodstream, they immediately face a gauntlet of biological barriers: blood proteins coat them (opsonization), immune cells try to destroy them, and the liver and spleen filter them out. Surface modifications like PEGylation extend circulation time from minutes to hours, and the enhanced permeability and retention effect allows some accumulation in tumors through leaky blood vessels. Adding targeting ligands improves the specificity of cellular uptake once particles reach the tumor. Yet even with the best current designs, only about 0.7% of injected nanoparticles reach a typical tumor — the rest accumulate primarily in the liver. This sounds discouraging until you compare it to conventional chemotherapy, where the drug distributes evenly throughout the body, killing rapidly dividing healthy cells alongside cancer cells. Even modest targeting improvement translates to higher drug concentration at the tumor and lower concentration everywhere else — reducing side effects while maintaining or improving efficacy. The most honest assessment: nanomedicine does not yet deliver drugs to individual cells with missile-like precision, but it significantly improves the therapeutic index by altering how drugs distribute through the body, when they release their payload, and how much damage they cause to healthy tissues.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: PEGylated Passive Targeting. 100nm nanoparticle, dense PEG coating, no targeting ligands, EPR-dependent accumulation.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Active Targeting with Antibody Ligands.
100nm nanoparticle with PEG coating and tumor-specific antibody ligands.

Before you run it — make a prediction. What do you predict happens to immune clearance rate when you add targeting ligands that protrude through the stealth PEG coating?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Stimulus-Responsive Release. pH-sensitive nanoparticles stable at blood pH 7.4 but releasing drug at tumor pH 6.5.
What do you predict the therapeutic advantage is when drug release is concentrated at the tumor versus distributed throughout the body?

Here's what our model reveals: Nanoparticle drug delivery represents a significant advance over conventional medicine, but the reality is more nuanced than the vision of molecular missiles finding and destroying individual cancer cells. When nanoparticles are injected into the bloodstream, they immediately face a gauntlet of biological barriers: blood proteins coat them (opsonization), immune cells try to destroy them, and the liver and spleen filter them out. Surface modifications like PEGylation extend circulation time from minutes to hours, and the enhanced permeability and retention effect allows some accumulation in tumors through leaky blood vessels. Adding targeting ligands improves the specificity of cellular uptake once particles reach the tumor. Yet even with the best current designs, only about 0.7% of injected nanoparticles reach a typical tumor — the rest accumulate primarily in the liver. This sounds discouraging until you compare it to conventional chemotherapy, where the drug distributes evenly throughout the body, killing rapidly dividing healthy cells alongside cancer cells. Even modest targeting improvement translates to higher drug concentration at the tumor and lower concentration everywhere else — reducing side effects while maintaining or improving efficacy. The most honest assessment: nanomedicine does not yet deliver drugs to individual cells with missile-like precision, but it significantly improves the therapeutic index by altering how drugs distribute through the body, when they release their payload, and how much damage they cause to healthy tissues.

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
CONFIGURE CONNECTION CONDITIONS — MODEL REFINEMENT

Your current model treats the Nanoparticle Size → Tumor Accumulation relationship as
unconditional. However, this relationship is scientifically
contingent on Immune Clearance Rate being active. Without this condition,
the simulation produces inaccurate results: Nanoparticle Size drives Tumor Accumulation
even when the prerequisite state is not met.

Task A: CONFIGURE THE CONNECTION CONDITION
   • Select the connection arrow: Nanoparticle Size → Tumor Accumulation
   • Click "Conditions" in the connection toolbar
   • Set the regulator condition: IF Immune Clearance Rate is ON
   • Click "Save Conditions"

Task B: VALIDATE THE CONDITIONAL MODEL
   • Run the simulation with Immune Clearance Rate active and observe
     how Nanoparticle Size's effect on Tumor Accumulation is now gated
   • Toggle Immune Clearance Rate ON/OFF while Nanoparticle Size remains constant
   • Verify that Tumor Accumulation only responds to Nanoparticle Size when the
     condition is satisfied

These conditional relationships capture critical system behavior:
not all connections operate continuously. Some are gated by the
state of other components, creating the non-linear dynamics that
characterize real-world complex systems.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NOW LET'S PLAY AND EXPLORE

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
   • What happens if you turn OFF Nanoparticle Size?
   • What happens if you turn OFF Surface PEGylation?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Blood-Brain Barrier Penetration — The ability of nanoparticles to cross the highly selective blood-brain barrier — a layer of tightly joined endothelial cells that prevents most molecules from entering brain tissue, requiring specialized surface modifications like transferrin receptor-targeting ligands or temporary barrier disruption techniques
   • Combination Payload — Nanoparticles carrying multiple therapeutic agents — such as a chemotherapy drug plus an immune-stimulating molecule — that can be released at different rates to achieve synergistic effects at the tumor site that neither drug achieves alone
   • Theranostic Capability — Nanoparticles that combine therapeutic drug delivery with diagnostic imaging — containing both a drug payload and an imaging contrast agent so that doctors can visualize exactly where the particles accumulate and track treatment response in real time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • Nanoparticles as Drug Carriers — how does this connect to your model?
   • Biological Barriers to Nanoparticle Delivery — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model demonstrate why the 0.7% tumor delivery rate is both disappointing compared to the vision and impressive compared to conventional chemotherapy?
   • Why does the PEGylation dilemma — needing stealth for survival but losing stealth for targeting — represent a fundamental design trade-off that cannot be fully resolved?
   • What does your model reveal about why active targeting improves cellular uptake specificity but does not dramatically increase the total amount of drug reaching the tumor?
   • How would your model change if nanoparticles could be designed that are completely invisible to the immune system?

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

Blood-Brain Barrier Penetration. The ability of nanoparticles to cross the highly selective blood-brain barrier — a layer of tightly joined endothelial cells that prevents most molecules from entering brain tissue, requiring specialized surface modifications like transferrin receptor-targeting ligands or temporary barrier disruption techniques
How would you model that?

Combination Payload. Nanoparticles carrying multiple therapeutic agents — such as a chemotherapy drug plus an immune-stimulating molecule — that can be released at different rates to achieve synergistic effects at the tumor site that neither drug achieves alone
How would you model that?

Theranostic Capability. Nanoparticles that combine therapeutic drug delivery with diagnostic imaging — containing both a drug payload and an imaging contrast agent so that doctors can visualize exactly where the particles accumulate and track treatment response in real time
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

Nanomedicine Scientists design and characterize nanoparticle drug delivery systems at pharmaceutical companies and research institutions, earning $90,000-$170,000/year. Pharmaceutical Engineers scale up nanoparticle manufacturing from laboratory batches to clinical production volumes while maintaining quality control, earning $85,000-$160,000/year. Clinical Pharmacologists evaluate how nanomedicines behave in human patients — tracking biodistribution, efficacy, and side effects — to optimize dosing and treatment protocols, earning $100,000-$200,000/year.

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
Visual: Title slide with nanoparticle navigating bloodstream toward cancer cell
Say: "Chemotherapy works by poisoning every fast-growing cell in your body and hoping the cancer dies before you do. What if we could design a medicine so precise that it finds individual cancer cells, delivers a lethal dose of drug directly to them, and leaves every healthy cell untouched? That is the promise of nanomedicine. The biology makes it much harder than it sounds."
Do: Open with the contrast between chemotherapy's blunt approach and nanomedicine's precision vision. Ask: if you could design the perfect drug delivery system, what properties would it have? List them. Then reveal the biological barriers.
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and vocabulary terms displayed
Say: "Today you are modeling the journey of a drug-carrying nanoparticle from injection to tumor. You will discover why the body treats these particles as invaders, why most never reach their target, and why even imperfect delivery is still a major improvement over flooding the body with toxic drugs."
Do: Have students read objectives. Pre-teach 'opsonization' as the body's foreign particle detection system. Pre-teach the 0.7% median delivery rate and let students react to this number before explaining its context.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: Can we design nanoparticles that deliver medication directly to diseased cells?
Say: "We CAN. We already DO — there are over a dozen FDA-approved nanomedicines. But the precision is not what the headlines suggest. Your model will show you exactly how much drug reaches the tumor, where the rest goes, and why even small improvements in targeting save lives."
Do: Quick-write: Students estimate what percentage of an injected drug dose reaches a tumor. Most will guess 50-90%. Reveal the 0.7% reality and discuss why this is both discouraging and meaningful.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps with nanomedicine context
Say: "We are modeling a system where nanoscale engineering meets the full complexity of human biology — where the immune system is both the obstacle and the inspiration for design."
Do: Preview LEVER steps. Emphasize that this model connects materials science (nanoparticle design) to immunology (immune clearance) to oncology (tumor biology) to pharmacology (drug delivery).
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Seven component cards for nanoparticle drug delivery model
Say: "Seven components. Two you design: nanoparticle size and PEG surface coating. Five that biology determines in response to your design choices. The most important insight: the body does not want foreign particles in the bloodstream, no matter how well you design them."
Do: Guide through components. Show electron microscope images of actual nanoparticles at scale. Discuss why size and PEGylation are the primary design levers. Calculate: at 0.7% delivery, how much drug must be injected for 1 milligram to reach the tumor?
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows showing the immune system as the central bottleneck
Say: "The immune system is the gatekeeper. It decides how long your nanoparticles circulate, which determines how many can reach the tumor. PEG buys time, but nothing buys permanent immunity from immune clearance. Design is about optimizing survival time, not achieving invincibility."
Do: Help students map the immune clearance pathway as the central bottleneck. Calculate circulation half-life effects: if half-life is 4 hours, what fraction remains after 12 hours? How does this limit the delivery window?
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Simulation results for passive, active, and stimulus-responsive scenarios
Say: "Three designs, each building on the last. Watch the numbers: how much drug reaches the tumor, how much reaches the liver, and how much stays in circulation."
Do: Students predict tumor accumulation before each scenario. The passive targeting scenario establishes the baseline. The active targeting scenario shows modest improvement. The stimulus-responsive scenario demonstrates how controlled release amplifies the therapeutic advantage of even modest targeting.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key findings about the 0.7% reality and the therapeutic index advantage
Say: "Nanomedicine's real advantage is not targeting precision — it is therapeutic index improvement. Even at 0.7% tumor delivery, the nanoparticle formulation concentrates drug at the tumor relative to the heart, kidneys, and gut, reducing the side effects that limit how much conventional chemotherapy patients can tolerate."
Do: Lead discussion reframing nanomedicine from the targeting precision narrative to the therapeutic index narrative. Compare side effect profiles: conventional doxorubicin causes heart damage, Doxil liposomal formulation does not. Same drug, different distribution, better outcomes.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Nanoparticle drug delivery system design challenge
Say: "A real oncology lab needs your nanoparticle design for a specific cancer. Choose your cancer type, design the particle, and show the numbers."
Do: Groups choose between brain, pancreatic, or melanoma cancer targets and design complete nanoparticle delivery systems. Must specify particle architecture, targeting strategy, release mechanism, predicted biodistribution, and honest comparison to conventional therapy. Present with model evidence.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: Can Nanotechnology Deliver Medicine to Individual Cells?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
Conventional chemotherapy is a blunt instrument: toxic drugs are injected into the bloodstream and distribute throughout the entire body, killing rapidly dividing cells wherever they are found — cancer cells in the tumor, but also hair follicle cells, gut lining cells, and bone marrow cells, causing the devastating side effects that make chemotherapy so brutal. The fundamental problem is targeting: how do you get the drug to the cancer and nowhere else? Nanotechnology offers a potential solution by packaging drugs inside nanoscale carriers designed to navigate biological barriers, evade immune destruction, and concentrate their payload at the tumor site. The vision is compelling. The reality is more complex — and more instructive — than the headlines suggest.

NGSS ALIGNMENT:
HS-LS1-3, HS-PS2-4: Plan and conduct an investigation to provide evidence that feedback mechanisms maintain homeostasis. Use mathematical representations of Newton's Law of Gravitation and Coulomb's Law to describe and predict the gravitational and electrostatic forces between objects.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Planning and Carrying Out Investigations
  Students plan investigations to test how nanoparticle design parameters affect biodistribution and therapeutic efficacy, controlling variables like particle size, surface chemistry, and targeting ligand density.
• Disciplinary Core Idea: LS1.A Structure and Function / PS2.B Types of Interactions
  Students model how nanoparticle surface chemistry determines interactions with biological systems — electrostatic forces, receptor-ligand binding, and protein adsorption — and how these nanoscale interactions determine macroscale therapeutic outcomes.
• Crosscutting Concept: Scale, Proportion, and Quantity
  Students analyze how the nanoscale properties of drug delivery particles — size, surface area, charge — create emergent behaviors at the biological scale that differ fundamentally from bulk material properties, and use quantitative reasoning to evaluate the 0.7% delivery efficiency in context.

PACING GUIDE:
• Step 1 (Locate): 8-10 minutes
• Step 2 (Establish): 8-10 minutes
• Step 3 (Visualize & Evaluate): 10-12 minutes
• Step 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Nanoparticle, Targeting Ligand, Enhanced Permeability and Retention Effect, Opsonization, Controlled Release
□ Prepare Can we design nanoparticles that navigate the human body, find specific diseased cells, and deliver medication directly to them — turning the blunt instrument of chemotherapy into a precision tool discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify seven key components of a nanoparticle drug delivery system: nanoparticle size, surface PEGylation, targeting ligand density, immune clearance rate, tumor accumulation, drug release rate, and off-target toxicity.
• Establish: Students map relationships showing that nanoparticle size and PEGylation are the primary controllable variables determining immune clearance rate, which combined with the EPR effect determines tumor accumulation, while targeting ligands improve cellular uptake specificity and drug release rate determines therapeutic concentration.
• Visualize: Students build a computational model showing the seven-component nanomedicine system with drug biodistribution as the key dependent outcome.
• Evaluate: Students run passive targeting, active targeting, and stimulus-responsive release scenarios to discover the realistic performance envelope of nanoparticle drug delivery and the biological barriers that limit it.
• Revise: Students add blood-brain barrier penetration, combination payload, or theranostic capability to model more advanced nanomedicine applications and their additional design constraints.

BACKGROUND CONTENT:
• Nanoparticles as Drug Carriers:
  Drug-loaded nanoparticles range from 10 to 200 nanometers in diameter — roughly 100 to 1,000 times smaller than a human cell. They can be made from lipids (liposomes, the most clinically successful platform), polymers (PLGA, PLA, chitosan), proteins (albumin), or inorganic materials (gold, silica, iron oxide). The drug is either encapsulated inside the particle, embedded in the particle matrix, or attached to the particle surface. Nanoparticle encapsulation solves several pharmaceutical problems simultaneously: it protects fragile drugs from degradation in the bloodstream, makes insoluble drugs injectable by packaging them in water-compatible carriers, and prevents the drug from interacting with the body until it is released at the intended site. The first FDA-approved nanomedicine — Doxil, a liposomal formulation of doxorubicin — was approved in 1995 and demonstrated that nanoparticle encapsulation could reduce the severe cardiac toxicity of free doxorubicin by altering the drug's biodistribution.

• Biological Barriers to Nanoparticle Delivery:
  The journey from injection site to target cell is an obstacle course. First, blood proteins immediately adsorb onto the nanoparticle surface (the protein corona), changing its biological identity and often marking it for immune destruction. Macrophages in the liver (Kupffer cells) and spleen recognize opsonized particles and engulf them within minutes — this is why 30-99% of most nanoparticle doses end up in the liver. Particles that survive immune clearance must find and enter the target tissue. For tumors, the enhanced permeability and retention (EPR) effect provides a passive mechanism: tumor blood vessels have gaps of 200-800 nanometers (normal vessels have gaps of less than 2 nanometers), allowing appropriately sized nanoparticles to leak into tumor tissue. However, the EPR effect varies enormously between tumor types, between patients, and even within a single tumor. After entering the tumor, particles must penetrate through the dense extracellular matrix to reach cancer cells, bind to or be internalized by the cells, and release their drug cargo at a therapeutic concentration.

• PEGylation and the Stealth Challenge:
  Polyethylene glycol (PEG) coating — PEGylation — revolutionized nanomedicine by creating a hydrophilic brush layer that reduces protein adsorption and immune recognition. PEGylated nanoparticles circulate for hours instead of minutes, dramatically increasing the opportunity for tumor accumulation. However, PEGylation creates a dilemma: the same polymer brush that shields the particle from macrophages also physically blocks targeting ligands from reaching cell surface receptors and can inhibit the cellular uptake needed for drug delivery. Additionally, repeated PEGylated nanoparticle injections can trigger anti-PEG antibodies — the accelerated blood clearance (ABC) phenomenon — where subsequent doses are cleared faster than the first. Researchers are exploring alternatives to PEG including zwitterionic polymers, cell membrane coatings, and CD47 'do not eat me' peptides that mimic the signals human cells use to avoid immune attack.

• The Targeting Reality Check:
  A landmark 2016 meta-analysis by Wilhelm et al. in Nature Reviews Materials analyzed data from over 200 published studies and found that the median percentage of injected nanoparticle dose reaching tumors was only 0.7% — meaning 99.3% of injected nanoparticles went elsewhere. Active targeting (adding ligands) improved this to approximately 0.9% — a statistically significant but practically modest improvement. These numbers shocked the nanomedicine community and sparked intense debate about whether the field's fundamental approach is viable. Defenders note that even 0.7% delivery can be clinically meaningful if it concentrates the drug at the tumor while reducing exposure elsewhere, and that the comparison should be against conventional drugs (which also have low tumor delivery) rather than against the theoretical ideal of 100% targeting. Critics argue that after 30 years and billions of dollars of research, the field needs to fundamentally rethink its approach. The debate continues, and the honest answer is that both sides have valid points.

COMMON MISCONCEPTIONS:
• "Nanoparticles deliver drugs directly to cancer cells like guided missiles"
  Reality: The guided missile metaphor is the most common and most misleading description of nanomedicine. In reality, nanoparticles are more like messages in bottles thrown into a river — most wash up on the wrong shore (the liver), some are destroyed by the current (immune clearance), and a tiny fraction (0.7%) drift to the intended beach (the tumor). Active targeting with ligands improves the chances that particles reaching the tumor enter cancer cells rather than just sitting in the tumor tissue, but it does not dramatically improve the fraction that reaches the tumor in the first place. The model quantitatively demonstrates this: the major loss pathway is immune clearance before tumor arrival, not failure to enter cancer cells after tumor arrival.
  Strategy: Demonstration: Simulate the nanoparticle journey with 1,000 marbles representing nanoparticles. Remove 500 at the liver, 150 at the spleen, 200 for immune clearance, 143 distributed to other organs, and 7 reaching the tumor. This physical demonstration makes the 0.7% delivery rate visceral and memorable.

• "Nanotechnology in medicine is futuristic and decades away from clinical use"
  Reality: Nanomedicine is already here: over a dozen FDA-approved nanoparticle drug formulations are in routine clinical use. Doxil (liposomal doxorubicin) was approved in 1995 — thirty years ago. Abraxane (albumin-bound paclitaxel) is a standard treatment for breast and pancreatic cancer. The mRNA vaccines from Pfizer-BioNTech and Moderna that were administered to billions of people during the COVID-19 pandemic use lipid nanoparticle delivery — making LNPs the most widely administered nanomedicine in history. The model helps students distinguish between current clinical reality (imperfect but useful nanoparticle formulations) and future aspirations (precise single-cell targeting).
  Strategy: Timeline activity: Create a timeline of FDA-approved nanomedicines from 1995 to present, showing how the technology has evolved from simple liposomes to complex targeted and stimulus-responsive systems, and how the COVID mRNA vaccines brought nanoparticle technology to billions of people.

• "Bigger nanoparticles can carry more drug so they must be better"
  Reality: Larger nanoparticles do have higher drug loading capacity, but size affects every biological interaction the particle encounters. Particles larger than 200 nanometers cannot exploit the EPR effect because they do not fit through tumor blood vessel gaps. Particles larger than 150 nanometers are cleared more rapidly by the liver and spleen. Particles larger than 5,000 nanometers can block capillaries, causing potentially fatal embolism. The optimal size for cancer nanomedicine is typically 50-150 nanometers — a compromise between drug loading, tumor penetration, immune evasion, and tissue distribution. The model demonstrates this nonlinear size-performance relationship and shows why the optimal size is a narrow window rather than simply bigger is better.
  Strategy: Graphing exercise: Plot tumor accumulation versus nanoparticle size using published data. Students observe the bell-shaped curve with a peak around 100 nanometers and discuss why both very small and very large particles fail to accumulate effectively.

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
Big Question: Can we design nanoparticles that navigate the human body, find specific diseased cells, and deliver medication directly to them — turning the blunt instrument of chemotherapy into a precision tool?
Answer: Nanoparticle drug delivery represents a significant advance over conventional medicine, but the reality is more nuanced than the vision of molecular missiles finding and destroying individual cancer cells. When nanoparticles are injected into the bloodstream, they immediately face a gauntlet of biological barriers: blood proteins coat them (opsonization), immune cells try to destroy them, and the liver and spleen filter them out. Surface modifications like PEGylation extend circulation time from minutes to hours, and the enhanced permeability and retention effect allows some accumulation in tumors through leaky blood vessels. Adding targeting ligands improves the specificity of cellular uptake once particles reach the tumor. Yet even with the best current designs, only about 0.7% of injected nanoparticles reach a typical tumor — the rest accumulate primarily in the liver. This sounds discouraging until you compare it to conventional chemotherapy, where the drug distributes evenly throughout the body, killing rapidly dividing healthy cells alongside cancer cells. Even modest targeting improvement translates to higher drug concentration at the tumor and lower concentration everywhere else — reducing side effects while maintaining or improving efficacy. The most honest assessment: nanomedicine does not yet deliver drugs to individual cells with missile-like precision, but it significantly improves the therapeutic index by altering how drugs distribute through the body, when they release their payload, and how much damage they cause to healthy tissues.

Simulation Answers:
• PEGylated Passive Targeting Scenario: With 100-nanometer PEGylated nanoparticles and no targeting ligands, the model shows a circulation half-life of approximately 4-8 hours, during which particles passively accumulate in tumors through the EPR effect. Tumor accumulation reaches approximately 0.5-1.0% of the injected dose over 24 hours. The liver captures 30-50% of the dose despite PEGylation, and the spleen captures an additional 5-15%. The model demonstrates that passive targeting through the EPR effect provides measurable but modest tumor accumulation, and that the majority of nanoparticles are sequestered by the mononuclear phagocyte system regardless of stealth coating. Compared to free drug (which distributes evenly based on blood flow), the nanoparticle formulation achieves approximately 5-10 times higher drug concentration at the tumor relative to the heart.
• Active Targeting with Antibody Ligands Scenario: Adding targeting ligands increases nanoparticle binding to and internalization by target cancer cells once particles reach the tumor. However, the total percentage of particles reaching the tumor increases only modestly — from approximately 0.7% to approximately 0.9% — because the major loss pathway (immune clearance before reaching the tumor) is not affected by targeting ligands. Furthermore, protruding ligands partially compromise the PEG stealth layer, slightly accelerating immune clearance. The net effect: better drug delivery per particle that reaches the tumor, but slightly fewer particles reaching the tumor. The model reveals that active targeting improves the quality but not dramatically the quantity of tumor-delivered drug.
• Stimulus-Responsive Release Scenario: pH-responsive nanoparticles designed to release drug at tumor pH (6.5-6.8) while remaining stable at blood pH (7.4) show the highest therapeutic advantage. Even though tumor accumulation remains at 0.7-1.0%, the drug is released preferentially in the tumor microenvironment rather than during circulation. This concentrates the therapeutic effect at the target while minimizing drug exposure in healthy tissues that maintain normal pH. The model shows that controlled release amplifies the therapeutic advantage of even modest targeting — it is not how much nanoparticle reaches the tumor but how much active drug is released there that determines efficacy.

Reflection Exemplars:
• Q: Why is the 0.7% tumor delivery rate both discouraging and clinically meaningful?
  A: The 0.7% median delivery rate means that for every 100 nanoparticles injected, fewer than 1 reaches the tumor — this seems like a failing technology. However, the comparison must be made against the alternative. Conventional chemotherapy drugs distribute throughout the body based on blood flow, with tumors receiving approximately the same concentration as every other tissue. If a tumor receives 2% of body blood flow, it gets 2% of the drug — but so does every other organ. A nanoparticle that delivers 0.7% of its dose to a tumor that constitutes 0.01% of body mass achieves a 70-fold concentration advantage over free drug. Furthermore, the nanoparticle reformulation reduces drug exposure to dose-limiting organs like the heart, allowing higher total doses. The model shows that nanomedicine's value is not in achieving perfect targeting but in shifting the distribution ratio between tumor and sensitive organs — improving the therapeutic index enough to save lives.
• Q: Why is the PEGylation dilemma a fundamental design constraint rather than a solvable engineering problem?
  A: PEGylation works by creating a hydrophilic polymer brush that sterically blocks protein adsorption — the same mechanism that prevents macrophage recognition also physically prevents targeting ligands from extending far enough to reach cell surface receptors and blocks the electrostatic and hydrophobic interactions needed for cellular uptake. Reducing PEG density to improve targeting re-exposes the particle to immune clearance. This is not a problem of insufficient engineering but a fundamental physical conflict: the molecular brush must be dense enough to block one type of molecular interaction (immune recognition) while permitting another (target cell binding) that occurs at the same spatial scale through similar molecular forces. Current solutions — cleavable PEG that detaches at the tumor site, PEG with different lengths to create ligand accessibility windows, and alternative stealth coatings — all represent compromises rather than true solutions. The model demonstrates this trade-off quantitatively: increasing PEGylation always improves circulation but always decreases cellular uptake.

STEM CHALLENGE GUIDANCE:
Title: Design a Nanoparticle Drug Delivery System
Mission: Design a nanoparticle drug delivery system for a specific cancer type, addressing particle design, targeting strategy, release mechanism, and predicted therapeutic advantage over conventional chemotherapy.
Scenario: An oncology research lab has challenged your team to design a nanoparticle drug delivery system for one of three cancer types: brain cancer (requires crossing the blood-brain barrier), pancreatic cancer (dense stromal tissue that blocks nanoparticle penetration), or melanoma (accessible tumors but high metastatic spread). Each cancer presents unique delivery challenges that your nanoparticle design must address. You must specify particle size, surface chemistry, targeting ligand, drug payload, release mechanism, and predicted biodistribution — and honestly assess how much improvement your design offers over conventional treatment.
Introduction: Present the challenge: An oncology research lab is developing nanoparticle drug delivery systems for three difficult-to-treat cancers: (1) glioblastoma brain cancer (requires crossing the blood-brain barrier), (2) pancreatic cancer (dense stromal tissue blocks nanoparticle penetration), or (3) metastatic melanoma (widely distributed small tumors throughout the body). Your team must design a complete nanoparticle system specifying core material, size, surface chemistry, targeting ligand, drug payload, release mechanism, predicted biodistribution, and therapeutic advantage over conventional chemotherapy — with honest quantitative assessment of limitations.

Key Concepts:
• Therapeutic Index: The ratio of drug concentration that causes therapeutic effect to the concentration that causes toxic side effects. A drug with a narrow therapeutic index (like doxorubicin) has a small safety margin — the dose that kills cancer is close to the dose that kills the patient. Nanoparticle delivery improves the therapeutic index by concentrating drug at the tumor while reducing exposure to dose-limiting organs.
• Protein Corona: When nanoparticles enter blood, hundreds of different proteins adsorb to the surface within seconds, forming a 'corona' that changes the particle's biological identity. The protein corona — not the engineered surface — is what immune cells actually see. Understanding and controlling corona formation is critical because it determines immune clearance rate, cellular uptake, and ultimately biodistribution.
• Tumor Heterogeneity: No two tumors are identical, and even within a single tumor, blood vessel density, leakiness, pH, and receptor expression vary enormously from region to region. This means nanoparticle delivery efficiency varies between patients and between different areas of the same tumor, making clinical outcomes less predictable than laboratory models suggest.

Evaluation Rubric:
• Expert (4): Design includes specific material selection with biocompatibility rationale, size optimization within the EPR-active range, surface chemistry addressing the PEGylation dilemma, cancer-specific targeting ligand, release mechanism matched to tumor microenvironment, quantitative biodistribution prediction with model evidence, and honest comparison to conventional therapy including limitations
• Proficient (3): Design addresses particle architecture, targeting strategy, and release mechanism with model evidence, and considers immune clearance and realistic delivery rates
• Developing (2): Design describes nanoparticle delivery concept but lacks quantitative biodistribution analysis or does not address immune clearance barriers
• Beginning (1): Design is incomplete, assumes most nanoparticles reach the tumor, or does not address biological barriers to delivery

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a nanoparticle platform comparison table showing liposomes (size: 80-200nm, drug loading: 5-20%, FDA approved: yes), polymeric NPs (size: 50-300nm, drug loading: 10-30%, FDA approved: some), gold NPs (size: 10-100nm, drug loading: surface only, FDA approved: none yet), and iron oxide NPs (size: 10-50nm, drug loading: low, FDA approved: for imaging) so students can evaluate trade-offs
  • Use a biodistribution visualization: show a body outline where the injected dose distributes to liver (30-50%), spleen (5-15%), tumor (0.7%), blood (declining over time), and other organs — making the delivery challenge visually concrete
  • Sentence frames: 'Our nanoparticle design uses a __ core of __ nanometers with __ surface coating and __ targeting ligand, which we predict will achieve __% tumor delivery and reduce off-target toxicity by __% compared to free drug because __'

Extensions (Advanced Learners):
  • Research the FDA-approved nanomedicines currently in clinical use — Doxil, Abraxane, Onivyde, and the mRNA-LNP COVID vaccines — and analyze what design features made them successful using your model framework
  • Investigate the controversy sparked by the Wilhelm et al. 2016 meta-analysis showing 0.7% median tumor delivery — what are the strongest arguments on both sides of the debate about nanomedicine's fundamental viability?
  • Design a theranostic nanoparticle that combines drug delivery with real-time imaging to allow doctors to visualize exactly where the particles accumulate and adjust treatment accordingly — specify the imaging modality, drug payload, and how the dual-function design affects particle size and performance

Cross-Curricular Connections:
  • Math: A nanoparticle system has a circulation half-life of 6 hours and a tumor accumulation rate of 0.15% of circulating dose per hour. Using exponential decay for the circulating dose and integration for cumulative tumor accumulation, calculate the total tumor delivery after 24 hours. Compare this to the tumor's share of cardiac output (approximately 2%) to quantify the targeting advantage.
  • ELA: Write a patient education document explaining nanoparticle drug delivery for cancer treatment. The patient has been offered enrollment in a clinical trial comparing conventional chemotherapy to a nanoparticle formulation of the same drug. Present the science accurately without overpromising, address the realistic benefits and limitations, and help the patient make an informed decision.
  • Social Studies: Analyze the global equity implications of nanomedicine: if nanoparticle cancer treatments cost 10-50 times more than conventional chemotherapy, who has access? Research how nanomedicine pricing compares to conventional treatment in the US, Europe, and low-income countries, and propose policy solutions to ensure equitable access to advanced therapies.

CAST ALIGNMENT:
• Model how nanoparticle size, PEGylation density, and targeting ligand selection interact to determine the percentage of injected dose reaching the target tumor versus off-target organs
• Analyze the relationship between immune clearance rate, circulation half-life, and the window of opportunity for nanoparticles to accumulate at tumor sites through the enhanced permeability and retention effect
• Evaluate the therapeutic advantage of targeted nanoparticle drug delivery over conventional chemotherapy using quantitative comparison of drug concentration at the tumor versus healthy tissue

CAST-Style Assessment Questions:
• Multiple Choice: A patient receives an injection of drug-loaded nanoparticles with a circulation half-life of 4 hours. After 12 hours (three half-lives), what percentage of the original nanoparticle dose remains in circulation, and if the tumor accumulation rate is 0.1% of circulating dose per hour, what is the approximate total tumor accumulation over this period?
• Constructed Response: Using evidence from your model, explain the PEGylation dilemma in nanoparticle design: why dense PEG coating is necessary for survival in the bloodstream but counterproductive for drug delivery at the target site. Propose and evaluate one design strategy to resolve this trade-off, referencing at least two model variables in your response.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: Can Nanotechnology Deliver Medicine to Individual Cells?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. What do you already know about how cancer is treated with chemotherapy, and why does chemotherapy cause side effects in healthy parts of the body?

   _________________________________________________________

   _________________________________________________________

2. If you could design a medicine that only affected cancer cells and left healthy cells alone, what properties would it need to have?

   _________________________________________________________

   _________________________________________________________

3. Draw a diagram showing how you think a drug-carrying nanoparticle could find and deliver medicine to a specific cancer cell in the body.

   [DRAWING BOX]

4. What is the difference between a drug that spreads evenly throughout the body versus one that concentrates at the site of disease?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Nanoparticle                  
___ Targeting Ligand              
___ Enhanced Permeability and Retention Effect
___ Opsonization                  
___ Controlled Release            

A. A particle between 1 and 100 nanometers in diameter — thousands of times smaller than a human cell — engineered to carry drug molecules, imaging agents, or genetic material through the body to specific target sites, exploiting size-dependent properties that emerge at the nanoscale
B. A molecule attached to the nanoparticle surface that recognizes and binds to a specific receptor protein found on the surface of target cells — functioning as a molecular address label that directs the nanoparticle to diseased cells while passing by healthy ones
C. The phenomenon by which nanoparticles 20-200 nanometers in diameter preferentially accumulate in tumor tissue because tumor blood vessels are leaky with gaps of 200-800 nanometers, allowing nanoparticles to pass through, while the tumor's poor lymphatic drainage prevents them from being cleared — passive targeting that requires no specific ligand
D. The process by which blood proteins coat the nanoparticle surface, marking it for recognition and destruction by immune cells called macrophages — the body's first-line defense against foreign particles, which clears most unmodified nanoparticles from the bloodstream within minutes
E. The engineered mechanism by which a nanoparticle releases its drug payload at a specific rate and location — triggered by conditions at the target site such as acidic pH inside tumors, specific enzymes produced by cancer cells, or external stimuli like light, heat, or magnetic fields

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

SCENARIO: PEGylated Passive Targeting
Settings: 100nm nanoparticle, dense PEG coating, no targeting ligands, EPR-dependent accumulation
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Active Targeting with Antibody Ligands
Settings: 100nm nanoparticle with PEG coating and tumor-specific antibody ligands
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Stimulus-Responsive Release
Settings: pH-sensitive nanoparticles stable at blood pH 7.4 but releasing drug at tumor pH 6.5
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

1. How does your model demonstrate why the 0.7% tumor delivery rate is both disappointing compared to the vision and impressive compared to conventional chemotherapy?

   _________________________________________________________

   _________________________________________________________

2. Why does the PEGylation dilemma — needing stealth for survival but losing stealth for targeting — represent a fundamental design trade-off that cannot be fully resolved?

   _________________________________________________________

   _________________________________________________________

3. What does your model reveal about why active targeting improves cellular uptake specificity but does not dramatically increase the total amount of drug reaching the tumor?

   _________________________________________________________

   _________________________________________________________

4. How would your model change if nanoparticles could be designed that are completely invisible to the immune system?

   _________________________________________________________

   _________________________________________________________

5. What are the limitations of modeling nanomedicine biodistribution when individual patients' immune systems, tumor vasculature, and blood chemistry vary significantly?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Can we design nanoparticles that navigate the human body, find specific diseased cells, and deliver medication directly to them — turning the blunt instrument of chemotherapy into a precision tool? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Planning and Carrying Out Investigations
   □ Disciplinary Core Idea: LS1.A Structure and Function / PS2.B Types of Interactions
   □ Crosscutting Concept: Scale, Proportion, and Quantity

3. What are the limitations of modeling nanomedicine biodistribution when individual patients' immune systems, tumor vasculature, and blood chemistry vary significantly?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Nanoparticle Drug Delivery System
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design a nanoparticle drug delivery system for a specific cancer type, addressing particle design, targeting strategy, release mechanism, and predicted therapeutic advantage over conventional chemotherapy.

SCENARIO: An oncology research lab has challenged your team to design a nanoparticle drug delivery system for one of three cancer types: brain cancer (requires crossing the blood-brain barrier), pancreatic cancer (dense stromal tissue that blocks nanoparticle penetration), or melanoma (accessible tumors but high metastatic spread). Each cancer presents unique delivery challenges that your nanoparticle design must address. You must specify particle size, surface chemistry, targeting ligand, drug payload, release mechanism, and predicted biodistribution — and honestly assess how much improvement your design offers over conventional treatment.

GUIDING QUESTIONS:
• What nanoparticle size and surface chemistry would maximize circulation time while still allowing accumulation at your target tumor?
• How would you design the drug release mechanism to activate specifically at the tumor site rather than during circulation?
• What percentage of injected dose do you realistically expect to reach the tumor, and how does this compare to conventional chemotherapy distribution?

DESIGN THINKING:
• What material would you choose for the nanoparticle core — lipid, polymer, silica, or metal — and what are the biocompatibility and drug loading trade-offs?

  _________________________________________________________

• What targeting ligand would you select for your specific cancer type and what receptor does it bind on the cancer cell surface?

  _________________________________________________________

• How would you address the PEGylation dilemma — the need for stealth coating versus the need for target cell uptake?

  _________________________________________________________

• What preclinical tests would you propose to evaluate your nanoparticle system's safety and efficacy before human trials?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Design includes specific material selection with biocompatibility rationale, size optimization within the EPR-active range, surface chemistry addressing the PEGylation dilemma, cancer-specific targeting ligand, release mechanism matched to tumor microenvironment, quantitative biodistribution prediction with model evidence, and honest comparison to conventional therapy including limitations
• Proficient (3): Design addresses particle architecture, targeting strategy, and release mechanism with model evidence, and considers immune clearance and realistic delivery rates
• Developing (2): Design describes nanoparticle delivery concept but lacks quantitative biodistribution analysis or does not address immune clearance barriers
• Beginning (1): Design is incomplete, assumes most nanoparticles reach the tumor, or does not address biological barriers to delivery

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CAST-Aligned Pre/Post Assessment

### Administration Instructions

These 5 multiple-choice questions are administered identically as both a pre-assessment (before Activity 1) and a post-assessment (after Activity 4). Score each out of 5. Learning growth = post-score minus pre-score.

Questions follow the California Science Test (CAST) stimulus-response format. Each item is three-dimensional, assessing a Science and Engineering Practice (SEP), Disciplinary Core Idea (DCI), and Crosscutting Concept (CCC) simultaneously, aligned to HS-LS1-3, HS-PS2-4.

---

### Question 1

CAST Alignment: SEP 2.1.1 (Develop and use a model to represent relationships) + DCI LS1.A (Feedback mechanisms maintain homeostasis) + CCC4 (Systems and system models)

A nanotechnology research team develops a drug delivery nanoparticle measuring 80 nanometers in diameter (800 times smaller than a red blood cell). The nanoparticle consists of a lipid bilayer shell encapsulating a chemotherapy drug, with antibodies on its surface that bind specifically to a protein (HER2) overexpressed on breast cancer cells. In cell culture experiments, the targeted nanoparticles deliver 15 times more drug to cancer cells than free drug, while reducing exposure to healthy cells by 90%. However, in mouse models, only 2% of injected nanoparticles actually reach the tumor, with the rest captured by the liver and spleen.

A student's model shows that increasing PEGylation density from 5% to 20% surface coverage extends circulation half-life from 2 to 12 hours but reduces cellular uptake at the tumor by 40%. What does this reveal about the design trade-off?

A. The reduced uptake is caused by the nanoparticle becoming too large
B. The stealth effect of PEG that evades immune cells also reduces the nanoparticle's ability to interact with and enter target tumor cells, creating a fundamental tension between surviving the journey and completing the delivery
C. PEGylation has no effect on tumor cell interactions
D. Higher PEGylation is always better because longer circulation is the only goal

Correct Answer: B

Feedback: The same PEG layer that protects nanoparticles from immune clearance also hinders their interaction with target cells. This 'PEG dilemma' is a central design challenge: stealth for the journey versus accessibility at the destination. If you chose D, this response overgeneralizes without considering the specific mechanisms and evidence presented. This is the 'PEG dilemma': the stealth coating that enables immune evasion also prevents interaction with target cells. The nanoparticle must evade immune cells during transit but engage target cells at the tumor. These requirements are fundamentally in tension. If you chose C, this answer does not account for the key mechanism or relationship the evidence demonstrates. This is the 'PEG dilemma': the stealth coating that enables immune evasion also prevents interaction with target cells. The nanoparticle must evade immune cells during transit but engage target cells at the tumor. These requirements are fundamentally in tension. If you chose A, this choice does not account for the key mechanism or relationship the evidence demonstrates. This is the 'PEG dilemma': the stealth coating that enables immune evasion also prevents interaction with target cells. The nanoparticle must evade immune cells during transit but engage target cells at the tumor. These requirements are fundamentally in tension.
---

### Question 2

CAST Alignment: SEP 2.1.2 (Determine relationships among system components) + DCI LS1.A (Feedback mechanisms maintain homeostasis) + CCC2 (Cause and effect)

A computational model of nanoparticle pharmacokinetics tracks the journey from injection to target cell. After intravenous injection, nanoparticles encounter three major barriers: (1) opsonization, where blood proteins coat the nanoparticle surface, marking it for immune cell capture, (2) vascular escape, where particles must exit blood vessels through gaps in the vessel wall to reach tissue, and (3) tumor penetration, where particles must navigate the dense extracellular matrix surrounding tumor cells. The model shows that each barrier eliminates 80-95% of remaining particles, explaining the low 2% delivery efficiency observed in animal studies.

The model shows that adding targeting ligands increases tumor cell binding by 300% but also increases liver accumulation by 150% because liver cells express low levels of the same receptor. What does this demonstrate about the specificity challenge?

A. Targeting ligands should never be used because they increase off-target accumulation
B. Liver accumulation is beneficial because it helps clear the drug from the body
C. Active targeting improves tumor delivery but is limited by the fact that target receptors are rarely exclusive to tumor cells. Low-level expression on healthy cells creates off-target binding that concentrates the drug in the liver, potentially causing hepatotoxicity
D. The 300% improvement in tumor binding outweighs all other considerations

Correct Answer: C

Feedback: The specificity challenge arises because few receptors are truly unique to tumor cells. Any receptor expressed (even at low levels) on healthy cells will capture targeting nanoparticles, concentrating drug in unintended organs and potentially causing toxicity. If you chose A, this response does not account for the key mechanism or relationship the evidence demonstrates. Targeting ligands improve tumor delivery but expose a specificity limitation: target receptors are rarely tumor-exclusive. Low-level expression on healthy cells, especially in the liver (which filters all blood), creates significant off-target accumulation. The therapeutic index must account for this. If you chose D, this answer overgeneralizes without considering the specific mechanisms and evidence presented. Targeting ligands improve tumor delivery but expose a specificity limitation: target receptors are rarely tumor-exclusive. Low-level expression on healthy cells, especially in the liver (which filters all blood), creates significant off-target accumulation. The therapeutic index must account for this. If you chose B, this choice does not account for the key mechanism or relationship the evidence demonstrates. Targeting ligands improve tumor delivery but expose a specificity limitation: target receptors are rarely tumor-exclusive. Low-level expression on healthy cells, especially in the liver (which filters all blood), creates significant off-target accumulation. The therapeutic index must account for this.
---

### Question 3

CAST Alignment: SEP 2.1.2 (Determine relationships among components) + DCI PS2.B (Electromagnetic forces) + CCC4 (Describe components and interactions)

Scientists compare three nanoparticle designs for drug delivery to brain tumors. Design A uses a 100 nm lipid nanoparticle that cannot cross the blood-brain barrier (BBB). Design B uses a 30 nm gold nanoparticle coated with transferrin protein, which exploits the brain's iron transport system to cross the BBB via receptor-mediated transcytosis, achieving 0.5% brain delivery. Design C uses focused ultrasound to temporarily open the BBB in the tumor region, allowing standard nanoparticles to enter, achieving 5% delivery but with a 48-hour window where the brain is vulnerable to infections and toxins.

A student models nanoparticle size optimization and finds that 100 nm particles have the best balance of EPR-mediated tumor accumulation and immune evasion. Particles of 20 nm accumulate well but are cleared by the kidneys; 200 nm particles avoid kidney clearance but are captured more efficiently by liver macrophages. What principle does this size optimization demonstrate?

A. All nanoparticle sizes perform equally well in the body
B. Size optimization is unnecessary because targeting ligands compensate for any size
C. Larger particles are always better because they carry more drug
D. Nanoparticle size must navigate between two biological barriers: renal filtration (removing particles that are too small) and phagocytic clearance (removing particles that are too large), creating a narrow optimal size window determined by the body's filtration and immune architecture

Correct Answer: D

Feedback: The body imposes size-dependent barriers: kidneys clear small particles, liver macrophages clear large particles. The optimal size window (~60-120 nm) avoids both barriers while exploiting the EPR effect for tumor accumulation. If you chose A, this response overgeneralizes without considering the specific mechanisms and evidence presented. The body's filtration systems create a size window: too small (<30 nm) and kidneys clear them; too large (>200 nm) and macrophages capture them more efficiently. The optimal range (~60-120 nm) threads between these biological barriers while maximizing tumor accumulation via the EPR effect. If you chose C, this answer overgeneralizes without considering the specific mechanisms and evidence presented. The body's filtration systems create a size window: too small (<30 nm) and kidneys clear them; too large (>200 nm) and macrophages capture them more efficiently. The optimal range (~60-120 nm) threads between these biological barriers while maximizing tumor accumulation via the EPR effect. If you chose B, this choice does not account for the key mechanism or relationship the evidence demonstrates. The body's filtration systems create a size window: too small (<30 nm) and kidneys clear them; too large (>200 nm) and macrophages capture them more efficiently. The optimal range (~60-120 nm) threads between these biological barriers while maximizing tumor accumulation via the EPR effect.
---

### Question 4

CAST Alignment: SEP 2.1.4 (Represent mechanisms to explain/predict events) + DCI LS1.A (Feedback mechanisms maintain homeostasis) + CCC7 (Stability and change)

A pharmacology team studies how nanoparticle size affects distribution in the body. Experiments with fluorescent nanoparticles of different diameters show distinct biodistribution patterns: particles smaller than 10 nm are rapidly cleared by the kidneys (half-life: 45 minutes), particles between 10-100 nm circulate for hours and accumulate preferentially in tumors through the enhanced permeability and retention (EPR) effect, and particles larger than 200 nm are captured by the liver and spleen within minutes. The computational model reveals an optimal size window of 50-100 nm that balances long circulation time with the ability to exit blood vessels at tumor sites.

The model reveals that drug release rate must be tuned to a specific window: too fast and the drug is lost during circulation before reaching the tumor; too slow and therapeutic concentrations are never achieved at the target. A student proposes using the fastest possible release rate. Why is this approach counterproductive?

A. With fast release, most of the drug payload leaks out during the hours of circulation before the nanoparticle reaches the tumor, resulting in systemic drug exposure (conventional chemotherapy's side effect profile) rather than targeted delivery
B. Release rate has no effect on therapeutic outcomes
C. Fast release makes nanoparticles easier for the immune system to detect
D. Fast release increases the drug's potency at the tumor

Correct Answer: A

Feedback: If the drug releases during transit, the nanoparticle delivers free drug throughout the body rather than concentrated drug at the tumor. This negates the entire advantage of targeted delivery and reverts to the side-effect profile of conventional chemotherapy. If you chose D, this response does not account for the key mechanism or relationship the evidence demonstrates. Premature drug release defeats the purpose of nanoparticle delivery. If the drug leaks out during the hours of bloodstream circulation, it distributes systemically, just like conventional chemotherapy. The nanoparticle must retain its payload until it reaches the tumor. If you chose B, this answer does not account for the key mechanism or relationship the evidence demonstrates. Premature drug release defeats the purpose of nanoparticle delivery. If the drug leaks out during the hours of bloodstream circulation, it distributes systemically, just like conventional chemotherapy. The nanoparticle must retain its payload until it reaches the tumor. If you chose C, this choice does not account for the key mechanism or relationship the evidence demonstrates. Premature drug release defeats the purpose of nanoparticle delivery. If the drug leaks out during the hours of bloodstream circulation, it distributes systemically, just like conventional chemotherapy. The nanoparticle must retain its payload until it reaches the tumor.
---

### Question 5

CAST Alignment: SEP 2.1.4 (Represent mechanisms to predict a scientific event) + DCI PS2.B (Electromagnetic forces) + CCC4 (Describe system components and interactions)

A pharmaceutical company evaluates whether to pursue nanoparticle-based cancer therapy or conventional chemotherapy for a new drug. The nanoparticle formulation reduces side effects by 70% and increases tumor drug concentration by 8-fold, but manufacturing costs are 20 times higher than the free drug formulation, and the nanoparticle's shelf life is 6 months versus 5 years for the conventional formulation. The systems model compares total healthcare costs (including hospitalization from side effects), patient quality of life, treatment efficacy, and manufacturing scalability across both approaches over a 10-year market projection.

Based on the nanoparticle drug delivery model, which conclusion about the 0.7% tumor delivery rate is best supported by the simulation data?

A. Despite the low percentage, the 0.7% delivery rate still represents a significant improvement over conventional chemotherapy because nanoparticles concentrate drug at the tumor while reducing exposure to healthy tissues. However, the model demonstrates that each biological barrier (opsonization, liver clearance, EPR variability, cellular uptake) multiplicatively reduces delivery, and meaningful improvement requires addressing multiple barriers simultaneously rather than optimizing any single parameter
B. The 0.7% rate will naturally improve to 50% with continued use
C. The 0.7% rate proves that nanoparticle drug delivery is a failed technology
D. Tumor delivery percentage is irrelevant to therapeutic efficacy

Correct Answer: A

Feedback: The barriers are multiplicative: if each of 5 barriers removes 50% of particles, only 0.5^5 = 3% survive. Improving one barrier from 50% to 25% loss yields only a modest gain. Meaningful improvement requires addressing multiple barriers simultaneously. If you chose C, this response does not account for the key mechanism or relationship the evidence demonstrates. The delivery barriers are multiplicative, not additive. Each biological obstacle removes a fraction of particles, and the fractions compound. This means optimizing a single barrier provides limited benefit; only simultaneous improvement across multiple barriers can substantially increase tumor delivery. If you chose B, this answer overgeneralizes without considering the specific mechanisms and evidence presented. The delivery barriers are multiplicative, not additive. Each biological obstacle removes a fraction of particles, and the fractions compound. This means optimizing a single barrier provides limited benefit; only simultaneous improvement across multiple barriers can substantially increase tumor delivery. If you chose D, this choice dismisses relevant factors that the evidence directly addresses. The delivery barriers are multiplicative, not additive. Each biological obstacle removes a fraction of particles, and the fractions compound. This means optimizing a single barrier provides limited benefit; only simultaneous improvement across multiple barriers can substantially increase tumor delivery.
---

### Answer Key

Question 1: B (Cognitive Level: Identify -- SEP 2.1.1, DCI HS-LS1-3, CCC4)
Question 2: C (Cognitive Level: Reason -- SEP 2.1.2, DCI HS-LS1-3, CCC2)
Question 3: D (Cognitive Level: Reason -- SEP 2.1.2, DCI HS-LS1-3, CCC4)
Question 4: A (Cognitive Level: Reason + Evidence -- SEP 2.1.4, DCI HS-PS2-4, CCC7)
Question 5: A (Cognitive Level: Predict + Apply -- SEP 2.1.4, DCI HS-PS2-4, CCC4)

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-11/G11L3-L09/G11L3-L09-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-11/G11L3-L09/G11L3-L09-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-11/G11L3-L09/G11L3-L09-Student-Presentation.pptx] |
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