from services.quran_service import search_quran


def generate_answer(question):

    results = search_quran(question)


    if results:

        return {
            "source": "Quran",
            "answer": results
        }


    return {
        "source": "Abdullah AI",
        "answer":
        "I could not find a direct source. Please consult qualified scholars for detailed rulings."
    }