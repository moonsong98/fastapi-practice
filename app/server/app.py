from fastapi import FastAPI
from .routes.user import router

app = FastAPI()
app.include_router(router, tags=["User"], prefix="/user")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to FastAPI Practice Project"}
