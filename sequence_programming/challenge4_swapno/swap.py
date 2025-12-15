def swap_numbers(a, b):
    return b, a


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    a, b = swap_numbers(a, b)
    print("After Swapping:")
    print("a =", a)
    print("b =", b)


if __name__ == "__main__":
    main()
