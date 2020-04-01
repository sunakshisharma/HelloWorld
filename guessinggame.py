
# tree1 = 'Mango Tree'
# tree2 = 'Neem Tree'
#
# # add the code to compare the trees
# if tree1 == tree2:
#     print("The trees are same")
#
# else:
#     print("The trees are different")

import random

highest = 100
answer = random.randint(1, highest)
print(answer) # TODO: Remove after testing
guess = 0

print("Please enter number between 1 to {} : ". format(highest))

while guess != answer (10):
    guess = int(input())
    if guess == 0:
        break
    if guess == answer:
        print("Well done you guessed it correctly. ")
        break
    elif guess > answer:
        print("Guess something lower. ")
    else:
        print("Please guess higher")






