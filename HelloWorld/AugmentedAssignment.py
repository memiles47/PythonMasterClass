__author__ = 'Michael E Miles'
# import PyPDF2 as p2

number = "9,223,372,036,854,775.807"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber += number[i]  # Augmented Assignment

newNumber = int(cleanedNumber)
print('The number is: {}'.format(newNumber))

# Additional Augmented Assignment
x = 23
x += 1
print(x)

x -= 4
print(x)

x *= 5
print(x)

x /= 4
print(x)

x **= 2
print(x)

x %= 60
print(x)

greeting = 'Good '
greeting += 'Morning '
print(greeting)

greeting *= 5
print(greeting)

number = 5
multiplier = 8
answer = 0

for i in range(0, multiplier):
    answer += number
print(answer)
