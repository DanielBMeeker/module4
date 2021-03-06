"""
Program: Coupon Calculations
Author: Daniel Meeker
Date: 06/09/2020

This program uses if-elif statements to calculate order totals
with discounts, shipping, and tax.
"""
# CONSTANT
TAX = .06


def calculate_price(price, cash_coupon, percent_coupon):
    price_after_discounts = (price - cash_coupon)*(1-percent_coupon)
    # Even if discount is greater than the price of the item customer still has to pay shipping
    # so reset price to 0 so that a discount is not applied to shipping.
    if price_after_discounts < 0:
        price_after_discounts = 0
    if 0 <= price_after_discounts < 10:
        shipping = 5.95
    elif 10 <= price_after_discounts < 30:
        shipping = 7.95
    elif 30 <= price_after_discounts < 50:
        shipping = 11.95
    else:  # Already dealt with all other numbers, only thing left is price_after_discounts over 50,
        # which have free shipping.
        shipping = 0
    subtotal = price_after_discounts+shipping
    total = subtotal*(1+.06)
    return total


if __name__ == '__main__':
    pass

