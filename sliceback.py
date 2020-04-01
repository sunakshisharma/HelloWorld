#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"
#          65432109876543210987654321

backwards = letters[25:0:-1]
print(backwards)

backwards = letters[25::-1]
print(backwards)

backwards = letters[::-1] # is a python idiom for reversing the series
print(backwards)
print()

print(letters[16:13:-1])

print(letters[4::-1])

print(letters[:17:-1])

print(letters[:-9:-1])
# python idioms
print(letters[-4:]) # last 4 letters of the string
print(letters[-1:]) # last letter of the sting
print(letters[:1]) # first letter of thr string


