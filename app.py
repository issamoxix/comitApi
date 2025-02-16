from fastapi import FastAPI
from pydantic import BaseModel
import logging

from services import ai


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[],
)


class request(BaseModel):
    code: str


app = FastAPI()


@app.post("/")
def generate_message(request: request, comitId: str | None = None):
    if len(request.code) < 10:
        return {"message": "Code too short"}
    response = ai.get_message(request.code)
    return {"message": response}

@app.get("/version")
def version():
    return {"version": "0.2"}