from app.models import TicketAnalysis


def route_ticket(analysis: TicketAnalysis) -> str:
    if analysis.category == "Billing":
        return "Finance Queue"
    if analysis.category == "Technical Support":
        return "Technical Support Queue"
    if analysis.category == "Account Access":
        return "Identity and Access Queue"
    if analysis.category == "Complaint":
        return "Customer Escalation Queue"
    if analysis.category == "Feature Request":
        return "Product Queue"
    return "General Support Queue"