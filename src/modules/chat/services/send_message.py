from bson import ObjectId
from ..exceptions.unauthorized_user import UnauthorizedUser
from ..helper.user_belongs_to_chat import user_belongs_to_chat

from src.databases.mongodb import chat


def send_message(chat_id, user_id, message):
    '''
        Try to add message to persisted chat

        1. Validate data keys
        2. Verify if user id belongs to chat
        3. create an instance of Message
        4. Find chat by id
        5. Add message instance to chat
    '''

    if (message == ''):
        raise ValueError('invalid message value')

    user = {
        '_id': ObjectId(user_id)
    }

    result = chat.find_one(filter={'_id': ObjectId(chat_id)})

    user_belongs_to_chat(
        user=user, chat=result
    )
