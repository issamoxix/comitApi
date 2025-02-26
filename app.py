from fastapi import FastAPI
from pydantic import BaseModel
import logging

import controllers


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[],
)


class request(BaseModel):
    code: str


class BranchNameRequest(BaseModel):
    context: str


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


@app.get("/version")
def version():
    return {"version": "0.4"}
