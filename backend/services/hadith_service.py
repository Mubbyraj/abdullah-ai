import json
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


HADITH_FILE = os.path.join(
    BASE_DIR,
    "islamic_sources",
    "hadith.json"
)


def load_hadith():

    with open(HADITH_FILE, "r") as file:
        return json.load(file)



def search_hadith(keyword):

    hadith = load_hadith()

    results = []

    for item in hadith:

        text = item.get("text", "")

        if keyword.lower() in text.lower():
            results.append(item)

    return results