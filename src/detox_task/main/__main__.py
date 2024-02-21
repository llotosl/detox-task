import asyncio
import logging
import uuid

from detoxify import Detoxify

from detox_task.adapters.broker.in_memory.broker import InMemoryBroker
from detox_task.adapters.db.in_memory.message_score_repository import InMemoryMessageScoreRepository
from detox_task.application.get_scores.service import GetMessageScoresService
from detox_task.application.score_message_consumer.consumer import ScoreMessageConsumer
from detox_task.main.message_consumer import run_consumer
from detox_task.main.web import create_app, run_api
from detox_task.models.message import Message

logger = logging.getLogger(__name__)


async def main() -> None:
    model = Detoxify("multilingual")  # TODO: use di-framework for dependency injection
    messages_topic = "messages"
    message_score_repository = InMemoryMessageScoreRepository()
    broker = build_brocker(messages_topic)
    get_message_scores_service = GetMessageScoresService(
        message_score_repository=message_score_repository,
    )

    app = create_app(get_message_scores_service)
    consumer = ScoreMessageConsumer(
        model=model,
        message_score_repository=message_score_repository,
        broker=broker,
        messages_topic=messages_topic,
    )

    run_consumer(consumer)
    await run_api(app)


def build_brocker(messages_topic: str) -> InMemoryBroker:
    broker = InMemoryBroker()
    for _ in range(5):  # TODO: delete it, it needs only for consumer working demonstration
        broker.produce_to(
            messages_topic,
            Message(
                id=uuid.uuid4(),
                sender_id=uuid.uuid4(),
                text="abc",
            ),
        )

    return broker


if __name__ == "__main__":
    asyncio.run(main())
