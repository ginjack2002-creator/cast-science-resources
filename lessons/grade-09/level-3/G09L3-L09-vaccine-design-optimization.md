# Lesson: Vaccine Design Optimization

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G09L3-L09 |
| **Grade** | 9th Grade — Level 3: Biotech |
| **Lesson Name** | Vaccine Design Optimization |
| **Status** | Template |

---

## Platform

### Title
**Vaccine Design Optimization — Modeling Immune Response Engineering from Antigen Selection to Population-Level Protection**

### Overview
This lesson introduces students to computational vaccine design — one of the most important applications of immunological modeling. Biotech skill focus: Multi-objective optimization against an evolving target. The COVID-19 pandemic demonstrated both the power of rapid vaccine development and the challenges of designing durable protection against a mutating pathogen. Students investigate the driving question: COVID-19 vaccines were developed in under a year — a process that usually takes 10-15 years. How do computational models of the immune system make it possible to design vaccines faster, and can we design a universal vaccine that works against a virus that keeps mutating? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of diverse 14-15 year old students in an advanced immunology lab examining 3D models of antibody-antigen interactions on holographic displays, with vaccine vials and immune cell microscopy images visible, dramatic blue and white laboratory lighting]

### Grade
9th Grade — Level 3: Biotech

### NGSS Standard
**HS-LS1-4, HS-LS4-2**: Use a model to illustrate the role of cellular division in producing and maintaining complex organisms; construct an explanation based on evidence that the process of evolution primarily results from four factors.

### Learning Objectives
- Build an immune response model that traces the cascade from antigen presentation through immune cell activation to antibody production, memory formation, and population-level protection
- Analyze how antigen selection, adjuvant strength, and pathogen mutation rate interact to determine vaccine effectiveness and duration of immunity
- Optimize vaccine design parameters to maximize population coverage while accounting for viral evolution and immune diversity
- Evaluate the trade-offs between vaccine specificity (targeting one strain precisely) and cross-reactivity (providing broader but weaker protection against multiple variants)

### Component List (Starting Model: 9 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Antigen Selection | External | The choice of which pathogen molecular target to include in the vaccine — ideally a surface protein that is essential for pathogen function (so it cannot easily mutate away), highly immunogenic (triggers strong immune responses), and conserved across variants (so immunity is broadly protective) |
| Adjuvant Strength | External | The potency of the immune-stimulating compound included in the vaccine formulation — stronger adjuvants produce more robust immune responses but also increase the risk of inflammation and side effects (reactogenicity) |
| Immune Cell Activation | Internal | The degree to which innate immune cells (dendritic cells, macrophages) process and present the vaccine antigen to adaptive immune cells (T cells, B cells) — the critical bridge between innate recognition and adaptive immunity |
| Antibody Production Rate | Internal | The speed and magnitude of antibody secretion by activated B cells (plasma cells) — determines how quickly protective antibody levels are reached after vaccination and the peak antibody titer achieved |
| Memory Cell Formation | Internal | The differentiation of activated B cells and T cells into long-lived memory cells that persist for years to decades — the key determinant of how long vaccine-induced immunity lasts |
| Pathogen Mutation Rate | External | The speed at which the target pathogen accumulates mutations in its surface proteins — RNA viruses mutate 100-1000x faster than DNA viruses, creating new variants that may escape vaccine-induced immunity |
| Cross-Reactivity | Internal | The degree to which antibodies generated against the vaccine antigen also recognize and neutralize variant strains of the pathogen — broader cross-reactivity provides protection against future variants but typically with lower potency per variant |
| Duration of Immunity | Internal | The length of time that vaccine-induced protection remains above the threshold needed to prevent infection or severe disease — determined by memory cell longevity, antibody half-life, and the rate of pathogen antigenic drift |
| Population Coverage | Internal | The fraction of a genetically diverse population that achieves protective immunity from the vaccine — influenced by human genetic variation in immune response genes (HLA diversity), age-related immune differences, and immunocompromised individuals |

### Research for Lesson
- How Vaccines Work: The Immune Response Cascade — reference materials and textbook resources
- Antigen Selection: The Foundation of Vaccine Design — reference materials and textbook resources
- Adjuvants and Immune Amplification — reference materials and textbook resources
- The Evolutionary Arms Race: Pathogen Mutation and Immune Escape — reference materials and textbook resources

---

## Step 1: LOCATE — Build Your System

### Text Editor

```
VACCINE DESIGN OPTIMIZATION

Modeling Immune Response Engineering from Antigen Selection to Population-Level Protection.
COVID-19 vaccines were developed in under a year — a process that usually takes 10-15 years. How do computational models of the immune system make it possible to design vaccines faster, and can we design a universal vaccine that works against a virus that keeps mutating?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Antigen Selection" — the choice of which pathogen molecular target to include in the vaccine — ideally a surface protein that is essential for pathogen function (so it cannot easily mutate away)
  ○ Click "Adjuvant Strength" — the potency of the immune-stimulating compound included in the vaccine formulation — stronger adjuvants produce more robust immune responses but also increase the risk of inflammation and side effects (reactogenicity)
  ○ Click "Pathogen Mutation Rate" — the speed at which the target pathogen accumulates mutations in its surface proteins — rna viruses mutate 100-1000x faster than dna viruses
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Immune Cell Activation" — the degree to which innate immune cells (dendritic cells
  ○ Click "Antibody Production Rate" — the speed and magnitude of antibody secretion by activated b cells (plasma cells) — determines how quickly protective antibody levels are reached after vaccination and the peak antibody titer achieved
  ○ Click "Memory Cell Formation" — the differentiation of activated b cells and t cells into long-lived memory cells that persist for years to decades — the key determinant of how long vaccine-induced immunity lasts
  ○ Click "Cross-Reactivity" — the degree to which antibodies generated against the vaccine antigen also recognize and neutralize variant strains of the pathogen — broader cross-reactivity provides protection against future variants but typically with lower potency per variant
  ○ Click "Duration of Immunity" — the length of time that vaccine-induced protection remains above the threshold needed to prevent infection or severe disease — determined by memory cell longevity
  ○ Click "Population Coverage" — the fraction of a genetically diverse population that achieves protective immunity from the vaccine — influenced by human genetic variation in immune response genes (hla diversity)

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
"COVID-19 vaccines were developed in under a year — a process that usually takes 10-15 years. How do computational models of the immune system make it possible to design vaccines faster, and can we design a universal vaccine that works against a virus that keeps mutating?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Antigen Selection' — that's external. The choice of which pathogen molecular target to include in the vaccine — ideally a surface protein that is essential for pathogen function (so it cannot easily mutate away).
Click on 'Adjuvant Strength' — that's external. The potency of the immune-stimulating compound included in the vaccine formulation — stronger adjuvants produce more robust immune responses but also increase the risk of inflammation and side effects (reactogenicity).
Click on 'Immune Cell Activation' — that's internal. The degree to which innate immune cells (dendritic cells.
Click on 'Antibody Production Rate' — that's internal. The speed and magnitude of antibody secretion by activated B cells (plasma cells) — determines how quickly protective antibody levels are reached after vaccination and the peak antibody titer achieved.
Click on 'Memory Cell Formation' — that's internal. The differentiation of activated B cells and T cells into long-lived memory cells that persist for years to decades — the key determinant of how long vaccine-induced immunity lasts.
Click on 'Pathogen Mutation Rate' — that's external. The speed at which the target pathogen accumulates mutations in its surface proteins — RNA viruses mutate 100-1000x faster than DNA viruses.
Click on 'Cross-Reactivity' — that's internal. The degree to which antibodies generated against the vaccine antigen also recognize and neutralize variant strains of the pathogen — broader cross-reactivity provides protection against future variants but typically with lower potency per variant.
Click on 'Duration of Immunity' — that's internal. The length of time that vaccine-induced protection remains above the threshold needed to prevent infection or severe disease — determined by memory cell longevity.
Click on 'Population Coverage' — that's internal. The fraction of a genetically diverse population that achieves protective immunity from the vaccine — influenced by human genetic variation in immune response genes (HLA diversity).

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Antigen Selection, Adjuvant Strength, and Pathogen Mutation Rate are the three external components. Antigen Selection and Adjuvant Strength are design decisions made by the vaccinologist — which piece of the pathogen to include and how strongly to stimulate the immune response. Pathogen Mutation Rate is an external biological reality determined by the virus's replication fidelity and population dynamics — it is not under the vaccine designer's control but profoundly affects vaccine performance. All other six components are internal: Immune Cell Activation, Antibody Production Rate, Memory Cell Formation, Cross-Reactivity, Duration of Immunity, and Population Coverage emerge as biological responses to the vaccine design interacting with human immune physiology and pathogen evolution.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next step, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 9 components sorted: Antigen Selection, Adjuvant Strength, Pathogen Mutation Rate (External), Immune Cell Activation, Antibody Production Rate, Memory Cell Formation, Cross-Reactivity, Duration of Immunity, Population Coverage (Internal)]

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
• Click on "Antigen Selection" and drag an arrow to "Immune Cell Activation"
• Click on "Adjuvant Strength" and drag an arrow to "Immune Cell Activation"
• Click on "Immune Cell Activation" and drag an arrow to "Antibody Production Rate"
• Click on "Memory Cell Formation" and drag an arrow to "Duration of Immunity"
• Click on "Pathogen Mutation Rate" and drag an arrow to "Duration of Immunity"
• Click on "Cross-Reactivity" and drag an arrow to "Population Coverage"

Task C: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Antigen Selection → Immune Cell Activation = POSITIVE (+)
    More immunogenic antigens (those that are well-recognized by human immune system components) produce stronger dendritic cell activation and more effective antigen presentation to T cells, amplifying the downstream adaptive response.

  ○ Adjuvant Strength → Immune Cell Activation = POSITIVE (+)
    Stronger adjuvants activate more innate immune cells and induce higher levels of co-stimulatory molecules and cytokines, amplifying antigen presentation and lowering the activation threshold for adaptive immune cells.

  ○ Immune Cell Activation → Antibody Production Rate = POSITIVE (+)
    Greater immune cell activation produces more activated helper T cells, which provide stronger signals for B cell clonal expansion and differentiation into antibody-secreting plasma cells.

  ○ Memory Cell Formation → Duration of Immunity = POSITIVE (+)
    More robust memory cell differentiation creates larger and more diverse pools of long-lived memory B cells and T cells, enabling faster and stronger recall responses for longer periods after vaccination.

  ○ Pathogen Mutation Rate → Duration of Immunity = NEGATIVE (−)
    Faster pathogen mutation generates variants that escape vaccine-induced immune recognition more quickly, eroding the effective Duration of Immunity even when memory cells remain functional — because the virus changes, not the memory.

  ○ Cross-Reactivity → Population Coverage = POSITIVE (+)
    Broader cross-reactivity means the vaccine provides at least partial protection against more pathogen variants, increasing the fraction of the population that encounters a variant covered by their vaccine-induced immunity.

Task D: CHECK YOUR MODEL
• You should have 6 arrows total
• 1 negative relationship(s), 5 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: Vaccine design is a multi-dimensional optimization problem with no perfect solution. You want high Antibody Production Rate, but if Adjuvant Strength is too high, the side effects become unacceptable and people refuse the vaccine. You want strong Memory Cell Formation for long Duration of Immunity, but Pathogen Mutation Rate can outrun even robust memory responses — look at influenza, which requires a new vaccine every year. You want maximum Cross-Reactivity to cover all variants, but broader Cross-Reactivity usually means weaker response to any specific variant. And Population Coverage varies because of human genetic diversity in immune system genes (HLA types). How do you design a vaccine that balances all of these competing constraints — especially against a pathogen that is actively evolving to escape your vaccine?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Antigen Selection' and drag an arrow
over to 'Immune Cell Activation.'

Here's the key question: When antigen selection goes UP, does
immune cell activation go UP or DOWN?

More immunogenic antigens (those that are well-recognized by human immune system components) produce stronger dendritic cell activation and more effective antigen presentation to T cells, amplifying the downstream adaptive response.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Adjuvant Strength' and drag an arrow
over to 'Immune Cell Activation.'

Here's the key question: When adjuvant strength goes UP, does
immune cell activation go UP or DOWN?

Stronger adjuvants activate more innate immune cells and induce higher levels of co-stimulatory molecules and cytokines, amplifying antigen presentation and lowering the activation threshold for adaptive immune cells.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'Immune Cell Activation' and drag an arrow
over to 'Antibody Production Rate.'

Here's the key question: When immune cell activation goes UP, does
antibody production rate go UP or DOWN?

Greater immune cell activation produces more activated helper T cells, which provide stronger signals for B cell clonal expansion and differentiation into antibody-secreting plasma cells.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Final connection: Click on 'Memory Cell Formation' and drag an arrow
over to 'Duration of Immunity.'

Here's the key question: When memory cell formation goes UP, does
duration of immunity go UP or DOWN?

More robust memory cell differentiation creates larger and more diverse pools of long-lived memory B cells and T cells, enabling faster and stronger recall responses for longer periods after vaccination.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Final connection: Click on 'Pathogen Mutation Rate' and drag an arrow
over to 'Duration of Immunity.'

Here's the key question: When pathogen mutation rate goes UP, does
duration of immunity go UP or DOWN?

Faster pathogen mutation generates variants that escape vaccine-induced immune recognition more quickly, eroding the effective Duration of Immunity even when memory cells remain functional — because the virus changes, not the memory.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Cross-Reactivity' and drag an arrow
over to 'Population Coverage.'

Here's the key question: When cross-reactivity goes UP, does
population coverage go UP or DOWN?

Broader cross-reactivity means the vaccine provides at least partial protection against more pathogen variants, increasing the fraction of the population that encounters a variant covered by their vaccine-induced immunity.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Look at your model now. You've got 1 negative and 5
positive relationships. 6 arrows total.

Vaccine design is a multi-dimensional optimization problem with no perfect solution. You want high Antibody Production Rate, but if Adjuvant Strength is too high, the side effects become unacceptable and people refuse the vaccine. You want strong Memory Cell Formation for long Duration of Immunity, but Pathogen Mutation Rate can outrun even robust memory responses — look at influenza, which requires a new vaccine every year. You want maximum Cross-Reactivity to cover all variants, but broader Cross-Reactivity usually means weaker response to any specific variant. And Population Coverage varies because of human genetic diversity in immune system genes (HLA types). How do you design a vaccine that balances all of these competing constraints — especially against a pathogen that is actively evolving to escape your vaccine?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Antigen Selection +→ Immune Cell Activation, Adjuvant Strength +→ Immune Cell Activation, Immune Cell Activation +→ Antibody Production Rate, Memory Cell Formation +→ Duration of Immunity, Pathogen Mutation Rate −→ Duration of Immunity, Cross-Reactivity +→ Population Coverage]

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
• When Antigen Selection is HIGH, what happens to the internal components?

Task C: SCENARIO — STRAIN-SPECIFIC
• Dominant strain antigen, moderate adjuvant
• PREDICT FIRST: What do you predict happens to vaccine effectiveness when a new variant emerges with mutations in the target antigen?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task D: SCENARIO — BROADLY PROTECTIVE
• Conserved region antigen, strong adjuvant
• PREDICT FIRST: Do you predict that targeting a conserved region provides better long-term protection despite lower peak antibody levels?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task E: SCENARIO — HIGH-MUTATION CHALLENGE
• Fast-mutating pathogen, any vaccine design
• PREDICT FIRST: How quickly do you predict the pathogen will evolve to escape vaccine-induced immunity at maximum Pathogen Mutation Rate?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• There is a fundamental trade-off between vaccine specificity and breadth — vaccines targeting strain-specific epitopes generate stronger antibody responses but are vulnerable to antigenic drift, while vaccines targeting conserved regions are more durable but less potent
• Adjuvant strength has diminishing returns — moderate adjuvant produces significantly better immune responses than no adjuvant, but very strong adjuvant increases side effects faster than it increases protection, reducing real-world uptake and Population Coverage
• Memory Cell Formation is the most critical component for long-term protection — even when circulating antibodies wane, robust immunological memory enables rapid recall responses that prevent severe disease upon re-exposure
• Population Coverage is limited by human genetic diversity — HLA (human leukocyte antigen) variation means the same vaccine antigen is presented differently to immune cells in different people, making universal vaccine design for genetically diverse populations inherently challenging

THE ANSWER: Vaccine design is fundamentally an optimization problem with competing constraints. The nine components of this model capture the core trade-offs: Antigen Selection determines what the immune system learns to recognize — too specific and variants escape, too conserved and the response is weak. Adjuvant Strength amplifies the immune response but with side-effect trade-offs. Immune Cell Activation bridges innate and adaptive immunity. Antibody Production Rate and Memory Cell Formation determine short-term and long-term protection respectively. Pathogen Mutation Rate is the adversary — constantly generating variants that test the breadth of vaccine-induced immunity. Cross-Reactivity is the defense against mutation, but it comes at the cost of per-variant potency. Duration of Immunity depends on the race between memory persistence and antigenic drift. And Population Coverage reflects the reality that human immune systems are genetically diverse, meaning no single vaccine design is optimal for every individual. Computational modeling allows vaccinologists to simulate thousands of antigen-adjuvant combinations against evolving pathogen populations in diverse human genetics — identifying the design sweet spot before committing to expensive clinical trials.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Strain-Specific. Dominant strain antigen, moderate adjuvant.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Broadly Protective.
Conserved region antigen, strong adjuvant.

Before you run it — make a prediction. Do you predict that targeting a conserved region provides better long-term protection despite lower peak antibody levels?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: High-Mutation Challenge. Fast-mutating pathogen, any vaccine design.
How quickly do you predict the pathogen will evolve to escape vaccine-induced immunity at maximum Pathogen Mutation Rate?

Here's what our model reveals: Vaccine design is fundamentally an optimization problem with competing constraints. The nine components of this model capture the core trade-offs: Antigen Selection determines what the immune system learns to recognize — too specific and variants escape, too conserved and the response is weak. Adjuvant Strength amplifies the immune response but with side-effect trade-offs. Immune Cell Activation bridges innate and adaptive immunity. Antibody Production Rate and Memory Cell Formation determine short-term and long-term protection respectively. Pathogen Mutation Rate is the adversary — constantly generating variants that test the breadth of vaccine-induced immunity. Cross-Reactivity is the defense against mutation, but it comes at the cost of per-variant potency. Duration of Immunity depends on the race between memory persistence and antigenic drift. And Population Coverage reflects the reality that human immune systems are genetically diverse, meaning no single vaccine design is optimal for every individual. Computational modeling allows vaccinologists to simulate thousands of antigen-adjuvant combinations against evolving pathogen populations in diverse human genetics — identifying the design sweet spot before committing to expensive clinical trials.

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
   • What happens if you turn OFF Antigen Selection?
   • What happens if you turn OFF Adjuvant Strength?
   • What happens if you turn OFF Pathogen Mutation Rate?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • T Cell Response Quality — The robustness of the cytotoxic T cell (killer T cell) response to the vaccine — while antibodies prevent infection, T cells destroy already-infected cells, providing a critical second line of defense that is often more durable and cross-reactive than antibody responses
   • Delivery Platform Efficiency — The technology used to present the antigen to the immune system — mRNA (rapid design, strong response, cold storage required), protein subunit (stable, well-understood, weaker response), viral vector (strong response, anti-vector immunity limits boosting), and nanoparticle (multivalent display, complex manufacturing)
   • Immune Imprinting Effect — The tendency of the immune system to preferentially recall its first response to a pathogen family rather than mounting a de novo response to new variants — original antigenic sin can reduce the effectiveness of updated vaccines by biasing the immune response toward the original strain

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • How Vaccines Work: The Immune Response Cascade — how does this connect to your model?
   • Antigen Selection: The Foundation of Vaccine Design — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model demonstrate the fundamental trade-off between vaccine specificity and cross-reactivity breadth?
   • Why is Pathogen Mutation Rate the most challenging component for long-term vaccine design — and how does Antigen Selection strategy affect vulnerability to antigenic drift?
   • What did the model reveal about the relationship between Adjuvant Strength and real-world Population Coverage — why doesn't 'stronger adjuvant' always mean 'better vaccine'?
   • How would adding Immune Imprinting Effect change your model's predictions about booster vaccine effectiveness?

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

T Cell Response Quality. The robustness of the cytotoxic T cell (killer T cell) response to the vaccine — while antibodies prevent infection, T cells destroy already-infected cells, providing a critical second line of defense that is often more durable and cross-reactive than antibody responses
How would you model that?

Delivery Platform Efficiency. The technology used to present the antigen to the immune system — mRNA (rapid design, strong response, cold storage required), protein subunit (stable, well-understood, weaker response), viral vector (strong response, anti-vector immunity limits boosting), and nanoparticle (multivalent display, complex manufacturing)
How would you model that?

Immune Imprinting Effect. The tendency of the immune system to preferentially recall its first response to a pathogen family rather than mounting a de novo response to new variants — original antigenic sin can reduce the effectiveness of updated vaccines by biasing the immune response toward the original strain
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

Vaccine Immunologists and Vaccinologists design and evaluate vaccines using computational modeling, animal studies, and clinical trials. They work for pharmaceutical companies (Pfizer, Moderna, GSK), biotech startups, government agencies (NIH, CDC, BARDA), and global health organizations (WHO, CEPI, Gavi), earning $100,000-$220,000/year. Computational Immunologists who model immune responses earn $90,000-$180,000/year.

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
Visual: Title slide with dramatic imagery of vaccine vials, viral particles, and antibody structures
Say: "COVID-19 vaccines went from genetic sequence to emergency authorization in 11 months. The previous record was 4 years. How did computational modeling make this possible — and can we design vaccines that never need updating?"
Do: Display the timeline comparison: traditional vaccine development (10-15 years) versus COVID-19 (11 months). Ask: What changed? What role did modeling play?
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals with immunology vocabulary
Say: "Today you're vaccine designers. You'll learn why vaccine design is one of the hardest optimization problems in biology — because your target is literally evolving to escape you."
Do: Pre-teach antigen and adjuvant. Use the analogy: an antigen is a 'wanted poster' that teaches your immune system what to look for; an adjuvant is the megaphone that makes sure the immune system pays attention.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: Can we design a universal vaccine that outruns viral evolution?
Say: "You need a new flu vaccine every year because the virus mutates its surface proteins. But you only need one measles vaccine for life. What's different about measles? Can we make flu behave more like measles?"
Do: Think-pair-share: Why do some vaccines last a lifetime while others need annual updating? What properties of the virus and the vaccine determine durability? Collect hypotheses.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps with immunology and evolutionary biology context
Say: "We're modeling the full cascade: from what you put in the vaccine to how the immune system responds to whether protection lasts when the virus mutates. And the virus IS mutating — that's the adversary in this model."
Do: Preview LEVER steps. Emphasize the unique challenge: this model has an adversarial component (Pathogen Mutation Rate) that actively works against the vaccine design.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Nine component cards spanning vaccine design, immune response, and protection outcome levels
Say: "Three of these nine components are inputs. Two you control (Antigen Selection, Adjuvant Strength). One you DON'T control (Pathogen Mutation Rate) — and it's working against you. Sort them."
Do: Guide sorting of external versus internal components. Emphasize the adversarial nature of Pathogen Mutation Rate as an uncontrollable external input that actively undermines vaccine effectiveness.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Immune response cascade from vaccine injection through memory formation to population protection
Say: "The specificity-breadth trade-off is the central tension. A sniper rifle (strain-specific) or a shotgun (broadly protective)? Each has advantages. Each has costs."
Do: Students map the immune cascade from antigen presentation through B cell and T cell activation to antibody and memory cell outputs. Trace how Antigen Selection choice propagates through Cross-Reactivity to Duration of Immunity.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Vaccine effectiveness over time under different mutation pressures
Say: "Design your vaccine. Now watch what happens when the virus starts mutating. Which design strategy holds up best over 2 years of viral evolution?"
Do: Students design their preferred vaccine strategy, predict performance, then simulate all three scenarios. The high-mutation challenge is the key insight — demonstrating how quickly strain-specific immunity erodes.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key vaccine design insights and real-world applications
Say: "You just discovered why we still don't have a universal flu vaccine after 80 years of trying — and why the mRNA platform that made COVID vaccines possible might finally crack this problem."
Do: Connect model findings to real vaccine development challenges. Discuss mRNA platform advantages for rapid variant-updated vaccine design.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Universal influenza vaccine design challenge
Say: "The WHO just gave your lab a billion dollars. Design the universal flu vaccine that ends annual flu shots forever. What do you target? How do you prove it works? Go."
Do: Groups design universal influenza vaccine strategies: antigen selection rationale, adjuvant choice, delivery platform, clinical trial design, and projections for cross-reactivity breadth. Present and defend.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: Vaccine Design Optimization
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
This lesson introduces students to computational vaccine design — one of the most important applications of immunological modeling. Biotech skill focus: Multi-objective optimization against an evolving target. The COVID-19 pandemic demonstrated both the power of rapid vaccine development and the challenges of designing durable protection against a mutating pathogen.

NGSS ALIGNMENT:
HS-LS1-4, HS-LS4-2: Use a model to illustrate the role of cellular division in producing and maintaining complex organisms; construct an explanation based on evidence that the process of evolution primarily results from four factors.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Developing and Using Models / Constructing Explanations
  Students develop an immune response model that connects molecular antigen-antibody interactions to cellular immune activation to population-level epidemiological outcomes, constructing explanations for vaccine design trade-offs.
• Disciplinary Core Idea: LS1.A Structure and Function / LS4.C Adaptation
  Immune system cells have specialized structures that enable antigen recognition, antibody production, and immunological memory; pathogen adaptation through mutation creates an evolutionary arms race that constrains vaccine design.
• Crosscutting Concept: Cause and Effect / Structure and Function
  Students trace causal chains from antigen molecular structure through immune cell recognition to antibody specificity and population-level protection, analyzing how pathogen structural evolution disrupts vaccine-induced immunity.

PACING GUIDE:
• Step 1 (Locate): 8-10 minutes
• Step 2 (Establish): 8-10 minutes
• Step 3 (Visualize & Evaluate): 10-12 minutes
• Step 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Antigen, Adjuvant, Immunological Memory, Antigenic Drift
□ Prepare COVID-19 vaccines were developed in under a year — a process that usually takes 10-15 years. How do computational models of the immune system make it possible to design vaccines faster, and can we design a universal vaccine that works against a virus that keeps mutating discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify nine components spanning vaccine design inputs (Antigen Selection, Adjuvant Strength, Pathogen Mutation Rate), immune response dynamics (Immune Cell Activation, Antibody Production Rate, Memory Cell Formation), and protection outcomes (Cross-Reactivity, Duration of Immunity, Population Coverage).
• Establish: Students determine that Antigen Selection, Adjuvant Strength, and Pathogen Mutation Rate are external inputs — two under the vaccinologist's control and one representing the evolutionary adversary — while Immune Cell Activation, Antibody Production Rate, Memory Cell Formation, Cross-Reactivity, Duration of Immunity, and Population Coverage emerge as biological responses.
• Visualize: Students build an immune response model connecting vaccine inputs through immune cell activation and antibody production to protection outcomes, visualizing the trade-offs between specificity and breadth, potency and safety, and short-term and long-term protection.
• Evaluate: Students run strain-specific, broadly-protective, and high-mutation-challenge scenarios to discover how antigen selection strategy determines vulnerability to pathogen evolution.
• Revise: Students add T Cell Response Quality, Delivery Platform Efficiency, or Immune Imprinting Effect to explore additional dimensions of vaccine design optimization.

BACKGROUND CONTENT:
• How Vaccines Work: The Immune Response Cascade:
  Vaccines exploit the adaptive immune system's ability to learn and remember. When a vaccine antigen is injected, innate immune cells (dendritic cells, macrophages) engulf and process it, presenting peptide fragments on their surface via MHC (major histocompatibility complex) molecules. Helper T cells recognize these presented peptides and activate, releasing cytokines that drive B cell activation. Activated B cells with receptors that match the antigen undergo clonal expansion (rapid division) and affinity maturation (mutation and selection for tighter antigen binding). Some activated B cells differentiate into plasma cells that secrete large quantities of antibodies; others become long-lived memory B cells. Simultaneously, cytotoxic T cells are activated to kill cells displaying the target peptides. The entire process takes 1-2 weeks for a primary response but only 1-3 days for a secondary (memory) response — which is why vaccines work: the memory response is fast enough to clear the pathogen before it causes disease.

• Antigen Selection: The Foundation of Vaccine Design:
  The choice of antigen determines everything else about a vaccine. An ideal antigen is: immunodominant (strongly recognized by diverse immune systems), essential for pathogen function (the pathogen cannot easily mutate it without losing fitness), surface-exposed (accessible to antibodies), and conserved across variants (mutations in this region are rare). In practice, these criteria often conflict. The SARS-CoV-2 spike protein receptor-binding domain (RBD) is highly immunodominant and surface-exposed but also rapidly mutating because it is under intense immune selection pressure. The spike protein's fusion machinery (S2 subunit) is more conserved but less immunodominant. The internal nucleoprotein is highly conserved but not accessible to antibodies (though T cells can target it). Computational modeling allows vaccinologists to evaluate thousands of potential antigen designs against simulated pathogen evolution, identifying targets that balance immunogenicity with conservation.

• Adjuvants and Immune Amplification:
  Purified protein antigens alone often produce weak immune responses — the adaptive immune system needs 'danger signals' from the innate immune system to mount a full response. Adjuvants provide these danger signals. Aluminum salts (alum) — the oldest and most common adjuvant — create a depot effect that prolongs antigen exposure and activate inflammasome pathways. AS01B (used in the Shingrix shingles vaccine) combines a toll-like receptor agonist with a saponin to produce exceptionally strong immune responses. MF59 (an oil-in-water emulsion) enhances antigen uptake by dendritic cells. mRNA vaccines use the lipid nanoparticle delivery system as a built-in adjuvant because the mRNA itself activates innate immune sensors. The choice of adjuvant determines the magnitude, quality, and durability of the immune response — but stronger adjuvants also produce more local and systemic reactogenicity (injection site pain, fever, fatigue), which affects public acceptance and population-level uptake.

• The Evolutionary Arms Race: Pathogen Mutation and Immune Escape:
  Vaccination creates a selection pressure on the pathogen: viral variants that can evade vaccine-induced immunity have a fitness advantage and become dominant. This is antigenic drift — the gradual accumulation of mutations in immune-targeted surface proteins. Influenza A virus mutates its hemagglutinin (HA) surface protein at a rate of approximately 4-6 amino acid substitutions per year, sufficient to require annual vaccine reformulation. SARS-CoV-2 demonstrated even faster antigenic evolution, with new variants of concern emerging every few months during the pandemic. The fundamental challenge for vaccine design is that the pathogen is not a static target — it is an evolving adversary that actively adapts to escape immune pressure. Computational models that co-simulate vaccine-induced immune responses AND pathogen evolution are essential for designing vaccines that maintain effectiveness over time.

COMMON MISCONCEPTIONS:
• "Vaccines give you a weakened version of the disease"
  Reality: While some historical vaccines used weakened (attenuated) live virus, most modern vaccines do NOT contain any live pathogen. Subunit vaccines contain only purified proteins. mRNA vaccines contain instructions for the body to make one viral protein (not the whole virus). Inactivated vaccines contain killed virus that cannot replicate. None of these can cause the disease they protect against. The immune system responds to the molecular shape of the antigen, not to the disease process itself.
  Strategy: Categorize: List 5 vaccines and their type (live attenuated, inactivated, subunit, mRNA, viral vector). Which ones contain live virus? Which cannot possibly cause infection? How does the immune response compare?

• "If a vaccine doesn't prevent infection 100%, it doesn't work"
  Reality: Vaccines provide a SPECTRUM of protection, not a binary shield. Even when a vaccine doesn't prevent infection entirely, it typically: reduces symptom severity by 70-90%, reduces hospitalization by 80-95%, reduces death by 90-99%, and reduces transmission by 40-60%. The model's Population Coverage component shows that even partially effective vaccines dramatically reduce disease burden at the population level through herd immunity effects and reduced transmission.
  Strategy: Calculate: If a vaccine is 70% effective at preventing infection and 95% effective at preventing hospitalization, what happens to hospital overcrowding during a pandemic if 80% of the population is vaccinated versus 20%?

• "Natural immunity is always better than vaccine immunity"
  Reality: Natural infection sometimes produces stronger immunity than vaccination — but at the cost of suffering the actual disease, with its risks of hospitalization, long-term complications, and death. The model shows that vaccines can be designed to optimize specific aspects of immunity (like Memory Cell Formation and Cross-Reactivity) that natural infection may not optimally stimulate. Adjuvants and delivery platforms can direct the immune response toward the most protective pathways. Furthermore, vaccines can target conserved epitopes that natural infection may not prominently expose to the immune system.
  Strategy: Thought experiment: If natural COVID infection gives stronger antibodies but also has a 1% chance of killing you, and the vaccine gives somewhat weaker antibodies with a 0.001% chance of serious side effects — which is the better population-level strategy? At what risk level would natural immunity become preferable?

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
Big Question: COVID-19 vaccines were developed in under a year — a process that usually takes 10-15 years. How do computational models of the immune system make it possible to design vaccines faster, and can we design a universal vaccine that works against a virus that keeps mutating?
Answer: Vaccine design is fundamentally an optimization problem with competing constraints. The nine components of this model capture the core trade-offs: Antigen Selection determines what the immune system learns to recognize — too specific and variants escape, too conserved and the response is weak. Adjuvant Strength amplifies the immune response but with side-effect trade-offs. Immune Cell Activation bridges innate and adaptive immunity. Antibody Production Rate and Memory Cell Formation determine short-term and long-term protection respectively. Pathogen Mutation Rate is the adversary — constantly generating variants that test the breadth of vaccine-induced immunity. Cross-Reactivity is the defense against mutation, but it comes at the cost of per-variant potency. Duration of Immunity depends on the race between memory persistence and antigenic drift. And Population Coverage reflects the reality that human immune systems are genetically diverse, meaning no single vaccine design is optimal for every individual. Computational modeling allows vaccinologists to simulate thousands of antigen-adjuvant combinations against evolving pathogen populations in diverse human genetics — identifying the design sweet spot before committing to expensive clinical trials.

Simulation Answers:
• Strain-Specific Vaccine Scenario: With a highly specific antigen targeting the dominant circulating strain, Immune Cell Activation and Antibody Production Rate are high — the immune system generates a strong, focused response. Cross-Reactivity is low because the antibodies precisely fit only the target strain's epitopes. Initially, this vaccine provides excellent protection with high efficacy. However, when Pathogen Mutation Rate generates new variants with changes in the targeted epitope, Duration of Immunity drops sharply. The vaccine becomes ineffective against the new variant within 6-18 months, requiring reformulation — exactly the problem with current seasonal flu vaccines.
• High-Mutation Pathogen Challenge Scenario: At maximum Pathogen Mutation Rate, the adversarial nature of viral evolution is starkly visible. Regardless of initial vaccine design, the pathogen generates escape variants on a timeline of months. Strain-specific vaccines lose efficacy first. Broadly protective vaccines maintain partial protection longer due to Cross-Reactivity, but even conserved regions accumulate some variation over time. The model demonstrates that no single vaccination event can provide permanent protection against a rapidly-evolving pathogen — ongoing surveillance, updated formulations, or universal vaccine approaches targeting highly conserved essential structures are necessary.

Reflection Exemplars:
• Q: What is the specificity-breadth trade-off in vaccine design?
  A: The model reveals a fundamental immunological trade-off: antibodies that bind one specific epitope with very high affinity (high specificity) typically cannot bind variant epitopes with different shapes (low cross-reactivity). Conversely, antibodies that recognize a broader range of variant structures (high cross-reactivity) typically bind each individual variant with lower affinity (lower per-variant potency). This is because antibody binding sites are shaped to be complementary to their target — the more precisely they fit one target, the less they fit related but different targets. Vaccine Antigen Selection determines where on this spectrum the immune response falls: strain-specific antigens drive high-affinity, narrow responses; conserved-region antigens drive lower-affinity, broader responses.
• Q: Why does Pathogen Mutation Rate erode immunity even when Memory Cell Formation is strong?
  A: Memory cells remember the SPECIFIC antigen they were trained on. When the pathogen mutates its surface proteins, the memory cells still remember the old version perfectly — but the new version looks different enough that memory cell recognition is weakened or lost entirely. This is not a failure of immunological memory; it's a success of pathogen evolution. The model shows that Duration of Immunity depends not just on how well the immune system remembers, but on whether the pathogen remains recognizable to what the immune system remembers. This is why targeting highly conserved, functionally essential regions is the key strategy for durable protection — the pathogen cannot mutate these regions without losing fitness.

STEM CHALLENGE GUIDANCE:
Title: Design a Universal Influenza Vaccine Strategy
Mission: Design a vaccine strategy that provides broad, long-lasting protection against influenza — eliminating the need for annual reformulation by targeting conserved viral elements.
Scenario: The WHO has launched a $1 billion initiative to develop a universal influenza vaccine — one that works against all flu strains and doesn't need to be redesigned every year. Current seasonal flu vaccines are only 20-60% effective because they target rapidly-mutating surface proteins (hemagglutinin head). Your immunology team must design a vaccine strategy that targets conserved viral elements to provide durable, broadly protective immunity.
Introduction: Present the challenge: The WHO has launched a $1 billion initiative to develop a universal influenza vaccine that eliminates the need for annual reformulation. Current flu vaccines are only 20-60% effective because they target rapidly-mutating surface proteins. Your immunology team will design a vaccine strategy targeting conserved viral elements for durable, broadly protective immunity.

Key Concepts:
• Conserved Antigen Targeting: Influenza has several conserved protein regions that cannot easily mutate without losing viral fitness: the hemagglutinin stalk domain (required for membrane fusion), the M2 ion channel ectodomain (required for viral uncoating), and internal proteins like nucleoprotein (NP) and matrix protein (M1) that are essential for replication. Each has different advantages: HA stalk antibodies can neutralize the virus directly; M2e antibodies recruit immune cells to kill infected cells; NP-specific T cells provide cross-reactive cellular immunity. A multi-antigen approach may be necessary.
• mRNA Platform Advantages: mRNA vaccine technology offers unique advantages for universal vaccine design: rapid sequence modification (weeks versus months for protein vaccines), ability to encode multiple antigens in one formulation, strong activation of both antibody and T cell responses, and self-adjuvanting properties of the lipid nanoparticle delivery system. mRNA vaccines can be quickly updated when new conserved antigen designs are identified through computational modeling.
• Clinical Trial Design for Broadly Protective Vaccines: Proving that a universal vaccine works is uniquely challenging because you need to demonstrate protection against strains that haven't emerged yet. Strategies include: testing against historically diverse archived strains in laboratory neutralization assays, animal challenge studies with multiple divergent strains, human challenge studies with controlled infection, and computational modeling of predicted protection against simulated future variants based on known evolutionary trajectories.

Evaluation Rubric:
• Expert (4): Strategy includes justified conserved antigen selection with evolutionary analysis, platform rationale, multi-antigen design consideration, clinical trial plan for broad protection, and population coverage analysis supported by model predictions
• Proficient (3): Strategy includes antigen selection targeting conserved regions with reasoning connected to model trade-offs and basic clinical validation approach
• Developing (2): Strategy identifies conserved targets but lacks detail on platform selection, breadth validation, or population coverage considerations
• Beginning (1): Strategy is incomplete or does not connect antigen selection to the immune response model's specificity-breadth trade-off

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a visual diagram of the immune response cascade from vaccine injection through antigen presentation, T cell and B cell activation, to antibody production and memory formation
  • Use an antigen comparison table: 'Antigen: ___, Conservation level: ___/10, Immunogenicity: ___/10, Surface accessible: Y/N, Cross-reactivity prediction: ___'
  • Scaffold the evolutionary trade-off: 'If I target the most immunogenic epitope, it will mutate in ___ months. If I target the most conserved epitope, my antibody levels will be ___% lower. The optimal strategy is ___'

Extensions (Advanced Learners):
  • Research the history of universal influenza vaccine attempts — what strategies have been tried, what failed, and what current candidates show the most promise?
  • Investigate how computational protein design (like RosettaDesign) is being used to create 'designer antigens' — artificial protein structures that present conserved epitopes in highly immunogenic conformations
  • Compare the immune evasion strategies of influenza (antigenic drift/shift), HIV (extreme variability, latency), and measles (antigenic stability) — what determines whether a virus can escape vaccine-induced immunity?

Cross-Curricular Connections:
  • Math: Calculate the probability that a virus with mutation rate M will generate an escape variant within T months, given N circulating viruses — model this as a Poisson process and determine the expected time to vaccine failure
  • ELA: Write a public health communication explaining why a universal flu vaccine would be one of the most important medical advances of the century — using data from your model to quantify the impact on global health
  • Social Studies/Ethics: Analyze the ethical frameworks for vaccine distribution during a pandemic — utilitarian (maximize lives saved), egalitarian (equal access), prioritarian (prioritize the vulnerable) — and how Population Coverage optimization relates to each framework

CAST ALIGNMENT:
• Model the immune response cascade from vaccine antigen presentation through immune cell activation to antibody production, memory formation, and duration of protection
• Analyze the specificity-breadth trade-off in antigen selection and its implications for protection against evolving pathogens
• Evaluate vaccine design strategies for maximizing population coverage across genetically diverse human populations facing rapidly-mutating pathogens

CAST-Style Assessment Questions:
• Multiple Choice: A new SARS-CoV-2 variant emerges with 15 mutations in the spike protein receptor-binding domain. Based on your model, which vaccine design strategy would maintain the most protection against this variant?
• Constructed Response: Using your immune response model, explain why a vaccine that produces very high antibody levels against one influenza strain might fail to protect against a new strain that emerges 6 months later. Reference at least three model components including Pathogen Mutation Rate, Cross-Reactivity, and Antigen Selection in your answer.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: Vaccine Design Optimization
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. How do you think a vaccine 'teaches' your immune system to fight a disease it has never encountered?

   _________________________________________________________

   _________________________________________________________

2. Why do you think you need a new flu vaccine every year but only one measles vaccine for life?

   _________________________________________________________

   _________________________________________________________

3. Draw a diagram showing how you think the immune system responds when it encounters a pathogen for the first time versus the second time.

   [DRAWING BOX]

4. What challenges do you think scientists face when designing vaccines against rapidly-mutating viruses like influenza or COVID-19?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Antigen                       
___ Adjuvant                      
___ Immunological Memory          
___ Antigenic Drift               

A. A molecular structure (protein, glycoprotein, or polysaccharide) from a pathogen that the immune system recognizes as foreign — vaccine antigens are carefully selected pieces of the pathogen that trigger a protective immune response without causing disease
B. A substance added to a vaccine to enhance the immune response to the antigen — adjuvants activate innate immune cells, increase antigen presentation, and promote stronger adaptive immunity, allowing lower antigen doses to achieve protective immunity
C. The ability of the adaptive immune system to 'remember' a pathogen it has previously encountered — mediated by long-lived memory B cells and memory T cells that mount a faster, stronger response upon re-exposure, providing lasting protection
D. The gradual accumulation of mutations in pathogen surface proteins (especially in RNA viruses like influenza and SARS-CoV-2) that allows the pathogen to partially evade existing immune responses — the primary reason seasonal flu vaccines must be redesigned annually

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

SCENARIO: Strain-Specific
Settings: Dominant strain antigen, moderate adjuvant
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Broadly Protective
Settings: Conserved region antigen, strong adjuvant
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: High-Mutation Challenge
Settings: Fast-mutating pathogen, any vaccine design
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

1. How does your model demonstrate the fundamental trade-off between vaccine specificity and cross-reactivity breadth?

   _________________________________________________________

   _________________________________________________________

2. Why is Pathogen Mutation Rate the most challenging component for long-term vaccine design — and how does Antigen Selection strategy affect vulnerability to antigenic drift?

   _________________________________________________________

   _________________________________________________________

3. What did the model reveal about the relationship between Adjuvant Strength and real-world Population Coverage — why doesn't 'stronger adjuvant' always mean 'better vaccine'?

   _________________________________________________________

   _________________________________________________________

4. How would adding Immune Imprinting Effect change your model's predictions about booster vaccine effectiveness?

   _________________________________________________________

   _________________________________________________________

5. What ethical considerations arise when optimizing vaccine design for population-level protection versus individual-level protection?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. COVID-19 vaccines were developed in under a year — a process that usually takes 10-15 years. How do computational models of the immune system make it possible to design vaccines faster, and can we design a universal vaccine that works against a virus that keeps mutating? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Developing and Using Models / Constructing Explanations
   □ Disciplinary Core Idea: LS1.A Structure and Function / LS4.C Adaptation
   □ Crosscutting Concept: Cause and Effect / Structure and Function

3. What ethical considerations arise when optimizing vaccine design for population-level protection versus individual-level protection?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Universal Influenza Vaccine Strategy
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design a vaccine strategy that provides broad, long-lasting protection against influenza — eliminating the need for annual reformulation by targeting conserved viral elements.

SCENARIO: The WHO has launched a $1 billion initiative to develop a universal influenza vaccine — one that works against all flu strains and doesn't need to be redesigned every year. Current seasonal flu vaccines are only 20-60% effective because they target rapidly-mutating surface proteins (hemagglutinin head). Your immunology team must design a vaccine strategy that targets conserved viral elements to provide durable, broadly protective immunity.

GUIDING QUESTIONS:
• Which conserved influenza proteins or protein regions would you target, and what is the trade-off between conservation and immunogenicity?
• What adjuvant and delivery platform (mRNA, protein subunit, viral vector, nanoparticle) would you use, and why?
• How would you test whether your vaccine provides Cross-Reactivity against historically diverse influenza strains?

DESIGN THINKING:
• Would you use a single antigen or a cocktail of multiple conserved antigens — and how does this affect manufacturing complexity?

  _________________________________________________________

• How would you design clinical trials to demonstrate broad protection against strains that haven't emerged yet?

  _________________________________________________________

• What booster schedule would maximize Duration of Immunity while remaining practical for population-wide implementation?

  _________________________________________________________

• How would you address immune imprinting (original antigenic sin) — the tendency of the immune system to preferentially recall responses to the first flu strain encountered, even when vaccinated against new strains?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Strategy includes justified conserved antigen selection with evolutionary analysis, platform rationale, multi-antigen design consideration, clinical trial plan for broad protection, and population coverage analysis supported by model predictions
• Proficient (3): Strategy includes antigen selection targeting conserved regions with reasoning connected to model trade-offs and basic clinical validation approach
• Developing (2): Strategy identifies conserved targets but lacks detail on platform selection, breadth validation, or population coverage considerations
• Beginning (1): Strategy is incomplete or does not connect antigen selection to the immune response model's specificity-breadth trade-off

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CAST-Aligned Pre/Post Assessment

### Administration Instructions

These 5 multiple-choice questions are administered identically as both a pre-assessment (before Activity 1) and a post-assessment (after Activity 4). Score each out of 5. Learning growth = post-score minus pre-score.

Questions follow the California Science Test (CAST) stimulus-response format. Each item is three-dimensional, assessing a Science and Engineering Practice (SEP), Disciplinary Core Idea (DCI), and Crosscutting Concept (CCC) simultaneously, aligned to HS-LS1-4, HS-LS4-2.

---

### Question 1

CAST Alignment: SEP 2.1.1 (Determine components of a system) + DCI LS1.4 + CCC4 (Systems and System Models)

A student is using the ModelIt platform to study the system in this lesson. The model includes these components: Antigen Selection, Adjuvant Strength, Immune Cell Activation, Antibody Production Rate, Memory Cell Formation, Pathogen Mutation Rate, Cross-Reactivity, Duration of Immunity, Population Coverage. Some components are external (Antigen Selection, Adjuvant Strength, Pathogen Mutation Rate) and some are internal (Immune Cell Activation, Antibody Production Rate, Memory Cell Formation, Cross-Reactivity, Duration of Immunity, Population Coverage). The student needs to understand what each component represents and how they are organized.

A student's vaccine model shows that a strain-specific vaccine targeting the dominant viral variant produces high Antibody Production Rate initially, but Duration of Immunity drops to near zero after 12 months as the virus undergoes antigenic drift. Which design modification would MOST effectively extend Duration of Immunity?

A. Increasing Adjuvant Strength to maximum to produce more antibodies against the same strain
B. Switching Antigen Selection to target a conserved region that is shared across variants, accepting lower peak antibody levels in exchange for broader Cross-Reactivity that remains effective as the virus mutates
C. Administering the same strain-specific vaccine more frequently
D. Removing the adjuvant to reduce immune overstimulation

Correct Answer: B

Feedback: Correct. The root cause of declining immunity is antigenic drift changing the target. More antibodies against an outdated target do not solve this. Targeting a conserved region trades peak antibody levels for durability, because the conserved target changes slowly even as the rest of the virus mutates. If you chose A, this answer suggests something is being added to the system. Look carefully at the model — the total amount stays the same even when components change. The system is conserving matter or energy. If you chose C, this answer suggests something is being added to the system. Look carefully at the model — the total amount stays the same even when components change. The system is conserving matter or energy. If you chose D, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows.

---

### Question 2

CAST Alignment: SEP 2.1.2 (Determine relationships among components) + DCI LS1.4 + CCC1 (Patterns)

In the computational model for this lesson, a student draws arrows between components to show relationships. The model shows that when Antigen Selection increases, Immune Cell Activation increases; when Adjuvant Strength increases, Immune Cell Activation increases. The student is trying to understand why these relationships are positive or negative.

In the model, increasing Adjuvant Strength from 0 to moderate produces a large increase in Immune Cell Activation and Antibody Production Rate. Increasing from moderate to maximum produces only a small additional increase in protection but a large increase in side effects. This pattern is BEST described as:

A. A linear dose-response relationship
B. Diminishing returns, where each additional unit of adjuvant produces progressively less additional benefit while side effects continue to increase proportionally, defining an optimal adjuvant level that maximizes the benefit-to-risk ratio
C. Evidence that adjuvants are unnecessary
D. A measurement error in the model

Correct Answer: B

Feedback: Correct. Adjuvant dose-response follows a law of diminishing returns. The immune system has a finite capacity for activation, so beyond the saturation point, additional adjuvant stimulates marginal additional protection while continuing to increase inflammatory side effects. The optimal dose maximizes the ratio of benefit to adverse reactions. If you chose A, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose C, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows.

---

### Question 3

CAST Alignment: SEP 2.1.3 (Evaluate a model's accuracy) + DCI LS1.4 + CCC4 (Systems and System Models)

A student runs a simulation of the model. The model shows that when Antigen Selection increases, Immune Cell Activation increases and when Adjuvant Strength increases, Immune Cell Activation increases and when Immune Cell Activation increases, Antibody Production Rate increases. The student changes one variable to see how the whole system responds.

A model simulation shows that two vaccines with identical Antibody Production Rates produce very different long-term outcomes: Vaccine A provides protection for 6 months while Vaccine B provides protection for 10 years. Which component MOST LIKELY differs between them?

A. Memory Cell Formation, where Vaccine B stimulates more robust differentiation of long-lived memory B cells and T cells that persist and rapidly reactivate upon pathogen re-exposure
B. The number of total antibodies produced during the initial response
C. The size of the injection needle used for administration
D. The color of the vaccine formulation

Correct Answer: A

Feedback: Correct. Antibody levels wane over months as short-lived plasma cells die. Long-term protection depends on memory cells, which persist for years or decades. Vaccine B likely triggers more effective memory cell differentiation, enabling rapid recall responses that re-establish protective antibody levels upon future pathogen encounter. If you chose B, look at the evidence from the model. The correct answer (A) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose C, look at the evidence from the model. The correct answer (A) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, look at the evidence from the model. The correct answer (A) is supported by the relationships between components. This answer does not match what the simulation data shows.

---

### Question 4

CAST Alignment: SEP 2.1.4 (Represent mechanisms to explain/predict events) + DCI LS1.4 + CCC4 (Systems and System Models)

Scientists are studying data related to this system. They collected observations over time and noticed patterns in how the components change. The data shows how changes in one part of the system cascade through the other parts.

A vaccine designer uses the model to evaluate Population Coverage across a genetically diverse population. The model shows that the vaccine protects 95% of individuals with one HLA type but only 40% of individuals with a different HLA type. What does this reveal about vaccine design?

A. The vaccine is defective and should not be used
B. Human genetic diversity in immune response genes (HLA) means the same antigen is presented differently to immune cells in different individuals, making it impossible to achieve equal protection across all genetic backgrounds with a single antigen design
C. HLA type has no effect on vaccine efficacy
D. Population coverage cannot be measured using computational models

Correct Answer: B

Feedback: Correct. HLA molecules determine which peptide fragments of the antigen are presented to T cells. Different HLA types present different fragments, meaning the same vaccine antigen triggers different immune responses in different people. This genetic diversity is a fundamental challenge for universal vaccine design and often requires multi-epitope vaccines. If you chose A, the model shows these components ARE connected. When one changes, it affects the others through the relationships (positive or negative) that you mapped in the model. If you chose C, the model shows these components ARE connected. When one changes, it affects the others through the relationships (positive or negative) that you mapped in the model. If you chose D, the model shows these components ARE connected. When one changes, it affects the others through the relationships (positive or negative) that you mapped in the model.

---

### Question 5

CAST Alignment: SEP 2.1.5 (Apply a model to make predictions) + DCI LS1.4 + CCC4 (Systems and System Models)

A team wants to use the model to solve a real-world problem related to this system. They know they cannot control the external components (Antigen Selection, Adjuvant Strength, Pathogen Mutation Rate), but they can take action on internal components (Immune Cell Activation, Antibody Production Rate, Memory Cell Formation, Cross-Reactivity, Duration of Immunity, Population Coverage). They need to decide which action would be most effective based on what the model shows.

A student runs two simulations with identical vaccine designs but different Pathogen Mutation Rates. At low mutation rate, Cross-Reactivity maintains protection for 15 years. At high mutation rate, protection degrades after 2 years. Based on this analysis, which vaccine development strategy is MOST appropriate for a rapidly mutating pathogen?

A. Design one perfect vaccine and administer it once
B. A platform technology (like mRNA) that can be rapidly updated to match new variants, combined with targeting of the most conserved epitopes to extend the effective period between updates
C. Abandon vaccination entirely for rapidly mutating pathogens
D. Increase the dose of the original vaccine to compensate for mutations

Correct Answer: B

Feedback: Correct. For rapidly mutating pathogens, the strategy must combine two approaches: (1) target conserved regions to maximize the interval before updates are needed, and (2) use a platform technology that enables rapid redesign when updates become necessary. This is exactly the strategy used for COVID-19 variant-updated mRNA boosters. If you chose A, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose C, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, this answer suggests something is being added to the system. Look carefully at the model — the total amount stays the same even when components change. The system is conserving matter or energy.

---

### Answer Key

Question 1: B (Cognitive Level: Identify — SEP 2.1.1, DCI LS1.4, CCC4)
Question 2: B (Cognitive Level: Reason — SEP 2.1.2, DCI LS1.4, CCC1)
Question 3: A (Cognitive Level: Reason — SEP 2.1.3, DCI LS1.4, CCC4)
Question 4: B (Cognitive Level: Reason + Evidence — SEP 2.1.4, DCI LS1.4, CCC4)
Question 5: B (Cognitive Level: Predict + Apply — SEP 2.1.5, DCI LS1.4, CCC4)


## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-09/G09L3-L09/G09L3-L09-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-09/G09L3-L09/G09L3-L09-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-09/G09L3-L09/G09L3-L09-Student-Presentation.pptx] |
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