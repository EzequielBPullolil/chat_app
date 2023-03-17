from flask import Blueprint, request, make_response
from bson import ObjectId

from src.databases.mongodb import user
from .helper.singed_user_nick import singed_user_nick
from .exceptions import UserDomainException
user_bp = Blueprint('user', __name__)


@user_bp.route('/', methods=['POST'])
def sing_user():
    '''
        Persist user before validate name, password and nick,
        and response a json with name, nickname and encripted password

        required payloads: name, nick, password

        response: JSON, status 201
    '''
    try:
        data = request.get_json()
        password = data['password']
        nick = data['nick']
        name = data['name']
        singed_user_nick(nick)
        result = user.insert_one({
            'name': name,
            'nick': nick,
            'password': password
        })
        return {
            'user': {
                '_id': str(result.inserted_id),
                'name': name,
                'nick': nick
            }
        }, 201

    except KeyError:
        missings_param = ''
        if (not 'password' in data):
            missings_param = 'password'

        if (not 'nick' in data):
            missings_param = 'nick'

        if (not 'name' in data):
            missings_param = 'name'

        return {
            'error': f'missing {missings_param} payload data'
        }, 400
    except UserDomainException as e_info:
        return {
            'error': e_info.message
        }, 400
