from modules.loader import load_pdf
from modules.chunking import chunk_docs
from modules.embedding import create_vector_store
from modules.graph import build_graph

print("🔄 Initializing system...\n")

docs = load_pdf("data/sample.pdf")
print(f"✅ Loaded {len(docs)} pages")

chunks = chunk_docs(docs)
print(f"✅ Created {len(chunks)} chunks")

db = create_vector_store(chunks)
print("✅ Vector database ready")

graph = build_graph()
print("✅ LangGraph workflow initialized")

print("\n🚀 System ready!\n")

while True:
    query = input("Ask a question (or type 'exit'): ")

    if query.lower() == "exit":
        print("Exiting system...")
        break

    result = graph.invoke({
        "query": query,
        "db": db
    })

    print("\nAnswer:")
    print(result["answer"])