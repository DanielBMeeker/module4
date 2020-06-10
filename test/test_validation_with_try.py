import unittest
from unittest import mock
from input_validation import validation_with_try as avg


class MyTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert avg.average() == 90

    def test_average_exception(self):
        with self.assertRaises(ValueError):
            avg.average_try(-90, 89, 78)
        with self.assertRaises(ValueError):
            avg.average_try(90, -89, 78)


if __name__ == '__main__':
    unittest.main()
