from datetime import datetime
from sqlmodel import SQLModel, Field
import uuid

class Transfer(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True
    )

    from_user_id: int = Field(
        foreign_key="user.id",
        nullable=False
    )

    to_user_id: int = Field(
        foreign_key="user.id",
        nullable=False
    )

    amount: float = Field(nullable=False)

    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False
    )
