def student_result(name, s1, s2, s3):
    total = s1 + s2 + s3
    avg = total / 3

    if avg >= 60:
        result = "1st Class"
    elif avg >= 50:
        result = "2nd Class"
    elif avg >= 35:
        result = "Pass Class"
    else:
        result = "Fail"

    return total, avg, result


def main():
    name = input("Enter student name: ")
    s1 = int(input("Enter subject 1 marks: "))
    s2 = int(input("Enter subject 2 marks: "))
    s3 = int(input("Enter subject 3 marks: "))

    total, avg, result = student_result(name, s1, s2, s3)

    print("Total =", total)
    print("Average =", avg)
    print("Class =", result)


if __name__ == "__main__":
    main()
