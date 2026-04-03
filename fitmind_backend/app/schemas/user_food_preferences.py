from pydantic import BaseModel
from typing import List, Optional

class UserFoodPreferences(BaseModel):
    food_preference: str  # veg, non-veg, vegan, eggitarian
    daily_foods: Optional[List[str]] = []
    allergies: Optional[List[str]] = []
