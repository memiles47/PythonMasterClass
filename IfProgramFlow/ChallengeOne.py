__author__ = 'Michael E Miles'
# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31.
# if they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

name = input('What is your name? ')
age = int(input('How old are you {}? '.format(name)))

if 18 <= age <= 30:
    print('Hello {} and welcome to the 18-30 holiday'.format(name))
else:
    print("I'm sorry {} but you are not the proper age for this holiday".format(name))


# Challenge complete and correct
