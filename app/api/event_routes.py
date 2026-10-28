
from fastapi import APIRouter, status

from app.dependencies import event_repository
from app.models.event import Event
from app.services.event_service import EventService


router = APIRouter(prefix="/events", tags=["Events"])

service = EventService(event_repository)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_event(event: Event):
    return service.create_event(event)


@router.get("/")
def get_all_events():
    return service.get_all_events()
