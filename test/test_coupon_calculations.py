"""
Program: Test Coupon Calculations
Author: Daniel Meeker
Date: 06/09/2020

This program uses if-elif statements to calculate order totals
with discounts, shipping, and tax. This file tests the program.
"""
import unittest
from store import coupon_calculations as cc

# Constants
PRICE_UNDER_TEN = 6.99
PRICE_BETWEEN_TEN_THIRTY = 24.99
PRICE_BETWEEN_THIRTY_FIFTY = 39.99
PRICE_OVER_FIFTY = 74.99
CASH_COUPON_FIVE = 5
CASH_COUPON_TEN = 10
PERCENT_COUPON_TEN = .1
PERCENT_COUPON_FIFTEEN = .15
PERCENT_COUPON_TWENTY = .2


class MyTestCase(unittest.TestCase):

    def test_price_under_ten(self):
        self.assertAlmostEqual(cc.calculate_price(PRICE_UNDER_TEN, CASH_COUPON_FIVE, PERCENT_COUPON_TEN), 8.21, places=2)
        self.assertAlmostEqual(cc.calculate_price(PRICE_UNDER_TEN, CASH_COUPON_FIVE, PERCENT_COUPON_FIFTEEN), 8.10, places=2)
        self.assertAlmostEqual(cc.calculate_price(PRICE_UNDER_TEN, CASH_COUPON_FIVE, PERCENT_COUPON_TWENTY), 7.99, places=2)
        self.assertAlmostEqual(cc.calculate_price(PRICE_UNDER_TEN, CASH_COUPON_TEN, PERCENT_COUPON_TEN), 6.31, places=2)
        self.assertAlmostEqual(cc.calculate_price(PRICE_UNDER_TEN, CASH_COUPON_TEN, PERCENT_COUPON_FIFTEEN), 6.31, places=2)
        self.assertAlmostEqual(cc.calculate_price(PRICE_UNDER_TEN, CASH_COUPON_TEN, PERCENT_COUPON_TWENTY), 6.31, places=2)

    def test_price_ten_to_thirty(self):
        self.assertAlmostEqual(cc.calculate_price(PRICE_BETWEEN_TEN_THIRTY, CASH_COUPON_FIVE, PERCENT_COUPON_TEN), 27.50, places=2)
        self.assertAlmostEqual(cc.calculate_price(PRICE_BETWEEN_TEN_THIRTY, CASH_COUPON_FIVE, PERCENT_COUPON_FIFTEEN), 26.44, places=2)
        self.assertAlmostEqual(cc.calculate_price(PRICE_BETWEEN_TEN_THIRTY, CASH_COUPON_FIVE, PERCENT_COUPON_TWENTY), 25.38, places=2)
        self.assertAlmostEqual(cc.calculate_price(PRICE_BETWEEN_TEN_THIRTY, CASH_COUPON_TEN, PERCENT_COUPON_TEN), 22.73, places=2)
        self.assertAlmostEqual(cc.calculate_price(PRICE_BETWEEN_TEN_THIRTY, CASH_COUPON_TEN, PERCENT_COUPON_FIFTEEN), 21.93, places=2)
        self.assertAlmostEqual(cc.calculate_price(PRICE_BETWEEN_TEN_THIRTY, CASH_COUPON_TEN, PERCENT_COUPON_TWENTY), 21.14, places=2)

    def test_price_thirty_to_fifty(self):
        self.assertAlmostEqual(cc.calculate_price(PRICE_BETWEEN_THIRTY_FIFTY, CASH_COUPON_FIVE, PERCENT_COUPON_TEN), 46.05, places=2)
        self.assertAlmostEqual(cc.calculate_price(PRICE_BETWEEN_THIRTY_FIFTY, CASH_COUPON_FIVE, PERCENT_COUPON_FIFTEEN), 39.95, places=2)
        self.assertAlmostEqual(cc.calculate_price(PRICE_BETWEEN_THIRTY_FIFTY, CASH_COUPON_FIVE, PERCENT_COUPON_TWENTY), 38.10, places=2)
        self.assertAlmostEqual(cc.calculate_price(PRICE_BETWEEN_THIRTY_FIFTY, CASH_COUPON_TEN, PERCENT_COUPON_TEN), 37.04, places=2)
        self.assertAlmostEqual(cc.calculate_price(PRICE_BETWEEN_THIRTY_FIFTY, CASH_COUPON_TEN, PERCENT_COUPON_FIFTEEN), 35.45, places=2)
        self.assertAlmostEqual(cc.calculate_price(PRICE_BETWEEN_THIRTY_FIFTY, CASH_COUPON_TEN, PERCENT_COUPON_TWENTY), 33.86, places=2)

    def test_price_over_fifty(self):
        self.assertAlmostEqual(cc.calculate_price(PRICE_OVER_FIFTY, CASH_COUPON_FIVE, PERCENT_COUPON_TEN), 66.77, places=2)
        self.assertAlmostEqual(cc.calculate_price(PRICE_OVER_FIFTY, CASH_COUPON_FIVE, PERCENT_COUPON_FIFTEEN), 63.06, places=2)
        self.assertAlmostEqual(cc.calculate_price(PRICE_OVER_FIFTY, CASH_COUPON_FIVE, PERCENT_COUPON_TWENTY), 59.35, places=2)
        self.assertAlmostEqual(cc.calculate_price(PRICE_OVER_FIFTY, CASH_COUPON_TEN, PERCENT_COUPON_TEN), 62.00, places=2)
        self.assertAlmostEqual(cc.calculate_price(PRICE_OVER_FIFTY, CASH_COUPON_TEN, PERCENT_COUPON_FIFTEEN), 58.56, places=2)
        self.assertAlmostEqual(cc.calculate_price(PRICE_OVER_FIFTY, CASH_COUPON_TEN, PERCENT_COUPON_TWENTY), 55.11, places=2)


if __name__ == '__main__':
    unittest.main()
