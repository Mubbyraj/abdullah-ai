def detect_topic(question):

    question = question.lower()


    topics = {

        "prayer": [
            "salah",
            "pray",
            "prayer",
            "namaz"
        ],

        "fasting": [
            "fast",
            "ramadan",
            "sawm"
        ],

        "marriage": [
            "marriage",
            "nikah",
            "wife",
            "husband"
        ],

        "purification": [
            "wudu",
            "ablution",
            "menstruation",
            "ghusl"
        ]
    }


    for topic, words in topics.items():

        for word in words:

            if word in question:
                return topic


    return "general"