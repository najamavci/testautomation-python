from src.registrations.member_service import MemberService


class Event:
    def __init__(self, member_service=None):
        self.members = []
        self.member_service = member_service if member_service else MemberService()

    def sign_up(self, member_name):
        self.members.append(member_name)

    def register_new_member(self, member_name):
        self.member_service.add_member(member_name)
        self.sign_up(member_name)