__author__ = 'Michael E Miles'
# import PyPDF2 as p2
import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {} (enter 0 'zero' to quit: ".format(highest), end="")
guess = int(input())

while guess != answer:
    if guess == 0:
        print("You Chicken!")
        break
    if guess < answer:
        print("Please guess higher: ", end="")
        guess = int(input())
    else:
        print("Please guess lower: ", end="")
        guess = int(input())
else:
    print("Good Job! The answer is {}".format(guess))
