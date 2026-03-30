# Lesson: How Does Your Immune System Learn?

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G11L1-L04 |
| **Grade** | 11th Grade — Level 1: Foundations of Complex Systems |
| **Lesson Name** | How Does Your Immune System Learn? |
| **Status** | Template |

---

## Platform

### Title
**How Does Your Immune System Learn? — Modeling Vaccine Mechanisms and Herd Immunity Thresholds**

### Overview
The development of vaccines is arguably the greatest achievement in the history of medicine — vaccines have saved an estimated 154 million lives over the past 50 years. Yet many people fundamentally misunderstand how vaccines work, confusing antibody levels with protection and individual immunity with population immunity. A deep understanding of the adaptive immune system and herd immunity dynamics is essential for making informed personal and public health decisions. Students investigate the driving question: How does your immune system 'remember' a disease it has never had — and at what point does vaccinating enough people protect everyone, even those who can't be vaccinated? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image showing an extreme close-up of a medical syringe with vaccine alongside a magnified view of antibodies attacking a virus, dramatic lighting with blue and white tones, sharp detail, scientific editorial quality]

### Grade
11th Grade — Level 1: Foundations of Complex Systems

### NGSS Standard
**HS-LS1-2, HS-LS1-4**: Develop and use a model to illustrate the hierarchical organization of interacting systems that provide specific functions within multicellular organisms. Use a model to illustrate the role of cellular division (mitosis) in producing and maintaining complex organisms.

### Learning Objectives
- Model how vaccines trigger the adaptive immune system to produce memory B cells and memory T cells without causing disease
- Explain the relationship between antigen exposure, antibody production, and immunological memory
- Predict the herd immunity threshold for diseases with different transmission rates (R0 values)
- Analyze how vaccination coverage affects disease spread through a population, including protection of immunocompromised individuals

### Component List (Starting Model: 6 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Vaccination Rate | External | The percentage of the population that receives the vaccine, determined by public health policy, access, and individual decisions — the primary controllable factor in achieving herd immunity |
| Antigen Exposure | External | The introduction of weakened, inactivated, or molecular components of a pathogen via vaccination that triggers the immune response without causing disease — different vaccine types provide different levels and durations of exposure |
| Antibody Production | Internal | The quantity and specificity of antibodies produced by B cells in response to vaccine antigen — antibody levels peak 2-4 weeks after vaccination and then decline, but memory cells persist |
| Memory Cell Population | Internal | The number of long-lived memory B cells and memory T cells that persist after the initial immune response, ready to mount a rapid defense upon future exposure to the real pathogen |
| Herd Immunity Level | Internal | The effective immunity of the population as a whole — when enough individuals are immune, transmission chains break and even unvaccinated people are indirectly protected |
| Disease Transmission Rate | Internal | The rate at which the pathogen spreads through the remaining susceptible population, determined by R0 and the proportion of people who are immune |

### Research for Lesson
- The Adaptive Immune System: Learning Through Molecular Recognition — reference materials and textbook resources
- How Vaccines Create Memory Without Disease — reference materials and textbook resources
- Memory Cells: The Permanent Guard — reference materials and textbook resources
- Herd Immunity: Individual Decisions, Collective Consequences — reference materials and textbook resources

---

## Step 1: LOCATE — Build Your System

### Text Editor

```
HOW DOES YOUR IMMUNE SYSTEM LEARN?

Modeling Vaccine Mechanisms and Herd Immunity Thresholds.
How does your immune system 'remember' a disease it has never had — and at what point does vaccinating enough people protect everyone, even those who can't be vaccinated?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Vaccination Rate" — the percentage of the population that receives the vaccine
  ○ Click "Antigen Exposure" — the introduction of weakened
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Antibody Production" — the quantity and specificity of antibodies produced by b cells in response to vaccine antigen — antibody levels peak 2-4 weeks after vaccination and then decline
  ○ Click "Memory Cell Population" — the number of long-lived memory b cells and memory t cells that persist after the initial immune response
  ○ Click "Herd Immunity Level" — the effective immunity of the population as a whole — when enough individuals are immune
  ○ Click "Disease Transmission Rate" — the rate at which the pathogen spreads through the remaining susceptible population

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
"How does your immune system 'remember' a disease it has never had — and at what point does vaccinating enough people protect everyone, even those who can't be vaccinated?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Vaccination Rate' — that's external. The percentage of the population that receives the vaccine.
Click on 'Antigen Exposure' — that's external. The introduction of weakened.
Click on 'Antibody Production' — that's internal. The quantity and specificity of antibodies produced by B cells in response to vaccine antigen — antibody levels peak 2-4 weeks after vaccination and then decline.
Click on 'Memory Cell Population' — that's internal. The number of long-lived memory B cells and memory T cells that persist after the initial immune response.
Click on 'Herd Immunity Level' — that's internal. The effective immunity of the population as a whole — when enough individuals are immune.
Click on 'Disease Transmission Rate' — that's internal. The rate at which the pathogen spreads through the remaining susceptible population.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Vaccination Rate and Antigen Exposure are external components because they represent human choices — public health officials set vaccination policies, and vaccine developers design the antigen delivery system. Antibody Production, Memory Cell Population, Herd Immunity Level, and Disease Transmission Rate are internal because they are biological and epidemiological outcomes that emerge from the interaction of vaccine-stimulated immune responses across a population — they cannot be set directly but are determined by the immune system's response and population dynamics.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next step, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 6 components sorted: Vaccination Rate, Antigen Exposure (External), Antibody Production, Memory Cell Population, Herd Immunity Level, Disease Transmission Rate (Internal)]

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
• Click on "Antigen Exposure" and drag an arrow to "Antibody Production"
• Click on "Antibody Production" and drag an arrow to "Memory Cell Population"
• Click on "Vaccination Rate" and drag an arrow to "Herd Immunity Level"

Task C: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Antigen Exposure → Antibody Production = POSITIVE (+)
    Vaccine antigens activate B cells with matching receptors, triggering clonal expansion and differentiation into antibody-secreting plasma cells. More effective antigen presentation (through adjuvants or optimal vaccine design) produces a stronger initial antibody response.

  ○ Antibody Production → Memory Cell Population = POSITIVE (+)
    During the immune response, a fraction of activated B cells and T cells differentiate into long-lived memory cells rather than short-lived effector cells. A stronger initial immune response (more antibody production) generally produces a larger and more diverse memory cell population.

  ○ Vaccination Rate → Herd Immunity Level = POSITIVE (+)
    As vaccination rate increases, herd immunity builds gradually but the protective effect is nonlinear — disease transmission drops sharply when coverage crosses the herd immunity threshold (1 - 1/R0). Below the threshold, outbreaks can still occur; above it, transmission chains break.

Task D: CHECK YOUR MODEL
• You should have 3 arrows total
• 0 negative relationship(s), 3 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: If Vaccination Rate is below the herd immunity threshold, pockets of susceptible people remain connected in the population, allowing transmission chains to continue. Once Vaccination Rate crosses the threshold, those chains break — even unvaccinated people become protected. What determines where that threshold is?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Antigen Exposure' and drag an arrow
over to 'Antibody Production.'

Here's the key question: When antigen exposure goes UP, does
antibody production go UP or DOWN?

Vaccine antigens activate B cells with matching receptors, triggering clonal expansion and differentiation into antibody-secreting plasma cells. More effective antigen presentation (through adjuvants or optimal vaccine design) produces a stronger initial antibody response.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Antibody Production' and drag an arrow
over to 'Memory Cell Population.'

Here's the key question: When antibody production goes UP, does
memory cell population go UP or DOWN?

During the immune response, a fraction of activated B cells and T cells differentiate into long-lived memory cells rather than short-lived effector cells. A stronger initial immune response (more antibody production) generally produces a larger and more diverse memory cell population.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'Vaccination Rate' and drag an arrow
over to 'Herd Immunity Level.'

Here's the key question: When vaccination rate goes UP, does
herd immunity level go UP or DOWN?

As vaccination rate increases, herd immunity builds gradually but the protective effect is nonlinear — disease transmission drops sharply when coverage crosses the herd immunity threshold (1 - 1/R0). Below the threshold, outbreaks can still occur; above it, transmission chains break.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Look at your model now. You've got 0 negative and 3
positive relationships. 3 arrows total.

If Vaccination Rate is below the herd immunity threshold, pockets of susceptible people remain connected in the population, allowing transmission chains to continue. Once Vaccination Rate crosses the threshold, those chains break — even unvaccinated people become protected. What determines where that threshold is?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Antigen Exposure +→ Antibody Production, Antibody Production +→ Memory Cell Population, Vaccination Rate +→ Herd Immunity Level]

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
• When Vaccination Rate is HIGH, what happens to the internal components?

Task C: SCENARIO — INDIVIDUAL IMMUNE RESPONSE
• Single vaccination dose | 30-day antibody tracking + 6-month memory tracking
• PREDICT FIRST: After vaccination, do you predict antibody levels will remain permanently high or decline after the initial response? If they decline, what protects you when you encounter the real pathogen years later?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task D: SCENARIO — HERD IMMUNITY BUILDUP
• Vaccination rate: 0% to 95% | Disease R0 = 5
• PREDICT FIRST: At what vaccination percentage do you predict disease transmission will effectively stop? Is it a gradual slowdown or a sharp threshold effect?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task E: SCENARIO — OUTBREAK IN UNDER-VACCINATED POPULATION
• Vaccination rate: 80% | Disease requiring 93% immunity (measles)
• PREDICT FIRST: If a community is 80% vaccinated against measles but the threshold is 93%, do you predict outbreaks will affect only unvaccinated individuals or also some vaccinated ones? Why?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Vaccines work by training the immune system to recognize a pathogen's antigens WITHOUT causing disease — the adaptive immune system produces the same memory cells it would during a real infection, but without the danger
• Antibody levels decline after vaccination, but long-lived memory B cells and memory T cells persist for years or decades, ready to mount a rapid secondary response that is 10-100 times faster than the primary response
• Herd immunity is a threshold effect, not a gradual process — below the threshold, outbreaks can still occur; above it, transmission chains break and the disease cannot sustain spread through the population
• People who cannot be vaccinated (infants, immunocompromised patients, organ transplant recipients) depend entirely on herd immunity for protection — when vaccination rates drop below the threshold, these vulnerable individuals are the first to be harmed

THE ANSWER: Your immune system learns through a remarkable process of molecular pattern recognition. When a vaccine introduces harmless fragments of a pathogen (antigens), your B cells and T cells that happen to recognize those specific molecular shapes are activated, multiply, and produce targeted antibodies. Most of these immune cells die off after the threat is cleared, but a critical population of memory B cells and memory T cells survive for years or decades. When the real pathogen arrives, these memory cells recognize it instantly and mount a massive, rapid response — producing antibodies in hours instead of the weeks the first response took. At the population level, when enough people are immune (the herd immunity threshold), the pathogen cannot find enough susceptible hosts to sustain transmission, and even unvaccinated individuals are protected. This threshold depends on how contagious the disease is: measles needs 93% immunity, while less contagious diseases need less.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Individual Immune Response. Single vaccination dose | 30-day antibody tracking + 6-month memory tracking.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Herd Immunity Buildup.
Vaccination rate: 0% to 95% | Disease R0 = 5.

Before you run it — make a prediction. At what vaccination percentage do you predict disease transmission will effectively stop? Is it a gradual slowdown or a sharp threshold effect?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Outbreak in Under-Vaccinated Population. Vaccination rate: 80% | Disease requiring 93% immunity (measles).
If a community is 80% vaccinated against measles but the threshold is 93%, do you predict outbreaks will affect only unvaccinated individuals or also some vaccinated ones? Why?

Here's what our model reveals: Your immune system learns through a remarkable process of molecular pattern recognition. When a vaccine introduces harmless fragments of a pathogen (antigens), your B cells and T cells that happen to recognize those specific molecular shapes are activated, multiply, and produce targeted antibodies. Most of these immune cells die off after the threat is cleared, but a critical population of memory B cells and memory T cells survive for years or decades. When the real pathogen arrives, these memory cells recognize it instantly and mount a massive, rapid response — producing antibodies in hours instead of the weeks the first response took. At the population level, when enough people are immune (the herd immunity threshold), the pathogen cannot find enough susceptible hosts to sustain transmission, and even unvaccinated individuals are protected. This threshold depends on how contagious the disease is: measles needs 93% immunity, while less contagious diseases need less.

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
   • What happens if you turn OFF Vaccination Rate?
   • What happens if you turn OFF Antigen Exposure?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Vaccine Efficacy Rate — The percentage of vaccinated individuals who develop full protective immunity — no vaccine is 100% effective; measles vaccine is 97%, flu vaccine ranges from 40-60%, COVID vaccines were 90-95% initially but declined against new variants
   • Variant Evolution — The tendency of pathogens to mutate, potentially producing variants that partially or fully escape vaccine-induced immunity — high transmission rates provide more opportunities for mutation, creating an evolutionary race between vaccination and viral adaptation
   • Vaccine Hesitancy — The spectrum of attitudes from full acceptance to full refusal of vaccination, influenced by trust in institutions, misinformation, historical medical abuse, and perceived risk-benefit calculations — hesitancy creates pockets of susceptibility that can sustain outbreaks

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • The Adaptive Immune System: Learning Through Molecular Recognition — how does this connect to your model?
   • How Vaccines Create Memory Without Disease — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model illustrate the difference between individual immunity and population-level herd immunity?
   • Why is the herd immunity threshold a sharp transition rather than a gradual improvement — what does this tell you about how diseases spread?
   • How does your model demonstrate that people who cannot be vaccinated are directly harmed when vaccination rates drop below the herd immunity threshold?
   • What role does R0 play in determining how difficult a disease is to control through vaccination?

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

Vaccine Efficacy Rate. The percentage of vaccinated individuals who develop full protective immunity — no vaccine is 100% effective; measles vaccine is 97%, flu vaccine ranges from 40-60%, COVID vaccines were 90-95% initially but declined against new variants
How would you model that?

Variant Evolution. The tendency of pathogens to mutate, potentially producing variants that partially or fully escape vaccine-induced immunity — high transmission rates provide more opportunities for mutation, creating an evolutionary race between vaccination and viral adaptation
How would you model that?

Vaccine Hesitancy. The spectrum of attitudes from full acceptance to full refusal of vaccination, influenced by trust in institutions, misinformation, historical medical abuse, and perceived risk-benefit calculations — hesitancy creates pockets of susceptibility that can sustain outbreaks
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

Epidemiologists study how diseases spread through populations, designing vaccination strategies and outbreak response plans at the CDC, WHO, state health departments, and pharmaceutical companies, earning $75,000–$140,000/year. Immunologists research the molecular mechanisms of immune memory and vaccine development at universities, NIH, and biotech firms, earning $80,000–$160,000/year.

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
Visual: Title slide with vaccine vial and immune cell imagery
Say: "You got vaccinated as a baby for diseases you've never had. You've never had measles, polio, or diphtheria. How does your body know how to fight something it's never encountered?"
Do: Ask students to name vaccines they've received. Then ask: How does a shot you got at 2 months old still protect you at 17? Collect hypotheses.
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and vocabulary terms
Say: "Today we're modeling two connected systems: how your individual immune system builds memory, and how a vaccinated population creates collective protection."
Do: Have students read objectives. Pre-teach 'memory B cell' and 'herd immunity threshold' with visual diagrams.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: Individual protection vs. community protection
Say: "Here's what most people get wrong about vaccines: they're not just about you. Your vaccination protects people around you who CAN'T be vaccinated — babies, cancer patients, organ recipients. At what point does YOUR decision become THEIR fate?"
Do: Quick-write: Students describe who they think is most affected when vaccination rates drop. Share out.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps overview with two-scale model preview
Say: "We're building a model that works at two scales — the molecular battle inside one person's body, and the epidemic math of an entire population."
Do: Preview LEVER steps. Emphasize the shift from individual cells to population dynamics.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Component cards for immunity model
Say: "What are the key players in this system? Some are choices we make, others are biological processes we can't directly control."
Do: Guide sorting: Vaccination Rate and Antigen Exposure are external. Antibody Production, Memory Cells, Herd Immunity, and Transmission Rate are internal biological/epidemiological outcomes.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows between components at both scales
Say: "Follow the chain: vaccine delivers antigen, antigen activates B cells, B cells make antibodies AND memory cells, memory cells provide long-term protection. Now zoom out: enough protected individuals create herd immunity that blocks transmission."
Do: Students map connections at both scales. Key insight: individual immunity aggregates into population protection through a threshold effect.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Simulation of immune response and herd immunity buildup
Say: "First, let's watch one person's immune system learn. Then let's vaccinate a population and find the exact moment where disease transmission stops."
Do: Run individual immune response simulation showing antibody peak and memory cell persistence. Then run herd immunity buildup, watching the sharp threshold transition.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key findings — memory cell longevity and herd immunity threshold
Say: "Your immune system is the most sophisticated learning machine on the planet. And when enough people's immune systems learn the same lesson, the whole community is protected — even those who can't learn it themselves."
Do: Calculate herd immunity thresholds for different diseases. Discuss: What happens to a baby in a NICU when vaccination rates drop below 93% for measles?
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Pandemic vaccination strategy design
Say: "A new virus just emerged. R0 is 4.5. You have limited vaccine supply and 6 months to reach herd immunity. Who gets vaccinated first, and can you prove your plan works?"
Do: Groups design vaccination rollout strategies with prioritization schedules, coverage targets, and model-based timeline predictions. Present and defend plans.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: How Does Your Immune System Learn?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
The development of vaccines is arguably the greatest achievement in the history of medicine — vaccines have saved an estimated 154 million lives over the past 50 years. Yet many people fundamentally misunderstand how vaccines work, confusing antibody levels with protection and individual immunity with population immunity. A deep understanding of the adaptive immune system and herd immunity dynamics is essential for making informed personal and public health decisions.

NGSS ALIGNMENT:
HS-LS1-2, HS-LS1-4: Develop and use a model to illustrate the hierarchical organization of interacting systems that provide specific functions within multicellular organisms. Use a model to illustrate the role of cellular division (mitosis) in producing and maintaining complex organisms.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Developing and Using Models
  Students develop computational models to illustrate how the adaptive immune system produces immunological memory and how population-level vaccination coverage creates herd immunity.
• Disciplinary Core Idea: LS1.A Structure and Function
  The immune system's hierarchical organization — from molecular antigen recognition through cellular activation to systemic memory — provides a specific defense function through coordinated interactions among specialized cells.
• Crosscutting Concept: Systems and System Models
  Students model immunity at two scales: the cellular scale (individual immune response) and the population scale (herd immunity dynamics), understanding how individual-level processes create emergent population-level protection.

PACING GUIDE:
• Step 1 (Locate): 8-10 minutes
• Step 2 (Establish): 8-10 minutes
• Step 3 (Visualize & Evaluate): 10-12 minutes
• Step 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Adaptive Immunity, Memory B Cell, Herd Immunity Threshold, R0 (Basic Reproduction Number)
□ Prepare How does your immune system 'remember' a disease it has never had — and at what point does vaccinating enough people protect everyone, even those who can't be vaccinated discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify vaccination rate, antigen exposure, antibody production, memory cell population, herd immunity level, and disease transmission rate as the key components of the vaccination-immunity system.
• Establish: Students determine that vaccination rate and antigen exposure are external inputs controlled by public health policy and vaccine design, while antibody production, memory cells, herd immunity, and disease transmission are biological and epidemiological outcomes that emerge from the interaction of individual immune responses at the population level.
• Visualize: Students build a computational model operating at two scales: individual immune response (antigen to memory cells) and population dynamics (vaccination rate to herd immunity threshold).
• Evaluate: Students run individual immune response, herd immunity buildup, and under-vaccinated outbreak scenarios to understand both the cellular basis of protection and the population-level dynamics of disease control.
• Revise: Students add vaccine efficacy rate, variant evolution, or vaccine hesitancy to explore real-world complications that affect both individual and population immunity.

BACKGROUND CONTENT:
• The Adaptive Immune System: Learning Through Molecular Recognition:
  The adaptive immune system relies on two types of lymphocytes: B cells (which produce antibodies) and T cells (which kill infected cells and coordinate the immune response). Each B cell and T cell carries unique receptors generated through random gene rearrangement — your body produces billions of different receptor variants, ensuring that at least a few will recognize virtually any pathogen. When a pathogen's antigens bind to matching receptors, those specific B and T cells are activated, multiply rapidly (clonal expansion), and mount a targeted attack. This process takes 7-14 days for a first exposure — which is why you get sick before your immune system can clear the infection.

• How Vaccines Create Memory Without Disease:
  Vaccines introduce antigens in a form that triggers the adaptive immune response without causing illness. Traditional vaccines use weakened (attenuated) or killed pathogens. Modern approaches include subunit vaccines (purified protein fragments), mRNA vaccines (genetic instructions for cells to make the antigen), and viral vector vaccines (harmless viruses carrying pathogen genes). All approaches accomplish the same goal: activating pathogen-specific B cells and T cells, driving clonal expansion, and producing memory cells — all without the pathogen ever establishing an infection.

• Memory Cells: The Permanent Guard:
  After the initial immune response clears the antigen, 90-95% of activated B and T cells die through apoptosis. But a critical fraction — memory B cells and memory T cells — survive and persist for years or decades in lymph nodes, bone marrow, and tissues throughout the body. These memory cells retain the exact receptor specificity for the pathogen. Upon re-exposure (whether from infection or a booster vaccine), memory cells activate within hours, producing a secondary response that is 10-100 times faster and stronger than the primary response. This is why vaccinated people either don't get sick at all or experience much milder illness.

• Herd Immunity: Individual Decisions, Collective Consequences:
  Herd immunity is the population-level protection that emerges when enough individuals are immune to break transmission chains. The threshold is calculated as 1 - (1/R0): measles (R0≈15) requires approximately 93% immunity; pertussis (R0≈12) requires 92%; COVID-19 original strain (R0≈3) required 67%. Below the threshold, outbreaks can occur because susceptible individuals are connected in the population. Above the threshold, even susceptible individuals (infants too young to vaccinate, immunocompromised patients) are protected because the pathogen cannot find enough hosts to sustain spread. Every person who chooses not to vaccinate shifts the population closer to — or below — this critical threshold.

COMMON MISCONCEPTIONS:
• "Vaccines inject the disease into your body and make you sick"
  Reality: Vaccines do not contain active, disease-causing pathogens. Depending on the type, they contain weakened (attenuated) pathogens that cannot cause disease, killed pathogens, purified protein subunits, or mRNA instructions for making a single viral protein. These trigger an immune response — which can cause mild side effects like soreness, low fever, and fatigue as the immune system activates — but this is fundamentally different from having the disease. The side effects are signs that your immune system is learning.
  Strategy: Analogy: A fire drill is not a fire. It activates the same response systems (alarm, evacuation procedures) without the actual danger. Mild discomfort after a vaccine is the immune system's 'drill' — your body is practicing for a threat it may face later.

• "If vaccines work, why do vaccinated people sometimes still get sick?"
  Reality: No vaccine is 100% effective — efficacy ranges from 40% (flu) to 97% (measles). Some vaccinated individuals don't develop full immunity due to individual variation in immune response. Additionally, immunity can wane over time, which is why boosters are recommended. However, vaccinated individuals who do become infected almost always experience milder illness, shorter duration, and dramatically lower risk of hospitalization or death compared to unvaccinated individuals. The model shows that even imperfect individual protection, when spread across a population, creates powerful herd immunity.
  Strategy: Show model data comparing disease outcomes in vaccinated versus unvaccinated groups. Even at 90% efficacy, a vaccinated population experiences 90% fewer infections and even greater reductions in severe disease.

• "Herd immunity can be achieved through natural infection instead of vaccination"
  Reality: While natural infection does produce immunity, achieving herd immunity through infection requires a massive number of people to actually get sick — and for diseases like measles, COVID-19, and influenza, this means widespread hospitalization, disability, and death. For measles (R0=15), 93% of the population would need to be infected, resulting in hundreds of thousands of deaths in a country like the US. Vaccination achieves the same herd immunity without the disease burden. The model clearly shows identical herd immunity curves whether immunity comes from vaccination or infection — but the human cost is orders of magnitude different.
  Strategy: Run the model with 93% immunity achieved through natural infection: calculate the hospitalizations and deaths required. Then run it with 93% achieved through vaccination. The herd immunity outcome is identical; the human cost is not.

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
Big Question: How does your immune system 'remember' a disease it has never had — and at what point does vaccinating enough people protect everyone, even those who can't be vaccinated?
Answer: Your immune system learns through a remarkable process of molecular pattern recognition. When a vaccine introduces harmless fragments of a pathogen (antigens), your B cells and T cells that happen to recognize those specific molecular shapes are activated, multiply, and produce targeted antibodies. Most of these immune cells die off after the threat is cleared, but a critical population of memory B cells and memory T cells survive for years or decades. When the real pathogen arrives, these memory cells recognize it instantly and mount a massive, rapid response — producing antibodies in hours instead of the weeks the first response took. At the population level, when enough people are immune (the herd immunity threshold), the pathogen cannot find enough susceptible hosts to sustain transmission, and even unvaccinated individuals are protected. This threshold depends on how contagious the disease is: measles needs 93% immunity, while less contagious diseases need less.

Simulation Answers:
• Individual Immune Response Scenario: After vaccination, the model shows Antibody Production peaking at approximately 2-4 weeks as activated B cells differentiate into plasma cells. Antibody levels then gradually decline over months as short-lived plasma cells die. However, Memory Cell Population stabilizes at a significant level and persists indefinitely. When the simulated pathogen exposure occurs months later, memory cells activate within hours, producing a secondary antibody response that is 10-100x faster and stronger than the primary response — fast enough to clear the pathogen before symptoms develop.
• Herd Immunity Buildup Scenario: As Vaccination Rate increases from 0% to 95% for a disease with R0=5 (herd immunity threshold = 80%), the model shows Disease Transmission Rate declining gradually at first but then dropping sharply as coverage approaches 80%. Below 80%, outbreaks still occur because chains of susceptible individuals allow the pathogen to spread. At exactly 80%, transmission becomes unsustainable — each infected person infects, on average, less than one other person, and the outbreak dies out. The 3% immunocompromised population that cannot be vaccinated is protected once the 80% threshold is crossed.

Reflection Exemplars:
• Q: How does your model illustrate the difference between individual and population immunity?
  A: My model operates at two distinct scales that connect through an emergent property. At the individual scale, vaccination triggers antigen recognition, B cell activation, antibody production, and memory cell formation — this protects ONE person. At the population scale, when enough individuals are immunized, herd immunity emerges — this protects EVERYONE, including those who cannot be vaccinated. The threshold effect is key: individual immunity adds up linearly, but the protective effect is nonlinear. Going from 70% to 80% vaccination might be the difference between sustained outbreaks and disease elimination.
• Q: Why are immunocompromised individuals harmed when vaccination rates drop?
  A: Immunocompromised people — cancer patients on chemotherapy, organ transplant recipients on anti-rejection drugs, babies too young to vaccinate — cannot develop their own immunity. They depend entirely on herd immunity: the community around them being vaccinated enough that the pathogen cannot reach them. My model shows that when vaccination drops below the herd immunity threshold, transmission chains reconnect and susceptible individuals are exposed. The immunocompromised are the most vulnerable because they have the weakest immune responses. A measles outbreak in a community at 80% vaccination (below the 93% threshold) will disproportionately hospitalize and kill those who could not be vaccinated. Individual vaccination decisions have collective consequences.

STEM CHALLENGE GUIDANCE:
Title: Design a Vaccination Strategy for a New Pandemic
Mission: Design a vaccination rollout strategy for a new respiratory virus with known R0 that achieves herd immunity in the shortest time while prioritizing the most vulnerable populations.
Scenario: A novel respiratory virus with an R0 of 4.5 has been identified, and a vaccine has just been approved. Your public health team must design a nationwide vaccination strategy. The herd immunity threshold is approximately 78%. You have limited initial vaccine supply (enough for 20% of the population per month), an immunocompromised population of 3% who cannot be vaccinated, and significant vaccine hesitancy in certain communities. Your plan must achieve herd immunity before the fall respiratory season.
Introduction: Present the challenge: A novel respiratory virus with R0 of 4.5 has emerged, and a vaccine has just been approved. Your public health team must design a nationwide rollout that achieves herd immunity before the fall respiratory season, with limited supply and significant hesitancy in certain communities.

Key Concepts:
• Vaccine Prioritization Ethics: When vaccine supply is limited, public health officials must decide who receives doses first. Priority frameworks balance multiple criteria: medical vulnerability (elderly, immunocompromised), essential workers (healthcare, food supply), transmission risk (dense housing, group settings), and equity (communities with highest disease burden and least access to care).
• Ring Vaccination: A targeted strategy where everyone in contact with a confirmed case is vaccinated immediately, creating a 'ring' of immunity around each outbreak. This strategy was used to eradicate smallpox and can be effective for diseases with moderate R0, especially when vaccine supply is limited.
• Addressing Vaccine Hesitancy: Effective public health communication requires understanding the root causes of hesitancy: medical mistrust (often justified by historical abuses like the Tuskegee experiment), misinformation, perceived low risk, and access barriers. Community health workers, trusted messengers, and culturally responsive communication are more effective than mandates or shaming.

Evaluation Rubric:
• Expert (4): Strategy calculates correct herd immunity threshold, prioritizes populations based on scientific and ethical criteria, addresses hesitancy with evidence-based communication plan, includes timeline with model-based projections, and protects immunocompromised populations
• Proficient (3): Strategy identifies correct threshold, proposes reasonable prioritization with some scientific justification, and considers hesitancy and vulnerable populations
• Developing (2): Strategy proposes vaccination rollout but lacks threshold calculations, detailed prioritization criteria, or consideration of hesitancy and vulnerable groups
• Beginning (1): Strategy is incomplete or proposes vaccination without calculating threshold, prioritizing populations, or using model evidence

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a visual diagram of the adaptive immune response from antigen exposure through memory cell formation, with labeled steps and timelines
  • Use a population grid visualization showing how increasing vaccination coverage breaks transmission chains at the herd immunity threshold
  • Sentence frames: 'For a disease with R0 of __, the herd immunity threshold is __ because the formula 1-(1/R0) gives __. This means __% of the population must be immune to stop transmission.'

Extensions (Advanced Learners):
  • Research how mRNA vaccine technology works compared to traditional attenuated vaccines — use your model to evaluate whether the faster production time of mRNA vaccines changes the calculus for pandemic response
  • Investigate the concept of 'original antigenic sin' — how prior immune memory can sometimes interfere with the response to new variants — and add this complication to your model
  • Analyze the global equity challenge: how does the distribution of vaccines between wealthy and developing nations affect the emergence of new variants and the timeline for global herd immunity?

Cross-Curricular Connections:
  • Math: Calculate the herd immunity threshold for the following diseases: Measles (R0=15), Pertussis (R0=12), COVID-19 original (R0=3), Seasonal flu (R0=1.3). Graph the relationship between R0 and threshold percentage. What mathematical function describes this relationship?
  • ELA: Write a public health communication piece designed to address vaccine hesitancy in a specific community. Research the community's concerns, acknowledge them honestly, and provide clear scientific explanations using your model's evidence about how individual vaccination decisions affect community protection.
  • History: Research the eradication of smallpox — the only human disease ever eliminated through vaccination. Analyze the scientific, logistical, and political challenges of the WHO's Intensified Eradication Program (1967-1980). What lessons from smallpox eradication apply to current global health challenges?

CAST ALIGNMENT:
• Model the cellular mechanisms by which vaccines produce immunological memory without causing disease
• Predict the herd immunity threshold for diseases with different R0 values
• Analyze how vaccination coverage affects disease transmission and protection of immunocompromised individuals

CAST-Style Assessment Questions:
• Multiple Choice: A disease has an R0 of 6, meaning each infected person spreads it to 6 others. Using the herd immunity formula (1 - 1/R0), what percentage of the population must be immune to stop transmission? A) 50% B) 67% C) 83% D) 93%
• Constructed Response: Using your model, explain why a person who was vaccinated 10 years ago is still protected even though their antibody levels have declined significantly. Describe the role of memory cells and how the secondary immune response differs from the primary response.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: How Does Your Immune System Learn?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. How do you think a vaccine protects you from getting sick — what is it actually doing inside your body?

   _________________________________________________________

   _________________________________________________________

2. Why do you think you need a new flu shot every year but your measles vaccine from childhood still works decades later?

   _________________________________________________________

   _________________________________________________________

3. If most people in a school are vaccinated against a disease, does that protect students who aren't vaccinated? Why or why not?

   _________________________________________________________

   _________________________________________________________

4. Draw a diagram showing what you think happens in your body between receiving a vaccine and being protected from the disease.

   [DRAWING BOX]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Adaptive Immunity             
___ Memory B Cell                 
___ Herd Immunity Threshold       
___ R0 (Basic Reproduction Number)

A. The branch of the immune system that learns to recognize specific pathogens through antigen presentation, producing targeted antibodies and memory cells — it is slower than innate immunity on first exposure but provides rapid, powerful protection upon re-exposure
B. A long-lived white blood cell produced during an immune response that retains the molecular blueprint for producing specific antibodies — upon re-exposure to the same pathogen, memory B cells rapidly differentiate into plasma cells that flood the body with antibodies in hours instead of weeks
C. The percentage of a population that must be immune to a disease for transmission to stop spreading — calculated as 1 - (1/R0), where R0 is the basic reproduction number. Measles (R0=15) requires 93% immunity; COVID (R0=3) requires 67%
D. The average number of people one infected person will spread the disease to in a fully susceptible population — measles has an R0 of 12-18 (extremely contagious), seasonal flu is 1.3, and COVID-19 original strain was approximately 2.5-3.0

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

SCENARIO: Individual Immune Response
Settings: Single vaccination dose | 30-day antibody tracking + 6-month memory tracking
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Herd Immunity Buildup
Settings: Vaccination rate: 0% to 95% | Disease R0 = 5
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Outbreak in Under-Vaccinated Population
Settings: Vaccination rate: 80% | Disease requiring 93% immunity (measles)
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

1. How does your model illustrate the difference between individual immunity and population-level herd immunity?

   _________________________________________________________

   _________________________________________________________

2. Why is the herd immunity threshold a sharp transition rather than a gradual improvement — what does this tell you about how diseases spread?

   _________________________________________________________

   _________________________________________________________

3. How does your model demonstrate that people who cannot be vaccinated are directly harmed when vaccination rates drop below the herd immunity threshold?

   _________________________________________________________

   _________________________________________________________

4. What role does R0 play in determining how difficult a disease is to control through vaccination?

   _________________________________________________________

   _________________________________________________________

5. What are the limitations of your model in representing real-world vaccination challenges like hesitancy, access, and variant evolution?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. How does your immune system 'remember' a disease it has never had — and at what point does vaccinating enough people protect everyone, even those who can't be vaccinated? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Developing and Using Models
   □ Disciplinary Core Idea: LS1.A Structure and Function
   □ Crosscutting Concept: Systems and System Models

3. What are the limitations of your model in representing real-world vaccination challenges like hesitancy, access, and variant evolution?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Vaccination Strategy for a New Pandemic
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design a vaccination rollout strategy for a new respiratory virus with known R0 that achieves herd immunity in the shortest time while prioritizing the most vulnerable populations.

SCENARIO: A novel respiratory virus with an R0 of 4.5 has been identified, and a vaccine has just been approved. Your public health team must design a nationwide vaccination strategy. The herd immunity threshold is approximately 78%. You have limited initial vaccine supply (enough for 20% of the population per month), an immunocompromised population of 3% who cannot be vaccinated, and significant vaccine hesitancy in certain communities. Your plan must achieve herd immunity before the fall respiratory season.

GUIDING QUESTIONS:
• Which population groups should receive the vaccine first, and what scientific reasoning supports your prioritization?
• At what vaccination coverage does your model predict transmission will stop — and how many months will it take to reach that level?
• How will your strategy protect the 3% of the population who cannot be vaccinated due to medical conditions?

DESIGN THINKING:
• What is the mathematically calculated herd immunity threshold for an R0 of 4.5, and what margin of error should you build in?

  _________________________________________________________

• How will you address vaccine hesitancy — what does your model show about the consequences of sub-threshold coverage?

  _________________________________________________________

• If a new variant emerges with R0 of 7, how does your strategy need to change?

  _________________________________________________________

• What monitoring system will you use to track vaccination coverage and detect outbreaks in under-vaccinated pockets?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Strategy calculates correct herd immunity threshold, prioritizes populations based on scientific and ethical criteria, addresses hesitancy with evidence-based communication plan, includes timeline with model-based projections, and protects immunocompromised populations
• Proficient (3): Strategy identifies correct threshold, proposes reasonable prioritization with some scientific justification, and considers hesitancy and vulnerable populations
• Developing (2): Strategy proposes vaccination rollout but lacks threshold calculations, detailed prioritization criteria, or consideration of hesitancy and vulnerable groups
• Beginning (1): Strategy is incomplete or proposes vaccination without calculating threshold, prioritizing populations, or using model evidence

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CAST-Aligned Pre/Post Assessment

### Administration Instructions

These 5 multiple-choice questions are administered identically as both a pre-assessment (before Activity 1) and a post-assessment (after Activity 4). Score each out of 5. Learning growth = post-score minus pre-score.

Questions follow the California Science Test (CAST) stimulus-response format. Each item is three-dimensional, assessing a Science and Engineering Practice (SEP), Disciplinary Core Idea (DCI), and Crosscutting Concept (CCC) simultaneously, aligned to HS-LS1-2, HS-LS1-4.

---

### Pre-Assessment Questions

### Question 1

A person is vaccinated against measles at age 2 and encounters the actual measles virus at age 17. Their immune system mounts a rapid, powerful response. Which component of the immune system is primarily responsible for this rapid secondary response?

A. Innate immune cells that provide the same nonspecific defense against all pathogens
B. Memory B cells that retained the molecular blueprint for producing measles-specific antibodies for 15 years
C. Red blood cells that carry antibodies through the bloodstream
D. The vaccine itself, which remains active in the body for decades

Correct Answer: B

Feedback: Correct. Memory B cells are long-lived cells that persist for years or decades after the initial immune response. Upon re-exposure to the measles antigen, they rapidly differentiate into plasma cells that produce targeted antibodies within hours rather than the weeks required for a primary response. Consider what makes the secondary immune response different from the first. The speed and specificity suggest the immune system 'remembers' the pathogen. Which cell type stores this molecular memory?

---

### Question 2

The herd immunity threshold for measles (R0 = 15) is approximately 93%. What does this percentage represent?

A. The percentage of infected people who will recover from measles
B. The proportion of the population that must be immune to prevent sustained community transmission
C. The effectiveness rate of the measles vaccine
D. The percentage of the population that will eventually contract measles

Correct Answer: B

Feedback: Correct. The herd immunity threshold (1 - 1/R0) is the proportion of the population that must be immune to break transmission chains. For measles, 93% immunity means each infected person encounters mostly immune individuals, reducing their effective transmission below 1. Herd immunity is a population-level concept. It refers to the point at which enough people are immune that the pathogen can no longer sustain transmission chains through the community. Calculate 1 - (1/15) to find the threshold.

---

### Question 3

Which statement best describes how vaccines train the immune system?

A. Vaccines inject pre-made antibodies that fight pathogens directly
B. Vaccines introduce weakened or inactivated pathogen components that trigger the adaptive immune system to produce its own memory cells without causing disease
C. Vaccines strengthen the innate immune system by increasing white blood cell production
D. Vaccines create a permanent barrier in the bloodstream that prevents all pathogens from entering

Correct Answer: B

Feedback: Correct. Vaccines expose the immune system to antigens (pathogen components) in a safe form. This triggers the full adaptive immune response, including antibody production and memory cell formation, without the risk of disease. The immune system builds its own lasting protection. Vaccines work WITH your immune system, not as a substitute for it. They provide a safe preview of the pathogen so your immune system can build memory before encountering the real threat.

---

### Question 4

If a community has 80% vaccination coverage against a disease requiring 93% coverage for herd immunity, which prediction is most accurate?

A. The community is fully protected because 80% is close enough to 93%
B. Outbreaks can still occur among the susceptible 20%, and unvaccinated individuals who cannot receive vaccines (infants, immunocompromised) remain at risk
C. Only vaccinated individuals can contract the disease
D. The disease will spontaneously disappear because 80% coverage eliminates the pathogen

Correct Answer: B

Feedback: Correct. The 13% gap below the herd immunity threshold means transmission chains can still propagate through the susceptible population. This puts everyone who cannot be vaccinated (infants, cancer patients, organ recipients) at risk because the community shield is incomplete. Herd immunity is a threshold effect, not a gradual one. Below the threshold, enough susceptible people remain connected in the population for the pathogen to spread. Consider who is most vulnerable when community protection is incomplete.

---

### Question 5

After receiving a vaccine, a patient's blood test shows antibody levels that peak at 2 weeks, then gradually decline over the following months. Does this decline mean the vaccine has stopped working?

A. Yes, declining antibodies mean the patient is no longer protected
B. No, because memory B cells persist long after circulating antibody levels decline, enabling rapid antibody production upon re-exposure
C. Yes, which is why booster shots must be given every month
D. No, because the vaccine continuously produces new antibodies

Correct Answer: B

Feedback: Correct. Circulating antibody levels naturally decline after the initial immune response, but the critical memory cells persist for years or decades. These memory cells can reactivate within hours of re-exposure, producing antibodies far faster than the original response. Distinguish between circulating antibodies (which are active proteins in the blood) and memory cells (which are living cells that store the blueprint for making those antibodies). Which one provides long-term protection?

---

### Post-Assessment Questions

### Question 1

A student's model shows that when vaccination rate crosses the herd immunity threshold, disease transmission drops sharply rather than gradually. Which explanation best accounts for this threshold behavior?

A. The vaccine becomes more effective at higher coverage levels
B. Below the threshold, transmission chains can connect susceptible individuals across the population; at the threshold, immune individuals fragment these chains into disconnected clusters that cannot sustain spread
C. The pathogen mutates to become less infectious at high vaccination rates
D. People change their behavior when they know most of the population is vaccinated

Correct Answer: B

Feedback: Correct. Herd immunity operates as a percolation threshold: when enough nodes (people) are immune, the network of susceptible individuals becomes fragmented into small, disconnected clusters. The pathogen can no longer find a continuous path through the population, and transmission collapses. Think of the population as a network. Each immune person removes a node from the transmission network. At some point, the network fractures into small disconnected groups. This is a sudden transition, not a gradual decline.

---

### Question 2

The model simulates an outbreak in a population with 85% vaccination coverage for a disease with R0 = 5 (herd immunity threshold = 80%). Despite being above the threshold, a small outbreak occurs. Which explanation is most consistent with the model?

A. The model is incorrect because outbreaks should be impossible above the herd immunity threshold
B. Clustering of unvaccinated individuals in geographic or social groups can create local pockets of susceptibility that sustain limited transmission even when overall coverage exceeds the threshold
C. The vaccine failed in all affected individuals simultaneously
D. The pathogen's R0 increased spontaneously during the simulation

Correct Answer: B

Feedback: Correct. Herd immunity thresholds assume uniform mixing. When unvaccinated individuals cluster together (by geography, community, or belief system), local susceptibility can exceed the threshold even when the overall population average is above it. This is why spatially uniform coverage matters. The overall percentage is above the threshold, but herd immunity assumes uniform distribution. Consider what happens if unvaccinated individuals are concentrated in the same school, neighborhood, or community rather than evenly spread across the population.

---

### Question 3

A model comparison shows that the individual immune response simulation takes 14 days to reach peak antibody production on first exposure but only 2 days on second exposure. Which cellular mechanism accounts for this 7-fold speed increase?

A. The pathogen is weaker on second exposure
B. Memory B cells bypass the initial antigen recognition and clonal expansion phases, immediately differentiating into antibody-producing plasma cells
C. The innate immune system handles the second infection entirely without adaptive immunity
D. Antibodies from the first exposure remain in the blood permanently

Correct Answer: B

Feedback: Correct. During the primary response, naive B cells must encounter the antigen, become activated, undergo clonal expansion, and differentiate into plasma cells. Memory B cells skip these early steps, having already been selected and expanded. They can begin producing antibodies almost immediately. Consider what steps are required during the first immune response that can be skipped during the second. Memory cells exist precisely to accelerate this process. What steps do they eliminate?

---

### Question 4

A pandemic response team uses the model to plan a vaccination rollout with limited supply. For a disease with R0 = 4.5 and a 6-month timeline, which prioritization strategy would the model evidence best support?

A. Vaccinate the youngest populations first because they have the longest remaining lifespan
B. Distribute vaccines randomly through a lottery system for fairness
C. Prioritize high-transmission groups (healthcare workers, essential workers, densely housed populations) first to reduce Re below 1 as quickly as possible with limited supply
D. Vaccinate only the elderly because they have the highest mortality risk

Correct Answer: C

Feedback: Correct. The model shows that reducing Re below 1 is the critical objective for stopping exponential growth. Vaccinating high-transmission individuals first has the largest impact on Re per dose administered, slowing spread most efficiently while supply is limited. The model tracks transmission dynamics, not just individual protection. With limited supply, the strategic question is: which vaccinations reduce the most transmission per dose? Consider who drives the most spread in the population.

---

### Question 5

A student observes that their model produces different outcomes for the same 85% vaccination rate depending on whether the disease has R0 = 3 or R0 = 12. For R0 = 3, the outbreak is contained; for R0 = 12, it spreads widely. Which analysis best explains this difference?

A. The vaccine is less effective against diseases with higher R0
B. 85% coverage exceeds the herd immunity threshold for R0 = 3 (threshold = 67%) but falls far short of the threshold for R0 = 12 (threshold = 92%), so the same coverage produces opposite outcomes
C. Diseases with higher R0 mutate faster and evade the vaccine
D. The model assigns random outcomes when coverage is between 80% and 90%

Correct Answer: B

Feedback: Correct. The herd immunity threshold depends directly on R0 (formula: 1 - 1/R0). At 85% coverage, R0 = 3 requires only 67% (covered), but R0 = 12 requires 92% (not covered). The same population-level immunity can be sufficient or inadequate depending on the pathogen's transmissibility. Calculate the herd immunity threshold for each R0 using 1 - (1/R0). For R0 = 3: 1 - (1/3) = 0.67 or 67%. For R0 = 12: 1 - (1/12) = 0.92 or 92%. Now compare each threshold to the 85% coverage.

---

### Answer Key

**Pre-Assessment:**
Question 1: B
Question 2: B
Question 3: B
Question 4: B
Question 5: B

**Post-Assessment:**
Question 1: B
Question 2: B
Question 3: B
Question 4: C
Question 5: B

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-11/G11L1-L04/G11L1-L04-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-11/G11L1-L04/G11L1-L04-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-11/G11L1-L04/G11L1-L04-Student-Presentation.pptx] |
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