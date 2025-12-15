def generate_employee_report(
    name, empid,
    gross_monthly, annual_gross,
    taxable_income, income_tax, cess,
    total_tax, net_salary
):
    print("\nEMPLOYEE TAX REPORT")
    print("=" * 60)
    print(f"{'Field':<30} {'Details'}")
    print("-" * 60)

    print(f"{'Name':<30} {name}")
    print(f"{'EmpID':<30} {empid}")
    print(f"{'Gross Monthly Salary':<30} ₹{gross_monthly:,.2f}")
    print(f"{'Annual Gross Salary':<30} ₹{annual_gross:,.2f}")
    print(f"{'Taxable Income':<30} ₹{taxable_income:,.2f}")
    print(f"{'Income Tax':<30} ₹{income_tax:,.2f}")
    print(f"{'Health & Education Cess':<30} ₹{cess:,.2f}")
    print(f"{'Total Tax Payable':<30} ₹{total_tax:,.2f}")
    print(f"{'Annual Net Salary':<30} ₹{net_salary:,.2f}")

    print("=" * 60)
