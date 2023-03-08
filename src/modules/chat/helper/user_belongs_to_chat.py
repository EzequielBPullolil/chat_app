from src.databases.mongodb import chat
from bson import ObjectId

from ..exceptions.unauthorized_user import UnauthorizedUser


def user_belongs_to_chat(chat_id, user_id):
    '''
        Return true if user are member of chat with chat_id

        chat_id and user_id has to be a no ObjectId instance
    '''
    if (type(chat_id) == ObjectId):
        raise Exception('chat_id must be non ObjectID param')

    if (type(user_id) == ObjectId):
        raise Exception('user_id must be non ObjectID param')

    chatid = ObjectId(chat_id)
    userid = ObjectId(user_id)
    result = chat.find_one(filter={'_id': chatid})

    members = result['members']

    for user in members:
        if (userid == user['_id']):
            return True

    raise UnauthorizedUser(chat_id=chat_id, user_id=user_id)
