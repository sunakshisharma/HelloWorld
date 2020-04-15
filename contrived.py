# to check weather the numbers in the list are divisible by 8 or not.
numbers = [ 18, 33, 67, 15, 89, 79]

for number in numbers:
    if number % 8 == 0:
        print("The number are unacceptable. ")
        break
else:
    print("All those numbers are fine. ")
