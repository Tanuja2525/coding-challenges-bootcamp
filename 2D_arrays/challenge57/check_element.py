def search_2d_array(matrix, key):
    for row in matrix:
        if key in row:
            return True
    return False


def main():
    matrix = [[1,2,3],[4,5,6]]
    key = int(input("Enter element to search: "))
    print("Found" if search_2d_array(matrix, key) else "Not Found")


if __name__ == "__main__":
    main()
