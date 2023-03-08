class TestChatEvents:
    def test_send_messsage_to_chat(self, sios):
        '''
            Emit send_message event in chat namespace
            catch chats id and emit new_message to
            all users in the same chat
        '''
        chatid = 'test'
        client1 = sios[0]
        client2 = sios[1]

        # users connect socket
        client1.connect(namespace='/chats')
        assert client1.is_connected() == True
        client2.connect(namespace='/chats')
        assert client2.is_connected() == True

        # users join chat
        client1.emit('join_chat', chatid, namespace='/chats')
        client2.emit('join_chat', chatid, namespace='/chats')

        client1.emit('send_message', {
            'message': 'hi',
            'username': 'client1',
            'chatid': chatid
        }, namespace='/chats')

        received = client2.get_received(namespace='/chats')
        print(received)

        assert received[0]['name'] == 'new_message'
        assert received[0]['args'][0]['username'] == 'client1'

    def test_users_who_arent_part_of_chat_no_receive_new_message_event(self, sios):
        '''
            Check if only the users in the same chat receive the event
            'new_message'
        '''
        chatid = 'test_chat'
        client1 = sios[0]
        client2 = sios[1]
        client_out_of_chat = sios[2]

        # clients join chat
        client1.connect(namespace='/chats')
        client2.connect(namespace='/chats')
        client_out_of_chat.connect(namespace='/chats')

        # verify clients connection
        assert client1.is_connected() == True
        assert client2.is_connected() == True
        assert client_out_of_chat.is_connected() == True
        # client1 and client2 join chat
        client1.emit('join_chat', chatid, namespace='/chats')
        client2.emit('join_chat', chatid, namespace='/chats')
        # client emit message
        client1.emit('send_message', {
            'message': 'hi',
            'username': 'client1',
            'chatid': chatid
        }, namespace='/chats')

        received = client_out_of_chat.get_received(namespace='/chats')

        assert len(received) == 0
