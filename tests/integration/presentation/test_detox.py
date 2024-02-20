from fastapi.testclient import TestClient

from detox_task.presentation.fapi.detox.models import ScoreModel


def test_detox_ws(fastapi_test_client: TestClient) -> None:
    with fastapi_test_client.websocket_connect("/detox/score-comments-ws") as ws:
        ws.send_json(["test"])
        data = ws.receive_json()

    ScoreModel(**data)
