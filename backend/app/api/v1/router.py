from fastapi import APIRouter
from app.api.v1.endpoints import health, crops

api_router = APIRouter()

# Incluir las rutas existentes y las nuevas
api_router.include_router(health.router, prefix="/health", tags=["Health"])
api_router.include_router(crops.router, prefix="/crops", tags=["Crops"])