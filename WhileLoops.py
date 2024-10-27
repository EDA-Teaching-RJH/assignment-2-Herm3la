### Part Two -- your code goes here. 
import random

user = int(input("Guess a number between 1 and 100: "))
number = random.randint(1,101)

while True:
    if (user == number):
        print("Yes that is correct")
        break
    if (number > user):
        print("Try a higher number")
    if (number < user):
        print("Try a lower number")
    if (user != number):
        user = int(input("wrong try again: "))

