from functools import lru_cache
from typing import Annotated, NoReturn

from detoxify import Detoxify
from fastapi import APIRouter, Depends, WebSocket
from starlette.websockets import WebSocketDisconnect

from detox_task.main.depends_stub import Stub
from detox_task.presentation.fapi.detox.models import CommentsModel, ScoreModel

detox_router = APIRouter()


@detox_router.post("/score-comments", response_model=ScoreModel)
def score_comments(
    comments: tuple[str],
    model: Annotated[
        Detoxify,
        Depends(Stub(Detoxify)),
    ],
) -> dict:
    return model_predict(model, comments)


@detox_router.websocket("/score-comments-ws")
async def score_comments_ws(
    websocket: WebSocket,
    model: Annotated[
        Detoxify,
        Depends(Stub(Detoxify)),
    ],
) -> None:
    await websocket.accept()

    try:
        await listen_comments(model, websocket)
    except WebSocketDisconnect:
        pass


async def listen_comments(model: Detoxify, websocket: WebSocket) -> NoReturn:
    while True:
        data = await websocket.receive_json()
        comments = CommentsModel(texts=data)  # TODO: send validation errors to ws

        score = model_predict(model, comments.texts)

        await websocket.send_json(score)


@lru_cache  # TODO: redis cache and use cache on endpoint instead of this function
def model_predict(
    model: Detoxify,
    texts: tuple[str],
) -> dict:
    return model.predict(texts)
