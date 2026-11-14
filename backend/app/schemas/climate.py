from pydantic import BaseModel, Field
from typing import Optional

class ClimateDataResponse(BaseModel):
    latitude: float = Field(..., description="Latitud de la parcela analizada")
    longitude: float = Field(..., description="Longitud de la parcela analizada")
    temperature_avg: float = Field(..., description="Temperatura promedio en grados Celsius")
    rainfall_total: float = Field(..., description="Precipitación total acumulada en mm")
    soil_moisture: Optional[float] = Field(None, description="Nivel de humedad superficial del suelo")
    source: str = Field("NASA POWER / GPM", description="Fuente de los datos satelitales")

    class Config:
        from_attributes = True