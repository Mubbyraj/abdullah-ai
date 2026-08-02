from services.search_engine import search_knowledge


questions = [
    "What is menstruation and prayer?",
    "What are intentions in Islam?",
    "Who is Prophet Muhammad?"
]


for question in questions:
    print("\nQUESTION:")
    print(question)

    results = search_knowledge(question)

    print("\nRESULT:")
    for item in results:
        print(item)

    print("-" * 50)