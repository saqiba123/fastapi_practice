from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()


@app.get("/test/")
async def test():
    return {"hello":"world"}

@app.get("/usernames/{user_id}/")
async def test(user_id:str, query:int=1):
    return {"hello":user_id}


class MyData(BaseModel):
    name: str
    age : int


@app.post("/create/")
async def create_user(data:MyData):
    return {"info":data}