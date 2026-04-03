from pydantic import BaseModel

class FitnessPlanCreate(BaseModel):
    plan_details: str

class FitnessPlanOut(BaseModel):
    id: str
    user_id: str
    plan_details: str
    created_at: str
