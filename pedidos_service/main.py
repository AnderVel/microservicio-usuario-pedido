from fastapi import FastAPI
from infraestructura.api.pedido_controller import router

app = FastAPI(title="Microservicio de Pedidos")

app.include_router(router)
