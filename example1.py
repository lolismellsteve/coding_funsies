#what am i making? A program asks a user to either enter 1 or 2
#if the user enters 1, it says Hello World 
#If the user enters 2, it says Hello Universe
import math
import random
import sys




#using this logic i could make something cool like what about a math test where
#if you get one question right it says Good job and onto next question and 
# if you get the next question wrong it generates a random number and you need to get three questions
#right to pass
counter = 0
random_number1 = random.randint(1, 100)
random_number2 = random.randint(1, 100)
user_input = int(input("What is " + str(random_number1) + " + " + str(random_number2) + "?"))

    
def function():
    global counter
    prompt = input("What is " + str(random_number1) + " + " + str(random_number2) + "?")
    if prompt == random_number1 + random_number2:
        counter += 1
        print("Good job you have" + str(counter) + "points and you need to get three to win")
        counter += 1
        if counter == 3:
            print("You passed")
            sys.exit()
    else:
        print("Try again")
        counter -= 1
        print("You now have" + str(counter) + "points")
        function()
function()

        

        


    
    
