# Introduction to Transformers in NLP with Practical Examples

This document explains how to use the Hugging Face Transformers library for three core NLP tasks:
- Text Classification (Sentiment Analysis)
- Machine Translation
- Text Summarization

Each section includes explanations, sample code, and expected output to help you understand how these models work in practice.

---

## 1. Text Classification using BERT

**What is it?**  
Text classification allows us to assign categories or labels to text. Sentiment analysis (detecting if a text is positive or negative) is a common example. BERT and its variants are state-of-the-art models for such tasks.

### Step-by-Step Example

#### 1.1. Install Transformers

```python
!pip install transformers
```
This command installs the `transformers` package, which provides easy access to pre-trained NLP models.

#### 1.2. Load a Pre-trained Sentiment Classifier

```python
from transformers import pipeline
classifier = pipeline('sentiment-analysis')
```
- `pipeline('sentiment-analysis')` loads a default sentiment analysis model (usually a version of BERT or DistilBERT).
- The model is automatically downloaded if not present.

#### 1.3. Run Sentiment Analysis

```python
texts = ["I like transformers!", "Sometimes Machine learning models behaves terrible"]
results = classifier(texts)
```
- The `classifier` takes a list of sentences and returns a list of results, each with a label (`POSITIVE` or `NEGATIVE`) and a confidence score.

#### 1.4. Display Results

```python
for text, result in zip(texts, results):
    print(f"'{text}' => {result['label']} ({result['score']:.2f})")
```
**Output:**
```
'I like transformers!' => POSITIVE (1.00)
'Sometimes Machine learning models behaves terrible' => NEGATIVE (1.00)
```
**Explanation:**  
The first sentence is classified as positive with high confidence. The second is negative, as it expresses dissatisfaction.

---

## 2. Machine Translation

**What is it?**  
Machine translation automatically converts text from one language to another using deep learning models.

### Example: English to Hindi Translation

#### 2.1. Load a Translation Pipeline

```python
translator = pipeline("translation_en_to_hi", model="Helsinki-NLP/opus-mt-en-hi")
```
- This loads a pre-trained model for English-to-Hindi translation from Hugging Face's Model Hub.

#### 2.2. Translate a Sentence

```python
output = translator("Roses are red and sky is blue", max_length=10)
print(output[0]['translation_text'])
```
**Output:**
```
रोज़ लाल हैं और आकाश नीला है
```
**Explanation:**  
The English sentence is accurately translated to Hindi.

---

## 3. Text Summarization

**What is it?**  
Text summarization condenses a long piece of text into a shorter version while retaining the main ideas.

### Example

#### 3.1. Load a Summarization Pipeline

```python
from transformers import pipeline
summarizer = pipeline("summarization")
```
- This loads a default summarization model (e.g., DistilBART or BART).

#### 3.2. Summarize Text

```python
text = """
Transformers have revolutionized the field of NLP by introducing self-attention and multi-head attention mechanisms.
They have replaced older models like RNNs and LSTMs in tasks like translation, summarization, and language modelling.
"""
summary = summarizer(text, max_length=50, min_length=20, do_sample=False)
print("Summary:", summary[0]['summary_text'])
```
**Output:**
```
Summary: Transformers have replaced older models like RNNs and LSTMs in tasks like translation, summarization, and language modelling.
```
**Explanation:**  
The summarizer condenses the given text, focusing on the main point: transformers replacing older NLP models.

#### 3.3. Using Different Summarization Models

You can specify different models for summarization, such as T5 or BART:

```python
# Using Google T5
summarizer = pipeline("summarization", model="google-t5/t5-base", tokenizer="google-t5/t5-base", framework="tf")

# Using Facebook BART Large CNN
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
```
**Why use different models?**  
Different models may provide different styles or qualities of summaries. Try a few to see which works best for your data.

---

## Key Takeaways

- **Transformers** are powerful deep learning models that have transformed NLP tasks such as classification, translation, and summarization.
- **Hugging Face Transformers** makes it easy to use these models with a high-level pipeline API.
- You can quickly try out state-of-the-art models for various languages and tasks, often with a single line of code.

---

## References

- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers/index)
- [Transformers Model Hub](https://huggingface.co/models)
