def star_pattern(n, cols=5):
    return ["*" * cols for _ in range(n)]


def main():
    n = int(input("Enter N: "))
    for line in star_pattern(n):
        print(line)


if __name__ == "__main__":
    main()
