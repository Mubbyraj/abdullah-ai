from fastapi import FastAPI
from services.ai_engine import ask_abdullah

app = FastAPI(
    title="Abdullah AI",
    description="Islamic Knowledge Assistant",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Abdullah AI is running"
    }


@app.post("/chat")
def chat(question: str):

    answer = ask_abdullah(question)

    return {
        "question": question,
        "answer": answer
    }