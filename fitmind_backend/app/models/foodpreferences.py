from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId

class FoodPreferences(BaseModel):
    user_id: ObjectId
    preferences: list[str] = []
    allergies: list[str] = []
    calorie_goal: float | None = None
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class FoodPreferencesInDB(FoodPreferences):
    id: str
