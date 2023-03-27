from bson import ObjectId
from src.databases.mongodb import user
from src.modules.user.services.persist_user import persist_user
import pytest


class TestPersistUserService:
    def test_user_was_persisted(self):
        '''
            Validates if user are correctly persisted
        '''
        persisted_user = persist_user(
            name='a test name', password='a test password', nick='test')

        is_persisted = user.find_one(filter={
            '_id': ObjectId(persisted_user['_id'])
        })
        assert is_persisted != None

    def test_user_password_was_encripted(self):
        '''
            Persist user and check if the password
            was encripted
        '''
        password = 'a password'
        persisted_user = persist_user(
            name='a test name', password=password, nick='test')

        persisted_user = user.find_one(filter={
            '_id': ObjectId(persisted_user['_id'])
        })

        assert persisted_user['password'] != password

    def test_user_nick_add_at(self):
        '''
            Validates if user nick have '@'
            after  persist it
        '''
        nick = 'test'
        persisted_user = persist_user(
            name='a test name', password='a test password', nick=nick)

        is_persisted = user.find_one(filter={
            '_id': ObjectId(persisted_user['_id'])
        })

        persisted_user_nick = is_persisted['nick']
        assert persisted_user_nick != nick

        assert '@' in persisted_user_nick

    def test_parse_nick_with_at_raise_error(self):
        '''
            Check if parse a nickname with '@' to persist_user function
            raise error
        '''
        with pytest.raises(ValueError) as e_info:
            persist_user('a name', 'a password', '@anick')

            assert e_info.message == "the 'nick' field must not contain '@'"
