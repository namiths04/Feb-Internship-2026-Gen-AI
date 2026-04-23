def retrieve_docs(db, query):
    docs = db.similarity_search(query, k=5)

    query_words = query.lower().split()

    def score(doc):
        text = doc.page_content.lower()
        return sum(word in text for word in query_words)

    docs = sorted(docs, key=score, reverse=True)

    return docs[:3]