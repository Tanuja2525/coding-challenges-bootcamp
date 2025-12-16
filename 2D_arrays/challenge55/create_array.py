def display_2d_array(matrix):
    return matrix


def main():
    r = int(input("Enter rows: "))
    c = int(input("Enter columns: "))
    matrix = []

    for _ in range(r):
        row = list(map(int, input().split()))
        matrix.append(row)
    print("matrix →")
    print("[")
    for row in display_2d_array(matrix):
        print(" ", row)
    print("]")



if __name__ == "__main__":
    main()
