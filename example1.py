#what am i making? A program asks a user to either enter 1 or 2
#if the user enters 1, it says Hello World 
#If the user enters 2, it says Hello Universe

user_input = "Enter either a number 1 or 2"
print(user_input)
user_input = int(input())


if user_input == 1:
    print("Hello World")

if user_input == 2:
    print("Hello Universe")
