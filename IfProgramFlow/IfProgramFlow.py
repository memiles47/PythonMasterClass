__author__ = 'Michael E Miles'
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
if 16 <= age <= 65:
    print('Have a good day at work')
