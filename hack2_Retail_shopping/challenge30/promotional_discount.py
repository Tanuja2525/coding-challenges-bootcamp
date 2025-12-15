def promo_discount(code, total):
    if code == "PROMO10":
        return total * 0.9
    return total
