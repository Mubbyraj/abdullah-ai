import json
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

QURAN_FILE = os.path.join(
    BASE_DIR,
    "islamic_sources",
    "quran.json"
)


def load_quran():

    with open(QURAN_FILE, "r") as file:
        return json.load(file)


def search_quran(keyword):

    quran = load_quran()

    results = []

    for verse in quran:

        if keyword.lower() in verse["text"].lower():
            results.append(verse)

    return results