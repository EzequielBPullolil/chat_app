from bson import ObjectId
from src.databases.mongodb import user


class TestPostUserRoutes:
    # Root route
    def test_valid_case_persist_user(self, client):
        post_data = {
            'name': 'test name',
            'nick': 'TestNick',
            'password': 'aPassword'
        }
        response = client.post('/users/', json=post_data)

        assert response.status_code == 201

        responsed_user = response.json['user']

        assert ObjectId.is_valid(responsed_user['_id']) == True
        assert responsed_user['name'] == post_data['name']
        assert responsed_user['nick'] == post_data['nick']

        is_persisted_user = user.find_one(filter={
            '_id': ObjectId(responsed_user['_id'])
        })
        assert is_persisted_user != None

    def test_missing_password_data_response_status_400(self, client):
        post_data = {
            'name': 'test name',
            'nick': 'TestNick'
        }

        response = client.post('/users/', json=post_data)
        assert response.status_code == 400
        assert response.json['error'] == 'missing password payload data'

    def test_missing_name_data_response_status_400(self, client):
        post_data = {
            'password': 'asd',
            'nick': 'TestNick'
        }

        response = client.post('/users/', json=post_data)
        assert response.status_code == 400
        assert response.json['error'] == 'missing name payload data'

    def test_missing_nick_data_response_status_400(self, client):
        post_data = {
            'password': 'asd',
            'name': 'test name'
        }

        response = client.post('/users/', json=post_data)
        assert response.status_code == 400
        assert response.json['error'] == 'missing nick payload data'

    def test_send_already_singed_nick_response_status_400(self, client, singed_nick):
        post_data = {
            'name': 'test name',
            'nick': singed_nick,
            'password': 'aPassword'
        }
        response = client.post('/users/', json=post_data)

        assert response.status_code == 400
        assert response.json['error'] == f'the nick @{singed_nick} is already singed'
