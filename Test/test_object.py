from unittest import TestCase
from unittest.mock import patch

class TestObject(TestCase):
    def setUp(self) -> None:
        self.Client = patch("Test.test_object.Client").start()

    #write a test for the client_object function and mock the Client class using the patch decorator
    @patch("Test.test_object.Client")
    def test_client_object(self, mock_client):
        #verify if the client object is created
        self.assertEqual(mock_client, self.Client)
        #verify if the client object is verified
        self.assertTrue(mock_client.verify.called)

    # write a test for the get_client_object function and mock the client_object function using the patch decorator
    @patch("Test.test_object.client_object")
    def test_get_client_object(self, mock_client_object):
        #verify if the client object is returned
        self.assertTrue(mock_client_object.return_value)
        #verify if the client object is verified
        self.assertTrue(mock_client_object.return_value.verify.called)

    # write a test for the auth_client_object function and mock the client_object and get_client_object functions using the patch decorator
    @patch("Test.test_object.client_object")
    @patch("Test.test_object.get_client_object")
    def test_auth_client_object(self, mock_get_client_object, mock_client_object):
        #verify if the client object is authenticated
        self.assertTrue(mock_get_client_object.return_value)
        #verify if the client object is verified
        self.assertTrue(mock_client_object.return_value.verify.called)