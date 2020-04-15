# t = "a", "b", "c"
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))

welcome = "Welcome to my Nightmare" , "Alice Cooper" , 19475
bad = "Bad company" , "Bad company" , 1974
budgie = "Nightflight", "Budgie" , 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

#metallica[0] = "Master of puppets" -- this gives an error as we can change the value of variables in Tuple.
# But tuple allow indexing and slicing so we can do changes through this both


#the way to edit the valiables in tuple through indexing.
imelda = imelda[0] , "Imilda May", imelda[2]
print(imelda)

#comparing to List
metallica2 = ["Ride the Lightning", "Metallica", 1984]
print(metallica2)
metallica2[0] = "Master of puppets"
print(metallica2)

title, artist, year = imelda
print(title)
print(artist)
print(year)
# this called unpacking the tuple.