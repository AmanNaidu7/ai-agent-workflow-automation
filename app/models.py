from pydantic import BaseModel


class Ticket(BaseModel):
    ticket_id: str
    customer_name: str
    email: str
    subject: str
    message: str


class TicketAnalysis(BaseModel):
    category: str
    priority: str
    sentiment: str
    summary: str
    recommended_action: str
    draft_response: str


class RoutedTicket(BaseModel):
    ticket_id: str
    customer_name: str
    email: str
    subject: str
    category: str
    priority: str
    sentiment: str
    summary: str
    recommended_action: str
    assigned_queue: str
    draft_response: str