from pydantic import BaseModel
from typing import List


class ObjectLocation(BaseModel):
    latitude: float
    longitude: float
    weight: float
    quantity: int
    product: str


class ObjectLocations(BaseModel):
    locations: List[ObjectLocation]
