class UnauthorizedUser(Exception):
    '''
        Exception raised when an user
        arent part of chat members try to emit send_message or join_chat
    '''

    def __init__(self, *args: object, user_id, chat_id) -> None:
        self.message = f"the user with id {user_id} arent part of chat with id {chat_id}"
        super().__init__(self.message, *args)
