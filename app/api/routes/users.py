from fastapi import APIRouter
from app.core.db import get_db
import json
from bson.json_util import dumps
from app.utils.db_queries import select_one
router = APIRouter()


@router.get("/get_all")
async def get_all_users():
    result= select_one("user",{"first_name":"Amir"},is_json=True)
    return result

