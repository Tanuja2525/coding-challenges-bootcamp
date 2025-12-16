def calculate_salary(basic, allowance, bonus_percent):
    if basic < 0 or allowance < 0:
        raise ValueError("Salary values cannot be negative")

    if bonus_percent < 0:
        raise ValueError("Bonus percentage cannot be negative")

    gross_monthly = basic + allowance
    annual_basic = gross_monthly * 12
    bonus = annual_basic * (bonus_percent / 100)
    annual_gross = annual_basic + bonus

    return gross_monthly, annual_gross


def main():
    try:
        name = input("Enter Name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty")

        emp_id = input("Enter EmpID: ").strip()
        if not emp_id:
            raise ValueError("EmpID cannot be empty")

        basic = float(input("Enter Basic Monthly Salary: "))
        allowance = float(input("Enter Special Allowance (Monthly): "))
        bonus_percent = float(input("Enter Bonus Percentage: "))

        gross_monthly, annual_gross = calculate_salary(
            basic, allowance, bonus_percent
        )

        print("\nEmployee Details")
        print("----------------------")
        print("Name :", name)
        print("EmpID:", emp_id)

        print("\nSalary Details")
        print("----------------------")
        print("Gross Monthly Salary :", round(gross_monthly, 2))
        print("Annual Gross Salary  :", round(annual_gross, 2))

    except ValueError as e:
        print("Input Error:", e)
    except Exception:
        print("Unexpected error occurred")


if __name__ == "__main__":
    main()
