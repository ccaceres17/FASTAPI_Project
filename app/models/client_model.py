from pydantic import BaseModel

class Client(BaseModel):
    primer_nombre: str
    segundo_nombre: str 
    primer_apellido: str
    segundo_apellido: str
    numero_documento: str
    correo: str
    telefono: str
    tipo_documento_id: int