import json
import os


BASE_PATH = "../islamic_sources"


def load_json_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    except Exception as e:
        print(f"Could not load {path}: {e}")
        return []


def load_directory(directory):

    data = []

    if not os.path.exists(directory):
        return data

    for file in os.listdir(directory):

        if file.endswith(".json"):

            path = os.path.join(directory, file)

            content = load_json_file(path)

            data.append({
                "source": file,
                "content": content
            })

    return data


def load_all_sources():

    knowledge = {}

    folders = [
        "quran",
        "hadith",
        "fiqh",
        "tafsir",
        "seerah",
        "aqeedah",
        "scholars"
    ]


    for folder in folders:

        path = os.path.join(BASE_PATH, folder)

        knowledge[folder] = load_directory(path)


    return knowledge



if __name__ == "__main__":

    data = load_all_sources()

    for category, sources in data.items():

        print(
            category,
            "=>",
            len(sources),
            "books loaded"
        )