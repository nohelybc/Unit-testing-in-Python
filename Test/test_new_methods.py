import unittest
from unittest.mock import patch, Mock

from Practices.new_methods import read_file


class MyTestCase(unittest.TestCase):
    def test_verify_data(self):
        self.assertEqual(id, '171368')

    @patch('builtins.open')
    def test_last_file(self):
        # Do a mock of the function max and iglob with a fake path
        with patch('max') as mock_max:
            with patch('glob.iglob') as mock_iglob:
                mock_iglob.return_value = '*.csv'
                mock_max.return_value = '*.csv'
                self.assertEqual(read_file(), '*.csv')

    def test_read_file(self):
        # do a unit test of the function read_file with assertRaises and assertLogs to check the exceptions
        with self.assertRaises(Exception):
            read_file('')
            self.assertLogs('File not found', level='ERROR')




if __name__ == '__main__':
    unittest.main()

