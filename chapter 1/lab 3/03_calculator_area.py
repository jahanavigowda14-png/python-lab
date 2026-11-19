print("1.Add 2.Subtract 3.Multiply 4.Divide")
choice = int(input("Enter choice: "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Result:", a + b)
elif choice == 2:
    print("Result:", a - b)
elif choice == 3:
    print("Result:", a * b)
elif choice == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")

print("Area Calculation")
print("1.Rectangle 2.Circle 3.Triangle")

choice = int(input("Enter choice: "))

if choice == 1:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    print("Area:", l * b)

elif choice == 2:
    r = float(input("Enter radius: "))
    print("Area:", 3.14 * r * r)

elif choice == 3:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Area:", 0.5 * b * h)

else:
    print("Invalid choice")