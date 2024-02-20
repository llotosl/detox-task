from fastapi import FastAPI, APIRouter, Depends
from pydantic import BaseModel
from detoxify import Detoxify
import logging
from typing import Callable, Annotated
import functools


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

def singleton(func: Callable) -> Callable:
    last_result = None
    
    @functools.wraps(func)
    def wrapper(*args: object, **kwargs: object) -> object:
        nonlocal last_result
        
        if last_result is None:
            last_result = func(*args, **kwargs)
        
        return last_result
        
    return wrapper

@singleton
def new_detoxify_model() -> Detoxify:
    return Detoxify("multilingual")

def init_dependencies(app: FastAPI) -> None:
    app.dependency_overrides[Detoxify] = new_detoxify_model

def create_app() -> FastAPI:
    app = FastAPI()
    init_routers(app)
    return app


app = create_app()