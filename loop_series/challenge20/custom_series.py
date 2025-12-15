def increasing_diff_series(n):
    series = []
    value = 1
    diff = 1

    for _ in range(n):
        series.append(value)
        value += diff
        diff += 1

    return series


def main():
    n = int(input("Enter number of terms: "))
    print(increasing_diff_series(n))


if __name__ == "__main__":
    main()
