class BankAccount:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn")
        else:
            print("Insufficient balance")

    def display(self):
        print("Name:", self.name)
        print("Balance:", self.balance)


name = input("Enter account holder name: ")

account = BankAccount(name)

while True:
    print("\n1.Deposit")
    print("2.Withdraw")
    print("3.Display Balance")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = float(input("Enter amount: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount: "))
        account.withdraw(amount)

    elif choice == 3:
        account.display()

    elif choice == 4:
        break

    else:
        print("Invalid choice")