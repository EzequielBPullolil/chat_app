from flask_socketio import SocketIO
from flask import Flask
from os import environ
from .modules.user.event import UserNamespace
debbug = environ['PYTHONENV'] == 'test' or environ['PYTHONENV'] == 'dev'
socketio = SocketIO(logger=debbug, engineio_logger=debbug)
def create_app():
    '''
        Creates
    '''
    app = Flask(__name__)


    socketio.init_app(app)

    socketio.on_namespace(UserNamespace('/users'))
    return app