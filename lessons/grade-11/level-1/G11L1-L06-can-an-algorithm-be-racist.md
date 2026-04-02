# Lesson: Can an Algorithm Be Racist?

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G11L1-L06 |
| **Grade** | 11th Grade — Level 1: Foundations of Complex Systems |
| **Lesson Name** | Can an Algorithm Be Racist? |
| **Status** | Template |

---

## Platform

### Title
**Can an Algorithm Be Racist? — Modeling Bias in Artificial Intelligence and Machine Learning**

### Overview
In 2016, ProPublica investigated COMPAS, an algorithm used across the United States to predict whether criminal defendants would reoffend. They found that the algorithm was twice as likely to falsely label Black defendants as high-risk compared to white defendants. The algorithm never used race as an input variable. This investigation revealed a fundamental truth about artificial intelligence: algorithms are not objective — they are mirrors that reflect the biases embedded in the data they learn from. Students investigate the driving question: If a computer algorithm trained on historical data makes decisions about who gets a loan, who gets hired, or who goes to jail — and the historical data reflects decades of racial discrimination — is the algorithm racist, or is it just doing math? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image showing a computer screen displaying an algorithm's decision interface with data points and demographic indicators, subtle visual tension between the clean digital interface and the human impact it represents, dramatic lighting, editorial quality]

### Grade
11th Grade — Level 1: Foundations of Complex Systems

### NGSS Standard
**HS-ETS1-1, HS-ETS1-4**: Analyze a major global challenge to specify qualitative and quantitative criteria and constraints for solutions that account for societal needs and wants. Use a computer simulation to model the impact of proposed solutions to a complex real-world problem with numerous criteria and constraints on interactions within and between systems relevant to the problem.

### Learning Objectives
- Model how training data bias propagates through machine learning algorithms to produce discriminatory outputs
- Explain the relationship between historical data patterns, algorithmic decision-making, and disparate impact on different demographic groups
- Predict how different training data compositions and algorithm design choices affect bias in automated decision systems
- Analyze the ethical implications of deploying biased algorithms in high-stakes domains like criminal justice, healthcare, and lending

### Component List (Starting Model: 5 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Training Data Composition | External | The demographic representation and historical patterns in the data used to train the algorithm — biased data produces biased algorithms regardless of the algorithm's design |
| Feature Selection | External | The specific data variables (features) the algorithm uses to make predictions — including or excluding certain features can amplify or reduce bias; removing race doesn't help if proxy variables remain |
| Algorithm Fairness Constraint | External | Rules built into the algorithm that explicitly limit disparate impact — such as requiring equal false positive rates across demographic groups — but implementing fairness constraints involves trade-offs with overall accuracy |
| Prediction Accuracy | Internal | The overall correctness of the algorithm's decisions, measured by how often it correctly predicts outcomes — biased algorithms may have high overall accuracy while being systematically wrong for minority groups |
| Disparate Impact Ratio | Internal | The ratio of favorable outcomes for the disadvantaged group compared to the advantaged group — a ratio below 0.8 is generally considered evidence of discriminatory impact under US law |

### Research for Lesson
- How Machine Learning Learns Bias — reference materials and textbook resources
- The Proxy Variable Problem — reference materials and textbook resources
- Real-World Algorithmic Harm — reference materials and textbook resources
- Toward Algorithmic Fairness — reference materials and textbook resources

---

## Step 1: LOCATE — Build Your System

### Text Editor

```
CAN AN ALGORITHM BE RACIST?

Modeling Bias in Artificial Intelligence and Machine Learning.
If a computer algorithm trained on historical data makes decisions about who gets a loan, who gets hired, or who goes to jail — and the historical data reflects decades of racial discrimination — is the algorithm racist, or is it just doing math?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Training Data Composition" — the demographic representation and historical patterns in the data used to train the algorithm — biased data produces biased algorithms regardless of the algorithm's design
  ○ Click "Feature Selection" — the specific data variables (features) the algorithm uses to make predictions — including or excluding certain features can amplify or reduce bias; removing race doesn't help if proxy variables remain
  ○ Click "Algorithm Fairness Constraint" — rules built into the algorithm that explicitly limit disparate impact — such as requiring equal false positive rates across demographic groups — but implementing fairness constraints involves trade-offs with overall accuracy
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Prediction Accuracy" — the overall correctness of the algorithm's decisions
  ○ Click "Disparate Impact Ratio" — the ratio of favorable outcomes for the disadvantaged group compared to the advantaged group — a ratio below 0

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
"If a computer algorithm trained on historical data makes decisions about who gets a loan, who gets hired, or who goes to jail — and the historical data reflects decades of racial discrimination — is the algorithm racist, or is it just doing math?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Training Data Composition' — that's external. The demographic representation and historical patterns in the data used to train the algorithm — biased data produces biased algorithms regardless of the algorithm's design.
Click on 'Feature Selection' — that's external. The specific data variables (features) the algorithm uses to make predictions — including or excluding certain features can amplify or reduce bias; removing race doesn't help if proxy variables remain.
Click on 'Algorithm Fairness Constraint' — that's external. Rules built into the algorithm that explicitly limit disparate impact — such as requiring equal false positive rates across demographic groups — but implementing fairness constraints involves trade-offs with overall accuracy.
Click on 'Prediction Accuracy' — that's internal. The overall correctness of the algorithm's decisions.
Click on 'Disparate Impact Ratio' — that's internal. The ratio of favorable outcomes for the disadvantaged group compared to the advantaged group — a ratio below 0.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Training Data Composition, Feature Selection, and Algorithm Fairness Constraint are external components because they are deliberate design decisions made by developers and data scientists — they choose what data to use, what features to include, and whether to impose fairness requirements. Prediction Accuracy and Disparate Impact Ratio are internal components because they are measurable outcomes that emerge from the interaction of data, features, and algorithm design — they cannot be set directly but are determined by the design choices.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next step, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 5 components sorted: Training Data Composition, Feature Selection, Algorithm Fairness Constraint (External), Prediction Accuracy, Disparate Impact Ratio (Internal)]

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
• Click on "Training Data Composition" and drag an arrow to "Disparate Impact Ratio"
• Click on "Feature Selection" and drag an arrow to "Disparate Impact Ratio"
• Click on "Algorithm Fairness Constraint" and drag an arrow to "Prediction Accuracy"

Task C: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Training Data Composition → Disparate Impact Ratio = POSITIVE (+)
    If training data reflects historical discrimination — where certain demographic groups were systematically disadvantaged — the algorithm learns those patterns as 'normal' and reproduces them. Biased training data directly produces low Disparate Impact Ratios (discriminatory outcomes) regardless of the algorithm's design.

  ○ Feature Selection → Disparate Impact Ratio = POSITIVE (+)
    Including proxy variables (zip code, school name, credit score) that correlate with race allows the algorithm to discriminate even without explicit demographic features. Removing or carefully engineering features can reduce but not eliminate bias if the underlying training data is biased.

  ○ Algorithm Fairness Constraint → Prediction Accuracy = NEGATIVE (−)
    Imposing fairness constraints (e.g., requiring equal false positive rates across groups) typically reduces overall prediction accuracy by a small but measurable amount, because it forces the algorithm to sacrifice some predictive power to achieve equitable outcomes. Research shows this trade-off is usually modest (1-3% accuracy reduction) but not zero.

Task D: CHECK YOUR MODEL
• You should have 3 arrows total
• 1 negative relationship(s), 0 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: If a hiring algorithm is trained on 20 years of a company's data, and for those 20 years the company mostly hired white men for leadership positions, what will the algorithm 'learn' about who is qualified for leadership? It will learn that being a white man predicts success — not because that's true, but because that's what the data shows. The algorithm doesn't know the difference between correlation and causation.
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Training Data Composition' and drag an arrow
over to 'Disparate Impact Ratio.'

Here's the key question: When training data composition goes UP, does
disparate impact ratio go UP or DOWN?

If training data reflects historical discrimination — where certain demographic groups were systematically disadvantaged — the algorithm learns those patterns as 'normal' and reproduces them. Biased training data directly produces low Disparate Impact Ratios (discriminatory outcomes) regardless of the algorithm's design.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Feature Selection' and drag an arrow
over to 'Disparate Impact Ratio.'

Here's the key question: When feature selection goes UP, does
disparate impact ratio go UP or DOWN?

Including proxy variables (zip code, school name, credit score) that correlate with race allows the algorithm to discriminate even without explicit demographic features. Removing or carefully engineering features can reduce but not eliminate bias if the underlying training data is biased.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'Algorithm Fairness Constraint' and drag an arrow
over to 'Prediction Accuracy.'

Here's the key question: When algorithm fairness constraint goes UP, does
prediction accuracy go UP or DOWN?

Imposing fairness constraints (e.g., requiring equal false positive rates across groups) typically reduces overall prediction accuracy by a small but measurable amount, because it forces the algorithm to sacrifice some predictive power to achieve equitable outcomes. Research shows this trade-off is usually modest (1-3% accuracy reduction) but not zero.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Look at your model now. You've got 1 negative and 0
positive relationships. 3 arrows total.

If a hiring algorithm is trained on 20 years of a company's data, and for those 20 years the company mostly hired white men for leadership positions, what will the algorithm 'learn' about who is qualified for leadership? It will learn that being a white man predicts success — not because that's true, but because that's what the data shows. The algorithm doesn't know the difference between correlation and causation.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Training Data Composition +→ Disparate Impact Ratio, Feature Selection +→ Disparate Impact Ratio, Algorithm Fairness Constraint −→ Prediction Accuracy]

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
• When Training Data Composition is HIGH, what happens to the internal components?

Task C: SCENARIO — BIASED HISTORICAL DATA
• Training data: 20 years of historical hiring with demographic imbalance | No fairness constraints
• PREDICT FIRST: Do you predict the algorithm's overall accuracy will be high or low? What about its accuracy specifically for minority applicants?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task D: SCENARIO — DEBIASED TRAINING DATA
• Training data: Balanced demographic representation | No fairness constraints
• PREDICT FIRST: If we balance the training data, do you predict overall accuracy will increase, decrease, or stay the same? What happens to the disparate impact ratio?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task E: SCENARIO — FAIRNESS-CONSTRAINED ALGORITHM
• Training data: Original biased data | Fairness constraint: Equal false positive rates
• PREDICT FIRST: If we force the algorithm to make errors at equal rates for all groups, do you predict this will increase or decrease overall accuracy? Is this trade-off worth it?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Algorithms trained on biased historical data reproduce and amplify existing discrimination — high overall accuracy can mask systematic bias against specific demographic groups because the majority group dominates the accuracy metric
• Removing explicit demographic variables (race, gender) from the algorithm does NOT eliminate bias because proxy variables (zip code, school name, arrest history) carry the same information due to historical segregation and discrimination
• Debiasing training data significantly improves fairness (higher Disparate Impact Ratio) with minimal loss of overall prediction accuracy — proving that much of the bias was noise, not signal
• Fairness constraints create a real but modest trade-off with overall accuracy — society must decide whether a small decrease in overall accuracy is an acceptable price for preventing algorithmic discrimination in life-changing decisions

THE ANSWER: An algorithm absolutely can be racist — not because it has intent or beliefs, but because it learns from data that reflects a racist world. When a machine learning system is trained on historical data from a society with decades of racial discrimination in hiring, lending, policing, and housing, it learns patterns that encode those disparities as 'normal.' It then reproduces those patterns at scale, with the veneer of mathematical objectivity. The algorithm doesn't need to use race explicitly — proxy variables like zip code, school district, and credit history carry racial information because of historical segregation. The result is a system that systematically disadvantages people of color while appearing fair. The science shows three paths forward: debias the training data, add fairness constraints to the algorithm, and always audit automated systems for disparate impact before deployment. The most dangerous myth is that algorithms are inherently objective — they are only as fair as the data and values humans build into them.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Biased Historical Data. Training data: 20 years of historical hiring with demographic imbalance | No fairness constraints.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Debiased Training Data.
Training data: Balanced demographic representation | No fairness constraints.

Before you run it — make a prediction. If we balance the training data, do you predict overall accuracy will increase, decrease, or stay the same? What happens to the disparate impact ratio?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Fairness-Constrained Algorithm. Training data: Original biased data | Fairness constraint: Equal false positive rates.
If we force the algorithm to make errors at equal rates for all groups, do you predict this will increase or decrease overall accuracy? Is this trade-off worth it?

Here's what our model reveals: An algorithm absolutely can be racist — not because it has intent or beliefs, but because it learns from data that reflects a racist world. When a machine learning system is trained on historical data from a society with decades of racial discrimination in hiring, lending, policing, and housing, it learns patterns that encode those disparities as 'normal.' It then reproduces those patterns at scale, with the veneer of mathematical objectivity. The algorithm doesn't need to use race explicitly — proxy variables like zip code, school district, and credit history carry racial information because of historical segregation. The result is a system that systematically disadvantages people of color while appearing fair. The science shows three paths forward: debias the training data, add fairness constraints to the algorithm, and always audit automated systems for disparate impact before deployment. The most dangerous myth is that algorithms are inherently objective — they are only as fair as the data and values humans build into them.

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
CONFIGURE CONNECTION CONDITIONS — MODEL REFINEMENT

Your current model treats the Training Data Composition → Disparate Impact Ratio relationship as
unconditional. However, this relationship is scientifically
contingent on Feature Selection being active. Without this condition,
the simulation produces inaccurate results: Training Data Composition drives Disparate Impact Ratio
even when the prerequisite state is not met.

Task A: CONFIGURE THE CONNECTION CONDITION
   • Select the connection arrow: Training Data Composition → Disparate Impact Ratio
   • Click "Conditions" in the connection toolbar
   • Set the regulator condition: IF Feature Selection is ON
   • Click "Save Conditions"

Task B: VALIDATE THE CONDITIONAL MODEL
   • Run the simulation with Feature Selection active and observe
     how Training Data Composition's effect on Disparate Impact Ratio is now gated
   • Toggle Feature Selection ON/OFF while Training Data Composition remains constant
   • Verify that Disparate Impact Ratio only responds to Training Data Composition when the
     condition is satisfied

Task C: ADDITIONAL CONDITION
   • Select: Feature Selection → Disparate Impact Ratio
   • Set condition: IF Training Data Composition is ON
   • This ensures Feature Selection's effect on Disparate Impact Ratio
     is contingent on Training Data Composition being active

These conditional relationships capture critical system behavior:
not all connections operate continuously. Some are gated by the
state of other components, creating the non-linear dynamics that
characterize real-world complex systems.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NOW LET'S PLAY AND EXPLORE

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
   • What happens if you turn OFF Training Data Composition?
   • What happens if you turn OFF Feature Selection?
   • What happens if you turn OFF Algorithm Fairness Constraint?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Feedback Loop Amplification — The tendency for biased algorithmic decisions to generate new biased data that further trains the algorithm — for example, if a predictive policing algorithm sends more officers to Black neighborhoods, more arrests occur there, generating data that 'confirms' the algorithm's prediction
   • Transparency Level — The degree to which the algorithm's decision-making process is interpretable and auditable — 'black box' deep learning models make accurate predictions but cannot explain WHY, making bias detection extremely difficult
   • Stakeholder Impact — The severity of consequences for individuals affected by biased algorithmic decisions — being wrongly denied a job is harmful; being wrongly denied medical treatment or bail is potentially life-threatening

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • How Machine Learning Learns Bias — how does this connect to your model?
   • The Proxy Variable Problem — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model demonstrate that mathematical objectivity does not guarantee fairness?
   • Why does removing race from the algorithm's feature set fail to eliminate racial bias?
   • What does your model reveal about the relationship between overall accuracy and demographic fairness — are they always in tension?
   • Who should be responsible for ensuring algorithms are fair — the developers, the companies that deploy them, or the government?

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

Feedback Loop Amplification. The tendency for biased algorithmic decisions to generate new biased data that further trains the algorithm — for example, if a predictive policing algorithm sends more officers to Black neighborhoods, more arrests occur there, generating data that 'confirms' the algorithm's prediction
How would you model that?

Transparency Level. The degree to which the algorithm's decision-making process is interpretable and auditable — 'black box' deep learning models make accurate predictions but cannot explain WHY, making bias detection extremely difficult
How would you model that?

Stakeholder Impact. The severity of consequences for individuals affected by biased algorithmic decisions — being wrongly denied a job is harmful; being wrongly denied medical treatment or bail is potentially life-threatening
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

AI Ethics Researchers study the social impact of artificial intelligence and develop frameworks for responsible AI deployment, earning $90,000–$180,000/year at tech companies, universities, and policy organizations. Algorithmic Auditors inspect automated decision systems for bias and fairness compliance, earning $85,000–$160,000/year. Data Scientists who specialize in fairness-aware machine learning earn $100,000–$200,000/year at leading tech companies.

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
Visual: Title slide with algorithm interface and human impact imagery
Say: "An algorithm decides whether you get a loan, a job, or bail from jail. It doesn't know your race. But it knows your zip code, your school, and your credit score — and in America, those tell the same story."
Do: Show the ProPublica COMPAS investigation headline. Ask: How can an algorithm that never sees your race still discriminate based on race?
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and vocabulary terms
Say: "Today we're putting AI on trial. We're going to build a model that shows exactly how bias gets into algorithms and exactly what it takes to get it out."
Do: Have students read objectives. Pre-teach 'proxy variable' and 'disparate impact' with concrete examples (zip code as proxy for race).
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: Algorithm code overlaid on diverse faces
Say: "If an algorithm is just doing math on historical data — and the history is racist — who is responsible for the racist outcome? The data? The programmer? The company? Society?"
Do: Quick-write: Students write who they think is responsible when an algorithm produces discriminatory outcomes. Discussion: Can math be racist?
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps overview
Say: "We're going to train an algorithm, measure its bias, try to fix it, and discover the trade-offs involved in making AI fair."
Do: Preview LEVER steps. Emphasize that this is about measuring bias with data, not just arguing about it.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Component cards for algorithmic bias model
Say: "What determines whether an algorithm is fair? Some factors are choices developers make, others are measurable outcomes."
Do: Guide sorting: Training Data Composition, Feature Selection, and Fairness Constraints are external (developer choices). Prediction Accuracy and Disparate Impact Ratio are internal (measurable outcomes).
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows between components
Say: "Biased data in, biased decisions out. But the proxy variable connection is the sneakiest: you can remove race from the data and the algorithm STILL discriminates. Let's trace how."
Do: Students map the path from historical discrimination through training data to proxy variables to disparate impact. Key insight: removing race doesn't remove racism from the data.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Bias audit results for three algorithm configurations
Say: "Let's run three versions of the same hiring algorithm: the default trained on biased data, one with debiased data, and one with a fairness constraint. Which one is fair? Which one is accurate? Can you have both?"
Do: Students predict accuracy and fairness metrics for each configuration. Run simulations. Analyze the accuracy-fairness trade-off.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key findings — bias audit results and comparison
Say: "The model proves two things: first, algorithms CAN be racist even without using race. Second, we CAN make them fairer — but it requires deliberate effort and value judgments that math alone can't provide."
Do: Discuss: If the trade-off between accuracy and fairness is small, why haven't all companies fixed their algorithms? What incentives work against fairness?
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Algorithmic audit design challenge
Say: "A tech company's AI hiring system is discriminating by zip code. You've been hired to audit it, find the bias, and fix it. Your evidence has to be so strong it would hold up in court."
Do: Groups design audit protocols, test hypotheses about proxy variables, and propose corrections with quantified fairness improvements. Present findings.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: Can an Algorithm Be Racist?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
In 2016, ProPublica investigated COMPAS, an algorithm used across the United States to predict whether criminal defendants would reoffend. They found that the algorithm was twice as likely to falsely label Black defendants as high-risk compared to white defendants. The algorithm never used race as an input variable. This investigation revealed a fundamental truth about artificial intelligence: algorithms are not objective — they are mirrors that reflect the biases embedded in the data they learn from.

NGSS ALIGNMENT:
HS-ETS1-1, HS-ETS1-4: Analyze a major global challenge to specify qualitative and quantitative criteria and constraints for solutions that account for societal needs and wants. Use a computer simulation to model the impact of proposed solutions to a complex real-world problem with numerous criteria and constraints on interactions within and between systems relevant to the problem.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Using Mathematics and Computational Thinking
  Students use computational simulations to model how training data composition and algorithm design choices produce measurably different outcomes for different demographic groups.
• Disciplinary Core Idea: ETS1.A Defining and Delimiting Engineering Problems / ETS1.B Developing Possible Solutions
  Algorithmic fairness is an engineering design problem that requires specifying quantitative criteria (disparate impact ratio, error rate parity) and constraints (accuracy, cost, legal compliance) while accounting for societal needs and values.
• Crosscutting Concept: Cause and Effect
  Students trace the causal pathway from historical discrimination through biased training data to disparate algorithmic outcomes, identifying how proxy variables transmit racial information even when race is not explicitly used.

PACING GUIDE:
• Step 1 (Locate): 8-10 minutes
• Step 2 (Establish): 8-10 minutes
• Step 3 (Visualize & Evaluate): 10-12 minutes
• Step 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Training Data, Algorithmic Bias, Disparate Impact, Proxy Variable
□ Prepare If a computer algorithm trained on historical data makes decisions about who gets a loan, who gets hired, or who goes to jail — and the historical data reflects decades of racial discrimination — is the algorithm racist, or is it just doing math discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify training data composition, feature selection, algorithm fairness constraint, prediction accuracy, and disparate impact ratio as the key components of the algorithmic bias system.
• Establish: Students determine that training data composition, feature selection, and fairness constraints are external design choices made by developers, while prediction accuracy and disparate impact ratio are outcomes determined by the interaction of data, algorithm design, and the underlying patterns in the data.
• Visualize: Students build a computational model that simulates how biased training data flows through a machine learning pipeline to produce measurably different outcomes for different demographic groups.
• Evaluate: Students run biased historical data, debiased training data, and fairness-constrained algorithm scenarios to quantify how different interventions affect both accuracy and fairness.
• Revise: Students add feedback loop amplification, transparency level, or stakeholder impact to explore how bias compounds over time and how the consequences vary across different decision domains.

BACKGROUND CONTENT:
• How Machine Learning Learns Bias:
  Machine learning algorithms find patterns in data. If the historical data contains discriminatory patterns — and virtually all real-world data does — the algorithm will learn and replicate those patterns. A hiring algorithm trained on a tech company's 20-year hiring history will learn that successful hires tend to be white and male, not because those demographics are more capable, but because historical hiring decisions were biased. The algorithm cannot distinguish between genuine performance predictors and artifacts of discrimination.

• The Proxy Variable Problem:
  Even when developers remove explicit demographic variables (race, gender, ethnicity) from an algorithm's input features, bias persists through proxy variables — seemingly neutral data points that are strongly correlated with protected characteristics due to historical patterns. Zip code predicts race because of residential segregation caused by redlining. School name predicts socioeconomic status. Arrest history predicts race because of discriminatory policing. Credit score predicts race because of disparities in lending and employment. An algorithm using these proxies can produce racially discriminatory outcomes while appearing race-blind.

• Real-World Algorithmic Harm:
  Algorithmic bias is not theoretical — it is causing measurable harm today. Amazon scrapped an AI hiring tool in 2018 after discovering it systematically downgraded resumes containing the word 'women's.' Healthcare algorithms used by hospitals across the US were found to systematically underestimate the health needs of Black patients, reducing their access to care. Facial recognition systems have error rates 10-100x higher for dark-skinned women than light-skinned men. Predictive policing algorithms send more officers to Black neighborhoods, generating more arrests that 'confirm' the algorithm's predictions in a vicious feedback loop.

• Toward Algorithmic Fairness:
  Researchers have developed multiple mathematical definitions of fairness, including demographic parity (equal selection rates), equalized odds (equal error rates), and calibration (equal accuracy of risk scores). The challenge is that these definitions are mathematically incompatible — satisfying one often violates another. This means algorithmic fairness requires VALUE JUDGMENTS about which type of fairness matters most in each context. Technical solutions include debiasing training data, adding fairness constraints during model training, and post-processing outputs to equalize metrics. But ultimately, ensuring algorithms are fair requires governance: mandatory bias audits, impact assessments, transparency requirements, and meaningful human oversight of automated decisions that affect people's lives.

COMMON MISCONCEPTIONS:
• "Algorithms are inherently objective because they use math, not feelings"
  Reality: Algorithms are built by humans, trained on human data, and optimized for human-defined objectives. Every step involves human choices: what data to collect, what features to include, what outcome to predict, what metric to optimize. These choices embed values and biases. The math itself may be neutral, but the inputs and objectives are profoundly human. An algorithm trained on biased data will produce biased outputs with mathematical precision — it is objectively implementing subjective bias.
  Strategy: Analogy: A calculator is objective — it will always say 2+2=4. But if a biased person gives it biased inputs, the 'objective' output is still wrong. Ask: Who chose the inputs? Who defined 'success'? Who benefits from the definition used?

• "If the algorithm is accurate overall, it must be fair"
  Reality: High overall accuracy can mask severe unfairness for minority groups. An algorithm with 85% overall accuracy might have 90% accuracy for the majority group and 60% accuracy for the minority group — because the majority group dominates the overall metric. This is why disaggregated metrics are essential: you must measure accuracy and error rates separately for each demographic group to detect disparate impact. The model clearly shows that 'accurate on average' does not mean 'fair for everyone.'
  Strategy: Run the model and show overall accuracy (82%) next to accuracy broken down by group (majority: 88%, minority: 64%). Ask: Is this algorithm fair? Is 82% accuracy a meaningful number if it's hiding a 24-point gap between groups?

• "Just remove race from the data and the algorithm will be fair"
  Reality: This is perhaps the most dangerous misconception because it feels so intuitive. Removing race from the input features changes almost nothing about the algorithm's outputs because proxy variables — zip code, school district, credit score, arrest record — carry racial information through historical correlations. In a segregated society, race is encoded in nearly every socioeconomic variable. True fairness requires active intervention: auditing outcomes by demographic, testing for proxy effects, imposing fairness constraints, and ongoing monitoring.
  Strategy: Demonstrate with the model: remove the race variable and show that the Disparate Impact Ratio barely changes. Then show which proxy variables carry the most racial information. Ask: If removing race doesn't help, what does?

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
Big Question: If a computer algorithm trained on historical data makes decisions about who gets a loan, who gets hired, or who goes to jail — and the historical data reflects decades of racial discrimination — is the algorithm racist, or is it just doing math?
Answer: An algorithm absolutely can be racist — not because it has intent or beliefs, but because it learns from data that reflects a racist world. When a machine learning system is trained on historical data from a society with decades of racial discrimination in hiring, lending, policing, and housing, it learns patterns that encode those disparities as 'normal.' It then reproduces those patterns at scale, with the veneer of mathematical objectivity. The algorithm doesn't need to use race explicitly — proxy variables like zip code, school district, and credit history carry racial information because of historical segregation. The result is a system that systematically disadvantages people of color while appearing fair. The science shows three paths forward: debias the training data, add fairness constraints to the algorithm, and always audit automated systems for disparate impact before deployment. The most dangerous myth is that algorithms are inherently objective — they are only as fair as the data and values humans build into them.

Simulation Answers:
• Biased Historical Data Scenario: The algorithm trained on 20 years of biased hiring data achieves high overall Prediction Accuracy (82%) because the majority group dominates the evaluation metric. However, accuracy for minority applicants is significantly lower (64%), and the Disparate Impact Ratio is 0.58 — well below the legal threshold of 0.8. The algorithm has learned that zip codes, schools, and activity patterns associated with white candidates predict 'success' not because of actual qualifications but because historical hiring was biased toward those candidates.
• Fairness-Constrained Algorithm Scenario: Adding a fairness constraint that requires equal false positive rates across demographic groups reduces overall Prediction Accuracy from 82% to 79% — a modest 3% decrease. But the Disparate Impact Ratio improves dramatically from 0.58 to 0.84, crossing the legal threshold. The fairness constraint forces the algorithm to rely less on proxy variables and more on genuinely predictive features. The 3% accuracy trade-off means 3 fewer correct predictions out of 100 — a small price for eliminating systematic discrimination.

Reflection Exemplars:
• Q: Why doesn't removing race from the algorithm eliminate racial bias?
  A: My model demonstrates that removing the race variable has almost no effect on the Disparate Impact Ratio because proxy variables carry the same information through different channels. Zip code predicts race because of residential segregation caused by historical redlining. School name predicts race because of school district boundaries drawn along racial lines. Credit score predicts race because of discriminatory lending and employment practices. The algorithm doesn't need to 'see' race directly — it reconstructs racial information from the structural consequences of racism embedded in every other variable. This is why fairness requires actively auditing outcomes, not just removing obvious demographic variables.
• Q: Who is responsible when an algorithm produces discriminatory outcomes?
  A: Responsibility is shared across multiple levels. The historical data reflects societal discrimination — we all inherit that. But the developers CHOSE that data and those features. The company CHOSE to deploy the algorithm without auditing for bias. And the regulators FAILED to require bias testing. My model shows that bias is detectable and correctable — debiasing and fairness constraints work. This means discriminatory outcomes from algorithms are not inevitable; they are the result of choices not to test, not to audit, and not to correct. When solutions exist and are not implemented, responsibility falls on those who had the power to act and didn't.

STEM CHALLENGE GUIDANCE:
Title: Design a Fair Hiring Algorithm Audit
Mission: Design an audit protocol for a company's AI hiring system that identifies bias, quantifies disparate impact, and recommends evidence-based corrections to achieve equitable outcomes.
Scenario: A major tech company uses an AI system to screen 500,000 job applications per year. An internal review found that the system recommends candidates from predominantly white zip codes at 3x the rate of candidates from predominantly Black zip codes, even after controlling for qualifications. The company hired your algorithmic fairness team to audit the system, identify sources of bias, and recommend corrections that achieve a Disparate Impact Ratio above 0.8 without significantly reducing the quality of hires.
Introduction: Present the challenge: A tech company's AI hiring system has been flagged for discriminating by zip code, producing a Disparate Impact Ratio of 0.58. Your algorithmic fairness team must audit the system, identify the sources of bias, test corrections, and produce a recommendation that brings the ratio above 0.8 with minimal accuracy loss.

Key Concepts:
• Confusion Matrices by Demographic: Breaking down algorithm errors (false positives, false negatives) separately for each demographic group reveals whether the algorithm makes systematically different kinds of errors for different people. Equal overall accuracy can hide wildly different error patterns across groups.
• Intersectionality in Algorithmic Bias: Bias often compounds at the intersection of multiple identities — a system may show acceptable metrics for Black men and white women separately, but Black women experience significantly worse outcomes because they face both racial and gender bias simultaneously. Audits must examine intersectional subgroups.
• Algorithmic Impact Assessment: A structured evaluation conducted before deploying an automated decision system, assessing potential harms, affected populations, data quality, fairness metrics, appeal mechanisms, and human oversight requirements — analogous to an Environmental Impact Assessment for construction projects.

Evaluation Rubric:
• Expert (4): Audit identifies specific proxy variables, quantifies disparate impact with statistical evidence, proposes corrections with model data showing improvement, addresses accuracy-fairness trade-off, and includes ongoing monitoring plan
• Proficient (3): Audit identifies likely sources of bias, proposes reasonable corrections with some model evidence, and considers the accuracy-fairness trade-off
• Developing (2): Audit identifies bias exists but lacks specific statistical evidence, detailed correction proposal, or consideration of trade-offs
• Beginning (1): Audit is incomplete, does not use model data to quantify bias, or proposes corrections without evidence

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a visual showing how zip code correlates with race in a sample city, connecting the concept of proxy variables to tangible geography
  • Use a simplified confusion matrix template that students can fill in separately for each demographic group to see disparate error rates
  • Sentence frames: 'Our audit found that the algorithm's __ feature serves as a proxy for __ because __. Removing this feature and adding a __ fairness constraint improved the Disparate Impact Ratio from __ to __ while reducing overall accuracy by only __%'

Extensions (Advanced Learners):
  • Research the COMPAS recidivism algorithm studied by ProPublica — replicate their analysis using your model and evaluate whether the algorithm's definition of 'accuracy' was hiding racial bias in error rates
  • Investigate facial recognition accuracy disparities — research the work of Joy Buolamwini and Timnit Gebru on demographic error rate differences and design a model that tests whether debiased training data improves accuracy for dark-skinned faces
  • Design an Algorithmic Impact Assessment template for your school — identify any automated decision systems used (grading algorithms, discipline prediction, college recommendation) and propose an audit framework

Cross-Curricular Connections:
  • Math: Calculate the Disparate Impact Ratio for a hiring algorithm: if 40% of white applicants are selected and 22% of Black applicants are selected, what is the ratio? Is it above or below the 0.8 threshold? If the algorithm switches to a debiased model and selects 36% of white and 31% of Black applicants, what is the new ratio?
  • ELA: Write a legal brief arguing that a company should be held liable for discriminatory outcomes from its AI hiring system, even though the algorithm never explicitly uses race. Use evidence from your model to demonstrate how proxy variables produce disparate impact and how available corrections were not implemented.
  • History: Research the history of 'scientific' racism — from phrenology to IQ testing to modern algorithmic bias. How has the appearance of mathematical objectivity been used throughout history to justify discrimination? What patterns do you see repeating in AI today?

CAST ALIGNMENT:
• Model how biased training data produces discriminatory algorithmic outputs even without explicit use of demographic variables
• Quantify disparate impact using statistical metrics and identify which features drive demographic differences in outcomes
• Evaluate trade-offs between overall prediction accuracy and demographic fairness in algorithmic decision systems

CAST-Style Assessment Questions:
• Multiple Choice: A lending algorithm trained on historical data denies loan applications from predominantly Black zip codes at twice the rate of predominantly white zip codes, even though it does not use race as an input variable. What is the most likely explanation? A) The algorithm is functioning correctly, B) Zip code is serving as a proxy variable for race, C) The algorithm has a programming error, D) Black applicants are genuinely less creditworthy
• Constructed Response: Using your model, explain why removing race from an algorithm's feature set does not eliminate racial bias. Describe the role of proxy variables and provide a specific example from your simulation showing how bias persists after removing demographic features.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: Can an Algorithm Be Racist?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Do you think a computer program can be biased or unfair? How is that possible if it's just following mathematical rules?

   _________________________________________________________

   _________________________________________________________

2. If an algorithm is trained on data from a world with racial discrimination, what do you think it will learn?

   _________________________________________________________

   _________________________________________________________

3. Should algorithms be used to make important decisions about people's lives — like who gets a job, a loan, or bail from jail? Why or why not?

   _________________________________________________________

   _________________________________________________________

4. What do you think the word 'fair' means when applied to an algorithm — equal treatment, equal outcomes, or something else?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Training Data                 
___ Algorithmic Bias              
___ Disparate Impact              
___ Proxy Variable                

A. The historical dataset used to teach a machine learning algorithm patterns and relationships — if the historical data contains racial, gender, or socioeconomic biases, the algorithm will learn and replicate those biases in its predictions
B. Systematic discrimination in the outputs of a computer algorithm caused by biased training data, biased feature selection, or biased evaluation metrics — algorithms can appear objective while encoding the prejudices embedded in the data they learned from
C. A legal and statistical concept where a seemingly neutral practice disproportionately harms a protected group — even if an algorithm never explicitly uses race, it can use proxy variables (zip code, school name, credit history) that are strongly correlated with race due to historical segregation
D. A data feature that is not directly discriminatory but is highly correlated with a protected characteristic due to historical patterns — for example, zip code serves as a proxy for race in many American cities because of residential segregation caused by redlining

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

SCENARIO: Biased Historical Data
Settings: Training data: 20 years of historical hiring with demographic imbalance | No fairness constraints
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Debiased Training Data
Settings: Training data: Balanced demographic representation | No fairness constraints
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Fairness-Constrained Algorithm
Settings: Training data: Original biased data | Fairness constraint: Equal false positive rates
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

1. How does your model demonstrate that mathematical objectivity does not guarantee fairness?

   _________________________________________________________

   _________________________________________________________

2. Why does removing race from the algorithm's feature set fail to eliminate racial bias?

   _________________________________________________________

   _________________________________________________________

3. What does your model reveal about the relationship between overall accuracy and demographic fairness — are they always in tension?

   _________________________________________________________

   _________________________________________________________

4. Who should be responsible for ensuring algorithms are fair — the developers, the companies that deploy them, or the government?

   _________________________________________________________

   _________________________________________________________

5. What limitations does your model have in capturing the full complexity of algorithmic discrimination in the real world?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. If a computer algorithm trained on historical data makes decisions about who gets a loan, who gets hired, or who goes to jail — and the historical data reflects decades of racial discrimination — is the algorithm racist, or is it just doing math? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Using Mathematics and Computational Thinking
   □ Disciplinary Core Idea: ETS1.A Defining and Delimiting Engineering Problems / ETS1.B Developing Possible Solutions
   □ Crosscutting Concept: Cause and Effect

3. What limitations does your model have in capturing the full complexity of algorithmic discrimination in the real world?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Fair Hiring Algorithm Audit
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design an audit protocol for a company's AI hiring system that identifies bias, quantifies disparate impact, and recommends evidence-based corrections to achieve equitable outcomes.

SCENARIO: A major tech company uses an AI system to screen 500,000 job applications per year. An internal review found that the system recommends candidates from predominantly white zip codes at 3x the rate of candidates from predominantly Black zip codes, even after controlling for qualifications. The company hired your algorithmic fairness team to audit the system, identify sources of bias, and recommend corrections that achieve a Disparate Impact Ratio above 0.8 without significantly reducing the quality of hires.

GUIDING QUESTIONS:
• Which features in the hiring algorithm are acting as proxy variables for race, and how does your model demonstrate this?
• What specific changes to training data or algorithm design does your model show will bring the Disparate Impact Ratio above 0.8?
• What trade-off does your model reveal between overall prediction accuracy and demographic fairness — and is the trade-off acceptable?

DESIGN THINKING:
• What data will you need to access to conduct a thorough bias audit, and what metrics will you use to measure fairness?

  _________________________________________________________

• How will you distinguish between features that genuinely predict job performance and features that are proxies for demographics?

  _________________________________________________________

• What fairness constraint will you recommend, and how does it affect outcomes for both majority and minority applicants?

  _________________________________________________________

• How will you ensure the corrected algorithm doesn't develop new biases over time as it processes new data?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Audit identifies specific proxy variables, quantifies disparate impact with statistical evidence, proposes corrections with model data showing improvement, addresses accuracy-fairness trade-off, and includes ongoing monitoring plan
• Proficient (3): Audit identifies likely sources of bias, proposes reasonable corrections with some model evidence, and considers the accuracy-fairness trade-off
• Developing (2): Audit identifies bias exists but lacks specific statistical evidence, detailed correction proposal, or consideration of trade-offs
• Beginning (1): Audit is incomplete, does not use model data to quantify bias, or proposes corrections without evidence

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CAST-Aligned Pre/Post Assessment

### Administration Instructions

These 5 multiple-choice questions are administered identically as both a pre-assessment (before Activity 1) and a post-assessment (after Activity 4). Score each out of 5. Learning growth = post-score minus pre-score.

Questions follow the California Science Test (CAST) stimulus-response format. Each item is three-dimensional, assessing a Science and Engineering Practice (SEP), Disciplinary Core Idea (DCI), and Crosscutting Concept (CCC) simultaneously, aligned to HS-ETS1-1, HS-ETS1-4.

---

### Question 1

CAST Alignment: SEP 2.1.1 (Develop and use a model to represent relationships) + DCI ETS1.A (Define and delimit engineering problems) + CCC4 (Systems and system models)

A data science team audits a predictive policing algorithm deployed across a California city. The algorithm analyzes historical crime data to predict where future crimes will occur and recommends patrol allocation accordingly. Analysis reveals that neighborhoods with higher historical arrest rates receive disproportionately more patrol allocation, which in turn generates more arrests in those same neighborhoods, regardless of whether actual crime rates differ. The team maps this as a system with feedback dynamics.

A student's model shows that retraining a hiring algorithm on demographically balanced data improves the Disparate Impact Ratio from 0.62 to 0.89, but overall Prediction Accuracy drops from 92% to 86%. A stakeholder argues the accuracy loss is unacceptable. Which response best applies systems thinking to evaluate this trade-off?

A. The algorithm should be abandoned entirely because no level of accuracy justifies deployment
B. The 6% accuracy drop reflects the removal of discriminatory patterns that inflated apparent accuracy by systematically disadvantaging one group; the 'lost' accuracy was built on bias, not genuine predictive power
C. The model proves that fairness and accuracy are always in direct conflict
D. The stakeholder is correct because accuracy should always be maximized

Correct Answer: B

Feedback: The model reveals that the original 92% accuracy was partly achieved by exploiting biased patterns in historical data. Those patterns predicted who was SELECTED in the past, not who was QUALIFIED. Removing bias exposes that some of the original accuracy was discriminatory signal, not genuine predictive power. If you chose D, this response overgeneralizes without considering the specific mechanisms and evidence presented. Consider what the algorithm was actually predicting at 92% accuracy. If it was predicting who got hired in a biased system, it was predicting bias, not merit. The accuracy decrease when bias is removed suggests some of the original accuracy was built on discriminatory patterns. If you chose C, this answer overgeneralizes without considering the specific mechanisms and evidence presented. Consider what the algorithm was actually predicting at 92% accuracy. If it was predicting who got hired in a biased system, it was predicting bias, not merit. The accuracy decrease when bias is removed suggests some of the original accuracy was built on discriminatory patterns. If you chose A, this choice does not account for the key mechanism or relationship the evidence demonstrates. Consider what the algorithm was actually predicting at 92% accuracy. If it was predicting who got hired in a biased system, it was predicting bias, not merit. The accuracy decrease when bias is removed suggests some of the original accuracy was built on discriminatory patterns.
---

### Question 2

CAST Alignment: SEP 2.1.2 (Determine relationships among system components) + DCI ETS1.A (Define and delimit engineering problems) + CCC2 (Cause and effect)

A computational model of algorithmic bias in hiring software reveals a reinforcement cycle. The algorithm is trained on 10 years of historical hiring data from a technology company that was 78% male. When the model scores new applicants, it assigns higher rankings to resumes with features correlated with male applicants (certain universities, specific extracurricular activities, aggressive language patterns). A student is analyzing how the training data creates a self-reinforcing bias loop.

The model demonstrates that adding a fairness constraint (equal false positive rates across groups) reduces the Disparate Impact Ratio to 1.0 (perfect parity) but reveals a new problem: the algorithm now rejects qualified candidates from the majority group at a higher rate. Which concept best describes this outcome?

A. An error in the fairness constraint implementation
B. A fairness-accuracy trade-off where constraining for equal false positive rates redistributes error across groups, revealing that multiple valid definitions of fairness can conflict with each other
C. Evidence that algorithms should never use fairness constraints
D. Reverse discrimination, proving that fairness constraints are inherently unjust

Correct Answer: B

Feedback: The model reveals a fundamental insight in algorithmic fairness: there are multiple mathematically valid definitions of fairness (equal false positive rates, equal false negative rates, demographic parity), and satisfying one can violate another. This is the impossibility theorem in action. If you chose D, this response does not account for the key mechanism or relationship the evidence demonstrates. The model shows something deeper than simple reverse discrimination. There are multiple valid ways to define fairness, and they can mathematically conflict. Equal false positive rates, equal false negative rates, and equal selection rates cannot all be satisfied simultaneously in most real-world data. If you chose A, this answer assumes the model or data is flawed rather than analyzing what the evidence actually shows. The model shows something deeper than simple reverse discrimination. There are multiple valid ways to define fairness, and they can mathematically conflict. Equal false positive rates, equal false negative rates, and equal selection rates cannot all be satisfied simultaneously in most real-world data. If you chose C, this choice does not account for the key mechanism or relationship the evidence demonstrates. The model shows something deeper than simple reverse discrimination. There are multiple valid ways to define fairness, and they can mathematically conflict. Equal false positive rates, equal false negative rates, and equal selection rates cannot all be satisfied simultaneously in most real-world data.
---

### Question 3

CAST Alignment: SEP 2.1.2 (Determine relationships among components) + DCI ETS1.B (Use computer simulations to model solutions) + CCC4 (Describe components and interactions)

Researchers compare outcomes from two lending algorithms used by different banks. Algorithm A uses zip code, education level, and employment history as primary factors, but these variables correlate strongly with race due to historical segregation and educational inequality. Algorithm B uses income, debt-to-income ratio, and payment history without location-based variables. Analysis shows that Algorithm A denies loans to qualified minority applicants at 2.4 times the rate of equally qualified white applicants, while Algorithm B shows no significant racial disparity in denial rates.

A student discovers that their model's algorithm uses 'years of experience' as a top predictive feature. In a field where women were historically excluded before 1990, this feature correlates strongly with gender for workers over 35. Which model-based intervention would most effectively address this bias?

A. Cap the maximum value of 'years of experience' at a level that postdates the historical exclusion period, neutralizing its proxy effect while retaining its legitimate predictive value for recent cohorts
B. Double the weight of 'years of experience' to reward long careers
C. Replace 'years of experience' with age, which is more objective
D. Remove 'years of experience' entirely from the algorithm

Correct Answer: A

Feedback: Capping experience at a post-exclusion threshold (e.g., 15 years) preserves the feature's legitimate predictive value for recent career progression while neutralizing its role as a gender proxy for workers whose career length was artificially shortened by historical discrimination. If you chose D, this response does not account for the key mechanism or relationship the evidence demonstrates. The challenge is that 'years of experience' has both legitimate predictive value AND serves as a proxy for historical gender discrimination. Simply removing it loses useful information. Consider an approach that retains its value while neutralizing its discriminatory correlation. If you chose B, this answer does not account for the key mechanism or relationship the evidence demonstrates. The challenge is that 'years of experience' has both legitimate predictive value AND serves as a proxy for historical gender discrimination. Simply removing it loses useful information. Consider an approach that retains its value while neutralizing its discriminatory correlation. If you chose C, this choice does not account for the key mechanism or relationship the evidence demonstrates. The challenge is that 'years of experience' has both legitimate predictive value AND serves as a proxy for historical gender discrimination. Simply removing it loses useful information. Consider an approach that retains its value while neutralizing its discriminatory correlation.
---

### Question 4

CAST Alignment: SEP 2.1.4 (Represent mechanisms to explain/predict events) + DCI ETS1.A (Define and delimit engineering problems) + CCC7 (Stability and change)

A school district implements an algorithm to identify students at risk of academic failure and allocate tutoring resources. After one year, an audit reveals that the algorithm disproportionately flags students from low-income neighborhoods, partially because it uses school attendance as a key predictor, and students in underfunded schools with fewer support services have higher absence rates. Meanwhile, struggling students in better-resourced schools are under-identified because their attendance is higher despite similar academic challenges.

The model shows that an algorithm deployed in healthcare allocates fewer resources to Black patients despite them having more severe health conditions. Investigation reveals the algorithm uses healthcare spending history as a proxy for health needs. Why does this produce racially biased outcomes?

A. The algorithm correctly identifies that lower spending indicates better health
B. Black patients have fewer health needs on average
C. Historical barriers to healthcare access (insurance gaps, provider discrimination, geographic access) mean Black patients spent less on healthcare not because they were healthier, but because they faced systemic barriers to care
D. Healthcare algorithms cannot produce biased outcomes because health data is objective

Correct Answer: C

Feedback: The algorithm conflated spending with health need, but spending reflects ACCESS to care, not need for care. Systemic barriers (insurance inequities, provider bias, geographic access) suppressed healthcare spending for Black patients, causing the algorithm to underestimate their health needs. If you chose B, this response does not account for the key mechanism or relationship the evidence demonstrates. Consider why spending might not equal need. If a person faces barriers to accessing healthcare (no insurance, no nearby providers, provider discrimination), they will spend less. Lower spending does not mean better health; it can mean less access to care. If you chose A, this answer does not account for the key mechanism or relationship the evidence demonstrates. Consider why spending might not equal need. If a person faces barriers to accessing healthcare (no insurance, no nearby providers, provider discrimination), they will spend less. Lower spending does not mean better health; it can mean less access to care. If you chose D, this choice dismisses relevant factors that the evidence directly addresses. Consider why spending might not equal need. If a person faces barriers to accessing healthcare (no insurance, no nearby providers, provider discrimination), they will spend less. Lower spending does not mean better health; it can mean less access to care.
---

### Question 5

CAST Alignment: SEP 2.1.4 (Represent mechanisms to predict a scientific event) + DCI ETS1.B (Use computer simulations to model solutions) + CCC4 (Describe system components and interactions)

A city council debates whether to continue using an algorithmic risk assessment tool in criminal sentencing. Supporters present data showing the algorithm predicts recidivism with 72% accuracy overall. Critics present a systems analysis showing that the algorithm's accuracy is 78% for white defendants but only 64% for Black defendants, and that false-positive rates (predicting re-offense when none occurs) are 2.1 times higher for Black defendants. The computational model reveals that these disparities stem from training data that reflects decades of inequitable policing and sentencing practices.

Based on the complete model analysis, which recommendation is best supported by the evidence for deploying algorithms in high-stakes decisions?

A. Algorithms should replace human decision-making entirely because they are more consistent
B. Algorithms should only be trained on data from the last 5 years to avoid historical bias
C. Algorithms should never be used in high-stakes decisions because bias cannot be eliminated
D. Algorithms should be deployed with mandatory bias auditing, transparent feature disclosure, defined fairness metrics, and ongoing monitoring, because bias can be measured and mitigated even if it cannot be perfectly eliminated

Correct Answer: D

Feedback: The model demonstrates that bias is measurable and reducible through deliberate interventions: balanced training data, proxy variable analysis, fairness constraints, and disparate impact auditing. Perfect fairness may be mathematically impossible, but accountability and transparency can ensure continuous improvement. If you chose A, this response does not account for the key mechanism or relationship the evidence demonstrates. The model showed that bias is a quantifiable, measurable phenomenon in algorithms. This means it can be detected, measured, and reduced through systematic interventions. Consider whether the evidence supports complete rejection, unconditional acceptance, or an approach that requires accountability. If you chose C, this answer dismisses relevant factors that the evidence directly addresses. The model showed that bias is a quantifiable, measurable phenomenon in algorithms. This means it can be detected, measured, and reduced through systematic interventions. Consider whether the evidence supports complete rejection, unconditional acceptance, or an approach that requires accountability. If you chose B, this choice oversimplifies a multi-factor system by focusing on a single variable. The model showed that bias is a quantifiable, measurable phenomenon in algorithms. This means it can be detected, measured, and reduced through systematic interventions. Consider whether the evidence supports complete rejection, unconditional acceptance, or an approach that requires accountability.
---

### Answer Key

Question 1: B (Cognitive Level: Identify -- SEP 2.1.1, DCI HS-ETS1-1, CCC4)
Question 2: B (Cognitive Level: Reason -- SEP 2.1.2, DCI HS-ETS1-1, CCC2)
Question 3: A (Cognitive Level: Reason -- SEP 2.1.2, DCI HS-ETS1-1, CCC4)
Question 4: C (Cognitive Level: Reason + Evidence -- SEP 2.1.4, DCI HS-ETS1-4, CCC7)
Question 5: D (Cognitive Level: Predict + Apply -- SEP 2.1.4, DCI HS-ETS1-4, CCC4)

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-11/G11L1-L06/G11L1-L06-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-11/G11L1-L06/G11L1-L06-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-11/G11L1-L06/G11L1-L06-Student-Presentation.pptx] |
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