from pydantic import BaseModel

class User(BaseModel):
    id: int = None
    nombre: str
    descripcion: str