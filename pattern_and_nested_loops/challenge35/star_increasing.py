def increasing_star(n):
    return ["*" * i for i in range(1, n + 1)]


def main():
    n = int(input("Enter N: "))
    for line in increasing_star(n):
        print(line)


if __name__ == "__main__":
    main()
