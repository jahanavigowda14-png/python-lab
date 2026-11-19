name = input("Enter student name: ")

marks = []

for i in range(3):
    m = float(input("Enter marks: "))

    if m < 0 or m > 100:
        print("Invalid marks")
        raise SystemExit

    marks.append(m)

total = sum(marks)
average = total / 3

print("Name:", name)
print("Total:", total)
print("Average:", average)

if average >= 90:
    print("Grade A")

elif average >= 75:
    print("Grade B")

elif average >= 60:
    print("Grade C")

elif average >= 40:
    print("Grade D")

else:
    print("Fail")