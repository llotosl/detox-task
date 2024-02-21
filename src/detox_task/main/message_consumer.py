import asyncio
from concurrent.futures import ThreadPoolExecutor

from detox_task.application.score_message_consumer.consumer import ScoreMessageConsumer


def run_consumer(consumer: ScoreMessageConsumer) -> None:
    executor = ThreadPoolExecutor(max_workers=1)
    loop = asyncio.get_running_loop()
    loop.run_in_executor(executor, consumer.execute)
