def multiply_matrices(a, b):
    result = [[0]*len(b[0]) for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result


def main():
    a = [[1,2],[3,4]]
    b = [[5,6],[7,8]]
    print("Result:", multiply_matrices(a, b))


if __name__ == "__main__":
    main()
