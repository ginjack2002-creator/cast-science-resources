# Lesson: How Do Self-Driving Cars See?

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G11L3-L07 |
| **Grade** | 11th Grade — Level 3: Systems Innovation Lab |
| **Lesson Name** | How Do Self-Driving Cars See? |
| **Status** | Template |

---

## Platform

### Title
**How Do Self-Driving Cars See? — Modeling LiDAR, Computer Vision, and Autonomous Decision-Making**

### Overview
Every time you ride in a car, your brain performs an extraordinary feat of real-time perception: processing visual information from two eyes, interpreting depth, motion, color, and context, predicting the behavior of other road users, and making continuous steering and speed decisions — all while holding a conversation or listening to music. Autonomous vehicles attempt to replicate this capability using an array of electronic sensors and artificial intelligence algorithms. The engineering challenge is immense: the system must work perfectly in conditions ranging from bright sunshine to heavy rain, from empty highways to crowded school zones, and must handle situations that no programmer anticipated. Students investigate the driving question: How does an autonomous vehicle build a real-time 3D understanding of its surroundings from raw sensor data — and can it ever be trusted to make life-or-death driving decisions? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of an autonomous vehicle with visible LiDAR sensors on a city street with colorful point cloud data visualization overlaid showing detected pedestrians and vehicles, featuring a diverse multicultural group with Black people centered of 16-17 year old students examining the technology through large glass windows at a testing facility]

### Grade
11th Grade — Level 3: Systems Innovation Lab

### NGSS Standard
**HS-PS4-1, HS-ETS1-2**: Use mathematical representations to support a claim regarding relationships among the frequency, wavelength, and speed of waves traveling in various media. Design a solution to a complex real-world problem by breaking it down into smaller, more manageable problems that can be solved through engineering.

### Learning Objectives
- Model how LiDAR, cameras, and radar sensors generate complementary data streams that are fused into a coherent 3D representation of the driving environment
- Analyze the relationship between sensor resolution, processing latency, and the vehicle's ability to detect and classify objects at highway speeds
- Evaluate the trade-offs between rule-based and machine-learning decision algorithms when autonomous vehicles encounter novel or ambiguous driving scenarios
- Predict how environmental conditions such as rain, fog, glare, and darkness degrade sensor performance and affect system safety margins

### Component List (Starting Model: 7 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| LiDAR Resolution | External | The density of laser points per square meter at a given distance — higher resolution creates more detailed 3D maps but generates exponentially more data that must be processed in real time |
| Camera Detection Accuracy | Internal | The percentage of objects correctly identified and classified by the computer vision neural network — affected by lighting conditions, object novelty, occlusion, and the diversity of the training dataset |
| Sensor Fusion Confidence | Internal | The system's calculated probability that its unified environmental model is correct — increases when multiple sensors agree on object location and classification, decreases when sensors provide conflicting data |
| Processing Latency | Internal | The time required to collect sensor data, fuse it into a coherent model, classify all objects, plan a safe path, and send commands to steering, braking, and acceleration actuators |
| Environmental Degradation | External | The reduction in sensor performance caused by weather, lighting, and road conditions — rain scatters LiDAR beams, fog reduces camera range, sun glare blinds cameras, and snow obscures lane markings and road edges |
| Decision Algorithm Reliability | Internal | The probability that the path-planning algorithm selects the safest action given the perceived environment — affected by the completeness of the environmental model, the novelty of the scenario, and whether the situation was represented in training data |
| Safety Margin | Internal | The buffer between the vehicle's current trajectory and the nearest potential collision — measured in both distance and time, this margin must account for sensor uncertainty, processing latency, and the unpredictable behavior of other road users |

### Research for Lesson
- LiDAR: Seeing in 3D with Light — reference materials and textbook resources
- Computer Vision: Understanding What the Sensors See — reference materials and textbook resources
- Sensor Fusion: Building a Unified World Model — reference materials and textbook resources
- The Decision-Making Challenge — reference materials and textbook resources

---

## Step 1: LOCATE — Build Your System

### Text Editor

```
HOW DO SELF-DRIVING CARS SEE?

Modeling LiDAR, Computer Vision, and Autonomous Decision-Making.
How does an autonomous vehicle build a real-time 3D understanding of its surroundings from raw sensor data — and can it ever be trusted to make life-or-death driving decisions?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "LiDAR Resolution" — the density of laser points per square meter at a given distance — higher resolution creates more detailed 3d maps but generates exponentially more data that must be processed in real time
  ○ Click "Environmental Degradation" — the reduction in sensor performance caused by weather
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Camera Detection Accuracy" — the percentage of objects correctly identified and classified by the computer vision neural network — affected by lighting conditions
  ○ Click "Sensor Fusion Confidence" — the system's calculated probability that its unified environmental model is correct — increases when multiple sensors agree on object location and classification
  ○ Click "Processing Latency" — the time required to collect sensor data
  ○ Click "Decision Algorithm Reliability" — the probability that the path-planning algorithm selects the safest action given the perceived environment — affected by the completeness of the environmental model
  ○ Click "Safety Margin" — the buffer between the vehicle's current trajectory and the nearest potential collision — measured in both distance and time

Task B: ADD TO YOUR MODEL
• Click the PLUS (+) button to add each component to your picture
• You should now see 7 components on your canvas

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
"How does an autonomous vehicle build a real-time 3D understanding of its surroundings from raw sensor data — and can it ever be trusted to make life-or-death driving decisions?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'LiDAR Resolution' — that's external. The density of laser points per square meter at a given distance — higher resolution creates more detailed 3D maps but generates exponentially more data that must be processed in real time.
Click on 'Camera Detection Accuracy' — that's internal. The percentage of objects correctly identified and classified by the computer vision neural network — affected by lighting conditions.
Click on 'Sensor Fusion Confidence' — that's internal. The system's calculated probability that its unified environmental model is correct — increases when multiple sensors agree on object location and classification.
Click on 'Processing Latency' — that's internal. The time required to collect sensor data.
Click on 'Environmental Degradation' — that's external. The reduction in sensor performance caused by weather.
Click on 'Decision Algorithm Reliability' — that's internal. The probability that the path-planning algorithm selects the safest action given the perceived environment — affected by the completeness of the environmental model.
Click on 'Safety Margin' — that's internal. The buffer between the vehicle's current trajectory and the nearest potential collision — measured in both distance and time.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

LiDAR Resolution is external because it represents the engineering design choice about sensor hardware specifications — a decision made during vehicle design, not determined by driving conditions. Environmental Degradation is external because it represents weather and lighting conditions imposed by the environment, outside the vehicle's control. The remaining five components are internal: Camera Detection Accuracy depends on lighting conditions and the neural network's training, Sensor Fusion Confidence emerges from the agreement or disagreement among sensor inputs, Processing Latency is determined by computational hardware and algorithm efficiency, Decision Algorithm Reliability depends on scenario familiarity and model quality, and Safety Margin is the calculated remainder after all processing delays and uncertainties are accounted for.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next step, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 7 components sorted: LiDAR Resolution, Environmental Degradation (External), Camera Detection Accuracy, Sensor Fusion Confidence, Processing Latency, Decision Algorithm Reliability, Safety Margin (Internal)]

### Graph
[Empty graph panel — no simulation yet]

---

## Step 2: ESTABLISH — Connect the Relationships

### Text Editor

```
TIME TO DRAW THE INVISIBLE LINES

Those 7 components don't just sit there — they AFFECT each other.
When one changes, others change too. Let's map those connections.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: OPEN CONNECTION MODE
• Click the "Connect" icon in the TOP LEFT corner of your screen
• Your cursor is now ready to draw relationship arrows

Task B: DRAW YOUR RELATIONSHIPS
• Click on "LiDAR Resolution" and drag an arrow to "Sensor Fusion Confidence"
• Click on "Environmental Degradation" and drag an arrow to "Camera Detection Accuracy"
• Click on "Processing Latency" and drag an arrow to "Safety Margin"
• Click on "Sensor Fusion Confidence" and drag an arrow to "Decision Algorithm Reliability"

Task C: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ LiDAR Resolution → Sensor Fusion Confidence = POSITIVE (+)
    Higher LiDAR resolution provides more detailed 3D point clouds with more data points per object, giving the fusion algorithm more geometric information to work with and increasing the confidence of the unified environmental model.

  ○ Environmental Degradation → Camera Detection Accuracy = NEGATIVE (−)
    Worsening environmental conditions — rain, fog, darkness, glare — directly reduce the quality of camera images and the accuracy of neural network object classification, because the visual features the network relies on become obscured or distorted.

  ○ Processing Latency → Safety Margin = NEGATIVE (−)
    Longer processing latency means the vehicle travels farther between sensing and acting, directly consuming safety margin. At 65 mph, each additional 100 milliseconds of latency reduces the available stopping distance by approximately 10 feet.

  ○ Sensor Fusion Confidence → Decision Algorithm Reliability = POSITIVE (+)
    Higher fusion confidence means the decision algorithm receives a more accurate environmental model, enabling more reliable path planning. When fusion confidence is low, the decision algorithm must make choices based on uncertain information, increasing the probability of errors.

Task D: CHECK YOUR MODEL
• You should have 4 arrows total
• 2 negative relationship(s), 2 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: A self-driving car processes millions of data points every second from LiDAR, cameras, and radar, fusing them into a 3D model of the world. But at 65 mph, the car travels nearly 100 feet per second. If processing takes 300 milliseconds, the car has already moved 30 feet before it can react to new information. How do you design a system that is safe when there is always a gap between sensing and acting?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'LiDAR Resolution' and drag an arrow
over to 'Sensor Fusion Confidence.'

Here's the key question: When lidar resolution goes UP, does
sensor fusion confidence go UP or DOWN?

Higher LiDAR resolution provides more detailed 3D point clouds with more data points per object, giving the fusion algorithm more geometric information to work with and increasing the confidence of the unified environmental model.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Environmental Degradation' and drag an arrow
over to 'Camera Detection Accuracy.'

Here's the key question: When environmental degradation goes UP, does
camera detection accuracy go UP or DOWN?

Worsening environmental conditions — rain, fog, darkness, glare — directly reduce the quality of camera images and the accuracy of neural network object classification, because the visual features the network relies on become obscured or distorted.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Last connection: Click on 'Processing Latency' and drag an arrow
over to 'Safety Margin.'

Here's the key question: When processing latency goes UP, does
safety margin go UP or DOWN?

Longer processing latency means the vehicle travels farther between sensing and acting, directly consuming safety margin. At 65 mph, each additional 100 milliseconds of latency reduces the available stopping distance by approximately 10 feet.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Sensor Fusion Confidence' and drag an arrow
over to 'Decision Algorithm Reliability.'

Here's the key question: When sensor fusion confidence goes UP, does
decision algorithm reliability go UP or DOWN?

Higher fusion confidence means the decision algorithm receives a more accurate environmental model, enabling more reliable path planning. When fusion confidence is low, the decision algorithm must make choices based on uncertain information, increasing the probability of errors.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Look at your model now. You've got 2 negative and 2
positive relationships. 4 arrows total.

A self-driving car processes millions of data points every second from LiDAR, cameras, and radar, fusing them into a 3D model of the world. But at 65 mph, the car travels nearly 100 feet per second. If processing takes 300 milliseconds, the car has already moved 30 feet before it can react to new information. How do you design a system that is safe when there is always a gap between sensing and acting?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: LiDAR Resolution +→ Sensor Fusion Confidence, Environmental Degradation −→ Camera Detection Accuracy, Processing Latency −→ Safety Margin, Sensor Fusion Confidence +→ Decision Algorithm Reliability]

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
• When LiDAR Resolution is HIGH, what happens to the internal components?

Task C: SCENARIO — CLEAR HIGHWAY DRIVING
• Maximum LiDAR, minimal environmental degradation, increasing speed
• PREDICT FIRST: What do you predict happens to the safety margin as vehicle speed doubles while processing latency remains constant?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task D: SCENARIO — HEAVY RAIN URBAN INTERSECTION
• 40% LiDAR degradation, 30% camera degradation, complex urban scene
• PREDICT FIRST: What do you predict happens to sensor fusion confidence when the two primary sensors both lose significant capability simultaneously?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task E: SCENARIO — NOVEL OBJECT EMERGENCY
• Unclassified obstacle appears in the vehicle's path at highway speed
• PREDICT FIRST: What do you predict the decision algorithm does when it detects something in the road but cannot determine what it is?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Sensor fusion is not simply averaging data from different sensors — it is a probabilistic calculation where each sensor's contribution is weighted by its reliability in current conditions, and the system's overall confidence can be lower than any individual sensor's confidence when sensors disagree
• Processing latency creates a fundamental safety limit: at highway speeds, the vehicle is always responding to a world that existed hundreds of milliseconds ago, meaning safety margins must account for everything that could change during the processing delay
• Environmental conditions do not degrade all sensors equally — rain primarily affects LiDAR and cameras but barely affects radar, while darkness eliminates camera utility but does not affect LiDAR or radar — which is why redundant multi-sensor systems are essential for all-weather autonomy
• The hardest challenge for autonomous vehicles is not normal driving but edge cases — the unusual, rare, and novel situations that were not well-represented in training data, where human drivers use general intelligence and common sense that current AI systems lack

THE ANSWER: Self-driving cars construct their understanding of the world through a sophisticated sensor fusion pipeline. LiDAR creates precise 3D point clouds using laser time-of-flight measurements. Cameras provide color and texture information for object classification using trained neural networks. Radar detects object velocity and works through weather that degrades optical sensors. These data streams are fused into a unified environmental model, updated dozens of times per second, from which path-planning algorithms calculate the safest trajectory. The system works remarkably well in common driving scenarios — highway cruising, lane following, and predictable intersections. However, fundamental challenges remain: processing latency means the car always reacts to slightly outdated information, environmental conditions can simultaneously degrade multiple sensors, and novel situations that fall outside the training distribution force the system to extrapolate in ways that may fail unpredictably. The question is not whether autonomous vehicles can drive — they demonstrably can — but whether they can handle the full diversity of real-world driving, including the rare catastrophic scenarios that human drivers navigate using general intelligence, social understanding, and common sense.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Clear Highway Driving. Maximum LiDAR, minimal environmental degradation, increasing speed.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Heavy Rain Urban Intersection.
40% LiDAR degradation, 30% camera degradation, complex urban scene.

Before you run it — make a prediction. What do you predict happens to sensor fusion confidence when the two primary sensors both lose significant capability simultaneously?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Novel Object Emergency. Unclassified obstacle appears in the vehicle's path at highway speed.
What do you predict the decision algorithm does when it detects something in the road but cannot determine what it is?

Here's what our model reveals: Self-driving cars construct their understanding of the world through a sophisticated sensor fusion pipeline. LiDAR creates precise 3D point clouds using laser time-of-flight measurements. Cameras provide color and texture information for object classification using trained neural networks. Radar detects object velocity and works through weather that degrades optical sensors. These data streams are fused into a unified environmental model, updated dozens of times per second, from which path-planning algorithms calculate the safest trajectory. The system works remarkably well in common driving scenarios — highway cruising, lane following, and predictable intersections. However, fundamental challenges remain: processing latency means the car always reacts to slightly outdated information, environmental conditions can simultaneously degrade multiple sensors, and novel situations that fall outside the training distribution force the system to extrapolate in ways that may fail unpredictably. The question is not whether autonomous vehicles can drive — they demonstrably can — but whether they can handle the full diversity of real-world driving, including the rare catastrophic scenarios that human drivers navigate using general intelligence, social understanding, and common sense.

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
   • What happens if you turn OFF LiDAR Resolution?
   • What happens if you turn OFF Environmental Degradation?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • V2X Communication — Vehicle-to-everything communication allows autonomous vehicles to receive data from traffic signals, other vehicles, and road infrastructure — extending perception beyond line-of-sight sensors to include information about conditions around corners, over hills, and at distant intersections
   • Prediction Horizon — The time window over which the vehicle's algorithms predict the future positions of all detected moving objects — longer prediction horizons enable earlier and smoother responses but become exponentially less accurate as behavioral uncertainty compounds
   • Ethical Decision Framework — The programmed hierarchy of values the vehicle uses when a collision is unavoidable — how it prioritizes between protecting its passengers, protecting pedestrians, minimizing total harm, and following traffic laws when these objectives conflict

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • LiDAR: Seeing in 3D with Light — how does this connect to your model?
   • Computer Vision: Understanding What the Sensors See — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model demonstrate the fundamental trade-off between sensor resolution and processing latency?
   • Why is sensor fusion more valuable than simply using the best single sensor, and what happens when sensors provide contradictory information?
   • What does your model reveal about why autonomous vehicles perform differently in clear conditions versus adverse weather?
   • How would your model change if processing latency could be reduced to near-zero through advanced computing hardware?

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

Your model has 7 components. Real systems involve
way more. Think about...

V2X Communication. Vehicle-to-everything communication allows autonomous vehicles to receive data from traffic signals, other vehicles, and road infrastructure — extending perception beyond line-of-sight sensors to include information about conditions around corners, over hills, and at distant intersections
How would you model that?

Prediction Horizon. The time window over which the vehicle's algorithms predict the future positions of all detected moving objects — longer prediction horizons enable earlier and smoother responses but become exponentially less accurate as behavioral uncertainty compounds
How would you model that?

Ethical Decision Framework. The programmed hierarchy of values the vehicle uses when a collision is unavoidable — how it prioritizes between protecting its passengers, protecting pedestrians, minimizing total harm, and following traffic laws when these objectives conflict
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

Autonomous Vehicle Engineers design and test self-driving systems at companies like Waymo, Cruise, and Aurora, integrating sensors, perception algorithms, and decision-making software, earning $120,000-$220,000/year. Robotics Perception Scientists develop the computer vision and sensor fusion algorithms that allow machines to understand their environment, earning $110,000-$200,000/year. Transportation Safety Analysts evaluate autonomous vehicle performance data and develop safety standards for regulatory agencies, earning $80,000-$140,000/year.

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
Visual: Title slide with autonomous vehicle and sensor visualization
Say: "Right now, cars are driving themselves on public roads. They use lasers, cameras, and radar to see the world, and artificial intelligence to decide what to do. They are already safer than average human drivers in some conditions — and catastrophically confused in others. How do they actually work?"
Do: Open with a video clip or image of an autonomous vehicle in operation. Ask: who has seen a self-driving car? Who would ride in one? Who would NOT ride in one? Catalog the trust concerns.
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and vocabulary terms displayed
Say: "Today you are modeling the perception and decision system of an autonomous vehicle. You will discover why these systems work brilliantly most of the time and fail dangerously in edge cases — and why that gap might be the hardest engineering problem of the century."
Do: Have students read objectives. Pre-teach 'point cloud' with a visual showing raw LiDAR data. Pre-teach 'decision latency' by calculating distance traveled at highway speed during a 300ms delay.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: How does an autonomous vehicle build a real-time 3D understanding of its surroundings?
Say: "Your brain does this effortlessly — you glance at a street and instantly understand the scene. But your brain has 86 billion neurons refined by 500 million years of evolution. An autonomous vehicle has sensors, processors, and algorithms designed in the last twenty years. Let us see how close they get."
Do: Quick-write: Students estimate how many data points per second a self-driving car must process. Reveal the real number (millions) and discuss the computational challenge.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps with autonomous vehicle context
Say: "We are modeling a system where multiple sensors must agree on what is real, where milliseconds determine safety, and where the hardest problems are the situations nobody predicted."
Do: Preview LEVER steps. Emphasize that this model connects physics (how sensors work) to engineering (how data is processed) to ethics (how decisions are made).
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Seven component cards for autonomous vehicle perception model
Say: "Seven components. Two you control: LiDAR resolution and environmental conditions. Five that emerge from physics, algorithms, and engineering constraints. The key insight: safety margin is what is left over after every other component takes its toll."
Do: Guide through components. Demonstrate LiDAR point cloud density at different resolutions. Show how environmental degradation affects each sensor type differently.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows showing sensor data flowing through fusion to decisions
Say: "Every sensor feeds into fusion, fusion feeds into decisions, and decisions must happen faster than the car covers dangerous distance. The bottleneck is not any single sensor — it is the entire pipeline from photon to steering wheel."
Do: Help students map the data flow pipeline. Calculate the distance traveled during processing latency at different speeds. Highlight the sensor disagreement problem.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Simulation results for highway, rain, and novel object scenarios
Say: "Three scenarios that test the system from comfortable to catastrophic. Watch what happens to your safety margin as conditions get harder."
Do: Students predict safety margins before each scenario. The novel object scenario is the key insight — the system cannot safely handle what it cannot classify. Discuss what the vehicle should do when confused.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key findings about sensor fusion, latency, and edge cases
Say: "Self-driving cars are engineering marvels that work brilliantly in the 95% of driving that is routine. The challenge — and the reason full autonomy remains elusive — is the 5% of situations that require human-level understanding of context, intention, and common sense."
Do: Lead discussion on the gap between statistical pattern matching and genuine understanding. When is good enough actually good enough for public safety? How do we quantify acceptable risk?
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Autonomous vehicle sensor suite design challenge
Say: "A real company needs your sensor design for their autonomous delivery vehicles in YOUR city. You know the weather, the roads, the traffic patterns. Design the system."
Do: Groups design sensor suites for their local conditions. Must specify sensor types and positions, processing requirements, safety thresholds, and failure protocols. Present with model evidence.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: How Do Self-Driving Cars See?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
Every time you ride in a car, your brain performs an extraordinary feat of real-time perception: processing visual information from two eyes, interpreting depth, motion, color, and context, predicting the behavior of other road users, and making continuous steering and speed decisions — all while holding a conversation or listening to music. Autonomous vehicles attempt to replicate this capability using an array of electronic sensors and artificial intelligence algorithms. The engineering challenge is immense: the system must work perfectly in conditions ranging from bright sunshine to heavy rain, from empty highways to crowded school zones, and must handle situations that no programmer anticipated.

NGSS ALIGNMENT:
HS-PS4-1, HS-ETS1-2: Use mathematical representations to support a claim regarding relationships among the frequency, wavelength, and speed of waves traveling in various media. Design a solution to a complex real-world problem by breaking it down into smaller, more manageable problems that can be solved through engineering.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Developing and Using Models
  Students develop computational models of sensor fusion and autonomous perception to predict how changes in sensor configuration, environmental conditions, and processing parameters affect driving safety.
• Disciplinary Core Idea: PS4.A Wave Properties / ETS1.B Developing Possible Solutions
  Students model how electromagnetic waves (laser light, radio waves) interact with matter to create sensor measurements, and engineer solutions to the perception and decision-making challenges of autonomous driving.
• Crosscutting Concept: Systems and System Models
  Students analyze the autonomous vehicle as an integrated system where sensors, processors, and actuators must work together with precise timing, and where failure in any subsystem cascades through the entire driving system.

PACING GUIDE:
• Step 1 (Locate): 8-10 minutes
• Step 2 (Establish): 8-10 minutes
• Step 3 (Visualize & Evaluate): 10-12 minutes
• Step 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: LiDAR, Point Cloud, Sensor Fusion, Object Classification, Decision Latency
□ Prepare How does an autonomous vehicle build a real-time 3D understanding of its surroundings from raw sensor data — and can it ever be trusted to make life-or-death driving decisions discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify seven key components of an autonomous vehicle perception system: LiDAR resolution, camera detection accuracy, sensor fusion confidence, processing latency, environmental degradation, decision algorithm reliability, and safety margin.
• Establish: Students map relationships showing that LiDAR resolution and environmental degradation are the primary drivers of sensor fusion confidence, which combined with processing latency determines the safety margin available for decision-making at any given speed.
• Visualize: Students build a computational model showing the seven-component autonomous perception system with sensor data flowing through fusion into decision-making.
• Evaluate: Students run clear highway, heavy rain urban, and novel object emergency scenarios to discover the conditions under which the autonomous system maintains safe operation versus requiring human intervention.
• Revise: Students add V2X communication, prediction horizon, or ethical decision framework to model more realistic autonomous driving complexity and edge-case handling.

BACKGROUND CONTENT:
• LiDAR: Seeing in 3D with Light:
  LiDAR sensors emit thousands of short laser pulses per second — typically 905 nanometer or 1550 nanometer infrared light — and measure the precise time each pulse takes to return after reflecting off objects. Because light travels at a known constant speed (approximately 300 million meters per second), the round-trip time reveals the exact distance to each reflection point. A modern automotive LiDAR unit generates 300,000 to 2 million points per second, creating a detailed 3D point cloud of everything within 200 meters. This point cloud provides precise geometric information — the shape, size, and distance of every object — but contains no color or texture information. LiDAR works equally well in daylight and darkness because it generates its own illumination, but performance degrades in rain, fog, and snow because water droplets scatter the laser beams, creating false returns and reducing range.

• Computer Vision: Understanding What the Sensors See:
  Cameras provide rich color and texture data that complement LiDAR's geometric precision. Convolutional neural networks trained on millions of labeled images can classify objects — distinguishing a child from a fire hydrant, a stop sign from a billboard, a pedestrian crossing from a shadow on the road. Modern autonomous vehicles use 8-12 cameras covering a full 360-degree view, often with both wide-angle and telephoto lenses. The neural networks process each camera frame (typically 30-60 frames per second) through dozens of computational layers that detect edges, textures, shapes, and contextual relationships. However, cameras share human vision's weaknesses: they struggle with glare, darkness, and weather that reduces visibility. They also inherit biases from their training data — a classifier trained primarily on images from sunny California may fail to recognize pedestrians in winter clothing or objects partially obscured by snow.

• Sensor Fusion: Building a Unified World Model:
  No single sensor provides complete information for safe driving. LiDAR provides precise 3D geometry but no color. Cameras provide rich visual detail but imprecise depth. Radar provides velocity measurements and works through weather but has low spatial resolution. Sensor fusion algorithms combine these complementary data streams into a single unified environmental model. The fusion process uses probabilistic methods — typically Kalman filters or particle filters — to weight each sensor's contribution based on its reliability in current conditions. When a LiDAR point cloud shows an object at 50 meters and a camera classifies it as a pedestrian, the fused model represents a pedestrian at 50 meters with high confidence. When sensors disagree — perhaps the camera sees nothing but LiDAR detects something — the system must resolve the conflict, usually by increasing uncertainty and triggering cautious behavior. The computational cost of real-time sensor fusion is enormous, requiring specialized processors that consume hundreds of watts of power.

• The Decision-Making Challenge:
  Perception — knowing what is around the car — is only half the problem. The vehicle must also decide what to do. Path-planning algorithms calculate the optimal trajectory considering road geometry, traffic rules, other vehicles' predicted movements, and safety constraints. In normal driving, this is relatively straightforward: follow the lane, maintain safe distance, obey signals. The challenge explodes in complexity at intersections, merges, and construction zones where multiple agents interact with conflicting intentions. And then there are edge cases: a ball rolling into the street (a child may follow), an emergency vehicle approaching from behind, a road surface that looks like a lane marking, or a completely novel situation the system has never encountered. Human drivers handle these with general intelligence, social awareness, and common sense. Current autonomous systems handle them with statistical pattern matching that can fail catastrophically when reality deviates from training data. This gap between statistical perception and genuine understanding is the central unsolved challenge of autonomous driving.

COMMON MISCONCEPTIONS:
• "Self-driving cars see the world the same way humans do"
  Reality: Autonomous vehicles and humans use fundamentally different perception mechanisms. Humans process visual information through biological neural networks refined by millions of years of evolution, creating a rich understanding of context, intention, and social cues. Autonomous vehicles process discrete sensor measurements through mathematical algorithms that detect statistical patterns without understanding meaning. A human sees a person looking at their phone while walking toward a crosswalk and predicts they might step into traffic without looking. An autonomous system sees a cluster of LiDAR points classified as a pedestrian and predicts movement based on trajectory statistics. The model shows how this gap manifests in edge cases where contextual understanding matters.
  Strategy: Compare: Show students the same scene from a human perspective and from the autonomous vehicle's sensor view (point cloud plus bounding boxes). Discuss what information is present in the human view but absent from the sensor view — intention, attention, emotional state, social context.

• "More sensors always make the car safer"
  Reality: Additional sensors provide more data but also increase processing latency, system complexity, and potential points of failure. Each new sensor must be integrated into the fusion algorithm, calibrated against all other sensors, and its data processed in real time. Beyond a certain point, the added processing delay from handling more data can actually reduce safety margin more than the improved perception adds. The model demonstrates the optimal sensor count where the trade-off between perception improvement and processing latency reaches its best balance.
  Strategy: Experiment: Model adding sensors incrementally and tracking both sensor fusion confidence and processing latency. Find the sweet spot where further sensors degrade rather than improve overall safety margin due to processing overhead.

• "Autonomous vehicles just need more training data to handle edge cases"
  Reality: More training data improves performance on situations similar to what has been seen before, but it cannot prepare the system for truly novel situations. The real world has an effectively infinite number of possible scenarios, and no dataset — however large — can include them all. A car trained on millions of hours of driving data in temperate climates may still fail when encountering its first dust storm, its first parade, or its first earthquake. The fundamental limitation is not data quantity but the gap between pattern recognition and causal reasoning. The model shows how classification confidence drops to near-random levels for objects and scenarios outside the training distribution.
  Strategy: Demonstration: Present the classification system with progressively more unusual objects — from common (car, pedestrian, bicycle) to uncommon (horse, wheelchair, scooter) to rare (overturned furniture, escaped animal, fallen tree) — and show how confidence decreases with novelty regardless of total training data volume.

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
Big Question: How does an autonomous vehicle build a real-time 3D understanding of its surroundings from raw sensor data — and can it ever be trusted to make life-or-death driving decisions?
Answer: Self-driving cars construct their understanding of the world through a sophisticated sensor fusion pipeline. LiDAR creates precise 3D point clouds using laser time-of-flight measurements. Cameras provide color and texture information for object classification using trained neural networks. Radar detects object velocity and works through weather that degrades optical sensors. These data streams are fused into a unified environmental model, updated dozens of times per second, from which path-planning algorithms calculate the safest trajectory. The system works remarkably well in common driving scenarios — highway cruising, lane following, and predictable intersections. However, fundamental challenges remain: processing latency means the car always reacts to slightly outdated information, environmental conditions can simultaneously degrade multiple sensors, and novel situations that fall outside the training distribution force the system to extrapolate in ways that may fail unpredictably. The question is not whether autonomous vehicles can drive — they demonstrably can — but whether they can handle the full diversity of real-world driving, including the rare catastrophic scenarios that human drivers navigate using general intelligence, social understanding, and common sense.

Simulation Answers:
• Clear Highway Driving Scenario: With maximum LiDAR resolution and minimal environmental degradation, the sensor fusion system achieves high confidence (greater than 95%) for all detected objects within 200 meters. At 30 mph, the safety margin is large — the vehicle can detect, classify, and respond to obstacles with hundreds of feet to spare. As speed increases to 75 mph, the safety margin shrinks because the vehicle covers 110 feet per second while processing latency remains constant at 200-300 milliseconds. At 75 mph, the processing delay alone consumes 22-33 feet of the safety margin. The model reveals that maximum safe speed is fundamentally limited by processing latency even in perfect sensor conditions.
• Heavy Rain Urban Intersection Scenario: Rain reduces LiDAR effective range by approximately 40% (from 200 meters to 120 meters) due to laser scatter from water droplets, and camera classification accuracy drops by approximately 30% due to water on lenses, reduced visibility, and reflections. Sensor fusion confidence decreases to 70-80% because the two primary sensors are simultaneously degraded. Radar becomes the most reliable sensor in this scenario but provides only coarse spatial information. The system compensates by reducing speed, increasing following distance, and lowering the confidence threshold for cautious behaviors. The model demonstrates why multi-sensor redundancy with diverse physics (optical versus radio) is essential — in rain, radar maintains functionality that optical sensors lose.
• Novel Object Emergency Scenario: When an unclassified object appears in the vehicle's path, the classification neural network returns low-confidence probabilities spread across multiple categories — it cannot determine what the object is. The decision algorithm must act without understanding: it knows something is there (LiDAR confirms a physical obstacle) but not what it is (camera classification fails). Conservative algorithms treat unclassified objects as pedestrians (worst-case assumption), triggering maximum braking. Aggressive algorithms may attempt to steer around the object. The model reveals that the vehicle's response to novel objects is entirely determined by its programmed assumptions, not by understanding — and that no finite training dataset can prepare the system for every possible real-world object.

Reflection Exemplars:
• Q: Why is processing latency a fundamental safety limit rather than just an engineering inconvenience?
  A: Processing latency creates a temporal blind spot during which the vehicle is acting on outdated information. At 65 mph (95 feet per second), a 300-millisecond processing delay means the vehicle has traveled 29 feet since the data it is currently acting on was collected. During those 29 feet, a pedestrian could step off the curb, a car ahead could slam its brakes, or debris could fall from a truck. No sensor improvement can fix this — even perfect sensors cannot compensate for the time required to process their data. The model shows that safety margin must always include a latency buffer proportional to speed, creating a hard upper bound on safe autonomous speed for any given computing capability. Faster processors help, but the speed of light through fiber optics and the irreducible complexity of fusion algorithms ensure latency can never reach zero.
• Q: Why are edge cases the central unsolved problem of autonomous driving?
  A: Edge cases are driving situations that are rare, novel, or ambiguous — a mattress on the highway, a traffic officer using hand signals that override a traffic light, a child chasing a ball between parked cars. The model demonstrates that the autonomous system's performance degrades sharply when scenarios fall outside its training distribution. A human driver recognizes a ball rolling into the street and predicts a child may follow because they understand the general concept of children, play, and cause-and-effect. The autonomous system must have seen enough labeled examples of balls-followed-by-children in its training data to make this prediction statistically. The fundamental gap is between statistical pattern matching (what the system does) and causal understanding (what humans do). The model cannot fully capture this gap because the model itself relies on predefined scenarios — it cannot generate truly novel situations.

STEM CHALLENGE GUIDANCE:
Title: Design an Autonomous Vehicle Sensor Suite
Mission: Design an optimal sensor configuration for an autonomous vehicle that must operate safely in your city's specific driving conditions, addressing sensor selection, placement, fusion architecture, and failure mode handling.
Scenario: A transportation company is deploying autonomous delivery vehicles in your city and has hired your team to design the sensor suite and perception system. Your city has specific challenges — weather patterns, road conditions, pedestrian density, and infrastructure — that the sensor system must handle. You must select and position sensors, design the fusion architecture, establish minimum safety margins for different conditions, and create protocols for what the vehicle does when sensor confidence drops below safe thresholds.
Introduction: Present the challenge: A transportation company is deploying autonomous delivery vehicles in your city and needs your team to design the complete sensor suite and perception system. Your design must account for local weather patterns, road infrastructure, pedestrian density, and traffic conditions. You must specify sensor selection and placement, fusion architecture, minimum safety thresholds, speed limits for different conditions, and failure protocols for sensor degradation and novel object encounters.

Key Concepts:
• Redundancy and Diversity: Reliable autonomous perception requires not just multiple sensors but sensors based on different physical principles. Two cameras provide redundancy (backup if one fails) but not diversity (both fail in darkness). A camera plus radar provides both redundancy and diversity because they fail in different conditions. System reliability increases with both the number and the physical diversity of sensors.
• Operational Design Domain: The specific set of conditions under which an autonomous vehicle is designed to operate safely — including geography, road type, speed range, weather, and time of day. No current system operates safely in all conditions, so defining and enforcing the operational design domain boundary is critical for safety.
• Safety of the Intended Functionality: The engineering standard (ISO 21448) that addresses hazards caused by functional insufficiency of the perception system — situations where the sensors work correctly but the system still makes unsafe decisions because the environment is too complex, too novel, or too ambiguous for the algorithms to handle correctly.

Evaluation Rubric:
• Expert (4): Design includes specific sensor selections with physics-based justification, detailed placement geometry with coverage analysis, quantitative safety thresholds for different conditions, failure mode protocols with model evidence, and honest assessment of scenarios where the system would require human intervention
• Proficient (3): Design addresses sensor selection, fusion architecture, and safety thresholds with model evidence, and considers failure modes and operational design domain limits
• Developing (2): Design describes sensor configuration but lacks quantitative safety analysis or does not address failure modes and edge cases
• Beginning (1): Design is incomplete, ignores environmental degradation effects, or uncritically assumes autonomous operation is safe in all conditions

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a sensor comparison table showing LiDAR (range: 200m, resolution: high, weather sensitivity: moderate, cost: $1,000-$10,000), camera (range: variable, resolution: very high, weather sensitivity: high, cost: $50-$500), and radar (range: 250m, resolution: low, weather sensitivity: low, cost: $100-$500) so students can evaluate trade-offs
  • Use a speed-distance-time calculator: at different speeds, show how far the car travels during 100ms, 200ms, and 500ms processing delays, making the latency problem concrete and visceral
  • Sentence frames: 'In our sensor design, we selected __ LiDAR units and __ cameras because __, which provides a safety margin of __ feet at __ mph in __ conditions based on our model showing __'

Extensions (Advanced Learners):
  • Research the NHTSA crash investigation reports for autonomous vehicle incidents involving Tesla, Waymo, or Cruise and analyze what perception failures caused each incident using your model framework
  • Investigate how different autonomous vehicle companies (Waymo, Cruise, Tesla, Mobileye) have made fundamentally different sensor architecture decisions and evaluate which approach your model predicts will be safest
  • Design an autonomous vehicle system for a specific challenging environment — arctic conditions, unpaved roads, or dense urban areas in developing countries — and explain how the sensor requirements differ from standard configurations

Cross-Curricular Connections:
  • Math: Calculate the minimum sensor detection range required for safe autonomous driving at different speeds. Given a processing latency of 250 milliseconds, a braking distance that increases with the square of velocity, and a required safety margin of 50 feet, derive the equation relating maximum safe speed to sensor range and solve for speeds of 25, 45, and 65 mph.
  • ELA: Write a policy recommendation to your city council evaluating whether autonomous delivery vehicles should be permitted on city streets. Use evidence from your model to address sensor capabilities and limitations, safety thresholds, weather-related restrictions, and the conditions under which autonomous operation should be suspended.
  • Ethics: Analyze the trolley problem as it applies to autonomous vehicle programming: when a collision is unavoidable, how should the vehicle's decision algorithm prioritize between different outcomes? Research how different cultures and legal frameworks approach this question and evaluate whether a single global standard is possible or desirable.

CAST ALIGNMENT:
• Model how LiDAR resolution, camera accuracy, and radar data are fused into a unified environmental representation with quantifiable confidence levels
• Analyze the relationship between processing latency, vehicle speed, and safety margin to determine the maximum safe operating speed for given computing hardware
• Evaluate the conditions under which autonomous vehicle sensor systems fail to provide adequate environmental awareness for safe driving decisions

CAST-Style Assessment Questions:
• Multiple Choice: An autonomous vehicle traveling at 65 mph has a total processing latency of 300 milliseconds from sensor input to actuator response. If a pedestrian steps into the road 150 feet ahead, and the vehicle requires 120 feet to stop at this speed, does the vehicle have sufficient distance to stop safely? Show your calculation including the distance traveled during the processing delay.
• Constructed Response: Using evidence from your model, explain why autonomous vehicles use multiple sensor types rather than relying solely on the highest-resolution sensor. Address how environmental conditions affect different sensors differently and how sensor fusion provides reliability that no single sensor can achieve alone.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: How Do Self-Driving Cars See?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. What do you already know about how self-driving cars detect objects around them, and what sensors do you think they use?

   _________________________________________________________

   _________________________________________________________

2. Why might a self-driving car have difficulty in heavy rain or fog when a human driver can still navigate safely?

   _________________________________________________________

   _________________________________________________________

3. Draw a diagram showing how you think a self-driving car builds a picture of its surroundings using different types of sensors.

   [DRAWING BOX]

4. What is the difference between a car that detects an obstacle and a car that decides what to do about it?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ LiDAR                         
___ Point Cloud                   
___ Sensor Fusion                 
___ Object Classification         
___ Decision Latency              

A. Light Detection and Ranging — a sensor that emits thousands of laser pulses per second and measures the time each pulse takes to bounce back from objects, generating a precise 3D point cloud of the vehicle's surroundings with centimeter-level accuracy at ranges up to 200 meters
B. A three-dimensional dataset consisting of millions of individual distance measurements collected by LiDAR, where each point represents a specific location in space — the autonomous vehicle's perception system must process and classify this raw data in real time to identify roads, vehicles, pedestrians, and obstacles
C. The computational process of combining data from multiple sensor types — LiDAR point clouds, camera images, radar returns, and GPS coordinates — into a single unified model of the environment that is more accurate and reliable than any individual sensor alone
D. The machine learning task of identifying what each detected object is — distinguishing a pedestrian from a mailbox, a bicycle from a motorcycle, a plastic bag from a rock — using trained neural networks that must make correct identifications within milliseconds at highway speeds
E. The total time from sensor data acquisition through perception processing, object classification, path planning, and actuator response — typically 100-500 milliseconds in current systems — during which a vehicle traveling at 65 mph covers 10-50 feet and cannot respond to new information

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

SCENARIO: Clear Highway Driving
Settings: Maximum LiDAR, minimal environmental degradation, increasing speed
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Heavy Rain Urban Intersection
Settings: 40% LiDAR degradation, 30% camera degradation, complex urban scene
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Novel Object Emergency
Settings: Unclassified obstacle appears in the vehicle's path at highway speed
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

1. How does your model demonstrate the fundamental trade-off between sensor resolution and processing latency?

   _________________________________________________________

   _________________________________________________________

2. Why is sensor fusion more valuable than simply using the best single sensor, and what happens when sensors provide contradictory information?

   _________________________________________________________

   _________________________________________________________

3. What does your model reveal about why autonomous vehicles perform differently in clear conditions versus adverse weather?

   _________________________________________________________

   _________________________________________________________

4. How would your model change if processing latency could be reduced to near-zero through advanced computing hardware?

   _________________________________________________________

   _________________________________________________________

5. What are the limitations of modeling autonomous vehicle safety when real-world driving includes situations that have never occurred before?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. How does an autonomous vehicle build a real-time 3D understanding of its surroundings from raw sensor data — and can it ever be trusted to make life-or-death driving decisions? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Developing and Using Models
   □ Disciplinary Core Idea: PS4.A Wave Properties / ETS1.B Developing Possible Solutions
   □ Crosscutting Concept: Systems and System Models

3. What are the limitations of modeling autonomous vehicle safety when real-world driving includes situations that have never occurred before?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design an Autonomous Vehicle Sensor Suite
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design an optimal sensor configuration for an autonomous vehicle that must operate safely in your city's specific driving conditions, addressing sensor selection, placement, fusion architecture, and failure mode handling.

SCENARIO: A transportation company is deploying autonomous delivery vehicles in your city and has hired your team to design the sensor suite and perception system. Your city has specific challenges — weather patterns, road conditions, pedestrian density, and infrastructure — that the sensor system must handle. You must select and position sensors, design the fusion architecture, establish minimum safety margins for different conditions, and create protocols for what the vehicle does when sensor confidence drops below safe thresholds.

GUIDING QUESTIONS:
• What combination of sensors provides adequate redundancy for your city's worst weather conditions?
• What is the minimum acceptable sensor fusion confidence for the vehicle to continue autonomous operation versus requesting human intervention?
• How should the vehicle behave when it encounters an object it cannot classify — stop, slow down, change lanes, or something else?

DESIGN THINKING:
• How many and what type of LiDAR units would you mount on the vehicle and where would you position them to minimize blind spots?

  _________________________________________________________

• What camera specifications (resolution, frame rate, field of view, low-light sensitivity) are required for reliable object classification at highway speeds?

  _________________________________________________________

• What is your maximum acceptable processing latency and how does this constrain your computing hardware requirements?

  _________________________________________________________

• What failure cascade protocol would you implement when environmental conditions degrade sensor confidence below your safety threshold?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Design includes specific sensor selections with physics-based justification, detailed placement geometry with coverage analysis, quantitative safety thresholds for different conditions, failure mode protocols with model evidence, and honest assessment of scenarios where the system would require human intervention
• Proficient (3): Design addresses sensor selection, fusion architecture, and safety thresholds with model evidence, and considers failure modes and operational design domain limits
• Developing (2): Design describes sensor configuration but lacks quantitative safety analysis or does not address failure modes and edge cases
• Beginning (1): Design is incomplete, ignores environmental degradation effects, or uncritically assumes autonomous operation is safe in all conditions

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CAST-Aligned Pre/Post Assessment

### Administration Instructions

These 5 multiple-choice questions are administered identically as both a pre-assessment (before Activity 1) and a post-assessment (after Activity 4). Score each out of 5. Learning growth = post-score minus pre-score.

Questions follow the California Science Test (CAST) stimulus-response format. Each item is three-dimensional, assessing a Science and Engineering Practice (SEP), Disciplinary Core Idea (DCI), and Crosscutting Concept (CCC) simultaneously, aligned to HS-PS4-1, HS-ETS1-2.

---

### Question 1

CAST Alignment: SEP 2.1.1 (Develop and use a model to represent relationships) + DCI PS4.A (Wave properties and relationships) + CCC4 (Systems and system models)

A self-driving car company reports data from 10 million miles of autonomous driving in California. The car's sensor array includes 8 cameras (visible light), 5 LiDAR units (laser ranging), 6 radar units (radio wave detection), and 12 ultrasonic sensors (close-range detection). The system processes 1.5 terabytes of sensor data per hour, fusing inputs from all sensor types into a unified 3D model of the environment updated 20 times per second. Despite this capability, the system has recorded 147 instances where sensor fusion produced incorrect object classifications, 23 of which required emergency human intervention.

A student's model shows that increasing LiDAR resolution from 100 to 400 points per square meter improves object detection by 25% but increases processing latency from 150ms to 350ms. At 65 mph, what is the safety implication of this trade-off?

A. Higher resolution is always safer because detection is more accurate
B. The improved detection is offset by increased latency: the vehicle now travels 35 feet instead of 15 feet before responding, meaning the system detects objects better but reacts to them slower, potentially creating a net decrease in safety at highway speeds
C. The vehicle should switch to camera-only mode at high speeds
D. Processing latency has no effect on safety if detection accuracy is high

Correct Answer: B

Feedback: Better detection is meaningless if the response comes too late. The 200ms increase in latency adds 20 feet of travel before response. Optimal system design must balance detection quality against response time for the given speed envelope. If you chose A, this response overgeneralizes without considering the specific mechanisms and evidence presented. Detection accuracy and response speed are coupled safety factors. The additional 200ms latency means the vehicle travels an extra 20 feet before reacting. At highway speeds, the faster but less detailed system may actually be safer because it responds sooner. If you chose D, this answer does not account for the key mechanism or relationship the evidence demonstrates. Detection accuracy and response speed are coupled safety factors. The additional 200ms latency means the vehicle travels an extra 20 feet before reacting. At highway speeds, the faster but less detailed system may actually be safer because it responds sooner. If you chose C, this choice oversimplifies a multi-factor system by focusing on a single variable. Detection accuracy and response speed are coupled safety factors. The additional 200ms latency means the vehicle travels an extra 20 feet before reacting. At highway speeds, the faster but less detailed system may actually be safer because it responds sooner.
---

### Question 2

CAST Alignment: SEP 2.1.2 (Determine relationships among system components) + DCI PS4.A (Wave properties and relationships) + CCC2 (Cause and effect)

A computational model of LiDAR perception explains how self-driving cars measure distance. The LiDAR emits 128 laser beams rotating 20 times per second, each beam reflecting off objects and returning to the sensor. The time-of-flight measurement (speed of light times half the round-trip time) provides distance accurate to 2 centimeters at 200 meters range. The model reveals that LiDAR creates a point cloud of 2.4 million 3D points per second, but these points are sparse: at 100 meters, the spacing between points is approximately 10 cm, meaning small objects (like a thin pole or a partially occluded pedestrian) may fall between scan lines and be missed entirely.

The model demonstrates that sensor fusion confidence drops sharply when LiDAR and camera disagree about an object's classification. A LiDAR return suggests a large solid object, but the camera classifies it as a plastic bag. How should the decision algorithm handle this conflict?

A. The system should apply a conservative safety hierarchy: treat the object as the more dangerous interpretation (solid obstacle) until additional sensor data or time resolves the conflict, because the cost of hitting a solid object far exceeds the cost of briefly avoiding a plastic bag
B. Ignore both sensors and maintain current speed and direction
C. Always trust the camera because it provides richer visual information
D. Average the two sensor readings to create a compromise classification

Correct Answer: A

Feedback: Asymmetric risk demands conservative decision-making. Misclassifying a solid object as a bag could be fatal, while briefly treating a bag as a solid object merely causes a momentary slowdown. The cost of being wrong differs dramatically between the two errors. If you chose C, this response overgeneralizes without considering the specific mechanisms and evidence presented. When sensors disagree, the system must consider the asymmetric consequences of each possible error. Treating a bag as a rock causes a brief inconvenience; treating a rock as a bag could cause a fatal collision. Conservative classification, defaulting to the more dangerous interpretation, is the safety-rational approach. If you chose D, this answer does not account for the key mechanism or relationship the evidence demonstrates. When sensors disagree, the system must consider the asymmetric consequences of each possible error. Treating a bag as a rock causes a brief inconvenience; treating a rock as a bag could cause a fatal collision. Conservative classification, defaulting to the more dangerous interpretation, is the safety-rational approach. If you chose B, this choice does not account for the key mechanism or relationship the evidence demonstrates. When sensors disagree, the system must consider the asymmetric consequences of each possible error. Treating a bag as a rock causes a brief inconvenience; treating a rock as a bag could cause a fatal collision. Conservative classification, defaulting to the more dangerous interpretation, is the safety-rational approach.
---

### Question 3

CAST Alignment: SEP 2.1.2 (Determine relationships among components) + DCI ETS1.B (Develop solutions to engineering problems) + CCC4 (Describe components and interactions)

Engineers analyze a scenario where a self-driving car must classify an ambiguous object on the road ahead. Camera data shows a dark shape, but glare from the setting sun makes color and texture unreliable. LiDAR data shows a 3D point cluster consistent with either a plastic bag (safe to drive over) or a small animal (requiring emergency braking). Radar data shows no metallic signature. The sensor fusion algorithm must assign probabilities to each interpretation and decide whether to brake, swerve, or continue. The model shows that this decision must be made within 150 milliseconds at highway speed, leaving no time for additional sensor sweeps.

A student observes that the model's decision algorithm performs well in scenarios represented in its training data but fails unpredictably in novel situations (e.g., a fallen tree across the road). What fundamental limitation of machine-learning-based decision systems does this reveal?

A. The algorithm should ignore novel scenarios and continue driving normally
B. The algorithm needs more processing power to handle novel scenarios
C. All novel scenarios can be solved by adding more training data
D. Machine learning systems can only reliably handle situations similar to their training data; truly novel scenarios that fall outside the training distribution expose the system's inability to reason from first principles, unlike human drivers who can improvise

Correct Answer: D

Feedback: This is the 'long tail' problem in autonomous driving. ML systems excel at pattern matching within their training distribution but cannot reason about genuinely novel situations. This limitation is why fully autonomous driving in all conditions remains unsolved. If you chose B, this response does not account for the key mechanism or relationship the evidence demonstrates. The fundamental issue is distribution shift: ML systems perform well within their training distribution but degrade unpredictably on novel inputs. Human drivers can reason about unfamiliar situations using general knowledge, but current AI systems lack this ability, creating the 'long tail' of rare but critical edge cases. If you chose C, this answer overgeneralizes without considering the specific mechanisms and evidence presented. The fundamental issue is distribution shift: ML systems perform well within their training distribution but degrade unpredictably on novel inputs. Human drivers can reason about unfamiliar situations using general knowledge, but current AI systems lack this ability, creating the 'long tail' of rare but critical edge cases. If you chose A, this choice overgeneralizes without considering the specific mechanisms and evidence presented. The fundamental issue is distribution shift: ML systems perform well within their training distribution but degrade unpredictably on novel inputs. Human drivers can reason about unfamiliar situations using general knowledge, but current AI systems lack this ability, creating the 'long tail' of rare but critical edge cases.
---

### Question 4

CAST Alignment: SEP 2.1.4 (Represent mechanisms to explain/predict events) + DCI PS4.A (Wave properties and relationships) + CCC7 (Stability and change)

Researchers testing self-driving car perception in adverse conditions document failure modes. In heavy rain, camera images show streaking and refraction that confuse object detection algorithms. LiDAR beams scatter off rain droplets, creating phantom objects (false positives) in the point cloud. Radar penetrates rain effectively but cannot determine object shape. The computational model shows that sensor fusion performance degrades nonlinearly with precipitation intensity: at 10 mm/hour (moderate rain), object detection accuracy drops from 99.5% to 94%; at 50 mm/hour (heavy rain), accuracy drops to 76%, below the safety threshold for autonomous operation.

The model shows that Environmental Degradation (heavy rain) reduces LiDAR range by 40%, camera detection by 60%, but radar by only 5%. What does this demonstrate about the critical role of sensor diversity in the system?

A. The degradation percentages are too small to affect driving safety
B. Sensor diversity provides graceful degradation: when weather impairs optical sensors, radar maintains environmental awareness, preventing complete perception failure. No single sensor type is optimal in all conditions, making diversity a safety requirement rather than a luxury
C. The vehicle should only use radar and eliminate LiDAR and cameras
D. Heavy rain makes autonomous driving completely impossible regardless of sensors

Correct Answer: B

Feedback: The asymmetric impact of rain across sensor types demonstrates why diversity is essential. Radar's weather resilience compensates for optical sensor degradation, maintaining minimum perception capability. Eliminating any sensor type would create conditions where the system is blind. If you chose C, this response oversimplifies a multi-factor system by focusing on a single variable. Sensor diversity provides resilience through complementary failure modes. Rain severely degrades optical sensors but barely affects radar. Without sensor diversity, a single weather condition could eliminate all perception. The system degrades gracefully rather than catastrophically. If you chose D, this answer does not account for the key mechanism or relationship the evidence demonstrates. Sensor diversity provides resilience through complementary failure modes. Rain severely degrades optical sensors but barely affects radar. Without sensor diversity, a single weather condition could eliminate all perception. The system degrades gracefully rather than catastrophically. If you chose A, this choice overgeneralizes without considering the specific mechanisms and evidence presented. Sensor diversity provides resilience through complementary failure modes. Rain severely degrades optical sensors but barely affects radar. Without sensor diversity, a single weather condition could eliminate all perception. The system degrades gracefully rather than catastrophically.
---

### Question 5

CAST Alignment: SEP 2.1.4 (Represent mechanisms to predict a scientific event) + DCI ETS1.B (Develop solutions to engineering problems) + CCC4 (Describe system components and interactions)

A regulatory agency evaluates whether self-driving cars should be required to achieve zero accidents before deployment or if a statistical safety threshold is sufficient. Human drivers in California cause 1.13 fatalities per 100 million vehicle miles. Current autonomous systems have achieved 0.4 fatalities per 100 million miles in testing, but the confidence interval is wide due to limited total miles. The computational model shows that proving statistical superiority over human drivers at a 95% confidence level would require approximately 11 billion miles of autonomous driving, taking the current test fleet 400 years to accumulate. The agency must decide what evidence standard is appropriate for deployment.

Based on the autonomous vehicle model, which conclusion about the relationship between safety margin and processing latency is best supported by the simulation data?

A. Safety margin only depends on the driver's reaction time, not the computer's processing time
B. Safety margin is independent of processing latency at all speeds
C. Safety margin decreases proportionally with both increasing speed and increasing processing latency, because the distance traveled during processing time is the product of speed and latency. This means safety-critical decisions are fundamentally constrained by computation speed, and faster algorithms directly translate to safer vehicles
D. Reducing speed to zero is the only way to ensure an adequate safety margin

Correct Answer: C

Feedback: The blind distance (speed x latency) directly determines the minimum safety margin. This mathematical relationship means that improving processing speed has a direct, quantifiable safety benefit that increases with vehicle speed. If you chose B, this response overgeneralizes without considering the specific mechanisms and evidence presented. Safety margin = available stopping distance minus blind distance (speed x latency). As speed or latency increases, the blind distance grows and the safety margin shrinks. Faster processing directly and proportionally improves safety at any given speed. If you chose A, this answer oversimplifies a multi-factor system by focusing on a single variable. Safety margin = available stopping distance minus blind distance (speed x latency). As speed or latency increases, the blind distance grows and the safety margin shrinks. Faster processing directly and proportionally improves safety at any given speed. If you chose D, this choice oversimplifies a multi-factor system by focusing on a single variable. Safety margin = available stopping distance minus blind distance (speed x latency). As speed or latency increases, the blind distance grows and the safety margin shrinks. Faster processing directly and proportionally improves safety at any given speed.
---

### Answer Key

Question 1: B (Cognitive Level: Identify -- SEP 2.1.1, DCI HS-PS4-1, CCC4)
Question 2: A (Cognitive Level: Reason -- SEP 2.1.2, DCI HS-PS4-1, CCC2)
Question 3: D (Cognitive Level: Reason -- SEP 2.1.2, DCI HS-PS4-1, CCC4)
Question 4: B (Cognitive Level: Reason + Evidence -- SEP 2.1.4, DCI HS-ETS1-2, CCC7)
Question 5: C (Cognitive Level: Predict + Apply -- SEP 2.1.4, DCI HS-ETS1-2, CCC4)

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-11/G11L3-L07/G11L3-L07-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-11/G11L3-L07/G11L3-L07-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-11/G11L3-L07/G11L3-L07-Student-Presentation.pptx] |
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