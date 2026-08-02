from services.response_engine import generate_answer


questions = [
    "What is menstruation and prayer?",
    "What are intentions in Islam?",
    "Who is Prophet Muhammad?"
]


for question in questions:

    print("\n====================")
    print("QUESTION:")
    print(question)


    result = generate_answer(question)


    print("\nANSWER:")
    print(result["answer"])


    print("\nSOURCES:")
    for source in result["sources"]:
        print("-", source)