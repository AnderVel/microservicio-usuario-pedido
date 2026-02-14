from dataclasses import dataclass

@dataclass
class Pedido:
    idpedido: int
    idusuario: int
    descripcion: str
