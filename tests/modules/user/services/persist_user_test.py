from bson import ObjectId
from src.databases.mongodb import user
from src.modules.user.services.persist_user import persist_user


class TestPersistUserService:
    def test_user_was_persisted(self):
        '''
            Validates if user are correctly persisted
        '''
        persisted_user = persist_user(
            name='a test name', password='a test password', nick='@test')

        is_persisted = user.find_one(filter={
            '_id': ObjectId(persisted_user['_id'])
        })

        assert is_persisted != None
