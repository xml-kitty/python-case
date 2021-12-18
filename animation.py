import turtle
import time

turtle.pensize(5)
turtle.tracer(0)

for i in range(4):
    turtle.forward(1)
    turtle.update()
    time.sleep(1/30)

turtle.done()
