from pydantic import BaseModel


class Co2Response(BaseModel):
    sequestration: float
    abatement: float
    plastic_collected: float
    plastic_recycled: float
    accus_issued: int


class EfficiencyResponse(BaseModel):
    sequestration_efficiency: float
