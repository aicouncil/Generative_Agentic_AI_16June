# Keras Embedding and Neural Network Text Classification – Detailed Explanations & Example

This document provides a comprehensive walk-through of Keras Embedding layers, followed by building a neural network to classify whether a text is about _cricket_ or _chess_. All concepts are supported by step-by-step explanations and practical code examples.

---

## 1. Keras Embedding Layer

### What is an Embedding Layer?

The **Embedding** layer in Keras is used to convert positive integer indices (representing words or tokens) into dense vectors of fixed size. These dense vectors are called **word embeddings**.

**Why use embeddings?**
- Text is categorical; models need numbers.
- One-hot encoding is sparse and high-dimensional. Embeddings are dense, low-dimensional, and learn word similarity (e.g., “king” and “queen” have closer vectors).

---

### Example: Creating an Embedding Layer in Keras

```python
from tensorflow.keras import models, layers

model = models.Sequential()
model.add(layers.Embedding(input_dim=9, output_dim=4, input_length=5))
model.summary()
```

**Arguments:**
- `input_dim=9`: Vocabulary size (number of unique tokens/words). Add 1 for padding.
- `output_dim=4`: Embedding vector size for each word.
- `input_length=5`: Length of each input sequence after padding.

**What happens?**
- Given a sequence like `[2, 3, 1, 4, 5]`, the embedding layer converts each integer into a vector of size 4.
- Output is a matrix of shape `(batch_size, input_length, output_dim)`.

#### Concrete Example

```python
import numpy as np
X = np.array([
    [2, 3, 1, 4, 5],  # "I am playing good cricket"
    [6, 7, 1, 8, 0]   # "He is playing chess" (0 is padding)
])
output = model.predict(X)
print(output.shape)  # (2, 5, 4)
print(output)
```

- Each sentence: 5 tokens.
- Each token: 4-dimensional vector.
- Output shape: (2 sentences, 5 tokens each, 4 values per token).

---

### How does it work during training?

- The embedding matrix starts with random values.
- During training, the network learns the best embedding values so that words with similar meanings get similar vectors.

---

### Visualizing Embeddings

After training, embeddings for “cricket” and “chess” might look like:
- “cricket”: `[0.1, 0.8, -0.2, 0.5]`
- “chess”: `[0.12, 0.85, -0.18, 0.47]`
If these vectors are close, the model has learned that the words are similar in some context.

---

### Practical Example

```python
from tensorflow.keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from tensorflow.keras import models, layers

texts = [
    "I love machine learning",
    "Deep learning is fun",
    "I enjoy learning"
]

# Tokenize
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
padded = pad_sequences(sequences, padding='post')

vocab_size = len(tokenizer.word_index) + 1
embedding_dim = 5
input_length = padded.shape[1]

model = models.Sequential()
model.add(layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=input_length))
model.summary()

output = model.predict(padded)
print(output.shape)  # (3, <max_sentence_length>, 5)
```

---

### Where to use Embeddings?

- Text classification (e.g., sentiment analysis)
- Sequence models (e.g., translation)
- Recommendation systems (e.g., product embeddings)

---

### Embedding Layer Summary

- **Input**: List of integers (tokenized and padded sentences).
- **Output**: Dense vectors for each token.
- **Learns**: Word meaning based on the specific training task.

---

## 2. Neural Network Model for Text Classification

We now build a predictive model to classify whether a sentence is about _cricket_ or _chess_ using the Keras Embedding layer.

---

### Step 1: Data Preparation

```python
texts = [
    "I am playing good cricket",
    "He is playing chess",
    "I like to watch cricket",
    "Chess is a mind game",
    "Cricket is played outdoors",
    "Chess pieces are interesting",
    "We played cricket yesterday",
    "He won the chess match"
]
labels = [0, 1, 0, 1, 0, 1, 0, 1]  # 0: cricket, 1: chess
```

---

### Step 2: Tokenization and Padding

```python
from tensorflow.keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
import numpy as np

tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
maxlen = max(len(seq) for seq in sequences)
padded_sequences = pad_sequences(sequences, maxlen=maxlen, padding='post')
labels = np.array(labels)

print("Word Index:", tokenizer.word_index)
print("Padded Sequences:\n", padded_sequences)
```

---

### Step 3: Model Creation

```python
from tensorflow.keras import models, layers

vocab_size = len(tokenizer.word_index) + 1
embedding_dim = 8

model = models.Sequential()
model.add(layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=maxlen))
model.add(layers.Flatten())
model.add(layers.Dense(8, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))  # Binary classification

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()
```

**Explanation:**
- **Embedding layer:** Learns word representations.
- **Flatten layer:** Converts the 2D embedding output into 1D for Dense layers.
- **Dense layers:** Learn and classify patterns.
- **Sigmoid output:** Predicts probability for binary classification.

---

### Step 4: Model Training

```python
history = model.fit(padded_sequences, labels, epochs=30, verbose=1)
```

---

### Step 5: Making Predictions

```python
def predict_topic(text):
    seq = tokenizer.texts_to_sequences([text])
    pad_seq = pad_sequences(seq, maxlen=maxlen, padding='post')
    pred = model.predict(pad_seq)[0][0]
    return "chess" if pred > 0.5 else "cricket"

print(predict_topic("The batsman scored a century"))  # cricket
print(predict_topic("He moved his knight"))           # chess
```

---

### Step 6: Full Example (All Steps Combined)

```python
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from tensorflow.keras import models, layers

# Data
texts = [
    "I am playing good cricket",
    "He is playing chess",
    "I like to watch cricket",
    "Chess is a mind game",
    "Cricket is played outdoors",
    "Chess pieces are interesting",
    "We played cricket yesterday",
    "He won the chess match"
]
labels = [0, 1, 0, 1, 0, 1, 0, 1]

# Tokenize
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
maxlen = max(len(seq) for seq in sequences)
padded_sequences = pad_sequences(sequences, maxlen=maxlen, padding='post')
labels = np.array(labels)

# Model
vocab_size = len(tokenizer.word_index) + 1
embedding_dim = 8
model = models.Sequential()
model.add(layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=maxlen))
model.add(layers.Flatten())
model.add(layers.Dense(8, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()

# Train
model.fit(padded_sequences, labels, epochs=30, verbose=1)

# Predict function
def predict_topic(text):
    seq = tokenizer.texts_to_sequences([text])
    pad_seq = pad_sequences(seq, maxlen=maxlen, padding='post')
    pred = model.predict(pad_seq)[0][0]
    return "chess" if pred > 0.5 else "cricket"

print(predict_topic("The batsman scored a century"))  # Output: cricket
print(predict_topic("He moved his knight"))           # Output: chess
```

---

## Summary Table

| Step           | Description                                                                                           |
|----------------|-------------------------------------------------------------------------------------------------------|
| Data Prep      | Sentences labeled as "cricket" or "chess"                                                             |
| Tokenization   | Text to integer sequences                                                                             |
| Padding        | All sequences have same length                                                                        |
| Embedding      | Each word turns into a learned dense vector                                                           |
| Model          | Simple neural net: Embedding → Flatten → Dense → Dense (sigmoid)                                      |
| Training       | Model learns to distinguish cricket from chess by optimizing embeddings and weights                    |
| Prediction     | Given a new sentence, predicts if it’s about cricket or chess                                         |

---

## Conclusion

- **Embedding layers** turn word indices into dense vectors, capturing word semantics.
- **Neural networks** can use these embeddings to classify text by topic or sentiment.
- This workflow can be extended to larger datasets, more topics, or more advanced models (e.g., LSTM, GRU).

Feel free to build on this example for more advanced NLP tasks!
