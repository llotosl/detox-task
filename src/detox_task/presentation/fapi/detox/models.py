from pydantic import BaseModel


class CommentsModel(BaseModel):
    texts: tuple[str]


class ScoreModel(BaseModel):
    toxicity: list[float]
    severe_toxicity: list[float]
    obscene: list[float]
    identity_attack: list[float]
    insult: list[float]
    threat: list[float]
    sexual_explicit: list[float]
