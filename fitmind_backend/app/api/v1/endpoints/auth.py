from fastapi import APIRouter, Depends, HTTPException
from app.schemas.auth import UserLogin, Token, UserCreate
from app.schemas.user import UserOut
from app.services.auth_service import authenticate_user, create_user
from app.core.security import create_access_token
from app.api.dependencies import get_current_user

router = APIRouter()

@router.post("/register", response_model=Token)
async def register(user: UserCreate):
    db_user = await create_user(user)
    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
async def login(user: UserLogin):
    user_auth = await authenticate_user(user.email, user.password)
    if not user_auth:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": user_auth.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserOut)
async def read_users_me(current_user = Depends(get_current_user)):
    return current_user
