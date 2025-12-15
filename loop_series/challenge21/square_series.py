def square_series(n):
    series = []
    for i in range(1, n + 1):
        series.append(i * i)
    return series


def main():
    n = int(input("Enter N: "))
    print(square_series(n))


if __name__ == "__main__":
    main()
