# Lesson: Predicting the Next Pandemic

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G09L3-L05 |
| **Grade** | 9th Grade — Level 3: Biotech |
| **Lesson Name** | Predicting the Next Pandemic |
| **Status** | Template |

---

## Platform

### Title
**Predicting the Next Pandemic — Predictive Modeling of Zoonotic Spillover and Pandemic Emergence**

### Overview
This lesson introduces students to predictive epidemiological modeling — the computational approach that can identify where and when the next pandemic is most likely to emerge. Biotech skill focus: Predictive modeling and optimization. COVID-19 demonstrated both the devastating consequences of failed pandemic prediction and the power of computational models to guide response. Students will build models that identify the conditions under which zoonotic spillover escalates to global catastrophe. Students investigate the driving question: COVID-19 killed millions. The next pandemic is already brewing in a bat cave, a wet market, or an industrial pig farm — can we predict where and when it will emerge? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of diverse 14-15 year old students in an advanced epidemiology command center, analyzing global outbreak maps and viral phylogenetic trees on multiple large screens, dramatic red and blue lighting suggesting urgency, world maps with outbreak hotspots illuminated]

### Grade
9th Grade — Level 3: Biotech

### NGSS Standard
**HS-LS2-6, HS-ETS1-4**: Evaluate claims, evidence, and reasoning that the complex interactions in ecosystems maintain relatively consistent numbers and types of organisms in stable conditions, but changing conditions may result in a new ecosystem; use a computer simulation to model the impact of proposed solutions to a complex real-world problem.

### Learning Objectives
- Build a predictive model for pandemic emergence that traces the pathway from wildlife-human contact through zoonotic spillover to global spread
- Analyze how wildlife contact rates, viral mutation, surveillance detection, and population connectivity interact to determine pandemic risk
- Predict which conditions are most likely to produce the next pandemic emergence event using multi-variable simulation
- Evaluate early warning surveillance systems and intervention strategies that could prevent the next pandemic before it starts

### Component List (Starting Model: 9 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Wildlife-Human Contact Rate | External | The frequency and intensity of interactions between humans and wild animal species that harbor novel viruses — increased by deforestation, bushmeat hunting, wildlife trade, and agricultural expansion into wild habitats |
| Viral Mutation Rate | Internal | The inherent rate at which the pathogen accumulates genetic changes during replication, some of which may enhance human infectivity, transmissibility, or immune evasion — determined by the virus's replication machinery |
| Zoonotic Spillover Probability | Internal | The calculated likelihood that a virus successfully jumps from animal to human during any given contact event — determined by viral compatibility with human cell receptors, dose of exposure, and individual immune status |
| Surveillance Detection Speed | External | The time between the first human infection and the moment public health authorities detect and identify the novel pathogen — faster detection enables earlier containment |
| Population Density | External | The concentration of people in the geographic area where spillover occurs, which determines how many potential secondary contacts an infected person has before detection |
| Travel Connectivity | External | The number and frequency of transportation links (flights, roads, shipping) connecting the spillover location to other population centers — determines how quickly a local outbreak becomes global |
| Immune Naivety | Internal | The proportion of the human population with zero pre-existing immunity to the novel pathogen — for truly novel zoonotic viruses, this is effectively 100%, enabling explosive epidemic growth |
| Healthcare Capacity | Internal | The ability of the local and national healthcare system to identify, isolate, treat, and contact-trace infected individuals — determines whether early cases are contained or amplified through nosocomial transmission |
| Intervention Speed | Internal | The time between outbreak detection and implementation of effective containment measures — quarantine, travel restrictions, vaccination campaigns, therapeutic deployment — the single most critical determinant of pandemic versus contained outbreak |

### Research for Lesson
- Zoonotic Spillover: Where Pandemics Begin — reference materials and textbook resources
- The Pandemic Prediction Problem — reference materials and textbook resources
- Surveillance: The Critical Intervention Window — reference materials and textbook resources
- Pandemic Risk Mapping: Predicting Hotspots — reference materials and textbook resources

---

## Step 1: LOCATE — Build Your System

### Text Editor

```
PREDICTING THE NEXT PANDEMIC

Predictive Modeling of Zoonotic Spillover and Pandemic Emergence.
COVID-19 killed millions. The next pandemic is already brewing in a bat cave, a wet market, or an industrial pig farm — can we predict where and when it will emerge?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Wildlife-Human Contact Rate" — the frequency and intensity of interactions between humans and wild animal species that harbor novel viruses — increased by deforestation
  ○ Click "Surveillance Detection Speed" — the time between the first human infection and the moment public health authorities detect and identify the novel pathogen — faster detection enables earlier containment
  ○ Click "Population Density" — the concentration of people in the geographic area where spillover occurs
  ○ Click "Travel Connectivity" — the number and frequency of transportation links (flights
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Viral Mutation Rate" — the inherent rate at which the pathogen accumulates genetic changes during replication
  ○ Click "Zoonotic Spillover Probability" — the calculated likelihood that a virus successfully jumps from animal to human during any given contact event — determined by viral compatibility with human cell receptors
  ○ Click "Immune Naivety" — the proportion of the human population with zero pre-existing immunity to the novel pathogen — for truly novel zoonotic viruses
  ○ Click "Healthcare Capacity" — the ability of the local and national healthcare system to identify
  ○ Click "Intervention Speed" — the time between outbreak detection and implementation of effective containment measures — quarantine

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
"COVID-19 killed millions. The next pandemic is already brewing in a bat cave, a wet market, or an industrial pig farm — can we predict where and when it will emerge?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Wildlife-Human Contact Rate' — that's external. The frequency and intensity of interactions between humans and wild animal species that harbor novel viruses — increased by deforestation.
Click on 'Viral Mutation Rate' — that's internal. The inherent rate at which the pathogen accumulates genetic changes during replication.
Click on 'Zoonotic Spillover Probability' — that's internal. The calculated likelihood that a virus successfully jumps from animal to human during any given contact event — determined by viral compatibility with human cell receptors.
Click on 'Surveillance Detection Speed' — that's external. The time between the first human infection and the moment public health authorities detect and identify the novel pathogen — faster detection enables earlier containment.
Click on 'Population Density' — that's external. The concentration of people in the geographic area where spillover occurs.
Click on 'Travel Connectivity' — that's external. The number and frequency of transportation links (flights.
Click on 'Immune Naivety' — that's internal. The proportion of the human population with zero pre-existing immunity to the novel pathogen — for truly novel zoonotic viruses.
Click on 'Healthcare Capacity' — that's internal. The ability of the local and national healthcare system to identify.
Click on 'Intervention Speed' — that's internal. The time between outbreak detection and implementation of effective containment measures — quarantine.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Wildlife-Human Contact Rate, Surveillance Detection Speed, Population Density, and Travel Connectivity are external components because they represent factors that can be influenced by policy decisions and infrastructure investments — governments can regulate deforestation, fund surveillance systems, manage urban planning, and implement travel screening. Viral Mutation Rate, Zoonotic Spillover Probability, Immune Naivety, Healthcare Capacity, and Intervention Speed are internal components — they are properties of the biological system or emergent responses that cannot be directly set but are influenced by the external conditions.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next step, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 9 components sorted: Wildlife-Human Contact Rate, Surveillance Detection Speed, Population Density, Travel Connectivity (External), Viral Mutation Rate, Zoonotic Spillover Probability, Immune Naivety, Healthcare Capacity, Intervention Speed (Internal)]

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
• Click on "Wildlife-Human Contact Rate" and drag an arrow to "Zoonotic Spillover Probability"
• Click on "Viral Mutation Rate" and drag an arrow to "Zoonotic Spillover Probability"
• Click on "Population Density" and drag an arrow to "Intervention Speed"
• Click on "Travel Connectivity" and drag an arrow to "Geographic Spread Rate"
• Click on "Surveillance Detection Speed" and drag an arrow to "Intervention Speed"

Task C: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Wildlife-Human Contact Rate → Zoonotic Spillover Probability = POSITIVE (+)
    More frequent contact between humans and wildlife creates more opportunities for cross-species viral transmission — each contact event is a probabilistic opportunity for spillover.

  ○ Viral Mutation Rate → Zoonotic Spillover Probability = POSITIVE (+)
    Higher viral mutation rate generates more genetic variants, increasing the probability that a human-compatible variant emerges that can infect human cells and achieve human-to-human transmission.

  ○ Population Density → Intervention Speed = NEGATIVE (−)
    Higher population density makes containment more difficult because infected individuals have more contacts before isolation, increasing the number of cases that must be traced and requiring more resources for intervention.

  ○ Travel Connectivity → Geographic Spread Rate = POSITIVE (+)
    More transportation links from the outbreak origin accelerate the geographic spread of the pathogen to new population centers, reducing the time window for containment.

  ○ Surveillance Detection Speed → Intervention Speed = POSITIVE (+)
    Faster surveillance detection enables faster intervention — you cannot contain what you haven't detected. Every day of detection delay exponentially increases the infected population that must be contained.

Task D: CHECK YOUR MODEL
• You should have 5 arrows total
• 1 negative relationship(s), 4 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: Wildlife-Human Contact Rate is increasing every year as deforestation pushes humans deeper into animal habitats. Each contact event has a small Zoonotic Spillover Probability that depends on Viral Mutation Rate producing a human-compatible variant. Once spillover occurs, the race begins: Surveillance Detection Speed versus Population Density and Travel Connectivity determine whether the world catches it early or learns about it after it's already everywhere. What combination of conditions turns a single sick person in a remote village into a global catastrophe?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Wildlife-Human Contact Rate' and drag an arrow
over to 'Zoonotic Spillover Probability.'

Here's the key question: When wildlife-human contact rate goes UP, does
zoonotic spillover probability go UP or DOWN?

More frequent contact between humans and wildlife creates more opportunities for cross-species viral transmission — each contact event is a probabilistic opportunity for spillover.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Viral Mutation Rate' and drag an arrow
over to 'Zoonotic Spillover Probability.'

Here's the key question: When viral mutation rate goes UP, does
zoonotic spillover probability go UP or DOWN?

Higher viral mutation rate generates more genetic variants, increasing the probability that a human-compatible variant emerges that can infect human cells and achieve human-to-human transmission.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'Population Density' and drag an arrow
over to 'Intervention Speed.'

Here's the key question: When population density goes UP, does
intervention speed go UP or DOWN?

Higher population density makes containment more difficult because infected individuals have more contacts before isolation, increasing the number of cases that must be traced and requiring more resources for intervention.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Travel Connectivity' and drag an arrow
over to 'Geographic Spread Rate.'

Here's the key question: When travel connectivity goes UP, does
geographic spread rate go UP or DOWN?

More transportation links from the outbreak origin accelerate the geographic spread of the pathogen to new population centers, reducing the time window for containment.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Final connection: Click on 'Surveillance Detection Speed' and drag an arrow
over to 'Intervention Speed.'

Here's the key question: When surveillance detection speed goes UP, does
intervention speed go UP or DOWN?

Faster surveillance detection enables faster intervention — you cannot contain what you haven't detected. Every day of detection delay exponentially increases the infected population that must be contained.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Look at your model now. You've got 1 negative and 4
positive relationships. 5 arrows total.

Wildlife-Human Contact Rate is increasing every year as deforestation pushes humans deeper into animal habitats. Each contact event has a small Zoonotic Spillover Probability that depends on Viral Mutation Rate producing a human-compatible variant. Once spillover occurs, the race begins: Surveillance Detection Speed versus Population Density and Travel Connectivity determine whether the world catches it early or learns about it after it's already everywhere. What combination of conditions turns a single sick person in a remote village into a global catastrophe?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Wildlife-Human Contact Rate +→ Zoonotic Spillover Probability, Viral Mutation Rate +→ Zoonotic Spillover Probability, Population Density −→ Intervention Speed, Travel Connectivity +→ Geographic Spread Rate, Surveillance Detection Speed +→ Intervention Speed]

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
• When Wildlife-Human Contact Rate is HIGH, what happens to the internal components?

Task C: SCENARIO — SLOW BURN
• Moderate contact, average mutation, moderate surveillance
• PREDICT FIRST: How many spillover events do you predict will occur before one leads to sustained human-to-human transmission?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task D: SCENARIO — COVID-19 ANALOG
• High contact, high density, high travel, slow detection
• PREDICT FIRST: What do you predict the infection curve looks like when surveillance is slow and travel connectivity is high?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task E: SCENARIO — EARLY WARNING OPTIMIZED
• Fast surveillance, moderate risk factors
• PREDICT FIRST: Do you predict that fast detection alone can prevent a pandemic, even if all other risk factors are elevated?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Zoonotic spillover events happen far more frequently than pandemics — most cross-species jumps lead to dead-end infections that don't transmit between humans, but each one is a roll of the evolutionary dice
• The critical window for containment is extremely narrow — once a novel virus achieves sustained human-to-human transmission in a connected population, pandemic spread is nearly inevitable with current infrastructure
• Surveillance detection speed is the single most impactful intervention point — the difference between detecting an outbreak in week 1 versus week 4 can mean the difference between 100 cases and 100,000 cases
• Pandemic risk is not random — it clusters in predictable geographic hotspots where high wildlife diversity, rapid deforestation, dense human populations, and limited healthcare infrastructure overlap

THE ANSWER: Pandemics are not random acts of nature — they emerge through a predictable sequence of events that can be modeled and potentially prevented. Wildlife-human contact creates opportunities for zoonotic spillover. Viral mutation generates variants capable of human infection. Population density and travel connectivity determine whether a local outbreak goes global. The model reveals that the most impactful intervention is surveillance — detecting novel outbreaks within days rather than weeks. COVID-19 demonstrated that a delay of just a few weeks in detection and response transformed a containable outbreak in one city into a global pandemic that killed millions. Predictive models can identify the geographic hotspots, seasonal windows, and viral lineages most likely to produce the next pandemic — enabling preemptive surveillance deployment rather than reactive response.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Slow Burn. Moderate contact, average mutation, moderate surveillance.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: COVID-19 Analog.
High contact, high density, high travel, slow detection.

Before you run it — make a prediction. What do you predict the infection curve looks like when surveillance is slow and travel connectivity is high?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Early Warning Optimized. Fast surveillance, moderate risk factors.
Do you predict that fast detection alone can prevent a pandemic, even if all other risk factors are elevated?

Here's what our model reveals: Pandemics are not random acts of nature — they emerge through a predictable sequence of events that can be modeled and potentially prevented. Wildlife-human contact creates opportunities for zoonotic spillover. Viral mutation generates variants capable of human infection. Population density and travel connectivity determine whether a local outbreak goes global. The model reveals that the most impactful intervention is surveillance — detecting novel outbreaks within days rather than weeks. COVID-19 demonstrated that a delay of just a few weeks in detection and response transformed a containable outbreak in one city into a global pandemic that killed millions. Predictive models can identify the geographic hotspots, seasonal windows, and viral lineages most likely to produce the next pandemic — enabling preemptive surveillance deployment rather than reactive response.

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

Your current model treats the Wildlife-Human Contact Rate → Zoonotic Spillover Probability relationship as
unconditional. However, this relationship is scientifically
contingent on Viral Mutation Rate being active. Without this condition,
the simulation produces inaccurate results: Wildlife-Human Contact Rate drives Zoonotic Spillover Probability
even when the prerequisite state is not met.

Task A: CONFIGURE THE CONNECTION CONDITION
   • Select the connection arrow: Wildlife-Human Contact Rate → Zoonotic Spillover Probability
   • Click "Conditions" in the connection toolbar
   • Set the regulator condition: IF Viral Mutation Rate is ON
   • Click "Save Conditions"

Task B: VALIDATE THE CONDITIONAL MODEL
   • Run the simulation with Viral Mutation Rate active and observe
     how Wildlife-Human Contact Rate's effect on Zoonotic Spillover Probability is now gated
   • Toggle Viral Mutation Rate ON/OFF while Wildlife-Human Contact Rate remains constant
   • Verify that Zoonotic Spillover Probability only responds to Wildlife-Human Contact Rate when the
     condition is satisfied

Task C: ADDITIONAL CONDITION
   • Select: Population Density → Intervention Speed
   • Set condition: IF Surveillance Detection Speed is ON
   • This ensures Population Density's effect on Intervention Speed
     is contingent on Surveillance Detection Speed being active

Task D: ADDITIONAL CONDITION
   • Select: Surveillance Detection Speed → Intervention Speed
   • Set condition: IF Population Density is OFF
   • This ensures Surveillance Detection Speed's effect on Intervention Speed
     is contingent on Population Density being inactive

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
   • What happens if you turn OFF Wildlife-Human Contact Rate?
   • What happens if you turn OFF Surveillance Detection Speed?
   • What happens if you turn OFF Population Density?
   • What happens if you turn OFF Travel Connectivity?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Seasonal Climate Patterns — Temperature and precipitation cycles that affect wildlife breeding, migration, and habitat overlap with human populations — creating predictable seasonal windows of elevated spillover risk
   • Viral Recombination Events — The exchange of genetic material between different viral strains co-infecting the same host cell, which can rapidly create novel viruses with pandemic potential — especially concerning in intermediate hosts like pigs
   • Global Supply Chain Disruption — The cascade of economic, food security, and social consequences that follow pandemic-related lockdowns and travel restrictions — the secondary disaster that amplifies the human toll beyond direct disease mortality

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • Zoonotic Spillover: Where Pandemics Begin — how does this connect to your model?
   • The Pandemic Prediction Problem — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your predictive model identify the conditions that distinguish a contained outbreak from a global pandemic?
   • Which intervention point in your model has the greatest leverage for preventing pandemics — why is surveillance speed so critical?
   • Why do you think pandemic risk is concentrated in specific geographic hotspots rather than distributed randomly?
   • How would adding Seasonal Climate Patterns change your model's ability to predict spillover timing?

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

Seasonal Climate Patterns. Temperature and precipitation cycles that affect wildlife breeding, migration, and habitat overlap with human populations — creating predictable seasonal windows of elevated spillover risk
How would you model that?

Viral Recombination Events. The exchange of genetic material between different viral strains co-infecting the same host cell, which can rapidly create novel viruses with pandemic potential — especially concerning in intermediate hosts like pigs
How would you model that?

Global Supply Chain Disruption. The cascade of economic, food security, and social consequences that follow pandemic-related lockdowns and travel restrictions — the secondary disaster that amplifies the human toll beyond direct disease mortality
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

Epidemiologists and Pandemic Preparedness Specialists design and operate disease surveillance systems. They work for the WHO, CDC, national health agencies, and organizations like PREDICT and the Global Virome Project, earning $70,000–$150,000/year. Computational Epidemiologists who build predictive outbreak models earn $90,000–$180,000/year.

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
Visual: Title slide with dramatic global pandemic risk map and COVID-19 timeline
Say: "COVID-19 was not a surprise to epidemiologists — they had been warning about exactly this scenario for decades. The virus, the location, even the timing were all predictable in hindsight. Today you're going to build the model that predicts the next one."
Do: Show a timeline of pandemic warnings that were ignored before COVID-19. Let students process the pattern.
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and pandemic science vocabulary
Say: "You're going to build a predictive model for pandemic emergence — the same type of computational tool that organizations like the WHO and CDC use to assess global health threats."
Do: Pre-teach zoonotic spillover and immune naivety. Show a simple animation of a virus jumping from bat to human to illustrate the spillover concept.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: The next pandemic is already brewing — can we predict where?
Say: "Somewhere in the world right now, a virus is mutating inside an animal. One day — maybe tomorrow, maybe in ten years — it will jump into a human. What determines whether that becomes a footnote or a catastrophe?"
Do: Think-pair-share: Students list conditions that would make a spillover event more likely to become a pandemic. Compile and categorize.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps with pandemic prediction context
Say: "We're building a predictive model — one that identifies WHERE pandemics are most likely to start and WHAT conditions enable their spread. This is proactive science."
Do: Preview LEVER steps. Distinguish between prediction (knowing the future) and preparedness (being ready for it). Both require models.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Nine component cards spanning ecology, virology, and public health
Say: "Four of these components are things governments can actually control — investments they can make RIGHT NOW to prevent the next pandemic. Which four? And which five are determined by nature?"
Do: Guide sorting of external versus internal components. Emphasize that the controllable variables represent policy decisions — funding surveillance, managing wildlife contact, regulating travel.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Causal chain from wildlife contact to global pandemic
Say: "Trace the pathway from a bat in a cave to a global pandemic. Every link in this chain is a potential intervention point — a place where we could break the chain if we were watching."
Do: Students map the full causal chain. Identify which connections represent the best intervention points (surveillance, containment) versus immutable factors (viral mutation rate).
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Pandemic probability dashboards and outbreak trajectory projections
Say: "Run these three scenarios and find the answer: Can we prevent the next pandemic if we invest in the right interventions — or are pandemics inevitable?"
Do: Students predict outcomes, then run all three scenarios. Compare pandemic probability across scenarios, focusing on how surveillance speed changes outcomes.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key predictive findings and surveillance evidence
Say: "Your model shows what epidemiologists have been saying for years: pandemics are predictable and preventable — but only if we invest in surveillance BEFORE the next one starts, not after."
Do: Connect model findings to COVID-19 timeline. Show how early detection could have changed the trajectory. Discuss why surveillance funding was cut before the pandemic.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Global pandemic early warning system design challenge
Say: "The WHO just hired your team. Design the surveillance system that detects the next pandemic virus within 72 hours of the first human case. This is the most important engineering challenge of our generation."
Do: Groups design early warning systems including data streams, detection algorithms, alert protocols, and deployment strategies for resource-limited settings. Present and evaluate.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: Predicting the Next Pandemic
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
This lesson introduces students to predictive epidemiological modeling — the computational approach that can identify where and when the next pandemic is most likely to emerge. Biotech skill focus: Predictive modeling and optimization. COVID-19 demonstrated both the devastating consequences of failed pandemic prediction and the power of computational models to guide response. Students will build models that identify the conditions under which zoonotic spillover escalates to global catastrophe.

NGSS ALIGNMENT:
HS-LS2-6, HS-ETS1-4: Evaluate claims, evidence, and reasoning that the complex interactions in ecosystems maintain relatively consistent numbers and types of organisms in stable conditions, but changing conditions may result in a new ecosystem; use a computer simulation to model the impact of proposed solutions to a complex real-world problem.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Using Mathematics and Computational Thinking
  Students use computational simulation to model the probabilistic chain of events from zoonotic spillover to pandemic emergence, varying parameters to predict outbreak trajectories.
• Disciplinary Core Idea: LS2.C Ecosystem Dynamics / ETS1.B Developing Possible Solutions
  Changing conditions in ecosystems affect organism interactions; engineering solutions to pandemic preparedness require modeling complex, multi-variable systems.
• Crosscutting Concept: Cause and Effect / Scale, Proportion, and Quantity
  Students trace the causal chain from local wildlife contact to global pandemic, analyzing how small changes in early-stage parameters produce vastly different outcomes at global scale.

PACING GUIDE:
• Step 1 (Locate): 8-10 minutes
• Step 2 (Establish): 8-10 minutes
• Step 3 (Visualize & Evaluate): 10-12 minutes
• Step 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Zoonotic Spillover, Viral Mutation Rate, Immune Naivety, Pandemic Preparedness
□ Prepare COVID-19 killed millions. The next pandemic is already brewing in a bat cave, a wet market, or an industrial pig farm — can we predict where and when it will emerge discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify nine components spanning ecological (Wildlife-Human Contact Rate), virological (Viral Mutation Rate, Zoonotic Spillover Probability), epidemiological (Population Density, Immune Naivety, Travel Connectivity), and public health (Surveillance Detection Speed, Healthcare Capacity, Intervention Speed) domains.
• Establish: Students determine that Wildlife-Human Contact Rate creates spillover opportunities, Viral Mutation Rate generates human-compatible variants, and the chain from Zoonotic Spillover Probability through Population Density and Travel Connectivity to global spread is modulated by Surveillance Detection Speed, Healthcare Capacity, and Intervention Speed.
• Visualize: Students build a predictive model connecting the spillover-to-pandemic pathway, visualizing how changes in surveillance and connectivity parameters shift the probability of pandemic emergence.
• Evaluate: Students run slow-burn, COVID-19-analog, and optimized-early-warning scenarios to identify the parameter combinations that produce pandemics versus contained outbreaks.
• Revise: Students add Seasonal Climate Patterns, Viral Recombination Events, or Global Supply Chain Disruption to explore more realistic and consequential pandemic dynamics.

BACKGROUND CONTENT:
• Zoonotic Spillover: Where Pandemics Begin:
  Approximately 75% of emerging infectious diseases are zoonotic — they originate in animals. HIV came from chimpanzees, Ebola from bats, SARS-CoV-1 from civets (originally bats), MERS from camels (originally bats), COVID-19 likely from bats (possibly through an intermediate host). The spillover process requires three conditions: contact (humans must encounter infected animals), compatibility (the virus must be able to infect human cells), and transmission (the virus must be able to spread between humans). Most zoonotic spillover events are dead ends — the virus infects one person and stops. But occasionally, mutation or recombination produces a variant that achieves sustained human-to-human transmission, and a pandemic is born. The PREDICT project identified over 1,000 novel viruses in wildlife, including 160+ coronaviruses, before it was defunded in 2019 — months before COVID-19 emerged.

• The Pandemic Prediction Problem:
  Pandemic emergence is a low-probability, high-consequence event that follows a multi-step stochastic process. Each step has its own probability: the chance of a spillover event during any given contact (~0.001-1%), the chance that the virus achieves human-to-human transmission (~0.1-10% of spillover events), the chance of sustained transmission before containment (~10-50% depending on response speed), and the chance of global spread (~50-90% once sustained transmission is established in a connected population). Predictive models don't forecast specific pandemic dates — they identify the conditions, locations, and viral families where the compound probability is highest. This is analogous to earthquake prediction: we can't say exactly when, but we can identify the fault lines.

• Surveillance: The Critical Intervention Window:
  The single most important determinant of pandemic prevention is surveillance speed — the time between the first human case and public health detection. COVID-19 circulated in Wuhan for an estimated 4-8 weeks before being identified and reported. By that time, the virus had infected thousands and spread to multiple countries through air travel. Models consistently show that detecting and responding to a novel pathogen within the first week of human cases — when the infected population is still small and geographically contained — can reduce pandemic probability by 90%+. Modern surveillance tools include wastewater genomic monitoring (detecting viral RNA in sewage before clinical cases are reported), syndromic surveillance (AI analysis of hospital admissions and symptom patterns), and metagenomic sequencing of clinical samples (identifying any pathogen, known or novel, directly from patient specimens).

• Pandemic Risk Mapping: Predicting Hotspots:
  The geographic distribution of pandemic risk is not random — it clusters in predictable hotspots. The highest-risk zones are tropical and subtropical regions with high wildlife biodiversity (especially bat species diversity), rapid deforestation and agricultural expansion (increasing wildlife-human contact), dense human populations near wildlife interfaces, live animal markets, intensive livestock farming (particularly pigs, which can serve as 'mixing vessels' for influenza reassortment), limited public health surveillance infrastructure, and high international travel connectivity. South and Southeast Asia, Central and West Africa, and parts of South America are consistently identified as the highest-risk regions. Predictive models integrate these risk factors into geographic risk maps that can guide targeted surveillance deployment.

COMMON MISCONCEPTIONS:
• "Pandemics are unpredictable 'acts of God'"
  Reality: Pandemics follow a predictable sequence: zoonotic spillover, adaptation to human transmission, spread through connected populations. The specific pathogen and exact timing are uncertain, but the geographic hotspots, risk factors, and transmission dynamics are well understood. Epidemiologists predicted a novel coronavirus pandemic from a bat reservoir in a densely populated Asian region years before COVID-19 — the surprise was not THAT it happened but that the world wasn't ready.
  Strategy: Timeline exercise: Show students the published pandemic predictions from 2015-2018 that described almost exactly what happened in 2020. Ask: Was this unpredictable, or was it unheeded?

• "COVID-19 was a once-in-a-century event"
  Reality: The frequency of pandemic-potential zoonotic spillover events is INCREASING, not decreasing. Deforestation is accelerating wildlife-human contact. Climate change is shifting animal ranges. Global travel connectivity is increasing. Industrial livestock farming creates massive pathogen amplification opportunities. The conditions that produced COVID-19 are more common today than they were in 2019, making the next pandemic more likely, not less.
  Strategy: Data point: Novel zoonotic virus discoveries have increased 4-fold since 1980. Ask: What's changed in the world since 1980 that would explain this trend?

• "We just need better drugs and vaccines to stop pandemics"
  Reality: Drugs and vaccines are response tools — they help AFTER a pandemic has started. By the time a vaccine is developed, tested, manufactured, and distributed (12-18 months minimum), millions may already be infected. The model shows that prevention through surveillance and early containment is orders of magnitude more effective and cheaper than response. The COVID-19 vaccine was the fastest ever developed, yet 5 million people died before it was widely available.
  Strategy: Compare costs: Global pandemic surveillance costs ~$4 billion/year. COVID-19 cost the global economy ~$16 TRILLION. Which investment makes more sense?

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
Big Question: COVID-19 killed millions. The next pandemic is already brewing in a bat cave, a wet market, or an industrial pig farm — can we predict where and when it will emerge?
Answer: Pandemics are not random acts of nature — they emerge through a predictable sequence of events that can be modeled and potentially prevented. Wildlife-human contact creates opportunities for zoonotic spillover. Viral mutation generates variants capable of human infection. Population density and travel connectivity determine whether a local outbreak goes global. The model reveals that the most impactful intervention is surveillance — detecting novel outbreaks within days rather than weeks. COVID-19 demonstrated that a delay of just a few weeks in detection and response transformed a containable outbreak in one city into a global pandemic that killed millions. Predictive models can identify the geographic hotspots, seasonal windows, and viral lineages most likely to produce the next pandemic — enabling preemptive surveillance deployment rather than reactive response.

Simulation Answers:
• COVID-19 Analog Scenario: With high Wildlife-Human Contact Rate, high Population Density, high Travel Connectivity, and slow Surveillance Detection Speed, the model predicts explosive pandemic emergence. Zoonotic Spillover Probability generates periodic successful jumps to humans, and once sustained transmission begins in a dense, connected population, global spread occurs within weeks. Immune Naivety near 100% means the entire population is susceptible. Healthcare Capacity is quickly overwhelmed. This closely mirrors the COVID-19 trajectory where weeks of undetected transmission in a high-density, internationally connected city enabled global spread before meaningful intervention.
• Early Warning Optimized Scenario: With maximized Surveillance Detection Speed but otherwise moderate risk conditions, the model shows that early detection dramatically changes outcomes. When a novel pathogen is identified within 3 days of the first human case, the infected population is still small enough for aggressive contact tracing and isolation to contain the outbreak. Healthcare Capacity is not overwhelmed because case numbers remain manageable. The critical insight is that surveillance speed has outsized impact — it's the highest-leverage intervention point in the pandemic pathway.

Reflection Exemplars:
• Q: Why is surveillance speed the most impactful intervention?
  A: The model reveals that epidemic growth is exponential — each infected person infects multiple others, who each infect multiple others. The infected population doubles on a timescale determined by the pathogen's generation time (2-7 days for most respiratory viruses). This means a 1-week detection delay doesn't just add one week of cases — it allows multiple doubling events. If the doubling time is 3 days, a 3-week delay means the infected population is 2^7 = 128 times larger than it would have been with immediate detection. Containment that would have required tracing 10 contacts now requires tracing 1,280.
• Q: Why do pandemics cluster in predictable hotspots?
  A: Pandemic risk is the product of multiple independent factors, all of which must align for a pandemic to emerge. Tropical forests have the highest bat diversity (and bats are the reservoir for most pandemic-potential viruses). Deforestation in these regions increases wildlife-human contact. Dense populations near these interfaces provide fuel for transmission. Limited healthcare infrastructure delays detection. International airports enable global spread. The hotspots are where ALL of these factors overlap simultaneously — South and Southeast Asia, Central and West Africa, and parts of South America.

STEM CHALLENGE GUIDANCE:
Title: Design a Global Pandemic Early Warning System
Mission: Design a surveillance network that detects zoonotic spillover events within 72 hours of the first human infection, anywhere on Earth.
Scenario: The World Health Organization has commissioned your team to design the next-generation pandemic early warning system. COVID-19 demonstrated that existing surveillance was too slow — the virus circulated for weeks or months before being identified. Your system must detect novel zoonotic viruses within 72 hours of the first human case, in any country, regardless of local healthcare infrastructure.
Introduction: Present the challenge: The World Health Organization has commissioned your team to design the next-generation Global Pandemic Early Warning System. COVID-19 proved that existing surveillance was inadequate. Your system must detect novel zoonotic pathogens within 72 hours of the first human case, anywhere on Earth, and trigger a rapid containment response.

Key Concepts:
• Wastewater Genomic Surveillance: Analyzing sewage for pathogen RNA provides population-level data without requiring individual testing. A single wastewater sample can detect a novel virus circulating in a community days before clinical cases are reported — it's the fastest passive surveillance technology available.
• Metagenomic Sequencing: Rather than testing for specific known pathogens, metagenomic sequencing analyzes ALL genetic material in a sample — identifying any virus, bacterium, or parasite present, including completely novel organisms. This is the only surveillance approach that can detect a pathogen that hasn't been discovered yet.
• Network Analysis for Outbreak Prediction: Pandemic models use airline flight data, mobile phone movement patterns, and trade networks to predict how a pathogen would spread from any given starting location. These network models can identify 'superspreader' locations — airports and transportation hubs that would amplify global spread.

Evaluation Rubric:
• Expert (4): System includes multiple complementary surveillance streams, AI-powered anomaly detection, rapid genomic sequencing capacity, international reporting protocols, and deployment strategy for low-resource settings, supported by model-derived evidence for design choices
• Proficient (3): System includes surveillance technology selection, detection protocol, and alert system with reasoning connected to model findings
• Developing (2): System covers basic surveillance concepts but lacks detail on detection technology or international coordination
• Beginning (1): System is incomplete or does not connect surveillance design to the pandemic prediction model

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a simplified spillover pathway diagram showing the steps from animal reservoir to global pandemic
  • Use an epidemic curve template where students can sketch predicted outbreak trajectories for different surveillance speed scenarios
  • Scaffold predictive thinking: 'The risk is highest when ___ AND ___ AND ___ because each factor multiplies the probability of ___.'

Extensions (Advanced Learners):
  • Research the Global Virome Project — the effort to identify every virus on Earth before the next pandemic — and evaluate its feasibility and impact potential
  • Investigate how climate change is expanding the geographic range of disease vectors (mosquitoes, ticks) and creating new pandemic risk zones
  • Compare the surveillance systems that detected SARS (2003, contained in 8 months) versus COVID-19 (2019, became a pandemic) and identify what was different

Cross-Curricular Connections:
  • Math: Calculate compound probabilities of spillover → transmission → pandemic using the model's parameter values, and determine how much each intervention reduces total pandemic probability
  • ELA: Write a policy brief to Congress arguing for increased pandemic preparedness funding, using model predictions and COVID-19 as evidence of the consequences of underfunding
  • Social Studies: Analyze how global inequality affects pandemic risk — why do most pandemics originate in regions with the least surveillance infrastructure, and what does this mean for global health equity?

CAST ALIGNMENT:
• Model the multi-step pathway from zoonotic spillover through sustained human transmission to global pandemic emergence
• Analyze how surveillance speed, population connectivity, and immune naivety interact to determine whether an outbreak becomes a pandemic
• Predict pandemic risk hotspots by identifying geographic regions where wildlife contact, population density, and limited surveillance overlap

CAST-Style Assessment Questions:
• Multiple Choice: A novel virus is detected in a remote village 4 weeks after the first case, compared to a scenario where it's detected in 3 days. Based on your model, how does this delay affect pandemic probability?
• Constructed Response: Using your predictive model, explain why deforestation in tropical regions increases pandemic risk. Trace the full causal chain from land-use change to potential pandemic emergence, referencing at least three model components.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: Predicting the Next Pandemic
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Where do you think new pandemic viruses come from — do they just appear, or is there a predictable process?

   _________________________________________________________

   _________________________________________________________

2. What do you think determines whether a new virus causes a local outbreak versus a global pandemic?

   _________________________________________________________

   _________________________________________________________

3. Draw a diagram showing the chain of events from a virus in a bat to a global pandemic — what steps have to occur?

   [DRAWING BOX]

4. What would an ideal pandemic early warning system look like, and why don't we have one?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Zoonotic Spillover            
___ Viral Mutation Rate           
___ Immune Naivety                
___ Pandemic Preparedness         

A. The event where a pathogen jumps from an animal host species to a human — the critical first step in pandemic emergence that occurs when humans come into contact with infected wildlife through hunting, farming, habitat destruction, or live animal markets
B. The frequency at which random errors occur during viral genome replication — RNA viruses like influenza and coronaviruses have high mutation rates that generate genetic variation, some of which may enable human infection or human-to-human transmission
C. The absence of pre-existing immunity in a human population to a novel pathogen — when a virus jumps from animals to humans, the entire human population is immunologically naive, allowing explosive spread because no one has protective antibodies
D. The systems, infrastructure, and protocols designed to detect, contain, and respond to emerging infectious diseases before they spread globally — including surveillance networks, stockpiled countermeasures, and international coordination agreements

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

SCENARIO: Slow Burn
Settings: Moderate contact, average mutation, moderate surveillance
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: COVID-19 Analog
Settings: High contact, high density, high travel, slow detection
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Early Warning Optimized
Settings: Fast surveillance, moderate risk factors
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

1. How does your predictive model identify the conditions that distinguish a contained outbreak from a global pandemic?

   _________________________________________________________

   _________________________________________________________

2. Which intervention point in your model has the greatest leverage for preventing pandemics — why is surveillance speed so critical?

   _________________________________________________________

   _________________________________________________________

3. Why do you think pandemic risk is concentrated in specific geographic hotspots rather than distributed randomly?

   _________________________________________________________

   _________________________________________________________

4. How would adding Seasonal Climate Patterns change your model's ability to predict spillover timing?

   _________________________________________________________

   _________________________________________________________

5. What are the ethical implications of predictive pandemic models — should governments restrict wildlife contact in areas your model identifies as high-risk?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. COVID-19 killed millions. The next pandemic is already brewing in a bat cave, a wet market, or an industrial pig farm — can we predict where and when it will emerge? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Using Mathematics and Computational Thinking
   □ Disciplinary Core Idea: LS2.C Ecosystem Dynamics / ETS1.B Developing Possible Solutions
   □ Crosscutting Concept: Cause and Effect / Scale, Proportion, and Quantity

3. What are the ethical implications of predictive pandemic models — should governments restrict wildlife contact in areas your model identifies as high-risk?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Global Pandemic Early Warning System
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design a surveillance network that detects zoonotic spillover events within 72 hours of the first human infection, anywhere on Earth.

SCENARIO: The World Health Organization has commissioned your team to design the next-generation pandemic early warning system. COVID-19 demonstrated that existing surveillance was too slow — the virus circulated for weeks or months before being identified. Your system must detect novel zoonotic viruses within 72 hours of the first human case, in any country, regardless of local healthcare infrastructure.

GUIDING QUESTIONS:
• What data streams would your surveillance system monitor — clinical data, wastewater, wildlife sampling, or something else?
• How would you detect a novel pathogen before it's even been identified and named?
• What triggers would cause your system to escalate from 'signal detected' to 'global alert'?

DESIGN THINKING:
• How would you deploy surveillance in remote areas with limited healthcare infrastructure?

  _________________________________________________________

• What role would artificial intelligence play in detecting outbreak signals in noisy real-world data?

  _________________________________________________________

• How would you overcome the political barriers to rapid international outbreak reporting?

  _________________________________________________________

• What genomic sequencing capacity would your system need, and where would you locate it?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): System includes multiple complementary surveillance streams, AI-powered anomaly detection, rapid genomic sequencing capacity, international reporting protocols, and deployment strategy for low-resource settings, supported by model-derived evidence for design choices
• Proficient (3): System includes surveillance technology selection, detection protocol, and alert system with reasoning connected to model findings
• Developing (2): System covers basic surveillance concepts but lacks detail on detection technology or international coordination
• Beginning (1): System is incomplete or does not connect surveillance design to the pandemic prediction model

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CAST-Aligned Pre/Post Assessment

### Administration Instructions

These 5 multiple-choice questions are administered identically as both a pre-assessment (before Activity 1) and a post-assessment (after Activity 4). Score each out of 5. Learning growth = post-score minus pre-score.

Questions follow the California Science Test (CAST) stimulus-response format. Each item is three-dimensional, assessing a Science and Engineering Practice (SEP), Disciplinary Core Idea (DCI), and Crosscutting Concept (CCC) simultaneously, aligned to HS-LS2-6, HS-ETS1-4.

---

### Question 1

CAST Alignment: SEP 2.1.1 (Determine components of a system) + DCI LS2.6 + CCC4 (Systems and System Models)

A student is using the ModelIt platform to study the system in this lesson. The model includes these components: Wildlife-Human Contact Rate, Viral Mutation Rate, Zoonotic Spillover Probability, Surveillance Detection Speed, Population Density, Travel Connectivity, Immune Naivety, Healthcare Capacity, Intervention Speed. Some components are external (Wildlife-Human Contact Rate, Surveillance Detection Speed, Population Density, Travel Connectivity) and some are internal (Viral Mutation Rate, Zoonotic Spillover Probability, Immune Naivety, Healthcare Capacity, Intervention Speed). The student needs to understand what each component represents and how they are organized.

A pandemic prediction model shows that reducing Surveillance Detection Speed from 28 days to 7 days decreases total predicted infections by 95%. Which systems-level principle explains why this relatively modest intervention has such a disproportionately large effect?

A. The 95% reduction is coincidental and does not reflect a causal relationship
B. Earlier detection allows containment during the exponential growth phase when case numbers are still small enough to trace and isolate
C. Faster detection automatically cures infected patients
D. Surveillance somehow reduces the mutation rate of the virus

Correct Answer: B

Feedback: Correct. During exponential growth, case counts double at regular intervals. At 7 days, there may be dozens of cases that can be individually traced and isolated. By 28 days, those dozens have become thousands or millions, making containment impossible. Early intervention operates during the period when each individual case still matters. If you chose C, look at the evidence from the model. The correct answer (A) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, look at the evidence from the model. The correct answer (A) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose A, the model shows these components ARE connected. When one changes, it affects the others through the relationships (positive or negative) that you mapped in the model.
---

### Question 2

CAST Alignment: SEP 2.1.2 (Determine relationships among components) + DCI LS2.6 + CCC4 (Systems and System Models)

In the computational model for this lesson, a student draws arrows between components to show relationships. The model shows that when Human Contact Rate increases, Zoonotic Spillover Probability increases; when Viral Mutation Rate increases, Zoonotic Spillover Probability increases. The student is trying to understand why these relationships are positive or negative.

A student's model identifies a geographic region as a 'pandemic hotspot' based on four overlapping risk factors. Which combination of factors represents the MOST scientifically valid set of hotspot indicators?

A. Cold climate, low population density, advanced hospitals, and strict border controls
B. High altitude, oceanic climate, rural population, and abundant wildlife veterinarians
C. Urban development, low wildlife diversity, high vaccination rates, and minimal travel
D. High wildlife diversity, rapid deforestation, dense human population, and limited healthcare infrastructure

Correct Answer: D

Feedback: Correct. Pandemic hotspots occur where high wildlife diversity (more potential reservoir species) overlaps with rapid deforestation (increasing human-wildlife contact), dense human populations (enabling human-to-human transmission), and limited healthcare (delayed detection and response). These factors collectively maximize spillover probability and minimize containment capacity. If you chose A, look at whether this is an external component (we can't control it) or an internal component (it changes based on other things in the system). The model makes this distinction clear. If you chose B, look at the evidence from the model. The correct answer (A) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose C, look at the evidence from the model. The correct answer (A) is supported by the relationships between components. This answer does not match what the simulation data shows.
---

### Question 3

CAST Alignment: SEP 2.1.3 (Evaluate a model's accuracy) + DCI LS2.6 + CCC4 (Systems and System Models)

A student runs a simulation of the model. The model shows that when Human Contact Rate increases, Zoonotic Spillover Probability increases and when Viral Mutation Rate increases, Zoonotic Spillover Probability increases and when Population Density increases, Intervention Speed decreases. The student changes one variable to see how the whole system responds.

A model simulation shows that a virus with a Viral Mutation Rate 10x higher than average produces successful zoonotic spillover events 3x more frequently. However, only 1 in 50 spillover events leads to sustained human-to-human transmission. What does this reveal about pandemic emergence?

A. Spillover events are necessary but not sufficient for pandemic emergence; the virus must also acquire mutations enabling efficient human-to-human transmission, which is a rare additional evolutionary step
B. If spillover occurs 50 times, a pandemic is guaranteed
C. Mutation rate has no relationship to pandemic risk
D. Most pandemics are caused by viruses with low mutation rates

Correct Answer: A

Feedback: Correct. Spillover is the first barrier, but sustained human-to-human transmission requires additional adaptations (receptor binding optimization, airborne transmission capability, immune evasion). Most spillover events are evolutionary dead ends. Pandemic emergence requires crossing multiple biological barriers, each with its own probability. If you chose D, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose C, the model shows these components ARE connected. When one changes, it affects the others through the relationships (positive or negative) that you mapped in the model. If you chose B, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows.
---

### Question 4

CAST Alignment: SEP 2.1.4 (Represent mechanisms to explain/predict events) + DCI LS2.6 + CCC4 (Systems and System Models)

Scientists are studying data related to this system. They collected observations over time and noticed patterns in how the components change. The data shows how changes in one part of the system cascade through the other parts.

A student compares two intervention strategies in the pandemic model: (1) reducing Wildlife-Human Contact Rate by 50% and (2) improving Surveillance Detection Speed by 50%. The model shows Strategy 2 prevents more pandemics. Which analysis BEST explains this result?

A. Surveillance is always cheaper than habitat protection
B. Reducing contact is irrelevant to pandemic prevention
C. Contact reduction prevents spillover events but has diminishing returns because some level of human-wildlife interaction is unavoidable; surveillance improvement is effective against ALL spillover events regardless of how they occur
D. Contact reduction increases mutation rate, which cancels out the benefit

Correct Answer: C

Feedback: Correct. Reducing contact rate decreases the frequency of spillover opportunities but cannot eliminate them entirely because human-wildlife interaction is unavoidable in agriculture, conservation, and daily life. Improved surveillance operates downstream, catching and containing spillover events regardless of their source, making it a more robust intervention point. If you chose B, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose A, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, this answer suggests something is being added to the system. Look carefully at the model — the total amount stays the same even when components change. The system is conserving matter or energy.
---

### Question 5

CAST Alignment: SEP 2.1.5 (Apply a model to make predictions) + DCI LS2.6 + CCC4 (Systems and System Models)

A team wants to use the model to solve a real-world problem related to this system. They know they cannot control the external components (Wildlife-Human Contact Rate, Surveillance Detection Speed, Population Density, Travel Connectivity), but they can take action on internal components (Viral Mutation Rate, Zoonotic Spillover Probability, Immune Naivety, Healthcare Capacity, Intervention Speed). They need to decide which action would be most effective based on what the model shows.

A pandemic prediction model shows that two scenarios with identical Zoonotic Spillover Probability produce vastly different outcomes: Scenario A results in 50 total cases while Scenario B results in 5 million cases. Which pair of variable differences MOST PLAUSIBLY explains the divergent outcomes?

A. Scenario B involved a different animal reservoir species
B. Scenario B had higher Viral Mutation Rate and lower Immune Naivety
C. Scenario B occurred in a warmer climate with more rainfall
D. Scenario B had higher Population Density and Travel Connectivity combined with slower Surveillance Detection Speed

Correct Answer: D

Feedback: Correct. Once spillover occurs, the trajectory depends on spread and detection variables. High Population Density provides more potential contacts, Travel Connectivity exports cases to other regions before containment, and slow Surveillance delays the response. Together, these variables determine whether a spillover becomes a contained cluster or a global pandemic. If you chose B, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose C, this answer suggests something is being added to the system. Look carefully at the model — the total amount stays the same even when components change. The system is conserving matter or energy. If you chose A, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows.
---

### Answer Key

Question 1: B (Cognitive Level: Identify — SEP 2.1.1, DCI LS2.6, CCC4)
Question 2: D (Cognitive Level: Reason — SEP 2.1.2, DCI LS2.6, CCC4)
Question 3: A (Cognitive Level: Reason — SEP 2.1.3, DCI LS2.6, CCC4)
Question 4: C (Cognitive Level: Reason + Evidence — SEP 2.1.4, DCI LS2.6, CCC4)
Question 5: D (Cognitive Level: Predict + Apply — SEP 2.1.5, DCI LS2.6, CCC4)


## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-09/G09L3-L05/G09L3-L05-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-09/G09L3-L05/G09L3-L05-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-09/G09L3-L05/G09L3-L05-Student-Presentation.pptx] |
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