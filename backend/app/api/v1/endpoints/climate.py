from fastapi import APIRouter, Query
from app.schemas.climate import ClimateDataResponse
from app.services.climate_service import get_nasa_climate_data

router = APIRouter()

@router.get("/", response_model=ClimateDataResponse)
def get_climate_indicators(
    lat: float = Query(20.97, description="Latitud de la parcela (Ej. Mérida: 20.97)"),
    lon: float = Query(-89.62, description="Longitud de la parcela (Ej. Mérida: -89.62)")
):
    """Obtiene los indicadores climáticos y de humedad de suelo basados en datos satelitales de la NASA."""
    climate_data = get_nasa_climate_data(lat, lon)
    return climate_data