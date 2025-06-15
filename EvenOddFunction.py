def evenodd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"

n=int(input("Enter the number you want to check: "))
print("The number is",evenodd(n))