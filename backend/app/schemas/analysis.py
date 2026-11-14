from pydantic import BaseModel, Field
from typing import List

class CoordinatePoint(BaseModel):
    lat: float = Field(..., description="Latitud del punto")
    lon: float = Field(..., description="Longitud del punto")

class ParcelAnalysisRequest(BaseModel):
    parcel_name: str = Field(..., min_length=2, max_length=100, description="Nombre identificador de la parcela")
    coordinates: List[CoordinatePoint] = Field(..., description="Lista de coordenadas que forman el polígono del terreno")
    target_crop: str = Field(..., description="Cultivo principal que el agricultor tiene en mente")

class AnalysisResponse(BaseModel):
    parcel_name: str
    area_hectares: float = Field(..., description="Superficie calculada del terreno en hectáreas")
    status: str = Field("success", description="Estado del análisis espacial")
    message: str