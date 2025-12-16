def payment_total(total, mode):
    print("\nApplying Payment Mode Rules:")
    original_total = total

    if not isinstance(total, (int, float)) or total < 0:
        raise ValueError("Total must be a non-negative number.")

    if not isinstance(mode, str):
        raise ValueError("Payment mode must be a string.")

    mode_clean = mode.strip().lower()

    if mode_clean == "card":
        surcharge = total * 0.02
        total *= 1.02
        print(f"Payment mode: Credit Card")
        print(f"Surcharge applied: +{surcharge:.2f}")
    elif mode_clean == "cash":
        print(f"Payment mode: Cash")
        print("No surcharge applied.")
    else:
        print(f"Payment mode: {mode_clean.capitalize()}")
        print("No surcharge applied (default).")

    print(f"Total before surcharge: {original_total:.2f}")
    print(f"Total after surcharge: {total:.2f}\n")
    return total


def main():
    print(" Payment Mode Rules")

    while True:
        try:
            total = float(input("Enter total amount: "))
            if total < 0:
                print("Total cannot be negative. Enter again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid number.")

    while True:
        mode = input("Enter payment mode (cash/card/upi): ").strip().lower()
        if mode not in ['cash', 'card', 'upi']:
            print("Invalid mode. Enter 'cash', 'card', or 'upi'.")
            continue
        break

    total_after_payment = payment_total(total, mode)
    print(f"Final payable amount: {total_after_payment:.2f}")


if __name__ == "__main__":
    main()
