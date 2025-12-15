def fibonacci_series(n):
    series = []

    a, b = 1, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b

    return series


def main():
    n = int(input("Enter number of terms: "))
    print(fibonacci_series(n))


if __name__ == "__main__":
    main()
