from ..repository.user_repo import UserRepository
from ..dto.UserCreated import UserCreateDTO
from ..models.user import User
class UserService:
    def __init__(self, user_repo: UserRepository):
        self._user_repo = user_repo
        
    def save(self, user_in: UserCreateDTO):
        usuario_existente = self._user_repo.get_user_by_email(user_in.email)
        if usuario_existente:
            raise ValueError("Email já cadastrado")
        
        user = User(
            nome_completo=user_in.nome_completo,
            cpf_cnpj=user_in.cpf_cnpj,
            email=user_in.email,
            senha=user_in.senha,
            tipo=user_in.tipo,
            saldo=0.0
        )
        return self._user_repo.save(user)
        
    def get_user_by_id(self, id: int) -> User:
        usuario = self._user_repo.get_user_by_id(id= id)
        if not usuario:
            raise ValueError("Usuário não encontrado")
        
        return usuario