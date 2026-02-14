from abc import ABC, abstractmethod
from domain.pedido import Pedido

class PedidoRepository(ABC):

    @abstractmethod
    def create(self, pedido: Pedido) -> Pedido:
        pass

    @abstractmethod
    def get(self, pedido_id: int) -> Pedido | None:
        pass

    @abstractmethod
    def update(self, pedido_id: int, descripcion: str) -> Pedido | None:
        pass

    @abstractmethod
    def delete(self, pedido_id: int) -> bool:
        pass
