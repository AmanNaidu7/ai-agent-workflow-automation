import json
from app.models import Ticket


def load_tickets(file_path: str) -> list[Ticket]:
    with open(file_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)
    return [Ticket(**item) for item in raw_data]