# End-to-End Notes: Basics of Generative AI & Retrieval-Augmented Generation (RAG)

This guide provides an end-to-end explanation of the foundational steps required to build a Retrieval-Augmented Generation (RAG) application using Generative AI, with detailed code examples inspired by `gen_ai_rag_basics.py`.

---

## 1. Introduction to RAG and Its Importance

**Generative AI** models (like GPT, Llama, etc.) are powerful but have a fixed knowledge cutoff and cannot access external or up-to-date information by default.

**Retrieval-Augmented Generation (RAG)** combines these models with an information retrieval component, allowing the system to fetch relevant documents or data chunks and use them for more accurate and context-aware generation.

**Use Cases:**
- Enterprise document Q&A
- Chatbots grounded on private knowledge
- Legal, healthcare, or technical document search

---

## 2. Key Steps in a RAG Pipeline

### 2.1. Document Ingestion

Documents are often in formats like PDF, DOCX, or plain text. The first step is to extract their text content.

**Example: Extracting text from PDF using PyMuPDF**

```python
import fitz  # PyMuPDF

def extract_data_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        text = page.get_text()
        full_text += text
    return full_text

# Usage
pdf_text = extract_data_from_pdf("company_manual.pdf")
print(pdf_text[:500])  # Print first 500 characters
```

---

### 2.2. Text Chunking

Large documents are split into smaller sections ("chunks") so retrieval can be more focused and relevant.

**Why Chunk?**
- Embedding models and language models have context length limits.
- Smaller chunks allow precise retrieval.

**Example: Chunking text by word count**

```python
def split_into_sentences(text, chunk_size=500):
    sentences = text.split()
    sections = []
    for i in range(0, len(sentences), chunk_size):
        section = ' '.join(sentences[i : i+chunk_size])
        sections.append(section)
    return sections

# Usage
text_chunks = split_into_sentences(pdf_text, chunk_size=100)
print(text_chunks[0])  # First chunk
```

---

### 2.3. Generating Embeddings

Each chunk is converted into a vector (embedding) using a transformer model. This allows you to compare queries and chunks for semantic similarity.

**Example: Using Sentence Transformers**

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Embed a chunk
embeddings = [model.encode(chunk) for chunk in text_chunks]

# Embed a query
query = "What is the company's return policy?"
query_embedding = model.encode(query)
```

---

### 2.4. Semantic Search (Retrieval)

Compare the query embedding to all chunk embeddings to find the most relevant sections.

**Example: Find most similar chunk**

```python
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Compute similarities
similarities = [cosine_similarity(query_embedding, emb) for emb in embeddings]

# Get the best chunk(s)
top_k = 3
top_k_indices = np.argsort(similarities)[-top_k:][::-1]
for idx in top_k_indices:
    print(f"Score: {similarities[idx]:.2f} | Chunk: {text_chunks[idx][:100]}")
```

---

### 2.5. Augmenting the Generative Model

Feed the retrieved chunk(s) as additional context to your generative model (e.g., GPT-4, Llama) for final answer generation.

**Example: Prompt Construction**

```
User Query: What is the company's return policy?

Context:
[Most relevant chunk from retrieval]

Answer:
```

---

## 3. Full Pipeline Example

```python
# 1. Extract text from PDF
pdf_text = extract_data_from_pdf("company_manual.pdf")

# 2. Split into chunks
chunks = split_into_sentences(pdf_text, chunk_size=100)

# 3. Generate embeddings for each chunk
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
chunk_embeddings = [model.encode(chunk) for chunk in chunks]

# 4. Encode the user query
query = "What is the company's return policy?"
query_emb = model.encode(query)

# 5. Find the most relevant chunk
sims = [cosine_similarity(query_emb, emb) for emb in chunk_embeddings]
best_idx = np.argmax(sims)
context = chunks[best_idx]

# 6. Construct the prompt for LLM
prompt = f"""User Query: {query}
Context: {context}
Answer:"""
# Send this prompt to your favorite LLM API!
```

---

## 4. Summary Table

| Step                  | Purpose                                   | Example Code                     |
|-----------------------|-------------------------------------------|----------------------------------|
| Document Ingestion    | Extract text from files                   | `extract_data_from_pdf()`        |
| Text Chunking         | Split text for efficient retrieval        | `split_into_sentences()`         |
| Embedding Generation  | Convert text to vectors for comparison    | `SentenceTransformer.encode()`   |
| Semantic Search       | Retrieve relevant content                 | `cosine_similarity()`            |
| Generative Augmentation | Use retrieved context for LLM responses | Prompt construction              |

---

## 5. Practical Tips

- Use chunk sizes appropriate to your LLM's context window (often 100-500 words).
- Choose embedding models that balance speed and accuracy (`MiniLM`, `all-MiniLM`, etc.).
- For production, store embeddings and perform search using vector databases (e.g., FAISS, Pinecone, Weaviate).

---

## 6. References

- [Sentence Transformers Documentation](https://www.sbert.net/)
- [PyMuPDF Documentation](https://pymupdf.readthedocs.io/)
- [Retrieval-Augmented Generation (RAG) Paper](https://arxiv.org/abs/2005.11401)
- [OpenAI Cookbook: RAG](https://cookbook.openai.com/examples/retrieval_augmented_generation)

---
