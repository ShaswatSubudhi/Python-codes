def cal(a, b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        if b==0:
            return 'Error: Division by zero'
        else:
            return a/b
    elif op=='%':
        if b==0:
            return 'Error: Division by zero'
        else:
            return a%b
    elif op=='**':
        return a**b
    else:
        return 'Error: Invalid operator'
def main():
    print("Calculator")
    print("Enter two numbers and an operator (+,-,*,/,%,**)")
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    operator=input("Enter operator: ")
    result=cal(num1, num2, operator)
    print("Result: ", result)
main()
