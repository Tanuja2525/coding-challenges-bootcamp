def calculate_net_salary(annual_gross, total_tax):
    net_salary = annual_gross - total_tax
    return net_salary


def main():
    annual_gross = float(input("Enter Annual Gross Salary: "))
    total_tax = float(input("Enter Total Tax Payable (including cess): "))

    net = calculate_net_salary(annual_gross, total_tax)

    print("\nNet Salary Calculation")
    print("----------------------------")
    print("Annual Gross Salary :", annual_gross)
    print("Total Tax Payable   :", total_tax)
    print("Annual Net Salary   :", net)


if __name__ == "__main__":
    main()
