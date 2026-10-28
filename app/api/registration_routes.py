
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from app.dependencies import (
    event_repository,
    participant_repository,
    registration_repository,
)
from app.services.registration_service import RegistrationService


router = APIRouter(prefix="/registrations", tags=["Registrations"])

service = RegistrationService(
    event_repository,
    participant_repository,
    registration_repository,
)


class RegistrationRequest(BaseModel):
    event_id: int = Field(gt=0)
    participant_id: int = Field(gt=0)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_registration(request: RegistrationRequest):
    try:
        return service.register(
            request.event_id,
            request.participant_id,
        )
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        )


@router.get("/")
def get_all_registrations():
    return service.get_all_registrations()
