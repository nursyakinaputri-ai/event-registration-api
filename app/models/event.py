
from pydantic import BaseModel, Field


class Event(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    description: str = Field(default="", max_length=500)
    location: str = Field(min_length=3, max_length=150)
    date: str
    capacity: int = Field(gt=0)
