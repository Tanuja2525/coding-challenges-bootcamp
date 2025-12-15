def apply_discounts(total, quantity):
    if total > 10000:
        total *= 0.9
    if quantity > 20:
        total *= 0.95
    return total
