from fastapi import APIRouter
from archipelago.api.routes import health, accu, recycling, geospatial, blockchain

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"], prefix="/health")
api_router.include_router(accu.router, tags=["accu"], prefix="/accu")
api_router.include_router(recycling.router, tags=["recycling"], prefix="/recycling")
api_router.include_router(geospatial.router, tags=["geospatial"], prefix="/geospatial")
api_router.include_router(blockchain.router, tags=["blockchain"], prefix="/blockchain")
