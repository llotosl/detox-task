from collections.abc import Sequence

from detox_task.application.common.interfaces.score_message_repository import MessageScoreRepository
from detox_task.domain.models.message_score import MessageScore


class GetMessageScoresService:
    def __init__(self, message_score_repository: MessageScoreRepository) -> None:
        self.__message_score_repository = message_score_repository

    def execute(self) -> Sequence[MessageScore]:
        return self.__message_score_repository.get()
