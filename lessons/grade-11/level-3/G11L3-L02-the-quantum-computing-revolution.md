# Lesson: The Quantum Computing Revolution

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G11L3-L02 |
| **Grade** | 11th Grade — Level 3: Systems Innovation Lab |
| **Lesson Name** | The Quantum Computing Revolution |
| **Status** | Template |

---

## Platform

### Title
**The Quantum Computing Revolution — Modeling Qubit Behavior, Superposition, and Computational Advantage**

### Overview
Classical computers process information as bits — switches that are either 0 or 1. Every computation, from spreadsheets to artificial intelligence, reduces to manipulating these binary values. Quantum computers exploit the laws of quantum mechanics to process information in fundamentally different ways, using qubits that can exist in superposition of 0 and 1 simultaneously. This is not simply faster classical computing — it is a different kind of computation that can solve certain problems exponentially faster than any classical machine ever built. Students investigate the driving question: Why would a computer built on the strangest rules in physics solve problems that every supercomputer on Earth combined could never crack? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of a massive quantum computing dilution refrigerator with its golden cylindrical stages visible, glowing with subtle blue quantum light effects, in a state-of-the-art quantum laboratory, featuring a diverse multicultural group with Black people centered of 16-17 year old students observing the hardware]

### Grade
11th Grade — Level 3: Systems Innovation Lab

### NGSS Standard
**HS-PS4-3, HS-PS4-5**: Evaluate the claims, evidence, and reasoning behind the idea that electromagnetic radiation can be described either by a wave model or a particle model, and that for some situations one model is more useful than the other. Communicate technical information about how some technological devices use the principles of wave behavior and wave interactions with matter to transmit and capture information and energy.

### Learning Objectives
- Model how qubits exploit superposition and entanglement to process exponentially more information than classical bits
- Analyze the engineering trade-offs between qubit coherence time, error rates, and computational depth in quantum circuits
- Evaluate why maintaining quantum states is fundamentally at odds with the thermal environment qubits must exist in
- Predict the conditions under which quantum advantage becomes achievable for specific problem classes

### Component List (Starting Model: 7 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Qubit Count | External | The total number of physical qubits available on the quantum processor — more qubits enable larger computations but also increase the complexity of control and error management |
| Coherence Time | Internal | The duration a qubit maintains its quantum superposition state before environmental noise causes decoherence — currently measured in microseconds to milliseconds for superconducting qubits |
| Gate Error Rate | Internal | The probability that a quantum logic operation produces an incorrect result — currently around 0.1-1% per gate for leading systems, which compounds exponentially across circuits with hundreds of operations |
| Entanglement Fidelity | Internal | The accuracy with which pairs of qubits can be entangled and maintain their quantum correlation — must exceed 99% for quantum algorithms to produce meaningful results |
| Operating Temperature | External | The thermal environment of the quantum processor — superconducting qubits require cooling to 15 millikelvin (colder than outer space) because any thermal energy destroys quantum states |
| Circuit Depth | Internal | The number of sequential gate operations that can be performed before accumulated errors and decoherence destroy the quantum state — deeper circuits solve harder problems but require better qubits |
| Quantum Volume | Internal | A holistic performance metric combining qubit count, connectivity, gate fidelity, and coherence time to measure actual computational capability rather than just qubit count |

### Research for Lesson
- Superposition and Quantum Parallelism — reference materials and textbook resources
- Entanglement and Quantum Algorithms — reference materials and textbook resources
- The Decoherence Challenge — reference materials and textbook resources
- The Path to Fault Tolerance — reference materials and textbook resources

---

## Step 1: LOCATE — Build Your System

### Text Editor

```
THE QUANTUM COMPUTING REVOLUTION

Modeling Qubit Behavior, Superposition, and Computational Advantage.
Why would a computer built on the strangest rules in physics solve problems that every supercomputer on Earth combined could never crack?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Qubit Count" — the total number of physical qubits available on the quantum processor — more qubits enable larger computations but also increase the complexity of control and error management
  ○ Click "Operating Temperature" — the thermal environment of the quantum processor — superconducting qubits require cooling to 15 millikelvin (colder than outer space) because any thermal energy destroys quantum states
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Coherence Time" — the duration a qubit maintains its quantum superposition state before environmental noise causes decoherence — currently measured in microseconds to milliseconds for superconducting qubits
  ○ Click "Gate Error Rate" — the probability that a quantum logic operation produces an incorrect result — currently around 0
  ○ Click "Entanglement Fidelity" — the accuracy with which pairs of qubits can be entangled and maintain their quantum correlation — must exceed 99% for quantum algorithms to produce meaningful results
  ○ Click "Circuit Depth" — the number of sequential gate operations that can be performed before accumulated errors and decoherence destroy the quantum state — deeper circuits solve harder problems but require better qubits
  ○ Click "Quantum Volume" — a holistic performance metric combining qubit count

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
"Why would a computer built on the strangest rules in physics solve problems that every supercomputer on Earth combined could never crack?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Qubit Count' — that's external. The total number of physical qubits available on the quantum processor — more qubits enable larger computations but also increase the complexity of control and error management.
Click on 'Coherence Time' — that's internal. The duration a qubit maintains its quantum superposition state before environmental noise causes decoherence — currently measured in microseconds to milliseconds for superconducting qubits.
Click on 'Gate Error Rate' — that's internal. The probability that a quantum logic operation produces an incorrect result — currently around 0.
Click on 'Entanglement Fidelity' — that's internal. The accuracy with which pairs of qubits can be entangled and maintain their quantum correlation — must exceed 99% for quantum algorithms to produce meaningful results.
Click on 'Operating Temperature' — that's external. The thermal environment of the quantum processor — superconducting qubits require cooling to 15 millikelvin (colder than outer space) because any thermal energy destroys quantum states.
Click on 'Circuit Depth' — that's internal. The number of sequential gate operations that can be performed before accumulated errors and decoherence destroy the quantum state — deeper circuits solve harder problems but require better qubits.
Click on 'Quantum Volume' — that's internal. A holistic performance metric combining qubit count.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Qubit Count is external because it represents the hardware design choice — how many physical qubits the engineering team fabricates on the processor chip. Operating Temperature is external because it represents the cryogenic engineering infrastructure — the dilution refrigerator temperature that engineers control through equipment design. The remaining five components are internal: Coherence Time, Gate Error Rate, and Entanglement Fidelity are physical properties that emerge from the qubit hardware and its thermal environment. Circuit Depth and Quantum Volume are computational properties determined by the interplay of all physical parameters.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next step, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 7 components sorted: Qubit Count, Operating Temperature (External), Coherence Time, Gate Error Rate, Entanglement Fidelity, Circuit Depth, Quantum Volume (Internal)]

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
• Click on "Operating Temperature" and drag an arrow to "Coherence Time"
• Click on "Coherence Time" and drag an arrow to "Circuit Depth"
• Click on "Gate Error Rate" and drag an arrow to "Quantum Volume"
• Click on "Qubit Count" and drag an arrow to "Quantum Volume"

Task C: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Operating Temperature → Coherence Time = NEGATIVE (−)
    Higher operating temperature increases thermal noise energy, which accelerates decoherence by disrupting the fragile quantum superposition state. As temperature rises, coherence time drops precipitously because thermal photons interact with and collapse qubit states.

  ○ Coherence Time → Circuit Depth = POSITIVE (+)
    Longer coherence time provides a larger window for quantum gate operations before the qubit state decoheres. More coherence time allows deeper circuits with more sequential operations, enabling more complex computations to complete successfully.

  ○ Gate Error Rate → Quantum Volume = NEGATIVE (−)
    Higher gate error rates mean each quantum operation has a greater chance of corrupting the computation. Accumulated errors reduce the effective circuit depth and limit the number of qubits that can work together reliably, directly decreasing quantum volume.

  ○ Qubit Count → Quantum Volume = POSITIVE (+)
    More physical qubits increase the computational space available for quantum algorithms and provide additional resources for error correction. However, this relationship is mediated by gate fidelity and connectivity — more qubits only help if they can be operated reliably.

Task D: CHECK YOUR MODEL
• You should have 4 arrows total
• 2 negative relationship(s), 2 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: Coherence Time sets a countdown clock — every quantum computation must complete before the qubits decohere. But quantum error correction, which extends effective coherence, requires MORE qubits and MORE gate operations. How do engineers escape this paradox where the cure for errors consumes the very resources errors are destroying?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Operating Temperature' and drag an arrow
over to 'Coherence Time.'

Here's the key question: When operating temperature goes UP, does
coherence time go UP or DOWN?

Higher operating temperature increases thermal noise energy, which accelerates decoherence by disrupting the fragile quantum superposition state. As temperature rises, coherence time drops precipitously because thermal photons interact with and collapse qubit states.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Next connection: Click on 'Coherence Time' and drag an arrow
over to 'Circuit Depth.'

Here's the key question: When coherence time goes UP, does
circuit depth go UP or DOWN?

Longer coherence time provides a larger window for quantum gate operations before the qubit state decoheres. More coherence time allows deeper circuits with more sequential operations, enabling more complex computations to complete successfully.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'Gate Error Rate' and drag an arrow
over to 'Quantum Volume.'

Here's the key question: When gate error rate goes UP, does
quantum volume go UP or DOWN?

Higher gate error rates mean each quantum operation has a greater chance of corrupting the computation. Accumulated errors reduce the effective circuit depth and limit the number of qubits that can work together reliably, directly decreasing quantum volume.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Qubit Count' and drag an arrow
over to 'Quantum Volume.'

Here's the key question: When qubit count goes UP, does
quantum volume go UP or DOWN?

More physical qubits increase the computational space available for quantum algorithms and provide additional resources for error correction. However, this relationship is mediated by gate fidelity and connectivity — more qubits only help if they can be operated reliably.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Look at your model now. You've got 2 negative and 2
positive relationships. 4 arrows total.

Coherence Time sets a countdown clock — every quantum computation must complete before the qubits decohere. But quantum error correction, which extends effective coherence, requires MORE qubits and MORE gate operations. How do engineers escape this paradox where the cure for errors consumes the very resources errors are destroying?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Operating Temperature −→ Coherence Time, Coherence Time +→ Circuit Depth, Gate Error Rate −→ Quantum Volume, Qubit Count +→ Quantum Volume]

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
• When Qubit Count is HIGH, what happens to the internal components?

Task C: SCENARIO — CURRENT STATE-OF-THE-ART
• 1,000 qubits, 100 microsecond coherence, 0.3% gate error rate
• PREDICT FIRST: What do you predict the quantum volume will be with today's noisy intermediate-scale quantum hardware?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task D: SCENARIO — ERROR-CORRECTED REGIME
• 10,000 qubits, 0.01% gate error, 10 ms coherence time
• PREDICT FIRST: What do you predict happens to circuit depth and computational advantage when errors become rare enough for fault-tolerant operation?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task E: SCENARIO — THERMAL DISRUPTION
• Operating temperature increases from 15 mK to 100 mK
• PREDICT FIRST: What do you predict happens to all quantum properties when thermal energy exceeds the qubit energy gap?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Quantum computing power grows exponentially with qubit count — 300 perfect qubits can represent more states simultaneously than there are atoms in the observable universe — but only if coherence and fidelity are maintained
• Gate error rates compound exponentially across circuit depth — a 0.3% error per gate becomes near-certain corruption after a few hundred gates, severely limiting the problems current hardware can solve
• Error correction creates a resource paradox: protecting one logical qubit may require 1,000 or more physical qubits, meaning the vast majority of a quantum computer's hardware is dedicated to managing errors rather than solving problems
• Quantum advantage is problem-specific — quantum computers will not replace classical computers for most tasks but will be transformative for specific applications like molecular simulation, cryptography, optimization, and machine learning

THE ANSWER: A quantum computer exploits superposition and entanglement to explore exponentially many computational paths simultaneously — something classical bits physically cannot do. But this quantum advantage is unimaginably fragile. Qubits lose their quantum properties within microseconds from the slightest environmental disturbance: a stray photon, a thermal vibration, even a cosmic ray. Every quantum gate operation introduces errors that compound across the circuit. Error correction requires roughly 1,000 physical qubits to protect each logical qubit, creating a resource paradox. The breakthrough will come not from building more qubits but from building quieter, more stable, and more precise qubits that maintain coherence long enough to complete useful computations — and we are approaching that threshold now.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Current State-of-the-Art. 1,000 qubits, 100 microsecond coherence, 0.3% gate error rate.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Error-Corrected Regime.
10,000 qubits, 0.01% gate error, 10 ms coherence time.

Before you run it — make a prediction. What do you predict happens to circuit depth and computational advantage when errors become rare enough for fault-tolerant operation?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Thermal Disruption. Operating temperature increases from 15 mK to 100 mK.
What do you predict happens to all quantum properties when thermal energy exceeds the qubit energy gap?

Here's what our model reveals: A quantum computer exploits superposition and entanglement to explore exponentially many computational paths simultaneously — something classical bits physically cannot do. But this quantum advantage is unimaginably fragile. Qubits lose their quantum properties within microseconds from the slightest environmental disturbance: a stray photon, a thermal vibration, even a cosmic ray. Every quantum gate operation introduces errors that compound across the circuit. Error correction requires roughly 1,000 physical qubits to protect each logical qubit, creating a resource paradox. The breakthrough will come not from building more qubits but from building quieter, more stable, and more precise qubits that maintain coherence long enough to complete useful computations — and we are approaching that threshold now.

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
   • What happens if you turn OFF Qubit Count?
   • What happens if you turn OFF Operating Temperature?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Qubit Connectivity — The degree to which qubits can directly interact with each other on the processor chip — limited connectivity forces extra gate operations to move information between distant qubits, consuming precious coherence time
   • Readout Fidelity — The accuracy with which the final quantum state of each qubit can be measured — measurement errors in the final readout can negate the computational advantage built up during the quantum circuit
   • Cross-Talk — Unwanted quantum interactions between neighboring qubits caused by their physical proximity on the chip — cross-talk creates correlated errors that are harder to correct than independent random noise

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • Superposition and Quantum Parallelism — how does this connect to your model?
   • Entanglement and Quantum Algorithms — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model demonstrate the exponential scaling of quantum computational power versus the exponential scaling of errors?
   • Why is the error correction overhead such a critical barrier to practical quantum computing?
   • What does your model reveal about the relationship between operating temperature and every other quantum parameter?
   • How would your model change if a room-temperature quantum computing technology were developed?

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

Qubit Connectivity. The degree to which qubits can directly interact with each other on the processor chip — limited connectivity forces extra gate operations to move information between distant qubits, consuming precious coherence time
How would you model that?

Readout Fidelity. The accuracy with which the final quantum state of each qubit can be measured — measurement errors in the final readout can negate the computational advantage built up during the quantum circuit
How would you model that?

Cross-Talk. Unwanted quantum interactions between neighboring qubits caused by their physical proximity on the chip — cross-talk creates correlated errors that are harder to correct than independent random noise
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

Quantum Software Engineers design algorithms and applications for quantum computers at companies like IBM Quantum, Google Quantum AI, IonQ, and Rigetti Computing, earning $120,000-$200,000/year. Quantum Hardware Engineers who build and maintain quantum processors work in cryogenics, microwave engineering, and materials science, earning $100,000-$180,000/year. Quantum Information Scientists at research universities and national labs push the theoretical boundaries of what quantum computers can achieve, earning $90,000-$170,000/year.

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
Visual: Title slide with dramatic quantum computing hardware image
Say: "Imagine a computer so powerful it could crack every password on the internet in seconds. Now imagine that same computer is destroyed by a single stray photon. Welcome to quantum computing — the most powerful and most fragile technology ever created."
Do: Open with the paradox of quantum power and fragility. Show an image of a dilution refrigerator and ask students why a computer needs to be colder than outer space.
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and vocabulary terms displayed
Say: "Today you are modeling a machine that operates by the rules of quantum mechanics — rules so strange that Einstein refused to believe them. But they are real, and they are the future of computing."
Do: Have students read objectives. Pre-teach 'superposition' using the NOT-a-coin analogy — the qubit is genuinely in both states, not just unknown. Pre-teach 'decoherence' as the enemy of quantum computing.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: Why would a quantum computer be millions of times faster for some problems?
Say: "The key word is SOME. Quantum computers will not make your phone faster or your video games better. But for specific problems — breaking encryption, simulating molecules, optimizing logistics — they will do what no classical computer ever could."
Do: Quick-write: Students list problems they think would benefit from exponentially faster computing. Share out. Challenge: Which problems would NOT benefit? Why not?
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps with quantum computing context
Say: "We are building a model where fragility is the central engineering challenge — every component must be nearly perfect because quantum errors compound exponentially."
Do: Preview LEVER steps. Emphasize the competing exponentials: power grows exponentially with qubits, but errors also grow exponentially with circuit depth.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Seven component cards for quantum computing model
Say: "Seven components determine whether this machine computes or collapses. Two of them — qubit count and operating temperature — are the engineering inputs. The rest are consequences of physics."
Do: Guide students through components. Discuss why qubit count and operating temperature are external — they are the hardware design choices. All other quantum properties emerge from these physical conditions.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows showing cascading dependencies from temperature through decoherence to computational output
Say: "Temperature controls everything. A fraction of a degree changes decoherence, which changes coherence time, which changes circuit depth, which changes whether you get an answer or noise."
Do: Help students map the cascade from temperature through all quantum parameters. Highlight the competing exponentials — power and errors both scale exponentially but in opposite directions.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Simulation results for three scenarios showing quantum volume and advantage metrics
Say: "Can today's quantum computers actually beat classical ones? Let us test the current state of the art, the near future, and what happens when things go wrong."
Do: Students predict quantum volume for each scenario. Key insight from thermal disruption: even a tiny temperature increase cascades catastrophically through every quantum parameter.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key findings from quantum computing model exploration
Say: "Quantum computing is not about speed — it is about doing something fundamentally different with information. But that difference is so fragile that most of the engineering is about protecting it from the universe that wants to destroy it."
Do: Lead discussion connecting model findings to real hardware progress. IBM's roadmap, Google's error correction results, and the timeline to useful quantum advantage.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Quantum computing application proposal design challenge
Say: "An investment firm wants to know: where will quantum computing first change the world? Your team needs to find the killer application and prove the numbers work."
Do: Groups select a problem domain and build an investment case. Must specify qubit requirements, timeline to hardware readiness, and economic value. Present with model evidence.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: The Quantum Computing Revolution
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
Classical computers process information as bits — switches that are either 0 or 1. Every computation, from spreadsheets to artificial intelligence, reduces to manipulating these binary values. Quantum computers exploit the laws of quantum mechanics to process information in fundamentally different ways, using qubits that can exist in superposition of 0 and 1 simultaneously. This is not simply faster classical computing — it is a different kind of computation that can solve certain problems exponentially faster than any classical machine ever built.

NGSS ALIGNMENT:
HS-PS4-3, HS-PS4-5: Evaluate the claims, evidence, and reasoning behind the idea that electromagnetic radiation can be described either by a wave model or a particle model, and that for some situations one model is more useful than the other. Communicate technical information about how some technological devices use the principles of wave behavior and wave interactions with matter to transmit and capture information and energy.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Using Mathematics and Computational Thinking
  Students use computational models to analyze how qubit parameters interact exponentially and calculate the resource requirements for fault-tolerant quantum computation.
• Disciplinary Core Idea: PS4.A Wave Properties / PS4.B Electromagnetic Radiation
  Students explore how quantum mechanical wave-particle duality, superposition, and measurement underpin qubit behavior and quantum information processing.
• Crosscutting Concept: Scale, Proportion, and Quantity
  Students analyze how quantum advantage scales exponentially with qubit count while errors also scale exponentially with circuit depth, creating competing exponentials that determine feasibility.

PACING GUIDE:
• Step 1 (Locate): 8-10 minutes
• Step 2 (Establish): 8-10 minutes
• Step 3 (Visualize & Evaluate): 10-12 minutes
• Step 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Qubit, Superposition, Entanglement, Decoherence, Quantum Error Correction
□ Prepare Why would a computer built on the strangest rules in physics solve problems that every supercomputer on Earth combined could never crack discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify seven key components of a quantum computing system: qubit count, coherence time, gate error rate, entanglement fidelity, operating temperature, circuit depth, and quantum volume.
• Establish: Students map relationships showing that operating temperature drives decoherence which limits coherence time which constrains circuit depth which determines quantum volume — revealing the cascading dependencies from physical engineering to computational capability.
• Visualize: Students build a computational model showing the seven-component quantum system with competing exponential scaling of power and errors.
• Evaluate: Students run current technology, error-corrected, and thermal disruption scenarios to identify the threshold conditions where quantum advantage emerges or collapses.
• Revise: Students add qubit connectivity, readout fidelity, or cross-talk to model more realistic quantum processor dynamics and limitations.

BACKGROUND CONTENT:
• Superposition and Quantum Parallelism:
  A classical bit is definitively 0 or 1 — like a coin lying flat showing heads or tails. A qubit in superposition is in a combination of both states simultaneously, described by probability amplitudes (complex numbers). This is not the same as a hidden coin — the qubit is genuinely in both states at once, a fact confirmed by over a century of quantum experiments. When you have N qubits in superposition, they collectively represent 2^N states simultaneously. With just 300 qubits, you represent more states than there are atoms in the observable universe. This exponential scaling is the source of quantum computing's power — and its fragility.

• Entanglement and Quantum Algorithms:
  Entanglement links qubits so that the state of one depends on the state of another, regardless of physical distance. Quantum algorithms like Shor's (for factoring large numbers) and Grover's (for searching databases) exploit entanglement to correlate computations across qubits in ways that have no classical analog. Shor's algorithm can factor a 2048-bit number exponentially faster than any known classical algorithm — which would break RSA encryption, the foundation of internet security. This has motivated billions in quantum computing investment and a parallel race to develop quantum-resistant cryptography.

• The Decoherence Challenge:
  Quantum states are extraordinarily fragile. Any interaction with the environment — thermal photons, electromagnetic radiation, mechanical vibrations, even cosmic rays — causes decoherence, collapsing the superposition into a classical state. Superconducting qubits must be cooled to 15 millikelvin (0.015 Kelvin) — colder than interstellar space — inside dilution refrigerators that weigh thousands of kilograms. Even at these temperatures, coherence times are measured in microseconds to milliseconds. Every quantum computation is a race against decoherence: the algorithm must complete before the quantum state dissolves.

• The Path to Fault Tolerance:
  Current quantum computers are in the 'noisy intermediate-scale quantum' (NISQ) era — hundreds to thousands of physical qubits with error rates around 0.1-1% per gate. Fault-tolerant quantum computing requires error correction codes that encode one protected logical qubit across many physical qubits. The leading approach, the surface code, requires roughly 1,000-10,000 physical qubits per logical qubit at current error rates. This means a fault-tolerant quantum computer solving useful problems might need millions of physical qubits. IBM, Google, Microsoft, and dozens of startups are racing toward this threshold, with IBM targeting 100,000 qubits by 2033 and Google demonstrating key error correction milestones in 2024.

COMMON MISCONCEPTIONS:
• "Quantum computers are just faster versions of regular computers"
  Reality: Quantum computers are not faster classical computers — they are a fundamentally different kind of computing machine. A classical computer processes bits sequentially or in limited parallelism. A quantum computer exploits superposition and entanglement to explore exponentially many computational paths simultaneously through quantum interference. For most everyday tasks (email, web browsing, spreadsheets), quantum computers offer no advantage at all. Their power is specific to problems with mathematical structures that allow quantum algorithms to amplify correct answers.
  Strategy: Analogy: A submarine is not a faster car — it operates in a completely different medium. Similarly, a quantum computer operates in the medium of quantum mechanics, which gives it power in some domains but is useless in others. Ask students: Would you use a submarine to drive to school?

• "Qubits are just bits that can be 0 and 1 at the same time like flipping a coin"
  Reality: The coin analogy is deeply misleading. A flipped coin in the air is in a DEFINITE state — it is just unknown. A qubit in superposition is genuinely in BOTH states simultaneously, described by complex probability amplitudes. This is not a metaphor or simplification — it is experimentally verified quantum mechanics. The qubit's state is a vector in a two-dimensional complex space (the Bloch sphere), and quantum algorithms manipulate these vectors through rotations and entanglement to produce interference patterns that amplify correct answers.
  Strategy: Demonstration: Use the Bloch sphere visualization from the model. A coin has two states (heads, tails). A qubit has an infinite continuum of states on the surface of the Bloch sphere, each representing a different superposition of 0 and 1 with different complex amplitudes.

• "We will have powerful quantum computers within a few years that replace all classical computers"
  Reality: The timeline to practically useful quantum computers is measured in decades for most applications, and quantum computers will NEVER replace classical computers for general computing. Current quantum hardware has roughly 1,000 noisy qubits. Fault-tolerant quantum computing for transformative applications like molecular simulation requires millions of high-quality qubits. IBM projects 100,000 qubits by 2033, and million-qubit systems may arrive in the 2030s-2040s. Even then, quantum computers will be specialized accelerators for specific problem types, not general-purpose replacements for laptops and phones.
  Strategy: Timeline exercise: Plot the trajectory from today's 1,000 qubits to the millions needed for transformative applications. At current scaling rates, when does the model predict we cross each threshold? What assumptions could make this faster or slower?

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
Big Question: Why would a computer built on the strangest rules in physics solve problems that every supercomputer on Earth combined could never crack?
Answer: A quantum computer exploits superposition and entanglement to explore exponentially many computational paths simultaneously — something classical bits physically cannot do. But this quantum advantage is unimaginably fragile. Qubits lose their quantum properties within microseconds from the slightest environmental disturbance: a stray photon, a thermal vibration, even a cosmic ray. Every quantum gate operation introduces errors that compound across the circuit. Error correction requires roughly 1,000 physical qubits to protect each logical qubit, creating a resource paradox. The breakthrough will come not from building more qubits but from building quieter, more stable, and more precise qubits that maintain coherence long enough to complete useful computations — and we are approaching that threshold now.

Simulation Answers:
• Current State-of-the-Art Scenario: With 1,000 qubits, 100 microsecond coherence, and 0.3% gate error rate, the model shows limited quantum volume. The 0.3% error rate means that after approximately 300 gate operations, the probability of an error-free computation drops below 50%. Coherence time limits circuits to operations completable within 100 microseconds. The result: current hardware can demonstrate quantum effects and run small proof-of-concept algorithms, but cannot achieve practical quantum advantage for real-world problems. Most computations are faster on classical hardware because quantum error rates consume the speedup.
• Error-Corrected Regime Scenario: With 10,000 qubits, 0.01% gate error, and 10 ms coherence, the model shows a dramatic transition. The improved error rate allows circuits of thousands of gates before corruption. The extended coherence time permits complex multi-step algorithms. With 10,000 physical qubits, approximately 10-50 logical qubits can be error-corrected using the surface code. This is sufficient for transformative applications like molecular simulation for drug discovery or optimization problems intractable classically. The model reveals a threshold effect: below certain error rates, quantum advantage suddenly emerges rather than gradually appearing.

Reflection Exemplars:
• Q: Why is the error correction overhead so devastating to near-term quantum computing?
  A: The surface code, the leading error correction approach, requires roughly 1,000 physical qubits to protect each logical qubit at current error rates. This means a quantum computer with 1,000 physical qubits can protect exactly ONE logical qubit — barely enough to store a single quantum bit of information, let alone compute. To run Shor's algorithm to break RSA-2048 encryption requires approximately 4,000 logical qubits, which translates to roughly 4 million physical qubits. Current hardware has about 1,000 qubits. The model clearly shows that the gap between available and required resources is the central bottleneck.
• Q: Why is quantum advantage problem-specific rather than universal?
  A: Quantum computers gain their advantage from superposition and entanglement, which allow certain algorithms to explore exponentially many paths simultaneously. But this advantage only applies to problems with specific mathematical structures — those that can be formulated so that quantum interference amplifies correct answers and cancels incorrect ones. Most everyday computing tasks like word processing, web browsing, and video rendering do not have this structure. The model shows that quantum volume and classical computing speed are measuring different capabilities — quantum computers are not faster classical computers but a different kind of computer, like how a submarine is not a faster car but a vehicle for a different medium.

STEM CHALLENGE GUIDANCE:
Title: Design a Quantum Computing Application Proposal
Mission: Identify a real-world problem where quantum computing could provide transformative advantage over classical methods and design a proposal specifying the quantum resources needed, the expected speedup, and the timeline for feasibility.
Scenario: A technology investment firm wants to identify the most promising near-term applications for quantum computing. Your team must select a specific problem domain — drug discovery, materials science, logistics optimization, cryptography, or climate modeling — and design a proposal that quantifies the quantum resources needed, estimates when hardware will be sufficient, and calculates the economic value of solving this problem faster than classical computers can.
Introduction: Present the challenge: A technology investment firm needs your team to identify the most promising near-term application for quantum computing and build a quantitative case for investment. You must select a specific problem domain, specify the quantum resources required, estimate when hardware will be sufficient, and calculate the economic return. Use your model data to justify every claim.

Key Concepts:
• Quantum Speedup Classes: Different problems receive different levels of quantum speedup: exponential speedup (like Shor's factoring algorithm, which makes the problem tractably fast), polynomial speedup (like Grover's search, which provides a square-root improvement), and no speedup (problems with no known quantum advantage). The value proposition depends entirely on which class your target problem falls into.
• NISQ vs. Fault-Tolerant Applications: Near-term NISQ (noisy intermediate-scale quantum) applications like variational quantum eigensolvers can run on current hardware but provide modest advantages. Fault-tolerant applications like full molecular simulation require millions of qubits but would be transformative. The investment timeline depends on which category you target.
• Quantum-Classical Hybrid Computing: Most practical quantum applications will combine quantum and classical processing — quantum processors handle the exponentially hard subroutines while classical computers manage everything else. Understanding where to split the computation between quantum and classical resources is a key design challenge.

Evaluation Rubric:
• Expert (4): Proposal identifies a specific computational bottleneck, specifies qubit count and fidelity requirements with model evidence, estimates a realistic hardware readiness timeline, quantifies economic value, and addresses the quantum-classical boundary
• Proficient (3): Proposal selects a problem domain with justification, provides approximate resource requirements from model data, and estimates feasibility timeline
• Developing (2): Proposal identifies a problem but lacks quantitative resource estimates or provides unrealistic hardware timelines
• Beginning (1): Proposal is vague, does not reference model data, or targets a problem without known quantum advantage

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a comparison table showing classical versus quantum resource scaling for different problem types: factoring, simulation, search, and optimization
  • Use a timeline visualization showing current hardware capabilities, projected improvements, and the threshold line for different applications
  • Sentence frames: 'Our application requires __ logical qubits because __, which translates to approximately __ physical qubits at current error rates, which we predict will be available by __'

Extensions (Advanced Learners):
  • Research the difference between superconducting qubits (IBM, Google), trapped ion qubits (IonQ, Quantinuum), and photonic qubits (PsiQuantum) — analyze which technology is best suited for different applications based on your model parameters
  • Investigate quantum-resistant cryptography standards (NIST post-quantum cryptography) and analyze what happens to internet security when large-scale quantum computers arrive before new encryption standards are fully deployed
  • Design a quantum computing curriculum for high school students — what concepts must be taught first, and how do you explain superposition without the misleading coin-flip analogy?

Cross-Curricular Connections:
  • Math: If a quantum computer with N qubits can represent 2^N states simultaneously, calculate how many states 50, 100, 200, and 300 qubits represent. Compare 2^300 to the estimated number of atoms in the observable universe (approximately 10^80). What does this scaling imply about quantum computing potential?
  • ELA: Write a policy brief for Congress explaining why the United States should or should not invest $10 billion in quantum computing research over the next decade. Address national security implications of quantum cryptography breaking, economic competitiveness with China, and the uncertainty of technological timelines.
  • History: Research the history of quantum mechanics from Planck's 1900 blackbody radiation to the 2022 Nobel Prize in Physics for entanglement experiments. How did a theory that scientists struggled to accept for decades become the foundation of a computing revolution?

CAST ALIGNMENT:
• Model how qubit count, coherence time, and gate error rate interact to determine quantum computational volume and advantage
• Analyze the resource paradox of quantum error correction where protecting information requires orders of magnitude more hardware than processing it
• Predict the hardware thresholds at which quantum advantage becomes achievable for specific real-world problem classes

CAST-Style Assessment Questions:
• Multiple Choice: A quantum processor has 100 qubits with a gate error rate of 0.5%. After applying 200 sequential gate operations, what is the approximate probability that the computation is error-free, and what does this imply about circuit depth limitations?
• Constructed Response: Using evidence from your model, explain why adding more qubits to a quantum computer does not automatically make it more powerful. Describe the relationship between qubit count, error rate, and coherence time, and explain why quantum volume is a better metric than qubit count alone.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: The Quantum Computing Revolution
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. What is the difference between a classical bit (0 or 1) and a quantum bit (qubit), and why does that difference matter for computing?

   _________________________________________________________

   _________________________________________________________

2. Why do you think quantum computers need to be cooled to nearly absolute zero to function?

   _________________________________________________________

   _________________________________________________________

3. Draw a diagram showing how you think a quantum computer processes information differently from a regular computer.

   [DRAWING BOX]

4. What types of problems do you think quantum computers could solve that regular computers cannot?

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
___ Quantum Error Correction      

A. A quantum bit that can exist in a superposition of 0 and 1 simultaneously — while a classical bit is always one or the other, a qubit occupies both states with different probability amplitudes until measured, enabling quantum parallelism across exponentially many states
B. The quantum mechanical principle that a particle can exist in multiple states simultaneously — for qubits, this means being in a combination of 0 and 1 described by complex probability amplitudes, not simply being in an unknown state like a hidden coin
C. A quantum correlation between particles where measuring one instantly determines the state of the other regardless of distance — Einstein called it 'spooky action at a distance' — it enables quantum algorithms to coordinate computations across qubits in ways impossible classically
D. The process by which a qubit's fragile quantum state is destroyed through interaction with the environment — thermal vibrations, electromagnetic noise, and even cosmic rays can collapse superposition, erasing the quantum advantage and leaving only classical noise
E. A set of techniques that protect quantum information by encoding one logical qubit across many physical qubits — because quantum states cannot be copied or directly observed without destroying them, error correction requires fundamentally different approaches than classical computing

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

SCENARIO: Current State-of-the-Art
Settings: 1,000 qubits, 100 microsecond coherence, 0.3% gate error rate
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Error-Corrected Regime
Settings: 10,000 qubits, 0.01% gate error, 10 ms coherence time
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Thermal Disruption
Settings: Operating temperature increases from 15 mK to 100 mK
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

1. How does your model demonstrate the exponential scaling of quantum computational power versus the exponential scaling of errors?

   _________________________________________________________

   _________________________________________________________

2. Why is the error correction overhead such a critical barrier to practical quantum computing?

   _________________________________________________________

   _________________________________________________________

3. What does your model reveal about the relationship between operating temperature and every other quantum parameter?

   _________________________________________________________

   _________________________________________________________

4. How would your model change if a room-temperature quantum computing technology were developed?

   _________________________________________________________

   _________________________________________________________

5. What are the limitations of modeling quantum advantage when the problems quantum computers solve best are the ones classical computers cannot verify?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Why would a computer built on the strangest rules in physics solve problems that every supercomputer on Earth combined could never crack? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Using Mathematics and Computational Thinking
   □ Disciplinary Core Idea: PS4.A Wave Properties / PS4.B Electromagnetic Radiation
   □ Crosscutting Concept: Scale, Proportion, and Quantity

3. What are the limitations of modeling quantum advantage when the problems quantum computers solve best are the ones classical computers cannot verify?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Quantum Computing Application Proposal
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Identify a real-world problem where quantum computing could provide transformative advantage over classical methods and design a proposal specifying the quantum resources needed, the expected speedup, and the timeline for feasibility.

SCENARIO: A technology investment firm wants to identify the most promising near-term applications for quantum computing. Your team must select a specific problem domain — drug discovery, materials science, logistics optimization, cryptography, or climate modeling — and design a proposal that quantifies the quantum resources needed, estimates when hardware will be sufficient, and calculates the economic value of solving this problem faster than classical computers can.

GUIDING QUESTIONS:
• What specific computational bottleneck in your chosen domain makes classical computers inadequate?
• How many logical qubits would your application require, and how does that translate to physical qubits given current error rates?
• When do you estimate quantum hardware will reach the threshold needed for your application based on current improvement trends?

DESIGN THINKING:
• What quantum algorithm would your application use and why is it faster than the best classical alternative?

  _________________________________________________________

• What are the minimum qubit count, coherence time, and gate fidelity requirements for your application?

  _________________________________________________________

• How would you verify that the quantum computer produced a correct answer for a problem too hard for classical verification?

  _________________________________________________________

• What is the estimated economic value of solving this problem with quantum advantage versus waiting for classical hardware improvements?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Proposal identifies a specific computational bottleneck, specifies qubit count and fidelity requirements with model evidence, estimates a realistic hardware readiness timeline, quantifies economic value, and addresses the quantum-classical boundary
• Proficient (3): Proposal selects a problem domain with justification, provides approximate resource requirements from model data, and estimates feasibility timeline
• Developing (2): Proposal identifies a problem but lacks quantitative resource estimates or provides unrealistic hardware timelines
• Beginning (1): Proposal is vague, does not reference model data, or targets a problem without known quantum advantage

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CAST-Aligned Pre/Post Assessment

### Administration Instructions

These 5 multiple-choice questions are administered identically as both a pre-assessment (before Activity 1) and a post-assessment (after Activity 4). Score each out of 5. Learning growth = post-score minus pre-score.

Questions follow the California Science Test (CAST) stimulus-response format. Each item is three-dimensional, assessing a Science and Engineering Practice (SEP), Disciplinary Core Idea (DCI), and Crosscutting Concept (CCC) simultaneously, aligned to HS-PS4-3, HS-PS4-5.

---

### Pre-Assessment Questions

### Question 1

A qubit differs from a classical bit because a qubit can exist in superposition. What does this mean for computational processing?

A. A qubit processes information twice as fast as a classical bit
B. A qubit can represent both 0 and 1 simultaneously with different probability amplitudes, enabling quantum parallelism
C. A qubit stores two classical bits of information in the same physical space
D. A qubit switches between 0 and 1 faster than a classical bit

Correct Answer: B

Feedback: Correct. Superposition allows a qubit to exist in a combination of 0 and 1 states simultaneously, described by probability amplitudes. This enables quantum algorithms to explore many solutions in parallel. Superposition is not about speed or storage size. A qubit occupies both 0 and 1 states simultaneously with different probability amplitudes until measured. This allows quantum algorithms to process exponentially many states in parallel.

---

### Question 2

Superconducting qubits must be cooled to approximately 15 millikelvin, colder than outer space. What is the primary reason for this extreme cooling requirement?

A. Superconducting materials only become conductive at very low temperatures
B. Thermal energy at higher temperatures destroys the fragile quantum superposition states that enable quantum computation
C. The cooling system generates the magnetic fields needed for qubit operations
D. Low temperatures increase the physical size of qubits, making them easier to manufacture

Correct Answer: B

Feedback: Correct. Even tiny amounts of thermal energy cause decoherence, destroying the quantum superposition that gives qubits their computational advantage. Extreme cooling minimizes this environmental interference. The primary reason is decoherence. Thermal vibrations, even at millikelvin scales, can destroy the quantum superposition states. Extreme cooling minimizes thermal noise so qubits maintain their quantum properties long enough to complete calculations.

---

### Question 3

Why is quantum error correction fundamentally different from classical error correction?

A. Quantum systems do not experience errors during computation
B. Classical errors can be detected by copying the data and comparing, but quantum states cannot be copied without destroying them
C. Quantum error correction requires fewer resources than classical error correction
D. Classical computers use parity bits while quantum computers use standard checksums

Correct Answer: B

Feedback: Correct. The no-cloning theorem prevents copying quantum states, so error correction must use fundamentally different strategies, such as encoding one logical qubit across many physical qubits to detect and correct errors indirectly. The core difference is that quantum states cannot be copied or directly measured without destroying them (the no-cloning theorem). Classical error correction relies on copying data to detect errors, but quantum error correction must encode information redundantly across many physical qubits.

---

### Question 4

A quantum computer with 50 qubits can theoretically represent 2^50 states simultaneously. Why doesn't this automatically make it faster than a classical supercomputer for all problems?

A. 50 qubits cannot store enough data for complex problems
B. Quantum advantage only exists for specific problem types where quantum algorithms exploit interference and entanglement; many problems have no known quantum speedup
C. Classical supercomputers always run faster because they operate at room temperature
D. The 2^50 states are all identical and provide no computational diversity

Correct Answer: B

Feedback: Correct. Quantum advantage is problem-specific. Only certain problems, such as factoring, optimization, and quantum simulation, have quantum algorithms that are provably faster. For many everyday computations, classical computers are equally or more efficient. Quantum speedup is not universal. It requires quantum algorithms that exploit superposition, entanglement, and interference for specific problem structures. Many computational tasks have no known quantum advantage.

---

### Question 5

Decoherence sets a time limit on quantum computation. Which statement best describes the engineering challenge this creates?

A. All quantum computations must complete before qubits lose their quantum states, but error correction to extend this time requires additional qubits and gate operations that themselves introduce errors
B. Decoherence can be completely eliminated by using better materials
C. Decoherence only affects the final measurement step, not the computation itself
D. Longer computations produce more accurate results because qubits stabilize over time

Correct Answer: A

Feedback: Correct. This is the central paradox: decoherence limits computation time, but error correction (the solution) consumes the very qubits and gate operations that decoherence is degrading, creating a challenging resource trade-off. Decoherence creates a countdown clock. The solution, quantum error correction, requires more qubits and more gates, which themselves are imperfect and consume limited resources. This creates a paradox where the cure for errors consumes the resources errors are destroying.

---

### Post-Assessment Questions

### Question 1

A student's quantum computing model shows that increasing qubit count from 50 to 100 doubles the potential computational power but increases the gate error rate from 0.5% to 0.8% per operation. For a 1,000-gate circuit, what is the most accurate analysis of this trade-off?

A. The increased qubit count will always outweigh the higher error rate
B. At 0.8% error per gate across 1,000 gates, the cumulative error probability approaches certainty, meaning the additional qubits provide no usable computational advantage without improved error correction
C. The error rate increase is negligible because individual gate errors do not compound
D. Reducing the circuit to 100 gates would eliminate all errors

Correct Answer: B

Feedback: Correct. Compound error probability across 1,000 gates at 0.8% per gate means the probability of zero errors is approximately (0.992)^1000, which is vanishingly small. More qubits are useless if the computation is drowned in errors. Gate errors compound across circuit depth. At 0.8% per gate over 1,000 gates, the probability that the entire circuit executes correctly is (0.992)^1000, which is extremely small. The additional qubits cannot overcome this error accumulation without better error correction.

---

### Question 2

The model demonstrates that quantum volume, not raw qubit count, determines actual computational capability. Which combination of improvements would most effectively increase quantum volume?

A. Doubling qubit count while keeping all other parameters the same
B. Simultaneously improving gate fidelity, coherence time, and qubit connectivity while modestly increasing qubit count
C. Maximizing qubit count and accepting higher error rates as a necessary trade-off
D. Reducing operating temperature from 15 millikelvin to 10 millikelvin without any other changes

Correct Answer: B

Feedback: Correct. Quantum volume is a holistic metric. Increasing qubit count without improving gate fidelity, coherence, and connectivity produces an unusable system. Balanced improvement across all parameters yields the greatest gain in actual computational capability. Quantum volume combines qubit count, gate fidelity, coherence time, and connectivity into a single metric. Improving one dimension alone, especially qubit count, without improving others provides minimal real-world computational gain.

---

### Question 3

A simulation shows that a quantum algorithm solves an optimization problem in 10 seconds that would take a classical computer 10,000 years. A student claims this proves quantum computers are universally superior. Which response best evaluates this claim?

A. The claim is correct because the speedup factor is enormous
B. The claim is incorrect because the comparison only demonstrates quantum advantage for that specific problem class; quantum computers may offer no speedup for sorting, databases, or many other computational tasks
C. The claim is incorrect because classical computers will eventually match quantum speed through hardware improvements
D. The claim is correct because all NP-hard problems can be solved faster on quantum computers

Correct Answer: B

Feedback: Correct. Quantum advantage is problem-specific. Exponential speedups exist for certain problem classes (factoring, certain optimizations, quantum simulation) but not for general-purpose computing. The dramatic speedup in one domain does not generalize. Quantum advantage is domain-specific. Some problems have provable quantum speedups, but many do not. Quantum computers are not universally faster; they exploit specific mathematical structures that only some problems possess.

---

### Question 4

In the model, a student notices that entanglement fidelity drops from 99.5% to 97% when the system scales from 20 to 80 qubits. What is the most significant consequence of this degradation for quantum algorithms?

A. The system will consume 2.5% more electricity
B. Algorithms that depend on entanglement to coordinate multi-qubit operations will produce increasingly unreliable results, potentially making the larger system less capable than the smaller one for entanglement-dependent computations
C. Individual qubit performance improves to compensate for lower fidelity
D. The system can still execute all quantum algorithms with minor output adjustments

Correct Answer: B

Feedback: Correct. Many quantum algorithms rely on high-fidelity entanglement. A drop from 99.5% to 97% compounds across operations, and for algorithms requiring extensive entanglement, the larger system may produce worse results than the smaller, higher-fidelity one. Entanglement fidelity drops compound across multi-qubit operations. For algorithms heavily dependent on entanglement, the error accumulation in the 80-qubit system could make it effectively less capable than the 20-qubit system despite having four times more qubits.

---

### Question 5

Based on the quantum computing model, which conclusion about the relationship between coherence time and circuit depth is best supported by the simulation data?

A. Coherence time and circuit depth are independent variables with no relationship
B. Coherence time sets an absolute ceiling on circuit depth because all gate operations must complete before quantum states decohere, making coherence time the fundamental bottleneck that limits the complexity of solvable problems
C. Longer circuits always produce more accurate results regardless of coherence time
D. Circuit depth can exceed coherence time limits by using faster gate operations without any trade-offs

Correct Answer: B

Feedback: Correct. Coherence time is the fundamental constraint. Every gate operation takes time, and the total circuit must complete before decoherence destroys the quantum state. This makes coherence time the ultimate limit on computational depth and problem complexity. Coherence time acts as a hard deadline. Since each gate operation consumes time, the maximum circuit depth equals coherence time divided by gate time. This ceiling limits which problems quantum computers can solve, making coherence time the foundational constraint.

---

### Answer Key

**Pre-Assessment:**
Question 1: B
Question 2: B
Question 3: B
Question 4: B
Question 5: A

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
| Activity Pack (DOCX) | [materials/grade-11/G11L3-L02/G11L3-L02-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-11/G11L3-L02/G11L3-L02-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-11/G11L3-L02/G11L3-L02-Student-Presentation.pptx] |
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