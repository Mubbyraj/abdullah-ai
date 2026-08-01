from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Assalamu Alaikum, I am Abdullah AI."
    }
@app.post("/chat")
def chat(question: str):
    return {
        "question": question,
        "answer": "I received your question. Abdullah AI is learning."
    }