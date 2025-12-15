def array_min(arr):
    if not arr:
        return None
    return min(arr)


def main():
    arr = list(map(int, input("Enter elements: ").split()))
    print("Minimum =", array_min(arr))


if __name__ == "__main__":
    main()
