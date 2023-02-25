from pydantic import BaseModel


class RecyclingEfficiency(BaseModel):
    sequestration_efficiency: float
