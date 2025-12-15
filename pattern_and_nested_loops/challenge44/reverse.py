def reverse_number(num):
    return int(str(num)[::-1])


def main():
    num = int(input("Enter number: "))
    print("Reverse =", reverse_number(num))


if __name__ == "__main__":
    main()
