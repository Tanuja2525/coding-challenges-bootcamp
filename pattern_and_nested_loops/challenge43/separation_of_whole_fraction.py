def separate_whole_fraction(num):
    whole = int(num)
    fraction = num - whole
    return whole, fraction


def main():
    num = float(input("Enter number: "))
    w, f = separate_whole_fraction(num)
    print("Whole:", w)
    print("Fraction:", f)


if __name__ == "__main__":
    main()
