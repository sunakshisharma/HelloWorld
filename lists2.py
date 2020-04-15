# list_1 = []
# list_2 = list()
#
# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("The lists are equal. ")
#
# print(list("123456789"))
# even =[2, 4, 6, 8]
# another_even = sorted(even, reverse=True)
#
# print(another_even is even)
# another_even.sort(reverse=True)
# print(even)
# even =[2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
# numbers = [even, odd]
# print(numbers)
#
# for number_set in numbers:
#     print(number_set)
#
#     for value in number_set:
#         print(value)

menu = []
menu.append(["Egg", "Spam", "Bacon"])
menu.append(["Egg", "Sausage", "Bacon"])
menu.append(["Egg", "Spam"])
menu.append(["Egg", "Bacon", "Spam"])
menu.append(["Egg", "Sausage"])
menu.append(["Egg", "Bacon", "Sausage", "Spam"])
menu.append(["Egg", "Spam", "Sausage", "Spam"])
# print(menu)

for meal in menu:
    if not "Spam" in meal:
        print(meal)

        for value in meal:
            print(value)
