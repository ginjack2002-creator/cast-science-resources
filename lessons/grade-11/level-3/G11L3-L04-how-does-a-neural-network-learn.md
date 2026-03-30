# Lesson: How Does a Neural Network Learn?

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G11L3-L04 |
| **Grade** | 11th Grade — Level 3: Systems Innovation Lab |
| **Lesson Name** | How Does a Neural Network Learn? |
| **Status** | Template |

---

## Platform

### Title
**How Does a Neural Network Learn? — Modeling Artificial Intelligence Training, Weights, and Pattern Recognition**

### Overview
In 2012, a neural network called AlexNet won an image recognition competition by a margin so large it shocked the field. In 2016, AlphaGo defeated the world champion at Go — a game many thought would resist AI for decades. In 2022, ChatGPT demonstrated conversational abilities that seemed indistinguishable from human writing. In 2024, AI systems can generate photorealistic images, write code, compose music, and pass medical licensing exams. All of this emerged from the same fundamental mechanism: adjusting connection weights in neural networks through exposure to massive amounts of data. Students investigate the driving question: How does a machine made of simple math operations learn to see faces, understand language, and create art — and what does it actually understand? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of a futuristic visualization of a neural network with glowing interconnected nodes and flowing data streams in blue and purple light, overlaid with subtle code elements, featuring a diverse multicultural group with Black people centered of 16-17 year old students interacting with the AI visualization on large holographic displays]

### Grade
11th Grade — Level 3: Systems Innovation Lab

### NGSS Standard
**HS-ETS1-1, HS-ETS1-4**: Analyze a major global challenge to specify qualitative and quantitative criteria and constraints for solutions that account for societal needs and wants. Use a computer simulation to model the impact of proposed solutions to a complex real-world problem with numerous criteria and constraints on interactions within and between systems relevant to the problem.

### Learning Objectives
- Model how neural network training adjusts connection weights through backpropagation to minimize prediction error
- Analyze the relationship between training data quality, network architecture, and the emergence of pattern recognition capabilities
- Evaluate the trade-offs between model complexity, training cost, and the risk of overfitting versus genuine understanding
- Predict how changes in training parameters affect whether a neural network learns generalizable patterns or memorizes specific examples

### Component List (Starting Model: 7 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Training Data Volume | External | The total number of labeled examples available for the network to learn from — more data generally improves generalization but with diminishing returns and increasing computational cost |
| Training Data Quality | External | The accuracy, diversity, and representativeness of the training examples — biased or unrepresentative data produces a model that works well for some populations but fails or discriminates against others |
| Network Depth | External | The number of hidden layers in the neural network — deeper networks can learn more complex and abstract patterns but are harder to train, require more data, and are more prone to overfitting |
| Learning Rate | External | The size of the weight adjustment step during each training iteration — too high and the network overshoots optimal weights, too low and training takes prohibitively long or gets stuck in suboptimal solutions |
| Prediction Accuracy | Internal | The percentage of correct outputs on data the network has not seen during training — the ultimate measure of whether the network learned generalizable patterns versus memorizing training examples |
| Overfitting Risk | Internal | The degree to which the network has memorized training data rather than learning underlying patterns — measured by the gap between training accuracy and validation accuracy |
| Computational Cost | Internal | The total energy, hardware time, and financial resources required to train the model — GPT-4 training estimated at $100+ million in compute costs and massive electricity consumption |

### Research for Lesson
- How Neural Networks Work — reference materials and textbook resources
- Backpropagation and Learning — reference materials and textbook resources
- The Bias Amplification Problem — reference materials and textbook resources
- The Scale Paradigm and Its Limits — reference materials and textbook resources

---

## Step 1: LOCATE — Build Your System

### Text Editor

```
HOW DOES A NEURAL NETWORK LEARN?

Modeling Artificial Intelligence Training, Weights, and Pattern Recognition.
How does a machine made of simple math operations learn to see faces, understand language, and create art — and what does it actually understand?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task A: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Training Data Volume" — the total number of labeled examples available for the network to learn from — more data generally improves generalization but with diminishing returns and increasing computational cost
  ○ Click "Training Data Quality" — the accuracy
  ○ Click "Network Depth" — the number of hidden layers in the neural network — deeper networks can learn more complex and abstract patterns but are harder to train
  ○ Click "Learning Rate" — the size of the weight adjustment step during each training iteration — too high and the network overshoots optimal weights
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Prediction Accuracy" — the percentage of correct outputs on data the network has not seen during training — the ultimate measure of whether the network learned generalizable patterns versus memorizing training examples
  ○ Click "Overfitting Risk" — the degree to which the network has memorized training data rather than learning underlying patterns — measured by the gap between training accuracy and validation accuracy
  ○ Click "Computational Cost" — the total energy

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
"How does a machine made of simple math operations learn to see faces, understand language, and create art — and what does it actually understand?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Training Data Volume' — that's external. The total number of labeled examples available for the network to learn from — more data generally improves generalization but with diminishing returns and increasing computational cost.
Click on 'Training Data Quality' — that's external. The accuracy.
Click on 'Network Depth' — that's external. The number of hidden layers in the neural network — deeper networks can learn more complex and abstract patterns but are harder to train.
Click on 'Learning Rate' — that's external. The size of the weight adjustment step during each training iteration — too high and the network overshoots optimal weights.
Click on 'Prediction Accuracy' — that's internal. The percentage of correct outputs on data the network has not seen during training — the ultimate measure of whether the network learned generalizable patterns versus memorizing training examples.
Click on 'Overfitting Risk' — that's internal. The degree to which the network has memorized training data rather than learning underlying patterns — measured by the gap between training accuracy and validation accuracy.
Click on 'Computational Cost' — that's internal. The total energy.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Training Data Volume, Training Data Quality, Network Depth, and Learning Rate are external components because they represent engineering choices that researchers directly control before and during training. Data scientists select how much data to collect, curate its quality, choose the network architecture depth, and set the learning rate hyperparameter. Prediction Accuracy, Overfitting Risk, and Computational Cost are internal because they are emergent properties of the training process — outcomes determined by the interaction of the external variables with the data and the mathematical optimization process.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next step, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 7 components sorted: Training Data Volume, Training Data Quality, Network Depth, Learning Rate (External), Prediction Accuracy, Overfitting Risk, Computational Cost (Internal)]

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
• Click on "Training Data Quality" and drag an arrow to "Prediction Accuracy"
• Click on "Network Depth" and drag an arrow to "Overfitting Risk"
• Click on "Training Data Volume" and drag an arrow to "Computational Cost"
• Click on "Training Data Quality" and drag an arrow to "Overfitting Risk"

Task C: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Training Data Quality → Prediction Accuracy = POSITIVE (+)
    Higher quality training data — more accurate labels, more diverse representation, fewer systematic biases — directly produces a model that makes more accurate predictions across all populations because it has learned genuine patterns rather than artifacts of poor data curation.

  ○ Network Depth → Overfitting Risk = POSITIVE (+)
    Deeper networks with more layers and parameters have more capacity to memorize specific training examples rather than learning generalizable patterns. Without sufficient regularization and data, increased depth increases the gap between training accuracy and real-world performance.

  ○ Training Data Volume → Computational Cost = POSITIVE (+)
    More training data requires proportionally more computation to process — each training epoch must iterate through every example, and larger datasets require more storage, memory, and GPU hours, increasing total training cost.

  ○ Training Data Quality → Overfitting Risk = NEGATIVE (−)
    Higher quality, more diverse training data reduces overfitting risk because the model encounters more varied examples that force it to learn general patterns rather than memorizing specific quirks of a narrow, unrepresentative dataset.

Task D: CHECK YOUR MODEL
• You should have 4 arrows total
• 1 negative relationship(s), 3 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: A deeper network with more training data generally performs better — but it also costs exponentially more to train and risks memorizing data rather than understanding patterns. GPT-4 required months of training on thousands of GPUs consuming megawatts of power. Is there a fundamental limit to the 'scale everything up' approach, and what happens when we hit it?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Training Data Quality' and drag an arrow
over to 'Prediction Accuracy.'

Here's the key question: When training data quality goes UP, does
prediction accuracy go UP or DOWN?

Higher quality training data — more accurate labels, more diverse representation, fewer systematic biases — directly produces a model that makes more accurate predictions across all populations because it has learned genuine patterns rather than artifacts of poor data curation.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Network Depth' and drag an arrow
over to 'Overfitting Risk.'

Here's the key question: When network depth goes UP, does
overfitting risk go UP or DOWN?

Deeper networks with more layers and parameters have more capacity to memorize specific training examples rather than learning generalizable patterns. Without sufficient regularization and data, increased depth increases the gap between training accuracy and real-world performance.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'Training Data Volume' and drag an arrow
over to 'Computational Cost.'

Here's the key question: When training data volume goes UP, does
computational cost go UP or DOWN?

More training data requires proportionally more computation to process — each training epoch must iterate through every example, and larger datasets require more storage, memory, and GPU hours, increasing total training cost.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Final connection: Click on 'Training Data Quality' and drag an arrow
over to 'Overfitting Risk.'

Here's the key question: When training data quality goes UP, does
overfitting risk go UP or DOWN?

Higher quality, more diverse training data reduces overfitting risk because the model encounters more varied examples that force it to learn general patterns rather than memorizing specific quirks of a narrow, unrepresentative dataset.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Look at your model now. You've got 1 negative and 3
positive relationships. 4 arrows total.

A deeper network with more training data generally performs better — but it also costs exponentially more to train and risks memorizing data rather than understanding patterns. GPT-4 required months of training on thousands of GPUs consuming megawatts of power. Is there a fundamental limit to the 'scale everything up' approach, and what happens when we hit it?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Training Data Quality +→ Prediction Accuracy, Network Depth +→ Overfitting Risk, Training Data Volume +→ Computational Cost, Training Data Quality −→ Overfitting Risk]

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
• When Training Data Volume is HIGH, what happens to the internal components?

Task C: SCENARIO — BALANCED TRAINING
• Moderate data volume, high quality, moderate depth, optimal learning rate
• PREDICT FIRST: What do you predict the relationship between prediction accuracy and computational cost looks like with a well-balanced training configuration?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task D: SCENARIO — SCALE-UP EXPERIMENT
• Maximum data volume and network depth
• PREDICT FIRST: What do you predict happens to both accuracy and computational cost when you scale everything to maximum?
• Resume the simulation and observe what happens
• Was your prediction correct?

Task E: SCENARIO — BIASED DATA SCENARIO
• Optimal architecture but low-quality, unrepresentative training data
• PREDICT FIRST: What do you predict happens to prediction accuracy for underrepresented groups when the training data does not represent them?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Neural networks do not understand anything in the human sense — they are sophisticated pattern matching systems that find statistical correlations in training data, and their apparent intelligence emerges from the scale and structure of these correlations
• Training data quality is the most critical variable for real-world impact — a brilliantly designed network trained on biased data will produce biased outputs that can reinforce and amplify societal discrimination at scale
• Scaling up (more data, more parameters, more compute) has produced remarkable capability gains, but with exponentially diminishing returns and exponentially increasing costs — each new generation of AI models costs roughly 10 times more to train
• The gap between training accuracy and real-world performance (overfitting) reveals a fundamental limitation — networks can appear to understand while merely having memorized patterns that fail in novel situations

THE ANSWER: A neural network learns by adjusting millions or billions of connection weights through repeated exposure to training data. During each training step, the network makes a prediction, the loss function measures how wrong it was, and backpropagation calculates which weights to adjust and by how much. After millions of iterations, the weights encode patterns extracted from the data. But the network does not understand what it has learned — it has found statistical correlations, not causal understanding. It can produce text that sounds insightful without comprehending a single word. Its capabilities are bounded by its training data: if the data is biased, the model is biased. If the data omits important patterns, the model will fail in those areas. The AI revolution is built on math, data, and enormous computation — not understanding.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Balanced Training. Moderate data volume, high quality, moderate depth, optimal learning rate.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Scale-Up Experiment.
Maximum data volume and network depth.

Before you run it — make a prediction. What do you predict happens to both accuracy and computational cost when you scale everything to maximum?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Biased Data Scenario. Optimal architecture but low-quality, unrepresentative training data.
What do you predict happens to prediction accuracy for underrepresented groups when the training data does not represent them?

Here's what our model reveals: A neural network learns by adjusting millions or billions of connection weights through repeated exposure to training data. During each training step, the network makes a prediction, the loss function measures how wrong it was, and backpropagation calculates which weights to adjust and by how much. After millions of iterations, the weights encode patterns extracted from the data. But the network does not understand what it has learned — it has found statistical correlations, not causal understanding. It can produce text that sounds insightful without comprehending a single word. Its capabilities are bounded by its training data: if the data is biased, the model is biased. If the data omits important patterns, the model will fail in those areas. The AI revolution is built on math, data, and enormous computation — not understanding.

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
   • What happens if you turn OFF Training Data Volume?
   • What happens if you turn OFF Training Data Quality?
   • What happens if you turn OFF Network Depth?
   • What happens if you turn OFF Learning Rate?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Regularization Strength — Techniques like dropout or weight decay that deliberately constrain the network's ability to memorize training data — forcing it to learn generalizable patterns at the cost of slightly lower training accuracy
   • Inference Latency — The time required for a trained model to process a single input and produce an output — critical for real-time applications like autonomous vehicles or medical alerts where milliseconds matter
   • Catastrophic Forgetting — The tendency of neural networks to lose previously learned capabilities when trained on new data — a fundamental challenge for creating AI systems that continuously learn and improve over time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • How Neural Networks Work — how does this connect to your model?
   • Backpropagation and Learning — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model demonstrate why training data quality is arguably more important than network architecture for real-world AI applications?
   • What does the overfitting phenomenon reveal about the difference between memorization and understanding in neural networks?
   • Why does the biased data scenario have disproportionate real-world impact compared to other sources of prediction error?
   • How would your model change if training data were unlimited and perfectly representative — would that solve the understanding problem?

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

Regularization Strength. Techniques like dropout or weight decay that deliberately constrain the network's ability to memorize training data — forcing it to learn generalizable patterns at the cost of slightly lower training accuracy
How would you model that?

Inference Latency. The time required for a trained model to process a single input and produce an output — critical for real-time applications like autonomous vehicles or medical alerts where milliseconds matter
How would you model that?

Catastrophic Forgetting. The tendency of neural networks to lose previously learned capabilities when trained on new data — a fundamental challenge for creating AI systems that continuously learn and improve over time
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

Machine Learning Engineers design and train neural networks at companies like Google DeepMind, OpenAI, Anthropic, Meta AI, and Microsoft Research, earning $130,000-$300,000/year. AI Ethics Researchers investigate bias, fairness, and safety in AI systems at universities, nonprofits, and technology companies, earning $90,000-$180,000/year. Data Scientists who prepare and curate training datasets are critical to AI quality, earning $100,000-$170,000/year.

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
Visual: Title slide with dramatic neural network visualization
Say: "An AI system can now pass the bar exam, diagnose diseases from X-rays, write poetry, and generate photorealistic faces of people who do not exist. All of this comes from the same mechanism: adjusting numbers in a massive web of connections. Today you find out how — and what is really happening under the hood."
Do: Open with demonstrations: show an AI-generated image, an AI-written poem, and an AI medical diagnosis. Ask: how did a machine learn to do all of this? What does it actually understand?
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and vocabulary terms displayed
Say: "Today you are modeling the engine behind the AI revolution — and discovering that what looks like intelligence is actually sophisticated pattern matching on an enormous scale."
Do: Have students read objectives. Pre-teach 'backpropagation' as the learning algorithm and 'overfitting' as the enemy of real learning. Use the test-memorizer analogy.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: How does a machine made of math operations learn to see, speak, and create?
Say: "The answer might surprise you: it does not understand any of it. It finds statistical patterns in data. The question is whether pattern matching at extreme scale starts to look like understanding — and whether the difference matters."
Do: Quick-write: Students write what they think 'understanding' means and whether a machine can truly understand. Share out. This philosophical question becomes concrete through the model.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps with neural network training context
Say: "We are modeling a system where the quality of what goes IN determines the quality and fairness of what comes OUT — and where bigger is not always better."
Do: Preview LEVER steps. Emphasize that this model directly connects to AI systems students use every day — social media algorithms, recommendation systems, ChatGPT.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Seven component cards for neural network training model
Say: "Seven components. Four inputs you can control: data volume, data quality, network depth, and learning rate. Three outputs that emerge from training: accuracy, overfitting, and cost. Watch what happens when you change the inputs."
Do: Guide through all seven components. Discuss why data volume, quality, depth, and learning rate are external — engineers choose these. Accuracy, overfitting, and cost are consequences.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows showing data quality as the foundational variable
Say: "Data quality is the keystone. You can build the most brilliant architecture and train for months on the most powerful hardware — but if the data is biased, the AI will be biased. Garbage in, garbage out, at billion-dollar scale."
Do: Help students map relationships. Highlight the asymmetry: poor data quality undermines everything, but good data quality does not guarantee good outcomes without adequate architecture.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Simulation results showing accuracy, fairness, and cost across three scenarios
Say: "Let us test: can you find settings where the AI is both accurate AND fair? What happens when you scale everything up? And what happens when the data is biased?"
Do: Students predict outcomes before each scenario. The biased data scenario is the critical learning moment — watch accuracy diverge between population groups even with a well-designed network.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key findings about AI learning, bias, and scaling
Say: "The biggest insight: AI does not learn truth from data. It learns patterns from data. If the data contains injustice, the AI learns injustice and calls it optimization."
Do: Lead discussion connecting model findings to real AI controversies: facial recognition accuracy disparities by race, hiring algorithms that discriminated, healthcare AI that underserved Black patients.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Fair AI system design challenge for medical application
Say: "A hospital wants to deploy AI to save lives — but the AI works better for some patients than others. Your job: fix it before anyone gets hurt."
Do: Groups design fair AI training protocols for the healthcare scenario. Must specify data collection changes, architecture decisions, fairness metrics, and monitoring plans. Present with model evidence.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: How Does a Neural Network Learn?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
In 2012, a neural network called AlexNet won an image recognition competition by a margin so large it shocked the field. In 2016, AlphaGo defeated the world champion at Go — a game many thought would resist AI for decades. In 2022, ChatGPT demonstrated conversational abilities that seemed indistinguishable from human writing. In 2024, AI systems can generate photorealistic images, write code, compose music, and pass medical licensing exams. All of this emerged from the same fundamental mechanism: adjusting connection weights in neural networks through exposure to massive amounts of data.

NGSS ALIGNMENT:
HS-ETS1-1, HS-ETS1-4: Analyze a major global challenge to specify qualitative and quantitative criteria and constraints for solutions that account for societal needs and wants. Use a computer simulation to model the impact of proposed solutions to a complex real-world problem with numerous criteria and constraints on interactions within and between systems relevant to the problem.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Using Mathematics and Computational Thinking
  Students use computational models to analyze how mathematical optimization through backpropagation creates emergent pattern recognition capabilities from simple weighted connections.
• Disciplinary Core Idea: ETS1.A Defining and Delimiting Engineering Problems / ETS1.B Developing Possible Solutions
  Students define the engineering problem of creating AI systems that are both accurate and fair, then develop solutions addressing training data, architecture, and evaluation criteria.
• Crosscutting Concept: Systems and System Models
  Students model the AI training pipeline as a system where inputs (data, architecture, hyperparameters) flow through a complex optimization process to produce outputs (predictions, biases, capabilities) with emergent behaviors not predictable from individual components.

PACING GUIDE:
• Step 1 (Locate): 8-10 minutes
• Step 2 (Establish): 8-10 minutes
• Step 3 (Visualize & Evaluate): 10-12 minutes
• Step 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Neural Network, Backpropagation, Training Data, Overfitting, Loss Function
□ Prepare How does a machine made of simple math operations learn to see faces, understand language, and create art — and what does it actually understand discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify seven key components of a neural network training system: training data volume, training data quality, network depth, learning rate, prediction accuracy, overfitting risk, and computational cost.
• Establish: Students map the relationships showing that training data quality is the foundational variable affecting all outcomes, that scaling (data volume and network depth) provides diminishing returns at exponentially increasing cost, and that the gap between training and validation accuracy reveals overfitting.
• Visualize: Students build a computational model showing the seven-component AI training system with competing pressures between accuracy, fairness, cost, and generalization.
• Evaluate: Students run balanced training, scale-up, and biased data scenarios to discover how each parameter affects the system and identify the conditions under which AI systems become both accurate and fair.
• Revise: Students add regularization strength, inference latency, or catastrophic forgetting to model more realistic AI system dynamics and limitations.

BACKGROUND CONTENT:
• How Neural Networks Work:
  A neural network is a series of layers, each containing nodes (artificial neurons) connected to nodes in the next layer. Each connection has a weight — a number that determines how strongly one node influences the next. An input (like an image's pixel values) enters the first layer, gets multiplied by weights, passed through activation functions that add non-linearity, and propagated through successive layers until the final layer produces an output (like 'cat' or 'dog'). Initially, all weights are random and the network's predictions are meaningless. Training is the process of systematically adjusting these weights so that correct predictions are amplified and incorrect ones are suppressed.

• Backpropagation and Learning:
  Backpropagation is the algorithm that makes neural network training possible. After each prediction, the loss function calculates the error — how far the prediction was from the correct answer. Backpropagation then traces this error backward through the network, computing how much each individual weight contributed to the mistake. Weights that pushed toward the wrong answer are decreased; weights that pushed toward the right answer are increased. The learning rate controls how large each adjustment is. Over millions of training iterations across thousands or millions of examples, the weights gradually encode the statistical patterns in the data.

• The Bias Amplification Problem:
  Neural networks learn whatever patterns exist in their training data — including patterns of discrimination. If historical healthcare data shows that Black patients received less aggressive treatment for the same symptoms (which is documented fact), an AI trained on this data will learn to recommend less aggressive treatment for Black patients, not because the AI is racist but because it faithfully reproduces the patterns in its training data. Worse, AI systems can amplify biases: a hiring AI trained on a company's historical hiring data (which skewed male) actively filtered out female candidates. The data encodes the past; the AI projects that past into the future.

• The Scale Paradigm and Its Limits:
  The dominant paradigm in modern AI is scaling: larger models trained on more data with more compute produce better results. GPT-3 had 175 billion parameters trained on 300 billion tokens. GPT-4 is estimated at over 1 trillion parameters. Each generation costs roughly 10 times more to train — GPT-4's training likely exceeded $100 million in compute costs alone. Scaling has produced remarkable capabilities, but returns are diminishing logarithmically while costs increase exponentially. A model 10 times larger may only be 10-20% better on benchmarks. This suggests that scaling alone will not achieve artificial general intelligence — something qualitatively different may be required.

COMMON MISCONCEPTIONS:
• "AI systems are objective because they are based on math, not human judgment"
  Reality: Neural networks are trained on data created by humans in a society with systemic biases. The math is objective; the data is not. When historical data reflects discrimination — less aggressive medical treatment for Black patients, fewer women hired into tech roles, heavier policing in communities of color — the AI learns these patterns and reproduces them as optimal predictions. The AI does not know it is being unfair; it is optimizing the objective function it was given using the data it was trained on. The bias is not in the algorithm — it is in the data, which reflects the world.
  Strategy: Exercise: Show students two identical patient profiles except for race. Run them through the model and observe any prediction differences. Trace the difference back to training data patterns. The AI is doing math correctly — the question is whether the data represents reality or injustice.

• "Bigger AI models are always better"
  Reality: The scaling paradigm has produced impressive results, but the relationship between scale and capability is logarithmic, not linear. Doubling the parameter count of a model from 500 billion to 1 trillion might improve accuracy by 2-5%, while increasing training cost from $50 million to $100+ million. The model shows diminishing returns clearly: the accuracy curve flattens while the cost curve steepens. Furthermore, larger models trained on more data simply amplify whatever patterns are in that data — including biases — at greater scale and with more confidence.
  Strategy: Graph: Plot accuracy versus cost from the model for networks of increasing depth. Students will see the classic diminishing returns curve — each doubling of compute produces less and less improvement. Ask: is this sustainable?

• "Neural networks think and understand like human brains"
  Reality: Despite the name 'neural network,' the connection to biological brains is superficial. Biological neurons use electrochemical signaling, have complex internal dynamics, form and dissolve connections based on experience, and operate in a biochemical soup that influences processing. Artificial neurons multiply inputs by weights and apply simple mathematical functions. Artificial neural networks have no goals, no experiences, no consciousness, and no understanding of what their outputs mean. They are extraordinarily powerful pattern-matching machines, but equating their processing with human cognition is a category error.
  Strategy: Thought experiment: A calculator can do arithmetic faster than any human. Does it understand what numbers mean? A language model can generate grammatically perfect text. Does it understand what words mean? The speed and accuracy of processing tells us nothing about understanding.

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
Big Question: How does a machine made of simple math operations learn to see faces, understand language, and create art — and what does it actually understand?
Answer: A neural network learns by adjusting millions or billions of connection weights through repeated exposure to training data. During each training step, the network makes a prediction, the loss function measures how wrong it was, and backpropagation calculates which weights to adjust and by how much. After millions of iterations, the weights encode patterns extracted from the data. But the network does not understand what it has learned — it has found statistical correlations, not causal understanding. It can produce text that sounds insightful without comprehending a single word. Its capabilities are bounded by its training data: if the data is biased, the model is biased. If the data omits important patterns, the model will fail in those areas. The AI revolution is built on math, data, and enormous computation — not understanding.

Simulation Answers:
• Balanced Training Scenario: With moderate data volume, high quality, moderate depth, and optimal learning rate, the model achieves strong prediction accuracy with low overfitting risk and manageable computational cost. The gap between training accuracy and validation accuracy is small, indicating genuine pattern learning rather than memorization. Prediction accuracy is consistent across different demographic groups because the high-quality data adequately represents all populations. This scenario demonstrates that a well-balanced approach often outperforms brute-force scaling.
• Biased Data Scenario: When training data quality is reduced — specifically, when certain demographic groups are underrepresented or historical biases are present in labels — the model shows high overall accuracy that masks significant disparities. Prediction accuracy for well-represented groups may reach 97% while accuracy for underrepresented groups drops to 80% or below. The model has not failed — it has faithfully learned the patterns in its data, and those patterns include systematic bias. This scenario demonstrates that AI fairness is fundamentally a data problem that cannot be solved by better algorithms alone.

Reflection Exemplars:
• Q: Why is training data quality more important than network architecture?
  A: The model demonstrates that even the most sophisticated network architecture cannot overcome fundamentally biased or unrepresentative training data. A simple network trained on excellent data outperforms a complex network trained on poor data because the network can only learn patterns that exist in its training examples. If certain populations, conditions, or edge cases are absent from the training data, no amount of mathematical optimization will enable the network to handle them correctly. This is why data curation is often the most important and most expensive part of AI development — the model clearly shows that quality data is the foundation everything else depends on.
• Q: Does a neural network actually understand anything?
  A: The model shows that neural networks find statistical correlations in data — they identify which patterns of pixels correlate with labels like 'cat' or 'dog,' and which patterns of words correlate with coherent text. This is pattern matching at extraordinary scale, not comprehension. A language model can generate a perfect explanation of quantum physics without having any concept of what atoms, energy, or measurement mean. The model reveals this through overfitting: a network that has memorized training data perfectly can score 100% on seen examples while failing catastrophically on slight variations — exactly what a student who memorized answers without understanding would do. Whether sufficiently complex pattern matching constitutes understanding is a philosophical question the model cannot answer.

STEM CHALLENGE GUIDANCE:
Title: Design a Fair AI System for a Real-World Application
Mission: Design a neural network-based system for a real-world application (medical diagnosis, college admissions, criminal justice, or hiring) that maximizes accuracy while ensuring fairness across all demographic groups.
Scenario: A hospital network wants to deploy an AI system that predicts which emergency room patients are most likely to have a heart attack within 24 hours, allowing faster treatment. However, early testing reveals that the system is significantly less accurate for Black patients because the training data underrepresents this population and uses historical treatment data that reflects existing healthcare disparities. Your team must redesign the training approach to ensure the system works equally well for all patients.
Introduction: Present the challenge: A hospital wants to deploy an AI system that predicts heart attack risk from emergency room data. Early testing reveals the system is significantly less accurate for Black patients because the training data reflects historical healthcare disparities. Your team must redesign the training approach — not just the model architecture — to ensure the system works equally well for all patients. Use evidence from your model to justify every design decision.

Key Concepts:
• Fairness Metrics: Multiple mathematical definitions of fairness exist, and they often conflict: demographic parity (equal prediction rates across groups), equalized odds (equal accuracy across groups), and calibration (predictions mean the same thing across groups) cannot all be satisfied simultaneously. Choosing which fairness metric to prioritize is an ethical decision, not a technical one.
• Data Augmentation and Resampling: When training data underrepresents certain populations, techniques like oversampling minorities, generating synthetic examples, or strategically weighting training examples can partially compensate. However, these techniques cannot create information that was never collected — they can only adjust the emphasis on existing patterns.
• Algorithmic Auditing: Before deploying AI in high-stakes domains, systems should be audited by independent evaluators who test performance across demographic groups, check for known bias patterns, and verify that the system meets predetermined fairness thresholds. This is analogous to drug safety testing before medical deployment.

Evaluation Rubric:
• Expert (4): Design includes specific data collection and curation changes, architecture decisions with regularization rationale, explicit fairness metrics with thresholds, demographic-disaggregated testing protocol, ongoing monitoring plan, and references model evidence for every decision
• Proficient (3): Design addresses data quality, includes fairness metrics, and uses model evidence to justify the approach
• Developing (2): Design identifies the bias problem but lacks specific solutions or does not connect to model evidence
• Beginning (1): Design is incomplete, does not address fairness, or ignores the role of training data quality

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a visual flowchart showing how biased data flows through network training to produce biased predictions, with intervention points marked where engineers can address bias
  • Use a simplified confusion matrix template disaggregated by demographic group so students can see where accuracy differs across populations
  • Sentence frames: 'Our model shows that when Training Data Quality drops for __ population, Prediction Accuracy for that group drops to __%, which means patients from that group would be __ times more likely to receive an incorrect prediction'

Extensions (Advanced Learners):
  • Research the COMPAS recidivism prediction system controversy and analyze how training on historical criminal justice data — which reflects systemic racism — produced an AI that discriminated against Black defendants
  • Investigate the energy consumption of training large language models and calculate the carbon footprint of GPT-4 training — debate whether the environmental cost is justified by the capabilities gained
  • Design an 'AI bill of rights' for your school that specifies when AI can and cannot be used for student-facing decisions like grading, discipline, and course recommendations

Cross-Curricular Connections:
  • Math: A neural network with 2 inputs, one hidden layer of 3 nodes, and 1 output has how many trainable weights? Extend this: how many weights in a network with 1000 inputs, 5 hidden layers of 500 nodes each, and 10 outputs? Why does parameter count grow so quickly with depth?
  • ELA: Write a investigative journalism piece examining a real case where AI bias caused harm — ProPublica's investigation of COMPAS, Amazon's gender-biased hiring tool, or dermatology AI that fails on dark skin. Your article must explain the technical mechanism of how bias entered the system.
  • Sociology/Ethics: Analyze the concept of 'algorithmic justice' — when an AI system produces racially disparate outcomes, who is responsible: the engineers who built it, the company that deployed it, the data that trained it, or the society that produced the biased data? Construct an argument for accountability.

CAST ALIGNMENT:
• Model how training data volume, quality, and network architecture interact to determine neural network prediction accuracy and generalization ability
• Analyze the relationship between scaling (more data, deeper networks, more compute) and the diminishing returns in accuracy improvement versus exponentially increasing cost
• Evaluate how training data bias propagates through network weights to produce systematically unfair predictions for underrepresented populations

CAST-Style Assessment Questions:
• Multiple Choice: A neural network trained on 10 million medical images achieves 97% accuracy on the test set overall, but only 82% accuracy for images from patients with dark skin tones. Which model variable most likely explains this disparity?
• Constructed Response: Using evidence from your model, explain why scaling up a neural network (more parameters, more training data, more compute) does not automatically solve the bias problem. Describe the specific mechanism by which biased training data produces biased predictions regardless of network size.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: How Does a Neural Network Learn?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. What do you think happens inside an artificial intelligence system when it recognizes a face or generates text?

   _________________________________________________________

   _________________________________________________________

2. How do you think AI systems like ChatGPT or image generators actually learn — what goes in and what comes out?

   _________________________________________________________

   _________________________________________________________

3. Draw a diagram showing how you think a computer could be trained to distinguish between photos of cats and dogs.

   [DRAWING BOX]

4. What concerns do you have about AI systems making important decisions about people's lives, like medical diagnosis or hiring?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Neural Network                
___ Backpropagation               
___ Training Data                 
___ Overfitting                   
___ Loss Function                 

A. A computational system inspired by biological brains, consisting of layers of interconnected nodes (artificial neurons) that transform inputs through weighted connections and activation functions — each layer extracts progressively more abstract features from data
B. The algorithm that trains neural networks by calculating how much each connection weight contributed to the prediction error, then adjusting weights in the direction that reduces error — this process repeats millions of times across the training data, gradually improving performance
C. The collection of labeled examples used to teach a neural network — the model never sees the real world directly, it only learns patterns from whatever data humans provide, which means biases in the data become biases in the model
D. When a neural network memorizes the specific training examples rather than learning generalizable patterns — an overfit model performs perfectly on training data but fails on new data it has not seen before, like a student who memorizes test answers without understanding concepts
E. The mathematical measure of how wrong the network's predictions are compared to the correct answers — training is the process of minimizing this function, and the choice of loss function determines what the network optimizes for

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

SCENARIO: Balanced Training
Settings: Moderate data volume, high quality, moderate depth, optimal learning rate
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Scale-Up Experiment
Settings: Maximum data volume and network depth
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Biased Data Scenario
Settings: Optimal architecture but low-quality, unrepresentative training data
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

1. How does your model demonstrate why training data quality is arguably more important than network architecture for real-world AI applications?

   _________________________________________________________

   _________________________________________________________

2. What does the overfitting phenomenon reveal about the difference between memorization and understanding in neural networks?

   _________________________________________________________

   _________________________________________________________

3. Why does the biased data scenario have disproportionate real-world impact compared to other sources of prediction error?

   _________________________________________________________

   _________________________________________________________

4. How would your model change if training data were unlimited and perfectly representative — would that solve the understanding problem?

   _________________________________________________________

   _________________________________________________________

5. What are the limitations of modeling AI training when real-world neural networks have billions of parameters interacting in ways we cannot fully trace?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. How does a machine made of simple math operations learn to see faces, understand language, and create art — and what does it actually understand? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Using Mathematics and Computational Thinking
   □ Disciplinary Core Idea: ETS1.A Defining and Delimiting Engineering Problems / ETS1.B Developing Possible Solutions
   □ Crosscutting Concept: Systems and System Models

3. What are the limitations of modeling AI training when real-world neural networks have billions of parameters interacting in ways we cannot fully trace?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Fair AI System for a Real-World Application
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design a neural network-based system for a real-world application (medical diagnosis, college admissions, criminal justice, or hiring) that maximizes accuracy while ensuring fairness across all demographic groups.

SCENARIO: A hospital network wants to deploy an AI system that predicts which emergency room patients are most likely to have a heart attack within 24 hours, allowing faster treatment. However, early testing reveals that the system is significantly less accurate for Black patients because the training data underrepresents this population and uses historical treatment data that reflects existing healthcare disparities. Your team must redesign the training approach to ensure the system works equally well for all patients.

GUIDING QUESTIONS:
• Why does training on historical healthcare data reproduce and potentially amplify existing racial disparities in care?
• How would you ensure the training data adequately represents all patient populations, including those historically underserved?
• What fairness metrics would you require the AI system to meet before deployment, and who should define those metrics?

DESIGN THINKING:
• What specific changes to Training Data Quality and Volume would you make to address the accuracy disparity?

  _________________________________________________________

• What network architecture decisions (depth, regularization) would help prevent overfitting to the majority population's patterns?

  _________________________________________________________

• How would you test the system's performance separately for different demographic groups before deployment?

  _________________________________________________________

• What ongoing monitoring would you require after deployment to detect if the system develops new biases over time?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Design includes specific data collection and curation changes, architecture decisions with regularization rationale, explicit fairness metrics with thresholds, demographic-disaggregated testing protocol, ongoing monitoring plan, and references model evidence for every decision
• Proficient (3): Design addresses data quality, includes fairness metrics, and uses model evidence to justify the approach
• Developing (2): Design identifies the bias problem but lacks specific solutions or does not connect to model evidence
• Beginning (1): Design is incomplete, does not address fairness, or ignores the role of training data quality

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CAST-Aligned Pre/Post Assessment

### Administration Instructions

These 5 multiple-choice questions are administered identically as both a pre-assessment (before Activity 1) and a post-assessment (after Activity 4). Score each out of 5. Learning growth = post-score minus pre-score.

Questions follow the California Science Test (CAST) stimulus-response format. Each item is three-dimensional, assessing a Science and Engineering Practice (SEP), Disciplinary Core Idea (DCI), and Crosscutting Concept (CCC) simultaneously, aligned to HS-ETS1-1, HS-ETS1-4.

---

### Pre-Assessment Questions

### Question 1

Backpropagation is the primary algorithm used to train neural networks. Which description best explains what backpropagation does?

A. It forwards data through the network to produce a prediction
B. It calculates how much each connection weight contributed to the prediction error and adjusts weights to reduce that error
C. It randomly generates new connection weights after each training cycle
D. It removes neurons that produce incorrect outputs

Correct Answer: B

Feedback: Correct. Backpropagation calculates the gradient of the error with respect to each weight, then adjusts weights in the direction that reduces the error. This process repeats millions of times to gradually improve the network's predictions. Backpropagation works backward from the output error, calculating each weight's contribution to that error, then adjusting weights to reduce the error. It is a systematic optimization process, not random or destructive.

---

### Question 2

A neural network achieves 99% accuracy on its training data but only 60% accuracy on new, unseen data. Which concept best explains this discrepancy?

A. The network needs more training time to improve on new data
B. Overfitting: the network memorized specific training examples rather than learning generalizable patterns
C. The new data contains errors that confuse the network
D. The network has too few layers to process new data types

Correct Answer: B

Feedback: Correct. The large gap between training accuracy (99%) and validation accuracy (60%) is the hallmark of overfitting. The network memorized the training examples instead of learning the underlying patterns that would generalize to new data. This gap between training and validation performance is the classic signature of overfitting. The network essentially memorized answers rather than understanding patterns, like a student who memorizes test answers without understanding the concepts.

---

### Question 3

Why does training data quality have a more significant impact on neural network fairness than network architecture?

A. Network architecture determines the speed of training but not the quality of outputs
B. The network never sees the real world directly; it only learns patterns from whatever data humans provide, so biases in the data become biases in the model
C. Network architecture is always unbiased regardless of training data
D. Training data quality only affects accuracy, not fairness

Correct Answer: B

Feedback: Correct. A neural network's understanding of the world is entirely derived from its training data. If the data underrepresents certain populations or encodes historical biases, the model will reproduce and potentially amplify those biases. Neural networks learn exclusively from their training data. They have no independent knowledge of the world. If training data is biased, incomplete, or unrepresentative, the model's outputs will reflect and potentially amplify those biases regardless of architecture.

---

### Question 4

The learning rate is a critical hyperparameter in neural network training. What happens if the learning rate is set too high?

A. The network trains more slowly but achieves higher accuracy
B. The network's weight adjustments are too large, causing it to overshoot optimal values and potentially never converge on a good solution
C. The network automatically adjusts the learning rate to compensate
D. Training data quality becomes less important at higher learning rates

Correct Answer: B

Feedback: Correct. A learning rate that is too high causes weight updates that are too large, causing the optimization to oscillate wildly or diverge rather than converging on the optimal solution. When the learning rate is too high, each weight adjustment overshoots the optimum. Instead of gradually descending toward the best solution, the network bounces around or diverges, failing to learn effectively.

---

### Question 5

Training GPT-4 reportedly cost over $100 million in computational resources. What does this reveal about the relationship between model capability and resource consumption in current AI development?

A. The high cost indicates that the model is inefficient and should use fewer parameters
B. Current state-of-the-art performance relies on scaling data, parameters, and compute, creating an exponentially increasing resource demand that raises questions about sustainability and access
C. The cost is a one-time investment that does not recur for future models
D. More expensive models always produce proportionally better results

Correct Answer: B

Feedback: Correct. The 'scaling paradigm' in AI achieves performance gains by increasing data, parameters, and compute, but each increment of improvement requires exponentially more resources, raising questions about sustainability, energy consumption, and who can afford to build frontier models. The enormous training cost reflects the scaling paradigm: bigger models with more data and compute produce better results, but the resource requirements grow exponentially. This raises fundamental questions about sustainability and whether only a few organizations can afford frontier AI.

---

### Post-Assessment Questions

### Question 1

A student's neural network model shows that increasing network depth from 5 to 20 layers improves pattern recognition accuracy from 75% to 92% but increases overfitting risk from 10% to 45%. What is the most scientifically sound interpretation of this trade-off?

A. Deeper networks are always better because accuracy is the only metric that matters
B. The depth-accuracy relationship exhibits diminishing returns that are offset by accelerating overfitting risk, suggesting that optimal network design requires balancing representational power against generalization ability
C. The overfitting can be ignored if the training accuracy is high enough
D. Reducing depth to 1 layer would eliminate overfitting while maintaining accuracy

Correct Answer: B

Feedback: Correct. The model reveals a nonlinear trade-off: accuracy gains diminish with depth while overfitting risk accelerates. Optimal design requires finding the depth that maximizes the gap between genuine pattern learning and memorization. The data shows diminishing accuracy returns (75% to 92%) against accelerating overfitting risk (10% to 45%). Optimal network design must balance the representational power of deeper networks against their tendency to memorize rather than generalize.

---

### Question 2

In the model, a student trains two identical networks on the same task, one with a diverse, representative dataset and one with a dataset that overrepresents one demographic group. Both achieve 90% overall accuracy. Why does the second network pose a fairness problem despite equal overall accuracy?

A. Overall accuracy masks performance disparities across subgroups; the biased network likely performs well on the overrepresented group and poorly on underrepresented groups
B. Both networks are equally fair because they have the same overall accuracy
C. The second network will naturally correct its bias through continued training
D. Demographic composition of training data does not affect neural network outputs

Correct Answer: A

Feedback: Correct. Aggregate accuracy can hide severe disparities. A model trained on biased data may achieve 98% accuracy on the overrepresented group and 60% on others, averaging to 90% overall but performing unacceptably for underrepresented populations. Overall accuracy is a misleading metric when data is biased. The biased network likely achieves high accuracy on the overrepresented group and much lower accuracy on underrepresented groups, creating discriminatory performance that is hidden by the aggregate number.

---

### Question 3

The model demonstrates that reducing the learning rate from 0.01 to 0.001 increases training time by 10x but reduces the loss function value by 30%. A student proposes using the higher learning rate to save time. What critical factor does this proposal overlook?

A. Training time is the only relevant cost metric
B. The higher learning rate may cause the optimization to settle in a suboptimal local minimum or oscillate, while the lower rate's 30% better loss translates to meaningfully better real-world performance that justifies the computational investment
C. Learning rate has no effect on final model quality
D. The 10x time increase can be eliminated by using fewer training examples

Correct Answer: B

Feedback: Correct. The 30% improvement in loss function represents meaningfully better pattern learning. The higher learning rate saves time but risks suboptimal convergence. The trade-off between training cost and model quality must be evaluated against the application's requirements. A higher learning rate often settles in suboptimal solutions because it overshoots better minima. The 30% loss improvement from the lower rate represents substantially better learning quality. For high-stakes applications, the 10x time investment may be essential.

---

### Question 4

A student observes that their model's computational cost scales quadratically with the number of parameters but performance improvements scale logarithmically. What does this relationship predict about the long-term sustainability of the 'scale everything up' approach to AI?

A. Scaling will always produce proportional improvements in performance
B. The widening gap between exponentially growing costs and diminishing performance returns suggests that scaling alone will eventually become economically and environmentally unsustainable, necessitating fundamental algorithmic breakthroughs
C. Hardware improvements will always keep pace with scaling demands
D. The logarithmic performance curve indicates that AI has reached its maximum capability

Correct Answer: B

Feedback: Correct. When costs grow quadratically but returns grow logarithmically, each increment of improvement becomes dramatically more expensive. This divergence predicts that pure scaling will hit economic and environmental limits, requiring new approaches. The divergence between quadratic cost growth and logarithmic performance improvement means each additional unit of capability costs far more than the last. This trajectory is unsustainable and implies that continued AI progress will require algorithmic innovations, not just bigger models.

---

### Question 5

Based on the neural network model, which conclusion about the relationship between training data volume and model generalization is best supported by the simulation?

A. More training data always produces better generalization without any diminishing returns
B. Training data volume improves generalization with diminishing returns, and beyond a threshold, additional data quality and diversity matter more than volume because the model has already captured the primary patterns in the data distribution
C. Training data volume has no effect on generalization; only network architecture matters
D. Generalization decreases with more training data because the network becomes confused

Correct Answer: B

Feedback: Correct. The model shows diminishing returns from data volume. After the network captures the distribution's primary patterns, additional identical data provides little benefit. Data quality and diversity, ensuring all subgroups and edge cases are represented, become more important than raw volume. Data volume helps generalization but with diminishing returns. Once the primary patterns are learned, adding more data of the same type provides minimal benefit. At that point, data quality and diversity, covering edge cases and underrepresented scenarios, become the limiting factors.

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
Question 2: A
Question 3: B
Question 4: B
Question 5: B

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-11/G11L3-L04/G11L3-L04-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-11/G11L3-L04/G11L3-L04-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-11/G11L3-L04/G11L3-L04-Student-Presentation.pptx] |
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