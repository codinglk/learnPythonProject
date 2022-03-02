# a for append the content in file
employee_file = open("employee.txt", "a")

# append the content exactly where file content ends
# employee_file.write("Aileen - Scrum Master")

# append the content in new line in the file
employee_file.write("\nMike - Software Developer and Trainer")

employee_file.close()
