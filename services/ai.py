from openai import OpenAI
from collections import defaultdict
import os

CONTEXT = defaultdict(list)
PROMPT = os.getenv("PROMPT")
BRANCH_PROMPT = os.getenv("BRANCH_PROMPT")
AGENT_PROMPT = os.getenv("AGENT_PROMPT")


def openai_response(messages):
    client = OpenAI()
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
    return response


def get_message(code: str):
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
    response = openai_response(messages)
    return response.choices[0].message.content


def get_branch_name(context: str):
    messages = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": BRANCH_PROMPT,
                }
            ],
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": context,
                }
            ],
        },
    ]
    response = openai_response(messages)
    return response.choices[0].message.content


def get_agent_response(prompt: str):
    messages = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": AGENT_PROMPT,
                }
            ],
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt,
                }
            ],
        },
    ]
    response = openai_response(messages)
    return response.choices[0].message.content
