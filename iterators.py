string = "1234567890"

# for char in string:
#     print(char)

# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# for char in string:
#     print(char)
# print()
#
# for char in iter(string):
#     print(char)
# challenge
my_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
my_iterators = iter(my_list)

for i in range(0, len(my_list)):
    next_item = next(my_iterators)
    print(next_item)




