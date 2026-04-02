# Lesson: Can We 3D-Print a Human Organ?

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G11L3-L08 |
| **Grade** | 11th Grade — Level 3: Systems Innovation Lab |
| **Lesson Name** | Can We 3D-Print a Human Organ? |
| **Status** | Template |

---

## Platform

### Title
**Can We 3D-Print a Human Organ? — Modeling Bioprinting, Tissue Engineering, and Transplant Viability**

### Overview
Over 100,000 people in the United States are on the organ transplant waiting list right now, and 17 of them die every day because a matching donor organ is not available in time. This shortage exists because organ donation depends on tragic circumstances — healthy organs from recently deceased individuals whose families consent to donation — and the demand far exceeds the supply. Bioprinting offers a revolutionary alternative: manufacturing replacement organs from the patient's own cells, eliminating both the donor shortage and the risk of immune rejection. The technology has made remarkable progress in simple tissues, but the leap to complex organs faces fundamental biological barriers that no engineering solution has yet overcome. Students investigate the driving question: Can we engineer living human organs from a patient's own cells — and could bioprinting end the transplant shortage that kills 17 people every day? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of a bioprinter depositing layers of living tissue with a translucent organ scaffold visible under blue-violet light in a sterile lab environment, featuring a diverse multicultural group with Black people centered of 16-17 year old students observing the bioprinting process through glass panels with expressions of fascination]

### Grade
11th Grade — Level 3: Systems Innovation Lab

### NGSS Standard
**HS-LS1-2, HS-ETS1-2**: Develop and use a model to illustrate the hierarchical organization of interacting systems that provide specific functions within multicellular organisms. Design a solution to a complex real-world problem by breaking it down into smaller, more manageable problems that can be solved through engineering.

### Learning Objectives
- Model how bioprinters deposit layers of living cells within biocompatible scaffolds to construct three-dimensional tissue structures with controlled architecture
- Analyze the relationship between cell viability, print resolution, and vascularization in determining whether bioprinted tissue can survive and function after implantation
- Evaluate the engineering trade-offs between printing speed, structural complexity, and cell survival rate when scaling from simple tissue patches to entire organs
- Predict how nutrient diffusion limits, immune compatibility, and maturation time constrain the maximum size and complexity of bioprinted constructs

### Component List (Starting Model: 7 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Print Resolution | External | The minimum feature size the bioprinter can create — measured in micrometers, determining how precisely cells and materials can be positioned to replicate the complex microarchitecture of native tissue, including capillary-scale blood vessel channels |
| Cell Viability Rate | Internal | The percentage of cells that survive the printing process — affected by shear stress in the print nozzle, temperature fluctuations, UV exposure during crosslinking, and time outside physiological conditions — typically 70-95% for current systems |
| Vascularization Depth | Internal | The maximum thickness of tissue that can be sustained by the engineered blood vessel network — without adequate vascularization, the interior of thick constructs becomes necrotic within hours as cells exhaust local oxygen and nutrients |
| Scaffold Degradation Rate | Internal | The speed at which the supporting scaffold material dissolves or is absorbed — must match the rate at which cells produce their own structural matrix, because too-fast degradation causes collapse while too-slow degradation prevents tissue remodeling |
| Nutrient Diffusion Limit | External | The maximum distance from a blood vessel or media surface at which cells can receive sufficient oxygen and nutrients to survive — approximately 200 micrometers in most tissues, creating a hard physical constraint on construct thickness without vascularization |
| Immune Compatibility | Internal | The degree to which the bioprinted tissue avoids triggering the recipient's immune system — using the patient's own cells (autologous) eliminates rejection but requires weeks of cell culture, while donor cells or stem cell lines offer faster availability but risk immune attack |
| Functional Maturation | Internal | The degree to which bioprinted tissue develops the specialized functions of native tissue — a bioprinted heart patch must not only survive but contract rhythmically, conduct electrical impulses, and integrate mechanically with the surrounding heart muscle |

### Research for Lesson
- How Bioprinting Works — reference materials and textbook resources
- The Vascularization Challenge — reference materials and textbook resources
- Cell Sourcing and Immune Compatibility — reference materials and textbook resources
- Current Achievements and Future Trajectory — reference materials and textbook resources

---

## Step 1: LOCATE — Build Your System

### Text Editor

```
CAN WE 3D-PRINT A HUMAN ORGAN?

Modeling Bioprinting, Tissue Engineering, and Transplant Viability.
Can we engineer living human organs from a patient's own cells — and could bioprinting end the transplant shortage that kills 17 people every day?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Print Resolution" — the minimum feature size the bioprinter can create — measured in micrometers
  ○ Click "Nutrient Diffusion Limit" — the maximum distance from a blood vessel or media surface at which cells can receive sufficient oxygen and nutrients to survive — approximately 200 micrometers in most tissues
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Cell Viability Rate" — the percentage of cells that survive the printing process — affected by shear stress in the print nozzle
  ○ Click "Vascularization Depth" — the maximum thickness of tissue that can be sustained by the engineered blood vessel network — without adequate vascularization
  ○ Click "Scaffold Degradation Rate" — the speed at which the supporting scaffold material dissolves or is absorbed — must match the rate at which cells produce their own structural matrix
  ○ Click "Immune Compatibility" — the degree to which the bioprinted tissue avoids triggering the recipient's immune system — using the patient's own cells (autologous) eliminates rejection but requires weeks of cell culture
  ○ Click "Functional Maturation" — the degree to which bioprinted tissue develops the specialized functions of native tissue — a bioprinted heart patch must not only survive but contract rhythmically

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
"Can we engineer living human organs from a patient's own cells — and could bioprinting end the transplant shortage that kills 17 people every day?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Print Resolution' — that's external. The minimum feature size the bioprinter can create — measured in micrometers.
Click on 'Cell Viability Rate' — that's internal. The percentage of cells that survive the printing process — affected by shear stress in the print nozzle.
Click on 'Vascularization Depth' — that's internal. The maximum thickness of tissue that can be sustained by the engineered blood vessel network — without adequate vascularization.
Click on 'Scaffold Degradation Rate' — that's internal. The speed at which the supporting scaffold material dissolves or is absorbed — must match the rate at which cells produce their own structural matrix.
Click on 'Nutrient Diffusion Limit' — that's external. The maximum distance from a blood vessel or media surface at which cells can receive sufficient oxygen and nutrients to survive — approximately 200 micrometers in most tissues.
Click on 'Immune Compatibility' — that's internal. The degree to which the bioprinted tissue avoids triggering the recipient's immune system — using the patient's own cells (autologous) eliminates rejection but requires weeks of cell culture.
Click on 'Functional Maturation' — that's internal. The degree to which bioprinted tissue develops the specialized functions of native tissue — a bioprinted heart patch must not only survive but contract rhythmically.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Print Resolution is external because it represents the engineering specification of the bioprinting hardware — a fixed capability of the printer being used, not determined by the biology of the tissue being printed. Nutrient Diffusion Limit is external because it represents a physical constant determined by the physics of molecular diffusion through tissue — approximately 200 micrometers for oxygen in most tissues, independent of any design choice. The remaining five components are internal: Cell Viability Rate depends on printing conditions and bioink properties, Vascularization Depth depends on both engineered vessel channels and biological self-assembly, Scaffold Degradation Rate is a material property that interacts with biological remodeling, Immune Compatibility depends on cell source and patient biology, and Functional Maturation depends on cell behavior, growth factor signaling, and mechanical conditioning during incubation.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next step, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 7 components sorted: Print Resolution, Nutrient Diffusion Limit (External), Cell Viability Rate, Vascularization Depth, Scaffold Degradation Rate, Immune Compatibility, Functional Maturation (Internal)]

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
• Click on "Print Resolution" and drag an arrow to "Cell Viability Rate"
• Click on "Vascularization Depth" and drag an arrow to "Functional Maturation"
• Click on "Nutrient Diffusion Limit" and drag an arrow to "Vascularization Depth"
• Click on "Scaffold Degradation Rate" and drag an arrow to "Functional Maturation"

Task C: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Print Resolution → Cell Viability Rate = NEGATIVE (−)
    Higher print resolution initially improves viability by creating more precise cell arrangements and better nutrient channel geometry. However, achieving very high resolution requires smaller nozzle diameters that increase shear stress on cells, eventually reducing viability. The relationship peaks at the optimal balance between structural precision and mechanical cell damage.

  ○ Vascularization Depth → Functional Maturation = POSITIVE (+)
    Greater vascularization depth means more cells throughout the construct receive adequate oxygen and nutrients, enabling them to survive, proliferate, and develop the specialized functions of mature tissue. Without sufficient vascularization, cells in the interior die before they can mature.

  ○ Nutrient Diffusion Limit → Vascularization Depth = NEGATIVE (−)
    The nutrient diffusion limit constrains vascularization depth because it sets the maximum distance between blood vessels — if channels are spaced farther apart than twice the diffusion limit, cells between them die. This constraint forces denser vascular networks as construct thickness increases.

  ○ Scaffold Degradation Rate → Functional Maturation = POSITIVE (+)
    If scaffold degradation is too fast, the construct loses mechanical support before cells produce sufficient extracellular matrix, causing collapse. If too slow, the persistent scaffold physically prevents cell migration, matrix deposition, and tissue remodeling. Only when degradation rate matches maturation rate does the tissue successfully transition from scaffold-dependent to self-supporting.

Task D: CHECK YOUR MODEL
• You should have 4 arrows total
• 2 negative relationship(s), 2 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: The 200-micrometer nutrient diffusion limit means that every cell in your body must be within 200 micrometers — about the width of two human hairs — of a blood capillary. A human kidney contains over 100 miles of blood vessels reaching every one of its million nephrons. How do you 3D-print a blood vessel network that dense and that complex?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Print Resolution' and drag an arrow
over to 'Cell Viability Rate.'

Here's the key question: When print resolution goes UP, does
cell viability rate go UP or DOWN?

Higher print resolution initially improves viability by creating more precise cell arrangements and better nutrient channel geometry. However, achieving very high resolution requires smaller nozzle diameters that increase shear stress on cells, eventually reducing viability. The relationship peaks at the optimal balance between structural precision and mechanical cell damage.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Next connection: Click on 'Vascularization Depth' and drag an arrow
over to 'Functional Maturation.'

Here's the key question: When vascularization depth goes UP, does
functional maturation go UP or DOWN?

Greater vascularization depth means more cells throughout the construct receive adequate oxygen and nutrients, enabling them to survive, proliferate, and develop the specialized functions of mature tissue. Without sufficient vascularization, cells in the interior die before they can mature.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'Nutrient Diffusion Limit' and drag an arrow
over to 'Vascularization Depth.'

Here's the key question: When nutrient diffusion limit goes UP, does
vascularization depth go UP or DOWN?

The nutrient diffusion limit constrains vascularization depth because it sets the maximum distance between blood vessels — if channels are spaced farther apart than twice the diffusion limit, cells between them die. This constraint forces denser vascular networks as construct thickness increases.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Scaffold Degradation Rate' and drag an arrow
over to 'Functional Maturation.'

Here's the key question: When scaffold degradation rate goes UP, does
functional maturation go UP or DOWN?

If scaffold degradation is too fast, the construct loses mechanical support before cells produce sufficient extracellular matrix, causing collapse. If too slow, the persistent scaffold physically prevents cell migration, matrix deposition, and tissue remodeling. Only when degradation rate matches maturation rate does the tissue successfully transition from scaffold-dependent to self-supporting.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Look at your model now. You've got 2 negative and 2
positive relationships. 4 arrows total.

The 200-micrometer nutrient diffusion limit means that every cell in your body must be within 200 micrometers — about the width of two human hairs — of a blood capillary. A human kidney contains over 100 miles of blood vessels reaching every one of its million nephrons. How do you 3D-print a blood vessel network that dense and that complex?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Print Resolution −→ Cell Viability Rate, Vascularization Depth +→ Functional Maturation, Nutrient Diffusion Limit −→ Vascularization Depth, Scaffold Degradation Rate +→ Functional Maturation]

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
• When Print Resolution is HIGH, what happens to the internal components?

Task C: SCENARIO — SKIN PATCH BIOPRINTING
• Moderate resolution, thin construct, no deep vascularization required
• PREDICT FIRST: What do you predict the cell viability rate will be in a tissue that is thin enough for nutrients to diffuse from the surface to all cells?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task D: SCENARIO — CARDIAC PATCH WITH VASCULARIZATION
• 5mm thick cardiac construct requiring internal blood vessel channels
• PREDICT FIRST: What do you predict happens to the cells in the center of the construct if the printed blood vessel channels do not connect to a nutrient supply within hours?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task E: SCENARIO — FULL KIDNEY SCAFFOLD
• Complex organ with millions of functional units and extensive vasculature
• PREDICT FIRST: What do you predict is the primary failure point when attempting to print an organ with the structural complexity of a human kidney?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• The 200-micrometer nutrient diffusion limit is the fundamental constraint that makes organ bioprinting qualitatively different from printing simple tissues — every thick construct must include a functional vascular network, and printing functional blood vessels at capillary scale remains the greatest unsolved challenge
• Cell viability decreases with print time because cells outside physiological conditions accumulate damage — this creates a race between printing speed and cell death that becomes more severe as constructs become larger and more complex
• Scaffold degradation timing must be precisely matched to tissue maturation rate — a mismatch of even a few days can cause either structural collapse or prevented tissue remodeling, and this timing varies unpredictably between patients and cell batches
• The gap between current capability (thin tissue patches, cartilage, simple blood vessels) and the goal (complete transplantable organs) is not incremental — it requires solving vascularization, multi-cell-type coordination, and functional maturation simultaneously at a complexity level thousands of times greater than anything achieved to date

THE ANSWER: Bioprinting constructs living tissue by depositing cells and biomaterials in precise three-dimensional patterns, layer by layer. For thin, relatively simple tissues — skin patches, cartilage, corneas — the technology is approaching clinical viability because these structures are thin enough for nutrients to diffuse from the surface and involve relatively few cell types. Researchers have successfully bioprinted skin grafts that heal burns, cartilage implants that repair joints, and blood vessel segments that carry blood flow. However, printing complex solid organs like kidneys, hearts, and livers requires solving the vascularization problem: every cell must be within 200 micrometers of a blood capillary, which means the printed organ must contain a complete, functional, microscale blood vessel network — something no bioprinter can yet achieve. A human kidney contains over 100 miles of blood vessels feeding a million filtering units composed of dozens of specialized cell types arranged in precise three-dimensional patterns. Current bioprinters can produce structures with channels for major blood vessels, but the capillary-level branching required to sustain thick tissue remains beyond current capability. The most honest answer: we can 3D-print tissues, we are making progress toward organs, but printing a complete transplantable organ is likely decades away — and the primary barrier is not the printer but the vascularization biology.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Skin Patch Bioprinting. Moderate resolution, thin construct, no deep vascularization required.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Cardiac Patch with Vascularization.
5mm thick cardiac construct requiring internal blood vessel channels.

Before you run it — make a prediction. What do you predict happens to the cells in the center of the construct if the printed blood vessel channels do not connect to a nutrient supply within hours?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Full Kidney Scaffold. Complex organ with millions of functional units and extensive vasculature.
What do you predict is the primary failure point when attempting to print an organ with the structural complexity of a human kidney?

Here's what our model reveals: Bioprinting constructs living tissue by depositing cells and biomaterials in precise three-dimensional patterns, layer by layer. For thin, relatively simple tissues — skin patches, cartilage, corneas — the technology is approaching clinical viability because these structures are thin enough for nutrients to diffuse from the surface and involve relatively few cell types. Researchers have successfully bioprinted skin grafts that heal burns, cartilage implants that repair joints, and blood vessel segments that carry blood flow. However, printing complex solid organs like kidneys, hearts, and livers requires solving the vascularization problem: every cell must be within 200 micrometers of a blood capillary, which means the printed organ must contain a complete, functional, microscale blood vessel network — something no bioprinter can yet achieve. A human kidney contains over 100 miles of blood vessels feeding a million filtering units composed of dozens of specialized cell types arranged in precise three-dimensional patterns. Current bioprinters can produce structures with channels for major blood vessels, but the capillary-level branching required to sustain thick tissue remains beyond current capability. The most honest answer: we can 3D-print tissues, we are making progress toward organs, but printing a complete transplantable organ is likely decades away — and the primary barrier is not the printer but the vascularization biology.

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

Your current model treats the Vascularization Depth → Functional Maturation relationship as
unconditional. However, this relationship is scientifically
contingent on Scaffold Degradation Rate being active. Without this condition,
the simulation produces inaccurate results: Vascularization Depth drives Functional Maturation
even when the prerequisite state is not met.

Task A: CONFIGURE THE CONNECTION CONDITION
   • Select the connection arrow: Vascularization Depth → Functional Maturation
   • Click "Conditions" in the connection toolbar
   • Set the regulator condition: IF Scaffold Degradation Rate is ON
   • Click "Save Conditions"

Task B: VALIDATE THE CONDITIONAL MODEL
   • Run the simulation with Scaffold Degradation Rate active and observe
     how Vascularization Depth's effect on Functional Maturation is now gated
   • Toggle Scaffold Degradation Rate ON/OFF while Vascularization Depth remains constant
   • Verify that Functional Maturation only responds to Vascularization Depth when the
     condition is satisfied

Task C: ADDITIONAL CONDITION
   • Select: Scaffold Degradation Rate → Functional Maturation
   • Set condition: IF Vascularization Depth is ON
   • This ensures Scaffold Degradation Rate's effect on Functional Maturation
     is contingent on Vascularization Depth being active

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
   • What happens if you turn OFF Print Resolution?
   • What happens if you turn OFF Nutrient Diffusion Limit?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Multi-Material Printing — The ability to deposit different cell types, scaffold materials, and growth factors from multiple print heads in a single print run — essential for organs that contain dozens of specialized cell types arranged in precise spatial patterns with different mechanical properties
   • Innervation — The growth of nerve fibers into bioprinted tissue to enable sensation and motor control — critical for functional integration of implanted constructs, particularly for tissues like skin that must sense touch and pain, or muscle that must respond to neural signals
   • Mechanical Conditioning — The application of controlled physical forces — stretching, compression, fluid flow — during tissue maturation to stimulate cells to produce stronger extracellular matrix and develop functional mechanical properties that match native tissue

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • How Bioprinting Works — how does this connect to your model?
   • The Vascularization Challenge — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model demonstrate why the 200-micrometer nutrient diffusion limit is the central constraint in organ bioprinting?
   • Why is matching scaffold degradation rate to tissue maturation rate so critical, and what happens when they are mismatched?
   • What does your model reveal about the qualitative difference between printing thin tissues and printing thick organs?
   • How would your model change if a method were developed to print functional capillary networks at the scale of individual cells?

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

Multi-Material Printing. The ability to deposit different cell types, scaffold materials, and growth factors from multiple print heads in a single print run — essential for organs that contain dozens of specialized cell types arranged in precise spatial patterns with different mechanical properties
How would you model that?

Innervation. The growth of nerve fibers into bioprinted tissue to enable sensation and motor control — critical for functional integration of implanted constructs, particularly for tissues like skin that must sense touch and pain, or muscle that must respond to neural signals
How would you model that?

Mechanical Conditioning. The application of controlled physical forces — stretching, compression, fluid flow — during tissue maturation to stimulate cells to produce stronger extracellular matrix and develop functional mechanical properties that match native tissue
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

Biomedical Engineers specializing in tissue engineering design bioprinting systems and tissue constructs at companies like Organovo, CELLINK, and academic medical centers, earning $80,000-$150,000/year. Regenerative Medicine Scientists develop new approaches to growing replacement tissues and organs, working at institutions like the Wake Forest Institute for Regenerative Medicine, earning $90,000-$170,000/year. Clinical Tissue Engineers oversee the production and quality control of bioprinted constructs for patient use in hospital settings, earning $85,000-$140,000/year.

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
Visual: Title slide with bioprinter and translucent tissue construct image
Say: "Seventeen people die every day in the United States waiting for an organ transplant. What if we could print new organs from the patient's own cells — no donor needed, no rejection, no waiting list? That is the promise of bioprinting. The reality is more complicated — and more fascinating — than it sounds."
Do: Open with the transplant shortage statistics. Ask: who knows someone who has been affected by organ failure or the transplant waiting list? Establish the human stakes before the science.
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and vocabulary terms displayed
Say: "Today you are modeling the intersection of 3D printing technology and living biology. You will discover why printing a skin graft is hard, printing a heart patch is harder, and printing a complete kidney is a challenge that may take decades to solve."
Do: Have students read objectives. Pre-teach 'bioink' and 'vascularization.' Demonstrate the 200-micrometer diffusion limit with a visual: hold up a sheet of paper (100 micrometers thick) and explain that cells can only survive within two paper-thicknesses of a blood vessel.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: Can we engineer living human organs from a patient's own cells?
Say: "We CAN print living tissue — several labs have done it. We can even implant bioprinted tissue into patients. The question is whether we can scale from millimeter-thin patches to centimeter-thick organs with billions of cells, miles of blood vessels, and dozens of specialized cell types. The biology says: not yet."
Do: Quick-write: Students estimate how many cells are in a human heart and how many blood vessels supply them. Reveal the real numbers (2-3 billion cells, 100,000+ miles of capillaries) and discuss the engineering scale.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps with bioprinting context
Say: "We are modeling a system where engineering precision meets biological complexity, and where the laws of physics — specifically diffusion — set hard limits on what is possible."
Do: Preview LEVER steps. Emphasize that this model will reveal why the jump from tissue patches to complete organs is not gradual but requires qualitative breakthroughs.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Seven component cards for bioprinting model
Say: "Seven components. Two are physical constraints you cannot change: print resolution and the 200-micrometer nutrient diffusion limit. The other five are biological variables that determine whether your printed tissue lives or dies."
Do: Guide through components. Use a microscope image to show the scale of 200 micrometers. Discuss why print resolution and nutrient diffusion are external constraints while the biological responses are internal.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows showing vascularization as the critical bottleneck
Say: "Everything flows through vascularization. No blood vessels, no oxygen. No oxygen, dead cells. Dead cells, failed organ. The entire challenge of organ bioprinting reduces to one question: can you print a blood vessel network at capillary scale?"
Do: Help students map the critical vascularization pathway. Calculate how many capillaries a kidney needs to serve its million nephrons. Highlight the scaffold degradation timing challenge.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Simulation results for skin, cardiac, and kidney scenarios
Say: "Three tissues, three levels of complexity, three very different outcomes. Watch what happens when you ask the same system to do progressively harder things."
Do: Students predict viability and function before each scenario. The skin scenario succeeds, the cardiac patch partially succeeds, and the kidney scenario reveals why full organs remain beyond reach. Discuss the qualitative difference between incremental and breakthrough challenges.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key findings about the vascularization barrier and complexity scaling
Say: "Bioprinting is not just a printing problem — it is a biology problem. The printer deposits cells, but the cells must organize themselves, build their own structures, and become a functioning tissue. We can guide this process but not fully control it."
Do: Lead discussion on the difference between engineering (precise control) and biology (guided self-organization). Why does tissue maturation take weeks? Why is the outcome variable between batches? Connect to the broader theme of engineering living systems.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Bioprinted tissue design challenge for clinical application
Say: "A hospital needs your tissue engineering design for a real clinical problem. Choose your application, design the construct, and prove it will work."
Do: Groups choose between skin, cartilage, or cardiac applications and design complete bioprinting protocols. Must specify cell source, bioink, scaffold, vascularization strategy, maturation protocol, and quality tests. Present with model evidence.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: Can We 3D-Print a Human Organ?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
Over 100,000 people in the United States are on the organ transplant waiting list right now, and 17 of them die every day because a matching donor organ is not available in time. This shortage exists because organ donation depends on tragic circumstances — healthy organs from recently deceased individuals whose families consent to donation — and the demand far exceeds the supply. Bioprinting offers a revolutionary alternative: manufacturing replacement organs from the patient's own cells, eliminating both the donor shortage and the risk of immune rejection. The technology has made remarkable progress in simple tissues, but the leap to complex organs faces fundamental biological barriers that no engineering solution has yet overcome.

NGSS ALIGNMENT:
HS-LS1-2, HS-ETS1-2: Develop and use a model to illustrate the hierarchical organization of interacting systems that provide specific functions within multicellular organisms. Design a solution to a complex real-world problem by breaking it down into smaller, more manageable problems that can be solved through engineering.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Developing and Using Models
  Students develop computational models of bioprinting and tissue engineering to predict how changes in print parameters, scaffold design, and vascularization affect the viability and function of bioprinted tissue constructs.
• Disciplinary Core Idea: LS1.A Structure and Function
  Students model the hierarchical organization of cells into tissues and organs, understanding how the structure of bioprinted constructs at the cellular and vascular level determines whether the tissue can perform its biological function.
• Crosscutting Concept: Structure and Function
  Students analyze how the three-dimensional architecture of bioprinted tissue — cell arrangement, scaffold geometry, blood vessel network — directly determines whether the construct can sustain cell life and replicate native tissue function.

PACING GUIDE:
• Step 1 (Locate): 8-10 minutes
• Step 2 (Establish): 8-10 minutes
• Step 3 (Visualize & Evaluate): 10-12 minutes
• Step 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Bioprinting, Bioink, Vascularization, Scaffold Architecture, Tissue Maturation
□ Prepare Can we engineer living human organs from a patient's own cells — and could bioprinting end the transplant shortage that kills 17 people every day discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify seven key components of a bioprinting system: print resolution, cell viability rate, vascularization depth, scaffold degradation rate, nutrient diffusion limit, immune compatibility, and functional maturation.
• Establish: Students map relationships showing that nutrient diffusion limit and vascularization depth are the primary constraints determining maximum construct thickness, while print resolution and cell viability determine structural fidelity, and scaffold degradation must be matched to functional maturation timing.
• Visualize: Students build a computational model showing the seven-component bioprinting system with cell survival and tissue function as dependent outcomes.
• Evaluate: Students run skin patch, cardiac patch, and full kidney scenarios to discover how complexity scaling reveals the vascularization barrier as the central unsolved challenge.
• Revise: Students add multi-material printing, innervation, or mechanical conditioning to model more realistic tissue engineering complexity and functional requirements.

BACKGROUND CONTENT:
• How Bioprinting Works:
  Bioprinters are specialized 3D printers that deposit living cells rather than plastic. The most common approach — extrusion bioprinting — pushes bioink (cells suspended in hydrogel) through a fine nozzle to create lines of material that are stacked layer by layer. The nozzle diameter (typically 100-500 micrometers) determines print resolution, while the hydrogel's properties must be carefully balanced: viscous enough to hold shape after deposition but soft enough that shear forces in the nozzle do not kill cells. Other approaches include inkjet bioprinting (which fires tiny droplets of cell-laden fluid), laser-assisted bioprinting (which uses a laser to propel cells from a donor ribbon onto a substrate), and stereolithographic bioprinting (which uses light to crosslink photosensitive hydrogels containing cells). Each method offers different trade-offs between resolution, speed, cell viability, and scalability. After printing, the construct is placed in a bioreactor that provides nutrients, oxygen, temperature control, and sometimes mechanical stimulation during weeks of tissue maturation.

• The Vascularization Challenge:
  The human body's blood vessel network is a fractal branching system spanning from the 2.5-centimeter-diameter aorta down to capillaries just 5-10 micrometers in diameter — smaller than a red blood cell. This network ensures that no cell is more than 200 micrometers from a capillary, because oxygen and nutrients can only diffuse that far through tissue before being consumed. In bioprinted constructs, cells more than 200 micrometers from a nutrient source begin dying within hours. For thin tissues like skin (1-3 millimeters thick), surface diffusion can sustain all cells during maturation. For thick tissues and organs, an internal blood vessel network is absolutely required. Current bioprinting can create channels for large and medium vessels (down to about 200-500 micrometers diameter), but the capillary-level branching that connects these channels to every cell requires self-assembly by the cells themselves — a process that takes weeks and is not reliably controlled. This vascularization gap is the single largest barrier between current tissue engineering and functional organ bioprinting.

• Cell Sourcing and Immune Compatibility:
  Bioprinted tissue requires billions of living cells. For a heart, that number is approximately 2-3 billion cardiomyocytes plus billions more endothelial cells, fibroblasts, and smooth muscle cells. These cells can come from the patient (autologous), from donors (allogeneic), or from pluripotent stem cell lines (iPSCs). Autologous cells — derived from the patient's own tissue and reprogrammed into needed cell types using induced pluripotent stem cell technology — eliminate immune rejection but require 4-8 weeks of cell culture to produce sufficient quantities. Donor cells and stem cell lines are more quickly available but trigger immune responses that may require lifelong immunosuppression. The iPSC approach is currently the most promising: a small skin biopsy from the patient is reprogrammed into stem cells that can differentiate into any cell type needed for the organ. However, iPSC reprogramming is expensive, takes weeks, and carries a small risk of genetic mutations during the reprogramming process.

• Current Achievements and Future Trajectory:
  As of 2025, bioprinting has achieved clinical or near-clinical success in several tissue types. Bioprinted skin grafts are in clinical trials for burn treatment. Bioprinted cartilage implants have been successfully implanted in human ears and noses. Researchers at the Wake Forest Institute for Regenerative Medicine have bioprinted bladder scaffolds that were successfully implanted in patients. Bioprinted blood vessel segments have been tested in animal models. Organovo has bioprinted liver tissue patches for drug toxicity testing. However, no complete solid organ has been bioprinted and transplanted. The progression from simple tissues to complex organs is not linear — it requires simultaneous breakthroughs in vascularization at capillary scale, multi-cell-type coordination, functional maturation of specialized structures (like kidney nephrons or liver lobules), and quality control for constructs containing billions of cells. Most researchers estimate that bioprinted tissue patches for organ repair will become clinically routine within 10-15 years, while complete bioprinted organs are 20-30 or more years away.

COMMON MISCONCEPTIONS:
• "Bioprinting organs works just like 3D printing plastic objects"
  Reality: 3D printing plastic is purely an engineering problem: deposit material, let it harden, done. Bioprinting deposits living cells that must survive the printing process, receive continuous nutrients and oxygen, organize themselves into functional tissue, and mature over weeks in bioreactors. The printed construct immediately after printing is like a building frame with workers inside — the structure exists but the function has not yet developed. Cell death begins within hours if nutrient supply is inadequate. The printed architecture may not match the final tissue architecture because cells migrate, proliferate, and remodel their environment. The model shows that printing is only about 10% of the challenge — the other 90% is keeping cells alive and guiding them to functional maturity.
  Strategy: Comparison activity: Students 3D-print a simple plastic object (takes minutes, is immediately functional) and then review a bioprinting protocol (takes hours to print, weeks to mature, may fail). Discuss what makes living material fundamentally different from plastic.

• "We will be able to print replacement organs within five years"
  Reality: This misconception confuses the pace of progress in simple tissues with the timeline for complex organs. Bioprinted skin grafts and cartilage implants may reach routine clinical use within five years because they are thin, involve few cell types, and have relatively simple functional requirements. Complete solid organs require solving vascularization at capillary scale, coordinating dozens of cell types in precise three-dimensional arrangements, achieving functional maturation of complex structures like nephrons or cardiac conducting fibers, and producing billions of patient-specific cells. These are not incremental improvements but fundamental breakthroughs. The model quantitatively demonstrates the orders-of-magnitude gap between current tissue capability and organ-level complexity.
  Strategy: Scale exercise: Compare the number of cell types, blood vessel length, and functional units in a skin patch versus a kidney. The skin patch has 2 cell types and no internal blood vessels. The kidney has 26+ cell types, 160 kilometers of blood vessels, and 1 million nephrons. Calculate how many times more complex the kidney is across each dimension.

• "Using the patient's own cells means there is no risk of immune rejection"
  Reality: While autologous cells (the patient's own cells) dramatically reduce rejection risk compared to donor cells, the bioprinting process introduces non-self materials — hydrogel scaffolds, crosslinking agents, residual growth factors — that can trigger immune responses. Additionally, the cell reprogramming process (iPSC generation) can introduce mutations that make cells partially foreign to the immune system. Scaffold degradation products may cause local inflammation. And if the bioprinted construct contains any contaminating bacteria or endotoxins from the manufacturing process, the immune response can be severe. The model shows that immune compatibility is a spectrum, not a binary, and that using autologous cells reduces but does not eliminate immune-related challenges.
  Strategy: Analysis: List every non-patient-derived material in a bioprinted construct (hydrogel, crosslinker, growth factors, culture media residue, scaffold polymers) and research which ones are known to trigger immune responses. Discuss why even an all-autologous-cell construct is not truly 100% self.

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
Big Question: Can we engineer living human organs from a patient's own cells — and could bioprinting end the transplant shortage that kills 17 people every day?
Answer: Bioprinting constructs living tissue by depositing cells and biomaterials in precise three-dimensional patterns, layer by layer. For thin, relatively simple tissues — skin patches, cartilage, corneas — the technology is approaching clinical viability because these structures are thin enough for nutrients to diffuse from the surface and involve relatively few cell types. Researchers have successfully bioprinted skin grafts that heal burns, cartilage implants that repair joints, and blood vessel segments that carry blood flow. However, printing complex solid organs like kidneys, hearts, and livers requires solving the vascularization problem: every cell must be within 200 micrometers of a blood capillary, which means the printed organ must contain a complete, functional, microscale blood vessel network — something no bioprinter can yet achieve. A human kidney contains over 100 miles of blood vessels feeding a million filtering units composed of dozens of specialized cell types arranged in precise three-dimensional patterns. Current bioprinters can produce structures with channels for major blood vessels, but the capillary-level branching required to sustain thick tissue remains beyond current capability. The most honest answer: we can 3D-print tissues, we are making progress toward organs, but printing a complete transplantable organ is likely decades away — and the primary barrier is not the printer but the vascularization biology.

Simulation Answers:
• Skin Patch Bioprinting Scenario: A skin patch 1-2 millimeters thick is within the nutrient diffusion limit for surface-fed constructs — no internal vascularization is required. Cell viability remains high (85-95%) because the construct is thin enough to print quickly with moderate resolution. The two primary skin cell types (keratinocytes and fibroblasts) are well-characterized and readily cultured. Scaffold degradation timing is relatively forgiving because skin has simple mechanical requirements. The model shows high overall success probability, consistent with real-world results: bioprinted skin grafts are in clinical trials with promising outcomes. This scenario represents the current frontier of bioprinting clinical application.
• Cardiac Patch with Vascularization Scenario: A 5-millimeter cardiac patch exceeds the nutrient diffusion limit, requiring internal blood vessel channels. With channels spaced 400 micrometers apart, the model shows adequate nutrient delivery to all cells — but only if the channels are perfused with nutrient media during maturation. Cell viability drops to 70-80% due to longer print times and the complexity of printing multiple cell types (cardiomyocytes, endothelial cells, fibroblasts). The critical challenge emerges during functional maturation: cardiomyocytes must organize into aligned fibers that contract synchronously and conduct electrical impulses. The model shows partial success — the outer regions mature well but the interior shows variable cell organization and incomplete electrical coupling. This represents the current research frontier.
• Full Kidney Scaffold Scenario: The kidney scenario reveals why complete organ bioprinting remains beyond current capability. A kidney contains approximately 1 million nephrons, each with a glomerulus, tubule system, and collecting duct, composed of at least 26 distinct cell types, supplied by over 100 miles of blood vessels branching from arteries down to capillaries 5-10 micrometers in diameter. The model shows cascading failures: print resolution cannot replicate glomerular architecture (which requires sub-cellular precision), vascularization cannot reach capillary scale through printing alone, the number of cells required (billions) exceeds current culture capacity for patient-derived cells, and the maturation time required for nephron functional development (months) exceeds the period during which printed scaffolds maintain structural integrity. The model quantitatively demonstrates that full organ bioprinting is not an incremental extension of tissue printing but requires qualitative breakthroughs in multiple simultaneous parameters.

Reflection Exemplars:
• Q: Why is the 200-micrometer diffusion limit the central constraint in organ bioprinting?
  A: The 200-micrometer diffusion limit is a physical constant — oxygen molecules can only diffuse approximately 200 micrometers through tissue before being consumed by cell metabolism. This means every cell in a bioprinted construct must be within 200 micrometers of either a surface (for thin tissues) or a blood vessel (for thick tissues). For a skin graft at 1-2 millimeters thickness, surface diffusion reaches all cells. For a heart at 15 millimeters thickness, the interior is 75 times farther than the diffusion limit from the nearest surface. This requires an internal vascular network with capillaries no more than 400 micrometers apart throughout the entire volume. The model shows that this constraint transforms organ bioprinting from a printing problem into a vascularization problem — and printing functional capillary networks at 5-10 micrometer scale is currently impossible.
• Q: Why is the jump from tissue patches to complete organs qualitatively different?
  A: The model reveals that scaling from patches to organs is not like making a bigger version of the same thing — it is like trying to build a city after successfully building a house. A skin patch requires 2 cell types, no internal vasculature, and simple mechanical properties. A kidney requires 26+ cell types arranged in precise three-dimensional patterns, over 100 miles of hierarchical blood vessels, a million identical functional units each with sub-cellular precision architecture, and months of coordinated maturation. The challenges are not additive but multiplicative: every increase in cell type diversity multiplies the printing complexity, every increase in thickness multiplies the vascularization requirement, and every increase in functional complexity multiplies the maturation challenge. The model shows that current bioprinting can handle individual challenges in isolation but cannot yet solve all of them simultaneously at organ scale.

STEM CHALLENGE GUIDANCE:
Title: Design a Bioprinted Tissue for Clinical Application
Mission: Design a bioprinted tissue construct for a specific clinical application, addressing cell sourcing, scaffold design, vascularization strategy, maturation protocol, and implantation safety.
Scenario: A hospital's tissue engineering lab has asked your team to design a bioprinted tissue construct for one of three clinical needs: a skin graft for burn patients, a cartilage patch for knee repair, or a cardiac patch for heart attack recovery. Each application has different requirements for thickness, cell types, mechanical properties, vascularization, and functional integration. Your design must specify the bioink composition, print parameters, scaffold architecture, maturation protocol, and quality control tests to ensure the construct is safe and functional before implantation.
Introduction: Present the challenge: A hospital tissue engineering laboratory needs your team to design a complete bioprinting protocol for one of three clinical applications: (1) a dermal skin graft for severe burn patients, (2) an articular cartilage patch for knee osteoarthritis, or (3) a cardiac muscle patch for heart attack recovery. Your design must specify the cell source and culture protocol, bioink composition, scaffold material and architecture, print parameters, vascularization strategy, bioreactor maturation conditions, quality control testing, and implantation procedure.

Key Concepts:
• Shear Thinning Hydrogels: Bioink hydrogels that become less viscous under the shear stress of extrusion through the print nozzle, allowing smooth flow, but rapidly recover their viscosity after deposition, holding their shape. This shear-thinning behavior is critical because it enables printing at reasonable pressures while maintaining structural fidelity — without it, the bioink either clogs the nozzle or spreads into a puddle after deposition.
• Bioreactor Conditioning: After printing, tissue constructs are placed in bioreactors that replicate physiological conditions — 37 degrees Celsius, 5% CO2, controlled oxygen, and nutrient media flow. For cardiac tissue, bioreactors apply electrical stimulation to encourage cardiomyocyte alignment and synchronous contraction. For cartilage, bioreactors apply compressive loading to stimulate matrix production. The bioreactor environment is as important to the final tissue quality as the printing itself.
• Decellularized Organ Scaffolds: An alternative to fully synthetic scaffolds: taking a donor organ, removing all cells with detergent solutions (decellularization), and reseeding the remaining extracellular matrix scaffold with the patient's own cells. This approach preserves the organ's natural three-dimensional architecture including the vascular network, but depends on donor organ availability and complete cell removal to prevent immune rejection.

Evaluation Rubric:
• Expert (4): Design includes specific cell source with culture timeline, detailed bioink formulation with rheological justification, scaffold architecture matched to tissue requirements, vascularization strategy with quantitative diffusion analysis, maturation protocol with bioreactor conditions, quality control tests with pass/fail criteria, and honest assessment of current limitations
• Proficient (3): Design addresses cell source, bioink, scaffold, and maturation with model evidence, and considers vascularization requirements and quality control
• Developing (2): Design describes bioprinting process but lacks quantitative analysis of vascularization constraints or does not address maturation and quality control
• Beginning (1): Design is incomplete, ignores the nutrient diffusion limit, or assumes organ-scale printing is straightforward without addressing fundamental biological constraints

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a tissue complexity comparison table showing skin (2 cell types, 1-2mm thick, no internal vasculature needed), cartilage (1-2 cell types, 3-5mm thick, avascular), cardiac (3-4 cell types, 5-15mm thick, dense vasculature required), and kidney (26+ cell types, 50mm+ thick, 100+ miles of vasculature) to help students select appropriate challenge levels
  • Use a scale visualization: the 200-micrometer diffusion limit is about the width of two human hairs — show this alongside the centimeter-scale thickness of organs to make the vascularization challenge visceral
  • Sentence frames: 'Our bioprinted __ construct uses __ cells in a __ hydrogel scaffold with blood vessel channels spaced __ micrometers apart, requiring __ weeks of maturation in a bioreactor at __ conditions, and we verify viability using __'

Extensions (Advanced Learners):
  • Research the Wake Forest Institute for Regenerative Medicine's achievements in bioprinting bladders, ears, and muscle tissue, and evaluate which of their techniques could be applied to more complex organs using your model framework
  • Investigate the decellularized organ scaffold approach as an alternative to fully bioprinted organs — compare the advantages and limitations of each approach for kidney replacement
  • Design a bioprinting facility that could produce 1,000 patient-specific skin grafts per year, specifying the cell culture infrastructure, bioprinting stations, bioreactor capacity, quality control laboratory, and cost per graft

Cross-Curricular Connections:
  • Math: Calculate the total length of blood vessels needed in a bioprinted kidney. If the kidney volume is 150 cubic centimeters and capillaries must be within 200 micrometers of every cell, model the capillary network as parallel tubes and calculate the total tube length required. Compare this to the actual approximately 160 kilometers of blood vessels in a real kidney.
  • ELA: Write a patient information document explaining bioprinted tissue therapy to a non-scientist facing a choice between a traditional organ transplant and an experimental bioprinted tissue implant. Use clear language, accurate science, and balanced presentation of benefits and risks to help them make an informed decision.
  • Ethics: Analyze the equity implications of bioprinted organ technology: if a bioprinted kidney costs $500,000, who has access? Should bioprinted organs be covered by insurance? Should government fund this research when preventive health care for the conditions that cause organ failure might cost less? Research these questions and present a policy recommendation.

CAST ALIGNMENT:
• Model how print resolution, cell viability, and vascularization depth interact to determine the maximum thickness and complexity of viable bioprinted tissue constructs
• Analyze the relationship between scaffold degradation rate, tissue maturation time, and the mechanical integrity of bioprinted constructs during the transition from artificial scaffold to natural extracellular matrix
• Evaluate the feasibility of bioprinting specific organs by comparing the vascularization, cell type, and structural complexity requirements against current bioprinting capabilities

CAST-Style Assessment Questions:
• Multiple Choice: A bioprinted cardiac patch is 5 millimeters thick and contains printed blood vessel channels spaced 400 micrometers apart. Given the 200-micrometer nutrient diffusion limit, will all cells in the construct receive adequate oxygen and nutrients? Explain your reasoning using the relationship between diffusion distance and channel spacing.
• Constructed Response: Using evidence from your model, explain why bioprinting a functional skin graft is achievable with current technology while bioprinting a functional kidney remains decades away. Reference at least three model variables — including vascularization depth, cell type complexity, and functional maturation requirements — in your response.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: Can We 3D-Print a Human Organ?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. What do you already know about 3D printing, and how do you think it might be adapted to print living tissue?

   _________________________________________________________

   _________________________________________________________

2. Why do you think there is a shortage of donor organs for transplantation, and what problems does this cause?

   _________________________________________________________

   _________________________________________________________

3. Draw a diagram showing how you think cells could be arranged in layers to build a piece of tissue, and label what each layer would need to survive.

   [DRAWING BOX]

4. What is the difference between printing a plastic object and printing living tissue — what additional challenges would living material create?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Bioprinting                   
___ Bioink                        
___ Vascularization               
___ Scaffold Architecture         
___ Tissue Maturation             

A. An additive manufacturing process that uses specialized printers to deposit living cells, biomaterials, and growth factors in precise three-dimensional patterns — building tissue layer by layer much like a conventional 3D printer builds plastic objects, but with living material that must remain viable throughout the printing process
B. The printable material containing living cells suspended in a hydrogel matrix — the hydrogel must be viscous enough to hold its shape during printing but soft enough to allow cells to survive, migrate, and form connections, while also providing nutrients and structural support during tissue maturation
C. The formation of blood vessel networks within bioprinted tissue — without blood vessels delivering oxygen and nutrients, cells more than 200 micrometers from a capillary die within hours, making vascularization the single greatest challenge in bioprinting organs thicker than a few cell layers
D. The three-dimensional structural framework — either printed simultaneously with cells or seeded with cells after printing — that provides mechanical support, guides cell organization, and degrades at a controlled rate as cells produce their own extracellular matrix to replace it
E. The weeks-to-months incubation period after printing during which cells proliferate, differentiate, form cell-cell junctions, deposit extracellular matrix, and develop the mechanical and functional properties of native tissue — a bioprinted construct immediately after printing is structurally and functionally immature

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

SCENARIO: Skin Patch Bioprinting
Settings: Moderate resolution, thin construct, no deep vascularization required
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Cardiac Patch with Vascularization
Settings: 5mm thick cardiac construct requiring internal blood vessel channels
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Full Kidney Scaffold
Settings: Complex organ with millions of functional units and extensive vasculature
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

1. How does your model demonstrate why the 200-micrometer nutrient diffusion limit is the central constraint in organ bioprinting?

   _________________________________________________________

   _________________________________________________________

2. Why is matching scaffold degradation rate to tissue maturation rate so critical, and what happens when they are mismatched?

   _________________________________________________________

   _________________________________________________________

3. What does your model reveal about the qualitative difference between printing thin tissues and printing thick organs?

   _________________________________________________________

   _________________________________________________________

4. How would your model change if a method were developed to print functional capillary networks at the scale of individual cells?

   _________________________________________________________

   _________________________________________________________

5. What are the limitations of modeling bioprinting when individual patient cells behave differently and maturation rates vary unpredictably?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Can we engineer living human organs from a patient's own cells — and could bioprinting end the transplant shortage that kills 17 people every day? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Developing and Using Models
   □ Disciplinary Core Idea: LS1.A Structure and Function
   □ Crosscutting Concept: Structure and Function

3. What are the limitations of modeling bioprinting when individual patient cells behave differently and maturation rates vary unpredictably?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Bioprinted Tissue for Clinical Application
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design a bioprinted tissue construct for a specific clinical application, addressing cell sourcing, scaffold design, vascularization strategy, maturation protocol, and implantation safety.

SCENARIO: A hospital's tissue engineering lab has asked your team to design a bioprinted tissue construct for one of three clinical needs: a skin graft for burn patients, a cartilage patch for knee repair, or a cardiac patch for heart attack recovery. Each application has different requirements for thickness, cell types, mechanical properties, vascularization, and functional integration. Your design must specify the bioink composition, print parameters, scaffold architecture, maturation protocol, and quality control tests to ensure the construct is safe and functional before implantation.

GUIDING QUESTIONS:
• What cell source provides the best balance between immune compatibility and production speed for your clinical application?
• How will you ensure adequate nutrient delivery throughout your construct during the maturation period before implantation?
• What functional tests would you require to confirm the bioprinted tissue is ready for implantation into a patient?

DESIGN THINKING:
• What bioink composition — hydrogel type, cell density, growth factors — would you select for your tissue type and why?

  _________________________________________________________

• What scaffold architecture would provide the mechanical properties your tissue needs while allowing cell migration and matrix remodeling?

  _________________________________________________________

• How long would you expect the maturation period to last and what environmental conditions would you maintain in the bioreactor?

  _________________________________________________________

• What are the three most critical quality control tests you would perform before approving the construct for implantation?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Design includes specific cell source with culture timeline, detailed bioink formulation with rheological justification, scaffold architecture matched to tissue requirements, vascularization strategy with quantitative diffusion analysis, maturation protocol with bioreactor conditions, quality control tests with pass/fail criteria, and honest assessment of current limitations
• Proficient (3): Design addresses cell source, bioink, scaffold, and maturation with model evidence, and considers vascularization requirements and quality control
• Developing (2): Design describes bioprinting process but lacks quantitative analysis of vascularization constraints or does not address maturation and quality control
• Beginning (1): Design is incomplete, ignores the nutrient diffusion limit, or assumes organ-scale printing is straightforward without addressing fundamental biological constraints

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CAST-Aligned Pre/Post Assessment

### Administration Instructions

These 5 multiple-choice questions are administered identically as both a pre-assessment (before Activity 1) and a post-assessment (after Activity 4). Score each out of 5. Learning growth = post-score minus pre-score.

Questions follow the California Science Test (CAST) stimulus-response format. Each item is three-dimensional, assessing a Science and Engineering Practice (SEP), Disciplinary Core Idea (DCI), and Crosscutting Concept (CCC) simultaneously, aligned to HS-LS1-2, HS-ETS1-2.

---

### Question 1

CAST Alignment: SEP 2.1.1 (Develop and use a model to represent relationships) + DCI LS1.A (Structure and function of organisms) + CCC4 (Systems and system models)

A bioprinting research team successfully prints a miniature kidney (organoid) measuring 2 cm in diameter. The printer deposits alternating layers of living kidney cells suspended in a biocompatible hydrogel matrix, with channels left open for eventual blood vessel formation. After 14 days of incubation, the organoid shows cellular organization resembling kidney tubules, and 70% of cells remain viable. However, cells deeper than 200 micrometers from the nearest channel show signs of oxygen deprivation (hypoxia), highlighting the critical challenge of vascularization in large-scale tissue engineering.

A student's bioprinting model shows that increasing print resolution from 200 to 50 micrometers improves tissue architecture fidelity by 60% but reduces cell viability from 90% to 65% due to increased shear stress. How should this trade-off be evaluated?

A. Higher resolution is always preferable because tissue architecture determines function
B. Cell viability is unimportant because dead cells will be replaced by living ones
C. The trade-off reveals that better structural precision comes at the cost of cell survival; a construct with beautiful architecture but 35% dead cells may fail to function. Optimal resolution must balance structural fidelity against the minimum cell viability required for tissue function
D. The 50-micrometer resolution should be used for all tissue types regardless of viability impact

Correct Answer: C

Feedback: Architecture is meaningless if cells die. The optimal print resolution varies by tissue type: complex organs may need 50-micrometer precision, but only if cell viability remains above the threshold for functional maturation. If you chose A, this response overgeneralizes without considering the specific mechanisms and evidence presented. Resolution and viability are coupled through shear stress. Finer printing requires smaller nozzles, generating more shear force. The optimal resolution is tissue-specific: some tissues require architectural precision, others prioritize cell survival. Neither variable can be maximized independently. If you chose B, this answer does not account for the key mechanism or relationship the evidence demonstrates. Resolution and viability are coupled through shear stress. Finer printing requires smaller nozzles, generating more shear force. The optimal resolution is tissue-specific: some tissues require architectural precision, others prioritize cell survival. Neither variable can be maximized independently. If you chose D, this choice overgeneralizes without considering the specific mechanisms and evidence presented. Resolution and viability are coupled through shear stress. Finer printing requires smaller nozzles, generating more shear force. The optimal resolution is tissue-specific: some tissues require architectural precision, others prioritize cell survival. Neither variable can be maximized independently.
---

### Question 2

CAST Alignment: SEP 2.1.2 (Determine relationships among system components) + DCI LS1.A (Structure and function of organisms) + CCC2 (Cause and effect)

A computational model of tissue engineering tracks the oxygen diffusion limit as the fundamental constraint on bioprinted organ size. Oxygen diffuses from blood vessels into surrounding tissue, but the diffusion distance is limited to approximately 200 micrometers before oxygen concentration drops below the level needed for cell survival. In a natural organ, capillary networks ensure that no cell is more than 200 micrometers from a blood vessel. The model shows that printing a full-sized kidney (12 cm) would require approximately 1.5 billion capillary branch points, a vascular network far more complex than current printing technology can achieve.

The model shows that scaffold degradation rate must match the rate of cell-produced extracellular matrix deposition. If the scaffold degrades faster than cells produce matrix, what is the structural consequence?

A. Faster scaffold degradation improves nutrient diffusion and cell survival
B. The degradation rate has no effect on construct integrity after printing
C. The construct becomes stronger because cells compensate by producing more matrix
D. The construct collapses because the supporting scaffold disappears before cells have produced sufficient structural matrix to maintain the tissue's shape and mechanical integrity

Correct Answer: D

Feedback: The scaffold provides mechanical support during maturation. If it degrades before cells produce their own structural matrix, the construct loses its shape and collapses. Matching these rates is critical for successful tissue engineering. If you chose C, this response does not account for the key mechanism or relationship the evidence demonstrates. The scaffold is a temporary structure that must persist until cells produce their own matrix. If degradation outpaces matrix production, the construct loses mechanical support and collapses. This timing mismatch is a common failure mode in bioprinted tissues. If you chose A, this answer does not account for the key mechanism or relationship the evidence demonstrates. The scaffold is a temporary structure that must persist until cells produce their own matrix. If degradation outpaces matrix production, the construct loses mechanical support and collapses. This timing mismatch is a common failure mode in bioprinted tissues. If you chose B, this choice does not account for the key mechanism or relationship the evidence demonstrates. The scaffold is a temporary structure that must persist until cells produce their own matrix. If degradation outpaces matrix production, the construct loses mechanical support and collapses. This timing mismatch is a common failure mode in bioprinted tissues.
---

### Question 3

CAST Alignment: SEP 2.1.2 (Determine relationships among components) + DCI ETS1.B (Develop solutions to engineering problems) + CCC4 (Describe components and interactions)

Researchers compare three approaches to solving the vascularization problem. Approach 1 prints sacrificial channels using a dissolvable material, creating hollow tubes that can be perfused with blood after printing. Approach 2 co-prints endothelial cells (the cells that line blood vessels) and relies on them to self-organize into capillary networks through angiogenesis. Approach 3 uses a decellularized donor organ scaffold (an organ with all cells removed, leaving only the protein scaffold including intact blood vessel channels) and repopulates it with the patient's own cells. The model evaluates each approach's vascularization density, scalability, and immune compatibility.

A student models two bioprinting approaches for a heart patch: Approach A achieves immediate structural integrity but requires donor cells with rejection risk. Approach B uses autologous cells with no rejection but requires 6 weeks of cell culture before printing. For a patient with heart failure deteriorating over 2-3 months, which analysis best evaluates these options?

A. The decision depends on the patient's deterioration timeline versus the 6-week culture period: if the patient can survive 6 weeks plus printing and maturation time, Approach B's immune compatibility advantage may produce better long-term outcomes despite the delay
B. Approach A is always superior because time is the only factor
C. Approach B is always superior because rejection will always destroy Approach A constructs
D. Both approaches are equivalent because maturation time is the same

Correct Answer: A

Feedback: This is a patient-specific clinical trade-off. The immune compatibility advantage of autologous cells provides long-term benefit, but only if the patient survives the cell culture delay. Medical decision-making must weigh acute survival against long-term graft success. If you chose B, this response overgeneralizes without considering the specific mechanisms and evidence presented. The optimal approach depends on the individual patient's condition. A rapidly deteriorating patient may not survive the 6-week culture period, making donor cells necessary despite rejection risk. A more stable patient benefits from the immune compatibility of autologous cells. If you chose C, this answer overgeneralizes without considering the specific mechanisms and evidence presented. The optimal approach depends on the individual patient's condition. A rapidly deteriorating patient may not survive the 6-week culture period, making donor cells necessary despite rejection risk. A more stable patient benefits from the immune compatibility of autologous cells. If you chose D, this choice does not account for the key mechanism or relationship the evidence demonstrates. The optimal approach depends on the individual patient's condition. A rapidly deteriorating patient may not survive the 6-week culture period, making donor cells necessary despite rejection risk. A more stable patient benefits from the immune compatibility of autologous cells.
---

### Question 4

CAST Alignment: SEP 2.1.4 (Represent mechanisms to explain/predict events) + DCI LS1.A (Structure and function of organisms) + CCC7 (Stability and change)

A clinical trial tracks outcomes of the first bioprinted tracheal (windpipe) implant in a patient whose own trachea was destroyed by cancer. The implant was printed using the patient's own stem cells on a synthetic polymer scaffold shaped by CT scan data. At 6-month follow-up, the implant has maintained structural integrity and 80% of the surface has been covered by the patient's own respiratory epithelial cells. However, the implant lacks the mucociliary escalator (coordinated hair-like cilia that move mucus), meaning the patient requires regular suctioning to clear secretions. The model predicts that functional cilia development may take 18-24 additional months.

The model reveals that bioprinted tissue thicker than 1 mm develops necrotic cores within 24 hours without vascularization, regardless of how perfectly the cells were printed. What does this demonstrate about the hierarchy of engineering challenges in bioprinting?

A. The necrotic core will eventually be cleared by the body's immune system
B. Thicker tissues are unnecessary because thin patches are sufficient for all applications
C. Cell viability during printing is more important than vascularization
D. Vascularization is the gating constraint: no matter how well you solve printing resolution, bioink composition, cell sourcing, or scaffold design, the construct will fail without adequate blood vessel networks, making vascularization the prerequisite that all other improvements depend on

Correct Answer: D

Feedback: Vascularization is the hierarchical gating constraint. All other bioprinting advances are necessary but insufficient without solving the vascular challenge. A perfectly printed organ with no blood supply is a dead organ. If you chose C, this response does not account for the key mechanism or relationship the evidence demonstrates. The model demonstrates a hierarchy of constraints: vascularization sits at the top. Without adequate blood vessel networks, improvements in every other parameter, resolution, bioink, cell viability, and scaffold design, cannot produce a viable thick tissue. Vascularization is the prerequisite for all other advances. If you chose B, this answer overgeneralizes without considering the specific mechanisms and evidence presented. The model demonstrates a hierarchy of constraints: vascularization sits at the top. Without adequate blood vessel networks, improvements in every other parameter, resolution, bioink, cell viability, and scaffold design, cannot produce a viable thick tissue. Vascularization is the prerequisite for all other advances. If you chose A, this choice overgeneralizes without considering the specific mechanisms and evidence presented. The model demonstrates a hierarchy of constraints: vascularization sits at the top. Without adequate blood vessel networks, improvements in every other parameter, resolution, bioink, cell viability, and scaffold design, cannot produce a viable thick tissue. Vascularization is the prerequisite for all other advances.
---

### Question 5

CAST Alignment: SEP 2.1.4 (Represent mechanisms to predict a scientific event) + DCI ETS1.B (Develop solutions to engineering problems) + CCC4 (Describe system components and interactions)

A regulatory and ethics committee reviews a proposal to bioprint a human heart for transplant. The engineering team presents a 10-year development roadmap: years 1-3 achieve multi-chamber printing with functional valves, years 4-6 achieve integrated vascularization and electrical conduction system, years 7-8 conduct large animal testing, and years 9-10 begin human clinical trials. Current organ transplant waitlists have 100,000+ patients with a 17-person daily death rate. The model compares the bioprinting timeline against alternative strategies: xenotransplantation (animal-to-human organ transplant, 3-5 years to clinical use) and mechanical artificial hearts (currently available but with a 2-year average device lifespan and significant quality-of-life limitations).

Based on the bioprinting model, which conclusion about the relationship between construct complexity and functional maturation time is best supported by the simulation data?

A. Simpler constructs require longer maturation because they have fewer cells to produce matrix
B. Functional maturation time increases nonlinearly with construct complexity because multi-tissue constructs require coordinated development of multiple cell types, formation of tissue-tissue interfaces, and integration of vascular, structural, and functional systems that must develop in the correct sequence
C. Maturation time is constant regardless of construct complexity
D. More complex constructs mature faster because they contain more diverse cell types

Correct Answer: B

Feedback: Complex constructs face a sequential development challenge: different tissue types must mature in coordination, interfaces must form between tissues, and vascular networks must integrate with functional units. This orchestration requires substantially more time than simple, single-tissue constructs. If you chose D, this response does not account for the key mechanism or relationship the evidence demonstrates. Complexity and maturation time have a nonlinear relationship. Simple tissue patches need only one cell type to mature. Multi-tissue constructs require coordinated development of multiple cell populations, tissue-tissue interface formation, and vascular integration, each adding time and complexity. If you chose C, this answer does not account for the key mechanism or relationship the evidence demonstrates. Complexity and maturation time have a nonlinear relationship. Simple tissue patches need only one cell type to mature. Multi-tissue constructs require coordinated development of multiple cell populations, tissue-tissue interface formation, and vascular integration, each adding time and complexity. If you chose A, this choice does not account for the key mechanism or relationship the evidence demonstrates. Complexity and maturation time have a nonlinear relationship. Simple tissue patches need only one cell type to mature. Multi-tissue constructs require coordinated development of multiple cell populations, tissue-tissue interface formation, and vascular integration, each adding time and complexity.
---

### Answer Key

Question 1: C (Cognitive Level: Identify -- SEP 2.1.1, DCI HS-LS1-2, CCC4)
Question 2: D (Cognitive Level: Reason -- SEP 2.1.2, DCI HS-LS1-2, CCC2)
Question 3: A (Cognitive Level: Reason -- SEP 2.1.2, DCI HS-LS1-2, CCC4)
Question 4: D (Cognitive Level: Reason + Evidence -- SEP 2.1.4, DCI HS-ETS1-2, CCC7)
Question 5: B (Cognitive Level: Predict + Apply -- SEP 2.1.4, DCI HS-ETS1-2, CCC4)

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-11/G11L3-L08/G11L3-L08-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-11/G11L3-L08/G11L3-L08-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-11/G11L3-L08/G11L3-L08-Student-Presentation.pptx] |
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