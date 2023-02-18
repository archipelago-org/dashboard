from fastapi import FastAPI

from archipelago.api.routes.router import api_router
from archipelago.core.config import API_PREFIX, APP_NAME, APP_VERSION, IS_DEBUG


def get_app() -> FastAPI:
    fast_app = FastAPI(title=APP_NAME, version=APP_VERSION, debug=IS_DEBUG)
    fast_app.include_router(api_router, prefix=API_PREFIX)
    return fast_app


app = get_app()
