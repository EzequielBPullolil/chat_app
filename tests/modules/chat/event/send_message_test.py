import pytest
from bson import ObjectId

from src.modules.chat.exceptions.unauthorized_user import UnauthorizedUser


class TestSendMessageEvent:
    def test_missing_user_id_raise_exception(self, sio):
        '''
            Check if missing user_id data param throw error
        '''
        sio.connect(namespace='/chats')
        assert sio.is_connected(namespace='/chats') == True

        with pytest.raises(ValueError) as e_info:
            sio.emit('send_message', {
                'chat_id': 'asdasdasdasd',
                'message': 'hi'
            }, namespace='/chats')
            assert 'missing user_id data param' in str(e_info.value)

    def test_missing_chat_id_raise_exception(self, sio):

        sio.connect(namespace='/chats')
        assert sio.is_connected(namespace='/chats') == True
        with pytest.raises(ValueError) as e_info:
            sio.emit('send_message', {
                'user_id': 'asdasdsads',
                'message': 'hi'
            }, namespace='/chats')
            assert 'missing chat_id data param' in str(e_info.value)

    def test_missing_message_raise_exception(self, sio):
        sio.connect(namespace='/chats')
        assert sio.is_connected(namespace='/chats') == True
        with pytest.raises(ValueError) as e_info:
            sio.emit('send_message', {
                'user_id': 'asdasdsads',
                'chat_id': 'asdasd'
            }, namespace='/chats')
            assert 'missing message data param' in str(e_info.value)

    def test_send_unrelated_chat_and_user_id_raise_exception(self, sio, chat_suject):
        '''
            check if send an fake user_id and persisted chat raise exception
        '''

        fake_user_id = str(ObjectId())
        chat_id = str(chat_suject.inserted_id)

        sio.connect(namespace='/chats')
        assert sio.is_connected(namespace='/chats') == True
        with pytest.raises(UnauthorizedUser) as e_info:
            sio.emit('send_message', {
                'chat_id': chat_id,
                'user_id': fake_user_id,
                'message': 'hi'
            }, namespace='/chats')
            assert e_info.type == UnauthorizedUser
