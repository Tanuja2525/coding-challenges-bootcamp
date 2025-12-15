def number_sequence_pattern(n):
    return ["".join(str(j) for j in range(1, i + 1)) for i in range(1, n + 1)]


def main():
    n = int(input("Enter N: "))
    for line in number_sequence_pattern(n):
        print(line)


if __name__ == "__main__":
    main()
