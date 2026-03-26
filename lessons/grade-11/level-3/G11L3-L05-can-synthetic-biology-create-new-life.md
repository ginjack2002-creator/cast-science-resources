# Lesson: Can Synthetic Biology Create New Life?

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G11L3-L05 |
| **Grade** | 11th Grade — Level 3: Systems Innovation Lab |
| **Lesson Name** | Can Synthetic Biology Create New Life? |
| **Status** | Template |

---

## Platform

### Title
**Can Synthetic Biology Create New Life? — Modeling Engineered Genetic Circuits and Synthetic Organism Design**

### Overview
In 2010, Craig Venter's team created the first synthetic organism — a bacterium with a genome written entirely by machines and assembled from chemical building blocks. They named it Mycoplasma mycoides JCVI-syn1.0, and it became the first living cell whose parent was a computer. Since then, synthetic biology has exploded: engineered yeast now produces artemisinin (an antimalarial drug) at scale, bacteria have been programmed to detect and kill cancer cells, and the International Genetically Engineered Machine (iGEM) competition has thousands of students building biological systems from standardized genetic parts. Students investigate the driving question: If we can write DNA from scratch like computer code, can we engineer entirely new forms of life — and what are the consequences if we do? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of a glowing synthetic bacterium engineered with bioluminescent circuits visible as colored light patterns inside a futuristic bioreactor, with DNA code projections overlaying the scene, featuring a diverse multicultural group with Black people centered of 16-17 year old students observing through advanced microscopy displays]

### Grade
11th Grade — Level 3: Systems Innovation Lab

### NGSS Standard
**HS-LS1-1, HS-LS3-1**: Construct an explanation based on evidence for how the structure of DNA determines the structure of proteins which carry out the essential functions of life through systems of specialized cells. Ask questions to clarify relationships about the role of DNA and chromosomes in coding the instructions for characteristic traits passed from parents to offspring.

### Learning Objectives
- Model how synthetic genetic circuits function as biological logic gates that control gene expression in engineered organisms
- Analyze the relationship between circuit complexity, metabolic burden, and the evolutionary stability of synthetic organisms
- Evaluate the trade-offs between organism functionality, biosafety containment, and the risk of unintended ecological consequences
- Predict how synthetic organisms respond when engineered functions compete with natural selection pressures

### Component List (Starting Model: 6 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Circuit Complexity | External | The number of genetic parts (promoters, genes, regulatory elements) and logic operations in the engineered system — more complex circuits enable more sophisticated behaviors but impose greater metabolic burden and have more failure points |
| Metabolic Burden | Internal | The fraction of the cell's energy and molecular resources consumed by the synthetic circuit — high burden slows growth and creates evolutionary pressure for mutations that disable the engineered functions |
| Evolutionary Stability | Internal | The probability that the synthetic circuit maintains its designed function over many generations — mutations that reduce metabolic burden are selected for, meaning evolution actively tries to break engineered systems |
| Output Fidelity | Internal | The precision and reliability with which the genetic circuit produces the intended biological output — affected by molecular noise, metabolic state, and environmental conditions |
| Growth Rate | Internal | The speed at which the engineered organism reproduces — determined by the balance between natural growth capacity and the metabolic burden imposed by synthetic circuits |
| Biocontainment Strength | External | The effectiveness of safety mechanisms preventing the organism from surviving outside controlled conditions — measured as the escape frequency, the probability that a mutant arises that defeats the containment system |

### Research for Lesson
- The DNA Programming Paradigm — reference materials and textbook resources
- Genetic Circuits as Logic Gates — reference materials and textbook resources
- The Evolutionary Arms Race — reference materials and textbook resources
- Biocontainment and Safety — reference materials and textbook resources

---

## Step 1: LOCATE — Build Your System

### Text Editor

```
CAN SYNTHETIC BIOLOGY CREATE NEW LIFE?

Modeling Engineered Genetic Circuits and Synthetic Organism Design.
If we can write DNA from scratch like computer code, can we engineer entirely new forms of life — and what are the consequences if we do?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Circuit Complexity" — the number of genetic parts (promoters
  ○ Click "Biocontainment Strength" — the effectiveness of safety mechanisms preventing the organism from surviving outside controlled conditions — measured as the escape frequency
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Metabolic Burden" — the fraction of the cell's energy and molecular resources consumed by the synthetic circuit — high burden slows growth and creates evolutionary pressure for mutations that disable the engineered functions
  ○ Click "Evolutionary Stability" — the probability that the synthetic circuit maintains its designed function over many generations — mutations that reduce metabolic burden are selected for
  ○ Click "Output Fidelity" — the precision and reliability with which the genetic circuit produces the intended biological output — affected by molecular noise
  ○ Click "Growth Rate" — the speed at which the engineered organism reproduces — determined by the balance between natural growth capacity and the metabolic burden imposed by synthetic circuits

Task B: ADD TO YOUR MODEL
• Click the PLUS (+) button to add each component to your picture
• You should now see 6 components on your canvas

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
"If we can write DNA from scratch like computer code, can we engineer entirely new forms of life — and what are the consequences if we do?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Circuit Complexity' — that's external. The number of genetic parts (promoters.
Click on 'Metabolic Burden' — that's internal. The fraction of the cell's energy and molecular resources consumed by the synthetic circuit — high burden slows growth and creates evolutionary pressure for mutations that disable the engineered functions.
Click on 'Evolutionary Stability' — that's internal. The probability that the synthetic circuit maintains its designed function over many generations — mutations that reduce metabolic burden are selected for.
Click on 'Output Fidelity' — that's internal. The precision and reliability with which the genetic circuit produces the intended biological output — affected by molecular noise.
Click on 'Growth Rate' — that's internal. The speed at which the engineered organism reproduces — determined by the balance between natural growth capacity and the metabolic burden imposed by synthetic circuits.
Click on 'Biocontainment Strength' — that's external. The effectiveness of safety mechanisms preventing the organism from surviving outside controlled conditions — measured as the escape frequency.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Circuit Complexity is external because it represents the engineering design choice — how many genetic parts and logic operations the synthetic biologist includes in the circuit. This is determined at the design stage before the organism is created. Biocontainment Strength is external because it represents the safety engineering choices — how many independent containment mechanisms are built into the organism. The remaining four components are internal: Metabolic Burden is a consequence of the circuit's resource demands on the cell, Evolutionary Stability is determined by the interplay of burden and mutation, Output Fidelity depends on circuit function and cellular conditions, and Growth Rate reflects the net balance between natural growth capacity and synthetic circuit costs.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next step, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 6 components sorted: Circuit Complexity, Biocontainment Strength (External), Metabolic Burden, Evolutionary Stability, Output Fidelity, Growth Rate (Internal)]

### Graph
[Empty graph panel — no simulation yet]

---

## Step 2: ESTABLISH — Connect the Relationships

### Text Editor

```
TIME TO DRAW THE INVISIBLE LINES

Those 6 components don't just sit there — they AFFECT each other.
When one changes, others change too. Let's map those connections.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: OPEN CONNECTION MODE
• Click the "Connect" icon in the TOP LEFT corner of your screen
• Your cursor is now ready to draw relationship arrows

Task B: DRAW YOUR RELATIONSHIPS
• Click on "Circuit Complexity" and drag an arrow to "Metabolic Burden"
• Click on "Metabolic Burden" and drag an arrow to "Evolutionary Stability"
• Click on "Metabolic Burden" and drag an arrow to "Growth Rate"
• Click on "Biocontainment Strength" and drag an arrow to "Growth Rate"

Task C: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Circuit Complexity → Metabolic Burden = POSITIVE (+)
    More complex genetic circuits require more cellular resources — ribosomes to translate additional mRNA, amino acids to build additional proteins, and ATP to power the additional biochemical reactions. Each added genetic part incrementally increases the energy and material drain on the host cell.

  ○ Metabolic Burden → Evolutionary Stability = NEGATIVE (−)
    Higher metabolic burden creates stronger evolutionary pressure to shed the engineered circuit. Mutants that inactivate burden-imposing genes grow faster and outcompete the engineered strain. The stronger the burden, the faster the engineered function is lost through natural selection.

  ○ Metabolic Burden → Growth Rate = NEGATIVE (−)
    Higher metabolic burden diverts cellular resources from growth to synthetic circuit maintenance, directly slowing cell division. An engineered bacterium with a heavy synthetic circuit may divide 20-50% slower than the same strain without the circuit.

  ○ Biocontainment Strength → Growth Rate = NEGATIVE (−)
    Biocontainment mechanisms themselves impose metabolic costs — kill switch genes must be maintained, synthetic amino acid requirements add metabolic complexity, and auxotrophies limit growth conditions. More containment layers add incremental growth penalties.

Task D: CHECK YOUR MODEL
• You should have 4 arrows total
• 3 negative relationship(s), 1 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: Evolution is both the greatest tool and the greatest enemy of synthetic biology. Organisms evolve — and any mutation that reduces the cost of an engineered circuit will be selected for. How do you engineer an organism to do something evolution is actively trying to undo?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Circuit Complexity' and drag an arrow
over to 'Metabolic Burden.'

Here's the key question: When circuit complexity goes UP, does
metabolic burden go UP or DOWN?

More complex genetic circuits require more cellular resources — ribosomes to translate additional mRNA, amino acids to build additional proteins, and ATP to power the additional biochemical reactions. Each added genetic part incrementally increases the energy and material drain on the host cell.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Metabolic Burden' and drag an arrow
over to 'Evolutionary Stability.'

Here's the key question: When metabolic burden goes UP, does
evolutionary stability go UP or DOWN?

Higher metabolic burden creates stronger evolutionary pressure to shed the engineered circuit. Mutants that inactivate burden-imposing genes grow faster and outcompete the engineered strain. The stronger the burden, the faster the engineered function is lost through natural selection.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Last connection: Click on 'Metabolic Burden' and drag an arrow
over to 'Growth Rate.'

Here's the key question: When metabolic burden goes UP, does
growth rate go UP or DOWN?

Higher metabolic burden diverts cellular resources from growth to synthetic circuit maintenance, directly slowing cell division. An engineered bacterium with a heavy synthetic circuit may divide 20-50% slower than the same strain without the circuit.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Biocontainment Strength' and drag an arrow
over to 'Growth Rate.'

Here's the key question: When biocontainment strength goes UP, does
growth rate go UP or DOWN?

Biocontainment mechanisms themselves impose metabolic costs — kill switch genes must be maintained, synthetic amino acid requirements add metabolic complexity, and auxotrophies limit growth conditions. More containment layers add incremental growth penalties.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Look at your model now. You've got 3 negative and 1
positive relationships. 4 arrows total.

Evolution is both the greatest tool and the greatest enemy of synthetic biology. Organisms evolve — and any mutation that reduces the cost of an engineered circuit will be selected for. How do you engineer an organism to do something evolution is actively trying to undo?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Circuit Complexity +→ Metabolic Burden, Metabolic Burden −→ Evolutionary Stability, Metabolic Burden −→ Growth Rate, Biocontainment Strength −→ Growth Rate]

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
• When Circuit Complexity is HIGH, what happens to the internal components?

Task C: SCENARIO — SIMPLE BIOSENSOR
• Low complexity circuit with one sensor and one output gene, moderate containment
• PREDICT FIRST: What do you predict the evolutionary stability of a simple engineered function will be over hundreds of generations?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task D: SCENARIO — COMPLEX METABOLIC PATHWAY
• High complexity circuit with 10+ engineered genes, standard containment
• PREDICT FIRST: What do you predict happens to the engineered function as evolution selects for faster-growing mutants that shed metabolic burden?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task E: SCENARIO — CONTAINMENT BREACH TEST
• Complex circuit with reduced biocontainment strength
• PREDICT FIRST: What do you predict is the probability that a mutant could both escape containment and retain enough function to survive in a natural environment?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Synthetic genetic circuits obey the same evolutionary rules as natural genes — mutations that reduce the metabolic cost of engineered functions are positively selected, meaning evolution actively works to break engineered systems
• Circuit complexity and evolutionary stability are in fundamental tension — the more complex the engineered system, the more mutations can disable it, and the stronger the selective pressure to do so
• Biocontainment must be engineered with multiple independent safety mechanisms because any single mechanism can be defeated by mutation — redundant containment dramatically reduces escape probability
• The most successful synthetic biology applications use simple circuits with minimal metabolic burden, aligning engineered function with rather than against evolutionary pressure

THE ANSWER: Synthetic biology can now write DNA from scratch, insert it into cells, and create organisms with functions that never existed in nature — from bacteria that detect and destroy cancer cells to yeast that produce antimalarial drugs. But creating truly new life is far more complex than writing genetic code. Every engineered organism is subject to evolution, which relentlessly selects for faster growth by shedding the metabolic burden of synthetic circuits. Complex engineered functions tend to be evolutionary unstable — the organism evolves to break them. Biocontainment is essential but imperfect — any single safety mechanism can be defeated by mutation. The power to write new genetic programs is real, but biology is not a computer. Cells are evolved systems that push back against engineering in ways that silicon never does.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Simple Biosensor. Low complexity circuit with one sensor and one output gene, moderate containment.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Complex Metabolic Pathway.
High complexity circuit with 10+ engineered genes, standard containment.

Before you run it — make a prediction. What do you predict happens to the engineered function as evolution selects for faster-growing mutants that shed metabolic burden?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Containment Breach Test. Complex circuit with reduced biocontainment strength.
What do you predict is the probability that a mutant could both escape containment and retain enough function to survive in a natural environment?

Here's what our model reveals: Synthetic biology can now write DNA from scratch, insert it into cells, and create organisms with functions that never existed in nature — from bacteria that detect and destroy cancer cells to yeast that produce antimalarial drugs. But creating truly new life is far more complex than writing genetic code. Every engineered organism is subject to evolution, which relentlessly selects for faster growth by shedding the metabolic burden of synthetic circuits. Complex engineered functions tend to be evolutionary unstable — the organism evolves to break them. Biocontainment is essential but imperfect — any single safety mechanism can be defeated by mutation. The power to write new genetic programs is real, but biology is not a computer. Cells are evolved systems that push back against engineering in ways that silicon never does.

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
   • What happens if you turn OFF Circuit Complexity?
   • What happens if you turn OFF Biocontainment Strength?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Genetic Part Standardization — The degree to which genetic components are characterized and modular — standardized parts with predictable behavior simplify circuit design but biological context-dependence means parts often behave differently in new organisms
   • Host Organism Compatibility — How well the synthetic circuit integrates with the host cell's existing metabolism — some organisms are better chassis for engineering due to their genetic tractability, growth characteristics, and existing genetic tools
   • Regulatory Approval Pathway — The government review process for deploying synthetic organisms — EPA, FDA, and USDA each have jurisdiction depending on the application, and the approval timeline can exceed the engineering timeline by years

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • The DNA Programming Paradigm — how does this connect to your model?
   • Genetic Circuits as Logic Gates — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model demonstrate why evolution is both the central tool and the central obstacle in synthetic biology?
   • What does the relationship between circuit complexity and evolutionary stability tell you about the practical limits of genetic engineering?
   • Why must biocontainment use multiple independent mechanisms rather than a single safety system?
   • How would your model change if you could engineer organisms that are immune to mutation in their synthetic circuits?

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

Your model has 6 components. Real systems involve
way more. Think about...

Genetic Part Standardization. The degree to which genetic components are characterized and modular — standardized parts with predictable behavior simplify circuit design but biological context-dependence means parts often behave differently in new organisms
How would you model that?

Host Organism Compatibility. How well the synthetic circuit integrates with the host cell's existing metabolism — some organisms are better chassis for engineering due to their genetic tractability, growth characteristics, and existing genetic tools
How would you model that?

Regulatory Approval Pathway. The government review process for deploying synthetic organisms — EPA, FDA, and USDA each have jurisdiction depending on the application, and the approval timeline can exceed the engineering timeline by years
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

Synthetic Biologists design and build new biological systems at companies like Ginkgo Bioworks, Zymergen, Amyris, and Twist Bioscience, earning $95,000-$175,000/year. Biosafety Officers ensure containment protocols protect researchers and the environment at biotech companies and government agencies like the CDC, earning $80,000-$140,000/year. Bioinformatics Scientists who design synthetic genetic sequences using computational tools earn $90,000-$165,000/year.

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
Visual: Title slide with synthetic biology imagery — glowing engineered bacteria
Say: "In 2010, scientists built a living cell from scratch — its DNA written on a computer, synthesized in a machine, and inserted into a cell that booted up and started reproducing. The first organism whose parent was a computer. Today you explore what this means for the future of life itself."
Do: Open with the Venter Institute story. Show the synthetic genome being assembled. Ask: if we can write the code of life, what should we write?
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and vocabulary terms displayed
Say: "Today you are modeling the intersection of engineering and evolution — designing living machines that biology itself is trying to reprogram."
Do: Have students read objectives. Pre-teach 'genetic circuit' using the electronic circuit analogy. Pre-teach 'metabolic burden' as the cost of running synthetic programs in a living cell.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: If we can write DNA from scratch, can we create new life — and should we?
Say: "We can already write any DNA sequence we want. We can insert it into cells. We can create organisms that do things nature never imagined. But biology is not software — cells evolve, mutate, and push back against engineering. How far can we go?"
Do: Quick-write: Students list potential applications of creating custom organisms and potential risks. Share out. Create two columns on the board: Promise and Peril.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps with synthetic biology context
Say: "We are modeling a system where the most powerful force in biology — evolution — is actively working against our engineering designs. Every generation, natural selection tests whether our circuit helps or hinders the cell."
Do: Preview LEVER steps. Emphasize the unique challenge: in synthetic biology, your creation can evolve to defeat your design.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Six component cards for synthetic biology model
Say: "Six components. Two you control: circuit complexity and biocontainment strength. Four that biology determines: metabolic burden, evolutionary stability, output fidelity, and growth rate. The cell is your factory — but it has its own priorities."
Do: Guide through components. Discuss why circuit complexity and biocontainment are external — they are engineering design choices. All other properties emerge from the interaction of the synthetic circuit with the cell's biology.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows showing the complexity-burden-stability cascade
Say: "More complexity means more burden. More burden means less stability. Less stability means your circuit breaks. Evolution is the universal debugger that removes your code because it slows the cell down."
Do: Help students trace the cascade from complexity through burden to stability loss. Discuss how biocontainment must be engineered independently of the functional circuit.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Simulation results for biosensor, complex pathway, and containment breach scenarios
Say: "How long does your engineered function last? What happens when you push complexity? And what is the probability your organism escapes containment?"
Do: Students predict evolutionary stability timelines before running simulations. Key insight: simple circuits persist, complex ones degrade. Containment breach scenario drives home the importance of redundancy.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key findings about synthetic biology limits and safety
Say: "The most important lesson: biology is not an obedient machine. It is an evolved system with four billion years of optimization that resists reprogramming. Successful synthetic biology works WITH evolution, not against it."
Do: Connect findings to real applications: artemisinin production in yeast (simple, commercially successful) versus complex therapeutic organisms (still in research). Discuss the biosafety implications.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Synthetic organism design for environmental remediation
Say: "A chemical spill threatens a river ecosystem. Can you design a synthetic organism that cleans it up without becoming an ecological problem itself? The engineering starts now."
Do: Groups design remediation organisms. Must address metabolic pathway, biocontainment (minimum three mechanisms), evolutionary stability strategy, and monitoring plan. Present with model evidence.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: Can Synthetic Biology Create New Life?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
In 2010, Craig Venter's team created the first synthetic organism — a bacterium with a genome written entirely by machines and assembled from chemical building blocks. They named it Mycoplasma mycoides JCVI-syn1.0, and it became the first living cell whose parent was a computer. Since then, synthetic biology has exploded: engineered yeast now produces artemisinin (an antimalarial drug) at scale, bacteria have been programmed to detect and kill cancer cells, and the International Genetically Engineered Machine (iGEM) competition has thousands of students building biological systems from standardized genetic parts.

NGSS ALIGNMENT:
HS-LS1-1, HS-LS3-1: Construct an explanation based on evidence for how the structure of DNA determines the structure of proteins which carry out the essential functions of life through systems of specialized cells. Ask questions to clarify relationships about the role of DNA and chromosomes in coding the instructions for characteristic traits passed from parents to offspring.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Constructing Explanations and Designing Solutions
  Students construct explanations for how synthetic genetic circuits function and design solutions that balance functionality, safety, and evolutionary stability in engineered organisms.
• Disciplinary Core Idea: LS1.A Structure and Function / LS3.A Inheritance of Traits
  Students model how DNA sequence determines protein function in engineered genetic circuits and how synthetic genetic information is inherited and subject to mutation across generations.
• Crosscutting Concept: Stability and Change
  Students analyze how engineered biological systems maintain designed function (stability) while experiencing evolutionary pressure toward mutation (change), and how this tension determines the practical limits of synthetic biology.

PACING GUIDE:
• Step 1 (Locate): 8-10 minutes
• Step 2 (Establish): 8-10 minutes
• Step 3 (Visualize & Evaluate): 10-12 minutes
• Step 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Synthetic Biology, Genetic Circuit, Metabolic Burden, Biocontainment, Minimal Genome
□ Prepare If we can write DNA from scratch like computer code, can we engineer entirely new forms of life — and what are the consequences if we do discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify six key components of a synthetic biology system: circuit complexity, metabolic burden, evolutionary stability, output fidelity, growth rate, and biocontainment strength.
• Establish: Students map relationships showing that circuit complexity drives metabolic burden which erodes evolutionary stability, while biocontainment strength must be maintained independently through multiple mechanisms to prevent escape.
• Visualize: Students build a computational model showing the six-component synthetic biology system with evolutionary dynamics and containment probability calculations.
• Evaluate: Students run simple biosensor, complex metabolic pathway, and containment breach scenarios to discover how evolutionary pressure and circuit complexity interact to determine practical engineering limits.
• Revise: Students add genetic part standardization, host organism compatibility, or regulatory approval pathway to model more realistic synthetic biology development and deployment.

BACKGROUND CONTENT:
• The DNA Programming Paradigm:
  Synthetic biology treats DNA as a programming language: four bases (A, T, G, C) encode instructions that cells execute. Just as software engineers write code from standardized functions, synthetic biologists assemble genetic circuits from standardized parts — promoters (on/off switches), ribosome binding sites (translation control), coding sequences (protein blueprints), and terminators (stop signals). The Registry of Standard Biological Parts catalogs thousands of characterized components. DNA synthesis technology can produce any sequence up to thousands of base pairs, and DNA assembly methods like Gibson Assembly combine multiple fragments into complete circuits in a single reaction.

• Genetic Circuits as Logic Gates:
  Biological logic gates use molecular interactions to implement Boolean logic. An AND gate produces output only when two inputs are present — for example, a gene that activates only when both lactose AND arabinose are detected. A NOT gate inverts the signal — a repressor protein that turns off a gene when a specific molecule is present. By combining these gates, engineers build complex biological programs: a bacterium that detects a cancer biomarker AND low oxygen (indicating a tumor) then produces a cytotoxic drug. The theoretical complexity is unlimited; the practical complexity is constrained by metabolic burden and evolutionary stability.

• The Evolutionary Arms Race:
  Every cell division is a roll of the evolutionary dice. DNA replication introduces roughly one mutation per billion base pairs per generation. For a bacterium dividing every 30 minutes, this means mutations accumulate rapidly across millions of descendants. Any mutation that reduces the metabolic cost of an engineered circuit — by disabling a non-essential gene, weakening a promoter, or breaking a regulatory connection — provides a growth advantage. Over hundreds of generations, these faster-growing mutants outcompete the engineered strain. This is not a failure of engineering; it is the fundamental nature of biology. Evolution is the strongest optimizer on Earth, and it does not care about human design intentions.

• Biocontainment and Safety:
  Preventing engineered organisms from persisting in the environment is a critical safety requirement. Multiple biocontainment strategies exist: kill switches (genes that produce a toxin when induced, killing the cell on command), auxotrophies (dependence on nutrients like synthetic amino acids that do not exist in nature), genetic safeguards (essential genes split between a chromosome and a plasmid that is lost outside the lab), and semantic containment (recoding the organism's genetic code so that it cannot exchange genes with natural organisms). No single strategy is perfectly reliable — mutations can defeat any individual mechanism. Layering three or more independent containment systems reduces escape probability to effectively zero: if each has a 10^-6 failure rate, three independent systems have a combined failure rate of 10^-18.

COMMON MISCONCEPTIONS:
• "Synthetic biology is the same as genetic modification (GMOs)"
  Reality: Traditional genetic modification typically moves existing genes between organisms — like inserting a fish antifreeze gene into a tomato. Synthetic biology goes further: it designs and builds entirely new genetic sequences from scratch, creates novel genetic circuits that implement logical programs, and can construct organisms with minimal genomes containing only the genes needed for specific functions. While GMOs modify nature's code, synthetic biology writes new code that never existed in any organism.
  Strategy: Compare: A GMO is like editing a document — moving paragraphs around and changing words. Synthetic biology is like writing a completely new document from scratch using the same alphabet. The tools and ambitions are fundamentally different.

• "Engineered organisms will work exactly as designed, like machines"
  Reality: Biological systems are fundamentally different from machines because they evolve, respond to environmental fluctuations, and contain molecular noise that creates variability in gene expression. A genetic circuit that works perfectly in a test tube may behave differently inside a living cell due to competition for cellular resources, environmental changes, and stochastic (random) fluctuations in molecular concentrations. The model shows that even well-designed circuits produce variable outputs and degrade over evolutionary time.
  Strategy: Lab reality: Show data from actual genetic circuits — the output is not a clean digital signal but a noisy distribution. A gene designed to be 'on' might be at 100% in some cells, 70% in others, and 0% in a few. Biology is analog, not digital.

• "If a synthetic organism escapes the lab it will take over the environment"
  Reality: Engineered organisms are almost always LESS fit than wild organisms in natural environments, not more. They carry metabolic burdens from synthetic circuits, lack adaptations to environmental stresses (UV radiation, predators, nutrient scarcity, temperature fluctuations), and have been optimized for laboratory conditions. A bacterium engineered to produce a chemical in a controlled bioreactor would likely be outcompeted by wild bacteria within days in a natural environment. The real biosafety concern is not dominance but unintended gene transfer to natural organisms through horizontal gene transfer — which is why genetic isolation mechanisms are included in biocontainment designs.
  Strategy: Thought experiment: Release a pampered house cat into the wilderness and a wild bobcat into the same territory. Which thrives? Engineered organisms are the house cats of biology — optimized for comfortable lab conditions, not survival in the wild.

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
Big Question: If we can write DNA from scratch like computer code, can we engineer entirely new forms of life — and what are the consequences if we do?
Answer: Synthetic biology can now write DNA from scratch, insert it into cells, and create organisms with functions that never existed in nature — from bacteria that detect and destroy cancer cells to yeast that produce antimalarial drugs. But creating truly new life is far more complex than writing genetic code. Every engineered organism is subject to evolution, which relentlessly selects for faster growth by shedding the metabolic burden of synthetic circuits. Complex engineered functions tend to be evolutionary unstable — the organism evolves to break them. Biocontainment is essential but imperfect — any single safety mechanism can be defeated by mutation. The power to write new genetic programs is real, but biology is not a computer. Cells are evolved systems that push back against engineering in ways that silicon never does.

Simulation Answers:
• Simple Biosensor Scenario: With a low-complexity circuit (one sensor gene and one reporter), the model shows minimal metabolic burden (less than 5% growth reduction), high evolutionary stability (functional over thousands of generations), and reliable output fidelity. The simple circuit presents a small mutational target, meaning few mutations can disable it, and the modest burden creates weak selective pressure for loss. This scenario demonstrates why the most commercially successful synthetic biology applications use relatively simple circuits — they align with rather than fight evolutionary dynamics.
• Complex Metabolic Pathway Scenario: With a high-complexity circuit (10+ genes), the model shows significant metabolic burden (20-40% growth reduction), rapidly declining evolutionary stability (function loss within 100-500 generations depending on burden level), and variable output fidelity. The large circuit presents many mutational targets — any of the 10+ genes can be disabled by point mutations, insertions, or deletions. The strong selective pressure for faster growth ensures that loss-of-function mutants quickly dominate the population. This scenario reveals why complex metabolic engineering remains challenging despite advances in DNA synthesis.

Reflection Exemplars:
• Q: Why is evolution both the tool and the enemy of synthetic biology?
  A: Evolution is the tool because all of synthetic biology relies on the cellular machinery that evolution created — DNA replication, transcription, translation, and metabolism are products of 4 billion years of evolutionary optimization. We reprogram these evolved systems to perform new functions. But evolution is also the enemy because it does not stop when we are done engineering. Every generation, mutations test whether the synthetic circuit helps or hinders the cell. Since engineered circuits almost always impose a metabolic cost, mutations that disable them provide a growth advantage. The model shows this clearly: within hundreds of generations, complex circuits are degraded by the same evolutionary process that created the cellular machinery we exploit.
• Q: Why are multiple biocontainment mechanisms essential?
  A: The model demonstrates that any single biocontainment mechanism has a finite failure rate — typically 10^-5 to 10^-8 per cell per generation, depending on the mechanism. In a culture of 10^9 bacteria, a 10^-6 escape frequency means approximately 1,000 potential escapees per generation. But if three independent mechanisms must ALL fail simultaneously, the combined escape frequency drops to 10^-18 — far fewer than one escapee in the lifetime of the universe for any reasonable culture size. The key word is independent — the mechanisms must fail through different mutational pathways so that a single mutation cannot defeat multiple systems. This is the biological equivalent of defense in depth in engineering.

STEM CHALLENGE GUIDANCE:
Title: Design a Synthetic Organism for Environmental Remediation
Mission: Design a synthetic organism engineered to break down a specific environmental pollutant, incorporating multiple biocontainment mechanisms and addressing evolutionary stability over deployment timescales.
Scenario: A chemical spill has contaminated a river with persistent organic pollutants that natural bacteria cannot efficiently degrade. Your team must design a synthetic bacterium engineered with a metabolic pathway to break down the pollutant, biocontainment mechanisms to prevent environmental persistence after the cleanup, and strategies to maintain the engineered function long enough to complete remediation before evolution disables it.
Introduction: Present the challenge: A chemical spill has contaminated a river with persistent organic pollutants that resist natural biodegradation. Your team must design a synthetic bacterium equipped with an engineered metabolic pathway to degrade the pollutant, multiple independent biocontainment mechanisms to prevent environmental persistence, and a strategy for maintaining engineered function long enough to complete remediation. Use your model to quantify the tradeoffs between circuit complexity, containment safety, and operational lifetime.

Key Concepts:
• Metabolic Pathway Engineering: Engineering a new metabolic pathway requires inserting multiple genes encoding enzymes that catalyze sequential chemical reactions. Each enzyme must function at the right level — too little and the pathway is bottlenecked, too much and the cell is overwhelmed. Balancing enzyme expression levels is one of the hardest practical challenges in synthetic biology.
• Kill Switch Design: A kill switch is a genetic circuit that produces a lethal toxin in response to a specific signal — such as the absence of a specific chemical found only in the laboratory. If the organism escapes to the environment where that chemical is absent, the kill switch activates and the cell dies. Advanced designs use multiple independent kill switches triggered by different signals.
• Directed Evolution: Rather than purely rational design, directed evolution uses cycles of mutation and selection to optimize engineered pathways. Organisms are mutagenized, screened for improved function, and the best performers are selected as parents for the next round. This harnesses evolution's power to improve designs that rational engineering cannot fully optimize.

Evaluation Rubric:
• Expert (4): Design includes a specific metabolic pathway with enzyme expression rationale, three or more independent biocontainment mechanisms with escape probability calculations, evolutionary stability strategy, environmental monitoring plan, and references model data for all key decisions
• Proficient (3): Design addresses degradation pathway, includes multiple containment mechanisms, and uses model evidence to justify stability predictions
• Developing (2): Design describes a general approach but lacks specific containment calculations or does not address evolutionary stability
• Beginning (1): Design is incomplete, relies on a single containment mechanism, or does not address the evolutionary stability challenge

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a visual genetic circuit diagram template showing how sensor, logic, and output genes connect, with standard biological part symbols
  • Use an evolutionary timeline showing predicted generations until circuit loss for different complexity levels, based on model data
  • Sentence frames: 'Our biocontainment system uses __ independent mechanisms: __, __, and __. If each has a failure rate of __, the combined escape probability is approximately __'

Extensions (Advanced Learners):
  • Research the Asilomar Conference on recombinant DNA (1975) and compare those early biosafety debates to today's discussions about synthetic biology — what has changed and what remains the same?
  • Investigate the iGEM (International Genetically Engineered Machine) competition and design a synthetic biology project that your team could theoretically enter, including all required biosafety documentation
  • Analyze the dual-use dilemma: the same synthetic biology techniques that create medicines and environmental solutions could theoretically create bioweapons. How should society regulate this technology without stifling beneficial innovation?

Cross-Curricular Connections:
  • Math: If a biocontainment mechanism has an escape frequency of 10^-6 per cell per generation, and a bioreactor contains 10^9 cells dividing every 30 minutes, how many potential escapees arise per day? How does adding a second independent mechanism (also 10^-6) change this calculation? A third?
  • ELA: Write a science fiction short story set 50 years in the future where synthetic organisms are commonplace — explore both the benefits and unintended consequences through a narrative that makes the science accessible to a general audience
  • Philosophy/Ethics: Debate: Does creating synthetic life from scratch cross a moral boundary? Consider perspectives from multiple philosophical traditions, religious viewpoints, and indigenous knowledge systems. Who has the right to create new forms of life?

CAST ALIGNMENT:
• Model how synthetic genetic circuit complexity relates to metabolic burden and evolutionary stability in engineered organisms
• Analyze the trade-off between organism functionality and biocontainment strength in synthetic biology applications
• Evaluate the probability of containment failure using multiple independent safety mechanisms versus single-point containment

CAST-Style Assessment Questions:
• Multiple Choice: A synthetic bacterium engineered with a 12-gene metabolic pathway shows declining pollutant degradation performance over 200 generations. According to your model, which variable most likely explains this decline?
• Constructed Response: Using evidence from your model, explain why a biocontainment system with three independent mechanisms is dramatically safer than one with a single mechanism. Calculate the approximate escape probability if each mechanism has a 10^-6 failure rate independently.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: Can Synthetic Biology Create New Life?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. What does it mean to 'engineer' a living organism, and how is it different from traditional genetic modification?

   _________________________________________________________

   _________________________________________________________

2. If scientists can write DNA from scratch, what do you think limits our ability to create entirely new organisms?

   _________________________________________________________

   _________________________________________________________

3. Draw a diagram showing how you think an engineered bacterium could be designed to perform a useful task, like cleaning up pollution.

   [DRAWING BOX]

4. What safety concerns would you have about releasing an engineered organism into the environment?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Synthetic Biology             
___ Genetic Circuit               
___ Metabolic Burden              
___ Biocontainment                
___ Minimal Genome                

A. An engineering discipline that designs and builds new biological parts, devices, and systems from standardized genetic components — treating DNA as a programming language and cells as programmable machines that can be engineered to perform novel functions
B. An engineered network of genes, promoters, and regulatory elements that functions like an electronic circuit — with biological logic gates (AND, OR, NOT) that process molecular inputs and produce specific protein outputs based on designed logic
C. The energy and resource cost that engineered genetic circuits impose on the host cell — synthetic genes compete with the cell's natural functions for ribosomes, amino acids, and ATP, and excessive burden causes growth defects and evolutionary instability
D. Safety mechanisms engineered into synthetic organisms to prevent them from surviving outside the laboratory — including kill switches, auxotrophies (dependence on nutrients not found in nature), and synthetic amino acid requirements that make environmental escape effectively impossible
E. The smallest set of genes required to sustain a free-living organism — Craig Venter's team created JCVI-syn3.0 with only 473 genes (compared to thousands in natural bacteria), establishing the minimum blueprint for life

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

SCENARIO: Simple Biosensor
Settings: Low complexity circuit with one sensor and one output gene, moderate containment
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Complex Metabolic Pathway
Settings: High complexity circuit with 10+ engineered genes, standard containment
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Containment Breach Test
Settings: Complex circuit with reduced biocontainment strength
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

1. How does your model demonstrate why evolution is both the central tool and the central obstacle in synthetic biology?

   _________________________________________________________

   _________________________________________________________

2. What does the relationship between circuit complexity and evolutionary stability tell you about the practical limits of genetic engineering?

   _________________________________________________________

   _________________________________________________________

3. Why must biocontainment use multiple independent mechanisms rather than a single safety system?

   _________________________________________________________

   _________________________________________________________

4. How would your model change if you could engineer organisms that are immune to mutation in their synthetic circuits?

   _________________________________________________________

   _________________________________________________________

5. What are the ethical boundaries of creating new forms of life, and who should draw those boundaries?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. If we can write DNA from scratch like computer code, can we engineer entirely new forms of life — and what are the consequences if we do? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Constructing Explanations and Designing Solutions
   □ Disciplinary Core Idea: LS1.A Structure and Function / LS3.A Inheritance of Traits
   □ Crosscutting Concept: Stability and Change

3. What are the ethical boundaries of creating new forms of life, and who should draw those boundaries?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Synthetic Organism for Environmental Remediation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design a synthetic organism engineered to break down a specific environmental pollutant, incorporating multiple biocontainment mechanisms and addressing evolutionary stability over deployment timescales.

SCENARIO: A chemical spill has contaminated a river with persistent organic pollutants that natural bacteria cannot efficiently degrade. Your team must design a synthetic bacterium engineered with a metabolic pathway to break down the pollutant, biocontainment mechanisms to prevent environmental persistence after the cleanup, and strategies to maintain the engineered function long enough to complete remediation before evolution disables it.

GUIDING QUESTIONS:
• How would you design the degradation pathway to minimize metabolic burden while maintaining pollutant breakdown efficiency?
• What biocontainment mechanisms would you layer to ensure the organism cannot persist in the environment after cleanup?
• How long must the engineered function remain stable, and what does your model predict about evolutionary timescales for circuit loss?

DESIGN THINKING:
• What specific genetic circuit design would you use to connect pollutant sensing to degradation enzyme expression?

  _________________________________________________________

• How many independent biocontainment mechanisms would you include and what type (kill switch, auxotrophy, synthetic amino acid)?

  _________________________________________________________

• What is your strategy for maintaining engineered function against evolutionary pressure during the deployment period?

  _________________________________________________________

• How would you monitor the synthetic organism in the field to detect containment failures or function loss?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Design includes a specific metabolic pathway with enzyme expression rationale, three or more independent biocontainment mechanisms with escape probability calculations, evolutionary stability strategy, environmental monitoring plan, and references model data for all key decisions
• Proficient (3): Design addresses degradation pathway, includes multiple containment mechanisms, and uses model evidence to justify stability predictions
• Developing (2): Design describes a general approach but lacks specific containment calculations or does not address evolutionary stability
• Beginning (1): Design is incomplete, relies on a single containment mechanism, or does not address the evolutionary stability challenge

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-11/G11L3-L05/G11L3-L05-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-11/G11L3-L05/G11L3-L05-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-11/G11L3-L05/G11L3-L05-Student-Presentation.pptx] |
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