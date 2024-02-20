import functools
from collections.abc import Callable

from detoxify import Detoxify
from fastapi import FastAPI

from detox_task.main.depends_stub import Stub


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
    app.dependency_overrides[Stub(Detoxify)] = new_detoxify_model
