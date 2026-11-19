students = {}

while True:
    print("\n1.Add Student")
    print("2.Mark Attendance")
    print("3.View Report")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter student name: ")

        if name not in students:
            students[name] = {"present": 0, "total": 0}
            print("Student added")
        else:
            print("Student already exists")

    elif choice == 2:
        name = input("Enter student name: ")

        if name not in students:
            print("Student not found")
            continue

        status = input("Enter P for Present or A for Absent: ").upper()

        if status not in ["P", "A"]:
            print("Invalid attendance")
            continue

        students[name]["total"] += 1

        if status == "P":
            students[name]["present"] += 1

        print("Attendance marked")

    elif choice == 3:
        for name, data in students.items():
            total = data["total"]
            present = data["present"]

            percentage = present / total * 100 if total else 0

            print(name, present, "/", total)
            print("Percentage:", percentage)

    elif choice == 4:
        break

    else:
        print("Invalid choice")