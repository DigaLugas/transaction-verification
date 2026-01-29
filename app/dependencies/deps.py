from fastapi import Depends
from sqlmodel import Session
from ..database.session import get_session
from ..domain.repository.user_repo import UserRepository
from ..domain.service.user_service import UserService
from ..domain.repository.transfer_repo import TransferRepository
from ..domain.service.transfer_service import  TransferService


def get_user_repository(
        session: Session = Depends(get_session),
) -> UserRepository:
    return UserRepository(session)

def get_user_service(
    repo: UserRepository = Depends(get_user_repository),
) -> UserService:
    return UserService(repo)
def get_transfer_repository(
        session: Session = Depends(get_session),
) -> UserRepository:
    return TransferRepository(session)
def get_transfer_service(
    repo: TransferRepository = Depends(get_transfer_repository),
    user_service: UserService = Depends(get_user_service) 
) -> TransferService:
    return TransferService(repo, user_service)