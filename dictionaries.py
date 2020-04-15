fruit = {"orange": " a sweet, orange , citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# print(fruit)
# print(fruit["apple"])
#
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
#
# fruit["lemon"] = "great with tequila"
# print(fruit)
#
# del fruit["lemon"] # to delete the specific item from the dictionary
#
# fruit.clear() # to clear all the items from the dictionary
print(fruit)
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We don't have a " + dict_key)

        # or
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have a " + dict_key)
#     print(description)

# for i in range(10):
#         for snack in fruit:
#             print(snack + "is" + fruit[snack])
#         print('-' * 40)

# ordered_key = list(fruit.keys())
# ordered_key.sort()
# for f in ordered_key:
#     print(f + " - " + fruit[f])
# print()
#     #or
# ordered_key = sorted(list(fruit.keys()))
# for f in ordered_key:
#     print(f + " - " + fruit[f])
# print()
#or
# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])

# fruit_key = fruit.keys()
# print(fruit_key)
#
# fruit["Tomato"] = "not nice with icecream"
# print(fruit_key)

print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))
