from fastapi import FastAPI
from infraestructura.api.user_controller import router

app = FastAPI(title="Microservicio de Usuarios")

app.include_router(router)

@app.get("/")
def root():
    return {"ok": True, "docs": "/docs", "endpoint": "/users"}
