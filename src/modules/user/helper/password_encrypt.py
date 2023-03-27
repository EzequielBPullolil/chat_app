import bcrypt


def password_encrypt(password):
    '''
        Encrypt password and return it 
    '''
    hashed_password = bcrypt.hashpw(
        bytes(password, 'utf-8'),
        bcrypt.gensalt())
    return hashed_password
