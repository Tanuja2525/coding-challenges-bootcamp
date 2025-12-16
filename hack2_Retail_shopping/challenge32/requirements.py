def check_minimum(total):
    return total >= 500


def main():
    print("Minimum Purchase Requirement")

    while True:
        try:
            total = float(input("Enter final amount: "))
            if total < 0:
                print("Total cannot be negative. Enter again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid number.")

    if check_minimum(total):
        print(f"Minimum purchase met. Invoice can be generated. Total: {total:.2f}")
    else:
        print(f"Minimum purchase not met. Total: {total:.2f}. Cannot generate invoice.")


if __name__ == "__main__":
    main()
