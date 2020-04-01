# without continue
for i in range(21):
    if i % 3 != 0 and i % 5 != 0:
        print(i)

# using continue
for x in range(21):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)