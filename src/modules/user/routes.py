from flask import Blueprint, request, make_response

user_bp = Blueprint('user', __name__)


@user_bp.route('/', methods=['POST'])
def create_user():
    '''
        Persist user in database
    '''
    try:
        data = request.get_json()
        password = data['password']
        return {}, 201

    except KeyError:
        if (not 'password' in data):
            return {
                'error': 'missing password payload data'
            }, 400
