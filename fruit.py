fruit = {"orange": " a sweet, orange , citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
print(fruit)

veg = {"cabbage": "every child's favourite ",
       "sprouts": "mmmmm , lovely",
       "spinach": "can i have some more fruit, please"}
print(veg)

veg.update(fruit)  # to add fruit dictionary to veg
print(veg)