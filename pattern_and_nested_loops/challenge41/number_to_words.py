def number_to_words(num):
    words = {
        '0': "Zero", '1': "One", '2': "Two", '3': "Three",
        '4': "Four", '5': "Five", '6': "Six",
        '7': "Seven", '8': "Eight", '9': "Nine"
    }
    return " ".join(words[d] for d in str(num))


def main():
    num = input("Enter number: ")
    print(number_to_words(num))


if __name__ == "__main__":
    main()
