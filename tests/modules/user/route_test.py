from flask import url_for


class TestPostUserRoutes:
    # Root route
    def test_post_method(self, client):
        post_data = {
            'name': 'test name',
            'nick': '@TestNick',
            'password': 'aPassword'
        }
        response = client.post('/users/', json=post_data)

        assert response.status_code == 201

    def test_missing_password_data_response_status_400(self, client):
        post_data = {
            'name': 'test name',
            'nick': '@TestNick'
        }

        response = client.post('/users/', json=post_data)
        assert response.status_code == 400
        assert response.json['error'] == 'missing password payload data'
