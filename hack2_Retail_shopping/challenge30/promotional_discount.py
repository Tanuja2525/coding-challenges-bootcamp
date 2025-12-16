
def promo_discount(code, total):
    print("\nApplying Promotional Discount:")
    original_total = total

    if not isinstance(total, (int, float)) or total < 0:
        raise ValueError("Total must be a non-negative number.")

    if isinstance(code, str) and code.strip().upper() == "PROMO10":
        discount = total * 0.10
        total *= 0.90
        print(f"10% promotional discount applied for code {code}: -{discount:.2f}")
    else:
        print(f"No promotional discount applied for code {code}.")

    print(f"Item total before discount: {original_total:.2f}")
    print(f"Item total after discount: {total:.2f}\n")
    return total


def main():
    print("Promotional Discounts")

    code = input("Enter item code: ").strip()
    while True:
        try:
            total = float(input("Enter item total: "))
            if total < 0:
                print("Total cannot be negative. Enter again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid number.")

    total_after_discount = promo_discount(code, total)
    print(f"Final total for item {code}: {total_after_discount:.2f}")


if __name__ == "__main__":
    main()
