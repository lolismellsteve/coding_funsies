#what am i making? A program asks a user to either enter 1 or 2
#if the user enters 1, it says Hello World 
#If the user enters 2, it says Hello Universe
import math
import random
import sys


user_input = "Enter either a number 1 or 2"
print(user_input)
user_input = int(input())


if user_input == 1:
    print("Hello World")

if user_input == 2:
    print("Hello Universe")

#using this logic i could make something cool like what about a math test where
#if you get one question right it says Good job and onto next question and 
# if you get the next question wrong it generates a random number and you need to get three questions
#right to pass
counter = 0

def function():
    global counter
    counter += 1
    if counter == 3:
        print("You passed")
        sys.exit()
random_number1 = random.randint(1, 100)
random_number2 = random.randint(1, 100)


print("What is " + str(random_number1) + " + " + str(random_number2) + "?")
user_input = int(input())
if user_input == random_number1 + random_number2:
    print("Good job")
else:
    print("Try again")
    



function()
user_input = "What is"