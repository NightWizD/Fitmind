from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId

class Supplement(BaseModel):
    name: str
    dosage: str
    reason: str

class SupplementRecommendation(BaseModel):
    user_id: ObjectId
    supplements: list[Supplement]
    created_at: datetime = Field(default_factory=datetime.utcnow)

class SupplementRecommendationInDB(SupplementRecommendation):
    id: str
