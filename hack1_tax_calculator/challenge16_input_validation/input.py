def validate_name():
    while True:
        name = input("Enter Name: ")
        if name.isalpha() and len(name) <= 50:
            return name
        print("Invalid Name. Use alphabets only (max 50 characters).")


def validate_empid():
    while True:
        empid = input("Enter EmpID: ")
        if empid.isalnum() and 5 <= len(empid) <= 10:
            return empid
        print("Invalid EmpID. Use alphanumeric (5-0 characters).")


def validate_basic_salary():
    while True:
        try:
            salary = float(input("Enter Basic Salary: "))
            if salary > 0 and salary <= 10000000:
                return salary
            print("Basic salary must be positive and ≤ ₹1,00,00,000.")
        except ValueError:
            print("Enter a valid number.")


def validate_allowance():
    while True:
        try:
            allowance = float(input("Enter Special Allowance: "))
            if allowance >= 0 and allowance <= 10000000:
                return allowance
            print("Allowance must be ≥ 0 and ≤ ₹1,00,00,000.")
        except ValueError:
            print("Enter a valid number.")


def validate_bonus():
    while True:
        try:
            bonus = float(input("Enter Bonus Percentage: "))
            if 0 <= bonus <= 100:
                return bonus
            print("Bonus percentage must be between 0 and 100.")
        except ValueError:
            print("Enter a valid number.")


def validate_derived_values(gross_monthly, annual_gross):
    if gross_monthly <= 0:
        print("Error: Gross Monthly Salary must be greater than zero.")
        return False
    if annual_gross > 50000000:
        print("Error: Annual Gross Salary exceeds realistic limit.")
        return False
    return True
