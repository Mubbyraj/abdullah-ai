import json
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


FIQH_FILE = os.path.join(
    BASE_DIR,
    "islamic_sources",
    "fiqh.json"
)



def load_fiqh():

    with open(FIQH_FILE, "r") as file:
        return json.load()



def search_fiqh(keyword):

    fiqh = load_fiqh()

    results = []

    for item in fiqh:

        if keyword.lower() in item["topic"].lower():
            results.append(item)

    return results