from fastapi import APIRouter
from archipelago.models.co2 import Co2Response
import archipelago.services.co2 as co2_service


router = APIRouter()


@router.get("/co2", response_model=Co2Response, name="co2")
def get_co2() -> Co2Response:
    co2: Co2Response = co2_service.get_co2()
    return co2
