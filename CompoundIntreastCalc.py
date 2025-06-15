def CompounfIntrest(n,P,r,t):
    while n>0:
        A=P*(1-r/n)**n*t
        n-=1
    return A
def main():
    P=float(input("Enter the principal Amount:"))
    r=float(input("Enter the rate of intrest:"))
    t=float(input("Enter the time period:"))
    n=int(input("Enter the number of times intrest applied per time period:"))
    print("The Compound Intrest is:",CompounfIntrest(n,P,r,t))
main()
