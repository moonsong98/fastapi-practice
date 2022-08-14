from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Body(BaseModel):
    height: int
    weight: int

bodies = {}

@app.get("/")
def read_all():
    return bodies

@app.get("/{id}", response_model=Union[Body, str])
async def read_body(id: str):
    if id in bodies:
        return bodies[id]
    else:
        return 'Not Found'

@app.post("/modify_body/{id}")
async def create_body(id: str, body: Body):
    bodies[id] = body

@app.patch("/modify_body/{id}")
async def update_body(id: str, body: Body):
    bodies[id] = body

@app.delete("/modify_body/{id}")
async def delete_body(id: str):
    if id in bodies:
        del bodies[id]
    

