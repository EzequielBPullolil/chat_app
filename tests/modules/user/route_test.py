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
