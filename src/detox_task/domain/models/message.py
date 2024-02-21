import uuid
from dataclasses import dataclass


@dataclass
class Message:
    id: uuid.UUID
    sender_id: uuid.UUID
    text: str
