from app.models import Ticket


def preprocess_ticket(ticket: Ticket) -> dict:
    return {
        "ticket_id": ticket.ticket_id,
        "customer_name": ticket.customer_name,
        "email": ticket.email,
        "subject": ticket.subject.strip(),
        "message": ticket.message.strip(),
        "combined_text": f"Subject: {ticket.subject}\nMessage: {ticket.message}"
    }