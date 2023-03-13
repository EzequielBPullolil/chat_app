from bson import ObjectId
from src.modules.chat.services.send_message import send_message
from src.modules.chat.exceptions.unauthorized_user import UnauthorizedUser
from src.databases.mongodb import chat
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

    def test_message_added_to_messages_chat_list(self, chat_memebers):
        '''
            Verify if send_message add a message to chat_suject
        '''
        user = chat_memebers['members'][0]
        chat_id = chat_memebers['chat_id']

        assert len(chat_memebers['messages']) == 0

        send_message(message='hi', user_id=user, chat_id=chat_id)

        result = chat.find_one(filter={'_id': ObjectId(chat_id)})

        assert len(result['messages']) > 0

    def test_parse_id_of_unauthorizeduser_not_update_messages(self, chat_suject):

        chat_id = str(chat_suject.inserted_id)
        fake_user_id = str(ObjectId())

        with raises(UnauthorizedUser):
            send_message(chat_id=chat_id, user_id=fake_user_id, message='hi')
            result = chat.find_one(filter={'_id', chat_suject.inserted_id})

            assert len(result['messages']) == 0
