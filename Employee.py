class Employee:
    def __init__(self,role,dep,salary):
        self.role=role
        self.dep=dep
        self.salary=salary
    def display(self):
        print("Role:",self.role)
        print("Department:",self.dep)
        print("Salary:",self.salary)

class Engineer(Employee):
    def __init__(self,name,age,role,dep,salary):
        self.name=name
        self.age=age
        super().__init__(role,dep,salary)
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        super().display()

def main():
    n=[]
    a=[]
    r=[]
    d=[]
    s=[]
    i=int(input("Enter the total no. of employees to be added: "))
    for i in range(i):
        n.append(input("Enter the name of the employee: "))
        a.append(int(input("Enter the age of the employee: ")))
        r.append(input("Enter the role of the employee: "))
        d.append(input("Enter the department of the employee: "))
        s.append(int(input("Enter the salary of the employee: ")))
    print("\n")
    for i in range(i+1):
        e=Engineer(n[i],a[i],r[i],d[i],s[i])
        e.display()
        print("\n")
main()

def main():
    n=input("Enter the name of the employee: ")
    a=int(input("Enter the age of the employee: "))
    r=input("Enter the role of the employee: ")
    d=input("Enter the department of the employee: ")
    s=int(input("Enter the salary of the employee: "))
    e=Engineer(n,a,r,d,s)
    e.display()
main()