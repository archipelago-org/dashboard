from pydantic import BaseModel


class AccuPriceResponse(BaseModel):
    spot: int
