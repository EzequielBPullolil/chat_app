# deps imports
from flask_socketio import Namespace, join_room, emit
from flask import request

# module imports
from .helper.user_belongs_to_chat import user_belongs_to_chat


class ChatNamespace(Namespace):
    def on_send_message(self, data):
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
            emit('new_message', {
                'username': data['username'],
                'message': data['message']
            }, to=data['chatid'])
        except KeyError:
            if (data.get('user_id', True)):
                raise ValueError('missing user_id data param')
            if (data.get('chat_id', True)):
                raise ValueError('missing chat_id data param')
            if (data.get('message', True)):
                raise ValueError('missing message data param')

    def on_join_chat(self, data):
        '''
            Verify if user with data['user_id'] are part
            of members of the chat with id == data['chat_id']
        '''
        user_id = data['user_id']
        chat_id = data['chat_id']

        user_belongs_to_chat(user_id=user_id, chat_id=chat_id)
        join_room(chat_id)
        print(f'user: {user_id} join to chat: {chat_id}')
