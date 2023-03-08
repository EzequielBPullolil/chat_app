from pytest import raises
from src.modules.chat.exceptions.unauthorized_user import UnauthorizedUser


class TestChatEvents:
    def test_trying_to_join_chat_we_are_not_part_of_raise_exception(self, sio, chat_suject):
        '''
            Check if user aren part of chat the event 'join_chat' raise exception
        '''
        client1 = sio
        client1.connect(namespace='/chats')
        assert client1.is_connected() == True
        with raises(UnauthorizedUser) as exception:
            client1.emit('join_chat', {
                'user_id': 'asdiasdiasdniasda',
                'chat_id': str(chat_suject.inserted_id)
            }, namespace='/chats')
            assert exception.type is UnauthorizedUser

    def test_send_messsage_to_chat(self, sios, chat_memebers):
        '''
            Emit send_message event in chat namespace
            catch chats id and emit new_message to
            all users in the same chat
        '''
        chatid = chat_memebers['chat_id']
        client1_sio = sios[0]
        client2_sio = sios[1]

        client1_id = chat_memebers['members'][0]
        client2_id = chat_memebers['members'][1]

        # users connect socket
        client1_sio.connect(namespace='/chats')
        assert client1_sio.is_connected() == True
        client2_sio.connect(namespace='/chats')
        assert client2_sio.is_connected() == True

        # users join chat
        client1_sio.emit('join_chat', {
            'user_id': client1_id,
            'chat_id': chatid
        }, namespace='/chats')
        client2_sio.emit('join_chat', {
            'user_id': client2_id,
            'chat_id': chatid
        }, namespace='/chats')

        client1_sio.emit('send_message', {
            'message': 'hi',
            'username': 'client1',
            'chatid': chatid
        }, namespace='/chats')

        received = client2_sio.get_received(namespace='/chats')
        print(received)

        assert received[0]['name'] == 'new_message'
        assert received[0]['args'][0]['username'] == 'client1'

    def test_users_who_arent_part_of_chat_no_receive_new_message_event(self, sios, chat_memebers):
        '''
            Check if only the users in the same chat receive the event
            'new_message'
        '''
        chatid = chat_memebers['chat_id']
        client1_sio = sios[0]
        client2_sio = sios[1]
        client_out_of_chat = sios[2]
        client1_id = chat_memebers['members'][0]
        client2_id = chat_memebers['members'][1]

        # clients join chat
        client1_sio.connect(namespace='/chats')
        client2_sio.connect(namespace='/chats')
        client_out_of_chat.connect(namespace='/chats')

        # verify clients connection
        assert client1_sio.is_connected() == True
        assert client2_sio.is_connected() == True
        assert client_out_of_chat.is_connected() == True
        # client1 and client2 join chat
        client1_sio.emit('join_chat',
                         {
                             'chat_id': chatid,
                             'user_id': client1_id
                         }, namespace='/chats')
        client2_sio.emit('join_chat',
                         {
                             'chat_id': chatid,
                             'user_id': client2_id
                         }, namespace='/chats')
        # client emit message
        client1_sio.emit('send_message', {
            'message': 'hi',
            'username': 'client1',
            'chatid': chatid
        }, namespace='/chats')

        received = client_out_of_chat.get_received(namespace='/chats')

        assert len(received) == 0
