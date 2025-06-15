L1=[1,2,3,2,1]
L2=L1.copy()
L2.reverse()

L3=[1,"abc","abc",1]
L4=L3.copy()
L4.reverse()

if(L1==L2): 
    print(L1,"is palindrome")
else:
    print(L1,"is not palindrome")
if(L3==L4):
    print(L3,"is palindrome")  
else:
  print(L3,"is not palindrome")