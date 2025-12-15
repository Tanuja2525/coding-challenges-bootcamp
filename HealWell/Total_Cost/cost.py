def subtotal(costs):
    total = sum(costs)
    if total <= 0:
        raise ValueError("Subtotal invalid")
    return total
