def reverse_array(arr):
    return arr[::-1]


def main():
    arr = list(map(int, input("Enter elements: ").split()))
    print(reverse_array(arr))


if __name__ == "__main__":
    main()
