def say_hello(name, age):
    print("Hello " + name + "!" + " You are " + age)


# passing string values
print("Top - passing string values")
say_hello("Lalit", "36")
say_hello("Mike", "35")
print("Bottom")


def say_hi(name, age):
    print("Hi " + name + "!" + " You are " + str(age))


# passing string and integer values
print("Top - passing string and integer values")
say_hi("Lalit", 36)
say_hi("Mike", 35)
print("Bottom")


def cube(num):
    return num*num*num


print("Top - cube")
result = cube(6)
print(result)
result = cube(4)
print(result)
print("Bottom")

