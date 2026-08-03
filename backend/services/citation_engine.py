import ast


def format_citations(documents):

    citations = []
    seen = set()

    for doc in documents:

        if not isinstance(doc, dict):
            continue

        source = doc.get("source", "")

        content = doc.get("content", "")

        topic = None
        surah = None
        ayah = None

        if content:

            try:
                parsed = ast.literal_eval(content)

                if isinstance(parsed, dict):

                    topic = parsed.get("topic")
                    surah = parsed.get("surah")
                    ayah = parsed.get("ayah")

            except Exception:
                pass

        if source:

            text = f"📚 Source: {source}"

            if text not in seen:
                citations.append(text)
                seen.add(text)

        if surah and ayah:

            text = f"📖 Quran: {surah} ({ayah})"

            if text not in seen:
                citations.append(text)
                seen.add(text)

        if topic:

            text = f"🏷 Topic: {topic}"

            if text not in seen:
                citations.append(text)
                seen.add(text)

    if not citations:
        return ""

    return "\n\nReferences:\n" + "\n".join(
        f"- {c}"
        for c in citations
    )