from pydantic import BaseModel
from datetime import datetime

class AIResponse(BaseModel):
    query: str
    response: str
    created_at: datetime = datetime.utcnow()
