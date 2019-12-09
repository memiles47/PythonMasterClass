__author__ = 'Michael E Miles'

myList = list(range(10))
print(myList)

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

print(even)
print(odd)

myString = "abcdefghijklmnopqrstuvwxyz"
print(myString.index("e"))
print(myString[4])

smallDecimals = range(0, 10)
print(smallDecimals)

print(smallDecimals.index(3))

odd = range(1, 10000, 2)
print(odd)

print(odd[985])

sevens = range(7, 1000000, 7)
print("Please enter a positive number less than one million: ", end="")
x = int(input())

if x in sevens:
    print("{0} is divisible by seven, {0} / 7 = {1}".format(x, x/7))
else:
    print("{} is not divisible by seven".format(x))

print(smallDecimals)

myRange = smallDecimals[::2]
print(myRange)
print(myRange.index(4))

decimals = range(100)
print(decimals)

myRange = decimals[3:40:3]
print(myRange)

for i in myRange:
    print(i)

print("=" * 40)

for i in range(3, 40, 3):
    print(i)

print(myRange == range(3, 40, 3))
