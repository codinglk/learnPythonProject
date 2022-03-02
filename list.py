
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[-1])
print(friends[-2])
print(friends[-3])
print(friends[1:])
print(friends[1:3])

friends[1] = "Mike"
print(friends[1])

lucky_numbers = [5, 9, 2, 12, 90]
friends.extend(lucky_numbers)
print(friends)

friends.append("Tom")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Oscar")
print(friends)

friends.pop()
print(friends)

print(friends.index("Toby"))
print(friends.count("Jim"))

friends1 = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends1.sort()
print(friends1)

numbers_list = [90, 3, 56, 1, 345, 23, 55]
numbers_list.sort()
print(numbers_list)
numbers_list.reverse()
print(numbers_list)

friends2 = friends1.copy()
print(friends2)

friends.clear()
print(friends)

