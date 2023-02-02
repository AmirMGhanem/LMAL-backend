from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    dict1 = {"name": "Amir", "age": 27,"address": {"city": "Mughar", "country": "Western Neighbourhood"}}
    return dict1



@app.post("/postitems")
async def post_item(item: Item):
    return JSONResponse({"name":item.name}, status_code=200)


