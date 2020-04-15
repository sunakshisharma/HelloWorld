# bike = {"make": "Honda", "model": "250 dream", "colour": "red", "engine_size": "250"}
#
# print(bike["engine_size"])
# print(bike["colour"])

locations = {0: "You are sitting in front of the computer learning Python",
             1: "You are sting at the end of the road before a small brick building",
             2: "You are at the top of the hill",
             3: "you are inside a building, a well house for a small stream",
             4: "You are in a valley beside the stream",
             5: "You are in a forest"}

exits = {{"Q" : 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1,"W": 2,"Q": 0},
         {"W": 2,"S": 1,"Q": 0}}

loc = 1
while True:
    availableExits = " , ".join(exit([loc].keys()))

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are" + availableExits + " ").upper()
    print()

    if direction in exits[loc]:
        loc = exits[loc][direction]

    else:
        print("You can not go in that direction. ")

