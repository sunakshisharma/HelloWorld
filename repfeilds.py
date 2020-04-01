age = 24
print("My age is " + str(age) + " years ")
print()

print("My age is {0} years " .format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7} " .format(31, "Jan", "Mar", "May", "July", "Aug", "Oct", "Dec"))

print("Jan:{1}, Feb:{0}, Mar:{1}, Apr:{2}, May:{1}, Jun:{2}, Jul:{1}, Aug:{1}, Sep:{2}, Oct:{1}, Nov:{2}, Dec:{1}" .format(28,31,30))
print()

print("""Jan:{1}, 
Feb:{0}
Mar:{1} 
Apr:{2} 
May:{1} 
Jun:{2}
Jul:{1} 
Aug:{1} 
Sep:{2} 
Oct:{1} 
Nov:{2} 
Dec:{1}""" .format(28,31,30))