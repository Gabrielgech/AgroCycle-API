from pydantic import BaseModel
from typing import List, Any

class ParcelInput(BaseModel):
    parcel_name: str
    coordinates: List[Any]  # Recibe los puntos del polígono de la parcela de forma flexible
    target_crop: str

class AnalysisResponse(BaseModel):
    parcel_name: str
    estimated_area_hectares: float
    suitability_score: float
    recommendations: List[str]
    source: str