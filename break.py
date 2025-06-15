t=(1,24,9,16,25,36,49,64,81,100)
x=int(input("Enter the number you want to search for: "))
for i in t:
    if(i==x):
        print("Your element",x,"found")
        break
else:
    print("Your element",x,"not found")