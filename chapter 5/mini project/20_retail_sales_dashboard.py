import csv
import matplotlib.pyplot as plt

sales = {}

try:
    with open("sales.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            product = row["Product"]
            amount = float(row["Sales"])

            if product in sales:
                sales[product] += amount
            else:
                sales[product] = amount

    print("Retail Sales:")

    for product, amount in sales.items():
        print(product, ":", amount)

    if sales:
        plt.bar(sales.keys(), sales.values())

        plt.title("Retail Sales Dashboard")
        plt.xlabel("Products")
        plt.ylabel("Sales")

        plt.show()

except FileNotFoundError:
    print("Sales file not found")