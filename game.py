locations = {0: "You are sitting in front of the computer learning Python",
             1: "You are sting at the end of the road before a small brick building",
             2: "You are at the top of the hill",
             3: "you are inside a building, a well house for a small stream",
             4: "You are in a valley beside the stream",
             5: "You are in a forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

namedExits = {
              1: {"2":2,"3":3,"5":5,"4":4},
              2: {"5":5},
              3: {"1":1},
              4: {"1":1,"2":2},
              5: {"2":2,"1":1}}
vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY":"4"}


loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break
    allExits = exits[loc].copy()
    allExits.update(namedExits[loc])

    direction = input("Available exits are: " + availableExits + " ").upper()
    print()

    if len(direction) > 1:

        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You can not go in that direction")
