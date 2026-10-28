
class RegistrationRepository:
    def __init__(self):
        self._registrations: list[dict] = []
        self._next_id = 1

    def create(self, event_id: int, participant_id: int) -> dict:
        registration = {
            "id": self._next_id,
            "event_id": event_id,
            "participant_id": participant_id,
        }

        self._registrations.append(registration)
        self._next_id += 1

        return registration

    def get_all(self) -> list[dict]:
        return self._registrations.copy()
