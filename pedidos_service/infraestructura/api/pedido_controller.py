from fastapi import APIRouter, HTTPException
from domain.pedido import Pedido
from application.services.pedido_service import PedidoService
from infraestructura.adapters.pedido_repository_memory import PedidoRepositoryMemory

router = APIRouter()

service = PedidoService(PedidoRepositoryMemory())

@router.post("/pedidos")
def create_pedido(pedido: Pedido):
    return service.create_pedido(pedido)

@router.get("/pedidos/{pedido_id}")
def get_pedido(pedido_id: int):
    pedido = service.get_pedido(pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido

@router.put("/pedidos/{pedido_id}")
def update_pedido(pedido_id: int, descripcion: str):
    pedido = service.update_pedido(pedido_id, descripcion)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido

@router.delete("/pedidos/{pedido_id}")
def delete_pedido(pedido_id: int):
    deleted = service.delete_pedido(pedido_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return {"message": "Pedido eliminado correctamente"}
