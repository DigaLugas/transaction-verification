from pydantic import BaseModel
from ..enum.user_type import UserType

class TransferCreateDTO(BaseModel):
    from_user_id: int
    to_user_id: int
    amount: float
