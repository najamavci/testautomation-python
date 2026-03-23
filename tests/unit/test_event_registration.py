import pytest
from src.registrations.event import Event
from src.registrations.member_service import MemberService


@pytest.mark.integration
def test_register_new_member_adds_member_to_service_and_event(mocker):
    member_service = MemberService()
    spy = mocker.spy(member_service, "add_member")
    event = Event(member_service=member_service)

    event.register_new_member("Charlie")

    spy.assert_called_once_with("Charlie")
    assert "Charlie" in member_service.members
    assert "Charlie" in event.members