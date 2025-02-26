from services import ai
import json


def commit_message(code: str, comitId: str | None = None):
    response = ai.get_message(code)
    try:
        response = json.loads(response.replace("'", '"'))
    except json.JSONDecodeError:
        print("Invalid JSON")
        response = [""]
    return {"message": response}
