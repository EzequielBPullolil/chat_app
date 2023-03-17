from . import UserDomainException


class AlreadySingedNick(UserDomainException):
    def __init__(self, *args: object, nick):
        super().__init__(*args)
        self.message = str(f'the nick @{nick} is already singed')
