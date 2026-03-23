import pytest
from src.registrations.member_service import MemberService


@pytest.mark.unit
def test_add_member_adds_member_to_member_list(mocker):
    service = MemberService()
    spy = mocker.spy(service, "add_member")

    result = service.add_member("Bob")

    spy.assert_called_once_with("Bob")
    assert result == "Bob"
    assert "Bob" in service.members
    assert len(service.members) == 1