# from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from database import database


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


@app.post("/items/")
async def create_item(item: Item):
    collection = database.users1
    new_user = await collection.insert_one(item.dict())
    x = new_user.inserted_id
    return {"item_id": str(x)}






# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
#
#
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}


