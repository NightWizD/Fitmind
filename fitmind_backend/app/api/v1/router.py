from fastapi import APIRouter

from .endpoints import auth, fitness, nutrition, user
from .endpoints.workout import router as workout_router
from .endpoints.diet import router as diet_router

api_router = APIRouter()

api_router.include_router(auth, prefix="/auth", tags=["auth"])
api_router.include_router(fitness, prefix="/fitness", tags=["fitness"])
api_router.include_router(nutrition, prefix="/nutrition", tags=["nutrition"])
api_router.include_router(user, prefix="/user", tags=["user"])
api_router.include_router(workout_router, prefix="/workout", tags=["workout"])
api_router.include_router(diet_router, prefix="/diet", tags=["diet"])
