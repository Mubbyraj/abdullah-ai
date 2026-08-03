import requests


OLLAMA_URL = "http://localhost:11434/api/generate"


def ask_llm(context, question):

    prompt = f"""
You are Abdullah AI.

You are an Islamic knowledge assistant using ONLY the provided database.

IMPORTANT RULES:

- Answer ONLY using information inside the SOURCES section.
- Never use your own Islamic knowledge.
- Never create Quran verses, hadith numbers, scholars, dates, or fatwas.
- If information is missing, say:
"I do not have enough information in my current Islamic knowledge database."

- Do not mention sources that are not provided.
- Do not say "according to Quran" unless Quran text exists in the sources.
- Keep answers respectful and concise.
- Use ﷺ only for Prophet Muhammad.

SOURCES:

{context}


QUESTION:

{question}


ANSWER:

"""


    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3.2:3b",
            "prompt": prompt,
            "temperature": 0,
            "stream": False
        }
    )


    return response.json()["response"]