from pydantic import BaseModel

class NutritionLogCreate(BaseModel):
    log_details: str

class NutritionLogOut(BaseModel):
    id: str
    user_id: str
    log_details: str
    created_at: str
