from fastapi import APIRouter
from archipelago.models.accu_info import AccuInfo
from archipelago.services.accu_service import AccuService


router = APIRouter()


@router.get("/info", response_model=AccuInfo, name="info")
def get_accu_info() -> AccuInfo:
    return AccuService().fetch_info()
