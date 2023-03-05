import socketio
import pytest

@pytest.fixture()
def sio():
    sio = socketio.AsyncClient(logger=True, engineio_logger=True)
    return sio