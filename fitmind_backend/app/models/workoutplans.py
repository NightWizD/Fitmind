from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId

class Exercise(BaseModel):
    name: str
    sets: int
    reps: int
    duration_min: int | None = None

class Workout(BaseModel):
    name: str
    exercises: list[Exercise]

class WorkoutPlan(BaseModel):
    user_id: ObjectId
    plan_name: str
    description: str | None = None
    workouts: list[Workout]
    duration_weeks: int | None = None
    status: str = "active"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class WorkoutPlanInDB(WorkoutPlan):
    id: str
