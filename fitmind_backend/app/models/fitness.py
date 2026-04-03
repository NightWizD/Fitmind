from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId

class Goal(BaseModel):
    user_id: ObjectId
    goal_type: str
    target_value: float
    current_value: float | None = None
    deadline: datetime | None = None
    status: str = "active"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class GoalInDB(Goal):
    id: str
