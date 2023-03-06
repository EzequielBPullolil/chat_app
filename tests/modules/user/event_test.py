from flask_socketio import ConnectionRefusedError
class TestUserEvents:
    def test_cant_connect_without_auth_params(self, sio):
        '''
            Verify if try connect to namespace /users
            without auth param refuse connection 
        '''
        sio.connect(namespace='/users')
        assert sio.is_connected(namespace='/users') == False

        sio.connect(namespace='/users', auth={
            'name': 'test'
        })
        assert sio.is_connected(namespace='/users') == True

    def test_send_message_emits_new_message_event(self, sios):
        '''
            Verify if user emits event 'send_message' to namespace /users 
            the server emits 'new_message' to all users 
        '''
        expected_message = 'hi'
        client1 = sios[0]
        client2 = sios[1]
        client1.connect(namespace='/users', auth={
            "name": 'client1'
        })
        client2.connect(namespace='/users', auth={
            "name": 'client2'
        })
        assert client1.is_connected(namespace='/users') == True
        assert client2.is_connected(namespace='/users') == True

        client1.emit('send_message', {
            "message": expected_message,
            "username": "client1"
        }, namespace='/users')
        received = client1.get_received(namespace='/users')
        assert received[0]['name'] == 'new_message'
        assert received[0]['args'][0]['message'] == expected_message
        assert received[0]['args'][0]['username'] == 'client1'