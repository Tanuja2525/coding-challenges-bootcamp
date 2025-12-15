def custom_series(n):
    series = [1]
    for i in range(1, n):
        series.append(series[-1] + i * i)
    return series


def main():
    n = int(input("Enter number of terms: "))
    print(custom_series(n))


if __name__ == "__main__":
    main()
