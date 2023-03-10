from src.databases.mongodb import chat
from bson import ObjectId

from ..exceptions.unauthorized_user import UnauthorizedUser


def user_belongs_to_chat(chat, user):
    '''
        iterate the members property and
        check that the user parameter is in the list

        @param chat DICT
        @param user DICT

        @error UnauthorizedUser
        @return True
    '''

    if (type(chat) != dict):
        raise ValueError("the 'chat' parameter is not a dict")

    if (type(user) != dict):
        raise ValueError("the 'user' paramter is not a dict")

    members = chat['members']
    for user_i in members:
        print(user_i)
        if (user_i['_id'] == user['_id']):
            return True

    raise UnauthorizedUser(chat_id=chat['_id'], user_id=user['_id'])
