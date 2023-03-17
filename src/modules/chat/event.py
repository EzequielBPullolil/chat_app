# deps imports
from bson import ObjectId
from flask_socketio import Namespace, join_room, emit
from flask import request

# module imports
from .helper.user_belongs_to_chat import user_belongs_to_chat

from src.databases.mongodb import chat
from .services.send_message import send_message


class ChatNamespace(Namespace):
    def on_send_message(self, data: dict):
        '''
            Emits to all users in the same chat
            the event 'new_message' and persist
            the message parsed by data

            1.validate data entrys
            2.verify if user belogns to chat
            3.persist menssage
        '''
        try:
            user_id = data['user_id']
            chat_id = data['chat_id']
            message = data['message']
            if (message == ''):
                raise ValueError('cannot be an empty string')

            send_message(chat_id, user_id, message)
            emit('new_message', {
                'username': 'temp name',
                'message': message
            }, to=chat_id)

        except KeyError:
            if (not 'user_id' in data):
                raise ValueError('missing user_id data param')
            if (not 'chat_id' in data):
                raise ValueError('missing chat_id data param')
            if (not 'message' in data):
                raise ValueError('missing message data param')

    def on_join_chat(self, data):
        '''
            Verify if user with data['user_id'] are part
            of members of the chat with id == data['chat_id']
        '''
        chat_id = data['chat_id']
        user_id = data['user_id']
        user = {
            '_id': ObjectId(user_id)
        }
        chat_param = chat.find_one(filter={'_id': ObjectId(chat_id)})

        user_belongs_to_chat(chat=chat_param, user=user)
        join_room(chat_id)
        print(f'user: {user_id} join to chat: {chat_id}')
