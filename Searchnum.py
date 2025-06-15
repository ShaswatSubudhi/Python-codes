l=(1,2,3,4,5,6,7,8,9,10)
i=0
x=int(input("Enter the number you want to search for: "))
while i < len(l):
    if(l[i]==x):
        print("Your element",x,"found at index",i)
        break
    elif(l[i]==l[-1]):
        print("Your element",x,"not found")
        break
    else:
        i+=1