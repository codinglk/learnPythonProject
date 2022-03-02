# import class from file

from Student import Student

student1 = Student("Mike", "Cloud Computing", 4.1, False)
student2 = Student("Toby", "Machine Learning", 3.1, True)

print(student1.major)
print(student2.gpa)

# calling class function here
print(student1.on_honor_role())
print(student2.on_honor_role())


