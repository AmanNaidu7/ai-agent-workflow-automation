import json
import os
from app.models import RoutedTicket


def save_routed_tickets(records: list[RoutedTicket], file_path: str) -> None:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump([record.model_dump() for record in records], f, indent=2)