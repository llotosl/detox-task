import abc
from collections.abc import Sequence

from detox_task.models.message_score import MessageScore


class MessageScoreRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, message_score: MessageScore) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self) -> Sequence[MessageScore]:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, message_score: MessageScore) -> None:
        raise NotImplementedError
