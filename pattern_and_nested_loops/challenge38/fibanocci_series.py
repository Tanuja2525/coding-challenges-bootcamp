def fibonacci_pattern(n):
    a, b = 1, 1
    result = []
    count = 0

    for i in range(1, n + 1):
        row = []
        for _ in range(i):
            row.append(a)
            a, b = b, a + b
        result.append(" ".join(map(str, row)))
    return result


def main():
    n = int(input("Enter N: "))
    for line in fibonacci_pattern(n):
        print(line)


if __name__ == "__main__":
    main()
