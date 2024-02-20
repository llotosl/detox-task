from pydantic import BaseModel


class CommentModel(BaseModel):
    text: str


class ScoreModel(BaseModel):
    toxicity: float
    severe_toxicity: float
    obscene: float
    identity_attack: float
    insult: float
    threat: float
    sexual_explicit: float
