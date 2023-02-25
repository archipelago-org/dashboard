from fastapi import APIRouter
from archipelago.api.routes import heartbeat, accu, plastic, geo, xrpl

api_router = APIRouter()
api_router.include_router(heartbeat.router, tags=["health"], prefix="/health")
api_router.include_router(accu.router, tags=["accu"], prefix="/accu")
api_router.include_router(plastic.router, tags=["plastic"], prefix="/plastic")
api_router.include_router(geo.router, tags=["geo"], prefix="/geo")
api_router.include_router(xrpl.router, tags=["xrpl"], prefix="/xrpl")
