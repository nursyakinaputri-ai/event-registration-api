from app.repositories.event_repository import EventRepository
from app.repositories.participant_repository import ParticipantRepository
from app.repositories.registration_repository import RegistrationRepository


class RegistrationService:
    def __init__(
        self,
        event_repository: EventRepository,
        participant_repository: ParticipantRepository,
        registration_repository: RegistrationRepository,
    ):
        self.event_repository = event_repository
        self.participant_repository = participant_repository
        self.registration_repository = registration_repository

    def register(self, event_id: int, participant_id: int) -> dict:
        events = self.event_repository.get_all()
        participants = self.participant_repository.get_all()
        registrations = self.registration_repository.get_all()

        event = next(
            (item for item in events if item["id"] == event_id),
            None,
        )
        if event is None:
            raise ValueError("Event tidak ditemukan.")

        participant = next(
            (item for item in participants if item["id"] == participant_id),
            None,
        )
        if participant is None:
            raise ValueError("Peserta tidak ditemukan.")

        already_registered = any(
            item["event_id"] == event_id
            and item["participant_id"] == participant_id
            for item in registrations
        )
        if already_registered:
            raise ValueError("Peserta sudah terdaftar pada event ini.")

        total_registered = sum(
            1 for item in registrations if item["event_id"] == event_id
        )
        if total_registered >= event["capacity"]:
            raise ValueError("Kuota event sudah penuh.")

        return self.registration_repository.create(event_id, participant_id)

    def get_all_registrations(self) -> list[dict]:
        return self.registration_repository.get_all()