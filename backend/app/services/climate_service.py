from app.schemas.climate import ClimateDataResponse

def get_nasa_climate_data(lat: float, lon: float) -> ClimateDataResponse:
    """
    Simula la consulta y procesamiento de los datos de la NASA POWER 
    para la ubicación solicitada (por defecto Mérida, Yucatán: lat 20.97, lon -89.62).
    """
    # Valores base extraídos del reporte de la NASA POWER para la zona
    return ClimateDataResponse(
        latitude=lat,
        longitude=lon,
        temperature_avg=26.73,  # Temperatura promedio anual de referencia en °C
        rainfall_total=1107.0,  # Precipitación total anual acumulada en mm
        soil_moisture=0.60,     # Humedad promedio de la zona radicular (GWETROOT)
        source="NASA POWER / MERRA-2 (Agroclimatology)"
    )