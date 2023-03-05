from flask_socketio import Namespace
from flask_socketio import emit
class UserNamespace(Namespace):
    def on_send_message(self, message):
        '''
            Emits new_message event to 
            all users in the same room
        '''

        emit('new_message', message)