from datetime import datetime
from sqlmodel import SQLModel, Field
import uuid

class Transfer(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True
    )
    value: float = Field(nullable=False)
    
    payer: int = Field(
        foreign_key="user.id",
        nullable=False
    )

    payee: int = Field(
        foreign_key="user.id",
        nullable=False
    )

    

    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False
    )
