num1 = float(input("Please enter first number: "))
op = input("Please enter the operator: ")
num2 = float(input("Please enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")