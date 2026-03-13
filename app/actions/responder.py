def print_summary(ticket_id: str, queue: str, category: str, priority: str) -> None:
    print(f"[{ticket_id}] Routed to: {queue} | Category: {category} | Priority: {priority}")