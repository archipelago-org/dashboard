from fastapi import APIRouter
from archipelago.models.accu_price import AccuPriceResult
import archipelago.services.accu as accu_service


router = APIRouter()


@router.get("/price", response_model=AccuPriceResult, name="price")
def get_accu_spot_price() -> AccuPriceResult:
    accu_price: AccuPriceResult = accu_service.fetch_price()
    return accu_price
