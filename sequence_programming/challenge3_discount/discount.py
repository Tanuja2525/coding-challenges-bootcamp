def calculate_discount(amount, discount_percent):
    discount = amount * discount_percent / 100
    return amount - discount, discount


def main():
    amount = float(input("Enter total amount: "))
    discount_percent = float(input("Enter discount percentage: "))

    final_amount, discount_amount = calculate_discount(amount, discount_percent)

    print("Discount Amount =", discount_amount)
    print("Final Amount =", final_amount)


if __name__ == "__main__":
    main()
