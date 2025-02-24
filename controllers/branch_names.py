from services import ai
import json


def branch_names(context: str, comitId: str | None = None):
    response = ai.get_branch_name(context)
    try:
        response = json.loads(response.replace("'", '"'))
    except json.JSONDecodeError:
        print("Invalid JSON")
        response = [""]
    return {"branch": response}
