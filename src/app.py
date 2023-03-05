from flask_socketio import SocketIO
from flask import Flask

socketio = SocketIO()
def create_app():
    '''
        Creates
    '''
    app = Flask(__name__)


    socketio.init_app(app)

    return app