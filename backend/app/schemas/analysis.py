from pydantic import BaseModel
from typing import List

class ParcelInput(BaseModel):
    terreno_name: str
    municipality: str
    state: str
    country: str
    latitude: float
    longitude: float
    area_hectares: float
    target_crop: str

class AnalysisResponse(BaseModel):
    terreno_name: str
    estimated_area_hectares: float
    suitability_score: float
    recommendations: List[str]
    source: str