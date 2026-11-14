from fastapi import APIRouter, HTTPException
from typing import List
from app.agronomy.catalog.crop_catalog import get_all_crops, get_crop_by_id, CropModel

router = APIRouter()

@router.get("/", response_model=List[CropModel])
def list_crops():
    """Obtiene la lista completa de cultivos disponibles para la planificación y rotación."""
    return get_all_crops()

@router.get("/{crop_id}", response_model=CropModel)
def get_crop_detail(crop_id: str):
    """Obtiene la información agronómica detallada de un cultivo específico por su ID."""
    crop = get_crop_by_id(crop_id)
    if not crop:
        raise HTTPException(status_code=404, detail="Cultivo no encontrado en el catálogo agronómico")
    return crop