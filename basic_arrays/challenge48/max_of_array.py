def array_max(arr):
    if not arr:
        return None
    return max(arr)


def main():
    arr = list(map(int, input("Enter elements: ").split()))
    print("Maximum =", array_max(arr))


if __name__ == "__main__":
    main()
