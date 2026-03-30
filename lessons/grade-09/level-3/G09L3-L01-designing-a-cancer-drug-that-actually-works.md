# Lesson: Designing a Cancer Drug That Actually Works

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G09L3-L01 |
| **Grade** | 9th Grade — Level 3: Biotech |
| **Lesson Name** | Designing a Cancer Drug That Actually Works |
| **Status** | Template |

---

## Platform

### Title
**Designing a Cancer Drug That Actually Works — Multi-Scale Pharmacokinetic Modeling from Molecule to Patient**

### Overview
This lesson introduces students to multi-scale pharmacokinetic modeling — one of the most powerful tools in modern drug development. Biotech skill focus: Multi-scale modeling (molecular to cellular to organism). The pharmaceutical industry loses billions of dollars annually on drugs that fail in clinical trials because researchers couldn't predict how molecular-level drug behavior would translate to patient-level outcomes. Computational pharmacokinetic models bridge this gap by integrating absorption, distribution, metabolism, and excretion (ADME) processes across biological scales. Students investigate the driving question: Why do most cancer drugs fail in clinical trials — and how can computational modeling help us design ones that actually work? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of diverse 14-15 year old students in an advanced biotech lab examining molecular drug models on holographic displays, with a pharmacokinetic concentration-time curve visible on a large monitor, dramatic lighting with blue and purple lab glow]

### Grade
9th Grade — Level 3: Biotech

### NGSS Standard
**HS-LS1-4, HS-ETS1-2**: Use a model to illustrate the role of cellular division in producing and maintaining complex organisms; design a solution to a complex real-world problem by breaking it down into smaller, more manageable problems.

### Learning Objectives
- Build a multi-scale pharmacokinetic model that traces drug behavior from molecular absorption to organism-level outcomes
- Analyze how drug dosage, absorption rate, and metabolism interact across biological scales to determine therapeutic effectiveness
- Optimize dosage parameters to maximize tumor destruction while minimizing damage to healthy tissues
- Evaluate the concept of a therapeutic window and explain why most cancer drugs have dangerously narrow ones

### Component List (Starting Model: 9 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Drug Dosage | External | The amount of chemotherapy drug administered to the patient per treatment cycle, measured in milligrams per square meter of body surface area |
| Absorption Rate | Internal | The speed at which the drug crosses from the administration site into the bloodstream, influenced by drug formulation, route of delivery, and patient physiology |
| Blood Concentration | Internal | The measured level of active drug molecules circulating in the patient's bloodstream at any given time, which rises after dosing and falls as the drug is metabolized |
| Tumor Uptake | Internal | The rate and amount of drug that successfully crosses from the bloodstream into the tumor microenvironment and binds to cancer cell targets |
| Healthy Cell Damage | Internal | The degree of collateral destruction to normal, non-cancerous cells caused by drug exposure — the primary source of chemotherapy side effects |
| Metabolism Rate | Internal | The speed at which the liver enzymatically breaks down the active drug into inactive metabolites, reducing the effective drug concentration over time |
| Kidney Clearance | Internal | The rate at which the kidneys filter drug metabolites and waste products from the blood for excretion in urine, which determines how quickly the drug leaves the body |
| Therapeutic Window | Internal | The calculated range between the minimum effective concentration (enough to kill cancer cells) and the maximum tolerated concentration (before organ toxicity occurs) |
| Side Effect Severity | Internal | The overall burden of adverse effects experienced by the patient — from nausea and fatigue to organ damage and immunosuppression — scored on a clinical severity scale |

### Research for Lesson
- Pharmacokinetics: The ADME Framework — reference materials and textbook resources
- The Therapeutic Window Problem in Oncology — reference materials and textbook resources
- Multi-Scale Modeling in Drug Development — reference materials and textbook resources
- Metronomic Chemotherapy: A Modeling Success Story — reference materials and textbook resources

---

## Step 1: LOCATE — Build Your System

### Text Editor

```
DESIGNING A CANCER DRUG THAT ACTUALLY WORKS

Multi-Scale Pharmacokinetic Modeling from Molecule to Patient.
Why do most cancer drugs fail in clinical trials — and how can computational modeling help us design ones that actually work?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Drug Dosage" — the amount of chemotherapy drug administered to the patient per treatment cycle
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Absorption Rate" — the speed at which the drug crosses from the administration site into the bloodstream
  ○ Click "Blood Concentration" — the measured level of active drug molecules circulating in the patient's bloodstream at any given time
  ○ Click "Tumor Uptake" — the rate and amount of drug that successfully crosses from the bloodstream into the tumor microenvironment and binds to cancer cell targets
  ○ Click "Healthy Cell Damage" — the degree of collateral destruction to normal
  ○ Click "Metabolism Rate" — the speed at which the liver enzymatically breaks down the active drug into inactive metabolites
  ○ Click "Kidney Clearance" — the rate at which the kidneys filter drug metabolites and waste products from the blood for excretion in urine
  ○ Click "Therapeutic Window" — the calculated range between the minimum effective concentration (enough to kill cancer cells) and the maximum tolerated concentration (before organ toxicity occurs)
  ○ Click "Side Effect Severity" — the overall burden of adverse effects experienced by the patient — from nausea and fatigue to organ damage and immunosuppression — scored on a clinical severity scale

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
"Why do most cancer drugs fail in clinical trials — and how can computational modeling help us design ones that actually work?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Drug Dosage' — that's external. The amount of chemotherapy drug administered to the patient per treatment cycle.
Click on 'Absorption Rate' — that's internal. The speed at which the drug crosses from the administration site into the bloodstream.
Click on 'Blood Concentration' — that's internal. The measured level of active drug molecules circulating in the patient's bloodstream at any given time.
Click on 'Tumor Uptake' — that's internal. The rate and amount of drug that successfully crosses from the bloodstream into the tumor microenvironment and binds to cancer cell targets.
Click on 'Healthy Cell Damage' — that's internal. The degree of collateral destruction to normal.
Click on 'Metabolism Rate' — that's internal. The speed at which the liver enzymatically breaks down the active drug into inactive metabolites.
Click on 'Kidney Clearance' — that's internal. The rate at which the kidneys filter drug metabolites and waste products from the blood for excretion in urine.
Click on 'Therapeutic Window' — that's internal. The calculated range between the minimum effective concentration (enough to kill cancer cells) and the maximum tolerated concentration (before organ toxicity occurs).
Click on 'Side Effect Severity' — that's internal. The overall burden of adverse effects experienced by the patient — from nausea and fatigue to organ damage and immunosuppression — scored on a clinical severity scale.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Drug Dosage is the only external component because it represents the physician's direct control over the amount of drug administered. All other eight components — Absorption Rate, Blood Concentration, Tumor Uptake, Healthy Cell Damage, Metabolism Rate, Kidney Clearance, Therapeutic Window, and Side Effect Severity — are internal responses determined by the patient's physiology interacting with the drug. The doctor cannot directly control how fast the liver metabolizes the drug or how much drug reaches the tumor.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next step, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 9 components sorted: Drug Dosage (External), Absorption Rate, Blood Concentration, Tumor Uptake, Healthy Cell Damage, Metabolism Rate, Kidney Clearance, Therapeutic Window, Side Effect Severity (Internal)]

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
• Click on "Drug Dosage" and drag an arrow to "Blood Concentration"
• Click on "Blood Concentration" and drag an arrow to "Tumor Uptake"
• Click on "Blood Concentration" and drag an arrow to "Healthy Cell Damage"
• Click on "Metabolism Rate" and drag an arrow to "Blood Concentration"
• Click on "Kidney Clearance" and drag an arrow to "Blood Concentration"
• Click on "Healthy Cell Damage" and drag an arrow to "Side Effect Severity"

Task C: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Drug Dosage → Blood Concentration = POSITIVE (+)
    Higher drug dosage increases the amount of drug entering the bloodstream through absorption, raising blood concentration proportionally to the dose administered.

  ○ Blood Concentration → Tumor Uptake = POSITIVE (+)
    Higher blood concentration creates a steeper concentration gradient between blood and tumor tissue, driving more drug molecules across the tumor vasculature into cancer cells.

  ○ Blood Concentration → Healthy Cell Damage = POSITIVE (+)
    Higher blood concentration simultaneously exposes healthy tissues to more drug, increasing collateral damage to rapidly-dividing normal cells like bone marrow, gut lining, and hair follicles.

  ○ Metabolism Rate → Blood Concentration = NEGATIVE (−)
    Faster liver metabolism breaks down more drug per unit time, actively reducing blood concentration and shortening the duration of therapeutic drug levels.

  ○ Kidney Clearance → Blood Concentration = NEGATIVE (−)
    More efficient kidney filtration removes drug metabolites and some active drug from circulation faster, accelerating the decline of blood concentration after dosing.

  ○ Healthy Cell Damage → Side Effect Severity = POSITIVE (+)
    Greater healthy cell damage directly increases the severity of clinical side effects — nausea from gut lining damage, immunosuppression from bone marrow damage, hair loss from follicle damage.

Task D: CHECK YOUR MODEL
• You should have 6 arrows total
• 2 negative relationship(s), 4 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: When Drug Dosage is increased, Blood Concentration rises — but so does Healthy Cell Damage. Meanwhile, Metabolism Rate and Kidney Clearance are constantly pulling the drug OUT of the blood. How do you find the sweet spot where Tumor Uptake is maximized but Side Effect Severity stays manageable? That's the therapeutic window — and for most cancer drugs, it's razor thin.
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Drug Dosage' and drag an arrow
over to 'Blood Concentration.'

Here's the key question: When drug dosage goes UP, does
blood concentration go UP or DOWN?

Higher drug dosage increases the amount of drug entering the bloodstream through absorption, raising blood concentration proportionally to the dose administered.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Blood Concentration' and drag an arrow
over to 'Tumor Uptake.'

Here's the key question: When blood concentration goes UP, does
tumor uptake go UP or DOWN?

Higher blood concentration creates a steeper concentration gradient between blood and tumor tissue, driving more drug molecules across the tumor vasculature into cancer cells.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'Blood Concentration' and drag an arrow
over to 'Healthy Cell Damage.'

Here's the key question: When blood concentration goes UP, does
healthy cell damage go UP or DOWN?

Higher blood concentration simultaneously exposes healthy tissues to more drug, increasing collateral damage to rapidly-dividing normal cells like bone marrow, gut lining, and hair follicles.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Final connection: Click on 'Metabolism Rate' and drag an arrow
over to 'Blood Concentration.'

Here's the key question: When metabolism rate goes UP, does
blood concentration go UP or DOWN?

Faster liver metabolism breaks down more drug per unit time, actively reducing blood concentration and shortening the duration of therapeutic drug levels.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Kidney Clearance' and drag an arrow
over to 'Blood Concentration.'

Here's the key question: When kidney clearance goes UP, does
blood concentration go UP or DOWN?

More efficient kidney filtration removes drug metabolites and some active drug from circulation faster, accelerating the decline of blood concentration after dosing.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Healthy Cell Damage' and drag an arrow
over to 'Side Effect Severity.'

Here's the key question: When healthy cell damage goes UP, does
side effect severity go UP or DOWN?

Greater healthy cell damage directly increases the severity of clinical side effects — nausea from gut lining damage, immunosuppression from bone marrow damage, hair loss from follicle damage.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Look at your model now. You've got 2 negative and 4
positive relationships. 6 arrows total.

When Drug Dosage is increased, Blood Concentration rises — but so does Healthy Cell Damage. Meanwhile, Metabolism Rate and Kidney Clearance are constantly pulling the drug OUT of the blood. How do you find the sweet spot where Tumor Uptake is maximized but Side Effect Severity stays manageable? That's the therapeutic window — and for most cancer drugs, it's razor thin.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Drug Dosage +→ Blood Concentration, Blood Concentration +→ Tumor Uptake, Blood Concentration +→ Healthy Cell Damage, Metabolism Rate −→ Blood Concentration, Kidney Clearance −→ Blood Concentration, Healthy Cell Damage +→ Side Effect Severity]

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
• When Drug Dosage is HIGH, what happens to the internal components?

Task C: SCENARIO — STANDARD DOSAGE
• Recommended clinical dose, normal metabolism
• PREDICT FIRST: What do you predict will happen to Blood Concentration over a 24-hour period after a single standard dose?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task D: SCENARIO — HIGH-DOSE AGGRESSIVE
• Double the standard dose
• PREDICT FIRST: What do you predict happens to the ratio of Tumor Uptake versus Healthy Cell Damage when the dose is doubled?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task E: SCENARIO — METRONOMIC OPTIMIZATION
• Half-dose given twice as frequently
• PREDICT FIRST: Do you predict that frequent low doses will maintain more consistent Tumor Uptake than a single high dose?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Drug concentration in the blood follows a predictable curve — rising after administration, peaking, then declining as metabolism and clearance remove the drug from circulation
• The therapeutic window for most cancer drugs is extremely narrow — the dose needed to kill cancer cells is dangerously close to the dose that damages healthy tissue
• Metabolism rate and kidney clearance vary significantly between patients, meaning the same dose can be therapeutic in one person and toxic in another
• Metronomic dosing (lower, more frequent doses) can maintain drug levels within the therapeutic window more consistently than traditional high-dose protocols

THE ANSWER: Most cancer drugs fail because the therapeutic window is incredibly narrow. The drug must reach a concentration high enough to penetrate the tumor microenvironment and kill cancer cells, but not so high that it destroys healthy tissue and overwhelms the patient with toxic side effects. Computational pharmacokinetic modeling allows researchers to simulate thousands of dosing strategies — optimizing absorption, predicting metabolism, and accounting for individual patient variation — before ever testing the drug in a human. Multi-scale modeling connects molecular drug-receptor interactions to cellular tumor response to whole-patient outcomes, making drug design more rational and less trial-and-error.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Standard Dosage. Recommended clinical dose, normal metabolism.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: High-Dose Aggressive.
Double the standard dose.

Before you run it — make a prediction. What do you predict happens to the ratio of Tumor Uptake versus Healthy Cell Damage when the dose is doubled?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Metronomic Optimization. Half-dose given twice as frequently.
Do you predict that frequent low doses will maintain more consistent Tumor Uptake than a single high dose?

Here's what our model reveals: Most cancer drugs fail because the therapeutic window is incredibly narrow. The drug must reach a concentration high enough to penetrate the tumor microenvironment and kill cancer cells, but not so high that it destroys healthy tissue and overwhelms the patient with toxic side effects. Computational pharmacokinetic modeling allows researchers to simulate thousands of dosing strategies — optimizing absorption, predicting metabolism, and accounting for individual patient variation — before ever testing the drug in a human. Multi-scale modeling connects molecular drug-receptor interactions to cellular tumor response to whole-patient outcomes, making drug design more rational and less trial-and-error.

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
   • What happens if you turn OFF Drug Dosage?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Tumor Blood Supply — The density and permeability of blood vessels feeding the tumor, which determines how much circulating drug can actually reach cancer cells — tumors with poor blood supply may be resistant even at high doses
   • Drug Resistance Factor — The probability that cancer cells develop molecular mechanisms to pump the drug out or deactivate it, reducing effectiveness over multiple treatment cycles
   • Patient Liver Function — The individual patient's liver enzyme activity, which determines how quickly the drug is metabolized — liver impairment can cause dangerous drug accumulation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • Pharmacokinetics: The ADME Framework — how does this connect to your model?
   • The Therapeutic Window Problem in Oncology — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your multi-scale model demonstrate the challenge of connecting molecular drug behavior to patient-level outcomes?
   • Why does the same drug dose produce different outcomes in different patients, according to your model?
   • What trade-offs did you discover between maximizing Tumor Uptake and minimizing Side Effect Severity?
   • How could your model be used to personalize cancer treatment for individual patients?

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

Tumor Blood Supply. The density and permeability of blood vessels feeding the tumor, which determines how much circulating drug can actually reach cancer cells — tumors with poor blood supply may be resistant even at high doses
How would you model that?

Drug Resistance Factor. The probability that cancer cells develop molecular mechanisms to pump the drug out or deactivate it, reducing effectiveness over multiple treatment cycles
How would you model that?

Patient Liver Function. The individual patient's liver enzyme activity, which determines how quickly the drug is metabolized — liver impairment can cause dangerous drug accumulation
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

Pharmacokineticists and Computational Pharmacologists design drug dosing protocols using mathematical models and computer simulations. They work for pharmaceutical companies, the FDA, and academic medical centers, earning $90,000–$180,000/year. Clinical Pharmacologists who manage cancer drug protocols earn $150,000–$300,000/year.

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
Visual: Title slide with dramatic image of molecular drug structures and pharmacokinetic curves
Say: "Over 95% of experimental cancer drugs fail in clinical trials. Not because they can't kill cancer cells — most of them can. They fail because we can't get them to kill cancer without killing the patient. Today, you're going to try to solve that problem."
Do: Display a statistic about cancer drug failure rates. Let the magnitude sink in before continuing.
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and advanced pharmacokinetic vocabulary
Say: "You're going to build a multi-scale pharmacokinetic model — the same type of computational tool that pharmaceutical companies use to design drug dosing protocols. This is real biotech."
Do: Pre-teach pharmacokinetics and therapeutic window. Have students write their own definitions before revealing the formal ones.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: Why do most cancer drugs fail — and how can modeling fix it?
Say: "A drug kills 99% of cancer cells in a petri dish. Six years and two billion dollars later, it fails in human trials. What went wrong between the dish and the patient?"
Do: Think-pair-share: Students brainstorm why a drug that works in a dish might fail in a body. Collect ideas on the board.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps with pharmacokinetic context
Say: "We're going to connect molecular-level drug behavior to cellular-level tumor response to patient-level outcomes. That's multi-scale modeling — and it's how real drug companies design chemotherapy protocols."
Do: Preview each LEVER step. Emphasize that this model spans three biological scales simultaneously.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Nine pharmacokinetic component cards across molecular, cellular, and organism scales
Say: "These nine components represent the complete journey of a cancer drug through the body. Only ONE of them is truly under the doctor's control — which one?"
Do: Guide identification of Drug Dosage as the only external component. Discuss why all other components are internal responses. Sort components by biological scale.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows showing the pharmacokinetic cascade from dosage to side effects
Say: "Here's the cruel paradox of cancer treatment: the same pathway that delivers drug to the tumor also delivers it to every other organ in the body. How do you maximize one and minimize the other?"
Do: Students trace the pathway from Drug Dosage through Blood Concentration to both Tumor Uptake and Healthy Cell Damage. Identify the therapeutic window as the narrow zone where the drug works without killing.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Concentration-time curves and therapeutic window visualization
Say: "You're now the pharmacokineticist. Run these three scenarios and find the dosing strategy that keeps the drug inside the therapeutic window the longest."
Do: Students predict outcomes first, then run standard, aggressive, and metronomic dosing scenarios. Track time-within-therapeutic-window as the key metric.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key pharmacokinetic findings and multi-scale insights
Say: "You just discovered what took the pharmaceutical industry decades to figure out — sometimes less is more. Metronomic dosing, predicted by computational models, is now saving real cancer patients' lives."
Do: Connect simulation findings to real clinical practice. Discuss how modeling predicted metronomic chemotherapy before clinical trials proved it.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Adaptive chemotherapy dosing algorithm design challenge
Say: "A pharmaceutical company just hired your team. Design an algorithm that adjusts chemotherapy doses in real time based on patient biomarkers. This is the future of cancer treatment."
Do: Groups design adaptive dosing algorithms. Must include biomarker inputs, decision logic, and safety thresholds. Present and defend designs.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: Designing a Cancer Drug That Actually Works
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
This lesson introduces students to multi-scale pharmacokinetic modeling — one of the most powerful tools in modern drug development. Biotech skill focus: Multi-scale modeling (molecular to cellular to organism). The pharmaceutical industry loses billions of dollars annually on drugs that fail in clinical trials because researchers couldn't predict how molecular-level drug behavior would translate to patient-level outcomes. Computational pharmacokinetic models bridge this gap by integrating absorption, distribution, metabolism, and excretion (ADME) processes across biological scales.

NGSS ALIGNMENT:
HS-LS1-4, HS-ETS1-2: Use a model to illustrate the role of cellular division in producing and maintaining complex organisms; design a solution to a complex real-world problem by breaking it down into smaller, more manageable problems.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Developing and Using Models
  Students develop a multi-scale computational model that connects molecular pharmacokinetics to cellular tumor response to organism-level treatment outcomes.
• Disciplinary Core Idea: LS1.A Structure and Function / ETS1.B Developing Possible Solutions
  Cellular processes including drug metabolism operate at multiple biological scales; engineering design requires systematic optimization of competing constraints.
• Crosscutting Concept: Systems and System Models
  Students model the human body as a complex system where drug behavior at the molecular scale produces emergent outcomes at the organism scale through multiple interacting subsystems.

PACING GUIDE:
• Step 1 (Locate): 8-10 minutes
• Step 2 (Establish): 8-10 minutes
• Step 3 (Visualize & Evaluate): 10-12 minutes
• Step 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Pharmacokinetics, Therapeutic Window, Multi-Scale Modeling, Pharmacodynamics
□ Prepare Why do most cancer drugs fail in clinical trials — and how can computational modeling help us design ones that actually work discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify nine pharmacokinetic components operating across molecular, cellular, and organism scales — from Drug Dosage input through absorption, blood concentration, tumor uptake, healthy cell damage, metabolism, clearance, therapeutic window, to side effect severity output.
• Establish: Students determine that Drug Dosage drives Blood Concentration through Absorption Rate, which simultaneously enables Tumor Uptake (desired) and Healthy Cell Damage (undesired), while Metabolism Rate and Kidney Clearance continuously remove the drug — creating the fundamental pharmacokinetic tension.
• Visualize: Students build a computational model connecting all nine components across biological scales, visualizing the concentration-time curve and the therapeutic window where the drug is effective but not toxic.
• Evaluate: Students run standard dosage, high-dose aggressive, and metronomic optimization scenarios to find dosing strategies that maximize time within the therapeutic window.
• Revise: Students add Tumor Blood Supply, Drug Resistance Factor, or Patient Liver Function to explore personalized pharmacokinetics and treatment optimization.

BACKGROUND CONTENT:
• Pharmacokinetics: The ADME Framework:
  Every drug's journey through the body follows four phases: Absorption (drug enters the bloodstream from the administration site — oral drugs must survive stomach acid and cross the intestinal wall, IV drugs bypass this entirely), Distribution (drug travels through the bloodstream and crosses into tissues — the blood-brain barrier, tumor vasculature, and protein binding all affect distribution), Metabolism (primarily in the liver, cytochrome P450 enzymes chemically modify the drug, usually inactivating it — genetic variation in CYP enzymes causes 10-fold differences in metabolism between patients), and Excretion (kidneys filter metabolites from blood into urine; some drugs are also excreted in bile, sweat, or exhaled air). The concentration-time curve that results from these four processes determines everything about whether a drug works or kills the patient.

• The Therapeutic Window Problem in Oncology:
  Cancer drugs face a unique pharmacokinetic challenge: cancer cells are human cells. Unlike antibiotics, which target bacterial proteins absent in human cells, chemotherapy drugs must exploit the subtle differences between cancer cells and normal cells — usually faster division rates. This means the concentration required to kill cancer cells (minimum effective concentration, or MEC) is often dangerously close to the concentration that causes organ toxicity (maximum tolerated concentration, or MTC). The therapeutic window (MTC minus MEC) for drugs like doxorubicin, cisplatin, and paclitaxel can be as narrow as a 2-fold range, compared to 10-fold or wider for common antibiotics. This is why chemotherapy has such devastating side effects.

• Multi-Scale Modeling in Drug Development:
  Traditional pharmacokinetic models operate at a single scale — tracking drug concentration in blood over time. Modern multi-scale models integrate three levels simultaneously: molecular scale (drug-receptor binding kinetics, enzyme-substrate interactions, protein conformational changes), cellular scale (signal transduction cascades, cell cycle arrest, apoptosis induction, resistance mechanism activation), and organism scale (organ function, immune response, clinical symptoms, survival probability). Physiologically-based pharmacokinetic (PBPK) models represent each organ as a compartment with its own blood flow, volume, and metabolic capacity. These models can predict drug behavior in populations that were never tested — pediatric patients, patients with liver disease, or patients taking multiple drugs simultaneously.

• Metronomic Chemotherapy: A Modeling Success Story:
  Computational pharmacokinetic modeling led to a paradigm shift in cancer treatment called metronomic chemotherapy. Traditional protocols give the maximum tolerated dose (MTD) on an infrequent schedule (e.g., every 3 weeks) to allow the patient to recover from side effects between cycles. Models predicted that lower doses given more frequently could maintain drug levels within the therapeutic window more consistently, reducing the peaks that cause toxicity and the troughs where the drug drops below effective levels. Clinical trials confirmed this — metronomic dosing showed equal or better tumor control with dramatically fewer side effects for several cancer types. This is multi-scale modeling literally saving lives.

COMMON MISCONCEPTIONS:
• "More drug always means more effective treatment"
  Reality: Increasing drug dosage beyond the therapeutic window does NOT improve outcomes — it increases toxicity and side effects without proportionally increasing tumor kill. Cancer cells that survive the initial drug exposure are often the resistant ones, so higher doses kill more healthy cells while selecting for resistant cancer cells. The relationship between dose and effectiveness plateaus while the relationship between dose and toxicity continues to climb.
  Strategy: Model it: Double the Drug Dosage and compare the ratio of Tumor Uptake increase versus Side Effect Severity increase. The toxicity outpaces the benefit.

• "Cancer drugs specifically target cancer cells"
  Reality: Most traditional chemotherapy drugs do NOT specifically target cancer cells. They target rapidly-dividing cells — which includes cancer but also bone marrow, gut lining, hair follicles, and immune cells. This is why chemotherapy causes hair loss, nausea, and immunosuppression. The drug cannot tell the difference between a dividing cancer cell and a dividing healthy cell.
  Strategy: Ask: If the drug kills 'rapidly dividing cells,' what other cells in your body divide rapidly? Make a list — that's your side effects list.

• "Computer models can perfectly predict drug outcomes"
  Reality: Pharmacokinetic models are powerful but imperfect. They simplify the staggering complexity of human biology into manageable mathematical equations. Real patients have genetic variation, comorbidities, microbiome differences, psychological stress responses, and countless other factors no model fully captures. Models are tools for better decision-making, not crystal balls.
  Strategy: Discuss: What factors does our 9-component model leave out? Make a list of things that could affect drug outcomes that aren't in the model.

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
Big Question: Why do most cancer drugs fail in clinical trials — and how can computational modeling help us design ones that actually work?
Answer: Most cancer drugs fail because the therapeutic window is incredibly narrow. The drug must reach a concentration high enough to penetrate the tumor microenvironment and kill cancer cells, but not so high that it destroys healthy tissue and overwhelms the patient with toxic side effects. Computational pharmacokinetic modeling allows researchers to simulate thousands of dosing strategies — optimizing absorption, predicting metabolism, and accounting for individual patient variation — before ever testing the drug in a human. Multi-scale modeling connects molecular drug-receptor interactions to cellular tumor response to whole-patient outcomes, making drug design more rational and less trial-and-error.

Simulation Answers:
• Standard Dosage Scenario: With the standard clinical dose, Blood Concentration rises sharply after administration, peaks within 1-4 hours, then gradually declines as Metabolism Rate and Kidney Clearance remove the drug. The concentration enters the Therapeutic Window for a limited period — typically 6-12 hours — during which Tumor Uptake is effective. However, the peak concentration also causes a spike in Healthy Cell Damage, producing moderate Side Effect Severity.
• Metronomic Optimization Scenario: With half-dose given twice as frequently, Blood Concentration never peaks as high (reducing the Healthy Cell Damage spike) but also never drops as low (maintaining consistent Tumor Uptake). The drug spends more total time within the Therapeutic Window per treatment cycle. Side Effect Severity is lower because the concentration peaks never reach the toxic threshold, even though the same total drug amount is administered.

Reflection Exemplars:
• Q: Why does the same dose produce different outcomes in different patients?
  A: The model reveals that Blood Concentration is not determined by Drug Dosage alone — it's the result of Absorption Rate, Metabolism Rate, and Kidney Clearance all acting simultaneously. A patient with fast liver metabolism (high Metabolism Rate) will clear the drug before it accumulates to therapeutic levels, while a patient with impaired kidneys (low Kidney Clearance) may accumulate toxic concentrations from the same dose. Personalizing treatment requires knowing each patient's individual pharmacokinetic parameters.
• Q: What trade-offs exist between Tumor Uptake and Side Effect Severity?
  A: The fundamental pharmacokinetic dilemma is that Tumor Uptake and Healthy Cell Damage both increase with Blood Concentration. The model shows that traditional high-dose protocols maximize Tumor Uptake but also maximize Side Effect Severity. Metronomic dosing represents a different trade-off — slightly lower peak Tumor Uptake but dramatically lower Side Effect Severity and more consistent drug levels. The optimal strategy depends on the specific cancer type, drug characteristics, and patient tolerance.

STEM CHALLENGE GUIDANCE:
Title: Design an Adaptive Chemotherapy Dosing Algorithm
Mission: Design a computational algorithm that adjusts chemotherapy dosing in real time based on patient biomarker data, optimizing tumor destruction while minimizing side effects.
Scenario: A pharmaceutical company is developing a next-generation adaptive dosing system for cancer treatment. Instead of giving every patient the same dose on a fixed schedule, the system would use real-time blood biomarker data to adjust doses automatically. Your team has been hired to design the algorithm that determines when and how much drug to administer.
Introduction: Present the challenge: A pharmaceutical company is developing an adaptive dosing system that adjusts chemotherapy in real time based on patient biomarkers. Your team will design the algorithm that decides when and how much drug to give — replacing the one-size-fits-all approach with precision oncology.

Key Concepts:
• Adaptive Dosing: Traditional chemotherapy uses fixed doses on a fixed schedule. Adaptive dosing uses real-time feedback — blood drug levels, tumor marker changes, white blood cell counts — to adjust doses dynamically. Computational models predict how each adjustment will cascade through the pharmacokinetic system.
• Biomarker-Driven Decision Making: Biomarkers like circulating tumor DNA (ctDNA), drug metabolite ratios, and inflammatory markers provide real-time windows into how a patient is responding. An adaptive algorithm processes these inputs and adjusts dosing to keep the drug within the therapeutic window.
• Safety-First Algorithm Design: Medical algorithms must be fail-safe. If sensor data is lost, the system must default to a safe state. Dose escalation rules must include hard upper limits. The algorithm must account for drug-drug interactions, organ function changes, and cumulative toxicity across treatment cycles.

Evaluation Rubric:
• Expert (4): Algorithm integrates multiple biomarker inputs, uses patient-specific pharmacokinetic parameters, includes graduated response logic, hard safety limits, and evidence-based justification from model simulations
• Proficient (3): Algorithm monitors key biomarkers and adjusts dosing with reasonable logic and safety thresholds based on model findings
• Developing (2): Algorithm monitors some indicators but adjustment logic is simplistic or safety thresholds are not well justified
• Beginning (1): Algorithm is incomplete or does not connect biomarker monitoring to the pharmacokinetic model

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a visual diagram of the ADME framework showing the drug's journey through the body
  • Use a concentration-time curve template where students can sketch predicted drug levels before running simulations
  • Scaffold multi-scale thinking: 'At the molecular level, the drug ___. At the cellular level, this causes ___. At the organism level, the patient experiences ___.'

Extensions (Advanced Learners):
  • Research how pharmacogenomics (genetic testing for drug metabolism enzymes) is personalizing cancer treatment dosing protocols
  • Investigate antibody-drug conjugates (ADCs) — 'smart missiles' that deliver chemotherapy directly to tumors — and model how they change the therapeutic window
  • Compare the pharmacokinetics of oral versus intravenous chemotherapy and explain the trade-offs for patient quality of life

Cross-Curricular Connections:
  • Math: Calculate area-under-the-curve (AUC) for different dosing strategies and compare total drug exposure versus time within the therapeutic window
  • ELA: Research and write a policy brief arguing for or against FDA approval of adaptive dosing algorithms that partially automate medical decisions
  • Health/Bioethics: Debate the ethics of computational models making life-and-death dosing decisions — who is responsible when an algorithm makes a mistake?

CAST ALIGNMENT:
• Model multi-scale pharmacokinetic behavior from molecular absorption through cellular uptake to organism-level treatment outcomes
• Optimize drug dosage parameters to maximize therapeutic effectiveness while minimizing toxic side effects
• Analyze the therapeutic window concept and explain why most cancer drugs have dangerously narrow effective ranges

CAST-Style Assessment Questions:
• Multiple Choice: A cancer patient's blood work shows their liver metabolism rate is 40% faster than average. Based on your pharmacokinetic model, what is the most likely clinical consequence?
• Constructed Response: Using your multi-scale model, explain why a drug that kills 99% of cancer cells in a petri dish might fail completely in a human patient. Reference at least three model components in your explanation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: Designing a Cancer Drug That Actually Works
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Why do you think cancer treatment often makes patients extremely sick — sometimes sicker than the cancer itself?

   _________________________________________________________

   _________________________________________________________

2. What do you think determines whether a drug dose is 'just right' versus 'too much' or 'too little'?

   _________________________________________________________

   _________________________________________________________

3. Draw a diagram showing how you think a drug travels through the body from the moment it's administered to the moment it reaches a tumor.

   [DRAWING BOX]

4. What is a therapeutic window and why might it matter for cancer treatment?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Pharmacokinetics              
___ Therapeutic Window            
___ Multi-Scale Modeling          
___ Pharmacodynamics              

A. The study of how a drug moves through the body over time — including absorption, distribution, metabolism, and excretion (ADME) — which determines whether a drug reaches its target at the right concentration
B. The narrow range of drug concentration in the blood that is high enough to kill cancer cells but low enough to avoid destroying healthy tissue — too low means ineffective, too high means toxic
C. A computational approach that connects molecular-level interactions (drug binding to receptors) to cellular-level effects (tumor cell death) to organism-level outcomes (patient survival) in a single integrated model
D. The study of what a drug does to the body once it reaches its target — including receptor binding, signal disruption, and the cascade of cellular responses that follow drug exposure

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

SCENARIO: Standard Dosage
Settings: Recommended clinical dose, normal metabolism
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: High-Dose Aggressive
Settings: Double the standard dose
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Metronomic Optimization
Settings: Half-dose given twice as frequently
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

1. How does your multi-scale model demonstrate the challenge of connecting molecular drug behavior to patient-level outcomes?

   _________________________________________________________

   _________________________________________________________

2. Why does the same drug dose produce different outcomes in different patients, according to your model?

   _________________________________________________________

   _________________________________________________________

3. What trade-offs did you discover between maximizing Tumor Uptake and minimizing Side Effect Severity?

   _________________________________________________________

   _________________________________________________________

4. How could your model be used to personalize cancer treatment for individual patients?

   _________________________________________________________

   _________________________________________________________

5. What are the limitations of modeling a 9-component pharmacokinetic system compared to the full complexity of cancer biology?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Why do most cancer drugs fail in clinical trials — and how can computational modeling help us design ones that actually work? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Developing and Using Models
   □ Disciplinary Core Idea: LS1.A Structure and Function / ETS1.B Developing Possible Solutions
   □ Crosscutting Concept: Systems and System Models

3. What are the limitations of modeling a 9-component pharmacokinetic system compared to the full complexity of cancer biology?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design an Adaptive Chemotherapy Dosing Algorithm
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design a computational algorithm that adjusts chemotherapy dosing in real time based on patient biomarker data, optimizing tumor destruction while minimizing side effects.

SCENARIO: A pharmaceutical company is developing a next-generation adaptive dosing system for cancer treatment. Instead of giving every patient the same dose on a fixed schedule, the system would use real-time blood biomarker data to adjust doses automatically. Your team has been hired to design the algorithm that determines when and how much drug to administer.

GUIDING QUESTIONS:
• What biomarkers would your algorithm monitor to decide when to adjust the dose?
• How would you program the system to respond differently to patients with fast versus slow metabolisms?
• What safety thresholds would trigger an automatic dose reduction or treatment pause?

DESIGN THINKING:
• How frequently should the system sample blood biomarkers — continuously or at intervals?

  _________________________________________________________

• What machine learning approach could improve dosing predictions over multiple treatment cycles?

  _________________________________________________________

• How would you validate your algorithm before testing it on real patients?

  _________________________________________________________

• What ethical considerations arise from automating medical dosing decisions?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Algorithm integrates multiple biomarker inputs, uses patient-specific pharmacokinetic parameters, includes graduated response logic, hard safety limits, and evidence-based justification from model simulations
• Proficient (3): Algorithm monitors key biomarkers and adjusts dosing with reasonable logic and safety thresholds based on model findings
• Developing (2): Algorithm monitors some indicators but adjustment logic is simplistic or safety thresholds are not well justified
• Beginning (1): Algorithm is incomplete or does not connect biomarker monitoring to the pharmacokinetic model

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CAST-Aligned Pre/Post Assessment

### Administration Instructions

These 5 multiple-choice questions are administered identically as both a pre-assessment (before Activity 1) and a post-assessment (after Activity 4). Score each out of 5. Learning growth = post-score minus pre-score.

Questions follow the California Science Test (CAST) stimulus-response format. Each item is three-dimensional, assessing a Science and Engineering Practice (SEP), Disciplinary Core Idea (DCI), and Crosscutting Concept (CCC) simultaneously, aligned to HS-LS1-4, HS-ETS1-2.

---

### Pre-Assessment Questions

### Question 1

A patient receives a chemotherapy drug that kills 95% of cancer cells in a petri dish. Which factor BEST explains why the same drug might fail when given to a patient?

A. The drug must travel through the body and may never reach sufficient concentration at the tumor site
B. Cancer cells in a petri dish are genetically different from those in a patient
C. Chemotherapy drugs only work on blood cancers, not solid tumors
D. The petri dish contains more oxygen than the human body

Correct Answer: A

Feedback: Correct. Pharmacokinetics describes how drugs move through the body. Absorption, metabolism, and clearance all reduce the concentration that actually reaches the tumor, which is often far lower than the controlled dose in a petri dish. Consider how a drug must be absorbed, distributed through the bloodstream, and metabolized before it reaches a tumor. The concentration at the tumor site may be very different from the dose administered.

---

### Question 2

Which of the following BEST describes why chemotherapy often causes severe side effects such as hair loss and nausea?

A. Chemotherapy drugs are designed to only target cancer cells but sometimes malfunction
B. The drugs damage rapidly dividing healthy cells in addition to cancer cells because they cannot distinguish between the two
C. Side effects are caused by allergic reactions to the drug compounds
D. Chemotherapy weakens the immune system, which causes all other symptoms

Correct Answer: B

Feedback: Correct. Most chemotherapy drugs target rapidly dividing cells. Since both cancer cells and certain healthy cells (hair follicles, gut lining, bone marrow) divide rapidly, the drugs damage both, producing severe side effects. Think about what cancer cells and certain healthy cells (like those in hair follicles and the digestive tract) have in common. Chemotherapy targets a cellular behavior, not a specific cell type.

---

### Question 3

A doctor says a drug has a 'narrow therapeutic window.' What does this MOST LIKELY mean?

A. The drug is only effective during a short time period after administration
B. The difference between an effective dose and a toxic dose is very small
C. The drug can only be given through one specific route of administration
D. Only a narrow range of patients can benefit from the drug

Correct Answer: B

Feedback: Correct. A narrow therapeutic window means the minimum dose needed for effectiveness is dangerously close to the maximum dose the body can tolerate, leaving very little room for dosing error. A therapeutic window refers to the range of drug concentrations in the blood between the minimum effective dose and the maximum safe dose. Consider what 'narrow' means in that context.

---

### Question 4

After taking a medication, a patient's blood test shows the drug concentration rising, peaking, and then declining over 12 hours. Which organs are MOST responsible for the decline phase?

A. The heart and lungs, which pump the drug out of the body
B. The liver and kidneys, which metabolize and excrete the drug
C. The stomach and intestines, which stop absorbing the drug
D. The brain and spinal cord, which signal the body to reject foreign chemicals

Correct Answer: B

Feedback: Correct. The liver enzymatically breaks down drugs into inactive metabolites, and the kidneys filter these metabolites from the blood for excretion in urine. Together, they are primarily responsible for drug clearance. Consider which organs are responsible for breaking down substances in the blood and removing waste products from the body.

---

### Question 5

Why would a computational model be useful in designing cancer drug dosing protocols BEFORE testing on patients?

A. Computer models can perfectly predict every patient's response to a drug
B. Models allow researchers to simulate thousands of dosing strategies and identify the most promising ones without risking patient safety
C. Computational models eliminate the need for clinical trials entirely
D. Models can generate new drug molecules that are guaranteed to work

Correct Answer: B

Feedback: Correct. Computational models enable researchers to test many variables (dose, timing, frequency) virtually, narrowing down the most promising strategies before expensive and risky human trials. They do not replace clinical trials but make them more efficient. Think about the purpose of modeling. Models are tools for exploring possibilities and reducing risk, not for producing guaranteed outcomes or replacing experimental validation.

---

### Post-Assessment Questions

### Question 1

In a multi-scale pharmacokinetic model, Drug Dosage is increased by 50%. Blood Concentration rises proportionally, but Tumor Uptake only increases by 10%. Which explanation BEST accounts for this discrepancy?

A. The tumor has limited blood supply and receptor binding capacity, so additional circulating drug cannot all be absorbed by the tumor
B. The kidneys immediately excrete the additional drug before it reaches the tumor
C. Higher doses always decrease tumor uptake due to receptor saturation
D. Blood concentration and tumor uptake are independent variables in pharmacokinetic models

Correct Answer: A

Feedback: Correct. Tumor uptake depends on the tumor's blood vessel density, permeability, and available receptor binding sites. Once these are saturated, additional circulating drug provides diminishing returns at the tumor while increasing systemic toxicity. Consider what limits the amount of drug that can cross from the bloodstream into the tumor microenvironment. Blood concentration is a necessary but not sufficient condition for tumor uptake.

---

### Question 2

A pharmacokineticist compares two dosing strategies: (1) a single high dose every 3 weeks and (2) lower doses given 3 times per week. Both deliver the same total drug amount. Which outcome does the metronomic (frequent low-dose) strategy MOST LIKELY produce?

A. Higher peak toxicity but longer time within the therapeutic window
B. More consistent blood concentration within the therapeutic window with reduced peak side effects
C. Lower overall drug effectiveness because each individual dose is too small
D. Identical outcomes because the total drug amount is the same

Correct Answer: B

Feedback: Correct. Metronomic dosing maintains more consistent drug levels by avoiding the extreme peaks (which cause toxicity) and deep troughs (which allow tumor regrowth) of single high-dose protocols. The total amount matters less than the time spent within the therapeutic window. Consider what happens to blood concentration over time with each strategy. A single large dose creates a high peak followed by a long trough, while frequent smaller doses create a more level concentration profile.

---

### Question 3

Two patients receive identical chemotherapy doses, but Patient A experiences severe toxicity while Patient B shows minimal side effects. Based on pharmacokinetic modeling, which variable MOST LIKELY differs between them?

A. The type of cancer they have
B. Their liver metabolism rate, which determines how quickly the drug is broken down
C. The hospital where they received treatment
D. The time of day the drug was administered

Correct Answer: B

Feedback: Correct. Liver enzyme activity (metabolism rate) varies significantly between individuals due to genetic polymorphisms. A patient with slow metabolism will maintain higher blood drug concentrations for longer, potentially exceeding the toxic threshold, while a fast metabolizer may clear the drug before it reaches effective levels. In pharmacokinetic modeling, the same dose produces different blood concentration profiles in different patients. Consider which biological process most directly controls how long the drug remains active in the body.

---

### Question 4

A student's pharmacokinetic model shows that increasing Kidney Clearance rate while holding all other variables constant results in DECREASED Side Effect Severity but ALSO decreased Tumor Uptake. Which analysis BEST explains this trade-off?

A. Faster kidney clearance removes the drug from the blood more quickly, reducing both the time for tumor absorption and the duration of healthy cell exposure
B. The kidneys selectively filter drug molecules headed toward healthy tissues but not those headed toward the tumor
C. Kidney clearance and tumor uptake are unrelated variables that happen to change simultaneously
D. Increased kidney function strengthens the immune system, which independently reduces side effects

Correct Answer: A

Feedback: Correct. Kidney clearance reduces overall blood concentration over time. This shorter exposure window means less time for healthy cells to absorb the drug (reducing side effects) but also less time for the tumor to accumulate sufficient drug (reducing efficacy). This is a systems-level trade-off. Consider that kidney clearance affects the overall drug concentration in the blood, which is the supply for BOTH tumor uptake and healthy cell damage. What happens when you reduce that shared supply faster?

---

### Question 5

An adaptive dosing algorithm monitors a cancer patient's blood biomarkers in real time and automatically adjusts the next dose. Which design principle is MOST critical for patient safety in this system?

A. The algorithm should always increase the dose to maximize tumor kill rate
B. The algorithm must include safety thresholds that trigger automatic dose reduction or treatment pause when blood concentration approaches the toxic limit
C. The algorithm should prioritize cost reduction over treatment effectiveness
D. The algorithm should use a fixed dosing schedule regardless of biomarker readings to ensure consistency

Correct Answer: B

Feedback: Correct. Safety thresholds are non-negotiable in adaptive dosing. The algorithm must continuously monitor blood concentration against the upper bound of the therapeutic window and automatically reduce or pause dosing before toxicity occurs, even if this temporarily reduces tumor kill rate. Consider the primary risk of automated medical dosing. What safeguard must be built into any system that adjusts drug doses without direct physician intervention for each decision?

---

### Answer Key

**Pre-Assessment:**
Question 1: A
Question 2: B
Question 3: B
Question 4: B
Question 5: B

**Post-Assessment:**
Question 1: A
Question 2: B
Question 3: B
Question 4: A
Question 5: B

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-09/G09L3-L01/G09L3-L01-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-09/G09L3-L01/G09L3-L01-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-09/G09L3-L01/G09L3-L01-Student-Presentation.pptx] |
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