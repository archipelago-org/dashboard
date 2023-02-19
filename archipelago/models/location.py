from pydantic import BaseModel
from typing import List


class Location(BaseModel):
    latitude: float
    longitude: float
    weight: float
    product: str


class LocationResponse(BaseModel):
    locations: List[Location]
