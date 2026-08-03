from services.rag_engine import generate_answer


questions = [
    "What are intentions in Islam?",
    "What is menstruation and prayer?",
    "Who is Prophet Muhammad?"
]


for q in questions:

    print("\n====================")
    print("QUESTION:")
    print(q)

    print("\nANSWER:")

    answer = generate_answer(q)

    print(answer)