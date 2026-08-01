from services.quran_service import search_quran
from services.hadith_service import search_hadith
from services.fiqh_service import search_fiqh

from utils.text_processing import detect_topic



def ask_abdullah(question):


    topic = detect_topic(question)


    quran = search_quran(question)

    if quran:

        return {
            "answer": quran,
            "source": "Quran",
            "topic": topic
        }


    hadith = search_hadith(question)

    if hadith:

        return {
            "answer": hadith,
            "source": "Hadith",
            "topic": topic
        }


    fiqh = search_fiqh(question)

    if fiqh:

        return {
            "answer": fiqh,
            "source": "Fiqh",
            "topic": topic
        }


    return {

        "answer":
        "I could not find a reliable source. Please consult a qualified scholar.",

        "source":
        "Abdullah AI",

        "topic":
        topic
    }