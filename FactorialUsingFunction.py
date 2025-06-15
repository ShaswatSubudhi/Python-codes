def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        print(n)
        return n * factorial(n - 1)

n = int(input("Enter the number you want factorial of: "))
print("Factorial of", n, "is", factorial(n))
