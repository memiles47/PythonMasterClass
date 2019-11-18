__author__ = 'Michael E Miles'
import PyPDF2 as p2
# name = input('Pleas enter your name: ')
# age = int(input('How old are you, {}? '.format(name)))
# print(age)
#
# if age >= 18:
#     print('You are old enough to vote')
#     print('Please put an " in the box.')
# else:
#     print('Please com back in {} years {}.'.format(18 - age, name))
# print('Please guess a number between 1 and 10: ')
# guess = int(input())
#
# if guess < 5:
#     print('Please guess higher')
#     guess = int(input())
#     if guess == 5:
#         print('Well done, you guessed it')
#     else:
#         print('Sorry, you have not guessed correctly.')
# elif guess > 5:
#     print('Please guess lower')
#     guess = int(input())
#     if guess == 5:
#         print('Well done, you guessed it')
#     else:
#         print('Sorry, you have not guessed correctly')
# else:
#     print('You got it the first time')

# More compact code
# if guess != 5:
#     if guess < 5:
#         print('Please guess higher')
#     else:
#         print('Please guess lower')
#     guess = int(input())
#     if guess == 5:
#         print('Well done, you guessed it')
#     else:
#         print('Sorry you have not guessed correctly')
# else:
#     print('You got it the first time')

# More complex if control code
age = int(input('How old are you? '))

# if (age >= 16) and (age <= 65):
# if 16 <= age <= 65:
#     print('Have a good day at work')
if (age < 16) or (age > 65):
    print('Enjoy your free time')
else:
    print('Have a good day at work')

x = 'false'  # This is the string, false
if x:  # This is checking is x is empty or not
    print('x is true')

print("""False: {0}
None: {1}
0: {2}
0.0: {3}
empty list []: {4}
empty tuple (): {5}
empty string '': {6}
empty string "": {7}
empty mapping {{}}: {8}
""".format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({})))

X = input('Please enter some text ')
if X:
    print('You enter "{}"'.format(X))
else:
    print('You did ot enter anything')

print(not True)
print(not False)

if not(age < 18):
    print("you are old enough to vote")
    print('Please put an X in the box')
else:
    print('Please come back in {} years'.format(18 - age))

parrot = 'Norwegian Blue'
letter = input('Enter a character: ')
if letter in parrot:
    print("Give me an {}, Bob".format(letter))
else:
    print("I don't need that letter")

# Challenge
x = 5
y = 7
if x == y:
    print('x equals y')
elif x > y:
    print('x is greater than y')
else:
    print('x is smaller than y')
