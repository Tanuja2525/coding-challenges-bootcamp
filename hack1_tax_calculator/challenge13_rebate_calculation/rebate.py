def calculate_tax(taxable_income):
    if taxable_income <= 700000:
        return 0, 0, 0   # tax, cess, total tax

    tax = 0
    remaining = taxable_income

    slabs = [
        (300000, 0.00),
        (300000, 0.05),
        (300000, 0.10),
        (300000, 0.15),
        (300000, 0.20),
        (float('inf'), 0.30)
    ]

    for limit, rate in slabs:
        if remaining <= 0:
            break
        amount = min(remaining, limit)
        tax += amount * rate
        remaining -= amount

    cess = tax * 0.04
    total_tax = tax + cess
    return tax, cess, total_tax


def main():
    taxable_income = float(input("Enter Taxable Income: "))

    tax, cess, total_tax = calculate_tax(taxable_income)

    print("\nTax Calculation Breakdown")
    print("------------------------------")
    print("Taxable Income :", taxable_income)
    print("Income Tax     :", tax)
    print("Health & Edu Cess (4%) :", cess)
    print("Total Tax Payable :", total_tax)


if __name__ == "__main__":
    main()
