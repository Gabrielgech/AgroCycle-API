from fastapi import APIRouter
from app.api.v1.endpoints import health, crops, climate, rotations, analysis

api_router = APIRouter()

# Incluir todos los routers de la API v1
api_router.include_router(health.router, prefix="/health", tags=["Health"])
api_router.include_router(crops.router, prefix="/crops", tags=["Crops"])
api_router.include_router(climate.router, prefix="/climate", tags=["Climate"])
api_router.include_router(rotations.router, prefix="/rotation", tags=["Rotation Strategy"])
api_router.include_router(analysis.router, prefix="/analysis", tags=["Parcel Analysis"])