import pytest
from src.registrations.event import Event


@pytest.mark.unit
def test_sign_up_adds_member_to_event():
    event = Event()
    event.sign_up("Alice")

    assert "Alice" in event.members
    assert len(event.members) == 1