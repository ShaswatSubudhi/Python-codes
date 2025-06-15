class Student:
    def __init__ (me,subname,submarks):
        me.subname=subname
        me.submarks=submarks
    def avg(me):
        sum=0
        for i in me.submarks:
            sum+=i
        return sum/len(me.submarks)
    
# s1=Student("Shaswat",[10,20,30])
m=[]
for i in range(3):
    m.append(int(input("Enter the marks : ")))

s1=Student(input("Enter the name of the student: "),m)
print("Avg of ",s1.subname," is ",s1.avg())