from fastapi import APIRouter
from archipelago.models.accu_price import AccuPriceResponse
import archipelago.services.accu as accu_service


router = APIRouter()


@router.get("/price", response_model=AccuPriceResponse, name="price")
def get_accu_spot_price() -> AccuPriceResponse:
    accu_price: AccuPriceResponse = accu_service.fetch_price()
    return accu_price
