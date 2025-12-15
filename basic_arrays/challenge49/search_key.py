def search_element(arr, key):
    return key in arr


def main():
    arr = list(map(int, input("Enter elements: ").split()))
    key = int(input("Enter element to search: "))
    print("Found" if search_element(arr, key) else "Not Found")


if __name__ == "__main__":
    main()
