def natural_numbers(n):
    return list(range(1, n + 1))


def main():
    n = int(input("Enter N: "))
    print(natural_numbers(n))


if __name__ == "__main__":
    main()
