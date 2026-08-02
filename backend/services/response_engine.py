from services.search_engine import search_knowledge
from services.llm_engine import ask_llm


def generate_answer(question):

    results = search_knowledge(question)


    context = ""

    sources = []


    for item in results:

        context += str(item["content"])
        context += "\n\n"

        sources.append(item["source"])


    answer = ask_llm(
        context,
        question
    )


    return {
        "answer": answer,
        "sources": list(set(sources))
    }