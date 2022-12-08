from unittest import TestCase
import unittest
from unittest.mock import patch

from Practices.objects import Client

class TestObject(TestCase):
    def setUp(self) -> None:
        self.Client = patch("Test.test_object.Client").start()

    # set up an environment variable for the test
    def tearDown(self) -> None:
        patch.stopall()

    @patch("Test.test_object.Client")
    def test_client_object(self, mock_client):
        #verify if the client object is created
        self.assertEqual(mock_client, self.Client)
        #verify if the client object is verified
        self.assertTrue(mock_client.verify.called)

    @patch("Test.test_object.client_object")
    def test_get_client_object(self, mock_client_object):
        #verify if the client object is returned
        self.assertTrue(mock_client_object.return_value)
        #verify if the client object is verified
        self.assertTrue(mock_client_object.return_value.verify.called)

    # wirte a test for the auth_client_object function and use the patch decorator to mock the client_object function
    @patch("Test.test_object.client_object")
    def test_auth_client_object(self, mock_client_object):
        #verify if the client object is returned
        self.assertTrue(mock_client_object.return_value)
        #verify if the client object is verified
        self.assertTrue(mock_client_object.return_value.verify.called)

if __name__ == "__main__":
    unittest.main()
