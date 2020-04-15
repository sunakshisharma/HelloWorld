my_list = ["a", "b","c","d"]

newString = ''
for c in my_list:
    newString += c + ", "
print(newString)

#or

my_list = ["a", "b","c","d"]
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "123456789"

newString = " mississippi ".join(numbers)

print(newString)