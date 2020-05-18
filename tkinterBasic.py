import tkinter

mainwindow = tkinter.Tk()
button= tkinter.Button(mainwindow, text='Click Me', command=mainwindow.quit)
button.pack(side='left')

mainwindow.geometry('640x480-8-200')

leftframe= tkinter.LabelFrame(mainwindow, text='Window')
leftframe.pack(side='top')
canvas= tkinter.Canvas(mainwindow, relief='raised', borderwidth= 1)
canvas.pack(side='top', fill=tkinter.X)

rightframe= tkinter.LabelFrame(mainwindow, text='Window')
rightframe.pack(side='bottom')
canvas= tkinter.Canvas(mainwindow, relief='raised', borderwidth= 1)
canvas.pack(side='top', fill=tkinter.X)

button1= tkinter.Button(mainwindow, text="OK", command=mainwindow.quit)
button2= tkinter.Button(mainwindow, text="Cancel", command=mainwindow.quit)
button3= tkinter.Button(mainwindow, text="Apply", command=mainwindow.quit)
button1.pack(side='right')
button2.pack(side='right')
button3.pack(side='right')

mainwindow.mainloop()