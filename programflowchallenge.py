option = {}

while option != 0:
    if option in range (1,5):
        print("Your choice is {}".format(option))
    else:
        print("""{}. Learn Python
{}. Learn Java
{}. Go swimming
{}. Have dinner 
{}. Exit """.format(1, 2, 3, 4, 0))
    option = int(input("Please choose your option from the list: "))



