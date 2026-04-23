def check_escalation(docs, response):
    if "i don't know" in response.lower():
        return True
    return False


def human_response():
    return "Escalated to human support."