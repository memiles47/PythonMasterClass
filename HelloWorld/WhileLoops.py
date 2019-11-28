__author__ = 'Michael E Miles'
# It seems like you can keep using IdeaJ even after the expiration.
# import PyPDF2 as p2
import random

# for i in range(10):
#     print('i is now: {}'.format(i))

# i = 0
# while i < 10:
#     print('i is now: {}'.format(i))
#     i += 1

availableExits = ['EAST', 'NORTH EAST', 'SOUTH']

chosenExit = ''
while chosenExit not in availableExits:
    randomNumber = random.randint(1, 10)
    chosenExit = input('Please choose a direction: '.format(randomNumber)).upper()
    if chosenExit == "QUIT":
        print("Game Over")
        break
    print(randomNumber)
else:
    print("Aren't you glad you got out of there?")
