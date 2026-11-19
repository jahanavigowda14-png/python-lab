n = int(input("Enter a number: "))

if n < 0:
    print("Enter a non-negative number")

else:
    if n < 2:
        print("Not a prime number")
    else:
        prime = True

        for i in range(2, n):
            if n % i == 0:
                prime = False
                break

        if prime:
            print("Prime number")
        else:
            print("Not a prime number")

    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    print("Factorial:", fact)