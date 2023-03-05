from flask_socketio import Namespace, ConnectionRefusedError
from flask_socketio import emit
class UserNamespace(Namespace):
    def on_connect(self, auth):
        if(auth == None): raise ConnectionRefusedError()

    def on_send_message(self, data):
        '''
            Emits event new_message and send
            dict with username and message sended
        '''

        print(f'User with username: "{data["username"]}" send message: "{data["message"]}"')
        emit('new_message',data)