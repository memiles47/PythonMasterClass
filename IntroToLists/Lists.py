__author__ = 'Michael E Miles'
# import PyPDF2 as p2

# ipAddress = input("Please enter an IP address: ")
# print(ipAddress.count("."))

# parrotList = ["non pinin'", "no more", "a stiff", "bereft of life"]
# parrotList.append("A Norwegian Blue")
# for state in parrotList:
#     print("This parrot is " + state)
#
# evenNumbers = [2, 4, 6, 8, 10]
# oddNumbers = [1, 3, 5, 7, 9, 11]
#
# numbers = oddNumbers + evenNumbers
# unsortedNumbers = numbers
# print(numbers)
# print(sorted(numbers))
# print(numbers)
# numbers.sort()
# print(numbers)
# print(sorted(unsortedNumbers))

# list1 = []  # Creates an empty list using an empty list
# list2 = list()  # Creates an empty list using the list() constructor
#
# print("List 1: {}".format(list1))
# print("List 2: {}".format(list2))
#
# if list1 == list2:
#     print("The lists are equal")
#
# print(list("The lists are equal"))
#
# even = [2, 4, 6, 8]
#
# anotherEven = even
# anotherEven.sort(reverse=True)
# print(even)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)

for numbersSet in numbers:
    print(numbersSet)
    for value in numbersSet:
        print(value)
