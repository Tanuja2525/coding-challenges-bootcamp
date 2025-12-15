def odd_numbers(n):
    return [i for i in range(1, n + 1, 2)]


def main():
    n = int(input("Enter N: "))
    print(odd_numbers(n))


if __name__ == "__main__":
    main()
