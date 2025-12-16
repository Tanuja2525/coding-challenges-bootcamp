from challenge25.basic_item import item_total
from challenge26.iterative_item_entry import grand_total
from challenge27.discount_apply import apply_discounts
from challenge28.membership_discount import membership_discount
from challenge29.tax_calculation import apply_tax
from challenge30.promotional_discount import promo_discount
from challenge31.payment_rules import payment_total
from challenge32.requirements import check_minimum
from challenge33.loyalty_points import loyalty_points

def main():
    print("=== Retail Shopping Application ===\n")
    
    while True:
        try:
            n = int(input("Enter number of items: "))
            if n <= 0:
                print("Number of items must be at least 1.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter an integer.")

    items_total = []
    total_quantity = 0

    for i in range(1, n+1):
        print(f"\nItem {i}:")
        code = input("Enter item code: ").strip()
        description = input("Enter item description: ").strip()

        while True:
            try:
                qty = int(input("Enter quantity: "))
                if qty < 0:
                    print("Quantity cannot be negative. Enter again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Enter an integer.")

        while True:
            try:
                price = float(input("Enter price: "))
                if price < 0:
                    print("Price cannot be negative. Enter again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Enter a valid number.")

        total_quantity += qty
        total = item_total(qty, price)
        total = promo_discount(code, total)
        items_total.append(total)

    grand = grand_total(items_total)
    print(f"\nGrand Total before discounts: {grand:.2f}")

    grand = apply_discounts(grand, total_quantity)

    while True:
        member = input("Are you a member? (y/n): ").strip().lower()
        if member not in ['y', 'n']:
            print("Invalid input. Enter 'y' or 'n'.")
            continue
        break
    grand = membership_discount(grand, member)

    grand = apply_tax(grand)

    while True:
        mode = input("Enter payment mode (cash/card/upi): ").strip().lower()
        if mode not in ['cash', 'card', 'upi']:
            print("Invalid mode. Enter 'cash', 'card', or 'upi'.")
            continue
        break
    grand = payment_total(grand, mode)

    if check_minimum(grand):
        print(f"\nFinal Amount Payable: ₹{round(grand, 2)}")
        points = loyalty_points(grand)
        print(f"Loyalty Points Earned: {points}")
    else:
        print(f"\nMinimum purchase not met. Final amount ₹{round(grand, 2)}. Cannot generate invoice.")


if __name__ == "__main__":
    main()
