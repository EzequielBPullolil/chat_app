from flask_socketio import Namespace, join_room, emit
from flask import request


class ChatNamespace(Namespace):

    def on_send_message(self, data):
        '''
            Emits to all users in the same chat 
            the event 'new_message' 
        '''
        if (data['chatid'] == None):
            raise Exception('Missing chatid')
        emit('new_message', {
            'username': data['username'],
            'message': data['message']
        }, to=data['chatid'])

    def on_join_chat(self, chatid):
        join_room(chatid)
        print(f'user join to chat {chatid}')
