from flask import Blueprint, request, make_response

user_bp = Blueprint('user', __name__)


@user_bp.route('/', methods=['POST'])
def create_user():
    return {}, 201
