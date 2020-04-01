for i in range(1,8):
    print("Square of {0} is {1} and Cube is {2}" .format(i, i**2, i**3))
print()

for i in range(1,9):
    print("Square of {0:2} is {1:2} and Cube is {2:3}" .format(i, i**2, i**3)) # systamatic digit presentation in output

print()

for i in range(1,9):
    print("Square of {0:2} is {1:<2} and Cube is {2:<3}" .format(i, i**2, i**3)) # left side align digit presentation in output
# < for left allign
# > for right allign
# ^ for center allign
print()

print("Pie is approximately {0:12}" .format(22/7))
print("Pie is approximately {0:12f}" .format(22/7))
print("Pie is approximately {0:12.50f}" .format(22/7))
print("Pie is approximately {0:<52.50f}" .format(22/7))
print("Pie is approximately {0:<62.50f}" .format(22/7))
print("Pie is approximately {0:<72.50f}" .format(22/7))
print()

for i in range(1,9):
    print("Square of {} is {} and Cube is {:3}" .format(i, i**2, i**3))


