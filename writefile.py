# w to overwrite the content in existing file or create new file and write

# provide the existing file name to overwrite the content of file
# employee_file = open("employee.txt", "w")
# employee_file.write("Kelly - Customer Service")

# provide the new file name to create and write the content in new file
# employee_file = open("employee1.txt", "w")
# employee_file.write("Kelly - Customer Service")
# employee_file.write("\nLalit Kumar - Senior Project Leader")

# provide the new file name to create and write the content in new file, here we create new HTML file
employee_file = open("index.html", "w")
employee_file.write("<html>")
employee_file.write("\n<body>")
employee_file.write("\n<p>This is HTML page.</p>")
employee_file.write("\n</body>")
employee_file.write("\n</html>")

employee_file.close()
