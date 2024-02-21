from httpx import AsyncClient


async def test_healthcheck(test_client: AsyncClient) -> None:
    response = await test_client.get("/")

    assert response.status_code == 200
