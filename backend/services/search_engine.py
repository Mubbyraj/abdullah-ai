from services.knowledge_loader import load_all_sources


knowledge = load_all_sources()


def search_knowledge(query):
    results = []

    query = query.lower()

    for category, books in knowledge.items():
        for book in books:

            entries = book.get("entries", [])

            for item in entries:
                text = item.get("text", "").lower()
                topic = item.get("topic", "").lower()

                if query in text or query in topic:
                    results.append({
                        "category": category,
                        "source": book.get("source", "Unknown"),
                        "reference": item.get("reference", ""),
                        "text": item.get("text", "")
                    })

    return results