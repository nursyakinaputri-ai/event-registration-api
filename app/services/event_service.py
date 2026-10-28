
from app.models.event import Event
from app.repositories.event_repository import EventRepository


class EventService:
    def __init__(self, repository: EventRepository):
        self.repository = repository

    def create_event(self, event: Event) -> dict:
        return self.repository.create(event)

    def get_all_events(self) -> list[dict]:
        return self.repository.get_all()
