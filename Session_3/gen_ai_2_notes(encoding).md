# Tokenization & Text Encoding in NLP

---

## 📌 What is Tokenization?

**Tokenization** is the process of splitting a sentence into smaller units called **tokens** (usually words or subwords).

**Example:**
- Sentence: `"AI is the future"`
- Tokens: `['AI', 'is', 'the', 'future']`

---

## 📌 Why Do We Need Text Encoding?

Machine learning models can’t work directly with text. We must **convert text into numbers**. That’s where text encoding techniques like:
- Bag of Words (BoW)
- TF-IDF
- Word Embeddings

come into play.

---

## 🔢 1. Bag of Words (BoW) Encoding

### ✍️ Example Sentences:

- d₁: `"I am a good Cricket player"` → label = 1  
- d₂: `"Rajiv is a bad Chess player"` → label = 0

### 🔠 Vocabulary from both sentences:
`['I', 'am', 'a', 'good', 'Cricket', 'player', 'Rajiv', 'is', 'bad', 'Chess']`

### 🧮 BoW Representation (Binary Encoding):

| Token  | I | am | a | good | Cricket | player | Rajiv | is | bad | Chess | Label |
|--------|---|----|---|------|---------|--------|-------|----|-----|-------|-------|
| d₁     | 1 | 1  | 1 | 1    | 1       | 1      | 0     | 0  | 0   | 0     | 1     |
| d₂     | 0 | 0  | 1 | 0    | 0       | 1      | 1     | 1  | 1   | 1     | 0     |

📌 **Each row becomes a feature vector for machine learning.**

---

### 🧑‍💻 BoW Code Example (Manual)

```python
from sklearn.feature_extraction.text import CountVectorizer

docs = [
    "I am a good Cricket player",
    "Rajiv is a bad Chess player"
]

vectorizer = CountVectorizer(binary=True)
bow_matrix = vectorizer.fit_transform(docs)

import pandas as pd
pd.DataFrame(bow_matrix.toarray(), columns=vectorizer.get_feature_names_out())
```

---

## 📊 2. TF-IDF Encoding

**TF-IDF (Term Frequency - Inverse Document Frequency)** is a more refined way to encode text:
- Gives higher weight to unique and important words in a document.
- Down-weights common words (like “is”, “a”, etc.).

### ✍️ TF-IDF Code Example:

```python
from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    "AI is the future",
    "AI and ML are the future",
    "Physics is really interesting thing",
    "I am interested in concepts of physics"
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(docs)

import pandas as pd
pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
```

### 📌 Output Table Sample:

|        | ai   | am   | and  | concepts | future | ... |
|--------|------|------|------|----------|--------|-----|
| Doc 1  | 0.70 | 0    | 0    | 0        | 0.70   | ... |
| Doc 2  | 0.50 | 0    | 0.50 | 0        | 0.50   | ... |
| ...    | ...  | ...  | ...  | ...      | ...    | ... |

---

## 🧠 Key Differences: BoW vs TF-IDF

| Feature         | BoW                    | TF-IDF                            |
|-----------------|-----------------------|-----------------------------------|
| Simplicity      | Very simple           | More sophisticated                |
| Word Weight     | Binary/Count (1 or n) | Based on term importance (float)  |
| Common Words    | Equal importance      | De-emphasized                     |
| Uniqueness      | Ignored               | Boosted                           |

---

## ✅ Summary

| Step             | Description                              |
|------------------|------------------------------------------|
| Tokenization     | Splits text into words                   |
| Integer Encoding | Converts words into unique IDs            |
| BoW              | Simple presence/absence or count of words |
| TF-IDF           | Weighted score showing word importance    |
| Output           | Numerical vectors for ML/DL models        |

---

# Integer Encoding (Word Index Encoding) in NLP

## ✅ What is Integer Encoding?

Integer Encoding is a foundational technique in Natural Language Processing (NLP) where each unique word in a dataset is assigned a unique integer ID.

---

### 📌 Purpose

To convert text into numerical format that can be understood and processed by machine learning or deep learning models.

---

## 💬 Example Input

```python
texts = [
    "Generative AI is intresting",
    "AI is tranforming the world",
    "I want to know about AI more"
]
```
These are raw text sentences — in natural language.

---

## 🧠 Step-by-Step Explanation

### 🔹 Step 1: Initialize and Fit the Tokenizer

```python
from tensorflow.keras.preprocessing.text import Tokenizer

tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
```

#### What happens here?

- The tokenizer scans all three sentences.
- Builds a word frequency dictionary.
- Assigns unique integers to each word based on frequency.

#### 🔍 Word Index Generated

```python
print(tokenizer.word_index)
```
**Output:**
```python
{
  'ai': 1, 'is': 2, 'generative': 3, 'intresting': 4,
  'tranforming': 5, 'the': 6, 'world': 7, 'i': 8,
  'want': 9, 'to': 10, 'know': 11, 'about': 12, 'more': 13
}
```
> 🧠 Note: 'ai' is the most frequent word → assigned 1, 'more' is least frequent → assigned 13

---

### 🔹 Step 2: Convert Texts to Integer Sequences

```python
sequences = tokenizer.texts_to_sequences(texts)
print(sequences)
```

**Output:**
```python
[[3, 1, 2, 4], [1, 2, 5, 6, 7], [8, 9, 10, 11, 12, 1, 13]]
```

| Original Sentence                | Integer Sequence            |
| -------------------------------- | -------------------------- |
| "Generative AI is intresting"    | [3, 1, 2, 4]               |
| "AI is tranforming the world"    | [1, 2, 5, 6, 7]            |
| "I want to know about AI more"   | [8, 9, 10, 11, 12, 1, 13]  |

✅ This numerical format is model-ready for neural networks.

---

### 🔹 Step 3: Padding the Sequences

```python
from keras.utils import pad_sequences
padded_sequences = pad_sequences(sequences, padding='post')
```

#### 📌 Why Padding?
Neural networks require inputs of the same length. So shorter sequences are padded with 0s.

**Output:**
```python
array([
  [ 3,  1,  2,  4,  0,  0,  0],
  [ 1,  2,  5,  6,  7,  0,  0],
  [ 8,  9, 10, 11, 12,  1, 13]
])
```
> 🧠 This makes all input vectors uniform in shape.

---

## ✅ What Is This Technique Called?

👉 **Integer Encoding** (also called Word Indexing)
- NOT one-hot encoding
- NOT Bag of Words
- Used as input for embedding layers or RNN-based models

---

## 🧠 When & Why Use Integer Encoding?

| Use Case                     | Reason                                    |
| ---------------------------- | ----------------------------------------- |
| Embedding Layer Input        | Embedding layers require integer inputs   |
| Preprocessing before LSTM/GRU| RNNs process sequences, not raw text      |
| Sequence Classification Tasks| Like sentiment analysis, intent detection |
| Token-based Generative AI    | Before feeding tokens to encoder/decoder layers in transformers |

---

## ✅ Real-Life Example: Input to an Embedding Layer

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Flatten, Dense

model = Sequential()
model.add(Embedding(input_dim=14, output_dim=8, input_length=7))  # 14 words, output vectors of size 8
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy')
model.summary()
```

---

## 🔚 Summary

| Concept           | Explanation                                         |
| ----------------- | -------------------------------------------------- |
| Tokenization      | Splitting text into words                          |
| Integer Encoding  | Assigning each word a unique ID                    |
| Sequence Encoding | Representing text as a sequence of integers        |
| Padding           | Making all sequences the same length               |
| Use in AI Models  | Required for embedding, RNN, LSTM, or transformer inputs |

## 🚀 What’s Next?

Once text is encoded:
- You can use these vectors for classification, clustering, or embedding into neural networks.
- You can move on to word embeddings like **Word2Vec**, **GloVe**, or contextual models like **BERT**.
