def number_pattern_same(n, cols=5):
    return [str(i) * cols for i in range(1, n + 1)]


def main():
    n = int(input("Enter N: "))
    for line in number_pattern_same(n):
        print(line)


if __name__ == "__main__":
    main()

