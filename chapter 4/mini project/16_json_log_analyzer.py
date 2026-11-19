import json

filename = "logs.json"

try:
    with open(filename, "r") as file:
        logs = json.load(file)

    count = {}

    for log in logs:
        level = log.get("level", "UNKNOWN").upper()

        if level in count:
            count[level] += 1
        else:
            count[level] = 1

    print("Total logs:", len(logs))

    for level, value in count.items():
        print(level, ":", value)

except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Invalid JSON file")