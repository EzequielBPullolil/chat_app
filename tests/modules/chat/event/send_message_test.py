import pytest


class TestSendMessageEvent:
    def test_missing_user_id_raise_error(self, sio, chat_memebers):
        '''
            Check if missing user_id data param throw error
        '''
        sio.connect(namespace='/chats')
        with pytest.raises(ValueError) as e_info:
            sio.emit('send_message', {
                'chat_id': 'asdasdasdasd',
                'message': 'hi'
            }, namespace='/chats')
            assert 'missing user_id data param' in str(e_info.value)

    def test_missing_chat_id_raise_error(self, sio):

        sio.connect(namespace='/chats')
        assert sio.is_connected(namespace='/chats') == True
        with pytest.raises(ValueError) as e_info:
            sio.emit('send_message', {
                'user_id': 'asdasdsads',
                'message': 'hi'
            }, namespace='/chats')
            assert 'missing chat_id data param' in str(e_info.value)
