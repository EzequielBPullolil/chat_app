from src.databases.mongodb import chat
from bson import ObjectId

from ..exceptions.unauthorized_user import UnauthorizedUser


def user_belongs_to_chat(chat_id, user_id):
    '''
        Return true if user are member of chat with chat_id
    '''
    result = chat.find_one(filter={'_id': ObjectId(chat_id)})

    members = result['members']

    for user in members:
        if (ObjectId(user_id) == user['_id']):
            return True

    raise UnauthorizedUser(chat_id=chat_id, user_id=user_id)
