from fastapi import APIRouter
from app.api.v1.endpoints import health, crops, climate, rotations, analysis, terreno

api_router = APIRouter()

api_router.include_router(health.router, tags=["health"])
api_router.include_router(crops.router, prefix="/crops", tags=["crops"])
api_router.include_router(climate.router, prefix="/climate", tags=["climate"])
api_router.include_router(rotations.router, prefix="/rotations", tags=["rotations"])
api_router.include_router(analysis.router, prefix="/analysis", tags=["analysis"])
api_router.include_router(terreno.router)  # <--- Incluimos el router del módulo terreno