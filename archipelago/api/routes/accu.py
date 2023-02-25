from fastapi import APIRouter
from archipelago.models.accu_info import AccuInfo
import archipelago.services.accu_service as accu_service


router = APIRouter()


@router.get("/info", response_model=AccuInfo, name="info")
def get_accu_info() -> AccuInfo:
    return accu_service.fetch_info()
