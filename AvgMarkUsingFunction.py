def avg():
    n=int(input("Enter the number of elements you want to enter: xyzw "))
    sum=0
    for i in range(0,n):
        x=int(input("Enter the number: "))
        sum+=x
    return sum/n

print("Average of the numbers is: ",avg())