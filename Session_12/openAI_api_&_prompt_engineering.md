# Prompt Engineering with OpenAI API: Concepts and Detailed Examples

This guide covers essential prompt engineering strategies for working with large language models, using practical examples in Python with the OpenAI API.

---

## 1. Introduction to OpenAI API

Before you begin, install and import the `openai` library, and set your API key.

```python
!pip install openai
import openai
openai.__version__
```

Set up your API key (in Google Colab, you might use `userdata`):

```python
import os
from google.colab import userdata

os.environ["OPENAI_API_KEY"] = userdata.get('o_key')
```

---

## 2. Basic API Usage

Send a simple prompt to a model:

```python
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-4.1-nano",
    instructions="You are a Physics teacher",
    input="Explain three laws of motion to me"
)

print(response.output_text)
```

**Output Example:**
```
Certainly! The three laws of motion were formulated by Sir Isaac Newton...
```

---

## 3. Summarization

Ask the model to summarize long texts:

```python
long_text = """
Self-determination theory (SDT) is one of the most well established...
"""

message = [{"role": "user", "content": f"Summarize the following text: {long_text}"}]

response = client.responses.create(
    model="gpt-4.1-nano",
    input=message,
    temperature=0.7
)

print(response.output_text)
```

---

## 4. Role-Based Instructions

Define the system's persona for tailored responses.

**Example: Customer Support Agent**
```python
message = [
    {"role": "system", "content": "You are a helpful customer support agent for an e-commerce website"},
    {"role": "user", "content": "Hi, my order has not arrived. Can you help me?"}
]
response = client.responses.create(model="gpt-4.1-nano", input=message, temperature=0.7)
print(response.output_text)
```

---

## 5. Prompting Techniques

### a. Zero-Shot Prompting

Give the task directly, with no examples.

```python
message = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Translate the following English sentence into Hindi: Hello, how are you?"}
]
response = client.responses.create(model="gpt-4.1-nano", input=message)
print(response.output_text)
```

**Output:**  
`नमस्ते, आप कैसे हैं?`

---

### b. One-Shot Prompting

Provide one example of the desired behavior.

```python
message = [
    {"role": "system", "content": "You are a helpful assistant that provides examples of synonyms"},
    {"role": "user", "content": "Provide synonyms for 'happy'"},
    {"role": "assistant", "content": "joyful, cheerful"},
    {"role": "user", "content": "Provide synonyms for 'sad'"}
]
response = client.responses.create(model="gpt-4.1-nano", input=message)
print(response.output_text)
```

**Output:**  
`unhappy, sorrowful`

---

### c. Few-Shot Prompting

Give several examples to guide the model.

```python
message = [
    {"role": "system", "content": "You are a sentiment analyzer"},
    {"role": "user", "content": "I liked the food today."},
    {"role": "assistant", "content": "+Ve"},
    {"role": "user", "content": "I am travelling to Goa today"},
    {"role": "assistant", "content": "Neutral"},
    {"role": "user", "content": "It was not a good movie"}
]
response = client.responses.create(model="gpt-4.1-nano", input=message)
print(response.output_text)
```

**Output:**  
`-Ve`

---

## 6. Chain-of-Thought Prompting

Encourage the model to walk through reasoning step by step.

```python
message = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "The quick brown fox jumps over the lazy dog. If the fox is brown, what color is the dog? Let's think step by step."}
]
response = client.responses.create(model="gpt-4.1-nano", input=message)
print(response.output_text)
```

**Output (truncated):**
```
Let's analyze the statement step by step:
1. The sentence is: "The quick brown fox...
...
Answer: The dog's color is unknown based on the given information.
```

---

## 7. Role-Playing Prompting

Make the model respond in a specific character or style.

```python
message = [
    {"role": "system", "content": "You are a pirate. Repond to all requests in pirate speak"},
    {"role": "user", "content": "Tell me about weather today"}
]
response = client.responses.create(model="gpt-4.1-nano", input=message)
print(response.output_text)
```

**Output:**  
`Arrr, matey! I be seein' the skies be clear as a calm sea today...`

---

## 8. Output Formatting

### a. JSON Output

```python
message = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "List some 5 tourist places and their attractions in India in json data format"}
]
response = client.responses.create(model="gpt-4.1-nano", input=message)
print(response.output_text)
```

**Sample Output:**
```json
[
  {
    "name": "Taj Mahal",
    "location": "Agra, Uttar Pradesh",
    "attractions": [
      "Iconic white marble mausoleum",
      "Beautiful Mughal architecture",
      "Gardens and reflecting pools"
    ]
  },
  ...
]
```

### b. Markdown Output

```python
message = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "List some 5 tourist places and their attractions in India in markdown data format"}
]
response = client.responses.create(model="gpt-4.1-nano", input=message)
print(response.output_text)
```

**Sample Output:**
```markdown
# Tourist Places in India and Their Attractions

1. **Taj Mahal, Agra**
   - Iconic white marble mausoleum
   - Symbol of love and Mughal architecture
   - Beautiful Mughal gardens and reflecting pools

2. **Jaipur, Rajasthan**
   - The Amber Fort and City Palace
   - Hawa Mahal (Palace of Winds)
   - Vibrant markets and traditional Rajasthani cuisine

3. **Varanasi, Uttar Pradesh**
   - Spiritual city on the banks of the Ganges River
   - Ganga Aarti ceremony at Dashashwamedh Ghat
   - Ancient temples and narrow winding streets

4. **Goa**
   - Pristine beaches like Baga and Palolem
   - Portuguese colonial architecture
   - Vibrant nightlife and water sports

5. **Ladakh, Jammu and Kashmir**
   - Stunning Himalayan landscapes
   - Pangong Lake and Nubra Valley
   - Monasteries like Hemis and Thiksey
```

---

## Conclusion

Prompt engineering involves crafting effective instructions and examples to elicit desired behaviors from language models. Techniques like zero-shot, one-shot, few-shot, chain-of-thought, and role-based prompting, along with output formatting, help tailor responses for diverse applications.

Use these patterns as building blocks for your own use cases and keep experimenting to discover what works best for your tasks!
