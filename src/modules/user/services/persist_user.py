from src.databases.mongodb import user
from ..helper.password_encrypt import password_encrypt


def persist_user(name, password, nick) -> dict:
    '''
        Encript password and add '@' to nick 
        and persist user to mongodb database
    '''
    password = password_encrypt(password)
    nick = f'@{nick}'
    result = user.insert_one({
        'name': name,
        'password': password,
        'nick': nick
    })
    return {
        '_id': str(result.inserted_id),
        'name': name,
        'nick': nick,
    }
