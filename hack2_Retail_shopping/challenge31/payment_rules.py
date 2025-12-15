def payment_total(total, mode):
    if mode == "card":
        return total * 1.02
    return total
