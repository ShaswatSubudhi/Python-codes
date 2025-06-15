def element(l,n):
    if(n==len(l)):
        return 
    else:
        print(l[n])
        element(l,n+1)


l=[1,2,3,4,5,6,7,8,9,10]
element(l,0)
