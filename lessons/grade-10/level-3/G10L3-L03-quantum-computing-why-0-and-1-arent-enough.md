# Lesson: Quantum Computing: Why 0 and 1 Aren't Enough

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G10L3-L03 |
| **Grade** | 10th Grade — Level 3: Advanced Engineering & Design |
| **Lesson Name** | Quantum Computing: Why 0 and 1 Aren't Enough |
| **Status** | Template |

---

## Platform

### Title
**Quantum Computing: Why 0 and 1 Aren't Enough — Modeling the Physics and Engineering of Computation Beyond Classical Limits**

### Overview
Classical computers have transformed civilization using a simple language: 0 and 1. Every photo, video, app, and AI model is built from billions of binary switches. But some problems are so complex that even a computer with every atom in the universe as a transistor could not solve them before the heat death of the cosmos. Quantum computing offers a fundamentally different approach — but building it requires engineering at the edge of physical possibility. Students investigate the driving question: Why would a computer that uses the weirdest rules in physics be millions of times faster than the most powerful supercomputer ever built? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of a quantum computing dilution refrigerator with its golden chandelier of wires and stages visible, blue-tinted lighting creating a futuristic atmosphere, the intricate engineering of quantum hardware visible at multiple scales]

### Grade
10th Grade — Level 3: Advanced Engineering & Design

### NGSS Standard
**HS-PS4-3, HS-PS2-5**: Evaluate the claims, evidence, and reasoning behind the idea that electromagnetic radiation can be described either by a wave model or a particle model. Plan and conduct an investigation to provide evidence that an electric current can produce a magnetic field and that a changing magnetic field can produce an electric current.

### Learning Objectives
- Model how nine interdependent parameters determine whether a quantum computer outperforms classical systems
- Analyze the engineering trade-offs between qubit coherence, error correction, and computational speed
- Evaluate why maintaining quantum states is fundamentally at odds with the environment qubits exist in
- Predict the conditions under which quantum advantage becomes achievable for real-world problems

### Component List (Starting Model: 9 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Qubit Coherence Time | Internal | The duration a qubit maintains its quantum state before decoherence destroys the superposition — currently measured in microseconds to milliseconds for superconducting qubits |
| Entanglement Fidelity | Internal | The accuracy with which two qubits can be entangled and maintain their correlation — measured as a percentage where 99.9%+ is needed for useful computation |
| Error Rate | Internal | The probability that a quantum gate operation produces an incorrect result — currently around 0.1-1% per gate, which compounds exponentially across circuits |
| Gate Operation Speed | Internal | The time required to perform a single quantum logic operation on one or two qubits — faster gates allow more operations within the coherence window |
| Cooling Temperature | External | The operating temperature of the quantum processor, which must approach absolute zero (15 millikelvin for superconducting qubits) to minimize thermal noise that causes decoherence |
| Quantum Volume | Internal | A holistic metric combining qubit count, connectivity, gate fidelity, and coherence time to measure the overall computational capability of a quantum system |
| Decoherence Rate | Internal | The speed at which environmental interference destroys quantum states — determined by temperature, electromagnetic shielding, vibration isolation, and material quality |
| Classical Overhead | External | The computational resources needed for error correction, calibration, control electronics, and classical pre/post-processing that support quantum operations |
| Computational Advantage | Internal | The factor by which a quantum computer outperforms the best classical algorithm for a specific problem — must exceed 1 for quantum computing to be useful |

### Research for Lesson
- Classical vs. Quantum Information — reference materials and textbook resources
- The Decoherence Problem — reference materials and textbook resources
- The Error Correction Challenge — reference materials and textbook resources
- The Race to Quantum Advantage — reference materials and textbook resources

---

## Activity 1: LOCATE — Build Your System

### Text Editor

```
QUANTUM COMPUTING: WHY 0 AND 1 AREN'T ENOUGH

Modeling the Physics and Engineering of Computation Beyond Classical Limits.
Why would a computer that uses the weirdest rules in physics be millions of times faster than the most powerful supercomputer ever built?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Cooling Temperature" — the operating temperature of the quantum processor
  ○ Click "Classical Overhead" — the computational resources needed for error correction
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Qubit Coherence Time" — the duration a qubit maintains its quantum state before decoherence destroys the superposition — currently measured in microseconds to milliseconds for superconducting qubits
  ○ Click "Entanglement Fidelity" — the accuracy with which two qubits can be entangled and maintain their correlation — measured as a percentage where 99
  ○ Click "Error Rate" — the probability that a quantum gate operation produces an incorrect result — currently around 0
  ○ Click "Gate Operation Speed" — the time required to perform a single quantum logic operation on one or two qubits — faster gates allow more operations within the coherence window
  ○ Click "Quantum Volume" — a holistic metric combining qubit count
  ○ Click "Decoherence Rate" — the speed at which environmental interference destroys quantum states — determined by temperature
  ○ Click "Computational Advantage" — the factor by which a quantum computer outperforms the best classical algorithm for a specific problem — must exceed 1 for quantum computing to be useful

STEP 2: ADD TO YOUR MODEL
• Click the PLUS (+) button to add each component to your picture
• You should now see 9 components on your canvas

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
"Why would a computer that uses the weirdest rules in physics be millions of times faster than the most powerful supercomputer ever built?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Qubit Coherence Time' — that's internal. The duration a qubit maintains its quantum state before decoherence destroys the superposition — currently measured in microseconds to milliseconds for superconducting qubits.
Click on 'Entanglement Fidelity' — that's internal. The accuracy with which two qubits can be entangled and maintain their correlation — measured as a percentage where 99.
Click on 'Error Rate' — that's internal. The probability that a quantum gate operation produces an incorrect result — currently around 0.
Click on 'Gate Operation Speed' — that's internal. The time required to perform a single quantum logic operation on one or two qubits — faster gates allow more operations within the coherence window.
Click on 'Cooling Temperature' — that's external. The operating temperature of the quantum processor.
Click on 'Quantum Volume' — that's internal. A holistic metric combining qubit count.
Click on 'Decoherence Rate' — that's internal. The speed at which environmental interference destroys quantum states — determined by temperature.
Click on 'Classical Overhead' — that's external. The computational resources needed for error correction.
Click on 'Computational Advantage' — that's internal. The factor by which a quantum computer outperforms the best classical algorithm for a specific problem — must exceed 1 for quantum computing to be useful.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Cooling Temperature is external because it is a direct engineering input — the dilution refrigerator temperature is set by the cryogenic system design and operation. Classical Overhead is external because it represents the classical computing resources (control electronics, error correction processing, calibration systems) that engineers allocate to support the quantum processor. The remaining seven components are internal because they are properties of the quantum system that emerge from the physical conditions: coherence time, entanglement fidelity, error rate, gate speed, quantum volume, decoherence rate, and computational advantage are all determined by the interplay between qubit physics and environmental conditions.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next activity, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 9 components sorted: Cooling Temperature, Classical Overhead (External), Qubit Coherence Time, Entanglement Fidelity, Error Rate, Gate Operation Speed, Quantum Volume, Decoherence Rate, Computational Advantage (Internal)]

### Graph
[Empty graph panel — no simulation yet]

---

## Activity 2: ESTABLISH — Connect the Relationships

### Text Editor

```
TIME TO DRAW THE INVISIBLE LINES

Those 9 components don't just sit there — they AFFECT each other.
When one changes, others change too. Let's map those connections.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: OPEN CONNECTION MODE
• Click the "Connect" icon in the TOP LEFT corner of your screen
• Your cursor is now ready to draw relationship arrows

STEP 2: DRAW YOUR RELATIONSHIPS
• Click on "Cooling Temperature" and drag an arrow to "Decoherence Rate"
• Click on "Decoherence Rate" and drag an arrow to "Qubit Coherence Time"
• Click on "Error Rate" and drag an arrow to "Classical Overhead"

STEP 3: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Cooling Temperature → Decoherence Rate = NEGATIVE (−)
    Lower cooling temperature means fewer thermal photons and phonons interacting with qubits, reducing the rate at which environmental noise destroys quantum states. Even tiny temperature increases dramatically accelerate decoherence.

  ○ Decoherence Rate → Qubit Coherence Time = NEGATIVE (−)
    Higher decoherence rate means quantum states collapse faster, directly reducing the time window available for quantum operations. Coherence time is inversely related to decoherence rate.

  ○ Error Rate → Classical Overhead = POSITIVE (+)
    Higher error rates require more physical qubits dedicated to error correction codes and more classical processing for syndrome measurement and correction — increasing the classical overhead and reducing the qubits available for actual computation.

STEP 4: CHECK YOUR MODEL
• You should have 3 arrows total
• 2 negative relationship(s), 1 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: Qubit Coherence Time sets the clock — every quantum computation must complete before decoherence destroys the quantum state. But Error Rate means you need error correction, which requires more qubits and more time. How do engineers escape this trap where fixing errors consumes the very resource errors steal?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Cooling Temperature' and drag an arrow
over to 'Decoherence Rate.'

Here's the key question: When cooling temperature goes UP, does
decoherence rate go UP or DOWN?

Lower cooling temperature means fewer thermal photons and phonons interacting with qubits, reducing the rate at which environmental noise destroys quantum states. Even tiny temperature increases dramatically accelerate decoherence.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Next connection: Click on 'Decoherence Rate' and drag an arrow
over to 'Qubit Coherence Time.'

Here's the key question: When decoherence rate goes UP, does
qubit coherence time go UP or DOWN?

Higher decoherence rate means quantum states collapse faster, directly reducing the time window available for quantum operations. Coherence time is inversely related to decoherence rate.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Last connection: Click on 'Error Rate' and drag an arrow
over to 'Classical Overhead.'

Here's the key question: When error rate goes UP, does
classical overhead go UP or DOWN?

Higher error rates require more physical qubits dedicated to error correction codes and more classical processing for syndrome measurement and correction — increasing the classical overhead and reducing the qubits available for actual computation.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Look at your model now. You've got 2 negative and 1
positive relationships. 3 arrows total.

Qubit Coherence Time sets the clock — every quantum computation must complete before decoherence destroys the quantum state. But Error Rate means you need error correction, which requires more qubits and more time. How do engineers escape this trap where fixing errors consumes the very resource errors steal?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Cooling Temperature −→ Decoherence Rate, Decoherence Rate −→ Qubit Coherence Time, Error Rate +→ Classical Overhead]

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
• When Cooling Temperature is HIGH, what happens to the internal components?

STEP 3: SCENARIO — CURRENT TECHNOLOGY
• 2024-era qubit parameters with 100 microsecond coherence
• PREDICT FIRST: What do you predict the Computational Advantage will be with today's noisy, error-prone qubits?
• Resume the simulation and observe what happens
• Was your prediction correct?

STEP 4: SCENARIO — NEAR-PERFECT QUBITS
• Error rate reduced to 0.01%, coherence extended to 10 ms
• PREDICT FIRST: What do you predict happens to Quantum Volume when errors become rare enough for deep circuits?
• Resume the simulation and observe what happens
• Was your prediction correct?

STEP 5: SCENARIO — THERMAL DISRUPTION
• Cooling temperature rises from 15 mK to 100 mK
• PREDICT FIRST: What do you predict happens to the quantum state when the processor warms up by even a fraction of a degree?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Quantum computing power is not limited by processing speed but by the race between computation and decoherence — every calculation must finish before the quantum state collapses
• Error rates compound exponentially across quantum circuits, meaning a 0.5% error per gate becomes near-certain failure after a few hundred gates without error correction
• Error correction itself requires massive overhead — correcting one logical qubit may need 1,000+ physical qubits, creating a resource paradox where most qubits are spent on error management rather than computation
• Quantum advantage is problem-specific, not universal — quantum computers will not replace classical computers but will solve specific problems (cryptography, molecular simulation, optimization) that are fundamentally intractable classically

THE ANSWER: A quantum computer exploits superposition and entanglement to explore exponentially many solutions simultaneously — something classical bits cannot do. But this power is incredibly fragile. Qubits lose their quantum properties (decohere) within microseconds due to the slightest environmental disturbance — heat, vibration, electromagnetic noise. Every quantum operation has a nonzero error rate that compounds across the circuit. And correcting these errors requires enormous overhead: roughly 1,000 physical qubits to protect one logical qubit. The engineering challenge is not making qubits faster but making them quiet, stable, and error-resistant enough to complete useful computations before decoherence destroys the quantum state.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Current Technology. 2024-era qubit parameters with 100 microsecond coherence.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Near-Perfect Qubits.
Error rate reduced to 0.01%, coherence extended to 10 ms.

Before you run it — make a prediction. What do you predict happens to Quantum Volume when errors become rare enough for deep circuits?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Thermal Disruption. Cooling temperature rises from 15 mK to 100 mK.
What do you predict happens to the quantum state when the processor warms up by even a fraction of a degree?

Here's what our model reveals: A quantum computer exploits superposition and entanglement to explore exponentially many solutions simultaneously — something classical bits cannot do. But this power is incredibly fragile. Qubits lose their quantum properties (decohere) within microseconds due to the slightest environmental disturbance — heat, vibration, electromagnetic noise. Every quantum operation has a nonzero error rate that compounds across the circuit. And correcting these errors requires enormous overhead: roughly 1,000 physical qubits to protect one logical qubit. The engineering challenge is not making qubits faster but making them quiet, stable, and error-resistant enough to complete useful computations before decoherence destroys the quantum state.

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
   • What happens if you turn OFF Cooling Temperature?
   • What happens if you turn OFF Classical Overhead?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Qubit Connectivity — The pattern of which qubits can directly interact with which others — full connectivity allows any two qubits to entangle directly, while limited connectivity requires extra operations to route information
   • Readout Fidelity — The accuracy with which the final quantum state can be measured and converted to a classical result — imperfect readout adds another layer of error to quantum computation
   • Crosstalk Interference — Unwanted coupling between neighboring qubits that causes operations on one qubit to disturb adjacent qubits — a major source of correlated errors in dense qubit arrays

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • Classical vs. Quantum Information — how does this connect to your model?
   • The Decoherence Problem — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model demonstrate that quantum computing is fundamentally a race against decoherence?
   • Why does the error correction overhead create a paradox — and how might future technology resolve it?
   • What does your model predict about the minimum qubit quality needed for quantum advantage on real problems?
   • How would your model change if a room-temperature qubit technology were invented?

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

Qubit Connectivity. The pattern of which qubits can directly interact with which others — full connectivity allows any two qubits to entangle directly, while limited connectivity requires extra operations to route information
How would you model that?

Readout Fidelity. The accuracy with which the final quantum state can be measured and converted to a classical result — imperfect readout adds another layer of error to quantum computation
How would you model that?

Crosstalk Interference. Unwanted coupling between neighboring qubits that causes operations on one qubit to disturb adjacent qubits — a major source of correlated errors in dense qubit arrays
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

Quantum Computing Engineers design and optimize quantum processors, error correction schemes, and quantum algorithms. They work at IBM, Google, Microsoft, Amazon, and startups like IonQ, Rigetti, and PsiQuantum, earning $120,000-$250,000/year. This is one of the fastest-growing and highest-paying fields in technology.

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
Visual: Title slide with dramatic quantum computer dilution refrigerator image
Say: "Your phone has billions of classical bits. This machine has 1,000 qubits and costs 50 million dollars. Yet for certain problems, this machine wins. Why?"
Do: Show an image of a quantum computer's golden chandelier hardware next to a smartphone. The contrast hooks students: why is this bizarre machine more powerful?
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and vocabulary terms
Say: "Today you are modeling computation at the boundary of physics — where the rules of quantum mechanics create possibilities that classical physics cannot match, but also create engineering nightmares."
Do: Have students read objectives. Pre-teach 'superposition' and 'decoherence' using the coin analogy: a spinning coin is both heads and tails until it lands.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: Why would a computer using quantum weirdness beat the most powerful supercomputer?
Say: "A classical computer with 300 bits can be in one of 2^300 states. A quantum computer with 300 qubits can be in all 2^300 states simultaneously. That number has more digits than atoms in the universe."
Do: Quick-write: Students estimate how many states 10 classical bits vs. 10 qubits can represent. Share out. Then scale to 50, 100, 300 — watch the exponential growth click.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps overview with quantum computing context
Say: "We are building a model of the most delicate machine ever engineered — a computer that operates at temperatures colder than deep space and breaks if a truck drives by on the street outside."
Do: Preview LEVER steps. Emphasize that this model captures the central tension: quantum power versus quantum fragility.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Nine component cards for quantum computing model
Say: "Nine parameters. Two you can control through engineering. Seven that the physics determines. The question is whether engineering can push the physics far enough."
Do: Guide students through components. Discuss why Cooling Temperature and Classical Overhead are external — they represent the engineering resources committed to supporting quantum operations.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows between nine components
Say: "Here is the cruel paradox: errors require correction, correction requires more qubits, more qubits generate more errors. How do you break that cycle?"
Do: Help students map the decoherence-error-correction cascade. Identify the error correction overhead paradox. Use red for destructive pathways.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Simulation graphs for three scenarios
Say: "Can today's quantum computers actually outperform a classical supercomputer? Let us find out — and discover exactly what needs to improve."
Do: Students predict Computational Advantage for each scenario. Run simulations. Compare how dramatically near-perfect qubits change the picture.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key findings from model exploration
Say: "Quantum computing is not about making computers faster — it is about making a fundamentally different kind of computation possible. But only if engineering can keep the quantum states alive long enough."
Do: Lead discussion connecting model findings to real quantum milestones. Google's quantum supremacy claim, IBM's quantum roadmap, the path to useful quantum advantage.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Quantum Error Correction Strategy design challenge
Say: "You have 1,000 physical qubits. How many become computation qubits, how many become error correction, and what can you actually solve? Your strategy determines whether this is a 50-million-dollar paperweight or a revolutionary machine."
Do: Groups design error correction allocation strategies. Present with justification from model data. Class evaluates which strategy maximizes real computational power.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: Quantum Computing: Why 0 and 1 Aren't Enough
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
Classical computers have transformed civilization using a simple language: 0 and 1. Every photo, video, app, and AI model is built from billions of binary switches. But some problems are so complex that even a computer with every atom in the universe as a transistor could not solve them before the heat death of the cosmos. Quantum computing offers a fundamentally different approach — but building it requires engineering at the edge of physical possibility.

NGSS ALIGNMENT:
HS-PS4-3, HS-PS2-5: Evaluate the claims, evidence, and reasoning behind the idea that electromagnetic radiation can be described either by a wave model or a particle model. Plan and conduct an investigation to provide evidence that an electric current can produce a magnetic field and that a changing magnetic field can produce an electric current.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Evaluating Claims and Evidence
  Students evaluate claims about quantum computing capabilities by modeling the physical constraints that determine whether quantum advantage is achievable for specific problems.
• Disciplinary Core Idea: PS4.A Wave Properties / PS2.B Types of Interactions
  Students model how quantum mechanical properties (superposition, entanglement) enable fundamentally different information processing, and how electromagnetic interactions cause decoherence.
• Crosscutting Concept: Cause and Effect
  Students trace causal chains from environmental noise through decoherence to error accumulation to computational failure, identifying the mechanisms that limit quantum computing performance.

PACING GUIDE:
• Activity 1 (Locate): 8-10 minutes
• Activity 2 (Establish): 8-10 minutes
• Activity 3 (Visualize & Evaluate): 10-12 minutes
• Activity 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Qubit, Superposition, Entanglement, Decoherence
□ Prepare Why would a computer that uses the weirdest rules in physics be millions of times faster than the most powerful supercomputer ever built discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify nine key components of a quantum computing system: qubit coherence time, entanglement fidelity, error rate, gate operation speed, cooling temperature, quantum volume, decoherence rate, classical overhead, and computational advantage.
• Establish: Students map relationships showing that cooling temperature drives decoherence rate, which determines coherence time, which limits the number of gate operations possible — while error rate determines how much of that limited time must be spent on error correction rather than useful computation.
• Visualize: Students build a computational model showing the nine-component quantum system with the central tension between computation speed and decoherence.
• Evaluate: Students run current technology, near-perfect qubits, and thermal disruption scenarios to identify the parameter thresholds where quantum advantage becomes achievable.
• Revise: Students add qubit connectivity, readout fidelity, or crosstalk interference to model more realistic quantum processor behavior.

BACKGROUND CONTENT:
• Classical vs. Quantum Information:
  A classical bit is a switch: 0 or 1, on or off. A qubit exploits quantum superposition to be in a combination of 0 and 1 simultaneously, described by probability amplitudes. Two qubits can represent four states at once, three can represent eight, and N qubits can represent 2^N states simultaneously. For 300 qubits, that is more states than atoms in the observable universe. This exponential scaling is the source of quantum computing's potential power.

• The Decoherence Problem:
  Quantum states are extraordinarily fragile. Any interaction with the environment — a single stray photon, a vibration from a passing truck, thermal energy from a fraction of a degree of warmth — can cause decoherence, collapsing the delicate superposition into an ordinary classical state. This is why quantum computers are cooled to 15 millikelvin (colder than outer space), suspended on vibration-isolating platforms, and shielded from electromagnetic radiation. Even with all these precautions, coherence times are measured in microseconds.

• The Error Correction Challenge:
  With per-gate error rates around 0.1-1%, a quantum circuit with 1,000 gates has a near-certain probability of containing errors. Quantum error correction encodes one logical qubit across many physical qubits, allowing errors to be detected and corrected. But the overhead is staggering: current schemes require roughly 1,000 physical qubits per logical qubit. A useful quantum computer might need millions of physical qubits to produce the thousands of error-corrected logical qubits needed for practical algorithms.

• The Race to Quantum Advantage:
  In 2019, Google claimed quantum supremacy with its 53-qubit Sycamore processor, completing a specific calculation in 200 seconds that would take a classical supercomputer 10,000 years. Critics argued the problem was artificial. True quantum advantage — solving a practical, economically valuable problem faster than any classical approach — remains the holy grail. The most promising applications are drug discovery (simulating molecular interactions), cryptography (breaking current encryption), optimization (logistics, finance), and materials science (designing new materials at the atomic level).

COMMON MISCONCEPTIONS:
• "Quantum computers are just faster classical computers"
  Reality: Quantum computers are fundamentally different, not just faster. They do not execute classical operations more quickly — they exploit superposition and entanglement to explore solution spaces in ways impossible for classical architecture. For most everyday tasks (email, web browsing, video streaming), quantum computers offer no advantage. Their power emerges only for specific problem types where quantum algorithms exist. A quantum computer will never replace your laptop — it will solve problems your laptop cannot even attempt.
  Strategy: Analogy: A submarine is not a faster car. It operates in a completely different medium (water vs. road) and excels at tasks cars cannot do. Quantum computers operate in a different computational medium (quantum states vs. binary logic) and excel at different problems.

• "Qubits are just bits that can be 0 and 1 at the same time"
  Reality: This is a common oversimplification that misses the crucial point. A qubit in superposition is described by a complex probability amplitude — a mathematical object with both magnitude and phase. Quantum advantage comes not just from superposition but from interference, where probability amplitudes add or cancel. Quantum algorithms are carefully designed so that correct answers constructively interfere (amplitudes add) and wrong answers destructively interfere (amplitudes cancel). Without this interference engineering, superposition alone is useless.
  Strategy: Demonstrate: If a qubit being 0 and 1 simultaneously were all there was to it, measuring it would give a random result — no better than flipping a coin. The magic is in engineering the interference patterns so the right answer is overwhelmingly probable.

• "Quantum computers will break all encryption tomorrow"
  Reality: Current quantum computers have fewer than 1,500 noisy physical qubits. Breaking RSA-2048 encryption with Shor's algorithm would require approximately 4,000 error-corrected logical qubits, which translates to roughly 20 million physical qubits at current error rates. Even optimistic timelines place this capability a decade or more in the future. Meanwhile, post-quantum cryptography algorithms that are resistant to quantum attack are already being standardized and deployed. The threat is real but not imminent.
  Strategy: Calculate: If we need 20 million physical qubits and the current largest processor has about 1,200, how many doublings are needed? At the current rate of progress, estimate when 20 million qubits might be achievable.

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
Big Question: Why would a computer that uses the weirdest rules in physics be millions of times faster than the most powerful supercomputer ever built?
Answer: A quantum computer exploits superposition and entanglement to explore exponentially many solutions simultaneously — something classical bits cannot do. But this power is incredibly fragile. Qubits lose their quantum properties (decohere) within microseconds due to the slightest environmental disturbance — heat, vibration, electromagnetic noise. Every quantum operation has a nonzero error rate that compounds across the circuit. And correcting these errors requires enormous overhead: roughly 1,000 physical qubits to protect one logical qubit. The engineering challenge is not making qubits faster but making them quiet, stable, and error-resistant enough to complete useful computations before decoherence destroys the quantum state.

Simulation Answers:
• Current Technology Scenario: With 2024-era parameters — 100 microsecond coherence, 0.5% error rate, 15 mK cooling — the model shows limited Computational Advantage. The high error rate means most qubits must be dedicated to error correction, leaving few logical qubits for computation. Gate operations are fast enough to fit many operations within the coherence window, but error accumulation limits useful circuit depth to hundreds of gates. Quantum Volume is modest, and Computational Advantage exceeds classical computers only for narrow, specially designed problems.
• Near-Perfect Qubits Scenario: Reducing Error Rate to 0.01% and extending Coherence Time to 10 milliseconds dramatically transforms the system. Error correction overhead drops by an order of magnitude, freeing physical qubits for computation. The longer coherence window allows circuits of tens of thousands of gates. Quantum Volume increases by several orders of magnitude. Computational Advantage becomes significant for practical problems like molecular simulation, optimization, and cryptanalysis. This scenario reveals the threshold at which quantum computing transitions from physics experiment to useful technology.

Reflection Exemplars:
• Q: Why is quantum computing a race against decoherence?
  A: Every quantum computation must complete before the environment destroys the quantum state. Coherence time sets a hard deadline — typically microseconds — within which all gate operations, error correction, and measurement must finish. If the computation takes longer than the coherence time, the qubits collapse into classical states and the result is meaningless random noise. This is fundamentally different from classical computing, where a calculation can take as long as needed. The model shows this clearly: increasing computation depth eventually crosses the coherence boundary, and Computational Advantage drops to zero.
• Q: Why does error correction create a paradox?
  A: Each physical qubit has a nonzero error rate per operation. Error correction protects logical qubits by distributing information across many physical qubits and detecting errors through redundancy. But this requires roughly 1,000 physical qubits per logical qubit with current error rates. The correction process itself requires gate operations, which introduce their own errors. And more physical qubits mean more potential decoherence events. The paradox is that the solution to errors introduces more potential for errors. The escape route is reducing per-gate error rates below a critical threshold where error correction gains outpace the errors it introduces — the fault-tolerance threshold, currently estimated around 0.1% per gate.

STEM CHALLENGE GUIDANCE:
Title: Design a Quantum Error Correction Strategy
Mission: Design an error correction approach for a 1,000-qubit quantum processor that maximizes the number of usable logical qubits while keeping total error rates below the threshold for useful computation.
Scenario: A quantum computing company has built a 1,000 physical qubit processor with a per-gate error rate of 0.3% and a coherence time of 200 microseconds. They need your team to design an error correction strategy that determines how many physical qubits to dedicate to error correction versus computation, and whether the resulting logical qubits can solve problems that justify the system's $50 million cost.
Introduction: Present the challenge: A quantum computing company has a 1,000-qubit processor and needs your team to design the optimal allocation between error correction and useful computation. Your strategy will determine whether this $50 million machine can solve problems no classical computer can — or whether it is an expensive physics experiment.

Key Concepts:
• Surface Codes: The leading quantum error correction approach tiles qubits in a 2D grid where data qubits are surrounded by syndrome qubits that detect errors. Current surface codes require roughly 1,000 physical qubits per logical qubit at 0.1% error rates — this ratio improves dramatically as error rates decrease.
• Logical vs. Physical Qubits: Physical qubits are the actual quantum devices on the chip. Logical qubits are the error-corrected computational units built from many physical qubits. A 1,000 physical qubit machine might yield only 1-10 logical qubits — and the number of logical qubits determines what problems can be solved.
• NISQ vs. Fault-Tolerant: Current quantum computers are NISQ (Noisy Intermediate-Scale Quantum) — too error-prone for full error correction but potentially useful for near-term algorithms designed to tolerate noise. Fault-tolerant quantum computing, with full error correction, requires millions of physical qubits and may be a decade away.

Evaluation Rubric:
• Expert (4): Strategy specifies an error correction code, calculates the physical-to-logical qubit ratio, identifies achievable circuit depth, names specific problems the resulting system could solve, and justifies all decisions with model evidence
• Proficient (3): Strategy allocates qubits between correction and computation with model-based justification and identifies target applications
• Developing (2): Strategy proposes a qubit allocation but lacks quantitative justification or does not connect to specific computational problems
• Beginning (1): Strategy is incomplete or does not address the fundamental error correction versus computation trade-off

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a visual showing 1,000 physical qubits divided into color-coded blocks for error correction versus computation at different error rates
  • Use a timeline diagram showing the coherence window with gate operations stacked inside it to visualize the race against decoherence
  • Sentence frames: 'With an error rate of __%, our correction code requires __ physical qubits per logical qubit, leaving __ logical qubits for computation, which is enough to solve __'

Extensions (Advanced Learners):
  • Research the different physical implementations of qubits — superconducting, trapped ion, photonic, topological — and compare their strengths across the nine model parameters
  • Investigate Shor's algorithm for factoring large numbers and calculate how many logical qubits would be needed to break current RSA encryption
  • Explore how quantum computing could revolutionize drug discovery by simulating molecular interactions that classical computers cannot model accurately

Cross-Curricular Connections:
  • Math: Calculate the exponential scaling: if a classical computer needs 2^N operations to search an unsorted database of N items, and Grover's quantum algorithm needs only the square root of 2^N, how much faster is the quantum approach for databases of 1 million, 1 billion, and 1 trillion entries?
  • ELA: Write a science journalism article explaining quantum computing to a general audience without using jargon, using analogies and model results to make the concepts accessible and accurate
  • Computer Science: Compare the computational complexity classes P, NP, and BQP — which problems can classical computers solve efficiently, which can quantum computers solve efficiently, and which remain hard for both?

CAST ALIGNMENT:
• Model how nine interdependent parameters determine quantum computational advantage over classical systems
• Analyze the trade-off between error correction overhead and usable computational qubits
• Predict the technology thresholds required for quantum computers to solve real-world problems

CAST-Style Assessment Questions:
• Multiple Choice: A quantum computer's coherence time is 100 microseconds and each gate operation takes 50 nanoseconds. If a useful computation requires 5,000 gates, what does your model predict about the computation's success without error correction?
• Constructed Response: Using your model, explain why doubling the number of qubits does not simply double a quantum computer's power. Address the roles of coherence time, error rate, and error correction overhead in your explanation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: Quantum Computing: Why 0 and 1 Aren't Enough
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. What is the difference between a classical bit (0 or 1) and a quantum bit (qubit)?

   _________________________________________________________

   _________________________________________________________

2. Why do you think quantum computers need to be cooled to near absolute zero?

   _________________________________________________________

   _________________________________________________________

3. Draw what you think happens when a qubit is in superposition versus when it is measured.

   [DRAWING BOX]

4. If quantum computers are so powerful, why don't we use them for everything already?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Qubit                         
___ Superposition                 
___ Entanglement                  
___ Decoherence                   

A. A quantum bit that can exist in a superposition of 0 and 1 simultaneously — unlike classical bits that must be one or the other — enabling quantum computers to explore many solutions in parallel
B. The quantum mechanical property allowing a particle to exist in multiple states at once until measured — a qubit in superposition is both 0 and 1 with certain probabilities, not simply unknown
C. A quantum correlation where two or more qubits become linked so that measuring one instantly determines the state of the other, regardless of distance — enabling quantum algorithms to process information in ways impossible for classical computers
D. The process by which quantum states lose their quantum properties through interaction with the environment — heat, vibration, electromagnetic noise — collapsing superposition and destroying the quantum advantage

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

SCENARIO: Current Technology
Settings: 2024-era qubit parameters with 100 microsecond coherence
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Near-Perfect Qubits
Settings: Error rate reduced to 0.01%, coherence extended to 10 ms
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Thermal Disruption
Settings: Cooling temperature rises from 15 mK to 100 mK
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

1. How does your model demonstrate that quantum computing is fundamentally a race against decoherence?

   _________________________________________________________

   _________________________________________________________

2. Why does the error correction overhead create a paradox — and how might future technology resolve it?

   _________________________________________________________

   _________________________________________________________

3. What does your model predict about the minimum qubit quality needed for quantum advantage on real problems?

   _________________________________________________________

   _________________________________________________________

4. How would your model change if a room-temperature qubit technology were invented?

   _________________________________________________________

   _________________________________________________________

5. What are the limitations of modeling quantum computation with classical simulation tools?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Why would a computer that uses the weirdest rules in physics be millions of times faster than the most powerful supercomputer ever built? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Evaluating Claims and Evidence
   □ Disciplinary Core Idea: PS4.A Wave Properties / PS2.B Types of Interactions
   □ Crosscutting Concept: Cause and Effect

3. What are the limitations of modeling quantum computation with classical simulation tools?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Quantum Error Correction Strategy
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design an error correction approach for a 1,000-qubit quantum processor that maximizes the number of usable logical qubits while keeping total error rates below the threshold for useful computation.

SCENARIO: A quantum computing company has built a 1,000 physical qubit processor with a per-gate error rate of 0.3% and a coherence time of 200 microseconds. They need your team to design an error correction strategy that determines how many physical qubits to dedicate to error correction versus computation, and whether the resulting logical qubits can solve problems that justify the system's $50 million cost.

GUIDING QUESTIONS:
• How many physical qubits would you dedicate to error correction versus actual computation, and why?
• What is the minimum error rate per gate needed for your error correction scheme to work?
• For what types of problems would your quantum system outperform a classical supercomputer?

DESIGN THINKING:
• What error correction code will you use and what is its qubit overhead ratio?

  _________________________________________________________

• How many logical qubits does your strategy produce from 1,000 physical qubits?

  _________________________________________________________

• What circuit depth can your logical qubits support before accumulated errors exceed your correction capacity?

  _________________________________________________________

• What specific real-world problem could your system solve that a classical computer cannot?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Strategy specifies an error correction code, calculates the physical-to-logical qubit ratio, identifies achievable circuit depth, names specific problems the resulting system could solve, and justifies all decisions with model evidence
• Proficient (3): Strategy allocates qubits between correction and computation with model-based justification and identifies target applications
• Developing (2): Strategy proposes a qubit allocation but lacks quantitative justification or does not connect to specific computational problems
• Beginning (1): Strategy is incomplete or does not address the fundamental error correction versus computation trade-off

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-10/G10L3-L03/G10L3-L03-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-10/G10L3-L03/G10L3-L03-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-10/G10L3-L03/G10L3-L03-Student-Presentation.pptx] |
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