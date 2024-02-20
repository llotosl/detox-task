from detox_task.main.web import singleton
import uuid

def test_singleton():
    singleton_uuid_fabric = singleton(uuid.uuid4)
    
    first_result = singleton_uuid_fabric()
    second_result = singleton_uuid_fabric()
    
    assert first_result is second_result