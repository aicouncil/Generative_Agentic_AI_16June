# Where Are We in the Encoder Block?

Here’s the full flow again:

```
Input
 |
 |-> Multi-head Self-Attention
 |-> Add & Norm
 |-> Feed Forward Network (FFN)
 |-> Add & Norm
Output
```

You are at the **Feed Forward Network (FFN)** step.

---

## What is the Feed Forward Network (FFN)?

It’s a simple 2-layer neural network (the same one applied to each word independently and in parallel).

Think of it like this:

- Each word's vector (after attention) goes through a mini brain (MLP) that helps it transform into a richer representation.

---

## FFN Formula

For each word (i.e., for each vector **x**):

```
FFN(x) = max(0, xW₁ + b₁)W₂ + b₂
```

That’s just:

- A linear transformation (W₁, b₁)
- A ReLU activation (introduces non-linearity)
- Another linear transformation (W₂, b₂)

---

## Dimensions

Assume:

- Input vector **x** has size `d_model = 512`
- Inner layer has size `d_ff = 2048`

Then:

- W₁ shape: (512 × 2048)
- W₂ shape: (2048 × 512)

So:

```
Input vector (512,) 
    → W₁ → ReLU → W₂ → Output vector (512,)
```

**Shape remains the same** (512 in → 512 out), so it fits well into the overall Transformer architecture.

---

## Example

Let’s say your context-aware vector (after attention) for the word "Transformers" is:

```
x = [0.3, 0.1, 0.5, 0.2]  # simplified to 4D for example
```

Let’s define:

- W₁ is a (4×8) matrix → expands dimensionality
- W₂ is (8×4) → compresses back

**Step 1: Linear layer + ReLU**

```
h1 = ReLU(x @ W₁ + b₁)  # shape becomes (8,)
```

Let’s say output after ReLU:

```
h1 = [0.2, 0.0, 0.7, 0.3, 0.0, 0.1, 0.4, 0.2]
```

**Step 2: Second Linear layer**

```
output = h1 @ W₂ + b₂  # shape becomes (4,)
```

Now you have your final FFN output:

```
[0.45, 0.3, 0.2, 0.5]  # enriched version of original
```

---

## Add & Norm After FFN

Just like after self-attention, we wrap FFN with:

- Residual Connection (Add input to FFN output)
- Layer Normalization

```
output = LayerNorm(x + FFN(x))
```

This ensures:

- Stability during training
- Gradient flow
- No vanishing/exploding issues

---

## Why is FFN Important?

While attention helps a word gather info from others, the FFN:

- Transforms the combined information
- Helps learn complex mappings
- Increases representation power

Think of it as:

> “I know what to focus on (thanks to attention), now let me process and refine that knowledge.”

---

## In Summary

| Part                 | Role                              |
|----------------------|-----------------------------------|
| Multi-head Attention | Let each word focus on others     |
| Add & Norm           | Stabilize + preserve info         |
| FFN                  | Process the info further (independently) |
| Add & Norm           | Again stabilize                   |

---

## Key Points About FFN

- Same FFN is applied to each word vector separately
- It’s a position-wise transformation
- Has non-linearity (ReLU)
- Shape stays the same (512 → 2048 → 512)
- Helps encode more abstract features
