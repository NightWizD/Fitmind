from pydantic import BaseModel
from typing import Optional

class UserMetrics(BaseModel):
    age: int
    gender: str
    height: float
    weight: float
    bmi: Optional[float] = None
    activity_level: Optional[str] = None

class UpdateMetrics(BaseModel):
    activity_level: str
