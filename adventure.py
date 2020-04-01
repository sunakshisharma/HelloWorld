# available_exits = [ "North", "South", "East", "West"]
#
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#
# print("Be happy you got out from there. ")
#
# available_exits = ["North", "South", "Up", "East", "West"]
#
# chosen_exit = ""
#
# while chosen_exit not in available_exits:
#     chosen_exit = input("please enter the direction: ")
#     if chosen_exit.casefold() == "quit":
#         print("Game Over ")
#         break
#         print("Be happy you got out from there")

for i in range(0,100,7):
    print(i)
    if  i > 0 and i % 11 == 0:
        break

