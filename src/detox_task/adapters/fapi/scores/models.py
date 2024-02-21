import uuid

from pydantic import BaseModel


class MessageModel(BaseModel):
    id: uuid.UUID
    text: str
    sender_id: uuid.UUID


class ScoreModel(BaseModel):
    toxicity: float
    severe_toxicity: float
    obscene: float
    identity_attack: float
    insult: float
    threat: float
    sexual_explicit: float


class MessageScoreModel(BaseModel):
    message: MessageModel
    score: ScoreModel
