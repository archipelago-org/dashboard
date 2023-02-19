from fastapi import APIRouter
import archipelago.services.location as location_service
from archipelago.models.location import LocationResponse

router = APIRouter()


@router.get("/location", response_model=LocationResponse, name="location")
def get_location() -> LocationResponse:
    locations = location_service.get_location()
    return locations
