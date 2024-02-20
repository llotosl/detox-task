from fastapi import FastAPI, APIRouter, Depends
from pydantic import BaseModel
from detoxify import Detoxify
import logging
from typing import Annotated

app = FastAPI()
router = APIRouter(prefix="/detoxify")


class Comment(BaseModel):
    text: str


class Score(BaseModel):
    score: int


@router.post("/score-comment")
def score_comment(comment: Comment, model: Annotated[Detoxify, Depends()]) -> dict:
    results = model.predict(
        [
            comment.text,
        ]
    )
    return results


logger = logging.getLogger(__name__)

def init_routers(app: FastAPI) -> None:
    app.include_router(router)


def create_app() -> FastAPI:
    app = FastAPI()
    init_routers(app)
    return app


app = create_app()