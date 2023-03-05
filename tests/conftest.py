import pytest
from src.app import create_app, socketio

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        'TESTING': True
    })

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def sio(app):
    flask_client = app.test_client()
    sio = socketio.test_client(
        app=app,
        flask_test_client=flask_client
    )
    return sio

@pytest.fixture()
def sios(app):
    sios = []
    for i in range(2):
        flask_client = app.test_client()
        sio = socketio.test_client(
            app=app,
            flask_test_client=flask_client
        )

        sios.append(sio)
        del sio
        del flask_client
    
    return sios