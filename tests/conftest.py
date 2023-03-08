from bson import ObjectId
import pytest
from src.app import app, socketio
from src.databases.mongodb import chat


def pytest_configure():
    '''
        Delete all rows in databases
    '''
    chat.delete_many({})
    print('all chats deleted')


@pytest.fixture()
def chat_suject():
    result = chat.insert_one({
        'name': 'chat_test',
        'members': [],
        'messages': []
    })

    return result


@pytest.fixture()
def chat_memebers():
    '''
        Insert  chat with members and return
        the chat _id and list of members ID
    '''
    members = [
        {
            '_id': ObjectId(),
            'name': 'client1'
        },
        {
            '_id': ObjectId(),
            'name': 'client2'
        }
    ]
    result = chat.insert_one({
        'name': 'chat_test',
        'members': members,
        'messages': []
    })
    return {
        'chat_id': str(result.inserted_id),
        'members': [str(members[0]['_id']), str(members[1]['_id'])]
    }


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
