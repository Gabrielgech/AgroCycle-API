from app.schemas.rotation import RotationStrategyResponse, CropRecommendationItem

def calculate_crop_rotation(target_crop: str) -> RotationStrategyResponse:
    """
    Genera una estrategia de rotación agronómica basada en el cultivo objetivo,
    siguiendo principios de alternancia de familias y regeneración de suelos.
    """
    target = target_crop.lower()
    
    if target in ["maize", "maíz"]:
        return RotationStrategyResponse(
            strategy_name="Estrategia Milpa Regenerativa (Gramínea - Leguminosa - Cucurbitácea)",
            recommended_sequence=[
                CropRecommendationItem(
                    crop_name="Maíz",
                    crop_family="Gramíneas (Cereales)",
                    score=85.0,
                    benefits=["Alto rendimiento y adaptación al clima regional"],
                    risks=["Alta demanda de nutrientes (Nitrógeno)"]
                ),
                CropRecommendationItem(
                    crop_name="Frijol",
                    crop_family="Leguminosas (Fijadoras de Nitrógeno)",
                    score=95.0,
                    benefits=["Fija nitrógeno atmosférico de forma natural", "Rompe ciclos biológicos de plagas de gramíneas"],
                    risks=["Sensibilidad a encharcamientos temporales"]
                ),
                CropRecommendationItem(
                    crop_name="Calabaza",
                    crop_family="Cucurbitáceas",
                    score=90.0,
                    benefits=["Cubre la superficie del suelo", "Reduce la evaporación de humedad y suprime malezas"],
                    risks=["Requiere monitoreo de humedad para evitar hongos foliares"]
                )
            ],
            overall_score=92.5,
            explanation="Secuencia óptima inspirada en el sistema tradicional de la Milpa. El maíz aprovecha los nutrientes, el frijol restituye el nitrógeno al suelo y la calabaza protege la superficie contra la desecación solar."
        )
    else:
        return RotationStrategyResponse(
            strategy_name="Estrategia de Diversificación y Resiliencia Climática",
            recommended_sequence=[
                CropRecommendationItem(
                    crop_name="Sorgo",
                    crop_family="Gramíneas (Cereales)",
                    score=82.0,
                    benefits=["Gran resistencia a altas temperaturas y sequía temporal"],
                    risks=["Agotamiento relativo del suelo si se cultiva continuamente"]
                ),
                CropRecommendationItem(
                    crop_name="Frijol",
                    crop_family="Leguminosas (Fijadoras de Nitrógeno)",
                    score=90.0,
                    benefits=["Mejora la fertilidad biológica y estructura del suelo"],
                    risks=["Requiere ventana de lluvia o riego inicial"]
                )
            ],
            overall_score=86.0,
            explanation="Combinación enfocada en terrenos con restricciones hídricas moderadas, alternando un cereal resistente con una leguminosa mejoradora de suelo."
        )