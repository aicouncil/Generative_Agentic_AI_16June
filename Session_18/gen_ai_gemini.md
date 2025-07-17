# 🧠 Generative AI with Gemini (Google Generative AI API)

> **Summary:**  
This notebook demonstrates how to use **Google’s Gemini (Generative AI)** API to generate text and images from natural language prompts using the `google-generativeai` Python SDK.  
It includes authentication, configuration, prompt submission, and output rendering for text and images.

---

## 📚 Table of Contents

- [Installing the Gemini SDK](#installing-the-gemini-sdk)
- [Importing Required Libraries](#importing-required-libraries)
- [Setting Up Google API Key](#setting-up-google-api-key)
- [Text Generation using Gemini Pro](#text-generation-using-gemini-pro)
- [Image Generation using Gemini Pro Vision](#image-generation-using-gemini-pro-vision)
- [📖 Further Reading & Resources](#-further-reading--resources)

---

## Installing the Gemini SDK

```python
!pip install google-generativeai
```

### 🧠 Explanation:
- This installs the official SDK to access **Google’s Gemini family of large language models**.
- It provides tools for text and image generation (`generativeai`).

> 💡 **Note:** If using Google Colab or Jupyter, this command should be run before importing modules.

---

## Importing Required Libraries

```python
import google.generativeai as genai
import os
```

### 🧠 Explanation:
- `google.generativeai` is the official SDK to interact with Gemini APIs.
- `os` is used to manage environment variables (like storing your API key securely).

---

## Setting Up Google API Key

```python
GOOGLE_API_KEY = "your-api-key"
genai.configure(api_key=GOOGLE_API_KEY)
```

### 🧠 Explanation:
- You must obtain an API key from [Google AI Studio](https://makersuite.google.com/app).
- `genai.configure(...)` authenticates your session so that subsequent API calls are authorized.

> 🔐 **Tip:** For production or public notebooks, store the key using environment variables or `.env` files instead of hardcoding it.

---

## Text Generation using Gemini Pro

```python
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Explain the concept of black holes in simple terms.")
print(response.text)
```

### 🧠 Explanation:
- Loads the **`gemini-pro`** text generation model (similar to GPT-4 in purpose).
- Sends a prompt (`"Explain the concept of black holes..."`) for completion.
- `response.text` extracts the generated result.

---

### 🔁 Request-Response Flow

```plaintext
[Prompt] --> [gemini-pro.generate_content()] --> [LLM Output]
```

---

### ✅ Example Output:
```
Black holes are areas in space where gravity is so strong that nothing can escape it — not even light...
```

---

## Image Generation using Gemini Pro Vision *(if included)*

```python
vision_model = genai.GenerativeModel("gemini-pro-vision")
response = vision_model.generate_content(["A futuristic city skyline at sunset"])
image_url = response.candidates[0].image_url
```

### 🧠 Explanation:
- `gemini-pro-vision` is used to generate or describe images from prompts.
- Returns candidate outputs that may include URLs or image data.
- You can render it using `IPython.display.Image(image_url)` or download it using `requests`.

---

### 🖼️ Image Generation Flow

```plaintext
[Text Prompt] --> [gemini-pro-vision.generate_content()] --> [Image or URL Output] --> [Display or Download]
```

---

## 📖 Further Reading & Resources

- [Google Generative AI Docs](https://ai.google.dev/)
- [AI Studio - Gemini Playground](https://makersuite.google.com/)
- [Gemini Model Capabilities](https://ai.google.dev/gemini)
- [Text vs. Vision Models](https://ai.google.dev/gemini-api/docs/models/gemini)
