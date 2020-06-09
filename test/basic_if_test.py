"""
Program: basic_if_test.py
Author:  Daniel Meeker
Date: 06/09/2020

This program accepts user input for desired membership
level then calculates and returns the cost of the level.
"""

import unittest
import unittest.mock as mock
from main import basic_if as basic_test


class MyTestCase(unittest.TestCase):
    def test_get_membership(self):  # Test to make sure user input is captured correctly
        with mock.patch('builtins.input', return_value='1'):
            self.assertEqual('1', basic_test.get_membership())

# Tests for calculating cost function
    def test_calculate_cost(self):
        self.assertEqual(['Platinum', 60], basic_test.calculate_cost(1))

    def test_calculate_cost(self):
        self.assertEqual(['Bronze', 30], basic_test.calculate_cost(4))

    def test_calculate_cost(self):
        self.assertEqual(['Free Trial', 0], basic_test.calculate_cost(5))

    def test_calculate_cost(self):
        self.assertEqual(['Error', 0], basic_test.calculate_cost(-2))

# Tests for outputting results function
    def test_output_result(self):
        self.assertEqual('You chose Platinum membership, your price is $60.00 per month',
                         basic_test.output_result(['Platinum', 60]))

    def test_output_result(self):
        self.assertEqual('You chose Gold membership, your price is $50.00 per month',
                         basic_test.output_result(['Gold', 50]))

    def test_output_result(self):
        self.assertEqual('Error, must choose a level between 1-5',
                         basic_test.output_result(['Error', 0]))


if __name__ == '__main__':
    unittest.main()
