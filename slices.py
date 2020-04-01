letters = "abcdefghijklmnopqrstuvwxyz"

print(letters[18])
print(letters[20])
print(letters[13])
print(letters[0])
print(letters[10])
print(letters[18])
print(letters[7])
print(letters[8])

print((letters[18] + (letters[20]) + (letters[13]) + (letters[0]) + (letters[10]) + (letters[18]) +
            (letters[7]) + (letters[8])))


print(letters[:3]+"-"+ letters[3:])
print(letters[:])
print()
#step in slices

#seperators = letters[0:5]
#print(seperators)
#values = "".join(char if char not in seperators else " " for char in letters) .split()
#print([int(val) for val in values])

seprators = '-'.join(letters[i:i+3] for i in range(0, len(letters), 3))
print(seprators)
