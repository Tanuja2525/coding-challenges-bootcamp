def membership_discount(total, member):
    print("\nApplying Membership Discount:")
    original_total = total

    if isinstance(member, str) and member.strip().lower() == 'y':
        discount = total * 0.02
        total *= 0.98
        print(f"2% membership discount applied: -{discount:.2f}")
    else:
        print("No membership discount applied.")

    print(f"Total before membership discount: {original_total:.2f}")
    print(f"Total after membership discount: {total:.2f}\n")
    return total


def main():
    print(" Membership Discounts")

    while True:
        try:
            total = float(input("Enter grand total after previous adjustments: "))
            if total < 0:
                print("Total cannot be negative. Enter again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid number.")

    while True:
        member = input("Are you a member? (y/n): ").strip().lower()
        if member not in ['y', 'n']:
            print("Invalid input. Enter 'y' or 'n'.")
            continue
        break

    total_after = membership_discount(total, member)
    print(f"Final total after membership discount: {total_after:.2f}")


if __name__ == "__main__":
    main()
