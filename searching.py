shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "Almond"
found_at = None

# for index in range(6)
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
# // The above type of code is not writing in python.the right way of writing code for this is below

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at the position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))