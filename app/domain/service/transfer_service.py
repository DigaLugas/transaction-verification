from ..repository.transfer_repo import TransferRepository
from ..dto.TransferCreate import TransferCreateDTO
from ..service.user_service import UserService 
from ..enum.user_type import UserType
import requests
class TransferService():
    def __init__(self, transfer_repo: TransferRepository, user_service: UserService):
        self._transfer_repo = transfer_repo
        self._user_service = user_service

    def transfer(self, transfer_in: TransferCreateDTO):
        payer = self._user_service.get_user_by_id(transfer_in.from_user_id)
        payee = self._user_service.get_user_by_id(transfer_in.to_user_id)
        if payer.tipo == UserType.LOJISTA:
            raise ValueError("Lojistas só recebem transferências.")
        url = 'https://util.devi.tools/api/v2/authorize'
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError("Transferência não autorizada por serviço externo.")
        print(response.status_code)
        print(response.json())  