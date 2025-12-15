def display_services(services):
    for i, s in enumerate(services, 1):
        print(f"{i}. {s}")

def select_services():
    while True:
        try:
            choices = list(set(int(i)-1 for i in input("Select services: ").split(",")))
            if all(i >= 0 for i in choices):
                return choices
            print("Invalid selection")
        except:
            print("Enter valid numbers")
