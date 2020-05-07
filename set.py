# farm_animal = {"sheep", "cow","hen"}
# print(farm_animal)
#
# for animal in farm_animal:
#     print(animal)
#
# print("#" * 40)
#
# wild_animal = set(["lion", "tiger", "panda", "elephant", "hare"])
# print(wild_animal)
#
# for animal in wild_animal:
#     print(animal)
#
# farm_animal.add("horse")
# wild_animal.add("horse")
# print(farm_animal)
# print(wild_animal)
#
# empty_set = set()   # to make empty set

# even = set(range(0,40,2))
# print(even)
# square_tuple = (4, 6, 9, 16, 25)
# squares = set(square_tuple)
# print(squares)

# union in sets :- merge both the set list.

# even = set(range(0,40,2))
# print(even)
# print(len(even))
#
# square_tuple = (4, 6, 9, 16, 25)
# squares = set(square_tuple)
# print(squares)
# print(len(square_tuple))
#
# print(even.union(squares))
# print(len(even.union(squares)))
# print(squares.union(even))
#
# print("#" * 40)
#
# # Intersection: common in both the set list
#
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)
#
# even = set(range(0,40,2))
# print(sorted(even))
# square_tuple = (4, 6, 9, 16, 25)
# squares = set(square_tuple)
# print(sorted(squares))

# # Minus:- remove the element commonly present and print the rest
# print("Even minus Squares")
# print(even.difference(squares))
# print(even - squares)
#
# print("Square minus Even")
# print(sorted(squares.difference(even)))
# print(sorted(squares - even))
#
# # to do minus in the original list
# print("#" * 40)
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))
#
# # Symmetric difference:- minus the elements commonly present in both list and print rest all element of both the list
# print("symmetric even minus squares")
# print(sorted(even.symmetric_difference(squares)))
#
# print("symmetric squares minus even")
# print(sorted(squares.symmetric_difference(even)))
#
# # there are 2 methods to remove items from the set:-
# # Remove and Discard:- diff is --  Romove gives an error if the item after going remove doesnt exist in the list but
# # discard does not give any error for the same
#
# squares.discard(4)
# squares.remove(16)
# squares.discard(8)  # no error
# print(squares)
#
# # squares.remove(8)
# # for make it work
#
# if 8 in squares:
#     squares.remove(8)

# Subset and Superset
# even = set(range(0,40,2))
# print(even)
# square_tuple = (4, 6, 16)
# squares = set(square_tuple)
# print(squares)
#
# if squares.issubset(even):
#     print("Squares is a subset of even")
#
# if even.issuperset(squares):
#     print("Even is a superset of squares")

# Frozen set :- once creatednot modified

# even = frozenset(range(0,40,2))
# print(even)






