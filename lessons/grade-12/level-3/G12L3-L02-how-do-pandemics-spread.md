# Lesson: How Do Pandemics Spread?

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G12L3-L02 |
| **Grade** | 12th Grade — Level 3: Capstone Innovation Lab |
| **Lesson Name** | How Do Pandemics Spread? |
| **Status** | Template |

---

## Platform

### Title
**How Do Pandemics Spread? — Modeling Epidemiological Dynamics, Transmission Networks, and Intervention Strategies**

### Overview
Pandemics have shaped human history more profoundly than wars or political revolutions. The 1918 influenza killed 50-100 million people. HIV/AIDS has killed over 40 million since 1981. COVID-19 caused over 20 million excess deaths worldwide. Yet despite this devastating history, most people struggle to understand why pandemics are so dangerous — because the human brain is not wired to intuitively grasp exponential growth. Students investigate the driving question: When a new virus emerges, it can circle the globe in weeks, infecting millions before scientists even identify it. How do mathematical models predict pandemic trajectories, and why do small differences in transmission rate or intervention timing determine whether thousands or millions die? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of diverse 17-18 year old students examining a large interactive display showing a global pandemic spread map with infection curves and transmission networks, modern science classroom, featuring a diverse multicultural group with Black people centered]

### Grade
12th Grade — Level 3: Capstone Innovation Lab

### NGSS Standard
**HS-LS2-8**: Evaluate the evidence for the role of group behavior on individual and species' chances to survive and reproduce.

### Learning Objectives
- Model how the basic reproduction number (R0), population density, contact patterns, and intervention timing interact to determine pandemic severity
- Analyze the exponential mathematics of disease transmission and explain why early interventions have disproportionately large effects on total infections
- Evaluate the effectiveness of vaccination, quarantine, mask mandates, and social distancing as intervention strategies using model-derived evidence
- Predict how changes in viral mutation rate, population immunity, and healthcare capacity affect pandemic outcomes and intervention requirements

### Component List (Starting Model: 10 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Viral Transmissibility (R0) | External | The inherent infectiousness of the pathogen determined by its biological properties — how efficiently it spreads through respiratory droplets, aerosols, or contact, independent of population behavior or interventions |
| Population Density | External | The number of people per unit area in the affected region — higher density means more frequent close contacts, shorter transmission chains, and faster exponential growth during the early phase of an outbreak |
| Initial Immune Fraction | External | The proportion of the population with pre-existing immunity from prior infection or vaccination before the outbreak begins — higher baseline immunity slows early transmission by reducing the pool of susceptible individuals |
| Contact Rate | Internal | The average number of close contacts each person has per day — influenced by cultural norms, urban design, workplace structure, and public health policies like social distancing mandates |
| Infection Detection Rate | Internal | The proportion of infected individuals who are identified through testing and surveillance within 48 hours of becoming infectious — higher detection enables faster quarantine and contact tracing |
| Quarantine Compliance | Internal | The percentage of identified infected individuals and their contacts who successfully isolate for the required duration — affected by economic support, housing conditions, cultural trust in health authorities, and enforcement mechanisms |
| Vaccination Coverage Rate | Internal | The percentage of the population that is vaccinated per week once a vaccine becomes available — determined by manufacturing capacity, distribution infrastructure, public willingness, and equitable access across communities |
| Healthcare System Capacity | Internal | The number of hospital beds, ICU units, ventilators, and trained staff available relative to patient demand — when capacity is exceeded, mortality rates increase dramatically as treatable patients cannot receive care |
| Mutation Rate | Internal | The frequency at which the pathogen undergoes genetic changes that may alter transmissibility, virulence, or immune evasion — higher mutation rates increase the probability of variants that escape existing immunity |
| Cumulative Mortality | Internal | The total number of deaths caused by the pandemic — determined by the interaction of infection rate, healthcare capacity, viral virulence, and the timing and effectiveness of interventions |

### Research for Lesson
- The Mathematics of Exponential Growth — reference materials and textbook resources
- The SIR Model Framework — reference materials and textbook resources
- Intervention Mechanics — reference materials and textbook resources
- Equity and Pandemic Impact — reference materials and textbook resources

---

## Activity 1: LOCATE — Build Your System

### Text Editor

```
HOW DO PANDEMICS SPREAD?

Modeling Epidemiological Dynamics, Transmission Networks, and Intervention Strategies.
When a new virus emerges, it can circle the globe in weeks, infecting millions before scientists even identify it. How do mathematical models predict pandemic trajectories, and why do small differences in transmission rate or intervention timing determine whether thousands or millions die?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Viral Transmissibility (R0)" — the inherent infectiousness of the pathogen determined by its biological properties — how efficiently it spreads through respiratory droplets
  ○ Click "Population Density" — the number of people per unit area in the affected region — higher density means more frequent close contacts
  ○ Click "Initial Immune Fraction" — the proportion of the population with pre-existing immunity from prior infection or vaccination before the outbreak begins — higher baseline immunity slows early transmission by reducing the pool of susceptible individuals
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Contact Rate" — the average number of close contacts each person has per day — influenced by cultural norms
  ○ Click "Infection Detection Rate" — the proportion of infected individuals who are identified through testing and surveillance within 48 hours of becoming infectious — higher detection enables faster quarantine and contact tracing
  ○ Click "Quarantine Compliance" — the percentage of identified infected individuals and their contacts who successfully isolate for the required duration — affected by economic support
  ○ Click "Vaccination Coverage Rate" — the percentage of the population that is vaccinated per week once a vaccine becomes available — determined by manufacturing capacity
  ○ Click "Healthcare System Capacity" — the number of hospital beds
  ○ Click "Mutation Rate" — the frequency at which the pathogen undergoes genetic changes that may alter transmissibility
  ○ Click "Cumulative Mortality" — the total number of deaths caused by the pandemic — determined by the interaction of infection rate

STEP 2: ADD TO YOUR MODEL
• Click the PLUS (+) button to add each component to your picture
• You should now see 10 components on your canvas

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
"When a new virus emerges, it can circle the globe in weeks, infecting millions before scientists even identify it. How do mathematical models predict pandemic trajectories, and why do small differences in transmission rate or intervention timing determine whether thousands or millions die?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Viral Transmissibility (R0)' — that's external. The inherent infectiousness of the pathogen determined by its biological properties — how efficiently it spreads through respiratory droplets.
Click on 'Population Density' — that's external. The number of people per unit area in the affected region — higher density means more frequent close contacts.
Click on 'Initial Immune Fraction' — that's external. The proportion of the population with pre-existing immunity from prior infection or vaccination before the outbreak begins — higher baseline immunity slows early transmission by reducing the pool of susceptible individuals.
Click on 'Contact Rate' — that's internal. The average number of close contacts each person has per day — influenced by cultural norms.
Click on 'Infection Detection Rate' — that's internal. The proportion of infected individuals who are identified through testing and surveillance within 48 hours of becoming infectious — higher detection enables faster quarantine and contact tracing.
Click on 'Quarantine Compliance' — that's internal. The percentage of identified infected individuals and their contacts who successfully isolate for the required duration — affected by economic support.
Click on 'Vaccination Coverage Rate' — that's internal. The percentage of the population that is vaccinated per week once a vaccine becomes available — determined by manufacturing capacity.
Click on 'Healthcare System Capacity' — that's internal. The number of hospital beds.
Click on 'Mutation Rate' — that's internal. The frequency at which the pathogen undergoes genetic changes that may alter transmissibility.
Click on 'Cumulative Mortality' — that's internal. The total number of deaths caused by the pandemic — determined by the interaction of infection rate.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Viral Transmissibility (R0), Population Density, and Initial Immune Fraction are external components because they represent pre-existing conditions that define the starting state of the pandemic — the virus's biology, the city's structure, and the population's immunological history cannot be changed once an outbreak begins. Contact Rate, Infection Detection Rate, Quarantine Compliance, Vaccination Coverage Rate, Healthcare System Capacity, Mutation Rate, and Cumulative Mortality are internal because they represent dynamics that emerge from the interaction between the virus and human response — they can be influenced by policy decisions, resource allocation, and collective behavior.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next activity, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 10 components sorted: Viral Transmissibility (R0), Population Density, Initial Immune Fraction (External), Contact Rate, Infection Detection Rate, Quarantine Compliance, Vaccination Coverage Rate, Healthcare System Capacity, Mutation Rate, Cumulative Mortality (Internal)]

### Graph
[Empty graph panel — no simulation yet]

---

## Activity 2: ESTABLISH — Connect the Relationships

### Text Editor

```
TIME TO DRAW THE INVISIBLE LINES

Those 10 components don't just sit there — they AFFECT each other.
When one changes, others change too. Let's map those connections.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: OPEN CONNECTION MODE
• Click the "Connect" icon in the TOP LEFT corner of your screen
• Your cursor is now ready to draw relationship arrows

STEP 2: DRAW YOUR RELATIONSHIPS
• Click on "Viral Transmissibility" and drag an arrow to "Cumulative Mortality"
• Click on "Population Density" and drag an arrow to "Contact Rate"
• Click on "Contact Rate" and drag an arrow to "Cumulative Mortality"
• Click on "Infection Detection Rate" and drag an arrow to "Quarantine Compliance"
• Click on "Vaccination Coverage Rate" and drag an arrow to "Cumulative Mortality"
• Click on "Healthcare System Capacity" and drag an arrow to "Cumulative Mortality"
• Click on "Mutation Rate" and drag an arrow to "Vaccination Coverage Rate"
• Click on "Quarantine Compliance" and drag an arrow to "Cumulative Mortality"

STEP 3: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Viral Transmissibility → Cumulative Mortality = POSITIVE (+)
    Higher R0 means faster exponential growth, more infections before interventions take effect, and greater likelihood of overwhelming healthcare capacity, all of which increase total deaths.

  ○ Population Density → Contact Rate = POSITIVE (+)
    Denser populations have more frequent close contacts in housing, transportation, workplaces, and public spaces, directly increasing the number of transmission opportunities per infected person per day.

  ○ Contact Rate → Cumulative Mortality = POSITIVE (+)
    Higher contact rates amplify the effective reproduction number, accelerating transmission and increasing the total number of infections. Reducing contact rate through social distancing is one of the most powerful intervention levers.

  ○ Infection Detection Rate → Quarantine Compliance = POSITIVE (+)
    Faster detection of infected individuals enables earlier quarantine of cases and contacts. Without detection, quarantine is impossible; with rapid detection, transmission chains can be broken before secondary spread occurs.

  ○ Vaccination Coverage Rate → Cumulative Mortality = NEGATIVE (−)
    Higher vaccination coverage reduces the susceptible population, lowering the effective reproduction number. Once vaccination exceeds the herd immunity threshold, sustained transmission becomes impossible and mortality stabilizes.

  ○ Healthcare System Capacity → Cumulative Mortality = NEGATIVE (−)
    Greater healthcare capacity means more patients receive treatment, reducing the case fatality rate. When capacity is exceeded, treatable patients die from lack of care, and mortality rates can increase 3-5 fold.

  ○ Mutation Rate → Vaccination Coverage Rate = NEGATIVE (−)
    Higher mutation rates increase the probability of immune-evasive variants that reduce vaccine effectiveness, potentially requiring booster campaigns and resetting progress toward herd immunity.

  ○ Quarantine Compliance → Cumulative Mortality = NEGATIVE (−)
    Higher quarantine compliance removes infectious individuals from the transmission chain faster, reducing secondary infections. Even moderate improvements in compliance have large effects because they break exponential transmission chains.

STEP 4: CHECK YOUR MODEL
• You should have 8 arrows total
• 4 negative relationship(s), 4 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: If R0 is 3 and you reduce Contact Rate by 50% through social distancing, the effective reproduction number drops to 1.5 — still above 1, so the pandemic still grows. What combination of interventions does your model suggest is needed to push the effective R0 below 1 and stop exponential spread?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Viral Transmissibility' and drag an arrow
over to 'Cumulative Mortality.'

Here's the key question: When viral transmissibility goes UP, does
cumulative mortality go UP or DOWN?

Higher R0 means faster exponential growth, more infections before interventions take effect, and greater likelihood of overwhelming healthcare capacity, all of which increase total deaths.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Population Density' and drag an arrow
over to 'Contact Rate.'

Here's the key question: When population density goes UP, does
contact rate go UP or DOWN?

Denser populations have more frequent close contacts in housing, transportation, workplaces, and public spaces, directly increasing the number of transmission opportunities per infected person per day.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'Contact Rate' and drag an arrow
over to 'Cumulative Mortality.'

Here's the key question: When contact rate goes UP, does
cumulative mortality go UP or DOWN?

Higher contact rates amplify the effective reproduction number, accelerating transmission and increasing the total number of infections. Reducing contact rate through social distancing is one of the most powerful intervention levers.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Final connection: Click on 'Infection Detection Rate' and drag an arrow
over to 'Quarantine Compliance.'

Here's the key question: When infection detection rate goes UP, does
quarantine compliance go UP or DOWN?

Faster detection of infected individuals enables earlier quarantine of cases and contacts. Without detection, quarantine is impossible; with rapid detection, transmission chains can be broken before secondary spread occurs.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Final connection: Click on 'Vaccination Coverage Rate' and drag an arrow
over to 'Cumulative Mortality.'

Here's the key question: When vaccination coverage rate goes UP, does
cumulative mortality go UP or DOWN?

Higher vaccination coverage reduces the susceptible population, lowering the effective reproduction number. Once vaccination exceeds the herd immunity threshold, sustained transmission becomes impossible and mortality stabilizes.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Healthcare System Capacity' and drag an arrow
over to 'Cumulative Mortality.'

Here's the key question: When healthcare system capacity goes UP, does
cumulative mortality go UP or DOWN?

Greater healthcare capacity means more patients receive treatment, reducing the case fatality rate. When capacity is exceeded, treatable patients die from lack of care, and mortality rates can increase 3-5 fold.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Mutation Rate' and drag an arrow
over to 'Vaccination Coverage Rate.'

Here's the key question: When mutation rate goes UP, does
vaccination coverage rate go UP or DOWN?

Higher mutation rates increase the probability of immune-evasive variants that reduce vaccine effectiveness, potentially requiring booster campaigns and resetting progress toward herd immunity.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Quarantine Compliance' and drag an arrow
over to 'Cumulative Mortality.'

Here's the key question: When quarantine compliance goes UP, does
cumulative mortality go UP or DOWN?

Higher quarantine compliance removes infectious individuals from the transmission chain faster, reducing secondary infections. Even moderate improvements in compliance have large effects because they break exponential transmission chains.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Look at your model now. You've got 4 negative and 4
positive relationships. 8 arrows total.

If R0 is 3 and you reduce Contact Rate by 50% through social distancing, the effective reproduction number drops to 1.5 — still above 1, so the pandemic still grows. What combination of interventions does your model suggest is needed to push the effective R0 below 1 and stop exponential spread?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Viral Transmissibility +→ Cumulative Mortality, Population Density +→ Contact Rate, Contact Rate +→ Cumulative Mortality, Infection Detection Rate +→ Quarantine Compliance, Vaccination Coverage Rate −→ Cumulative Mortality, Healthcare System Capacity −→ Cumulative Mortality, Mutation Rate −→ Vaccination Coverage Rate, Quarantine Compliance −→ Cumulative Mortality]

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
• When Viral Transmissibility (R0) is HIGH, what happens to the internal components?

STEP 3: SCENARIO — UNCONTROLLED SPREAD
• R0: 3 | Population Density: High | Initial Immunity: 0% | No interventions
• PREDICT FIRST: What do you predict happens to the epidemiological curve and healthcare capacity when a highly transmissible virus spreads through a completely susceptible population with no interventions?
• Resume the simulation and observe what happens
• Was your prediction correct?

STEP 4: SCENARIO — EARLY VS. LATE INTERVENTION
• R0: 3 | Interventions start at Week 2 vs. Week 6
• PREDICT FIRST: How much difference do you predict four weeks of delay in implementing interventions makes to total infections and deaths?
• Resume the simulation and observe what happens
• Was your prediction correct?

STEP 5: SCENARIO — VARIANT EMERGENCE
• R0: 3 initially | Mutation Rate: High | Immune evasion variant appears at Week 20
• PREDICT FIRST: What do you predict happens when a variant emerges that partially evades existing immunity in a population that was approaching herd immunity?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Exponential growth is deceptively slow at first and then explosively fast — by the time a pandemic is visibly widespread, the window for effective early intervention has already closed, which is why mathematical models are essential for triggering preemptive action
• The timing of interventions matters more than their intensity — implementing moderate social distancing two weeks after the first case prevents more deaths than implementing strict lockdowns six weeks later, because exponential growth makes every day of delay dramatically more costly
• Healthcare capacity creates a mortality multiplier — when hospitals are overwhelmed, deaths increase not only from the pandemic disease but from all other conditions that cannot receive treatment, meaning the true death toll far exceeds direct infection mortality
• Herd immunity is not a fixed threshold but a moving target — viral mutations that increase transmissibility raise the herd immunity threshold, and variants that evade immunity reset the susceptible population, meaning a pandemic can have multiple waves even with high vaccination rates

THE ANSWER: Pandemics spread through the mathematics of exponential growth, where each infected person transmits to an average of R0 others, who each transmit to R0 more, creating a chain reaction that can infect millions within weeks. Our model reveals that the outcome is determined by the race between viral transmission and human intervention. Small differences in timing have enormous consequences: intervening two weeks earlier can reduce total deaths by 50-80% because exponential growth means the number of infections doubles every few days. Vaccination works by reducing the susceptible population below the herd immunity threshold, but it must be deployed faster than the virus mutates. The most dangerous moment in a pandemic is when everything looks fine — because exponential growth is invisible until it becomes overwhelming.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Uncontrolled Spread. R0: 3 | Population Density: High | Initial Immunity: 0% | No interventions.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Early vs. Late Intervention.
R0: 3 | Interventions start at Week 2 vs. Week 6.

Before you run it — make a prediction. How much difference do you predict four weeks of delay in implementing interventions makes to total infections and deaths?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Variant Emergence. R0: 3 initially | Mutation Rate: High | Immune evasion variant appears at Week 20.
What do you predict happens when a variant emerges that partially evades existing immunity in a population that was approaching herd immunity?

Here's what our model reveals: Pandemics spread through the mathematics of exponential growth, where each infected person transmits to an average of R0 others, who each transmit to R0 more, creating a chain reaction that can infect millions within weeks. Our model reveals that the outcome is determined by the race between viral transmission and human intervention. Small differences in timing have enormous consequences: intervening two weeks earlier can reduce total deaths by 50-80% because exponential growth means the number of infections doubles every few days. Vaccination works by reducing the susceptible population below the herd immunity threshold, but it must be deployed faster than the virus mutates. The most dangerous moment in a pandemic is when everything looks fine — because exponential growth is invisible until it becomes overwhelming.

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
   • What happens if you turn OFF Viral Transmissibility (R0)?
   • What happens if you turn OFF Population Density?
   • What happens if you turn OFF Initial Immune Fraction?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Economic Impact Index — The cumulative economic damage from both the pandemic itself and the interventions used to control it — business closures, unemployment, supply chain disruption, and healthcare costs that disproportionately affect low-income communities and create pressure to relax interventions prematurely
   • Misinformation Spread Rate — The velocity at which false health information propagates through social media and community networks — misinformation reduces vaccination uptake, quarantine compliance, and trust in public health authorities, effectively increasing the virus's transmission advantage
   • Genomic Surveillance Capacity — The ability to sequence viral genomes from patient samples to detect emerging variants early — countries with strong genomic surveillance can identify immune-evasive or more transmissible variants weeks before they become dominant, enabling proactive rather than reactive public health responses

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • The Mathematics of Exponential Growth — how does this connect to your model?
   • The SIR Model Framework — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model demonstrate why exponential growth makes early intervention timing far more important than intervention intensity?
   • What does the model reveal about why healthcare capacity is a mortality multiplier rather than just a treatment variable?
   • Why is herd immunity a moving target rather than a fixed threshold, and what does this mean for vaccination strategy?
   • How would adding economic impact or misinformation to your model change the predicted effectiveness of interventions?

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

Your model has 10 components. Real systems involve
way more. Think about...

Economic Impact Index. The cumulative economic damage from both the pandemic itself and the interventions used to control it — business closures, unemployment, supply chain disruption, and healthcare costs that disproportionately affect low-income communities and create pressure to relax interventions prematurely
How would you model that?

Misinformation Spread Rate. The velocity at which false health information propagates through social media and community networks — misinformation reduces vaccination uptake, quarantine compliance, and trust in public health authorities, effectively increasing the virus's transmission advantage
How would you model that?

Genomic Surveillance Capacity. The ability to sequence viral genomes from patient samples to detect emerging variants early — countries with strong genomic surveillance can identify immune-evasive or more transmissible variants weeks before they become dominant, enabling proactive rather than reactive public health responses
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

Epidemiologists who track and model disease outbreaks earn $60,000-$120,000/year at agencies like the CDC, WHO, and state health departments. Biostatisticians who build mathematical models of pandemic spread earn $75,000-$140,000/year. Public health emergency preparedness directors coordinate city and county pandemic response, earning $80,000-$150,000/year. Infectious disease physicians who treat patients during outbreaks earn $200,000-$350,000/year.

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
Say: "In January 2020, a handful of mysterious pneumonia cases appeared in Wuhan, China. Twelve months later, COVID-19 had infected over 100 million people and killed over 2 million. How does a single case become a global catastrophe? The answer is mathematics — and today you will learn to read the equations that predict pandemics."
Do: Show cover image. Ask: how many of you were personally affected by COVID-19? Acknowledge the lived experience in the room before moving to the science.
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and vocabulary terms displayed
Say: "Today you are building a mathematical model of pandemic spread. You will discover why exponential growth is so deceptive, why timing matters more than intensity, and why equity is an epidemiological variable, not just a moral one."
Do: Have students read objectives. Pre-teach R0 with a physical demonstration: give one student 3 cards, each of those students gets 3 cards, and count how fast the classroom is 'infected.' 
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: Epidemiological curve showing exponential growth phase
Say: "Small differences in transmission rate or intervention timing can mean the difference between thousands and millions of deaths. Why? Because your brain cannot intuitively understand exponential growth. Today your model will teach your brain what it cannot feel."
Do: Quick-write: Students estimate how many people one infected person with R0=3 would ultimately infect after 15 transmission generations. Reveal the answer (over 14 million) to demonstrate exponential growth intuition failure.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps overview with pandemic context
Say: "We will Label ten components of the pandemic system, Establish their relationships, Visualize how they interact, Evaluate intervention scenarios, and Refine by adding equity and information variables."
Do: Preview each LEVER step. Emphasize that this model will explain why the same virus can kill 1,000 in one city and 100,000 in another.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Ten component cards for the pandemic system
Say: "Three of these components describe the virus and the population it enters — the inputs we cannot control initially. Seven describe the human response — the variables we CAN control. Sorting them correctly is the first step to understanding why intervention design matters."
Do: Students sort external versus internal components. Debate: is Contact Rate external or internal? It reflects both cultural norms and policy choices. Use this to discuss the boundary between behavior and biology.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows between pandemic components
Say: "R0 drives infection rate. Contact rate multiplies transmission. Quarantine removes infectious people from circulation. Vaccination shrinks the susceptible pool. But these all interact — and some relationships create reinforcing feedback loops that can make a pandemic spiral out of control."
Do: Students draw arrows showing positive and negative relationships. Identify the critical feedback loop: overwhelmed healthcare -> higher mortality -> public fear -> better compliance but also economic collapse -> reduced compliance.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Simulation dashboard with epidemiological curves
Say: "Now run three scenarios: uncontrolled spread, early intervention, and vaccine rollout. Record your predictions BEFORE you run each scenario. The gap between what you predict and what happens will teach you something important about your intuition."
Do: Students run all scenarios, recording predictions versus observations. Key question after each: how close was your prediction? Most students will underestimate exponential growth and underestimate the impact of early intervention.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key findings summary with comparative mortality graphs
Say: "Your model reveals a brutal truth: in a pandemic, every day of delay costs lives — not linearly, but exponentially. The difference between acting at 100 cases and acting at 1,000 cases is not 10x more deaths. It can be 50x or 100x more deaths."
Do: Class discussion of discoveries. Show the comparative mortality graphs from the three scenarios. Ask: knowing this, why do governments often delay action?
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Engineering challenge: Design a Pandemic Preparedness Plan
Say: "A novel virus with R0 of 4 is approaching your city. You have 2-4 weeks before the first case arrives. No vaccine exists. Design a preparedness plan that saves the most lives while keeping the city functioning. Your model data is your evidence."
Do: Groups design preparedness plans with specific timelines, trigger points, and interventions. Each team must justify every decision with model evidence. Present and compare: which plan saves the most lives? Which is most equitable?
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: How Do Pandemics Spread?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
Pandemics have shaped human history more profoundly than wars or political revolutions. The 1918 influenza killed 50-100 million people. HIV/AIDS has killed over 40 million since 1981. COVID-19 caused over 20 million excess deaths worldwide. Yet despite this devastating history, most people struggle to understand why pandemics are so dangerous — because the human brain is not wired to intuitively grasp exponential growth.

NGSS ALIGNMENT:
HS-LS2-8: Evaluate the evidence for the role of group behavior on individual and species' chances to survive and reproduce.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Using Mathematics and Computational Thinking
  Students use mathematical models of exponential growth, reproduction numbers, and herd immunity thresholds to predict pandemic trajectories and evaluate intervention effectiveness quantitatively.
• Disciplinary Core Idea: LS2.D Social Interactions and Group Behavior
  Students model how individual behaviors — contact patterns, quarantine compliance, vaccination decisions — aggregate to determine population-level pandemic outcomes, demonstrating that group behavior emerges from but cannot be predicted by individual actions alone.
• Crosscutting Concept: Stability and Change
  Students analyze how pandemic systems can shift rapidly from apparent stability (low case counts) to explosive growth (exponential phase) and identify the tipping points where interventions can restore stability or where delay makes control impossible.

PACING GUIDE:
• Activity 1 (Locate): 8-10 minutes
• Activity 2 (Establish): 8-10 minutes
• Activity 3 (Visualize & Evaluate): 10-12 minutes
• Activity 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Basic Reproduction Number (R0), Herd Immunity Threshold, Epidemiological Curve, Superspreader Event
□ Prepare When a new virus emerges, it can circle the globe in weeks, infecting millions before scientists even identify it. How do mathematical models predict pandemic trajectories, and why do small differences in transmission rate or intervention timing determine whether thousands or millions die discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify ten key components of the pandemic system: viral transmissibility, population density, initial immunity, contact rate, infection detection, quarantine compliance, vaccination coverage, healthcare capacity, mutation rate, and cumulative mortality.
• Establish: Students map the causal relationships showing how R0 drives exponential growth, how interventions reduce the effective reproduction number, and how healthcare capacity creates a mortality threshold effect.
• Visualize: Students build a ten-component computational model showing the competing dynamics between viral transmission and intervention effectiveness, with feedback loops from mutation and waning immunity.
• Evaluate: Students run uncontrolled spread, early intervention, and vaccine rollout scenarios to quantify how timing and intensity of interventions determine total mortality.
• Revise: Students add economic impact, misinformation spread, or genomic surveillance to model how social and informational factors modify the biological dynamics of pandemic spread.

BACKGROUND CONTENT:
• The Mathematics of Exponential Growth:
  If one person infects three others (R0 = 3) and each of those three infects three more, the chain grows from 1 to 3 to 9 to 27 to 81 to 243 to 729 in just six generations. After 20 generations — which can occur in as few as 40-60 days for a respiratory virus — the theoretical number exceeds 3.5 billion. In reality, the growth slows as the susceptible population shrinks, but the key insight is that by the time exponential growth becomes visible (hundreds or thousands of cases), millions of transmission chains are already in progress. This is why epidemiologists sound the alarm when cases number in the dozens — they can see the mathematical future that is invisible to intuition.

• The SIR Model Framework:
  Epidemiologists use compartmental models to track pandemic dynamics. The simplest is SIR: Susceptible, Infected, Recovered. Everyone begins as Susceptible. Infected individuals transmit at rate R0 and eventually move to Recovered (immune) or die. The pandemic ends when enough people have moved from S to R that the remaining susceptible population is too small to sustain transmission — this is herd immunity. The herd immunity threshold is 1 - 1/R0: for R0 = 3, it is 67%; for R0 = 5, it is 80%. More sophisticated models add Exposed (pre-infectious) and Deceased compartments, age structure, spatial heterogeneity, and waning immunity.

• Intervention Mechanics:
  Social distancing reduces the contact rate component of R0. Masks reduce the transmission probability per contact. Quarantine removes infectious individuals from the transmission chain. Vaccination moves people directly from Susceptible to Recovered without experiencing disease. Each intervention has a quantifiable effect on the effective reproduction number (Reff). The goal is to push Reff below 1.0, at which point each infected person transmits to fewer than one other on average and the epidemic declines. The challenge is that interventions have social, economic, and psychological costs that limit duration and compliance.

• Equity and Pandemic Impact:
  Pandemics do not affect all communities equally. COVID-19 mortality rates were 2-3 times higher in Black, Latino, and Indigenous communities in the United States due to structural factors: higher rates of essential worker employment, crowded housing that prevents effective isolation, less access to healthcare, and higher prevalence of underlying conditions caused by chronic stress and environmental exposures. Effective pandemic preparedness must explicitly address these disparities — equitable vaccine distribution, economic support for quarantine compliance, and targeted testing in underserved communities are not just ethical imperatives but epidemiological necessities, because uncontrolled transmission in any subpopulation threatens the entire population.

COMMON MISCONCEPTIONS:
• "Herd immunity will happen naturally so we don't need vaccines"
  Reality: Natural herd immunity requires a large fraction of the population to become infected, which means millions of severe cases and hundreds of thousands of deaths for a disease with even modest fatality rates. For a disease with R0=3 and 1% fatality rate in a country of 330 million, natural herd immunity would require approximately 220 million infections and 2.2 million deaths. Vaccination achieves the same immunological endpoint without the mass casualties.
  Strategy: Calculate the numbers together: for R0 of 3, herd immunity threshold is 67%. In the US population of 330 million, that means 221 million infections. At 1% fatality, that is 2.2 million deaths. Ask: is there a better way to get to 67% immunity?

• "Pandemics end when the virus runs out of people to infect"
  Reality: This is partially true but oversimplified. Pandemics can have multiple waves because immunity wanes over time, new susceptible individuals are born, and viral mutations create variants that evade existing immunity. COVID-19 demonstrated this with successive waves driven by Alpha, Delta, and Omicron variants, each partially escaping prior immunity. A pandemic transitions to endemic status when population immunity stabilizes transmission at a sustainable baseline level.
  Strategy: Show the multi-wave pattern of COVID-19 globally and ask students to identify what changed between waves — variant emergence, waning immunity, behavior changes — that prevented a simple single-wave pattern.

• "Masks and social distancing don't work because the pandemic continued even with those measures"
  Reality: Individual interventions reduce but do not eliminate transmission. The goal is not zero transmission but reducing the effective reproduction number below 1. If R0 is 4 and social distancing reduces contacts by 40% and masks reduce per-contact transmission by 30%, the combined effect reduces Reff to approximately 1.7 — still above 1, meaning the pandemic continues but at a much slower rate with far fewer total deaths. The fact that cases continued does not mean interventions failed; it means the virus was so transmissible that multiple simultaneous interventions were needed.
  Strategy: Use the math: R0 = 4, social distancing reduces contact by 40% (factor of 0.6), masks reduce transmission by 30% (factor of 0.7). Reff = 4 x 0.6 x 0.7 = 1.68. Still above 1, so cases grow, but much more slowly. What additional intervention pushes Reff below 1?

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
Big Question: When a new virus emerges, it can circle the globe in weeks, infecting millions before scientists even identify it. How do mathematical models predict pandemic trajectories, and why do small differences in transmission rate or intervention timing determine whether thousands or millions die?
Answer: Pandemics spread through the mathematics of exponential growth, where each infected person transmits to an average of R0 others, who each transmit to R0 more, creating a chain reaction that can infect millions within weeks. Our model reveals that the outcome is determined by the race between viral transmission and human intervention. Small differences in timing have enormous consequences: intervening two weeks earlier can reduce total deaths by 50-80% because exponential growth means the number of infections doubles every few days. Vaccination works by reducing the susceptible population below the herd immunity threshold, but it must be deployed faster than the virus mutates. The most dangerous moment in a pandemic is when everything looks fine — because exponential growth is invisible until it becomes overwhelming.

Simulation Answers:
• Uncontrolled Spread: With R0 = 3, no immunity, and no interventions, the model shows explosive exponential growth that peaks in 8-12 weeks, overwhelming healthcare capacity by week 4-6. Once hospitals are full, the case fatality rate increases 3-5x because treatable patients cannot receive care. Cumulative mortality reaches its maximum because the epidemic infects the majority of the population before natural herd immunity develops.
• Early vs. Late Intervention: The model demonstrates a dramatic timing effect: implementing social distancing and testing at Week 2 (when cases are in the dozens) reduces cumulative mortality by 60-80% compared to implementing the same measures at Week 6 (when cases are in the thousands). This is because exponential growth means the virus has created thousands of parallel transmission chains during those four weeks of delay, each of which must be independently interrupted.
• Variant Emergence: When a partially immune-evasive variant emerges at Week 20, the model shows a second wave that can be as severe as the first because the effective susceptible population resets. Populations that relied primarily on natural infection for immunity are hit harder than those with high vaccination rates, because vaccines can be updated faster than natural immunity can be rebuilt through reinfection.

Reflection Exemplars:
• Q: Why does intervention timing matter more than intensity?
  A: The model demonstrates this through the mathematics of exponential growth. At Week 2, there might be 50 active infections. At Week 6, there might be 5,000. Implementing a 50% contact reduction at Week 2 prevents thousands of future infections because each prevented case also prevents all downstream transmission chains. The same 50% reduction at Week 6 must interrupt 100 times more active chains. This is why moderate early action outperforms aggressive late action — you are fighting the exponent, not the number. Every day of delay allows the exponential function to compound, making the same intervention less effective.
• Q: How does healthcare capacity create a mortality multiplier?
  A: The model shows a threshold effect: below healthcare capacity, the case fatality rate reflects medical treatment quality (perhaps 1-2%). Above capacity, it reflects untreated disease (perhaps 5-10%). This means that if an uncontrolled pandemic overwhelms hospitals, the death rate per infection increases 3-5 fold. But the effect is even worse because the increased mortality applies to ALL hospital patients, not just pandemic cases — heart attacks, strokes, accidents, and other emergencies also go untreated. Flattening the curve is not just about spreading infections over time; it is about keeping the mortality rate at the treatable level rather than the untreated level.

STEM CHALLENGE GUIDANCE:
Title: Design a Pandemic Preparedness Plan
Mission: Design a comprehensive pandemic preparedness plan for a city of 1 million people that minimizes cumulative mortality while balancing economic, social, and equity considerations, using model data to justify intervention timing and intensity.
Scenario: A novel respiratory virus with an estimated R0 of 4 has been detected in three countries. Your city of 1 million people has zero confirmed cases but the virus is expected to arrive within 2-4 weeks. No vaccine exists yet and development will take 12-18 months. Your team must design a preparedness plan that specifies exactly when and how to implement testing, quarantine, social distancing, healthcare surge capacity, and eventually vaccination — and justify every decision with model data.
Introduction: Present the challenge: A novel respiratory virus with R0 = 4 has been detected in three countries and is expected to reach your city of 1 million people within 2-4 weeks. No vaccine exists and development will take 12-18 months. Your team must design a comprehensive preparedness plan that specifies intervention triggers, timeline, and implementation strategy — justified by model evidence — while addressing equity, economic sustainability, and adaptability to new variants.

Key Concepts:
• Non-Pharmaceutical Interventions: Measures that reduce transmission without medical products: social distancing (reduces contact rate), masks (reduce per-contact transmission probability), hand hygiene (reduces fomite transmission), ventilation improvements (reduce aerosol accumulation), and gathering size limits (reduce superspreader event probability). Each has a quantifiable effect on the effective reproduction number.
• Vaccine Distribution Equity: Historical evidence shows that vaccines reach wealthy communities and nations first, leaving vulnerable populations unprotected. During COVID-19, high-income countries had 60-70% vaccination rates while low-income countries remained below 20%. Equitable distribution is not only a moral imperative but an epidemiological one — uncontrolled transmission in any population generates variants that threaten everyone.
• Syndromic Surveillance: Monitoring emergency department visits, pharmacy sales, school absenteeism, and wastewater viral loads to detect outbreaks before clinical testing confirms them. Wastewater surveillance can detect community transmission 4-7 days before the first positive test, providing critical early warning for intervention activation.

Evaluation Rubric:
• Expert (4): Plan specifies quantitative intervention triggers derived from model data, addresses equity with concrete mechanisms, includes adaptive strategies for variant emergence, and justifies every decision with mathematical evidence from the pandemic model
• Proficient (3): Plan includes reasonable intervention timeline with some model evidence and addresses most equity and adaptability concerns
• Developing (2): Plan describes interventions but lacks specific triggers, timeline, or quantitative connection to model evidence
• Beginning (1): Plan is incomplete or does not connect intervention choices to pandemic dynamics model data

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a simplified exponential growth calculator where students input R0 and generation time to see how quickly infections accumulate over weeks
  • Use a physical demonstration with colored tokens: start with 1 red token (infected) among 30 blue tokens (susceptible) and act out transmission rounds at R0 = 3
  • Sentence frames: 'If R0 is ___ and we reduce contacts by ___%, the effective reproduction number becomes ___, which is above/below 1, meaning the pandemic will grow/shrink because ___.'

Extensions (Advanced Learners):
  • Research the actual COVID-19 responses of two countries (e.g., New Zealand vs. United States) and use your model to explain why their outcomes differed so dramatically
  • Build a spreadsheet-based SIR model that calculates daily new infections, recoveries, and deaths for different R0 values and intervention scenarios
  • Investigate how wastewater epidemiology works as an early warning system and design a wastewater surveillance network for your city

Cross-Curricular Connections:
  • Math: Derive the herd immunity threshold formula (1 - 1/R0) from the SIR model equations and calculate the vaccination percentage needed for diseases with different R0 values: measles (R0=15), COVID-19 Delta (R0=7), seasonal flu (R0=1.3)
  • ELA: Read firsthand accounts from healthcare workers during the COVID-19 surge in New York City in April 2020 and write an analytical essay connecting their experiences to the concept of healthcare capacity as a mortality multiplier
  • History: Compare the public health responses to the 1918 influenza pandemic in Philadelphia (held a large parade, delayed interventions) and St. Louis (implemented early closures) and analyze how the mortality data validates the exponential growth model

CAST ALIGNMENT:
• Model how the basic reproduction number, contact rate, and intervention timing interact to determine the trajectory of an epidemiological curve
• Predict cumulative mortality under different intervention scenarios using mathematical relationships between R0, healthcare capacity, and population immunity
• Evaluate the equity implications of pandemic interventions by analyzing how quarantine feasibility and vaccination access vary across socioeconomic groups

CAST-Style Assessment Questions:
• Multiple Choice: A new virus with R0 = 4 is spreading in a city. Social distancing reduces contacts by 40% and masks reduce transmission probability by 30%. If both are implemented, what is the approximate effective reproduction number, and is this sufficient to stop exponential growth?
• Constructed Response: Using evidence from your model, explain why a city that delays implementing social distancing by just three weeks during the early phase of a pandemic might experience five times more total deaths than a city that acts immediately. Reference the mathematics of exponential growth and at least two model components.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: How Do Pandemics Spread?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. What does it mean when scientists say a virus has an R0 of 3, and why does that matter for how fast a pandemic spreads?

   _________________________________________________________

   _________________________________________________________

2. Why do you think some pandemics kill thousands while others kill millions, even when caused by similar types of viruses?

   _________________________________________________________

   _________________________________________________________

3. What interventions did your community use during the COVID-19 pandemic, and which ones do you think were most effective?

   _________________________________________________________

   _________________________________________________________

4. What do you think 'herd immunity' means and how is it related to vaccination?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Basic Reproduction Number (R0)
___ Herd Immunity Threshold       
___ Epidemiological Curve         
___ Superspreader Event           

A. The average number of secondary infections produced by one infected person in a completely susceptible population — an R0 of 3 means each infected person transmits to 3 others on average, and any disease with R0 greater than 1 will spread exponentially until interventions or immunity reduce the effective reproduction number below 1
B. The proportion of a population that must be immune (through vaccination or prior infection) to prevent sustained transmission — calculated as 1 minus 1/R0, meaning a disease with R0 of 5 requires 80% population immunity to stop spreading
C. A graph showing the number of new infections over time — the shape of this curve determines whether healthcare systems are overwhelmed (tall sharp peak) or can manage the caseload (flattened extended curve), which directly affects mortality rates
D. An incident where a single infected individual transmits to far more people than the average R0 predicts — driven by individual variation in infectiousness, behavior, and environmental conditions such as crowded indoor spaces with poor ventilation

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

SCENARIO: Uncontrolled Spread
Settings: R0: 3 | Population Density: High | Initial Immunity: 0% | No interventions
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Early vs. Late Intervention
Settings: R0: 3 | Interventions start at Week 2 vs. Week 6
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Variant Emergence
Settings: R0: 3 initially | Mutation Rate: High | Immune evasion variant appears at Week 20
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

1. How does your model demonstrate why exponential growth makes early intervention timing far more important than intervention intensity?

   _________________________________________________________

   _________________________________________________________

2. What does the model reveal about why healthcare capacity is a mortality multiplier rather than just a treatment variable?

   _________________________________________________________

   _________________________________________________________

3. Why is herd immunity a moving target rather than a fixed threshold, and what does this mean for vaccination strategy?

   _________________________________________________________

   _________________________________________________________

4. How would adding economic impact or misinformation to your model change the predicted effectiveness of interventions?

   _________________________________________________________

   _________________________________________________________

5. What are the limitations of modeling pandemic spread when individual human behavior varies enormously and changes over time?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. When a new virus emerges, it can circle the globe in weeks, infecting millions before scientists even identify it. How do mathematical models predict pandemic trajectories, and why do small differences in transmission rate or intervention timing determine whether thousands or millions die? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Using Mathematics and Computational Thinking
   □ Disciplinary Core Idea: LS2.D Social Interactions and Group Behavior
   □ Crosscutting Concept: Stability and Change

3. What are the limitations of modeling pandemic spread when individual human behavior varies enormously and changes over time?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Pandemic Preparedness Plan
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design a comprehensive pandemic preparedness plan for a city of 1 million people that minimizes cumulative mortality while balancing economic, social, and equity considerations, using model data to justify intervention timing and intensity.

SCENARIO: A novel respiratory virus with an estimated R0 of 4 has been detected in three countries. Your city of 1 million people has zero confirmed cases but the virus is expected to arrive within 2-4 weeks. No vaccine exists yet and development will take 12-18 months. Your team must design a preparedness plan that specifies exactly when and how to implement testing, quarantine, social distancing, healthcare surge capacity, and eventually vaccination — and justify every decision with model data.

GUIDING QUESTIONS:
• At what number of confirmed cases should your city implement social distancing measures, and what does your model predict about the cost of waiting one additional week?
• How does your model inform the testing capacity needed to detect and quarantine enough cases to push the effective R0 below 1?
• What does your model reveal about the relationship between healthcare surge capacity and mortality rate when the system is overwhelmed?

DESIGN THINKING:
• What is your intervention timeline and what model evidence supports each trigger point?

  _________________________________________________________

• How does your plan address equity — ensuring that quarantine compliance is feasible for low-income workers and that vaccination reaches underserved communities?

  _________________________________________________________

• What economic support mechanisms does your plan include to make social distancing financially sustainable?

  _________________________________________________________

• How would you adapt your plan if a more transmissible variant emerged midway through implementation?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Plan specifies quantitative intervention triggers derived from model data, addresses equity with concrete mechanisms, includes adaptive strategies for variant emergence, and justifies every decision with mathematical evidence from the pandemic model
• Proficient (3): Plan includes reasonable intervention timeline with some model evidence and addresses most equity and adaptability concerns
• Developing (2): Plan describes interventions but lacks specific triggers, timeline, or quantitative connection to model evidence
• Beginning (1): Plan is incomplete or does not connect intervention choices to pandemic dynamics model data

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-12/G12L3-L02/G12L3-L02-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-12/G12L3-L02/G12L3-L02-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-12/G12L3-L02/G12L3-L02-Student-Presentation.pptx] |
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