# Detailed Explanation of `gen_ai_3.ipynb`

This document provides an in-depth explanation of the topics and code covered in the notebook `gen_ai_3.ipynb`, found in the [Session_5](./gen_ai_3.ipynb) directory. The notebook demonstrates practical steps for building a simple text classification model using Keras, and introduces sentiment analysis using the IMDB dataset.

---

## Table of Contents

1. [Text Tokenization and Sequence Preparation](#1-text-tokenization-and-sequence-preparation)
    - What is Tokenization?
    - Example: Tokenizer in Keras
    - Converting Texts to Sequences
    - Padding Sequences
2. [Label and Vocabulary Preparation](#2-label-and-vocabulary-preparation)
    - Label Encoding
    - Vocabulary Size Calculation
3. [Neural Network Model for Text Classification](#3-neural-network-model-for-text-classification)
    - Model Architecture
    - Embedding Layer
    - Model Compilation and Summary
4. [Model Training and Evaluation](#4-model-training-and-evaluation)
    - Fitting the Model
    - Training Output Example
5. [Prediction on New Text](#5-prediction-on-new-text)
    - Example: Predicting Topic of a New Sentence
    - Creating a Prediction Function
6. [IMDB Sentiment Prediction (Introduction)](#6-imdb-sentiment-prediction-introduction)
    - Loading the Dataset
    - Exploring the IMDB Dataset
    - Accessing the Word Index
7. [Review Checklist](#7-review-checklist)

---

## 1. Text Tokenization and Sequence Preparation

### What is Tokenization?

Tokenization is the process of splitting text into smaller pieces (tokens), such as words or subwords, and mapping them to unique integers so they can be processed by machine learning models.

### Example: Tokenizer in Keras

```python
from tensorflow.keras.preprocessing.text import Tokenizer

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

tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
print(tokenizer.word_index)
```

**Output:**
```
{'cricket': 1, 'chess': 2, 'is': 3, 'i': 4, ...}
```

### Converting Texts to Sequences

Each word is replaced by its corresponding integer from the word index.

```python
sequences = tokenizer.texts_to_sequences(texts)
print(sequences)
```

**Output:**
```
[[4, 8, 5, 9, 1], [6, 3, 5, 2], ...]
```

### Padding Sequences

Neural networks require fixed-length inputs. Padding makes all sequences the same length.

```python
from keras.utils import pad_sequences

maxlen = max(len(seq) for seq in sequences)
padded_sequences = pad_sequences(sequences, maxlen=maxlen, padding='pre')
print(padded_sequences)
```

**Output:**
```
array([[ 4,  8,  5,  9,  1],
       [ 0,  6,  3,  5,  2],
       ...])
```

---

## 2. Label and Vocabulary Preparation

### Label Encoding

Labels are converted to numpy arrays for model training.

```python
import numpy as np
labels = [0, 1, 0, 1, 0, 1, 0, 1]
labels = np.array(labels)
print(labels)
```

**Output:**
```
[0 1 0 1 0 1 0 1]
```

### Vocabulary Size Calculation

```python
vocab_size = len(tokenizer.word_index) + 1
print(vocab_size)
```

**Output:**
```
25
```
> `+1` is to accommodate the reserved 0 index for padding.

---

## 3. Neural Network Model for Text Classification

### Model Architecture

A simple Keras Sequential model is built for binary classification (cricket vs. chess).

```python
from tensorflow.keras import models, layers

embedding_dim = 8
model = models.Sequential()
model.add(layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=maxlen))
model.add(layers.Flatten())
model.add(layers.Dense(8, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()
```

**Explanation:**
- **Embedding Layer:** Converts words into dense vectors of fixed size (`embedding_dim`).
- **Flatten:** Converts the 2D embedding output to 1D.
- **Dense (8, relu):** Adds non-linearity.
- **Dense (1, sigmoid):** Outputs probability for binary classification.

**Model Summary Output (abridged):**
```
Layer (type)         Output Shape     Param #
=================================================
embedding (Embedding) (None, 5, 8)   200
flatten (Flatten)     (None, 40)      0
dense (Dense)         (None, 8)       328
dense_1 (Dense)       (None, 1)       9
=================================================
Total params: 537
```

---

## 4. Model Training and Evaluation

### Fitting the Model

```python
model.fit(padded_sequences, labels, epochs=30, verbose=1)
```

**Training Output Example:**
```
Epoch 1/30
1/1 [==============================] - 2s 2s/step - accuracy: 0.3750 - loss: 0.7003
...
Epoch 30/30
1/1 [==============================] - 0s 47ms/step - accuracy: 1.0000 - loss: 0.6465
```

---

## 5. Prediction on New Text

### Example: Predicting Topic of a New Sentence

```python
new_text = "The batsman scored a century"
seq = tokenizer.texts_to_sequences([new_text])
pad_seq = pad_sequences(seq, maxlen=maxlen, padding='pre')
print(int(model.predict(pad_seq) > 0.5))
```

**Output:**
```
1
```
> `1` might correspond to "chess" or "cricket", depending on your label encoding.

### Creating a Prediction Function

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

## 6. IMDB Sentiment Prediction (Introduction)

### Loading the Dataset

The IMDB dataset is a standard benchmark for sentiment analysis (positive/negative movie reviews).

```python
from tensorflow.keras.datasets import imdb

(xtrain, ytrain), (xtest, ytest) = imdb.load_data()
```

### Exploring the IMDB Dataset

```python
print(xtrain.shape)   # (25000,)
print(xtest.shape)    # (25000,)
print(ytrain.shape)   # (25000,)
print(ytest.shape)    # (25000,)
print(len(xtrain[0])) # Length of first review (number of tokens)
```

### Accessing the Word Index

```python
word_index = imdb.get_word_index()
print(list(word_index.items())[:10])
```

**Output:**
```
[('fawn', 34701), ('tsukino', 52006), ('nunnery', 52007), ...]
```

---

## 7. Review Checklist

- [x] **Text Tokenization and Sequence Preparation**: Explained with Keras code and outputs
- [x] **Label and Vocabulary Preparation**: Shown how to encode labels and compute vocab size
- [x] **Neural Network Model for Text Classification**: Model structure and summary included
- [x] **Model Training and Evaluation**: Example training output and explanation
- [x] **Prediction on New Text**: Examples and function for prediction
- [x] **IMDB Sentiment Prediction (Introduction)**: Dataset loading, exploration, and word index access

---

## Summary

This document has broken down the entire `gen_ai_3.ipynb` notebook into its core educational and practical components, providing explanations, code snippets, and expected outputs. You should now have a clear understanding of how to preprocess text, build a neural network for text classification, and get started with sentiment analysis using real-world datasets.
