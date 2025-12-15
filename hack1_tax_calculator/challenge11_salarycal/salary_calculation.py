def calculate_salary(basic, allowance, bonus_percent):
    gross_monthly = basic + allowance
    bonus = (gross_monthly * 12) * (bonus_percent / 100)
    annual_gross = (gross_monthly * 12) + bonus
    return gross_monthly, annual_gross


def main():
    name = input("Enter Name: ")
    emp_id = input("Enter EmpID: ")
    basic = float(input("Enter Basic Monthly Salary: "))
    allowance = float(input("Enter Special Allowance (Monthly): "))
    bonus_percent = float(input("Enter Bonus Percentage: "))

    gross_monthly, annual_gross = calculate_salary(basic, allowance, bonus_percent)

    print("\nEmployee Details")
    print("----------------------")
    print("Name :", name)
    print("EmpID:", emp_id)

    print("\nSalary Details")
    print("----------------------")
    print("Gross Monthly Salary :", gross_monthly)
    print("Annual Gross Salary  :", annual_gross)


if __name__ == "__main__":
    main()
