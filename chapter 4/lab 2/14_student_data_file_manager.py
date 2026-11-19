filename = "students.txt"

while True:
    print("\n1.Add Student")
    print("2.Display Students")
    print("3.Search Student")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        usn = input("Enter USN: ")

        with open(filename, "a") as f:
            f.write(name + "," + usn + "\n")

        print("Student saved")

    elif choice == 2:
        try:
            with open(filename, "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("No records found")

    elif choice == 3:
        search = input("Enter USN: ")
        found = False

        try:
            with open(filename, "r") as f:
                for line in f:
                    name, usn = line.strip().split(",", 1)

                    if usn == search:
                        print("Name:", name)
                        print("USN:", usn)
                        found = True

            if not found:
                print("Student not found")

        except FileNotFoundError:
            print("No records found")

    elif choice == 4:
        break