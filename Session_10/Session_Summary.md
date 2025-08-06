The provided document is a summary of a meeting held on August 5, 2025, titled "Generative & Agentic AI - 22 July." The primary goal of the session was to build a RAG-like application for question answering from PDF data.

Here's a breakdown of the key topics covered:

  * **Previous Session Review and Current Goal:** AI Council reviewed transformer models and set the current session's objective: creating an application to answer questions from PDF data, similar to a RAG application.
  * **RAG Application Approaches:** Two RAG approaches were explained:
      * **Keyword Search:** Cheaper, no LLM involved, matches keywords from queries to documents.
      * **Semantic Search:** Understands the meaning of queries, requires an LLM, and is more expensive.
  * **Common Development Steps:** The common steps for both keyword and semantic search RAG applications were outlined:
      * Accessing and reading documents (using PyPDF2).
      * Cleaning extracted text data (removing white spaces, newlines, non-ASCII characters with regular expressions).
      * Splitting the document into multiple sections for efficient processing.
  * **Keyword Search Functionality:** AI Council demonstrated a keyword search system that splits a user query into individual keywords, converts them to lowercase, and then searches for matches within section titles and content. The system tracks "hits" to identify the best match.
  * **Keyword Search vs. LLM Models:** A distinction was made between keyword search (direct copy-paste) and LLM models (which can generate, summarize, and transform output). It was noted that keyword search was used before LLMs were prevalent. LLMs convert queries and data into vectors for comparison using cosine similarity.
  * **Importance and Future Steps:** The importance of understanding keyword search as a foundational step for future semantic search was emphasized. The next class will focus on improving the system with semantic search and LLM-powered applications.
