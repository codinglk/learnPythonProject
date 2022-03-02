# To create a dictionary use {}

monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# Dictionary with key as String example
print("Dictionary with key as String example")
print(monthConversion["Mar"])
print(monthConversion.get("Aug"))

# If you pass a key which is not available in the dictionary then it returns None
print(monthConversion.get("ott"))

# Return some default value if key is not found
print(monthConversion.get("ott", "Not a valid key"))

# Key as numbers example
print("Dictionary with key as numbers example")
monthConversion1 = {
    0: "January",
    1: "February",
    2: "March",
    3: "April",
    4: "May",
    5: "June",
    6: "July",
    7: "August",
    8: "September",
    9: "October",
    10: "November",
    11: "December"
}

print(monthConversion1[2])
print(monthConversion1.get(11))

# If you pass a key which is not available in the dictionary then it returns None
print(monthConversion1.get(23))

# Return some default value if key is not found
print(monthConversion1.get(23, "Not a valid key"))
