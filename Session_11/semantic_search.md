# Detailed Explanations of Semantic Search Workflow

This document provides detailed explanations (with examples) of the main steps involved in building a semantic search engine using sentence embeddings, as implemented in the `gen_ai_7(semantic_search).ipynb` notebook. It also covers the differences between traditional (keyword) search and semantic search.

---

## 1. Installing Required Dependencies (`sentence-transformers` and `PyPDF2`)

To enable semantic search, we need two main Python libraries:

- **sentence-transformers**: For generating semantic embeddings of sentences or texts using pre-trained models.
- **PyPDF2**: For extracting text from PDF files.

**Installation Example:**
```python
!pip install -q sentence-transformers
!pip install PyPDF2
```

---

## 2. Extracting Text Data from a PDF File Using PyPDF2

PyPDF2 allows you to programmatically read and extract text from PDF documents.

**Example:**
```python
import PyPDF2

def extract_data_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdfreader = PyPDF2.PdfReader(file)
        full_text = ''
        for page in pdfreader.pages:
            full_text += page.extract_text()
    return full_text

extracted_text = extract_data_from_pdf("company_manual.pdf")
print(extracted_text)
```
*This function reads every page in the PDF and concatenates their text.*

---

## 3. Cleaning and Preprocessing the Extracted Text

Raw PDF text may contain extra spaces, line breaks, or non-ASCII characters. Cleaning helps standardize the input for downstream processing.

**Example:**
```python
import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)            # Removes extra whitespace
    text = re.sub(r'[^\x00-\x7F]+', '', text)   # Removes non-ASCII characters
    return text

cleaned_text = clean_text(extracted_text)
print(cleaned_text)
```

---

## 4. Loading and Using a Pre-trained SentenceTransformer Model

The `SentenceTransformer` library provides pre-trained models for generating semantic embeddings.

**Example:**
```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
```
*This loads a lightweight yet powerful model capable of producing 384-dimensional embeddings for sentences or paragraphs.*

---

## 5. Segmenting the Document Content into Logical Sections

For efficient searching, the document is split into meaningful sections based on headers or known delimiters.

**Example:**
```python
sections = {
    "About the Company" : cleaned_text.split('About the Company')[1].split('Return Policy')[0],
    "Return Policy" : cleaned_text.split('Return Policy')[1].split('Warranty')[0],
    "Warranty" : cleaned_text.split('Warranty')[1].split('Customer Service')[0],
    "Customer Service" : cleaned_text.split('Customer Service')[1].split('Environmental Commitment')[0],
    "Environmental Commitment" : cleaned_text.split('Environmental Commitment')[1]
}
```
*Each section contains the relevant portion of the text.*

---

## 6. Creating Embeddings for Each Section and for a Given Query

We encode both the document sections and the user's query into vector representations (embeddings).

**Example:**
```python
# Encode a query
query = "How do I send the item back?"
query_embedding = model.encode([query])[0]

# Encode each section
section_embeddings = {title: model.encode([content])[0] for title, content in sections.items()}
```
*Now, each section and the query are represented as vectors in semantic space.*

---

## 7. Calculating Cosine Similarity to Identify the Most Relevant Section

Cosine similarity quantifies how similar two vectors are. The section with the highest similarity to the query is the best match.

**Example:**
```python
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

similarities = {
    title: cosine_similarity(query_embedding, emb)
    for title, emb in section_embeddings.items()
}
best_match = max(similarities, key=similarities.get)
print(f"Best Match: {best_match}")
```

---

## 8. Visualizing Similarity Scores with a Horizontal Bar Plot

A visualization helps interpret which sections are most similar to a query.

**Example:**
```python
import matplotlib.pyplot as plt

titles = list(similarities.keys())
scores = list(similarities.values())

plt.figure(figsize=(8, 4))
plt.barh(titles, scores, color='skyblue')
plt.xlabel("Cosine similarities")
plt.title("Query Similarity to Document Sections")
plt.show()
```

---

## 9. Implementing a Semantic Search Chatbot Function

A chatbot function takes a user's query and returns the most relevant section based on semantic similarity.

**Example:**
```python
def semantic_search(query, sections, model):
    query_embedding = model.encode([query])[0]
    best_match = None
    max_similarity = 0.3  # Threshold
    for section_title, content in sections.items():
        section_embedding = model.encode([content])[0]
        similarity = cosine_similarity(query_embedding, section_embedding)
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = section_title
    if best_match:
        return f"Bot: The most relevant section is: {best_match}\nHere is a brief answer:\n{sections[best_match][:500]}"
    else:
        return "Bot: I couldn't find the most relevant section."

# Usage
response = semantic_search("How do I claim warranty?", sections, model)
print(response)
```

---

## Difference Between Traditional (Keyword) Search and Semantic Search

| Aspect                | Traditional (Keyword) Search           | Semantic Search (Embedding-based)            |
|-----------------------|----------------------------------------|----------------------------------------------|
| **How it Works**      | Matches literal words/phrases          | Measures meaning/similarity in vector space  |
| **Query Example**     | Query: "return policy"                 | Query: "How can I send my product back?"     |
| **Match Example**     | Only matches text containing "return policy" | Matches text about returns even if words differ |
| **Synonyms**          | Not detected (strict word match)       | Detected (captures meaning, e.g., "refund")  |
| **Flexibility**       | Rigid (misses rephrased info)          | Flexible (captures paraphrases and concepts) |
| **False Negatives**   | High (misses semantically related info)| Low                                         |
| **Implementation**    | Regex, string match, tf-idf, etc.      | Embeddings, neural nets, cosine similarity   |

**Example:**

- **Keyword Search:**  
  - Query: "send item back"  
  - Returns sections containing exactly "send item back".
- **Semantic Search:**  
  - Query: "send item back"  
  - Returns sections about "returns", "refunds", "return policy", even if the exact phrase isn't present.

---

## Summary

This workflow enables building an intelligent search/chatbot system that understands user intent and retrieves the most relevant information, regardless of how the question is phrased, by leveraging modern NLP embeddings and semantic similarity.
