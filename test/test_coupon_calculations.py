import unittest
from store import coupon_calculations as cc

# Constants
PRICE_UNDER_TEN = 6.99
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


if __name__ == '__main__':
    unittest.main()
