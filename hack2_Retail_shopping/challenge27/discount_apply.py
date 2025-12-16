def apply_discounts(total, quantity):
    print("\nApplying Discounts:")
    original_total = total

    
    if total > 10000:
        discount1 = total * 0.10
        total *= 0.90
        print(f"10% discount for total > 10000 applied: -{discount1:.2f}")
    else:
        print("No discount for total amount (≤ 10000).")
    
    
    if quantity > 20:
        discount2 = total * 0.05
        total *= 0.95
        print(f"5% quantity discount for quantity > 20 applied: -{discount2:.2f}")
    else:
        print("No quantity discount (quantity ≤ 20).")

    print(f"Total before discounts: {original_total:.2f}")
    print(f"Total after discounts: {total:.2f}\n")
    return total


def main():
    print("Challenge 27: Applying Discounts")

    while True:
        try:
            total = float(input("Enter grand total: "))
            if total < 0:
                print("Total cannot be negative. Enter again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a number.")

    while True:
        try:
            quantity = int(input("Enter total quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative. Enter again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter an integer.")

    total_after = apply_discounts(total, quantity)
    print(f"Final total after all discounts: {total_after:.2f}")


if __name__ == "__main__":
    main()
