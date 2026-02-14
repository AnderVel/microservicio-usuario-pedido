from pydantic import BaseModel

class User(BaseModel):
    idusuario: int
    nombre: str
    email: str
