from fastapi import Depends
from sqlmodel import Session
from ..database.session import get_session
from ..domain.repository.user_repo import UserRepository
from ..domain.service.user_service import UserService

def get_user_repository(
        session: Session = Depends(get_session),
) -> UserRepository:
    return UserRepository(session)

def get_user_service(
    repo: UserRepository = Depends(get_user_repository),
) -> UserService:
    return UserService(repo)