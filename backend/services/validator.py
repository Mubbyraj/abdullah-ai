def validate_answer(answer, context):

    context_lower = context.lower()


    sentences = [
        s.strip()
        for s in answer.split(".")
        if s.strip()
    ]


    approved_sentences = []


    for sentence in sentences:

        words = sentence.lower().split()


        matches = 0


        for word in words:

            clean_word = (
                word
                .replace(",", "")
                .replace("(", "")
                .replace(")", "")
                .replace("'", "")
            )


            if len(clean_word) > 4 and clean_word in context_lower:
                matches += 1


        # keep sentences that have evidence
        if matches >= 2:

            approved_sentences.append(sentence)


    if not approved_sentences:

        return (
            "I do not have enough information in my current "
            "Islamic knowledge database."
        )


    return ". ".join(approved_sentences) + "."