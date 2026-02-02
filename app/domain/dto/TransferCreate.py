from pydantic import BaseModel
from ..enum.user_type import UserType

class TransferCreateDTO(BaseModel):
    value: float
    payer: int
    payee: int
    
