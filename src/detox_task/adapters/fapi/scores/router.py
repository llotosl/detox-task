from typing import Annotated

from fastapi import APIRouter, Depends

from detox_task.adapters.fapi.scores.models import MessageScoreModel
from detox_task.application.get_message_scores.service import GetMessageScoresService
from detox_task.main.depends_stub import Stub

scores_router = APIRouter(prefix="/scores")


@scores_router.get("", response_model=list[MessageScoreModel])  # TODO: sorting by score values
def get_scores(
    get_message_scores_service: Annotated[
        GetMessageScoresService,
        Depends(Stub(GetMessageScoresService)),
    ],
) -> list[MessageScoreModel]:
    message_scores = get_message_scores_service.execute()

    return [MessageScoreModel.model_validate(message_score, from_attributes=True) for message_score in message_scores]
