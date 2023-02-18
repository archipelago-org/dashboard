from pydantic import BaseModel


class Co2Result(BaseModel):
    sequestration: float
    abatement: float
    plastic_collected: float
    plastic_recycled: float
