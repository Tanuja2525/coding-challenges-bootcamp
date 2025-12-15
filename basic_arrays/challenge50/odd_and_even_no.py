def count_odd_even(arr):
    even = 0
    odd = 0
    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


def main():
    arr = list(map(int, input("Enter elements: ").split()))
    even, odd = count_odd_even(arr)
    print("Even =", even)
    print("Odd =", odd)


if __name__ == "__main__":
    main()
