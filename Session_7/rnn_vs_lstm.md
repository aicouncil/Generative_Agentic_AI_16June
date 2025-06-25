# Introduction to RNN and LSTM for Text Generation

## 1. What are RNNs and LSTMs?

### Recurrent Neural Networks (RNNs)
RNNs are a class of neural networks designed for sequential data. Unlike traditional feedforward neural networks, RNNs have connections that form cycles, allowing information to persist from one step to the next. This makes them particularly suitable for tasks involving sequences, such as text, time series, and speech data.

**Key Idea:**  
RNNs process an input sequence one element at a time, maintaining a hidden state that captures information about preceding elements.

**Typical Applications:**  
- Language modeling
- Text generation
- Machine translation
- Speech recognition

### Long Short-Term Memory Networks (LSTMs)
LSTMs are a special kind of RNN capable of learning long-term dependencies. They address the vanishing gradient problem that standard RNNs face by introducing a memory cell and gates (input, forget, and output gates) that regulate the flow of information.

**Key Idea:**  
LSTMs can remember information for long periods, making them highly effective for complex sequential tasks.

---

## 2. Why Use RNN/LSTM for Text Generation?

Text generation involves predicting the next word or character in a sequence, given the previous context. Since the meaning of a word often depends on the words that came before, RNNs and LSTMs are ideal because they can model such dependencies.

---

## 3. Example Workflow: Text Generation with LSTM

### Step 1: Data Preparation

Suppose we have the following text:
```
Hello world. This is a simple LSTM example.
```
We want to train a model that, given a sequence of words, predicts the next word.

**Tokenization Example (using Keras):**
```python
from tensorflow.keras.preprocessing.text import Tokenizer

text = "Hello world. This is a simple LSTM example."
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])
word_index = tokenizer.word_index
print(word_index)
```

**Output:**
```
{'hello': 1, 'world': 2, 'this': 3, 'is': 4, 'a': 5, 'simple': 6, 'lstm': 7, 'example': 8}
```

**Creating Sequences:**
- "Hello world" → Predict "This"
- "world This" → Predict "is"
- ... and so on.

### Step 2: Sequence Padding

All input sequences must be of the same length. We use padding for this.
```python
from tensorflow.keras.preprocessing.sequence import pad_sequences

sequences = [
    [1, 2, 3],  # "Hello world This"
    [2, 3, 4],  # "world This is"
    [3, 4, 5],  # ...
    # etc.
]
padded_sequences = pad_sequences(sequences, maxlen=5)
```

---

### Step 3: Building the LSTM Model

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

vocab_size = len(word_index) + 1  # +1 for padding token

model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=10, input_length=5),
    LSTM(100),
    Dense(vocab_size, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()
```

---

### Step 4: Preparing Labels and Training

The label for each sequence is the "next word" (one-hot encoded for categorical crossentropy).

```python
import numpy as np
from tensorflow.keras.utils import to_categorical

# Suppose 'X' is the padded input and 'y' is the target word index
X = padded_sequences  # shape: (num_samples, sequence_length)
y = [3, 4, 5]        # example target word indices
y = to_categorical(y, num_classes=vocab_size)

# Training (example)
model.fit(X, y, epochs=100, verbose=1)
```

---

### Step 5: Generating Text

To generate text, you feed a seed sequence and repeatedly predict the next word, appending it to the sequence.

```python
import numpy as np

seed_text = "Hello world"
for _ in range(5):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = pad_sequences([token_list], maxlen=5)
    predicted = np.argmax(model.predict(token_list), axis=-1)[0]
    output_word = ""
    for word, index in tokenizer.word_index.items():
        if index == predicted:
            output_word = word
            break
    seed_text += " " + output_word
print(seed_text)
```

---

## 4. Practical Notes and Tips

- **Data Size:** LSTMs perform better with more data. Small datasets may result in poor generation.
- **Temperature Sampling:** To generate more creative text, you can use temperature sampling rather than always picking the highest-probability word.
- **Preprocessing:** Clean and preprocess your text (lowercase, remove punctuation, etc.) for best results.
- **Epochs and Model Size:** Tune the number of LSTM units and training epochs for optimal performance.

---

## 5. Summary

- RNNs and LSTMs are powerful for sequential data like text.
- LSTMs overcome the limitations of basic RNNs for long-term dependencies.
- The general workflow is: preprocess text → tokenize → create input/output sequences → pad sequences → build and train an LSTM model → generate text iteratively.

---

## 6. References

- [TensorFlow Keras Documentation](https://keras.io/api/layers/recurrent_layers/lstm/)
- [Text Generation with LSTM](https://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/)
