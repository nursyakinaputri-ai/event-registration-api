
from app.models.event import Event


class EventRepository:
    def __init__(self):
        self._events: list[dict] = []
        self._next_id = 1

    def create(self, event: Event) -> dict:
        event_data = event.model_dump()
        event_data["id"] = self._next_id

        self._events.append(event_data)
        self._next_id += 1

        return event_data

    def get_all(self) -> list[dict]:
        return self._events.copy()
