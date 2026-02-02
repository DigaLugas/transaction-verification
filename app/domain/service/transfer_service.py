from ..repository.transfer_repo import TransferRepository
from ..dto.TransferCreate import TransferCreateDTO
from ..service.user_service import UserService 
from ..enum.user_type import UserType
import requests
class TransferService():
    def __init__(self, transfer_repo: TransferRepository, user_service: UserService):
        self._transfer_repo = transfer_repo
        self._user_service = user_service
        self._authorize_api = 'https://util.devi.tools/api/v2/authorize'
        self._notify_api = 'https://util.devi.tools/api/v1/notify'

    def transfer(self, transfer_in: TransferCreateDTO):
        payer = self._user_service.get_user_by_id(transfer_in.payer)
        payee = self._user_service.get_user_by_id(transfer_in.payee)

        if payer.tipo == UserType.LOJISTA:
            raise ValueError("Lojistas só recebem transferências.")
        response = requests.get(self._authorize_api)
        if payer.saldo < transfer_in.value:
            raise ValueError("Saldo insuficiente para realizar a transferência.")
        if response.status_code != 200:
            raise ValueError("Transferência não autorizada por serviço externo.") 
        payer.saldo -= transfer_in.value
        payee.saldo += transfer_in.value
        self._user_service.update_user(payer)
        self._user_service.update_user(payee)  
        self.notify_users()



    def notify_users(self):
        response = requests.post(self._notify_api, json={
            "message": "Transferência realizada com sucesso."
        })
        if response.status_code != 200:
            raise ValueError("Falha ao notificar usuários.")