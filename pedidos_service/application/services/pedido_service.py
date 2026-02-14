from domain.pedido import Pedido
from application.ports.pedido_repository import PedidoRepository

class PedidoService:

    def __init__(self, repository: PedidoRepository):
        self.repository = repository

    def create_pedido(self, pedido: Pedido) -> Pedido:
        return self.repository.create(pedido)

    def get_pedido(self, pedido_id: int) -> Pedido | None:
        return self.repository.get(pedido_id)

    def update_pedido(self, pedido_id: int, descripcion: str) -> Pedido | None:
        return self.repository.update(pedido_id, descripcion)

    def delete_pedido(self, pedido_id: int) -> bool:
        return self.repository.delete(pedido_id)
