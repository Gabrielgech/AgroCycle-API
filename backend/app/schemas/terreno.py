from pydantic import BaseModel
from typing import Optional

class TerrenoCreate(BaseModel):
    terreno_name: str
    municipality: str
    state: str
    country: str
    latitude: float
    longitude: float
    area_hectares: float
    target_crop: str

class TerrenoUpdate(BaseModel):
    terreno_name: Optional[str] = None
    municipality: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    area_hectares: Optional[float] = None
    target_crop: Optional[str] = None