def tax_check(name, salary):
    if salary > 300000:
        return f"{name} must pay tax"
    else:
        return f"{name} does not need to pay tax"


def main():
    name = input("Enter name: ")
    salary = float(input("Enter salary: "))

    print(tax_check(name, salary))


if __name__ == "__main__":
    main()
