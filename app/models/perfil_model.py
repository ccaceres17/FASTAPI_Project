from pydantic import BaseModel

class Perfil(BaseModel):
    id: int | None = None
    nombre: str
    descripcion: str