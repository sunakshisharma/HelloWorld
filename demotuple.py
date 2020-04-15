# a = b = c = d = 12
# print(c)
#
# a, b = 12 , 13
# print(a, b)
#
# a, b = b, a
# print("a is {}".format(a))
# print("b is {}".format(b))

# welcome = "Welcome to my Nightmare" , "Alice Cooper" , 19475
# bad = "Bad company" , "Bad company" , 1974
# budgie = "Nightflight", "Budgie" , 1981
# imelda = "More Mayhem", "Emilda May", 2011,(1, "Pulling the Rug"), (2, "Psycho"),(3, "Mayhem"), (4, "Kentish Town Walts")
#
# print(imelda)
#
# title, artist, year, track1, track2, track3,  track4 = imelda
# print(title)
# print(artist)
# print(year)
# print(track1)
# print(track2)
# print(track3)
# print(track4)

# #challenge
# imelda = "More Mayhem", "Emilda May", 2011, (
#     (1, "Pulling the Rug"), (2, "Psycho"),(3, "Mayhem"), (4, "Kentish Town Walts"))
#
# print(imelda)
#
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
# print(tracks)
#
# for song in tracks:
#     track, title = song
#     print("Track number {} , Title: {}". format(track, title))

trees = ["Larch", "Larch"]
identified_trees = trees
identified_trees.append("chestnut")
print(trees)

numbers = range(0,20,2)
new_range = numbers[::-1]
print(new_range)

products = (('No. 5', 'perfume', 'Chanel'),
            ('Inflallible', 'cosmetic', "L'Oreal"),
            ('Poison', 'perfume', 'Dior'),
            ('Double Wear', 'cosmetic', 'Estee Lauder'),
            ('Wonder Wing', 'cosmetic', 'Rimmel London')
            )

for product in products:
    print(products[3])