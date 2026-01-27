from sqlmodel import SQLModel
from .engine import engine

from ..domain.models.user import User 
def init_db():
    SQLModel.metadata.create_all(engine)
