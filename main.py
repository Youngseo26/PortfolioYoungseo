from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()

answer='TRAIN'
@app.get('/answer')
def get_answer():
    return {'answer':answer}

app.mount("/wordle", StaticFiles(directory="static", html=True), name="static")

# class Item(BaseModel):
#     id:int
#     content:str

#@app.get("/hello")
# def sayHello():
#     return {"message": "Hello World"}

#items = ["IMac", "Apple watch", "IPhone", "AirPod"]

# @app.get('/items')
# def read_items():
#     return items

# @app.get('/items/{id}')
# def read_id_items(id):
#     return items[int(id)] ####id라는 문자열을 숫자로 형변환해서

# @app.get("/items")
# def read_item(skip:int=0,limit:int=10):
#     return items[skip:skip+limit]

# @app.post("/items")
# def post_items(item:Item):
#     items.append(item.content) 
#     return "Success"