import logging

import uvicorn
from fastapi import FastAPI

from detox_task.adapters.fapi.index import index_router
from detox_task.adapters.fapi.scores.router import scores_router
from detox_task.application.get_message_scores.service import GetMessageScoresService
from detox_task.main.depends_stub import Stub

logger = logging.getLogger(__name__)


def create_app(get_message_scores_service: GetMessageScoresService) -> FastAPI:
    app = FastAPI()
    init_routers(app)
    init_dependencies(app, get_message_scores_service)
    return app


def init_routers(app: FastAPI) -> None:
    app.include_router(index_router)
    app.include_router(scores_router)


def init_dependencies(app: FastAPI, get_message_scores_service: GetMessageScoresService) -> None:
    app.dependency_overrides[Stub(GetMessageScoresService)] = lambda: get_message_scores_service


async def run_api(app: FastAPI) -> None:
    config = uvicorn.Config(
        app,
        host="127.0.0.1",  # TODO: .env variables
        port=8000,
        log_level=logging.INFO,
    )
    server = uvicorn.Server(config)
    logger.info("Server started")
    await server.serve()
