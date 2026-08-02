from services.search_engine import search_knowledge
import ast


def clean_content(content):

    # Convert string dictionary into real dictionary
    if isinstance(content, str):

        try:
            content = ast.literal_eval(content)

        except:
            return content


    if not isinstance(content, dict):
        return str(content)


    text_parts = []


    if "text" in content:
        text_parts.append(content["text"])

    if "ruling" in content:
        text_parts.append(content["ruling"])

    if "commentary" in content:
        text_parts.append(content["commentary"])


    return " ".join(text_parts)



def generate_answer(question):

    results = search_knowledge(question)


    if not results:
        return {
            "answer": "I could not find relevant Islamic information.",
            "sources": []
        }


    answer = """
Assalamu Alaikum.

Here is what Abdullah AI found from the Islamic knowledge sources:

"""


    sources = []


    for item in results:

        cleaned = clean_content(item["content"])

        answer += "• " + cleaned + "\n\n"

        sources.append(item["source"])



    answer += """
Abdullah AI reminder:

This response is generated from the provided Islamic knowledge database.
For detailed personal rulings and individual situations, please consult qualified scholars.
"""


    return {
        "answer": answer.strip(),
        "sources": list(set(sources))
    }