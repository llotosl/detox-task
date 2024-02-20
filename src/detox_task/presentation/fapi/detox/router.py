from typing import Annotated

from detoxify import Detoxify
from fastapi import APIRouter, Depends

from detox_task.main.depends_stub import Stub
from detox_task.presentation.fapi.detox.models import CommentModel, ScoreModel

detox_router = APIRouter()


@detox_router.post("/score-comment", response_model=ScoreModel)
def score_comment(
    comment: CommentModel,
    model: Annotated[
        Detoxify,
        Depends(Stub(Detoxify)),
    ],
) -> dict:
    results = model.predict(
        comment.text,
    )
    return results
