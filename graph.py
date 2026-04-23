from langgraph.graph import StateGraph

from modules.retriever import retrieve_docs
from modules.llm import generate_answer
from modules.hitl import check_escalation, human_response


def retrieve_node(state):
    query = state["query"]
    db = state["db"]

    docs = retrieve_docs(db, query)

    return {
        "query": query,
        "db": db,
        "docs": docs
    }


def generate_node(state):
    query = state["query"]
    docs = state["docs"]
    db = state["db"]

    answer = generate_answer(query, docs)

    return {
        "query": query,
        "db": db,
        "docs": docs,
        "answer": answer
    }


def decision_node(state):
    if check_escalation(state["docs"], state["answer"]):
        return "hitl"
    return "final"


def hitl_node(state):
    return {
        "answer": human_response()
    }


def build_graph():
    graph = StateGraph(dict)

    graph.add_node("retrieve", retrieve_node)
    graph.add_node("generate", generate_node)
    graph.add_node("hitl", hitl_node)

    graph.set_entry_point("retrieve")

    graph.add_edge("retrieve", "generate")

    graph.add_conditional_edges(
        "generate",
        decision_node,
        {
            "hitl": "hitl",
            "final": "__end__"
        }
    )

    graph.add_edge("hitl", "__end__")

    return graph.compile()