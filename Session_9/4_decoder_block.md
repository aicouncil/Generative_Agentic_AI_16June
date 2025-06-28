# Step-by-Step Decoder Architecture Breakdown

```
Input (Generated so far)
 |
 |-> Masked Multi-head Self-Attention
 |-> Add & Norm
 |-> Encoder-Decoder Attention
 |-> Add & Norm
 |-> Feed Forward Network (FFN)
 |-> Add & Norm
Output (Next word probabilities)
```

Let’s unpack each component.

---

## 1. Masked Multi-head Self-Attention

**What is self-attention?**  
Each word looks at all other words and decides what’s important.

**What’s new here: Masking!**  
In the decoder, the model cannot peek at future words.

**Example:**  
Generating the sentence:  
`"The cat sat on the mat."`  
At time step 3 (predicting "sat"), the decoder should only know:  
- "The"
- "cat"  
It should not look ahead to "on the mat".

**How do we block future words?**  
We use a masking matrix.

**Example Mask (at position 3):**
```
[
 [1, 0, 0],
 [1, 1, 0],
 [1, 1, 1]
]
```
- Word 1 attends only to itself
- Word 2 attends to word 1 and itself
- Word 3 attends to word 1, 2, and itself

This is called a *causal mask* or *look-ahead mask*.

**What happens here?**
- Decoder input embeddings → Linear layers → Q, K, V
- Apply self-attention with masking
- Ensures word t only attends to positions ≤ t (not t+1, t+2, …)
- Output: contextual vectors based on generated words so far

---

## 2. Encoder-Decoder Attention

**Idea:**  
Lets the decoder attend to the full encoder outputs (source sentence) — *without* masking.

- Query (Q) comes from the decoder (previous step)
- Key (K) and Value (V) come from the encoder outputs

**Example:**  
Source sentence: `"Transformers are amazing"`  
Decoder is generating: `"Les transformateurs"` (in French)

At each time step, the decoder:
- Looks at all previously generated words (via masked self-attention)
- Then attends to the full source sentence (via encoder-decoder attention)
    - For example, so it can “know” that "Transformers" maps to "Les transformateurs"

**Why is this important?**
- Focus on relevant source words while generating
- Choose what to translate or copy
- Capture alignment (useful for translation, summarization, etc.)

---

## 3. FFN and Add & Norm (Same as Encoder)

After attention, the same steps as in the encoder:

- **Feed Forward Network (FFN):** Processes information per token
- **Residual Connection:** Add input back to output of layer
- **Layer Normalization:** Stabilize values

---

## Visual Summary of One Decoder Layer

```
Decoder Input (e.g., "Les")
  ↓ Masked Multi-Head Self-Attention
    [Sees only "Les"]
  ↓ Add & Norm

  ↓ Encoder-Decoder Attention
    [Looks at full encoded source: "Transformers are amazing"]
  ↓ Add & Norm

  ↓ Feed Forward Network (process info)
  ↓ Add & Norm

→ Output vector for "Les"
```

---

## So What's Happening During Generation?

Suppose the decoder is to generate:  
`“Les transformateurs sont incroyables”`

At each time step:
- Decoder has generated: “Les”
- Masks future words, attends to “Les”
- Attends to the entire source sentence
- Uses attention outputs + FFN to predict the next word: “transformateurs”
- Adds the predicted word to the input and repeats

This is called **auto-regressive generation** — word by word, left to right.

---

## Final Summary

| Step                           | What It Does                                  | Why It Matters                                          |
|--------------------------------|-----------------------------------------------|---------------------------------------------------------|
| Masked Multi-head Self-Attention | Each word looks only at past words            | Enables autoregressive generation (no cheating!)        |
| Add & Norm                     | Residual + Normalize                          | Helps stable training                                   |
| Encoder-Decoder Attention      | Decoder word looks at the entire source sentence | Helps map source to target (e.g., translation)          |
| Add & Norm                     | Again, stabilize and preserve info            | Improves gradients                                      |
| FFN                            | Refines info per token                        | Adds depth and complexity                               |
| Add & Norm                     | Final normalization                           | Clean output to next layer or final softmax             |
