import abc
from collections.abc import Iterable
from typing import Any


class Broker(abc.ABC):  # TODO: think about broker interface, divide it to consumer and producer interfaces
    @abc.abstractmethod
    def consume_from(self, topic: str) -> Iterable[Any]:  # noqa: ANN401
        raise NotImplementedError

    @abc.abstractmethod
    def produce_to(self, topic: str, message: Any) -> None:  # noqa: ANN401
        raise NotImplementedError
