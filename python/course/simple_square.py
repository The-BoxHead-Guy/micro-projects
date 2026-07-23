import time
from turtle import Screen, Turtle, mainloop

turtle = Turtle()
screen = Screen()

screen.setup(width=800, height=600)

turtle.speed(1)
turtle.color("black")

time.sleep(2)

for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

# The library itself, when it's imported completely contains a wrap of this method, in which it maintains the screen opened without being closed
# done = mainloop()
mainloop()
