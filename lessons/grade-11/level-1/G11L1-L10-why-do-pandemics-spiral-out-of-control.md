# Lesson: Why Do Pandemics Spiral Out of Control?

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G11L1-L10 |
| **Grade** | 11th Grade — Level 1: Foundations of Complex Systems |
| **Lesson Name** | Why Do Pandemics Spiral Out of Control? |
| **Status** | Template |

---

## Platform

### Title
**Why Do Pandemics Spiral Out of Control? — Modeling Infectious Disease Transmission and Public Health Interventions**

### Overview
Pandemics have shaped human history more than wars, and they follow mathematical laws as precise as any in physics. The SIR (Susceptible-Infected-Recovered) model, developed in the 1920s, remains the foundation of epidemiological modeling because it captures the essential dynamics: a susceptible population that shrinks as people are infected, an infectious population that grows and then declines, and a recovered population that provides immunity. Understanding these dynamics isn't just academic — it's the science that determines whether millions live or die. Students investigate the driving question: Why do some outbreaks burn out on their own while others explode into global pandemics — and what determines whether we can stop them? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of a global pandemic visualization — a world map with glowing red dots spreading outward from a point of origin, network connection lines showing transmission paths between cities, dramatic dark background with data visualization overlays, editorial quality]

### Grade
11th Grade — Level 1: Foundations of Complex Systems

### NGSS Standard
**HS-LS2-2, HS-LS4-6**: Use mathematical representations to support and revise explanations based on evidence about factors affecting biodiversity and populations in ecosystems of different scales. Create or revise a simulation to test a solution to mitigate adverse impacts of human activity on biodiversity.

### Learning Objectives
- Model how the basic reproduction number (R0), transmission rate, and population susceptibility interact to determine whether an outbreak grows or dies
- Analyze the feedback loops between infection spread, herd immunity buildup, and public health interventions
- Predict the impact of different intervention strategies (vaccination, quarantine, social distancing) on epidemic curves
- Evaluate why the timing of public health interventions is the single most critical factor in pandemic control

### Component List (Starting Model: 6 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| R0 Value | External | The baseline reproductive number of the pathogen, determined by its biology — airborne pathogens like measles (R0=15) spread far more easily than contact-transmitted pathogens like Ebola (R0=2) |
| Vaccination Rate | External | The percentage of the population vaccinated before or during the outbreak — vaccines reduce the susceptible population, lowering the effective reproduction number below the epidemic threshold |
| Susceptible Population | Internal | The fraction of the total population that can still be infected — decreases as people are vaccinated, recover with immunity, or (in the model) are removed from the susceptible pool |
| Infection Rate | Internal | The number of new infections per day, driven by the product of R0, the transmission rate, and the fraction of the population still susceptible — this is the engine of exponential growth |
| Recovery Rate | Internal | The rate at which infected individuals recover and develop immunity — faster recovery means shorter infectious periods, reducing the window for transmission to others |
| Effective R (Re) | Internal | The actual reproduction number at any point during the epidemic, adjusted for immunity and interventions — Re = R0 * (susceptible fraction) * (1 - intervention effectiveness). When Re drops below 1, the epidemic declines |

### Research for Lesson
- The SIR Model Framework — reference materials and textbook resources
- Exponential Growth and the Doubling Time — reference materials and textbook resources
- Herd Immunity: Natural vs. Vaccination — reference materials and textbook resources
- Why Timing Is Everything — reference materials and textbook resources

---

## Step 1: LOCATE — Build Your System

### Text Editor

```
WHY DO PANDEMICS SPIRAL OUT OF CONTROL?

Modeling Infectious Disease Transmission and Public Health Interventions.
Why do some outbreaks burn out on their own while others explode into global pandemics — and what determines whether we can stop them?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "R0 Value" — the baseline reproductive number of the pathogen
  ○ Click "Vaccination Rate" — the percentage of the population vaccinated before or during the outbreak — vaccines reduce the susceptible population
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Susceptible Population" — the fraction of the total population that can still be infected — decreases as people are vaccinated
  ○ Click "Infection Rate" — the number of new infections per day
  ○ Click "Recovery Rate" — the rate at which infected individuals recover and develop immunity — faster recovery means shorter infectious periods
  ○ Click "Effective R (Re)" — the actual reproduction number at any point during the epidemic

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
"Why do some outbreaks burn out on their own while others explode into global pandemics — and what determines whether we can stop them?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'R0 Value' — that's external. The baseline reproductive number of the pathogen.
Click on 'Vaccination Rate' — that's external. The percentage of the population vaccinated before or during the outbreak — vaccines reduce the susceptible population.
Click on 'Susceptible Population' — that's internal. The fraction of the total population that can still be infected — decreases as people are vaccinated.
Click on 'Infection Rate' — that's internal. The number of new infections per day.
Click on 'Recovery Rate' — that's internal. The rate at which infected individuals recover and develop immunity — faster recovery means shorter infectious periods.
Click on 'Effective R (Re)' — that's internal. The actual reproduction number at any point during the epidemic, adjusted for immunity and interventions — Re = R0 * (susceptible fraction) * (1 - intervention effectiveness).

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

R0 Value and Vaccination Rate are external components because R0 is determined by the pathogen's biology (how it transmits, infectious period) and cannot be changed, while Vaccination Rate is a policy decision made by public health authorities. Susceptible Population, Infection Rate, Recovery Rate, and Effective R are internal components because they are determined by the dynamics of the SIR model — Susceptible Population shrinks as infections occur, Infection Rate depends on the product of Re and susceptible fraction, Recovery Rate is a biological constant, and Effective R emerges from the interaction of R0 with current immunity levels.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next step, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 6 components sorted: R0 Value, Vaccination Rate (External), Susceptible Population, Infection Rate, Recovery Rate, Effective R (Re) (Internal)]

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
• Click on "R0 Value" and drag an arrow to "Infection Rate"
• Click on "Vaccination Rate" and drag an arrow to "Susceptible Population"
• Click on "Susceptible Population" and drag an arrow to "Effective R"
• Click on "Infection Rate" and drag an arrow to "Susceptible Population"

Task C: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ R0 Value → Infection Rate = POSITIVE (+)
    Higher R0 means each infected person transmits to more others, directly increasing the rate of new infections. A pathogen with R0=3 produces 3x more new infections per generation than one with R0=1.

  ○ Vaccination Rate → Susceptible Population = NEGATIVE (−)
    Higher vaccination rates directly reduce the susceptible population — each vaccinated person is removed from the pool of potential hosts. At 60% vaccination, only 40% of the population remains susceptible.

  ○ Susceptible Population → Effective R = POSITIVE (+)
    Re = R0 * (fraction susceptible). As the susceptible population shrinks (through vaccination or natural infection), the effective reproduction number drops proportionally. When Re falls below 1, the epidemic declines.

  ○ Infection Rate → Susceptible Population = NEGATIVE (−)
    Each new infection removes one person from the susceptible pool. Higher infection rates accelerate the depletion of susceptible individuals, which eventually reduces Re below 1 — this is the negative feedback loop that ends all epidemics.

Task D: CHECK YOUR MODEL
• You should have 4 arrows total
• 2 negative relationship(s), 2 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: At the start of an epidemic, nearly everyone is susceptible, so Re equals R0 and infections grow exponentially. But each infection removes one person from the susceptible pool. As the susceptible population shrinks, Re falls. Where is the tipping point — and can interventions push Re below 1 before the hospital system is overwhelmed?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'R0 Value' and drag an arrow
over to 'Infection Rate.'

Here's the key question: When r0 value goes UP, does
infection rate go UP or DOWN?

Higher R0 means each infected person transmits to more others, directly increasing the rate of new infections. A pathogen with R0=3 produces 3x more new infections per generation than one with R0=1.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Vaccination Rate' and drag an arrow
over to 'Susceptible Population.'

Here's the key question: When vaccination rate goes UP, does
susceptible population go UP or DOWN?

Higher vaccination rates directly reduce the susceptible population — each vaccinated person is removed from the pool of potential hosts. At 60% vaccination, only 40% of the population remains susceptible.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Last connection: Click on 'Susceptible Population' and drag an arrow
over to 'Effective R.'

Here's the key question: When susceptible population goes UP, does
effective r go UP or DOWN?

Re = R0 * (fraction susceptible). As the susceptible population shrinks (through vaccination or natural infection), the effective reproduction number drops proportionally. When Re falls below 1, the epidemic declines.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Final connection: Click on 'Infection Rate' and drag an arrow
over to 'Susceptible Population.'

Here's the key question: When infection rate goes UP, does
susceptible population go UP or DOWN?

Each new infection removes one person from the susceptible pool. Higher infection rates accelerate the depletion of susceptible individuals, which eventually reduces Re below 1 — this is the negative feedback loop that ends all epidemics.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Look at your model now. You've got 2 negative and 2
positive relationships. 4 arrows total.

At the start of an epidemic, nearly everyone is susceptible, so Re equals R0 and infections grow exponentially. But each infection removes one person from the susceptible pool. As the susceptible population shrinks, Re falls. Where is the tipping point — and can interventions push Re below 1 before the hospital system is overwhelmed?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: R0 Value +→ Infection Rate, Vaccination Rate −→ Susceptible Population, Susceptible Population +→ Effective R, Infection Rate −→ Susceptible Population]

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
• When R0 Value is HIGH, what happens to the internal components?

Task C: SCENARIO — UNCONTROLLED OUTBREAK
• R0: 2.5 | Vaccination: 0% | Interventions: None
• PREDICT FIRST: What shape do you predict the epidemic curve will take? Will infections grow linearly or exponentially — and when do you predict the peak will occur?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task D: SCENARIO — VACCINATION SHIELD
• R0: 2.5 | Vaccination: 60% | Interventions: None
• PREDICT FIRST: If 60% of the population is vaccinated before the outbreak, do you predict the epidemic will still grow? What happens to Re when you remove 60% of the susceptible population?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task E: SCENARIO — TIMING IS EVERYTHING
• R0: 2.5 | Social distancing at Day 10 vs. Day 30
• PREDICT FIRST: Do you predict a 20-day delay in implementing social distancing will significantly change the total number of infections? By how much?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Epidemics grow exponentially, not linearly — each infected person infects R0 others, who each infect R0 more, creating a doubling cascade that makes early stages deceptively quiet before infections explode
• The herd immunity threshold (1 - 1/R0) determines the minimum vaccination coverage needed to prevent outbreaks — for R0=2.5, this is 60%, for R0=15 (measles), it's 93%
• Intervention timing is the most critical variable — the same intervention implemented 20 days earlier can reduce total infections by 50-80% because exponential growth means every day of delay allows the infected population to double
• All outbreaks eventually end because the susceptible population shrinks — the question is whether they end through controlled vaccination (few deaths) or uncontrolled infection (mass death and overwhelmed hospitals)

THE ANSWER: Pandemics spiral out of control because of exponential growth — a process that is counterintuitively quiet at first and catastrophic by the time it's obvious. When R0 is above 1, each infected person creates more than one new infection, and those new infections each create more. In a population where everyone is susceptible, a pathogen with R0=2.5 will infect 60% of the population before herd immunity naturally stops it. The difference between a manageable outbreak and a civilizational crisis comes down to timing: early interventions (vaccination, social distancing, quarantine) reduce the effective R below 1 while most people are still uninfected. Wait too long, and the exponential curve has already generated millions of cases. This is why epidemiologists say 'if it looks like you overreacted, you did it right' — successful early intervention makes the crisis look like it was never a crisis at all.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Uncontrolled Outbreak. R0: 2.5 | Vaccination: 0% | Interventions: None.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Vaccination Shield.
R0: 2.5 | Vaccination: 60% | Interventions: None.

Before you run it — make a prediction. If 60% of the population is vaccinated before the outbreak, do you predict the epidemic will still grow? What happens to Re when you remove 60% of the susceptible population?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Timing Is Everything. R0: 2.5 | Social distancing at Day 10 vs. Day 30.
Do you predict a 20-day delay in implementing social distancing will significantly change the total number of infections? By how much?

Here's what our model reveals: Pandemics spiral out of control because of exponential growth — a process that is counterintuitively quiet at first and catastrophic by the time it's obvious. When R0 is above 1, each infected person creates more than one new infection, and those new infections each create more. In a population where everyone is susceptible, a pathogen with R0=2.5 will infect 60% of the population before herd immunity naturally stops it. The difference between a manageable outbreak and a civilizational crisis comes down to timing: early interventions (vaccination, social distancing, quarantine) reduce the effective R below 1 while most people are still uninfected. Wait too long, and the exponential curve has already generated millions of cases. This is why epidemiologists say 'if it looks like you overreacted, you did it right' — successful early intervention makes the crisis look like it was never a crisis at all.

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
   • What happens if you turn OFF R0 Value?
   • What happens if you turn OFF Vaccination Rate?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Superspreader Events — Occasions where a single infected person transmits to an unusually large number of others — research shows 10-20% of infected people cause 80% of transmission, making disease spread far more uneven than R0 alone suggests
   • Hospital Capacity — The number of ICU beds, ventilators, and healthcare workers available — when infection rate exceeds hospital capacity, mortality spikes because treatable patients cannot receive care, creating a catastrophic amplification of the death toll
   • Behavioral Compliance — The percentage of the population that actually follows recommended interventions like social distancing and mask-wearing — compliance typically starts high during peak fear and declines over time, creating waves of re-emergence as Re fluctuates above and below 1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • The SIR Model Framework — how does this connect to your model?
   • Exponential Growth and the Doubling Time — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • Why does exponential growth make early-stage pandemics so deceptively dangerous — and why do people consistently underestimate the threat until it's too late?
   • How does the herd immunity threshold equation (1 - 1/R0) explain why measles outbreaks occur even in highly vaccinated populations?
   • Why do epidemiologists say 'if it looks like you overreacted, you probably did it right' — what does this reveal about the paradox of successful early intervention?
   • How could your model be extended to account for superspreader events, which make disease spread far more uneven than a simple R0 value suggests?

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

Superspreader Events. Occasions where a single infected person transmits to an unusually large number of others — research shows 10-20% of infected people cause 80% of transmission, making disease spread far more uneven than R0 alone suggests
How would you model that?

Hospital Capacity. The number of ICU beds, ventilators, and healthcare workers available — when infection rate exceeds hospital capacity, mortality spikes because treatable patients cannot receive care, creating a catastrophic amplification of the death toll
How would you model that?

Behavioral Compliance. The percentage of the population that actually follows recommended interventions like social distancing and mask-wearing — compliance typically starts high during peak fear and declines over time, creating waves of re-emergence as Re fluctuates above and below 1
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

Epidemiologists study disease patterns and design public health interventions, working at the CDC, WHO, state health departments, and pharmaceutical companies, earning $75,000-$140,000/year. Mathematical Modelers who build computational disease transmission models earn $80,000-$160,000/year and are among the most in-demand scientists during outbreaks. Public Health Emergency Managers coordinate pandemic response logistics and resource allocation, earning $70,000-$130,000/year.

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
Visual: Title slide with pandemic spread visualization
Say: "In January 2020, there were 282 confirmed COVID cases worldwide. By January 2021, there were 100 million. How does a number that small become a number that large?"
Do: Show the COVID case count graph from January 2020 to peak. Point out the deceptive quiet of the early weeks. Ask: At what point would YOU have started worrying?
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and vocabulary terms
Say: "Today we're modeling the mathematics of contagion — the same equations that epidemiologists use to predict, and try to prevent, the next pandemic."
Do: Have students read objectives. Pre-teach R0 with the rice-on-a-chessboard analogy: if each grain doubles, how many squares until the board overflows? (Answer: 64 squares, final square has 9.2 quintillion grains.)
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: Two outbreaks: one contained, one global — what's different?
Say: "SARS in 2003: 8,098 cases, contained. COVID in 2020: 700 million cases, global pandemic. Both respiratory viruses. Both from China. What was different?"
Do: Quick-write: What factors do you think determine whether an outbreak stays small or goes global? Share out and list responses.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps overview
Say: "We're building the same model the CDC and WHO use to predict outbreaks. It's called the SIR model, and it's surprisingly simple — just three boxes and two arrows."
Do: Draw S → I → R on the board. Explain: people flow from Susceptible to Infected to Recovered. The speed of the first arrow is the whole game.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Component cards for epidemic model
Say: "We can choose how contagious the pathogen is and how many people are vaccinated. Everything else — infection rate, how fast it spreads, when it peaks — follows from those choices."
Do: Guide sorting: R0 Value and Vaccination Rate are external (biology and policy). Susceptible Population, Infection Rate, Recovery Rate, and Effective R are internal (model dynamics).
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows between SIR components
Say: "Here's the key insight: R0 starts as a constant, but the EFFECTIVE R changes every day because every new infection removes one person from the susceptible pool. The epidemic is fighting against its own success."
Do: Students map the feedback loop: higher infection → lower susceptible population → lower effective R → eventually Re < 1 → epidemic declines. This is the negative feedback loop that ends all epidemics.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Epidemic curve simulations under different conditions
Say: "Let's run three worlds: no intervention, 60% vaccination, and early vs. late social distancing. Watch the epidemic curves — the differences will shock you."
Do: Students predict peak infection day and total infections for each scenario. Run simulations. The timing comparison (Day 10 vs. Day 30 intervention) should produce the most dramatic difference.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key findings — intervention timing comparison
Say: "Twenty days. That's all it takes. The same intervention, implemented 20 days earlier, can cut total infections by 80%. In a pandemic, procrastination kills."
Do: Show the side-by-side epidemic curves for early vs. late intervention. Calculate: at a 4-day doubling time, 20 days = 5 doublings = 32x more infections. The math is the argument.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Pandemic response plan design
Say: "A new virus just showed up. R0 is 3.0. Cases are doubling every 4 days. No vaccine for 6 months. You're in charge. Design the response plan that saves the most lives while spending the least money."
Do: Groups design phased response plans with intervention triggers, resource allocation, and communication strategies. Must justify timing decisions with model evidence. Present and defend plans.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: Why Do Pandemics Spiral Out of Control?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
Pandemics have shaped human history more than wars, and they follow mathematical laws as precise as any in physics. The SIR (Susceptible-Infected-Recovered) model, developed in the 1920s, remains the foundation of epidemiological modeling because it captures the essential dynamics: a susceptible population that shrinks as people are infected, an infectious population that grows and then declines, and a recovered population that provides immunity. Understanding these dynamics isn't just academic — it's the science that determines whether millions live or die.

NGSS ALIGNMENT:
HS-LS2-2, HS-LS4-6: Use mathematical representations to support and revise explanations based on evidence about factors affecting biodiversity and populations in ecosystems of different scales. Create or revise a simulation to test a solution to mitigate adverse impacts of human activity on biodiversity.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Using Mathematics and Computational Thinking
  Students use the SIR (Susceptible-Infected-Recovered) model framework and R0 calculations to predict epidemic dynamics, evaluate intervention timing, and compare outbreak scenarios mathematically.
• Disciplinary Core Idea: LS2.A Interdependent Relationships in Ecosystems / LS4.D Biodiversity and Humans
  Disease transmission follows mathematical patterns governed by pathogen-host interactions. Human activities (population density, travel, intervention policies) fundamentally alter these dynamics.
• Crosscutting Concept: Cause and Effect
  Students trace the causal chain from pathogen R0 through population susceptibility to epidemic outcome, identifying how interventions at specific points in the chain produce dramatically different results depending on timing.

PACING GUIDE:
• Step 1 (Locate): 8-10 minutes
• Step 2 (Establish): 8-10 minutes
• Step 3 (Visualize & Evaluate): 10-12 minutes
• Step 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: R0 (Basic Reproduction Number), Herd Immunity Threshold, Epidemic Curve, Transmission Rate
□ Prepare Why do some outbreaks burn out on their own while others explode into global pandemics — and what determines whether we can stop them discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify R0 value, vaccination rate, susceptible population, infection rate, recovery rate, and effective R as the key components of the epidemic transmission system.
• Establish: Students determine that R0 and vaccination rate are external inputs (pathogen biology and policy decisions), while susceptible population, infection rate, recovery rate, and effective R are internal dynamics governed by the SIR model equations.
• Visualize: Students build a computational SIR model showing how infections flow from susceptible to infected to recovered, with the effective reproduction number declining as susceptible population shrinks.
• Evaluate: Students run uncontrolled, vaccinated, and early vs. late intervention scenarios to observe how exponential growth, herd immunity, and intervention timing shape epidemic curves.
• Revise: Students add superspreader events, hospital capacity, or behavioral compliance to explore how real-world heterogeneity and human behavior modify the idealized SIR predictions.

BACKGROUND CONTENT:
• The SIR Model Framework:
  The SIR model divides a population into three compartments: Susceptible (S) — those who can be infected, Infected (I) — those who are currently infectious, and Recovered (R) — those who have cleared the infection and are immune. The flow between compartments follows differential equations: dS/dt = -beta*S*I, dI/dt = beta*S*I - gamma*I, dR/dt = gamma*I, where beta is the transmission rate and gamma is the recovery rate. R0 = beta/gamma represents the basic reproduction number. When S is large (early epidemic), Re is close to R0 and infections grow exponentially. As S shrinks (people recover), Re falls until Re < 1 and the epidemic declines.

• Exponential Growth and the Doubling Time:
  In the early phase of an epidemic, when nearly everyone is susceptible, infections grow exponentially: I(t) = I_0 * e^(kt), where k depends on R0 and the generation time. For COVID-19 (R0~2.5, generation time ~5 days), the doubling time was approximately 3-4 days in uncontrolled settings. This means 10 cases become 20, then 40, 80, 160, 320, 640, 1280 — from 10 to over 1,000 in just three weeks. The deceptive quiet of the early phase (only 10-100 cases) is precisely why pandemics catch populations by surprise.

• Herd Immunity: Natural vs. Vaccination:
  Herd immunity occurs when enough people are immune that the effective reproduction number drops below 1. The threshold is 1 - 1/R0. For R0=2.5: threshold is 60%. For R0=15 (measles): threshold is 93%. Reaching this threshold through natural infection means 60-93% of the population must be infected — with all the associated hospitalization and death. Vaccination achieves the same mathematical result without the illness. This is why vaccination is the single most powerful tool in pandemic response: it reduces the susceptible population directly.

• Why Timing Is Everything:
  Mathematical modeling consistently shows that the same intervention implemented 2-3 weeks earlier can reduce total infections by 50-80%. The reason is exponential growth: during those 2-3 weeks, the infected population doubles multiple times. Early social distancing when there are 100 cases means controlling 100 infections; the same measures 3 weeks later means controlling 1,600 infections. This creates the 'paradox of prevention': successful early intervention makes the threat seem like it was never serious, leading critics to claim the response was an overreaction. In reality, the low case count IS the evidence that early intervention worked.

COMMON MISCONCEPTIONS:
• "Pandemics grow at a constant rate"
  Reality: Pandemics grow EXPONENTIALLY in the early phase, not linearly or at a constant rate. This means the rate of new infections increases every day — each generation of infections is larger than the last by a factor of R0. This is why an outbreak that seems manageable (100 cases) can become catastrophic (100,000 cases) in just a few weeks. Students often graph pandemic growth as a straight line because linear thinking is intuitive. The model shows the actual exponential curve, which curves sharply upward — a shape that is qualitatively different from linear growth.
  Strategy: Graph exercise: have students predict the number of infections after 10 generations starting from 10 cases with R0=2 (linear guess vs. exponential reality). Linear guess: 10+20=30 per generation → 210 total. Exponential reality: 10→20→40→80→160→320→640→1280→2560→5120 = 10,230. The exponential is 49x larger.

• "Herd immunity means NOBODY gets sick"
  Reality: Herd immunity doesn't prevent all infections — it prevents sustained CHAINS of transmission. When the susceptible population drops below the critical threshold (1-1/R0), each infected person transmits to fewer than one other person on average. Individual infections still occur, but they can't sustain an epidemic chain — they fizzle out. Think of it like a fire: herd immunity doesn't prevent sparks, it prevents the forest fire by removing enough fuel (susceptible people) that flames can't spread.
  Strategy: Analogy: remove 70% of the trees from a forest. A lightning strike can still ignite a tree, but the fire can't spread to the next tree because the gap is too wide. Individual trees still burn, but the forest fire is prevented.

• "You can wait to see how bad it gets before responding"
  Reality: This is the most dangerous misconception because it leads to the worst outcomes. Exponential growth means that by the time the threat is 'obvious' (thousands of cases, hospitals filling), the epidemic has been doubling for weeks and contains millions of infections in the pipeline. Waiting for visible evidence of severity guarantees a late response. The model shows this brutally: the same intervention at Day 10 (100 cases) vs. Day 30 (3,200 cases) results in 5-10x more total infections. In a pandemic, the evidence that justifies action is the mathematical model, not the case count you can see.
  Strategy: Show two graphs: City A responded at 50 cases (total epidemic: 2,000 cases). City B responded at 5,000 cases (total epidemic: 200,000 cases). Both used identical interventions. Ask: Did City A overreact? (No — City A's low total is PROOF the early response worked, not evidence that it was unnecessary.)

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
Big Question: Why do some outbreaks burn out on their own while others explode into global pandemics — and what determines whether we can stop them?
Answer: Pandemics spiral out of control because of exponential growth — a process that is counterintuitively quiet at first and catastrophic by the time it's obvious. When R0 is above 1, each infected person creates more than one new infection, and those new infections each create more. In a population where everyone is susceptible, a pathogen with R0=2.5 will infect 60% of the population before herd immunity naturally stops it. The difference between a manageable outbreak and a civilizational crisis comes down to timing: early interventions (vaccination, social distancing, quarantine) reduce the effective R below 1 while most people are still uninfected. Wait too long, and the exponential curve has already generated millions of cases. This is why epidemiologists say 'if it looks like you overreacted, you did it right' — successful early intervention makes the crisis look like it was never a crisis at all.

Simulation Answers:
• Uncontrolled Outbreak Scenario: With R0=2.5, no vaccination, and no interventions, the model shows classic exponential growth in the early phase, with infections doubling every 4-5 days. The epidemic curve rises steeply to a peak at approximately Day 45-55 when the susceptible population drops below the herd immunity threshold (60%). Total infections reach approximately 80-90% of the population because the epidemic overshoots the herd immunity threshold due to momentum — people already infected during the peak continue to transmit even after Re drops below 1. The curve is tall and narrow: a sharp spike that overwhelms hospitals.
• Delayed vs. Early Intervention Scenario: With identical pathogen parameters (R0=2.5), implementing social distancing (reducing Re by 40%) at Day 10 vs. Day 30 produces dramatically different outcomes. At Day 10, there are approximately 100 infections — the intervention catches the curve while it's still small, reducing Re below 1 and flattening the curve to a manageable peak. At Day 30, there are approximately 3,200 infections (5 doublings later) — the same intervention struggles to contain the much larger infected population. The Day 30 scenario results in 5-10x more total infections and a peak that exceeds hospital capacity. The model vividly demonstrates that in exponential growth, every day of delay costs exponentially more infections.

Reflection Exemplars:
• Q: Why do people consistently underestimate pandemics in the early stages?
  A: Human intuition is calibrated for linear growth, not exponential growth. When you see 100 cases doubling to 200, the increase of 100 feels small. But that same doubling rate means 100,000 becomes 200,000 — an increase of 100,000 cases in the same time period. Our brains process the absolute number (100 vs. 200 — no big deal) rather than the growth rate (doubling every 4 days — catastrophic). Additionally, early epidemic stages look identical to outbreaks that fizzle out on their own, making it genuinely difficult to distinguish a future pandemic from a false alarm until exponential growth becomes visible — at which point it's already too late for early intervention.
• Q: Why is 'if it looks like you overreacted, you did it right' a fundamental truth of pandemic response?
  A: Successful early intervention prevents the exponential growth that would have made the threat visible. If a city implements aggressive social distancing when there are 50 cases and the epidemic peaks at 500, critics will say 'it was only 500 cases — the response was an overreaction.' But the model shows that without intervention, those 50 cases would have become 500,000. The intervention didn't fail to prevent a crisis — it SUCCEEDED in preventing a crisis. The paradox is that the better the intervention works, the less evidence people see of the threat it prevented. This is why model-based evidence is essential: it shows the counterfactual scenario that would have occurred without action.

STEM CHALLENGE GUIDANCE:
Title: Design a Pandemic Response Plan
Mission: Design an evidence-based pandemic response plan for a novel respiratory pathogen, specifying intervention triggers, timing, and resource allocation to minimize both infections and economic disruption.
Scenario: A novel respiratory virus with R0=3.0 has been detected in a city of 2 million people. Initial cases are doubling every 4 days. No vaccine exists yet, but one could be available in 6 months. Your public health team must design a response plan that specifies when to implement social distancing, testing and contact tracing protocols, and resource allocation for hospitals — with the constraint that economic shutdown costs $500 million per month.
Introduction: Present the challenge: A novel respiratory virus (R0=3.0) has been detected with cases doubling every 4 days. No vaccine will be available for 6 months. Students must design a phased public health response that specifies intervention triggers, timing, and resource allocation. The constraint: economic shutdown costs $500 million per month, so the plan must balance health outcomes against economic impact using model evidence to justify every decision.

Key Concepts:
• The SIR Model in Practice: The SIR framework divides populations into Susceptible, Infected, and Recovered compartments. Real-world applications add complexity: SEIR models include an Exposed (latent) period, age-structured models account for different contact rates by age group, and spatial models track geographic spread. But the core insight remains: Re determines whether the epidemic grows or shrinks, and interventions aim to push Re below 1.
• Flatten the Curve: The 'flatten the curve' strategy doesn't necessarily reduce total infections — it spreads them over a longer time period so that the healthcare system is never overwhelmed. The peak determines whether hospitals can treat patients. A tall, narrow epidemic curve means hospitals overflow and treatable patients die. A flat, wide curve (same area = same total infections) keeps hospitalization rates below capacity, reducing mortality. Interventions that reduce Re don't just save infections — they save the healthcare system.
• Contact Tracing and Targeted Intervention: Rather than locking down entire populations, contact tracing identifies and isolates only the chain of transmission — infected individuals and their recent contacts. This targets intervention precisely where the virus is spreading, achieving epidemic control with minimal economic disruption. However, contact tracing only works when case numbers are low enough to track individually — another reason early intervention is critical.

Evaluation Rubric:
• Expert (4): Response plan specifies precise intervention triggers based on epidemiological indicators, demonstrates with model data that the timing prevents hospital overflow, balances economic cost against health outcomes with quantitative comparison, and includes a communication strategy addressing public perception
• Proficient (3): Response plan includes intervention timing and resource allocation with model evidence, and considers the trade-off between health and economic costs
• Developing (2): Response plan describes interventions but lacks specific triggers, timing justification, or model-based evidence for the strategy
• Beginning (1): Response plan is incomplete, proposes interventions without timing or evidence, or ignores the exponential growth dynamics that make timing critical

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a visual SIR diagram with arrows showing the flow from S → I → R, with labels explaining what drives each transition (transmission rate, recovery rate) and how Re decreases as S shrinks
  • Use the penny-doubling analogy: if you start with 1 penny and double it daily, you have $5.12 after 10 days but $5.2 million after 30 days — the same exponential curve that drives epidemic growth
  • Sentence frames: 'With R0 = __ and __% of the population susceptible, Re = __, which means each infected person creates __ new infections. At this rate, infections will double every __ days, reaching __ total cases by Day __.'

Extensions (Advanced Learners):
  • Research the difference between the 1918 influenza pandemic and COVID-19 in terms of R0, case fatality rate, and intervention effectiveness — how did a century of medical advances change the outcome?
  • Investigate how superspreader events (where one person infects dozens) deviate from the R0 average and model how targeting superspreader environments could be more effective than blanket social distancing
  • Design a COVID-19 variant scenario: if a new variant emerges with R0=5.0 (up from 2.5), recalculate the herd immunity threshold and evaluate whether current vaccination rates are sufficient

Cross-Curricular Connections:
  • Math: Calculate the herd immunity threshold for pathogens with R0 values of 1.5, 2.5, 4.0, 8.0, and 15.0 using the formula 1-1/R0. Graph the results. Then calculate how many days it takes for 10 cases to become 1 million at a 3-day doubling time. (Answer: about 50 days.) The math of exponential growth IS the math of pandemics.
  • ELA: Write a public health communication for teenagers explaining why social distancing measures are being implemented when there are 'only' 50 cases in the city. Your audience is skeptical and fatigued. Use model evidence to show what 50 cases becomes in 30 days without intervention — but communicate it in language that motivates action rather than causing panic.
  • History: Compare the public health responses to three pandemics: the 1918 Spanish Flu (limited intervention), 2003 SARS (aggressive early containment), and 2020 COVID-19 (varied response by country). How did intervention timing affect outcomes in each case? Which cities or countries responded earliest and how did their outcomes compare?

CAST ALIGNMENT:
• Model how R0, susceptible population, and interventions interact to determine epidemic trajectory
• Predict the impact of vaccination coverage on outbreak severity using the herd immunity threshold equation
• Evaluate how intervention timing affects total infections and peak healthcare demand

CAST-Style Assessment Questions:
• Multiple Choice: A new pathogen has R0 = 4.0. Using the herd immunity threshold formula (1 - 1/R0), what percentage of the population must be immune to prevent sustained transmission? A) 25%, B) 50%, C) 75%, D) 90%
• Constructed Response: Using your model, explain why a 20-day delay in implementing social distancing can result in 5-10 times more total infections than early implementation. Connect your answer to exponential growth, the effective reproduction number, and the time-dependent shrinking of the susceptible population.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: Why Do Pandemics Spiral Out of Control?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. What do you think determines whether a disease outbreak stays local or becomes a global pandemic?

   _________________________________________________________

   _________________________________________________________

2. What does 'exponential growth' mean, and can you give an example of how it applies to disease spread?

   _________________________________________________________

   _________________________________________________________

3. Why do you think public health officials sometimes recommend extreme measures (lockdowns, travel bans) when there are only a few cases?

   _________________________________________________________

   _________________________________________________________

4. What is herd immunity, and why do different diseases require different levels of vaccination coverage?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ R0 (Basic Reproduction Number)
___ Herd Immunity Threshold       
___ Epidemic Curve                
___ Transmission Rate             

A. The average number of new infections caused by a single infected person in a fully susceptible population — if R0 > 1, the outbreak grows exponentially; if R0 < 1, it dies out. COVID-19 had an R0 of 2-3, measles has an R0 of 12-18, making it one of the most contagious diseases known
B. The proportion of the population that must be immune (through vaccination or prior infection) to prevent sustained transmission — calculated as 1 - (1/R0). For measles (R0=15), this is 93%; for COVID-19 (R0=2.5), it's 60%. Below this threshold, outbreaks can still occur
C. A graph showing the number of new infections over time — the shape of the curve (steep spike vs. gradual hill vs. flattened plateau) reveals how fast the disease is spreading and whether interventions are working
D. The probability that contact between an infected and susceptible person results in transmission — determined by pathogen biology (airborne vs. contact), viral load, duration of exposure, and protective measures like masks or ventilation

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

SCENARIO: Uncontrolled Outbreak
Settings: R0: 2.5 | Vaccination: 0% | Interventions: None
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Vaccination Shield
Settings: R0: 2.5 | Vaccination: 60% | Interventions: None
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Timing Is Everything
Settings: R0: 2.5 | Social distancing at Day 10 vs. Day 30
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

1. Why does exponential growth make early-stage pandemics so deceptively dangerous — and why do people consistently underestimate the threat until it's too late?

   _________________________________________________________

   _________________________________________________________

2. How does the herd immunity threshold equation (1 - 1/R0) explain why measles outbreaks occur even in highly vaccinated populations?

   _________________________________________________________

   _________________________________________________________

3. Why do epidemiologists say 'if it looks like you overreacted, you probably did it right' — what does this reveal about the paradox of successful early intervention?

   _________________________________________________________

   _________________________________________________________

4. How could your model be extended to account for superspreader events, which make disease spread far more uneven than a simple R0 value suggests?

   _________________________________________________________

   _________________________________________________________

5. What are the ethical trade-offs between implementing early, aggressive interventions (which cause economic harm but save lives) and waiting for more data (which costs lives but reduces economic disruption)?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Why do some outbreaks burn out on their own while others explode into global pandemics — and what determines whether we can stop them? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Using Mathematics and Computational Thinking
   □ Disciplinary Core Idea: LS2.A Interdependent Relationships in Ecosystems / LS4.D Biodiversity and Humans
   □ Crosscutting Concept: Cause and Effect

3. What are the ethical trade-offs between implementing early, aggressive interventions (which cause economic harm but save lives) and waiting for more data (which costs lives but reduces economic disruption)?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Pandemic Response Plan
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design an evidence-based pandemic response plan for a novel respiratory pathogen, specifying intervention triggers, timing, and resource allocation to minimize both infections and economic disruption.

SCENARIO: A novel respiratory virus with R0=3.0 has been detected in a city of 2 million people. Initial cases are doubling every 4 days. No vaccine exists yet, but one could be available in 6 months. Your public health team must design a response plan that specifies when to implement social distancing, testing and contact tracing protocols, and resource allocation for hospitals — with the constraint that economic shutdown costs $500 million per month.

GUIDING QUESTIONS:
• At what infection threshold should you implement social distancing — and what does your model show happens if you wait until hospitals are at capacity?
• How do you balance the economic cost of early intervention against the health cost of delayed intervention?
• What combination of interventions keeps Re below 1 while minimizing economic disruption?

DESIGN THINKING:
• What epidemiological data triggers each phase of your response plan?

  _________________________________________________________

• How would you allocate limited testing capacity to maximize the effectiveness of contact tracing?

  _________________________________________________________

• What is the minimum level of social distancing needed to keep Re below 1 for this pathogen?

  _________________________________________________________

• How would you communicate the necessity of early intervention to a skeptical public that sees only a few cases?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Response plan specifies precise intervention triggers based on epidemiological indicators, demonstrates with model data that the timing prevents hospital overflow, balances economic cost against health outcomes with quantitative comparison, and includes a communication strategy addressing public perception
• Proficient (3): Response plan includes intervention timing and resource allocation with model evidence, and considers the trade-off between health and economic costs
• Developing (2): Response plan describes interventions but lacks specific triggers, timing justification, or model-based evidence for the strategy
• Beginning (1): Response plan is incomplete, proposes interventions without timing or evidence, or ignores the exponential growth dynamics that make timing critical

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CAST-Aligned Pre/Post Assessment

### Administration Instructions

These 5 multiple-choice questions are administered identically as both a pre-assessment (before Activity 1) and a post-assessment (after Activity 4). Score each out of 5. Learning growth = post-score minus pre-score.

Questions follow the California Science Test (CAST) stimulus-response format. Each item is three-dimensional, assessing a Science and Engineering Practice (SEP), Disciplinary Core Idea (DCI), and Crosscutting Concept (CCC) simultaneously, aligned to HS-LS2-2, HS-LS4-6.

---

### Question 1

CAST Alignment: SEP 2.1.1 (Determine components of a system) + DCI LS2.2 + CCC4 (Systems and System Models)

A student is using the ModelIt platform to study the system in this lesson. The model includes these components: R0 Value, Vaccination Rate, Susceptible Population, Infection Rate, Recovery Rate, Effective R (Re). Some components are external (R0 Value, Vaccination Rate) and some are internal (Susceptible Population, Infection Rate, Recovery Rate, Effective R (Re)). The student needs to understand what each component represents and how they are organized.

A student's model shows that implementing social distancing on day 10 of an outbreak reduces total infections by 85%, but implementing the same measure on day 30 reduces total infections by only 22%. Which mathematical concept best explains this dramatic difference?

A. Social distancing becomes less effective over time because the virus adapts
B. Exponential growth means the 20-day delay allows the infected population to double approximately 5 times (at a 4-day doubling period), resulting in roughly 32 times more infections at the point of intervention
C. The model assigns less effectiveness to later interventions
D. Social distancing only works in the first two weeks of any outbreak

Correct Answer: B

Feedback: Correct. During exponential growth, delays are devastating. With a 4-day doubling period, 20 days represents 5 doublings: 2^5 = 32. Intervening at 32x the infection level means 32x more people are already infected and transmitting. The same intervention is applied to a vastly larger problem, reducing its relative impact dramatically. If you chose A, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose C, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows.

---

### Question 2

CAST Alignment: SEP 2.1.2 (Determine relationships among components) + DCI LS2.2 + CCC2 (Cause and Effect)

In the computational model for this lesson, a student draws arrows between components to show relationships. The model shows that when R0 Value increases, Infection Rate increases; when Vaccination Rate increases, Susceptible Population decreases. The student is trying to understand why these relationships are positive or negative.

The model compares an uncontrolled outbreak (R0 = 2.5, no interventions) with a managed outbreak (same R0, vaccination + social distancing started at day 14). The uncontrolled outbreak infects 78% of the population; the managed outbreak infects 31%. A student observes that Re dropped below 1 on day 42 in the managed scenario. What caused Re to cross this critical threshold?

A. The virus mutated to become less contagious at day 42
B. The combination of growing natural immunity from recovered individuals, vaccine-induced immunity, and reduced contact rates from social distancing collectively reduced the susceptible population below the level needed to sustain Re above 1
C. All infected individuals recovered simultaneously on day 42
D. The model automatically forces Re below 1 after a fixed number of days

Correct Answer: B

Feedback: Correct. Re = R0 * (susceptible fraction) * (1 - intervention effectiveness). Three factors compound: natural immunity removes people from the susceptible pool, vaccination removes more, and social distancing reduces the transmission probability per contact. Together they pushed the effective susceptible fraction below the epidemic threshold. If you chose A, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose C, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows.

---

### Question 3

CAST Alignment: SEP 2.1.3 (Evaluate a model's accuracy) + DCI LS2.2 + CCC4 (Systems and System Models)

A student runs a simulation of the model. The model shows that when R0 Value increases, Infection Rate increases and when Vaccination Rate increases, Susceptible Population decreases and when Susceptible Population increases, Effective R increases. The student changes one variable to see how the whole system responds.

A student compares two diseases in the model: Disease A (R0 = 2, 14-day infectious period) and Disease B (R0 = 2, 3-day infectious period). Both produce the same peak infection percentage but Disease B's epidemic is over in 45 days while Disease A's lasts 180 days. Which analysis best explains the timeline difference?

A. Disease B is more dangerous because it spreads faster
B. With the same R0 but shorter infectious period, Disease B must have a higher per-day transmission probability. This compresses the same total epidemic into a shorter timeframe because each generation of infection cycles faster, even though the final size is determined by R0
C. Disease A is less contagious than Disease B
D. The infectious period has no effect on epidemic timeline

Correct Answer: B

Feedback: Correct. R0 determines the final epidemic size (how many total infections), but the generation time (related to infectious period) determines the speed. Disease B cycles through the S-I-R compartments much faster because each infected person transmits and recovers in 3 days instead of 14, compressing the same total epidemic into fewer days. If you chose A, this answer suggests something is being added to the system. Look carefully at the model — the total amount stays the same even when components change. The system is conserving matter or energy. If you chose C, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, the model shows these components ARE connected. When one changes, it affects the others through the relationships (positive or negative) that you mapped in the model.

---

### Question 4

CAST Alignment: SEP 2.1.4 (Represent mechanisms to explain/predict events) + DCI LS2.2 + CCC4 (Systems and System Models)

Scientists are studying data related to this system. They collected observations over time and noticed patterns in how the components change. The data shows how changes in one part of the system cascade through the other parts.

The model shows that quarantining 50% of detected cases reduces total infections by 40%, while quarantining 90% of detected cases reduces total infections by 75%. A student notes this is not proportional. Which factor accounts for the diminishing returns?

A. Quarantine becomes less effective at higher rates because the virus evolves to escape
B. Undetected presymptomatic and asymptomatic transmission continues regardless of quarantine rates for detected cases, creating a transmission floor that quarantine alone cannot eliminate
C. The model incorrectly calculates quarantine effectiveness at high rates
D. People refuse to comply with quarantine at higher rates

Correct Answer: B

Feedback: Correct. Quarantine can only isolate DETECTED cases. Presymptomatic transmission (before symptoms appear) and asymptomatic transmission (in people who never show symptoms) create chains of invisible spread that are unaffected by quarantine. This undetectable transmission becomes the dominant pathway as quarantine catches more detected cases. If you chose A, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose C, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows.

---

### Question 5

CAST Alignment: SEP 2.1.5 (Apply a model to make predictions) + DCI LS2.2 + CCC4 (Systems and System Models)

A team wants to use the model to solve a real-world problem related to this system. They know they cannot control the external components (R0 Value, Vaccination Rate), but they can take action on internal components (Susceptible Population, Infection Rate, Recovery Rate, Effective R (Re)). They need to decide which action would be most effective based on what the model shows.

Based on the complete model analysis, a public health official must choose between two strategies with limited resources: (A) achieve 60% vaccination coverage slowly over 6 months, or (B) achieve 40% vaccination coverage quickly in the first 2 months. For a disease with R0 = 2.5 and herd immunity threshold of 60%, which strategy does the model predict will result in fewer total infections, and why?

A. Strategy A, because 60% coverage meets the herd immunity threshold
B. Strategy B, because early vaccination during exponential growth has a disproportionate impact on total infections: reducing Re below 1 even temporarily during the early exponential phase prevents far more infections than reaching a higher final coverage after the epidemic peak has already passed
C. Both strategies produce identical outcomes because the same number of people are eventually vaccinated
D. Strategy A, because higher coverage is always better regardless of timing

Correct Answer: B

Feedback: Correct. The model demonstrates that timing matters more than final coverage during exponential growth. Vaccinating 40% of the population in the first 2 months reduces Re during the critical growth phase, potentially preventing millions of infections that would otherwise occur before Strategy A reaches its higher but later coverage target. The epidemic does not wait for vaccination programs to finish. If you chose A, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose C, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows.

---

### Answer Key

Question 1: B (Cognitive Level: Identify — SEP 2.1.1, DCI LS2.2, CCC4)
Question 2: B (Cognitive Level: Reason — SEP 2.1.2, DCI LS2.2, CCC2)
Question 3: B (Cognitive Level: Reason — SEP 2.1.3, DCI LS2.2, CCC4)
Question 4: B (Cognitive Level: Reason + Evidence — SEP 2.1.4, DCI LS2.2, CCC4)
Question 5: B (Cognitive Level: Predict + Apply — SEP 2.1.5, DCI LS2.2, CCC4)


## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-11/G11L1-L10/G11L1-L10-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-11/G11L1-L10/G11L1-L10-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-11/G11L1-L10/G11L1-L10-Student-Presentation.pptx] |
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