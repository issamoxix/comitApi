from openai import OpenAI
from collections import defaultdict
import os

CONTEXT = defaultdict(list)
PROMPT = os.getenv("PROMPT")
BRANCH_PROMPT = os.getenv("BRANCH_PROMPT")


def get_message(code: str):
    client = OpenAI()
    messages = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": PROMPT + code,
                }
            ],
        }
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


def get_branch_name(context: str):
    client = OpenAI()
    messages = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": BRANCH_PROMPT + context,
                }
            ],
        }
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
