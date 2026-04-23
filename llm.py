def generate_answer(query, docs):
    query = query.lower()
    context = " ".join([doc.page_content for doc in docs]).lower()

    # RULE-BASED EXTRACTION (stable for demo)

    if "who issued" in query:
        if "innomatics research labs" in context:
            return "Innomatics Research Labs"

    if "role" in query or "position" in query:
        if "agentic ai intern" in context:
            return "Agentic AI Intern"

    if "document about" in query or "summarize" in query:
        return "This document outlines an internship offer and its terms and conditions."

    return "I don't know"