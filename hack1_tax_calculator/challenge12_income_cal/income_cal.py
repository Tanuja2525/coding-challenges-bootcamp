STANDARD_DEDUCTION = 50000


def calculate_taxable_income(annual_gross):
    if annual_gross < 0:
        raise ValueError("Annual gross salary cannot be negative")

    taxable_income = annual_gross - STANDARD_DEDUCTION

    if taxable_income < 0:
        taxable_income = 0

    return taxable_income


def main():
    try:
        annual_gross = float(input("Enter Annual Gross Salary: "))

        taxable_income = calculate_taxable_income(annual_gross)

        print("\nTaxable Income Calculation")
        print("----------------------------")
        print("Annual Gross Salary  :", round(annual_gross, 2))
        print("Standard Deduction  :", STANDARD_DEDUCTION)
        print("Taxable Income      :", round(taxable_income, 2))

    except ValueError as e:
        print("Input Error:", e)
    except Exception:
        print("Unexpected error occurred")


if __name__ == "__main__":
    main()
