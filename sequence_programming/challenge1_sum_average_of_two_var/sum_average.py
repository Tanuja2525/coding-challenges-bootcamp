def sum_and_average(a, b):
    return a + b, (a + b) / 2


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    total, avg = sum_and_average(a, b)

    print("Sum =", total)
    print("Average =", avg)


if __name__ == "__main__":
    main()
