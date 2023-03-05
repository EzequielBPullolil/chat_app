class TestApp:
    def test_client_connect(self, sio):
        '''
            Verify client connection 
        '''

        assert sio.connected == True