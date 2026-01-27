from pydantic import BaseModel, EmailStr, Field, field_validator
from ..enum.user_type import UserType

class UserCreateDTO(BaseModel):
    nome_completo: str = Field(..., min_length=3, max_length=100)
    cpf_cnpj: str = Field(..., pattern=r"^\d{11,14}$") 
    email: EmailStr 
    senha: str = Field(..., min_length=8)
    tipo: UserType
    saldo: float = Field(default=0.0, ge=0) 

    @field_validator('nome_completo')
    @classmethod
    def nome_deve_ter_espaco(cls, v: str) -> str:
        if ' ' not in v:
            raise ValueError('O nome deve conter sobrenome')
        return v.title()

    class Config:
        from_attributes = True 