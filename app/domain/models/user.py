from sqlmodel import SQLModel, Field, String, Column
from  ..enum.user_type import UserType

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome_completo: str = Column(String(255), index=True)
    cpf_cnpj: str = Column(String(255), unique=True, index=True, nullable=False)
    email: str = Column(String(255), unique=True, index=True, nullable=False)
    senha: str
    tipo: UserType
    saldo: float = Field(default=0.0)
