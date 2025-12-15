def get_patient():
    while True:
        name = input("Enter Name: ").strip()
        if name.replace(" ", "").isalpha():
            break
        print("Invalid name")

    while True:
        try:
            age = int(input("Enter Age: "))
            if 0 < age <= 120:
                break
            print("Invalid age")
        except:
            print("Enter valid age")

    while True:
        gender = input("Enter Gender: ").strip()
        if gender.lower() in ["male", "female", "other"]:
            break
        print("Invalid gender")

    while True:
        contact = input("Enter Contact Number: ").strip()
        if contact.isdigit() and len(contact) == 10:
            break
        print("Contact must be 10 digits")

    return name, age, gender, contact
