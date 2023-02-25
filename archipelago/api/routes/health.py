from fastapi import APIRouter

from archipelago.models.heartbeat import Hearbeat

router = APIRouter()


@router.get("/heartbeat", response_model=Hearbeat, name="heartbeat")
def get_hearbeat() -> Hearbeat:
    return Hearbeat(is_alive=True)
