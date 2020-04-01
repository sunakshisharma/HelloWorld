activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold(): # use for comparing strings that is case sensitive always .casefold lowercase the letter.
    print("But I want to go cinema. ")
else:
    print("Ok! Let's go. ")