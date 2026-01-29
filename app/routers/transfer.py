from fastapi import APIRouter, Depends, status, HTTPException
from ..dependencies.deps import get_transfer_service
from ..domain.service.transfer_service import TransferService
from ..domain.dto.TransferCreate import TransferCreateDTO
router = APIRouter(
    prefix= "/transfer",
    tags=["transfer"]
)

@router.post("", status_code=status.HTTP_201_CREATED)
def transfer(
    transfer_in: TransferCreateDTO, 
    service: TransferService = Depends(get_transfer_service)
):
    try:
        transfer = service.transfer(transfer_in)
        return { "message": "Transferência realizada com sucesso"}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=str(e)
        )
     