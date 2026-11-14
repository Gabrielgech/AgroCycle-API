from fastapi import APIRouter
from app.schemas.analysis import AnalysisResponse, ParcelInput
from app.services.analysis_service import analyze_parcel

router = APIRouter()

@router.post("/", response_model=AnalysisResponse)
def create_parcel_analysis(parcel_data: ParcelInput):
    """Recibe la información y el polígono de la parcela para calcular su superficie y viabilidad."""
    analysis_result = analyze_parcel(parcel_data)
    return analysis_result