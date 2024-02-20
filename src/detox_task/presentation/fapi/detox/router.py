from functools import lru_cache
from typing import Annotated

from detoxify import Detoxify
from fastapi import APIRouter, Depends

from detox_task.main.depends_stub import Stub
from detox_task.presentation.fapi.detox.models import CommentModel, ScoreModel

detox_router = APIRouter()


@lru_cache  # TODO: redis cache and use cache on endpoint instead of this function
def model_predict(
    model: Detoxify,
    texts: tuple[str],
) -> dict:
    return model.predict(texts)


@detox_router.post("/score-comment", response_model=ScoreModel)
def score_comment(
    comment: CommentModel,
    model: Annotated[
        Detoxify,
        Depends(Stub(Detoxify)),
    ],
) -> dict:
    return model_predict(model, comment.texts)
