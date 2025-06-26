# How Transformers Learn Attention: Behind the Scenes

---

## 🔍 What Are Contextualized Vectors?

A **contextualized vector** is a word's numerical meaning that changes based on the words around it.

**Example:**
- “bank” in “river bank” → river side
- “bank” in “money bank” → financial institution

💡 These meanings are different, so the vectors (numbers) for the word “bank” are different in each case.

---

## 🔄 How Transformers Create Contextual Vectors

Let’s understand how this happens using **Self-Attention** and training.

---

### 🧱 Step 1: Initial Word Embeddings (Non-Contextual)

Each word is converted to a fixed vector (just a representation, not yet contextual).

**Example:**
- “Transformers” → `[0.2, 0.4, …]`
- “are” → `[0.3, 0.1, …]`
- “amazing” → `[0.5, 0.7, …]`

---

### 🔧 Step 2: Generate Query, Key, Value Vectors (Q, K, V)

Each embedding goes through three learned layers:

```
Q = x @ W_Q
K = x @ W_K
V = x @ W_V
```
Where:
- `x` = embedding of a word
- `@` = matrix multiplication
- `W_Q, W_K, W_V` = learned weights

These are used to calculate attention.

---

### 🔢 Step 3: Compute Attention Scores

For every pair of words:

```
Score = dot(Qᵢ, Kⱼ)
```
This tells us how much word *i* should attend to word *j*.

We apply **Softmax** on these scores to get attention weights.

**Example scores:**
- “amazing” → “Transformers” = 8
- “amazing” → “are” = 2
- “amazing” → “amazing” = 5

After Softmax → `[0.84, 0.01, 0.15]`

---

### 🎯 Step 4: Weighted Sum of Value Vectors

Each word’s new vector =

> Sum of all value vectors (V), weighted by attention weights

This new vector is **contextualized** — it “knows” what to focus on.

---

### 🔁 Happens in All Layers

Each layer builds deeper meaning:
- **Early layers:** grammar and structure
- **Later layers:** semantics and relationships

By the end, each word “understands” its full sentence context.

---

## ❓How Does the Model Learn These Attention Weights?

Let’s go step by step 👇

---

### 🧪 Step 1: Training Data

We give the model:
- **Input:** “Transformers are amazing”
- **Output:** “ट्रांसफॉर्मर अद्भुत हैं”

We don’t tell the model:
- “amazing” should attend to “Transformers”

---

### 🧠 Step 2: Model Makes a Guess

At first, the model might guess wrong:
- Predicted: “हैं अद्भुत ट्रांसफॉर्मर”

This is incorrect.

---

### 🧮 Step 3: Loss Function Calculates Error

The loss function checks how far the model’s prediction is from the actual answer.

- Wrong prediction = high loss
- Correct prediction = low loss

---

### 🔧 Step 4: Backpropagation Fixes the Mistake

Using the loss, the model updates:

- `W_Q, W_K, W_V`
- Embedding layers
- Feedforward layers

Now, “amazing” learns to pay more attention to “Transformers”, not “are”.

---

### 📈 Over Thousands of Sentences…

The model sees:
- “Books are interesting”
- “Cars are fast”
- “Transformers are amazing”

It starts learning that adjectives like ‘amazing’ describe nouns, not verbs like “are”.

---

### 🧠 Analogy: How You Learned

You weren’t told:
- “‘Beautiful’ describes a noun”

You learned by reading and correcting mistakes.

Transformers do the same — with:
- Vector math
- Prediction errors
- Millions of examples

---

## ✅ Recap: How Context Is Learned

| Component             | What It Does                                       |
|-----------------------|----------------------------------------------------|
| Input Embedding       | Basic word meaning (not contextual yet)            |
| Q, K, V Vectors       | Created from input via learned matrices            |
| Dot Product + Softmax | Creates attention weights (who to focus on)        |
| Value Vectors         | Combined using attention weights                   |
| Multi-Head Attention  | Looks at different relations in parallel           |
| Layers + Training     | Learn deeper meanings through repetition + feedback|

---

## Final Takeaway

- Transformers don’t need to be told what to attend to.
- They learn it themselves — by making guesses, measuring errors, and adjusting focus over millions of examples.

**That’s Self-Attention + Training in action. 🔁**
