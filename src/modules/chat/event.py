from flask_socketio import Namespace, join_room, emit
from flask import request


class ChatNamespace(Namespace):
    globalid = 'chatidexample'

    def on_send_message(self, data):
        emit('new_message', data, to=self.globalid)

    def on_connect(self):
        join_room(self.globalid)
        print(f'user enter to room')
