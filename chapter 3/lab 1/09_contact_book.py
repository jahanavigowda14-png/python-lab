contacts = {}

while True:
    print("\n1.Add Contact")
    print("2.Search Contact")
    print("3.Display Contacts")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact added")

    elif choice == 2:
        name = input("Enter name to search: ")

        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found")

    elif choice == 3:
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == 4:
        break

    else:
        print("Invalid choice")