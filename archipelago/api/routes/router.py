from fastapi import APIRouter
from archipelago.api.routes import heartbeat, accu, plastic

api_router = APIRouter()
api_router.include_router(heartbeat.router, tags=["health"], prefix="/health")
api_router.include_router(accu.router, tags=["accu"], prefix="/accu")
api_router.include_router(plastic.router, tags=["plastic"], prefix="/plastic")
