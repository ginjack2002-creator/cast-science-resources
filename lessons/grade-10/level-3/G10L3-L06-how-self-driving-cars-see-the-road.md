# Lesson: How Self-Driving Cars See the Road

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G10L3-L06 |
| **Grade** | 10th Grade — Level 3: Advanced Engineering & Design |
| **Lesson Name** | How Self-Driving Cars See the Road |
| **Status** | Template |

---

## Platform

### Title
**How Self-Driving Cars See the Road — Modeling the Sensor Fusion and Decision Systems of Autonomous Vehicles**

### Overview
Human drivers kill over 40,000 people per year in the United States alone, with 94% of crashes caused by human error — distraction, impairment, fatigue, and poor judgment. Autonomous vehicles promise to eliminate these errors with sensors that never blink, algorithms that never get tired, and reaction times five times faster than humans. But replacing human perception and decision-making with technology is one of the hardest engineering challenges ever attempted. Students investigate the driving question: How does a car with no human driver detect, identify, and react to dangers faster than any human — and why does it still sometimes fail? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of an autonomous vehicle on a city street with visible sensor visualization overlays — LIDAR point clouds in blue, radar fields in green, camera vision cones in yellow — showing how the car perceives its 360-degree environment]

### Grade
10th Grade — Level 3: Advanced Engineering & Design

### NGSS Standard
**HS-PS4-2, HS-PS4-5**: Evaluate questions about the advantages of using digital transmission and storage of information. Communicate technical information about how some technological devices use the principles of wave behavior and wave interactions with matter to transmit and capture information and energy.

### Learning Objectives
- Model how nine sensor and decision-making variables interact to enable autonomous vehicle navigation
- Analyze the engineering trade-offs between sensor range, processing speed, and decision accuracy in self-driving systems
- Evaluate why sensor fusion — combining multiple data sources — is more reliable than any single sensor alone
- Predict the conditions under which autonomous driving systems fail and how those failures can be mitigated

### Component List (Starting Model: 9 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| LIDAR Pulse Frequency | External | The rate at which the LIDAR sensor fires laser pulses, determining the density and update rate of the 3D point cloud — higher frequency provides more detailed and current environmental mapping |
| Detection Range | Internal | The maximum distance at which the sensor suite can reliably detect and classify objects — longer range provides more reaction time but requires more processing power and higher-quality sensors |
| Signal Processing Speed | Internal | The rate at which raw sensor data is converted into usable environmental information — measured in frames per second for cameras and points per second for LIDAR |
| Obstacle Classification | Internal | The accuracy with which the system identifies detected objects — distinguishing a pedestrian from a mailbox, a bicycle from a motorcycle, or a plastic bag from a boulder |
| Weather Interference | External | The degree to which rain, fog, snow, dust, or direct sunlight degrades sensor performance — LIDAR scatters in rain, cameras blur in fog, radar reflects off wet surfaces |
| Decision Latency | Internal | The total time from detection to vehicle response — including perception processing, path planning, and actuator activation |
| Sensor Fusion Accuracy | Internal | The quality of the combined perception model created by integrating LIDAR, camera, radar, and ultrasonic data — higher accuracy means fewer misclassifications and missed detections |
| Route Optimization | Internal | The efficiency of the path-planning algorithm in selecting the safest and most efficient route, accounting for traffic, road conditions, construction zones, and real-time hazards |
| Safety Margin | Internal | The buffer distance and time the system maintains beyond the minimum required for safe operation — larger margins provide more room for error but may reduce efficiency and traffic flow |

### Research for Lesson
- The Sensor Stack — reference materials and textbook resources
- Sensor Fusion: The Key Innovation — reference materials and textbook resources
- The Decision Pipeline — reference materials and textbook resources
- The Edge Case Problem — reference materials and textbook resources

---

## Step 1: LOCATE — Build Your System

### Text Editor

```
HOW SELF-DRIVING CARS SEE THE ROAD

Modeling the Sensor Fusion and Decision Systems of Autonomous Vehicles.
How does a car with no human driver detect, identify, and react to dangers faster than any human — and why does it still sometimes fail?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "LIDAR Pulse Frequency" — the rate at which the lidar sensor fires laser pulses
  ○ Click "Weather Interference" — the degree to which rain
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Detection Range" — the maximum distance at which the sensor suite can reliably detect and classify objects — longer range provides more reaction time but requires more processing power and higher-quality sensors
  ○ Click "Signal Processing Speed" — the rate at which raw sensor data is converted into usable environmental information — measured in frames per second for cameras and points per second for lidar
  ○ Click "Obstacle Classification" — the accuracy with which the system identifies detected objects — distinguishing a pedestrian from a mailbox
  ○ Click "Decision Latency" — the total time from detection to vehicle response — including perception processing
  ○ Click "Sensor Fusion Accuracy" — the quality of the combined perception model created by integrating lidar
  ○ Click "Route Optimization" — the efficiency of the path-planning algorithm in selecting the safest and most efficient route
  ○ Click "Safety Margin" — the buffer distance and time the system maintains beyond the minimum required for safe operation — larger margins provide more room for error but may reduce efficiency and traffic flow

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
"How does a car with no human driver detect, identify, and react to dangers faster than any human — and why does it still sometimes fail?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'LIDAR Pulse Frequency' — that's external. The rate at which the LIDAR sensor fires laser pulses.
Click on 'Detection Range' — that's internal. The maximum distance at which the sensor suite can reliably detect and classify objects — longer range provides more reaction time but requires more processing power and higher-quality sensors.
Click on 'Signal Processing Speed' — that's internal. The rate at which raw sensor data is converted into usable environmental information — measured in frames per second for cameras and points per second for LIDAR.
Click on 'Obstacle Classification' — that's internal. The accuracy with which the system identifies detected objects — distinguishing a pedestrian from a mailbox.
Click on 'Weather Interference' — that's external. The degree to which rain.
Click on 'Decision Latency' — that's internal. The total time from detection to vehicle response — including perception processing.
Click on 'Sensor Fusion Accuracy' — that's internal. The quality of the combined perception model created by integrating LIDAR.
Click on 'Route Optimization' — that's internal. The efficiency of the path-planning algorithm in selecting the safest and most efficient route.
Click on 'Safety Margin' — that's internal. The buffer distance and time the system maintains beyond the minimum required for safe operation — larger margins provide more room for error but may reduce efficiency and traffic flow.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

LIDAR Pulse Frequency is external because it is a direct hardware specification chosen during system design — the sensor fires at a rate determined by its engineering capabilities and power allocation. Weather Interference is external because it represents environmental conditions that the vehicle cannot control — rain, fog, snow, and sunlight affect sensor performance regardless of vehicle design. The remaining seven components are internal because they are system responses: Detection Range depends on sensor quality and weather, Signal Processing Speed is determined by onboard computing power interacting with data volume, Obstacle Classification emerges from the fusion algorithm's accuracy, and Decision Latency, Sensor Fusion Accuracy, Route Optimization, and Safety Margin are all determined by how the perception and planning systems perform under the given conditions.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next step, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 9 components sorted: LIDAR Pulse Frequency, Weather Interference (External), Detection Range, Signal Processing Speed, Obstacle Classification, Decision Latency, Sensor Fusion Accuracy, Route Optimization, Safety Margin (Internal)]

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
• Click on "LIDAR Pulse Frequency" and drag an arrow to "Detection Range"
• Click on "Weather Interference" and drag an arrow to "Sensor Fusion Accuracy"
• Click on "Sensor Fusion Accuracy" and drag an arrow to "Decision Latency"

Task C: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ LIDAR Pulse Frequency → Detection Range = POSITIVE (+)
    Higher pulse frequency creates denser point clouds that can resolve smaller and more distant objects, effectively extending the reliable detection range. At 300,000+ pulses per second, modern LIDAR can detect and classify objects at 200+ meters.

  ○ Weather Interference → Sensor Fusion Accuracy = NEGATIVE (−)
    Increased weather interference degrades individual sensor performance — LIDAR scatters in rain, cameras lose contrast in fog, radar gets surface reflections in snow. When multiple sensors degrade simultaneously, the fusion algorithm has fewer reliable data sources, reducing overall perception accuracy.

  ○ Sensor Fusion Accuracy → Decision Latency = NEGATIVE (−)
    Higher sensor fusion accuracy means the decision system receives clear, confident object classifications, enabling faster path planning. When accuracy drops due to weather or edge cases, the system requires additional processing cycles to resolve ambiguity, increasing total decision latency.

Task D: CHECK YOUR MODEL
• You should have 3 arrows total
• 2 negative relationship(s), 1 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: In heavy rain, LIDAR performance degrades, cameras struggle with visibility, and road markings become obscured. If Weather Interference is high, how does the system maintain reliable Obstacle Classification when its primary sensors are impaired? What role does Sensor Fusion play as a backup?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'LIDAR Pulse Frequency' and drag an arrow
over to 'Detection Range.'

Here's the key question: When lidar pulse frequency goes UP, does
detection range go UP or DOWN?

Higher pulse frequency creates denser point clouds that can resolve smaller and more distant objects, effectively extending the reliable detection range. At 300,000+ pulses per second, modern LIDAR can detect and classify objects at 200+ meters.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Weather Interference' and drag an arrow
over to 'Sensor Fusion Accuracy.'

Here's the key question: When weather interference goes UP, does
sensor fusion accuracy go UP or DOWN?

Increased weather interference degrades individual sensor performance — LIDAR scatters in rain, cameras lose contrast in fog, radar gets surface reflections in snow. When multiple sensors degrade simultaneously, the fusion algorithm has fewer reliable data sources, reducing overall perception accuracy.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Last connection: Click on 'Sensor Fusion Accuracy' and drag an arrow
over to 'Decision Latency.'

Here's the key question: When sensor fusion accuracy goes UP, does
decision latency go UP or DOWN?

Higher sensor fusion accuracy means the decision system receives clear, confident object classifications, enabling faster path planning. When accuracy drops due to weather or edge cases, the system requires additional processing cycles to resolve ambiguity, increasing total decision latency.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Look at your model now. You've got 2 negative and 1
positive relationships. 3 arrows total.

In heavy rain, LIDAR performance degrades, cameras struggle with visibility, and road markings become obscured. If Weather Interference is high, how does the system maintain reliable Obstacle Classification when its primary sensors are impaired? What role does Sensor Fusion play as a backup?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: LIDAR Pulse Frequency +→ Detection Range, Weather Interference −→ Sensor Fusion Accuracy, Sensor Fusion Accuracy −→ Decision Latency]

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
• When LIDAR Pulse Frequency is HIGH, what happens to the internal components?

Task C: SCENARIO — CLEAR HIGHWAY
• Minimal weather interference, highway driving
• PREDICT FIRST: What do you predict the system's Detection Range and Decision Latency will be under ideal conditions?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task D: SCENARIO — HEAVY RAIN URBAN
• Heavy rain, complex urban intersection
• PREDICT FIRST: What do you predict happens to Obstacle Classification accuracy when LIDAR and cameras are degraded by rain?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task E: SCENARIO — EDGE CASE
• Unusual obstacle not in training data
• PREDICT FIRST: What do you predict the system does when it detects something it cannot classify with confidence?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Sensor fusion provides redundancy that no single sensor can match — when LIDAR fails in rain, radar takes over for distance measurement while cameras maintain object classification
• Decision Latency for autonomous systems (100-300 ms) is 5-10 times faster than human reaction time (1,500+ ms), but this advantage narrows significantly in complex, ambiguous situations requiring judgment
• Edge cases represent the fundamental challenge: autonomous systems excel at common scenarios but struggle with rare, novel situations that humans handle through general intelligence and common sense
• The Safety Margin variable reveals a deep engineering trade-off: larger margins make the car safer but also slower, less efficient, and more disruptive to traffic flow — finding the optimal margin is both an engineering and ethical question

THE ANSWER: Self-driving cars see the road through an array of complementary sensors. LIDAR creates a precise 3D map by firing thousands of laser pulses per second. Cameras provide color, texture, and sign-reading capability. Radar measures velocity and works in all weather. Sensor fusion algorithms combine these data streams into a unified perception model that is more reliable than any single sensor. The system then classifies every object, predicts its trajectory, plans a safe path, and executes — all in 100-300 milliseconds. It fails when sensors are all degraded simultaneously (heavy snow), when objects are genuinely novel (edge cases), or when ethical dilemmas require human-type judgment the algorithm was not designed to make.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Clear Highway. Minimal weather interference, highway driving.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Heavy Rain Urban.
Heavy rain, complex urban intersection.

Before you run it — make a prediction. What do you predict happens to Obstacle Classification accuracy when LIDAR and cameras are degraded by rain?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Edge Case. Unusual obstacle not in training data.
What do you predict the system does when it detects something it cannot classify with confidence?

Here's what our model reveals: Self-driving cars see the road through an array of complementary sensors. LIDAR creates a precise 3D map by firing thousands of laser pulses per second. Cameras provide color, texture, and sign-reading capability. Radar measures velocity and works in all weather. Sensor fusion algorithms combine these data streams into a unified perception model that is more reliable than any single sensor. The system then classifies every object, predicts its trajectory, plans a safe path, and executes — all in 100-300 milliseconds. It fails when sensors are all degraded simultaneously (heavy snow), when objects are genuinely novel (edge cases), or when ethical dilemmas require human-type judgment the algorithm was not designed to make.

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
   • What happens if you turn OFF LIDAR Pulse Frequency?
   • What happens if you turn OFF Weather Interference?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • V2X Communication — Vehicle-to-Everything communication that allows the car to receive data from other vehicles, traffic signals, and road infrastructure — providing information about hazards beyond sensor range
   • Map Precision — The accuracy of the pre-built high-definition map the vehicle uses for localization — centimeter-precise maps provide reliable reference but must be continuously updated
   • Cybersecurity Resilience — The system's ability to resist hacking, sensor spoofing, and data manipulation — a critical safety concern when lives depend on the accuracy of sensor data

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • The Sensor Stack — how does this connect to your model?
   • Sensor Fusion: The Key Innovation — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model demonstrate why sensor fusion is more reliable than any single sensor type?
   • What does the model reveal about the trade-off between Safety Margin and driving efficiency?
   • Why are edge cases the fundamental challenge for autonomous vehicles, and can they ever be fully solved?
   • How would adding V2X communication change the system's performance in scenarios where sensors are degraded?

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

V2X Communication. Vehicle-to-Everything communication that allows the car to receive data from other vehicles, traffic signals, and road infrastructure — providing information about hazards beyond sensor range
How would you model that?

Map Precision. The accuracy of the pre-built high-definition map the vehicle uses for localization — centimeter-precise maps provide reliable reference but must be continuously updated
How would you model that?

Cybersecurity Resilience. The system's ability to resist hacking, sensor spoofing, and data manipulation — a critical safety concern when lives depend on the accuracy of sensor data
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

Autonomous Vehicle Engineers design the sensor, perception, and decision systems that enable self-driving cars, trucks, and delivery robots. They work at Waymo, Cruise, Tesla, Aurora, and Zoox, earning $130,000-$300,000/year. This field combines electrical engineering, computer science, and robotics into one of the most cutting-edge career paths in technology.

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
Visual: Title slide with autonomous vehicle sensor visualization overlay
Say: "Your eyes have 120 million photoreceptors. This car has 64 laser beams, 8 cameras, 6 radars, and 12 ultrasonics — processing 1 terabyte of data per hour. But can it see better than you?"
Do: Show a split-screen: human driver's view versus the car's sensor visualization (point clouds, bounding boxes, trajectory predictions). The complexity hooks students.
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and vocabulary terms
Say: "Today you are engineering the perception system that must be better than human vision in every condition — rain, darkness, fog, and the completely unexpected."
Do: Have students read objectives. Pre-teach 'sensor fusion' and 'LIDAR.' Demonstrate LIDAR concept with a flashlight in a dark room — light hits objects and bounces back, revealing their distance.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: How does a car see without eyes — and why does it sometimes fail?
Say: "40,000 people die on US roads every year. 94 percent from human error. Can machines do better? And what happens when they cannot?"
Do: Quick-write: Students list situations where a self-driving car would outperform a human driver, and situations where it would fail. Share out and create two lists.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps overview with autonomous vehicle context
Say: "We are building a model of a machine that must make life-or-death decisions in 200 milliseconds based on noisy, incomplete sensor data. No pressure."
Do: Preview LEVER steps. Emphasize the sensor fusion concept — no single sensor is sufficient, but together they create something more capable than any one.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Nine component cards for autonomous vehicle model
Say: "Nine variables. Two you control through engineering design. Seven that the physics and software determine. The challenge is making them work together faster than any human can think."
Do: Guide students through all nine components. Spend extra time comparing what each sensor type provides — LIDAR for distance, camera for classification, radar for velocity and weather resilience.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows between nine components
Say: "When it rains, LIDAR degrades. When LIDAR degrades, the 3D map gets fuzzy. When the map gets fuzzy, obstacle classification confidence drops. Trace the cascade."
Do: Help students map the weather degradation cascade through multiple sensors. Then show how sensor fusion mitigates by reweighting sensor trust. Use green arrows for fusion recovery pathways.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Simulation graphs for three scenarios
Say: "Perfect conditions, terrible weather, and the thing no algorithm was trained for. Let us see where the system works, where it struggles, and where it fails."
Do: Students predict system performance for each scenario. Run simulations. The edge case scenario should generate discussion about the limits of pattern-matching AI.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key findings from model exploration
Say: "Self-driving cars are superhuman in routine driving and subhuman in the unexpected. The question is whether we can make the superhuman common enough and the failures rare enough to save more lives than we lose."
Do: Lead discussion on the statistical safety argument: if autonomous vehicles are 10 times safer overall but fail catastrophically in rare edge cases, is that acceptable? Who decides?
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Extreme weather sensor suite design challenge
Say: "Your car company wants to launch in Seattle — rain capital of the US. Design a sensor system that works when every sensor is degraded. Or tell the car to stop."
Do: Groups design weather-resilient sensor fusion architectures. Include handoff-to-human protocols. Present with model evidence for performance claims. Class evaluates which design is safest.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: How Self-Driving Cars See the Road
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
Human drivers kill over 40,000 people per year in the United States alone, with 94% of crashes caused by human error — distraction, impairment, fatigue, and poor judgment. Autonomous vehicles promise to eliminate these errors with sensors that never blink, algorithms that never get tired, and reaction times five times faster than humans. But replacing human perception and decision-making with technology is one of the hardest engineering challenges ever attempted.

NGSS ALIGNMENT:
HS-PS4-2, HS-PS4-5: Evaluate questions about the advantages of using digital transmission and storage of information. Communicate technical information about how some technological devices use the principles of wave behavior and wave interactions with matter to transmit and capture information and energy.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Communicating Technical Information
  Students communicate technical information about how LIDAR, radar, and cameras use wave behavior to detect and measure the vehicle's environment.
• Disciplinary Core Idea: PS4.C Information Technologies and Instrumentation
  Students model how electromagnetic waves of different frequencies (laser, radio, visible light) are used to detect, measure, and classify objects for autonomous vehicle navigation.
• Crosscutting Concept: Systems and System Models
  Students model the autonomous driving system as interacting subsystems (sensing, processing, deciding, acting) where the performance of each subsystem depends on and affects the others.

PACING GUIDE:
• Step 1 (Locate): 8-10 minutes
• Step 2 (Establish): 8-10 minutes
• Step 3 (Visualize & Evaluate): 10-12 minutes
• Step 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: LIDAR, Sensor Fusion, Decision Latency, Edge Case
□ Prepare How does a car with no human driver detect, identify, and react to dangers faster than any human — and why does it still sometimes fail discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify nine key components of the autonomous vehicle perception and decision system: LIDAR pulse frequency, detection range, signal processing speed, obstacle classification, weather interference, decision latency, sensor fusion accuracy, route optimization, and safety margin.
• Establish: Students map relationships showing that LIDAR pulse frequency and weather interference determine detection quality, which feeds into obstacle classification and sensor fusion accuracy, which determine decision latency and safety margin — with weather creating a degradation cascade through multiple pathways.
• Visualize: Students build a computational model showing the nine-component autonomous driving system with sensor redundancy and weather degradation pathways.
• Evaluate: Students run clear highway, heavy rain urban, and edge case scenarios to test their model and identify the conditions where autonomous driving transitions from safe to unreliable.
• Revise: Students add V2X communication, map precision, or cybersecurity resilience to model more complete autonomous vehicle system dynamics.

BACKGROUND CONTENT:
• The Sensor Stack:
  Modern autonomous vehicles use four complementary sensor types: LIDAR (laser-based 3D mapping, centimeter accuracy, limited in rain/snow), cameras (color/texture recognition, sign reading, lane detection, limited in darkness/glare), radar (velocity measurement, all-weather capability, low resolution), and ultrasonic (short-range parking and close-object detection). Each sensor has strengths and weaknesses — LIDAR excels at precise distance measurement but cannot read signs, cameras read signs but cannot measure distance as precisely, radar works in all weather but provides only coarse object shapes.

• Sensor Fusion: The Key Innovation:
  Sensor fusion is the algorithmic process of combining all sensor data into a unified perception model. When LIDAR detects an object at 150 meters, the camera classifies it as a pedestrian, and radar measures its approach velocity at 5 km/h. No single sensor provides all three pieces of information. Fusion algorithms use Kalman filters, neural networks, and probabilistic models to weight each sensor's contribution based on its confidence and current reliability — automatically reducing weight on rain-degraded LIDAR while increasing reliance on radar.

• The Decision Pipeline:
  From detection to action, the autonomous driving pipeline has five stages: (1) Perception — raw sensor data converted to environmental model (50-100 ms), (2) Prediction — estimating what every detected object will do next (10-30 ms), (3) Planning — computing the optimal path avoiding all predicted hazards (20-50 ms), (4) Control — translating the planned path into steering, braking, and acceleration commands (10-20 ms), (5) Actuation — physical execution of commands by the vehicle systems (20-50 ms). Total pipeline: 110-250 ms, compared to 1,500+ ms for human perception-to-action.

• The Edge Case Problem:
  Autonomous systems are trained on millions of miles of driving data, but the real world is infinitely variable. Edge cases — unusual scenarios not well-represented in training data — expose the fundamental limitation of pattern-matching approaches. A construction worker wearing a dinosaur costume, an overturned wheelchair in a lane, a drone flying at car height, or a child darting between parked cars all challenge classification algorithms in ways that human general intelligence handles naturally. The industry debates whether edge cases can ever be fully eliminated or whether a different approach to AI is needed.

COMMON MISCONCEPTIONS:
• "Self-driving cars use cameras like human eyes"
  Reality: While cameras provide color and texture information similar to human vision, they are only one of four sensor types. LIDAR provides 3D spatial information far more precise than human depth perception. Radar measures object velocities directly. The autonomous system perceives in 360 degrees simultaneously, in wavelengths humans cannot see, and processes data from all sensors in parallel. The result is fundamentally different from human vision — more precise in some ways (exact distances, 360-degree coverage, no blind spots) and less capable in others (general object understanding, context, common sense).
  Strategy: Demonstration: Show a LIDAR point cloud visualization alongside a camera image of the same scene. The point cloud provides perfect 3D geometry but no color or texture. The camera provides rich visual detail but no precise depth. Together they create a perception richer than either alone — or human vision.

• "Autonomous cars are safer because computers are faster"
  Reality: Raw speed is necessary but not sufficient. A computer can react in 150 ms versus a human's 1,500 ms, but safety also requires accurate perception, correct classification, and appropriate decisions. A computer that reacts in 150 ms to a misclassified object (slamming the brakes for a plastic bag it thinks is a boulder) is not safer than a human who takes 1,500 ms but correctly ignores the harmless bag. Speed without accuracy can be more dangerous than slower, correct human judgment.
  Strategy: Thought experiment: Would you rather have a driver with 100 ms reaction time who is wrong 5% of the time, or a driver with 1,000 ms reaction time who is wrong 0.1% of the time? The answer depends on the consequences of being wrong.

• "Self-driving cars will eliminate all traffic accidents"
  Reality: Even perfect autonomous vehicles cannot eliminate all accidents. Some crashes involve unavoidable mechanical failures (tire blowouts), road infrastructure failures (bridge collapses), or extreme weather events. Additionally, during the transition period when autonomous and human-driven vehicles share roads, the interaction between predictable machine behavior and unpredictable human behavior creates new failure modes. Most safety researchers predict autonomous vehicles will reduce crashes by 80-90%, not eliminate them entirely.
  Strategy: Calculate: If autonomous vehicles reduce US traffic deaths by 90%, that still means 4,000 deaths per year. Is that acceptable? Who is responsible when an autonomous vehicle kills someone — the passenger, the manufacturer, the programmer, or the algorithm?

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
Big Question: How does a car with no human driver detect, identify, and react to dangers faster than any human — and why does it still sometimes fail?
Answer: Self-driving cars see the road through an array of complementary sensors. LIDAR creates a precise 3D map by firing thousands of laser pulses per second. Cameras provide color, texture, and sign-reading capability. Radar measures velocity and works in all weather. Sensor fusion algorithms combine these data streams into a unified perception model that is more reliable than any single sensor. The system then classifies every object, predicts its trajectory, plans a safe path, and executes — all in 100-300 milliseconds. It fails when sensors are all degraded simultaneously (heavy snow), when objects are genuinely novel (edge cases), or when ethical dilemmas require human-type judgment the algorithm was not designed to make.

Simulation Answers:
• Clear Highway Scenario: Under ideal conditions with minimal weather interference, the sensor suite operates at peak performance. LIDAR provides precise 3D mapping to 200+ meters, cameras classify objects with high confidence, and radar confirms velocities. Sensor Fusion Accuracy exceeds 99.5%, Decision Latency drops below 150 milliseconds, and Safety Margin is maximized. The system outperforms human driving by a wide margin in this scenario, with Detection Range and reaction time both far exceeding human capability.
• Heavy Rain Urban Scenario: In heavy rain, LIDAR performance degrades by 40-60% as water droplets scatter laser pulses, creating noise in the point cloud. Camera performance drops 30-50% due to water on lenses and reduced visibility. Radar, which operates at longer wavelengths less affected by rain, maintains 85-90% performance. The fusion algorithm shifts weight from LIDAR and cameras toward radar, maintaining acceptable Obstacle Classification for large objects but struggling with smaller obstacles like pedestrians at distance. Safety Margin decreases significantly, and the model shows a threshold where the system should initiate handoff to human control.

Reflection Exemplars:
• Q: Why is sensor fusion more reliable than any single sensor?
  A: Each sensor type has a different failure mode. LIDAR fails in rain and snow (wavelength similar to water droplet size). Cameras fail in darkness and glare (dependent on visible light). Radar fails at precise classification (low spatial resolution). Ultrasonic fails at range (sound attenuates quickly). Because these failure modes are different, the probability that ALL sensors fail simultaneously is much lower than any single sensor failing. The fusion algorithm exploits this by dynamically weighting each sensor based on its current reliability. When LIDAR degrades, radar picks up distance measurement. When cameras lose visibility, LIDAR maintains 3D structure. This complementarity is the foundation of safe autonomous driving.
• Q: Why are edge cases the fundamental challenge?
  A: Autonomous driving algorithms learn from data — millions of miles of recorded driving scenarios. They excel at recognizing and responding to common situations: other cars, pedestrians, traffic signals, lane markings. But the real world is infinitely variable. An overturned shopping cart, a person in an inflatable dinosaur costume, a helium balloon at windshield height, or a newly erected construction barrier that is not in any map — these are all situations the algorithm may never have encountered. Human drivers handle these through general intelligence: reasoning, context, common sense. Current AI lacks this generality. The model shows that Obstacle Classification confidence drops dramatically for novel objects, increasing Decision Latency and potentially triggering unsafe responses.

STEM CHALLENGE GUIDANCE:
Title: Design a Self-Driving Sensor Suite for Extreme Weather
Mission: Design a sensor fusion architecture that maintains safe autonomous driving in severe weather conditions where individual sensor types degrade by 40-70%.
Scenario: An autonomous vehicle company wants to expand operations to cities with heavy rain, snow, and fog. Current sensor suites lose 40-70% of capability in these conditions. Your team must design a sensor fusion architecture that maintains sufficient Detection Range, Obstacle Classification accuracy, and Safety Margin to operate safely in the worst weather conditions — or determine the threshold at which the car must hand control back to a human driver.
Introduction: Present the challenge: An autonomous vehicle company wants to expand to cities with heavy rain, snow, and fog. Current sensor suites lose 40-70% capability in these conditions. Your team must design a sensor fusion architecture that maintains safe operation in severe weather, or define the precise conditions that require human takeover.

Key Concepts:
• Redundancy vs. Diversity: Adding more of the same sensor (redundancy) improves reliability but not capability. Adding different sensor types (diversity) provides fundamentally new information that compensates for other sensors' weaknesses. Optimal design balances both — multiple LIDAR units for redundancy and different sensor types for diversity.
• Graceful Degradation in Autonomy: When conditions degrade, the vehicle should not suddenly switch from full autonomy to no autonomy. Instead, it should gracefully reduce speed, increase safety margins, simplify its operating domain (avoid complex intersections), and prepare for human handoff — giving the human driver time to take control safely.
• The Long Tail of Safety: Autonomous vehicles must be safe not for 99% of situations but for 99.9999% — because at scale (millions of vehicles driving billions of miles), even a 0.01% failure rate translates to thousands of crashes per year. Achieving this reliability in the long tail of rare edge cases is the central engineering challenge.

Evaluation Rubric:
• Expert (4): Design specifies sensor types, quantities, and placement with weather-performance analysis for each, includes adaptive fusion weighting algorithm, defines quantitative safety thresholds for human handoff, and demonstrates system performance with model evidence across multiple weather scenarios
• Proficient (3): Design includes multiple complementary sensors with weather degradation analysis and identifies conditions requiring human handoff
• Developing (2): Design proposes a sensor configuration but lacks weather degradation analysis or does not define safe operating boundaries
• Beginning (1): Design is incomplete or does not demonstrate understanding of sensor complementarity and fusion

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a sensor comparison chart showing LIDAR, camera, radar, and ultrasonic performance across clear, rain, snow, fog, and darkness conditions
  • Use a visual sensor coverage map showing blind spots and overlapping coverage zones for different sensor placement configurations
  • Sentence frames: 'In __ weather conditions, __ sensor degrades by __%, so our fusion algorithm shifts weight to __ sensor, which maintains __% performance because __'

Extensions (Advanced Learners):
  • Research how Waymo, Cruise, and Tesla take fundamentally different approaches to autonomous driving (LIDAR-centric versus camera-only) and debate which strategy is more likely to achieve full self-driving
  • Investigate the ethical frameworks proposed for autonomous vehicle decision-making in unavoidable crash scenarios and design your own ethical decision algorithm
  • Explore how 5G and V2X (Vehicle-to-Everything) communication could supplement onboard sensors by providing information about hazards beyond line of sight

Cross-Curricular Connections:
  • Math: Calculate stopping distances: if a car travels at 100 km/h and detects an obstacle at 150 meters with a decision latency of 200 ms and a braking deceleration of 8 m/s^2, does it stop in time? At what maximum speed can it guarantee stopping within the detection range? How does this change if Detection Range is halved by rain?
  • ELA: Write a balanced investigative journalism article exploring both the promise and the risks of self-driving cars, interviewing stakeholders including engineers, accident victims, disability advocates, and urban planners
  • Ethics/Philosophy: Analyze the trolley problem in the context of autonomous vehicles: if a crash is unavoidable, should the car minimize total harm (utilitarian), protect its passengers (contractual), or refuse to make the choice (deontological)? Who should program these decisions?

CAST ALIGNMENT:
• Model how nine sensor and decision variables interact to enable safe autonomous vehicle navigation
• Analyze how weather interference degrades individual sensors and how sensor fusion provides redundancy
• Evaluate the engineering and ethical trade-offs in setting Safety Margin parameters for autonomous vehicles

CAST-Style Assessment Questions:
• Multiple Choice: During heavy rain, a self-driving car's LIDAR performance drops by 60% and camera performance drops by 40%, but radar performance drops by only 10%. According to your model, how does the sensor fusion system maintain Obstacle Classification accuracy?
• Constructed Response: Using your model, explain why a self-driving car that performs perfectly in 99.9% of situations is still not safe enough for public roads. Address the concept of edge cases, the scale of driving (millions of miles), and the difference between statistical safety and individual trust in your response.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: How Self-Driving Cars See the Road
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. How do you think a self-driving car knows what is around it without a human watching the road?

   _________________________________________________________

   _________________________________________________________

2. What sensors do you think a self-driving car uses and what does each one detect?

   _________________________________________________________

   _________________________________________________________

3. Draw what you think a self-driving car 'sees' compared to what a human driver sees.

   [DRAWING BOX]

4. Why do you think self-driving cars sometimes have accidents even though computers are faster than humans?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ LIDAR                         
___ Sensor Fusion                 
___ Decision Latency              
___ Edge Case                     

A. Light Detection and Ranging — a sensor that fires thousands of laser pulses per second and measures the time for each to return, creating a precise 3D point cloud map of the environment with centimeter accuracy up to 200+ meters
B. The algorithmic process of combining data from multiple sensor types — LIDAR, cameras, radar, ultrasonic — to create a unified, more reliable perception model than any single sensor can provide alone
C. The total time from initial sensor detection of a hazard to the vehicle executing a response action — including sensor processing, object classification, path planning, and actuator response — typically 100-300 milliseconds for autonomous systems versus 1,500+ milliseconds for human drivers
D. An unusual or rare scenario that falls outside the training data of an autonomous system — a construction worker in a gorilla costume, a mattress falling off a truck, or a child chasing a ball into the street — where the system's classification algorithms may fail or respond incorrectly

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

SCENARIO: Clear Highway
Settings: Minimal weather interference, highway driving
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Heavy Rain Urban
Settings: Heavy rain, complex urban intersection
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Edge Case
Settings: Unusual obstacle not in training data
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

1. How does your model demonstrate why sensor fusion is more reliable than any single sensor type?

   _________________________________________________________

   _________________________________________________________

2. What does the model reveal about the trade-off between Safety Margin and driving efficiency?

   _________________________________________________________

   _________________________________________________________

3. Why are edge cases the fundamental challenge for autonomous vehicles, and can they ever be fully solved?

   _________________________________________________________

   _________________________________________________________

4. How would adding V2X communication change the system's performance in scenarios where sensors are degraded?

   _________________________________________________________

   _________________________________________________________

5. What ethical questions arise from the Safety Margin trade-off — who decides how much risk is acceptable?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. How does a car with no human driver detect, identify, and react to dangers faster than any human — and why does it still sometimes fail? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Communicating Technical Information
   □ Disciplinary Core Idea: PS4.C Information Technologies and Instrumentation
   □ Crosscutting Concept: Systems and System Models

3. What ethical questions arise from the Safety Margin trade-off — who decides how much risk is acceptable?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Self-Driving Sensor Suite for Extreme Weather
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design a sensor fusion architecture that maintains safe autonomous driving in severe weather conditions where individual sensor types degrade by 40-70%.

SCENARIO: An autonomous vehicle company wants to expand operations to cities with heavy rain, snow, and fog. Current sensor suites lose 40-70% of capability in these conditions. Your team must design a sensor fusion architecture that maintains sufficient Detection Range, Obstacle Classification accuracy, and Safety Margin to operate safely in the worst weather conditions — or determine the threshold at which the car must hand control back to a human driver.

GUIDING QUESTIONS:
• Which sensor types are most and least affected by each weather condition?
• How does your sensor fusion algorithm weight different sensors when some are degraded?
• At what point should the system determine that conditions are too dangerous for autonomous operation?

DESIGN THINKING:
• What sensor types and quantities does your suite include and where are they mounted?

  _________________________________________________________

• How does your fusion algorithm adjust sensor weighting when specific sensors are degraded?

  _________________________________________________________

• What is the minimum Detection Range and Obstacle Classification accuracy your system requires for safe operation?

  _________________________________________________________

• What is your handoff protocol when weather degrades beyond safe autonomous limits?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Design specifies sensor types, quantities, and placement with weather-performance analysis for each, includes adaptive fusion weighting algorithm, defines quantitative safety thresholds for human handoff, and demonstrates system performance with model evidence across multiple weather scenarios
• Proficient (3): Design includes multiple complementary sensors with weather degradation analysis and identifies conditions requiring human handoff
• Developing (2): Design proposes a sensor configuration but lacks weather degradation analysis or does not define safe operating boundaries
• Beginning (1): Design is incomplete or does not demonstrate understanding of sensor complementarity and fusion

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CAST-Aligned Pre/Post Assessment

### Administration Instructions

These 5 multiple-choice questions are administered identically as both a pre-assessment (before Activity 1) and a post-assessment (after Activity 4). Score each out of 5. Learning growth = post-score minus pre-score.

Questions follow the California Science Test (CAST) stimulus-response format. Each item is three-dimensional, assessing a Science and Engineering Practice (SEP), Disciplinary Core Idea (DCI), and Crosscutting Concept (CCC) simultaneously, aligned to HS-PS4-2, HS-PS4-5.

---

### Pre-Assessment Questions

### Question 1

A self-driving car uses LIDAR, cameras, and radar simultaneously. Why is this multi-sensor approach (sensor fusion) more reliable than using any single sensor?

A. More sensors make the car look more advanced and increase consumer confidence
B. Each sensor type excels in different conditions and detects different properties — LIDAR provides 3D mapping, cameras provide color and sign recognition, radar works in all weather — so combining them creates redundancy where one sensor's weakness is covered by another's strength
C. Using three sensors makes the car exactly three times safer
D. Single sensors are never used in any vehicle application

Correct Answer: B

Feedback: Correct. Sensor fusion combines complementary strengths: LIDAR provides precise 3D spatial mapping but fails in rain, cameras provide color/texture for classification but struggle in fog, and radar measures velocity and penetrates weather but lacks spatial detail. Together, they create a perception model more robust than any single source. Consider what each sensor type is good at and what it struggles with. LIDAR fires lasers, cameras capture visible light, and radar uses radio waves. Each interacts with the environment differently.

---

### Question 2

An autonomous vehicle's decision latency is 200 milliseconds, while a human driver's reaction time is approximately 1,500 milliseconds. At 60 mph (27 m/s), how much additional stopping distance does the human driver need compared to the autonomous system?

A. Approximately 5 meters (negligible difference)
B. Approximately 15 meters (the human needs about 35 meters of reaction distance versus the car's 5.4 meters)
C. Approximately 35 meters (the human needs about 40 meters versus 5.4 meters)
D. The difference depends on the type of obstacle, not the reaction time

Correct Answer: C

Feedback: Correct. Human reaction distance = 27 m/s x 1.5 s = 40.5 m. AV reaction distance = 27 m/s x 0.2 s = 5.4 m. The difference is approximately 35 meters — enough to determine whether a collision occurs. This demonstrates the reaction time advantage of autonomous systems. Calculate distance = speed x time for both reaction times. At 27 m/s, how far does the vehicle travel during 1.5 seconds (human) versus 0.2 seconds (autonomous)?

---

### Question 3

An autonomous vehicle encounters an object it cannot classify with high confidence — a deflated mylar balloon in the road. This situation is called an 'edge case.' Why are edge cases particularly dangerous for autonomous systems?

A. Edge cases cause the sensors to malfunction permanently
B. The system's machine learning models were trained on common scenarios and may misclassify novel objects — stopping for a harmless balloon wastes time, but driving over an object misidentified as harmless could be fatal
C. Edge cases only occur in bad weather, so they are easily avoided
D. Human drivers also cannot handle edge cases, so it is not a unique autonomous vehicle problem

Correct Answer: B

Feedback: Correct. Edge cases expose the fundamental limitation of pattern-matching AI: it excels at recognizing common objects from training data but struggles with novel situations. Humans use general intelligence and common sense to assess unknown objects; autonomous systems must choose between stopping (safe but potentially disruptive) or proceeding (efficient but potentially dangerous). Consider how the system decides what to do with an object. It compares what it sees to patterns it learned during training. What happens when the object does not match any learned pattern?

---

### Question 4

During heavy rain, a self-driving car's LIDAR loses 60% of its effectiveness because laser pulses scatter off water droplets. Which alternative sensor is LEAST affected by rain and could compensate?

A. Additional LIDAR units mounted at different angles
B. High-resolution cameras, which also use visible light affected by rain
C. Radar, which uses radio waves that penetrate rain, fog, and snow with minimal degradation
D. Ultrasonic sensors, which have sufficient range to replace LIDAR

Correct Answer: C

Feedback: Correct. Radar uses radio waves (centimeter wavelengths) that pass through rain droplets with minimal scattering, unlike LIDAR (near-infrared, micrometer wavelengths) and cameras (visible light) which are significantly degraded. This is why sensor fusion is essential — radar provides reliable distance and velocity data when other sensors fail. Consider the wavelength of each sensor's emissions relative to the size of rain droplets. Longer wavelengths pass through small obstacles more easily than shorter wavelengths.

---

### Question 5

An autonomous vehicle maintains a safety margin — a buffer distance beyond the minimum required for safe braking. Increasing this margin makes the car safer but has a trade-off. What is the primary trade-off?

A. Larger safety margins require more fuel, increasing emissions
B. Larger margins cause the car to brake earlier, drive slower, and create gaps in traffic flow — reducing efficiency and potentially frustrating other drivers who may drive unpredictably in response
C. Larger margins increase the risk of rear-end collisions from following vehicles
D. There is no trade-off — larger safety margins are always better in every way

Correct Answer: B

Feedback: Correct. The safety margin trade-off is both an engineering and societal question. Overly conservative driving reduces throughput, increases congestion, and may cause human drivers to behave aggressively around the autonomous vehicle. Finding the optimal margin balances individual safety against traffic flow and social integration. Think about what happens when a car maintains very large following distances and brakes much earlier than necessary. How does this affect the overall traffic system and other drivers?

---

### Post-Assessment Questions

### Question 1

The model shows that in heavy rain, LIDAR performance drops 60%, camera drops 40%, but radar drops only 10%. Despite these individual degradations, Sensor Fusion Accuracy drops by only 25%. What system property explains this resilience?

A. The model underestimates the impact of rain on sensor performance
B. Sensor fusion creates redundancy — the algorithm dynamically reweights sensors, relying more heavily on radar when LIDAR and cameras are degraded, maintaining combined accuracy above any single degraded sensor
C. The 25% drop is unacceptable and means the system should shut down immediately
D. Rain does not actually affect autonomous vehicle performance in real systems

Correct Answer: B

Feedback: Correct. The model demonstrates the core value of sensor fusion: when individual sensors degrade at different rates due to environmental conditions, the fusion algorithm shifts weighting toward the most reliable sensor. This built-in redundancy maintains system-level performance above any single sensor's degraded level. Consider what happens when the fusion algorithm knows that LIDAR and cameras are less reliable in rain. Can it adjust how much it trusts each sensor's data? What sensor remains reliable?

---

### Question 2

In the edge case scenario, the model shows Obstacle Classification confidence dropping below 50% for a novel object. The system responds by expanding Safety Margin and reducing speed. What decision-making principle does this represent?

A. The system is malfunctioning because confidence should always be above 90%
B. Conservative fallback — when uncertainty is high, the system increases caution by trading efficiency for safety, buying more time to classify the object or allowing the human to take control
C. The system ignores unclassified objects to maintain traffic flow
D. Speed reduction is the only response the system has to any anomaly

Correct Answer: B

Feedback: Correct. The model demonstrates a fundamental safety principle: when the perception system has low confidence, the decision system compensates by increasing safety margins. This buys time for additional sensor data, allows the object to be observed from closer range, and provides the option for human takeover. Think about what a cautious human driver would do when encountering something unexpected on the road. Would they speed up, maintain speed, or slow down? Why?

---

### Question 3

The model classifies LIDAR Pulse Frequency and Weather Interference as external variables. Why is Weather Interference classified as external even though it directly affects sensor performance?

A. External variables must always be environmental conditions
B. Weather Interference is a condition the autonomous system encounters but cannot control or change — it is an input from the environment, not a property of the engineering system being modeled
C. Weather interference is too unpredictable to be modeled as an internal variable
D. The classification is incorrect and should be changed

Correct Answer: B

Feedback: Correct. External variables represent conditions imposed on the system from outside. The autonomous vehicle cannot change the weather — it can only respond to it. Weather Interference is an environmental input that affects system performance but is not controlled by the system. Ask: can the autonomous vehicle control the weather? If not, weather is an environmental condition the system must deal with, not a system property it can adjust.

---

### Question 4

The model predicts that Decision Latency increases from 150 ms in clear conditions to 350 ms in the edge case scenario. What system interaction causes this increase?

A. The processors slow down in unusual situations
B. Low Obstacle Classification confidence triggers additional processing cycles — the system runs more analysis algorithms, cross-references additional data sources, and may request human verification, all adding time before a decision is made
C. Decision Latency is constant and does not change between scenarios
D. The increase is caused by physical distance to the obstacle, not processing time

Correct Answer: B

Feedback: Correct. The model reveals an important trade-off: when the system encounters an ambiguous object, it spends more time trying to classify it correctly before deciding on an action. This is the speed-accuracy trade-off — taking longer to decide increases accuracy but also increases the distance traveled before responding. Consider what the system does when it encounters an object it cannot quickly classify. Does it immediately decide, or does it run additional analysis to improve classification confidence?

---

### Question 5

A student argues that autonomous vehicles should not be deployed until they can handle 100% of edge cases correctly. Based on the model, what is the most scientifically valid evaluation of this standard?

A. The standard is achievable within 5 years with current technology trajectories
B. The 100% standard is mathematically impossible — the set of possible edge cases is effectively infinite, and the model shows that the system's strength lies in safe fallback responses (slowing, stopping, human handoff) when it encounters situations beyond its classification ability
C. Edge cases are rare enough that they can be ignored
D. Human drivers handle 100% of edge cases correctly, so autonomous vehicles should too

Correct Answer: B

Feedback: Correct. The real world presents an effectively infinite set of possible situations. No system — human or autonomous — handles all of them correctly. The model shows that the engineering solution is not perfect classification but safe degradation: when confidence is low, the system increases caution and can hand control to a human driver. Consider whether it is possible to train a system on every possible situation it might ever encounter. Also consider: do human drivers handle 100% of situations correctly? The relevant question is how the system responds when it encounters uncertainty.

---

### Answer Key

**Pre-Assessment:**
Question 1: B
Question 2: C
Question 3: B
Question 4: C
Question 5: B

**Post-Assessment:**
Question 1: B
Question 2: B
Question 3: B
Question 4: B
Question 5: B

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-10/G10L3-L06/G10L3-L06-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-10/G10L3-L06/G10L3-L06-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-10/G10L3-L06/G10L3-L06-Student-Presentation.pptx] |
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