import uuid

from detox_task.main.di import singleton


def test_singleton() -> None:
    singleton_uuid_fabric = singleton(uuid.uuid4)

    first_result = singleton_uuid_fabric()
    second_result = singleton_uuid_fabric()

    assert first_result is second_result
