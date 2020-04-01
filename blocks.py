# for i in range(1, 10):
#    print("The square of no. {} and cube {} is {:4}" .format(i, i**2, i**3))
#    print("*" * 80)
# print()

name = input("Enter you name: ")
age = int(input("How old are you , {} ? : " .format(name)))
# if age >= 18:
#     print("Please Vote. ")
# elif age > 120:
#     print("Please write the correct age. ")
# else:
#     print("Please come after {} years to vote. ".format(18 - age))

if age < 18:
    print("Please come after {} years to vote. ".format(18 - age))
elif age > 120:
    print("Please write the correct age. ")
else:
    print("Please Vote. ")

print()

if x>y:
    print("x is greater than y ")

elif x<y:
    print("x is smaller than y ")

else:
    print("x equals y ")
