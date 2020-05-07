text = "Hello World"
final=set()
for letters in text:
    vowels = ["a","e","i","o","u"]
    if letters not in vowels:
        final.add(letters)
print(sorted(final))


print('*' * 40)

text = "Hello World"
vowels = frozenset("aeiou")

finalset = set(text).difference(vowels)
print(finalset)

finallist = sorted(finalset)
print(finallist)
