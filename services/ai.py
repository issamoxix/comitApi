from openai import OpenAI
from collections import defaultdict
import os

CONTEXT = defaultdict(list)
PROMPT = os.getenv("PROMPT")

def get_message(code: str):
    client = OpenAI()
    messages = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": PROMPT,
                }
            ],
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": code,
                }
            ],
        },
    ]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        response_format={"type": "text"},
        temperature=1,
        max_completion_tokens=11585,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response.choices[0].message.content
