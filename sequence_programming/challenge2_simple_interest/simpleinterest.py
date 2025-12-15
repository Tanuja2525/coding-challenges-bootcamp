def simple_interest(p, r, t):
    return (p * r * t) / 100


def main():
    p = float(input("Enter principal: "))
    r = float(input("Enter rate: "))
    t = float(input("Enter time: "))

    si = simple_interest(p, r, t)
    print("Simple Interest =", si)


if __name__ == "__main__":
    main()
