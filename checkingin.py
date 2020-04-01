# parrot = "Norwegian Blue"
# letter = input("Enter the character: ")
#
# if letter in parrot:
#     print("{} is in {}" .format(letter, parrot))
# else:
#     print("I don't need a letter. ")
from datetime import date

name = input("Enter your name: ")
age = int(input(" Enter your age: "))

if 18 <= age <= 30:
    print("Welcome {} for the Holiday. ".format(name))
else:
    print("We are sorry {} but you are not eligible for this holiday. ".format(name))
