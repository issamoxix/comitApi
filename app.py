from fastapi import FastAPI
from pydantic import BaseModel

from services import ai


class request(BaseModel):
    code: str


app = FastAPI()


@app.post("/")
def generate_message(request: request):
    if len(request.code) < 10:
        return {"message": "Code too short"}
    response = ai.get_message(request.code)
    return {"message": response}
