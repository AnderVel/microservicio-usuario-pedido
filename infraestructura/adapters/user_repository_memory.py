from application.ports.user_repository import UserRepository

class UserRepositoryMemory(UserRepository):
    def __init__(self):
        self.users = {}

    def create(self, user):
        self.users[user.idusuario] = user
        return user

    def get_all(self):
        return list(self.users.values())

    def get_by_id(self, idusuario: int):
        if idusuario not in self.users:
            return None
        return self.users[idusuario]

    def update(self, idusuario: int, user):
        if idusuario not in self.users:
            return None
        self.users[idusuario] = user
        return user

    def delete(self, idusuario: int):
        if idusuario not in self.users:
            return False
        del self.users[idusuario]
        return True
