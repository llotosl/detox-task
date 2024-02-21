import logging
import uuid
from functools import lru_cache

from detoxify import Detoxify

from detox_task.application.common.interfaces.broker import Broker
from detox_task.application.common.interfaces.score_message_repository import MessageScoreRepository
from detox_task.domain.models import Score
from detox_task.domain.models.message_score import MessageScore

logger = logging.getLogger(__name__)


class ScoreMessageConsumer:
    def __init__(
        self,
        model: Detoxify,
        message_score_repository: MessageScoreRepository,
        broker: Broker,
        messages_topic: str,
    ) -> None:
        self.__model = model
        self.__message_score_repository = message_score_repository
        self.__broker = broker
        self.__messages_topic = messages_topic

    def execute(self) -> None:
        for message in self.__broker.consume_from(self.__messages_topic):
            logger.info("Predict message %s", message.id)

            score = self.__predict(message.text)

            message_score = MessageScore(
                id=uuid.uuid4(),
                message=message,
                score=Score(**score),
            )

            self.__message_score_repository.save(message_score)

    @lru_cache  # noqa: B019 TODO: add redis cache
    def __predict(self, text: str) -> dict:
        return self.__model.predict(text)
