# Lesson: Can CRISPR Cure Genetic Diseases?

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G11L3-L01 |
| **Grade** | 11th Grade — Level 3: Systems Innovation Lab |
| **Lesson Name** | Can CRISPR Cure Genetic Diseases? |
| **Status** | Template |

---

## Platform

### Title
**Can CRISPR Cure Genetic Diseases? — Modeling Gene Editing Precision, Off-Target Effects, and Ethical Boundaries**

### Overview
CRISPR-Cas9 is the most transformative biological technology since the discovery of DNA's structure in 1953. Derived from an ancient bacterial immune system, it allows scientists to edit any gene in any organism with unprecedented precision. In 2023, the FDA approved the first CRISPR-based therapy (Casgevy) for sickle cell disease, marking the beginning of the gene editing era in medicine. But the power to rewrite the code of life raises questions that science alone cannot answer. Students investigate the driving question: Could we rewrite the code of life to eliminate genetic disease — and should we? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of a DNA double helix being precisely edited by a glowing CRISPR molecular tool with subtle blue and gold light effects, a futuristic laboratory background, featuring a diverse multicultural group with Black people centered of 16-17 year old students observing the molecular visualization on advanced holographic displays]

### Grade
11th Grade — Level 3: Systems Innovation Lab

### NGSS Standard
**HS-LS3-1, HS-LS3-2**: Ask questions to clarify relationships about the role of DNA and chromosomes in coding the instructions for characteristic traits passed from parents to offspring. Make and defend a claim based on evidence that inheritable genetic variations may result from new genetic combinations through meiosis, viable errors occurring during replication, or mutations caused by environmental factors.

### Learning Objectives
- Model how the CRISPR-Cas9 system identifies and edits specific DNA sequences with varying degrees of precision
- Analyze the relationship between guide RNA specificity, off-target editing frequency, and unintended genomic consequences
- Evaluate the trade-offs between therapeutic benefit and biological risk when editing human germline versus somatic cells
- Predict how changes in editing parameters affect the probability of successful disease correction versus harmful mutations

### Component List (Starting Model: 7 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Guide RNA Specificity | External | The degree to which the guide RNA matches only the intended target sequence and not similar sequences elsewhere in the genome — higher specificity means fewer off-target cuts |
| Cas9 Cutting Efficiency | Internal | The percentage of cells in which the Cas9 enzyme successfully makes a double-strand break at the target site — affected by chromatin accessibility, guide RNA design, and delivery method |
| Off-Target Edit Rate | Internal | The frequency at which Cas9 cuts DNA at unintended genomic locations — even a 0.1% off-target rate can affect millions of base pairs across the 3.2 billion base-pair human genome |
| Repair Pathway Selection | Internal | The cellular mechanism activated after Cas9 cuts DNA — either precise homology-directed repair that inserts the correct sequence, or error-prone non-homologous end joining that introduces random insertions or deletions |
| Delivery Efficiency | External | The percentage of target cells that successfully receive the CRISPR components — viral vectors, lipid nanoparticles, and electroporation each have different efficiency and safety profiles |
| Therapeutic Benefit | Internal | The measurable improvement in disease symptoms resulting from successful gene correction — depends on what percentage of cells are correctly edited and how critical the affected gene is |
| Unintended Mutations | Internal | Novel genetic changes introduced by imprecise repair, off-target cuts, or large-scale chromosomal rearrangements that were not present before editing — some may be harmless, others potentially oncogenic |

### Research for Lesson
- How CRISPR-Cas9 Works — reference materials and textbook resources
- The Off-Target Problem — reference materials and textbook resources
- Somatic vs. Germline: The Ethical Divide — reference materials and textbook resources
- Current Clinical Applications — reference materials and textbook resources

---

## Activity 1: LOCATE — Build Your System

### Text Editor

```
CAN CRISPR CURE GENETIC DISEASES?

Modeling Gene Editing Precision, Off-Target Effects, and Ethical Boundaries.
Could we rewrite the code of life to eliminate genetic disease — and should we?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Guide RNA Specificity" — the degree to which the guide rna matches only the intended target sequence and not similar sequences elsewhere in the genome — higher specificity means fewer off-target cuts
  ○ Click "Delivery Efficiency" — the percentage of target cells that successfully receive the crispr components — viral vectors
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Cas9 Cutting Efficiency" — the percentage of cells in which the cas9 enzyme successfully makes a double-strand break at the target site — affected by chromatin accessibility
  ○ Click "Off-Target Edit Rate" — the frequency at which cas9 cuts dna at unintended genomic locations — even a 0
  ○ Click "Repair Pathway Selection" — the cellular mechanism activated after cas9 cuts dna — either precise homology-directed repair that inserts the correct sequence
  ○ Click "Therapeutic Benefit" — the measurable improvement in disease symptoms resulting from successful gene correction — depends on what percentage of cells are correctly edited and how critical the affected gene is
  ○ Click "Unintended Mutations" — novel genetic changes introduced by imprecise repair

STEP 2: ADD TO YOUR MODEL
• Click the PLUS (+) button to add each component to your picture
• You should now see 7 components on your canvas

STEP 3: SORT YOUR COMPONENTS
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
"Could we rewrite the code of life to eliminate genetic disease — and should we?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Guide RNA Specificity' — that's external. The degree to which the guide RNA matches only the intended target sequence and not similar sequences elsewhere in the genome — higher specificity means fewer off-target cuts.
Click on 'Cas9 Cutting Efficiency' — that's internal. The percentage of cells in which the Cas9 enzyme successfully makes a double-strand break at the target site — affected by chromatin accessibility.
Click on 'Off-Target Edit Rate' — that's internal. The frequency at which Cas9 cuts DNA at unintended genomic locations — even a 0.
Click on 'Repair Pathway Selection' — that's internal. The cellular mechanism activated after Cas9 cuts DNA — either precise homology-directed repair that inserts the correct sequence.
Click on 'Delivery Efficiency' — that's external. The percentage of target cells that successfully receive the CRISPR components — viral vectors.
Click on 'Therapeutic Benefit' — that's internal. The measurable improvement in disease symptoms resulting from successful gene correction — depends on what percentage of cells are correctly edited and how critical the affected gene is.
Click on 'Unintended Mutations' — that's internal. Novel genetic changes introduced by imprecise repair.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Guide RNA Specificity is external because it represents the engineered design variable that scientists directly control — they can modify the guide RNA sequence, length, and chemical modifications to tune precision. Delivery Efficiency is external because it represents the choice of delivery technology and dosing that researchers select. The remaining five components are internal: Cas9 Cutting Efficiency responds to guide RNA binding and chromatin state, Off-Target Edit Rate is a consequence of specificity interacting with the genome, Repair Pathway Selection is determined by cellular biology, and Therapeutic Benefit and Unintended Mutations are the downstream outcomes of all upstream variables.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next activity, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 7 components sorted: Guide RNA Specificity, Delivery Efficiency (External), Cas9 Cutting Efficiency, Off-Target Edit Rate, Repair Pathway Selection, Therapeutic Benefit, Unintended Mutations (Internal)]

### Graph
[Empty graph panel — no simulation yet]

---

## Activity 2: ESTABLISH — Connect the Relationships

### Text Editor

```
TIME TO DRAW THE INVISIBLE LINES

Those 7 components don't just sit there — they AFFECT each other.
When one changes, others change too. Let's map those connections.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: OPEN CONNECTION MODE
• Click the "Connect" icon in the TOP LEFT corner of your screen
• Your cursor is now ready to draw relationship arrows

STEP 2: DRAW YOUR RELATIONSHIPS
• Click on "Guide RNA Specificity" and drag an arrow to "Off-Target Edit Rate"
• Click on "Delivery Efficiency" and drag an arrow to "Cas9 Cutting Efficiency"
• Click on "Off-Target Edit Rate" and drag an arrow to "Unintended Mutations"
• Click on "Cas9 Cutting Efficiency" and drag an arrow to "Therapeutic Benefit"

STEP 3: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Guide RNA Specificity → Off-Target Edit Rate = NEGATIVE (−)
    Higher guide RNA specificity means the guide RNA binds ONLY to the intended target and not to similar sequences — reducing off-target cuts. Lower specificity allows binding at multiple genomic locations, increasing unintended edits.

  ○ Delivery Efficiency → Cas9 Cutting Efficiency = POSITIVE (+)
    Higher delivery efficiency means more cells receive the CRISPR components, increasing the percentage of target cells where Cas9 successfully makes double-strand breaks at the intended site.

  ○ Off-Target Edit Rate → Unintended Mutations = POSITIVE (+)
    Higher off-target editing means Cas9 is cutting DNA at more unintended locations, directly increasing the number of novel mutations that could disrupt genes, activate oncogenes, or cause chromosomal rearrangements.

  ○ Cas9 Cutting Efficiency → Therapeutic Benefit = POSITIVE (+)
    Higher cutting efficiency at the target site means more cells have the disease-causing mutation corrected, directly increasing the measurable improvement in the patient's condition.

STEP 4: CHECK YOUR MODEL
• You should have 4 arrows total
• 1 negative relationship(s), 3 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: Guide RNA Specificity controls where Cas9 cuts, but the human genome contains many similar sequences. If your guide RNA has even two mismatches with another gene, Cas9 might cut there too. How do you balance the urgency of curing a fatal disease against the risk of creating new mutations?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Guide RNA Specificity' and drag an arrow
over to 'Off-Target Edit Rate.'

Here's the key question: When guide rna specificity goes UP, does
off-target edit rate go UP or DOWN?

Higher guide RNA specificity means the guide RNA binds ONLY to the intended target and not to similar sequences — reducing off-target cuts. Lower specificity allows binding at multiple genomic locations, increasing unintended edits.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Next connection: Click on 'Delivery Efficiency' and drag an arrow
over to 'Cas9 Cutting Efficiency.'

Here's the key question: When delivery efficiency goes UP, does
cas9 cutting efficiency go UP or DOWN?

Higher delivery efficiency means more cells receive the CRISPR components, increasing the percentage of target cells where Cas9 successfully makes double-strand breaks at the intended site.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'Off-Target Edit Rate' and drag an arrow
over to 'Unintended Mutations.'

Here's the key question: When off-target edit rate goes UP, does
unintended mutations go UP or DOWN?

Higher off-target editing means Cas9 is cutting DNA at more unintended locations, directly increasing the number of novel mutations that could disrupt genes, activate oncogenes, or cause chromosomal rearrangements.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Final connection: Click on 'Cas9 Cutting Efficiency' and drag an arrow
over to 'Therapeutic Benefit.'

Here's the key question: When cas9 cutting efficiency goes UP, does
therapeutic benefit go UP or DOWN?

Higher cutting efficiency at the target site means more cells have the disease-causing mutation corrected, directly increasing the measurable improvement in the patient's condition.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Look at your model now. You've got 1 negative and 3
positive relationships. 4 arrows total.

Guide RNA Specificity controls where Cas9 cuts, but the human genome contains many similar sequences. If your guide RNA has even two mismatches with another gene, Cas9 might cut there too. How do you balance the urgency of curing a fatal disease against the risk of creating new mutations?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Guide RNA Specificity −→ Off-Target Edit Rate, Delivery Efficiency +→ Cas9 Cutting Efficiency, Off-Target Edit Rate +→ Unintended Mutations, Cas9 Cutting Efficiency +→ Therapeutic Benefit]

---

## Activity 3: VISUALIZE & EVALUATE — Run Your Model

### Text Editor

```
TIME TO SEE YOUR SYSTEM IN ACTION

You built it. You connected it. Now let's see if it actually WORKS
like the real world.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: RUN THE SIMULATION
• Click the "Play" button in the TOP LEFT corner
• Watch the graph panel — you'll see percentage lines for each component

STEP 2: OBSERVE THE BASELINE
• Let it run for about 30 time steps
• Notice how the lines relate to each other
• When Guide RNA Specificity is HIGH, what happens to the internal components?

STEP 3: SCENARIO — HIGH-PRECISION SICKLE CELL EDIT
• Maximum guide RNA specificity, optimized Cas9, single HBB target
• PREDICT FIRST: What do you predict the ratio of successful edits to off-target events will be with the most precise tools available?
• Resume the simulation and observe what happens
• Was your prediction correct?

STEP 4: SCENARIO — LOW-SPECIFICITY BROAD EDIT
• Moderate guide RNA specificity targeting a gene with many similar sequences
• PREDICT FIRST: What do you predict happens to the off-target edit rate when the guide RNA can bind to dozens of similar genomic locations?
• Resume the simulation and observe what happens
• Was your prediction correct?

STEP 5: SCENARIO — GERMLINE VS. SOMATIC COMPARISON
• Same editing parameters applied to somatic versus germline cells
• PREDICT FIRST: What do you predict changes about the risk calculation when every off-target edit becomes permanent and heritable?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• CRISPR precision is extraordinary by historical standards but still imperfect — even the best guide RNAs produce detectable off-target edits, and the 3.2 billion base-pair genome provides countless near-match sites
• The cell's DNA repair choice after Cas9 cutting is largely outside the scientist's control — error-prone non-homologous end joining is more common than precise homology-directed repair, meaning many edits introduce random mutations rather than the intended correction
• Delivery efficiency creates a dose-response dilemma — increasing CRISPR components to edit more cells also increases off-target events proportionally, and not all tissues are equally accessible
• The ethical boundary between curing disease and enhancing traits is scientifically indistinguishable — the same CRISPR technology that corrects sickle cell disease could theoretically modify intelligence, athleticism, or appearance genes

THE ANSWER: CRISPR-Cas9 has already cured sickle cell disease in clinical trials and shows promise for dozens of other genetic conditions. The technology works by directing a molecular scissor to a precise DNA location using a guide RNA, cutting the faulty gene, and allowing cellular repair machinery to insert the correct sequence. However, the system is not perfect: off-target edits occur at similar sequences elsewhere in the genome, the cell's repair pathway is not fully controllable, and delivery to all affected cells remains challenging. The most profound question is not whether CRISPR can cure disease — it already has — but whether we should edit human embryos, creating heritable changes that affect all future generations without their consent. The science is advancing faster than the ethical frameworks to govern it.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: High-Precision Sickle Cell Edit. Maximum guide RNA specificity, optimized Cas9, single HBB target.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Low-Specificity Broad Edit.
Moderate guide RNA specificity targeting a gene with many similar sequences.

Before you run it — make a prediction. What do you predict happens to the off-target edit rate when the guide RNA can bind to dozens of similar genomic locations?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Germline vs. Somatic Comparison. Same editing parameters applied to somatic versus germline cells.
What do you predict changes about the risk calculation when every off-target edit becomes permanent and heritable?

Here's what our model reveals: CRISPR-Cas9 has already cured sickle cell disease in clinical trials and shows promise for dozens of other genetic conditions. The technology works by directing a molecular scissor to a precise DNA location using a guide RNA, cutting the faulty gene, and allowing cellular repair machinery to insert the correct sequence. However, the system is not perfect: off-target edits occur at similar sequences elsewhere in the genome, the cell's repair pathway is not fully controllable, and delivery to all affected cells remains challenging. The most profound question is not whether CRISPR can cure disease — it already has — but whether we should edit human embryos, creating heritable changes that affect all future generations without their consent. The science is advancing faster than the ethical frameworks to govern it.

You just used a computational model to explain a real-world
phenomenon. That's what scientists do every day.

Now it's your turn to ModelIt!"
```

### Graph
[Screenshot showing simulation graph with scenario results — baseline vs. experimental conditions]

---

## Activity 4: REVISE & EXTEND — Play, Research, Expand

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
   • What happens if you turn OFF Guide RNA Specificity?
   • What happens if you turn OFF Delivery Efficiency?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Epigenetic Disruption — Changes to gene regulation patterns caused by CRISPR editing near regulatory regions — even successful target edits can alter how neighboring genes are expressed, potentially causing unexpected phenotypic effects
   • Immune Response — The patient's immune system reaction to Cas9 protein and viral delivery vectors — many humans have pre-existing antibodies to common Cas9 variants because they evolved from bacteria that infect humans
   • Mosaicism Rate — The percentage of cells that receive different editing outcomes — some cells may be correctly edited, others incorrectly edited, and others unedited, creating a genetic mosaic that complicates therapeutic efficacy

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • How CRISPR-Cas9 Works — how does this connect to your model?
   • The Off-Target Problem — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model demonstrate the tension between editing precision and the sheer size of the human genome?
   • Why is the cell's choice between repair pathways such a critical variable, and how does it limit CRISPR's therapeutic potential?
   • What does your model reveal about the difference in risk profiles between somatic and germline editing?
   • How would your model change if a new Cas9 variant were developed with zero off-target activity?

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

Epigenetic Disruption. Changes to gene regulation patterns caused by CRISPR editing near regulatory regions — even successful target edits can alter how neighboring genes are expressed, potentially causing unexpected phenotypic effects
How would you model that?

Immune Response. The patient's immune system reaction to Cas9 protein and viral delivery vectors — many humans have pre-existing antibodies to common Cas9 variants because they evolved from bacteria that infect humans
How would you model that?

Mosaicism Rate. The percentage of cells that receive different editing outcomes — some cells may be correctly edited, others incorrectly edited, and others unedited, creating a genetic mosaic that complicates therapeutic efficacy
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

Genetic Counselors help patients and families understand genetic test results and the implications of gene therapy options, earning $85,000-$120,000/year. Gene Therapy Scientists design and test CRISPR-based treatments at biotech companies like Editas Medicine, CRISPR Therapeutics, and Intellia, earning $95,000-$180,000/year. Bioethicists who specialize in emerging genetic technologies advise hospitals, companies, and governments on ethical frameworks, earning $70,000-$140,000/year.

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
Visual: Title slide with dramatic CRISPR molecular editing visualization
Say: "In 2023, a 12-year-old named Victoria Gray became the first person cured of sickle cell disease by CRISPR gene editing. She had suffered agonizing pain crises her entire life. Now she is pain-free. But the same technology that saved her could also be used to edit human embryos — changing the DNA of every future generation. Where do we draw the line?"
Do: Open with Victoria Gray's story. Show before and after — a life of pain crises versus a cure. Let the emotional weight settle before introducing the technology.
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and vocabulary terms displayed
Say: "Today you are modeling the most powerful biological tool humans have ever created. You will discover why it works, where it fails, and why the hardest questions about CRISPR are not scientific but ethical."
Do: Have students read objectives. Pre-teach 'guide RNA' and 'off-target effects.' Emphasize that precision is the central engineering challenge.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: Could we rewrite the code of life to eliminate genetic disease — and should we?
Say: "Notice this question has two parts: CAN we and SHOULD we. The science answers the first. Only society can answer the second. Today your model will show you exactly why that distinction matters."
Do: Quick-write: Students write what they already know about CRISPR and one concern they have about gene editing. Share out and catalog concerns on the board.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps overview with gene editing context
Say: "We are building a model of how molecular precision at the scale of individual DNA bases determines whether a patient is cured or harmed."
Do: Preview each LEVER step. Emphasize that this model connects molecular biology to medical outcomes to ethical decisions.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Seven component cards for CRISPR gene editing model
Say: "Seven components control whether gene editing saves a life or causes new damage. Two of them — guide RNA specificity and delivery efficiency — are the variables scientists can directly engineer. Everything else is a consequence."
Do: Guide students through components. Discuss why guide RNA specificity and delivery are external — they are the design choices. Cutting efficiency, repair pathway, and outcomes are biological responses.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows showing how guide RNA specificity drives both therapeutic and harmful outcomes
Say: "Here is the cruel trade-off: the same guide RNA that finds your target also searches the entire genome for similar sequences. More delivery means more editing — both on-target AND off-target."
Do: Help students map the dual-pathway structure. Use green arrows for therapeutic pathways and red for harmful ones. Emphasize that both flow from the same input variables.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Simulation results comparing high-precision, low-specificity, and germline scenarios
Say: "Let us test: can you find parameter settings where the therapy cures the disease without creating dangerous new mutations? What happens when you push for maximum coverage?"
Do: Students predict outcomes before each scenario. Compare predictions with model outputs. Special attention to the germline scenario — same numbers, completely different ethical weight.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key findings from model exploration
Say: "CRISPR is not a magic eraser — it is a precision tool operating in a genome with 3.2 billion characters where many sequences look alike. The question is not IF off-target edits happen but WHETHER the therapeutic benefit outweighs the risk."
Do: Lead discussion connecting model findings to real clinical outcomes. Victoria Gray is cured — but the therapy costs two million dollars and required destroying and rebuilding her blood system. Is that sustainable?
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: CRISPR clinical trial protocol design challenge
Say: "A biotech company needs your clinical trial design. Fatal disease, promising therapy, known risks. How do you protect patients while advancing a cure that could save millions?"
Do: Groups design clinical trial protocols addressing target selection, safety monitoring, patient selection, and ethical review. Present with evidence from model simulations.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: Can CRISPR Cure Genetic Diseases?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
CRISPR-Cas9 is the most transformative biological technology since the discovery of DNA's structure in 1953. Derived from an ancient bacterial immune system, it allows scientists to edit any gene in any organism with unprecedented precision. In 2023, the FDA approved the first CRISPR-based therapy (Casgevy) for sickle cell disease, marking the beginning of the gene editing era in medicine. But the power to rewrite the code of life raises questions that science alone cannot answer.

NGSS ALIGNMENT:
HS-LS3-1, HS-LS3-2: Ask questions to clarify relationships about the role of DNA and chromosomes in coding the instructions for characteristic traits passed from parents to offspring. Make and defend a claim based on evidence that inheritable genetic variations may result from new genetic combinations through meiosis, viable errors occurring during replication, or mutations caused by environmental factors.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Asking Questions and Defining Problems
  Students ask questions about how CRISPR precision, off-target rates, and repair pathways interact to determine whether gene editing therapy succeeds or causes harm.
• Disciplinary Core Idea: LS3.A Inheritance of Traits / LS3.B Variation of Traits
  Students model how DNA mutations cause genetic diseases and how targeted gene editing can correct these mutations, while also understanding how editing introduces new genetic variation.
• Crosscutting Concept: Cause and Effect
  Students trace the causal chain from guide RNA design through Cas9 cutting, repair pathway selection, and ultimately therapeutic or harmful outcomes, identifying how each variable influences the final result.

PACING GUIDE:
• Activity 1 (Locate): 8-10 minutes
• Activity 2 (Establish): 8-10 minutes
• Activity 3 (Visualize & Evaluate): 10-12 minutes
• Activity 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: CRISPR-Cas9, Guide RNA, Off-Target Effects, Germline Editing, Homology-Directed Repair
□ Prepare Could we rewrite the code of life to eliminate genetic disease — and should we discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify seven key components of the CRISPR gene editing system: guide RNA specificity, Cas9 cutting efficiency, off-target edit rate, repair pathway selection, delivery efficiency, therapeutic benefit, and unintended mutations.
• Establish: Students map the causal relationships showing how guide RNA specificity and delivery efficiency drive both therapeutic benefit and off-target risk, revealing the fundamental precision-versus-coverage trade-off in gene editing.
• Visualize: Students build a computational model showing the seven-component gene editing system with competing pathways leading to therapeutic success or unintended harm.
• Evaluate: Students run high-precision sickle cell, low-specificity broad edit, and germline versus somatic comparison scenarios to identify the parameter ranges where therapeutic benefit outweighs risk.
• Revise: Students add epigenetic disruption, immune response, or mosaicism rate to model more realistic biological complexity in CRISPR therapy outcomes.

BACKGROUND CONTENT:
• How CRISPR-Cas9 Works:
  The CRISPR system has two key components: a guide RNA that matches the target DNA sequence, and the Cas9 enzyme that acts as molecular scissors. The guide RNA directs Cas9 to the target location by base-pairing with the complementary DNA strand. Once bound, Cas9 makes a double-strand break in the DNA. The cell then repairs this break using one of two pathways: non-homologous end joining (NHEJ), which is fast but error-prone and often introduces small insertions or deletions, or homology-directed repair (HDR), which uses a provided DNA template to make precise corrections. Scientists prefer HDR for therapeutic applications, but cells default to NHEJ about 80% of the time.

• The Off-Target Problem:
  The human genome contains 3.2 billion base pairs, and many 20-nucleotide sequences appear multiple times with slight variations. A guide RNA designed to match one specific location may also bind to sequences that differ by just one or two bases. When Cas9 cuts at these off-target sites, it can disrupt essential genes, activate cancer-causing oncogenes, or create chromosomal rearrangements. Modern high-fidelity Cas9 variants (like eSpCas9 and HiFi Cas9) reduce but do not eliminate off-target activity. Whole-genome sequencing after editing reveals that even optimized systems produce detectable off-target mutations.

• Somatic vs. Germline: The Ethical Divide:
  Somatic gene editing modifies cells in a living patient — blood cells, muscle cells, neurons — and those changes die with the patient. This is ethically similar to any medical treatment: the patient consents, bears the risks, and receives the benefits. Germline editing modifies embryos, sperm, or eggs, meaning the changes become heritable and pass to all future generations. In 2018, Chinese scientist He Jiankui created the first gene-edited babies, modifying the CCR5 gene to confer HIV resistance. The global scientific community condemned this as premature, reckless, and unethical — he was sentenced to three years in prison. The ethical debate centers on consent: future generations cannot consent to changes that permanently alter the human genome.

• Current Clinical Applications:
  As of 2025, CRISPR therapies are approved or in late-stage clinical trials for sickle cell disease, beta-thalassemia, certain cancers (via CAR-T cell engineering), hereditary blindness (Leber congenital amaurosis), hereditary angioedema, and transthyretin amyloidosis. The sickle cell therapy works by editing blood stem cells outside the body, reactivating fetal hemoglobin production that compensates for the defective adult hemoglobin gene. Results have been remarkable: patients who suffered debilitating pain crises are now symptom-free years after treatment. However, the therapy costs over $2 million per patient, raising serious questions about equitable access.

COMMON MISCONCEPTIONS:
• "CRISPR edits genes with perfect precision like a word processor"
  Reality: CRISPR is remarkably precise compared to previous genetic engineering tools, but it is not perfect. The Cas9 enzyme can cut at off-target sites that partially match the guide RNA, the cell's DNA repair after cutting is not fully controllable (NHEJ is error-prone and more common than HDR), and large deletions or chromosomal rearrangements occasionally occur at cut sites. Current best-case on-target efficiency is about 90-95% with detectable off-target activity at multiple genomic sites.
  Strategy: Analogy: CRISPR is like a GPS-guided missile, not a laser pointer. It usually hits the target, but the blast radius affects surrounding areas. Show students whole-genome sequencing data from edited cells revealing off-target mutations.

• "Gene editing can only be used for curing diseases"
  Reality: The same CRISPR technology that corrects disease-causing mutations can in principle modify any gene — including those affecting height, intelligence, athletic ability, skin color, or any other trait. The technology does not distinguish between therapeutic and enhancement applications. This is why the scientific community draws a sharp ethical line between somatic editing for medical treatment and germline editing that could enable designer babies.
  Strategy: Discussion: If you could edit one gene in an embryo, would you choose to cure a fatal disease? Prevent a mild disability? Enhance intelligence? Change eye color? Where exactly does the ethical line fall, and who gets to draw it?

• "If CRISPR can cure one genetic disease it can cure them all"
  Reality: Different genetic diseases present vastly different CRISPR challenges. Single-gene disorders with well-characterized mutations in accessible tissues (like sickle cell in blood cells) are the easiest targets. Diseases involving multiple genes, genes in hard-to-reach tissues (brain, heart), or conditions where the gene function is complex and context-dependent are far harder. Some genetic conditions would require editing millions of cells in solid organs simultaneously, which is currently impossible. The model shows that delivery efficiency and tissue accessibility are major limiting variables.
  Strategy: Compare: Sickle cell requires editing one gene in blood stem cells that can be removed, edited outside the body, and returned. Alzheimer's involves multiple genes in billions of brain neurons that cannot be removed. Same tool, vastly different challenges.

FACILITATION TIPS:
• Activity 1: Let students explore the interface. Don't over-explain.
  Let them discover. Circulate and support, don't lecture.
• Activity 2: Ask "When this goes up, what happens to that?" to
  guide positive/negative relationship decisions. Let students debate.
• Activity 3: Give time for students to "break" the model — turn
  things on/off and observe. This is where real insight happens.
• Activity 4: Don't give answers. Ask questions. Let curiosity drive
  the research. Celebrate when students' additions don't work as
  expected — that's authentic science.

ANSWER KEY:
Big Question: Could we rewrite the code of life to eliminate genetic disease — and should we?
Answer: CRISPR-Cas9 has already cured sickle cell disease in clinical trials and shows promise for dozens of other genetic conditions. The technology works by directing a molecular scissor to a precise DNA location using a guide RNA, cutting the faulty gene, and allowing cellular repair machinery to insert the correct sequence. However, the system is not perfect: off-target edits occur at similar sequences elsewhere in the genome, the cell's repair pathway is not fully controllable, and delivery to all affected cells remains challenging. The most profound question is not whether CRISPR can cure disease — it already has — but whether we should edit human embryos, creating heritable changes that affect all future generations without their consent. The science is advancing faster than the ethical frameworks to govern it.

Simulation Answers:
• High-Precision Sickle Cell Edit Scenario: With maximum guide RNA specificity and optimized Cas9, the model shows high on-target editing rates (85-95% of successfully delivered cells) with very low off-target activity (less than 0.01% per potential off-target site). Therapeutic benefit is strong because the sickle cell mutation is a single nucleotide change in a well-characterized gene. However, even at 0.01% off-target rate, whole-genome analysis reveals a small number of unintended edits, mostly in non-coding regions. The model demonstrates that high-precision editing of well-defined single-gene diseases represents the best current use case for CRISPR therapy.
• Low-Specificity Broad Edit Scenario: When guide RNA specificity is reduced, the off-target edit rate increases dramatically — potentially by 10-100 fold. The model shows Cas9 cutting at dozens of genomic locations that share partial sequence similarity with the target. Unintended mutations accumulate across the genome, with some falling in gene coding regions or regulatory elements. Therapeutic benefit at the target site may still occur, but the ratio of beneficial to harmful edits shifts dangerously. This scenario illustrates why guide RNA design is the most critical engineering variable in CRISPR therapy.

Reflection Exemplars:
• Q: Why is the off-target problem fundamentally unsolvable with current technology?
  A: The human genome is 3.2 billion base pairs long, and the guide RNA targets a sequence of about 20 bases. Statistically, a random 20-base sequence appears approximately once in 4^20 (about 1 trillion) possible sequences — but the genome also contains many sequences that differ by just one or two bases from any target. High-fidelity Cas9 variants discriminate better between perfect and imperfect matches, but they cannot achieve zero off-target activity because the thermodynamics of RNA-DNA binding allow some mismatch tolerance. The model shows that improving specificity reduces but never eliminates off-target edits — you can approach zero but never reach it.
• Q: Why does the somatic vs. germline distinction matter if the editing parameters are identical?
  A: The model produces identical molecular outcomes for somatic and germline editing because the CRISPR mechanism works the same way in any cell. The difference is entirely about consequences: somatic edits affect only the patient's cells and die with them. Germline edits become part of the human gene pool forever. An off-target mutation in a somatic cell might cause problems for one patient. The same mutation in a germline cell propagates through every descendant for all future generations. The model shows that the acceptable risk threshold must be dramatically lower for germline editing because the cumulative impact scales across generations, not just one lifetime.

STEM CHALLENGE GUIDANCE:
Title: Design a CRISPR Clinical Trial Protocol
Mission: Design a clinical trial protocol for using CRISPR to treat a specific genetic disease, addressing editing precision, safety monitoring, delivery strategy, and ethical safeguards.
Scenario: A biotech company has asked your team to design the Phase 1 clinical trial protocol for a new CRISPR therapy targeting Huntington's disease — a fatal neurological condition caused by a single gene mutation. You must balance the urgency of treating a terminal disease against the safety risks of off-target editing in brain tissue, design a delivery strategy that reaches neurons, and establish monitoring protocols to detect unintended mutations before they cause harm.
Introduction: Present the challenge: A biotech company developing a CRISPR therapy for Huntington's disease needs your team to design the Phase 1 clinical trial protocol. Huntington's is a fatal neurodegenerative disease caused by a single gene mutation, but the target tissue is the brain — the hardest organ to deliver CRISPR to. Your protocol must address guide RNA design for maximum specificity, delivery strategy for neurons, patient safety monitoring at every stage, and ethical review requirements.

Key Concepts:
• Therapeutic Index: The ratio of therapeutic benefit to harmful side effects — in gene editing, this means the ratio of correctly edited cells to cells with off-target mutations. A therapy is viable only if the therapeutic index is high enough that the cure does not cause worse problems than the disease.
• Delivery Vectors: The vehicles that carry CRISPR components into cells — adeno-associated viruses (AAVs) are commonly used for brain delivery because they can cross the blood-brain barrier, but they have limited cargo capacity and can trigger immune responses. Lipid nanoparticles offer an alternative with different trade-offs in efficiency and safety.
• Informed Consent in Gene Therapy: The ethical requirement that patients fully understand the risks of irreversible genetic modification before agreeing to treatment — particularly challenging for gene editing because long-term effects may not be known and off-target edits are difficult to detect comprehensively.

Evaluation Rubric:
• Expert (4): Protocol includes specific guide RNA design rationale with off-target prediction analysis, evidence-based delivery strategy for brain tissue, comprehensive safety monitoring with defined stopping rules, ethical review process, and uses model data to justify risk-benefit calculations
• Proficient (3): Protocol addresses guide RNA specificity, delivery choice, and safety monitoring with model evidence, and considers ethical implications
• Developing (2): Protocol identifies key challenges but lacks quantitative model evidence or does not adequately address delivery or ethical review
• Beginning (1): Protocol is incomplete, does not reference model data, or fails to address safety monitoring and ethical considerations

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a visual guide showing the CRISPR mechanism step by step: guide RNA design, Cas9 binding, DNA cutting, and repair pathway options
  • Use a risk matrix template with rows for different off-target rates and columns for different delivery efficiencies so students can map the parameter space
  • Sentence frames: 'The guide RNA specificity must be at least __% because our model shows that below this level, off-target edits in __ increase to __ which could cause __'

Extensions (Advanced Learners):
  • Research the He Jiankui germline editing case and write a scientific ethics analysis of what went wrong and what safeguards were violated
  • Investigate base editing and prime editing — newer CRISPR variants that do not make double-strand breaks — and analyze how they change the off-target risk profile in your model
  • Design an equitable access framework for CRISPR therapies that cost over two million dollars per patient — how should society distribute a cure that works but is unaffordable for most?

Cross-Curricular Connections:
  • Math: Calculate the probability of off-target editing: if a guide RNA has a 0.05% chance of binding at each of 200 potential off-target sites, what is the probability that at least one off-target edit occurs in a treated cell? How does this scale across one billion treated cells?
  • ELA: Write a patient consent document for a CRISPR clinical trial that explains the technology, potential benefits, known risks, and unknown long-term effects in language accessible to a non-scientist — then evaluate whether true informed consent is possible for irreversible genetic modification
  • History/Ethics: Research the history of eugenics in America and analyze how modern gene editing technology could be misused to repeat historical injustices — what safeguards are needed to prevent CRISPR from becoming a tool of genetic discrimination?

CAST ALIGNMENT:
• Model how CRISPR-Cas9 guide RNA specificity determines the ratio of on-target corrections to off-target mutations across the human genome
• Analyze the relationship between delivery efficiency, repair pathway selection, and therapeutic outcome in gene editing therapy
• Evaluate the ethical implications of germline versus somatic editing using quantitative risk data from computational models

CAST-Style Assessment Questions:
• Multiple Choice: A CRISPR therapy achieves 95% on-target editing efficiency but has a 0.1% off-target rate. Given that the human genome has 3.2 billion base pairs, approximately how many unintended edits could occur per treated cell, and why does this matter?
• Constructed Response: Using evidence from your model, explain why curing sickle cell disease with CRISPR in adult blood stem cells is considered ethically acceptable by most scientists, while using the same technology to edit embryos to prevent sickle cell disease in future generations remains deeply controversial. Reference at least two model variables in your response.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: Can CRISPR Cure Genetic Diseases?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. What do you already know about how CRISPR gene editing works, and where does the technology come from?

   _________________________________________________________

   _________________________________________________________

2. If scientists could fix a gene that causes a fatal disease, what reasons might there be to proceed with caution?

   _________________________________________________________

   _________________________________________________________

3. Draw a diagram showing how you think a gene editing tool finds and changes a specific location in DNA.

   [DRAWING BOX]

4. What is the difference between editing genes in a person's body cells versus editing genes in an embryo?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ CRISPR-Cas9                   
___ Guide RNA                     
___ Off-Target Effects            
___ Germline Editing              
___ Homology-Directed Repair      

A. A molecular tool derived from bacterial immune systems that uses a guide RNA to direct the Cas9 enzyme to a specific DNA sequence, where it makes a precise double-strand cut — enabling scientists to delete, replace, or insert genetic material at targeted locations in any organism's genome
B. A synthetic RNA molecule approximately 20 nucleotides long that is complementary to the target DNA sequence — it acts as the GPS system directing the Cas9 enzyme to the exact genomic location where editing should occur
C. Unintended edits at genomic locations that are similar but not identical to the target sequence — guide RNA can bind to sequences with one or two mismatches, causing Cas9 to cut DNA at the wrong location, potentially disrupting essential genes or activating oncogenes
D. Genetic modifications made to sperm, eggs, or embryos that become heritable — meaning they pass to all future generations — raising profound ethical questions because the edited individual and all descendants carry changes they never consented to
E. A precise DNA repair pathway that uses a provided template to fix double-strand breaks, allowing scientists to insert specific new sequences — this is the mechanism by which CRISPR replaces disease-causing mutations with correct versions

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

SCENARIO: High-Precision Sickle Cell Edit
Settings: Maximum guide RNA specificity, optimized Cas9, single HBB target
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Low-Specificity Broad Edit
Settings: Moderate guide RNA specificity targeting a gene with many similar sequences
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Germline vs. Somatic Comparison
Settings: Same editing parameters applied to somatic versus germline cells
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

1. How does your model demonstrate the tension between editing precision and the sheer size of the human genome?

   _________________________________________________________

   _________________________________________________________

2. Why is the cell's choice between repair pathways such a critical variable, and how does it limit CRISPR's therapeutic potential?

   _________________________________________________________

   _________________________________________________________

3. What does your model reveal about the difference in risk profiles between somatic and germline editing?

   _________________________________________________________

   _________________________________________________________

4. How would your model change if a new Cas9 variant were developed with zero off-target activity?

   _________________________________________________________

   _________________________________________________________

5. What are the limitations of modeling gene editing when individual patient genomes vary by millions of base pairs?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Could we rewrite the code of life to eliminate genetic disease — and should we? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Asking Questions and Defining Problems
   □ Disciplinary Core Idea: LS3.A Inheritance of Traits / LS3.B Variation of Traits
   □ Crosscutting Concept: Cause and Effect

3. What are the limitations of modeling gene editing when individual patient genomes vary by millions of base pairs?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a CRISPR Clinical Trial Protocol
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design a clinical trial protocol for using CRISPR to treat a specific genetic disease, addressing editing precision, safety monitoring, delivery strategy, and ethical safeguards.

SCENARIO: A biotech company has asked your team to design the Phase 1 clinical trial protocol for a new CRISPR therapy targeting Huntington's disease — a fatal neurological condition caused by a single gene mutation. You must balance the urgency of treating a terminal disease against the safety risks of off-target editing in brain tissue, design a delivery strategy that reaches neurons, and establish monitoring protocols to detect unintended mutations before they cause harm.

GUIDING QUESTIONS:
• What level of off-target editing is acceptable when the alternative is a fatal disease with no other treatment?
• How would you deliver CRISPR components specifically to neurons in the brain without affecting other tissues?
• What monitoring tests would you require at each stage of the trial to detect harmful unintended edits?

DESIGN THINKING:
• What guide RNA design features maximize specificity for the Huntington's gene while minimizing off-target potential?

  _________________________________________________________

• What delivery method would you choose for brain tissue and what are the trade-offs versus other approaches?

  _________________________________________________________

• How many patients should be in your Phase 1 trial and what are your primary safety endpoints?

  _________________________________________________________

• What ethical review process would you require before the first patient receives CRISPR treatment?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Protocol includes specific guide RNA design rationale with off-target prediction analysis, evidence-based delivery strategy for brain tissue, comprehensive safety monitoring with defined stopping rules, ethical review process, and uses model data to justify risk-benefit calculations
• Proficient (3): Protocol addresses guide RNA specificity, delivery choice, and safety monitoring with model evidence, and considers ethical implications
• Developing (2): Protocol identifies key challenges but lacks quantitative model evidence or does not adequately address delivery or ethical review
• Beginning (1): Protocol is incomplete, does not reference model data, or fails to address safety monitoring and ethical considerations

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-11/G11L3-L01/G11L3-L01-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-11/G11L3-L01/G11L3-L01-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-11/G11L3-L01/G11L3-L01-Student-Presentation.pptx] |
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