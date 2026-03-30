# Lesson: How Does 5G Actually Work?

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G10L2-L06 |
| **Grade** | 10th Grade — Level 2: Systems Under Pressure |
| **Lesson Name** | How Does 5G Actually Work? |
| **Status** | Template |

---

## Platform

### Title
**How Does 5G Actually Work? — Modeling Electromagnetic Wave Behavior in Wireless Communication Networks**

### Overview
Every time you stream a video, send a text, or scroll social media, you're using electromagnetic waves traveling at the speed of light between your device and a cell tower. The evolution from 4G to 5G represents a fundamental shift in which electromagnetic frequencies we use — and understanding why higher frequencies mean faster speeds but shorter range reveals the core physics of wireless communication. Students investigate the driving question: Why does 5G promise lightning-fast internet but struggle to work through walls — and what trade-offs did engineers have to make? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of a modern cityscape with visible electromagnetic wave patterns emanating from small cell towers on building tops and light poles, showing how waves interact with buildings and obstacles, futuristic visualization with blue and purple wave graphics overlaid on realistic urban architecture]

### Grade
10th Grade — Level 2: Systems Under Pressure

### NGSS Standard
**HS-PS4-2, HS-PS4-3**: Evaluate questions about the advantages of using digital transmission and storage of information. Evaluate the claims, evidence, and reasoning behind the idea that electromagnetic radiation can be described either by a wave model or a particle model.

### Learning Objectives
- Model how signal frequency, wave penetration, and tower density interact to determine wireless network performance
- Analyze the fundamental trade-off between data transfer rate and signal penetration in electromagnetic wave communication
- Predict how interference, absorption, and network capacity change as frequency increases from 4G to 5G ranges
- Evaluate the engineering compromises required to build a high-speed, wide-coverage wireless network

### Component List (Starting Model: 7 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Signal Frequency | External | The frequency of electromagnetic waves used for data transmission — higher frequencies (millimeter wave) carry more data but are absorbed more easily by obstacles and atmosphere |
| Wave Penetration | Internal | The ability of electromagnetic waves to pass through solid materials like walls, glass, and vegetation — inversely related to frequency, with higher frequencies being blocked more easily |
| Data Transfer Rate | Internal | The volume of digital information that can be transmitted per second, measured in megabits or gigabits per second — directly proportional to bandwidth, which increases with signal frequency |
| Tower Density | External | The number of cell towers or small cells per square kilometer needed to maintain coverage — must increase dramatically as frequency increases because each tower covers a smaller area |
| Interference Level | Internal | The degree to which signals from neighboring towers, devices, and environmental reflections degrade signal quality, requiring error correction and reducing effective throughput |
| Energy Absorption | Internal | The rate at which electromagnetic energy is absorbed by atmospheric gases, water vapor, building materials, vegetation, and human tissue as signals propagate from tower to device |
| Network Capacity | Internal | The total volume of data that can be simultaneously served to all users in a coverage area, determined by the interaction of frequency, tower density, MIMO technology, and interference management |

### Research for Lesson
- The Electromagnetic Spectrum and Data — reference materials and textbook resources
- The Penetration Problem — reference materials and textbook resources
- Small Cells and Densification — reference materials and textbook resources
- The Layered Solution — reference materials and textbook resources

---

## Step 1: LOCATE — Build Your System

### Text Editor

```
HOW DOES 5G ACTUALLY WORK?

Modeling Electromagnetic Wave Behavior in Wireless Communication Networks.
Why does 5G promise lightning-fast internet but struggle to work through walls — and what trade-offs did engineers have to make?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Signal Frequency" — the frequency of electromagnetic waves used for data transmission — higher frequencies (millimeter wave) carry more data but are absorbed more easily by obstacles and atmosphere
  ○ Click "Tower Density" — the number of cell towers or small cells per square kilometer needed to maintain coverage — must increase dramatically as frequency increases because each tower covers a smaller area
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Wave Penetration" — the ability of electromagnetic waves to pass through solid materials like walls
  ○ Click "Data Transfer Rate" — the volume of digital information that can be transmitted per second
  ○ Click "Interference Level" — the degree to which signals from neighboring towers
  ○ Click "Energy Absorption" — the rate at which electromagnetic energy is absorbed by atmospheric gases
  ○ Click "Network Capacity" — the total volume of data that can be simultaneously served to all users in a coverage area

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
"Why does 5G promise lightning-fast internet but struggle to work through walls — and what trade-offs did engineers have to make?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Signal Frequency' — that's external. The frequency of electromagnetic waves used for data transmission — higher frequencies (millimeter wave) carry more data but are absorbed more easily by obstacles and atmosphere.
Click on 'Wave Penetration' — that's internal. The ability of electromagnetic waves to pass through solid materials like walls.
Click on 'Data Transfer Rate' — that's internal. The volume of digital information that can be transmitted per second.
Click on 'Tower Density' — that's external. The number of cell towers or small cells per square kilometer needed to maintain coverage — must increase dramatically as frequency increases because each tower covers a smaller area.
Click on 'Interference Level' — that's internal. The degree to which signals from neighboring towers.
Click on 'Energy Absorption' — that's internal. The rate at which electromagnetic energy is absorbed by atmospheric gases.
Click on 'Network Capacity' — that's internal. The total volume of data that can be simultaneously served to all users in a coverage area.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Signal Frequency and Tower Density are external components because they represent deliberate engineering decisions made by network designers — choosing which electromagnetic frequencies to use and how many cell towers to deploy. Wave Penetration, Data Transfer Rate, Interference Level, Energy Absorption, and Network Capacity are internal because they are physical consequences determined by the laws of electromagnetic wave propagation interacting with the chosen frequency and infrastructure density.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next step, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 7 components sorted: Signal Frequency, Tower Density (External), Wave Penetration, Data Transfer Rate, Interference Level, Energy Absorption, Network Capacity (Internal)]

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
• Click on "Signal Frequency" and drag an arrow to "Data Transfer Rate"
• Click on "Signal Frequency" and drag an arrow to "Wave Penetration"
• Click on "Tower Density" and drag an arrow to "Interference Level"

Task C: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Signal Frequency → Data Transfer Rate = POSITIVE (+)
    Higher Signal Frequency allows wider bandwidth channels, which can carry proportionally more data per second. Doubling the frequency roughly doubles the available bandwidth and data capacity.

  ○ Signal Frequency → Wave Penetration = NEGATIVE (−)
    Higher Signal Frequency produces shorter wavelengths that interact more strongly with building materials, vegetation, and atmospheric particles. Millimeter waves at 28 GHz lose 99.99% of energy through a concrete wall, while 700 MHz signals pass with moderate attenuation.

  ○ Tower Density → Interference Level = POSITIVE (+)
    Higher Tower Density means more overlapping signals in the same geographic area. Without sophisticated interference management (beamforming, MIMO), signals from adjacent cells degrade each other, reducing effective Data Transfer Rate and Network Capacity.

Task D: CHECK YOUR MODEL
• You should have 3 arrows total
• 1 negative relationship(s), 2 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: When Signal Frequency increases to millimeter wave ranges, Data Transfer Rate skyrockets — but Wave Penetration collapses and Energy Absorption increases. Tower Density must increase enormously to compensate. How do engineers balance this fundamental trade-off between speed and coverage?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Signal Frequency' and drag an arrow
over to 'Data Transfer Rate.'

Here's the key question: When signal frequency goes UP, does
data transfer rate go UP or DOWN?

Higher Signal Frequency allows wider bandwidth channels, which can carry proportionally more data per second. Doubling the frequency roughly doubles the available bandwidth and data capacity.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Signal Frequency' and drag an arrow
over to 'Wave Penetration.'

Here's the key question: When signal frequency goes UP, does
wave penetration go UP or DOWN?

Higher Signal Frequency produces shorter wavelengths that interact more strongly with building materials, vegetation, and atmospheric particles. Millimeter waves at 28 GHz lose 99.99% of energy through a concrete wall, while 700 MHz signals pass with moderate attenuation.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Last connection: Click on 'Tower Density' and drag an arrow
over to 'Interference Level.'

Here's the key question: When tower density goes UP, does
interference level go UP or DOWN?

Higher Tower Density means more overlapping signals in the same geographic area. Without sophisticated interference management (beamforming, MIMO), signals from adjacent cells degrade each other, reducing effective Data Transfer Rate and Network Capacity.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Look at your model now. You've got 1 negative and 2
positive relationships. 3 arrows total.

When Signal Frequency increases to millimeter wave ranges, Data Transfer Rate skyrockets — but Wave Penetration collapses and Energy Absorption increases. Tower Density must increase enormously to compensate. How do engineers balance this fundamental trade-off between speed and coverage?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Signal Frequency +→ Data Transfer Rate, Signal Frequency −→ Wave Penetration, Tower Density +→ Interference Level]

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
• When Signal Frequency is HIGH, what happens to the internal components?

Task C: SCENARIO — 4G STANDARD
• Low frequency, wide coverage
• PREDICT FIRST: What do you predict happens to Wave Penetration and Tower Density when operating at 700 MHz?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task D: SCENARIO — 5G MILLIMETER WAVE
• High frequency, narrow coverage
• PREDICT FIRST: What do you predict happens to Data Transfer Rate and Wave Penetration when frequency jumps to 28 GHz?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task E: SCENARIO — 5G MID-BAND
• Medium frequency, balanced approach
• PREDICT FIRST: Do you predict the mid-band compromise provides enough speed improvement while maintaining reasonable coverage?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• There is a fundamental physics trade-off in wireless communication: higher frequencies carry more data but penetrate materials less effectively and are absorbed more by the atmosphere
• 5G millimeter wave delivers extraordinary data rates (10+ Gbps) but requires a massive increase in Tower Density because each cell covers only 200-300 meters versus 2-5 kilometers for 4G
• Interference Level increases with Tower Density, requiring sophisticated beamforming and MIMO technology to direct signals precisely and manage overlapping coverage
• The 'best' 5G solution is actually a layered network using multiple frequency bands — low-band for wide coverage, mid-band for urban areas, and millimeter wave for dense hotspots

THE ANSWER: 5G works by transmitting data on higher electromagnetic frequencies than 4G — up to 28-39 GHz (millimeter wave) compared to 4G's 700 MHz to 2.5 GHz. Higher frequencies carry vastly more data because bandwidth is proportional to frequency. But physics creates an inescapable trade-off: as frequency increases, electromagnetic waves are increasingly blocked by walls, trees, glass, rain, and even human bodies. A 28 GHz signal loses 98% of its energy passing through a single brick wall. This means 5G millimeter wave requires a cell tower (or small cell) every 200-300 meters instead of every 2-5 kilometers. The engineering solution is a layered network: low-band 5G for wide coverage, mid-band for cities, and millimeter wave for stadiums, airports, and dense urban areas where demand is highest.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: 4G Standard. Low frequency, wide coverage.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: 5G Millimeter Wave.
High frequency, narrow coverage.

Before you run it — make a prediction. What do you predict happens to Data Transfer Rate and Wave Penetration when frequency jumps to 28 GHz?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: 5G Mid-Band. Medium frequency, balanced approach.
Do you predict the mid-band compromise provides enough speed improvement while maintaining reasonable coverage?

Here's what our model reveals: 5G works by transmitting data on higher electromagnetic frequencies than 4G — up to 28-39 GHz (millimeter wave) compared to 4G's 700 MHz to 2.5 GHz. Higher frequencies carry vastly more data because bandwidth is proportional to frequency. But physics creates an inescapable trade-off: as frequency increases, electromagnetic waves are increasingly blocked by walls, trees, glass, rain, and even human bodies. A 28 GHz signal loses 98% of its energy passing through a single brick wall. This means 5G millimeter wave requires a cell tower (or small cell) every 200-300 meters instead of every 2-5 kilometers. The engineering solution is a layered network: low-band 5G for wide coverage, mid-band for cities, and millimeter wave for stadiums, airports, and dense urban areas where demand is highest.

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
   • What happens if you turn OFF Signal Frequency?
   • What happens if you turn OFF Tower Density?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Beamforming Precision — The ability of MIMO antenna arrays to focus electromagnetic energy into narrow beams directed at specific users, improving signal-to-noise ratio and allowing multiple users to share the same frequency without interference
   • Weather Impact — The effect of rain, snow, humidity, and atmospheric conditions on signal propagation — millimeter waves are particularly susceptible to rain fade, where water droplets absorb and scatter the signal
   • Latency — The time delay between transmitting and receiving a signal, measured in milliseconds — 5G promises 1ms latency versus 30-50ms for 4G, enabling real-time applications like autonomous vehicles and remote surgery

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • The Electromagnetic Spectrum and Data — how does this connect to your model?
   • The Penetration Problem — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model demonstrate the fundamental trade-off between data speed and signal penetration in electromagnetic communication?
   • Why does increasing Signal Frequency require such a dramatic increase in Tower Density — what does this reveal about wave physics?
   • What does your model suggest about why 5G networks use multiple frequency bands instead of one?
   • How does Interference Level change as Tower Density increases, and what engineering solutions address this challenge?

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

Beamforming Precision. The ability of MIMO antenna arrays to focus electromagnetic energy into narrow beams directed at specific users, improving signal-to-noise ratio and allowing multiple users to share the same frequency without interference
How would you model that?

Weather Impact. The effect of rain, snow, humidity, and atmospheric conditions on signal propagation — millimeter waves are particularly susceptible to rain fade, where water droplets absorb and scatter the signal
How would you model that?

Latency. The time delay between transmitting and receiving a signal, measured in milliseconds — 5G promises 1ms latency versus 30-50ms for 4G, enabling real-time applications like autonomous vehicles and remote surgery
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

RF Engineers (Radio Frequency Engineers) design wireless communication systems, optimizing antenna placement, frequency selection, and interference management. They work for telecom companies, tech firms, and government agencies, earning $80,000–$150,000/year. Network Architects who design large-scale wireless infrastructure earn $100,000–$180,000/year.

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
Visual: Title slide with futuristic 5G cityscape visualization
Say: "5G promises to download a movie in three seconds. But walk behind a wall and the signal vanishes. Why? The answer is pure physics."
Do: Demo: If possible, compare signal strength between 4G and 5G in the classroom using a signal strength app. If not, show a signal propagation comparison video.
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and vocabulary terms
Say: "Today you're learning the physics behind every text, every stream, every download — and why engineers had to make painful trade-offs to give you faster internet."
Do: Have students read objectives. Pre-teach 'millimeter wave' and 'signal attenuation.' Quick-write: Why do you think 5G is faster than 4G?
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: Why does 5G struggle to work through walls?
Say: "You'd think faster internet is just about better technology. But it's actually about physics — and physics doesn't negotiate."
Do: Students guess: What happens when you double the frequency of a wave? What happens to its ability to go through walls? Collect hypotheses.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps overview
Say: "We're going to model the electromagnetic physics behind wireless networks — and discover why engineers have to compromise between speed and coverage."
Do: Preview each LEVER step. Emphasize that this is about the physics of electromagnetic waves interacting with matter.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Seven component cards for wireless network model
Say: "Two things the engineers choose: what frequency to broadcast on and how many towers to build. Physics determines the rest."
Do: Guide component sorting. Discuss why Signal Frequency and Tower Density are external (engineering choices) while Wave Penetration and Energy Absorption are governed by physics.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows between network components
Say: "When you crank up the frequency for more speed, what chain reaction ripples through every other component of the network?"
Do: Help students trace the trade-off cascade: higher frequency means more data but less penetration, requiring more towers, creating more interference. Find the balance points.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Graph predictions and simulation results for three frequency bands
Say: "Let's compare 4G, 5G mid-band, and 5G millimeter wave. Same city, same users, completely different physics."
Do: Students predict outcomes for each frequency band. Run simulations. Compare tower counts, coverage gaps, and data speeds side by side.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key findings from model exploration
Say: "Now you know why there's no perfect wireless solution — only trade-offs. The real genius of 5G is using ALL the frequencies and switching between them."
Do: Lead discussion on the layered network approach. Connect model findings to students' real experience with cell signal variability.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Campus 5G network design challenge
Say: "Your school just got funding for a 5G network. Design it. Where do the antennas go? What frequencies do you use? And what happens during the school assembly?"
Do: Groups design campus networks using model data. Must specify antenna locations, frequency bands, and capacity for high-density events. Present as engineering proposals.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: How Does 5G Actually Work?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
Every time you stream a video, send a text, or scroll social media, you're using electromagnetic waves traveling at the speed of light between your device and a cell tower. The evolution from 4G to 5G represents a fundamental shift in which electromagnetic frequencies we use — and understanding why higher frequencies mean faster speeds but shorter range reveals the core physics of wireless communication.

NGSS ALIGNMENT:
HS-PS4-2, HS-PS4-3: Evaluate questions about the advantages of using digital transmission and storage of information. Evaluate the claims, evidence, and reasoning behind the idea that electromagnetic radiation can be described either by a wave model or a particle model.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Evaluating Claims and Evidence
  Students evaluate claims about 5G performance by building computational models that reveal the physics-based trade-offs between frequency, penetration, and coverage.
• Disciplinary Core Idea: PS4.A Wave Properties / PS4.C Information Technologies and Instrumentation
  Electromagnetic waves transport energy and information; wave frequency determines both data capacity and interaction with matter, creating fundamental engineering trade-offs.
• Crosscutting Concept: Structure and Function
  Students analyze how the physical structure of electromagnetic waves (frequency, wavelength) determines their functional properties (data capacity, penetration, absorption) and constrains network design.

PACING GUIDE:
• Step 1 (Locate): 8-10 minutes
• Step 2 (Establish): 8-10 minutes
• Step 3 (Visualize & Evaluate): 10-12 minutes
• Step 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Millimeter Wave, Signal Attenuation, MIMO Antenna Array, Beamforming
□ Prepare Why does 5G promise lightning-fast internet but struggle to work through walls — and what trade-offs did engineers have to make discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify seven components of the 5G network system: Signal Frequency, Wave Penetration, Data Transfer Rate, Tower Density, Interference Level, Energy Absorption, and Network Capacity — with Signal Frequency and Tower Density as external engineering choices.
• Establish: Students determine that increasing Signal Frequency dramatically increases Data Transfer Rate but decreases Wave Penetration and increases Energy Absorption. This forces higher Tower Density, which increases Interference Level. Net Network Capacity depends on balancing all these trade-offs.
• Visualize: Students build a computational model showing how frequency selection cascades through all network parameters, revealing the fundamental physics trade-off in wireless communication.
• Evaluate: Students run 4G standard, 5G millimeter wave, and 5G mid-band scenarios to compare data speed, coverage area, and infrastructure requirements for each frequency strategy.
• Revise: Students add Beamforming Precision, Weather Impact, or Latency to explore how advanced antenna technology and environmental conditions affect network performance.

BACKGROUND CONTENT:
• The Electromagnetic Spectrum and Data:
  All wireless communication uses electromagnetic waves — the same fundamental phenomenon as visible light, radio waves, and X-rays, differing only in frequency. Data is encoded by modulating the wave's amplitude, frequency, or phase. The amount of data a wave can carry is directly proportional to its bandwidth (the range of frequencies used). Higher carrier frequencies allow wider bandwidths. A 28 GHz millimeter wave channel can be 400 MHz wide (carrying 10+ Gbps), while a 700 MHz 4G channel is typically 20 MHz wide (carrying 100 Mbps). This is why 5G is faster — it uses higher frequencies with wider channels.

• The Penetration Problem:
  Electromagnetic waves interact with matter in frequency-dependent ways. Low-frequency waves (700 MHz, wavelength ~43 cm) can diffract around obstacles and penetrate building materials with moderate loss. High-frequency millimeter waves (28 GHz, wavelength ~1 cm) are absorbed and reflected by most solid materials. A 28 GHz signal loses approximately 40 dB passing through a concrete wall — that's 99.99% energy loss. Even glass windows, tree foliage, and rain attenuate millimeter waves significantly. This is a consequence of the wave's wavelength being similar in size to common obstacles, maximizing interaction.

• Small Cells and Densification:
  Because millimeter wave signals cover only 200-300 meters (versus 2-5 km for 4G), 5G requires network densification — deploying many small cell antennas on light poles, building facades, and utility poles rather than relying on a few large towers. A single city block might need 4-6 small cells for millimeter wave coverage. This creates challenges: more antennas mean more interference between cells, more power consumption, more installation costs, and more community resistance to antenna proliferation.

• The Layered Solution:
  Real 5G networks don't use one frequency — they layer three bands. Low-band (600-900 MHz) provides wide coverage similar to 4G with modest speed improvements. Mid-band (2.5-6 GHz) offers a balance of coverage and speed for urban areas — this is where most users experience 5G. Millimeter wave (24-100 GHz) provides extreme speed in dense locations like stadiums, airports, and downtown areas. Your phone automatically switches between bands based on availability. This layered approach is an engineering compromise that maximizes the strengths of each frequency range.

COMMON MISCONCEPTIONS:
• "5G is dangerous to human health"
  Reality: 5G uses non-ionizing electromagnetic radiation — the same fundamental type as FM radio, Wi-Fi, and visible light. Non-ionizing radiation does not have enough energy per photon to break chemical bonds or damage DNA. The frequencies used by 5G (up to 39 GHz) are far below the ionizing threshold (approximately 3,000,000 GHz for UV light). Decades of research have found no confirmed health effects from non-ionizing radiation at the power levels used by cell networks.
  Strategy: Calculate: Compare the photon energy of a 28 GHz 5G signal to a 500,000 GHz visible light photon. Visible light is 18,000 times more energetic per photon — and we evolved under constant visible light exposure.

• "5G is just faster 4G"
  Reality: 5G is not simply 4G with higher speeds — it represents a fundamental architectural change in wireless networks. 5G introduces network slicing (dedicating virtual network segments to different applications), massive MIMO (hundreds of antennas per tower), edge computing (processing data near the user rather than in distant data centers), and ultra-low latency (1ms vs 30-50ms). These capabilities enable entirely new applications like autonomous vehicles, remote surgery, and industrial automation that were impossible on 4G.
  Strategy: Analogy: 4G is like a highway — it can carry more or fewer cars. 5G is like redesigning the entire transportation system with highways, railways, bike lanes, and air taxis, each optimized for different needs.

• "Higher frequency always means better performance"
  Reality: The model demonstrates that higher frequency increases data rate but simultaneously decreases coverage area, increases infrastructure costs, and introduces vulnerability to weather and obstacles. There is no universally 'better' frequency — each range offers different trade-offs. The optimal frequency depends on the specific use case: low-band for rural coverage, mid-band for suburban areas, and millimeter wave for dense urban hotspots.
  Strategy: Test it: Ask students whether they'd rather have extremely fast internet that works only outdoors within 200 meters of a tower, or moderately fast internet that works everywhere including inside buildings. Neither answer is 'wrong' — it depends on the use case.

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
Big Question: Why does 5G promise lightning-fast internet but struggle to work through walls — and what trade-offs did engineers have to make?
Answer: 5G works by transmitting data on higher electromagnetic frequencies than 4G — up to 28-39 GHz (millimeter wave) compared to 4G's 700 MHz to 2.5 GHz. Higher frequencies carry vastly more data because bandwidth is proportional to frequency. But physics creates an inescapable trade-off: as frequency increases, electromagnetic waves are increasingly blocked by walls, trees, glass, rain, and even human bodies. A 28 GHz signal loses 98% of its energy passing through a single brick wall. This means 5G millimeter wave requires a cell tower (or small cell) every 200-300 meters instead of every 2-5 kilometers. The engineering solution is a layered network: low-band 5G for wide coverage, mid-band for cities, and millimeter wave for stadiums, airports, and dense urban areas where demand is highest.

Simulation Answers:
• 4G Standard Scenario: At 700 MHz, Wave Penetration is high — signals easily pass through walls and travel 2-5 km from towers. Tower Density can be low, keeping infrastructure costs manageable. But Data Transfer Rate is limited by the narrow bandwidth available at low frequencies — typically 50-100 Mbps peak. Network Capacity is adequate for current demand but insufficient for future bandwidth-intensive applications.
• 5G Millimeter Wave Scenario: At 28 GHz, Data Transfer Rate skyrockets to 10+ Gbps — fast enough to download a full movie in seconds. But Wave Penetration collapses: signals cannot pass through walls, are blocked by trees, and are attenuated by rain. Each cell covers only 200-300 meters, requiring enormous Tower Density. Interference Level becomes a major challenge requiring advanced beamforming. Network Capacity is extraordinary within coverage areas but coverage gaps are pervasive.

Reflection Exemplars:
• Q: Why can't engineers just use the highest frequency?
  A: The model reveals a fundamental physics constraint: electromagnetic wave penetration decreases as frequency increases. This isn't an engineering limitation that can be overcome with better technology — it's a property of how electromagnetic waves interact with matter at the atomic level. Higher-frequency waves have shorter wavelengths that match the size of common obstacles (walls, rain drops, leaves), maximizing absorption and scattering. Engineers must work within these physics constraints, which is why the solution is a layered network using multiple frequencies rather than one 'best' frequency.
• Q: How does the 5G trade-off relate to the electromagnetic spectrum?
  A: The model demonstrates a universal principle: every region of the electromagnetic spectrum has trade-offs. Radio waves penetrate walls but carry little data. Microwaves carry more data but are partially blocked. Millimeter waves carry enormous data but are blocked by almost everything. X-rays penetrate everything but are too energetic for communication. This trade-off is fundamental to wave physics — there is no frequency that combines high data capacity with high penetration. The engineering challenge is designing systems that navigate this constraint.

STEM CHALLENGE GUIDANCE:
Title: Design a Campus 5G Network
Mission: Design the placement and frequency strategy for a 5G network covering a school campus, optimizing for both coverage and capacity while managing interference.
Scenario: Your school district is deploying a 5G network across campus to support 2,000 simultaneous device connections for digital learning. The network must work inside classrooms, in outdoor spaces, and in the auditorium during events. Your team has been hired to design the antenna placement and frequency strategy.
Introduction: Present the challenge: Your school is deploying a 5G network for 2,000 students. Design the antenna placement and frequency strategy that provides coverage in classrooms, outdoor spaces, and the auditorium — using your model data to justify every engineering decision.

Key Concepts:
• Coverage Mapping: Network engineers create coverage maps showing signal strength at every point in the target area, accounting for building materials, terrain, and antenna characteristics. Dead zones — areas with insufficient signal — must be identified and addressed with additional antennas or frequency adjustments.
• Capacity Planning: Networks must handle peak demand, not just average demand. A school assembly with 2,000 devices in one room requires vastly more capacity than normal distributed usage. Capacity planning uses traffic models to predict demand patterns and ensure the network can handle worst-case scenarios.
• Cost-Benefit Analysis: Every additional antenna improves coverage but increases cost. Engineers must optimize the trade-off between network performance and budget. Millimeter wave small cells cost $10,000-$30,000 each including installation, so placement must be strategic, not blanket coverage.

Evaluation Rubric:
• Expert (4): Network design uses multiple frequency bands strategically, includes coverage maps with dead zone analysis, accounts for peak capacity scenarios, optimizes antenna placement using model data, and includes cost estimate
• Proficient (3): Network design includes reasonable antenna placement and frequency selection with some model-based justification for coverage decisions
• Developing (2): Network design includes antenna placement but lacks frequency strategy, coverage analysis, or capacity planning
• Beginning (1): Network design is incomplete or does not connect antenna placement to electromagnetic wave physics

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a simplified campus map showing building outlines, wall materials, and key gathering areas for students to plan antenna placement
  • Use a frequency-penetration chart showing signal loss through common materials (drywall, concrete, glass, vegetation) at different frequencies
  • Sentence frames: 'At __ GHz, the signal can/cannot penetrate __ because __, so we need to place antennas at __ to ensure coverage'

Extensions (Advanced Learners):
  • Research how 5G millimeter wave technology is being used in fixed wireless access to provide home internet without cable, and model whether this could replace fiber optic connections
  • Investigate the physics of beamforming — how antenna arrays create focused beams — and explain why this technology is essential for making millimeter wave 5G practical
  • Compare the electromagnetic frequency allocations used by different countries for 5G and analyze why spectrum policy is a matter of national economic competition

Cross-Curricular Connections:
  • Math: Calculate the number of small cells needed to provide millimeter wave coverage to a 10 square kilometer urban area, accounting for 200-meter cell radius and 15% overlap for handoff zones
  • ELA: Evaluate competing claims about 5G health effects by analyzing the scientific evidence, electromagnetic energy levels, and the difference between ionizing and non-ionizing radiation
  • Social Studies: Research the digital divide — how unequal access to high-speed internet affects educational and economic opportunity — and analyze whether 5G will narrow or widen this gap

CAST ALIGNMENT:
• Model how electromagnetic wave frequency determines the trade-off between data transfer rate and signal penetration
• Analyze the engineering compromises in 5G network design between coverage area, capacity, and infrastructure cost
• Evaluate claims about 5G performance using computational model evidence

CAST-Style Assessment Questions:
• Multiple Choice: A 5G tower using 28 GHz millimeter wave covers approximately 200 meters, while a 4G tower at 700 MHz covers 5 kilometers. Based on your model, how many 5G small cells would be needed to replace one 4G tower's coverage area?
• Constructed Response: Using your model, explain why 5G promises much faster speeds than 4G but requires dramatically more cell towers. Reference the relationship between Signal Frequency, Wave Penetration, Data Transfer Rate, and Tower Density in your explanation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: How Does 5G Actually Work?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. What do you think makes 5G different from 4G — and why is it faster?

   _________________________________________________________

   _________________________________________________________

2. Why do you think your phone signal gets worse inside certain buildings?

   _________________________________________________________

   _________________________________________________________

3. Draw a diagram showing how you think a signal travels from a cell tower to your phone.

   [DRAWING BOX]

4. What trade-offs do you think engineers have to make when designing a wireless network?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Millimeter Wave               
___ Signal Attenuation            
___ MIMO Antenna Array            
___ Beamforming                   

A. Electromagnetic waves with frequencies between 30 GHz and 300 GHz, corresponding to wavelengths of 1-10 millimeters — 5G uses these frequencies for their enormous data capacity but they are easily blocked by buildings, trees, and even rain
B. The reduction in electromagnetic signal strength as it travels through space, caused by distance (inverse square law), absorption by materials, atmospheric scattering, and interference from other signals
C. Multiple-Input Multiple-Output technology that uses dozens or hundreds of small antennas to simultaneously transmit and receive multiple data streams, dramatically increasing network capacity and reliability
D. A signal processing technique that focuses electromagnetic energy into narrow, directed beams aimed at specific users rather than broadcasting in all directions, improving signal strength and reducing interference

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

SCENARIO: 4G Standard
Settings: Low frequency, wide coverage
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: 5G Millimeter Wave
Settings: High frequency, narrow coverage
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: 5G Mid-Band
Settings: Medium frequency, balanced approach
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

1. How does your model demonstrate the fundamental trade-off between data speed and signal penetration in electromagnetic communication?

   _________________________________________________________

   _________________________________________________________

2. Why does increasing Signal Frequency require such a dramatic increase in Tower Density — what does this reveal about wave physics?

   _________________________________________________________

   _________________________________________________________

3. What does your model suggest about why 5G networks use multiple frequency bands instead of one?

   _________________________________________________________

   _________________________________________________________

4. How does Interference Level change as Tower Density increases, and what engineering solutions address this challenge?

   _________________________________________________________

   _________________________________________________________

5. What are the limitations of modeling wireless network behavior with only seven components when real networks involve terrain, weather, and thousands of simultaneous users?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Why does 5G promise lightning-fast internet but struggle to work through walls — and what trade-offs did engineers have to make? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Evaluating Claims and Evidence
   □ Disciplinary Core Idea: PS4.A Wave Properties / PS4.C Information Technologies and Instrumentation
   □ Crosscutting Concept: Structure and Function

3. What are the limitations of modeling wireless network behavior with only seven components when real networks involve terrain, weather, and thousands of simultaneous users?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Campus 5G Network
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design the placement and frequency strategy for a 5G network covering a school campus, optimizing for both coverage and capacity while managing interference.

SCENARIO: Your school district is deploying a 5G network across campus to support 2,000 simultaneous device connections for digital learning. The network must work inside classrooms, in outdoor spaces, and in the auditorium during events. Your team has been hired to design the antenna placement and frequency strategy.

GUIDING QUESTIONS:
• Which areas of campus need millimeter wave coverage (high density) versus mid-band coverage (general use)?
• How will you ensure signal penetrates into classrooms through walls and windows?
• What happens to your network during a school assembly when 2,000 devices are in one room?

DESIGN THINKING:
• Where would you place small cells for millimeter wave coverage and macro cells for wide coverage?

  _________________________________________________________

• How would you use beamforming to direct signals to classroom areas without creating dead zones?

  _________________________________________________________

• What frequency mix would balance speed, coverage, and cost for the campus budget?

  _________________________________________________________

• How would you test your network design before installation using your model data?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Network design uses multiple frequency bands strategically, includes coverage maps with dead zone analysis, accounts for peak capacity scenarios, optimizes antenna placement using model data, and includes cost estimate
• Proficient (3): Network design includes reasonable antenna placement and frequency selection with some model-based justification for coverage decisions
• Developing (2): Network design includes antenna placement but lacks frequency strategy, coverage analysis, or capacity planning
• Beginning (1): Network design is incomplete or does not connect antenna placement to electromagnetic wave physics

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CAST-Aligned Pre/Post Assessment

### Administration Instructions

These 5 multiple-choice questions are administered identically as both a pre-assessment (before Activity 1) and a post-assessment (after Activity 4). Score each out of 5. Learning growth = post-score minus pre-score.

Questions follow the California Science Test (CAST) stimulus-response format. Each item is three-dimensional, assessing a Science and Engineering Practice (SEP), Disciplinary Core Idea (DCI), and Crosscutting Concept (CCC) simultaneously, aligned to HS-PS4-2, HS-PS4-3.

---

### Pre-Assessment Questions

### Question 1

Electromagnetic waves are used for wireless communication. Which relationship between frequency and wavelength is correct?

A. Higher frequency corresponds to longer wavelength
B. Higher frequency corresponds to shorter wavelength
C. Frequency and wavelength are independent of each other
D. All electromagnetic waves have the same wavelength regardless of frequency

Correct Answer: B

Feedback: Correct. Frequency and wavelength are inversely related. Since all electromagnetic waves travel at the speed of light, higher frequency waves must have shorter wavelengths. Frequency and wavelength have an inverse relationship: as frequency increases, wavelength decreases. This follows from the wave equation: speed of light = frequency x wavelength.

---

### Question 2

When an electromagnetic wave encounters a solid wall, some of its energy is absorbed. Which factor most determines how much energy is absorbed?

A. The color of the wall
B. The frequency of the electromagnetic wave and the material composition of the wall
C. The speed at which the wave is traveling
D. The number of walls in the building

Correct Answer: B

Feedback: Correct. Absorption depends on the interaction between the wave's frequency and the material's molecular structure. Higher-frequency waves are generally absorbed more readily by common building materials. Absorption depends on two factors: the frequency of the wave (higher frequencies tend to be absorbed more) and the material properties of the obstacle (density, composition, moisture content).

---

### Question 3

A cell tower broadcasts a signal. According to the inverse square law, what happens to the signal strength when the distance from the tower is doubled?

A. Signal strength is reduced to one-half
B. Signal strength is reduced to one-quarter
C. Signal strength remains the same
D. Signal strength doubles

Correct Answer: B

Feedback: Correct. The inverse square law states that signal intensity is inversely proportional to the square of the distance. Doubling the distance reduces signal strength to (1/2)^2 = 1/4. The inverse square law states that intensity decreases with the square of the distance. At twice the distance, intensity drops to 1/4, not 1/2. This is because the signal spreads over four times the area.

---

### Question 4

5G networks use frequencies in the 'millimeter wave' range (30-300 GHz). What trade-off does this frequency range present for network engineers?

A. Millimeter waves travel farther but carry less data than lower frequencies
B. Millimeter waves carry enormous amounts of data but are easily blocked by buildings, trees, and rain
C. Millimeter waves are invisible to detection equipment, making network monitoring impossible
D. Millimeter waves require less energy to transmit than lower-frequency signals

Correct Answer: B

Feedback: Correct. This fundamental trade-off between data capacity and penetration ability is the central engineering challenge of 5G: higher frequencies enable faster data rates but are absorbed and blocked by obstacles far more easily. The millimeter wave trade-off is fundamental: these high frequencies can carry vastly more data (10+ Gbps) but are easily absorbed by buildings, vegetation, rain, and even humidity, severely limiting their range and penetration.

---

### Question 5

MIMO (Multiple-Input Multiple-Output) antenna technology uses multiple antennas simultaneously. What is the primary advantage of this approach?

A. It allows a single antenna to broadcast at multiple frequencies simultaneously
B. It increases network capacity by transmitting and receiving multiple independent data streams at the same time
C. It eliminates the need for cell towers entirely
D. It converts electromagnetic waves into sound waves for clearer voice calls

Correct Answer: B

Feedback: Correct. MIMO uses spatial multiplexing to send multiple independent data streams through multiple antennas simultaneously, dramatically increasing the total data capacity of the network. MIMO's primary advantage is increased capacity through spatial multiplexing. By using multiple antennas to transmit and receive independent data streams simultaneously, the network can serve more users at higher speeds.

---

### Post-Assessment Questions

### Question 1

In the wireless communication model, what is the fundamental trade-off that the relationship between Signal Frequency and Wave Penetration reveals?

A. Higher frequencies penetrate materials better but carry less data
B. Higher frequencies carry more data but penetrate materials less effectively, requiring more infrastructure to compensate
C. Signal frequency has no measurable effect on wave penetration in the model
D. Lower frequencies require more tower density because they carry less data per tower

Correct Answer: B

Feedback: Correct. The model demonstrates the core physics trade-off: Data Transfer Rate increases with frequency but Wave Penetration decreases, forcing engineers to dramatically increase Tower Density to maintain coverage. The model reveals the fundamental constraint: as Signal Frequency increases, Data Transfer Rate rises (more bandwidth) but Wave Penetration drops (signals blocked more easily). This trade-off is the defining engineering challenge of 5G.

---

### Question 2

A student compares the 4G scenario (700 MHz) to the 5G millimeter wave scenario (39 GHz) in the model. Tower Density must increase dramatically for 5G. What does the model show as the primary reason?

A. 5G towers are physically smaller and cannot transmit as much power
B. Each 5G millimeter wave cell covers only 200-300 meters versus 2-5 kilometers for 4G because higher-frequency signals are absorbed more rapidly by the atmosphere and obstacles
C. 5G towers are more expensive, so more small towers are needed to reduce cost
D. 4G towers broadcast in all directions while 5G towers can only broadcast in one direction

Correct Answer: B

Feedback: Correct. The model shows that millimeter wave signals attenuate so rapidly that each cell covers a fraction of the area of a 4G cell, requiring a massive increase in the number of transmitters to provide continuous coverage. The model demonstrates that coverage area per cell shrinks dramatically at higher frequencies. A 4G cell at 700 MHz might cover 2-5 km, but a 5G millimeter wave cell at 39 GHz covers only 200-300 meters due to rapid signal attenuation.

---

### Question 3

The model shows that increasing Tower Density to compensate for poor Wave Penetration creates a secondary problem. What is it?

A. More towers reduce the total network capacity by splitting the available bandwidth
B. Interference Level increases as more closely spaced towers produce overlapping signals, requiring beamforming and MIMO to manage
C. More towers consume less total energy because each tower is smaller
D. Tower Density has no effect on any other variable in the model

Correct Answer: B

Feedback: Correct. The model reveals a cascade: more towers create more signal overlap and interference, which degrades network quality. Engineers must deploy beamforming and MIMO technology to direct signals precisely and manage interference. The model shows that Tower Density creates a secondary challenge: more closely-spaced towers produce overlapping signals that interfere with each other, requiring sophisticated beamforming and MIMO technology to maintain signal quality.

---

### Question 4

Based on the model, why did engineers design 5G as a layered network using multiple frequency bands rather than a single millimeter wave frequency?

A. Because a single frequency would have been too simple to implement
B. Because no single frequency band resolves the coverage-versus-capacity trade-off; low-band provides wide coverage, mid-band balances speed and reach, and millimeter wave provides high-density capacity
C. Because the model shows that all frequency bands perform identically
D. Because millimeter waves are dangerous to human health at high power levels

Correct Answer: B

Feedback: Correct. The model demonstrates that no single frequency band can optimize both coverage and capacity. The layered approach uses each band's strengths: low-band for reach, mid-band for balance, and millimeter wave for dense, high-speed areas. The model shows that the coverage-capacity trade-off cannot be resolved with a single frequency. A layered approach assigns low-band frequencies for rural coverage, mid-band for urban areas, and millimeter wave for high-density locations like stadiums.

---

### Question 5

A student claims that 5G is simply 'better 4G' with no fundamental physics differences. Using evidence from the model, which response best evaluates this claim?

A. The claim is correct because both use electromagnetic waves for communication
B. The claim is incorrect because 5G operates at fundamentally different frequencies that introduce new physics trade-offs: millimeter waves behave qualitatively differently than sub-6 GHz signals regarding penetration, absorption, and infrastructure requirements
C. The claim is correct because tower density is the same for both technologies
D. The claim is incorrect because 5G uses sound waves instead of electromagnetic waves

Correct Answer: B

Feedback: Correct. While both use electromagnetic waves, the model shows that millimeter wave frequencies introduce qualitatively different behavior: near-total absorption by obstacles, atmospheric attenuation by rain, and coverage areas orders of magnitude smaller. The model demonstrates that 5G is not simply a faster version of 4G. The jump to millimeter wave frequencies introduces fundamentally different physics: signals that cannot penetrate walls, are absorbed by rain, and require completely different infrastructure.

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
Question 4: B
Question 5: B

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-10/G10L2-L06/G10L2-L06-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-10/G10L2-L06/G10L2-L06-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-10/G10L2-L06/G10L2-L06-Student-Presentation.pptx] |
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