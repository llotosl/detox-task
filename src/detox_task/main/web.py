from fastapi import FastAPI

from detox_task.main.di import init_dependencies
from detox_task.presentation.fapi.detox.router import detox_router
from detox_task.presentation.fapi.index import index_router


def init_routers(app: FastAPI) -> None:
    app.include_router(index_router)
    app.include_router(detox_router, prefix="/detox")


def create_app() -> FastAPI:
    app = FastAPI()
    init_routers(app)
    init_dependencies(app)
    return app


app = create_app()
