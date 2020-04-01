# parrot = "Norwegian Blue"
#
# for character in parrot:
#     print((character))

# number = input("Please enter  a series of number , using any separators you like: ")
# seperators = ""
#
# for char in number:
#     if not char.isnumeric():
#         seperators = seperators + char
#
# print(seperators)
#
# values = "".join(char if char not in seperators else " " for char in number) .split()
# print(sum([int(val) for val in values]))

quote = """Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?"""
upper_char = ""

for char in quote:
    if char .isupper():
        upper_char = upper_char + char

print(upper_char)

