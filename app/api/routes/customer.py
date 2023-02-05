from fastapi import APIRouter
from app.utils.db_queries import *
from app.core.db import get_db
from app.models.customer import Customer
router = APIRouter()
db = get_db()

@router.post("/add")
async def create_customer(customer: Customer):
    if "customer" not in db.list_collection_names():
        db.create_collection("customer")
    customers_collection = db["customer"]
    users_collection = db["user"]
    users_collection.insert_one(customer.user.dict())
    customers_collection.insert_one(customer.dict())
    return {"Customer": customer.dict(), "message": "Customer created successfully"}



@router.get("/get_all")
async def get_all_customers():
    result= select_all("customer",is_json=True)
    return result
