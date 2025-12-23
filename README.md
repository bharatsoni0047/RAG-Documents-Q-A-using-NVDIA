# RAG-Documents-Q-A-using-NVDIA

# NVIDIA API with DeepSeek-V3.2 - Live Thinking (Reasoning) Streaming Example

This is a simple Python script that uses the **NVIDIA API** (via NVIDIA NIM) to call the **DeepSeek-V3.2** model with **thinking mode** enabled, allowing you to stream and view the model's internal reasoning steps live, followed by the final response.

The key feature is that it separately prints the model's **reasoning_content** (thinking steps) as they are generated, giving you real-time insight into how the model is reasoning.

## Requirements

- Python 3.7 or higher
- OpenAI Python library: `pip install openai`

## Getting Your NVIDIA API Key

1. Go to https://build.nvidia.com
2. Sign in or create an account
3. Select the model `deepseek-ai/deepseek-v3.2`
4. Click **Generate API Key** to get your key

> Note: The free tier has limited quota, but it's sufficient for testing.

## Usage

1. Set your API key as an environment variable:

bash
export NVIDIA_API_KEY="your_api_key_here"

Save the script (e.g., as deepseek_thinking_stream.py)
Edit the messages list to add your desired prompt
Run the script:

from openai import OpenAI
client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "$NVIDIA_API_KEY"
)
completion = client.chat.completions.create(
  model="deepseek-ai/deepseek-v3.2",
  messages=[{"role":"user","content":""}],
  temperature=1,
  top_p=0.95,
  max_tokens=8192,
  extra_body={"chat_template_kwargs": {"thinking":True}},
  stream=True
)
for chunk in completion:
  if not getattr(chunk, "choices", None):
    continue
  reasoning = getattr(chunk.choices[0].delta, "reasoning_content", None)
  if reasoning:
    print(reasoning, end="")
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")
 
 
 
iska read me banao for githubNVIDIA API से DeepSeek-V3.2 मॉडल के साथ लाइव थिंकिंग (Reasoning) स्ट्रीमिंग
यह एक साधारण Python स्क्रिप्ट है जो NVIDIA API (NVIDIA NIM) का उपयोग करके DeepSeek-V3.2 मॉडल को कॉल करती है और थिंकिंग मोड (reasoning mode) को एनेबल करके स्ट्रीमिंग रिस्पॉन्स प्राप्त करती है।
इस स्क्रिप्ट की खासियत यह है कि यह मॉडल के इंटरनल reasoning content (थिंकिंग स्टेप्स) को अलग से प्रिंट करती है, और फिर फाइनल आंसर को। इससे आप लाइव देख सकते हैं कि मॉडल कैसे सोच रहा है।
आवश्यकताएँ (Requirements)

Python 3.7+
OpenAI Python लाइब्रेरी: pip install openai

API की प्राप्त करना

https://build.nvidia.com पर जाएँ।
अपना अकाउंट बनाएँ/लॉगिन करें।
"deepseek-ai/deepseek-v3.2" मॉडल को सिलेक्ट करें।
Generate API Key पर क्लिक करके अपना NVIDIA API की प्राप्त करें।

नोट: NVIDIA API फ्री टियर में लिमिटेड क्वोटा होता है, लेकिन टेस्टिंग के लिए काफी है।
उपयोग कैसे करें (Usage)

अपनी API की को एनवायरनमेंट वेरिएबल में सेट करें:

Bashexport NVIDIA_API_KEY="your_api_key_here"

स्क्रिप्ट को सेव करें (उदाहरण: deepseek_thinking_stream.py) और यूजर प्रॉम्प्ट को बदलें।
रन करें:

Bashpython deepseek_thinking_stream.py
कोड
Pythonimport os
from openai import OpenAI

clientInterrupted36 sourcesin english and 1 time copy paste readyMarkdown# NVIDIA API with DeepSeek-V3.2 - Live Thinking (Reasoning) Streaming Example

This is a simple Python script that uses the **NVIDIA API** (via NVIDIA NIM) to call the **DeepSeek-V3.2** model with **thinking mode** enabled, allowing you to stream and view the model's internal reasoning steps live, followed by the final response.

The key feature is that it separately prints the model's **reasoning_content** (thinking steps) as they are generated, giving you real-time insight into how the model is reasoning.

## Requirements

- Python 3.7 or higher
- OpenAI Python library: `pip install openai`

## Getting Your NVIDIA API Key

1. Go to https://build.nvidia.com
2. Sign in or create an account
3. Select the model `deepseek-ai/deepseek-v3.2`
4. Click **Generate API Key** to get your key

> Note: The free tier has limited quota, but it's sufficient for testing.

## Usage

1. Set your API key as an environment variable:

bash
export NVIDIA_API_KEY="your_api_key_here"

Save the script (e.g., as deepseek_thinking_stream.py)
Edit the messages list to add your desired prompt
Run the script:

Bashpython deepseek_thinking_stream.py
Code
Pythonimport os
from openai import OpenAI

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

completion = client.chat.completions.create(
    model="deepseek-ai/deepseek-v3.2",
    messages=[{"role": "user", "content": "Your prompt here"}],  # Change this prompt
    temperature=1,
    top_p=0.95,
    max_tokens=8192,
    extra_body={"chat_template_kwargs": {"thinking": True}},
    stream=True
)

for chunk in completion:
    if not getattr(chunk, "choices", None):
        continue
    reasoning = getattr(chunk.choices[0].delta, "reasoning_content", None)
    if reasoning:
        print(reasoning, end="")
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
Notes

The thinking: True flag enables the model's step-by-step reasoning output.
Reasoning content is printed as it streams, followed immediately by the final answer tokens.
Make sure your API key is correctly set in the environment — the script will fail otherwise.

Enjoy watching the model think in real time!
