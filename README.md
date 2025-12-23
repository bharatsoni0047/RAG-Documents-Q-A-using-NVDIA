# RAG-Documents-Q-A-using-NVIDIA

## NVIDIA API with DeepSeek-V3.2 – Live Thinking (Reasoning) Streaming Example

A lightweight Python script that demonstrates how to use the **NVIDIA NIM API** to interact with the **DeepSeek-V3.2** model in **thinking mode**. This mode streams the model's internal step-by-step reasoning in real time before delivering the final answer – perfect for observing chain-of-thought behavior live.

### Features
- Real-time streaming of both reasoning steps and final response
- Uses official OpenAI-compatible NVIDIA endpoint
- Simple, clean, and ready-to-run

### Requirements
- Python 3.7+
- OpenAI Python library  
  ```bash
  pip install openai
Getting Your NVIDIA API Key

Visit https://build.nvidia.com
Sign in or create a free account
Search for and select the model: deepseek-ai/deepseek-v3.2
Click Generate API Key
Copy the key (free tier provides generous credits for testing)

Setup & Usage

Set your API key as an environment variable:Bashexport NVIDIA_API_KEY="your_api_key_here"
Save the script as deepseek_thinking_stream.py
Edit the prompt inside the messages list with your question
Run the script:Bashpython deepseek_thinking_stream.py

You’ll see the model’s reasoning steps printed first (as they stream), followed seamlessly by the final answer.
Important Notes

The special parameter thinking: True enables the visible chain-of-thought/reasoning output
Reasoning tokens appear before regular content tokens in the stream
Always keep your API key secure and never commit it to version control
Free tier has usage limits – sufficient for experimentation and small projects

Example Use Cases

Debugging complex prompts
Educational demos of LLM reasoning
Building transparent AI applications
Prototyping RAG systems with visible thought processes

Enjoy watching DeepSeek-V3.2 think step-by-step in real time! 🚀
