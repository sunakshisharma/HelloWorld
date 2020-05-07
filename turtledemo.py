#!/Users/apple/venv/python3/bin/python
# import turtle
# import time
#
# turtle.forward(150)
# turtle.right(250)
# turtle.forward(150)
#
# time.sleep(4)

# from turtle import *
# #noinspection PyUnresolvedReferences
# forward(150)
# #noinspection PyUnresolvedReferences
# right(250)
# #noinspection PyUnresolvedReferences
# forward(150)
#
# done()
#
# print()

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
