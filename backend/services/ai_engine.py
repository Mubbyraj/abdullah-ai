from services.quran_service import search_quran
from services.hadith_service import search_hadith
from services.fiqh_service import search_fiqh


def ask_abdullah(question):

    quran = search_quran(question)

    if quran:
        return {
            "source": "Quran",
            "result": quran
        }


    hadith = search_hadith(question)

    if hadith:
        return {
            "source": "Hadith",
            "result": hadith
        }


    fiqh = search_fiqh(question)

    if fiqh:
        return {
            "source": "Fiqh",
            "result": fiqh
        }


    return {
        "source": "Abdullah AI",
        "result": "I could not find a reliable source yet."
    }