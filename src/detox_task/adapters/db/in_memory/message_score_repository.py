from collections.abc import Sequence

from detox_task.application.common.interfaces.score_message_repository import MessageScoreRepository
from detox_task.models.message_score import MessageScore


class InMemoryMessageScoreRepository(MessageScoreRepository):
    def __init__(self) -> None:
        self.__db = {}

    def save(self, message_score: MessageScore) -> None:
        self.__db[message_score.id] = message_score

    def get(self) -> Sequence[MessageScore]:
        return tuple(self.__db.values())

    def delete(self, message_score: MessageScore) -> None:
        self.__db.pop(message_score.id)
