def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))


def main():
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))

    matrix = []

    print("Enter matrix elements row-wise:")
    for i in range(r):
        row = list(map(int, input().split()))
        matrix.append(row)

    print("Matrix:", matrix)
    print("Transpose:", transpose_matrix(matrix))


if __name__ == "__main__":
    main()
