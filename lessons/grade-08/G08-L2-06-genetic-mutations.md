# Lesson: Genetic Mutations: When DNA Makes a Typo

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G08L2-L06 |
| **Grade** | 8th |
| **Lesson Name** | Genetic Mutations: When DNA Makes a Typo |
| **Status** | Template |

---

## Platform

### Title
**Genetic Mutations: When DNA Makes a Typo — How UV Radiation and Cell Division Create Errors That Change Organisms**

### Overview
Students model how mutations arise from UV radiation and cell division, how they affect protein function, and why they matter for both disease and evolution. By building a computational model connecting environmental and cellular inputs to genetic and organism-level outputs, students discover that most mutations are neutral, some are harmful, and rarely, some are beneficial. This lesson connects genetics, cancer biology, and evolution.

### Cover Image
[Dramatic visualization of a DNA double helix with a glowing error section highlighted in red, molecular biology laboratory background]

### Grade
8th

### NGSS Standard
**MS-LS3-1**: Develop and use a model to describe why structural changes to genes (mutations) located on chromosomes may affect proteins and may result in harmful, beneficial, or neutral effects to the structure and function of the organism.
**MS-LS3-2**: Develop and use a model to describe why asexual reproduction results in offspring with identical genetic information and sexual reproduction results in offspring with genetic variation.

### Learning Objectives
- Explain how UV radiation and cell division rate affect mutation frequency
- Model the relationship between mutations, protein function, and organism fitness
- Predict whether mutations are likely to be harmful, beneficial, or neutral
- Evaluate evidence for why mutations are the raw material for evolution

### Component List (Starting Model: 5 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| UV Radiation Exposure | External | Intensity of ultraviolet light hitting cells |
| Cell Division Rate | External | How frequently cells divide and copy their DNA |
| Mutation Frequency | Internal | How often DNA copying errors occur per generation |
| Protein Function Change | Internal | Whether mutations alter protein shape and function |
| Organism Fitness | Internal | Overall survival and reproduction ability |

### Research for Lesson
- https://www.genome.gov/genetics-glossary/Mutation
- https://www.cancer.gov/about-cancer/causes-prevention/risk/sunlight
- https://learn.genetics.utah.edu/content/basics/mutation/

---

## Step 1: LOCATE — Build Your Mutation System

### Text Editor

```
GENETIC MUTATIONS: WHEN DNA MAKES A TYPO

Every time a cell divides, it copies 3 BILLION letters of DNA.
That's like typing out the entire contents of 1,000 thick novels —
perfectly, every single time. Except it's not perfect. Errors
happen. And when UV radiation damages the DNA on top of that?
More errors. A lot more.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• EXTERNAL (inputs that cause mutations):
  ○ "UV Radiation Exposure" — sunlight damages DNA bases
  ○ "Cell Division Rate" — each copy is another chance for error
• INTERNAL (things that respond):
  ○ "Mutation Frequency" — how often errors occur
  ○ "Protein Function Change" — whether the error matters
  ○ "Organism Fitness" — how the organism is affected overall

Task B: ADD TO YOUR MODEL — 5 components total

Task C: SORT YOUR COMPONENTS
• EXTERNAL = UV Radiation and Cell Division Rate
• INTERNAL = Mutation Frequency, Protein Function Change, Organism Fitness

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHY THIS SORTING MATTERS:
UV Radiation Exposure and Cell Division Rate are external because
they are inputs from outside the cell's genetic system. UV comes
from the environment and cell division rate is set by growth
signals. Mutation Frequency, Protein Function Change, and Organism
Fitness are internal because they are consequences that result
from DNA damage and copying errors.
```

### Video Script

```
"Your body copies 3 billion letters of DNA every time a cell
divides. Imagine copying a paragraph by hand a thousand times.
How many errors would you make?

Now imagine someone keeps shining a bright UV light at your paper,
damaging the letters as you try to copy them. More errors, right?

That's what happens inside your cells. UV radiation damages DNA.
Cell division copies it — errors and all. And those errors?
We call them mutations.

Today, you're going to model what causes mutations, what they do
to proteins, and why they matter for both your health and the
future of every species on Earth.

Two external inputs:
UV Radiation Exposure — sunlight damages DNA bases.
Cell Division Rate — each copy is another chance for error.

Three internal responses:
Mutation Frequency — how often errors happen.
Protein Function Change — whether the error changes anything.
Organism Fitness — what it means for the whole organism.

Sort them. Add them. Let's build.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 5 components sorted: UV Radiation and Cell Division Rate (External), Mutation Frequency, Protein Function Change, Organism Fitness (Internal)]

### Graph
[Empty graph panel]

---

## Step 2: ESTABLISH — Connect the Relationships

### Text Editor

```
TIME TO TRACE THE MUTATION PATHWAY

From sunlight to DNA damage to protein changes to organism
effects. Let's map the chain.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: DRAW YOUR RELATIONSHIPS
• UV Radiation Exposure → Mutation Frequency
• Cell Division Rate → Mutation Frequency
• Mutation Frequency → Protein Function Change
• Protein Function Change → Organism Fitness
• Organism Fitness → Cell Division Rate

Task B: SET POSITIVE OR NEGATIVE
  ○ UV Radiation → Mutation Frequency = POSITIVE (+)
    More UV causes more DNA damage, increasing mutation rate

  ○ Cell Division Rate → Mutation Frequency = POSITIVE (+)
    Faster division = more DNA copies = more chances for errors

  ○ Mutation Frequency → Protein Function Change = POSITIVE (+)
    More mutations = more chances a gene's code is altered

  ○ Protein Function Change → Organism Fitness = POSITIVE/NEGATIVE (+/−)
    Changed proteins can be harmful (most common), neutral (very
    common), or rarely beneficial. The net effect depends on WHICH
    proteins are affected

  ○ Organism Fitness → Cell Division Rate = POSITIVE (+)
    Healthier organisms maintain normal growth and division

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KEY INSIGHT: Both UV and fast division increase mutations, but
through different mechanisms. UV damages DNA directly. Fast
division creates more copying opportunities. The risks are additive.
```

### Video Script

```
"Let's trace the mutation pathway from sunlight to organism.

UV Radiation to Mutation Frequency. UV light causes chemical
changes to DNA bases — thymine dimers. These damaged bases get
copied incorrectly during the next cell division. More UV means
more damage means more mutations. POSITIVE.

Cell Division Rate to Mutation Frequency. Every time DNA is
copied, there's a chance for error. DNA polymerase makes about
1 mistake per billion bases — sounds rare, but with 3 billion
bases and millions of cell divisions per day, errors accumulate.
More divisions means more chances. POSITIVE.

Mutation Frequency to Protein Function Change. Mutations change
the DNA code, which can change the amino acid sequence, which can
change the protein's shape and function. More mutations means
more potential protein changes. POSITIVE.

Now here's the nuanced one. Protein Function Change to Organism
Fitness. This relationship goes BOTH ways. Most mutations are
neutral — the genetic code has redundancy, so many changes don't
alter the protein at all. Some are harmful — disrupting vital
functions. And very rarely, a mutation creates something BETTER.

About 70% neutral. 29% harmful. Less than 1% beneficial. But
that rare 1%? That's the raw material for evolution.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model: UV +→ Mutation Freq ←+ Cell Division, Mutation Freq +→ Protein Function +/−→ Organism Fitness +→ Cell Division Rate]

---

## Step 3: VISUALIZE & EVALUATE — Run Your Mutation Model

### Text Editor

```
TIME TO CRANK UP THE UV AND WATCH THE MUTATIONS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: SCENARIO 1 — NORMAL CONDITIONS
• Set UV Radiation and Cell Division Rate to moderate (50% each)
• Observe Mutation Frequency and Organism Fitness

Task B: SCENARIO 2 — HIGH UV EXPOSURE
• Lock UV Radiation to 90%
• What happens to Protein Function Change and Organism Fitness?

Task C: SCENARIO 3 — RAPID DIVISION
• Set Cell Division Rate to 90%, moderate UV
• How does this compare to high UV alone?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT TO LOOK FOR:

High UV Exposure: Mutation Frequency rises dramatically. Protein
Function Change increases. Organism Fitness gradually declines
because harmful mutations outnumber beneficial ones. This models
why chronic sun exposure increases cancer risk over time.

Rapid Division: Mutation Frequency also rises significantly —
each division is another copying opportunity. The effect is
similar to high UV but through a different mechanism. This
explains why rapidly dividing tissues like skin and gut lining
are more prone to cancer.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

REFLECTION QUESTIONS:
• Why are most mutations neutral rather than harmful?
• How does the model explain skin cancer risk from sun exposure?
• If mutations are mostly harmful, why are they evolution's fuel?
```

### Video Script

```
"Let's test the mutation model.

Normal conditions first. Moderate UV, moderate cell division.
Run it. Mutation Frequency is present but manageable. Organism
Fitness stays relatively stable. The body's DNA repair mechanisms
handle the normal error rate.

Now crank up the UV. Lock it to 90%. This is chronic, unprotected
sun exposure.

Watch Mutation Frequency spike. Protein Function Change rises as
more genes are affected. And Organism Fitness? It gradually
declines. Harmful mutations are accumulating faster than repair
can handle. Over years, this is exactly the pathway to skin cancer.

Now try the other route. Set Cell Division to 90% with moderate
UV. Rapid growth — like developing tissue or healing wounds.

Mutation Frequency rises again, but through a different mechanism.
More copies means more errors. This explains why rapidly dividing
cells — skin, gut lining, blood cells — have higher cancer risk
even without excessive UV exposure.

Here's the profound paradox: most individual mutations are neutral
or harmful. But across an entire population over many generations,
that rare beneficial mutation — less than 1% — provides the raw
material for natural selection. Without mutations, there would
be no genetic variation. Without variation, there would be no
evolution.

Mutations are dangerous to individuals but essential for species.

Now it's your turn to ModelIt!"
```

### Graph
[Screenshot showing High UV and Rapid Division scenarios with rising Mutation Frequency and declining Organism Fitness]

---

## Step 4: REVISE & EXTEND — Play, Research, Expand

### Text Editor

```
YOUR MODEL WORKS — BUT CELLS FIGHT BACK

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PLAY TIME CHALLENGES:

1. DOUBLE WHAMMY
   • Set BOTH UV and Cell Division to 90%
   • How does the combined effect compare to each alone?

2. FIND THE THRESHOLD
   • At what UV level does Organism Fitness start declining?
   • Is there a "safe" amount of UV exposure?

3. WHAT'S MISSING?
   • DNA Repair Mechanisms — cells fix most damage before it becomes permanent
   • Chemical Mutagen Exposure — smoke, chemicals damage DNA too
   • Cancer Risk — accumulated mutations in growth-control genes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

🔍 QUESTIONS TO INVESTIGATE:
   • How does CRISPR let scientists intentionally create mutations?
   • Why does cancer risk increase with age?
   • How do DNA repair enzymes work at the molecular level?
   • Why do some mutations cause genetic diseases while others drive adaptation?

🌐 RELIABLE SOURCES:
   • National Human Genome Research Institute: genome.gov
   • Learn Genetics Utah: learn.genetics.utah.edu
   • Cancer.gov: cancer.gov

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ADD TO YOUR MODEL and test!
```

### Video Script

```
"Your mutation model works. UV and cell division both increase
mutations. Most mutations are neutral, but the harmful ones
accumulate and reduce fitness.

But cells aren't defenseless. DNA repair enzymes scan the genome
constantly, fixing damage before the next division. What would
happen if you added a DNA Repair component? It would create a
NEGATIVE relationship to Mutation Frequency — reducing the
effective error rate.

Try it. Add repair. Run the model. How much does it buffer against
UV damage? At what point is the repair system overwhelmed?

That threshold — where damage exceeds repair capacity — is exactly
what happens with chronic sun exposure leading to skin cancer.

Now it's your turn to ModelIt!"
```

### Activity Network
[Screenshot showing expanded model with DNA Repair Mechanisms or Cancer Risk added]

---

## Fun Fact (Career Connection)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧬 CAREER CONNECTION: GENETIC COUNSELOR / MOLECULAR BIOLOGIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Genetic Counselors and Molecular Biologists study how mutations
affect health and disease. They help families understand genetic
risks and develop therapies that target specific mutations.

From CRISPR gene editing to personalized cancer treatment, these
scientists use their understanding of mutations to save lives.

💰 SALARY: $65,000 - $110,000/year

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## TPT Materials

### PowerPoint Slides

```
SLIDE 1: TITLE — "When DNA Makes a Typo"
SLIDE 2: LEARNING OBJECTIVES & VOCABULARY
SLIDE 3: BIG QUESTION — "What happens when DNA copies itself and makes a mistake?"
SLIDE 4: LEVER FRAMEWORK
SLIDE 5: ACTIVITY 1 — Mutation system components
SLIDE 6: ACTIVITY 2 — Mutation pathway connections
SLIDE 7: ACTIVITY 3 — UV and division rate scenarios
SLIDE 8: DISCOVERIES — 70% neutral, 29% harmful, <1% beneficial
SLIDE 9: STEM CHALLENGE — Skin cancer prevention campaign
```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: Genetic Mutations
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NGSS: MS-LS3-1, MS-LS3-2

THREE-DIMENSIONAL LEARNING:
• SEP: Developing and Using Models
• DCI: LS3.A Inheritance of Traits — mutations alter genes and proteins
• CCC: Cause and Effect — UV and division CAUSE mutations, protein
  changes are EFFECTS

LEVER FRAMEWORK:
• L: Identify UV radiation, cell division rate, mutation frequency,
  protein function change, and organism fitness.
• E: Both UV and division increase mutations; mutations change
  proteins; protein changes affect fitness positively or negatively.
• V: Build mutation model connecting inputs to genetic to organism
  level effects.
• Ev: Compare normal, high UV, and rapid division scenarios.
• R: Add DNA repair mechanisms or cancer risk.

PACING: ~53 minutes

SLIDE-BY-SLIDE:
Slide 1: "3 billion letters copied. What if there's a typo?"
Analogy: copy a paragraph 1,000 times by hand.
Slide 5: Sort components. UV and division are external inputs.
Slide 6: Map pathway. Discuss +/- nature of protein function
changes (can help OR hurt).
Slide 7: Students predict, then run. Compare UV vs. division
mechanisms.
Slide 8: Connect to cancer risk data. Sunscreen matters at the
molecular level.
Slide 9: Evidence-based prevention campaign for teens.

MISCONCEPTIONS:
• "Mutations are always harmful" → 70% neutral due to genetic
   code redundancy. Only critical region changes matter.
• "UV causes mutations instantly" → UV damages DNA but mutations
   happen during the NEXT cell division when damaged DNA is copied.
• "You can feel mutations happening" → Molecular-level events.
   Cancer from UV typically takes 20-30 years to develop.

BACKGROUND:
DNA polymerase: ~1 error/billion bases. UV causes thymine dimers.
Types: point, insertion, deletion, frameshift. Cancer requires
5-10 mutations in growth-control genes over a lifetime. SPF 30
blocks ~97% of UV-B rays.

DIFFERENTIATION:
Support: Visual DNA sequence showing before/after. Letter
substitution exercises. Sentence frames.
Challenge: Research CRISPR. Add DNA repair. Compare mutation rates
across organisms.
ELL: Visual vocabulary. Partner pairing.

CROSS-CURRICULAR:
• Math: Calculate mutation probability given error rate and divisions
• ELA: Write how a single mutation can lead to cancer, with evidence
• Social Studies: Compare sun protection education across countries

STEM CHALLENGE: Skin Cancer Prevention Campaign
Present: Dermatology clinic wants teen-focused, evidence-based
messaging about UV and skin cancer. No scare tactics. Use model
data. Key concepts: SPF, DNA repair, cumulative damage.

RUBRIC:
• Expert (4): Model data, mutation-cancer pathway, actionable
  recommendations, teen-appropriate design
• Proficient (3): Model evidence + two science-based strategies
• Developing (2): Mentions UV and cancer but lacks model data
• Beginning (1): Doesn't connect to mutation science

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: Genetic Mutations
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

PRE-ASSESSMENT
1. What is a mutation and what causes one?
   _________________________________________________________
2. Are most mutations harmful, helpful, or no effect? Why?
   _________________________________________________________
3. How might UV light affect your DNA?
   _________________________________________________________
4. Draw what happens to a protein when its gene has a mutation:
   [DRAWING BOX]

VOCABULARY
___ Mutation        A. Environmental factor increasing mutation rate
___ Mutagen         B. A change in DNA sequence
___ Protein Func.   C. An organism's survival and reproduction ability
___ Organism Fit.   D. The specific job a protein performs
___ Gene Expression E. Process of using gene info to produce a protein

MODEL PLANNING
EXTERNAL: _______________ _______________
INTERNAL: _______________ _______________ _______________

SIMULATION OBSERVATIONS
High UV (90%): Mutation Frequency: HIGH / LOW
Organism Fitness: DECLINED / STABLE
Rapid Division (90%): Mutation Frequency: HIGH / LOW
Compared to UV: SIMILAR EFFECT / VERY DIFFERENT

RESEARCH & EXTEND
New component: _________________ Effect: _________________

REFLECTION
1. Why are most mutations neutral?
   _________________________________________________________
2. How are mutations both dangerous AND essential for evolution?
   _________________________________________________________
3. Why does skin cancer risk increase with sun exposure?
   _________________________________________________________

POST-ASSESSMENT
1. Explain how UV radiation leads to mutations:
   _________________________________________________________
2. Why are rapidly dividing cells at higher cancer risk?
   _________________________________________________________
3. As a Genetic Counselor, what would you advise about UV exposure?
   _________________________________________________________

STEM CHALLENGE: Design a Skin Cancer Prevention Campaign
for teenagers using MODEL data, not scare tactics.
1. Key facts from model for messaging: _____________________
2. How to communicate risk without fear: ___________________
3. Specific protective behaviors to recommend: ______________
4. How to measure behavior change: _________________________

RUBRIC: Expert(4)/Proficient(3)/Developing(2)/Beginning(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CAST-Aligned Pre/Post Assessment

### Administration Instructions

5 questions aligned to MS-LS3-1 and MS-LS3-2.

---

### Question 1

Which components are external in a mutation model? A student has: UV Radiation, Cell Division Rate, Mutation Frequency, Protein Function Change, Organism Fitness.

A. UV Radiation and Mutation Frequency
B. UV Radiation and Cell Division Rate
C. Mutation Frequency and Protein Function Change
D. Cell Division Rate and Organism Fitness

Correct Answer: B

---

### Question 2

A mutation changes one amino acid in a protein. The organism shows no change in appearance or survival. What type of mutation is this?

A. Harmful — all mutations damage the organism
B. Beneficial — the protein must have improved
C. Neutral — the change didn't significantly affect protein function
D. Lethal — the organism will die eventually from accumulated damage

Correct Answer: C

Feedback: About 70% of point mutations are neutral due to redundancy in the genetic code and because many amino acid substitutions don't significantly alter protein shape or function.

---

### Question 3

Two tissues in the body: skin cells divide frequently; nerve cells rarely divide. Based on a mutation model, which prediction is correct?

A. Nerve cells accumulate more mutations because they are older.
B. Skin cells accumulate more mutations because each division is another chance for copying errors.
C. Both accumulate mutations at the same rate regardless of division.
D. Neither accumulates significant mutations during a normal lifespan.

Correct Answer: B

---

### Question 4

A student increases UV radiation in the model to 90% but sets Cell Division to 0%. What happens to Mutation Frequency?

A. Mutation Frequency increases dramatically because UV damages DNA.
B. Mutation Frequency stays low because mutations only occur during DNA copying, and no copying is happening.
C. Mutation Frequency increases, then decreases as the cell repairs itself.
D. Mutation Frequency is unpredictable without cell division data.

Correct Answer: B

Feedback: UV damages DNA, but that damage becomes a MUTATION only when the cell divides and copies the damaged DNA incorrectly. No division means no copying, so no new mutations are created from the damage.

---

### Question 5

Mutations are described as "the raw material for evolution." How can something mostly harmful be essential for species survival?

A. Harmful mutations strengthen species by killing off weak individuals.
B. Across large populations and many generations, the rare beneficial mutation provides new traits for natural selection to act on.
C. Mutations are actually mostly beneficial, but scientists haven't discovered the benefits yet.
D. Evolution doesn't actually require mutations — it works through environmental pressure alone.

Correct Answer: B

Feedback: While most individual mutations are neutral or harmful, across an entire population over many generations, the rare beneficial mutation introduces new genetic variation. Without mutations creating variation, natural selection would have nothing to select for, and evolution could not occur.

---

### Answer Key

Question 1: B | Question 2: C | Question 3: B | Question 4: B | Question 5: B

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (PDF) | [To be created] |
| Teacher Guide (PDF) | [To be created] |
| PPT Presentation | [To be created] |
| Platform Link | [ModelIt lesson link] |

---

## Lesson Metadata

| Field | Value |
|-------|-------|
| Created | March 2026 |
| Author | Alexandria's Design |
| Template Version | 1.0 |
| Platform | ModelIt (formerly Cell Collective) |
| Estimated Time | 50-55 minutes |
| Can Split Across | 2 class periods |
