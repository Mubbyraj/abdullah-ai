import json


def search_quran(keyword):
    with open("../islamic_sources/quran.json", "r") as file:
        verses = json.load(file)

    results = []

    for verse in verses:
        if keyword.lower() in verse["topic"].lower():
            results.append(verse)

    return results