class Account:
    account={}
    def __init__(self,name,Amount=0):
        self.Amount=Amount
        self.name=name
        Account.account[name]=self

    def deposit(self):
        dep=int(input("Enter the amount you want to deposit: "))
        self.Amount+=dep
        print("Amount deposited successfully")
        return self.Amount

    def Credit(self):
        cr=int(input("Enter the amount you want to credit: "))
        if cr>self.Amount:
            print("Insufficient balance")
        else:
            self.Amount-=cr
            print("Amount credited successfully . Your remaining balance is ",self.Amount)
            return self.Amount

    def check(self):
        print("Your current balance is ",self.Amount)
        return self.Amount
    @classmethod
    def get_account(cls,name):
        return cls.account.get(name)
def main():
    print("welcome to SS Banking System...")
    name=input("Enter your name:")
    acc=Account.get_account(name)
    if acc is None:
        op=input("No account found. would you like to creat a new account...(y/n):")
        if op.lower()=='y':
            acc=Account(name)
            print("Your account has been created successfully")
        else:
            print("Thank you for visiting SS Banking System.please do visit again after creating your account")
            return
    else:
        print("Welcome back to SS Banking")
    while True:
        print("What would you like to do")
        print("1.Deposit")
        print("2.Credit")
        print("3.Check Balance")
        print("4.Exit")
        choice=int(input("Enter your choice(1-4):"))
        if choice==1:
            acc.deposit()
        elif choice==2:
            acc.Credit()
        elif choice==3:
            acc.check()
        elif choice==4:
            print("Thank you for visiting SS Banking System")
            break
        else:
            print("Invalid choice")
main()