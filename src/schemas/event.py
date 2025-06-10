from pydantic import BaseModel
from datetime import date

class Event(BaseModel):
    title: str
    city: str
    date: date
