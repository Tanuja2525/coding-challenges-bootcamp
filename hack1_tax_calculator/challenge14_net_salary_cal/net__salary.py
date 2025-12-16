def calculate_net_salary(annual_gross, total_tax):
    if annual_gross < 0:
        raise ValueError("Annual gross salary cannot be negative")

    if total_tax < 0:
        raise ValueError("Total tax cannot be negative")

    if total_tax > annual_gross:
        raise ValueError("Total tax cannot exceed annual gross salary")

    net_salary = annual_gross - total_tax
    return net_salary


def main():
    try:
        annual_gross = float(input("Enter Annual Gross Salary: "))
        total_tax = float(input("Enter Total Tax Payable (including cess): "))

        net = calculate_net_salary(annual_gross, total_tax)

        print("\nNet Salary Calculation")
        print("----------------------------")
        print("Annual Gross Salary :", round(annual_gross, 2))
        print("Total Tax Payable   :", round(total_tax, 2))
        print("Annual Net Salary   :", round(net, 2))

    except ValueError as e:
        print("Input Error:", e)
    except Exception:
        print("Unexpected error occurred")


if __name__ == "__main__":
    main()
