from app.config import DATA_FILE, OUTPUT_DIR
from app.input.loader import load_tickets
from app.processing.preprocess import preprocess_ticket
from app.llm.analyzer import analyze_ticket
from app.workflow.router import route_ticket
from app.actions.logger import save_routed_tickets
from app.actions.responder import print_summary
from app.models import RoutedTicket


def run_workflow() -> None:
    tickets = load_tickets(DATA_FILE)
    results: list[RoutedTicket] = []

    for ticket in tickets:
        prepared = preprocess_ticket(ticket)
        analysis = analyze_ticket(prepared["combined_text"])
        assigned_queue = route_ticket(analysis)

        routed = RoutedTicket(
            ticket_id=ticket.ticket_id,
            customer_name=ticket.customer_name,
            email=ticket.email,
            subject=ticket.subject,
            category=analysis.category,
            priority=analysis.priority,
            sentiment=analysis.sentiment,
            summary=analysis.summary,
            recommended_action=analysis.recommended_action,
            assigned_queue=assigned_queue,
            draft_response=analysis.draft_response,
        )

        results.append(routed)
        print_summary(
            ticket_id=routed.ticket_id,
            queue=routed.assigned_queue,
            category=routed.category,
            priority=routed.priority,
        )

    save_routed_tickets(results, f"{OUTPUT_DIR}/routed_tickets.json")
    print("\nWorkflow complete. Results saved to outputs/routed_tickets.json")


if __name__ == "__main__":
    run_workflow()