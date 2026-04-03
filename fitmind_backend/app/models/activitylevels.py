from pydantic import BaseModel

class ActivityLevel(BaseModel):
    level: str
    description: str
    multiplier: float

class ActivityLevelInDB(ActivityLevel):
    id: str
