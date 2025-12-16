def item_total(quantity, price):
    return quantity * price


def main():
    print(" Basic Item Entry")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    print("Item Total:", item_total(qty, price))


if __name__ == "__main__":
    main()
