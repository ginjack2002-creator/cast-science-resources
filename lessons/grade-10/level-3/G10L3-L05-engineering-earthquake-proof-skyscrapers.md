# Lesson: Engineering Earthquake-Proof Skyscrapers

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G10L3-L05 |
| **Grade** | 10th Grade — Level 3: Advanced Engineering & Design |
| **Lesson Name** | Engineering Earthquake-Proof Skyscrapers |
| **Status** | Template |

---

## Platform

### Title
**Engineering Earthquake-Proof Skyscrapers — Modeling the Physics of Structural Survival Under Seismic Forces**

### Overview
Earthquakes generate forces that can accelerate the ground at the same rate as gravity — imagine the floor suddenly tilting 90 degrees. Buildings, which are designed to resist vertical gravity loads, must also survive violent horizontal shaking. The engineering of earthquake-resistant structures is a battle against F=ma: the more mass a building has, the greater the forces it must withstand during acceleration. Students investigate the driving question: How can a million-ton building survive forces that level entire cities — and why do some skyscrapers collapse while others barely sway? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of a modern skyscraper with visible base isolation bearings and a cutaway showing the tuned mass damper at the top, set against a dramatic sky with subtle motion blur suggesting earthquake movement, engineering detail visible]

### Grade
10th Grade — Level 3: Advanced Engineering & Design

### NGSS Standard
**HS-ESS2-2, HS-PS2-1**: Analyze geoscience data to make the claim that one change to Earth's surface can create feedbacks that cause changes to other Earth systems. Analyze data to support the claim that Newton's second law of motion describes the mathematical relationship among the net force on a macroscopic object, its mass, and its acceleration.

### Learning Objectives
- Model how nine interdependent structural and seismic variables determine whether a building survives an earthquake
- Analyze the engineering trade-offs between building mass, flexibility, and damping systems in seismic design
- Evaluate how resonance frequency matching between seismic waves and building natural frequency amplifies destruction
- Predict the seismic conditions under which different structural designs transition from safe to catastrophic failure

### Component List (Starting Model: 9 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Seismic Wave Intensity | External | The peak ground acceleration (PGA) of the earthquake at the building site, measured in g-forces — from 0.1g for minor quakes to 2.0+g for extreme events near the fault |
| Building Mass | Internal | The total weight of the structure including all floors, materials, contents, and occupants — heavier buildings experience greater inertial forces (F=ma) during seismic acceleration |
| Damper Effectiveness | Internal | The percentage of oscillation energy absorbed by tuned mass dampers, viscous dampers, or friction dampers — ranging from 20% for basic systems to 60% for advanced multi-mode dampers |
| Foundation Flexibility | External | The degree to which the foundation system (base isolators, rocking foundations, or flexible piles) decouples the building from ground motion — measured in displacement capacity |
| Resonance Frequency | Internal | The relationship between the building's natural oscillation period and the dominant frequency of the seismic waves — when they match, forces amplify catastrophically |
| Material Strength | Internal | The capacity of structural members (steel, reinforced concrete, composite) to resist forces without yielding or fracturing — measured in megapascals of tensile and compressive strength |
| Floor Acceleration | Internal | The acceleration experienced on each floor of the building during shaking — typically amplified toward the top, which is why upper floors experience more violent motion |
| Evacuation Time | Internal | The time required for all occupants to safely exit the building or reach designated safe zones — affected by building height, stairwell design, occupant density, and structural damage blocking exits |
| Damage Index | Internal | A composite measure of structural damage from 0 (no damage) to 1.0 (total collapse), integrating member failures, connection fractures, permanent deformation, and foundation displacement |

### Research for Lesson
- Seismic Wave Physics — reference materials and textbook resources
- The Resonance Problem — reference materials and textbook resources
- Modern Seismic Engineering Strategies — reference materials and textbook resources
- Design Philosophy: Life Safety vs. Collapse Prevention — reference materials and textbook resources

---

## Step 1: LOCATE — Build Your System

### Text Editor

```
ENGINEERING EARTHQUAKE-PROOF SKYSCRAPERS

Modeling the Physics of Structural Survival Under Seismic Forces.
How can a million-ton building survive forces that level entire cities — and why do some skyscrapers collapse while others barely sway?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Seismic Wave Intensity" — the peak ground acceleration (pga) of the earthquake at the building site
  ○ Click "Foundation Flexibility" — the degree to which the foundation system (base isolators
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Building Mass" — the total weight of the structure including all floors
  ○ Click "Damper Effectiveness" — the percentage of oscillation energy absorbed by tuned mass dampers
  ○ Click "Resonance Frequency" — the relationship between the building's natural oscillation period and the dominant frequency of the seismic waves — when they match
  ○ Click "Material Strength" — the capacity of structural members (steel
  ○ Click "Floor Acceleration" — the acceleration experienced on each floor of the building during shaking — typically amplified toward the top
  ○ Click "Evacuation Time" — the time required for all occupants to safely exit the building or reach designated safe zones — affected by building height
  ○ Click "Damage Index" — a composite measure of structural damage from 0 (no damage) to 1

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
"How can a million-ton building survive forces that level entire cities — and why do some skyscrapers collapse while others barely sway?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Seismic Wave Intensity' — that's external. The peak ground acceleration (PGA) of the earthquake at the building site, measured in g-forces — from 0.
Click on 'Building Mass' — that's internal. The total weight of the structure including all floors.
Click on 'Damper Effectiveness' — that's internal. The percentage of oscillation energy absorbed by tuned mass dampers.
Click on 'Foundation Flexibility' — that's external. The degree to which the foundation system (base isolators.
Click on 'Resonance Frequency' — that's internal. The relationship between the building's natural oscillation period and the dominant frequency of the seismic waves — when they match.
Click on 'Material Strength' — that's internal. The capacity of structural members (steel.
Click on 'Floor Acceleration' — that's internal. The acceleration experienced on each floor of the building during shaking — typically amplified toward the top.
Click on 'Evacuation Time' — that's internal. The time required for all occupants to safely exit the building or reach designated safe zones — affected by building height.
Click on 'Damage Index' — that's internal. A composite measure of structural damage from 0 (no damage) to 1.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Seismic Wave Intensity is external because it represents the earthquake ground motion that the building experiences — it is determined by the earthquake source and site geology, not by the building design. Foundation Flexibility is external because it represents a direct engineering design choice made before the earthquake occurs — the type and quality of base isolation or foundation system installed. The remaining seven components are internal because they are system responses: Building Mass is a design consequence, Damper Effectiveness depends on the damper design interacting with actual earthquake motion, Resonance Frequency emerges from the interaction of building properties with seismic wave properties, and Material Strength, Floor Acceleration, Evacuation Time, and Damage Index are all determined by how the structural system responds to the seismic loading.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next step, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 9 components sorted: Seismic Wave Intensity, Foundation Flexibility (External), Building Mass, Damper Effectiveness, Resonance Frequency, Material Strength, Floor Acceleration, Evacuation Time, Damage Index (Internal)]

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
• Click on "Seismic Wave Intensity" and drag an arrow to "Floor Acceleration"
• Click on "Resonance Frequency" and drag an arrow to "Floor Acceleration"
• Click on "Floor Acceleration" and drag an arrow to "Damage Index"

Task C: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Seismic Wave Intensity → Floor Acceleration = POSITIVE (+)
    Higher seismic wave intensity at the foundation drives greater accelerations throughout the building structure. Floor accelerations are typically amplified toward the top of the building, with upper floors experiencing 2-3 times the ground-level acceleration.

  ○ Resonance Frequency → Floor Acceleration = POSITIVE (+)
    When the dominant frequency of seismic waves approaches the building's natural frequency, floor accelerations are amplified by a factor of 5-10 through resonance. This amplification is the single most destructive phenomenon in earthquake engineering.

  ○ Floor Acceleration → Damage Index = POSITIVE (+)
    Higher floor accelerations generate greater forces on structural members (F=ma), increasing the stress on connections, columns, and beams. When these forces exceed material strength, members fail, connections fracture, and the Damage Index rises toward collapse.

Task D: CHECK YOUR MODEL
• You should have 3 arrows total
• 0 negative relationship(s), 2 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: If Seismic Wave Intensity is high and the earthquake frequency matches the building's natural Resonance Frequency, forces are amplified by 5-10 times. How do engineers design buildings so that resonance NEVER occurs — and what happens when they fail?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Seismic Wave Intensity' and drag an arrow
over to 'Floor Acceleration.'

Here's the key question: When seismic wave intensity goes UP, does
floor acceleration go UP or DOWN?

Higher seismic wave intensity at the foundation drives greater accelerations throughout the building structure. Floor accelerations are typically amplified toward the top of the building, with upper floors experiencing 2-3 times the ground-level acceleration.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Resonance Frequency' and drag an arrow
over to 'Floor Acceleration.'

Here's the key question: When resonance frequency goes UP, does
floor acceleration go UP or DOWN?

When the dominant frequency of seismic waves approaches the building's natural frequency, floor accelerations are amplified by a factor of 5-10 through resonance. This amplification is the single most destructive phenomenon in earthquake engineering.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'Floor Acceleration' and drag an arrow
over to 'Damage Index.'

Here's the key question: When floor acceleration goes UP, does
damage index go UP or DOWN?

Higher floor accelerations generate greater forces on structural members (F=ma), increasing the stress on connections, columns, and beams. When these forces exceed material strength, members fail, connections fracture, and the Damage Index rises toward collapse.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Look at your model now. You've got 0 negative and 2
positive relationships. 3 arrows total.

If Seismic Wave Intensity is high and the earthquake frequency matches the building's natural Resonance Frequency, forces are amplified by 5-10 times. How do engineers design buildings so that resonance NEVER occurs — and what happens when they fail?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Seismic Wave Intensity +→ Floor Acceleration, Resonance Frequency +→ Floor Acceleration, Floor Acceleration +→ Damage Index]

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
• When Seismic Wave Intensity is HIGH, what happens to the internal components?

Task C: SCENARIO — MODERATE EARTHQUAKE, MODERN DESIGN
• 0.3g PGA with advanced damping and base isolation
• PREDICT FIRST: What do you predict the Damage Index will be for a well-engineered building during a moderate earthquake?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task D: SCENARIO — RESONANCE CATASTROPHE
• Seismic frequency matching building natural period
• PREDICT FIRST: What do you predict happens to Floor Acceleration when the earthquake's frequency matches the building's resonance?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task E: SCENARIO — MAXIMUM CREDIBLE EARTHQUAKE
• 1.5g PGA near-fault ground motion
• PREDICT FIRST: What do you predict is the upper limit of earthquake intensity that even the best-designed building can survive?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Resonance is the primary killer in earthquakes — buildings collapse not because the ground motion is too strong but because the building amplifies the motion to destructive levels when frequencies match
• Modern seismic engineering uses a three-layer defense: base isolation decouples from ground motion, flexible design avoids resonance, and dampers absorb energy that gets through
• Building mass is a double-edged sword: heavier buildings have lower natural frequencies (avoiding resonance with typical seismic waves) but experience greater inertial forces at any given acceleration
• No building can be made truly earthquake-proof — engineers design for graceful failure, where the structure absorbs damage in planned locations while protecting life safety and evacuation routes

THE ANSWER: Earthquake-proof skyscrapers survive through three engineering strategies working together. First, base isolation decouples the building from ground motion — the earth moves but the building stays relatively still. Second, flexible structural design ensures the building's natural frequency does not match typical seismic wave frequencies, preventing catastrophic resonance amplification. Third, tuned mass dampers and energy-dissipating connections absorb the energy that does reach the structure. The critical insight is that resonance — not raw force — is the primary destroyer. A moderate earthquake at the building's resonance frequency is more dangerous than a powerful earthquake at a non-resonant frequency.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Moderate Earthquake, Modern Design. 0.3g PGA with advanced damping and base isolation.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Resonance Catastrophe.
Seismic frequency matching building natural period.

Before you run it — make a prediction. What do you predict happens to Floor Acceleration when the earthquake's frequency matches the building's resonance?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Maximum Credible Earthquake. 1.5g PGA near-fault ground motion.
What do you predict is the upper limit of earthquake intensity that even the best-designed building can survive?

Here's what our model reveals: Earthquake-proof skyscrapers survive through three engineering strategies working together. First, base isolation decouples the building from ground motion — the earth moves but the building stays relatively still. Second, flexible structural design ensures the building's natural frequency does not match typical seismic wave frequencies, preventing catastrophic resonance amplification. Third, tuned mass dampers and energy-dissipating connections absorb the energy that does reach the structure. The critical insight is that resonance — not raw force — is the primary destroyer. A moderate earthquake at the building's resonance frequency is more dangerous than a powerful earthquake at a non-resonant frequency.

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
   • What happens if you turn OFF Seismic Wave Intensity?
   • What happens if you turn OFF Foundation Flexibility?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Soil Amplification Factor — The degree to which local soil conditions amplify or dampen seismic waves before they reach the foundation — soft clay can amplify ground motion by 2-5 times compared to bedrock
   • Aftershock Vulnerability — The increased susceptibility to damage during aftershocks when the primary earthquake has already weakened structural connections and reduced the building's remaining capacity
   • Non-Structural Damage — Damage to interior elements — ceilings, partitions, mechanical systems, elevators — that can injure occupants and block evacuation even when the structural frame remains intact

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • Seismic Wave Physics — how does this connect to your model?
   • The Resonance Problem — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model demonstrate that resonance, not raw force, is the primary cause of catastrophic building failure in earthquakes?
   • Why is the three-layer defense (isolation, flexibility, damping) more effective than making the building as strong as possible?
   • What trade-offs does your model reveal between building mass, height, and seismic vulnerability?
   • How would your model change if the building were on soft clay versus bedrock?

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

Soil Amplification Factor. The degree to which local soil conditions amplify or dampen seismic waves before they reach the foundation — soft clay can amplify ground motion by 2-5 times compared to bedrock
How would you model that?

Aftershock Vulnerability. The increased susceptibility to damage during aftershocks when the primary earthquake has already weakened structural connections and reduced the building's remaining capacity
How would you model that?

Non-Structural Damage. Damage to interior elements — ceilings, partitions, mechanical systems, elevators — that can injure occupants and block evacuation even when the structural frame remains intact
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

Structural Engineers specializing in seismic design develop earthquake-resistant buildings, bridges, and infrastructure. They use computational modeling to simulate seismic response and work at engineering firms, government agencies, and research institutions, earning $80,000-$160,000/year. Seismologists who study earthquake physics earn $70,000-$130,000/year.

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
Visual: Title slide with earthquake-damaged building next to intact modern skyscraper
Say: "In 1985, a magnitude 8.0 earthquake hit Mexico City. Buildings of 8-15 stories collapsed everywhere while shorter and taller buildings survived. Why those specific buildings? The answer changed earthquake engineering forever."
Do: Show before/after images of the 1985 Mexico City earthquake. The pattern of destruction by building height hooks students into the resonance concept.
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and vocabulary terms
Say: "Today you are engineering buildings that survive the most destructive force on Earth. And the secret is not making them stronger — it is making them smarter."
Do: Have students read objectives. Pre-teach 'resonance' using a playground swing analogy: pushing at the natural frequency makes the swing go higher and higher.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: How can a million-ton building survive forces that level cities?
Say: "A skyscraper weighs hundreds of thousands of tons. During an earthquake, F equals ma — all that mass times the ground acceleration equals enormous force. So how does it not fall down?"
Do: Quick-write: Students list strategies they think engineers use. Share out. Most will guess 'make it stronger' — set up the surprise that flexibility beats strength.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps overview with seismic engineering context
Say: "We are building a model of a building's fight against an earthquake — nine variables that determine whether 1,000 people on the upper floors live or die."
Do: Preview LEVER steps. Emphasize that this model reveals a counterintuitive truth about what makes buildings survive.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Nine component cards for earthquake engineering model
Say: "Nine variables. Two you set as conditions — earthquake intensity and foundation type. Seven that the physics determines. Which combinations lead to survival?"
Do: Guide students through all nine components. Spend extra time on resonance frequency — this is the key concept that unlocks the model.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows between nine components
Say: "Here is the deadly math: Force equals mass times acceleration. Resonance multiplies acceleration by 5 to 10 times. That means forces that should be survivable become catastrophic."
Do: Help students map the resonance amplification pathway. Use the swing analogy: small pushes at the right frequency create enormous motion.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Simulation graphs for three scenarios
Say: "Let us find out what kills a building. Spoiler: it is not the biggest earthquake — it is the earthquake at exactly the wrong frequency."
Do: Students predict Damage Index for each scenario. The resonance catastrophe scenario should surprise them — moderate earthquake, massive damage. Discuss why.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key findings from model exploration
Say: "Now you know the secret: earthquake engineering is not about being the strongest — it is about being the smartest. Avoid resonance, absorb energy, decouple from the ground."
Do: Connect model findings to the Mexico City 1985 case: medium-rise buildings collapsed because their natural period matched the earthquake's dominant frequency. Taller and shorter buildings survived.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: 60-story tower seismic protection design challenge
Say: "Your city just approved a 60-story tower 8 km from an active fault. Design the seismic system that keeps everyone alive during a magnitude 7.5 earthquake."
Do: Groups design comprehensive seismic protection systems. Test concepts against model scenarios. Present with engineering justification from simulation data.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: Engineering Earthquake-Proof Skyscrapers
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
Earthquakes generate forces that can accelerate the ground at the same rate as gravity — imagine the floor suddenly tilting 90 degrees. Buildings, which are designed to resist vertical gravity loads, must also survive violent horizontal shaking. The engineering of earthquake-resistant structures is a battle against F=ma: the more mass a building has, the greater the forces it must withstand during acceleration.

NGSS ALIGNMENT:
HS-ESS2-2, HS-PS2-1: Analyze geoscience data to make the claim that one change to Earth's surface can create feedbacks that cause changes to other Earth systems. Analyze data to support the claim that Newton's second law of motion describes the mathematical relationship among the net force on a macroscopic object, its mass, and its acceleration.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Analyzing and Interpreting Data
  Students analyze seismic wave data and structural response data to identify relationships between ground motion characteristics, building properties, and damage outcomes.
• Disciplinary Core Idea: ESS2.B Plate Tectonics and Large-Scale System Interactions / PS2.A Forces and Motion
  Students apply Newton's second law (F=ma) to understand how seismic accelerations generate forces proportional to building mass, and how plate tectonics generates the seismic waves.
• Crosscutting Concept: Structure and Function
  Students analyze how the structural design of a building (its shape, materials, connections, dampers) determines its function (survival or collapse) during seismic loading.

PACING GUIDE:
• Step 1 (Locate): 8-10 minutes
• Step 2 (Establish): 8-10 minutes
• Step 3 (Visualize & Evaluate): 10-12 minutes
• Step 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Seismic Waves, Resonance, Tuned Mass Damper, Base Isolation
□ Prepare How can a million-ton building survive forces that level entire cities — and why do some skyscrapers collapse while others barely sway discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify nine key components of the seismic building system: seismic wave intensity, building mass, damper effectiveness, foundation flexibility, resonance frequency, material strength, floor acceleration, evacuation time, and damage index.
• Establish: Students map relationships showing that seismic wave intensity and resonance frequency interact to determine floor acceleration, which combines with building mass to generate forces that material strength must resist, while dampers and base isolation reduce the energy reaching the structure.
• Visualize: Students build a computational model showing the nine-component system with resonance amplification as the critical interaction.
• Evaluate: Students run moderate earthquake, resonance catastrophe, and maximum credible earthquake scenarios to test their model and identify the conditions under which each seismic protection strategy becomes critical.
• Revise: Students add soil amplification factor, aftershock vulnerability, or non-structural damage to model more realistic seismic response scenarios.

BACKGROUND CONTENT:
• Seismic Wave Physics:
  Earthquakes generate three types of waves: P-waves (compression, fastest, arrive first), S-waves (shear, side-to-side, more damaging), and surface waves (rolling motion, slowest, most destructive). Each wave type has characteristic frequencies. Most building damage comes from surface waves and S-waves with periods of 0.5-5 seconds — which unfortunately overlaps with the natural periods of most buildings from 3 to 60 stories.

• The Resonance Problem:
  Every structure has a natural frequency at which it wants to oscillate — like a tuning fork. For tall buildings, this period is roughly 0.1 seconds per story (a 30-story building has a natural period of about 3 seconds). When earthquake waves arrive at frequencies matching the building's natural period, the structure enters resonance: each cycle of ground motion adds energy to the building's oscillation, amplifying forces by 5-10 times. This is why medium-rise buildings (5-15 stories) are particularly vulnerable — their natural periods match the dominant frequencies of most earthquakes.

• Modern Seismic Engineering Strategies:
  Three primary strategies protect buildings: (1) Base isolation uses flexible bearings between the foundation and structure, allowing the ground to move while the building stays relatively stationary — reducing forces by 50-80%. (2) Structural flexibility through moment-resisting frames and shear walls allows the building to flex without breaking, with a natural period designed to avoid resonance with expected earthquake frequencies. (3) Energy dissipation through tuned mass dampers, viscous fluid dampers, and friction connections absorbs kinetic energy and converts it to heat, reducing peak accelerations on upper floors by 30-50%.

• Design Philosophy: Life Safety vs. Collapse Prevention:
  Earthquake engineering does not aim for zero damage — that would be prohibitively expensive. Instead, buildings are designed to three performance levels: Immediate Occupancy (minimal damage, building fully usable — for hospitals and fire stations), Life Safety (significant structural damage but no collapse — occupants can evacuate safely — the standard for most buildings), and Collapse Prevention (severe damage, building may be demolished afterward, but it does not kill occupants — the minimum standard). This philosophy accepts that buildings are sacrificial structures that protect human life through controlled damage.

COMMON MISCONCEPTIONS:
• "Stronger buildings are safer in earthquakes"
  Reality: This is one of the most dangerous misconceptions in earthquake engineering. A perfectly rigid, extremely strong building transmits 100% of ground acceleration to every floor. If that acceleration hits the building's resonance frequency, forces amplify to destructive levels regardless of material strength. Flexible buildings that deform elastically absorb and dissipate seismic energy, reducing peak forces. Base-isolated buildings decouple entirely. The lesson: flexibility and energy absorption protect buildings more than raw strength.
  Strategy: Demonstration: Hold a stiff ruler and a flexible ruler vertically. Shake the base. The stiff ruler transmits every vibration to the top. The flexible ruler absorbs and dampens the motion. Which would you rather be standing on top of?

• "Earthquakes destroy buildings by shaking them apart"
  Reality: Earthquakes primarily destroy buildings through resonance amplification and connection failure, not through raw shaking intensity. Most structural collapses occur because the building's natural frequency matched the earthquake's dominant frequency, amplifying motion to 5-10 times the ground movement. Failure typically begins at connections — where beams meet columns — not in the members themselves. A well-connected, flexible building can survive extreme shaking; a poorly connected, rigid building can collapse in a moderate earthquake.
  Strategy: Case study: In the 1985 Mexico City earthquake, the soft lake-bed soil amplified seismic waves with a 2-second period. Buildings with natural periods near 2 seconds (roughly 6-15 stories) were selectively destroyed. Shorter and taller buildings survived because they were off-resonance.

• "If a building survives one earthquake, it will survive the next one"
  Reality: Every earthquake causes some degree of damage, even if invisible. Micro-cracks in concrete, loosened bolts, fatigued steel connections, and permanent deformation all reduce the building's remaining capacity. A building that barely survived a moderate earthquake may collapse in an aftershock that is weaker than the initial quake. This is why post-earthquake inspections are critical — a building may look fine from outside while its structural reserves have been depleted. The model shows how Damage Index does not reset between seismic events.
  Strategy: Analogy: If you bend a paperclip back and forth, it does not break the first time. But each bend weakens the metal at the fold. Eventually, a very gentle bend snaps it. Buildings accumulate fatigue the same way — the next earthquake does not start from zero damage.

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
Big Question: How can a million-ton building survive forces that level entire cities — and why do some skyscrapers collapse while others barely sway?
Answer: Earthquake-proof skyscrapers survive through three engineering strategies working together. First, base isolation decouples the building from ground motion — the earth moves but the building stays relatively still. Second, flexible structural design ensures the building's natural frequency does not match typical seismic wave frequencies, preventing catastrophic resonance amplification. Third, tuned mass dampers and energy-dissipating connections absorb the energy that does reach the structure. The critical insight is that resonance — not raw force — is the primary destroyer. A moderate earthquake at the building's resonance frequency is more dangerous than a powerful earthquake at a non-resonant frequency.

Simulation Answers:
• Moderate Earthquake, Modern Design Scenario: With 0.3g peak ground acceleration, effective base isolation reduces the motion transmitted to the building by 60-80%. The remaining motion is further reduced by tuned mass dampers absorbing 30-40% of oscillation energy. Floor Acceleration remains well within material capacity, Resonance is avoided through the base isolation's period-shifting effect, and Damage Index stays near zero. Modern seismic engineering transforms a potentially damaging earthquake into a noticeable but harmless experience for occupants.
• Resonance Catastrophe Scenario: When seismic wave frequency matches the building's natural period, the model shows devastating amplification. Even moderate ground motion (0.3g) produces Floor Accelerations of 1.5-3.0g through resonance. These amplified forces exceed Material Strength in structural members, causing progressive connection failures. Damage Index rapidly approaches 1.0 (total collapse) as each floor's failure redistributes load to remaining members in a cascading collapse. This scenario explains why the 1985 Mexico City earthquake selectively destroyed medium-rise buildings — their natural periods matched the 2-second dominant period of the lake-bed-amplified seismic waves.

Reflection Exemplars:
• Q: Why is resonance more dangerous than raw force?
  A: A very strong earthquake at a frequency that does not match the building's natural period pushes the building back and forth, but each push is partially absorbed before the next arrives. The building flexes but each cycle starts from near-zero. In resonance, each seismic cycle arrives at exactly the moment the building is swinging back the other way, adding energy to the existing motion. After just 5-10 cycles, the building is swinging 5-10 times farther than the ground movement alone would cause. It is the same principle as pushing a swing — tiny pushes at the right frequency create enormous amplitude. The model shows that a 0.3g earthquake at resonance can be more destructive than a 1.0g earthquake off-resonance.
• Q: Why does flexibility beat strength?
  A: A rigid building directly transmits ground acceleration to all floors — whatever the ground does, the building does. A flexible building decouples from the ground: while the foundation moves, the upper floors take time to catch up, spreading the energy over a longer period and reducing peak forces. This is counterintuitive: most students assume a stronger building is safer. But in earthquake engineering, a stiff, strong building that enters resonance will be destroyed, while a flexible, weaker building that avoids resonance will survive. The model demonstrates this clearly: increasing Material Strength while maintaining the same resonance risk barely reduces Damage Index, while adding base isolation (flexibility) dramatically reduces it.

STEM CHALLENGE GUIDANCE:
Title: Design a Seismic Protection System for a 60-Story Tower
Mission: Design a comprehensive seismic protection system for a 60-story tower in a Zone 4 earthquake region that minimizes Damage Index while maintaining acceptable construction costs and Evacuation Time.
Scenario: A major city in an active seismic zone has approved construction of a new 60-story mixed-use tower. The site is 8 km from an active fault capable of producing M7.5 earthquakes. Your team must design the building's seismic protection system — including foundation type, structural system, damping technology, and evacuation plan — to achieve a Damage Index below 0.2 for the maximum credible earthquake.
Introduction: Present the challenge: A major seismic-zone city has approved a 60-story tower 8 km from an active fault capable of M7.5 earthquakes. Your engineering team must design the complete seismic protection system — foundation, structure, damping, and evacuation — to achieve a Damage Index below 0.2 for the maximum credible earthquake.

Key Concepts:
• Base Isolation Systems: Lead-rubber bearings, friction pendulum bearings, and triple pendulum bearings each offer different displacement capacities and period-shifting characteristics. The choice depends on building mass, height, and local seismic conditions. Base isolation can reduce forces by 50-80% but requires expensive foundation work and a seismic gap around the building.
• Tuned Mass Damper Design: The damper mass must be calibrated to the building's natural frequency (typically 1-5% of building mass). Taipei 101's famous 730-ton steel pendulum reduced peak accelerations by 40% during Typhoon Soudelor. Placement, tuning, and backup dampers for multiple vibration modes are critical design decisions.
• Performance-Based Seismic Design: Modern codes allow engineers to design for specific performance objectives at different earthquake levels: Frequent earthquakes (50-year return) should cause no damage, Design-level earthquakes (475-year return) should allow life safety, and Maximum earthquakes (2,475-year return) should prevent collapse. This tiered approach optimizes cost versus safety.

Evaluation Rubric:
• Expert (4): Design includes integrated base isolation, structural system, and damping technology with quantitative performance targets, specifies evacuation strategy, calculates cost-benefit, and demonstrates Damage Index below 0.2 using model evidence for the maximum credible earthquake
• Proficient (3): Design includes multiple seismic protection layers with model-based justification and addresses evacuation planning
• Developing (2): Design proposes seismic protection strategies but lacks integration between systems or quantitative performance analysis
• Beginning (1): Design addresses only one protection strategy or does not demonstrate understanding of resonance avoidance and energy absorption

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a frequency spectrum chart showing typical earthquake dominant periods and typical building natural periods by height, highlighting the dangerous overlap zone
  • Use a visual comparison of rigid, flexible, and base-isolated building responses to the same earthquake to illustrate the advantage of each strategy
  • Sentence frames: 'Our seismic system uses __ for foundation isolation, __ for structural flexibility, and __ for energy absorption, which reduces Floor Acceleration from __ to __ and keeps Damage Index below __'

Extensions (Advanced Learners):
  • Research the seismic design of Taipei 101 (730-ton tuned mass damper), the Transamerica Pyramid (tapered design), and Tokyo Skytree (central shaft damper) — compare their approaches using the nine model parameters
  • Investigate liquefaction — how water-saturated soil behaves like liquid during earthquakes — and model how this additional variable would affect your building's seismic response
  • Design a shake table experiment to test scale models of rigid versus flexible versus base-isolated structures and compare results to your computational model predictions

Cross-Curricular Connections:
  • Math: Apply Newton's second law: if a 60-story building has a mass of 200,000 metric tons and experiences a floor acceleration of 0.5g at resonance, calculate the lateral force on the structure in meganewtons. Then calculate how much a base isolation system reducing acceleration by 70% saves in required structural capacity.
  • ELA: Research the ethical dimensions of earthquake engineering codes: write an argumentative essay on whether building codes should require the highest seismic protection (expensive but safer) or allow risk-based design (cheaper but accepting some probability of collapse)
  • Social Studies: Investigate why earthquake deaths are dramatically higher in developing nations — compare the 2010 Haiti earthquake (316,000 deaths, M7.0) with the 2011 Japan earthquake (18,000 deaths, M9.0) and analyze the role of engineering codes, economic resources, and building practices

CAST ALIGNMENT:
• Model how nine seismic and structural variables interact to determine building survival during earthquakes
• Analyze why resonance frequency matching between seismic waves and building natural period causes catastrophic amplification
• Design multi-layered seismic protection systems using computational model evidence

CAST-Style Assessment Questions:
• Multiple Choice: Two buildings of equal height experience the same earthquake. Building A has a natural period of 3.0 seconds and the earthquake's dominant period is 3.1 seconds. Building B has a natural period of 1.2 seconds. According to your model, which building is in greater danger and why?
• Constructed Response: Using your model, explain why making a building stronger (higher Material Strength) is not sufficient to make it earthquake-resistant. Address the roles of resonance, flexibility, and energy absorption in your explanation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: Engineering Earthquake-Proof Skyscrapers
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Why do some buildings collapse in earthquakes while others nearby survive with little damage?

   _________________________________________________________

   _________________________________________________________

2. What do you think is the difference between a rigid building and a flexible building during an earthquake?

   _________________________________________________________

   _________________________________________________________

3. Draw what you think happens to a tall building when seismic waves hit its foundation.

   [DRAWING BOX]

4. Have you heard of tuned mass dampers or base isolation? What do you think they do?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Seismic Waves                 
___ Resonance                     
___ Tuned Mass Damper             
___ Base Isolation                

A. Energy waves propagating through the Earth from an earthquake's focus — P-waves compress and expand rock, S-waves shear it side to side, and surface waves roll the ground — each type affects buildings differently based on their frequency and amplitude
B. The phenomenon where a structure's natural oscillation frequency matches the frequency of incoming seismic waves, causing amplification of motion that can multiply forces by 5-10 times — the primary cause of catastrophic building failure in earthquakes
C. A heavy mass mounted near the top of a building on springs or pendulums that swings opposite to the building's motion during earthquakes or wind, canceling out oscillation energy and reducing sway by 30-50%
D. A seismic protection system where the building sits on flexible bearings (rubber-steel laminates or friction pendulums) that decouple the structure from ground motion, allowing the earth to move beneath the building while the building remains relatively stationary

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

SCENARIO: Moderate Earthquake, Modern Design
Settings: 0.3g PGA with advanced damping and base isolation
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Resonance Catastrophe
Settings: Seismic frequency matching building natural period
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Maximum Credible Earthquake
Settings: 1.5g PGA near-fault ground motion
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

1. How does your model demonstrate that resonance, not raw force, is the primary cause of catastrophic building failure in earthquakes?

   _________________________________________________________

   _________________________________________________________

2. Why is the three-layer defense (isolation, flexibility, damping) more effective than making the building as strong as possible?

   _________________________________________________________

   _________________________________________________________

3. What trade-offs does your model reveal between building mass, height, and seismic vulnerability?

   _________________________________________________________

   _________________________________________________________

4. How would your model change if the building were on soft clay versus bedrock?

   _________________________________________________________

   _________________________________________________________

5. What does 'earthquake-proof versus earthquake-resistant' mean in terms of your Damage Index results?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. How can a million-ton building survive forces that level entire cities — and why do some skyscrapers collapse while others barely sway? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Analyzing and Interpreting Data
   □ Disciplinary Core Idea: ESS2.B Plate Tectonics and Large-Scale System Interactions / PS2.A Forces and Motion
   □ Crosscutting Concept: Structure and Function

3. What does 'earthquake-proof versus earthquake-resistant' mean in terms of your Damage Index results?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Seismic Protection System for a 60-Story Tower
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design a comprehensive seismic protection system for a 60-story tower in a Zone 4 earthquake region that minimizes Damage Index while maintaining acceptable construction costs and Evacuation Time.

SCENARIO: A major city in an active seismic zone has approved construction of a new 60-story mixed-use tower. The site is 8 km from an active fault capable of producing M7.5 earthquakes. Your team must design the building's seismic protection system — including foundation type, structural system, damping technology, and evacuation plan — to achieve a Damage Index below 0.2 for the maximum credible earthquake.

GUIDING QUESTIONS:
• What foundation system will you use to decouple the building from ground motion?
• How will you ensure the building's natural frequency avoids resonance with expected seismic waves?
• What damping technology will you deploy and how much oscillation energy will it absorb?

DESIGN THINKING:
• What structural material and configuration will you use and what is its strength-to-weight ratio?

  _________________________________________________________

• Where will you place dampers in the building and what type provides the best multi-mode energy absorption?

  _________________________________________________________

• How will you design evacuation routes that remain functional even when the building sustains damage?

  _________________________________________________________

• What is the estimated additional cost of your seismic system as a percentage of total construction cost?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Design includes integrated base isolation, structural system, and damping technology with quantitative performance targets, specifies evacuation strategy, calculates cost-benefit, and demonstrates Damage Index below 0.2 using model evidence for the maximum credible earthquake
• Proficient (3): Design includes multiple seismic protection layers with model-based justification and addresses evacuation planning
• Developing (2): Design proposes seismic protection strategies but lacks integration between systems or quantitative performance analysis
• Beginning (1): Design addresses only one protection strategy or does not demonstrate understanding of resonance avoidance and energy absorption

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CAST-Aligned Pre/Post Assessment

### Administration Instructions

These 5 multiple-choice questions are administered identically as both a pre-assessment (before Activity 1) and a post-assessment (after Activity 4). Score each out of 5. Learning growth = post-score minus pre-score.

Questions follow the California Science Test (CAST) stimulus-response format. Each item is three-dimensional, assessing a Science and Engineering Practice (SEP), Disciplinary Core Idea (DCI), and Crosscutting Concept (CCC) simultaneously, aligned to HS-ESS2-2, HS-PS2-1.

---

### Pre-Assessment Questions

### Question 1

Two identical buildings experience the same earthquake. Building A is rigidly connected to its foundation. Building B sits on flexible rubber-steel bearings (base isolation). Which building experiences greater floor acceleration, and why?

A. Building B, because the flexible bearings amplify ground motion like a trampoline
B. Building A, because the rigid connection transmits 100% of ground acceleration directly to the structure, while base isolation decouples the building from ground motion
C. Both experience identical acceleration because they have the same mass
D. Neither experiences significant acceleration because modern buildings are earthquake-proof

Correct Answer: B

Feedback: Correct. Base isolation works by decoupling the building from ground motion. The flexible bearings absorb and spread seismic energy over a longer period, reducing the peak acceleration transmitted to the structure by 50-80%. The rigid building transmits every ground acceleration directly. Consider what happens when you shake a table with a cup glued to it versus a cup sitting on a rubber pad. Which cup experiences more force from the shaking?

---

### Question 2

In the 1985 Mexico City earthquake, buildings of 8-15 stories collapsed while shorter and taller buildings survived. What physical phenomenon best explains this selective destruction?

A. Buildings of 8-15 stories were built with weaker materials
B. The earthquake's dominant wave frequency matched the natural oscillation period of 8-15 story buildings, causing resonance amplification that multiplied forces by 5-10 times
C. Only 8-15 story buildings were occupied at the time of the earthquake
D. Taller buildings have deeper foundations that protected them from ground motion

Correct Answer: B

Feedback: Correct. Resonance occurs when external forcing frequency matches a structure's natural frequency. Medium-rise buildings (8-15 stories) have natural periods of approximately 1-2 seconds, which matched the 2-second dominant period of the Mexico City earthquake. This amplified ground motion 5-10 times, causing selective destruction. Consider why ONLY buildings of a certain height range were destroyed. What physical property changes with building height, and how could matching with earthquake characteristics cause amplified damage?

---

### Question 3

A tuned mass damper is a heavy pendulum mounted near the top of a skyscraper. During an earthquake, the damper swings opposite to the building's motion. What physical principle explains how this reduces damage?

A. The damper's weight prevents the building from moving at all
B. The damper absorbs kinetic energy from the building's oscillation and converts it to heat through friction, reducing the amplitude of building motion by 30-50%
C. The damper pushes the building back to vertical using stored gravitational energy
D. The damper is primarily decorative and has minimal structural benefit

Correct Answer: B

Feedback: Correct. The tuned mass damper acts as an energy sink. When the building sways right, the damper swings left, absorbing kinetic energy through friction and viscous resistance. This energy is converted to heat rather than continuing to build up in the structure. Taipei 101's 730-ton damper reduces sway by approximately 40%. Think about energy conservation: the earthquake pumps kinetic energy into the building. Where does that energy go? The damper provides a mechanism to remove energy from the building's oscillation.

---

### Question 4

Newton's second law states F = ma. During an earthquake, a 200,000-ton skyscraper experiences a floor acceleration of 0.5g. What is the approximate lateral force on the structure?

A. 100,000 newtons
B. 1 million newtons (1 MN)
C. Approximately 980 million newtons (980 MN) — almost 1 billion newtons
D. The force cannot be calculated without knowing the building height

Correct Answer: C

Feedback: Correct. F = ma = 200,000,000 kg x 0.5 x 9.8 m/s^2 = 980,000,000 N = 980 MN. This enormous force — nearly 1 billion newtons — demonstrates why seismic engineering focuses on reducing acceleration (through base isolation and damping) rather than just strengthening structures. Apply F = ma directly. Convert 200,000 metric tons to kilograms (multiply by 1,000,000). Multiply by 0.5g (where g = 9.8 m/s^2).

---

### Question 5

Modern earthquake engineering designs buildings for 'life safety' rather than 'zero damage.' What engineering principle justifies this approach?

A. Engineers do not know how to build damage-free structures
B. Designing for zero damage in the maximum credible earthquake would be prohibitively expensive, so buildings are designed to sustain controlled structural damage that protects occupants while potentially sacrificing the building itself
C. All earthquake damage can be repaired after the event, so prevention is unnecessary
D. Life safety and zero damage require the same engineering approach

Correct Answer: B

Feedback: Correct. This is performance-based design: the building absorbs seismic energy through planned damage in designated structural members (like sacrificial fuses) while maintaining enough integrity for safe evacuation. The building may be demolished afterward, but no one dies. This philosophy optimizes cost versus safety. Consider the cost-benefit analysis. Designing for the absolute worst-case earthquake with zero damage would require enormous structural capacity. Is it more practical to accept some damage while ensuring the building does not collapse?

---

### Post-Assessment Questions

### Question 1

The model shows Building A (natural period 3.0 seconds) in an earthquake with a dominant period of 3.1 seconds. Building B (natural period 1.2 seconds) is in the same earthquake. The model predicts Building A's Damage Index is 5 times higher. What variable drives this difference?

A. Building A is taller and therefore always more vulnerable
B. Resonance Frequency — Building A's natural period nearly matches the earthquake's dominant period, causing resonance amplification of forces, while Building B is far from resonance
C. Building B has stronger materials based on its shorter natural period
D. The earthquake hits Building B with less intensity because it is shorter

Correct Answer: B

Feedback: Correct. The model demonstrates that resonance is the primary determinant of damage, not building height or material strength. Building A's 3.0-second period nearly matches the earthquake's 3.1-second period, causing amplification. Building B's 1.2-second period is far from resonance, so it experiences the earthquake at its actual intensity. Look at the relationship between each building's natural period and the earthquake's dominant period. When do forces amplify? When the frequencies are close to matching, or when they are far apart?

---

### Question 2

In the model, a student increases Material Strength by 50% while keeping all other variables the same, including resonance risk. The Damage Index decreases by only 10%. What does this disproportionate response reveal?

A. Material Strength is incorrectly modeled and should have more impact
B. The model is broken because stronger materials should always dramatically reduce damage
C. When resonance amplifies forces by 5-10 times, a 50% increase in material strength is overwhelmed — addressing resonance avoidance (through flexibility or isolation) is more effective than adding strength
D. Material Strength has no relationship to Damage Index in the model

Correct Answer: C

Feedback: Correct. This is a key model insight: strength alone cannot overcome resonance amplification. If an earthquake at resonance multiplies forces by 5-10x, a 50% stronger structure still fails under those amplified forces. The model shows that avoiding resonance (through base isolation or period-shifting) reduces damage far more effectively than adding strength. Consider the magnitude of resonance amplification (5-10x) versus the material improvement (1.5x). If forces are multiplied by 7 through resonance, does making the structure 1.5 times stronger prevent failure?

---

### Question 3

The model classifies Seismic Wave Intensity and Foundation Flexibility as external variables. A student argues that Building Mass should also be external because it is set during design. What is the best evaluation of this argument?

A. The argument is correct — Building Mass is a design choice and should be external
B. While Building Mass is determined during design, in the model's context it is treated as a system property that interacts with seismic forces through F=ma — it is a characteristic of the system being analyzed, not a condition imposed on it
C. Building Mass cannot be classified as either external or internal
D. The classification makes no difference to model behavior

Correct Answer: B

Feedback: Correct. The distinction is nuanced: external variables represent conditions that the system encounters (earthquake intensity, foundation engineering choice). Building Mass, while determined during design, is a property of the system itself — it interacts with acceleration to produce force (F=ma) and with natural period to determine resonance risk. The model treats it as a system characteristic. Consider the difference between conditions the building encounters (earthquake characteristics, foundation type) and properties of the building itself. The model analyzes how the building system responds to seismic conditions.

---

### Question 4

The model's moderate earthquake scenario (0.3g) with base isolation shows a Damage Index near zero, while the same earthquake at resonance (without isolation) shows a Damage Index near 0.8. Both scenarios have identical earthquake intensity. What does this comparison demonstrate about seismic design?

A. Base isolation makes buildings completely indestructible
B. The comparison demonstrates that resonance avoidance and energy decoupling are more important than earthquake intensity alone — the same earthquake can be harmless or catastrophic depending on the structural design
C. The 0.3g earthquake is too weak to damage any building, so the comparison is meaningless
D. Damage Index is not a reliable metric for comparing seismic scenarios

Correct Answer: B

Feedback: Correct. This is the model's most powerful finding: the same earthquake produces radically different outcomes based solely on structural design. Base isolation prevents resonance and decouples the building from ground motion. Without it, resonance amplifies the same moderate earthquake to destructive levels. Design, not earthquake size, determines survival. Compare the two scenarios: same earthquake intensity, same building, but dramatically different outcomes. What is the only difference between them? What does that tell you about what determines building survival?

---

### Question 5

After running all three scenarios, a student concludes that base isolation alone is sufficient seismic protection for any building. Using model evidence, what is the strongest limitation of this conclusion?

A. Base isolation is too expensive to be practical
B. The maximum credible earthquake scenario (1.5g near-fault) shows that even base-isolated buildings experience significant forces — a multi-layered defense (isolation + dampers + flexible design) is needed for extreme events because no single strategy handles all scenarios
C. Base isolation only works for buildings under 10 stories
D. The model does not include a base isolation variable

Correct Answer: B

Feedback: Correct. The model's three scenarios reveal that base isolation handles moderate earthquakes excellently but has limits under extreme near-fault ground motion. The maximum credible earthquake scenario demonstrates that combined strategies — isolation, structural flexibility, and energy-dissipating dampers — are needed for comprehensive protection. Look at the maximum credible earthquake scenario results. Does base isolation alone reduce the Damage Index to near zero in that extreme case, or does the building still experience significant forces?

---

### Answer Key

**Pre-Assessment:**
Question 1: B
Question 2: B
Question 3: B
Question 4: C
Question 5: B

**Post-Assessment:**
Question 1: B
Question 2: C
Question 3: B
Question 4: B
Question 5: B

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-10/G10L3-L05/G10L3-L05-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-10/G10L3-L05/G10L3-L05-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-10/G10L3-L05/G10L3-L05-Student-Presentation.pptx] |
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