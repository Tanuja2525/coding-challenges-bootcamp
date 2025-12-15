def number_pattern_fixed(n, cols=5):
    pattern = []
    for _ in range(n):
        pattern.append("".join(str(i) for i in range(1, cols + 1)))
    return pattern


def main():
    n = int(input("Enter number of rows: "))
    for line in number_pattern_fixed(n):
        print(line)


if __name__ == "__main__":
    main()
