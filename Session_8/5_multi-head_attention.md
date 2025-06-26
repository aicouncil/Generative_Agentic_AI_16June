# Multi-Head Attention & Positional Encoding

We'll break down both concepts with clear analogies, visuals (in text), step-by-step math, and detailed examples.

---

## 🔷 PART 1: Multi-Head Attention

### ❓ Why Do We Need Multi-Head Attention?

Single-head attention can only learn **one kind** of relationship at a time. But language is complex!  
Let's look at this sentence:

> **"The cat sat on the mat."**

Some relationships we want the model to learn:

- **Syntactic roles:** Who is the subject? (the cat), what is the verb? (sat), what is the object? (the mat)
- **Coreference:** "the cat" may later be referred to as "it"
- **Emphasis/meaning:** Which words are important for the sentence's sense?

**Limitation:**  
If you use only one attention head, it might only focus on, say, the most important word, but miss out on other patterns.

---

### ✅ Solution: Use Multiple Attention Heads

**Multi-Head Attention** means the transformer uses several attention "heads" in parallel.  
Each head:

- Has its **own Q, K, V matrices** (learns different parameters)
- Focuses on **different types of relationships**
- **Operates in parallel**, then their outputs are combined

#### **Example Diagram:**

```
Input Sentence:
"The cat sat on the mat."

         ┌───────────────┐
         │ Input Tokens  │
         └─────┬─────────┘
               │
        ┌──────┴─────────┐
        │  Multi-Head    │
        │   Attention    │
        └─────┬──────────┘
   ┌──────────┴────────────┬─────────────┬─────────────┐
   │ Head 1                │ Head 2      │ Head 3      │
   │ (focus: grammar)      │ (focus:     │ (focus:     │
   │                       │ coreference)│ position)   │
   │                       │             │             │
   └──────────┬────────────┴─────────────┴─────────────┘
              │
          Concatenate
              │
       Linear Projection
              │
           Output
```

#### **Step-by-Step Math (per head):**

For each head \( h \):

1. **Project input embeddings:**  
   \( Q_h = X W^Q_h \)  
   \( K_h = X W^K_h \)  
   \( V_h = X W^V_h \)

2. **Calculate attention weights:**  
   \( \text{Attention}_h(Q, K, V) = \text{softmax}\left(\frac{Q_h K_h^T}{\sqrt{d_k}}\right) V_h \)

3. **Do this for all heads in parallel.**

4. **Concatenate outputs:**  
   \( \text{Concat}(\text{head}_1, ..., \text{head}_n) \)

5. **Project with another linear layer to mix information.**

---

### **Detailed Example:**

Suppose we have 2 heads and a mini-sentence:  
> "She eats fish"

- **Head 1:** Might learn to connect pronouns to verbs ("She" ↔ "eats")
- **Head 2:** Might learn object relationships ("eats" ↔ "fish")

For the word "eats":

- Head 1 output: focuses on "She"
- Head 2 output: focuses on "fish"

**After concatenation + linear projection:**  
The model's representation of "eats" now "knows" about both the subject ("She") and object ("fish").

---

### **Summary Table: Multi-Head Attention**

| Feature            | Benefit                                   |
|--------------------|-------------------------------------------|
| Parallel heads     | Learn different patterns simultaneously   |
| Richer output      | Context considers multiple relationships  |
| Improved learning  | Captures subtle language dependencies     |

---

## 🔷 PART 2: Positional Encoding

### ❓ Why Do We Need Positional Encoding?

Transformers **do not** use recurrence (like RNNs) or convolution (like CNNs).  
Without any modification, they **cannot distinguish word order**!

> "The cat sat on the mat."  
> "Sat the on cat the mat."

→ The model would treat these as the same! (since attention is order-agnostic)

---

### ✅ Solution: Add Positional Information to Embeddings

**Key Idea:**  
Add a unique vector to each word embedding based on its position in the sentence.

#### **How It Works:**

- **Word embedding:** Encodes word meaning (e.g., "Transformers" → `[0.1, 0.3, 0.2, 0.4]`)
- **Positional encoding:** Encodes the token's position (e.g., position 0 → `[0.5, 0.1, 0.3, 0.6]`)
- **Final input:** Add both vectors element-wise:
  ```
  [0.1, 0.3, 0.2, 0.4]    (embedding)
+ [0.5, 0.1, 0.3, 0.6]    (positional encoding)
= [0.6, 0.4, 0.5, 1.0]    (input to transformer)
  ```

#### **(Optional) How are Positional Encodings computed?**

Common method: **Sinusoidal encoding** (so model can generalize to longer sequences):

- For each position \( pos \) and dimension \( i \):
  - \( PE_{(pos, 2i)} = \sin(pos / 10000^{2i/d_{model}}) \)
  - \( PE_{(pos, 2i+1)} = \cos(pos / 10000^{2i/d_{model}}) \)

But you can also learn the encodings!

---

### **Visual Summary:**

```
Token Embedding:       [word meaning]
Positional Encoding: + [word position]
                     = Final Input to Transformer
```

---

### **Summary Table: Positional Encoding**

| Without PE                    | With PE                                   |
|-------------------------------|-------------------------------------------|
| All positions look the same   | Each position has a unique identity       |
| No sense of "first/second"    | Learns position-sensitive representations|

---

## 🔶 Final Concept Table

| Concept                | Purpose                                    |
|------------------------|--------------------------------------------|
| Multi-Head Attention   | Learn different relationships in parallel  |
| Positional Encoding    | Add sequence order information to model    |

---

**In summary:**  
- **Multi-head attention** lets the model learn several types of relationships between words at once.
- **Positional encoding** gives the model a sense of word order, so it knows "cat sat" ≠ "sat cat".

Both are crucial for the power and flexibility of the Transformer architecture!
