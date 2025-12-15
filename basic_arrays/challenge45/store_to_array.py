def create_array(elements):
    return elements


def main():
    n = int(input("Enter number of elements: "))
    arr = []
    for _ in range(n):
        arr.append(int(input("Enter element: ")))
    print(create_array(arr))


if __name__ == "__main__":
    main()
