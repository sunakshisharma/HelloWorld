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
vocabulary = {"Quit": "Q",
              "North": "N",
              "South": "S",
              "East": "E",
              "West": "W", }

# print(locations[0].split())
# print(locations[3].split())
# print(" ".join(locations[0].split()))

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are: " + availableExits + " ").upper()
    print()
    # parse the input , using vocabulary dictionary if necessary
    if len(direction) > 1:   # more than 1 letter , so check vocab
        # for word in  vocabulary:   # does it contain a word we know
        #     if word in direction:
        #         direction = vocabulary[word]
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You can not go in that direction")
