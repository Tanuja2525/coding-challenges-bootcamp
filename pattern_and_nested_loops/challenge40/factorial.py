def factorial_pattern(n):
    fact = 1
    num = 1
    result = []

    for i in range(1, n + 1):
        row = []
        for _ in range(i):
            fact *= num
            row.append(str(fact))
            num += 1
        result.append(" ".join(row))
    return result


def main():
    n = int(input("Enter N: "))
    for line in factorial_pattern(n):
        print(line)


if __name__ == "__main__":
    main()
