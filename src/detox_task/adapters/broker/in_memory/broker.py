from collections import defaultdict
from collections.abc import Iterable
from queue import Queue
from typing import Any

from detox_task.application.common.interfaces.broker import Broker


class InMemoryBroker(Broker):
    def __init__(self) -> None:
        self.__queues: dict[str, Queue] = defaultdict(Queue)

    def consume_from(self, topic: str) -> Iterable[Any]:
        while True:
            yield self.__queues[topic].get()

    def produce_to(self, topic: str, message: Any) -> None:  # noqa: ANN401
        self.__queues[topic].put(message)
