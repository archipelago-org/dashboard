from fastapi import APIRouter

from archipelago.models.heartbeat import HearbeatResponse

router = APIRouter()


@router.get("/heartbeat", response_model=HearbeatResponse, name="heartbeat")
def get_hearbeat() -> HearbeatResponse:
    heartbeat = HearbeatResponse(is_alive=True)
    return heartbeat
