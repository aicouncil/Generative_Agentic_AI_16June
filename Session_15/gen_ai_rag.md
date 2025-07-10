# Retrieval Augmented Generation (RAG) with GPT: Concepts, Implementation, and Examples

This document provides a detailed explanation of Retrieval Augmented Generation (RAG) using GPT models, including the vector store concept, retrieval mechanisms, and a step-by-step implementation using Python, LangChain, and FAISS. Code snippets and practical examples are included for clarity.

---

## 1. What is Retrieval Augmented Generation (RAG)?

**RAG** is a technique where a language model (like GPT) is enhanced by retrieving relevant context from a knowledge base before generating an answer. This approach combines the strengths of information retrieval and generative AI, resulting in more accurate and contextually relevant responses.

### **How RAG Works:**

1. **Retrieve:** Fetch relevant documents or data chunks from a knowledge source based on the user query.
2. **Augment:** Feed these retrieved chunks as additional context to the language model.
3. **Generate:** The language model (e.g., GPT) generates an answer, leveraging both the retrieved data and its own knowledge.

---

## 2. Key Concepts

### **a. Vector Store**

A vector store is a special type of database designed for efficient similarity search. It enables fast retrieval of text chunks that are semantically close to a query.

- **Embedding:** Each chunk of text is converted to a vector using an embedding model (e.g., OpenAIEmbeddings).
- **Storage:** Vectors are stored in a database like FAISS.
- **Search:** When a query is made, it is also embedded as a vector. The vector store then finds the most similar stored vectors (i.e., text chunks).

#### **Example:**

Suppose you have a PDF manual split into paragraphs:
- Convert each paragraph into a vector.
- Store all vectors in FAISS.
- For a user question, convert it to a vector and find the top-3 similar paragraphs.

### **b. Retrieval**

Retrieval refers to the process of identifying the most relevant information chunks from the vector store based on query similarity.

---

## 3. Implementation Steps

### **A. Install Required Libraries**

```python
!pip install pymupdf
!pip install -U langchain-community
!pip install faiss-cpu
```

### **B. Import Libraries**

```python
import os
import fitz  # PyMuPDF for PDF reading
from openai import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
```

### **C. Core Functions**

#### 1. Load Text from PDF

```python
def load_pdf_text(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        text = page.get_text()
        full_text += text
    return full_text
```

#### 2. Split Text into Chunks

```python
def split_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=100)
    docs = splitter.create_documents([text])
    return docs
```

#### 3. Create Vector Store

```python
def create_vector_store(docs):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore
```

#### 4. Set Up RAG QA Pipeline

```python
def setup_rag_qa(vectorstore):
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    llm = ChatOpenAI(temperature=0.3, model="gpt-4.1-nano")
    rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return rag_chain
```

---

## 4. Example Workflow

### **Step 1:** Load and Process PDF

```python
pdf_path = '/content/company_manual.pdf'
text = load_pdf_text(pdf_path)
docs = split_text(text)
vectorstore = create_vector_store(docs)
qa_chain = setup_rag_qa(vectorstore)
```

### **Step 2:** Ask Questions Using RAG

#### Example 1: About the Company and Product

```python
query = "Tell me about the company and product. Output expected in bullet form."
result = qa_chain(query)
print(result['result'])
```

**Sample Output:**
```
- TechNova Solutions Pvt. Ltd. is a global leader in consumer electronics.
- The company is committed to delivering innovative technology and excellent customer service.
- Headquarters are located in Bengaluru, India, with major regional offices in Singapore, Germany, and the United States.
- The company specializes in smart devices, home automation, and sustainable technology solutions.
- Its mission is to make everyday life smarter, simpler, and more connected.
- TechNova values innovation, environmental responsibility, and customer satisfaction above all else.
```

#### Example 2: Customer Support Contact Details

```python
query = "Tell me about the contact details of customer support. Output expected in bullet form."
result = qa_chain(query)
print(result['result'])
```

**Sample Output:**
```
- Phone: +91-9999999999 (Available Mon-Fri, 9 AM to 6 PM IST)
- Email: support@technova.com (Response time: within 24 hours)
- Live Chat: Available on our website and mobile app
- Help Center: https://support.technova.com
```

---

## 5. Bonus: Building a Simple RAG Assistant UI with Gradio

Below is a conceptual sketch for a Gradio app where users can upload a PDF and ask questions interactively.

```python
import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("# Rag Assistant with GPT")
    gr.Markdown("Upload a PDF, then ask your question. Powered by OpenAI + FAISS + LangChain")
    with gr.row():
        pdf_input = gr.file(label="Upload PDF")
        upload_status = gr.Textbox(label="Status")

    with gr.row():
        question_input = gr.Textbox(label="Ask a question")
        answer_output = gr.Textbox(label="Answer")

    # Event handlers would be connected here (pseudo-code)
    # pdf_input.change(fn=load_pdf_and_update_status, inputs=pdf_input, outputs=upload_status)
    # question_input.submit(fn=answer_question, inputs=question_input, outputs=answer_output)

demo.launch()
```

---

## 6. Summary Table

| **Component**            | **Purpose**                                   | **Example**                        |
|--------------------------|-----------------------------------------------|------------------------------------|
| **OpenAIEmbeddings**     | Convert text to vectors                       | Creating vector representations    |
| **FAISS**                | Fast vector-based search                      | Finding similar text chunks        |
| **TextSplitter**         | Split large text into chunks                  | Preparing data for embeddings      |
| **RetrievalQA**          | Combines retrieval and GPT answering          | End-to-end Q&A system              |
| **ChatOpenAI**           | Interface for GPT models                      | Generates final answers            |

---

## 7. Conclusion

Retrieval Augmented Generation (RAG) is a powerful technique for building intelligent Q&A systems that can leverage both structured knowledge and the reasoning abilities of modern language models. By combining vector search (FAISS), advanced embeddings (OpenAI), and generative AI (GPT), you can create efficient, accurate, and scalable solutions for a wide array of knowledge management tasks.

---

**Further Reading:**
- [FAISS Documentation](https://github.com/facebookresearch/faiss)
- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API](https://platform.openai.com/docs/)
