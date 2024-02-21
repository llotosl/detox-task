import uuid
from dataclasses import dataclass

from detox_task.models.message import Message
from detox_task.models.score import Score


@dataclass
class MessageScore:
    id: uuid.UUID
    message: Message
    score: Score
