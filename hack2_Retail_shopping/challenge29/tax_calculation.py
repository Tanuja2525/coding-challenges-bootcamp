def apply_tax(total):
    if total < 5000:
        return total * 1.05
    elif total <= 20000:
        return total * 1.10
    else:
        return total * 1.15
