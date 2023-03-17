from src.databases.mongodb import user
from ..exceptions.already_singed_nick import AlreadySingedNick


def singed_user_nick(nick):
    result = user.find_one(filter={'nick': f'@{nick}'})

    if (result != None):
        raise AlreadySingedNick(nick=nick)
