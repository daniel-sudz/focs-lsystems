import turtle as turtle

win_width, win_height, bg_color = 100, 100, 'black'

turtle.setup()

t = turtle.Turtle()
s = turtle.Screen()

t.color(0.0, 0.0, 0.0)
t.pencolor(1.0, 1.0, 1.0)

s.bgcolor(0, 0, 0)

for _ in range(10000):
    t.forward(100)
    t.right(100)

s.exitonclick()
