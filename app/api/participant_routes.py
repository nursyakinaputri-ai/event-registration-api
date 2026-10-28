
from fastapi import APIRouter, status

from app.dependencies import participant_repository
from app.models.participant import Participant
from app.services.participant_service import ParticipantService


router = APIRouter(prefix="/participants", tags=["Participants"])

service = ParticipantService(participant_repository)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_participant(participant: Participant):
    return service.create_participant(participant)


@router.get("/")
def get_all_participants():
    return service.get_all_participants()
