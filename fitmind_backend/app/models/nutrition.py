from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId

class Meal(BaseModel):
    meal_type: str
    foods: list[dict]  # {name: str, calories: float, protein_g: float}

class DietPlan(BaseModel):
    user_id: ObjectId
    plan_name: str
    description: str | None = None
    meals: list[Meal]
    total_calories: float | None = None
    status: str = "active"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class DietPlanInDB(DietPlan):
    id: str
