class TestUserEvents:
    def test_send_message_emits_new_message(self, sios):
        '''
            Verify if user emits event 'send_message' to namespace /users 
            the server emits 'new_message' to all users 
        '''
        expected_message = 'hi'
        client1 = sios[0]
        client2 = sios[1]
        client1.connect(namespace='/users')
        client2.connect(namespace='/users')
        assert client1.is_connected(namespace='/users')
        assert client2.is_connected(namespace='/users')

        client1.emit('send_message', expected_message, namespace='/users')


        received = client1.get_received(namespace='/users')
        assert received[0]['name'] == 'new_message'
        assert received[0]['args'][0] == expected_message