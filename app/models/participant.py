
from pydantic import BaseModel, Field, EmailStr


class Participant(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    email: EmailStr
