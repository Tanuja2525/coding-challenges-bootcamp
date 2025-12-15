def sort_array(arr, order):
    if order == "desc":
        return sorted(arr, reverse=True)
    return sorted(arr)


def main():
    arr = list(map(int, input("Enter elements: ").split()))
    order = input("Enter order (asc/desc): ")
    print(sort_array(arr, order))


if __name__ == "__main__":
    main()
