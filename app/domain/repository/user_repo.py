from sqlmodel import Session, select
from ..models.user import User
class UserRepository:
    def __init__(self, session: Session):
        self._session = session
        

    def save(self, user: User) -> User:
        self._session.add(user)
        self._session.commit()
        self._session.refresh(user)
        return user
    
    def get_user_by_email(self, email: str) -> User:
        query = select(User).where(User.email == email)
        return self._session.exec(query).first()

    def get_user_by_id(self, id: int) -> User:
        query = select(User).where(User.id == id)
        
        return self._session.exec(query).first()