# The Real Purpose of Masking in the Decoder: Training vs Inference

Let’s break it into two situations:

---

## 1. During Training (Teacher Forcing is Used)

We already know the correct translation, for example:

```
Hindi Target = “गुलाब लाल हैं और आकाश नीला है”
```

**We feed it like this:**

- Input to encoder = English sentence (source)
- Input to decoder = Shifted Hindi target sentence:

```
[START], गुलाब, लाल, हैं, और, आकाश, नीला
→ Output:      गुलाब, लाल, हैं, और, आकाश, नीला, है
```

### Step 1: What is Decoder Learning to Do?

The decoder is trained to predict the next word, one step at a time.

For example, for the sentence:

```
“गुलाब लाल हैं और आकाश नीला है”
```

We don’t give the whole sentence to be copied.  
We give input-output pairs like this:

| Input to Decoder (shifted)  | Target Output |
|-----------------------------|---------------|
| [START]                     | गुलाब         |
| [START], गुलाब              | लाल           |
| [START], गुलाब, लाल         | हैं           |
| ...                         | ...           |

---

### Step 2: The Magic of Training = Teacher Forcing

We don’t wait for the model to generate the correct output by itself from scratch.

Instead, we use the true previous words (from the training data) as input, like this:

During training:

- Input to decoder: `[START], गुलाब, लाल`
- Target to predict: `→ हैं`

So the decoder:

- Gets actual correct history (`[START], गुलाब, लाल`)
- Is trained to predict the next correct word (`हैं`)
- But we mask it so that each position:
    - Can attend to itself and to the left
    - Cannot cheat by looking at future words (like “हैं” or “आकाश”)

---

### Step 3: What If There’s No Masking?

Without masking, the decoder could just peek ahead at the next correct word, because the full sentence is right there during training.

This would be like:

- Decoder input: `[START], गुलाब, लाल, हैं, ...`
- Query at “गुलाब”: sees “लाल” ahead → just memorize and cheat!

It doesn't learn to generate the next word. It just copies.

---

### With Masking — It Still Learns, Not Guesses Randomly

Let’s say we are at position 2, trying to predict “लाल”:

- Decoder sees input: `[START], गुलाब`
- It runs masked self-attention, so:
    - “गुलाब” can only attend to `[START]` and “गुलाब”
    - It does NOT see “लाल” or beyond
- But the correct label (“लाल”) is known
- The loss function will penalize if decoder predicts “abcde” or any wrong word
- The model learns that given `[START], गुलाब`, the correct next word is “लाल”

#### So how does it NOT predict “abcde”?

Because during training:

- The correct previous words are used as inputs (not random guesses)
- The model is penalized (via loss) when it guesses wrong
- Over time, it learns strong associations like:

  If input = `[START], गुलाब` → correct next word = “लाल”

---

## If Masking is Not Done

**Bad Outcome:**

The decoder could:

- Look at the full target sentence
- Directly “copy” the next word (it knows the answer!)
- Get artificially low training loss, but fail during inference (real-world use)

It would never learn to:

- Predict the next word based on what has been generated so far + context from encoder

**Result:** It fails at generation time.

---

## 2. During Inference (Generation Time)

At generation time:

- No Hindi sentence is available
- We generate word by word
- After generating “गुलाब”, we feed it back in to predict “लाल”
- Masking naturally happens because:
    - We’ve only generated up to “गुलाब”
    - Later words aren’t available yet

**So:** In inference, masking automatically applies because you literally don’t have future tokens.

---

## So What Does Masking Actually Do?

| Without Masking                  | With Masking                                |
|----------------------------------|---------------------------------------------|
| Sees full future → cheats        | Only sees past → learns properly            |
| Unrealistic loss during training | Realistic autoregressive learning           |
| Model performs poorly in real life | Model learns proper generation logic       |

---

## Visual Analogy

- Imagine you're writing a sentence word-by-word on a whiteboard.
- If you're allowed to see the full final sentence — you’ll just copy.
- But if you're only allowed to see what you’ve written so far, you’ll have to think: “Hmm, based on this, what comes next?”

That's masked self-attention.

---

## Summary

| Concept                        | Clarification                                                                 |
|--------------------------------|-------------------------------------------------------------------------------|
| We provide correct decoder inputs | Yes (during training we use true tokens from the dataset)                  |
| Then why mask?                 | So the model can’t cheat by attending to future words                        |
| Doesn’t that make it guess randomly? | No — because it still sees the correct context so far, and learns from it |
| So it still gets supervision?  | Yes — via cross-entropy loss on the correct next word                        |
| At test time, what changes?    | We don’t provide the target. The model generates one word at a time, feeding its own output back in. |

| Concept              | Why It’s Used                                                     |
|----------------------|-------------------------------------------------------------------|
| Masking in Decoder   | Prevents model from cheating by looking ahead                     |
| Without Masking      | Decoder would just memorize the sequence                          |
| With Masking         | Model learns how to generate next word based only on past + encoder context |
| Training             | Masking needed even though full output is available               |
| Inference            | Masking happens naturally since future words aren't generated yet |
