def number_repeat_pattern(n):
    return [str(i) * i for i in range(1, n + 1)]


def main():
    n = int(input("Enter N: "))
    for line in number_repeat_pattern(n):
        print(line)


if __name__ == "__main__":
    main()
