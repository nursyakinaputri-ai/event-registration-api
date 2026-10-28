
from app.models.participant import Participant


class ParticipantRepository:
    def __init__(self):
        self._participants: list[dict] = []
        self._next_id = 1

    def create(self, participant: Participant) -> dict:
        participant_data = participant.model_dump(mode="json")
        participant_data["id"] = self._next_id

        self._participants.append(participant_data)
        self._next_id += 1

        return participant_data

    def get_all(self) -> list[dict]:
        return self._participants.copy()
