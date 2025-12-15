def array_sum(arr):
    return sum(arr)


def main():
    arr = list(map(int, input("Enter elements: ").split()))
    print("Sum =", array_sum(arr))


if __name__ == "__main__":
    main()
