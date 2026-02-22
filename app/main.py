from fastapi import FastAPI

from app.routes.user_routes import router as user_router
from app.routes.client_routes import router as client_router
from app.routes.perfil_routes import router as perfil_router

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(client_router, prefix="/clients", tags=["Clients"])
app.include_router(perfil_router, prefix="/perfils", tags=["Perfils"])