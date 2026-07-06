from fastapi import FastAPI , HTTPException
from pydantic import BaseModel 

class Item(BaseModel):
    name : str 
    price : float

app = FastAPI()

db = {}

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post('/items/{item_id}')
def create_item(item_id : int , item : Item):
    if item_id in db:
        raise HTTPException(status_code = 404 , detail = "Item already Exists")
    
    db[item_id] = item
    return {f"Item {item.name} Created Successfully "}


@app.get("/item/{item_id}")
def get_item(item_id : int):
    if item_id not in db:
        raise  HTTPException(status_code = 404 , detail = "Item Not Found" )
    
    return db[item_id]

@app.put("/item/{item_id}")
def update_item(item_id : int , item : Item):
    if item_id not in db:
        raise HTTPException(status_code = 404 , detail = "Item Not Found" )
    
    db[item_id] = item
    return {f"Item {item.name} Updated Successfully "}

@app.delete("/item/{item_id}")
def delete_item(item_id : int):
    if item_id not in db:
        raise HTTPException(status_code = 404 , detail = "Item Not Found" )
    
    name = db[item_id].name
    del db[item_id]
    return {f"Item {name} Deleted Successfully "}

