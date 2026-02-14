from abc import ABC, abstractmethod
from domain.user import User

class UserRepository(ABC):
    @abstractmethod
    def create(self, user: User): ...

    @abstractmethod
    def get_all(self): ...

    @abstractmethod
    def get_by_id(self, idusuario: int): ...

    @abstractmethod
    def update(self, idusuario: int, user: User): ...

    @abstractmethod
    def delete(self, idusuario: int): ...
