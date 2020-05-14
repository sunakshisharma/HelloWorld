try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

tkinter._test()

mainwindow = tkinter.Tk()

mainwindow.title("Hello World")
mainwindow.geometry('640x480+8+400')
lable = tkinter.Label(mainwindow, text= "Hello World")
lable.pack(side='top')

leftFrame = tkinter.Frame(mainwindow)
leftFrame.pack(side='left', anchor= 'n', fill= tkinter.Y, expand= False)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.pack(side='left', anchor= 'n')

rightFrame = tkinter.Frame(mainwindow)
rightFrame.pack(side='right', anchor= 'n', expand= True)

button1 = tkinter.Button(rightFrame,text= "Button1")
button2 = tkinter.Button(rightFrame,text= "Button2")
button3 = tkinter.Button(rightFrame,text= "Button3")
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

mainwindow.mainloop()