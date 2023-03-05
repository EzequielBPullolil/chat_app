class TestApp:
    def test_client_connect(self, sio):
        '''
            Verify client connection 
        '''

        sio.connect()
        assert sio.is_connected() == True