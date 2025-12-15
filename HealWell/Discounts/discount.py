def discount(subtotal, age):
    disc = 0
    if age >= 60:
        disc += subtotal * 0.10
    temp = subtotal - disc
    if temp > 5000:
        disc += temp * 0.05
    return subtotal - disc, disc
