from fastapi import APIRouter
from archipelago.models.accu_price import AccuPriceResult
import archipelago.services.accu_service as accu_service


router = APIRouter()


@router.get("/accu-spot-price", response_model=AccuPriceResult, name="accu_price")
def get_accu_spot_price() -> AccuPriceResult:
    accu_price: AccuPriceResult = accu_service.fetch_spot_price()
    return accu_price
