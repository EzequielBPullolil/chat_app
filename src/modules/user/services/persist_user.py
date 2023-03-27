from src.databases.mongodb import user


def persist_user(name, password, nick) -> dict:
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
