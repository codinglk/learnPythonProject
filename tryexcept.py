# try and except examples , comment the code and just uncomment one try except section for better understanding

try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")

try:
    value = 10/0
    print(value)
except:
    print("ZeroDivisionError: division by zero")

try:
    number = int(input("Enter a number: "))
    print(number)
    value = 10/0
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid Input")

# print the specific error
try:
    value = 10/0
    print(value)
except ZeroDivisionError as err:
    print(err)
