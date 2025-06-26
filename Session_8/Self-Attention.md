# 📌 What is Self-Attention?

### 🎯 Goal: Let each word in a sentence focus on the other words that are most relevant to its meaning.

Imagine this sentence:

> "The cat sat on the mat because it was tired."

**Question:** What does "it" refer to?  
**Answer:** "cat"

To make sense of this, a model must understand that "it" refers back to "cat". **Self-Attention** helps the model figure that out by letting every word "look at" other words and decide which ones are important.

---

## 🔍 Real-Life Example of Self-Attention

Sentence: **"Transformers are amazing"**

What should the model understand?

* "amazing" describes **"Transformers"**, not **"are"**.

Here’s what Self-Attention learns:

* **"Transformers"** attends to **"amazing"**
* **"are"** is less important
* **"amazing"** attends back to **"Transformers"**

---

## 🧠 How It Works: The Q-K-V Magic

Each word creates **3 vectors**:

1. **Query (Q):** What am I looking for?
2. **Key (K):** What do I offer?
3. **Value (V):** What do I say if you pay attention to me?

### 🧮 Attention Score:

> `Attention Score = Q · K` (Dot product between query and key)

This score tells the model how much focus (or attention) one word should give to another.

---

### 🧾 What Happens Step by Step:

1. Compute the dot product between the query and all keys.
2. Apply Softmax to turn these into probabilities (attention weights).
3. Use these weights to get a **weighted sum of the value vectors**.
4. The result is a **contextualized vector** for each word.

---

### 🧠 Contextualized Vector:

This is a vector that represents a word **in context** — it “knows” the meaning of the surrounding words.

**Example:**

* "bank" in
    * "river bank" → means riverside
    * "go to the bank" → means financial institution

The vector for "bank" is different in each case.

---

# 🔁 What is Multi-Head Attention?

Instead of doing self-attention once, we do it **multiple times in parallel**, using different "heads".

**Example (with 3 heads):**

* **Head 1:** Looks at subject-verb relations
* **Head 2:** Focuses on adjective-noun links
* **Head 3:** Tracks long-distance dependencies

### 🛠 Then:

* All heads are **concatenated and combined** to produce a richer understanding.

---

# 🧪 Add & Norm (Add and Normalize)

After each attention or feedforward step:

1. **Add:** Add the original input back (this is called a *residual connection*)
2. **Normalize:** Stabilizes the learning and makes it smoother

---

# 🔧 Feed Forward Network (FFN)

Each word’s vector is passed through a small neural network:

> `FFN(x) = ReLU(W1·x + b1) → W2·x + b2`

It helps to transform the output of attention into something richer.

---

# ✅ Final Encoder Output

After all encoder layers are done:

* Each word becomes a **deeply contextualized vector**.
* These vectors are used for further tasks (e.g., translation).

**Example:**

> "Transformers" → \[0.1, 0.3, ..., 0.7]  (knows it’s being called "amazing")

These vectors are also called **hidden states**.

---
