STANDARD_DEDUCTION = 50000

def calculate_taxable_income(annual_gross):
    taxable_income = annual_gross - STANDARD_DEDUCTION
    if taxable_income < 0:
        taxable_income = 0
    return taxable_income


def main():
    annual_gross = float(input("Enter Annual Gross Salary: "))

    taxable_income = calculate_taxable_income(annual_gross)

    print("\nTaxable Income Calculation")
    print("----------------------------")
    print("Annual Gross Salary  :", annual_gross)
    print("Standard Deduction  :", STANDARD_DEDUCTION)
    print("Taxable Income      :", taxable_income)


if __name__ == "__main__":
    main()
