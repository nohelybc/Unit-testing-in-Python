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