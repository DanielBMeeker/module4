# constants
TAX = .06


def calculate_price(price, cash_coupon, percent_coupon):
    if 0 < price < 10:
        shipping = 5.95
        # Even if discount is greater than the price of the item customer still has to pay shipping.
        if (price - cash_coupon)*(1-percent_coupon) < 0:
            subtotal = shipping
        else:
            subtotal = (price - cash_coupon)*(1-percent_coupon)+shipping
    total = subtotal*(1+.06)
    return total


if __name__ == '__main__':
    pass

