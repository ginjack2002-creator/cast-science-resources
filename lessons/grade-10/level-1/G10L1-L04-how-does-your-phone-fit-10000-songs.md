# Lesson: How Does Your Phone Fit 10,000 Songs?

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G10L1-L04 |
| **Grade** | 10th Grade — Level 1: How the World Works |
| **Lesson Name** | How Does Your Phone Fit 10,000 Songs? |
| **Status** | Template |

---

## Platform

### Title
**How Does Your Phone Fit 10,000 Songs? — Modeling Digital Signal Processing, Data Compression, and Recommendation Algorithms**

### Overview
The ability to carry thousands of songs in your pocket represents one of the most remarkable applications of wave physics and computational mathematics in history. Every song on your phone began as vibrations in air, was converted to electrical signals, digitized into numbers, compressed by algorithms that exploit human hearing limits, and stored as magnetic patterns on a tiny chip. Understanding this chain means understanding both the physics of waves and the engineering of information. Students investigate the driving question: How does a device the size of your palm store an entire music library and somehow know what song you want to hear next? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of a smartphone displaying a music app with colorful waveform visualizations, high-quality earbuds connected, sound wave patterns emanating from the phone in a creative artistic style, modern dark background]

### Grade
10th Grade — Level 1: How the World Works

### NGSS Standard
**HS-PS4-5, HS-ETS1-1**: Communicate technical information about how some technological devices use the principles of wave behavior and wave interactions with matter to transmit and capture information and energy. Analyze a major global challenge to specify qualitative and quantitative criteria and constraints for solutions that account for societal needs and wants.

### Learning Objectives
- Model how analog audio signals are digitized, compressed, and stored on electronic devices
- Explain the trade-off between audio quality and file size in data compression algorithms
- Analyze how recommendation algorithms use listening data to predict user preferences
- Evaluate the engineering trade-offs between signal quality, storage efficiency, and user experience

### Component List (Starting Model: 5 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Audio Signal Quality | External | The fidelity of the original sound wave capture, determined by sampling rate and bit depth — higher quality means larger raw files but more accurate sound reproduction |
| Data Compression Rate | External | The ratio of original file size to compressed file size, controlled by the compression algorithm settings — higher compression means smaller files but more information lost |
| Algorithm Accuracy | Internal | How effectively the recommendation system predicts songs the user will enjoy, based on the quantity and quality of listening data processed |
| User Engagement | Internal | The amount of time users spend listening and interacting with the platform, which generates more data and improves algorithm accuracy in a feedback loop |
| Recommendation Match | Internal | The percentage of algorithmically suggested songs that the user actually listens to and enjoys, representing the system's real-world performance |

### Research for Lesson
- Sound as Waves — reference materials and textbook resources
- Analog-to-Digital Conversion — reference materials and textbook resources
- Psychoacoustic Compression — reference materials and textbook resources
- Machine Learning Recommendations — reference materials and textbook resources

---

## Step 1: LOCATE — Build Your System

### Text Editor

```
HOW DOES YOUR PHONE FIT 10,000 SONGS?

Modeling Digital Signal Processing, Data Compression, and Recommendation Algorithms.
How does a device the size of your palm store an entire music library and somehow know what song you want to hear next?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Audio Signal Quality" — the fidelity of the original sound wave capture
  ○ Click "Data Compression Rate" — the ratio of original file size to compressed file size
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Algorithm Accuracy" — how effectively the recommendation system predicts songs the user will enjoy
  ○ Click "User Engagement" — the amount of time users spend listening and interacting with the platform
  ○ Click "Recommendation Match" — the percentage of algorithmically suggested songs that the user actually listens to and enjoys

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
"How does a device the size of your palm store an entire music library and somehow know what song you want to hear next?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Audio Signal Quality' — that's external. The fidelity of the original sound wave capture.
Click on 'Data Compression Rate' — that's external. The ratio of original file size to compressed file size.
Click on 'Algorithm Accuracy' — that's internal. How effectively the recommendation system predicts songs the user will enjoy.
Click on 'User Engagement' — that's internal. The amount of time users spend listening and interacting with the platform.
Click on 'Recommendation Match' — that's internal. The percentage of algorithmically suggested songs that the user actually listens to and enjoys.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Audio Signal Quality and Data Compression Rate are external components because they are engineering design choices — a streaming service decides what recording quality to use and how aggressively to compress files. Algorithm Accuracy, User Engagement, and Recommendation Match are internal because they emerge from the interaction between the system and user behavior — they cannot be directly set but result from how well the system works.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next step, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 5 components sorted: Audio Signal Quality, Data Compression Rate (External), Algorithm Accuracy, User Engagement, Recommendation Match (Internal)]

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
• Click on "Audio Signal Quality" and drag an arrow to "Data Compression Rate"
• Click on "Data Compression Rate" and drag an arrow to "User Engagement"
• Click on "User Engagement" and drag an arrow to "Algorithm Accuracy"

Task C: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Audio Signal Quality → Data Compression Rate = POSITIVE (+)
    Higher audio quality means larger raw files that require more aggressive compression to fit in limited storage. Engineers must balance capturing high-fidelity sound against the need to reduce file size for practical storage and streaming.

  ○ Data Compression Rate → User Engagement = POSITIVE (+)
    Moderate compression maintains audio quality that keeps users engaged. But excessive compression degrades quality enough that users disengage — there is an optimal zone where files are small enough to store efficiently but good enough to enjoy.

  ○ User Engagement → Algorithm Accuracy = POSITIVE (+)
    More user engagement generates more listening data — play counts, skip rates, completion rates, time-of-day patterns. This data trains the recommendation algorithm, improving its accuracy. The more you listen, the better it knows you.

Task D: CHECK YOUR MODEL
• You should have 3 arrows total
• 0 negative relationship(s), 1 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: When you compress a song from 50MB to 5MB, something must be removed. How does the algorithm decide what you won't miss — and what happens to the music experience when it removes too much?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Audio Signal Quality' and drag an arrow
over to 'Data Compression Rate.'

Here's the key question: When audio signal quality goes UP, does
data compression rate go UP or DOWN?

Higher audio quality means larger raw files that require more aggressive compression to fit in limited storage. Engineers must balance capturing high-fidelity sound against the need to reduce file size for practical storage and streaming.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Data Compression Rate' and drag an arrow
over to 'User Engagement.'

Here's the key question: When data compression rate goes UP, does
user engagement go UP or DOWN?

Moderate compression maintains audio quality that keeps users engaged. But excessive compression degrades quality enough that users disengage — there is an optimal zone where files are small enough to store efficiently but good enough to enjoy.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'User Engagement' and drag an arrow
over to 'Algorithm Accuracy.'

Here's the key question: When user engagement goes UP, does
algorithm accuracy go UP or DOWN?

More user engagement generates more listening data — play counts, skip rates, completion rates, time-of-day patterns. This data trains the recommendation algorithm, improving its accuracy. The more you listen, the better it knows you.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Look at your model now. You've got 0 negative and 1
positive relationships. 3 arrows total.

When you compress a song from 50MB to 5MB, something must be removed. How does the algorithm decide what you won't miss — and what happens to the music experience when it removes too much?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Audio Signal Quality +→ Data Compression Rate, Data Compression Rate +→ User Engagement, User Engagement +→ Algorithm Accuracy]

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
• When Audio Signal Quality is HIGH, what happens to the internal components?

Task C: SCENARIO — HIGH QUALITY
• Audio Quality: Maximum | Compression: Minimal
• PREDICT FIRST: How many songs do you predict can fit on a 64GB device at maximum quality versus maximum compression?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task D: SCENARIO — MAXIMUM COMPRESSION
• Audio Quality: Standard | Compression: Maximum
• PREDICT FIRST: At what compression ratio do you predict the average listener will start noticing audio quality loss?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task E: SCENARIO — NEW VS. VETERAN USER
• Comparing algorithm with 0 vs. 10,000 hours of data
• PREDICT FIRST: How many data points do you predict the algorithm needs before its recommendations match what you'd choose yourself?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Data compression exploits human perception limits — MP3 removes frequencies most people can't hear and sounds masked by louder sounds, reducing file size by 90% with minimal perceived quality loss
• There's a critical compression threshold beyond which quality drops noticeably — the algorithm must balance file size against the limits of human hearing perception
• Recommendation algorithms improve through a feedback loop: more listening generates more data, which improves predictions, which increases engagement, which generates more data
• The entire modern music industry depends on the same wave physics principles that govern how sound travels through air — digitization is simply converting those waves to numbers

THE ANSWER: Your phone fits 10,000 songs through a brilliant exploitation of psychoacoustics — the science of human hearing perception. Compression algorithms like AAC and MP3 analyze each song's sound waves and remove frequencies your ear can't hear (above ~20kHz), sounds masked by louder sounds, and redundant data patterns. A 50MB raw audio file becomes 5MB with virtually no perceptible quality loss. Recommendation algorithms then use your listening patterns — skip rates, repeat plays, time of day, genre sequences — to predict what you want to hear next. Both technologies are applied wave physics and computational mathematics working together.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: High Quality. Audio Quality: Maximum | Compression: Minimal.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Maximum Compression.
Audio Quality: Standard | Compression: Maximum.

Before you run it — make a prediction. At what compression ratio do you predict the average listener will start noticing audio quality loss?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: New vs. Veteran User. Comparing algorithm with 0 vs. 10,000 hours of data.
How many data points do you predict the algorithm needs before its recommendations match what you'd choose yourself?

Here's what our model reveals: Your phone fits 10,000 songs through a brilliant exploitation of psychoacoustics — the science of human hearing perception. Compression algorithms like AAC and MP3 analyze each song's sound waves and remove frequencies your ear can't hear (above ~20kHz), sounds masked by louder sounds, and redundant data patterns. A 50MB raw audio file becomes 5MB with virtually no perceptible quality loss. Recommendation algorithms then use your listening patterns — skip rates, repeat plays, time of day, genre sequences — to predict what you want to hear next. Both technologies are applied wave physics and computational mathematics working together.

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
   • What happens if you turn OFF Audio Signal Quality?
   • What happens if you turn OFF Data Compression Rate?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Bit Depth — The number of bits used to represent each audio sample — 16-bit provides 65,536 possible values per sample while 24-bit provides over 16 million, capturing quieter details and greater dynamic range
   • Network Bandwidth — The speed of the data connection available for streaming, which limits the quality of audio that can be delivered in real time and determines whether compression must be increased
   • Listening Context — Environmental factors like background noise, earphone quality, and listener attention that affect whether compression artifacts are perceptible

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • Sound as Waves — how does this connect to your model?
   • Analog-to-Digital Conversion — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model demonstrate the trade-off between file size and audio quality?
   • Why is it important that compression algorithms are based on human perception rather than pure mathematics?
   • What feedback loop drives recommendation algorithm improvement, and what are its limitations?
   • How would your model change if the target user was an audiophile versus a casual listener?

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

Bit Depth. The number of bits used to represent each audio sample — 16-bit provides 65,536 possible values per sample while 24-bit provides over 16 million, capturing quieter details and greater dynamic range
How would you model that?

Network Bandwidth. The speed of the data connection available for streaming, which limits the quality of audio that can be delivered in real time and determines whether compression must be increased
How would you model that?

Listening Context. Environmental factors like background noise, earphone quality, and listener attention that affect whether compression artifacts are perceptible
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

Audio Engineers design sound recording, processing, and playback systems using wave physics and digital signal processing. They work in music studios, tech companies (Spotify, Apple, Sony), and live sound, earning $50,000–$120,000/year. Data Scientists who build recommendation algorithms earn $90,000–$180,000/year at tech companies.

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
Visual: Title slide with phone displaying music library
Say: "Your phone has 10,000 songs on it. Each song started as vibrations in a recording studio. How did AIR VIBRATIONS become DATA in your pocket?"
Do: Show file size comparison: one uncompressed WAV song (50MB) vs. 10,000 compressed songs on a 64GB phone. How is that possible?
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and vocabulary
Say: "Today we're tracing the journey of a sound wave from a singer's mouth to your earbuds — and every transformation along the way."
Do: Have students read objectives. Pre-teach 'data compression' and 'sampling rate' with audio examples.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: How does 10,000 songs fit in your palm?
Say: "If one song takes 50MB uncompressed, 10,000 songs would need 500GB. Your phone has 64GB. Something is being removed. What?"
Do: Students calculate: How much data must be removed? What could possibly be expendable in a song?
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps overview
Say: "We're modeling the entire chain — from sound wave to compressed file to recommended playlist."
Do: Preview LEVER steps. Emphasize this connects wave physics to information technology.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Component cards for digital music model
Say: "What can a streaming service CONTROL? What outcomes emerge from those choices?"
Do: Guide sorting. Audio quality and compression rate are design choices; engagement and match are outcomes.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows between components
Say: "More compression means smaller files but worse sound. Where's the sweet spot where your ears can't tell the difference?"
Do: Play audio samples at different compression levels. Can students identify which is compressed?
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Compression quality curves and recommendation accuracy graphs
Say: "Let's find the threshold — the exact compression level where your ears stop noticing the difference."
Do: Students predict the perception threshold. Run simulations. Then test new-user vs. veteran recommendation accuracy.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key findings about compression and algorithms
Say: "The algorithm removes sounds you literally CANNOT hear. And the recommendation engine gets better every time you press play or skip."
Do: Connect psychoacoustic masking to wave physics. Discuss the feedback loop driving algorithm improvement.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Music platform design challenge
Say: "Build a music app for students with cheap phones and bad wifi. Make it sound good, fit a lot of songs, and recommend what they'll love."
Do: Groups design streaming systems balancing quality, storage, and recommendation. Present solutions.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: How Does Your Phone Fit 10,000 Songs?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
The ability to carry thousands of songs in your pocket represents one of the most remarkable applications of wave physics and computational mathematics in history. Every song on your phone began as vibrations in air, was converted to electrical signals, digitized into numbers, compressed by algorithms that exploit human hearing limits, and stored as magnetic patterns on a tiny chip. Understanding this chain means understanding both the physics of waves and the engineering of information.

NGSS ALIGNMENT:
HS-PS4-5, HS-ETS1-1: Communicate technical information about how some technological devices use the principles of wave behavior and wave interactions with matter to transmit and capture information and energy. Analyze a major global challenge to specify qualitative and quantitative criteria and constraints for solutions that account for societal needs and wants.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Constructing Explanations and Designing Solutions
  Students construct explanations of how wave behavior enables digital audio capture and design solutions that balance quality, storage, and user experience.
• Disciplinary Core Idea: PS4.C Information Technologies and Instrumentation / ETS1.A Defining and Delimiting Engineering Problems
  Technological devices use wave principles to capture, process, and transmit audio information. Engineering problems require specifying criteria and constraints.
• Crosscutting Concept: Systems and System Models
  Students model the music streaming system as interconnected subsystems — signal capture, compression, storage, and recommendation — that must be optimized together.

PACING GUIDE:
• Step 1 (Locate): 8-10 minutes
• Step 2 (Establish): 8-10 minutes
• Step 3 (Visualize & Evaluate): 10-12 minutes
• Step 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Digital Signal Processing, Data Compression, Sampling Rate, Recommendation Algorithm
□ Prepare How does a device the size of your palm store an entire music library and somehow know what song you want to hear next discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify audio signal quality, data compression rate, algorithm accuracy, user engagement, and recommendation match as the key components of the digital music system.
• Establish: Students determine that audio quality and compression rate have an inverse relationship, and that algorithm accuracy improves through a feedback loop with user engagement — more data means better predictions.
• Visualize: Students build a computational model showing how compression settings affect storage capacity and audio fidelity, and how user data volume drives recommendation performance.
• Evaluate: Students run high quality, maximum compression, and new-vs-veteran user scenarios to discover the perception threshold for compression and the data requirement for accurate recommendations.
• Revise: Students add bit depth, network bandwidth, or listening context to model more realistic streaming system dynamics.

BACKGROUND CONTENT:
• Sound as Waves:
  Sound is a longitudinal pressure wave traveling through air at about 343 m/s. The wave's frequency (20 Hz to 20,000 Hz for human hearing) determines pitch, and its amplitude determines loudness. When a microphone captures sound, it converts these pressure variations into an analog electrical signal that mirrors the original wave pattern.

• Analog-to-Digital Conversion:
  To store sound digitally, the analog signal must be sampled — measured at regular intervals — and quantized — rounded to the nearest digital value. CD quality uses 44,100 samples per second (Nyquist theorem requires 2x the highest frequency) at 16-bit depth (65,536 possible values per sample). This produces about 10MB of raw data per minute of stereo music.

• Psychoacoustic Compression:
  MP3, AAC, and Ogg Vorbis compression algorithms exploit the limits of human hearing through a technique called perceptual coding. Sounds below the hearing threshold are removed. When a loud sound masks a quiet sound (simultaneous masking), the quiet sound is removed. Sounds that occur just before or after a loud sound are also removed (temporal masking). The result: 90% data reduction with minimal perceived quality loss.

• Machine Learning Recommendations:
  Modern recommendation systems use collaborative filtering (users who liked X also liked Y), content analysis (analyzing the audio features of songs — tempo, key, energy, danceability), and deep learning (neural networks that find complex patterns in billions of listening sessions). Spotify's 'Discover Weekly' playlist analyzes over 100 data points per song per listener to generate 30 personalized recommendations each Monday.

COMMON MISCONCEPTIONS:
• "Compressed music sounds terrible compared to the original"
  Reality: Modern lossy compression at 256kbps or higher is virtually indistinguishable from the original in controlled listening tests. The compression algorithm specifically removes sounds that fall below human perception thresholds — frequencies you can't hear and sounds masked by louder sounds. Most people cannot identify the compressed version in a blind A/B test at standard quality settings.
  Strategy: Run a blind listening test in class: play a WAV and a 256kbps AAC version of the same song. Can anyone consistently identify which is compressed? Most cannot.

• "More data always means better recommendations"
  Reality: While more data generally improves recommendations, there are diminishing returns and quality matters more than quantity. An algorithm with 100 hours of diverse listening data often outperforms one with 1,000 hours of repetitive data. Additionally, more data collection raises privacy concerns — the question isn't just CAN we collect more data, but SHOULD we.
  Strategy: Thought experiment: If the algorithm tracked your location, heart rate, and mood while listening, it would make better recommendations. Would you accept that trade-off?

• "Digital music perfectly captures the original sound"
  Reality: Digitization is a sampling process that captures snapshots of the sound wave at regular intervals. Between samples, the original analog information is lost and must be interpolated. At CD quality (44.1kHz), the Nyquist theorem guarantees frequencies up to 22.05kHz are captured accurately — sufficient for human hearing (20Hz-20kHz). But no digital format captures every infinitesimal detail of the original analog wave.
  Strategy: Show a zoomed-in view of a smooth sine wave versus its sampled staircase approximation. At normal zoom, they look identical. The difference is real but below human perception — which is the entire point.

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
Big Question: How does a device the size of your palm store an entire music library and somehow know what song you want to hear next?
Answer: Your phone fits 10,000 songs through a brilliant exploitation of psychoacoustics — the science of human hearing perception. Compression algorithms like AAC and MP3 analyze each song's sound waves and remove frequencies your ear can't hear (above ~20kHz), sounds masked by louder sounds, and redundant data patterns. A 50MB raw audio file becomes 5MB with virtually no perceptible quality loss. Recommendation algorithms then use your listening patterns — skip rates, repeat plays, time of day, genre sequences — to predict what you want to hear next. Both technologies are applied wave physics and computational mathematics working together.

Simulation Answers:
• High Quality Scenario: At maximum Audio Signal Quality with minimal Data Compression Rate, each song takes approximately 50MB (uncompressed WAV) or 15MB (lossless FLAC). A 64GB device holds only about 1,200-4,200 songs at these settings. The audio fidelity is perfect, but storage is severely limited. Most listeners cannot distinguish this quality from well-compressed audio in typical listening environments.
• New vs. Veteran User Scenario: A brand-new user with zero listening history receives generic, popularity-based recommendations with about 20-30% match rate. After 100 hours of listening, the algorithm has enough behavioral data to identify genre preferences, increasing match to ~50%. After 1,000+ hours, the system understands nuanced taste patterns — tempo preferences, lyrical themes, seasonal patterns — reaching 70-80% match rate. This demonstrates the feedback loop: engagement drives data, data drives accuracy.

Reflection Exemplars:
• Q: Why is human perception the key to compression?
  A: Compression algorithms don't just remove random data — they remove data that human ears cannot perceive. The MP3 algorithm uses a psychoacoustic model that predicts which frequencies are masked by louder sounds, which sounds fall below the hearing threshold, and which temporal details the brain fills in automatically. This means compression is fundamentally about BIOLOGY as much as mathematics — the algorithm succeeds because it exploits the limitations of the human auditory system.
• Q: What ethical concerns arise from recommendation algorithms?
  A: Recommendation algorithms create filter bubbles — by always suggesting similar music, they can narrow a listener's exposure and reinforce existing preferences rather than introducing diversity. The engagement feedback loop optimizes for TIME SPENT, not necessarily for genuine satisfaction or musical growth. Additionally, these systems collect enormous amounts of behavioral data — what you listen to, when, where, and how you react — raising significant privacy concerns. The model reveals that optimizing for engagement can conflict with optimizing for user well-being.

STEM CHALLENGE GUIDANCE:
Title: Design a Music Discovery Platform
Mission: Design a music streaming system that optimizes the balance between audio quality, storage efficiency, and recommendation accuracy for a target user group.
Scenario: A startup is building a music app for students that must work on devices with limited storage (16GB) and unreliable cellular data. The app needs to store enough songs for offline listening while still delivering good sound quality and accurate recommendations. Your team must specify the compression settings, storage allocation, and recommendation algorithm approach.
Introduction: Present the challenge: A startup needs a music app that works on budget devices with 16GB storage and unreliable connectivity. Your team must specify compression formats, quality settings, storage allocation, and a recommendation approach that provides an excellent experience within severe technical constraints.

Key Concepts:
• Perceptual Coding: The mathematical technique that analyzes audio signals to identify and remove sounds that fall below human perception thresholds. It relies on psychoacoustic models derived from decades of hearing research and is the foundation of all modern lossy audio compression.
• Cold-Start Problem: The challenge of making recommendations for new users who have no listening history. Solutions include asking for initial preferences, using demographic data, or starting with popular content and rapidly adapting as the user provides implicit feedback through plays and skips.
• Adaptive Bitrate Streaming: Technology that automatically adjusts audio quality based on available network bandwidth. When connection is strong, full-quality audio streams; when connection weakens, the system seamlessly drops to lower quality to prevent buffering. This requires encoding each song at multiple quality levels.

Evaluation Rubric:
• Expert (4): Design specifies compression format with justified quality settings, addresses storage allocation with calculations, solves the cold-start problem for recommendations, and accounts for variable network conditions
• Proficient (3): Design addresses compression quality and storage with reasonable specifications and mentions recommendation approach
• Developing (2): Design identifies some technical considerations but lacks specific settings, calculations, or justified trade-offs
• Beginning (1): Design is incomplete or doesn't connect wave physics principles to digital audio technology

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a visual diagram showing the analog-to-digital conversion pipeline from microphone to compressed file
  • Use a listening comparison activity where students rate audio quality at 64kbps, 128kbps, 256kbps, and lossless
  • Sentence frames: 'Compressing at __ kbps reduces file size by __% because the algorithm removes __, which listeners __'

Extensions (Advanced Learners):
  • Research how Dolby Atmos and spatial audio encode 3D sound positioning information — what additional data is needed and how is it compressed?
  • Investigate the audiophile debate: Can trained listeners really distinguish between 320kbps MP3 and lossless FLAC? Design a double-blind test to find out.
  • Explore how deepfake audio technology uses AI to synthesize realistic speech and music — what are the ethical implications?

Cross-Curricular Connections:
  • Math: Calculate storage requirements: A 44,100 Hz sampling rate at 16-bit stereo produces how many bytes per second? Per minute? How does 10:1 compression change these numbers? How many songs fit on 64GB?
  • ELA: Write a persuasive essay arguing whether music streaming algorithms are beneficial (helping discover new music) or harmful (creating filter bubbles and reducing musical diversity)
  • Social Studies: Research how music streaming has transformed the music industry economically — who benefits and who loses when physical albums are replaced by algorithmic playlists?

CAST ALIGNMENT:
• Model how analog audio signals are digitized and compressed using wave behavior principles
• Evaluate the trade-off between audio fidelity and storage efficiency at different compression levels
• Analyze how recommendation algorithms use data patterns to predict user preferences

CAST-Style Assessment Questions:
• Multiple Choice: An uncompressed WAV file of a 3-minute song is 30MB. After MP3 compression at 128kbps, the file is 2.8MB. What percentage of the original data was removed, and why don't most listeners notice?
• Constructed Response: Using your model, explain how a music streaming service can deliver audio that sounds nearly identical to the original recording while using only 10% of the data. Connect your explanation to wave behavior, human hearing perception, and compression algorithm design.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: How Does Your Phone Fit 10,000 Songs?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. How do you think a song gets from a recording studio onto your phone?

   _________________________________________________________

   _________________________________________________________

2. What do you think happens to the sound quality when a music file is compressed to save space?

   _________________________________________________________

   _________________________________________________________

3. Draw a diagram showing how you think sound waves are converted into digital data.

   [DRAWING BOX]

4. How do you think Spotify or Apple Music knows what songs to recommend to you?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Digital Signal Processing     
___ Data Compression              
___ Sampling Rate                 
___ Recommendation Algorithm      

A. The mathematical manipulation of analog signals (like sound waves) after they've been converted to digital data — enabling compression, filtering, and enhancement of audio information
B. Algorithms that reduce file size by removing redundant or imperceptible information — lossy compression (like MP3) permanently removes data, while lossless (like FLAC) preserves all original information
C. The number of times per second an analog sound wave is measured and converted to a digital value — CD quality uses 44,100 samples per second, capturing frequencies up to 22,050 Hz
D. A computational system that analyzes patterns in user behavior data to predict preferences — Spotify's algorithm processes 100+ data points per listening session to suggest songs

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

SCENARIO: High Quality
Settings: Audio Quality: Maximum | Compression: Minimal
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Maximum Compression
Settings: Audio Quality: Standard | Compression: Maximum
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: New vs. Veteran User
Settings: Comparing algorithm with 0 vs. 10,000 hours of data
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

1. How does your model demonstrate the trade-off between file size and audio quality?

   _________________________________________________________

   _________________________________________________________

2. Why is it important that compression algorithms are based on human perception rather than pure mathematics?

   _________________________________________________________

   _________________________________________________________

3. What feedback loop drives recommendation algorithm improvement, and what are its limitations?

   _________________________________________________________

   _________________________________________________________

4. How would your model change if the target user was an audiophile versus a casual listener?

   _________________________________________________________

   _________________________________________________________

5. What ethical questions arise from algorithms that learn your preferences and influence your listening behavior?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. How does a device the size of your palm store an entire music library and somehow know what song you want to hear next? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Constructing Explanations and Designing Solutions
   □ Disciplinary Core Idea: PS4.C Information Technologies and Instrumentation / ETS1.A Defining and Delimiting Engineering Problems
   □ Crosscutting Concept: Systems and System Models

3. What ethical questions arise from algorithms that learn your preferences and influence your listening behavior?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Music Discovery Platform
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design a music streaming system that optimizes the balance between audio quality, storage efficiency, and recommendation accuracy for a target user group.

SCENARIO: A startup is building a music app for students that must work on devices with limited storage (16GB) and unreliable cellular data. The app needs to store enough songs for offline listening while still delivering good sound quality and accurate recommendations. Your team must specify the compression settings, storage allocation, and recommendation algorithm approach.

GUIDING QUESTIONS:
• What compression format and settings will you use to balance quality and storage on limited devices?
• How will your recommendation algorithm handle new users with no listening history?
• What data will you collect from users, and how does privacy factor into your design?

DESIGN THINKING:
• How much storage will you allocate for music versus app functionality and cached data?

  _________________________________________________________

• What audio quality settings will you offer and what are the trade-offs of each?

  _________________________________________________________

• How will you handle the cold-start problem when a new user has no listening data?

  _________________________________________________________

• What metrics will you use to measure whether your recommendations are actually good?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Design specifies compression format with justified quality settings, addresses storage allocation with calculations, solves the cold-start problem for recommendations, and accounts for variable network conditions
• Proficient (3): Design addresses compression quality and storage with reasonable specifications and mentions recommendation approach
• Developing (2): Design identifies some technical considerations but lacks specific settings, calculations, or justified trade-offs
• Beginning (1): Design is incomplete or doesn't connect wave physics principles to digital audio technology

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CAST-Aligned Pre/Post Assessment

### Administration Instructions

These 5 multiple-choice questions are administered identically as both a pre-assessment (before Activity 1) and a post-assessment (after Activity 4). Score each out of 5. Learning growth = post-score minus pre-score.

Questions follow the California Science Test (CAST) stimulus-response format. Each item is three-dimensional, assessing a Science and Engineering Practice (SEP), Disciplinary Core Idea (DCI), and Crosscutting Concept (CCC) simultaneously, aligned to HS-PS4-5, HS-ETS1-1.

---

### Pre-Assessment Questions

### Question 1

Sound travels through air as a wave. When a microphone captures this sound, what physical quantity does it detect?

A. Changes in air temperature caused by the sound source.
B. Variations in air pressure that correspond to the frequency and amplitude of the sound wave.
C. Electromagnetic radiation emitted by vibrating molecules.
D. The velocity of individual air molecules traveling from the source to the microphone.

Correct Answer: B

Feedback: Correct. Sound is a longitudinal pressure wave. A microphone's diaphragm responds to the alternating compressions and rarefactions of air pressure, converting them to an electrical signal. Incorrect. Sound is a mechanical pressure wave. The microphone detects pressure variations in the air that correspond to the sound's frequency (pitch) and amplitude (loudness).

---

### Question 2

A 3-minute song stored as an uncompressed audio file is approximately 30 MB. The same song compressed as an MP3 is 3 MB. What was removed during compression?

A. The lower-quality instruments in the recording.
B. Every other sound sample, cutting the data in half repeatedly.
C. Sounds and frequencies that fall below the threshold of human hearing perception.
D. The silence between notes, which takes up most of the file.

Correct Answer: C

Feedback: Correct. Lossy compression algorithms like MP3 use psychoacoustic models to identify and remove frequencies humans cannot hear, sounds masked by louder sounds, and redundant data patterns. Incorrect. MP3 compression exploits the limits of human hearing. It removes inaudible frequencies (above ~20 kHz), sounds masked by louder simultaneous sounds, and temporal details the brain fills in.

---

### Question 3

The Nyquist theorem states that to accurately capture a sound wave digitally, the sampling rate must be at least:

A. Equal to the frequency of the sound wave.
B. Twice the highest frequency to be captured.
C. Ten times the highest frequency to ensure accuracy.
D. Independent of frequency, as long as bit depth is sufficient.

Correct Answer: B

Feedback: Correct. The Nyquist theorem requires sampling at twice the maximum frequency. CD quality samples at 44,100 Hz to capture frequencies up to 22,050 Hz, exceeding the ~20,000 Hz limit of human hearing. Incorrect. The Nyquist theorem requires a sampling rate of at least twice the highest frequency in the signal. This prevents aliasing and ensures accurate digital reproduction of the analog waveform.

---

### Question 4

A music streaming service recommends songs to users. Which type of data would be MOST useful for the recommendation algorithm?

A. The user's age, gender, and geographic location.
B. Patterns of listening behavior, including play counts, skip rates, and completion rates across many users.
C. The recording quality and bit rate of each song file.
D. The number of awards each artist has won.

Correct Answer: B

Feedback: Correct. Recommendation algorithms rely on behavioral data. Play counts, skip rates, listening duration, and patterns across millions of users reveal preferences far more accurately than demographic data alone. Incorrect. Behavioral listening data (what people play, skip, repeat, and how they interact with suggestions) provides the richest signal for predicting preferences through collaborative filtering.

---

### Question 5

Which statement accurately describes the relationship between audio file size and sound quality in digital music?

A. Larger files always sound better because they contain more data.
B. There is a trade-off: higher quality requires more data, but beyond a threshold most listeners cannot detect further improvements.
C. File size has no relationship to sound quality in modern formats.
D. Smaller files sound better because compression removes noise and distortion.

Correct Answer: B

Feedback: Correct. Higher bit rates and sampling rates capture more audio detail, but human hearing has limits. Above approximately 256 kbps, most listeners cannot distinguish compressed from uncompressed audio in blind tests. Incorrect. There is a direct trade-off between file size and quality, but it has a perceptual ceiling. Beyond a certain quality level, the human auditory system cannot detect further improvements.

---

### Post-Assessment Questions

### Question 1

The model shows that at maximum Data Compression Rate, audio quality degrades noticeably. At moderate compression, quality is virtually indistinguishable from the original. What concept from wave physics explains why moderate compression works without perceptible quality loss?

A. Destructive interference cancels out the removed frequencies.
B. Psychoacoustic masking means louder sounds hide quieter sounds from perception, so removing the masked sounds is undetectable.
C. The human ear processes all frequencies equally, so removing some has minimal impact.
D. Compression algorithms add synthetic frequencies to replace removed data.

Correct Answer: B

Feedback: Correct. Psychoacoustic masking is a property of human hearing where loud sounds render quieter nearby sounds imperceptible. Compression algorithms exploit this by removing masked data that the listener would never perceive. Incorrect. The model demonstrates that compression works because of psychoacoustic masking. Human hearing naturally suppresses perception of sounds masked by louder sounds, making their removal undetectable.

---

### Question 2

In the model, a new user with no listening history receives recommendations with approximately 20-30% accuracy, while a veteran user with 1,000+ hours has 70-80% accuracy. What system behavior does this demonstrate?

A. Linear growth, where accuracy improves at a constant rate with each hour of listening.
B. A positive feedback loop, where engagement generates data that improves predictions, which increases engagement and generates more data.
C. Random variation, where accuracy fluctuates unpredictably regardless of data quantity.
D. Diminishing returns, where additional data beyond the first hour provides no benefit.

Correct Answer: B

Feedback: Correct. The model reveals a positive feedback loop: more listening generates more behavioral data, which trains better algorithms, which provide better recommendations, which increases engagement and data generation. Incorrect. The model demonstrates a feedback loop: engagement produces data, data improves algorithm accuracy, better accuracy increases user satisfaction and engagement, generating more data.

---

### Question 3

A student examines the model and notices that a 64 GB device stores approximately 1,200 songs at maximum quality but 12,000 songs at standard compression. The student argues that maximum compression should always be used. Which model evidence challenges this argument?

A. Maximum compression makes files too small for the device to read efficiently.
B. Beyond a critical compression threshold, audio quality degrades enough that user engagement decreases, reducing the effectiveness of recommendation algorithms.
C. Maximum compression takes too long to process on mobile devices.
D. The model shows that all compression levels produce identical listening experiences.

Correct Answer: B

Feedback: Correct. The model shows that excessive compression degrades quality, which reduces user engagement, which decreases the data feeding the recommendation algorithm. The system optimizes for a balance, not a single variable. Incorrect. The model demonstrates that compression exists on a curve with diminishing returns. Beyond the perception threshold, further compression degrades quality enough to reduce engagement, harming the entire system.

---

### Question 4

Based on the model, which statement best explains why digital music storage became practical for portable devices?

A. Storage devices became large enough to hold uncompressed audio files.
B. Engineers discovered that the physics of human hearing perception could be exploited to reduce file sizes by 90% without perceptible quality loss.
C. Music quality standards were lowered to accommodate smaller storage.
D. Digital signals are inherently smaller than analog signals.

Correct Answer: B

Feedback: Correct. The model shows that psychoacoustic compression, based on wave physics and human hearing limits, enables 90% data reduction while maintaining perceptually identical quality, making portable music libraries possible. Incorrect. The breakthrough was understanding that human hearing has specific limitations (frequency range, masking effects) that compression algorithms can exploit to dramatically reduce file sizes without perceptible quality loss.

---

### Question 5

The model demonstrates that algorithm accuracy improves from 20% to 80% as listening data increases. A privacy advocate argues that less data should be collected. Using the model, which design approach best addresses both accuracy and privacy concerns?

A. Collect all possible data since accuracy is the only goal.
B. Collect no data and rely on random recommendations.
C. Identify the minimum data points needed to reach acceptable accuracy, and collect only those, transparently disclosing what is collected and why.
D. The model proves privacy and accuracy are completely incompatible goals.

Correct Answer: C

Feedback: Correct. The model shows diminishing returns in accuracy with additional data. Engineering solutions can identify the optimal data collection level that achieves acceptable accuracy while minimizing privacy intrusion. Incorrect. The model shows diminishing returns in the data-accuracy relationship. This means a balance point exists where sufficient accuracy is achieved with limited, transparent data collection.

---

### Answer Key

**Pre-Assessment:**
Question 1: B
Question 2: C
Question 3: B
Question 4: B
Question 5: B

**Post-Assessment:**
Question 1: B
Question 2: B
Question 3: B
Question 4: B
Question 5: C

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-10/G10L1-L04/G10L1-L04-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-10/G10L1-L04/G10L1-L04-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-10/G10L1-L04/G10L1-L04-Student-Presentation.pptx] |
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