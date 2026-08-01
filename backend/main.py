from fastapi import FastAPI
from services.ai_engine import generate_answer


app = FastAPI(
    title="Abdullah AI",
    description="Islamic AI Assistant",
    version="1.0"
)


@app.get("/")
def home():

    return {
        "message":
        "Assalamu Alaikum. Abdullah AI is running."
    }


@app.post("/chat")
def chat(question:str):

    response = generate_answer(question)

    return response