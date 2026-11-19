print("UNIT CONVERTER")
print("1. KM to Metres")
print("2. Metres to CM")
print("3. Celsius to Fahrenheit")
print("4. KG to Grams")

choice = int(input("Enter choice: "))
value = float(input("Enter value: "))

if choice == 1:
    print("Metres:", value * 1000)

elif choice == 2:
    print("Centimetres:", value * 100)

elif choice == 3:
    print("Fahrenheit:", (value * 9/5) + 32)

elif choice == 4:
    print("Grams:", value * 1000)

else:
    print("Invalid choice")