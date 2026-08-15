from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime

from backend.database import Base


class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)

    start_time = Column(DateTime, default=datetime.utcnow)

    end_time = Column(DateTime, nullable=True)

    fatigue_score = Column(Float, default=0.0)

    blink_count = Column(Integer, default=0)

    yawn_count = Column(Integer, default=0)

    posture = Column(String, default="Unknown")