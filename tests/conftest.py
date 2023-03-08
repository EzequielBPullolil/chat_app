import pytest
from src.app import app, socketio
from src.databases.mongodb import chat


@pytest.fixture()
def chat_suject():
    result = chat.insert_one({
        'name': 'chat_test',
        'members': [],
        'messages': []
    })

    return result


@pytest.fixture()
def flask_app():
    global app
    app.config.update({
        'TESTING': True
    })

    yield app


@pytest.fixture()
def client(flask_app):
    return app.test_client()


@pytest.fixture()
def sio(flask_app):
    flask_client = flask_app.test_client()
    sio = socketio.test_client(
        app=flask_app,
        flask_test_client=flask_client
    )
    return sio


@pytest.fixture()
def sios(flask_app):
    sios = []
    for i in range(3):
        flask_client = flask_app.test_client()
        sio = socketio.test_client(
            app=flask_app,
            flask_test_client=flask_client
        )

        sios.append(sio)
        del sio
        del flask_client

    return sios
