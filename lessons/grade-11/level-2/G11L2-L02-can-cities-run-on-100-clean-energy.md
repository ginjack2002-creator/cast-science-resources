# Lesson: Can Cities Run on 100% Clean Energy?

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G11L2-L02 |
| **Grade** | 11th Grade — Level 2: Advanced Systems Analysis |
| **Lesson Name** | Can Cities Run on 100% Clean Energy? |
| **Status** | Template |

---

## Platform

### Title
**Can Cities Run on 100% Clean Energy? — Modeling Renewable Grid Stability, Storage, and Intermittency**

### Overview
The transition to 100% renewable electricity is the defining engineering challenge of the 21st century. While solar and wind costs have dropped 90% in the past decade, making them the cheapest sources of new electricity generation, their intermittent nature creates a systems integration challenge that grows exponentially as renewable penetration increases. Understanding this challenge requires modeling energy as a complex system with daily, weekly, and seasonal dynamics. Students investigate the driving question: If the sun doesn't always shine and the wind doesn't always blow, can an entire city really run on 100% renewable energy without the lights going out? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic aerial view of a modern city skyline at sunset with extensive rooftop solar panels gleaming, large wind turbines on surrounding hills, and a massive battery storage facility in the foreground with glowing status indicators, dramatic golden-hour lighting with purple sky]

### Grade
11th Grade — Level 2: Advanced Systems Analysis

### NGSS Standard
**HS-PS3-3, HS-ESS3-2**: Design, build, and refine a device that works within given constraints to convert one form of energy into another form of energy. Evaluate competing design solutions for developing, managing, and utilizing energy and mineral resources based on cost-benefit ratios.

### Learning Objectives
- Model how solar and wind intermittency creates gaps between energy supply and demand across daily and seasonal cycles
- Analyze the feedback loops connecting energy storage capacity, grid stability, and renewable penetration rates
- Predict the storage requirements needed to maintain grid reliability at different levels of renewable energy adoption
- Evaluate the trade-offs between different energy storage technologies and their roles in a fully renewable grid

### Component List (Starting Model: 6 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Solar Generation Capacity | External | The total installed solar panel capacity and its output, which varies with time of day, season, cloud cover, and latitude — producing maximum power at midday and zero at night |
| Wind Generation Capacity | External | The total installed wind turbine capacity and its output, which varies with weather patterns, season, and geography — often complementary to solar, producing more at night and in winter |
| Energy Storage Capacity | External | The total battery, pumped hydro, and other storage available to absorb excess renewable generation and discharge during gaps — measured in megawatt-hours of stored energy |
| Grid Demand Pattern | Internal | The hour-by-hour electricity consumption pattern of the city, with morning and evening peaks, midday plateau, and overnight minimum — influenced by weather, season, and economic activity |
| Supply-Demand Balance | Internal | The real-time match between electricity generation (renewable + stored) and consumption, which must be maintained within tight tolerances to prevent grid instability |
| Grid Reliability Index | Internal | The percentage of time the grid successfully meets demand without blackouts, brownouts, or emergency fossil fuel backup — the target standard is 99.97% (less than 3 hours of outage per year) |

### Research for Lesson
- The Intermittency Challenge — reference materials and textbook resources
- The Duck Curve and Daily Cycling — reference materials and textbook resources
- Storage Technologies and Their Limits — reference materials and textbook resources
- Real-World Progress and Remaining Gaps — reference materials and textbook resources

---

## Step 1: LOCATE — Build Your System

### Text Editor

```
CAN CITIES RUN ON 100% CLEAN ENERGY?

Modeling Renewable Grid Stability, Storage, and Intermittency.
If the sun doesn't always shine and the wind doesn't always blow, can an entire city really run on 100% renewable energy without the lights going out?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Solar Generation Capacity" — the total installed solar panel capacity and its output
  ○ Click "Wind Generation Capacity" — the total installed wind turbine capacity and its output
  ○ Click "Energy Storage Capacity" — the total battery
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Grid Demand Pattern" — the hour-by-hour electricity consumption pattern of the city
  ○ Click "Supply-Demand Balance" — the real-time match between electricity generation (renewable + stored) and consumption
  ○ Click "Grid Reliability Index" — the percentage of time the grid successfully meets demand without blackouts

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
"If the sun doesn't always shine and the wind doesn't always blow, can an entire city really run on 100% renewable energy without the lights going out?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Solar Generation Capacity' — that's external. The total installed solar panel capacity and its output.
Click on 'Wind Generation Capacity' — that's external. The total installed wind turbine capacity and its output.
Click on 'Energy Storage Capacity' — that's external. The total battery.
Click on 'Grid Demand Pattern' — that's internal. The hour-by-hour electricity consumption pattern of the city.
Click on 'Supply-Demand Balance' — that's internal. The real-time match between electricity generation (renewable + stored) and consumption.
Click on 'Grid Reliability Index' — that's internal. The percentage of time the grid successfully meets demand without blackouts, brownouts, or emergency fossil fuel backup — the target standard is 99.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Solar Generation Capacity, Wind Generation Capacity, and Energy Storage Capacity are external components because they are determined by infrastructure investment decisions — city planners choose how much of each to build. Grid Demand Pattern, Supply-Demand Balance, and Grid Reliability Index are internal components because they emerge from the interactions between generation, storage, weather, and consumption patterns within the system.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next step, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 6 components sorted: Solar Generation Capacity, Wind Generation Capacity, Energy Storage Capacity (External), Grid Demand Pattern, Supply-Demand Balance, Grid Reliability Index (Internal)]

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
• Click on "Solar Generation Capacity" and drag an arrow to "Supply-Demand Balance"
• Click on "Wind Generation Capacity" and drag an arrow to "Supply-Demand Balance"
• Click on "Energy Storage Capacity" and drag an arrow to "Grid Reliability Index"
• Click on "Supply-Demand Balance" and drag an arrow to "Grid Reliability Index"

Task C: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Solar Generation Capacity → Supply-Demand Balance = POSITIVE (+)
    Higher Solar Generation increases daytime electricity supply, improving Supply-Demand Balance during daylight hours. However, this relationship reverses at night when solar output drops to zero, creating the daily cycling challenge.

  ○ Wind Generation Capacity → Supply-Demand Balance = POSITIVE (+)
    Higher Wind Generation adds electricity supply that partially complements solar — wind often produces more at night and in winter when solar is weakest. This diversification improves overall Supply-Demand Balance across more hours.

  ○ Energy Storage Capacity → Grid Reliability Index = POSITIVE (+)
    More storage allows the grid to absorb excess renewable generation and discharge during gaps, directly increasing the percentage of time demand is met. The relationship is strongly positive but with diminishing returns — each additional hour of storage covers increasingly rare weather events.

  ○ Supply-Demand Balance → Grid Reliability Index = POSITIVE (+)
    Better Supply-Demand Balance directly improves Grid Reliability — every hour where supply meets demand is an hour without blackouts. The relationship is binary at each moment: either demand is met or it isn't.

Task D: CHECK YOUR MODEL
• You should have 4 arrows total
• 0 negative relationship(s), 4 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: At 4 PM on a winter evening, solar generation drops to near zero while demand surges as people come home and turn on lights and heaters. If wind is calm, the only power available comes from storage. How much storage is enough — and what happens if it runs out before sunrise?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Solar Generation Capacity' and drag an arrow
over to 'Supply-Demand Balance.'

Here's the key question: When solar generation capacity goes UP, does
supply-demand balance go UP or DOWN?

Higher Solar Generation increases daytime electricity supply, improving Supply-Demand Balance during daylight hours. However, this relationship reverses at night when solar output drops to zero, creating the daily cycling challenge.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Wind Generation Capacity' and drag an arrow
over to 'Supply-Demand Balance.'

Here's the key question: When wind generation capacity goes UP, does
supply-demand balance go UP or DOWN?

Higher Wind Generation adds electricity supply that partially complements solar — wind often produces more at night and in winter when solar is weakest. This diversification improves overall Supply-Demand Balance across more hours.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'Energy Storage Capacity' and drag an arrow
over to 'Grid Reliability Index.'

Here's the key question: When energy storage capacity goes UP, does
grid reliability index go UP or DOWN?

More storage allows the grid to absorb excess renewable generation and discharge during gaps, directly increasing the percentage of time demand is met. The relationship is strongly positive but with diminishing returns — each additional hour of storage covers increasingly rare weather events.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Final connection: Click on 'Supply-Demand Balance' and drag an arrow
over to 'Grid Reliability Index.'

Here's the key question: When supply-demand balance goes UP, does
grid reliability index go UP or DOWN?

Better Supply-Demand Balance directly improves Grid Reliability — every hour where supply meets demand is an hour without blackouts. The relationship is binary at each moment: either demand is met or it isn't.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Look at your model now. You've got 0 negative and 4
positive relationships. 4 arrows total.

At 4 PM on a winter evening, solar generation drops to near zero while demand surges as people come home and turn on lights and heaters. If wind is calm, the only power available comes from storage. How much storage is enough — and what happens if it runs out before sunrise?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Solar Generation Capacity +→ Supply-Demand Balance, Wind Generation Capacity +→ Supply-Demand Balance, Energy Storage Capacity +→ Grid Reliability Index, Supply-Demand Balance +→ Grid Reliability Index]

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
• When Solar Generation Capacity is HIGH, what happens to the internal components?

Task C: SCENARIO — 50% RENEWABLE
• Half renewable, half conventional, moderate storage
• PREDICT FIRST: Do you predict the grid can stay stable with 50% renewables and how much storage is needed?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task D: SCENARIO — 90% RENEWABLE
• Heavy renewable, minimal fossil backup, current storage
• PREDICT FIRST: What do you predict happens to Grid Reliability during a week of cloudy, windless winter weather at 90% renewables?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task E: SCENARIO — 100% RENEWABLE + STORAGE
• All renewable with 48 hours of storage
• PREDICT FIRST: Do you predict that 48 hours of storage is enough to keep the lights on year-round without any fossil fuel backup?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• The first 50-60% of renewable energy on a grid is relatively straightforward to integrate because existing backup plants can fill gaps — but the last 20% from 80% to 100% requires exponentially more storage
• The duck curve creates a paradox: midday solar overproduction must be curtailed (wasted) while evening demand peaks require stored energy — solving this requires massive battery deployment or demand shifting
• Seasonal variation is the hardest challenge: a city might need 4 hours of storage to handle daily solar cycles but 4 weeks of storage to handle winter solar droughts — a 170x difference in storage requirement
• Grid reliability of 99.97% requires that even the worst-case weather scenario (a week of clouds and calm wind in winter) can be covered by storage alone — this sets the minimum storage requirement

THE ANSWER: Cities can run on 100% clean energy, but it requires far more than just installing solar panels and wind turbines. The fundamental challenge is intermittency — the sun and wind don't produce power on demand. Getting to 50% renewable is relatively easy because conventional plants can back up the gaps. But pushing past 80% requires exponential increases in energy storage to handle daily cycles (the duck curve), multi-day weather events, and seasonal variation. The key insight from modeling is that the last 10-20% of decarbonization is by far the hardest and most expensive. The solution likely requires a combination of battery storage, pumped hydro, demand flexibility, geographic diversification, and potentially green hydrogen for long-duration storage. It's technically possible — but the systems engineering challenge is enormous.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: 50% Renewable. Half renewable, half conventional, moderate storage.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: 90% Renewable.
Heavy renewable, minimal fossil backup, current storage.

Before you run it — make a prediction. What do you predict happens to Grid Reliability during a week of cloudy, windless winter weather at 90% renewables?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: 100% Renewable + Storage. All renewable with 48 hours of storage.
Do you predict that 48 hours of storage is enough to keep the lights on year-round without any fossil fuel backup?

Here's what our model reveals: Cities can run on 100% clean energy, but it requires far more than just installing solar panels and wind turbines. The fundamental challenge is intermittency — the sun and wind don't produce power on demand. Getting to 50% renewable is relatively easy because conventional plants can back up the gaps. But pushing past 80% requires exponential increases in energy storage to handle daily cycles (the duck curve), multi-day weather events, and seasonal variation. The key insight from modeling is that the last 10-20% of decarbonization is by far the hardest and most expensive. The solution likely requires a combination of battery storage, pumped hydro, demand flexibility, geographic diversification, and potentially green hydrogen for long-duration storage. It's technically possible — but the systems engineering challenge is enormous.

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
   • What happens if you turn OFF Solar Generation Capacity?
   • What happens if you turn OFF Wind Generation Capacity?
   • What happens if you turn OFF Energy Storage Capacity?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Demand Response Programs — Smart grid systems that incentivize consumers to shift electricity usage away from peak hours — like running dishwashers at midnight when wind power is abundant — reducing the gap between supply and demand
   • Green Hydrogen Production — Using excess renewable electricity to split water into hydrogen and oxygen through electrolysis — storing energy in chemical form for weeks or months and converting it back to electricity when needed
   • Geographic Diversification — Connecting grids across wide geographic areas so that when wind is calm in one region, power can be imported from where it's blowing — the wind is always blowing somewhere

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • The Intermittency Challenge — how does this connect to your model?
   • The Duck Curve and Daily Cycling — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • Why does the difficulty of integrating renewables increase exponentially rather than linearly as you approach 100%?
   • How does the duck curve in your model create both waste and shortage on the same day?
   • What does your model reveal about why seasonal storage is a fundamentally different challenge than daily storage?
   • How would climate change itself (hotter summers, more extreme weather) affect the grid your model designs?

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

Demand Response Programs. Smart grid systems that incentivize consumers to shift electricity usage away from peak hours — like running dishwashers at midnight when wind power is abundant — reducing the gap between supply and demand
How would you model that?

Green Hydrogen Production. Using excess renewable electricity to split water into hydrogen and oxygen through electrolysis — storing energy in chemical form for weeks or months and converting it back to electricity when needed
How would you model that?

Geographic Diversification. Connecting grids across wide geographic areas so that when wind is calm in one region, power can be imported from where it's blowing — the wind is always blowing somewhere
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

Grid Integration Engineers design the systems that connect renewable energy sources to electrical grids while maintaining stability and reliability. They work for utilities, grid operators like CAISO and ERCOT, renewable energy companies, and consulting firms, earning $85,000–$155,000/year. Energy Storage Engineers specializing in battery systems and grid-scale storage earn $90,000–$160,000/year.

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
Visual: Title slide with futuristic renewable city skyline at sunset
Say: "What if I told you that California threw away enough solar energy last year to power 350,000 homes — while still burning natural gas for electricity? That paradox is what we're modeling today."
Do: Show the California duck curve graph. Let students identify the 'duck.' Ask: Why would we waste clean energy while also burning fossil fuels?
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and vocabulary terms
Say: "Today you're tackling one of the biggest engineering challenges of your lifetime — making the electrical grid run on nature's schedule."
Do: Have students read objectives. Pre-teach 'intermittency' and 'grid stability.' Quick activity: turn off the classroom lights for 3 seconds. That's what a grid failure feels like — except for a hospital.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: Can a city run on 100% clean energy?
Say: "Solar costs have dropped 90% in ten years. Wind is now the cheapest electricity on Earth. So why aren't we at 100% renewable already? The answer isn't cost — it's physics."
Do: Quick-write: What happens at 8 PM on a cloudy, windless winter night? Where does electricity come from? Pair-share responses.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps overview
Say: "We're modeling an entire city's electrical grid — millions of people's power, every second of every day, through every weather pattern."
Do: Preview each LEVER step. Emphasize that this is a dynamic system where supply and demand must balance in real time — there's no inventory of electricity.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Six component cards for energy grid model
Say: "Three things you can build — solar, wind, and storage. Three things the system determines — demand pattern, balance, and reliability. How do they connect?"
Do: Guide sorting of external vs. internal components. Discuss why Solar, Wind, and Storage are external (we choose how much to build) while Demand, Balance, and Reliability are system responses.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows between all six components
Say: "When solar generation peaks at noon but demand peaks at 7 PM, what bridges the gap? And what happens when the bridge isn't big enough?"
Do: Help students map the timing mismatches. Draw the duck curve on the board. Identify where storage absorbs surplus and where it discharges. Find the failure point.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Graph predictions and simulation results for three renewable penetration levels
Say: "Let's push the grid to its limits. 50% renewable — easy. 90% — challenging. 100% — let's see if it breaks."
Do: Students predict storage requirements for each level before running simulations. Focus on the nonlinear jump in storage needs from 80% to 100%. Compare curtailment vs. shortage events.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key findings from model exploration
Say: "Your model just showed why the last 20% is ten times harder than the first 80%. But it also showed it's not impossible — just expensive and complex."
Do: Lead discussion on why 100% renewable requires systems thinking, not just more panels. Connect to real-world examples: South Australia, Denmark, California. Discuss the role of emerging storage technologies.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: 100% renewable city energy plan design challenge
Say: "You're now city energy planners. Half a million people are counting on you. Design a grid that never goes dark — using only clean energy."
Do: Groups design comprehensive energy portfolios specifying solar/wind ratios, storage types and capacities, and demand management strategies. Present as city council proposals with cost estimates.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: Can Cities Run on 100% Clean Energy?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
The transition to 100% renewable electricity is the defining engineering challenge of the 21st century. While solar and wind costs have dropped 90% in the past decade, making them the cheapest sources of new electricity generation, their intermittent nature creates a systems integration challenge that grows exponentially as renewable penetration increases. Understanding this challenge requires modeling energy as a complex system with daily, weekly, and seasonal dynamics.

NGSS ALIGNMENT:
HS-PS3-3, HS-ESS3-2: Design, build, and refine a device that works within given constraints to convert one form of energy into another form of energy. Evaluate competing design solutions for developing, managing, and utilizing energy and mineral resources based on cost-benefit ratios.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Designing Solutions and Using Computational Thinking
  Students design energy system solutions using computational models to optimize the balance between renewable generation, storage capacity, and grid reliability under variable weather conditions.
• Disciplinary Core Idea: PS3.D Energy in Chemical Processes / ESS3.A Natural Resources
  Students apply energy conversion principles to understand how electricity is generated from renewable sources and stored in chemical or mechanical form, while evaluating the resource requirements of different storage technologies.
• Crosscutting Concept: Systems and System Models / Energy and Matter
  Students model the energy grid as a complex system where energy flows from generation through storage to consumption, analyzing how intermittent inputs and variable demand create system-level challenges.

PACING GUIDE:
• Step 1 (Locate): 8-10 minutes
• Step 2 (Establish): 8-10 minutes
• Step 3 (Visualize & Evaluate): 10-12 minutes
• Step 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Intermittency, Grid Stability, Capacity Factor, Curtailment, Duck Curve
□ Prepare If the sun doesn't always shine and the wind doesn't always blow, can an entire city really run on 100% renewable energy without the lights going out discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify six components of the renewable energy grid system: Solar Generation Capacity, Wind Generation Capacity, Energy Storage Capacity, Grid Demand Pattern, Supply-Demand Balance, and Grid Reliability Index — distinguishing controllable inputs from system responses.
• Establish: Students determine that Solar and Wind generation create variable supply that must match Grid Demand Pattern through Energy Storage. Supply-Demand Balance determines Grid Reliability. The duck curve emerges when solar peaks misalign with demand peaks.
• Visualize: Students build a computational model showing hourly energy generation, storage cycling, and demand matching across daily and seasonal timescales.
• Evaluate: Students run 50%, 90%, and 100% renewable scenarios to quantify how storage requirements scale nonlinearly with renewable penetration and identify the reliability limits of each configuration.
• Revise: Students add Demand Response Programs, Green Hydrogen, or Geographic Diversification to explore advanced strategies for closing the final gap to 100% renewable electricity.

BACKGROUND CONTENT:
• The Intermittency Challenge:
  Solar panels produce electricity only during daylight hours, with output peaking at midday and dropping to zero at night. Cloud cover can reduce output by 80% within minutes. Wind turbines produce power when wind speeds are between 7-55 mph, but calm periods lasting days are common. In most locations, solar output is 2-3 times higher in summer than winter, while heating demand peaks in winter — creating a seasonal mismatch. A grid relying on these sources must somehow match supply to demand every second of every day, even when nature doesn't cooperate.

• The Duck Curve and Daily Cycling:
  As solar penetration increases, midday electricity production increasingly exceeds demand. California's famous 'duck curve' shows net demand (total demand minus solar) plunging at midday and then surging in the evening as solar drops and people come home. This creates two problems: curtailment (wasting solar energy because the grid can't absorb it) and ramping (needing to bring massive generation online in just 3 hours as solar disappears). In 2023, California curtailed over 2.4 million MWh of solar energy — enough to power 350,000 homes — while still relying on natural gas for evening peaks.

• Storage Technologies and Their Limits:
  Lithium-ion batteries currently dominate grid storage, with costs falling to $150/kWh for 4-hour systems. They excel at daily cycling — absorbing midday solar surplus and discharging during evening peaks. But they become prohibitively expensive for multi-day or seasonal storage because you need enormous capacity. Pumped hydro storage (pumping water uphill to store energy) provides 93% of global energy storage but requires specific geography. Emerging technologies include compressed air, iron-air batteries (100-hour duration), and green hydrogen (seasonal storage). Each technology has different cost, duration, efficiency, and geographic constraints.

• Real-World Progress and Remaining Gaps:
  Several regions have achieved high renewable penetration: South Australia regularly exceeds 70% renewable, Denmark hits 80%+ on windy days, and Costa Rica runs on 98% renewable (mostly hydro). But these success stories rely on interconnection with neighbors who provide backup. A truly isolated 100% renewable grid has never been achieved at city scale. Studies suggest that getting from 80% to 100% renewable requires 5-10x more storage per additional percentage point compared to getting from 0% to 50%. The final 10% may require seasonal storage technologies that don't yet exist at commercial scale.

COMMON MISCONCEPTIONS:
• "Solar and wind are unreliable so we can't depend on them"
  Reality: Solar and wind are variable, not unreliable — their output patterns are predictable and well-understood. Solar will always peak at midday and wind follows seasonal patterns. The challenge is engineering the system to handle variability, not the sources themselves. With sufficient storage and geographic diversification, variable sources can provide reliable electricity.
  Strategy: Distinction: 'unreliable' means unpredictable failure. 'Variable' means predictable fluctuation. Weather forecasting now predicts solar and wind output 72 hours ahead with 95% accuracy. The grid plans for this variability just as it plans for demand variability.

• "We just need more solar panels"
  Reality: Adding more solar panels increases midday production but does nothing for nighttime, cloudy days, or winter months. Beyond a certain point, additional solar increases curtailment (wasted energy) more than it increases useful generation. The bottleneck isn't generation — it's storage and grid integration.
  Strategy: Show the model: double solar capacity and observe what happens. Midday surplus doubles (more curtailment) but nighttime shortage remains identical. Storage is the missing piece, not more panels.

• "Batteries can store unlimited energy"
  Reality: All storage technologies have physical and economic limits. Lithium-ion batteries are excellent for hours but prohibitively expensive for weeks. A city needing 7 days of backup would require battery capacity costing more than the entire generation infrastructure. Different timescales need different storage technologies, and some (like seasonal storage) remain unsolved at commercial scale.
  Strategy: Calculate: At current battery prices ($150/kWh), how much would it cost to store 7 days of electricity for a city? Compare that to the city's annual budget. This reveals why a portfolio of storage types is essential.

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
Big Question: If the sun doesn't always shine and the wind doesn't always blow, can an entire city really run on 100% renewable energy without the lights going out?
Answer: Cities can run on 100% clean energy, but it requires far more than just installing solar panels and wind turbines. The fundamental challenge is intermittency — the sun and wind don't produce power on demand. Getting to 50% renewable is relatively easy because conventional plants can back up the gaps. But pushing past 80% requires exponential increases in energy storage to handle daily cycles (the duck curve), multi-day weather events, and seasonal variation. The key insight from modeling is that the last 10-20% of decarbonization is by far the hardest and most expensive. The solution likely requires a combination of battery storage, pumped hydro, demand flexibility, geographic diversification, and potentially green hydrogen for long-duration storage. It's technically possible — but the systems engineering challenge is enormous.

Simulation Answers:
• 50% Renewable: With 50% renewable generation and moderate storage, the grid maintains high reliability because conventional backup plants can fill gaps during low-sun and low-wind periods. Storage primarily handles the daily duck curve, shifting midday solar to evening peaks. Curtailment is low because solar production rarely exceeds demand. The system is stable and manageable.
• 100% Renewable + Storage: With 100% renewable and 48 hours of storage, the grid handles most scenarios effectively — daily cycling, multi-day weather events, and moderate seasonal variation. However, the model reveals that extreme scenarios (a week of clouds and calm in winter) can deplete even 48 hours of storage. Achieving true 99.97% reliability likely requires either 100+ hours of storage, geographic interconnection, or demand curtailment agreements for the rarest weather events.

Reflection Exemplars:
• Q: Why does the last 20% cost more than the first 80%?
  A: The model demonstrates exponential scaling of storage requirements. At low renewable penetration, conventional plants fill gaps cheaply. At 50%, modest battery storage handles daily cycling. But approaching 100% means covering increasingly rare but increasingly long gaps — a 5-day winter calm requires orders of magnitude more storage than a single night. Additionally, curtailment rises dramatically as peak production exceeds demand more often, meaning you need to build far more generation capacity than peak demand to ensure enough energy is captured and stored for the gaps.
• Q: How does the duck curve create both waste and shortage?
  A: The duck curve shows that at midday, solar production can exceed total grid demand, forcing curtailment — literally throwing away clean electricity. Then just hours later, as the sun sets and demand surges, the grid faces a shortage that must be filled by storage or backup. The model reveals that the same city, on the same day, can waste gigawatt-hours of solar energy at noon and then scramble for power at 7 PM. Storage is the bridge, but its capacity determines whether the gap is bridged or the lights go out.

STEM CHALLENGE GUIDANCE:
Title: Design a 100% Renewable City Energy Plan
Mission: Design a comprehensive energy plan for a mid-sized city (population 500,000) that achieves 100% renewable electricity while maintaining 99.97% grid reliability through all weather conditions.
Scenario: A city council has committed to 100% renewable electricity by 2040 and hired your engineering team to design the generation and storage portfolio. You must balance solar, wind, and storage to maintain reliability through the worst weather weeks of the year while minimizing cost and land use.
Introduction: Present the challenge: A city of 500,000 has committed to 100% renewable electricity by 2040. Your engineering team must design the complete generation and storage portfolio — specifying solar capacity, wind capacity, battery storage, long-duration storage, and demand management programs that maintain 99.97% reliability through all weather conditions.

Key Concepts:
• Energy Density and Storage Duration: Different storage technologies serve different timescales: lithium-ion batteries excel at 2-8 hour daily cycling, pumped hydro provides 8-24 hours, iron-air batteries can store 100+ hours, and green hydrogen enables seasonal storage. The optimal grid uses a portfolio of technologies matched to different duration needs.
• Capacity Factor and Overbuilding: Because solar panels produce only 20-25% of their maximum capacity on average (due to night, clouds, and seasons), a 100% renewable grid must install 3-5x the generation capacity of peak demand to produce enough energy annually. This overbuilding creates more curtailment but also more energy available for storage.
• Grid Inertia and Frequency Regulation: Traditional power plants provide rotational inertia that stabilizes grid frequency. Inverter-based solar and wind don't inherently provide this. Advanced inverters and battery systems can provide synthetic inertia, but grid stability requires careful engineering as conventional plants are retired.

Evaluation Rubric:
• Expert (4): Energy plan specifies optimal solar/wind ratio with geographic justification, deploys multiple storage technologies matched to different duration needs, includes demand management, provides phased implementation timeline, and uses model data to demonstrate 99.97% reliability
• Proficient (3): Energy plan includes solar, wind, and storage with reasonable capacity estimates and addresses daily and multi-day storage needs
• Developing (2): Energy plan mentions solar, wind, and batteries but lacks capacity calculations, duration analysis, or reliability verification
• Beginning (1): Energy plan is incomplete or does not address how intermittency gaps would be covered across different timescales

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a simplified duck curve template where students can plot solar production and demand on the same 24-hour graph to visualize the gap
  • Use stacking blocks to physically represent different storage durations: one block per hour of battery, showing how many blocks are needed for 1 night vs. 5 days vs. 1 month
  • Sentence frames: 'When solar generation drops at sunset, the grid needs __ hours of storage because demand __ while supply __'

Extensions (Advanced Learners):
  • Research the Hornsdale Power Reserve in South Australia (Tesla big battery) and analyze how it transformed grid stability in a region with 70% renewable energy
  • Model how electrifying transportation (EV charging) would change the city's demand curve and whether smart charging could help solve the duck curve by shifting demand to midday
  • Investigate the potential of green hydrogen as seasonal energy storage and calculate how much excess renewable electricity would need to be converted given round-trip efficiency losses

Cross-Curricular Connections:
  • Math: Calculate the total energy storage capacity in MWh needed for a city of 500,000 to survive 5 days without sun or wind, given average per-capita electricity consumption of 30 kWh/day
  • ELA: Write a persuasive op-ed arguing for or against a city mandate requiring 100% renewable electricity by 2040, using model data and real-world examples as evidence
  • Economics: Analyze the levelized cost of electricity for different generation and storage portfolios and create a cost-benefit comparison of 80% vs. 90% vs. 100% renewable targets

CAST ALIGNMENT:
• Model the daily and seasonal patterns of solar and wind generation and how they interact with demand cycles
• Analyze the nonlinear relationship between renewable penetration percentage and required energy storage capacity
• Design an energy portfolio that optimizes the balance between generation, storage, reliability, and cost

CAST-Style Assessment Questions:
• Multiple Choice: A city at 90% renewable energy experiences a week of overcast skies and calm winds in January. Battery storage is depleted after 36 hours. Based on your model, which outcome is MOST likely?
• Constructed Response: Using your model, explain why the cost of achieving 100% renewable electricity is not simply double the cost of achieving 50%. Reference the duck curve, seasonal variation, and storage requirements in your explanation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: Can Cities Run on 100% Clean Energy?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. What do you think happens to a city's electricity when the sun goes down if the city relies on solar power?

   _________________________________________________________

   _________________________________________________________

2. Why can't we just build enough solar panels and wind turbines to power everything?

   _________________________________________________________

   _________________________________________________________

3. Draw a graph showing when you think a city uses the most and least electricity during a 24-hour day.

   [DRAWING BOX]

4. What technologies do you know about that can store large amounts of energy?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Intermittency                 
___ Grid Stability                
___ Capacity Factor               
___ Curtailment                   
___ Duck Curve                    

A. The inherent variability of renewable energy sources like solar and wind, which produce electricity only when the sun shines or wind blows — creating gaps that must be filled by storage or backup generation
B. The ability of an electrical grid to maintain consistent voltage and frequency while instantly matching electricity supply to demand — even a few seconds of imbalance can cause blackouts
C. The ratio of actual electricity output to maximum possible output over time — solar panels average 20-25%, wind turbines 25-45%, while natural gas plants achieve 55-90%
D. The deliberate reduction of renewable energy output when production exceeds demand and storage is full — essentially wasting clean energy because the grid cannot absorb it
E. The graph of net electricity demand (total demand minus solar production) that shows a deep midday dip and steep evening ramp, resembling a duck's profile — the defining challenge of high-solar grids

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

SCENARIO: 50% Renewable
Settings: Half renewable, half conventional, moderate storage
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: 90% Renewable
Settings: Heavy renewable, minimal fossil backup, current storage
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: 100% Renewable + Storage
Settings: All renewable with 48 hours of storage
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

1. Why does the difficulty of integrating renewables increase exponentially rather than linearly as you approach 100%?

   _________________________________________________________

   _________________________________________________________

2. How does the duck curve in your model create both waste and shortage on the same day?

   _________________________________________________________

   _________________________________________________________

3. What does your model reveal about why seasonal storage is a fundamentally different challenge than daily storage?

   _________________________________________________________

   _________________________________________________________

4. How would climate change itself (hotter summers, more extreme weather) affect the grid your model designs?

   _________________________________________________________

   _________________________________________________________

5. What trade-offs does your model expose between cost, land use, reliability, and speed of decarbonization?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. If the sun doesn't always shine and the wind doesn't always blow, can an entire city really run on 100% renewable energy without the lights going out? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Designing Solutions and Using Computational Thinking
   □ Disciplinary Core Idea: PS3.D Energy in Chemical Processes / ESS3.A Natural Resources
   □ Crosscutting Concept: Systems and System Models / Energy and Matter

3. What trade-offs does your model expose between cost, land use, reliability, and speed of decarbonization?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a 100% Renewable City Energy Plan
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design a comprehensive energy plan for a mid-sized city (population 500,000) that achieves 100% renewable electricity while maintaining 99.97% grid reliability through all weather conditions.

SCENARIO: A city council has committed to 100% renewable electricity by 2040 and hired your engineering team to design the generation and storage portfolio. You must balance solar, wind, and storage to maintain reliability through the worst weather weeks of the year while minimizing cost and land use.

GUIDING QUESTIONS:
• What mix of solar and wind generation minimizes the total storage requirement for your city's latitude?
• How would you handle a five-day winter weather event with minimal sun and wind?
• What role should demand-side management play in reducing peak storage requirements?

DESIGN THINKING:
• What is the optimal ratio of solar to wind capacity for your city's location and climate?

  _________________________________________________________

• How many hours of battery storage would you deploy versus long-duration storage like pumped hydro?

  _________________________________________________________

• What demand flexibility programs would you implement to shift loads away from evening peaks?

  _________________________________________________________

• How would you phase the transition over 15 years to maintain reliability at each stage?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Energy plan specifies optimal solar/wind ratio with geographic justification, deploys multiple storage technologies matched to different duration needs, includes demand management, provides phased implementation timeline, and uses model data to demonstrate 99.97% reliability
• Proficient (3): Energy plan includes solar, wind, and storage with reasonable capacity estimates and addresses daily and multi-day storage needs
• Developing (2): Energy plan mentions solar, wind, and batteries but lacks capacity calculations, duration analysis, or reliability verification
• Beginning (1): Energy plan is incomplete or does not address how intermittency gaps would be covered across different timescales

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CAST-Aligned Pre/Post Assessment

### Administration Instructions

These 5 multiple-choice questions are administered identically as both a pre-assessment (before Activity 1) and a post-assessment (after Activity 4). Score each out of 5. Learning growth = post-score minus pre-score.

Questions follow the California Science Test (CAST) stimulus-response format. Each item is three-dimensional, assessing a Science and Engineering Practice (SEP), Disciplinary Core Idea (DCI), and Crosscutting Concept (CCC) simultaneously, aligned to HS-PS3-3, HS-ESS3-2.

---

### Question 1

CAST Alignment: SEP 2.1.1 (Determine components of a system) + DCI PS3.3 + CCC5 (Energy and Matter)

A student is using the ModelIt platform to study the system in this lesson. The model includes these components: Solar Generation Capacity, Wind Generation Capacity, Energy Storage Capacity, Grid Demand Pattern, Supply-Demand Balance, Grid Reliability Index. Some components are external (Solar Generation Capacity, Wind Generation Capacity, Energy Storage Capacity) and some are internal (Grid Demand Pattern, Supply-Demand Balance, Grid Reliability Index). The student needs to understand what each component represents and how they are organized.

A model shows that moving from 50% to 80% renewable energy requires doubling storage capacity, but moving from 80% to 100% requires increasing storage capacity tenfold. Which concept best explains this nonlinear relationship?

A. Renewable energy becomes less efficient at higher penetration levels
B. At high renewable penetration, rare multi-day weather events with minimal sun and wind require enormous storage reserves to avoid blackouts
C. Battery technology degrades faster when used more frequently
D. Grid operators intentionally slow renewable adoption above 80%

Correct Answer: B

Feedback: Correct. The exponential storage increase is driven by worst-case scenarios: at 100% renewable, even rare events like a week of cloudy, windless winter weather must be covered entirely by storage. If you chose A, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose C, this answer suggests something is being added to the system. Look carefully at the model — the total amount stays the same even when components change. The system is conserving matter or energy. If you chose D, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows.

---

### Question 2

CAST Alignment: SEP 2.1.2 (Determine relationships among components) + DCI PS3.3 + CCC1 (Patterns)

In the computational model for this lesson, a student draws arrows between components to show relationships. The model shows that when Energy Storage Capacity increases, Grid Reliability Index increases; when Demand Balance increases, Grid Reliability Index increases. The student is trying to understand why these relationships are positive or negative.

The 'duck curve' describes a pattern where net electricity demand dips at midday and spikes in the evening. A student proposes solving this by installing more solar panels. Why is this solution insufficient?

A. Solar panels cannot be installed on residential rooftops
B. More solar deepens the midday surplus (increasing curtailment) but does nothing for the evening peak when solar output is zero
C. The duck curve only occurs in tropical climates
D. Solar panels generate more electricity in the evening than at midday

Correct Answer: B

Feedback: Correct. Adding more solar worsens the midday oversupply while the evening demand peak remains unmet, making the duck curve problem worse, not better. If you chose A, the model shows these components ARE connected. When one changes, it affects the others through the relationships (positive or negative) that you mapped in the model. If you chose C, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, this answer suggests something is being added to the system. Look carefully at the model — the total amount stays the same even when components change. The system is conserving matter or energy.

---

### Question 3

CAST Alignment: SEP 2.1.3 (Evaluate a model's accuracy) + DCI PS3.3 + CCC4 (Systems and System Models)

A student runs a simulation of the model. The model shows that when Energy Storage Capacity increases, Grid Reliability Index increases and when Demand Balance increases, Grid Reliability Index increases. The student changes one variable to see how the whole system responds.

A city's grid model achieves 99.97% reliability at 90% renewable energy with 12 hours of battery storage. When pushed to 100% renewable, reliability drops to 98.5%. What systems-level intervention would most effectively close this gap?

A. Replace all wind turbines with solar panels to increase consistency
B. Combine expanded battery storage with pumped hydro for multi-day reserves, demand response programs, and geographic diversification of renewable sources
C. Reduce the city's population to lower demand
D. Accept the lower reliability since 98.5% is close enough

Correct Answer: B

Feedback: Correct. Closing the last reliability gap requires a systems approach: long-duration storage (pumped hydro), flexible demand, and geographically diverse generation to reduce the probability of system-wide low generation. If you chose A, this answer suggests something is being added to the system. Look carefully at the model — the total amount stays the same even when components change. The system is conserving matter or energy. If you chose C, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows.

---

### Question 4

CAST Alignment: SEP 2.1.4 (Represent mechanisms to explain/predict events) + DCI PS3.3 + CCC2 (Cause and Effect)

Scientists are studying data related to this system. They collected observations over time and noticed patterns in how the components change. The data shows how changes in one part of the system cascade through the other parts.

A student argues that seasonal variation in solar energy is a minor challenge because 'the sun shines every day.' Using model data, which evidence best counters this claim?

A. A city at 45 degrees N latitude receives 4x more solar energy in June than December, creating a seasonal generation gap that daily batteries cannot bridge
B. Solar panels stop working when temperatures drop below freezing
C. Cloud cover only affects solar generation in the summer months
D. Wind energy perfectly compensates for all seasonal solar variation

Correct Answer: A

Feedback: Correct. Seasonal variation at mid-latitudes creates a generation gap lasting weeks to months. Daily battery cycling (4-12 hours) cannot bridge a months-long winter solar deficit. If you chose B, look at the evidence from the model. The correct answer (A) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose C, look at the evidence from the model. The correct answer (A) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, look at the evidence from the model. The correct answer (A) is supported by the relationships between components. This answer does not match what the simulation data shows.

---

### Question 5

CAST Alignment: SEP 2.1.5 (Apply a model to make predictions) + DCI PS3.3 + CCC5 (Energy and Matter)

A team wants to use the model to solve a real-world problem related to this system. They know they cannot control the external components (Solar Generation Capacity, Wind Generation Capacity, Energy Storage Capacity), but they can take action on internal components (Grid Demand Pattern, Supply-Demand Balance, Grid Reliability Index). They need to decide which action would be most effective based on what the model shows.

Evaluate this claim: 'Since wind and solar are now the cheapest forms of electricity generation, transitioning to 100% renewable energy is primarily an economic decision.' Which model finding most effectively challenges this claim?

A. Renewable energy equipment is manufactured using fossil fuels
B. While generation costs are low, the systems integration costs (storage, grid upgrades, backup capacity) for 100% renewable are the dominant expense and represent a physics and engineering challenge, not just an economic one
C. Solar and wind are only cheaper in sunny and windy regions
D. Fossil fuel companies will lobby against the transition

Correct Answer: B

Feedback: Correct. The cost of generating renewable electricity is low, but the systems engineering challenge of maintaining reliability through all weather conditions drives exponentially higher storage and infrastructure costs. If you chose A, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose C, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows.

---

### Answer Key

Question 1: B (Cognitive Level: Identify — SEP 2.1.1, DCI PS3.3, CCC5)
Question 2: B (Cognitive Level: Reason — SEP 2.1.2, DCI PS3.3, CCC1)
Question 3: B (Cognitive Level: Reason — SEP 2.1.3, DCI PS3.3, CCC4)
Question 4: A (Cognitive Level: Reason + Evidence — SEP 2.1.4, DCI PS3.3, CCC2)
Question 5: B (Cognitive Level: Predict + Apply — SEP 2.1.5, DCI PS3.3, CCC5)


## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-11/G11L2-L02/G11L2-L02-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-11/G11L2-L02/G11L2-L02-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-11/G11L2-L02/G11L2-L02-Student-Presentation.pptx] |
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