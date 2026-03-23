class MemberService:
    def __init__(self):
        self.members = []

    def add_member(self, member_name):
        self.members.append(member_name)
        return member_name