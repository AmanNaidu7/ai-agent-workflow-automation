import json
from openai import OpenAI
from app.config import OPENAI_API_KEY, OPENAI_MODEL
from app.llm.prompts import SYSTEM_PROMPT
from app.models import TicketAnalysis

client = OpenAI(api_key=OPENAI_API_KEY)


def analyze_ticket(ticket_text: str) -> TicketAnalysis:
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        temperature=0,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": ticket_text}
        ]
    )

    content = response.choices[0].message.content.strip()
    parsed = json.loads(content)
    return TicketAnalysis(**parsed)