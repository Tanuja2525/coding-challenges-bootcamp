def even_square_series(n):
    series = []
    for i in range(2, n + 1, 2):
        series.append(i * i)
    return series


def main():
    n = int(input("Enter N: "))
    print(even_square_series(n))


if __name__ == "__main__":
    main()
