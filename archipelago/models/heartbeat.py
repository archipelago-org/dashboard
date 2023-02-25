from pydantic import BaseModel


class Hearbeat(BaseModel):
    is_alive: bool
