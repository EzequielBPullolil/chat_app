from flask_socketio import SocketIO
from flask import Flask
from os import environ
from .modules.user.event import UserNamespace
from .modules.chat.event import ChatNamespace
debbug = environ['PYTHONENV'] == 'test' or environ['PYTHONENV'] == 'dev'
socketio = SocketIO(logger=debbug, engineio_logger=debbug)

app = Flask(__name__)
socketio.init_app(app,  cors_allowed_origins="*")

# namespaces implement
socketio.on_namespace(UserNamespace('/users'))
socketio.on_namespace(ChatNamespace('/chats'))

if __name__ == '__main__':
    socketio.run(app)
