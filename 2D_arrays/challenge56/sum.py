def sum_2d_array(matrix):
    return sum(sum(row) for row in matrix)


def main():
    r = int(input("Enter rows: "))
    c = int(input("Enter columns: "))
    matrix = []

    for _ in range(r):
        matrix.append(list(map(int, input().split())))

    print("Sum =", sum_2d_array(matrix))


if __name__ == "__main__":
    main()
