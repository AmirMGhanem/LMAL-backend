from fastapi import APIRouter
from app.models.user import User
from app.utils.db_queries import *
from app.core.db import get_db
router = APIRouter()
db = get_db()


@router.get("/get_all")
async def get_all_users():
    result= select_all("user",is_json=True)
    return result


@router.post("/add")
async def create_user(user: User):
    users_collection = db["user"]
    users_collection.insert_one(user.dict())
    return {"User": user.dict(), "message": "User created successfully"}



