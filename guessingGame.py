import math
import random
from random import random

rawnumber = random() * 10
number = math.floor(rawnumber)

chances = 5

print("Number Guessing Game")
print("Guess a number between 0 and 10")

while(chances <= 5):

    guess = int(input("Enter number:"))

    if(guess == number):
        print("Congratulations! You won!")

    else:
        chances = chances - 1
        print("Try again")
        print("Chances left: ")
        print(chances)

    if(chances == 0):
        print("Game Over. You Lost")
