class TestChatEvents:
    def test_send_messsage_to_chat(self, sios, chatid):
        '''
            Emit send_message event in chat namespace
            catch chats id and emit new_message to 
            all users in the same chat
        '''
        client1 = sios[0]
        client2 = sios[1]

        client1.connect(namespace='/chats')
        client2.connect(namespace='/chats')

        assert client1.is_connected() == True
        assert client2.is_connected() == True

        client1.emit('send_message', {
            'message': 'hi',
            'username': 'client1'
        }, namespace='/chats')

        received = client2.get_received(namespace='/chats')

        assert received[0]['name'] == 'new_message'
        assert received[0]['args'][0]['username'] == 'client1'
