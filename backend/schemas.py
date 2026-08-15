from pydantic import BaseModel
from datetime import datetime


class SessionResponse(BaseModel):
    id: int

    start_time: datetime

    end_time: datetime | None

    fatigue_score: float

    blink_count: int

    yawn_count: int

    posture: str

    class Config:
        from_attributes = True