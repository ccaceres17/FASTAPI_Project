from fastapi import APIRouter, HTTPException
from app.controllers.perfil_controller import *
from app.models.perfil_model import Perfil
router = APIRouter()

nuevo_usuario = PerfilController()


@router.post("/create_perfil")
async def create_perfil(perfil: Perfil):
    rpta = nuevo_usuario.create_user(perfil)
    return rpta


@router.get("/get_perfil/{user_id}",response_model=Perfil)
async def get_perfil(perfil_id: int):
    rpta = nuevo_usuario.get_user(perfil_id)
    return rpta

@router.get("/get_perfiles/")
async def get_perfiles():
    rpta = nuevo_perfil.get_perfiles()
    return rpta