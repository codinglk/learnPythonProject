# read file, r for read, w for write, r+ for read/write, a for append content in file

employee_file = open("employee.txt", "r")

# To check the file is readable or not
print(employee_file.readable())

# To read the file
# print(employee_file.read())

# To read the line
# print(employee_file.readline())
# print(employee_file.readline())
# print(employee_file.readline())
# print(employee_file.readline())

# put the lines in array
# print(employee_file.readlines())

# access line using index
# print(employee_file.readlines()[1])

# using for loop
for employee in employee_file.readlines():
    print(employee)

employee_file.close()
