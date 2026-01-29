from sqlmodel import Session, select
from ..models.transfer import Transfer
class TransferRepository:
    def __init__(self, session: Session):
        self._session = session
        