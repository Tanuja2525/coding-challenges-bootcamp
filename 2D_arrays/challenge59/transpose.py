def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))


def main():
    matrix = [[1,2,3],[4,5,6]]
    print("Matrix:", matrix)
    print("Transpose:", transpose_matrix(matrix))


if __name__ == "__main__":
    main()
