from fastapi import APIRouter, Query
from app.schemas.rotation import RotationStrategyResponse
from app.services.rotation_service import calculate_crop_rotation

router = APIRouter()

@router.get("/", response_model=RotationStrategyResponse)
def get_rotation_strategy(
    target_crop: str = Query("maize", description="Cultivo principal objetivo (Ej. maize, bean, sorghum)")
):
    """Calcula y devuelve la estrategia recomendada de rotación de cultivos basada en criterios agronómicos."""
    strategy = calculate_crop_rotation(target_crop)
    return strategy