for i in range(0, 10, 2):
    print("The value of i is {}" .format(i))

print()
for i in range(10, 0, -2):
    print("The value of i is {}" .format(i))

for i in range(0, 101,7): # prog for number divisible by 7 using range
    print(i)

# using slice
for i in range(101)[::7]:
    print(i)
