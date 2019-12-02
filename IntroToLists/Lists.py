__author__ = 'Michael E Miles'
# import PyPDF2 as p2

# ipAddress = input("Please enter and IP address: ")
# print(ipAddress.count("."))

parrotList = ["non pinin'", "no more", "a stiff", "bereft of life"]
parrotList.append("A Norwegian Blue")
for state in parrotList:
    print("This parrot is " + state)

evenNumbers = [2, 4, 6, 8, 10]
oddNumbers = [1, 3, 5, 7, 9, 11]

numbers = oddNumbers + evenNumbers
unsortedNumbers = numbers
print(numbers)
numbers.sort()
print(numbers)
print(sorted(unsortedNumbers))
