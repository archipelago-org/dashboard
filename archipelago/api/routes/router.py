from fastapi import APIRouter
from archipelago.api.routes import heartbeat, accu_price

api_router = APIRouter()
api_router.include_router(heartbeat.router, tags=["health"], prefix="/health")
api_router.include_router(accu_price.router, tags=["accu_price"], prefix="/accu-price")
