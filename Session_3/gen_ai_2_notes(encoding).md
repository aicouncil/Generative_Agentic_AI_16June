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

## 🚀 What’s Next?

Once text is encoded:
- You can use these vectors for classification, clustering, or embedding into neural networks.
- You can move on to word embeddings like **Word2Vec**, **GloVe**, or contextual models like **BERT**.
