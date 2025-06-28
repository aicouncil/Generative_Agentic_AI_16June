# 1. What is Self-Attention? (Intuition)

Imagine you're the word "amazing" in this sentence. To fully understand your meaning, you might look around and realize that "Transformers" gives you important context. That’s self-attention:

> Each word looks at (attends to) other words and decides how much each one matters, to update its meaning.

---

# 2. The Core Formula: Scaled Dot-Product Attention

Here’s the key formula:

```
Attention(Q, K, V) = softmax(Q × Kᵀ / √d_k) × V
```

**Where:**

| Term      | Meaning                 | Analogy                       |
|-----------|------------------------|-------------------------------|
| Q (Query) | What I’m looking for   | What do I need?               |
| K (Key)   | What you offer         | Why should I care about you?  |
| V (Value) | What you say           | The actual information you provide |
| d_k       | Dimension of K         | Scaling factor for stability  |

---

# 3. Let’s Go Step by Step

## Step 1: Word Embeddings

Start with input vectors for each word (say, 4 dimensions):

```
"Transformers": [0.1, 0.3, 0.2, 0.4]
"are":          [0.0, 0.1, 0.0, 0.1]
"amazing":      [0.5, 0.2, 0.1, 0.3]
```

These are the initial word representations (X).

---

## Step 2: Create Q, K, V Matrices

Each word embedding goes through three linear layers to produce:

```
Q = X × W_Q
K = X × W_K
V = X × W_V
```

These weight matrices (W_Q, W_K, W_V) are trained to learn what kind of queries, keys, and values are useful.

**Example output (dummy):**

| Word         | Q           | K           | V           |
|--------------|-------------|-------------|-------------|
| Transformers | [0.2, 0.1, ...] | [0.3, 0.4, ...] | [0.7, 0.5, ...] |
| are          | [0.0, 0.2, ...] | [0.1, 0.1, ...] | [0.1, 0.0, ...] |
| amazing      | [0.3, 0.2, ...] | [0.2, 0.3, ...] | [0.6, 0.4, ...] |

---

## Step 3: Compute Attention Scores (Q × Kᵀ)

Each word's Query vector is compared to all Key vectors using dot product to see how similar (relevant) they are.

This forms a score matrix:

```
      K1    K2    K3
    ┌────┬────┬────┐
Q1→ │0.8 │0.2 │0.7 │ ← "Transformers" attends to...
Q2→ │0.3 │0.1 │0.4 │ ← "are"
Q3→ │0.7 │0.5 │0.9 │ ← "amazing"
    └────┴────┴────┘
```

---

## Step 4: Scale & Softmax

To stabilize training, we divide by √d_k (e.g., if d_k = 4 → √4 = 2):

Example (first row):

```
[0.8, 0.2, 0.7] → [0.4, 0.1, 0.35]
```

Apply softmax:

```
softmax([0.4, 0.1, 0.35]) → [0.41, 0.27, 0.32]
```

This means:

- "Transformers" gives:
    - 41% weight to itself
    - 27% to "are"
    - 32% to "amazing"

---

## Step 5: Weighted Sum of Value Vectors

Now we use the attention weights to combine the V vectors.

For "Transformers":

```
output_1 = 0.41 × V1 + 0.27 × V2 + 0.32 × V3
```

This new output vector is a context-aware version of "Transformers" — it now "knows" it's amazing!

---

# Visual Summary

```
Word Embeddings (X)
    ↓
Linear Layers → Q, K, V
    ↓
Dot(Q, Kᵀ) → Score Matrix
    ↓
Scale + Softmax → Attention Weights
    ↓
Attention Weights × V → New Contextual Vectors
```

---

# Why It’s So Powerful

- Each word understands others — even far away in the sentence.
- Unlike RNNs, there's no left-to-right limitation.
- Everything is parallelizable, so it’s super fast.
- You can add multiple heads (multi-head attention) to learn different patterns at the same time.

---

# Quick Summary Table

| Component     | Role                        |
|---------------|----------------------------|
| Q (Query)     | What I'm looking for        |
| K (Key)       | What you offer              |
| V (Value)     | What you say                |
| Q·Kᵀ          | Match score                 |
| Softmax       | Turn into attention weights |
| Weights × V   | Final output (contextualized vector) |

---
