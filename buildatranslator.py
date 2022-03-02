# Build a Translator

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "l"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))


# using lower and isupper function here
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "L"
            else:
                translation = translation + "l"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))
