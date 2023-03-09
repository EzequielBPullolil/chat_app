from src.modules.chat.services.send_message import send_message
from pytest import raises


class TestSendMessageService:
    def test_call_send_message_and_parse_an_empty_message_raise_error(self):
        '''
            check raises of function send_message when parses 
            an empty string or non parse message
        '''

        with raises(ValueError) as e_info:
            send_message({
                'message': ''
            })
            assert e_info.message == 'invalid message value'

        with raises(ValueError) as e_info:
            send_message({})
            assert e_info.message == 'missing message param'
