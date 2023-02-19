

from pydantic import BaseModel


class HearbeatResponse(BaseModel):
    is_alive: bool
