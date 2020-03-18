#indexing
#         01234567891234
parrot = "Norwegian Blue"
#         43210987654321
print(parrot)

print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])
print()

print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
print()

print(parrot[3 - 14])
print(parrot[4- 14])
print(parrot[9- 14])
print(parrot[3- 14])
print(parrot[6- 14])
print(parrot[8- 14])

#slices
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
print(parrot[10:])
print(parrot[10:14])

print(parrot[:6] + parrot[6:])

print(parrot[:])

#negetive slices
print(parrot[-14:-5])
print(parrot[-8:7])
print(parrot[7:-5])

seprators = parrot[0:14:3]
print(seprators)
