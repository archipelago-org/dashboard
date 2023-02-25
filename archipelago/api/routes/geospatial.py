from fastapi import APIRouter
import archipelago.services.object_location_service as location_service
from archipelago.models.object_location import ObjectLocations

router = APIRouter()


@router.get("/object-locations", response_model=ObjectLocations, name="object_locations")
def get_location() -> ObjectLocations:
    return location_service.get_locations()
