from services import ai
def agent(prompt: str, comitId: str | None = None):
    response = ai.get_agent_response(prompt)
    return {"prompt": response}