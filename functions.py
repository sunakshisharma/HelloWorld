def python_food():
    width = 80
    text = "Spam and Eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


# def center_text(*args, sep=' ', end='\n', file=None, flush=False):
def center_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    # print(" " * left_margin, text, end= end, file=file, flush=flush)
    return " " * left_margin + text


# # with open("centered", mode='w') as centered_file:
# s1 = center_text("spam and Eggs")  # can do in this way as well
# print(s1)
# s2= center_text("Spam,Spam and Eggs")
# print(s2)
# print(center_text(12))
# print(center_text("Spam,Spam,Spam"))
# print(center_text("Spam", "1", "2", "3", "All", sep=":"))

with open("menu", mode='w') as menu:
    s1 = center_text("spam and Eggs")
    print(s1, file=menu)
    s2= center_text("Spam,Spam and Eggs")
    print(s2, file=menu)
    print(center_text(12), file=menu)
    print(center_text("Spam,Spam,Spam"), file=menu)
    s5 = center_text("Spam", "1", "2", "3", "All", sep=":")
    print(s5,  file=menu)
