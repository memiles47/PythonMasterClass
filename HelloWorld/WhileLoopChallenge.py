__author__ = 'Michael E Miles'
# import PyPDF2 as p2
import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest), end="")
guess = int(input())

while guess != answer:
    print("Guess again")
