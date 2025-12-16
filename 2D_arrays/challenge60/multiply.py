def multiply_matrices(a, b):
    result = [[0] * len(b[0]) for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result


def main():
    r1 = int(input("Enter number of rows of first matrix: "))
    c1 = int(input("Enter number of columns of first matrix: "))

    print("Enter elements of first matrix:")
    a = []
    for i in range(r1):
        row = list(map(int, input().split()))
        a.append(row)

    r2 = int(input("Enter number of rows of second matrix: "))
    c2 = int(input("Enter number of columns of second matrix: "))

    print("Enter elements of second matrix:")
    b = []
    for i in range(r2):
        row = list(map(int, input().split()))
        b.append(row)

    # Matrix multiplication condition
    if c1 != r2:
        print("Matrix multiplication not possible")
        return

    result = multiply_matrices(a, b)
    print("Result:", result)


if __name__ == "__main__":
    main()
