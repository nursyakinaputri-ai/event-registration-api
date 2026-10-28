
from app.models.participant import Participant
from app.repositories.participant_repository import ParticipantRepository


class ParticipantService:
    def __init__(self, repository: ParticipantRepository):
        self.repository = repository

    def create_participant(self, participant: Participant) -> dict:
        return self.repository.create(participant)

    def get_all_participants(self) -> list[dict]:
        return self.repository.get_all()
