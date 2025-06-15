n=int(input("Enter the number you want factorial of :"))
fac=1
for i in range(1,n+1):
    fac*=i
print("Factorial of",n,"is",fac)