from challenge25.basic_item import item_total
from challenge26.iterative_item_entry import grand_total
from challenge27.discount_apply import apply_discounts
from challenge28.membership_discount import membership_discount
from challenge29.tax_calculation import apply_tax
from challenge30.promotional_discount import promo_discount
from challenge31.payment_rules import payment_total
from challenge32.requirements import check_minimum
from challenge33.loyalty_points import loyalty_points

items_total = []
total_quantity = 0

n = int(input("Enter number of items: "))

for i in range(n):
    print(f"Item {i+1}")
    code = input("Enter item code: ")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    total_quantity += qty
    total = item_total(qty, price)
    total = promo_discount(code, total)
    items_total.append(total)

grand = grand_total(items_total)
grand = apply_discounts(grand, total_quantity)

member = input("Are you a member? (y/n): ")
grand = membership_discount(grand, member)

grand = apply_tax(grand)

mode = input("Enter payment mode (cash/card/upi): ")
grand = payment_total(grand, mode)

if check_minimum(grand):
    print("Final Amount:", round(grand, 2))
    print("Loyalty Points:", loyalty_points(grand))
else:
    print("Minimum purchase not met")
