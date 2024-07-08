expression = input("Enter expression: ").strip()
num1, operation, num2 = expression.split(" ")
num1, num2 = float(num1), float(num2)

if operation == '+':
    print(num1+num2)
elif operation == '-':
    print(num1-num2)
elif operation == '*':
    print(num1*num2)
elif operation == '/' and num2 != 0.0:
    print(num1/num2) 
