from bson import ObjectId
from src.modules.chat.services.send_message import send_message
from src.modules.chat.exceptions.unauthorized_user import UnauthorizedUser
from pytest import raises


class TestSendMessageService:
    def test_parse_an_empty_message_raise_error(self):
        '''
            check raises of function send_message when parses 
            an empty string or non parse message
        '''

        with raises(ValueError) as e_info:
            send_message(
                user_id='fake_user_id',
                chat_id='fake_chat_id',
                message=''
            )
            assert e_info.message == 'invalid message value'

    def test_raise_error_if_user_no_belongs_to_chat(self, chat_suject):
        fake_user_id = ObjectId()
        with raises(UnauthorizedUser) as e_info:
            send_message(
                message='test_message',
                user_id=str(fake_user_id),
                chat_id=str(chat_suject.inserted_id)
            )
            assert e_info.type is UnauthorizedUser
