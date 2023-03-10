from src.modules.chat.helper.user_belongs_to_chat import user_belongs_to_chat
import pytest
from src.databases.mongodb import chat


class TestUsersBelongsToChatHelper:

    def test_raise_valueerror_if_chat_not_are_collection_instance(self, chat_suject):
        '''
            Throw error if chat param is not a dict
        '''

        with pytest.raises(ValueError) as e_info:
            user_belongs_to_chat(user={}, chat='a')

            assert e_info.message == "the 'chat' parameter is not a dict"
