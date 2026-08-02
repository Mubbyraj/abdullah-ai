import json
import os


BASE_PATH = "../islamic_sources"


def load_all_sources():

    documents = []

    for root, dirs, files in os.walk(BASE_PATH):

        for file in files:

            if file.endswith(".json"):

                path = os.path.join(root, file)

                try:

                    with open(path, "r", encoding="utf-8") as f:
                        data = json.load(f)


                    if isinstance(data, list):

                        for item in data:
                            documents.append({
                                "source": file,
                                "content": str(item)
                            })


                    elif isinstance(data, dict):

                        documents.append({
                            "source": file,
                            "content": str(data)
                        })


                except Exception as e:

                    print(f"Could not load {path}: {e}")


    return documents



if __name__ == "__main__":

    docs = load_all_sources()

    print("Documents loaded:", len(docs))