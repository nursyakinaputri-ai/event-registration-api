
import pytest

from app.models.event import Event
from app.models.participant import Participant
from app.repositories.event_repository import EventRepository
from app.repositories.participant_repository import ParticipantRepository
from app.repositories.registration_repository import RegistrationRepository
from app.services.event_service import EventService
from app.services.participant_service import ParticipantService
from app.services.registration_service import RegistrationService


@pytest.fixture
def setup_service():
    event_repository = EventRepository()
    participant_repository = ParticipantRepository()
    registration_repository = RegistrationRepository()

    event_service = EventService(event_repository)
    participant_service = ParticipantService(participant_repository)

    registration_service = RegistrationService(
        event_repository,
        participant_repository,
        registration_repository,
    )

    event = event_service.create_event(
        Event(
            name="Workshop Python",
            description="Belajar Python",
            location="Lab Komputer",
            date="2026-11-20",
            capacity=2,
        )
    )

    participant1 = participant_service.create_participant(
        Participant(name="Andi Pratama", email="andi@example.com")
    )

    participant2 = participant_service.create_participant(
        Participant(name="Budi Santoso", email="budi@example.com")
    )

    participant3 = participant_service.create_participant(
        Participant(name="Citra Amelia", email="citra@example.com")
    )

    return registration_service, event, participant1, participant2, participant3


def test_successful_registration(setup_service):
    service, event, participant1, _, _ = setup_service

    result = service.register(event["id"], participant1["id"])

    assert result["event_id"] == event["id"]
    assert result["participant_id"] == participant1["id"]


def test_duplicate_registration_rejected(setup_service):
    service, event, participant1, _, _ = setup_service

    service.register(event["id"], participant1["id"])

    with pytest.raises(ValueError, match="sudah terdaftar"):
        service.register(event["id"], participant1["id"])


def test_registration_rejected_when_event_is_full(setup_service):
    service, event, participant1, participant2, participant3 = setup_service

    service.register(event["id"], participant1["id"])
    service.register(event["id"], participant2["id"])

    with pytest.raises(ValueError, match="Kuota event sudah penuh"):
        service.register(event["id"], participant3["id"])
