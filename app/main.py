from fastapi import FastAPI
from .routers import users
from .database.init_db import init_db
from contextlib import asynccontextmanager
from .routers import transfer
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan= lifespan)

app.include_router(users.router)
app.include_router(transfer.router)
