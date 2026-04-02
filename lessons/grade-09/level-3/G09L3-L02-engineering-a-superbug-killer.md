# Lesson: Engineering a Superbug Killer

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G09L3-L02 |
| **Grade** | 9th Grade — Level 3: Biotech |
| **Lesson Name** | Engineering a Superbug Killer |
| **Status** | Template |

---

## Platform

### Title
**Engineering a Superbug Killer — Optimizing Bacteriophage Therapy Against Antibiotic-Resistant Bacteria**

### Overview
This lesson introduces students to predictive modeling and optimization in the context of bacteriophage therapy — one of the most promising alternatives to antibiotics. Biotech skill focus: Predictive modeling and optimization. With antibiotic resistance killing over 1.27 million people annually and the pipeline for new antibiotics nearly dry, phage therapy represents a paradigm shift in infectious disease treatment that students must understand. Students investigate the driving question: Antibiotics are failing. Can we engineer viruses to kill the superbugs that antibiotics can't? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of diverse 14-15 year old students in an advanced microbiology lab examining electron microscope images of bacteriophages attacking bacteria on large display screens, with phage therapy diagrams and bacterial culture plates visible, dramatic blue-green laboratory lighting]

### Grade
9th Grade — Level 3: Biotech

### NGSS Standard
**HS-LS1-2, HS-LS4-2**: Develop and use a model to illustrate the hierarchical organization of interacting systems that provide specific functions within multicellular organisms; construct an explanation based on evidence that the process of evolution primarily results from natural selection.

### Learning Objectives
- Build an optimization model for bacteriophage therapy that balances phage specificity, bacterial resistance evolution, and microbiome safety
- Analyze how phage-bacteria population dynamics interact with the human immune system across treatment timelines
- Optimize treatment timing and dosage to maximize bacterial kill while minimizing disruption to beneficial gut flora
- Evaluate how natural selection drives bacterial resistance to phage therapy and design strategies to counter it

### Component List (Starting Model: 9 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Phage Population | Internal | The total number of active bacteriophage particles in the patient's system, which increases through successful replication inside bacterial hosts and decreases through immune clearance and natural degradation |
| Target Bacteria Population | Internal | The count of pathogenic antibiotic-resistant bacteria causing the infection, which decreases as phages successfully infect and lyse cells but increases through bacterial reproduction |
| Phage Specificity | External | The engineered precision of the phage's targeting system — how well it distinguishes the pathogenic bacteria from beneficial microbiome species, adjustable through bioengineering of tail fiber proteins |
| Bacterial Resistance Rate | Internal | The speed at which the target bacterial population evolves resistance to the phage through mutations in surface receptor proteins, preventing phage attachment and infection |
| Immune System Response | Internal | The patient's innate and adaptive immune activity against both the infecting bacteria AND the therapeutic phages — the immune system may clear phages before they complete their work |
| Phage Replication Rate | Internal | The number of new phage particles produced per lysis event (burst size) multiplied by the infection frequency — determines how fast the phage population amplifies in the presence of target bacteria |
| Healthy Microbiome Impact | Internal | The degree of collateral damage to beneficial gut bacteria caused by off-target phage activity — lower Phage Specificity increases microbiome disruption |
| Treatment Timing | External | When in the infection timeline the phage therapy is initiated — early intervention targets smaller, less diverse bacterial populations while late intervention faces larger, potentially more resistant populations |
| Dosage Optimization | External | The calculated initial phage dose administered to the patient, which must be sufficient to establish a self-amplifying phage population before the immune system clears the therapeutic phages |

### Research for Lesson
- The Antibiotic Resistance Crisis — reference materials and textbook resources
- Bacteriophage Biology — reference materials and textbook resources
- Phage-Bacteria Co-Evolution: The Red Queen Hypothesis — reference materials and textbook resources
- Clinical Phage Therapy: From Compassionate Use to Precision Medicine — reference materials and textbook resources

---

## Step 1: LOCATE — Build Your System

### Text Editor

```
ENGINEERING A SUPERBUG KILLER

Optimizing Bacteriophage Therapy Against Antibiotic-Resistant Bacteria.
Antibiotics are failing. Can we engineer viruses to kill the superbugs that antibiotics can't?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Phage Specificity" — the engineered precision of the phage's targeting system — how well it distinguishes the pathogenic bacteria from beneficial microbiome species
  ○ Click "Treatment Timing" — when in the infection timeline the phage therapy is initiated — early intervention targets smaller
  ○ Click "Dosage Optimization" — the calculated initial phage dose administered to the patient
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Phage Population" — the total number of active bacteriophage particles in the patient's system
  ○ Click "Target Bacteria Population" — the count of pathogenic antibiotic-resistant bacteria causing the infection
  ○ Click "Bacterial Resistance Rate" — the speed at which the target bacterial population evolves resistance to the phage through mutations in surface receptor proteins
  ○ Click "Immune System Response" — the patient's innate and adaptive immune activity against both the infecting bacteria and the therapeutic phages — the immune system may clear phages before they complete their work
  ○ Click "Phage Replication Rate" — the number of new phage particles produced per lysis event (burst size) multiplied by the infection frequency — determines how fast the phage population amplifies in the presence of target bacteria
  ○ Click "Healthy Microbiome Impact" — the degree of collateral damage to beneficial gut bacteria caused by off-target phage activity — lower phage specificity increases microbiome disruption

Task B: ADD TO YOUR MODEL
• Click the PLUS (+) button to add each component to your picture
• You should now see 9 components on your canvas

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
"Antibiotics are failing. Can we engineer viruses to kill the superbugs that antibiotics can't?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Phage Population' — that's internal. The total number of active bacteriophage particles in the patient's system.
Click on 'Target Bacteria Population' — that's internal. The count of pathogenic antibiotic-resistant bacteria causing the infection.
Click on 'Phage Specificity' — that's external. The engineered precision of the phage's targeting system — how well it distinguishes the pathogenic bacteria from beneficial microbiome species.
Click on 'Bacterial Resistance Rate' — that's internal. The speed at which the target bacterial population evolves resistance to the phage through mutations in surface receptor proteins.
Click on 'Immune System Response' — that's internal. The patient's innate and adaptive immune activity against both the infecting bacteria AND the therapeutic phages — the immune system may clear phages before they complete their work.
Click on 'Phage Replication Rate' — that's internal. The number of new phage particles produced per lysis event (burst size) multiplied by the infection frequency — determines how fast the phage population amplifies in the presence of target bacteria.
Click on 'Healthy Microbiome Impact' — that's internal. The degree of collateral damage to beneficial gut bacteria caused by off-target phage activity — lower Phage Specificity increases microbiome disruption.
Click on 'Treatment Timing' — that's external. When in the infection timeline the phage therapy is initiated — early intervention targets smaller.
Click on 'Dosage Optimization' — that's external. The calculated initial phage dose administered to the patient.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Phage Specificity, Treatment Timing, and Dosage Optimization are external components because they represent parameters that clinicians and bioengineers directly control. Phage Specificity can be engineered through synthetic biology; Treatment Timing is a clinical decision; Dosage Optimization determines how many phages are initially administered. All other components — Phage Population, Target Bacteria Population, Bacterial Resistance Rate, Immune System Response, Phage Replication Rate, and Healthy Microbiome Impact — are internal biological responses that emerge from the dynamic interactions between phages, bacteria, and the patient's body.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next step, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 9 components sorted: Phage Specificity, Treatment Timing, Dosage Optimization (External), Phage Population, Target Bacteria Population, Bacterial Resistance Rate, Immune System Response, Phage Replication Rate, Healthy Microbiome Impact (Internal)]

### Graph
[Empty graph panel — no simulation yet]

---

## Step 2: ESTABLISH — Connect the Relationships

### Text Editor

```
TIME TO DRAW THE INVISIBLE LINES

Those 9 components don't just sit there — they AFFECT each other.
When one changes, others change too. Let's map those connections.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: OPEN CONNECTION MODE
• Click the "Connect" icon in the TOP LEFT corner of your screen
• Your cursor is now ready to draw relationship arrows

Task B: DRAW YOUR RELATIONSHIPS
• Click on "Dosage Optimization" and drag an arrow to "Phage Population"
• Click on "Phage Population" and drag an arrow to "Target Bacteria Population"
• Click on "Target Bacteria Population" and drag an arrow to "Phage Replication Rate"
• Click on "Phage Specificity" and drag an arrow to "Healthy Microbiome Impact"
• Click on "Target Bacteria Population" and drag an arrow to "Bacterial Resistance Rate"

Task C: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Dosage Optimization → Phage Population = POSITIVE (+)
    Higher initial phage dose establishes a larger starting Phage Population, increasing the probability that phages encounter and infect target bacteria before the immune system clears them.

  ○ Phage Population → Target Bacteria Population = NEGATIVE (−)
    More phages infecting and lysing target bacteria directly reduces the Target Bacteria Population through predator-prey dynamics.

  ○ Target Bacteria Population → Phage Replication Rate = POSITIVE (+)
    More abundant target bacteria provide more hosts for phage replication, increasing Phage Replication Rate — this is the self-amplifying nature of phage therapy.

  ○ Phage Specificity → Healthy Microbiome Impact = NEGATIVE (−)
    Higher Phage Specificity means the phages more precisely target only the pathogenic bacteria, reducing off-target damage to beneficial gut microbiome species.

  ○ Target Bacteria Population → Bacterial Resistance Rate = POSITIVE (+)
    Larger bacterial populations contain more genetic diversity through random mutation, increasing the probability that resistance-conferring mutations exist and are selected for under phage pressure.

Task D: CHECK YOUR MODEL
• You should have 5 arrows total
• 2 negative relationship(s), 3 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: Phage therapy has a remarkable feature: the treatment amplifies itself. Unlike antibiotics that degrade after administration, phages replicate inside the very bacteria they're killing. But the bacteria are evolving resistance in real time, and the patient's immune system may clear the phages. How do you optimize Dosage, Timing, and Specificity to win this three-way race?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Dosage Optimization' and drag an arrow
over to 'Phage Population.'

Here's the key question: When dosage optimization goes UP, does
phage population go UP or DOWN?

Higher initial phage dose establishes a larger starting Phage Population, increasing the probability that phages encounter and infect target bacteria before the immune system clears them.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Phage Population' and drag an arrow
over to 'Target Bacteria Population.'

Here's the key question: When phage population goes UP, does
target bacteria population go UP or DOWN?

More phages infecting and lysing target bacteria directly reduces the Target Bacteria Population through predator-prey dynamics.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Last connection: Click on 'Target Bacteria Population' and drag an arrow
over to 'Phage Replication Rate.'

Here's the key question: When target bacteria population goes UP, does
phage replication rate go UP or DOWN?

More abundant target bacteria provide more hosts for phage replication, increasing Phage Replication Rate — this is the self-amplifying nature of phage therapy.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Final connection: Click on 'Phage Specificity' and drag an arrow
over to 'Healthy Microbiome Impact.'

Here's the key question: When phage specificity goes UP, does
healthy microbiome impact go UP or DOWN?

Higher Phage Specificity means the phages more precisely target only the pathogenic bacteria, reducing off-target damage to beneficial gut microbiome species.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Target Bacteria Population' and drag an arrow
over to 'Bacterial Resistance Rate.'

Here's the key question: When target bacteria population goes UP, does
bacterial resistance rate go UP or DOWN?

Larger bacterial populations contain more genetic diversity through random mutation, increasing the probability that resistance-conferring mutations exist and are selected for under phage pressure.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Look at your model now. You've got 2 negative and 3
positive relationships. 5 arrows total.

Phage therapy has a remarkable feature: the treatment amplifies itself. Unlike antibiotics that degrade after administration, phages replicate inside the very bacteria they're killing. But the bacteria are evolving resistance in real time, and the patient's immune system may clear the phages. How do you optimize Dosage, Timing, and Specificity to win this three-way race?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Dosage Optimization +→ Phage Population, Phage Population −→ Target Bacteria Population, Target Bacteria Population +→ Phage Replication Rate, Phage Specificity −→ Healthy Microbiome Impact, Target Bacteria Population +→ Bacterial Resistance Rate]

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
• When Phage Specificity is HIGH, what happens to the internal components?

Task C: SCENARIO — STANDARD PROTOCOL
• Moderate dose, medium specificity, early treatment
• PREDICT FIRST: What do you predict happens to the Phage Population as it encounters a growing bacterial population?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task D: SCENARIO — DELAYED TREATMENT
• Late timing, established bacterial resistance
• PREDICT FIRST: What do you predict happens to the race between Phage Replication Rate and Bacterial Resistance Rate when treatment starts late?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task E: SCENARIO — OPTIMIZED COCKTAIL
• High specificity, high dose, early timing
• PREDICT FIRST: Do you predict that maximizing all three external parameters eliminates bacterial resistance evolution entirely?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Phage therapy is self-amplifying — phage populations grow exponentially when target bacteria are abundant, then decline naturally when the infection clears, making it inherently self-limiting
• Bacterial resistance to phages evolves rapidly but often comes with a fitness cost — resistant bacteria may lose virulence factors or become re-sensitized to antibiotics
• The immune system is both ally and obstacle — it helps clear the infection but may also neutralize therapeutic phages before they complete their work
• Treatment timing is critical because early intervention targets smaller, more genetically homogeneous populations that are less likely to contain pre-existing resistant mutants

THE ANSWER: Bacteriophage therapy works by exploiting the natural predator-prey relationship between viruses and bacteria. Unlike antibiotics, phages are self-amplifying — they reproduce inside the bacteria they kill, so the treatment literally grows as the infection grows. The optimization challenge is a three-way race: phages must kill bacteria faster than bacteria evolve resistance, while the patient's immune system tolerates the phages long enough for them to work. Engineering high-specificity phages, optimizing initial dosage, and treating early in the infection timeline are the key variables. Remarkably, when bacteria evolve resistance to phages, they often lose the very surface receptors that made them antibiotic-resistant in the first place — a phenomenon called phage-antibiotic synergy.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Standard Protocol. Moderate dose, medium specificity, early treatment.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Delayed Treatment.
Late timing, established bacterial resistance.

Before you run it — make a prediction. What do you predict happens to the race between Phage Replication Rate and Bacterial Resistance Rate when treatment starts late?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Optimized Cocktail. High specificity, high dose, early timing.
Do you predict that maximizing all three external parameters eliminates bacterial resistance evolution entirely?

Here's what our model reveals: Bacteriophage therapy works by exploiting the natural predator-prey relationship between viruses and bacteria. Unlike antibiotics, phages are self-amplifying — they reproduce inside the bacteria they kill, so the treatment literally grows as the infection grows. The optimization challenge is a three-way race: phages must kill bacteria faster than bacteria evolve resistance, while the patient's immune system tolerates the phages long enough for them to work. Engineering high-specificity phages, optimizing initial dosage, and treating early in the infection timeline are the key variables. Remarkably, when bacteria evolve resistance to phages, they often lose the very surface receptors that made them antibiotic-resistant in the first place — a phenomenon called phage-antibiotic synergy.

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
   • What happens if you turn OFF Phage Specificity?
   • What happens if you turn OFF Treatment Timing?
   • What happens if you turn OFF Dosage Optimization?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Phage-Antibiotic Synergy — The phenomenon where bacteria that evolve resistance to phages become re-sensitized to antibiotics, and vice versa — creating a therapeutic one-two punch
   • Biofilm Penetration — The ability of phages to penetrate bacterial biofilms — dense protective communities that antibiotics cannot reach — using phage-encoded depolymerase enzymes
   • Phage Engineering Level — The degree of genetic modification applied to the phage genome — from wild-type phages to CRISPR-enhanced phages with expanded host range and resistance-countering capabilities

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • The Antibiotic Resistance Crisis — how does this connect to your model?
   • Bacteriophage Biology — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model demonstrate the predator-prey dynamics between phages and bacteria?
   • Why is phage therapy described as 'self-amplifying' and how does this differ from antibiotic treatment?
   • What trade-offs did you discover between Phage Specificity and treatment speed?
   • How does natural selection drive bacterial resistance to phages, and why might this resistance come with a fitness cost?

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

Your model has 9 components. Real systems involve
way more. Think about...

Phage-Antibiotic Synergy. The phenomenon where bacteria that evolve resistance to phages become re-sensitized to antibiotics, and vice versa — creating a therapeutic one-two punch
How would you model that?

Biofilm Penetration. The ability of phages to penetrate bacterial biofilms — dense protective communities that antibiotics cannot reach — using phage-encoded depolymerase enzymes
How would you model that?

Phage Engineering Level. The degree of genetic modification applied to the phage genome — from wild-type phages to CRISPR-enhanced phages with expanded host range and resistance-countering capabilities
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

Phage Biologists and Phage Therapy Researchers develop bacteriophage treatments for antibiotic-resistant infections. They work for biotech startups, academic medical centers, and government agencies like DARPA, earning $75,000–$150,000/year. Synthetic Biologists who engineer phage genomes for therapeutic applications earn $100,000–$200,000/year.

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
Visual: Title slide with electron microscope images of phages attacking bacteria
Say: "Antibiotic-resistant bacteria killed 1.27 million people last year — more than HIV and malaria combined. The drugs are failing. But there's an ancient weapon we forgot about for 80 years: viruses that eat bacteria."
Do: Show the WHO antibiotic resistance infographic. Let students react to the death toll before introducing phages.
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and phage biology vocabulary
Say: "Today you're going to engineer a treatment protocol using something that's been killing bacteria for 3.5 billion years — bacteriophages. And you're going to optimize it using computational modeling."
Do: Pre-teach bacteriophage and antibiotic resistance. Show a 30-second phage lysis animation to establish the biological mechanism.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: Antibiotics are failing — can we engineer viruses to kill superbugs?
Say: "Every antibiotic we've ever invented, bacteria have evolved resistance to. Every single one. So why would phage therapy be any different — or would it?"
Do: Quick-write: Students predict whether bacteria can evolve resistance to phages and what might be different about viral versus chemical treatment. Share predictions.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps with phage therapy optimization context
Say: "We're going to optimize a living treatment — one that reproduces, evolves, and interacts with the patient's immune system in real time. This is nothing like designing a pill."
Do: Preview LEVER steps. Emphasize that phage therapy involves optimizing a dynamic biological system, not just finding the right dose.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Nine component cards spanning phage, bacteria, and patient biology
Say: "Three of these components are under the doctor's control. Six are determined by biology and evolution. Which is which — and why does that distinction matter?"
Do: Guide sorting of external versus internal components. Discuss why Phage Specificity is controllable through engineering but Bacterial Resistance Rate is not.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Complex relationship web showing predator-prey dynamics and evolutionary feedback
Say: "This model has something none of our previous models had: the treatment reproduces inside the disease. Trace what happens when phages meet bacteria."
Do: Students map the self-amplifying feedback loop. Identify the three-way race between phage replication, bacterial resistance, and immune clearance.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Population dynamics graphs and optimization dashboards
Say: "You're the biotech engineer. Find the combination of specificity, timing, and dosage that clears the infection. But watch what evolution does in real time."
Do: Students predict outcomes, then run all three scenarios. Track bacterial clearance rate, resistance emergence, and microbiome impact as key metrics.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key findings about optimization and evolutionary trade-offs
Say: "Here's the twist: when bacteria evolve resistance to phages, they sometimes lose their antibiotic resistance. The phage forces them into an evolutionary trap. This is phage-antibiotic synergy — and your model just predicted it."
Do: Connect model findings to the real evolutionary trade-off in phage therapy. Discuss how this changes the treatment strategy.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Personalized phage therapy protocol design challenge
Say: "A patient walks into your phage therapy clinic with an infection that no antibiotic can touch. Design their treatment protocol."
Do: Groups design personalized protocols including phage selection, cocktail composition, timing, dosage, and resistance monitoring. Present and defend.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: Engineering a Superbug Killer
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
This lesson introduces students to predictive modeling and optimization in the context of bacteriophage therapy — one of the most promising alternatives to antibiotics. Biotech skill focus: Predictive modeling and optimization. With antibiotic resistance killing over 1.27 million people annually and the pipeline for new antibiotics nearly dry, phage therapy represents a paradigm shift in infectious disease treatment that students must understand.

NGSS ALIGNMENT:
HS-LS1-2, HS-LS4-2: Develop and use a model to illustrate the hierarchical organization of interacting systems that provide specific functions within multicellular organisms; construct an explanation based on evidence that the process of evolution primarily results from natural selection.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Constructing Explanations and Designing Solutions
  Students construct evidence-based explanations of phage-bacteria co-evolution and design optimized therapeutic protocols using model-derived data.
• Disciplinary Core Idea: LS1.A Structure and Function / LS4.B Natural Selection
  Organisms have complex hierarchical structures that determine function; natural selection acts on heritable variation, driving bacterial resistance evolution under phage pressure.
• Crosscutting Concept: Cause and Effect / Stability and Change
  Students analyze the causal chain from phage infection to bacterial lysis to resistance evolution, and identify conditions that shift the system toward treatment success or failure.

PACING GUIDE:
• Step 1 (Locate): 8-10 minutes
• Step 2 (Establish): 8-10 minutes
• Step 3 (Visualize & Evaluate): 10-12 minutes
• Step 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Bacteriophage, Antibiotic Resistance, Phage Specificity, Microbiome
□ Prepare Antibiotics are failing. Can we engineer viruses to kill the superbugs that antibiotics can't discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify nine components spanning phage biology, bacterial evolution, immune response, and treatment parameters — including three externally controllable variables (Phage Specificity, Treatment Timing, Dosage Optimization) and six internal dynamic responses.
• Establish: Students determine that Dosage Optimization establishes the initial Phage Population, which interacts with Target Bacteria Population through predator-prey dynamics while Bacterial Resistance Rate and Immune System Response work against the therapy — and that Phage Specificity controls the trade-off between targeting precision and Healthy Microbiome Impact.
• Visualize: Students build a computational model showing the three-way race between phage replication, bacterial resistance evolution, and immune clearance, with treatment outcome determined by which process dominates.
• Evaluate: Students run standard, delayed-treatment, and optimized-cocktail scenarios to identify the parameter combinations that maximize bacterial clearance while minimizing resistance emergence and microbiome damage.
• Revise: Students add Phage-Antibiotic Synergy, Biofilm Penetration, or Phage Engineering Level to explore advanced therapeutic strategies.

BACKGROUND CONTENT:
• The Antibiotic Resistance Crisis:
  Antibiotic-resistant bacteria kill more people than HIV/AIDS or malaria. The WHO has declared antimicrobial resistance one of the top 10 global public health threats. Resistance arises through natural selection: when antibiotics are used, susceptible bacteria die while naturally resistant mutants survive and reproduce. Hospitals harbor 'superbugs' like MRSA (methicillin-resistant Staphylococcus aureus), CRE (carbapenem-resistant Enterobacteriaceae), and extensively drug-resistant tuberculosis that are resistant to nearly all available antibiotics. The pharmaceutical industry has largely abandoned antibiotic development because it's not profitable — a new antibiotic costs $1-2 billion to develop and is used sparingly (to prevent resistance), generating far less revenue than drugs taken daily for chronic conditions.

• Bacteriophage Biology:
  Bacteriophages are viruses that exclusively infect bacteria — they cannot infect human cells because they require bacterial surface receptors for attachment. Phages follow a lytic cycle: (1) attachment to specific bacterial surface receptors, (2) injection of phage DNA into the bacterium, (3) hijacking of bacterial protein synthesis machinery to produce new phage components, (4) assembly of 50-200 new phage particles inside the cell, (5) lysis — the bacterial cell bursts, releasing new phages to infect more bacteria. This specificity is both a strength (precision targeting) and a challenge (each phage only kills specific bacterial strains). Phage cocktails — mixtures of multiple phage types — address this limitation.

• Phage-Bacteria Co-Evolution: The Red Queen Hypothesis:
  Bacteria and phages have been co-evolving for 3.5 billion years in the longest-running arms race on Earth. Bacteria evolve phage resistance primarily by modifying surface receptors (so phages can't attach), producing restriction enzymes (that cut foreign DNA), or using CRISPR-Cas systems (bacterial immune memory). But resistance often comes at a cost: the surface receptors that phages use for attachment are frequently the same receptors bacteria use for virulence or antibiotic resistance. When bacteria modify these receptors to escape phages, they may lose their antibiotic resistance — a phenomenon called 'phage-antibiotic synergy' or 'evolutionary trade-offs.' This creates a therapeutic strategy: use phages to force bacteria into an evolutionary corner where they become vulnerable to antibiotics again.

• Clinical Phage Therapy: From Compassionate Use to Precision Medicine:
  Phage therapy has been used clinically in the Republic of Georgia for over 100 years, but Western medicine largely abandoned it when antibiotics were discovered. Now, with antibiotics failing, phage therapy is experiencing a renaissance. The FDA has approved compassionate-use phage therapy for patients with untreatable infections. Notable cases include Tom Patterson (2016), who survived a multi-drug-resistant Acinetobacter infection after personalized phage therapy when all antibiotics failed. Modern phage therapy uses genomic sequencing to match phages to patient-specific bacterial strains, synthetic biology to engineer phages with expanded host ranges, and computational models to optimize dosing and treatment timing. The challenge is that each treatment is essentially a custom-designed biological product — very different from mass-produced antibiotic pills.

COMMON MISCONCEPTIONS:
• "Phages are dangerous because they're viruses"
  Reality: Bacteriophages CANNOT infect human cells — period. They require specific bacterial surface receptors that human cells do not have. Phages have been part of the human microbiome since birth; you carry approximately 10^12 phages in your gut right now. They are the most abundant biological entities on Earth and have never caused a human infection. The word 'virus' triggers fear, but phages are fundamentally different from human-infecting viruses.
  Strategy: Ask: What would a phage need to infect a human cell? It would need to recognize human surface receptors — but phage tail proteins evolved over 3.5 billion years to recognize BACTERIAL receptors. That's like trying to use a USB-C cable to charge a gas-powered car.

• "Bacteria can become resistant to everything eventually"
  Reality: While bacteria can evolve resistance to any single selective pressure, resistance always comes at a cost. The model shows that phage resistance often requires modifying surface receptors that serve other essential functions. Phage cocktails (multiple phages targeting different receptors) make it exponentially harder for bacteria to evolve resistance to ALL phages simultaneously — the same principle behind HIV combination therapy.
  Strategy: Calculate: If resistance to one phage occurs at a rate of 1 in 10^6, what's the probability of simultaneous resistance to three phages targeting different receptors? 1 in 10^18 — more bacteria than exist in the patient.

• "We should just develop new antibiotics instead"
  Reality: New antibiotic development has nearly stopped because it's economically unviable — $1-2 billion to develop a drug that's used sparingly and becomes obsolete when resistance emerges. Only 2 new antibiotic classes have been discovered in the last 50 years. Phage therapy offers a fundamentally different approach: instead of chemical warfare against bacteria, it uses a co-evolved biological weapon that adapts alongside its target.
  Strategy: Discuss: Why would a pharmaceutical company prefer to develop a blood pressure medication taken daily for life versus an antibiotic taken for 10 days? Follow the money.

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
Big Question: Antibiotics are failing. Can we engineer viruses to kill the superbugs that antibiotics can't?
Answer: Bacteriophage therapy works by exploiting the natural predator-prey relationship between viruses and bacteria. Unlike antibiotics, phages are self-amplifying — they reproduce inside the bacteria they kill, so the treatment literally grows as the infection grows. The optimization challenge is a three-way race: phages must kill bacteria faster than bacteria evolve resistance, while the patient's immune system tolerates the phages long enough for them to work. Engineering high-specificity phages, optimizing initial dosage, and treating early in the infection timeline are the key variables. Remarkably, when bacteria evolve resistance to phages, they often lose the very surface receptors that made them antibiotic-resistant in the first place — a phenomenon called phage-antibiotic synergy.

Simulation Answers:
• Standard Protocol Scenario: With moderate dosage, medium specificity, and early treatment, the Phage Population quickly amplifies using the smaller bacterial population as hosts. Target Bacteria Population drops sharply as phage predation outpaces bacterial reproduction. Bacterial Resistance Rate increases modestly but remains manageable because the population was small at treatment onset. Immune System Response clears remaining phages after bacteria are depleted. Healthy Microbiome Impact is moderate due to medium specificity.
• Optimized Cocktail Scenario: With high specificity, high dose, and early timing, the initial Phage Population is large enough to rapidly overwhelm the bacterial population before significant resistance can evolve. High Phage Specificity dramatically reduces Healthy Microbiome Impact. The key insight is that early timing prevents the bacterial population from reaching the size where resistance-conferring mutations become statistically likely. However, even under optimal conditions, some resistance evolution is observed — the arms race is never fully won.

Reflection Exemplars:
• Q: Why is phage therapy described as self-amplifying?
  A: Unlike antibiotics — which are administered at a fixed dose and steadily degrade — phages reproduce inside the bacteria they kill. Each lysis event releases 50-200 new phage particles that immediately seek new bacterial hosts. The model shows that Phage Population can increase exponentially when Target Bacteria Population is high, creating a self-reinforcing treatment cycle. When bacteria are eliminated, phages lose their reproduction substrate and the population naturally declines. This makes phage therapy inherently self-limiting — the treatment stops when the infection stops.
• Q: How does natural selection create the resistance trade-off?
  A: The model shows Bacterial Resistance Rate increasing under phage pressure as natural selection favors mutants with modified surface receptors. But these surface receptors serve other bacterial functions — they may be the same proteins used for nutrient uptake, antibiotic efflux, or virulence. When bacteria modify these receptors to escape phages, they may lose these other capabilities. This is the evolutionary trade-off: resistance to phages comes at the cost of fitness in other dimensions, potentially re-sensitizing the bacteria to antibiotics.

STEM CHALLENGE GUIDANCE:
Title: Design a Personalized Phage Therapy Protocol
Mission: Design a treatment protocol that matches engineered phage cocktails to specific patient infections, optimizing timing, dosage, and specificity for maximum effectiveness.
Scenario: A biotech startup is developing a phage therapy clinic for patients with antibiotic-resistant infections. Each patient's infection is different — different bacterial strains, different resistance profiles, different immune status. Your team must design the decision-making protocol that determines which phages to use, when to start treatment, and how to adjust the approach if resistance emerges.
Introduction: Present the challenge: A biotech startup is opening a phage therapy clinic for patients with untreatable antibiotic-resistant infections. Each patient's infection is unique. Your team must design the clinical decision-making protocol — from bacterial strain identification through phage selection to treatment monitoring and resistance management.

Key Concepts:
• Personalized Phage Selection: Unlike mass-produced antibiotics, phage therapy can be customized to each patient's specific bacterial infection. Rapid genome sequencing identifies the pathogen; phage libraries are screened for activity; cocktails of 3-5 complementary phages are assembled to reduce resistance risk.
• Treatment Monitoring: Phage therapy requires real-time monitoring of bacterial counts (are they decreasing?), phage titers (are phages replicating?), resistance markers (are bacteria evolving escape?), and patient inflammatory markers (is the immune system interfering?). Computational models predict expected trajectories and flag deviations.
• Resistance Management Strategy: The 'phage-antibiotic synergy' strategy deliberately uses phage therapy to force bacteria to evolve in predictable directions — trading phage resistance for antibiotic susceptibility — then follows up with targeted antibiotics to eliminate the now-vulnerable population.

Evaluation Rubric:
• Expert (4): Protocol includes systematic phage selection, cocktail design rationale, monitoring schedule with specific biomarkers, resistance contingency plan with phage-antibiotic synergy strategy, and model-derived evidence
• Proficient (3): Protocol includes phage selection, monitoring, and basic resistance management based on model findings
• Developing (2): Protocol covers basic treatment steps but lacks monitoring detail or resistance contingency planning
• Beginning (1): Protocol is incomplete or does not connect treatment decisions to the population dynamics model

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a simplified phage lytic cycle diagram showing the five steps from attachment to lysis
  • Use predator-prey graph templates (Lotka-Volterra style) where students can sketch predicted population trajectories before simulating
  • Scaffold evolutionary thinking: 'If phages kill all bacteria EXCEPT those with ___ mutation, what happens to the next generation?'

Extensions (Advanced Learners):
  • Research the Tom Patterson case — the first FDA-approved compassionate-use phage therapy in the US — and analyze what made his treatment protocol successful
  • Investigate how CRISPR-enhanced phages are being engineered to overcome bacterial defense systems and expand host range
  • Compare the economic models of phage therapy (personalized per patient) versus antibiotics (mass produced) and debate which is more sustainable

Cross-Curricular Connections:
  • Math: Model phage-bacteria population dynamics using Lotka-Volterra predator-prey equations and compare mathematical predictions to simulation results
  • ELA: Research and write a feature article for a science magazine explaining why phage therapy, abandoned 80 years ago, is making a comeback in the antibiotic resistance crisis
  • Social Studies: Investigate why phage therapy thrived in the Soviet Union/Georgia while the West pursued antibiotics — how do political and economic systems shape scientific priorities?

CAST ALIGNMENT:
• Model the population dynamics of bacteriophage-bacteria interactions including immune system interference and resistance evolution
• Optimize phage therapy treatment parameters (timing, dosage, specificity) to maximize pathogen clearance while preserving microbiome health
• Analyze how natural selection drives real-time bacterial resistance to therapeutic phages and evaluate counter-strategies

CAST-Style Assessment Questions:
• Multiple Choice: A patient's phage therapy is started 5 days after infection instead of 1 day. Based on your model, which outcome is most likely and why?
• Constructed Response: Using your model, explain the 'arms race' between bacteriophages and bacteria. Why does bacterial resistance to phages sometimes make the bacteria more vulnerable to antibiotics? Reference at least three model components.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: Engineering a Superbug Killer
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Why are antibiotic-resistant bacteria considered one of the greatest threats to human health in the 21st century?

   _________________________________________________________

   _________________________________________________________

2. What is a bacteriophage and how is it different from the viruses that make humans sick?

   _________________________________________________________

   _________________________________________________________

3. Draw a diagram showing how you think a virus could be used as a medical treatment instead of a disease.

   [DRAWING BOX]

4. What do you think happens when bacteria evolve resistance to a treatment — does the bacteria 'decide' to become resistant?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Bacteriophage                 
___ Antibiotic Resistance         
___ Phage Specificity             
___ Microbiome                    

A. A virus that exclusively infects and kills bacteria by injecting its genetic material, hijacking the cell's machinery to produce copies of itself, and bursting the cell open — the most abundant biological entity on Earth with over 10^31 phages globally
B. The evolved ability of bacteria to survive exposure to antibiotics through mechanisms like drug efflux pumps, enzyme degradation of the drug, or target site modification — driven by natural selection under antibiotic pressure
C. The precision with which a bacteriophage targets a particular bacterial species or strain, determined by the molecular fit between phage tail proteins and bacterial surface receptors — high specificity means fewer collateral effects on beneficial bacteria
D. The complex community of trillions of bacteria, archaea, fungi, and viruses living in and on the human body — particularly dense in the gut — that plays critical roles in digestion, immunity, vitamin synthesis, and mental health

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

SCENARIO: Standard Protocol
Settings: Moderate dose, medium specificity, early treatment
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Delayed Treatment
Settings: Late timing, established bacterial resistance
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Optimized Cocktail
Settings: High specificity, high dose, early timing
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

1. How does your model demonstrate the predator-prey dynamics between phages and bacteria?

   _________________________________________________________

   _________________________________________________________

2. Why is phage therapy described as 'self-amplifying' and how does this differ from antibiotic treatment?

   _________________________________________________________

   _________________________________________________________

3. What trade-offs did you discover between Phage Specificity and treatment speed?

   _________________________________________________________

   _________________________________________________________

4. How does natural selection drive bacterial resistance to phages, and why might this resistance come with a fitness cost?

   _________________________________________________________

   _________________________________________________________

5. What are the limitations of modeling phage therapy with nine components when real infections involve thousands of bacterial strains and immune factors?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Antibiotics are failing. Can we engineer viruses to kill the superbugs that antibiotics can't? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Constructing Explanations and Designing Solutions
   □ Disciplinary Core Idea: LS1.A Structure and Function / LS4.B Natural Selection
   □ Crosscutting Concept: Cause and Effect / Stability and Change

3. What are the limitations of modeling phage therapy with nine components when real infections involve thousands of bacterial strains and immune factors?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Personalized Phage Therapy Protocol
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design a treatment protocol that matches engineered phage cocktails to specific patient infections, optimizing timing, dosage, and specificity for maximum effectiveness.

SCENARIO: A biotech startup is developing a phage therapy clinic for patients with antibiotic-resistant infections. Each patient's infection is different — different bacterial strains, different resistance profiles, different immune status. Your team must design the decision-making protocol that determines which phages to use, when to start treatment, and how to adjust the approach if resistance emerges.

GUIDING QUESTIONS:
• How would you rapidly identify which phages are effective against a specific patient's bacterial infection?
• What patient factors would you assess before designing the treatment protocol?
• How would you monitor treatment progress and detect emerging phage resistance?

DESIGN THINKING:
• Would you use a single phage or a cocktail of multiple phages — and what are the trade-offs?

  _________________________________________________________

• How would you sequence phage therapy with existing antibiotic treatments?

  _________________________________________________________

• What backup strategies would you include if the first phage cocktail encounters resistance?

  _________________________________________________________

• How would you ensure phage specificity is high enough to protect the patient's microbiome?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Protocol includes systematic phage selection, cocktail design rationale, monitoring schedule with specific biomarkers, resistance contingency plan with phage-antibiotic synergy strategy, and model-derived evidence
• Proficient (3): Protocol includes phage selection, monitoring, and basic resistance management based on model findings
• Developing (2): Protocol covers basic treatment steps but lacks monitoring detail or resistance contingency planning
• Beginning (1): Protocol is incomplete or does not connect treatment decisions to the population dynamics model

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CAST-Aligned Pre/Post Assessment

### Administration Instructions

These 5 multiple-choice questions are administered identically as both a pre-assessment (before Activity 1) and a post-assessment (after Activity 4). Score each out of 5. Learning growth = post-score minus pre-score.

Questions follow the California Science Test (CAST) stimulus-response format. Each item is three-dimensional, assessing a Science and Engineering Practice (SEP), Disciplinary Core Idea (DCI), and Crosscutting Concept (CCC) simultaneously, aligned to HS-LS1-2, HS-LS4-2.

---

### Question 1

CAST Alignment: SEP 2.1.1 (Determine components of a system) + DCI LS1.2 + CCC4 (Systems and System Models)

A student is using the ModelIt platform to study the system in this lesson. The model includes these components: Phage Population, Target Bacteria Population, Phage Specificity, Bacterial Resistance Rate, Immune System Response, Phage Replication Rate, Healthy Microbiome Impact, Treatment Timing, Dosage Optimization. Some components are external (Phage Specificity, Treatment Timing, Dosage Optimization) and some are internal (Phage Population, Target Bacteria Population, Bacterial Resistance Rate, Immune System Response, Phage Replication Rate, Healthy Microbiome Impact). The student needs to understand what each component represents and how they are organized.

In a phage therapy model, a student observes that increasing initial Phage Dosage leads to faster bacterial clearance, but the effect plateaus after a certain dose. Which explanation BEST accounts for this plateau?

A. Phages are self-amplifying, so once enough phages establish successful infections, additional initial phages are redundant because the population grows exponentially from bacterial lysis
B. The immune system destroys all phages above a certain concentration
C. Bacteria become instantly resistant when phage concentration is too high
D. Higher doses are always toxic to the patient

Correct Answer: A

Feedback: Correct. Because phage therapy is self-amplifying (each lysed bacterium releases 50-200 new phages), the initial dose only needs to be large enough to establish productive infections. Beyond that threshold, the phage population grows exponentially regardless of the starting dose. If you chose D, look at the evidence from the model. The correct answer (A) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose B, this reflects a common misconception. Matter cannot be created or destroyed — it can only change form. The total amount of matter in the system stays the same. If you chose C, look at the evidence from the model. The correct answer (A) is supported by the relationships between components. This answer does not match what the simulation data shows.
---

### Question 2

CAST Alignment: SEP 2.1.2 (Determine relationships among components) + DCI LS1.2 + CCC4 (Systems and System Models)

In the computational model for this lesson, a student draws arrows between components to show relationships. The model shows that when Dosage Optimization increases, Phage Population increases; when Phage Population increases, Target Bacteria Population decreases. The student is trying to understand why these relationships are positive or negative.

A model simulation shows that when Treatment Timing is delayed from Day 1 to Day 5 of infection, the probability of treatment failure increases dramatically. Which factor MOST directly explains this finding?

A. The patient's immune system becomes too weak to support phage therapy after 5 days
B. The infection has already caused irreversible organ damage by Day 5
C. A larger, more genetically diverse bacterial population is more likely to contain pre-existing resistance mutations that natural selection can amplify
D. Phages lose their effectiveness after being stored for 5 days

Correct Answer: C

Feedback: Correct. As bacterial populations grow, they accumulate genetic diversity through random mutation. A population of 10 billion bacteria is far more likely to contain individuals with phage-resistant mutations than a population of 10,000. Natural selection rapidly amplifies these resistant mutants under phage pressure. If you chose A, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose B, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows.
---

### Question 3

CAST Alignment: SEP 2.1.3 (Evaluate a model's accuracy) + DCI LS1.2 + CCC4 (Systems and System Models)

A student runs a simulation of the model. The model shows that when Dosage Optimization increases, Phage Population increases and when Phage Population increases, Target Bacteria Population decreases and when Target Bacteria Population increases, Phage Replication Rate increases. The student changes one variable to see how the whole system responds.

A researcher observes that bacteria which evolve resistance to a phage by modifying their surface receptors simultaneously become susceptible to an antibiotic they were previously resistant to. This phenomenon is BEST explained by which concept?

A. The antibiotic was reformulated to be more effective against the mutant strain
B. Horizontal gene transfer from phage DNA to bacterial DNA
C. Genetic linkage, where the resistance and susceptibility genes are on the same chromosome
D. Evolutionary trade-offs, where the surface receptors used for phage attachment are the same receptors that confer antibiotic resistance, so modifying them costs both functions

Correct Answer: D

Feedback: Correct. This is phage-antibiotic synergy. Surface receptor proteins often serve multiple functions. When bacteria modify a receptor to block phage attachment, they may lose the efflux pump or structural feature that made them antibiotic-resistant. Evolution forces a trade-off between two survival strategies. If you chose C, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose B, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose A, this answer suggests something is being added to the system. Look carefully at the model — the total amount stays the same even when components change. The system is conserving matter or energy.
---

### Question 4

CAST Alignment: SEP 2.1.4 (Represent mechanisms to explain/predict events) + DCI LS1.2 + CCC4 (Systems and System Models)

Scientists are studying data related to this system. They collected observations over time and noticed patterns in how the components change. The data shows how changes in one part of the system cascade through the other parts.

A phage therapy optimization model includes both Phage Specificity and Healthy Microbiome Impact as components. A student increases Phage Specificity to its maximum value. What is the MOST LIKELY effect on Healthy Microbiome Impact?

A. Healthy Microbiome Impact decreases because highly specific phages only target the pathogenic strain and leave beneficial bacteria unharmed
B. Healthy Microbiome Impact increases because more specific phages are more potent
C. Healthy Microbiome Impact remains the same because the microbiome is immune to phages
D. There is no relationship between specificity and microbiome impact

Correct Answer: A

Feedback: Correct. Phage Specificity and Healthy Microbiome Impact have a negative relationship. Higher specificity means the phage more precisely distinguishes between pathogenic bacteria and beneficial microbiome species, resulting in less collateral damage to the gut ecosystem. If you chose B, this answer suggests something is being added to the system. Look carefully at the model — the total amount stays the same even when components change. The system is conserving matter or energy. If you chose D, the model shows these components ARE connected. When one changes, it affects the others through the relationships (positive or negative) that you mapped in the model. If you chose C, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows.
---

### Question 5

CAST Alignment: SEP 2.1.5 (Apply a model to make predictions) + DCI LS1.2 + CCC4 (Systems and System Models)

A team wants to use the model to solve a real-world problem related to this system. They know they cannot control the external components (Phage Specificity, Treatment Timing, Dosage Optimization), but they can take action on internal components (Phage Population, Target Bacteria Population, Bacterial Resistance Rate, Immune System Response, Phage Replication Rate, Healthy Microbiome Impact). They need to decide which action would be most effective based on what the model shows.

A clinical team is designing a phage cocktail containing three different phages, each targeting a different surface receptor on the same pathogenic bacterium. What is the PRIMARY advantage of this multi-phage approach over using a single phage type?

A. Using three phages reduces the immune system's response to the treatment
B. The probability of simultaneous resistance to all three phages is exponentially lower than resistance to any single phage, making treatment failure far less likely
C. Three phages kill bacteria three times faster than one phage
D. Different phages target different organs in the body, increasing tissue coverage

Correct Answer: B

Feedback: Correct. If resistance to one phage occurs at a rate of 1 in 10^6, simultaneous resistance to three independent phages targeting different receptors occurs at approximately 1 in 10^18. This combinatorial principle is the same logic behind HIV combination therapy and makes resistance evolution astronomically unlikely. If you chose C, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose A, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows.
---

### Answer Key

Question 1: A (Cognitive Level: Identify — SEP 2.1.1, DCI LS1.2, CCC4)
Question 2: C (Cognitive Level: Reason — SEP 2.1.2, DCI LS1.2, CCC4)
Question 3: D (Cognitive Level: Reason — SEP 2.1.3, DCI LS1.2, CCC4)
Question 4: A (Cognitive Level: Reason + Evidence — SEP 2.1.4, DCI LS1.2, CCC4)
Question 5: B (Cognitive Level: Predict + Apply — SEP 2.1.5, DCI LS1.2, CCC4)


## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-09/G09L3-L02/G09L3-L02-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-09/G09L3-L02/G09L3-L02-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-09/G09L3-L02/G09L3-L02-Student-Presentation.pptx] |
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