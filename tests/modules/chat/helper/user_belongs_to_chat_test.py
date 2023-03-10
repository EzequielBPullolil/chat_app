from bson import ObjectId
from src.modules.chat.helper.user_belongs_to_chat import user_belongs_to_chat
import pytest
from src.databases.mongodb import chat
from src.modules.chat.exceptions.unauthorized_user import UnauthorizedUser


class TestUsersBelongsToChatHelper:
    def test_raise_valueerror_if_chat_not_are_collection_instance(self):
        '''
            Throw error if chat param is not a dict
        '''

        with pytest.raises(ValueError) as e_info:
            user_belongs_to_chat(user={}, chat='a')

            assert e_info.message == "the 'chat' parameter is not a dict"

    def test_raise_valueerror_if_user_not_are_collection_instace(self):
        with pytest.raises(ValueError) as e_info:
            user_belongs_to_chat(chat={}, user='a')

            assert e_info.message == "the 'user' parameter is not a dict"

    def test_passing_an_unrelated_user_and_chat_raise_UnauthorizedUser(self, chat_suject):
        '''
            check if parse an user who arent part of chat members
            as params of user_belongs_to_chat raise UnauthorizedUser
            exception
        '''
        user = {
            '_id': ObjectId()
        }
        chat_param = chat.find_one(filter={'_id': chat_suject.inserted_id})

        with pytest.raises(UnauthorizedUser) as e_info:
            user_belongs_to_chat(user=user, chat=chat_param)

            assert e_info.message == f"the user with id {user['_id']} arent part of chat with id {chat_param['_id']}"
