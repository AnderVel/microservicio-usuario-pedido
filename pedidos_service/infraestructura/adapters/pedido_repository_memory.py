from domain.pedido import Pedido
from application.ports.pedido_repository import PedidoRepository

class PedidoRepositoryMemory(PedidoRepository):

    def __init__(self):
        self.pedidos: dict[int, Pedido] = {}

    def create(self, pedido: Pedido) -> Pedido:
        self.pedidos[pedido.idpedido] = pedido
        return pedido

    def get(self, pedido_id: int) -> Pedido | None:
        return self.pedidos.get(pedido_id)

    def update(self, pedido_id: int, descripcion: str) -> Pedido | None:
        pedido = self.pedidos.get(pedido_id)
        if not pedido:
            return None
        pedido.descripcion = descripcion
        return pedido

    def delete(self, pedido_id: int) -> bool:
        return self.pedidos.pop(pedido_id, None) is not None
