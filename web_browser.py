import webbrowser
#
# # webbrowser.open("http://www.python.org/")
#
# help(webbrowser)

# for i in range(10):
#     print(1,2,3,4,5, sep=';', end=' ')

safari = webbrowser.get(using='safari')
safari.open_new("http://www.python.org/")