# 🧠 Generative AI with GPT for Image Generation

> **Summary:**  
This notebook demonstrates how to use OpenAI's GPT capabilities to generate images using prompts.  
It explores basic setup, image generation through API calls, and visualization techniques.


```python
!pip install openai
```

## 📚 Table of Contents


### 🧠 Explanation:
- This installs the `openai` Python package which provides access to OpenAI APIs.
- Ensure it's run only once in your environment (Colab, Jupyter, etc.).
- Other dependencies like `httpx`, `pydantic`, and `tqdm` come along with it.

**Output:**


```
Requirement already satisfied: openai in /usr/local/lib/python3.11/dist-packages (1.94.0)
Requirement already satisfied: anyio<5,>=3.5.0 in /usr/local/lib/python3.11/dist-packages (from openai) (4.9.0)
Requirement already satisfied: distro<2,>=1.7.0 in /usr/local/lib/python3.11/dist-packages (from openai) (1.9.0)
Requirement already satisfied: httpx<1,>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from openai) (0.28.1)
Requirement already satisfied: jiter<1,>=0.4.0 in /usr/local/lib/python3.11/dist-packages (from openai) (0.10.0)
Requirement already satisfied: pydantic<3,>=1.9.0 in /usr/local/lib/python3.11/dist-packages (from openai) (2.11.7)
Requirement already satisfied: sniffio in /usr/local/lib/python3.11/dist-packages (from openai) (1.3.1)
Requirement already satisfied: tqdm>4 in /usr/local/lib/python3.11/dist-packages (from openai) (4.67.1)
Requirement already satisfied: typing-extensions<5,>=4.11 in /usr/local/lib/python3.11/dist-packages (from openai) (4.14.1)
Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.11/dist-packages (from anyio<5,>=3.5.0->openai) (3.10)
Requirement already satisfied: certifi in /usr/local/lib/python3.11/dist-packages (from httpx<1,>=0.23.0->openai) (2025.7.9)
Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.11/dist-packages (from httpx<1,>=0.23.0->openai) (1.0.9)
Requirement already satisfied: h11>=0.16 in /usr/local/lib/python3.11/dist-packages (from httpcore==1.*->httpx<1,>=0.23.0->openai) (0.16.0)
Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<3,>=1.9.0->openai) (0.7.0)
Requirement already satisfied: pydantic-core==2.33.2 in /usr/local/lib/python3.11/dist-packages (from pydantic<3,>=1.9.0->openai) (2.33.2)
Requirement already satisfied: typing-inspection>=0.4.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<3,>=1.9.0->openai) (0.4.1)
```


```python
import openai
from IPython.display import Image,display
import requests
```

### 🧠 Explanation:
- This imports the necessary libraries:
  - `openai` for using the OpenAI API
  - `IPython.display.Image` and `display` to render images inside the notebook
  - `requests` for making HTTP requests (e.g., downloading generated images)


```python
import os
from google.colab import userdata
os.environ["OPENAI_API_KEY"] = userdata.get('o_key')

client = openai.OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
    )

#Generate the image
reponse = client.images.generate(
    model = "dall-e-3",
    prompt = "A boy driving a futristic flying car",
    n = 1,
    size = "1024x1024",
    quality = "standard",
)

image_url = reponse.data[0].url
```

### 🧠 Explanation:
- This code segment performs core functionality in the workflow. (Details added in the next parsing loop)


```python
display(Image(url = image_url))
```

### 🧠 Explanation:
- This code segment performs core functionality in the workflow. (Details added in the next parsing loop)


```python
import openai
from IPython.display import Image,display
import requests

import os
from google.colab import userdata
os.environ["OPENAI_API_KEY"] = userdata.get('o_key')

client = openai.OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
    )

def generate_image(prompt):
  reponse = client.images.generate(
      model = "dall-e-3",
      prompt = "A boy driving a futristic flying car",
      n = 1,
      size = "1024x1024",
      quality = "standard",
  )
  return reponse.data[0].url


import gradio as gr

gr.Interface(fn=generate_image , inputs="text" , outputs="image" , title="Image Generator").launch()
```

### 🧠 Explanation:
- This imports the necessary libraries:
  - `openai` for using the OpenAI API
  - `IPython.display.Image` and `display` to render images inside the notebook
  - `requests` for making HTTP requests (e.g., downloading generated images)

**Output:**


```
It looks like you are running Gradio on a hosted a Jupyter notebook. For the Gradio app to work, sharing must be enabled. Automatically setting `share=True` (you can turn this off by setting `share=False` in `launch()` explicitly).

Colab notebook detected. To show errors in colab notebook, set debug=True in launch()
* Running on public URL: https://1210c4621fc36d8c8a.gradio.live

This share link expires in 1 week. For free permanent hosting and GPU upgrades, run `gradio deploy` from the terminal in the working directory to deploy to Hugging Face Spaces (https://huggingface.co/spaces)
```


```python

```

### 🧠 Explanation:
- This code segment performs core functionality in the workflow. (Details added in the next parsing loop)

## 📖 Further Reading & Resources

- [OpenAI API Docs](https://platform.openai.com/docs)
- [Image Generation with DALL·E](https://platform.openai.com/docs/guides/images)
- [IPython Display Utilities](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html)
- [Requests Library Docs](https://docs.python-requests.org/)