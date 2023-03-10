from fastapi import APIRouter
from archipelago.models.object_location import ObjectLocations
from archipelago.services.object_location_service import ObjectLocationService

router = APIRouter()


@router.get("/object-locations", response_model=ObjectLocations, name="object_locations")
def get_location() -> ObjectLocations:
    return ObjectLocationService().get_locations()
