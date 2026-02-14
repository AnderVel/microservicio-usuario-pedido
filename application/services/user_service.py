from application.ports.user_repository import UserRepository

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def create(self, user):
        return self.repo.create(user)

    def list(self):
        return self.repo.get_all()

    def get(self, idusuario: int):
        return self.repo.get_by_id(idusuario)

    def update(self, idusuario: int, user):
        return self.repo.update(idusuario, user)

    def delete(self, idusuario: int):
        return self.repo.delete(idusuario)
