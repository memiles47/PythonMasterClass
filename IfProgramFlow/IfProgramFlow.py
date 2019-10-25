__author__ = 'Michael E Miles'
name = input('Pleas enter your name: ')
age = int(input('How old are you, {}? '.format(name)))
print(age)

if age >= 18:
    print('You are old enough to vote')
    print('Please put an " in the box.')
else:
    print('Please com back in {} years {}.'.format(18 - age, name))
