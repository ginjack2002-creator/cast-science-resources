# Lesson: Why Can't Weather Apps Get It Right?

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G10L1-L07 |
| **Grade** | 10th Grade — Level 1: How the World Works |
| **Lesson Name** | Why Can't Weather Apps Get It Right? |
| **Status** | Template |

---

## Platform

### Title
**Why Can't Weather Apps Get It Right? — Modeling Atmospheric Systems, Chaos Theory, and the Limits of Prediction**

### Overview
In 1961, meteorologist Edward Lorenz accidentally discovered one of the most profound principles in science. While running a weather simulation, he rounded an initial value from 0.506127 to 0.506 — a difference of less than 0.02%. The resulting forecast was completely different. This discovery — sensitive dependence on initial conditions — revealed that the atmosphere is a chaotic system with a fundamental prediction limit that no technology can ever overcome. Students investigate the driving question: If we have supercomputers, satellites, and thousands of weather stations, why is a 10-day forecast still barely better than a coin flip? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of a dramatic thunderstorm forming over a landscape, dark cumulonimbus clouds with visible lightning, rain curtain in the distance, dramatic lighting with sun still visible on the horizon]

### Grade
10th Grade — Level 1: How the World Works

### NGSS Standard
**HS-ESS2-5, HS-ESS2-3**: Plan and conduct an investigation of the properties of water and its effects on Earth materials and surface processes. Develop a model based on evidence of Earth's interior to describe the cycling of matter by thermal convection.

### Learning Objectives
- Model how solar radiation, temperature, moisture, and wind interact to produce weather patterns
- Explain why small differences in initial conditions can produce dramatically different weather outcomes (chaos theory)
- Predict storm probability based on the interaction of atmospheric variables
- Analyze the fundamental limits of weather prediction and why forecast accuracy decreases with time

### Component List (Starting Model: 5 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Solar Radiation Input | External | The amount of solar energy reaching the surface, which varies by latitude, season, time of day, and cloud cover — the primary energy source driving all atmospheric motion |
| Air Temperature | Internal | The temperature of the air mass, determined by solar heating, latitude, elevation, and nearby land/ocean surfaces — temperature differences between air masses are the engine of weather |
| Moisture Content | Internal | The amount of water vapor in the air, supplied by evaporation from oceans, lakes, and vegetation — determines precipitation potential and releases latent heat when it condenses |
| Wind Speed | Internal | The velocity of air movement, driven by pressure differences created by differential heating — carries heat and moisture horizontally and determines storm movement and intensity |
| Storm Probability | Internal | The likelihood of significant weather events (thunderstorms, rain, severe weather) based on the interaction of temperature, moisture, instability, and forcing mechanisms |

### Research for Lesson
- How Weather Works — reference materials and textbook resources
- Chaos Theory and Weather — reference materials and textbook resources
- Modern Weather Forecasting — reference materials and textbook resources
- Forecast Accuracy by Lead Time — reference materials and textbook resources

---

## Step 1: LOCATE — Build Your System

### Text Editor

```
WHY CAN'T WEATHER APPS GET IT RIGHT?

Modeling Atmospheric Systems, Chaos Theory, and the Limits of Prediction.
If we have supercomputers, satellites, and thousands of weather stations, why is a 10-day forecast still barely better than a coin flip?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Solar Radiation Input" — the amount of solar energy reaching the surface
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Air Temperature" — the temperature of the air mass
  ○ Click "Moisture Content" — the amount of water vapor in the air
  ○ Click "Wind Speed" — the velocity of air movement
  ○ Click "Storm Probability" — the likelihood of significant weather events (thunderstorms

Task B: ADD TO YOUR MODEL
• Click the PLUS (+) button to add each component to your picture
• You should now see 5 components on your canvas

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
"If we have supercomputers, satellites, and thousands of weather stations, why is a 10-day forecast still barely better than a coin flip?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Solar Radiation Input' — that's external. The amount of solar energy reaching the surface.
Click on 'Air Temperature' — that's internal. The temperature of the air mass.
Click on 'Moisture Content' — that's internal. The amount of water vapor in the air.
Click on 'Wind Speed' — that's internal. The velocity of air movement.
Click on 'Storm Probability' — that's internal. The likelihood of significant weather events (thunderstorms.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Solar Radiation Input is the external component because it is the energy source that drives all atmospheric processes and varies based on astronomical and geographic factors independent of the atmosphere itself. Air Temperature, Moisture Content, Wind Speed, and Storm Probability are internal because they are atmospheric responses that emerge from the complex interactions driven by solar energy — they cannot be independently controlled but are determined by the physics of the atmospheric system.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next step, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 5 components sorted: Solar Radiation Input (External), Air Temperature, Moisture Content, Wind Speed, Storm Probability (Internal)]

### Graph
[Empty graph panel — no simulation yet]

---

## Step 2: ESTABLISH — Connect the Relationships

### Text Editor

```
TIME TO DRAW THE INVISIBLE LINES

Those 5 components don't just sit there — they AFFECT each other.
When one changes, others change too. Let's map those connections.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: OPEN CONNECTION MODE
• Click the "Connect" icon in the TOP LEFT corner of your screen
• Your cursor is now ready to draw relationship arrows

Task B: DRAW YOUR RELATIONSHIPS
• Click on "Solar Radiation Input" and drag an arrow to "Air Temperature"
• Click on "Air Temperature" and drag an arrow to "Wind Speed"
• Click on "Moisture Content" and drag an arrow to "Storm Probability"

Task C: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Solar Radiation Input → Air Temperature = POSITIVE (+)
    More solar radiation heats the surface and the air in contact with it. Differential heating by latitude, land/ocean, and cloud cover creates the temperature gradients that drive all atmospheric motion.

  ○ Air Temperature → Wind Speed = POSITIVE (+)
    Greater temperature differences between air masses create steeper pressure gradients, which drive stronger winds. Temperature is the engine; wind is the motion. Without temperature differences, there would be no wind.

  ○ Moisture Content → Storm Probability = POSITIVE (+)
    Higher moisture content provides more raw material for precipitation and more latent heat release during condensation. When moist air rises and cools, water vapor condenses, releasing energy that fuels thunderstorm updrafts, creating a positive feedback loop that intensifies storms.

Task D: CHECK YOUR MODEL
• You should have 3 arrows total
• 0 negative relationship(s), 3 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: If you change the Solar Radiation Input by just 1% in one location, the resulting temperature change alters wind patterns, which shifts moisture, which changes where storms form. How does this tiny initial difference grow into a completely different forecast?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Solar Radiation Input' and drag an arrow
over to 'Air Temperature.'

Here's the key question: When solar radiation input goes UP, does
air temperature go UP or DOWN?

More solar radiation heats the surface and the air in contact with it. Differential heating by latitude, land/ocean, and cloud cover creates the temperature gradients that drive all atmospheric motion.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Air Temperature' and drag an arrow
over to 'Wind Speed.'

Here's the key question: When air temperature goes UP, does
wind speed go UP or DOWN?

Greater temperature differences between air masses create steeper pressure gradients, which drive stronger winds. Temperature is the engine; wind is the motion. Without temperature differences, there would be no wind.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'Moisture Content' and drag an arrow
over to 'Storm Probability.'

Here's the key question: When moisture content goes UP, does
storm probability go UP or DOWN?

Higher moisture content provides more raw material for precipitation and more latent heat release during condensation. When moist air rises and cools, water vapor condenses, releasing energy that fuels thunderstorm updrafts, creating a positive feedback loop that intensifies storms.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Look at your model now. You've got 0 negative and 3
positive relationships. 3 arrows total.

If you change the Solar Radiation Input by just 1% in one location, the resulting temperature change alters wind patterns, which shifts moisture, which changes where storms form. How does this tiny initial difference grow into a completely different forecast?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Solar Radiation Input +→ Air Temperature, Air Temperature +→ Wind Speed, Moisture Content +→ Storm Probability]

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
• When Solar Radiation Input is HIGH, what happens to the internal components?

Task C: SCENARIO — SUNNY AND STABLE
• Solar Radiation: Moderate | Air: Dry and stable
• PREDICT FIRST: What do you predict Storm Probability will be under clear, stable conditions?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task D: SCENARIO — APPROACHING FRONT
• Solar Radiation: Strong | Moisture: High and rising
• PREDICT FIRST: When warm, moist air meets strong solar heating, what do you predict happens to Storm Probability?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task E: SCENARIO — BUTTERFLY EFFECT
• Two runs with 0.1% difference in Solar Radiation
• PREDICT FIRST: How different do you predict the weather forecasts will be after 3, 7, and 14 simulated days?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Weather is driven by energy transfers — solar radiation heats the surface unevenly, creating temperature differences that drive wind, which carries moisture, which produces precipitation
• The atmosphere is a chaotic system — tiny measurement errors in initial conditions amplify over time, making long-range forecasts fundamentally unreliable beyond about 10-14 days
• Storm formation requires the simultaneous interaction of multiple factors: instability, moisture, lifting mechanism, and wind shear — missing any one ingredient dramatically reduces storm probability
• Weather prediction accuracy decreases predictably: 1-day forecasts are about 95% accurate, 5-day about 80%, 10-day about 50%, and beyond 14 days, forecasts provide little useful information

THE ANSWER: Weather apps struggle with accuracy because the atmosphere is a chaotic system — mathematically, this means tiny measurement errors in today's conditions grow exponentially over time until the forecast becomes meaningless. Even with millions of data points from satellites, weather balloons, and ground stations, we can't measure EVERYTHING with perfect precision. A temperature measurement off by 0.01°C in one location can cascade through the atmospheric equations and produce a completely different forecast a week later. This isn't a technology problem — it's a fundamental mathematical limit discovered by Edward Lorenz in 1961. We'll never have a perfectly accurate 14-day forecast, no matter how powerful our computers become.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Sunny and Stable. Solar Radiation: Moderate | Air: Dry and stable.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Approaching Front.
Solar Radiation: Strong | Moisture: High and rising.

Before you run it — make a prediction. When warm, moist air meets strong solar heating, what do you predict happens to Storm Probability?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Butterfly Effect. Two runs with 0.1% difference in Solar Radiation.
How different do you predict the weather forecasts will be after 3, 7, and 14 simulated days?

Here's what our model reveals: Weather apps struggle with accuracy because the atmosphere is a chaotic system — mathematically, this means tiny measurement errors in today's conditions grow exponentially over time until the forecast becomes meaningless. Even with millions of data points from satellites, weather balloons, and ground stations, we can't measure EVERYTHING with perfect precision. A temperature measurement off by 0.01°C in one location can cascade through the atmospheric equations and produce a completely different forecast a week later. This isn't a technology problem — it's a fundamental mathematical limit discovered by Edward Lorenz in 1961. We'll never have a perfectly accurate 14-day forecast, no matter how powerful our computers become.

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
   • What happens if you turn OFF Solar Radiation Input?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Pressure Gradient — The difference in atmospheric pressure between two locations, which directly drives wind speed and direction — steeper gradients produce stronger winds and more dynamic weather
   • Wind Shear — The change in wind speed or direction with altitude, which is critical for severe weather development — strong wind shear helps organize thunderstorms into supercells capable of producing tornadoes
   • Land-Ocean Contrast — The difference in heating rate between land and water surfaces, which creates sea breezes, monsoons, and coastal weather patterns that complicate forecasting

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • How Weather Works — how does this connect to your model?
   • Chaos Theory and Weather — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model demonstrate that weather is a chaotic system where small changes produce large effects?
   • Why does the butterfly effect set a fundamental limit on forecast accuracy that better technology cannot overcome?
   • What does the model reveal about why severe weather forecasting is harder than fair-weather forecasting?
   • How could understanding chaos theory help people make better decisions about weather-dependent activities?

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

Your model has 5 components. Real systems involve
way more. Think about...

Pressure Gradient. The difference in atmospheric pressure between two locations, which directly drives wind speed and direction — steeper gradients produce stronger winds and more dynamic weather
How would you model that?

Wind Shear. The change in wind speed or direction with altitude, which is critical for severe weather development — strong wind shear helps organize thunderstorms into supercells capable of producing tornadoes
How would you model that?

Land-Ocean Contrast. The difference in heating rate between land and water surfaces, which creates sea breezes, monsoons, and coastal weather patterns that complicate forecasting
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

Meteorologists study atmospheric science and forecast weather using computational models, satellite data, and field observations. They work for the National Weather Service, media organizations, private weather companies, and aviation, earning $55,000–$120,000/year. Atmospheric Scientists who research climate modeling and chaos theory earn $70,000–$140,000/year.

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
Visual: Title slide with dramatic storm imagery
Say: "Your weather app says 70% chance of rain on Saturday. Saturday comes — it's sunny. Why? The answer involves one of the deepest discoveries in mathematics."
Do: Quick poll: How far into the future do you trust a weather forecast? 1 day? 3 days? 7 days? Record responses.
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and vocabulary
Say: "Today we're discovering WHY weather is so hard to predict — and it's not because meteorologists are bad at their jobs."
Do: Have students read objectives. Pre-teach 'atmospheric convection' and 'sensitive dependence' with visual demonstrations.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: Supercomputers vs. 10-day forecasts — why can't we win?
Say: "We have satellites watching every inch of the planet and supercomputers doing quadrillions of calculations per second. So why can't we get a 14-day forecast right?"
Do: Students hypothesize: Is it bad technology? Not enough data? Or something more fundamental?
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps overview
Say: "We're building a model of the atmosphere and then deliberately breaking it to discover the limits of predictability."
Do: Preview LEVER steps. Emphasize that we're testing the LIMITS of the model, not just how it works.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Component cards for atmospheric model
Say: "What factors drive weather? Which one is the ultimate energy source for ALL atmospheric motion?"
Do: Guide sorting. Solar radiation is the only external input — everything else responds to it. Discuss why.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows between atmospheric variables
Say: "The sun heats the surface unevenly. That creates temperature differences. Temperature differences create wind. Wind carries moisture. Moisture creates storms. It's all connected."
Do: Build the energy cascade from solar input to storms. Emphasize that every variable affects every other.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Diverging forecast comparison graphs
Say: "Now the fun part — let's change ONE number by 0.1% and see what happens to the 10-day forecast."
Do: Students predict whether 0.1% matters. Run twin simulations. Watch the forecasts diverge. This is the butterfly effect.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Forecast accuracy decay curve
Say: "Edward Lorenz discovered this in 1961 by accident. He rounded a number from 0.506127 to 0.506, and the entire weather forecast changed. That 0.02% difference rewrote the future."
Do: Show the accuracy decay curve: 95% at 1 day, 80% at 5 days, 50% at 10 days. Discuss the theoretical 2-3 week limit.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Severe weather alert system design
Say: "If you can't predict far ahead, you need to detect FAST. Design a system that gives your school maximum warning time for severe storms."
Do: Groups design alert systems specifying sensors, thresholds, communication channels, and false alarm mitigation.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: Why Can't Weather Apps Get It Right?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
In 1961, meteorologist Edward Lorenz accidentally discovered one of the most profound principles in science. While running a weather simulation, he rounded an initial value from 0.506127 to 0.506 — a difference of less than 0.02%. The resulting forecast was completely different. This discovery — sensitive dependence on initial conditions — revealed that the atmosphere is a chaotic system with a fundamental prediction limit that no technology can ever overcome.

NGSS ALIGNMENT:
HS-ESS2-5, HS-ESS2-3: Plan and conduct an investigation of the properties of water and its effects on Earth materials and surface processes. Develop a model based on evidence of Earth's interior to describe the cycling of matter by thermal convection.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Planning and Carrying Out Investigations
  Students plan investigations to test how varying initial conditions in their atmospheric model affect forecast outcomes, demonstrating sensitive dependence.
• Disciplinary Core Idea: ESS2.D Weather and Climate
  The foundation for Earth's global climate system is the electromagnetic radiation from the sun and its interaction with Earth's surface and atmosphere. Weather results from complex interactions among atmospheric variables driven by solar energy.
• Crosscutting Concept: Cause and Effect
  Students investigate how small causes (tiny measurement errors) can produce large, unpredictable effects in complex systems, distinguishing deterministic chaos from randomness.

PACING GUIDE:
• Step 1 (Locate): 8-10 minutes
• Step 2 (Establish): 8-10 minutes
• Step 3 (Visualize & Evaluate): 10-12 minutes
• Step 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Atmospheric Convection, Sensitive Dependence, Relative Humidity, Atmospheric Instability
□ Prepare If we have supercomputers, satellites, and thousands of weather stations, why is a 10-day forecast still barely better than a coin flip discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify solar radiation input, air temperature, moisture content, wind speed, and storm probability as the key components of the atmospheric weather system.
• Establish: Students determine that solar radiation drives temperature, temperature differences drive wind, wind transports moisture, and the interaction of all four factors determines storm probability.
• Visualize: Students build a computational model showing how atmospheric variables interact to produce weather patterns and how tiny changes in initial conditions cascade into different forecasts.
• Evaluate: Students run stable weather, approaching front, and butterfly effect scenarios to discover the limits of predictability in chaotic atmospheric systems.
• Revise: Students add pressure gradient, wind shear, or land-ocean contrast to model more realistic atmospheric dynamics.

BACKGROUND CONTENT:
• How Weather Works:
  All weather is driven by differential solar heating. The equator receives more solar energy per square meter than the poles, creating temperature gradients that drive atmospheric circulation. Warm air rises (convection), creating low pressure at the surface. Cool air sinks, creating high pressure. Air flows from high to low pressure (wind), carrying moisture evaporated from oceans. When moist air rises and cools, water vapor condenses into clouds and precipitation. This cycle — heating, convection, moisture transport, condensation — produces all weather.

• Chaos Theory and Weather:
  Chaotic systems are deterministic (governed by fixed physical laws) but unpredictable beyond a certain time horizon because they exhibit sensitive dependence on initial conditions. In the atmosphere, this means that two nearly identical starting states will diverge exponentially over time. The 'Lyapunov time' for the atmosphere — how long before small errors double — is approximately 2-3 days. After 5 doublings (~10-15 days), initial measurement errors have grown to the size of the weather features themselves, making the forecast meaningless.

• Modern Weather Forecasting:
  Today's forecasts use numerical weather prediction (NWP): supercomputers solve the Navier-Stokes equations and thermodynamic equations on a 3D grid covering the globe. Models divide the atmosphere into millions of cells, each about 3-10 km across and hundreds of meters tall. Every cell's temperature, pressure, humidity, and wind are updated every few minutes. To address chaos, forecasters run 'ensemble models' — 20-50 slightly different versions of the same forecast — and analyze how much they diverge to estimate confidence.

• Forecast Accuracy by Lead Time:
  Modern 1-day forecasts are about 95% accurate — essentially as good as they can get. 3-day forecasts are about 90% accurate, comparable to what 1-day forecasts were in the 1980s. 5-day forecasts are about 80% accurate, rivaling 3-day forecasts from 20 years ago. Beyond 10 days, accuracy drops below 60%. Beyond 14 days, forecasts provide only marginal improvement over using historical climate averages. The theoretical maximum useful forecast for the atmosphere is approximately 2-3 weeks.

COMMON MISCONCEPTIONS:
• "Weather apps are inaccurate because meteorologists are bad at their jobs"
  Reality: Modern weather forecasting is one of the greatest achievements of computational science. A 5-day forecast today is as accurate as a 1-day forecast was in the 1980s. The remaining inaccuracy isn't due to incompetence — it's due to chaos theory, a fundamental mathematical property of the atmospheric equations. No amount of skill can overcome the butterfly effect beyond approximately 2 weeks.
  Strategy: Show the improvement graph: 1-day forecast accuracy has gone from ~70% in 1970 to ~95% today. 5-day forecasts have improved from ~40% to ~80%. Progress is real but asymptotic — approaching a mathematical limit.

• "If we had enough data and computing power, we could predict weather perfectly"
  Reality: This is the fundamental insight of chaos theory: perfect prediction requires perfect measurements of initial conditions, which is physically impossible. The atmosphere has approximately 10^44 molecules, each with position and velocity that would need to be measured with infinite precision. Even quantum mechanics (Heisenberg's uncertainty principle) prevents measurements below certain precision limits. Better computers and data improve short-range forecasts but cannot extend the fundamental prediction horizon.
  Strategy: Thought experiment: To perfectly predict the weather 30 days out, you would need to account for every molecule of air on Earth. How many sensors would that require? More than the number of atoms in the sensor material itself — it's a logical impossibility.

• "Climate can't be predicted if weather can't"
  Reality: Weather and climate are fundamentally different prediction problems. Weather is about the specific state of the atmosphere on a specific day — chaotic and unpredictable beyond ~2 weeks. Climate is about the statistical average of weather over decades — driven by well-understood energy balance physics and highly predictable. You can't predict which coin flip will be heads, but you can confidently predict that 1,000 flips will be close to 50% heads.
  Strategy: Analogy: You can't predict exactly when a specific person will die (chaotic individual variation), but you can predict average life expectancy for a population with great accuracy (statistical trends). Climate prediction works the same way.

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
Big Question: If we have supercomputers, satellites, and thousands of weather stations, why is a 10-day forecast still barely better than a coin flip?
Answer: Weather apps struggle with accuracy because the atmosphere is a chaotic system — mathematically, this means tiny measurement errors in today's conditions grow exponentially over time until the forecast becomes meaningless. Even with millions of data points from satellites, weather balloons, and ground stations, we can't measure EVERYTHING with perfect precision. A temperature measurement off by 0.01°C in one location can cascade through the atmospheric equations and produce a completely different forecast a week later. This isn't a technology problem — it's a fundamental mathematical limit discovered by Edward Lorenz in 1961. We'll never have a perfectly accurate 14-day forecast, no matter how powerful our computers become.

Simulation Answers:
• Approaching Front Scenario: When Moisture Content is high and Solar Radiation Input is strong, the model shows air temperature rising significantly, creating instability. Warm, moist air at the surface is overlain by cooler air aloft, promoting rapid convection. Wind speed increases as pressure gradients steepen. Storm Probability rises sharply as all ingredients for severe weather converge: instability, moisture, and lift. The model produces thunderstorm development within hours.
• Butterfly Effect Scenario: Two simulations run with Solar Radiation Input differing by just 0.1% produce nearly identical forecasts for the first 2-3 simulated days. By day 5, the forecasts begin to noticeably diverge — one predicts rain where the other predicts sun. By day 10, the forecasts are essentially unrelated — predicting different temperatures, wind patterns, and storm locations. This demonstrates that deterministic chaos makes long-range weather prediction fundamentally limited regardless of computational power.

Reflection Exemplars:
• Q: Why can't better technology solve this?
  A: The butterfly effect isn't a technology problem — it's a mathematical property of the atmospheric equations themselves. Even with perfect sensors measuring every molecule of air, the equations are chaotic: they amplify infinitesimally small differences exponentially over time. To produce a perfect 14-day forecast, you would need to measure the position and velocity of every molecule in the atmosphere with perfect precision — which is physically impossible (and forbidden by quantum mechanics at the smallest scales). Better computers improve short-range forecasts but cannot extend the fundamental predictability horizon.
• Q: How is chaos different from randomness?
  A: Chaotic systems are deterministic — they follow exact physical laws and the same initial conditions always produce the same result. They're not random. The problem is that infinitely small differences in initial conditions produce different results, and we can never measure initial conditions with infinite precision. Weather is governed by the Navier-Stokes equations — precise, deterministic physics — but the solutions to those equations diverge exponentially from nearby starting points. Randomness means no rules; chaos means rules that are exquisitely sensitive.

STEM CHALLENGE GUIDANCE:
Title: Design a Severe Weather Alert System
Mission: Design a localized severe weather monitoring and alert system that maximizes warning time for thunderstorms and tornadoes while minimizing false alarms.
Scenario: A school district in an area prone to severe thunderstorms and occasional tornadoes needs a better warning system than just watching the news. The current system provides only 13 minutes of average tornado warning time, and false alarms have trained people to ignore alerts. Your team must design a monitoring system that provides earlier, more accurate warnings for the school and surrounding community.
Introduction: Present the challenge: A school district needs a severe weather alert system that provides maximum warning time for thunderstorms and tornadoes while avoiding the false alarm fatigue that makes people ignore alerts. Your team will design the monitoring sensors, alert thresholds, communication channels, and validation protocols.

Key Concepts:
• Nowcasting: Very short-term forecasting (0-6 hours) that uses real-time observations — radar, satellite, lightning detection — rather than model predictions. Nowcasting is much more accurate than longer-range forecasting because it detects weather that has already formed rather than predicting weather that hasn't.
• Ensemble Forecasting: Running 20-50 slightly different versions of the same weather model to see how much the forecasts diverge. When all ensemble members agree, confidence is high. When they spread widely, uncertainty is high. This converts the chaos problem into a probability estimate.
• False Alarm Mitigation: When false alarm rates are too high, people stop responding to real alerts (the 'cry wolf' effect). The National Weather Service aims for a tornado warning false alarm rate of 70% — meaning 7 out of 10 tornado warnings are false alarms. Reducing this rate while maintaining detection capability is a critical engineering challenge.

Evaluation Rubric:
• Expert (4): System combines multiple data sources, specifies evidence-based alert thresholds, addresses false alarm rates with quantitative targets, includes communication redundancy, and uses model evidence to justify design decisions
• Proficient (3): System identifies appropriate data sources and alert thresholds with reasonable false alarm consideration
• Developing (2): System identifies some monitoring needs but lacks specific thresholds or false alarm management
• Beginning (1): System is incomplete or doesn't connect atmospheric science to alert system design

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a severe weather ingredients checklist showing the atmospheric conditions that must combine for thunderstorm and tornado development
  • Use a forecast accuracy chart showing how accuracy decreases with lead time as a reference for system design decisions
  • Sentence frames: 'Our system triggers a __ alert when __ exceeds __ because our model shows this combination produces storms __% of the time'

Extensions (Advanced Learners):
  • Research Edward Lorenz's original 1963 paper on deterministic chaos — how did a weather simulation error lead to one of the most important discoveries in mathematics?
  • Investigate how artificial intelligence is being used to improve weather prediction — can machine learning extend the forecast horizon beyond the chaos theory limit?
  • Compare weather prediction to earthquake prediction — why can we forecast weather 5 days out but not earthquakes 5 minutes out?

Cross-Curricular Connections:
  • Math: Explore exponential growth of errors: If measurement error doubles every 2.5 days and starts at 0.01°C, calculate the error after 5, 10, and 15 days. At what point does the error exceed the size of the weather feature being predicted?
  • ELA: Write a public communication piece explaining why weather forecasts are probabilistic, not certain. Target an audience that gets frustrated when forecasts are 'wrong' and help them understand what a '70% chance of rain' actually means.
  • History: Research the Great Galveston Hurricane of 1900 (before modern forecasting killed 8,000 people) and compare to Hurricane Harvey in 2017 (advanced warning saved thousands). How much have forecasting improvements reduced weather-related deaths?

CAST ALIGNMENT:
• Model how atmospheric variables interact to produce weather patterns and storm formation
• Demonstrate the butterfly effect by comparing forecasts from slightly different initial conditions
• Analyze why weather forecast accuracy decreases predictably with forecast lead time

CAST-Style Assessment Questions:
• Multiple Choice: A meteorologist runs two computer forecasts with initial temperatures differing by only 0.01°C. The 3-day forecasts are nearly identical, but the 10-day forecasts predict completely different weather. This is best explained by:
• Constructed Response: Using your model, explain why it is mathematically impossible to produce an accurate 30-day weather forecast even with perfect technology. Include the concepts of sensitive dependence, measurement uncertainty, and chaotic systems in your explanation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: Why Can't Weather Apps Get It Right?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Why do you think weather forecasts become less accurate for days further in the future?

   _________________________________________________________

   _________________________________________________________

2. What information do you think meteorologists use to predict tomorrow's weather?

   _________________________________________________________

   _________________________________________________________

3. Draw a diagram showing how you think a thunderstorm forms — what ingredients are needed?

   [DRAWING BOX]

4. Have you ever heard of the 'butterfly effect'? What do you think it means for weather prediction?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Atmospheric Convection        
___ Sensitive Dependence          
___ Relative Humidity             
___ Atmospheric Instability       

A. The vertical movement of air caused by differential heating — warm air rises, expands, and cools; cool air sinks, compresses, and warms. This cycling drives weather patterns from local thunderstorms to global circulation cells
B. The mathematical property of chaotic systems where tiny differences in starting conditions lead to vastly different outcomes over time — popularly called the 'butterfly effect' in weather forecasting
C. The amount of water vapor in the air expressed as a percentage of the maximum the air could hold at that temperature — warm air can hold more moisture, so cooling air causes humidity to rise toward saturation and precipitation
D. A condition where warm, moist air near the surface is overlain by cooler, drier air above — this temperature structure promotes rapid vertical convection and can trigger thunderstorms

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

SCENARIO: Sunny and Stable
Settings: Solar Radiation: Moderate | Air: Dry and stable
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Approaching Front
Settings: Solar Radiation: Strong | Moisture: High and rising
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Butterfly Effect
Settings: Two runs with 0.1% difference in Solar Radiation
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

1. How does your model demonstrate that weather is a chaotic system where small changes produce large effects?

   _________________________________________________________

   _________________________________________________________

2. Why does the butterfly effect set a fundamental limit on forecast accuracy that better technology cannot overcome?

   _________________________________________________________

   _________________________________________________________

3. What does the model reveal about why severe weather forecasting is harder than fair-weather forecasting?

   _________________________________________________________

   _________________________________________________________

4. How could understanding chaos theory help people make better decisions about weather-dependent activities?

   _________________________________________________________

   _________________________________________________________

5. What are the limitations of modeling the atmosphere with only five components?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. If we have supercomputers, satellites, and thousands of weather stations, why is a 10-day forecast still barely better than a coin flip? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Planning and Carrying Out Investigations
   □ Disciplinary Core Idea: ESS2.D Weather and Climate
   □ Crosscutting Concept: Cause and Effect

3. What are the limitations of modeling the atmosphere with only five components?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Severe Weather Alert System
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design a localized severe weather monitoring and alert system that maximizes warning time for thunderstorms and tornadoes while minimizing false alarms.

SCENARIO: A school district in an area prone to severe thunderstorms and occasional tornadoes needs a better warning system than just watching the news. The current system provides only 13 minutes of average tornado warning time, and false alarms have trained people to ignore alerts. Your team must design a monitoring system that provides earlier, more accurate warnings for the school and surrounding community.

GUIDING QUESTIONS:
• What atmospheric variables does your system monitor and what thresholds trigger alerts?
• How will you balance early warnings (more lead time) against false alarm rates (crying wolf)?
• What data sources will you combine for the most accurate short-term predictions?

DESIGN THINKING:
• What sensors and data sources will your system use and where will they be placed?

  _________________________________________________________

• How will you define alert thresholds that maximize warning time without triggering too many false alarms?

  _________________________________________________________

• What communication channels will you use to reach students, staff, and the community quickly?

  _________________________________________________________

• How will you test and validate your system before relying on it for safety?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): System combines multiple data sources, specifies evidence-based alert thresholds, addresses false alarm rates with quantitative targets, includes communication redundancy, and uses model evidence to justify design decisions
• Proficient (3): System identifies appropriate data sources and alert thresholds with reasonable false alarm consideration
• Developing (2): System identifies some monitoring needs but lacks specific thresholds or false alarm management
• Beginning (1): System is incomplete or doesn't connect atmospheric science to alert system design

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CAST-Aligned Pre/Post Assessment

### Administration Instructions

These 5 multiple-choice questions are administered identically as both a pre-assessment (before Activity 1) and a post-assessment (after Activity 4). Score each out of 5. Learning growth = post-score minus pre-score.

Questions follow the California Science Test (CAST) stimulus-response format. Each item is three-dimensional, assessing a Science and Engineering Practice (SEP), Disciplinary Core Idea (DCI), and Crosscutting Concept (CCC) simultaneously, aligned to HS-ESS2-5, HS-ESS2-3.

---

### Question 1

CAST Alignment: SEP 2.1.1 (Determine components of a system) + DCI ESS2.5 + CCC4 (Systems and System Models)

A student is using the ModelIt platform to study the system in this lesson. The model includes these components: Solar Radiation Input, Air Temperature, Moisture Content, Wind Speed, Storm Probability. Some components are external (Solar Radiation Input) and some are internal (Air Temperature, Moisture Content, Wind Speed, Storm Probability). The student needs to understand what each component represents and how they are organized.

In the Butterfly Effect Test scenario, two model runs with Solar Radiation differing by only 0.1% produce nearly identical 3-day forecasts but completely different 10-day forecasts. What mathematical property of the atmosphere does this demonstrate?

A. Deterministic chaos, where the system follows precise physical laws but small initial differences grow exponentially, making long-range prediction impossible.
B. Measurement instruments are too imprecise for useful forecasting.
C. The model is flawed because a 0.1% change should not affect the forecast.
D. The atmosphere follows random, unpredictable behavior at all timescales.

Correct Answer: A

Feedback: Correct. This demonstrates deterministic chaos: the system obeys exact physical laws (it is not random), but infinitesimal differences in starting conditions amplify exponentially, producing divergent outcomes after several days. If you chose D, the model shows a clear, predictable pattern. The relationships between components are consistent — they always work the same way when conditions change. If you chose B, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose C, the model shows these components ARE connected. When one changes, it affects the others through the relationships (positive or negative) that you mapped in the model.
---

### Question 2

CAST Alignment: SEP 2.1.2 (Determine relationships among components) + DCI ESS2.5 + CCC4 (Systems and System Models)

In the computational model for this lesson, a student draws arrows between components to show relationships. The model shows that when Solar Radiation Input increases, Air Temperature increases; when Air Temperature increases, Wind Speed increases. The student is trying to understand why these relationships are positive or negative.

The model shows that Storm Probability increases when high Moisture Content coincides with strong Solar Radiation. A student asks why deserts have strong solar radiation but few thunderstorms. Which model component explains this?

A. Wind Speed, because deserts have too much wind for storms to form.
B. Air Temperature, because deserts are too hot for storms.
C. Moisture Content, because storms require simultaneous presence of multiple ingredients, and deserts lack sufficient atmospheric moisture despite having strong solar heating.
D. Solar Radiation Input, which is actually weaker in deserts than other regions.

Correct Answer: C

Feedback: Correct. The model demonstrates that storm formation requires MULTIPLE ingredients simultaneously. Deserts have strong heating but lack moisture. Without sufficient moisture, atmospheric instability alone cannot produce storms. If you chose A, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose B, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows.
---

### Question 3

CAST Alignment: SEP 2.1.3 (Evaluate a model's accuracy) + DCI ESS2.5 + CCC4 (Systems and System Models)

A student runs a simulation of the model. The model shows that when Solar Radiation Input increases, Air Temperature increases and when Air Temperature increases, Wind Speed increases and when Moisture Content increases, Storm Probability increases. The student changes one variable to see how the whole system responds.

Based on the model's forecast accuracy decay curve (95% at 1 day, 80% at 5 days, 50% at 10 days), a technology company claims its new AI system will produce accurate 30-day forecasts. What does the model's chaos theory framework predict about this claim?

A. AI would only need slightly more data to achieve 30-day accuracy.
B. The claim violates the fundamental predictability limit of chaotic atmospheric systems. No technology can extend useful forecasts beyond approximately 2-3 weeks.
C. The model cannot evaluate this claim because it doesn't include AI.
D. AI could achieve this because it can process data faster than traditional models.

Correct Answer: B

Feedback: Correct. The theoretical predictability limit for the atmosphere (~2-3 weeks) is a mathematical property of the chaotic equations, not a technology limitation. No computational advancement can overcome this fundamental boundary. If you chose D, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose A, this answer suggests something is being added to the system. Look carefully at the model — the total amount stays the same even when components change. The system is conserving matter or energy. If you chose C, the model shows these components ARE connected. When one changes, it affects the others through the relationships (positive or negative) that you mapped in the model.
---

### Question 4

CAST Alignment: SEP 2.1.4 (Represent mechanisms to explain/predict events) + DCI ESS2.5 + CCC4 (Systems and System Models)

Scientists are studying data related to this system. They collected observations over time and noticed patterns in how the components change. The data shows how changes in one part of the system cascade through the other parts.

The model demonstrates that all five atmospheric variables (solar radiation, temperature, moisture, wind, storm probability) interact with each other. Why does this interconnection make weather prediction particularly challenging?

A. It means only one variable needs to be measured accurately for a good forecast.
B. Only temperature and moisture interact; the other variables are independent.
C. The interactions cancel each other out, making the system simpler than it appears.
D. Each variable's error feeds into every other variable's calculation, causing errors to compound and propagate through the entire system simultaneously.

Correct Answer: D

Feedback: Correct. In an interconnected system, measurement errors in ANY variable propagate to ALL other variables through their interactions. This error propagation compounds exponentially in a chaotic system. If you chose A, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose C, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose B, the model shows these components ARE connected. When one changes, it affects the others through the relationships (positive or negative) that you mapped in the model.
---

### Question 5

CAST Alignment: SEP 2.1.5 (Apply a model to make predictions) + DCI ESS2.5 + CCC4 (Systems and System Models)

A team wants to use the model to solve a real-world problem related to this system. They know they cannot control the external components (Solar Radiation Input), but they can take action on internal components (Air Temperature, Moisture Content, Wind Speed, Storm Probability). They need to decide which action would be most effective based on what the model shows.

A school principal wants to know if it will rain during an outdoor event in 14 days. Based on the model's findings about forecast accuracy, which recommendation is most scientifically sound?

A. Check the 14-day forecast now and plan accordingly.
B. The model shows that 14-day rain predictions are 90% accurate, so trust the current forecast.
C. 14-day forecasts are unreliable. Plan for both scenarios now, and check 3-5 day forecasts closer to the event for a more accurate prediction.
D. Weather 14 days out is completely random, so there is no useful information available.

Correct Answer: C

Feedback: Correct. The model shows 14-day forecasts are near the predictability limit and barely better than climatological averages. The scientifically sound approach is flexible planning now with decision-making based on more accurate 3-5 day forecasts. If you chose A, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, the model shows these components ARE connected. When one changes, it affects the others through the relationships (positive or negative) that you mapped in the model. If you chose B, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows.
---

### Answer Key

Question 1: A (Cognitive Level: Identify — SEP 2.1.1, DCI ESS2.5, CCC4)
Question 2: C (Cognitive Level: Reason — SEP 2.1.2, DCI ESS2.5, CCC4)
Question 3: B (Cognitive Level: Reason — SEP 2.1.3, DCI ESS2.5, CCC4)
Question 4: D (Cognitive Level: Reason + Evidence — SEP 2.1.4, DCI ESS2.5, CCC4)
Question 5: C (Cognitive Level: Predict + Apply — SEP 2.1.5, DCI ESS2.5, CCC4)


## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-10/G10L1-L07/G10L1-L07-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-10/G10L1-L07/G10L1-L07-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-10/G10L1-L07/G10L1-L07-Student-Presentation.pptx] |
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