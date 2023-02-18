from pydantic import BaseModel


class AccuPriceResult(BaseModel):
    spot: int
