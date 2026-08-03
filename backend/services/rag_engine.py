import ast

from services.search_engine import search_knowledge
from services.llm_engine import ask_llm
from services.citation_engine import format_citations
from services.validator import validate_answer



def extract_text(doc):

    if isinstance(doc, dict):

        content = doc.get("content")

        if content:

            try:
                parsed = ast.literal_eval(content)

                if isinstance(parsed, dict):

                    return {
                        "source": doc.get("source"),
                        "text": parsed.get("text", content),
                        "topic": parsed.get("topic")
                    }

            except Exception:

                return {
                    "source": doc.get("source"),
                    "text": content
                }


        if "text" in doc:

            return {
                "source": doc.get("source"),
                "text": doc["text"]
            }


    return {
        "text": str(doc)
    }



def generate_answer(question):

    documents = search_knowledge(
        question,
        top_k=3
    )


    context_parts = []


    for doc in documents:

        extracted = extract_text(doc)


        source = extracted.get(
            "source",
            "unknown"
        )

        topic = extracted.get(
            "topic",
            "unknown"
        )

        text = extracted.get(
            "text",
            ""
        )


        context_parts.append(
            f"""
SOURCE FILE:
{source}

TOPIC:
{topic}

CONTENT:
{text}
"""
        )


    context = "\n\n-----------------\n\n".join(
        context_parts
    )


    answer = ask_llm(
        context,
        question
    )


    # Check for hallucination
    answer = validate_answer(
        answer,
        context
    )


    citations = format_citations(
        documents
    )


    return answer + "\n\n" + citations