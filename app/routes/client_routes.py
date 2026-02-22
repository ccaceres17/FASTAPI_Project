from fastapi import APIRouter
from app.controllers.client_controller import ClientController
from app.models.client_model import Client

router = APIRouter()
client_controller = ClientController()

@router.post("/create_client")
async def create_client(client: Client):
    return client_controller.create_client(client)

@router.get("/get_clients")
async def get_clients():
    return client_controller.get_clients()

@router.delete("/delete_client/{client_id}")
async def delete_client(client_id: int):
    return client_controller.delete_client(client_id)