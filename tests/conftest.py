import pytest
from httpx import AsyncClient

from detox_task.main.web import app


@pytest.fixture(autouse=True)
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture
async def test_client() -> AsyncClient:
    async with AsyncClient(
        app=app,
        base_url="http://127.0.0.1:8000",  # TODO: .env variable
    ) as client:
        yield client
