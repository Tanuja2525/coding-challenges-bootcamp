def square_sign_pattern(n, cols=6):
    num = 1
    result = []

    for _ in range(n):
        row = []
        for _ in range(cols):
            val = num * num
            if num % 2 == 0:
                val = -val
            row.append(str(val))
            num += 1
        result.append(" ".join(row))
    return result


def main():
    n = int(input("Enter N: "))
    for line in square_sign_pattern(n):
        print(line)


if __name__ == "__main__":
    main()
