from flask_socketio import SocketIO
from flask import Flask

from .modules.user.event import UserNamespace

socketio = SocketIO()
def create_app():
    '''
        Creates
    '''
    app = Flask(__name__)


    socketio.init_app(app)

    socketio.on_namespace(UserNamespace('/users'))
    return app