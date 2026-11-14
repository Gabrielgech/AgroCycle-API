from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from app.agronomy.catalog.crop_families import CropFamily

class CropModel(BaseModel):
    id: str = Field(..., description="Identificador único del cultivo")
    name: str = Field(..., description="Nombre común del cultivo")
    family: CropFamily = Field(..., description="Familia botánica para control de plagas y rotación")
    optimal_temp_min: float = Field(..., description="Temperatura mínima óptima en °C")
    optimal_temp_max: float = Field(..., description="Temperatura máxima óptima en °C")
    water_requirement_mm: float = Field(..., description="Requerimiento hídrico total aproximado en mm por ciclo")
    growing_season_days: int = Field(..., description="Duración promedio del ciclo de cultivo en días")
    nitrogen_fixing: bool = Field(False, description="Indica si la planta fija nitrógeno en el suelo")
    description: str = Field(..., description="Breve descripción agronómica")

# Catálogo base de cultivos para el MVP de AgroAdapt
CROP_CATALOG: Dict[str, CropModel] = {
    "maize": CropModel(
        id="maize",
        name="Maíz",
        family=CropFamily.GRAMINEAE,
        optimal_temp_min=18.0,
        optimal_temp_max=27.0,
        water_requirement_mm=500.0,
        growing_season_days=120,
        nitrogen_fixing=False,
        description="Cultivo básico de alta demanda nutricional, excelente para integrar con leguminosas."
    ),
    "bean": CropModel(
        id="bean",
        name="Frijol",
        family=CropFamily.LEGUMINOSAE,
        optimal_temp_min=16.0,
        optimal_temp_max=24.0,
        water_requirement_mm=350.0,
        growing_season_days=90,
        nitrogen_fixing=True,
        description="Leguminosa fijadora de nitrógeno; rompe ciclos de plagas de gramíneas y enriquece el suelo."
    ),
    "squash": CropModel(
        id="squash",
        name="Calabaza",
        family=CropFamily.CUCURBITACEAE,
        optimal_temp_min=20.0,
        optimal_temp_max=30.0,
        water_requirement_mm=400.0,
        growing_season_days=100,
        nitrogen_fixing=False,
        description="Cultivo de cobertura baja que ayuda a conservar la humedad superficial y suprimir arvenses."
    ),
    "sorghum": CropModel(
        id="sorghum",
        name="Sorgo",
        family=CropFamily.GRAMINEAE,
        optimal_temp_min=21.0,
        optimal_temp_max=32.0,
        water_requirement_mm=450.0,
        growing_season_days=110,
        nitrogen_fixing=False,
        description="Gran resistencia a condiciones de estrés hídrico y altas temperaturas."
    )
}

def get_crop_by_id(crop_id: str) -> Optional[CropModel]:
    """Obtiene la información detallada de un cultivo por su ID."""
    return CROP_CATALOG.get(crop_id.lower())

def get_all_crops() -> List[CropModel]:
    """Retorna la lista completa de cultivos disponibles en el catálogo."""
    return list(CROP_CATALOG.values())