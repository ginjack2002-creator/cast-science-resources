# Lesson: How Do Noise-Canceling Headphones Work?

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G11L1-L08 |
| **Grade** | 11th Grade — Level 1: Foundations of Complex Systems |
| **Lesson Name** | How Do Noise-Canceling Headphones Work? |
| **Status** | Template |

---

## Platform

### Title
**How Do Noise-Canceling Headphones Work? — Modeling Wave Superposition and Destructive Interference**

### Overview
Noise-canceling headphones represent one of the most elegant applications of wave physics in consumer technology. The concept seems paradoxical — how can adding more sound make things quieter? The answer lies in the mathematical principle of superposition, which governs how all waves interact. Understanding noise cancellation means understanding the fundamental nature of waves themselves. Students investigate the driving question: How can adding more sound to your ears actually make everything quieter — and what does this tell us about the hidden mathematical nature of waves? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of a pair of premium noise-canceling headphones with visible sound wave visualizations showing incoming noise waves being canceled by anti-phase waves, dramatic dark background with blue and orange wave graphics, editorial quality]

### Grade
11th Grade — Level 1: Foundations of Complex Systems

### NGSS Standard
**HS-PS4-1, HS-PS4-5**: Use mathematical representations to support a claim regarding relationships among the frequency, wavelength, and speed of waves traveling in various media. Communicate technical information about how some technological devices use the principles of wave behavior to function.

### Learning Objectives
- Model how noise-canceling headphones use destructive interference to eliminate unwanted sound by generating anti-phase waves
- Explain the relationship between wave frequency, wavelength, amplitude, and the conditions required for complete destructive interference
- Predict the effectiveness of noise cancellation across different frequency ranges and environmental noise conditions
- Analyze why active noise cancellation works better for low-frequency sounds than high-frequency sounds

### Component List (Starting Model: 5 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Ambient Noise Frequency | External | The frequency of the environmental sound to be canceled, measured in Hertz — low-frequency rumbles (airplane engines at 80-200 Hz, traffic at 100-500 Hz) are easier to cancel than high-frequency sounds (conversation at 300-3,000 Hz, birdsong at 2,000-8,000 Hz) |
| Ambient Noise Amplitude | External | The loudness of the environmental noise, measured in decibels — louder noise requires a stronger anti-phase signal for complete cancellation |
| Processing Speed | Internal | How quickly the headphone's microphone-processor-speaker system can sample incoming noise, compute the anti-phase signal, and output it — measured in microseconds. Faster processing enables cancellation of higher-frequency sounds |
| Phase Accuracy | Internal | How precisely the anti-phase signal aligns with the incoming noise wave — even a small phase error reduces cancellation effectiveness. Perfect cancellation requires exact 180-degree phase offset at every frequency |
| Cancellation Effectiveness | Internal | The percentage of ambient noise amplitude that is eliminated by destructive interference, measured as noise reduction in decibels — top-tier headphones achieve 20-30 dB reduction at low frequencies |

### Research for Lesson
- The Physics of Sound Waves — reference materials and textbook resources
- Superposition and Interference — reference materials and textbook resources
- How Active Noise Cancellation Works — reference materials and textbook resources
- Passive Plus Active: The Complete System — reference materials and textbook resources

---

## Step 1: LOCATE — Build Your System

### Text Editor

```
HOW DO NOISE-CANCELING HEADPHONES WORK?

Modeling Wave Superposition and Destructive Interference.
How can adding more sound to your ears actually make everything quieter — and what does this tell us about the hidden mathematical nature of waves?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Ambient Noise Frequency" — the frequency of the environmental sound to be canceled
  ○ Click "Ambient Noise Amplitude" — the loudness of the environmental noise
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Processing Speed" — how quickly the headphone's microphone-processor-speaker system can sample incoming noise
  ○ Click "Phase Accuracy" — how precisely the anti-phase signal aligns with the incoming noise wave — even a small phase error reduces cancellation effectiveness
  ○ Click "Cancellation Effectiveness" — the percentage of ambient noise amplitude that is eliminated by destructive interference

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
"How can adding more sound to your ears actually make everything quieter — and what does this tell us about the hidden mathematical nature of waves?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Ambient Noise Frequency' — that's external. The frequency of the environmental sound to be canceled.
Click on 'Ambient Noise Amplitude' — that's external. The loudness of the environmental noise.
Click on 'Processing Speed' — that's internal. How quickly the headphone's microphone-processor-speaker system can sample incoming noise, compute the anti-phase signal, and output it — measured in microseconds.
Click on 'Phase Accuracy' — that's internal. How precisely the anti-phase signal aligns with the incoming noise wave — even a small phase error reduces cancellation effectiveness.
Click on 'Cancellation Effectiveness' — that's internal. The percentage of ambient noise amplitude that is eliminated by destructive interference.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Ambient Noise Frequency and Ambient Noise Amplitude are external components because they are properties of the environment that the headphone system must respond to — they cannot be controlled by the technology. Processing Speed, Phase Accuracy, and Cancellation Effectiveness are internal components because they are determined by the headphone's hardware capabilities and the physics of wave interference — Processing Speed is a fixed property of the DSP chip, Phase Accuracy depends on the interaction of processing speed with wavelength, and Cancellation Effectiveness is the outcome of superposition between the noise and anti-phase waves.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next step, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 5 components sorted: Ambient Noise Frequency, Ambient Noise Amplitude (External), Processing Speed, Phase Accuracy, Cancellation Effectiveness (Internal)]

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
• Click on "Ambient Noise Frequency" and drag an arrow to "Phase Accuracy"
• Click on "Phase Accuracy" and drag an arrow to "Cancellation Effectiveness"
• Click on "Processing Speed" and drag an arrow to "Phase Accuracy"

Task C: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Ambient Noise Frequency → Phase Accuracy = NEGATIVE (−)
    Higher noise frequency means shorter wavelength, which means the same processing delay causes a larger percentage phase error. At 100 Hz (wavelength 3.43m), a 10μs delay causes 0.36° error; at 4,000 Hz (wavelength 8.6cm), the same delay causes 14.4° error. Higher frequency makes phase accuracy harder to achieve.

  ○ Phase Accuracy → Cancellation Effectiveness = POSITIVE (+)
    More precise phase alignment produces better cancellation. Perfect 180° offset gives complete cancellation (theoretically infinite dB reduction). A 10° error reduces cancellation by about 1.5 dB; a 30° error reduces it by about 7 dB. Cancellation effectiveness degrades rapidly as phase accuracy worsens.

  ○ Processing Speed → Phase Accuracy = POSITIVE (+)
    Faster processing (lower latency from microphone to speaker) reduces the time delay that causes phase error. Halving the processing time halves the phase error at any given frequency. Faster processors allow effective cancellation at higher frequencies.

Task D: CHECK YOUR MODEL
• You should have 3 arrows total
• 1 negative relationship(s), 2 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: If the anti-phase signal is even slightly off — 175 degrees instead of 180 degrees — the cancellation is incomplete and you hear residual noise. At low frequencies (long wavelengths), a tiny timing error represents a small fraction of the wavelength. At high frequencies (short wavelengths), the same timing error represents a LARGE fraction of the wavelength. Why does this make high frequencies harder to cancel?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Ambient Noise Frequency' and drag an arrow
over to 'Phase Accuracy.'

Here's the key question: When ambient noise frequency goes UP, does
phase accuracy go UP or DOWN?

Higher noise frequency means shorter wavelength, which means the same processing delay causes a larger percentage phase error. At 100 Hz (wavelength 3.43m), a 10μs delay causes 0.36° error; at 4,000 Hz (wavelength 8.6cm), the same delay causes 14.4° error. Higher frequency makes phase accuracy harder to achieve.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Next connection: Click on 'Phase Accuracy' and drag an arrow
over to 'Cancellation Effectiveness.'

Here's the key question: When phase accuracy goes UP, does
cancellation effectiveness go UP or DOWN?

More precise phase alignment produces better cancellation. Perfect 180° offset gives complete cancellation (theoretically infinite dB reduction). A 10° error reduces cancellation by about 1.5 dB; a 30° error reduces it by about 7 dB. Cancellation effectiveness degrades rapidly as phase accuracy worsens.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'Processing Speed' and drag an arrow
over to 'Phase Accuracy.'

Here's the key question: When processing speed goes UP, does
phase accuracy go UP or DOWN?

Faster processing (lower latency from microphone to speaker) reduces the time delay that causes phase error. Halving the processing time halves the phase error at any given frequency. Faster processors allow effective cancellation at higher frequencies.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Look at your model now. You've got 1 negative and 2
positive relationships. 3 arrows total.

If the anti-phase signal is even slightly off — 175 degrees instead of 180 degrees — the cancellation is incomplete and you hear residual noise. At low frequencies (long wavelengths), a tiny timing error represents a small fraction of the wavelength. At high frequencies (short wavelengths), the same timing error represents a LARGE fraction of the wavelength. Why does this make high frequencies harder to cancel?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Ambient Noise Frequency −→ Phase Accuracy, Phase Accuracy +→ Cancellation Effectiveness, Processing Speed +→ Phase Accuracy]

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
• When Ambient Noise Frequency is HIGH, what happens to the internal components?

Task C: SCENARIO — LOW-FREQUENCY CANCELLATION
• Noise: 100 Hz sine wave at 80 dB | ANC: Active
• PREDICT FIRST: How many decibels of noise reduction do you predict at 100 Hz? Will the cancellation be nearly perfect or partial?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task D: SCENARIO — HIGH-FREQUENCY CHALLENGE
• Noise: 4,000 Hz sine wave at 70 dB | ANC: Active
• PREDICT FIRST: Do you predict noise cancellation will be as effective at 4,000 Hz as at 100 Hz? Why or why not?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task E: SCENARIO — MIXED ENVIRONMENT
• Noise: Airplane cabin spectrum (multiple frequencies) | ANC: Active
• PREDICT FIRST: In a real airplane cabin with noise at many frequencies simultaneously, which frequency components do you predict will be canceled most effectively?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Active noise cancellation works by exploiting the principle of superposition — the anti-phase signal doesn't 'absorb' or 'block' sound, it literally adds an equal-and-opposite wave that sums to zero through destructive interference
• Low-frequency noise (below 1,000 Hz) is canceled very effectively because long wavelengths are tolerant of small phase errors — the processing system has more time to compute the anti-phase signal accurately
• High-frequency noise is much harder to cancel because short wavelengths require microsecond-level phase accuracy — even tiny processing delays cause significant phase errors at high frequencies, reducing cancellation effectiveness
• Real noise-canceling headphones combine active cancellation (for low frequencies) with passive isolation (physical ear cup padding that blocks high frequencies) to achieve broad-spectrum noise reduction

THE ANSWER: Noise-canceling headphones work by adding sound to your ears, not blocking it — specifically, they generate an 'anti-noise' wave that is the exact mathematical inverse of the incoming noise. A microphone on the outside of the headphone captures ambient sound. A processor analyzes the wave's frequency and amplitude in real-time and generates an anti-phase signal — the same wave shape shifted by exactly 180 degrees (half a wavelength). When this anti-phase signal is played through the headphone speaker at the same time the original noise arrives at your ear, superposition occurs: the positive pressure peaks of the noise align with the negative pressure troughs of the anti-noise, and they cancel each other to produce silence. This works brilliantly for low-frequency sounds like engine rumble because the long wavelengths are forgiving of small timing errors. It works poorly for high-frequency sounds like voices because the short wavelengths demand impossibly precise phase alignment. That's why your noise-canceling headphones silence the airplane engine but not the person talking next to you.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Low-Frequency Cancellation. Noise: 100 Hz sine wave at 80 dB | ANC: Active.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: High-Frequency Challenge.
Noise: 4,000 Hz sine wave at 70 dB | ANC: Active.

Before you run it — make a prediction. Do you predict noise cancellation will be as effective at 4,000 Hz as at 100 Hz? Why or why not?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Mixed Environment. Noise: Airplane cabin spectrum (multiple frequencies) | ANC: Active.
In a real airplane cabin with noise at many frequencies simultaneously, which frequency components do you predict will be canceled most effectively?

Here's what our model reveals: Noise-canceling headphones work by adding sound to your ears, not blocking it — specifically, they generate an 'anti-noise' wave that is the exact mathematical inverse of the incoming noise. A microphone on the outside of the headphone captures ambient sound. A processor analyzes the wave's frequency and amplitude in real-time and generates an anti-phase signal — the same wave shape shifted by exactly 180 degrees (half a wavelength). When this anti-phase signal is played through the headphone speaker at the same time the original noise arrives at your ear, superposition occurs: the positive pressure peaks of the noise align with the negative pressure troughs of the anti-noise, and they cancel each other to produce silence. This works brilliantly for low-frequency sounds like engine rumble because the long wavelengths are forgiving of small timing errors. It works poorly for high-frequency sounds like voices because the short wavelengths demand impossibly precise phase alignment. That's why your noise-canceling headphones silence the airplane engine but not the person talking next to you.

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
   • What happens if you turn OFF Ambient Noise Frequency?
   • What happens if you turn OFF Ambient Noise Amplitude?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Feedback vs. Feedforward Architecture — Two approaches to ANC microphone placement: feedforward places the mic outside the ear cup (sensing noise before it arrives) while feedback places it inside (sensing the combined result). Each has trade-offs in latency, accuracy, and frequency range
   • Ear Seal Quality — The physical fit and acoustic seal between the headphone ear cup and the wearer's head — passive isolation from the physical seal blocks 10-25 dB of high-frequency noise that active cancellation struggles with, making passive and active noise reduction complementary
   • Adaptive Algorithm — Machine learning algorithms that learn the acoustic characteristics of common noise environments (airplane, train, office) and pre-load optimized anti-phase profiles, reducing the processing time needed for real-time cancellation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • The Physics of Sound Waves — how does this connect to your model?
   • Superposition and Interference — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model demonstrate that noise cancellation is based on wave mathematics (superposition) rather than physical sound blocking?
   • Why does the same timing error that barely affects low-frequency cancellation completely ruin high-frequency cancellation?
   • What does the frequency-dependent effectiveness of noise cancellation reveal about the fundamental relationship between wavelength and precision?
   • How could the principles of destructive interference be applied beyond headphones — in architecture, vehicles, or industrial noise control?

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

Feedback vs. Feedforward Architecture. Two approaches to ANC microphone placement: feedforward places the mic outside the ear cup (sensing noise before it arrives) while feedback places it inside (sensing the combined result). Each has trade-offs in latency, accuracy, and frequency range
How would you model that?

Ear Seal Quality. The physical fit and acoustic seal between the headphone ear cup and the wearer's head — passive isolation from the physical seal blocks 10-25 dB of high-frequency noise that active cancellation struggles with, making passive and active noise reduction complementary
How would you model that?

Adaptive Algorithm. Machine learning algorithms that learn the acoustic characteristics of common noise environments (airplane, train, office) and pre-load optimized anti-phase profiles, reducing the processing time needed for real-time cancellation
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

Acoustic Engineers design sound management systems for headphones, concert venues, automotive cabins, and architectural spaces, earning $70,000–$130,000/year. Audio DSP (Digital Signal Processing) Engineers develop the real-time algorithms that compute anti-phase signals in noise-canceling headphones, earning $90,000–$170,000/year at companies like Bose, Sony, and Apple. Acoustics Researchers study wave behavior and develop new approaches to sound control, earning $75,000–$140,000/year.

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
Visual: Title slide with noise-canceling headphones and wave imagery
Say: "Your noise-canceling headphones don't block sound — they fight sound WITH sound. They literally add noise to your ears to make everything quieter. How is that possible?"
Do: Demonstrate: play a loud tone through a speaker, then play the anti-phase tone through a second speaker and let students hear the cancellation. Watch their reactions.
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and vocabulary terms
Say: "Today we're modeling the physics of silence — how two waves that are each individually loud can combine to produce nothing. It's one of the most beautiful results in all of physics."
Do: Have students read objectives. Pre-teach 'superposition' and 'destructive interference' with a visual animation of two waves combining.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: Sound wave + anti-phase wave = silence (visual equation)
Say: "More sound equals less sound. That sounds impossible — but it's just math. Two plus negative two equals zero. And that equation IS noise cancellation."
Do: Show the wave addition animation: y1 + y2 = 0 when waves are 180 degrees out of phase. Quick-write: Why do you think this works for airplane noise but not for your friend talking?
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps overview
Say: "We're going to build a model that shows exactly how anti-phase waves cancel noise — and discover why there's a frequency limit to this technology."
Do: Preview LEVER steps. Emphasize the connection between wave mathematics and real technology they use every day.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Component cards for noise cancellation model
Say: "What factors determine whether noise cancellation works? Some come from the environment, others come from the technology."
Do: Guide sorting: Ambient Noise Frequency and Amplitude are external (environmental inputs). Processing Speed, Phase Accuracy, and Cancellation Effectiveness are internal (technology and physics outcomes).
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows between components
Say: "Higher frequency means shorter wavelength. Shorter wavelength means tighter phase tolerance. But processing speed is finite. Follow this chain and you'll find the wall that noise cancellation hits."
Do: Students map the causal chain from frequency through wavelength to phase tolerance to cancellation effectiveness. Key insight: the limitation is physics, not engineering.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Wave cancellation simulations at different frequencies
Say: "Let's cancel a 100 Hz airplane engine, a 500 Hz rumble, and a 4,000 Hz voice. Watch the wave addition in real time and measure how much noise survives each one."
Do: Students predict dB reduction for each frequency. Run simulations showing wave superposition at each frequency. Visualize the increasing phase error at higher frequencies.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key findings — frequency vs. cancellation effectiveness curve
Say: "The physics is clear: long wavelengths are forgiving, short wavelengths are demanding. That's why your headphones kill the engine noise but not the conversation — and why the solution combines active cancellation with passive physical blocking."
Do: Show the frequency response curve of actual noise-canceling headphones. Compare to model predictions. Discuss: How close was the model to reality?
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Next-gen ANC system design
Say: "The headphone company wants to cancel human speech — the one thing current headphones can't do well. Your acoustic engineering team has to push the physics. What's your design?"
Do: Groups design improved ANC systems addressing the high-frequency challenge through faster processing, predictive algorithms, or multi-microphone arrays. Present with model-based frequency response predictions.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: How Do Noise-Canceling Headphones Work?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
Noise-canceling headphones represent one of the most elegant applications of wave physics in consumer technology. The concept seems paradoxical — how can adding more sound make things quieter? The answer lies in the mathematical principle of superposition, which governs how all waves interact. Understanding noise cancellation means understanding the fundamental nature of waves themselves.

NGSS ALIGNMENT:
HS-PS4-1, HS-PS4-5: Use mathematical representations to support a claim regarding relationships among the frequency, wavelength, and speed of waves traveling in various media. Communicate technical information about how some technological devices use the principles of wave behavior to function.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Using Mathematics and Computational Thinking
  Students use mathematical representations of wave functions to model superposition and predict the conditions under which destructive interference produces effective noise cancellation.
• Disciplinary Core Idea: PS4.A Wave Properties
  Waves of the same frequency can interfere constructively or destructively depending on their relative phase. The mathematical representation of superposition (y_total = y1 + y2) predicts the outcome of wave combination.
• Crosscutting Concept: Structure and Function
  Students analyze how the structure of the noise-canceling system (microphone placement, processing architecture, speaker design) determines its function (frequency-dependent cancellation effectiveness).

PACING GUIDE:
• Step 1 (Locate): 8-10 minutes
• Step 2 (Establish): 8-10 minutes
• Step 3 (Visualize & Evaluate): 10-12 minutes
• Step 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Superposition, Destructive Interference, Anti-Phase Signal, Frequency Response
□ Prepare How can adding more sound to your ears actually make everything quieter — and what does this tell us about the hidden mathematical nature of waves discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify ambient noise frequency, ambient noise amplitude, processing speed, phase accuracy, and cancellation effectiveness as the key components of the noise cancellation system.
• Establish: Students determine that ambient noise frequency and amplitude are external inputs from the environment, while processing speed, phase accuracy, and cancellation effectiveness are internal outcomes determined by the headphone's technology and the physics of wave interference.
• Visualize: Students build a computational model simulating wave superposition between ambient noise and an anti-phase signal, visualizing how phase alignment determines cancellation effectiveness across different frequencies.
• Evaluate: Students run low-frequency, high-frequency, and mixed-environment scenarios to observe how wavelength interacts with processing constraints to determine frequency-dependent cancellation performance.
• Revise: Students add feedback vs. feedforward architecture, ear seal quality, or adaptive algorithms to explore how engineering design choices extend the practical limits of noise cancellation.

BACKGROUND CONTENT:
• The Physics of Sound Waves:
  Sound is a longitudinal pressure wave — alternating compressions (high pressure) and rarefactions (low pressure) propagating through air at approximately 343 m/s at room temperature. Each sound wave can be described mathematically as y = A sin(2 pi f t + phi), where A is amplitude (loudness), f is frequency (pitch), and phi is phase (timing). Frequency is measured in Hertz (cycles per second): a 100 Hz wave has a wavelength of 3.43 meters, while a 4,000 Hz wave has a wavelength of only 8.6 centimeters. This wavelength difference is central to understanding why noise cancellation varies with frequency.

• Superposition and Interference:
  The principle of superposition states that when two waves occupy the same space, the total displacement at any point is the sum of the individual displacements. When two waves of the same frequency and amplitude are in phase (peaks aligned with peaks), they add constructively — the result is a wave of double amplitude (louder sound). When they are exactly 180 degrees out of phase (peaks aligned with troughs), they add destructively — the result is zero displacement (silence). Any phase offset between 0 and 180 degrees produces partial cancellation. Active noise cancellation exploits destructive interference by generating a wave that is as close to 180 degrees out of phase with the noise as possible.

• How Active Noise Cancellation Works:
  A noise-canceling headphone contains three critical components: an external microphone that samples ambient noise, a digital signal processor (DSP) that analyzes the noise wave and computes the anti-phase signal in real-time, and a speaker driver that outputs the anti-phase wave. The entire chain — sampling, computation, and playback — must complete in microseconds. For a 100 Hz wave (wavelength 3.43m), a 10-microsecond delay produces a phase error of only 0.36 degrees — negligible. But for a 4,000 Hz wave (wavelength 8.6cm), the same 10-microsecond delay produces a phase error of 14.4 degrees — significant enough to reduce cancellation effectiveness by 50%. This is the fundamental limitation: finite processing speed creates phase errors that scale with frequency.

• Passive Plus Active: The Complete System:
  Modern noise-canceling headphones don't rely on active cancellation alone — they combine it with passive isolation. The physical ear cup and cushion provide 10-25 dB of high-frequency noise reduction through absorption and reflection, similar to earplugs. Active cancellation handles the low frequencies (below 1,000 Hz) that pass through physical barriers easily due to their long wavelengths. Together, the hybrid system achieves 20-30 dB of total noise reduction across a broad frequency range. Some premium headphones also use adaptive algorithms that learn the acoustic properties of common environments and pre-compute anti-phase profiles, reducing the real-time processing burden.

COMMON MISCONCEPTIONS:
• "Noise-canceling headphones block or absorb sound"
  Reality: Active noise cancellation does not block or absorb sound waves — it adds a second sound wave that is the exact mathematical inverse of the first. The two waves combine through the principle of superposition to produce zero displacement (silence). This is fundamentally different from earmuffs or earplugs, which physically block sound. However, modern headphones DO combine active cancellation with passive blocking — the ear cup provides physical isolation for high frequencies while the ANC system handles low frequencies.
  Strategy: Demonstrate: play a tone and show it on an oscilloscope. Then play the anti-phase tone and show the cancellation on the oscilloscope. The sound isn't being absorbed — it's being canceled by addition. Remove one speaker and the tone returns.

• "Complete silence is possible with noise cancellation"
  Reality: Perfect destructive interference requires exact matching of frequency, amplitude, and phase — conditions that are theoretically possible for simple sine waves but practically impossible for complex real-world noise. Real noise contains thousands of frequencies simultaneously, each requiring its own anti-phase component. Noise-canceling headphones reduce noise by 20-30 dB (perceived as 75-90% quieter) but cannot achieve true silence. Additionally, the bone conduction of sound through the skull bypasses the headphones entirely.
  Strategy: Play a recording of noise-canceled audio (available online) and let students hear the residual noise. Ask: Is this silence? (No — it's 25 dB quieter, which sounds dramatically different but isn't zero.) Calculate: 25 dB reduction means the noise is reduced to about 3% of its original power.

• "Higher quality headphones can cancel ALL frequencies equally"
  Reality: No headphone, regardless of price, can equally cancel all frequencies because the limitation is fundamental physics, not engineering quality. Finite processing speed creates phase errors that increase linearly with frequency. Better headphones have faster processors (reducing the phase error at any given frequency) and better passive isolation (compensating for what active cancellation cannot achieve at high frequencies). But the physics of wavelength versus processing latency means there will always be a frequency above which active cancellation becomes ineffective.
  Strategy: Show the frequency response curves of the best noise-canceling headphones in the world — even the most expensive models show declining cancellation effectiveness above 1,000 Hz. Ask: If a $500 headphone can't do it, is it a quality problem or a physics problem?

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
Big Question: How can adding more sound to your ears actually make everything quieter — and what does this tell us about the hidden mathematical nature of waves?
Answer: Noise-canceling headphones work by adding sound to your ears, not blocking it — specifically, they generate an 'anti-noise' wave that is the exact mathematical inverse of the incoming noise. A microphone on the outside of the headphone captures ambient sound. A processor analyzes the wave's frequency and amplitude in real-time and generates an anti-phase signal — the same wave shape shifted by exactly 180 degrees (half a wavelength). When this anti-phase signal is played through the headphone speaker at the same time the original noise arrives at your ear, superposition occurs: the positive pressure peaks of the noise align with the negative pressure troughs of the anti-noise, and they cancel each other to produce silence. This works brilliantly for low-frequency sounds like engine rumble because the long wavelengths are forgiving of small timing errors. It works poorly for high-frequency sounds like voices because the short wavelengths demand impossibly precise phase alignment. That's why your noise-canceling headphones silence the airplane engine but not the person talking next to you.

Simulation Answers:
• Low-Frequency Cancellation Scenario: At 100 Hz, the model shows the anti-phase signal achieving nearly perfect 180° alignment with phase error below 1°. The noise wave and anti-phase wave combine through destructive interference, reducing amplitude by approximately 25-30 dB — the noise is perceived as barely audible background hiss. The long wavelength (3.43m) means even significant processing delays produce negligible phase errors, making low-frequency cancellation reliable and effective.
• High-Frequency Challenge Scenario: At 4,000 Hz, the model shows phase error increasing to 14-20° due to the short wavelength (8.6cm) and finite processing time. The destructive interference is incomplete — peaks and troughs no longer align precisely, leaving significant residual noise. Cancellation Effectiveness drops to only 3-5 dB, barely perceptible to the human ear. The model visualizes the misaligned anti-phase wave overlapping the noise wave, showing clearly where the phase error prevents cancellation.

Reflection Exemplars:
• Q: Why does the same processing delay ruin high-frequency cancellation but barely affect low-frequency cancellation?
  A: Phase error is measured as a fraction of the wavelength. A 10-microsecond processing delay translates to a fixed distance that sound travels (approximately 3.4mm at 343 m/s). At 100 Hz, the wavelength is 3.43 meters, so 3.4mm represents only 0.1% of the wavelength — a phase error of 0.36°, which barely affects cancellation. At 4,000 Hz, the wavelength is only 8.6 centimeters, so the same 3.4mm represents 4% of the wavelength — a phase error of 14.4°, which significantly reduces cancellation. The processing delay doesn't change, but its IMPACT changes dramatically with frequency because shorter wavelengths have tighter tolerance for timing errors.
• Q: How could destructive interference be applied beyond headphones?
  A: The same physics applies anywhere unwanted waves exist. Automotive engineers use active noise cancellation in car cabins to reduce engine and road noise. Architects design anti-noise systems for buildings near airports. Industrial facilities use destructive interference to create quiet zones for workers near loud machinery. Even beyond sound, destructive interference is used in optics (anti-reflective coatings on glasses and camera lenses work by destructive interference of light waves) and in medical imaging (noise cancellation in MRI machines). The underlying principle — two waves of equal amplitude and opposite phase sum to zero — is universal.

STEM CHALLENGE GUIDANCE:
Title: Design a Next-Generation Noise Cancellation System
Mission: Design an improved active noise cancellation system that extends effective cancellation to higher frequency ranges than current technology allows.
Scenario: A headphone manufacturer wants to develop the next generation of noise-canceling headphones that can cancel not just engine rumble but also human speech and other mid-frequency noise. Current technology achieves 25 dB reduction below 500 Hz but only 5 dB reduction above 2,000 Hz. Your acoustic engineering team must design a system architecture that improves high-frequency cancellation using faster processing, predictive algorithms, or multi-microphone arrays.
Introduction: Present the challenge: A headphone manufacturer wants next-generation ANC that effectively cancels human speech (300-3,000 Hz) in addition to the low-frequency noise current models handle well. Your acoustic engineering team must design a system architecture that overcomes the fundamental processing speed limitation through faster hardware, predictive algorithms, or novel microphone configurations.

Key Concepts:
• Digital Signal Processing Latency: The time between when a sound enters the microphone and when the anti-phase signal exits the speaker — measured in microseconds. Current ANC chips achieve latencies of 5-15 microseconds. Reducing this to 1-2 microseconds would dramatically improve high-frequency cancellation.
• Multi-Microphone Beamforming: Using arrays of multiple microphones to create a spatial map of incoming noise — direction, distance, and frequency content. This spatial information allows the processor to predict what the noise wave will look like when it reaches the ear, compensating for processing delay.
• Hybrid ANC Architecture: Systems that combine feedforward (external mic sensing noise before it arrives), feedback (internal mic measuring residual noise and adjusting), and adaptive filtering (learning and predicting noise patterns over time) to achieve cancellation performance that exceeds any single approach.

Evaluation Rubric:
• Expert (4): Design addresses the fundamental phase-accuracy-frequency relationship, proposes specific engineering solutions for reducing latency or compensating for it, includes frequency response predictions from model data, and demonstrates measurable improvement over current technology
• Proficient (3): Design identifies the high-frequency challenge, proposes reasonable engineering approaches with some reference to wave physics and model data
• Developing (2): Design proposes improvements but lacks detailed connection to phase accuracy, wavelength, or processing speed constraints
• Beginning (1): Design is incomplete or does not address the fundamental physics limitation that prevents high-frequency cancellation

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a visual showing two waves adding together at various phase offsets (0°, 90°, 180°) so students can see constructive, partial, and destructive interference directly
  • Use a wavelength comparison chart showing the relationship between frequency (100 Hz to 10,000 Hz), wavelength (3.43m to 3.4cm), and the phase error produced by a fixed processing delay at each frequency
  • Sentence frames: 'At __ Hz, the wavelength is __m, so a __μs processing delay produces a __° phase error, reducing cancellation from the ideal __dB to approximately __dB because __'

Extensions (Advanced Learners):
  • Research how anti-reflective coatings on glasses and camera lenses use destructive interference of LIGHT waves — compare the physics to sound-based noise cancellation and explain why the thin-film thickness must be exactly one-quarter wavelength
  • Investigate the Bose QuietComfort and Sony WH-1000XM series — research the engineering specifications and compare their measured frequency response curves to your model's predictions
  • Design an experiment using two speakers, a tone generator, and a sound level meter to demonstrate destructive interference in your classroom — predict the results using your model before running the experiment

Cross-Curricular Connections:
  • Math: Calculate the phase error (in degrees) produced by a 10-microsecond processing delay at frequencies of 50 Hz, 200 Hz, 1,000 Hz, 4,000 Hz, and 10,000 Hz. (Use: phase error = 360° x f x t_delay.) Graph the results. At what frequency does the phase error exceed 30° — the approximate threshold for 'poor' cancellation?
  • ELA: Write a product review of noise-canceling headphones that explains the physics of WHY they work (and why they don't work for everything) using accessible but scientifically accurate language. Target audience: tech-savvy teenagers who want to understand what they're buying.
  • History: Research the history of active noise cancellation — from Paul Lueg's 1936 patent to Lawrence Fogel's early prototypes to Amar Bose's commercial headphones in 2000. How did advances in digital signal processing and microchip miniaturization enable a 64-year-old idea to finally become practical?

CAST ALIGNMENT:
• Model how anti-phase sound waves produce destructive interference to cancel ambient noise
• Predict the frequency-dependent effectiveness of active noise cancellation based on wavelength and processing constraints
• Explain why noise-canceling headphones combine active cancellation (low frequency) with passive isolation (high frequency)

CAST-Style Assessment Questions:
• Multiple Choice: An airplane engine produces noise at 120 Hz. Noise-canceling headphones generate an anti-phase signal at the same frequency and amplitude, but the phase offset is 170 degrees instead of the ideal 180 degrees. What is the result? A) Complete silence, B) Significant noise reduction with some residual sound, C) No change in noise level, D) The noise gets louder
• Constructed Response: Using your model, explain why noise-canceling headphones effectively silence a 100 Hz airplane engine rumble but barely reduce a 3,000 Hz human voice. Connect your answer to wavelength, processing speed, phase accuracy, and the mathematical requirements for destructive interference.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: How Do Noise-Canceling Headphones Work?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. How do you think noise-canceling headphones work — do they block sound, absorb it, or do something else entirely?

   _________________________________________________________

   _________________________________________________________

2. What happens when two waves meet in the same place at the same time? Can you think of examples from water or sound?

   _________________________________________________________

   _________________________________________________________

3. Why do you think noise-canceling headphones are better at canceling airplane engine noise than they are at canceling human voices?

   _________________________________________________________

   _________________________________________________________

4. If I told you that noise-canceling headphones work by adding MORE sound to your ears, would you believe me? How could more sound make things quieter?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Superposition                 
___ Destructive Interference      
___ Anti-Phase Signal             
___ Frequency Response            

A. The principle that when two waves occupy the same space, the resulting displacement at any point is the algebraic sum of the individual wave displacements — waves add together constructively (amplitudes combine to increase) or destructively (amplitudes cancel to decrease)
B. The phenomenon that occurs when two waves of the same frequency and amplitude meet exactly out of phase (shifted by half a wavelength) — their peaks align with the other's troughs, and the waves cancel to produce silence or reduced amplitude
C. A sound wave generated by noise-canceling headphones that is identical to the incoming noise but shifted by exactly 180 degrees (half a wavelength) — when combined with the original noise wave, the two signals destructively interfere, canceling each other
D. The range of sound frequencies over which a noise-canceling system is effective — current technology cancels low frequencies (below 1,000 Hz) very well but struggles with high frequencies because their shorter wavelengths require faster processing to maintain accurate phase alignment

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

SCENARIO: Low-Frequency Cancellation
Settings: Noise: 100 Hz sine wave at 80 dB | ANC: Active
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: High-Frequency Challenge
Settings: Noise: 4,000 Hz sine wave at 70 dB | ANC: Active
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Mixed Environment
Settings: Noise: Airplane cabin spectrum (multiple frequencies) | ANC: Active
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

1. How does your model demonstrate that noise cancellation is based on wave mathematics (superposition) rather than physical sound blocking?

   _________________________________________________________

   _________________________________________________________

2. Why does the same timing error that barely affects low-frequency cancellation completely ruin high-frequency cancellation?

   _________________________________________________________

   _________________________________________________________

3. What does the frequency-dependent effectiveness of noise cancellation reveal about the fundamental relationship between wavelength and precision?

   _________________________________________________________

   _________________________________________________________

4. How could the principles of destructive interference be applied beyond headphones — in architecture, vehicles, or industrial noise control?

   _________________________________________________________

   _________________________________________________________

5. What limitations does your model have in capturing the full complexity of real-world noise cancellation environments?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. How can adding more sound to your ears actually make everything quieter — and what does this tell us about the hidden mathematical nature of waves? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Using Mathematics and Computational Thinking
   □ Disciplinary Core Idea: PS4.A Wave Properties
   □ Crosscutting Concept: Structure and Function

3. What limitations does your model have in capturing the full complexity of real-world noise cancellation environments?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Next-Generation Noise Cancellation System
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design an improved active noise cancellation system that extends effective cancellation to higher frequency ranges than current technology allows.

SCENARIO: A headphone manufacturer wants to develop the next generation of noise-canceling headphones that can cancel not just engine rumble but also human speech and other mid-frequency noise. Current technology achieves 25 dB reduction below 500 Hz but only 5 dB reduction above 2,000 Hz. Your acoustic engineering team must design a system architecture that improves high-frequency cancellation using faster processing, predictive algorithms, or multi-microphone arrays.

GUIDING QUESTIONS:
• What is the fundamental physics limitation that prevents current systems from canceling high-frequency noise effectively?
• What processing speed improvement does your model show is needed to achieve 15 dB reduction at 2,000 Hz?
• Could predictive algorithms that anticipate noise patterns reduce the effective processing delay — and what model evidence supports this?

DESIGN THINKING:
• What microphone placement strategy would minimize the distance sound must travel before being sampled, reducing processing delay?

  _________________________________________________________

• How could multiple microphones create a spatial noise map that predicts incoming sound direction and characteristics?

  _________________________________________________________

• What role could machine learning play in pre-computing anti-phase signals for common noise environments (airplane, subway, office)?

  _________________________________________________________

• How would you test your improved system, and what metrics would prove it outperforms current technology?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Design addresses the fundamental phase-accuracy-frequency relationship, proposes specific engineering solutions for reducing latency or compensating for it, includes frequency response predictions from model data, and demonstrates measurable improvement over current technology
• Proficient (3): Design identifies the high-frequency challenge, proposes reasonable engineering approaches with some reference to wave physics and model data
• Developing (2): Design proposes improvements but lacks detailed connection to phase accuracy, wavelength, or processing speed constraints
• Beginning (1): Design is incomplete or does not address the fundamental physics limitation that prevents high-frequency cancellation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CAST-Aligned Pre/Post Assessment

### Administration Instructions

These 5 multiple-choice questions are administered identically as both a pre-assessment (before Activity 1) and a post-assessment (after Activity 4). Score each out of 5. Learning growth = post-score minus pre-score.

Questions follow the California Science Test (CAST) stimulus-response format. Each item is three-dimensional, assessing a Science and Engineering Practice (SEP), Disciplinary Core Idea (DCI), and Crosscutting Concept (CCC) simultaneously, aligned to HS-PS4-1, HS-PS4-5.

---

### Question 1

CAST Alignment: SEP 2.1.1 (Determine components of a system) + DCI PS4.1 + CCC4 (Systems and System Models)

A student is using the ModelIt platform to study the system in this lesson. The model includes these components: Ambient Noise Frequency, Ambient Noise Amplitude, Processing Speed, Phase Accuracy, Cancellation Effectiveness. Some components are external (Ambient Noise Frequency, Ambient Noise Amplitude) and some are internal (Processing Speed, Phase Accuracy, Cancellation Effectiveness). The student needs to understand what each component represents and how they are organized.

A student's model shows that at 100 Hz, a 5-microsecond timing error in the anti-phase signal reduces cancellation effectiveness by only 2%, but at 5,000 Hz the same error reduces effectiveness by 45%. Which analysis best explains this frequency-dependent sensitivity?

A. The electronics work harder at high frequencies, introducing more noise
B. At 100 Hz (wavelength 3.4 m), 5 microseconds represents 0.05% of the wave period, barely affecting phase alignment; at 5,000 Hz (wavelength 0.069 m), the same delay represents 2.5% of the wave period, creating significant phase misalignment that prevents destructive interference
C. Low-frequency sounds are naturally quieter, so less cancellation is needed
D. The model applies different equations for low and high frequencies

Correct Answer: B

Feedback: Correct. Phase accuracy is relative to wavelength, not absolute. A fixed timing error is a small fraction of a long-period wave (low frequency) but a large fraction of a short-period wave (high frequency). This is why the same hardware achieves excellent low-frequency cancellation but poor high-frequency cancellation. If you chose A, this answer suggests something is being added to the system. Look carefully at the model — the total amount stays the same even when components change. The system is conserving matter or energy. If you chose C, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows.

---

### Question 2

CAST Alignment: SEP 2.1.2 (Determine relationships among components) + DCI PS4.1 + CCC4 (Systems and System Models)

In the computational model for this lesson, a student draws arrows between components to show relationships. The model shows that when Ambient Noise Frequency increases, Phase Accuracy decreases; when Phase Accuracy increases, Cancellation Effectiveness increases. The student is trying to understand why these relationships are positive or negative.

The model reveals that when the anti-phase signal has 95% amplitude accuracy but perfect phase alignment, cancellation effectiveness is 90%. When phase accuracy is 95% but amplitude is perfect, cancellation effectiveness drops to 72%. Which conclusion is best supported by this comparison?

A. Amplitude and phase contribute equally to cancellation effectiveness
B. Phase accuracy has a more critical effect on cancellation than amplitude accuracy because even small phase errors create regions where the waves partially reinforce rather than cancel
C. Amplitude accuracy is more important than phase accuracy
D. Neither accuracy matters because cancellation is an all-or-nothing phenomenon

Correct Answer: B

Feedback: Correct. Phase errors cause portions of the anti-phase signal to shift from canceling (destructive) to reinforcing (constructive), actively adding energy rather than removing it. Amplitude errors merely leave residual noise proportional to the mismatch. Phase errors have more severe consequences because they can reverse the intended effect. If you chose A, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose C, this answer suggests something is being added to the system. Look carefully at the model — the total amount stays the same even when components change. The system is conserving matter or energy. If you chose D, this reflects a common misconception. Matter cannot be created or destroyed — it can only change form. The total amount of matter in the system stays the same.

---

### Question 3

CAST Alignment: SEP 2.1.3 (Evaluate a model's accuracy) + DCI PS4.1 + CCC4 (Systems and System Models)

A student runs a simulation of the model. The model shows that when Ambient Noise Frequency increases, Phase Accuracy decreases and when Phase Accuracy increases, Cancellation Effectiveness increases and when Processing Speed increases, Phase Accuracy increases. The student changes one variable to see how the whole system responds.

A student proposes improving noise cancellation by adding a second microphone farther from the ear to give the processor more time to compute the anti-phase signal. Based on the model, which evaluation of this proposal is most accurate?

A. The proposal would not help because all microphones are equally fast
B. The proposal is sound: a forward-facing microphone detects noise earlier, giving the processor more time to analyze frequency content and generate an accurate anti-phase signal, particularly improving performance at higher frequencies
C. Two microphones would create twice as much noise to cancel
D. The additional microphone would cancel the first microphone's signal

Correct Answer: B

Feedback: Correct. This is exactly how modern feedforward noise cancellation works. An external microphone captures noise before it reaches the ear, providing crucial extra processing time. This advance warning is particularly valuable for higher frequencies, where the short wavelengths demand faster and more precise anti-phase generation. If you chose A, the model shows these components ARE connected. When one changes, it affects the others through the relationships (positive or negative) that you mapped in the model. If you chose C, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows.

---

### Question 4

CAST Alignment: SEP 2.1.4 (Represent mechanisms to explain/predict events) + DCI PS4.1 + CCC4 (Systems and System Models)

Scientists are studying data related to this system. They collected observations over time and noticed patterns in how the components change. The data shows how changes in one part of the system cascade through the other parts.

The model shows that noise cancellation achieves 28 dB reduction at 100 Hz, 22 dB at 500 Hz, 12 dB at 2,000 Hz, and only 3 dB at 8,000 Hz. A student asks why the headphones do not simply use passive isolation (physical blocking) for high frequencies instead. Based on wave physics, which response is most accurate?

A. Passive isolation does not work for any frequency
B. This is exactly what modern headphones do: high-frequency sounds have short wavelengths that are easily blocked by the physical ear cup padding, while low-frequency long wavelengths diffract around barriers, requiring active cancellation
C. Passive isolation only works for low frequencies
D. High frequencies are too quiet to need isolation

Correct Answer: B

Feedback: Correct. This is a fundamental insight about wave behavior: long-wavelength (low-frequency) waves diffract around barriers, making them hard to block physically but their long period makes them easy to cancel actively. Short-wavelength (high-frequency) waves are easily blocked by physical barriers but hard to cancel actively. Modern headphones combine both methods. If you chose A, the model shows these components ARE connected. When one changes, it affects the others through the relationships (positive or negative) that you mapped in the model. If you chose C, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows.

---

### Question 5

CAST Alignment: SEP 2.1.5 (Apply a model to make predictions) + DCI PS4.1 + CCC4 (Systems and System Models)

A team wants to use the model to solve a real-world problem related to this system. They know they cannot control the external components (Ambient Noise Frequency, Ambient Noise Amplitude), but they can take action on internal components (Processing Speed, Phase Accuracy, Cancellation Effectiveness). They need to decide which action would be most effective based on what the model shows.

Based on the complete model analysis, a student claims that perfect noise cancellation across all frequencies is theoretically possible with fast enough electronics. Which model-based assessment is most accurate?

A. The student is correct because faster processing solves all phase accuracy problems
B. Even with infinitely fast processing, perfect cancellation faces fundamental limits: the acoustic environment changes continuously, reflected sound arrives from multiple angles and distances, and the ear canal's geometry creates resonances that shift the phase relationship unpredictably
C. The student is correct because noise cancellation is limited only by processing speed
D. Perfect cancellation is already achieved by current technology

Correct Answer: B

Feedback: Correct. Processing speed is one limit, but not the only one. Sound reaches the ear from multiple directions with different delays, the listener's head movement changes the acoustic geometry, ear canal resonances alter phase relationships, and environmental noise is constantly changing. These physical realities impose limits beyond processing speed. If you chose A, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose C, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows. If you chose D, look at the evidence from the model. The correct answer (B) is supported by the relationships between components. This answer does not match what the simulation data shows.

---

### Answer Key

Question 1: B (Cognitive Level: Identify — SEP 2.1.1, DCI PS4.1, CCC4)
Question 2: B (Cognitive Level: Reason — SEP 2.1.2, DCI PS4.1, CCC4)
Question 3: B (Cognitive Level: Reason — SEP 2.1.3, DCI PS4.1, CCC4)
Question 4: B (Cognitive Level: Reason + Evidence — SEP 2.1.4, DCI PS4.1, CCC4)
Question 5: B (Cognitive Level: Predict + Apply — SEP 2.1.5, DCI PS4.1, CCC4)


## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-11/G11L1-L08/G11L1-L08-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-11/G11L1-L08/G11L1-L08-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-11/G11L1-L08/G11L1-L08-Student-Presentation.pptx] |
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