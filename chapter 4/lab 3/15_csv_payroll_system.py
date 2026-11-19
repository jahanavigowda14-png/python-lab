import csv

filename = "payroll.csv"

n = int(input("Enter number of employees: "))

with open(filename, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "ID", "Name", "Basic Salary",
        "Allowance", "Deduction", "Net Salary"
    ])

    for i in range(n):

        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")

        basic = float(input("Enter basic salary: "))
        allowance = float(input("Enter allowance: "))
        deduction = float(input("Enter deduction: "))

        net = basic + allowance - deduction

        writer.writerow([
            emp_id, name, basic,
            allowance, deduction, net
        ])

print("Payroll saved successfully")