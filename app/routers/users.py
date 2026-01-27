from fastapi import APIRouter, status, HTTPException, Depends
from ..dependencies.deps import get_user_service
from ..domain.service.user_service import UserService
from ..domain.dto.UserCreated import UserCreateDTO
router = APIRouter(
    prefix= "/users", tags=["users"]
)

@router.post(
    "",
    status_code= status.HTTP_201_CREATED
)
def create_user(
    user_in: UserCreateDTO,
    service: UserService = Depends(get_user_service),
):
    try:
        user = service.save(user_in)
        return user
    except ValueError as e:
        raise HTTPException(
        status_code= status.HTTP_409_CONFLICT,
        detail= str(e)
        )