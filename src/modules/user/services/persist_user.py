from src.databases.mongodb import user
from ..helper.password_encrypt import password_encrypt


def persist_user(name, password, nick):
    '''
        Encript password and add '@' to nick 
        and persist user to mongodb database
    '''
    if ('@' in nick):
        raise ValueError("the 'nick' field must not contain '@'")
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
