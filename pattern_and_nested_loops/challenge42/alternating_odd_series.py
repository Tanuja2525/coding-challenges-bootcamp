def alternating_series(n):
    result = []
    num = 1
    for i in range(n):
        result.append(num if i % 2 == 0 else -num)
        num += 4
    return result


def main():
    n = int(input("Enter N: "))
    print(alternating_series(n))


if __name__ == "__main__":
    main()
