__author__ = 'dev'
# greeting = "Michael"
# _myName = "Mike"
# Mike57 = "Good"
# # 1Mike = "Bad"
# Mike57_was_56 = "Hello"
# Greeting = "There"
# print(Mike57_was_56 + " " + greeting)
#
# age = 24
# print(age)
#
# print(greeting + age)

# Integers and order of operations
a = 12
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

for i in range(1, a//b):
    print(i)
print()
print(a + b / 3 - 4 * 12)

# Order of Precedence examples
print(8 / 2 * 3)
print(8 * 3 / 2)

print((((a + b) / 3) - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

# String variables
parrot = "Norwegian Blue"
print(parrot)
print(parrot[0])
print(parrot[3])
print(parrot[-1])
print(parrot[0:6])
print(parrot[:6])
print(parrot[6:])
print(parrot[-4:-2])
print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,223,372,036,854,775,807"
print(number[1::4])

wholeNumbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(wholeNumbers[::3])

string1 = "He's "
string2 = "probably "
print(string1 + string2)
print("He's " "probably " "pining")
print("Hello " * 5)

today = "Monday"
print("day" in today)
print("Mon" in today)  # Case Sensitive
print("Thur" in today)
print("parrot" in "fjord")





