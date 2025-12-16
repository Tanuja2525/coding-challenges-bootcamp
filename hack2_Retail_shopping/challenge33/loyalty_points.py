def loyalty_points(total):
    if not isinstance(total, (int, float)) or total < 0:
        raise ValueError("Total must be a non-negative number.")
    points = int(total // 100)
    return points


def main():
    print("Loyalty Points")

    while True:
        try:
            total = float(input("Enter final total amount: "))
            if total < 0:
                print("Total cannot be negative. Enter again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid number.")

    points = loyalty_points(total)
    print(f"Loyalty Points Earned: {points}")


if __name__ == "__main__":
    main()
