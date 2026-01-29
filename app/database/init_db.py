from sqlmodel import SQLModel
from .engine import engine
from ..domain.models.user import User
from ..domain.models.transfer import Transfer

def init_db():
    SQLModel.metadata.create_all(engine)
