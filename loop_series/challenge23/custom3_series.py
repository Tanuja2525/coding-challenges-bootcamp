def mixed_increment_series(n):
    series = [1]
    inc = 4

    for i in range(1, n):
        series.append(series[-1] + inc)
        inc = 4 if inc == 8 else 8

    return series


def main():
    n = int(input("Enter number of terms: "))
    print(mixed_increment_series(n))


if __name__ == "__main__":
    main()
