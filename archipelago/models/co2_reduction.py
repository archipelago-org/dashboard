from pydantic import BaseModel


class Co2Reduction(BaseModel):
    sequestration: float
    abatement: float
    plastic_collected: float
    plastic_recycled: float
    accus_issued: int
