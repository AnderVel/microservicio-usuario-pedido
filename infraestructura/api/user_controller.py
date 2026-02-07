from fastapi import APIRouter, HTTPException
from domain.user import User
from application.services.user_service import UserService
from infraestructura.adapters.user_repository_memory import UserRepositoryMemory

router = APIRouter(prefix="/users", tags=["Usuarios"])

service = UserService(UserRepositoryMemory())

@router.post("/", status_code=201)
def create_user(user: User):
    return service.create(user)

@router.get("/")
def list_users():
    return service.list()

@router.get("/{idusuario}")
def get_user(idusuario: int):
    user = service.get(idusuario)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.put("/{idusuario}")
def update_user(idusuario: int, user: User):
    updated = service.update(idusuario, user)
    if updated is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return updated

@router.delete("/{idusuario}", status_code=204)
def delete_user(idusuario: int):
    ok = service.delete(idusuario)
    if not ok:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
