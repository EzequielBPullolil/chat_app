def send_message(data):
    '''
        Try to add message to persisted chat

        1. Validate data keys
        2. Verify if user id belongs to chat
        3. create an instance of Message
        4. Find chat by id
        5. Add message instance to chat
    '''
    if (data.get('message', None) == None):
        raise ValueError('missing message param')
    if (data['message'] == ''):
        raise ValueError('invalid message value')
