from app.schemas.analysis import AnalysisResponse, ParcelInput

def analyze_parcel(parcel_data: ParcelInput) -> AnalysisResponse:
    # Lógica de análisis simulada en memoria
    suitability = 89.5
    
    recommendations_list = [
        f"El terreno '{parcel_data.terreno_name}' ubicado en {parcel_data.municipality}, {parcel_data.state}, {parcel_data.country} presenta condiciones favorables para {parcel_data.target_crop}.",
        f"Con una superficie de {parcel_data.area_hectares} ha, se recomienda optimizar el riego en las coordenadas ({parcel_data.latitude}, {parcel_data.longitude}).",
        "Se sugiere integrar rotación con cultivos de cobertura para enriquecer el suelo."
    ]

    return AnalysisResponse(
        terreno_name=parcel_data.terreno_name,
        estimated_area_hectares=parcel_data.area_hectares,
        suitability_score=suitability,
        recommendations=recommendations_list,
        source="AgroAdapt Analytics Engine"
    )