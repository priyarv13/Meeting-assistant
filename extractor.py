# extractor.py

import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("TOGETHER_API_KEY")
openai.api_base = "https://api.together.xyz/v1"

def extract_action_items(transcript):
    prompt = f"""
    Extract all action items from this transcript.

    Return the result strictly in JSON array format like:
    [
      {{
        "name": "Person Name",
        "task": "Task description",
        "deadline": "if mentioned"
      }},
      ...
    ]

    Transcript:
    {transcript}
    """
    try:
        response = openai.ChatCompletion.create(
            model="meta-llama/Llama-3-8b-chat-hf",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"⚠️ LLM error: {e}"
