from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId

class Message(BaseModel):
    role: str
    content: str
    timestamp: datetime

class ChatHistory(BaseModel):
    user_id: ObjectId
    session_id: str | None = None
    messages: list[Message]
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ChatHistoryInDB(ChatHistory):
    id: str
