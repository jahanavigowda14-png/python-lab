filename = "sample.log"

try:
    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines:
        print(line.strip())

    print("Total lines:", len(lines))

except FileNotFoundError:
    print("File not found")