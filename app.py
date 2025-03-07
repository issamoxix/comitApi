from fastapi import FastAPI
from pydantic import BaseModel
import logging
import os

import controllers
from services.ai import live_agent_response, CONTEXT


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[],
)


class request(BaseModel):
    code: str


class BranchNameRequest(BaseModel):
    context: str


class AgentRequest(BaseModel):
    prompt: str


class LiveRequest(BaseModel):
    prompt: str

VERSION = os.getenv("VERSION")

app = FastAPI()


@app.post("/")
def generate_message(request: request, comitId: str | None = None):
    if len(request.code) < 10:
        return {"message": "Code too short"}
    response = controllers.commit_message(request.code, comitId)
    return response


@app.post("/branch")
def generate_branch_name(request: BranchNameRequest, comitId: str | None = None):
    response = controllers.branch_names(request.context, comitId)
    return response


@app.post("/agent")
def generate_agent_message(agent_request: AgentRequest, comitId: str | None = None):
    response = controllers.agent(agent_request.prompt, comitId)
    return response


@app.post("/live")
def live_agent(request: LiveRequest, comitId: str | None = None):
    response = live_agent_response(request.prompt, comitId)
    return {"prompt": response}

@app.delete("/reset")
def reset(comitId: str | None = None):
    del CONTEXT[comitId]
    return {"message": "Reset"}


@app.get("/version")
def version():
    return {"version": VERSION}
