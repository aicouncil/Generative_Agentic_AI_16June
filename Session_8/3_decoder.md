# Understanding the Decoder: Making Predictions One Word at a Time

## 🧠 What Is a Decoder?

While the encoder understands the input sentence (like English), the decoder generates the output sentence (like Hindi).

Just like a translator listens to a sentence and then speaks it out word by word, the decoder works in steps, generating one word at a time.

---

## 🔧 Decoder Block: Step-by-Step Breakdown

Each decoder block has the following components in this order:

| Step | Component                        | What It Does                                        |
| ---- | -------------------------------- | --------------------------------------------------- |
| 1    | Masked Multi-Head Self-Attention | Looks at **previously generated** words only        |
| 2    | Add & Normalize                  | Stabilizes training                                 |
| 3    | Encoder–Decoder Attention        | Focuses on the **input sentence** (encoder output)  |
| 4    | Add & Normalize                  | Again, keeps everything smooth                      |
| 5    | Feed Forward Network             | Adds extra transformation to improve representation |
| 6    | Add & Normalize                  | Final clean-up before passing to next decoder layer |

---

### 1. Masked Multi-Head Self-Attention

**Why “masked”?**

Because the decoder must not peek at future words — it can only use the words it has already generated.

Imagine you're writing a translation:

- You've written: “मैं एआई”
- You’re about to write the next word.
- You can’t look ahead at the correct answer (“सीख रहा हूँ”) — you can only use “मैं एआई” so far.

🔑 **Masking ensures this happens.**

---

### 2. Encoder–Decoder Attention

Now that the decoder knows what it's written so far, it looks at the encoder’s output to get information from the input sentence.

It uses the same Query–Key–Value (Q-K-V) mechanism:

- **Query:** decoder’s current word
- **Key & Value:** encoder output vectors

**Example:**  
If you’re generating the word “एआई”, the decoder may look back at the word “AI” from the input sentence to get help.

---

### 3. Feed Forward + Add & Normalize

This is just like the encoder:

- Each word's vector goes through a small neural network.
- Then we use Add & Norm again to make training stable.

These steps help turn attention outputs into useful representations for the final prediction.

---

## 🧾 Step-by-Step: How Prediction Happens

1. **Start with Input:**  
   Sentence: “Transformers are amazing”

2. **Tokenization:**  
   Turns into numbers: [20345, 1012, 8763]

3. **Embeddings + Positional Encoding:**  
   Vectors for each word + position added.

4. **Encoder Processes Input:**  
   Understands relationships (e.g., “amazing” describes “Transformers”).

5. **Decoder Starts Generating Output:**
    - First input: [“मैं”]
    - Predicts next: “एआई”, then “सीख”, then “रहा”, then “हूँ”

6. **Each Decoder Layer Includes Attention:**
    - Looks at previous outputs
    - Looks at encoder outputs
    - Combines everything to decide next word

---

## 🎯 Final Output: One Token at a Time

At each step:

- The decoder produces a vector.
- That vector goes through:
    - Linear layer (to match vocab size)
    - Softmax (to get probabilities)

**Example:**

Output vector → {"मैं": 0.6, "तुम": 0.2, "AI": 0.05, ...}  
Highest score → “मैं” is chosen

The process repeats until a special `[END]` token is generated.

---

## 🧠 Recap

| Component               | Role                                                |
|-------------------------|-----------------------------------------------------|
| Masked Self-Attention   | Looks at past words only (no peeking ahead)         |
| Encoder–Decoder Attn.   | Looks at input sentence from encoder                |
| Feed Forward Layer      | Adds more understanding                             |
| Linear + Softmax        | Chooses next word                                   |
| Repeats                 | One word at a time, until done                      |
