from pydantic import BaseModel, Field
from typing import List

class CropRecommendationItem(BaseModel):
    crop_name: str = Field(..., description="Nombre del cultivo recomendado")
    crop_family: str = Field(..., description="Familia botánica para control de plagas y suelo")
    score: float = Field(..., ge=0, le=100, description="Puntuación de viabilidad del 0 al 100")
    benefits: List[str] = Field(..., description="Beneficios agronómicos de incluir este cultivo")
    risks: List[str] = Field(..., description="Riesgos climáticos o de manejo a considerar")

class RotationStrategyResponse(BaseModel):
    strategy_name: str = Field(..., description="Nombre de la estrategia (Ej: Diversificación y Salud de Suelo)")
    recommended_sequence: List[CropRecommendationItem] = Field(..., description="Secuencia ordenada de cultivos para la rotación")
    overall_score: float = Field(..., description="Calificación global de la estrategia")
    explanation: str = Field(..., description="Explicación en lenguaje claro del porqué de esta estrategia")