from sqlmodel import Session, select
from ..models.transfer import Transfer
class TransferRepository:
    def __init__(self, session: Session):
        self._session = session
        
    def save(self, transfer: Transfer) -> Transfer:
        self._session.add(transfer)
        self._session.commit()
        self._session.refresh(transfer)
        return transfer