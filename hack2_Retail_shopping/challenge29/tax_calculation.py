def apply_tax(total):
    print("\nApplying Tax:")
    original_total = total

    if total < 0:
        raise ValueError("Total cannot be negative.")

    if total < 5000:
        tax = total * 0.05
        total *= 1.05
        print(f"5% tax applied: +{tax:.2f}")
    elif total <= 20000:
        tax = total * 0.10
        total *= 1.10
        print(f"10% tax applied: +{tax:.2f}")
    else:
        tax = total * 0.15
        total *= 1.15
        print(f"15% tax applied: +{tax:.2f}")

    print(f"Total before tax: {original_total:.2f}")
    print(f"Total after tax: {total:.2f}\n")
    return total


def main():
    print(" Tax Calculation")

    while True:
        try:
            total = float(input("Enter grand total before tax: "))
            if total < 0:
                print("Total cannot be negative. Enter again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid number.")

    total_after_tax = apply_tax(total)
    print(f"Final total after tax: {total_after_tax:.2f}")


if __name__ == "__main__":
    main()
