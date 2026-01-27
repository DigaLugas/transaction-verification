from fastapi import FastAPI
from .routers import users
from .database.init_db import init_db
app = FastAPI()

app.include_router(users.router)

@app.on_event("startup")
def on_startup():
    return init_db()