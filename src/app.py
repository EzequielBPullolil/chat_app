from flask_socketio import SocketIO
from flask import Flask
from os import environ
from .modules.user.event import UserNamespace
from .modules.user.routes import user_bp
from .modules.chat.event import ChatNamespace
debbug = environ['PYTHONENV'] == 'test' or environ['PYTHONENV'] == 'dev'
socketio = SocketIO(logger=debbug, engineio_logger=debbug)

app = Flask(__name__)
socketio.init_app(app,  cors_allowed_origins="*")

app.register_blueprint(user_bp, url_prefix='/users')
# namespaces implement
socketio.on_namespace(UserNamespace('/users'))
socketio.on_namespace(ChatNamespace('/chats'))

app.url_map.strict_slashes = False
if __name__ == '__main__':
    socketio.run(app)
