from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel

app = FastAPI()
router = APIRouter()

users_db = {}  # Будем использовать dict для хранения данных пользователей

class User(BaseModel):
    email: str
    name: str
    surname: str
    patronymic: str

@router.post("/user/", response_model=User)
async def create_user(user: User):
    if user.email in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.email] = user
    return user

@router.get("/user/{email}", response_model=User)
async def get_user(email: str):
    user = users_db.get(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

app.include_router(router)
