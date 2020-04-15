# my_list = list(range(10))
# print(my_list)
#
# even = list(range(0,1000,2))
# odd = list(range(1,1000,2))
# print(even)
# print(odd)

# my_string = "abcdefghijklmnopqrstuvwxyz"
# print(my_string.index("e"))
# print(my_string[4])
#
# small_decimal = range(0,10)
# print(small_decimal)
# print(small_decimal.index(3))
#
# odd_list = range(1,10000,2)
# print(odd_list)
# print(odd_list[201])
# print(odd_list.index(101))
#
# sevens = range(7,1000,7)
# x = int(input("Please enter any number less than 1 thousand: "))
# if x in sevens:
#     print("{} is divisible by 7".format(x))
#
# print(small_decimal)
# my_range = small_decimal[::2]
# print(my_range)
# print(my_range.index(3))
# print(my_range[3])

decimals = range(0,100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)

print('-' * 40)

for i in range(3,40,3):
    print(i)