from challenge11_salarycal.salary_calculation import calculate_salary
from challenge12_income_cal.income_cal import calculate_taxable_income
from challenge13_rebate_calculation.rebate import calculate_tax
from challenge14_net_salary_cal.net__salary import calculate_net_salary
from challenge15_report_generation.report import generate_employee_report
from challenge16_input_validation.input import (
    validate_name,
    validate_empid,
    validate_basic_salary,
    validate_allowance,
    validate_bonus,
    validate_derived_values
)

def main():
    print("GlobalNext HR-Tech Tax Calculator (New Regime 2023)")

    name = validate_name()
    empid = validate_empid()
    basic = validate_basic_salary()
    allowance = validate_allowance()
    bonus_percent = validate_bonus()

    gross_monthly, annual_gross = calculate_salary(basic, allowance, bonus_percent)

    if not validate_derived_values(gross_monthly, annual_gross):
        print("Invalid salary values.")
        return

    taxable_income = calculate_taxable_income(annual_gross)
    income_tax, cess, total_tax = calculate_tax(taxable_income)
    net_salary = calculate_net_salary(annual_gross, total_tax)

    generate_employee_report(
        name,
        empid,
        gross_monthly,
        annual_gross,
        taxable_income,
        income_tax,
        cess,
        total_tax,
        net_salary
    )

if __name__ == "__main__":
    main()
