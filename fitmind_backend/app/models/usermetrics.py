from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId

class UserMetrics(BaseModel):
    user_id: ObjectId
    height_cm: float
    weight_kg: float
    age: int
    gender: str
    bmi: float | None = None
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class UserMetricsInDB(UserMetrics):
    id: str
